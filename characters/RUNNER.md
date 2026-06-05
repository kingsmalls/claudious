# RUNNER

Kane's bottom-tier muscle. Recruited from Kane's "neighborhood liaison" jobs program — a euphemism for a paycheck in exchange for nights like this one. Most of them are going to wake up tomorrow regretting being here. They don't know that yet.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> **One sheet = one specific person.** Every cell in the sheet must show the **same individual** with the same skin tone, same hair, same head silhouette, same clothing colors. The previous Runner sheet failed because hair colour and headwear changed between cells (blonde in some frames, dark in others, baseball cap in some, hood in others) — this reads as "the character is glitching" in motion.
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
- One attack: a wild forward swipe (a haymaker, telegraphed by a shoulder dip).

## Animations (8 frames each unless noted)

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | Slight sway. Hands at hip level. Cocky tilt. |
| `walk`   | 6 | Loose stride. |
| `run`    | 4 | Limbs flail. Bandana visible on the rear arm during the back-swing. |
| `atk1`   | 4 | Forward swipe. Frame 1 = wind-up shoulder dip; frame 3 = full extension. |
| `hurt`   | 3 | Body folds. Face shows fear. |
| `dead`   | 3 | Falls flat onto back, knockback drift. |
| `flee`   | 4 | Same as run but body lower, head ducked. |

## DO NOT include

- **Different versions of the runner across frames** — hair, headwear, skin tone, clothing colors must be identical in every cell. This is the #1 reason previous sheets read as "broken" in motion.
- **Baked-in text** — no animation labels (`idle`, `walk`, `atk1`), no frame numbers (`F1`, `F2`), no row headers. The cell must contain ONLY the character.
- **Cell separator lines** — no grid lines, no borders. Cells are defined by even spacing, not drawn lines.
- Tactical gear / military look — these are *kids*, not soldiers.
- Visible weapons — Runners brawl bare-handed. (Slice is the knife guy; Lamplight is the gun guy.)
- The yellow bandana from Rio (different character, different color, different wrist).
- Glowing energy / elemental effects.

## Sheet specs

- 8 columns × 4 rows uniform grid (32 cells, ~28 frames used)
- Cell size: **48 × 64** (smaller than playable chars — these are mooks)
- Background: solid magenta (`#ff00ff`) for keying
- Bottom-center anchor

When the sheet lands, save as `characters/runner.png` and add a `runner_layout.json` per the same pattern as the playable characters.
