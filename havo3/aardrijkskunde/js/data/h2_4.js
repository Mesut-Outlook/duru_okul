/* Onderwerp 2.4 — Delfstoffen in Europa
   buiteNLand 3 HAVO Hoofdstuk 2 */
DURU.register({
  id: "ak-h2-4",
  hoofdstuk: 2,
  paragraaf: "2.4",
  titel: "Delfstoffen in Europa",
  korteUitleg: "Delfstoffen in Europa, bruinkool in Duitsland, ijzererts in Kiruna (Zweden) en importafhankelijkheid.",
  icoon: "⛏️",
  kleur: "h2-thema",
  theorie: `
    <h3>2.4 Delfstoffen in Europa</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Bruinkool in Duitsland (dagbouw), steenkool in Polen (Silezië), ijzererts in Kiruna (Zweden), importafhankelijkheid, strategische autonomie, Critical Raw Materials Act.
    </div>
    <h4>1. Delfstoffen op Europese bodem</h4>
    <p>Hoewel Europa over belangrijke delfstoffen beschikt, zijn de voorraden zeer ongelijk verdeeld:</p>
    <ul>
      <li><b>Duitsland:</b> Grootste producent van <b>bruinkool</b> ter wereld. In enorme dagbouwgroeven (zoals Garzweiler) graven reusachtige graafwielbaggers complete landschappen af voor elektriciteitscentrales.</li>
      <li><b>Polen:</b> Haalt veel energie uit <b>steenkool</b> uit het Silezische bekken.</li>
      <li><b>Zweden (Kiruna):</b> Herbergt de grootste en modernste ondergrondse <b>ijzerertsmijn</b> ter wereld. Omdat de mijngangen onder de stad doorlopen, moet de stad Kiruna letterlijk worden verplaatst wegens verzakkingsgevaar.</li>
      <li><b>Noordzee:</b> Aardolie en aardgasvelden geëxploiteerd door Noorwegen en het VK.</li>
    </ul>

    <h4>2. Importafhankelijkheid en de energietransitie</h4>
    <p>Europa is voor het merendeel van zijn metalen en zeldzame aardmetalen <b>afhankelijk van import</b> (China levert ruim 90% van de zeldzame aardmetalen). Voor de energietransitie (windmolens, elektrische auto's) zijn gigantische hoeveelheden lithium, kobalt en koper nodig. Met de <i>Critical Raw Materials Act</i> stimuleert de EU eigen mijnbouw, diversificatie van importeurs en kringloopeconomie.</p>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Welke fossiele brandstof wordt in Duitsland op grote schaal in dagbouwmijnen gewonnen?",
      opties: [
        "Bruinkool",
        "Goud",
        "Diamant",
        "Aardgas"
      ],
      antwoord: 0,
      uitleg: "Duitsland wint veel bruinkool in dagbouwgroeven in het Rijnland en de Lausitz."
    },
    {
      type: "mc",
      vraag: "Waarom moet de Zweedse stad <b>Kiruna</b> voor een deel verplaatst worden?",
      opties: [
        "Wegens een dreigende vulkaanuitbarsting",
        "Door ondergrondse ijzerertsmijnbouw ontstaan scheuren en verzakkingen onder het stadscentrum",
        "Omdat de stad overstroomd wordt door zeewater",
        "Omdat de bewoners liever op een eiland willen wonen"
      ],
      antwoord: 1,
      uitleg: "De uitbreiding van de LKAB-ijzerertsmijn veroorzaakt instortingsgevaar in de bovengelegen stad."
    },
    {
      type: "waaronwaar",
      vraag: "Europa is voor meer dan 90% afhankelijk van import voor zeldzame aardmetalen die nodig zijn in windturbines en telefoons.",
      antwoord: true,
      uitleg: "Waar. China domineert de wereldwijde keten van zeldzame aardmetalen."
    },
    {
      type: "invoer",
      vraag: "In welk Midden-Europees land wordt in de regio Silezië nog veel steenkool gedolven voor de energievoorziening?",
      antwoord: "Polen",
      uitleg: "Polen steunt traditioneel zwaar op steenkoolcentrales voor elektriciteit."
    },
    {
      type: "mc",
      vraag: "Wat is het doel van de Europese <b>Critical Raw Materials Act</b>?",
      opties: [
        "Het verplicht stellen van steenkool in alle huishoudens",
        "Het verbieden van alle elektrische apparaten in de EU",
        "De Europese afhankelijkheid van buitenlandse grondstoffen verkleinen door eigen mijnbouw, partnerschappen en recycling",
        "Het heffen van 100% belasting op zonnepanelen"
      ],
      antwoord: 2,
      uitleg: "De wet waarborgt de strategische autonomie van Europa voor kritieke materialen."
    },
    {
      type: "waaronwaar",
      vraag: "Het winnen van delfstoffen in Europa is altijd goedkoper dan importeren uit Zuid-Amerika of Azië.",
      antwoord: false,
      uitleg: "Niet waar. Hoge lonen en strenge milieunormen maken Europese winning vaak duurder dan import."
    },
    {
      type: "invoer",
      vraag: "Welk oeroud, stabiel en ertsrijk geologisch schild ligt in Scandinavië en Finland aan de oppervlakte?",
      antwoord: "Baltisch Schild|het Baltisch Schild|Baltische schild",
      uitleg: "Het Baltisch Schild bevat oeroude Precambrische gesteenten vol waardevolle metaalertsen."
    },
    {
      type: "mc",
      vraag: "Wat is het <b>NIMBY-effect</b> (Not In My Back Yard) bij het openen van nieuwe Europese mijnen?",
      opties: [
        "Een subsidie voor het planten van bloemen bij mijnschachten",
        "Iedereen wil graag een eigen goudmijn in zijn achtertuin graven",
        "Een verbod op het hebben van een achtertuin in heel Europa",
        "Mensen begrijpen dat grondstoffen nodig zijn, maar willen geen vervuilende mijn in hun eigen woonomgeving"
      ],
      antwoord: 3,
      uitleg: "Omwonenden vrezen geluidsoverlast en watervervuiling, wat leidt tot fel protest tegen nieuwe mijnbouw."
    }
  ]
});
