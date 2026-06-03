# CLAUDE.md — Duru_Okul

Hub die Duru's oefensites (MAVO 2) samenvoegt. **Pure static, geen build, geen ES-modules** (werkt op `file://` / `http.server`).

## Structuur
```
index.html        landing (iframe-shell)
css/style.css     vak-kleuren: blauw/groen/oranje/teal
js/landing.js     VAKKEN-array + render + iframe-shell
nask/             submodule duru_nask        (DURU-engine, natuurkunde, H4 & H6)
economi/          submodule duru_economi     (DURU-engine, economie, H6)
nederlands/begrijpend-lezen/  submodule duru_begrijpen_lezen ("Meester Max")
wiskunde/         GEEN submodule — gewone map (DURU-engine, H8 Vergelijkingen)
Duru_Okul_Baslat.command   start server (poort 8125)
Guncelle.command           werkt submodules bij + pusht backup
```

Submodule-repo's: `github.com/Mesut-Outlook/duru_{nask,economi,begrijpen_lezen}`.
**Wijzig nooit bestanden in submodule-mappen via deze repo** — commit in de bronrepo, update daarna de pointer.

## Wiskunde (in-repo, wél hier bewerken)
Eigen DURU-engine-site, **Hoofdstuk 8** (8.1 gelijksoortige termen · 8.2 de balans · 8.3 vergelijkingen oplossen · 8.4 het snijpunt). Thema teal. localStorage `duru_wiskunde_v1` + `duru_wiskunde_examens_v1` (apart van de andere sites). Data: `wiskunde/js/data/h8_*.js` + `examen_*.js`; contract in `wiskunde/SPEC.md`. Script-volgorde in `wiskunde/index.html`: bootstrap → exams → data/examen_* → data/h8_* → engine.js (laatst).

## Vak toevoegen
Voeg een entry toe aan `VAKKEN` in `js/landing.js`:
```js
{ id:'wiskunde', titel:'Wiskunde', icoon:'⚖️', kleur:'teal',
  beschrijving:'…', href:'./wiskunde/' }   // categorie = geen href maar onderwerpen:[…]
```
Links altijd **relatief** (`./wiskunde/` …). Een nieuwe `kleur` heeft bijbehorende CSS-vars + `.vak-kaart--<kleur>`/`.vak-badge--<kleur>` nodig (zie `teal`). Navigatie werkt automatisch mee (zie hieronder).

## Navigatie (iframe-shell)
Een vak opent in `#vak-frame` met een vaste "← Terug naar de vakken"-balk, zodat sub-sites onaangeroerd blijven. Terug = knop / Escape / browser-back (`history.pushState` + `popstate`). iframe-`src` is `about:blank` als gesloten (nooit lege `src=""`, dat herlaadt de hub). Alle logica in `js/landing.js`.

## Draaien & bijwerken
```bash
open Duru_Okul_Baslat.command          # of: python3 -m http.server 8125
git submodule update --remote --merge  # nieuwste content uit bronrepo's (of: Guncelle.command)
```
Lokaal: `http://localhost:8125/` · thuisnetwerk: `http://<mac-ip>:8125/` (`ipconfig getifaddr en0`).

## Hosting & werkwijze
**Lokaal-only — geen GitHub Pages** (op verzoek). De GitHub-repo is **alleen backup** (`git push origin main`). Pages niet opnieuw toevoegen tenzij gevraagd.

Conventie (zoals Duru_Nask/Duru_Economi): **planning met Opus 4.8, code door Sonnet sub-agents**; commit-trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

Git lokaal: `user.name=Mesut-Outlook`, `user.email=ozdemirmesut@gmail.com`, `remote=git@github.com:Mesut-Outlook/duru_okul.git`.
