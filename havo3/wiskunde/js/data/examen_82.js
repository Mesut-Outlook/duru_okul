/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 82 — §1.5 Groeifactor en tijd (extra 4/5, toetsniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-59",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 82 — §1.5 Groeifactor en tijd (extra 4/5, toetsniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 1,8% per jaar. Met hoeveel procent groeit de bevolking in 100 jaar? Rond af op één decimaal.",
      "antwoord": "495,4",
      "uitleg": "Groeifactor per jaar 1,018. Per 100 jaar: 1,018¹⁰⁰ ≈ 5,954, dus ongeveer 495,4% groei (niet 180%).",
      "tolerantie": 0.15
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 1,15ᵗ met t in dagen. Bereken de groeifactor per 6 dagen. Rond af op drie decimalen.",
      "antwoord": "2,313",
      "uitleg": "6 dagen = 6 stappen: 1,15⁶ ≈ 2,313.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,9 per half uur. Bereken de groeifactor per uur.",
      "antwoord": "0,81",
      "uitleg": "Per uur zijn er twee stappen: 0,9 · 0,9 = 0,9² = 0,81.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "Het totaal aantal gespeelde partijen op een schaakwebsite nam exponentieel toe met groeifactor 1,04 per maand. Op 1 december waren er in totaal 412.000 partijen gespeeld. Hoeveel waren dat er op 1 juni? Rond af op een geheel getal.",
      "antwoord": "325610",
      "uitleg": "1 juni is 6 maanden eerder. Delen door de groeifactor per 6 maanden: 412.000 : 1,04⁶ ≈ 325.610.",
      "tolerantie": 162
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,85ᵗ procent werkzaam. Na 3 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": true,
      "uitleg": "Waar. P = 100 · 0,85³ ≈ 61,4%. Er is dus 38,6% verdwenen, meer dan een kwart (25%)."
    },
    {
      "type": "mc",
      "vraag": "Het aantal bezoekers is N = 840 · 1,08ᵗ met t in jaren. Welke formule hoort bij t in perioden van 10 jaar? (groeifactor in drie decimalen)",
      "uitleg": "Per 10 jaar: 1,08¹⁰ ≈ 2,159. De beginwaarde 840 blijft hetzelfde.",
      "opties": [
        "N = 840 · 2,159ᵗ",
        "N = 840 · 1,008ᵗ",
        "N = 8400 · 1,08ᵗ",
        "N = 840 · 1,800ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,2ᵗ is t de tijd in kwartieren. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "2,07",
      "uitleg": "In een uur passen 4 keer kwartier. Groeifactor per uur: 1,2⁴ ≈ 2,0736 ≈ 2,07.",
      "tolerantie": 0.006
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 4 miljoen mensen. Dat aantal neemt elk jaar met 10% toe. Na hoeveel hele jaren is het aantal voor het eerst meer dan 8 miljoen mensen?",
      "antwoord": "8",
      "uitleg": "Groeifactor 1,1. Probeer t: na 7 jaar 7,79, na 8 jaar 8,57 (grens 8). Dus na 8 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 0,95 per jaar. In 2020 kwamen er 240.000 bezoekers. Bereken het aantal bezoekers in 2010. Rond af op een geheel getal.",
      "antwoord": "400844",
      "uitleg": "Groeifactor per 10 jaar: 0,95¹⁰ ≈ 0,5987. Terug: delen: 240.000 : 0,5987 ≈ 400.844.",
      "tolerantie": 400
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,95ᵗ procent werkzaam. Na 5 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": false,
      "uitleg": "Onwaar. P = 100 · 0,95⁵ ≈ 77,4%. Er is dus 22,6% verdwenen, minder dan een kwart (25%)."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 120 · 1,012ᵗ, met t in maanden. Hoeveel dollar is de vaas na 2 jaar waard? Rond af op twee decimalen.",
      "antwoord": "159,78",
      "uitleg": "Na 2 jaar is t = 24: W = 120 · 1,012²⁴ ≈ 159,78 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "De waarde van een postzegelverzameling groeit met groeifactor 0,970 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,970¹² ≈ 0,694. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "0,885",
        "11,640",
        "0,640",
        "0,694"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 3% per jaar. Met hoeveel procent groeit de bevolking in 50 jaar? Rond af op één decimaal.",
      "antwoord": "338,4",
      "uitleg": "Groeifactor per jaar 1,03. Per 50 jaar: 1,03⁵⁰ ≈ 4,384, dus ongeveer 338,4% groei (niet 150%).",
      "tolerantie": 0.15
    },
    {
      "type": "waaronwaar",
      "vraag": "De bevolking groeit met 5% per jaar. Dat is hetzelfde als een groei van 100% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,05²⁰ ≈ 2,653, dus ongeveer 165,3% groei, niet 100%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,95 per maand. Nu is de hoeveelheid 2000. Hoe groot was de hoeveelheid 4 maanden eerder? Rond af op een geheel getal.",
      "antwoord": "2455",
      "uitleg": "Groeifactor per 4 maanden: 0,95⁴. Terugrekenen = delen: 2000 : 0,95⁴ ≈ 2455.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,6 per 10 minuten, soort B met groeifactor 8 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,6⁶ ≈ 16,8. Vergelijk met 8: soort A groeit het snelst.",
      "opties": [
        "soort B",
        "soort A",
        "ze groeien even snel",
        "dat kun je niet vergelijken"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 0,85ᵗ met t in dagen. Bereken de groeifactor per 3 dagen. Rond af op drie decimalen.",
      "antwoord": "0,614",
      "uitleg": "3 dagen = 3 stappen: 0,85³ ≈ 0,614.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 800 dieren. Dat aantal neemt elk jaar met 15% af. Na hoeveel hele jaren is het aantal voor het eerst minder dan de helft?",
      "antwoord": "5",
      "uitleg": "Groeifactor 0,85. Probeer t: na 4 jaar 418, na 5 jaar 355 (grens 400). Dus na 5 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 0,93 per jaar. In 2020 kwamen er 112.000 bezoekers. Bereken het aantal bezoekers in 2010. Rond af op een geheel getal.",
      "antwoord": "231413",
      "uitleg": "Groeifactor per 10 jaar: 0,93¹⁰ ≈ 0,4840. Terug: delen: 112.000 : 0,4840 ≈ 231.413.",
      "tolerantie": 231
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 1000 · 1,04ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 1000 · 1,12ᵗ",
      "sleutelwoorden": [
        "1,12/1.12"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,04³ ≈ 1,12. De beginwaarde blijft 1000: A = 1000 · 1,12ᵗ."
    }
  ]
});
