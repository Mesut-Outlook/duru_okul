# CLAUDE.md — Duru_Okul

Hub die Duru's oefensites (MAVO 2) samenvoegt onder één link. **Pure static, geen build, geen ES-modules** (werkt op `file://` / `http.server`). **Self-contained**: alle sites zitten als gewone mappen in deze ene repo — geen submodules (vroeger wel; sinds 2026-06-03 ingebed).

## Structuur
```
index.html        landing (iframe-shell & dashboard container)
css/style.css     vak-kleuren: blauw/groen/oranje/teal + dashboard styles
js/landing.js     VAKKEN-array + render + iframe-shell + storage-interceptor
js/dashboard.js   statistieken dashboard logica + SVG charts + examens log
nask/             DURU-engine, natuurkunde (H4 Snelheid & H6 Elektriciteit)
economi/          DURU-engine, economie (H6 De overheid)
nederlands/begrijpend-lezen/   "Meester Max"-engine (begrijpend lezen)
nederlands/spelling/           DURU-engine, Spelling & Grammatica
wiskunde/         DURU-engine, H8 Vergelijkingen
geschiedenis/     DURU-engine, geschiedenis (WO I & II)
Duru_Okul_Baslat.command   start server (poort 8125)
```
Elke vak-map is een zelfstandige site (eigen `index.html`, `js/`, `css/`). Bewerk ze gewoon hier.

## Dashboard & Statistieken
Het dashboard is in `index.html` geïntegreerd via twee views ("Mijn vakken" en "Mijn prestaties & statistieken"). De logica in `js/dashboard.js` leest de localStorage uit en aggregeert data over alle vakken. Opbouw van de statistieken-view (sinds 2026-06-15 herontworpen, **vak/onderwerp-gericht**):
1. **Samenvattingsstrip** — 4 hero-kaarten: ⚡ XP · 🏆 badges · 📝 gemaakte proeftoetsen · 🎯 gemiddeld cijfer.
2. **Per-vak kaarten** (`#vak-stats-grid`, `renderVakKaarten()`) — per vak in één oogopslag: gemiddeld + hoogste cijfer, 🧪 aantal proeftoetsen, 🔁 aantal keer geoefend, 📚 aantal onderwerpen. Een **"Details ▾"**-knop (gedelegeerde click-listener) klapt een drill-down open: proeftoetsen gegroepeerd per `examId` (titel · aantal keer · beste/laatste cijfer · datum) + oefenen per onderwerp (titel · aantal keer · beste score %).
3. **Score verloop** — responsive SVG-lijnchart (`renderScoreTimeline`, laatste 15 pogingen, tooltips).
4. **Volledig logboek** — doorzoekbare/filterbare tabel met alle pogingen (`renderAttemptsTable`).

`renderVakKaarten` leest per vak de oefen-sleutel (`pogingen{}`/`titels{}`/`beste{}`) + de examen-sleutel (`history` per `examId`). Begrijpend Lezen heeft geen oefen-data → toont alleen examen-achtige geschiedenis. Cijfer = `1 + pct/100*9` (geslaagd ≥ 5,5). **Let op cache-versie**: bij CSS/JS-wijzigingen `style.css?v=` in `index.html` bumpen (nu `v=2.4`).

**Proeftoetskaarten Status**: De selectiekaarten van de proeftoetsen tonen direct of een examen al is gemaakt (`✓ Gemaakt` / `Nog niet gemaakt`) en laten zowel het beste (`🏆 Beste cijfer`) als het meest recente cijfer (`⏱️ Laatste cijfer`) zien.


## DURU-engine sites (nask / economi / wiskunde / spelling / geschiedenis)
Zelfde motor: `bootstrap.js` (register/registerExamen) → `engine.js` (oefenen) → `exams.js` (proeftoets). Data in `<vak>/js/data/*.js`; contract in `<vak>/SPEC.md`. **localStorage-sleutels zijn per site uniek** (`duru_nask_*`, `duru_economi_*`, `duru_wiskunde_*`, `duru_nederlands_spelling_*`, `duru_geschiedenis_*`, en begrijpend lezen `begrijpend_lezen_history`) — niet door elkaar halen. Het oefen-voortgangsobject (`duru_<vak>_v1`) bevat `{ xp, streak, badges{}, beste{id:pct}, gedaan{}, pogingen{id:count}, titels{id:titel} }` — `pogingen`/`titels` worden in `engine.js`'s `renderResultaat()` bijgewerkt en voeden de per-vak dashboard-kaarten (gebruik altijd `|| {}`-guards; oude data mist deze velden).

**Per-vak dashboard (in elke DURU-site zelf)**: elke engine heeft een route `dashboard` (`DURU.gaNaar('dashboard')`, knop "📊 Mijn dashboard" in de hero van `renderHome`) → `renderDashboard()` toont een vak-eigen dashboard: samenvatting (gemiddeld/hoogste cijfer, aantal proeftoetsen, keer geoefend, onderwerpen geoefend) + oefenen-per-onderwerp tabel + proeftoetsen gegroepeerd per `examId`. Leest oefen-data uit `P` (+ `DURU.onderwerpen` voor alle titels) en examen-data uit de afgeleide sleutel `SLEUTEL.replace(/_v1$/,"_examens_v1")`. Hergebruikt bestaande klassen (`.topic-card`, `.nask`, `.mini-progress`, `.sectie-titel`) → erft automatisch het licht/donker-thema van de site. Begrijpend Lezen (aparte engine) heeft een eigen dashboard-achtige "Resultatenhistorie" met samenvattingskaarten in `renderHistorySection()` (`app.js`). Script-volgorde in elke `index.html`: bootstrap → exams → data/examen_* → data/h*_* / sp_* → engine.js (laatst). Begrijpend-lezen is een aparte engine (`app.js` + `questions.js`).

## Vak toevoegen
Voeg een entry toe aan `VAKKEN` in `js/landing.js`:
```js
{ id:'wiskunde', titel:'Wiskunde', icoon:'⚖️', kleur:'teal',
  beschrijving:'…', href:'./wiskunde/' }   // categorie = geen href maar onderwerpen:[…]
```
Links altijd **relatief** (`./wiskunde/` …). Een nieuwe `kleur` heeft bijbehorende CSS-vars + `.vak-kaart--<kleur>`/`.vak-badge--<kleur>` nodig (zie `teal`). Navigatie werkt automatisch mee.

## Navigatie (iframe-shell)
Een vak opent in `#vak-frame` met een vaste "← Terug naar de vakken"-balk. Terug = knop / Escape / browser-back (`history.pushState` + `popstate`). iframe-`src` is `about:blank` als gesloten (nooit lege `src=""`, dat herlaadt de hub). Logica in `js/landing.js`.

## Storage & SVG Iframe Bugfixes (Crucial)
1. **Storage Interception**: In `js/landing.js` wordt `win.Storage.prototype.setItem` overschreven om resultaten van `duru_*` te synchroniseren met de lokale python server (`POST /api/score`). Het overschrijven gebeurt op het prototype niveau met een `try-catch` wrapper om `Illegal invocation` type errors (met name in Safari/Chrome) te voorkomen.
2. **SVG Ring Render**: Vanwege weergave-fouten met SVG `<linearGradient>` (`url(#g2)`) binnen iframes in Safari, gebruiken alle voortgangscirkels in `engine.js` en `exams.js` een solide themakleur (`stroke="var(--paars)"`) in plaats van ID-referenties.

## Draaien & hosting
`open Duru_Okul_Baslat.command` (of `python3 -m http.server 8125`) → `http://localhost:8125/`. Thuisnetwerk: `http://<mac-ip>:8125/`. UFW firewall openen via `sudo ufw allow 8125/tcp`.

**Lokaal-only — geen GitHub Pages** (op verzoek). De GitHub-repo `git@github.com:Mesut-Outlook/duru_okul.git` is **alleen backup** (`git push origin main`). Pages niet toevoegen tenzij gevraagd.

## Werkwijze
Conventie (zoals de oude zustersites): **planning met Opus 4.8, code door Sonnet sub-agents**; commit-trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. Git lokaal: `user.name=Mesut-Outlook`, `user.email=ozdemirmesut@gmail.com`.
