/* Onderwerp 1.3 — Grondstoffen op de wereldmarkt
   buiteNLand 3 HAVO Hoofdstuk 1 */
DURU.register({
  id: "ak-h1-3",
  hoofdstuk: 1,
  paragraaf: "1.3",
  titel: "Grondstoffen op de wereldmarkt",
  korteUitleg: "Waardeketen, ruilvoetverslechtering, resource curse, Gini-coëfficiënt en SDG's.",
  icoon: "⛏️",
  kleur: "h1-thema",
  theorie: `
    <h3>1.3 Grondstoffen op de wereldmarkt</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Waardeketen (value chain), ruilvoetverslechtering, resource curse (grondstoffenvloek), Gini-coëfficiënt, SDG's, DR Congo vs VS.
    </div>
    <h4>1. De internationale waardeketen</h4>
    <p>Elk product doorloopt een <b>waardeketen</b>: van de winning van ruwe grondstoffen via verwerking, assemblage en transport tot aan de verkoop in winkels. Bij elke tussenstap wordt waarde toegevoegd. In de praktijk ontvangen de delvers van ruwe ertsen en boeren het allerkleinste deel van de opbrengst, terwijl hightech ontwerpers, merkhouders en verkopers de hoogste winsten boeken.</p>

    <h4>2. Ruilvoetverslechtering en de grondstoffenvloek</h4>
    <p>Veel ontwikkelingslanden hebben een <b>eenzijdige exportstructuur</b>: zij exporteren bijna uitsluitend onbewerkte delfstoffen of landbouwgewassen. Omdat de prijzen van hightech apparaten harder stijgen dan die van ruwe ertsen, treedt <b>ruilvoetverslechtering</b> op: het land moet steeds meer grondstoffen exporteren om dezelfde hoeveelheid machines te importeren.</p>
    <p>Bovendien kampen veel landen met de <b>grondstoffenvloek</b> (resource curse). Een overvloed aan kostbare grondstoffen leidt vaak tot corruptie, gewapende conflicten en verwaarlozing van onderwijs en landbouw. In de <b>Democratische Republiek Congo</b> (rijk aan kobalt en koper voor accu's) leven miljoenen mensen ondanks gigantische bodemschatten in bittere armoede.</p>

    <h4>3. Ongelijkheid en Duurzaamheidsdoelen</h4>
    <p>De <b>Gini-coëfficiënt</b> meet de inkomensongelijkheid in een land op een schaal van 0 (iedereen verdient exact evenveel) tot 1 (één persoon heeft alle inkomsten). Om wereldwijd armoede uit te bannen en eerlijke handel te bevorderen, hebben de VN 17 <b>Sustainable Development Goals (SDG's)</b> opgesteld voor 2030.</p>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Wat gebeurt er bij <b>ruilvoetverslechtering</b>?",
      opties: [
        "De prijzen van geïmporteerde industriegoederen stijgen sneller dan de opbrengsten van geëxporteerde ruwe grondstoffen",
        "Het geld van een land wordt automatisch verdubbeld door de bank",
        "Alle buitenlandse handel wordt wettelijk afgeschaft",
        "Grondstoffen worden gratis weggegeven aan buurlanden"
      ],
      antwoord: 0,
      uitleg: "Ruilvoetverslechtering holt de koopkracht van grondstofexporterende ontwikkelingslanden uit."
    },
    {
      type: "mc",
      vraag: "Welk metaal uit de DR Congo is essentieel voor batterijen in elektrische auto's?",
      opties: [
        "Graniet",
        "Kobalt",
        "Zand",
        "Krijt"
      ],
      antwoord: 1,
      uitleg: "Congo levert ruim 70% van het wereldwijde kobalt, een sleutelmineraal voor lithium-ion batterijen."
    },
    {
      type: "waaronwaar",
      vraag: "De Gini-coëfficiënt van een land is 0 als alle inwoners een exact gelijk inkomen hebben.",
      antwoord: true,
      uitleg: "Waar. 0 staat voor volkomen inkomensgelijkheid; 1 staat voor maximale ongelijkheid."
    },
    {
      type: "invoer",
      vraag: "Hoeveel Sustainable Development Goals (SDG's) hebben de Verenigde Naties vastgesteld voor 2030?",
      antwoord: "17|zeventien",
      uitleg: "De 17 doelen richten zich op welzijn, gelijkheid, klimaat en economische ontwikkeling."
    },
    {
      type: "mc",
      vraag: "Wat houdt de <b>grondstoffenvloek</b> (resource curse) in?",
      opties: [
        "Een vloek die door archeologen over oude piramides is uitgesproken",
        "Alle grondstoffen in de bodem verdwijnen als je ernaar kijkt",
        "Landen met veel bodemschatten hebben paradoxaal genoeg vaak meer corruptie, burgeroorlogen en armoede",
        "Het verplicht moeten opeten van alle gedolven metalen"
      ],
      antwoord: 2,
      uitleg: "Grote grondstofrijkdom leidt bij zwakke instituties tot machtsstrijd en verwaarlozing van de bredere economie."
    },
    {
      type: "waaronwaar",
      vraag: "De Verenigde Staten exporteren jaarlijks voor meer dan $200 miljard aan landbouwproducten, dankzij een hoogontwikkelde en gemechaniseerde agrarische sector.",
      antwoord: true,
      uitleg: "Waar. De VS zijn de grootste agrarische exporteur ter wereld."
    },
    {
      type: "invoer",
      vraag: "Hoe noem je alle opeenvolgende stappen die een product doorloopt van grondstof tot eindgebruiker, waarbij telkens waarde wordt toegevoegd?",
      antwoord: "waardeketen|value chain|de waardeketen",
      uitleg: "De waardeketen omvat winning, raffinage, productie, transport, marketing en verkoop."
    },
    {
      type: "mc",
      vraag: "Waarom is kinderarbeid in artisanale kobaltmijnen in Congo een ernstig probleem in de wereldhandel?",
      opties: [
        "Er werken helemaal geen kinderen in Afrikaanse mijnen",
        "Omdat kinderen sneller kunnen programmeren dan volwassenen",
        "Omdat kinderen te veel belasting moeten betalen over hun salaris",
        "Het schendt fundamentele mensenrechten en leidt tot levensgevaarlijke omstandigheden voor kinderen in de mijnbouw"
      ],
      antwoord: 3,
      uitleg: "Internationale bedrijven staan onder zware maatschappelijke druk om kinderarbeid en conflictmineralen uit hun toeleveringsketens te bannen."
    }
  ]
});
