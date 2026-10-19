/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 83 — §1.5 Groeifactor en tijd (extra 5/5, eindniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-60",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 83 — §1.5 Groeifactor en tijd (extra 5/5, eindniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 2% per jaar. Met hoeveel procent groeit de bevolking in 100 jaar? Rond af op één decimaal.",
      "antwoord": "624,5",
      "uitleg": "Groeifactor per jaar 1,02. Per 100 jaar: 1,02¹⁰⁰ ≈ 7,245, dus ongeveer 624,5% groei (niet 200%).",
      "tolerantie": 0.15
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 0,93ᵗ met t in dagen. Bereken de groeifactor per 3 dagen. Rond af op drie decimalen.",
      "antwoord": "0,804",
      "uitleg": "3 dagen = 3 stappen: 0,93³ ≈ 0,804.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,2 per half uur. Bereken de groeifactor per uur.",
      "antwoord": "1,44",
      "uitleg": "Per uur zijn er twee stappen: 1,2 · 1,2 = 1,2² = 1,44.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "Het totaal aantal gespeelde partijen op een schaakwebsite nam exponentieel toe met groeifactor 1,06 per maand. Op 1 november waren er in totaal 75.800 partijen gespeeld. Hoeveel waren dat er op 1 juli? Rond af op een geheel getal.",
      "antwoord": "60041",
      "uitleg": "1 juli is 4 maanden eerder. Delen door de groeifactor per 4 maanden: 75.800 : 1,06⁴ ≈ 60.041.",
      "tolerantie": 30
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,93ᵗ procent werkzaam. Na 5 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": true,
      "uitleg": "Waar. P = 100 · 0,93⁵ ≈ 69,6%. Er is dus 30,4% verdwenen, meer dan een kwart (25%)."
    },
    {
      "type": "mc",
      "vraag": "Het aantal bezoekers is N = 25.000 · 1,04ᵗ met t in jaren. Welke formule hoort bij t in perioden van 2 jaar? (groeifactor in drie decimalen)",
      "uitleg": "Per 2 jaar: 1,04² ≈ 1,082. De beginwaarde 25.000 blijft hetzelfde.",
      "opties": [
        "N = 25.000 · 1,080ᵗ",
        "N = 25.000 · 1,082ᵗ",
        "N = 25.000 · 1,020ᵗ",
        "N = 50.000 · 1,04ᵗ"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,1ᵗ is t de tijd in eenheden van tien minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "1,77",
      "uitleg": "In een uur passen 6 keer tien minuten. Groeifactor per uur: 1,1⁶ ≈ 1,7716 ≈ 1,77.",
      "tolerantie": 0.006
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 4 miljoen mensen. Dat aantal neemt elk jaar met 3% af. Na hoeveel hele jaren is het aantal voor het eerst minder dan de helft?",
      "antwoord": "23",
      "uitleg": "Groeifactor 0,97. Probeer t: na 22 jaar 2,05, na 23 jaar 1,99 (grens 2). Dus na 23 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 1,04 per jaar. In 2020 kwamen er 112.000 bezoekers. Bereken het aantal bezoekers in 2025. Rond af op een geheel getal.",
      "antwoord": "136265",
      "uitleg": "Groeifactor per 5 jaar: 1,04⁵ ≈ 1,2167. Vooruit: vermenigvuldigen: 112.000 · 1,2167 ≈ 136.265.",
      "tolerantie": 136
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,96ᵗ procent werkzaam. Na 3 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": false,
      "uitleg": "Onwaar. P = 100 · 0,96³ ≈ 88,5%. Er is dus 11,5% verdwenen, minder dan een kwart (25%)."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 50 · 1,025ᵗ, met t in maanden. Hoeveel dollar is de vaas na 18 maanden waard? Rond af op twee decimalen.",
      "antwoord": "77,98",
      "uitleg": "t = 18: W = 50 · 1,025¹⁸ ≈ 77,98 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "De waarde van een oude auto groeit met groeifactor 0,980 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,980¹² ≈ 0,785. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "0,922",
        "11,760",
        "0,760",
        "0,785"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 1,8% per jaar. Met hoeveel procent groeit de bevolking in 20 jaar? Rond af op één decimaal.",
      "antwoord": "42,9",
      "uitleg": "Groeifactor per jaar 1,018. Per 20 jaar: 1,018²⁰ ≈ 1,429, dus ongeveer 42,9% groei (niet 36%).",
      "tolerantie": 0.15
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal leden van een club groeit met 10% per jaar. Dat is hetzelfde als een groei van 100% in 10 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 10 jaar is 1,1¹⁰ ≈ 2,594, dus ongeveer 159,4% groei, niet 100%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,025 per uur. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 3 uur eerder? Rond af op een geheel getal.",
      "antwoord": "297152",
      "uitleg": "Groeifactor per 3 uur: 1,025³. Terugrekenen = delen: 320.000 : 1,025³ ≈ 297152.",
      "tolerantie": 148
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,5 per 10 minuten, soort B met groeifactor 12 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,5⁶ ≈ 11,4. Vergelijk met 12: soort B groeit het snelst.",
      "opties": [
        "ze groeien even snel",
        "dat kun je niet vergelijken",
        "soort B",
        "soort A"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 1,6ᵗ met t in dagen. Bereken de groeifactor per 3 dagen. Rond af op drie decimalen.",
      "antwoord": "4,096",
      "uitleg": "3 dagen = 3 stappen: 1,6³ ≈ 4,096.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 4 miljoen mensen. Dat aantal neemt elk jaar met 15% toe. Na hoeveel hele jaren is het aantal voor het eerst meer dan 8 miljoen mensen?",
      "antwoord": "5",
      "uitleg": "Groeifactor 1,15. Probeer t: na 4 jaar 7,00, na 5 jaar 8,05 (grens 8). Dus na 5 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 1,04 per jaar. In 2020 kwamen er 86.000 bezoekers. Bereken het aantal bezoekers in 2025. Rond af op een geheel getal.",
      "antwoord": "104632",
      "uitleg": "Groeifactor per 5 jaar: 1,04⁵ ≈ 1,2167. Vooruit: vermenigvuldigen: 86.000 · 1,2167 ≈ 104.632.",
      "tolerantie": 104
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 500 · 1,06ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 500 · 1,19ᵗ",
      "sleutelwoorden": [
        "1,19/1.19"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,06³ ≈ 1,19. De beginwaarde blijft 500: A = 500 · 1,19ᵗ."
    }
  ]
});
