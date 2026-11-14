/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 85 — Integrale zwakte-toets H1
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-85",
  "hoofdstuk": 1,
  "paragraaf": "mix",
  "titel": "Toets 85 — Herhaling H1: Integrale zwakte-toets (alle zwakke punten)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🎯",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een drone stijgt met een constante snelheid recht omhoog. De zwaartekracht op de drone is 14 N. Hoe groot is de kracht van de rotoren omhoog?",
      "opties": ["28 N", "0 N", "14 N", "7 N"],
      "antwoord": 2,
      "uitleg": "Constante snelheid betekent Fres = 0 N. De rotorkracht omhoog is dus even groot als Fz omlaag: 14 N. Optellen (28 N) is fout."
    },
    {
      "type": "mc",
      "vraag": "Een roeier vaart met een constante snelheid. De voortstuwende kracht is 95 N, de wrijving van het water is 35 N. Hoe groot is de luchtweerstand?",
      "opties": ["60 N", "130 N", "2,7 N", "0 N"],
      "antwoord": 0,
      "uitleg": "Constante snelheid: Fvoor = Ftegen. 95 = 35 + Flucht, dus Flucht = 60 N. Je telt de krachten niet op (130 N)."
    },
    {
      "type": "mc",
      "vraag": "Op een kind op een glijbaan werkt een zwaartekracht van 343,35 N (g = 9,81 N/kg). Hoe groot is de massa van het kind?",
      "opties": ["3368 kg", "343 kg", "0,029 kg", "35 kg"],
      "antwoord": 3,
      "uitleg": "m = Fz / g = 343,35 / 9,81 = 35 kg. Vermenigvuldigen (3368) of g door Fz delen (0,029) is fout."
    },
    {
      "type": "mc",
      "vraag": "Een tram heeft een massa van 6000 kg. De resulterende kracht is 9000 N. Hoe groot is de versnelling?",
      "opties": ["54 000 000 m/s²", "1,5 m/s²", "0,67 m/s²", "15 000 m/s²"],
      "antwoord": 1,
      "uitleg": "a = Fres / m = 9000 / 6000 = 1,5 m/s². Je deelt Fres door m; vermenigvuldigen geeft een onzinnig groot getal."
    },
    {
      "type": "mc",
      "vraag": "Een scooter rijdt 15 km/h en heeft een remweg van 2,0 m. Hoe groot is de remweg bij 45 km/h (dezelfde remkracht)?",
      "opties": ["6,0 m", "18 m", "4,0 m", "9,0 m"],
      "antwoord": 1,
      "uitleg": "De remweg is evenredig met v². 3 keer zo snel geeft 3² = 9 keer zo lange remweg: 9 · 2,0 = 18 m. Niet 3 keer (6,0 m)."
    },
    {
      "type": "mc",
      "vraag": "Een automobilist heeft een reactietijd van 0,8 s en rijdt met 25 m/s. Hoe groot is de reactieafstand?",
      "opties": ["31 m", "0,03 m", "45 m", "20 m"],
      "antwoord": 3,
      "uitleg": "Reactieafstand = v · treactie = 25 · 0,8 = 20 m. Delen (31 m) of optellen is fout."
    },
    {
      "type": "mc",
      "vraag": "Een werknemer loopt horizontaal 15 m met een kist van 20 kg. Hoeveel arbeid verricht de zwaartekracht op de kist tijdens die 15 m?",
      "opties": ["0 J (loodrecht)", "2943 J (m·g·s)", "196 J (alleen F)", "300 J (m·s)"],
      "antwoord": 0,
      "uitleg": "Alleen een kracht in de bewegingsrichting verricht arbeid. Fz werkt loodrecht op de beweging, dus W = 0 J."
    },
    {
      "type": "mc",
      "vraag": "Een kraan hijst een blok van 250 kg met constante snelheid 8 m omhoog (g = 9,81 N/kg). Hoeveel arbeid verricht de kraankracht?",
      "opties": ["2000 J", "204 J", "19620 J", "2453 J"],
      "antwoord": 2,
      "uitleg": "De kraankracht is gelijk aan Fz = 250 · 9,81 = 2452,5 N. W = F · s = 2452,5 · 8 = 19620 J."
    },
    {
      "type": "mc",
      "vraag": "Een drone is gefilmd; de (s,t)-grafiek van zijn vlucht is 10 s lang een vlak stuk op s = 40 m. Welke conclusie klopt?",
      "opties": [
        "Hij vliegt met een constante snelheid van 40 m/s",
        "Hij versnelt steeds sneller vanaf het begin",
        "Hij vliegt 40 m per seconde terug naar de start",
        "Hij staat stil op 40 m van het beginpunt af"
      ],
      "antwoord": 3,
      "uitleg": "De helling van een (s,t)-lijn is de snelheid. Een horizontale lijn heeft helling 0: de drone staat stil."
    },
    {
      "type": "mc",
      "vraag": "Een auto remt af tot stilstand. Hoe bepaal je de remweg uit het (v,t)-diagram?",
      "opties": [
        "Met de helling van de lijn",
        "Met de oppervlakte onder de lijn",
        "Met de snelheid aan het einde",
        "Met het hoogste punt van de lijn"
      ],
      "antwoord": 1,
      "uitleg": "In een (v,t)-diagram is de oppervlakte onder de lijn de afgelegde afstand, dus ook de remweg. De helling is de versnelling."
    },
    {
      "type": "mc",
      "vraag": "Op een sleetje werken horizontaal 40 N naar rechts, 15 N naar links en 10 N naar links. Wat is Fres?",
      "opties": ["15 N naar rechts", "25 N naar rechts", "65 N naar rechts", "15 N naar links"],
      "antwoord": 0,
      "uitleg": "Naar links: 15 + 10 = 25 N. Fres = 40 − 25 = 15 N naar rechts, de kant van de grootste kracht."
    },
    {
      "type": "waaronwaar",
      "vraag": "Door alcohol wordt de remweg van een auto langer, omdat de remmen slechter werken.",
      "antwoord": false,
      "uitleg": "Onwaar: alcohol verlengt de reactietijd en dus de reactieafstand. De remweg zelf hangt van snelheid en remkracht af."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kist staat stil op de grond. Er werken dan geen krachten op de kist.",
      "antwoord": false,
      "uitleg": "Onwaar: de zwaartekracht en de steunkracht werken wel, maar ze heffen elkaar op. Fres = 0 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kraan hijst een container met constante snelheid 7 m omhoog en daarna een tweede keer 14 m omhoog. De tweede keer is de arbeid 2 keer zo groot.",
      "antwoord": true,
      "uitleg": "Waar: W = Fz · h met dezelfde Fz. Dubbele hoogte geeft dubbele arbeid, niet vier keer zoveel. (Fz is niet veranderd.)"
    },
    {
      "type": "waaronwaar",
      "vraag": "Een airbag maakt de kracht op je lichaam kleiner doordat de botstijd langer wordt.",
      "antwoord": true,
      "uitleg": "Waar: de airbag geeft mee, waardoor je langzamer tot stilstand komt. Een langere botstijd geeft een kleinere kracht."
    },
    {
      "type": "invul",
      "vraag": "Een fles water weegt op de weegschaal 640 g. Hoe groot is de zwaartekracht op de fles in N? Neem g = 9,81 N/kg.",
      "antwoord": "6,3|6.3|6,3 N|6.3 N|6,28|6.28|6,28 N|6.28 N",
      "uitleg": "m = 0,640 kg. Fz = 0,640 · 9,81 = 6,28 N, afgerond 6,3 N."
    },
    {
      "type": "invul",
      "vraag": "Een tram trekt eenparig op met een versnelling van 1,2 m/s². Hoeveel seconden duurt het om van 0 naar 9,0 m/s te komen?",
      "antwoord": "7,5|7.5|7,5 s|7.5 s",
      "uitleg": "t = Δv / a = 9,0 / 1,2 = 7,5 s. Je deelt Δv door a, niet andersom."
    },
    {
      "type": "invul",
      "vraag": "Een fietser remt eenparig van 6,0 m/s tot stilstand in 4,0 s. Bereken de remweg in m.",
      "antwoord": "12|12 m",
      "uitleg": "vgem = ½ · 6,0 = 3,0 m/s. Remweg = 3,0 · 4,0 = 12 m. Vergeet de factor ½ niet (anders 24 m)."
    },
    {
      "type": "invul",
      "vraag": "Een fiets rijdt met constante snelheid. De totale tegenwerkende kracht is 90 N; de luchtweerstand is twee keer zo groot als de rolweerstand. Hoeveel N is de rolweerstand?",
      "antwoord": "30|30 N",
      "uitleg": "Ftegen = 90 N = 2x + x = 3x, dus de rolweerstand x = 30 N."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom een auto op een nat wegdek een langere remweg heeft. <i>(Eén korte zin is genoeg.)</i>",
      "modelantwoord": "Er is minder wrijving tussen band en weg, dus de remkracht is kleiner en de auto vertraagt langzamer.",
      "minTreffers": 1,
      "sleutelwoorden": ["wrijving/grip/glad/remkracht/glijdt/slipt"],
      "uitleg": "Minder wrijving geeft een kleinere remkracht, dus een kleinere vertraging en een langere remweg."
    }
  ]
});
