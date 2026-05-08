# KANE — Final Boss

**Victor Kane.** Real-estate developer. Founder and CEO of **Kane Properties LLC**. The reason every other fight in this game happens.

Kane has never thrown a punch in his life. He doesn't need to. Other people throw the punches; Kane writes the contracts. When the protagonist reaches him at the top of his tower, the fight is a **QTE cinematic**, not a brawl. Kane stays seated at his desk. He talks. He offers a check. The protagonist refuses.

You don't beat Kane with violence. You beat him by refusing the deal.

This is the most important character in the game — the entire campaign points at him. The art has to read on first sight as: *this man owns everything. He owns the room. He owns the city. He owns the conversation.*

## Physical

- **Age:** 58
- **Height/build:** 5'11", lean, fit. Looks 50, not 58. Maintains his body the way he maintains his portfolio. Yoga and morning runs.
- **Skin:** White, slightly tan from a recent vacation. Smooth.
- **Body language:** Composed. Sits forward in his chair when interested, leans back when bored. Doesn't fidget. The hands tell you everything — fingers steepled or folded, occasionally drumming the desk.
- **Face:** Sharp features. Thin lips. Eyes that look genuinely interested in whoever he's talking to. **Always smiling.** Not a smirk — a real, warm smile. The smile is the menace.

## Hair

- Silver-grey, slicked back. Perfectly styled. Receding slightly at the temples. Never moves.

## Costume (head to feet)

1. **Bespoke charcoal three-piece suit** — `#3a3a40` with subtle pinstripe (a 1-px lighter line every 6 px). Single-breasted jacket, perfect tailoring. Fits like it was sewn onto him.
2. **White dress shirt** — crisp, starched white (`#f4f4f0`).
3. **Dark burgundy silk tie** — `#4a1018`, perfectly knotted.
4. **Three-piece vest** — same charcoal as the suit, six buttons all done up.
5. **Dark slacks** matching the suit, perfect break at the shoe.
6. **Black oxford shoes** — mirror-polished. `#08080a` with a `#1c1c22` highlight.
7. **A gold cufflink visible on each sleeve** — `#f4c860`, ~2 × 2 px.
8. **A single gold ring on the left hand** — wedding band. (His wife is dead; he still wears it. Not for sentiment — for the *image*.)

## Identity items — REQUIRED IN EVERY FRAME

1. **The smile.** Always smiling. Even when the protagonist refuses, even when the building shakes, even when his lieutenants have all fallen — Kane smiles. The smile is what makes him terrifying.
2. **The desk.** Kane sits behind a heavy mahogany desk during the entire encounter. The desk is iconic — a wide, dark wood surface with a single document and a fountain pen on it. His hands rest on the desk in idle.
3. **The fountain pen** — black with a gold cap (`#f4c860`), held casually in the right hand during many frames. He uses it to gesture, to point, to offer to sign a check.
4. **A leather-bound checkbook** open on the desk — visible from F1 onward. The check is the *real* weapon. The protagonist has to refuse it.

## Palette (hex)

```
suit charcoal mid  #3a3a40
suit shadow        #1c1c22
suit highlight     #4a4a52
pinstripe          #4f4f57
shirt white        #f4f4f0
shirt shadow       #d4d4d0
tie burgundy       #4a1018
tie hi             #6a1828
vest dark          #2a2a30
shoe black         #08080a
shoe polish hi     #1c1c22
hair silver        #b8b8bc
hair shadow        #6a6a72
hair highlight     #d4d4d8
skin (light)       #e8c4a0
skin (mid)         #c89878
skin (shadow)      #8a6a4a
gold cufflink      #f4c860
gold ring          #cfa040
desk mahogany      #4a2818
desk shadow        #1a0e08
desk highlight     #6a3820
checkbook leather  #2a1810
fountain pen black #0a0a10
fountain pen gold  #f4c860
paper white        #f8f4e8
ink blue           #1a3a8a
```

## Personality / behavior

- **Polite. Patient. Genuine.** Kane *means* what he says. He thinks the protagonist is being unreasonable. He believes he's the rational party.
- **Speaks softly.** Multiple lines during the QTE — each prompt the protagonist hits is a refusal of one of Kane's points:
  - **Prompt 1:** "I understand you're upset. I would be too. Let me make it right."
  - **Prompt 2:** "Three million. To you, today. Walk out of this building rich."
  - **Prompt 3:** "Your friends in the gym? They get the next ten years rent-free. Marcus would have wanted that."
  - **Prompt 4:** "Sit down. Sign the paper. Or I'll find someone in your life who *will*."
  - **Prompt 5 (final):** "...I see."
- **Never breaks composure.** No raised voice, no anger. The threat in Prompt 4 is delivered with the same warm smile as the offer in Prompt 1.

## Animations (cinematic frames, not a fighter sheet)

Because Kane is a QTE encounter, he doesn't have combat animations. Instead, he has **scene poses** — one per beat of the dialog. These are the frames the cinematic crossfades between.

| Pose       | Notes |
|------------|-------|
| `seated_open`   | Idle. Hands folded on desk, smile, eyes on protagonist. |
| `lean_in`       | Plays during Prompt 1. Leans forward, elbows on desk. |
| `gesture_open`  | Plays during Prompt 2. Right hand extended palm-up offering the check. Pen still in left hand. |
| `gesture_pen`   | Plays during Prompt 3. Pen pointed at protagonist (gentle). |
| `gesture_hard`  | Plays during Prompt 4. Pen tip lowered to the document. The smile is the same; the eyes are colder for one beat. |
| `lean_back`     | Plays during Prompt 5. Leans back in chair, sets pen down, hands folded again. The smile NEVER drops. |
| `quiet`         | Final pose after the QTE ends. Same as `seated_open` but fully still. The protagonist walks out; Kane is still there. |

Kane never stands. He never throws a punch. The lack of motion is the menace.

## DO NOT include

- A scowl, an angry face, or any visible negative expression. The smile is permanent.
- Standing or fighting poses. Kane is seated for the entire encounter.
- Tactical / combat gear of any kind.
- Disheveled hair, loose tie, unbuttoned vest. *Perfect* always.
- Modern phone, laptop, or computer on the desk — period-feel: the document, the pen, the checkbook. That's all.

## Sheet specs

- 4 columns × 2 rows = 8 cells (one per pose, plus 1–2 spares for in-between frames if you want crossfades)
- Cell size: **128 × 128** — Kane needs more horizontal width because the desk is part of the silhouette. The desk extends across the full cell.
- Magenta `#ff00ff` background OR transparent (Kane scenes draw over a darkened penthouse interior in the cinematic)
- Anchor: bottom-center, but the desk itself anchors the frame more than Kane's body

## Cinematic-fight design notes

- Plays as **STATE: cinematic** (already wired in the engine).
- 5 prompt-presses total, each at a specific timestamp. Hitting on time = refusal lands. Missing = the prompt's offer "almost convinces" the protagonist (visual: the protagonist's silhouette tilts toward the desk for a beat).
- All 5 prompts hit = victory. Kane says "...I see." and the cinematic ends. Game proceeds to the victory screen.
- All 5 missed = bad ending: the protagonist signs. Stage fails. (We can implement this as a future variant; for v1, keep the prompts hittable.)
- Music: a stripped-down version of the `kane` theme — bass and a single sparse lead. Removes the drums for the duration of the cinematic so Kane's voice has room.
