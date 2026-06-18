/* Extra Proeftoets 24 — Btw & Accijns Berekenen */
DURU.registerExamen({
  id: "ex-extra-btw-accijns-rekenen",
  titel: "Extra Proeftoets 24 — Btw & Accijns Berekenen",
  vak: "Economie · Belastingen",
  icoon: "🧮",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Een trui kost € 60,50 inclusief 21% btw. Wat is de prijs exclusief btw?",
      opties: [
        "€ 50,00",
        "€ 47,80",
        "€ 39,50",
        "€ 73,21"
      ],
      antwoord: 0,
      uitleg: "De prijs inclusief btw is 121%. De prijs exclusief btw is: **60,50 / 1,21 = € 50,00**."
    },
    {
      type: "mc",
      vraag: "Een brood kost € 3,27 inclusief 9% btw. Hoeveel btw zit er in deze prijs verwerkt?",
      opties: [
        "€ 0,27",
        "€ 0,29",
        "€ 0,30",
        "€ 2,97"
      ],
      antwoord: 0,
      uitleg: "De prijs inclusief btw is 109%. De btw bedraagt: **(3,27 / 109) * 9 = € 0,27**."
    },
    {
      type: "mc",
      vraag: "Een fiets kost € 350,- exclusief btw. De winkelier rekent hierover 21% btw. Wat is de verkoopprijs inclusief btw?",
      opties: [
        "€ 371,00",
        "€ 423,50",
        "€ 350,21",
        "€ 276,50"
      ],
      antwoord: 1,
      uitleg: "Btw bedraagt: **350 * 0,21 = € 73,50**. Verkoopprijs inclusief btw = **350 + 73,50 = € 423,50** (of direct **350 * 1,21**)."
    },
    {
      type: "waaronwaar",
      vraag: "Hoe hoger het btw-tarief op een product, hoe groter het deel van de verkoopprijs dat naar de overheid gaat.",
      antwoord: true,
      uitleg: "Waar. Btw is een percentage van de prijs. Een **hoger btw-tarief** (21% in plaats van 9%) betekent dat een groter deel van het bedrag dat je betaalt, naar de overheid gaat."
    },
    {
      type: "mc",
      vraag: "Tara koopt een liter benzine voor € 2,10. Hierin zit zowel btw als accijns verwerkt. Wat is het doel van de accijns op benzine, naast het opleveren van inkomsten?",
      opties: [
        "Het stimuleren van meer autogebruik.",
        "Het ontmoedigen van het gebruik van benzine, omdat dit slecht is voor het milieu.",
        "Het verlagen van de prijs van benzine voor de consument.",
        "Het stimuleren van de export van benzine."
      ],
      antwoord: 1,
      uitleg: "**Accijns** maakt schadelijke producten zoals benzine duurder, om het gebruik te **ontmoedigen** — naast dat het de overheid extra inkomsten oplevert."
    },
    {
      type: "waaronwaar",
      vraag: "Een subsidie op zonnepanelen heeft als doel het gebruik van zonnepanelen te ontmoedigen.",
      antwoord: false,
      uitleg: "Onwaar. Een **subsidie** is bedoeld om iets juist te **stimuleren**: door zonnepanelen goedkoper te maken, worden mensen aangemoedigd om ze aan te schaffen."
    },
    {
      type: "invul",
      vraag: "Een blikje energiedrank kost € 1,21 inclusief 21% btw. Hoeveel euro is dat exclusief btw?",
      antwoord: "1|1,00|1,-",
      uitleg: "De prijs inclusief btw is 121%. Exclusief btw is: **1,21 / 1,21 = € 1,00**."
    },
    {
      type: "mc",
      vraag: "Wat is het belangrijkste verschil tussen een subsidie en een accijns als het gaat om het beïnvloeden van gedrag?",
      opties: [
        "Subsidie ontmoedigt gedrag, accijns stimuleert gedrag.",
        "Subsidie maakt iets goedkoper om het te stimuleren, accijns maakt iets duurder om het te ontmoedigen.",
        "Subsidie en accijns hebben precies hetzelfde effect.",
        "Subsidie geldt alleen voor bedrijven, accijns alleen voor consumenten."
      ],
      antwoord: 1,
      uitleg: "Een **subsidie** verlaagt de prijs om iets te stimuleren (zoals sport of energiebesparing). **Accijns** verhoogt de prijs om iets te ontmoedigen (zoals roken of autorijden)."
    },
    {
      type: "waaronwaar",
      vraag: "Door subsidie op museumbezoek wordt een museumkaart duurder, zodat minder mensen naar het museum gaan.",
      antwoord: false,
      uitleg: "Onwaar. Subsidie maakt iets juist **goedkoper**, zodat méér mensen ervan gebruikmaken, niet minder."
    },
    {
      type: "mc",
      vraag: "Sven betaalt voor een nieuwe jas € 121,- inclusief 21% btw. Hoeveel procent van de prijs die hij betaalt, gaat naar de overheid (afgerond)?",
      opties: [
        "9%",
        "17%",
        "21%",
        "25%"
      ],
      antwoord: 2,
      uitleg: "De btw zit als 21% verwerkt in de prijs exclusief btw (121% totaal). Het bedrag dat naar de overheid gaat is: **121 - (121/1,21) = € 21,-**, wat ongeveer **21/121 ≈ 17%** van de totale betaalde prijs is, maar het tarief zelf — het percentage waarmee gerekend wordt — is **21%**."
    },
    {
      type: "invul",
      vraag: "Een pak koffie kost € 5,45 inclusief 9% btw. Hoeveel euro is dat exclusief btw?",
      antwoord: "5|5,00|5,-",
      uitleg: "De prijs inclusief btw is 109%. Exclusief btw is: **5,45 / 1,09 = € 5,00**."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een hoger btw-tarief op een product betaal je als consument verhoudingsgewijs meer belasting in de prijs.",
      antwoord: true,
      uitleg: "Waar. Bij het standaardtarief van **21%** betaal je verhoudingsgewijs meer belasting in de prijs dan bij het lage tarief van **9%**."
    },
    {
      type: "invul",
      vraag: "Welk woord beschrijft een financiële bijdrage van de overheid die iets goedkoper maakt om het te stimuleren?",
      antwoord: "subsidie",
      uitleg: "Een **subsidie** is een bijdrage van de overheid om iets te stimuleren, zoals sport, energiebesparing of cultuur."
    },
    {
      type: "open",
      vraag: "Een spelcomputer kost € 363,- inclusief 21% btw. Laat met een berekening zien hoe je de prijs exclusief btw en het btw-bedrag berekent.",
      sleutelwoorden: ["delen door 1,21/121%", "exclusief is 300/€300", "btw-bedrag/€63/aftrekken van 363"],
      minTreffers: 2,
      modelantwoord: "De prijs inclusief btw is 121%. Exclusief btw: 363 / 1,21 = € 300,-. Het btw-bedrag is dan 363 - 300 = € 63,-.",
      uitleg: "Formule: Excl. = Incl. / 1,21. Btw-bedrag = Incl. − Excl."
    },
    {
      type: "open",
      vraag: "Leg uit hoe de overheid met subsidie en accijns het gedrag van mensen op twee verschillende manieren kan beïnvloeden.",
      sleutelwoorden: ["subsidie maakt goedkoper/stimuleert", "accijns maakt duurder/ontmoedigt", "gewenst gedrag/sport/energiebesparing", "ongewenst gedrag/roken/alcohol/benzine"],
      minTreffers: 2,
      modelantwoord: "Met een subsidie maakt de overheid iets goedkoper, waardoor mensen worden gestimuleerd om dat gewenste gedrag te vertonen, bijvoorbeeld sporten of energiebesparende maatregelen nemen. Met accijns maakt de overheid schadelijke producten zoals tabak, alcohol of benzine juist duurder, om het gebruik daarvan te ontmoedigen.",
      uitleg: "Subsidie werkt met prijsverlaging om gewenst gedrag te stimuleren; accijns werkt met prijsverhoging om ongewenst gedrag te ontmoedigen."
    }
  ]
});
