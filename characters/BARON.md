# BARON — Stage 3 Boss

Kane's old-school enforcer. The classic noir-comic "heavy" archetype made flesh. Real name **William "Baron" Halsey** — a name and a man who only exist in this game. Ex-college boxer, ex-something-else-he-doesn't-talk-about. Kane hired him to run "respectable" street-level work — the shakedowns that look like inspections, the evictions that look like negotiations.

He fights like a boxer because he was one. The brass knuckles are for the people who don't know that.

> **NOTE FOR ARTISTS / AI GENERATORS:** Baron is **explicitly fictional** — a Dick-Tracy-villain-style caricature, not a real-world person. Lean into the **caricature**: brick-shaped body, neck wider than the head, jaw exaggeratedly square, comically broad shoulders, slightly stylised proportions like a 1940s noir comic panel. **Avoid any resemblance to actual public figures.** If a draft looks like a known person, exaggerate further — make the jaw squarer, the neck thicker, the shoulders wider, the scar more obvious — until it doesn't. The point of reference is **Flattop / Pruneface / The Brow from Dick Tracy, or the Kingpin's enforcers in 60s/70s comics**, not a real cop or real boxer.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **11 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — jab (4 frames)
> 4. `atk2` — cross (5 frames)
> 5. `atk3` — haymaker (9 frames)
> 6. `knee` — rising knee (5 frames)
> 7. `leap` — leaping double-smash (6 frames)
> 8. `jump_atk` — aerial knee (4 frames)
> 9. `hurt` (3 frames)
> 10. `taunt` (5 frames)
> 11. `dead` (5 frames)
>
> **Total: 56 frames in 11 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.

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

- **Five signature moves — jab / cross / haymaker / knee / leaping smash. Brass knuckles glint gold on every punch — the colour tell. The square jaw juts forward during attacks — the caricature in motion.**
  - **`jab` — Pistoning lead.** Fast left-hand boxer's jab. **Visual signature: F2 shows the fist mid-extension with a 1-px GOLD GLINT on the brass knuckles** — the only bright colour in the frame. Body barely twists. Coat doesn't move. 11 dmg.
  - **`cross` — Hip-driven straight.** Heavy right-hand straight. **Visual signature: F3 the long coat FLARES WIDE behind him in a 45° fan** as the body rotates fully, gold knuckles forward at peak. Front foot rooted, rear heel rising. **The square jaw juts forward** by 1 px at peak. 16 dmg.
  - **`haymaker` — Looping overhand.** Telegraphed wind-up overhand. **Visual signature: F1–F4 the coat OPENS FULLY (both panels swept aside) revealing the chest scar at the open collar — a 4-frame "I'm about to end this" tell.** F5 = peak with the right arm at full overhand extension, body rotated past 90°, gold knuckles tracing a comet arc from shoulder-high down to chest-of-target. 28 dmg + 250 knockback. **Super-armored** — eats hits during the wind-up.
  - **`knee` — Rising knee strike.** Close-range knee to the gut. **Visual signature: F2–F3 the rear knee drives upward 18 px past the body line, leading with the kneecap. Both hands grab the imagined opponent's collar to pull them DOWN onto the knee — body folds forward 20° to meet the knee, coat flaring open**. Pure noir-comic enforcer move. 18 dmg + 90 knockback.
  - **`leap` — Leaping double-fist smash.** A short forward jump ending with both fists driving down. **Visual signature: F2–F3 silhouette is a forward-leaping figure — both fists clasped together overhead, knees tucked under, coat flaring behind**. F4 lands hard with **dust burst (4–5 brown specks at his feet)** as both knuckle-rings come down together. 22 dmg + 180 knockback.
- **Boxing patterns mixed with bare-knuckle brutality.** Strings 2–3 jabs, then a cross, occasional haymaker, occasional knee at close range, occasional leap as a gap-closer.
- **Talks during the fight.** Calm and even-toned: "You don't have to do this." / "Walk away. I'll tell Kane it was nothing." / "This is the last time I ask."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | **Boxer's bounce on the balls of the feet** (1 px up/down). Hands at chin in textbook guard, gold knuckles catching highlight on F2. Coat sways 1 px at the hem. **Square jaw + scar + white hair streak visible.** |
| `walk`     | 6 | Casual approach, almost a stroll. Coat trails 2 px behind. Hands at chin, low guard. |
| `atk1`     | 4 | **Jab.** F1 = lead shoulder cocks back 2 px. F2 = **fist extends with gold-knuckle glint at peak**. F3 = full extension, knuckles vertical. F4 = sharp snap-back. |
| `atk2`     | 5 | **Cross.** F1 = hip cocks back. F2 = rotation begins. F3 = **peak — rear fist crosses centerline, coat flares behind in 45° fan, gold knuckles forward, body rotated 45°, square jaw juts forward 1 px**. F4 = rotation continues. F5 = snap-back, coat resettles. |
| `atk3`     | 9 | **Haymaker.** F1–F4 = wind-up — **coat OPENS FULLY across all four frames, chest scar visible at the open collar**. F5 = peak — right arm at full overhand extension above the shoulder, body rotated past 90°, **gold-knuckle trail (3-px arc of comet glint)**. F6–F8 = follow-through. F9 = recovery, coat closing back. |
| `knee`     | 5 | **Rising knee.** F1 = both hands rise to "collar grab" pose, body coils. F2 = **rear knee starts driving up, hands pull DOWN simultaneously, body folds forward 10°**. F3 = peak — **knee 18 px past body line, body bent forward 20°, coat flaring open at the front**. F4 = held one frame. F5 = recovery, knee plants. |
| `leap`     | 6 | **Leaping double-smash.** F1 = deep coil, knees bend, both fists drop to hips. F2 = launch — **body airborne, knees tucked under, both fists clasping together overhead, coat flaring behind 8 px**. F3 = mid-flight peak, full leap silhouette. F4 = descent begins, fists arcing down. F5 = **landing impact — both clasped fists at chest-of-target height, dust burst at his feet (4–5 brown specks)**. F6 = recovery, body straightening. |
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
