/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Temperatuur & Soortelijke Warmte
   ========================================================= */
DURU.register({
  "id": "h4-2-soortelijke-warmte",
  "hoofdstuk": 4,
  "paragraaf": "4.2",
  "titel": "Temperatuur & Soortelijke Warmte",
  "korteUitleg": "Temperatuur (Celsius/Kelvin), warmtehoeveelheid (Q = m·c·ΔT) en soortelijke warmte.",
  "icoon": "🌡️",
  "kleur": "h4-thema",
  "theorie": "<h3>4.2 Soortelijke warmte</h3><div class='formule-box'><strong>Warmte berekenen:</strong><br>Q = m × c × ΔT<br><br>• Q = warmtehoeveelheid in <b>Joule (J)</b><br>• m = massa in kg (of gram)<br>• c = soortelijke warmte in J/(kg·K) (of J/(g·°C))<br>• ΔT = temperatuurverschil in K of °C<br><br><strong>Temperatuurschalen:</strong> T (in K) = T (in °C) + 273</div>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat stelt de wet van Archimedes over de opwaartse kracht op een ondergedompeld lichaam?",
      "opties": [
        "De opwaartse kracht is gelijk aan het gewicht van de verplaatste vloeistof",
        "De opwaartse kracht is gelijk aan het eigen gewicht van het voorwerp",
        "De opwaartse kracht is altijd nul",
        "De opwaartse kracht duwt het voorwerp omlaag"
      ],
      "antwoord": 0,
      "uitleg": "Fopw = gewicht van de verplaatste vloeistofmassa."
    },
    {
      "type": "mc",
      "vraag": "Wanneer zal een voorwerp in vloeistof zweven?",
      "opties": [
        "Als het voorwerp van hout is",
        "Wanneer de dichtheid van het voorwerp exact gelijk is aan die van de vloeistof",
        "Als de opwaartse kracht nul is",
        "Als het voorwerp zwaarder is dan lood"
      ],
      "antwoord": 1,
      "uitleg": "Zweven treedt op bij gelijke dichtheid (ρ_voorwerp = ρ_vloeistof)."
    },
    {
      "type": "mc",
      "vraag": "Waarom blijft een holle stalen boot van duizenden tonnen toch drijven?",
      "opties": [
        "Door de motoren",
        "Omdat staal lichter is dan water",
        "Omdat het totale gemiddelde volume veel lucht bevat, waardoor de gemiddelde dichtheid kleiner is dan water",
        "Omdat zout water geen zwaartekracht heeft"
      ],
      "antwoord": 2,
      "uitleg": "De holle vorm verplaatst heel veel water bij een relatief lage gemiddelde dichtheid."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de opwaartse kracht als een onderzeeër ballasttanks volpompt met water?",
      "opties": [
        "Er verandert niets",
        "De opwaartse kracht verdubbelt",
        "De onderzeeër schiet omhoog",
        "Het totale gewicht wordt groter dan de opwaartse kracht waardoor de onderzeeër zinkt"
      ],
      "antwoord": 3,
      "uitleg": "Zwaartekracht overtreft opwaartse kracht, waardoor de boot duikt."
    },
    {
      "type": "waaronwaar",
      "vraag": "In zout zeewater (dichtheid 1,03 g/cm³) blijft een mens makkelijker drijven dan in zoet zwembadwater.",
      "antwoord": true,
      "uitleg": "Waar: zout water heeft een grotere dichtheid en levert meer opwaartse kracht per liter verplaatst volume."
    },
    {
      "type": "waaronwaar",
      "vraag": "De opwaartse kracht op een zinkende stenen knikker wordt steeds kleiner naarmate hij dieper zinkt.",
      "antwoord": false,
      "uitleg": "Onwaar: zolang de knikker volledig ondergedompeld is, blijft het verplaatste watervolume gelijk en is Fopw constant."
    },
    {
      "type": "invoer",
      "vraag": "Welke natuurkundige ontdekte in zijn badkuip de opwaartse kracht en riep 'Eureka!'?",
      "antwoord": "Archimedes",
      "uitleg": "De Griekse geleerde Archimedes."
    },
    {
      "type": "invoer",
      "vraag": "Als een drijvende houten balk 4 kg weegt, hoeveel Newton bedraagt de opwaartse kracht dan in evenwicht (g = 10 N/kg)?",
      "antwoord": "40|40 N|40 Newton",
      "uitleg": "Bij drijven is Fopw = Fz = 4 × 10 = 40 N."
    }
  ]
});
