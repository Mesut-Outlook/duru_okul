/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 116 — §2.5 Drie vormen van kwadratische formules (3/5, gemengd)
   Bron: Noordhoff H2 Parabolen (§2.5)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-25-3",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Proeftoets 116 — §2.5 Drie vormen van kwadratische formules (3/5, gemengd)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 3(x − 3)(x − 4) zonder haakjes.",
      "uitleg": "Eerst (x − 3)(x − 4) = x² − 7x + 12. Dan elke term keer 3: y = 3x² − 21x + 36.",
      "opties": [
        "y = 3x² + 21x + 36",
        "y = 3x² − 21x − 36",
        "y = 3x² − 21x + 36",
        "y = 3x² − 7x + 12"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = ½(x − 2)² − 12 zonder haakjes.",
      "uitleg": "(x − 2)² = x² − 4x + 4 (niet x² + 4!). Keer 0,5: ½x² − 2x + 2. Daarna − 12: y = ½x² − 2x − 10.",
      "opties": [
        "y = ½x² − 2x − 4",
        "y = ½x² − 2x + 2",
        "y = ½x² − 2x − 10",
        "y = ½x² − 10"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Herleid de formule y = (4x − 3)² + 5x² door alle haakjes uit te werken tot een vorm zonder haakjes. Welk getal staat er voor x?",
      "antwoord": "-24",
      "uitleg": "Stap 1: Werk het kwadraat uit:\n(4x − 3)² = 16x² − 24x + 9.\nStap 2: Tel 5x² op:\ny = 16x² − 24x + 9 + 5x² = 21x² − 24x + 9.\nVoor x staat het getal −24."
    },
    {
      "type": "invul",
      "vraag": "Een cirkelsproeier op een sportveld spuit water volgens h = −0,2a² + 2,4a + 1,2, met h en a in meters. Bereken de hoogte van het hoogste punt van de waterstraal (in meters).",
      "antwoord": "8,4",
      "uitleg": "Stap 1: Bereken de a-waarde van de top:\na = −2,4 / (2 · −0,2) = 6 meter.\nStap 2: Vul a = 6 in de formule in:\nh = −0,2 · 36 + 2,4 · 6 + 1,2 = −7,2 + 14,4 + 1,2 = 8,4 meter."
    },
    {
      "type": "invul",
      "vraag": "In de wiskundeles zie je een dalparabool met top (9, −6) die door (0, 75) gaat. Welke formule heeft de vorm y = ax² + bx + c? Bereken de waarde van b.",
      "antwoord": "-18",
      "uitleg": "Stap 1: Gebruik de topvorm met top (9, −6):\ny = a(x − 9)² − 6.\nStap 2: Vul (0, 75) in:\n75 = 81a − 6 → 81a = 81 → a = 1.\nStap 3: Werk de haakjes uit:\ny = 1(x² − 18x + 81) − 6 = x² − 18x + 75.\nVoor x staat het getal b = −18."
    },
    {
      "type": "invul",
      "vraag": "Een tennisbal wordt omhoog geslagen volgens de kromme h = −0,2x² + 1,4x + 0,35, met h en x in meters. Hoeveel cm hoog bevindt de bal zich bij x = 0?",
      "antwoord": "35",
      "uitleg": "Stap 1: Vul x = 0 in de formule in:\nh = −0,2 · 0² + 1,4 · 0 + 0,35 = 0,35 meter.\nStap 2: Reken om naar centimeters:\n0,35 · 100 = 35 cm."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −½(x + 8)(x − 6) is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan −½: een bergparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = ¼(x − 4)² − 10 is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan ¼: een dalparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −(x + 3)(x + 7) is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan −1: een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Twee posities op dezelfde parabool bezitten dezelfde hoogte: de grafiek y = −x² + 17x + 4 heeft y-waarde 4 bij de y-as. Welke x-waarde heeft het andere punt met dezelfde uitkomst?",
      "opties": [
        "17",
        "−17",
        "8,5",
        "4"
      ],
      "antwoord": 0,
      "uitleg": "Stap 1: Stel y = 4:\n−x² + 17x + 4 = 4.\nStap 2: Trek 4 af:\n−x² + 17x = 0.\nStap 3: Ontbind in factoren:\nx(−x + 17) = 0.\nDit geeft x = 0 of x = 17."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x − 9)(x − 5).",
      "antwoord": "7",
      "uitleg": "De snijpunten met de x-as zijn x = 9 en x = 5. De top ligt precies in het midden: x = (9 + 5) : 2 = 7."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −(x + 8)(x + 4).",
      "antwoord": "4",
      "uitleg": "De top heeft x = −6. Vul dit in de formule in: y = − · (−6 − (−8))(−6 − (−4)) = 4."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = (x + 5)(x + 3) snijdt de x-as in twee punten. Wat is de kleinste x-coördinaat van deze twee snijpunten?",
      "antwoord": "-5",
      "uitleg": "De snijpunten met de x-as vind je via y = 0: x = −5 of x = −3. De kleinste x-coördinaat hiervan is −5."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = ½(x + 6)(x − 6) snijdt de x-as in twee punten. Wat is de grootste x-coördinaat van deze twee snijpunten?",
      "antwoord": "6",
      "uitleg": "De snijpunten met de x-as vind je via y = 0: x = −6 of x = 6. De grootste x-coördinaat hiervan is 6."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de expressie y = (2x + 7)² − 15 zonder haakjes. Welke constante term zonder x blijft er over in het antwoord?",
      "opties": [
        "49",
        "34",
        "15",
        "28"
      ],
      "antwoord": 1,
      "uitleg": "Stap 1: Werk het kwadraat uit:\n(2x + 7)² = 4x² + 28x + 49.\nStap 2: Trek 15 af:\ny = 4x² + 28x + 34.\nHet losse getal is 34."
    },
    {
      "type": "invul",
      "vraag": "Een geworpen speer beweegt volgens de paraboolbaan h = −0,05x² + 1,4x + 1,6, met afstanden in meters. Bereken de hoogte van het hoogste punt van de speer (in meters).",
      "antwoord": "11,4",
      "uitleg": "Stap 1: Bereken de x-coördinaat van de top:\nx = −1,4 / (2 · −0,05) = 14 meter.\nStap 2: Vul x = 14 in de formule in:\nh = −0,05 · 14² + 1,4 · 14 + 1,6 = −9,8 + 19,6 + 1,6 = 11,4 meter."
    },
    {
      "type": "invul",
      "vraag": "Tussen twee bomen hangt een hangmat symmetrisch volgens h = 0,5(a − 2,5)² + 0,45 (h en a in meters, a gemeten vanaf de linkerboom). Wat is de afstand tussen de twee bomen in meters?",
      "antwoord": "5",
      "uitleg": "Het laagste punt is de top (a = 2,5): h = 0,45 m = 45 cm. Bij de boom (a = 0): h = 0,5 · 2,5² + 0,45 = 3,575 m. De andere boom staat even ver aan de andere kant: a = 5 m."
    },
    {
      "type": "invul",
      "vraag": "De weekwinst W in euro van een bedrijf dat q producten verkoopt is W = −0,4(q − 300)(q − 400). Bereken de maximale winst in euro.",
      "antwoord": "1000",
      "uitleg": "Snijpunten met de horizontale as: q = 300 en q = 400. Midden: q = 350. W = −0,4 · (350 − 300)(350 − 400) = 1000 euro."
    },
    {
      "type": "invul",
      "vraag": "De boog van een brug heeft de vorm h = −0,2(x − 8)² + 13, met h en x in meters. Wat is de maximale hoogte van de brug in meters?",
      "antwoord": "13",
      "uitleg": "Dit is een bergparabool in de topvorm. De top is (8, 13), dus de maximale hoogte is 13 meter."
    },
    {
      "type": "mc",
      "vraag": "In welke vorm staat de kwadratische formule y = 2(x − 2)² − 20?",
      "uitleg": "y = 2(x − 2)² − 20 bevat een kwadraat van een tweeterm met een constante erachter, dus de topvorm.",
      "opties": [
        "de algemene vorm: y = ax² + bx + c",
        "de lineaire vorm van de formule: y = ax + b",
        "de ontbonden vorm: y = a(x − s)(x − t)",
        "de topvorm van de parabool: y = a(x − p)² + q"
      ],
      "antwoord": 3
    }
  ]
});
