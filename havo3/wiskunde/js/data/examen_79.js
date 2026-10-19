/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 79 — §1.5 Groeifactor en tijd (extra 1/5, basis)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-56",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 79 — §1.5 Groeifactor en tijd (extra 1/5, basis)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 2,5% per jaar. Met hoeveel procent groeit de bevolking in 100 jaar? Rond af op één decimaal.",
      "antwoord": "1081,4",
      "uitleg": "Groeifactor per jaar 1,025. Per 100 jaar: 1,025¹⁰⁰ ≈ 11,814, dus ongeveer 1081,4% groei (niet 250%).",
      "tolerantie": 0.15
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 0,96ᵗ met t in dagen. Bereken de groeifactor per 2 dagen. Rond af op drie decimalen.",
      "antwoord": "0,922",
      "uitleg": "2 dagen = 2 stappen: 0,96² ≈ 0,922.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,5 per week. Bereken de groeifactor per twee weken.",
      "antwoord": "2,25",
      "uitleg": "Per twee weken zijn er twee stappen: 1,5 · 1,5 = 1,5² = 2,25.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "Het totaal aantal gespeelde partijen op een schaakwebsite nam exponentieel toe met groeifactor 1,015 per maand. Op 1 december waren er in totaal 412.000 partijen gespeeld. Hoeveel waren dat er op 1 augustus? Rond af op een geheel getal.",
      "antwoord": "388180",
      "uitleg": "1 augustus is 4 maanden eerder. Delen door de groeifactor per 4 maanden: 412.000 : 1,015⁴ ≈ 388.180.",
      "tolerantie": 194
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,917ᵗ procent werkzaam. Na 6 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": true,
      "uitleg": "Waar. P = 100 · 0,917⁶ ≈ 59,5%. Er is dus 40,5% verdwenen, meer dan een kwart (25%)."
    },
    {
      "type": "mc",
      "vraag": "Het aantal bezoekers is N = 840 · 1,08ᵗ met t in jaren. Welke formule hoort bij t in perioden van 2 jaar? (groeifactor in drie decimalen)",
      "uitleg": "Per 2 jaar: 1,08² ≈ 1,166. De beginwaarde 840 blijft hetzelfde.",
      "opties": [
        "N = 840 · 1,039ᵗ",
        "N = 840 · 1,160ᵗ",
        "N = 1680 · 1,08ᵗ",
        "N = 840 · 1,166ᵗ"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,3ᵗ is t de tijd in kwartieren. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "2,86",
      "uitleg": "In een uur passen 4 keer kwartier. Groeifactor per uur: 1,3⁴ ≈ 2,8561 ≈ 2,86.",
      "tolerantie": 0.006
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 2400 dieren. Dat aantal neemt elk jaar met 4% toe. Na hoeveel hele jaren is het aantal voor het eerst meer dan 4800 dieren?",
      "antwoord": "18",
      "uitleg": "Groeifactor 1,04. Probeer t: na 17 jaar 4675, na 18 jaar 4862 (grens 4800). Dus na 18 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 0,95 per jaar. In 2020 kwamen er 112.000 bezoekers. Bereken het aantal bezoekers in 2030. Rond af op een geheel getal.",
      "antwoord": "67059",
      "uitleg": "Groeifactor per 10 jaar: 0,95¹⁰ ≈ 0,5987. Vooruit: vermenigvuldigen: 112.000 · 0,5987 ≈ 67.059.",
      "tolerantie": 67
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,93ᵗ procent werkzaam. Na 2 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": false,
      "uitleg": "Onwaar. P = 100 · 0,93² ≈ 86,5%. Er is dus 13,5% verdwenen, minder dan een kwart (25%)."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 20 · 1,025ᵗ, met t in maanden. Hoeveel dollar is de vaas na 18 maanden waard? Rond af op twee decimalen.",
      "antwoord": "31,19",
      "uitleg": "t = 18: W = 20 · 1,025¹⁸ ≈ 31,19 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "De waarde van een aandeel groeit met groeifactor 0,980 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,980¹² ≈ 0,785. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "0,922",
        "0,760",
        "0,785",
        "11,760"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 4% per jaar. Met hoeveel procent groeit de bevolking in 100 jaar? Rond af op één decimaal.",
      "antwoord": "4950,5",
      "uitleg": "Groeifactor per jaar 1,04. Per 100 jaar: 1,04¹⁰⁰ ≈ 50,505, dus ongeveer 4950,5% groei (niet 400%).",
      "tolerantie": 0.15
    },
    {
      "type": "waaronwaar",
      "vraag": "Een hoeveelheid groeit met 5% per jaar. Dat is hetzelfde als een groei van 50% in 10 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 10 jaar is 1,05¹⁰ ≈ 1,629, dus ongeveer 62,9% groei, niet 50%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,95 per uur. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 3 uur eerder? Rond af op een geheel getal.",
      "antwoord": "373232",
      "uitleg": "Groeifactor per 3 uur: 0,95³. Terugrekenen = delen: 320.000 : 0,95³ ≈ 373232.",
      "tolerantie": 186
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,4 per 10 minuten, soort B met groeifactor 30 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,4⁶ ≈ 7,5. Vergelijk met 30: soort B groeit het snelst.",
      "opties": [
        "ze groeien even snel",
        "soort B",
        "dat kun je niet vergelijken",
        "soort A"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 1,07ᵗ met t in jaren. Bereken de groeifactor per 6 jaar. Rond af op drie decimalen.",
      "antwoord": "1,501",
      "uitleg": "6 jaar = 6 stappen: 1,07⁶ ≈ 1,501.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 4 miljoen mensen. Dat aantal neemt elk jaar met 8% af. Na hoeveel hele jaren is het aantal voor het eerst minder dan de helft?",
      "antwoord": "9",
      "uitleg": "Groeifactor 0,92. Probeer t: na 8 jaar 2,05, na 9 jaar 1,89 (grens 2). Dus na 9 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 0,97 per jaar. In 2020 kwamen er 86.000 bezoekers. Bereken het aantal bezoekers in 2010. Rond af op een geheel getal.",
      "antwoord": "116622",
      "uitleg": "Groeifactor per 10 jaar: 0,97¹⁰ ≈ 0,7374. Terug: delen: 86.000 : 0,7374 ≈ 116.622.",
      "tolerantie": 116
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 1000 · 1,10ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 1000 · 1,33ᵗ",
      "sleutelwoorden": [
        "1,33/1.33"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,10³ ≈ 1,33. De beginwaarde blijft 1000: A = 1000 · 1,33ᵗ."
    }
  ]
});
