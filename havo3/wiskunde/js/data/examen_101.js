/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 101 — §2.2 Symmetrie en top (3/5, gemengd)
   Bron: Noordhoff H2 Parabolen (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h2_parabolen.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-3",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 101 — §2.2 Symmetrie en top (3/5, gemengd)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −x² + 10x − 21.",
      "antwoord": "5",
      "uitleg": "1 Uit x = 0 volgt y = −21. 2 −x² + 10x − 21 = −21 → −x² + 10x = 0 → x(−x + 10) = 0 → x = 0 of x = 10. 3 De x-coördinaat van de top ligt midden tussen 0 en 10: x = 5. 4 y = −5² + 10 · 5 − 21 = 4. 5 De top is (5, 4)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −x² + 8x − 22.",
      "antwoord": "-6",
      "uitleg": "1 Uit x = 0 volgt y = −22. 2 −x² + 8x − 22 = −22 → −x² + 8x = 0 → x(−x + 8) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = −4² + 8 · 4 − 22 = −6. 5 De top is (4, −6)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = x² + 4x + 6?",
      "uitleg": "1 Uit x = 0 volgt y = 6. 2 x² + 4x + 6 = 6 → x² + 4x = 0 → x(x + 4) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = (−2)² + 4 · (−2) + 6 = 2. 5 De top is (−2, 2).",
      "opties": [
        "(−2, 2)",
        "(2, 2)",
        "(−2, 6)",
        "(−2, 18)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 3x² − 18x + 33 snijdt de y-as in (0, 33). Er is nog een punt op de parabool met y = 33. Bereken de x-coördinaat van dat punt.",
      "antwoord": "6",
      "uitleg": "3x² − 18x + 33 = 33 → 3x² − 18x = 0 → x(3x − 18) = 0 → x = 0 of x = 6. Het andere punt is (6, 33)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = ½(x − 7)(x − 9).",
      "antwoord": "8",
      "uitleg": "½(x − 7)(x − 9) = 0 → x = 7 of x = 9: de snijpunten met de x-as zijn (7, 0) en (9, 0). De top ligt midden tussen x = 7 en x = 9: x = (7 + 9) / 2 = 8. y = ½ · (8 − 7)(8 − 9) = −0,5. Top (8, −0,5)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = −2(x + 7)(x + 5) met de x-as?",
      "uitleg": "Los −2(x + 7)(x + 5) = 0 op: (x + 7) = 0 of (x + 5) = 0, dus x = −7 of x = −5. De snijpunten met de x-as zijn (−7, 0) en (−5, 0). Let goed op de mintekens!",
      "opties": [
        "(0, −7) en (0, −5)",
        "(7, 0) en (5, 0)",
        "(−7, 0) en (−5, 0)",
        "(−7, 0) en (5, 0)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −(x − 8)(x + 3). Een breuk of decimaal getal mag.",
      "antwoord": "30,25",
      "uitleg": "−(x − 8)(x + 3) = 0 → x = 8 of x = −3: de snijpunten met de x-as zijn (8, 0) en (−3, 0). De top ligt midden tussen x = 8 en x = −3: x = (8 + (−3)) / 2 = 2,5. y = −(2,5 − 8)(2,5 − (−3)) = 30,25. Top (2,5, 30,25)."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx + 8. De x-coördinaat van de top van de parabool is 3. Bereken b.",
      "antwoord": "-6",
      "uitleg": "De parabool snijdt de y-as in (0, 8). Het andere punt met y = 8 ligt even ver aan de andere kant van de top: x = 2 · 3 = 6. Invullen: 6² + b · 6 + 8 = 8 → 36 + 6b = 0 → b = −6."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 2,5a − 0,25a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "10",
      "uitleg": "2,5a − 0,25a² = 0 → a(2,5 − 0,25a) = 0 → a = 0 of a = 2,5 / 0,25 = 10. De tunnel is 10 m breed. Midden: a = 5, h = 2,5 · 5 − 0,25 · 5² = 6,25 m."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −2(x + 3)(x + 6)?",
      "uitleg": "−2(x + 3)(x + 6) = 0 → x = −3 of x = −6: de snijpunten met de x-as zijn (−3, 0) en (−6, 0). De top ligt midden tussen x = −3 en x = −6: x = (−3 + (−6)) / 2 = −4,5. y = −2 · (−4,5 − (−3))(−4,5 − (−6)) = 4,5. Top (−4,5, 4,5).",
      "opties": [
        "(−4,5, 4,5)",
        "(4,5, 4,5)",
        "(−6, 0)",
        "(−4,5, −4,5)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −3x² + 18x − 31.",
      "antwoord": "3",
      "uitleg": "1 Uit x = 0 volgt y = −31. 2 −3x² + 18x − 31 = −31 → −3x² + 18x = 0 → x(−3x + 18) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = −3·3² + 18 · 3 − 31 = −4. 5 De top is (3, −4)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = x² + 2x − 7.",
      "antwoord": "-8",
      "uitleg": "1 Uit x = 0 volgt y = −7. 2 x² + 2x − 7 = −7 → x² + 2x = 0 → x(x + 2) = 0 → x = 0 of x = −2. 3 De x-coördinaat van de top ligt midden tussen 0 en −2: x = −1. 4 y = (−1)² + 2 · (−1) − 7 = −8. 5 De top is (−1, −8)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2x² − 16x + 37?",
      "uitleg": "1 Uit x = 0 volgt y = 37. 2 2x² − 16x + 37 = 37 → 2x² − 16x = 0 → x(2x − 16) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = 2·4² − 16 · 4 + 37 = 5. 5 De top is (4, 5).",
      "opties": [
        "(−4, 5)",
        "(4, 37)",
        "(4, 133)",
        "(4, 5)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Twee punten op de parabool bij een formule hebben dezelfde y-coördinaat: (−2, 7) en (0, 7). Bereken de x-coördinaat van de top van de parabool.",
      "antwoord": "-1",
      "uitleg": "De parabool is symmetrisch. De top ligt precies midden tussen x = −2 en x = 0: x = (−2 + 0) / 2 = −1."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −3x² − 18x − 18 snijdt de y-as in (0, −18). Er is nog een punt op de parabool met y = −18. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-6",
      "uitleg": "−3x² − 18x − 18 = −18 → −3x² − 18x = 0 → x(−3x − 18) = 0 → x = 0 of x = −6. Het andere punt is (−6, −18)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = −(x + 2)(x + 8) met de x-as?",
      "uitleg": "Los −(x + 2)(x + 8) = 0 op: (x + 2) = 0 of (x + 8) = 0, dus x = −2 of x = −8. De snijpunten met de x-as zijn (−8, 0) en (−2, 0). Let goed op de mintekens!",
      "opties": [
        "(0, −8) en (0, −2)",
        "(−8, 0) en (−2, 0)",
        "(8, 0) en (2, 0)",
        "(−8, 0) en (2, 0)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De formule h = 4a − 0,4a² hoort bij de hoogte van een tunnelboog (h in meters, a in meters vanaf de linkermuur). Hoeveel meter hoog is de tunnel in het midden?",
      "antwoord": "10",
      "uitleg": "4a − 0,4a² = 0 → a(4 − 0,4a) = 0 → a = 0 of a = 4 / 0,4 = 10. De tunnel is 10 m breed. Midden: a = 5, h = 4 · 5 − 0,4 · 5² = 10 m."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx − 11. De x-coördinaat van de top van de parabool is −4. Bereken b.",
      "antwoord": "8",
      "uitleg": "De parabool snijdt de y-as in (0, -11). Het andere punt met y = -11 ligt even ver aan de andere kant van de top: x = 2 · (−4) = −8. Invullen: (−8)² + b · (−8) + (−11) = -11 → 64 + −8b = 0 → b = 8."
    },
    {
      "type": "invul",
      "vraag": "De symmetrieas van een parabool is de lijn x = 1. Het punt (−6, 11) ligt op de parabool. Er is nog een punt op de parabool met y = 11. Bereken de x-coördinaat van dat punt.",
      "antwoord": "8",
      "uitleg": "De symmetrieas is x = 1. Het punt (−6, 11) ligt op afstand 7 links van de symmetrieas. Het andere punt met dezelfde hoogte ligt op gelijke afstand rechts van de as: x = 1 + 7 = 8."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −(x + 3)(x + 7)?",
      "uitleg": "−(x + 3)(x + 7) = 0 → x = −3 of x = −7: de snijpunten met de x-as zijn (−3, 0) en (−7, 0). De top ligt midden tussen x = −3 en x = −7: x = (−3 + (−7)) / 2 = −5. y = −(−5 − (−3))(−5 − (−7)) = 4. Top (−5, 4).",
      "opties": [
        "(−7, 0)",
        "(5, 4)",
        "(−5, −4)",
        "(−5, 4)"
      ],
      "antwoord": 3
    }
  ]
});
