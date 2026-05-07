# THE BLOCK — Production Roadmap

Status as of the last commit on `claude/build-beatem-up-game-HDqjt`. Phases 1-5 are systems-complete (procedural rendering); from here it's content polish, art replacement, and shipping logistics.

---

## Where we are

**Code:** feature-complete for the spec.

- [x] **Phase 1** — engine, fixed-step loop, Rio playable, RUNNER + hit detection
- [x] **Phase 2** — combo chains, heavy launcher, jump attack, dodge, parry system, Sunset Spin / Rolling Thunder / Foundation Stone, grab+throw, back attack, full Duke + Atlas, scaled hit feel, milestone words
- [x] **Phase 3** — 7 additional enemy types (Tank, Lamplight, Slice, Chains, Shade, Dojo, Rig), stages 2-5 with hazards, BARON boss (Stage 3), localStorage save / unlocks / scoring
- [x] **Phase 4** — stages 6-10 + RAZOR / VOLT / BLACKWELL bosses + Kane QTE, character select with personality vignettes, mobile touch + haptics, audio (procedural WebAudio), gamepad polling (Standard Mapping), pause menu, accessibility (reduce flash / shake), difficulty (Story / Normal / Brutal), opt-in sprite atlas loader
- [x] **Phase 5** — `pipeline.py` (validate / palette / manifest / release / process-sheet), `sprite_slicer.html` (interactive sheet annotator), landing page template, character bible, this roadmap

**Visual ceiling:** the game ships fully playable with procedural `fillRect` rendering. Sprites are an upgrade path, not a dependency.

---

## What's next (your work, not the engine's)

These are the actual blockers to release. The order is intentional — don't paint before you've felt how the game plays in friends' hands.

### 1. Playtest pass (1–2 weeks)

Goal: one weekend per playtester, three or four playtesters total. We're answering five questions:

- Does the parry system feel like the headline mechanic, or like a finicky timing puzzle?
- Are the enemy patterns readable on first encounter, or do tells need to be louder?
- Are stages distinguishable enough that playtesters describe them by name rather than number?
- Is the Story difficulty actually accessible, or just slower-Brutal?
- Does the Kane QTE land emotionally, or feel anticlimactic?

Tune from those answers. The frame data is data — bring a notebook, change values, retest. Don't change the systems unless a system itself is broken.

### 2. Music (~2 weeks of evenings)

12-15 tracks at $10/mo Suno. Genres:

- THE BLOCK / UPTOWN: minor-key funk, slow walking bass
- THE TUNNELS / RIVER ROW / THE WORKS: industrial dub, low filter sweeps
- LANTERN ROW: warm mid-tempo pads with light percussion
- THE CAGE: heavy drums, distorted bass, crowd noise sample
- THE FREEWAY: synthwave with car-pass samples
- THE TOWER / THE TOP: tense ambient → chase pulse → final clash
- BARON / RAZOR / VOLT / BLACKWELL: per-boss themes (a third of the duration of stage themes)
- TITLE / SELECT / VICTORY / GAME OVER

Generate 50+ candidates per slot. Pick the one that sounds like it walks the way the character walks.

### 3. SFX (~1 week)

Existing procedural WebAudio sounds ship; replacing with real samples is optional and you can stage it. Targets:

- 4 hit weights (light / medium / heavy / KO)
- 3 parry tiers (perfect / good / late)
- 1 dodge whoosh, 1 jump grunt, 1 land thud
- 8 footstep variants (per surface — concrete / metal / wood / marble)
- 1 special move per character (Sunset Spin sweep, Rolling Thunder elbows, Foundation Stone slam)
- 4 boss intro stings
- 1 victory cheer, 1 game-over swell

Sources: Sonniss GameAudioGDC packs (free annually, royalty-free), Freesound CC0, JSFXR for retro game sounds.

### 4. Art (~30 hours per character + ~6 hours per stage; biggest cost)

Per **CHARACTER_BIBLE.md** the per-character frame budget is ~80 unique frames. Per the project brief, this is the actual blocker — not the code.

Workflow:

1. AI-generate rough sprite sheets per anim slot (Gemini / Stable Diffusion / Pixellab)
2. Hand-clean in LibreSprite / Aseprite — palette discipline is the priority
3. Drop `<charkey>.png` and `<charkey>_atlas.json` next to `the_block.html` and the engine picks them up automatically (Phase 4.5 loader)
4. Iterate against playtest feedback

Stage backgrounds: each stage already has procedural backdrop. Sprite stage backgrounds are an extension, not a replacement.

**Be honest about the legal status.** US Copyright Office: AI-generated art is not copyrightable. Steam requires AI disclosure. Some buyers will refuse on principle. Anyone can copy uncopyrighted assets. You decided to accept these tradeoffs; the procedural fallback exists so you can ship without crossing that line if you change your mind.

### 5. Steam page + itch page (~1 week)

- Trademark search "The Block" before listing. Likely conflicts; have alternates ready (HOLD THE LINE, FOUR CORNERS, NO QUARTER, CONCRETE & STEEL).
- Capsule art, header art, logo, screenshots (5–10), one trailer (60–90s)
- Long description (~500 words), short description (~140 chars)
- Demo build (separate Steam depot)
- Wishlist link from `landing.html`

### 6. Marketing (continuous, see MARKETING.md)

Set a launch date 3 months out. Work backward.

### 7. Launch (1 day, exhausting)

Same-day launch on Steam + itch.io. Twitter / Bluesky / Mastodon thread. Press kit ready. Discord channel for bug reports.

### 8. Post-launch (1 month)

Patch obvious bugs in the first 2 weeks. Add character costume variants per **CHARACTER_BIBLE.md**. Possibly an endless mode (the engine supports it; STAGES table just needs an "endless" generator).

Mobile port: the touch overlay already works. Wrap with Capacitor or just leave as a PWA.

---

## Realistic timeline (solo dev, evenings + weekends)

| Phase                    | Weeks |
|--------------------------|------:|
| Playtest + tuning         | 2     |
| Music                     | 2     |
| SFX                       | 1     |
| Art (3 chars + bosses)    | 12    |
| Steam / itch listings     | 1     |
| Marketing pre-launch      | 8 (parallel) |
| Bug fixes / final polish  | 2     |
| Launch                    | 0.2   |
| Post-launch patches       | 4     |

**Total: ~24 weeks (six months) from end-of-systems to launch.**

If you push art entirely off to AI generation without manual cleanup it's faster but the quality hit is steep enough that you'll lose more in store-page conversion than you save in dev time. Don't.

---

## Budget targets (sub-$1500)

- Suno Pro: $10/mo × 6 = $60
- Aseprite license: $20 one-time
- Steam app fee: $100 one-time
- Domain + landing hosting: $30/yr
- Stock SFX (if not free): $50–$100
- Logo / capsule art commission (recommended; AI here is more visible): $200–$400
- Trademark search service: $50

**Total floor: ~$460. Total ceiling: ~$760.** Leaves room for a couple of paid playtest sessions and unexpected costs.

---

## Revenue target

$5,000–$50,000 lifetime, per the original brief. The plan is sound for that band: ~500–5,000 copies at the indie tier. Anything more is upside.

---

## Don't do (until after launch)

- Multiplayer (engine doesn't support netcode; rebuilding the loop costs more than it earns)
- Procedural levels (stages are designed encounters; randomizing dilutes them)
- A second story arc (the gentrification angle is the hook — don't dilute it with side plots before the main story has been seen)
- Microtransactions / monetization beyond the base sale
- Console certification (until itch and Steam revenue justifies the certification cost)
