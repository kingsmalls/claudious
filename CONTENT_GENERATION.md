# Content generation with your Anthropic API key

`generate.py` is a dev-time script that uses your Anthropic API key to mass-produce game content. The output lands in `content/*.json` and gets baked into the static game — **no API calls happen during gameplay**, so shipping the game costs nothing per player.

## What it generates

| Command | Output | What it makes |
|---|---|---|
| `npc_chatter` | `content/npc_chatter.json` | Short bark lines that random offscreen NPCs shout during stages. 12 lines per stage, ~120 total. Wired into the game — appears in-game as floating text. |
| `enemy_variants` | `content/enemy_variants.json` | 4 named sub-types per enemy with custom stats, dialog, and 1-line backstory. Schema reserved for future engine wiring. |
| `boss_dialog` | `content/boss_dialog.json` | Per-boss dialog pool: intro (3 lines), midfight (8), taunt (6), defeat (3). Schema reserved. |
| `achievements` | `content/achievements.json` | **Already shipped with 30 achievements.** Re-running overwrites with fresh AI-generated copy. Triggers are already wired into the engine. |

## Setup

1. Install the Anthropic Python SDK:
   ```bash
   pip install anthropic
   ```
2. Set your API key:
   ```bash
   export ANTHROPIC_API_KEY=sk-ant-...
   ```
   (Windows PowerShell: `$env:ANTHROPIC_API_KEY="sk-ant-..."`)
3. Run a generator:
   ```bash
   python generate.py npc_chatter
   python generate.py achievements
   python generate.py all      # all four
   ```

Each command backs up the existing file to `<name>.bak.json` before overwriting so you can iterate safely.

Total cost for one full run: **under $1**. Uses `claude-sonnet-4-6` (latest Sonnet 4.x).

## How content flows into the game

```
generate.py        →    content/*.json    →    the_block.html (fetch at boot)
[Anthropic API]         [committed to repo]    [runtime: no API calls]
```

The game `fetch()`es each JSON file on boot, falls back to seeded defaults if a file is missing. Achievements unlock during play via triggers wired into the engine; NPC chatter pops up as floating text at random intervals during stages.

## What's wired vs. what's data-only

**Already wired into gameplay**:
- `npc_chatter.json` — drives the random offscreen bark text during stages
- `achievements.json` — drives the popup display, save-state, and tracks 30 achievement triggers

**Generated but not yet consumed by the engine** (the JSON files exist; the engine doesn't read them yet — they're documentation + future-work data):
- `enemy_variants.json` — would let the engine spawn named sub-types
- `boss_dialog.json` — would let boss intros/midfight/taunt pull from a pool of lines

These two can be wired up in a follow-up commit. For now, generating them gives you a content library you can manually grep and paste into the game.

## Achievement triggers — what's currently wired

Triggers fire from `unlockAchievement(id)` calls scattered through the engine:

| Achievement ID | When it fires |
|---|---|
| `first_stage` | Beat stage 1 |
| `first_boss` | KO Baron |
| `razor_down` | KO Razor |
| `volt_down` | KO Volt |
| `refuse_kane` | Hit all 5 prompts in the Kane QTE |
| `find_blackwell` | KO Blackwell (brutal-only encounter) |
| `first_combo_5` / `combo_10` / `combo_20` / `combo_30` | Combo milestones |
| `perfect_parry_1` / `perfect_parry_10` | Perfect parry counts |
| `parry_haymaker` | Perfect-parry Baron's haymaker specifically |
| `no_damage_block` | Clear stage 1 without taking damage |
| `rio_run` / `duke_run` / `atlas_run` | Beat the game with each character |
| `all_chars_clear` | Beat the game with all three |
| `brutal_clear` | Beat the game on brutal difficulty |
| `100_kos` / `500_kos` | Cumulative KO milestones |
| `all_stages_clear` | All 10 stages cleared at least once |
| `stage_select` | Use the stage-select feature once |
| `counter_special` | Fire a counter-special at full meter |

Some achievements in the JSON aren't wired yet (dodge_taxi, dodge_train, no_dodge_all, no_special_all, back_atk_3, launcher_juggle) — those need per-run tracking. Easy follow-up if you want them all live.

## Costs and limits

- One full `generate.py all` run: under $1 of API spend
- Each generator can be re-run independently
- Existing content files are backed up to `*.bak.json` before overwrite
- Generated JSON is committed to git so production deploys don't need the API key

## If something breaks

- **JSON parse errors**: the model sometimes wraps output in markdown fences. The script handles common cases. If it fails, look at the raw response (the script prints the first 500 chars of failed responses).
- **Rate limits**: if you hit a rate limit, wait a minute and re-run. Each command does ~10 sequential calls max.
- **API key missing**: script exits with a clear error message before any API spend.
