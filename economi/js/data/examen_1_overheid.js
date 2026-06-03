/* Proeftoets 1 — De overheid (6.1 + 6.2) */
DURU.registerExamen({
  id: "ex-overheid",
  titel: "Proeftoets — Wie is de overheid?",
  vak: "Economie · H6 (6.1 & 6.2)",
  icoon: "🏛️",
  duurMin: 20,
  vragen: [

    /* ── PARAGRAAF 6.1 ── */

    {
      type: "mc", vraag: "Welke overheidslaag bestuurt heel Nederland?",
      opties: ["De gemeente", "De provincie", "De rijksoverheid", "De waterschappen"],
      antwoord: 2,
      uitleg: "De <b>rijksoverheid</b> (de regering in Den Haag) maakt regels en beslissingen voor het hele land. Gemeenten en provincies regelen alleen hun eigen gebied."
    },

    {
      type: "mc", vraag: "Uit hoeveel provincies bestaat Nederland?",
      opties: ["10", "11", "12", "13"],
      antwoord: 2,
      uitleg: "Nederland heeft precies <b>12 provincies</b>, van Groningen in het noorden tot Zeeland in het zuiden."
    },

    {
      type: "mc", vraag: "In welke stad vergadert de nationale regering van Nederland?",
      opties: ["Amsterdam", "Utrecht", "Rotterdam", "Den Haag"],
      antwoord: 3,
      uitleg: "<b>Den Haag</b> is de regeringsstad. Hier vergadert de regering, zitten de ministeries en is het parlement (de Staten-Generaal) gevestigd."
    },

    {
      type: "mc", vraag: "Wie maakt de dagelijkse beslissingen in een gemeente?",
      opties: ["De gemeenteraad", "Het college van B&W", "De burgemeester alleen", "Provinciale Staten"],
      antwoord: 1,
      uitleg: "Het <b>college van burgemeester en wethouders (B&W)</b> bestuurt de gemeente dag in dag uit. De gemeenteraad controleert hen en stelt de grote lijnen vast."
    },

    {
      type: "mc", vraag: "Uit hoeveel leden bestaat de Tweede Kamer?",
      opties: ["75", "100", "150", "225"],
      antwoord: 2,
      uitleg: "De <b>Tweede Kamer</b> telt <b>150 leden</b> die rechtstreeks door de bevolking worden gekozen. De Eerste Kamer heeft 75 leden."
    },

    {
      type: "mc", vraag: "Wie controleert het college van B&W in een gemeente?",
      opties: ["De provincie", "De Tweede Kamer", "De gemeenteraad", "De rijksoverheid"],
      antwoord: 2,
      uitleg: "De <b>gemeenteraad</b> is het gekozen orgaan dat het college van B&W controleert. De raad kiest ook de wethouders."
    },

    {
      type: "mc", vraag: "Welk orgaan bestuurt een provincie van dag tot dag?",
      opties: ["Provinciale Staten", "Gedeputeerde Staten", "Het college van B&W", "De gemeenteraad"],
      antwoord: 1,
      uitleg: "<b>Gedeputeerde Staten</b> (GS) bestuurt de provincie dagelijks — vergelijkbaar met het college van B&W in een gemeente. Provinciale Staten (PS) is het gekozen controleorgaan van de provincie."
    },

    {
      type: "mc", vraag: "Duru vraagt haar paspoort aan bij de overheid. Bij welke overheidslaag moet zij zijn?",
      opties: ["De rijksoverheid in Den Haag", "De provincie", "De gemeente", "Het waterschap"],
      antwoord: 2,
      uitleg: "Paspoorten en identiteitsbewijzen vraag je aan bij de <b>gemeente</b> waar je woont. Dit is een taak van de gemeentelijke overheid."
    },

    {
      type: "waaronwaar", vraag: "De Eerste Kamer heeft meer leden dan de Tweede Kamer.",
      antwoord: false,
      uitleg: "Onwaar. De <b>Tweede Kamer</b> heeft <b>150 leden</b> en de Eerste Kamer heeft <b>75 leden</b>. De Tweede Kamer is dus groter."
    },

    {
      type: "waaronwaar", vraag: "Een provincie regelt zaken voor een kleiner gebied dan een gemeente.",
      antwoord: false,
      uitleg: "Onwaar. Een <b>provincie</b> is groter dan een gemeente. Een provincie bestaat uit meerdere gemeenten. Nederland heeft 12 provincies maar honderden gemeenten."
    },

    {
      type: "waaronwaar", vraag: "De burgemeester is de voorzitter van de gemeenteraad én van het college van B&W.",
      antwoord: true,
      uitleg: "Waar. De <b>burgemeester</b> is voorzitter van zowel de gemeenteraad als het college van B&W. De burgemeester wordt niet gekozen maar benoemd door de Kroon."
    },

    {
      type: "waaronwaar", vraag: "Leden van Provinciale Staten worden rechtstreeks door de bevolking gekozen.",
      antwoord: true,
      uitleg: "Waar. De leden van <b>Provinciale Staten</b> worden elke vier jaar door de inwoners van de provincie gekozen — net zoals de gemeenteraad en de Tweede Kamer."
    },

    {
      type: "invul", vraag: "De overheid bestaat uit drie lagen: het Rijk, de ______ en de gemeente.",
      antwoord: "provincie|de provincie|provincies",
      uitleg: "De drie lagen van de overheid zijn het <b>Rijk</b> (nationaal), de <b>provincie</b> (regionaal) en de <b>gemeente</b> (lokaal). Ze zijn van groot naar klein."
    },

    {
      type: "invul", vraag: "Het dagelijks bestuur van een gemeente heet het college van burgemeester en ______.",
      antwoord: "wethouders|de wethouders",
      uitleg: "Het <b>college van burgemeester en wethouders (B&W)</b> vormt het dagelijks bestuur van de gemeente. Wethouders zijn als ministers van de gemeente."
    },

    {
      type: "open", vraag: "Leg uit wat de drie lagen van de overheid in Nederland zijn en geef van elke laag een voorbeeld van een taak die zij uitvoert.",
      sleutelwoorden: ["rijk/rijksoverheid", "provincie", "gemeente", "taak/voorbeeld/regelt"],
      minTreffers: 3,
      modelantwoord: "De drie lagen zijn: (1) het Rijk, dat regels maakt voor heel Nederland, zoals de belastingwet of de politie. (2) De provincie, die zorgt voor regionale taken zoals ruimtelijke ordening en provinciale wegen. (3) De gemeente, die lokale taken uitvoert zoals het afgeven van paspoorten, het onderhoud van straten en de lokale zorg.",
      uitleg: "Onthoud: Rijk (nationaal) → provincie (regionaal) → gemeente (lokaal). Elke laag heeft zijn eigen taken en zijn eigen gebied."
    },

    {
      type: "open", vraag: "Wat is het verschil tussen de gemeenteraad en het college van B&W?",
      sleutelwoorden: ["gemeenteraad/gekozen/controle/controleren", "B&W/burgemeester/wethouders/bestuur/dagelijks"],
      minTreffers: 2,
      modelantwoord: "De gemeenteraad is het gekozen orgaan dat de grote beslissingen neemt en het college van B&W controleert. Het college van B&W (burgemeester en wethouders) voert het dagelijks bestuur uit.",
      uitleg: "Simpel gezegd: de <b>gemeenteraad</b> = controleur (gekozen), het <b>college van B&W</b> = dagelijks bestuur (uitvoerder)."
    },

    /* ── PARAGRAAF 6.2 ── */

    {
      type: "mc", vraag: "Wat zijn collectieve voorzieningen?",
      opties: [
        "Producten die je zelf in de winkel koopt",
        "Spullen en diensten die de overheid voor iedereen regelt en betaalt",
        "Goederen die alleen voor rijke mensen zijn",
        "Diensten die bedrijven aanbieden voor winst"
      ],
      antwoord: 1,
      uitleg: "<b>Collectieve voorzieningen</b> zijn spullen en diensten die de overheid voor iedereen regelt en betaalt, zoals politie, onderwijs en wegen. Ze worden betaald uit belastinggeld."
    },

    {
      type: "mc", vraag: "Waarom zorgt de overheid voor collectieve voorzieningen en doet de markt dit niet?",
      opties: [
        "Omdat bedrijven te groot zijn om dit te regelen",
        "Omdat het te duur is en iedereen er baat bij heeft, ook wie niet betaalt",
        "Omdat de overheid meer geld heeft dan bedrijven",
        "Omdat de wet dit verbiedt aan bedrijven"
      ],
      antwoord: 1,
      uitleg: "Collectieve voorzieningen zoals veiligheid en dijken zijn <b>voor iedereen tegelijk</b> beschikbaar — ook wie niet betaalt profiteert mee. Bedrijven hebben dan geen prikkel om ze aan te bieden, want je kunt mensen niet uitsluiten. Daarom regelt de overheid dit."
    },

    {
      type: "mc", vraag: "Welke van de volgende zaken is GEEN voorbeeld van een collectieve voorziening?",
      opties: ["Een snelweg", "Politie en brandweer", "Een televisie kopen bij MediaMarkt", "Een openbare school"],
      antwoord: 2,
      uitleg: "Een televisie kopen is een <b>individuele</b> (privé) aankoop — jij betaalt, jij hebt hem. Snelwegen, politie en openbare scholen zijn collectieve voorzieningen: de overheid regelt en betaalt ze voor iedereen."
    },

    {
      type: "mc", vraag: "Waarmee betaalt de overheid de collectieve voorzieningen?",
      opties: ["Met leningen van banken", "Met belastinggeld dat burgers en bedrijven betalen", "Met geld dat de overheid zelf verdient door producten te verkopen", "Met donaties van rijke burgers"],
      antwoord: 1,
      uitleg: "Collectieve voorzieningen worden betaald uit <b>belastingen</b>. Iedereen betaalt belasting (inkomstenbelasting, btw, enz.) en de overheid gebruikt dat geld om voorzieningen voor iedereen te bekostigen."
    },

    {
      type: "mc", vraag: "Welke vier gebieden noemt het boek als de belangrijkste collectieve voorzieningen?",
      opties: [
        "Sport, kunst, toerisme en landbouw",
        "Veiligheid, infrastructuur, onderwijs en zorg",
        "Energie, water, telefoon en internet",
        "Huisvesting, voedsel, kleding en vervoer"
      ],
      antwoord: 1,
      uitleg: "Het boek noemt <b>veiligheid</b> (politie, brandweer, leger), <b>infrastructuur</b> (wegen, bruggen), <b>onderwijs</b> (scholen) en <b>zorg</b> (ziekenhuizen, AOW) als de vier grote collectieve voorzieningen."
    },

    {
      type: "waaronwaar", vraag: "Collectieve voorzieningen worden betaald door de mensen die er gebruik van maken.",
      antwoord: false,
      uitleg: "Onwaar. Collectieve voorzieningen worden betaald door <b>iedereen via belastingen</b> — ook mensen die er op dat moment geen gebruik van maken. Zo betaal je ook mee aan de brandweer, ook als jouw huis niet brandt."
    },

    {
      type: "waaronwaar", vraag: "Zonder de overheid zou er waarschijnlijk te weinig politie en te weinig dijkonderhoud zijn.",
      antwoord: true,
      uitleg: "Waar. Politie en dijken zijn collectieve voorzieningen: iedereen profiteert, maar niemand wil vrijwillig alleen betalen. Zonder overheid die dit organiseert en financiert via belastingen, zou er te weinig van zijn."
    },

    {
      type: "open", vraag: "Geef twee redenen waarom de overheid het onderwijs regelt en betaalt, in plaats van dat ieder gezin zelf een school moet betalen.",
      sleutelwoorden: ["iedereen/gelijk/gelijke kansen", "belasting/collectief/samen", "arm/arme/inkomen/betalen", "maatschappij/samenleving/belang"],
      minTreffers: 2,
      modelantwoord: "Ten eerste heeft iedereen recht op gelijke kansen: als ouders zelf moesten betalen, zouden arme kinderen misschien niet naar school kunnen. Ten tweede is goed onderwijs goed voor de hele samenleving: meer kennis = betere banen = meer welvaart voor iedereen. Daarom is onderwijs een collectieve voorziening betaald uit belastingen.",
      uitleg: "Denk aan <b>gelijke kansen</b> en <b>maatschappelijk belang</b>: goede burgers en werknemers zijn goed voor iedereen, dus betalen we er samen aan mee via belastingen."
    },

    {
      type: "invul", vraag: "Spullen en diensten die de overheid voor iedereen regelt en betaalt heten ______ voorzieningen.",
      antwoord: "collectieve|collectief",
      uitleg: "<b>Collectieve voorzieningen</b> zijn er voor de hele gemeenschap (collectief = samen). Ze worden betaald uit belastingen en zijn beschikbaar voor iedereen."
    }

  ]
});
