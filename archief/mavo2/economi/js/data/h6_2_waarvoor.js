DURU.register({
  id: "h6-2",
  hoofdstuk: 6,
  paragraaf: "6.2",
  titel: "Waar zorgt de overheid voor?",
  korteUitleg: "Collectieve voorzieningen: wat de overheid voor iedereen regelt en betaalt.",
  icoon: "🛣️",

  theorie: `
<h3>Het is voor iedereen</h3>
<p>Er zijn allerlei zaken die iedereen nodig heeft maar die bedrijven niet (goed) kunnen regelen.
Denk aan veiligheid, wegen en scholen. De <b>overheid</b> zorgt hiervoor en betaalt het uit
<b>belastinggeld</b>.</p>

<div class="formule-box">
  <span class="formule">Collectieve voorzieningen</span>
  <small>spullen en diensten die de overheid voor <b>iedereen</b> regelt en betaalt,
  omdat de markt dit niet (goed) doet</small>
</div>

<div class="info-box"><span class="kop">💡 Onthoud</span>
  Het woord <em>collectief</em> komt van het Latijnse <em>collectivus</em> = <b>voor de groep</b>.
  Collectieve voorzieningen zijn dus voorzieningen voor de hele samenleving samen.
</div>

<h3>Voorbeelden van collectieve voorzieningen</h3>
<p>Er zijn veel verschillende soorten. Hieronder staan de belangrijkste:</p>

<table class="nask">
  <tr>
    <th>Soort</th>
    <th>Voorbeelden</th>
  </tr>
  <tr>
    <td><b>Veiligheid</b></td>
    <td>Politie, brandweer, leger, dijken en waterkeringen</td>
  </tr>
  <tr>
    <td><b>Infrastructuur</b></td>
    <td>Wegen, fietspaden, bruggen, tunnels, openbaar vervoer (bus, trein)</td>
  </tr>
  <tr>
    <td><b>Onderwijs</b></td>
    <td>Basisschool, middelbare school, universiteit</td>
  </tr>
  <tr>
    <td><b>Gezondheidszorg</b></td>
    <td>Ziekenhuizen, GGD, vaccinaties, AOW voor ouderen</td>
  </tr>
  <tr>
    <td><b>Milieu &amp; leefomgeving</b></td>
    <td>Schone lucht, afvalverwerking, straatverlichting, parken</td>
  </tr>
</table>

<h3>Waarom doet de overheid dit?</h3>
<p>Er zijn drie belangrijke redenen waarom de overheid collectieve voorzieningen regelt
in plaats van private bedrijven:</p>
<ul>
  <li><b>Iedereen heeft er baat bij.</b> Een weg of dijk helpt de hele samenleving, niet alleen
  degene die ervoor betaalt.</li>
  <li><b>Niet winstgevend.</b> Bedrijven willen winst maken. Een veilig land of schone lucht
  leveren geen directe winst op, dus bedrijven doen dit niet (of niet genoeg).</li>
  <li><b>Meeliftgedrag.</b> Als je een weg aanlegt, rijden alle mensen erop mee — ook mensen
  die er niet voor hebben betaald. Dat heet <em>meeliftgedrag</em> (of "free rider"-probleem).
  De overheid lost dit op door via belastingen iedereen mee te laten betalen.</li>
</ul>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  Collectieve voorzieningen zijn <b>niet gratis</b>! Ze worden betaald uit <b>belastingen</b> die
  burgers en bedrijven afdragen. Dit komt in paragraaf 6.3 verder aan bod.
</div>

<h3>Overzicht: overheid en haar voorzieningen</h3>

<figure class="bron">
  <svg viewBox="0 0 440 320" width="100%" style="max-width:440px;display:block;margin:0 auto"
       aria-label="Rondje overheid met pijlen naar vier collectieve voorzieningen">
    <!-- Achtergrond -->
    <rect width="440" height="320" rx="12" fill="#f0f7ff" stroke="#3a86ff" stroke-width="1.5"/>

    <!-- Overheid in het midden -->
    <circle cx="220" cy="160" r="52" fill="#1d3557" stroke="#3a86ff" stroke-width="3"/>
    <text x="220" y="154" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Over-</text>
    <text x="220" y="172" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">heid</text>

    <!-- Pijl naar boven: Veiligheid -->
    <line x1="220" y1="108" x2="220" y2="60" stroke="#e63946" stroke-width="2.5" marker-end="url(#pijl-r)"/>
    <!-- Ballon veiligheid -->
    <rect x="158" y="12" width="124" height="44" rx="10" fill="#e63946"/>
    <text x="220" y="32" text-anchor="middle" font-size="13" font-weight="bold" fill="#fff">🚓 Veiligheid</text>
    <text x="220" y="50" text-anchor="middle" font-size="10" fill="#fff">politie · brandweer · leger</text>

    <!-- Pijl naar rechts: Infrastructuur -->
    <line x1="272" y1="160" x2="340" y2="160" stroke="#f4a261" stroke-width="2.5" marker-end="url(#pijl-o)"/>
    <!-- Ballon infrastructuur -->
    <rect x="340" y="132" width="84" height="56" rx="10" fill="#f4a261"/>
    <text x="382" y="152" text-anchor="middle" font-size="11" font-weight="bold" fill="#fff">🛣️ Infra-</text>
    <text x="382" y="166" text-anchor="middle" font-size="11" font-weight="bold" fill="#fff">structuur</text>
    <text x="382" y="181" text-anchor="middle" font-size="9" fill="#fff">wegen · OV · fietspaden</text>

    <!-- Pijl naar onder: Onderwijs -->
    <line x1="220" y1="212" x2="220" y2="262" stroke="#2a9d8f" stroke-width="2.5" marker-end="url(#pijl-g)"/>
    <!-- Ballon onderwijs -->
    <rect x="158" y="264" width="124" height="44" rx="10" fill="#2a9d8f"/>
    <text x="220" y="284" text-anchor="middle" font-size="13" font-weight="bold" fill="#fff">🏫 Onderwijs</text>
    <text x="220" y="301" text-anchor="middle" font-size="10" fill="#fff">school · universiteit</text>

    <!-- Pijl naar links: Zorg -->
    <line x1="168" y1="160" x2="100" y2="160" stroke="#457b9d" stroke-width="2.5" marker-end="url(#pijl-b)"/>
    <!-- Ballon zorg -->
    <rect x="16" y="132" width="84" height="56" rx="10" fill="#457b9d"/>
    <text x="58" y="152" text-anchor="middle" font-size="13" font-weight="bold" fill="#fff">🏥 Zorg</text>
    <text x="58" y="170" text-anchor="middle" font-size="10" fill="#fff">ziekenhuis · GGD</text>
    <text x="58" y="183" text-anchor="middle" font-size="9" fill="#fff">vaccinaties · AOW</text>

    <!-- Pijlkoppen (arrowhead markers) -->
    <defs>
      <marker id="pijl-r" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#e63946"/>
      </marker>
      <marker id="pijl-o" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#f4a261"/>
      </marker>
      <marker id="pijl-g" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#2a9d8f"/>
      </marker>
      <marker id="pijl-b" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#457b9d"/>
      </marker>
    </defs>
  </svg>
  <figcaption>De overheid regelt en betaalt vier grote groepen collectieve voorzieningen voor iedereen.</figcaption>
</figure>

<h3>Collectief vs. particulier</h3>
<p>Niet alles wat de overheid aanbiedt is collectief, en niet alles wat bedrijven leveren is particulier.
Het verschil zit in <b>wie betaalt</b>:</p>

<table class="nask">
  <tr>
    <th>Collectief (overheid betaalt)</th>
    <th>Particulier (jijzelf betaalt)</th>
  </tr>
  <tr>
    <td>Openbare basisschool</td>
    <td>Privéles of bijles</td>
  </tr>
  <tr>
    <td>Straatverlichting</td>
    <td>Lamp in je eigen tuin</td>
  </tr>
  <tr>
    <td>Brandweer</td>
    <td>Inbraakalarm voor je huis</td>
  </tr>
  <tr>
    <td>Openbaar zwembad</td>
    <td>Zwembad in je achtertuin</td>
  </tr>
</table>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Vraag jezelf altijd af: <em>Wie betaalt dit?</em> Betaalt de overheid het (via belasting)?
  Dan is het een collectieve voorziening. Betaal jij het zelf? Dan is het particulier.
</div>

<h3>Hoe wordt het betaald?</h3>
<p>Alle collectieve voorzieningen worden betaald uit <b>belastingen</b>. Burgers en bedrijven
dragen belasting af aan de overheid. De overheid gebruikt dat geld om politieagenten
te betalen, wegen aan te leggen, scholen te bouwen enzovoort.
Dit komt verder aan bod in <em>paragraaf 6.3</em>.</p>
`,

  vragen: [
    // ── NIVEAU 1 — MEERKEUZE ─────────────────────────────────────────────────

    {
      type: "mc", niveau: 1,
      vraag: "Wat zijn collectieve voorzieningen?",
      opties: [
        "Spullen en diensten die je zelf koopt in de winkel.",
        "Spullen en diensten die de overheid voor iedereen regelt en betaalt.",
        "Producten die alleen voor rijke mensen beschikbaar zijn.",
        "Diensten die bedrijven gratis aanbieden."
      ],
      antwoord: 1,
      uitleg: "<b>Collectieve voorzieningen</b> zijn spullen en diensten die de overheid voor de hele samenleving regelt en betaalt, omdat de markt dit niet (goed) doet."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Waarmee betaalt de overheid de collectieve voorzieningen?",
      opties: ["Met winst uit staatsbedrijven.", "Met leningen van de bank.", "Met belastinggeld van burgers en bedrijven.", "Met donaties van inwoners."],
      antwoord: 2,
      uitleg: "Collectieve voorzieningen worden betaald uit <b>belastingen</b> die burgers en bedrijven afdragen aan de overheid."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Welk van de volgende voorbeelden is een collectieve voorziening?",
      opties: ["Een privéswembad in de achtertuin.", "Straatverlichting in de wijk.", "Een abonnement op een streamingdienst.", "Een boodschappenkar in de supermarkt."],
      antwoord: 1,
      uitleg: "<b>Straatverlichting</b> wordt door de overheid aangelegd en betaald voor alle inwoners. Het is er voor iedereen, niet alleen voor degene die er apart voor betaalt."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Welke dienst hoort bij de collectieve voorziening 'veiligheid'?",
      opties: ["Een privébeveiligingsbedrijf.", "Een alarm voor je fiets.", "De brandweer.", "Een slot op de voordeur."],
      antwoord: 2,
      uitleg: "De <b>brandweer</b> is een collectieve voorziening: de overheid betaalt de brandweer zodat iedereen geholpen kan worden bij brand, niet alleen mensen die er zelf voor betalen."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Waarom zijn wegen en fietspaden een collectieve voorziening?",
      opties: [
        "Omdat automobilisten er altijd zelf voor betalen.",
        "Omdat iedereen er gebruik van maakt en bedrijven er geen winst op maken.",
        "Omdat alleen de gemeente er gebruik van mag maken.",
        "Omdat ze alleen in grote steden nodig zijn."
      ],
      antwoord: 1,
      uitleg: "Wegen en fietspaden zijn er voor <b>iedereen</b> en leveren geen directe winst op voor bedrijven. Daarom legt de overheid ze aan en betaalt ze via belastingen."
    },

    // ── NIVEAU 2 — MEERKEUZE ─────────────────────────────────────────────────

    {
      type: "mc", niveau: 2,
      vraag: "Wat is meeliftgedrag (het 'free rider'-probleem)?",
      opties: [
        "Gratis meerijden op de fiets van een vriend.",
        "Profiteren van een collectieve voorziening zonder er zelf voor te betalen.",
        "Te veel belasting betalen terwijl je weinig gebruik maakt van voorzieningen.",
        "Een abonnement op het openbaar vervoer dat je niet gebruikt."
      ],
      antwoord: 1,
      uitleg: "<b>Meeliftgedrag</b> ontstaat als mensen profiteren van een voorziening (bijv. een weg of de politie) zonder ervoor te betalen. De overheid lost dit op door belastingen te heffen zodat iedereen meebetaalt.",
      hint: "Denk aan een weg: als je er eenmaal is, kan iedereen er rijden, ook wie niet heeft betaald."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Duru vraagt zich af of haar openbare basisschool een collectieve voorziening is. Wat is het juiste antwoord?",
      opties: [
        "Nee, want haar ouders betalen schoolgeld.",
        "Ja, want de overheid betaalt een groot deel via belastingen.",
        "Nee, want scholen worden door bedrijven beheerd.",
        "Ja, maar alleen als de school meer dan 500 leerlingen heeft."
      ],
      antwoord: 1,
      uitleg: "Een <b>openbare basisschool</b> wordt grotendeels betaald door de overheid (via belastingen). Ouders betalen geen (of heel weinig) schoolgeld. Het is dus een collectieve voorziening."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Waarom regelt de overheid collectieve voorzieningen en niet het bedrijfsleven?",
      opties: [
        "Omdat bedrijven te klein zijn om grote projecten te doen.",
        "Omdat de overheid meer werknemers heeft dan bedrijven.",
        "Omdat veel collectieve voorzieningen niet winstgevend zijn voor bedrijven.",
        "Omdat bedrijven niet mogen samenwerken met de overheid."
      ],
      antwoord: 2,
      uitleg: "Bedrijven willen <b>winst</b> maken. Voorzieningen zoals veiligheid, dijken of straatverlichting leveren geen winst op. Daarom doet de overheid dit — zij hoeft geen winst te maken."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Welke van de volgende zaken is GEEN collectieve voorziening?",
      opties: ["De GGD die gratis vaccinaties geeft.", "Een privéziekenhuis waar je extra betaalt voor een eigen kamer.", "Een openbare weg door de stad.", "De politie die inbraken onderzoekt."],
      antwoord: 1,
      uitleg: "Een <b>privéziekenhuis</b> waar je extra betaalt is een <em>particuliere</em> dienst, geen collectieve voorziening. De andere drie worden betaald en geregeld door de overheid voor iedereen."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Nederland heeft dijken en waterkeringen om het land droog te houden. Waarom is dit een collectieve voorziening?",
      opties: [
        "Omdat dijken heel duur zijn en alleen de overheid dat kan betalen.",
        "Omdat iedereen in Nederland er baat bij heeft en meeliftgedrag anders een groot probleem is.",
        "Omdat dijken altijd van steen zijn en bedrijven geen steen mogen verwerken.",
        "Omdat de Europese Unie dit verplicht stelt."
      ],
      antwoord: 1,
      uitleg: "Dijken beschermen <b>iedereen</b> in Nederland. Als je dijken aan de markt overlaat, profiteert iedereen mee (meeliftgedrag) maar betaalt niemand vrijwillig. De overheid lost dit op door het via belastingen te financieren.",
      hint: "Stel je voor: als alleen mensen die betalen beschermd worden door de dijk, wat gebeurt er dan met de rest?"
    },

    // ── NIVEAU 2 — WAAR / ONWAAR ─────────────────────────────────────────────

    {
      type: "waaronwaar", niveau: 2,
      vraag: "Collectieve voorzieningen zijn gratis voor iedereen — niemand betaalt er iets voor.",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> Collectieve voorzieningen worden betaald uit <b>belastinggeld</b>. Burgers en bedrijven betalen via belastingen mee. Ze zijn dus niet gratis — je betaalt er indirect voor."
    },

    {
      type: "waaronwaar", niveau: 2,
      vraag: "Het leger is een voorbeeld van een collectieve voorziening.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Het leger zorgt voor de veiligheid van het hele land. Iedereen heeft er baat bij, en het wordt betaald uit belastingen. Dat maakt het een collectieve voorziening."
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "Een privézwembad in de achtertuin van een rijke buurman is een collectieve voorziening.",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> Een privézwembad is een <em>particuliere</em> voorziening: de eigenaar betaalt zelf en het is niet voor iedereen. Een collectieve voorziening is voor de <b>hele samenleving</b>."
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "Straatverlichting in een wijk is een voorbeeld van een collectieve voorziening.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Straatverlichting is er voor <b>iedereen</b> in de wijk en wordt betaald door de (gemeente)overheid via belastingen. Het is een typisch voorbeeld van een collectieve voorziening."
    },

    // ── NIVEAU 3 — MEERKEUZE ─────────────────────────────────────────────────

    {
      type: "mc", niveau: 3,
      vraag: "Stel: de overheid besluit de politie te privatiseren (van de markt te laten regelen). Welk probleem ontstaat er dan hoogstwaarschijnlijk?",
      opties: [
        "De politie wordt goedkoper, want concurrentie verlaagt de prijzen.",
        "Er komen meer agenten, want bedrijven zijn efficiënter.",
        "Meeliftgedrag: mensen die niet betalen, worden niet geholpen maar profiteren wel van de veiligheid die betalende mensen creëren.",
        "De overheid kan dan meer belasting heffen voor andere voorzieningen."
      ],
      antwoord: 2,
      uitleg: "Als politie privaat zou zijn, betalen alleen betalende klanten. Maar veiligheid is een <b>collectief goed</b>: als de buurt veiliger is, profiteert iedereen mee — ook wie niet betaalt (<em>meeliftgedrag</em>). Daardoor is er altijd te weinig vraag en investeert de markt te weinig in veiligheid.",
      hint: "Denk aan het free rider-probleem: als jij betaalt voor veiligheid in de straat, hebben je buren er ook baat bij zonder te betalen."
    },

    {
      type: "mc", niveau: 3,
      vraag: "Een leerling zegt: 'Ik gebruik het openbaar vervoer nooit, dus ik hoef er ook geen belasting voor te betalen.' Wat klopt er niet aan deze redenering?",
      opties: [
        "De leerling heeft gelijk: wie het niet gebruikt, hoeft niet te betalen.",
        "Collectieve voorzieningen worden betaald door álle belastingbetalers, ook als je ze zelf niet direct gebruikt — want de samenleving als geheel heeft er baat bij.",
        "Openbaar vervoer is geen collectieve voorziening, dus de leerling hoeft inderdaad niet mee te betalen.",
        "Alleen ouderen betalen mee aan het openbaar vervoer."
      ],
      antwoord: 1,
      uitleg: "Collectieve voorzieningen worden betaald door <b>iedereen</b> via belastingen, ook als je ze zelf niet altijd gebruikt. Het openbaar vervoer vermindert files, zorgt dat mensen naar werk kunnen en houdt de economie draaiende — de hele samenleving heeft er baat bij.",
      hint: "Stel jezelf de vraag: heeft de samenleving als geheel baat bij goed openbaar vervoer, ook als jij er zelf niet in zit?"
    },

    {
      type: "mc", niveau: 3,
      vraag: "Welke uitspraak beschrijft het beste waarom de overheid onderwijs als collectieve voorziening aanbiedt?",
      opties: [
        "Omdat scholen anders te weinig leerlingen zouden trekken.",
        "Omdat goed opgeleide mensen alleen goed zijn voor henzelf.",
        "Omdat goed onderwijs de hele samenleving sterker maakt — meer kennis leidt tot betere banen, meer welvaart en minder ongelijkheid.",
        "Omdat de EU dit verplicht heeft gesteld voor alle lidstaten."
      ],
      antwoord: 2,
      uitleg: "Goed <b>onderwijs</b> is niet alleen voordelig voor de leerling zelf, maar voor de <em>hele samenleving</em>: hogere welvaart, minder werkloosheid, innovatie en minder ongelijkheid. Dat is precies waarom de overheid het als collectieve voorziening regelt.",
      hint: "Denk verder dan de individuele leerling: wat levert goed onderwijs op voor het hele land?"
    }
  ]
});
