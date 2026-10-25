/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 100 — §2.2 Symmetrie en top (2/5, oefenen)
   Bron: Noordhoff H2 Parabolen (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h2_parabolen.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-2",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 100 — §2.2 Symmetrie en top (2/5, oefenen)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = ½(x + 5)(x + 4) met de x-as?",
      "uitleg": "Los ½(x + 5)(x + 4) = 0 op: (x + 5) = 0 of (x + 4) = 0, dus x = −5 of x = −4. De snijpunten met de x-as zijn (−5, 0) en (−4, 0). Let goed op de mintekens!",
      "opties": [
        "(−5, 0) en (−4, 0)",
        "(0, −5) en (0, −4)",
        "(5, 0) en (4, 0)",
        "(−5, 0) en (4, 0)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = ½(x − 5)(x + 5).",
      "antwoord": "0",
      "uitleg": "½(x − 5)(x + 5) = 0 → x = 5 of x = −5: de snijpunten met de x-as zijn (5, 0) en (−5, 0). De top ligt midden tussen x = 5 en x = −5: x = (5 + (−5)) / 2 = 0. y = ½ · (0 − 5)(0 − (−5)) = −12,5. Top (0, −12,5)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = 2(x − 7)(x + 3).",
      "antwoord": "-50",
      "uitleg": "2(x − 7)(x + 3) = 0 → x = 7 of x = −3: de snijpunten met de x-as zijn (7, 0) en (−3, 0). De top ligt midden tussen x = 7 en x = −3: x = (7 + (−3)) / 2 = 2. y = 2 · (2 − 7)(2 − (−3)) = −50. Top (2, −50)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −2(x + 2)(x + 1)?",
      "uitleg": "−2(x + 2)(x + 1) = 0 → x = −2 of x = −1: de snijpunten met de x-as zijn (−2, 0) en (−1, 0). De top ligt midden tussen x = −2 en x = −1: x = (−2 + (−1)) / 2 = −1,5. y = −2 · (−1,5 − (−2))(−1,5 − (−1)) = 0,5. Top (−1,5, 0,5).",
      "opties": [
        "(−2, 0)",
        "(−1,5, 0,5)",
        "(1,5, 0,5)",
        "(−1,5, −0,5)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −3x² − 18x − 25.",
      "antwoord": "-3",
      "uitleg": "1 Uit x = 0 volgt y = −25. 2 −3x² − 18x − 25 = −25 → −3x² − 18x = 0 → x(−3x − 18) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −3·(−3)² − 18 · (−3) − 25 = 2. 5 De top is (−3, 2)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −x² − 10x − 27.",
      "antwoord": "-2",
      "uitleg": "1 Uit x = 0 volgt y = −27. 2 −x² − 10x − 27 = −27 → −x² − 10x = 0 → x(−x − 10) = 0 → x = 0 of x = −10. 3 De x-coördinaat van de top ligt midden tussen 0 en −10: x = −5. 4 y = −(−5)² − 10 · (−5) − 27 = −2. 5 De top is (−5, −2)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = x² + 8x + 17 snijdt de y-as in (0, 17). Er is nog een punt op de parabool met y = 17. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-8",
      "uitleg": "x² + 8x + 17 = 17 → x² + 8x = 0 → x(x + 8) = 0 → x = 0 of x = −8. Het andere punt is (−8, 17)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −2x² + 16x − 24?",
      "uitleg": "1 Uit x = 0 volgt y = −24. 2 −2x² + 16x − 24 = −24 → −2x² + 16x = 0 → x(−2x + 16) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = −2·4² + 16 · 4 − 24 = 8. 5 De top is (4, 8).",
      "opties": [
        "(−4, 8)",
        "(4, −120)",
        "(4, 8)",
        "(4, −24)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De symmetrieas van een parabool is de lijn x = 6. Het punt (0, 17) ligt op de parabool. Er is nog een punt op de parabool met y = 17. Bereken de x-coördinaat van dat punt.",
      "antwoord": "12",
      "uitleg": "De symmetrieas is x = 6. Het punt (0, 17) ligt op afstand 6 links van de symmetrieas. Het andere punt met dezelfde hoogte ligt op gelijke afstand rechts van de as: x = 6 + 6 = 12."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x − 3)(x − 9).",
      "antwoord": "6",
      "uitleg": "−(x − 3)(x − 9) = 0 → x = 3 of x = 9: de snijpunten met de x-as zijn (3, 0) en (9, 0). De top ligt midden tussen x = 3 en x = 9: x = (3 + 9) / 2 = 6. y = −(6 − 3)(6 − 9) = 9. Top (6, 9)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = ½(x + 5)(x − 5). Een breuk of decimaal getal mag.",
      "antwoord": "-12,5",
      "uitleg": "½(x + 5)(x − 5) = 0 → x = −5 of x = 5: de snijpunten met de x-as zijn (−5, 0) en (5, 0). De top ligt midden tussen x = −5 en x = 5: x = (−5 + 5) / 2 = 0. y = ½ · (0 − (−5))(0 − 5) = −12,5. Top (0, −12,5)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = 2(x + 3)(x − 5) met de x-as?",
      "uitleg": "Los 2(x + 3)(x − 5) = 0 op: (x + 3) = 0 of (x − 5) = 0, dus x = −3 of x = 5. De snijpunten met de x-as zijn (−3, 0) en (5, 0). Let goed op de mintekens!",
      "opties": [
        "(−3, 0) en (−5, 0)",
        "(−3, 0) en (5, 0)",
        "(3, 0) en (−5, 0)",
        "(0, −3) en (0, 5)"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2(x − 9)(x − 4)?",
      "uitleg": "2(x − 9)(x − 4) = 0 → x = 9 of x = 4: de snijpunten met de x-as zijn (9, 0) en (4, 0). De top ligt midden tussen x = 9 en x = 4: x = (9 + 4) / 2 = 6,5. y = 2 · (6,5 − 9)(6,5 − 4) = −12,5. Top (6,5, −12,5).",
      "opties": [
        "(6,5, −12,5)",
        "(−6,5, −12,5)",
        "(4, 0)",
        "(6,5, 12,5)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −3x² − 18x − 26.",
      "antwoord": "-3",
      "uitleg": "1 Uit x = 0 volgt y = −26. 2 −3x² − 18x − 26 = −26 → −3x² − 18x = 0 → x(−3x − 18) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −3·(−3)² − 18 · (−3) − 26 = 1. 5 De top is (−3, 1)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −x² − 6x − 1.",
      "antwoord": "8",
      "uitleg": "1 Uit x = 0 volgt y = −1. 2 −x² − 6x − 1 = −1 → −x² − 6x = 0 → x(−x − 6) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −(−3)² − 6 · (−3) − 1 = 8. 5 De top is (−3, 8)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = ½x² + 2x − 1 snijdt de y-as in (0, −1). Er is nog een punt op de parabool met y = −1. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-4",
      "uitleg": "½x² + 2x − 1 = −1 → ½x² + 2x = 0 → x(½x + 2) = 0 → x = 0 of x = −4. Het andere punt is (−4, −1)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −3x² − 24x − 54?",
      "uitleg": "1 Uit x = 0 volgt y = −54. 2 −3x² − 24x − 54 = −54 → −3x² − 24x = 0 → x(−3x − 24) = 0 → x = 0 of x = −8. 3 De x-coördinaat van de top ligt midden tussen 0 en −8: x = −4. 4 y = −3·(−4)² − 24 · (−4) − 54 = −6. 5 De top is (−4, −6).",
      "opties": [
        "(−4, −198)",
        "(4, −6)",
        "(−4, −6)",
        "(−4, −54)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De symmetrieas van een parabool is de lijn x = 0. Het punt (−2, -17) ligt op de parabool. Er is nog een punt op de parabool met y = -17. Bereken de x-coördinaat van dat punt.",
      "antwoord": "2",
      "uitleg": "De symmetrieas is x = 0. Het punt (−2, -17) ligt op afstand 2 links van de symmetrieas. Het andere punt met dezelfde hoogte ligt op gelijke afstand rechts van de as: x = 0 + 2 = 2."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x + 8)(x − 5). Een breuk of decimaal getal mag.",
      "antwoord": "-1,5",
      "uitleg": "−(x + 8)(x − 5) = 0 → x = −8 of x = 5: de snijpunten met de x-as zijn (−8, 0) en (5, 0). De top ligt midden tussen x = −8 en x = 5: x = (−8 + 5) / 2 = −1,5. y = −(−1,5 − (−8))(−1,5 − 5) = 42,25. Top (−1,5, 42,25)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −(x + 1)(x − 3).",
      "antwoord": "4",
      "uitleg": "−(x + 1)(x − 3) = 0 → x = −1 of x = 3: de snijpunten met de x-as zijn (−1, 0) en (3, 0). De top ligt midden tussen x = −1 en x = 3: x = (−1 + 3) / 2 = 1. y = −(1 − (−1))(1 − 3) = 4. Top (1, 4)."
    }
  ]
});
