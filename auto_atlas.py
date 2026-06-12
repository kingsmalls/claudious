#!/usr/bin/env python3
"""Re-slice every character sprite sheet into an atlas JSON.

Strategy: 2D connected-component blob detection. Gemini's sheets don't
follow uniform grids — characters sit at staggered heights, rows overlap,
and per-row slicing inevitably bleeds one row into another. Instead we:

1. Chroma-key magenta/black background to alpha-0 (also fixes rendering).
2. Dilate the foreground mask so a character merges with its own detached
   pieces (motion lines, props), then label connected components.
3. Drop noise blobs (tiny area) and text banners (very flat aspect).
4. Cluster blob centers into rows by vertical overlap, sort rows
   top-to-bottom, blobs left-to-right within each row.
5. Map rows to the spec's REQUIRED ANIMATION ROWS order; take the first
   `expected_frames` blobs per row.
6. Store per-frame target height (`th`) so poses keep their relative
   heights within a row when the engine scales them down.

Usage:
    python3 auto_atlas.py            # re-slice every character
    python3 auto_atlas.py shade rig  # re-slice only the named ones
"""
import json
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage
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
    # Mid-tier enemies — scaled up to closer-to-player size so they read
    # well on screen now that the Gemini sheets are high-res. Previously
    # 64-80 px tall to match the original spec dimensions; bumping to 88-96
    # so they have more visible body detail.
    "runner": 96, "chains": 96, "slice": 96, "tank": 104,
    "lamplight": 96, "dojo": 96, "shade": 88, "rig": 96,
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


def looks_like_text_row(fg, y0, y1):
    """Disabled — every heuristic I tried for "this row is text" also kills
    legitimate character rows. The text problem is rare enough (one row in
    rio.png had the SPINNING label) that hand-editing the affected atlas
    after generation is more reliable than a blanket filter."""
    return False


def chroma_key_to_alpha(png_path, out_path):
    """Pre-process a sheet: replace magenta + near-black backgrounds with
    fully transparent pixels and save as a new PNG. The engine then renders
    each frame without showing magenta padding around the character.

    Detects magenta by chroma-dominance (r and b both significantly higher
    than g) rather than a strict brightness threshold, because Gemini's
    output sometimes contains dark-magenta gradients (e.g. rgb(145,3,151))
    around the cell borders that the strict #ff00ff test misses.
    """
    im = Image.open(png_path).convert("RGBA")
    arr = np.array(im)
    r = arr[..., 0].astype(int)
    g = arr[..., 1].astype(int)
    b = arr[..., 2].astype(int)
    # Magenta detection — generous on the green channel because Gemini's
    # newer sheets render "magenta" with a strong gradient up to g≈140 at
    # the edges of each character. We catch anything where:
    #   - red and blue are both bright,
    #   - chroma dominance (r + b - 2g) clearly favors magenta over green,
    #   - red and blue are roughly balanced (not a pink skin tone, which
    #     would be skewed toward red).
    # The "near-magenta" pass below is more aggressive (catches dim magenta
    # gradient pixels like rgb(160, 38, 159)) than the core pure-magenta
    # test, but only fires when both r and b are well above g.
    chroma_dom = (r + b) - 2 * g
    rb_balance = np.abs(r - b)
    # Pure magenta: bright with strong purple bias and red≈blue. Permissive
    # on green to catch Gemini's noisy magenta gradient (g up to ~140).
    pure_magenta = (chroma_dom > 140) & (g < 150) & (r > 140) & (b > 140) & (rb_balance < 80)
    # Dim magenta: dim-purple anti-aliasing at the edges of pure-magenta
    # against a character. Tight constraints (r,b both > 90, g well below
    # both) so this doesn't catch skin tones or cream fabrics.
    dim_magenta = (chroma_dom > 90) & (r > 90) & (b > 90) & (g < r - 55) & (g < b - 55) & (rb_balance < 50)
    is_magenta = pure_magenta | dim_magenta
    is_dark = (r < 18) & (g < 18) & (b < 18)
    is_bg = is_magenta | is_dark
    arr_out = arr.copy()
    arr_out[is_bg, 3] = 0
    Image.fromarray(arr_out, "RGBA").save(out_path)


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


def find_row_bands(fg, min_gap=2, min_height=80, gap_ratio=0.05):
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

    # Refine per-cell bbox so each frame is tight HORIZONTALLY but keeps
    # the row's full vertical extent. Tightening the vertical bbox per-cell
    # was breaking attack frames where the character pose has empty space
    # below (e.g. an arm extended sideways with no torso below) — the bbox
    # collapsed to just the arm and the engine then scaled it 3-4x larger
    # than expected because target_h / frame.h gave a huge factor.
    #
    # The row band already brackets the row tightly; using its bounds as
    # the per-frame vertical extent keeps all frames in an anim at the same
    # height, which is also what the engine's scaling logic assumes.
    out = []
    for cx0, cx1 in cells:
        col_slice = fg[y0:y1, cx0:cx1]
        H_band = y1 - y0
        col_thresh = max(3, int(H_band * 0.04))
        col_has = col_slice.sum(axis=0) >= col_thresh
        if not col_has.any():
            continue
        xs = np.where(col_has)[0]
        tx0 = cx0 + int(xs.min())
        tx1 = cx0 + int(xs.max()) + 1
        out.append((tx0, y0, tx1, y1))
    return out


def find_row_bands_by_peaks(fg, max_rows):
    """Locate up to `max_rows` row bands via peak detection on row-density.

    Returns whatever peaks were found (capped at max_rows). Caller decides
    whether fewer-than-expected is acceptable or to fall back to uniform.
    Each character row's center of mass shows up as a distinct peak in the
    smoothed row-density signal; bands are sliced halfway between peaks.
    """
    H = fg.shape[0]
    if max_rows <= 0:
        return []
    row_density = fg.sum(axis=1).astype(float)
    sigma = max(10, H // 80)
    smoothed = gaussian_filter1d(row_density, sigma=sigma)
    if smoothed.max() <= 0:
        return []
    # Min vertical distance between rows. Use a larger minimum (120 px) so
    # peak detection doesn't fire on body-part bumps within one character
    # (a raised arm, a kicking leg). We'd rather miss a row than slice the
    # sheet into 30-tall slivers.
    min_dist = max(120, H // (max_rows * 2 + 2))
    peaks, _ = find_peaks(
        smoothed,
        distance=min_dist,
        prominence=smoothed.max() * 0.05,
    )
    if len(peaks) == 0:
        return []
    peaks = sorted(peaks)[:max_rows]
    bands = []
    # Enforce a minimum band height so that adjacent peaks can't produce
    # sliver bands. If a band would be smaller than min_band_h, expand it
    # symmetrically around the peak.
    min_band_h = max(60, min_dist - 10)
    for i, p in enumerate(peaks):
        top = (peaks[i - 1] + p) // 2 if i > 0 else max(0, p - min_dist)
        bot = (peaks[i + 1] + p) // 2 if i + 1 < len(peaks) else min(H, p + min_dist)
        if bot - top < min_band_h:
            grow = (min_band_h - (bot - top)) // 2 + 1
            top = max(0, top - grow)
            bot = min(H, bot + grow)
        bands.append((int(top), int(bot)))
    return bands
    bands = []
    for i, p in enumerate(peaks):
        top = (peaks[i - 1] + p) // 2 if i > 0 else max(0, p - min_dist)
        bot = (peaks[i + 1] + p) // 2 if i + 1 < len(peaks) else min(H, p + min_dist)
        bands.append((int(top), int(bot)))
    return bands


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


def detect_blobs(fg, min_area=600, dilate_px=3):
    """Find raw blobs via 2D connected components with light dilation.

    Small dilation only — heavier merges adjacent characters on dense
    sheets. Detached pieces (a hat above a head, a wrist between body
    and hand) become separate blobs and re-merge later via x-overlap
    in cluster_blob_rows.

    Drops obvious text-label blobs at the source: wide-and-short shapes
    with sparse fill (text strokes leave most of the bbox empty).

    Returns a list of (x0, y0, x1, y1, area) tuples.
    """
    structure = np.ones((dilate_px, dilate_px), dtype=bool)
    dilated = ndimage.binary_dilation(fg, structure=structure)
    labels, n = ndimage.label(dilated)
    blobs = []
    for sl in ndimage.find_objects(labels):
        if sl is None:
            continue
        region = fg[sl]
        area = int(region.sum())
        if area < min_area:
            continue  # compression noise / stray specks
        ys, xs = np.where(region)
        y0 = sl[0].start + int(ys.min())
        y1 = sl[0].start + int(ys.max()) + 1
        x0 = sl[1].start + int(xs.min())
        x1 = sl[1].start + int(xs.max()) + 1
        bw, bh = x1 - x0, y1 - y0
        # Text-label signature: wide-and-short (aspect > 2.2) and sparse
        # fill (text strokes leave most of the bbox empty). A character
        # turned sideways stays denser than this.
        fill_ratio = area / max(1, bw * bh)
        if bw > bh * 2.2 and fill_ratio < 0.45:
            continue
        # Extremely thin slivers can't be characters at all.
        if bh < 30 or bw < 16:
            continue
        blobs.append((x0, y0, x1, y1, area))
    return blobs


def strip_text_label_from_blob(b, fg, est_h):
    """If a blob's bbox contains a text label stuck above the character,
    return a new bbox tight around just the character portion."""
    x0, y0, x1, y1, area = b
    h = y1 - y0
    if h <= est_h * 1.1:
        return b
    strip = fg[y0:y1, x0:x1]
    row_density = strip.sum(axis=1).astype(float)
    # Smooth so individual letter glyphs don't look like separate peaks.
    sm = gaussian_filter1d(row_density, sigma=max(3, h // 60))
    # Find horizontal gaps (rows with density well below the body max).
    body_max = sm.max()
    gap_thresh = body_max * 0.18
    in_gap = sm < gap_thresh
    # Look for the largest near-top gap. If found, drop everything above it.
    segments = []
    i = 0
    while i < h:
        if not in_gap[i]:
            j = i
            while j < h and not in_gap[j]:
                j += 1
            segments.append((i, j))
            i = j
        else:
            i += 1
    if len(segments) <= 1:
        return b
    # Pick the segment with the largest area that's at least est_h * 0.6 tall.
    best = None
    best_area = -1
    for sy0, sy1 in segments:
        if sy1 - sy0 < est_h * 0.55:
            continue
        seg = strip[sy0:sy1]
        a = int(seg.sum())
        if a > best_area:
            best_area = a
            best = (sy0, sy1, a)
    if not best:
        return b
    sy0, sy1, a = best
    seg = strip[sy0:sy1]
    ys, xs = np.where(seg)
    if not ys.size:
        return b
    return (x0 + int(xs.min()), y0 + sy0 + int(ys.min()),
            x0 + int(xs.max()) + 1, y0 + sy0 + int(ys.max()) + 1, a)


def split_tall_blobs(blobs, fg, est_h):
    """Split blobs that span multiple rows (characters touching vertically).

    `est_h` is the estimated single-character height (content height divided
    by the spec's expected row count). A blob taller than 1.5x that estimate
    gets cut at the row-density valleys nearest to the uniform cut points.
    """
    out = []
    for (x0, y0, x1, y1, area) in blobs:
        h = y1 - y0
        if h <= est_h * 1.5:
            out.append((x0, y0, x1, y1, area))
            continue
        k = max(2, round(h / est_h))
        strip = fg[y0:y1, x0:x1]
        density = strip.sum(axis=1).astype(float)
        sm = gaussian_filter1d(density, sigma=max(4, h // (k * 8)))
        cuts = [0]
        for i in range(1, k):
            center = int(i * h / k)
            lo = max(1, center - int(est_h * 0.3))
            hi = min(h - 1, center + int(est_h * 0.3))
            if lo >= hi:
                cuts.append(center)
                continue
            cuts.append(lo + int(np.argmin(sm[lo:hi])))
        cuts.append(h)
        for i in range(k):
            cy0, cy1 = cuts[i], cuts[i + 1]
            seg = strip[cy0:cy1]
            if not seg.any():
                continue
            ys, xs = np.where(seg)
            out.append((x0 + int(xs.min()), y0 + cy0 + int(ys.min()),
                        x0 + int(xs.max()) + 1, y0 + cy0 + int(ys.max()) + 1,
                        int(seg.sum())))
    return out


def split_wide_blob(blob, fg, n_pieces):
    """Split one wide blob into n_pieces by column-density valleys.
    Used when a whole row merged into a single blob (no gutters)."""
    x0, y0, x1, y1, _area = blob
    w = x1 - x0
    strip = fg[y0:y1, x0:x1]
    density = strip.sum(axis=0).astype(float)
    sm = gaussian_filter1d(density, sigma=max(4, w // (n_pieces * 8)))
    cuts = [0]
    for i in range(1, n_pieces):
        center = int(i * w / n_pieces)
        span = int(w / n_pieces * 0.35)
        lo = max(1, center - span)
        hi = min(w - 1, center + span)
        if lo >= hi:
            cuts.append(center)
            continue
        cuts.append(lo + int(np.argmin(sm[lo:hi])))
    cuts.append(w)
    pieces = []
    for i in range(n_pieces):
        cx0, cx1 = cuts[i], cuts[i + 1]
        seg = strip[:, cx0:cx1]
        if not seg.any():
            continue
        ys, xs = np.where(seg)
        pieces.append((x0 + cx0 + int(xs.min()), y0 + int(ys.min()),
                       x0 + cx0 + int(xs.max()) + 1, y0 + int(ys.max()) + 1,
                       int(seg.sum())))
    return pieces


def split_wide_blobs_auto(blobs, fg):
    """Split blobs whose aspect says "multiple characters merged
    side-by-side" (w > 1.8x h). Cut at midpoints between column-density
    peaks — each peak is one character's body mass."""
    out = []
    for b in blobs:
        x0, y0, x1, y1, area = b
        w, h = x1 - x0, y1 - y0
        if w <= h * 1.8:
            out.append(b)
            continue
        strip = fg[y0:y1, x0:x1]
        density = strip.sum(axis=0).astype(float)
        sm = gaussian_filter1d(density, sigma=max(6, h // 10))
        if sm.max() <= 0:
            out.append(b)
            continue
        min_dist = max(30, int(h * 0.35))
        peaks, _ = find_peaks(sm, distance=min_dist, prominence=sm.max() * 0.08)
        if len(peaks) < 2:
            out.append(b)
            continue
        cuts = [0] + [int((peaks[i] + peaks[i + 1]) / 2)
                      for i in range(len(peaks) - 1)] + [w]
        for i in range(len(cuts) - 1):
            seg = strip[:, cuts[i]:cuts[i + 1]]
            if not seg.any():
                continue
            ys, xs = np.where(seg)
            out.append((x0 + cuts[i] + int(xs.min()), y0 + int(ys.min()),
                        x0 + cuts[i] + int(xs.max()) + 1, y0 + int(ys.max()) + 1,
                        int(seg.sum())))
    return out


def cluster_blob_rows(blobs, img_h, est_h):
    """Group blobs into rows, merge intra-character fragments, drop noise.

    1. Cluster blobs into rows by vertical-center overlap.
    2. Within each row, merge blobs whose x-ranges overlap — a floating
       hat or detached foot occupies the same column band as its owner.
    3. Drop fragments much shorter than the row's dominant blob height
       (leftover slivers from a neighbouring row bleeding into this one).
    4. Drop text-banner rows: short AND sparse (low fill ratio). Lying-down
       death poses are also flat but their pixel fill is dense, so they
       survive the fill-ratio test.
    """
    remaining = sorted(blobs, key=lambda b: (b[1] + b[3]) / 2)
    rows = []
    for b in remaining:
        cy = (b[1] + b[3]) / 2
        placed = False
        for row in rows:
            ry0 = min(x[1] for x in row)
            ry1 = max(x[3] for x in row)
            if ry0 <= cy <= ry1:
                row.append(b)
                placed = True
                break
        if not placed:
            rows.append([b])
    rows.sort(key=lambda row: min(b[1] for b in row))

    cleaned_rows = []
    for row in rows:
        row.sort(key=lambda b: b[0])
        # Merge x-overlapping blobs (same character's detached pieces).
        merged = []
        for b in row:
            if merged:
                m = merged[-1]
                overlap = min(m[2], b[2]) - max(m[0], b[0])
                min_w = min(m[2] - m[0], b[2] - b[0])
                if overlap > 0.35 * min_w:
                    merged[-1] = (min(m[0], b[0]), min(m[1], b[1]),
                                  max(m[2], b[2]), max(m[3], b[3]),
                                  m[4] + b[4])
                    continue
            merged.append(b)
        if not merged:
            continue
        # Drop fragments much shorter than the row's dominant height.
        max_h = max(b[3] - b[1] for b in merged)
        keep = [b for b in merged if (b[3] - b[1]) >= max_h * 0.55]
        if not keep:
            continue
        # Noise rows: dominant height too small to be a character.
        if max_h < max(50, est_h * 0.35):
            continue
        # Text-banner rows: short + flat + sparse fill.
        fills = [b[4] / max(1, (b[2] - b[0]) * (b[3] - b[1])) for b in keep]
        all_flat = all((b[2] - b[0]) > (b[3] - b[1]) * 2.2 for b in keep)
        if all_flat and max_h < est_h * 0.75 and (sum(fills) / len(fills)) < 0.38:
            continue
        cleaned_rows.append(keep)
    return cleaned_rows


def slice_sheet(png_path, expected_slots):
    fg, _ = load_mask(png_path)
    if not fg.any():
        return None, 0, 0
    char = os.path.splitext(os.path.basename(png_path))[0]
    expected_frames_map = EXPECTED_FRAMES.get(char, {})
    target_h = TARGET_CELL_H.get(char, 96)

    # Sanity check: if the sheet has effectively no magenta background
    # (less than 25% transparent after chroma-key), we can't separate the
    # characters reliably — every blob detection produces giant merged
    # masses. Refuse to ship a broken atlas; the engine will fall back to
    # procedural rendering.
    total_px = fg.size
    fg_ratio = fg.sum() / max(1, total_px)
    if fg_ratio > 0.75:
        return None, 0, 0

    blobs = detect_blobs(fg)
    if not blobs:
        return None, 0, 0
    # Estimate single-character height. The MEDIAN blob height is the most
    # reliable signal — Gemini often draws fewer/bigger rows than the spec
    # asks for, so deriving est_h from the expected row count splits real
    # characters at the waist (the half-body bug). Only fall back to the
    # spec-derived prior when blob detection found too few blobs to trust
    # (whole sheet merged into one mass).
    ys_content = np.where(fg.any(axis=1))[0]
    content_h = int(ys_content.max() - ys_content.min() + 1) if ys_content.size else fg.shape[0]
    prior_h = max(60, content_h / max(1, len(expected_slots)))
    heights = sorted(b[3] - b[1] for b in blobs)
    med_h = heights[len(heights) // 2]
    # Use the LARGER of the median and the prior. Some sheets (Baron) have
    # head-shot blobs mixed in that drag the median way below the real
    # character height; the prior is conservative and keeps full bodies.
    if len(blobs) >= 6 and prior_h * 0.6 <= med_h <= prior_h * 3.5:
        est_h = max(60, max(med_h, prior_h * 0.9))
    else:
        est_h = prior_h
    # Drop the "everything is connected" giant blob — it spans multiple
    # rows vertically AND covers most of the image width.
    img_w = fg.shape[1]
    blobs = [b for b in blobs
             if not ((b[3] - b[1]) > est_h * 2.5 and (b[2] - b[0]) > img_w * 0.7)]
    blobs = [strip_text_label_from_blob(b, fg, est_h) for b in blobs]
    blobs = split_tall_blobs(blobs, fg, est_h)
    blobs = split_wide_blobs_auto(blobs, fg)
    rows = cluster_blob_rows(blobs, fg.shape[0], est_h)

    frames = {}
    anims = {}
    used_slots = expected_slots[:len(rows)]
    for i, row in enumerate(rows):
        if i >= len(used_slots):
            break
        slot = used_slots[i]
        expected_cells = expected_frames_map.get(slot)
        # If the whole row merged into fewer blobs than the spec expects
        # AND one blob is much wider than the others, split the wide one
        # horizontally at column-density valleys.
        if expected_cells and len(row) < expected_cells:
            widths = [b[2] - b[0] for b in row]
            med_w = sorted(widths)[len(widths) // 2]
            expanded = []
            need = expected_cells - len(row) + 1
            for b in row:
                bw = b[2] - b[0]
                if need > 1 and bw > med_w * 1.7:
                    k = min(need, max(2, round(bw / max(1, med_w))))
                    pieces = split_wide_blob(b, fg, k)
                    expanded.extend(pieces if pieces else [b])
                    need -= (len(pieces) - 1) if pieces else 0
                else:
                    expanded.append(b)
            row = sorted(expanded, key=lambda b: b[0])
        # Reading order: first N blobs are frame 0..N-1 of the anim.
        chosen = row[:expected_cells] if expected_cells else row
        # Per-row max height — poses keep their RELATIVE heights when the
        # engine scales (a crouch stays shorter than a stand).
        row_max_h = max(b[3] - b[1] for b in chosen)
        names = []
        for j, (x0, y0, x1, y1, _area) in enumerate(chosen):
            key = f"{slot}_{j}"
            h = y1 - y0
            frames[key] = {
                "x": int(x0), "y": int(y0),
                "w": int(x1 - x0), "h": int(h),
                # Per-frame display height: preserves pose proportions
                # within the row. Engine prefers frame.th over the global
                # atlas target_h when present.
                "th": max(8, round(target_h * h / row_max_h)),
            }
            names.append(key)
        if names:
            anims[slot] = names

    atlas = {
        "fps": 8,
        "frames": frames,
        "anims": anims,
        "anchor": {"x": 0.5, "y": 1.0},
        "target_h": target_h,
    }
    return atlas, len(rows), sum(len(v) for v in anims.values())


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
        # Pre-process: replace magenta + black backgrounds with transparent.
        # The engine then draws each frame without any chroma key — the
        # background is already alpha-zero, so it composites cleanly.
        chroma_key_to_alpha(png, png)
        atlas, n_bands, n_frames = slice_sheet(png, expected)
        if atlas is None:
            # Refuse to ship a broken atlas. Delete any existing one so the
            # engine falls back to the procedural renderer for this char.
            if os.path.exists(out):
                os.remove(out)
            print(f"  SKIP   {name:11}  unsalvageable (no magenta or no rows) — falling back to procedural")
            continue
        # Quality check: drop any frame whose width is so much larger than
        # its height that it must be a merged row instead of a character.
        bad = [k for k, fr in atlas["frames"].items() if fr["w"] > fr["h"] * 1.9]
        for k in bad:
            atlas["frames"].pop(k, None)
        for slot, framelist in list(atlas["anims"].items()):
            atlas["anims"][slot] = [k for k in framelist if k in atlas["frames"]]
            if not atlas["anims"][slot]:
                del atlas["anims"][slot]
        if not atlas["anims"]:
            if os.path.exists(out):
                os.remove(out)
            print(f"  SKIP   {name:11}  every frame failed quality check — falling back to procedural")
            continue
        with open(out, "w") as f:
            json.dump(atlas, f, indent=2)
        ok = "OK   " if n_bands == len(expected) else "WARN "
        slot_str = ",".join(atlas["anims"].keys())
        print(f"  {ok}  {name:11}  {n_bands}/{len(expected)} rows  {n_frames} frames  -> {slot_str}")


if __name__ == "__main__":
    main()
