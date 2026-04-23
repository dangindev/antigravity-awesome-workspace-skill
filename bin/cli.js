#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const args = process.argv.slice(2);
const pyScript = path.join(__dirname, '..', 'init_vibe_project.py');

if (!fs.existsSync(pyScript)) {
  console.error(`[-] Error: Cannot find init script at ${pyScript}`);
  process.exit(1);
}

// First try `python`
let result = spawnSync('python', [pyScript, ...args], { stdio: 'inherit' });

// If `python` command is not found, fallback to `python3`
if (result.error && result.error.code === 'ENOENT') {
  result = spawnSync('python3', [pyScript, ...args], { stdio: 'inherit' });
}

if (result.error) {
  console.error(`[-] Failed to execute init script: ${result.error.message}`);
  process.exit(1);
}

process.exit(result.status !== null ? result.status : 1);
