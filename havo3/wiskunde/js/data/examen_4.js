/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 4 — Steel-bladdiagram & Kwartielen
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h2-4",
  "hoofdstuk": 2,
  "titel": "Proeftoets 4 — Steel-bladdiagram & Kwartielen",
  "vak": "Wiskunde · H2 Statistiek",
  "icoon": "🌳",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "In een steel-bladdiagram staat steel 5 met bladeren 1, 4, 7 (legenda 5 | 1 = 51). Welke getallen zijn dit?",
      "opties": [
        "51, 54, 57",
        "5, 1, 4, 7",
        "15, 45, 75",
        "5147"
      ],
      "antwoord": 0,
      "uitleg": "Steel 5 met bladeren 1, 4 en 7 vormt 51, 54 en 57."
    },
    {
      "type": "mc",
      "vraag": "Wat is de spreidingsbreedte van een dataset met minimum 14 en maximum 62?",
      "opties": [
        "46",
        "48",
        "50",
        "76"
      ],
      "antwoord": 1,
      "uitleg": "Spreidingsbreedte = Max - Min = 62 - 14 = 48."
    },
    {
      "type": "mc",
      "vraag": "Welk kwartiel komt exact overeen met de mediaan van de hele dataset?",
      "opties": [
        "Eerste kwartiel (Q1)",
        "Derde kwartiel (Q3)",
        "Tweede kwartiel (Q2)",
        "Vierde kwartiel (Q4)"
      ],
      "antwoord": 2,
      "uitleg": "Q2 is de mediaan (50% punt)."
    },
    {
      "type": "mc",
      "vraag": "Als Q1 = 30 en Q3 = 55, wat is dan de kwartielafstand?",
      "opties": [
        "20",
        "85",
        "35",
        "25"
      ],
      "antwoord": 3,
      "uitleg": "Kwartielafstand = Q3 - Q1 = 55 - 30 = 25."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel procent van de waarnemingen ligt boven het derde kwartiel (Q3)?",
      "opties": [
        "25%",
        "50%",
        "75%",
        "100%"
      ],
      "antwoord": 0,
      "uitleg": "Boven Q3 bevindt zich het hoogste kwart (25%)."
    },
    {
      "type": "mc",
      "vraag": "In een steel-bladdiagram met legenda 2 | 3 = 2,3 staat steel 4 met blad 8. Welk getal is dit?",
      "opties": [
        "48",
        "4,8",
        "0,48",
        "480"
      ],
      "antwoord": 1,
      "uitleg": "Volgens de legenda staat 4 | 8 voor 4,8."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel waarnemingen bevat een steel-bladdiagram met in totaal 18 getallen in de bladeren?",
      "opties": [
        "9",
        "36",
        "18",
        "Afhankelijk van de steel"
      ],
      "antwoord": 2,
      "uitleg": "Elk cijfer in het blad vertegenwoordigt exact één waarneming (dus 18 waarnemingen)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de spreidingsbreedte van de getallen: 5, 8, 12, 19, 27?",
      "opties": [
        "20",
        "27",
        "24",
        "22"
      ],
      "antwoord": 3,
      "uitleg": "Max (27) - Min (5) = 22."
    },
    {
      "type": "mc",
      "vraag": "Welk percentage van de data ligt tussen het minimum en het eerste kwartiel (Q1)?",
      "opties": [
        "25%",
        "50%",
        "75%",
        "10%"
      ],
      "antwoord": 0,
      "uitleg": "Van minimum tot Q1 is het eerste kwart (25%)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het eerste kwartiel van de getallenrij: 2, 4, 6, 8, 10, 12, 14?",
      "opties": [
        "2",
        "4",
        "6",
        "8"
      ],
      "antwoord": 1,
      "uitleg": "Mediaan = 8. Linkerhelft = 2, 4, 6. De mediaan van de linkerhelft is Q1 = 4."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een steel-bladdiagram moeten de bladeren per steel altijd van klein naar groot worden gerangschikt.",
      "antwoord": true,
      "uitleg": "Waar: dit is verplicht om de mediaan en kwartielen direct te kunnen aflezen."
    },
    {
      "type": "waaronwaar",
      "vraag": "De kwartielafstand bereken je met de formule Q1 + Q3.",
      "antwoord": false,
      "uitleg": "Onwaar: kwartielafstand = Q3 - Q1."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een steel-bladdiagram behoudt alle individuele meetwaarden van de data.",
      "antwoord": true,
      "uitleg": "Waar: je kunt elk getal direct reconstrueren."
    },
    {
      "type": "waaronwaar",
      "vraag": "De spreidingsbreedte is ongevoelig voor uitschieters.",
      "antwoord": false,
      "uitleg": "Onwaar: spreidingsbreedte gebruikt juist het absolute minimum en maximum en is extreem gevoelig voor uitschieters."
    },
    {
      "type": "invul",
      "vraag": "Als de hoogste score 95 is en de laagste score 38, wat is dan de spreidingsbreedte?",
      "antwoord": "57",
      "uitleg": "De spreidingsbreedte is de hoogste min de laagste waarde: 95 - 38 = 57."
    },
    {
      "type": "invul",
      "vraag": "Als Q3 = 76 en Q1 = 42, bereken dan de kwartielafstand.",
      "antwoord": "34",
      "uitleg": "De kwartielafstand is het verschil tussen Q3 en Q1: 76 - 42 = 34."
    },
    {
      "type": "invul",
      "vraag": "In een steel-bladdiagram staat steel 8 met blad 0, 3, 9 (legenda 8 | 3 = 83). Wat is de hoogste waarde in deze rij?",
      "antwoord": "89",
      "uitleg": "8 met blad 9 = 89."
    },
    {
      "type": "invul",
      "vraag": "Welk percentage van de waarnemingen ligt tussen Q1 en Q3?",
      "antwoord": "50|50%|50 procent",
      "uitleg": "Tussen 25% en 75% zit 50% van de data."
    },
    {
      "type": "open",
      "vraag": "Leg uit hoe je stapsgewijs het eerste kwartiel (Q1) en derde kwartiel (Q3) bepaalt uit een geordende getallenreeks.",
      "sleutelwoorden": [
        "mediaan",
        "linkerhelft",
        "rechterhelft"
      ],
      "minTreffers": 2,
      "modelantwoord": "1) Bepaal eerst de algehele mediaan (Q2) die de rij in twee helften splitst. 2) Bepaal de mediaan van de linkerhelft (dit is Q1). 3) Bepaal de mediaan van de rechterhelft (dit is Q3).",
      "uitleg": "Q1 is mediaan van linkerhelft, Q3 is mediaan van rechterhelft."
    },
    {
      "type": "open",
      "vraag": "Gegeven de scores: 10, 12, 14, 16, 18, 20, 22. Bereken Q1, Mediaan (Q2) en Q3.",
      "sleutelwoorden": [
        "12",
        "16",
        "20"
      ],
      "minTreffers": 3,
      "modelantwoord": "Mediaan (Q2) = 16. Linkerhelft is 10, 12, 14 -> Q1 = 12. Rechterhelft is 18, 20, 22 -> Q3 = 20.",
      "uitleg": "Q1 = 12, Q2 = 16, Q3 = 20."
    }
  ]
});
