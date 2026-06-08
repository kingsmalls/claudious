# BARON — Stage 3 Boss

Kane's old-school enforcer. The classic noir-comic "heavy" archetype made flesh. Real name **William "Baron" Halsey** — a name and a man who only exist in this game. Ex-college boxer, ex-something-else-he-doesn't-talk-about. Kane hired him to run "respectable" street-level work — the shakedowns that look like inspections, the evictions that look like negotiations.

He fights like a boxer because he was one. The brass knuckles are for the people who don't know that.

> **NOTE FOR ARTISTS / AI GENERATORS:** Baron is **explicitly fictional** — a Dick-Tracy-villain-style caricature, not a real-world person. Lean into the **caricature**: brick-shaped body, neck wider than the head, jaw exaggeratedly square, comically broad shoulders, slightly stylised proportions like a 1940s noir comic panel. **Avoid any resemblance to actual public figures.** If a draft looks like a known person, exaggerate further — make the jaw squarer, the neck thicker, the shoulders wider, the scar more obvious — until it doesn't. The point of reference is **Flattop / Pruneface / The Brow from Dick Tracy, or the Kingpin's enforcers in 60s/70s comics**, not a real cop or real boxer.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **14 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — jab (4 frames) — head-level straight
> 4. `atk2` — cross (5 frames) — head-level straight with hip drive
> 5. `atk3` — liver hook (5 frames) — low body shot at hip level (different angle)
> 6. `uppercut` — rising brass-knuckle uppercut (6 frames) — vertical rising fist
> 7. `haymaker` — overhand looping (9 frames) — telegraphed heavy
> 8. `clinch` — clinch + knee (7 frames) — boxer's grab into rising knee strike
> 9. `special` — BONE-BREAKER COMBO (12 frames) — five-strike chained finisher, **must be visually distinct from atk3**
> 10. `counter` — coat parry-riposte (6 frames) — coat-flare deflect into hidden cross
> 11. `jump_atk` — aerial knee (4 frames)
> 12. `hurt` (3 frames)
> 13. `taunt` (5 frames) — hair-comb gesture
> 14. `dead` (5 frames)
>
> **Total: 81 frames in 14 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> Cells must contain only the character — no anim labels, no row headers, no frame numbers, no cell borders.
>
> Baron is **the same man** across every cell: same face, same hair, same eye-scar, same suit, same brass knuckles. Only the pose changes.

## Physical

- **Age (presented):** 50s — but stylised, not realistic. He's a comic-book "thug in his prime gone slightly to seed."
- **Build:** **Comically rectangular**. Body silhouette reads as a TRAPEZOID — shoulders wider than the hips by an exaggerated margin. Wider than the protagonists by 50%. Heavier than Atlas. Slower than Tank. Cartoonishly broad-chested.
- **Neck:** **Wider than the head.** The neck-to-shoulder line is one continuous slope, no taper. This is the signature proportion.
- **Jaw:** **Square. Exaggeratedly so.** Lantern-jaw caricature. The jawline is a 90° angle at the corner, not curved.
- **Skin:** Pale ivory (`#e0c8a0`), ruddy on the cheeks and at the broken nose. Not photoreal — flat noir-comic shading with hard edges between light and shadow zones.
- **Body language:** Loose-shouldered, deliberately unintimidating. Stands relaxed. The posture is part of the menace — he wants you to underestimate him. Ankles roll slightly outward.
- **Face:** Heavy square jaw. **Cleft chin** (a clear 1-px vertical groove). Eyes small and close-set under a heavy brow. Resting expression: a small polite smile that never reaches the eyes.

## Identity markers — clearly fictional, REQUIRED IN EVERY FRAME

1. **A diagonal scar across the LEFT eyebrow** — 4-px white line cutting from above the eye down toward the cheek, splitting the eyebrow in half. This is Baron's "this is a fictional character" tell — no living person would have it drawn exactly this way.
2. **Cleft chin.** 1-px vertical groove in the center of the chin.
3. **Salt-and-pepper hair** with a **single bright-white stripe** running from the right temple back across the top of the head — like a comic-book villain's hair flash. Slicked back severely.
4. **Brass knuckles on BOTH fists** — visible in every cell. Oversized, comic-book brass-knuckle silhouette (read clearly from across the screen, not realistic gauntlet-shaped).
5. **Trench coat — but cut LONGER than modern style** (mid-shin, almost like a duster). Period-feeling, not contemporary tactical.

## Hair

- Salt-and-pepper, **dark grey base with a single bright-white streak from the right temple back across the head**. Slicked back hard with no part. Receding hairline showing a high widow's-peak.

## Costume (head to feet)

1. **Tan duster coat** — mid-shin length, beige-tan (`#8a6a3a`), open in front. Cut longer than modern fashion — period noir-comic feel. The coat IS the silhouette. Has noticeable weight — swings 1 frame behind body movement.
2. **High-collar white dress shirt** under, slightly stained, top two buttons open. **No tie** — open collar showing a chest scar.
3. **Dark high-waisted slacks** — charcoal grey (`#2a2a30`), pleated front (period detail).
4. **Black wing-tip oxford shoes** — polished, scuffed at the toe. Period footwear.
5. **Plain leather belt** with a comically large silver buckle (`#8a8a8e`).
6. **Brass knuckles** on both fists — oversized comic-book silhouette, `#cfa040` with deeper shadow. **Visible in every frame.**
7. **A small chest scar** visible at the open collar — 3 px white line just above the sternum.

## Palette (hex)

```
trench coat (mid)  #8a6a3a
trench (shadow)    #4a3a18
trench (highlight) #ad8a4f
shirt white        #e8e2d4
shirt stain        #b8a888
slacks             #2a2a30
slacks shadow      #181820
shoe black         #08080a
shoe shadow        #050507
brass knuckles mid #cfa040
brass kn shadow    #8a6020
brass kn highlight #f4d870
hair grey          #4a4a50
hair white streak  #e8e8e4
hair shadow        #2a2a30
skin (light)       #e0c8a0
skin (shadow)      #a8866a
skin (deep)        #6a4830
scar white         #f4f0e0
buckle silver      #8a8a8e
```

## Personality / fighting style

- **Eight signature moves with VARIED ANGLES — head punches, body punches, vertical uppercuts, grapples, a multi-hit special, a counter. Brass knuckles glint gold on every punch — the colour tell. The square jaw juts forward during attacks — the caricature in motion.**
  - **`jab` — Pistoning lead.** Fast left-hand boxer's jab. **Visual signature: F2 fist mid-extension with a 1-px GOLD GLINT on the brass knuckles — the only bright colour in the frame, at HEAD level.** Body barely twists. Coat doesn't move. 11 dmg.
  - **`cross` — Hip-driven straight.** Heavy right-hand straight. **Visual signature: F3 the long coat FLARES WIDE behind him in a 45° fan** as the body rotates fully, gold knuckles forward at HEAD level. Front foot rooted, rear heel rising. **Square jaw juts forward** by 1 px at peak. 16 dmg.
  - **`liver_hook` — Body shot.** Low horizontal hook to the gut. **Visual signature: F2–F3 body SQUATS DOWN slightly (knees bend, shoulder drops), rear arm whips around in a horizontal arc, gold knuckles trail visible at HIP LEVEL (not head level) — the angle that distinguishes this from jab/cross. F4 follow-through carries body past target.** Boxer's signature liver shot. 18 dmg + 120 knockback.
  - **`uppercut` — Rising brass-knuckle uppercut.** Vertical rising fist into the chin. **Visual signature: F2 deep coil — body crouches, lead fist drops to thigh. F3–F4 explosive RISE — body uncoils upward, lead fist drives straight UP past the chin, gold-knuckle vertical streak from hip to overhead (different angle from any other Baron punch — only one going UP).** 20 dmg + 80 knockback, launches.
  - **`haymaker` — Overhand looping.** Telegraphed wind-up overhand. **Visual signature: F1–F4 the coat OPENS FULLY (both panels swept aside) revealing the chest scar at the open collar — a 4-frame "I'm about to end this" tell.** F5 = peak with the right arm at full overhand extension above the shoulder, body rotated past 90°, gold knuckles tracing a comet arc from shoulder-high down to chest-of-target. 28 dmg + 250 knockback. **Super-armored** — eats hits during the wind-up.
  - **`clinch` — Boxer's clinch + knee combo.** Grab + pull-down + rising knee, one continuous motion. **Visual signature: F1–F2 both arms reach forward and CLAMP onto the opponent's shoulders (Baron's hands close into fists holding the imagined collar). F3 he PULLS DOWN hard (body bends forward, head lowers). F4 simultaneously his rear KNEE drives UP into the gut at the moment the opponent reaches the bent-over position. F5 release. F6–F7 recovery.** Grab + knee in one motion — no other character does this. 22 dmg + 100 knockback.
  - **`special` — "Bone-Breaker" five-hit combo.** Baron's signature multi-hit finisher. **Visual signature: 5 RAPID-FIRE BRASS-KNUCKLE STRIKES, each with a gold glint, body alternating left-right with each hit, coat whipping in every direction:**
    - F1–F2 = deep boxer stance load, both arms cocked
    - F3 = STRIKE 1 — JAB to face (gold glint #1, head level)
    - F4 = STRIKE 2 — CROSS to face (gold glint #2, head level, body torqued opposite)
    - F5 = STRIKE 3 — LIVER HOOK (gold glint #3, hip level — third glint at a NEW height)
    - F6 = STRIKE 4 — UPPERCUT (gold glint #4, vertical streak rising)
    - F7–F8 = body coils backward for finisher, both arms wind back
    - F9 = STRIKE 5 — HAYMAKER (gold glint #5 + COAT FLARES BEHIND like a cape, biggest glint of the five)
    - F10 = hold the finisher pose
    - F11–F12 = recovery, body returns to guard
    - Total visual: 5 gold flashes in rapid succession at DIFFERENT heights (head, head, hip, vertical, head — like a piano scale of brass-knuckle glints). 60 dmg total across the chain, last hit knockdowns.
  - **`counter` — Coat-parry riposte.** Magician-like deflect-and-strike. **Visual signature: F1 Baron raises his lead arm in a defensive guard. F2 the coat FANS WIDE in front of his body in a 90° sweep — for 1 frame his torso is HIDDEN BEHIND THE COAT (the magician's misdirection). F3 coat begins to drop, brass knuckles glint behind it. F4 a CROSS PUNCH erupts THROUGH the coat with gold-knuckle trail. F5–F6 coat resettles, body returns to guard.** Reads as "where did the punch come from?" 18 dmg + parry effect.
- **Boxing patterns mixed with bare-knuckle brutality.** Strings 1–2 jabs, mixes in a liver hook for variety, occasional cross or uppercut, occasional haymaker, occasional clinch at close range. Counter-fires when player throws at his guard. Uses Bone-Breaker special at low HP or when player tries to combo him.
- **Talks during the fight.** Calm and even-toned: "You don't have to do this." / "Walk away. I'll tell Kane it was nothing." / "This is the last time I ask."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | **Boxer's bounce on the balls of the feet** (1 px up/down). Hands at chin in textbook guard, gold knuckles catching highlight on F2. Coat sways 1 px at the hem. **Square jaw + scar + white hair streak visible.** |
| `walk`     | 6 | Casual approach, almost a stroll. Coat trails 2 px behind. Hands at chin, low guard. |
| `atk1`     | 4 | **Jab (head level).** F1 = lead shoulder cocks back 2 px. F2 = **fist extends with gold-knuckle glint at peak, head level**. F3 = full extension, knuckles vertical. F4 = sharp snap-back. |
| `atk2`     | 5 | **Cross (head level).** F1 = hip cocks back. F2 = rotation begins. F3 = **peak — rear fist crosses centerline, coat flares behind in 45° fan, gold knuckles forward at head level, body rotated 45°, square jaw juts forward 1 px**. F4 = rotation continues. F5 = snap-back, coat resettles. |
| `atk3`     | 5 | **Liver hook (BODY shot, HIP level — different angle than atk1/atk2).** F1 = body SQUATS slightly, knees bend 10°, lead shoulder drops. F2 = rear arm whips around horizontally at hip height. F3 = **peak — gold knuckles at HIP LEVEL (not head — the angle that distinguishes this from jab/cross), body torqued 60°, opposite arm thrown back for balance**. F4 = follow-through past target. F5 = body rises back to stance. |
| `uppercut` | 6 | **Brass-knuckle uppercut (VERTICAL — the only Baron punch going UP).** F1 = deep coil — body crouches low, lead fist drops to thigh height. F2 = body still coiled, weight on rear leg. F3 = **explosive RISE begins, lead fist starts climbing straight up**. F4 = **peak — body fully extended skyward, lead fist driven straight up past head height, gold-knuckle VERTICAL STREAK from hip-start to head-end**. F5 = held one frame at peak. F6 = recovery, fist coming down. |
| `haymaker` | 9 | **Overhand haymaker.** F1–F4 = wind-up — **coat OPENS FULLY across all four frames, chest scar visible at the open collar**. F5 = peak — right arm at full overhand extension above the shoulder, body rotated past 90°, **gold-knuckle trail (3-px arc of comet glint)** from shoulder-high down to chest-of-target. F6–F8 = follow-through. F9 = recovery, coat closing back. |
| `clinch`   | 7 | **Clinch + knee combo.** F1 = both hands rise to chest height, palms open. F2 = **arms CLAMP onto the imagined opponent's shoulders (hands close into fists holding the collar)**. F3 = **PULL DOWN hard — body folds forward, imagined opponent dragged down toward Baron's hip area**. F4 = rear knee starts driving UP toward the bent-down opponent. F5 = **peak — knee 18 px past body line at gut-of-target height, both hands still gripping the collar (target is bent at the waist), coat flaring open at the front**. F6 = release — hands let go, opponent flies back. F7 = recovery, knee plants. |
| `special`  | 12 | **"BONE-BREAKER" 5-hit combo (the signature finisher).** F1–F2 = deep boxer stance load, both arms cocked. F3 = **STRIKE 1: jab to face — gold glint #1 at HEAD level**. F4 = **STRIKE 2: cross to face — gold glint #2 at HEAD level, body torqued opposite**. F5 = **STRIKE 3: liver hook — gold glint #3 at HIP level (third glint at a NEW height)**. F6 = **STRIKE 4: uppercut — gold glint #4 as VERTICAL streak rising**. F7–F8 = body coils backward for the finisher, both arms wind back, coat flares open. F9 = **STRIKE 5: HAYMAKER — gold glint #5 (biggest of the five) + COAT FLARES FULLY BEHIND like a cape, body rotated 90°**. F10 = hold the finisher pose. F11–F12 = recovery, body returns to guard. **Visual identity: 5 gold flashes at DIFFERENT heights (head, head, hip, vertical, head) — like a piano scale of brass-knuckle glints.** |
| `counter`  | 6 | **Coat-parry riposte (magician's deflect-and-strike).** F1 = Baron raises lead arm in defensive guard. F2 = **the coat FANS WIDE in front of his body in a 90° sweep — for 1 frame his torso is HIDDEN BEHIND THE COAT (the magician's misdirection)**. F3 = coat starts to drop, **brass knuckles glint behind the coat (visible through a gap)**. F4 = **CROSS PUNCH erupts THROUGH the coat with gold-knuckle trail**, fist past the body. F5–F6 = coat resettles, body returns to guard. |
| `jump_atk` | 4 | **Aerial knee** — short-hop forward, rear knee drives forward at chest height. Coat flares behind. |
| `hurt`     | 3 | Body folds. **Hair stays neat.** Hands drop briefly from guard. Scar stays visible. |
| `taunt`    | 5 | **Combs hair with one hand** — checks the white streak. F1–F2 = right hand rises to hair. F3 = held comb pose. F4–F5 = hand returns to guard. Polite smile throughout. (Plays once during the fight.) |
| `dead`     | 5 | Falls hard. F3 = on his side. F4 = coat splays open, **brass knuckles fall from his hands and roll out 8 px ahead of him** — the iconic image. F5 = settled. |

## DO NOT include

- **Any resemblance to a real public figure.** If a draft looks like a known person, exaggerate jaw / neck / shoulders / scar further until it doesn't.
- **Realistic body proportions** — Baron is a noir-comic caricature, not a real boxer. Brick-shaped torso, wider neck than head, square 90°-corner jaw.
- **Text inside cells** — no `JAB` / `CROSS` / `HAYMAKER` / row headers / frame numbers.
- **Cell separator lines.**
- **Variation of Baron across frames** — same square jaw, same scar, same white hair streak, same coat in every cell.
- Visible firearm — Baron is brass-knuckles-only on the streets.
- Wrinkled or dirty trench coat — clean, even mid-fight.
- Modern tactical gear, modern shoes, modern haircut. The whole look is noir-comic period.
- Tattoos.
- A scowl — he never *looks* angry. The polite smile is the menace.

## Visual VFX summary

Baron's identity is the **brass-knuckle gold glint** at different heights per move (his "piano scale" of glints) + coat flares + the square jaw juts forward.

- `jab` — gold glint at head height
- `cross` — gold glint at head height + 45° coat flare behind
- `liver_hook` — gold glint at HIP height (lower than jab/cross — the body-shot tell)
- `uppercut` — gold knuckle leaves a VERTICAL gold streak from hip to overhead
- `haymaker` — coat OPENS FULLY across 4 frames (revealing chest scar) + gold-knuckle comet arc from shoulder down
- `clinch` — both hands grab + rear knee drives up + coat flares open
- `special` BONE-BREAKER — 5 gold glints at DIFFERENT heights (head, head, hip, vertical, head) — the piano-scale
- `counter` — coat fans wide hiding torso for 1 frame (magician's misdirection) + cross emerges through the coat with gold trail

**Hurt / flinch:** F1 body folds at the waist, but the hair STAYS NEAT (his signature — he's never disheveled), polite smile remains. F2 hands drop briefly from guard. 1-px white impact spark on the brass knuckles (his own knuckles catch the hit's spark).

**Dead:** Falls hard. Brass knuckles roll 8 px ahead of him on F4 — the iconic image. The polite smile finally drops on the very last frame for ONE frame.

## Sheet specs

- 8 columns × 6 rows = 48 cells (~45 frames used; he has 5 attacks now)
- Cell size: **80 × 96** — Baron reads as bigger than the protagonists in silhouette
- Magenta `#ff00ff` background
- Bottom-center anchor

## Boss-fight design notes

- HP ≈ 220 (sqrt-scaled per difficulty).
- Has a name plate that appears on the screen on spawn: **"BARON — Kane's enforcer"**.
- Music: switch to the `river` theme during the fight (already wired).
- Defeat: he goes down on one knee first, then falls to the floor. He doesn't beg. He says "Fine. He'll send someone worse."
