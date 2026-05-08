# BARON — Stage 3 Boss

Kane's old-school enforcer. Real name **William "Baron" Halsey.** Ex-cop. Took a buyout from the department six years ago after an internal affairs investigation that nobody wanted to finish. Kane hired him within the month. Baron runs Kane's "respectable" street-level operations — the shakedowns that look like inspections, the evictions that look like negotiations.

He fights like a boxer because he was one in college. The brass knuckles are for the people who don't know that.

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

- **Three attacks:**
  - `jab` — fast left-hand boxing jab. 11 dmg.
  - `cross` — heavy right-hand straight, full hip rotation. 16 dmg.
  - `haymaker` — telegraphed overhand. 28 dmg + 250 knockback. **Super-armored** — Baron eats hits during the wind-up.
- **Boxing patterns.** Strings 2–3 jabs, then a cross, occasional haymaker. Reads like a real fighter.
- **Talks during the fight.** Calm and even-toned: "You don't have to do this." / "Walk away. I'll tell Kane it was nothing." / "This is the last time I ask."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Boxer's bounce on the balls of the feet. Coat sways. |
| `walk`     | 6 | Casual approach. Coat trails. |
| `atk1`     | 4 | Jab. Fast snap-back. |
| `atk2`     | 5 | Cross. Body rotates 45°. Coat flares wide on F3. |
| `atk3`     | 9 | Haymaker. F1–F4 = wind-up (coat opens, badge visible briefly), F5 = peak (full extension), F6–F9 = recovery. |
| `hurt`     | 3 | Body folds. Hair stays neat. |
| `taunt`    | 5 | Combs hair with one hand. Smiles politely. (Plays once during the fight.) |
| `dead`     | 5 | Falls hard. Coat splays open. Knuckles fall from his hands. |

## DO NOT include

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
