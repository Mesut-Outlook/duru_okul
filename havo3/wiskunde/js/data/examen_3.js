/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 3 — Centrummaten: Gemiddelde, Mediaan & Modus
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h2-3",
  "hoofdstuk": 2,
  "titel": "Proeftoets 3 — Centrummaten: Gemiddelde, Mediaan & Modus",
  "vak": "Wiskunde · H2 Statistiek",
  "icoon": "🎯",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de mediaan van de getallenrij: 2, 4, 7, 9, 12?",
      "opties": [
        "7",
        "4",
        "8",
        "9"
      ],
      "antwoord": 0,
      "uitleg": "De 5 getallen staan gesorteerd; het middelste getal is 7."
    },
    {
      "type": "mc",
      "vraag": "Wat is het gemiddelde van de cijfers: 6, 7, 8, 9, 10?",
      "opties": [
        "7",
        "8",
        "8,5",
        "9"
      ],
      "antwoord": 1,
      "uitleg": "(6 + 7 + 8 + 9 + 10) / 5 = 40 / 5 = 8."
    },
    {
      "type": "mc",
      "vraag": "Wat is de modus van de reeks: 3, 5, 5, 6, 7, 7, 7, 8, 9?",
      "opties": [
        "5",
        "6",
        "7",
        "8"
      ],
      "antwoord": 2,
      "uitleg": "Het getal 7 komt het vaakst voor (3 keer)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de mediaan van de getallen: 4, 8, 10, 14?",
      "opties": [
        "8",
        "11",
        "10",
        "9"
      ],
      "antwoord": 3,
      "uitleg": "Even aantal getallen: mediaan = (8 + 10) / 2 = 9."
    },
    {
      "type": "mc",
      "vraag": "Duru haalt voor wiskunde een 6 (telt 1x) en een 9 (telt 2x). Wat is haar gewogen gemiddelde?",
      "opties": [
        "8,0",
        "7,5",
        "7,0",
        "8,5"
      ],
      "antwoord": 0,
      "uitleg": "(1 × 6 + 2 × 9) / 3 = (6 + 18) / 3 = 24 / 3 = 8,0."
    },
    {
      "type": "mc",
      "vraag": "Welke centrummaat kan ook worden bepaald voor niet-numerieke gegevens (zoals oogkleur)?",
      "opties": [
        "Gemiddelde",
        "Modus",
        "Mediaan",
        "Klassenmidden"
      ],
      "antwoord": 1,
      "uitleg": "De modus is de meest voorkomende categorie (bijv. 'bruin' als meeste mensen bruine ogen hebben)."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de mediaan als de hoogste score in een getallenrij verdubbelt?",
      "opties": [
        "De mediaan verdubbelt ook",
        "De mediaan halveert",
        "De mediaan blijft exact gelijk",
        "De mediaan kan niet meer berekend worden"
      ],
      "antwoord": 2,
      "uitleg": "De mediaan kijkt puur naar de middelste positie en is ongevoelig voor extreme uitschieters."
    },
    {
      "type": "mc",
      "vraag": "Wat is de mediaan van: 12, 5, 8, 3, 19?",
      "opties": [
        "5",
        "9,4",
        "12",
        "8"
      ],
      "antwoord": 3,
      "uitleg": "Eerst sorteren: 3, 5, 8, 12, 19. Het middelste getal is 8."
    },
    {
      "type": "mc",
      "vraag": "In een klas scoren 10 leerlingen een 7 en 10 leerlingen een 9. Wat is het gemiddelde?",
      "opties": [
        "8,0",
        "7,5",
        "8,5",
        "9,0"
      ],
      "antwoord": 0,
      "uitleg": "(10 × 7 + 10 × 9) / 20 = 160 / 20 = 8,0."
    },
    {
      "type": "mc",
      "vraag": "Wat is de modus van de rij: 2, 4, 6, 8, 10?",
      "opties": [
        "6",
        "Er is geen modus",
        "0",
        "10"
      ],
      "antwoord": 1,
      "uitleg": "Alle getallen komen 1 keer voor; er is geen modus."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om de mediaan te bepalen moet je de data altijd eerst op volgorde zetten van klein naar groot.",
      "antwoord": true,
      "uitleg": "Waar: zonder sortering kun je het werkelijke midden niet bepalen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het gemiddelde is ongevoelig voor extreme uitschieters in de data.",
      "antwoord": false,
      "uitleg": "Onwaar: een extreme uitschieter trekt het gemiddelde sterk naar zich toe."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een even aantal getallen neem je voor de mediaan het gemiddelde van de twee middelste getallen.",
      "antwoord": true,
      "uitleg": "Waar: (middelste 1 + middelste 2) / 2."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een getallenrij heeft altijd exact één modus.",
      "antwoord": false,
      "uitleg": "Onwaar: er kan géén modus zijn (als alles even vaak voorkomt) of meerdere modi (bimodaal)."
    },
    {
      "type": "invul",
      "vraag": "Bereken het gemiddelde van de scores: 4, 6, 8, 10 en 12.",
      "antwoord": "8|8,0",
      "uitleg": "(4 + 6 + 8 + 10 + 12) / 5 = 40 / 5 = 8."
    },
    {
      "type": "invul",
      "vraag": "Wat is de mediaan van de getallen: 10, 14, 18, 22, 26, 30?",
      "antwoord": "20",
      "uitleg": "De twee middelste zijn 18 en 22. Mediaan = (18 + 22) / 2 = 20."
    },
    {
      "type": "invul",
      "vraag": "Wat is de modus van de reeks: 5, 8, 8, 9, 12, 12, 12, 15?",
      "antwoord": "12",
      "uitleg": "12 komt het vaakst voor (3x)."
    },
    {
      "type": "invul",
      "vraag": "Een leerling heeft een 5 (gewicht 1), een 7 (gewicht 2) en een 8 (gewicht 3). Bereken het gewogen gemiddelde.",
      "antwoord": "7,17|7,2|7,16",
      "uitleg": "(1×5 + 2×7 + 3×8) / 6 = (5 + 14 + 24) / 6 = 43 / 6 = 7,17."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom de mediaan soms een beter beeld van het midden geeft dan het gemiddelde aan de hand van salarisgegevens waarin één directeur miljoenen verdient.",
      "sleutelwoorden": [
        "uitschieter/extreem",
        "vertekend/beïnvloedt/ongevoelig"
      ],
      "minTreffers": 2,
      "modelantwoord": "Het gemiddelde wordt sterk omhoog getrokken door het extreem hoge salaris van de directeur (uitschieter). De mediaan kijkt naar de middelste werknemer en geeft daardoor een veel realistischer beeld van het typische inkomen.",
      "uitleg": "Mediaan is ongevoelig voor extreme uitschieters."
    },
    {
      "type": "open",
      "vraag": "Gegeven de getallen: 3, 7, 7, $x$. Bepaal de waarde van $x$ als het gemiddelde van de 4 getallen precies 8 moet zijn.",
      "sleutelwoorden": [
        "15",
        "32",
        "som"
      ],
      "minTreffers": 1,
      "modelantwoord": "Voor een gemiddelde van 8 moet de som 4 × 8 = 32 zijn. De huidige som is 3 + 7 + 7 = 17. Dus x = 32 - 17 = 15.",
      "uitleg": "x = 32 - 17 = 15."
    }
  ]
});
