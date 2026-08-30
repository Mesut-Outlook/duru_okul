/* Proeftoets 8 — Aardrijkskunde HAVO 3: Hoofdstuk 2 (Schatkist aarde?)
   Focus: Paragraaf 2.3 — Het gebruik van delfstoffen, ertsen, dagbouw vs schachtbouw, milieu-impact, Suriname (goud/kwik), Nigeria (aardolie in Nigerdelta).
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-ak-8",
  hoofdstuk: 2,
  hoofdstukTitel: "Hoofdstuk 2 — Schatkist aarde?",
  titel: "Toets 8 — Delfstoffen, Mijnbouw & Milieu (Suriname & Nigeria)",
  vak: "Aardrijkskunde · HAVO 3 (H2)",
  icoon: "🌍",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de definitie van een <b>delfstof</b>?",
      opties: [
        "Alle bruikbare gesteenten, ertsen en mineralen die uit de aardkorst worden gewonnen voor menselijk gebruik",
        "Uitsluitend landbouwgewassen die door boeren op akkers worden geoogst",
        "Diersoorten die in diepe grotten onder de grond leven",
        "Hout dat gekapt wordt in tropische regenwouden"
      ],
      antwoord: 0,
      uitleg: "Delfstoffen omvatten alle nuttige vaste, vloeibare en gasvormige stoffen die uit de aarde worden gehaald (metalen, mineralen, zand, grind, olie, gas)."
    },
    {
      type: "mc",
      vraag: "Wat is het verschil tussen <b>dagbouw</b> en <b>schachtbouw</b> in de mijnbouw?",
      opties: [
        "Dagbouw gebeurt alleen als de zon schijnt; schachtbouw alleen 's nachts",
        "Bij dagbouw worden delfstoffen in een open groeve aan het aardoppervlak afgegraven; bij schachtbouw worden ze via diepe ondergrondse mijngangen gewonnen",
        "Dagbouw is uitsluitend bedoeld voor vloeibare aardolie; schachtbouw voor drinkwater",
        "Bij dagbouw werken alleen robots; bij schachtbouw alleen machines"
      ],
      antwoord: 1,
      uitleg: "Dagbouw (open-pit mining) verwijdert de toplaag van het landschap voor ondiepe ertsen; schachtbouw graaft verticale schachten en horizontale gangen voor diepe lagen."
    },
    {
      type: "waaronwaar",
      vraag: "Een <b>erts</b> is een gesteente dat een economisch winbare concentratie van een bepaald metaal bevat (zoals bauxiet voor aluminium of ijzererts voor ijzer).",
      antwoord: true,
      uitleg: "Waar. Als het metaalgehalte in een gesteente hoog genoeg is om met winst te worden ontgonnen, spreekt men van een erts."
    },
    {
      type: "invul",
      vraag: "Welk zwaar giftig vloeibaar metaal wordt door illegale goudzoekers in Suriname gebruikt om kleine gouddeeltjes uit rivierzand aan elkaar te binden?",
      antwoord: "kwik|kwikzilver",
      uitleg: "Kwik vormt een amalgaam met goud. Bij verhitting verdampt het kwik, wat leidt tot ernstige zenuwvergiftiging en watervervuiling in het regenwoud."
    },
    {
      type: "mc",
      vraag: "Wat is een van de grootste milieuproblemen veroorzaakt door kleinschalige en illegale goudwinning in het binnenland van Suriname?",
      opties: [
        "Een massale toename van de hoeveelheid tropisch hardhout",
        "Het ontstaan van gigantische gletsjers in het oerwoud",
        "Ontbossing van het regenwoud, erosie van rivieroevers en zware kwikvergiftiging van viswater en drinkwater voor inheemse gemeenschappen",
        "Het volledig stilvallen van alle rivierstromingen door gebrek aan regen"
      ],
      antwoord: 2,
      uitleg: "Goudzoekers spuiten oevers kapot met waterkanonnen en lozen kwikhoudend slib direct in rivieren, waardoor vis en drinkwater giftig worden."
    },
    {
      type: "waaronwaar",
      vraag: "In de Nigerdelta in Nigeria heeft de grootschalige oliewinning door multinationals geleid tot ernstige bodem- en watervervuiling door lekkende pijpleidingen en fakkelen van gas.",
      antwoord: true,
      uitleg: "Waar. Olielozingen hebben mangrovebossen vernietigd, landbouwgronden onvruchtbaar gemaakt en visbestanden gedecimeerd in de Nigerdelta."
    },
    {
      type: "invul",
      vraag: "Welk aluminiumerts werd jarenlang op grote schaal gewonnen in Suriname rondom Moengo en Paranam?",
      antwoord: "bauxiet",
      uitleg: "Bauxiet is het belangrijkste erts waaruit aluminiumoxide en uiteindelijk zuiver aluminium metaal wordt geproduceerd."
    },
    {
      type: "mc",
      vraag: "Waarom zijn zogeheten <b>zeldzame aardmetalen</b> (zoals neodymium en dysprosium) en lithium van strategisch belang voor de toekomst?",
      opties: [
        "Ze kunnen gebruikt worden om gratis elektriciteit uit gewone stenen te persen",
        "Ze worden uitsluitend gebruikt als kleurstof in kinderspeelgoed",
        "Ze vervangen de behoefte aan drinkwater in steden",
        "Ze zijn onmisbaar voor de fabricage van windturbines, elektromotoren, batterijen en smartphones"
      ],
      antwoord: 3,
      uitleg: "De wereldwijde energietransitie en digitalisering steunen op sterke permanente magneten en accu's die zeldzame aardmetalen en lithium vereisen."
    },
    {
      type: "waaronwaar",
      vraag: "Omdat de aarde oneindig veel ertsen en fossiele brandstoffen aanmaakt per dag, is er geen enkel risico dat delfstoffen ooit opraken.",
      antwoord: false,
      uitleg: "Niet waar. Delfstoffen zijn niet-hernieuwbare hulpbronnen; het kostte de aarde honderden miljoenen jaren om ze te vormen, terwijl de mens ze in decennia opsoepeert."
    },
    {
      type: "mc",
      vraag: "Wat verstaat men onder <b>urban mining</b> (stedelijke mijnbouw)?",
      opties: [
        "Het terugwinnen en recyclen van waardevolle metalen uit afgedankte elektronica, kabels en sloopafval in steden",
        "Het graven van een diepe steenkoolschacht midden op de Dam in Amsterdam",
        "Het bouwen van flatgebouwen bovenop actieve vulkanen",
        "Het winnen van drinkwater uit de stadsriolering met behulp van zout"
      ],
      antwoord: 0,
      uitleg: "Urban mining haalt goud, zilver, koper en kobalt uit afgedankte e-waste (printplaten, telefoons), wat veel milieuvriendelijker is dan primaire mijnbouw."
    },
    {
      type: "invul",
      vraag: "Wat is de term voor een afvalbassin waarin giftig slib en fijngemalen gesteente na het chemisch scheiden van ertsen wordt opgeslagen?",
      antwoord: "tailingvijver|tailings dam|bezinkbassin|slibbekken",
      uitleg: "Tailings dammen bevatten vaak zware metalen en cyanide. Bij een dambreuk kan een dodelijke modderstroom hele dorpen en rivieren verwoesten."
    },
    {
      type: "waaronwaar",
      vraag: "Dagbouwmijnen laten vaak enorme gapende kraters achter in het landschap die het lokale ecosysteem en het grondwaterpeil blijvend verstoren.",
      antwoord: true,
      uitleg: "Waar. De gigantische afgravingen vernietigen bodemlagen, verlagen het grondwater en vereisen na sluiting kostbare herinrichting."
    },
    {
      type: "mc",
      vraag: "Wat is een belangrijke reden waarom veel westerse landen afhankelijk zijn van import voor kritieke grondstoffen?",
      opties: [
        "Omdat westerse landen wettelijk verboden hebben om metaal te gebruiken",
        "Veel kritieke mineralen komen in Europa niet in winbare concentraties voor, of de winning is wegens strenge milieueisen te duur",
        "Omdat de Europese bodem uitsluitend uit zuiver goud bestaat",
        "Omdat alle Europese mijnen al in de Romeinse tijd volledig zijn uitgeput"
      ],
      antwoord: 1,
      uitleg: "Concentraties van zeldzame aardmetalen en lithium bevinden zich vooral in China, Australië, Afrika en Zuid-Amerika; winning in Europa stuit bovendien op milieuprotest."
    },
    {
      type: "invul",
      vraag: "Welk land in Zuid-Amerika vormt samen met Chili en Argentinië de zogeheten 'lithiumdriehoek' in zoutvlaktes hoog in de Andes?",
      antwoord: "Bolivia",
      uitleg: "Bolivia beschikt op de Salar de Uyuni over gigantische voorraden lithiumpekel onder de uitgestrekte zoutkorst."
    },
    {
      type: "waaronwaar",
      vraag: "De winning van lithium uit zoutmeren in Zuid-Amerika vereist nauwelijks water en heeft geen enkele invloed op de watervoorziening van lokale boeren.",
      antwoord: false,
      uitleg: "Niet waar. Voor het verdampen van lithiumpekel worden miljarden liters water aan de extreem droge woestijnbodem onttrokken, wat leidt tot ernstige watertekorten."
    },
    {
      type: "mc",
      vraag: "Wat is een kenmerk van de zogeheten 'resource curse' in Nigeria rondom aardolie?",
      opties: [
        "Alle inwoners van Nigeria krijgen gratis een eigen olietanker cadeau",
        "Het land heeft door de olie geen enkele buitenlandse schuld meer",
        "Ondanks miljarden aan olie-inkomsten leeft de meerderheid van de bevolking in armoede door corruptie en milieuvernietiging",
        "Er is in Nigeria nog nooit een druppel olie uit de grond gehaald"
      ],
      antwoord: 2,
      uitleg: "De opbrengsten van de aardolie vloeien grotendeels weg naar de politieke elite en buitenlandse oliemaatschappijen, terwijl de lokale bevolking met de vervuiling blijft zitten."
    },
    {
      type: "waaronwaar",
      vraag: "In een circulaire economie worden grondstoffen zo ontworpen en hergebruikt dat er zo min mogelijk nieuwe primaire delfstoffen uit de aarde hoeven te worden gehaald.",
      antwoord: true,
      uitleg: "Waar. Een circulaire economie streeft naar gesloten kringlopen door recycling, reparatie en levensduurverlenging."
    },
    {
      type: "mc",
      vraag: "Welk metaal wordt het meest gerecycled ter wereld omdat het omsmelten 95% minder energie kost dan de productie uit bauxiet?",
      opties: [
        "Zand",
        "Kwik",
        "Steenkool",
        "Aluminium"
      ],
      antwoord: 3,
      uitleg: "Aluminium kan oneindig worden omgesmolten zonder kwaliteitsverlies, wat een enorme energie- en CO2-besparing oplevert ten opzichte van nieuw bauxiet."
    },
    {
      type: "open",
      vraag: "Vergelijk de milieugevolgen van de goudwinning in Suriname met de oliewinning in Nigeria.",
      sleutelwoorden: ["Suriname kwikvergiftiging/ontbossing", "Nigeria olielekkages/vervuilde mangroven", "water- en bodemverontreiniging"],
      minTreffers: 2,
      modelantwoord: "In Suriname leidt vooral illegale kleinschalige goudwinning tot grootschalige ontbossing van het regenwoud en zware kwikvergiftiging van rivieren en visbestanden. In Nigeria veroorzaakt de grootschalige oliewinning door lekkende leidingen en lozingen ernstige bodemvervuiling, vernietiging van kwetsbare mangrovebossen en vervuiling van viswateren in de dichtbevolkte Nigerdelta.",
      uitleg: "Suriname = ontbossing + kwik; Nigeria = olielozingen + vernietiging mangrove-ecosystemen."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de overgang naar duurzame energie (windmolens, elektrische auto's) leidt tot een verschuiving in de geopolitieke vraag naar delfstoffen.",
      sleutelwoorden: ["minder fossiele brandstoffen/olie en gas", "meer vraag naar kritieke metalen/lithium/kobalt", "afhankelijkheid van nieuwe exportlanden/China"],
      minTreffers: 2,
      modelantwoord: "Voor de energietransitie zijn veel minder fossiele brandstoffen (zoals aardolie en steenkool) nodig, maar juist gigantisch veel meer kritieke metalen zoals lithium, kobalt, koper en zeldzame aardmetalen voor accu's, windmolens en elektriciteitsnetten. Hierdoor verschuift de geopolitieke afhankelijkheid van traditionele oliestaten (in het Midden-Oosten) naar landen met grote metaalvoorraden en verwerkingscapaciteit (zoals China en Congo).",
      uitleg: "Fossiele afhankelijkheid maakt plaats voor kritieke metaalafhankelijkheid in de geopolitiek."
    }
  ]
});
