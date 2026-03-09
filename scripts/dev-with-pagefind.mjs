import { spawn } from 'node:child_process';
import { createInterface } from 'node:readline';
import { existsSync } from 'node:fs';

const HUGO_ARGS = ['server', '--disableFastRender'];
const PATH_PREFIXES = ['/usr/local/go/bin', '/usr/local/bin'];

let debounceTimer = null;
let pagefindProcess = null;
let rerunRequested = false;
let shuttingDown = false;

function buildEnv() {
  const currentPath = process.env.PATH ?? '';
  const parts = currentPath.split(':').filter(Boolean);

  for (const prefix of PATH_PREFIXES) {
    if (existsSync(prefix) && !parts.includes(prefix)) {
      parts.unshift(prefix);
    }
  }

  return {
    ...process.env,
    PATH: parts.join(':'),
  };
}

function log(message) {
  process.stdout.write(`[dev:search] ${message}\n`);
}

function schedulePagefind(reason) {
  if (shuttingDown) return;
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => runPagefind(reason), 250);
}

function runPagefind(reason) {
  if (shuttingDown) return;

  if (pagefindProcess) {
    rerunRequested = true;
    return;
  }

  log(`Updating Pagefind index after ${reason}...`);

  pagefindProcess = spawn('npx', ['pagefind', '--site', 'public'], {
    stdio: 'inherit',
    env: buildEnv(),
  });

  pagefindProcess.on('exit', (code) => {
    const shouldRerun = rerunRequested;
    pagefindProcess = null;
    rerunRequested = false;

    if (code === 0) {
      log('Pagefind index is up to date.');
    } else if (!shuttingDown) {
      process.stderr.write(`[dev:search] Pagefind exited with code ${code ?? 'unknown'}.\n`);
    }

    if (shouldRerun && !shuttingDown) {
      schedulePagefind('a queued Hugo rebuild');
    }
  });

  pagefindProcess.on('error', (error) => {
    pagefindProcess = null;
    process.stderr.write(`[dev:search] Failed to run Pagefind: ${error.message}\n`);
  });
}

function pipeHugoOutput(stream, output) {
  const rl = createInterface({ input: stream });
  rl.on('line', (line) => {
    output.write(`${line}\n`);

    const trimmed = line.trim();
    if (/^(Built|Total) in\b/.test(trimmed)) {
      schedulePagefind('the latest Hugo build');
    }
  });
}

function shutdown(hugoProcess) {
  if (shuttingDown) return;
  shuttingDown = true;
  clearTimeout(debounceTimer);

  if (pagefindProcess) {
    pagefindProcess.kill('SIGTERM');
  }

  if (hugoProcess.exitCode === null) {
    hugoProcess.kill('SIGINT');
  }
}

log('Starting Hugo with automatic Pagefind indexing...');

const hugoProcess = spawn('hugo', HUGO_ARGS, {
  stdio: ['inherit', 'pipe', 'pipe'],
  env: buildEnv(),
});

pipeHugoOutput(hugoProcess.stdout, process.stdout);
pipeHugoOutput(hugoProcess.stderr, process.stderr);

hugoProcess.on('error', (error) => {
  process.stderr.write(`[dev:search] Failed to start Hugo: ${error.message}\n`);
  process.exit(1);
});

hugoProcess.on('exit', (code, signal) => {
  clearTimeout(debounceTimer);

  if (shuttingDown) {
    process.exit(0);
  }

  if (signal) {
    process.exit(1);
  }

  process.exit(code ?? 1);
});

process.on('SIGINT', () => shutdown(hugoProcess));
process.on('SIGTERM', () => shutdown(hugoProcess));
