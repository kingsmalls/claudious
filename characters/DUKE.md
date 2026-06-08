# DUKE

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **16 distinct animation rows** in this exact order, one anim per row, no skipping, no merging:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `run` (6 frames)
> 4. `jump` (3 frames)
> 5. `atk1` — BOXING JAB (4 frames)
> 6. `atk2` — CROSS (5 frames)
> 7. `atk3` — HOOK + STOMP (6 frames)
> 8. `atk4` — DROPPING OVERHAND (6 frames) — **NEW** combo finisher: worn-out boxer drops his weight into one final looping right (visually distinct from atk3 horizontal hook)
> 9. `heavy` — UPPERCUT LAUNCHER (7 frames)
> 10. `jump_atk` — DIVING ELBOW DROP (4 frames)
> 11. `back_atk` — REAR ELBOW (4 frames)
> 12. `special` — ROLLING THUNDER (12 frames) — **the signature move, must be visually distinct from atk3/atk4**
> 13. `throw` (5 frames)
> 14. `counter` (6 frames)
> 15. `hurt` (3 frames)
> 16. `dodge` (5 frames)
>
> **Total: 86 frames in 16 rows.** If any row is missing, the engine substitutes a fallback that may not match the intended move.

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

### `atk1` — BOXING JAB (4 frames, 12 fps)
**Visual signature:** textbook boxer's lead jab — sharp snap-back is the tell that this is a trained fighter, not a brawler. **Cigarette stays put on the ear** even through the snap. Hair strand falls across the forehead and re-settles each cycle.
- F1: load — front shoulder pulls back 2 px, fist near chin level. Eyes lock forward.
- F2: extend — left fist drives forward ~14 px, body twist minimal (5°), back foot stays planted.
- F3: peak — fist fully extended, knuckles vertical (boxing form), shoulder rolled forward to protect the chin.
- F4: **snap-back — fist retracts 80% sharply** (the boxer detail; not a slow draw-back). Body returns to stance.

### `atk2` — CROSS (5 frames, 11 fps)
**Visual signature:** full-body weight transfer cross — body rotates 45° as the rear fist crosses the centerline. **F4 the mouth tightens 1 px** (the rare focus expression). The hair strand whips with the rotation and settles back on the snap-back.
- F1: hip cocks back, weight shifts to back foot, right (rear) fist near jaw.
- F2: hip drives forward, rear shoulder rotates — torque visibly winding.
- F3: extend — rear fist crosses the center line, reaching ~18 px forward. Front (left) hand stays up at chin height for guard.
- F4: peak — fist fully extended, body rotated 45°, weight on front foot. **Mouth tightens 1 px**.
- F5: snap-back, body unwinds. Hair strand settles back across the forehead.

### `atk3` — HOOK + STOMP (6 frames, 11 fps) — chains into atk4
**Visual signature:** the **STOMP**. Duke transfers power through a hard right-foot stomp on the same frame the hook lands, and the **dust puff at his right foot is unique to Duke** — no other character generates ground dust from a footstrike during a punch.
- F1: load — body coils, front foot lifts 2 px off the ground, left (front) fist at hip height.
- F2: stomp wind-up — right foot drives downward.
- F3: hook arc — left fist swings inward in a horizontal arc as the right foot lands.
- F4: **contact + stomp landing — fist at impact, DUST PUFF at right foot (1–2 brown specks)**.
- F5: follow-through, body tilted 10° forward, fist past the impact line.
- F6: recovery — body unwinds, hair strand falls back. **Chains into atk4 if light pressed.**

### `atk4` — DROPPING OVERHAND (6 frames, 11 fps) — combo finisher
**Visual signature:** Duke drops his entire WEIGHT into one looping overhand right. **F3 the silhouette is unmistakable — body angled 25° forward, right arm at full overhand extension above the shoulder coming DOWN in a vertical comet arc (different from atk3's horizontal hook). F4 the half-grin appears — the cynic's "I shouldn't be enjoying this" tell that he reserves for the finisher. Cigarette stays put through the whole motion.**
- F1: load — body coils backward, weight shifting to the left (good) leg, right fist drawn behind the body at shoulder height. **The bad right knee strains visibly** (the 1-px tilt that says "this is going to cost him").
- F2: wind-up — right arm arcing OVERHEAD now, body rotating, hair strand whipping.
- F3: **DRIVE — right arm at full overhand extension ABOVE the shoulder, body angled 25° forward, weight transferring forward. The vertical fist position is the move's identity — atk3 was horizontal hook, atk4 is overhand**. 4-px brown stomp-dust spray at his right foot as the weight lands.
- F4: **impact — right fist at chest-of-target height (having come DOWN from overhead in a comet arc), body fully forward, HALF-GRIN visible**. Cigarette unmoved.
- F5: follow-through — body bent forward at the waist, fist past the impact line, hair strand falling across the forehead.
- F6: recovery — body straightens slowly, fist coming back, hair settles.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 9 fps)
**Visual signature:** the **strained bad knee** is the tell on F1 — a 1-px tilt that says "this is going to hurt him too." F5 peak shows the half-grin AND the cigarette unmoved AND the fist 16 px above his head. The whole pose is "worn-out man putting his whole body into one shot." Slowest player attack — the load takes time.
- F1: deep crouch — both knees bend, both fists at hip. **The bad right knee is visibly strained (1-px tilt outward)**.
- F2: load — front fist near belly, body coiled like a spring.
- F3: rise begins — knees start straightening, fist starts climbing.
- F4: drive — explosive vertical rise, front fist 16 px above head height.
- F5: peak — body fully extended skyward, fist directly above body line, **HALF-GRIN visible**. **Cigarette stays put**.
- F6: hold — pose held one extra frame for the launcher feel.
- F7: recovery — body lowers back to stance, knees absorbing.

### `jump_atk` — DIVING ELBOW DROP (4 frames, 10 fps)
**Visual signature:** Duke isn't graceful in the air — he DIVES. Body angled forward at 45°, **right elbow cocked overhead with the FOREARM VERTICAL like a spear**, the whole body falling onto the elbow's point. **F3 the impact pose shows the entire body folded behind the descending elbow — head, shoulder, hip, and lead foot all in a diagonal line from the elbow tip to his back foot**. Not a graceful flying kick; a worn-out brawler turning gravity into a weapon. Hair strand whips upward. **Cigarette stays put** even at the apex.
- F1: airborne, right elbow cocked overhead with forearm vertical, body still rising.
- F2: descent begins — body angles 30° forward, elbow leading the drop.
- F3: **peak impact — elbow at chest-of-target height, body 45° forward in a diagonal line from elbow-tip to rear foot**. Hair strand whipped up.
- F4: recovery — body resets, elbow lowering toward landing.

### `back_atk` — REAR ELBOW (4 frames, 12 fps)
- Heavier rear-elbow strike than Rio's — Duke pivots more on the bad knee, so the move loads slow but lands hard.
- F1: wind-up — body turns 30° toward the rear, right elbow lifts to shoulder height. Weight shifts to the left (good) leg.
- F2: drive — elbow drives backward, right hip rotating with it.
- F3: peak — elbow fully extended *behind* him, body twisted 60°, the half-grin briefly appears (1 frame).
- F4: recovery — body unwinds back to stance, weight redistributing.
- **Cigarette stays put** through the rotation.

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

### `throw` (5 frames, 10 fps)
- Heave-and-slam — Duke grabs the collar, heaves the enemy off the ground, slams them down.
- F1: grab — both hands forward at chest height, fistfuls of imagined collar.
- F2: lift — body straightens, enemy hoisted off the ground, Duke's weight on his back foot for leverage.
- F3: spin — body rotates 90°, enemy pivoting overhead.
- F4: slam — body drives the enemy downward, Duke leaning forward.
- F5: recovery — hands drop, body straightens back to stance.
- **Cigarette stays put** through the whole throw.

### `counter` — counter-special (6 frames, 11 fps)
- The free counter-special at full parry meter. A bigger, meaner version of the Rolling Thunder haymaker — body wider, fist heavier.
- F1: load — body torques back further than the special's haymaker, weight on the left leg, right fist drawn behind.
- F2: drive begins — body weight drops forward, right fist arcs downward.
- F3: arc — fist mid-arc, body fully forward, hair strand whipping.
- F4: contact — right fist at impact, **bigger dust puff at his feet** (5–6 brown specks in a half-circle), half-grin at full visibility.
- F5: follow-through — body past impact, fist still extended.
- F6: recovery — body straightens, fist lowering. Cigarette has not moved.

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

Duke's identity in motion is the **dust puff at his stomping right foot + cigarette unmoved + half-grin reserved for finishers**. He's a worn-out boxer — every move costs him visibly.

- `atk1` JAB — sharp snap-back, cigarette unmoved, no dust (efficient)
- `atk2` CROSS — 1-px hair-strand whip across the forehead at peak
- `atk3` HOOK + STOMP — dust puff (1–2 brown specks) at his right foot on impact
- `atk4` DROPPING OVERHAND — bigger dust puff (4 brown specks) at right foot, half-grin appears
- `heavy` UPPERCUT — bad-knee strain visible on F1, half-grin on F5
- `special` ROLLING THUNDER — 3 elbow speedlines (3-px → 4-px → 5-px growing) + dust puff on the haymaker finisher + half-grin

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

