# Sprite-sheet generation rules

Universal rules for every character sheet in this project. Each character's
own `.md` file calls out variants and identity items; the rules below are
the things that broke previous sheets in ways the engine can't recover from
at runtime.

## 1. One character per sheet — identical across every cell

The single biggest source of "the character is glitching" in motion is the
same character being **drawn differently** in different cells:

- Hair colour shifts (blonde → dark → bald across the same anim)
- Headwear appears in some cells and not others (hood on, hood off, baseball cap)
- Skin tone shifts row to row
- Clothing colour drifts (charcoal in idle, navy in walk)
- A whole different person is drawn in one row (e.g. Dojo's bow row)

Pick one specific person, lock every identity attribute, and draw THAT person
in every cell. **Only the pose changes between cells.** Variety across spawns
is handled by the engine (per-spawn tint, variant lookup) — never by varying
the sheet.

## 2. No text inside cells — ever

Every previous problem sheet had text baked into the image:

- Anim-name labels: `idle`, `walk`, `atk1`, `JAB`, `CROSS`, `BACKSTAB`, …
- Row headers
- Frame counters: `F1`, `F2`, `F9`, `F10`
- Status words: `Hurt`, `Dead`, `K2 Backstab`

The engine slices each cell and renders whatever is inside it — so labels
appear as floating text stuck above the character. The cell must contain
**only the character** (plus weapon, projectile, effect particles, etc. that
are visually part of the pose).

If you need to verify alignment, do it on a separate proof image and discard.

## 3. No drawn cell separators

Cells are defined by **even pixel spacing**, not by drawn lines. Do not
include:

- Thin coloured lines between cells (white, magenta, anything)
- Cell borders
- Row dividers
- Reference rectangles

These lines render as part of the cell content and cut through the character
during animation. Razor's previous sheet had vertical white separator lines
that bisected her body in every frame — exactly this problem.

## 4. Background is magenta `#ff00ff` or fully transparent

Other backgrounds (white, dark grey, near-black, dark purple) are not
removed cleanly by the chroma key and leave a coloured rectangle around the
character — which is then revealed during the hit-flash render. If
transparent PNG, the engine will skip the chroma step.

## 5. Identity items in every frame

Each character's spec lists "REQUIRED IN EVERY FRAME" items. If a frame
omits one, the frame is wrong. Common offenders:

- Rio's yellow wrist bandana
- Duke's cigarette behind the ear
- Atlas's silver wedding band on neck chain
- Lamplight's fedora + scarf + pistol
- Rig's yellow hardhat
- Shade's eye-glow
- Razor's dual knives
- Kane's round wire-rim glasses + half-smile

Hurt and dead frames count. The hardhat does not fall off when Rig is hit.
The scarf does not come down when Lamplight dies.

## 6. Frame layout

- Uniform grid: every cell is the same `cell_w × cell_h` pixels.
- Bottom-center anchor: the character's feet (or the lowest body point in
  airborne/down poses) sit at the bottom of the cell, horizontally centered.
- Empty space above the head is fine; the engine's tightening pass handles
  the trim. **Inconsistent vertical placement of the character within cells
  is what causes "the hat bobs up and down between frames."**
- If a pose needs more width than `cell_w` (an extended kick, a swung
  chain), expand the cell size for the whole sheet rather than letting that
  one pose bleed into the neighboring cell.

## 7. Animation ordering

Frames are read **row by row, left to right**, in the order declared by the
character's `.md` (typically idle → walk → run → jump → atk1 → atk2 →
atk3 → heavy → jump_atk → back_atk → special → throw → counter → hurt →
dodge for player characters; per-character order for enemies).

If you reorder for layout reasons, update the character's `.md` so the atlas
JSON generator knows the new order.

## 8. Magenta against dark characters

Lamplight, Shade, and Razor all wear near-black clothing. Magenta `#ff00ff`
gives the strongest possible contrast to that, which is good for the
chroma key. Do not pick a softer "background magenta" — keep it pure.
