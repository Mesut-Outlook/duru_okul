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
├── css/style.css            ← landing styles (niet aanpassen zonder overleg)
├── js/landing.js            ← landing logic + VAKKEN-array (zie hieronder)
├── nask/                    ← submodule: duru_nask (DURU-engine, natuurkunde)
├── economi/                 ← submodule: duru_economi (DURU-engine, economie)
├── nederlands/
│   └── begrijpend-lezen/    ← submodule: duru_begrijpen_lezen ("Meester Max"-engine)
├── .github/workflows/pages.yml
├── .gitignore
├── README.md
├── CLAUDE.md
└── Duru_Okul_Baslat.command
```

## Submodules

| Pad | GitHub-repo | Engine / beschrijving |
|-----|-------------|----------------------|
| `nask/` | https://github.com/Mesut-Outlook/duru_nask | DURU-engine — hoofdstuk 4 (Snelheid) & 6 (Elektriciteit), theorie + quiz + proeftoets |
| `economi/` | https://github.com/Mesut-Outlook/duru_economi | DURU-engine — hoofdstuk 6 (De overheid), theorie + quiz + proeftoets |
| `nederlands/begrijpend-lezen/` | https://github.com/Mesut-Outlook/duru_begrijpen_lezen | "Meester Max"-engine — begrijpend lezen, leesteksten & vragen |

Wijzig NOOIT bestanden binnen de submodule-mappen via deze repo. Commit altijd via de bronrepo en update daarna de submodule-pointer hier.

## Vakken toevoegen of aanpassen

De landing wordt aangestuurd door de `VAKKEN`-array in `js/landing.js`. Om een nieuw vak of onderwerp toe te voegen, pas die array aan:

```js
// Voorbeeld entry in VAKKEN
{
  id: "wiskunde",
  label: "Wiskunde",
  icon: "📐",
  path: "./wiskunde/",      // relatief pad — werkt zowel lokaal als onder /duru_okul/
  description: "Oefeningen rekenen en algebra"
}
```

Links zijn altijd **relatief** (`./nask/`, `./economi/`, `./nederlands/begrijpend-lezen/`) zodat ze correct werken zowel lokaal (`http://localhost:8125/`) als op GitHub Pages (`https://mesut-outlook.github.io/duru_okul/`).

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

## Deploy (GitHub Pages)

Workflow: `.github/workflows/pages.yml`
- Trigger: push naar `main` of handmatig via Actions
- Checkout met `submodules: recursive` en `fetch-depth: 0`
- Publiceert de volledige repo-root as-is (geen build)
- URL: https://mesut-outlook.github.io/duru_okul/

**Vereiste GitHub-instelling:** Ga naar repo Settings → Pages → Source: stel in op "GitHub Actions".

## Werkwijze / Convention

**"Planning met Opus 4.8, alle code geschreven door Sonnet sub-agents"**

Zoals bij de zustersites Duru_Nask en Duru_Economi: architectuurbeslissingen en taakplanning worden gedaan door het Opus-model; de daadwerkelijke code wordt geschreven door Sonnet sub-agents. Vermeld dit in commit-trailers als `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

## Git-configuratie (lokaal)

```
user.name  = Mesut-Outlook
user.email = ozdemirmesut@gmail.com
remote     = git@github.com:Mesut-Outlook/duru_okul.git
```
