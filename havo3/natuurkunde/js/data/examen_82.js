/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 82 — Herhaling H1: eenheden omrekenen en formules omdraaien
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-82",
  "hoofdstuk": 1,
  "paragraaf": "mix",
  "titel": "Toets 82 — Herhaling H1: Rekenen: eenheden omrekenen en formules omdraaien",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🧮",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een pak rijst heeft een massa van 650 g. Hoe groot is de zwaartekracht op het pak (g = 9,81 N/kg)? Reken eerst de massa om naar kg.",
      "opties": ["0,066 N", "64 N", "6,4 N", "6377 N"],
      "antwoord": 2,
      "uitleg": "650 g = 0,650 kg. Fz = m · g = 0,650 · 9,81 = 6,4 N. Wie de gram niet omrekent, krijgt 6377 N."
    },
    {
      "type": "mc",
      "vraag": "Een fietser rijdt 54 km/h. Hoeveel m/s is dat?",
      "opties": ["54 m/s", "15 m/s", "194 m/s", "5,4 m/s"],
      "antwoord": 1,
      "uitleg": "Van km/h naar m/s deel je door 3,6: 54 / 3,6 = 15 m/s. Vermenigvuldigen met 3,6 geeft een veel te groot getal."
    },
    {
      "type": "mc",
      "vraag": "Op een kist werkt een zwaartekracht van 736 N (g = 9,81 N/kg). Wat is de massa van de kist?",
      "opties": ["0,0133 kg", "7220 kg", "750 kg", "75,0 kg"],
      "antwoord": 3,
      "uitleg": "Fz = m · g, dus m = Fz / g = 736 / 9,81 = 75,0 kg. Je moet delen door g, niet vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Een resulterende kracht van 4800 N werkt op een bus met een massa van 1200 kg. Wat is de versnelling?",
      "opties": ["4,0 m/s²", "0,25 m/s²", "5760 m/s²", "0,40 m/s²"],
      "antwoord": 0,
      "uitleg": "Fres = m · a, dus a = Fres / m = 4800 / 1200 = 4,0 m/s². Delen, niet vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Een fietser rijdt met 6,0 m/s gedurende 5,0 minuten. Reken eerst de tijd om naar seconden. Hoeveel meter legt hij af?",
      "antwoord": "1800|1800 m|1,8 km|1,8|1.8",
      "uitleg": "5,0 min = 300 s. s = v · t = 6,0 · 300 = 1800 m."
    },
    {
      "type": "invul",
      "vraag": "Een scooter heeft een versnelling van 0,50 m/s². Na hoeveel seconden is zijn snelheid van 0 toegenomen tot 6,0 m/s?",
      "antwoord": "12|12 s",
      "uitleg": "a = Δv / t, dus t = Δv / a = 6,0 / 0,50 = 12 s. Niet a / Δv doen."
    },
    {
      "type": "invul",
      "vraag": "Een trein versnelt eenparig van 5,0 m/s naar 20 m/s in 6,0 s. Bereken de versnelling in m/s².",
      "antwoord": "2,5|2.5|2,5 m/s²|2.5 m/s²|2,5 m/s2",
      "uitleg": "Δv = 20 − 5,0 = 15 m/s. a = Δv / t = 15 / 6,0 = 2,5 m/s². De beginsnelheid is niet 0, dus trek die eerst af."
    },
    {
      "type": "invul",
      "vraag": "Een kar wordt over een afstand van 40 m getrokken. De arbeid die de trekkracht verricht is 3000 J. Hoe groot is de kracht in N?",
      "antwoord": "75|75 N",
      "uitleg": "W = F · s, dus F = W / s = 3000 / 40 = 75 N."
    },
    {
      "type": "mc",
      "vraag": "Een kar van 1500 kg versnelt met 0,80 m/s². Hoe groot is de resulterende kracht?",
      "opties": ["0,00053 N", "1875 N", "1200 N", "1500 N"],
      "antwoord": 2,
      "uitleg": "Fres = m · a = 1500 · 0,80 = 1200 N. Delen van m door a geeft 1875, maar dat is niet de formule."
    },
    {
      "type": "mc",
      "vraag": "Een motorrijder rijdt met constante snelheid. De motorkracht is 640 N en de rolweerstand is 180 N. Hoe groot is de luchtweerstand?",
      "opties": ["460 N", "820 N", "640 N", "1100 N"],
      "antwoord": 0,
      "uitleg": "Constante snelheid betekent Fres = 0 N, dus Ftegen = 640 N. Lucht = 640 − 180 = 460 N. Optellen geeft 820 N, en dat klopt niet."
    },
    {
      "type": "mc",
      "vraag": "Een auto heeft bij een bepaalde snelheid een remweg van 15 m. Hoe lang wordt de remweg bij een drie keer zo grote snelheid (zelfde wegdek)?",
      "opties": ["45 m", "60 m", "225 m", "135 m"],
      "antwoord": 3,
      "uitleg": "De remweg is evenredig met v². Drie keer zo snel geeft 3² = 9 keer zo lang: 9 · 15 = 135 m."
    },
    {
      "type": "mc",
      "vraag": "Een tram remt gelijkmatig tot stilstand in 5,0 s. Zijn beginsnelheid is 16 m/s. Hoe groot is de remweg?",
      "opties": ["80 m", "40 m", "21 m", "11 m"],
      "antwoord": 1,
      "uitleg": "De gemiddelde snelheid is ½ · 16 = 8,0 m/s. Remweg = 8,0 · 5,0 = 40 m. Zonder de helft krijg je 80 m."
    },
    {
      "type": "mc",
      "vraag": "Een boek ligt stil op een tafel. Welke uitspraak klopt?",
      "opties": [
        "Er werken geen krachten op het boek, want het staat stil",
        "Fz is groter dan de kracht van de tafel, dus Fres wijst omlaag",
        "De krachten werken wel, maar heffen elkaar op: Fres = 0 N",
        "De kracht van de tafel bestaat alleen als het boek beweegt"
      ],
      "antwoord": 2,
      "uitleg": "Bij stilstand werken er wel krachten, maar de zwaartekracht en de kracht van de tafel zijn even groot en tegengesteld. Fres = 0 N."
    },
    {
      "type": "mc",
      "vraag": "In een (v,t)-diagram loopt een horizontale lijn op v = 5,0 m/s van t = 0 s tot t = 6,0 s. Welke afstand is afgelegd?",
      "opties": ["11 m", "30 m", "0 m", "0,83 m"],
      "antwoord": 1,
      "uitleg": "De oppervlakte onder de lijn is de afstand: 5,0 · 6,0 = 30 m. De lijn is horizontaal, dus de snelheid is constant en niet 0."
    },
    {
      "type": "mc",
      "vraag": "Een kind tilt een tas van 4,0 kg langzaam 1,5 m omhoog (g = 9,81 N/kg). Hoeveel arbeid verricht de spierkracht?",
      "opties": ["39 J", "6,0 J", "2,7 J", "59 J"],
      "antwoord": 3,
      "uitleg": "De spierkracht is gelijk aan Fz = 4,0 · 9,81 = 39 N. W = F · s = 39 · 1,5 = 59 J."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een snelheid van 36 km/h is hetzelfde als 10 m/s.",
      "antwoord": true,
      "uitleg": "Waar: 36 / 3,6 = 10 m/s."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om de massa uit de zwaartekracht te berekenen, vermenigvuldig je Fz met g.",
      "antwoord": false,
      "uitleg": "Onwaar: Fz = m · g, dus m = Fz / g. Je deelt door g."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kelner loopt met een dienblad op een horizontale vloer. De zwaartekracht op het dienblad verricht dan geen arbeid.",
      "antwoord": true,
      "uitleg": "Waar: de zwaartekracht werkt omlaag en de beweging is horizontaal. Alleen de kracht in de bewegingsrichting verricht arbeid, dus W = 0 J."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een voorwerp met een horizontale lijn op v = 3,0 m/s in een (v,t)-diagram staat stil.",
      "antwoord": false,
      "uitleg": "Onwaar: een horizontale lijn betekent een constante snelheid (a = 0). Alleen op de tijdas (v = 0 m/s) staat het voorwerp stil."
    },
    {
      "type": "open",
      "vraag": "Je wilt een snelheid in km/h omrekenen naar m/s. Wat doe je met het getal? <i>(Eén korte zin is genoeg.)</i>",
      "modelantwoord": "Je deelt het getal door 3,6.",
      "minTreffers": 1,
      "sleutelwoorden": [
        "deelt/delen/gedeeld/delen door"
      ],
      "uitleg": "1 m/s = 3,6 km/h, dus van km/h naar m/s deel je door 3,6."
    }
  ]
});
