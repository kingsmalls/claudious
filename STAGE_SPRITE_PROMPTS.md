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

> Pixel art sprite sheet, side-view 2D beat-em-up style, **NOIR GUNMAN aesthetic** — fedora + long trench coat + white scarf over the face. Think 1940s/1970s hardboiled detective with a pistol. 64x88 frame size, 8 columns by 4 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character — noir hired gun, NOT a tactical-game henchman:** Lamplight. 35-50 year old hired gun. Lean but not athletic, 5'10"-6'1", carries weight at the shoulders from years of holding a gun raised. **Almost the whole face hidden** — only a narrow strip of eyes visible (#d4a888 light skin, flat bored expression) between the fedora brim above and the scarf below. Gender ambiguous. Hair completely hidden under the hat.
>
> **Costume — the silhouette IS the threat:**
> - **BLACK FEDORA** (#0a0a10) with a wide-ish brim **pulled low over the eyes** so the brim casts shadow across the upper face. Slightly battered darker leather band around the crown. This is the most recognizable silhouette element.
> - **LONG DARK TRENCH COAT** mid-calf length (#1a1a22 body, #0a0a10 shadow, #2a2a36 highlight). Collar **popped UP**, reaching the bottom of the scarf. Steel buckle belt at the waist. **Flares behind on motion** like a cape but isn't a cape.
> - **LONG WHITE SCARF** (#dcd6c4 with #9a9482 shadow) wrapped twice around the neck and **pulled up over the nose and mouth**. The ends hang loose from the neck — visible 14-18 px tail down the front of the coat. **The white scarf against the black coat is the high-contrast tell.**
> - Black fitted leather gloves (#16100a).
> - Dark tactical pants (#1a1a22) under the coat — only the lower legs (below the coat hem) visible.
> - Heavy black combat boots (#0a0a10) laced full.
>
> **Required identity items, must be visible in EVERY frame:**
> 1. The **fedora silhouette** with shadow cast over the upper face.
> 2. The **white scarf** wrapped twice, ends visible hanging down the coat front.
> 3. The **pistol** always held two-handed at chest level by default (gun body #3a3a40, barrel #4a4a50). Raises to fire.
> 4. During `atk1` active frame: a bright **orange-yellow muzzle flash dot** at the barrel (#fff8c0 core, #ffd76a mid, #ff8a40 edge) — visible past the scarf.
>
> **Tone:** composed, holds 70-110 px range from the target. Backs up if you close in. Never melees. Quiet during combat.
>
> **Frame layout (top to bottom, 8 per row):**
> Row 1: `idle` x4 (gun two-handed at chest, eye-slit visible under fedora brim, scarf tails sway 1 px on breath), `walk` x4 (backward steps while keeping gun raised, coat hem sways behind)
> Row 2: `atk1` x5 (regular shot — F1-2 raise + aim, fedora tilts down 1 px, F3 trigger pull with muzzle flash visible past the scarf, F4-5 recoil + recover), `atk2` x3 first half (charged shot — F1-3 long aim with growing BLUE glow at barrel #4a8ad0, glow also tints the scarf for one frame)
> Row 3: `atk2` x5 (charged — F4 longer aim with brighter glow, F5 bigger muzzle flash, F6-8 harder recoil with body rocking back and coat flaring behind), `hurt` x3 (body twists, gun arm drops 1 frame, fedora and scarf stay in place)
> Row 4: `dead` x4 (falls — F3 fedora rolls off the head revealing buzz cut underneath, but the face is still scarf-covered, gun lands on ground beside body), 4 spare cells
>
> **DO NOT include:** visible face below the eyes (scarf stays up on every frame including hurt), visible hair (fedora covers it), modern tactical gear (vests, plate carriers, knee pads — Lamplight is noir, not military), visible logos or badges, two visible guns, a cigarette (that's Duke), a long flowing cape (the coat flares slightly but isn't a cape).
>
> Pixel-art style. The silhouette must read as 1940s noir gunman from any angle — fedora + popped collar + white scarf are the three things that must always be visible.

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

**Enemies you need to generate**: `kane` (1 new — a real fighter sheet now, not QTE-only).

### kane.png

KANE was reworked in v1.2 — he's now a real combat boss with a **sword-cane and a pocket-watch chain whip**. He stands up from his desk and reveals he's been a fighter all along. The QTE cinematic still plays as the intro; the actual fight begins after the 5 prompts resolve.

**IMPORTANT for the AI generator:** Kane is **explicitly fictional** — a Dickensian-villain caricature in a modern suit — because generic "wealthy older businessman" prompts trigger safety filters on real-person resemblance. Lead with the **caricatured features and period accessories** (round wire-rim glasses, tall-coat silhouette, sword-cane, stand-up wing collar) — the reference points are **Mr. Burns from The Simpsons or Anton Ego from Ratatouille**, NOT any real public figure. See `characters/KANE.md` for full spec.

> Pixel art sprite sheet of a **FICTIONAL Dickensian-villain fencing master** — a tall thin caricature in a long charcoal three-piece suit who fights with a sword-cane and a brass pocket-watch chain whip. NOT a real person, NOT a public figure. Reference points: Mr. Burns from The Simpsons, Anton Ego from Ratatouille. 128x144 frame size, 6 columns by 10 rows uniform grid, magenta `#ff00ff` background, bottom-center anchor.
>
> **Character — caricatured, fictional, Dickensian fencing villain:** "Victor Kane." 60-65 year old man, unnaturally TALL and THIN like an old crane in a suit (~6'2", reads taller because he stands perfectly straight, long fingers, narrow shoulders). **Moves with the precision of a fencing master in his prime** — explosive snap from STILL to fully extended strike, no wasted motion. Pale waxen skin (#d8c8b8 light, #a89488 shadow). Long thin nose, sharp narrow cheekbones, small precise mouth, deep-set eyes. **Round wire-rim gold glasses** (#cfa040 thin frames, perfectly circular ~3px lenses) — biggest "fictional character" visual hook, prominent in every frame. **Pure white hair** (#e8e8e4) slicked back from a high widow's peak, with **a single dark grey streak** (#5a5a62) on the RIGHT side. **Asymmetric half-smile — LEFT corner only** — never drops, even on death (until the final death frame).
>
> **Costume — Dickensian fencing master:** Charcoal three-piece suit (#3a3a40 body, 1-px pinstripe #4f4f57 every 6 px). **Jacket cut LONGER than modern fashion** — mid-thigh tall-coat hem. **Stand-up wing collar** (period detail). **Emerald-green silk cravat** (#1a4a30 with #2a6a40 highlight) in a fat 19th-century knot. Vest with **brass pocket-watch chain** (#cfa040) looped across from a buttonhole into the right vest pocket (8-10 px arc). Dark slacks. Mirror-polished black oxford shoes. **Tiny brass skyscraper lapel pin** (#cfa040, ~2x4 px) on the left lapel. **Thin white cotton gloves** (#dcd6c4) on BOTH hands in `idle`. The RIGHT GLOVE is removed during the `glove_off` reveal pose and stays off for the rest of the sheet (his bare right hand grips the sword).
>
> **Weapons — revealed when he stands up to fight:**
> - **SWORD-CANE**: a long black walking cane (#08080a sheath, #cfa040 brass knob) that conceals a thin silver blade (#cfd0d6 with #ffffff edge). Once drawn, **the silver blade is ~80 px long** (gives him exceptional reach). He holds the empty sheath in the LEFT hand as a parrying tool.
> - **POCKET-WATCH WHIP**: the brass chain (#cfa040) with a gold watch fob (#f4c860) at the end. Used only for the `special` move — pulled from the vest pocket and swung in a wide horizontal arc.
>
> **Required identity items, must be visible in EVERY frame:**
> 1. **ROUND WIRE-RIM GOLD GLASSES** — small, perfectly circular.
> 2. **ASYMMETRIC HALF-SMILE** — LEFT corner only.
> 3. **SINGLE DARK GREY STREAK** in pure-white slicked-back hair.
> 4. **TALL-COAT JACKET SILHOUETTE** (mid-thigh hem).
> 5. **STAND-UP WING COLLAR**.
> 6. **POCKET-WATCH CHAIN** arc across the vest in all idle/walk frames (the chain is pulled out only during `special`).
> 7. **SWORD-CANE** in his hand from `glove_off` onward — sheath in LEFT hand, drawn blade in RIGHT hand.
>
> **Frame layout (top to bottom, 6 per row):**
> Row 1: `idle` x4 (standing tall behind the desk, sword-cane planted point-down, gloved off-hand on knob, pure stillness), `walk` x2 first half (slow precise approach, cane taps floor)
> Row 2: `walk` x4 last (cane-tap continues), `atk1` x2 first half (cane thrust — F1-2 wind-up shoulder back)
> Row 3: `atk1` x3 last (F3 full extend sword tip forward, F4 hold, F5 retract), `atk2` x3 first half (cross sweep — F1 cane raised diagonally, F2 horizontal slash with body torque, F3 follow-through with jacket flare like a cape)
> Row 4: `atk2` x3 last (F4-5 reset to stance, F6 idle), `atk3` x3 first half (fencing lunge — F1 coil down, F2-3 explosive forward lunge with sword leading)
> Row 5: `atk3` x4 last (F4-5 hold the lunge — longest reach pose, F6-7 recover to stance), `special` x2 first half (chain whip — F1 pulls watch out of vest, F2 winds chain in half-circle)
> Row 6: `special` x6 last (F3-4 winds higher, F5-7 horizontal wide arc across screen at chest height with motion-blur on chain, F8 watch returns to pocket)
> Row 7: `special` x2 final (F9 cane re-planted, F10 idle reset), `counter` x4 (F1 sheath raised to deflect, F2 deflect impact, F3 immediate sword thrust forward, F4 recovery)
> Row 8: `counter` x1 last (F5 reset), `hurt` x3 (body folds slightly at waist, glasses STAY ON, half-smile STAYS, sword stays in hand), `glove_off` x2 first half (Kane stands from desk — F1, removes right glove with precise tug — F2)
> Row 9: `glove_off` x2 last (F3 drops glove, F4 draws sword from cane), `dead` x4 first half (falls backwards over the desk — F1-2 falling, F3-4 landed)
> Row 10: `dead` x1 last (F5 — half-smile finally drops for ONE frame, his face is empty), 5 spare cells
>
> **DO NOT include:** any resemblance to a real public figure (if a draft looks like a known person, change features until it doesn't). No symmetric smile — always lopsided (left corner only). **NO pistol, gun, or modern firearm of any kind** — he fights with the sword-cane and the chain whip only. No modern phone, laptop, tablet on the desk — period props only. No bare hands except the right hand from `glove_off` onward. No mussed hair or open jacket — appearance stays perfect except on `dead`. The smile should never reach the eyes.
>
> Pixel-art style, clean silhouette, hard edges, exaggerated caricatured proportions. Kane is tall enough to fill the cell height comfortably; the desk only appears in `idle` and `glove_off` frames.

---

## After generation — wiring it up

When each enemy/boss sheet is saved as `characters/<type>.png`:

1. I'll add a layout config at `layouts/<type>_layout.json` mapping each row to its animation slot
2. Run `python3 pipeline.py build-atlas layouts/<type>_layout.json --output characters/<type>_atlas.json`
3. Wire the engine renderer to prefer the sprite when present (currently the per-enemy `drawTank`, `drawSlice`, etc. functions render procedurally)

Tell me when you've finished a stage's sprites and I'll wire that stage's sprites into the engine. You don't have to do all stages at once — generate stage 1's three sheets, ping me, I integrate them; then stage 3, etc.
