# CLAUDE.md — Duru_Okul

Guidance voor toekomstige Claude Code-sessies op deze repo.

## Wat is dit project?

**Duru's School** is een pure-statische, buildloze landing hub die drie oefensites voor Duru (MAVO 2) samenvoegt. Er is geen bundler, geen ES-modules (`type="module"` wordt NIET gebruikt), en er is geen server nodig voor productie — alles draait via `file://` of een eenvoudige `http.server`.

- Geen build-stap
- Geen npm/node_modules in deze root
- Geen ES-module-imports over bestanden heen (CORS-beperking op `file://`)

## Architectuur

```
Duru_Okul/
├── index.html               ← landing page (niet aanpassen zonder overleg)
├── css/style.css            ← landing styles (vak-kleuren: blauw/groen/oranje/teal)
├── js/landing.js            ← landing logic + VAKKEN-array (zie hieronder)
├── nask/                    ← submodule: duru_nask (DURU-engine, natuurkunde)
├── economi/                 ← submodule: duru_economi (DURU-engine, economie)
├── nederlands/
│   └── begrijpend-lezen/    ← submodule: duru_begrijpen_lezen ("Meester Max"-engine)
├── wiskunde/                ← GEEN submodule — gewone map in deze repo (DURU-engine, H8)
├── .gitignore
├── README.md
├── CLAUDE.md
├── Duru_Okul_Baslat.command ← start lokale server (poort 8125)
└── Guncelle.command         ← werkt submodule-content bij + pusht backup
```

## Submodules

| Pad | GitHub-repo | Engine / beschrijving |
|-----|-------------|----------------------|
| `nask/` | https://github.com/Mesut-Outlook/duru_nask | DURU-engine — hoofdstuk 4 (Snelheid) & 6 (Elektriciteit), theorie + quiz + proeftoets |
| `economi/` | https://github.com/Mesut-Outlook/duru_economi | DURU-engine — hoofdstuk 6 (De overheid), theorie + quiz + proeftoets |
| `nederlands/begrijpend-lezen/` | https://github.com/Mesut-Outlook/duru_begrijpen_lezen | "Meester Max"-engine — begrijpend lezen, leesteksten & vragen |

Wijzig NOOIT bestanden binnen de submodule-mappen via deze repo. Commit altijd via de bronrepo en update daarna de submodule-pointer hier.

### Wiskunde — GEEN submodule
`wiskunde/` is **geen submodule** maar een gewone map binnen deze repo (op verzoek: geen aparte GitHub-repo aanmaken). Het is een eigen DURU-engine-site (zoals NASK/Economie) over **Hoofdstuk 8 — Vergelijkingen** (8.1 Gelijksoortige termen · 8.2 De balans · 8.3 Vergelijkingen oplossen · 8.4 Het snijpunt). Bewerk deze map dus gewoon hier in `Duru_Okul`.

- Engine geadapteerd van `nask/`; thema-accent = **teal** (`#0d9488`).
- localStorage-sleutels: `duru_wiskunde_v1` (oefenen) + `duru_wiskunde_examens_v1` (proeftoetsen) — APART van nask/economi.
- Data: `wiskunde/js/data/h8_*.js` (4 onderwerpen) + `examen_*.js` (2 proeftoetsen); contract in `wiskunde/SPEC.md`.
- Script-volgorde in `wiskunde/index.html`: bootstrap → exams → data/examen_* → data/h8_* → engine.js (laatst). Niet breken.
- Bron: gescande `Duru Matematik 8.1 to 8.4.pdf` (iCloud `2. DURU DERSLER/MATEMATIK`), via PyMuPDF naar PNG gerenderd en visueel gelezen (`_math_extract/`, staat in `.gitignore`).

## Vakken toevoegen of aanpassen

De landing wordt aangestuurd door de `VAKKEN`-array in `js/landing.js`. Om een nieuw vak of onderwerp toe te voegen, pas die array aan:

```js
// Echte velden van een direct-vak in VAKKEN (zie js/landing.js):
{
  id: 'wiskunde',
  titel: 'Wiskunde',
  icoon: '⚖️',
  kleur: 'teal',            // moet matchen met een kleur in css/style.css
  beschrijving: 'Hoofdstuk 8 — Vergelijkingen: termen, de balans en het snijpunt.',
  href: './wiskunde/'       // relatief pad
}
// Een categorie-vak (zoals Nederlands) heeft GEEN href maar een `onderwerpen: [...]`-array.
```

Een nieuwe `kleur` vereist bijbehorende CSS-variabelen + `.vak-kaart--<kleur>` / `.vak-badge--<kleur>` regels in `css/style.css` (zie hoe `teal` is toegevoegd).

Links zijn altijd **relatief** (`./nask/`, `./wiskunde/`, `./economi/`, `./nederlands/begrijpend-lezen/`) zodat ze zowel lokaal (`http://localhost:8125/`) als vanaf het LAN (`http://<mac-ip>:8125/`) werken.

## Submodules bijwerken

```bash
git submodule update --remote --merge   # haal nieuwste commits op uit bronrepo's
git add nask economi nederlands/begrijpend-lezen
git commit -m "Submodules bijgewerkt naar nieuwste versie"
git push
```

## Lokaal draaien

Port: **8125**

```bash
# Via launcher (aanbevolen):
open Duru_Okul_Baslat.command

# Of handmatig:
git submodule update --init --recursive
python3 -m http.server 8125
# Ga naar http://localhost:8125/
```

## Hosting — LOKAAL, geen GitHub Pages

Op verzoek van de gebruiker (2026-06-03): **GitHub Pages is NIET gewenst.** Het project draait lokaal / op het thuisnetwerk; de GitHub-repo dient **alleen als backup**. De `.github/workflows/pages.yml` is verwijderd (faalde op cross-repo submodule-fetch én Pages was ongewenst). **Voeg Pages niet opnieuw toe tenzij erom gevraagd wordt.**

- Lokaal: `Duru_Okul_Baslat.command` → `http://localhost:8125/`
- Thuisnetwerk (bv. Duru's telefoon, zelfde wifi): `http://<mac-LAN-ip>:8125/` (vind ip met `ipconfig getifaddr en0`)
- Backup pushen: gewoon `git push origin main` (repo is public, alleen als backup).

## Werkwijze / Convention

**"Planning met Opus 4.8, alle code geschreven door Sonnet sub-agents"**

Zoals bij de zustersites Duru_Nask en Duru_Economi: architectuurbeslissingen en taakplanning worden gedaan door het Opus-model; de daadwerkelijke code wordt geschreven door Sonnet sub-agents. Vermeld dit in commit-trailers als `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

## Git-configuratie (lokaal)

```
user.name  = Mesut-Outlook
user.email = ozdemirmesut@gmail.com
remote     = git@github.com:Mesut-Outlook/duru_okul.git
```
