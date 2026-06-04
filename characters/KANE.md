# KANE — Final Boss

**Victor Kane.** Real-estate developer. Founder and CEO of **Kane Properties LLC**. The reason every other fight in this game happens.

Kane has never thrown a punch in his life. He doesn't need to. Other people throw the punches; Kane writes the contracts. When the protagonist reaches him at the top of his tower, the fight is a **QTE cinematic**, not a brawl. Kane stays seated at his desk. He talks. He offers a check. The protagonist refuses.

You don't beat Kane with violence. You beat him by refusing the deal.

This is the most important character in the game — the entire campaign points at him. The art has to read on first sight as: *this man owns everything. He owns the room. He owns the city. He owns the conversation.*

> **NOTE FOR ARTISTS / AI GENERATORS:** Kane is **explicitly fictional** — a Dickensian villain in a modern suit, not a real-world businessman. Lean into the **caricature**: exaggerated features, period-feeling accessories (round wire-rim glasses, pocket watch on a brass chain, a small lapel pin shaped like a skyscraper), unnaturally still posture. Avoid any resemblance to actual public figures. If you find yourself sketching anyone famous, change three things until you don't.

## Physical

- **Age:** 60–65, but it's hard to tell — he could be a well-preserved 70 or a heavily-lined 55. Ageless in the way that makes you uneasy.
- **Height/build:** Tall and unnaturally thin. ~6'2" but reads taller because he sits perfectly straight. Long fingers. Narrow shoulders. Like an old crane that learned to wear a suit.
- **Skin:** Pale and slightly waxen — a man who hasn't been outside in years. Faint dark circles under the eyes that read as exhaustion or amusement depending on the angle.
- **Body language:** Unnaturally STILL. Most idle frames have zero motion — he doesn't fidget, doesn't drum, doesn't even seem to breathe. The hands rest flat on the desk. The head turns precisely, never absently. When he moves it's purposeful — like a chess piece being placed.
- **Face:** Distinctive caricatured features — **sharp narrow cheekbones**, **deep-set eyes**, **a long thin nose**, **a small precise mouth**. **The perpetual smile lifts only the LEFT corner of his mouth** — a half-smile that never reaches the eyes. The asymmetry is the tell. Drawn well, this should look unmistakably fictional, not photo-realistic.

## Hair

- **Pure white**, neatly slicked back from a sharp widow's peak. **A single dark grey streak runs through the right side** of the hair — visible in every frame. (Storywise: the streak is the same dark grey as his suit. Stylistically: it's instant character recognition.)
- Hairline starts unusually high — adds to the elongated-skull silhouette.

## Costume (head to feet) — Dickensian banker dressed for a 2026 boardroom

1. **Charcoal three-piece suit** — `#3a3a40` body with subtle 1-px pinstripe (`#4f4f57`) every 6 px. **Jacket cut LONGER than modern fashion** — the hem reaches mid-thigh, giving him a tall-coat silhouette. Single-breasted, two-button.
2. **White dress shirt** with a **stand-up wing collar** (period detail, not a modern collar) — `#f4f4f0`.
3. **Cravat-style silk tie** in **deep emerald green** — `#1a4a30` with a `#2a6a40` highlight. Tied in a fat knot like a 19th-century banker, not a modern Windsor.
4. **Charcoal vest** matching the suit, six buttons all done up. **A brass pocket-watch chain** loops across the vest from a buttonhole into the right vest pocket — `#cfa040` chain, visible 8–10 px arc.
5. **Round wire-rim glasses** — thin gold frames (`#cfa040`), perfectly round lenses ~3 px diameter. **These are the single biggest 'this is a fictional character' visual hook** — make them prominent.
6. **Dark slacks** matching the suit, perfect break at the shoe.
7. **Black leather oxford shoes** mirror-polished — `#08080a` with `#1c1c22` highlight.
8. **A single brass lapel pin shaped like a tiny skyscraper** on the left lapel — `#cfa040`, ~2 × 4 px. Replaces the "K" pin from the earlier spec. (Storywise: it's a model of the building you're currently fighting in.)
9. **Thin white cotton gloves** on both hands — `#dcd6c4`, the kind of gloves nobody wears indoors anymore. (Storywise: he doesn't like fingerprints. Stylistically: another 19th-century banker detail.)

## Identity items — REQUIRED IN EVERY FRAME

1. **The asymmetric half-smile** — left corner only. Always present. If the artist draws a full symmetric smile, the character reads as someone else.
2. **The round wire-rim glasses** — small, gold, perfectly circular.
3. **The single dark grey streak in white hair**.
4. **The skyscraper lapel pin**.
5. **The white cotton gloves**.
6. **The desk** — heavy dark mahogany (`#4a2818` body, `#1a0e08` shadow, `#6a3820` highlight), wide surface taking up the bottom third of every cell. His gloved hands rest flat on the desk in idle.
7. **The pocket-watch chain** arc across the vest.
8. **A small brass-caged finch** on the desk's left side — `#cfa040` cage, `#a8a4a0` bird inside. (Storywise: "the ones who don't fly are mine." Stylistically: cements the "Victorian banker" reading.)
9. **A folded contract + fountain pen** on the desk's right side, where Kane can reach them. The fountain pen is black with a gold cap (`#cfa040`), gestured with during the QTE prompts.

The combined silhouette — long jacket + stand-up collar + round glasses + slicked white hair with grey streak + pocket-watch chain + caged bird + gloved hands on mahogany desk — should read on first sight as **"this is a character from a story, not a person you saw on TV."**

## Palette (hex)

```
suit charcoal mid   #3a3a40
suit shadow         #1c1c22
suit highlight      #4a4a52
pinstripe           #4f4f57
shirt white         #f4f4f0
shirt shadow        #d4d4d0
cravat green        #1a4a30
cravat highlight    #2a6a40
cravat shadow       #08280c
vest dark           #2a2a30
shoe black          #08080a
shoe polish hi      #1c1c22
hair white          #e8e8e4
hair grey streak    #5a5a62
hair shadow         #a8a8a8
skin (light)        #d8c8b8
skin (shadow)       #a89488
skin (deep)         #6a5848
eye iris            #1a2030
glasses gold frame  #cfa040
glasses lens tint   #2a3040    (faint, low-alpha)
gloves white        #dcd6c4
gloves shadow       #a8a294
pocket watch chain  #cfa040
lapel pin gold      #cfa040
lapel pin shadow    #8a6020
desk mahogany       #4a2818
desk shadow         #1a0e08
desk highlight      #6a3820
finch cage gold     #cfa040
finch grey          #a8a4a0
contract paper      #f8f4e8
fountain pen black  #0a0a10
fountain pen gold   #cfa040
```

## Personality / behavior

- **Polite. Patient. Genuine.** Kane *means* what he says. He thinks the protagonist is being unreasonable. He believes he is the rational party.
- **Speaks softly.** Multiple lines during the QTE — each prompt the protagonist hits is a refusal of one of Kane's points:
  - **Prompt 1:** "I understand you're upset. I would be too. Let me make it right."
  - **Prompt 2:** "Three million. To you, today. Walk out of this building rich."
  - **Prompt 3:** "Your friends in the gym? They get the next ten years rent-free. Marcus would have wanted that."
  - **Prompt 4:** "Sit down. Sign the paper. Or I'll find someone in your life who *will*."
  - **Prompt 5 (final):** "...I see."
- **Never breaks composure.** No raised voice, no anger. The threat in Prompt 4 is delivered with the same warm half-smile as the offer in Prompt 1.
- **The finch chirps once between prompts.** Kane never looks at it.

## Animations (cinematic frames, not a fighter sheet)

Because Kane is a QTE encounter, he doesn't have combat animations. Instead, he has **scene poses** — one per beat of the dialog. These are the frames the cinematic crossfades between.

| Pose            | Notes |
|-----------------|-------|
| `seated_open`   | Idle. Gloved hands folded on desk, half-smile, eyes on protagonist. Finch perfectly still. |
| `lean_in`       | Plays during Prompt 1. Leans forward, elbows on desk, gloves now flat on the wood. |
| `gesture_open`  | Plays during Prompt 2. Right hand extended palm-up offering the contract. Pen still in left hand. |
| `gesture_pen`   | Plays during Prompt 3. Pen pointed at protagonist — gentle, like a teacher. |
| `gesture_hard`  | Plays during Prompt 4. Pen tip lowered to the document. The half-smile is the same; the eyes are cold for ONE beat. |
| `lean_back`     | Plays during Prompt 5. Leans back in chair, sets pen down, gloved hands fold again on the desk. The half-smile NEVER drops. |
| `quiet`         | Final pose after the QTE ends. Same as `seated_open` but fully still. The protagonist walks out; Kane remains. The finch remains. |

Kane never stands. He never throws a punch. The lack of motion is the menace.

## DO NOT include

- **Any resemblance to a real, named public figure.** If a draft looks like a known person, change features until it doesn't.
- A full symmetric smile. The smile is always lopsided (left corner only).
- Standing or fighting poses. Kane is seated for the entire encounter.
- Modern phone, laptop, computer, or tablet on the desk — period-feeling props only: the contract, the fountain pen, the caged finch.
- Disheveled hair, loose tie, unbuttoned vest, removed gloves. *Perfect* always.
- Visible jewelry beyond the lapel pin and pocket-watch chain. No wedding ring in this revision — the gloves cover the hands anyway, and the ring was real-person-coded.

## Sheet specs

- 4 columns × 2 rows = 8 cells (one per pose, plus 1–2 spares for in-between frames if you want crossfades)
- Cell size: **128 × 128** — Kane needs the horizontal width because the desk is part of the silhouette. The desk extends across the full cell.
- Magenta `#ff00ff` background OR transparent (Kane scenes draw over a darkened penthouse interior in the cinematic)
- Anchor: bottom-center, but the desk itself anchors the frame more than Kane's body

## Cinematic-fight design notes

- Plays as **STATE: cinematic** (already wired in the engine).
- 5 prompt-presses total, each at a specific timestamp. Hitting on time = refusal lands. Missing = the prompt's offer "almost convinces" the protagonist (visual: the protagonist's silhouette tilts toward the desk for a beat).
- All 5 prompts hit = victory. Kane says "...I see." and the cinematic ends. Game proceeds to the victory screen.
- All 5 missed = bad ending: the protagonist signs. Stage fails. (We can implement this as a future variant; for v1, keep the prompts hittable.)
- Music: a stripped-down version of the `kane` theme — bass and a single sparse lead. Removes the drums for the duration of the cinematic so Kane's voice has room.
