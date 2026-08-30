/* =========================================================
   Duru's Wiskunde (HAVO 3) — Centrummaten: Gemiddelde, Mediaan & Modus
   ========================================================= */
DURU.register({
  "id": "h2-4-centrummaten",
  "hoofdstuk": 2,
  "paragraaf": "2.4",
  "titel": "Centrummaten: Gemiddelde, Mediaan & Modus",
  "korteUitleg": "Het rekenkundig gemiddelde, gewogen gemiddelde, de middelste waarneming (mediaan) en de modus.",
  "icoon": "🎯",
  "kleur": "blauw",
  "theorie": "<h3>2.4 Centrummaten: Gemiddelde, Mediaan & Modus</h3>\n<p>Een <b>centrummaat</b> is één enkel getal dat een samenvatting geeft van het 'midden' of de centrale ligging van een hele reeks waarnemingsgetallen. We onderscheiden drie belangrijke centrummaten:</p>\n<h4>1. Het Gemiddelde (Rekenkundig gemiddelde)</h4>\n<div class=\"formule-box\">\n  <code>Gemiddelde = Som van alle getallen / Totaal aantal waarnemingen</code><br>\n  Bij een frequentietabel bereken je het <b>gewogen gemiddelde</b>:<br>\n  <code>Gewogen gemiddelde = Som van (Waarde × Frequentie) / Totale frequentie</code>\n</div>\n<h4>2. De Mediaan (Het middelste getal)</h4>\n<p>De <b>mediaan</b> is het middelste getal wanneer alle waarnemingen op <b>volgorde van klein naar groot</b> zijn gezet:</p>\n<ul>\n  <li><b>Bij een ONEVEN aantal getallen (bijv. $n = 9$):</b> Er is één exact middelste getal op positie <code>(n + 1) / 2 = (9 + 1) / 2 = 5e getal</code>.</li>\n  <li><b>Bij een EVEN aantal getallen (bijv. $n = 10$):</b> Er zijn twee middelste getallen (het 5e en 6e getal). De mediaan is het <b>gemiddelde van die twee middelste getallen</b>: <code>(5e getal + 6e getal) / 2</code>.</li>\n</ul>\n<h4>3. De Modus (De meest voorkomende waarde)</h4>\n<p>De <b>modus</b> is het getal met de <b>hoogste frequentie</b> (het getal dat het allervaakst voorkomt):</p>\n<ul>\n  <li>Als twee waarden even vaak voorkomen en de hoogste frequentie delen, zijn er twee modi (of spreken we van bimodaal).</li>\n  <li>Komen alle getallen even vaak voor (bijv. allemaal 1 keer), dan is er <b>geen modus</b>.</li>\n</ul>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de mediaan van de getallenrij: 3, 5, 7, 8, 9, 11, 13?",
      "opties": [
        "8",
        "7",
        "9",
        "8,5"
      ],
      "antwoord": 0,
      "uitleg": "De 7 getallen staan op volgorde; het 4e getal (8) is precies het midden."
    },
    {
      "type": "mc",
      "vraag": "Wat is de modus van de getallenrij: 4, 6, 7, 7, 8, 9, 9, 9, 10?",
      "opties": [
        "7",
        "9",
        "8",
        "10"
      ],
      "antwoord": 1,
      "uitleg": "Het getal 9 komt 3 keer voor (vaker dan elk ander getal) en is dus de modus."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om de mediaan te bepalen, moeten de getallen altijd eerst op volgorde van klein naar groot worden gezet.",
      "antwoord": true,
      "uitleg": "Waar: zonder sorteren kun je de werkelijke mediaan niet vinden."
    },
    {
      "type": "invoer",
      "vraag": "Bereken het gemiddelde van de getallen: 6, 7, 8 en 11.",
      "antwoord": "8|8,0",
      "uitleg": "(6 + 7 + 8 + 11) / 4 = 32 / 4 = 8."
    },
    {
      "type": "mc",
      "vraag": "Wat is de mediaan van de getallen: 4, 6, 8, 12?",
      "opties": [
        "6",
        "8",
        "7",
        "7,5"
      ],
      "antwoord": 2,
      "uitleg": "Er zijn 4 getallen (even). De middelste zijn 6 en 8. Mediaan = (6 + 8) / 2 = 7."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het rekenkundig gemiddelde blijft gegarandeerd gelijk wanneer één enkele toetsscore in de klas plotseling verdubbelt.",
      "antwoord": false,
      "uitleg": "Niet waar: een extreme uitschieter (zoals een 1 of een 100) trekt het gemiddelde sterk omhoog of omlaag. De mediaan is daar juist wél ongevoelig voor."
    },
    {
      "type": "invoer",
      "vraag": "Welke centrummaat geeft de waarde aan die het vaakst voorkomt in een dataset?",
      "antwoord": "modus",
      "uitleg": "De modus is de meest voorkomende waarde."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een dataset kan meerdere modi hebben als twee getallen even vaak en het meest voorkomen.",
      "antwoord": true,
      "uitleg": "Waar: dan spreken we van een bimodale verdeling."
    }
  ]
});
