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
