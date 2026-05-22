#!/usr/bin/env python3
"""
THE BLOCK — content generation tool.

Uses the Anthropic API to mass-produce game content that gets baked into
static JSON files in `content/`. Run locally with your API key set in the
environment; the resulting JSON files are committed to the repo and loaded
by the game at runtime. No API calls happen during gameplay.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    pip install anthropic

    python generate.py npc_chatter        # bark lines per stage
    python generate.py enemy_variants     # named sub-types per enemy
    python generate.py boss_dialog        # dialog pool per boss per beat
    python generate.py achievements       # 30+ achievements with copy
    python generate.py all                # all four

Each command writes to content/<name>.json. Existing files are backed up
to content/<name>.bak.json before overwrite so iterations are safe.

Model defaults to claude-sonnet-4-6 (latest Sonnet 4.x as of this writing).
Cost estimate per full run: under $1 total.
"""

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
CONTENT.mkdir(exist_ok=True)

MODEL = "claude-sonnet-4-6"   # latest Sonnet 4.x
MAX_TOK = 4096

# ---------- Context loaders ----------
# We feed Claude the existing canon docs so generated content matches the
# game's tone (gentrification, social-realist, Kane never raises his voice).

def load(path):
    p = ROOT / path
    return p.read_text() if p.exists() else ""

CONTEXT_STORY  = load("STORY.md")
CONTEXT_BIBLE  = load("CHARACTER_BIBLE.md")
CONTEXT_RIO    = load("characters/RIO.md")
CONTEXT_DUKE   = load("characters/DUKE.md")
CONTEXT_ATLAS  = load("characters/ATLAS.md")
CONTEXT_KANE   = load("characters/KANE.md")
CONTEXT_BARON  = load("characters/BARON.md")
CONTEXT_RAZOR  = load("characters/RAZOR.md")
CONTEXT_VOLT   = load("characters/VOLT.md")
CONTEXT_BLACKWELL = load("characters/BLACKWELL.md")
CONTEXT_RUNNER = load("characters/RUNNER.md")
CONTEXT_TANK   = load("characters/TANK.md")
CONTEXT_SLICE  = load("characters/SLICE.md")
CONTEXT_CHAINS = load("characters/CHAINS.md")
CONTEXT_LAMPLIGHT = load("characters/LAMPLIGHT.md")
CONTEXT_SHADE  = load("characters/SHADE.md")
CONTEXT_DOJO   = load("characters/DOJO.md")
CONTEXT_RIG    = load("characters/RIG.md")

# Hard tone reminder we paste into every prompt so the model doesn't drift
# into generic action-game writing.
TONE = """\
TONE RULES (apply to every line you generate):
- No revenge fantasy. The protagonists fight because the alternative is losing the place that made them.
- Kane never raises his voice. Politeness is the menace.
- Hits hurt. No glamour around violence.
- The Block is the protagonist. Lines should land specific to neighborhood life — names of corners, businesses, people.
- Voice differs per character: Rio = calm/deadpan, Duke = tired/cynical/half-finished, Atlas = father energy/slow to anger.
- Short. Beat-em-ups don't have time for paragraphs. 4-10 words per bark unless the format calls for more.
- No emojis. No hashtags. No exclamation points unless the moment really earns one.
"""

# ---------- Anthropic client ----------
def get_client():
    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: anthropic SDK not installed. Run:  pip install anthropic", file=sys.stderr)
        sys.exit(1)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY env var not set.", file=sys.stderr)
        sys.exit(1)
    return Anthropic()

def call(client, system, user):
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOK,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return resp.content[0].text

def parse_json_from_response(text):
    """Models sometimes wrap JSON in code fences or prose. Extract the JSON block."""
    # Strip code fences.
    if "```" in text:
        # Take everything between the first ``` and the next ```
        chunks = text.split("```")
        for c in chunks:
            c = c.strip()
            if c.startswith("json"): c = c[4:].strip()
            if c.startswith("{") or c.startswith("["):
                try:
                    return json.loads(c)
                except Exception:
                    pass
    # Try the raw text.
    try:
        return json.loads(text.strip())
    except Exception:
        pass
    # Find the first { or [ and the matching last } or ].
    for open_ch, close_ch in [("[", "]"), ("{", "}")]:
        i = text.find(open_ch)
        j = text.rfind(close_ch)
        if i >= 0 and j > i:
            try:
                return json.loads(text[i:j+1])
            except Exception:
                pass
    raise ValueError("Could not parse JSON from response:\n" + text[:500])

def save(name, data):
    """Backup existing file, then write new content."""
    out = CONTENT / f"{name}.json"
    if out.exists():
        bak = CONTENT / f"{name}.bak.json"
        bak.write_text(out.read_text())
    out.write_text(json.dumps(data, indent=2))
    print(f"[generate] wrote {out}")

# ---------- 1. NPC chatter ----------
STAGES = [
    ("THE BLOCK",     "The protagonist's home neighborhood. Marcus's gym just got padlocked. People still on the street."),
    ("THE TUNNELS",   "Subway platform / storm drain. Train rumbles every minute. Echoey concrete. Few witnesses."),
    ("RIVER ROW",     "Industrial dock district. Old warehouses, shipping containers, foghorns in the distance."),
    ("LANTERN ROW",   "Market street, paper lanterns hanging across the alleys. Some vendors still open."),
    ("THE CAGE",      "Underground fight club Kane is using as a holding pen. Crowd watching, phones up."),
    ("UPTOWN",        "Glass-and-steel financial district. Doormen, security guards, expensive coffee shops."),
    ("THE WORKS",     "Foundry being converted to lofts. Workers Kane kept on payroll. Smell of molten metal."),
    ("THE FREEWAY",   "Overpass at night. Encampment Kane's crew is clearing out. Cars blasting overhead."),
    ("THE TOWER",     "Upper floor of Kane Properties. Wind through a broken window. Documents flying."),
    ("THE TOP",       "Penthouse. Kane's office. Skyline view. Calm. The fight is symbolic."),
]

def gen_npc_chatter():
    client = get_client()
    out = {}
    for name, vibe in STAGES:
        print(f"  generating NPC chatter for {name}...")
        user = f"""\
Generate 12 short NPC bark lines for the {name} stage of THE BLOCK.
Setting: {vibe}

These lines shout from offscreen during fights — neighbors at windows, vendors at stalls, people running past, witnesses watching. They land between hits, not during cutscenes.

Output as a JSON array of strings. Each line:
- 4-10 words
- Specific to this stage's setting (mention specific things you'd see/hear there)
- Mix tones: some encouraging, some bystanding, some scared, some bitter at Kane
- Some name people: "Marcus", "Atlas", "the gym", "Foster Hardware", "Kane Properties"
- No exclamation points unless the line really earns one
- No emojis

Example for THE BLOCK: ["Get him for Marcus.", "Cops aren't coming.", "Tell Kane to choke on it."]

Return ONLY the JSON array, no preamble."""
        text = call(client, TONE, user)
        lines = parse_json_from_response(text)
        out[name] = lines
    save("npc_chatter", out)

# ---------- 2. Enemy variants ----------
ENEMY_TYPES = [
    ("runner",    CONTEXT_RUNNER),
    ("tank",      CONTEXT_TANK),
    ("slice",     CONTEXT_SLICE),
    ("chains",    CONTEXT_CHAINS),
    ("lamplight", CONTEXT_LAMPLIGHT),
    ("shade",     CONTEXT_SHADE),
    ("dojo",      CONTEXT_DOJO),
    ("rig",       CONTEXT_RIG),
]

def gen_enemy_variants():
    client = get_client()
    out = {}
    for key, spec in ENEMY_TYPES:
        print(f"  generating variants for {key}...")
        user = f"""\
Here's the spec for the {key.upper()} enemy in THE BLOCK:

{spec[:4000]}

Generate 4 named VARIANTS of this enemy — sub-types Kane might field with slight differences.

Each variant has:
- "name": Short caps tag, ~2-3 words, fits the neighborhood feel
- "subtitle": 6-12 words, one-line vibe
- "hp_mul": 0.7-1.4 multiplier on the base HP (less for nimbler, more for tougher)
- "speed_mul": 0.7-1.4 multiplier on walk/run speed
- "damage_mul": 0.8-1.3 multiplier on damage dealt
- "dialog_grunt": one short line they say when first hit (3-6 words)
- "dialog_kod": one short line they say going down (3-6 words)
- "backstory": one sentence — who this person was before Kane's crew

Output as a JSON array of 4 objects. Return ONLY the JSON array, no preamble."""
        text = call(client, TONE, user)
        variants = parse_json_from_response(text)
        out[key] = variants
    save("enemy_variants", out)

# ---------- 3. Boss dialog expansion ----------
BOSSES = [
    ("baron",     CONTEXT_BARON),
    ("razor",     CONTEXT_RAZOR),
    ("volt",      CONTEXT_VOLT),
    ("blackwell", CONTEXT_BLACKWELL),
    ("kane",      CONTEXT_KANE),
]

def gen_boss_dialog():
    client = get_client()
    out = {}
    for key, spec in BOSSES:
        print(f"  generating dialog pool for {key.upper()}...")
        user = f"""\
Here's the spec for {key.upper()}, a boss in THE BLOCK:

{spec[:5000]}

Generate dialog variants this boss says in 4 beats:
- "intro" — said when first encountered (cutscene before the fight). 3 lines.
- "midfight" — said mid-fight after taking ~50%% damage. 8 short lines (~4-8 words each).
- "taunt" — said when they land a hit. 6 short lines (~3-6 words each).
- "defeat" — said going down. 3 lines.

Stay in character per the spec. Boss should never break character.

Output as a JSON object: {{"intro": [...], "midfight": [...], "taunt": [...], "defeat": [...]}}.

For KANE specifically: he never throws a punch. His "midfight" and "taunt" are spoken from the desk during the QTE — soft offers escalating into quiet threats. His "defeat" is the moment he says "...I see."

Return ONLY the JSON object, no preamble."""
        text = call(client, TONE, user)
        beats = parse_json_from_response(text)
        out[key] = beats
    save("boss_dialog", out)

# ---------- 4. Achievements ----------
def gen_achievements():
    client = get_client()
    user = f"""\
Generate 30 achievements for THE BLOCK — a browser beat-em-up where Rio, Duke, or Atlas defend their neighborhood from a developer named Kane.

Story context:
{CONTEXT_STORY[:6000]}

Each achievement:
- "id": snake_case short identifier (e.g. "first_blood", "no_damage_block")
- "name": short title in ALL CAPS, 2-5 words
- "description": 1-line description matching the game's tone, ~10-15 words
- "trigger": brief technical hint of when it fires (e.g., "kill 10 enemies in one combo", "clear stage 1 with full HP")
- "rarity": one of "common" (5pts), "uncommon" (10pts), "rare" (25pts), "legendary" (50pts)

Cover a mix of:
- Story milestones (first stage clear, beat each boss, refuse Kane, ending)
- Skill challenges (long combos, perfect parry the haymaker, no-damage clears, no-special clears)
- Hidden / discovery (find BLACKWELL on brutal, talk to Atlas first, etc.)
- Character-specific (clear with each protagonist, max HP through KANE)
- Cumulative (100 enemies KO'd, all stages cleared, 20 perfect parries)
- Tone-driven (refuse all 5 KANE prompts, dodge the taxi 5 times, parry baron's haymaker)

Mix rarities: ~12 common, ~10 uncommon, ~6 rare, ~2 legendary.

Output as a JSON array of 30 objects. Return ONLY the JSON array, no preamble."""
    client = get_client()
    print("  generating achievements (this is the biggest request)...")
    text = call(client, TONE, user)
    achievements = parse_json_from_response(text)
    save("achievements", achievements)

# ---------- entry point ----------
GENERATORS = {
    "npc_chatter":     gen_npc_chatter,
    "enemy_variants":  gen_enemy_variants,
    "boss_dialog":     gen_boss_dialog,
    "achievements":    gen_achievements,
}

def main():
    p = argparse.ArgumentParser(description="THE BLOCK content generator")
    p.add_argument("cmd", choices=list(GENERATORS.keys()) + ["all"],
                   help="which content to generate")
    args = p.parse_args()
    if args.cmd == "all":
        for name, fn in GENERATORS.items():
            print(f"\n=== {name} ===")
            fn()
    else:
        GENERATORS[args.cmd]()

if __name__ == "__main__":
    main()
