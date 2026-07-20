# Duru's Wiskunde Academie — Hoofdstuk 8: Vergelijkingen

Statische oefensite voor Duru (MAVO 2, wiskunde). Geen build, geen framework — puur HTML, CSS en JavaScript.

## Inhoud

**Hoofdstuk 8 — Vergelijkingen** (4 onderwerpen):
- **8.1** Gelijksoortige termen
- **8.2** De balans
- **8.3** Vergelijkingen oplossen
- **8.4** Het snijpunt

Plus 2 proeftoetsen op tijd, met cijfer en nakijkfunctie.

## Opstarten

```bash
# Via de hub (aanbevolen):
open /Users/mesutozdemir/Duru_Okul/index.html

# Of rechtstreeks via een eenvoudige server (poort 8125):
cd /Users/mesutozdemir/Duru_Okul/wiskunde
python3 -m http.server 8125
# Open daarna: http://localhost:8125
```

> **Let op:** de site werkt ook direct via `file://` in de browser (geen CORS-problemen omdat er geen ES modules worden gebruikt).

## Bestandsstructuur

```
wiskunde/
├── index.html          ← shell + script-laadvolgorde
├── css/
│   └── style.css       ← design system (teal/turquoise thema)
├── js/
│   ├── bootstrap.js    ← DURU-object + register/registerExamen
│   ├── engine.js       ← oefen-quiz, XP, badges, routing
│   ├── exams.js        ← proeftoets-modus, timer, cijfer, nakijken
│   └── data/           ← inhoud (gegenereerd door content-agents)
│       ├── examen_1_gemengd.js
│       ├── examen_2_vergelijkingen.js
│       ├── h8_1_gelijksoortige_termen.js
│       ├── h8_2_de_balans.js
│       ├── h8_3_vergelijkingen_oplossen.js
│       └── h8_4_het_snijpunt.js
├── SPEC.md             ← datacontract voor content-agents
└── README.md           ← dit bestand
```

## Technische details

- **localStorage-sleutels**: `duru_wiskunde_v1` (oefen-XP) en `duru_wiskunde_examens_v1` (toetscijfers) — apart van de NASK- en Economie-sites.
- **Themakleur**: teal/turquoise (`#0d9488` / `#14b8a6`).
- Geen externe afhankelijkheden behalve Google Fonts (Baloo 2).
- Vraagtypen: `mc`, `waaronwaar`, `invoer` (oefen); `mc`, `waaronwaar`, `invul`, `open` (examen).
