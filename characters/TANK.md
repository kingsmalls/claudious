# TANK

Kane's heavy enforcer. Ex-prison-yard fighters and former bouncers Kane bought out of debt. They don't move fast and they don't talk much. Their job is to be the wall between Kane's interests and anyone who won't move.

## Physical

- **Age range:** 35–50
- **Height/build:** 6'2" – 6'5", massive. 280–320 lbs of muscle gone soft in the gut. Not as tall as Atlas; broader.
- **Skin tone:** Varies; default to weathered olive/brown.
- **Body language:** Rooted. Plants both feet shoulder-width minimum. Doesn't bounce, doesn't shift — *stands*. Arms loose at his sides, ready to backhand.
- **Face:** Heavy brow. Broken nose (multiple times). Resting expression: bored.

## Hair

- Shaved head or buzzed close. Most have full beards, untrimmed.

## Costume (head to feet)

1. **Tactical vest** over a plain black t-shirt — slate grey (`#3a4050`) with utility straps. The vest is plates-rated. Empty pouches on the front (no weapons; he doesn't need them).
2. **Heavy duty cargo pants** — black (`#1a1a22`).
3. **Combat boots** — black, steel-toed, scuffed. Heavy soles that thump on impact.

## Identity item — REQUIRED IN EVERY FRAME

**A laminated ID badge clipped to the front-left of the vest.** Reads "KANE PROPERTIES SECURITY." White rectangle with a small red logo (`#a83040`). 6 × 4 px. The badge is what makes him *legal* — Kane gives him paperwork so the cops won't intervene. Visible at all times, even when knocked down.

## Palette (hex)

```
vest (mid)         #3a4050
vest (shadow)      #1f2530
shirt              #1a1a22
pants              #161618
boot               #0a0a10
boot sole          #08080a
skin (light)       #a87858
skin (shadow)      #6a4830
beard              #2a2520
ID badge white     #f4f4f0
ID badge red       #a83040
strap brown        #4a3a28
```

## Personality / fighting style

- **Slow and inevitable.** Walks at half speed. Doesn't run.
- **Super-armor through hits.** Takes 3 hits before flinching (engine: `staggerN: 3`). The protagonist learns to commit to a heavy or wait for the wind-up gap.
- **Signature move — `slam`: Two-handed sledgehammer drop.** Both massive arms raise OVERHEAD with **fists clasped together**, body coils backward like a question mark, then crashes down. **Visual signature: at peak the silhouette reads as a pyramid — wide feet planted, both arms straight up overhead, fists meeting at the top, body arched slightly backwards**. The pose is unmistakable from across the screen — "incoming danger." Dust falls *downward* from his boots during the wind-up because the ground is already shaking under him. Ground-rumble specks radiate from his stance on F2–F3.
- **Doesn't speak.** Loud nasal grunts on the slam impact.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | **Wide planted stance** — feet outside shoulder width. Slow chest rise on breath. Arms hang loose, fists half-clenched. Vest **badge catches a 1-px gold highlight**. |
| `walk`   | 6 | **Heavy stomp gait** — boots flat-footed. Body barely sways. **Dust puff (1–2 brown specks) at the planted heel on every step**. Vest jiggles 1 px on impact. |
| `atk1`   | 7 | **Sledgehammer slam.** F1 = both arms start rising, knees bending. F2 = arms above head, fists clasping, body coiled back (ground-rumble specks at his feet). F3 = **peak pyramid pose — feet wide, both arms vertical overhead, fists meeting, body arched backwards**. F4 = drive down (body folds at the waist, both fists crash at chest-height of target) — **dust burst, 5–6 brown specks in a half-circle at his feet**. F5 = follow-through, body bent forward, fists at thigh height. F6 = straighten. F7 = recovery to stance, badge re-catches highlight. |
| `hurt`   | 3 | Body absorbs, **barely flinches** — head turns 5°, vest doesn't move. (At full HP he's almost unimpressed.) |
| `dead`   | 4 | Falls hard like a tree — F1 folds at the knees, F2 falls to one knee (dust puff), F3 collapses sideways, F4 face down. |

## DO NOT include

- Athletic / spring-loaded movement.
- Firearms or knives — Tanks brawl with their hands.
- Trimmed beard or styled hair.
- The KANE PROPERTIES badge replaced by anything else, ever.

## Sheet specs

- 6 columns × 4 rows = 24 cells (24 frames used)
- Cell size: **64 × 80** — Tank reads as big in silhouette
- Solid magenta `#ff00ff` background
- Bottom-center anchor
