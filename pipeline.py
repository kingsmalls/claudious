#!/usr/bin/env python3
"""
THE BLOCK — asset pipeline.

Subcommands:
  validate-atlas <atlas.json>          Check required anims + frame integrity.
  extract-palette <image.png>          Print top N colors (uses Pillow if installed).
  manifest [<dir>]                     SHA-256 manifest of project assets.
  release <output.zip>                 Bundle the release (the_block.html + atlas pairs).
  process-sheet <input.png>            Slice a uniform sprite sheet into atlas + packed PNG.
                                       (Used as the export step from sprite_slicer.html.)
  build-atlas <layout.json>            Generate an atlas JSON from a per-anim layout config
                                       (row + col + frame count per anim slot). For sheets
                                       that already have row-by-row anim labels.

The procedural fallback in the_block.html means atlases are optional —
this tool helps you maintain them when they exist. Pure stdlib by default;
Pillow optional, only required for palette extraction and process-sheet.
"""

import argparse
import hashlib
import json
import os
import sys
import zipfile
from collections import Counter
from pathlib import Path

# Animations the renderer can use. Anything missing falls back to the
# procedural path for that animation only.
REQUIRED_ANIMS = [
    "idle", "walk", "run", "jump",
    "atk1", "atk2", "atk3", "heavy", "jump_atk", "back_atk",
    "special", "throw", "counter", "hurt", "dodge",
]
CHARS = ["rio", "duke", "atlas"]


# ---------- validate-atlas ----------

def cmd_validate_atlas(args):
    path = Path(args.path)
    if not path.exists():
        print(f"[validate] no such file: {path}", file=sys.stderr)
        return 1
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        print(f"[validate] {path}: invalid JSON: {e}", file=sys.stderr)
        return 1

    errors = []
    warnings = []
    if "frames" not in data:
        errors.append("missing 'frames'")
    if "anims" not in data:
        errors.append("missing 'anims'")
    frames = data.get("frames", {})
    anims = data.get("anims", {})

    for k, frame in frames.items():
        if not isinstance(frame, dict):
            errors.append(f"frame {k!r}: not an object")
            continue
        for f in ("x", "y", "w", "h"):
            if f not in frame:
                errors.append(f"frame {k!r}: missing {f}")
        if frame.get("w", 0) <= 0 or frame.get("h", 0) <= 0:
            errors.append(f"frame {k!r}: non-positive size")

    for need in REQUIRED_ANIMS:
        if need not in anims:
            warnings.append(f"missing anim '{need}' (procedural fallback will draw it)")

    for name, frame_list in anims.items():
        if not isinstance(frame_list, list):
            errors.append(f"anim {name!r}: not a list")
            continue
        if not frame_list:
            warnings.append(f"anim {name!r}: empty frame list")
        for f in frame_list:
            if f not in frames:
                errors.append(f"anim {name!r}: frame {f!r} not in frames table")

    print(f"[validate] {path}")
    for e in errors:
        print(f"  ERROR  {e}")
    for w in warnings:
        print(f"  WARN   {w}")
    if not errors and not warnings:
        print("  OK")
    print(f"  {len(frames)} frames, {len(anims)} animations")
    return 1 if errors else 0


# ---------- extract-palette ----------

def cmd_extract_palette(args):
    path = Path(args.path)
    if not path.exists():
        print(f"[palette] no such file: {path}", file=sys.stderr)
        return 1
    try:
        from PIL import Image
    except ImportError:
        print("[palette] Pillow not installed — pip install Pillow for color extraction.")
        print(f"  (skipping {path})")
        return 0
    img = Image.open(path).convert("RGBA")
    pixels = list(img.getdata())
    counter = Counter(p for p in pixels if p[3] > 0)
    total = sum(counter.values()) or 1
    print(f"[palette] {path}  ({img.width}x{img.height}, {total} opaque px)")
    for color, count in counter.most_common(args.top):
        hex_code = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        bar = "#" * max(1, int(count * 30 / total))
        print(f"  {hex_code}  {count:>8}  {count * 100 / total:5.1f}%  {bar}")
    return 0


# ---------- manifest ----------

def cmd_manifest(args):
    root = Path(args.dir or ".")
    rows = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        # Skip dotfiles, node_modules, zip outputs, and smoke-test screenshots.
        skip = False
        for part in p.parts:
            if part.startswith(".") or part == "node_modules":
                skip = True
                break
        if skip:
            continue
        if p.suffix.lower() == ".zip":
            continue
        # Test artifacts.
        if p.name.startswith("shot_") and p.suffix.lower() == ".png":
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        rows.append((str(p.relative_to(root)), h, p.stat().st_size))
    print(f"[manifest] {root}")
    for rel, h, size in rows:
        print(f"  {h[:12]}  {size:>9}  {rel}")
    print(f"  ({len(rows)} files)")
    return 0


# ---------- release ----------

def cmd_release(args):
    output = Path(args.output)
    bundle_files = []
    # Always include the main HTML file.
    main_html = Path("the_block.html")
    if not main_html.exists():
        print(f"[release] {main_html} not found — run from project root", file=sys.stderr)
        return 1
    bundle_files.append(main_html)
    # Bundle character atlas pairs that exist.
    for c in CHARS:
        for ext in (".png", "_atlas.json"):
            f = Path(c + ext)
            if f.exists():
                bundle_files.append(f)
    # Bundle sprite slicer + landing page if present.
    for extra in ["sprite_slicer.html", "landing.html", "README.md"]:
        f = Path(extra)
        if f.exists():
            bundle_files.append(f)

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as z:
        for f in bundle_files:
            z.write(f, arcname=f.name)
    print(f"[release] wrote {output} ({output.stat().st_size} bytes)")
    for f in bundle_files:
        print(f"  + {f.name}")
    return 0


# ---------- process-sheet ----------

def cmd_process_sheet(args):
    try:
        from PIL import Image
    except ImportError:
        print("[process-sheet] requires Pillow (pip install Pillow)", file=sys.stderr)
        return 1
    sheet_path = Path(args.input)
    if not sheet_path.exists():
        print(f"[process-sheet] no such file: {sheet_path}", file=sys.stderr)
        return 1
    sheet = Image.open(sheet_path).convert("RGBA")
    fw, fh = args.width, args.height
    if sheet.width % fw or sheet.height % fh:
        print(f"[process-sheet] sheet {sheet.width}x{sheet.height} is not a clean multiple "
              f"of {fw}x{fh} — output may include partial frames",
              file=sys.stderr)
    cols = sheet.width // fw
    rows_n = sheet.height // fh
    frames = {}
    for j in range(rows_n):
        for i in range(cols):
            name = f"frame_{j:02d}_{i:02d}"
            frames[name] = {"x": i * fw, "y": j * fh, "w": fw, "h": fh}
    sheet.save(args.output_png)
    out_atlas = {
        "fps": args.fps,
        "frames": frames,
        # Stub anims; user fills in real ones via sprite_slicer.html or by hand.
        "anims": {"idle": [next(iter(frames.keys()))]} if frames else {},
        "anchor": {"x": 0.5, "y": 1.0},
    }
    Path(args.output_atlas).write_text(json.dumps(out_atlas, indent=2))
    print(f"[process-sheet] saved {args.output_png} + {args.output_atlas}")
    print(f"  {len(frames)} frames at {fw}x{fh}, {cols} columns × {rows_n} rows")
    return 0


# ---------- build-atlas ----------
# Consumes a small JSON layout config that names each animation slot's
# starting cell and frame count on a uniform-grid sheet. Outputs a full
# atlas JSON ready for the engine.
#
# Layout config schema:
#   {
#     "sheet":       "rio.png",        // source PNG (informational only)
#     "cell_width":  64,
#     "cell_height": 96,
#     "fps":         8,                // optional, default 8
#     "anchor":      { "x": 0.5, "y": 1.0 },   // optional, default bottom-center
#     "anims": {
#       "idle":     { "row": 0, "col": 0, "count": 4 },
#       "walk":     { "row": 0, "col": 4, "count": 6 },
#       "run":      { "row": 0, "col": 10, "count": 6 },
#       "jump":     { "row": 1, "col": 0, "count": 3 },
#       "atk1":     { "row": 1, "col": 3, "count": 4 },
#       ...
#     }
#   }
#
# Wraps to the next row automatically if (col + count) overflows the sheet
# width, but it's clearer to keep each anim within a single row. Frames are
# named "<anim>_<index>" in the output atlas.

def cmd_build_atlas(args):
    layout_path = Path(args.layout)
    if not layout_path.exists():
        print(f"[build-atlas] no such file: {layout_path}", file=sys.stderr)
        return 1
    try:
        layout = json.loads(layout_path.read_text())
    except json.JSONDecodeError as e:
        print(f"[build-atlas] {layout_path}: invalid JSON: {e}", file=sys.stderr)
        return 1

    cw = layout.get("cell_width")
    ch = layout.get("cell_height")
    if not (isinstance(cw, int) and isinstance(ch, int) and cw > 0 and ch > 0):
        print("[build-atlas] cell_width and cell_height must be positive integers",
              file=sys.stderr)
        return 1

    anims_in = layout.get("anims") or {}
    if not anims_in:
        print("[build-atlas] no anims defined in layout", file=sys.stderr)
        return 1

    # Optional sheet width/height in cells, for overflow detection only.
    sheet_path = layout.get("sheet")
    sheet_cols = None
    if sheet_path:
        try:
            from PIL import Image
            spath = layout_path.parent / sheet_path
            if spath.exists():
                with Image.open(spath) as im:
                    sheet_cols = im.width // cw
        except ImportError:
            pass  # overflow detection skipped without Pillow

    frames = {}
    anims_out = {}
    for anim_name, spec in anims_in.items():
        row = spec.get("row")
        col = spec.get("col")
        count = spec.get("count")
        if not all(isinstance(v, int) and v >= 0 for v in (row, col, count)) or count == 0:
            print(f"[build-atlas] anim '{anim_name}': row/col/count must be non-negative ints "
                  f"with count > 0", file=sys.stderr)
            return 1
        seq = []
        for i in range(count):
            cur_col = col + i
            cur_row = row
            if sheet_cols and cur_col >= sheet_cols:
                cur_row += cur_col // sheet_cols
                cur_col = cur_col % sheet_cols
            fname = f"{anim_name}_{i}"
            frames[fname] = {
                "x": cur_col * cw,
                "y": cur_row * ch,
                "w": cw,
                "h": ch,
            }
            seq.append(fname)
        anims_out[anim_name] = seq

    out = {
        "fps": layout.get("fps", 8),
        "frames": frames,
        "anims": anims_out,
        "anchor": layout.get("anchor", {"x": 0.5, "y": 1.0}),
    }
    Path(args.output).write_text(json.dumps(out, indent=2))
    missing = [a for a in REQUIRED_ANIMS if a not in anims_out]
    print(f"[build-atlas] wrote {args.output} — {len(frames)} frames, {len(anims_out)} anims")
    if missing:
        print(f"[build-atlas] note: anim slots missing (will fall back to procedural): "
              f"{', '.join(missing)}")
    return 0


# ---------- entry point ----------

def main():
    p = argparse.ArgumentParser(description="THE BLOCK — asset pipeline")
    sp = p.add_subparsers(dest="cmd", required=True)

    a = sp.add_parser("validate-atlas", help="check an atlas JSON for completeness")
    a.add_argument("path")
    a.set_defaults(func=cmd_validate_atlas)

    a = sp.add_parser("extract-palette", help="print top palette colors of an image")
    a.add_argument("path")
    a.add_argument("--top", type=int, default=16,
                   help="how many colors to print (default 16)")
    a.set_defaults(func=cmd_extract_palette)

    a = sp.add_parser("manifest", help="SHA-256 manifest of project assets")
    a.add_argument("dir", nargs="?", help="directory to walk (default cwd)")
    a.set_defaults(func=cmd_manifest)

    a = sp.add_parser("release", help="bundle release zip")
    a.add_argument("output", help="output .zip path")
    a.set_defaults(func=cmd_release)

    a = sp.add_parser("build-atlas", help="generate atlas JSON from a per-anim layout config")
    a.add_argument("layout", help="layout config JSON (sheet, cell size, anim row/col/count)")
    a.add_argument("--output", "-o", required=True, help="output atlas JSON path")
    a.set_defaults(func=cmd_build_atlas)

    a = sp.add_parser("process-sheet", help="slice a uniform sprite sheet into an atlas")
    a.add_argument("input", help="input PNG sprite sheet")
    a.add_argument("--output-png",   required=True, help="copy/cleaned output PNG path")
    a.add_argument("--output-atlas", required=True, help="output atlas JSON path")
    a.add_argument("--width",  type=int, default=32, help="frame width in pixels")
    a.add_argument("--height", type=int, default=48, help="frame height in pixels")
    a.add_argument("--fps",    type=int, default=8,  help="default playback fps")
    a.set_defaults(func=cmd_process_sheet)

    args = p.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
