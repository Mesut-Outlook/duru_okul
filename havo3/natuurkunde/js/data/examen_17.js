/* Proeftoets 17 — Natuurkunde HAVO 3: Hoofdstuk 4 (Stoffen en materialen - Deel 2)
   Focus: Paragraaf 4.2 — Temperatuur, Kelvin, warmtehoeveelheid en soortelijke warmte (Q = m * c * Delta T).
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-17",
  titel: "Toets 17 — Temperatuur, Warmte & Soortelijke Warmte",
  vak: "Natuurkunde · HAVO 3 (H4)",
  icoon: "🌡️",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is het verschil tussen de begrippen <b>temperatuur</b> en <b>warmte</b> in de natuurkunde?",
      opties: [
        "Temperatuur is een maat voor de gemiddelde bewegingssnelheid van moleculen (°C of K); warmte is een vorm van energie die overgaat van warm naar koud (Joule)",
        "Temperatuur en warmte zijn precies hetzelfde",
        "Temperatuur meet je in Joule en warmte in graden Celsius",
        "Warmte is koud en temperatuur is heet"
      ],
      antwoord: 0,
      uitleg: "Temperatuur is een toestand (gemiddelde kinetische energie van atomen); warmte Q is stromende thermische energie in Joule."
    },
    {
      type: "mc",
      vraag: "Wat is het <b>absolute nulpunt</b> van temperatuur (0 Kelvin)?",
      opties: [
        "0 °C (smeltpunt van ijs)",
        "-273,15 °C (de laagst mogelijke temperatuur waarbij moleculen vrijwel stilstaan)",
        "-100 °C",
        "-450 °C"
      ],
      antwoord: 1,
      uitleg: "0 Kelvin = -273,15 °C. Lager dan 0 K kan een temperatuur niet dalen."
    },
    {
      type: "invul",
      vraag: "Reken om: een temperatuur van <b>25 °C</b> is gelijk aan hoeveel Kelvin (K)?",
      antwoord: "298|298 K|298,15|298,15 K",
      uitleg: "T(K) = T(°C) + 273 = 25 + 273 = 298 K."
    },
    {
      type: "invul",
      vraag: "Reken om: vloeibare stikstof kookt bij <b>77 K</b>. Hoeveel graden Celsius (°C) is dat?",
      antwoord: "-196|-196 °C|-196,15",
      uitleg: "T(°C) = T(K) - 273 = 77 - 273 = -196 °C."
    },
    {
      type: "mc",
      vraag: "Welke formule gebruik je om de benodigde <b>warmtehoeveelheid (Q)</b> te berekenen om een stof op te warmen?",
      opties: [
        "Q = P × t",
        "Q = m / (c × ΔT)",
        "Q = m × c × ΔT",
        "Q = U × I"
      ],
      antwoord: 2,
      uitleg: "Q = m · c · ΔT, waarbij Q de warmte in Joule is, m de massa in kg (of g), c de soortelijke warmte en ΔT het temperatuurverschil."
    },
    {
      type: "mc",
      vraag: "Wat geeft de <b>soortelijke warmte (c)</b> van een stof aan?",
      opties: [
        "Hoe snel een stof verdampt",
        "De elektrische weerstand bij 100 °C",
        "De dichtheid van een hete stof",
        "Hoeveel Joule warmte er nodig is om 1 kg (of 1 g) van die stof 1 graad in temperatuur te laten stijgen"
      ],
      antwoord: 3,
      uitleg: "Soortelijke warmte is de stofeigenschap die aangeeft hoeveel warmte-energie 1 kg stof per graad temperatuurstijging opneemt."
    },
    {
      type: "invul",
      vraag: "De soortelijke warmte van water is 4180 J/(kg·K). Hoeveel Joule warmte is er nodig om 2,0 kg water van 20 °C naar 70 °C te verwarmen (ΔT = 50 °C)?",
      antwoord: "418000|418.000|418 kJ|418000 J|418.000 J",
      uitleg: "Q = m × c × ΔT = 2,0 kg × 4180 J/(kg·K) × 50 K = 418.000 Joule (418 kJ)."
    },
    {
      type: "waaronwaar",
      vraag: "Water heeft een opvallend <b>hoge</b> soortelijke warmte vergeleken met de meeste metalen en zand.",
      antwoord: true,
      uitleg: "Waar. Water (4180 J/kg·K) kan enorm veel warmte opslaan zonder dat de temperatuur extreem stijgt (ideaal voor centrale verwarming en koelsystemen)."
    },
    {
      type: "mc",
      vraag: "IJzer heeft een soortelijke warmte van 460 J/(kg·K) en water van 4180 J/(kg·K). Als je 1 kg ijzer en 1 kg water dezelfde hoeveelheid warmte Q toevoert:",
      opties: [
        "Stijgt de temperatuur van het ijzer veel sneller en hoger dan die van het water",
        "Stijgt de temperatuur van het water sneller",
        "Stijgen beide temperaturen precies evenveel",
        "Wordt het ijzer koud en het water heet"
      ],
      antwoord: 0,
      uitleg: "IJzer heeft een bijna 10× lagere soortelijke warmte dan water, dus warmt 1 kg ijzer bij gelijke warmtetoevoer bijna 10× zo snel op."
    },
    {
      type: "invul",
      vraag: "Een aluminium pan (m = 0,50 kg, c = 880 J/(kg·K)) koelt af van 100 °C naar 20 °C (ΔT = 80 K). Hoeveel Joule warmte staat de pan af aan de omgeving?",
      antwoord: "35200|35.200|35,2 kJ|35200 J|35.200 J",
      uitleg: "Q = m × c × ΔT = 0,50 kg × 880 J/(kg·K) × 80 K = 35.200 Joule (35,2 kJ)."
    },
    {
      type: "waaronwaar",
      vraag: "Een temperatuurstijging van 1 graad Celsius (	ext{ °C}$) is qua grootte exact gelijk aan een stijging van 	ext{ Kelvin}$ (	ext{ K}$).",
      antwoord: true,
      uitleg: "Waar. De schaalstappen van Celsius en Kelvin zijn identiek; alleen het nulpunt verschilt (0 K = -273 °C)."
    },
    {
      type: "mc",
      vraag: "Waarom warmt zand op het strand op een zonnige zomerdag veel heter op dan het zeewater, terwijl de zon op beide even sterk schijnt?",
      opties: [
        "Omdat zand donkerder is dan water",
        "Omdat zand een veel lagere soortelijke warmte heeft dan water en daardoor veel sneller in temperatuur stijgt",
        "Omdat zand zelf warmte produceert",
        "Omdat water geen zonlicht absorbeert"
      ],
      antwoord: 1,
      uitleg: "Zand heeft een veel lagere soortelijke warmte (ca. 800 J/kg·K vs. 4180 J/kg·K voor water), waardoor zand snel gloeiend heet wordt."
    },
    {
      type: "invul",
      vraag: "Een dompelaar levert 500 W aan 0,25 kg water. Hoeveel Joule warmte levert de dompelaar in 60 seconden ( = P 	imes t$)?",
      antwoord: "30000|30.000|30 kJ|30000 J",
      uitleg: "Q = P × t = 500 W × 60 s = 30.000 Joule (30 kJ)."
    },
    {
      type: "mc",
      vraag: "In de vorige vraag (Q = 30.000 J toegevoegd aan 0,25 kg water met c = 4180 J/(kg·K)): hoeveel graden stijgt de temperatuur van het water (afgerond op 1 decimaal)?",
      opties: [
        "14,4 °C",
        "50,0 °C",
        "28,7 °C",
        "71,8 °C"
      ],
      antwoord: 2,
      uitleg: "ΔT = Q / (m × c) = 30.000 / (0,25 × 4180) = 30.000 / 1045 ≈ 28,7 °C."
    },
    {
      type: "waaronwaar",
      vraag: "Bij het koken van water op 100 °C stijgt de temperatuur van het kokende water verder naar 110 °C zolang je het vuur hoog laat staan.",
      antwoord: false,
      uitleg: "Niet waar. Tijdens een faseovergang (koken) blijft de temperatuur constant op 100 °C; alle toegevoerde warmte wordt gebruikt voor het verdampen (verdampingswarmte)."
    },
    {
      type: "invul",
      vraag: "Om 100 gram van een onbekende vloeistof 10 °C te verwarmen is 2400 Joule nodig. Wat is de soortelijke warmte van deze vloeistof in J/(kg·K)?",
      antwoord: "2400|2400 J/(kg·K)|2400 J/kgK",
      uitleg: "m = 0,10 kg. c = Q / (m × ΔT) = 2400 J / (0,10 kg × 10 K) = 2400 J/(kg·K)."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de moleculen in een vloeistof als je de vloeistof afkoelt?",
      opties: [
        "Ze gaan steeds sneller bewegen",
        "Ze worden groter van formaat",
        "Ze verdwijnen",
        "Ze gaan langzamer bewegen en komen dichter bij elkaar"
      ],
      antwoord: 3,
      uitleg: "Lagere temperatuur betekent een lagere gemiddelde bewegingssnelheid van de moleculen."
    },
    {
      type: "waaronwaar",
      vraag: "Warmte stroomt vanzelf altijd van een voorwerp met een hogere temperatuur naar een voorwerp met een lagere temperatuur totdat de temperaturen gelijk zijn.",
      antwoord: true,
      uitleg: "Waar. Dit heet thermisch evenwicht."
    },
    {
      type: "open",
      vraag: "Leg uit waarom water uitermate geschikt is als transportmiddel in een centrale verwarmingsinstallatie (cv) in woonhuizen. Betrek daarin de <b>soortelijke warmte</b> van water.",
      sleutelwoorden: ["zeer hoge soortelijke warmte", "hoge soortelijke warmte/veel warmte", "warmtetransport/langzaam afkoelen"],
      minTreffers: 2,
      modelantwoord: "Water heeft een uitzonderlijk hoge soortelijke warmte (4180 J/kg·K). Dit betekent dat een relatief kleine hoeveelheid rondgepompt water in de cv-ketel een enorme hoeveelheid warmte-energie kan opnemen en transporteren naar de radiatoren in de kamers zonder snel drastisch af te koelen. Bovendien is water goedkoop, vloeibaar en veilig.",
      uitleg: "Hoge warmtecapaciteit maakt water ideaal voor efficiënt warmtetransport."
    },
    {
      type: "open",
      vraag: "Een warm stuk koper van 200 gram met een temperatuur van 90 °C wordt in een bekerglas met 300 gram water van 20 °C gelegd. Leg uit wat er gebeurt met de warmte en de eindtemperatuur van het mengsel.",
      sleutelwoorden: ["warmte stroomt/koper naar water", "koper koelt af, water warmt op", "thermisch evenwicht/eindtemperatuur"],
      minTreffers: 2,
      modelantwoord: "Het hete koper staat warmte af aan het koudere water. Omdat energie behouden blijft (Q_afgestaan = Q_opgenomen), koelt het koper af en stijgt de temperatuur van het water totdat beide stoffen dezelfde eindtemperatuur bereiken (thermisch evenwicht). Omdat water een veel grotere soortelijke warmte en massa heeft, ligt de eindtemperatuur veel dichter bij de 20 °C van het water dan bij de 90 °C van het koper.",
      uitleg: "Warmteoverdracht tot thermisch evenwicht; water bepaalt grotendeels de eindtemperatuur door hoge c."
    }
  ]
});
