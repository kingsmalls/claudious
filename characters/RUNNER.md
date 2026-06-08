# RUNNER

Kane's bottom-tier muscle. Recruited from Kane's "neighborhood liaison" jobs program — a euphemism for a paycheck in exchange for nights like this one. Most of them are going to wake up tomorrow regretting being here. They don't know that yet.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **8 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `run` (4 frames)
> 4. `atk1` — WILD SWIPE (4 frames) — **over-committed OVERHAND HAYMAKER**, front leg crosses past the body line, rear arm flails behind, RED BICEP BANDANA streaks horizontally through the swing
> 5. `atk2` — SLOPPY KICK (4 frames) — **kicking leg straight forward at hip height with the FOOT FLAT (not flexed)**, body leans BACK 30° (no balance), both arms flailing wide, supporting knee visibly buckling
> 6. `hurt` (3 frames)
> 7. `dead` (3 frames)
> 8. `flee` (4 frames)
>
> **Total: 32 frames in 8 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Runner only has two attacks, and the generator's failure mode is **both reading as "cocky kid stumbling forward."** Each must occupy a different silhouette quadrant — the over-commitment must read in different limbs and opposite body angles:
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` wild swipe | Body OVER-COMMITS FORWARD, front leg crosses past body line | Lead ARM in an overhand haymaker arc | Diagonal-down forward from overhead | Front leg CROSSES past the body line, rear arm flails BEHIND for balance, RED BICEP BANDANA streaks horizontally through the swing — the only arm attack + body falling forward into it |
> | `atk2` sloppy kick | Body LEANS BACK 30° (no balance), supporting knee buckling | Kicking LEG, foot FLAT (untrained) | Horizontal forward at hip height | Body leans BACKWARD (opposite of swipe's forward fall), foot is FLAT (not flexed like a trained kick), both arms flailing WIDE for balance, supporting knee visibly buckling — the only leg attack + the only backward body lean |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 = body falls FORWARD into the hit, front leg crosses center, rear arm trails behind. atk2 = body leans BACK 30°, leg straight forward, both arms wide. Opposite body angles — if both look like "kid stumbling," redraw atk1 forward-falling and atk2 with the body clearly rocked back.
> - **atk2 vs kick discipline:** the foot must be FLAT (toes pointed forward, not pulled back). A trained kick would have a flexed foot — Runner doesn't know how. If the foot is flexed, redraw flat to show the lack of training.
> - **Over-commitment rule:** both attacks must look like the body is going to FALL after — F4 of each shows him stumbling, never returning to balanced stance. If F4 shows a balanced recovery, redraw — the over-commitment IS the character.
> - **Red bandana visibility:** the bicep bandana must be visible in every attack frame. atk1 lets it streak horizontally as the arm swings; atk2 lets it sit on the bicep with the arms flailing wide. If the bandana is hidden behind the body in any frame, reorient so it shows.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> **One sheet = one specific person.** Every cell in the sheet must show the **same individual** with the same skin tone, same hair, same head silhouette, same clothing colors.
>
> Variety across spawns is handled at runtime by the engine (per-spawn tint + variant lookup). **Do not vary the character within the sheet itself.**
>
> Pick ONE option from each list below and lock it for every frame:
> - **Skin tone:** ONE of `#c89478` (medium-light) / `#8a6248` (medium) / `#5a3a28` (dark)
> - **Hair:** ONE of (a) short black buzz cut, (b) short dark-brown fade, (c) dark hood pulled up
> - **Headwear:** EITHER no headwear OR the hood up — pick one and stick with it
> - **Hoodie zip state:** zipped halfway, all frames
> - **Red bandana on right bicep:** present in every frame
>
> Frame-to-frame, only **pose** changes. Hair, clothes, skin, accessories — identical.

## Physical

- **Age range:** 18–24
- **Height/build:** 5'8" – 6'0", lean to wiry. Not athletes. Just willing.
- **Skin tone:** **Locked per sheet** — pick one tone from the palette and use it on every frame. Spawn-variety is handled by the engine at runtime, not by varying frames within the sheet.
- **Body language:** Cocky on approach, panicked when hit. Knees bent forward, hands raised but loose.
- **Face:** Young. Stubble or clean-shaven — pick one and lock it across all frames. Don't show fear in idle — show it in `hurt`.

## Hair

- Short and **identical across every frame** of this sheet. Pick ONE: black buzz cut, dark-brown fade, or hood-up (no hair shown). If you want to ship alternates, make separate sheets (`runner_a.png`, `runner_b.png`) — never mix looks inside one sheet.

## Costume (head to feet)

1. **Hoodie / windbreaker** — dark grey (`#36363f`), zipped halfway. The hood is up on most variants.
2. **T-shirt / tank** under, off-white or dark grey, visible at the hem.
3. **Cargo pants** — navy (`#2f3a4a`), loose. Some have a chain wallet (1px gold streak at hip).
4. **Sneakers** — black or grey. Worn.

## Identity item — REQUIRED IN EVERY FRAME

**A red bandana, knotted around the right bicep.** This is Kane's neighborhood-liaison uniform tag — every Runner wears it so the police know not to roust them. 4–5 px wide stripe of marigold-red (`#a83040`) around the upper arm. Visible in all frames.

## Palette (hex)

```
hoodie (mid)       #36363f
hoodie (shadow)    #23232a
shirt              #cfc8b8
pants (mid)        #2f3a4a
pants (shadow)     #1f2838
shoe               #18181c
skin (light)       #c89478   (vary per spawn)
skin (shadow)      #8a6248
hair               #1a1410
RED BANDANA mid    #a83040
RED BANDANA hi     #c84a58
RED BANDANA shadow #6a1828
```

## Personality / fighting style

- **Cocky.** Approaches with a swagger, hands low. Doesn't expect a fight.
- **Hit-and-run.** After every swipe, backpedals 30 px. Doesn't sit in the protagonist's range.
- **Panicked at low HP** — flees toward the screen edge, no strategy.
- **Two signature moves — wild swipe + sloppy kick. Both moves OVER-COMMIT — the character literally falls forward into his attacks because he has no training.**
  - **`wild_swipe` — Overhand haymaker.** A street-fighter's overhand haymaker thrown with no technique at all. **Visual signature: the body OVER-COMMITS** — front leg crosses past the body line, rear shoulder flies up, rear arm flails behind for balance. He looks like he's falling forward more than punching. **The red bicep bandana streaks horizontally** through the swing as the arm trails behind the fist.
  - **`sloppy_kick` — Untrained front kick.** A kick thrown by someone who has never been taught how. **Visual signature: F3 the kicking leg extends forward but the body LEANS BACK 30° (no balance) with both arms wildly flailing outward, the kicking foot is FLAT (not pulled back like a trained kick), and the supporting leg is visibly buckling at the knee. He'll fall on his back if he misses.** Reads as "tough-kid energy without skill." 10 dmg.

## Animations (8 frames each unless noted)

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | Cocky tilt. Hands at hip level, palms loose (not fists). Weight on the back foot, **front foot tapping** — itchy energy. |
| `walk`   | 6 | **Loose swagger that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 = LEFT leg fwd + RIGHT arm fwd swing (at side). F2 = passing. F3 = RIGHT leg fwd + LEFT arm fwd swing. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. Shoulders roll with each step. **Hands stay LOW at the sides, swinging in a relaxed arc** — never extended forward (that would read as the wild_swipe wind-up). No planted/stomp foot on F6. |
| `run`    | 4 | 4-frame loop. F1: LEFT foot strike + right arm fwd swing. F2: airborne, arms pumping at sides. F3: RIGHT foot strike + left arm fwd swing. F4: airborne — blends into F1. **Arms PUMP at the sides** (elbows bent, hands at hip-to-chest height) — NEVER extend forward (would read as swipe/tackle). Bandana visible on the back-swing of the rear arm. Body upright (not athletic crouch). |
| `atk1`   | 4 | **Wild swipe.** F1 = shoulder DIP back and DOWN (the unmistakable wind-up). F2 = body lunges forward, front leg crossing past center. F3 = **full extension — fist 18 px past the body, rear arm flailing behind, bandana streaking horizontally through the swing**. F4 = stumble-back recovery, body over-balanced. |
| `atk2`   | 4 | **Sloppy kick.** F1 = kicking leg starts lifting, body already leaning back 15°. F2 = leg rising, body leaning back further, arms starting to flail. F3 = **peak — kicking leg extended forward at hip height with foot FLAT (not flexed), body leaned back 30°, both arms flailing wide for balance, supporting knee visibly buckling**. F4 = stumble — kicking leg drops, body over-balanced, arms still wide. |
| `hurt`   | 3 | Body folds at the waist. Face shows **fear** (eyebrows up, mouth open). Hands fly up. |
| `dead`   | 3 | Falls flat onto the back, arms splayed. |
| `flee`   | 4 | Same as run but body lower, head tucked, **looking back over the shoulder** on F2 and F4 — the panic-glance. |

## DO NOT include

- **Different versions of the runner across frames** — hair, headwear, skin tone, clothing colors must be identical in every cell.
- **Baked-in text** — no animation labels (`idle`, `walk`, `atk1`), no frame numbers (`F1`, `F2`), no row headers. The cell must contain ONLY the character.
- **Cell separator lines** — no grid lines, no borders. Cells are defined by even spacing, not drawn lines.
- Tactical gear / military look — these are *kids*, not soldiers.
- Visible weapons — Runners brawl bare-handed. (Slice is the knife guy; Lamplight is the gun guy.)
- The yellow bandana from Rio (different character, different color, different wrist).
- Glowing energy / elemental effects.

## Visual VFX summary

Runner's identity is the **over-committed body posture** + red bicep bandana streaking horizontally through swings. No technique — he literally falls forward into his hits. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so the swipe and the kick never blur together.

- `atk1` WILD SWIPE — body over-commits FORWARD with the front leg crossing past the body line + lead arm in an overhand haymaker arc + rear arm flails BEHIND for balance + red bicep bandana 12-px horizontal streak through the swing
- `atk2` SLOPPY KICK — body leans BACK 30° (opposite of swipe's forward fall), kicking leg straight forward at hip height with the FOOT FLAT (not flexed — he doesn't know how), both arms flailing wide, supporting knee visibly buckling

**Hurt / flinch:** F1 body folds at the waist, face shows FEAR (eyebrows up, mouth open). F2 hands fly up defensively. 1-px white impact spark.

**Dead:** Falls flat onto back, arms splayed. Bandana visible against the ground.

## Sheet specs

- 8 columns × 4 rows uniform grid (32 cells, ~28 frames used)
- Cell size: **48 × 64** (smaller than playable chars — these are mooks)
- Background: solid magenta (`#ff00ff`) for keying
- Bottom-center anchor

When the sheet lands, save as `characters/runner.png` and add a `runner_layout.json` per the same pattern as the playable characters.
