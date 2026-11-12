/* =========================================================
   Duru's Economie (HAVO 3) — Proeftoets 116: Reëel inkomen stap voor stap — plus of min?
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-economie-116",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Proeftoets 116: Reëel inkomen stap voor stap — plus of min?",
  "vak": "Economie · HAVO 3 (Pincode)",
  "icoon": "🧮",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de formule voor de procentuele verandering van het reëel inkomen?",
      "uitleg": "Je haalt het inflatiepercentage af van de procentuele verandering van het nominaal inkomen. Draai je het om, dan krijg je het verkeerde teken.",
      "opties": [
        "% verandering nominaal inkomen − inflatiepercentage",
        "% verandering nominaal inkomen × inflatiepercentage",
        "% verandering nominaal inkomen + inflatiepercentage",
        "inflatiepercentage − % verandering nominaal inkomen"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "In de cao van de supermarkt gaan de lonen 2% omhoog, terwijl alles in de winkel gemiddeld 5% duurder wordt. Hoe verandert het reëel inkomen van de vakkenvullers?",
      "uitleg": "2% − 5% = −3%. De prijzen stijgen harder dan de lonen, dus je kunt minder kopen: de uitkomst krijgt een min-teken.",
      "opties": [
        "Het stijgt met 7%, dus +7%",
        "Het blijft gelijk, want beide stijgen",
        "Het daalt met 3%, dus −3%",
        "Het stijgt met 3%, dus +3%"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Bij een tabel met cao-lonen en consumentenprijzen: in welk jaar daalde het reëel inkomen?\n2019: lonen +2,5%, prijzen +2,6% · 2020: lonen +3,0%, prijzen +1,3% · 2021: lonen +2,0%, prijzen +2,7%",
      "uitleg": "2019: 2,5 − 2,6 = −0,1%. 2020: 3,0 − 1,3 = +1,7%. 2021: 2,0 − 2,7 = −0,7%. Ook al stijgen de lonen, het reëel inkomen daalt als de prijzen nog harder stijgen.",
      "opties": [
        "In 2019 én 2021, want toen stegen de prijzen harder dan de lonen",
        "Alleen in 2021, want toen stegen de prijzen het hardst",
        "In geen enkel jaar, want de lonen stegen elk jaar",
        "Alleen in 2020, want toen stegen de lonen het hardst"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Zelfde tabel. In welk jaar steeg het reëel inkomen het meest?\n2019: lonen +2,5%, prijzen +2,6% · 2020: lonen +3,0%, prijzen +1,3% · 2021: lonen +2,0%, prijzen +2,7%",
      "uitleg": "Je kijkt niet naar het hoogste staafje, maar naar het verschil: lonen − prijzen. In 2020 is dat 3,0 − 1,3 = +1,7%, het grootste.",
      "opties": [
        "2019, want daar stegen de lonen en de prijzen bijna even hard",
        "2019, want daar was de prijsstijging het hoogste van alle jaren",
        "2020, want daar is het verschil lonen min prijzen het grootst (+1,7%)",
        "2021, want daar stegen de prijzen het hardst van de drie jaren"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Joost verdiende € 2.000 en nu € 2.060. De inflatie is 4%. Wat is de eerste stap?",
      "uitleg": "Stap 1: % verandering nominaal = (2.060 − 2.000) / 2.000 × 100% = 3%. Stap 2: 3% − 4% = −1%. Zijn koopkracht daalt met 1%.",
      "opties": [
        "Eerst de % verandering van zijn nominaal inkomen: 60 / 2.000 × 100% = 3%",
        "Eerst 4% bij € 2.000 optellen en dat is meteen zijn nieuwe reëel inkomen",
        "Eerst € 2.060 − € 2.000 = € 60 en dat is meteen de koopkrachtverandering",
        "Eerst 4% van € 2.060 afhalen en dat bedrag als koopkracht opschrijven"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "In een land in crisis krijgen werknemers 4% minder loon, maar de winkelprijzen zakken met 6%. Kunnen de werknemers nu meer of minder kopen?",
      "uitleg": "−4% − (−6%) = −4 + 6 = +2%. De prijzen dalen harder dan de lonen, dus je kunt meer kopen.",
      "opties": [
        "Minder: hun koopkracht daalt met 2%, want minder loon is altijd slechter",
        "Minder: hun koopkracht daalt met 10%, want loon en prijzen zakken",
        "Meer: hun koopkracht stijgt met 2%, want −4 − (−6) = +2",
        "Evenveel: loon en prijzen bewegen dezelfde kant op, dus er verandert niets"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Als het nominaal inkomen stijgt, stijgt de koopkracht altijd ook.",
      "antwoord": false,
      "uitleg": "Niet waar. Als je inkomen bijvoorbeeld 3% stijgt en de inflatie is 8%, ga je er in koopkracht op achteruit (3 − 8 = −5%)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een uitkomst van −1,5% bij de verandering van het reëel inkomen betekent dat je 1,5% minder goederen en diensten kunt kopen.",
      "antwoord": true,
      "uitleg": "Waar. Het min-teken betekent een daling: met je inkomen kun je gemiddeld 1,5% minder kopen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Stijgen de lonen met 2,0% en de prijzen ook met 2,0%, dan daalt het reëel inkomen met 2,0%.",
      "antwoord": false,
      "uitleg": "Niet waar. 2,0 − 2,0 = 0%: het reëel inkomen en de koopkracht blijven gelijk."
    },
    {
      "type": "invul",
      "vraag": "Het nominaal inkomen stijgt met 1,2%. De inflatie is 3,0%. Verandering reëel inkomen = ____ % (zet er een min-teken voor als het daalt).",
      "antwoord": "-1,8|−1,8",
      "uitleg": "1,2 − 3,0 = −1,8%. Let op het min-teken: de prijzen stijgen harder dan het inkomen."
    },
    {
      "type": "invul",
      "vraag": "Tess verdient € 1.500 per maand en krijgt er € 45 bij. De prijzen stijgen met 1%. Haar reëel inkomen verandert met ____ %.",
      "antwoord": "2|+2|2,0",
      "uitleg": "% nominaal = 45 / 1.500 × 100% = 3%. Reëel = 3% − 1% = +2%."
    },
    {
      "type": "mc",
      "vraag": "Hoe noem je de verandering van je inkomen in euro's, zonder rekening te houden met de prijzen?",
      "uitleg": "Een verandering van je inkomen in euro's is een verandering van het nominaal inkomen. Het reëel inkomen houdt ook rekening met de prijzen.",
      "opties": [
        "De verandering van het inflatiecijfer",
        "De verandering van het nominaal inkomen",
        "De verandering van de koopkrachtplaatjes",
        "De verandering van het reëel inkomen"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Welke groep merkt in verhouding het meest van duurdere zorg?",
      "uitleg": "Volgens het boek geven mensen van 60 tot 70 jaar in verhouding meer uit aan gezondheidszorg.",
      "opties": [
        "Mensen van 30 tot 40 jaar",
        "Mensen van 60 tot 70 jaar",
        "Mensen van 18 tot 25 jaar",
        "Jongeren onder de 18 jaar"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Waarom verschilt de koopkrachtontwikkeling per groep mensen?",
      "uitleg": "Het boek geeft twee redenen: mensen kopen verschillende dingen, en niet bij iedereen stijgt het inkomen in dezelfde mate.",
      "opties": [
        "Het CBS rekent voor elke groep met een ander inflatiecijfer per jaar",
        "Niet iedereen koopt hetzelfde en niet bij iedereen stijgt het inkomen evenveel",
        "Alleen mensen met een modaal inkomen hebben last van inflatie, alle andere groepen niet",
        "Iedereen koopt hetzelfde, maar de prijzen zijn per winkel verschillend"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Om je koopkracht gelijk te houden, moet je inkomen evenveel stijgen als de prijzen.",
      "antwoord": true,
      "uitleg": "Waar. Dan is de verandering van het reëel inkomen 0%."
    },
    {
      "type": "open",
      "vraag": "Een vriend zegt: 'Mijn loon steeg 2% en de inflatie was 6%, dus mijn koopkracht steeg met 4%.' Verbeter hem in één zin.",
      "sleutelwoorden": [
        "daalt/gedaald/daling/achteruit/minder/-4/−4"
      ],
      "minTreffers": 1,
      "modelantwoord": "Zijn koopkracht daalt juist met 4%, want 2% − 6% = −4%.",
      "uitleg": "Reëel = 2% − 6% = −4%. De prijzen stijgen harder dan zijn loon, dus zijn koopkracht daalt."
    },
    {
      "type": "mc",
      "vraag": "Wie maakt elk jaar de koopkrachtplaatjes?",
      "uitleg": "Het CPB (Centraal Planbureau) maakt de koopkrachtplaatjes. Het CBS (Centraal Bureau voor de Statistiek) meet de inflatie. Die twee worden vaak verwisseld.",
      "opties": [
        "De supermarkten",
        "De Belastingdienst",
        "Het CBS",
        "Het CPB"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat laat het reëel inkomen zien?",
      "uitleg": "Het reëel inkomen geeft aan hoeveel goederen je met je inkomen kunt kopen. Het bedrag in euro's is het nominaal inkomen.",
      "opties": [
        "Hoeveel je per maand spaart",
        "Hoeveel euro er elke maand op je loonstrook staat",
        "Hoeveel goederen je met je inkomen kunt kopen",
        "Hoeveel belasting je over je loon betaalt"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Mo verdiende € 2.500 en verdient nu € 2.550. De inflatie is 0%. Zijn reëel inkomen verandert met ____ %.",
      "antwoord": "2|+2|2,0",
      "uitleg": "50 / 2.500 × 100% = 2%. Zonder inflatie is de reële verandering gelijk aan de nominale: +2%."
    },
    {
      "type": "open",
      "vraag": "Lena's inkomen gaat 3% omhoog, de prijzen 1%. Bereken de verandering van haar koopkracht.",
      "sleutelwoorden": [
        "2",
        "stijgt/stijging/toe/vooruit/meer"
      ],
      "minTreffers": 1,
      "modelantwoord": "3% − 1% = +2%: haar koopkracht stijgt met 2%.",
      "uitleg": "Reëel = 3% − 1% = +2%. Haar inkomen stijgt harder dan de prijzen, dus haar koopkracht stijgt."
    }
  ]
});
