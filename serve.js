#!/usr/bin/env node
// Tiny dev server. Run with: node serve.js   (or:  npm run play)
// Serves the project directory at http://localhost:8765/the_block.html
// Auto-opens the browser if possible. Ctrl+C to stop.

const http = require("http");
const fs   = require("fs");
const path = require("path");
const { exec } = require("child_process");

const PORT = 8765;
const ROOT = __dirname;
const URL  = `http://localhost:${PORT}/the_block.html`;

const types = {
  ".html": "text/html",
  ".js":   "application/javascript",
  ".json": "application/json",
  ".png":  "image/png",
  ".jpg":  "image/jpeg",
  ".css":  "text/css",
  ".svg":  "image/svg+xml",
};

const srv = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split("?")[0]);
  const f = path.join(ROOT, u === "/" ? "/the_block.html" : u);
  if (!f.startsWith(ROOT)) { res.writeHead(403); res.end(); return; }
  fs.readFile(f, (err, data) => {
    if (err) { res.writeHead(404); res.end("Not found: " + u); return; }
    res.writeHead(200, { "Content-Type": types[path.extname(f)] || "application/octet-stream" });
    res.end(data);
  });
});

srv.listen(PORT, "127.0.0.1", () => {
  console.log("");
  console.log("  THE BLOCK — local dev server");
  console.log("  ────────────────────────────────");
  console.log("  Game:    " + URL);
  console.log("  Landing: http://localhost:" + PORT + "/landing.html");
  console.log("");
  console.log("  Press Ctrl+C to stop.");
  console.log("");
  // Best-effort: open the default browser. Silently ignored if the OS
  // command isn't available.
  const opener =
    process.platform === "darwin" ? "open" :
    process.platform === "win32"  ? "start \"\"" :
                                    "xdg-open";
  exec(`${opener} ${URL}`, () => {});
});
