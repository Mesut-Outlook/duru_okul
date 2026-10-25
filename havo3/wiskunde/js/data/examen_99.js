/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 99 — §2.2 Symmetrie en top (1/5, basis)
   Bron: Noordhoff H2 Parabolen (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h2_parabolen.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-1",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 99 — §2.2 Symmetrie en top (1/5, basis)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "De parabool bij y = 2x² + 20x + 59 snijdt de y-as in (0, 59). Er is nog een punt op de parabool met y = 59. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-10",
      "uitleg": "2x² + 20x + 59 = 59 → 2x² + 20x = 0 → x(2x + 20) = 0 → x = 0 of x = −10. Het andere punt is (−10, 59)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −3x² + 18x − 34.",
      "antwoord": "3",
      "uitleg": "1 Uit x = 0 volgt y = −34. 2 −3x² + 18x − 34 = −34 → −3x² + 18x = 0 → x(−3x + 18) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = −3·3² + 18 · 3 − 34 = −7. 5 De top is (3, −7)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = 2x² + 4x + 6.",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = 6. 2 2x² + 4x + 6 = 6 → 2x² + 4x = 0 → x(2x + 4) = 0 → x = 0 of x = −2. 3 De x-coördinaat van de top ligt midden tussen 0 en −2: x = −1. 4 y = 2·(−1)² + 4 · (−1) + 6 = 4. 5 De top is (−1, 4)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −2x² − 12x − 16?",
      "uitleg": "1 Uit x = 0 volgt y = −16. 2 −2x² − 12x − 16 = −16 → −2x² − 12x = 0 → x(−2x − 12) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −2·(−3)² − 12 · (−3) − 16 = 2. 5 De top is (−3, 2).",
      "opties": [
        "(−3, −16)",
        "(3, 2)",
        "(−3, 2)",
        "(−3, −70)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Twee punten op de parabool bij een formule hebben dezelfde y-coördinaat: (−7, 53) en (3, 53). Bereken de x-coördinaat van de top van de parabool.",
      "antwoord": "-2",
      "uitleg": "De parabool is symmetrisch. De top ligt precies midden tussen x = −7 en x = 3: x = (−7 + 3) / 2 = −2."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = −½x² + 4x − 16 met top (4, −8). Vul in: x = …",
      "antwoord": "4",
      "uitleg": "De symmetrieas van de parabool bij y = −½x² + 4x − 16 is de verticale lijn door de top (4, −8). De formule is dus x = 4."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = −2(x + 8)(x − 6) met de x-as?",
      "uitleg": "Los −2(x + 8)(x − 6) = 0 op: (x + 8) = 0 of (x − 6) = 0, dus x = −8 of x = 6. De snijpunten met de x-as zijn (−8, 0) en (6, 0). Let goed op de mintekens!",
      "opties": [
        "(0, −8) en (0, 6)",
        "(−8, 0) en (6, 0)",
        "(−8, 0) en (−6, 0)",
        "(8, 0) en (−6, 0)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = 2(x + 6)(x + 2).",
      "antwoord": "-4",
      "uitleg": "2(x + 6)(x + 2) = 0 → x = −6 of x = −2: de snijpunten met de x-as zijn (−6, 0) en (−2, 0). De top ligt midden tussen x = −6 en x = −2: x = (−6 + (−2)) / 2 = −4. y = 2 · (−4 − (−6))(−4 − (−2)) = −8. Top (−4, −8)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2(x + 8)(x + 6)?",
      "uitleg": "2(x + 8)(x + 6) = 0 → x = −8 of x = −6: de snijpunten met de x-as zijn (−8, 0) en (−6, 0). De top ligt midden tussen x = −8 en x = −6: x = (−8 + (−6)) / 2 = −7. y = 2 · (−7 − (−8))(−7 − (−6)) = −2. Top (−7, −2).",
      "opties": [
        "(−7, 2)",
        "(−8, 0)",
        "(7, −2)",
        "(−7, −2)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −3x² − 18x − 33 snijdt de y-as in (0, −33). Er is nog een punt op de parabool met y = −33. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-6",
      "uitleg": "−3x² − 18x − 33 = −33 → −3x² − 18x = 0 → x(−3x − 18) = 0 → x = 0 of x = −6. Het andere punt is (−6, −33)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −3x² − 12x − 18.",
      "antwoord": "-2",
      "uitleg": "1 Uit x = 0 volgt y = −18. 2 −3x² − 12x − 18 = −18 → −3x² − 12x = 0 → x(−3x − 12) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = −3·(−2)² − 12 · (−2) − 18 = −6. 5 De top is (−2, −6)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = 3x² + 12x + 16.",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = 16. 2 3x² + 12x + 16 = 16 → 3x² + 12x = 0 → x(3x + 12) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = 3·(−2)² + 12 · (−2) + 16 = 4. 5 De top is (−2, 4)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −x² − 2x − 3?",
      "uitleg": "1 Uit x = 0 volgt y = −3. 2 −x² − 2x − 3 = −3 → −x² − 2x = 0 → x(−x − 2) = 0 → x = 0 of x = −2. 3 De x-coördinaat van de top ligt midden tussen 0 en −2: x = −1. 4 y = −(−1)² − 2 · (−1) − 3 = −2. 5 De top is (−1, −2).",
      "opties": [
        "(−1, −3)",
        "(1, −2)",
        "(−1, −6)",
        "(−1, −2)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Twee punten op de parabool bij een formule hebben dezelfde y-coördinaat: (−7, 59) en (3, 59). Bereken de x-coördinaat van de top van de parabool.",
      "antwoord": "-2",
      "uitleg": "De parabool is symmetrisch. De top ligt precies midden tussen x = −7 en x = 3: x = (−7 + 3) / 2 = −2."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = 3x² − 12x + 19 met top (2, 7). Vul in: x = …",
      "antwoord": "2",
      "uitleg": "De symmetrieas van de parabool bij y = 3x² − 12x + 19 is de verticale lijn door de top (2, 7). De formule is dus x = 2."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = 2(x − 1)(x + 6) met de x-as?",
      "uitleg": "Los 2(x − 1)(x + 6) = 0 op: (x − 1) = 0 of (x + 6) = 0, dus x = 1 of x = −6. De snijpunten met de x-as zijn (−6, 0) en (1, 0). Let goed op de mintekens!",
      "opties": [
        "(−6, 0) en (−1, 0)",
        "(6, 0) en (−1, 0)",
        "(−6, 0) en (1, 0)",
        "(0, −6) en (0, 1)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = ½x² + 2x + 3 snijdt de y-as in (0, 3). Er is nog een punt op de parabool met y = 3. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-4",
      "uitleg": "½x² + 2x + 3 = 3 → ½x² + 2x = 0 → x(½x + 2) = 0 → x = 0 of x = −4. Het andere punt is (−4, 3)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = ½x² + 2x + 5.",
      "antwoord": "-2",
      "uitleg": "1 Uit x = 0 volgt y = 5. 2 ½x² + 2x + 5 = 5 → ½x² + 2x = 0 → x(½x + 2) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = ½·(−2)² + 2 · (−2) + 5 = 3. 5 De top is (−2, 3)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = 3x² + 24x + 52.",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = 52. 2 3x² + 24x + 52 = 52 → 3x² + 24x = 0 → x(3x + 24) = 0 → x = 0 of x = −8. 3 De x-coördinaat van de top ligt midden tussen 0 en −8: x = −4. 4 y = 3·(−4)² + 24 · (−4) + 52 = 4. 5 De top is (−4, 4)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2(x − 2)(x + 3)?",
      "uitleg": "2(x − 2)(x + 3) = 0 → x = 2 of x = −3: de snijpunten met de x-as zijn (2, 0) en (−3, 0). De top ligt midden tussen x = 2 en x = −3: x = (2 + (−3)) / 2 = −0,5. y = 2 · (−0,5 − 2)(−0,5 − (−3)) = −12,5. Top (−0,5, −12,5).",
      "opties": [
        "(−0,5, −12,5)",
        "(0,5, −12,5)",
        "(−3, 0)",
        "(−0,5, 12,5)"
      ],
      "antwoord": 0
    }
  ]
});
