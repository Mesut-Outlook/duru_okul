/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 5 — Integrale Eindtoets Hoofdstuk 1 (Kracht & Beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-5",
  "hoofdstuk": 1,
  "titel": "Toets 5 — Integrale Eindtoets Hoofdstuk 1 (Kracht & Beweging)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🏆",
  "duurMin": 35,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een parachutist van 80 kg valt met een constante snelheid van 55 m/s naar beneden (neem g = 9,81 N/kg). Hoe groot is de opwaartse <b>luchtweerstandskracht</b> op dat moment?",
      "opties": [
        "785 N",
        "440 N",
        "0 N",
        "4400 N"
      ],
      "antwoord": 0,
      "uitleg": "Omdat de snelheid constant is (a = 0), is F_res = 0 N. De opwaartse luchtweerstand moet gelijk zijn aan de neerwaartse zwaartekracht: F_lucht = F_z = m × g = 80 kg × 9,81 N/kg = 785 N."
    },
    {
      "type": "mc",
      "vraag": "Welke grootheid vind je door de <b>helling (steilheid)</b> van een <b>(v,t)-diagram</b> te bepalen?",
      "opties": [
        "De afgelegde afstand",
        "De versnelling (a)",
        "De arbeid (W)",
        "De resulterende kracht direct in Newton"
      ],
      "antwoord": 1,
      "uitleg": "De helling in een (v,t)-diagram is verticaal gedeeld door horizontaal: Δv / Δt = versnelling a."
    },
    {
      "type": "invul",
      "vraag": "Een elektrische auto trekt op vanuit stilstand en bereikt na 4,0 seconden een snelheid van 72 km/h (20 m/s). Bereken de versnelling a in m/s².",
      "antwoord": "5|5,0|5 m/s²|5,0 m/s²",
      "uitleg": "a = Δv / Δt = 20 m/s / 4,0 s = 5,0 m/s²."
    },
    {
      "type": "mc",
      "vraag": "Als dezelfde elektrische auto een massa heeft van 1500 kg en accelereert met a = 5,0 m/s², hoeveel resulterende kracht (F_res) levert de motor dan netto?",
      "opties": [
        "300 N",
        "3000 N",
        "7500 N",
        "6000 N"
      ],
      "antwoord": 2,
      "uitleg": "F_res = m × a = 1500 kg × 5,0 m/s² = 7500 N (7,5 kN)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De oppervlakte onder een <b>(v,t)-grafiek</b> stelt altijd de totale <b>afgelegde afstand (s)</b> voor, ongeacht of de beweging eenparig of versneld is.",
      "antwoord": true,
      "uitleg": "Waar. De oppervlakte onder de (v,t)-curve is altijd gelijk aan de afgelegde afstand s."
    },
    {
      "type": "invul",
      "vraag": "Een lift met een massa van 600 kg wordt met een constante snelheid 12 meter omhoog gehesen (neem g = 10 N/kg). Hoeveel kJ arbeid verricht de trekkabel?",
      "antwoord": "72|72 kJ|72,0|72000",
      "uitleg": "F_kabel = F_z = m × g = 600 kg × 10 N/kg = 6000 N. W = F × s = 6000 N × 12 m = 72.000 J = 72 kJ."
    },
    {
      "type": "mc",
      "vraag": "Een bestuurder rijdt met 108 km/h op de snelweg. Hoeveel meter legt de auto af in <b>1 seconde reactietijd</b>?",
      "opties": [
        "15 meter",
        "25 meter",
        "108 meter",
        "30 meter"
      ],
      "antwoord": 3,
      "uitleg": "108 km/h / 3,6 = 30 m/s. In 1 seconde reactietijd legt de auto s_reactie = 30 m/s × 1 s = 30 meter af."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de nettokracht op een voorwerp nul is (F_res = 0 N), kan het voorwerp toch een snelheid hebben van 100 km/h.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Volgens de eerste wet van Newton betekent F_res = 0 N dat de snelheid niet verandert (constante snelheid in een rechte lijn). Het voorwerp hoeft dus niet stil te staan!"
    },
    {
      "type": "invul",
      "vraag": "Een fietser rijdt met 6,0 m/s. Door de remmen in te knijpen remt hij af met een constante vertraging van 1,5 m/s². Hoeveel seconden duurt het voor hij stilstaat?",
      "antwoord": "4|4,0|4 s|4,0 s|4 sec",
      "uitleg": "t_rem = v / a = 6,0 m/s / 1,5 m/s² = 4,0 seconden."
    },
    {
      "type": "mc",
      "vraag": "Een slee wordt over een afstand van 40 meter over sneeuw getrokken met een trekkracht van 80 N. De wrijvingskracht van de sneeuw is 20 N tegenwerkend. Hoeveel <b>nuttige arbeid</b> is er netto aan de versnelling van de slee geleverd?",
      "opties": [
        "2400 J",
        "800 J",
        "3200 J",
        "4000 J"
      ],
      "antwoord": 0,
      "uitleg": "F_res = 80 N - 20 N = 60 N. W_netto = F_res × s = 60 N × 40 m = 2400 Joule."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als een auto 3 keer zo snel rijdt (bijv. 90 km/h i.p.v. 30 km/h), wordt de remweg <b>9 keer zo lang</b> (3² = 9).",
      "antwoord": true,
      "uitleg": "Waar. De remweg schaalt kwadratisch met de snelheid: (3)² = 9 maal zo lang."
    },
    {
      "type": "invul",
      "vraag": "Een speerwerper oefent tijdens zijn worp een gemiddelde kracht van 350 N uit over een afzet-afstand van 1,2 meter. Bereken de verrichte arbeid op de speer in Joule.",
      "antwoord": "420|420 J|420,0",
      "uitleg": "W = F × s = 350 N × 1,2 m = 420 Joule."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de bewegingsenergie van een auto als deze via een noodstop tot stilstand wordt gebracht op een droge weg?",
      "opties": [
        "De energie wordt vernietigd",
        "De bewegingsenergie wordt door wrijving omgezet in warmte in de remschijven en banden",
        "De bewegingsenergie wordt omgezet in zwaarte-energie in de banden",
        "De energie verdwijnt in de kreukelzone zonder warmteontwikkeling"
      ],
      "antwoord": 1,
      "uitleg": "Energie kan nooit verdwijnen. Door wrijvingsarbeid (negatieve arbeid) wordt de kinetische energie omgezet in warmte en een beetje geluid."
    },
    {
      "type": "invul",
      "vraag": "Een kogel van 5,0 kg wordt weggestoten met een versnelling van 24 m/s². Hoeveel Newton spierkracht (resulterende kracht) werkte er op de kogel tijdens het afstoten?",
      "antwoord": "120|120 N|120,0",
      "uitleg": "F_res = m × a = 5,0 kg × 24 m/s² = 120 N."
    },
    {
      "type": "mc",
      "vraag": "In een (s,t)-diagram van een fietser zie je een <b>kromme lijn die steeds minder steil</b> wordt. Wat voor soort beweging is dit?",
      "opties": [
        "Eenparige beweging",
        "Versnelde beweging",
        "Vertraagde beweging",
        "Stilstand"
      ],
      "antwoord": 2,
      "uitleg": "De steilheid in een (s,t)-diagram stelt de snelheid voor. Als de grafiek minder steil wordt, neemt de snelheid af: een vertraagde beweging."
    },
    {
      "type": "waaronwaar",
      "vraag": "Zowel een kreukelzone als een airbag verminderen de letselkans door de botstijd Δt te verlengen, waardoor de vertraging a en dus de botskracht F afnemen.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. F_bots = m × (Δv / Δt). Door Δt groter te maken, wordt de kracht F kleiner."
    },
    {
      "type": "invul",
      "vraag": "Een schaatser glijdt na een eindsprint uit over het ijs. Hij heeft een massa van 70 kg en de ijs-wrijving is 14 N tegenwerkend. Wat is zijn (negatieve) vertraging in m/s²?",
      "antwoord": "0,2|0,2 m/s²|0,20",
      "uitleg": "a = F / m = 14 N / 70 kg = 0,2 m/s²."
    },
    {
      "type": "mc",
      "vraag": "Een fietser fietst in 30 seconden 150 meter en staat daarna 10 seconden stil voor het stoplicht. Wat is zijn <b>gemiddelde snelheid over de totale tijd van 40 seconden</b>?",
      "opties": [
        "15 m/s",
        "5,0 m/s",
        "7,5 m/s",
        "3,75 m/s"
      ],
      "antwoord": 3,
      "uitleg": "Totale afstand s_tot = 150 m. Totale tijd t_tot = 30 s + 10 s = 40 s. v_gem = s_tot / t_tot = 150 m / 40 s = 3,75 m/s."
    },
    {
      "type": "open",
      "vraag": "Beschrijf de drie opeenvolgende fasen van een noodstop in het verkeer vanaf het moment dat een automobilist een obstakel ziet opdoemen. Benoem per fase de bewegingssoort, de krachten en hoe de afgelegde afstand berekend wordt.",
      "sleutelwoorden": [
        "reactiefase/reactietijd/constante snelheid",
        "remfase/vertragende beweging/remkracht",
        "stopafstand is som van beide"
      ],
      "minTreffers": 2,
      "modelantwoord": "1. Reactiefase: Tijdens de reactietijd (t_r) reageert de bestuurder; de auto beweegt met constante snelheid (F_res = 0 N) en legt s_reactie = v × t_r af. 2. Remfase: Zodra het rempedaal wordt ingetrapt, levert het remsysteem een tegenwerkende remkracht; de beweging is (eenparig) vertraagd (a = F_rem / m) en legt de remweg s_rem = 0,5 × v × t_rem af. 3. Stilstand: De auto staat stil (v = 0 m/s). De totale stopafstand is s_stop = s_reactie + s_rem.",
      "uitleg": "Duidelijk onderscheid tussen reactiefase (eenparig) en remfase (vertraagd)."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom een wielrenner die 40 km/h fietst veel meer vermogen en arbeid per seconde moet leveren dan wanneer hij 20 km/h fietst. Betrek daarin de <b>luchtweerstand</b> en de formule <b>W = F × s</b>.",
      "sleutelwoorden": [
        "luchtweerstand kwadratisch/veel groter",
        "W = F * s / grotere kracht vereist meer arbeid",
        "afstand per seconde groter"
      ],
      "minTreffers": 2,
      "modelantwoord": "Bij verdubbeling van de snelheid van 20 naar 40 km/h wordt de luchtweerstandskracht (F_lucht) ongeveer vier keer zo groot (kwadratisch verband). Om een constante snelheid te houden moet de trapkracht gelijk zijn aan de luchtweerstand. Volgens W = F × s vereist een 4× zo grote kracht over dezelfde afstand 4× zoveel arbeid. Bovendien legt de wielrenner per seconde twee keer zoveel afstand af, waardoor hij in dezelfde tijd veel meer arbeid moet leveren.",
      "uitleg": "Kracht stijgt kwadratisch met de snelheid, en de verplaatsing per tijdseenheid verdubbelt ook, waardoor het benodigde vermogen enorm toeneemt."
    }
  ]
});
