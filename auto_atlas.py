#!/usr/bin/env python3
"""Re-slice every character sprite sheet into an atlas JSON.

The Gemini-generated PNGs use a magenta (#ff00ff) background with characters
arranged in even row bands and per-frame cells inside each row. This script
finds the row bands by horizontal magenta gutters, then finds cells inside
each row by vertical magenta gutters, then names the rows in the order
declared by EXPECTED_SLOTS for that character.

Usage:
    python3 auto_atlas.py            # re-slice every character
    python3 auto_atlas.py shade rig  # re-slice only the named ones
"""
import json
import os
import sys
import numpy as np
from PIL import Image

CHAR_DIR = "characters"

# Order MUST match the REQUIRED ANIMATION ROWS lists in each spec.
EXPECTED_SLOTS = {
    "rio":       ["idle","walk","run","jump","atk1","atk2","atk3","atk4","heavy","jump_atk","back_atk","special","throw","counter","hurt","dodge"],
    "duke":      ["idle","walk","run","jump","atk1","atk2","atk3","atk4","heavy","jump_atk","back_atk","special","throw","counter","hurt","dodge"],
    "atlas":     ["idle","walk","run","jump","atk1","atk2","atk3","heavy","jump_atk","back_atk","special","throw","counter","hurt","dodge"],
    "baron":     ["idle","walk","atk1","atk2","atk3","heavy","jump_atk","back_atk","special","throw","counter","hurt"],
    "razor":     ["idle","walk","atk1","atk2","atk3","heavy","jump_atk","back_atk","special","throw","counter","hurt"],
    "volt":      ["idle","walk","atk1","atk2","atk3","heavy","jump_atk","back_atk","special","throw","counter","hurt"],
    "blackwell": ["idle","walk","atk1","atk2","atk3","heavy","jump_atk","back_atk","special","throw","counter","hurt"],
    "runner":    ["idle","walk","run","atk1","atk2","hurt","dead","flee"],
    "chains":    ["idle","walk","atk1","atk2","atk3","hurt","dead"],
    "slice":     ["idle","walk","run","atk1","atk2","jump_atk","dash","hurt","dead"],
    "tank":      ["idle","walk","atk1","atk2","atk3","hurt","dead"],
    "lamplight": ["idle","walk","atk1","atk2","atk3","atk4","atk5","hurt","dead"],
    "dojo":      ["idle","walk","atk1","atk2","atk3","atk4","hurt","dead"],
    "shade":     ["idle","walk","atk1","atk2","atk3","atk4","atk5","atk6","vanish","reappear","hurt","dead"],
    "rig":       ["idle","walk","atk1","atk2","atk3","atk4","atk5","atk6","hurt","dead"],
}


def load_mask(path):
    """Load image as a boolean foreground mask (True where the character is)."""
    im = Image.open(path).convert("RGBA")
    arr = np.array(im)  # (H, W, 4)
    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    # Magenta tolerance (Gemini sometimes outputs e.g. #ff03f4).
    is_magenta = (r > 220) & (g < 60) & (b > 220)
    is_transparent = a < 16
    fg = ~(is_magenta | is_transparent)
    return fg, arr


def find_row_bands(fg, min_gap=2, min_height=20, gap_threshold=60):
    """Return list of (y0, y1) row bands containing characters.

    A row counts as 'gap' if it has fewer than `gap_threshold` foreground
    pixels (small enough to be compression noise or hairline stragglers).
    A band closes when `min_gap` consecutive gap rows are seen.
    """
    row_has_fg = fg.sum(axis=1) >= gap_threshold
    bands = []
    in_band = False
    y0 = 0
    H = len(row_has_fg)
    y = 0
    while y < H:
        if row_has_fg[y] and not in_band:
            y0 = y
            in_band = True
            y += 1
        elif not row_has_fg[y] and in_band:
            # Look ahead `min_gap` rows; if all empty, close the band.
            empty = all((y + k < H and not row_has_fg[y + k]) for k in range(min_gap))
            if empty:
                if y - y0 >= min_height:
                    bands.append((y0, y))
                in_band = False
            y += 1
        else:
            y += 1
    if in_band and H - y0 >= min_height:
        bands.append((y0, H))
    return bands


def find_cells_in_row(fg, y0, y1, min_gap=3, min_width=10):
    """Return list of (x0, y0, x1, y1) cell bounding boxes inside a row."""
    sub = fg[y0:y1]
    col_has_fg = sub.sum(axis=0) > 2
    cells = []
    in_cell = False
    x0 = 0
    W = len(col_has_fg)
    for x in range(W):
        if col_has_fg[x] and not in_cell:
            x0 = x
            in_cell = True
        elif not col_has_fg[x] and in_cell:
            if all(not col_has_fg[x + k] for k in range(min_gap) if x + k < W):
                if x - x0 >= min_width:
                    cells.append([x0, x])
                in_cell = False
    if in_cell and W - x0 >= min_width:
        cells.append([x0, W])
    # Refine vertical extent for each cell so the tight bbox is per-cell.
    out = []
    for cx0, cx1 in cells:
        col_slice = fg[y0:y1, cx0:cx1]
        row_has = col_slice.sum(axis=1) > 0
        if not row_has.any():
            continue
        ys = np.where(row_has)[0]
        ty0 = y0 + int(ys.min())
        ty1 = y0 + int(ys.max()) + 1
        # Also tighten horizontally inside the cell.
        col_has = col_slice.sum(axis=0) > 0
        xs = np.where(col_has)[0]
        tx0 = cx0 + int(xs.min())
        tx1 = cx0 + int(xs.max()) + 1
        out.append((tx0, ty0, tx1, ty1))
    return out


def slice_sheet(png_path, expected_slots):
    fg, _ = load_mask(png_path)
    bands = find_row_bands(fg)
    frames = {}
    anims = {}
    n_slots = len(expected_slots)
    n_bands = len(bands)
    if n_bands == 0:
        return None, n_bands, 0
    used_slots = expected_slots[:n_bands]
    for i, (y0, y1) in enumerate(bands):
        slot = used_slots[i] if i < n_slots else f"row{i}"
        cells = find_cells_in_row(fg, y0, y1)
        if not cells:
            continue
        names = []
        for j, (x0, ty0, x1, ty1) in enumerate(cells):
            key = f"{slot}_{j}"
            frames[key] = {"x": int(x0), "y": int(ty0), "w": int(x1 - x0), "h": int(ty1 - ty0)}
            names.append(key)
        anims[slot] = names
    atlas = {
        "fps": 8,
        "frames": frames,
        "anims": anims,
        "anchor": {"x": 0.5, "y": 1.0},
    }
    return atlas, n_bands, sum(len(v) for v in anims.values())


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else sorted(EXPECTED_SLOTS.keys())
    print(f"Re-slicing {len(targets)} sheet(s)...")
    print()
    for name in targets:
        png = os.path.join(CHAR_DIR, f"{name}.png")
        out = os.path.join(CHAR_DIR, f"{name}_atlas.json")
        if not os.path.exists(png):
            print(f"  SKIP   {name:11}  no PNG at {png}")
            continue
        if name not in EXPECTED_SLOTS:
            print(f"  SKIP   {name:11}  not in EXPECTED_SLOTS")
            continue
        expected = EXPECTED_SLOTS[name]
        atlas, n_bands, n_frames = slice_sheet(png, expected)
        if atlas is None:
            print(f"  FAIL   {name:11}  no row bands found")
            continue
        # Backup existing.
        if os.path.exists(out):
            with open(out + ".bak", "w") as f:
                with open(out) as orig:
                    f.write(orig.read())
        with open(out, "w") as f:
            json.dump(atlas, f, indent=2)
        ok = "OK   " if n_bands == len(expected) else "WARN "
        slot_str = ",".join(atlas["anims"].keys())
        print(f"  {ok}  {name:11}  {n_bands}/{len(expected)} rows  {n_frames} frames  -> {slot_str}")


if __name__ == "__main__":
    main()
