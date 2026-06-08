# CHAINS

Kane's crowd-control specialists. Recruited from biker gangs and salvage-yard work crews. They swing a chain because it makes a wide hitbox, keeps everyone at arm's length, and looks like the kind of thing someone walks into a Block fight expecting to lose.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **7 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — BULLWHIP SWING (6 frames) — **CHAIN fully extended in a horizontal TAUT LINE 36 px past the body**, body torqued 45°, near shoulder thrown forward
> 4. `atk2` — BOOT-SWEEP (5 frames) — **body LOW with supporting hand braced on the floor**, free LEG horizontal at ankle height in a 120° sweeping arc, chain trailing as a low secondary arc
> 5. `atk3` — CENTRIFUGE SPIN (12 frames) — **full 360° spin with the CHAIN tracing a complete HALO around the body** (motion-blur circle, chain visible at four cardinal points across the spin frames)
> 6. `hurt` (3 frames)
> 7. `dead` (3 frames)
>
> **Total: 39 frames in 7 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Chains has three chain-attacks and the generator's failure mode is **all three reading as "guy swinging chain horizontally."** Each must occupy a different silhouette quadrant — the chain's PATH and the body's POSTURE must differ between them. If two attacks share a silhouette, redraw one:
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` bullwhip swing | Vertical, body torqued 45° at the hip | Wrapped arm + CHAIN | Horizontal TAUT line at chest height | Chain is a STRAIGHT TAUT LINE 36 px past the body (single side, not a circle), body torqued 45° showing the swing through, free hand on hip — only attack with the chain extended on ONE side as a straight line |
> | `atk2` boot-sweep | Body LOW (dropped to one knee), supporting HAND on the floor | Free LEG at ankle height | Horizontal ankle-height ARC | Body LOW to the ground with supporting HAND BRACED ON FLOOR (the only attack that touches the ground with the hand), free leg sweeping at ankle height — chain trails as a SECONDARY LOW ARC behind the leg, not the primary weapon |
> | `atk3` centrifuge spin | Vertical, body rotating through 360° with head SPOTTED forward | Wrapped arm extended + CHAIN | Horizontal at chest height, FULL CIRCLE around the body | Chain forms a complete HALO around the body (visible at 12 / 3 / 6 / 9 o'clock across the spin frames) + head stays FACING FORWARD while the body rotates (the ballet-spot tell) — the only attack with the chain as a full circle |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk3:** atk1 = chain straight TAUT LINE on ONE side of the body, body torqued 45° once. atk3 = chain HALO all the way around the body, body spinning 360°. If atk3 frames look like atk1 with extra speedlines, redraw — atk3's chain must visibly continue past the body to the opposite side, forming a circle across the active frames.
> - **atk2 vs anything else:** atk2 is the ONLY attack where Chains drops LOW with his supporting hand on the FLOOR. If F3 doesn't show the hand braced on the ground with the body crouched, the sweep isn't reading — redraw.
> - **atk1 chain vs atk2 chain:** atk1's chain is at CHEST height in a STRAIGHT LINE. atk2's chain is at ANKLE height trailing the sweeping leg (secondary low arc). Different heights, different roles. If both look identical at chest height, atk2's chain isn't dropped low enough — redraw.
> - **atk3 head-spotting rule:** atk3's head must face FORWARD across every spin frame even as the body rotates underneath (ballet-spot mechanic). If the head rotates with the body, the spin reads as just dizzy — redraw with the head locked forward.
> - **Chain-wrap rule:** the heavy industrial chain is wrapped twice around the dominant forearm in EVERY frame including hurt and dead. If any frame shows a bare forearm, redraw — the chain wrap is identity.

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
| `walk`   | 6 | **Heavy gait that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 = LEFT leg fwd + RIGHT arm fwd swing (at side). F2 = passing. F3 = RIGHT leg fwd + LEFT arm fwd swing. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. **Both arms swing in a relaxed arc at the sides** — the chain-wrapped arm swings too (the chain trails 1 frame behind that arm). Arms NEVER extend forward (would read as bullwhip swing wind-up). Boots strike flat-footed. No planted/stomp pose on F6. |
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

Chains' identity is the **chain motion-blur trail** + sparks where the chain hits the ground. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so the swing, the sweep, and the spin never blur together.

- `atk1` BULLWHIP SWING — chain fully extended in a horizontal TAUT LINE 36 px past the body (single side, straight line), body torqued 45° showing the swing through, free hand on hip — the only attack with the chain as a straight one-sided line
- `atk2` BOOT-SWEEP — body LOW with supporting HAND BRACED ON THE FLOOR, free leg horizontal at ankle height in a 120° sweeping arc, chain trailing behind the leg as a SECONDARY LOW ARC (chain at ankle height, not chest height) — the only attack that touches the ground with the hand
- `atk3` CENTRIFUGE SPIN — chain traces a complete HALO around the body (motion-blur circle, visible at 12 / 3 / 6 / 9 o'clock across the spin frames), head stays FACING FORWARD while the body rotates underneath (ballet-spot) — the only attack with the chain as a full circle + the only multi-hit AOE

**Hurt / flinch:** F1 stagger, chain drops slack 4 px. F2 free hand goes to the wound. 1-px white impact spark.

**Dead:** Falls forward to one knee, then onto the side. Chain pools beneath the body in a coiled S-shape.

## Sheet specs

- 8 columns × 5 rows = 40 cells (~36 frames used; spin needs 12)
- Cell size: **64 × 80**
- Magenta `#ff00ff` background
- Bottom-center anchor — chain should always be visible in silhouette
