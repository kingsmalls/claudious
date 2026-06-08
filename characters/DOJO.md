# DOJO

The disciplined ones. Kane found them at a martial-arts studio in financial trouble — paid the rent for a year and got the senior students on retainer. They don't enjoy this work the way Slice does. They treat the protagonist as an opponent, not an obstacle.

Of all Kane's crews, Dojo is the only one who *bows* before the fight.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **10 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — FRONT KICK / mae geri (4 frames) — **rear LEG drives STRAIGHT FORWARD horizontally** at chest height, FOOT FLEXED (toes pulled back), heel leading, body upright
> 4. `atk2` — ROUNDHOUSE / mawashi geri (5 frames) — **kicking leg HORIZONTAL at chest height with shin PARALLEL to ground**, body torqued 45°, top-of-foot leading
> 5. `atk3` — AXE KICK / kakato otoshi (6 frames) — **kicking leg STRAIGHT VERTICAL past the head** (180° leg extension splitting the silhouette), then HEEL drops straight down like a guillotine
> 6. `jump_atk` — FLYING SIDE KICK / tobi yoko geri (5 frames) — **AIRBORNE body fully HORIZONTAL mid-flight**, lead leg extended straight forward with the SIDE of the foot leading, rear leg tucked under
> 7. `guard` (3 frames)
> 8. `bow` (6 frames)
> 9. `hurt` (3 frames)
> 10. `dead` (4 frames)
>
> **Total: 46 frames in 10 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Dojo is the only character whose attacks are ALL kicks, which is exactly the failure mode — the generator falls back to "guy lifting a leg" for every move. Each kick must occupy a DIFFERENT silhouette quadrant. If two kicks share a silhouette, redraw one:
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` front kick | Vertical, body upright, slight 5° forward | Rear leg, FOOT FLEXED (toes back), HEEL leading | Horizontal STRAIGHT forward | Foot is FLEXED with toes pulled back — heel/ball of foot leads in a straight line; body stays upright facing forward |
> | `atk2` roundhouse | Torqued 45° sideways, hip rotated through | Kicking leg, TOP-OF-FOOT (instep) leading | Horizontal ARC at chest height from the OUTSIDE in | Shin parallel to the ground, body rotated 45° showing the hip drive, top-of-foot leading — only attack with the hip clearly torqued and the foot pointed (NOT flexed) |
> | `atk3` axe kick | Vertical, body leaned BACK slightly, then forward | Same leg whole 180° up then DOWN | Vertical UP then vertical DOWN | Leg STRAIGHT VERTICAL past the head at F3 (the leg splits the silhouette down the middle) — the only attack with the kicking leg ABOVE the head |
> | `jump_atk` flying side kick | AIRBORNE, body fully HORIZONTAL parallel to ground | Lead leg, SIDE of the foot leading | Horizontal forward at chest height (mid-air) | Only AIRBORNE kick + body fully horizontal in flight + side-of-foot leading (NOT heel like atk1, NOT instep like atk2) — an arrow silhouette |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 = STRAIGHT-LINE leg with the foot FLEXED (toes pulled back, heel leading); body stays squared forward. atk2 = ARCING leg with the foot POINTED (top-of-foot leading); body torqued 45° showing the hip rotation. If both kicks look like "leg out at chest height," redraw atk1 with the foot clearly flexed and the body squared, and atk2 with the shin clearly horizontal-parallel and the hip rotated.
> - **atk2 vs jump_atk:** atk2 is GROUNDED with the supporting foot planted and the body torqued. jump_atk is fully AIRBORNE with the body horizontal in flight and BOTH legs off the ground (lead extended, rear tucked under). If jump_atk shows a planted foot at peak, redraw — it must be airborne.
> - **atk3 vs anything else:** atk3 is the ONLY attack where the kicking leg goes STRAIGHT UP past the head (vertical leg pose). If atk3 shows the leg at chest height instead, redraw — the vertical-leg silhouette IS the move's identity.
> - **jump_atk vs flying knee (other characters):** Dojo does NOT throw a knee strike. The flying attack is a SIDE KICK with the lead leg straight forward, side-of-foot leading. If F3 shows a bent knee leading, redraw with the leg straight.
> - **No-punches rule:** Dojo NEVER throws a punch. Hands stay in knife-hand guard at chin/hip across every attack frame. If any attack shows the lead arm extending forward like a strike, redraw — the kick is always the weapon.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> **One specific Dojo across the entire sheet** — bow, walk, kick, hurt are all the same person. Pick once:
> - **Hair:** short black slicked back, OR short black topknot — choose ONE for the whole sheet.
> - **Build:** lean and athletic, identical proportions in every frame.
> - **Skin tone:** pick one and lock it.
> - **Gi:** plain black with white belt — same shade of black in every cell, no purple/maroon shifts.
>
> Frame-to-frame, **only pose changes**. The same person stands up, bows, walks, kicks, gets hurt.

## Physical

- **Age range:** 24–35
- **Height/build:** 5'8" – 5'11", athletic-toned. Visible deltoids and forearms but not bulky. Posture is *perfect* — every spawn looks like they trained for years.
- **Body language:** Centered. Stands in a formal stance with the front foot 30° off-center, weight 60/40 on the back foot. Hands raised in a guard. Eyes locked on the protagonist's center mass.
- **Face:** Calm. No smile. No scowl. Often Asian / South-Asian / mixed presentation; vary across spawns. Some have a small braided sidelock or a goatee — pick distinct silhouettes per spawn.

## Hair

- Tied back into a tight low ponytail OR shaved on the sides with a topknot. Two distinct looks — vary across spawns.

## Costume (head to feet)

1. **Black gi top** — heavy cotton (`#0a0a10`), open V-collar, sleeves rolled up to the elbow. **Sleeves are key — they flap with motion.**
2. **White training belt** wrapped around the waist with a knot tied off-center on the left. Two short tails hang ~14 px down.
3. **Loose gi pants** — black (`#1a1a22`), rolled at the cuff above the ankle.
4. **Bare feet** — visible toes. Important: no shoes. Dojos fight barefoot.
5. **White hand wraps** — knuckles to mid-forearm.

## Identity item — REQUIRED IN EVERY FRAME

**The white belt knot at the left hip with two short tails hanging down.** White (`#dcd6c4`) on the black gi — the highest-contrast element of the silhouette. The tails should swing with motion (1 frame lag on direction changes). This and the bare feet make Dojo immediately distinguishable from any other enemy.

## Palette (hex)

```
gi top (mid)       #0a0a10
gi top (shadow)    #050507
gi top (highlight) #1c1c22
belt white         #dcd6c4
belt shadow        #a8a294
gi pants           #1a1a22
pants shadow       #0e0e15
hand wraps         #dcd6c4
skin (light)       #c89478    (vary)
skin (shadow)      #8a6248
hair               #1a1410
toenails           #c8a890     (1px detail)
```

## Personality / fighting style

- **Active guard.** While `guardActive` is on (1.0 s armed / 1.4 s open cycle), Dojo *parries* incoming player hits and counters with a kick. Forces the protagonist to pick their moments, not button-mash.
- **Four signature moves — front kick / roundhouse / axe kick / flying side kick. Dojo is the ONLY character in the cast whose attacks are entirely KICKS — no punches.** Bare feet visible on every strike. Belt tails snap with each kick.
  - **`front_kick` — Mae geri (straight thrust kick).** **Visual signature: F2–F3 the rear leg drives FORWARD horizontally, FOOT FLEXED with toes pulled back, heel leading — striking with the ball of the foot at chest-of-target height. Supporting leg slightly bent, body upright, both hands in guard at chest.** Belt tails snap forward with the kick. 11 dmg + 100 knockback.
  - **`roundhouse` — Mawashi geri.** **Visual signature: F3 silhouette is unmistakable — supporting leg planted, kicking leg horizontal at chest height with the shin parallel to the ground, body torqued 45° showing the hip drive, top of the foot leading**. Both arms swung to the rear shoulder for counter-balance. Belt tails snap horizontally with the rotation. 14 dmg + 130 knockback.
  - **`axe_kick` — Heel drop from overhead.** **Visual signature: F1–F2 the kicking leg rises STRAIGHT UP past the head (a 180° leg extension splitting the silhouette vertically), F3 drives the heel DOWNWARD onto the target — the leg slicing through the air like a falling guillotine**. Body slightly leaned back for balance. The vertical-up leg pose is unmistakable. 18 dmg + 120 knockback.
  - **`flying_kick` — Tobi yoko geri (flying side kick).** **Visual signature: F3 silhouette is a horizontal arrow — body airborne, fully horizontal mid-flight, lead leg extended straight forward with the SIDE of the foot leading, rear leg tucked under the body, both arms swept back**. Lands and recovers. 20 dmg + 180 knockback.
- **Stance and posture are the visual identity** — narrow blade-stance with one foot leading, shoulders square, chin tucked. **He never throws a punch.** Hands stay in knife-hand guard during every kick — guard is purely defensive.
- **Bows before combat.** The first idle cycle on spawn includes a quick formal bow — head tilts forward 15°, hands at sides, then resumes stance.
- **Speaks short formal phrases:** "Begin." or "Show me." Rare — only at fight start.

## Animations

| Slot         | Frames | Notes |
|--------------|-------:|-------|
| `idle`       | 4 | **Karate front-stance** — narrow front-back foot placement, front knee bent, back leg straight. **Bare feet visible.** Hands in **knife-hand guard** (open palms vertical, fingers up, one forward at chin height, one at hip). Belt tails sway 1 px on breath. |
| `walk`       | 6 | **Disciplined gliding stride that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 = LEFT foot slides fwd + RIGHT shoulder rotates fwd 2 px (opposite-side, but kept tight to the body). F2 = passing position (feet roughly under body). F3 = RIGHT foot slides fwd + LEFT shoulder rotates fwd 2 px. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. **Hands stay in knife-hand guard at chin/hip the whole cycle** — they do NOT swing out wide, but the shoulders rotate AT THE SIDES with each step so the body still reads as walking, not as a static stance. Arms NEVER extend forward past chin height (would read as a strike — and Dojo doesn't strike with hands). Bare feet stay flat, never crossing the center line. Belt tails drift 1 px laterally per step. No planted/stomp pose on F6 — the cycle blends straight back. |
| `atk1`       | 4 | **Front kick (mae geri).** F1 = rear knee lifts to chest, foot pulled toward the hip (chamber). F2 = **leg drives forward horizontally, foot flexed with toes back, heel leading**. F3 = peak — leg fully extended at chest-of-target height, ball of foot at impact, supporting leg slightly bent, **belt tails snapped forward 6 px**. F4 = re-chamber knee, return to stance. |
| `atk2`       | 5 | **Roundhouse (mawashi geri).** F1 = body torques back, kicking leg starts lifting sideways with knee bent. F2 = leg chambers to the side, knee at shoulder height. F3 = **peak — kicking leg horizontal at chest height, shin parallel to ground, top-of-foot leading, body rotated 45°, arms swung to rear shoulder, belt tails snap horizontally**. F4 = leg follow-through past the target. F5 = recovery, leg returns to stance. |
| `atk3`       | 6 | **Axe kick.** F1 = kicking leg lifts toward chest. F2 = leg continues rising straight up, body leans back slightly. F3 = **peak — kicking leg STRAIGHT UP vertical past the head (the leg splits the silhouette into two halves), supporting leg planted, body arched back slightly**. F4 = leg DRIVES DOWN with heel leading (vertical chop). F5 = heel at chest-of-target height. F6 = recovery, leg plants. |
| `jump_atk`   | 5 | **Flying side kick.** F1 = explosive leap-off (both knees coiled, body lowering for spring). F2 = airborne, body rising and tilting horizontal. F3 = **peak — body fully horizontal mid-air, lead leg extended straight forward with the SIDE of the foot leading, rear leg tucked under, both arms swept back** — arrow silhouette. F4 = held one frame in flight. F5 = landing recovery. |
| `guard`      | 3 | Both hands in tight knife-hand guard, body angled 30° away from camera (blade-stance). **Belt tails ABSOLUTELY STILL** — the stillness is intentional. |
| `bow`        | 6 | Formal bow. F1–F2 = head + torso tilt forward 15°, hands flat at thighs. F3 = held bow (1 frame). F4–F6 = return to stance. |
| `hurt`       | 3 | Body folds. **Belt tails swing wide and snap**. Recovers fast — by F3, back in guard. |
| `dead`       | 4 | F1 = body folds. F2 = falls to one knee (composed, not collapsed). F3 = forward to all fours. F4 = settles. (Dojos die with composure.) |

## DO NOT include

- **Different Dojo designs across rows** — the bowing Dojo, the walking Dojo, and the kicking Dojo are all the SAME person. Same hair, same proportions, same skin tone, same gi.
- **Text inside cells** — no anim labels, no row headers, no frame numbers.
- **Cell separator lines.**
- Modern street clothes — Dojo always wears the gi.
- Visible weapons — empty hands, bare feet, no knife / chain / gun.
- Bright colors — black gi, white belt, that's it. No purple/maroon tint shifts between rows.
- Tattoos.
- Loose, untied hair (always tied back).
- Footwear of any kind.

## Visual VFX summary

Dojo's identity is the **belt-tail snap** with every kick + the karate front-stance + bare feet visible on strikes. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so no two kicks blur together — and Dojo never punches.

- `atk1` FRONT KICK (mae geri) — body upright, rear leg drives STRAIGHT forward at chest height, foot FLEXED with toes pulled back and HEEL leading; belt tails snap forward 6 px
- `atk2` ROUNDHOUSE (mawashi geri) — body torqued 45°, kicking leg horizontal at chest height with shin PARALLEL to the ground, top-of-foot (instep) leading; belt tails snap horizontally with the rotation
- `atk3` AXE KICK — kicking leg goes STRAIGHT UP past the head (vertical leg splits the silhouette), then heel drives straight DOWN like a guillotine; belt tails snap upward then down
- `jump_atk` FLYING SIDE KICK (tobi yoko geri) — body fully AIRBORNE and HORIZONTAL mid-flight, lead leg straight forward with the SIDE of the foot leading, rear leg tucked under, both arms swept back; belt tails trailing horizontally behind

**Hurt / flinch:** F1 body folds. F2 belt tails swing WIDE and snap. Recovers fast — by F3 back in guard stance. 1-px white impact spark.

**Dead:** Falls to one knee first (composed, not collapsed), then forward to all fours. Bare feet visible throughout.

## Sheet specs

- 7 columns × 5 rows = 35 cells (~30 frames used)
- Cell size: **52 × 72**
- Magenta `#ff00ff` background — high-contrast against the black gi
- Bottom-center anchor
