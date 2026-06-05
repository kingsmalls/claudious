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

- **Three attacks:**
  - `punch` — heavy single straight punch. 16 dmg, 140 knockback.
  - `charge` — massive shoulder-tackle with super-armor + 240 px self-push. 24 dmg, 220 knockback. Telegraphed by 14-frame stance shift.
  - `overhead` — both fists raised overhead, smashes downward. 32 dmg, 260 knockback. **Super-armored** through the entire wind-up. The protagonist can't trade with this; has to dodge.
- **Doesn't talk.** Ever. Not at start, not on hits, not on defeat.
- **Patient.** Waits for the protagonist to commit before acting.

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Crossed arms. Subtle chest rise. Eyes track. |
| `walk`     | 6 | Slow, deliberate. Arms stay crossed for the first 4 frames; uncross on F5 if approaching to attack. |
| `atk1`     | 6 | Punch: F1 = arm uncoils, F2 = step forward, F3 = peak extension (gold ring catches light), F4–F6 recovery. |
| `atk2`     | 12 | Charge: F1–F4 = stance widens, shoulder lowers (super-armor active), F5–F8 = forward charge with motion lines, F9 = impact, F10–F12 = recovery. |
| `atk3`     | 13 | Overhead: F1–F4 = both arms rise overhead, body coils, F5–F8 = body extends fully skyward, F9–F11 = drive downward, F12 = ground impact (huge burst), F13 = recovery. |
| `hurt`     | 3 | Body absorbs. Almost no flinch. (At full HP, he barely registers hits.) |
| `dead`     | 7 | The first significant flinch is also the death animation. He goes down slowly, in stages — first to one knee, then to all fours, then onto his side. Stays unconscious. |

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
