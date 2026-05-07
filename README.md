# THE BLOCK

Three fighters defend their neighborhood gym from a developer who's tearing the block down. A 2D side-scrolling beat-em-up about gentrification, not generic revenge.

---

## Status

**Systems-complete.** All 17 milestones from the production plan are landed:

- HTML5 canvas single-file engine, 60Hz fixed-timestep loop
- 3 playable characters: **Rio** (speed/finesse), **Duke** (balanced), **Atlas** (power)
- Per-character toolkits: 3-hit chain combo, heavy launcher, jump attack, dodge,
  back attack, signature special (Sunset Spin / Rolling Thunder / Foundation Stone),
  grab + directional throw, parry counter-special
- **Tiered parry system** (PERFECT / GOOD / LATE windows, chain meter, free counter at full)
- 8 enemy types + 4 bosses (BARON / RAZOR / VOLT / BLACKWELL) + Kane QTE finale
- 10 stages with hazards (water on RIVER ROW, molten metal on THE WORKS, cars on THE FREEWAY)
- Full HUD: HP bar, parry meter, combo counter with milestone words ("NICE!" / "AWESOME!" / "BRUTAL!" / "INSANE!" / "RUTHLESS!"), boss HP bar
- Modern hit feel: scaled hitstop, screen shake, damage tier sparks, floating numbers, screen flash
- Title + character select with personality vignettes, victory + game over with run recaps
- Mobile touch controls overlay + haptics
- Full gamepad support (Standard Mapping)
- Audio: 16 procedural WebAudio SFX with master/SFX volume + mute
- Pause menu with difficulty (Story / Normal / Brutal), accessibility (reduce flash / shake), audio settings
- Save / load via localStorage: high scores per character, best combo per stage, character unlocks (Atlas unlocks after 3 stage clears)
- Opt-in sprite atlas loader (drop `<char>.png` + `<char>_atlas.json` and the renderer prefers sprites)
- `pipeline.py` asset tool: validate-atlas, extract-palette, manifest, release, process-sheet
- `sprite_slicer.html` interactive sheet annotator
- `landing.html` wishlist landing page template

The game **runs and ships fully playable** on procedural `fillRect` rendering. Sprites are an upgrade path, not a dependency.

---

## How to play

Open `the_block.html` in any modern browser. No build step, no install.

### Controls

| Action  | Keyboard           | Gamepad (Standard) | Touch       |
|---------|--------------------|--------------------|-------------|
| Move    | WASD or arrows     | Left stick / D-pad | D-pad       |
| Jump    | Space              | A                  | JMP         |
| Light   | J                  | B (or X)           | J           |
| Heavy   | K                  | Y                  | K           |
| Special | L                  | RT                 | L           |
| Grab    | U                  | LB                 | U           |
| Parry   | I                  | RB (or LT)         | P           |
| Dodge   | down + jump        | down + A           | ▼ + JMP     |
| Run     | double-tap left/right | stick / d-pad   | double-tap  |
| Pause   | P                  | Start              | (planned)   |
| Debug   | F3 (DEV builds)    | —                  | —           |

### Combo flow

- J → J → J chains atk1 → atk2 → atk3 (jab → cross → hook).
- J then K cancels into the heavy uppercut launcher.
- Press I when an enemy attack is coming to parry. Frames 1-3 land a PERFECT (counter damage + heal at chain ≥ 2). Frames 4-7 land a GOOD (stuns the attacker). Frames 8-12 land a LATE (block only).
- Build the parry meter to 100% — your next light or heavy press fires a free counter-special with no HP cost.
- Heavy hits launch enemies — chain a jump attack into the juggle.

---

## Project layout

```
the_block.html        — the game (single-file HTML5 build)
sprite_slicer.html    — interactive sprite-sheet annotator (Phase 5.2)
landing.html          — wishlist landing page template (Phase 5.3)
pipeline.py           — asset pipeline CLI tool (Phase 5.1)
smoke.js              — headless test harness (jsdom + node-canvas)
CHARACTER_BIBLE.md    — canonical character documentation
ROADMAP.md            — production roadmap to launch
MARKETING.md          — pre-launch / launch / post-launch checklist
README.md             — this file
```

---

## Headless smoke test

```bash
# One-time install (anywhere; NODE_PATH points at it)
cd /tmp && npm install jsdom canvas

# Run from the project root
NODE_PATH=/tmp/node_modules node smoke.js
```

The harness drives synthetic input through a deterministic 60Hz frame stepper, dumps PNG snapshots at key moments, and reports a non-zero exit code if any error fires. Useful for catching regressions during refactors.

---

## Tech stack

**Primary:** HTML5 Canvas, vanilla JavaScript, no build step. Single file is the deliverable. Procedural rendering is the always-available fallback so the game ships even with zero sprite art.

**Secondary (deferred):** `TheBlock_Unity.cs` for native ports — not started; will arrive after the HTML build proves itself in player hands.

**Render context** is the global `X` (per project convention). Game state lives in module-level `let` variables; no class-based state hierarchy. Frame counts in `ATTACK_DATA` and `ENEMY_ATK` are 60Hz fixed-step ticks, not seconds — combat is frame-precise.

---

## Asset strategy (real talk)

The art and music are the actual blockers — not the code. The procedural fallback exists so this fact doesn't gate shipping.

- **Sprites:** AI-generated rough → manual cleanup in LibreSprite/Aseprite → atlas via `sprite_slicer.html` → drop `rio.png` + `rio_atlas.json` next to the HTML, the engine picks them up. Budget ~30 hours per character per the brief.
- **Music:** Suno paid tier ($10/mo). Generate 50+, pick best 12-15. Genres per stage in `ROADMAP.md`.
- **SFX:** Freesound CC0, Sonniss GameAudioGDC packs (free annually), JSFXR. The procedural WebAudio sounds in `the_block.html` ship by default.

**Legal note:** US Copyright Office: AI-generated art is not copyrightable. Steam requires AI disclosure. Some buyers will refuse on principle. The dev has accepted these tradeoffs; the procedural fallback exists in case you change your mind.

---

## What this game is, and isn't

It's an indie beat-em-up in the Fight'N Rage / 99Vidas / River City Girls tier, with a tone closer to social-realist storytelling than genre cliché. Stakes are small — one neighborhood, one community center.

It is not trying to beat Streets of Rage 4 — that's a $2-5M studio production. Realistic revenue band: **$5,000–$50,000 lifetime.** That's the plan.

---

## Working title

**THE BLOCK.** Trademark search before any storefront listing. Alternates: HOLD THE LINE, FOUR CORNERS, NO QUARTER, CONCRETE & STEEL.

---

## Branch & pull workflow

The systems work landed on `claude/build-beatem-up-game-HDqjt`. Pull, open `the_block.html` in a browser, play. If you want to keep iterating, branch from there.
