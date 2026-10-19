/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 80 — §1.5 Groeifactor en tijd (extra 2/5, oefenen)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-57",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 80 — §1.5 Groeifactor en tijd (extra 2/5, oefenen)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 1,8% per jaar. Met hoeveel procent groeit de bevolking in 50 jaar? Rond af op één decimaal.",
      "antwoord": "144,0",
      "uitleg": "Groeifactor per jaar 1,018. Per 50 jaar: 1,018⁵⁰ ≈ 2,440, dus ongeveer 144,0% groei (niet 90%).",
      "tolerantie": 0.15
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 1,6ᵗ met t in jaren. Bereken de groeifactor per 2 jaar. Rond af op drie decimalen.",
      "antwoord": "2,560",
      "uitleg": "2 jaar = 2 stappen: 1,6² ≈ 2,560.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,5 per half uur. Bereken de groeifactor per uur.",
      "antwoord": "2,25",
      "uitleg": "Per uur zijn er twee stappen: 1,5 · 1,5 = 1,5² = 2,25.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "Het totaal aantal gespeelde partijen op een schaakwebsite nam exponentieel toe met groeifactor 1,04 per maand. Op 1 oktober waren er in totaal 182.000 partijen gespeeld. Hoeveel waren dat er op 1 april? Rond af op een geheel getal.",
      "antwoord": "143837",
      "uitleg": "1 april is 6 maanden eerder. Delen door de groeifactor per 6 maanden: 182.000 : 1,04⁶ ≈ 143.837.",
      "tolerantie": 71
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,917ᵗ procent werkzaam. Na 5 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": true,
      "uitleg": "Waar. P = 100 · 0,917⁵ ≈ 64,8%. Er is dus 35,2% verdwenen, meer dan een kwart (25%)."
    },
    {
      "type": "mc",
      "vraag": "Het aantal bezoekers is N = 5000 · 0,95ᵗ met t in jaren. Welke formule hoort bij t in perioden van 2 jaar? (groeifactor in drie decimalen)",
      "uitleg": "Per 2 jaar: 0,95² ≈ 0,902. De beginwaarde 5000 blijft hetzelfde.",
      "opties": [
        "N = 5000 · 0,902ᵗ",
        "N = 5000 · 0,975ᵗ",
        "N = 5000 · 0,900ᵗ",
        "N = 10.000 · 0,95ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 0,9ᵗ is t de tijd in kwartieren. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "0,66",
      "uitleg": "In een uur passen 4 keer kwartier. Groeifactor per uur: 0,9⁴ ≈ 0,6561 ≈ 0,66.",
      "tolerantie": 0.006
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 4 miljoen mensen. Dat aantal neemt elk jaar met 4% toe. Na hoeveel hele jaren is het aantal voor het eerst meer dan 8 miljoen mensen?",
      "antwoord": "18",
      "uitleg": "Groeifactor 1,04. Probeer t: na 17 jaar 7,79, na 18 jaar 8,10 (grens 8). Dus na 18 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 1,06 per jaar. In 2020 kwamen er 86.000 bezoekers. Bereken het aantal bezoekers in 2025. Rond af op een geheel getal.",
      "antwoord": "115087",
      "uitleg": "Groeifactor per 5 jaar: 1,06⁵ ≈ 1,3382. Vooruit: vermenigvuldigen: 86.000 · 1,3382 ≈ 115.087.",
      "tolerantie": 115
    },
    {
      "type": "waaronwaar",
      "vraag": "Van een medicijn is na t dagen nog P = 100 · 0,917ᵗ procent werkzaam. Na 3 dagen is er al meer dan een kwart van het medicijn verdwenen.",
      "antwoord": false,
      "uitleg": "Onwaar. P = 100 · 0,917³ ≈ 77,1%. Er is dus 22,9% verdwenen, minder dan een kwart (25%)."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 20 · 1,019ᵗ, met t in maanden. Hoeveel dollar is de vaas na 18 maanden waard? Rond af op twee decimalen.",
      "antwoord": "28,07",
      "uitleg": "t = 18: W = 20 · 1,019¹⁸ ≈ 28,07 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "De waarde van een schilderij groeit met groeifactor 1,030 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 1,030¹² ≈ 1,426. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "1,360",
        "1,126",
        "12,360",
        "1,426"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 1,5% per jaar. Met hoeveel procent groeit de bevolking in 25 jaar? Rond af op één decimaal.",
      "antwoord": "45,1",
      "uitleg": "Groeifactor per jaar 1,015. Per 25 jaar: 1,015²⁵ ≈ 1,451, dus ongeveer 45,1% groei (niet 37,5%).",
      "tolerantie": 0.15
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal leden van een club groeit met 3% per jaar. Dat is hetzelfde als een groei van 60% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,03²⁰ ≈ 1,806, dus ongeveer 80,6% groei, niet 60%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,025 per jaar. Nu is de hoeveelheid 254.200. Hoe groot was de hoeveelheid 3 jaar eerder? Rond af op een geheel getal.",
      "antwoord": "236050",
      "uitleg": "Groeifactor per 3 jaar: 1,025³. Terugrekenen = delen: 254.200 : 1,025³ ≈ 236050.",
      "tolerantie": 118
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,4 per 10 minuten, soort B met groeifactor 12 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,4⁶ ≈ 7,5. Vergelijk met 12: soort B groeit het snelst.",
      "opties": [
        "soort A",
        "ze groeien even snel",
        "soort B",
        "dat kun je niet vergelijken"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 0,93ᵗ met t in weken. Bereken de groeifactor per 6 weken. Rond af op drie decimalen.",
      "antwoord": "0,647",
      "uitleg": "6 weken = 6 stappen: 0,93⁶ ≈ 0,647.",
      "tolerantie": 0.0015
    },
    {
      "type": "invul",
      "vraag": "In een gebied leven 12 miljoen mensen. Dat aantal neemt elk jaar met 10% af. Na hoeveel hele jaren is het aantal voor het eerst minder dan de helft?",
      "antwoord": "7",
      "uitleg": "Groeifactor 0,9. Probeer t: na 6 jaar 6,38, na 7 jaar 5,74 (grens 6). Dus na 7 jaar."
    },
    {
      "type": "invul",
      "vraag": "Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor 0,95 per jaar. In 2020 kwamen er 240.000 bezoekers. Bereken het aantal bezoekers in 2015. Rond af op een geheel getal.",
      "antwoord": "310165",
      "uitleg": "Groeifactor per 5 jaar: 0,95⁵ ≈ 0,7738. Terug: delen: 240.000 : 0,7738 ≈ 310.165.",
      "tolerantie": 310
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 1000 · 0,90ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 1000 · 0,73ᵗ",
      "sleutelwoorden": [
        "0,73/0.73"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 0,90³ ≈ 0,73. De beginwaarde blijft 1000: A = 1000 · 0,73ᵗ."
    }
  ]
});
