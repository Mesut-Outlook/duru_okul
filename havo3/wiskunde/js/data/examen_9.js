/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 9 — Centrummaten: Gemiddelde, Mediaan & Modus
   ========================================================= */
DURU.registerExamen(
{
  "id": "ex-wiskunde-h2-9",
  "hoofdstuk": 2,
  "titel": "Proeftoets 9 — Centrummaten: Gemiddelde, Mediaan & Modus",
  "vak": "Wiskunde · H2 Statistiek",
  "icoon": "🎯",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven is de getallenrij: 3, 4, 7, 9, 12. Wat is de mediaan van deze getallen?",
      "opties": [
        "7",
        "4",
        "9",
        "7,0"
      ],
      "antwoord": 0,
      "uitleg": "De 5 getallen staan op volgorde; het 3e getal is precies het middelste: 7."
    },
    {
      "type": "mc",
      "vraag": "Gegeven is de getallenrij met een even aantal getallen: 4, 6, 8, 10, 12, 14. Wat is de mediaan?",
      "opties": [
        "8",
        "9",
        "10",
        "8,5"
      ],
      "antwoord": 1,
      "uitleg": "De twee middelste getallen zijn 8 en 10. De mediaan is het gemiddelde: (8 + 10) / 2 = 9."
    },
    {
      "type": "mc",
      "vraag": "Wat is de modus van de getallenreeks: 5, 7, 8, 8, 9, 11, 11, 11, 14?",
      "opties": [
        "9",
        "8",
        "11",
        "Er is geen modus"
      ],
      "antwoord": 2,
      "uitleg": "Het getal 11 komt het vaakst voor (3 keer) en is dus de modus."
    },
    {
      "type": "mc",
      "vraag": "Wat is het rekenkundig gemiddelde van de cijfers: 6, 7, 8, 8, 9, 10?",
      "opties": [
        "8,5",
        "7,5",
        "8,2",
        "8,0"
      ],
      "antwoord": 3,
      "uitleg": "Som = 6 + 7 + 8 + 8 + 9 + 10 = 48. Gemiddelde = 48 / 6 = 8,0."
    },
    {
      "type": "mc",
      "vraag": "Wanneer heeft een getallenreeks GEEN modus?",
      "opties": [
        "Wanneer alle getallen even vaak voorkomen (bijvoorbeeld allemaal 1 keer).",
        "Wanneer het aantal getallen oneven is.",
        "Wanneer het gemiddelde gelijk is aan de mediaan.",
        "Wanneer er negatieve getallen in de reeks voorkomen."
      ],
      "antwoord": 0,
      "uitleg": "Als geen enkel getal vaker voorkomt dan de rest, is er geen unieke hoogste frequentie en dus geen modus."
    },
    {
      "type": "mc",
      "vraag": "Een leerling haalt voor vier toetsen de cijfers 6,5; 7,0; 8,0 en 8,5. Welk cijfer moet hij voor de vijfde toets halen om precies een 7,5 gemiddeld te staan?",
      "opties": [
        "7,0",
        "7,5",
        "8,0",
        "6,5"
      ],
      "antwoord": 1,
      "uitleg": "Voor een gemiddelde van 7,5 over 5 toetsen is een totaalsom van 5 × 7,5 = 37,5 nodig. Huidige som = 6,5 + 7 + 8 + 8,5 = 30. Benodigd cijfer = 37,5 - 30 = 7,5."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de getallen: 14, 8, 22, 11, 19. Wat moet je ALTIJD eerst doen voordat je de mediaan kunt bepalen?",
      "opties": [
        "Het kleinste getal van het grootste getal aftrekken.",
        "Het gemiddelde van de getallen uitrekenen.",
        "De getallen op volgorde van klein naar groot zetten.",
        "Alle getallen vermenigvuldigen met elkaar."
      ],
      "antwoord": 2,
      "uitleg": "De mediaan is het middelste getal van een GEORDENDE reeks (8, 11, 14, 19, 22 → mediaan is 14)."
    },
    {
      "type": "mc",
      "vraag": "Welke centrummaat is het MEEST gevoelig voor één extreme uitschieter (bijvoorbeeld een extreem hoog of laag getal)?",
      "opties": [
        "Zowel de mediaan als de modus",
        "De mediaan",
        "De modus",
        "Het gemiddelde"
      ],
      "antwoord": 3,
      "uitleg": "Het gemiddelde telt elke waarde mee in de som en verschuift sterk bij een extreme uitschieter. De mediaan blijft op zijn plek."
    },
    {
      "type": "mc",
      "vraag": "In een straat wonen 5 gezinnen met de volgende aantallen huisdieren: 0, 1, 1, 2, 6. Wat is de mediaan van het aantal huisdieren?",
      "opties": [
        "1 huisdier",
        "2 huisdieren",
        "0 huisdieren",
        "2,5 huisdieren"
      ],
      "antwoord": 0,
      "uitleg": "De 5 getallen staan op volgorde (0, 1, 1, 2, 6). Het 3e getal is 1."
    },
    {
      "type": "mc",
      "vraag": "Wat is de modus van de schoenmaten: 38, 39, 40, 40, 41, 42, 42, 43?",
      "opties": [
        "De modus is 40,5.",
        "Er zijn twee modi: 40 en 42 (bimodaal).",
        "Er is geen modus.",
        "De modus is 41."
      ],
      "antwoord": 1,
      "uitleg": "Zowel 40 als 42 komen elk 2 keer voor en delen de hoogste frequentie. Er zijn twee modi."
    },
    {
      "type": "mc",
      "vraag": "Drie proefwerken tellen elk 1 keer mee en een grote eindtoets telt 2 keer mee (gewicht 2). Een leerling haalt voor de proefwerken een 6, 7 en 8, en voor de eindtoets een 9. Wat is het gewogen gemiddelde?",
      "opties": [
        "8,0",
        "7,5",
        "7,8",
        "7,6"
      ],
      "antwoord": 2,
      "uitleg": "Som = (6×1) + (7×1) + (8×1) + (9×2) = 6 + 7 + 8 + 18 = 39. Totale weging = 1 + 1 + 1 + 2 = 5. Gemiddelde = 39 / 5 = 7,8."
    },
    {
      "type": "mc",
      "vraag": "Als een reeks uit 15 geordende getallen bestaat, op welke positie bevindt zich dan de mediaan?",
      "opties": [
        "Het 9e getal",
        "Het 7e getal",
        "Het 7,5e getal",
        "Het 8e getal"
      ],
      "antwoord": 3,
      "uitleg": "(n + 1) / 2 = (15 + 1) / 2 = 16 / 2 = 8e getal."
    },
    {
      "type": "waaronwaar",
      "vraag": "De mediaan van een getallenreeks is altijd gelijk aan het rekenkundig gemiddelde van die reeks.",
      "antwoord": false,
      "uitleg": "Onwaar: gemiddelde en mediaan zijn meestal verschillend, zeker bij scheve verdelingen of uitschieters."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een getallenrij kan meerdere modi hebben als meerdere getallen dezelfde hoogste frequentie delen.",
      "antwoord": true,
      "uitleg": "Waar: delen twee waarden de hoogste frequentie, dan spreken we van twee modi (bimodaal)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om de mediaan van 10 getallen te berekenen neem je het gemiddelde van het 5e en 6e getal (mits geordend).",
      "antwoord": true,
      "uitleg": "Waar: bij een even aantal getallen neem je het gemiddelde van de twee middelste getallen."
    },
    {
      "type": "waaronwaar",
      "vraag": "De modus is de som van alle getallen gedeeld door het aantal getallen.",
      "antwoord": false,
      "uitleg": "Onwaar: dat is de definitie van het gemiddelde. De modus is de waarde die het vaakst voorkomt."
    },
    {
      "type": "invul",
      "vraag": "Het getal dat in een statistische dataset het vaakst voorkomt noemen we de [modus].",
      "antwoord": "modus",
      "uitleg": "De modus is de waarneming met de hoogste frequentie."
    },
    {
      "type": "invul",
      "vraag": "De middelste waarde van een op volgorde gezette getallenreeks heet de [mediaan].",
      "antwoord": "mediaan",
      "uitleg": "De mediaan verdeelt de geordende dataset precies in twee gelijke helften van 50%."
    },
    {
      "type": "open",
      "vraag": "Gegeven zijn de cijfers: 4, 9, 6, 7, 9, 8, 6, 7, 7. Bepaal het gemiddelde, de mediaan en de modus van deze cijfers.",
      "sleutelwoorden": [
        "gemiddelde = 7|gemiddelde 7",
        "mediaan = 7|mediaan 7",
        "modus = 7|modus 7"
      ],
      "minTreffers": 1,
      "modelantwoord": "Geordend: 4, 6, 6, 7, 7, 7, 8, 9, 9 (n = 9). Som = 63. Gemiddelde = 63 / 9 = 7. Mediaan = 5e getal = 7. Modus = 7 (komt 3 keer voor).",
      "uitleg": "Som is 63 / 9 = 7; middelste getal is 7; meest voorkomende getal is 7."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom een makelaar bij huizenprijzen in een wijk liever de mediaan vermeldt dan het gemiddelde.",
      "sleutelwoorden": [
        "uitschieter/villa/miljoenenwoning/duur huis",
        "gemiddelde omhoog trekt/vertekend beeld/mediaan betrouwbaarder"
      ],
      "minTreffers": 1,
      "modelantwoord": "Als er in een wijk één extreem duur landhuis van 3 miljoen euro staat, trekt dat het gemiddelde enorm omhoog. De mediaan trekt zich niets aan van die ene uitschieter en geeft een veel betrouwbaarder beeld van wat een 'normale' woning in die wijk kost.",
      "uitleg": "De mediaan is ongevoelig voor extreme uitschieters."
    }
  ]
}
);
