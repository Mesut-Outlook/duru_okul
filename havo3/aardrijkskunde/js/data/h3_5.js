/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §3.5 Migratie en Nederland
   buiteNLand 3 HAVO Hoofdstuk 3 (Migratie)
   ========================================================= */
DURU.register({
  id: "ak-h3-5",
  hoofdstuk: 3,
  paragraaf: "3.5",
  titel: "Migratie en Nederland",
  korteUitleg: "Migratiegeschiedenis van Nederland: koloniale migranten, gastarbeiders, vluchtelingen, expats en inburgering.",
  icoon: "🇳🇱",
  kleur: "h3-thema",
  theorie: `<h3>3.5 Migratie en Nederland</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Koloniale migranten, gastarbeiders, asielmigranten, kennismigranten, eerste generatie migrant, tweede generatie migrant, inburgeringsplicht, integratiebeleid.
</div>

<h4>1. De vier grote migratiegolven naar Nederland sinds 1945</h4>
<p>Nederland is sinds de Tweede Wereldoorlog veranderd van een emigratieland (veel Nederlanders emigreerden in de jaren 50 naar Canada en Australië) in een echt <b>immigratieland</b>. We onderscheiden vier grote groepen:</p>
<ol>
  <li><b>Koloniale migranten:</b> Na de onafhankelijkheid van Indonesië (1949) kwamen ruim 300.000 Indische Nederlanders en Molukkers naar Nederland. Rond de onafhankelijkheid van Suriname in 1975 migreerde bijna de helft van de Surinaamse bevolking naar Nederland. Ook vanuit de Nederlandse Antillen (Curaçao, Aruba, Bonaire) kwamen velen voor studie of werk.</li>
  <li><b>Gastarbeiders (arbeidsmigranten):</b> In de jaren 1960 en 1970 was er in Nederland een groot tekort aan arbeiders voor zwaar en laagbetaald fabrieks-, schoonmaak- en havenwerk. De overheid en bedrijven wierven actieve werknemers, eerst in Zuid-Europa (Spanje, Italië) en later vooral in <b>Turkije</b> en <b>Marokko</b>. Men dacht dat zij tijdelijk zouden blijven ('gasten'), maar velen bleven definitief en lieten hun gezin overkomen via <i>gezinshereniging</i>.</li>
  <li><b>Vluchtelingen en asielzoekers:</b> Vanaf de jaren 1980 en 1990 ontving Nederland mensen die vluchtten voor burgeroorlogen en geweld, onder andere uit voormalig Joegoslavië, Somalië, Irak, Afghanistan, Syrië, Eritrea en recentelijk Oekraïne.</li>
  <li><b>Europese werknemers en kennismigranten:</b> Binnen de EU werken honderdduizenden Midden- en Oost-Europeanen in de tuinbouw, logistiek en bouw. Daarnaast trekken bedrijven als ASML, Philips en universiteiten tienduizenden hoogopgeleide <i>kennismigranten</i> en internationale studenten aan.</li>
</ol>

<h4>2. Eerste en tweede generatie</h4>
<p>Het CBS hanteert duidelijke definities om de bevolking in te delen:</p>
<ul>
  <li><b>Eerste generatie migrant:</b> Iemand die zelf in het buitenland is geboren en naar Nederland is verhuisd.</li>
  <li><b>Tweede generatie migrant:</b> Iemand die zelf in Nederland is geboren, maar van wie ten minste één van de ouders in het buitenland is geboren.</li>
</ul>

<h4>3. Inburgering en integratiebeleid</h4>
<p>In het verleden ging de overheid ervan uit dat gastarbeiders vanzelf zouden terugkeren. Sinds de jaren 1990 voert Nederland een actief <b>inburgeringsbeleid</b>: nieuwkomers van buiten de EU hebben een <b>inburgeringsplicht</b>. Zij moeten de Nederlandse taal leren op taalniveau en slagen voor examens over de Nederlandse maatschappij en arbeidsmarkt om een verblijfsvergunning voor onbepaalde tijd of het staatsburgerschap te kunnen verkrijgen.</p>`,
  vragen: [
    {
        "type": "mc",
        "vraag": "Uit welke twee landen werden in de jaren 1960 en 1970 de meeste <b>gastarbeiders</b> naar Nederland gehaald?",
        "opties": [
            "Turkije en Marokko",
            "China en Japan",
            "Canada en de Verenigde Staten",
            "Noorwegen en Zweden"
        ],
        "antwoord": 0,
        "uitleg": "Vanaf de jaren 60 wierven Nederlandse bedrijven actief arbeiders in Turkije en Marokko."
    },
    {
        "type": "mc",
        "vraag": "Rond welk historisch moment migreerden honderdduizenden Surinamers naar Nederland?",
        "opties": [
            "De afschaffing van de slavernij in 1863",
            "De onafhankelijkheid van Suriname in 1975",
            "De Eerste Wereldoorlog in 1914",
            "De watersnoodramp in 1953"
        ],
        "antwoord": 1,
        "uitleg": "Rond de Surinaamse onafhankelijkheid in 1975 koos bijna de helft van de bevolking voor een Nederlands paspoort."
    },
    {
        "type": "waaronwaar",
        "vraag": "Iemand die in Rotterdam geboren is en van wie beide ouders in Turkije zijn geboren, behoort tot de tweede generatie migranten.",
        "antwoord": true,
        "uitleg": "Waar. Zelf in Nederland geboren + ten minste één ouder in buitenland geboren = tweede generatie."
    },
    {
        "type": "waaronwaar",
        "vraag": "In de jaren 1950 was Nederland een belangrijk immigratieland waar miljoenen buitenlanders naartoe kwamen.",
        "antwoord": false,
        "uitleg": "Niet waar. In de jaren 50 was Nederland juist een emigratieland; veel Nederlanders emigreerden naar Canada en Australië."
    },
    {
        "type": "invoer",
        "vraag": "Hoe noemen we de wettelijke verplichting voor nieuwkomers van buiten de EU om Nederlands te leren en examen te doen?",
        "antwoord": "inburgeringsplicht|inburgering",
        "uitleg": "De inburgeringsplicht verplicht nieuwkomers een inburgeringscursus en -examen te doen."
    },
    {
        "type": "invoer",
        "vraag": "Hoe werd een buitenlandse arbeider genoemd die in de jaren 60 door de overheid werd aangetrokken voor tijdelijk werk?",
        "antwoord": "gastarbeider",
        "uitleg": "Zij werden destijds gastarbeiders genoemd."
    },
    {
        "type": "mc",
        "vraag": "Wat verstaat het CBS onder een <b>eerste generatie migrant</b>?",
        "opties": [
            "Iemand die in Nederland is geboren maar geen Nederlands spreekt",
            "Iemand wiens grootouders in het buitenland zijn geboren",
            "Iemand die zelf in het buitenland is geboren en naar Nederland is verhuisd",
            "Iemand die tijdelijk als toerist in Nederland verblijft"
        ],
        "antwoord": 2,
        "uitleg": "De eerste generatie is zelf in het buitenland geboren."
    },
    {
        "type": "mc",
        "vraag": "Waarom bleven veel gastarbeiders die in de jaren 60 kwamen uiteindelijk toch definitief in Nederland?",
        "opties": [
            "Omdat zij verplicht werden hun paspoort in te leveren",
            "Omdat er in Nederland geen werk meer was",
            "Omdat het herkomstland hen de toegang weigerde",
            "Omdat zij economisch geworteld raakten en hun gezin lieten overkomen via gezinshereniging"
        ],
        "antwoord": 3,
        "uitleg": "Zij bouwden hier een bestaan op en kozen ervoor hun gezinnen over te laten komen."
    }
]
});
