#!/usr/bin/env node
/* Teslim denetimi — gate.js'in ölçmediği üç şey. Yalnız YENİ sınavlara bakar:
   node tools/teslim_check.js <vak> <ilk-sınav-no> ["yasak|terim|regex"]
   1. Doğru şık tek başına en kısa, dosya başına ≤%40 (kapı 17'nin tersi: çeldiriciyi şişirerek geçmeyi yakalar)
   2. Yakın kopya: mevcut ya da başka yeni bir soruyla kelime benzerliği ≥0,7 (gate kural 2 yalnız birebir)
   3. Yasak terim: kitapta olmayan kavramlar, soru/şık/cevap/uitleg'in hepsinde
   Bulgu varsa exit 1. */
const fs = require('fs'), vm = require('vm'), path = require('path');
const [vak, ilk, yasak] = process.argv.slice(2);
if (!vak || !ilk) { console.log('kullanım: node tools/teslim_check.js <vak> <ilk-no> ["regex"]'); process.exit(2); }
const d = path.join(__dirname, '..', 'havo3', vak, 'js');
const c = { console }; c.window = c; vm.createContext(c);
vm.runInContext(fs.readFileSync(path.join(d, 'bootstrap.js'), 'utf8'), c);
c.DURU.examens = []; c.DURU.registerExamen = e => c.DURU.examens.push(e);
for (const f of fs.readdirSync(path.join(d, 'data')).sort()) vm.runInContext(fs.readFileSync(path.join(d, 'data', f), 'utf8'), c, { filename: f });
const D = c.DURU, no = e => +(String(e.id).match(/(\d+)$/) || [0, 0])[1], yeni = e => no(e) >= +ilk;
const woorden = s => new Set(String(s).toLowerCase().replace(/<[^>]+>/g, ' ').match(/[a-zà-ÿ0-9]{4,}/g) || []);
const sim = (a, b) => { let n = 0; for (const x of a) if (b.has(x)) n++; return n / (a.size + b.size - n || 1); };
let bulgu = 0; const meld = s => { bulgu++; console.log(s); };

for (const e of D.examens.filter(yeni)) {
  const mc = e.vragen.filter(v => v.type === 'mc');
  const kort = mc.filter(v => { const g = v.opties[v.antwoord].length; return v.opties.every((o, i) => i === v.antwoord || o.length > g); }).length;
  if (mc.length >= 6 && kort / mc.length > 0.4) meld(`KISA ${e.id}: doğru şık ${kort}/${mc.length} kez tek başına en kısa`);
}
const alle = [];
for (const e of D.examens) e.vragen.forEach((v, i) => alle.push({ k: `${no(e)}#${i + 1}`, n: yeni(e), w: woorden(v.vraag), s: v.vraag }));
for (const o of D.onderwerpen) o.vragen.forEach((v, i) => alle.push({ k: `${o.id}#${i + 1}`, n: false, w: woorden(v.vraag), s: v.vraag }));
alle.forEach((a, i) => { if (a.w.size >= 4) alle.forEach((b, j) => {
  if (a.n && (!b.n || i < j) && a !== b && b.w.size >= 4 && sim(a.w, b.w) >= 0.7) meld(`KOPYA ${a.k} ~ ${b.k}: ${a.s.slice(0, 70)} || ${b.s.slice(0, 70)}`);
}); });
if (yasak) { const re = new RegExp(yasak, 'i');
  for (const e of D.examens.filter(yeni)) e.vragen.forEach((v, i) => {
    const m = [v.vraag, ...(v.opties || []), v.antwoord, v.modelantwoord, v.uitleg].join(' ').match(re);
    if (m) meld(`TERİM ${no(e)}#${i + 1} "${m[0]}": ${v.vraag.slice(0, 80)}`);
  });
}
console.log(bulgu ? `${bulgu} bulgu` : 'temiz'); process.exit(bulgu ? 1 : 0);
