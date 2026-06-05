# DOJO

The disciplined ones. Kane found them at a martial-arts studio in financial trouble — paid the rent for a year and got the senior students on retainer. They don't enjoy this work the way Slice does. They treat the protagonist as an opponent, not an obstacle.

Of all Kane's crews, Dojo is the only one who *bows* before the fight.

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

- **Active guard.** While `guardActive` is on (1.0 s armed / 1.4 s open cycle), Dojo *parries* incoming player hits and immediately counters. Forces the protagonist to pick their moments, not button-mash.
- **Signature move — `counter`: Parry-strike (one-frame deflection + open-palm strike in a single motion).** This is NOT a boxer's straight punch — it's a karate technique. **Visual signature: F2 shows BOTH hands working at once — the rear hand sweeping outward to deflect (palm out, fingers up), the lead hand simultaneously driving forward in an open-palm strike (heel-of-palm leading, fingers angled up).** Body in a deep front stance (bent front knee, straight back leg) — VERY different from any boxer in the cast. **Belt tails snap forward** with the strike. 11 dmg + 110 knockback.
- **Stance and posture are the visual identity** — narrow blade-stance with one foot leading, shoulders square, chin tucked. He never stands square-on like a brawler.
- **Bows before combat.** The first idle cycle on spawn includes a quick formal bow — head tilts forward 15°, hands at sides, then resumes stance.
- **Speaks short formal phrases:** "Begin." or "Show me." Rare — only at fight start.

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | **Karate front-stance** — narrow front-back foot placement, front knee bent, back leg straight. Hands in **knife-hand guard** (open palms vertical, fingers up, one forward at chin height, one at hip). Belt tails sway 1 px on breath. |
| `walk`     | 6 | Light gliding steps in stance — front foot slides forward, rear foot follows. **Never crosses center line** (no boxer's stride). Hands stay in guard. |
| `atk1`     | 4 | **Parry-strike.** F1 = guard tightens, rear hand cocks. F2 = **rear hand sweeps OUT/DOWN in a deflecting arc, lead hand simultaneously drives forward in an open-palm strike (palm heel leading, fingers angled up)** — both arms active in the SAME frame. F3 = peak (lead palm fully extended at chest-of-target height, rear hand returned to guard, **belt tails snapped forward 6 px**). F4 = retract to stance. |
| `guard`    | 3 | Both hands in tight knife-hand guard, body angled 30° away from camera (blade-stance). **Belt tails ABSOLUTELY STILL** — the stillness is intentional. |
| `bow`      | 6 | Formal bow. F1–F2 = head + torso tilt forward 15°, hands flat at thighs. F3 = held bow (1 frame). F4–F6 = return to stance. |
| `hurt`     | 3 | Body folds. **Belt tails swing wide and snap**. Recovers fast — by F3, back in guard. |
| `dead`     | 4 | F1 = body folds. F2 = falls to one knee (composed, not collapsed). F3 = forward to all fours. F4 = settles. (Dojos die with composure.) |

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

## Sheet specs

- 7 columns × 5 rows = 35 cells (~30 frames used)
- Cell size: **52 × 72**
- Magenta `#ff00ff` background — high-contrast against the black gi
- Bottom-center anchor
