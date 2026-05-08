# THE BLOCK — Character Bible

Single source of truth for art direction, voice, and design. Anything that contradicts this file is wrong; update the file first.

---

## Tone (applies to everyone)

Direct. Lived-in. Weary. Small-scale stakes — one neighborhood, one gym. Nobody is "saving humanity." They're saving the corner where they live and the people they know on it.

Avoid:

- "Evil rises" / "fate of humanity" / "the chosen one" framing
- Speeches longer than two sentences
- Banter that breaks the tone (no quips, no one-liners)
- Treating the developer (Kane) as a cartoon villain — he's a real-world type

Voice direction (if/when VO is recorded): low effort, conversational, breath. No theatrical projection. Hits should sound tired, not heroic.

---

## RIO

**Age 24. Speed / finesse fighter. Speed 5 / Power 2 / Range 3.**

### Visual

- Dark brown skin (`#6b3f2a` / `#8a5235`)
- Full afro, dark brown to black, ~3-4 inches deep
- Cropped olive bomber jacket (`#5a6b3a` / `#7d8d4f`)
- Black tank top under (`#0a0a10`)
- Slim cargo pants (`#1a1a22`)
- Ankle boxing boots (`#0a0a10`)
- Hand wraps, exposed knuckles (`#dcd6c4`)
- Single small gold hoop earring (camera-side)
- **Yellow bandana on left wrist (`#e8c04a`) — signature item, must always be visible.**
  Rendered camera-side regardless of facing so it never hides behind the body.
  Trails through the air on the punch arc; whips through the full circle on
  Sunset Spin.

### Personality

Calm. Deadpan. Smiles when she lands a clean combo (the one moment her face changes — useful for cinematics). Speaks rarely. When she speaks she's quiet enough you have to lean in.

### Backstory (canonical)

Foster care. Learned to fight on the streets — actual streets, not metaphor. Marcus, a retired pro boxer, caught her sparring strangers for cash on a corner near his gym and took her in. He was the first person who showed up for her without wanting something. He died last year. She runs his old gym free for kids now. **The block being torn down is the block where Marcus first found her.** That's why she's here.

### Signature: Sunset Spin

Spinning leg sweep into a rising double-fist uppercut. Yellow bandana trails through the arc — the spin pulls it into a wide ribbon, the uppercut sends it skyward. Implementation in the engine: 5 frames startup, 18 frames active (multi-hit, every 5 frames), 14 frames recovery, costs 10 HP, last 3 active frames upgrade to a launcher.

### Voice direction

If/when recorded: a quiet alto, just above a whisper. Dry. Most reactions are an exhale, not a word. When she does speak: complete sentences but short. No fillers.

### Costume variants (post-launch)

- Marcus's old hoodie (oversized, his colors)
- Tournament fight night (shorts + wraps, no bandana — narrative impact reserved)

---

## DUKE

**Age 31. Balanced fighter. Speed 3 / Power 4 / Range 3.**

### Visual

- Weathered pale skin (`#d4a888`), several days of stubble
- Messy dark blonde hair (`#a08c4a`), uneven top, a wayward strand to one side
- Faded denim cut-off jacket (`#5a6678` / `#404a5c`) with ragged hem
- Stained white t-shirt under (`#cfc8b8`)
- Dark jeans (`#2a2e3a`), worn-in
- Beat-up combat boots (`#161618`)
- **Cigarette behind one ear (never lit, always there) — small white stick with a brown tip on the camera-side ear**

### Personality

Tired. Cynical. Half-finished sentences. Occasional swearing when pissed. Doesn't trust himself, doesn't expect others to trust him. Doesn't talk about the years between his boxing career and now.

### Backstory (canonical)

Semi-pro boxer until a knee injury ended it. After that: bouncing. Debt collection. Things he doesn't talk about. Came back when he heard the gym was in trouble. Tells himself it's about the gym. It's about Marcus, who once kept him out of jail when nobody else would. He owes that. He'll never say so.

### Signature: Rolling Thunder

Three-hit elbow combo finishing with a haymaker that drops his weight into the strike. Each elbow has a speedline; the haymaker has a diagonal impact crack. Implementation: 6 startup, 14 active (multi-hit), 16 recovery, hpCost 8, finalLauncher 80, pushSelf 60 px/s — he stomps forward through the combo.

### Voice direction

Tenor that's seen better days. Dry, slightly raspy. Half-mumbled. When he swears it's flat, like he's stating a fact, not venting.

### Costume variants

- Boxing gym kit (open robe, gloves)
- Debt-collection era (longer jacket, harder eyes)

---

## ATLAS

**Age 47. Power / grappler. Speed 2 / Power 5 / Range 4.**

### Visual

- 6'4". Massive (powerlifter physique, slightly soft now)
- Dark olive complexion (`#7a5234` / `#583820`)
- Bald head, full salt-and-pepper beard (`#a8a4a0`)
- Sleeveless deep-red flannel (`#7a3030` / `#5a1c1c`), sleeves torn off, top three buttons undone
- Heavy work pants (`#3a3024`) with a wide leather belt and brass buckle
- Steel-toed boots (`#1c140c`)
- **Faded geometric tribal forearm tattoos (1-pixel bands)** on both bare arms
- **Silver wedding band on a chain around his neck (`#c0c0c8`)** — visible
  through the open V of the flannel

### Personality

Father energy. Slow to anger and terrifying when he gets there. Calls everyone "kid." Listens before he speaks. Knows everybody's name on the block. Believes the law works because for two decades it has — it's the part of him that still has to break in this story.

### Backstory (canonical)

Gym regular for 20 years. Owns the hardware store next door. Married. Kids in college. Has been holding the block together legally, financially, and physically against developers for years — file lawsuits, pay legal fees, stand his ground at council meetings. Now they sent people he can't reason with. He's not a fighter anymore — he's a man who used to be — and that's exactly why he's coming back.

### Signature: Foundation Stone

Running shoulder charge with three speedlines, picks the enemy up, two-handed slam. The ground shakes. Implementation: 8 startup, 12 active (multi-hit + pushSelf 90 px/s), 22 recovery, hpCost 12, finalLauncher 240. The slam pose plants both feet, both fists overhead, with a dust burst at the feet on contact.

### Voice direction

Bass, slow, careful. Doesn't raise his voice. Shouts only when something is genuinely on fire. The "kid" is gentle, never patronising.

### Costume variants

- Council meeting suit (the clothes he wears when he's still trying to do this the right way)
- Gym vest from his prime (size XXXL, faded)

---

## VICTOR KANE (the antagonist)

**Late 50s. Real-estate developer. Never throws a punch onscreen.**

### Visual

- Tall, slightly stooped
- Expensive suits (`#22202c` / `#3a3848`) with a cream pocket square (`#cfa040`)
- Slick-back grey hair (`#6a6a64`)
- White shirt, deep-red tie (`#5a1018`)
- Calm, narrow eyes — never wide
- Always rendered as a silhouette in cinematics. The story makes the point that
  he doesn't lift his own hands; the framing should reinforce that.

### Personality

Polite. Patient. Has lawyers. Speaks in numbers and zoning code. Will smile when he tells you it's been a pleasure. Believes the block was always going to fall — he's just the one collecting the fee. That's the worst thing about him.

### Backstory

Built a portfolio across the city by buying out resistant blocks one at a time. Has done this before. Will do it again somewhere else after this. The block is just the next address in a list.

### How he appears in the game

- Stages 1-9: never seen onscreen. His name is on signs, in newspaper clippings on the title fade-in, in the tape barrier across the gym entrance.
- Stage 10 boss: **the Enforcer** (BLACKWELL) is the actual fight. Kane watches.
- Final QTE: a direct confrontation with him on the rooftop. He still doesn't throw a punch. The player presses J/K to land four strikes; the cinematic ends with him on the ground. *He gets back up to consult his lawyer in any post-credits sequence.* That's the point.

---

## Marcus (offscreen — but central)

The trainer who took Rio in, kept Duke out of jail, was the gym for Atlas's prime. Dies a year before the game starts. **Never appears onscreen.** Lives in the gym walls — photographs in the background, a faded poster of his old fight card, a spot at the heavy bag where the wrap is still taped down to his preferred radius.

Each character's reason for fighting traces back to him without ever needing exposition. Don't write a flashback.

---

## Visual rules

- All three protagonists keep palette discipline at all times. Don't add unsupported colors during animation.
- Drop shadows are always on the ground (not under the body); shrink with elevation.
- Damaged poses use the existing iframe flash, not new colors.
- Bandana, cigarette, wedding band — these are the **identity items.** They are visible in every frame they could possibly be visible in. If a frame omits one, the frame is wrong.

## Animation requirements (per character)

Required anim slots (atlas keys):

```
idle  walk  run  jump
atk1  atk2  atk3  heavy  jump_atk  back_atk
special  throw  counter  hurt  dodge
```

The engine renders procedural fallback for any anim that's missing from the atlas, so partial atlases ship fine.

Frame counts (suggested minimum for sprite art):

| Anim       | Frames |
|------------|--------|
| idle       | 4      |
| walk       | 6      |
| run        | 6      |
| jump       | 3      |
| atk1       | 4      |
| atk2       | 5      |
| atk3       | 6      |
| heavy      | 7      |
| jump_atk   | 4      |
| back_atk   | 4      |
| special    | 12     |
| throw      | 5      |
| counter    | 6      |
| hurt       | 3      |
| dodge      | 5      |

Total: ~80 frames per character × 3 characters = ~240 unique frames. At 10–30 minutes per frame from AI-generated rough → cleanup, that's the ~30-hour-per-character budget.
