/* Onderwerp 1.5 — Rol van Nederland in de wereldhandel
   buiteNLand 3 HAVO Hoofdstuk 1 */
DURU.register({
  id: "ak-h1-5",
  hoofdstuk: 1,
  paragraaf: "1.5",
  titel: "Rol van Nederland in de wereldhandel",
  korteUitleg: "Nederland distributieland, mainports (Rotterdam, Schiphol), Brainport Eindhoven en wederuitvoer.",
  icoon: "🚢",
  kleur: "h1-thema",
  theorie: `
    <h3>1.5 Rol van Nederland in de wereldhandel</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Distributieland, Gateway to Europe, mainports (Haven van Rotterdam, Schiphol), Brainport Eindhoven, ASML, doorvoer vs wederuitvoer, KOF Globaliseringsindex.
    </div>
    <h4>1. Nederland als logistiek knooppunt</h4>
    <p>Nederland is een van de meest open en internationaal georiënteerde economieën ter wereld. Volgens de <b>KOF Globaliseringsindex</b> staat Nederland consequent in de wereldwijde top drie. Dankzij de strategische ligging aan de Noordzee en de monding van de Rijn en Maas fungeert Nederland als de <b>Gateway to Europe</b>.</p>
    <p>Nederland beschikt over twee cruciale <b>mainports</b>:</p>
    <ul>
      <li><b>Haven van Rotterdam:</b> De grootste zeehaven van Europa. Gigantische containerschepen meren aan bij de Maasvlakte 2. Via binnenvaartschepen over de Rijn en goederentreinen over de <b>Betuweroute</b> worden grondstoffen en consumentengoederen razendsnel doorgevoerd naar het Europese achterland (vooral Duitsland).</li>
      <li><b>Luchthaven Schiphol:</b> Een van de belangrijkste Europese luchthavens voor internationaal passagiers- en vrachtvervoer.</li>
    </ul>

    <h4>2. Wederuitvoer en Brainport Eindhoven</h4>
    <p>We maken onderscheid tussen:</p>
    <ul>
      <li><b>Doorvoer (transit):</b> Goederen reizen direct door zonder eigendomsoverdracht; Nederland verdient alleen aan overslag en transport.</li>
      <li><b>Wederuitvoer:</b> Buitenlandse goederen worden tijdelijk eigendom van een Nederlands bedrijf, opgeslagen, gekeurd of licht bewerkt en daarna met winst geëxporteerd. Dit levert aanzienlijk meer toegevoegde waarde op.</li>
    </ul>
    <p>Naast logistiek blinkt Nederland uit in de kenniseconomie: <b>Brainport Eindhoven</b> is de mondiale hotspot voor hightech chipmachines (ASML), waar topbedrijven, de TU Eindhoven en onderzoekers nauw samenwerken.</p>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Waarom staat Nederland bekend als 'Gateway to Europe'?",
      opties: [
        "Dankzij de strategische ligging aan zee met grote mainports en uitstekende verbindingen naar het Europese achterland",
        "Omdat Nederland het grootste landoppervlak van Europa heeft",
        "Omdat alle Europese wetten in Amsterdam worden geschreven",
        "Omdat Nederland geen enkel buitenlands product toelaat"
      ],
      antwoord: 0,
      uitleg: "De ligging en infrastructuur maken Nederland het belangrijkste doorvoerland van Europa."
    },
    {
      type: "mc",
      vraag: "Wat zijn de twee Nederlandse <b>mainports</b>?",
      opties: [
        "De haven van Enkhuizen en station Utrecht",
        "De Haven van Rotterdam en Luchthaven Schiphol",
        "Vliegveld Eelde en de haven van Terschelling",
        "De Afsluitdijk en de Zeelandbrug"
      ],
      antwoord: 1,
      uitleg: "Rotterdam (zeevaart) en Schiphol (luchtvaart) zijn de twee officiële logistieke mainports."
    },
    {
      type: "waaronwaar",
      vraag: "Bij wederuitvoer worden ingevoerde goederen tijdelijk eigendom van een Nederlands bedrijf voordat ze worden doorverkocht aan het buitenland.",
      antwoord: true,
      uitleg: "Waar. Dit levert meer winst en toegevoegde waarde op dan pure doorvoer."
    },
    {
      type: "invoer",
      vraag: "Hoe noem je de goederenspoorlijn die de Rotterdamse haven rechtstreeks verbindt met de Duitse grens?",
      antwoord: "Betuweroute|de Betuweroute",
      uitleg: "De Betuweroute ontlast het wegennet door massaal containervervoer per spoor."
    },
    {
      type: "mc",
      vraag: "Welke hightechregio in Nederland staat wereldwijd bekend om chiptechnologie en innovatie?",
      opties: [
        "Deltapoort Zeeland",
        "Greenport Westland",
        "Brainport Eindhoven",
        "Waddenhaven Texel"
      ],
      antwoord: 2,
      uitleg: "Brainport Eindhoven is de hightech-motor van de Nederlandse kenniseconomie."
    },
    {
      type: "waaronwaar",
      vraag: "Nederland staat wereldwijd in de top drie van de KOF Globaliseringsindex vanwege zijn sterke internationale verwevenheid.",
      antwoord: true,
      uitleg: "Waar. Nederland is economisch, sociaal en politiek extreem sterk verbonden met het buitenland."
    },
    {
      type: "invoer",
      vraag: "Welk hightechbedrijf in Veldhoven bouwt de meest geavanceerde chipmachines ter wereld?",
      antwoord: "ASML",
      uitleg: "ASML is een cruciale wereldspeler in de halfgeleiderindustrie."
    },
    {
      type: "mc",
      vraag: "Wat is een nadeel van de sterke toename van distributiecentra ('verdozing') in het Nederlandse landschap?",
      opties: [
        "Distributiecentra hebben geen enkel nadeel",
        "Het veroorzaakt een tekort aan buitenlandse toeristen",
        "Het leidt tot het verdwijnen van de Nederlandse taal",
        "Het neemt veel schaarse open ruimte in beslag en zorgt voor extra vrachtverkeer en stikstofuitstoot"
      ],
      antwoord: 3,
      uitleg: "Verdozing tast het open landschap aan en belast de lokale infrastructuur."
    }
  ]
});
