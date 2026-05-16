# Enemy sprite sheet prompts — per stage

For each stage, the list of enemies that appear plus a ready-to-paste AI-generator prompt for each new enemy you haven't generated yet. **Generate them in order — once an enemy is saved to `characters/<type>.png`, every later stage that uses the same enemy reuses the sprite. You only need to generate each type once.**

Stages are listed in play order. Bosses are at the end of their stage's section.

After you generate a sheet, save it as `characters/<type>.png` (lowercase enemy type name). The atlas loader picks it up automatically on next page load — same flow as the playable characters.

## Required identity items per enemy (must appear in EVERY frame)

| Enemy | Identity item |
|---|---|
| RUNNER | red bandana knotted around the right bicep |
| TANK | laminated "KANE PROPERTIES SECURITY" badge on the vest |
| LAMPLIGHT | pistol always visible (held two-handed at chest) |
| SLICE | bowie knife held in reverse grip, blade along the forearm |
| CHAINS | heavy industrial chain wrapped twice around the dominant forearm |
| SHADE | dark purple eye-glow (only visible feature inside the matte black hood) |
| DOJO | white training belt with two short tails at the left hip |
| RIG | yellow hard hat with small KANE PROPERTIES logo on the brim |
| BARON | tan trench coat + brass knuckles + (visible only when coat flares) retired-NPD badge inside coat |
| RAZOR | twin folding knives in reverse grip + small gold "K" lapel pin |
| VOLT | cybernetic left arm + both cyber legs with blue power-line glow |
| BLACKWELL | crossed-arms idle + gold pinky ring + empty chest holsters |

---

## STAGE 1 — THE BLOCK

**Enemies you need to generate**: `runner`, `slice`, `chains` (3 new sheets).

### runner.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 48x64 frame size, 8 columns by 4 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Runner. 18-24 year old neighborhood thug. Lean to wiry build, 5'8"-6'0". Dark grey hoodie (#36363f) zipped halfway, hood up. Off-white t-shirt visible at hem (#cfc8b8). Navy cargo pants (#2f3a4a), loose. Worn black sneakers. Vary skin tone (#c89478 light to darker) across spawns. Hair short and varied — buzz cut, fade, or beanie.
>
> **Required identity item, must be visible in EVERY frame:** a bright red bandana (#a83040 mid, #c84a58 highlight) knotted around the right bicep, 4-5 px wide stripe. This is Kane's neighborhood-liaison uniform marker.
>
> **Tone:** cocky on approach, panicked when hit. Hands raised loose. Brawls bare-handed (no weapons).
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (slight sway, hands at hip), `walk` x4 (loose stride)
> Row 2: `run` x4 (limbs flail, bandana visible on back-swing), `atk1` x4 (wild forward swipe — F1 shoulder-dip wind-up, F2 step, F3 full-extend, F4 retract)
> Row 3: `hurt` x3 (body folds, face shows fear), `dead` x3 (falls onto back), `flee` x2 first half (body lower, head ducked)
> Row 4: `flee` x2 last half, 6 spare cells
>
> Pixel-art style, clean silhouette, hard edges, 5-6 colors per body part, no anti-aliasing on outline. Reference: Streets of Rage 4 mook quality.

### slice.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 48x72 frame size, 8 columns by 4 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Slice. 22-32 year old knife specialist. Lean and fast, 5'6"-5'10", whip-thin. Black sleeveless mesh shirt (#0a0a10) exposing arms. Dark grey studded leather vest (#36363f with #a8a8b0 stud rivets) over the mesh. Skinny black pants (#1a1a22). Combat boots laced loose. Black fingerless gloves (#16100a). Vary hair per spawn — side-shaved with long top slicked back, OR ponytail, OR mullet. Some have small scars.
>
> **Required identity item, must be visible in EVERY frame:** a bowie knife in REVERSE grip in the dominant hand. Steel-grey blade (#cfd0d6) with bright edge highlight, black handle (#0a0a10). Blade lies along the forearm in idle (concealed), flips forward during the lunge. ~14 px long extended.
>
> **Tone:** always shifting weight, bobs on the balls of the feet. Cocky half-smile in idle. Enjoys the work.
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (bouncing weight shift, knife on forearm), `walk` x4 (light fast steps)
> Row 2: `run` x4 (sprint with motion lines, knife arm forward), `atk1` x6 first 4 (lunge — F1 coil, F2 launch full extension, F3-4 stab forward)
> Row 3: `atk1` last 2 (recoil), `dash` x4 (backward dash, body low, knife out), `hurt` x2 first half
> Row 4: `hurt` x1 last, `dead` x3 (knife falls beside body), 4 spare cells
>
> Pixel-art style, clean silhouette, hard edges. Slice is FAST — every frame reads as motion.

### chains.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x80 frame size, 8 columns by 5 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Chains. 30-45 year old brawler. Broad-shouldered, blocky, 6'0"-6'3", heavyset but not soft. Black sleeveless leather vest (#16100a) open in front showing a stained grey tank top (#9b9482). Dark indigo work jeans (#2a2e3a) with worn knees. Steel-toed black work boots with grey toe caps. Wide black leather belt with brass square buckle (#cfa040). Vary per spawn — long ponytail OR fully shaved head, full beard OR clean-shaven with goatee.
>
> **Required identity item, must be visible in EVERY frame:** a heavy industrial chain wrapped twice around the dominant forearm, free end ~30 px held in the fist. Steel-grey links (#7a7a82 mid, #cfd0d6 highlight, #3a3a40 shadow). Chain has weight — lags 1 frame behind body motion. Extends to full ~50 px length on the swing attack.
>
> **Tone:** holds ground, doesn't chase. Lets you come to him. Grunts on swings. Cigar between teeth on some spawns (decoration, not lit).
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (slow shoulder rise, chain swings 1-2 px), `walk` x4 (heavy gait, chain trails)
> Row 2: `atk1` x6 (horizontal swing — F1-2 wind-up arm cocks, chain pools, F3 forward arc full extension, F4-6 follow-through), 2 spare
> Row 3: `atk2` x8 (spin — F1-3 body coils, F4-5 first half of 360° rotation with chain tracing arc)
> Row 4: `atk2` x4 (spin — F6-7 second half rotation, F8 recovery), `hurt` x3 (stagger, chain drops slack), `dead` x1 first
> Row 5: `dead` x2 last (falls, chain pools beneath body), 6 spare cells
>
> Pixel-art style, clean silhouette. The chain is THE silhouette element — visible at the edge of every pose.

---

## STAGE 2 — THE TUNNELS

**Enemies you need to generate**: none new — `slice`, `runner`, `chains` already done in stage 1.

---

## STAGE 3 — RIVER ROW (Boss: BARON)

**Enemies you need to generate**: `tank`, `lamplight`, `baron` (3 new sheets). `runner` already done in stage 1.

### tank.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x80 frame size, 6 columns by 4 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Tank. 35-50 year old heavy enforcer. Massive build, 6'2"-6'5", 280-320 lbs, muscle gone soft in the gut but wide shoulders. Slate grey tactical vest (#3a4050) with utility straps and empty pouches (no weapons — doesn't need them). Plain black t-shirt under (#1a1a22). Black heavy cargo pants. Scuffed black combat boots with steel toes. Shaved head or close buzz, full untrimmed beard most spawns. Heavy brow, broken nose, bored resting expression.
>
> **Required identity item, must be visible in EVERY frame:** a laminated white "KANE PROPERTIES SECURITY" ID badge clipped to the front-left of the vest. White rectangle (#f4f4f0) with small red Kane logo (#a83040). ~6x4 px. Always visible, even on knockdown frames — this is what keeps the cops from arresting him.
>
> **Tone:** slow and inevitable. Doesn't bounce, doesn't shift. Stands wide. Walks at half speed. Doesn't speak — grunts on impact. Super-armored through 2-3 hits before flinching.
>
> **Frame layout (top to bottom, 6 per row):**
> Row 1: `idle` x4 (slow chest rise, stance wide), `walk` x2 first half (heavy stomp gait, boots strike flat)
> Row 2: `walk` x4 last (stomp continues), `atk1` x2 first half (slam — F1-2 arm raised overhead body coiled)
> Row 3: `atk1` x5 (slam — F3 wind-up peak with ground rumble particles, F4 swing peak, F5-7 recovery), 1 spare
> Row 4: `hurt` x3 (barely flinches, head turns 5°), `dead` x3 (falls hard, drop shadow grows)
>
> Pixel-art style, clean silhouette. Read as BIG — Tank is the wall.

### lamplight.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 48x72 frame size, 8 columns by 4 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Lamplight. 28-40 year old hired gun. Lean, 5'10"-6'1", steady hands. Black balaclava covers face from nose down — only eyes visible (flat, bored, slightly tan skin around eyes #d4a888). Dark brown leather jacket (#2a1f15) fitted, two front pockets. Black tactical pants (#1a1a22) slim cut. Combat boots laced full. Hair hidden under beanie. Gender ambiguous.
>
> **Required identity item, must be visible in EVERY frame:** a pistol always visible, held two-handed at chest height by default. Gun body (#3a3a40) with lighter barrel (#4a4a50). Raises to fire. During `atk1` active frame, a bright orange-yellow muzzle flash dot (#ffd76a core, #ff8a40 edge) appears at the barrel tip.
>
> **Tone:** composed, holds 70-110 px range from the target. Backs up if you close in. Never melees. Quiet during combat.
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (gun two-handed at chest, eyes scan), `walk` x4 (backward steps while keeping gun raised)
> Row 2: `atk1` x5 (regular shot — F1-2 raise + aim, F3 trigger pull with muzzle flash, F4-5 recoil + recover), `atk2` x3 first half (charged shot — F1-3 long aim with growing glow at barrel)
> Row 3: `atk2` x5 (charged — F4 longer aim with brighter glow, F5 bigger muzzle flash, F6-8 harder recoil), `hurt` x3 (body twists, gun arm drops 1 frame)
> Row 4: `dead` x4 (falls, gun lands on ground beside body), 4 spare cells
>
> Pixel-art style. Visible identity = the gun + the masked face.

### baron.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 80x96 frame size, 8 columns by 6 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor. Boss-tier — Baron should read BIGGER than a regular Tank.
>
> **Character:** William "Baron" Halsey. 52-year-old ex-cop, Kane's enforcer. 6'2", thick powerlifter frame gone slightly soft. Pale-white ruddy skin (#d4a888). Steel-grey hair (#8a8a8e) parted neatly right, receding. Always combed even mid-fight. Heavy jaw, broken nose (multiple times), tired eyes that never look away. Small polite smile in resting expression — the smile is the menace.
>
> **Costume:** Long tan trench coat (#8a6a3a body, #4a3a18 shadow, #ad8a4f highlight), knee-length, open in front. Coat has WEIGHT — swings 1 frame behind body motion. White dress shirt under (#e8e2d4) slightly stained. Dark charcoal slacks (#2a2a30). Polished black dress shoes scuffed at toe (#08080a). Black leather belt with silver buckle.
>
> **Required identity items, must be visible in EVERY frame:**
> 1. The TRENCH COAT — Baron's silhouette.
> 2. BRASS KNUCKLES on both fists — gold (#cfa040) with shadow (#8a6020) and small highlight pixel during attacks.
> 3. A gold sheriff-style badge clipped INSIDE the coat — only visible when the coat flares open during atk2 (cross) and atk3 (haymaker). Reads "RETIRED — NPD" in tiny pixels.
>
> **Tone:** loose-shouldered, deliberately unintimidating. Stands relaxed. Speaks calmly during fights: "You don't have to do this." Talks like a fighter who's done this 100 times.
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (boxer's bounce on balls of feet, coat sways), `walk` x4 (casual approach, coat trails)
> Row 2: `atk1` x4 (left jab — fast snap-back), `atk2` x4 (right cross — body rotates 45°, coat FLARES open on F3 revealing badge briefly)
> Row 3: `atk3` x8 (haymaker — F1-4 wind-up coat opens badge visible, F5 peak full extension, F6-8 recovery)
> Row 4: `atk3` x1 last + `hurt` x3 (body folds, hair stays neat), `taunt` x4 (combs hair with one hand, smiles politely — plays once per fight)
> Row 5: `dead` x5 (falls hard, coat splays open, knuckles fall from his hands), 3 spare cells
> Row 6: 8 spare cells
>
> Pixel-art style, clean silhouette. Coat is iconic — give it room. Smile NEVER drops into a scowl, even when hurt.

---

## STAGE 4 — LANTERN ROW

**Enemies you need to generate**: `shade` (1 new). `chains` + `slice` already done.

### shade.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 48x72 frame size, 7 columns by 5 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Shade. Indeterminate age — body looks 25-35, eyes look older. 5'9"-5'11", lean-athletic, whip-quick. Gender-ambiguous on purpose. Composed body language — doesn't bounce, weight centered. Closes eyes briefly before vanishing.
>
> **Costume:** Matte black hooded utility cloak (#16161a body, #08080a shadow, #2a2a2f highlight), draped to lower thigh, hood always up. **Cloak hem trails as motion lines during dash and vanish.** Skin-tight black bodysuit (#1a1a1f) under, visible at neck, arms, legs. Featureless dark grey mask (#2a2a2f) covers nose and mouth — no logo, no decoration. Soft-soled tactical shoes (#0a0a10). Black leather gloves, fingertips removed, knuckles taped white.
>
> **Required identity item, must be visible in EVERY frame:** **a faint dark-purple glow at the eyes** — `#6a3080` core, `#3a2050` edge, 1-2 px high. The only color on a near-black silhouette. **During vanish frames**, the eye-glow grows brighter and persists in the air for 2-3 frames after the body fades. Plus: **wisps of black-purple smoke** (#3a2a4a) trailing from the cloak hem during all motion frames.
>
> **Tone:** silent. Never speaks. Patient. Closes eyes before vanishing.
>
> **Frame layout (top to bottom, 7 per row):**
> Row 1: `idle` x4 (subtle, hood breathes, eyes glow steady), `walk` x3 first half (smooth glide, cloak trails, smoke wisps)
> Row 2: `walk` x3 last (continues), `atk1` x4 (strike — front arm chop, fast 16fps)
> Row 3: `atk2` x4 (backstab — same beats as atk1 but cloak still trails reappear smoke for 2 frames), `vanish` x3 first half (F1 inhale, F2-3 body fades to outline)
> Row 4: `vanish` x2 last (only eye-glow + smoke remain), `reappear` x3 (F1 smoke + eye-glow only, F2 body reforms low alpha, F3 full opacity), `hurt` x2 first half
> Row 5: `hurt` x1 last (body folds, hood drops back), `dead` x4 (body crumples, cloak pools, eye-glow fades over death frames), 2 spare cells
>
> Pixel-art style. Shade should look ALMOST INVISIBLE against magenta because the palette is so dark — the eye-glow IS the silhouette. That's intentional.

---

## STAGE 5 — THE CAGE

**Enemies you need to generate**: `dojo`, `rig` (2 new). `chains` already done.

### dojo.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 52x72 frame size, 7 columns by 5 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Dojo. 24-35 year old martial artist. 5'8"-5'11", athletic-toned with visible deltoids and forearms (not bulky). Posture PERFECT — every spawn looks like years of training. Asian / South-Asian / mixed presentation (vary across spawns). Some have a small braided sidelock or goatee. Hair tied back into a tight low ponytail OR shaved sides with topknot — two distinct silhouettes.
>
> **Costume:** Black heavy-cotton gi top (#0a0a10), open V-collar, sleeves rolled to elbow. **Sleeves are key — they flap with motion.** Loose black gi pants (#1a1a22) rolled at the cuff above the ankle. **BARE FEET — visible toes, no shoes.** White hand wraps from knuckles to mid-forearm.
>
> **Required identity item, must be visible in EVERY frame:** **a white training belt** (#dcd6c4) wrapped around the waist with the knot tied OFF-CENTER on the LEFT hip and **two short tails** hanging ~14 px down. White on the black gi = highest-contrast element of the silhouette. Tails should SWING with motion (1 frame lag on direction changes).
>
> **Tone:** centered. Stands in formal stance — front foot 30° off-center, weight 60/40 on back foot, hands raised in guard, eyes locked on the target's center mass. Calm — no smile, no scowl. Bows formally before combat ("Begin.").
>
> **Frame layout (top to bottom, 7 per row):**
> Row 1: `idle` x4 (stance held, belt tails sway 1 px), `walk` x3 first half (light balanced steps, front foot leads)
> Row 2: `walk` x3 last, `atk1` x4 (counter punch — F1 guard tightens, F2 forward step + punch extend, F3 peak knuckles forward, F4 retract to stance)
> Row 3: `guard` x3 (hands tighter, body angled 30°, belt tails STILL), `bow` x4 (formal bow — head + torso tilt forward, then return — plays once)
> Row 4: `hurt` x3 (body folds, belt tails swing wide, fast recover), `dead` x4 (falls to one knee FIRST, then to ground — Dojo dies with composure)
> Row 5: 7 spare cells
>
> Pixel-art style. Black gi + white belt + bare feet = the silhouette.

### rig.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x80 frame size, 8 columns by 5 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Rig. 28-45 year old construction worker. Thick pure-mass build from manual labor, 6'0"-6'4". Broad shoulders, tight gut. Heavy and slow. Doesn't bounce. Hands curled into fists at thigh height. Spits to the side occasionally. Weathered face, scruffy stubble or full beard, some have safety goggles pushed up onto the hard hat.
>
> **Costume:** Hi-vis fluorescent orange safety vest (#ff7a30) over a brown work shirt with two reflective grey stripes (#a8a8a8) horizontal across the front. Brown long-sleeved work shirt rolled to elbow — forearms exposed, hairy. Khaki-brown dirty work pants (#7a5a3a) with oil stains (darker patches). Heavy brown steel-toed work boots (#3a2a1c with #5a5a5a steel toes — chunkier than Atlas's). Heavy leather work belt with empty hammer loops.
>
> **Required identity item, must be visible in EVERY frame:** **YELLOW HARD HAT** (#cfa040 with #e8c860 highlight and #8a6020 shadow), battered and scuffed at the brim. Stays on every frame — even hurt, even dead. Small black KANE PROPERTIES logo (#1a1a22, ~3 px square) on the front-left of the brim. The hat + the hi-vis orange vest = Rig's silhouette.
>
> **Tone:** doesn't enjoy this work, doing the job. Mutters: "Just doin' the job." / "Move it, kid." Bored, not malicious. Walks slow, trusts weight.
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (heavy chest rise, hard hat brim catches 1-px highlight), `walk` x4 (stomp gait, boots strike flat)
> Row 2: `atk1` x5 (strike — F1 wind-up, F2 step forward, F3 peak punch extension, F4-5 recover), `atk2` x3 first half (pound — F1-3 both fists rise overhead, rumble particles)
> Row 3: `atk2` x8 (pound — F4 body coiled at peak, F5-6 peak with hands above head, F7-9 drive downward, F10 impact shockwave burst with screen shake feel, F11-12 recovery)
> Row 4: `atk2` x1 last + `hurt` x3 (stagger, head turns, HARD HAT STAYS ON), `dead` x4 (falls forward, hard hat stays)
> Row 5: 8 spare cells
>
> Pixel-art style. Hard hat NEVER falls off — that's the visual joke. Vest stays orange even on death frames.

---

## STAGE 6 — UPTOWN (Boss: RAZOR)

**Enemies you need to generate**: `razor` (1 new). `lamplight`, `dojo`, `chains` already done.

### razor.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x96 frame size, 8 columns by 6 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor. Boss-tier.
>
> **Character:** Eliza "Razor" Park. 38-year-old corporate intimidation specialist. 5'7", lean athletic yoga/kickboxing build. Korean, light olive skin (#dcb088). Sharp jawline, dark eyes (#1a1410). Neutral resting expression — small DELIBERATE smile only when landing a hit. **Sleek straight black bob** ending at the jawline, with **two small bleached blonde streaks** (#c8a060) on either side at the front — each ~3 px wide. Streaks must be visible in every frame.
>
> **Costume:** Tailored black suit jacket (#1a1a22), fitted, two-button, single vent, lapels visible. Black silk camisole under, V-neck. Slim black slacks straight to ankle. Black low-heeled oxford shoes polished (#0a0a10). Black leather gloves fitted, fingertips exposed only at the tips.
>
> **Required identity items, must be visible in EVERY frame:**
> 1. **TWO folding knives** — one in each hand during attacks; sheathed at small-of-back belt in idle/walk. Blades: ~10 px steel-grey (#cfd0d6) with mirror-bright edge highlight. Handles: dark grey (#2a2a2f) with **deep burgundy inlay** (#4a1018).
> 2. **The bleached blonde streaks** in the hair.
> 3. **A small gold "K" lapel pin** on the left lapel — Kane Properties logo. Gold (#f4c860), ~2x3 px.
>
> **Tone:** calm, polite, lethal. Hands clasped behind back in idle. Walks calmly no rush. Switches to fencing stance when knives draw — front foot 45°, back foot perpendicular. Speaks during fights: "We could have done this in your kitchen."
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (hands clasped behind back, suit perfectly clean, subtle breath), `walk` x4 (heel-toe walk steady tempo)
> Row 2: `draw` x4 (F1 body shifts to fencing stance, F2-3 knives drawn from belt, F4 ready pose both blades forward — plays once), `atk1` x4 (slash — fast forward single-blade cut)
> Row 3: `atk2` x8 (dash — F1-2 wind-up, F3 launch with motion lines, F4-6 active both blades extended, F7-9 recovery — wait, 9 frames in 8 cells, compress to 8)
> Row 4: `atk3` x5 (throw — F1-2 arm cocked back, F3 release knife projectile spawned, F4-5 retract), `phase2` x3 first half (wipes blood off one knife with sleeve)
> Row 5: `phase2` x1 last (returns to stance — plays once when she drops below 40%% HP), `hurt` x3 (body twists, suit stays clean), `dead` x4 (falls to one knee, then to floor, knives clatter)
> Row 6: 8 spare cells
>
> Pixel-art style. Razor is POISED — even when hurt, hair stays neat. Only the burgundy knife inlays and the gold pin break the black silhouette.

---

## STAGE 7 — THE WORKS

**Enemies you need to generate**: none new — `tank`, `rig` already done.

---

## STAGE 8 — THE FREEWAY

**Enemies you need to generate**: none new — `chains`, `slice`, `lamplight` already done.

---

## STAGE 9 — THE TOWER (Boss: VOLT)

**Enemies you need to generate**: `volt` (1 new). `dojo`, `lamplight`, `rig` already done.

### volt.png

> Pixel art sprite sheet, side-view 2D beat-em-up style, 64x96 frame size, 8 columns by 5 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor. Boss-tier.
>
> **Character:** Daniel "Volt" Vega. 34-year-old cybernetic enforcer, Kane's loyal lieutenant. 6'1" WITH the prosthetics (originally 5'10"). Athletic-toned upper body (organic). Latino, medium brown skin (#a87858). Mid-30s, short scruff, tired eyes. Gauntness from rehab months. Resting expression: focused. **Buzz-cut black hair**, ~2 px short.
>
> **Costume:** Sleeveless dark grey tactical shirt (#2a2a32) fitted across the chest. Right arm BARE and visible (organic). Black cargo shorts (#16161a) end at mid-thigh where cyber legs begin — **the transition (organic skin to mechanical) is VISIBLE and not hidden.** Black tactical belt with small power-pack module on right hip (#1a1a22 with single blue LED #6aa0e8).
>
> **Required identity items, must be visible in EVERY frame:**
> 1. **CYBERNETIC LEFT ARM** — matte gun-metal grey (#5a5e6a with #2a2e36 shadow and #8a8e9a highlight). Mechanical joints visible at shoulder, elbow, wrist. Hand is articulated plates instead of skin. **Thin blue power-line glow (#4a8ad0) runs along the forearm.**
> 2. **BOTH CYBER LEGS** — same gun-metal palette, replaced from mid-thigh down. Heavy plate construction, exposed pneumatic pistons at knees. **Glowing blue power-lines along outside of each thigh and calf.** Feet are stylized armored plates, not boots.
> 3. **Hip-mounted power pack** with single blue LED.
>
> **Power-lines pulse subtly** (1-px glow variation per frame). Brighter during attacks — at peak of uppercut and shock charge they flash white.
>
> **Tone:** heavy below the waist (cyber legs are powerful but lack organic bounce). Plants every step. Upper body moves naturally. Mismatch is part of the character. Quiet during combat. Speaks once: "Kane built me. So I owe him a building."
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (heavy stance, power-lines pulse, right shoulder rises on breath), `walk` x4 (cyber-leg stomp — should clearly read as METAL on concrete)
> Row 2: `atk1` x6 (cybernetic strike — F1-2 wind-up power-lines on cyber arm BRIGHT, F3 drive forward, F4-6 recovery), `atk2` x2 first half (uppercut — F1-2 deep crouch)
> Row 3: `atk2` x6 (uppercut — F3-4 explosive rise both arms drive up, F5 peak power-lines flash white, F6-8 recovery), `atk3` x2 first half (shock — F1-2 charge cyber arm raised growing blue glow at palm)
> Row 4: `atk3` x6 (shock — F3-4 continued charge, F5 release projectile spawns, F6-8 recovery), `hurt` x2 (body recoils, cyber limbs less affected — don't flinch like organic)
> Row 5: `dead` x6 (falls, cyber limbs spasm briefly with sparks at joints, power-lines fade to dark over the death frames), 2 spare cells
>
> Pixel-art style. Organic torso + cyber limbs is the iconic mix. NO red glow — blue power-lines only.

---

## STAGE 10 — THE TOP (KANE final boss)

**Enemies you need to generate**: `kane` (1 new — though this is a cinematic sheet, not a fighter sheet).

### kane.png

KANE is a QTE cinematic encounter — never throws a punch, stays seated at his desk for the entire scene. The sheet is **scene poses**, not combat frames.

> Pixel art sprite sheet, side-view 2D beat-em-up style, **128x128** frame size (bigger because the DESK is part of the silhouette), 4 columns by 2 rows uniform grid (8 cells, one per pose), magenta `#ff00ff` background, bottom-center anchor.
>
> **Character:** Victor Kane. 58-year-old real-estate developer. CEO of Kane Properties LLC. 5'11", lean fit. Looks 50 not 58. Maintains body like a portfolio. White skin slightly tan from recent vacation. Sharp features, thin lips, eyes that look genuinely interested. **PERPETUAL WARM SMILE** — not a smirk, a real smile. The smile is the menace.
>
> **Costume:** Bespoke charcoal three-piece suit (#3a3a40 with subtle 1-px pinstripe every 6 px in #4f4f57). Single-breasted jacket, perfect tailoring. Crisp starched white dress shirt (#f4f4f0). Dark burgundy silk tie (#4a1018), perfectly knotted. Three-piece vest all six buttons done up. Dark slacks matching suit. Mirror-polished black oxford shoes. **A gold cufflink visible on each sleeve** (#f4c860). A single gold wedding band on the left hand (his wife is dead, he wears it for the image).
>
> **Required identity items, must be visible in EVERY frame:**
> 1. **THE SMILE.** Always smiling. Even when refused, even when the building shakes. The smile NEVER drops.
> 2. **THE DESK** — heavy mahogany (#4a2818 with #1a0e08 shadow and #6a3820 highlight), wide dark wood surface taking up the bottom 1/3 of the frame. Hands rest on the desk in idle.
> 3. **A fountain pen** held casually in the right hand, black with gold cap (#f4c860). Used to gesture, point, offer to sign.
> 4. **A leather-bound checkbook** open on the desk, visible from F1 onward. The check is the REAL weapon. The protagonist refuses it.
>
> **Tone:** polite, patient, GENUINE. Means what he says. Never raises voice. Never stands.
>
> **Pose layout (top to bottom, 4 per row — 1 pose per cell):**
> Row 1: `seated_open` (idle — hands folded on desk, smile, eyes on target), `lean_in` (Prompt 1 — leans forward elbows on desk), `gesture_open` (Prompt 2 — right hand extended palm-up offering the check), `gesture_pen` (Prompt 3 — pen pointed at target gently)
> Row 2: `gesture_hard` (Prompt 4 — pen tip lowered to document, smile same but eyes colder for one beat), `lean_back` (Prompt 5 — leans back in chair, sets pen down, hands folded again, smile NEVER drops), `quiet` (final pose — same as seated_open but fully still), 1 spare
>
> Pixel-art style. Desk extends across the full cell width. Kane is centered behind it, head/shoulders visible above. No standing or fighting poses. **The lack of motion is the menace.**

---

## After generation — wiring it up

When each enemy/boss sheet is saved as `characters/<type>.png`:

1. I'll add a layout config at `layouts/<type>_layout.json` mapping each row to its animation slot
2. Run `python3 pipeline.py build-atlas layouts/<type>_layout.json --output characters/<type>_atlas.json`
3. Wire the engine renderer to prefer the sprite when present (currently the per-enemy `drawTank`, `drawSlice`, etc. functions render procedurally)

Tell me when you've finished a stage's sprites and I'll wire that stage's sprites into the engine. You don't have to do all stages at once — generate stage 1's three sheets, ping me, I integrate them; then stage 3, etc.
