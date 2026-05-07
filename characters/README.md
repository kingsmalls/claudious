# Character build files

One file per character. Each file is **self-contained** — hand it to your AI generator (or artist) without any other docs and they have everything they need to build that character's full sprite sheet.

| File | Character | Length |
|---|---|---|
| `RIO.md` | Rio — 24, Black, locs, olive bomber jacket, **yellow bandana on left wrist** | 224 lines |
| `DUKE.md` | Duke — 31, white, blonde messy hair, denim cut-off jacket, **never-lit cigarette behind one ear** | 220 lines |
| `ATLAS.md` | Atlas — 47, mixed/Mediterranean, bald + full salt-pepper beard, sleeveless red flannel, **silver wedding band on chain + tribal forearm tattoos** | 234 lines |

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
