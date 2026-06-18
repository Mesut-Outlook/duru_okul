/* Extra Proeftoets 21 — Directe & Indirecte Belastingen */
DURU.registerExamen({
  id: "ex-extra-directe-indirecte",
  titel: "Extra Proeftoets 21 — Directe & Indirecte Belastingen",
  vak: "Economie · Belastingen",
  icoon: "🧾",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is een belasting?",
      opties: [
        "Een vrijwillige gift aan een goed doel.",
        "Een verplichte bijdrage van burgers en bedrijven aan de overheid.",
        "Een lening die de overheid verstrekt aan bedrijven.",
        "Een bonus die de werkgever uitbetaalt."
      ],
      antwoord: 1,
      uitleg: "Belasting is een **verplichte bijdrage** van burgers en bedrijven, waarmee de overheid collectieve voorzieningen zoals scholen, wegen en zorg betaalt."
    },
    {
      type: "mc",
      vraag: "Wat is het verschil tussen een directe en een indirecte belasting?",
      opties: [
        "Een directe belasting betaal je rechtstreeks aan de Belastingdienst, een indirecte belasting betaal je via een omweg (verwerkt in de prijs).",
        "Een directe belasting geldt alleen voor bedrijven, een indirecte belasting alleen voor burgers.",
        "Een directe belasting is altijd hoger dan een indirecte belasting.",
        "Er is geen verschil, het zijn twee namen voor hetzelfde."
      ],
      antwoord: 0,
      uitleg: "Bij een **directe belasting** betaal je rechtstreeks aan de Belastingdienst (zoals inkomstenbelasting). Bij een **indirecte belasting** betaal je via een omweg, omdat de belasting in de prijs van een product zit (zoals btw)."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende belastingen is een directe belasting?",
      opties: [
        "Btw op een nieuwe fiets.",
        "Accijns op een pakje sigaretten.",
        "Inkomstenbelasting over je salaris.",
        "Btw op een restaurantbezoek."
      ],
      antwoord: 2,
      uitleg: "**Inkomstenbelasting** betaal je rechtstreeks over je inkomen aan de Belastingdienst, dus dat is een **directe belasting**."
    },
    {
      type: "waaronwaar",
      vraag: "Btw is een voorbeeld van een indirecte belasting.",
      antwoord: true,
      uitleg: "Waar. **Btw** zit verwerkt in de winkelprijs. De winkelier draagt het bedrag af aan de Belastingdienst, jij betaalt het via een omweg."
    },
    {
      type: "mc",
      vraag: "Wie draagt de btw die jij als consument betaalt, uiteindelijk af aan de Belastingdienst?",
      opties: [
        "Jijzelf, rechtstreeks elk jaar.",
        "De winkelier of verkoper.",
        "De gemeente waarin je woont.",
        "Niemand, btw wordt niet afgedragen."
      ],
      antwoord: 1,
      uitleg: "Bij een indirecte belasting zoals btw betaalt de **winkelier/verkoper** het bedrag aan de Belastingdienst, niet de consument zelf rechtstreeks."
    },
    {
      type: "waaronwaar",
      vraag: "Vennootschapsbelasting is een belasting die bedrijven betalen over hun winst, en is een directe belasting.",
      antwoord: true,
      uitleg: "Waar. **Vennootschapsbelasting** betalen bedrijven rechtstreeks aan de Belastingdienst over hun winst, dus dat is een **directe belasting**."
    },
    {
      type: "mc",
      vraag: "Waarom heft de overheid belasting?",
      opties: [
        "Om winst te maken zoals een bedrijf.",
        "Om collectieve voorzieningen te kunnen betalen, zoals scholen, wegen, zorg en de brandweer.",
        "Omdat de wet dit toevallig zo wil, zonder verder doel.",
        "Om de export van Nederland te verhogen."
      ],
      antwoord: 1,
      uitleg: "Met belastinggeld betaalt de overheid **collectieve voorzieningen**: dingen waar iedereen gebruik van maakt, zoals onderwijs, infrastructuur, veiligheid en zorg."
    },
    {
      type: "waaronwaar",
      vraag: "Het standaard btw-tarief in Nederland is 21%.",
      antwoord: true,
      uitleg: "Waar. Het **standaardtarief** btw is 21%. Voor bepaalde producten, zoals boodschappen, geldt een laag tarief van 9%."
    },
    {
      type: "invul",
      vraag: "Welk btw-tarief geldt er voor boodschappen zoals brood en groente: 21% of ____%?",
      antwoord: "9",
      uitleg: "Voor eerste levensbehoeften zoals boodschappen geldt het **lage btw-tarief van 9%**, in plaats van het standaardtarief van 21%."
    },
    {
      type: "mc",
      vraag: "Welke belasting is GEEN voorbeeld van een directe belasting?",
      opties: [
        "Inkomstenbelasting.",
        "Vennootschapsbelasting.",
        "Accijns.",
        "Loonbelasting."
      ],
      antwoord: 2,
      uitleg: "**Accijns** is een indirecte belasting: deze zit verwerkt in de prijs van producten zoals benzine of tabak en wordt door de verkoper afgedragen."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een indirecte belasting weet je als consument altijd precies hoeveel belasting je per product betaalt, omdat dit los wordt vermeld op de kassabon.",
      antwoord: false,
      uitleg: "Onwaar. De btw zit **verwerkt in de prijs**. Hoewel het bedrag soms op de bon staat, betaal je het via een omweg, zonder een apart formulier of aangifte zoals bij directe belasting."
    },
    {
      type: "invul",
      vraag: "Aan welke instantie betaal je inkomstenbelasting rechtstreeks?",
      antwoord: "belastingdienst",
      uitleg: "Inkomstenbelasting is een directe belasting: je betaalt deze rechtstreeks aan de **Belastingdienst**."
    },
    {
      type: "invul",
      vraag: "Hoe noemen we belasting die je via een omweg betaalt, verwerkt in de prijs van een product?",
      antwoord: "indirecte belasting|indirecte belastingen",
      uitleg: "Belasting die verwerkt is in de prijs en via een omweg bij de overheid terechtkomt, heet een **indirecte belasting**."
    },
    {
      type: "open",
      vraag: "Leg uit wat het verschil is tussen een directe en een indirecte belasting, en geef van elk één voorbeeld.",
      sleutelwoorden: ["rechtstreeks/zelf betalen aan belastingdienst", "omweg/verwerkt in de prijs", "inkomstenbelasting/vennootschapsbelasting", "btw/accijns"],
      minTreffers: 2,
      modelantwoord: "Een directe belasting betaal je rechtstreeks aan de Belastingdienst, bijvoorbeeld inkomstenbelasting. Een indirecte belasting betaal je via een omweg, omdat deze verwerkt is in de prijs van een product, bijvoorbeeld btw. Bij indirecte belasting draagt de winkelier het bedrag af aan de Belastingdienst.",
      uitleg: "Het kernverschil zit in de manier van betalen: rechtstreeks (direct) of via de prijs van een product (indirect)."
    },
    {
      type: "open",
      vraag: "Waarom heeft de overheid belasting nodig om collectieve voorzieningen te kunnen betalen?",
      sleutelwoorden: ["geen winstoogmerk/gratis voor gebruiker", "iedereen profiteert/samen betalen", "scholen/wegen/zorg/brandweer/politie"],
      minTreffers: 2,
      modelantwoord: "Collectieve voorzieningen zoals scholen, wegen, de brandweer en de zorg zijn er voor iedereen, en niemand betaalt er apart voor bij gebruik. Daarom haalt de overheid geld op via belasting, zodat deze voorzieningen toch betaald en voor iedereen beschikbaar kunnen blijven.",
      uitleg: "Belasting is de manier waarop de overheid gezamenlijke kosten verdeelt over alle burgers en bedrijven."
    }
  ]
});
