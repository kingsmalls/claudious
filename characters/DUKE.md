# DUKE

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **16 distinct animation rows** in this exact order, one anim per row, no skipping, no merging:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `run` (6 frames)
> 4. `jump` (3 frames)
> 5. `atk1` — OVERHAND LEFT (4 frames) — **lead fist ARCS DOWN from above the shoulder** onto the target's temple, body slips right (not a stiff jab — a looping dirty-boxing lead)
> 6. `atk2` — SOLAR-PLEXUS CROSS (5 frames) — **REAR fist drives forward at GUT HEIGHT**, body coils LOW, **cigarette ash flecks fall for 1 frame** (only frame the cig produces ash)
> 7. `atk3` — OBLIQUE KICK (6 frames) — **left BOOT drives at a DOWNWARD ANGLE into the opponent's LEAD KNEE**, foot pointed down-and-inward, body half-turned (UFC's knee-snapper)
> 8. `atk4` — SOCCER KICK (6 frames) — **full back-swing → LEFT BOOT drives forward at HEAD HEIGHT like a football punt**, body leans back, hair strand whips, dust kicks at supporting boot, HALF-GRIN appears
> 9. `heavy` — UPPERCUT LAUNCHER (7 frames) — **ONE rear fist RISING vertically** from below the knee to above the head, wedding-band-style focus tell
> 10. `jump_atk` — FALLING AXE KICK (4 frames) — **AIRBORNE, LEFT LEG raised VERTICAL ABOVE THE HEAD**, then HEEL drops straight down on the target's skull
> 11. `back_atk` — SPINNING BACKFIST (4 frames) — **body PIVOTS 180°**, back of rear fist WHIPS horizontally at head height, hair-strand comet trail traces the full spin
> 12. `special` — ROLLING THUNDER (12 frames) — three FORWARD elbow strikes (left-right-left, growing speedlines) + a haymaker (multi-phase)
> 13. `throw` — COLLAR-HOIST KNEE-SLAM (5 frames) — collar grab → hoist chest-high → **LEFT KNEE DRIVES INTO ENEMY GUT (cinematic mid-throw beat)** → toss → recover
> 14. `counter` — LIVER SHOT KO (6 frames) — **body CROUCHED low**, rear fist drives FORWARD at HIP HEIGHT (the only attack below chest level)
> 15. `hurt` (3 frames)
> 16. `dodge` (5 frames)
>
> **Total: 86 frames in 16 rows.** If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Duke's moveset is built around **cinematic dirty-boxing flair**. Every attack has both a unique silhouette AND a unique signature beat (cigarette ash on the gut-cross, the half-grin on the soccer kick, the hair-strand comet on the backfist, the mid-throw knee, the wedding-band-style tell on the launcher). If two attacks share a silhouette OR share a signature beat, redraw one.
>
> | Attack | Body axis | Striking limb | Direction | Unique signature beat |
> |---|---|---|---|---|
> | `atk1` overhand left | Vertical, slipped right 10° | LEAD (left) fist | Diagonal DOWN from above the shoulder onto target temple | Fist arc comes from ABOVE shoulder height (not horizontal) + slip-right body tell |
> | `atk2` solar-plexus cross | Body coiled LOW 6 px below idle | REAR (right) fist | Horizontal forward at GUT HEIGHT (not face) | Lands at SOLAR PLEXUS not face + 1-frame CIGARETTE ASH FLECK (only frame in the game the cig produces ash) |
> | `atk3` oblique kick | Half-turned 30° sideways | LEFT BOOT (sole down-inward) | Diagonal DOWN-FORWARD into knee height | Boot is angled DOWN AND INWARD (toes drop, sole facing the target's lead knee) — only diagonal-down kick |
> | `atk4` soccer kick | Body leans BACK 20° for full back-swing | LEFT BOOT | Rising arc up to HEAD height (football punt) | Full back-swing chamber + boot at HEAD height with toes pointed (the only kick that goes high) + HALF-GRIN on impact |
> | `heavy` uppercut | Vertical, extending upward | ONE rear fist | Ascending vertical | Single rising fist from below the knee + bad-knee strain on F1 + half-grin on F5 |
> | `jump_atk` axe kick | AIRBORNE, body vertical | LEFT HEEL | Descending vertical from ABOVE the head | Body airborne with one leg pointed straight UP at peak then HEEL drops vertically — the only inverted-leg silhouette |
> | `back_atk` spinning backfist | Pivoting 180° through the spin | Back of REAR fist | Horizontal whip at head height | Body fully ROTATING (visible spin frames) + hair-strand comet streak traces the rotation |
> | `special` rolling thunder | Multi-phase, grounded, facing forward | THREE forward elbows + haymaker | Forward, alternating sides | Three forearm strikes left-right-left with growing speedlines (3-px → 4-px → 5-px) + haymaker finisher with dust + half-grin |
> | `throw` knee-slam | Body upright → hoisting → driving knee | Both hands grip + LEFT KNEE | Lift + knee strike + toss | Three-beat sequence with a visible KNEE DRIVE into the enemy's gut in the middle (only throw with an intermediate strike) |
> | `counter` liver shot | CROUCHED LOW, knees deep past 90° | Rear fist | Horizontal forward at HIP height | Body lower than any other pose; fist at LIVER HEIGHT — only below-the-belt attack + half-grin at full visibility |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 is a DIAGONAL DOWN arc onto the temple (fist starts above the shoulder, ends at face); atk2 is a HORIZONTAL forward drive at GUT HEIGHT with the body coiled low. Different angles, different target heights, different body postures. If both look like the same straight punch, redraw.
> - **atk3 vs atk4:** atk3 is a DOWN-AND-INWARD chop kick at KNEE HEIGHT (sole of the boot pointed at a knee joint); atk4 is a RISING ARC to HEAD HEIGHT with toes pointed (football punt). One kick goes LOW with the boot angled down; the other goes HIGH with the toes leading. Opposite heights and opposite foot orientations.
> - **atk4 vs heavy:** atk4 = leg rising to head height (boot leads); heavy = fist rising to overhead (single fist leads). Both go UP but atk4 is leg-led, heavy is fist-led. The kicking leg in atk4 must clearly be the weapon — boot above hip height, fully extended.
> - **jump_atk vs atk4:** both involve a high leg. jump_atk is AIRBORNE with the leg pointed STRAIGHT UP above the head then dropping HEEL-FIRST. atk4 is GROUNDED with the leg arcing FORWARD AND UP to head height with TOES leading. Different orientations (vertical heel-down vs horizontal toes-forward) and different grounding (airborne vs planted).
> - **back_atk vs special:** back_atk = body ROTATING through a 180° spin (visible mid-spin frames). special = body GROUNDED and FORWARD-FACING throwing three elbows in place. If back_atk doesn't show the spin clearly, redraw with a 90°-pivoted mid-frame.
> - **heavy vs counter:** heavy goes UP (single fist ascending from below knee to overhead). counter goes FORWARD AT HIP HEIGHT with body crouched. Opposite directions, opposite body heights.
> - **Bad-knee tell:** every kick (atk3, atk4, jump_atk) uses the LEFT (good) leg as the weapon. The right (bad) knee is the supporting leg and visibly strains under load (1-px outward tilt).
> - **Signature-beat rule:** atk2 produces cigarette ash for 1 frame. atk4 reveals the half-grin. back_atk leaves the hair-strand comet streak. throw shows the knee mid-air. These tells exist nowhere else — they are how each move is read from across the screen. If the tell is missing, the move isn't reading.

## Physical

- **Age:** 31
- **Height/build:** 5'10", solid, semi-pro boxer's frame. Heavier than Rio, leaner than Atlas. Carries himself slightly hunched — old knee injury changed his posture. **Right knee favors a slight bend even when standing.**
- **Ethnicity:** White; weathered, slightly tan from outdoor work.
- **Body language:** Loose, low-energy. Stands flat-footed (not bouncing like Rio). Doesn't raise his guard high — he absorbs hits and waits for a tell.
- **Face:** Squared jaw with three to four days of stubble. Slightly broken nose (small bump on the bridge). Heavy brow casting shadow over the eyes. Mouth often slightly parted, like he's about to say something cynical and then doesn't.

## Hair

- **Style:** Messy, dark blonde, uneven. Roughly 2–3 inches at the longest, no defined cut — like he hasn't been to a barber in months. **A wayward strand falls across his forehead** on the camera-facing side; it must be there in every frame.
- **Movement:** Hair shifts with hard motion but doesn't bounce; it's heavier (greasier?) than Rio's.

## Costume (head to feet)

1. **CIGARETTE:** **An unlit, off-white cigarette tucked behind ONE ear** (camera-side). 1-pixel wide, 4-pixel long, with a brown filter tip. **Never smoked, never moves, never falls.** Visible in every single frame including KO and damage poses.
2. **T-shirt:** Stained off-white/cream cotton, fitted around the chest and shoulders, slightly looser at the waist. **Two visible discolorations** (slight grey-yellow patches at the collar and one rib) suggesting wear and stains. V-neck or crew, plain.
3. **Denim cut-off jacket:** **Sleeveless** — the sleeves were cut off jaggedly, leaving raw frayed edges at the shoulders. Faded medium blue (washed denim, not new). Open in front, no buttons. **Ragged hem** at the bottom — 2-pixel jagged line. Two breast pockets, slightly worn.
4. **Belt:** Brown leather, plain buckle (square, brushed metal). Visible at the waistline.
5. **Jeans:** Dark indigo, well-worn. Not skinny — straight cut. **One visible knee tear** on the right knee (the bad one) — not gaping, just a 4-pixel slash.
6. **Boots:** Beat-up black combat boots (laced halfway up, then loose). Toes scuffed/scratched. Sole slightly worn unevenly (favors the right).

## Palette (hex)

```
skin (light)        #d4a888
skin (shadow)       #9a785a
skin (deep shadow)  #6e503a
hair (highlight)    #a08c4a
hair (shadow)       #6e5e2c
stubble             #3a2a1c
shirt (light)       #cfc8b8
shirt (shadow)      #9b9482
shirt stains        #b8b09a
jacket (mid)        #5a6678
jacket (shadow)     #404a5c
jacket (highlight)  #7886a0
jacket (frayed edge) #2a3040
jeans               #2a2e3a
jeans shadow        #191c26
boot                #161618
boot sole           #08080a
belt                #4a3020
belt buckle         #8a8a8a
cigarette body      #e8e4d2
cigarette tip       #7a4a26
eye whites          #f0f0f0
```

## Personality cues that should show in poses

- **Tired posture.** Never fully erect. Shoulders slightly forward.
- **Hands low.** He guards with his elbows, not his fists.
- **Half-grin on heavy hits.** A pinched expression on the Rolling Thunder haymaker — like he's enjoying it despite himself.
- **The cigarette never moves.** Even during KO. It's the joke.

## Animations (per slot — pose + key pose details)

### `idle` (4 frames, loops, 6 fps)
- F1: weight settled on the left leg (the good one), right leg bent 10° and slightly forward — bad knee never fully loaded. Hands at lower-belly height, loosely fisted (not raised — he guards with elbows).
- F2: subtle weight shift, shoulders rise 1–2 px on inhale.
- F3: weight back on left, mirror of F1.
- F4: shoulders settle 1 px down on exhale, head dips 1 px.
- **Cigarette** behind camera-side ear, never moves across the cycle.
- **Wayward forehead strand** falls across the camera-side eye.
- Mouth slightly parted, eyes half-lidded — the tired look is part of idle.

### `walk` (6 frames, 7 fps) — **must read clearly as LOCOMOTION, never an attack**
- 6-frame limping stride cycle that LOOPS SEAMLESSLY (F6 blends back into F1). **Left leg strides cleanly; right leg drags slightly** — the limp.
- F1 = LEFT leg forward (clean stride) + RIGHT arm forward swing (opposite-side arm) at hip height.
- F2 = passing position (feet roughly under body, arms at sides).
- F3 = RIGHT leg forward (shorter, dragged stride) + LEFT arm forward swing.
- F4 = passing position.
- F5 = LEFT leg forward again (mirror of F1).
- F6 = passing position — blends straight back into F1.
- **Both arms swing in a small relaxed arc AT THE SIDES** (economic ROM, but still side-swinging). Fists loosely closed at hip level.
- Body leans 5° forward, head bobs 1 px on each strike.
- **Cigarette stays put.** Hair strand hangs forward, sways 1 px on each strike.
- **NEVER**: arms reaching forward past the body, fists extended like a jab, a planted stomp-foot pose on the final frame, body coiled like a wind-up. Walk is the tired man traveling — not the boxer winding up.

### `run` (6 frames, 11 fps) — locomotion, NOT a punch chain
- 6-frame run cycle, looping seamlessly (F6 blends into F1).
- Body forward 10°, longer strides than walk but the right-leg stride is still 1–2 px shorter than the left's (limp still visible).
- F1, F4: foot strikes (alternating). F2–F3, F5–F6: airborne / passing phases.
- **Arms PUMP up and down at the sides** like a boxer's road-work — elbows bent, fists loosely closed at hip-to-chest height. Pump is tired but rhythmic.
- **Arms NEVER extend forward past the body.** No jab pose, no grab pose, no overhand wind-up.
- Jacket flares open at the shoulders behind him — the cut-off frayed edges flap visibly.
- Hair flops on each back-swing — wayward strand whips up off the forehead briefly.
- **Frames 3 and 6:** 3-px horizontal speedlines behind each heel.
- **Cigarette stays put** even at this speed — it's the running gag.
- **NEVER**: a frame where his fist reaches forward at chest height (reads as Rolling Thunder elbow), a planted stomp pose (reads as atk3 stomp), or an overhand arc (reads as atk4).

### `jump` (3 frames, 8 fps — non-looping)
- F1: deep crouch, right (bad) knee bent shallower than left — he loads with the left leg primarily. Both fists drop to hip level.
- F2: airborne — body slightly tucked, **left leg leads**, right leg trails. Jacket flares open showing the t-shirt underneath.
- F3: landing — touches down on the left leg first, right foot follows half a frame later. Body absorbs into a half-crouch.
- **Cigarette stays put.** Hair strand whips upward at the apex.

### `atk1` — OVERHAND LEFT (4 frames, 12 fps)
**Visual signature:** Duke's dirty-boxing lead — not a stiff jab, but a **looping OVERHAND LEFT that arcs DOWNWARD from above the shoulder onto the target's TEMPLE**. The fist starts at chin height, swings up and OVER the shoulder line, then drops in a 30° diagonal arc onto the imagined target's head. Body SLIPS to the right 10° at impact (defensive boxing layering — the slip IS the move's tell). Hair strand whips with the slip. The fist arc comes from ABOVE the shoulder, which makes the silhouette read instantly different from atk2's gut-cross.
- F1: load — left shoulder rises, left fist swings up past the chin to shoulder-height, body weight shifting to front foot. Hair strand whips up off the forehead.
- F2: arc — left fist now ABOVE the left shoulder, body starting to slip right 5°, arm arcing into the diagonal-down path.
- F3: **peak — left fist DROPPING at a 30° diagonal toward the imagined target's TEMPLE, body slipped right 10°, rear hand stays up at chin for guard. Hair strand fully whipped across the forehead. 1-px white impact spark at the fist**. Cigarette unmoved.
- F4: snap-back — fist retracts sharply, body unwinds back to stance, slip resolves. Hair strand settles.

### `atk2` — SOLAR-PLEXUS CROSS (5 frames, 11 fps)
**Visual signature:** Duke's mid-line gut-cross — **the body COILS LOW (drops 6 px from idle) on the wind-up, then the rear fist DRIVES FORWARD AT GUT HEIGHT** (solar-plexus, not face). Different target altitude from any other punch. **The signature beat is the CIGARETTE ASH** — F4 a 2-pixel cluster of grey ash flecks falls from the cig behind his ear (the only frame in the entire game where the cigarette produces ash; the cig itself stays put). The mouth tightens 1 px on the focus. Hair strand whips with the rotation.
- F1: cock — hip and rear shoulder pull back, rear fist drops to hip level, body starts coiling LOW (knees bending 2 px deeper than idle).
- F2: coiled — body 4 px lower than idle, knees fully bent into the load, rear shoulder fully drawn back. Mouth begins to tighten.
- F3: drive — body uncoils with weight transferring to front foot, rear fist starting forward at GUT-HEIGHT line (not face height). Body angle dropped 6 px from idle.
- F4: **peak — body still LOW with knees bent, rear fist FULLY EXTENDED FORWARD at SOLAR-PLEXUS HEIGHT (~18 px past the body, ~32 px above floor — gut level, well below the chin), body rotated 45° with the hip-drive, front hand at chin for guard. Mouth tightened 1 px. CIGARETTE ASH FLECKS — 2 small grey pixels falling from behind the ear (1 frame only, only frame in the whole game)**.
- F5: snap-back — fist retracts, body uncoils and rises back to idle height, hair strand settles.

### `atk3` — OBLIQUE KICK (6 frames, 11 fps) — chains into atk4
**Visual signature:** UFC's knee-snapping low kick — **LEFT BOOT drives at a DOWN-AND-INWARD angle into the opponent's LEAD KNEE**. Body half-turns 30° sideways, left leg extends forward but the BOOT is angled with toes pointed DOWN and the sole facing the target's knee joint (not flat-forward like a push kick, not parallel like a roundhouse). The kicking-foot orientation IS the silhouette — boot pointed at a knee. Brutal, efficient, no flair. Front (left) arm extends FORWARD across the body for balance during the kick. Cigarette unmoved.
- F1: load — body steps slightly sideways with the left foot, half-turning 15°, left knee starting to lift. Front arm rising for balance.
- F2: chamber — left knee at hip height, shin folded down with the BOOT TURNED so the sole faces forward-and-down. Body half-turned 30°, supporting right leg planted.
- F3: drive — left leg starting to extend at a downward-forward angle, foot leading sole-first toward the imagined knee joint.
- F4: **peak — LEFT LEG fully extended at a 30° DOWNWARD-FORWARD angle, BOOT SOLE facing the target's lead knee (~24 px past the body and ~24 px above the floor — much lower than head, distinctly aimed at knee height). Body half-turned 30°, front (left) arm extended forward across the body for balance. 1-px white impact spark at the boot toe**. Hair strand whips.
- F5: follow-through — leg past the impact line, body settling, balance arm returning.
- F6: recovery — leg retracts, body squares up to stance. **Chains into atk4 if light pressed.**

### `atk4` — SOCCER KICK (6 frames, 11 fps) — combo finisher
**Visual signature:** Duke's cinematic punt — full football-kicker mechanic. **F2 he takes a deep BACK-SWING with the left leg drawing fully behind him at thigh height** (the wind-up silhouette is one-of-a-kind). **F4 the LEFT BOOT drives FORWARD AND UP in a long rising arc to HEAD HEIGHT, toes pointed and leading**, body leaned back 20° for the counterweight, both arms flared wide. Hair strand whips, dust kicks at supporting boot, **HALF-GRIN visible at full intensity** (the cynical "I shouldn't enjoy this" tell). The high-arc + toes-leading silhouette must NOT be confused with atk3's down-and-inward chop kick — opposite trajectories.
- F1: plant — right foot plants firmly as the support, body weight transferring fully to right leg. Left knee lifting forward briefly to telegraph the kick.
- F2: **BACK-SWING — left leg drawn FULLY BEHIND the body at thigh height (left foot raised 30 px behind him), body leaning forward to counterweight the leg's rear position, arms flared. This is the football-kicker chamber, unique silhouette**. Bad right knee strains visibly with the supporting load (1-px outward tilt).
- F3: drive — left leg swings forward through the kick path, body rotation pulling it through, hips driving forward.
- F4: **peak impact — LEFT BOOT at HEAD HEIGHT (~40 px above the floor), TOES POINTED forward leading the strike, leg fully extended in a long forward-and-up arc, body LEANED BACK 20° for counterbalance, both arms flared wide. HALF-GRIN at full visibility. 4-px dust puff at the supporting right boot (the punt-through impact). Hair strand fully whipped backward**. Cigarette unmoved.
- F5: follow-through — left leg continues past the impact line, body fully rotated through the kick, foot still high.
- F6: recovery — left leg drops forward to plant, body squaring up, half-grin fading. Hair settles.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 9 fps)
**Visual signature:** the **strained bad knee** is the tell on F1 — a 1-px tilt that says "this is going to hurt him too." F5 peak shows the half-grin AND the cigarette unmoved AND the fist 16 px above his head. The whole pose is "worn-out man putting his whole body into one shot." Slowest player attack — the load takes time.
- F1: deep crouch — both knees bend, both fists at hip. **The bad right knee is visibly strained (1-px tilt outward)**.
- F2: load — front fist near belly, body coiled like a spring.
- F3: rise begins — knees start straightening, fist starts climbing.
- F4: drive — explosive vertical rise, front fist 16 px above head height.
- F5: peak — body fully extended skyward, fist directly above body line, **HALF-GRIN visible**. **Cigarette stays put**.
- F6: hold — pose held one extra frame for the launcher feel.
- F7: recovery — body lowers back to stance, knees absorbing.

### `jump_atk` — FALLING AXE KICK (4 frames, 10 fps)
**Visual signature:** the most cinematic frame Duke ever produces. **At apex, body airborne and FULLY VERTICAL, LEFT LEG pointed STRAIGHT UP ABOVE THE HEAD** (the inverted-leg silhouette — no other Duke move has the leg above the head), then the **HEEL DROPS STRAIGHT DOWN like a falling axe blade** on the imagined target's skull. Hair strand whips upward at apex. Cigarette stays put through the entire arc — even inverted, the cig stays.
- F1: launch — body airborne and rising, left knee starting to drive up toward the chest. Both fists tucked at chest. Hair beginning to whip.
- F2: apex chamber — body airborne and vertical, **LEFT LEG raising fully overhead with the foot pointed STRAIGHT UP above the head** (left thigh past vertical, shin vertical, heel above the skull). Right leg hanging straight down for balance. Hair fully whipped up. Arms flared for balance.
- F3: **DROP — heel driving DOWNWARD in a vertical line, left leg now pointed STRAIGHT DOWN through the imagined target's head, body still airborne and vertical, hair strand fully whipped, 1-px white impact spark at the heel. Half-grin briefly visible (1 frame)**.
- F4: landing — left foot touches down first into a half-crouch absorbing the drop, right leg planting beside it. Hair settles.

### `back_atk` — SPINNING BACKFIST (4 frames, 12 fps)
**Visual signature:** Duke pivots through a full 180° spin, and the **BACK of his rear fist WHIPS around horizontally at head height** — a backfist, not an elbow. Hair strand traces the rotation as a 6-px **brown comet streak** (the rotation tell unique to this move). Body visibly rotates across the four frames: F1 facing forward, F2 mid-spin (profile), F3 facing AWAY then snapping back, F4 finished forward. Cigarette stays put even through the spin.
- F1: load — front foot pivots 60°, body starting to rotate, rear arm swinging out from the body to chamber the backfist. Hair strand starts whipping.
- F2: mid-spin — body now in profile to the camera (90° rotation), rear arm fully extended out behind, the BACK OF THE FIST starting to whip around horizontally at head height. **Hair strand traces a 6-px brown comet streak** behind the body.
- F3: **peak — body rotated 180° (briefly past the spin into a backwards-facing then snapping forward), BACK OF REAR FIST extended horizontally at head height (~22 px past the body), elbow nearly straight. Hair-strand comet streak fully visible (6 px). Half-grin briefly visible. 1-px white impact spark at the back of the fist**.
- F4: recovery — body finishes the rotation back to forward-facing, rear arm retracts to stance. Hair settles. **Cigarette stays put** through the entire 180° spin.

### `special` — ROLLING THUNDER (12 frames, 11 fps)
The signature.
**Visual signature:** **THREE FORWARD ELBOWS** (left, right, left) each with its own speedline (3 px → 4 px → 5 px, growing), body torquing further with each one, then a haymaker that lands with the **half-grin at full visibility** AND a dust puff at the feet. Duke's elbows are HIS move — no other player uses elbows. **Cigarette stays put through all 12 frames** (this is the gag — even on the haymaker, the cigarette is still behind his ear).
- F1: stance — body coils, hands at chin, weight loading on the left leg.
- F2: **first elbow (left)** — left elbow drives forward 8 px, body rotates 15°. 3-px speedline streak behind the elbow.
- F3: first elbow continues into the next windup, right arm drawing back.
- F4: **second elbow (right)** — right elbow drives forward 10 px, body rotated 30° the other way. 4-px speedline.
- F5: second elbow follow-through, body resetting toward forward.
- F6: **third elbow (left)** — left elbow again, deeper drive 12 px, body lower (knees bend more), 5-px speedline. Hair strand whipping with each elbow.
- F7: third elbow follow-through, body torquing far back to load the haymaker.
- F8: haymaker load — body torques fully back, right fist drawn way behind the body. Mouth tightens.
- F9: drive — body weight drops forward, right fist arcs in a downward overhand path.
- F10: contact — right fist at impact point, body weight forward, **dust puff at his feet** (2–3 brown pixels), the **half-grin is at full visibility** (the one frame Duke looks alive).
- F11: hold — pose locked one extra frame for the kill-shot feel.
- F12: recovery — body straightens slightly, fist lowering. Hair strand falls back into place.
- **Cigarette stays put** through all 12 frames.

### `throw` — COLLAR-HOIST KNEE-SLAM (5 frames, 10 fps)
**Visual signature:** three-beat throw with a **cinematic KNEE-DRIVE in the middle** (the only throw in the cast with an intermediate strike). F1 grab, F2 hoist, F3 LEFT KNEE drives upward into the imagined enemy's gut (knee at hip height with the enemy bent over it), F4 hurl forward, F5 recovery. The knee-mid-throw beat is the signature — no other character interrupts a throw with a strike. Cigarette stays put through all 5 frames.
- F1: grab — both hands forward at chest height, fistfuls of imagined collar, body slightly forward to take the enemy's weight.
- F2: hoist — body straightens, enemy lifted to chest height, Duke's weight on the right (bad) leg as the LEFT leg starts chambering for the knee strike.
- F3: **KNEE STRIKE — LEFT KNEE drives upward at hip height with full thigh-vertical chamber, the imagined enemy bent over the rising knee. Body angled 10° forward into the strike. Both hands still gripping the collar holding the enemy in place over the knee. 1-px white impact spark at the knee. Half-grin briefly visible — Duke enjoys this one**.
- F4: toss — left leg drops back to plant, body uncoils forward, both arms drive the enemy forward and away.
- F5: recovery — hands drop, body straightens back to stance. Hair strand falls back. **Cigarette stays put** through the whole three-beat throw.

### `counter` — LIVER SHOT KO (6 frames, 11 fps)
**Visual signature:** Duke's veteran-boxer trick. **The ONLY attack in his kit aimed BELOW chest level**. Body drops into a deep crouch (lower than any other pose Duke takes — knees bent past 90°, weight slammed forward onto the front foot), then the rear fist drives FORWARD HORIZONTALLY at LIVER HEIGHT (just above the belt, well below the head). The body posture is unmistakable — Duke is the SHORTEST in this frame, fist horizontal at hip height, not arcing up or down. F4 the half-grin is at full visibility — the cynic enjoying the dirty win. Cigarette stays put through the whole motion. **Must NOT show the fist above chest height and must NOT show an arc — this is a level, straight, low body shot.**
- F1: load — body starts dropping, knees bending past their idle angle, weight transferring to front foot. Rear fist drops to hip level (already low, telegraphing the body shot).
- F2: deeper crouch — knees fully bent past 90°, body lowered 6–8 px from idle, rear shoulder pulling back to load the fist.
- F3: **drive — body at FULL CROUCH (the shortest Duke gets), weight slammed forward, rear fist starting to drive forward HORIZONTALLY at hip/liver height**. Eyes lock forward on the target's body, not the head.
- F4: **peak impact — body still crouched low, rear fist FULLY EXTENDED forward at HIP HEIGHT (~14 px past the body, ~28 px above the floor — well below chest), front hand still raised at chin for guard. HALF-GRIN at full visibility — the cynic's smile. 1-px white impact spark at fist height (low, not high)**. Hair strand falls across the forehead.
- F5: follow-through — body still crouched, fist holding the extension one extra frame for the kill-shot weight, weight transferring through the punch.
- F6: recovery — body slowly rises back toward idle, fist retracting, knees straightening. Hair strand settles. **Cigarette has not moved.**

### `hurt` (3 frames, 12 fps)
- F1: impact — head whips back 8°, torso folds at the waist, both hands fly outward briefly.
- F2: recoil — torso bent forward, body absorbing the hit, knees bending.
- F3: recovery — body straightening back toward stance.
- **Cigarette stays in place. This is the joke.** Even on KO frames he's planning to draw later, the cigarette stays.

### `dodge` — BACKWARD STEP (5 frames, 12 fps)
- Duke doesn't roll — the bad knee won't allow it. He **steps backward fast** with one hand raised.
- F1: weight shifts hard onto the left leg, right foot lifts.
- F2: push-off — left leg drives backward, body slides 4 px back, right hand raises to chin level.
- F3: airborne briefly — both feet off ground for one frame, body sliding back.
- F4: landing — right foot plants behind him (slightly bent for the bad knee), body absorbs.
- F5: settled — back into stance, **right hand still raised in a "stop" gesture** (the read: he's daring you to come at him again).
- **Cigarette stays put** through the dodge.

## DO NOT include for Duke

- Glowing energy / elemental effects of any kind
- Clean / pressed clothes — everything is worn-in
- Boxing gloves — he uses his bare/wrapped hands now
- Athletic / spring-loaded movement — he's tired and worn
- A full beard — it's stubble (3–4 days)
- The cigarette LIT or removed — never lit, never moves

## Visual VFX summary

Duke's identity in motion is **dirty cinematic boxing** — every move carries a signature beat (cigarette ash, hair-strand comet, half-grin, inverted leg, mid-throw knee). He's a worn-out boxer with a bag of veteran tricks. **Every attack occupies a distinct silhouette quadrant AND a distinct signature beat** (see the SILHOUETTE DIFFERENTIATION table near the top).

- `atk1` OVERHAND LEFT — lead fist arcs DOWN from above the shoulder onto the temple, body slips right 10°, hair-strand whips (the looping dirty-boxer lead, not a stiff jab)
- `atk2` SOLAR-PLEXUS CROSS — body coils LOW (6 px below idle), rear fist drives forward at GUT HEIGHT, **1-frame CIGARETTE ASH FLECKS** (the only frame in the game the cig produces ash)
- `atk3` OBLIQUE KICK — LEFT BOOT angled DOWN-AND-INWARD at opponent's lead KNEE (sole facing knee joint), body half-turned 30°, front arm forward for balance (UFC's knee-snapper)
- `atk4` SOCCER KICK — full BACK-SWING then LEFT BOOT punts forward at HEAD HEIGHT with TOES leading, body leans back 20°, dust puff at supporting boot, **HALF-GRIN at full intensity**
- `heavy` UPPERCUT — ONE rear fist RISING vertically from below the knee to overhead, bad-knee strain visible on F1, half-grin on F5
- `jump_atk` FALLING AXE KICK — AIRBORNE, **LEFT LEG pointed STRAIGHT UP ABOVE THE HEAD** at apex, then HEEL drops vertically (the only inverted-leg silhouette)
- `back_atk` SPINNING BACKFIST — body PIVOTS 180°, back of rear fist whips at head height, **6-px hair-strand BROWN COMET STREAK** traces the rotation
- `special` ROLLING THUNDER — three FORWARD elbow strikes (left-right-left) with growing speedlines (3-px → 4-px → 5-px) + a haymaker finisher with dust puff + half-grin
- `throw` COLLAR-HOIST KNEE-SLAM — three-beat: grab → hoist → **LEFT KNEE DRIVES INTO ENEMY GUT (mid-throw cinematic beat)** → toss (the only throw with an intermediate strike)
- `counter` LIVER SHOT KO — body CROUCHED low (shortest pose Duke takes), rear fist drives forward at HIP HEIGHT — the only attack below chest level + half-grin at full visibility

**Kick discipline note (every kick uses the LEFT — good — leg).** Duke's right knee is bad; he never kicks with the right leg. atk3, atk4, jump_atk, and the throw's knee-beat all use the LEFT leg as the weapon. The right (bad) knee is either the supporting leg under load (atk3, atk4, throw) or trailing as counterweight (jump_atk), and it visibly strains when it carries load.

**Signature-beat dictionary (read from across the screen).** The following tells appear EXACTLY ONCE in Duke's whole sheet — they are how each move is identified:
- Cigarette ash flecks (1 frame, F4) — atk2 SOLAR-PLEXUS CROSS only
- Hair-strand brown comet streak (6 px) — back_atk SPINNING BACKFIST only
- Leg pointed STRAIGHT UP above the head — jump_atk FALLING AXE KICK only
- Mid-attack knee strike — throw KNEE-SLAM only
- Body crouched LOWER than any other pose — counter LIVER SHOT only
- Body slipped RIGHT 10° — atk1 OVERHAND LEFT only
- Full back-swing chamber (leg drawn 30 px behind) — atk4 SOCCER KICK only

**Hurt / flinch:** F1 body folds, jaw clenches. F2 cigarette wobbles 1 px but stays on the ear (the gag). 1-px white impact spark at the contact point. F3 body returns to stance, hair strand falls across the forehead.

**Dead:** Falls backward. Cigarette finally falls off the ear on F4 — first time it moves in the whole game.

## Sheet specs (same for all three characters)

### Color discipline
- Each body part stays within its 3-color palette (mid, shadow, highlight). Don't blend pixels between palettes.
- Identity-item colors are reserved — bandana yellow, wedding-band silver, cigarette cream are unique to that character. Don't reuse them on other parts.

### Outline
- 1-pixel hard outline at the silhouette boundary, in the deepest shadow color of that body part (not pure black).
- No anti-aliasing along the outline.

### Lighting direction
- Light comes from the upper-front-right of the character (the camera-side, slightly above).
- Highlights along the upper-front edges, shadows along the lower-back edges.

### Reference quality target
- Streets of Rage 4 character pixel quality (not the SoR4 final art — they're 2D-vector — but the same readability and silhouette discipline).
- Fight'N Rage character density and hand-poses.
- Castle Crashers tier of expressive poses (a bit more cartoon-readable than realistic).

### Frame counts (Duke total: 80)

| Slot | Frames |
|---|---:|
| idle | 4 |
| walk | 6 |
| run | 6 |
| jump | 3 |
| atk1 | 4 |
| atk2 | 5 |
| atk3 | 6 |
| heavy | 7 |
| jump_atk | 4 |
| back_atk | 4 |
| special | 12 |
| throw | 5 |
| counter | 6 |
| hurt | 3 |
| dodge | 5 |

### Sheet layout
- Uniform grid, **8 columns × 10 rows = 80 cells**.
- Each cell: **64 wide × 96 tall**.
- Background: solid magenta `#ff00ff` for keying, OR transparent PNG.
- Anchor each frame's character at **bottom-center** of the cell.

### Final integration step

When this sheet lands:
1. Save to project root as `duke.png`.
2. Open `sprite_slicer.html`, load the PNG, click through to label all 15 anim slots.
3. Export `duke_atlas.json` next to the PNG.
4. `python3 pipeline.py validate-atlas duke_atlas.json`.
5. Reload `the_block.html`. The atlas loader picks it up automatically — Duke switches from procedural to sprite rendering. Any anim slot that's missing falls back to procedural for that animation only, so partial atlases are fine.

