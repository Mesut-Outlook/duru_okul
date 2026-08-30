/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toepassingen in Geneeskunde & Techniek
   ========================================================= */
DURU.register({
  "id": "h3-4-toepassingen",
  "hoofdstuk": 3,
  "paragraaf": "3.4",
  "titel": "Toepassingen in Geneeskunde & Techniek",
  "korteUitleg": "Tracers, radiotherapie, CT-scans, rookmelders, diktemeting en C-14 datering.",
  "icoon": "🔬",
  "kleur": "h3-thema",
  "theorie": "<h3>3.4 Straling gebruiken</h3><div class=\"formule-box\"><strong>Belangrijke toepassingen:</strong><br>• <b>Medische diagnose:</b> Tracers (kortlevende gammastralers, bijv. Tc-99m) + gammacamera, CT-scan.<br>• <b>Radiotherapie:</b> Gerichte bestraling van tumoren om kankercellen te doden.<br>• <b>Sterilisatie:</b> Gammastraling steriliseert medisch gereedschap door verpakking heen.<br>• <b>Industrie & Archeologie:</b> Diktemeting met $\\beta$-straling, C-14 datering ($t_{1/2} = 5730\\text{ j}$).</div>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welk type ioniserende straling bestaat uit zware heliumkernen (2 protonen en 2 neutronen)?",
      "opties": [
        "Alfastraling (α)",
        "Bètastraling (β)",
        "Gammastraling (γ)",
        "Röntgenstraling"
      ],
      "antwoord": 0,
      "uitleg": "Alfadeeltjes zijn helium-4 kernen."
    },
    {
      "type": "mc",
      "vraag": "Welk materiaal is al voldoende om alfastraling (α) volledig tegen te houden?",
      "opties": [
        "Een dikke plaat lood van 10 cm",
        "Een enkel velletje papier of de bovenste dode huidlaag",
        "Een betonnen bunker",
        "Een stalen kluis"
      ],
      "antwoord": 1,
      "uitleg": "Alfastraling heeft een zeer klein doordringend vermogen (stopt bij papier)."
    },
    {
      "type": "mc",
      "vraag": "Waaruit bestaat bètastraling (β)?",
      "opties": [
        "Elektromagnetische golven",
        "Heliumkernen",
        "Snelle elektronen",
        "Neutronen"
      ],
      "antwoord": 2,
      "uitleg": "Bètastraling bestaat uit met hoge snelheid weggeschoten elektronen."
    },
    {
      "type": "mc",
      "vraag": "Waarom is ioniserende straling gevaarlijk voor levende cellen?",
      "opties": [
        "Het verandert water in benzine",
        "Het maakt cellen direct radioactief",
        "Het koelt cellen af tot het vriespunt",
        "Het kan DNA-moleculen in cellen beschadigen en mutaties veroorzaken"
      ],
      "antwoord": 3,
      "uitleg": "Ioniserende straling kan atomen ioniseren en DNA beschadigen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Gammastraling heeft geen massa en geen elektrische lading.",
      "antwoord": true,
      "uitleg": "Waar: gammastraling bestaat uit fotonen (energiepakketjes)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Besmetting met een radioactieve stof is hetzelfde als bestraling van buitenaf.",
      "antwoord": false,
      "uitleg": "Onwaar: bij bestraling vang je straling op; bij besmetting zit de radioactieve bron OP of IN je lichaam."
    },
    {
      "type": "invoer",
      "vraag": "In welke eenheid wordt de effectieve stralingsdosis voor de mens uitgedrukt?",
      "antwoord": "Sievert|Sv|mSv",
      "uitleg": "Dosis wordt gemeten in Sievert (Sv)."
    },
    {
      "type": "invoer",
      "vraag": "Met welk meettoestel kun je ioniserende straling aantonen en 'klikjes' horen?",
      "antwoord": "Geiger-Müller-teller|geigerteller|GM-teller",
      "uitleg": "Een Geigerteller detecteert stralingsdeeltjes."
    }
  ]
});
