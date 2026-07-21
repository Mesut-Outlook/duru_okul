/* Extra Proeftoets 2 — Belastingen & Subsidies (6.3) */
DURU.registerExamen({
  id: "ex-extra-belastingen-subsidies",
  titel: "Extra Proeftoets 2 — Belastingen & Subsidies",
  vak: "Economie · H6 (6.3)",
  icoon: "💸",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Welke belasting betaalt een naamloze vennootschap (nv) of besloten vennootschap (bv) over de gemaakte winst?",
      opties: [
        "Inkomstenbelasting",
        "Omzetbelasting",
        "Vennootschapsbelasting",
        "Accijns"
      ],
      antwoord: 2,
      uitleg: "Bedrijven (zoals nv's en bv's) betalen <b>vennootschapsbelasting</b> over hun winst. Burgers betalen inkomstenbelasting over hun loon."
    },
    {
      type: "mc",
      vraag: "Wat houdt een progressief belastingstelsel in?",
      opties: [
        "Iedereen betaalt precies hetzelfde percentage belasting.",
        "Mensen met een hoger inkomen betalen een hoger percentage belasting dan mensen met een lager inkomen.",
        "Alleen bedrijven betalen belasting, burgers betalen niets.",
        "De belastingpercentages dalen elk jaar."
      ],
      antwoord: 1,
      uitleg: "Bij een <b>progressief stelsel</b> stijgt het belastingtarief (percentage) naarmate het inkomen hoger wordt. Dit zorgt voor nivellering."
    },
    {
      type: "mc",
      vraag: "Welk btw-tarief betaal je in Nederland over basisgoederen zoals voedsel, boeken en de kapper?",
      opties: [
        "0%",
        "9%",
        "21%",
        "25%"
      ],
      antwoord: 1,
      uitleg: "Het verlaagde tarief van <b>9%</b> geldt voor eerste levensbehoeften (voedsel, kraanwater), boeken, medicijnen en sommige diensten (kapper, openbaar vervoer). Het standaardtarief is 21%."
    },
    {
      type: "mc",
      vraag: "Wat is het belangrijkste doel van motorrijtuigenbelasting (wegenbelasting)?",
      opties: [
        "Het stimuleren van de aankoop van dieselauto's.",
        "Geld ophalen om het openbaar vervoer gratis te maken.",
        "Betalen voor het onderhoud van de wegen en de invloed van verkeer op het milieu compenseren.",
        "Het subsidiëren van buitenlandse reizen."
      ],
      antwoord: 2,
      uitleg: "Wie een auto, motor of vrachtwagen bezit, betaalt <b>motorrijtuigenbelasting</b>. De overheid gebruikt dit geld voor wegenonderhoud en infrastructuur."
    },
    {
      type: "mc",
      vraag: "Hoe noemen we het als inkomensverschillen in verhouding kleiner worden door overheidsmaatregelen?",
      opties: [
        "Denivellering",
        "Nivellering",
        "Progressie",
        "Begrotingsdiscipline"
      ],
      antwoord: 1,
      uitleg: "<b>Nivellering</b> is het kleiner maken van inkomensverschillen (bijvoorbeeld door rijken meer belasting te laten betalen en toeslagen te geven aan lagere inkomens)."
    },
    {
      type: "waaronwaar",
      vraag: "Btw (Belasting over de Toegevoegde Waarde) is een voorbeeld van een directe belasting.",
      antwoord: false,
      uitleg: "Onwaar. <b>Btw</b> is een indirecte belasting (consumptiebelasting). Je betaalt het aan de winkelier, die het namens jou afdraagt aan de belastingdienst."
    },
    {
      type: "waaronwaar",
      vraag: "Accijns is bedoeld om de verkoop van schadelijke of milieuvervuilende goederen af te remmen.",
      antwoord: true,
      uitleg: "Waar. Met <b>accijns</b> maakt de overheid tabak, alcohol en brandstoffen duurder om het gebruik ervan te ontmoedigen."
    },
    {
      type: "invul",
      vraag: "Een financiële bijdrage van de overheid om gewenst gedrag (zoals het kopen van zonnepanelen) goedkoper te maken heet ______.",
      antwoord: "subsidie|een subsidie",
      uitleg: "De overheid geeft <b>subsidie</b> om positieve of milieuvriendelijke keuzes te stimuleren."
    },
    {
      type: "open",
      vraag: "Leg uit hoe een progressief belastingstelsel bijdraagt aan nivellering.",
      sleutelwoorden: ["hoger/hoog/meer/rijken", "percentage/procent/tarief", "verschil/verschillen/kleiner/gelijker"],
      minTreffers: 2,
      modelantwoord: "Bij progressieve belastingen betalen mensen met een hoog inkomen een hoger percentage belasting dan mensen met een laag inkomen. Hierdoor houden mensen met hoge inkomens relatief minder over en worden de inkomensverschillen na belastingbetaling kleiner (nivellering).",
      uitleg: "Doordat hoge inkomens procentueel meer afdragen, schuiven de netto inkomens dichter naar elkaar toe."
    },
    {
      type: "open",
      vraag: "Noem twee verschillende redenen waarom de overheid belastingen heft.",
      sleutelwoorden: ["geld/inkomsten/voorzieningen/betalen", "gedrag/sturen/ontmoedigen/accijns/subsidie", "inkomens/verschillen/nivelleren/nivellering"],
      minTreffers: 2,
      modelantwoord: "Ten eerste om inkomsten te verkrijgen waarmee de overheid collectieve voorzieningen (zoals scholen en wegen) kan betalen. Ten tweede om het gedrag van burgers te sturen, bijvoorbeeld door schadelijke producten duurder te maken met accijns.",
      uitleg: "Belastingen hebben een <b>financieringsfunctie</b> (geld ophalen) en een <b>sturingsfunctie</b> (gedrag beïnvloeden)."
    }
  ]
});
