/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 81 — §1.5 Groeifactor en tijd (extra 3/5, gemengd)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-58",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 81 — §1.5 Groeifactor en tijd (extra 3/5, gemengd)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 2% per jaar. Met hoeveel procent groeit de bevolking in 20 jaar? Rond af op één decimaal.",
      "antwoord": "48,6",
      "uitleg": "Groeifactor per jaar 1,02. Per 20 jaar: 1,02²⁰ ≈ 1,486, dus ongeveer 48,6% groei (niet 40%).",
      "tolerantie": 0.15
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 0,96ᵗ met t in weken. Bereken de groeifactor per 6 weken. Rond af op drie decimalen.",
      "antwoord": "0,783",
      "uitleg": "6 weken = 6 stappen: 0,96⁶ ≈ 0,783.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,2 per halfjaar. Bereken de groeifactor per jaar.",
      "antwoord": "1,44",
      "uitleg": "Per jaar zijn er twee stappen: 1,2 · 1,2 = 1,2² = 1,44.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "Het totaal aantal gespeelde partijen op een schaakwebsite nam exponentieel toe met groeifactor 1,06 per maand. Op 1 november waren er in totaal 96.500 partijen gespeeld. Hoeveel waren dat er op 1 augustus? Rond af op een geheel getal.",
      "antwoord": "81023",
      "uitleg": "1 augustus is 3 maanden eerder. Delen door de groeifactor per 3 maanden: 96.500 : 1,06³ ≈ 81.023.",
      "tolerantie": 40
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,88ᵗ procent werkzaam. Na 3 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": true,
      "uitleg": "Waar. P = 100 · 0,88³ ≈ 68,1%. Er is dus 31,9% verdwenen, meer dan een kwart (25%)."
    },
    {
      "type": "mc",
      "vraag": "Het aantal bezoekers is N = 112.000 · 0,95ᵗ met t in jaren. Welke formule hoort bij t in perioden van 5 jaar? (groeifactor in drie decimalen)",
      "uitleg": "Per 5 jaar: 0,95⁵ ≈ 0,774. De beginwaarde 112.000 blijft hetzelfde.",
      "opties": [
        "N = 560.000 · 0,95ᵗ",
        "N = 112.000 · 0,750ᵗ",
        "N = 112.000 · 0,990ᵗ",
        "N = 112.000 · 0,774ᵗ"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,3ᵗ is t de tijd in eenheden van tien minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "4,83",
      "uitleg": "In een uur passen 6 keer tien minuten. Groeifactor per uur: 1,3⁶ ≈ 4,8268 ≈ 4,83.",
      "tolerantie": 0.006
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 2,5 miljoen mensen. Dat aantal neemt elk jaar met 20% af. Na hoeveel hele jaren is het aantal voor het eerst minder dan de helft?",
      "antwoord": "4",
      "uitleg": "Groeifactor 0,8. Probeer t: na 3 jaar 1,28, na 4 jaar 1,02 (grens 1,25). Dus na 4 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 1,04 per jaar. In 2020 kwamen er 112.000 bezoekers. Bereken het aantal bezoekers in 2010. Rond af op een geheel getal.",
      "antwoord": "75663",
      "uitleg": "Groeifactor per 10 jaar: 1,04¹⁰ ≈ 1,4802. Terug: delen: 112.000 : 1,4802 ≈ 75.663.",
      "tolerantie": 75
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,95ᵗ procent werkzaam. Na 3 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": false,
      "uitleg": "Onwaar. P = 100 · 0,95³ ≈ 85,7%. Er is dus 14,3% verdwenen, minder dan een kwart (25%)."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 300 · 1,025ᵗ, met t in maanden. Hoeveel dollar is de vaas na 2 jaar waard? Rond af op twee decimalen.",
      "antwoord": "542,62",
      "uitleg": "Na 2 jaar is t = 24: W = 300 · 1,025²⁴ ≈ 542,62 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "De waarde van een oude auto groeit met groeifactor 1,019 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 1,019¹² ≈ 1,253. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "12,228",
        "1,253",
        "1,078",
        "1,228"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 3% per jaar. Met hoeveel procent groeit de bevolking in 100 jaar? Rond af op één decimaal.",
      "antwoord": "1821,9",
      "uitleg": "Groeifactor per jaar 1,03. Per 100 jaar: 1,03¹⁰⁰ ≈ 19,219, dus ongeveer 1821,9% groei (niet 300%).",
      "tolerantie": 0.15
    },
    {
      "type": "waaronwaar",
      "vraag": "Een spaarbedrag groeit met 3% per jaar. Dat is hetzelfde als een groei van 60% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,03²⁰ ≈ 1,806, dus ongeveer 80,6% groei, niet 60%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,12 per jaar. Nu is de hoeveelheid 254.200. Hoe groot was de hoeveelheid 3 jaar eerder? Rond af op een geheel getal.",
      "antwoord": "180935",
      "uitleg": "Groeifactor per 3 jaar: 1,12³. Terugrekenen = delen: 254.200 : 1,12³ ≈ 180935.",
      "tolerantie": 90
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,9 per 10 minuten, soort B met groeifactor 19 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,9⁶ ≈ 47,0. Vergelijk met 19: soort A groeit het snelst.",
      "opties": [
        "soort A",
        "ze groeien even snel",
        "soort B",
        "dat kun je niet vergelijken"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 1,15ᵗ met t in jaren. Bereken de groeifactor per 3 jaar. Rond af op drie decimalen.",
      "antwoord": "1,521",
      "uitleg": "3 jaar = 3 stappen: 1,15³ ≈ 1,521.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 2400 dieren. Dat aantal neemt elk jaar met 20% af. Na hoeveel hele jaren is het aantal voor het eerst minder dan de helft?",
      "antwoord": "4",
      "uitleg": "Groeifactor 0,8. Probeer t: na 3 jaar 1229, na 4 jaar 983 (grens 1200). Dus na 4 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 1,04 per jaar. In 2020 kwamen er 54.000 bezoekers. Bereken het aantal bezoekers in 2025. Rond af op een geheel getal.",
      "antwoord": "65699",
      "uitleg": "Groeifactor per 5 jaar: 1,04⁵ ≈ 1,2167. Vooruit: vermenigvuldigen: 54.000 · 1,2167 ≈ 65.699.",
      "tolerantie": 65
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 200 · 1,04ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 200 · 1,12ᵗ",
      "sleutelwoorden": [
        "1,12/1.12"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,04³ ≈ 1,12. De beginwaarde blijft 200: A = 200 · 1,12ᵗ."
    }
  ]
});
