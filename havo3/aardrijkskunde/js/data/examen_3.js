/* Proeftoets 3 — Aardrijkskunde HAVO 3: Hoofdstuk 1 (Wereldhandel in beweging)
   Focus: Paragraaf 1.3 — Grondstoffen op de wereldmarkt, waardeketen, ruilvoetverslechtering, resource curse, Gini-coëfficiënt, SDG's, DR Congo vs VS.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-ak-3",
  hoofdstuk: 1,
  hoofdstukTitel: "Hoofdstuk 1 — Wereldhandel in beweging",
  titel: "Toets 3 — Grondstoffen, Waardeketen & DR Congo vs VS",
  vak: "Aardrijkskunde · HAVO 3 (H1)",
  icoon: "⛏️",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat wordt bedoeld met de <b>waardeketen</b> (value chain) van een product?",
      opties: [
        "Alle opeenvolgende stappen van grondstofwinning, verwerking, transport tot verkoop waarbij telkens waarde wordt toegevoegd",
        "De ketting waarmee zeecontainers op een vrachtschip worden vastgezet",
        "De totale lijst van alle winkelprijzen in één specifiek warenhuis",
        "Het verplichte keurmerk dat aangeeft dat een product van goud is gemaakt"
      ],
      antwoord: 0,
      uitleg: "In de waardeketen wordt bij elke stap (ontwerp, raffinage, assemblage, marketing, verkoop) extra waarde en winstmarge toegevoegd aan het oorspronkelijke ruwe materiaal."
    },
    {
      type: "mc",
      vraag: "In welke fase van de waardeketen wordt over het algemeen de <b>laagste winstmarge</b> behaald?",
      opties: [
        "Bij het ontwerpen van de software in Silicon Valley",
        "Bij de winning van de ruwe grondstoffen in de mijnbouw of landbouw",
        "Bij de wereldwijde marketingcampagne en merkreclame",
        "Bij de uiteindelijke verkoop van het eindproduct aan consumenten"
      ],
      antwoord: 1,
      uitleg: "Het winnen van ruwe delfstoffen en agrarische grondstoffen levert relatief weinig op; het meeste geld wordt verdiend met hightech verwerking, merkontwikkeling en retail."
    },
    {
      type: "waaronwaar",
      vraag: "<b>Ruilvoetverslechtering</b> betekent dat een land steeds meer ruwe grondstoffen moet exporteren om dezelfde hoeveelheid geïmporteerde industrieproducten te kunnen betalen.",
      antwoord: true,
      uitleg: "Waar. Omdat de prijzen van hightech eindproducten harder stijgen dan die van onbewerkte grondstoffen, verslechtert de ruilvoet voor grondstofafhankelijke landen."
    },
    {
      type: "invul",
      vraag: "Welke economische term beschrijft het paradoxale fenomeen dat landen met een enorme rijkdom aan bodemschatten vaak kampen met corruptie, armoede en trage economische groei?",
      antwoord: "grondstoffenvloek|resource curse|de grondstoffenvloek|paradox of plenty",
      uitleg: "De grondstoffenvloek (resource curse) verklaart waarom overvloed aan ertsen of olie vaak leidt tot burgeroorlogen en economische verwaarlozing van andere sectoren."
    },
    {
      type: "mc",
      vraag: "Voor welk cruciaal mineraal, dat onmisbaar is in de accu's van elektrische auto's en smartphones, is de Democratische Republiek Congo de grootste producent ter wereld?",
      opties: [
        "Kiezelsteen",
        "Zout",
        "Kobalt",
        "Graniet"
      ],
      antwoord: 2,
      uitleg: "Meer dan 70% van de wereldwijde kobaltwinning vindt plaats in de DR Congo. Kobalt is een essentieel bestanddeel van lithium-ion-accu's."
    },
    {
      type: "waaronwaar",
      vraag: "In de Democratische Republiek Congo profiteert de gehele bevolking gelijkmatig van de miljardenopbrengsten uit de koper- en kobaltmijnen.",
      antwoord: false,
      uitleg: "Niet waar. Een groot deel van de opbrengsten verdwijnt naar corrupte elites, gewapende milities en buitenlandse mijnbouwreuzen, terwijl veel mijnwerkers in extreme armoede leven."
    },
    {
      type: "invul",
      vraag: "Wat meet de <b>Gini-coëfficiënt</b> (een getal tussen 0 en 1) in een land?",
      antwoord: "inkomensongelijkheid|ongelijkheid|de inkomensongelijkheid|vermogensongelijkheid",
      uitleg: "De Gini-coëfficiënt geeft de mate van inkomensongelijkheid weer: 0 betekent volkomen gelijkheid (iedereen verdient evenveel) en 1 betekent maximale ongelijkheid."
    },
    {
      type: "mc",
      vraag: "Welke bewering over de landbouwexport van de Verenigde Staten is juist?",
      opties: [
        "De Amerikaanse landbouw maakt geen gebruik van machines of kunstmest",
        "De VS importeren al hun voedsel omdat er in Noord-Amerika geen akkerbouw mogelijk is",
        "De agrarische export van de VS bestaat voor 100% uit tropische cacaobonen",
        "De VS zijn de grootste landbouwexporteur ter wereld met meer dan $200 miljard aan agrarische export, hoewel dit maar een klein deel van hun totale BBP vormt"
      ],
      antwoord: 3,
      uitleg: "De VS hebben een hoogontwikkelde, kapitaalintensieve landbouwsector die enorme volumes maïs, soja, graan en vlees wereldwijd exporteert."
    },
    {
      type: "waaronwaar",
      vraag: "De 17 Sustainable Development Goals (SDG's) zijn door de Verenigde Naties opgesteld om armoede te bestrijden, ongelijkheid te verminderen en het klimaat te beschermen.",
      antwoord: true,
      uitleg: "Waar. De SDG's (duurzame ontwikkelingsdoelen) vormen het internationale kompas voor duurzame wereldwijde ontwikkeling richting 2030."
    },
    {
      type: "mc",
      vraag: "Wat is een kenmerk van een <b>eenzijdige exportstructuur</b> in een ontwikkelingsland?",
      opties: [
        "De inkomsten van het land zijn voor meer dan 80% afhankelijk van slechts één of twee ruwe delfstoffen of landbouwgewassen",
        "Het land exporteert exact evenveel software, vliegtuigen, medicijnen als kleding",
        "Het land heeft handelsovereenkomsten met alle 193 landen van de Verenigde Naties",
        "Er worden uitsluitend goederen geïmporteerd en helemaal niets geëxporteerd"
      ],
      antwoord: 0,
      uitleg: "Monocultuur of eenzijdige export maakt een land extreem kwetsbaar voor prijsschommelingen op de wereldmarkt."
    },
    {
      type: "invul",
      vraag: "Hoeveel Sustainable Development Goals (SDG's / Duurzame Ontwikkelingsdoelen) heeft de VN vastgesteld voor het jaar 2030?",
      antwoord: "17|zeventien",
      uitleg: "Er zijn precies 17 SDG's die uiteenlopen van armoedebestrijding en goed onderwijs tot schoon water en klimaatactie."
    },
    {
      type: "waaronwaar",
      vraag: "Een land met een Gini-coëfficiënt van 0,65 heeft een veel gelijkmatigere inkomensverdeling dan een land met een Gini-coëfficiënt van 0,25.",
      antwoord: false,
      uitleg: "Niet waar. Hoe hoger het getal (dichter bij 1), des te groter is de ongelijkheid. Een score van 0,25 wijst op grote gelijkheid (zoals in Scandinavië)."
    },
    {
      type: "mc",
      vraag: "Waarom hebben veel kleinschalige mijnwerkers in de artisanale mijnbouw in Afrika te maken met gevaarlijke en ongezonde werkomstandigheden?",
      opties: [
        "Zij werken uitsluitend in geautomatiseerde, geklimatiseerde kantoorgebouwen",
        "Er is gebrek aan beschermende kleding, tunnels kunnen instorten en er worden giftige stoffen zonder toezicht gebruikt",
        "De overheid verplicht alle mijnwerkers om maximaal 2 uur per dag te werken",
        "Mijnbouw levert nergens ter wereld enig gezondheidsrisico op"
      ],
      antwoord: 1,
      uitleg: "Kleinschalige en illegale mijnbouw ontbeert veiligheidsmaatregelen, wat leidt tot instortingen, stoflongen en blootstelling aan chemicaliën."
    },
    {
      type: "invul",
      vraag: "Wat is de afkorting voor het Bruto Binnenlands Product, de totale geldwaarde van alle goederen en diensten die in een land in één jaar worden geproduceerd?",
      antwoord: "BBP|bbp|GDP|gdp",
      uitleg: "Het BBP (Bruto Binnenlands Product / Engels: GDP) is de belangrijkste graadmeter voor de economische omvang van een land."
    },
    {
      type: "waaronwaar",
      vraag: "Fairtrade-keurmerken en duurzame toeleveringsketens hebben als doel boeren en mijnwerkers in ontwikkelingslanden een eerlijke prijs en veilige werkomstandigheden te garanderen.",
      antwoord: true,
      uitleg: "Waar. Eerlijke handel streeft naar transparantie, leefbare inkomens en het uitbannen van kinderarbeid in de productieketen."
    },
    {
      type: "mc",
      vraag: "Wat is het gevolg voor een Afrikaans land wanneer de wereldmarktprijs van zijn belangrijkste exportmetaal plotseling met 50% instort?",
      opties: [
        "Alle buitenlandse schulden van het land worden automatisch kwijtgescholden",
        "Het land wordt direct het rijkste land van het continent",
        "De staatsinkomsten dalen drastisch, waardoor de overheid moet bezuinigen op scholen, ziekenhuizen en infrastructuur",
        "De binnenlandse werkloosheid verdwijnt onmiddellijk"
      ],
      antwoord: 2,
      uitleg: "Grondstofafhankelijke landen worden bij een prijsval geconfronteerd met grote begrotingstekorten en economische crises."
    },
    {
      type: "waaronwaar",
      vraag: "In de internationale waardeketen van een smartphone gaat het grootste deel van de uiteindelijke verkoopprijs naar de mijnwerker die het kobalt en koper opgraaft.",
      antwoord: false,
      uitleg: "Niet waar. De grondstofdelvers ontvangen slechts fracties van een procent; het merendeel van de opbrengst gaat naar tech-ontwikkelaars, merkhouders en distributeurs."
    },
    {
      type: "mc",
      vraag: "Welke SDG van de Verenigde Naties richt zich specifiek op het beëindigen van extreme armoede overal ter wereld?",
      opties: [
        "SDG 11: Duurzame steden en gemeenschappen",
        "SDG 14: Leven in het water",
        "SDG 7: Betaalbare en duurzame energie",
        "SDG 1: Geen armoede"
      ],
      antwoord: 3,
      uitleg: "SDG 1 stelt als hoofddoel om tegen 2030 een einde te maken aan extreme armoede en ervoor te zorgen dat iedereen toegang heeft tot basisbehoeften."
    },
    {
      type: "open",
      vraag: "Leg uit waarom het voor een land als DR Congo moeilijk is om te ontsnappen aan de grondstoffenvloek, ondanks een gigantische rijkdom aan kobalt en koper.",
      sleutelwoorden: ["corruptie/milities", "ruilvoetverslechtering/weinig verwerking", "buitenlandse multinationals/geen welvaartsverdeling"],
      minTreffers: 2,
      modelantwoord: "DR Congo exporteert vooral onbewerkte ertsen waar weinig toegevoegde waarde op zit. De opbrengsten komen vaak terecht bij corrupte leiders, gewapende milities en buitenlandse multinationals in plaats van de bevolking. Omdat het land nauwelijks eigen verwerkende fabrieken, infrastructuur of een stabiele rechtsstaat heeft, blijft de lokale economie kwetsbaar en arm.",
      uitleg: "Ontbreken van verwerkende industrie, zwakke instituties en oneerlijke verdeling bestendigen de grondstoffenvloek."
    },
    {
      type: "open",
      vraag: "Vergelijk de waardeketen van een agrarisch product uit de VS met de export van ruwe mineralen uit een ontwikkelingsland.",
      sleutelwoorden: ["hightech/mechanisatie/subsidies in VS", "onbewerkt/handwerk in ontwikkelingsland", "hoge toegevoegde waarde/kennis"],
      minTreffers: 2,
      modelantwoord: "De agrarische sector in de VS is sterk gemechaniseerd, gesubsidieerd en gekoppeld aan geavanceerde voedselverwerkende multinationals die merkproducten met hoge winstmarges wereldwijd afzetten. In een ontwikkelingsland wordt het mineraal vaak met de hand gedolven en onbewerkt geëxporteerd, waardoor de lokale economie de hoge winsten uit latere raffinage en chipfabricage misloopt.",
      uitleg: "Mechanisatie, industriële verwerking en merkkracht bepalen het verschil in economische opbrengst in de keten."
    }
  ]
});
