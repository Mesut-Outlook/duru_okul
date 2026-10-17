/* =========================================================
   Duru's Economie (HAVO 3) — Proeftoets 39: Koopkracht berekenen (Paragraaf 2.3)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-economie-39",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Proeftoets 39: Koopkracht berekenen (Paragraaf 2.3)",
  "vak": "Economie · HAVO 3 (Pincode)",
  "icoon": "🧮",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Het nominaal inkomen stijgt met 4% en de inflatie bedraagt 1,5%. Wat gebeurt er met de koopkracht?",
      "opties": [
        "De koopkracht stijgt met 5,5%.",
        "De koopkracht daalt met 2,5%.",
        "De koopkracht blijft gelijk.",
        "De koopkracht stijgt met 2,5%."
      ],
      "antwoord": 3,
      "uitleg": "Procentuele verandering reîl inkomen = procentuele verandering nominaal inkomen − inflatiepercentage. 4% − 1,5% = 2,5%: de koopkracht stijgt."
    },
    {
      "type": "mc",
      "vraag": "Het nominaal inkomen stijgt met 2% terwijl de inflatie 5,5% is. Wat gebeurt er met de koopkracht?",
      "opties": [
        "De koopkracht stijgt met 3,5%.",
        "De koopkracht daalt met 3,5%.",
        "De koopkracht daalt met 7,5%.",
        "De koopkracht blijft gelijk."
      ],
      "antwoord": 1,
      "uitleg": "Procentuele verandering reîl inkomen = procentuele verandering nominaal inkomen − inflatiepercentage. 2% − 5,5% = −3,5%: de koopkracht daalt."
    },
    {
      "type": "mc",
      "vraag": "Het loon van Said blijft gelijk, terwijl de prijzen gemiddeld met 3% stijgen. Met hoeveel procent verandert zijn koopkracht?",
      "opties": [
        "Zij stijgt met 3%.",
        "Zij blijft gelijk.",
        "Zij daalt met 3%.",
        "Zij daalt met 1,5%."
      ],
      "antwoord": 2,
      "uitleg": "Procentuele verandering reîl inkomen = procentuele verandering nominaal inkomen − inflatiepercentage. 0% − 3% = −3%."
    },
    {
      "type": "mc",
      "vraag": "De lonen in een land dalen met 2% en de prijzen dalen met 4%. Wat gebeurt er met de koopkracht?",
      "opties": [
        "De koopkracht stijgt met 2%.",
        "De koopkracht daalt met 6%.",
        "De koopkracht daalt met 2%.",
        "De koopkracht blijft gelijk."
      ],
      "antwoord": 0,
      "uitleg": "Procentuele verandering reîl inkomen = procentuele verandering nominaal inkomen − inflatiepercentage. −2% − (−4%) = +2%: de prijzen dalen harder dan het inkomen."
    },
    {
      "type": "mc",
      "vraag": "Het inkomen van Bo stijgt van € 3.200 naar € 3.296 per maand. De inflatie is 2%. Met hoeveel procent verandert Bo’s reële inkomen?",
      "opties": [
        "Het stijgt met 3%.",
        "Het daalt met 1%.",
        "Het stijgt met 1%.",
        "Het stijgt met 5%."
      ],
      "antwoord": 2,
      "uitleg": "Nominaal: (3.296 − 3.200) ÷ 3.200 × 100% = 3%. Reîl: 3% − 2% = 1%."
    },
    {
      "type": "mc",
      "vraag": "De prijzen in een land stijgen met 5%. De werknemers krijgen extra loon, maar dat is maar 40% van het inflatiepercentage. Met hoeveel procent verandert de koopkracht?",
      "opties": [
        "De koopkracht daalt met 2%.",
        "De koopkracht daalt met 3%.",
        "De koopkracht stijgt met 2%.",
        "De koopkracht daalt met 5%."
      ],
      "antwoord": 1,
      "uitleg": "Het loon stijgt met 40% van 5% = 2%. Koopkracht: 2% − 5% = −3%."
    },
    {
      "type": "mc",
      "vraag": "Bij een inflatie van 3,5%: met hoeveel procent moet je nominale inkomen stijgen om je koopkracht gelijk te houden?",
      "opties": [
        "Met 0%",
        "Met 7%",
        "Met 1,75%",
        "Met 3,5%"
      ],
      "antwoord": 3,
      "uitleg": "Het reële inkomen blijft gelijk als de verandering 0% is: nominaal − 3,5% = 0%, dus het nominaal inkomen moet 3,5% stijgen."
    },
    {
      "type": "mc",
      "vraag": "De koopkracht van Lena stijgt met 2% terwijl de inflatie 3% is. Met hoeveel procent is haar nominaal inkomen gestegen?",
      "opties": [
        "Met 5%",
        "Met 1%",
        "Met 2%",
        "Met 6%"
      ],
      "antwoord": 0,
      "uitleg": "Nominaal − 3% = 2%, dus nominaal = 2% + 3% = 5%."
    },
    {
      "type": "mc",
      "vraag": "Het nominaal inkomen stijgt met 6% en de koopkracht stijgt met 2,5%. Hoe hoog is de inflatie?",
      "opties": [
        "3,5%",
        "8,5%",
        "2,5%",
        "6%"
      ],
      "antwoord": 0,
      "uitleg": "6% − inflatie = 2,5%, dus de inflatie is 6% − 2,5% = 3,5%."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het nominaal inkomen stijgt met 3% en de inflatie is 4%. Dan stijgt de koopkracht met 1%.",
      "antwoord": false,
      "uitleg": "Onwaar. 3% − 4% = −1%: de koopkracht daalt met 1%."
    },
    {
      "type": "waaronwaar",
      "vraag": "De procentuele verandering van het reële inkomen bereken je door van de procentuele verandering van het nominaal inkomen het inflatiepercentage af te halen.",
      "antwoord": true,
      "uitleg": "Waar. Dat is de formule uit het boek."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het nominaal inkomen stijgt met 5% en de inflatie is 2%. Dan is de koopkracht met 7% gestegen.",
      "antwoord": false,
      "uitleg": "Onwaar. Je trekt de inflatie af: 5% − 2% = 3%."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als het nominaal inkomen met 3% daalt en de prijzen ook met 3% dalen, blijft de koopkracht gelijk.",
      "antwoord": true,
      "uitleg": "Waar. −3% − (−3%) = 0%: de reële verandering is nul."
    },
    {
      "type": "invul",
      "vraag": "Het inkomen van Joni stijgt van € 2.400 naar € 2.496 per maand. Met hoeveel procent is haar nominaal inkomen gestegen? Antwoord in %: ____",
      "antwoord": "4",
      "uitleg": "(2.496 − 2.400) ÷ 2.400 × 100% = 4%."
    },
    {
      "type": "invul",
      "vraag": "Het nominaal inkomen stijgt met 6% en de inflatie is 2,5%. Met hoeveel procent stijgt het reële inkomen? Antwoord in %: ____",
      "antwoord": "3,5",
      "uitleg": "6% − 2,5% = 3,5%."
    },
    {
      "type": "invul",
      "vraag": "Het nominaal inkomen stijgt met 2,5% en de koopkracht daalt met 1,5%. Hoe hoog is de inflatie? Antwoord in %: ____",
      "antwoord": "4",
      "uitleg": "2,5% − inflatie = −1,5%, dus inflatie = 2,5% + 1,5% = 4%."
    },
    {
      "type": "invul",
      "vraag": "De inflatie is −2% (de prijzen dalen) en het reële inkomen stijgt met 1%. Met hoeveel procent verandert het nominaal inkomen? Antwoord in %: ____",
      "antwoord": "-1",
      "uitleg": "Nominaal − (−2%) = 1%, dus nominaal = 1% + (−2%) = −1%."
    },
    {
      "type": "invul",
      "vraag": "De lonen in een land dalen met 4% en de prijzen dalen met 6%. Met hoeveel procent stijgt de koopkracht? Antwoord in %: ____",
      "antwoord": "2",
      "uitleg": "−4% − (−6%) = +2%."
    },
    {
      "type": "open",
      "vraag": "Het inkomen van Femke stijgt van € 2.500 naar € 2.600 per maand. In dezelfde periode stijgen de prijzen gemiddeld met 3%. Bereken de procentuele verandering van haar nominaal inkomen en van haar reële inkomen. Laat je berekening zien.",
      "sleutelwoorden": [
        "4%/4 procent",
        "1%/1 procent"
      ],
      "minTreffers": 2,
      "modelantwoord": "Nominaal: (2.600 − 2.500) ÷ 2.500 × 100% = 4%. Reîl: 4% − 3% = 1%.",
      "uitleg": "Eerst het nominale percentage uitrekenen (4%), daarna de inflatie (3%) eraf halen: het reële inkomen stijgt met 1%."
    },
    {
      "type": "open",
      "vraag": "Een werknemer krijgt een loonsverhoging van 2,5%. De inflatie is 4%. Leg uit wat er met zijn koopkracht gebeurt en bereken met hoeveel procent.",
      "sleutelwoorden": [
        "daalt/daling/neemt af",
        "1,5"
      ],
      "minTreffers": 2,
      "modelantwoord": "De koopkracht daalt met 1,5%, want 2,5% − 4% = −1,5%.",
      "uitleg": "Reîl = nominaal − inflatie = 2,5% − 4% = −1,5%: de koopkracht daalt."
    }
  ]
});
