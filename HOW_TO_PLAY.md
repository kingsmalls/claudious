# How to play THE BLOCK on your home computer

The game runs in your browser, but it needs a **local web server** running on your computer (the sprite atlas loader uses `fetch()`, which browsers refuse to do from `file://`). Don't worry — that's one command.

Pick the path that matches what you already have installed. **Mac** users almost always have Python; **Windows** users may need a one-click Python install.

---

## Path A — Node.js (recommended, one command)

If you have **Node.js** installed (or are okay installing it once — it's free, from nodejs.org):

1. **Get the code** — either:
   - Download ZIP: visit your repo on github.com → green **Code** button → **Download ZIP** → extract somewhere (e.g. `~/Documents/the-block`)
   - OR clone with GitHub Desktop (desktop.github.com): File → Clone repository → pick your repo → choose folder
2. **Open a terminal in that folder**:
   - **Mac**: Right-click the folder in Finder → "New Terminal at Folder"
   - **Windows**: Open the folder, click in the address bar, type `cmd` and press Enter
3. Run:
   ```bash
   npm install
   npm run play
   ```
4. Your browser opens to `http://localhost:8765/the_block.html`. Press Ctrl+C in the terminal to stop the server when done.

`npm install` only needs to happen once. From then on it's just `npm run play`.

---

## Path B — Python (no Node.js needed)

If you have **Python** installed:

1. Get the code (same as Path A step 1)
2. Open a terminal in the project folder (same as Path A step 2)
3. Run:
   ```bash
   python3 -m http.server 8765
   ```
   (On Windows, sometimes that's just `python` instead of `python3`.)
4. Open your browser to `http://localhost:8765/the_block.html`
5. Press Ctrl+C in the terminal to stop the server when done.

---

## Don't have either?

- **Mac**: You already have Python. Just use Path B.
- **Windows**: Easiest option is to install Python from the Microsoft Store — search "Python" → click Install → ~30 seconds. Or install Node.js from nodejs.org.

---

## Controls

| Action | Keyboard | Notes |
|---|---|---|
| Move | WASD or arrow keys | hold to walk |
| Run | Double-tap a direction | |
| Jump | Space | |
| Dodge | Down + Space | invincible briefly |
| Light attack | **J** | chain J → J → J for a combo |
| Heavy / launcher | **K** | crouches then rises |
| Special | **L** | costs HP — Sunset Spin / Rolling Thunder / Foundation Stone |
| Grab | **U** | grab an enemy → throw with J |
| Parry | **I** | tap right before a hit lands |
| Pause | **P** or Escape | also adjust audio + difficulty here |
| Debug overlay | **F3** | shows hitboxes |
| Skip cutscene | Enter / Space / J / Escape | works for opening, boss intros, stage beats, ending |

Gamepad also works — Xbox / PlayStation controllers are auto-detected.

---

## What you should see when you start

1. **Title screen** — press Enter
2. **Character select** — pick Rio / Duke / Atlas with arrows, Enter to confirm
3. **Opening cutscene** — your character's voiceover at the locked gym (skip with Enter)
4. **Stage 1 — THE BLOCK** starts
5. After each stage clear, a one-line narrative beat plays
6. Boss stages (3 / 6 / 9) get a full intro cutscene
7. Stage 10 is the Kane QTE — press the J / K prompts in time to refuse each of his offers
8. Ending cinematic plays, then victory screen

---

## Troubleshooting

- **"npm: command not found"** — Node.js isn't installed yet. Either install it from nodejs.org, or use Path B (Python) instead.
- **"python3: command not found" on Windows** — try `python` instead of `python3`.
- **Browser shows code instead of the game** — you opened the `.html` file directly. You need to run the server first and open `http://localhost:8765/the_block.html`.
- **Black screen / no sprites** — open the browser's developer console (F12) and look for red errors. Most likely either the server isn't running or you're on the wrong URL.
- **No music** — click anywhere in the game first; browsers require user interaction before audio starts (autoplay policy).
- **Tests** — `npm run smoke` runs the game-flow regression. `npm run smoke-sprites` confirms sprite atlases load and render. Both should print `ERRORS: 0` (or `ERRORS: 1` mentioning localStorage — that one's expected in jsdom).
