// Sprite-rendering smoke test for the_block.html.
//
// Boots the engine in jsdom against a local http server (so fetch + Image
// can load characters/<char>.png + characters/<char>_atlas.json), confirms
// each atlas attaches to SPRITES, hooks drawSpriteCharacter to count whether
// the renderer takes the sprite path or falls back to procedural for each
// character, and writes one shot_sprite_<char>.png per character.
//
// Run with:  node smoke_sprites.js
// (or: npm run smoke-sprites)
//
// Exits 0 on success, 1 if any character renders procedural-only after a
// short window, or if expected anims/frames are missing.

const fs = require("fs");
const path = require("path");
const http = require("http");
const fetch = require("node-fetch");
const { JSDOM, VirtualConsole } = require("jsdom");

const PORT = 8765;
const ROOT = __dirname;

// Tiny static server: serves files from project root. No external process
// to coordinate, no port-clobber surprises in CI.
function startServer() {
  const types = {
    ".html": "text/html", ".js":  "application/javascript",
    ".json": "application/json", ".png": "image/png",
    ".css":  "text/css", ".svg":  "image/svg+xml",
  };
  const srv = http.createServer((req, res) => {
    const u = decodeURIComponent(req.url.split("?")[0]);
    const f = path.join(ROOT, u === "/" ? "/index.html" : u);
    if (!f.startsWith(ROOT)) { res.writeHead(403); res.end(); return; }
    fs.readFile(f, (err, data) => {
      if (err) { res.writeHead(404); res.end(); return; }
      res.writeHead(200, { "Content-Type": types[path.extname(f)] || "application/octet-stream" });
      res.end(data);
    });
  });
  return new Promise(r => srv.listen(PORT, "127.0.0.1", () => r(srv)));
}

(async () => {
  const server = await startServer();
  let raf = [];
  const vc = new VirtualConsole();
  const errors = [];
  vc.on("jsdomError", e => errors.push("jsdom: " + (e.message || e)));

  const dom = await JSDOM.fromURL(`http://127.0.0.1:${PORT}/the_block.html`, {
    runScripts: "dangerously",
    pretendToBeVisual: true,
    resources: "usable",
    virtualConsole: vc,
    beforeParse(window) {
      let t = 0;
      window.performance = { now: () => t };
      window.requestAnimationFrame = (cb) => { raf.push(cb); return raf.length; };
      window.cancelAnimationFrame = () => {};
      window.__advance = (ms) => { t += ms; const c = raf; raf = []; for (const cb of c) cb(t); };
      // jsdom doesn't ship fetch — polyfill so the engine's atlas loader works.
      window.fetch = (url, ...rest) => {
        const abs = url.startsWith("http") ? url : `http://127.0.0.1:${PORT}/${url}`;
        return fetch(abs, ...rest);
      };
    },
  });
  const { window } = dom;

  // Wait up to 3s for atlases to attach.
  for (let i = 0; i < 30; i++) {
    await new Promise(r => setTimeout(r, 100));
    if (window.eval("SPRITES.rio && SPRITES.duke && SPRITES.atlas")) break;
  }

  let failed = false;
  const checkAtlas = (key, expectedAnims) => {
    const s = window.eval(`SPRITES['${key}']`);
    if (!s) {
      console.log(`${key}: NOT LOADED`);
      failed = true; return;
    }
    const fc = Object.keys(s.atlas.frames).length;
    const ac = Object.keys(s.atlas.anims).length;
    console.log(`${key.padEnd(6)}: ${s.img.naturalWidth}x${s.img.naturalHeight}, ${fc} frames, ${ac} anims`);
    if (ac < expectedAnims) {
      console.log(`  WARN: expected at least ${expectedAnims} anims, got ${ac}`);
      failed = true;
    }
  };
  checkAtlas("rio",   15);
  checkAtlas("duke",  15);
  checkAtlas("atlas", 15);

  // Hook drawSpriteCharacter to confirm the renderer takes the sprite path.
  window.eval(`
    window.__spriteUsed = 0; window.__procFallback = 0;
    const _orig = drawSpriteCharacter;
    drawSpriteCharacter = function(p) {
      const r = _orig(p);
      if (p === player) (r ? window.__spriteUsed++ : window.__procFallback++);
      return r;
    };
    save.unlocks.atlas = true;
  `);

  function dispatchKey(type, code) {
    const e = new window.KeyboardEvent(type, { code, key: code, bubbles: true });
    Object.defineProperty(e, "code", { value: code });
    window.dispatchEvent(e);
  }
  function press(c) { dispatchKey("keydown", c); dispatchKey("keyup", c); }
  function step(n) { for (let i = 0; i < n; i++) window.__advance(17); }

  async function capture(charKey) {
    window.eval(`selectedChar = '${charKey}';`);
    if (window.eval("STATE") !== "title") { press("Escape"); step(4); }
    press("Enter"); step(2);  // title -> select
    press("Enter"); step(2);  // select -> playing
    window.eval("__spriteUsed = 0; __procFallback = 0;");
    step(20);
    const su = window.eval("__spriteUsed");
    const pf = window.eval("__procFallback");
    const live = window.eval("player.char");
    console.log(`${charKey.padEnd(6)} render: sprite=${su} procedural=${pf}  (player.char=${live})`);
    if (su === 0) failed = true;
    const canvas = window.document.getElementById("c");
    const buf = Buffer.from(canvas.toDataURL("image/png").split(",")[1], "base64");
    fs.writeFileSync(path.join(ROOT, `shot_sprite_${charKey}.png`), buf);
  }

  await capture("rio");
  await capture("duke");
  await capture("atlas");

  console.log("\nERRORS:", errors.length);
  for (const e of errors.slice(0, 5)) console.log(" -", e);

  server.close();
  process.exit(failed ? 1 : 0);
})();
