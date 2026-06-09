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
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d

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

# Target on-screen cell HEIGHT in CSS / engine pixels. The Gemini-regenerated
# sheets are 3-4x larger than the originals, which makes the sprites render
# enormous when drawn at native frame size. The engine scales each frame's
# render size to match this target.
TARGET_CELL_H = {
    "rio": 96, "duke": 96, "atlas": 112,
    "baron": 96, "razor": 96, "volt": 96, "blackwell": 96,
    "runner": 64, "chains": 80, "slice": 80, "tank": 96,
    "lamplight": 88, "dojo": 80, "shade": 72, "rig": 80,
}

# Expected frame count per anim slot. Used to force uniform cell division
# when the magenta gutters between cells in a row are too noisy for the
# gap-based detector to find reliably.
EXPECTED_FRAMES = {
    "rio": {"idle":4,"walk":6,"run":6,"jump":3,"atk1":4,"atk2":5,"atk3":6,"atk4":6,"heavy":7,"jump_atk":4,"back_atk":4,"special":12,"throw":5,"counter":6,"hurt":3,"dodge":5},
    "duke": {"idle":4,"walk":6,"run":6,"jump":3,"atk1":4,"atk2":5,"atk3":6,"atk4":6,"heavy":7,"jump_atk":4,"back_atk":4,"special":12,"throw":5,"counter":6,"hurt":3,"dodge":5},
    "atlas": {"idle":4,"walk":6,"run":6,"jump":3,"atk1":4,"atk2":5,"atk3":6,"heavy":7,"jump_atk":4,"back_atk":4,"special":12,"throw":5,"counter":6,"hurt":3,"dodge":5},
    "baron": {"idle":4,"walk":6,"atk1":4,"atk2":5,"atk3":5,"heavy":7,"jump_atk":4,"back_atk":4,"special":12,"throw":5,"counter":6,"hurt":3},
    "razor": {"idle":4,"walk":6,"atk1":4,"atk2":5,"atk3":6,"heavy":7,"jump_atk":4,"back_atk":4,"special":12,"throw":5,"counter":6,"hurt":3},
    "volt": {"idle":4,"walk":6,"atk1":4,"atk2":5,"atk3":6,"heavy":7,"jump_atk":4,"back_atk":4,"special":12,"throw":5,"counter":6,"hurt":3},
    "blackwell": {"idle":4,"walk":6,"atk1":4,"atk2":5,"atk3":6,"heavy":7,"jump_atk":4,"back_atk":4,"special":12,"throw":5,"counter":6,"hurt":3},
    "runner": {"idle":4,"walk":6,"run":4,"atk1":4,"atk2":4,"hurt":3,"dead":3,"flee":4},
    "chains": {"idle":4,"walk":6,"atk1":6,"atk2":5,"atk3":12,"hurt":3,"dead":3},
    "slice": {"idle":4,"walk":6,"run":4,"atk1":6,"atk2":5,"jump_atk":5,"dash":4,"hurt":3,"dead":3},
    "tank": {"idle":4,"walk":6,"atk1":6,"atk2":7,"atk3":7,"hurt":3,"dead":3},
    "lamplight": {"idle":4,"walk":6,"atk1":5,"atk2":8,"atk3":6,"atk4":7,"atk5":5,"hurt":3,"dead":4},
    "dojo": {"idle":4,"walk":6,"atk1":6,"atk2":6,"atk3":6,"atk4":6,"hurt":3,"dead":3},
    "shade": {"idle":4,"walk":6,"atk1":4,"atk2":4,"atk3":5,"atk4":5,"atk5":5,"atk6":6,"vanish":5,"reappear":3,"hurt":3,"dead":4},
    "rig": {"idle":4,"walk":6,"atk1":5,"atk2":5,"atk3":5,"atk4":6,"atk5":6,"atk6":12,"hurt":3,"dead":4},
}


def load_mask(path):
    """Load image as a boolean foreground mask (True where the character is).

    Treats both magenta (#ff00ff) and near-black borders (Gemini sometimes
    wraps sheets in a black frame) as background.
    """
    im = Image.open(path).convert("RGBA")
    arr = np.array(im)  # (H, W, 4)
    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    # Magenta with widened tolerance for JPEG-style compression noise.
    is_magenta = (r > 200) & (g < 100) & (b > 200) & (r.astype(int) + b.astype(int) - 2 * g.astype(int) > 200)
    # Near-black border / letterboxing.
    is_dark = (r < 25) & (g < 25) & (b < 25)
    is_transparent = a < 16
    fg = ~(is_magenta | is_dark | is_transparent)
    return fg, arr


def crop_to_content(fg):
    """Return (y0, y1, x0, x1) bounding box of the entire content region.

    Useful when Gemini wraps the magenta sheet in a black letterbox border
    — the band detector would otherwise see no magenta gutters at all.
    """
    rows = fg.any(axis=1)
    cols = fg.any(axis=0)
    if not rows.any():
        return None
    y0 = int(np.argmax(rows))
    y1 = int(len(rows) - np.argmax(rows[::-1]))
    x0 = int(np.argmax(cols))
    x1 = int(len(cols) - np.argmax(cols[::-1]))
    return (y0, y1, x0, x1)


def find_row_bands(fg, min_gap=2, min_height=20, gap_ratio=0.05):
    """Return list of (y0, y1) row bands containing characters.

    A row counts as 'gap' if fewer than `gap_ratio` of the row's pixels are
    foreground (large enough to filter out the constant compression noise
    that Gemini's PNG output sprinkles across magenta gutters). A band
    closes when `min_gap` consecutive gap rows are seen.
    """
    W = fg.shape[1]
    gap_threshold = max(40, int(W * gap_ratio))
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


def find_cells_in_row(fg, y0, y1, expected_cells=None, min_gap=2, min_width=10, gap_ratio=0.05):
    """Return list of (x0, y0, x1, y1) cell bounding boxes inside a row.

    If `expected_cells` is given and gap-based detection produces fewer
    cells than that, fall back to uniform column division. Each detected
    cell's bounding box is tightened around the actual non-magenta pixels.
    """
    sub = fg[y0:y1]
    H_band = y1 - y0
    col_gap_threshold = max(8, int(H_band * gap_ratio))
    col_has_fg = sub.sum(axis=0) >= col_gap_threshold
    cells = []
    in_cell = False
    x0 = 0
    W = len(col_has_fg)
    x = 0
    while x < W:
        if col_has_fg[x] and not in_cell:
            x0 = x
            in_cell = True
            x += 1
        elif not col_has_fg[x] and in_cell:
            empty = all((x + k < W and not col_has_fg[x + k]) for k in range(min_gap))
            if empty:
                if x - x0 >= min_width:
                    cells.append([x0, x])
                in_cell = False
            x += 1
        else:
            x += 1
    if in_cell and W - x0 >= min_width:
        cells.append([x0, W])

    # When expected_cells is known, find character centers via peak detection
    # on the column-density signal. The Gemini sheets don't follow the
    # prompt's "8 cells per row" rule — they pack in however many poses the
    # generator decided to draw, so we can't rely on a fixed grid. Each peak
    # in the smoothed column-density is one character; we slice around the
    # FIRST `expected_cells` peaks (left-to-right reading order) so that the
    # spec's frame-name order (idle_0, idle_1, …) maps to the first N poses
    # the artist drew on that row.
    if expected_cells:
        col_density = sub.sum(axis=0).astype(float)
        sigma = max(8, W // 100)
        smoothed = gaussian_filter1d(col_density, sigma=sigma)
        if smoothed.max() > 0:
            # Min distance between peaks: assume the artist drew at MOST one
            # character per 60 px (worst case ~50 chars per 2900-wide row).
            # That's permissive enough to catch packed sheets, strict enough
            # to filter body-part bumps within one character.
            min_dist = max(30, W // 60)
            peaks, props = find_peaks(
                smoothed,
                distance=min_dist,
                prominence=smoothed.max() * 0.08,
            )
            if len(peaks) >= expected_cells:
                # Keep the FIRST expected_cells peaks in left-to-right order
                # — these correspond to frame 0, 1, 2, … of the anim.
                peaks = peaks[:expected_cells]
                cells = []
                for i, p in enumerate(peaks):
                    # Cell extends halfway to the neighbouring peak so each
                    # cell is tight around one character with minimal overlap.
                    left = (peaks[i - 1] + p) // 2 if i > 0 else max(0, p - min_dist)
                    right = (peaks[i + 1] + p) // 2 if i + 1 < len(peaks) else min(W, p + min_dist)
                    cells.append([int(left), int(right)])

        # Fall back to uniform division over content bbox if peak detection
        # didn't produce enough cells.
        if len(cells) < expected_cells:
            cols_with_fg = sub.sum(axis=0) > 0
            if cols_with_fg.any():
                xs = np.where(cols_with_fg)[0]
                content_x0, content_x1 = int(xs.min()), int(xs.max()) + 1
                step = (content_x1 - content_x0) / expected_cells
                cells = [[int(content_x0 + i * step), int(content_x0 + (i + 1) * step)]
                         for i in range(expected_cells)]

    # Refine per-cell bbox so each frame is tight around the actual character.
    # Use a noise-aware threshold: a row/column counts as content only if it
    # has at least a few percent of its dimension as foreground (filters out
    # the constant compression noise that would otherwise prevent any
    # tightening at all).
    out = []
    for cx0, cx1 in cells:
        col_slice = fg[y0:y1, cx0:cx1]
        H_band = y1 - y0
        W_cell = cx1 - cx0
        row_thresh = max(3, int(W_cell * 0.04))
        col_thresh = max(3, int(H_band * 0.04))
        row_has = col_slice.sum(axis=1) >= row_thresh
        col_has = col_slice.sum(axis=0) >= col_thresh
        if not row_has.any() or not col_has.any():
            continue
        ys = np.where(row_has)[0]
        xs = np.where(col_has)[0]
        ty0 = y0 + int(ys.min())
        ty1 = y0 + int(ys.max()) + 1
        tx0 = cx0 + int(xs.min())
        tx1 = cx0 + int(xs.max()) + 1
        out.append((tx0, ty0, tx1, ty1))
    return out


def uniform_row_bands(fg, n_rows):
    """Divide the cropped foreground area into n_rows equal horizontal bands.

    Used as a fallback when gap detection can't find natural gutters
    (densely-packed sheets where Gemini didn't leave magenta between rows).
    """
    H = fg.shape[0]
    if n_rows <= 0:
        return []
    step = H // n_rows
    return [(i * step, (i + 1) * step if i < n_rows - 1 else H) for i in range(n_rows)]


def slice_sheet(png_path, expected_slots):
    fg, _ = load_mask(png_path)
    # If Gemini wrapped the sheet in a black border, the gap rows in that
    # border aren't useful for band detection — crop the content region first.
    bbox = crop_to_content(fg)
    if bbox is None:
        return None, 0, 0
    y_off, _, x_off, _ = bbox
    fg = fg[bbox[0]:bbox[1], bbox[2]:bbox[3]]
    bands = find_row_bands(fg)
    # Fallback: if gap detection didn't find every expected row, the sheet
    # probably has too little magenta gutter between rows. Divide the
    # cropped region into uniform horizontal bands instead. This assumes
    # the artist drew the rows in the order specified by the spec — which
    # the Gemini prompts force via the explicit "Row 1 / Row 2 / …" layout.
    if len(bands) < len(expected_slots):
        bands = uniform_row_bands(fg, len(expected_slots))
    frames = {}
    anims = {}
    n_slots = len(expected_slots)
    n_bands = len(bands)
    if n_bands == 0:
        return None, n_bands, 0
    used_slots = expected_slots[:n_bands]
    char = os.path.splitext(os.path.basename(png_path))[0]
    expected_frames_map = EXPECTED_FRAMES.get(char, {})
    for i, (y0, y1) in enumerate(bands):
        slot = used_slots[i] if i < n_slots else f"row{i}"
        expected_cells = expected_frames_map.get(slot)
        cells = find_cells_in_row(fg, y0, y1, expected_cells=expected_cells)
        if not cells:
            continue
        names = []
        for j, (x0, ty0, x1, ty1) in enumerate(cells):
            key = f"{slot}_{j}"
            # Restore original-image coordinates by adding the crop offset.
            frames[key] = {
                "x": int(x0) + x_off,
                "y": int(ty0) + y_off,
                "w": int(x1 - x0),
                "h": int(ty1 - ty0),
            }
            names.append(key)
        anims[slot] = names
    # Use the character's name (parent dir's basename of the PNG) to pick a
    # target on-screen cell height so the engine can scale the high-res
    # Gemini frames down to gameplay size.
    char = os.path.splitext(os.path.basename(png_path))[0]
    target_h = TARGET_CELL_H.get(char, 96)
    atlas = {
        "fps": 8,
        "frames": frames,
        "anims": anims,
        "anchor": {"x": 0.5, "y": 1.0},
        "target_h": target_h,
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
