# SPRITE GENERATION PROMPTS

Per-character prompts for the AI sprite generator (Gemini / Pixellab / similar). Each prompt is **paste-ready** and self-contained — copy the entire block-quote into the generator without edits.

Every prompt locks:
- Exact identity items (must appear in every frame)
- Hex-coded palette per body part
- A uniform grid that `auto_atlas.py` can re-slice automatically
- Per-frame poses with signature beats (so each attack reads as a different move)
- An explicit DO-NOT list (the things generators always get wrong)

Required identity items — these MUST appear in every frame (including hurt and dead):

| Character | Identity items |
|---|---|
| **RIO** | yellow bandana on LEFT wrist |
| **DUKE** | unlit cigarette behind one ear |
| **ATLAS** | silver wedding band on neck chain (visible through open flannel V) + tribal forearm tattoos |
| **BARON** | brass knuckles on both fists + diagonal scar across LEFT eyebrow + cleft chin + single white hair-streak |
| **RAZOR** | dual knives (one in each hand) + half-shaved mohawk |
| **VOLT** | cybernetic LEFT arm + both cyber legs from mid-thigh + blue power-lines |
| **BLACKWELL** | bald + heavy goatee + championship wrestling belt |
| **RUNNER** | red bandana on right bicep |
| **CHAINS** | industrial chain wrapped twice around dominant forearm |
| **SLICE** | knife (reverse/icepick grip default; flips to forward grip only on lunge) |
| **TANK** | massive bald + military-surplus vest |
| **LAMPLIGHT** | fedora pulled low + white scarf over face + pistol + popped coat collar |
| **DOJO** | gi + black belt + clean-shaven |
| **SHADE** | hooded cloak + featureless mask + purple eye-glow + cloak-hem smoke wisps |
| **RIG** | yellow construction hardhat (always on, even when hit/dead) + hi-vis orange vest |

If the generator drops the identity item, regenerate that frame.

---

## 🛑 NON-NEGOTIABLE RULES — paste these AT THE TOP of every prompt before the per-character block

The slicer found that Gemini regularly violated three rules across the last batch of regenerations: rows were skipped, the background was a dark-purple gradient instead of pure magenta, and some sheets had anim-name banners baked into the image. Including this rules block at the START of each generation request — even before the character description — fixes ~90% of the slicing problems.

> **HARD RULES — read first, do not violate. Failure on any of these requires a full regeneration:**
>
> 1. **Row count is exact, not approximate.** This prompt specifies EXACTLY N animation rows. The output PNG must contain EXACTLY N rows of character poses, top-to-bottom, in the order specified below. If the spec calls for 16 rows you must draw 16 — not 14, not 12, not "however many fit comfortably." Each anim row gets its own horizontal strip. Skipping or merging rows breaks the engine.
>
> 2. **Background is PURE MAGENTA `#ff00ff` everywhere.** Not dark purple. Not pink. Not a gradient. Not transparent. The exact RGB value `255, 0, 255` between every character, above the top character, below the bottom character, and in every cell that doesn't contain a pose. If you use any other shade the chroma-key fails and the character ships with a coloured rectangle around them. Verify the background of the output is pure magenta before submitting.
>
> 3. **No text characters anywhere in the image.** No animation labels (`IDLE`, `WALK`, `SPINNING`, `KICK`). No frame numbers (`F1`, `1`, `2`). No row headers. No captions. No watermarks. No grid coordinates. **Zero letters or numbers** in the output PNG. If you want to label cells for your own reference during planning, do it on a separate sheet and discard it — the production sheet ships text-free. The slicer renders any baked-in text as part of the sprite, so a sheet with one stray letter is unusable.
>
> 4. **Every row has the exact frame count the spec lists.** If a row says "atk1 × 4 frames" the row must have 4 distinct character poses left-to-right. Don't draw 3, don't draw 6. The same goes for unused cells in a row: leave them as pure magenta — DO NOT fill them with extra poses or with text.
>
> 5. **Characters do not touch each other vertically OR horizontally.** Leave at least 8 pixels of pure magenta between adjacent characters in a row, and at least 12 pixels of pure magenta between rows. The slicer uses these magenta gutters to find character boundaries — touching characters get merged into a single sliced frame.
>
> 6. **Every character pose is a FULL BODY** — head, torso, arms, legs, feet — unless the spec explicitly says "head only" or "knees up." Crouches, dives, and kicks still need feet visible. The bottom of every character body must be the character's lowest body point (foot, knee, hand on ground) — never cropped at the waist or shoulders.
>
> 7. **Self-check before submitting.** Count the rows top-to-bottom. Count the poses left-to-right in each row. Compare both to the spec. If either count is wrong, regenerate.

---

## Recommended grid

- **Background:** solid magenta `#ff00ff` for chroma keying. Pure magenta only — softer purples won't key.
- **Anchor:** bottom-center of each cell (the character's feet sit at the bottom-center).
- **Cells:** uniform grid, ONE animation per row. Unused cells stay magenta.
- **No text anywhere in the image** — no labels, no row headers, no frame numbers, no captions. Pixels only.
- **No cell separator lines** — cells are defined by even spacing on magenta.

After the sheet lands in `characters/<name>.png`, run `python3 auto_atlas.py <name>` to re-slice. The slicer reads each spec's REQUIRED ANIMATION ROWS list (in the `.md` file) and labels rows top-to-bottom in that order.

---

## Animation list — per-character row counts

Each character's full row list lives in `characters/<NAME>.md`. Summary:

| Character | Rows | Frame total | Cell size | Grid |
|---|---:|---:|---|---|
| **RIO** (player) | 16 | 86 | 64×96 | 8×10 grid (some rows pad) |
| **DUKE** (player) | 16 | 86 | 64×96 | 8×10 |
| **ATLAS** (player) | 15 | 80 | 80×112 | 8×10 |
| **BARON** (boss) | 14 | 81 | 80×96 | 8×6 (long rows) |
| **RAZOR** (boss) | 13 | ~70 | 64×96 | 8×9 |
| **VOLT** (boss) | 12 | ~65 | 64×96 | 8×5 (originally) |
| **BLACKWELL** (boss) | 12 | ~65 | 80×96 | 8×9 |
| **RUNNER** (enemy) | 8 | 32 | 48×64 | 8×4 |
| **CHAINS** (enemy) | 7 | 39 | 64×80 | 8×5 |
| **SLICE** (enemy) | 9 | 40 | 64×80 | 8×5 |
| **TANK** (enemy) | 7 | ~45 | 80×96 | 8×6 |
| **LAMPLIGHT** (enemy) | 9 | 48 | 64×88 | 8×9 (one anim per row) |
| **DOJO** (enemy) | 8 | ~35 | 64×80 | 8×5 |
| **SHADE** (enemy) | 12 | 54 | 48×72 | 8×12 (one anim per row) |
| **RIG** (enemy) | 10 | 56 | 64×80 | 8×10 (one anim per row) |

---

## RIO — generation prompt (current moveset)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x96 frame size, 8 columns × 10 rows uniform grid, **magenta `#ff00ff` background**, bottom-center anchor. **NO text, NO labels, NO frame numbers anywhere — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **16 rows exactly, 86 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 16 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `run` × 6 frames
>  4. `jump` × 3 frames
>  5. `atk1` × 4 frames
>  6. `atk2` × 5 frames
>  7. `atk3` × 6 frames
>  8. `atk4` × 6 frames
>  9. `heavy` × 7 frames
> 10. `jump_atk` × 4 frames
> 11. `back_atk` × 4 frames
> 12. `special` × 12 frames
> 13. `throw` × 5 frames
> 14. `counter` × 6 frames
> 15. `hurt` × 3 frames
> 16. `dodge` × 5 frames
>
> Total: **86 character poses in 16 rows**. Count both before submitting.
>
>
> **Character:** Rio. 24-year-old woman, dark brown skin (`#8a5235`), athletic boxer's frame. Full afro, dark brown to black (`#1a1410`), ~3–4 in. deep, soft round silhouette. Single small gold hoop earring (camera-side). Cropped olive-sage bomber jacket (`#7d8d4f` mid, `#5a6b3a` shadow, `#9bab6a` highlight), ends at lower ribs, two slash pockets, knit collar/cuffs/hem. Black ribbed tank top under (`#0a0a10`). Off-white hand wraps wrapping the knuckles 4 times (`#dcd6c4`). Slim charcoal cargo pants (`#1a1a22`). Ankle-high lace-up boxing boots, black with white soles.
>
> **REQUIRED identity item (every frame, including hurt and dodge):** **bright marigold yellow bandana tied around the LEFT wrist** over the hand wraps. 4–5 px wide stripe of yellow (`#e8c04a` mid, `#ffd76a` highlight, `#b89426` shadow), small 2-px knot tail. **The bandana TRAILS through fast motion** — punches, the spin, the uppercut, the dodge roll.
>
> **Tone:** calm, focused, deadpan. Smile appears ONLY for one frame on the spinning back kick finisher and the sunset spin finisher. Defensive footwork, never flat-footed.
>
> **Frame layout — 16 rows, one anim per row, 8 cells per row (unused cells stay magenta):**
>
> 1. `idle` × 4 — bouncing boxer's stance, hands at chin, weight shifts subtly. Bandana visible on left wrist.
> 2. `walk` × 6 — opposite-arm-to-leg swing AT THE SIDES, fists loose at hip level, afro bounces 1–2 px. Loops seamlessly (F6 → F1). **Arms NEVER reach forward past the body.**
> 3. `run` × 6 — body leans 5–10° forward, knees high, **arms PUMP up/down at the sides** like a sprinter (NEVER forward). F3/F6 have 2-px speedlines behind trailing heel.
> 4. `jump` × 3 — anticipation crouch, peak airborne, landing absorb.
> 5. `atk1` JAB × 4 — front fist horizontal forward at head height + **12-px yellow bandana ribbon trail behind the fist** at peak.
> 6. `atk2` CROSS × 5 — rear fist forward at head height, body rotated 45° + **bandana whips OPPOSITE the cross fist** (creates yellow X across body).
> 7. `atk3` ROUNDHOUSE KICK × 6 — leg horizontal at chest height, shin parallel to floor, body torqued 90° + yellow bandana ribbon trails the kicking foot.
> 8. `atk4` SPINNING BACK KICK × 6 — **F4 body airborne mid-spin, kicking leg VERTICAL with HEEL ABOVE THE HEAD**, body 270° rotated. **Bandana traces complete 360° CIRCLE around her body across F2–F5.** F5 the brief SMILE appears for one frame.
> 9. `heavy` UPPERCUT × 7 — body crouches deep, then front fist drives straight UP. **Bandana streaks STRAIGHT UP as a vertical yellow column from wrist to 14 px above her head.**
> 10. `jump_atk` FLYING KNEE × 4 — airborne, lead knee at chest height with lower leg tucked, both arms wide for balance, bandana trails diagonal.
> 11. `back_atk` REAR ELBOW × 4 — body twists 60° toward rear, elbow drives back behind the body.
> 12. `special` SUNSET SPIN × 12 — F1–F6 spinning leg sweep with **bandana tracing horizontal yellow halo at hip level**; F7–F12 rising double-fist uppercut with both fists driving overhead and **bandana drawn as a free-floating yellow streak 8 px above her head on F10**. F11 the brief SMILE (1 frame).
> 13. `throw` × 5 — grab, lift overhead, spin, release downward.
> 14. `counter` CHECK HOOK × 6 — boxer's textbook counter. **F4 body fully SIDEWAYS to camera (90° pivot, profile silhouette)**, lead fist hooked tight at head height with elbow bent 90°, rear hand at chin for guard. Bandana tight inward arc across face line. F5 the brief SMILE.
> 15. `hurt` × 3 — body folds at waist, head rocks back 5°, bandana lifts 4 px from wrist.
> 16. `dodge` BACKWARD ROLL × 5 — crouch, tuck, mid-roll compact ball, uncurl, back to stance. Bandana still visible during tucked frames.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; flowing capes; glowing energy fists or elemental effects (no fire, lightning, ice — she's a boxer); modern military boots (hers are sport boxing boots); long flowing hair (afro is contained); open jacket flapping wildly (cropped fit); any frame missing the yellow LEFT-wrist bandana.
>
> **Style:** Streets of Rage 4 character pixel quality, Fight'N Rage character density. Hard 1-px outlines in deepest shadow colour of each part. 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 512×960 (8×10 cells), exactly 8 columns × 10 rows on magenta. Save as `rio.png`.**

---

## DUKE — generation prompt (current moveset with kicks + cinematic flair)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x96 frame size, 8 columns × 10 rows uniform grid, **magenta `#ff00ff` background**, bottom-center anchor. **NO text anywhere.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **16 rows exactly, 86 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 16 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `run` × 6 frames
>  4. `jump` × 3 frames
>  5. `atk1` × 4 frames
>  6. `atk2` × 5 frames
>  7. `atk3` × 6 frames
>  8. `atk4` × 6 frames
>  9. `heavy` × 7 frames
> 10. `jump_atk` × 4 frames
> 11. `back_atk` × 4 frames
> 12. `special` × 12 frames
> 13. `throw` × 5 frames
> 14. `counter` × 6 frames
> 15. `hurt` × 3 frames
> 16. `dodge` × 5 frames
>
> Total: **86 character poses in 16 rows**. Count both before submitting.
>
>
> **Character:** Duke. 31-year-old man, weathered pale skin (`#d4a888`), 3–4 days of stubble (`#3a2a1c`), squared jaw, slightly broken nose. Ex-boxer's frame — heavier than Rio, leaner than Atlas. **Carries himself slightly hunched** — old knee injury changed his posture. **Right knee favors a slight bend even when standing.** Messy dark blonde hair (`#a08c4a` highlight, `#6e5e2c` shadow), 2–3 in., uneven, **a wayward strand falls across the forehead on the camera-side in every frame.**
>
> **Costume:** Stained off-white t-shirt (`#cfc8b8` mid, `#9b9482` shadow, two visible discolorations). Sleeveless faded denim cut-off jacket (`#5a6678` mid, `#404a5c` shadow, `#7886a0` highlight), **sleeves cut off with jagged frayed edges** at the shoulders. Two breast pockets. Open in front, no buttons. Brown leather belt, plain square buckle. Dark indigo straight-cut jeans (`#2a2e3a`), one visible 4-px knee tear on the RIGHT knee. Beat-up black combat boots laced halfway, scuffed toes, sole slightly worn unevenly.
>
> **REQUIRED identity items (every frame including hurt and dead):**
> 1. **An UNLIT off-white cigarette tucked behind ONE ear** (camera-side). 1-px wide, 4-px long, with a brown filter tip (`#e8e4d2` body, `#7a4a26` tip). **NEVER lit, NEVER moves, NEVER falls** — even on hurt, even on KO. The cigarette stays in place is the running gag. ONLY moves on `dead` F4 where it finally falls off.
> 2. **Wayward forehead hair strand** falls across the camera-side eye in every frame.
>
> **Tone:** tired, cynical, dirty-boxing veteran. Movement reads as economical, weight-shifted, no wasted motion. Half-grin reserved ONLY for finishers (atk4, heavy F5, special F10, counter F4, throw F3). The grin is a tell — "I shouldn't be enjoying this."
>
> **Frame layout — 16 rows, one anim per row, 8 cells per row:**
>
> 1. `idle` × 4 — boxer stance with the bad right knee bent shallower, hands at lower-belly height (not chin). Subtle shoulder rise on breath. Cigarette behind ear unmoved.
> 2. `walk` × 6 — limping cycle, left leg strides cleanly, right leg drags 1 frame behind. **Opposite arms swing at the sides** (small ROM). Loops seamlessly. Body leans 5° forward. Cigarette stays put.
> 3. `run` × 6 — body forward 10°, longer strides but right leg still 1–2 px shorter. **Arms pump UP/DOWN at the sides** (NEVER forward). F3/F6 have 3-px speedlines behind both heels. Jacket flares at the shoulders. Cigarette stays put (the running gag).
> 4. `jump` × 3 — deep crouch loading on the LEFT leg, airborne with left leg leading, landing on left foot first.
> 5. `atk1` OVERHAND LEFT × 4 — looping dirty-boxer lead. F2 left fist swings UP past the chin to ABOVE the shoulder. F3 **fist DROPS at 30° diagonal toward the imagined target's TEMPLE**, body SLIPS right 10° (defensive slip — the move's tell). Hair strand whips. F4 sharp snap-back.
> 6. `atk2` SOLAR-PLEXUS CROSS × 5 — F2 body COILS LOW (drops 6 px from idle), rear shoulder drawn back. F4 **rear fist FULLY EXTENDED at SOLAR-PLEXUS height (~32 px above floor, gut level — NOT face level)**, body rotated 45° + **CIGARETTE ASH FLECKS — 2 small grey pixels falling from behind the ear (1 frame only, the ONLY frame in the whole game the cig produces ash)**. F5 snap-back.
> 7. `atk3` OBLIQUE KICK × 6 — UFC knee-snapper. F4 **LEFT BOOT extended at 30° DOWNWARD-FORWARD angle, BOOT SOLE facing the target's lead knee** (~24 px past body, ~24 px above floor — knee height). Body half-turned 30°. Front arm extended forward across the body for balance. F1–F2: **bad right knee strains visibly (1-px outward tilt)** as the supporting leg.
> 8. `atk4` SOCCER KICK × 6 — full football-punt mechanic. F2 **BACK-SWING — left leg drawn FULLY BEHIND the body at thigh height (raised 30 px behind)** — unique chamber silhouette. F4 **LEFT BOOT at HEAD HEIGHT (~40 px above floor), TOES POINTED leading**, body LEANED BACK 20° for counterbalance, arms flared. 4-px dust at supporting boot. **HALF-GRIN at full visibility**. Cigarette unmoved.
> 9. `heavy` UPPERCUT × 7 — F1 deep crouch with both fists at hip, **bad right knee strains (1-px outward tilt)**. F4 explosive vertical rise, front fist drives straight up. F5 fist 16 px above head height, **half-grin visible**. F6 held one extra frame. F7 recovery. Cigarette unmoved.
> 10. `jump_atk` FALLING AXE KICK × 4 — F2 body airborne and VERTICAL, **LEFT LEG raised STRAIGHT UP ABOVE THE HEAD** (the inverted-leg silhouette, unique to this move). F3 **HEEL DROPS vertically** through the target. Hair strand whipped up. Half-grin briefly visible (1 frame).
> 11. `back_atk` SPINNING BACKFIST × 4 — body PIVOTS 180°. F2 mid-spin (90°, profile to camera). F3 **back of REAR fist whips horizontally at head height + 6-px hair-strand BROWN COMET STREAK trails behind the body** (the rotation tell). F4 finishes back to forward. Cigarette stays put through the spin.
> 12. `special` ROLLING THUNDER × 12 — **three forward ELBOWS** (left-right-left) with growing speedlines (3-px → 4-px → 5-px), then a haymaker finisher. F2 left elbow + 3-px streak. F4 right elbow + 4-px streak. F6 left elbow + 5-px streak. F8 haymaker load (body torqued fully back). F9–F10 right fist arcs down. F10 **dust puff at his feet (2–3 brown pixels) + half-grin at full visibility**. F11 hold. F12 recovery. Cigarette unmoved across all 12 frames.
> 13. `throw` COLLAR-HOIST KNEE-SLAM × 5 — three-beat throw, the only throw in the cast with a mid-throw strike. F1 grab collar. F2 hoist enemy chest-high. F3 **LEFT KNEE DRIVES UP into enemy's gut** (knee at hip height, imagined enemy bent over it). **Half-grin briefly visible — Duke enjoys this one.** F4 toss forward. F5 recovery. Cigarette unmoved.
> 14. `counter` LIVER SHOT KO × 6 — F3 **body at FULL CROUCH (shortest pose Duke takes, knees past 90°)**, rear fist starts forward at HIP/liver height. F4 **rear fist FULLY EXTENDED FORWARD at HIP HEIGHT (~14 px past body, ~28 px above floor — well below chest), HALF-GRIN at full visibility**. NOT an arc — a level straight low body shot. Cigarette unmoved.
> 15. `hurt` × 3 — body folds, jaw clenches, **cigarette wobbles 1 px but STAYS ON the ear (the gag)**, hair strand falls. 1-px white impact spark.
> 16. `dodge` BACKWARD STEP × 5 — bad knee won't let him roll. F1 weight to left leg, right foot lifts. F3 airborne briefly sliding back. F5 settled back into stance, **right hand still raised in a "stop" gesture**. Cigarette unmoved.
>
> **Signature beats — each appears EXACTLY ONCE in the whole sheet:**
> - Cigarette ASH FLECKS (1 frame) → atk2 F4 only
> - Hair-strand BROWN COMET streak (6 px) → back_atk only
> - Leg pointed STRAIGHT UP above the head → jump_atk only
> - Mid-attack knee strike → throw F3 only
> - Body crouched lower than any other pose → counter only
> - Body slipped RIGHT 10° → atk1 only
> - Full back-swing (leg drawn 30 px behind) → atk4 only
>
> **Kick discipline:** every kick (atk3, atk4, jump_atk, throw knee) uses the LEFT (good) leg. Right knee is the supporting leg under load and visibly strains (1-px outward tilt) on atk3 F1, atk4 F1, heavy F1.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; the cigarette lit, removed, or moved (except dead F4); glowing energy of any kind; clean/pressed clothes; boxing gloves (bare/wrapped hands only); athletic springy movement (he's tired); a full beard (it's 3–4 days stubble); right-leg kicks (always left).
>
> **Style:** Streets of Rage 4 character pixel quality. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 512×960, exactly 8 cols × 10 rows on magenta. Save as `duke.png`.**

---

## ATLAS — generation prompt (current moveset with headbutt + stomp counter)

> Pixel art sprite sheet, side-view 2D beat-em-up style, **80x112 frame size** (Atlas is bigger than the other players), 8 columns × 10 rows uniform grid, **magenta `#ff00ff` background**, bottom-center anchor. **NO text anywhere.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **15 rows exactly, 80 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 15 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `run` × 6 frames
>  4. `jump` × 3 frames
>  5. `atk1` × 4 frames
>  6. `atk2` × 5 frames
>  7. `atk3` × 6 frames
>  8. `heavy` × 7 frames
>  9. `jump_atk` × 4 frames
> 10. `back_atk` × 4 frames
> 11. `special` × 12 frames
> 12. `throw` × 5 frames
> 13. `counter` × 6 frames
> 14. `hurt` × 3 frames
> 15. `dodge` × 5 frames
>
> Total: **80 character poses in 15 rows**. Count both before submitting.
>
>
> **Character:** Atlas. 47-year-old man, **6'4", massive** — powerlifter physique slightly soft. Reads AT LEAST 30% bigger than Rio or Duke in silhouette. **BALD** with a salt-and-pepper FULL beard wrapping the lower jaw (`#a8a4a0` light, `#6e6c6a` shadow, `#4a4844` dark accent). Mediterranean/mixed olive skin (`#7a5234` light, `#583820` shadow). Heavy brow, deep-set eyes, broad nose (broken once long ago).
>
> **Costume:** **Sleeveless deep-red plaid flannel** (`#7a3030` mid, `#5a1c1c` shadow, `#9a4040` highlight) with sleeves torn off (jagged frayed edges) and **TOP THREE BUTTONS UNDONE** showing an open V of skin and chain. Hem to mid-hip. Heavy black leather belt with brass buckle. Heavy work pants, dark olive-brown (`#3a3024`) with two patches (one on right knee — lighter brown square, one on left thigh — frayed darker patch). **Steel-toed work boots** dark brown leather (`#1c140c`) with grey steel toes (`#5a5a5a`).
>
> **REQUIRED identity items (every frame including hurt and dead):**
> 1. **SILVER WEDDING BAND on a thin silver chain around the neck.** 1-px chain (`#c0c0c8`), 2×2 px band (`#d8d8e0`) at chest height. **Visible through the open V of the flannel in every frame.** Catches a 1-px highlight glint on heavy F4.
> 2. **TRIBAL FOREARM TATTOOS on BOTH bare forearms** — two horizontal bands per forearm, each 1 px tall and 6–8 px long, dark green-black ink (`#3a2a1a`). Faded — looks like old work softened over decades.
>
> **Tone:** slow, deliberate, planted. Doesn't bounce. Stands shoulder-width minimum. Moves like a man who knows everyone is watching. Resting expression: thoughtful, not angry. Small parental smile on atk3 F6 and special F11 only.
>
> **Frame layout — 15 rows, one anim per row, 8 cells per row:**
>
> 1. `idle` × 4 — slow chest rise/fall (5 fps — slowest in cast), shoulders rise 2 px on inhale, wedding band catches 1-px highlight on F2.
> 2. `walk` × 6 — heavy stomp gait, both boots flat-footed, 1-px dust at each heel-strike. Opposite arms swing at sides (slow rhythm). Loops seamlessly. Wide stance throughout. Chain swings 1–2 px laterally each step.
> 3. `run` × 6 — body angled 5° forward, body surges not bounces. Foot strikes on F1/F3 (alternating) with 3–4 px dust each. **Arms PUMP up/down at the sides** (NEVER forward). Chain bounces 2–3 px vertically per stride.
> 4. `jump` × 3 — deep crouch, body extended airborne (~6–8 px off ground, arms NOT raised overhead), landing with both knees absorbing and dust burst at both boots.
> 5. `atk1` OPEN-PALM SHOVE × 4 — F3 front (left) PALM fully extended ~16 px forward, **fingers visibly SPLAYED** (open hand, not a fist — only open-hand attack in the cast). Body angled 10° forward. Tribal forearm tattoos prominent.
> 6. `atk2` CHARGING HEADBUTT × 5 — body itself is the weapon. F1 body coils back 4 px, head tucks. F3 **body LUNGED 8 px forward with HEAD LEADING at chest-of-target height, BOTH hands GRIPPING FORWARD at chest** (palms down, fingers curled around imagined collar). Body angled 30° forward. Beard tilted forward. F4 peak impact at brow + 1-px white spark + wedding band swung 3 px forward. F5 recovery.
> 7. `atk3` OVERHEAD CHOPPING SMASH × 6 — F2 both hands above head, fists CLASPED together, body extended skyward. F3 1-frame hold at peak. F4 body folds forward at the waist, both hands drive DOWN together. F5 hands at chest-of-target height + **big dust puff at his feet (4–5 brown specks)**. F6 the **small parental smile is visible for one frame** (the gentle moment).
> 8. `heavy` UPPERCUT LAUNCHER × 7 — slowest attack in cast. F1 deep crouch, rear fist drops below knee. F4 fist drives upward + **WEDDING BAND CATCHES A 1-PX HIGHLIGHT GLINT** (the tell — when it glints, the launcher hits). F5 peak with fist directly overhead. F6 held one extra frame (Atlas pauses at the top, terrifying). F7 recovery.
> 9. `jump_atk` FLYING BODY SPLASH × 4 — Atlas doesn't kick, he becomes a falling building. F3 **body FULLY HORIZONTAL parallel to ground at peak, both arms spread WIDE like a wrestler's diving splash, chest leading the descent. Wedding-band chain flown 4 px forward off the chest**. Tribal tattoos visible on both spread arms. F4 landing with dust burst (5–6 brown specks horizontal smear).
> 10. `back_atk` REAR ELBOW × 4 — body turns 35° to rear, elbow drives backward, body twists 70°, chain swings sideways across the chest (3 px lateral travel). F3 mouth tightens. Tribal tattoos visible on striking forearm.
> 11. `special` FOUNDATION STONE × 12 — three phases. F1–F5 **forward shoulder charge** — body angled 25° forward, shoulder leading, speedlines grow from 3 → 4 → 5 lines, chain trails 2 px behind. F6 contact. F7 lift — both hands grab enemy at chest height. F8 **enemy lifted OVERHEAD 2–3 px above Atlas's head, arms fully extended skyward**. F9–F10 **SLAM IMPACT** — enemy at ground level + **DUST BURST around both boots in a wide half-circle (5–6 brown pixels each side)**. F11 **parental smile visible for one frame**. F12 recovery.
> 12. `throw` LIFTING SUPLEX × 5 — F1 grab. F2 hoist. F3 Atlas's body bends BACKWARD 30°, enemy goes overhead, chain against the chin. F4 slam down together with dust burst. F5 push back to standing.
> 13. `counter` STOMP CRUSH × 6 — the ONLY leg attack in his kit. F3 **right KNEE LIFTED to chest height, right boot dangling below the knee, body fully vertical and tall, BOTH hands STILL AT HIPS** (NOT overhead, NOT clasped — the leg is the weapon). F5 **STOMP IMPACT — right boot crashes into the ground + MASSIVE DUST BURST at the right boot (8–10 brown specks in a half-circle 40 px wide). The parental smile is at full visibility for one frame.**
> 14. `hurt` × 3 — body absorbs but barely flinches (heaviest in cast). Head turns 5°, beard tilts. Chain swings 2 px sideways.
> 15. `dodge` SIDESTEP × 5 — Atlas doesn't roll, the body won't allow it. F2 back foot crosses over in front, body slides 4 px laterally, **right forearm rises across the body to chest height (guard position)**. F3 planted briefly with tribal tattoos prominent on the guard arm. F5 settled back to stance.
>
> **Silhouette discipline — every attack occupies a DIFFERENT body axis:**
> - atk1 = vertical body + open palm forward (only open-hand)
> - atk2 = body LUNGING forward head-first (only attack where the head leads)
> - atk3 = BOTH fists clasped DESCENDING vertically
> - heavy = ONE fist ASCENDING vertically (atk3 = two going down, heavy = one going up — never confuse)
> - jump_atk = body HORIZONTAL in air (only aerial)
> - back_atk = body twisted 70° sideways
> - special = LIFTS an enemy overhead (only grapple-and-slam)
> - throw = body ARCHES BACKWARD (special folds forward; throw bends backward)
> - counter = ONE LEG raised knee-to-chest then boot drops (the only leg attack — hands stay at hips, NEVER overhead)
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; long hair / mohawk / any hair on the head (BALD); trimmed/short beard (FULL beard, slightly wild); sleeves on the flannel (torn off); closed flannel (top three buttons undone); glowing fists / elemental effects; boots without steel toe (have a visible silver/grey toe cap); athletic shorts / gym wear (heavy work pants); any frame missing the wedding-band chain or tribal forearm tattoos; counter showing clasped fists overhead (it's a STOMP — hands at hips).
>
> **Style:** Streets of Rage 4 character pixel quality, big-bruiser archetype. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 640×1120 (8 cols × 10 rows × 80×112 cells) on magenta. Save as `atlas.png`.**

---

## BARON — generation prompt (Stage-3 boss, full detail)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 80x96 frame size, 8 columns by 14 rows uniform grid (total image 640 wide × 1344 tall), **magenta `#ff00ff` background**, bottom-center anchor. Boss tier. **NO text anywhere — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **12 rows exactly, 65 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 12 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 4 frames
>  4. `atk2` × 5 frames
>  5. `atk3` × 5 frames
>  6. `heavy` × 7 frames
>  7. `jump_atk` × 4 frames
>  8. `back_atk` × 4 frames
>  9. `special` × 12 frames
> 10. `throw` × 5 frames
> 11. `counter` × 6 frames
> 12. `hurt` × 3 frames
>
> Total: **65 character poses in 12 rows**. Count both before submitting.
>
>
> **Character — FICTIONAL Dick-Tracy-villain noir-comic caricature** ("William 'Baron' Halsey"). NOT a real public figure. Reference points: **Flattop / Pruneface / The Brow from Dick Tracy**, or 60s/70s comic-book Kingpin enforcers. Stylised proportions, NOT realistic. 50s reading age. **Body silhouette is a TRAPEZOID** — shoulders comically wider than hips. Wider than the protagonists by 50%, heavier than Atlas. **Neck WIDER THAN THE HEAD** (one continuous slope from shoulder to skull — no taper). **Jaw SQUARE WITH A 90° CORNER**, lantern-jaw caricature. Pale ivory skin (`#e0c8a0`) flat noir-comic shading, ruddy on cheeks. Heavy brow, eyes small and close-set. **Resting expression: a small polite smile that never reaches the eyes.**
>
> **Identity markers — fictional caricature, REQUIRED in every frame:**
> 1. **Diagonal scar across the LEFT eyebrow** — 4-px white line cutting from above the eye down toward the cheek, splitting the eyebrow in half.
> 2. **Cleft chin** — 1-px vertical groove in the centre of the chin.
> 3. **Salt-and-pepper hair** (`#4a4a50` base, `#2a2a30` shadow) with a **SINGLE BRIGHT-WHITE STRIPE** (`#e8e8e4`) running from the right temple back across the top of the head — comic-book villain hair flash. Slicked back severely, high widow's peak.
> 4. **Brass knuckles on BOTH fists** (`#cfa040` mid, `#8a6020` shadow, `#f4d870` highlight) — oversized comic-book silhouette, NOT realistic gauntlet shape.
> 5. **Tan duster coat** (`#8a6a3a` mid, `#4a3a18` shadow, `#ad8a4f` highlight) — mid-shin length (longer than modern fashion), open in front, period noir-comic feel. Swings 1 frame behind body movement.
>
> **Costume:** high-collar white dress shirt (`#e8e2d4`) slightly stained, top two buttons open showing a **3-px white chest scar** above the sternum, no tie. Dark charcoal pleated slacks (`#2a2a30`). Black polished wing-tip oxford shoes scuffed at the toe. Plain leather belt with comically large silver buckle (`#8a8a8e`).
>
> **Frame layout — 14 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — boxer's bounce on the balls of the feet (1 px up/down), hands at chin in textbook guard, gold knuckles catching highlight on F2. Coat sways 1 px at hem. Square jaw + scar + white hair-streak visible.
> 2. `walk` × 6 — casual approach almost a stroll, coat trails 2 px behind, hands at chin in low guard. Opposite arms swing at sides. Loops seamlessly.
> 3. `atk1` JAB × 4 — front fist horizontal forward at HEAD level. F2 **fist extends with 1-px GOLD GLINT on the brass knuckles at HEAD height** — the only bright colour in the frame. F3 full extension, knuckles vertical. F4 sharp snap-back. Body barely twists, coat does NOT move.
> 4. `atk2` CROSS × 5 — rear fist horizontal forward at HEAD level. F3 peak — **rear fist crosses centerline, COAT FLARES BEHIND in a 45° FAN as the body rotates fully, gold knuckles forward at head level, body rotated 45°, square jaw juts forward 1 px**. F5 snap-back, coat resettles.
> 5. `atk3` LIVER HOOK × 5 — BODY shot at HIP level (different from atk1/atk2 head shots). F1 **body SQUATS DOWN 10° (knees bend, shoulder drops)**. F3 peak — **gold knuckles at HIP LEVEL (~28 px above floor — the only Baron punch at hip height), body torqued 60°, opposite arm thrown back for balance**. F5 body rises back.
> 6. `uppercut` RISING UPPERCUT × 6 — only Baron punch going UP. F1 deep coil, lead fist drops to thigh height. F4 **explosive rise — lead fist drives STRAIGHT UP past head height, gold-knuckle VERTICAL STREAK from hip-start to head-end**. F5 held one frame at peak. F6 recovery.
> 7. `haymaker` OVERHAND × 9 — longest tell in the kit. F1–F4 **wind-up — COAT OPENS FULLY (both panels swept aside) across all four frames revealing the chest scar at the open collar**. F5 peak — right arm at full overhand extension above the shoulder, body rotated past 90°, **gold-knuckle trail (3-px comet arc)** from shoulder-high down to chest-of-target. F6–F8 follow-through. F9 recovery, coat closing back.
> 8. `clinch` CLINCH + RISING KNEE × 7 — F1 both hands rise to chest height, palms open. F2 **arms CLAMP onto imagined opponent's shoulders (hands close into fists holding the collar)**. F3 **PULL DOWN HARD — body folds forward, imagined opponent dragged down**. F4 rear knee starts driving UP. F5 **peak — knee 18 px past body line at gut-of-target height, BOTH hands still gripping the collar (target bent at the waist), coat flaring open at the front**. F6 release. F7 recovery.
> 9. `special` BONE-BREAKER × 12 — the signature finisher: 5 RAPID brass-knuckle strikes at 5 DIFFERENT heights. F1–F2 deep stance load, both arms cocked. F3 **STRIKE 1: jab to face — gold glint #1 at HEAD level**. F4 **STRIKE 2: cross to face — gold glint #2 at HEAD level, body torqued opposite**. F5 **STRIKE 3: liver hook — gold glint #3 at HIP level**. F6 **STRIKE 4: uppercut — gold glint #4 VERTICAL streak rising**. F7–F8 body coils backward for the finisher, both arms wind back, coat flares open. F9 **STRIKE 5: HAYMAKER — gold glint #5 (BIGGEST) + COAT FLARES FULLY BEHIND like a cape, body rotated 90°**. F10 hold finisher. F11–F12 recovery. Five gold flashes at five different heights — head, head, hip, vertical, head (piano-scale of glints).
> 10. `counter` COAT PARRY-RIPOSTE × 6 — magician's deflect-and-strike. F1 lead arm raises in defensive guard. F2 **the COAT FANS WIDE in front of the body in a 90° sweep — for 1 frame his TORSO IS HIDDEN BEHIND THE COAT** (magician's misdirection — the move's identity). F3 coat starts to drop, brass knuckles glint behind the coat. F4 **CROSS PUNCH erupts THROUGH the coat with gold-knuckle trail**. F5–F6 coat resettles.
> 11. `jump_atk` AERIAL KNEE × 4 — short-hop forward, rear knee drives forward at chest height (no grab, body airborne — distinct from clinch's grounded grab-knee). Coat flares behind.
> 12. `hurt` × 3 — body folds, **hair STAYS NEAT** (his signature — never disheveled), polite smile remains, hands drop briefly from guard, scar stays visible. 1-px white impact spark on the brass knuckles.
> 13. `taunt` × 5 — **combs hair with right hand** — checks the white streak. F1–F2 right hand rises to hair. F3 held comb pose. F4–F5 hand returns to guard. Polite smile throughout.
> 14. `dead` × 5 — falls hard. F3 on his side. F4 coat splays open, **brass knuckles fall from his hands and roll out 8 px ahead of him** (the iconic image). F5 settled. Polite smile finally drops on the very last frame for ONE frame.
>
> **DO NOT include:** any resemblance to a real public figure (if a draft looks like a known person, exaggerate jaw / neck / shoulders / scar further until it doesn't); realistic body proportions (Baron is a noir-comic caricature); text/labels/frame numbers; cell separator lines; variation of Baron across frames (same square jaw, scar, white hair-streak, coat in every cell); visible firearm (brass-knuckles only); wrinkled or dirty trench coat; modern tactical gear / modern shoes / modern haircut; tattoos; a scowl (the polite smile IS the menace).
>
> **Style:** Streets of Rage 4 character pixel quality + Dick-Tracy noir-comic caricature proportions. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 640×1344 (8 cols × 14 rows), on magenta. Save as `baron.png`.**

---

## LAMPLIGHT — generation prompt (full detail)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x88 frame size, 8 columns by 9 rows uniform grid (total image 512 wide × 792 tall), **magenta `#ff00ff` background**, bottom-center anchor. Mid-tier enemy. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **9 rows exactly, 48 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 9 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 5 frames
>  4. `atk2` × 8 frames
>  5. `atk3` × 6 frames
>  6. `atk4` × 7 frames
>  7. `atk5` × 5 frames
>  8. `hurt` × 3 frames
>  9. `dead` × 4 frames
>
> Total: **48 character poses in 9 rows**. Count both before submitting.
>
>
> **Character — noir gunslinger:** Lamplight. Age 35–50 (read as a veteran), 5'10"–6'1", lean but not athletic — steady-hands, soldier's-stance build. Gender-ambiguous on purpose. Face is **almost entirely hidden** — only a narrow horizontal eye-strip is visible between the fedora brim above and the scarf below. Skin tone in that strip is medium tan (`#d4a888`).
>
> **Costume:** Black fedora pulled low (brim shadows the upper face). Long charcoal-black trench coat (`#1a1a22` body, `#0a0a10` shadow, `#2a2a36` highlight) mid-calf length, collar popped up, belt cinched at the waist with a steel buckle. **Deep burgundy inner lining (`#4a1018`) — visible ONLY on atk5 F3/F4.** Long white scarf (`#dcd6c4` body, `#9a9482` shadow) wrapped twice around the neck, pulled up over the nose and mouth, two loose tails 14–18 px down the coat front. Black leather gloves. Dark tactical pants below the coat hem. Heavy black combat boots. **Single black semi-auto pistol** (body `#3a3a40`, barrel `#4a4a50`), two-handed at chest by default.
>
> **REQUIRED in every frame including hurt and dead:** fedora on head, white scarf up over nose and mouth, pistol in hand, popped coat collar.
>
> **Frame layout — 9 rows, 1 anim per row, 8 cells per row, unused cells stay pure magenta:**
>
> 1. `idle` × 4 — stand with pistol two-handed at chest, fedora level, coat hanging straight. F2 subtle inhale (shoulders +1 px). F3 hold. F4 exhale (shoulders −1 px).
> 2. `walk` × 6 — composed gunslinger gait that loops seamlessly. Pistol stays two-handed at chest. Shoulders rotate slightly each step. F1 LEFT foot fwd + RIGHT shoulder rotates fwd 1 px. F2 passing. F3 RIGHT foot fwd + LEFT shoulder fwd. F4 passing. F5 mirror of F1. F6 passing (blends back into F1). Coat hem sways 2 px behind trailing leg. **Coat never flares in walk.** Scarf tails drift 1 px per step.
> 3. `atk1` PISTOL SHOT × 5 — F1 raise pistol toward firing line. F2 aim — **fedora tilts DOWN 1 px** to sight along the barrel. F3 **trigger pull — 4-pixel ORANGE-YELLOW muzzle flash (`#ffd76a` core, `#ff8a40` edge) at the barrel tip**, visible past the scarf. Body does NOT rock back. F4 small recoil — pistol kicks up 2 px. F5 back to aim posture.
> 4. `atk2` CHARGED SHOT × 8 — F1 aim begins, **2-px BLUE GLOW (`#4a8ad0`)** at muzzle. F2 **3-px blue glow**. F3 **5-px blue glow** — lower edge of the white scarf begins tinting one shade cooler. F4 **7-px blue orb at full charge — scarf's lower edge visibly tinted grey-blue for this one frame**. F5 **RELEASE — bigger 8-px WHITE-ORANGE muzzle flash** (white-hot core `#fff8c0`, orange edge `#ff8a40`), consuming the blue. F6 **RECOIL — body ROCKS BACK 10°, COAT FLARES behind in a 45° fan** (only flare in the sheet outside atk5). F7 settling. F8 back to aim posture.
> 5. `atk3` PISTOL WHIP × 6 — NO MUZZLE FLASH anywhere. F1 **pistol ROTATES IN THE HAND — Lamplight now grips the BARREL** so the metal grip leads forward like a brass-knuckle club (this reversed grip is the move's identity). F2 wind-up — pistol drawn back over the shoulder, free hand braces at chest. F3 **body LUNGES forward 6 px**, pistol arcs horizontally. F4 **PEAK — GUN-BUTT at HEAD HEIGHT, metal grip leading, 1-pixel WHITE IMPACT SPARK at the gun-butt**. Scarf tails whip. F5 follow-through. F6 recovery — **pistol rotates back to normal forward grip**.
> 6. `atk4` HIPFIRE FAN × 7 — F1 **pistol DROPS from chest to HIP HEIGHT, ONE-HANDED grip**, free hand at side, body squared, no fedora tilt. F2 aim set at hip. F3 **FIRST muzzle flash — 3-px orange burst angled LEFT-of-center** (gun rotated 8° counter-clockwise). F4 recoil ride, gun rotates back. F5 **SECOND flash — 3-px orange STRAIGHT FORWARD** (centered). F6 recoil rotates further clockwise. F7 **THIRD flash — 3-px orange angled RIGHT-of-center** (gun rotated 8° clockwise). Three flashes must appear at F3/F5/F7 fanning left→center→right. Body squared and steady throughout.
> 7. `atk5` COAT-FLARE KICK × 5 — F1 body pivots 30° on lead foot, rear knee lifts, **pistol arm crosses the body** (gun pointing down-and-away across his chest). F2 rear knee chambered at hip height. F3 **PEAK — REAR BOOT extended forward at GUT HEIGHT (~22 px past body), COAT FLARES OPEN BEHIND like a CAPE revealing the deep BURGUNDY INNER LINING (`#4a1018`) — both panels swept aside, lining visible across the entire back of the coat**. This is the ONLY frame in the whole sheet where the lining shows. Pistol crossed at chest. Scarf tails whipping. F4 follow-through, lining still partly visible. F5 recovery, coat closes, lining gone.
> 8. `hurt` × 3 — F1 body twists 8°, gun arm drops 4 px, fedora and scarf stay. Coat does NOT flare. F2 deeper recoil. F3 recovery — body straightens, gun returning to chest grip.
> 9. `dead` × 4 — F1 legs buckle. F2 collapse, body falling sideways. F3 **FEDORA ROLLS OFF the head revealing a short buzz cut underneath — the scarf STAYS UP**, pistol lands beside the body. F4 settled on the ground, fedora brim-down nearby, scarf still up.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; the face below the eyes (scarf stays up always); hair anywhere except the brief buzz-cut reveal on dead F3; modern tactical gear or modern firearms with rails; dual-wielding (single pistol); a cigarette (Duke's identity); a flowing cape (coat flares only on atk2 F6 and atk5 F3); the burgundy lining in any frame except atk5 F3–F4; pistol pointed at camera.
>
> **Style:** Streets of Rage 4 character pixel quality. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 512×792 (8 cols × 9 rows), on magenta. Save as `lamplight.png`.**

---

## SHADE — generation prompt (full detail, 12 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 48x72 frame size, 8 columns by 12 rows uniform grid (total image 384 wide × 864 tall), **magenta `#ff00ff` background**, bottom-center anchor. Mid-tier enemy. **NO text anywhere.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **12 rows exactly, 54 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 12 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 4 frames
>  4. `atk2` × 4 frames
>  5. `atk3` × 5 frames
>  6. `atk4` × 5 frames
>  7. `atk5` × 5 frames
>  8. `atk6` × 6 frames
>  9. `vanish` × 5 frames
> 10. `reappear` × 3 frames
> 11. `hurt` × 3 frames
> 12. `dead` × 4 frames
>
> Total: **54 character poses in 12 rows**. Count both before submitting.
>
>
> **Character — stealth operator:** Shade. Age indeterminate (body 25–35, eyes look older). 5'9"–5'11", lean-athletic whip-quick build. Gender-ambiguous on purpose. Body language is composed — doesn't bounce, stands flat with arms loose at the sides, weight perfectly centered.
>
> **Costume:** Hooded utility cloak — matte black (`#16161a` mid, `#08080a` shadow, `#2a2a2f` highlight), draped, hood always up, hangs to lower thigh. Skin-tight black bodysuit under, visible at neck/arms/legs. Featureless dark grey mask (`#2a2a2f`) covering nose and mouth — no logo, no decoration. Soft-soled tactical shoes (black, no laces). Black leather gloves, fingertips removed, knuckles wrapped with thin tape.
>
> **REQUIRED identity items (every frame including vanish/reappear/hurt/dead):**
> 1. **PURPLE EYE-GLOW** — two 1–2 px dots, `#6a3080` core with `#3a2050` edge. The ONLY saturated colour on Shade. Steady in idle, brighter during vanish.
> 2. **Cloak hood UP**.
> 3. **Mask UP** — no face visible below the eyes EVER, even in death.
> 4. **Black-purple smoke wisps** (`#3a2a4a` body, `#1a0e22` edge) trailing from the cloak hem during all movement frames.
>
> **Frame layout — 12 rows, one anim per row, 8 cells per row:**
>
> 1. `idle` × 4 — hood breathes (rises 1 px on F2), eye-glow steady, cloak hem sways 1 px, purple wisp curls from the hem on F3.
> 2. `walk` × 6 — smooth predator glide that loops seamlessly. F1 LEFT foot fwd + RIGHT shoulder rotates fwd 1 px. F2 passing. F3 RIGHT foot fwd + LEFT shoulder fwd. F4 passing. F5 mirror of F1. F6 passing (blends into F1). Arms hang AT THE SIDES inside the cloak. Feet barely visible under the hem. Small purple smoke wisps from the hem on F1/F3/F5.
> 3. `atk1` SHADOW CHOP × 4 — open knife-hand at neck height. F1 front hand cocks back across chest. F3 **peak — chopping hand fully extended forward at NECK height with FINGERS EXTENDED (open hand, NO blade) and edge-of-hand leading, cloak hem fanned 180° BEHIND in a comet-tail arc**. F4 retract.
> 4. `atk2` MATERIALISING BACKSTAB × 4 — F1 **blade visible FIRST emerging from a purple smoke wisp, body STILL <40% ALPHA** (only the blade and eye-glow are clearly visible). F2 body solidifies fully, blade leading. F3 **forward thrust — blade 18 px past body in clenched fist forward grip, free arm flung BACK for balance**. F4 retract.
> 5. `atk3` CLOAK-CYCLONE HOOK KICK × 5 — F1 body coils, supporting foot pivots, kicking leg starts rising sideways. F2 body starts rotating. F3 **peak — body rotated mid-spin, kicking leg HORIZONTAL at HEAD height with HEEL leading (whip-style), free arm extended for balance, CLOAK FANNED IN A FULL 360° PURPLE HALO around the body (motion blur, purple ribbon halo)**. F4 follow-through. F5 recovery.
> 6. `atk4` CLOAK-WHIP LOW SWEEP × 5 — F1 body drops into a crouch, supporting hand reaches for floor. F2 body LOW with supporting HAND BRACED ON FLOOR. F3 **peak — body CROUCHED LOW (lowest pose Shade ever takes), supporting HAND ON FLOOR, CLOAK HEM extended HORIZONTALLY at ANKLE HEIGHT in a 140° arc with purple-smoke trail behind the whipping hem** (the cloak ITSELF is the weapon). F4 cloak past sweep line. F5 body rises back.
> 7. `atk5` TWIN-BLADE FAN × 5 — F1 body squared, both arms cross in front of the chest, fists clenched. F2 **TWO blades MATERIALISE SIMULTANEOUSLY at BOTH wrists from purple smoke wisps** (mirror of backstab tell, doubled — both blades visible at once). F3 **peak — both arms FULLY EXPLODED OUTWARD in opposite directions forming a "T" SILHOUETTE, left blade pointing left and right blade pointing right (~16 px past body each side), purple smoke trailing behind both blades**. F4 hold extension 1 frame (hit window for both sides). F5 arms retract, blades dissipate back into purple smoke.
> 8. `atk6` PHANTOM-CLONE BACKSTAB × 6 — F1 real Shade in center, cloak gathering, eye-glow pulses brighter. F2 **body SPLITS — THREE side-by-side silhouettes: LEFT clone @40% alpha (offset -14 px), CENTER clone @70% alpha, RIGHT clone @40% alpha (offset +14 px)**, all identical pose, blade visible at each one's front hand. F3 three silhouettes hold, all three blades raised together (the deception window). F4 **CONVERGENCE — LEFT and RIGHT clones FADE to 0% sliding toward center, CENTER silhouette brightens to 100% alpha**. F5 real Shade drives the blade forward in a thrust. F6 retract.
> 9. `vanish` × 5 — F1 inhale, cloak puffs outward. F2 body fades to 60% alpha, hem dissolving into smoke. F3 body 30% alpha, only the head/cloak outline + eye-glow legible. F4 body gone, just eye-glow + thick purple smoke. F5 **eye-glow alone, NO body** (the iconic vanish frame).
> 10. `reappear` × 3 — F1 eye-glow + smoke only. F2 body reforms at 50% alpha behind the smoke. F3 full opacity, smoke dissipating.
> 11. `hurt` × 3 — F1 body folds. F2 **hood briefly drops back 4 px** exposing more of the upper mask (but NEVER the face below the eyes). F3 recovery.
> 12. `dead` × 4 — body crumples. **Cloak pools out around the body in a wide circle.** Eye-glow fades — bright on F1, dim on F2, gone by F3. Purple smoke dissipates upward across the frames.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; different Shade designs across frames (same cloak silhouette, same eye-glow placement, same wisp colour in every cell); visible scifi / glowing energy weapons (the only glow is the eyes); capes / dramatic flowing robes (the cloak is fitted utility); bright colors anywhere (black, grey, dark purple ONLY); the face below the eyes in any frame; multiple shades / clones outside atk6 F2–F4.
>
> **Style:** Streets of Rage 4 character pixel quality, stealth-operator archetype. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background — Shade should look almost invisible against magenta because of how dark the palette is. That's intentional; the eye-glow IS the silhouette.
>
> **Output: single PNG, 384×864 (8 cols × 12 rows), on magenta. Save as `shade.png`.**

---

## RIG — generation prompt (full detail, 10 rows with new cinematic moves)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x80 frame size, 8 columns by 10 rows uniform grid (total image 512 wide × 800 tall), **magenta `#ff00ff` background**, bottom-center anchor. Mid-tier enemy. **NO text anywhere.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **10 rows exactly, 56 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 10 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 5 frames
>  4. `atk2` × 5 frames
>  5. `atk3` × 5 frames
>  6. `atk4` × 6 frames
>  7. `atk5` × 6 frames
>  8. `atk6` × 12 frames
>  9. `hurt` × 3 frames
> 10. `dead` × 4 frames
>
> Total: **56 character poses in 10 rows**. Count both before submitting.
>
>
> **Character — construction-crew muscle:** Rig. Age 28–45, 6'0"–6'4", thick — pure-mass build from manual labor. Shoulders broader than Tank, gut tighter. Heavy and slow. Weathered face, scruffy stubble or full beard (pick one and lock it). Hair mostly hidden under the hardhat.
>
> **Costume:** **Yellow hardhat** (`#cfa040` body, `#e8c860` highlight, `#8a6020` shadow) — battered, scuffed at the brim, small black "KANE PROPERTIES" logo (`#1a1a22`, ~3 px square) on the front-left of the brim. **Hi-vis safety vest** fluorescent orange (`#ff7a30` mid, `#ffa050` highlight, `#b04a10` shadow) over a brown long-sleeve work shirt (`#7a5a3a`, sleeves rolled to the elbow). Two reflective grey stripes (`#a8a8a8`) horizontal across the front of the vest. Brown forearms exposed (hairy). Dirty khaki-brown work pants (`#7a5a3a`) with darker oil-stain patches. **Steel-toed work boots** heavy brown leather (`#3a2a1c`) with grey steel toes (`#5a5a5a`) — bigger than Atlas's, chunkier sole. Heavy leather work belt with empty hammer loops (no tools today).
>
> **REQUIRED identity items (every frame, including hurt and dead):**
> 1. **Yellow hardhat ALWAYS on the head** — never falls off, never knocked aside. Even on hurt, even on dead.
> 2. **Hi-vis orange vest** with two horizontal grey reflective stripes.
> 3. **Bare fists** — Rig never carries a wrench, hammer, brick, or any tool. The hands ARE the tools.
>
> **Tone:** mutters during fights ("Just doin' the job", "Move it, kid"). Not malicious; bored. Doesn't chase fast — walks, trusts his weight to do the work.
>
> **Frame layout — 10 rows, one anim per row, 8 cells per row:**
>
> 1. `idle` × 4 — heavy chest rise, hardhat brim catches a 1-px yellow highlight on F2, shoulders rolled forward, both fists hang at thigh height half-clenched.
> 2. `walk` × 6 — heavy worker stomp gait that loops seamlessly. F1 LEFT leg fwd + RIGHT arm fwd swing (at side, hip-level). F2 passing. F3 RIGHT leg fwd + LEFT arm fwd swing. F4 passing. F5 mirror of F1. F6 passing (blends into F1). Hardhat stays LEVEL (does NOT tilt forward during walk — forward tilt is the atk1 tell). Boots flat-footed, **1-px brown dust speck at the planted boot heel on F1/F3/F5**. Vest jiggles 1 px on impact.
> 3. `atk1` HARDHAT RAM-JAB × 5 — F1 **head LOWERS, hardhat tilts forward like a battering ram** (head dropped below shoulder line), body bends at waist, fists rise. F2 step forward (hardhat leading). F3 **peak — lead fist drives forward UNDER the hardhat brim**, hardhat still angled forward, free arm trailing for balance. F4 retract fist. F5 head rises back, hardhat re-levels.
> 4. `atk2` STEEL-TOE BOOT KICK × 5 — F1 kicking leg raises (knee to chest), supporting leg planted, body leans back 5°. F2 leg begins extending forward. F3 **peak — leg STRAIGHT FORWARD at HIP HEIGHT, boot SOLE leading FLAT at the target (a horizontal boot-print pointing at the target), body leaned back 10°, both arms thrown back, 2-px brown dust at supporting boot**. F4 leg retracts. F5 boot plants back, body returns to stance.
> 5. `atk3` IRON-CLAP THUNDER × 5 — F1 both arms drawn out to the sides at shoulder height, palms facing inward, body squared. F2 arms beginning to swing IN toward each other. F3 **peak — BOTH FISTS MEET IN FRONT OF THE CHEST with a 4-px WHITE IMPACT SPARK at the meeting point + TWO horizontal brown dust shockwave arcs radiating LEFT AND RIGHT at chest height (~24 px each side, 2-px arc thickness)**. Body squared, knees braced. F4 fists hold together for 1 frame (the concussion). F5 arms drop back to thigh height, recovery.
> 6. `atk4` CONCRETE-BREAKER OVERHEAD × 6 — F1 both fists rise from hip toward chest, body coiling. F2 **both fists CLASPED ABOVE THE HARDHAT, body stretched fully tall, hardhat steady on the head**. F3 clasp held 1 frame (the launch tell). F4 **DRIVE — clasped fists arc DOWN in a vertical comet path, body folding forward 30° at the waist, ending at chest/head height of the imagined target** (NOT floor level — that's atk6). 1-px white impact spark at the fists. **Hardhat tilts forward 1 px on the fold-through**. F5 follow-through, clasped fists past the impact line. F6 arms unclasp and drop to thigh height, body straightens.
> 7. `atk5` WRECKING-BALL SHOULDER CHARGE × 6 — F1 body lowers (knees bend), **RIGHT SHOULDER drops forward**, hardhat angles forward. Free (left) arm pulls back behind for balance. F2 forward step — body angled 25° forward, motion-blur streaks beginning behind both boots (1 px). F3 **CHARGE — body angled 35° forward with RIGHT SHOULDER LEADING (shoulder LOWER than the chin), hardhat brim pointed at imagined target, body MOVED 6 px forward; 3-px brown motion-blur streaks behind BOTH boots**. F4 impact — body MOVED 12 px total from start, shoulder driving through the target, 1-px white impact spark at the shoulder, motion-blur streaks at peak intensity. F5 follow-through — body still moving forward, shoulder past the impact line. F6 recovery — body straightens, free arm settles, streaks fade.
> 8. `atk6` PNEUMATIC-DRILL POUND × 12 (AOE finisher) — F1 both arms start rising, knees bend. F2–F3 arms continue up, body straightening (small dust specks at boots starting). F4 arms above head, fists clasping (more ground specks). F5 **vertical column pose — fists clasped above hardhat, body stretched fully UP from heels to hands**. F6 held column (1 frame, the launch tell). F7–F8 drive downward (body folds, fists arcing all the way down to boot level). F9 body fully folded, fists AT BOOT LEVEL. F10 **IMPACT — FLOOR-LEVEL shockwave dust ring radiating 36 px on each side at boot height (2-px arc thickness), vertical dust plume rising up to hardhat height**. F11 recovery start. F12 back to standing.
> 9. `hurt` × 3 — stagger, head turns 10°, **HARDHAT STAYS ON** (his signature — never falls off). 1-px white impact spark on the vest. F3 returns to stance.
> 10. `dead` × 4 — falls FORWARD onto the ground (face down, hardhat lands first). **Hardhat stays on the head through all 4 frames.**
>
> **Signature beats — each appears EXACTLY ONCE in the whole sheet:**
> - Hardhat tilted forward as a ram → atk1 only
> - Boot SOLE flat at the target → atk2 only
> - TWO horizontal shockwave arcs at CHEST height radiating left AND right → atk3 only
> - Clasped fists arcing DOWN to head-height (NOT floor) → atk4 only
> - Body MOVING forward 12 px with motion-blur streaks behind both boots → atk5 only
> - FLOOR-LEVEL shockwave ring + vertical dust plume → atk6 only
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; a bareheaded Rig in any frame (yellow hardhat is on the head in every single cell, including hurt and dead); a different worker across frames (same face, beard choice, hat, vest, pants in every cell); tactical / military gear (Rigs are construction workers); visible weapons or tools (wrenches, hammers, bricks — bare fists only); clean / pressed clothing (worn-in and stained); the hardhat replaced by a beanie or other headgear.
>
> **Style:** Streets of Rage 4 character pixel quality, blue-collar construction archetype. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 512×800 (8 cols × 10 rows), on magenta. Save as `rig.png`.**

---

## RAZOR — generation prompt (full detail, 13 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x96 frame size, 8 columns by 13 rows uniform grid (total image 512 wide × 1248 tall), **magenta `#ff00ff` background**, bottom-center anchor. Stage 7 boss. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **12 rows exactly, 66 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 12 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 4 frames
>  4. `atk2` × 5 frames
>  5. `atk3` × 6 frames
>  6. `heavy` × 7 frames
>  7. `jump_atk` × 4 frames
>  8. `back_atk` × 4 frames
>  9. `special` × 12 frames
> 10. `throw` × 5 frames
> 11. `counter` × 6 frames
> 12. `hurt` × 3 frames
>
> Total: **66 character poses in 12 rows**. Count both before submitting.
>
>
> **Character — corporate-suit knife fencer:** Razor (real name Eliza Park). 38-year-old Korean woman, 5'7", lean yoga/kickboxing build — athletic but never bulky. Sharp jawline, dark eyes, neutral resting expression with a small deliberate smile only when she lands a hit. Light olive skin (`#dcb088` mid, `#a07858` shadow).
>
> **Hair:** Sleek straight **BLACK BOB** (`#1a1410`) ending exactly at the jawline — never longer, never looser. **TWO BLEACHED BLONDE STREAKS (`#c8a060`)** at the front, one each side, ~3 px wide. The blonde streaks are her tell — visible in every single frame.
>
> **Costume head-to-feet:** Tailored two-button black suit jacket (`#1a1a22` mid, `#08080a` shadow, `#2a2a32` highlight), fitted, single vent, lapels clearly drawn. Black silk V-neck camisole under (`#16161a`). Slim straight-cut black slacks (`#1a1a22`). Polished black low-heeled oxford-style shoes (`#0a0a10`). Fitted black leather gloves with fingertips exposed only at the tips (`#16100a`). Suit must look pressed and CLEAN even on hurt frames — corporate-immaculate.
>
> **REQUIRED in every frame (including hurt and dead):**
> 1. **TWO FOLDING KNIVES** — blades ~10 px, dark steel (`#cfd0d6`) with mirror-bright edge highlight (`#ffffff`); handles dark grey (`#2a2a2f`) with deep burgundy inlay (`#4a1018`). One in each hand during all combat frames; sheathed at the small-of-back belt during idle/walk only.
> 2. **Bleached blonde hair streaks** — visible at the front of the bob in every cell.
> 3. **Gold "K" lapel pin (`#f4c860`)** — ~2 × 3 px on the LEFT lapel, every cell.
>
> **Tone:** Calm. Polite. Lethal. Hands clasped behind her back in idle (knives concealed). When she draws, body language flips into a fencing stance — front foot 45°, rear foot perpendicular, heels in line. Doesn't bounce. Doesn't rush. The small deliberate smile appears at exactly four moments across the whole sheet: atk1 F3 (cross-cut peak), atk5 F5 (pirouette complete), special F13 (X-burst finisher), counter F4 (low leg-cut peak).
>
> **Frame layout — 13 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — heels together, toes splayed slightly (formal posture), **hands clasped behind her back, knives concealed**. F2 subtle inhale (shoulders +1 px). F3 hold. F4 exhale (shoulders −1 px). Suit perfectly clean. Blonde streaks and gold pin visible.
> 2. `walk` × 6 — composed heel-toe walk that loops seamlessly. **Hands stay clasped behind the back, knives concealed.** F1 LEFT foot fwd + RIGHT shoulder rotates fwd 1 px. F2 passing. F3 RIGHT foot fwd + LEFT shoulder fwd. F4 passing. F5 mirror of F1. F6 passing → blends into F1. Jacket hem trails 1 px behind trailing leg. Arms NEVER swing forward (they stay clasped behind). No planted/stomp pose on F6.
> 3. `draw` × 4 — F1 body shifts into fencing stance (front foot 45°, rear foot perpendicular). F2 hands swing around to the small-of-back belt and pull both folding knives free. F3 **ready pose — FRONT blade horizontal forward at hip height, REAR blade vertical guard at the shoulder, both blades fully visible**. F4 settle into the stance. (Plays once on combat start.)
> 4. `atk1` CROSS-CUT SLASH × 4 — single-blade signature. F1 **front blade cocks back over the right shoulder, rear blade stays at the hip** (this is the only attack where ONE blade stays still). F2 diagonal slash begins, blade tip tracing 14 px down-and-left across the body. F3 **PEAK — single 28-px DIAGONAL RED MOTION ARC (`#a83040` core, `#c84a58` highlight) from upper-right to lower-left at chest height drawn by the front blade tip; rear blade still at hip; small deliberate smile visible for one frame**. F4 return to fencing stance, both blades visible. **No second arc — atk1 is the single-blade signature.**
> 5. `atk2` TWIN-BLADE FLURRY × 8 — three alternating slashes. F1 stance squares, both blades chamber at the hips. F2 LEFT blade cocks up. F3 **STRIKE 1 — LEFT blade arcs from upper-left to lower-right at chest height, thin 2-px red motion-line (`#a83040`)**. F4 left retracts as RIGHT blade cocks up. F5 **STRIKE 2 — RIGHT blade arcs from upper-right to lower-left at chest height (opposite diagonal of strike 1)**. F6 right retracts as LEFT blade cocks again. F7 **STRIKE 3 — LEFT blade arcs again at hip height (lower than strike 1 — the third arc is stacked BELOW the first two)**. F8 recovery, both blades return to hip guard. **Visual identity: criss-cross of three stacked red arcs at chest level — the only multi-arc chain at chest height.**
> 6. `atk3` FENCING KICK × 5 — the only kick in her kit + the only attack where the blades are static. F1 front foot lifts, knee chambered toward chest, **BOTH blades held still in fencing guard (front blade forward at hip, rear blade vertical at shoulder)**. F2 leg begins extending. F3 **PEAK — FRONT LEG fully extended STRAIGHT FORWARD at HIP HEIGHT, FOOT FLEXED with HEEL LEADING (the en-garde foot-thrust silhouette), supporting leg straight, both blades STILL in fencing guard**. F4 leg retracts to chamber. F5 foot plants back, return to stance.
> 7. `atk4` MISSILE DASH × 9 — the only airborne attack. F1 stance widens, both blades raise. F2 body coils, knees bend deep. F3 launch — body angles 45° forward, both knives leading. F4 **body FULLY HORIZONTAL parallel to ground mid-air, BOTH blades extended forward as a leading X, legs trailing horizontally behind — the X-arrow silhouette**. F5 held missile pose, 4-px white motion-line streaks (`#ffffff`) trailing both blade tips. F6 held, streaks at peak intensity. F7 land — front foot plants, blades still extended forward. F8 stance recovery. F9 back to fencing stance.
> 8. `atk5` SPINNING PIROUETTE × 8 — grounded 360° + AOE. F1 supporting foot pivots, body starts rotating, **both blades EXTEND outward perpendicular to the body at HIP height**. F2 body 90° through rotation (profile to camera), blades still extended at hip level. F3 body 180° (facing away). F4 body 270°. F5 **body completes 360° (back to original facing), small deliberate smile visible for one frame**. F6 blades start drawing back in. F7 settle into fencing stance. F8 back to ready. **Visual identity: across F1–F5 the blades trace a continuous CIRCLE around her at hip height — a red halo of motion (`#a83040` smear at the hip-line ring).**
> 9. `throw` KNIFE THROW × 5 — the only attack where Razor is missing a knife. F1 body squares to target, rear arm cocks the knife at ear height, **front blade stays at the hip in fencing guard**. F2 arm begins forward motion. F3 **RELEASE — knife drawn 18 px ahead of the now-empty throwing hand, blade angled 30° pointing forward, 6-px white motion-line trail (`#ffffff`) behind the projectile; throwing hand visibly empty**. F4 follow-through, throwing arm fully extended forward, hand still empty, blade further down-screen. F5 return to stance, throwing hand still empty (second blade still at hip).
> 10. `special` BLADE DANCE × 14 — six-strike kata diagram, the showpiece. F1–F2 wide stance load, both blades raised at shoulder height. F3 **STRIKE 1: FRONT-blade slash upper-right to lower-left (red arc #1, diagonal — same angle as atk1 but cleaner)**. F4 wind-up for next. F5 **STRIKE 2: REAR-blade slash upper-left to lower-right (red arc #2, opposite diagonal)**. F6 wind-up. F7 **STRIKE 3: FRONT-blade horizontal cut at HIP height (red arc #3, horizontal, low)**. F8 wind-up. F9 **STRIKE 4: REAR-blade horizontal cut at NECK height (red arc #4, horizontal, high)**. F10 wind-up. F11 **STRIKE 5: FRONT-blade VERTICAL cut downward (red arc #5, vertical, top-to-bottom)**. F12 body coils, both blades raise behind shoulders. F13 **STRIKE 6 FINISHER: BOTH BLADES THRUST FORWARD TOGETHER — biggest red X-BURST of the six (`#c84a58` core, `#a83040` edge, 12-px across), small deliberate smile visible for one frame**. F14 recovery, body settling back into fencing stance. **Visual identity: 6 red arcs at six different angles forming a kata-diagram pattern — diagonal, opposite diagonal, horizontal-hip, horizontal-neck, vertical, X-burst. Each arc must hit a DIFFERENT height/angle.**
> 11. `counter` SCISSOR-PARRY + LOW LEG-CUT × 6 — the new counter (no projectile). F1 both blades rise toward the chest, weight shifts to the front foot. F2 **BOTH BLADES CROSSED IN A TIGHT X OVER THE CHEST (the scissor-block, the only X-block pose in her kit) — 3-px white spark (`#ffffff`) at the blade-crossing point as the imagined incoming strike is caught**. F3 step-past — front foot plants past the imagined opponent, body lowering, blades uncrossing. F4 **PEAK — body fully CROUCHED LOW (the shortest pose Razor ever takes, knees past 90°), FRONT blade whips HORIZONTALLY across THIGH height as a tight 16-px red arc (`#a83040`) at leg level (the only blade arc below the knee in the entire sheet), rear blade trailing at hip guard, small deliberate smile visible for one frame**. F5 follow-through, front blade past the target line, body still low. F6 body rises, return to ready fencing stance, BOTH knives still in hand (no projectile — that's `throw`'s job).
> 12. `hurt` × 3 — F1 body twists 15° from the hit, **both knives stay in her hands (she never drops them)**, suit STAYS CLEAN (her signature — even mid-hit the tailoring is perfect). F2 deeper recoil, 1-px white spark (`#ffffff`) at the contact point. F3 body straightens, blades return to fencing guard.
> 13. `dead` × 5 — F1 body folds at the waist. F2 falls to one knee. F3 collapses onto her side. F4 **BOTH knives slide 8 px from her open hands** (the only frames where she releases them — handles visible separate from the gloves). F5 settled on the ground, knives lying beside her, suit still clean, bob hair fanned across the floor.
>
> **Signature beats — each appears EXACTLY ONCE in the whole sheet:**
> - Single 28-px diagonal red arc with the rear blade staying at the hip → atk1 only
> - Criss-cross of THREE stacked red arcs at chest level → atk2 only
> - Front leg horizontal at hip height with foot FLEXED + heel leading + both blades static → atk3 only
> - Body fully horizontal mid-air with both blades extended as an X → atk4 only
> - Red halo ring of blade-motion at hip height → atk5 only
> - Detached knife with a 6-px motion-line, throwing hand visibly empty → throw only
> - Six red arcs at six different angles (kata diagram) → special only
> - Both blades crossed in an X over the chest + body crouched LOW with one blade horizontal at THIGH height → counter only
>
> **Cross-checks before approving the sheet:**
> - atk1 = ONE arc with ONE blade. atk2 = THREE alternating arcs with BOTH blades.
> - atk3 = the ONLY kick + the ONLY attack where the blades don't move.
> - atk4 = airborne with the body horizontal. atk5 = grounded with the body vertical rotating in place.
> - counter KEEPS both knives (X-block + low leg cut at thigh height). throw RELEASES one knife as a projectile. If counter shows a knife flying, redraw — the counter no longer throws.
> - counter F4 is the lowest pose Razor takes in the entire sheet — the cut lands at THIGH height, the only blade arc below the knee.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; disheveled hair / wrinkled suit (she's poised even when hurt); visible piercings or heavy makeup (corporate-clean); bright colors anywhere except the gold lapel pin, burgundy knife inlays, and red blade-arc VFX; a second weapon style (knives only — no gun, no whip); any frame missing the dual knives during combat rows (idle and walk are the only rows where knives are sheathed); the counter throwing a projectile (counter keeps both blades — it cuts low at the legs).
>
> **Style:** Streets of Rage 4 character pixel quality, Fight'N Rage character density. Hard 1-px outlines in deepest shadow colour of each part. 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 512×1248 (8 cols × 13 rows), on magenta. Save as `razor.png`.**

---

## VOLT — generation prompt (full detail, 12 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x96 frame size, 8 columns by 12 rows uniform grid (total image 512 wide × 1152 tall), **magenta `#ff00ff` background**, bottom-center anchor. Stage 9 boss. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **12 rows exactly, 66 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 12 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 4 frames
>  4. `atk2` × 5 frames
>  5. `atk3` × 6 frames
>  6. `heavy` × 7 frames
>  7. `jump_atk` × 4 frames
>  8. `back_atk` × 4 frames
>  9. `special` × 12 frames
> 10. `throw` × 5 frames
> 11. `counter` × 6 frames
> 12. `hurt` × 3 frames
>
> Total: **66 character poses in 12 rows**. Count both before submitting.
>
>
> **Character — cybernetic enforcer:** Volt (real name Daniel Vega). 34-year-old Latino man, 6'1" with the prosthetics (originally 5'10"). Athletic-toned upper body (organic), heavy cyber limbs below. Medium-brown skin (`#a87858` mid, `#6e4e30` shadow). Short scruff (`#2a201a`), tired eyes, gauntness from rehab months. Buzz-cut black hair (`#1a1410`), ~2 px short. Resting expression: focused, not angry.
>
> **Costume:** Sleeveless dark grey tactical shirt (`#2a2a32` mid, `#16161a` shadow), fitted across the chest. Right (organic) arm bare and visible. Black cargo shorts (`#16161a`) ending at mid-thigh where the cyber legs begin — the organic-to-mechanical TRANSITION IS VISIBLE and not hidden. Black tactical belt with a small power-pack module on the right hip (`#1a1a22` body with a single bright blue LED `#6aa0e8`).
>
> **REQUIRED in every frame (including hurt and dead):**
> 1. **CYBERNETIC LEFT ARM** — matte gun-metal grey (`#5a5e6a` mid, `#2a2e36` shadow, `#8a8e9a` highlight), mechanical joints visible at the shoulder, elbow, wrist; the hand is articulated plates instead of skin. **Thin blue power-line glow (`#4a8ad0`) running along the forearm** — pulses dim on F1/F3 and brighter cyan on F2/F4 of idle (heartbeat rhythm), brighter still during attack wind-ups.
> 2. **CYBERNETIC LEGS (BOTH)** — same gun-metal palette, replaced from mid-thigh down. Heavy plate construction, exposed pneumatic pistons at the knees, glowing blue power-lines (`#4a8ad0`) along the outside of each thigh and calf. Feet are stylized armored plates, NOT boots.
> 3. **Hip power-pack with the single blue LED (`#6aa0e8`)** — visible every frame.
>
> **Tone:** Heavy below the waist (cyber legs are powerful but lack organic bounce — every step PLANTS), natural movement above. The mismatch is the character. Quiet. Doesn't taunt. Speaks once at the start of the fight: "Kane built me. So I owe him a building."
>
> **Frame layout — 12 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — heavy planted stance, organic right arm relaxed, cyber left arm slightly raised (always at the ready). **Power-lines pulse blue** — dim cyan on F1/F3, brighter cyan on F2/F4 (heartbeat rhythm). Shoulder rises 1 px on breath. Hip LED steady blue.
> 2. `walk` × 6 — **asymmetric cyber-leg stomp gait that loops seamlessly**. F1 LEFT (cyber) leg lands HEAVY with a 1-px white highlight (`#8acbf4`) on the cyber knee joint + RIGHT arm forward swing at side. F2 passing. F3 RIGHT (organic) leg lands SOFT + LEFT (cyber) arm forward swing at side. F4 passing. F5 mirror of F1. F6 passing → blends into F1. Power-lines pulse one beat brighter on every cyber-leg step (F1 / F5). Arms NEVER extend forward past the body. No planted/stomp pose on F6.
> 3. `atk1` CYBER-HAYMAKER × 6 — single forward cyber-fist strike. F1 cyber arm cocks back, **powerlines start brightening from dim cyan to electric-white (`#8acbf4` → `#ffffff` core)** — the charge tell, visible from across the screen. F2 arm fully cocked, **powerlines at PEAK WHITE intensity, body torqued 30° on the hip drive**, organic arm pulled back as counter-weight. F3 forward drive — cyber fist driving forward, **4-px blue plasma trail (`#4a8ad0` core, `#8acbf4` highlight) behind the cyber knuckles**. F4 **PEAK — cyber fist 18 px past body at chest height of imagined target, body torqued, plasma trail at full extension**. F5 retract, plasma trail fading. F6 powerlines dim back to idle cyan, stance recovery. **Only single-fist forward strike in the kit.**
> 4. `atk2` TWIN-FIST LAUNCHER UPPERCUT × 8 — both fists ascending into an overhead V. F1 deep crouch (both arms drop, knees bend hard). F2 load — both fists at hip, body coiled, powerlines on cyber arm at peak white. F3 explosive rise begins, both arms swinging up. F4 both arms rising past chest. F5 **PEAK — UPWARD V SILHOUETTE, both fists vertical above the head, body fully extended skyward, WHITE LIGHTNING STAR-BURST (6-px white core `#ffffff` fading to blue `#4a8ad0` edge) erupting from the CYBER ELBOW JOINT**. F6 held peak, star-burst still visible. F7 arms lowering. F8 recovery, back to stance. **Only ascending attack + only twin-fist attack.**
> 5. `atk3` PLASMA ORB × 8 — the only projectile attack. F1 cyber arm raises, palm forward and open, **2-px blue orb (`#4a8ad0` core, `#8acbf4` halo) forming at the palm center**. F2 **orb GROWS to 4 px, first 1-px white lightning arc visible from orb to forearm**. F3 **orb at 6 px, 2 lightning arcs from orb to forearm**. F4 **PEAK CHARGE — orb at 8 px, white-hot core (`#ffffff`), blue-cyan halo (`#4a8ad0`/`#8acbf4`), 3 lightning arcs jumping from orb to forearm**. F5 **RELEASE — orb LEAVES the palm, drawn 12 px ahead of the cyber hand as a free-flying projectile, palm still glowing faintly, no arcs left at the palm**. F6 recovery, palm dimming. F7 cyber arm lowering. F8 back to stance. **Visible 2→4→6→8 px charge growth is mandatory + the orb must be DETACHED from the hand by F5.**
> 6. `atk4` CYBER AXE KICK × 5 — the only kick. F1 cyber leg starts rising, **powerlines on the cyber thigh BRIGHTEN from dim cyan to electric-white as the servos load**. F2 leg continues rising straight up past the head. F3 **PEAK — CYBER (LEFT) LEG fully VERTICAL above the head, foot at the top of the silhouette, 1-px white glow (`#ffffff`) at the cyber knee-joint**. F4 leg DRIVES DOWNWARD with the heel leading, **vertical 4-px BLUE PLASMA TRAIL (`#4a8ad0` core, `#8acbf4` highlight) behind the descending heel**. F5 IMPACT — heel at chest-of-target height, body slightly leaned back for balance, plasma trail dissipating.
> 7. `atk5` THUNDER CLAP × 7 — bilateral AOE. F1 both arms wide apart at shoulder height, **powerlines on cyber arm BRIGHT WHITE**. F2 arms start swinging inward toward chest. F3 arms approaching each other at center, both fists clenching, body crouching slightly. F4 **CLAP — both fists meet at chest centerline + WHITE LIGHTNING STAR-BURST (6-px white core `#ffffff`, blue edge `#4a8ad0`) at the impact point + 6-px shockwave rings (`#8acbf4`) radiating LEFT and RIGHT SIMULTANEOUSLY to ~24 px on each side**. F5 shockwaves continue outward at smaller intensity (4-px rings further out at ~36 px). F6 recovery, arms drop. F7 back to stance. **Only bilateral / symmetric AOE — shockwaves go ONLY left+right, never a full ring.**
> 8. `clinch` LIGHTNING CLINCH GRAB × 8 — sustained-current grab. F1 cyber arm extends forward, palm OPEN. F2 **cyber hand CLAMPS SHUT on the imagined opponent's shoulder, powerlines BRIGHTEN to white instantly**. F3 held grip — imagined opponent locked in the cyber-grip at arm's length (silhouette of a held target dangling at the cyber fist). F4 **CURRENT FLOWS — 4 small white lightning arcs (`#ffffff`) jump from the cyber hand UP the imagined opponent's body**. F5 current peaks, 5 arcs, opponent visibly convulsing in the grip. F6 current peak +1, 5 arcs at full intensity. F7 RELEASE — cyber hand opens, opponent flies back, arcs dissipate. F8 recovery, cyber arm lowering. **Only grab + only sustained-current attack — arcs travel UP across F4–F6.**
> 9. `special` OVERDRIVE SURGE × 12 — the 360° ring finisher. F1 cyber arm raised vertically at the side, powerlines start brightening. F2 powerlines reach normal-bright cyan. F3 **powerlines GO WHITE-HOT (`#ffffff`), cyber arm visibly trembling (1-px jitter)**. F4 **cyber arm RAISED OVERHEAD, body coiled, ELECTRICITY ARCING ALL AROUND the body (8+ visible white arcs)**. F5 **cyber arm POINTS DOWN at the floor, body explodes outward**. F6 **FIRST WAVE — expanding LIGHTNING RING (`#8acbf4` outer, `#ffffff` inner) radiates outward from Volt at chest height, 16-px diameter ring of pure blue-white electricity**. F7 ring at 24 px out, arcs jumping in all directions. F8 ring at 32 px out, peak. F9 ring fading at 40 px. F10 arcs dissipating. F11 recovery, body returning to stance. F12 powerlines dim back to idle cyan. **Only full 360° ring AOE — the ring must visibly encircle Volt and expand omni-directionally.**
> 10. `counter` CYBER-REFLECT + ELBOW SMASH × 6 — shield-plane block + close-range elbow. F1 cyber arm rises across the body in defensive guard, powerlines starting to brighten. F2 **cyber palm faces OUTWARD forming a flat SHIELD-PLANE — 3 horizontal white lightning arcs (`#ffffff`) in a flat plane suspended in front of the chest** (the only flat-plane VFX in his kit). F3 incoming strike IMPACTS the shield-plane, **3-px white spark burst (`#ffffff`) at the contact point**. F4 **cyber arm FOLDS — forearm pulls back hard so the ELBOW LEADS, then drives FORWARD at close range into the opponent's sternum, 3-px white discharge spark (`#ffffff`) at the cyber elbow tip, body folded slightly forward — close-range, NOT a fully extended fist**. F5 follow-through, elbow held one frame, shield-plane dissipating. F6 recovery, arm returns to guard. **NO free projectile — that's atk3's job. The elbow is the contact point, NOT a forward-thrown fist.**
> 11. `hurt` × 3 — F1 body recoils, **cyber limbs LESS affected (organic side flinches harder)**, 1-px white impact spark (`#ffffff`) on the cyber armour. F2 powerlines FLICKER (brightness drops then surges in a 1-frame glitch). F3 recovery, powerlines back to idle cyan pulse.
> 12. `dead` × 6 — F1 falls to knees, cyber legs visibly LOCKING. F2 collapses forward onto chest. F3 **CYBER LIMBS SPASM — 3-px white spark (`#ffffff`) at the cyber elbow joint**. F4 **second spasm — 3-px white spark at the cyber knee joint**. F5 sparks fading, powerlines dimming. F6 powerlines FULLY DARK, body settled face-down.
>
> **Signature beats — each appears EXACTLY ONCE in the whole sheet:**
> - Single cyber fist forward horizontal at chest height with 4-px blue plasma trail → atk1 only
> - Both arms in an overhead V + white star-burst at the cyber elbow → atk2 only
> - Free-flying detached blue orb projectile + visible 2→4→6→8 px charge → atk3 only
> - Cyber LEG fully vertical above the head + vertical heel plasma trail → atk4 only
> - Symmetric bilateral shockwaves left AND right from a chest-centerline clap → atk5 only
> - Cyber hand clamped on a held target at arm's length + lightning arcs jumping UP → clinch only
> - Full 360° expanding lightning ring at chest height → special only
> - Flat shield-plane of 3 lightning arcs in front of the chest + close-range cyber ELBOW → counter only
>
> **Cross-checks before approving the sheet:**
> - atk1 = ONE cyber fist HORIZONTAL at chest height. atk2 = BOTH fists ASCENDING vertical into an overhead V. Opposite axes.
> - atk3 throws a FREE projectile forward. Counter holds a flat SHIELD-PLANE then strikes with an ELBOW (not a fist, not a projectile). If counter shoots anything free, redraw.
> - atk4 = the only kick + the only leg vertical above the head. atk2 puts ARMS overhead in a V, not a leg.
> - atk5 = LEFT+RIGHT shockwaves only (bilateral). special = FULL 360° ring (omni-directional). If atk5 shows a ring, redraw.
> - counter F4 elbow is CLOSE-RANGE (forearm folded back, elbow leads). NOT a long-extended fist (that's atk1).
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; full-body armor (the organic torso + cyber limbs mix IS the silhouette); a cape or coat (utility-grade); a face mask (face fully visible); multiple visible weapons (his body IS the weapon); glowing RED anywhere (blue power-lines only); the counter throwing a free projectile (that overlaps atk3 — counter must use the close-range elbow instead).
>
> **Style:** Streets of Rage 4 character pixel quality. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 512×1152 (8 cols × 12 rows), on magenta. Save as `volt.png`.**

---

## BLACKWELL — generation prompt (full detail, 12 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 80x96 frame size, 8 columns by 12 rows uniform grid (total image 640 wide × 1152 tall), **magenta `#ff00ff` background**, bottom-center anchor. Stage 8 boss / brutal-only encounter. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **12 rows exactly, 66 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 12 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 4 frames
>  4. `atk2` × 5 frames
>  5. `atk3` × 6 frames
>  6. `heavy` × 7 frames
>  7. `jump_atk` × 4 frames
>  8. `back_atk` × 4 frames
>  9. `special` × 12 frames
> 10. `throw` × 5 frames
> 11. `counter` × 6 frames
> 12. `hurt` × 3 frames
>
> Total: **66 character poses in 12 rows**. Count both before submitting.
>
>
> **Character — wall of muscle:** Blackwell (real name Marcus Blackwell). 44-year-old Black man, 6'5", massive — heavier than Atlas, heavier than Tank. Pure-mass strongman build that hasn't gone soft. Arms thicker than the protagonist's torso. Reads as the BIGGEST silhouette in the game. Very dark skin (`#3a2418` mid, `#4a2c1a` shadow stages, `#1a0e08` deep, `#6a4a30` light). Square jaw. **Shaved head COMPLETELY SMOOTH (no hair anywhere on the scalp). Thin gray-black goatee (`#2a201a` dark, `#5a5450` grey accent) wrapping the chin only.** Small scar above the LEFT eyebrow. Resting expression: BLANK — he doesn't show anything until he hits.
>
> **Costume head-to-feet:** **Black tactical turtleneck** (`#0a0a10` body, `#050507` shadow, `#1c1c22` highlight), long sleeves, fitted, neck up to the chin. Modern high-end fabric. **Tactical chest holster rig** over the turtleneck — leather (`#1a1410` body, `#2a1f15` strap accent) with EMPTY pistol holsters on each side (he doesn't draw guns; the empty holsters ARE the threat). Slim black tactical pants (`#0a0a10`), tucked into boots. Heavy combat boots (`#050507` with `#1c1c22` polish highlights), polished, laced full to the calf. Fitted black leather gloves with NO fingertips exposed (`#16100a`).
>
> **REQUIRED in every frame (including hurt and dead):**
> 1. **THE CROSSED-ARMS IDLE POSE** — arms folded tight across the chest. This IS Blackwell's silhouette. He uncrosses ONLY to attack; arms re-cross by the final frame of every attack row. Idle, walk F1–F3, hurt all 3 frames, and counter F1–F2 all show the crossed-arm pose.
> 2. **HEAVY GOLD RING on the RIGHT PINKY** — `#cfa040` mid with `#8a6020` shadow and a 1-px black engraving (`#1a1a22`) for the Kane Properties insignia. 2 × 2 px. The only color on him — visible during all attacks (the punching hand is the right hand).
> 3. **Tactical chest holster rig with EMPTY holsters** — visible in every frame including hurt and dead.
> 4. **Bald head + goatee** — every frame, no exceptions.
>
> **Tone:** Still. Patient. Doesn't bounce, doesn't shift weight, doesn't taunt. **Never speaks. Never shows emotion.** Every motion is committed — he doesn't telegraph; he just MOVES.
>
> **Frame layout — 12 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — **arms crossed tight over chest** (the defining silhouette). Subtle chest rise on F2 (+1 px). **Gold ring catches a 1-px highlight (`#f4d870`) on F2.** Stance wide and rooted. Blank expression.
> 2. `walk` × 6 — slow deliberate gait that loops seamlessly. **Arms STAY CROSSED on F1–F3, then UNCROSS on F4 to swing naturally with the stride for F4–F6** (so walk reads visibly different from idle). F1 LEFT leg fwd + arms still crossed. F2 passing. F3 RIGHT leg fwd + arms still crossed. F4 passing + arms uncross. F5 LEFT leg fwd + RIGHT arm fwd swing at side. F6 passing + arms beginning to recross → blends back into F1's crossed pose. Boots flat-footed, heavy.
> 3. `atk1` STEPPING HOOK + KNUCKLE SPARK × 6 — single forward strike. F1 arms uncross fully. F2 lead foot steps forward 16 px, **rear arm cocks back behind the shoulder, gold ring on the right pinky visible at the cocked fist**. F3 peak — torso rotated 60°, rear (right) fist mid-arc at chest height, body leaned 15° into the punch. F4 **CONTACT — 4-px WHITE STAR-BURST (`#ffffff` core, `#a8a8b0` edge) at the GOLD-RING side of the fist** (his impact-spark signature — no other character emits this). F5 retract, arm pulling back. F6 arms RE-CROSS to idle pose.
> 4. `atk2` RISING KNEE STRIKE × 5 — wrestler-style knee, both hands grip and pull down. F1 arms uncross, body lowers into wrestler crouch. F2 **both hands rise to grab the imagined opponent's shoulders (open hands clamping at chest height)**. F3 **PEAK — REAR KNEE driven UPWARD 20 px past body line at gut height, both hands STILL GRIPPING the imagined collar and PULLING DOWN onto the rising knee, body folded forward 25°**. F4 held strike, knee still up, hands still pulling down. F5 knee plants back, arms RE-CROSS. **Only attack where Blackwell is HOLDING and STRIKING simultaneously — hands pull DOWN, knee drives UP.**
> 5. `atk3` CONCRETE-BREAKER CHARGE × 12 — forward shoulder charge that scars the floor. F1 arms uncross. F2 stance widens. F3 lead shoulder LOWERS to chest height. F4 body fully horizontal-low at 35°, arms swept behind. F5 launch — motion lines + **first 6-px JAGGED FLOOR CRACK (`#5a5a5a` dark, `#1a1a22` deepest line) appearing under the rear boot**. F6 stride 2, **second floor crack appearing under the next boot footfall (8-px, bigger)**. F7 stride 3, **third floor crack (10-px, biggest — three jagged dark cracks remain visible behind him on the floor)**. F8 approaching impact, body still angled forward. F9 **IMPACT — body upright, dust burst (5–6 brown specks `#7a5a3a`) + 1-frame screen-jitter suggestion (entire sprite jitters 1 px right)**. F10 follow-through. F11 recovery start. F12 arms RE-CROSS. **Only attack that scars the floor while traveling — the 3 jagged cracks must each appear at a different footfall and remain visible after the charge.**
> 6. `atk4` APOCALYPSE OVERHEAD × 13 — question-mark wind-up into the floor. F1 arms uncross. F2 both arms rising. F3 arms continuing up. F4 arms approaching vertical. F5 **PEAK WIND-UP — body fully vertical, both arms STRAIGHT UP overhead, fists CLASPED at apex, body ARCHED BACKWARDS like a question-mark**. F6 held peak. F7 held peak. F8 held peak. F9 body folds forward, fists arcing down. F10 fists past head, body bent forward. F11 fists past chest, body bent further. F12 **IMPACT INTO THE FLOOR — both clasped fists DRIVEN INTO THE GROUND + 8 LIGHT-GREY (`#a8a8b0`) CONCRETE-CHUNK chips radiating in a star pattern (N, NE, E, SE, S, SW, W, NW — each chunk 2–3 px) + brown dust burst (10–12 specks `#7a5a3a` reaching 50 px out) + vertical dust plume past head height**. F13 straighten, dust + chunks still in the air, arms beginning to re-cross. **Only attack that breaks the floor open from above — the impact ends with both fists IN the floor and concrete chunks in a star pattern.**
> 7. `throat_lift` ONE-HANDED THROAT-LIFT SLAM × 9 — single-hand vertical lift. F1 arms uncross, **LEAD hand REACHES forward at neck height**. F2 **lead hand CLAMPS SHUT on the imagined opponent's throat (SINGLE hand, not two — fingers visibly wrapped around an imagined neck)**. F3 **LIFT — opponent dangles VERTICALLY with FEET OFF the ground, held one-handed at arm's length, LEGS visibly LIMP (dangling below the held position)**. F4 held lift (the intimidation beat — opponent suspended in the silhouette). F5 body coils for the slam. F6 **SLAM ARC — arm swings forward + down, opponent following the arc downward**. F7 **IMPACT — opponent CRASHES onto the floor, dust burst at the impact zone (4–5 brown specks `#7a5a3a`)**. F8 release, hand opens. F9 arms RE-CROSS. **Only one-handed grab + only attack with a visibly suspended opponent.**
> 8. `earthquake` DOUBLE-FOOT EARTH STOMP × 8 — AOE from the feet. F1 arms uncross, body coils — knees deep, arms swing up. F2 body fully coiled, weight loaded. F3 body explodes upward — **briefly AIRBORNE (small jump, 4 px off the floor)**. F4 APEX — both feet tucked under. F5 **TOUCHDOWN — both feet slam DOWN SIMULTANEOUSLY + FIRST SHOCKWAVE RING — 12-px circle of dust (`#7a5a3a`) radiating from his feet at ground level**. F6 **second ring at 24 px out (fainter)**. F7 **THIRD + FOURTH + FIFTH rings at 36 / 48 / 56 px out — 5 CONCENTRIC EXPANDING DUST RINGS visible simultaneously in this frame at ground level radiating outward 360°**. F8 rings dissipate, arms RE-CROSS. **Only AOE that fires from the FEET — rings are at ground level only, nothing at chest height.**
> 9. `special` JUGGERNAUT CHARGE-GRAB-SPIN-THROW × 16 — wrestler's Giant Swing, the signature. F1 arms uncross. F2 stance widens deep. F3 **CHARGE START — body lowered, first ground crack appearing**. F4 launch, motion lines, second ground crack. F5 **CONTACT — both arms reach forward to GRAB**. F6 **GRAB the opponent's LEG (body bent over the imagined leg, hands clamped around an imagined ankle at waist height)**. F7 **LIFT — opponent now hanging UPSIDE-DOWN, held by ONE ankle, head dangling near the floor**. F8 SPIN start, opponent beginning to rise. F9 **SPIN 90° — opponent extended outward like a PROPELLER BLADE, body horizontal at Blackwell's chest height, 16-px motion-blur arc (`#a8a8b0`) tracing the opponent's head through the air**. F10 **SPIN 180° — opponent on the opposite side, 24-px motion-blur arc**. F11 **SPIN 270° — opponent's trajectory is now a near-complete CIRCLE of arc-lines around Blackwell at chest height**. F12 **THROW — Blackwell RELEASES the ankle, opponent FLIES off-screen at chest height as a projectile** (silhouette of the opponent's body leaving the frame). F13 Blackwell stumbles back from centrifugal force, arms wide. F14 recovery. F15 stance returning. F16 arms RE-CROSS. **Only attack where the OPPONENT'S BODY is the silhouette tell — they trace a full 360° circle around Blackwell.**
> 10. `counter` IRON WALL SHOCKWAVE + COUNTER-CROSS × 7 — starts from the crossed-arm idle. F1 **arms cross TIGHTER (defensive guard — the only attack that begins from the crossed-arm pose)**. F2 **incoming attack IMPACTS the crossed forearms — 8-POINTED WHITE STAR-BURST (`#ffffff` core, 8 spike-points radiating N/NE/E/SE/S/SW/W/NW, each 4-px) at the contact point + 3 CONCENTRIC SHOCKWAVE RINGS expanding outward (8-px, 14-px, 20-px rings in `#a8a8b0`) — instant ripple**. F3 held parry pose (the "I caught that" beat — arms still crossed, star-burst fading). F4 arms EXPLODE outward, rear (right) arm winds up far behind. F5 **RETURN PUNCH — single devastating cross with GOLD-RING glint (`#f4d870` 1-px highlight on the ring) + 3 GHOST-FIST motion-blur trails (`#1a1a22` at 60% / 40% / 20% alpha) behind the moving fist (decreasing alpha, impossible-speed motion-blur effect)**. F6 held punch, ghost-fists fading. F7 arms RE-CROSS. **Only attack starting FROM the crossed-arm idle + only attack with 8-pointed star-burst + 3 shockwave rings + only attack with ghost-fist trails. The parry star has 8 points (atk1's impact spark has 4 points — different counts).**
> 11. `hurt` × 3 — almost no flinch (he's a wall). F1 head turns 5°, **crossed arms STAY CROSSED even when struck**. F2 1-px white impact spark (`#ffffff`) on the forearms. F3 returns to idle pose, arms still crossed.
> 12. `dead` × 7 — the first significant flinch IS the death animation. He goes down slowly in stages. F1 folds at the waist (arms finally uncross). F2 falls to one knee. F3 onto both knees. F4 forward to all fours. F5 elbows give. F6 forehead touches the ground. F7 settled face down.
>
> **Signature beats — each appears EXACTLY ONCE in the whole sheet:**
> - 4-pixel white impact STAR-BURST at the gold-ring fist → atk1 only
> - Both hands gripping a collar + rear knee driving up → atk2 only
> - 3 jagged floor cracks appearing under the footsteps + 1-frame screen-jitter → atk3 only
> - Question-mark backward arch with both arms vertical + both fists driven INTO the floor + 8 concrete-chunk star → atk4 only
> - One-handed throat grip + opponent dangling vertically with legs LIMP → throat_lift only
> - 5 concentric expanding ground-level dust rings → earthquake only
> - Opponent held UPSIDE-DOWN by one ankle + opponent's body traces a 360° circle at chest height → special only
> - 8-POINTED white star-burst + 3 shockwave rings on a CROSSED-FOREARM parry + 3 ghost-fist trails on the counter-cross → counter only
>
> **Cross-checks before approving the sheet:**
> - atk1's spark = 4 points. counter's parry burst = 8 points + 3 concentric rings. Different counts.
> - atk2 PULLS DOWN onto a rising knee (both hands at shoulder height). throat_lift LIFTS UP (one hand at neck height). Opposite verticals.
> - atk4 ends with FISTS in the floor + concrete chunks. earthquake ends with FEET stomping the floor + dust rings. Different impact limbs, different debris.
> - special must show the opponent visibly UPSIDE-DOWN by F7 and tracing a circle around Blackwell by F9–F11.
> - counter F1–F2 must show the arms STILL CROSSED (the crossed-arm catch IS the move). Every other attack starts with F1 uncrossing.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; visible weapons in any holster (empty holsters only — the threat IS that he doesn't need them); a scowl or any visible emotion (Blackwell is blank); loose/unfitted clothing; tattoos; decorative jewelry beyond the single gold pinky ring; any frame missing the crossed-arm pose in idle/hurt; the counter parry burst rendered with 4 points (it must be 8 points with 3 shockwave rings); the same VFX repeated across attacks (each attack has its own destructive signature — spark, crack, chunk, ring, motion-blur, propeller arc).
>
> **Style:** Streets of Rage 4 character pixel quality, big-bruiser archetype at the biggest possible silhouette. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 640×1152 (8 cols × 12 rows), on magenta. Save as `blackwell.png`.**

---

## RUNNER — generation prompt (full detail, 8 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 48x64 frame size, 8 columns by 8 rows uniform grid (total image 384 wide × 512 tall), **magenta `#ff00ff` background**, bottom-center anchor. Basic mook enemy. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **8 rows exactly, 32 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 8 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `run` × 4 frames
>  4. `atk1` × 4 frames
>  5. `atk2` × 4 frames
>  6. `hurt` × 3 frames
>  7. `dead` × 3 frames
>  8. `flee` × 4 frames
>
> Total: **32 character poses in 8 rows**. Count both before submitting.
>
>
> **Character — neighborhood-liaison kid:** Runner. Age 18–24, 5'8"–6'0", lean to wiry. Not an athlete, just willing. Pick ONE skin tone and lock it for every frame: medium-light (`#c89478` mid, `#8a6248` shadow) OR medium (`#8a6248`) OR dark (`#5a3a28`). Pick ONE: short black buzz cut, dark-brown fade, OR hood-up (no hair shown). Pick ONE: clean-shaven OR light stubble. **Lock every choice across all 32 cells — only the pose changes.**
>
> **Costume head-to-feet:** Dark grey hoodie / windbreaker (`#36363f` mid, `#23232a` shadow), zipped halfway (same zip state in every frame). Off-white or dark-grey t-shirt under (`#cfc8b8`), visible at the hem. Navy loose cargo pants (`#2f3a4a` mid, `#1f2838` shadow). Black or grey worn sneakers (`#18181c`). Optional 1-px gold streak at the hip (chain wallet).
>
> **REQUIRED in every frame (including hurt and dead):**
> 1. **RED BANDANA on the RIGHT BICEP** — 4–5 px wide stripe of marigold-red (`#a83040` mid, `#c84a58` highlight, `#6a1828` shadow) knotted around the upper arm, small 1-px knot tail. **Kane's neighborhood-liaison uniform tag — must be visible in every cell.** Streaks horizontally through the swing on atk1.
>
> **Tone:** Cocky on approach, panicked when hit. Knees bent forward, hands raised but loose. Don't show fear in idle — show it ONLY in hurt and flee.
>
> **Frame layout — 8 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — cocky tilt. Hands at hip level, palms loose (not fists). Weight on the back foot, **front foot tapping** (itchy energy — 1-px vertical bob on F2). Red bandana visible on the right bicep.
> 2. `walk` × 6 — **loose swagger that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 LEFT leg fwd + RIGHT arm fwd swing at side. F2 passing. F3 RIGHT leg fwd + LEFT arm fwd swing at side. F4 passing. F5 mirror of F1. F6 passing → blends into F1. Shoulders roll with each step. **Hands stay LOW at the sides, swinging in a relaxed arc — NEVER extended forward** (that would read as the wild-swipe wind-up). No planted/stomp foot on F6. Hood (if up) stays consistent.
> 3. `run` × 4 — 4-frame loop, body upright (NOT athletic crouch). F1 LEFT foot strike + RIGHT arm fwd swing at side. F2 airborne, arms pumping at sides. F3 RIGHT foot strike + LEFT arm fwd swing at side. F4 airborne → blends into F1. **Arms PUMP at the sides** (elbows bent, hands at hip-to-chest height) — NEVER extend forward. Red bandana visible on the back-swing of the rear arm. 1-px white motion-line (`#cfc8b8`) behind the trailing heel on F2 and F4.
> 4. `atk1` WILD SWIPE × 4 — over-committed overhand haymaker. F1 **shoulder DIP back and DOWN (the unmistakable wind-up — body weight loading)**. F2 **body LUNGES forward, front leg CROSSING PAST CENTER (foot lands past the body's centerline), rear arm starting to flail back**. F3 **PEAK — fist 18 px past the body in an overhand arc at chest height, rear arm FLAILING BEHIND for balance, body OVER-COMMITTED FORWARD (visibly falling into the punch), RED BICEP BANDANA streaks HORIZONTALLY 12-px behind the swinging arm (`#a83040` smear)**. F4 stumble-back recovery, body over-balanced, hands wide, looks like he's about to fall. **Only arm attack + the only attack where the body falls forward into the hit.**
> 5. `atk2` SLOPPY KICK × 4 — untrained front kick. F1 kicking leg starts lifting, body already leaning back 15°. F2 leg rising, body leaning back further (25°), arms starting to flail. F3 **PEAK — kicking leg extended STRAIGHT FORWARD at HIP height with FOOT FLAT (toes pointed forward, NOT pulled back — he doesn't know how to flex), body LEANED BACK 30° (no balance, opposite axis from atk1), BOTH arms FLAILING WIDE for balance, supporting knee visibly BUCKLING inward 1 px (untrained tell)**. F4 stumble — kicking leg drops, body over-balanced backward, arms still wide, looks like he's about to fall on his back. **Only leg attack + only attack with the body rocked BACKWARD + foot must be FLAT (not flexed) to show the lack of training.**
> 6. `hurt` × 3 — F1 body folds at the waist. F2 **face shows FEAR — eyebrows up, mouth open, hands fly up defensively**. 1-px white impact spark (`#ffffff`). F3 staggered recovery, still afraid.
> 7. `dead` × 3 — F1 body collapses. F2 falls back. F3 **flat onto the back, arms splayed, bandana still visible against the floor**.
> 8. `flee` × 4 — same body posture as run but LOWER (body crouched 5°), head tucked. **F2 and F4 = head TURNED to look back over the shoulder (the panic-glance)** — eyes wide with fear. Arms pumping at the sides as before.
>
> **Cross-checks before approving the sheet:**
> - atk1 = body falls FORWARD, front leg CROSSES center, rear arm flails BEHIND. atk2 = body rocks BACKWARD 30°, leg straight forward, BOTH arms flail wide. Opposite body angles.
> - atk2's foot must be FLAT (untrained). A flexed foot reads as a trained kick — Runner doesn't know how.
> - F4 of both attacks must show stumble / over-balance, NOT a clean recovery to stance. The over-commitment IS the character.
> - Red bandana visible in EVERY attack frame — never hidden behind the body.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; **different versions of the runner across frames** (lock the skin tone, hair, headwear, beard choice for the whole sheet — variety is handled by engine tint, not by varying the sheet); tactical / military gear (these are kids, not soldiers); visible weapons (Runners brawl bare-handed — Slice is the knife guy, Lamplight is the gun guy); the yellow bandana from Rio (different character, different color, different wrist — Runner's is RED and on the RIGHT BICEP); glowing energy / elemental effects; a balanced clean kick or punch (the over-commitment IS the move).
>
> **Style:** Streets of Rage 4 character pixel quality, untrained-mook archetype. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 384×512 (8 cols × 8 rows), on magenta. Save as `runner.png`.**

---

## CHAINS — generation prompt (full detail, 7 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x80 frame size, 8 columns by 7 rows uniform grid (total image 512 wide × 560 tall), **magenta `#ff00ff` background**, bottom-center anchor. Mid-tier enemy. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **7 rows exactly, 39 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 7 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 6 frames
>  4. `atk2` × 5 frames
>  5. `atk3` × 12 frames
>  6. `hurt` × 3 frames
>  7. `dead` × 3 frames
>
> Total: **39 character poses in 7 rows**. Count both before submitting.
>
>
> **Character — crowd-control biker:** Chains. Age 30–45, 6'0"–6'3", broad-shouldered and blocky, heavyset but not soft. Pick ONE per sheet and lock it: long hair tied back into a low ponytail OR shaved entirely. Pick ONE: full beard OR clean-shaven with a goatee. Hard face, optional cigar between teeth (decoration, not lit). Pick ONE skin tone and lock it: light (`#c89478` mid, `#8a6248` shadow), medium (`#8a6248`), or dark (`#5a3a28`).
>
> **Costume head-to-feet:** **Sleeveless leather vest** — black (`#16100a`), open in front showing a stained tank top. Off-white or grey tight tank top (`#9b9482`). Heavy work jeans, dark indigo (`#2a2e3a` mid, `#191c26` shadow), worn knees visible. Wide brown leather belt (`#4a3020`) with a square brass buckle (`#cfa040`). Steel-toed work boots — black (`#0a0a10`) with grey steel toe caps (`#5a5a5a`).
>
> **REQUIRED in every frame (including hurt and dead):**
> 1. **HEAVY INDUSTRIAL CHAIN WRAPPED TWICE AROUND THE DOMINANT FOREARM** — steel-grey links (`#7a7a82` mid, `#cfd0d6` highlight, `#3a3a40` shadow). Two visible wraps around the forearm, plus a free end ~30 px long held in the fist. The chain has WEIGHT — it lags behind body movement by 1 frame in motion rows. During the swing attack the chain extends to its full ~50 px length in a horizontal taut line. **Every frame including hurt and dead must show the forearm wrap.**
>
> **Tone:** Holds ground. Doesn't chase. Plants both feet wide and dares the protagonist to walk into the chain's reach. Grunts on swings; doesn't talk.
>
> **Frame layout — 7 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — **wide planted stance, feet shoulder-width plus**. Slow shoulder rise on F2 (breath, +1 px). **Chain hangs from the wrist-wrap, slack pooled at the boots, swings 1–2 px laterally** with each breath. Free hand on his hip. Steel-toe boot caps catch a 1-px highlight on F2.
> 2. `walk` × 6 — **heavy gait that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 LEFT leg fwd + RIGHT arm fwd swing at side. F2 passing. F3 RIGHT leg fwd + LEFT arm fwd swing at side. F4 passing. F5 mirror of F1. F6 passing → blends into F1. **Both arms swing in a relaxed arc AT THE SIDES** — the chain-wrapped arm swings too, and **the chain trails 1 frame behind that arm's motion** (lag mass). Arms NEVER extend forward past the body (would read as bullwhip swing wind-up). Boots strike flat-footed. No planted/stomp pose on F6.
> 3. `atk1` BULLWHIP SWING × 6 — chain as a straight taut line. F1 chain-wrapped arm cocks back, **chain pools at the rear (slack piling)**. F2 shoulder rotates back further, **chain pulled tight behind the body**. F3 **PEAK — body torqued 45° at the hip, near (chain-wrapped) shoulder thrown forward, far shoulder pulled back, free hand on hip; CHAIN FULLY EXTENDED in a HORIZONTAL TAUT LINE 36 px past the body at CHEST height (the chain reads as a straight one-sided line — NOT a circle)**. F4 chain past the imagined target, 3-px motion blur (`#cfd0d6`) on the tip. F5 arm follow-through, chain starting to slack. F6 recovery, chain re-pools at the boots. **Only attack with the chain extended on ONE side as a straight line.**
> 4. `atk2` BOOT-SWEEP × 5 — only attack that touches the floor with a hand. F1 body drops, knee lowering toward ground. F2 **body crouched, SUPPORTING HAND BRACED ON THE FLOOR (the only frame in the sheet where Chains touches the ground with his hand — the free hand is the floor-hand)**, free leg starting to sweep. F3 **PEAK — body LOW (knees deep), supporting HAND ON FLOOR, free LEG horizontal at ANKLE height in a 120° sweeping arc, CHAIN trailing behind the sweeping leg as a SECONDARY LOW ARC at ankle level (not chest)**. F4 leg past midline, body following the rotation, chain still trailing low. F5 recovery, body rises back to stance. **Chain at ANKLE height (low), not chest — different role from atk1.**
> 5. `atk3` CENTRIFUGE SPIN × 12 — full chain halo + ballet-spot. F1 body coils, chain starts swinging up off the ground. F2 chain rising to chest height. F3 chain at 12 o'clock above the body. F4 body starts spinning, **chain at 3 o'clock (right of body) at chest height**. F5 body 90° through rotation, **chain at 6 o'clock (in front of body) — head STAYS FACING FORWARD even as body rotates (ballet-spot)**. F6 body 180°, **chain at 9 o'clock (left of body), head still facing forward**. F7 body 270°, **chain back at 12 o'clock**. F8 body 360°, **chain at 3 o'clock again (second pass)**. F9 chain at 6 o'clock (second pass). F10 chain at 9 o'clock (second pass). F11 chain at 12 o'clock final. F12 stop, chain re-pools at the side. **Visual identity: across F4–F11 the chain visibly traces a full CIRCLE around the body (12 / 3 / 6 / 9 o'clock cardinal points across the spin), head LOCKED FORWARD ballet-spot-style. Only attack with the chain as a full circle + only multi-hit AOE.**
> 6. `hurt` × 3 — F1 stagger, body twists. F2 **chain drops slack 4 px below idle position**, free hand goes to the wound. 1-px white impact spark (`#ffffff`) at the contact point. F3 recovery, chain returning to held position. **Forearm wrap still visible.**
> 7. `dead` × 3 — F1 falls forward to one knee, chain swinging forward of body. F2 collapses onto the side. F3 **settled — CHAIN POOLS BENEATH THE BODY IN A COILED S-SHAPE**, free end visible beside the open hand. Forearm wrap still visible.
>
> **Cross-checks before approving the sheet:**
> - atk1 = chain STRAIGHT TAUT line on ONE side at CHEST height, body torqued 45° once. atk3 = chain HALO all the way around the body, body spinning 360°. If atk3 frames look like atk1 with extra speedlines, redraw — atk3's chain must visibly continue past the body to the opposite side, forming a circle across the active frames.
> - atk2 is the ONLY attack where Chains drops LOW with his supporting hand on the FLOOR. If F3 doesn't show the hand braced on the ground with the body crouched, the sweep isn't reading.
> - atk1's chain is at CHEST height. atk2's chain is at ANKLE height trailing the sweeping leg. Different heights, different roles.
> - atk3's head must face FORWARD across every spin frame even as the body rotates underneath (ballet-spot mechanic). If the head rotates with the body, the spin reads as just dizzy — redraw with the head locked forward.
> - The chain wrap is on the forearm in EVERY frame including hurt and dead. If any frame shows a bare forearm, redraw — the wrap is identity.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; **variation of Chains across frames** (same person, same arm-wrap, same beard choice in every cell); multiple chains / nunchaku style (single chain only); spike studs on the chain (keep it industrial, not cartoony fantasy); tactical / military gear (Chains are blue-collar, not soldiers); a face mask (Chains is recognizable, he doesn't hide); bright colors anywhere except the brass belt buckle.
>
> **Style:** Streets of Rage 4 character pixel quality, biker-enforcer archetype. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 512×560 (8 cols × 7 rows), on magenta. Save as `chains.png`.**

---

## SLICE — generation prompt (full detail, 9 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x80 frame size, 8 columns by 9 rows uniform grid (total image 512 wide × 720 tall), **magenta `#ff00ff` background**, bottom-center anchor. Mid-tier enemy. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **9 rows exactly, 40 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 9 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `run` × 4 frames
>  4. `atk1` × 6 frames
>  5. `atk2` × 5 frames
>  6. `jump_atk` × 5 frames
>  7. `dash` × 4 frames
>  8. `hurt` × 3 frames
>  9. `dead` × 3 frames
>
> Total: **40 character poses in 9 rows**. Count both before submitting.
>
>
> **Character — knife-club hit-and-run fighter:** Slice. Age 22–32, 5'6"–5'10", lean and fast, whip-thin. Pick ONE per sheet and lock it: side-shaved with long top slicked back, OR tied-back ponytail, OR mullet. Cocky half-smile in idle. Some have small scars across cheek or eyebrow (optional but lock once). Pick ONE skin tone and lock it: light (`#d4a888` mid, `#9a785a` shadow), medium, or dark.
>
> **Costume head-to-feet:** Sleeveless mesh shirt — black (`#0a0a10`), tight, exposing the arms. Some have a fishnet undershirt visible at the collar. Optional studded vest over the mesh — dark grey leather (`#36363f`) with metallic stud rivets (`#a8a8b0`). Skinny black pants (`#1a1a22`), tight, ankle-length. Black laced-loose combat boots (`#0a0a10`), scuffed. Fingerless black leather gloves (`#16100a`).
>
> **REQUIRED in every frame (including hurt and dead):**
> 1. **BOWIE KNIFE held in the dominant hand** — steel-grey blade (`#cfd0d6`) with mirror-bright edge highlight (`#ffffff`), black handle (`#0a0a10`) with a small wrist-strap. Blade ~14 px when extended. **Default grip = REVERSE / ICEPICK (blade along the forearm, concealed line)**. Grip FLIPS to FORWARD (blade leading from a clenched fist) ONLY on the lunge wind-up (atk1 F1). Returns to reverse grip on the flying stab and all other rows. Knife is visible in every cell — it's what makes Slice *Slice*.
>
> **Tone:** Always shifting weight, never stands flat. Bobs and weaves on the balls of the feet. Cocky half-smile in idle/walk/run/dash; the smile FINALLY drops on hurt F2.
>
> **Frame layout — 9 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — **bouncing weight shift** (never still — 1-px vertical bob across F1–F4). Knife reverse-grip against the right forearm (blade along the inside of the forearm). Body angled 30° toward the camera (boxer's blade-stance). Cocky half-smile visible.
> 2. `walk` × 6 — **light prowling cycle that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 LEFT leg fwd + RIGHT arm fwd swing at side. F2 passing. F3 RIGHT leg fwd + LEFT arm fwd swing at side. F4 passing. F5 mirror of F1. F6 passing → blends into F1. **Both arms swing in a relaxed arc AT THE SIDES** — knife arm swings too, blade still reverse-grip along the forearm. Arms NEVER extend forward past the body (would read as the lunge wind-up). No planted/stomp pose on F6. Feet barely lift.
> 3. `run` × 4 — 4-frame loop that blends seamlessly (F4 → F1). F1 LEFT foot strike + RIGHT arm fwd swing at side. F2 airborne, arms pumping at sides. F3 RIGHT foot strike + LEFT arm fwd swing at side. F4 airborne → blends into F1. **Arms PUMP at the sides** (elbows bent, hands at hip-to-chest height) — knife arm pumps too, blade still reverse-grip along the forearm. Arms NEVER extend forward past the body. **2-px white motion-lines (`#cfc8b8`) behind both heels on F1 and F3.**
> 4. `atk1` FENCER'S LUNGE × 6 — arrow silhouette + grip flip. F1 **coil — knees deep bent, knife at hip, BLADE VISIBLY FLIPS from reverse to FORWARD grip (clenched fist with blade leading)** — the grip-flip IS the move's tell. F2 launch — front leg explodes forward, rear leg extending back. F3 **PEAK — body fully HORIZONTAL parallel to the ground (front leg fully extended forward, rear leg straight back, torso flat), knife in forward grip leading 24 px past the front foot like a spear, 4-px white motion-line streak (`#ffffff`) behind the knife — the ARROW POSE pointing at the target**. F4 active stab held one frame, body still horizontal. F5 miss-pose, body still extended, blade swung past. F6 recoil pull-back to stance, **knife flips BACK to reverse grip**. **Only attack with the body fully horizontal parallel to the ground + only attack with the knife in forward grip.**
> 5. `atk2` LOW SWEEP KICK × 5 — only attack that touches the floor with a hand. F1 body drops low, supporting hand reaches for the floor. F2 **body crouched, SUPPORTING HAND BRACED ON THE FLOOR (knife in that hand, blade STILL reverse-grip along the floor-hand's forearm)**, free leg starts sweeping. F3 **PEAK — body LOW, supporting hand on FLOOR, free leg horizontal at ANKLE height sweeping in a 90° arc**. F4 follow-through, leg past midline. F5 recovery, body rises back to stance. **Only attack where Slice's supporting hand is on the floor — knife stays in the floor-hand in reverse grip.**
> 6. `jump_atk` FLYING STAB × 5 — airborne icepick dart. F1 coil-and-leap (knees bend then explode upward). F2 airborne, body rotating to diagonal, **knife arm rising overhead, BLADE in REVERSE / ICEPICK GRIP pointing DOWN from the fist**. F3 **PEAK AIRBORNE — body diagonal at 45° downward angle (falling dart), knife in ICEPICK GRIP held OVERHEAD POINTING DOWN, free arm trailing behind, body falling toward the imagined target**. F4 descent, blade leading downward. F5 land + recover (knees absorb). **Only aerial attack + knife held OVERHEAD in icepick grip pointing DOWN — opposite of atk1's forward grip leading horizontally.**
> 7. `dash` × 4 — backward dash after lunge. Body low (knees deep), **knife held across the chest as a guard (blade still reverse-grip)**. F1 push off (front foot extending back). F2 mid-slide back, motion lines trail FORWARD from the heels (because he's reversing direction). F3 still sliding back. F4 plant, settle into stance.
> 8. `hurt` × 3 — F1 body folds at the waist, knife arm drops to hip but DOESN'T release the knife. F2 **cocky half-smile FINALLY DROPS, mouth open, fear visible**. 1-px white impact spark (`#ffffff`). F3 staggered recovery.
> 9. `dead` × 3 — F1 body crumples sideways. F2 falls. F3 **settled on side — KNIFE SLIDES 6 px from the OPEN HAND** (the only frame in the whole sheet where he releases the blade — handle visible separate from the glove).
>
> **Cross-checks before approving the sheet:**
> - atk1 is GROUNDED with the knife in FORWARD grip leading horizontally; jump_atk is AIRBORNE with the knife in REVERSE/icepick grip pointing DOWN from overhead. Grip flip + grounding + direction are all opposite.
> - atk2 is the ONLY attack where the supporting hand is on the floor. If F3 doesn't show the hand braced on the ground with the body low, redraw.
> - atk1 F3 the body must be FULLY HORIZONTAL parallel to the ground. If the torso is still upright with just the arm out, that's a jab, not a lunge — redraw.
> - The visible grip FLIP during atk1 F1 is part of the character's tell. Reverse in every row except atk1's forward-grip frames.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; multiple knives / dual wield (single bowie only); bulky armor (Slice is FAST); a gun on the hip (Slices don't carry guns); the red bandana from Runner's bicep (different character); bright colors anywhere; a balanced upright lunge (the body MUST go fully horizontal at F3); the knife in forward grip on any row other than atk1's F1–F5.
>
> **Style:** Streets of Rage 4 character pixel quality, knife-fencer archetype. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 512×720 (8 cols × 9 rows), on magenta. Save as `slice.png`.**

---

## TANK — generation prompt (full detail, 8 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 80x96 frame size, 8 columns by 8 rows uniform grid (total image 640 wide × 768 tall), **magenta `#ff00ff` background**, bottom-center anchor. Mid-tier heavy enemy. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **7 rows exactly, 36 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 7 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 6 frames
>  4. `atk2` × 7 frames
>  5. `atk3` × 7 frames
>  6. `hurt` × 3 frames
>  7. `dead` × 3 frames
>
> Total: **36 character poses in 7 rows**. Count both before submitting.
>
>
> **Character — massive bouncer:** Tank. Age 35–50, 6'2"–6'5", massive — 280–320 lbs of muscle gone soft in the gut. Broader than Atlas, not as tall. Reads big in silhouette. Weathered olive-brown skin (`#a87858` light, `#6a4830` shadow). **SHAVED head or buzzed close, FULL untrimmed beard (`#2a2520`).** Heavy brow, broken nose (multiple times). Resting expression: bored.
>
> **Costume head-to-feet:** **Tactical vest** over a plain black t-shirt — slate grey (`#3a4050` mid, `#1f2530` shadow) with utility straps (`#4a3a28` brown straps). The vest is plates-rated with EMPTY pouches on the front (no weapons — he doesn't need them). Black t-shirt visible under (`#1a1a22`). Heavy duty black cargo pants (`#161618`). Heavy combat boots, black with steel toes (`#0a0a10` body, `#08080a` sole) — heavy soles that thump on impact.
>
> **REQUIRED in every frame (including hurt and dead):**
> 1. **LAMINATED ID BADGE clipped to the FRONT-LEFT of the vest** — white rectangle (`#f4f4f0`) with a small red Kane Properties logo (`#a83040`). 6 × 4 px. The badge is what makes him *legal* — Kane gives him paperwork so the cops won't intervene. Visible at all times including when knocked down.
> 2. **Full untrimmed beard + bald/buzzed head** — every frame.
> 3. **Empty pouches on the tactical vest** — visible every frame (the empty pouches ARE the threat).
>
> **Tone:** Rooted. Plants both feet shoulder-width minimum. Doesn't bounce, doesn't shift weight, doesn't taunt. Just STANDS. Arms loose at his sides, ready to backhand. Super-armor through hits — at full HP he's almost unimpressed by being struck.
>
> **Frame layout — 8 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — **wide planted stance, feet outside shoulder width**. Slow chest rise on F2 (+1 px breath). Arms hang loose, fists half-clenched at hip height. **ID badge catches a 1-px highlight (`#ffffff`) on F2.** Bored expression.
> 2. `walk` × 6 — **heavy stomp gait that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 LEFT leg fwd + RIGHT arm fwd swing at side (hip-level). F2 passing. F3 RIGHT leg fwd + LEFT arm fwd swing at side. F4 passing. F5 mirror of F1. F6 passing → blends into F1. **Both arms swing in a relaxed arc AT THE SIDES, fists half-clenched at hip height.** Arms NEVER extend forward past the body (would read as a bear-hug grab or shoulder-charge wind-up). Boots flat-footed, body barely sways. **1–2 brown dust specks (`#7a5a3a`) at the planted heel on F1, F3, F5.** Vest jiggles 1 px on impact. No planted/stomp pose on F6.
> 3. `atk1` SLEDGEHAMMER SLAM × 7 — pyramid silhouette. F1 both arms start rising, knees bending. F2 arms above head, **fists CLASPING TOGETHER**, body coiled back (2–3 ground-rumble brown specks at his feet). F3 **PEAK PYRAMID POSE — feet WIDE planted, BOTH arms STRAIGHT VERTICAL OVERHEAD, fists meeting at the very top of the silhouette, body arched slightly BACKWARDS** (silhouette is taller than wide, like a triangle pointing up). F4 drive down — body folds at the waist, both clasped fists CRASH at chest-height of target, **5–6 brown dust specks (`#7a5a3a`) in a half-circle at his feet (impact dust)**. F5 follow-through, body bent forward, fists at thigh height. F6 straighten. F7 recovery to stance. **Only attack with the pyramid silhouette + fists clasped vertical overhead.**
> 4. `atk2` SHOULDER CHARGE × 8 — battering-ram. F1 stance widens, body coils backward. F2 body angles forward 15°, lead shoulder starts lowering. F3 **lead SHOULDER LOWERED to chest height, ARMS SWEPT BEHIND (NOT forward — arms are NOT the weapon), body angled 30° forward (battering-ram silhouette), knees deeply bent and driving forward**. F4 launch — first stride forward, 3-px motion lines (`#cfc8b8`) behind shoulders, **brown dust trail (3 specks `#7a5a3a`) behind rear boot**. F5 mid-charge, second stride, more motion lines. F6 approaching impact, body still angled forward. F7 impact, body straightens slightly, dust burst at contact point. F8 recovery to stance. **Only attack with arms swept BEHIND + shoulder leading.**
> 5. `atk3` BEAR HUG GRAB × 6 — only grappling pose. F1 both arms start rising at the sides, body angling forward. F2 arms swing forward at chest height, **fingers SPREAD WIDE, palms facing INWARD**, body bent 15° forward. F3 **PEAK — BOTH ARMS reaching FORWARD at chest height in a WIDE WRAPPING C-shape, PALMS facing IN, FINGERS SPREAD WIDE (the only attack with spread open fingers), body bent forward 20°**. F4 **arms WRAP INWARD — imagined target now squeezed between them, body squeezes inward, head tilts BACK** (the crushing beat). F5 held crush pose. F6 release, arms come down, body straightens. **Only grappling pose + only attack with spread open fingers. Hands MUST NOT be clasped overhead (that's atk1) or swept behind (that's atk2).**
> 6. `atk4` BELLY FLOP × 6 — only prone attack. F1 small forward hop, knees bent. F2 **AIRBORNE, body angled 60° forward, arms thrown WIDE like a dive-splash, GUT LEADING the descent**. F3 peak airborne, body almost horizontal. F4 **LANDING FLAT — body fully HORIZONTAL on the ground (parallel to the floor), arms spread wide, dust burst of 8 brown specks (`#7a5a3a`) spraying outward from underneath the entire body length**. F5 held flop pose (the ground shakes). F6 pushes himself back up, body lifting onto hands and knees. **Only attack where Tank ends FLAT on the ground horizontal.**
> 7. `hurt` × 3 — almost no flinch. F1 head turns 5°, **vest doesn't move (he's barely impressed)**. 1-px white impact spark (`#ffffff`) on the vest. F2 holds. F3 returns to idle stance.
> 8. `dead` × 4 — falls like a tree. F1 folds at the knees. F2 falls to one knee (4-speck brown dust puff `#7a5a3a`). F3 collapses sideways. F4 face down, body settled. Badge still visible on the vest.
>
> **Signature beats — each appears EXACTLY ONCE in the whole sheet:**
> - PYRAMID silhouette (both fists clasped vertical overhead) → atk1 only
> - Body angled 30° forward with lead shoulder lowered + arms swept BEHIND → atk2 only
> - Both arms reaching forward in a C-shape with palms IN + fingers SPREAD wide → atk3 only
> - Body fully horizontal flat on the ground with 8-speck dust burst from underneath → atk4 only
>
> **Cross-checks before approving the sheet:**
> - atk1 = both fists CLASPED TOGETHER OVERHEAD (vertical pyramid, fists at the top of the silhouette). atk3 = both arms reach FORWARD at chest height with fingers SPREAD WIDE (palms in, hands NOT clasped, NOT overhead). If atk3 shows fists clasped overhead, redraw with hands open, spread, forward at chest height.
> - atk2 = arms swept BEHIND, lead SHOULDER lowered as the weapon. atk3 = arms reach FORWARD wrapping (arms ARE the weapon). If atk2 shows arms forward, redraw with arms back and shoulder leading.
> - atk1 ends standing upright with arms overhead at impact. atk4 ends FLAT ON THE GROUND with the body horizontal. Opposite orientations.
> - atk2 must visibly differ from walk — the lead shoulder must clearly DROP to chest height. If charge looks like Tank just walking faster, redraw.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; **variation of Tank across frames** (same bald head, same beard, same vest, same badge in every cell); athletic / spring-loaded movement (he's heavy and slow); firearms or knives (Tanks brawl with their hands — pouches are empty); a trimmed beard or styled hair; the KANE PROPERTIES badge replaced by anything else; the bear-hug shown with clasped fists overhead (that's atk1's silhouette).
>
> **Style:** Streets of Rage 4 character pixel quality, heavy-bouncer archetype at a wide silhouette. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background.
>
> **Output: single PNG, 640×768 (8 cols × 8 rows), on magenta. Save as `tank.png`.**

---

## DOJO — generation prompt (full detail, 10 rows)

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x80 frame size, 8 columns by 10 rows uniform grid (total image 512 wide × 800 tall), **magenta `#ff00ff` background**, bottom-center anchor. Mid-tier disciplined enemy. **NO text, NO labels, NO row headers, NO frame numbers anywhere in the image — pixels only.**
>

> **READ THESE FIRST — failure on any of these requires regeneration:**
>
> 1. **8 rows exactly, 40 total frames.** Top-to-bottom, in the order listed below. Do not skip rows. Do not merge rows. Do not draw a 17th row because you have space.
> 2. **Pure magenta `#ff00ff` (RGB 255, 0, 255) background.** Not dark purple. Not pink. Not a gradient. Pure magenta in every cell, every gutter, every empty pixel.
> 3. **Zero text characters in the image.** No row labels, no animation names, no frame numbers, no captions.
> 4. **Full-body characters, every frame.** Head to feet visible — never cropped at the waist.
> 5. **At least 12 px of pure magenta between rows, 8 px between characters in a row.** The slicer needs these gutters.
>
> **ROW-BY-ROW CHECKLIST — draw exactly these 8 rows in this exact order:**
>
>  1. `idle` × 4 frames
>  2. `walk` × 6 frames
>  3. `atk1` × 6 frames
>  4. `atk2` × 6 frames
>  5. `atk3` × 6 frames
>  6. `atk4` × 6 frames
>  7. `hurt` × 3 frames
>  8. `dead` × 3 frames
>
> Total: **40 character poses in 8 rows**. Count both before submitting.
>
>
> **Character — formal martial artist:** Dojo. Age 24–35, 5'8"–5'11", athletic-toned, visible deltoids and forearms but not bulky. Posture is *perfect* — trained for years. Often Asian / South-Asian / mixed presentation. Pick ONE per sheet and lock it: short black slicked back, OR short black topknot (shaved sides). Pick ONE skin tone and lock it (`#c89478` mid, `#8a6248` shadow). **Clean-shaven** (no facial hair anywhere — that's part of the discipline). Calm face, no smile, no scowl.
>
> **Costume head-to-feet:** **Black gi top** — heavy cotton (`#0a0a10` mid, `#050507` shadow, `#1c1c22` highlight), open V-collar, sleeves rolled up to the elbow. **Sleeves are key — they flap with motion.** Loose black gi pants (`#1a1a22` mid, `#0e0e15` shadow), rolled at the cuff above the ankle. **BARE FEET — visible toes, no shoes (Dojos fight barefoot)**, 1-px toenail detail (`#c8a890`). White hand wraps from knuckles to mid-forearm (`#dcd6c4`).
>
> **REQUIRED in every frame (including hurt and dead):**
> 1. **WHITE BELT KNOT at the LEFT HIP with TWO SHORT TAILS hanging ~14 px down** — white (`#dcd6c4` body, `#a8a294` shadow) on the black gi. The highest-contrast element of the silhouette. **The tails swing with motion (1 frame lag on direction changes) and snap with every kick.**
> 2. **Bare feet** — visible toes, no footwear anywhere.
> 3. **Clean-shaven face** — no beard, no goatee.
>
> **Tone:** Centered. Stands in a formal stance with the front foot 30° off-center, weight 60/40 on the back foot. Hands raised in a knife-hand guard (open palms vertical, fingers up). Eyes locked on the protagonist's center mass. **NEVER throws a punch.** Hands stay in knife-hand guard at chin/hip across every attack frame. Speaks short formal phrases only at fight start ("Begin." or "Show me.").
>
> **Frame layout — 10 rows, one anim per row, 8 cells per row, unused cells stay magenta:**
>
> 1. `idle` × 4 — **karate front-stance** — narrow front-back foot placement, front knee bent, back leg straight. **Bare feet visible (toes clearly drawn).** Hands in **knife-hand guard** — open palms VERTICAL, fingers up, one forward at chin height, one at hip. Belt tails sway 1 px on breath.
> 2. `walk` × 6 — **disciplined gliding stride that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 LEFT foot slides fwd + RIGHT shoulder rotates fwd 2 px (kept tight to the body). F2 passing position. F3 RIGHT foot slides fwd + LEFT shoulder rotates fwd 2 px. F4 passing. F5 mirror of F1. F6 passing → blends into F1. **Hands stay in knife-hand guard at chin/hip the entire cycle** — they do NOT swing out wide, but shoulders rotate at the sides with each step so the body still reads as walking. Arms NEVER extend forward past chin height (would read as a strike — and Dojo doesn't strike with hands). Bare feet stay flat, never crossing the centerline. **Belt tails drift 1 px laterally per step.** No planted/stomp pose on F6.
> 3. `atk1` FRONT KICK / mae geri × 4 — straight-line thrust. F1 rear knee lifts to chest, foot pulled toward the hip (chamber). F2 **leg drives FORWARD horizontally, FOOT FLEXED with TOES PULLED BACK, HEEL leading**. F3 **PEAK — REAR LEG fully extended STRAIGHT FORWARD at CHEST-of-target height, BALL OF FOOT at impact, foot flexed with heel leading, supporting leg slightly bent, body upright, hands STAY in knife-hand guard at chin/hip, BELT TAILS SNAPPED FORWARD 6 px**. F4 re-chamber knee, return to stance. **Foot MUST be FLEXED (toes back) — heel leads.**
> 4. `atk2` ROUNDHOUSE / mawashi geri × 5 — arc with hip drive. F1 body torques back, kicking leg starts lifting sideways with the knee bent. F2 leg chambers to the side, knee at shoulder height. F3 **PEAK — kicking leg HORIZONTAL at CHEST height with SHIN PARALLEL to the ground, TOP-OF-FOOT (instep) leading (foot POINTED, NOT flexed — opposite of atk1), body ROTATED 45° showing the hip drive, both arms swung to the rear shoulder for counter-balance, BELT TAILS SNAP HORIZONTALLY with the rotation**. F4 leg follow-through past the target. F5 recovery, leg returns to stance. **Foot is POINTED (top-of-foot leading); body is TORQUED 45° (hip rotation visible).**
> 5. `atk3` AXE KICK / kakato otoshi × 6 — vertical guillotine. F1 kicking leg lifts toward chest. F2 leg continues rising straight up, body leans back slightly. F3 **PEAK — KICKING LEG STRAIGHT UP VERTICAL PAST THE HEAD (180° leg extension splitting the silhouette down the middle into two halves), supporting leg planted, body arched back slightly, hands STILL in knife-hand guard, BELT TAILS SNAP UPWARD**. F4 **leg DRIVES DOWN with HEEL leading (vertical chop)**, belt tails snapping down. F5 heel at chest-of-target height. F6 recovery, leg plants back into stance. **Only attack with the kicking leg ABOVE the head.**
> 6. `jump_atk` FLYING SIDE KICK / tobi yoko geri × 5 — airborne arrow. F1 explosive leap-off (both knees coiled, body lowering for spring). F2 airborne, body rising and tilting to horizontal. F3 **PEAK — body fully HORIZONTAL parallel to the ground MID-AIR, LEAD LEG extended STRAIGHT forward with the SIDE of the foot leading (NOT heel like atk1, NOT instep like atk2), REAR LEG tucked under the body, BOTH ARMS swept back — arrow silhouette in flight, belt tails trailing horizontally behind**. F4 held one frame in flight. F5 landing recovery (knees absorb). **Only airborne attack + body fully horizontal in flight + side-of-foot leading.**
> 7. `guard` × 3 — both hands in tight knife-hand guard, body angled 30° away from camera (blade-stance). **BELT TAILS ABSOLUTELY STILL** — the stillness is intentional (Dojo is COILED, not relaxed). F1 enters guard. F2 holds. F3 holds.
> 8. `bow` × 6 — formal pre-fight bow. F1 head + torso start tilting forward, hands lowering to the thighs. F2 **head + torso tilted forward 15°, hands flat at thighs, body in formal bow posture**. F3 held bow (1 frame). F4 head + torso starting to rise. F5 returning to stance. F6 back in karate front-stance.
> 9. `hurt` × 3 — F1 body folds at the waist. F2 **belt tails swing WIDE and SNAP outward** (the most belt-tail motion in the sheet). 1-px white impact spark (`#ffffff`). F3 recovery — by F3 he's already back in knife-hand guard (Dojos recover fast).
> 10. `dead` × 4 — composed death. F1 body folds. F2 falls to one knee (composed, NOT collapsed). F3 forward to all fours. F4 settled. **Bare feet visible throughout.**
>
> **Signature beats — each appears EXACTLY ONCE in the whole sheet:**
> - Foot FLEXED with heel leading + body upright + leg straight forward → atk1 only
> - Foot POINTED (instep leading) + body torqued 45° + shin parallel to ground → atk2 only
> - Kicking leg STRAIGHT UP vertical past the head + leg splits the silhouette → atk3 only
> - Body fully horizontal in mid-air + side-of-foot leading + rear leg tucked → jump_atk only
> - Belt tails absolutely still → guard only
> - Formal head-bow posture → bow only
>
> **Cross-checks before approving the sheet:**
> - atk1 = STRAIGHT-LINE leg with the foot FLEXED (toes pulled back, heel leading); body squared forward. atk2 = ARCING leg with the foot POINTED (top-of-foot leading); body torqued 45° showing hip rotation. If both look like "leg out at chest height," redraw.
> - atk2 = GROUNDED with the supporting foot planted and the body torqued. jump_atk = fully AIRBORNE with the body horizontal in flight and BOTH legs off the ground (lead extended, rear tucked). If jump_atk shows a planted foot at peak, redraw — it must be airborne.
> - atk3 = the ONLY attack where the kicking leg goes STRAIGHT UP past the head. If atk3 shows the leg at chest height instead, redraw.
> - jump_atk lead leg must be STRAIGHT with the SIDE of the foot leading (NOT a bent knee, NOT a heel like atk1).
> - Hands stay in knife-hand guard at chin/hip across every attack frame. **NEVER throws a punch.** If any attack shows the lead arm extending forward like a strike, redraw.
>
> **DO NOT include:** any text/labels/frame numbers; cell separator lines; **different Dojo designs across rows** (the bowing Dojo, the walking Dojo, and the kicking Dojo are all the SAME person — same hair, same proportions, same skin tone, same gi); modern street clothes (Dojo always wears the gi); visible weapons (empty hands, bare feet, no knife / chain / gun); bright colors (black gi, white belt, that's it — no purple/maroon tint shifts between rows); tattoos; loose untied hair (always tied back); footwear of any kind (bare feet always); any frame missing the white belt knot at the left hip with the two tails; any frame where Dojo throws a punch.
>
> **Style:** Streets of Rage 4 character pixel quality, formal-karateka archetype. Hard 1-px outlines, 3-color palette per body part. Pure magenta `#ff00ff` background — high contrast against the black gi.
>
> **Output: single PNG, 512×800 (8 cols × 10 rows), on magenta. Save as `dojo.png`.**

---

## After generation

1. Drop the resulting PNG into `characters/<name>.png`.
2. Run `python3 auto_atlas.py <name>` to re-slice. The slicer detects magenta-bounded row bands automatically and labels them top-to-bottom in the order from the character's `.md` spec.
3. Reload `the_block.html`. The atlas loader picks it up automatically — that character switches from procedural to sprite rendering. Any anim slot the sheet is missing falls back via `ANIM_FALLBACK` so partial sheets ship cleanly.

If a sprite is missing an identity item in any frame, regenerate that single frame and re-slice. Don't ship without the bandana, the cigarette, the chain, the hardhat, the fedora, the brass knuckles, or the eye-glow — those are the characters' tells.

For the smaller-tier enemies (Runner, Slice, Chains, Tank, Dojo) and the other bosses (Razor, Volt, Blackwell), see `STAGE_SPRITE_PROMPTS.md` for stage-by-stage generation prompts. Their movesets are documented in `characters/<NAME>.md` and the auto-slicer handles them via the same workflow.
