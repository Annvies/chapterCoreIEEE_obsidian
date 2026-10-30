// Uso (desde la raíz de la bóveda): node .claude/skills/obsidian-cerebros/scripts/navegabilidad.mjs .
// Comprueba que desde el cerebro central y desde cada "Cerebro N" se llega, siguiendo enlaces [[...]],
// a todas las notas de su módulo, y cuántos clics hacen falta como máximo. Solo lee archivos.
import fs from 'fs'; import path from 'path';
const root = process.argv[2]; const dir = path.join(root, 'Cerebros');
const notes = new Map();
for (const f of fs.readdirSync(dir)) if (f.endsWith('.md')) notes.set(f.slice(0, -3), fs.readFileSync(path.join(dir, f), 'utf8'));
const links = t => [...t.matchAll(/\[\[([^\]|#]+)/g)].map(m => m[1].trim());
const mod = t => (t.match(/^\s+- modulo-(\d)\s*$/m) || [])[1];
const type = t => (t.match(/^type: (.+)$/m) || [])[1] || (t.includes('- subgrupo') ? 'subgrupo' : 'otro');
function bfs(start, same) {
  const seen = new Map([[start, 0]]), q = [start];
  while (q.length) { const n = q.shift(); for (const l of links(notes.get(n) || '')) if (notes.has(l) && !seen.has(l) && same(l)) { seen.set(l, seen.get(n) + 1); q.push(l); } }
  return seen;
}
const central = bfs('ChapterCore - Cerebro central', () => true);
console.log(`Desde el central: ${central.size}/${notes.size} notas, máx ${Math.max(...central.values())} clics`);
for (let m = 1; m <= 7; m++) {
  const hub = [...notes.keys()].find(n => n.startsWith(`Cerebro ${m} - `));
  const mine = [...notes.keys()].filter(n => mod(notes.get(n)) === String(m));
  const seen = bfs(hub, l => mod(notes.get(l)) === String(m));
  const tipos = {}; for (const n of mine) { const t = type(notes.get(n)); tipos[t] = (tipos[t] || 0) + 1; }
  const miss = mine.filter(n => !seen.has(n));
  console.log(`M${m}: ${seen.size}/${mine.length} alcanzables, máx ${Math.max(...seen.values())} clics ·`, JSON.stringify(tipos), miss.length ? 'NO: ' + miss.join(' | ') : '');
}
