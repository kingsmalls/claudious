# RAZOR — Stage 6 Boss

Kane's white-collar specialist. Real name **Eliza Park.** Came up through corporate compliance and "private security" consulting before Kane found her. Her job is to *talk* a holdout into selling. The dual knives are for the people who think a polite conversation can't end this way.

She wears a tailored suit because she does most of her work in office buildings. The Block is the first job in years where she's had to use the knives.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> **Sheet must be on solid magenta `#ff00ff`** (or fully transparent PNG). White backgrounds will not chroma-key out and will render as rectangles around the character.
>
> **No drawn cell separators of any kind** — no white lines, no borders, no grid. Cells are defined by even pixel spacing only.
>
> Razor stays **identical** across every cell: same bob cut, same suit colors, same dual knives. Only the pose changes.

## Physical

- **Age:** 38
- **Height/build:** 5'7", lean, athletic but not muscular. Yoga / kickboxing build.
- **Skin:** Korean. Light olive (`#dcb088`).
- **Body language:** Composed. Hands clasped behind her back in idle. Walks calmly, no rush. When she draws the knives, the body language shifts to a fencing stance — front foot 45°, back foot perpendicular.
- **Face:** Sharp jawline, dark eyes, neutral resting expression. A small, deliberate smile when she lands a hit.

## Hair

- Black, sleek, **straight bob** ending at the jawline. **Two small streaks of bleached blonde** on either side at the front (one each side, ~3 px wide). The blonde streaks are her tell — small detail visible in every frame.

## Costume (head to feet)

1. **Tailored black suit jacket** — fitted, two-button, single vent. Lapels visible. No shirt collar peeking; the jacket is buttoned over a black silk shell.
2. **Black silk camisole** under, V-neck.
3. **Slim black slacks** — straight cut to the ankle.
4. **Black low-heeled oxford-style shoes** — polished. Sound silent on hard floors.
5. **Black leather gloves** — fitted, fingers exposed only at the tips.

## Identity items — REQUIRED IN EVERY FRAME

1. **Two folding knives** — one in each hand during attacks; sheathed at the small-of-back belt during idle/walk. **Blades:** ~10 px, dark steel (`#cfd0d6`) with mirror-bright edge highlight (`#ffffff`). **Handles:** dark grey (`#2a2a2f`) with a deep burgundy inlay (`#4a1018`).
2. **The bleached blonde streaks** in her hair (described above).
3. **A small lapel pin** on the jacket — a stylized "K" logo (Kane Properties). Gold (`#f4c860`), ~2 × 3 px. Visible on the left lapel in every frame.

## Palette (hex)

```
suit jacket black  #1a1a22
suit shadow        #08080a
suit highlight     #2a2a32
silk camisole      #16161a
slacks             #1a1a22
shoe               #0a0a10
glove leather      #16100a
skin (light)       #dcb088
skin (shadow)      #a07858
hair black         #1a1410
hair blonde streak #c8a060
knife blade        #cfd0d6
knife edge hi      #ffffff
knife handle       #2a2a2f
knife handle inlay #4a1018
lapel pin gold     #f4c860
lapel pin shadow   #8a6020
```

## Personality / fighting style

- **Calm. Polite. Lethal.**
- **Three signature moves — slash / dash / throw. The dual blades are the visual identity. Both knives are visible in every combat frame.**
  - **`slash` — Cross-cut.** Single-knife forward slash drawn DIAGONALLY across the body. **Visual signature: F2–F3 shows a 28-px diagonal red-tinted arc from upper-right to lower-left** drawn by the blade tip (motion-blur tracing). The other knife stays in fencing-guard at the hip. Body in fencing posture — front foot leading, rear arm angled behind. 10 dmg. Fast 4-frame startup.
  - **`dash` — Missile.** Telegraphed forward dash with BOTH blades extended. **Visual signature: F4–F6 silhouette is an X-shape — body fully horizontal at chest height, both arms extended forward with blades leading, legs trailing horizontally behind**. Two horizontal motion-line streaks behind the heels. She becomes a literal missile. 16 dmg + 160 knockback. Self-pushes 240 px.
  - **`throw` — Released knife.** At low HP (<40%), starts throwing knives. **Visual signature: F3 the knife has just released — it's drawn 18 px ahead of her hand with a thin 6-px motion-line behind it, blade angled at 30° pointing forward**. She remains in throwing stance with the released arm forward, rear arm cocked. Spawns a `knife` projectile (12 dmg, 240 px/s).
- **Pattern:** mostly slash-slash-dash, occasional throws in phase 2.
- **Talks during fights:** "We could have done this in your kitchen." / "You're making this so much harder than it needs to be."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | **Hands clasped behind back, knives concealed.** Suit perfectly clean. Subtle breath (1-px shoulder rise on F2). Heels together, toes splayed slightly (formal posture). |
| `walk`     | 6 | **Heel-toe walk, steady tempo.** Suit trails 1 px. Hands stay clasped behind back. |
| `draw`     | 4 | F1 = body shifts into **fencing stance** (front foot lead, rear foot perpendicular). F2 = knives drawn from belt sheaths. F3 = **ready pose — front blade horizontal forward at hip height, rear blade vertical guard at the shoulder**. F4 = settle into stance. (Plays once on combat start.) |
| `atk1`     | 4 | **Cross-cut slash.** F1 = front blade cocks back over right shoulder. F2 = **diagonal slash begins, blade tip tracing 14 px down-and-left across the body**. F3 = peak — blade extended at hip level on the left, **28-px diagonal red-tinted motion arc visible from upper-right to lower-left** as the trail. F4 = return to fencing stance, both blades visible again. |
| `atk2`     | 9 | **Missile dash.** F1 = stance widens, both blades raise to shoulder-height-forward. F2 = body coils, blades fully forward. F3 = launch (body angles 45° forward, both knives leading). F4 = **body fully horizontal mid-air, both blades extended, legs trailing horizontally behind — X-shape silhouette**. F5 = held missile pose. F6 = X-shape continues, motion lines streaking behind. F7 = land, blades still extended. F8 = stance recovery. F9 = back to ready. |
| `atk3`     | 5 | **Knife throw.** F1 = body squares to target, rear arm cocks the knife at ear height. F2 = arm begins forward motion. F3 = **release — knife drawn 18 px ahead of the throwing hand, 6-px motion-line trail behind it, blade angled 30° pointing forward**. F4 = follow-through, throwing arm fully extended. F5 = return to stance. |
| `hurt`     | 3 | Body twists. **Suit stays clean.** Both knives stay in hand. |
| `dead`     | 5 | F1 = body folds. F2 = falls to one knee. F3 = collapses to side. **F4 = both knives slide 8 px from open hands.** F5 = settled. |
| `phase2`   | 4 | **Brief tell when she crosses 40% HP** — F1 = lifts one blade to her sleeve. F2 = wipes blood off the blade with the sleeve. F3 = examines the blade. F4 = returns to stance. |

## DO NOT include

- **White background** — must be magenta `#ff00ff` or transparent. White is NOT chroma-keyed by the importer.
- **Drawn cell separator lines / borders / grid lines** of any color. Cells are spaced, not bordered.
- **Frame numbers, anim names, or any text inside cells.**
- **Variation of Razor across frames** — same bob, same suit, same knives in every cell.
- Disheveled hair / wrinkled suit — Razor is *poised*. Even when hurt, she's neat.
- Visible piercings or tattoos — corporate-clean.
- Heavy makeup — minimal, sharp.
- Bright colors — black suit, only the gold pin and burgundy knife inlays break it.
- A second weapon style — knives only. No gun, no whip, no nonsense.

## Sheet specs

- 8 columns × 6 rows = 48 cells (~38 frames used)
- Cell size: **64 × 96**
- Magenta `#ff00ff` background
- Bottom-center anchor

## Boss-fight design notes

- HP ≈ 200.
- Music: continue Stage 6's `lantern` theme (mood-piece tension).
- Defeat: she sheaths the remaining knife, sits down on one of the shattered glass piles, says "Tell Kane I'm done." She doesn't fall.
