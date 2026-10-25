/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 102 — §2.2 Symmetrie en top (4/5, toetsniveau)
   Bron: Noordhoff H2 Parabolen (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h2_parabolen.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-4",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 102 — §2.2 Symmetrie en top (4/5, toetsniveau)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −2x² + 8x − 7.",
      "antwoord": "2",
      "uitleg": "1 Uit x = 0 volgt y = −7. 2 −2x² + 8x − 7 = −7 → −2x² + 8x = 0 → x(−2x + 8) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = −2·2² + 8 · 2 − 7 = 1. 5 De top is (2, 1)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −x² + 6x − 1?",
      "uitleg": "1 Uit x = 0 volgt y = −1. 2 −x² + 6x − 1 = −1 → −x² + 6x = 0 → x(−x + 6) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = −3² + 6 · 3 − 1 = 8. 5 De top is (3, 8).",
      "opties": [
        "(3, −1)",
        "(−3, 8)",
        "(3, 8)",
        "(3, −28)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = 3x² − 18x + 26.",
      "antwoord": "-1",
      "uitleg": "1 Uit x = 0 volgt y = 26. 2 3x² − 18x + 26 = 26 → 3x² − 18x = 0 → x(3x − 18) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = 3·3² − 18 · 3 + 26 = −1. 5 De top is (3, −1)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = (x − 1)(x − 6) met de x-as?",
      "uitleg": "Los (x − 1)(x − 6) = 0 op: (x − 1) = 0 of (x − 6) = 0, dus x = 1 of x = 6. De snijpunten met de x-as zijn (1, 0) en (6, 0). Let goed op de mintekens!",
      "opties": [
        "(−1, 0) en (−6, 0)",
        "(1, 0) en (−6, 0)",
        "(0, 1) en (0, 6)",
        "(1, 0) en (6, 0)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = (x − 2)(x + 8)?",
      "uitleg": "(x − 2)(x + 8) = 0 → x = 2 of x = −8: de snijpunten met de x-as zijn (2, 0) en (−8, 0). De top ligt midden tussen x = 2 en x = −8: x = (2 + (−8)) / 2 = −3. y = (−3 − 2)(−3 − (−8)) = −25. Top (−3, −25).",
      "opties": [
        "(−3, −25)",
        "(3, −25)",
        "(−3, 25)",
        "(−8, 0)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 3x² + 18x + 24 snijdt de y-as in (0, 24). Er is nog een punt op de parabool met y = 24. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-6",
      "uitleg": "3x² + 18x + 24 = 24 → 3x² + 18x = 0 → x(3x + 18) = 0 → x = 0 of x = −6. Het andere punt is (−6, 24)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = 2(x + 2)(x − 5). Een breuk of decimaal getal mag.",
      "antwoord": "1,5",
      "uitleg": "2(x + 2)(x − 5) = 0 → x = −2 of x = 5: de snijpunten met de x-as zijn (−2, 0) en (5, 0). De top ligt midden tussen x = −2 en x = 5: x = (−2 + 5) / 2 = 1,5. y = 2 · (1,5 − (−2))(1,5 − 5) = −24,5. Top (1,5, −24,5)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = ½x(x + 4).",
      "antwoord": "-2",
      "uitleg": "½x(x + 4) = 0 → x = 0 of x = −4: de snijpunten met de x-as zijn (0, 0) en (−4, 0). De top ligt midden tussen x = 0 en x = −4: x = (0 + (−4)) / 2 = −2. y = ½ · (−2 − 0)(−2 − (−4)) = −2. Top (−2, −2)."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx − 2. De x-coördinaat van de top van de parabool is −4. Bereken b.",
      "antwoord": "8",
      "uitleg": "De parabool snijdt de y-as in (0, -2). Het andere punt met y = -2 ligt even ver aan de andere kant van de top: x = 2 · (−4) = −8. Invullen: (−8)² + b · (−8) + (−2) = -2 → 64 + −8b = 0 → b = 8."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 4a − 0,5a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "8",
      "uitleg": "4a − 0,5a² = 0 → a(4 − 0,5a) = 0 → a = 0 of a = 4 / 0,5 = 8. De tunnel is 8 m breed. Midden: a = 4, h = 4 · 4 − 0,5 · 4² = 8 m."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = 3x² − 30x + 79.",
      "antwoord": "5",
      "uitleg": "1 Uit x = 0 volgt y = 79. 2 3x² − 30x + 79 = 79 → 3x² − 30x = 0 → x(3x − 30) = 0 → x = 0 of x = 10. 3 De x-coördinaat van de top ligt midden tussen 0 en 10: x = 5. 4 y = 3·5² − 30 · 5 + 79 = 4. 5 De top is (5, 4)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = x² + 6x + 1?",
      "uitleg": "1 Uit x = 0 volgt y = 1. 2 x² + 6x + 1 = 1 → x² + 6x = 0 → x(x + 6) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = (−3)² + 6 · (−3) + 1 = −8. 5 De top is (−3, −8).",
      "opties": [
        "(−3, 28)",
        "(−3, 1)",
        "(−3, −8)",
        "(3, −8)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = 2x² − 12x + 16.",
      "antwoord": "-2",
      "uitleg": "1 Uit x = 0 volgt y = 16. 2 2x² − 12x + 16 = 16 → 2x² − 12x = 0 → x(2x − 12) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = 2·3² − 12 · 3 + 16 = −2. 5 De top is (3, −2)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −x(x − 5)?",
      "uitleg": "−(x − 5)x = 0 → x = 5 of x = 0: de snijpunten met de x-as zijn (5, 0) en (0, 0). De top ligt midden tussen x = 5 en x = 0: x = (5 + 0) / 2 = 2,5. y = −(2,5 − 5)(2,5 − 0) = 6,25. Top (2,5, 6,25).",
      "opties": [
        "(2,5, 6,25)",
        "(2,5, −6,25)",
        "(−2,5, 6,25)",
        "(0, 0)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,025a² − 0,75a + 15. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "9,375",
      "uitleg": "P ligt op hoogte 15. Zelfde hoogte: 0,025a² − 0,75a = 0 → a = 0 of a = 0,75 / 0,025 = 30. Laagste punt in het midden: a = 15, h = 9,375 m."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = ½(x − 9)(x − 3) met de x-as?",
      "uitleg": "Los ½(x − 9)(x − 3) = 0 op: (x − 9) = 0 of (x − 3) = 0, dus x = 9 of x = 3. De snijpunten met de x-as zijn (3, 0) en (9, 0). Let goed op de mintekens!",
      "opties": [
        "(0, 3) en (0, 9)",
        "(3, 0) en (−9, 0)",
        "(−3, 0) en (−9, 0)",
        "(3, 0) en (9, 0)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x − 4)(x + 7). Een breuk of decimaal getal mag.",
      "antwoord": "-1,5",
      "uitleg": "−(x − 4)(x + 7) = 0 → x = 4 of x = −7: de snijpunten met de x-as zijn (4, 0) en (−7, 0). De top ligt midden tussen x = 4 en x = −7: x = (4 + (−7)) / 2 = −1,5. y = −(−1,5 − 4)(−1,5 − (−7)) = 30,25. Top (−1,5, 30,25)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −(x + 7)(x − 1).",
      "antwoord": "16",
      "uitleg": "−(x + 7)(x − 1) = 0 → x = −7 of x = 1: de snijpunten met de x-as zijn (−7, 0) en (1, 0). De top ligt midden tussen x = −7 en x = 1: x = (−7 + 1) / 2 = −3. y = −(−3 − (−7))(−3 − 1) = 16. Top (−3, 16)."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx − 12. De x-coördinaat van de top van de parabool is 2. Bereken b.",
      "antwoord": "-4",
      "uitleg": "De parabool snijdt de y-as in (0, -12). Het andere punt met y = -12 ligt even ver aan de andere kant van de top: x = 2 · 2 = 4. Invullen: 4² + b · 4 + (−12) = -12 → 16 + 4b = 0 → b = −4."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 2,4a − 0,4a² hoort bij de hoogte van een tunnelboog (h in meters, a in meters vanaf de linkermuur). Hoeveel meter hoog is de tunnel in het midden?",
      "antwoord": "3,6",
      "uitleg": "2,4a − 0,4a² = 0 → a(2,4 − 0,4a) = 0 → a = 0 of a = 2,4 / 0,4 = 6. De tunnel is 6 m breed. Midden: a = 3, h = 2,4 · 3 − 0,4 · 3² = 3,6 m."
    }
  ]
});
