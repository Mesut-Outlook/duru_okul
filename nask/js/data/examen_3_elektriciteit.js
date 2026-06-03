DURU.registerExamen({
  id: "toets-h6-elektriciteit",
  titel: "Oefentoets H6 — Elektriciteit",
  vak: "Elektriciteit · Hoofdstuk 6",
  icoon: "⚡",
  duurMin: 20,
  vragen: [

    /* ── MC ── */

    { type: "mc",
      vraag: "Wat is het symbool voor spanning en wat is de eenheid?",
      opties: ["U, volt (V)", "I, ampère (A)", "P, watt (W)", "R, ohm (Ω)"],
      antwoord: 0,
      uitleg: "Spanning heeft symbool <b>U</b> en eenheid <b>volt (V)</b>." },

    { type: "mc",
      vraag: "Welke spanning levert een normaal stopcontact (lichtnet) in Nederland?",
      opties: ["230 V", "12 V", "1,5 V", "9 V"],
      antwoord: 0,
      uitleg: "Het lichtnet (stopcontact) levert <b>230 volt</b>. Een AA-batterij levert slechts 1,5 V." },

    { type: "mc",
      vraag: "Wat meet een voltmeter?",
      opties: ["Spanning (in volt)", "Stroomsterkte (in ampère)", "Weerstand (in ohm)", "Vermogen (in watt)"],
      antwoord: 0,
      uitleg: "Een <b>voltmeter</b> meet de <b>spanning</b> in volt. De ampèremeter meet de stroom." },

    { type: "mc",
      vraag: "Hoe sluit je een voltmeter aan op een lamp waarvan je de spanning wilt meten?",
      opties: ["Parallel (naast de lamp)", "In serie (achter de lamp)", "Tussen schakelaar en lamp", "Maakt niet uit"],
      antwoord: 0,
      uitleg: "Een voltmeter sluit je altijd <b>parallel</b> aan — hij staat <b>over</b> het onderdeel dat je meet." },

    { type: "mc",
      vraag: "Wat is de eenheid van stroomsterkte en wat is het symbool?",
      opties: ["Ampère (A), symbool I", "Volt (V), symbool U", "Watt (W), symbool P", "Ohm (Ω), symbool R"],
      antwoord: 0,
      uitleg: "Stroomsterkte: symbool <b>I</b>, eenheid <b>ampère (A)</b>." },

    { type: "mc",
      vraag: "Hoeveel milliampère is gelijk aan 1 ampère?",
      opties: ["1 000 mA", "100 mA", "10 mA", "10 000 mA"],
      antwoord: 0,
      uitleg: "1 A = <b>1 000 mA</b>. Je vermenigvuldigt met 1 000 om van A naar mA te gaan." },

    { type: "mc",
      vraag: "Hoe sluit je een ampèremeter aan om de stroom door een lamp te meten?",
      opties: ["In serie (achter elkaar in de kring)", "Parallel (naast de lamp)", "Op de pluspool van de batterij", "Maakt niet uit"],
      antwoord: 0,
      uitleg: "Een ampèremeter sluit je <b>in serie</b> aan — alle stroom moet er doorheen lopen." },

    { type: "mc",
      vraag: "Wat zijn DRIE voorbeelden van een isolator?",
      opties: ["Plastic, rubber en hout", "Koper, ijzer en aluminium", "Koper, plastic en rubber", "Goud, zilver en koper"],
      antwoord: 0,
      uitleg: "<b>Isolatoren</b> geleiden geen stroom: plastic, rubber, hout, glas en lucht zijn voorbeelden. Metalen zijn juist geleiders." },

    { type: "mc",
      vraag: "Twee lampen staan in serie. Lamp 1 brandt door. Wat gebeurt er als lamp 2 stuk gaat (draad breekt)?",
      opties: ["Lamp 1 gaat ook uit", "Lamp 1 brandt gewoon door", "Lamp 1 gaat feller branden", "Er verandert niets"],
      antwoord: 0,
      uitleg: "Bij een <b>serieschakeling</b> is er maar één kring. Eén kapotte lamp verbreekt de kring → <b>alle lampen uit</b>." },

    { type: "mc",
      vraag: "Lampen in huis (plafondlamp, keukenlamp, leeslamp) zijn geschakeld in …",
      opties: ["Parallel", "Serie", "Afwisselend serie en parallel", "Dat verschilt per huis"],
      antwoord: 0,
      uitleg: "Huishoudelijke lampen staan <b>parallel</b>: ze krijgen elk de volle spanning en kunnen apart aan/uit." },

    { type: "mc",
      vraag: "Bekijk het figuur. Wat stelt dit symbool voor?",
      figuur: `<svg viewBox="0 0 80 80" width="80" height="80" xmlns="http://www.w3.org/2000/svg">
  <circle cx="40" cy="40" r="28" stroke="#333" stroke-width="3" fill="none"/>
  <text x="40" y="46" font-size="22" font-family="Arial" font-weight="bold" text-anchor="middle" fill="#333">V</text>
</svg>`,
      opties: ["Een voltmeter", "Een ampèremeter", "Een lamp", "Een schakelaar"],
      antwoord: 0,
      uitleg: "Een <b>V in een cirkel</b> is het schakelsymbool van de <b>voltmeter</b>." },

    /* ── WAAR/ONWAAR ── */

    { type: "waaronwaar",
      vraag: "Stroom bestaat uit bewegende elektronen.",
      antwoord: true,
      uitleg: "Waar. <b>Elektrische stroom</b> = een stroom van bewegende <b>elektronen</b> door een geleider." },

    { type: "waaronwaar",
      vraag: "In een open stroomkring (schakelaar open) loopt er stroom.",
      antwoord: false,
      uitleg: "Onwaar. Stroom loopt alleen in een <b>gesloten kring</b>. Open kring → geen stroom → lamp uit." },

    { type: "waaronwaar",
      vraag: "Een auto-accu levert een spanning van 12 volt.",
      antwoord: true,
      uitleg: "Waar. Een <b>auto-accu</b> levert standaard <b>12 V</b>." },

    { type: "waaronwaar",
      vraag: "Bij een parallelschakeling krijgt elk onderdeel dezelfde (volle) spanning.",
      antwoord: true,
      uitleg: "Waar. Bij <b>parallel</b> staat elk onderdeel direct op de spanning van de bron → ieder krijgt de <b>volle spanning</b>." },

    { type: "waaronwaar",
      vraag: "Bij een serieschakeling is de stroom in elk onderdeel anders groot.",
      antwoord: false,
      uitleg: "Onwaar. Bij serie is er maar één pad → de stroom is <b>overal even groot</b>." },

    { type: "waaronwaar",
      vraag: "Koper is een geleider.",
      antwoord: true,
      uitleg: "Waar. <b>Koper (metaal)</b> geleidt stroom goed. Daarom worden elektriciteitskabels van koper gemaakt." },

    { type: "waaronwaar",
      vraag: "Oude kerstverlichting was in serie geschakeld. Als één lampje doorbrandt, gaan alle andere ook uit.",
      antwoord: true,
      uitleg: "Waar. Bij <b>serie</b> zijn alle lampjes in één kring. Eén kapot lampje verbreekt de kring → alles uit." },

    /* ── OPEN ── */

    { type: "open",
      vraag: "Leg uit wat het verschil is tussen een serieschakeling en een parallelschakeling. Geef van elk één voorbeeld uit het dagelijks leven.",
      sleutelwoorden: ["serie/achter elkaar/één kring", "parallel/naast elkaar/eigen tak", "kerstverlichting/kerst", "lampen thuis/thuis/huis"],
      minTreffers: 2,
      modelantwoord: "Bij serie staan onderdelen achter elkaar in één kring (bijv. oude kerstverlichting). Bij parallel staan ze naast elkaar, elk in een eigen tak (bijv. lampen thuis).",
      uitleg: "<b>Serie:</b> achter elkaar, één kring, één stuk → alles uit.<br><b>Parallel:</b> naast elkaar, eigen tak, één stuk → rest brandt door." },

    { type: "open",
      vraag: "Waarom sluit je een voltmeter parallel aan en een ampèremeter in serie?",
      sleutelwoorden: ["spanning/voltage/volt", "stroom/stroomsterkte", "parallel/over", "serie/door"],
      minTreffers: 2,
      modelantwoord: "Een voltmeter meet het spanningsverschil over een onderdeel, dus moet hij ernaast (parallel). Een ampèremeter meet hoeveel stroom er doorheen loopt, dus de stroom moet er echt doorheen — dat kan alleen in serie.",
      uitleg: "Voltmeter: meet <b>spanning over</b> het onderdeel → <b>parallel</b>.<br>Ampèremeter: meet <b>stroom door</b> het onderdeel → <b>in serie</b>." },

    { type: "open",
      vraag: "Noem drie spanningsbronnen en geef bij elk de spanning (in volt).",
      sleutelwoorden: ["batterij/aa/1,5/1.5", "auto-accu/accu/12", "stopcontact/lichtnet/230", "dynamo", "zonnecel"],
      minTreffers: 2,
      modelantwoord: "Batterij (1,5 V), auto-accu (12 V), stopcontact/lichtnet (230 V). Ook dynamo en zonnecel zijn spanningsbronnen.",
      uitleg: "Voorbeelden: <b>batterij 1,5 V</b>, <b>auto-accu 12 V</b>, <b>lichtnet 230 V</b>, dynamo, zonnecel." },

    { type: "open",
      vraag: "Reken om: een apparaatje gebruikt 0,75 A. Hoeveel milliampère is dat?",
      sleutelwoorden: ["750/750 ma/750ma"],
      minTreffers: 1,
      modelantwoord: "0,75 A × 1 000 = 750 mA.",
      uitleg: "Van A naar mA: vermenigvuldig met 1 000. 0,75 × 1 000 = <b>750 mA</b>." },

    { type: "open",
      vraag: "Reken om: een ledlampje heeft een stroom van 500 mA. Hoeveel ampère is dat?",
      sleutelwoorden: ["0,5/0.5/half"],
      minTreffers: 1,
      modelantwoord: "500 mA ÷ 1 000 = 0,5 A.",
      uitleg: "Van mA naar A: deel door 1 000. 500 ÷ 1 000 = <b>0,5 A</b>." },

    { type: "open",
      vraag: "Bekijk het figuur. Wat stelt dit symbool voor en in welke schakeling sluit je dit aan?",
      figuur: `<svg viewBox="0 0 80 80" width="80" height="80" xmlns="http://www.w3.org/2000/svg">
  <circle cx="40" cy="40" r="28" stroke="#333" stroke-width="3" fill="none"/>
  <text x="40" y="46" font-size="22" font-family="Arial" font-weight="bold" text-anchor="middle" fill="#333">A</text>
</svg>`,
      sleutelwoorden: ["ampèremeter/ampere/amperemeter", "serie/in serie/achter elkaar"],
      minTreffers: 2,
      modelantwoord: "Dit is de ampèremeter (A in cirkel). Je sluit hem in serie aan, zodat de stroom er helemaal doorheen loopt.",
      uitleg: "Een <b>A in een cirkel</b> = <b>ampèremeter</b>. Die sluit je <b>in serie</b> aan." },

    { type: "open",
      vraag: "Leg uit wat een gesloten stroomkring is en waarom een lamp anders niet brandt.",
      sleutelwoorden: ["gesloten/complete/heel", "kring/circuit", "stroom/loopt"],
      minTreffers: 2,
      modelantwoord: "In een gesloten stroomkring is er een ononderbroken pad van de plus- naar de minpool. Alleen dan kunnen elektronen stromen en kan de lamp branden.",
      uitleg: "Stroom loopt alleen als het pad <b>gesloten (ononderbroken)</b> is. Open kring = geen stroom = lamp uit." },

    { type: "open",
      vraag: "Geef twee redenen waarom de lampen in een huis parallel zijn geschakeld en niet in serie.",
      sleutelwoorden: ["volle spanning/eigen spanning/230", "apart/zelfstandig/onafhankelijk", "stuk/kapot/anderen"],
      minTreffers: 2,
      modelantwoord: "1) Elke lamp krijgt de volle spanning (230 V) en brandt dus even helder. 2) Als één lamp kapot gaat, branden de andere gewoon door.",
      uitleg: "Parallel: <b>volle spanning</b> voor elke lamp én <b>onafhankelijk</b> van elkaar (één kapot → rest blijft aan)." },

    /* ── INVUL ── */

    { type: "invul",
      vraag: "Vul aan: De spanning in een kring geef je aan met de letter ______ en meet je in ______.",
      antwoord: "u en volt|u, volt|u en v|u / volt|u;volt",
      uitleg: "Spanning: symbool <b>U</b>, eenheid <b>volt (V)</b>." },

    { type: "invul",
      vraag: "Vul aan: 2 ampère is gelijk aan ______ milliampère.",
      antwoord: "2000|2 000",
      uitleg: "2 A × 1 000 = <b>2 000 mA</b>." },

    { type: "invul",
      vraag: "Vul aan: Een voltmeter sluit je ______ aan; een ampèremeter sluit je ______ aan.",
      antwoord: "parallel en in serie|parallel; in serie|parallel, in serie|parallel / in serie",
      uitleg: "Voltmeter → <b>parallel</b>. Ampèremeter → <b>in serie</b>." }

  ]
});
