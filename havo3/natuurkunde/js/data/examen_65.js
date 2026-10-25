/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 65 — Integrale Examentraining Hoofdstuk 1 (Mix §1.1 t/m §1.5)
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-65",
  "hoofdstuk": 1,
  "paragraaf": "mix",
  "titel": "Toets 65 — Integrale Examentraining Hoofdstuk 1 (Mix §1.1 t/m §1.5)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🎯",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een auto rijdt met constante snelheid op de snelweg. De motorkracht is 1500 N. Hoe groot is de totale tegenwerkende kracht van rol- en luchtweerstand?",
      "opties": [
        "0 N",
        "Exact 1500 N",
        "Minder dan 1500 N",
        "3000 N"
      ],
      "antwoord": 1,
      "uitleg": "Bij constante snelheid is de versnelling a = 0 m/s² en dus de resulterende kracht Fres = 0 N. De tegenwerkende krachten moeten de motorkracht exact opheffen: F_tegen = 1500 N."
    },
    {
      "type": "mc",
      "vraag": "Wat lees je af aan de <b>steilheid (helling)</b> van de grafieklijn in een <b>(s,t)-diagram</b>?",
      "opties": [
        "De snelheid van het voorwerp",
        "De versnelling van het voorwerp",
        "De resulterende kracht op het voorwerp",
        "De totale verrichte arbeid"
      ],
      "antwoord": 0,
      "uitleg": "In een afstand-tijddiagram is de helling Δs / Δt gelijk aan de snelheid. Hoe steiler de lijn, hoe groter de snelheid."
    },
    {
      "type": "mc",
      "vraag": "Een voorwerp met een massa van 4,0 kg ondervindt een resulterende kracht van 12 N. Hoe groot is de versnelling?",
      "opties": [
        "48 m/s²",
        "0,33 m/s²",
        "16 m/s²",
        "3,0 m/s²"
      ],
      "antwoord": 3,
      "uitleg": "Volgens de tweede wet van Newton geldt Fres = m · a, dus a = Fres / m = 12 N / 4,0 kg = 3,0 m/s²."
    },
    {
      "type": "mc",
      "vraag": "Hoe bereken je de afgelegde afstand uit een <b>(v,t)-diagram</b>?",
      "opties": [
        "Door de helling van de lijn te delen door de tijd",
        "Door de eindsnelheid te vermenigvuldigen met de versnelling",
        "Door de oppervlakte onder de grafieklijn te bepalen",
        "Door de verticale aswaarde op t = 0 af te lezen"
      ],
      "antwoord": 2,
      "uitleg": "De oppervlakte onder de grafieklijn in een (v,t)-diagram is gelijk aan de afgelegde afstand s (snelheid × tijd = afstand)."
    },
    {
      "type": "mc",
      "vraag": "Een scooterrijder rijdt met 10 m/s en remt af tot stilstand met een constante vertraging in 4,0 s. Wat is de afgelegde remweg?",
      "opties": [
        "20 meter",
        "40 meter",
        "10 meter",
        "2,5 meter"
      ],
      "antwoord": 0,
      "uitleg": "v_gem = (10 + 0) / 2 = 5,0 m/s. De remweg is s_rem = v_gem · t_rem = 5,0 m/s · 4,0 s = 20 meter."
    },
    {
      "type": "mc",
      "vraag": "Een hijskraan tilt een vracht van 500 kg over 6,0 meter hoogte omhoog (neem g = 10 N/kg). Hoeveel arbeid verricht de kraan?",
      "opties": [
        "3000 Joule",
        "50 kilojoule",
        "30 kilojoule",
        "83,3 Joule"
      ],
      "antwoord": 2,
      "uitleg": "F_z = m · g = 500 kg · 10 N/kg = 5000 N. Arbeid W = F · s = 5000 N · 6,0 m = 30 000 J = 30 kJ."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de remweg als een automobilist zijn snelheid verhoogt van 40 km/h naar 120 km/h?",
      "opties": [
        "De remweg wordt 3 keer zo lang",
        "De remweg wordt 9 keer zo lang",
        "De remweg wordt 6 keer zo lang",
        "De remweg wordt 16 keer zo lang"
      ],
      "antwoord": 1,
      "uitleg": "De snelheid wordt 3 keer zo groot (120 / 40 = 3). De remweg schaalt kwadratisch: (3)² = 9 keer zo lang."
    },
    {
      "type": "mc",
      "vraag": "Waarom blijft een hockeybal op glad ijs veel langer doorglijden dan op een grasveld?",
      "opties": [
        "Omdat de zwaartekracht op ijs veel minder sterk is",
        "Omdat de wrijvingskracht op ijs groter is dan de motorkracht",
        "Omdat de bal op ijs een veel grotere massa krijgt",
        "Omdat de tegenwerkende wrijvingskracht op glad ijs zeer klein is"
      ],
      "antwoord": 3,
      "uitleg": "Volgens de eerste wet van Newton behoudt een voorwerp zijn snelheid zolang er geen netto tegenkracht werkt; op glad ijs is de wrijving nagenoeg verwaarloosbaar."
    },
    {
      "type": "mc",
      "vraag": "Een auto heeft een massa van 1000 kg en accelereert met 2,5 m/s². De wrijvingskrachten bedragen samen 400 N. Hoe groot is de voorwaartse motorkracht?",
      "opties": [
        "2500 N",
        "2100 N",
        "400 N",
        "2900 N"
      ],
      "antwoord": 3,
      "uitleg": "Fres = m · a = 1000 kg · 2,5 m/s² = 2500 N. Omdat Fres = F_motor - F_wrijving, geldt F_motor = Fres + F_wrijving = 2500 N + 400 N = 2900 N."
    },
    {
      "type": "mc",
      "vraag": "Welke passieve veiligheidsvoorziening zorgt ervoor dat de vertragingstijd van het menselijk lichaam tijdens een crash wordt verlengd?",
      "opties": [
        "De stijve veiligheidskooi rond de passagiersruimte",
        "De kreukelzone en de meerekende veiligheidsgordel",
        "Het antiblokkeersysteem (ABS) van de remmen",
        "De achteruitrijcamera op de achterklep"
      ],
      "antwoord": 1,
      "uitleg": "Kreukelzones, meerekende gordels en airbags vervormen gecontroleerd, waardoor de botstijd Δt toeneemt en de kracht F daalt."
    },
    {
      "type": "mc",
      "vraag": "Een hardloper rent 400 meter in 50 seconden. Wat is zijn gemiddelde snelheid in kilometer per uur?",
      "opties": [
        "8,0 km/h",
        "20 km/h",
        "28,8 km/h",
        "32,4 km/h"
      ],
      "antwoord": 2,
      "uitleg": "v_gem = s / t = 400 m / 50 s = 8,0 m/s. Omrekenen naar km/h: 8,0 · 3,6 = 28,8 km/h."
    },
    {
      "type": "mc",
      "vraag": "In welke situatie wordt er natuurkundig gezien <b>negatieve arbeid</b> verricht?",
      "opties": [
        "Wanneer een parachutist wordt afgeremd door de luchtweerstand",
        "Wanneer een raketmotor een ruimteschip versnelt",
        "Wanneer een kraan een container omhoog hijst",
        "Wanneer een appel uit een boom naar beneden valt"
      ],
      "antwoord": 0,
      "uitleg": "De luchtweerstand werkt omhoog terwijl de parachutist naar beneden beweegt; de kracht werkt tegen de beweging in en verricht dus negatieve arbeid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de resulterende kracht op een bewegend voorwerp nul is, komt het voorwerp binnen enkele seconden tot stilstand.",
      "antwoord": false,
      "uitleg": "Onwaar: Als Fres = 0 N, blijft de snelheid onveranderd en beweegt het voorwerp met constante snelheid in een rechte lijn door (eerste wet van Newton)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De totale stopafstand van een auto is gelijk aan de reactieafstand plus de remweg.",
      "antwoord": true,
      "uitleg": "Waar: De totale afstand vanaf het zien van een gevaar tot volledige stilstand is de som van reactieafstand en remweg: s_stop = s_reactie + s_rem."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kracht die onder een hoek van 90° (loodrecht) op de bewegingsrichting staat, verricht geen mechanische arbeid.",
      "antwoord": true,
      "uitleg": "Waar: Omdat de krachtcomponent in de bewegingsrichting nul is, is de verrichte arbeid exact 0 Joule."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een zware vrachtwagen en een lichte bromfiets hebben bij dezelfde snelheid en gelijke remkracht exact dezelfde remweg.",
      "antwoord": false,
      "uitleg": "Onwaar: De vrachtwagen heeft door zijn grote massa veel meer traagheid (a = F/m is kleiner) en veel meer kinetische energie, waardoor de remweg veel langer is."
    },
    {
      "type": "invul",
      "vraag": "Een kracht van 45 N verplaatst een kist over een afstand van 8,0 meter in de richting van de kracht. Bereken de verrichte arbeid in Joule.",
      "antwoord": "360|360 J|360 Joule",
      "uitleg": "W = F · s = 45 N · 8,0 m = 360 Joule."
    },
    {
      "type": "invul",
      "vraag": "Een scooter rijdt met 15 m/s. De bestuurder heeft een reactietijd van 0,8 s. Hoeveel meter legt de scooter af tijdens de reactietijd?",
      "antwoord": "12|12 m|12 meter",
      "uitleg": "s_reactie = v · t_r = 15 m/s · 0,8 s = 12 meter."
    },
    {
      "type": "open",
      "vraag": "Beschrijf wat er gebeurt met de snelheid van een voorwerp wanneer de resulterende kracht in dezelfde richting werkt als de beweging.",
      "modelantwoord": "Wanneer de resulterende kracht in de bewegingsrichting werkt, versnelt het voorwerp (de snelheid neemt toe) volgens de tweede wet van Newton (Fres = m · a).",
      "minTreffers": 1,
      "sleutelwoorden": [
        "versnelt/versnelling/toeneemt",
        "fres = m/newton"
      ],
      "uitleg": "Een resulterende kracht in de bewegingsrichting levert een positieve versnelling waardoor de snelheid toeneemt."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom het dragen van een veiligheidsgordel in combinatie met een kreukelzone de kans op ernstig letsel verkleint.",
      "modelantwoord": "De kreukelzone en de meerekende gordel verlengen samen de vertragingstijd (de botstijd Δt) van het lichaam. Omdat F = m · Δv / Δt daalt de piekbelasting (kracht) op de inzittenden aanzienlijk. Bovendien voorkomt de gordel dat de inzittende hard tegen het stuur of de voorruit slaat.",
      "minTreffers": 2,
      "sleutelwoorden": [
        "vertragingstijd/botstijd/tijd verlengen",
        "piekbelasting/kracht daalt/kleinere kracht"
      ],
      "uitleg": "Door de verlengde vertragingstijd Δt daalt de uitgeoefende impactkracht F volgens F = m · Δv / Δt en wordt doorschieten voorkomen."
    }
  ]
});
