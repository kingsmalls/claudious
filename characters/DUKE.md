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

