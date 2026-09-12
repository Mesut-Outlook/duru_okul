/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Serie- en Parallelschakelingen
   ========================================================= */
DURU.register({
  "id": "h2-3-serie-parallel",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Serie- en Parallelschakelingen",
  "korteUitleg": "Stroom- en spanningsverdeling, vervangingsweerstand en huisinstallaties.",
  "icoon": "🔌",
  "kleur": "h2-thema",
  "theorie": "<h3>2.3 Serie en parallel</h3><div class=\"formule-box\"><strong>Serieschakeling:</strong><br>• I<sub>tot</sub> = I<sub>1</sub> = I<sub>2</sub> = … (stroom overal gelijk)<br>• U<sub>tot</sub> = U<sub>1</sub> + U<sub>2</sub> + … (spanning verdeelt zich)<br>• R<sub>tot</sub> = R<sub>1</sub> + R<sub>2</sub> + … (weerstanden tellen op)<br><br><strong>Parallelschakeling:</strong><br>• U<sub>tot</sub> = U<sub>1</sub> = U<sub>2</sub> = … (spanning overal gelijk)<br>• I<sub>tot</sub> = I<sub>1</sub> + I<sub>2</sub> + … (hoofdstroom is som van takstromen)<br>• Totale weerstand daalt: 1/R<sub>tot</sub> = 1/R<sub>1</sub> + 1/R<sub>2</sub> of R<sub>tot</sub> = U/I<sub>tot</sub></div>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter (m) (bijv. 1 km = 1000 m, 1 cm = 0,01 m).</li>\n      <li>Tijd: altijd omrekenen naar seconden (s) (bijv. 1 uur = 3600 s, 1 min = 60 s).</li>\n      <li>Snelheid: van km/h naar m/s deel je door 3,6. Van m/s naar km/h vermenigvuldig je met 3,6.</li>\n      <li>Massa: in kilogram (kg) of gram (g) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat geldt voor de stroomsterkte in een serieschakeling?",
      "opties": [
        "De stroomsterkte is overal in de kring exact gelijk (Itot = I1 = I2)",
        "De stroom splitst zich over de lampjes",
        "De stroomsterkte is bij het laatste lampje nul",
        "De stroomsterkte verdubbelt bij elk lampje"
      ],
      "antwoord": 0,
      "uitleg": "In een onvertakte kring vloeit overal evenveel stroom."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de overige lampjes in een parallelschakeling als één lampje wordt losgedraaid?",
      "opties": [
        "Alle lampjes gaan direct uit",
        "De andere lampjes blijven gewoon branden",
        "De andere lampjes ontploffen",
        "De batterij raakt direct leeg"
      ],
      "antwoord": 1,
      "uitleg": "In een parallelschakeling heeft elke tak een eigen gesloten kring."
    },
    {
      "type": "mc",
      "vraag": "Twee weerstanden van 20 Ω en 30 Ω staan in serie. Wat is de totale vervangingsweerstand?",
      "opties": [
        "600 Ω",
        "12 Ω",
        "50 Ω",
        "10 Ω"
      ],
      "antwoord": 2,
      "uitleg": "In serie tel je weerstanden op: Rv = R1 + R2 = 20 + 30 = 50 Ω."
    },
    {
      "type": "mc",
      "vraag": "Welke schakeling wordt gebruikt voor stopcontacten in huis zodat elk apparaat 230 V krijgt?",
      "opties": [
        "Driefasenschakeling",
        "Serieschakeling",
        "Kortsluiting",
        "Parallelschakeling"
      ],
      "antwoord": 3,
      "uitleg": "Huisinstallaties zijn parallel geschakeld."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een parallelschakeling is de totale vervangingsweerstand altijd kleiner dan de kleinste individuele weerstand.",
      "antwoord": true,
      "uitleg": "Waar: parallel schakelen creëert extra stroompaden, waardoor de totale weerstand daalt."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een serieschakeling is de totale spanning gelijk aan de spanning van één enkel lampje.",
      "antwoord": false,
      "uitleg": "Onwaar: de bronspanning verdeelt zich over de serie-onderdelen (Utot = U1 + U2 + ...)."
    },
    {
      "type": "invoer",
      "vraag": "Hoeveel Volt staat over elk aangesloten apparaat op het Nederlandse lichtnet thuis?",
      "antwoord": "230|230 V|230 Volt",
      "uitleg": "De netspanning in Nederland is 230 Volt."
    },
    {
      "type": "invoer",
      "vraag": "Als een hoofdleiding 5 A levert en tak 1 vraagt 2 A, hoeveel Ampère vloeit dan door tak 2 in een parallelschakeling?",
      "antwoord": "3|3 A|3 Ampere",
      "uitleg": "Itot = I1 + I2 -> I2 = 5 - 2 = 3 A."
    }
  ]
});
