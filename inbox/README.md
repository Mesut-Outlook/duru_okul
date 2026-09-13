# Inbox — Lesmateriaal inleveren

Plaats hier je schoolmateriaal (PDF, Word of foto's van lesboeken/aantekeningen). Wij lezen het materiaal en maken er oefenmateriaal en proeftoetsen van!

## ⚠️ Auteursrechtelijk materiaal

PDF's van schoolboeken zijn **auteursrechtelijk beschermd**. `.gitignore` sluit `inbox/**/*.pdf`
(en `havo3/*/pdf/`) uit van git — ze komen **nooit** in de repository terecht en worden **nooit**
gepubliceerd via GitHub Pages. Ze blijven alleen lokaal op schijf. Het ruwe, ongesorteerde archief
van alle schoolboeken staat in `~/Downloads/Eğitim/Duru/` (alleen-lezen bronmateriaal, niet
onder git-beheer) — de bestanden hier in `inbox/<schooljaar>/<vak>/` zijn de **schoongemaakte,
kanoniek benoemde** kopieën die klaar zijn voor verwerking.

## Waar plaats je je bestanden?

Zet je bestand in de juiste map voor het **schooljaar** en het **vak**:

```
inbox/<schooljaar>/<vak>/
```

### Voorbeelden:
- **Geschiedenis (HAVO 3)**: `inbox/2026-2027/geschiedenis/`
- **Wiskunde (HAVO 3)**: `inbox/2026-2027/wiskunde/`
- **Economie (MAVO 2 - archief)**: `inbox/2025-2026/economi/`

## Kanonieke bestandsnaam (verplicht)

Eén vaste vorm, zodat elk bestand op zichzelf zegt welk hoofdstuk het dekt:

```
<vak>_h<NN>_<slug>.pdf
```

- `<vak>` — de sitemap-slug (`natuurkunde`, `scheikunde`, `wiskunde`, `biologie`, `economie`, …).
- `<NN>` — het hoofdstuknummer **zoals het in de site staat**
  (`havo3/<vak>/js/bootstrap.js` → `DURU.hoofdstukken`, veld `nr`) — eerst opzoeken, niet raden.
- `<slug>` — kleine letters, ASCII, woorden gescheiden door `-` (bijv. `kracht-en-beweging`).

Varianten:
- **Geen hoofdstuk (extra materiaal)**: `<vak>_extra_<slug>.pdf`
- **Werkboek**: `<vak>_h<NN>-werkboek_<slug>.pdf`
- **Paragraaf-subset** van een hoofdstuk: nummers in de slug, bijv.
  `biologie_h10_je-verandert-10-1-10-2.pdf` (§10.1–10.2).

### OCR-bronnen
Een OCR-tekstbestand hoort **naast** zijn PDF, met dezelfde stam:
```
<vak>_h<NN>_<slug>.ocr.txt
```
(bijv. `geschiedenis_h02_tussen-de-oorlogen.ocr.txt` naast een gelijknamige PDF, of los als de
PDF zelf niet in de inbox staat). Tussentijdse render-artefacten (pagina-PNG's, ruwe per-pagina
tekst) horen in een `_render/` submap van het vak (bijv. `inbox/2026-2027/wiskunde/_render/`) —
die staat in `.gitignore`, want het is wegwerp-tussenmateriaal, geen brondocument.

## Ondersteunde bestandsformaten
- 📄 **PDF-bestanden** (bijv. digitale hoofdstukken of samenvattingen)
- 📝 **Word-documenten** (`.docx` of `.doc`)
- 📸 **Afbeeldingen & Foto's** (`.jpg`, `.png` - duidelijke foto's van je boek of aantekeningen)

## Hoe het werkt
1. **Plaats het bestand** in de juiste vak-map, met de kanonieke naam hierboven.
2. **Verwerking**: het materiaal wordt geanalyseerd en omgezet in oefenmateriaal/proeftoetsen
   volgens `../docs/PIPELINE.md`.
3. **`PDF_INDEX.md`**: `inbox/2026-2027/PDF_INDEX.md` is een gegenereerd overzicht van alle
   PDF's in dit schooljaar (output van `tools/pdf_check.py --index`) — niet handmatig bewerken,
   opnieuw genereren na wijzigingen.

---
*Zie `../docs/PIPELINE.md` voor technische details over het verwerkingsproces.*
