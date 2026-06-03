DURU.register({
  id: "h6-4",
  hoofdstuk: 6,
  paragraaf: "6.4",
  titel: "Is de schatkist goed gevuld?",
  korteUitleg: "Hoe werkt de rijksbegroting en wat is de staatsschuld?",
  icoon: "💰",

  theorie: `
<h3>💰 Is de schatkist goed gevuld?</h3>

<p>Elke euro die de overheid uitgeeft, moet ergens vandaan komen. Maar waar? En wat gebeurt
er als er niet genoeg geld is? Dat lees je in deze paragraaf over de <b>rijksbegroting</b>
en de <b>staatsschuld</b>.</p>

<h4>Wat is de rijksbegroting?</h4>

<p>De <b>rijksbegroting</b> is het financiële plan van de nationale overheid (het Rijk) voor
één jaar. Daarin staat hoeveel geld de overheid verwacht te <em>ontvangen</em> (inkomsten)
en hoeveel geld ze verwacht <em>uit te geven</em> (uitgaven).</p>

<div class="formule-box">
  <span class="formule">Rijksbegroting = overzicht van verwachte inkomsten én uitgaven van het Rijk voor één jaar</span>
  <small>Elk jaar opnieuw vastgesteld — voor het volgende kalenderjaar</small>
</div>

<div class="info-box">
  <span class="kop">💡 Onthoud</span>
  Op <b>Prinsjesdag</b> — de derde dinsdag van september — presenteert de minister-president
  de rijksbegroting aan de Tweede Kamer. De koning leest de <b>troonrede</b> voor in de
  Ridderzaal in Den Haag. De minister van Financiën biedt de <b>Miljoenennota</b> aan:
  een dikke map vol plannen en cijfers.
</div>

<h4>Inkomsten van de overheid</h4>
<p>De overheid haalt haar geld vooral uit <b>belastingen</b>:</p>
<ul>
  <li><b>Loonbelasting / inkomstenbelasting</b> — betaald door werknemers en ondernemers</li>
  <li><b>Btw</b> (omzetbelasting) — betaald bij elke aankoop in de winkel</li>
  <li><b>Vennootschapsbelasting</b> — betaald door bedrijven over hun winst</li>
  <li><b>Accijnzen</b> — extra belasting op bv. benzine, tabak en alcohol</li>
</ul>

<h4>Uitgaven van de overheid</h4>
<p>Waarvoor geeft de overheid al dat geld uit? De grootste posten zijn:</p>
<ul>
  <li><b>Zorg</b> — ziekenhuizen, medicijnen, thuiszorg</li>
  <li><b>Sociale zekerheid</b> — AOW (pensioenen), werkloosheidsuitkeringen, bijstand</li>
  <li><b>Onderwijs</b> — scholen, universiteiten, leraarssalarissen</li>
  <li><b>Veiligheid</b> — politie, rechtbanken, defensie</li>
  <li><b>Infrastructuur</b> — wegen, spoorlijnen, bruggen</li>
  <li><b>Rente</b> — betaling over eerder geleende bedragen (staatsschuld)</li>
</ul>

<h4>Begrotingstekort en begrotingsoverschot</h4>

<p>Aan het einde van een jaar kan de begroting op drie manieren uitkomen:</p>

<table class="nask">
  <tr><th>Situatie</th><th>Wat het betekent</th><th>Gevolg</th></tr>
  <tr>
    <td><b>Begrotingsoverschot</b></td>
    <td>Inkomsten &gt; Uitgaven — er is geld over</td>
    <td>Overheid kan schulden aflossen of sparen</td>
  </tr>
  <tr>
    <td><b>Evenwicht</b></td>
    <td>Inkomsten = Uitgaven — precies op nul</td>
    <td>Geen nieuw tekort, geen nieuw overschot</td>
  </tr>
  <tr>
    <td><b>Begrotingstekort</b></td>
    <td>Uitgaven &gt; Inkomsten — er is geld tekort</td>
    <td>Overheid moet <b>lenen</b></td>
  </tr>
</table>

<div class="formule-box">
  <span class="formule">Begrotingssaldo = inkomsten − uitgaven</span>
  <small>Positief saldo = overschot &nbsp;·&nbsp; Negatief saldo = tekort</small>
</div>

<div class="formule-box">
  <span class="formule">Staatsschuld = alle openstaande leningen van de overheid bij elkaar opgeteld</span>
  <small>Bij een begrotingstekort groeit de staatsschuld; bij een overschot kan ze krimpen</small>
</div>

<h4>Waarom is de staatsschuld een probleem?</h4>
<p>Als de overheid geld leent, moet ze daar <b>rente</b> over betalen. Hoe hoger de staatsschuld,
hoe meer rente er elk jaar betaald moet worden. Die rentebetalingen zijn op zichzelf ook
weer een grote uitgavenpost op de begroting. Dat geld kan dan niet aan zorg of onderwijs
worden besteed.</p>

<figure class="bron">
  <svg viewBox="0 0 440 260" width="100%" style="max-width:440px;display:block;margin:12px auto;font-family:sans-serif">
    <!-- Achtergrond -->
    <rect width="440" height="260" rx="10" fill="#f8f9fa"/>

    <!-- Titel -->
    <text x="220" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">Rijksbegroting — inkomsten vs. uitgaven</text>

    <!-- X-as labels -->
    <text x="130" y="200" text-anchor="middle" font-size="12" fill="#27ae60" font-weight="bold">Inkomsten</text>
    <text x="310" y="200" text-anchor="middle" font-size="12" fill="#e74c3c" font-weight="bold">Uitgaven</text>

    <!-- Y-as lijn -->
    <line x1="60" y1="40" x2="60" y2="190" stroke="#bdc3c7" stroke-width="1.5"/>
    <!-- Y-as labels -->
    <text x="55" y="190" text-anchor="end" font-size="10" fill="#7f8c8d">0</text>
    <text x="55" y="140" text-anchor="end" font-size="10" fill="#7f8c8d">200</text>
    <text x="55" y="90" text-anchor="end" font-size="10" fill="#7f8c8d">350</text>
    <text x="55" y="55" text-anchor="end" font-size="10" fill="#7f8c8d">mld €</text>
    <!-- Y-as rasterlijnen -->
    <line x1="60" y1="140" x2="400" y2="140" stroke="#ecf0f1" stroke-width="1"/>
    <line x1="60" y1="90"  x2="400" y2="90"  stroke="#ecf0f1" stroke-width="1"/>

    <!-- Staaf inkomsten (€ 350 mld) → hoogte 150px, top = 190-150=40 -->
    <rect x="80" y="40" width="100" height="150" rx="6" fill="#27ae60" opacity="0.85"/>
    <text x="130" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="#27ae60">€ 350 mld</text>

    <!-- Staaf uitgaven (€ 370 mld) → hoogte 158px, top = 190-158=32 -->
    <rect x="260" y="32" width="100" height="158" rx="6" fill="#e74c3c" opacity="0.85"/>
    <text x="310" y="27" text-anchor="middle" font-size="12" font-weight="bold" fill="#e74c3c">€ 370 mld</text>

    <!-- Pijl + label tekort -->
    <line x1="310" y1="40" x2="310" y2="210" stroke="#c0392b" stroke-width="0" />
    <!-- Accolade-lijn tekort: dubbele lijn tussen de tops -->
    <line x1="180" y1="36" x2="260" y2="36" stroke="#c0392b" stroke-width="2" stroke-dasharray="4,3"/>
    <text x="220" y="30" text-anchor="middle" font-size="11" fill="#c0392b" font-weight="bold">tekort: € 20 mld</text>

    <!-- X-as onderlijn -->
    <line x1="60" y1="190" x2="400" y2="190" stroke="#bdc3c7" stroke-width="1.5"/>

    <!-- Legenda onderaan -->
    <rect x="80"  y="215" width="14" height="14" rx="3" fill="#27ae60"/>
    <text x="100" y="226" font-size="11" fill="#2c3e50">Inkomsten (belastingen)</text>
    <rect x="260" y="215" width="14" height="14" rx="3" fill="#e74c3c"/>
    <text x="280" y="226" font-size="11" fill="#2c3e50">Uitgaven</text>

    <!-- Pijl tekort naar lenen -->
    <text x="220" y="246" text-anchor="middle" font-size="11" fill="#8e44ad">▼ Tekort → overheid leent → staatsschuld groeit</text>
  </svg>
  <figcaption>Staafdiagram: als de uitgavenstaaf hoger is dan de inkomstenstaaf, is er een begrotingstekort. De overheid moet dan geld lenen, waardoor de staatsschuld groeit.</figcaption>
</figure>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld — Begrotingstekort berekenen</div>
  <div class="stap"><b>Gegeven:</b> inkomsten Rijk = € 350 miljard &nbsp;|&nbsp; uitgaven Rijk = € 370 miljard</div>
  <div class="stap"><b>Formule:</b> begrotingssaldo = inkomsten − uitgaven</div>
  <div class="stap"><b>Berekening:</b> 350 − 370 = −20 miljard euro</div>
  <div class="stap"><b>Antwoord:</b> Er is een <b>begrotingstekort van € 20 miljard</b>. De overheid moet dit bedrag lenen. De staatsschuld stijgt daardoor met € 20 miljard.</div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld — Begrotingsoverschot berekenen</div>
  <div class="stap"><b>Gegeven:</b> inkomsten Rijk = € 380 miljard &nbsp;|&nbsp; uitgaven Rijk = € 360 miljard</div>
  <div class="stap"><b>Formule:</b> begrotingssaldo = inkomsten − uitgaven</div>
  <div class="stap"><b>Berekening:</b> 380 − 360 = +20 miljard euro</div>
  <div class="stap"><b>Antwoord:</b> Er is een <b>begrotingsoverschot van € 20 miljard</b>. De overheid kan dit gebruiken om schulden af te lossen.</div>
</div>

<div class="info-box let-op">
  <span class="kop">⚠️ Let op</span>
  Verwar <b>begrotingstekort</b> niet met <b>staatsschuld</b>! Het begrotingstekort is het
  tekort van <em>één jaar</em>. De staatsschuld is de <em>optelsom van alle leningen</em>
  door de jaren heen. Een klein jaarlijks tekort laat de staatsschuld langzaam groeien;
  een overschot laat hem krimpen.
</div>

<div class="info-box tip">
  <span class="kop">✅ Handige tip</span>
  Onthoud de formule zo: <b>I − U = saldo</b> (Inkomsten minus Uitgaven).
  Positief saldo = overschot (goed voor de schatkist). Negatief saldo = tekort (moet lenen).
</div>
`,

  vragen: [

    /* ── NIVEAU 1 — Begrip & herkenning ── */

    {
      type: "mc", niveau: 1,
      vraag: "Wat is de rijksbegroting?",
      opties: [
        "Een overzicht van de schulden van alle gemeenten samen",
        "Het financiële jaarplan van de nationale overheid met inkomsten en uitgaven",
        "Het salaris van de ministers voor één jaar",
        "De totale schuld van Nederland aan het buitenland"
      ],
      antwoord: 1,
      uitleg: "De <b>rijksbegroting</b> is het financiële plan van het Rijk voor één jaar: alle verwachte inkomsten én uitgaven staan erin."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Op welke dag presenteert de regering elk jaar de rijksbegroting?",
      opties: [
        "Koningsdag (27 april)",
        "Bevrijdingsdag (5 mei)",
        "Prinsjesdag (derde dinsdag van september)",
        "Nieuwjaarsdag (1 januari)"
      ],
      antwoord: 2,
      uitleg: "Op <b>Prinsjesdag</b> — de derde dinsdag van september — biedt de minister van Financiën de Miljoenennota aan en leest de koning de troonrede voor in Den Haag."
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "De grootste inkomstenbron van de rijksoverheid zijn belastingen.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Belastingen — zoals loonbelasting, btw en vennootschapsbelasting — vormen verreweg de grootste inkomstenbron voor het Rijk."
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "Als de overheid meer uitgeeft dan ze ontvangt, spreken we van een begrotingsoverschot.",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> Als uitgaven groter zijn dan inkomsten, is er een <b>begrotingstekort</b>. Een overschot is juist het omgekeerde: inkomsten zijn groter dan uitgaven."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Wat is de staatsschuld?",
      opties: [
        "Het begrotingstekort van dit jaar",
        "De totale som van alle openstaande leningen van de overheid",
        "Het bedrag dat burgers aan belasting betalen",
        "De winst van de overheid na aftrek van de kosten"
      ],
      antwoord: 1,
      uitleg: "De <b>staatsschuld</b> is de optelsom van <em>alle</em> leningen van de overheid — opgebouwd over vele jaren. Het begrotingstekort is slechts het tekort van één jaar."
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "De Miljoenennota is de naam voor de rijksbegroting die op Prinsjesdag wordt aangeboden.",
      antwoord: true,
      uitleg: "<b>Waar.</b> De <b>Miljoenennota</b> is het officiële document met alle begrotingsplannen van het Rijk, aangeboden door de minister van Financiën op Prinsjesdag."
    },

    /* ── NIVEAU 2 — Inzicht & rekenen ── */

    {
      type: "invoer", niveau: 2,
      vraag: "De rijksoverheid heeft in een jaar inkomsten van € 350 miljard en uitgaven van € 370 miljard. Bereken het begrotingssaldo. Is er een tekort of overschot?",
      antwoord: "-20|−20",
      eenheid: "miljard euro",
      uitleg: "Saldo = inkomsten − uitgaven = 350 − 370 = <b>−20 miljard euro</b>. Negatief = begrotingstekort. De overheid moet € 20 miljard lenen.",
      hint: "Gebruik de formule: saldo = inkomsten − uitgaven."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "De overheid ontvangt € 380 miljard en geeft € 360 miljard uit. Bereken het begrotingssaldo.",
      antwoord: "20",
      eenheid: "miljard euro",
      uitleg: "Saldo = 380 − 360 = <b>+20 miljard euro</b>. Positief = begrotingsoverschot. De overheid kan schulden aflossen."
    },

    {
      type: "mc", niveau: 2,
      vraag: "De overheid heeft inkomsten van € 290 miljard en uitgaven van € 310 miljard. Wat is het begrotingssaldo?",
      opties: [
        "Een overschot van € 20 miljard",
        "Een tekort van € 20 miljard",
        "Een tekort van € 310 miljard",
        "Precies in evenwicht"
      ],
      antwoord: 1,
      uitleg: "Saldo = 290 − 310 = −20 miljard. Negatief saldo = <b>begrotingstekort van € 20 miljard</b>. De overheid moet dit bedrag lenen.",
      hint: "Trek inkomsten af van uitgaven: 290 − 310."
    },

    {
      type: "waaronwaar", niveau: 2,
      vraag: "Als de overheid jarenlang een begrotingstekort heeft, groeit de staatsschuld steeds verder.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Elk jaar dat er een tekort is, moet de overheid opnieuw lenen. Die nieuwe lening wordt opgeteld bij de bestaande staatsschuld. Zo groeit die schuld jaar na jaar."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Welke van de volgende uitgaven hoort bij de rijksbegroting?",
      opties: [
        "De weekboodschappen van een gezin",
        "Het salaris van leraren in het openbaar onderwijs",
        "De huur die een bedrijf betaalt voor zijn kantoor",
        "De vakantiekosten van een provincie-ambtenaar"
      ],
      antwoord: 1,
      uitleg: "<b>Onderwijs</b> — waaronder de salarissen van leraren — is een grote uitgavenpost op de rijksbegroting. De andere opties zijn privé- of bedrijfsuitgaven."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een land heeft een staatsschuld van € 400 miljard. In het nieuwe jaar is er een begrotingstekort van € 25 miljard. Hoe hoog is de staatsschuld aan het einde van dat jaar?",
      antwoord: "425",
      eenheid: "miljard euro",
      uitleg: "Nieuwe staatsschuld = 400 + 25 = <b>€ 425 miljard</b>. Bij een tekort moet de overheid lenen; dat bedrag wordt bij de bestaande schuld opgeteld.",
      hint: "Tekort betekent lenen. Tel het tekort op bij de bestaande schuld."
    },

    {
      type: "waaronwaar", niveau: 2,
      vraag: "Over de staatsschuld betaalt de overheid rente. Die rente is zelf ook een uitgavenpost op de begroting.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Rente over leningen is een echte uitgave op de rijksbegroting. Hoe groter de staatsschuld, hoe meer rente — en hoe minder geld overblijft voor zorg, onderwijs, etc."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Duru kijkt naar Prinsjesdag op tv. De minister zegt: 'Dit jaar is er een begrotingstekort van € 15 miljard.' Wat betekent dit voor de staatsschuld?",
      opties: [
        "De staatsschuld daalt met € 15 miljard",
        "De staatsschuld verandert niet",
        "De staatsschuld stijgt met € 15 miljard",
        "De staatsschuld wordt precies € 15 miljard"
      ],
      antwoord: 2,
      uitleg: "Bij een <b>begrotingstekort</b> moet de overheid lenen. Die lening wordt opgeteld bij de bestaande staatsschuld — die stijgt dus met € 15 miljard.",
      hint: "Tekort = lenen = schuld groeit."
    },

    /* ── NIVEAU 3 — Dieper inzicht & combineren ── */

    {
      type: "invoer", niveau: 3,
      vraag: "De staatsschuld van Nederland is € 450 miljard. In dat jaar heeft de overheid een begrotingsoverschot van € 10 miljard en lost ze dat af op de schuld. Hoe hoog is de staatsschuld daarna?",
      antwoord: "440",
      eenheid: "miljard euro",
      uitleg: "Bij een overschot kan de overheid schulden aflossen: 450 − 10 = <b>€ 440 miljard</b>. De staatsschuld krimpt.",
      hint: "Overschot = geld over = schuld aflossen = schuld daalt."
    },

    {
      type: "mc", niveau: 3,
      vraag: "De overheid wil de zorguitgaven verhogen zonder de belastingen te verhogen. Wat is het meest waarschijnlijke gevolg voor de begroting?",
      opties: [
        "Het begrotingstekort neemt af",
        "Het begrotingstekort neemt toe (of het overschot wordt kleiner)",
        "De staatsschuld daalt automatisch",
        "De inkomsten stijgen vanzelf mee"
      ],
      antwoord: 1,
      uitleg: "Als de uitgaven stijgen maar de inkomsten gelijkblijven, wordt het saldo (inkomsten − uitgaven) <em>negatiever</em>. Het tekort groeit dus, of een bestaand overschot wordt kleiner.",
      hint: "Denk aan de formule: saldo = inkomsten − uitgaven. Wat gebeurt er als uitgaven stijgen?"
    },

    {
      type: "waaronwaar", niveau: 3,
      vraag: "Een land met een begrotingsoverschot heeft per definitie geen staatsschuld.",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> Een overschot betekent dat er <em>dit jaar</em> meer binnenkomt dan uitgegeven wordt. Maar de staatsschuld is de optelsom van schulden over <em>alle voorgaande jaren</em>. Een land kan tegelijk een overschot hebben én een enorme staatsschuld uit het verleden.",
      hint: "Staatsschuld en jaarlijks saldo zijn twee verschillende begrippen."
    },

    {
      type: "invoer", niveau: 3,
      vraag: "Bereken het begrotingssaldo: inkomsten zijn € 420 miljard, uitgaven zijn € 395 miljard. Is er een tekort of overschot, en hoe groot?",
      antwoord: "25",
      eenheid: "miljard euro",
      uitleg: "Saldo = 420 − 395 = <b>+25 miljard euro</b>. Positief = <b>begrotingsoverschot</b> van € 25 miljard. De overheid heeft geld over.",
      hint: "Saldo = inkomsten − uitgaven. Positief saldo = overschot."
    },

  ]
});
