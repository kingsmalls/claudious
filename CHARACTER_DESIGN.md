# CHARACTER DESIGN REFERENCE

The exhaustive visual brief. Hand this to the artist (or the AI generator) along with the prompts in `SPRITE_PROMPTS.md`. Anything missing from this doc is undocumented — fill it in, don't invent it.

For each character: physical specs, costume layers, identity items, palette, per-animation poses, per-special-move beat sheet, and a "do NOT include" list to keep generators on-spec.

---
# RIO

## Physical

- **Age:** 24
- **Height/build:** 5'5", lean athletic — boxer's frame. Visible deltoids and forearms; not bulky, not slight. Tapered waist. Knees slightly bent in idle (fighting stance).
- **Ethnicity:** Black; deep brown skin.
- **Body language:** Centered, low. Stays on the balls of her feet. Hands up by default — guard never fully drops.
- **Face:** Strong jaw, broad cheekbones. Dark eyebrows, deep brown eyes. Straight nose, full lips. Resting expression is calm/focused, not angry. **The smile only appears on a clean combo finisher** — that's the one moment her face changes.

## Hair

- **Style:** Full afro, dark brown to black, ~3–4 inches deep. Round, soft silhouette around the head; not picked super-tall, not pressed down — natural shape. A few strands fall forward over the forehead.
- **Movement:** The afro **bounces visibly with hard motion** — compresses on landings, rises with the Sunset Spin, lifts at the apex of jumps. Springy, not flowing.

## Costume (head to feet)

1. **Earring:** Single small gold hoop (≈1px sprite), camera-side ear only.
2. **Neck:** Bare. No jewelry.
3. **Tank top:** Black ribbed, snug. Visible only where the cropped jacket leaves it exposed (lower torso strip and upper chest collar).
4. **Bomber jacket:** Cropped (ends at lower ribs). Olive/sage green, faded. Two slash pockets at hip line. Knit collar, cuffs, and hem in slightly darker olive. Zipper open about a third of the way down. **Sleeves end mid-forearm**, leaving wrists exposed.
5. **Hand wraps:** Off-white/cream cotton, wrapped 4 times around the knuckles and back of hand. Clean white, slightly worn at the edges. Knuckles exposed (no full glove). Both wrists wrapped.
6. **YELLOW BANDANA:** **Bright marigold yellow, tied around the LEFT wrist over the hand wraps.** A small knot tail (2 pixels) hangs off. The bandana is the single most important visual element — it must be visible in every frame, on the camera side of her body when possible. It TRAILS through fast motion (jabs, the spin, the uppercut, the dodge roll).
7. **Pants:** Slim-cut cargo pants, near-black charcoal. Two cargo pockets on the thighs, low-profile (not bulky). Tapered to the ankle.
8. **Boots:** Ankle-high lace-up boxing boots, black with white soles. Laces black. Toe slightly worn.

## Palette (hex)

```
skin (light)        #8a5235
skin (shadow)       #6b3f2a
hair (afro)         #1a1410
hair (highlight)    #2a201a
jacket (mid)        #7d8d4f
jacket (shadow)     #5a6b3a
jacket (highlight)  #9bab6a
tank black          #0a0a10
pants               #1a1a22
pants shadow        #0e0e15
boot                #0a0a10
boot sole           #d8d8c0
hand wraps          #dcd6c4
hand wraps shadow   #a8a294
BANDANA highlight   #ffd76a
BANDANA mid         #e8c04a
BANDANA shadow      #b89426
earring             #e8c04a
eye whites          #ffffff
```

## Personality cues that should show in poses

- **Calm head, busy hands.** In idle, her face is neutral but her fists are always ready.
- **Economy of motion.** No wasted limbs. Every frame's silhouette reads as deliberate.
- **The SMILE.** Reserved for the third hit of a combo (atk3) and the Sunset Spin's uppercut finisher. One frame, brief, almost imperceptible — but there.
- **Defensive footwork.** Walks on the balls of her feet, never flat-footed.

## Animations (per slot — pose + key pose details)

### `idle` (4 frames, loops, 6 fps)
- Frames 1, 3: bounce-down — knees bent slightly, weight on the front foot, hands at chin level.
- Frames 2, 4: bounce-up — slight rise, afro lifts 1px.
- Bandana visible on left wrist throughout, hanging slightly.
- Eyes scanning forward. Mouth neutral.

### `walk` (6 frames, 8 fps)
- 6-frame stride cycle. Forward foot strikes on frames 1 and 4.
- Front arm swings opposite to leg.
- Afro bounces subtly (1–2 px).
- Bandana sways with the wrist.
- Hands stay roughly at hip level — not raised, not dropped.

### `run` (6 frames, 12 fps)
- Lower torso, longer stride. Body leans forward 5–10°.
- Arms pump hard. Bandana trails behind on the back-swing.
- Frames 3 and 6 have horizontal speedlines behind the heel.
- Afro bounces more visibly.

### `jump` (3 frames, 8 fps — non-looping)
- F1: anticipation crouch — knees deep bend, arms drop.
- F2: peak/airborne — body extended, knees tucked slightly under, both fists raised.
- F3: landing — knees absorb, body re-collapsing toward idle.

### `atk1` — JAB (4 frames, 12 fps)
- F1: wind-up — front arm cocks back 4–6 px, body rotates slightly.
- F2: extend — front fist reaches forward to ~14 px past the body. Bandana trails behind the fist.
- F3: peak — fist fully extended, knuckles forward, bandana fully forward.
- F4: retract — fist returns 75% of the way back. Body returns to neutral.

### `atk2` — CROSS (5 frames, 11 fps)
- F1: wind-up — REAR arm cocks back, hip rotates back.
- F2: rotation — hip drives forward, rear shoulder rotates over.
- F3: extend — rear fist crosses the body line, reaching ~18 px forward. Bandana stays at hip on the now-back arm.
- F4: peak — fist fully extended, body rotated ~45°.
- F5: retract — body unwinds back toward forward stance.

### `atk3` — HOOK (6 frames, 11 fps) — combo finisher
- F1: wind-up — front fist drops slightly, body coils.
- F2: hip drive — body torque begins, hand starts arcing inward.
- F3: arc — fist sweeps in a horizontal arc, knuckles leading.
- F4: contact — fist at impact point, body fully torqued.
- F5: BRIEF SMILE — barely 1-pixel-changed mouth corner.
- F6: recovery — body returns toward stance.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 10 fps)
- F1: deep crouch — body drops, weight on rear leg, front fist drops to hip.
- F2: load — front fist near hip, body coiled.
- F3–F4: rise — body straightens explosively, front fist drives upward in a vertical line.
- F5: peak — fist directly above body line, arm fully extended skyward.
- F6: hold — pose held for emphasis (1 frame).
- F7: recovery — body lowers back to stance, fist comes down.

### `jump_atk` — AERIAL KNEE (4 frames, 10 fps)
- F1: airborne preparation — body airborne, front knee lifts toward chest.
- F2: extend — front knee extends downward + forward, body angles 30° forward.
- F3: peak — knee at full extension, foot pointing down-forward.
- F4: recovery — body resets toward landing pose.

### `back_atk` — REAR ELBOW (4 frames, 12 fps)
- F1: wind-up — body turns slightly toward the rear, rear elbow lifts.
- F2: drive — elbow drives back behind the body.
- F3: peak — elbow fully extended *behind* her, body twisted.
- F4: recovery — body unwinds.

### `special` — SUNSET SPIN (12 frames, 12 fps)
The signature. Spinning leg sweep into rising double-fist uppercut.
- F1: low crouch, weight loaded on the back foot.
- F2: pivot — front foot plants, body begins to rotate.
- F3–F4: leg sweep (lower body) — back leg sweeps in a 180° arc at ankle height. Bandana trails wide (drawn as a smear/streak across two frames).
- F5: rotation continues — body fully rotated, leg planting.
- F6: recovery from sweep — body straightens.
- F7: load — feet plant wide, both fists drop to hips.
- F8: BOTH ARMS RISE — vertical fist drive, both fists rocketing upward.
- F9: peak — both arms fully extended overhead, body slightly leaning into the upward motion.
- F10: bandana trail — bandana drawn as a streak ABOVE her, having flown skyward.
- F11: hold — pose for emphasis.
- F12: recovery — arms come down, body returns to stance.

### `throw` (5 frames, 11 fps)
- F1: grab — both arms forward, hands on enemy's collar.
- F2: lift — body straightens, enemy hoisted off-ground.
- F3: rotation — body twists, enemy pivots overhead.
- F4: release — enemy released downward, Rio's body in a forward lean.
- F5: recovery.

### `counter` — counter-special (6 frames, 12 fps)
- A bigger, brighter atk1 with a bandana flare. Same movement as the jab but the bandana **streaks across the entire arm length** for two frames.

### `hurt` (3 frames, 12 fps)
- F1: impact — body folds, head rocks back 5°.
- F2: recoil — torso bent slightly, arms momentarily out.
- F3: recovery — body straightening back to stance.

### `dodge` — backward roll (5 frames, 14 fps)
- F1: drop — body crouches sharply.
- F2: tuck — body curls forward, head down.
- F3: roll — body fully tucked, mid-roll silhouette (compact ball).
- F4: extend — body uncoiling out of the roll.
- F5: stand — back to stance.
- **Bandana stays visible** even during the tucked frames — a small yellow strip on the curled-up side.

## DO NOT include for Rio

- Glowing energy auras around hands or body
- Elemental effects (fire, lightning, ice) — she's a boxer, not a magic user
- Cape/scarf/long flowing items — only the bandana
- Modern combat boots (military style) — hers are sport boxing boots
- Long hair flowing — afro is contained, not flowing
- Open jacket flapping wildly — it's cropped and tight

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

### Frame counts (Rio total: 80)

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
1. Save to project root as `rio.png`.
2. Open `sprite_slicer.html`, load the PNG, click through to label all 15 anim slots.
3. Export `rio_atlas.json` next to the PNG.
4. `python3 pipeline.py validate-atlas rio_atlas.json`.
5. Reload `the_block.html`. The atlas loader picks it up automatically — Rio switches from procedural to sprite rendering. Any anim slot that's missing falls back to procedural for that animation only, so partial atlases are fine.


---

# DUKE

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

### `walk` (6 frames, 7 fps)
- 6-frame limping cycle. **Left leg strides cleanly; right leg drags 1 frame behind** — the limp.
- F1: left foot strikes forward, right foot still planted.
- F2: weight transfers, right foot lifts late.
- F3: right foot mid-swing (shorter stride than left's).
- F4: right foot strikes (shorter reach), left foot still planted.
- F5: weight transfers, left foot lifts.
- F6: left foot mid-swing (longer stride).
- Arms swing economically — front arm moves opposite to leg, but the swing is small (no exaggerated ROM).
- Body leans 5° forward, head bobbing 1 px on each strike.
- **Cigarette stays put.** Hair strand hangs forward, sways 1 px on each strike.

### `run` (6 frames, 11 fps)
- Body forward 10°, longer strides than walk but the right-leg stride is still 1–2 px shorter than the left's.
- F1, 4: foot strikes (alternating); F2–3, 5–6: in-air phases.
- Arms pump harder than walk but still elbow-led, not full-shoulder.
- Jacket flares open at the shoulders behind him — the cut-off frayed edges flap visibly.
- Hair flops on each back-swing — wayward strand whips up off the forehead briefly.
- **Frames 3 and 6:** 3-px horizontal speedlines behind each heel.
- **Cigarette stays put** even at this speed — it's the running gag.

### `jump` (3 frames, 8 fps — non-looping)
- F1: deep crouch, right (bad) knee bent shallower than left — he loads with the left leg primarily. Both fists drop to hip level.
- F2: airborne — body slightly tucked, **left leg leads**, right leg trails. Jacket flares open showing the t-shirt underneath.
- F3: landing — touches down on the left leg first, right foot follows half a frame later. Body absorbs into a half-crouch.
- **Cigarette stays put.** Hair strand whips upward at the apex.

### `atk1` — BOXING JAB (4 frames, 12 fps)
- Classic boxer's lead jab — front (left) hand, minimal body twist, snap-quick.
- F1: load — front shoulder pulls back 2 px, fist near the chin level. Eyes lock forward.
- F2: extend — left fist drives forward ~14 px, body twist minimal (5°), back foot stays planted.
- F3: peak — fist fully extended, knuckles vertical (boxing form), shoulder rolled forward to protect the chin.
- F4: snap-back — fist retracts 80% of the way back sharply (the boxer detail; not a slow draw-back). Body returns to stance.
- **Cigarette stays put** even on the snap-back.

### `atk2` — CROSS (5 frames, 11 fps)
- Right cross with full hip rotation — Duke's weight transfer move.
- F1: hip cocks back, weight shifts to back foot, right (rear) fist near jaw.
- F2: hip drives forward, rear shoulder rotates — torque visibly winding.
- F3: extend — rear fist crosses the center line, reaching ~18 px forward. Front (left) hand stays up at chin height for guard.
- F4: peak — fist fully extended, body rotated 45°, weight on front foot. Mouth tightens 1 px (the rare focus expression).
- F5: snap-back, body unwinds back to neutral stance. Hair strand settles back across the forehead.

### `atk3` — HOOK + STOMP (6 frames, 11 fps) — combo finisher
- Front hand hooks horizontally while the right foot stomps for power transfer.
- F1: load — body coils, front foot lifts 2 px off the ground, left (front) fist at hip height.
- F2: stomp wind-up — right foot drives downward.
- F3: hook arc — left fist swings inward in a horizontal arc as the right foot lands.
- F4: contact + stomp landing — fist at impact point, **dust puff at right foot** (1–2 px brown specks).
- F5: follow-through — body tilted 10° forward, fist past the impact line, the half-grin appears for one frame.
- F6: recovery — body unwinds back toward stance, hair strand falls back across forehead.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 9 fps)
- The launcher. Slow load, explosive rise — Duke putting his whole worn-out body into one shot.
- F1: deep crouch — both knees bend, both fists at hip. The **bad right knee is visibly strained** (1 px tilt).
- F2: load — front fist near belly, body coiled like a spring.
- F3: rise begins — knees start straightening, fist starts climbing.
- F4: drive — explosive vertical rise, front fist 16 px above the head height.
- F5: peak — body fully extended skyward, fist directly above body line, **half-grin visible** (this is the moment — he's enjoying it despite himself).
- F6: hold — pose held one extra frame for the launcher feel.
- F7: recovery — body lowers back to stance, knees absorbing.
- **Cigarette stays put** through the full extension.

### `jump_atk` — DROP ELBOW (4 frames, 10 fps)
- Aerial elbow drop — uses gravity, not a kick.
- F1: airborne, right elbow cocked overhead, body still rising.
- F2: descent begins — body angles 30° forward, elbow leading the drop.
- F3: peak impact — elbow at chest-of-imagined-target height, body 45° forward. Hair strand whips upward.
- F4: recovery — body resets, elbow lowering toward landing.
- **Cigarette stays put** even at the apex.

### `back_atk` — REAR ELBOW (4 frames, 12 fps)
- Heavier rear-elbow strike than Rio's — Duke pivots more on the bad knee, so the move loads slow but lands hard.
- F1: wind-up — body turns 30° toward the rear, right elbow lifts to shoulder height. Weight shifts to the left (good) leg.
- F2: drive — elbow drives backward, right hip rotating with it.
- F3: peak — elbow fully extended *behind* him, body twisted 60°, the half-grin briefly appears (1 frame).
- F4: recovery — body unwinds back to stance, weight redistributing.
- **Cigarette stays put** through the rotation.

### `special` — ROLLING THUNDER (12 frames, 11 fps)
The signature. Three rapid forward elbows finishing with a haymaker that ends fights.
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


---

# ATLAS

## Physical

- **Age:** 47
- **Height/build:** **6'4", massive** — powerlifter physique that's gone slightly soft. Broad shoulders, thick neck, large barrel chest, arms thicker than Rio's calves. Belly slightly rounded but chest still huge. **He should read AT LEAST 30% bigger than Rio or Duke** in silhouette.
- **Ethnicity:** Mixed/Mediterranean; deep olive skin, weathered.
- **Body language:** Slow, deliberate, planted. Doesn't bounce. Stands with feet shoulder-width apart minimum. **He moves like a man who knows everyone is watching him** — there's no rush.
- **Face:** Heavy brow, deep-set eyes, broad nose (broken once long ago). Strong jawline mostly hidden by the beard. Resting expression: thoughtful, not angry. Smile is small, parental.

## Hair

- **Style:** **Bald.** Completely. Smooth scalp with maybe a slight 5 o'clock shadow across the dome (1–2 px darker tint).
- **Beard:** **FULL salt-and-pepper.** Wraps the lower jaw and chin, thick and visible. Mostly grey-silver with darker streaks near the chin. Neat but not trimmed-to-the-millimeter — slightly wild around the edges. **Mustache connects to the beard** (not a chinstrap-only look).

## Costume (head to feet)

1. **SILVER WEDDING BAND ON A CHAIN:** **Around his neck**, a thin silver chain (1-pixel wide). At chest height it carries a single silver wedding band (2x2 px). **Visible through the open V of the flannel** in every frame. Catches a tiny highlight pixel on the band.
2. **Flannel shirt:** **Sleeveless** — the sleeves are torn off (jagged edge, like Duke's denim but worse, frayed threads visible). Deep red plaid pattern: dark red base with subtle black cross-hatching. **Top three buttons undone** showing a V of skin and the chain. Hem comes to mid-hip. Slightly tighter at the shoulders, looser around the waist.
3. **TRIBAL FOREARM TATTOOS:** **Both bare forearms** carry faded geometric tribal tattoo bands. Two horizontal bands per forearm, each band 1 px tall, 6–8 px long, dark green-black ink. Faded — not crisp/new. Reads as old work that's softened over decades.
4. **Belt:** Wide black leather belt, **brass buckle** (5x4 px square, brushed gold). Sits at the natural waist.
5. **Pants:** Heavy work pants, dark olive-brown (think Carhartt). Slightly baggier than Duke's jeans. **Two patches** — one at the right knee (lighter brown, square), one on the left thigh (frayed darker patch).
6. **Boots:** **Steel-toed work boots,** dark brown leather, scuffed white/grey at the steel toe. Heavy laces, top loose. Soles thick.

## Palette (hex)

```
skin (light)        #7a5234
skin (shadow)       #583820
skin (deep)         #3a2218
beard (light)       #a8a4a0
beard (shadow)      #6e6c6a
beard (dark accent) #4a4844
flannel (mid)       #7a3030
flannel (shadow)    #5a1c1c
flannel (highlight) #9a4040
flannel (plaid line) #3a1010
pants               #3a3024
pants shadow        #221c14
pants patch         #5a4a30
pants frayed patch  #28201a
boot                #1c140c
boot sole           #08060a
boot steel toe      #5a5a5a
belt                #1a1410
belt buckle         #cfa040
chain silver        #c0c0c8
chain shadow        #7a7a82
wedding band        #d8d8e0
tattoo              #3a2a1a
tattoo highlight    #4a3a2a
eye whites          #f0f0f0
```

## Personality cues that should show in poses

- **Slow, planted stance.** Both feet on the ground. He moves them deliberately.
- **The hands are huge.** Draw them slightly larger relative to body than Rio/Duke.
- **The smile is gentle.** When it appears (atk3 finisher, after Foundation Stone), it's a small parental smile.
- **The wedding band is a tell.** When he gets serious — when the haymaker is coming — the band catches a brief 1-pixel glint highlight.

## Animations (per slot — pose + key pose details)

### `idle` (4 frames, loops, 5 fps — slowest in the cast)
- F1: chest at full inhale — shoulders raised 2 px, ribcage visibly out, beard tilts up 1 px. Hands at hip height, loosely closed (not fisted hard).
- F2: hold — barely-perceptible pause at full inhale, **wedding band catches a 1-px highlight** as it sits on the chest.
- F3: chest at full exhale — shoulders settle 3 px, beard relaxes downward. Chain dips 1 px lower against the chest.
- F4: hold at exhale, eyes scanning the camera-side direction (he's watching the block).
- **Wedding band on chain visible through the open V** the entire cycle.
- **Tribal forearm tattoos** visible on both forearms.
- Mouth set in a thoughtful, neutral expression — not angry.

### `walk` (6 frames, 6 fps — slowest walk in the cast)
- **Heavy stomp gait.** Both boots land flat-footed; each step has weight.
- F1: left foot strikes forward, right foot still planted. **1-px dust puff at the left heel.**
- F2: weight transfer — body sways 1 px to the left, right foot lifts.
- F3: right foot mid-swing.
- F4: right foot strikes forward, left planted. **1-px dust puff at the right heel.**
- F5: weight transfer — body sways 1 px to the right.
- F6: left foot mid-swing, beginning the cycle again.
- Body wide stance throughout — minimum shoulder-width even at full stride.
- **Chain swings 1–2 px laterally with each weight shift.** Wedding band visible.
- Beard moves 1 px with each impact.

### `run` (6 frames, 10 fps)
- Running for Atlas isn't graceful — he covers ground but the body doesn't bounce, it surges. Body angled 5° forward.
- F1: left foot strike — bigger dust puff than walk (3–4 brown specks). Body forward.
- F2: airborne briefly, both feet off, arms swinging.
- F3: right foot strike — dust puff. Body still forward.
- F4: airborne, the second push.
- F5: same as F1 cycle continues.
- F6: same as F3.
- **Frames 1 and 4 (foot strikes):** dust kicks at the boots, 3–4 px brown specks each.
- **Chain bounces visibly** — 2–3 px vertical movement per stride. Wedding band trails behind the chain by 1 frame.
- Flannel hem flares slightly behind him — body so wide it doesn't flap dramatically, but the bottom edge lifts 2 px on each stride.

### `jump` (3 frames, 8 fps — non-looping)
- F1: deep crouch — both knees bend hard, body coils, weight on both feet equally. Hands drop to knee level.
- F2: peak — body extended but arms NOT raised overhead (he doesn't reach skyward; that's not his style). He gets maybe 6–8 px off the ground; not a high jump. Chain lifts off the chest 2 px.
- F3: landing — heavy compression, both knees absorb. **Dust burst at both boots** (4–5 brown pixels).
- **Wedding band stays visible** at all three frames.

### `atk1` — OPEN-PALM SHOVE (4 frames, 11 fps)
- Front arm extends as a palm-strike, fingers splayed — Atlas doesn't waste energy throwing fists for jabs. The shove sets up combos by knocking enemies back.
- F1: load — front (left) palm at chest level, fingers loose. Body weight forward 5°.
- F2: drive — palm extends forward, body weight transfers to front foot.
- F3: peak — palm fully extended ~16 px forward, **fingers visibly splayed** (open hand, not a fist), body angled 10° forward.
- F4: retract — palm pulls back 70%, body returns to neutral. **Tribal tattoos** visible on the forward forearm during the extension.
- Wedding band catches a small movement against the chest.

### `atk2` — REAR HEAVY SLAP (5 frames, 10 fps)
- Rear arm sweeps across in a heavy backhand slap, palm leading — heavier than a hook because the whole body torques.
- F1: load — right arm wound up across the body to the left side, body torqued back.
- F2: hip rotates forward, right shoulder begins arcing across.
- F3: sweep — right arm crosses the center line, palm leading at face-of-imagined-target height.
- F4: peak — palm fully across the body, body rotated 60°, **beard moves 2 px with the strike** (the head whips slightly with the rotation).
- F5: recovery — body unwinds back to stance, chain swinging back to neutral.
- **Tribal tattoos** prominent on the bare striking forearm.

### `atk3` — OVERHEAD CHOPPING SMASH (6 frames, 10 fps) — combo finisher
- Both hands clasp together overhead, then drive downward like a hammer-fist — Atlas's signature combo finisher, ends with the gentle parental smile.
- F1: load — both fists rise overhead, clasped together, body coiling.
- F2: rise complete — both hands above head, body extended skyward, ribs visibly out.
- F3: pause — slight 1-frame hold at the peak (the load before the drop).
- F4: descent — body folds forward at the waist, both hands drive downward together.
- F5: impact — hands at chest-of-imagined-target height, **big dust puff at his feet** (4–5 brown specks). Beard tilts forward with the body.
- F6: follow-through + recovery — body straightens, **the small parental smile is visible** for one frame (the gentle moment).
- **Wedding band on chain visible** throughout, swinging with the body.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 8 fps — slowest in the cast)
- Massive uppercut. Both legs braced, fist rises slowly but with terrifying weight.
- F1: deep crouch — both knees bend, right (rear) fist drops below the knee, body coils. Beard tucks down.
- F2: load — body fully coiled, fist near hip, weight evenly on both feet.
- F3: rise begins — body slowly straightens, fist starts climbing.
- F4: drive — fist drives upward, **WEDDING BAND CATCHES A 1-PX HIGHLIGHT GLINT** (this is the tell — when the band glints, the haymaker is coming).
- F5: peak — fist directly overhead, body fully extended, both feet planted firmly. Mouth set hard.
- F6: hold — pose held one extra frame for the launcher feel — Atlas pauses at the top, terrifying.
- F7: recovery — body lowers back to stance, fist coming down slowly.
- **Tribal tattoos** prominent on the rising arm at F4–F5.

### `jump_atk` — BODY SLAM (4 frames, 9 fps)
- He doesn't kick — he uses his weight. Drops elbow-first, all 280 pounds of him.
- F1: airborne, body angled forward 20°, right elbow lifted overhead.
- F2: descent begins — body angles down further (45°), elbow leading the drop, weight visibly forward.
- F3: peak impact — elbow at impact zone, body nearly horizontal, **chain has flown forward off his chest** (visible in front of the flannel, 3 px out from the body).
- F4: recovery — body resets toward landing, chain settling back against the chest.
- **Wedding band visible** at all four frames.

### `back_atk` — REAR ELBOW (4 frames, 11 fps)
- Heavier rear-elbow than Rio's — Atlas's whole body has to rotate, so the move is slow but devastating.
- F1: wind-up — body turns 35° toward the rear, right elbow lifts to shoulder height, weight loads on the left foot.
- F2: drive — right elbow drives backward, hip rotating with it, body torquing.
- F3: peak — elbow fully extended *behind* him, body twisted 70°, **chain swings sideways across the chest** (visible swinging arc, 3 px lateral travel). Mouth tightens.
- F4: recovery — body unwinds back to stance, chain settling back, weight redistributing.
- **Tribal tattoos** visible on the striking forearm at F3.

### `special` — FOUNDATION STONE (12 frames, 10 fps)
The signature. Running shoulder charge, picks the enemy off the ground, two-handed overhead slam — Atlas asserting that this block is his.
- F1: stance — shoulder lowered (charge prep), body coiled, weight loading on the back leg.
- F2: forward step — leading (left) leg plants 6 px ahead, body angled 15° forward.
- F3: charge — body angled 20° forward, **shoulder leading** the run. **Three 4-px speedlines** behind him at body height.
- F4: charge continues — body lower, knees deeper, **four speedlines** now (more density).
- F5: charge peak speed — body lowest, **five speedlines**, chain visibly trailing behind the running body by 2 px.
- F6: contact — body crashes into imagined enemy, both arms reach forward to grab. Body straightens slightly from the charge.
- F7: lift — both hands grab the enemy at chest height, hoisting them upward. Body straightens, knees beginning to drive up. **Tribal tattoos** prominent on both forearms.
- F8: peak — enemy lifted **OVERHEAD** (2–3 px above Atlas's head), Atlas's arms fully extended skyward, body stretched tall. **Wedding band visible** against the now-tightened flannel V.
- F9: descent begins — Atlas's body rotates forward, slamming the enemy down. Arms drive downward in a controlled arc.
- F10: **SLAM IMPACT** — enemy at ground level, **DUST BURST AROUND BOTH BOOTS** in a wide half-circle pattern (5–6 brown pixels). Atlas's body folded forward 30°, hands at his shins. Beard tilts forward.
- F11: hold — pose locked, body upright, both fists at hip, **the small parental smile visible** for one frame (the sentimental beat — he doesn't enjoy violence, but he just protected someone).
- F12: recovery — body returns to stance, chain settling back against the chest.

### `throw` (5 frames, 9 fps)
- Lifting suplex — slower and heavier than Rio's or Duke's throw. Atlas wraps the enemy around his back and falls with them.
- F1: grab — both hands on enemy at chest height, body coiling.
- F2: lift — body straightens, enemy leaves the ground, Atlas's knees beginning to drive up.
- F3: arch back — Atlas's body bends backward 30°, enemy goes overhead, **chain visible against the chin** as the chest tilts up.
- F4: slam — both fall together, Atlas on top, enemy underneath. **Dust burst around both bodies** at impact (4–5 brown specks).
- F5: recovery — Atlas planting his hands, pushing back up to standing. Body upright again, chain back against the chest.
- **Tribal tattoos** visible on both forearms throughout the lift.

### `counter` — counter-special (6 frames, 10 fps)
- The free counter-special at full parry meter. A bigger, meaner atk3 (the overhead chopping smash) with double the dust burst — the counter that ends fights.
- F1: load — both fists clasped overhead, body coiled deeper than atk3 (knees bending more), weight loading.
- F2: rise to peak — both hands above head, body extended fully skyward, **wedding band glint visible** (the tell).
- F3: pause — 1-frame hold at peak, the kill-shot windup.
- F4: descent — body folds forward at the waist, both hands drive downward together with maximum force.
- F5: impact — hands at chest-of-imagined-target height, **MASSIVE DUST BURST at his feet** (8–10 brown specks in a wide half-circle, twice the size of atk3's). The parental smile is at full visibility.
- F6: recovery — body straightens, hands lowering. Chain settling.

### `hurt` (3 frames, 12 fps)
- F1: impact — body absorbs, doesn't fold much (he's heavy and built for it). Head turns 5° with the strike, beard tilts.
- F2: recoil — body bends 10° at the waist, knees bending slightly. Chain swings 2 px sideways.
- F3: recovery — body straightening back to stance, chain settling.
- **Wedding band stays visible** through all three frames — it's part of him.

### `dodge` — SIDESTEP (5 frames, 11 fps)
- Atlas doesn't roll. The body doesn't allow it. He **takes a planted side step** with a forearm raised across the body in a guard.
- F1: weight shifts onto one foot (the foot opposite the dodge direction), body coils.
- F2: side step — back foot crosses over in front, body sliding 4 px laterally. Right forearm rises across the body to chest height (guard position).
- F3: planted — body sideways briefly, **right forearm fully across the body** (tribal tattoos prominent on the guard arm), feet wide.
- F4: foot returns — back foot uncrosses, weight redistributing.
- F5: stance — settled back into idle stance, forearm lowering. Chain settling back against the chest.

## DO NOT include for Atlas

- Long hair / mohawk / any hair on the head — bald
- Trimmed/short beard — full beard, slightly wild
- Sleeves on the flannel — they're torn off
- Closed flannel — top three buttons undone showing the chain
- Glowing fists / elemental effects — he's a man, not a magic user
- Boots without steel toe — they have a visible silver/grey toe cap
- Athletic shorts / gym wear — he's in heavy work pants

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

### Frame counts (Atlas total: 80)

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
- Each cell: **80 wide × 112 tall** for Atlas (he's bigger than Rio/Duke). If sticking to a 64×96 cell to match the other two sheets, allow his body to fill the whole cell with his head touching the top edge.
- Background: solid magenta `#ff00ff` for keying, OR transparent PNG.
- Anchor each frame's character at **bottom-center** of the cell.

### Final integration step

When this sheet lands:
1. Save to project root as `atlas.png`.
2. Open `sprite_slicer.html`, load the PNG, click through to label all 15 anim slots.
3. Export `atlas_atlas.json` next to the PNG.
4. `python3 pipeline.py validate-atlas atlas_atlas.json`.
5. Reload `the_block.html`. The atlas loader picks it up automatically — Atlas switches from procedural to sprite rendering. Any anim slot that's missing falls back to procedural for that animation only, so partial atlases are fine.
