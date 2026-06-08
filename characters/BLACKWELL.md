# BLACKWELL — Optional / Brutal-tier Encounter

Kane's personal bodyguard. Real name **Marcus Blackwell** (no relation to Rio's Marcus, despite the coincidence — the universe is cruel that way). He doesn't run a crew. He doesn't run errands. His only job is to be inside whatever room Kane is in.

In the engine: BLACKWELL spawns as an extra wave on stages 7 and 8 in **brutal** difficulty only. He's a wall between the player and the final stage. If you can beat him on brutal, you've earned the run.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **12 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames) — **ARMS CROSSED tight over chest**, gold ring catches periodic highlight
> 2. `walk` (6 frames)
> 3. `atk1` — STEPPING HOOK + KNUCKLE SPARK (6 frames) — **REAR (gold-ring) fist HORIZONTAL inward arc at chest height**, body torqued 60° + 4-px white star-burst at the gold-ring fist on contact
> 4. `atk2` — RISING KNEE STRIKE (5 frames) — **REAR knee DRIVES UP at gut height** + BOTH hands GRAB an imagined collar and PULL DOWN onto the knee, body folded forward 25° (wrestler-style, NOT a kick)
> 5. `atk3` — CONCRETE-BREAKER CHARGE (12 frames) — **body LOWERED to chest-height shoulder charge, traveling FORWARD across the floor** + 3 visible jagged floor cracks trailing the footsteps (the only forward-traveling attack outside the special)
> 6. `atk4` — APOCALYPSE OVERHEAD (13 frames) — **BOTH fists CLASPED overhead in a question-mark arch then SLAMMED DOWNWARD into the floor** + 8-direction concrete-chunk debris radiating from impact + vertical dust plume past head height (the only attack that ends with fists into the floor)
> 7. `throat_lift` — ONE-HANDED THROAT-LIFT SLAM (9 frames) — **SINGLE lead hand clamps the throat and LIFTS the opponent VERTICALLY off the ground** (legs visibly dangling limp), then arcs down for the slam (the only one-handed grab)
> 8. `earthquake` — DOUBLE-FOOT EARTH STOMP (8 frames) — **brief AIRBORNE hop then BOTH FEET slam down together** + 5 concentric expanding shockwave rings radiating outward 360° AOE both sides (the only AOE that fires from the FEET)
> 9. `special` — JUGGERNAUT CHARGE-GRAB-SPIN-THROW (16 frames) — wrestler's Giant Swing: **charges in, GRABS opponent's LEG, SPINS them upside-down around his body like a propeller blade, launches them off-screen as a projectile** (the only attack where the opponent's body traces a full circle around Blackwell)
> 10. `counter` — IRON WALL SHOCKWAVE + COUNTER-CROSS (7 frames) — **ARMS STAY CROSSED to catch the strike** + 8-pointed white star-burst + 3 concentric shockwave rings at parry impact, then a counter-cross with 3 ghost-fist trails (the only attack where Blackwell starts FROM the crossed-arm idle)
> 11. `hurt` (3 frames) — almost no flinch, head turns 5°, arms stay crossed
> 12. `dead` (7 frames) — falls slowly in stages
>
> **Total: 96 frames in 12 rows.** Every row must be present. The visual VFX (sparks, debris, shockwave rings, ghost-fist trails) are what distinguishes Blackwell from a generic heavy striker — without them his moves read flat.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Blackwell's sheet kept producing attacks that all looked like "big bald man swinging both arms." Every attack below must occupy a DIFFERENT silhouette quadrant — if two attacks share a silhouette, redraw one. Blackwell's whole identity is the **slow inevitability of a wall that moves** — each attack must feel like a different kind of structural collapse.
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` stepping hook | Vertical, torso rotated 60° on a forward step | REAR (gold-ring) fist | Horizontal inward arc at chest height | Single forward step + 4-px WHITE STAR-BURST at the gold-ring fist on contact (the only single-fist forward strike + the only impact-spark VFX) |
> | `atk2` rising knee | Folded forward 25°, body crouched on the supporting leg | REAR knee + BOTH hands gripping | Knee UP into the gut + collar PULLED DOWN | Both hands gripping an imagined collar and yanking DOWN onto the rising knee — only attack where Blackwell is HOLDING + striking with a knee simultaneously |
> | `atk3` concrete-breaker charge | Body LOWERED, shoulder leading horizontal | LEAD shoulder | Forward, traveling across the floor | 3 visible JAGGED FLOOR CRACKS trailing each footstep (only attack that scars the floor while traveling) + body horizontal-low silhouette during the charge phase |
> | `atk4` apocalypse overhead | Vertical, body ARCHED backward in question-mark then folded forward | BOTH fists CLASPED | Descending vertical INTO the floor | Body arched into a backwards question-mark at peak + impact ends with both fists DRIVEN INTO THE FLOOR + 8 concrete-chunk debris in a star pattern (the only attack that breaks the floor open) |
> | `throat_lift` one-handed slam | Vertical, single arm extended out at neck height | LEAD hand (closed throat grip) | Lift VERTICAL then slam arc | Opponent dangling VERTICALLY with feet OFF the ground, held in ONE hand at arm's length, legs visibly LIMP — the only one-handed grab + only vertical-lift pose |
> | `earthquake` double-foot stomp | Vertical, briefly AIRBORNE then both feet planted wide | BOTH FEET | Downward, then 360° shockwave outward at ground level | Both feet on the ground simultaneously + 5 concentric EXPANDING DUST RINGS at ground level radiating omni-directionally (the only AOE that fires from the FEET) |
> | `special` juggernaut spin-throw | Body upright spinning in place, holding opponent extended outward | Opponent's body (as a flail) + leg-grip | Opponent traces a full 360° circle around Blackwell | Opponent's BODY is the silhouette tell — held UPSIDE-DOWN by one ankle, body horizontal extended outward like a propeller blade tracing a circle around Blackwell (the only attack where the opponent is the weapon) |
> | `counter` iron wall + counter-cross | Vertical, arms CROSSED tight then exploding outward | Crossed forearms (block) → REAR cross | Catch incoming strike then cross forward | F2 has the 8-POINTED STAR-BURST + 3 SHOCKWAVE RINGS at the crossed-forearm impact point (only attack that starts from the crossed-arm idle pose) + F5 has 3 GHOST-FIST motion-blur trails behind the counter-fist (only attack with motion-blur ghost trails) |
>
> Cross-checks before approving the sheet:
> - **atk1 vs counter:** atk1's gold-ring fist generates a 4-px WHITE STAR-BURST on contact. Counter generates an 8-POINTED STAR-BURST + 3 SHOCKWAVE RINGS on the crossed-arm parry — different number of points (4 vs 8) and counter has the concentric rings. If both look like the same spark, redraw counter's burst at 8 points with 3 rings.
> - **atk2 vs throat_lift:** atk2 grabs with BOTH hands at SHOULDER height and yanks DOWN onto a rising knee. throat_lift grabs with ONE hand at NECK height and lifts the opponent STRAIGHT UP. If atk2 lifts the opponent off the ground, redraw — atk2 PULLS DOWN, throat_lift LIFTS UP. Opposite verticals.
> - **atk3 vs special charge:** atk3 is a pure forward shoulder charge (impacts and that's it). Special starts with a charge but then GRABS the LEG and SPINS. If the special looks like atk3 with no grab, redraw — the grab+spin IS the special's identity, and the opponent must be visibly UPSIDE-DOWN by F7.
> - **atk4 vs earthquake:** atk4 ends with BOTH FISTS driven into the floor (impact from the hands) + concrete-chunk debris in a star. earthquake ends with BOTH FEET stomping the floor (impact from the feet) + dust ring shockwaves. Same source-material (the floor) but different impact limbs and different debris types — if atk4 shows dust rings or earthquake shows concrete chunks, the VFX are crossed.
> - **earthquake vs special spin:** both are AOE-feeling. Earthquake is rings of dust expanding OUTWARD on the ground around Blackwell — nothing moves through the air at chest height. Special has the opponent's BODY moving in a circle at chest height — nothing happens on the floor. If earthquake shows a body flying around or special shows ground rings, the silhouettes are crossed.
> - **counter vs idle:** counter STARTS from the crossed-arm pose and stays crossed for F1–F2. If counter F1 shows the arms already uncrossed, redraw — the crossed-arm catch IS the move's identity, and the parry star-burst happens AT the crossed forearms.
> - **Every attack except idle/walk/counter requires arms UNCROSSED.** All other attacks must begin with an F1 that shows the arms uncrossing — counter is the lone exception where the crossed pose IS the block.

## Physical

- **Age:** 44
- **Height/build:** 6'5", massive. Heavier than Atlas, heavier than Tank. Pure-mass strongman build that hasn't gone soft. Arms thicker than the protagonist's torso.
- **Skin:** Black, very dark (`#3a2418`).
- **Body language:** Still. Stands with arms crossed in idle. Doesn't bounce, doesn't shift weight. Watches with patience. Every motion is committed — he doesn't telegraph; he just *moves*.
- **Face:** Square jaw. Thin gray-black goatee. Small scar above the left eyebrow. Resting expression: blank. He doesn't show anything until he hits.

## Hair

- Shaved completely smooth. No facial hair other than the goatee.

## Costume (head to feet)

1. **Black tactical turtleneck** — `#0a0a10`, long sleeves, fitted, neck up to the chin. Modern, high-end fabric.
2. **Tactical chest holster rig** over the turtleneck — leather (`#1a1410`) with empty pistol holsters on each side (he doesn't draw guns; the holsters are decoration / threat).
3. **Slim black tactical pants** — same matte black, tucked into boots.
4. **Heavy combat boots** — black, polished, laced full to the calf.
5. **Black leather gloves** — fitted, hand-stitched, no fingertips exposed.

## Identity items — REQUIRED IN EVERY FRAME

1. **The crossed-arms idle pose** — arms folded across the chest. This is Blackwell's silhouette in idle. He uncrosses only to attack.
2. **A heavy gold ring on the right pinky** — the only color on him. `#cfa040` with a 1-px black engraving (Kane Properties insignia). 2 × 2 px. Visible during attacks.
3. **The tactical chest holster rig with empty holsters** — visible in every frame. The empty holsters are the threat: he doesn't NEED them.

## Palette (hex)

```
turtleneck black   #0a0a10
turtleneck shadow  #050507
turtleneck hi      #1c1c22
holster rig        #1a1410
holster strap      #2a1f15
pants              #0a0a10
boot               #050507
boot polish hi     #1c1c22
glove leather      #16100a
skin (light)       #6a4a30
skin (mid)         #4a2c1a
skin (shadow)      #2a1810
skin (deep)        #1a0e08
goatee dark        #2a201a
goatee grey        #5a5450
gold ring          #cfa040
gold ring shadow   #8a6020
ring engraving     #1a1a22
```

## Personality / fighting style

- **Eight signature moves — hook+spark / knee / charge / overhead / throat-lift / earthquake / juggernaut / iron wall. Every move involves visible VFX (sparks, debris, shockwaves, floor cracks, ghost-trails) — Blackwell's identity is the WALL OF MUSCLE that BREAKS the floor when he moves.**
  - **`hook` — Stepping hook with knuckle spark.** Step forward, body torque, gold-ring fist whips around. **Visual signature: F4 a 4-px WHITE STAR-BURST erupts at the gold-ring fist on contact** (his brass-knuckle-equivalent spark — no other character emits an impact spark). 16 dmg.
  - **`knee` — Rising knee strike.** Wrestler-style knee, not a karate kick. **Visual signature: F3 both hands GRAB the imagined opponent's collar and pull DOWN onto the rising knee, body folded forward 25°. Pure brawler move.** 20 dmg.
  - **`charge` — Concrete-breaker shoulder charge.** **Visual signature: 3 visible JAGGED FLOOR CRACKS appear in the floor under each footstep across F5–F7, getting bigger with each stride. F9 impact has a 1-frame screen-jitter suggestion.** Super-armored, 24 dmg.
  - **`overhead` — Apocalypse smash.** Question-mark wind-up, drives both fists into the floor. **Visual signature: F12 IMPACT — 8 light-grey CONCRETE-CHUNK chips radiate in a star pattern (N/NE/E/SE/S/SW/W/NW) PLUS the brown dust burst PLUS a vertical dust plume past head height. He literally breaks the floor open.** 32 dmg + super-armored.
  - **`throat_lift` — One-handed throat-grab slam.** **Visual signature: F3 SINGLE-HAND grab clamps on the imagined opponent's throat. F3 LIFTS them VERTICALLY off the ground (legs visibly dangling limp). F6–F7 slam arc as he swings them down to the floor.** Cinematic intimidation move. 28 dmg.
  - **`earthquake` — Double-foot earth stomp (AOE).** Brief jump, slams both feet down. **Visual signature: F7 silhouette has 5 CONCENTRIC EXPANDING SHOCKWAVE RINGS of dust radiating outward from his feet (12 px, 24 px, 36 px, 48 px, and a forming 5th ring at the boundary). True AOE — hits both sides.** 22 dmg.
  - **`special` — JUGGERNAUT charge-grab-spin-throw (signature).** Wrestler's Giant Swing. **Visual signature: F9–F11 the imagined opponent visibly SPINS AROUND Blackwell like a propeller blade — body horizontal, motion-blur arc tracing their head through a full circle around Blackwell. F12 he RELEASES, opponent FLIES off-screen at chest height as a projectile.** 36 dmg + super-armored. No other character does this move.
  - **`counter` — IRON WALL shockwave + counter-cross.** Catches the incoming attack on crossed forearms. **Visual signature: F2 8-POINTED WHITE STAR-BURST at the contact point + 3 CONCENTRIC SHOCKWAVE RINGS expanding outward (8 px, 14 px, 20 px). F5 counter-cross has 3 GHOST-FIST motion-blur trails behind the moving fist (impossible-speed motion blur for a man his size).** The parry itself is explosive.
- **Doesn't talk.** Ever. Not at start, not on hits, not on defeat.
- **Patient.** Waits for the protagonist to commit before acting. Uses earthquake when surrounded, juggernaut when player is mid-combo, iron wall when player is committing to a heavy.

## Animations

| Slot         | Frames | Notes |
|--------------|-------:|-------|
| `idle`       | 4 | **Arms crossed tight over chest.** Subtle chest rise. **Gold ring catches a 1-px highlight on F2.** Only the idle uses the crossed-arm pose. |
| `walk`       | 6 | Slow, deliberate. Arms stay crossed on F1–F3, then **uncross on F4 to swing naturally with the stride for F4–F6** (so walk reads different from idle). |
| `atk1`       | 6 | **Stepping hook + knuckle spark.** F1 = arms uncross fully. F2 = lead foot steps forward 16 px, rear arm cocks back behind the shoulder. F3 = peak — torso rotated 60°, rear fist mid-arc at chest height, body leaned 15° into the punch. F4 = **CONTACT — 4-px WHITE STAR-BURST at the gold-ring side of the fist** (his impact spark). F5 = retract. F6 = arms re-cross. |
| `atk2`       | 5 | **Rising knee.** F1 = arms uncross, body lowers into wrestler crouch. F2 = both hands rise to grab the imagined opponent's shoulders. F3 = **peak — rear KNEE driven UPWARD 20 px past body line at gut height, both hands PULLING the imagined opponent DOWN onto the rising knee, body folded forward 25°**. F4 = held strike. F5 = knee plants, arms re-cross. |
| `atk3`       | 12 | **Concrete-breaker charge.** F1 = arms uncross. F2 = stance widens. F3 = lead shoulder LOWERS to chest height. F4 = body fully horizontal at 35°, arms swept behind. F5 = launch — motion lines + **first 6-px JAGGED FLOOR CRACK under the rear boot**. F6 = stride 2, **second floor crack (bigger)**. F7 = stride 3, **third crack (biggest — the 3 cracks remain visible on the floor for several frames after the charge)**. F8 = approaching impact. F9 = **impact, body upright, dust burst + 1-frame screen-jitter (entire sprite jitters 1px)**. F10 = follow-through. F11 = recovery. F12 = arms re-cross. |
| `atk4`       | 13 | **APOCALYPSE overhead.** F1 = arms uncross. F2 = both arms rising. F3 = arms continuing up. F4 = arms approaching vertical. F5 = **peak — body fully vertical, both arms straight UP, fists clasped at apex, body arched backwards (question-mark)**. F6–F8 = held peak (3 frames). F9 = body folds forward, fists arcing down. F10–F11 = fists past head, body bent forward. F12 = **IMPACT — 8 LIGHT-GREY CONCRETE CHUNKS radiating in a star pattern (N, NE, E, SE, S, SW, W, NW — each chunk 2–3 px) + brown dust burst (10–12 specks reaching 50 px out) + vertical dust plume past head height**. F13 = straighten, dust + chunks still in the air. |
| `throat_lift`| 9 | **One-handed throat-lift + slam.** F1 = arms uncross, lead hand REACHES forward at neck height. F2 = **lead hand CLAMPS shut on the imagined opponent's throat (single hand, not two)**. F3 = **LIFT — opponent dangles VERTICALLY with feet OFF the ground, held one-handed at arm's length, legs visibly LIMP**. F4 = held lift (the intimidation beat). F5 = body coils for the slam. F6 = **SLAM ARC — arm swings forward + down, opponent following the arc**. F7 = **IMPACT — opponent CRASHES onto the floor, dust burst at impact zone**. F8 = release, hand opens. F9 = arms re-cross. |
| `earthquake` | 8 | **Double-foot earth stomp (AOE).** F1 = arms uncross, body coils — knees deep, arms swing up. F2 = body fully coiled, weight loaded. F3 = body explodes upward — **briefly AIRBORNE (small jump)**. F4 = APEX — both feet tucked under. F5 = **TOUCHDOWN — both feet slam DOWN SIMULTANEOUSLY. First SHOCKWAVE RING — 12-px circle of dust radiating from his feet**. F6 = **second ring at 24 px out (fainter)**. F7 = **third + fourth + fifth rings at 36 / 48 / 56 px out — 5 CONCENTRIC EXPANDING RINGS visible in this frame**. F8 = rings dissipate, arms re-cross. |
| `special`    | 16 | **JUGGERNAUT — charge / grab / spin-throw (wrestler's Giant Swing).** F1 = arms uncross. F2 = stance widens deep. F3 = **CHARGE start — body lowered, ground crack**. F4 = launch, motion lines, 2nd crack. F5 = **CONTACT — both arms reach forward to GRAB**. F6 = **GRAB the opponent's LEG (body bent over the leg)**. F7 = **LIFT — opponent now hanging UPSIDE-DOWN, held by one ankle**. F8 = SPIN start. F9 = **SPIN 90° — opponent extended outward like a propeller blade, body horizontal, 16-px motion-blur arc tracing their head**. F10 = **SPIN 180° — opponent on opposite side, 24-px motion arc**. F11 = **SPIN 270° — opponent's trajectory is a complete circle of arc-lines around Blackwell**. F12 = **THROW — releases the ankle, opponent FLIES off-screen at chest height as a projectile**. F13 = Blackwell stumbles back from centrifugal force, arms wide. F14 = recovery. F15 = stance returning. F16 = arms re-cross. |
| `counter`    | 7 | **IRON WALL shockwave + counter-cross.** F1 = arms cross TIGHTER (defensive guard). F2 = **incoming attack IMPACTS the crossed forearms — 8-POINTED WHITE STAR-BURST at the contact point + 3 CONCENTRIC SHOCKWAVE RINGS expanding outward (8 px, 14 px, 20 px) — instant ripple**. F3 = held parry pose (the "I caught that" beat). F4 = arms EXPLODE outward, rear arm winds up. F5 = **RETURN PUNCH — single devastating cross with gold-ring glint + 3 GHOST-FIST motion-blur trails behind the moving fist (decreasing alpha, impossible-speed effect)**. F6 = held punch, ghost-fists fading. F7 = arms re-cross. |
| `hurt`       | 3 | Body absorbs. Almost no flinch. Head turns 5°. Crossed arms stay crossed. |
| `dead`       | 7 | The first significant flinch IS the death animation. He goes down slowly, in stages — first to one knee, then to all fours, then onto his side. Stays unconscious. |

## DO NOT include

- Visible weapons — empty holsters only.
- A scowl or any visible emotion — Blackwell is *blank*.
- Loose, unfitted clothing.
- Decorative jewelry beyond the single gold ring.
- Tattoos.
- Speaking lines.

## Visual VFX summary

Blackwell's identity is the **wall of muscle that breaks the floor when he moves** — every attack has a distinct piece of destructible scenery in its VFX (spark, crack, chunk, ring, motion-blur, propeller arc). **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so no two moves blur together.

- `atk1` STEPPING HOOK + KNUCKLE SPARK — REAR (gold-ring) fist in a horizontal inward arc at chest height + 4-px WHITE STAR-BURST at the gold-ring fist on contact (the only single-fist forward strike + the only knuckle-spark VFX)
- `atk2` RISING KNEE STRIKE — REAR knee DRIVES UP at gut height + BOTH hands gripping an imagined collar and PULLING DOWN onto the rising knee, body folded forward 25° (the only attack where Blackwell holds AND strikes simultaneously)
- `atk3` CONCRETE-BREAKER CHARGE — body LOWERED, shoulder leading forward across the floor + 3 JAGGED FLOOR CRACKS trailing each footstep (getting bigger) + 1-frame screen-jitter on impact (the only attack that scars the floor while traveling)
- `atk4` APOCALYPSE OVERHEAD — body ARCHED backward into a question-mark with BOTH fists clasped overhead, then folded forward to DRIVE both fists INTO THE FLOOR + 8 LIGHT-GREY CONCRETE-CHUNK debris in a star pattern + vertical dust plume past head height (the only attack that breaks the floor open from above)
- `throat_lift` ONE-HANDED THROAT-LIFT SLAM — LEAD hand clamped on the throat, opponent dangling VERTICALLY with legs LIMP at arm's length, then arc-slam to the floor (the only one-handed grab + only vertical-lift pose)
- `earthquake` DOUBLE-FOOT EARTH STOMP — brief AIRBORNE hop then BOTH FEET slam down together + 5 CONCENTRIC EXPANDING SHOCKWAVE RINGS of dust radiating outward 360° at ground level (the only AOE firing from the FEET)
- `special` JUGGERNAUT CHARGE-GRAB-SPIN-THROW — charges in, GRABS opponent's LEG, holds them UPSIDE-DOWN by one ankle, SPINS them around his body like a propeller blade tracing a full 360° motion-blur arc at chest height, then RELEASES them off-screen as a projectile (the only attack where the OPPONENT is the silhouette)
- `counter` IRON WALL SHOCKWAVE + COUNTER-CROSS — arms STAY CROSSED to catch the strike + 8-POINTED WHITE STAR-BURST + 3 CONCENTRIC SHOCKWAVE RINGS at the parry impact, then a counter-cross with 3 GHOST-FIST motion-blur trails behind the moving fist (the only attack starting FROM the crossed-arm idle + only attack with ghost-fist trails)

**Hurt / flinch:** Almost no flinch (he's a wall). F1 head turns 5°, crossed arms STAY CROSSED even when struck. F2 1-px white impact spark on the forearms. F3 returns to idle.

**Dead:** The first significant flinch IS the death animation. He goes down slowly in stages — F1 folds at the waist, F2 to one knee, F3 onto both knees, F4 forward to all fours, F5 elbows give, F6 forehead touches ground, F7 settled face down.

## Sheet specs

- 8 columns × 6 rows = 48 cells (~45 frames used; he has the longest attack chain)
- Cell size: **80 × 104** — Blackwell reads as the BIGGEST silhouette in the game (yes, bigger than Atlas)
- Magenta `#ff00ff` background
- Bottom-center anchor

## Boss-fight design notes

- HP ≈ 360 (the highest in the game).
- Spawns only in **brutal** difficulty, on stages 7 and 8 as a mid-stage wave (replaces a regular Tank wave).
- Music: `kane` theme during the fight.
- Defeat: he doesn't react. Just collapses on the third significant hit after his HP zeroes. The fight ENDS the moment he's down.
