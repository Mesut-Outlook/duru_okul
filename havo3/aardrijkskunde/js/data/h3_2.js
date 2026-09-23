/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §3.2 Gevolgen voor de herkomstgebieden
   buiteNLand 3 HAVO Hoofdstuk 3 (Migratie)
   ========================================================= */
DURU.register({
  id: "ak-h3-2",
  hoofdstuk: 3,
  paragraaf: "3.2",
  titel: "Gevolgen voor de herkomstgebieden",
  korteUitleg: "Braindrain, braingain, geldzendingen (remittances), migratienetwerken en demografische veranderingen.",
  icoon: "📉",
  kleur: "h3-thema",
  theorie: `<h3>3.2 Gevolgen voor de herkomstgebieden</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Braindrain, braingain, geldzendingen (remittances), migratienetwerken, volgmigratie (kettingmigratie), selectieve migratie, retourmigratie.
</div>

<h4>1. Economische effecten: Geldzendingen (Remittances)</h4>
<p>Een van de meest directe positieve gevolgen van emigratie voor arme herkomstlanden zijn <b>geldzendingen</b> (in het Engels: <i>remittances</i>). Migranten die in rijke landen werken, sturen maandelijks een aanzienlijk deel van hun spaargeld terug naar familieleden die achterbleven. Wereldwijd is het totale bedrag aan geldzendingen vele malen groter dan alle officiële internationale ontwikkelingshulp van overheden bij elkaar opgeteld! Dit geld wordt direct besteed aan dagelijks voedsel, betere huisvesting, schoolgeld voor kinderen en medische zorg.</p>

<h4>2. Het kenniseffect: Braindrain versus Braingain</h4>
<p>Migratie heeft echter ook zware schaduwkanten voor de herkomstgebieden:</p>
<ul>
  <li><b>Braindrain:</b> Dit ontstaat wanneer veel hoogopgeleide, getalenteerde en ondernemende mensen (zoals artsen, verpleegkundigen, docenten, ingenieurs en wetenschappers) massaal het land verlaten om in het buitenland meer geld te verdienen. Hierdoor kampt het herkomstland met een chronisch tekort aan essentiële specialisten, wat de lokale economische ontwikkeling ernstig remt.</li>
  <li><b>Braingain:</b> Wanneer geëmigreerde specialisten na enkele jaren besluiten terug te keren naar hun vaderland (<b>retourmigratie</b>), brengen zij waardevolle kennis, internationale werkervaring, vreemde talen en investeringskapitaal mee. Hierdoor kan braindrain uiteindelijk omslaan in een stimulans voor het herkomstland.</li>
</ul>

<h4>3. Demografische en sociale gevolgen</h4>
<p>Migratie is vrijwel altijd <b>selectieve migratie</b>: het zijn meestal niet de ouderen of de allerarmsten die verhuizen, maar met name gezonde, jonge volwassenen tussen de 18 en 35 jaar. Dit heeft duidelijke gevolgen voor het herkomstgebied:</p>
<ul>
  <li><b>Vergrijzing en ontvolking:</b> In dorpen en plattelandsgebieden blijven vooral ouderen, vrouwen en jonge kinderen achter. Landbouwgrond raakt soms verlaten.</li>
  <li><b>Migratienetwerken en volgmigratie:</b> De eerste pioniers die vertrekken bouwen een netwerk op in het bestemmingsland. Zij helpen familieleden en vrienden aan onderdak en werk, waardoor één migrant vaak leidt tot tientallen nieuwe migranten (<b>volgmigratie</b> of kettingmigratie).</li>
</ul>`,
  vragen: [
    {
        "type": "mc",
        "vraag": "Wat is het belangrijkste kenmerk van een <b>braindrain</b> voor een ontwikkelingsland?",
        "opties": [
            "Hoogopgeleide krachten zoals artsen en ingenieurs verlaten massaal het land",
            "Er stromen te veel buitenlandse studenten het land binnen",
            "Het land verliest al zijn landbouwgrond door overstromingen",
            "Er is geen internetverbinding meer beschikbaar"
        ],
        "antwoord": 0,
        "uitleg": "Braindrain betekent letterlijk het weglekken van hersenen (kennis) doordat talentvolle specialisten emigreren."
    },
    {
        "type": "mc",
        "vraag": "Wat zijn <b>geldzendingen (remittances)</b>?",
        "opties": [
            "Subsidies die de Europese Unie betaalt aan boeren",
            "Geld dat migranten vanuit het bestemmingsland terugsturen naar familie in het herkomstland",
            "Boetes die illegale smokkelaars moeten betalen aan de douane",
            "Leningen die bedrijven afsluiten bij buitenlandse banken"
        ],
        "antwoord": 1,
        "uitleg": "Geldzendingen zijn overboekingen van migranten naar hun familie thuis, een enorme inkomstenbron voor herkomstlanden."
    },
    {
        "type": "waaronwaar",
        "vraag": "Braingain ontstaat wanneer terugkerende migranten nieuwe kennis en investeringen meebrengen naar hun herkomstland.",
        "antwoord": true,
        "uitleg": "Waar. Braingain is het positieve kenniseffect van terugkerende migranten."
    },
    {
        "type": "waaronwaar",
        "vraag": "Bij selectieve migratie vertrekken vooral hoogbejaarde mensen naar het buitenland.",
        "antwoord": false,
        "uitleg": "Niet waar. Selectieve migratie betreft vooral jonge, fysiek gezonde volwassenen (18-35 jaar)."
    },
    {
        "type": "invoer",
        "vraag": "Hoe heet het verschijnsel waarbij de vestiging van eerdere migranten leidt tot het overkomen van familieleden en vrienden?",
        "antwoord": "volgmigratie|kettingmigratie",
        "uitleg": "Volgmigratie of kettingmigratie ontstaat via migratienetwerken."
    },
    {
        "type": "invoer",
        "vraag": "Hoe noemen we de vorm van migratie waarbij mensen definitief terugkeren naar hun geboorteland?",
        "antwoord": "retourmigratie|terugkeermigratie",
        "uitleg": "Retourmigratie is het terugkeren naar het land van herkomst."
    },
    {
        "type": "mc",
        "vraag": "Wat is een nadelig demografisch gevolg van selectieve emigratie voor achterblijvende dorpen op het platteland?",
        "opties": [
            "Een plotselinge geboortegolf in de dorpen",
            "Een sterke daling van het aantal ouderen",
            "Vergrijzing en tekort aan arbeidskrachten doordat jonge volwassenen wegtrekken",
            "Overbevolking in de dorpen"
        ],
        "antwoord": 2,
        "uitleg": "Als jonge volwassenen wegtrekken blijven vooral ouderen en kinderen achter, waardoor het dorp vergrijst."
    },
    {
        "type": "mc",
        "vraag": "Waarom zijn geldzendingen van migranten economisch zo belangrijk voor herkomstlanden?",
        "opties": [
            "Omdat de overheid dit geld volledig mag confisqueren voor defensie",
            "Omdat migranten verplicht zijn aandelen te kopen in de centrale bank",
            "Omdat het bedrag alleen aan buitenlandse luxeproducten besteed mag worden",
            "Omdat het geld rechtstreeks bij arme gezinnen terechtkomt voor onderwijs, voedsel en bouw"
        ],
        "antwoord": 3,
        "uitleg": "Geldzendingen komen direct bij huishoudens terecht en zorgen voor armoedeverlichting en betere levensomstandigheden."
    }
]
});
