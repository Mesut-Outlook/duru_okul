/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 121 — §2.2 Symmetrie en top (8/10, gemengd)
   Bron: Noordhoff H2 Parabolen §2.2 (opgaven uit het boek met andere getallen)
   Gegenereerd met tools/gen_wiskunde_parabolen_22_extra.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-8",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 121 — §2.2 Symmetrie en top (8/10, gemengd)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2x² + 20x + 43?",
      "uitleg": "1 Uit x = 0 volgt y = 43. 2 2x² + 20x + 43 = 43 → 2x² + 20x = 0 → x(2x + 20) = 0 → x = 0 of x = −10. 3 De x-coördinaat van de top ligt midden tussen 0 en −10: x = −5. 4 y = 2·(−5)² + 20 · (−5) + 43 = −7. 5 De top is (−5, −7).",
      "opties": [
        "(−5, 43)",
        "(5, −7)",
        "(−5, 193)",
        "(−5, −7)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = (x + 6)(x − 8).",
      "antwoord": "-49",
      "uitleg": "(x + 6)(x − 8) = 0 → x = −6 of x = 8: de snijpunten met de x-as zijn (−6, 0) en (8, 0). De top ligt midden tussen x = −6 en x = 8: x = (−6 + 8) / 2 = 1. y = (1 − (−6))(1 − 8) = −49. Top (1, −49)."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = 2x² + 8x + 6. Vul in: x = …",
      "antwoord": "-2",
      "uitleg": "1 Uit x = 0 volgt y = 6. 2 2x² + 8x + 6 = 6 → 2x² + 8x = 0 → x(2x + 8) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = 2·(−2)² + 8 · (−2) + 6 = −2. 5 De top is (−2, −2). De symmetrieas is de verticale lijn door de top: x = −2."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = x² + 6x + 4 heeft symmetrieas x = −3. Het punt (−1, −1) ligt op de parabool. Er is nog een punt met y = −1. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-5",
      "uitleg": "−1 ligt 2 van de as x = −3. Het gespiegelde punt ligt even ver aan de andere kant: x = −3 − 2 = −5."
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = −x² + 2x − 6 is (1, −5).",
      "antwoord": true,
      "uitleg": "Waar. 1 Uit x = 0 volgt y = −6. 2 −x² + 2x − 6 = −6 → −x² + 2x = 0 → x(−x + 2) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = −1² + 2 · 1 − 6 = −5. 5 De top is (1, −5)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = 2x² + 20x + 44.",
      "antwoord": "-5",
      "uitleg": "1 Uit x = 0 volgt y = 44. 2 2x² + 20x + 44 = 44 → 2x² + 20x = 0 → x(2x + 20) = 0 → x = 0 of x = −10. 3 De x-coördinaat van de top ligt midden tussen 0 en −10: x = −5. 4 y = 2·(−5)² + 20 · (−5) + 44 = −6. 5 De top is (−5, −6)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = −2(x + 6)(x + 5) met de x-as?",
      "uitleg": "Los −2(x + 6)(x + 5) = 0 op: (x + 6) = 0 of (x + 5) = 0, dus x = −6 of x = −5. Let op het teken: bij (x + 3) hoort x = −3.",
      "opties": [
        "(−6, 0) en (−5, 0)",
        "(6, 0) en (5, 0)",
        "(−6, 0) en (5, 0)",
        "(0, −6) en (0, −5)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = x² + 10x + 27 snijdt de y-as in (0, 27). Er is nog een punt op de parabool met y = 27. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-10",
      "uitleg": "x² + 10x + 27 = 27 → x² + 10x = 0 → x(x + 10) = 0 → x = 0 of x = −10. Het andere punt is (−10, 27)."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 4a − 0,4a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "10",
      "uitleg": "4a − 0,4a² = 0 → a(4 − 0,4a) = 0 → a = 0 of a = 4 / 0,4 = 10. De tunnel is 10 m breed. Midden: a = 5, h = 4 · 5 − 0,4 · 5² = 10 m."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −x² − 4x + 3.",
      "antwoord": "7",
      "uitleg": "1 Uit x = 0 volgt y = 3. 2 −x² − 4x + 3 = 3 → −x² − 4x = 0 → x(−x − 4) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = −(−2)² − 4 · (−2) + 3 = 7. 5 De top is (−2, 7)."
    },
    {
      "type": "invul",
      "vraag": "De punten (−11, 47) en (3, 47) liggen op dezelfde parabool. Bereken de x-coördinaat van de top.",
      "antwoord": "-4",
      "uitleg": "Beide punten hebben y = 47, dus ze liggen symmetrisch t.o.v. de symmetrieas. De top ligt midden tussen: x = (−11 + 3) / 2 = −4."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = (x − 7)(x − 1).",
      "antwoord": "4",
      "uitleg": "(x − 7)(x − 1) = 0 → x = 7 of x = 1: de snijpunten met de x-as zijn (7, 0) en (1, 0). De top ligt midden tussen x = 7 en x = 1: x = (7 + 1) / 2 = 4. y = (4 − 7)(4 − 1) = −9. Top (4, −9)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2x² − 16x + 41?",
      "uitleg": "1 Uit x = 0 volgt y = 41. 2 2x² − 16x + 41 = 41 → 2x² − 16x = 0 → x(2x − 16) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = 2·4² − 16 · 4 + 41 = 9. 5 De top is (4, 9).",
      "opties": [
        "(4, 41)",
        "(4, 137)",
        "(4, 9)",
        "(−4, 9)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx + 3. De x-coördinaat van de top van de parabool is −4. Bereken b.",
      "antwoord": "8",
      "uitleg": "De parabool snijdt de y-as in (0, 3). Het andere punt met y = 3 ligt even ver aan de andere kant van de top: x = 2 · (−4) = −8. Invullen: (−8)² + b · (−8) + 3 = 3 → 64 + −8b = 0 → b = 8."
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = x² + 2x + 9 is (1, 8).",
      "antwoord": false,
      "uitleg": "Onwaar. 1 Uit x = 0 volgt y = 9. 2 x² + 2x + 9 = 9 → x² + 2x = 0 → x(x + 2) = 0 → x = 0 of x = −2. 3 De x-coördinaat van de top ligt midden tussen 0 en −2: x = −1. 4 y = (−1)² + 2 · (−1) + 9 = 8. 5 De top is (−1, 8)."
    },
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,05a² − a + 25. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "20",
      "uitleg": "P ligt op hoogte 25. Zelfde hoogte: 0,05a² − a = 0 → a = 0 of a = 1 / 0,05 = 20. Laagste punt in het midden: a = 10, h = 20 m."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −2x² + 20x − 42.",
      "antwoord": "8",
      "uitleg": "1 Uit x = 0 volgt y = −42. 2 −2x² + 20x − 42 = −42 → −2x² + 20x = 0 → x(−2x + 20) = 0 → x = 0 of x = 10. 3 De x-coördinaat van de top ligt midden tussen 0 en 10: x = 5. 4 y = −2·5² + 20 · 5 − 42 = 8. 5 De top is (5, 8)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −2x² + 20x − 53 heeft symmetrieas x = 5. Het punt (8, −21) ligt op de parabool. Er is nog een punt met y = −21. Bereken de x-coördinaat van dat punt.",
      "antwoord": "2",
      "uitleg": "8 ligt 3 van de as x = 5. Het gespiegelde punt ligt even ver aan de andere kant: x = 5 − 3 = 2."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2x² + 8x + 3?",
      "uitleg": "1 Uit x = 0 volgt y = 3. 2 2x² + 8x + 3 = 3 → 2x² + 8x = 0 → x(2x + 8) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = 2·(−2)² + 8 · (−2) + 3 = −5. 5 De top is (−2, −5).",
      "opties": [
        "(2, −5)",
        "(−2, −5)",
        "(−2, 27)",
        "(−2, 3)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −x(x + 3). Een breuk of decimaal getal mag.",
      "antwoord": "2,25",
      "uitleg": "−(x + 3)x = 0 → x = −3 of x = 0: de snijpunten met de x-as zijn (−3, 0) en (0, 0). De top ligt midden tussen x = −3 en x = 0: x = (−3 + 0) / 2 = −1,5. y = −(−1,5 − (−3))(−1,5 − 0) = 2,25. Top (−1,5, 2,25)."
    }
  ]
});
