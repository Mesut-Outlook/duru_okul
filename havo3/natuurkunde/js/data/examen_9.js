/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 9 — Vermogen, Energieverbruik & kWh
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-9",
  "titel": "Toets 9 — Vermogen, Energieverbruik & kWh",
  "vak": "Natuurkunde · HAVO 3 (H2)",
  "icoon": "⚡",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de officiële eenheid van <b>elektrisch vermogen (P)</b>?",
      "opties": [
        "Watt (W)",
        "Joule (J)",
        "Volt (V)",
        "Ampère (A)"
      ],
      "antwoord": 0,
      "uitleg": "Vermogen is de hoeveelheid energie die een apparaat per seconde omzet en wordt gemeten in Watt (W). 1 W = 1 J/s."
    },
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je om het elektrisch vermogen te berekenen uit spanning en stroomsterkte?",
      "opties": [
        "P = U / I",
        "P = U × I",
        "P = I / U",
        "P = E × t"
      ],
      "antwoord": 1,
      "uitleg": "P = U × I (Vermogen in Watt = Spanning in Volt × Stroomsterkte in Ampère)."
    },
    {
      "type": "invul",
      "vraag": "Een stofzuiger werkt op 230 V en trekt een stroom van 4,0 A. Bereken het vermogen in Watt.",
      "antwoord": "920|920 W|920 watt",
      "uitleg": "P = U × I = 230 V × 4,0 A = 920 W."
    },
    {
      "type": "invul",
      "vraag": "Een waterkoker heeft een vermogen van 2300 W op 230 V. Hoeveel Ampère stroom loopt er door het verwarmingselement?",
      "antwoord": "10|10 A|10,0|10,0 A",
      "uitleg": "I = P / U = 2300 W / 230 V = 10 A."
    },
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je om het totale <b>energieverbruik (E)</b> van een apparaat te berekenen?",
      "opties": [
        "E = P / t",
        "E = U × R",
        "E = P × t",
        "E = I / t"
      ],
      "antwoord": 2,
      "uitleg": "E = P × t (Energie = Vermogen × Tijd)."
    },
    {
      "type": "invul",
      "vraag": "Een LED-lamp van 10 W brandt gedurende 300 seconden. Hoeveel Joule elektrische energie heeft de lamp verbruikt?",
      "antwoord": "3000|3000 J|3.000|3000J|3 kJ",
      "uitleg": "E = P × t = 10 W × 300 s = 3000 Joule (3 kJ)."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel Joule (J) is precies <b>1 kilowattuur (kWh)</b>?",
      "opties": [
        "1.000 J",
        "60.000 J",
        "36.000.000 J",
        "3.600.000 J (3,6 MJ)"
      ],
      "antwoord": 3,
      "uitleg": "1 kWh = 1000 W × 3600 seconden = 3.600.000 Joule = 3,6 MJ."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het kilowattuur (kWh) is een eenheid van elektrisch vermogen.",
      "antwoord": false,
      "uitleg": "Niet waar. Kilowattuur (kWh) is een eenheid van <b>energie</b> (net als Joule). Kilowatt (kW) is de eenheid van vermogen."
    },
    {
      "type": "invul",
      "vraag": "Een elektrisch kacheltje van 2,0 kW staat 4,5 uur aan. Hoeveel kWh energie heeft het kacheltje verbruikt?",
      "antwoord": "9|9 kWh|9,0|9,0 kWh",
      "uitleg": "E = P × t = 2,0 kW × 4,5 uur = 9 kWh."
    },
    {
      "type": "invul",
      "vraag": "De elektriciteitsprijs is € 0,30 per kWh. Wat kost het laten branden van een kachel die 9 kWh heeft verbruikt (in euro's)?",
      "antwoord": "2,70|2,7|€ 2,70|€2,70",
      "uitleg": "Kosten = 9 kWh × € 0,30 = € 2,70."
    },
    {
      "type": "mc",
      "vraag": "Een magnetron heeft een vermogen van 800 W. Hoeveel kW is dat?",
      "opties": [
        "0,8 kW",
        "8 kW",
        "0,08 kW",
        "80 kW"
      ],
      "antwoord": 0,
      "uitleg": "800 W / 1000 = 0,8 kW."
    },
    {
      "type": "invul",
      "vraag": "Een computer verbruikt 150 W (0,15 kW). Een leerling gebruikt de computer 40 uur per maand. Hoeveel kWh is het maandverbruik?",
      "antwoord": "6|6 kWh|6,0",
      "uitleg": "E = 0,15 kW × 40 h = 6 kWh."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een apparaat met een energielabel A is energiezuiniger en heeft een hoger rendement dan een vergelijkbaar apparaat met label G.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Label A staat voor zeer efficiënt energiegebruik met weinig ongewenst warmteverlies."
    },
    {
      "type": "mc",
      "vraag": "Bij een oude gloeilamp van 60 W wordt slechts 3 W omgezet in nuttig licht. Wat gebeurt er met de overige 57 W?",
      "opties": [
        "Die verdwijnt in de stroomdraad",
        "Die wordt omgezet in ongewenste warmte",
        "Die wordt teruggestuurd naar de centrale",
        "Die wordt opgeslagen in de fitting"
      ],
      "antwoord": 1,
      "uitleg": "95% van de energie bij een gloeilamp gaat verloren als warmte (rendement is slechts 5%)."
    },
    {
      "type": "invul",
      "vraag": "Wat is het rendement van de gloeilamp uit de vorige vraag (3 W nuttig licht uit 60 W totaal vermogen) in procenten?",
      "antwoord": "5|5%|5 procent",
      "uitleg": "Rendement η = (E_nuttig / E_totaal) × 100% = (3 / 60) × 100% = 5%."
    },
    {
      "type": "mc",
      "vraag": "Wat meet de <b>kwh-meter (elektriciteitsmeter)</b> in de meterkast?",
      "opties": [
        "De gemiddelde netspanning in Volt",
        "De momentane stroomsterkte in Ampère",
        "De totale hoeveelheid afgenomen elektrische energie in kWh",
        "Het maximale piekvermogen van het huis"
      ],
      "antwoord": 2,
      "uitleg": "De kWh-meter meet de totale cumulatieve verbruikte elektrische energie in kilowattuur."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je twee apparaten van 1000 W elk tegelijk 1 uur aanzet, verbruiken ze samen evenveel energie als één apparaat van 2000 W dat 1 uur aanstaat.",
      "antwoord": true,
      "uitleg": "Waar. In beide gevallen is E = 2 kW × 1 h = 2 kWh."
    },
    {
      "type": "invul",
      "vraag": "Een wasdroger heeft een vermogen van 2500 W (2,5 kW) en draait een programma van 1,5 uur. Bij een stroomprijs van € 0,40 per kWh, hoeveel euro kost deze droogbeurt?",
      "antwoord": "1,50|1,5|€ 1,50|€1,50",
      "uitleg": "E = 2,5 kW × 1,5 h = 3,75 kWh. Kosten = 3,75 kWh × € 0,40 = € 1,50."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom het vervangen van oude 50 W halogeenspots door 5 W LED-lampen op jaarbasis veel geld bespaart, terwijl de lichtopbrengst hetzelfde blijft.",
      "sleutelwoorden": [
        "lager vermogen/minder Watt",
        "minder energie/minder kWh",
        "rendement/minder warmte"
      ],
      "minTreffers": 2,
      "modelantwoord": "Een 5 W LED levert evenveel nuttig licht als een 50 W halogeenlamp omdat LED-verlichting een veel hoger rendement heeft (verliest nauwelijks energie aan warmte). Omdat het vermogen 10 keer zo laag is (5 W i.p.v. 50 W), verbruikt de lamp volgens E = P × t tien keer minder kilowattuur (kWh) aan energie over dezelfde branduren, waardoor de elektriciteitskosten met 90% dalen.",
      "uitleg": "Hoger rendement -> lager elektrisch vermogen voor zelfde licht -> drastisch minder kWh-verbruik."
    },
    {
      "type": "open",
      "vraag": "Een apparaat staat het hele jaar onnodig in de <b>stand-by-stand</b> met een continu vermogen van 10 W. Bereken het jaarverbruik in kWh (1 jaar = 8760 uur) en leg uit waarom sluipverbruik een probleem is.",
      "sleutelwoorden": [
        "87,6 kWh / 88 kWh",
        "E = 0,010 kW * 8760 h",
        "sluipverbruik kost onnodig geld/energie"
      ],
      "minTreffers": 2,
      "modelantwoord": "P = 10 W = 0,010 kW. E = P × t = 0,010 kW × 8760 uur = 87,6 kWh per jaar. Bij € 0,35 per kWh kost dit apparaat jaarlijks circa € 30,- aan ongebruikte stand-by-stroom. Sluipverbruik van meerdere apparaten bij elkaar telt op tot honderden kilowatturen per jaar, wat zorgt voor onnodige energiekosten en extra belasting van het milieu.",
      "uitleg": "Jaarlijks 87,6 kWh continu verlies; vermenigvuldigd over meerdere apparaten leidt dat tot flinke kosten."
    }
  ]
});
