/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 103 — §2.2 Symmetrie en top (5/5, eindniveau)
   Bron: Noordhoff H2 Parabolen (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h2_parabolen.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-5",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 103 — §2.2 Symmetrie en top (5/5, eindniveau)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = ½x² + 4x?",
      "uitleg": "1 Uit x = 0 volgt y = 0. 2 ½x² + 4x = 0 → ½x² + 4x = 0 → x(½x + 4) = 0 → x = 0 of x = −8. 3 De x-coördinaat van de top ligt midden tussen 0 en −8: x = −4. 4 y = ½·(−4)² + 4 · (−4) = −8. 5 De top is (−4, −8).",
      "opties": [
        "(−4, −8)",
        "(−4, 0)",
        "(4, −8)",
        "(−4, 24)"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2(x + 6)(x − 2)?",
      "uitleg": "2(x + 6)(x − 2) = 0 → x = −6 of x = 2: de snijpunten met de x-as zijn (−6, 0) en (2, 0). De top ligt midden tussen x = −6 en x = 2: x = (−6 + 2) / 2 = −2. y = 2 · (−2 − (−6))(−2 − 2) = −32. Top (−2, −32).",
      "opties": [
        "(−2, 32)",
        "(−6, 0)",
        "(2, −32)",
        "(−2, −32)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = (x + 2)(x + 8) met de x-as?",
      "uitleg": "Los (x + 2)(x + 8) = 0 op: (x + 2) = 0 of (x + 8) = 0, dus x = −2 of x = −8. De snijpunten met de x-as zijn (−8, 0) en (−2, 0). Let goed op de mintekens!",
      "opties": [
        "(−8, 0) en (−2, 0)",
        "(−8, 0) en (2, 0)",
        "(8, 0) en (2, 0)",
        "(0, −8) en (0, −2)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = 3x² − 6x + 4.",
      "antwoord": "1",
      "uitleg": "1 Uit x = 0 volgt y = 4. 2 3x² − 6x + 4 = 4 → 3x² − 6x = 0 → x(3x − 6) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = 3·1² − 6 · 1 + 4 = 1. 5 De top is (1, 1)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = x² + 6x + 10.",
      "antwoord": "1",
      "uitleg": "1 Uit x = 0 volgt y = 10. 2 x² + 6x + 10 = 10 → x² + 6x = 0 → x(x + 6) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = (−3)² + 6 · (−3) + 10 = 1. 5 De top is (−3, 1)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 3x² + 18x + 19 snijdt de y-as in (0, 19). Er is nog een punt op de parabool met y = 19. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-6",
      "uitleg": "3x² + 18x + 19 = 19 → 3x² + 18x = 0 → x(3x + 18) = 0 → x = 0 of x = −6. Het andere punt is (−6, 19)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = 2(x + 6)(x + 9). Een breuk of decimaal getal mag.",
      "antwoord": "-7,5",
      "uitleg": "2(x + 6)(x + 9) = 0 → x = −6 of x = −9: de snijpunten met de x-as zijn (−6, 0) en (−9, 0). De top ligt midden tussen x = −6 en x = −9: x = (−6 + (−9)) / 2 = −7,5. y = 2 · (−7,5 − (−6))(−7,5 − (−9)) = −4,5. Top (−7,5, −4,5)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = ½(x + 4)(x + 6). Een breuk of decimaal getal mag.",
      "antwoord": "-0,5",
      "uitleg": "½(x + 4)(x + 6) = 0 → x = −4 of x = −6: de snijpunten met de x-as zijn (−4, 0) en (−6, 0). De top ligt midden tussen x = −4 en x = −6: x = (−4 + (−6)) / 2 = −5. y = ½ · (−5 − (−4))(−5 − (−6)) = −0,5. Top (−5, −0,5)."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx + 2. De x-coördinaat van de top van de parabool is 4. Bereken b.",
      "antwoord": "-8",
      "uitleg": "De parabool snijdt de y-as in (0, 2). Het andere punt met y = 2 ligt even ver aan de andere kant van de top: x = 2 · 4 = 8. Invullen: 8² + b · 8 + 2 = 2 → 64 + 8b = 0 → b = −8."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 6a − 0,5a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "12",
      "uitleg": "6a − 0,5a² = 0 → a(6 − 0,5a) = 0 → a = 0 of a = 6 / 0,5 = 12. De tunnel is 12 m breed. Midden: a = 6, h = 6 · 6 − 0,5 · 6² = 18 m."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −3x² − 18x − 26?",
      "uitleg": "1 Uit x = 0 volgt y = −26. 2 −3x² − 18x − 26 = −26 → −3x² − 18x = 0 → x(−3x − 18) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −3·(−3)² − 18 · (−3) − 26 = 1. 5 De top is (−3, 1).",
      "opties": [
        "(−3, −26)",
        "(−3, 1)",
        "(3, 1)",
        "(−3, −107)"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = (x − 2)(x − 6)?",
      "uitleg": "(x − 2)(x − 6) = 0 → x = 2 of x = 6: de snijpunten met de x-as zijn (2, 0) en (6, 0). De top ligt midden tussen x = 2 en x = 6: x = (2 + 6) / 2 = 4. y = (4 − 2)(4 − 6) = −4. Top (4, −4).",
      "opties": [
        "(4, 4)",
        "(−4, −4)",
        "(2, 0)",
        "(4, −4)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = ½(x − 1)(x − 5) met de x-as?",
      "uitleg": "Los ½(x − 1)(x − 5) = 0 op: (x − 1) = 0 of (x − 5) = 0, dus x = 1 of x = 5. De snijpunten met de x-as zijn (1, 0) en (5, 0). Let goed op de mintekens!",
      "opties": [
        "(−1, 0) en (−5, 0)",
        "(1, 0) en (5, 0)",
        "(1, 0) en (−5, 0)",
        "(0, 1) en (0, 5)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −2x² + 12x − 9.",
      "antwoord": "3",
      "uitleg": "1 Uit x = 0 volgt y = −9. 2 −2x² + 12x − 9 = −9 → −2x² + 12x = 0 → x(−2x + 12) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = −2·3² + 12 · 3 − 9 = 9. 5 De top is (3, 9)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = ½x² − 2x − 3.",
      "antwoord": "-5",
      "uitleg": "1 Uit x = 0 volgt y = −3. 2 ½x² − 2x − 3 = −3 → ½x² − 2x = 0 → x(½x − 2) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = ½·2² − 2 · 2 − 3 = −5. 5 De top is (2, −5)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 2x² − 16x + 29 snijdt de y-as in (0, 29). Er is nog een punt op de parabool met y = 29. Bereken de x-coördinaat van dat punt.",
      "antwoord": "8",
      "uitleg": "2x² − 16x + 29 = 29 → 2x² − 16x = 0 → x(2x − 16) = 0 → x = 0 of x = 8. Het andere punt is (8, 29)."
    },
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,05a² − 2a + 28. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "8",
      "uitleg": "P ligt op hoogte 28. Zelfde hoogte: 0,05a² − 2a = 0 → a = 0 of a = 2 / 0,05 = 40. Laagste punt in het midden: a = 20, h = 8 m."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx − 10. De x-coördinaat van de top van de parabool is 1. Bereken b.",
      "antwoord": "-2",
      "uitleg": "De parabool snijdt de y-as in (0, -10). Het andere punt met y = -10 ligt even ver aan de andere kant van de top: x = 2 · 1 = 2. Invullen: 2² + b · 2 + (−10) = -10 → 4 + 2b = 0 → b = −2."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 3a − 0,5a² hoort bij de hoogte van een tunnelboog (h in meters, a in meters vanaf de linkermuur). Hoeveel meter hoog is de tunnel in het midden?",
      "antwoord": "4,5",
      "uitleg": "3a − 0,5a² = 0 → a(3 − 0,5a) = 0 → a = 0 of a = 3 / 0,5 = 6. De tunnel is 6 m breed. Midden: a = 3, h = 3 · 3 − 0,5 · 3² = 4,5 m."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −2x(x − 8).",
      "antwoord": "4",
      "uitleg": "−2x(x − 8) = 0 → x = 0 of x = 8: de snijpunten met de x-as zijn (0, 0) en (8, 0). De top ligt midden tussen x = 0 en x = 8: x = (0 + 8) / 2 = 4. y = −2 · (4 − 0)(4 − 8) = 32. Top (4, 32)."
    }
  ]
});
