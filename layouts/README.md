# Sprite sheet layout configs

Each `*_layout.json` here is a per-anim layout config consumed by:

```bash
python3 pipeline.py build-atlas layouts/rio_layout.json --output rio_atlas.json
```

## Schema

```json
{
  "sheet":       "rio.png",
  "cell_width":  64,
  "cell_height": 96,
  "fps":         8,
  "anchor":      { "x": 0.5, "y": 1.0 },
  "anims": {
    "idle":     { "row": 0, "col": 0,  "count": 4 },
    "walk":     { "row": 0, "col": 4,  "count": 6 },
    "run":      { "row": 0, "col": 10, "count": 6 },
    "jump":     { "row": 1, "col": 0,  "count": 3 },
    "atk1":     { "row": 1, "col": 3,  "count": 4 },
    "atk2":     { "row": 1, "col": 7,  "count": 5 },
    "atk3":     { "row": 1, "col": 12, "count": 6 },
    "heavy":    { "row": 2, "col": 0,  "count": 7 },
    "jump_atk": { "row": 2, "col": 7,  "count": 4 },
    "back_atk": { "row": 2, "col": 11, "count": 4 },
    "special":  { "row": 3, "col": 0,  "count": 12 },
    "throw":    { "row": 3, "col": 12, "count": 5 },
    "counter":  { "row": 4, "col": 0,  "count": 6 },
    "hurt":     { "row": 4, "col": 6,  "count": 3 },
    "dodge":    { "row": 4, "col": 9,  "count": 5 }
  }
}
```

## Workflow

1. Save your sprite sheet PNG at the project root (e.g. `rio.png`).
2. Copy the schema above into `layouts/<char>_layout.json`.
3. Adjust `cell_width`, `cell_height`, and each anim's `row`, `col`, `count`
   to match the actual layout on the sheet.
4. Run:
   ```bash
   python3 pipeline.py build-atlas layouts/rio_layout.json --output rio_atlas.json
   python3 pipeline.py validate-atlas rio_atlas.json
   ```
5. Reload `the_block.html`. The engine auto-loads `<char>.png` + `<char>_atlas.json`
   pairs at boot and prefers sprite rendering over the procedural fallback for
   that character.

## Frame counts (per character, total 80)

| Slot       | Count |
|------------|------:|
| idle       | 4     |
| walk       | 6     |
| run        | 6     |
| jump       | 3     |
| atk1       | 4     |
| atk2       | 5     |
| atk3       | 6     |
| heavy      | 7     |
| jump_atk   | 4     |
| back_atk   | 4     |
| special    | 12    |
| throw      | 5     |
| counter    | 6     |
| hurt       | 3     |
| dodge      | 5     |

These are the counts specified in `characters/<NAME>.md`. If your generated
sheet has different counts (e.g. fewer idle frames), adjust the `count`
fields here — the engine works with whatever frame counts you provide.

## Notes

- `row` and `col` are zero-indexed cell positions on the sheet grid.
- Frames named `<anim>_0`, `<anim>_1`, … are auto-generated.
- Anims overflowing a row will wrap to the next row, but it's clearer to
  keep each anim on a single row.
- Any anim slot you omit falls back to procedural rendering for that one
  animation — partial atlases are fine.
