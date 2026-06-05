# BARON — Stage 3 Boss

Kane's old-school enforcer. Real name **William "Baron" Halsey.** Ex-cop. Took a buyout from the department six years ago after an internal affairs investigation that nobody wanted to finish. Kane hired him within the month. Baron runs Kane's "respectable" street-level operations — the shakedowns that look like inspections, the evictions that look like negotiations.

He fights like a boxer because he was one in college. The brass knuckles are for the people who don't know that.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> Cells must contain only the character — no anim labels, no row headers, no frame numbers, no cell borders.
>
> Baron is **the same man** across every cell: same face, same hair, same suit, same brass knuckles. Only the pose changes.

## Physical

- **Age:** 52
- **Height/build:** 6'2", thick. Powerlifter frame gone soft in the gut but the shoulders are still wide. Heavier than Atlas, slower than Tank.
- **Skin:** Pale-white, ruddy from years of bad sleep. Broken nose (broken once playing college football, twice on the job).
- **Body language:** Loose-shouldered, deliberately unintimidating. Stands relaxed. The posture is part of the menace — he wants you to underestimate him. Ankles roll slightly outward.
- **Face:** Heavy jaw. Eyes that look tired but never look away. Resting expression: a small, polite smile.

## Hair

- Steel grey, short, parted neatly to the right. Receding hairline. Always combed — even mid-fight, he checks it during recovery frames.

## Costume (head to feet)

1. **Tan trench coat** — long, knee-length, beige-tan (`#8a6a3a`), open in front. The coat IS the silhouette. Has noticeable weight — swings 1 frame behind body movement.
2. **White dress shirt** under, slightly stained, top two buttons open. No tie.
3. **Dark slacks** — charcoal grey (`#2a2a30`).
4. **Black dress shoes** — polished, scuffed at the toe.
5. **Belt** — black leather with a plain silver buckle.
6. **Brass knuckles** on both fists — `#cfa040` with deeper shadow.

## Identity items — REQUIRED IN EVERY FRAME

1. **The trench coat** — even mid-uppercut. The coat is Baron.
2. **Brass knuckles** — visible on both fists. Catch a small highlight pixel during attacks.
3. **A gold sheriff-style badge clipped to the inside-left of the coat** — visible only when the coat flares open during attacks. Reads "RETIRED — NPD." This is what Baron pulls out when the cops try to ask questions. ~6 × 5 px gold.

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
hair grey          #8a8a8e
hair shadow        #4a4a50
skin (light)       #d4a888
skin (shadow)      #9a6e4e
skin (deep)        #6a4830
badge gold         #f4c860
```

## Personality / fighting style

- **Three signature moves — jab / cross / haymaker. Brass knuckles glint gold on every punch — the colour tell.**
  - **`jab` — Pistoning lead.** Fast left-hand boxer's jab. **Visual signature: F2 shows the fist mid-extension with a 1-px GOLD GLINT on the brass knuckles** — the only bright colour in the frame. Body barely twists (real-boxer economy). Coat doesn't move. 11 dmg.
  - **`cross` — Hip-driven straight.** Heavy right-hand straight. **Visual signature: F3 the long coat FLARES WIDE behind him in a 45° fan** as the body rotates fully, gold knuckles forward at peak. Front foot rooted, rear heel rising. 16 dmg.
  - **`haymaker` — Looping overhand.** Telegraphed wind-up overhand. **Visual signature: F1–F4 the coat OPENS FULLY (both panels swept aside) revealing the vest + brass badge underneath — a 4-frame "I'm about to end this" tell.** F5 = peak with the right arm at full overhand extension, body rotated past 90°, gold knuckles tracing a comet arc from shoulder-high down to chest-of-target. 28 dmg + 250 knockback. **Super-armored** — eats hits during the wind-up.
- **Boxing patterns.** Strings 2–3 jabs, then a cross, occasional haymaker. Reads like a real fighter.
- **Talks during the fight.** Calm and even-toned: "You don't have to do this." / "Walk away. I'll tell Kane it was nothing." / "This is the last time I ask."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | **Boxer's bounce on the balls of the feet** (1 px up/down). Hands at chin in textbook guard, gold knuckles catching highlight on F2. Coat sways 1 px at the hem. |
| `walk`     | 6 | Casual approach, almost a stroll. Coat trails 2 px behind. Hands at chin, low guard. |
| `atk1`     | 4 | **Jab.** F1 = lead shoulder cocks back 2 px. F2 = **fist extends with gold-knuckle glint at peak**. F3 = full extension, knuckles vertical. F4 = sharp snap-back to guard. |
| `atk2`     | 5 | **Cross.** F1 = hip cocks back, rear heel grounded. F2 = hip rotation begins. F3 = **peak — rear fist crosses the centerline, coat flares behind in a 45° fan, gold knuckles forward, body rotated 45°**. F4 = body rotation continues, fist held forward. F5 = snap-back, coat resettles. |
| `atk3`     | 9 | **Haymaker.** F1–F4 = wind-up — body coils, rear arm draws back behind shoulder, **coat OPENS FULLY across all four frames, vest + brass badge visible underneath, free hand drops to hip for balance**. F5 = peak — right arm at full overhand extension above the shoulder, body rotated past 90°, **gold-knuckle trail (3-px arc of comet glint)** from shoulder-high down to target chest-height. F6–F8 = follow-through, body fully torqued. F9 = recovery, coat closing back. |
| `hurt`     | 3 | Body folds. **Hair stays neat.** Hands drop briefly from guard. |
| `taunt`    | 5 | **Combs hair with one hand**. F1–F2 = right hand rises to hair. F3 = held comb pose. F4–F5 = hand returns to guard. Polite smile throughout. (Plays once during the fight.) |
| `dead`     | 5 | Falls hard. F3 = on his side. F4 = coat splays open, **brass knuckles fall from his hands and roll out 8 px ahead of him** — the iconic image. F5 = settled. |

## DO NOT include

- **Text inside cells** — no `JAB` / `CROSS` / `HAYMAKER` / row headers / frame numbers.
- **Cell separator lines.**
- **Variation of Baron across frames.**
- Visible firearm — Baron is brass-knuckles-only on the streets.
- Wrinkled or dirty trench coat — clean, even mid-fight.
- A scowl — he never *looks* angry. The polite smile is the menace.
- Modern tactical gear.
- Tattoos.

## Sheet specs

- 8 columns × 6 rows = 48 cells (~40 frames used)
- Cell size: **80 × 96** — Baron reads as bigger than the protagonists in silhouette
- Magenta `#ff00ff` background
- Bottom-center anchor

## Boss-fight design notes

- HP ≈ 220 (1 sqrt-scaled per difficulty).
- Has a name plate that appears on the screen on spawn: **"BARON — Kane's enforcer"**.
- Music: switch to the `river` theme during the fight (already wired).
- Defeat: he goes down on one knee first, then falls to the floor. He doesn't beg. He says "Fine. He'll send someone worse."
