/* Onderwerp 2.2 — Weerstand */
DURU.register({
  id: "h2-2-weerstand-ohm",
  hoofdstuk: 2,
  paragraaf: "2.2",
  titel: "Weerstand & Wet van Ohm (R = U / I)",
  korteUitleg: "Weerstand berekenen in Ohm, ohmse weerstanden en factoren van draadweerstand.",
  icoon: "💡",
  kleur: "h2-thema",
  theorie: "<h3>2.2 Weerstand en de Wet van Ohm</h3><div class=\"formule-box\"><strong>Wet van Ohm:</strong><br>$R = \\frac{U}{I}$ &nbsp;&nbsp;|&nbsp;&nbsp; $U = I \\cdot R$ &nbsp;&nbsp;|&nbsp;&nbsp; $I = \\frac{U}{R}$<br><br>• $R$ = weerstand in <b>Ohm ($\\Omega$)</b><br>• $U$ = spanning in <b>Volt (V)</b><br>• $I$ = stroomsterkte in <b>Ampère (A)</b></div><h4>Factoren voor draadweerstand</h4><ul><li><b>Lengte ($l$):</b> Hoe langer de draad, hoe <b>groter</b> de weerstand ($R \\sim l$).</li><li><b>Doorsnede ($A$):</b> Hoe dikker de draad, hoe <b>kleiner</b> de weerstand ($R \\sim 1/A$).</li><li><b>Materiaal:</b> Bepaald door de soortelijke weerstand ($\\rho$). Koper heeft lage weerstand, constantaan een matige.</li><li><b>Temperatuur:</b> Bij de meeste metalen stijgt de weerstand als de draad warmer wordt (PTC).</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid van elektrische weerstand?",
      opties: ["Ohm", "Ampère", "Volt", "Joule"],
      antwoord: 0,
      uitleg: "Weerstand wordt gemeten in Ohm (Ω)."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Over een weerstand staat 24 V. De stroom is 2,0 A. Bereken de weerstand in Ohm.",
      antwoord: "12|12 Ω|12 ohm|12,0",
      uitleg: "R = U / I = 24 V / 2,0 A = 12 Ω."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een weerstand van 50 Ω is aangesloten op 230 V. Bereken de stroomsterkte in Ampère.",
      antwoord: "4,6|4,6 A|4,60",
      uitleg: "I = U / R = 230 V / 50 Ω = 4,6 A."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat gebeurt er met de weerstand van een draad als je hem twee keer zo lang maakt?",
      opties: ["Wordt 2× zo klein", "Wordt 2× zo groot", "Blijft gelijk", "Wordt 4× zo groot"],
      antwoord: 1,
      uitleg: "Weerstand is evenredig met de lengte: 2× zo lang = 2× zoveel weerstand."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een ohmse weerstand heeft in een (I,U)-diagram een rechte lijn door de oorsprong.",
      antwoord: true,
      uitleg: "Waar: bij een ohmse weerstand is R constant."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Door een weerstand van 2,5 kΩ (2500 Ω) loopt een stroom van 4,0 mA (0,004 A). Bereken de spanning in Volt.",
      antwoord: "10|10 V|10,0",
      uitleg: "U = I × R = 0,004 A × 2500 Ω = 10 V."
    }
  ]
});
