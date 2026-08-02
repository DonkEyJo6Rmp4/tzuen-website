import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = decodeURIComponent(new URL('..', import.meta.url).pathname);
const read = (file) => readFileSync(join(root, file), 'utf8');

for (const file of ['index.html', 'styles.css', 'app.js']) {
  assert.ok(existsSync(join(root, file)), `${file} must exist`);
}

const html = read('index.html');
const app = read('app.js');

for (const section of ['about', 'work', 'legal', 'news', 'contact']) {
  assert.match(html, new RegExp(`id=["']${section}["']`), `missing #${section}`);
}

assert.match(html, /logo-round\.webp/);
assert.match(html, /Tzuen\/assets\/slogan橫式白\.svg/);
assert.match(html, /財團法人佛教慈恩育幼基金/);
assert.match(html, /Buddhist Tzuen Children’s Welfare Foundation/);
assert.doesNotMatch(html, /calligraphy-card/);
assert.match(html, /重要資料_立案證書\.webp/);
assert.match(html, /重要資料_法人登記證\.webp/);
assert.match(html, /loading="lazy"/);
assert.match(app, /Be the Sunshine That Warms Every Heart\./);
assert.match(app, /讓自己成為最溫暖的陽光/);
assert.match(app, /localStorage/);
assert.equal((app.match(/date:/g) || []).length, 14, 'seven dated services required in each language');
assert.match(html, /04771311/);
assert.match(html, /tzuen76201061@gmail\.com/);

console.log('Static website checks passed.');
