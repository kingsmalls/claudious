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
> 4. `atk1` — cross-cut slash (4 frames) — single diagonal cut
> 5. `atk2` — twin-blade flurry (8 frames) — rapid alternating slashes left-right-left-right
> 6. `atk3` — fencing kick (5 frames) — heel-thrust forward
> 7. `atk4` — missile dash (9 frames) — both blades extended, X-shape body
> 8. `atk5` — spinning pirouette (8 frames) — 360° turn with both blades sweeping
> 9. `throw` — knife throw (5 frames) — released knife with motion trail
> 10. `special` — BLADE DANCE (14 frames) — six-hit signature, **must be visually distinct from atk1/atk2**
> 11. `counter` — parry-and-throw (6 frames) — off-hand blade deflects, throwing-hand knife flies
> 12. `hurt` (3 frames)
> 13. `dead` (5 frames)
>
> **Total: 81 frames in 13 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.

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
  - **`counter` — Parry-and-throw riposte.** NEW. Defensive deflect with one blade + instant knife throw with the other. **Visual signature: F1 off-hand blade rises diagonally to deflect (visible spark at deflection point). F2 the parry connects. F3 rear arm cocks the THROWING blade. F4 throwing-hand blade RELEASES forward as a projectile. F5–F6 stance recovery.** Reads as "she deflected with one hand and threw with the other in a single motion."
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
| `counter`  | 6 | **Parry-and-throw riposte.** F1 = off-hand blade rises diagonally to deflect (visible spark at deflection point). F2 = parry connects, body angles slightly. F3 = rear arm cocks the THROWING blade at ear height. F4 = **throwing-hand blade RELEASES forward as a projectile (motion-line trail)**. F5 = follow-through, throwing arm extended. F6 = return to ready stance. |
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
