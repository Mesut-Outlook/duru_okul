/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 2 — Frequentietabel & Histogrammen
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h2-2",
  "hoofdstuk": 2,
  "titel": "Proeftoets 2 — Frequentietabel & Histogrammen",
  "vak": "Wiskunde · H2 Statistiek",
  "icoon": "📊",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat geeft de absolute frequentie van een waarneming aan?",
      "opties": [
        "Hoe vaak een bepaalde waarde voorkomt",
        "Het percentage van het geheel",
        "De gemiddelde score",
        "Het verschil tussen max en min"
      ],
      "antwoord": 0,
      "uitleg": "Absolute frequentie is het werkelijke aantal keren dat een score geteld is."
    },
    {
      "type": "mc",
      "vraag": "In een klas van 20 leerlingen hebben 4 leerlingen een 9 gehaald. Wat is de relatieve frequentie van het cijfer 9?",
      "opties": [
        "15%",
        "20%",
        "25%",
        "30%"
      ],
      "antwoord": 1,
      "uitleg": "(4 / 20) × 100% = 20%."
    },
    {
      "type": "mc",
      "vraag": "Wat is het klassenmidden van de klasse 60 - < 80?",
      "opties": [
        "65",
        "75",
        "70",
        "80"
      ],
      "antwoord": 2,
      "uitleg": "(60 + 80) / 2 = 70."
    },
    {
      "type": "mc",
      "vraag": "Wat is de klassenbreedte van de klasse 120 - < 150?",
      "opties": [
        "20",
        "25",
        "35",
        "30"
      ],
      "antwoord": 3,
      "uitleg": "150 - 120 = 30."
    },
    {
      "type": "mc",
      "vraag": "In een frequentietabel staan de scores 4 (3x), 5 (5x), 6 (8x) en 7 (4x). Hoeveel waarnemingen zijn er in totaal?",
      "opties": [
        "20",
        "18",
        "22",
        "24"
      ],
      "antwoord": 0,
      "uitleg": "3 + 5 + 8 + 4 = 20 waarnemingen."
    },
    {
      "type": "mc",
      "vraag": "Wat is de cumulatieve frequentie tot en met score 6 bij de vorige vraag?",
      "opties": [
        "8",
        "16",
        "11",
        "20"
      ],
      "antwoord": 1,
      "uitleg": "3 + 5 + 8 = 16."
    },
    {
      "type": "mc",
      "vraag": "Welk diagram gebruikt staven die direct tegen elkaar aan staan om continue klassendata weer te geven?",
      "opties": [
        "Cirkeldiagram",
        "Lijndiagram",
        "Histogram",
        "Beelddiagram"
      ],
      "antwoord": 2,
      "uitleg": "In een histogram sluiten de staven direct op elkaar aan."
    },
    {
      "type": "mc",
      "vraag": "Wat is de relatieve frequentie als 18 van de 72 mensen voor optie A kiezen?",
      "opties": [
        "20%",
        "33%",
        "30%",
        "25%"
      ],
      "antwoord": 3,
      "uitleg": "(18 / 72) × 100% = 25%."
    },
    {
      "type": "mc",
      "vraag": "Wat is het klassenmidden van 0 - < 10?",
      "opties": [
        "5",
        "4",
        "6",
        "10"
      ],
      "antwoord": 0,
      "uitleg": "(0 + 10) / 2 = 5."
    },
    {
      "type": "mc",
      "vraag": "Als een klasse 50 - < 60 een frequentie van 12 heeft op een totaal van 60, wat is het percentage?",
      "opties": [
        "15%",
        "20%",
        "25%",
        "30%"
      ],
      "antwoord": 1,
      "uitleg": "(12 / 60) × 100% = 20%."
    },
    {
      "type": "waaronwaar",
      "vraag": "De relatieve frequentie van alle waarnemingen samen telt altijd op tot 100%.",
      "antwoord": true,
      "uitleg": "Waar: alle relatieve aandelen vormen samen 100%."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de klasse 30 - < 40 hoort de waarde 40 thuis.",
      "antwoord": false,
      "uitleg": "Onwaar: '< 40' betekent tot 40 (40 zit in de volgende klasse)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een frequentietabel kan uitsluitend worden gebruikt voor getallen en nooit voor categorische gegevens zoals lievelingskleur.",
      "antwoord": false,
      "uitleg": "Onwaar: je kunt ook prima turven hoeveel mensen blauw, rood of groen kiezen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het klassenmidden bereken je door de ondergrens en bovengrens op te tellen en te delen door 2.",
      "antwoord": true,
      "uitleg": "Waar: (onder + boven) / 2."
    },
    {
      "type": "invul",
      "vraag": "In een onderzoek worden 80 mensen ondervraagd. 24 van hen reizen met de trein. Bereken de relatieve frequentie in procenten.",
      "antwoord": "30|30%|30 procent",
      "uitleg": "(24 / 80) × 100% = 30%."
    },
    {
      "type": "invul",
      "vraag": "Wat is het klassenmidden van de lengteklasse 165 - < 175 cm?",
      "antwoord": "170|170 cm",
      "uitleg": "(165 + 175) / 2 = 170."
    },
    {
      "type": "invul",
      "vraag": "Wat is de klassenbreedte van de klasse 45 - < 60?",
      "antwoord": "15",
      "uitleg": "De klassenbreedte is de bovengrens min de ondergrens: 60 - 45 = 15."
    },
    {
      "type": "invul",
      "vraag": "Als de cumulatieve frequentie bij score 5 gelijk is aan 14 en bij score 6 gelijk is aan 22, wat is dan de frequentie van score 6?",
      "antwoord": "8",
      "uitleg": "De frequentie van score 6 is het verschil in cumulatieve som: 22 - 14 = 8."
    },
    {
      "type": "open",
      "vraag": "Leg het verschil uit tussen absolute frequentie en relatieve frequentie aan de hand van een groep van 40 personen waarin 10 rokers zitten.",
      "sleutelwoorden": [
        "10",
        "25%",
        "aantal"
      ],
      "minTreffers": 2,
      "modelantwoord": "De absolute frequentie is het werkelijke aantal (10 personen). De relatieve frequentie is het percentage van het totaal: (10 / 40) × 100% = 25%.",
      "uitleg": "Absoluut is aantal (10); relatief is percentage (25%)."
    },
    {
      "type": "open",
      "vraag": "Bereken het geschatte gemiddelde van een groep met klassen: 0 - < 10 (freq 2) en 10 - < 20 (freq 8) met behulp van klassenmiddens.",
      "sleutelwoorden": [
        "5",
        "15",
        "13"
      ],
      "minTreffers": 2,
      "modelantwoord": "Klassenmiddens zijn 5 en 15. Totaal = (2 × 5 + 8 × 15) / 10 = (10 + 120) / 10 = 130 / 10 = 13.",
      "uitleg": "Geschat gemiddelde met klassenmiddens is 13."
    }
  ]
});
