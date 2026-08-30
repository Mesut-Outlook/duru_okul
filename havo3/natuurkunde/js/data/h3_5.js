/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Kernenergie, Kernsplijting & Reactor
   ========================================================= */
DURU.register({
  "id": "h3-5-kerncentrale",
  "hoofdstuk": 3,
  "paragraaf": "3.5",
  "titel": "Kernenergie, Kernsplijting & Reactor",
  "korteUitleg": "Kernsplijting van Uranium-235, kettingreacties, regelstaven, moderator en kernafval.",
  "icoon": "🏭",
  "kleur": "h3-thema",
  "theorie": "<h3>3.5 De kerncentrale</h3><div class=\"formule-box\"><strong>Kernsplijting (Uranium-235):</strong><br>Neutron + U-235 → 2 dochterkernen + 2 à 3 snelle neutronen + <b>warmte</b>.<br><br><strong>Onderdelen kernreactor:</strong><br>• <b>Splijtstofstaven:</b> Bevatten uraniumbrandstof.<br>• <b>Regelstaven:</b> Vangen neutronen weg om de kettingreactie te regelen/stoppen.<br>• <b>Moderator (water/grafiet):</b> Remt snelle neutronen af.<br>• <b>Turbine & Generator:</b> Stoom drijft turbine aan, generator wekt stroom op.</div>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent de halveringstijd (T½) van een radioactieve isotoop?",
      "opties": [
        "De tijd waarin de helft van de radioactieve kernen vervalt",
        "De tijd totdat de straling compleet verdwenen is",
        "De levensduur van een kerncentrale",
        "De tijd die nodig is om een atoom te splitsen"
      ],
      "antwoord": 0,
      "uitleg": "Na één halveringstijd is nog 50% van de moederkernen over."
    },
    {
      "type": "mc",
      "vraag": "Een radioactieve bron heeft een activiteit van 800 Bq. De halveringstijd is 6 uur. Wat is de activiteit na 18 uur?",
      "opties": [
        "200 Bq",
        "100 Bq",
        "400 Bq",
        "50 Bq"
      ],
      "antwoord": 1,
      "uitleg": "18 uur = 3 periodes: 800 -> 400 -> 200 -> 100 Bq."
    },
    {
      "type": "mc",
      "vraag": "Welke eenheid geeft het aantal kernvervallen per seconde aan (activiteit van de bron)?",
      "opties": [
        "Gray (Gy)",
        "Sievert (Sv)",
        "Becquerel (Bq)",
        "Joule (J)"
      ],
      "antwoord": 2,
      "uitleg": "1 Becquerel = 1 vervallende atoomkern per seconde."
    },
    {
      "type": "mc",
      "vraag": "Waarom worden in de medische diagnostiek (zoals bij PET-scans) radioactieve stoffen met een KORTE halveringstijd gebruikt?",
      "opties": [
        "Omdat ze licht geven in het donker",
        "Omdat lange halveringstijden verboden zijn",
        "Omdat korte stoffen goedkoper zijn",
        "Zodat de patiënt na het onderzoek snel weer stralingsvrij is"
      ],
      "antwoord": 3,
      "uitleg": "Korte halveringstijd minimaliseert de totale stralingsbelasting voor de patiënt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Na twee halveringstijden is een radioactieve stof voor 100% verdwenen.",
      "antwoord": false,
      "uitleg": "Onwaar: na 2 periodes is nog 25% (een kwart) over."
    },
    {
      "type": "waaronwaar",
      "vraag": "Radioactiviteit is een spontaan proces in onstabiele atoomkernen dat je met hitte of druk niet kunt versnellen of vertragen.",
      "antwoord": true,
      "uitleg": "Waar: kernverval verloopt volgens vaste kwantummechanische kansen."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de eenheid van radioactieve activiteit?",
      "antwoord": "Becquerel|Bq",
      "uitleg": "Activiteit meet je in Becquerel (Bq)."
    },
    {
      "type": "invoer",
      "vraag": "Als een monster 120 gram bevat en na 1 halveringstijd vervalt, hoeveel gram van de moederstof blijft over?",
      "antwoord": "60|60 gram|60 g",
      "uitleg": "120 / 2 = 60 gram."
    }
  ]
});
