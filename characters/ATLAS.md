# ATLAS

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **15 distinct animation rows** in this exact order, one anim per row, no skipping, no merging:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `run` (6 frames)
> 4. `jump` (3 frames)
> 5. `atk1` — OPEN-PALM SHOVE (4 frames)
> 6. `atk2` — REAR HEAVY SLAP (5 frames)
> 7. `atk3` — OVERHEAD CHOPPING SMASH (6 frames)
> 8. `heavy` — UPPERCUT LAUNCHER (7 frames)
> 9. `jump_atk` — FLYING BODY SPLASH (4 frames)
> 10. `back_atk` — REAR ELBOW (4 frames)
> 11. `special` — FOUNDATION STONE (12 frames) — **the signature move, must be visually distinct from atk3**
> 12. `throw` (5 frames)
> 13. `counter` (6 frames)
> 14. `hurt` (3 frames)
> 15. `dodge` (5 frames)
>
> **Total: 80 frames in 10 rows × 8 columns.** If any row is missing, the engine substitutes a fallback that looks wrong (e.g. special replaying the atk3 combo finisher). Every row matters.

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
**Visual signature:** **OPEN PALM, fingers visibly splayed** — Atlas's jab is not a fist. Front arm extends as a palm-strike. The tribal forearm tattoos are prominent on the striking arm. The wedding band on its chain shifts against the chest as the body shoves forward. This is the only "jab" in the cast that isn't a fist — instantly readable as Atlas.
- F1: load — front (left) palm at chest level, fingers loose. Body weight forward 5°.
- F2: drive — palm extends forward, body weight transfers to front foot.
- F3: peak — palm fully extended ~16 px forward, **fingers visibly splayed** (open hand, not a fist), body angled 10° forward.
- F4: retract — palm pulls back 70%, body returns to neutral. **Tribal tattoos** visible on the forward forearm during the extension.
- Wedding band catches a small movement against the chest.

### `atk2` — REAR HEAVY SLAP (5 frames, 10 fps)
**Visual signature:** **massive backhand slap with the WHOLE BODY torquing** — rear arm crosses the entire screen from one side to the other (a 60°+ body rotation), palm leading. The beard whips 2 px with the rotation. Tribal tattoos prominent on the bare striking forearm throughout the arc. Unmistakable "wide arc, not a punch" silhouette.
- F1: load — right arm wound up across the body to the left side, body torqued back.
- F2: hip rotates forward, right shoulder begins arcing across.
- F3: sweep — right arm crosses the center line, palm leading at face-of-imagined-target height.
- F4: peak — palm fully across the body, body rotated 60°, **beard moves 2 px with the strike** (the head whips slightly with the rotation).
- F5: recovery — body unwinds back to stance, chain swinging back to neutral.
- **Tribal tattoos** prominent on the bare striking forearm.

### `atk3` — OVERHEAD CHOPPING SMASH (6 frames, 10 fps) — combo finisher
**Visual signature:** **BOTH HANDS CLASPED TOGETHER overhead** (like swinging an invisible sledgehammer), driven downward in a vertical chopping motion. Body folds forward at the waist on impact, **dust burst at his feet (4–5 brown specks)**. F6 the **brief parental smile** appears for one frame — the only soft moment in the whole cast.
- F1: load — both fists rise overhead, clasped together, body coiling.
- F2: rise complete — both hands above head, body extended skyward, ribs visibly out.
- F3: pause — slight 1-frame hold at the peak (the load before the drop).
- F4: descent — body folds forward at the waist, both hands drive downward together.
- F5: impact — hands at chest-of-imagined-target height, **big dust puff at his feet** (4–5 brown specks). Beard tilts forward with the body.
- F6: follow-through + recovery — body straightens, **the small parental smile is visible** for one frame (the gentle moment).
- **Wedding band on chain visible** throughout, swinging with the body.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 8 fps — slowest in the cast)
**Visual signature:** the **WEDDING-BAND GLINT on F4** is the tell — a 1-px highlight on the silver band as the chain swings with the rising fist. When the band glints, the launcher is about to hit. Both legs braced flat (Atlas never goes up on his toes). Slowest attack in the cast — held one extra frame at the peak.
- F1: deep crouch — both knees bend, right (rear) fist drops below the knee, body coils. Beard tucks down.
- F2: load — body fully coiled, fist near hip, weight evenly on both feet.
- F3: rise begins — body slowly straightens, fist starts climbing.
- F4: drive — fist drives upward, **WEDDING BAND CATCHES A 1-PX HIGHLIGHT GLINT** (this is the tell — when the band glints, the haymaker is coming).
- F5: peak — fist directly overhead, body fully extended, both feet planted firmly. Mouth set hard.
- F6: hold — pose held one extra frame for the launcher feel — Atlas pauses at the top, terrifying.
- F7: recovery — body lowers back to stance, fist coming down slowly.
- **Tribal tattoos** prominent on the rising arm at F4–F5.

### `jump_atk` — FLYING BODY SPLASH (4 frames, 9 fps)
**Visual signature:** Atlas doesn't kick — he becomes a falling building. **F3 silhouette: body HORIZONTAL parallel to the ground at peak, arms spread out wide like a wrestler's diving splash, chest leading the descent. The wedding-band chain has flown 4 px forward off his chest from the dive momentum. Tribal forearm tattoos prominent on both spread arms.** Lands flat — both forearms and chest hit simultaneously. The most graceless aerial in the cast, intentionally.
- F1: airborne, body still rising, arms beginning to spread.
- F2: peak of jump — body starts rotating from vertical toward horizontal, arms spreading wider.
- F3: **peak descent — body fully horizontal parallel to ground, both arms spread wide like a diving splash, chest leading, chain flown 4 px forward off the chest, tribal tattoos visible on both forearms**.
- F4: landing — both arms and chest impact, **dust burst beneath the body (5–6 brown specks in a wide horizontal smear)**, chain settling back.
- **Wedding band visible** at all four frames.

### `back_atk` — REAR ELBOW (4 frames, 11 fps)
- Heavier rear-elbow than Rio's — Atlas's whole body has to rotate, so the move is slow but devastating.
- F1: wind-up — body turns 35° toward the rear, right elbow lifts to shoulder height, weight loads on the left foot.
- F2: drive — right elbow drives backward, hip rotating with it, body torquing.
- F3: peak — elbow fully extended *behind* him, body twisted 70°, **chain swings sideways across the chest** (visible swinging arc, 3 px lateral travel). Mouth tightens.
- F4: recovery — body unwinds back to stance, chain settling back, weight redistributing.
- **Tribal tattoos** visible on the striking forearm at F3.

### `special` — FOUNDATION STONE (12 frames, 10 fps)
The signature.
**Visual signature:** THREE distinct phases readable from across the room. (1) **Forward shoulder charge** — body angled 25° forward, speed-lines growing from 3 → 5 lines as he sprints. (2) **Pickup grapple** — both arms reach forward, lift the imagined enemy chest-high, tribal tattoos prominent on both bare forearms, wedding-band chain swinging. (3) **Overhead two-handed slam** — both fists clasped above the head, then DRIVEN STRAIGHT DOWN into the ground with a **massive dust burst (8–10 brown specks in a wide half-circle reaching 40 px each side)** plus a 1-frame screen-shake suggestion. The slam pose plants both feet wide. The only grapple-into-slam move in the cast.
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
