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

  // ---- COMBO CHAIN: J → J → J (atk1 → atk2 → atk3) ----
  press("Escape");  step(2);
  press("Enter");   step(2);
  // Walk in to range.
  hold("KeyD");
  while (true) {
    step(2);
    const e0 = peek("enemies[0]");
    if (!e0) break;
    if (e0.x - peek("player.x") < 24 && e0.x - peek("player.x") > 0) break;
  }
  release("KeyD");
  step(2);
  const startHp = peek("enemies[0].hp");
  press("KeyJ"); step(6);  // atk1 active hits at frame 5
  console.log("after J #1: e0.hp =", peek("enemies[0].hp"),
              " p.attackName =", peek("player.attackName"),
              " p.attackFrame =", peek("player.attackFrame"));
  press("KeyJ"); step(8);  // chain into atk2
  console.log("after J #2: e0.hp =", peek("enemies[0].hp"),
              " p.attackName =", peek("player.attackName"),
              " p.attackFrame =", peek("player.attackFrame"));
  press("KeyJ"); step(10); // chain into atk3
  console.log("after J #3: e0.hp =", peek("enemies[0].hp"),
              " p.attackName =", peek("player.attackName"),
              " p.comboHits =", peek("player.comboHits"));
  snapshot("12_combo_chain");
  console.log("combo dealt:", startHp - peek("enemies[0] && enemies[0].hp || 0"), "dmg total");

  // ---- DODGE: clean test, no enemies in range ----
  press("Escape"); step(2);
  press("Enter");  step(2);
  // Walk off to the left so runners are off-screen-far when we test dodge.
  hold("KeyA"); step(40); release("KeyA"); step(2);
  hold("ArrowDown");
  press("Space");
  step(2);
  console.log("dodge fired: dodging =", peek("player.dodging"),
              " iframes =", peek("player.iframes"),
              " vx =", peek("player.vx").toFixed(1));
  snapshot("14_dodge");
  step(20);
  console.log("post-dodge: dodging =", peek("player.dodging"));
  release("ArrowDown");

  // ---- JUMP ATTACK: clean test ----
  step(10);
  press("Space"); step(2);
  console.log("jumped: z =", peek("player.z").toFixed(1));
  press("KeyJ"); step(3);
  console.log("jump_atk: attackName =", peek("player.attackName"),
              " hitboxes:", peek("player.hitboxes.length"));
  snapshot("15_jump_atk");

  // ---- HEAVY whiff: confirm K starts the heavy attack from idle ----
  press("Escape"); step(2);
  press("Enter");  step(2);
  press("KeyK"); step(15);
  console.log("heavy whiff:",
              "atkName=", peek("player.attackName"),
              "atkFrame=", peek("player.attackFrame"));
  snapshot("13_launcher");

  // ---- LAUNCHER: position runner adjacent and disable its AI swipe ----
  press("Escape"); step(2);
  press("Enter");  step(2);
  // Mutate state directly: place runner [0] in range, raise its cooldown so it
  // won't swipe Rio mid-startup, and clear runner [1] so it doesn't interfere.
  window.eval(
    "enemies[0].x = player.x + 22;" +
    "enemies[0].y = player.y;" +
    "enemies[0].aiCooldown = 5;" +
    "enemies[1].hp = 0;" +
    "enemies[1].dead = true;" +
    "enemies[1].deathTimer = 100;"
  );
  step(2);
  press("KeyK");
  step(35);
  console.log("launcher hit:",
              "e0.hp=", peek("enemies[0] && enemies[0].hp"),
              "e0.airborne=", peek("enemies[0] && enemies[0].airborne"),
              "e0.z=", peek("enemies[0] && enemies[0].z || 0").toFixed(1),
              "e0.vz=", peek("enemies[0] && enemies[0].vz || 0").toFixed(1));
  snapshot("16_falling");
  step(40);
  console.log("after fall:",
              "e0.z=", peek("enemies[0] && enemies[0].z || 0").toFixed(1),
              "e0.airborne=", peek("enemies[0] && enemies[0].airborne"),
              "e0.knockdownFrames=", peek("enemies[0] && enemies[0].knockdownFrames || 0"));

  // ---- PARRY: tier classification by frame timing ----
  // Setup helper: place runner adjacent, force-start its swipe at a frame chosen
  // so that, after `targetParryFrame` ticks of advancing, the runner's active
  // phase starts (attackFrame becomes 7) on the same tick that the player's
  // parryFrame reaches `targetParryFrame`.
  function setupParry(targetParryFrame) {
    press("Escape"); step(2);
    press("Enter");  step(2);
    // attackFrame increments at the start of each updateRunner tick. Tick K sees
    // attackFrame = startFrame + K. Active phase starts when attackFrame = 7.
    // Choose startFrame so startFrame + targetParryFrame == 7.
    const startFrame = 7 - targetParryFrame;
    window.eval(
      "enemies[0].x = player.x + 22;" +
      "enemies[0].y = player.y;" +
      "enemies[0].attacking = true;" +
      "enemies[0].attackName = 'swipe';" +
      "enemies[0].attackFrame = " + startFrame + ";" +
      "enemies[0].attackHits = new Set();" +
      "enemies[1].hp = 0; enemies[1].dead = true; enemies[1].deathTimer = 100;" +
      "player.parryMeter = 0; player.parryChain = 0;"
    );
  }

  // PERFECT: parryFrame 1-3 when hit lands. Pick parryFrame=3 (last PERFECT frame).
  setupParry(3);
  const hpBefore_perfect = peek("enemies[0].hp");
  press("KeyI");
  step(3);
  console.log("PERFECT:",
              "p.hp=", peek("player.hp"),
              "p.meter=", peek("player.parryMeter"),
              "p.chain=", peek("player.parryChain"),
              "e0.hp=", peek("enemies[0].hp"),
              "e0.hitstun=", peek("enemies[0].hitstun"),
              "dmg=", hpBefore_perfect - peek("enemies[0].hp"));
  snapshot("17_parry_perfect");

  // GOOD: parryFrame 4-7 when hit.
  setupParry(6);
  press("KeyI");
  step(6);
  console.log("GOOD:",
              "p.hp=", peek("player.hp"),
              "p.meter=", peek("player.parryMeter"),
              "p.chain=", peek("player.parryChain"),
              "e0.hitstun=", peek("enemies[0].hitstun"));
  snapshot("18_parry_good");

  // LATE: parryFrame 8-12 when hit (block, no counter).
  setupParry(10);
  press("KeyI");
  step(10);
  console.log("LATE:",
              "p.hp=", peek("player.hp"),
              "p.meter=", peek("player.parryMeter"),
              "p.chain=", peek("player.parryChain"));
  snapshot("19_parry_late");

  // COUNTER-SPECIAL at full meter: J fires rio_counter free.
  press("Escape"); step(2);
  press("Enter");  step(2);
  window.eval("player.parryMeter = 100;");
  press("KeyJ");
  step(2);
  console.log("counter-special:",
              "atkName=", peek("player.attackName"),
              "meter=", peek("player.parryMeter"));
  snapshot("20_counter_special");

  // ---- BACK ATTACK: hold left (against facing=right) + J ----
  press("Escape"); step(2);
  press("Enter");  step(2);
  // Place runner directly behind player, facing right.
  window.eval(
    "player.facing = 1;" +
    "enemies[0].x = player.x - 18;" +
    "enemies[0].y = player.y;" +
    "enemies[1].hp = 0; enemies[1].dead = true; enemies[1].deathTimer = 100;"
  );
  hold("KeyA");      // hold back direction
  press("KeyJ");
  step(8);
  console.log("back_atk:",
              "atkName=", peek("player.attackName"),
              "e0.hp=", peek("enemies[0].hp"));
  release("KeyA");
  snapshot("21_back_atk");

  // ---- SPECIAL: Sunset Spin — costs HP, multi-hit AOE ----
  press("Escape"); step(2);
  press("Enter");  step(2);
  window.eval(
    "enemies[0].x = player.x + 18; enemies[0].y = player.y;" +
    "enemies[0].aiCooldown = 5;" +
    "enemies[1].x = player.x - 18; enemies[1].y = player.y;" +
    "enemies[1].aiCooldown = 5;"
  );
  const hpBeforeSpec = peek("player.hp");
  const e0HpBeforeSpec = peek("enemies[0].hp");
  press("KeyL");
  step(40);  // startup 5 + active 18 + recovery 14 = 37
  console.log("sunset spin:",
              "p.hp=", peek("player.hp"),  // should drop by 10 (hpCost)
              "p.hpDelta=", hpBeforeSpec - peek("player.hp"),
              "e0.hp=", peek("enemies[0].hp"),
              "e0.hpDelta=", e0HpBeforeSpec - peek("enemies[0].hp"),
              "e0.airborne=", peek("enemies[0].airborne"),
              "e1.hp=", peek("enemies[1].hp"));
  snapshot("22_sunset_spin");

  // ---- GRAB + THROW ----
  press("Escape"); step(2);
  press("Enter");  step(2);
  window.eval(
    "enemies[0].x = player.x + 16; enemies[0].y = player.y;" +
    "enemies[0].aiCooldown = 5;" +
    "enemies[1].hp = 0; enemies[1].dead = true; enemies[1].deathTimer = 100;"
  );
  press("KeyU");  // grab
  step(2);
  console.log("grab:",
              "p.grabbing!=null=", peek("player.grabbing != null"),
              "e0.grabbedBy!=null=", peek("enemies[0].grabbedBy != null"));
  snapshot("23_grab");
  // Throw forward.
  hold("KeyD");
  press("KeyJ");
  step(15);
  console.log("throw:",
              "e0.airborne=", peek("enemies[0].airborne"),
              "e0.knockX=", peek("enemies[0].knockX || 0").toFixed(1),
              "e0.hp=", peek("enemies[0].hp"));
  release("KeyD");
  snapshot("24_throw");

  console.log("\nERRORS:", errors.length);
  for (const e of errors) console.log("  -", e);
  process.exit(errors.length ? 1 : 0);
})();
