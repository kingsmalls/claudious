# RAZOR — Stage 6 Boss

Kane's white-collar specialist. Real name **Eliza Park.** Came up through corporate compliance and "private security" consulting before Kane found her. Her job is to *talk* a holdout into selling. The dual knives are for the people who think a polite conversation can't end this way.

She wears a tailored suit because she does most of her work in office buildings. The Block is the first job in years where she's had to use the knives.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **13 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `draw` (4 frames)
> 4. `atk1` — CROSS-CUT SLASH (4 frames) — **SINGLE front blade DIAGONAL upper-right to lower-left across the body**, other blade at the hip
> 5. `atk2` — TWIN-BLADE FLURRY (8 frames) — **THREE alternating slashes left-right-left**, criss-cross of red arcs stacked on top of each other (only multi-slash chain at chest level)
> 6. `atk3` — FENCING KICK (5 frames) — **FRONT leg STRAIGHT FORWARD at hip height, foot FLEXED with HEEL leading**, both blades in fencing guard (the only kick)
> 7. `atk4` — MISSILE DASH (9 frames) — **body fully HORIZONTAL mid-air**, BOTH blades extended forward as a leading X-shape, legs trailing horizontally
> 8. `atk5` — SPINNING PIROUETTE (8 frames) — **full 360° spin GROUNDED**, both blades held perpendicular at HIP height tracing a complete circle (red halo at hip level)
> 9. `throw` — KNIFE THROW (5 frames) — **one blade RELEASED as a projectile** 18 px ahead of the empty throwing hand, second blade still held at the hip
> 10. `special` — BLADE DANCE (14 frames) — **SIX sequential slashes at SIX different angles** (diagonal, opposite diagonal, horizontal hip, horizontal neck, vertical, X-burst) — the kata-diagram
> 11. `counter` — SCISSOR-PARRY + LOW LEG-CUT (6 frames) — **both blades CROSS in an X to catch the strike**, then a step-past + low scything cut at the THIGHS (the only attack below knee height; no projectile)
> 12. `hurt` (3 frames)
> 13. `dead` (5 frames)
>
> **Total: 81 frames in 13 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Razor's sheet kept producing attacks that all looked like "woman in a suit waving a knife." Every attack below must occupy a DIFFERENT silhouette quadrant — if two attacks share a silhouette, redraw one. The dual-blade arcs are designed as a **chart of angles and heights** — every blade move sits at a different angle on the body.
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` cross-cut | Vertical fencing stance | FRONT blade only | Diagonal upper-right to lower-left at chest height | Single 28-px red diagonal arc; rear blade stays at the hip — the only single-blade slash |
> | `atk2` flurry | Squared, body alternating L/R | BOTH blades alternating | Three chest-height arcs in opposing diagonals | Criss-cross of THREE stacked red arcs (one frame shows one blade mid-arc, the other already chambered) — only multi-arc chest pattern |
> | `atk3` fencing kick | Vertical, supporting leg straight | FRONT leg (HEEL leading) | Straight forward at hip height | Front leg fully extended forward, foot FLEXED with HEEL leading, BOTH blades still held in guard — only kick / only attack where blades are NOT moving |
> | `atk4` missile dash | Body fully HORIZONTAL mid-air | BOTH blades extended forward | Forward at chest height (flying) | Body parallel to the ground, both arms forward as a leading X, legs trailing — only airborne attack |
> | `atk5` pirouette | GROUNDED 360° rotation | BOTH blades perpendicular outward | Continuous circle around the body at HIP height | Red halo ring around the body at hip level — only attack with a circular sweep + only AOE multi-hit |
> | `throw` knife throw | Vertical, body squared to target | ONE blade as projectile | Forward through the air | The blade is DETACHED from the hand (only attack where Razor is missing a knife); 6-px motion-line behind the projectile |
> | `special` blade dance | Multi-phase, body shifting per strike | All angles chained | 6 hits at varied heights and angles | 6 red arcs forming a kata diagram (diagonal, opposite diagonal, horizontal hip, horizontal neck, vertical, X-burst finisher) — only multi-angle chain |
> | `counter` scissor-parry + leg-cut | Folded LOW on F4, leg-height blade | BOTH blades cross then ONE low blade | Cross in front, then horizontal scythe at THIGH height | F2 both blades crossed in an X over the chest (only X-block pose); F4 body crouched LOW with one blade horizontal at thigh height — the only sub-knee blade attack |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 is ONE slash with ONE blade; the other blade stays at the hip. atk2 is THREE alternating slashes with BOTH blades in succession. If atk1 shows both blades arcing, redraw — atk1 is the single-blade signature.
> - **atk1/atk2 vs special:** the special's 6 strikes deliberately re-use the slash arcs of atk1/atk2, but at SIX different angles across 14 frames. If special looks like atk2 repeated, redraw so each of the 6 arcs hits a different height/angle (per the table above).
> - **atk3 (fencing kick) vs any blade move:** atk3 is the ONLY attack where the blades are static and the LEG is the weapon. The foot must be clearly at hip height with the heel leading. If the kick reads as "Razor slashing while standing on one leg," redraw — the leg IS the weapon.
> - **atk4 (missile dash) vs atk5 (pirouette):** atk4 is AIRBORNE with the body horizontal flying forward. atk5 is GROUNDED with the body vertical rotating in place. If both look like "blades extended out from the body," redraw — one flies straight, one spins on the spot.
> - **atk5 (pirouette) vs counter (scissor parry):** both involve both blades. Pirouette = blades perpendicular OUTWARD tracing a horizontal halo while the body spins. Counter = blades CROSSED in front of the chest in an X (defensive). Opposite intents and opposite silhouettes.
> - **throw vs counter:** throw RELEASES a blade as a projectile (one hand empty after F3). Counter KEEPS both blades — the X-parry then a low leg-cut. If counter shows a knife flying, redraw — the counter no longer throws; it cuts low at the legs instead. This is the differentiation from the throw.
> - **counter vs any other slash:** counter's F4 silhouette is the SHORTEST Razor gets — body crouched low with one blade horizontal at THIGH height. If counter's cut lands at chest height, redraw — it's the only sub-knee blade in the kit.

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
- **Seven signature moves — slash / flurry / fencing kick / dash / pirouette / throw / special. The dual blades are the visual identity. Both knives are visible in every combat frame.**
  - **`slash` — Cross-cut.** Single-knife forward slash drawn DIAGONALLY across the body. **Visual signature: F2–F3 shows a 28-px diagonal red-tinted arc from upper-right to lower-left** drawn by the blade tip. The other knife stays in fencing-guard at the hip. 10 dmg.
  - **`flurry` — Twin-blade rapid alternating slashes.** NEW. Both blades work in rapid succession — left blade slashes, then right blade slashes, then left again. **Visual signature: F2–F7 alternating diagonal arcs in opposing directions — each frame shows ONE blade mid-arc with a thin red motion line, the other blade at the hip ready. F3 left blade arcs up-left to down-right, F5 right blade arcs up-right to down-left, F7 left blade again. Forms a CRISS-CROSS pattern of red trails on top of the target.** 4-hit multi-hit, 6 dmg per hit (24 dmg total). Mid-range.
  - **`fencing_kick` — Heel-thrust to chest.** A fencer's straight kick. **Visual signature: F3 silhouette is unmistakably en garde with the foot — front leg extended straight forward at hip height, foot FLEXED with HEEL leading, supporting leg straight, BOTH blades held in fencing guard.** 12 dmg + 100 knockback.
  - **`dash` — Missile.** Telegraphed forward dash with BOTH blades extended. **Visual signature: F4–F6 silhouette is an X-shape — body fully horizontal at chest height, both arms extended forward with blades leading, legs trailing horizontally behind**. 16 dmg + 160 knockback. Self-pushes 240 px.
  - **`pirouette` — Spinning twin-blade.** NEW. Full 360° rotation with both blades extended outward at hip height. **Visual signature: F3–F8 across six frames the body completes a full spin. Both blades trace a continuous CIRCLE around her at chest height — the silhouette is a red halo of motion. Hits both sides simultaneously.** Multi-hit (6 ticks). 8 dmg per hit. AOE.
  - **`throw` — Released knife.** **Visual signature: F3 the knife is drawn 18 px ahead of her hand with a thin 6-px motion-line behind it, blade angled at 30° pointing forward.** Spawns a `knife` projectile (12 dmg, 240 px/s).
  - **`special` — "BLADE DANCE" multi-hit signature.** NEW. Six-strike chained ballet of slashes. **Visual signature: 6 SEQUENTIAL BLADE ARCS at different angles and heights — like a choreographed dance:**
    - F1–F2 = wide stance load, both blades up at shoulder
    - F3 = STRIKE 1: front-blade slash from upper-right to lower-left (red arc #1, diagonal)
    - F5 = STRIKE 2: rear-blade slash from upper-left to lower-right (red arc #2, opposite diagonal)
    - F7 = STRIKE 3: front-blade horizontal cut at hip height (red arc #3, horizontal)
    - F9 = STRIKE 4: rear-blade horizontal cut at neck height (red arc #4, high horizontal)
    - F11 = STRIKE 5: front-blade vertical cut downward (red arc #5, vertical)
    - F13 = STRIKE 6: BOTH BLADES thrust forward together as X-shape finisher (red X-burst, biggest of the six)
    - F14 = hold + recovery
    - **Visual identity: 6 red arcs at varied angles forming a complex pattern — like a kata diagram. Launches on the final X-thrust.** 42 dmg total across the 6 hits.
  - **`counter` — Scissor-parry + low leg-cut.** Defensive X-block with BOTH blades, then a step-past and a low horizontal scythe at the opponent's thighs. **Visual signature: F2 BOTH blades cross over the chest in a tight X to catch the incoming strike (visible spark at the crossing point). F3 Razor steps past on the front foot, body lowering. F4 body fully CROUCHED low (the shortest she gets), front blade whips around HORIZONTALLY at THIGH height as a tight 16-px red arc at leg level — the only blade arc below the knee. F5 follow-through, blade past target. F6 stance returns.** Reads as "she blocked it with both blades and cut your leg out from under you." Keeps both knives — no projectile (that's what `throw` is for). 16 dmg + 80 knockback; cripples low.
- **Pattern:** Phase 1 mixes slash + flurry + fencing kick + dash. Phase 2 adds pirouette and the Blade Dance special.
- **Talks during fights:** "We could have done this in your kitchen." / "You're making this so much harder than it needs to be."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | **Hands clasped behind back, knives concealed.** Suit perfectly clean. Subtle breath (1-px shoulder rise on F2). Heels together, toes splayed slightly (formal posture). |
| `walk`     | 6 | **Heel-toe walk, steady tempo.** Suit trails 1 px. Hands stay clasped behind back. |
| `draw`     | 4 | F1 = body shifts into **fencing stance** (front foot lead, rear foot perpendicular). F2 = knives drawn from belt sheaths. F3 = **ready pose — front blade horizontal forward at hip height, rear blade vertical guard at the shoulder**. F4 = settle into stance. (Plays once on combat start.) |
| `atk1`     | 4 | **Cross-cut slash.** F1 = front blade cocks back over right shoulder. F2 = **diagonal slash begins, blade tip tracing 14 px down-and-left across the body**. F3 = peak — **28-px diagonal red motion arc visible from upper-right to lower-left**. F4 = return to fencing stance, both blades visible. |
| `atk2`     | 8 | **Twin-blade flurry.** F1 = stance squares, both blades chamber at the hips. F2 = LEFT blade cocks up. F3 = **STRIKE 1 — left blade arcs from upper-left to lower-right at chest height, thin red motion-line**. F4 = left retracts as RIGHT blade cocks up. F5 = **STRIKE 2 — right blade arcs from upper-right to lower-left at chest height (opposite diagonal of strike 1)**. F6 = right retracts as LEFT blade cocks again. F7 = **STRIKE 3 — left blade arcs again at hip height (lower than strike 1)**. F8 = recovery, both blades return to hip guard. **Visual identity: criss-cross of red arcs on top of each other.** |
| `atk3`     | 5 | **Fencing kick.** F1 = front foot lifts, knee chambered toward chest, both blades in fencing guard. F2 = leg begins extending. F3 = **peak — front leg fully extended straight forward at hip height, foot FLEXED with HEEL leading**. F4 = leg retracts to chamber. F5 = foot plants back, return to stance. |
| `atk4`     | 9 | **Missile dash.** F1 = stance widens, both blades raise. F2 = body coils. F3 = launch (body angles 45°, both knives leading). F4 = **body fully horizontal mid-air, both blades extended, legs trailing horizontally — X-shape**. F5–F6 held missile pose. F7 = land, blades still extended. F8–F9 = stance recovery. |
| `atk5`     | 8 | **Spinning pirouette.** F1 = supporting foot pivots, body starts rotating, both blades EXTEND outward at hip height (perpendicular to the body). F2 = body 90° through the rotation, blades still extended at hip level. F3 = body 180° (facing away from camera). F4 = body 270°. F5 = body completes 360° (back to original facing). F6 = blades start drawing back in. F7 = settle into fencing stance. F8 = back to ready. **Visual identity: blades trace a continuous circle around her at hip height through F1–F5 — red halo of motion.** |
| `throw`    | 5 | **Knife throw.** F1 = body squares to target, rear arm cocks the knife at ear height. F2 = arm begins forward motion. F3 = **release — knife drawn 18 px ahead of the throwing hand, 6-px motion-line trail behind it, blade angled 30° pointing forward**. F4 = follow-through, throwing arm fully extended. F5 = return to stance. |
| `special`  | 14 | **BLADE DANCE — six-hit signature.** F1–F2 = wide stance load, both blades at shoulder height. F3 = **STRIKE 1: front-blade slash upper-right to lower-left (red arc #1, diagonal)**. F4 = wind-up for next. F5 = **STRIKE 2: rear-blade slash upper-left to lower-right (red arc #2, opposite diagonal)**. F6 = wind-up. F7 = **STRIKE 3: front-blade horizontal cut at HIP height (red arc #3, horizontal)**. F8 = wind-up. F9 = **STRIKE 4: rear-blade horizontal cut at NECK height (red arc #4, high horizontal)**. F10 = wind-up. F11 = **STRIKE 5: front-blade VERTICAL cut downward (red arc #5, vertical)**. F12 = body coils, both blades raise. F13 = **STRIKE 6 (finisher): BOTH BLADES thrust forward together — X-burst, biggest of the six red marks**. F14 = recovery. **Six varied-angle arcs — the kata diagram identity.** |
| `counter`  | 6 | **Scissor-parry + low leg-cut.** F1 = both blades rise toward the chest, weight shifts to the front foot. F2 = **BOTH blades cross over the chest in a tight X (the scissor block) — visible spark at the crossing point as the incoming strike is caught**. F3 = step-past — front foot plants past the imagined opponent, body lowering, blades uncrossing. F4 = **peak — body CROUCHED LOW (shortest pose Razor takes), front blade whipped HORIZONTALLY across THIGH height as a 16-px tight red arc at leg level (the only sub-knee blade arc)**. F5 = follow-through, blade past target, second blade trailing at hip guard. F6 = return to ready stance, both blades still in hand. |
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

## Visual VFX summary

Razor's identity is the **dual-blade red motion arcs at varied angles** + immaculate posture (suit never wrinkles). **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so no two moves blur together.

- `atk1` CROSS-CUT SLASH — single 28-px diagonal red arc from upper-right to lower-left at chest height; rear blade stays at the hip (the only single-blade slash)
- `atk2` TWIN-BLADE FLURRY — THREE alternating slashes (left-right-left) forming a criss-cross of red arcs stacked at chest height (the only multi-arc chain at chest level)
- `atk3` FENCING KICK — no blade arc; FRONT leg STRAIGHT FORWARD at hip height with the foot FLEXED and HEEL leading, both blades held in guard (the only kick + only attack where blades are static)
- `atk4` MISSILE DASH — body fully HORIZONTAL mid-air, both blades extended forward as a leading X, legs trailing horizontally (the only airborne attack)
- `atk5` SPINNING PIROUETTE — GROUNDED 360° rotation, both blades held perpendicular at HIP height tracing a complete circle — red halo ring at hip level (the only AOE multi-hit + only circular sweep)
- `throw` KNIFE THROW — one blade RELEASED as a projectile 18 px ahead of the empty throwing hand with a 6-px motion-line trail (the only attack where Razor is missing a knife)
- `special` BLADE DANCE — 6 red arcs at six different angles (diagonal, opposite diagonal, horizontal hip, horizontal neck, vertical, X-burst finisher) — the kata-diagram identity
- `counter` SCISSOR-PARRY + LOW LEG-CUT — F2 both blades crossed in an X over the chest (the only X-block pose), then F4 body CROUCHED LOW with front blade whipping HORIZONTALLY at THIGH height as a 16-px red arc (the only blade arc below the knee). Both knives stay in hand.

**Hurt / flinch:** F1 body twists 15° from the hit, both knives stay in hand (she never drops them). F2 suit stays clean (her signature — even mid-hit the tailoring is perfect). 1-px white spark at the contact point.

**Dead:** Falls to one knee, then to her side. Both knives slide 8 px from her open hands on F4 — the only frames where she releases them.

## Sheet specs

- 8 columns × 6 rows = 48 cells (~38 frames used)
- Cell size: **64 × 96**
- Magenta `#ff00ff` background
- Bottom-center anchor

## Boss-fight design notes

- HP ≈ 200.
- Music: continue Stage 6's `lantern` theme (mood-piece tension).
- Defeat: she sheaths the remaining knife, sits down on one of the shattered glass piles, says "Tell Kane I'm done." She doesn't fall.
