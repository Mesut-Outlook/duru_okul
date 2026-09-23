"""
Script om Aardrijkskunde Hoofdstuk 4 Proeftoetsen (examen_16.js t/m examen_20.js) te genereren.
Elke toets:
- 20 vragen precies (12 mc, 4 waaronwaar, 2 invul, 2 open)
- mc antwoorden: precies 3x 0 (A), 3x 1 (B), 3x 2 (C), 3x 3 (D) (25% elk)
- waaronwaar: precies 2x True, 2x False (50% onwaar)
- Geen 'invoer'
- Vragen uniek t.o.v. onderwerpen en eerdere examens
"""
import os
import json

BASE_DIR = 'havo3/aardrijkskunde/js/data'

EXAMENS = [
    {
        'file': 'examen_16.js',
        'id': 'ex-h3-ak-16',
        'hoofdstuk': 4,
        'paragraaf': '4.1',
        'titel': 'Proeftoets 16 — §4.1 De aarde warmt op!',
        'icoon': '🌡️',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat gebeurt er met het volume van zeewater wanneer de temperatuur van de oceanen stijgt?',
                'opties': [
                    'Het zeewater zet uit waardoor het meer ruimte inneemt (thermische expansie)',
                    'Het zeewater krimpt juist in elkaar waardoor het dieper zakt',
                    'Het volume blijft exact gelijk omdat water niet kan uitzetten',
                    'Het zeewater verdampt onmiddellijk volledig naar de ruimte'
                ],
                'antwoord': 0,
                'uitleg': 'Wanneer water opwarmt, zetten de moleculen uit; dit proces verklaart een groot deel van de zeespiegelstijging.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Welke van de volgende gassen is GEEN broeikasgas in onze atmosfeer?',
                'opties': [
                    'Koolstofdioxide (CO2)',
                    'Zuurstofgas (O2)',
                    'Methaan (CH4)',
                    'Distikstofmonoxide (lachgas, N2O)'
                ],
                'antwoord': 1,
                'uitleg': 'Zuurstof (O2) vormt ongeveer 21% van de lucht en absorbeert geen infraroodstraling (geen broeikasgas).'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Op welke manier beïnvloedt de opwarming van de aarde de frequentie van extreme bosbranden?',
                'opties': [
                    'Het risico neemt af omdat warmere lucht altijd voor mist zorgt',
                    'Er is geen enkel verband tussen temperatuur en vegetatiebranden',
                    'Hogere temperaturen en langere droogteperiodes drogen bossen en bodems sneller uit',
                    'Bosbranden ontstaan alleen nog maar in de winter'
                ],
                'antwoord': 2,
                'uitleg': 'Door aanhoudende hitte en verdamping wordt de vegetatie kurkdroog, waardoor natuurbranden veel sneller ontbranden en uitbreiden.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat is een groot verschil tussen het smelten van landijs (zoals op Groenland) en zee-ijs (op de Noordpool)?',
                'opties': [
                    'Zee-ijs bestaat uit zoetwater en landijs altijd uit zoutwater',
                    'Landijs smelt alleen in de winter en zee-ijs alleen in de herfst',
                    'Smeltend zee-ijs zorgt voor vulkaanuitbarstingen terwijl landijs dat niet doet',
                    'Smeltend landijs voegt nieuw water toe aan de oceaan, terwijl drijvend zee-ijs zijn eigen gewicht al verplaatst'
                ],
                'antwoord': 3,
                'uitleg': 'Drijvend ijs verplaatst al water volgens de wet van Archimedes; afsmeltend landijs verhoogt het totale volume van de oceanen.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is een direct ecologisch gevolg van het afsmelten van bergkappen en gletsjers in Azië?',
                'opties': [
                    'Grote rivieren (zoals de Indus en Ganges) krijgen eerst tijdelijk veel smeltwater, maar drogen op termijn in droge seizoenen deels op',
                    'De Himalaya verandert in een tropisch regenwoud',
                    'Er ontstaan geen lawines meer in de bergen',
                    'Alle omringende landen veranderen spontaan in moeras'
                ],
                'antwoord': 0,
                'uitleg': 'Gletsjers fungeren als natuurlijke waterreservoirs die water bufferen voor droge seizoenen; als ze verdwijnen ontstaat waterschaarste.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat betekent het begrip thermische expansie in relatie tot de opwarming van de aarde?',
                'opties': [
                    'Het smelten van gletsjerijs in de Alpen',
                    'Het uitzetten van warmer oceaanwater waardoor het zeeniveau stijgt',
                    'Het bevriezen van waterdruppels in hoge wolken',
                    'Het uitzetten van rotsen door dagelijkse zonnewarmte'
                ],
                'antwoord': 1,
                'uitleg': 'Thermische expansie betekent letterlijk warmte-uitzetting: water neemt bij hogere temperaturen meer volume in.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'In welke sector van de wereldeconomie ontstaat de grootste uitstoot van lachgas (N2O)?',
                'opties': [
                    'In de staalproductie en scheepsbouw',
                    'In het personenvervoer per auto',
                    'In de landbouw door overmatig gebruik van stikstofkunstmest',
                    'In de luchtvaart door kerosineverbranding'
                ],
                'antwoord': 2,
                'uitleg': 'Bodemmicroben zetten stikstofverbindingen uit kunstmest om in distikstofmonoxide (lachgas).'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom noemt men het effect van broeikasgassen in de atmosfeer een klimaatmachine?',
                'opties': [
                    'Omdat de atmosfeer door een computer wordt bestuurd',
                    'Omdat de mens met grote turbines de wind kan regelen',
                    'Omdat er turbines in de dampkring zijn geplaatst',
                    'Omdat een verandering in de dampkringopbouw een kettingreactie van wind-, oceaan- en weersveranderingen teweegbrengt'
                ],
                'antwoord': 3,
                'uitleg': 'Het klimaatsysteem is een complex samenspel waarin warmte, luchtstromen en zeestromingen nauw met elkaar zijn verbonden.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Welke tropische eilandenstaten worden als eerste bedreigd met volledige overstroming door de zeespiegelstijging?',
                'opties': [
                    'Lage koraalatollen in de Stille Oceaan zoals Tuvalu en Kiribati',
                    'Hooggelegen vulkaaneilanden zoals Hawaï',
                    'Grote continentale eilanden zoals Madagaskar',
                    'Bergachtige eilanden zoals IJsland'
                ],
                'antwoord': 0,
                'uitleg': 'Laaggelegen atollen steken vaak slechts één tot twee meter boven de zeespiegel uit en lopen groot gevaar.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste verschil tussen het weer en het klimaat?',
                'opties': [
                    'Het weer geldt wereldwijd en het klimaat alleen voor één straat',
                    'Het weer is de toestand van de dampkring op een bepaald moment; het klimaat is de gemiddelde weersgesteldheid over dertig jaar',
                    'Het weer verandert nooit en het klimaat verandert ieder uur',
                    'Het weer wordt gemeten door satellieten en het klimaat met een regenmeter'
                ],
                'antwoord': 1,
                'uitleg': 'Weer is actueel en lokaal; klimaat is het langjarig gemiddelde (standaardperiode van 30 jaar).'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn dichtbevolkte rivierdelta s in ontwikkelingslanden (zoals Bangladesh) extra kwetsbaar voor klimaatverandering?',
                'opties': [
                    'Omdat er in delta s nooit regen valt',
                    'Omdat delta s op grote hoogte in de bergen liggen',
                    'Omdat ze vlak bij zeeniveau liggen en tegelijk te maken krijgen met piekafvoeren van rivieren en tropische stormvloeden',
                    'Omdat er geen dijken of dammen gebouwd mogen worden van de wet'
                ],
                'antwoord': 2,
                'uitleg': 'Laaggelegen delta s vangen zowel rivieroverstromingen als opstuwende stormvloeden vanuit zee op.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welke menselijke activiteit draagt bij aan het versterkte broeikaseffect doordat er minder CO2 uit de lucht wordt opgenomen?',
                'opties': [
                    'Het aanplanten van nieuwe bossen',
                    'Het bouwen van windmolens',
                    'Het composteren van groenteafval',
                    'Grootschalige ontbossing van tropische regenwouden'
                ],
                'antwoord': 3,
                'uitleg': 'Bomen slaan tijdens fotosynthese koolstof op; bij ontbossing verdwijnt deze opslag en komt CO2 vrij bij verbranding of rotting.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'Koolstofdioxide (CO2) blijft na uitstoot honderden jaren actief aanwezig in de atmosfeer.',
                'antwoord': True,
                'uitleg': 'Waar: CO2 breekt niet snel af en blijft eeuwenlang in de koolstofkringloop van dampkring en oceanen circuleren.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'Wetenschappers hebben vastgesteld dat de aarde de afgelopen honderd jaar juist kouder is geworden.',
                'antwoord': False,
                'uitleg': 'Onwaar: de wereldwijde meetreeksen tonen onmiskenbaar aan dat de gemiddelde temperatuur wereldwijd sterk is gestegen.'
            },
            # WOW 3: True
            {
                'type': 'waaronwaar',
                'vraag': 'In de zomer van 2022 bereikten grote Europese rivieren zoals de Rijn historisch lage waterstanden door aanhoudende droogte.',
                'antwoord': True,
                'uitleg': 'Waar: door extreme droogte en hitte daalde het waterpeil in de Rijn zo ver dat de binnenvaart zwaar werd belemmerd.'
            },
            # WOW 4: False
            {
                'type': 'waaronwaar',
                'vraag': 'Het smelten van gletsjers heeft uitsluitend voordelen omdat er overal op aarde meer drinkwater ontstaat.',
                'antwoord': False,
                'uitleg': 'Onwaar: na een tijdelijke toename van smeltwater vallen rivieren in droge seizoenen juist droog, wat tot ernstige watercrises leidt.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'Het verschijnsel waarbij warm zeewater uitzet en daardoor meer ruimte inneemt, heet thermische ....',
                'antwoord': 'expansie',
                'uitleg': 'Thermische expansie (warmte-uitzetting) is een van de hoofdoorzaken van de wereldwijde zeespiegelstijging.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'Mensen die moeten vluchten omdat hun woongebied onleefbaar wordt door klimaatverandering, noemen we ....',
                'antwoord': 'klimaatmigranten',
                'uitleg': 'Klimaatmigranten verlaten hun land of streek door ecologische veranderingen zoals droogte of zeespiegelstijging.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem het gas dat bij de verbranding van fossiele brandstoffen het meest wordt uitgestoten en de grootste bijdrage levert aan de opwarming van de aarde.',
                'sleutelwoorden': [
                    'koolstofdioxide/CO2/koolzuurgas'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Koolstofdioxide (CO2) is het belangrijkste broeikasgas dat vrijkomt bij de verbranding van fossiele brandstoffen.',
                'uitleg': 'Koolstofdioxide (CO2) ontstaat bij verbranding van kolen, olie en gas.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Leg uit waarom het natuurlijke effect van broeikasgassen in de atmosfeer noodzakelijk is voor het leven op aarde.',
                'sleutelwoorden': [
                    'koud/koude/temperatuur/warmte/leefbaar'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Zonder het natuurlijke broeikaseffect zou de aarde veel te koud zijn (circa -18 graden) waardoor er geen leven mogelijk zou zijn.',
                'uitleg': 'Het natuurlijke broeikaseffect houdt voldoende warmte vast om een leefbare gemiddelde temperatuur van 15 graden te garanderen.'
            }
        ]
    },
    {
        'file': 'examen_17.js',
        'id': 'ex-h3-ak-17',
        'hoofdstuk': 4,
        'paragraaf': '4.2',
        'titel': 'Proeftoets 17 — §4.2 Op weg naar duurzame energiebronnen',
        'icoon': '🛢️',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Waarom worden steenkool, aardolie en aardgas uitputbare energiebronnen genoemd?',
                'opties': [
                    'Omdat de natuur miljoenen jaren nodig heeft om ze te vormen en de voorraad op aarde eindig is',
                    'Omdat ze alleen onder invloed van zonlicht branden',
                    'Omdat ze na verbranding spontaan weer terugkeren in de aarde',
                    'Omdat ze overal ter wereld gratis uit de lucht gehaald kunnen worden'
                ],
                'antwoord': 0,
                'uitleg': 'Fossiele brandstoffen ontstaan over geologische tijdperken van miljoenen jaren; de mens verbruikt ze vele malen sneller.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste kenmerk van niet-conventionele olie en gas?',
                'opties': [
                    'Het bevindt zich altijd in grote open ondergrondse grotten',
                    'Het zit vast in compact moedergesteente of teerzand en vraagt complexe en dure winningstechnieken',
                    'Het stoot geen enkele vorm van warmte of gas uit',
                    'Het wordt uitsluitend gewonnen in tropische regenwouden'
                ],
                'antwoord': 1,
                'uitleg': 'Niet-conventionele voorraden (zoals schaliegas of teerzand) vereisen ingrijpende technieken zoals hydraulische stimulatie of teerzandafgraving.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Hoeveel energie gaat er gemiddeld verloren bij de opwekking en het transport van stroom uit fossiele centrales?',
                'opties': [
                    'Vrijwel niets, minder dan 2%',
                    'Ongeveer een tiende (10%)',
                    'Ongeveer twee derde (circa 65%) in de vorm van onbenutte restwarmte',
                    'Honderd procent, er blijft niets over'
                ],
                'antwoord': 2,
                'uitleg': 'Klassieke thermische centrales hebben een relatief laag rendement; het merendeel van de energie verdwijnt als koelwater of schoorsteenwarmte.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat gebeurt er bij de nucleaire reactie in een traditionele kerncentrale?',
                'opties': [
                    'Waterstofatomen worden samengesmolten tot helium',
                    'Steenkool wordt onder hoge druk vloeibaar gemaakt',
                    'Zonlicht wordt rechtstreeks omgezet in gammastralen',
                    'Atoomkernen van zware elementen (zoals uranium) worden gespleten om warmte op te wekken'
                ],
                'antwoord': 3,
                'uitleg': 'Kernenergie ontstaat door kernsplijting van uraniumatomen in een gecontroleerde kettingreactie.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is de voornaamste reden dat teerzandwinning in Canada zo zwaar bekritiseerd wordt door milieuorganisaties?',
                'opties': [
                    'Het vergt grootschalige ontbossing, enorme hoeveelheden heet water en energie en veroorzaakt giftige afvalmeren',
                    'Het trekt te veel toeristen naar de Canadese natuurparken',
                    'Het leidt tot extreme koudegolven in de regio',
                    'Er wordt bij teerzandwinning helemaal geen olie geproduceerd'
                ],
                'antwoord': 0,
                'uitleg': 'De winning van bitumen uit teerzand vernietigt boreale bossen en laat zwaar vervuilde bekkens achter.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Welke zware kernramp in 2011 deed veel landen twijfelen aan de veiligheid van kernenergie?',
                'opties': [
                    'De ramp bij Tsjernobyl in Oekraïne',
                    'De ramp bij Fukushima in Japan',
                    'De explosie bij Three Mile Island in de VS',
                    'De brand in Sellafield in het Verenigd Koninkrijk'
                ],
                'antwoord': 1,
                'uitleg': 'In maart 2011 veroorzaakte een zeebeving en tsunami een driedubbele meltdown in de kerncentrale van Fukushima Daiichi.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat is de CO2-voetafdruk per inwoner?',
                'opties': [
                    'De schoenmaat van een gemiddelde inwoner van een land',
                    'Het aantal bomen dat een burger jaarlijks plant',
                    'De totale hoeveelheid broeikasgassen die direct en indirect wordt uitgestoten voor de levensstijl en consumptie van één inwoner',
                    'Het gewicht van het huishoudelijk afval per maand'
                ],
                'antwoord': 2,
                'uitleg': 'De CO2-voetafdruk meet de totale uitstoot die nodig is voor wonen, vervoer, voeding en spullen van een individu.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom noemen we aardgas vaak de minst vervuilende van de traditionele fossiele brandstoffen?',
                'opties': [
                    'Omdat gas gratis uit de dampkring gewonnen kan worden',
                    'Omdat gas helemaal geen koolstofatomen bevat',
                    'Omdat aardgas bij verbranding waterstofatomen aanmaakt',
                    'Omdat aardgas per opgewekte hoeveelheid energie aanzienlijk minder CO2 en fijnstof uitstoot dan steenkool of olie'
                ],
                'antwoord': 3,
                'uitleg': 'Aardgas heeft een gunstigere verhouding tussen koolstof en waterstof en stoot tot 50% minder CO2 uit dan kolen.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is een groot voordeel van kerncentrales voor de betrouwbaarheid van het energienet?',
                'opties': [
                    'Ze leveren continu en stabiel basislastvermogen, onafhankelijk van dag, nacht of weersomstandigheden',
                    'Ze kunnen binnen tien seconden aan- en uitgezet worden',
                    'Ze kunnen op de zolder van gewone huizen geïnstalleerd worden',
                    'Ze functioneren volledig zonder water'
                ],
                'antwoord': 0,
                'uitleg': 'Kerncentrales draaien dag en nacht op vol vermogen en zijn niet afhankelijk van de grillen van het weer.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is een belangrijk geopolitiek argument voor Europese landen om over te stappen op hernieuwbare energie?',
                'opties': [
                    'Om alle fabrieken te verplaatsen naar Azië',
                    'Om minder afhankelijk te zijn van autoritaire en instabiele regimes die olie en gas exporteren',
                    'Om de invoer van elektriciteit uit buurlanden volledig te verbieden',
                    'Om de benzineprijzen te kunnen verdriedubbelen'
                ],
                'antwoord': 1,
                'uitleg': 'Eigen opwekking van zon en wind versterkt de strategische autonomie en energieveiligheid van Europa.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste probleem bij de eindopslag van radioactief afval uit kerncentrales?',
                'opties': [
                    'Het afval verdampt binnen een dag naar de lucht',
                    'Het afval is te zwaar om met vrachtwagens te vervoeren',
                    'Het afval blijft tienduizenden jaren gevaarlijk radioactief en vereist uiterst veilige geologische diepteberging',
                    'Het afval kan alleen bewaard worden in vloeibare stikstof'
                ],
                'antwoord': 2,
                'uitleg': 'De extreem lange halveringstijd van bepaalde splijtingsproducten maakt langdurige veilige opslag een technisch en maatschappelijk vraagstuk.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welke energiebron heeft de hoogste energiedichtheid (meeste energie per kilogram brandstof)?',
                'opties': [
                    'Droog brandhout',
                    'Bruinkool',
                    'Aardolie',
                    'Uranium (nucleaire brandstof)'
                ],
                'antwoord': 3,
                'uitleg': 'Uranium heeft een ongekend hoge energiedichtheid; 1 kg uranium levert miljoenen malen meer energie dan 1 kg kolen.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'Bij de normale werking van een kerncentrale komt tijdens de elektriciteitsproductie geen koolstofdioxide vrij.',
                'antwoord': True,
                'uitleg': 'Waar: kernsplijting is een nucleair proces waarbij geen fossiele koolstof wordt verbrand.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'Conventionele olie is veel moeilijker en duurder om te winnen dan olie uit teerzanden.',
                'antwoord': False,
                'uitleg': 'Onwaar: conventionele olie stroomt relatief gemakkelijk omhoog uit poreus reservoirgesteente, terwijl teerzandwinning extreem bewerkelijk is.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'De voorraad fossiele brandstoffen in de aardkorst is oneindig groot en vult zich elk jaar vanzelf aan.',
                'antwoord': False,
                'uitleg': 'Onwaar: fossiele brandstoffen zijn uitputbaar omdat de vorming miljoenen jaren duurt.'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'In de Canadese provincie Alberta wordt olie gewonnen uit uitgestrekte afzettingen van klei en zand gemengd met bitumen.',
                'antwoord': True,
                'uitleg': 'Waar: Alberta staat bekend om de enorme open mijnen en in-situ projecten voor teerzandwinning.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'Olie- en gasvoorraden die gemakkelijk via een traditionele boorput uit reservoirgesteente omhoog gepompt kunnen worden, noemen we .... olie en gas.',
                'antwoord': 'conventionele',
                'uitleg': 'Conventionele winning betreft makkelijk bereikbare reserves in doorlatend gesteente.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'De structurele overstap van fossiele brandstoffen naar schone, hernieuwbare energiebronnen heet de ....',
                'antwoord': 'energietransitie',
                'uitleg': 'De energietransitie is de gecoördineerde overgang naar een CO2-neutrale energievoorziening.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem het radioactieve chemische element dat in kerncentrales als splijtstof wordt benut.',
                'sleutelwoorden': [
                    'uranium'
                ],
                'minTreffers': 1,
                'modelantwoord': 'In kerncentrales wordt uranium gebruikt als splijtstof.',
                'uitleg': 'Uranium is het zware metaal waarvan de isotopen (zoals U-235) worden gespleten.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Noem een belangrijk nadeel van het gebruik van kernenergie voor toekomstige generaties.',
                'sleutelwoorden': [
                    'afval/radioactief/straling/kernafval'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Het hoogradioactieve afval blijft tienduizenden jaren gevaarlijk en moet veilig worden opgeslagen.',
                'uitleg': 'Radioactief afval vormt een langdurig risico voor de volksgezondheid en het milieu.'
            }
        ]
    },
    {
        'file': 'examen_18.js',
        'id': 'ex-h3-ak-18',
        'hoofdstuk': 4,
        'paragraaf': '4.3',
        'titel': 'Proeftoets 18 — §4.3 Het tegengaan van klimaatverandering',
        'icoon': '☀️',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is het werkingsprincipe van geothermische energie (aardwarmte)?',
                'opties': [
                    'Heet grondwater of stoom uit diepe aardlagen oppompen om warmte of elektriciteit op te wekken',
                    'Het verbranden van gedroogde lava in hoogovens',
                    'Koude zeelucht door ondergrondse tunnels blazen',
                    'Zonlicht concentreren op een diepe schacht in de grond'
                ],
                'antwoord': 0,
                'uitleg': 'Geothermie maakt gebruik van de warmte die van nature in het binnenste van de aarde aanwezig is.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Waarom wordt biomassa gerekend tot hernieuwbare energiebronnen?',
                'opties': [
                    'Omdat biomassa helemaal geen rook of as achterlaat',
                    'Omdat de verbrande planten en bomen opnieuw kunnen groeien en tijdens hun groei CO2 hebben opgenomen (korte koolstofkringloop)',
                    'Omdat biomassa uitsluitend uit gerecycled plastic bestaat',
                    'Omdat biomassa alleen in de ruimte kan ontstaan'
                ],
                'antwoord': 1,
                'uitleg': 'Biomassa maakt deel uit van de actuele koolstofkringloop; opnieuw groeiende bomen leggen de vrijgekomen koolstof weer vast.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat is een belangrijk doel van het klimaatschadefonds dat op recente klimaattoppen werd opgericht?',
                'opties': [
                    'Het financieren van ruimtereizen voor wetenschappers',
                    'Het vergoeden van autoschade na een hagelbui in rijke landen',
                    'Financiële hulp bieden aan kwetsbare ontwikkelingslanden die getroffen worden door onherstelbare klimaatschade',
                    'Het subsidiëren van olieboringen in ontwikkelingslanden'
                ],
                'antwoord': 2,
                'uitleg': 'Het Loss and Damage-fonds compenseert arme landen die zelf amper uitstoot veroorzaakten maar wel zware schade lijden.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welke van de volgende energiebronnen is afhankelijk van de zwaartekracht van de maan en de zon?',
                'opties': [
                    'Geothermische energie',
                    'Zonne-energie',
                    'Windenergie',
                    'Getijdenenergie (eb en vloed)'
                ],
                'antwoord': 3,
                'uitleg': 'Getijdenenergie benut de waterbeweging van eb en vloed, veroorzaakt door de gravitatiekracht van maan en zon.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste verschil tussen zonnepanelen (PV) en zonnecollectoren?',
                'opties': [
                    'Zonnepanelen wekken elektriciteit op uit licht; zonnecollectoren warmen water op met zonnewarmte',
                    'Zonnepanelen werken alleen op de maan; zonnecollectoren werken op aarde',
                    'Zonnepanelen zijn altijd rond; zonnecollectoren zijn altijd driehoekig',
                    'Zonnecollectoren wekken kernenergie op en zonnepanelen niet'
                ],
                'antwoord': 0,
                'uitleg': 'Fotovoltaïsche cellen (PV) genereren stroom; zonneboilers en collectoren leveren warm tapwater of verwarming.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn stuwmeren voor waterkrachtcentrales niet overal zomaar aan te leggen?',
                'opties': [
                    'Omdat turbines alleen in zoutwater kunnen draaien',
                    'Omdat je aanzienlijke hoogteverschillen (reliëf) en veel wateraanvoer nodig hebt om voldoende waterdruk op te bouwen',
                    'Omdat waterkracht verboden is door de Verenigde Naties',
                    'Omdat rivieren altijd vanzelf bergopwaarts stromen'
                ],
                'antwoord': 1,
                'uitleg': 'Waterkracht vereist verval (hoogteverschil) en een flink debiet, waardoor vlakke laaglanden zoals Nederland minder geschikt zijn.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke zeldzame grondstof is onmisbaar voor de fabricage van moderne accu s in elektrische auto s?',
                'opties': [
                    'Steenkool',
                    'Kalksteen',
                    'Lithium',
                    'Asbest'
                ],
                'antwoord': 2,
                'uitleg': 'Lithium is een essentieel licht metaal voor lithium-ion-accu s in consumentenelektronica en elektrische voertuigen.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom blijft de uitstoot van de internationale luchtvaart een lastig punt in klimaatakkoorden?',
                'opties': [
                    'Omdat vliegtuigen geen enkele uitstoot veroorzaken',
                    'Omdat alle vliegtuigen al op zonne-energie vliegen',
                    'Omdat piloten weigeren mee te doen aan klimaatmetingen',
                    'Omdat internationale vluchten tussen landen vliegen waardoor geen enkel land zich individueel verantwoordelijk voelt voor die uitstoot'
                ],
                'antwoord': 3,
                'uitleg': 'Internationale vlieg- en scheepvaartroutes vallen buiten de landelijke doelstellingen van nationale overheden.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'In welk land dekt geothermische energie (aardwarmte) een zeer groot deel van de nationale warmte- en elektriciteitsbehoefte?',
                'opties': [
                    'IJsland',
                    'Nederland',
                    'Egypte',
                    'Polen'
                ],
                'antwoord': 0,
                'uitleg': 'Door zijn ligging op de Mid-Atlantische Rug beschikt IJsland over enorme hoeveelheden vulkanische hitte vlak onder het oppervlak.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is een belangrijk ecologisch bezwaar tegen de aanleg van grote stuwdammen in rivieren?',
                'opties': [
                    'De rivier verdwijnt onmiddellijk in de aarde',
                    'Stuwmeren overstromen stroomopwaarts grote natuurgebieden en blokkeren de trek van trekvissen zoals zalm',
                    'De stoom uit de centrale vergiftigt alle vogels',
                    'Stuwmeren zorgen ervoor dat het nooit meer regent'
                ],
                'antwoord': 1,
                'uitleg': 'Dammen onderbreken het rivierecosysteem, verhinderen vistrek en houden vruchtbaar rivierslib stroomopwaarts tegen.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste kenmerk van hernieuwbare energiebronnen ten opzichte van fossiele bronnen?',
                'opties': [
                    'Ze zijn altijd goedkoper dan welke brandstof ook',
                    'Ze kunnen alleen binnen in fabrieken worden gemaakt',
                    'Ze raken bij gebruik nooit op omdat natuurlijke processen ze voortdurend aanvullen',
                    'Ze zijn allemaal uitgevonden in de eenentwintigste eeuw'
                ],
                'antwoord': 2,
                'uitleg': 'Hernieuwbare bronnen benutten onuitputtelijke natuurlijke stromen zoals zon, wind en water.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn windturbines op zee (offshore) veel hoger en krachtiger dan op het land?',
                'opties': [
                    'Omdat de zeebodem van beton is gemaakt',
                    'Omdat er op zee minder waterdamp aanwezig is',
                    'Omdat zeevogels de wieken sneller doen draaien',
                    'Omdat er op open zee geen hinder is van bomen en gebouwen en er reusachtige turbines geplaatst kunnen worden'
                ],
                'antwoord': 3,
                'uitleg': 'Op zee is meer ruimte voor gigantische rotordiameters en waait het veel harder en regelmatiger.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'Het Akkoord van Parijs werd in 2015 ondertekend door bijna alle landen ter wereld.',
                'antwoord': True,
                'uitleg': 'Waar: bijna 200 landen sloten zich aan bij dit bindende internationale klimaatakkoord.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'Windenergie veroorzaakt tijdens de elektriciteitsopwekking door de wieken grote hoeveelheden giftige rookgassen.',
                'antwoord': False,
                'uitleg': 'Onwaar: windturbines wekken stroom op zonder verbranding en stoten tijdens de werking geen uitlaatgassen uit.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'In het klimaatakkoord is vastgelegd dat arme ontwikkelingslanden per direct evenveel geld moeten bijdragen aan het klimaatschadefonds als rijke westerse landen.',
                'antwoord': False,
                'uitleg': 'Onwaar: juist de rijke westerse landen zijn verplicht het fonds te vullen ter compensatie van de kwetsbare landen.'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'IJsland verwarmt bijna al zijn woningen met geothermische energie uit vulkanische bronnen.',
                'antwoord': True,
                'uitleg': 'Waar: geothermie voorziet in vrijwel de volledige behoefte aan stadsverwarming op IJsland.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'Energie die wordt opgewekt door gebruik te maken van de hitte diep in de aardkorst, noemen we .... energie.',
                'antwoord': 'geothermische',
                'uitleg': 'Geothermische energie (of aardwarmte) benut de natuurlijke warmte uit de ondergrond.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'Het internationale verdrag uit 2015 waarin afspraken zijn gemaakt om de opwarming ruim onder de 2 graden te houden, heet het Klimaatakkoord van ....',
                'antwoord': 'Parijs',
                'uitleg': 'Het Akkoord van Parijs vormt de hoeksteen van het wereldwijde klimaatbeleid.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem een voorbeeld van een biologische reststof die kan worden benut als biomassa voor energieopwekking.',
                'sleutelwoorden': [
                    'hout/houtsnippers/mest/gft/frituurvet/plantenresten'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Houtsnippers, mest of gft-afval zijn veelgebruikte grondstoffen voor biomassa.',
                'uitleg': 'Biomassa benut organisch afvalmateriaal om warmte of biobrandstoffen te produceren.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Leg uit waarom rijke westerse landen volgens het principe van klimaatrechtvaardigheid een grotere financiële bijdrage moeten leveren aan klimaatmaatregelen.',
                'sleutelwoorden': [
                    'historisch/verleden/meeste/uitstoot/geld/vervuiler'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Rijke landen hebben historisch gezien sinds de industriële revolutie de meeste CO2 uitgestoten en beschikken over meer financiële middelen.',
                'uitleg': 'De historische vervuilers dragen de morele en financiële verantwoordelijkheid voor de aangerichte schade.'
            }
        ]
    },
    {
        'file': 'examen_19.js',
        'id': 'ex-h3-ak-19',
        'hoofdstuk': 4,
        'paragraaf': '4.4',
        'titel': 'Proeftoets 19 — §4.4 Klimaatverandering in Europa',
        'icoon': '🇪🇺',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste doel van het Europese beleidsprogramma de Green Deal?',
                'opties': [
                    'Van de Europese Unie in 2050 het eerste klimaatneutrale continent ter wereld maken',
                    'Alle bossen in Europa kappen voor landbouwgronden',
                    'Het stimuleren van het gebruik van steenkool in Midden-Europa',
                    'Het opheffen van alle milieuregels voor grote industrieën'
                ],
                'antwoord': 0,
                'uitleg': 'De Green Deal stelt als wettelijk doel dat de EU in 2050 netto nul broeikasgassen uitstoot.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn wintersportdorpen in de lagere delen van de Alpen steeds kwetsbaarder geworden?',
                'opties': [
                    'Omdat skiliften verboden zijn door de Europese Unie',
                    'Omdat de sneeuwzekere periode korter wordt en de sneeuwgrens door stijgende temperaturen omhoog schuift',
                    'Omdat bergen ieder jaar tien meter lager worden',
                    'Omdat er geen toeristen meer naar de bergen willen reizen'
                ],
                'antwoord': 1,
                'uitleg': 'Lager gelegen skigebieden (onder de 1500 meter) hebben steeds meer te maken met regen en te weinig natuursneeuw.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men in de fysische geografie onder waterstress?',
                'opties': [
                    'Wanneer vissen in een meer te snel zwemmen',
                    'Wanneer dijken te veel water moeten tegenhouden',
                    'Een situatie waarin de vraag naar schoon zoetwater groter is dan het beschikbare aanbod',
                    'Wanneer drinkwater te veel mineralen bevat'
                ],
                'antwoord': 2,
                'uitleg': 'Waterstress ontstaat bij langdurige droogte wanneer landbouw, industrie en bevolking met watertekorten kampen.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welk risico brengt het ontdooien van de permafrost in het Hoge Noorden met zich mee voor het wereldwijde klimaat?',
                'opties': [
                    'Er ontstaan enorme gletsjers in de toendra',
                    'De aarde stopt met draaien',
                    'Het zeewater wordt overal ter wereld zoet',
                    'Grote hoeveelheden opgeslagen methaan en koolstofdioxide komen vrij in de atmosfeer, wat de opwarming verder versnelt'
                ],
                'antwoord': 3,
                'uitleg': 'In bevroren veen- en toendrabodems zit eeuwenoud organisch materiaal dat bij ontdooiing massaal methaan produceert (positieve terugkoppeling).'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is het verschil tussen klimaatmitigatie en klimaatadaptatie?',
                'opties': [
                    'Mitigatie bestrijdt de oorzaak (uitstoot verminderen); adaptatie past de leefomgeving aan de gevolgen aan',
                    'Mitigatie geldt alleen voor schepen en adaptatie alleen voor treinen',
                    'Mitigatie kost niets en adaptatie kost miljarden',
                    'Mitigatie is verboden in Europa en adaptatie is verplicht'
                ],
                'antwoord': 0,
                'uitleg': 'Mitigatie = voorkomen (uitstoot omlaag); adaptatie = aanpassen (dijken verhogen, steden vergroenen).'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn dichtbebouwde steden in Europa op warme zomerdagen vaak meerdere graden heter dan het platteland (stedelijk hitte-eiland)?',
                'opties': [
                    'Omdat er in steden meer vogels vliegen',
                    'Omdat donkere stenen oppervlakken veel zonnestraling absorberen en er weinig vegetatie is voor verkoelende verdamping',
                    'Omdat de atmosfeer boven een stad dunner is',
                    'Omdat alle huizen in de stad hun verwarming aanzetten'
                ],
                'antwoord': 1,
                'uitleg': 'Weinig groen en veel beton en asfalt houden warmte lang vast en verminderen verdampingskoeling.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke Zuid-Europese landen kregen de afgelopen zomers te maken met gigantische bosbranden en temperaturen boven de 45 graden?',
                'opties': [
                    'Noorwegen en Zweden',
                    'Ierland en Schotland',
                    'Griekenland, Spanje en Portugal',
                    'Denemarken en Finland'
                ],
                'antwoord': 2,
                'uitleg': 'Het Middellandse Zeegebied beleeft steeds vaker extreme zomers met verwoestende natuurbranden.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat is een mogelijk positief gevolg van de opwarming van de aarde voor de landbouw in Noord-Europa (zoals Scandinavië)?',
                'opties': [
                    'Er kunnen nooit meer insectenplagen ontstaan',
                    'Er is geen regenwater meer nodig voor de gewassen',
                    'Alle landbouwgrond verandert in goud',
                    'Het groeiseizoen voor gewassen wordt langer en er kunnen nieuwe gewassoorten verbouwd worden'
                ],
                'antwoord': 3,
                'uitleg': 'Een hogere gemiddelde temperatuur en minder vorstdagen verlengen de teeltperiode in koude noordelijke gebieden.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is een wadi in een klimaatbestendige stad?',
                'opties': [
                    'Een verlaagde groene strook of grasveld waar overtollig regenwater tijdelijk kan infiltreren in de bodem',
                    'Een ondergronds metrostation dat dient als schuilkelder',
                    'Een nieuw type elektrische bus',
                    'Een fontein die uitsluitend drinkwater spuit'
                ],
                'antwoord': 0,
                'uitleg': 'Wadi\'s vangen piekbuien op in de wijk zodat het riool niet overstroomt en het grondwater wordt aangevuld.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Hoeveel sneller warmt het Europese continent sinds de pre-industriële tijd op vergeleken met het wereldwijde gemiddelde?',
                'opties': [
                    'Precies half zo snel',
                    'Bijna twee keer zo snel (ruim 2,1 °C t.o.v. 1,1 °C)',
                    'Tien keer zo snel',
                    'Europa warmt helemaal niet op'
                ],
                'antwoord': 1,
                'uitleg': 'Metingen van onder andere Copernicus tonen aan dat Europa circa twee keer zo snel opwarmt als het wereldgemiddelde.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke gezondheidsbedreiging neemt in Midden- en Zuid-Europa toe als gevolg van zachtere winters en warmere zomers?',
                'opties': [
                    'Bevriezing van ledematen in de zomer',
                    'Een tekort aan zuurstof in de bergen',
                    'De opmars van exotische muggensoorten (zoals de tijgermug) die tropische ziekten kunnen overbrengen',
                    'Een plotselinge afname van allergieën'
                ],
                'antwoord': 2,
                'uitleg': 'Hogere temperaturen stellen invasieve vectoren zoals de tijgermug in staat om te overwinteren en ziektes te verspreiden.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat is het doel van het tussentijdse EU-klimaatdoel Fit for 55 voor het jaar 2030?',
                'opties': [
                    'De gemiddelde levensverwachting verhogen naar 55 jaar',
                    'De Europese bevolking met 55% laten krimpen',
                    '55 nieuwe kerncentrales bouwen in Frankrijk',
                    'De netto-uitstoot van broeikasgassen in de EU met minimaal 55% verminderen ten opzichte van 1990'
                ],
                'antwoord': 3,
                'uitleg': 'Fit for 55 bevat wetgeving om de 55% reductiedoelstelling van 2030 wettelijk en praktisch te borgen.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'In de Mediterrane regio neemt door klimaatverandering het risico op verwoestijning en bodemerosie toe.',
                'antwoord': True,
                'uitleg': 'Waar: door droogte verdwijnt de plantenbedekking waardoor zeldzame zware buien de vruchtbare toplaag wegspoelen.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'In Europa zijn de gevolgen van klimaatverandering in alle regio s precies hetzelfde.',
                'antwoord': False,
                'uitleg': 'Onwaar: er zijn enorme regionale verschillen tussen bijvoorbeeld het hete zuiden, het natte noordwesten en de Alpen.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'Groene daken en stadsparken verhogen de hittestress in binnensteden aanzienlijk.',
                'antwoord': False,
                'uitleg': 'Onwaar: vegetatie koelt de omgeving door schaduw en waterverdamping (evapotranspiratie).'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'Klimaatadaptatie omvat maatregelen zoals dijkversterkingen en het vergroten van waterbergingsgebieden.',
                'antwoord': True,
                'uitleg': 'Waar: adaptatie richt zich op het weerbaar maken van het landschap tegen wateroverlast, droogte en zeespiegelstijging.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'Het fenomeen waarbij de temperatuur in dichtbebouwde steden aanzienlijk hoger is dan op het omringende platteland, heet het stedelijk ....',
                'antwoord': 'hitte-eiland',
                'uitleg': 'Het hitte-eilandeffect ontstaat door steenachtige materialen die hitte vasthouden en gebrek aan groen.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'Het aanpassen van steden en landschappen aan de onvermijdelijke gevolgen van een veranderend klimaat, noemen we klimaat....',
                'antwoord': 'adaptatie',
                'uitleg': 'Adaptatie betekent aanpassing aan de nieuwe klimatologische omstandigheden.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem een maatregel die een gemeente kan nemen om wateroverlast door hevige hoosbuien in een woonwijk te verminderen.',
                'sleutelwoorden': [
                    'wadi/groen/waterberging/ontstenen/regenpijp/vijver/dak'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Het aanleggen van wadi s, groene daken of waterpleinen helpt om overtollig regenwater op te vangen.',
                'uitleg': 'Meer groen en waterberging ontlasten het riool bij hevige stortbuien.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Waarom leidt het verdwijnen van de permafrost in berghellingen tot gevaarlijke puinlawines?',
                'sleutelwoorden': [
                    'ontdooien/smelten/dooi/dooien/smelt'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Het ijs in de ondergrond gaat ontdooien waardoor de losse stenen naar beneden storten.',
                'uitleg': 'Permafrost houdt los gesteente vast; door opwarming smelt dit bindmiddel weg.'
            }
        ]
    },
    {
        'file': 'examen_20.js',
        'id': 'ex-h3-ak-20',
        'hoofdstuk': 4,
        'paragraaf': '4.5',
        'titel': 'Proeftoets 20 — §4.5 Naar minder CO2-uitstoot in Nederland',
        'icoon': '🇳🇱',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste verschil tussen een energiebron en een energiedrager?',
                'opties': [
                    'Een energiebron levert direct primaire energie; een energiedrager slaat energie op die eerst met een andere bron gemaakt moet worden',
                    'Een energiedrager is altijd vloeibaar en een energiebron altijd vast',
                    'Energiedragers zijn gratis en energiebronnen zijn altijd duur',
                    'Energiedragers kunnen alleen in het buitenland gebruikt worden'
                ],
                'antwoord': 0,
                'uitleg': 'Waterstof en batterijen zijn dragers: ze bevatten opgeslagen energie die eerst elders opgewekt is.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Welke sector in Nederland is van oudsher een zeer grote verbruiker van aardgas voor verwarming en verlichting?',
                'opties': [
                    'De bosbouw op de Veluwe',
                    'De intensieve glastuinbouw (kassen in het Westland)',
                    'De traditionele schapenhouderij',
                    'De binnenvaart op het IJsselmeer'
                ],
                'antwoord': 1,
                'uitleg': 'Glastuinbouwers stoken van oudsher veel aardgas in warmtekrachtkoppelingen om kassen warm te houden en CO2 te leveren aan planten.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat is de voornaamste oorzaak van netcongestie op het Nederlandse elektriciteitsnet?',
                'opties': [
                    'Kopersnijders die alle hoogspanningskabels doorsnijden',
                    'Een plotselinge afname van het aantal elektrische apparaten in huis',
                    'De snelle toename van zonnepanelen, windmolens, warmtepompen en laadpalen waardoor kabels en transformatoren overbelast raken',
                    'Het sluiten van alle snelwegen in Nederland'
                ],
                'antwoord': 2,
                'uitleg': 'De overstap naar elektrificatie vraagt veel meer transportcapaciteit dan waar het historische stroomnetwerk op berekend was.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat betekent het NIMBY-syndroom bij ruimtelijke projecten voor duurzame energie?',
                'opties': [
                    'Niemand wil meer schone energie gebruiken',
                    'Boeren eisen dat alle windmolens op zee worden gebouwd',
                    'Iedereen wil direct een kerncentrale in zijn achtertuin',
                    'Mensen zijn voorstander van duurzame energie, maar willen de windmolens of zonneparken niet in hun eigen directe woonomgeving (Not In My Back Yard)'
                ],
                'antwoord': 3,
                'uitleg': 'NIMBY (Not In My Back Yard) ontstaat wanneer burgers vrezen voor horizonvervuiling, geluidshinder of waardedaling van hun woning.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Waarom biedt het bestaande Nederlandse gasnetwerk een groot voordeel voor de toekomstige overstap op waterstof?',
                'opties': [
                    'Omdat de ondergrondse leidingen na inspectie en technische aanpassingen kunnen worden ingezet om waterstofgas naar de industrie te transporteren',
                    'Omdat waterstof spontaan in de gasbuizen ontstaat',
                    'Omdat de buizen gratis door buurlanden onderhouden worden',
                    'Omdat waterstof precies dezelfde moleculaire samenstelling heeft als Gronings aardgas'
                ],
                'antwoord': 0,
                'uitleg': 'Het fijnmazige gasnet van Gasunie en regionale netbeheerders kan deels worden omgebouwd tot een landelijke waterstofbackbone.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Hoeveel procent reductie van broeikasgassen moet Nederland volgens de Klimaatwet in 2030 bereikt hebben ten opzichte van 1990?',
                'opties': [
                    'Minimaal 20%',
                    'Minimaal 55%',
                    'Precies 80%',
                    '100% (volledig klimaatneutraal)'
                ],
                'antwoord': 1,
                'uitleg': 'De Nederlandse wet stelt de doelstelling op minimaal 55% reductie in 2030.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke industriële regio in Nederland is verantwoordelijk voor een zeer groot aandeel in de nationale industriële CO2-uitstoot?',
                'opties': [
                    'De heidevelden van Drenthe',
                    'De duinen van Texel',
                    'Het haven- en industriegebied van Rotterdam (Rijnmond)',
                    'De heuvels van Zuid-Limburg'
                ],
                'antwoord': 2,
                'uitleg': 'In de Rotterdamse haven concentreren zich olieraffinaderijen en petrochemische fabrieken die grote hoeveelheden energie verbruiken.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat is een groot bezwaar van omwonenden tegen grote windturbines op land?',
                'opties': [
                    'Ze trekken gevaarlijke wilde dieren aan',
                    'Ze verlagen de buitentemperatuur met tien graden',
                    'Ze maken de lucht te droog om te ademen',
                    'Geluidsoverlast (zoemend geluid), horizonvervuiling en periodieke slagschaduw op hun woning'
                ],
                'antwoord': 3,
                'uitleg': 'Draaiende wieken kunnen flikkerende schaduwen werpen en laagfrequent geluid veroorzaken dat omwonenden stoort.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is een belangrijk voordeel van waterstof voor zware industriële processen (zoals staalproductie bij Tata Steel)?',
                'opties': [
                    'Waterstof kan de extreem hoge temperaturen leveren die nodig zijn om ijzererts te reduceren zonder dat er CO2 ontstaat',
                    'Waterstof is goedkoper dan kraanwater',
                    'Waterstof hoeft niet vervoerd te worden',
                    'Waterstof maakt staal vanzelf roestvrij'
                ],
                'antwoord': 0,
                'uitleg': 'Groene waterstof kan steenkool vervangen bij het smelten en zuiveren van ruwijzer, waarbij alleen waterdamp vrijkomt.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Waarom ontstaan er in Nederland vaak ruimtelijke conflicten rondom de aanleg van grootschalige zonneparken?',
                'opties': [
                    'Omdat zonnepanelen giftige gassen naar de bodem blazen',
                    'Omdat de beschikbare ruimte schaars is en boeren of burgers liever landbouw, natuur of woningbouw op die grond zien',
                    'Omdat zonneparken alleen in het donker werken',
                    'Omdat zonnepanelen verboden zijn in provincies buiten de Randstad'
                ],
                'antwoord': 1,
                'uitleg': 'In een dichtbevolkt land concurreert de energietransitie rechtstreeks met landbouw, woningbouw en natuurontwikkeling.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Hoe kan de glastuinbouwsector zijn CO2-uitstoot drastisch verminderen zonder kassen te sluiten?',
                'opties': [
                    'Door alleen nog in de vrieskou te telen',
                    'Door alle lampen in kassen te vervangen door kaarsen',
                    'Door over te schakelen op diepe aardwarmte (geothermie) en industriële restwarmte',
                    'Door kassen alleen nog op steenkool te verwarmen'
                ],
                'antwoord': 2,
                'uitleg': 'Veel glastuinbouwgebieden benutten inmiddels geothermiebronnen om kassen duurzaam te verwarmen.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat gebeurt er tijdens het proces van elektrolyse?',
                'opties': [
                    'Aardolie wordt omgezet in plastic korrels',
                    'Kolen worden vermalen tot poeder',
                    'Uranium wordt gespleten in een kernreactor',
                    'Watermoleculen (H2O) worden met behulp van elektriciteit gesplitst in waterstofgas (H2) en zuurstofgas (O2)'
                ],
                'antwoord': 3,
                'uitleg': 'Elektrolyse gebruikt elektrische stroom om water te ontleden in waterstof en zuurstof.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'De Nederlandse Klimaatwet verplicht de regering om periodiek klimaatplannen op te stellen om de uitstootdoelen te halen.',
                'antwoord': True,
                'uitleg': 'Waar: de wet schrijft voor dat het kabinet elke paar jaar een klimaatplan en voortgangsrapportage presenteert.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'Nederland heeft binnen Europa altijd de allergeringste CO2-uitstoot per inwoner gehad.',
                'antwoord': False,
                'uitleg': 'Onwaar: door zware havenindustrie, kassen en intensieve veeteelt lag de uitstoot per inwoner in Nederland historisch juist bovengemiddeld hoog.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'Het opwekken van groene waterstof via elektrolyse levert direct grote hoeveelheden koolstofdioxide op.',
                'antwoord': False,
                'uitleg': 'Onwaar: bij de elektrolyse van water ontstaat uitsluitend waterstof en zuurstof; als de stroom groen is, is het proces emissievrij.'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'Netcongestie kan ervoor zorgen dat nieuwe woonwijken of bedrijven moeten wachten op een aansluiting op het stroomnet.',
                'antwoord': True,
                'uitleg': 'Waar: door capaciteitstekorten op het hoogspannings- en middenspanningsnet ontstaat er in diverse provincies een aansluitstop.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'Het verschijnsel dat het elektriciteitsnet vol zit waardoor stroom niet getransporteerd kan worden, heet net....',
                'antwoord': 'congestie',
                'uitleg': 'Netcongestie betekent filevorming op het elektriciteitsnetwerk.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'Meningsverschillen over de bestemming en inrichting van schaarse landoppervlakte noemen we een .... conflict.',
                'antwoord': 'ruimtelijk',
                'uitleg': 'Een ruimtelijk conflict ontstaat bij botsende belangen over grondgebruik.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Waarom wordt waterstof geclassificeerd als een drager en niet als een primaire bron?',
                'sleutelwoorden': [
                    'produceren/geproduceerd/maken/gemaakt/fabriceren'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Waterstof komt niet kant-en-klaar voor en moet eerst kunstmatig geproduceerd worden.',
                'uitleg': 'Je moet waterstof eerst vervaardigen met stroom voordat het als energieopslag kan dienen.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Noem een oorzaak waarom omwonenden bezwaar kunnen maken tegen de bouw van een windmolenpark vlak bij hun woning.',
                'sleutelwoorden': [
                    'geluid/slagschaduw/horizon/uitzicht/waardedaling'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Omwonenden vrezen voor geluidsoverlast, periodieke slagschaduw op hun ramen of horizonvervuiling.',
                'uitleg': 'Slagschaduw, geluid en aantasting van het landschap zijn de voornaamste bezwaren.'
            }
        ]
    }
]

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    for ex in EXAMENS:
        path = os.path.join(BASE_DIR, ex['file'])
        content = f"""/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — {ex['titel']}
   buiteNLand 3 HAVO Hoofdstuk 4 (Energietransitie)
   ========================================================= */
DURU.registerExamen({{
  id: "{ex['id']}",
  hoofdstuk: {ex['hoofdstuk']},
  paragraaf: "{ex['paragraaf']}",
  hoofdstukTitel: "Hoofdstuk 4 — Energietransitie",
  titel: "{ex['titel']}",
  vak: "Aardrijkskunde · HAVO 3 (H4)",
  icoon: "{ex['icoon']}",
  duurMin: {ex['duurMin']},
  vragen: {json.dumps(ex['vragen'], indent=4, ensure_ascii=False)}
}});
"""
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Geschreven: {path} (vragen: {len(ex['vragen'])})")

if __name__ == '__main__':
    main()
