/* =========================================================
   Duru's Scheikunde (HAVO 3) — Toets 22 — Grootheden, eenheden & notaties H1
   Hoofdstuk 1 (Chemie Overal) — grootheid/eenheid, voorvoegsels, dichtheid, °C ↔ K, pH-notatie
   20 vragen · 30 minuten. Gebaseerd op §1.1, §1.3 en §1.4 van het boek (eigen voorbeelden en getallen).
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-sch-h1-22",
  "hoofdstuk": 1,
  "paragraaf": "begrippen",
  "titel": "Toets 22 — Grootheden, eenheden & notaties H1",
  "vak": "Scheikunde · HAVO 3 (H1 — grootheden)",
  "icoon": "🧪",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Kilogram (kg) en liter (L) zijn allebei ...",
      "opties": [
        "grootheden, want je kunt ze meten",
        "stofeigenschappen, want ze horen bij een stof",
        "eenheden, waarmee je een grootheid meet",
        "voorvoegsels, want ze bestaan uit meerdere delen"
      ],
      "antwoord": 2,
      "uitleg": "Een grootheid (zoals massa of volume) is een eigenschap die je kunt meten. De eenheid (zoals kilogram of liter) is de maat waarin je die grootheid meet."
    },
    {
      "type": "mc",
      "vraag": "Het voorvoegsel <b>milli (m)</b> in milliliter betekent ...",
      "opties": [
        "duizend keer zo groot",
        "honderd keer zo klein",
        "een duizendste deel",
        "tien keer zo groot"
      ],
      "antwoord": 2,
      "uitleg": "Milli (m) is een duizendste: 1 milliliter is 0,001 liter. Kilo (k) is het tegenovergestelde en betekent duizend."
    },
    {
      "type": "mc",
      "vraag": "Je hebt 0,250 kg zout. Hoeveel gram is dat?",
      "opties": [
        "0,000250 g",
        "250 g",
        "2,50 g",
        "25,0 g"
      ],
      "antwoord": 1,
      "uitleg": "Van kg naar g vermenigvuldig je met 1000: 0,250 × 1000 = 250 g."
    },
    {
      "type": "mc",
      "vraag": "Een maatbeker bevat 0,0470 L water. Hoeveel cm³ is dat?",
      "opties": [
        "47,0 cm³",
        "4,70 cm³",
        "0,0000470 cm³",
        "470 cm³"
      ],
      "antwoord": 0,
      "uitleg": "Van L naar cm³ vermenigvuldig je met 1000: 0,0470 × 1000 = 47,0 cm³."
    },
    {
      "type": "mc",
      "vraag": "Aluminium heeft een dichtheid van 2,7 g/cm³. Wat is de massa van een blokje aluminium van 10,0 cm³?",
      "opties": [
        "0,27 g",
        "27 g",
        "3,7 g",
        "2,7 g"
      ],
      "antwoord": 1,
      "uitleg": "massa = dichtheid × volume = 2,7 × 10,0 = 27 g."
    },
    {
      "type": "mc",
      "vraag": "Een metalen blokje heeft een massa van 90,0 g en een volume van 20,0 cm³. Wat is de dichtheid?",
      "opties": [
        "0,22 g/cm³",
        "70,0 g/cm³",
        "1800 g/cm³",
        "4,50 g/cm³"
      ],
      "antwoord": 3,
      "uitleg": "dichtheid = massa / volume = 90,0 / 20,0 = 4,50 g/cm³."
    },
    {
      "type": "mc",
      "vraag": "Magnesium heeft een dichtheid van 1,7 g/cm³. Welk volume heeft 8,5 g magnesium?",
      "opties": [
        "14 cm³",
        "0,20 cm³",
        "5,0 cm³",
        "10 cm³"
      ],
      "antwoord": 2,
      "uitleg": "volume = massa / dichtheid = 8,5 / 1,7 = 5,0 cm³."
    },
    {
      "type": "mc",
      "vraag": "Een leerling meet buiten 25 °C. Hoeveel kelvin is dat?",
      "opties": [
        "298 K",
        "25 K",
        "6825 K",
        "−248 K"
      ],
      "antwoord": 0,
      "uitleg": "Van °C naar K tel je 273 op: 25 + 273 = 298 K."
    },
    {
      "type": "mc",
      "vraag": "Een stof heeft een kookpunt van 400 K. Hoeveel graden Celsius is dat?",
      "opties": [
        "127 °C",
        "673 °C",
        "−127 °C",
        "1,47 °C"
      ],
      "antwoord": 0,
      "uitleg": "Van K naar °C trek je 273 af: 400 − 273 = 127 °C."
    },
    {
      "type": "mc",
      "vraag": "De massa van een diamant geef je weer in karaat (1 karaat = 0,200 g). Wat is karaat dan?",
      "opties": [
        "Een grootheid, want het gaat over de massa",
        "Een voorvoegsel, want het betekent een deel van een gram",
        "Een stofeigenschap, want het gaat over diamant",
        "Een eenheid, want je meet er een grootheid mee"
      ],
      "antwoord": 3,
      "uitleg": "Karaat is de maat waarin je de massa van een diamant meet, dus een eenheid. De grootheid is de massa."
    },
    {
      "type": "mc",
      "vraag": "Tomatenketchup heeft een pH van 3,6. Wat past daarbij?",
      "opties": [
        "Neutraal, want de pH ligt dicht bij 7",
        "Basisch, want de pH is groter dan 0",
        "Zuur, want de pH is kleiner dan 7",
        "Niet te bepalen zonder pH-papier"
      ],
      "antwoord": 2,
      "uitleg": "pH &lt; 7 betekent een zure oplossing. Hoe lager de pH, des te zuurder de oplossing."
    },
    {
      "type": "waaronwaar",
      "vraag": "Massa en volume zijn stofeigenschappen, want je kunt ze allebei meten.",
      "antwoord": false,
      "uitleg": "Onwaar. Massa en volume kun je weliswaar meten (het zijn grootheden), maar ze zeggen niet om welke stof het gaat: elke stof kan elke massa en elk volume hebben."
    },
    {
      "type": "waaronwaar",
      "vraag": "De dichtheid van een stof is wel een stofeigenschap.",
      "antwoord": true,
      "uitleg": "Waar. Dichtheid is de massa per volume-eenheid. Daarmee kun je bepalen van welke stof iets gemaakt is."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een volume van 0,0250 L is gelijk aan 25,0 cm³.",
      "antwoord": true,
      "uitleg": "Waar. 0,0250 × 1000 = 25,0 cm³."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een temperatuur van 300 K komt overeen met 573 °C.",
      "antwoord": false,
      "uitleg": "Onwaar. Van K naar °C trek je 273 af: 300 − 273 = 27 °C. Je telt 273 alleen op als je van °C naar K gaat."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een oplossing met pH 5 is basischer dan een oplossing met pH 9.",
      "antwoord": false,
      "uitleg": "Onwaar. Hoe hoger de pH, des te basischer de oplossing. pH 9 is dus basischer dan pH 5; pH 5 is zelfs zuur."
    },
    {
      "type": "invul",
      "vraag": "Kamertemperatuur is 20 °C. Hoeveel kelvin is dat? (alleen het getal)",
      "antwoord": "293",
      "uitleg": "20 + 273 = 293 K."
    },
    {
      "type": "invul",
      "vraag": "Hoeveel graden Celsius is het absolute nulpunt, dus 0 K? (alleen het getal)",
      "antwoord": "-273|−273",
      "uitleg": "Stoffen kunnen nooit kouder worden dan −273 °C. Dit absolute nulpunt is gelijk aan 0 K."
    },
    {
      "type": "invul",
      "vraag": "Een stukje metaal heeft een massa van 120 g en een volume van 40 cm³. Bereken de dichtheid in g/cm³ (één decimaal).",
      "antwoord": "3,0|3.0|3",
      "uitleg": "dichtheid = massa / volume = 120 / 40 = 3,0 g/cm³."
    },
    {
      "type": "open",
      "vraag": "Iemand zegt: ‘Lood is zwaarder dan veren.’ Leg uit wat hier wetenschappelijk beter gezegd moet worden.",
      "sleutelwoorden": [
        "dichtheid/massa per volume",
        "massa/kilogram/gewicht",
        "volume/dezelfde hoeveelheid/zelfde volume"
      ],
      "minTreffers": 2,
      "modelantwoord": "Een hoeveelheid lood kan evenveel of minder massa hebben dan een hoeveelheid veren, want massa hangt af van hoeveel je neemt. Je kunt wel zeggen dat de dichtheid van lood groter is: bij hetzelfde volume heeft lood meer massa dan veren.",
      "uitleg": "Massa is geen stofeigenschap, dichtheid wel. Vergelijk je lood en veren, dan kun je alleen iets zeggen over de dichtheid (massa per volume-eenheid), niet over de massa zonder hoeveelheid."
    }
  ]
});
