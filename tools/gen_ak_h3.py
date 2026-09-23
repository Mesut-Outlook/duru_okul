"""
Script om Aardrijkskunde Hoofdstuk 3 (Migratie) te genereren:
- 5 Onderwerpen (h3_1.js t/m h3_5.js)
- 5 Proeftoetsen (examen_11.js t/m examen_15.js)
Gebaseerd op buiteNLand 3 HAVO Hoofdstuk 3 (Migratie, p. 8-44).
"""
import os
import json

BASE_DIR = 'havo3/aardrijkskunde/js/data'

ONDERWERPEN = [
    {
        'file': 'h3_1.js',
        'id': 'ak-h3-1',
        'hoofdstuk': 3,
        'paragraaf': '3.1',
        'titel': 'Migratie in de wereld',
        'korteUitleg': 'Vormen van migratie, push- en pullfactoren en migratiemotieven (economisch, politiek, sociaal, fysisch).',
        'icoon': '🧳',
        'kleur': 'h3-thema',
        'theorie': """<h3>3.1 Migratie in de wereld</h3>
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
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat is het formele verschil tussen een emigrant en een immigrant?',
                'opties': [
                    'Een emigrant verlaat een land; een immigrant komt een land binnen om er te wonen',
                    'Een emigrant vlucht voor oorlog; een immigrant zoekt altijd werk',
                    'Een emigrant reist binnen zijn eigen land; een immigrant gaat naar het buitenland',
                    'Een emigrant heeft geen paspoort; een immigrant heeft een dubbele nationaliteit'
                ],
                'antwoord': 0,
                'uitleg': 'Emigreren is weggaan uit een land; immigreren is aankomen in een nieuw land.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke situatie is een klassiek voorbeeld van een <b>pullfactor</b> van een bestemmingsgebied?',
                'opties': [
                    'Een plotselinge misoogst door ernstige droogte in het herkomstland',
                    'De beschikbaarheid van goedbetaalde banen en uitstekende scholen in het doelland',
                    'Oorlog en politieke onderdrukking door een gewelddadige dictator',
                    'Een gebrek aan ziekenhuizen en medicijnen in het dorp'
                ],
                'antwoord': 1,
                'uitleg': 'Een pullfactor trekt mensen naar een land toe, zoals welvaart, banen en goed onderwijs.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Wanneer een immigrant zijn partner en kinderen uit zijn herkomstland laat overkomen, spreken we van gezinsvorming.',
                'antwoord': False,
                'uitleg': 'Niet waar. Dit heet gezinshereniging (het reeds bestaande gezin wordt herenigd). Gezinsvorming is trouwen met een nieuwe partner uit het buitenland.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Een asielzoeker is iemand die in een ander land officiële bescherming aanvraagt tegen vervolging of oorlog.',
                'antwoord': True,
                'uitleg': 'Waar. Asielzoekers vragen asiel (bescherming) aan volgens het VN-Vluchtelingenverdrag.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe noemen we factoren in een herkomstland die mensen dwingen of motiveren om te vertrekken (bijv. werkloosheid of oorlog)?',
                'antwoord': 'pushfactoren|pushfactor|push-factoren|push-factor',
                'uitleg': 'Pushfactoren duwen mensen weg uit hun herkomstgebied.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe noemen we een hoogopgeleide arbeidsmigrant die vanwege specifieke technische of wetenschappelijke kennis naar een land verhuist?',
                'antwoord': 'kennismigrant|expat',
                'uitleg': 'Een kennismigrant verhuist vanwege specialistische kennis.'
            },
            {
                'type': 'mc',
                'vraag': 'Tot welk migratiemotief behoort een verhuizing wegens aanhoudende overstromingen en zeespiegelstijging?',
                'opties': [
                    'Politiek motief',
                    'Sociaal motief',
                    'Fysisch / ecologisch motief',
                    'Economisch motief'
                ],
                'antwoord': 2,
                'uitleg': 'Natuurrampen en klimaatverandering vallen onder fysische (natuurlijke of ecologische) motieven.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men in het model van Lee onder <b>tussenliggende hindernissen</b>?',
                'opties': [
                    'De redenen waarom iemand in zijn geboortestad wil blijven wonen',
                    'De culturele verschillen die pas na tien jaar optreden',
                    'De belastingregels in het herkomstland',
                    'Obstakels zoals grote afstand, hoge reiskosten en strenge visumvereisten'
                ],
                'antwoord': 3,
                'uitleg': 'Tussenliggende hindernissen zijn de obstakels die de migrant moet overwinnen om het doelland te bereiken.'
            }
        ]
    },
    {
        'file': 'h3_2.js',
        'id': 'ak-h3-2',
        'hoofdstuk': 3,
        'paragraaf': '3.2',
        'titel': 'Gevolgen voor de herkomstgebieden',
        'korteUitleg': 'Braindrain, braingain, geldzendingen (remittances), migratienetwerken en demografische veranderingen.',
        'icoon': '📉',
        'kleur': 'h3-thema',
        'theorie': """<h3>3.2 Gevolgen voor de herkomstgebieden</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Braindrain, braingain, geldzendingen (remittances), migratienetwerken, volgmigratie (kettingmigratie), selectieve migratie, retourmigratie.
</div>

<h4>1. Economische effecten: Geldzendingen (Remittances)</h4>
<p>Een van de meest directe positieve gevolgen van emigratie voor arme herkomstlanden zijn <b>geldzendingen</b> (in het Engels: <i>remittances</i>). Migranten die in rijke landen werken, sturen maandelijks een aanzienlijk deel van hun spaargeld terug naar familieleden die achterbleven. Wereldwijd is het totale bedrag aan geldzendingen vele malen groter dan alle officiële internationale ontwikkelingshulp van overheden bij elkaar opgeteld! Dit geld wordt direct besteed aan dagelijks voedsel, betere huisvesting, schoolgeld voor kinderen en medische zorg.</p>

<h4>2. Het kenniseffect: Braindrain versus Braingain</h4>
<p>Migratie heeft echter ook zware schaduwkanten voor de herkomstgebieden:</p>
<ul>
  <li><b>Braindrain:</b> Dit ontstaat wanneer veel hoogopgeleide, getalenteerde en ondernemende mensen (zoals artsen, verpleegkundigen, docenten, ingenieurs en wetenschappers) massaal het land verlaten om in het buitenland meer geld te verdienen. Hierdoor kampt het herkomstland met een chronisch tekort aan essentiële specialisten, wat de lokale economische ontwikkeling ernstig remt.</li>
  <li><b>Braingain:</b> Wanneer geëmigreerde specialisten na enkele jaren besluiten terug te keren naar hun vaderland (<b>retourmigratie</b>), brengen zij waardevolle kennis, internationale werkervaring, vreemde talen en investeringskapitaal mee. Hierdoor kan braindrain uiteindelijk omslaan in een stimulans voor het herkomstland.</li>
</ul>

<h4>3. Demografische en sociale gevolgen</h4>
<p>Migratie is vrijwel altijd <b>selectieve migratie</b>: het zijn meestal niet de ouderen of de allerarmsten die verhuizen, maar met name gezonde, jonge volwassenen tussen de 18 en 35 jaar. Dit heeft duidelijke gevolgen voor het herkomstgebied:</p>
<ul>
  <li><b>Vergrijzing en ontvolking:</b> In dorpen en plattelandsgebieden blijven vooral ouderen, vrouwen en jonge kinderen achter. Landbouwgrond raakt soms verlaten.</li>
  <li><b>Migratienetwerken en volgmigratie:</b> De eerste pioniers die vertrekken bouwen een netwerk op in het bestemmingsland. Zij helpen familieleden en vrienden aan onderdak en werk, waardoor één migrant vaak leidt tot tientallen nieuwe migranten (<b>volgmigratie</b> of kettingmigratie).</li>
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste kenmerk van een <b>braindrain</b> voor een ontwikkelingsland?',
                'opties': [
                    'Hoogopgeleide krachten zoals artsen en ingenieurs verlaten massaal het land',
                    'Er stromen te veel buitenlandse studenten het land binnen',
                    'Het land verliest al zijn landbouwgrond door overstromingen',
                    'Er is geen internetverbinding meer beschikbaar'
                ],
                'antwoord': 0,
                'uitleg': 'Braindrain betekent letterlijk het weglekken van hersenen (kennis) doordat talentvolle specialisten emigreren.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat zijn <b>geldzendingen (remittances)</b>?',
                'opties': [
                    'Subsidies die de Europese Unie betaalt aan boeren',
                    'Geld dat migranten vanuit het bestemmingsland terugsturen naar familie in het herkomstland',
                    'Boetes die illegale smokkelaars moeten betalen aan de douane',
                    'Leningen die bedrijven afsluiten bij buitenlandse banken'
                ],
                'antwoord': 1,
                'uitleg': 'Geldzendingen zijn overboekingen van migranten naar hun familie thuis, een enorme inkomstenbron voor herkomstlanden.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Braingain ontstaat wanneer terugkerende migranten nieuwe kennis en investeringen meebrengen naar hun herkomstland.',
                'antwoord': True,
                'uitleg': 'Waar. Braingain is het positieve kenniseffect van terugkerende migranten.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Bij selectieve migratie vertrekken vooral hoogbejaarde mensen naar het buitenland.',
                'antwoord': False,
                'uitleg': 'Niet waar. Selectieve migratie betreft vooral jonge, fysiek gezonde volwassenen (18-35 jaar).'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe heet het verschijnsel waarbij de vestiging van eerdere migranten leidt tot het overkomen van familieleden en vrienden?',
                'antwoord': 'volgmigratie|kettingmigratie',
                'uitleg': 'Volgmigratie of kettingmigratie ontstaat via migratienetwerken.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe noemen we de vorm van migratie waarbij mensen definitief terugkeren naar hun geboorteland?',
                'antwoord': 'retourmigratie|terugkeermigratie',
                'uitleg': 'Retourmigratie is het terugkeren naar het land van herkomst.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een nadelig demografisch gevolg van selectieve emigratie voor achterblijvende dorpen op het platteland?',
                'opties': [
                    'Een plotselinge geboortegolf in de dorpen',
                    'Een sterke daling van het aantal ouderen',
                    'Vergrijzing en tekort aan arbeidskrachten doordat jonge volwassenen wegtrekken',
                    'Overbevolking in de dorpen'
                ],
                'antwoord': 2,
                'uitleg': 'Als jonge volwassenen wegtrekken blijven vooral ouderen en kinderen achter, waardoor het dorp vergrijst.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom zijn geldzendingen van migranten economisch zo belangrijk voor herkomstlanden?',
                'opties': [
                    'Omdat de overheid dit geld volledig mag confisqueren voor defensie',
                    'Omdat migranten verplicht zijn aandelen te kopen in de centrale bank',
                    'Omdat het bedrag alleen aan buitenlandse luxeproducten besteed mag worden',
                    'Omdat het geld rechtstreeks bij arme gezinnen terechtkomt voor onderwijs, voedsel en bouw'
                ],
                'antwoord': 3,
                'uitleg': 'Geldzendingen komen direct bij huishoudens terecht en zorgen voor armoedeverlichting en betere levensomstandigheden.'
            }
        ]
    },
    {
        'file': 'h3_3.js',
        'id': 'ak-h3-3',
        'hoofdstuk': 3,
        'paragraaf': '3.3',
        'titel': 'Gevolgen voor de bestemmingsgebieden',
        'korteUitleg': 'Multiculturele samenleving, integratie, acculturatie, segregatie en arbeidsmarktverhoudingen.',
        'icoon': '🏙️',
        'kleur': 'h3-thema',
        'theorie': """<h3>3.3 Gevolgen voor de bestemmingsgebieden</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Multiculturele samenleving, integratie, acculturatie, assimilatie, segregatie (ruimtelijk en sociaal), ontmoeting en spanningen.
</div>

<h4>1. De multiculturele samenleving</h4>
<p>Wanneer mensen uit diverse landen en culturen zich langdurig vestigen in een nieuw land, ontstaat een <b>multiculturele samenleving</b>. Hierin leven groepen met uiteenlopende culturele waarden, talen, godsdiensten en leefgewoonten naast en met elkaar. Dit zie je overal ter wereld vooral terug in de grote steden (zoals Amsterdam, Rotterdam, Londen, Parijs en New York), waar honderden nationaliteiten samenwonen.</p>

<h4>2. Cultuuroverdracht en aanpassing</h4>
<p>Hoe gaan immigranten en de ontvangende samenleving met elkaars cultuur om? Geografen en sociologen onderscheiden drie belangrijke begrippen:</p>
<ul>
  <li><b>Integratie:</b> Nieuwkomers passen zich aan de basisregels van de ontvangende samenleving aan (zoals het leren van de taal, respecteren van wetten en deelnemen aan de arbeidsmarkt), maar behouden tegelijkertijd hun eigen culturele identiteit, geloof en familietradities.</li>
  <li><b>Assimilatie:</b> De immigrantengroep neemt de cultuur van het bestemmingsland zo volledig over dat de eigen oorspronkelijke culturele kenmerken en taal geheel verdwijnen.</li>
  <li><b>Acculturatie:</b> Het proces van wederzijdse cultuurbeïnvloeding door langdurig contact tussen groepen. Zowel de immigranten als de autochtone bevolking nemen elementen van elkaar over (denk aan leenwoorden in de taal, eetcultuur zoals Surinaamse roti of Italiaanse pizza, en muziekstijlen).</li>
</ul>

<h4>3. Segregatie: Ruimtelijke scheiding in de stad</h4>
<p>Een belangrijk geografisch vraagstuk in steden is <b>segregatie</b>: het ruimtelijk of sociaal gescheiden wonen van bevolkingsgroepen op basis van etniciteit of inkomensniveau:</p>
<ul>
  <li><b>Ruimtelijke segregatie:</b> Bepaalde groepen concentreren zich in specifieke wijken (bijvoorbeeld door goedkope sociale huurwoningen), waardoor zogenoemde 'etnische wijken' ontstaan met eigen winkels en gebedshuizen.</li>
  <li><b>Sociale segregatie:</b> Mensen hebben in het dagelijks leven (school, sportclub, vriendenkring) nauwelijks contact met andere bevolkingsgroepen, waardoor wederzijds onbegrip en vooroordelen kunnen toenemen.</li>
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men onder een <b>multiculturele samenleving</b>?',
                'opties': [
                    'Een samenleving waarin mensen met verschillende culturele achtergronden samenleven',
                    'Een land waarin iedereen exact dezelfde religie belijdt',
                    'Een staat waar uitsluitend mensen wonen die in het land zelf geboren zijn',
                    'Een samenleving zonder enige vorm van wetgeving of overheid'
                ],
                'antwoord': 0,
                'uitleg': 'In een multiculturele samenleving wonen groepen met verschillende culturen, talen en gewoonten samen.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het verschil tussen <b>integratie</b> en <b>assimilatie</b>?',
                'opties': [
                    'Bij integratie moet iedereen verhuizen; bij assimilatie mag iedereen blijven',
                    'Bij integratie behoudt men deels de eigen cultuur; bij assimilatie geeft men de eigen cultuur volledig op',
                    'Integratie geldt alleen voor toeristen; assimilatie voor expats',
                    'Integratie is verboden volgens de wet; assimilatie is verplicht'
                ],
                'antwoord': 1,
                'uitleg': 'Integratie = meedoen met behoud van eigen identiteit; assimilatie = volledige aanpassing waarbij de oorspronkelijke cultuur verdwijnt.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Acculturatie betekent dat culturen elkaar over en weer beïnvloeden door langdurig contact, bijvoorbeeld in eetcultuur en muziek.',
                'antwoord': True,
                'uitleg': 'Waar. Acculturatie is wederzijdse culturele beïnvloeding.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Ruimtelijke segregatie betekent dat verschillende bevolkingsgroepen gelijkmatig over alle straten van de stad verspreid wonen.',
                'antwoord': False,
                'uitleg': 'Niet waar. Segregatie betekent juist dat groepen gescheiden van elkaar wonen in aparte wijken of buurten.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe noemt men de ruimtelijke of sociale scheiding van bevolkingsgroepen in een stad?',
                'antwoord': 'segregatie',
                'uitleg': 'Segregatie is de scheiding van groepen in wijken of sociale kringen.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welke term beschrijft het meedoen aan de samenleving (zoals taal leren en werken) met behoud van de eigen culturele achtergrond?',
                'antwoord': 'integratie',
                'uitleg': 'Integratie is deelnemen aan de maatschappij met behoud van eigen identiteit.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een veelvoorkomende oorzaak van ruimtelijke segregatie in grote steden?',
                'opties': [
                    'Wettelijke verplichting om per nationaliteit in een afgesloten wijk te wonen',
                    'Het feit dat iedereen in een grote stad exact evenveel verdient',
                    'Verschillen in inkomen en de concentratie van goedkope sociale huurwoningen in bepaalde buurten',
                    'Het ontbreken van openbaar vervoer tussen stadswijken'
                ],
                'antwoord': 2,
                'uitleg': 'Inkomensverschillen en de ligging van goedkope sociale huurwoningen sturen waar nieuwkomers kunnen wonen.'
            },
            {
                'type': 'mc',
                'vraag': 'Welk voorbeeld illustreert het begrip <b>acculturatie</b> in Nederland?',
                'opties': [
                    'Het sluiten van alle internationale restaurants in een stad',
                    'Het verbieden van vreemde talen op straat',
                    'De verplichte emigratie van buitenlandse werknemers',
                    'Het overnemen van Surinaamse roti, Turkse pizza en Indische nasi in de dagelijkse Nederlandse keuken'
                ],
                'antwoord': 3,
                'uitleg': 'Het opnemen van gerechten en gebruiken uit migrantenculturen in het dagelijks leven is een klassiek voorbeeld van acculturatie.'
            }
        ]
    },
    {
        'file': 'h3_4.js',
        'id': 'ak-h3-4',
        'hoofdstuk': 3,
        'paragraaf': '3.4',
        'titel': 'Migratie en de Europese Unie',
        'korteUitleg': 'Verdrag van Schengen, buitengrenzen van de EU, Frontex, Dublin-verordening en asielbeleid.',
        'icoon': '🇪🇺',
        'kleur': 'h3-thema',
        'theorie': """<h3>3.4 Migratie en de Europese Unie</h3>
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
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste gevolg van het <b>Verdrag van Schengen</b> voor reizigers binnen Europa?',
                'opties': [
                    'De paspoortcontroles aan de binnengrenzen tussen de aangesloten landen zijn afgeschaft',
                    'Iedere burger moet bij iedere provinciegrens een nieuw visum kopen',
                    'Vliegtickets binnen Europa zijn overal gratis gemaakt',
                    'Er mag geen handel meer worden gedreven over landsgrenzen heen'
                ],
                'antwoord': 0,
                'uitleg': 'Schengen regelt het vrije verkeer van personen zonder grenscontroles aan de binnengrenzen.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is de taak van het Europese agentschap <b>Frontex</b>?',
                'opties': [
                    'Het innen van inkomstenbelasting in alle EU-steden',
                    'Het bewaken van de gemeenschappelijke buitengrenzen van de Europese Unie',
                    'Het organiseren van sportwedstrijden tussen Europese universiteiten',
                    'Het bepalen van de rentetarieven van de Europese Centrale Bank'
                ],
                'antwoord': 1,
                'uitleg': 'Frontex is het Europese grens- en kustwachtagentschap dat de buitengrenzen bewaakt.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Volgens de Dublin-verordening mag een asielzoeker zelf kiezen in welk EU-land hij zijn aanvraag indient, ongeacht waar hij Europa binnenkwam.',
                'antwoord': False,
                'uitleg': 'Niet waar. Volgens Dublin moet de aanvraag worden behandeld in het eerste land van aankomst in de EU.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Een inwoner met de Spaanse nationaliteit mag zonder werkvergunning in Nederland gaan werken vanwege het vrije verkeer van werknemers in de EU.',
                'antwoord': True,
                'uitleg': 'Waar. EU-burgers hebben het recht op vrij verkeer van werknemers binnen alle lidstaten.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe heet het Europese verdrag waarmee de paspoortcontroles aan de binnengrenzen zijn afgeschaft?',
                'antwoord': 'schengen|verdrag van schengen',
                'uitleg': 'Het Verdrag van Schengen regelt het afschaffen van de binnengrenzen.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welke Europese verordening bepaalt dat een asielaanvraag behandeld moet worden in het eerste EU-land van aankomst?',
                'antwoord': 'dublin|dublin-verordening|dublin verordening',
                'uitleg': 'De Dublin-verordening regelt de toewijzing van de asielprocedure.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom ervaren landen als Griekenland en Italië de Dublin-verordening als oneerlijk?',
                'opties': [
                    'Omdat zij geen lid mogen zijn van de Europese Unie',
                    'Omdat migranten weigeren in Griekenland of Italië vakantie te vieren',
                    'Omdat zij door hun geografische ligging aan de Middellandse Zee de meeste asielzoekers moeten opvangen en registreren',
                    'Omdat zij verplicht zijn alle migranten direct een Nederlands paspoort te geven'
                ],
                'antwoord': 2,
                'uitleg': 'Zuidelijke grenslanden vangen door hun ligging aan zee de grootste stroom nieuwkomers op.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke term wordt door critici gebruikt om aan te duiden dat de EU haar buitengrenzen zwaar barricadeert tegen migranten van buiten Europa?',
                'opties': [
                    'Verenigde Staten van Europa',
                    'De Gouden Eeuw',
                    'De Europese Triade',
                    'Fort Europa'
                ],
                'antwoord': 3,
                'uitleg': 'De term \'Fort Europa\' verwijst naar het strenge buitengrenzenbeleid om irreguliere migratie tegen te houden.'
            }
        ]
    },
    {
        'file': 'h3_5.js',
        'id': 'ak-h3-5',
        'hoofdstuk': 3,
        'paragraaf': '3.5',
        'titel': 'Migratie en Nederland',
        'korteUitleg': 'Migratiegeschiedenis van Nederland: koloniale migranten, gastarbeiders, vluchtelingen, expats en inburgering.',
        'icoon': '🇳🇱',
        'kleur': 'h3-thema',
        'theorie': """<h3>3.5 Migratie en Nederland</h3>
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
<p>In het verleden ging de overheid ervan uit dat gastarbeiders vanzelf zouden terugkeren. Sinds de jaren 1990 voert Nederland een actief <b>inburgeringsbeleid</b>: nieuwkomers van buiten de EU hebben een <b>inburgeringsplicht</b>. Zij moeten de Nederlandse taal leren op taalniveau en slagen voor examens over de Nederlandse maatschappij en arbeidsmarkt om een verblijfsvergunning voor onbepaalde tijd of het staatsburgerschap te kunnen verkrijgen.</p>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Uit welke twee landen werden in de jaren 1960 en 1970 de meeste <b>gastarbeiders</b> naar Nederland gehaald?',
                'opties': [
                    'Turkije en Marokko',
                    'China en Japan',
                    'Canada en de Verenigde Staten',
                    'Noorwegen en Zweden'
                ],
                'antwoord': 0,
                'uitleg': 'Vanaf de jaren 60 wierven Nederlandse bedrijven actief arbeiders in Turkije en Marokko.'
            },
            {
                'type': 'mc',
                'vraag': 'Rond welk historisch moment migreerden honderdduizenden Surinamers naar Nederland?',
                'opties': [
                    'De afschaffing van de slavernij in 1863',
                    'De onafhankelijkheid van Suriname in 1975',
                    'De Eerste Wereldoorlog in 1914',
                    'De watersnoodramp in 1953'
                ],
                'antwoord': 1,
                'uitleg': 'Rond de Surinaamse onafhankelijkheid in 1975 koos bijna de helft van de bevolking voor een Nederlands paspoort.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Iemand die in Rotterdam geboren is en van wie beide ouders in Turkije zijn geboren, behoort tot de tweede generatie migranten.',
                'antwoord': True,
                'uitleg': 'Waar. Zelf in Nederland geboren + ten minste één ouder in buitenland geboren = tweede generatie.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'In de jaren 1950 was Nederland een belangrijk immigratieland waar miljoenen buitenlanders naartoe kwamen.',
                'antwoord': False,
                'uitleg': 'Niet waar. In de jaren 50 was Nederland juist een emigratieland; veel Nederlanders emigreerden naar Canada en Australië.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe noemen we de wettelijke verplichting voor nieuwkomers van buiten de EU om Nederlands te leren en examen te doen?',
                'antwoord': 'inburgeringsplicht|inburgering',
                'uitleg': 'De inburgeringsplicht verplicht nieuwkomers een inburgeringscursus en -examen te doen.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe werd een buitenlandse arbeider genoemd die in de jaren 60 door de overheid werd aangetrokken voor tijdelijk werk?',
                'antwoord': 'gastarbeider',
                'uitleg': 'Zij werden destijds gastarbeiders genoemd.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaat het CBS onder een <b>eerste generatie migrant</b>?',
                'opties': [
                    'Iemand die in Nederland is geboren maar geen Nederlands spreekt',
                    'Iemand wiens grootouders in het buitenland zijn geboren',
                    'Iemand die zelf in het buitenland is geboren en naar Nederland is verhuisd',
                    'Iemand die tijdelijk als toerist in Nederland verblijft'
                ],
                'antwoord': 2,
                'uitleg': 'De eerste generatie is zelf in het buitenland geboren.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom bleven veel gastarbeiders die in de jaren 60 kwamen uiteindelijk toch definitief in Nederland?',
                'opties': [
                    'Omdat zij verplicht werden hun paspoort in te leveren',
                    'Omdat er in Nederland geen werk meer was',
                    'Omdat het herkomstland hen de toegang weigerde',
                    'Omdat zij economisch geworteld raakten en hun gezin lieten overkomen via gezinshereniging'
                ],
                'antwoord': 3,
                'uitleg': 'Zij bouwden hier een bestaan op en kozen ervoor hun gezinnen over te laten komen.'
            }
        ]
    }
]

for o in ONDERWERPEN:
    path = os.path.join(BASE_DIR, o['file'])
    content = f"""/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §{o['paragraaf']} {o['titel']}
   buiteNLand 3 HAVO Hoofdstuk 3 (Migratie)
   ========================================================= */
DURU.register({{
  id: "{o['id']}",
  hoofdstuk: {o['hoofdstuk']},
  paragraaf: "{o['paragraaf']}",
  titel: "{o['titel']}",
  korteUitleg: "{o['korteUitleg']}",
  icoon: "{o['icoon']}",
  kleur: "{o['kleur']}",
  theorie: `{o['theorie']}`,
  vragen: {json.dumps(o['vragen'], indent=4, ensure_ascii=False)}
}});
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {path}")

print("Onderwerpen done!")
