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
- **One attack: telegraphed slam.** 14-frame wind-up with visible ground-rumble particles. If it lands, big knockback and big damage.
- **Doesn't speak.** Grunts on impact.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | Slow chest rise. Stance wide. |
| `walk`   | 6 | Heavy stomp gait — boots strike flat-footed on each step. |
| `atk1`   | 7 | Slam: F1–F3 wind-up (arm raised overhead, body coiled), F4 swing peak, F5–F7 recovery. Ground rumble particles during F2–F3. |
| `hurt`   | 3 | Body absorbs, barely flinches. Head turns 5°. |
| `dead`   | 4 | Falls hard. Drop shadow grows. |

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
