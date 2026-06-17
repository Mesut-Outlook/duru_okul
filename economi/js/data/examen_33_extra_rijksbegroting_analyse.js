/* Extra Proeftoets 28 — Diepgaande Rijksbegrotingsanalyse */
DURU.registerExamen({
  id: "ex-extra-rijksbegroting-analyse",
  titel: "Extra Proeftoets 28 — Diepgaande Rijksbegrotingsanalyse",
  vak: "Economie · Staatsfinanciën",
  icoon: "📊",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Welke twee posten vormen samen de allergrootste uitgaven op de Nederlandse Rijksbegroting?",
      opties: [
        "Defensie en Infrastructuur (wegen en openbaar vervoer).",
        "Zorg en Sociale Zekerheid (zoals uitkeringen en AOW).",
        "Onderwijs en Cultuur.",
        "Rente op de staatsschuld en politie."
      ],
      antwoord: 1,
      uitleg: "Meer dan de helft van alle overheidsuitgaven gaat naar de **zorg** en naar **sociale zekerheid/uitkeringen**."
    },
    {
      type: "waaronwaar",
      vraag: "De Rijksbegroting is een definitief overzicht van alle inkomsten en uitgaven van het afgelopen jaar.",
      antwoord: false,
      uitleg: "Onwaar. De Rijksbegroting is een **schatting/vooruitblik** van de verwachte inkomsten en uitgaven voor het *komende* jaar."
    },
    {
      type: "invul",
      vraag: "Welke nota, gepresenteerd in het bekende koffertje op Prinsjesdag, vat de plannen en de Rijksbegroting in grote lijnen samen?",
      antwoord: "Miljoenennota|miljoenennota",
      uitleg: "De **Miljoenennota** geeft het overzicht over de totale economische situatie en de begroting."
    },
    {
      type: "mc",
      vraag: "Wat zijn rentelasten op de Rijksbegroting?",
      opties: [
        "De rente die burgers ontvangen op hun spaarrekeningen.",
        "De rente die de overheid jaarlijks moet betalen aan beleggers over de uitstaande staatsschuld.",
        "De rente die commerciële banken aan elkaar betalen.",
        "Een extra belasting op leningen."
      ],
      antwoord: 1,
      uitleg: "Omdat de overheid een staatsschuld heeft, moet zij hierover jaarlijks **rente** betalen aan de schuldeisers."
    },
    {
      type: "waaronwaar",
      vraag: "Bezuinigen betekent dat de overheid besluit om minder geld uit te geven aan bepaalde posten om zo het begrotingstekort te verkleinen.",
      antwoord: true,
      uitleg: "Waar. **Bezuinigen** is het verlagen van overheidsuitgaven."
    },
    {
      type: "invul",
      vraag: "Hoe noem je belastingen die direct geheven worden over je inkomen, winst of vermogen (zoals de inkomstenbelasting)?",
      antwoord: "directe",
      uitleg: "**Directe belastingen** betaal je rechtstreeks aan de Belastingdienst over je eigen verdiende geld of bezit."
    },
    {
      type: "mc",
      vraag: "Wat is het financieringstekort van de overheid?",
      opties: [
        "Het begrotingstekort minus de aflossingen op de staatsschuld.",
        "Het totale bedrag dat de overheid aan btw binnenkrijgt.",
        "Het verschil tussen de inkomsten van het Rijk en de gemeenten.",
        "De rente die de overheid niet kan betalen."
      ],
      antwoord: 0,
      uitleg: "Het **financieringstekort** is het begrotingstekort minus de aflossingen op de staatsschuld. Dit bedrag geeft aan hoeveel de schuld echt stijgt."
    },
    {
      type: "waaronwaar",
      vraag: "De staatsschuld stijgt in een jaar met een bedrag dat exact gelijk is aan het begrotingstekort.",
      antwoord: false,
      uitleg: "Onwaar. De staatsschuld stijgt met de omvang van het **financieringstekort** (omdat aflossingen de schuld verlagen, hoewel ze wel als uitgaven op de begroting staan)."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende belastingen is een indirecte belasting?",
      opties: [
        "Inkomstenbelasting",
        "Btw (omzetbelasting)",
        "Vennootschapsbelasting",
        "Erfbelasting"
      ],
      antwoord: 1,
      uitleg: "**Btw** is een indirecte belasting: je betaalt het via een omweg (de winkelier) bij de aankoop van goederen."
    },
    {
      type: "invul",
      vraag: "De belasting die bedrijven (zoals een bv of nv) betalen over de winst die zij maken heet _______belasting.",
      antwoord: "vennootschaps|vennootschapsbelasting",
      uitleg: "**Vennootschapsbelasting** is de inkomstenbelasting voor rechtspersonen (bedrijven)."
    },
    {
      type: "mc",
      vraag: "Waarom stelt de Europese Unie eisen aan de begrotingstekorten (max 3%) en staatsschulden (max 60%) van lidstaten?",
      opties: [
        "Om te zorgen dat de overheden van alle landen precies even groot worden.",
        "Om de waarde en stabiliteit van de gemeenschappelijke munt (de euro) te beschermen.",
        "Zodat landen geen wegen meer kunnen bouwen.",
        "Om het toerisme te stimuleren."
      ],
      antwoord: 1,
      uitleg: "Als één land in de eurozone failliet dreigt te gaan, kan dat de **stabiliteit van de euro** en andere Europese economieën in gevaar brengen."
    },
    {
      type: "waaronwaar",
      vraag: "De staatsschuldquote geeft de staatsschuld weer als percentage van het Bruto Binnenlands Product (BBP).",
      antwoord: true,
      uitleg: "Waar. De **staatsschuldquote** geeft een beter beeld van de ernst van de schuld dan het absolute bedrag in euro's."
    },
    {
      type: "mc",
      vraag: "Wat is het gevolg van een begrotingsoverschot voor de staatsschuld?",
      opties: [
        "De staatsschuld stijgt automatisch.",
        "De overheid kan hiermee de staatsschuld verlagen of aflossen.",
        "Het BBP daalt direct.",
        "De overheid moet direct geld lenen."
      ],
      antwoord: 1,
      uitleg: "Bij een **begrotingsoverschot** houdt de overheid geld over, waarmee ze schulden kan aflossen, wat de staatsschuld verlaagt."
    },
    {
      type: "open",
      vraag: "Leg uit hoe de vergrijzing van de bevolking (meer ouderen) leidt tot hogere uitgaven én lagere belastinginkomsten op de Rijksbegroting.",
      sleutelwoorden: ["meer AOW-uitkeringen", "hogere zorgkosten/zorguitgaven", "minder werkenden/krimp beroepsbevolking", "lagere loonbelasting/inkomstenbelasting"],
      minTreffers: 2,
      modelantwoord: "Vergrijzing betekent dat er meer ouderen komen, waardoor de uitgaven aan AOW-uitkeringen en medische zorg stijgen. Tegelijkertijd gaat een groter deel van de bevolking met pensioen, waardoor er minder werkenden zijn die inkomstenbelasting betalen. Hierdoor dalen de belastinginkomsten.",
      uitleg: "Meer uitgaven (AOW + zorg) en minder inkomsten (loonbelasting)."
    },
    {
      type: "open",
      vraag: "Berekening: De inkomsten van de overheid zijn € 300 miljard. De totale uitgaven (inclusief € 12 miljard aflossing op de staatsschuld) zijn € 310 miljard. Bereken het begrotingstekort en het financieringstekort en leg uit met hoeveel de staatsschuld stijgt.",
      sleutelwoorden: ["begrotingstekort is 10 miljard", "financieringstekort is 10 miljard min 12 miljard", "financieringstekort is -2 miljard/overschot van 2 miljard", "staatsschuld daalt met 2 miljard/stijgt niet"],
      minTreffers: 2,
      modelantwoord: "Het begrotingstekort is het verschil tussen inkomsten en uitgaven: € 310 miljard - € 300 miljard = € 10 miljard. Het financieringstekort is het begrotingstekort minus de aflossingen: € 10 miljard - € 12 miljard = -€ 2 miljard. Omdat het financieringstekort negatief is (-€ 2 miljard), stijgt de staatsschuld niet, maar daalt deze juist met € 2 miljard door de netto aflossing.",
      uitleg: "Begrotingstekort = € 10 miljard. Financieringstekort = -€ 2 miljard. De staatsschuld daalt met € 2 miljard."
    }
  ]
});
