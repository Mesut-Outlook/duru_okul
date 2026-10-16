/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 63 — §2.2 Symmetrie en top (1/2)
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-3",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 63 — §2.2 Symmetrie en top (1/2)",
  "vak": "Wiskunde · H2 Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "De parabool bij y = 2x² − 8x + 10 snijdt de y-as in (0, 10). Er is nog een punt op de parabool met y = 10. Bereken de x-coördinaat van dat punt.",
      "antwoord": "4",
      "uitleg": "2x² − 8x + 10 = 10 → 2x² − 8x = 0 → x(2x − 8) = 0 → x = 0 of x = 4. Het andere punt is (4, 10)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = 3x² − 12x + 20.",
      "antwoord": "2",
      "uitleg": "1 Uit x = 0 volgt y = 20. 2 3x² − 12x + 20 = 20 → 3x² − 12x = 0 → x(3x − 12) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = 3·2² − 12 · 2 + 20 = 8. 5 De top is (2, 8)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −½x² − 2x + 6.",
      "antwoord": "8",
      "uitleg": "1 Uit x = 0 volgt y = 6. 2 −½x² − 2x + 6 = 6 → −½x² − 2x = 0 → x(−½x − 2) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = −½·(−2)² − 2 · (−2) + 6 = 8. 5 De top is (−2, 8)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −x² + 8x − 21?",
      "uitleg": "1 Uit x = 0 volgt y = −21. 2 −x² + 8x − 21 = −21 → −x² + 8x = 0 → x(−x + 8) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = −4² + 8 · 4 − 21 = −5. 5 De top is (4, −5).",
      "opties": [
        "(4, −5)",
        "(−4, −5)",
        "(4, −21)",
        "(4, −69)"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = ½(x + 4)(x − 4) met de x-as?",
      "uitleg": "Los ½(x + 4)(x − 4) = 0 op: (x + 4) = 0 of (x − 4) = 0, dus x = −4 of x = 4. Let op het teken: bij (x + 3) hoort x = −3.",
      "opties": [
        "(4, 0) en (−4, 0)",
        "(0, −4) en (0, 4)",
        "(−4, 0) en (−4, 0)",
        "(−4, 0) en (4, 0)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x + 3)(x − 1).",
      "antwoord": "-1",
      "uitleg": "−(x + 3)(x − 1) = 0 → x = −3 of x = 1: de snijpunten met de x-as zijn (−3, 0) en (1, 0). De top ligt midden tussen x = −3 en x = 1: x = (−3 + 1) / 2 = −1. y = −(−1 − (−3))(−1 − 1) = 4. Top (−1, 4)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −2(x + 3)(x + 5).",
      "antwoord": "2",
      "uitleg": "−2(x + 3)(x + 5) = 0 → x = −3 of x = −5: de snijpunten met de x-as zijn (−3, 0) en (−5, 0). De top ligt midden tussen x = −3 en x = −5: x = (−3 + (−5)) / 2 = −4. y = −2 · (−4 − (−3))(−4 − (−5)) = 2. Top (−4, 2)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −3x² + 18x − 30.",
      "antwoord": "3",
      "uitleg": "1 Uit x = 0 volgt y = −30. 2 −3x² + 18x − 30 = −30 → −3x² + 18x = 0 → x(−3x + 18) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = −3·3² + 18 · 3 − 30 = −3. 5 De top is (3, −3)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −2x² + 20x − 56?",
      "uitleg": "1 Uit x = 0 volgt y = −56. 2 −2x² + 20x − 56 = −56 → −2x² + 20x = 0 → x(−2x + 20) = 0 → x = 0 of x = 10. 3 De x-coördinaat van de top ligt midden tussen 0 en 10: x = 5. 4 y = −2·5² + 20 · 5 − 56 = −6. 5 De top is (5, −6).",
      "opties": [
        "(5, −206)",
        "(5, −56)",
        "(5, −6)",
        "(−5, −6)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −½x² + 4x − 16 snijdt de y-as in (0, −16). Er is nog een punt op de parabool met y = −16. Bereken de x-coördinaat van dat punt.",
      "antwoord": "8",
      "uitleg": "−½x² + 4x − 16 = −16 → −½x² + 4x = 0 → x(−½x + 4) = 0 → x = 0 of x = 8. Het andere punt is (8, −16)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = ½x² + 2x + 7.",
      "antwoord": "5",
      "uitleg": "1 Uit x = 0 volgt y = 7. 2 ½x² + 2x + 7 = 7 → ½x² + 2x = 0 → x(½x + 2) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = ½·(−2)² + 2 · (−2) + 7 = 5. 5 De top is (−2, 5)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = (x + 5)(x − 9).",
      "antwoord": "2",
      "uitleg": "(x + 5)(x − 9) = 0 → x = −5 of x = 9: de snijpunten met de x-as zijn (−5, 0) en (9, 0). De top ligt midden tussen x = −5 en x = 9: x = (−5 + 9) / 2 = 2. y = (2 − (−5))(2 − 9) = −49. Top (2, −49)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = 2(x − 5)(x − 3) met de x-as?",
      "uitleg": "Los 2(x − 5)(x − 3) = 0 op: (x − 5) = 0 of (x − 3) = 0, dus x = 5 of x = 3. Let op het teken: bij (x + 3) hoort x = −3.",
      "opties": [
        "(0, 3) en (0, 5)",
        "(3, 0) en (5, 0)",
        "(3, 0) en (−5, 0)",
        "(−3, 0) en (−5, 0)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De formule h = 2a − 0,5a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "4",
      "uitleg": "2a − 0,5a² = 0 → a(2 − 0,5a) = 0 → a = 0 of a = 2 / 0,5 = 4. De tunnel is 4 m breed. Midden: a = 2, h = 2 · 2 − 0,5 · 2² = 2 m."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 3,6a − 0,6a² hoort bij de hoogte van een tunnelboog (h in meters, a in meters vanaf de linkermuur). Hoeveel meter hoog is de tunnel in het midden?",
      "antwoord": "5,4",
      "uitleg": "3,6a − 0,6a² = 0 → a(3,6 − 0,6a) = 0 → a = 0 of a = 3,6 / 0,6 = 6. De tunnel is 6 m breed. Midden: a = 3, h = 3,6 · 3 − 0,6 · 3² = 5,4 m."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = ½x² − 4x + 2?",
      "uitleg": "1 Uit x = 0 volgt y = 2. 2 ½x² − 4x + 2 = 2 → ½x² − 4x = 0 → x(½x − 4) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = ½·4² − 4 · 4 + 2 = −6. 5 De top is (4, −6).",
      "opties": [
        "(4, −6)",
        "(−4, −6)",
        "(4, 26)",
        "(4, 2)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −2(x + 5)(x − 5).",
      "antwoord": "50",
      "uitleg": "−2(x + 5)(x − 5) = 0 → x = −5 of x = 5: de snijpunten met de x-as zijn (−5, 0) en (5, 0). De top ligt midden tussen x = −5 en x = 5: x = (−5 + 5) / 2 = 0. y = −2 · (0 − (−5))(0 − 5) = 50. Top (0, 50)."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx − 10. De x-coördinaat van de top van de parabool is −4. Bereken b.",
      "antwoord": "8",
      "uitleg": "De parabool snijdt de y-as in (0, -10). Het andere punt met y = -10 ligt even ver aan de andere kant van de top: x = 2 · (−4) = −8. Invullen: (−8)² + b · (−8) + (−10) = -10 → 64 + −8b = 0 → b = 8."
    },
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,02a² − 0,4a + 27. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "25",
      "uitleg": "P ligt op hoogte 27. Zelfde hoogte: 0,02a² − 0,4a = 0 → a = 0 of a = 0,4 / 0,02 = 20. Laagste punt in het midden: a = 10, h = 25 m."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = 3x² − 12x + 7.",
      "antwoord": "-5",
      "uitleg": "1 Uit x = 0 volgt y = 7. 2 3x² − 12x + 7 = 7 → 3x² − 12x = 0 → x(3x − 12) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = 3·2² − 12 · 2 + 7 = −5. 5 De top is (2, −5)."
    }
  ]
});
