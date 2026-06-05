# CHAINS

Kane's crowd-control specialists. Recruited from biker gangs and salvage-yard work crews. They swing a chain because it makes a wide hitbox, keeps everyone at arm's length, and looks like the kind of thing someone walks into a Block fight expecting to lose.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> Cells must contain only the character — no labels, no row headers, no frame numbers, no cell borders.
>
> One specific Chains across every cell: same beard, same vest, same arm-wrap of chain. Only the pose changes.

## Physical

- **Age range:** 30–45
- **Height/build:** 6'0" – 6'3", broad-shouldered, blocky. Heavyset but not soft.
- **Body language:** Stands with the chain hanging loose from the right hand, the slack pooled at the boots. Subtle wind-up sway when about to swing.
- **Face:** Hard. Some have full beards, some clean-shaven with a goatee. Often a cigar between teeth (decoration, not lit).

## Hair

- Long, tied back into a low ponytail, OR shaved entirely. Two distinct silhouettes — pick one per spawn.

## Costume (head to feet)

1. **Sleeveless leather vest** — black (`#16100a`), open in front showing a stained tank top.
2. **Tank top** — off-white or grey (`#9b9482`), tight.
3. **Heavy work jeans** — dark indigo (`#2a2e3a`), worn knees.
4. **Steel-toed work boots** — black with grey toe caps (`#0a0a10` with `#5a5a5a` toes).
5. **Wide leather belt** with a square brass buckle (`#cfa040`).

## Identity item — REQUIRED IN EVERY FRAME

**A heavy industrial chain wrapped twice around the dominant forearm, free end ~30 px long held in the fist.** Steel-grey links (`#7a7a82`) with darker shadow (`#3a3a40`). The chain swings during all motion frames — it has *weight*, it lags behind body movement by 1 frame. During the swing attack, the chain extends to its full length (~50 px) in a horizontal arc.

## Palette (hex)

```
vest leather       #16100a
tank top           #9b9482
jeans              #2a2e3a
jeans shadow       #191c26
boot               #0a0a10
boot toe (steel)   #5a5a5a
belt               #4a3020
belt buckle        #cfa040
skin (light)       #c89478    (vary)
skin (shadow)      #8a6248
hair               #1a1410
chain link mid     #7a7a82
chain link hi      #cfd0d6
chain link shadow  #3a3a40
```

## Personality / fighting style

- **Holds ground.** Doesn't chase the protagonist; lets them come.
- **Two attacks:**
  - `swing` (default) — long-reach horizontal swing. Chain extends 28–38 px forward.
  - `spin` (every 3rd attack) — full 360° spin with the chain at full extension. Hitbox covers BOTH sides of Chains' body simultaneously. Multi-hit (3 hits across the active window). The protagonist can't sidestep through it — must jump or back away.
- **Doesn't talk much.** Grunts on swings.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | Slow shoulder rise on breath. Chain swings 1–2 px with each breath. |
| `walk`   | 6 | Heavy gait. Chain trails behind 1 frame. |
| `atk1`   | 6 | Swing: F1–F2 = arm cocks back, chain pools, F3 = forward arc with chain fully extended, F4–F6 = follow-through. |
| `atk2`   | 12 | Spin: F1–F3 = body coils, F4–F11 = body rotates 360° once, chain traces full arc all around (motion-blur on chain), F12 = recovery. |
| `hurt`   | 3 | Stagger. Chain drops slack 4 px. |
| `dead`   | 3 | Falls. Chain pools beneath body. |

## DO NOT include

- **Text inside cells** — no anim labels, no row headers, no frame numbers.
- **Cell separator lines.**
- **Variation of Chains across frames** — same person, same arm-wrap, same beard.
- Multiple chains / nunchaku style — single chain only.
- Spike studs on the chain — keep it industrial, not cartoony fantasy.
- Tactical / military gear — Chains are blue-collar, not soldiers.
- A face mask — Chains is *recognizable*. He doesn't hide.

## Sheet specs

- 8 columns × 5 rows = 40 cells (~36 frames used; spin needs 12)
- Cell size: **64 × 80**
- Magenta `#ff00ff` background
- Bottom-center anchor — chain should always be visible in silhouette
