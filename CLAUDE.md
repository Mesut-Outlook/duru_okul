# CLAUDE.md — Duru_Okul

Hub die Duru's oefensites (MAVO 2) samenvoegt onder één link. **Pure static, geen build, geen ES-modules** (werkt op `file://` / `http.server`). **Self-contained**: alle sites zitten als gewone mappen in deze ene repo — geen submodules (vroeger wel; sinds 2026-06-03 ingebed).

## Structuur
```
index.html        landing (iframe-shell)
css/style.css     vak-kleuren: blauw/groen/oranje/teal
js/landing.js     VAKKEN-array + render + iframe-shell
nask/             DURU-engine, natuurkunde (H4 Snelheid & H6 Elektriciteit)
economi/          DURU-engine, economie (H6 De overheid)
nederlands/begrijpend-lezen/   "Meester Max"-engine (begrijpend lezen)
wiskunde/         DURU-engine, H8 Vergelijkingen
Duru_Okul_Baslat.command   start server (poort 8125)
```
Elke vak-map is een zelfstandige site (eigen `index.html`, `js/`, `css/`). Bewerk ze gewoon hier.

## DURU-engine sites (nask / economi / wiskunde)
Zelfde motor: `bootstrap.js` (register/registerExamen) → `engine.js` (oefenen) → `exams.js` (proeftoets). Data in `<vak>/js/data/*.js`; contract in `<vak>/SPEC.md`. **localStorage-sleutels zijn per site uniek** (`duru_nask_*`, `duru_economi_*`, `duru_wiskunde_*`) — niet door elkaar halen. Script-volgorde in elke `index.html`: bootstrap → exams → data/examen_* → data/h*_* → engine.js (laatst). Begrijpend-lezen is een aparte engine (`app.js` + `questions.js`).

## Vak toevoegen
Voeg een entry toe aan `VAKKEN` in `js/landing.js`:
```js
{ id:'wiskunde', titel:'Wiskunde', icoon:'⚖️', kleur:'teal',
  beschrijving:'…', href:'./wiskunde/' }   // categorie = geen href maar onderwerpen:[…]
```
Links altijd **relatief** (`./wiskunde/` …). Een nieuwe `kleur` heeft bijbehorende CSS-vars + `.vak-kaart--<kleur>`/`.vak-badge--<kleur>` nodig (zie `teal`). Navigatie werkt automatisch mee.

## Navigatie (iframe-shell)
Een vak opent in `#vak-frame` met een vaste "← Terug naar de vakken"-balk. Terug = knop / Escape / browser-back (`history.pushState` + `popstate`). iframe-`src` is `about:blank` als gesloten (nooit lege `src=""`, dat herlaadt de hub). Logica in `js/landing.js`.

## Draaien & hosting
`open Duru_Okul_Baslat.command` (of `python3 -m http.server 8125`) → `http://localhost:8125/`. Thuisnetwerk: `http://<mac-ip>:8125/` (`ipconfig getifaddr en0`).

**Lokaal-only — geen GitHub Pages** (op verzoek). De GitHub-repo `git@github.com:Mesut-Outlook/duru_okul.git` is **alleen backup** (`git push origin main`). Pages niet toevoegen tenzij gevraagd.

## Werkwijze
Conventie (zoals de oude zustersites): **planning met Opus 4.8, code door Sonnet sub-agents**; commit-trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. Git lokaal: `user.name=Mesut-Outlook`, `user.email=ozdemirmesut@gmail.com`.
