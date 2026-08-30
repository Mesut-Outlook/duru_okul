/* Onderwerp 1.2 — Wereldhandel: van kolonialisme tot nu
   buiteNLand 3 HAVO Hoofdstuk 1 */
DURU.register({
  id: "ak-h1-2",
  hoofdstuk: 1,
  paragraaf: "1.2",
  titel: "Wereldhandel: van kolonialisme tot nu",
  korteUitleg: "Handelskolonialisme, exploitatie vs vestiging, dekolonisatie en hedendaagse chipoorlog.",
  icoon: "⛵",
  kleur: "h1-thema",
  theorie: `
    <h3>1.2 Wereldhandel: van kolonialisme tot nu</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Handelskolonialisme, exploitatiekolonie, vestigingskolonie, dekolonisatie, neokolonialisme, chipoorlog.
    </div>
    <h4>1. Het ontstaan van een wereldeconomie</h4>
    <p>De wortels van de moderne wereldhandel liggen in het <b>handelskolonialisme</b> van de 16e tot 18e eeuw. Europese mogendheden stichtten handelscompagnieën (zoals de VOC en WIC in Nederland) en voeren over de wereldzeeën op zoek naar specerijen, suiker, koffie, tabak en goud. Zij stichtten handelsposten en plantages langs de kusten.</p>

    <h4>2. Twee typen kolonies</h4>
    <p>Historisch onderscheiden we twee hoofdtypen kolonies:</p>
    <ul>
      <li><b>Exploitatiekolonies:</b> Gebieden (zoals Indonesië, Suriname en grote delen van Afrika) die door het moederland puur als wingewest werden gebruikt. Lokale grondstoffen en arbeid werden geëxploiteerd ten gunste van Europa, terwijl de lokale bevolking weinig onderwijs of infrastructuur kreeg.</li>
      <li><b>Vestigingskolonies:</b> Gebieden (zoals de Verenigde Staten, Canada, Australië en Nieuw-Zeeland) waar Europeanen zich massaal en permanent vestigden. Zij bouwden steden, universiteiten en wetten op naar Europees model en legden de basis voor welvarende moderne centrumlanden.</li>
    </ul>

    <h4>3. Dekolonisatie en moderne handelsconflicten</h4>
    <p>Tussen 1945 en 1975 voltrok zich de <b>dekolonisatie</b>: koloniën werden zelfstandige staten. Desondanks bleven veel voormalige exploitatiekolonies economisch afhankelijk van het Westen.</p>
    <p>In de huidige wereld zien we nieuwe spanningen: de <b>chipoorlog</b> tussen de VS en China. Geavanceerde microchips zijn onmisbaar voor supercomputers en defensie. Westerse landen leggen strenge exportrestricties op aan geavanceerde chipmachines (zoals die van ASML) om technologisch en militair de leiding te behouden.</p>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Wat was het kenmerk van een <b>exploitatiekolonie</b>?",
      opties: [
        "Het gebied werd door het moederland gebruikt om ruwe grondstoffen te winnen voor de Europese markt",
        "Europese burgers gingen er massaal permanent wonen om het land op te bouwen",
        "Het land werd direct lid van de Europese Unie",
        "Er werden uitsluitend computers en auto's geproduceerd"
      ],
      antwoord: 0,
      uitleg: "In exploitatiekolonies stond economische uitbuiting van natuurlijke hulpbronnen centraal."
    },
    {
      type: "mc",
      vraag: "Welk land is een historisch voorbeeld van een <b>vestigingskolonie</b>?",
      opties: [
        "Suriname",
        "Australië",
        "Nederlands-Indië",
        "Congo"
      ],
      antwoord: 1,
      uitleg: "In Australië, Canada en de VS vestigden Europese kolonisten zich permanent en bouwden westerse samenlevingen op."
    },
    {
      type: "waaronwaar",
      vraag: "Tijdens de dekolonisatie (1945-1975) verloren Europese landen hun politieke heerschappij over overzeese koloniën.",
      antwoord: true,
      uitleg: "Waar. Tientallen landen in Azië en Afrika werden soevereine onafhankelijke staten."
    },
    {
      type: "invoer",
      vraag: "Welke Nederlandse handelscompagnie beheerste in de 17e en 18e eeuw de specerijenhandel in Azië?",
      antwoord: "VOC|Verenigde Oost-Indische Compagnie|de VOC",
      uitleg: "De VOC was de eerste beursgenoteerde multinational ter wereld."
    },
    {
      type: "mc",
      vraag: "Wat is de kern van de hedendaagse <b>chipoorlog</b>?",
      opties: [
        "Een tekort aan zand op de stranden van Californië",
        "Een militair gevecht tussen computerprogrammeurs in een datacenter",
        "De geopolitieke strijd tussen de VS en China om dominantie op het gebied van geavanceerde microchips en AI",
        "Een conflict over het vervoer van aardappelen per schip"
      ],
      antwoord: 2,
      uitleg: "De chipoorlog draait om technologische voorsprong en nationale veiligheid in de 21e eeuw."
    },
    {
      type: "waaronwaar",
      vraag: "Het Nederlandse bedrijf ASML mag zijn allernieuwste EUV-chipmachines onbeperkt en zonder enige exportvergunning aan Chinese staatsbedrijven verkopen.",
      antwoord: false,
      uitleg: "Niet waar. Nederland en de VS leggen strenge exportbeperkingen op om te voorkomen dat geavanceerde chiptechnologie in het Chinese leger belandt."
    },
    {
      type: "invoer",
      vraag: "Welke term beschrijft het verschijnsel dat voormalige koloniën na hun politieke onafhankelijkheid economisch toch sterk afhankelijk bleven van westerse multinationals?",
      antwoord: "neokolonialisme|neo-kolonialisme",
      uitleg: "Neokolonialisme wijst op blijvende economische overheersing zonder formele politieke bezetting."
    },
    {
      type: "mc",
      vraag: "Wat was een belangrijke stimulans voor het modern imperialisme in de 19e eeuw?",
      opties: [
        "De massale emigratie van alle Europeanen naar Antarctica",
        "De wens om alle fabrieken in Europa definitief af te breken",
        "Het verbod op het gebruik van stoommachines in Europa",
        "De Industriële Revolutie: fabrieken zochten grondstoffen (katoen, rubber, erts) en afzetmarkten"
      ],
      antwoord: 3,
      uitleg: "Europese fabrieken hadden een onstilbare honger naar grondstoffen en grote markten voor hun massaproducten."
    }
  ]
});
