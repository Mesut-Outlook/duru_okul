/* Proeftoets 6 — Natuurkunde HAVO 3: Hoofdstuk 2 (Elektriciteit - Deel 1)
   Focus: Paragraaf 2.1 — Lading, stroomkring, spanning, stroomsterkte en meetinstrumenten.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-6",
  titel: "Toets 6 — Lading, Stroomkring, Spanning & Stroomsterkte",
  vak: "Natuurkunde · HAVO 3 (H2)",
  icoon: "🔋",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Welke deeltjes bewegen door een metalen stroomdraad wanneer er een elektrische stroom loopt?",
      opties: ["Protonen", "Elektronen", "Neutronen", "Atomen"],
      antwoord: 1,
      uitleg: "Elektrische stroom in een metaaldraad bestaat uit een stroom van vrij bewegende negatieve elektronen."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er als twee voorwerpen beide <b>positief geladen</b> zijn en dicht bij elkaar worden gehouden?",
      opties: [
        "Ze trekken elkaar aan",
        "Ze stoten elkaar af",
        "Er gebeurt niets",
        "Ze ontladen direct zonder kracht"
      ],
      antwoord: 1,
      uitleg: "Gelijksoortige ladingen (positief-positief of negatief-negatief) stoten elkaar af. Ongelijksoortige ladingen trekken elkaar aan."
    },
    {
      type: "waaronwaar",
      vraag: "Om een lampje te laten branden, is altijd een <b>gesloten stroomkring</b> én een <b>spanningsbron</b> nodig.",
      antwoord: true,
      uitleg: "Waar. Zonder gesloten kring kan er geen lading rondstromen, en zonder spanningsbron is er geen 'duwkracht' (energie) om de elektronen te laten bewegen."
    },
    {
      type: "invul",
      vraag: "Wat is de officiële eenheid van <b>elektrische spanning (U)</b>?",
      antwoord: "Volt|V|volt",
      uitleg: "Spanning wordt aangeduid met het symbool U en de eenheid Volt (V)."
    },
    {
      type: "invul",
      vraag: "Wat is de officiële eenheid van <b>stroomsterkte (I)</b>?",
      antwoord: "Ampère|Ampere|A|ampère|ampere",
      uitleg: "Stroomsterkte wordt aangeduid met het symbool I en de eenheid Ampère (A)."
    },
    {
      type: "mc",
      vraag: "Hoe sluit je een <b>spanningsmeter (voltmeter)</b> aan op een component in een schakeling?",
      opties: [
        "In serie (in de stroomkring opgenomen)",
        "Parallel (over het component heen)",
        "Altijd direct aan de pluspool van de batterij",
        "Aan één kant van het lampje en de aarde"
      ],
      antwoord: 1,
      uitleg: "Een voltmeter meet het potentiaalverschil over een onderdeel en moet daarom altijd PARALLEL geschakeld worden."
    },
    {
      type: "mc",
      vraag: "Hoe sluit je een <b>stroommeter (ampèremeter)</b> aan om de stroom door een lampje te meten?",
      opties: [
        "In serie (in dezelfde stroomtak)",
        "Parallel over het lampje",
        "Direct tussen de plus- en minpool van de bron zonder lampje",
        "Draadloos naast de schakeling"
      ],
      antwoord: 0,
      uitleg: "Een stroommeter meet hoeveel lading er per seconde passeert en moet daarom IN SERIE in de stroomkring opgenomen worden."
    },
    {
      type: "invul",
      vraag: "Reken om: een stroommeter geeft <b>350 mA</b> aan. Hoeveel Ampère (A) is dat?",
      antwoord: "0,35|0,35 A|0,35A",
      uitleg: "1 A = 1000 mA. Dus 350 / 1000 = 0,35 A."
    },
    {
      type: "invul",
      vraag: "Reken om: een stroomsterkte is <b>2,4 A</b>. Hoeveel milliampère (mA) is dat?",
      antwoord: "2400|2400 mA|2.400|2400mA",
      uitleg: "2,4 × 1000 = 2400 mA."
    },
    {
      type: "waaronwaar",
      vraag: "De netspanning uit een standaard stopcontact in Nederland bedraagt <b>230 Volt</b>.",
      antwoord: true,
      uitleg: "Waar. De standaard netspanning voor huishoudens in Nederland en Europa is 230 V wisselspanning."
    },
    {
      type: "mc",
      vraag: "Wat is het verschil tussen een <b>geleider</b> en een <b>isolator</b>?",
      opties: [
        "Een geleider laat elektrische stroom goed door (bevat vrije elektronen); een isolator laat stroom nauwelijks door",
        "Een geleider is altijd van plastic; een isolator altijd van koper",
        "Een isolator kan alleen wisselstroom geleiden",
        "Er is geen verschil in stroomdoorlatendheid"
      ],
      antwoord: 0,
      uitleg: "Metalen zoals koper, aluminium en ijzer zijn goede geleiders. Stoffen als rubber, plastic, glas en lucht zijn isolatoren."
    },
    {
      type: "waaronwaar",
      vraag: "Als je een ballon over een wollen trui wrijft, springen er protonen over waardoor de ballon statisch geladen wordt.",
      antwoord: false,
      uitleg: "Niet waar. Alleen elektronen kunnen bewegen en overspringen tussen atomen. Protonen zitten vast in de atoomkern."
    },
    {
      type: "mc",
      vraag: "Een stroomsterkte van 1 Ampère betekent dat er:",
      opties: [
        "1 Joule energie per seconde geleverd wordt",
        "1 Coulomb aan lading per seconde door de draad stroomt",
        "1 Volt spanning over de draad staat",
        "1 Ohm weerstand in de draad aanwezig is"
      ],
      antwoord: 1,
      uitleg: "Stroomsterkte I is de hoeveelheid lading per seconde: 1 A = 1 C/s (Coulomb per seconde)."
    },
    {
      type: "invul",
      vraag: "Hoe noem je een onderdeel in een stroomkring waarmee je de stroomkring kunt openen en sluiten?",
      antwoord: "schakelaar|een schakelaar",
      uitleg: "Met een schakelaar onderbreek of sluit je de stroomkring."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende stoffen is een <b>goede elektrische geleider</b>?",
      opties: [
        "Glas",
        "Koper",
        "Hout",
        "Porselein"
      ],
      antwoord: 1,
      uitleg: "Koper is een uitstekende geleider en wordt daarom gebruikt in installatiedraad en stroomkabels."
    },
    {
      type: "waaronwaar",
      vraag: "Een ideale stroommeter heeft een zo laag mogelijke weerstand (bijna 0 Ω), zodat hij de stroom in de kring niet afremt.",
      antwoord: true,
      uitleg: "Waar. Een ampèremeter heeft vrijwel geen weerstand om de stroomkring niet te beïnvloeden."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er als je een ampèremeter per ongeluk <b>parallel</b> over een sterke batterij aansluit?",
      opties: [
        "Hij meet keurig de spanning",
        "Er ontstaat kortsluiting met een zeer grote stroom, waardoor de meter of zekering kan doorbranden",
        "Er gaat helemaal geen stroom lopen",
        "De batterij laadt razendsnel op"
      ],
      antwoord: 1,
      uitleg: "Omdat de ampèremeter bijna 0 Ω weerstand heeft, ontstaat er kortsluiting met een gevaarlijk hoge stroomsterkte."
    },
    {
      type: "invul",
      vraag: "Hoeveel Volt levert een standaard AA- of AAA-alkalinebatterij?",
      antwoord: "1,5|1,5 V|1.5|1,5 volt",
      uitleg: "Een standaard cilindrische alkalinebatterij (AA / AAA / C / D) heeft een klemspanning van 1,5 V."
    },
    {
      type: "open",
      vraag: "Leg uit hoe statische elektriciteit ontstaat wanneer je op sokken over een nylon tapijt loopt en daarna een metalen deurklink aanraakt.",
      sleutelwoorden: ["wrijving", "elektronen overgaan/overspringen/lading opbouwen", "ontlading/schokje naar metaal"],
      minTreffers: 2,
      modelantwoord: "Door wrijving tussen je sokken en het tapijt springen er elektronen over, waardoor je lichaam een statische elektrische lading opbouwt. Wanneer je vervolgens de metalen geleidende deurklink nadert, springen de overtollige elektronen in één keer over (een vonkje/schok), waardoor je lichaam weer neutraal ontlaadt.",
      uitleg: "Kern: lading door wrijving (elektronenoverdracht) en plotselinge ontlading via een geleider."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de koperen kern van een netsnoer altijd omhuld is met een laag flexibel PVC-plastic.",
      sleutelwoorden: ["koper is geleider", "plastic is isolator", "veiligheid/kortsluiting voorkomen/aanraking/schok voorkomen"],
      minTreffers: 2,
      modelantwoord: "Koper is een uitstekende geleider die de elektrische stroom naar het apparaat transporteert. Het plastic eromheen is een isolator die de stroom tegenhoudt. Dit voorkomt dat je bij aanraking een gevaarlijke elektrische schok krijgt en voorkomt kortsluiting met andere draden.",
      uitleg: "Koper = geleider voor stroomtransport; plastic = isolator voor bescherming en veiligheid."
    }
  ]
});
