# KANE — Final Boss

**Victor Kane.** Real-estate developer. Founder and CEO of **Kane Properties LLC**. The reason every other fight in this game happens.

For nine stages Kane has never lifted a hand. When the protagonist reaches him at the top of his tower, he finally **stands up from his desk**. The gloves come off. The cane he's been leaning on contains a sword. The pocket-watch chain looped across his vest is a brass whip with a weighted fob at the end. The man who pays other people to swing has been a fighter all along — he just never thought you'd make it this far.

This is the **hardest fight in the game**. Kane is fast, precise, and almost never tires.

> **NOTE FOR ARTISTS / AI GENERATORS:** Kane is **explicitly fictional** — a Dickensian villain caricature in a modern suit, not a real-world businessman. Lean into the **caricature**: exaggerated tall-thin proportions, period-feeling accessories (round wire-rim glasses, pocket-watch chain, sword-cane, white cotton gloves), unnaturally precise posture. **Avoid any resemblance to actual public figures.** If a draft looks like a known person, change features until it doesn't. The point of reference is **Mr. Burns from The Simpsons or Anton Ego from Ratatouille**, not a real CEO.

## Physical

- **Age:** 60–65, ageless in an uneasy way.
- **Height/build:** Unnaturally TALL and THIN. ~6'2" but reads taller because he stands perfectly straight. Long fingers. Narrow shoulders. Like an old crane that learned to wear a suit. **He moves with the precision of a fencing master in his prime.**
- **Skin:** Pale and slightly waxen — a man who hasn't been outside in years. Faint dark circles under the eyes.
- **Body language:** Unnaturally STILL in idle, then **explosively precise** in motion. No wasted movement. When he attacks the body snaps into the form like a chess piece being placed; on miss-recovery the body folds back to STILL within one frame.
- **Face:** Sharp narrow cheekbones, deep-set eyes, long thin nose, small precise mouth. **The asymmetric half-smile (LEFT corner only)** never drops — not on attacks, not on hurt, not on death.

## Hair

- **Pure white**, neatly slicked back from a sharp widow's peak. **A single dark grey streak runs through the right side** of the hair — visible in every frame.

## Costume

1. **Charcoal three-piece suit** — `#3a3a40` with subtle 1-px pinstripe (`#4f4f57`) every 6 px. **Jacket cut LONGER than modern fashion** (mid-thigh tall-coat silhouette). Single-breasted, two-button.
2. **White stand-up wing collar shirt** — `#f4f4f0`.
3. **Emerald-green silk cravat** — `#1a4a30` with `#2a6a40` highlight. Fat 19th-century knot.
4. **Charcoal vest** matching the suit, six buttons done up. **Pocket-watch chain** loops across the vest from a buttonhole into the right vest pocket — `#cfa040`, 8–10 px arc.
5. **Round wire-rim gold glasses** — thin gold frames (`#cfa040`), perfectly round lenses ~3 px. **Largest 'fictional character' visual hook.**
6. **Dark slacks** matching the suit.
7. **Black leather oxford shoes** mirror-polished — `#08080a` with `#1c1c22` highlight.
8. **Tiny brass skyscraper lapel pin** — `#cfa040`, ~2 × 4 px, left lapel.
9. **Thin white cotton gloves** on both hands — `#dcd6c4`. Removed mid-fight (see `glove_off` pose below).

## Weapons — REVEALED IN COMBAT

1. **Sword-cane** — Kane has been leaning on a long black walking cane all along. When the fight begins he **draws a thin silver blade from inside the cane** (`#cfd0d6` blade, `#08080a` cane sheath, `#cfa040` brass knob handle). The remaining cane sheath he holds in his off-hand as a parrying tool. **The sword is ~80 px long** — gives him exceptional reach.
2. **Pocket-watch whip** — the brass chain (`#cfa040`) that was looped across his vest. He pulls the watch out and uses the **chain as a whip with the weighted gold watch fob** at the end (`#cfa040` chain, `#f4c860` watch face). Used for his `special` move — wide horizontal sweep across the room.

## Identity items — REQUIRED IN EVERY FRAME

1. **The asymmetric half-smile** — LEFT corner only. Always present, even on death.
2. **Round wire-rim gold glasses** — small, gold, perfectly circular.
3. **Single dark grey streak in white hair**.
4. **Skyscraper lapel pin**.
5. **The sword-cane** — visible in every frame from `stand_up` onward (sheath in off-hand, blade in dominant hand).
6. **Long suit jacket** mid-thigh hem — the silhouette signature.

## Palette (hex)

```
suit charcoal mid   #3a3a40
suit shadow         #1c1c22
suit highlight      #4a4a52
pinstripe           #4f4f57
shirt white         #f4f4f0
cravat green        #1a4a30
cravat highlight    #2a6a40
cravat shadow       #08280c
vest dark           #2a2a30
shoe black          #08080a
hair white          #e8e8e4
hair grey streak    #5a5a62
skin (light)        #d8c8b8
skin (shadow)       #a89488
skin (deep)         #6a5848
glasses gold frame  #cfa040
gloves white        #dcd6c4
sword blade         #cfd0d6
sword edge hi       #ffffff
cane sheath black   #08080a
cane brass knob     #cfa040
watch chain brass   #cfa040
watch face          #f4c860
desk mahogany       #4a2818
desk shadow         #1a0e08
```

## Personality / fighting style

- **Polite, patient, lethal.** Speaks calmly during the fight — no shouting.
- **Three combat patterns:**
  - `atk1` — **cane thrust.** Front-foot stab forward with the sword. Long reach (cane + arm + ~80 px blade).
  - `atk2` — **cross sweep.** Horizontal cane-sword slash from the right side, parried with the sheath in the off-hand on miss.
  - `atk3` — **lunge thrust.** Full fencing-lunge body extension; longest reach in the game. Heavily telegraphed but punishing if it connects.
- **Special:** `chain_whip` — the pocket-watch chain swings in a wide horizontal arc across the entire screen at chest height. Player must duck (back row) or jump.
- **Counter:** `parry_riposte` — when player attacks at close range, Kane parries with the cane-sheath and ripostes with the sword.
- **Dialog while fighting** (mid-fight pool, picked at random by the engine):
  - "I have lawyers on retainer for situations exactly like this."
  - "The Block was always going to fall."
  - "Marcus signed his lease in 1986. I have the paperwork."
  - "You really don't have to do this."

## Animations

Sheet should support these slots for the engine's combat path. (Old QTE-only `seated_open / lean_in / gesture_open / ...` poses are deprecated — the cinematic now plays before the fight, not instead of it.)

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Standing tall behind the desk, sword-cane planted point-down on the floor, gloved off-hand resting on knob. Pure stillness. |
| `walk`     | 6 | Slow, precise approach. Cane taps the floor on every other step. |
| `atk1`     | 5 | Cane thrust — F1 wind-up shoulder back, F2 forward step, F3 full extend (sword tip forward), F4 hold, F5 retract. |
| `atk2`     | 6 | Cross sweep — F1 cane raised diagonally, F2 horizontal slash with full body torque, F3-4 follow-through with cape-like jacket flare, F5-6 reset to stance. |
| `atk3`     | 7 | Fencing lunge — F1 coil down, F2-3 explosive forward lunge (body fully extended, sword leading), F4-5 hold the lunge (longest reach pose), F6-7 recover to stance. |
| `special`  | 10 | Chain whip — F1-2 pulls watch out of vest pocket, F3-4 winds the chain in a half-circle, F5-7 horizontal wide arc across screen at chest height (motion-blur the chain), F8-10 watch returns to pocket. |
| `counter`  | 5 | Parry-riposte — F1 sheath raised to deflect, F2 deflect impact, F3 immediate sword thrust forward, F4-5 recovery. |
| `hurt`     | 3 | Body folds slightly at the waist. Glasses STAY ON. Half-smile STAYS. Sword stays in hand. |
| `glove_off`| 4 | One-time reveal pose at fight start — Kane stands from the desk (F1), removes the right glove with a single precise tug (F2), drops it (F3), draws the sword from the cane (F4). Plays once when the cinematic transitions into the fight. |
| `dead`     | 5 | Falls backwards over the desk. Sword clatters to the floor. Half-smile finally drops on the LAST frame only — for one frame his face is empty. Then the fight ends. |

## DO NOT include

- **Any resemblance to a real public figure.** If a draft looks like a known person, change features until it doesn't.
- A full symmetric smile. Always lopsided (left corner only).
- A pistol, gun, or any modern firearm. Kane fights with the sword-cane and the chain whip — no firearms ever.
- Modern phone, laptop, computer. Period props only.
- Loose hair or messed-up jacket — even on hurt frames, the appearance stays perfect.
- The glove on the right hand from `glove_off` onward — that hand stays bare to grip the sword.
- The smile reaching the eyes. The eyes are always cold; only the mouth corner moves.

## Sheet specs

- 6 columns × 10 rows = 60 cells (allows generous per-anim frame counts)
- Cell size: **128 × 144** — Kane is tall and the desk doesn't need to be in every cell anymore (only `idle` and `glove_off` show the desk)
- Magenta `#ff00ff` background OR transparent
- Anchor: bottom-center

## Fight design notes

- HP ≈ 400 — highest in the game.
- Music: full `kane` theme with all instrumentation (drums included — the QTE-only theme stripped them; the real fight needs them back).
- The QTE cinematic still plays as the intro to the fight. After the 5 prompts resolve, the cinematic ends with Kane saying "...I see" — then `glove_off` animates and the fight proper begins.
- On defeat: Kane falls back over his own desk. Final frame his eyes are open, half-smile finally gone. The fight ends. Cut to ending cinematic.
