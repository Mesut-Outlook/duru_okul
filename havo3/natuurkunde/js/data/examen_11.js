/* Proeftoets 11 — Natuurkunde HAVO 3: Hoofdstuk 3 (Straling - Deel 1)
   Focus: Paragraaf 3.1 — Elektromagnetisch spectrum, golflengte, frequentie, IR, UV en röntgenstraling.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-11",
  titel: "Toets 11 — Het Elektromagnetisch Spectrum & Soorten Straling",
  vak: "Natuurkunde · HAVO 3 (H3)",
  icoon: "🌈",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Welke soort elektromagnetische straling heeft de <b>grootste golflengte</b> en de <b>laagste energie per foton</b>?",
      opties: [
        "Radiogolven",
        "Röntgenstraling",
        "Zichtbaar licht",
        "Gammastraling"
      ],
      antwoord: 0,
      uitleg: "Radiogolven hebben de langste golflengte (tot kilometers) en de laagste frequentie/energie in het spectrum."
    },
    {
      type: "mc",
      vraag: "Welke soort elektromagnetische straling heeft de <b>kortste golflengte</b> en de <b>hoogste energie</b>?",
      opties: [
        "Infraroodstraling",
        "Gammastraling",
        "Ultraviolette straling (UV)",
        "Microgolven"
      ],
      antwoord: 1,
      uitleg: "Gammastraling heeft de kortste golflengte en de allerhoogste energie en doordringend vermogen."
    },
    {
      type: "waaronwaar",
      vraag: "Alle elektromagnetische golven planten zich in een vacuüm voort met de <b>lichtsnelheid</b> ($c \approx 300.000\text{ km/s}$).",
      antwoord: true,
      uitleg: "Waar. Alle EM-straling (van radio tot gamma) reist in een vacuüm met circa 300.000 km/s (3 × 10⁸ m/s)."
    },
    {
      type: "mc",
      vraag: "Welke stralingssoort zendt het menselijk lichaam voornamelijk uit door lichaamswarmte?",
      opties: [
        "Ultraviolette straling (UV)",
        "Röntgenstraling",
        "Infraroodstraling (IR / warmtestraling)",
        "Microgolven"
      ],
      antwoord: 2,
      uitleg: "Warme voorwerpen (zoals mensen van ca. 37 °C) zenden onzichtbare infraroodstraling (IR) uit."
    },
    {
      type: "invul",
      vraag: "Welk meetapparaat gebruikt een arts of beveiliger om op afstand zonder contact koorts te meten via warmtestraling?",
      antwoord: "infraroodthermometer|infrarood thermometer|IR-thermometer|IR thermometer|warmtecamera|infraroodcamera",
      uitleg: "Een infraroodthermometer meet de intensiteit van de uitgezonden IR-warmtestraling van het voorhoofd of oor."
    },
    {
      type: "mc",
      vraag: "Welke kleuren vormen van lage naar hoge frequentie het <b>zichtbare licht</b> spectrum?",
      opties: [
        "Violet, blauw, groen, geel, oranje, rood",
        "Infrarood, geel, ultraviolet",
        "Wit, grijs, zwart",
        "Rood, oranje, geel, groen, blauw, violet (ROGGBIV)"
      ],
      antwoord: 3,
      uitleg: "Rood heeft de langste golflengte / laagste frequentie van zichtbaar licht; violet heeft de kortste golflengte / hoogste frequentie."
    },
    {
      type: "waaronwaar",
      vraag: "Ultraviolette straling (UV) van de zon zorgt voor de aanmaak van vitamine D in de huid, maar kan bij overmatige blootstelling zonnebrand en huidkanker veroorzaken.",
      antwoord: true,
      uitleg: "Waar. UV stimuleert vitamine D-aanmaak, maar te veel UV beschadigt DNA in huidcellen."
    },
    {
      type: "mc",
      vraag: "Waarom worden botten op een <b>röntgenfoto</b> wit/licht afgebeeld, terwijl spieren en vet donkerder zijn?",
      opties: [
        "Omdat botten (door calcium) meer röntgenstraling absorberen/tegenhouden dan weke weefsels",
        "Omdat botten zelf röntgenstraling uitzenden",
        "Omdat botten warmer zijn dan spieren",
        "Omdat spieren de straling weerkaatsen"
      ],
      antwoord: 0,
      uitleg: "Botten bevatten veel zware atomen (calcium) en absorberen röntgenstralen, waardoor er minder straling op de film achter het bot valt (witte schaduw)."
    },
    {
      type: "invul",
      vraag: "Welke gassenlaag hoog in de aardatmosfeer beschermt het leven op aarde door het grootste deel van de schadelijke UV-C en UV-B straling te absorberen?",
      antwoord: "ozonlaag|de ozonlaag|ozon",
      uitleg: "De ozonlaag in de stratosfeer filtert het grootste deel van de gevaarlijke ultraviolette straling van de zon."
    },
    {
      type: "mc",
      vraag: "Wat voor straling gebruikt een <b>magnetron</b> om voedsel te verwarmen?",
      opties: [
        "Röntgenstraling",
        "Microgolven",
        "Alfastraling",
        "Gammastraling"
      ],
      antwoord: 1,
      uitleg: "Een magnetron zendt microgolven uit die watermoleculen in het eten snel laten trillen, wat wrijvingswarmte opwekt."
    },
    {
      type: "waaronwaar",
      vraag: "Zowel radiogolven als röntgenstraling zijn vormen van elektromagnetische straling.",
      antwoord: true,
      uitleg: "Waar. Beide zijn EM-golven; ze verschillen alleen in golflengte, frequentie en energie per foton."
    },
    {
      type: "mc",
      vraag: "Welke stralingssoorten in het spectrum zijn <b>ioniserend</b> (kunnen elektronen uit atomen slaan en DNA beschadigen)?",
      opties: [
        "Alleen radiogolven en infrarood",
        "Alleen zichtbaar groen licht",
        "Extreem UV, röntgenstraling en gammastraling",
        "Microgolven en infrarood"
      ],
      antwoord: 2,
      uitleg: "Alleen straling met zeer hoge energie en korte golflengte (hoog-energetisch UV, röntgen en gamma) is ioniserend."
    },
    {
      type: "invul",
      vraag: "Reken om: de golflengte van een groen lichtdeeltje is 500 nm (nanometer). Hoeveel meter is dat (in wetenschappelijke notatie of als decimaal getal: 1 nm = 10⁻⁹ m)?",
      antwoord: "0,0000005|0,0000005 m|5e-7|5*10^-7|5 x 10^-7",
      uitleg: "500 nm = 500 × 10⁻⁹ m = 0,0000005 m = 5 × 10⁻⁷ m."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de kleur van een gloeiend stuk ijzer als de temperatuur steeds verder <b>stijgt</b>?",
      opties: [
        "Gaat van witgloeiend naar dofrood",
        "Wordt direct zwart",
        "Blijft altijd dezelfde kleur rood",
        "Gaat van donkerrood naar oranje, geel en uiteindelijk fel witblauw"
      ],
      antwoord: 3,
      uitleg: "Bij hogere temperatuur zendt het voorwerp straling uit met kortere golflengte en hogere frequentie: van donkerrood naar fel witblauw."
    },
    {
      type: "waaronwaar",
      vraag: "Röntgenstraling kan dwars door een loden schort van 1 cm dik heen gaan alsof het glas is.",
      antwoord: false,
      uitleg: "Niet waar. Lood heeft een zeer hoge dichtheid en atoomnummer en absorbeert röntgenstraling uitstekend. Daarom draagt de tandarts/radioloog een loden schort."
    },
    {
      type: "mc",
      vraag: "Wat betekent de 'Zonkracht' (UV-index) in het weerbericht?",
      opties: [
        "Een maat voor de hoeveelheid schadelijke UV-straling die het aardoppervlak bereikt",
        "De temperatuur van de zon in graden Celsius",
        "De windsnelheid op grote hoogte",
        "De helderheid van de blauwe lucht"
      ],
      antwoord: 0,
      uitleg: "De UV-index geeft aan hoe sterk de ultraviolette straling is en hoe snel de onbeschermde huid kan verbranden."
    },
    {
      type: "invul",
      vraag: "Welke stralingssoort wordt gebruikt in de afstandsbediening van je televisie?",
      antwoord: "infrarood|infraroodstraling|IR|IR-straling",
      uitleg: "Een afstandsbediening zendt gecodeerde infrarood-lichtpulsen uit naar de tv-ontvanger."
    },
    {
      type: "waaronwaar",
      vraag: "Zichtbaar licht heeft meer energie per foton dan infraroodstraling.",
      antwoord: true,
      uitleg: "Waar. Zichtbaar licht heeft een kortere golflengte en hogere frequentie dan infrarood, dus meer energie."
    },
    {
      type: "open",
      vraag: "Plaats de volgende vier soorten elektromagnetische straling in volgorde van <b>laagste naar hoogste energie</b> (langste naar kortste golflengte): <i>Röntgenstraling, Infrarood, Radiogolven, Zichtbaar licht</i>. Licht je keuze kort toe.",
      sleutelwoorden: ["radiogolven", "infrarood", "zichtbaar licht", "röntgenstraling"],
      minTreffers: 4,
      modelantwoord: "Volgorde (van laagste naar hoogste energie / langste naar kortste golflengte):\n1. Radiogolven (laagste frequentie, langste golflengte)\n2. Infrarood\n3. Zichtbaar licht\n4. Röntgenstraling (hoogste frequentie, kortste golflengte, meest energierijk/ioniserend).",
      uitleg: "Correcte volgorde in het elektromagnetisch spectrum."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de tandartsassistente de behandelkamer verlaat of achter een loden wand gaat staan wanneer er een röntgenfoto van jouw gebit gemaakt wordt, terwijl jij als patiënt gewoon in de stoel mag blijven zitten.",
      sleutelwoorden: ["cumulatieve dosis/dagelijks blootgesteld", "patiënt slechts één keer / heel lage dosis", "gezondheidsrisico/stralingsdosis beperken"],
      minTreffers: 2,
      modelantwoord: "Als patiënt krijg je slechts af en toe één foto (een verwaarloosbaar kleine stralingsdosis zonder gezondheidsrisico). De assistente maakt echter dagelijks tientallen foto's. Als zij telkens in de ruimte zou blijven, telt de totale opgetelde stralingsdosis (cumulatieve dosis) op tot een gevaarlijk niveau. Daarom moet zij zich beroepsmatig beschermen achter lood.",
      uitleg: "Verschil tussen eenmalige lage dosis voor patiënt en herhaalde beroepsmatige blootstelling."
    }
  ]
});
