import { cpSync, existsSync, mkdirSync, rmSync } from 'node:fs';
import { join } from 'node:path';

const root = decodeURIComponent(new URL('..', import.meta.url).pathname);
const output = join(root, 'dist');

rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });

for (const item of ['index.html', 'styles.css', 'app.js', 'public']) {
  const source = join(root, item);
  if (!existsSync(source)) throw new Error(`Missing build input: ${item}`);
  cpSync(source, join(output, item), { recursive: true });
}

const sloganSource = join(root, 'resource', 'assets', 'slogan橫式白.svg');
const sloganOutput = join(output, 'resource', 'assets', 'slogan橫式白.svg');
mkdirSync(join(output, 'resource', 'assets'), { recursive: true });
cpSync(sloganSource, sloganOutput);

console.log(`Static site built at ${output}`);
