# BLACKWELL — Optional / Brutal-tier Encounter

Kane's personal bodyguard. Real name **Marcus Blackwell** (no relation to Rio's Marcus, despite the coincidence — the universe is cruel that way). He doesn't run a crew. He doesn't run errands. His only job is to be inside whatever room Kane is in.

In the engine: BLACKWELL spawns as an extra wave on stages 7 and 8 in **brutal** difficulty only. He's a wall between the player and the final stage. If you can beat him on brutal, you've earned the run.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> **The cells must contain ONLY the character.** No text. No labels. No frame numbers. No row headers. No anim names.
>
> If you need to verify cell alignment, do it on a separate proof sheet — the production sheet must be clean.
>
> Blackwell himself stays **identical** across every frame: same bald head, same suit, same shoulder holster, same arm tattoo silhouette. Only the pose changes.

## Physical

- **Age:** 44
- **Height/build:** 6'5", massive. Heavier than Atlas, heavier than Tank. Pure-mass strongman build that hasn't gone soft. Arms thicker than the protagonist's torso.
- **Skin:** Black, very dark (`#3a2418`).
- **Body language:** Still. Stands with arms crossed in idle. Doesn't bounce, doesn't shift weight. Watches with patience. Every motion is committed — he doesn't telegraph; he just *moves*.
- **Face:** Square jaw. Thin gray-black goatee. Small scar above the left eyebrow. Resting expression: blank. He doesn't show anything until he hits.

## Hair

- Shaved completely smooth. No facial hair other than the goatee.

## Costume (head to feet)

1. **Black tactical turtleneck** — `#0a0a10`, long sleeves, fitted, neck up to the chin. Modern, high-end fabric.
2. **Tactical chest holster rig** over the turtleneck — leather (`#1a1410`) with empty pistol holsters on each side (he doesn't draw guns; the holsters are decoration / threat).
3. **Slim black tactical pants** — same matte black, tucked into boots.
4. **Heavy combat boots** — black, polished, laced full to the calf.
5. **Black leather gloves** — fitted, hand-stitched, no fingertips exposed.

## Identity items — REQUIRED IN EVERY FRAME

1. **The crossed-arms idle pose** — arms folded across the chest. This is Blackwell's silhouette in idle. He uncrosses only to attack.
2. **A heavy gold ring on the right pinky** — the only color on him. `#cfa040` with a 1-px black engraving (Kane Properties insignia). 2 × 2 px. Visible during attacks.
3. **The tactical chest holster rig with empty holsters** — visible in every frame. The empty holsters are the threat: he doesn't NEED them.

## Palette (hex)

```
turtleneck black   #0a0a10
turtleneck shadow  #050507
turtleneck hi      #1c1c22
holster rig        #1a1410
holster strap      #2a1f15
pants              #0a0a10
boot               #050507
boot polish hi     #1c1c22
glove leather      #16100a
skin (light)       #6a4a30
skin (mid)         #4a2c1a
skin (shadow)      #2a1810
skin (deep)        #1a0e08
goatee dark        #2a201a
goatee grey        #5a5450
gold ring          #cfa040
gold ring shadow   #8a6020
ring engraving     #1a1a22
```

## Personality / fighting style

- **Three signature moves — punch / charge / overhead. The single gold wedding ring is the only colour on him; it catches a 1-px highlight at the peak of every strike. That glint is the visual identity.**
  - **`punch` — Crossed-arm to straight.** Arms STAY CROSSED until the last moment. **Visual signature: F1 still in crossed-arm idle, F2 the lead arm uncoils from across the chest (the slow reveal of intent), F3 peak extension — fist forward, gold ring catches the only bright pixel in the frame**. Body barely steps forward. The whole motion reads as "I haven't even tried yet." 16 dmg, 140 knockback.
  - **`charge` — Freight-train shoulder-tackle.** Massive shoulder-led charge. **Visual signature: F1–F4 he WIDENS into a sprinter's stance, lowering the lead shoulder until it's nearly horizontal — body angled at 35° forward, both arms swept behind for aerodynamics**. F5–F8 the charge has **4-px motion lines and a 2-px GROUND CRACK trailing behind each footstep** (small jagged dark lines on the floor). F9 impact, body upright. Super-armored. 24 dmg, 220 knockback. Self-pushes 240 px.
  - **`overhead` — Question-mark smash.** Both fists raised overhead, then driven into the ground. **Visual signature: F5–F8 silhouette is a question mark — body fully vertical, both arms straight UP with fists clasped at the apex, body slightly arched backwards. The pose is held for FOUR FRAMES — twice as long as anyone else's wind-up — because Blackwell can.** F12 impact creates a **huge dust burst (10–12 brown specks in a half-circle reaching 50 px out each side) plus a vertical dust plume rising past his head**. Super-armored throughout. 32 dmg, 260 knockback. The protagonist can't trade with this; has to dodge.
- **Doesn't talk.** Ever. Not at start, not on hits, not on defeat.
- **Patient.** Waits for the protagonist to commit before acting.

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | **Arms crossed tight over chest** — the iconic pose. Subtle chest rise on breath. Eyes track the protagonist. Gold ring catches a 1-px highlight on F2. |
| `walk`     | 6 | **Slow, deliberate stride. Arms STAY CROSSED for F1–F4**, uncross on F5 only if approaching to attack. Otherwise he walks with arms folded like a bouncer. |
| `atk1`     | 6 | **Crossed-arm punch.** F1 = still crossed, lead arm starts to slide free. F2 = lead arm uncoils across the chest, body shifts forward 2 px. F3 = **peak extension — fist forward 18 px, gold ring catches the highlight (only bright pixel in the frame)**. F4 = held strike one frame. F5 = retract. F6 = re-cross arms back into idle pose. |
| `atk2`     | 12 | **Freight-train charge.** F1 = arms uncross fully. F2 = stance widens (feet apart). F3 = **lead shoulder LOWERS to nearly horizontal**, body angled 25° forward. F4 = **fully horizontal forward, body at 35°, both arms swept behind for aerodynamics**. F5 = launch (forward motion begins, 4-px motion lines behind shoulders). F6 = mid-charge, **first ground-crack visible (2-px jagged dark line at the rear boot's last contact)**. F7 = continuing charge, second ground-crack. F8 = approaching impact. F9 = **impact, body upright, dust burst at contact**. F10 = follow-through, body straightening. F11 = stance recovery. F12 = arms re-cross. |
| `atk3`     | 13 | **Question-mark overhead.** F1 = arms uncross. F2 = both arms start rising at sides. F3 = arms continuing up, body coiling. F4 = arms approaching vertical. F5 = **peak A — body fully vertical, both arms straight UP, fists clasped at the apex, body arched slightly backwards (question mark silhouette)**. F6 = held peak (1). F7 = held peak (2). F8 = **held peak (3) — FOUR-FRAME hold of the apex pose**. F9 = body folds forward at the waist, fists arcing down. F10 = fists past the head. F11 = fists at chest height, body fully bent forward. F12 = **impact — fists driving into the ground, MASSIVE dust burst (10–12 brown specks in a half-circle reaching 50 px out each side, vertical dust plume rising past head height), body fully folded forward over the impact point**. F13 = straighten, dust settling. |
| `hurt`     | 3 | **Body absorbs, almost no flinch.** Head turns 5°. Crossed arms stay crossed even on hit. (At full HP, he barely registers.) |
| `dead`     | 7 | The first significant flinch IS the death animation — he goes down slowly, in stages. F1 = body folds at the waist. F2 = falls to one knee, arms uncross. F3 = onto both knees. F4 = forward to all fours. F5 = elbows give. F6 = forehead touches the ground. F7 = settled, face down. Stays unconscious. |

## DO NOT include

- **Frame numbers, anim names, or any text inside cells.** No `F1`, no `Hurt`, no row headers. The cell contains the character and nothing else.
- **Cell separator lines / grid borders.** Cells are defined by even spacing only.
- **Variation of Blackwell across frames** — same head, same suit, same proportions in every cell.
- Visible weapons — empty holsters only.
- A scowl or any visible emotion — Blackwell is *blank*.
- Loose, unfitted clothing.
- Decorative jewelry beyond the single gold ring.
- Tattoos.
- Speaking lines.

## Sheet specs

- 8 columns × 6 rows = 48 cells (~45 frames used; he has the longest attack chain)
- Cell size: **80 × 104** — Blackwell reads as the BIGGEST silhouette in the game (yes, bigger than Atlas)
- Magenta `#ff00ff` background
- Bottom-center anchor

## Boss-fight design notes

- HP ≈ 360 (the highest in the game).
- Spawns only in **brutal** difficulty, on stages 7 and 8 as a mid-stage wave (replaces a regular Tank wave).
- Music: `kane` theme during the fight.
- Defeat: he doesn't react. Just collapses on the third significant hit after his HP zeroes. The fight ENDS the moment he's down.
