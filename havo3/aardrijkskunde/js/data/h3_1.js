/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §3.1 Migratie in de wereld
   buiteNLand 3 HAVO Hoofdstuk 3 (Migratie)
   ========================================================= */
DURU.register({
  id: "ak-h3-1",
  hoofdstuk: 3,
  paragraaf: "3.1",
  titel: "Migratie in de wereld",
  korteUitleg: "Vormen van migratie, push- en pullfactoren en migratiemotieven (economisch, politiek, sociaal, fysisch).",
  icoon: "🧳",
  kleur: "h3-thema",
  theorie: `<h3>3.1 Migratie in de wereld</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Migratie, emigratie, immigratie, pushfactoren, pullfactoren, arbeidsmigrant, kennismigrant, asielzoeker, gezinsmigratie (gezinsvorming en gezinshereniging), tussenliggende hindernissen.
</div>

<h4>1. Wat is migratie?</h4>
<p><b>Migratie</b> is het verhuizen naar een andere gemeente of een ander land met het doel zich daar voor langere tijd te vestigen. Iemand die zijn geboorteland verlaat heet een <b>emigrant</b> voor het vertrekland, en een <b>immigrant</b> voor het bestemmingsland. Migratie binnen de grenzen van een land (bijvoorbeeld van een plattelandsdorp naar de hoofdstad) noemen we <i>binnenlandse migratie</i>; verhuizen over een landsgrens heen heet <i>buitenlandse of internationale migratie</i>.</p>

<h4>2. Motieven om te migreren</h4>
<p>Waarom verlaten mensen hun vertrouwde omgeving? We onderscheiden vier hoofdredenen:</p>
<ul>
  <li><b>Economische motieven:</b> Mensen verhuizen om werk te vinden, meer geld te verdienen of extreme armoede te ontvluchten. Dit zijn <b>arbeidsmigranten</b>. Hoogopgeleide werknemers met specialistische kennis (zoals IT-specialisten of ingenieurs) noemen we <b>kennismigranten</b> of expats.</li>
  <li><b>Politieke motieven:</b> Mensen vluchten voor oorlog, geweld, dictatuur of vervolging vanwege hun religie, ras of politieke overtuiging. Als zij in een ander land officiële bescherming aanvragen, noemen we hen <b>asielzoekers</b>. Wordt hun aanvraag goedgekeurd, dan krijgen zij de status van <b>statushouder</b> of vluchteling.</li>
  <li><b>Sociale motieven:</b> Verhuizen uit sociale redenen, met name voor de liefde of familie. We onderscheiden <i>gezinshereniging</i> (waarbij reeds gemigreerde gezinsleden hun partner of minderjarige kinderen laten overkomen) en <i>gezinsvorming</i> (waarbij iemand trouwt met een partner uit het buitenland en die naar het woonland haalt).</li>
  <li><b>Fysische / ecologische motieven:</b> Verhuizen vanwege natuurrampen of klimaatverandering, zoals aanhoudende droogte, mislukte oogsten, overstromingen of zeespiegelstijging (klimaatvluchtelingen).</li>
</ul>

<h4>3. Het Push- en Pullmodel van Lee</h4>
<p>Geograaf Everett Lee ontwikkelde het bekende push- en pullmodel om migratiestromen te verklaren:</p>
<ul>
  <li><b>Pushfactoren (afstotende krachten):</b> Omstandigheden in het herkomstgebied die mensen als het ware 'wegduwen', zoals werkloosheid, honger, lage lonen, gebrek aan vrijheid, discriminatie of natuurrampen.</li>
  <li><b>Pullfactoren (aantrekkende krachten):</b> Omstandigheden in het bestemmingsgebied die mensen 'aantrekken', zoals goede banen, hoge salarissen, veiligheid, democratie, hoogwaardig onderwijs en uitstekende gezondheidszorg.</li>
  <li><b>Tussenliggende hindernissen:</b> Factoren die de migratie bemoeilijken of tegenhouden, zoals de fysieke afstand, hoge reiskosten, visumbeperkingen, gevaarlijke smokkelroutes over zee of gesloten grenzen.</li>
</ul>`,
  vragen: [
    {
        "type": "mc",
        "vraag": "Wat is het formele verschil tussen een emigrant en een immigrant?",
        "opties": [
            "Een emigrant verlaat een land; een immigrant komt een land binnen om er te wonen",
            "Een emigrant vlucht voor oorlog; een immigrant zoekt altijd werk",
            "Een emigrant reist binnen zijn eigen land; een immigrant gaat naar het buitenland",
            "Een emigrant heeft geen paspoort; een immigrant heeft een dubbele nationaliteit"
        ],
        "antwoord": 0,
        "uitleg": "Emigreren is weggaan uit een land; immigreren is aankomen in een nieuw land."
    },
    {
        "type": "mc",
        "vraag": "Welke situatie is een klassiek voorbeeld van een <b>pullfactor</b> van een bestemmingsgebied?",
        "opties": [
            "Een plotselinge misoogst door ernstige droogte in het herkomstland",
            "De beschikbaarheid van goedbetaalde banen en uitstekende scholen in het doelland",
            "Oorlog en politieke onderdrukking door een gewelddadige dictator",
            "Een gebrek aan ziekenhuizen en medicijnen in het dorp"
        ],
        "antwoord": 1,
        "uitleg": "Een pullfactor trekt mensen naar een land toe, zoals welvaart, banen en goed onderwijs."
    },
    {
        "type": "waaronwaar",
        "vraag": "Wanneer een immigrant zijn partner en kinderen uit zijn herkomstland laat overkomen, spreken we van gezinsvorming.",
        "antwoord": false,
        "uitleg": "Niet waar. Dit heet gezinshereniging (het reeds bestaande gezin wordt herenigd). Gezinsvorming is trouwen met een nieuwe partner uit het buitenland."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een asielzoeker is iemand die in een ander land officiële bescherming aanvraagt tegen vervolging of oorlog.",
        "antwoord": true,
        "uitleg": "Waar. Asielzoekers vragen asiel (bescherming) aan volgens het VN-Vluchtelingenverdrag."
    },
    {
        "type": "invoer",
        "vraag": "Hoe noemen we factoren in een herkomstland die mensen dwingen of motiveren om te vertrekken (bijv. werkloosheid of oorlog)?",
        "antwoord": "pushfactoren|pushfactor|push-factoren|push-factor",
        "uitleg": "Pushfactoren duwen mensen weg uit hun herkomstgebied."
    },
    {
        "type": "invoer",
        "vraag": "Hoe noemen we een hoogopgeleide arbeidsmigrant die vanwege specifieke technische of wetenschappelijke kennis naar een land verhuist?",
        "antwoord": "kennismigrant|expat",
        "uitleg": "Een kennismigrant verhuist vanwege specialistische kennis."
    },
    {
        "type": "mc",
        "vraag": "Tot welk migratiemotief behoort een verhuizing wegens aanhoudende overstromingen en zeespiegelstijging?",
        "opties": [
            "Politiek motief",
            "Sociaal motief",
            "Fysisch / ecologisch motief",
            "Economisch motief"
        ],
        "antwoord": 2,
        "uitleg": "Natuurrampen en klimaatverandering vallen onder fysische (natuurlijke of ecologische) motieven."
    },
    {
        "type": "mc",
        "vraag": "Wat verstaat men in het model van Lee onder <b>tussenliggende hindernissen</b>?",
        "opties": [
            "De redenen waarom iemand in zijn geboortestad wil blijven wonen",
            "De culturele verschillen die pas na tien jaar optreden",
            "De belastingregels in het herkomstland",
            "Obstakels zoals grote afstand, hoge reiskosten en strenge visumvereisten"
        ],
        "antwoord": 3,
        "uitleg": "Tussenliggende hindernissen zijn de obstakels die de migrant moet overwinnen om het doelland te bereiken."
    }
]
});
