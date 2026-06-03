# Duru's School

Een centrale hub die drie oefensites voor Duru (MAVO 2) samenvoegt op één plek.

## Vakken

| Vak | Map | Site |
|-----|-----|------|
| Natuurkunde (NASK) | `nask/` | Hoofdstuk 4 (Snelheid) & 6 (Elektriciteit) |
| Economie | `economi/` | Hoofdstuk 6 (De overheid) |
| Nederlands — Begrijpend lezen | `nederlands/begrijpend-lezen/` | Leesteksten & vragen |

Elke site is een zelfstandige repo die als **git submodule** is opgenomen. De bronrepo's blijven de enige bron van waarheid; deze hub verwijst er alleen naar.

## Lokaal starten

Dubbelklik op `Duru_Okul_Baslat.command` — de site opent vanzelf op `http://localhost:8125/`.

Of handmatig via de terminal:

```bash
cd /pad/naar/Duru_Okul
git submodule update --init --recursive
python3 -m http.server 8125
```

Open dan `http://localhost:8125/` in je browser.

## Content bijwerken

Wanneer een van de bronsites nieuwe oefeningen of hoofdstukken heeft gekregen:

```bash
git submodule update --remote --merge
git add nask economi nederlands/begrijpend-lezen
git commit -m "Submodules bijgewerkt naar nieuwste versie"
git push
```

## GitHub Pages

Na aanmaken van de repo op GitHub wordt de hub automatisch gepubliceerd op:

**https://mesut-outlook.github.io/duru_okul/**

De workflow `.github/workflows/pages.yml` zorgt hiervoor bij elke push naar `main`.
