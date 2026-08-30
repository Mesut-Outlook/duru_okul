/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Lading, Spanning & Stroomkring
   ========================================================= */
DURU.register({
  "id": "h2-1-lading-spanning",
  "hoofdstuk": 2,
  "paragraaf": "2.1",
  "titel": "Lading, Spanning & Stroomkring",
  "korteUitleg": "Elektrische lading, statische elektriciteit, spanning (V), stroomsterkte (A) en meters aansluiten.",
  "icoon": "🔋",
  "kleur": "h2-thema",
  "theorie": "<h3>2.1 Elektriciteit en lading</h3><div class=\"formule-box\"><strong>Grootheden en eenheden:</strong><br>• <b>Spanning (U):</b> in <b>Volt (V)</b> — 'energie meegegeven aan de lading'<br>• <b>Stroomsterkte (I):</b> in <b>Ampère (A)</b> of <b>milliampère (mA)</b> — 1 A = 1000 mA</div><h4>Lading en krachten</h4><ul><li>Gelijksoortige ladingen stoten elkaar af (+ en + of - en -).</li><li>Ongelijksoortige ladingen trekken elkaar aan (+ en -).</li><li>Stroom in metaaldraden bestaat uit bewegende <b>negatieve elektronen</b>.</li></ul><h4>Meetinstrumenten aansluiten</h4><ul><li><b>Stroommeter (Ampèremeter):</b> Altijd <b>IN SERIE</b> geschakeld (zeer lage weerstand).</li><li><b>Spanningsmeter (Voltmeter):</b> Altijd <b>PARALLEL</b> over het onderdeel (zeer hoge weerstand).</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke deeltjes verplaatsen zich door een koperdraad wanneer er elektrische stroom vloeit?",
      "opties": [
        "Vrije elektronen",
        "Protonen",
        "Neutronen",
        "Atomen"
      ],
      "antwoord": 0,
      "uitleg": "Elektrische stroom is de gerichte stroom van vrije elektronen."
    },
    {
      "type": "mc",
      "vraag": "Wat is de eenheid van elektrische stroomsterkte?",
      "opties": [
        "Volt (V)",
        "Ampère (A)",
        "Ohm (Ω)",
        "Watt (W)"
      ],
      "antwoord": 1,
      "uitleg": "Stroomsterkte meet je in Ampère."
    },
    {
      "type": "mc",
      "vraag": "Hoe sluit je een stroommeter (ampèremeter) aan in een schakeling?",
      "opties": [
        "Direct tussen plus en min van de bron",
        "Parallel over het onderdeel",
        "In serie met het onderdeel",
        "Buiten de stroomkring"
      ],
      "antwoord": 2,
      "uitleg": "Een ampèremeter staat altijd in serie."
    },
    {
      "type": "mc",
      "vraag": "Wat levert een batterij in een gesloten stroomkring?",
      "opties": [
        "Koude lucht",
        "Neutronen aan de schakeling",
        "Magnetische golven",
        "Elektrische spanning die de lading rondpompt"
      ],
      "antwoord": 3,
      "uitleg": "De spanningsbron levert de 'druk' (spanning) om lading te verplaatsen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Twee gelijksoortig geladen voorwerpen (bijv. beide positief) trekken elkaar krachtig aan.",
      "antwoord": false,
      "uitleg": "Onwaar: gelijke ladingen stoten elkaar af; tegengestelde ladingen trekken elkaar aan."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een open stroomkring kan er geen elektrische stroom lopen.",
      "antwoord": true,
      "uitleg": "Waar: alleen een gesloten kring geleidt stroom."
    },
    {
      "type": "invoer",
      "vraag": "Met welk meetinstrument meet je de elektrische spanning over een lampje?",
      "antwoord": "voltmeter|spanningsmeter",
      "uitleg": "Spanning meet je met een voltmeter."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de eenheid van elektrische spanning?",
      "antwoord": "Volt|V",
      "uitleg": "Spanning wordt gemeten in Volt (V)."
    }
  ]
});
