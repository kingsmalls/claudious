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

// Helper: drive the state machine from ANY state to a fresh "playing" run.
// Always cycles through title and select so tests start from clean state
// rather than reusing an in-progress run.
function goToPlay() {
  if (window.eval("STATE") !== "title") {
    press("Escape"); step(4);
  }
  // From title press through select → playing.
  if (window.eval("STATE") === "title") {
    press("Enter"); step(4);
  }
  if (window.eval("STATE") === "select") {
    press("Enter"); step(4);
  }
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

  press("Enter"); step(2);   // title -> select
  press("Enter"); step(2);   // select -> playing
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
  goToPlay();
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
  goToPlay();
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
  goToPlay();
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
  goToPlay();
  press("KeyK"); step(15);
  console.log("heavy whiff:",
              "atkName=", peek("player.attackName"),
              "atkFrame=", peek("player.attackFrame"));
  snapshot("13_launcher");

  // ---- LAUNCHER: position runner adjacent and disable its AI swipe ----
  goToPlay();
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
    goToPlay();
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
  goToPlay();
  window.eval("player.parryMeter = 100;");
  press("KeyJ");
  step(2);
  console.log("counter-special:",
              "atkName=", peek("player.attackName"),
              "meter=", peek("player.parryMeter"));
  snapshot("20_counter_special");

  // ---- BACK ATTACK: hold left (against facing=right) + J ----
  goToPlay();
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
  goToPlay();
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
  goToPlay();
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

  // ---- DUKE: pick character on title, jab, sunset → rolling thunder ----
  press("Escape"); step(2);
  press("Digit2"); step(2);
  press("Enter");  step(2);
  console.log("duke chosen: char =", peek("player.char"),
              "hp=", peek("player.hp"),
              "walkSpeed=", peek("player.walkSpeed"));
  // Walk in.
  hold("KeyD");
  while (true) {
    step(2);
    const e0 = peek("enemies[0]");
    if (!e0) break;
    if (e0.x - peek("player.x") < 24 && e0.x - peek("player.x") > 0) break;
  }
  release("KeyD"); step(2);
  press("KeyJ"); step(7);
  console.log("duke jab: e0.hp =", peek("enemies[0].hp"));
  snapshot("25_duke_idle_atk");
  press("KeyL");  // rolling thunder
  step(40);
  console.log("rolling thunder: p.hp=", peek("player.hp"),
              "e0.hp=", peek("enemies[0] && enemies[0].hp"));
  snapshot("26_duke_special");

  // ---- ATLAS ----
  // Force atlas unlocked for the test (early in the run it's still locked).
  window.eval("save.unlocks.atlas = true; selectedChar = 'atlas';");
  goToPlay();
  console.log("atlas chosen: char =", peek("player.char"),
              "hp=", peek("player.hp"),
              "walkSpeed=", peek("player.walkSpeed"));
  hold("KeyD");
  while (true) {
    step(2);
    const e0 = peek("enemies[0]");
    if (!e0) break;
    if (e0.x - peek("player.x") < 28 && e0.x - peek("player.x") > 0) break;
  }
  release("KeyD"); step(2);
  press("KeyJ"); step(8);
  console.log("atlas atk1: e0.hp =", peek("enemies[0].hp"));
  snapshot("27_atlas_idle_atk");
  press("KeyL"); step(45);
  console.log("foundation stone: p.hp=", peek("player.hp"),
              "e0.hp=", peek("enemies[0] && enemies[0].hp"),
              "e0.airborne=", peek("enemies[0] && enemies[0].airborne"));
  snapshot("28_atlas_special");

  // ---- MILESTONE WORD: NICE! at hit #5 ----
  press("Escape"); step(2);
  press("Digit1"); step(2);
  press("Enter");  step(2);
  window.eval(
    "enemies[0].x = player.x + 22; enemies[0].y = player.y;" +
    "enemies[0].aiCooldown = 5; enemies[0].hp = 9999;" +
    "enemies[1].dead = true; enemies[1].deathTimer = 100;" +
    "player.comboHits = 4; player.comboTimer = 1.4;"
  );
  press("KeyJ"); step(7);
  console.log("milestone NICE: comboHits =", peek("player.comboHits"));
  snapshot("29_milestone_nice");

  // ---- MILESTONE WORD: AWESOME! at hit #10 ----
  window.eval(
    "enemies[0].iframes = 0; enemies[0].hitstun = 0;" +
    "player.comboHits = 9; player.comboTimer = 1.4;"
  );
  step(20);
  press("KeyJ"); step(7);
  console.log("milestone AWESOME: comboHits =", peek("player.comboHits"));
  snapshot("30_milestone_awesome");

  // ---- ENEMY GALLERY: spawn each new type and snapshot ----
  press("Escape"); step(2);
  press("Digit1"); step(2);
  press("Enter");  step(2);
  // Replace the default spawn with one of each new type lined up across the stage.
  window.eval(
    "enemies = [" +
    "  makeEnemy('tank',      180, 282)," +
    "  makeEnemy('lamplight', 240, 322)," +
    "  makeEnemy('slice',     300, 282)," +
    "  makeEnemy('chains',    360, 322)," +
    "  makeEnemy('shade',     420, 282)," +
    "  makeEnemy('dojo',      480, 322)," +
    "  makeEnemy('rig',       560, 282)" +
    "];" +
    "for (const e of enemies) e.aiCooldown = 999;"
  );
  step(8);
  console.log("gallery: enemies =", peek("enemies.length"));
  snapshot("31_enemy_gallery");

  // ---- LAMPLIGHT projectile ----
  window.eval(
    "enemies = [makeEnemy('lamplight', 400, 300)];" +
    "enemies[0].aiCooldown = 0;" +
    "player.x = 320; player.y = 300;"
  );
  step(15);
  console.log("lamplight projectiles:", peek("projectiles.length"),
              "atkName=", peek("enemies[0].attackName"));
  snapshot("32_lamplight_shoot");

  // ---- TANK super-armor ----
  window.eval(
    "enemies = [makeEnemy('tank', player.x + 40, player.y)];" +
    "enemies[0].aiCooldown = 999;"
  );
  hold("KeyD");
  while (true) {
    step(2);
    if (Math.abs(peek("enemies[0].x") - peek("player.x")) < 24) break;
  }
  release("KeyD"); step(2);
  press("KeyJ"); step(8);
  const tankHpAfter1 = peek("enemies[0].hp");
  const tankHitstunAfter1 = peek("enemies[0].hitstun");
  console.log("tank hit 1: hp =", tankHpAfter1, "hitstun =", tankHitstunAfter1,
              "(should not stun on first hit)");
  snapshot("33_tank_armor");

  // ---- DOJO deflect ----
  goToPlay();
  window.eval(
    "enemies = [makeEnemy('dojo', player.x + 22, player.y)];" +
    "enemies[0].aiCooldown = 999;" +
    "enemies[0].guardActive = true;" +
    "enemies[0].guardTimer = 0;"
  );
  press("KeyJ"); step(8);
  console.log("dojo deflect:",
              "p.hitstun =", peek("player.hitstun"),
              "dojo.attacking =", peek("enemies[0].attacking"));
  snapshot("34_dojo_deflect");

  // ---- STAGE BACKDROPS: snapshot each ----
  for (let s = 0; s < 5; s++) {
    goToPlay();
    window.eval("currentStage = " + s + "; enemies = []; particles = []; projectiles = [];");
    step(4);
    console.log("stage " + s + " (" + peek("STAGES[" + s + "].name") + "): rendered");
    snapshot("4" + s + "_stage_" + s);
  }

  // ---- STAGE PROGRESSION: clear wave, observe wave delay then next wave spawn ----
  goToPlay();
  window.eval("currentStage = 0; currentWave = 0; enemies.forEach(e => { e.dead = true; e.deathTimer = 100; });");
  step(70); // wait for waveDelay (1.0s) + cleanup
  console.log("after clear wave 0: currentWave =", peek("currentWave"),
              "enemies =", peek("enemies.length"),
              "waveDelay =", peek("waveDelay").toFixed(2));
  snapshot("46_wave_advance");

  // ---- BARON: spawn directly and verify HP bar + AI pattern ----
  goToPlay();
  window.eval(
    "currentStage = 2; currentWave = 0;" +
    "enemies = [makeEnemy('baron', 480, 300)];" +
    "particles = [];"
  );
  step(8);
  console.log("baron spawned:",
              "type=", peek("enemies[0].type"),
              "isBoss=", peek("enemies[0].isBoss"),
              "hp=", peek("enemies[0].hp"),
              "name=", peek("enemies[0].bossName"));
  snapshot("47_baron_spawn");
  // Watch the AI run through its first attack.
  step(60);
  console.log("baron after 60f:",
              "atkName=", peek("enemies[0].attackName"),
              "patternStep=", peek("enemies[0].bossPatternStep"));
  snapshot("48_baron_attacking");
  // Land some hits to confirm super-armor.
  hold("KeyD");
  while (true) {
    step(2);
    if (Math.abs(peek("enemies[0].x") - peek("player.x")) < 26) break;
    if (peek("enemies[0].dead")) break;
  }
  release("KeyD"); step(2);
  for (let i = 0; i < 5; i++) {
    press("KeyJ"); step(8);
  }
  console.log("after 5 jabs: baron.hp =", peek("enemies[0].hp"),
              "hitstun =", peek("enemies[0].hitstun"));
  snapshot("49_baron_armor");

  // ---- SAVE / LOAD: Atlas unlock after clearing 3 stages ----
  console.log("before unlock: atlas =", peek("save.unlocks.atlas"));
  goToPlay();
  // Simulate clearing three stages.
  window.eval(
    "player.stagesClearedThisRun = 0;" +
    "for (let s = 0; s < 3; s++) { currentStage = s; player.maxCombo = 12 + s; beginStageClear(); }"
  );
  console.log("after 3 clears: atlas unlocked =", peek("save.unlocks.atlas"),
              "bestCombo =", peek("save.bestCombo"));

  // Verify finalizeRun records score.
  window.eval(
    "player.damageDealt = 320; player.maxCombo = 22; player.parryPerfectCount = 4;" +
    "player.parryGoodCount = 6; player.stagesClearedThisRun = 5;" +
    "finalizeRun(true);"
  );
  console.log("score =", peek("player.score"),
              "highScore[rio] =", peek("save.highScores.rio"));
  // localStorage round-trip.
  const fromLs = peek("typeof localStorage !== 'undefined' ? localStorage.getItem('the_block.save.v1') : null");
  console.log("localStorage save bytes =", (fromLs || "").length);

  // Title screen with unlocks visible + hi-score readout.
  press("Escape"); step(2);
  step(8);
  snapshot("50_title_with_save");

  // ---- LATE-GAME STAGES: snapshot backdrops 6-10 ----
  for (let s = 5; s < 10; s++) {
    goToPlay();
    if (!peek("player")) {
      // Force enter playing — title machinery may have eaten the Enter.
      window.eval("enterPlaying();");
      step(2);
    }
    window.eval("currentStage = " + s + "; enemies = []; particles = []; projectiles = []; player.x = 120; player.y = 300;");
    step(6);
    console.log("stage " + s + " (" + peek("STAGES[" + s + "].name") + "): STATE=" + peek("STATE"));
    snapshot("S" + (s + 1) + "_stage");
  }

  // ---- LATE BOSSES: spawn each, snapshot ----
  for (const b of ["razor", "volt", "blackwell"]) {
    goToPlay();
    window.eval("enemies = [makeEnemy('" + b + "', 460, 300)];");
    step(8);
    console.log(b + ": hp =", peek("enemies[0].hp"),
                "name =", peek("enemies[0].bossName"));
    snapshot("6" + b[0] + "_" + b);
  }

  // ---- CHARACTER SELECT screen ----
  press("Escape"); step(2);
  // From title, Enter goes to select.
  press("Enter"); step(4);
  console.log("select state =", peek("STATE"), "selectedChar =", peek("selectedChar"));
  snapshot("80_select_rio");
  press("ArrowRight"); step(4);
  console.log("after right: selectedChar =", peek("selectedChar"));
  snapshot("81_select_duke");
  press("ArrowRight"); step(4);
  console.log("after right (atlas unlocked? " + peek("save.unlocks.atlas") + "): selectedChar =", peek("selectedChar"));
  snapshot("82_select_atlas");
  press("Enter"); step(4);
  console.log("after enter from select: STATE =", peek("STATE"));

  // ---- KANE CINEMATIC: enter directly and watch ----
  goToPlay();
  window.eval("currentStage = 9;");
  step(2);
  window.eval("beginKaneCinematic();");
  step(60); // ~1 second in
  console.log("cinematic at 1s: state =", peek("STATE"),
              "t =", peek("cineState && cineState.t").toFixed(2));
  snapshot("70_kane_cinematic");
  // Press J at the right moment.
  step(36); // approach the first prompt at t=1.6
  press("KeyJ");
  step(60);
  console.log("after J #1: prompts.hit =",
              peek("cineState && cineState.prompts[0].hit"));
  snapshot("71_kane_strike");

  console.log("\nERRORS:", errors.length);
  for (const e of errors) console.log("  -", e);
  process.exit(errors.length ? 1 : 0);
})();
