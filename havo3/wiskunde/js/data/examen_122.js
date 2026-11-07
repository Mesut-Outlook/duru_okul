/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 122 — §2.2 Symmetrie en top (9/10, toetsniveau)
   Bron: Noordhoff H2 Parabolen §2.2 (opgaven uit het boek met andere getallen)
   Gegenereerd met tools/gen_wiskunde_parabolen_22_extra.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-9",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 122 — §2.2 Symmetrie en top (9/10, toetsniveau)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −2(x + 7)(x + 8). Een breuk of decimaal getal mag.",
      "antwoord": "-7,5",
      "uitleg": "−2(x + 7)(x + 8) = 0 → x = −7 of x = −8: de snijpunten met de x-as zijn (−7, 0) en (−8, 0). De top ligt midden tussen x = −7 en x = −8: x = (−7 + (−8)) / 2 = −7,5. y = −2 · (−7,5 − (−7))(−7,5 − (−8)) = 0,5. Top (−7,5, 0,5)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = x² − 8x + 20?",
      "uitleg": "1 Uit x = 0 volgt y = 20. 2 x² − 8x + 20 = 20 → x² − 8x = 0 → x(x − 8) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = 4² − 8 · 4 + 20 = 4. 5 De top is (4, 4).",
      "opties": [
        "(4, 4)",
        "(−4, 4)",
        "(4, 20)",
        "(4, 68)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx + 3. De x-coördinaat van de top van de parabool is −2. Bereken b.",
      "antwoord": "4",
      "uitleg": "De parabool snijdt de y-as in (0, 3). Het andere punt met y = 3 ligt even ver aan de andere kant van de top: x = 2 · (−2) = −4. Invullen: (−4)² + b · (−4) + 3 = 3 → 16 + −4b = 0 → b = 4."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 3x² − 24x + 44 heeft symmetrieas x = 4. Het punt (0, 44) ligt op de parabool. Er is nog een punt met y = 44. Bereken de x-coördinaat van dat punt.",
      "antwoord": "8",
      "uitleg": "0 ligt 4 van de as x = 4. Het gespiegelde punt ligt even ver aan de andere kant: x = 4 + 4 = 8."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = 2x² + 8x + 14.",
      "antwoord": "6",
      "uitleg": "1 Uit x = 0 volgt y = 14. 2 2x² + 8x + 14 = 14 → 2x² + 8x = 0 → x(2x + 8) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = 2·(−2)² + 8 · (−2) + 14 = 6. 5 De top is (−2, 6)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = 2x² − 16x + 40 is (−4, 8).",
      "antwoord": false,
      "uitleg": "Onwaar. 1 Uit x = 0 volgt y = 40. 2 2x² − 16x + 40 = 40 → 2x² − 16x = 0 → x(2x − 16) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = 2·4² − 16 · 4 + 40 = 8. 5 De top is (4, 8)."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 9,6a − 0,8a² hoort bij de hoogte van een tunnelboog (h in meters, a in meters vanaf de linkermuur). Hoeveel meter hoog is de tunnel in het midden?",
      "antwoord": "28,8",
      "uitleg": "9,6a − 0,8a² = 0 → a(9,6 − 0,8a) = 0 → a = 0 of a = 9,6 / 0,8 = 12. De tunnel is 12 m breed. Midden: a = 6, h = 9,6 · 6 − 0,8 · 6² = 28,8 m."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = −2x² − 12x − 13. Vul in: x = …",
      "antwoord": "-3",
      "uitleg": "1 Uit x = 0 volgt y = −13. 2 −2x² − 12x − 13 = −13 → −2x² − 12x = 0 → x(−2x − 12) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −2·(−3)² − 12 · (−3) − 13 = 5. 5 De top is (−3, 5). De symmetrieas is de verticale lijn door de top: x = −3."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = 2(x − 8)(x + 1) met de x-as?",
      "uitleg": "Los 2(x − 8)(x + 1) = 0 op: (x − 8) = 0 of (x + 1) = 0, dus x = 8 of x = −1. Let op het teken: bij (x + 3) hoort x = −3.",
      "opties": [
        "(−1, 0) en (−8, 0)",
        "(1, 0) en (−8, 0)",
        "(−1, 0) en (8, 0)",
        "(0, −1) en (0, 8)"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −2x² + 8x + 1?",
      "uitleg": "1 Uit x = 0 volgt y = 1. 2 −2x² + 8x + 1 = 1 → −2x² + 8x = 0 → x(−2x + 8) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = −2·2² + 8 · 2 + 1 = 9. 5 De top is (2, 9).",
      "opties": [
        "(−2, 9)",
        "(2, 1)",
        "(2, −23)",
        "(2, 9)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −x² − 8x − 21 snijdt de y-as in (0, −21). Er is nog een punt op de parabool met y = −21. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-8",
      "uitleg": "−x² − 8x − 21 = −21 → −x² − 8x = 0 → x(−x − 8) = 0 → x = 0 of x = −8. Het andere punt is (−8, −21)."
    },
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,02a² − 0,8a + 28. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "20",
      "uitleg": "P ligt op hoogte 28. Zelfde hoogte: 0,02a² − 0,8a = 0 → a = 0 of a = 0,8 / 0,02 = 40. Laagste punt in het midden: a = 20, h = 20 m."
    },
    {
      "type": "invul",
      "vraag": "De punten (−9, −35) en (1, −35) liggen op dezelfde parabool. Bereken de x-coördinaat van de top.",
      "antwoord": "-4",
      "uitleg": "Beide punten hebben y = −35, dus ze liggen symmetrisch t.o.v. de symmetrieas. De top ligt midden tussen: x = (−9 + 1) / 2 = −4."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −2x(x − 6).",
      "antwoord": "18",
      "uitleg": "−2(x − 6)x = 0 → x = 6 of x = 0: de snijpunten met de x-as zijn (6, 0) en (0, 0). De top ligt midden tussen x = 6 en x = 0: x = (6 + 0) / 2 = 3. y = −2 · (3 − 6)(3 − 0) = 18. Top (3, 18)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2x² + 20x + 48?",
      "uitleg": "1 Uit x = 0 volgt y = 48. 2 2x² + 20x + 48 = 48 → 2x² + 20x = 0 → x(2x + 20) = 0 → x = 0 of x = −10. 3 De x-coördinaat van de top ligt midden tussen 0 en −10: x = −5. 4 y = 2·(−5)² + 20 · (−5) + 48 = −2. 5 De top is (−5, −2).",
      "opties": [
        "(−5, 48)",
        "(−5, −2)",
        "(−5, 198)",
        "(5, −2)"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = −3x² + 18x − 21 is (3, 6).",
      "antwoord": true,
      "uitleg": "Waar. 1 Uit x = 0 volgt y = −21. 2 −3x² + 18x − 21 = −21 → −3x² + 18x = 0 → x(−3x + 18) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = −3·3² + 18 · 3 − 21 = 6. 5 De top is (3, 6)."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx − 5. De x-coördinaat van de top van de parabool is −1. Bereken b.",
      "antwoord": "2",
      "uitleg": "De parabool snijdt de y-as in (0, -5). Het andere punt met y = -5 ligt even ver aan de andere kant van de top: x = 2 · (−1) = −2. Invullen: (−2)² + b · (−2) + (−5) = -5 → 4 + −2b = 0 → b = 2."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −2x² + 16x − 40.",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = −40. 2 −2x² + 16x − 40 = −40 → −2x² + 16x = 0 → x(−2x + 16) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = −2·4² + 16 · 4 − 40 = −8. 5 De top is (4, −8)."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 3a − 0,5a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "6",
      "uitleg": "3a − 0,5a² = 0 → a(3 − 0,5a) = 0 → a = 0 of a = 3 / 0,5 = 6. De tunnel is 6 m breed. Midden: a = 3, h = 3 · 3 − 0,5 · 3² = 4,5 m."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −x² + 6x − 3.",
      "antwoord": "6",
      "uitleg": "1 Uit x = 0 volgt y = −3. 2 −x² + 6x − 3 = −3 → −x² + 6x = 0 → x(−x + 6) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = −3² + 6 · 3 − 3 = 6. 5 De top is (3, 6)."
    }
  ]
});
