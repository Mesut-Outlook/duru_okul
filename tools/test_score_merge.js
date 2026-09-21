/* =========================================================
   tools/test_score_merge.js — regressietest voor de score-merger

   Waarom dit bestaat: op 2026-09-20 bleek restoreScores() in js/landing.js
   de localStorage-sleutel te OVERSCHRIJVEN in plaats van samen te voegen.
   Elke cloud-pull (elke 20 s) verving Duru's lokale voortgang door wat er in
   de cloud stond. Kosten: 865 XP -> 95 en 5 -> 1 medaille bij natuurkunde,
   plus 199 pogingen over vier vakken.

   De regel die deze test bewaakt: SAMENVOEGEN MAG GROEIEN, NOOIT KRIMPEN.
   De functies worden LETTERLIJK uit js/landing.js gesneden en op een nep-
   localStorage uitgevoerd, zodat de test de echte broncode meet.

   Gebruik:  node tools/test_score_merge.js [pad/naar/landing.js]
   Exit 0 = alles goed, exit 1 = merger is kapot.
   Zie CLAUDE.md -> "Skor kayit hatti" en docs/ENGINE_SPEC.md.
   ========================================================= */

const fs = require('fs');
const path = require('path');
const LANDING = process.argv[2] || path.join(__dirname, '..', 'js', 'landing.js');
const src = fs.readFileSync(LANDING, 'utf8');

function slice(name) {
  const start = src.indexOf('  function ' + name + '(');
  if (start < 0) {
    // Oudere landing.js zonder de pure merger: dat is precies de kapotte vorm.
    console.error('FAIL  ' + name + '() niet gevonden in ' + LANDING +
                  '\n      Deze landing.js mist de merger — zie CLAUDE.md -> ' +
                  '"Bulut senkron & birlestirme degismezi".');
    process.exit(1);
  }
  let depth = 0, i = src.indexOf('{', start);
  for (let j = i; j < src.length; j++) {
    if (src[j] === '{') depth++;
    else if (src[j] === '}') { depth--; if (depth === 0) return src.slice(start, j + 1); }
  }
  throw new Error('kapanmadi: ' + name);
}

const store = {};
const localStorage = {
  getItem: k => (k in store ? store[k] : null),
  setItem: (k, v) => { store[k] = String(v); },
  removeItem: k => { delete store[k]; },
  key: i => Object.keys(store)[i],
  get length() { return Object.keys(store).length; }
};

const bron = slice('parseAttemptDate') + '\n' + slice('mergeScoreItems') + '\n' + slice('restoreScores');
const api = new Function('localStorage', bron + '\nreturn { restoreScores: restoreScores, merge: mergeScoreItems };')(localStorage);
const fn = api.restoreScores;
const merge = api.merge;

let fail = 0;
const kort = v => { const t = JSON.stringify(v); return t && t.length > 70 ? t.slice(0, 67) + '...' : t; };
const ok = (naam, got, exp) => {
  const good = JSON.stringify(got) === JSON.stringify(exp);
  if (!good) fail++;
  // Bij PASS alleen de naam; bij FAIL de (ingekorte) waarden, anders verzuipt
  // een geslaagde run in JSON.
  console.log(good ? 'PASS ' + naam
                   : 'FAIL ' + naam + '  beklenen=' + kort(exp) + ' gelen=' + kort(got));
};

/* ── 1) voortgang: yereldeki XP/madalya, fakir uzak pakette yok ── */
store['duru_2627_natuurkunde_v1'] = JSON.stringify({
  xp: 865, streak: 11, badges: { a: 1, b: 2, c: 3, d: 4, e: 5 },
  beste: { t1: 90 }, gedaan: { t1: true }, pogingen: { t1: 7 }, titels: { t1: 'x' }
});
fn([{ key: 'duru_2627_natuurkunde_v1', val: { xp: 95, streak: 1, badges: { a: 1 }, beste: { t1: 40 }, pogingen: { t1: 1 } } }]);
let v = JSON.parse(store['duru_2627_natuurkunde_v1']);
ok('XP korunuyor (max)',        v.xp, 865);
ok('streak korunuyor (max)',    v.streak, 11);
ok('madalyalar korunuyor',      Object.keys(v.badges).length, 5);
ok('beste korunuyor (max)',     v.beste.t1, 90);
ok('pogingen korunuyor (max)',  v.pogingen.t1, 7);

/* ── 2) voortgang: uzak paket YENI madalya getiriyor -> eklenmeli ── */
fn([{ key: 'duru_2627_natuurkunde_v1', val: { xp: 900, badges: { z: 9 } } }]);
v = JSON.parse(store['duru_2627_natuurkunde_v1']);
ok('yeni XP aliniyor',          v.xp, 900);
ok('yeni madalya ekleniyor',    Object.keys(v.badges).length, 6);

/* ── 3) examens: history union, kucuk paket silmemeli ── */
store['duru_2627_frans_examens_v1'] = JSON.stringify({
  beste: {}, laatste: {},
  history: [{ attemptId: 'att_1000', examId: 'ex-1', pct: 80, datum: '01-09-2026 10:00' },
            { attemptId: 'att_2000', examId: 'ex-2', pct: 60, datum: '02-09-2026 10:00' }]
});
fn([{ key: 'duru_2627_frans_examens_v1', val: { history: [{ attemptId: 'att_3000', examId: 'ex-3', pct: 40, datum: '03-09-2026 10:00' }] } }]);
let e = JSON.parse(store['duru_2627_frans_examens_v1']);
ok('history union',             e.history.length, 3);
ok('beste yeniden hesaplandi',  e.beste['ex-1'], 80);
ok('en yeni en basta',          e.history[0].attemptId, 'att_3000');

/* ── 4) ayni poging iki kez -> tekilleniyor ── */
fn([{ key: 'duru_2627_frans_examens_v1', val: { history: [{ attemptId: 'att_1000', examId: 'ex-1', pct: 80, datum: '01-09-2026 10:00' }] } }]);
e = JSON.parse(store['duru_2627_frans_examens_v1']);
ok('tekrar poging eklenmiyor',  e.history.length, 3);

/* ── 5) bozuk yerel deger -> cokmemeli ── */
store['duru_2627_duits_v1'] = '{bozuk json';
fn([{ key: 'duru_2627_duits_v1', val: { xp: 50, badges: {} } }]);
ok('bozuk yerel deger kurtariliyor', JSON.parse(store['duru_2627_duits_v1']).xp, 50);

/* ── 6) PUSH-pad: pure merger mag de cloud niet uitkleden ──
   cloud_sync.js leest de knoop, voegt samen met het lokale en schrijft pas dan.
   Verarmd lokaal + rijke cloud moet RIJK opleveren, niet arm. */
const rijkeCloud = [{ key: 'duru_2627_natuurkunde_v1', val: { xp: 865, streak: 11, badges: { a:1,b:2,c:3,d:4,e:5 }, beste: { t1: 90 }, pogingen: { t1: 7 } } }];
const armLokaal  = [{ key: 'duru_2627_natuurkunde_v1', val: { xp: 95, streak: 1, badges: { a:1 }, beste: { t1: 40 }, pogingen: { t1: 1 } } }];
let push = merge(rijkeCloud.concat(armLokaal))['duru_2627_natuurkunde_v1'];
ok('push: XP krimpt niet',       push.xp, 865);
ok('push: madalya krimpt niet',  Object.keys(push.badges).length, 5);
ok('push: pogingen krimpt niet', push.pogingen.t1, 7);

/* ── 7) merger is puur: schrijft niet naar localStorage ── */
const voor = JSON.stringify(store);
merge(rijkeCloud);
ok('merge() localStorage-a dokunmuyor', JSON.stringify(store), voor);

/* ── 8) history: cloud 48, lokaal 1 -> 48 blijft ── */
const h48 = { history: Array.from({ length: 48 }, (_, i) => ({ attemptId: 'att_' + (i + 1), examId: 'ex-' + i, pct: 70, datum: '01-09-2026 10:00' })) };
const h1  = { history: [{ attemptId: 'att_1', examId: 'ex-0', pct: 70, datum: '01-09-2026 10:00' }] };
let ph = merge([{ key: 'duru_2627_natuurkunde_examens_v1', val: h48 },
                { key: 'duru_2627_natuurkunde_examens_v1', val: h1 }])['duru_2627_natuurkunde_examens_v1'];
ok('push: 48 poging korunuyor', ph.history.length, 48);

console.log(fail === 0 ? '\nTUM TESTLER GECTI' : '\n' + fail + ' TEST BASARISIZ');
process.exit(fail ? 1 : 0);
