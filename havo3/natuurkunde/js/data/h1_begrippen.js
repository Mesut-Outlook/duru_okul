/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Kernbegrippen & Formules (§1.1 t/m §1.3)
   ========================================================= */
DURU.register({
  "id": "h1-begrippen",
  "hoofdstuk": 1,
  "paragraaf": "1.0",
  "titel": "Kernbegrippen & Formules (§1.1 t/m §1.3)",
  "korteUitleg": "Volledig overzicht van definities, eenheden, formules en wetten van paragraaf 1.1, 1.2 en 1.3.",
  "icoon": "🔑",
  "kleur": "h1-thema",
  "theorie": "<h3>Kernbegrippen & Formules — Hoofdstuk 1 (§1.1, §1.2 & §1.3)</h3>\n<p>Dit overzicht bevat alle essentiële theorie, definities, formules en rekenregels uit de eerste drie paragrafen van <i>Overal Natuurkunde 3 HAVO</i>. Leer deze begrippen grondig voor de toetsen!</p>\n\n<div class=\"formule-box\">\n  <strong>Belangrijkste Formules & Rekenregels:</strong><br>\n  • <b>Gemiddelde snelheid:</b> v<sub>gem</sub> = s/t &nbsp;|&nbsp; s = v<sub>gem</sub> · t &nbsp;|&nbsp; t = s/v<sub>gem</sub><br>\n  • <b>Eenheden omrekenen:</b> van km/h naar m/s deel je door 3,6. Van m/s naar km/h vermenigvuldig je met 3,6.<br>\n  • <b>Versnelling:</b> a = (Δv)/(Δt) = (v<sub>eind</sub> - v<sub>begin</sub>)/t (in m/s²)<br>\n  • <b>Tweede wet van Newton:</b> F<sub>res</sub> = m · a &nbsp;|&nbsp; m = F<sub>res</sub>/a &nbsp;|&nbsp; a = F<sub>res</sub>/m<br>\n  • <b>Resulterende kracht:</b> krachten in dezelfde richting optellen (F<sub>res</sub> = F<sub>1</sub> + F<sub>2</sub>), in tegengestelde richting aftrekken (F<sub>res</sub> = F<sub>vooruit</sub> - F<sub>tegen</sub>).\n</div>\n\n<h4>1. Grootheden, Symbolen en SI-Eenheden</h4>\n<table class=\"nask\" style=\"width:100%; border-collapse: collapse; margin: 12px 0;\">\n  <thead>\n    <tr style=\"background: var(--grijs-licht, #f1f5f9); text-align: left;\">\n      <th style=\"padding: 6px;\">Grootheid</th>\n      <th style=\"padding: 6px;\">Symbool</th>\n      <th style=\"padding: 6px;\">Standaard SI-eenheid</th>\n      <th style=\"padding: 6px;\">Andere gebruikte eenheid</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr><td style=\"padding: 6px;\">Afstand / Verplaatsing</td><td style=\"padding: 6px;\"><b>s</b></td><td style=\"padding: 6px;\">meter (m)</td><td style=\"padding: 6px;\">kilometer (km)</td></tr>\n    <tr><td style=\"padding: 6px;\">Tijd</td><td style=\"padding: 6px;\"><b>t</b></td><td style=\"padding: 6px;\">seconde (s)</td><td style=\"padding: 6px;\">uur (h), minuut (min)</td></tr>\n    <tr><td style=\"padding: 6px;\">Snelheid</td><td style=\"padding: 6px;\"><b>v</b></td><td style=\"padding: 6px;\">meter per seconde (m/s)</td><td style=\"padding: 6px;\">kilometer per uur (km/h)</td></tr>\n    <tr><td style=\"padding: 6px;\">Versnelling</td><td style=\"padding: 6px;\"><b>a</b></td><td style=\"padding: 6px;\">meter per seconde kwadraat (m/s²)</td><td style=\"padding: 6px;\">-</td></tr>\n    <tr><td style=\"padding: 6px;\">Massa</td><td style=\"padding: 6px;\"><b>m</b></td><td style=\"padding: 6px;\">kilogram (kg)</td><td style=\"padding: 6px;\">gram (g)</td></tr>\n    <tr><td style=\"padding: 6px;\">Kracht</td><td style=\"padding: 6px;\"><b>F</b></td><td style=\"padding: 6px;\">Newton (N)</td><td style=\"padding: 6px;\">kilonewton (kN)</td></tr>\n  </tbody>\n</table>\n\n<h4>2. Bewegingssoorten & Diagrammen</h4>\n<ul>\n  <li><b>Eenparige beweging:</b> De snelheid is constant (a = 0). In het (s,t)-diagram is dit een rechte schuine lijn; in het (v,t)-diagram een rechte horizontale lijn.</li>\n  <li><b>Eenparig versnelde beweging:</b> De snelheid neemt iedere seconde met een vaste hoeveelheid toe (a is constant positief). In het (s,t)-diagram een steeds steiler wordende kromme; in het (v,t)-diagram een rechte stijgende lijn.</li>\n  <li><b>Eenparig vertraagde beweging:</b> De snelheid neemt iedere seconde met een vaste hoeveelheid af (a is constant negatief). In het (s,t)-diagram vlakt de lijn af; in het (v,t)-diagram een rechte dalende lijn.</li>\n  <li><b>Helling in (s,t)-diagram:</b> De steilheid geeft de snelheid aan. Horizontaal betekent stilstand (v = 0).</li>\n  <li><b>Oppervlakte in (v,t)-diagram:</b> De oppervlakte onder de grafiek is gelijk aan de afgelegde afstand (s). Voor een rechthoek s = v · t, voor een driehoek s = 0,5 · v<sub>top</sub> · t.</li>\n</ul>\n\n<h4>3. Krachten & De Wetten van Newton</h4>\n<div class=\"begrippen-box\">\n  <b>Kernbegrippen:</b>\n  <ul>\n    <li><b>Resulterende kracht (F<sub>res</sub>):</b> De somkracht die alle op een voorwerp werkende krachten vervangt. Als F<sub>res</sub> = 0 N, heffen de krachten elkaar op en verandert de snelheid niet (Eerste wet van Newton).</li>\n    <li><b>Tweede wet van Newton:</b> Een resulterende kracht veroorzaakt een versnelling (F<sub>res</sub> = m · a). Hoe groter de massa, des te meer kracht er nodig is voor dezelfde versnelling.</li>\n    <li><b>Traagheid (inertie):</b> De natuurlijke eigenschap van massa waardoor een voorwerp zich verzet tegen verandering van beweging of richting.</li>\n    <li><b>Tegenwerkende krachten:</b> Bij beweging spelen <i>rolweerstand</i> (vervorming van banden/wegdek) en <i>luchtweerstand</i> (botsing met luchtdeeltjes) een centrale rol. Luchtweerstand stijgt kwadratisch met de snelheid!</li>\n  </ul>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "niveau": 1,
      "vraag": "Wat is de officiële SI-eenheid van versnelling?",
      "opties": [
        "m/s²",
        "m/s",
        "km/h",
        "Newton"
      ],
      "antwoord": 0,
      "uitleg": "De eenheid van versnelling is m/s² (meter per seconde kwadraat)."
    },
    {
      "type": "mc",
      "niveau": 1,
      "vraag": "Wat stelt de oppervlakte onder de grafieklijn voor in een (v,t)-diagram?",
      "opties": [
        "De versnelling",
        "De afgelegde afstand",
        "De resulterende kracht",
        "De massa"
      ],
      "antwoord": 1,
      "uitleg": "Oppervlakte in een (v,t)-diagram = snelheid × tijd = afstand in meters."
    },
    {
      "type": "mc",
      "niveau": 2,
      "vraag": "Hoe groot is de resulterende kracht op een fietser die met een constante snelheid van 20 km/h fietst?",
      "opties": [
        "20 N",
        "Afhankelijk van zijn massa",
        "Exact 0 N",
        "Gelijk aan de zwaartekracht"
      ],
      "antwoord": 2,
      "uitleg": "Bij constante snelheid is er geen versnelling, dus Fres = 0 N."
    },
    {
      "type": "mc",
      "niveau": 2,
      "vraag": "Hoe reken je een snelheid in km/h om naar m/s?",
      "opties": [
        "Vermenigvuldigen met 3,6",
        "Delen door 60",
        "Vermenigvuldigen met 10",
        "Delen door 3,6"
      ],
      "antwoord": 3,
      "uitleg": "Omrekenen van km/h naar m/s doe je door te delen door 3,6."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een (s,t)-diagram betekent een horizontale rechte lijn dat het voorwerp stilstaat.",
      "antwoord": true,
      "uitleg": "Waar. De afstand s verandert niet in de tijd, dus v = 0 m/s."
    },
    {
      "type": "waaronwaar",
      "vraag": "Volgens F<sub>res</sub> = m · a levert een twee keer zo grote massa bij gelijke kracht een twee keer zo grote versnelling op.",
      "antwoord": false,
      "uitleg": "Niet waar. Meer massa betekent meer traagheid, dus juist een twee keer zo kleine versnelling."
    },
    {
      "type": "invoer",
      "niveau": 1,
      "vraag": "Reken om: 72 km/h is gelijk aan hoeveel m/s? Vul alleen het getal in.",
      "antwoord": "20|20,0",
      "uitleg": "72 / 3,6 = 20 m/s."
    },
    {
      "type": "invoer",
      "niveau": 2,
      "vraag": "Een voorwerp met een massa van 5 kg versnelt met 3 m/s². Hoe groot is de resulterende kracht in Newton? Vul alleen het getal in.",
      "antwoord": "15|15,0",
      "uitleg": "Fres = m × a = 5 × 3 = 15 N."
    }
  ]
});
