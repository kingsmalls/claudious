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
> **Character:** Rio. 24-year-old woman, dark brown skin (#8a5235), athletic build. Full afro, dark brown to black hair (#1a1410). Single small gold hoop earring. Cropped olive bomber jacket (#7d8d4f highlights, #5a6b3a shadow). Black tank top under (#0a0a10). Slim charcoal cargo pants (#1a1a22). Ankle boxing boots, black. White hand wraps on knuckles (#dcd6c4).
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

## LAMPLIGHT — generation prompt (full detail, paste into Gemini)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x88 frame size, 8 columns by 9 rows uniform grid (total image 512 wide × 792 tall), **magenta `#ff00ff` background**, bottom-center anchor. Mid-tier enemy. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>
> **Character — noir gunslinger:** Lamplight. Age 35–50 (read as a veteran), 5'10"–6'1", lean but not athletic — steady-hands, soldier's-stance build. Gender-ambiguous on purpose. Face is **almost entirely hidden** — only a narrow horizontal eye-strip is visible between the fedora brim above and the scarf below. Skin tone in that strip is medium tan (`#d4a888`).
>
> **Costume (head to feet):**
> 1. **Black fedora** — wide-brim pulled low; the brim casts a hard shadow across the upper face so only the eye-slit is visible. Battered band of darker leather around the crown. The fedora is **the silhouette tell** — recognisable from across the screen.
> 2. **Long charcoal-black trench coat** — mid-calf length, covers most of the body. Collar popped UP touching the bottom of the scarf. Belt cinched at the waist with a steel buckle. The coat normally hangs straight — **it only flares behind during the charged shot's recoil (atk2 F6) and on the kick (atk5 F3)**. The kick is the only frame that exposes the coat's **deep burgundy inner lining (`#4a1018`)** — see atk5.
> 3. **Long white scarf** (`#dcd6c4` body, `#9a9482` shadow) wrapped twice around the neck and **pulled up over the nose and mouth**. Two loose tails hang 14–18 px down the front of the coat. **The scarf stays up in every single frame including hurt and dead — never lower than the cheekbones.**
> 4. **Black leather gloves** — fitted, no fingers exposed.
> 5. **Dark tactical pants** (`#1a1a22`) below the coat hem.
> 6. **Heavy black combat boots** (`#0a0a10`).
> 7. **Single black pistol** — semi-auto silhouette, body `#3a3a40`, barrel `#4a4a50`. Held two-handed at chest height in idle, walk, atk1, atk2. **Re-oriented in the hand differently per attack — see frame layout.**
>
> **Required identity items, must be visible in EVERY frame including hurt and dead:**
> 1. **Fedora on the head** (the silhouette tell).
> 2. **White scarf up over nose and mouth** (the high-contrast tell against the black coat).
> 3. **Pistol in hand** (held at chest two-handed by default; differently per attack — see frame layout).
> 4. **Popped coat collar** reaching the bottom of the scarf.
>
> **Tone:** composed, bored, never theatrical. Walks slowly. The face never reads — only the eyes show, and they don't change. The threat is the silhouette.
>
> **Frame layout — 9 rows, 1 anim per row, 8 cells per row (unused cells stay magenta):**
>
> **Row 1 — `idle` × 4 frames** (cells 1–4; cells 5–8 magenta).
> - F1: standing flat, pistol held two-handed at chest, fedora level, scarf still, coat hanging straight.
> - F2: subtle inhale — shoulders rise 1 px, scarf tails sway 1 px.
> - F3: hold pose, same as F1.
> - F4: exhale — shoulders settle 1 px down.
>
> **Row 2 — `walk` × 6 frames** (cells 1–6; cells 7–8 magenta).
> - Composed gunslinger backwards-gait that **loops seamlessly** (F6 blends back into F1). Pistol stays in the two-handed chest grip the whole time. The arms don't swing wide (the coat masks them) but the SHOULDERS rotate slightly each step so it reads as walking, not hovering.
> - F1: LEFT foot fwd under the hem + RIGHT shoulder rotates fwd 1 px.
> - F2: passing position (feet under body, shoulders neutral).
> - F3: RIGHT foot fwd + LEFT shoulder rotates fwd 1 px.
> - F4: passing position.
> - F5: mirror of F1.
> - F6: passing position — blends straight back into F1.
> - Coat hem sways 2 px behind the trailing leg per step. Coat **never** flares. Scarf tails drift 1 px lateral per step.
>
> **Row 3 — `atk1` (PISTOL SHOT) × 5 frames** (cells 1–5; cells 6–8 magenta).
> - F1: raise — pistol coming up to firing line, body settling.
> - F2: aim — **fedora tilts DOWN 1 px** as he sights along the barrel (the aiming tell). Pistol at chest height, two-handed grip locked.
> - F3: **trigger pull — 4-pixel ORANGE-YELLOW muzzle flash (`#ffd76a` core, `#ff8a40` edge) at the barrel tip**. The flash is visible past the white scarf. Body does NOT rock back. Coat does NOT flare.
> - F4: recoil — pistol kicks up 2 px, fedora levels back.
> - F5: recover — back to aim posture.
>
> **Row 4 — `atk2` (CHARGED SHOT) × 8 frames** (cells 1–8, full row).
> - F1: aim begins. Two-handed grip. **Tiny 2-px BLUE GLOW (`#4a8ad0`)** at the muzzle tip.
> - F2: **3-px blue glow** at muzzle, growing.
> - F3: **5-px blue glow** at muzzle. The blue light begins tinting the lower edge of the white scarf one shade cooler.
> - F4: **7-px blue orb** at muzzle — full charge. **The white scarf's lower edge is visibly tinted cool grey-blue for this one frame.** Body still squared, arms steady.
> - F5: **RELEASE — bigger 8-px WHITE-ORANGE muzzle flash (white-hot core `#fff8c0`, orange edge `#ff8a40`)**. The blue glow is consumed in the flash.
> - F6: **RECOIL — body ROCKS BACK 10°, COAT FLARES behind in a 45° fan** (the only walk/idle/shot/whip/hipfire row where the coat flares — flare is reserved for charged recoil only). Coat lining stays hidden (not the kick — see atk5).
> - F7: settling — body returning to vertical, coat falling back.
> - F8: recover — back to two-handed aim posture.
>
> **Row 5 — `atk3` (PISTOL WHIP) × 6 frames** (cells 1–6; cells 7–8 magenta).
> - This is a **melee** strike — NO MUZZLE FLASH anywhere in this anim. The pistol is reversed in the hand.
> - F1: load — body coils, **pistol ROTATES IN THE HAND so Lamplight grips the BARREL** (the metal frame's grip is now leading forward like a brass-knuckle club). The reversed grip is the move's visual identity.
> - F2: wind-up — pistol drawn back over the shoulder, free hand braced at chest.
> - F3: **drive — body LUNGES forward 6 px**, pistol arcing in a horizontal swing.
> - F4: **PEAK IMPACT — GUN-BUTT ARCS HORIZONTALLY at HEAD HEIGHT, the metal grip leading the swing. 1-pixel WHITE IMPACT SPARK at the gun-butt.** Scarf tails whip with the lunge. Free hand still at chest. NO muzzle flash.
> - F5: follow-through — pistol past the impact line, body still lunged forward.
> - F6: recovery — body straightens back, **pistol rotates back to normal forward grip** (ready to shoot again next frame).
>
> **Row 6 — `atk4` (HIPFIRE FAN) × 7 frames** (cells 1–7; cell 8 magenta).
> - The only attack where the gun is below chest height. The only one-handed grip.
> - F1: pistol **DROPS from chest to HIP HEIGHT** in a **ONE-HANDED grip** (free hand drops to the side or rests at the belt). Body squared, no fedora tilt, no aim-down posture.
> - F2: aim set at hip level, body squared.
> - F3: **FIRST muzzle flash — 3-px orange burst, angled slightly LEFT-of-center** (gun rotated 8° counter-clockwise so the barrel points left of straight forward).
> - F4: recoil ride — gun briefly kicks up 1 px, then rotates back toward center.
> - F5: **SECOND muzzle flash — 3-px orange burst, angled STRAIGHT FORWARD** (gun centered).
> - F6: recoil ride — gun rotates further clockwise toward the right.
> - F7: **THIRD muzzle flash — 3-px orange burst, angled slightly RIGHT-of-center** (gun rotated 8° clockwise so the barrel points right of straight forward). Three distinct flashes must appear across F3, F5, F7 — they fan from left to center to right across the lane. Body squared and steady through all 7 frames.
>
> **Row 7 — `atk5` (COAT-FLARE KICK) × 5 frames** (cells 1–5; cells 6–8 magenta).
> - The ONLY leg attack. The ONLY frame in the entire sheet that exposes the coat's burgundy inner lining.
> - F1: body pivots 30° on the lead foot, rear knee starts lifting, **pistol arm crosses the body** for balance (gun pointing down-and-away across his chest).
> - F2: rear leg chambering, knee at hip height, pistol arm still crossed.
> - F3: **PEAK — REAR BOOT extended forward at GUT HEIGHT (~22 px past the body). COAT FLARES OPEN BEHIND HIM like a CAPE revealing the deep BURGUNDY INNER LINING (`#4a1018`) — both panels swept aside, lining visible across the entire back of the coat.** This is the only frame in the whole sheet where the lining shows. Pistol arm crossed at chest holding the gun out of the way. Scarf tails whipping with the pivot.
> - F4: follow-through — leg past the impact line, coat starting to fall back, lining still partially visible.
> - F5: recovery — leg returns to stance position, coat closes, lining disappears, pistol arm uncrosses back to chest.
>
> **Row 8 — `hurt` × 3 frames** (cells 1–3; cells 4–8 magenta).
> - F1: body twists 8° from the hit. Gun arm drops 4 px. Fedora and scarf stay in place. Coat does NOT flare.
> - F2: deeper recoil — body bent at the waist, gun arm at hip briefly.
> - F3: recovery — body straightens back toward stance, gun returning to chest grip.
>
> **Row 9 — `dead` × 4 frames** (cells 1–4; cells 5–8 magenta).
> - F1: legs buckle, body folding.
> - F2: collapse — body falling sideways, coat splaying.
> - F3: **FEDORA ROLLS OFF the head as the body hits the ground**, revealing a short buzz cut underneath. **The scarf stays up — the face below the eyes is STILL HIDDEN even in death.** Pistol lands on the ground beside the body.
> - F4: settled on the ground, fedora lying nearby brim-down, scarf still up, pistol on the floor.
>
> **DO NOT include:**
> - Any text, labels, row headers, frame numbers, animation names, or captions anywhere in the image. The cells must contain only the character.
> - Cell separator lines, grid borders, or coloured outlines between cells. Cells are defined by even spacing on the magenta background.
> - The face below the eyes ever — the scarf stays up in every single frame, including hurt and dead. If the mouth or nose is visible, that frame is wrong.
> - Hair anywhere except the brief buzz-cut reveal on `dead` F3 — the fedora covers everything otherwise.
> - Modern tactical gear (vests, plate carriers, knee pads, optics, holsters), modern combat boots with visible logos, or modern firearms with rails. The look is **noir** (1940s–1970s hired gun), not military.
> - Dual-wielding — single pistol only.
> - A cigarette — that belongs to Duke, not Lamplight.
> - A long flowing cape — the coat flares only on atk2 F6 recoil and atk5 F3 kick, never otherwise.
> - The burgundy coat lining in any frame except atk5 F3 and F4 — the lining reveal is reserved for the kick.
> - The pistol pointed at the camera, the player, or in any inappropriate angle — barrel goes forward in shots, gripped backwards (barrel pointing at his own wrist) in the pistol whip, crossed across the body in the kick.
>
> **Style references:** Streets of Rage 4 character pixel quality, Fight'N Rage character density, Castle Crashers tier of expressive poses. Clean silhouette, hard 1-pixel outlines in the deepest shadow colour of each body part, no anti-aliasing on the outline, 3-color palette per body part (mid / shadow / highlight). Pure magenta `#ff00ff` background — the chroma key only catches that exact magenta, not softer purples.
>
> **Output: a single PNG image, 512 × 792 pixels, exactly 8 columns × 9 rows on a magenta `#ff00ff` background.** Save as `lamplight.png`.

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
