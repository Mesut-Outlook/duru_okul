/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 20 — Sensoren & Integrale Eindtoets Hoofdstuk 4
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-20",
  "hoofdstuk": 4,
  "titel": "Toets 20 — Sensoren & Integrale Eindtoets Hoofdstuk 4",
  "vak": "Natuurkunde · HAVO 3 (H4)",
  "icoon": "🏆",
  "duurMin": 35,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is een <b>sensor</b> in een elektronische schakeling?",
      "opties": [
        "Een onderdeel dat een natuurkundige grootheid (zoals temperatuur, licht of druk) omzet in een elektrisch signaal (spanning of weerstandsverandering)",
        "Een soort batterij die stroom produceert uit zonlicht",
        "Een schakelaar die altijd open blijft staan",
        "Een luidspreker die geluid maakt"
      ],
      "antwoord": 0,
      "uitleg": "Een sensor meet een fysische grootheid en vertaalt dit naar een elektrische verandering."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de weerstand van een <b>NTC-weerstand</b> als de temperatuur stijgt?",
      "opties": [
        "De weerstand stijgt",
        "De weerstand daalt sterk (Negatieve Temperatuur Coëfficiënt)",
        "De weerstand blijft altijd 1000 Ω",
        "De weerstand wordt oneindig"
      ],
      "antwoord": 1,
      "uitleg": "NTC = Negative Temperature Coefficient: hogere temperatuur -> lagere weerstand."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de weerstand van een <b>PTC-weerstand</b> als de temperatuur stijgt?",
      "opties": [
        "De stroom valt weg",
        "De weerstand daalt",
        "De weerstand stijgt (Positieve Temperatuur Coëfficiënt)",
        "De spanning wordt negatief"
      ],
      "antwoord": 2,
      "uitleg": "PTC = Positive Temperature Coefficient: hogere temperatuur -> hogere weerstand."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de weerstand van een <b>LDR</b> (Light Dependent Resistor) als er fel licht op schijnt?",
      "opties": [
        "De weerstand wordt heel hoog",
        "De LDR smelt direct",
        "De weerstand verandert niet",
        "De weerstand wordt heel laag (er kan veel stroom lopen)"
      ],
      "antwoord": 3,
      "uitleg": "Veel licht -> lage weerstand; donker -> zeer hoge weerstand."
    },
    {
      "type": "invul",
      "vraag": "Een massief blokje goud (ρ = 19,3 g/cm³) heeft een massa van 38,6 gram. Bereken het volume in cm³.",
      "antwoord": "2|2 cm³|2,0|2,0 cm³",
      "uitleg": "V = m / ρ = 38,6 g / 19,3 g/cm³ = 2,0 cm³."
    },
    {
      "type": "invul",
      "vraag": "Hoeveel Joule warmte is er nodig om 0,50 kg water (c = 4180 J/(kg·K)) te verwarmen van 20 °C naar 100 °C (ΔT = 80 K)?",
      "antwoord": "167200|167.200|167,2 kJ|167200 J|167.200 J",
      "uitleg": "Q = m × c × ΔT = 0,50 kg × 4180 J/(kg·K) × 80 K = 167.200 J (167,2 kJ)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een NTC-sensor wordt vaak gebruikt in digitale thermometers en thermostaten om de temperatuur nauwkeurig te meten.",
      "antwoord": true,
      "uitleg": "Waar. De veranderende weerstand van de NTC wordt door een microcontroller omgerekend naar graden Celsius."
    },
    {
      "type": "mc",
      "vraag": "Een NTC staat in serie met een vaste weerstand van 100 Ω op een 5 V voeding. Als de temperatuur stijgt, daalt de weerstand van de NTC. Wat gebeurt er met de stroomsterkte in de kring?",
      "opties": [
        "De stroomsterkte stijgt (I = U / R_tot, en R_tot is kleiner geworden)",
        "De stroomsterkte daalt",
        "De stroomsterkte blijft gelijk",
        "De stroomsterkte wordt 0 A"
      ],
      "antwoord": 0,
      "uitleg": "Omdat R_tot = R_ntc + 100 daalt, stijgt de stroomsterkte I = U / R_tot."
    },
    {
      "type": "waaronwaar",
      "vraag": "De soortelijke warmte van aluminium (880 J/kg·K) is bijna 5 keer zo klein als die van water (4180 J/kg·K).",
      "antwoord": false,
      "uitleg": "Onwaar: Waar: 4180 / 880 ≈ 4,75, dus water heeft bijna vijf keer zoveel warmte nodig om dezelfde massa met 1 K op te warmen. Daarom warmt aluminium veel sneller op (en koelt het ook sneller af) dan water bij dezelfde toegevoerde warmte."
    },
    {
      "type": "invul",
      "vraag": "Een koperdraad van 100 m lengte met doorsnede A = 1,7 mm² heeft een soortelijke weerstand ρ = 0,017 Ω·mm²/m. Bereken de weerstand in Ohm.",
      "antwoord": "1|1 Ω|1 ohm|1,0",
      "uitleg": "R = (ρ × l) / A = (0,017 × 100) / 1,7 = 1,7 / 1,7 = 1,0 Ω."
    },
    {
      "type": "mc",
      "vraag": "Welk materiaal is het meest geschikt als isolator in een spouwmuur?",
      "opties": [
        "Koperwol",
        "Glaswol of EPS-piepschuimkorrels",
        "IJzervijlsel",
        "Aluminiumpoeder"
      ],
      "antwoord": 1,
      "uitleg": "Glaswol en EPS-korrels sluiten stilstaande lucht in en hebben een extreem lage warmtegeleidingscoëfficiënt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je twee voorwerpen van verschillende materialen met dezelfde massa en hetzelfde beginvolume evenveel warmte Q geeft, eindigen ze altijd op dezelfde temperatuur.",
      "antwoord": false,
      "uitleg": "Niet waar. De temperatuurstijging ΔT = Q / (m · c) hangt af van de soortelijke warmte c van het materiaal."
    },
    {
      "type": "invul",
      "vraag": "Een dompelaar van 1000 W verwarmt water gedurende 3 minuten (180 s). Hoeveel kJ elektrische warmte levert de dompelaar?",
      "antwoord": "180|180 kJ|180000|180.000",
      "uitleg": "Q = P × t = 1000 W × 180 s = 180.000 J = 180 kJ."
    },
    {
      "type": "mc",
      "vraag": "In een schemerschakelaar voor straatverlichting zit een LDR. Hoe zorgt de schakeling ervoor dat de lamp automatisch aangaat als het donker wordt?",
      "opties": [
        "De LDR smelt in het donker",
        "In het donker gaat de LDR licht geven",
        "In het donker stijgt de weerstand van de LDR; een elektronische schakeling detecteert de veranderde spanning en schakelt het relais van de straatlantaarn in",
        "De LDR wekt zelf 230 V op"
      ],
      "antwoord": 2,
      "uitleg": "In het donker wordt R_ldr heel groot -> spanning over de LDR stijgt -> transistor/relais schakelt de lantaarn in."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een vacuüm kan warmtetransport uitsluitend plaatsvinden via warmtestraling (infrarood).",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Geleiding en stroming hebben materie (atomen/moleculen) nodig."
    },
    {
      "type": "invul",
      "vraag": "Een ijsblokje heeft een volume van 50 cm³ en een dichtheid van 0,92 g/cm³. Wat is de massa van het ijsblokje in gram?",
      "antwoord": "46|46 g|46,0",
      "uitleg": "m = ρ × V = 0,92 g/cm³ × 50 cm³ = 46 gram."
    },
    {
      "type": "mc",
      "vraag": "Waarom worden koelribben op de achterkant van een koelkast of op een computerprocessor zwart gemaakt?",
      "opties": [
        "Om ze tegen roest te beschermen",
        "Zodat ze minder stof aantrekken",
        "Omdat zwarte verf elektriciteit geleidt",
        "Omdat een zwart, mat oppervlak warmtestraling (infrarood) maximaal uitstraalt naar de omgeving"
      ],
      "antwoord": 3,
      "uitleg": "Zwarte, doffe oppervlakken zijn de beste stralers van warmte (geven warmte snel af)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De eenheid van soortelijke warmte is J/(kg·K) of J/(kg·°C).",
      "antwoord": true,
      "uitleg": "Waar. Beide notaties worden in de natuurkunde gebruikt."
    },
    {
      "type": "open",
      "vraag": "Leg uit hoe een <b>automatische brandmelder</b> met een <b>NTC-weerstand</b> werkt wanneer er brand uitbreekt in een kamer.",
      "sleutelwoorden": [
        "temperatuur stijgt door vuur/brand",
        "weerstand van NTC daalt",
        "weerstand daalt/stroom stijgt",
        "schakeling activeert sirene/alarm"
      ],
      "minTreffers": 3,
      "modelantwoord": "Wanneer er brand uitbreekt, stijgt de kamertemperatuur snel. Door de hitte daalt de weerstand van de NTC-sensor sterk. Hierdoor neemt de stroomsterkte in de sensorserieketen toe (of verandert de deelspanning over de sensor). Een elektronische schakeling detecteert dat de grenswaarde wordt overschreden en stuurt direct een stroom naar de alarmsirene.",
      "uitleg": "Hitte -> weerstand NTC daalt -> stroom stijgt / spanning kantelt -> sirene gaat af."
    },
    {
      "type": "open",
      "vraag": "Vergelijk een koperen kookpan met een dikke aluminium kookpan op het gebied van <b>warmtegeleiding</b>, <b>massa</b> en <b>warmtecapaciteit</b>.",
      "sleutelwoorden": [
        "koper betere geleider/sneller warm",
        "aluminium lichter/goedkoper",
        "soortelijke warmte"
      ],
      "minTreffers": 2,
      "modelantwoord": "1. Warmtegeleiding: Koper heeft een hogere warmtegeleidingscoëfficiënt dan aluminium en verdeelt de warmte vanaf de vlam nog sneller en gelijkmatiger over de panbodem. 2. Massa: Aluminium heeft een veel lagere dichtheid (2,7 g/cm³ vs. 8,9 g/cm³), waardoor een aluminium pan veel lichter en handzamer is. 3. Warmtecapaciteit: Aluminium heeft een hogere soortelijke warmte (880 J/kg·K vs. 390 J/kg·K), waardoor het relatief veel warmte vasthoudt.",
      "uitleg": "Vergelijking op geleiding (λ), dichtheid (massa) en soortelijke warmte (c)."
    }
  ]
});
