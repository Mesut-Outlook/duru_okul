/* =========================================================
   Duru's Natuurkunde (HAVO 3) — §7.2 Rekenen met energie
   ========================================================= */
DURU.register({
  "id": "h7-2-rekenen-met-energie",
  "hoofdstuk": 7,
  "paragraaf": "7.2",
  "titel": "Rekenen met energie",
  "korteUitleg": "Vermogen, de formule E = P·t, rendement en de wet van behoud van energie.",
  "icoon": "🧮",
  "kleur": "h7-thema",
  "theorie": "<h3>7.2 Rekenen met energie</h3>\n<p>De hoeveelheid energie die een apparaat per seconde omzet, noem je het <b>vermogen</b> van dat apparaat. De eenheid van vermogen is daarom joule per seconde (J/s), oftewel <b>watt (W)</b>. Met het vermogen kun je uitrekenen hoeveel energie een apparaat heeft omgezet. Op een energierekening staat de gebruikte hoeveelheid energie vaak in kilowattuur (kWh).</p>\n<div class='formule-box'>\n<b>E = P · t</b><br>\n<i>E</i> is de energie in joule (J) of kilowattuur (kWh)<br>\n<i>P</i> is het vermogen in watt (W) of kilowatt (kW)<br>\n<i>t</i> is de tijd in seconde (s) of uur (h)<br><br>\n<b>1 kWh = 1000 Wh = 1000 × 3600 Ws = 3.600.000 J</b>\n</div>\n<div class='voorbeeld'>\n<span class='vb-kop'>Voorbeeld: de elektrische auto</span>\n<div class='stap'>Een elektrische auto heeft een vermogen van 16.000 W en rijdt hiermee 15 minuten. Gegeven: P = 16.000 W = 16 kW; t = 15 min = 900 s = 0,25 h. Formule: E = P · t. In joule: E = 16.000 W × 900 s = 14.400.000 J = 14,4 MJ. In kWh: E = 16 kW × 0,25 h = 4,0 kWh.</div>\n</div>\n\n<h4>Rendement</h4>\n<p>Tot het begin van de twintigste eeuw werden voor verlichting kaarsen, olielampen en gaslampen gebruikt. De uitvinding van de elektrische gloeilamp bracht verandering: een dun draadje wordt heet doordat er stroom doorheen gaat, en gaat gloeien en licht geven. De warmte die in een gloeilamp ontstaat, is meestal niet nuttig. Later kwam de spaarlamp (minder warmte), en daarna de ledlamp (nauwelijks warm).</p>\n<p>Een ledlamp heeft een rendement van ongeveer 50%: slechts 50% van de energie die de ledlamp in totaal gebruikt, wordt daadwerkelijk omgezet in licht. De rest wordt omgezet in ongewenste energie (warmte). Een spaarlamp heeft een rendement van 35 tot 40%. Een gloeilamp heeft een rendement van slechts 5 tot 10%, de reden dat deze lamp in 2013 uit de handel is genomen.</p>\n<div class='formule-box'>\n<b>η = E<sub>nuttig</sub> / E<sub>totaal</sub> × 100%</b> &nbsp; of &nbsp; <b>η = P<sub>nuttig</sub> / P<sub>totaal</sub> × 100%</b><br>\n<i>η</i> is het rendement in procent (%) · <i>E<sub>nuttig</sub></i>/<i>P<sub>nuttig</sub></i> is de energie/het vermogen die nuttig wordt gebruikt · <i>E<sub>totaal</sub></i>/<i>P<sub>totaal</sub></i> is de energie/het vermogen die totaal wordt omgezet.\n</div>\n<div class='voorbeeld'>\n<span class='vb-kop'>Voorbeeld: rendement van een mixer</span>\n<div class='stap'>Een mixer gebruikt een totaal vermogen van 500 W. Voor het kloppen van 200 mL slagroom is 48 kJ energie nodig. De mixer doet hier 2 minuten over. Gegeven: P<sub>totaal</sub> = 500 W; E<sub>nuttig</sub> = 48 kJ = 48.000 J; t = 2 min = 120 s. Formule: P<sub>nuttig</sub> = E<sub>nuttig</sub>/t = 48.000/120 = 400 W. η = P<sub>nuttig</sub>/P<sub>totaal</sub> × 100% = 400/500 × 100% = 80%.</div>\n</div>\n\n<h4>Wet van behoud van energie</h4>\n<p>Een rendement van 100% is in de praktijk niet haalbaar. Er geldt de <b>wet van behoud van energie</b>: nuttige en ongewenste energie samen zijn evenveel als de totale gebruikte energie. Energie gaat nooit verloren; ze ontstaat niet en verdwijnt niet. Energie kun je alleen van de ene in een andere vorm omzetten. Het energieprobleem gaat dus niet over het produceren van energie, maar over het produceren van bruikbare energie (bijvoorbeeld elektriciteit of brandstof voor vervoer). Hoe hoger het rendement bij een energieomzetting, hoe minder energie er 'verloren' gaat als ongewenste energie.</p>\n<div class='voorbeeld'>\n<span class='vb-kop'>Voorbeeld: de kerncentrale</span>\n<div class='stap'>De kerncentrale in Borssele heeft een rendement van 35% en levert een nuttig vermogen van 455 MW. 455 MW is dan 35% van het totale vermogen: 1% is 455/35 ≈ 13 MW, dus het ongewenste vermogen (65%) is 65 × 13 = 845 MW. Over een etmaal (24 uur = 86.400 s) ontstaat er dus E<sub>ongewenst</sub> = 845 MW × 86.400 s = 73.008.000 MJ aan afvalwarmte. Het is mogelijk om een deel van deze warmte te gebruiken in een warmtenet (stadsverwarming); koppel je dat aan de kerncentrale, dan wordt het rendement hoger.</div>\n</div>\n<div class='begrippen-box'><b>Samengevat:</b> vermogen (P) is de energie die een apparaat per seconde gebruikt (1 W = 1 J/s). Energie bereken je met E = P·t. Rendement is dat deel van de energie dat wordt omgezet in nuttige energie: η = E<sub>nuttig</sub>/E<sub>totaal</sub> × 100%. Energie gaat niet verloren, ze wordt omgezet van de ene in een andere vorm.</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de eenheid van vermogen?",
      "opties": [
        "Joule (J)",
        "Watt (W)",
        "Kilowattuur (kWh)",
        "Newton (N)"
      ],
      "antwoord": 1,
      "uitleg": "Vermogen is energie per seconde, de eenheid is watt (W), gelijk aan J/s."
    },
    {
      "type": "mc",
      "vraag": "Een föhn heeft een vermogen van 1200 W en wordt 5 minuten (300 s) gebruikt. Hoeveel energie is dat in joule?",
      "opties": [
        "6000 J",
        "36.000 J",
        "360.000 J",
        "3.600.000 J"
      ],
      "antwoord": 2,
      "uitleg": "E = P · t = 1200 W × 300 s = 360.000 J."
    },
    {
      "type": "mc",
      "vraag": "Waarom is de gloeilamp in 2013 uit de handel genomen?",
      "opties": [
        "Omdat het rendement slechts 5 tot 10% is",
        "Omdat gloeilampen te veel licht geven",
        "Omdat gloeilampen geen warmte maken",
        "Omdat het rendement 100% is"
      ],
      "antwoord": 0,
      "uitleg": "Het lage rendement (5-10%) van de gloeilamp betekent dat het grootste deel van de energie als warmte verloren gaat."
    },
    {
      "type": "mc",
      "vraag": "Een apparaat gebruikt in totaal 800 J energie, waarvan 200 J nuttig wordt gebruikt. Wat is het rendement?",
      "opties": [
        "20%",
        "40%",
        "80%",
        "25%"
      ],
      "antwoord": 3,
      "uitleg": "η = Enuttig/Etotaal × 100% = 200/800 × 100% = 25%."
    },
    {
      "type": "mc",
      "vraag": "Welke uitspraak hoort bij de wet van behoud van energie?",
      "opties": [
        "Energie kan volledig verdwijnen bij een omzetting",
        "Rendement is altijd 100%",
        "Nuttige en ongewenste energie samen zijn evenveel als de totale gebruikte energie",
        "Energie kan alleen ontstaan, nooit verdwijnen"
      ],
      "antwoord": 2,
      "uitleg": "De wet van behoud van energie stelt dat energie niet verdwijnt maar alleen van vorm verandert; nuttige plus ongewenste energie is gelijk aan de totale energie."
    },
    {
      "type": "waaronwaar",
      "vraag": "1 kWh staat gelijk aan 3.600.000 joule.",
      "antwoord": true,
      "uitleg": "Waar: 1 kWh = 1000 Wh = 1000 × 3600 Ws = 3.600.000 J."
    },
    {
      "type": "waaronwaar",
      "vraag": "Hoe hoger het rendement van een energieomzetting, hoe meer energie er als ongewenste energie verloren gaat.",
      "antwoord": false,
      "uitleg": "Onwaar: een hoger rendement betekent juist dat er minder energie als ongewenste energie (meestal warmte) verloren gaat."
    },
    {
      "type": "invoer",
      "vraag": "Hoe noem je het deel van de energie dat wordt omgezet in nuttige energie, uitgedrukt in procenten?",
      "antwoord": "rendement",
      "uitleg": "Dit percentage heet het rendement."
    },
    {
      "type": "invoer",
      "vraag": "Een lamp heeft een vermogen van 10 W en brandt 2 uur (7200 s). Hoeveel energie gebruikt de lamp in joule? Vul alleen het getal in.",
      "antwoord": "72000|72.000",
      "uitleg": "E = P · t = 10 W × 7200 s = 72.000 J."
    }
  ]
});
