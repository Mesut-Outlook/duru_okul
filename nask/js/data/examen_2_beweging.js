/* Oefentoets 2 — Snelheid & Beweging (Hoofdstuk 4) */
DURU.registerExamen({
  id: "toets-h4-beweging",
  titel: "Oefentoets H4 — Snelheid & Beweging",
  vak: "Snelheid · Hoofdstuk 4",
  icoon: "🚀",
  duurMin: 20,
  vragen: [

    /* ── MEERKEUZE (10) ── */

    { type: "mc",
      vraag: "Een trein legt 360 km af in 4 uur. Wat is de gemiddelde snelheid?",
      opties: ["90 km/u", "364 km/u", "1440 km/u", "356 km/u"], antwoord: 0,
      uitleg: "snelheid = afstand : tijd = 360 : 4 = <b>90 km/u</b>." },

    { type: "mc",
      vraag: "Een hardloper sprint met 8 m/s. Hoeveel meter legt hij af in 15 seconden?",
      opties: ["120 m", "60 m", "23 m", "1,9 m"], antwoord: 0,
      uitleg: "afstand = snelheid × tijd = 8 × 15 = <b>120 m</b>." },

    { type: "mc",
      vraag: "Een fietser rijdt 90 km met een gemiddelde snelheid van 18 km/u. Hoe lang is hij onderweg?",
      opties: ["5 uur", "1620 uur", "72 uur", "108 uur"], antwoord: 0,
      uitleg: "tijd = afstand : snelheid = 90 : 18 = <b>5 uur</b>." },

    { type: "mc",
      vraag: "Welke snelheid in m/s hoort bij 72 km/u?",
      opties: ["20 m/s", "259,2 m/s", "72 m/s", "0,02 m/s"], antwoord: 0,
      uitleg: "km/u omrekenen naar m/s: deel door 3,6. → 72 : 3,6 = <b>20 m/s</b>." },

    { type: "mc",
      vraag: "Een schaatser rijdt 15 m/s. Hoe snel is dat in km/u?",
      opties: ["54 km/u", "4,2 km/u", "15 km/u", "150 km/u"], antwoord: 0,
      uitleg: "m/s omrekenen naar km/u: vermenigvuldig met 3,6. → 15 × 3,6 = <b>54 km/u</b>." },

    { type: "mc",
      vraag: "Een auto rijdt 10 minuten met 60 km/u en daarna 20 minuten met 90 km/u. Wat is de totale afstand?",
      opties: ["40 km", "150 km", "75 km", "30 km"], antwoord: 0,
      uitleg: "10 min = 1/6 uur → 60 × 1/6 = 10 km. 20 min = 1/3 uur → 90 × 1/3 = 30 km. Totaal: 10 + 30 = <b>40 km</b>." },

    { type: "mc",
      vraag: "Reactieafstand = snelheid (m/s) × reactietijd. Een auto rijdt 25 m/s en de bestuurder heeft een reactietijd van 0,8 s. Wat is de reactieafstand?",
      opties: ["20 m", "25 m", "31,25 m", "10 m"], antwoord: 0,
      uitleg: "reactieafstand = 25 × 0,8 = <b>20 m</b>." },

    { type: "mc",
      vraag: "Wat is de stopafstand?",
      opties: ["Reactieafstand + remafstand", "Alleen de remafstand", "Rijafstand − remafstand", "Reactieafstand × remafstand"], antwoord: 0,
      uitleg: "Stopafstand = <b>reactieafstand + remafstand</b>. Zolang je nog niet remt, rij je de reactieafstand door." },

    { type: "mc",
      vraag: "In een snelheid-tijddiagram is een horizontale lijn te zien. Wat betekent dit?",
      opties: ["De snelheid is constant", "Het object staat stil", "Het object versnelt", "Het object vertraagt"], antwoord: 0,
      uitleg: "Een <b>horizontale lijn</b> in een v,t-diagram betekent: de snelheid verandert niet → <b>constante snelheid</b>." },

    { type: "mc",
      vraag: "In een afstand-tijddiagram loopt de lijn steeds steiler omhoog. Wat betekent dit?",
      opties: ["Het object versnelt", "Het object rijdt met constante snelheid", "Het object staat stil", "Het object vertraagt"], antwoord: 0,
      uitleg: "Een steeds steilere lijn in een a,t-diagram betekent: in dezelfde tijd wordt steeds <b>meer</b> afstand afgelegd → het object <b>versnelt</b>." },

    /* ── WAAR/ONWAAR (6) ── */

    { type: "waaronwaar",
      vraag: "Om van km/u naar m/s te rekenen, vermenigvuldig je met 3,6.",
      antwoord: false,
      uitleg: "Onwaar. Om van km/u naar m/s te rekenen, <b>deel</b> je door 3,6. Vermenigvuldigen met 3,6 is de omgekeerde omrekening (m/s → km/u)." },

    { type: "waaronwaar",
      vraag: "36 km/u is hetzelfde als 10 m/s.",
      antwoord: true,
      uitleg: "Waar. 36 : 3,6 = <b>10 m/s</b>." },

    { type: "waaronwaar",
      vraag: "De reactieafstand wordt groter als je sneller rijdt.",
      antwoord: true,
      uitleg: "Waar. Reactieafstand = snelheid × reactietijd. Bij een hogere snelheid leg je in dezelfde reactietijd een <b>grotere</b> afstand af." },

    { type: "waaronwaar",
      vraag: "Als je moe bent, wordt je reactietijd korter.",
      antwoord: false,
      uitleg: "Onwaar. Vermoeidheid maakt je trager, dus je reactietijd wordt <b>langer</b>. Dat is gevaarlijk in het verkeer." },

    { type: "waaronwaar",
      vraag: "In een snelheid-tijddiagram stelt de oppervlakte onder de lijn de afgelegde afstand voor.",
      antwoord: true,
      uitleg: "Waar. De oppervlakte onder de lijn in een v,t-diagram is snelheid × tijd = <b>afstand</b>." },

    { type: "waaronwaar",
      vraag: "Een auto die vertraagt, heeft een stijgende lijn in het snelheid-tijddiagram.",
      antwoord: false,
      uitleg: "Onwaar. Bij vertragen <b>daalt</b> de snelheid; de lijn gaat dus <b>omlaag</b> in het v,t-diagram." },

    /* ── OPEN (9) ── */

    { type: "open",
      vraag: "Een fietser rijdt 12 km in 30 minuten. Bereken de gemiddelde snelheid in km/u. Leg je berekening uit.",
      sleutelwoorden: ["30 minuten/0,5 uur", "24/vierentwintig", "afstand/tijd/deel"],
      minTreffers: 2,
      modelantwoord: "30 minuten = 0,5 uur. snelheid = 12 : 0,5 = 24 km/u.",
      uitleg: "Zet 30 minuten om: 30 min = <b>0,5 uur</b>. Dan: snelheid = 12 : 0,5 = <b>24 km/u</b>." },

    { type: "open",
      vraag: "Leg uit waarom alcohol drinken gevaarlijk is in het verkeer. Gebruik de begrippen reactietijd en reactieafstand.",
      sleutelwoorden: ["reactietijd/langer/groter", "reactieafstand/groter/meer", "alcohol/drinken"],
      minTreffers: 2,
      modelantwoord: "Alcohol vergroot de reactietijd. Daardoor wordt ook de reactieafstand groter: je rijdt verder door voordat je remt.",
      uitleg: "Alcohol → <b>langere reactietijd</b> → <b>grotere reactieafstand</b> → meer kans op een ongeluk." },

    { type: "open",
      vraag: "Beschrijf wat je ziet in een afstand-tijddiagram wanneer een object stilstaat.",
      sleutelwoorden: ["horizontale/platte/rechte lijn", "afstand/verandert niet/gelijk", "stil/stilstaan"],
      minTreffers: 1,
      modelantwoord: "Je ziet een horizontale lijn: de afstand verandert niet, want het object staat stil.",
      uitleg: "Stilstaan = geen verandering in afstand → <b>horizontale lijn</b> in het a,t-diagram." },

    { type: "open",
      vraag: "Een trein rijdt 2 uur met 120 km/u, maakt daarna een tussenstop van 30 minuten en rijdt dan nog 1 uur met 100 km/u. Bereken de gemiddelde snelheid over de hele reis.",
      sleutelwoorden: ["340/driehonderd veertig", "gemiddelde/totaal/3,5/3½/drieëneenhalf"],
      minTreffers: 1,
      modelantwoord: "Afstand: 2×120 + 1×100 = 240 + 100 = 340 km. Tijd: 2 + 0,5 + 1 = 3,5 uur. Gemiddelde snelheid = 340 : 3,5 ≈ 97,1 km/u.",
      uitleg: "Totale afstand = 240 + 100 = <b>340 km</b>. Totale tijd = 3,5 uur (de stop telt mee!). v = 340 : 3,5 ≈ <b>97,1 km/u</b>." },

    { type: "open",
      vraag: "Wat is het verschil tussen remafstand en stopafstand? Geef ook aan welke het grootst is.",
      sleutelwoorden: ["remafstand/remmen", "stopafstand/reactieafstand", "groter/stopafstand is groter"],
      minTreffers: 2,
      modelantwoord: "Remafstand is de afstand die je aflegt terwijl je aan het remmen bent. Stopafstand is reactieafstand plus remafstand, dus groter.",
      uitleg: "<b>Remafstand</b> = afstand tijdens het remmen. <b>Stopafstand</b> = reactieafstand + remafstand. Stopafstand is dus altijd <b>groter</b>." },

    { type: "open",
      vraag: "Noem drie dingen die je reactietijd kunnen vergroten.",
      sleutelwoorden: ["alcohol/drinken", "moe/vermoeidheid/slaperig", "telefoon/afgeleid/afleiding", "medicijnen/drugs"],
      minTreffers: 2,
      modelantwoord: "Bijvoorbeeld: alcohol, vermoeidheid, en gebruik van de telefoon achter het stuur.",
      uitleg: "Reactietijd wordt vergroot door <b>alcohol</b>, <b>vermoeidheid</b>, <b>afleiding</b> (telefoon) en sommige <b>medicijnen</b>." },

    { type: "open",
      vraag: "Een hardloper heeft een gemiddelde snelheid van 5 m/s. Bereken hoe lang hij over 2 km doet. Geef je antwoord in minuten.",
      sleutelwoorden: ["400/vierhonderd seconden", "6,67/6 minuten/7 minuten/6 minuten 40"],
      minTreffers: 1,
      modelantwoord: "2 km = 2000 m. tijd = afstand : snelheid = 2000 : 5 = 400 seconden = 6 minuten en 40 seconden.",
      uitleg: "2 km = 2000 m. tijd = 2000 : 5 = <b>400 s</b> = 6 min 40 s ≈ <b>6,67 minuten</b>." },

    { type: "open",
      vraag: "Beschrijf het verschil tussen een versnellende en een vertragende beweging in een snelheid-tijddiagram.",
      sleutelwoorden: ["stijgt/omhoog/hoger", "daalt/omlaag/lager", "stijgende lijn/dalende lijn"],
      minTreffers: 2,
      modelantwoord: "Bij versnellen stijgt de lijn (snelheid neemt toe). Bij vertragen daalt de lijn (snelheid neemt af).",
      uitleg: "<b>Versnellen</b> → lijn gaat <b>omhoog</b>. <b>Vertragen</b> → lijn gaat <b>omlaag</b>. Allebei in het v,t-diagram." },

    { type: "open",
      vraag: "Een auto rijdt 90 km/u. Reken dit om naar m/s en leg uit hoe je dat doet.",
      sleutelwoorden: ["25/vijfentwintig m/s", "deel/gedeeld/3,6"],
      minTreffers: 1,
      modelantwoord: "Deel de snelheid door 3,6: 90 : 3,6 = 25 m/s.",
      uitleg: "km/u → m/s: <b>deel door 3,6</b>. → 90 : 3,6 = <b>25 m/s</b>." },

    /* ── INVUL (3) ── */

    { type: "invul",
      vraag: "Vul aan: Om een snelheid van km/u om te rekenen naar m/s, deel je de snelheid door ______.",
      antwoord: "3,6|3.6|drie komma zes",
      uitleg: "km/u → m/s = <b>delen door 3,6</b>. Bijv. 36 km/u : 3,6 = 10 m/s." },

    { type: "invul",
      vraag: "Vul aan: De stopafstand bestaat uit de reactieafstand en de ______.",
      antwoord: "remafstand|rem afstand",
      uitleg: "Stopafstand = reactieafstand + <b>remafstand</b>." },

    { type: "invul",
      vraag: "Een fietser rijdt met 10 m/s. Uitgedrukt in km/u is dat ______ km/u.",
      antwoord: "36|zesendertig",
      uitleg: "m/s → km/u: vermenigvuldig met 3,6. → 10 × 3,6 = <b>36 km/u</b>." }

  ]
});
