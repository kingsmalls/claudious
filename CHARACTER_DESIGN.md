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

- **Style:** Shaved at the temples and back of neck (low fade — short clipper line, not bare). Short locs on top, 2–3 inches long, framing the crown. Locs are dark brown to black, slightly uneven length, a few falling forward over the forehead.
- **Movement:** Locs swing slightly with hard motion — visible bounce on jumps and the Sunset Spin spin. Not flowing dramatic hair; firm, weighty.

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
hair (locs)         #1a1410
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
- Frames 2, 4: bounce-up — slight rise, locs lift 1px.
- Bandana visible on left wrist throughout, hanging slightly.
- Eyes scanning forward. Mouth neutral.

### `walk` (6 frames, 8 fps)
- 6-frame stride cycle. Forward foot strikes on frames 1 and 4.
- Front arm swings opposite to leg.
- Locs bounce subtly (1–2 px).
- Bandana sways with the wrist.
- Hands stay roughly at hip level — not raised, not dropped.

### `run` (6 frames, 12 fps)
- Lower torso, longer stride. Body leans forward 5–10°.
- Arms pump hard. Bandana trails behind on the back-swing.
- Frames 3 and 6 have horizontal speedlines behind the heel.
- Locs bounce more visibly.

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
- Long hair flowing — locs are short and structured
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

## Animations (per slot)

### `idle` (4 frames, 6 fps)
- F1, 3: weight on left leg (the good one), right leg slightly bent and forward.
- F2, 4: weight subtly shifts. Shoulders rise/fall with breath.
- Hands at lower-belly height, loosely fisted.
- Cigarette behind camera-side ear.

### `walk` (6 frames, 7 fps)
- Slightly limping gait (right knee). Left leg strides normally, right leg follows with a half-second delay.
- Arms swing economically, not exaggerated.
- Body leans slightly forward.

### `run` (6 frames, 11 fps)
- The limp is mostly absorbed at this speed but right leg's stride is slightly shorter than left's.
- Arms pump, jacket flares open behind him.
- Hair flops on the back-swing.
- Frames 3 and 6 have speedlines.

### `jump` (3 frames)
- F1: deep crouch with right leg loaded weaker.
- F2: airborne, body slightly tucked, left leg leads.
- F3: landing — favors the left leg on touch-down.

### `atk1` — BOXING JAB (4 frames, 12 fps)
- Standard boxer's jab. Front (left) hand, body twist minimal.
- F1: load — front shoulder back 2px.
- F2: extend — fist drives forward 14 px.
- F3: peak — fist fully extended, knuckles vertical.
- F4: snap-back — fist returns sharply (this is the boxing detail — the snap-back).

### `atk2` — CROSS (5 frames, 10 fps)
- Right cross with full hip rotation.
- F1: hip cocks back, weight shifts to back foot.
- F2: hip drives, rear shoulder begins rotation.
- F3: rear fist crosses center line.
- F4: peak — fist 18 px forward, body fully rotated, weight on front foot.
- F5: snap-back, returning to stance.

### `atk3` — HOOK + STOMP (6 frames, 10 fps)
- Combo finisher. Front hand hooks while right foot stomps.
- F1: load — body coils, front foot lifts slightly.
- F2: stomp begins — foot drives down.
- F3: hook arc — front fist swings horizontally inward.
- F4: contact + stomp landing — small dust puff at the right foot (1–2 px brown specks).
- F5: peak with body tilted forward.
- F6: recovery.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 9 fps)
- F1: deep crouch, both fists at hip.
- F2–3: front fist loads near belly.
- F4: explosive rise — fist drives up.
- F5: peak — body fully extended, fist overhead, **half-grin visible** (this is the moment).
- F6: hold.
- F7: recovery.

### `jump_atk` — DROP ELBOW (4 frames, 11 fps)
- F1: airborne, elbow cocked overhead.
- F2: descent — body angles down, elbow leading.
- F3: peak — elbow at chest-of-imagined-target height, body angled 45° forward.
- F4: recovery.

### `back_atk` — REAR ELBOW (4 frames, 12 fps)
- Same beats as Rio but heavier; body rotates more.

### `special` — ROLLING THUNDER (12 frames, 11 fps)
Three rapid forward elbows finishing with a haymaker.
- F1: stance, body coils.
- F2–F3: **first elbow** — left elbow drives forward 8 px with a short speedline (3 px streak behind the elbow).
- F4–F5: **second elbow** — right elbow drives forward 10 px, body rotated. Speedline.
- F6–F7: **third elbow** — left elbow again, deeper drive 12 px, body lower.
- F8: load haymaker — body torques back, right fist way behind.
- F9: drive — body weight drops forward, right fist arcs in a downward overhand path.
- F10: contact — fist at impact point, **dust puff at his feet** (2–3 brown pixels), face shows the half-grin.
- F11: hold (one frame of pose).
- F12: recovery — body straightens slightly.

### `throw` (5 frames, 10 fps)
- F1: grab — both hands forward, fistfuls of imagined collar.
- F2: lift — heave upward, body in a row stance.
- F3: spin — rotates the enemy.
- F4: slam — drives them downward.
- F5: recovery, hands dropping.

### `counter` — counter-special (6 frames, 11 fps)
- A bigger Rolling Thunder finishing strike. Body wider, fist heavier. Dust puff is bigger (5–6 specks).

### `hurt` (3 frames)
- F1: impact, head whips back.
- F2: recoil, torso folded.
- F3: recovery.
- **Cigarette stays in place.** This is the joke.

### `dodge` — BACKWARD STEP (5 frames, 12 fps)
- Duke doesn't roll — knee won't allow it. He **steps back fast** with a hand raised.
- F1: weight shifts to back foot.
- F2–F3: pushes back hard, body slides backward.
- F4–F5: settles into stance, hand still raised in a "stop" gesture.

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

## Animations (per slot)

### `idle` (4 frames, 5 fps — slower than the others)
- Heavy chest rise/fall. Shoulders move 2–3 px on the breath cycle.
- Hands at hip level, loosely closed.
- Wedding band visible through the V; chain slightly catching breath rhythm.
- Beard moves with breath subtly.

### `walk` (6 frames, 6 fps)
- **Heavy stomp gait.** Boots land flat-footed. Each step has impact.
- Frames 1 and 4: foot strike — slight 1-px dust puff at the heel.
- Body sways laterally (he's wide).
- Chain swings 1–2 px with each step.

### `run` (6 frames, 10 fps)
- He runs but it's not graceful. Long strides, body forward 5°.
- Chain bounces visibly.
- Frames 3 and 6 have **dust kicks** at the boots (3–4 px brown specks).

### `jump` (3 frames)
- F1: crouch — heavy load, both knees bent deep.
- F2: peak — body extended but arms not fully raised. He gets a foot off the ground; not a high jump.
- F3: landing — heavy compression, dust burst at both boots.

### `atk1` — OPEN-PALM SHOVE (4 frames, 11 fps)
- Front arm extends as a palm-strike, not a fist. Body weight slightly forward.
- F1: load — palm at chest level.
- F2: extend — palm drives forward 16 px.
- F3: peak — fingers slightly splayed.
- F4: retract.

### `atk2` — REAR HEAVY SLAP (5 frames, 10 fps)
- Rear arm comes across in a heavy backhand slap, not a closed fist.
- F1: arm wound up across the body.
- F2: hip rotates.
- F3: arm sweeps across, palm leading.
- F4: peak — palm fully across body, beard moves with the strike.
- F5: recovery.

### `atk3` — OVERHEAD CHOPPING SMASH (6 frames, 10 fps)
- Combo finisher. Both hands clasp above head, then drive downward like a hammer-fist.
- F1: hands rise — both fists clasped together drive upward overhead.
- F2: peak — hands above head, body extended skyward.
- F3: load — slight pause at peak.
- F4: descent — body folds forward, hands drive down.
- F5: impact — hands at chest-of-imagined-target height, **dust puff at his feet**.
- F6: hold + the small parental smile.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 8 fps — slowest of the cast)
- Massive uppercut. Both legs braced, fist rises slowly but with terrifying weight.
- F1: deep crouch, fist drops below the knee.
- F2: load — body coiled, fist near hip.
- F3: rise begins — body slowly straightens.
- F4: drive — fist drives upward, **wedding band glint** visible (1 frame highlight).
- F5: peak — fist directly overhead, body fully extended, both feet planted.
- F6: hold — pose held one extra frame for emphasis.
- F7: recovery.

### `jump_atk` — BODY SLAM (4 frames, 9 fps)
- He doesn't kick — he uses his weight. Drops elbow-first.
- F1: airborne, body angled forward.
- F2: descent — elbow lifted overhead, weight forward.
- F3: peak — elbow drive at impact zone, body horizontal-ish.
- F4: recovery — body resets to landing.

### `back_atk` — REAR ELBOW (4 frames, 11 fps)
- Heavier than the others. Elbow drives back with hip rotation.

### `special` — FOUNDATION STONE (12 frames, 10 fps)
The signature. Running shoulder charge, picks up the enemy, two-handed slam.
- F1: stance with shoulder lowered (charge prep).
- F2: forward step — leading leg plants 6 px ahead.
- F3: charge — body angled 20° forward, shoulder leading. **Three speedlines** behind him.
- F4–F5: charge continues, body lower, more speedlines.
- F6: contact — body crashes into imagined enemy, both arms reach forward.
- F7: lift — both hands grab the enemy, hoisting them upward.
- F8: peak — enemy lifted overhead (2–3 px above Atlas's head), Atlas's arms fully extended.
- F9: descent begins — Atlas body rotates forward, slamming the enemy down.
- F10: SLAM IMPACT — enemy at ground level, **DUST BURST AROUND BOTH BOOTS** (5–6 brown pixels in a half-circle pattern).
- F11: hold — pose held, both fists at hip, body upright.
- F12: recovery — body returns to stance.

### `throw` (5 frames, 9 fps)
- Lifting suplex. Slower and heavier than Rio's or Duke's throw.
- F1: grab — both hands on enemy.
- F2: lift — body straightens, enemy leaves ground.
- F3: arch back — Atlas's body bends backward, enemy goes overhead.
- F4: slam — both fall together, enemy underneath.
- F5: recovery — Atlas planting feet, standing back up.

### `counter` — counter-special (6 frames, 10 fps)
- A bigger atk3 (overhead smash) with even bigger dust burst on impact (8 brown pixels).

### `hurt` (3 frames)
- F1: impact — body absorbs, doesn't fold much (he's heavy).
- F2: head turns slightly with the strike.
- F3: recovery.
- **Wedding band stays visible.**

### `dodge` — SIDESTEP (5 frames, 11 fps)
- Atlas doesn't roll. He **takes a side step** with a forearm raised across the body.
- F1: weight shift to one foot.
- F2: side step — the back foot crosses over.
- F3: planted — body sideways briefly, forearm guard up.
- F4: foot returns.
- F5: stance.

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

---

Each character section above is **self-contained for copy-paste**: physical, costume, identity items, palette, animation poses, special-move beat sheet, "do NOT include" list, and full sheet specs. Hand any single section to your generator/artist and they have everything they need for that character.
