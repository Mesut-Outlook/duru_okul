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
      "vraag": "Twee posities op dezelfde parabool bereiken dezelfde hoogte: de kromme y = −x² + 16x + 9 heeft als snijpunt met de y-as (0, 9). Bereken de x-waarde van het nevenpunt met diezelfde functiewaarde 9.",
      "antwoord": "16",
      "uitleg": "Stap 1: Stel y = 9:\n−x² + 16x + 9 = 9.\nStap 2: Trek 9 af:\n−x² + 16x = 0.\nStap 3: Ontbind in factoren:\nx(−x + 16) = 0.\nDit geeft x = 0 of x = 16."
    },
    {
      "type": "mc",
      "vraag": "Bij een fontein spuit water volgens h = −0,5x² + 2x + 0,8, waarin h en x in meters zijn. Hoeveel cm hoog bevindt zich het mondstuk van de straal bij x = 0?",
      "opties": [
        "80 cm",
        "8 cm",
        "200 cm",
        "0,8 cm"
      ],
      "antwoord": 0,
      "uitleg": "Stap 1: Vul x = 0 in:\nh = −0,5 · 0² + 2 · 0 + 0,8 = 0,8 meter.\nStap 2: Reken om naar centimeters:\n0,8 · 100 = 80 cm."
    },
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,05a² − 1,2a + 36. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "28,8",
      "uitleg": "P ligt op hoogte 36. Zelfde hoogte: 0,05a² − 1,2a = 0 → a = 0 of a = 1,2 / 0,05 = 24. Laagste punt in het midden: a = 12, h = 28,8 m."
    },
    {
      "type": "invul",
      "vraag": "Een hard weggeschoten bal volgt de vluchtlijn h = −0,1x² + 1,6x + 1, met h en x in meters. Bereken de hoogte van het hoogste punt van de bal (in meters).",
      "antwoord": "7,4",
      "uitleg": "Stap 1: Bereken de x-coördinaat van de top:\nx = −1,6 / (2 · −0,1) = 8 meter.\nStap 2: Vul x = 8 in:\nh = −0,1 · 64 + 1,6 · 8 + 1 = −6,4 + 12,8 + 1 = 7,4 meter."
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
      "vraag": "Een symmetrische dalparabool met top (7, −4) snijdt de y-as in (0, 45). Welke formule heeft de vorm y = ax² + bx + c? Bereken de waarde van b.",
      "antwoord": "-14",
      "uitleg": "Stap 1: Gebruik de topvorm met top (7, −4):\ny = a(x − 7)² − 4.\nStap 2: Vul (0, 45) in:\n45 = 49a − 4 → 49a = 49 → a = 1.\nStap 3: Werk de haakjes uit:\ny = 1(x² − 14x + 49) − 4 = x² − 14x + 45.\nVoor x staat het getal b = −14."
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
      "vraag": "Tijdens een rally gooit Lisa een volleybal over het net. Na 22 meter afstand heeft de bal weer dezelfde hoogte van 1,5 meter als bij het vertrek. Bepaal de x-coördinaat van de symmetrieas.",
      "antwoord": "11",
      "uitleg": "Stap 1: De bal bevindt zich op gelijke hoogte bij x = 0 en x = 22 meter.\nStap 2: De symmetrieas ligt precies in het midden:\nx = 22 / 2 = 11 meter."
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
