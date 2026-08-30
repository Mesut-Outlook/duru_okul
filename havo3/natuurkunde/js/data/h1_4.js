/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Veiligheid, Remweg & Stopafstand
   ========================================================= */
DURU.register({
  "id": "h1-4-veiligheid-verkeer",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Veiligheid, Remweg & Stopafstand",
  "korteUitleg": "Reactietijd, remweg, stopafstand en de werking van kreukelzones, airbags en gordels.",
  "icoon": "🚗",
  "kleur": "h1-thema",
  "theorie": "<h3>1.4 Veiligheidsmaatregelen in het verkeer</h3><div class=\"formule-box\"><strong>Stopafstand:</strong><br>s_stop = s_reactie + s_rem<br><br>• <b>Reactieafstand (s_reactie):</b> Afstand tijdens de reactietijd (t_r): s_reactie = v × t_r<br>• <b>Remweg (s_rem):</b> Afstand tijdens het remmen: s_rem = 0,5 × v × t_rem<br>• <b>Kwadratisch effect:</b> Als de snelheid <b>2×</b> zo groot wordt, wordt de remweg <b>4× (2²)</b> zo lang!</div><h4>Veiligheidsvoorzieningen</h4><p><b>Kreukelzone, gordel, airbag en helm</b> zorgen ervoor dat de <b>remtijd / botstijd (Δt)</b> wordt verlengd. Volgens F = m × (Δv / Δt) wordt de botskracht F daardoor aanzienlijk kleiner!</p>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de remweg van een auto als de beginsnelheid verdubbelt?",
      "opties": [
        "De remweg wordt 4 keer zo lang",
        "De remweg verdubbelt",
        "De remweg blijft gelijk",
        "De remweg halveert"
      ],
      "antwoord": 0,
      "uitleg": "Remweg is kwadratisch afhankelijk van de snelheid: 2² = 4× zo lang."
    },
    {
      "type": "mc",
      "vraag": "Waaruit bestaat de totale stopafstand van een voertuig?",
      "opties": [
        "Alleen de remweg",
        "Reactieafstand + remweg",
        "Reactietijd × remkracht",
        "Snelheid / vertraging"
      ],
      "antwoord": 1,
      "uitleg": "Stopafstand = reactieafstand (tijdens reactietijd) + remweg (tijdens remmen)."
    },
    {
      "type": "mc",
      "vraag": "Welke factor verlengt de reactietijd van een automobilist?",
      "opties": [
        "Versleten remblokken",
        "Een nat wegdek",
        "Afleiding door smartphonegebruik of vermoeidheid",
        "Een te lage bandenspanning"
      ],
      "antwoord": 2,
      "uitleg": "Afleiding en alcohol beïnvloeden de menselijke reactietijd."
    },
    {
      "type": "mc",
      "vraag": "Wat is de functie van een kreukelzone in een moderne auto?",
      "opties": [
        "De auto sneller laten optrekken",
        "De auto lichter maken",
        "Het brandstofverbruik verminderen",
        "De botsingstijd verlengen waardoor de botskracht op inzittenden afneemt"
      ],
      "antwoord": 3,
      "uitleg": "Door gecontroleerd in te deuken verlengt de kreukelzone de remtijd."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een nat of beijzeld wegdek verlengt de reactieafstand van de bestuurder.",
      "antwoord": false,
      "uitleg": "Onwaar: gladheid verlengt de REMWEG; de reactieafstand hangt alleen af van de bestuurder en rijsnelheid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Veiligheidsgordels voorkomen dat inzittenden bij een frontale botsing door de voorruit vliegen door de traagheid van hun lichaam.",
      "antwoord": true,
      "uitleg": "Waar: de gordel oefent een remkracht uit op het lichaam."
    },
    {
      "type": "invoer",
      "vraag": "Een auto rijdt 20 m/s en de reactietijd is 1,2 s. Bereken de reactieafstand in meters.",
      "antwoord": "24|24 m|24 meter",
      "uitleg": "s_reactie = v × t = 20 × 1,2 = 24 meter."
    },
    {
      "type": "invoer",
      "vraag": "Als de reactieafstand 15 m is en de remweg 35 m, wat is dan de totale stopafstand in meters?",
      "antwoord": "50|50 m|50 meter",
      "uitleg": "Stopafstand = 15 + 35 = 50 meter."
    }
  ]
});
