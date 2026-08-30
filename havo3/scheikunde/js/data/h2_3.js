/* =========================================================
   Duru's Scheikunde (HAVO 3) — Chemische Formuletaal & Coëfficiënten
   ========================================================= */
DURU.register({
  "id": "sch-h2-3-formuletaal",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Chemische Formuletaal & Coëfficiënten",
  "korteUitleg": "Elementsymbolen, molecuulformules, index, coëfficiënt en de zeven twee-atomige elementen (BrINClHOF).",
  "icoon": "📝",
  "kleur": "h2-thema",
  "theorie": "<h3>2.3 Chemische Formuletaal</h3>\n<p>Om stoffen en chemische reacties wereldwijd eenduidig te noteren, gebruiken chemici een universele <b>formuletaal</b> met standaardsymbolen.</p>\n<h4>Elementsymbolen en Formules</h4>\n<ul>\n  <li>Elk scheikundig element heeft een uniek symbool: één hoofdletter (bijv. <b>C</b> voor koolstof, <b>O</b> voor zuurstof, <b>N</b> voor stikstof) of een hoofdletter gevolgd door een kleine letter (bijv. <b>Na</b> voor natrium, <b>Fe</b> voor ijzer, <b>Cl</b> voor chloor).</li>\n  <li><b>Elementaire stof:</b> Een stof waarvan de moleculen uit slechts <i>één enkele atoomsoort</i> bestaan (bijvoorbeeld O₂, Fe, S₈).</li>\n  <li><b>Verbinding:</b> Een stof waarvan de moleculen zijn opgebouwd uit <i>twee of meer verschillende atoomsoorten</i> (bijvoorbeeld H₂O, CO₂, C₆H₁₂O₆).</li>\n</ul>\n<h4>Index versus Coëfficiënt</h4>\n<div class=\"formule-box\">\n  Kijk goed naar het voorbeeld: <code>3 H₂O</code><br>\n  • <b>Index (het kleine cijfer rechtsonder, bijv. ₂):</b> Geeft aan hoeveel atomen van die specifieke atoomsoort in <i>één enkel molecuul</i> zitten. In één H₂O molecuul zitten 2 waterstofatomen en 1 zuurstofatoom.<br>\n  • <b>Coëfficiënt (het grote getal vóór de formule, bijv. 3):</b> Geeft aan hoeveel <i>losse moleculen</i> er zijn. In totaal heb je hier dus: <code>3 × 2 = 6</code> waterstofatomen en <code>3 × 1 = 3</code> zuurstofatomen.\n</div>\n<h4>De zeven twee-atomige elementen (BrINClHOF)</h4>\n<p>Zeven niet-metalen komen in de natuur als zuivere vrije stof NOOIT als losse atomen voor, maar altijd als <b>twee-atomige moleculen</b>. Onthoud het ezelsbruggetje <b>BrINClHOF</b>:</p>\n<p>• <b>Br₂</b> (broom), <b>I₂</b> (jood), <b>N₂</b> (stikstof), <b>Cl₂</b> (chloor), <b>H₂</b> (waterstof), <b>O₂</b> (zuurstof), <b>F₂</b> (fluor).</p>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Hoeveel zuurstofatomen zitten er in totaal in de notatie 4 CO₂?",
      "opties": [
        "8 atomen",
        "4 atomen",
        "2 atomen",
        "6 atomen"
      ],
      "antwoord": 0,
      "uitleg": "Coëfficiënt (4) vermenigvuldigen met de index van zuurstof (2) = 4 × 2 = 8 zuurstofatomen."
    },
    {
      "type": "mc",
      "vraag": "Welk ezelsbruggetje helpt je herinneren welke zeven elementen altijd als twee-atomige moleculen voorkomen?",
      "opties": [
        "KANO",
        "BrINClHOF",
        "VRIJE",
        "ROYGBIV"
      ],
      "antwoord": 1,
      "uitleg": "BrINClHOF staat voor Br₂, I₂, N₂, Cl₂, H₂, O₂ en F₂."
    },
    {
      "type": "waaronwaar",
      "vraag": "Water (H₂O) is een voorbeeld van een elementaire stof omdat het uit één soort vloeistof bestaat.",
      "antwoord": false,
      "uitleg": "Onwaar: water bestaat uit twee verschillende atoomsoorten (H en O) en is dus een chemische verbinding."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet het grote getal vóór een chemische formule dat het aantal moleculen aangeeft?",
      "antwoord": "coëfficiënt|coefficient",
      "uitleg": "De coëfficiënt geeft het aantal moleculen aan."
    },
    {
      "type": "mc",
      "vraag": "Wat is het verschil tussen CO en Co in de chemische notatie?",
      "opties": [
        "Er is geen enkel verschil",
        "CO is kobalt; Co is koper",
        "CO is koolstofmonoxide (verbinding); Co is het metaal kobalt (element)",
        "CO is vloeibaar; Co is gasvormig"
      ],
      "antwoord": 2,
      "uitleg": "Twee hoofdletters (CO) betekent twee atoomsoorten (C en O); één hoofdletter met kleine letter (Co) is het element kobalt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Stikstofgas in de lucht noteer je scheikundig altijd als N₂.",
      "antwoord": true,
      "uitleg": "Waar: stikstof hoort bij de BrINClHOF-groep en vormt twee-atomige moleculen."
    },
    {
      "type": "invoer",
      "vraag": "Hoe noem je het kleine verlaagde getal in een formule (zoals de 2 in H₂O)?",
      "antwoord": "index",
      "uitleg": "De index geeft het aantal atomen van die soort binnen één molecuul aan."
    },
    {
      "type": "waaronwaar",
      "vraag": "In 2 H₂SO₄ zitten in totaal 14 atomen.",
      "antwoord": true,
      "uitleg": "Waar: één molecuul H₂SO₄ telt 2+1+4 = 7 atomen. Met coëfficiënt 2 zijn dat 2 × 7 = 14 atomen."
    }
  ]
});
