# RIG

Kane's construction-crew muscle. These were already on Kane's payroll — laborers and demolition workers who knew what would happen to a holdout block long before anyone else did. They show up to fights in the same hard hats and steel-toes they wore on shift. Most of them are just *doing the job*.

## Physical

- **Age range:** 28–45
- **Height/build:** 6'0" – 6'4", thick. Pure-mass build from manual labor. Shoulders broader than Tank; gut tighter.
- **Body language:** Heavy and slow. Doesn't bounce. Hands curled into fists at thigh height. Spits to the side occasionally (1 frame, 1 px).
- **Face:** Weathered. Scruffy stubble or full beard. Some have safety goggles pushed up onto the hard hat.

## Hair

- Mostly hidden by the hard hat. What's visible: short, sweat-flat, shades of brown or grey.

## Costume (head to feet)

1. **Yellow hard hat** — `#cfa040`. Battered, scuffed at the brim. The single most visible thing about Rig.
2. **High-vis safety vest** — fluorescent orange (`#ff7a30`) over a brown work shirt. Two reflective grey stripes (`#a8a8a8`) horizontal across the front.
3. **Brown work shirt** — long sleeves rolled up to the elbow. Forearms exposed, hairy.
4. **Dirty work pants** — khaki-brown (`#7a5a3a`), oil stains visible (darker patches).
5. **Steel-toed work boots** — heavy brown leather (`#3a2a1c`) with grey steel toes (`#5a5a5a`). Bigger than Atlas's; chunkier sole.
6. **Heavy leather work belt** with hammer loops (empty — he's not carrying tools today).

## Identity item — REQUIRED IN EVERY FRAME

**The yellow hard hat.** Always on the head, never knocked off (even on hurt / dead frames — it stays). Has a small black "KANE PROPERTIES" logo (`#1a1a22`, ~3 px square) on the front-left of the brim. The combination of the hard hat + hi-vis orange vest is what makes Rig instantly readable as a *worker*, not a thug.

## Palette (hex)

```
hard hat yellow    #cfa040
hard hat hi        #e8c860
hard hat shadow    #8a6020
hard hat logo      #1a1a22
hi-vis orange      #ff7a30
hi-vis hi          #ffa050
hi-vis shadow      #b04a10
reflective stripe  #a8a8a8
work shirt         #7a5a3a
work shirt shadow  #3a2a18
pants              #7a5a3a
pants shadow       #3a2a18
boot leather       #3a2a1c
boot toe (steel)   #5a5a5a
skin (light)       #d4a888     (vary)
skin (shadow)      #9a785a
beard              #4a3a28
```

## Personality / fighting style

- **Two attacks:**
  - `strike` (default) — heavy forward fist. 14 dmg, 130 knockback.
  - `pound` (every 4th attack) — AOE ground smash. **Both fists clasped overhead → drives down into the ground.** Heavily telegraphed (18-frame startup with rumble particles), super-armored, hits both sides simultaneously with a shockwave hitbox. Big damage, big knockback.
- **Mutters during fights.** Short worker-talk phrases: "Just doin' the job." or "Move it, kid." Not malicious; bored.
- **Doesn't chase fast.** Walks. Trusts his weight to do the work.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | Heavy chest rise. Hard hat brim catches a 1-px highlight. |
| `walk`   | 6 | Stomp gait. Boots strike flat-footed. |
| `atk1`   | 5 | Strike: F1 = wind-up, F2 = step forward, F3 = peak punch extension, F4–F5 = recover. |
| `atk2`   | 12 | Pound: F1–F4 = both fists rise overhead, body coiled (rumble particles), F5–F6 = peak with hands above head, F7–F9 = drive downward, F10 = impact (shockwave burst, screen shake), F11–F12 = recovery. |
| `hurt`   | 3 | Stagger — head turns, hard hat stays on. |
| `dead`   | 4 | Falls forward onto the ground. Hard hat stays. |

## DO NOT include

- Hard hat falling off — it stays on every frame.
- Tactical / military gear — Rigs are construction workers, not soldiers.
- Visible weapons — bare fists only. (Ironic that the most dangerous AOE in the game is empty-handed.)
- Clean, pressed clothing — everything is worn-in and stained.
- The hard hat replaced by a beanie or other headgear. Stays the yellow construction helmet.

## Sheet specs

- 8 columns × 5 rows = 40 cells (~35 frames used; pound attack is the big one at 12)
- Cell size: **64 × 80**
- Magenta `#ff00ff` background
- Bottom-center anchor
