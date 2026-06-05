# RIG

Kane's construction-crew muscle. These were already on Kane's payroll — laborers and demolition workers who knew what would happen to a holdout block long before anyone else did. They show up to fights in the same hard hats and steel-toes they wore on shift. Most of them are just *doing the job*.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> **The yellow hardhat is on his head in EVERY frame, in EVERY animation**, including hurt and dead. The hardhat is Rig's identity item — a frame without it is a wrong frame.
>
> Cells must contain only the character — no labels, no row headers, no frame numbers, no cell borders.
>
> Rig is **one specific worker** across every cell — same face, same beard / clean-shaven choice (pick one), same hardhat, same orange vest, same brown pants. Only the pose changes.

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

- **Mutters during fights.** Short worker-talk phrases: "Just doin' the job." or "Move it, kid." Not malicious; bored.
- **Doesn't chase fast.** Walks. Trusts his weight to do the work.
- **Two signature moves — strike + pound.**
  - **`strike` — Hardhat headbutt-and-jab.** Not a regular punch. **Visual signature: F1 he LOWERS his head and angles the yellow hardhat forward like a battering ram**, body bent at the waist. F2 he drives forward with the hardhat leading, free arm trailing for balance. F3 the lead fist comes in BENEATH the hat as a hook — so the hardhat threatens, the fist lands. Reads as "I'll hit you with my head, or with my fist, your choice." 14 dmg, 130 knockback.
  - **`pound` (every 4th attack) — Pneumatic-drill earthquake.** AOE ground smash. **Visual signature: F5–F6 silhouette is a vertical column — both fists clasped above the hardhat, body fully stretched UP into a straight line from heels to hands**. Then he piledrives downward — F10 impact has a **shockwave ring radiating outward from his boots** (a 2-px arc of brown dust specks reaching 36 px out on each side) **plus a vertical dust plume rising up his body** to hat height. Hits both sides simultaneously. Hard-hat **does not move** during the rise/drop — locked to his head. Big damage, big knockback. Super-armored throughout.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | Heavy chest rise. Hardhat brim catches a 1-px yellow highlight on F2. Shoulders rolled forward (working-man posture). |
| `walk`   | 6 | **Stomp gait** — boots flat-footed, body barely sways. Dust puff (1 brown speck) at the planted boot heel on every step. |
| `atk1`   | 5 | **Hardhat headbutt-and-jab.** F1 = **head LOWERS, hardhat tilts forward like a ram**, body bends at waist, fists rise. F2 = step forward (hardhat leading). F3 = peak — **lead fist drives forward UNDER the hardhat brim**, hardhat still angled forward, free arm trailing for balance. F4 = retract fist. F5 = head rises back, hardhat re-levels. |
| `atk2`   | 12 | **Pneumatic-drill earthquake.** F1 = both arms start rising, knees bend. F2–F3 = arms continue up, body straightening (small dust specks at boots starting). F4 = arms above head, fists clasping (more ground specks). F5 = **vertical column pose — fists clasped above hardhat, body stretched fully UP from heels to hands, hardhat steady**. F6 = held column (1 frame, the launch tell). F7–F8 = drive downward (body folds, fists arcing down). F9 = body fully folded, fists at boot level. F10 = **impact — shockwave dust ring radiating 36 px on each side, vertical dust plume rising up to hardhat height, body bent forward**. F11 = recovery start, body lifts. F12 = back to standing, dust settling. |
| `hurt`   | 3 | Stagger. Head turns 10°. **Hardhat stays on.** |
| `dead`   | 4 | Falls FORWARD onto the ground (face down, hardhat lands first). Hardhat stays on the head through all 4 frames. |

## DO NOT include

- **Text labels inside cells** — no `idle`, no `walk`, no `atk1`, no row headers, no frame numbers.
- **Cell separator lines or borders.**
- **A bareheaded Rig in any frame** — yellow hardhat is on the head in every single cell, including hurt/dead.
- **A different worker across frames** — same face, same beard choice, same hat, same vest, same pants in every cell.
- Tactical / military gear — Rigs are construction workers, not soldiers.
- Visible weapons — bare fists only. (Ironic that the most dangerous AOE in the game is empty-handed.)
- Clean, pressed clothing — everything is worn-in and stained.
- The hard hat replaced by a beanie or other headgear. Stays the yellow construction helmet.

## Sheet specs

- 8 columns × 5 rows = 40 cells (~35 frames used; pound attack is the big one at 12)
- Cell size: **64 × 80**
- Magenta `#ff00ff` background
- Bottom-center anchor
