/* =========================================================
   Duru's Wiskunde (HAVO 3) — Verhoudingstabel & Procenten
   ========================================================= */
DURU.register({
  "id": "h2-1-verhoudingstabel",
  "hoofdstuk": 2,
  "paragraaf": "2.1",
  "titel": "Verhoudingstabel & Procenten",
  "korteUitleg": "Rekenen met verhoudingen, kruislinks vermenigvuldigen en procentuele toename of afname.",
  "icoon": "✖️",
  "kleur": "blauw",
  "theorie": "<h3>2.1 Verhoudingstabel & Procenten</h3>\n<p>Een <b>verhoudingstabel</b> is een krachtig wiskundig hulpmiddel om evenredige verbanden overzichtelijk op te lossen. Bij een verhoudingstabel geldt de gouden regel: <i>wat je aan de bovenkant vermenigvuldigt of deelt, moet je aan de onderkant met exact hetzelfde getal vermenigvuldigen of delen</i>.</p>\n<h4>Kruislings vermenigvuldigen</h4>\n<p>In een tabel met 4 vakjes waarin 1 onbekende ($x$) staat, zijn de kruisproducten altijd aan elkaar gelijk:</p>\n<div class=\"formule-box\">\n  Als $\\frac{a}{b} = \\frac{c}{x}$, dan geldt: <code>a × x = b × c</code><br>\n  Dus: <code>x = (b × c) / a</code><br>\n  <i>Vuistregel: Vermenigvuldig de twee getallen die schuin tegenover elkaar staan en deel door het overgebleven getal!</i>\n</div>\n<h4>Procentuele toename en afname</h4>\n<p>Om te berekenen met hoeveel procent een hoeveelheid is gestegen of gedaald ten opzichte van de beginsituatie, gebruik je de standaardformule:</p>\n<div class=\"formule-box\">\n  <code>Procentuele verandering = ((Nieuw - Oud) / Oud) × 100%</code><br>\n  • Is de uitkomst <b>positief</b>? Dan is er sprake van een procentuele toename (stijging).<br>\n  • Is de uitkomst <b>negatief</b>? Dan is er sprake van een procentuele afname (daling of korting).\n</div>\n<h4>Rekenen met de groeifactor (vermenigvuldigingsfactor)</h4>\n<p>Bij een snelle berekening van een nieuw bedrag werk je met een factor:</p>\n<ul>\n  <li>Bij een <b>stijging van 6%</b>: factor = <code>1 + (6 / 100) = 1,06</code>. Nieuw bedrag = <code>Oud × 1,06</code>.</li>\n  <li>Bij een <b>korting van 15%</b>: factor = <code>1 - (15 / 100) = 0,85</code>. Nieuw bedrag = <code>Oud × 0,85</code>.</li>\n</ul>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een trui kost oorspronkelijk € 80 en wordt afgeprijsd naar € 60. Wat is het kortingspercentage?",
      "opties": [
        "25%",
        "20%",
        "33,3%",
        "15%"
      ],
      "antwoord": 0,
      "uitleg": "((60 - 80) / 80) × 100% = (-20 / 80) × 100% = -25% (dus 25% korting)."
    },
    {
      "type": "mc",
      "vraag": "Als 4 schriften samen € 6,00 kosten, hoeveel kosten 10 van dezelfde schriften?",
      "opties": [
        "€ 12,00",
        "€ 15,00",
        "€ 18,00",
        "€ 20,00"
      ],
      "antwoord": 1,
      "uitleg": "(10 × 6,00) / 4 = 60 / 4 = € 15,00."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een prijsstijging van 12% betekent dat je de oude prijs moet vermenigvuldigen met de factor 1,12.",
      "antwoord": true,
      "uitleg": "Waar: 100% + 12% = 112% = factor 1,12."
    },
    {
      "type": "invoer",
      "vraag": "Een bedrag van € 200 stijgt met 5%. Wat is het nieuwe bedrag in euro's?",
      "antwoord": "210|210 euro|€ 210|€210",
      "uitleg": "200 × 1,05 = € 210."
    },
    {
      "type": "mc",
      "vraag": "Wat is de groeifactor die hoort bij een afname van 18%?",
      "opties": [
        "0,18",
        "1,18",
        "0,82",
        "0,88"
      ],
      "antwoord": 2,
      "uitleg": "100% - 18% = 82% = factor 0,82."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij het berekenen van een procentuele verandering deel je het verschil altijd door de NIEUWE waarde.",
      "antwoord": false,
      "uitleg": "Niet waar: je deelt altijd door de OUDE (oorspronkelijke) waarde: (Nieuw - Oud) / Oud."
    },
    {
      "type": "invoer",
      "vraag": "Bereken x als geldt: 3 / 7 = 12 / x.",
      "antwoord": "28",
      "uitleg": "x = (7 × 12) / 3 = 84 / 3 = 28."
    },
    {
      "type": "waaronwaar",
      "vraag": "Eerst 10% erbij en daarna 10% eraf levert weer exact het oorspronkelijke beginbedrag op.",
      "antwoord": false,
      "uitleg": "Niet waar: 100 × 1,10 = 110. Vervolgens 110 × 0,90 = 99 (je houdt 1% minder over)."
    }
  ]
});
