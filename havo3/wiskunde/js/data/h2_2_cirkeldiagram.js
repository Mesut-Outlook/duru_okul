/* =========================================================
   Duru's Wiskunde (HAVO 3) — Cirkeldiagrammen & Middelpuntshoeken
   ========================================================= */
DURU.register({
  "id": "h2-2-cirkeldiagram",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Cirkeldiagrammen & Middelpuntshoeken",
  "korteUitleg": "Omrekenen van absolute aantallen en percentages naar sectorhoeken in graden (360°).",
  "icoon": "🥧",
  "kleur": "blauw",
  "theorie": "<h3>2.2 Cirkeldiagrammen & Middelpuntshoeken</h3>\n<p>Een <b>cirkeldiagram (taartdiagram)</b> is een visuele weergave van gegevens waarbij een totale verzameling wordt verdeeld in verschillende taartpunten (sectoren). Een cirkeldiagram is vooral geschikt om te laten zien hoe een <b>totaal (100%)</b> is opgebouwd uit verschillende delen.</p>\n<h4>De basisregels van een cirkel</h4>\n<ul>\n  <li>Een volledige cirkel is altijd gelijk aan <b>360 graden (360°)</b>.</li>\n  <li>Een volledige cirkel komt overeen met <b>100%</b> van het totaal.</li>\n  <li>Hieruit volgt dat <b>1%</b> in een cirkeldiagram exact overeenkomt met: <code>360° / 100 = 3,6°</code>.</li>\n</ul>\n<h4>Omrekenformules voor sectorhoeken</h4>\n<div class=\"formule-box\">\n  <b>Van percentage naar sectorhoek (middelpuntshoek):</b><br>\n  <code>Sectorhoek in graden = Percentage × 3,6°</code><br><br>\n  <b>Van aantal (frequentie) naar sectorhoek:</b><br>\n  <code>Sectorhoek in graden = (Deel / Totaal) × 360°</code><br><br>\n  <b>Van sectorhoek terug naar percentage:</b><br>\n  <code>Percentage = (Sectorhoek in graden / 360°) × 100%</code>\n</div>\n<h4>Stappenplan voor het tekenen van een cirkeldiagram</h4>\n<ol>\n  <li>Bereken eerst het totale aantal waarnemingen (de som van alle frequenties).</li>\n  <li>Bereken voor elke categorie de bijbehorende sectorhoek in graden met de formule <code>(aantal / totaal) × 360°</code>.</li>\n  <li>Controleer of de som van alle berekende hoeken samen precies <b>360°</b> is!</li>\n  <li>Teken een cirkel met een passer, trek een rechte startstraal naar boven (12 uur) en meet met je geodriehoek de hoeken nauwkeurig af.</li>\n  <li>Schrijf in of bij elke sector de categorienaam of het percentage en geef het diagram een duidelijke titel.</li>\n</ol>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Hoeveel graden is de sectorhoek van een categorie die 25% van het totaal beslaat?",
      "opties": [
        "90°",
        "60°",
        "45°",
        "120°"
      ],
      "antwoord": 0,
      "uitleg": "25 × 3,6° = 90° (of 0,25 × 360° = 90°)."
    },
    {
      "type": "mc",
      "vraag": "In een klas van 30 leerlingen hebben 6 leerlingen een hond. Hoe groot is de sectorhoek voor de categorie 'hond'?",
      "opties": [
        "36°",
        "72°",
        "60°",
        "90°"
      ],
      "antwoord": 1,
      "uitleg": "(6 / 30) × 360° = 0,20 × 360° = 72°."
    },
    {
      "type": "waaronwaar",
      "vraag": "Eén procent in een cirkeldiagram komt overeen met precies 3,6 graden.",
      "antwoord": true,
      "uitleg": "Waar: 360° / 100 = 3,6° per procent."
    },
    {
      "type": "invoer",
      "vraag": "Hoeveel graden is een halve cirkel (50%) in een cirkeldiagram?",
      "antwoord": "180|180 graden|180°",
      "uitleg": "50 × 3,6° = 180°."
    },
    {
      "type": "mc",
      "vraag": "Een sector heeft een middelpuntshoek van 54°. Welk percentage hoort hierbij?",
      "opties": [
        "10%",
        "20%",
        "15%",
        "25%"
      ],
      "antwoord": 2,
      "uitleg": "(54 / 360) × 100% = 0,15 × 100% = 15%."
    },
    {
      "type": "waaronwaar",
      "vraag": "De som van alle sectorhoeken in een cirkeldiagram mag maximaal 100 graden zijn.",
      "antwoord": false,
      "uitleg": "Onwaar: de som van alle hoeken in een cirkel is altijd exact 360 graden."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de sectorhoek in graden voor een percentage van 10%.",
      "antwoord": "36|36 graden|36°",
      "uitleg": "10 × 3,6° = 36°."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een cirkeldiagram is ideaal om te zien hoe een totaal van 100% is verdeeld.",
      "antwoord": true,
      "uitleg": "Waar: een cirkeldiagram toont de verhouding van de delen ten opzichte van het geheel."
    }
  ]
});
