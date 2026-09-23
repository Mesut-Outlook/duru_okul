/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §3.4 Migratie en de Europese Unie
   buiteNLand 3 HAVO Hoofdstuk 3 (Migratie)
   ========================================================= */
DURU.register({
  id: "ak-h3-4",
  hoofdstuk: 3,
  paragraaf: "3.4",
  titel: "Migratie en de Europese Unie",
  korteUitleg: "Verdrag van Schengen, buitengrenzen van de EU, Frontex, Dublin-verordening en asielbeleid.",
  icoon: "🇪🇺",
  kleur: "h3-thema",
  theorie: `<h3>3.4 Migratie en de Europese Unie</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Europese Unie, Schengenzone, vrij verkeer van personen en goederen, buitengrenzen, Frontex, Dublin-verordening, asielprocedure, Fort Europa.
</div>

<h4>1. Het Verdrag van Schengen en vrij verkeer</h4>
<p>Een van de grootste verworvenheden van de Europese integratie is het <b>Verdrag van Schengen</b>. Binnen het zogeheten Schengengebied (waartoe de meeste EU-landen en enkele niet-EU-landen zoals Zwitserland en Noorwegen behoren) zijn de vaste paspoortcontroles aan de <b>binnengrenzen afgeschaft</b>. Dit betekent dat burgers en vrachtwagens ongehinderd van Nederland naar België, Frankrijk of Duitsland kunnen reizen zonder stil te hoeven staan bij douaneposten.</p>
<p>Tegelijkertijd geldt binnen de EU het recht op <b>vrij verkeer van werknemers</b>: iedere burger met een paspoort van een EU-lidstaat mag in ieder ander EU-land wonen, studeren en werken zonder dat daar een tewerkstellingsvergunning voor nodig is. Veel werknemers uit Midden- en Oost-Europa (zoals Polen en Roemenië) werken hierdoor in West-Europese landen.</p>

<h4>2. Buitengrenzen en Frontex</h4>
<p>Omdat mensen zich eenmaal binnen de Schengenzone vrij kunnen verplaatsen, is er een gezamenlijke verantwoordelijkheid voor de <b>buitengrenzen van de EU</b>. Landen aan de rand van Europa (zoals Griekenland, Italië en Spanje) hebben te maken met grote druk op hun zee- en landgrenzen. Het Europese grens- en kustwachtagentschap <b>Frontex</b> ondersteunt deze lidstaten bij de grensbewaking en het tegengaan van irreguliere migratie en mensensmokkel.</p>

<h4>3. Het Europese asielbeleid en de Dublin-verordening</h4>
<p>Om te bepalen welk land verantwoordelijk is voor de behandeling van een asielaanvraag, hebben de EU-lidstaten de <b>Dublin-verordening</b> afgesproken:</p>
<ul>
  <li>Volgens deze regel moet een asielzoeker zijn asielaanvraag indienen in het <b>eerste EU-land</b> waar hij voet aan wal zet of geregistreerd wordt.</li>
  <li>Dit leidt in de praktijk tot grote spanningen, omdat zuidelijke grensoverschrijdende landen onevenredig zwaar worden belast met de opvang, terwijl veel migranten liever doorreizen naar welvarende Noord- en West-Europese landen zoals Duitsland of Nederland.</li>
</ul>`,
  vragen: [
    {
        "type": "mc",
        "vraag": "Wat is het belangrijkste gevolg van het <b>Verdrag van Schengen</b> voor reizigers binnen Europa?",
        "opties": [
            "De paspoortcontroles aan de binnengrenzen tussen de aangesloten landen zijn afgeschaft",
            "Iedere burger moet bij iedere provinciegrens een nieuw visum kopen",
            "Vliegtickets binnen Europa zijn overal gratis gemaakt",
            "Er mag geen handel meer worden gedreven over landsgrenzen heen"
        ],
        "antwoord": 0,
        "uitleg": "Schengen regelt het vrije verkeer van personen zonder grenscontroles aan de binnengrenzen."
    },
    {
        "type": "mc",
        "vraag": "Wat is de taak van het Europese agentschap <b>Frontex</b>?",
        "opties": [
            "Het innen van inkomstenbelasting in alle EU-steden",
            "Het bewaken van de gemeenschappelijke buitengrenzen van de Europese Unie",
            "Het organiseren van sportwedstrijden tussen Europese universiteiten",
            "Het bepalen van de rentetarieven van de Europese Centrale Bank"
        ],
        "antwoord": 1,
        "uitleg": "Frontex is het Europese grens- en kustwachtagentschap dat de buitengrenzen bewaakt."
    },
    {
        "type": "waaronwaar",
        "vraag": "Volgens de Dublin-verordening mag een asielzoeker zelf kiezen in welk EU-land hij zijn aanvraag indient, ongeacht waar hij Europa binnenkwam.",
        "antwoord": false,
        "uitleg": "Niet waar. Volgens Dublin moet de aanvraag worden behandeld in het eerste land van aankomst in de EU."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een inwoner met de Spaanse nationaliteit mag zonder werkvergunning in Nederland gaan werken vanwege het vrije verkeer van werknemers in de EU.",
        "antwoord": true,
        "uitleg": "Waar. EU-burgers hebben het recht op vrij verkeer van werknemers binnen alle lidstaten."
    },
    {
        "type": "invoer",
        "vraag": "Hoe heet het Europese verdrag waarmee de paspoortcontroles aan de binnengrenzen zijn afgeschaft?",
        "antwoord": "schengen|verdrag van schengen",
        "uitleg": "Het Verdrag van Schengen regelt het afschaffen van de binnengrenzen."
    },
    {
        "type": "invoer",
        "vraag": "Welke Europese verordening bepaalt dat een asielaanvraag behandeld moet worden in het eerste EU-land van aankomst?",
        "antwoord": "dublin|dublin-verordening|dublin verordening",
        "uitleg": "De Dublin-verordening regelt de toewijzing van de asielprocedure."
    },
    {
        "type": "mc",
        "vraag": "Waarom ervaren landen als Griekenland en Italië de Dublin-verordening als oneerlijk?",
        "opties": [
            "Omdat zij geen lid mogen zijn van de Europese Unie",
            "Omdat migranten weigeren in Griekenland of Italië vakantie te vieren",
            "Omdat zij door hun geografische ligging aan de Middellandse Zee de meeste asielzoekers moeten opvangen en registreren",
            "Omdat zij verplicht zijn alle migranten direct een Nederlands paspoort te geven"
        ],
        "antwoord": 2,
        "uitleg": "Zuidelijke grenslanden vangen door hun ligging aan zee de grootste stroom nieuwkomers op."
    },
    {
        "type": "mc",
        "vraag": "Welke term wordt door critici gebruikt om aan te duiden dat de EU haar buitengrenzen zwaar barricadeert tegen migranten van buiten Europa?",
        "opties": [
            "Verenigde Staten van Europa",
            "De Gouden Eeuw",
            "De Europese Triade",
            "Fort Europa"
        ],
        "antwoord": 3,
        "uitleg": "De term 'Fort Europa' verwijst naar het strenge buitengrenzenbeleid om irreguliere migratie tegen te houden."
    }
]
});
