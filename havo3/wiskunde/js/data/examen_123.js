/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 123 — §2.2 Symmetrie en top (10/10, eindniveau)
   Bron: Noordhoff H2 Parabolen §2.2 (opgaven uit het boek met andere getallen)
   Gegenereerd met tools/gen_wiskunde_parabolen_22_extra.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-10",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 123 — §2.2 Symmetrie en top (10/10, eindniveau)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx + 3. De x-coördinaat van de top van de parabool is −3. Bereken b.",
      "antwoord": "6",
      "uitleg": "De parabool snijdt de y-as in (0, 3). Het andere punt met y = 3 ligt even ver aan de andere kant van de top: x = 2 · (−3) = −6. Invullen: (−6)² + b · (−6) + 3 = 3 → 36 + −6b = 0 → b = 6."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = x² − 2x − 1?",
      "uitleg": "1 Uit x = 0 volgt y = −1. 2 x² − 2x − 1 = −1 → x² − 2x = 0 → x(x − 2) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = 1² − 2 · 1 − 1 = −2. 5 De top is (1, −2).",
      "opties": [
        "(1, −2)",
        "(1, 2)",
        "(1, −1)",
        "(−1, −2)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,05a² − 1,2a + 36. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "28,8",
      "uitleg": "P ligt op hoogte 36. Zelfde hoogte: 0,05a² − 1,2a = 0 → a = 0 of a = 1,2 / 0,05 = 24. Laagste punt in het midden: a = 12, h = 28,8 m."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −(x + 2)(x − 3). Een breuk of decimaal getal mag.",
      "antwoord": "6,25",
      "uitleg": "−(x + 2)(x − 3) = 0 → x = −2 of x = 3: de snijpunten met de x-as zijn (−2, 0) en (3, 0). De top ligt midden tussen x = −2 en x = 3: x = (−2 + 3) / 2 = 0,5. y = −(0,5 − (−2))(0,5 − 3) = 6,25. Top (0,5, 6,25)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −½x² + 2x + 4 heeft symmetrieas x = 2. Het punt (6, −2) ligt op de parabool. Er is nog een punt met y = −2. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-2",
      "uitleg": "6 ligt 4 van de as x = 2. Het gespiegelde punt ligt even ver aan de andere kant: x = 2 − 4 = −2."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 8a − 0,8a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "10",
      "uitleg": "8a − 0,8a² = 0 → a(8 − 0,8a) = 0 → a = 0 of a = 8 / 0,8 = 10. De tunnel is 10 m breed. Midden: a = 5, h = 8 · 5 − 0,8 · 5² = 20 m."
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = −3x² + 30x − 81 is (5, −6).",
      "antwoord": true,
      "uitleg": "Waar. 1 Uit x = 0 volgt y = −81. 2 −3x² + 30x − 81 = −81 → −3x² + 30x = 0 → x(−3x + 30) = 0 → x = 0 of x = 10. 3 De x-coördinaat van de top ligt midden tussen 0 en 10: x = 5. 4 y = −3·5² + 30 · 5 − 81 = −6. 5 De top is (5, −6)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = x² + 10x + 16.",
      "antwoord": "-9",
      "uitleg": "1 Uit x = 0 volgt y = 16. 2 x² + 10x + 16 = 16 → x² + 10x = 0 → x(x + 10) = 0 → x = 0 of x = −10. 3 De x-coördinaat van de top ligt midden tussen 0 en −10: x = −5. 4 y = (−5)² + 10 · (−5) + 16 = −9. 5 De top is (−5, −9)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = −(x + 2)(x − 5) met de x-as?",
      "uitleg": "Los −(x + 2)(x − 5) = 0 op: (x + 2) = 0 of (x − 5) = 0, dus x = −2 of x = 5. Let op het teken: bij (x + 3) hoort x = −3.",
      "opties": [
        "(−2, 0) en (−5, 0)",
        "(−2, 0) en (5, 0)",
        "(0, −2) en (0, 5)",
        "(2, 0) en (−5, 0)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = (x + 8)(x + 3). Een breuk of decimaal getal mag.",
      "antwoord": "-5,5",
      "uitleg": "(x + 8)(x + 3) = 0 → x = −8 of x = −3: de snijpunten met de x-as zijn (−8, 0) en (−3, 0). De top ligt midden tussen x = −8 en x = −3: x = (−8 + (−3)) / 2 = −5,5. y = (−5,5 − (−8))(−5,5 − (−3)) = −6,25. Top (−5,5, −6,25)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 3x² − 18x + 26?",
      "uitleg": "1 Uit x = 0 volgt y = 26. 2 3x² − 18x + 26 = 26 → 3x² − 18x = 0 → x(3x − 18) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = 3·3² − 18 · 3 + 26 = −1. 5 De top is (3, −1).",
      "opties": [
        "(3, 26)",
        "(3, 107)",
        "(−3, −1)",
        "(3, −1)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De formule h = 6,4a − 0,8a² hoort bij de hoogte van een tunnelboog (h in meters, a in meters vanaf de linkermuur). Hoeveel meter hoog is de tunnel in het midden?",
      "antwoord": "12,8",
      "uitleg": "6,4a − 0,8a² = 0 → a(6,4 − 0,8a) = 0 → a = 0 of a = 6,4 / 0,8 = 8. De tunnel is 8 m breed. Midden: a = 4, h = 6,4 · 4 − 0,8 · 4² = 12,8 m."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx + 4. De x-coördinaat van de top van de parabool is −1. Bereken b.",
      "antwoord": "2",
      "uitleg": "De parabool snijdt de y-as in (0, 4). Het andere punt met y = 4 ligt even ver aan de andere kant van de top: x = 2 · (−1) = −2. Invullen: (−2)² + b · (−2) + 4 = 4 → 4 + −2b = 0 → b = 2."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = ½x² − 4x + 8. Vul in: x = …",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = 8. 2 ½x² − 4x + 8 = 8 → ½x² − 4x = 0 → x(½x − 4) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = ½·4² − 4 · 4 + 8 = 0. 5 De top is (4, 0). De symmetrieas is de verticale lijn door de top: x = 4."
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = 2x² + 4x − 4 is (1, −6).",
      "antwoord": false,
      "uitleg": "Onwaar. 1 Uit x = 0 volgt y = −4. 2 2x² + 4x − 4 = −4 → 2x² + 4x = 0 → x(2x + 4) = 0 → x = 0 of x = −2. 3 De x-coördinaat van de top ligt midden tussen 0 en −2: x = −1. 4 y = 2·(−1)² + 4 · (−1) − 4 = −6. 5 De top is (−1, −6)."
    },
    {
      "type": "invul",
      "vraag": "De punten (−12, 56) en (4, 56) liggen op dezelfde parabool. Bereken de x-coördinaat van de top.",
      "antwoord": "-4",
      "uitleg": "Beide punten hebben y = 56, dus ze liggen symmetrisch t.o.v. de symmetrieas. De top ligt midden tussen: x = (−12 + 4) / 2 = −4."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 3x² + 18x + 36?",
      "uitleg": "1 Uit x = 0 volgt y = 36. 2 3x² + 18x + 36 = 36 → 3x² + 18x = 0 → x(3x + 18) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = 3·(−3)² + 18 · (−3) + 36 = 9. 5 De top is (−3, 9).",
      "opties": [
        "(−3, 36)",
        "(3, 9)",
        "(−3, 9)",
        "(−3, 117)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,02a² − 0,4a + 28. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "26",
      "uitleg": "P ligt op hoogte 28. Zelfde hoogte: 0,02a² − 0,4a = 0 → a = 0 of a = 0,4 / 0,02 = 20. Laagste punt in het midden: a = 10, h = 26 m."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = 2(x + 7)(x + 9).",
      "antwoord": "-2",
      "uitleg": "2(x + 7)(x + 9) = 0 → x = −7 of x = −9: de snijpunten met de x-as zijn (−7, 0) en (−9, 0). De top ligt midden tussen x = −7 en x = −9: x = (−7 + (−9)) / 2 = −8. y = 2 · (−8 − (−7))(−8 − (−9)) = −2. Top (−8, −2)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −x² − 4x − 1.",
      "antwoord": "3",
      "uitleg": "1 Uit x = 0 volgt y = −1. 2 −x² − 4x − 1 = −1 → −x² − 4x = 0 → x(−x − 4) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = −(−2)² − 4 · (−2) − 1 = 3. 5 De top is (−2, 3)."
    }
  ]
});
