# RAZOR — Stage 6 Boss

Kane's white-collar specialist. Real name **Eliza Park.** Came up through corporate compliance and "private security" consulting before Kane found her. Her job is to *talk* a holdout into selling. The dual knives are for the people who think a polite conversation can't end this way.

She wears a tailored suit because she does most of her work in office buildings. The Block is the first job in years where she's had to use the knives.

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
- **Three attacks:**
  - `slash` — quick single-knife slash, 10 dmg, fast 4-frame startup.
  - `dash` — telegraphed forward dash with both blades extended. 16 dmg + 160 knockback. **Self-pushes 240 px.** She becomes a missile.
  - `throw` — at low HP (<40%), starts throwing knives. Spawns a `knife` projectile (12 dmg, 240 px/s).
- **Pattern:** mostly slash-slash-dash, occasional throws in phase 2.
- **Talks during fights:** "We could have done this in your kitchen." / "You're making this so much harder than it needs to be."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Hands clasped behind back. Suit perfectly clean. Subtle breath. |
| `walk`     | 6 | Heel-toe walk, steady tempo. Suit trails 1 px. |
| `draw`     | 4 | F1 = body shifts into fencing stance, F2–F3 = knives drawn from belt, F4 = ready pose with both blades forward. (Plays once on combat start.) |
| `atk1`     | 4 | Slash: fast forward cut with one blade. |
| `atk2`     | 9 | Dash: F1–F2 wind-up, F3 launch (motion lines), F4–F6 active (both blades extended), F7–F9 recovery. |
| `atk3`     | 5 | Throw: F1–F2 = arm cocked back, F3 = release (knife projectile spawned), F4–F5 = retract. |
| `hurt`     | 3 | Body twists. Suit stays clean. |
| `dead`     | 5 | Falls to one knee, then to the floor. Knives clatter. |
| `phase2`   | 4 | Brief tell when she crosses 40% HP — wipes blood off one knife with her sleeve, returns to stance. |

## DO NOT include

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
