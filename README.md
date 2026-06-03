# Duru's School

Een centrale hub die Duru's oefensites (MAVO 2) samenvoegt op één plek, met één link.

## Vakken

| Vak | Map | Inhoud | Type |
|-----|-----|--------|------|
| Natuurkunde (NASK) | `nask/` | Hoofdstuk 4 (Snelheid) & 6 (Elektriciteit) | git submodule |
| Wiskunde | `wiskunde/` | Hoofdstuk 8 — Vergelijkingen (8.1–8.4) | map in deze repo |
| Economie | `economi/` | Hoofdstuk 6 (De overheid) | git submodule |
| Nederlands — Begrijpend Lezen | `nederlands/begrijpend-lezen/` | Leesteksten & vragen (Meester Max) | git submodule |

Drie sites zijn zelfstandige repo's die als **git submodule** zijn opgenomen (de bronrepo's blijven de bron van waarheid). **Wiskunde** is geen aparte repo maar een gewone map in deze hub.

## Lokaal starten

Dubbelklik op **`Duru_Okul_Baslat.command`** — de site opent vanzelf op `http://localhost:8125/`.

Of handmatig via de terminal:

```bash
cd /pad/naar/Duru_Okul
git submodule update --init --recursive
python3 -m http.server 8125
```

Open dan `http://localhost:8125/` in je browser.

**Vanaf je telefoon** (zelfde wifi, terwijl de Mac draait): ga naar `http://<mac-ip>:8125/` — vind het ip met `ipconfig getifaddr en0`.

## Navigeren

- Klik op een vak → de oefensite opent binnen de hub.
- **Terug naar het overzicht** kan altijd via de knop **"← Terug naar de vakken"** bovenaan, de **Escape**-toets, of de **terugknop** van je browser.
- **Nederlands** is een categorie: klik erop om de onderwerpen (o.a. Begrijpend Lezen) uit te klappen.

## Content bijwerken

Dubbelklik op **`Guncelle.command`** — haalt de nieuwste inhoud van de submodule-sites op en pusht een backup. Of handmatig:

```bash
git submodule update --remote --merge
git add -A
git commit -m "Submodules bijgewerkt naar nieuwste versie"
git push
```

## Hosting

Dit project draait **lokaal / op het thuisnetwerk**. De GitHub-repo (`Mesut-Outlook/duru_okul`) dient **alleen als backup** — er is bewust géén GitHub Pages.
