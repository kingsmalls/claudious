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

## After generation

1. Drop the resulting PNG into `characters/<name>.png`.
2. Run `python3 auto_atlas.py <name>` to re-slice. The slicer detects magenta-bounded row bands automatically and labels them top-to-bottom in the order from the character's `.md` spec.
3. Reload `the_block.html`. The atlas loader picks it up automatically — that character switches from procedural to sprite rendering. Any anim slot the sheet is missing falls back via `ANIM_FALLBACK` so partial sheets ship cleanly.

If a sprite is missing an identity item in any frame, regenerate that single frame and re-slice. Don't ship without the bandana, the cigarette, the chain, the hardhat, the fedora, the brass knuckles, or the eye-glow — those are the characters' tells.

For the smaller-tier enemies (Runner, Slice, Chains, Tank, Dojo) and the other bosses (Razor, Volt, Blackwell), see `STAGE_SPRITE_PROMPTS.md` for stage-by-stage generation prompts. Their movesets are documented in `characters/<NAME>.md` and the auto-slicer handles them via the same workflow.
