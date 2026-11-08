/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 119 — §2.2 Symmetrie en top (6/10, basis)
   Bron: Noordhoff H2 Parabolen §2.2 (opgaven uit het boek met andere getallen)
   Gegenereerd met tools/gen_wiskunde_parabolen_22_extra.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-22-6",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Proeftoets 119 — §2.2 Symmetrie en top (6/10, basis)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "De parabool bij y = −3x² − 18x − 26 snijdt de y-as in (0, −26). Er is nog een punt op de parabool met y = −26. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-6",
      "uitleg": "−3x² − 18x − 26 = −26 → −3x² − 18x = 0 → x(−3x − 18) = 0 → x = 0 of x = −6. Het andere punt is (−6, −26)."
    },
    {
      "type": "invul",
      "vraag": "Twee posities op dezelfde parabool bereiken dezelfde hoogte: de bergparabool y = −x² + 13x + 11 gaat door (0, 11). Bepaal de x-coördinaat van de andere positie met y = 11.",
      "antwoord": "13",
      "uitleg": "Stap 1: Stel y = 11:\n−x² + 13x + 11 = 11.\nStap 2: Trek 11 af:\n−x² + 13x = 0.\nStap 3: Ontbind in factoren:\nx(−x + 13) = 0.\nDit geeft x = 0 of x = 13."
    },
    {
      "type": "invul",
      "vraag": "Bij een tuinornament spuit water omhoog volgens h = −0,25x² + 1,5x + 0,55, waarin h en x in meters zijn. Hoeveel cm hoog bevindt zich de wateruitlaat (bij x = 0)?",
      "antwoord": "55",
      "uitleg": "Stap 1: Vul x = 0 in:\nh = −0,25 · 0² + 1,5 · 0 + 0,55 = 0,55 meter.\nStap 2: Reken om naar centimeters:\n0,55 · 100 = 55 cm."
    },
    {
      "type": "mc",
      "vraag": "Een weggeschoten tennisbal beweegt langs de baan h = −0,2x² + 1,6x + 1,2, waarin h en x in meters zijn. Wat is de hoogte van het hoogste punt van de bal?",
      "opties": [
        "4 meter",
        "1,2 meter",
        "5,2 meter",
        "4,4 meter"
      ],
      "antwoord": 3,
      "uitleg": "Stap 1: Bereken de x-coördinaat van de top:\nx = −1,6 / (2 · −0,2) = 4 meter.\nStap 2: Vul x = 4 in:\nh = −0,2 · 4² + 1,6 · 4 + 1,2 = −3,2 + 6,4 + 1,2 = 4,4 meter."
    },
    {
      "type": "invul",
      "vraag": "De punten (−4, 21) en (14, 21) liggen op dezelfde parabool. Bereken de x-coördinaat van de top.",
      "antwoord": "5",
      "uitleg": "Beide punten hebben y = 21, dus ze liggen symmetrisch t.o.v. de symmetrieas. De top ligt midden tussen: x = (−4 + 14) / 2 = 5."
    },
    {
      "type": "invul",
      "vraag": "Een getekende dalparabool met top (7, −5) snijdt de y-as in (0, 44). Welke formule heeft de vorm y = ax² + bx + c? Bereken de waarde van b.",
      "antwoord": "-14",
      "uitleg": "Stap 1: Gebruik de topvorm met top (7, −5):\ny = a(x − 7)² − 5.\nStap 2: Vul (0, 44) in:\n44 = 49a − 5 → 49a = 49 → a = 1.\nStap 3: Werk de haakjes uit:\ny = 1(x² − 14x + 49) − 5 = x² − 14x + 44.\nVoor x staat het getal b = −14."
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = 3x² − 12x + 17 is (2, 5).",
      "antwoord": true,
      "uitleg": "Waar. 1 Uit x = 0 volgt y = 17. 2 3x² − 12x + 17 = 17 → 3x² − 12x = 0 → x(3x − 12) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = 3·2² − 12 · 2 + 17 = 5. 5 De top is (2, 5)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x + 7)(x − 7).",
      "antwoord": "0",
      "uitleg": "−(x + 7)(x − 7) = 0 → x = −7 of x = 7: de snijpunten met de x-as zijn (−7, 0) en (7, 0). De top ligt midden tussen x = −7 en x = 7: x = (−7 + 7) / 2 = 0. y = −(0 − (−7))(0 − 7) = 49. Top (0, 49)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = (x − 7)(x − 9) met de x-as?",
      "uitleg": "Los (x − 7)(x − 9) = 0 op: (x − 7) = 0 of (x − 9) = 0, dus x = 7 of x = 9. Let op het teken: bij (x + 3) hoort x = −3.",
      "opties": [
        "(7, 0) en (9, 0)",
        "(−7, 0) en (−9, 0)",
        "(7, 0) en (−9, 0)",
        "(0, 7) en (0, 9)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 3x² + 12x + 3 heeft symmetrieas x = −2. Het punt (−5, 18) ligt op de parabool. Er is nog een punt met y = 18. Bereken de x-coördinaat van dat punt.",
      "antwoord": "1",
      "uitleg": "−5 ligt 3 van de as x = −2. Het gespiegelde punt ligt even ver aan de andere kant: x = −2 + 3 = 1."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = x² − 2x − 6.",
      "antwoord": "1",
      "uitleg": "1 Uit x = 0 volgt y = −6. 2 x² − 2x − 6 = −6 → x² − 2x = 0 → x(x − 2) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = 1² − 2 · 1 − 6 = −7. 5 De top is (1, −7)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −x² + 2x + 7?",
      "uitleg": "1 Uit x = 0 volgt y = 7. 2 −x² + 2x + 7 = 7 → −x² + 2x = 0 → x(−x + 2) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = −1² + 2 · 1 + 7 = 8. 5 De top is (1, 8).",
      "opties": [
        "(1, 4)",
        "(1, 8)",
        "(1, 7)",
        "(−1, 8)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Tijdens een worp gooit Daan een basketbal omhoog. Na 22 meter afstand bereikt de bal weer dezelfde hoogte van 2 meter als bij de start. Bereken de x-coördinaat van de symmetrieas.",
      "antwoord": "11",
      "uitleg": "Stap 1: De bal is op gelijke hoogte bij x = 0 en x = 22 meter.\nStap 2: De symmetrieas ligt precies halverwege:\nx = 22 / 2 = 11 meter."
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = −3x² − 18x − 32 is (3, −5).",
      "antwoord": false,
      "uitleg": "Onwaar. 1 Uit x = 0 volgt y = −32. 2 −3x² − 18x − 32 = −32 → −3x² − 18x = 0 → x(−3x − 18) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −3·(−3)² − 18 · (−3) − 32 = −5. 5 De top is (−3, −5)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −2x² + 16x − 39 snijdt de y-as in (0, −39). Er is nog een punt op de parabool met y = −39. Bereken de x-coördinaat van dat punt.",
      "antwoord": "8",
      "uitleg": "−2x² + 16x − 39 = −39 → −2x² + 16x = 0 → x(−2x + 16) = 0 → x = 0 of x = 8. Het andere punt is (8, −39)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −2(x + 6)(x − 1). Een breuk of decimaal getal mag.",
      "antwoord": "24,5",
      "uitleg": "−2(x + 6)(x − 1) = 0 → x = −6 of x = 1: de snijpunten met de x-as zijn (−6, 0) en (1, 0). De top ligt midden tussen x = −6 en x = 1: x = (−6 + 1) / 2 = −2,5. y = −2 · (−2,5 − (−6))(−2,5 − 1) = 24,5. Top (−2,5, 24,5)."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 4,8a − 0,6a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "8",
      "uitleg": "4,8a − 0,6a² = 0 → a(4,8 − 0,6a) = 0 → a = 0 of a = 4,8 / 0,6 = 8. De tunnel is 8 m breed. Midden: a = 4, h = 4,8 · 4 − 0,6 · 4² = 9,6 m."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = 2x² − 16x + 29. Vul in: x = …",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = 29. 2 2x² − 16x + 29 = 29 → 2x² − 16x = 0 → x(2x − 16) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = 2·4² − 16 · 4 + 29 = −3. 5 De top is (4, −3). De symmetrieas is de verticale lijn door de top: x = 4."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −3x² − 30x − 76?",
      "uitleg": "1 Uit x = 0 volgt y = −76. 2 −3x² − 30x − 76 = −76 → −3x² − 30x = 0 → x(−3x − 30) = 0 → x = 0 of x = −10. 3 De x-coördinaat van de top ligt midden tussen 0 en −10: x = −5. 4 y = −3·(−5)² − 30 · (−5) − 76 = −1. 5 De top is (−5, −1).",
      "opties": [
        "(−5, −301)",
        "(5, −1)",
        "(−5, −1)",
        "(−5, −76)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx − 10. De x-coördinaat van de top van de parabool is −1. Bereken b.",
      "antwoord": "2",
      "uitleg": "De parabool snijdt de y-as in (0, -10). Het andere punt met y = -10 ligt even ver aan de andere kant van de top: x = 2 · (−1) = −2. Invullen: (−2)² + b · (−2) + (−10) = -10 → 4 + −2b = 0 → b = 2."
    }
  ]
});
