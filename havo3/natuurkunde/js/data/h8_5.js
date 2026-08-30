/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Vloeistofdruk & Hydraulica
   ========================================================= */
DURU.register({
  "id": "h8-5-vloeistofdruk",
  "hoofdstuk": 8,
  "paragraaf": "8.5",
  "titel": "Vloeistofdruk & Hydraulica",
  "korteUitleg": "De Wet van Pascal, werking van hydraulische persen, krikken en voertuigremmen.",
  "icoon": "💧",
  "kleur": "h8-thema",
  "theorie": "<h3>8.5 Vloeistofdruk en hydraulica</h3><div class='formule-box'><strong>De Wet van Pascal:</strong><br>In een afgesloten vloeistofsysteem plant een uitgeoefende druk zich in alle richtingen gelijkmatig voort.<br><br>89565p = \frac{F_1}{A_1} = \frac{F_2}{A_2} implies F_2 = F_1 \times \frac{A_2}{A_1}89565</div><h4>Eigenschappen van hydraulische systemen</h4><ul><li>Vloeistoffen (zoals hydraulische olie) zijn <b>niet samendrukbaar</b>.</li><li>Als zuiger 2 een 0\times$ groter oppervlak heeft ( = 10 \times A_1$), levert het een 0\times$ grotere kracht ( = 10 \times F_1$).</li><li>Volgens de Gouden Regel verplaatst zuiger 2 zich dan wel 0\times$ minder ver ( = s_1 / 10$).</li><li>Toepassingen: autoremmen, hydraulische krik, graafmachines, laadkleppen.</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat stelt de wet van behoud van energie?",
      "opties": [
        "Energie kan niet ontstaan of verloren gaan, alleen van vorm veranderen",
        "Energie verdwijnt vanzelf in de ruimte",
        "Energie kan gratis worden opgewekt",
        "Energie is altijd nul"
      ],
      "antwoord": 0,
      "uitleg": "De totale energie in een gesloten systeem is constant."
    },
    {
      "type": "mc",
      "vraag": "Welke energieomzetting vindt plaats in een zonnecel?",
      "opties": [
        "Chemische energie naar kernenergie",
        "Stralingsenergie van licht wordt omgezet in elektrische energie",
        "Warmte naar zwaarte-energie",
        "Magnetische energie naar kinetische energie"
      ],
      "antwoord": 1,
      "uitleg": "Zonnecellen zetten licht direct om in elektriciteit."
    },
    {
      "type": "mc",
      "vraag": "Welke energieomzetting vindt plaats in de spieren van een wielrenner?",
      "opties": [
        "Stralingsenergie naar hoogte",
        "Kernenergie naar elektriciteit",
        "Chemische energie uit voedsel wordt omgezet in bewegingsenergie en warmte",
        "Elektrische energie naar magnetisme"
      ],
      "antwoord": 2,
      "uitleg": "Spieren verbranden glucose (chemisch) tot arbeid en lichaamswarmte."
    },
    {
      "type": "mc",
      "vraag": "Wat is een energiediagram (Sankey-diagram)?",
      "opties": [
        "Een plattegrond van een fabriek",
        "Een cirkeldiagram van batterijen",
        "Een grafiek van spanning tegen stroom",
        "Een stroomdiagram waarin de breedte van de pijlen de hoeveelheid energie per soort weergeeft"
      ],
      "antwoord": 3,
      "uitleg": "In een Sankey-diagram toont de pijlbreedte de energiestromen (nuttig vs verlies)."
    },
    {
      "type": "waaronwaar",
      "question": "Bij elke reële energieomzetting ontstaat altijd een deel warmteverlies door wrijving of weerstand.",
      "antwoord": true,
      "uitleg": "Waar: 100% nuttig rendement is in de praktijk onhaalbaar."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een dynamo zet elektrische energie om in bewegingsenergie.",
      "antwoord": false,
      "uitleg": "Onwaar: een dynamo zet BEWEGINGSENERGIE om in ELEKTRISCHE ENERGIE (een elektromotor doet het omgekeerde)."
    },
    {
      "type": "invoer",
      "vraag": "Hoe noem je de energie die zit opgeslagen in moleculen van voedsel en brandstoffen zoals benzine?",
      "antwoord": "chemische energie",
      "uitleg": "Chemische energie zit in chemische bindingen."
    },
    {
      "type": "invoer",
      "vraag": "Als 100 J zonne-energie op een zonnepaneel valt en er ontstaat 22 J elektriciteit, hoeveel Joule warmteverlies ontstaat er dan?",
      "antwoord": "78|78 J|78 Joule",
      "uitleg": "100 - 22 = 78 Joule."
    }
  ]
});
