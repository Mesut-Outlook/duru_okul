"""
Script om de 5 proeftoetsen voor Aardrijkskunde Hoofdstuk 3 (Migratie) te genereren:
examen_11.js t/m examen_15.js (ex-h3-ak-11 t/m ex-h3-ak-15).
"""
import os
import json

BASE_DIR = 'havo3/aardrijkskunde/js/data'

EXAMS = [
    {
        'file': 'examen_11.js',
        'id': 'ex-h3-ak-11',
        'hoofdstuk': 3,
        'paragraaf': '3.1',
        'hoofdstukTitel': 'Hoofdstuk 3 — Migratie',
        'titel': 'Proeftoets 11 — §3.1 Migratie in de wereld & Push-pullfactoren',
        'vak': 'Aardrijkskunde · HAVO 3 (H3)',
        'icoon': '🧳',
        'duurMin': 30,
        'vragen': [
            # 12 MC (0: 3, 1: 3, 2: 3, 3: 3)
            {
                'type': 'mc',
                'vraag': 'Wat is in de geografie de definitie van <b>buitenlandse migratie</b>?',
                'opties': [
                    'Verhuizen over een landsgrens naar een ander land om daar te gaan wonen',
                    'Verhuizen van een dorp naar een stad binnen dezelfde provincie',
                    'Reizen naar een ander land uitsluitend voor een korte zomervakantie',
                    'Dagelijks heen en weer reizen tussen woning en werk'
                ],
                'antwoord': 0,
                'uitleg': 'Buitenlandse of internationale migratie betekent dat je een landsgrens oversteekt om je elders te vestigen.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke van de volgende omstandigheden is een voorbeeld van een <b>economische pushfactor</b>?',
                'opties': [
                    'De aanwezigheid van uitstekende universiteiten in het buurland',
                    'Structurele werkloosheid en het ontbreken van inkomen in het herkomstgebied',
                    'Godsdienstvrijheid en een stabiele democratie in het bestemmingsland',
                    'Een aangenaam zonnig mediterraan klimaat'
                ],
                'antwoord': 1,
                'uitleg': 'Werkloosheid en armoede duwen mensen weg uit hun herkomstgebied (pushfactor).'
            },
            {
                'type': 'mc',
                'vraag': 'Een arts vlucht uit een dictatuur omdat hij bedreigd wordt vanwege zijn politieke uitspraken. Welk motief staat hier centraal?',
                'opties': [
                    'Ecologisch motief',
                    'Economisch motief',
                    'Politiek motief',
                    'Sociaal motief'
                ],
                'antwoord': 2,
                'uitleg': 'Vluchten voor dictatuur, oorlog of politieke vervolging is een politiek migratiemotief.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste verschil tussen <b>gezinsvorming</b> en <b>gezinshereniging</b>?',
                'opties': [
                    'Gezinshereniging is illegaal; gezinsvorming is legaal',
                    'Bij gezinshereniging verhuist men binnen Nederland; bij gezinsvorming naar het buitenland',
                    'Gezinshereniging betreft alleen grootouders; gezinsvorming betreft alleen baby\'s',
                    'Bij gezinshereniging laat men bestaande gezinsleden overkomen; bij gezinsvorming trouwt men met iemand uit het buitenland'
                ],
                'antwoord': 3,
                'uitleg': 'Gezinshereniging brengt een reeds bestaand huwelijk of gezin samen; bij gezinsvorming trouwt een inwoner met een partner uit het buitenland.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'In het model van Everett Lee zijn pushfactoren de aantrekkelijke kanten van het bestemmingsland die migranten lokken.',
                'antwoord': False,
                'uitleg': 'Onwaar. Pushfactoren zijn de afstotende omstandigheden in het herkomstland; pullfactoren zijn de aantrekkende krachten van het doelland.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Een kennismigrant is een arbeidsmigrant die verhuist vanwege specialistische kennis die schaars is in het bestemmingsland.',
                'antwoord': True,
                'uitleg': 'Waar. Denk aan IT-engineers, biotechnologen of medisch onderzoekers.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men onder een <b>statushouder</b> in het Nederlandse asielsysteem?',
                'opties': [
                    'Een asielzoeker wiens asielverzoek officieel is ingewilligd en die een verblijfsvergunning heeft gekregen',
                    'Een toerist die langer dan drie maanden in een hotel verblijft',
                    'Een buitenlandse diplomaat met een diplomatiek paspoort',
                    'Een buitenlandse student die tijdelijk stage loopt bij een bedrijf'
                ],
                'antwoord': 0,
                'uitleg': 'Een statushouder is een erkende vluchteling met een geldige verblijfsvergunning.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat voor soort migrant is iemand die Tuvalu verlaat omdat zijn eiland onbewoonbaar wordt door zeespiegelstijging?',
                'opties': [
                    'Een economische gelukszoeker',
                    'Een klimaatvluchteling (fysisch motief)',
                    'Een gezinshereniger',
                    'Een illegale handelaar'
                ],
                'antwoord': 1,
                'uitleg': 'Mensen die vluchten voor overstromingen, droogte of zeespiegelstijging zijn klimaatvluchtelingen.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke barrière vormt een typisch voorbeeld van een <b>fysieke tussenliggende hindernis</b>?',
                'opties': [
                    'Het belastingstelsel in het bestemmingsland',
                    'Het ontbreken van familieleden in het doelland',
                    'De gevaarlijke oversteek van de Middellandse Zee in wankele bootjes',
                    'Het moeten leren van een nieuwe taal op school'
                ],
                'antwoord': 2,
                'uitleg': 'Grote afstanden, woestijnen en gevaarlijke zeeroutes zijn fysieke tussenliggende hindernissen.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom kiezen veel migranten voor een land waar de eigen taal al gesproken wordt (bijv. Franstalige Afrikanen naar Frankrijk)?',
                'opties': [
                    'Omdat de grondwet van het herkomstland andere landen verbiedt',
                    'Omdat vliegtickets naar die landen altijd gratis zijn',
                    'Omdat ze daar verplicht in het leger moeten dienen',
                    'Omdat de taalovereenkomst een sterke culturele pullfactor vormt die integratie vergemakkelijkt'
                ],
                'antwoord': 3,
                'uitleg': 'Taal en historische banden verlagen de culturele drempel en trekken migranten aan.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'Iemand die verhuist van een boerderij in Drenthe naar een appartement in Amsterdam is een internationale migrant.',
                'antwoord': False,
                'uitleg': 'Onwaar. Dit is binnenlandse migratie, omdat er geen landsgrens wordt overgestoken.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Sociale netwerken van eerdere migranten verlagen de tussenliggende hindernissen voor nieuwe nieuwkomers.',
                'antwoord': True,
                'uitleg': 'Waar. Familie en dorpsgenoten bieden opvang, leningen en advies, waardoor de drempel daalt.'
            },
            # 2 Invul
            {
                'type': 'invul',
                'vraag': 'Vul de juiste term in: Factoren die mensen aantrekken naar een bestemmingsgebied noemen geografen ...',
                'antwoord': 'pullfactoren|pull-factoren|pullfactor|pull-factor',
                'uitleg': 'Pullfactoren zijn de aantrekkingskrachten van een gebied.'
            },
            {
                'type': 'invul',
                'vraag': 'Vul de term in: Iemand die zijn geboorteland definitief verlaat om ergens anders te gaan wonen, is voor dat geboorteland een ...',
                'antwoord': 'emigrant',
                'uitleg': 'Een emigrant vertrekt uit zijn land (immigrant komt binnen).'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Wat is een voorbeeld van een <b>sociale pullfactor</b>?',
                'opties': [
                    'De aanwezigheid van familieleden en een hechte gemeenschap van landgenoten',
                    'Een hoog minimumloon bij fabrieken',
                    'Het ontbreken van godsdienstvrijheid in het herkomstland',
                    'Een aardbeving die de eigen woning verwoestte'
                ],
                'antwoord': 0,
                'uitleg': 'Familiebanden en vrienden vallen onder sociale pullfactoren.'
            },
            {
                'type': 'mc',
                'vraag': 'Hoe noemen we het vertrek van mensen uit een land om te ontkomen aan oorlog en vervolging?',
                'opties': [
                    'Vrijwillige arbeidsmigratie',
                    'Gedwongen migratie / vluchtmigratie',
                    'Pensioenmigratie',
                    'Toeristische rondreis'
                ],
                'antwoord': 1,
                'uitleg': 'Vluchten voor levensbedreigende situaties is gedwongen migratie.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke rol spelen moderne smartphones en sociale media bij hedendaagse migratie?',
                'opties': [
                    'Zij maken reizen onmogelijk door strikte overheidscontroles',
                    'Zij zorgen ervoor dat niemand meer wil verhuizen',
                    'Zij verlagen informatiehindernissen door realtime contact over routes, kosten en smokkelaars',
                    'Zij vervangen de fysieke verhuizing volledig door virtuele aanwezigheid'
                ],
                'antwoord': 2,
                'uitleg': 'Smartphones stellen migranten in staat contact te houden met thuis en routes te plannen.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat gebeurt er als de tussenliggende hindernissen tussen twee landen extreem hoog worden (bijv. streng bewaakte muren en zeeblokkades)?',
                'opties': [
                    'De pushfactoren verdwijnen direct uit het herkomstland',
                    'Iedereen besluit spontaan een vliegticket te boeken',
                    'De migratiestroom neemt automatisch met 100% toe',
                    'De migratiestroom wordt afgeremd of wijkt uit naar veel gevaarlijkere alternatieve routes'
                ],
                'antwoord': 3,
                'uitleg': 'Hoge hindernissen remmen migratie af of dwingen migranten in handen van illegale mensensmokkelaars.'
            },
            # 2 Open
            {
                'type': 'open',
                'vraag': 'Noem de term voor het overbrengen van reeds bestaande gezinsleden (zoals partner of minderjarige kinderen) naar het land waar de migrant al woont.',
                'sleutelwoorden': ['gezinshereniging'],
                'minTreffers': 1,
                'modelantwoord': 'Deze vorm van migratie heet gezinshereniging.',
                'uitleg': 'Gezinshereniging herenigt gezinsleden die al een gezin vormden voor de migratie.'
            },
            {
                'type': 'open',
                'vraag': 'Hoe noemt men de afstotende factoren in een herkomstgebied die mensen stimuleren om hun woonplaats te verlaten?',
                'sleutelwoorden': ['pushfactoren/pushfactor/push'],
                'minTreffers': 1,
                'modelantwoord': 'Dit worden pushfactoren (of afstotende factoren) genoemd.',
                'uitleg': 'Pushfactoren duwen mensen weg uit hun herkomstland.'
            }
        ]
    },
    {
        'file': 'examen_12.js',
        'id': 'ex-h3-ak-12',
        'hoofdstuk': 3,
        'paragraaf': '3.2',
        'hoofdstukTitel': 'Hoofdstuk 3 — Migratie',
        'titel': 'Proeftoets 12 — §3.2 Gevolgen voor de herkomstgebieden & Braindrain',
        'vak': 'Aardrijkskunde · HAVO 3 (H3)',
        'icoon': '📉',
        'duurMin': 30,
        'vragen': [
            # 12 MC (0: 3, 1: 3, 2: 3, 3: 3)
            {
                'type': 'mc',
                'vraag': 'Wat is het directe gevolg voor een herkomstland wanneer veel artsen en docenten emigreren naar rijke landen?',
                'opties': [
                    'Er ontstaat een braindrain waardoor de gezondheidszorg en het onderwijs in het herkomstland verzwakken',
                    'Het land krijgt direct een overschot aan hoogwaardige ziekenhuizen',
                    'De universiteiten in het herkomstland worden gratis voor iedereen',
                    'Het geboortecijfer verdubbelt direct'
                ],
                'antwoord': 0,
                'uitleg': 'Braindrain berooft herkomstlanden van hun broodnodige intellectuele en medische kader.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom zijn <b>geldzendingen (remittances)</b> vaak effectiever tegen acute armoede dan officiële buitenlandse hulpgelden?',
                'opties': [
                    'Omdat hulpgelden altijd in contanten op straat worden uitgedeeld',
                    'Omdat geldzendingen direct bij de achtergebleven familieleden terechtkomen zonder tussenkomst van corrupte bureaucratie',
                    'Omdat migranten verplicht zijn alleen voedselpakketten op te sturen',
                    'Omdat ontwikkelingshulp verboden is volgens de Verenigde Naties'
                ],
                'antwoord': 1,
                'uitleg': 'Geldzendingen gaan rechtstreeks naar huishoudens en worden besteed aan eerste levensbehoeften, zorg en bouw.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat bedoelt men met <b>selectieve migratie</b>?',
                'opties': [
                    'Migratie waarbij de overheid willekeurig mensen aanwijst die moeten vertrekken',
                    'Migratie waarbij uitsluitend baby\'s en peuters verhuizen',
                    'Het verschijnsel dat migranten geen doorsnede van de bevolking vormen, maar vooral bestaan uit jonge, actieve volwassenen',
                    'Het verhuizen naar een land dat met een dobbelsteen gekozen is'
                ],
                'antwoord': 2,
                'uitleg': 'Selectieve migratie betekent dat bepaalde groepen (vooral jonge, energieke mensen van 18-35 jaar) oververtegenwoordigd zijn.'
            },
            {
                'type': 'mc',
                'vraag': 'Onder welke voorwaarde kan een braindrain op de lange termijn omslaan in een <b>braingain</b>?',
                'opties': [
                    'Als het herkomstland besluit alle grenzen voorgoed af te sluiten',
                    'Als migranten al hun bezittingen verbranden',
                    'Als de achterblijvers stoppen met werken op het platteland',
                    'Als geëmigreerde specialisten terugkeren (retourmigratie) en kennis, innovatie en investeringen meebrengen'
                ],
                'antwoord': 3,
                'uitleg': 'Terugkerende migranten met buitenlandse diploma\'s en spaargeld versterken de thuiseconomie (braingain).'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'Geldzendingen van migranten naar hun vaderland zijn wereldwijd kleiner dan de jaarlijkse budgetten voor ontwikkelingssamenwerking.',
                'antwoord': False,
                'uitleg': 'Onwaar. Geldzendingen (honderden miljarden dollars per jaar) zijn wereldwijd ruim drie keer zo groot als alle officiële ontwikkelingshulp.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Migratienetwerken tussen herkomst- en bestemmingsdorpen stimuleren volgmigratie.',
                'antwoord': True,
                'uitleg': 'Waar. Eerdere migranten helpen latere migranten met informatie, opvang en werk.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Welke demografische piramidevorm ontstaat er vaak in plattelandsdorpen waaruit veel jonge mensen zijn vertrokken?',
                'opties': [
                    'Een zandlopermodel met veel ouderen en jonge kinderen, maar een uitgeholde middengroep van twintigers en dertigers',
                    'Een perfecte driehoek met een enorme piek in de categorie 20-30 jaar',
                    'Een cirkelvormige piramide',
                    'Een toren met uitsluitend pasgeboren baby\'s'
                ],
                'antwoord': 0,
                'uitleg': 'Omdat de jonge volwassenen wegtrekken, ontbreekt de middengroep van potentiële arbeidskrachten.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een economisch risico voor een familie die volledig afhankelijk is van geldzendingen uit het buitenland?',
                'opties': [
                    'Zij worden verplicht om direct te emigreren',
                    'Als de migrant in het doelland werkloos raakt of de wisselkoers instort, verliest de familie plotseling haar hele inkomen',
                    'Zij mogen geen Nederlandse producten meer kopen',
                    'Het herkomstland ontneemt hen het stemrecht'
                ],
                'antwoord': 1,
                'uitleg': 'Volledige afhankelijkheid van geldzendingen maakt gezinnen kwetsbaar voor economische crises in het bestemmingsland.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat betekent de term <b>retourmigratie</b>?',
                'opties': [
                    'Het verhuizen van het ene buitenlandse land naar het andere',
                    'Het op vakantie gaan naar een pretpark',
                    'Het na verloop van tijd definitief terugkeren van migranten naar hun land van herkomst',
                    'Het weigeren van een paspoort aan grensoverschrijdende reizigers'
                ],
                'antwoord': 2,
                'uitleg': 'Retourmigratie is de terugkeer naar het geboorteland na een periode van wonen en werken in het buitenland.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat kan een negatief sociaal gevolg zijn van grootschalige emigratie van jonge ouders?',
                'opties': [
                    'Alle scholen in het dorp worden overvol',
                    'Er zijn te veel volwassen mannen in het dorp',
                    'De huizenprijzen dalen naar nul euro',
                    'Veel kinderen groeien op zonder hun ouders en worden opgevoed door grootouders (achterblijvers)'
                ],
                'antwoord': 3,
                'uitleg': 'Achterblijvende kinderen missen de dagelijkse opvoeding en steun van hun ouders.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'Braindrain zorgt voor een snelle stijging van het aantal gekwalificeerde chirurgen in Afrikaanse dorpsziekenhuizen.',
                'antwoord': False,
                'uitleg': 'Onwaar. Braindrain zorgt juist voor een ernstig tekort aan artsen en chirurgen doordat zij naar rijkere landen vertrekken.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Veel geldzendingen worden door gezinnen geïnvesteerd in het bouwen van betere stenen huizen en het betalen van schoolgeld.',
                'antwoord': True,
                'uitleg': 'Waar. Het geld verbetert de directe levensstandaard en de toekomstkansen van kinderen.'
            },
            # 2 Invul
            {
                'type': 'invul',
                'vraag': 'Vul de geografische term in: Het verschijnsel dat hoogopgeleide specialisten massaal hun geboorteland verlaten heet ...',
                'antwoord': 'braindrain|brain drain',
                'uitleg': 'Braindrain beschrijft het verlies van hoogopgeleid personeel.'
            },
            {
                'type': 'invul',
                'vraag': 'Vul de Engelse term in: Geld dat migranten overboeken naar familieleden in het herkomstland noemen we ...',
                'antwoord': 'remittances|remittance|geldzendingen',
                'uitleg': 'Remittances (geldzendingen) zijn overschrijvingen naar het thuisfront.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Hoe kan de overheid van een herkomstland proberen om braindrain tegen te gaan?',
                'opties': [
                    'Door salarissen, werkomstandigheden en onderzoeksfaciliteiten voor specialisten in eigen land sterk te verbeteren',
                    'Door alle universiteiten in het land te sluiten',
                    'Door een algeheel verbod op internet in te voeren',
                    'Door artsen te verbieden een medische opleiding te volgen'
                ],
                'antwoord': 0,
                'uitleg': 'Betere salarissen en carrièremogelijkheden verkleinen de drang om te emigreren.'
            },
            {
                'type': 'mc',
                'vraag': 'Welk effect heeft de bouw van nieuwe huizen met geldzendingen op de lokale economie van een dorp?',
                'opties': [
                    'Het leidt tot onmiddellijke faillissementen van alle lokale bouwvakkers',
                    'Het stimuleert lokale werkgelegenheid voor metselaars, timmerlieden en leveranciers van bouwmaterialen',
                    'Het zorgt ervoor dat niemand meer een woning kan bezitten',
                    'Het heeft geen enkele economische invloed'
                ],
                'antwoord': 1,
                'uitleg': 'De bouwactiviteit creëert banen en omzet voor lokale winkels en vaklieden.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom emigreren hoogopgeleide IT\'ers uit India vaak naar Silicon Valley of West-Europa?',
                'opties': [
                    'Omdat India geen computers heeft',
                    'Omdat de Indiase overheid emigratie verplicht stelt voor informatici',
                    'Vanwege de enorme inkomensverschillen en doorgroeimogelijkheden bij toonaangevende techbedrijven',
                    'Omdat de vlucht naar de VS gratis is'
                ],
                'antwoord': 2,
                'uitleg': 'Veel hogere salarissen en geavanceerde technologie fungeren als sterke pullfactor.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is <b>kettingmigratie</b> (volgmigratie)?',
                'opties': [
                    'Migratie waarbij mensen aan elkaar worden vastgeketend tijdens het transport',
                    'Het verhuizen van gevangenen naar een ander land',
                    'Het verplicht rondreizen van diplomaten',
                    'Het proces waarbij de komst van één migrant leidt tot de migratie van familie en dorpsgenoten via gevestigde netwerken'
                ],
                'antwoord': 3,
                'uitleg': 'Kettingmigratie beschrijft het opvolgende karakter van migratie via bekenden en verwanten.'
            },
            # 2 Open
            {
                'type': 'open',
                'vraag': 'Hoe noemt men het positieve effect waarbij terugkerende migranten nieuwe vaardigheden en investeringen meebrengen naar hun herkomstland?',
                'sleutelwoorden': ['braingain/brain gain'],
                'minTreffers': 1,
                'modelantwoord': 'Dit positieve effect heet braingain.',
                'uitleg': 'Braingain is het tegenovergestelde van braindrain.'
            },
            {
                'type': 'open',
                'vraag': 'Welke term gebruiken we voor de overboekingen van verdiend salaris door migranten naar hun familie thuis?',
                'sleutelwoorden': ['remittances/geldzendingen'],
                'minTreffers': 1,
                'modelantwoord': 'Dit noemen we geldzendingen of remittances.',
                'uitleg': 'Geldzendingen ondersteunen miljoenen gezinnen in ontwikkelingslanden.'
            }
        ]
    },
    {
        'file': 'examen_13.js',
        'id': 'ex-h3-ak-13',
        'hoofdstuk': 3,
        'paragraaf': '3.3',
        'hoofdstukTitel': 'Hoofdstuk 3 — Migratie',
        'titel': 'Proeftoets 13 — §3.3 Gevolgen voor bestemmingsgebieden & Segregatie',
        'vak': 'Aardrijkskunde · HAVO 3 (H3)',
        'icoon': '🏙️',
        'duurMin': 30,
        'vragen': [
            # 12 MC (0: 3, 1: 3, 2: 3, 3: 3)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste kenmerk van een <b>etnische wijk</b> in een grote stad?',
                'opties': [
                    'Een buurt waar een specifieke bevolkingsgroep sterk geconcentreerd woont, met eigen winkels en voorzieningen',
                    'Een wijk waar alleen toeristen mogen overnachten',
                    'Een industriegebied zonder woningen',
                    'Een wijk waarin alle huizen precies dezelfde kleur hebben'
                ],
                'antwoord': 0,
                'uitleg': 'Etnische wijken ontstaan door ruimtelijke concentratie van migrantengroepen (bijv. Chinatown of de Indische Buurt).'
            },
            {
                'type': 'mc',
                'vraag': 'Wat houdt het integratiemodel van een <b>melting pot</b> (smeltkroes) in?',
                'opties': [
                    'Iedereen behoudt zijn eigen paspoort en woont in afzonderlijke reservaten',
                    'Verschillende immigrantenculturen smelten samen tot één geheel nieuwe, gezamenlijke nationale cultuur',
                    'Alle buitenlanders worden na vijf jaar teruggestuurd',
                    'De staat verbiedt alle religieuze feestdagen'
                ],
                'antwoord': 1,
                'uitleg': 'In een melting pot versmelten verschillende culturen tot één nieuwe identiteit (historisch ideaal van de VS).'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een groot risico van sterke <b>sociale segregatie</b> tussen bevolkingsgroepen in een stad?',
                'opties': [
                    'De huizenprijzen worden overal in de stad identiek',
                    'Er komen te veel sportvelden in de wijk',
                    'Groepen leven langs elkaar heen, waardoor vooroordelen en wantrouwen toenemen',
                    'Iedereen spreekt automatisch dezelfde taal'
                ],
                'antwoord': 2,
                'uitleg': 'Gebrek aan contact tussen groepen leidt tot polarisatie, onbegrip en segregatie.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke omschrijving past het best bij het sociologische begrip <b>assimilatie</b>?',
                'opties': [
                    'Het vreedzaam naast elkaar leven van verschillende culturen met behoud van tradities',
                    'Het tijdelijk verblijven in een asielzoekerscentrum',
                    'Het organiseren van een internationaal cultuurfestival',
                    'Het zo volledig overnemen van de dominante cultuur dat de oorspronkelijke cultuurkenmerken verdwijnen'
                ],
                'antwoord': 3,
                'uitleg': 'Bij assimilatie past de minderheidsgroep zich volledig aan en geeft haar eigen kenmerken op.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'Ruimtelijke segregatie ontstaat uitsluitend doordat de overheid wetten maakt die bepalen waar migranten moeten wonen.',
                'antwoord': False,
                'uitleg': 'Onwaar. Het ontstaat vooral door inkomensverschillen, woningmarktprijzen en de wens om dicht bij familie en bekenden te wonen.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Een multiculturele samenleving kenmerkt zich door de aanwezigheid van diverse culturen, religies en leefstijlen.',
                'antwoord': True,
                'uitleg': 'Waar. Dit is de definitie van een multiculturele samenleving.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Hoe kan een gemeente ruimtelijke segregatie in een achterstandswijk actief bestrijden?',
                'opties': [
                    'Door een mix van sociale huurwoningen en duurdere koopwoningen te bouwen (differentiatie)',
                    'Door alle nieuwbouw in de wijk direct te verbieden',
                    'Door hekken rond de wijk te plaatsen',
                    'Door het openbaar vervoer naar de wijk stop te zetten'
                ],
                'antwoord': 0,
                'uitleg': 'Woningdifferentiatie trekt verschillende inkomensgroepen aan en doorbreekt eenzijdige concentratie.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een voorbeeld van <b>acculturatie</b> in de Nederlandse samenleving?',
                'opties': [
                    'Het sluiten van alle buitenlandse ambassades in Den Haag',
                    'Het inburgeren van buitenlandse gerechten zoals döner kebab en bami in de Nederlandse eetcultuur',
                    'Het verbieden van alle musea over de koloniale geschiedenis',
                    'Het verplichten van klederdracht op feestdagen'
                ],
                'antwoord': 1,
                'uitleg': 'Acculturatie is de wederzijdse culturele beïnvloeding, zoals te zien is in onze eetcultuur en taal.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men onder een taalachterstand bij nieuwkomers op de arbeidsmarkt?',
                'opties': [
                    'Het feit dat zij te veel verschillende talen vloeiend spreken',
                    'De verplichting om op het werk alleen Latijn te schrijven',
                    'Het onvoldoende beheersen van de taal van het bestemmingsland, wat doorgroeikansen naar hogere functies belemmert',
                    'Het spreken met een regionaal accent'
                ],
                'antwoord': 2,
                'uitleg': 'Een taalachterstand maakt solliciteren en communiceren op de werkvloer moeilijker.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke rol spelen buurthuizen en sportverenigingen in een diverse stadswijk?',
                'opties': [
                    'Zij stimuleren segregatie door groepen strikt te scheiden',
                    'Zij zijn uitsluitend bedoeld voor buitenlandse toeristen',
                    'Zij controleren de geldigheid van verblijfsvergunningen',
                    'Zij fungeren als ontmoetingsplekken die sociale cohesie en integratie tussen bewoners bevorderen'
                ],
                'antwoord': 3,
                'uitleg': 'Sport en ontmoeting brengen mensen met verschillende achtergronden met elkaar in contact.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'Bij integratie is het verboden om thuis nog de taal van het herkomstland te spreken of eigen feestdagen te vieren.',
                'antwoord': False,
                'uitleg': 'Onwaar. Bij integratie behoudt men juist de vrijheid van de eigen cultuur en godsdienst, zolang men de wet respecteert.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Discriminatie op de arbeidsmarkt kan ertoe leiden dat gekwalificeerde migranten moeilijker aan een passende baan komen.',
                'antwoord': True,
                'uitleg': 'Waar. Vooroordelen en discriminatie belemmeren gelijke kansen op werk.'
            },
            # 2 Invul
            {
                'type': 'invul',
                'vraag': 'Vul de term in: Het ruimtelijk gescheiden wonen van verschillende bevolkingsgroepen in een stad heet ruimtelijke ...',
                'antwoord': 'segregatie',
                'uitleg': 'Ruimtelijke segregatie is de scheiding van groepen over wijken.'
            },
            {
                'type': 'invul',
                'vraag': 'Vul in: Een samenleving waarin mensen met verschillende culturele achtergronden vreedzaam samenleven heet een ... samenleving.',
                'antwoord': 'multiculturele',
                'uitleg': 'Een multiculturele samenleving omvat meerdere culturen.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Wat is het verschil tussen het concept van een <b>salad bowl</b> en een <b>melting pot</b>?',
                'opties': [
                    'In een salad bowl behouden de culturen hun eigen unieke smaak en identiteit, terwijl ze samen één geheel vormen',
                    'Een salad bowl geldt alleen voor vegetarische restaurants',
                    'In een salad bowl mag niemand met elkaar praten',
                    'Een melting pot is uitsluitend van toepassing op Europese hoofdsteden'
                ],
                'antwoord': 0,
                'uitleg': 'Salad bowl = culturele diversiteit blijft zichtbaar; melting pot = culturen versmelten tot één geheel.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom zijn arbeidsmigranten in bestemmingslanden vaak oververtegenwoordigd in flexibele en laagbetaalde sectoren?',
                'opties': [
                    'Omdat de wet bepaalt dat migranten geen vast contract mogen krijgen',
                    'Omdat zij vaak worden ingezet op zwaar, repetitief werk in logistiek, tuinbouw en schoonmaak waar lokale arbeidskrachten schaars zijn',
                    'Omdat zij geen salaris wensen te ontvangen',
                    'Omdat buitenlandse diploma\'s automatisch ongeldig zijn in de hele wereld'
                ],
                'antwoord': 1,
                'uitleg': 'Arbeidsmigranten vullen tekorten aan de onderkant van de arbeidsmarkt op.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaan geografen onder <b>witte vlucht</b> (white flight) in stedelijke gebieden?',
                'opties': [
                    'Het massaal vliegen van toeristen naar besneeuwde skigebieden',
                    'Het verdwijnen van witte verf in doe-het-zelfzaken',
                    'Het wegverhuizen van oorspronkelijke autochtone bewoners uit stadswijken zodra het aandeel migranten sterk toeneemt',
                    'De verplichte verhuizing van ambtenaren naar Den Haag'
                ],
                'antwoord': 2,
                'uitleg': 'White flight beschrijft de verhuizing van autochtone middenklassengezinnen naar buitenwijken of groeikernen.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke factor draagt het meest bij aan een succesvolle integratie van immigranten in het bestemmingsland?',
                'opties': [
                    'Het isoleren van nieuwkomers in afgesloten opvangkampen',
                    'Het verbieden van contact met buurtbewoners',
                    'Het afpakken van alle communicatiemiddelen',
                    'Snel de taal leren, een betaalde baan vinden en actieve deelname aan het maatschappelijk leven'
                ],
                'antwoord': 3,
                'uitleg': 'Taal en werk zijn de belangrijkste hefbomen voor maatschappelijke participatie en integratie.'
            },
            # 2 Open
            {
                'type': 'open',
                'vraag': 'Hoe noemen we het sociologische proces waarbij een immigrantengroep de heersende cultuur zó volledig overneemt dat haar oorspronkelijke cultuur verdwijnt?',
                'sleutelwoorden': ['assimilatie'],
                'minTreffers': 1,
                'modelantwoord': 'Dit proces wordt assimilatie genoemd.',
                'uitleg': 'Assimilatie is de volledige opname in een cultuur ten koste van de eigen tradities.'
            },
            {
                'type': 'open',
                'vraag': 'Wat is het geografische begrip voor het proces van wederzijdse cultuurbeïnvloeding door langdurig direct contact tussen bevolkingsgroepen?',
                'sleutelwoorden': ['acculturatie'],
                'minTreffers': 1,
                'modelantwoord': 'Dit proces heet acculturatie.',
                'uitleg': 'Acculturatie is de wederzijdse beïnvloeding van culturen.'
            }
        ]
    },
    {
        'file': 'examen_14.js',
        'id': 'ex-h3-ak-14',
        'hoofdstuk': 3,
        'paragraaf': '3.4',
        'hoofdstukTitel': 'Hoofdstuk 3 — Migratie',
        'titel': 'Proeftoets 14 — §3.4 Migratie en de Europese Unie & Schengen',
        'vak': 'Aardrijkskunde · HAVO 3 (H3)',
        'icoon': '🇪🇺',
        'duurMin': 30,
        'vragen': [
            # 12 MC (0: 3, 1: 3, 2: 3, 3: 3)
            {
                'type': 'mc',
                'vraag': 'Welk land behoort wel tot het Schengengebied maar is GEEN lid van de Europese Unie?',
                'opties': [
                    'Zwitserland',
                    'Frankrijk',
                    'Duitsland',
                    'België'
                ],
                'antwoord': 0,
                'uitleg': 'Zwitserland en Noorwegen zijn geen EU-lid, maar nemen wel deel aan het Schengenverdrag (geen grenscontroles).'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het hoofddoel van de <b>Dublin-verordening</b> binnen de Europese Unie?',
                'opties': [
                    'Het invoeren van een gezamenlijke Europese dienstplicht',
                    'Vaststellen welke lidstaat verantwoordelijk is voor de behandeling van een specifieke asielaanvraag',
                    'Het bepalen van de graanprijzen voor Ierse landbouwers',
                    'Het afschaffen van alle paspoorten wereldwijd'
                ],
                'antwoord': 1,
                'uitleg': 'De Dublin-verordening voorkomt dat asielzoekers in meerdere EU-landen tegelijk asiel aanvragen.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom heeft de afschaffing van de binnengrenzen in het Schengengebied geleid tot strengere bewaking van de buitengrenzen?',
                'opties': [
                    'Omdat de Europese Unie geen handel meer wil drijven met de rest van de wereld',
                    'Omdat vliegtuigen niet meer mogen landen op Europese vliegvelden',
                    'Omdat een migrant die eenmaal binnen is, ongehinderd door kan reizen naar alle andere aangesloten landen',
                    'Omdat elk Schengenland verplicht zijn eigen leger heeft opgeheven'
                ],
                'antwoord': 2,
                'uitleg': 'Zonder interne controles moet de controle aan de externe grens waterdicht zijn.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke instantie coördineert de bewaking van de Europese buitengrenzen en bestrijdt mensensmokkel op zee?',
                'opties': [
                    'De Wereldbank',
                    'De NAVO-veiligheidsraad',
                    'Unicef',
                    'Frontex'
                ],
                'antwoord': 3,
                'uitleg': 'Frontex is het Europese grens- en kustwachtagentschap.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'Binnen de Europese Unie hebben burgers van alle lidstaten een speciale werkvergunning nodig om in een ander EU-land te werken.',
                'antwoord': False,
                'uitleg': 'Onwaar. Binnen de EU geldt het grondrecht op vrij verkeer van werknemers zonder werkvergunning.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Het Verdrag van Schengen werd oorspronkelijk ondertekend in een klein plaatsje in Luxemburg.',
                'antwoord': True,
                'uitleg': 'Waar. Schengen is een dorp in Luxemburg op het drielandenpunt met Frankrijk en Duitsland.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Wat houdt de zogeheten <b>Turkijedeal</b> van 2016 tussen de EU en Turkije in?',
                'opties': [
                    'Turkije houdt migranten en mensensmokkelaars tegen in ruil voor Europese financiële steun voor vluchtelingenopvang',
                    'Alle inwoners van Turkije krijgen automatisch een visum voor heel Europa',
                    'Turkije wordt direct volwaardig lid van de eurozone',
                    'Europese burgers mogen gratis naar Turkije verhuizen'
                ],
                'antwoord': 0,
                'uitleg': 'De Turkijedeal was bedoeld om de gevaarlijke overtocht over de Egeïsche Zee naar Griekenland te stoppen.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het gevolg van het principe van \'veilig derde land\' in het Europese asielbeleid?',
                'opties': [
                    'Asielzoekers krijgen in ieder land automatisch gratis huisvesting',
                    'Een asielzoeker kan worden teruggestuurd naar een land buiten de EU waar hij al veilig was en bescherming kon krijgen',
                    'Alle niet-Europese landen worden als onveilig beschouwd',
                    'Vluchtelingen mogen niet meer reizen per trein'
                ],
                'antwoord': 1,
                'uitleg': 'Als een migrant via een veilig land reisde, kan hij daarnaartoe worden teruggestuurd.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke landen dragen door de Dublin-verordening historisch gezien de zwaarste lasten bij de opvang van bootvluchtelingen?',
                'opties': [
                    'Zweden, Finland en Noorwegen',
                    'Polen, Tsjechië en Slowakije',
                    'Italië, Griekenland en Spanje',
                    'Ierland en het Verenigd Koninkrijk'
                ],
                'antwoord': 2,
                'uitleg': 'Middellandse Zeelanden liggen op de primaire aankomstroutes van migranten vanuit Afrika en het Midden-Oosten.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een belangrijk economisch voordeel voor Nederlandse bedrijven van het vrije verkeer van werknemers binnen de EU?',
                'opties': [
                    'Bedrijven hoeven geen salaris meer te betalen aan buitenlandse krachten',
                    'Er mag geen belasting meer worden geheven op winst',
                    'Bedrijven mogen onbeperkt contant geld exporteren',
                    'Zij kunnen makkelijker personeelstekorten opvullen met werknemers uit andere EU-landen'
                ],
                'antwoord': 3,
                'uitleg': 'Bedrijven kunnen soepel vakmensen en seizoensarbeiders uit de hele EU aannemen.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'Het Verenigd Koninkrijk maakt sinds de Brexit nog altijd deel uit van het Schengengebied.',
                'antwoord': False,
                'uitleg': 'Onwaar. Het VK maakte zelfs voor de Brexit al geen deel uit van Schengen en controleerde altijd paspoorten.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'De term \'Fort Europa\' slaat op de zware grensbewaking en afschrikkingsmaatregelen aan de Europese buitengrenzen.',
                'antwoord': True,
                'uitleg': 'Waar. Het bekritiseert het beleid dat Europa moeilijk toegankelijk maakt voor vluchtelingen.'
            },
            # 2 Invul
            {
                'type': 'invul',
                'vraag': 'Vul de naam in van het Europese grens- en kustwachtagentschap dat de buitengrenzen bewaakt: ...',
                'antwoord': 'frontex',
                'uitleg': 'Frontex is het Europese agentschap voor grensbeheer.'
            },
            {
                'type': 'invul',
                'vraag': 'Vul de stad in: De Europese asielverordening die bepaalt welk land een asielaanvraag behandelt is vernoemd naar de Ierse hoofdstad ...',
                'antwoord': 'dublin',
                'uitleg': 'De Dublin-verordening regelt de asieltoewijzing.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Wat is een <b>irreguliere migrant</b> (ook wel ongedocumenteerde genoemd)?',
                'opties': [
                    'Iemand die zonder geldige visa of verblijfspapieren in een land verblijft of de grens oversteekt',
                    'Een toerist die met een geldig paspoort op Schiphol landt',
                    'Een student die een beurs ontvangt van de Europese Unie',
                    'Een diplomaat die namens de VN reist'
                ],
                'antwoord': 0,
                'uitleg': 'Irreguliere migratie vindt plaats buiten de officiële wetten en visumregels om.'
            },
            {
                'type': 'mc',
                'vraag': 'Welk probleem ontstaat er als EU-landen geen overeenstemming kunnen bereiken over een eerlijke herverdeling van asielzoekers?',
                'opties': [
                    'De euro wordt onmiddellijk afgeschaft',
                    'Grenslanden raken overbelast en de solidariteit en het vertrouwen tussen lidstaten komt ernstig onder druk te staan',
                    'Alle grenzen in de wereld worden direct gesloten',
                    'Er mag geen handel meer worden gedreven tussen EU-lidstaten'
                ],
                'antwoord': 1,
                'uitleg': 'Gebrek aan herverdeling leidt tot overvolle opvangkampen in Zuid-Europa en politieke ruzies.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat gebeurt er als een land in noodsituaties tijdelijk weer grenscontroles aan zijn binnengrenzen invoert (bijv. tijdens een pandemie)?',
                'opties': [
                    'Het land wordt automatisch uit de EU gezet',
                    'Het land mag nooit meer meedoen aan Schengen',
                    'Het Schengenverdrag staat toe dat dit tijdelijk en onder strikte voorwaarden gebeurt bij ernstige bedreigingen van de openbare orde',
                    'Alle buitenlandse inwoners moeten het land binnen 24 uur verlaten'
                ],
                'antwoord': 2,
                'uitleg': 'In uitzonderlijke noodsituaties mogen lidstaten tijdelijk controles herinvoeren.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom investeren EU-landen in ontwikkelingsprojecten in Afrikaanse herkomstlanden van migranten?',
                'opties': [
                    'Om te zorgen dat alle inwoners daar verplicht Frans gaan leren',
                    'Om het toerisme vanuit Europa naar die landen te verbieden',
                    'Om alle fabrieken in Europa te sluiten en daarheen te verplaatsen',
                    'Om de grondoorzaken van migratie (armoede, werkloosheid) aan te pakken zodat mensen een toekomst in eigen land zien'
                ],
                'antwoord': 3,
                'uitleg': 'Het aanpakken van grondoorzaken (pushfactoren) moet de noodzaak tot emigratie verminderen.'
            },
            # 2 Open
            {
                'type': 'open',
                'vraag': 'Noem het verdrag waarmee de vaste paspoortcontroles aan de binnengrenzen tussen de meeste Europese landen zijn afgeschaft.',
                'sleutelwoorden': ['schengen/schengenverdrag/verdrag van schengen'],
                'minTreffers': 1,
                'modelantwoord': 'Dit is het Verdrag van Schengen.',
                'uitleg': 'Schengen regelt het vrije personenverkeer.'
            },
            {
                'type': 'open',
                'vraag': 'Welke kritische benaming wordt gebruikt voor het strenge grens- en afweerbeleid aan de buitengrenzen van de EU?',
                'sleutelwoorden': ['fort europa'],
                'minTreffers': 1,
                'modelantwoord': 'Dit wordt Fort Europa genoemd.',
                'uitleg': 'Fort Europa verwijst naar de zwaar beveiligde buitengrens.'
            }
        ]
    },
    {
        'file': 'examen_15.js',
        'id': 'ex-h3-ak-15',
        'hoofdstuk': 3,
        'paragraaf': '3.5',
        'hoofdstukTitel': 'Hoofdstuk 3 — Migratie',
        'titel': 'Proeftoets 15 — §3.5 Migratie en Nederland & Examentraining Integraal',
        'vak': 'Aardrijkskunde · HAVO 3 (H3)',
        'icoon': '🎓',
        'duurMin': 35,
        'vragen': [
            # 12 MC (0: 3, 1: 3, 2: 3, 3: 3)
            {
                'type': 'mc',
                'vraag': 'Welke groep migranten kwam rond 1949-1951 na de onafhankelijkheidsoorlog naar Nederland?',
                'opties': [
                    'Indische Nederlanders en Molukkers uit voormalig Nederlands-Indië',
                    'Gastarbeiders uit Marokko en Turkije',
                    'Vluchtelingen uit voormalig Joegoslavië',
                    'Expats uit de Verenigde Staten'
                ],
                'antwoord': 0,
                'uitleg': 'Na de soevereiniteitsoverdracht van Indonesië repatrieerden honderdduizenden Indische Nederlanders en Molukkers.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom startte de Nederlandse regering in de jaren 1960 met het werven van <b>gastarbeiders</b> in Zuid-Europa en Turkije/Marokko?',
                'opties': [
                    'Omdat Nederland dreigde te ontvolken door hongersnood',
                    'Vanwege een enorm tekort aan arbeidskrachten voor zwaar lichamelijk en laagbetaald fabrieks- en havenwerk',
                    'Om de Nederlandse taal over heel de wereld te verspreiden',
                    'Omdat de Europese wetgeving dat destijds verplichtte'
                ],
                'antwoord': 1,
                'uitleg': 'De snelgroeiende Nederlandse naoorlogse industrie had dringend arbeiders nodig.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is volgens het Centraal Bureau voor de Statistiek (CBS) een <b>tweede generatie migrant</b>?',
                'opties': [
                    'Iemand die zelf in het buitenland is geboren en op latere leeftijd naar Nederland kwam',
                    'Iemand die minstens vier buitenlandse grootouders heeft',
                    'Iemand die in Nederland is geboren en van wie ten minste één ouder in het buitenland is geboren',
                    'Iemand die uitsluitend een buitenlands paspoort bezit'
                ],
                'antwoord': 2,
                'uitleg': 'Zelf in Nederland geboren + minimaal één ouder in het buitenland geboren = tweede generatie.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat houdt de <b>inburgeringsplicht</b> in Nederland in?',
                'opties': [
                    'De plicht om elk jaar minimaal één marathon te lopen',
                    'De verplichting om uitsluitend in klederdracht op feestdagen te verschijnen',
                    'De eis dat men afstand moet doen van al het spaargeld',
                    'De wettelijke verplichting voor nieuwkomers om Nederlands te leren en kennis van de samenleving op te doen via een inburgeringsexamen'
                ],
                'antwoord': 3,
                'uitleg': 'Inburgering toetst taalbeheersing en maatschappelijke kennis van nieuwkomers.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'In de jaren 1950 kwamen er meer immigranten naar Nederland dan dat er emigranten vertrokken.',
                'antwoord': False,
                'uitleg': 'Onwaar. In de jaren 50 vertrokken honderdduizenden Nederlanders naar Canada, Australië en de VS (emigratie-overschot).'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Rond de onafhankelijkheid van Suriname in 1975 verhuisde ongeveer de helft van de Surinaamse bevolking naar Nederland.',
                'antwoord': True,
                'uitleg': 'Waar. Uit onzekerheid over de toekomst kozen velen voor het behoud van het Nederlandse staatsburgerschap.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Welke migrantengroep in Nederland bestaat voornamelijk uit hoogopgeleide technici en wetenschappers die werken bij multinationals zoals ASML in Eindhoven?',
                'opties': [
                    'Kennismigranten / expats',
                    'Gastarbeiders uit de jaren 60',
                    'Seizoensplukkers in de glastuinbouw',
                    'Asielzoekers in afwachting van een status'
                ],
                'antwoord': 0,
                'uitleg': 'De Brainportregio Eindhoven trekt tienduizenden kennismigranten van over de hele wereld aan.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom leidde het verblijf van gastarbeiders in de jaren 1970 en 1980 tot een nieuwe grote migratiestroom naar Nederland?',
                'opties': [
                    'Omdat zij allemaal besloten terug te keren naar hun herkomstland',
                    'Omdat zij hun partners en kinderen lieten overkomen via gezinshereniging',
                    'Omdat zij verplicht werden hun hele dorp mee te nemen',
                    'Omdat Nederland alle grenzen met Turkije en Marokko volledig openstelde voor vrij verkeer'
                ],
                'antwoord': 1,
                'uitleg': 'Toen duidelijk werd dat arbeiders bleven, haalden zij hun gezinnen naar Nederland (gezinshereniging).'
            },
            {
                'type': 'mc',
                'vraag': 'In welke delen van Nederland is het aandeel inwoners met een migratieachtergrond het hoogst geconcentreerd?',
                'opties': [
                    'Op de Waddeneilanden en in het noorden van Friesland',
                    'In kleine plattelandsdorpen in Zeeland en Drenthe',
                    'In de vier grote steden van de Randstad (Amsterdam, Rotterdam, Den Haag en Utrecht)',
                    'Uitsluitend in de provincie Limburg'
                ],
                'antwoord': 2,
                'uitleg': 'In de grote steden heeft meer dan de helft van de bevolking een migratieachtergrond.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste verschil tussen een asielzoeker en een statushouder?',
                'opties': [
                    'Een asielzoeker heeft een Nederlands paspoort; een statushouder niet',
                    'Een asielzoeker komt uit Europa; een statushouder van buiten Europa',
                    'Een asielzoeker heeft een baan; een statushouder mag niet werken',
                    'Een asielzoeker wacht nog op een beslissing; een statushouder heeft officieel een verblijfsvergunning gekregen'
                ],
                'antwoord': 3,
                'uitleg': 'Een statushouder is een asielzoeker wiens vluchtelingenstatus officieel is erkend.'
            },
            # 2 Waaronwaar (1 false, 1 true)
            {
                'type': 'waaronwaar',
                'vraag': 'Iemand die zelf in Marokko is geboren en op 20-jarige leeftijd naar Nederland verhuisde, behoort tot de tweede generatie migranten.',
                'antwoord': False,
                'uitleg': 'Onwaar. Wie zelf in het buitenland is geboren behoort tot de eerste generatie.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Mensen uit Curaçao en Aruba hebben het Nederlandse paspoort omdat deze eilanden deel uitmaken van het Koninkrijk der Nederlanden.',
                'antwoord': True,
                'uitleg': 'Waar. Als rijksgenoten bezitten zij de Nederlandse nationaliteit.'
            },
            # 2 Invul
            {
                'type': 'invul',
                'vraag': 'Vul het jaartal in: Suriname werd een onafhankelijke republiek in het jaar ...',
                'antwoord': '1975',
                'uitleg': 'Suriname werd op 25 november 1975 onafhankelijk.'
            },
            {
                'type': 'invul',
                'vraag': 'Vul de term in: Iemand die in Nederland is geboren maar van wie ten minste één ouder in het buitenland is geboren, behoort tot de ... generatie.',
                'antwoord': 'tweede|2e|tweede generatie',
                'uitleg': 'Dit is de officiële definitie van de tweede generatie migrant.'
            },
            # 4 MC (0: 1, 1: 1, 2: 1, 3: 1)
            {
                'type': 'mc',
                'vraag': 'Wat was een belangrijk kenmerk van het Nederlandse integratiebeleid vóór de jaren 1990?',
                'opties': [
                    'Men ging ervan uit dat gastarbeiders tijdelijk waren en uiteindelijk zouden terugkeren naar hun vaderland',
                    'Iedere nieuwkomer moest verplicht direct van naam veranderen',
                    'Nieuwkomers kregen direct stemrecht voor de Tweede Kamer',
                    'Er werd streng gecontroleerd op beheersing van de Nederlandse taal'
                ],
                'antwoord': 0,
                'uitleg': 'Tot in de jaren 80 dacht men dat de arbeiders tijdelijk in Nederland verbleven (het gastarbeidersconcept).'
            },
            {
                'type': 'mc',
                'vraag': 'Welke sector in Nederland leunt tegenwoordig zwaar op Europese arbeidsmigranten uit landen als Polen en Roemenië?',
                'opties': [
                    'Het bankwezen en de effectenbeurs',
                    'De glastuinbouw in het Westland, distributiecentra en vleesverwerking',
                    'Het basisonderwijs',
                    'De bemanning van defensieonderzeeboten'
                ],
                'antwoord': 1,
                'uitleg': 'In kassen, distributiecentra en vleesverwerking werken veel arbeidsmigranten uit Midden- en Oost-Europa.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een <b>expatriate</b> (expat)?',
                'opties': [
                    'Iemand die zijn nationaliteit is kwijtgeraakt door een misdrijf',
                    'Een asielzoeker die illegaal in een bos verblijft',
                    'Een hoogopgeleide buitenlandse werknemer die tijdelijk in een land woont voor zijn internationale carrière',
                    'Een student die spijbelt van school'
                ],
                'antwoord': 2,
                'uitleg': 'Expats zijn veelal hoogopgeleide werknemers die tijdelijk voor internationale bedrijven worden uitgezonden.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom heeft Nederland een <b>inburgeringsexamen</b> ingevoerd voor nieuwkomers van buiten de EU?',
                'opties': [
                    'Om ervoor te zorgen dat niemand meer naar Nederland mag reizen',
                    'Om extra belastinggeld op te halen voor de schatkist',
                    'Om de geschiedenis van alle Europese koningshuizen uit het hoofd te leren',
                    'Om te bevorderen dat nieuwkomers de taal leren, de waarden en wetten kennen en sneller meedoen op de arbeidsmarkt'
                ],
                'antwoord': 3,
                'uitleg': 'Inburgering bevordert zelfredzaamheid en integratie in de Nederlandse samenleving.'
            },
            # 2 Open
            {
                'type': 'open',
                'vraag': 'Hoe werd een buitenlandse werknemer genoemd die in de jaren 1960 door overheid en bedrijven werd aangetrokken voor tijdelijk werk?',
                'sleutelwoorden': ['gastarbeider/gastarbeiders'],
                'minTreffers': 1,
                'modelantwoord': 'Deze werknemers werden gastarbeiders genoemd.',
                'uitleg': 'Zij werden destijds gastarbeiders genoemd.'
            },
            {
                'type': 'open',
                'vraag': 'Noem de generatie waartoe iemand behoort die zelf in het buitenland geboren is en later naar Nederland verhuisde.',
                'sleutelwoorden': ['eerste generatie/eerste/1e'],
                'minTreffers': 1,
                'modelantwoord': 'Dit is de eerste generatie migrant.',
                'uitleg': 'Zelf in het buitenland geboren = eerste generatie.'
            }
        ]
    }
]

for ex in EXAMS:
    path = os.path.join(BASE_DIR, ex['file'])
    content = f"""/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — {ex['titel']}
   buiteNLand 3 HAVO Hoofdstuk 3 (Migratie)
   ========================================================= */
DURU.registerExamen({{
  id: "{ex['id']}",
  hoofdstuk: {ex['hoofdstuk']},
  paragraaf: "{ex['paragraaf']}",
  hoofdstukTitel: "{ex['hoofdstukTitel']}",
  titel: "{ex['titel']}",
  vak: "{ex['vak']}",
  icoon: "{ex['icoon']}",
  duurMin: {ex['duurMin']},
  vragen: {json.dumps(ex['vragen'], indent=4, ensure_ascii=False)}
}});
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {path}")

print("Exams done!")
