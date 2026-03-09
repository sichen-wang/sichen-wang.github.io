import { mkdirSync, existsSync, writeFileSync } from 'node:fs';
import path from 'node:path';

const VALID_CATEGORIES = ['CP', 'Research', 'Courses', 'Essays'];
const DEFAULT_CATEGORY = 'CP';

function printUsage() {
  process.stdout.write(
    [
      'Usage:',
      '  npm run new:blog -- "Article Title"',
      '  npm run new:blog -- "Article Title" Courses',
      '  npm run new:blog -- --category Research "Article Title"',
      '  npm run new:blog -- --dry-run "Article Title" Essays',
      '',
      `Valid categories: ${VALID_CATEGORIES.join(', ')}`,
    ].join('\n') + '\n',
  );
}

function fail(message) {
  process.stderr.write(`[new:blog] ${message}\n`);
  process.exit(1);
}

function formatDate(date) {
  const pad = (value) => String(value).padStart(2, '0');
  return [
    `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`,
    `${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`,
  ].join(' ');
}

function parseArgs(argv) {
  const positional = [];
  let category = DEFAULT_CATEGORY;
  let dryRun = false;

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];

    if (arg === '--help' || arg === '-h') {
      printUsage();
      process.exit(0);
    }

    if (arg === '--dry-run') {
      dryRun = true;
      continue;
    }

    if (arg === '--category' || arg === '-c') {
      const value = argv[i + 1];
      if (!value) fail('Missing value after --category.');
      category = value;
      i += 1;
      continue;
    }

    positional.push(arg);
  }

  if (positional.length === 0) {
    printUsage();
    fail('Missing article title.');
  }

  if (positional.length >= 2 && category === DEFAULT_CATEGORY) {
    category = positional[1];
  }

  return {
    title: positional[0],
    category,
    dryRun,
  };
}

const { title: rawTitle, category: rawCategory, dryRun } = parseArgs(process.argv.slice(2));
const title = rawTitle.trim();
const category = rawCategory.trim();

if (!title) fail('Article title cannot be empty.');
if (/[\\/]/.test(title)) fail('Article title cannot contain path separators.');
if (!VALID_CATEGORIES.includes(category)) {
  fail(`Invalid category "${category}". Valid categories: ${VALID_CATEGORIES.join(', ')}.`);
}

const postDir = path.join(process.cwd(), 'content', 'blog', title);
const postFile = path.join(postDir, 'index.md');

if (existsSync(postDir) || existsSync(postFile)) {
  fail(`Target already exists: ${postDir}`);
}

const content = [
  '---',
  `title: ${JSON.stringify(title)}`,
  `date: "${formatDate(new Date())}"`,
  'card_summary: |-',
  '  ',
  'tags: []',
  'categories:',
  `  - ${JSON.stringify(category)}`,
  '---',
  '',
  'Write the summary here.',
  '',
  '<!--more-->',
  '',
  '## Notes',
  '',
  'Start writing here.',
  '',
].join('\n');

if (dryRun) {
  process.stdout.write(`[new:blog] Would create: ${postFile}\n\n${content}`);
  process.exit(0);
}

mkdirSync(postDir, { recursive: true });
writeFileSync(postFile, content, 'utf8');

process.stdout.write(
  [
    `[new:blog] Created ${postFile}`,
    '[new:blog] You can now run `npm run dev` to preview it.',
  ].join('\n') + '\n',
);
