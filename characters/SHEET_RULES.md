# Sprite-sheet generation rules

Universal rules for every character sheet in this project. Each character's
own `.md` file specifies that character's appearance, identity items, and
anim list; the rules below apply to every sheet.

## 🛑 LOCOMOTION ROWS — `walk` and `run` MUST read as locomotion

The `walk` and `run` rows have been the biggest source of "looks like a
grab attempt / shadow boxing / jump stomp" complaints. The cause is
usually one of two mistakes the generator makes:

1. Drawing tucked arms or arms extended FORWARD on a frame — that frame
   reads as a punch or grab when looped at game speed.
2. The last frame of the walk shows a planted leg or stomped foot — when
   the cycle wraps back to frame 1, the snap looks like a sudden stomp.

Rules for every `walk` row:

- All frames show **forward locomotion** — feet alternating, arms
  swinging at the sides OPPOSITE to the leg direction (left leg
  forward = right arm forward swing, and vice versa).
- **Both arms swing in a relaxed arc at the sides.** Arms NEVER reach
  forward past the body. Fists stay loosely closed, not in striking
  position.
- The cycle must **loop seamlessly** — the last frame's pose should
  blend back into the first frame's pose. No planted-leg "ending"
  frame.
- Body is upright. No body lean, no crouch, no kick.
- Walk = 6 frames typically. Each frame is a single step in the cycle:
  - F1: left leg forward, right arm forward
  - F2: passing position (feet under body), arms at sides
  - F3: right leg forward, left arm forward
  - F4: passing position
  - F5: left leg forward again (mirror of F1 OR same as F1)
  - F6: passing position
- This anim loops continuously while the character walks. **It must
  loop CLEANLY** — no pose at the end that reads as "stomp" or
  "kick" or "arm extended."

Rules for every `run` row:

- Body leans forward 5-10°.
- Knees lift higher than walk — visible airborne stride.
- **Arms PUMP up and down at the sides**, fists loosely closed.
  Arms NEVER extend forward past the body (that reads as punch/grab).
- Same loop-cleanly rule as walk.
- Optional: 1-2 px motion lines behind the heel on the trailing foot.

What walk/run frames MUST NOT contain:

- Extended fists / arms forward (reads as punch or grab)
- Open hands grabbing forward (reads as throw setup)
- A planted-leg "stomp" or "kick" pose on the final frame
- A pose that reuses the character's atk1 or jump_atk silhouette
- Body coiled like a wind-up
- A grimace or attack-face expression

The character should be **calm and traveling**, not preparing for a
hit. Walk reads as "walking somewhere," run reads as "running
somewhere." Combat poses live in the atk rows.

---

## 🛑 RULE ZERO — NO TEXT IN THE OUTPUT IMAGE, EVER

The output PNG must contain **ZERO text characters**. This is the rule
most often broken by image generators. Treat it as absolute.

The following must NOT appear anywhere in the sheet:

- Anim-name labels: `IDLE`, `WALK`, `RUN`, `ATK1`, `ATK2`, `JAB`, `CROSS`,
  `HAYMAKER`, `SWING`, `SPIN`, `STRIKE`, `BACKSTAB`, `HURT`, `DEAD`,
  `KICK`, `SLAM`, `CHARGE`, `OVERHEAD`, `PUNCH`, `LUNGE`, `THROW`,
  `SHOT`, `VANISH`, `BOW`, `COUNTER`, `DODGE`, `JUMP`, etc.
- Frame counters: `F1`, `F2`, `F3`, `F4`, `F5`, `F6`, `F7`, `F8`, `F9`,
  `F10`, `F11`, `F12`, `H1`, `1`, `2`, `3`, `5°`, etc.
- Status words: `Hurt`, `Dead`, `KO`, `Idle`, etc.
- Row / column headers, captions, titles, legends.
- ANY letter or number anywhere in any cell, even small ones.

If the generator wants to label cells for reference, it should produce a
SEPARATE annotated proof image and discard it. The production sheet ships
text-free.

A sheet with even one piece of stray text is unusable — the engine will
render the letters as part of the sprite.

---

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

## 2. Already-covered: no text — see Rule Zero above

(Kept here so section numbers in old references don't shift.) The cell
must contain **only the character** (plus weapon, projectile, effect
particles, etc. that are visually part of the pose).

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
