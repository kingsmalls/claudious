# Character build files

One file per character. Each file is **self-contained** — hand it to your AI generator (or artist) without any other docs and they have everything they need to build that character's full sprite sheet.

## Playable protagonists

| File | Character | Length |
|---|---|---|
| `RIO.md` | Rio — 24, Black, **full afro**, olive bomber jacket, **yellow bandana on left wrist** | 224 lines |
| `DUKE.md` | Duke — 31, white, blonde messy hair, denim cut-off jacket, **never-lit cigarette behind one ear** | 220 lines |
| `ATLAS.md` | Atlas — 47, mixed/Mediterranean, bald + full salt-pepper beard, sleeveless red flannel, **silver wedding band on chain + tribal forearm tattoos** | 234 lines |

## Enemy minions (Kane's crews)

| File | Character | Identity item |
|---|---|---|
| `RUNNER.md` | Bottom-tier neighborhood thug, hoodie, panicked at low HP | Red bandana on right bicep |
| `TANK.md` | Heavy enforcer, tactical vest, super-armored | KANE PROPERTIES SECURITY badge |
| `LAMPLIGHT.md` | Masked gunman, balaclava, holds 70-110 px range | Pistol always visible |
| `SLICE.md` | Mesh-shirt knife specialist, hit-and-run | Bowie knife in reverse grip |
| `CHAINS.md` | Leather-vest brawler, holds ground | Industrial chain wrapped on forearm |
| `SHADE.md` | Hooded teleporter, almost all matte black | Purple-glow eyes + smoke trail |
| `DOJO.md` | Black-gi martial artist, parries hits | White training belt with two tails |
| `RIG.md` | Construction-worker AOE bruiser | Yellow hard hat with KANE logo |

## Bosses

| File | Character | Stage |
|---|---|---|
| `BARON.md` | Ex-cop boxer, brass knuckles, polite menace | Stage 3 |
| `RAZOR.md` | Corporate dual-knife specialist, suit, blonde streaks | Stage 6 |
| `VOLT.md` | Cybernetic enforcer, blue power-line glow | Stage 9 |
| `BLACKWELL.md` | Kane's personal bodyguard | Optional, brutal-only mid-stage 7/8 |
| `KANE.md` | The final boss — QTE cinematic, never throws a punch | Stage 10 |

## Each file contains

- **Physical** — age, height, build, posture, body language, face
- **Hair** — cut, length, movement
- **Costume (head to feet)** — every layer with material notes
- **Identity items** — what MUST be visible in every frame (the bandana / cigarette / chain are not optional)
- **Palette** — full hex codes per body part
- **Personality cues** — what should show through in poses
- **Animations** — frame-by-frame pose breakdown for all 15 engine slots:
  - `idle`, `walk`, `run`, `jump` (4 + 6 + 6 + 3 frames)
  - `atk1`, `atk2`, `atk3`, `heavy` (4 + 5 + 6 + 7 frames)
  - `jump_atk`, `back_atk` (4 + 4 frames)
  - `special` — the signature 12-frame move (Sunset Spin / Rolling Thunder / Foundation Stone)
  - `throw`, `counter`, `hurt`, `dodge` (5 + 6 + 3 + 5 frames)
- **Do NOT include** — the negative-prompt list
- **Sheet specs** — color discipline, outline, lighting, reference quality, sheet layout (8×10 grid at 64×96 cells), final integration steps

## Workflow

1. Open `RIO.md` (or `DUKE.md` / `ATLAS.md`).
2. Copy its full content into your generator prompt window.
3. Save the resulting sheet as `rio.png` (or `duke.png` / `atlas.png`) at the project root.
4. Open `sprite_slicer.html` in a browser, load the PNG, click cells to label each animation.
5. Export `<char>_atlas.json` next to the PNG.
6. Run `python3 pipeline.py validate-atlas rio_atlas.json` to confirm.
7. Reload `the_block.html` — that character switches from procedural to sprite rendering automatically.

## Combined reference

If you'd rather read all three side-by-side, `../CHARACTER_DESIGN.md` contains the same content in one document. The split files here exist to make copy-paste handoff easier.

## v1 art status (2026-05-08)

What landed in the current `<char>.png` sheets vs what the bible specifies. **Code-side integration is complete for all three** — these gaps are art tasks for v1.1.

### RIO ✅ — ships v1

- ✅ Yellow bandana on left wrist
- ✅ Olive bomber jacket
- ✅ Slim charcoal pants, ankle boxing boots
- ✅ Hand wraps
- ✅ All 15 anim slots labeled (idle / walk / run / jump / atk1–3 / heavy / jump_atk / back_atk / special / throw / counter / hurt / dodge)
- ✅ Sunset Spin special with bandana arc

### DUKE ✅ — ships v1

- ✅ Cigarette behind one ear (visible across animations)
- ✅ Blonde messy hair, denim cut-off vest, jeans
- ✅ Combat boots
- ✅ All 15 anim slots labeled
- ✅ Rolling Thunder special (3 elbows + haymaker)

### ATLAS ⚠️ — ships v1 with known gaps

- ✅ Bald, large frame
- ✅ Red plaid flannel (sleeveless)
- ✅ Heavy work pants
- ✅ All 15 anim slots labeled (atk3 trimmed to OVERHEAD CHOPPING SMASH, see commit `3abe39f`)
- ✅ Foundation Stone special with charge → lift → slam beats
- ❌ **Salt-and-pepper beard** — needs v1.1 art pass
- ❌ **Silver wedding band on chain** — needs v1.1 art pass
- ❌ **Tribal forearm tattoos** — needs v1.1 art pass
- ❌ Visible belt with brass buckle — needs v1.1 art pass

For v1.1 regen, hand `ATLAS.md` to the generator with explicit emphasis on the four `❌` items as REQUIRED-IN-EVERY-FRAME. Layout config (`layouts/atlas_layout.json`) and atlas JSON (`atlas_atlas.json`) stay valid as long as the new sheet matches the same 1024×559 / 16×6 grid.
