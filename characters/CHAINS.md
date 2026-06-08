# CHAINS

Kane's crowd-control specialists. Recruited from biker gangs and salvage-yard work crews. They swing a chain because it makes a wide hitbox, keeps everyone at arm's length, and looks like the kind of thing someone walks into a Block fight expecting to lose.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **7 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — bullwhip swing (6 frames)
> 4. `atk2` — boot-sweep (5 frames)
> 5. `atk3` — centrifuge spin (12 frames)
> 6. `hurt` (3 frames)
> 7. `dead` (3 frames)
>
> **Total: 39 frames in 7 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.

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

- **Holds ground.** Doesn't chase the protagonist; lets them come. Plants his feet wide and dares you to walk into the chain's reach.
- **Three attacks:**
  - **`swing` (default) — Bullwhip arc.** Side-armed horizontal swing. **Visual signature: at peak, the chain forms a full taut arc from his fist out 36 px past his body**, links visibly stretched in the apex curve. Body torques 45° with the swing, far shoulder pulled back, near shoulder thrown forward. The chain is the obvious silhouette — read from across the screen. 12 dmg, 140 knockback.
  - **`low_sweep` — Boot-sweep low kick.** A heavy bouncer's leg sweep at ankle height. **Visual signature: F3 he DROPS to one knee, supporting hand braced on the floor, free leg extended HORIZONTALLY at ankle height in a 120° sweeping arc. The chain trails behind the sweeping leg as a secondary low-arc trail — chain follows the kick.** 11 dmg + 60 knockback. Trips the target.
  - **`spin` (every 3rd attack) — Centrifuge.** Full 360° spin with the chain at full extension. **Visual signature: across F4–F11 the chain traces a complete halo around his body** — a circle of motion-blur, with the chain itself visible at 4 cardinal points (12 / 3 / 6 / 9 o'clock) across the eight active frames. His head stays facing forward (spotting like a dancer) while the body rotates underneath. Hits BOTH sides simultaneously. Multi-hit (3 across the window). 14 dmg per hit. Protagonist can't sidestep — must jump or back away.
- **Doesn't talk much.** Grunts on swings.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | **Wide planted stance** — feet shoulder-width plus. Slow shoulder rise on breath. Chain hangs from the wrist-wrap and swings 1–2 px with each breath. Free hand on his hip. |
| `walk`   | 6 | Heavy gait. **Chain trails 1 frame behind** the rear-swinging arm. Boots strike flat-footed. |
| `atk1`   | 6 | **Bullwhip swing.** F1 = arm cocks back, chain pools at the rear. F2 = shoulder rotates back further, chain pulled tight behind. F3 = **forward arc — chain fully extended in a horizontal taut line 36 px past body, body torqued 45°**. F4 = chain past target (3-px motion blur on the tip). F5 = arm follow-through. F6 = recovery, chain re-pools. |
| `atk2`   | 5 | **Boot-sweep.** F1 = body drops, knee lowering toward ground. F2 = body crouched, **supporting hand braced on the floor**, free leg starting to sweep. F3 = **peak — body low, supporting hand on floor, free leg horizontal at ankle height in a 120° sweeping arc, chain trailing behind the sweeping leg as a low secondary arc**. F4 = leg past midline, body following the rotation. F5 = recovery, back to stance. |
| `atk3`   | 12 | **Centrifuge spin.** F1–F3 = body coils, chain starts swinging up. F4 = chain at 12, body starts spinning. F5–F11 = full 360° rotation — chain visible at one cardinal point per frame with motion blur tracing the arc (3 → 6 → 9 → 12 → 3). **Head faces forward through the entire spin** — spotted like a ballet turn. F12 = stop, chain re-pools at the side. |
| `hurt`   | 3 | Stagger. Chain drops slack 4 px on F2. |
| `dead`   | 3 | Falls forward to one knee, then onto the side. **Chain pools beneath body in a coiled S-shape.** |

## DO NOT include

- **Text inside cells** — no anim labels, no row headers, no frame numbers.
- **Cell separator lines.**
- **Variation of Chains across frames** — same person, same arm-wrap, same beard.
- Multiple chains / nunchaku style — single chain only.
- Spike studs on the chain — keep it industrial, not cartoony fantasy.
- Tactical / military gear — Chains are blue-collar, not soldiers.
- A face mask — Chains is *recognizable*. He doesn't hide.

## Visual VFX summary

Chains' identity is the **chain motion-blur trail** + sparks where the chain hits the ground.

- `swing` bullwhip arc — chain fully extended in horizontal taut line 36 px past body, body torqued 45°
- `spin` centrifuge — chain traces a complete halo around his body (motion-blur circle, visible at 4 cardinal points across the spin frames)
- `low_sweep` boot-sweep — body low, supporting hand on the floor, free leg sweeping in 120° arc at ankle height, chain trailing as a low secondary arc

**Hurt / flinch:** F1 stagger, chain drops slack 4 px. F2 free hand goes to the wound. 1-px white impact spark.

**Dead:** Falls forward to one knee, then onto the side. Chain pools beneath the body in a coiled S-shape.

## Sheet specs

- 8 columns × 5 rows = 40 cells (~36 frames used; spin needs 12)
- Cell size: **64 × 80**
- Magenta `#ff00ff` background
- Bottom-center anchor — chain should always be visible in silhouette
