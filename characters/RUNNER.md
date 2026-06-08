# RUNNER

Kane's bottom-tier muscle. Recruited from Kane's "neighborhood liaison" jobs program — a euphemism for a paycheck in exchange for nights like this one. Most of them are going to wake up tomorrow regretting being here. They don't know that yet.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **8 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `run` (4 frames)
> 4. `atk1` — wild swipe (4 frames)
> 5. `atk2` — sloppy kick (4 frames)
> 6. `hurt` (3 frames)
> 7. `dead` (3 frames)
> 8. `flee` (4 frames)
>
> **Total: 32 frames in 8 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.

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
| `walk`   | 6 | Loose swagger. Shoulders roll with each step. **Hands stay low**, not raised — he's not expecting to fight. |
| `run`    | 4 | Limbs flail. Bandana visible on the back-swing of the rear arm. Body upright (not athletic crouch). |
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

Runner's identity is the **over-committed body posture** + red bicep bandana streaking horizontally through swings. No technique — he literally falls forward into his hits.

- `swipe` wild haymaker — front leg crosses past body line, rear arm flails behind for balance, bandana 12-px horizontal streak through the swing
- `tackle` body slam — body fully horizontal mid-air, both arms forward like a football tackle, motion lines behind the feet
- `kick` panicked kick — body leans BACK 30° (no balance), kicking foot FLAT (not flexed), both arms flailing wide, supporting knee visibly buckling

**Hurt / flinch:** F1 body folds at the waist, face shows FEAR (eyebrows up, mouth open). F2 hands fly up defensively. 1-px white impact spark.

**Dead:** Falls flat onto back, arms splayed. Bandana visible against the ground.

## Sheet specs

- 8 columns × 4 rows uniform grid (32 cells, ~28 frames used)
- Cell size: **48 × 64** (smaller than playable chars — these are mooks)
- Background: solid magenta (`#ff00ff`) for keying
- Bottom-center anchor

When the sheet lands, save as `characters/runner.png` and add a `runner_layout.json` per the same pattern as the playable characters.
