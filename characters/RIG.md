# RIG

Kane's construction-crew muscle. These were already on Kane's payroll — laborers and demolition workers who knew what would happen to a holdout block long before anyone else did. They show up to fights in the same hard hats and steel-toes they wore on shift. Most of them are just *doing the job*.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **10 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — HARDHAT RAM-JAB (5 frames) — **HEAD LOWERS so the YELLOW HARDHAT tilts forward like a battering ram**, lead fist then drives forward UNDER the brim
> 4. `atk2` — STEEL-TOE BOOT KICK (5 frames) — **kicking leg STRAIGHT FORWARD at hip height with the boot SOLE leading FLAT**, body leans BACK 10° for counter-balance
> 5. `atk3` — IRON-CLAP THUNDER (5 frames) — **both hands SMASH TOGETHER at chest height in a loud iron-clap**, two horizontal shockwave arcs of brown dust radiate left AND right at chest height (the only attack where both fists MEET in front of the chest)
> 6. `atk4` — CONCRETE-BREAKER OVERHEAD (6 frames) — **both fists CLASPED above the hardhat, then DRIVE DOWN in a vertical chop into the target's head**, body folds 30° forward at impact (vertical DESCENDING arc, different from atk6's column-then-floor stomp)
> 7. `atk5` — SHOULDER-CHARGE WRECKING BALL (6 frames) — **body lowers, RIGHT SHOULDER drops forward, hardhat angles forward**, body CHARGES 12 px forward with motion-blur streaks behind both boots (the only attack where Rig moves forward — wrecking-ball lunge)
> 8. `atk6` — PNEUMATIC-DRILL POUND (12 frames) — **VERTICAL COLUMN silhouette** (both fists clasped above the hardhat, body stretched fully UP from heels to hands), then PILEDRIVES downward with a shockwave dust ring + vertical dust plume (the AOE finisher)
> 9. `hurt` (3 frames)
> 10. `dead` (4 frames)
>
> **Total: 56 frames in 10 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Rig's six attacks must each occupy a DIFFERENT silhouette quadrant — the generator's failure mode is "construction worker swinging a fist" for every move. Every attack also has a unique signature beat (the hardhat-tilt, the boot-sole, the iron-clap shockwave, the overhead chop, the charging lunge, the AOE column) that exists nowhere else in his sheet:
>
> | Attack | Body axis | Striking limb | Direction | Unique signature beat |
> |---|---|---|---|---|
> | `atk1` ram-jab | Body bent FORWARD 20°, head LOWERED so hardhat angles forward | YELLOW HARDHAT + lead fist | Horizontal forward at chest height | HARDHAT TILTED FORWARD like a battering ram (head dropped below shoulder line) + lead fist drives in UNDER the brim — only attack where the head leads |
> | `atk2` boot kick | Body LEANS BACK 10° for counter-balance | Kicking LEG, boot SOLE flat | Horizontal forward at hip height | Boot SOLE pointing flat at the target (sole-of-boot is the focal point, not toe or heel) + body leans BACKWARD + 2-px dust at supporting boot — only leg attack |
> | `atk3` iron-clap | Body squared, arms swung in from both sides | BOTH fists meeting at chest height | Lateral inward then HORIZONTAL shockwave | Both fists MEET IN FRONT OF THE CHEST with a 4-px white impact spark + TWO horizontal brown shockwave arcs radiating LEFT AND RIGHT at chest height (~24 px each side) — only chest-height shockwave |
> | `atk4` concrete-breaker | Body stretched UP then folded forward 30° | BOTH fists CLASPED overhead | Descending VERTICAL chop ending at head height of target | Both fists clasped above hardhat then DROPPED in a vertical comet path that STOPS at head height (not floor level) + 1-px white impact spark at the imagined target head + hardhat tilts forward 1 px on the fold-through — only descending overhead chop |
> | `atk5` wrecking-ball charge | Body angled 35° forward, RIGHT SHOULDER lowered and leading | RIGHT SHOULDER (+ hardhat front) | Charging FORWARD 12 px through the active frames | Body MOVES forward 12 px across the attack (no other Rig attack moves the body) + 3-px brown motion-blur streaks behind BOTH boots + free arm trails behind for balance — only locomoting attack |
> | `atk6` pneumatic-pound | Body fully VERTICAL stretched UP, then folds straight DOWN to floor | BOTH fists clasped above hardhat | Vertical UP then vertical DOWN to floor | VERTICAL COLUMN — body stretched from heels to clasped fists above hardhat (tallest Rig ever gets) + impact has FLOOR-LEVEL SHOCKWAVE RING (radiating 36 px each side at boot height) + vertical dust plume up to hardhat height — only AOE attack with floor shockwave + only attack that hits both sides |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk5:** both involve the hardhat angled forward, but atk1 is STATIONARY (body bent at the waist over the front foot) and atk5 is CHARGING (body angled forward AND moving 12 px through the attack with motion-blur streaks). If atk5 looks like atk1 with the same posture, redraw — atk5 must show the body in transit and dust streaks behind both boots.
> - **atk3 vs atk4:** both use TWO hands — but atk3 brings the fists IN FROM OUTSIDE to MEET IN FRONT OF THE CHEST (lateral collision at chest height with sideways shockwave arcs), while atk4 brings the fists DOWN FROM OVERHEAD as a single clasped fist-block (vertical comet arc that stops at head height). atk3 shockwaves spray sideways at chest height; atk4 has no shockwave (it lands on a target, not the floor).
> - **atk4 vs atk6:** both involve clasped fists overhead. atk4 ENDS at head height of the imagined target (~chest-to-shoulder height of Rig), body bent forward 30°. atk6 ENDS at the FLOOR with both fists at boot level and a floor-level shockwave ring radiating outward. atk4 is a head-shot chop, atk6 is a ground-pound AOE. If atk4 hits the ground, redraw — that would conflate with atk6.
> - **atk1 vs atk3:** atk1's body bends FORWARD over the front foot with the hardhat tilted (the fist is one arm). atk3's body stays VERTICAL with both fists meeting in front (both arms involved). Different body angles and different arm counts.
> - **atk2 vs walk:** atk2's kicking leg is STRAIGHT FORWARD at HIP height with the body rocked back — it must look nothing like a walk stride. If atk2 reads as a heavy step, redraw with the leg clearly extended past the body and the sole flat.
> - **Hardhat-on rule:** the yellow hardhat is on the head in EVERY frame including hurt and dead. If any frame shows a bareheaded Rig, redraw — the hardhat is identity.
> - **Bare-fists rule:** Rig never carries a wrench, hammer, brick, or any other tool — both hands are empty in every frame. The hands ARE the tools. If any attack shows a weapon, redraw.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> **The yellow hardhat is on his head in EVERY frame, in EVERY animation**, including hurt and dead. The hardhat is Rig's identity item — a frame without it is a wrong frame.
>
> Cells must contain only the character — no labels, no row headers, no frame numbers, no cell borders.
>
> Rig is **one specific worker** across every cell — same face, same beard / clean-shaven choice (pick one), same hardhat, same orange vest, same brown pants. Only the pose changes.

## Physical

- **Age range:** 28–45
- **Height/build:** 6'0" – 6'4", thick. Pure-mass build from manual labor. Shoulders broader than Tank; gut tighter.
- **Body language:** Heavy and slow. Doesn't bounce. Hands curled into fists at thigh height. Spits to the side occasionally (1 frame, 1 px).
- **Face:** Weathered. Scruffy stubble or full beard. Some have safety goggles pushed up onto the hard hat.

## Hair

- Mostly hidden by the hard hat. What's visible: short, sweat-flat, shades of brown or grey.

## Costume (head to feet)

1. **Yellow hard hat** — `#cfa040`. Battered, scuffed at the brim. The single most visible thing about Rig.
2. **High-vis safety vest** — fluorescent orange (`#ff7a30`) over a brown work shirt. Two reflective grey stripes (`#a8a8a8`) horizontal across the front.
3. **Brown work shirt** — long sleeves rolled up to the elbow. Forearms exposed, hairy.
4. **Dirty work pants** — khaki-brown (`#7a5a3a`), oil stains visible (darker patches).
5. **Steel-toed work boots** — heavy brown leather (`#3a2a1c`) with grey steel toes (`#5a5a5a`). Bigger than Atlas's; chunkier sole.
6. **Heavy leather work belt** with hammer loops (empty — he's not carrying tools today).

## Identity item — REQUIRED IN EVERY FRAME

**The yellow hard hat.** Always on the head, never knocked off (even on hurt / dead frames — it stays). Has a small black "KANE PROPERTIES" logo (`#1a1a22`, ~3 px square) on the front-left of the brim. The combination of the hard hat + hi-vis orange vest is what makes Rig instantly readable as a *worker*, not a thug.

## Palette (hex)

```
hard hat yellow    #cfa040
hard hat hi        #e8c860
hard hat shadow    #8a6020
hard hat logo      #1a1a22
hi-vis orange      #ff7a30
hi-vis hi          #ffa050
hi-vis shadow      #b04a10
reflective stripe  #a8a8a8
work shirt         #7a5a3a
work shirt shadow  #3a2a18
pants              #7a5a3a
pants shadow       #3a2a18
boot leather       #3a2a1c
boot toe (steel)   #5a5a5a
skin (light)       #d4a888     (vary)
skin (shadow)      #9a785a
beard              #4a3a28
```

## Personality / fighting style

- **Mutters during fights.** Short worker-talk phrases: "Just doin' the job." or "Move it, kid." Not malicious; bored.
- **Doesn't chase fast.** Walks. Trusts his weight to do the work. But will charge with the wrecking-ball shoulder when given an opening.
- **Six signature moves — all bare-fisted. The hands ARE his tools.** Every move carries an industrial-construction signature beat (battering-ram hardhat, sole-print kick, iron-clap shockwave, sledgehammer overhead, wrecking-ball charge, pneumatic pound).
  - **`strike` — Hardhat ram-jab.** Not a regular punch. **Visual signature: F1 he LOWERS his head and angles the yellow hardhat forward like a battering ram**, body bent at the waist. F2 he drives forward with the hardhat leading, free arm trailing. F3 the lead fist comes in BENEATH the hat as a hook — hardhat threatens, fist lands. 14 dmg, 130 knockback.
  - **`boot_kick` — Steel-toe front kick.** Heavy front-thrust kick with the steel-toed work boot. **Visual signature: F3 silhouette has the kicking leg extended STRAIGHT FORWARD at hip height with the boot SOLE leading flat (a flat horizontal boot-print pointing at the target). Body leans back 10°, both arms thrown back. The thick brown sole is the focal point.** 12 dmg, 110 knockback.
  - **`clap` — Iron-clap thunder.** Both massive hands swing in from OUTSIDE and SMASH TOGETHER at chest height with a thunderous concussion. **Visual signature: F3 BOTH FISTS MEET IN FRONT OF THE CHEST with a 4-px white impact spark + TWO horizontal brown dust shockwave arcs radiate LEFT AND RIGHT at chest height (~24 px each side)**. Reads like clanging two iron plates. 11 dmg, 100 knockback. Stuns briefly.
  - **`overhead` — Concrete-breaker.** Sledgehammer-style overhead chop with both clasped fists driving DOWN onto the target's HEAD. **Visual signature: F2 BOTH FISTS CLASPED ABOVE THE HARDHAT (body stretched tall); F4 DRIVE DOWN in a vertical comet arc that lands at HEAD HEIGHT of the imagined target (not floor level — atk6 does that); body folds 30° forward at impact**. The only descending overhead chop. 16 dmg, 150 knockback.
  - **`charge` — Wrecking-ball shoulder charge.** Lowers body, RIGHT SHOULDER drops forward and LEADS, and Rig CHARGES 12 px forward through the attack like a runaway wrecking ball. **Visual signature: body angled 35° forward, shoulder lowered below the chin, hardhat angled forward; 3-px brown motion-blur streaks behind BOTH boots; free arm trails behind for balance**. The only attack where Rig MOVES forward. 13 dmg, 140 knockback + tackles the player.
  - **`pound` (every 5th attack) — Pneumatic-drill earthquake.** AOE ground smash. **Visual signature: F5–F6 silhouette is a vertical column — both fists clasped above the hardhat, body fully stretched UP into a straight line from heels to hands**. Then piledrives downward — F10 impact has a **floor-level shockwave ring radiating outward from his boots** (2-px arc of brown dust specks, 36 px each side) **plus a vertical dust plume rising up his body** to hat height. Hits both sides. Hardhat locked on. Super-armored throughout.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | Heavy chest rise. Hardhat brim catches a 1-px yellow highlight on F2. Shoulders rolled forward (working-man posture). Both fists hang at thigh height, half-clenched. |
| `walk`   | 6 | **Heavy worker stomp gait that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 = LEFT leg fwd + RIGHT arm fwd swing (at side, hip-level). F2 = passing position. F3 = RIGHT leg fwd + LEFT arm fwd swing. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. **Both arms swing in a relaxed arc AT THE SIDES** — fists half-clenched at hip height. Arms NEVER extend forward past the body (would read as the headbutt wind-up). Hardhat stays level on the head — does NOT tilt forward during walk (the forward tilt is the atk1 tell, reserved). Boots flat-footed, body barely sways. **Dust puff (1 brown speck) at the planted boot heel on F1, F3, F5**. Vest jiggles 1 px on impact. No planted/stomp pose on F6 — the cycle blends straight back. |
| `atk1`   | 5 | **Hardhat ram-jab.** F1 = head LOWERS, hardhat tilts forward like a ram, body bends at waist, fists rise. F2 = step forward (hardhat leading). F3 = peak — lead fist drives forward UNDER the hardhat brim, hardhat still angled forward, free arm trailing. F4 = retract fist. F5 = head rises back, hardhat re-levels. |
| `atk2`   | 5 | **Steel-toe boot kick.** F1 = kicking leg raises (knee to chest), supporting leg planted, body leans back 5°. F2 = leg begins extending forward. F3 = peak — leg straight forward at hip height, boot SOLE leading flat at the target, body leaned back 10°, both arms thrown back. **2-px dust at supporting boot**. F4 = leg starts retracting. F5 = boot plants back, body returns to stance. |
| `atk3`   | 5 | **Iron-clap thunder.** F1 = both arms drawn out to the sides at shoulder height, palms facing inward, body squared. F2 = arms beginning to swing IN toward each other, chest rising slightly. F3 = **peak — BOTH FISTS MEET IN FRONT OF THE CHEST with a 4-px WHITE IMPACT SPARK at the meeting point + TWO horizontal brown dust shockwave arcs radiating LEFT AND RIGHT at chest height (~24 px each side, 2-px arc thickness)**. Body squared, knees braced. F4 = fists hold together for 1 frame (the concussion). F5 = arms drop back to thigh height, recovery. |
| `atk4`   | 6 | **Concrete-breaker overhead.** F1 = both fists rise from hip toward chest, body coiling. F2 = **both fists CLASPED ABOVE THE HARDHAT, body stretched fully tall, hardhat steady on the head**. F3 = clasp held 1 frame (the launch tell). F4 = **DRIVE — clasped fists arc DOWN in a vertical comet path, body folding forward 30° at the waist, ending at chest/head height of the imagined target**. 1-px white impact spark at the fists. Hardhat tilts forward 1 px on the fold-through. F5 = follow-through, clasped fists past the impact line. F6 = arms unclasp and drop to thigh height, body straightens. |
| `atk5`   | 6 | **Wrecking-ball shoulder charge.** F1 = body lowers (knees bend), RIGHT SHOULDER drops forward, hardhat angles forward. Free (left) arm pulls back behind for balance. F2 = forward step — body angled 25° forward, motion-blur streaks beginning behind both boots (1 px). F3 = **CHARGE — body angled 35° forward with RIGHT SHOULDER LEADING (shoulder LOWER than the chin), hardhat brim pointed at imagined target, body MOVED 6 px forward; 3-px brown motion-blur streaks behind BOTH boots**. F4 = impact — body MOVED 12 px total from start, shoulder driving through the target, 1-px white impact spark at the shoulder, motion-blur streaks at peak intensity. F5 = follow-through — body still moving forward, shoulder past the impact line. F6 = recovery — body straightens, free arm settles, streaks fade. |
| `atk6`   | 12 | **Pneumatic-drill earthquake (pound).** F1 = both arms start rising, knees bend. F2–F3 = arms continue up, body straightening (small dust specks at boots). F4 = arms above head, fists clasping (more ground specks). F5 = **vertical column pose — fists clasped above hardhat, body stretched fully UP from heels to hands**. F6 = held column (1 frame). F7–F8 = drive downward (body folds, fists arcing all the way down to boot level). F9 = body fully folded, fists AT BOOT LEVEL. F10 = **IMPACT — FLOOR-LEVEL shockwave dust ring radiating 36 px on each side at boot height (2-px arc thickness), vertical dust plume rising up to hardhat height**. F11 = recovery start. F12 = back to standing. |
| `hurt`   | 3 | Stagger. Head turns 10°. **Hardhat stays on.** |
| `dead`   | 4 | Falls FORWARD onto the ground (face down, hardhat lands first). Hardhat stays on the head through all 4 frames. |

## DO NOT include

- **Text labels inside cells** — no `idle`, no `walk`, no `atk1`, no row headers, no frame numbers.
- **Cell separator lines or borders.**
- **A bareheaded Rig in any frame** — yellow hardhat is on the head in every single cell, including hurt/dead.
- **A different worker across frames** — same face, same beard choice, same hat, same vest, same pants in every cell.
- Tactical / military gear — Rigs are construction workers, not soldiers.
- Visible weapons — bare fists only. (Ironic that the most dangerous AOE in the game is empty-handed.)
- Clean, pressed clothing — everything is worn-in and stained.
- The hard hat replaced by a beanie or other headgear. Stays the yellow construction helmet.

## Visual VFX summary

Rig's identity is the **yellow hardhat** (always on, even when hit/dead) + dust at his boots + construction-site signature beats. **Every attack occupies a distinct silhouette quadrant AND a unique signature beat** (see the SILHOUETTE DIFFERENTIATION table near the top).

- `atk1` HARDHAT RAM-JAB — body bent forward 20°, head LOWERS with the yellow hardhat tilted forward like a battering ram + lead fist drives forward UNDER the hardhat brim (only attack where the head leads)
- `atk2` STEEL-TOE BOOT KICK — kicking leg straight forward at hip height with the boot SOLE flat at the target + body leans BACK 10° + 2-px dust at supporting boot (opposite body angle from atk1)
- `atk3` IRON-CLAP THUNDER — BOTH fists meet IN FRONT OF THE CHEST + 4-px white impact spark at the meeting point + TWO horizontal brown shockwave arcs radiating LEFT AND RIGHT at chest height (the only chest-height shockwave; reads like clanging two iron plates)
- `atk4` CONCRETE-BREAKER OVERHEAD — both fists CLASPED ABOVE THE HARDHAT then DRIVE DOWN in a vertical comet path ending at head height of the target + body folds 30° forward + hardhat tilts forward 1 px on the fold-through (the only descending overhead chop, sledgehammer-style)
- `atk5` WRECKING-BALL CHARGE — body angled 35° forward with RIGHT SHOULDER LEADING (shoulder lower than the chin) + body MOVES forward 12 px through the attack (only attack where Rig moves) + 3-px brown motion-blur streaks behind BOTH boots
- `atk6` PNEUMATIC-DRILL POUND — VERTICAL COLUMN silhouette (fists clasped above hardhat, body stretched fully UP from heels to hands) + FLOOR-LEVEL shockwave dust ring radiating 36 px each side at impact + vertical dust plume up to hardhat height (the only AOE + only attack that hits both sides)

**Signature-beat dictionary (read from across the screen).** The following beats appear EXACTLY ONCE in Rig's whole sheet:
- Hardhat tilted forward as a ram (head dropped below shoulder line) — atk1 only
- Boot SOLE flat at the target — atk2 only
- TWO horizontal shockwave arcs at CHEST height radiating left AND right — atk3 only
- Clasped fists arcing DOWN to head-height (NOT floor) — atk4 only
- Body MOVING forward 12 px with motion-blur streaks behind both boots — atk5 only
- FLOOR-LEVEL shockwave ring + vertical dust plume — atk6 only

**Hurt / flinch:** F1 stagger, head turns 10°. F2 hardhat STAYS ON (his signature — never falls off). 1-px white impact spark on the vest. F3 returns to stance.

**Dead:** Falls FORWARD onto the ground (face down, hardhat lands first). Hardhat stays on the head through all 4 frames.

## Sheet specs

- 8 columns × 5 rows = 40 cells (~35 frames used; pound attack is the big one at 12)
- Cell size: **64 × 80**
- Magenta `#ff00ff` background
- Bottom-center anchor
