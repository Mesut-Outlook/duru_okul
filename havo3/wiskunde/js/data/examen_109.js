/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 109 — §2.4 De vorm en de ligging van de parabool (1/5, basis)
   Bron: Noordhoff H2 Parabolen (§2.4)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-24-1",
  "hoofdstuk": 2,
  "paragraaf": "2.4",
  "titel": "Proeftoets 109 — §2.4 De vorm en de ligging van de parabool (1/5, basis)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = −3x² − 3x + 3?",
      "uitleg": "Kijk naar het getal voor x²: a = −3. Omdat a negatief is, is de grafiek een bergparabool.",
      "opties": [
        "een dalparabool, want het startgetal is positief",
        "een dalparabool, want het getal voor x² is negatief",
        "een rechte lijn, omdat er ook een losse x in de formule staat",
        "een bergparabool, want het getal voor x² is negatief"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Heeft de parabool bij de formule y = −¼x² + 7x + 1 een maximum of een minimum?",
      "uitleg": "Bij a = −¼ is de grafiek een bergparabool, dus heeft de parabool een maximum (hoogste punt).",
      "opties": [
        "een minimum (laagste punt)",
        "geen top, want de grafiek loopt oneindig ver door",
        "zowel een maximum als een minimum",
        "een maximum (hoogste punt)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van het snijpunt van de parabool bij y = 3x² + 6x − 5 met de y-as?",
      "uitleg": "Het snijpunt met de y-as vind je door x = 0 in te vullen: y = −5. De coördinaten zijn (0, −5).",
      "opties": [
        "(0, 5)",
        "(0, −5)",
        "(5, 0)",
        "(−5, 0)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Geef de y-coördinaat van het snijpunt van de parabool bij y = −4x² − x − 6 met de y-as.",
      "antwoord": "-6",
      "uitleg": "Bij x = 0 blijft alleen c over: het snijpunt met de y-as is (0, −6)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −½x² − 11 heeft zijn top op de y-as. Wat is de x-coördinaat van de top?",
      "antwoord": "0",
      "uitleg": "Omdat b = 0 ligt de top op de y-as. Voor alle punten op de y-as geldt x = 0, dus de x-coördinaat van de top is 0."
    },
    {
      "type": "waaronwaar",
      "vraag": "De parabool bij y = −½x² + 7x + 7 is smaller dan de parabool bij y = −¼x² + 8x + 6.",
      "antwoord": true,
      "uitleg": "Waar. Kijk naar het getal voor x²: −½ en −¼. Hoe verder van 0, hoe smaller. −½ ligt verder van 0 dan −¼, dus de eerste parabool is smaller."
    },
    {
      "type": "waaronwaar",
      "vraag": "De parabool bij y = −x² − 2x − 5 is smaller dan de parabool bij y = 4x² − x + 7.",
      "antwoord": false,
      "uitleg": "Onwaar. Kijk naar het getal voor x²: −1 en 4. Hoe verder van 0, hoe smaller. −1 ligt dichter bij 0 dan 4, dus de eerste parabool is breder."
    },
    {
      "type": "waaronwaar",
      "vraag": "De parabool bij y = −2x² − x gaat door de oorsprong.",
      "antwoord": true,
      "uitleg": "Waar. Door de oorsprong ⇔ c = 0: bij x = 0 moet y = 0 zijn. Hier is c = 0."
    },
    {
      "type": "waaronwaar",
      "vraag": "De parabool bij y = 3x² − 2x + 3 gaat door de oorsprong.",
      "antwoord": false,
      "uitleg": "Onwaar. Door de oorsprong ⇔ c = 0: bij x = 0 moet y = 0 zijn. Hier is c = 3."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = −½x² + 8x + 4, y = −2x² − 6x − 6, y = ⅓x² + 3x + 8 en y = −3x² − 4. Bij welke formule is de parabool het smalst?",
      "uitleg": "Vergelijk de getallen voor x²: −½, −2, ⅓, −3. Het verst van 0 ligt −3, dus die parabool is het smalst.",
      "opties": [
        "y = −3x² − 4",
        "y = −2x² − 6x − 6",
        "y = ⅓x² + 3x + 8",
        "y = −½x² + 8x + 4"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = ¼x² + 5x − 1, y = −⅓x² + 6x − 5, y = ½x² + 5x − 8 en y = −x² + 8x − 6. Bij welke formule is de parabool het breedst?",
      "uitleg": "Vergelijk de getallen voor x²: ¼, −⅓, ½, −1. Het dichtst bij 0 ligt ¼, dus die parabool is het breedst.",
      "opties": [
        "y = ½x² + 5x − 8",
        "y = −⅓x² + 6x − 5",
        "y = −x² + 8x − 6",
        "y = ¼x² + 5x − 1"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = −¼x² − 2, y = x² − 4x − 8, y = 4x² − x − 9 en y = ½x² − 9x − 4. Bij welke formule ligt de top van de parabool op de y-as?",
      "uitleg": "Ligt de top op de y-as, dan is b = 0: de formule heeft de vorm y = ax² + c. Dat is y = −¼x² − 2.",
      "opties": [
        "y = 4x² − x − 9",
        "y = −¼x² − 2",
        "y = x² − 4x − 8",
        "y = ½x² − 9x − 4"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = 3x² − 9x − 1, y = 4x² + 9x − 9, y = 4x² − 3x en y = −3x² − 8x − 7. Bij welke formule gaat de parabool door de oorsprong?",
      "uitleg": "Gaat de parabool door de oorsprong, dan is c = 0: bij x = 0 hoort y = 0. Dat is y = 4x² − 3x.",
      "opties": [
        "y = 3x² − 9x − 1",
        "y = 4x² + 9x − 9",
        "y = 4x² − 3x",
        "y = −3x² − 8x − 7"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −9 + 3x²?",
      "uitleg": "Er is geen term met x (b = 0), dus de top ligt op de y-as: (0, −9).",
      "opties": [
        "(0, −9)",
        "(−9, 0)",
        "(0, 9)",
        "(3, −9)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −4x² + 6x + c snijdt de y-as in het punt (0, −12). Wat is de waarde van c?",
      "antwoord": "-12",
      "uitleg": "Het snijpunt met de y-as vind je door x = 0 in te vullen. Dan is y = c. Omdat het snijpunt (0, −12) is, is c = −12."
    },
    {
      "type": "invul",
      "vraag": "De baan van een weggeschoten bal wordt beschreven door h = −0,2x² + 4x + 2. Hierin is h de hoogte in meters en x de horizontale afstand in meters. Op welke hoogte in meters wordt de bal weggeschoten (bij x = 0)?",
      "antwoord": "2",
      "uitleg": "Vul x = 0 in de formule in: h = −0,2 · 0² + 4 · 0 + 2 = 2 meter."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn parabool 1: y = −x² + 4 en parabool 2: y = −3x² − 8x − 8. Welke uitspraak over de breedte is juist?",
      "uitleg": "Kijk naar |a|: bij parabool 1 is |a| = 1 en bij parabool 2 is |a| = 3. Omdat 1 dichter bij 0 ligt, is parabool 1 breder.",
      "opties": [
        "Beide parabolen zijn exact even breed",
        "Parabool 1 is smaller dan parabool 2",
        "Parabool 1 is breder dan parabool 2",
        "Dat kun je niet bepalen zonder grafiek"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Welke van de volgende parabolen is even breed als de parabool bij y = 3x² + 1?",
      "uitleg": "Twee parabolen zijn even breed als de absolute waarde van het getal voor x² gelijk is (|a| = 3). Dat is zo bij y = −3x² + 4x + 7.",
      "opties": [
        "y = 2x² + 3x + 4",
        "y = −3x² + 4x + 7",
        "y = −x² − 3x − 7",
        "y = −¼x² + 3x + 4"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Geef de y-coördinaat van het snijpunt van de parabool bij y = −2x² − 6x + 5 met de y-as.",
      "antwoord": "5",
      "uitleg": "Bij x = 0 blijft alleen c over: het snijpunt met de y-as is (0, 5)."
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = −4x² − x + 9?",
      "uitleg": "Kijk naar het getal voor x²: a = −4. Omdat a negatief is, is de grafiek een bergparabool.",
      "opties": [
        "een bergparabool, want het getal voor x² is negatief",
        "een rechte lijn, omdat er ook een losse x in de formule staat",
        "een dalparabool, want het startgetal is positief",
        "een dalparabool, want het getal voor x² is negatief"
      ],
      "antwoord": 0
    }
  ]
});
