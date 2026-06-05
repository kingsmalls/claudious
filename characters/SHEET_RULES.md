# Sprite-sheet generation rules

Universal rules for every character sheet in this project. Each character's
own `.md` file specifies that character's appearance, identity items, and
anim list; the rules below apply to every sheet.

## 1. One character per sheet — identical across every cell

Pick one specific person, lock every identity attribute, and draw THAT
person in every cell. **Only the pose changes between cells.**

The following must be identical in every cell of the sheet:

- Skin tone
- Hair colour and style
- Headwear (or lack of it)
- Clothing colour and cut
- Accessories (jewellery, tattoos, weapons, identity items)
- Build and proportions

Variety across spawns is handled by the engine (per-spawn tint, variant
lookup) — never by varying the sheet itself. If you want alternate looks,
ship them as separate sheets (`runner_a.png`, `runner_b.png`).

## 2. No text inside cells

The cell must contain **only the character** (plus weapon, projectile,
effect particles, etc. that are visually part of the pose). Do not include:

- Anim-name labels (`idle`, `walk`, `atk1`, `JAB`, `BACKSTAB`, …)
- Row headers
- Frame counters (`F1`, `F2`, `F9`, …)
- Status words (`Hurt`, `Dead`, …)

If you need to verify alignment, do it on a separate proof image and discard.

## 3. No drawn cell separators

Cells are defined by **even pixel spacing**, not by drawn lines. Do not
include:

- Coloured lines between cells (white, magenta, anything)
- Cell borders
- Row dividers
- Reference rectangles

## 4. Background is magenta `#ff00ff` or fully transparent

Other backgrounds (white, dark grey, near-black, dark purple) are not
removed by the chroma key and will render as a coloured rectangle around
the character.

## 5. Attacks must be visually distinct from idle and from each other

Every attack must have a **clearly different silhouette** from the character's
idle/walk pose AND from every other attack. The peak frame of each attack
should be readable from across the screen as that specific attack.

Common failure: the generator draws an attack that's mostly the idle pose
with one limb slightly extended. The result reads as "still idle" in motion.

To avoid this in each attack:

- The **body posture changes** (lean angle, crouch level, weight transfer)
- **Multiple limbs move** — not just one fist or one foot extending from
  an otherwise-idle pose
- **Visual effects accompany the peak frame** (motion lines, dust, weapon
  trail, particle burst, lighting tell)
- The peak-frame silhouette would be **recognisable in pure black-on-white
  outline form** — if the silhouette doesn't read, the attack doesn't read

If a character's idle includes a distinctive prop or pose (Blackwell's
crossed arms, Razor's hands-behind-back), that prop/pose must **leave**
during attacks. Otherwise every attack looks like idle.

## 6. Identity items in every frame

Each character's spec lists "REQUIRED IN EVERY FRAME" items. If a frame
omits one, the frame is wrong. Hurt and dead frames count.

Common identity items:

- Rio's yellow wrist bandana
- Duke's cigarette behind the ear
- Atlas's silver wedding band on neck chain
- Lamplight's fedora + scarf + pistol
- Rig's yellow hardhat
- Shade's eye-glow
- Razor's dual knives
- Kane's round wire-rim glasses + half-smile

## 7. Frame layout

- Uniform grid: every cell is the same `cell_w × cell_h` pixels.
- Bottom-center anchor: the character's feet (or the lowest body point in
  airborne / down poses) sit at the bottom of the cell, horizontally
  centered.
- Empty space above the head is fine; the engine's tightening pass handles
  the trim.
- Vertical placement of the character within the cell must be **consistent
  across all frames in an animation**, or the head will appear to bob up
  and down between frames.
- If a pose needs more width than `cell_w` (an extended kick, a swung
  chain), expand the cell size for the whole sheet rather than letting that
  one pose bleed into the neighboring cell.

## 8. Animation ordering

Frames are read **row by row, left to right**, in the order declared by the
character's `.md` (typically `idle → walk → run → jump → atk1 → atk2 →
atk3 → heavy → jump_atk → back_atk → special → throw → counter → hurt →
dodge` for player characters; per-character order for enemies).

## 9. Magenta against dark characters

Lamplight, Shade, and Razor all wear near-black clothing. Magenta `#ff00ff`
gives the strongest possible contrast to that, which is good for the
chroma key. Keep it pure — do not pick a softer "background magenta."
