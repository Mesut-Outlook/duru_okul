/* Extra Proeftoets 11 — De Rijksbegroting in Detail */
DURU.registerExamen({
  id: "ex-extra-rijksbegroting-detail",
  titel: "Extra Proeftoets 11 — De Rijksbegroting in Detail",
  vak: "Economie · Begroting",
  icoon: "💼",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Welk ministerie coördineert het opstellen van de Rijksbegroting?",
      opties: [
        "Het Ministerie van Sociale Zaken en Werkgelegenheid",
        "Het Ministerie van Financiën",
        "Het Ministerie van Algemene Zaken (Minister-President)",
        "Het Ministerie van Economische Zaken en Klimaat"
      ],
      antwoord: 1,
      uitleg: "De Minister van **Financiën** stelt samen met alle andere ministers de begroting op en houdt toezicht op de staatskas."
    },
    {
      type: "mc",
      vraag: "Wat is de allergrootste uitgavenpost op de Nederlandse Rijksbegroting?",
      opties: [
        "Defensie (leger)",
        "Infrastructuur (wegen en spoor)",
        "Zorg en Sociale Zekerheid (uitkeringen, zorgtoeslag en pensioenen)",
        "Onderwijs en Wetenschap"
      ],
      antwoord: 2,
      uitleg: "Veruit het meeste overheidsgeld gaat naar de **zorg** en de **sociale zekerheid** (zoals AOW en bijstand)."
    },
    {
      type: "mc",
      vraag: "Wat is een overdrachtsinkomen?",
      opties: [
        "Het loon dat je ontvangt van je werkgever.",
        "Een uitkering of toeslag van de overheid waarvoor je geen directe tegenprestatie (werk) hoeft te leveren.",
        "Geld dat je leent bij de bank om een huis te kopen.",
        "De winst die een winkelier maakt op de verkoop van kleding."
      ],
      antwoord: 1,
      uitleg: "Voorbeelden van **overdrachtsinkomens** zijn kinderbijslag, zorgtoeslag, AOW en de WW-uitkering."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de staatsschuld als de overheid meerdere jaren achter elkaar een begrotingstekort heeft?",
      opties: [
        "De staatsschuld daalt omdat de economie groeit.",
        "De staatsschuld stijgt omdat de overheid extra geld moet lenen om de tekorten te betalen.",
        "De staatsschuld blijft precies gelijk.",
        "De staatsschuld wordt kwijtgescholden door de Europese Unie."
      ],
      antwoord: 1,
      uitleg: "Elk jaar dat er een **begrotingstekort** is, moet de overheid dit tekort financieren door geld te lenen op de kapitaalmarkt, wat de **staatsschuld** vergroot."
    },
    {
      type: "mc",
      vraag: "Wat is de staatsschuldquote?",
      opties: [
        "Het bedrag dat elke burger moet betalen om de schuld af te lossen.",
        "De totale staatsschuld uitgedrukt als percentage van het Bruto Binnenlands Product (BBP / het inkomen van het hele land).",
        "Het tarief van de btw in procenten.",
        "De maximale lening die de koning mag afsluiten."
      ],
      antwoord: 1,
      uitleg: "De **staatsschuldquote** geeft aan hoe zwaar de schuld drukt op de totale economie van het land."
    },
    {
      type: "waaronwaar",
      vraag: "De Tweede Kamer mag wijzigingen aanbrengen in de Rijksbegroting van een ministerie (recht van amendement).",
      antwoord: true,
      uitleg: "Waar. Dit hoort bij het **budgetrecht** van het parlement: zij bepalen uiteindelijk waar het geld naartoe gaat."
    },
    {
      type: "waaronwaar",
      vraag: "De koning bepaalt zelfstandig hoe hoog de btw in Nederland wordt.",
      antwoord: false,
      uitleg: "Onwaar. Belastingtarieven worden voorgesteld door de minister en vastgesteld door het parlement (Eerste en Tweede Kamer)."
    },
    {
      type: "invul",
      vraag: "Het document waarin de plannen van de overheid staan en de cijfers van de Rijksbegroting worden toegelicht heet de ____________.",
      antwoord: "Miljoenennota",
      uitleg: "De **Miljoenennota** verschijnt elk jaar op Prinsjesdag en bevat de toelichting op de begroting."
    },
    {
      type: "open",
      vraag: "Leg uit hoe een stijging van de staatsschuld ertoe kan leiden dat de overheid in de toekomst moet bezuinigen op zorg en onderwijs.",
      sleutelwoorden: ["rente/rentelasten/rente betalen", "minder geld overblijven/minder te besteden", "bezuinigen/bezuinigingen/kosten drukken"],
      minTreffers: 2,
      modelantwoord: "Als de staatsschuld stijgt, moet de overheid meer rente betalen over die schuld. Deze rentelasten zijn verplichte uitgaven. Hierdoor blijft er minder geld over op de begroting voor andere belangrijke zaken zoals zorg, onderwijs en veiligheid, waardoor de overheid daarop moet bezuinigen.",
      uitleg: "Rentelasten drukken andere begrotingsuitgaven weg (verdringingseffect)."
    },
    {
      type: "open",
      vraag: "Wat is het verschil tussen overheidsuitgaven aan voorzieningen (zoals infrastructuur) en uitgaven aan overdrachtsinkomens?",
      sleutelwoorden: ["voorzieningen/dienst/dienstverlening/wegen/infrastructuur", "overdrachtsinkomens/geld/direct/uitkering/burgers/toeslag", "geen tegenprestatie/tegenprestatie"],
      minTreffers: 2,
      modelantwoord: "Uitgaven aan voorzieningen zijn bedoeld voor goederen of diensten waar iedereen gebruik van maakt (zoals wegen, politie en dijken). Overdrachtsinkomens zijn directe geldelijke bijdragen (zoals uitkeringen en toeslagen) die de overheid overdraagt aan individuele burgers om hun inkomen te ondersteunen, zonder dat zij hier een directe tegenprestatie voor leveren.",
      uitleg: "Voorzieningen = tastbare zaken/infrastructuur. Overdracht = inkomensoverdracht aan burgers."
    }
  ]
});
