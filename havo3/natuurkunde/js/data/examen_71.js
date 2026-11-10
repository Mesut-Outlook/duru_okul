/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 71 — §1.2 Soorten beweging & Diagrammen — Toets G
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-71",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Toets 71 — §1.2 Soorten beweging & Diagrammen — Toets G",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🏁",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een voorwerp is op t = 0, 2, 5 en 9 s op s = 0, 6, 18 en 22 m. In welk tijdsinterval is de snelheid het grootst?",
      "opties": [
        "Van 0 tot 2 s",
        "Van 5 tot 9 s",
        "In alle intervallen is de snelheid gelijk",
        "Van 2 tot 5 s"
      ],
      "antwoord": 3,
      "uitleg": "Snelheden: 6/2 = 3,0 m/s, 12/3 = 4,0 m/s en 4/4 = 1,0 m/s. Het tweede interval is het snelst."
    },
    {
      "type": "mc",
      "vraag": "Bij dezelfde beweging (s = 0, 6, 18, 22 m op t = 0, 2, 5, 9 s) wil je de gemiddelde snelheid over het hele traject weten. Wat is die?",
      "opties": [
        "1,0 m/s",
        "2,4 m/s",
        "2,7 m/s",
        "4,0 m/s"
      ],
      "antwoord": 1,
      "uitleg": "v_gem = totale afstand / totale tijd = 22 / 9 = 2,4 m/s. Het gemiddelde van de drie deelsnelheden (2,7 m/s) is niet hetzelfde."
    },
    {
      "type": "mc",
      "vraag": "Een auto trekt eenparig op vanuit stilstand. Hoeveel keer zo groot wordt de afgelegde afstand als de optrektijd twee keer zo lang is (zelfde versnelling)?",
      "opties": [
        "4 keer zo groot",
        "2 keer zo groot",
        "8 keer zo groot",
        "Even groot"
      ],
      "antwoord": 0,
      "uitleg": "De eindsnelheid wordt 2× zo groot én de tijd ook 2×, dus de oppervlakte onder de lijn wordt 2 × 2 = 4× zo groot."
    },
    {
      "type": "mc",
      "vraag": "In een (v,t)-diagram loopt de lijn recht van 12 m/s naar 0 m/s in 6,0 s. Hoeveel meter legt het voorwerp in die tijd af?",
      "opties": [
        "36 m",
        "72 m",
        "18 m",
        "2,0 m"
      ],
      "antwoord": 0,
      "uitleg": "De oppervlakte is een driehoek: ½ × 6,0 × 12 = 36 m. Zonder het ½-deel krijg je 72 m."
    },
    {
      "type": "mc",
      "vraag": "Wat is de (v,t)-grafiek van een voorwerp dat stilstaat?",
      "opties": [
        "Een horizontale lijn op v = 0 m/s",
        "Een horizontale lijn boven de t-as",
        "Een stijgende rechte lijn",
        "Een rechte lijn die omlaag loopt"
      ],
      "antwoord": 0,
      "uitleg": "Stilstand betekent v = 0 m/s voor elk tijdstip: de lijn ligt op de t-as."
    },
    {
      "type": "mc",
      "vraag": "Een voorwerp heeft op t = 0 s een snelheid van 2,0 m/s en op t = 4,0 s een snelheid van 10 m/s, met een rechte lijn ertussen in het (v,t)-diagram. Hoe groot is de versnelling?",
      "opties": [
        "8,0 m/s²",
        "2,0 m/s²",
        "3,0 m/s²",
        "2,5 m/s²"
      ],
      "antwoord": 1,
      "uitleg": "a = Δv / t = (10 − 2,0) / 4,0 = 2,0 m/s². Delen door de eindsnelheid (2,5) of rekenen vanaf 0 (3,0) klopt niet."
    },
    {
      "type": "mc",
      "vraag": "Fietser A rijdt met 18 km/h en fietser B met 4,5 m/s. Wie rijdt het snelst?",
      "opties": [
        "B, want 4,5 kleiner is dan 18 maar B heeft een SI-eenheid",
        "B, want 4,5 m/s is meer dan 18 km/h",
        "A, want 18 km/h is 5,0 m/s",
        "Ze rijden even snel"
      ],
      "antwoord": 2,
      "uitleg": "Reken eerst om naar dezelfde eenheid: 18 / 3,6 = 5,0 m/s, en dat is meer dan 4,5 m/s."
    },
    {
      "type": "mc",
      "vraag": "In een (s,t)-diagram snijden de lijnen van twee fietsers elkaar op t = 20 s. Wat betekent dat?",
      "opties": [
        "Op dat moment staan beide fietsers stil",
        "Op dat moment hebben ze dezelfde snelheid",
        "Op dat moment hebben ze dezelfde versnelling",
        "Op dat moment zijn ze op dezelfde plaats"
      ],
      "antwoord": 3,
      "uitleg": "Een snijpunt in een (s,t)-diagram betekent dezelfde s op dezelfde t: ze zijn op dezelfde plek. De hellingen (snelheden) kunnen verschillen."
    },
    {
      "type": "mc",
      "vraag": "Welke eenheid heeft de oppervlakte onder een (v,t)-grafiek als v in m/s en t in s staat?",
      "opties": [
        "Meter per seconde kwadraat",
        "Seconde",
        "Meter",
        "Meter per seconde"
      ],
      "antwoord": 2,
      "uitleg": "(m/s) × s = m: de oppervlakte is een afstand."
    },
    {
      "type": "mc",
      "vraag": "Een auto start vanuit stilstand met een constante versnelling van 3,0 m/s². Wat is zijn snelheid na 4,0 s?",
      "opties": [
        "12 m/s",
        "7,0 m/s",
        "48 m/s",
        "0,75 m/s"
      ],
      "antwoord": 0,
      "uitleg": "Elke seconde komt er 3,0 m/s bij: v = a × t = 3,0 × 4,0 = 12 m/s."
    },
    {
      "type": "mc",
      "vraag": "Een voorwerp remt af van 72 km/h naar 36 km/h in 5,0 s. Wat is de grootte van de vertraging in m/s²?",
      "opties": [
        "3,6 m/s²",
        "10 m/s²",
        "2,0 m/s²",
        "7,2 m/s²"
      ],
      "antwoord": 2,
      "uitleg": "72 km/h = 20 m/s en 36 km/h = 10 m/s. Δv = 10 m/s in 5,0 s geeft 2,0 m/s²."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het (v,t)-diagram van een eenparig versnelde beweging vanuit stilstand is een rechte lijn die door de oorsprong gaat.",
      "antwoord": true,
      "uitleg": "Waar: Op t = 0 is v = 0 en daarna neemt v gelijkmatig toe: een rechte lijn vanuit (0,0)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als twee lijnen in een (s,t)-diagram elkaar snijden, hebben beide voorwerpen op dat moment dezelfde plaats.",
      "antwoord": true,
      "uitleg": "Waar: Dezelfde s op dezelfde t betekent dezelfde plek, ook al verschilt de snelheid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een voorwerp met een dalende lijn in het (v,t)-diagram legt een negatieve afstand af.",
      "antwoord": false,
      "uitleg": "Onwaar: De snelheid neemt af, maar de oppervlakte onder de lijn en dus de afstand blijft positief."
    },
    {
      "type": "waaronwaar",
      "vraag": "De gemiddelde snelheid van een heen- en terugreis met 60 km/h heen en 40 km/h terug is precies 50 km/h.",
      "antwoord": false,
      "uitleg": "Onwaar: De terugreis duurt langer dan de heenreis, dus de gemiddelde snelheid is lager dan 50 km/h (namelijk 48 km/h)."
    },
    {
      "type": "invul",
      "vraag": "Een wielrenner rijdt 2,7 km in 6,0 minuten. Hoe groot is zijn gemiddelde snelheid in m/s?",
      "antwoord": "7,5|7.5|7,5 m/s|7.5 m/s",
      "uitleg": "2,7 km = 2700 m en 6,0 min = 360 s, dus v = 2700 / 360 = 7,5 m/s."
    },
    {
      "type": "invul",
      "vraag": "Een voorwerp versnelt in 4,0 s eenparig van 0 naar 12 m/s en rijdt daarna nog 6,0 s met 12 m/s. Bereken de totale afstand in meter.",
      "antwoord": "96|96 m",
      "uitleg": "Eerst ½ × 4,0 × 12 = 24 m, daarna 12 × 6,0 = 72 m. Totaal 96 m."
    },
    {
      "type": "invul",
      "vraag": "Een trein rijdt 108 km/h en remt eenparig af met een vertraging van 1,5 m/s² tot stilstand. Bereken de remafstand in meter.",
      "antwoord": "300|300 m",
      "uitleg": "v = 30 m/s, remtijd = 30 / 1,5 = 20 s, afstand = ½ × 20 × 30 = 300 m."
    },
    {
      "type": "invul",
      "vraag": "Een auto versnelt eenparig in 5,0 s van 14 m/s naar 26 m/s. Bereken de afgelegde afstand in meter.",
      "antwoord": "100|100 m",
      "uitleg": "v_gem = (14 + 26) / 2 = 20 m/s, dus s = 20 × 5,0 = 100 m."
    },
    {
      "type": "open",
      "vraag": "Hoe ziet de (s,t)-grafiek eruit van fietser B, die eenparig versneld optrekt? <i>(Alleen het antwoord is genoeg.)</i>",
      "modelantwoord": "De grafiek van B is een kromme lijn die steeds steiler loopt.",
      "minTreffers": 1,
      "sleutelwoorden": ["kromme/gekromd/bocht/parabool"],
      "uitleg": "Constante snelheid geeft een rechte lijn, toenemende snelheid een steeds steilere kromme lijn."
    }
  ]
});
