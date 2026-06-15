DURU.register({
  id: "sp-4",
  hoofdstuk: 2,
  paragraaf: "2.1",
  titel: "Voegwoorden & Interpunctie",
  korteUitleg: "Oefen met voegwoorden (omdat, want, maar) en leestekens (komma, punt, vraagteken).",
  icoon: "🔗",
  theorie: `
    <h3>1. Voegwoorden (Conjunctions)</h3>
    <p>Een voegwoord verbindt twee zinnen met elkaar. Elk voegwoord heeft een eigen betekenis:</p>

    <ul>
      <li><b>omdat</b> &rarr; geeft een <b>reden</b> aan. (De bijzin krijgt een andere woordvolgorde)</li>
      <li><b>want</b> &rarr; geeft ook een <b>reden</b> aan. (De bijzin behoudt de normale woordvolgorde)</li>
      <li><b>maar</b> &rarr; geeft een <b>tegenstelling</b> aan.</li>
      <li><b>dus</b> &rarr; geeft een <b>gevolg</b> aan.</li>
      <li><b>terwijl</b> &rarr; geeft aan dat iets <b>tegelijkertijd</b> gebeurt.</li>
      <li><b>hoewel</b> &rarr; geeft een tegenwerping aan (<b>ondanks iets</b>).</li>
    </ul>

    <div class="voorbeeld">
      <div class="vb-kop">📐 Voorbeelden uit je aantekeningen</div>
      <div class="stap">Ik blijf binnen, <b>omdat</b> het regent. (Reden)</div>
      <div class="stap">Ik blijf binnen, <b>want</b> het regent. (Reden)</div>
      <div class="stap">Het regent, <b>maar</b> ik ga toch naar buiten. (Tegenstelling)</div>
      <div class="stap">Het regent, <b>dus</b> ik neem een paraplu mee. (Gevolg)</div>
      <div class="stap">Ik luister naar muziek, <b>terwijl</b> ik mijn huiswerk maak. (Tegelijk iets)</div>
      <div class="stap">Ik ga naar buiten, <b>hoewel</b> het hard regent. (Ondanks iets)</div>
    </div>

    <h3>2. Interpunctie (Leestekens)</h3>
    <p>Leestekens helpen om een zin makkelijker te lezen. Onthoud deze basisregels:</p>

    <ul>
      <li><b>Hoofdletter:</b> Altijd aan het <b>begin van een zin</b> (en bij namen).</li>
      <li><b>Punt (.):</b> Aan het eind van een <b>gewone zin</b>.</li>
      <li><b>Vraagteken (?):</b> Aan het eind van een <b>vraag</b>.</li>
      <li><b>Uitroepteken (!):</b> Bij een <b>emotie</b>, uitroep of <b>waarschuwing</b>.</li>
      <li><b>Komma (,):</b> Schrijf je <b>vaak voor voegwoorden</b> (zoals <i>want</i>, <i>maar</i>, <i>omdat</i>, <i>terwijl</i>, <i>hoewel</i>). Voor het voegwoord <i>en</i> schrijf je meestal <u>geen</u> komma!</li>
    </ul>
  `,
  vragen: [
    {
      type: "mc", niveau: 1,
      vraag: "Welk voegwoord geeft een <b>tegenstelling</b> aan?",
      opties: ["omdat", "terwijl", "maar", "dus"],
      antwoord: 2,
      uitleg: "Het voegwoord <b>maar</b> geeft een tegenstelling aan.",
      hint: "Denk aan: 'Ik wil wel, ___ ik mag niet.'"
    },
    {
      type: "waaronwaar", niveau: 1,
      vraag: "De voegwoorden <b>omdat</b> en <b>want</b> betekenen allebei dat er een reden wordt gegeven.",
      antwoord: true,
      uitleg: "Ja! Beide voegwoorden geven een reden aan. Het verschil is alleen de woordvolgorde in de zin die erachter komt."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Welk voegwoord past hier het best? (kies uit: <i>hoewel</i>, <i>dus</i>, <i>terwijl</i>)<br>'Het is erg koud buiten, ___ trek ik een dikke jas aan.'",
      antwoord: "dus",
      uitleg: "Het trekken van een dikke jas is het <b>gevolg</b> van de kou. Daarom is <b>dus</b> het juiste voegwoord.",
      hint: "Geeft dit een gevolg, tegelijkertijd of een tegenwerping aan?"
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Welk voegwoord past hier het best? (kies uit: <i>hoewel</i>, <i>dus</i>, <i>terwijl</i>)<br>'Duru maakt haar huiswerk, ___ ze naar muziek luistert.'",
      antwoord: "terwijl",
      uitleg: "Het maken van huiswerk en het luisteren naar muziek gebeuren <b>tegelijkertijd</b>, dus gebruiken we <b>terwijl</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Welk voegwoord past hier het best? (kies uit: <i>hoewel</i>, <i>dus</i>, <i>terwijl</i>)<br>'Ik ga hardlopen, ___ het regent.'",
      antwoord: "hoewel",
      uitleg: "Het hardlopen gebeurt <b>ondanks</b> de regen. Daarom is <b>hoewel</b> het juiste voegwoord."
    },
    {
      type: "invoer", niveau: 1,
      vraag: "Welk leesteken hoort aan het eind van deze zin?<br>'Hoe laat begint de Nederlands-les'",
      antwoord: "?",
      uitleg: "Dit is een vraag, dus de zin moet eindigen met een <b>vraagteken (?)</b>."
    },
    {
      type: "invoer", niveau: 1,
      vraag: "Welk leesteken hoort aan het eind van deze zin?<br>'Pas op, die pan is heel heet'",
      antwoord: "!",
      uitleg: "Dit is een waarschuwing, dus de zin eindigt met een <b>uitroepteken (!)</b>."
    },
    {
      type: "waaronwaar", niveau: 2,
      vraag: "Voor het voegwoord <b>en</b> schrijf je meestal een komma.",
      antwoord: false,
      uitleg: "Onwaar: voor het voegwoord <i>en</i> schrijf je in de regel <b>geen komma</b>.",
      hint: "Denk aan de uitzonderingen van de komma-regels."
    },
    {
      type: "mc", niveau: 2,
      vraag: "Welke zin heeft de juiste interpunctie?",
      opties: [
        "Ik wil graag mee, maar ik heb geen geld.",
        "Ik wil graag mee maar ik heb geen geld.",
        "Ik wil graag mee, maar, ik heb geen geld."
      ],
      antwoord: 0,
      uitleg: "Er hoort een komma <b>voor</b> het voegwoord <i>maar</i>. Na het voegwoord schrijf je geen komma.",
      hint: "Waar hoort de komma bij het voegwoord 'maar'?"
    },
    {
      type: "waaronwaar", niveau: 2,
      vraag: "Een hoofdletter schrijf je aan het begin van de zin én bij namen.",
      antwoord: true,
      uitleg: "Ja, dit is correct! Hoofdletters gebruik je aan het begin van een zin en bij eigennamen (zoals Duru)."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Welk voegwoord geeft een <b>reden</b> aan en past in deze zin?<br>'Duru gaat vroeg slapen, ___ ze is erg moe.'",
      antwoord: "want",
      uitleg: "Zowel <i>want</i> als <i>omdat</i> geven een reden. Maar omdat de persoonsvorm (is) direct na het onderwerp (ze) staat, moeten we <b>want</b> gebruiken. (Bij <i>omdat</i> zou de zin zijn: 'omdat ze erg moe is'.)",
      hint: "Let op de woordvolgorde: '... ze is erg moe.' (onderwerp + persoonsvorm)."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Welk voegwoord geeft een <b>reden</b> aan en past in deze zin?<br>'Duru gaat vroeg slapen, ___ ze erg moe is.'",
      antwoord: "omdat",
      uitleg: "Het voegwoord <b>omdat</b> zorgt ervoor dat de persoonsvorm (is) helemaal aan het einde van de bijzin komt te staan.",
      hint: "Kijk naar de persoonsvorm 'is' aan het einde van de zin."
    },
    {
      type: "mc", niveau: 3,
      vraag: "Welke zin is grammaticaal en qua interpunctie helemaal correct?",
      opties: [
        "Hoewel Duru hard studeerde, vond ze de toets best moeilijk.",
        "Hoewel Duru hard studeerde vond ze de toets best moeilijk.",
        "hoewel Duru hard studeerde, vond ze de toets best moeilijk."
      ],
      antwoord: 0,
      uitleg: "De zin moet beginnen met een hoofdletter, en er hoort een komma tussen de twee zinsdelen (bijzin en hoofdzin): <b>Hoewel Duru hard studeerde, vond ze...</b>"
    },
    {
      type: "waaronwaar", niveau: 3,
      vraag: "In de zin: 'Ik ga naar school, dus ik leer veel.' geeft het voegwoord <i>dus</i> een <b>reden</b> aan.",
      antwoord: false,
      uitleg: "Onwaar: <i>dus</i> geeft een <b>gevolg</b> aan, geen reden."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Typ de hele zin correct over met de juiste hoofdletters, komma's en punt:<br>'duru vindt wiskunde leuk maar nederlands is haar favoriet'",
      antwoord: "Duru vindt wiskunde leuk, maar Nederlands is haar favoriet.",
      uitleg: "Namen (Duru, Nederlands) krijgen een hoofdletter. Er hoort een komma voor het voegwoord <i>maar</i>. De zin eindigt met een punt.",
      hint: "Let op: Duru en Nederlands zijn namen. Denk aan de komma voor 'maar' en de punt aan het eind."
    }
  ]
});
