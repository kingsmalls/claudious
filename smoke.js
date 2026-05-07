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
              " hitbox.cx =", (hb && hb[0]) ? hb[0].cx.toFixed(1) : "none");
  snapshot("07_attack_left");

  // Toggle debug overlay and capture with hitbox visualizer
  press("F3");
  press("KeyJ");
  step(6);
  snapshot("08_debug_hitboxes");

  // ---- RUNNER combat ----
  // Walk into the runners and attack until the first dies.
  press("Escape");          // back to title
  step(2);
  press("Enter");           // re-enter playing (spawns 2 runners at 440,280 and 520,320)
  step(2);
  console.log("\nenemies spawned:", peek("enemies.length"));
  // Walk right until adjacent to the first runner, then stop.
  hold("KeyD");
  let walked = 0;
  while (walked < 300) {
    step(2); walked += 2;
    const e0 = peek("enemies[0]");
    const px = peek("player.x");
    if (!e0) break;
    // Stop just before passing the runner so we keep facing it.
    if (e0.x - px < 26 && e0.x - px > 0) break;
  }
  release("KeyD");
  step(2);
  console.log("approach end: player.x =", peek("player.x").toFixed(1),
              " player.hp =", peek("player.hp"),
              " e0.x =", peek("enemies[0].x").toFixed(1),
              " e0.hp =", peek("enemies[0].hp"),
              " facing =", peek("player.facing"));
  snapshot("09_runner_approach");

  // Throw a punch — should connect on an active frame.
  press("KeyJ");
  step(7);
  console.log("after first jab: e0.hp =", peek("enemies[0].hp"),
              " hitstop =", peek("hitstopFrames"),
              " particles =", peek("particles.length"));
  snapshot("10_first_hit");

  // Recover, then chase + jab until the runner dies. 26hp / 5dmg = 6 hits min.
  for (let i = 0; i < 30; i++) {
    step(20); // wait through recovery + iframes
    if (!peek("enemies[0]") || peek("enemies[0].dead")) break;
    const dx = peek("enemies[0].x") - peek("player.x");
    // Walk into range if knocked or runner stepped back.
    if (Math.abs(dx) > 24) {
      hold(dx > 0 ? "KeyD" : "KeyA");
      while (true) {
        step(2);
        if (!peek("enemies[0]") || peek("enemies[0].dead")) break;
        const cur = peek("enemies[0].x") - peek("player.x");
        if (Math.abs(cur) <= 22) break;
        if (Math.sign(cur) !== Math.sign(dx)) break; // overshot
      }
      release(dx > 0 ? "KeyD" : "KeyA");
    }
    press("KeyJ");
    step(10);
  }
  console.log("after combo: enemies =", peek("enemies.length"),
              " e0.hp =", peek("enemies[0] && enemies[0].hp"),
              " e0.dead =", peek("enemies[0] && enemies[0].dead"),
              " player.hp =", peek("player.hp"));
  snapshot("11_combo_finish");

  // Wait for cleanup (>1.4s after death), confirm dead enemy is removed.
  step(120);
  console.log("after cleanup: enemies =", peek("enemies.length"));

  console.log("\nERRORS:", errors.length);
  for (const e of errors) console.log("  -", e);
  process.exit(errors.length ? 1 : 0);
})();
