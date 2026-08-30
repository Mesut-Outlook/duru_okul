/* Onderwerp 1.1 — Kantelt het economisch wereldbeeld?
   buiteNLand 3 HAVO Hoofdstuk 1 */
DURU.register({
  id: "ak-h1-1",
  hoofdstuk: 1,
  paragraaf: "1.1",
  titel: "Kantelt het economisch wereldbeeld?",
  korteUitleg: "Multipolaire wereldeconomie, global shift, centrum-semiperiferie en Big Tech.",
  icoon: "🌐",
  kleur: "h1-thema",
  theorie: `
    <h3>1.1 Kantelt het economisch wereldbeeld?</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Global shift, multipolaire wereldeconomie, Triade, Big Tech, centrum-semiperiferie-periferie, vrijhandel vs protectionisme.
    </div>
    <h4>1. De verschuiving van economische macht</h4>
    <p>Decennialang werd de wereldeconomie gedomineerd door de traditionele <b>Triade</b>: Noord-Amerika (de VS), West-Europa en Oost-Azië (Japan). Deze drie regio's vormden het rijke economische centrum van de wereld. Sinds het begin van de 21e eeuw zien we echter een duidelijke <b>global shift</b>: het economische en industriële zwaartepunt verschuift in hoog tempo naar opkomende economieën in Azië, met name <b>China</b> en <b>India</b>.</p>
    <p>Hierdoor leven we tegenwoordig in een <b>multipolaire wereldeconomie</b>. Dit betekent dat er niet meer één of twee dominante mogendheden zijn, maar meerdere gelijkwaardige economische machtscentra verspreid over de aardbol.</p>

    <h4>2. Het centrum-semiperiferie-periferiemodel</h4>
    <p>Om de economische verschillen en de wereldwijde arbeidsverdeling te begrijpen, gebruiken geografen het driedelige model:</p>
    <ul>
      <li><b>Centrumlanden:</b> Rijke, hoogontwikkelde kenniseconomieën (zoals Nederland, Duitsland, de VS en Japan) met een hoge koopkracht, hoogwaardige technologie, R&D en hoofdkantoren van multinationals.</li>
      <li><b>Semiperiferielanden:</b> Snelgroeiende, industrialiserende economieën (zoals China, Brazilië, Mexico en India). Zij combineren lage loonkosten met moderne fabrieken en een groeiende middenklasse.</li>
      <li><b>Periferielanden:</b> Economisch achterblijvende landen (vooral in Afrika bezuiden de Sahara en delen van Zuid-Azië) die voornamelijk afhankelijk zijn van de export van onbewerkte landbouwproducten en ruwe delfstoffen.</li>
    </ul>

    <h4>3. De opkomst van Big Tech en data</h4>
    <p>Waar de traditionele economie draaide om fabrieken en fysieke containers, wordt de 21e-eeuwse economie in toenemende mate gedomineerd door <b>Big Tech-bedrijven</b> (zoals Google, Apple, Microsoft, Amazon en Meta). Deze bedrijven verdienen hun miljarden met het verzamelen, analyseren en verkopen van data en digitale platforms. Data fungeert als de 'nieuwe aardolie' van de wereldeconomie.</p>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Wat betekent de term <b>global shift</b>?",
      opties: [
        "Het verschuiven van het economische zwaartepunt van het Westen naar opkomende regio's in Azië",
        "Het wereldwijd verdwijnen van alle fabrieken",
        "De invoering van één wereldwijde munt",
        "Het sluiten van alle internationale grenzen"
      ],
      antwoord: 0,
      uitleg: "Global shift beschrijft de verplaatsing van industriële productie en economische groei naar Aziatische landen zoals China en India."
    },
    {
      type: "mc",
      vraag: "Uit welke drie regio's bestond de historische <b>Triade</b>?",
      opties: [
        "Afrika, Zuid-Amerika en Australië",
        "Noord-Amerika, West-Europa en Japan/Oost-Azië",
        "Rusland, China en India",
        "Brazilië, Egypte en Canada"
      ],
      antwoord: 1,
      uitleg: "De Triade omvatte de drie traditionele rijke machtsblokken van de 20e eeuw."
    },
    {
      type: "waaronwaar",
      vraag: "Een multipolaire wereldeconomie betekent dat er slechts één enkel land is dat alle beslissingen in de wereldhandel neemt.",
      antwoord: false,
      uitleg: "Niet waar. Multipolair betekent dat er meerdere economische en politieke zwaartepunten naast elkaar bestaan."
    },
    {
      type: "invoer",
      vraag: "Welke term gebruikt men voor grote tech-bedrijven zoals Alphabet, Apple en Amazon die miljarden verdienen met online data?",
      antwoord: "big tech|big tech-bedrijven|big tech bedrijven",
      uitleg: "Big Tech-bedrijven hebben enorme controle over informatie, communicatie en e-commerce."
    },
    {
      type: "mc",
      vraag: "Wat kenmerkt een land in de <b>semiperiferie</b>?",
      opties: [
        "Het hoogste inkomen ter wereld zonder fabrieken",
        "Uitsluitend export van bananen zonder enige fabriek",
        "Snelle industrialisatie, economische groei en stijgende inkomens",
        "Een verbod op buitenlandse handel"
      ],
      antwoord: 2,
      uitleg: "Semiperiferielanden zitten in de overgangsfase en vormen de opkomende industriële werkplaatsen van de wereld."
    },
    {
      type: "waaronwaar",
      vraag: "China heeft zich in enkele decennia ontwikkeld van een arm ontwikkelingsland tot een van de grootste industriële wereldmachten.",
      antwoord: true,
      uitleg: "Waar. Door hervormingen en speciale economische zones werd China de tweede economie ter wereld."
    },
    {
      type: "invoer",
      vraag: "Hoe noem je het economische beleid waarbij een regering invoerrechten heft om de eigen binnenlandse producenten te beschermen?",
      antwoord: "protectionisme|protectie",
      uitleg: "Protectionisme schermt de binnenlandse markt af voor buitenlandse concurrenten."
    },
    {
      type: "mc",
      vraag: "Waarom is online data tegenwoordig van onschatbare waarde voor bedrijven?",
      opties: [
        "Data heeft economisch gezien helemaal geen enkele waarde",
        "Omdat data fysiek als brandstof in verbrandingsmotoren kan worden gestopt",
        "Omdat data ervoor zorgt dat zeecontainers sneller varen",
        "Bedrijven kunnen hiermee consumentengedrag voorspellen, gepersonaliseerde advertenties verkopen en AI trainen"
      ],
      antwoord: 3,
      uitleg: "Data stelt bedrijven in staat om marketing hypergericht in te zetten en algoritmes te perfectioneren."
    }
  ]
});
