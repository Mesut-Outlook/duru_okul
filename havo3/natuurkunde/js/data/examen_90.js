/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 90 — Herhaling H1: Arbeid (cm, km en kJ; wanneer is W = 0?)
   Gegenereerd door tools/gen_natuurkunde_h1_zwakte_86_91.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-90",
  "hoofdstuk": 1,
  "paragraaf": "mix",
  "titel": "Toets 90 — Herhaling H1: Arbeid (cm, km en kJ; wanneer is W = 0?)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🏋️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Reken om: 2,5 kJ = …",
      "uitleg": "1 kJ = 1000 J, dus 2,5 kJ = 2500 J.",
      "opties": [
        "250 J",
        "25 J",
        "2500 J",
        "0,0025 J"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Reken om: 3 cm = …",
      "uitleg": "1 m = 100 cm, dus 3 cm = 3 / 100 = 0,03 m.",
      "opties": [
        "0,03 m",
        "300 m",
        "0,003 m",
        "0,3 m"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Een hamer slaat een spijker 2,0 cm het hout in met een gemiddelde kracht van 400 N. Bereken de arbeid in J. Reken eerst cm om naar m.",
      "antwoord": "8|8,0|8 J",
      "uitleg": "2,0 cm = 0,020 m. W = F · s = 400 · 0,020 = 8,0 J. Met 2,0 (cm) rekenen geeft 800: veel te groot."
    },
    {
      "type": "mc",
      "vraag": "Een timmerman drijft met één klap een nagel 0,5 cm diep in een balk; de hamer duwt gemiddeld met 1200 N. Hoeveel joule is dat?",
      "uitleg": "0,5 cm = 0,005 m. W = 1200 · 0,005 = 6,0 J. 600 J is zonder omrekenen; 2400 is 1200 / 0,5 (gedeeld).",
      "opties": [
        "600 J",
        "2400 J",
        "0,6 J",
        "6,0 J"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een fietser rijdt 3,0 km met constante snelheid tegen een wrijving van 50 N. Bereken de arbeid van zijn spierkracht in kJ.",
      "antwoord": "150|150 kJ",
      "uitleg": "3,0 km = 3000 m. W = 50 · 3000 = 150000 J = 150 kJ."
    },
    {
      "type": "mc",
      "vraag": "Een kar wordt met 200 N over 1,5 km getrokken. Hoeveel arbeid verricht de trekkracht?",
      "uitleg": "1,5 km = 1500 m. W = 200 · 1500 = 300000 J = 300 kJ. 300 J krijg je als je de km niet omrekent.",
      "opties": [
        "300 kJ",
        "3,0 kJ",
        "133 J",
        "300 J"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Vier paarden trekken samen een kar 200 m ver. Samen verrichten ze 280 kJ arbeid. Stap 1: hoe groot is de trekkracht van de vier paarden samen in N?",
      "antwoord": "1400|1400 N",
      "uitleg": "280 kJ = 280000 J. F = W / s = 280000 / 200 = 1400 N."
    },
    {
      "type": "invul",
      "vraag": "Vier paarden trekken samen een kar 200 m ver met samen 280 kJ arbeid. Stap 2: hoe groot is de kracht van één paard in N?",
      "antwoord": "350|350 N",
      "uitleg": "Samen 1400 N, verdeeld over 4 paarden: 1400 / 4 = 350 N per paard."
    },
    {
      "type": "mc",
      "vraag": "Je draagt een tas 10 m ver over een vlakke vloer. Hoeveel arbeid verricht je spierkracht (omhoog) op de tas?",
      "uitleg": "Je spierkracht wijst omhoog, de beweging is horizontaal. Kracht loodrecht op de beweging → W = 0 J.",
      "opties": [
        "Veel, want je moet de tas de hele tijd vasthouden",
        "0 J, want de kracht staat loodrecht op de beweging",
        "Negatief, want de tas gaat niet omhoog maar opzij",
        "10 J, want je hebt de tas 10 m ver gedragen"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Je duwt hard tegen een muur die niet beweegt. Je spierkracht verricht dan arbeid.",
      "antwoord": false,
      "uitleg": "Onwaar: de muur verplaatst niet, s = 0 m, dus W = F · s = 0 J (ook al word je moe)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een appel valt 2,0 m uit een boom. Tijdens de val is de arbeid van de zwaartekracht groter dan 0 J.",
      "antwoord": true,
      "uitleg": "Waar: de zwaartekracht wijst omlaag en de bal beweegt omlaag, dus W > 0."
    },
    {
      "type": "mc",
      "vraag": "Een bal wordt recht omhoog gegooid en valt terug tot dezelfde hoogte. Hoeveel arbeid verricht de zwaartekracht over de hele rit?",
      "uitleg": "Omhoog: W = −Fz · h. Omlaag: W = +Fz · h. Samen 0 J, want begin- en eindhoogte zijn gelijk.",
      "opties": [
        "Positief, want de bal valt aan het eind",
        "0 J: omhoog negatief, omlaag even veel positief",
        "Twee keer zoveel als bij alleen vallen",
        "Negatief, want de bal gaat eerst omhoog"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Een last van 50 kg wordt met constante snelheid 4,0 m omhoog getild (g = 9,81 N/kg). Hoeveel arbeid kost dat?",
      "uitleg": "F = Fz = 50 · 9,81 = 490,5 N. W = 490,5 · 4,0 = 1962 J. 123 J is 490,5 / 4,0: je moet vermenigvuldigen, niet delen.",
      "opties": [
        "200 J",
        "1250 J",
        "1962 J",
        "123 J"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "De wrijvingskracht verricht negatieve arbeid, want hij werkt tegen de beweging in.",
      "antwoord": true,
      "uitleg": "Waar: kracht tegen de beweging in → W = −F · s."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een doos twee keer zo hoog tillen kost vier keer zoveel arbeid.",
      "antwoord": false,
      "uitleg": "Onwaar: W = F · s. Twee keer zo hoog = twee keer zoveel arbeid (niet vier)."
    },
    {
      "type": "invul",
      "vraag": "Een surfer vaart met constante snelheid 30 m. De windkracht is 200 N. Hoeveel arbeid verricht de weerstand van het water in J? Let op het teken.",
      "antwoord": "-6000|−6000|-6000 J|−6000 J|-6 kJ",
      "uitleg": "Constante snelheid → weerstand = 200 N, tegen de beweging in. W = −200 · 30 = −6000 J."
    },
    {
      "type": "mc",
      "vraag": "Een trein trekt eenparig op van 0 tot 30 m/s in 60 s. Welke afstand legt hij af?",
      "uitleg": "s = v_gem · t = 15 · 60 = 900 m. 0,5 is de versnelling.",
      "opties": [
        "30 m",
        "900 m",
        "0,5 m",
        "1800 m"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Een resulterende kracht van 1500 N geeft een kar een versnelling van 3,0 m/s². Wat is de massa?",
      "uitleg": "m = Fres / a = 1500 / 3,0 = 500 kg.",
      "opties": [
        "4500 kg",
        "1503 kg",
        "0,002 kg",
        "500 kg"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De reactieafstand is evenredig met de snelheid.",
      "antwoord": true,
      "uitleg": "Waar: s_r = v · t_r. Twee keer zo snel = twee keer zo'n lange reactieafstand."
    },
    {
      "type": "open",
      "vraag": "Waarom verricht de zwaartekracht geen arbeid op een bal die over een vlakke tafel rolt? <i>(Eén korte zin is genoeg.)</i>",
      "sleutelwoorden": [
        "loodrecht/haaks/90/hoogte/niet omlaag/niet naar beneden"
      ],
      "minTreffers": 1,
      "modelantwoord": "Omdat de zwaartekracht loodrecht op de beweging staat.",
      "uitleg": "De bal gaat niet omlaag; een kracht loodrecht op de beweging verricht geen arbeid."
    }
  ]
});
