// Headless smoke test for the_block.html
// - Loads the HTML in jsdom with canvas support
// - Drives Enter (title -> playing), then J (attack), capturing frames
// - Saves PNGs of the canvas at key moments

const fs = require("fs");
const path = require("path");
const { JSDOM, VirtualConsole } = require("jsdom");

const html = fs.readFileSync(path.join(__dirname, "the_block.html"), "utf8");

const errors = [];
const vc = new VirtualConsole();
vc.on("jsdomError", e => errors.push("jsdomError: " + (e.stack || e.message)));
vc.on("error",      e => errors.push("error: " + e));
vc.on("warn",       (...a) => console.warn("[warn]", ...a));
vc.on("log",        (...a) => console.log("[log]", ...a));

// Mock requestAnimationFrame so we can step deterministically.
let raf_cbs = [];
const dom = new JSDOM(html, {
  runScripts: "dangerously",
  pretendToBeVisual: true,
  resources: "usable",
  virtualConsole: vc,
  beforeParse(window) {
    let t = 0;
    window.performance = { now: () => t };
    window.requestAnimationFrame = (cb) => { raf_cbs.push(cb); return raf_cbs.length; };
    window.cancelAnimationFrame = () => {};
    window.__advance = (ms) => {
      t += ms;
      const cbs = raf_cbs; raf_cbs = [];
      for (const cb of cbs) {
        try { cb(t); } catch (e) { errors.push("raf: " + (e.stack || e)); }
      }
    };
  },
});

const { window } = dom;
const document = window.document;

function dispatchKey(type, code, key) {
  const e = new window.KeyboardEvent(type, { code, key, bubbles: true });
  // jsdom sometimes clears .code if not set explicitly via defineProperty
  Object.defineProperty(e, "code", { value: code });
  window.dispatchEvent(e);
}
function press(code, key) {
  dispatchKey("keydown", code, key || code);
  dispatchKey("keyup",   code, key || code);
}
function hold(code, key) { dispatchKey("keydown", code, key || code); }
function release(code, key) { dispatchKey("keyup", code, key || code); }

function step(frames) {
  // Use 17ms (slightly above 1/60s) so the accumulator reliably ticks on every advance.
  for (let i = 0; i < frames; i++) window.__advance(17);
}

function snapshot(name) {
  const c = document.getElementById("c");
  const url = c.toDataURL("image/png");
  const b64 = url.split(",", 2)[1];
  const buf = Buffer.from(b64, "base64");
  fs.writeFileSync(path.join(__dirname, "shot_" + name + ".png"), buf);
  console.log("wrote shot_" + name + ".png  (", buf.length, "bytes )");
}

function peek(expr) {
  try { return window.eval(expr); }
  catch (e) {
    errors.push("peek(" + JSON.stringify(expr) + "): " + e.message);
    return undefined;
  }
}

(async () => {
  // Let the inline <script> attach handlers and queue the first RAF.
  await new Promise(r => setTimeout(r, 50));

  step(2);  // boot frames
  console.log("STATE after boot:", peek("STATE"));
  snapshot("01_title");

  press("Enter");
  step(2);
  console.log("STATE after Enter:", peek("STATE"), "player:", !!peek("player"));
  snapshot("02_playing_idle");

  // Walk right for ~30 frames
  hold("KeyD");
  step(30);
  release("KeyD");
  console.log("after walk: player.x =", peek("player") && peek("player").x.toFixed(1),
              " state:", peek("player") && peek("player").animState);
  snapshot("03_after_walk");

  // Throw a punch
  press("KeyJ");
  step(4); // mid-startup / active
  console.log("during atk1: frame =", peek("player").attackFrame,
              " hitboxes:", peek("player").hitboxes.length);
  snapshot("04_attack_active");

  step(20); // recover
  console.log("after atk recovery: attacking =", peek("player").attacking);

  // Jump
  press("Space");
  step(8);
  console.log("mid-jump z =", peek("player").z.toFixed(1),
              " vz =", peek("player").vz.toFixed(1));
  snapshot("05_jumping");

  // Run via double-tap right
  press("KeyD");
  press("KeyD");
  hold("KeyD");
  step(20);
  release("KeyD");
  console.log("after double-tap run: animState =", peek("player").animState,
              " running =", peek("player").running, " x =", peek("player").x.toFixed(1));
  snapshot("06_run");

  // Land before testing the left-facing attack.
  step(25);
  console.log("after land: z =", peek("player.z").toFixed(1),
              " animState =", peek("player.animState"));
  hold("KeyA");
  step(10);
  release("KeyA");
  console.log("pre-left-atk: facing =", peek("player.facing"),
              " z =", peek("player.z").toFixed(1));
  press("KeyJ");
  step(6);
  const hb = peek("player.hitboxes");
  console.log("left-facing atk: facing =", peek("player.facing"),
              " attackFrame =", peek("player.attackFrame"),
              " hitboxes =", hb && hb.length,
              " hitbox.x =", (hb && hb[0]) ? hb[0].x.toFixed(1) : "none");
  snapshot("07_attack_left");

  // Toggle debug overlay and capture with hitbox visualizer
  press("F3");
  press("KeyJ");
  step(6);
  snapshot("08_debug_hitboxes");

  console.log("\nERRORS:", errors.length);
  for (const e of errors) console.log("  -", e);
  process.exit(errors.length ? 1 : 0);
})();
