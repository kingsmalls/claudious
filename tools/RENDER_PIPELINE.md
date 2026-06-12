# Rendering Studio-Quality Sprites from Unity → The Block

You picked Path B: render the KayKit 3D rigged characters out to 2D sprite sheets
the engine already knows how to draw. Plus Cyberpunk City as a parallax backdrop.
This file is the operating manual.

## What you need installed

In a Unity project (any 2022 LTS or 6.x version):
- **KayKit — Adventurers Character Pack** (7 rigged characters + 104 anims/char)
- **Kevin Iglesias — Human Melee Animations** (extra punch/kick/strafe/jump anims)
- **Cyberpunk City** (for the backdrop)
- *(optional)* **Low-Poly Medieval Fantasy Heroes** for variety on bosses/enemies

In this repo:
- `tools/SpriteSheetRenderer.cs` — the Unity Editor script that does the rendering
- `auto_atlas.py` is no longer used for these characters (we ship rendered atlases directly)
- The engine in `the_block.html` consumes the rendered atlases unchanged

## Phase 1 — Render a single character end-to-end (sanity check)

Goal: prove the pipeline works on ONE character before scaling up.

1. **Set up Unity scene** (one-time):
   - Create a new empty scene
   - Drag a KayKit character prefab (e.g. `Adventurer_Knight`) into the scene at world (0, 0, 0)
   - Rotate the character so it faces **+X (camera-right)**
   - Add a directional light from above-front
   - Create an **Orthographic Camera**:
     - Position: `(0, 1, -5)`
     - Rotation: `(0, 0, 0)`
     - Projection: Orthographic
     - Size: `1.2`
     - Clear Flags: **Solid Color**
     - Background: **(0, 0, 0, 0)** — fully transparent
   - Save the scene as `Assets/Scenes/RenderRig.unity`

2. **Install the renderer**:
   - Copy `tools/SpriteSheetRenderer.cs` from this repo into `Assets/Editor/`
     in your Unity project (create the Editor folder if it doesn't exist)
   - Unity recompiles automatically

3. **Render**:
   - Open `Window → The Block → Render Sprite Sheet`
   - Drag the character GameObject into **Character**
   - Drag the camera into **Render Camera**
   - Output name: `rio` (or whichever role you're testing)
   - Frame size: `256` (good default; raise to 384 for higher quality)
   - Frames per anim: `8` (matches the slicer's expectations)
   - Engine display height: `96` (matches existing players)
   - Click **Render All Animations**

4. **Wire into the game**:
   - In Unity's project window, find `Assets/RenderedSprites/rio.png` and
     `Assets/RenderedSprites/rio_atlas.json`
   - Copy both files into `characters/` in this repo (overwrite the existing
     ones — back them up first if you want to keep the Gemini versions)
   - Reload `the_block.html`. The engine pulls the new atlas automatically
     thanks to the cache-buster

If Rio shows up animated and full-body, the pipeline works. Move on.

## Phase 2 — Map all 15 game characters to KayKit characters

KayKit Adventurers has 7 chars; we need to cover 15 game roles. The reasonable
mapping is below — adjust to taste based on what visually fits.

| Game role | KayKit character | Notes |
|---|---|---|
| **Rio** (player, agile) | Rogue or Ranger | quick, light |
| **Duke** (player, brawler) | Adventurer / Fighter | balanced |
| **Atlas** (player, heavy) | Large Barbarian | wide silhouette |
| **Baron** (boss, brick villain) | Knight (large rig) | imposing |
| **Razor** (boss, dual knives) | Rogue with twin blades | dual-wield |
| **Volt** (boss, ranged) | Mage | "cyber" reskin via texture tint |
| **Blackwell** (boss, wrestler) | Barbarian | grapple animations |
| **Runner** (enemy) | Adventurer (light) | basic |
| **Chains** (enemy) | Barbarian palette swap | weapon = chain |
| **Slice** (enemy) | Rogue palette swap | quick |
| **Tank** (enemy) | Knight palette swap | armored |
| **Lamplight** (enemy, ranged) | Ranger | uses bow → reskin to pistol if you can |
| **Dojo** (enemy, martial) | Adventurer (unarmed punches/kicks) | use Kevin Iglesias kicks |
| **Shade** (enemy, stealth) | Rogue with dark texture | sneak/dash anims |
| **Rig** (enemy, brute) | Barbarian palette swap | bare-fist swing |

For each role:
1. Place that KayKit prefab in `RenderRig.unity`
2. Open the renderer, set Output name = the role (rio / duke / etc.)
3. Click Render
4. Copy the two output files into `characters/`

Per-character takes ~30 seconds. All 15: about 10 minutes of clicking.

## Phase 3 — Cyberpunk City backdrop

Replace the procedural city skyline in `the_block.html` with rendered art.

1. Open the Cyberpunk City demo scene in Unity
2. Frame the camera on a street-level slice (sideways, ~16:9, no character)
3. Save the camera view as a PNG (use the same `EditorWindow` pattern, or
   just Game-view → screenshot → save as PNG)
4. We want THREE parallax layers:
   - `bg_far.png`  — distant skyline + neon glow (slowest scroll)
   - `bg_mid.png`  — mid-distance buildings + signage
   - `bg_near.png` — near street, lamp posts (fastest scroll)
5. Drop all three into `characters/backdrops/` and ping me — I'll wire the
   parallax into the stage renderer (replace the procedural draws in
   `drawSky` / `drawSidewalk`).

## Phase 4 — Polish & per-character tuning

After Phases 1–3, expect:
- Animations smooth (8 fps × clip length, rendered from real motion capture)
- All 15 characters consistent in pose and proportion
- City backdrop scrolling behind action

Tunable per character via the atlas's `target_h` field:
- Rio / Duke / players: `96`
- Atlas / Blackwell / Baron (big): `112`
- Runner / Slice (small): `80`

And per-anim FPS via the atlas's `fps` field (default 10 in the renderer;
raise to 12 for snappier attacks).

## What NOT to do

- Don't use the existing Gemini atlases as fallbacks — delete them when
  you ship the Unity-rendered version, or the chroma-key pre-pass in
  `auto_atlas.py` will corrupt the transparency on re-runs. Once Unity is
  the source of truth, stop running `auto_atlas.py`.

- Don't change the engine's `loadAtlasFor` paths — keep the rendered output
  named `<character>.png` and `<character>_atlas.json` in `characters/`. The
  engine and cache-buster already know that layout.
