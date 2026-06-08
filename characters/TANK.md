# TANK

Kane's heavy enforcer. Ex-prison-yard fighters and former bouncers Kane bought out of debt. They don't move fast and they don't talk much. Their job is to be the wall between Kane's interests and anyone who won't move.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **8 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — SLEDGEHAMMER SLAM (7 frames) — **PYRAMID silhouette**, both fists clasped overhead, body straight VERTICAL
> 4. `atk2` — SHOULDER CHARGE (8 frames) — **body angled 30° forward like a BATTERING RAM**, lead shoulder lowered, arms swept BEHIND
> 5. `atk3` — BEAR HUG GRAB (6 frames) — **BOTH arms reach forward at chest height in a WIDE WRAPPING posture**, fingers spread (the only grappling pose)
> 6. `atk4` — BELLY FLOP (6 frames) — **body HORIZONTAL on the ground**, arms spread wide, gut-down (the only prone attack)
> 7. `hurt` (3 frames)
> 8. `dead` (4 frames)
>
> **Total: 44 frames in 8 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Tank's biggest sheet-generation failure is **slam / charge / bear hug blurring together** because the generator falls back to "big man with arms out" for all three. Every attack below must occupy a DIFFERENT silhouette quadrant — if two attacks share a silhouette, redraw one:
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` slam | Body VERTICAL, arched back slightly | BOTH fists clasped overhead | Descending vertical | PYRAMID — wide feet, both arms straight vertical OVERHEAD with fists meeting at the top; the silhouette is taller than wide |
> | `atk2` shoulder charge | Body angled 30° FORWARD, lowered | Lead SHOULDER | Horizontal forward (whole-body ram) | Body angled forward like a battering ram with the lead shoulder dropped to chest height and arms swept BEHIND for aerodynamics (arms are NOT the weapon) |
> | `atk3` bear hug | Body bent forward 20°, upright-ish | BOTH arms wrap forward | Horizontal forward at chest height, then INWARD | Both arms reach forward in a WIDE WRAPPING C-shape with palms facing IN and fingers SPREAD (the only attack with open spread fingers); F4 squeezes inward |
> | `atk4` belly flop | Body HORIZONTAL on the GROUND | Whole gut/chest | Falling forward, then prone | Only attack where Tank ends FLAT on the ground; F4 silhouette is a horizontal mass with arms spread wide and the body parallel to the floor |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk3:** atk1 = both fists CLASPED TOGETHER OVERHEAD (vertical pyramid, fists meeting at the top of the silhouette). atk3 = both arms reach FORWARD at chest height with fingers SPREAD WIDE (palms in, hands NOT clasped, NOT overhead). If atk3 shows fists clasped overhead it's drawn as a slam — redraw with hands open, spread, forward at chest height.
> - **atk2 vs atk3:** atk2 = arms swept BEHIND, lead SHOULDER lowered as the weapon (whole body angled forward like a ram). atk3 = arms reach FORWARD wrapping (the weapon IS the arms). If atk2 shows arms forward, the charge isn't reading — redraw with arms back, shoulder leading.
> - **atk1 vs atk4:** atk1 ends standing upright with arms overhead at impact (vertical). atk4 ends flat on the ground with the body horizontal (prone). Opposite orientations. If atk4 shows Tank still standing at peak, redraw — the move's identity IS the prone landing.
> - **atk2 vs walk:** the charge body must be lower and more angled than walk; the lead shoulder visibly DROPS to chest height. If charge looks like Tank just walking faster, redraw with the shoulder clearly lowered and arms swept back.

> ## 🛑 ABSOLUTE RULE — DO NOT WRITE ANY TEXT INTO THE SHEET
>
> The output PNG **must contain ZERO text characters**. No `IDLE`, no `WALK`, no `ATK1`, no `F1` / `F2` / `F3` / `F4` / `F5` / `F6` / `F7`, no `HURT`, no `H1`, no `DEAD`, no `5°`, no row labels, no column labels, no frame counters, no annotations of any kind. Every cell must contain ONLY Tank — no captions, no diagrams, no overlays.
>
> If you need a reference for which cell is which, make a separate annotated proof image and throw it away. The production sheet ships clean.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> Same Tank in every cell — same bald head, same beard, same vest, same badge placement. Only the pose changes.
>
> No cell separator lines or borders. Cells are defined by even spacing.
>
> All four attacks must be **visually distinct** from idle AND from each other. The peak frame of each attack should be recognisable as that attack from outline alone.

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
- **Four signature moves — slam / shoulder charge / bear hug / belly flop. Tank uses his MASS as the weapon. Every attack involves the whole body in a different posture.**
  - **`slam` — Two-handed sledgehammer drop.** Both massive arms raise OVERHEAD with **fists clasped together**, body coils backward like a question mark, then crashes down. **Visual signature: at peak the silhouette is a PYRAMID — wide feet planted, both arms straight vertical overhead, fists meeting at the very top, body arched slightly backwards.** Dust falls downward from his boots during the wind-up (the ground shakes under him). 14 dmg + 180 knockback.
  - **`shoulder_charge` — Bull rush forward.** Lowered-shoulder shoulder-tackle. **Visual signature: F3–F4 silhouette is body angled 30° forward like a battering ram — lead shoulder LOWERED to chest height, arms swept BEHIND for aerodynamics, knees deeply bent and driving forward. Two heavy boot-prints with motion lines and dust trails behind each rear footfall.** Super-armored. 16 dmg + 200 knockback. Self-pushes 180 px forward.
  - **`bear_hug` — Crushing grapple.** Tank's pure-mass grab. **Visual signature: F2–F3 BOTH ARMS reach forward at chest height in a wide WRAPPING posture (like he's about to wrap them around a tree trunk), body bent forward 20°, fingers spread wide. F4 the imagined target is held against his chest while Tank's body squeezes inward, both arms wrapped, head tilted back as he crushes them.** No other character in the cast does a grapple this way. 20 dmg + 0 knockback (the target stays in place to get squeezed). 4 dmg per held second.
  - **`belly_flop` — Falling-tree body drop.** Tank LEAPS forward (short hop) then **falls flat onto his chest** like a falling tree. **Visual signature: F2 silhouette is body angled forward 60° mid-fall, arms thrown wide like dive-splash, gut leading the descent. F3 lands FLAT — body horizontal on the ground, arms spread wide, dust burst (8 brown specks) spraying outward from underneath the entire body length.** Heavy and graceless. 22 dmg + 220 knockback (AOE — hits anyone in front).

- **Doesn't speak.** Loud nasal grunts on the slam impact. Wheeze after bear hug. Heavy exhale after belly flop.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | **Wide planted stance** — feet outside shoulder width. Slow chest rise on breath. Arms hang loose, fists half-clenched. Vest **badge catches a 1-px gold highlight**. |
| `walk`   | 6 | **Heavy stomp gait that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 = LEFT leg fwd + RIGHT arm fwd swing (at side, hip-level). F2 = passing position. F3 = RIGHT leg fwd + LEFT arm fwd swing. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. **Both arms swing in a relaxed arc AT THE SIDES**, fists half-clenched at hip height. Arms NEVER extend forward past the body (would read as a bear-hug grab or shoulder-charge wind-up). Boots flat-footed, body barely sways. **Dust puff (1–2 brown specks) at the planted heel on F1, F3, F5**. Vest jiggles 1 px on impact. No planted/stomp pose on F6 — the cycle blends straight back. |
| `atk1`   | 7 | **Sledgehammer slam.** F1 = both arms start rising, knees bending. F2 = arms above head, fists clasping, body coiled back (ground-rumble specks at his feet). F3 = **peak PYRAMID pose — feet wide, both arms vertical overhead, fists meeting at the top, body arched backwards**. F4 = drive down (body folds at the waist, both fists crash at chest-height of target) — **dust burst, 5–6 brown specks in a half-circle at his feet**. F5 = follow-through, body bent forward, fists at thigh height. F6 = straighten. F7 = recovery to stance. |
| `atk2`   | 8 | **Shoulder charge.** F1 = stance widens, body coils backward. F2 = body angles forward 15°, lead shoulder starts lowering. F3 = **lead shoulder LOWERED to chest height, arms swept BEHIND, body angled 30° forward (battering-ram silhouette)**. F4 = launch — first stride forward, motion lines behind shoulders, **dust trail behind rear boot**. F5 = mid-charge, second stride, more motion lines. F6 = approaching impact, body still angled forward. F7 = impact, body straightens slightly, dust burst at contact point. F8 = recovery to stance. |
| `atk3`   | 6 | **Bear hug grab.** F1 = both arms start rising at the sides, body angling forward. F2 = arms swing forward at chest height, fingers spread wide, body bent 15° forward. F3 = **peak — BOTH ARMS reaching forward at chest height in a WIDE WRAPPING posture (palms in, fingers spread), body bent forward 20°**. F4 = arms WRAP inward (imagined target now between them), body squeezes inward, head tilts back. F5 = held crush pose. F6 = release, arms come down, body straightens. |
| `atk4`   | 6 | **Belly flop.** F1 = small forward hop, knees bent. F2 = **airborne, body angled 60° forward, arms thrown wide like dive splash, gut leading the descent**. F3 = peak airborne, body almost horizontal. F4 = **LANDING FLAT — body horizontal on the ground, arms spread wide, dust burst (8 brown specks spraying outward) along the entire body length**. F5 = held flop pose (the ground shakes). F6 = pushes himself back up, body lifting onto hands and knees. |
| `hurt`   | 3 | Body absorbs, **barely flinches** — head turns 5°, vest doesn't move. (At full HP he's almost unimpressed.) |
| `dead`   | 4 | Falls hard like a tree — F1 folds at the knees, F2 falls to one knee (dust puff), F3 collapses sideways, F4 face down. |

## DO NOT include

- **Any text in any cell** — no anim names, no frame numbers, no row headers, no captions. Production sheet is text-free.
- **Cell separator lines or borders.**
- **Variation of Tank across frames** — same bald head, same beard, same vest, same badge in every cell.
- Athletic / spring-loaded movement.
- Firearms or knives — Tanks brawl with their hands.
- Trimmed beard or styled hair.
- The KANE PROPERTIES badge replaced by anything else, ever.

## Visual VFX summary

Tank's identity is the **ground-rumble dust** during slam wind-ups + heavy boot-print dust on every footstep + the pyramid silhouette on the slam. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so no two moves blur together.

- `atk1` SLEDGEHAMMER SLAM — PYRAMID silhouette (wide feet, both arms vertical OVERHEAD with fists CLASPED at the top, body arched slightly back) + dust burst at his feet on impact + 1-frame screen-jitter
- `atk2` SHOULDER CHARGE — battering-ram silhouette (body angled 30° forward, lead SHOULDER lowered to chest height, arms swept BEHIND for aerodynamics) + dust trail behind rear boot
- `atk3` BEAR HUG GRAB — both arms reach FORWARD at chest height in a WIDE WRAPPING C-shape, palms IN, fingers SPREAD wide; body bent forward 20° (the only attack with spread fingers + the only grappling pose)
- `atk4` BELLY FLOP — body falls forward 60°, then lands FLAT HORIZONTAL on the ground with arms spread wide; 8-speck dust burst spraying outward along the entire body length (the only prone attack)

**Hurt / flinch:** Almost no flinch. F1 head turns 5°, vest doesn't move (he's barely impressed). 1-px white impact spark on the vest.

**Dead:** Falls like a tree — F1 folds at the knees, F2 falls to one knee (dust puff), F3 collapses sideways, F4 face down.

## Sheet specs

- 8 columns × 6 rows = 48 cells (~44 frames used; he now has 4 attacks)
- Cell size: **80 × 96** — Tank reads as big in silhouette
- Solid magenta `#ff00ff` background OR fully transparent PNG
- Bottom-center anchor
