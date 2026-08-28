/* Proeftoets 1 — Economie HAVO 3: Hoofdstuk 4 (Het bedrijfsleven - Deel 1)
   Focus: Paragraaf 4.1 — Produceren, consumeren, zelfvoorziening, kringloop en productiefactoren.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-economie-1",
  titel: "Toets 1 — Produceren, Consumeren & Productiefactoren",
  vak: "Economie · HAVO 3 (H4)",
  icoon: "🏭",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de economische definitie van <b>produceren</b>?",
      opties: [
        "Het maken van goederen of het leveren van diensten door bedrijven voor anderen",
        "Het kopen van spullen in een winkel",
        "Het sparen van geld op een bankrekening",
        "Het weggooien van afval"
      ],
      antwoord: 0,
      uitleg: "Produceren is het voortbrengen van goederen en diensten door producenten voor consumenten of andere bedrijven."
    },
    {
      type: "mc",
      vraag: "Wat is <b>zelfvoorziening</b>?",
      opties: [
        "Alleen geld uitgeven aan luxegoederen",
        "Wanneer consumenten goederen of diensten voor zichzelf maken zonder tussenkomst van bedrijven (bijv. zelf groenten verbouwen of zelf koken)",
        "Werken voor de overheid",
        "Geld lenen van vrienden"
      ],
      antwoord: 1,
      uitleg: "Zelfvoorziening = voor jezelf produceren (geen ruil met geld)."
    },
    {
      type: "mc",
      vraag: "Welke <b>vier productiefactoren</b> worden in de economie onderscheiden?",
      opties: [
        "Consumenten, Winkels, Fabrieken en Banken",
        "Geld, Goud, Aandelen en Vastgoed",
        "Kapitaal, Arbeid, Natuur en Ondernemerschap (KANO)",
        "Import, Export, Belasting en Subsidie"
      ],
      antwoord: 2,
      uitleg: "De 4 productiefactoren zijn: Kapitaal (machines/gebouwen), Arbeid (werknemers), Natuur (grond/grondstoffen), Ondernemerschap (organisatie/risico). Ezelsbruggetje: KANO."
    },
    {
      type: "invul",
      vraag: "Welke beloning (inkomen) ontvangt de productiefactor <b>arbeid</b>?",
      antwoord: "loon|salaris",
      uitleg: "Voor arbeid ontvang je loon (of salaris)."
    },
    {
      type: "invul",
      vraag: "Welke beloning ontvangt de productiefactor <b>ondernemerschap</b>?",
      antwoord: "winst",
      uitleg: "De ondernemer neemt risico en ontvangt winst als beloning."
    },
    {
      type: "invul",
      vraag: "Welke beloning ontvangt de productiefactor <b>kapitaal</b> (voor uitgeleend geld)?",
      antwoord: "rente|interest",
      uitleg: "Voor kapitaal ontvang je rente (of huur bij kapitaalgoederen)."
    },
    {
      type: "mc",
      vraag: "Onder welke productiefactor valt een vrachtwagen die door een transportbedrijf wordt gekocht?",
      opties: [
        "Consumptie",
        "Natuur",
        "Arbeid",
        "Kapitaal (kapitaalgoederen)"
      ],
      antwoord: 3,
      uitleg: "Een vrachtwagen is een kapitaalgoed (vast productiemiddel om mee te produceren)."
    },
    {
      type: "waaronwaar",
      vraag: "Als je moeder thuis voor het gezin kookt, is dat economisch gezien consumptie/zelfvoorziening; als een kok in een restaurant dezelfde maaltijd kookt, is het productie.",
      antwoord: true,
      uitleg: "Waar. In een restaurant wordt geproduceerd voor de verkoop aan anderen (toegevoegde waarde met geldstroom)."
    },
    {
      type: "mc",
      vraag: "Wat is een <b>bedrijfskolom</b>?",
      opties: [
        "Een schematisch overzicht van alle opeenvolgende bedrijven die meewerken aan de productie van een product, van oerproducent (grondstof) tot en met de winkelier",
        "Een grote fabrieksschoorsteen",
        "De winst- en verliesrekening van één winkel",
        "Een lijst met alle werknemers van een bedrijf"
      ],
      antwoord: 0,
      uitleg: "De bedrijfskolom toont de keten van grondstof tot consument (bijv. katoenplantage -> weverij -> kledingfabriek -> groothandel -> winkel)."
    },
    {
      type: "waaronwaar",
      vraag: "De consument maakt ZELF onderdeel uit van de bedrijfskolom.",
      antwoord: false,
      uitleg: "Niet waar. De bedrijfskolom stopt bij de detailhandel (de winkel). De consument staat eronder en hoort niet bij de bedrijven."
    },
    {
      type: "invul",
      vraag: "Hoe noem je het verschil tussen de verkoopprijs en de inkoopprijs van een product bij een bedrijf?",
      antwoord: "toegevoegde waarde",
      uitleg: "Toegevoegde waarde = verkoopprijs - inkoopprijs (waarde die het bedrijf toevoegt door bewerking, opslag of transport)."
    },
    {
      type: "mc",
      vraag: "Een stoffenfabrikant koopt katoen in voor € 3,00 per meter en verkoopt de geweven stof voor € 8,00 per meter aan de kledingfabriek. Hoeveel waarde voegt de stoffenfabrikant toe per meter?",
      opties: [
        "€ 11,00",
        "€ 5,00",
        "€ 8,00",
        "€ 3,00"
      ],
      antwoord: 1,
      uitleg: "Toegevoegde waarde = € 8,00 - € 3,00 = € 5,00."
    },
    {
      type: "mc",
      vraag: "Wat is het verschil tussen een <b>handelsonderneming</b> en een <b>productieonderneming</b>?",
      opties: [
        "Een productieonderneming heeft geen machines",
        "Een handelsonderneming maakt geen winst",
        "Een handelsonderneming verandert niets aan het product (koopt in en verkoopt door); een productieonderneming maakt van grondstoffen nieuwe producten",
        "Er is geen verschil"
      ],
      antwoord: 2,
      uitleg: "Handelsonderneming = winkels/groothandels (doorverkoop). Productieonderneming = fabrieken/boerderijen (bewerken/maken)."
    },
    {
      type: "mc",
      vraag: "Welk bedrijf is een voorbeeld van een <b>dienstverlenend bedrijf</b>?",
      opties: [
        "Een bakkerij die brood bakt",
        "Een schoenenfabriek",
        "Een olieraffinaderij",
        "Een kapper"
      ],
      antwoord: 3,
      uitleg: "Een kapper verleent een dienst (handeling) en verkoopt geen zelfgemaakt tastbaar product."
    },
    {
      type: "waaronwaar",
      vraag: "Door de inzet van kapitaalgoederen (zoals machines) kan de arbeidsproductiviteit van werknemers aanzienlijk stijgen.",
      antwoord: true,
      uitleg: "Waar. Met een machine kan één werknemer per uur veel meer producten maken."
    },
    {
      type: "invul",
      vraag: "Hoeveel productiefactoren zijn er in totaal volgens de economische theorie? (Geef het getal)",
      antwoord: "4|vier",
      uitleg: "4: Kapitaal, Arbeid, Natuur, Ondernemerschap."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende zaken hoort bij de productiefactor <b>natuur</b>?",
      opties: [
        "Zonlicht, windenergie en ruwe aardolie in de grond",
        "Een banklening van € 50.000",
        "De heftruck in het magazijn",
        "Het salaris van de directeur"
      ],
      antwoord: 0,
      uitleg: "Natuur = alle onbewerkte natuurlijke hulpbronnen, grond en energiebronnen."
    },
    {
      type: "waaronwaar",
      vraag: "Een meubelwinkel die kasten inkoopt bij de fabriek en verkoopt aan consumenten is een productieonderneming.",
      antwoord: false,
      uitleg: "Niet waar. Een meubelwinkel is een handelsonderneming (detailhandel)."
    },
    {
      type: "open",
      vraag: "Noem de <b>vier productiefactoren</b> en geef bij elke factor een concreet voorbeeld van een middel dat een bakkerij nodig heeft om brood te bakken.",
      sleutelwoorden: ["1. Kapitaal: deegmachine / oven / bestelbus / winkelpand", "2. Arbeid: bakkersknecht / verkoopster", "3. Natuur: graan / water / zout / aardgas", "4. Ondernemerschap: bakker / eigenaar die het bedrijf leidt"],
      minTreffers: 3,
      modelantwoord: "De vier productiefactoren bij een bakkerij:\n1. Kapitaal: De deegmengmachine, de bakovens, het winkelpand en de bestelbus.\n2. Arbeid: De bakker en het winkelpersoneel die het werk uitvoeren.\n3. Natuur: Het meel/graan, water, zout en de energie (gas/stroom voor de oven).\n4. Ondernemerschap: De bakkerseigenaar die de grondstoffen inkoopt, personeel aanstuurt en financieel risico draagt.",
      uitleg: "Toepassing van de productiefactoren op een concrete onderneming."
    },
    {
      type: "open",
      vraag: "Leg uit hoe een <b>bedrijfskolom</b> werkt aan de hand van de productie van een katoenen spijkerbroek. Noem minstens vier schakels in deze keten.",
      sleutelwoorden: ["katoenplantage (oerteler)", "weverij / stoffenfabriek", "kledingfabriek (confectie)", "groothandel / kledingwinkel (detailhandel)"],
      minTreffers: 3,
      modelantwoord: "Een bedrijfskolom toont de route van grondstof tot eindproduct:\n1. Katoenplantage: Verbouwt en oogst ruwe katoen.\n2. Spinnerij / Weverij: Spint draden en weeft spijkerstof (denim).\n3. Kledingfabriek: Knipt en naait de stof tot spijkerbroeken.\n4. Groothandel / Kledingwinkel: Koopt de broeken in partijen in en verkoopt ze in de winkel aan de consument.\n(De consument staat aan het eind buiten de bedrijfskolom).",
      uitleg: "Opbouw van een bedrijfskolom."
    }
  ]
});
