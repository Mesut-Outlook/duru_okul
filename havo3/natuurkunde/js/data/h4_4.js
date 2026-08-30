/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Soortelijke Weerstand (R = ρ · l / A)
   ========================================================= */
DURU.register({
  "id": "h4-4-soortelijke-weerstand",
  "hoofdstuk": 4,
  "paragraaf": "4.4",
  "titel": "Soortelijke Weerstand (R = ρ · l / A)",
  "korteUitleg": "Bereken de weerstand van stroomdraden uit lengte, dikte en materiaalsoort.",
  "icoon": "📏",
  "kleur": "h4-thema",
  "theorie": "<h3>4.4 Soortelijke weerstand</h3><div class='formule-box'><strong>Draadweerstand formule:</strong><br>R = (ρ × l) / A<br><br>• R = weerstand in <b>Ohm (Ω)</b><br>• ρ (rho) = soortelijke weerstand in Ω·mm²/m (koper: 0,017; constantaan: 0,45)<br>• l = lengte van de draad in <b>meter (m)</b><br>• A = doorsnede (oppervlakte) in <b>mm²</b></div><h4>Eigenschappen</h4><ul><li>Draad 2× zo lang -> R wordt 2× zo groot (R ~ l).</li><li>Draad 2× zo dik (A) -> R wordt 2× zo klein (R ~ 1/A).</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat zegt de wet van Boyle over een opgesloten hoeveelheid gas bij constante temperatuur?",
      "opties": [
        "Druk en volume zijn omgekeerd evenredig: p × V = constant",
        "Druk en volume zijn recht evenredig",
        "Als het volume halveert, halveert de druk ook",
        "Gas heeft geen druk"
      ],
      "antwoord": 0,
      "uitleg": "Boyle: p1 × V1 = p2 × V2."
    },
    {
      "type": "mc",
      "vraag": "Wat is de gemiddelde luchtdruk op zeeniveau op aarde?",
      "opties": [
        "100 Pa",
        "Ongeveer 1013 hPa (1 bar of 101.300 Pa)",
        "10 bar",
        "0 Pa"
      ],
      "antwoord": 1,
      "uitleg": "Standaard atmosferische druk = 1013 hPa = 1,013 bar."
    },
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je voor druk?",
      "opties": [
        "p = A / F",
        "p = F × A",
        "p = F / A",
        "p = m × g"
      ],
      "antwoord": 2,
      "uitleg": "Druk (p) = Kracht (F) / Oppervlakte (A)."
    },
    {
      "type": "mc",
      "vraag": "Waarom zijn damesschoenen met naaldhakken schadelijker voor een houten vloer dan de platte voeten van een zware olifant?",
      "opties": [
        "Omdat hout niet tegen leer kan",
        "Omdat een vrouw zwaarder is dan een olifant",
        "Omdat hakken van staal zijn",
        "Omdat het contactoppervlak van de hak miniem klein is, waardoor de druk (F/A) extreem hoog wordt"
      ],
      "antwoord": 3,
      "uitleg": "Klein oppervlak A geeft een gigantische druk p = F/A."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je een afgesloten spuit met lucht indrukt tot het halve volume, wordt de luchtdruk binnenin twee keer zo hoog.",
      "antwoord": true,
      "uitleg": "Waar: volgens de wet van Boyle verdubbelt de druk bij halvering van het volume."
    },
    {
      "type": "waaronwaar",
      "vraag": "Op grote hoogte in de bergen is de luchtdruk hoger dan op zeeniveau.",
      "antwoord": false,
      "uitleg": "Onwaar: hoe hoger je komt, hoe minder lucht erboven drukt, dus hoe lager de atmosferische druk."
    },
    {
      "type": "invoer",
      "vraag": "Met welk meetinstrument meet je de luchtdruk van het weer?",
      "antwoord": "barometer",
      "uitleg": "Een barometer meet luchtdruk."
    },
    {
      "type": "invoer",
      "vraag": "Als een kracht van 600 N werkt op een oppervlak van 2 m², wat is de druk in N/m² (Pascal)?",
      "antwoord": "300|300 Pa|300 N/m2",
      "uitleg": "p = F / A = 600 / 2 = 300 Pa."
    }
  ]
});
