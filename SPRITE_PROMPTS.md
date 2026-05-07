# SPRITE GENERATION PROMPTS

Per-character prompts for the AI sprite generator (Pixellab / Stable Diffusion / Gemini / similar). Each prompt:

1. Names the character with the exact identity items from `CHARACTER_BIBLE.md`
2. Locks the palette to the documented hex codes
3. Demands a **uniform grid** so `sprite_slicer.html` can slice it cleanly
4. Lists all 15 animation slots the engine expects, with frame counts

Required identity items per character — these MUST appear in every frame:

- **RIO**: yellow bandana on left wrist
- **DUKE**: cigarette tucked behind one ear (never lit)
- **ATLAS**: silver wedding band on chain around neck (visible through open V of flannel) + tribal forearm tattoos

If the generator drops the identity item, regenerate the frame.

---

## Recommended grid

Aim for a **uniform-grid sprite sheet**:

- Frame size: **64 × 96** (room for jumps and uppercuts above the body)
- Layout: **8 columns × N rows** where N = sum of frame counts below
- Background: solid magenta (`#ff00ff`) for keying, or transparent PNG

For RIO and DUKE the body fits comfortably in 48-tall; for ATLAS use the full 96 height (he's bigger).

The atlas loader expects bottom-center anchor by default. Place the character's feet at the bottom-center of each cell. Specials and jumps may extend above the body — that's fine, the cell height accommodates it.

---

## Animation list (engine-required)

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Subtle bob; identity items visible. |
| `walk`     | 6 | Cycle. |
| `run`      | 6 | Faster cycle. |
| `jump`     | 3 | Anticipation, peak, landing. |
| `atk1`     | 4 | Light strike (jab / shove). |
| `atk2`     | 5 | Medium strike (cross / heavy slap). |
| `atk3`     | 6 | Combo finisher (hook / overhead). |
| `heavy`    | 7 | Uppercut launcher — body crouches, then rises. |
| `jump_atk` | 4 | Aerial attack (dive kick / drop). |
| `back_atk` | 4 | Elbow strike *behind* the body. |
| `special`  | 12 | Signature move (see per-character below). |
| `throw`    | 5 | Brief throw release pose. |
| `counter`  | 6 | Free counter-special at full parry meter. |
| `hurt`     | 3 | Knockback / staggered. |
| `dodge`    | 5 | Backward roll / sidestep. |

Total: ~80 frames per character. At 8 columns wide that's 10 rows.

---

## RIO — generation prompt

> Pixel art sprite sheet, side-view 2D fighting game style, 64x96 frame size, 8 columns by 10 rows uniform grid, transparent background.
>
> **Character:** Rio. 24-year-old woman, dark brown skin (#8a5235), athletic build. Shaved sides with low fade, short locs on top, dark brown to black hair (#1a1410). Single small gold hoop earring. Cropped olive bomber jacket (#7d8d4f highlights, #5a6b3a shadow). Black tank top under (#0a0a10). Slim charcoal cargo pants (#1a1a22). Ankle boxing boots, black. White hand wraps on knuckles (#dcd6c4).
>
> **Required identity item, must be visible in EVERY frame:** bright yellow bandana tied around her LEFT wrist (#e8c04a body, #ffd76a highlight, #b89426 shadow). The bandana is 7-8 pixels wide, has a small dangling tail, and TRAILS through punches and spins.
>
> **Tone:** calm, deadpan, focused. Smiles only on a clean combo. Speed/finesse boxer trained by a retired pro. Movement reads as fast and precise.
>
> **Frame layout (top to bottom, 8 frames per row):**
> Row 1: `idle` x4 (subtle breathing bob), then `walk` first 4
> Row 2: `walk` last 2, `run` x6
> Row 3: `jump` x3 (anticipation, peak, landing), `atk1` x4 (jab — front-arm jab, bandana extends with the punch), 1 spare
> Row 4: `atk2` x5 (cross — REAR-arm straight punch, body rotates), `atk3` x3 first half (hook — front arm hooks across)
> Row 5: `atk3` last 3, `heavy` x5 (uppercut: crouch, fist rises from low to high, BANDANA TRAILS THROUGH ARC)
> Row 6: `heavy` last 2, `jump_atk` x4 (aerial knee/kick), `back_atk` x2 first half
> Row 7: `back_atk` last 2 (rear elbow strike behind her), `special` x6 first half (Sunset Spin: spinning leg sweep — body rotates 360° with bandana tracing a wide arc)
> Row 8: `special` x6 last half (rising double-fist uppercut finisher, bandana flying skyward)
> Row 9: `throw` x5 (overhand grab + slam), `counter` x3 first half
> Row 10: `counter` x3 last half (counter-special — bigger version of atk1 with bandana glow), `hurt` x3, `dodge` x2 first half
>
> Pixel-art style, clean silhouette, hard edges, 5-6 color palette per body part, no anti-aliasing on outline, action-readable poses. Reference: Streets of Rage 4, Fight'N Rage character pixel quality.

---

## DUKE — generation prompt

> Pixel art sprite sheet, side-view 2D fighting game style, 64x96 frame size, 8 columns by 10 rows uniform grid, transparent background.
>
> **Character:** Duke. 31-year-old man, weathered pale skin (#d4a888), several days of stubble (#3a2a1c) on a square jaw, athletic ex-boxer build. Messy dark blonde hair (#a08c4a highlight, #6e5e2c shadow), uneven top, a wayward strand falling over his forehead. Faded denim cut-off jacket (#5a6678 body, #404a5c shadow), sleeveless with ragged hem. Stained off-white t-shirt under (#cfc8b8). Dark worn jeans (#2a2e3a). Beat-up black combat boots, slightly chunkier than normal sneakers (#161618).
>
> **Required identity item, must be visible in EVERY frame:** an unlit cigarette (1-pixel wide, off-white #e8e4d2 with brown tip #7a4a26) tucked behind ONE ear, camera-side. Never lit, never moves.
>
> **Tone:** tired, cynical, half-finished sentences, semi-pro boxer with a knee injury. Movement reads as economical, no wasted motion, hits with weight.
>
> **Frame layout (top to bottom, 8 frames per row):**
> Row 1: `idle` x4 (slight sway), `walk` first 4
> Row 2: `walk` last 2, `run` x6
> Row 3: `jump` x3, `atk1` x4 (jab — front-hand boxing jab), 1 spare
> Row 4: `atk2` x5 (cross — rear-hand straight, full hip rotation), `atk3` x3 first half (hook with a slight stomp)
> Row 5: `atk3` last 3, `heavy` x5 (uppercut launcher — body crouches, then rising fist)
> Row 6: `heavy` last 2, `jump_atk` x4 (aerial elbow drop), `back_atk` x2 first half
> Row 7: `back_atk` last 2 (rear elbow), `special` x6 first half (Rolling Thunder: three rapid forward elbow strikes with speedlines — frame 1 wind-up, frames 2-3 first elbow, frames 4-5 second elbow)
> Row 8: `special` x6 last half (third elbow + haymaker — body weight drops into a downward overhand right, dust kicks up at his feet)
> Row 9: `throw` x5 (uppercut throw — grabs + flips), `counter` x3 first half
> Row 10: `counter` x3 last half (counter haymaker), `hurt` x3, `dodge` x2 first half
>
> Pixel-art style, clean silhouette, hard edges, 5-6 color palette per body part. The cigarette stays visible in every pose — even when ducking, even mid-roll. Reference: Streets of Rage 4 character quality.

---

## ATLAS — generation prompt

> Pixel art sprite sheet, side-view 2D fighting game style, 64x96 frame size, 8 columns by 10 rows uniform grid, transparent background.
>
> **Character:** Atlas. 47-year-old man, 6'4", massive (powerlifter physique, slightly soft now). Dark olive complexion (#7a5234 light, #583820 shadow). Bald head, full salt-and-pepper beard (#a8a4a0 light, #6e6c6a shadow) — beard wraps the lower jaw. Sleeveless deep-red plaid flannel (#7a3030 body, #5a1c1c shadow, #9a4040 highlight) with sleeves torn off and TOP THREE BUTTONS UNDONE — open V of skin showing. Heavy work pants (#3a3024) with a wide black leather belt and brass buckle (#a89060). Heavy steel-toed boots (#1c140c with grey #3a3a3a steel toe).
>
> **Required identity items, must be visible in EVERY frame:**
> 1. **Silver wedding band on a thin chain (#c0c0c8) around his neck**, the band itself visible through the open V of the flannel, swinging slightly with motion.
> 2. **Faded geometric tribal tattoos (#332016)** as 1-pixel-wide bands on both bare forearms — small dark stripes, two per forearm.
>
> **Tone:** father energy, slow to anger and terrifying when he gets there, calls everyone "kid". Hardware store owner, has been protecting the block legally and financially for 20 years. Movement reads as deliberate, heavy, never rushed.
>
> **Frame layout (top to bottom, 8 frames per row):**
> Row 1: `idle` x4 (slow chest rise/fall, wedding ring catches light), `walk` first 4
> Row 2: `walk` last 2 (heavy stomp gait), `run` x6 (long strides, dust kicks at boots)
> Row 3: `jump` x3, `atk1` x4 (open-palm shove with the front arm)
> Row 4: `atk2` x5 (rear-arm heavy slap — body torque, beard moves with the strike), `atk3` x3 first half (overhead chopping smash)
> Row 5: `atk3` last 3 (overhead lands, dust at feet), `heavy` x5 (massive uppercut, both legs braced, fist rising)
> Row 6: `heavy` last 2 (peak), `jump_atk` x4 (aerial body slam), `back_atk` x2 first half
> Row 7: `back_atk` last 2 (rear elbow), `special` x6 first half (Foundation Stone: forward shoulder charge with three speedlines, crouches, picks the enemy off the ground)
> Row 8: `special` x6 last half (TWO-HANDED slam — both arms overhead, then ground impact with dust burst all around the boots)
> Row 9: `throw` x5 (lifting suplex), `counter` x3 first half
> Row 10: `counter` x3 last half, `hurt` x3, `dodge` x2 first half (sidestep, not a roll — Atlas doesn't roll)
>
> Pixel-art style, clean silhouette, hard edges. Atlas is wider than the other two — give him 16 horizontal pixels of body width vs 12-14 for Rio/Duke. The chain + tattoos visible in every frame. Reference: Streets of Rage 4 character quality, big-bruiser archetype.

---

## After generation

1. Drop the resulting `rio.png`, `duke.png`, `atlas.png` into the project root.
2. Open `sprite_slicer.html` in a browser, load the PNG, set frame width 64 / height 96 (or whatever you exported at), click cells to label each animation frame.
3. Export the atlas JSON. The slicer auto-pre-creates all 15 standard anim slots — fill them in by clicking through the sheet.
4. Run `python3 pipeline.py validate-atlas rio_atlas.json` to confirm no errors.
5. Reload `the_block.html` — the engine picks up the atlas automatically and switches that character from procedural to sprite rendering. The procedural fallback covers any animation slot you haven't filled in yet, so you can ship partial atlases.

If a sprite is missing an identity item in any frame, regenerate that single frame and re-export. Don't ship without the bandana, the cigarette, or the chain — those are the characters' tells.

---

## Notes on the previous sprite pass

The first sheets you generated (red-energy fists / blue lightning / earth-bruiser with elemental specials) read as fighting-game characters rather than the lived-in social-realist tone the bible commits to. The prompts above explicitly forbid elemental effects and require the identity items, which should pull the generator back toward the canonical look on a regeneration pass.

If you decide later to keep the first sheets as **alternate costumes** ("STORM" / "SPARK" / "TITAN" skins as post-launch DLC), the engine has the wiring for it via `selectedChar` keys — just add `rio_storm.png` + `rio_storm_atlas.json` and a costume selector in the character-select panel. That's a clean Phase 6 if it proves popular.
