"""
Script om Aardrijkskunde Hoofdstuk 4 (Energietransitie) te genereren:
- 5 Onderwerpen (h4_1.js t/m h4_5.js)
- 5 Proeftoetsen (examen_16.js t/m examen_20.js)
Gebaseerd op buiteNLand 3 HAVO Hoofdstuk 4 (Energietransitie, p. 148-190).
"""
import os
import json

BASE_DIR = 'havo3/aardrijkskunde/js/data'

ONDERWERPEN = [
    {
        'file': 'h4_1.js',
        'id': 'ak-h4-1',
        'hoofdstuk': 4,
        'paragraaf': '4.1',
        'titel': 'De aarde warmt op!',
        'korteUitleg': 'Feiten over klimaatopwarming, broeikasgassen en mondiale gevolgen.',
        'icoon': '🌡️',
        'kleur': 'h4-thema',
        'theorie': """<h3>4.1 De aarde warmt op!</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Broeikasgassen (CO2, methaan, lachgas), versterkt broeikaseffect, mondiale gevolgen, zeespiegelstijging, piekafvoeren, klimaatmigranten, biodiversiteit.
</div>

<h4>1. Feiten over de klimaatopwarming</h4>
<p>Vrijwel alle klimaatwetenschappers zijn het erover eens: de aarde warmt in hoog tempo op. Dit blijkt uit onweerlegbare metingen over de hele wereld:</p>
<ul>
  <li><b>Stijgende temperaturen:</b> Sinds de industriële revolutie stijgt de wereldwijde gemiddelde temperatuur gestaag. De afgelopen decennia sneuvelen wereldwijd hitterecords.</li>
  <li><b>Smeltend ijs:</b> Gletsjers in gebergten trekken zich massaal terug en de grote ijskappen van Groenland en Antarctica verliezen netto honderden miljarden tonnen ijs per jaar.</li>
  <li><b>Zeespiegelstijging:</b> Doordat gletsjers en landijs smelten én doordat zeewater uitzet naarmate het warmer wordt (thermische expansie), stijgt het niveau van de oceanen wereldwijd.</li>
  <li><b>Vertraging in het klimaatsysteem:</b> Zelfs als vandaag alle uitstoot van broeikasgassen onmiddellijk zou stoppen, zet de opwarming nog tientallen jaren door vanwege de traagheid van oceanen en ijskappen.</li>
</ul>

<h4>2. Oorzaken: Het versterkte broeikaseffect</h4>
<p>Het <i>natuurlijke broeikaseffect</i> is noodzakelijk voor leven op aarde; zonder broeikasgassen in de atmosfeer zou de gemiddelde temperatuur -18 graden Celsius zijn in plaats van de aangename +15 graden Celsius. Echter, door menselijke activiteiten (verbranding van fossiele brandstoffen als steenkool, aardolie en aardgas, ontbossing en industriële landbouw) komen er enorme hoeveelheden extra broeikasgassen in de dampkring terecht. Dit noemen we het <b>versterkte broeikaseffect</b>.</p>
<p>De belangrijkste broeikasgassen zijn:</p>
<ul>
  <li><b>Koolstofdioxide (CO2):</b> Komt vooral vrij bij de verbranding van fossiele brandstoffen in fabrieken, elektriciteitscentrales en het verkeer.</li>
  <li><b>Methaan (CH4):</b> Een zeer krachtig broeikasgas dat vrijkomt bij veeteelt (o.a. koeien), natte rijstbouw, afvalstortplaatsen en smeltende permafrost.</li>
  <li><b>Distikstofmonoxide (lachgas, N2O):</b> Komt vrij door het gebruik van kunstmest in de intensieve landbouw en chemische industrie.</li>
</ul>

<h4>3. Mondiale gevolgen</h4>
<p>De gevolgen van klimaatverandering zijn mondiaal (wereldwijd) voelbaar:</p>
<ul>
  <li><b>Extremer weer:</b> Meer langdurige hittegolven, aanhoudende droogteperiodes enerzijds, en hevigere stortbuien met <i>piekafvoeren</i> in rivieren en plotselinge overstromingen anderzijds.</li>
  <li><b>Bedreiging van de voedselzekerheid:</b> In subtropische en droge gebieden (zoals de Sahel en delen van Azië) mislukken oogsten vaker door watertekorten en hittestress.</li>
  <li><b>Klimaatmigranten:</b> Mensen die gedwongen moeten verhuizen omdat hun leefomgeving onbewoonbaar wordt door zeespiegelstijging, kusterosie of extreme droogte.</li>
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat is de belangrijkste oorzaak van het versterkte broeikaseffect sinds de industriële revolutie?',
                'opties': [
                    'Het grootschalig verbranden van fossiele brandstoffen door menselijke activiteiten',
                    'Natuurlijke variaties in de baan van de aarde rond de zon',
                    'Het toenemende aantal vulkaanuitbarstingen wereldwijd',
                    'Warmte die direct uit het binnenste van de aarde naar buiten lekt'
                ],
                'antwoord': 0,
                'uitleg': 'Het versterkte broeikaseffect ontstaat doordat de mens op grote schaal fossiele brandstoffen verbrandt en bossen kapt.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke twee processen zorgen er samen voor dat de zeespiegel wereldwijd stijgt?',
                'opties': [
                    'Het smelten van zee-ijs en het toenemen van zandafzetting aan de kusten',
                    'Het smelten van landijs en gletsjers plus het uitzetten van warmer zeewater',
                    'Verhoogde verdamping boven de tropen en toegenomen regenval op zee',
                    'Bodemdaling van de oceaanbodem en beweging van tektonische platen'
                ],
                'antwoord': 1,
                'uitleg': 'Zeespiegelstijging ontstaat door smeltend landijs en gletsjers plus thermische expansie (warm water zet uit).'
            },
            {
                'type': 'mc',
                'vraag': 'Welk broeikasgas komt in aanzienlijke hoeveelheden vrij bij intensieve veeteelt en natte rijstbouw?',
                'opties': [
                    'Zwaveldioxide',
                    'Stikstofgas',
                    'Methaan',
                    'Argon'
                ],
                'antwoord': 2,
                'uitleg': 'Methaan (CH4) ontstaat onder andere bij de spijsvertering van herkauwers en in zuurstofarme rijstvelden.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom zou de opwarming van de aarde nog tientallen jaren doorgaan als vandaag alle uitstoot zou stoppen?',
                'opties': [
                    'Omdat planten direct stoppen met het opnemen van zonlicht',
                    'Omdat de dampkring geen gassen kan vasthouden',
                    'Omdat de oceanen en ijskappen veel tijd nodig hebben om zich aan te passen aan de nieuwe temperatuur',
                    'Omdat de aarde steeds dichter bij de zon komt te staan'
                ],
                'antwoord': 2,
                'uitleg': 'Door de enorme warmtecapaciteit en traagheid van de oceanen reageert het klimaatsysteem vertraagd op veranderingen.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men in de fysische geografie onder een piekafvoer van een rivier?',
                'opties': [
                    'Het moment in de zomer waarop een rivier helemaal droogvalt',
                    'Een extreem hoge waterafvoer na hevige regenval of plotseling smeltwater',
                    'De gemiddelde hoeveelheid water die een rivier per jaar afvoert',
                    'De diepte van de rivierbedding gemeten bij de bron'
                ],
                'antwoord': 1,
                'uitleg': 'Een piekafvoer is een tijdelijk zeer hoge waterafvoer in een rivier die tot overstromingen kan leiden.'
            },
            {
                'type': 'mc',
                'vraag': 'Hoe noemen we mensen die hun woongebied noodgedwongen moeten verlaten door bijvoorbeeld aanhoudende droogte of overstromingen?',
                'opties': [
                    'Kennismigranten',
                    'Gastarbeiders',
                    'Klimaatmigranten',
                    'Expats'
                ],
                'antwoord': 2,
                'uitleg': 'Klimaatmigranten (of milieuvluchtelingen) migreren omdat hun omgeving door ecologische veranderingen onleefbaar wordt.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Zonder het natuurlijke broeikaseffect zou de aarde veel te koud zijn voor menselijk leven.',
                'antwoord': True,
                'uitleg': 'Waar: zonder het natuurlijke broeikaseffect zou de aarde gemiddeld zo n min 18 graden zijn in plaats van plus 15 graden.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Het smelten van drijvend zee-ijs op de Noordpool draagt direct bij aan een grote stijging van de zeespiegel.',
                'antwoord': False,
                'uitleg': 'Onwaar: drijvend zee-ijs verplaatst al evenveel water als zijn eigen gewicht; alleen smeltend landijs verhoogt de zeespiegel direct.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Lachgas (distikstofmonoxide) is een broeikasgas dat vrijkomt bij het gebruik van kunstmest in de landbouw.',
                'antwoord': True,
                'uitleg': 'Waar: lachgas ontstaat door microbiologische processen in zwaar bemeste landbouwbodems.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welk krachtig broeikasgas met chemische formule CH4 komt vooral vrij bij de veehouderij en afvalstorten?',
                'antwoord': 'methaan',
                'uitleg': 'Methaan (CH4) is een zeer effectief broeikasgas dat veel warmte vasthoudt in de atmosfeer.'
            }
        ]
    },
    {
        'file': 'h4_2.js',
        'id': 'ak-h4-2',
        'hoofdstuk': 4,
        'paragraaf': '4.2',
        'titel': 'Op weg naar duurzame energiebronnen',
        'korteUitleg': 'Traditionele versus niet-conventionele energiebronnen, kernenergie en de noodzaak tot transitie.',
        'icoon': '🛢️',
        'kleur': 'h4-thema',
        'theorie': """<h3>4.2 Op weg naar duurzame energiebronnen</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Fossiele brandstoffen, uitputbare energiebronnen, conventionele olie en gas, niet-conventionele olie en gas, teerzand, kernenergie, uranium, radioactiviteit, CO2-voetafdruk/inw.
</div>

<h4>1. Traditionele en fossiele energiebronnen</h4>
<p>Sinds de industriële revolutie draait de wereldeconomie op fossiele brandstoffen: steenkool, aardolie en aardgas. Dit zijn <b>uitputbare energiebronnen</b>: ze zijn miljoenen jaren geleden gevormd uit samengeperste resten van planten en plankton en raken op een dag op. Bij de opwekking en het transport gaat gemiddeld tot wel twee derde van de energie verloren in de vorm van restwarmte.</p>

<h4>2. Conventionele versus niet-conventionele winning</h4>
<ul>
  <li><b>Conventionele olie en gas:</b> Olie en gas die na hun ontstaan zijn gemigreerd naar een poreus reservoirgesteente onder een ondoordringbare afsluitlaag. Deze voorraden kunnen relatief eenvoudig en goedkoop met verticale boringen worden opgepompt.</li>
  <li><b>Niet-conventionele olie en gas:</b> Olie en gas die vastzitten in het oorspronkelijke moedergesteente (zoals schaliegas en schalie-olie) of voorkomen als kleverige bitumen vermengd met zand en klei. Een bekend voorbeeld zijn de <b>teerzanden</b> in de Canadese provincie Alberta.</li>
</ul>
<p>De winning van teerzand is extreem kostbaar en belastend voor het milieu. Voor één vat ruwe olie moet zo n twee ton teerzand worden afgegraven. Het proces verbruikt reusachtige hoeveelheden heet water en energie en laat giftige bekkens met chemicaliën en zware metalen achter.</p>

<h4>3. Voor- en nadelen van kernenergie</h4>
<p>Kernenergie wordt opgewekt door het splijten van <b>uranium</b> in kerncentrales. Het is een zeer krachtige energiebron: één kilogram uranium kan net zoveel energie leveren als tientallen tonnen steenkool.</p>
<ul>
  <li><b>Voordelen:</b> Bij de stroomproductie in een kerncentrale komt geen CO2 vrij. Een kerncentrale levert continu en betrouwbaar grote hoeveelheden elektriciteit, ongeacht wind of zon.</li>
  <li><b>Nadelen:</b> Er ontstaat hoogradioactief afval dat duizenden jaren veilig ondergronds moet worden opgeslagen. Daarnaast bestaat er altijd een risico op ernstige kernongevallen (zoals Tsjernobyl in 1986 en Fukushima in 2011 door een tsunami), waarbij grote gebieden decennialang onbewoonbaar raken door dodelijke straling.</li>
</ul>

<h4>4. De noodzaak van de energietransitie</h4>
<p>De <b>energietransitie</b> is de structurele overstap van fossiele en uitputbare brandstoffen naar duurzame, hernieuwbare energiebronnen die geen broeikasgassen uitstoten en nooit opraken. Deze overstap is noodzakelijk om catastrofale klimaatverandering te voorkomen en om niet langer afhankelijk te zijn van instabiele exportlanden van olie en gas.</p>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste kenmerk van conventionele olie en gas?',
                'opties': [
                    'Het is makkelijk te winnen doordat het zich verzameld heeft in een poreus reservoirgesteente',
                    'Het kan uitsluitend worden gewonnen door open mijnbouw in zandgroeven',
                    'Het stoot bij verbranding helemaal geen koolstofdioxide uit',
                    'Het ontstaat binnen enkele weken uit huishoudelijk afval'
                ],
                'antwoord': 0,
                'uitleg': 'Conventioneel gas en olie bevinden zich in reservoirgesteenten en kunnen relatief gemakkelijk omhoog gepompt worden.'
            },
            {
                'type': 'mc',
                'vraag': 'In welk land liggen enorme voorraden teerzand waarvan de winning grote landschappelijke schade veroorzaakt?',
                'opties': [
                    'Saoedi-Arabië',
                    'Canada',
                    'Noorwegen',
                    'Japan'
                ],
                'antwoord': 1,
                'uitleg': 'In Canada (vooral Alberta) wordt olie op grote schaal gewonnen uit uitgestrekte teerzandvelden.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke grondstof wordt in kerncentrales gebruikt als splijtstof om elektriciteit op te wekken?',
                'opties': [
                    'Bauxiet',
                    'Steenkool',
                    'Uranium',
                    'Lithium'
                ],
                'antwoord': 2,
                'uitleg': 'Kerncentrales gebruiken uranium als splijtstof voor de nucleaire kettingreactie.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een groot milieutechnisch voordeel van kernenergie vergeleken met kolencentrales?',
                'opties': [
                    'Er ontstaat tijdens de stroomopwekking geen directe uitstoot van CO2',
                    'Er blijft na gebruik geen enkel schadelijk afval over',
                    'Kerncentrales zijn gratis en eenvoudig te bouwen',
                    'De brandstof uranium is onuitputtelijk en groeit overal aan bomen'
                ],
                'antwoord': 0,
                'uitleg': 'Bij kernsplijting komt geen CO2 vrij, wat helpt in de strijd tegen het broeikaseffect.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een groot nadeel van het delven van olie uit teerzanden?',
                'opties': [
                    'Het vereist enorm veel energie en heet water en laat giftig afval achter',
                    'Er kan helemaal geen bruikbare brandstof uit gewonnen worden',
                    'Het kan alleen midden op volle zee worden uitgevoerd',
                    'Het veroorzaakt overmatige afkoeling van de atmosfeer'
                ],
                'antwoord': 0,
                'uitleg': 'Teerzandwinning vergt reusachtige hoeveelheden water en energie en veroorzaakt ernstige milieuvervuiling.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaan we onder het begrip energietransitie?',
                'opties': [
                    'Het sluiten van alle fabrieken en transportbedrijven in een land',
                    'De overstap van fossiele brandstoffen naar hernieuwbare en schone energiebronnen',
                    'Het vervangen van benzineauto s door uitsluitend dieseltreinen',
                    'Het verhogen van de gasprijzen om de staatskas aan te vullen'
                ],
                'antwoord': 1,
                'uitleg': 'Energietransitie betekent de omschakeling van fossiele brandstoffen naar duurzame energiebronnen.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Aardolie, aardgas en steenkool noemen we uitputbare energiebronnen omdat ze sneller worden verbruikt dan de natuur ze kan aanmaken.',
                'antwoord': True,
                'uitleg': 'Waar: de vorming van fossiele brandstoffen duurt miljoenen jaren, waardoor de voorraad eindig is.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Kernafval verliest binnen enkele dagen al zijn radioactiviteit en kan als gewone compost worden hergebruikt.',
                'antwoord': False,
                'uitleg': 'Onwaar: hoogradioactief afval blijft tienduizenden jaren gevaarlijk stralend en moet zorgvuldig worden opgeborgen.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Bij het kernongeval in Fukushima in 2011 speelde een zware tsunami een cruciale rol bij het uitvallen van de koelsystemen.',
                'antwoord': True,
                'uitleg': 'Waar: de vloedgolf overspoelde de noodgeneratoren waardoor de koeling uitviel en een meltdown ontstond.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welk zwaar metaal dient als voornaamste splijtstof in kernreactoren?',
                'antwoord': 'uranium',
                'uitleg': 'Uranium is het radioactieve element waarvan de atoomkernen worden gespleten om warmte en stroom op te wekken.'
            }
        ]
    },
    {
        'file': 'h4_3.js',
        'id': 'ak-h4-3',
        'hoofdstuk': 4,
        'paragraaf': '4.3',
        'titel': 'Het tegengaan van klimaatverandering',
        'korteUitleg': 'Duurzame energiebronnen, internationale klimaatakkoorden en klimaatrechtvaardigheid.',
        'icoon': '☀️',
        'kleur': 'h4-thema',
        'theorie': """<h3>4.3 Het tegengaan van klimaatverandering</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Duurzame/hernieuwbare energie, zonne-energie, windenergie, waterkracht, geothermische energie (aardwarmte), biomassa, klimaatakkoord van Parijs, klimaatschadefonds.
</div>

<h4>1. Duurzame en hernieuwbare energiebronnen</h4>
<p>Om de uitstoot van broeikasgassen drastisch te verminderen, moeten we overschakelen op <b>duurzame of hernieuwbare energiebronnen</b>. Deze bronnen raken nooit op en veroorzaken bij de opwekking geen CO2-uitstoot. De belangrijkste vormen zijn:</p>
<ul>
  <li><b>Zonne-energie:</b> Het omzetten van zonlicht in elektriciteit via zonnepanelen (fotovoltaïsche cellen) of in warmte via zonnecollectoren. De zon straalt iedere dag duizenden malen meer energie naar de aarde dan de mensheid verbruikt.</li>
  <li><b>Windenergie:</b> Windturbines op land (onshore) of op zee (offshore) zetten de bewegingsenergie van luchtstromen om in elektriciteit. Wind op zee waait krachtiger en constanter, maar de installatie en het onderhoud zijn duurder.</li>
  <li><b>Waterkracht:</b> Elektriciteit opwekken met behulp van stromend of vallend water via stuwdammen in rivieren of getijdencentrales aan de kust.</li>
  <li><b>Geothermische energie (aardwarmte):</b> Het benutten van de natuurlijke hitte die diep in de aardkorst aanwezig is om gebouwen te verwarmen of stoomturbines aan te drijven (veel toegepast in vulkanische gebieden zoals IJsland).</li>
  <li><b>Biomassa:</b> Energie halen uit organisch materiaal zoals snoeihout, gft-afval, mest of plantaardige oliën. Let op: bij verbranding van biomassa komt wel CO2 vrij, maar die is recentelijk door planten opgenomen (kortcyclische koolstofkringloop).</li>
</ul>

<h4>2. Nadelen en uitdagingen van duurzame energie</h4>
<p>Hoewel duurzame bronnen onmisbaar zijn, kennen ze ook uitdagingen:</p>
<ul>
  <li><b>Ruimtebeslag:</b> Windparken en zonnevelden nemen per opgewekte megawatt veel meer landoppervlakte in beslag dan een compacte kolen- of kerncentrale.</li>
  <li><b>Intermittentie (weersafhankelijkheid):</b> De zon schijnt niet s nachts en de wind waait niet altijd even hard. Daarom is grootschalige energieopslag (zoals batterijen en waterstof) cruciaal.</li>
  <li><b>Grondstoffen:</b> Voor zonnepanelen, windturbines en accu s zijn grote hoeveelheden zeldzame metalen en mineralen nodig (zoals koper, lithium, kobalt en neodymium).</li>
</ul>

<h4>3. Internationale afspraken en klimaatrechtvaardigheid</h4>
<p>Klimaatverandering houdt niet op bij landsgrenzen. Tijdens de klimaattop in Parijs (2015) spraken bijna 200 landen af om de opwarming van de aarde te beperken tot ruim onder de 2 graden Celsius, en bij voorkeur tot maximaal 1,5 graad Celsius ten opzichte van het pre-industriële tijdperk.</p>
<p><b>Klimaatrechtvaardigheid:</b> Historisch gezien hebben rijke westerse landen de meeste fossiele brandstoffen verstookt en dus de grootste schuld aan het probleem. Veel arme ontwikkelingslanden (zoals eilandstaten in de Stille Oceaan of landen in de Sahel) stoten zelf vrijwel niets uit, maar worden wel het hardst getroffen door zeespiegelstijging en extreme droogte. Daarom is internationaal afgesproken dat rijke landen arme landen financieel moeten compenseren en ondersteunen via een <b>klimaatschadefonds</b>.</p>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Hoe noemen we energie die wordt opgewekt door gebruik te maken van de hitte diep in de aarde?',
                'opties': [
                    'Geothermische energie (aardwarmte)',
                    'Biomassa-energie',
                    'Kernfusie-energie',
                    'Getijdenenergie'
                ],
                'antwoord': 0,
                'uitleg': 'Aardwarmte of geothermische energie maakt gebruik van heet water of stoom uit diepe aardlagen.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste doel van het historische Klimaatakkoord van Parijs (2015)?',
                'opties': [
                    'Het wereldwijde gebruik van steenkool verdubbelen vóór 2030',
                    'De opwarming van de aarde beperken tot ruim onder de 2 °C, bij voorkeur 1,5 °C',
                    'Alle kerncentrales in de wereld onmiddellijk ontmantelen',
                    'Het verplichten van alle burgers om uitsluitend per trein te reizen'
                ],
                'antwoord': 1,
                'uitleg': 'Het Akkoord van Parijs streeft ernaar de opwarming te beperken tot maximaal 1,5 tot 2 graden Celsius.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom waait de wind op zee (offshore windparken) vaak constanter en harder dan op land?',
                'opties': [
                    'Omdat de zwaartekracht op zee minder krachtig is',
                    'Omdat er op open zee geen obstakels zoals heuvels, bomen en gebouwen zijn die wrijving veroorzaken',
                    'Omdat de wolken boven zee altijd kouder zijn dan boven land',
                    'Omdat schepen de luchtstroom kunstmatig aandrijven'
                ],
                'antwoord': 1,
                'uitleg': 'Door het vlakke wateroppervlak is de ruwheid laag en ondervindt de wind nauwelijks wrijvingsweerstand.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men in het internationale klimaatbeleid onder klimaatrechtvaardigheid?',
                'opties': [
                    'Dat arme landen alle kosten van de energietransitie moeten betalen',
                    'Dat elk land precies evenveel windmolens moet plaatsen',
                    'Dat rijke landen die historisch de meeste CO2 uitstootten arme kwetsbare landen financieel steunen',
                    'Dat alle rechtszaken over het weer verboden worden'
                ],
                'antwoord': 2,
                'uitleg': 'Klimaatrechtvaardigheid betekent dat de historische vervuilers verantwoordelijkheid nemen voor kwetsbare ontwikkelingslanden.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke brandstof valt onder biomassa?',
                'opties': [
                    'Steenkool uit diepe mijnschachten',
                    'Ruwe aardolie uit boorplatforms',
                    'Houtsnippers, snoeiafval en dierlijke mest',
                    'Vloeibaar aardgas (LNG)'
                ],
                'antwoord': 2,
                'uitleg': 'Biomassa bestaat uit organisch restmateriaal zoals hout, plantaardig afval en mest.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een belangrijk nadeel van wind- en zonne-energie ten opzichte van gascentrales?',
                'opties': [
                    'Ze stoten bij de opwekking enorme hoeveelheden zwavel uit',
                    'Ze zijn weersafhankelijk waardoor vraag en aanbod niet altijd gelijk lopen',
                    'Ze kunnen alleen op de Noordpool geplaatst worden',
                    'Ze veroorzaken een permanente verdwijning van de zwaartekracht'
                ],
                'antwoord': 1,
                'uitleg': 'Doordat de wind niet altijd waait en de zon niet altijd schijnt, is opslag of back-upcapaciteit nodig.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Waterkrachtcentrales maken gebruik van vallend of snelstromend water om turbines in beweging te brengen.',
                'antwoord': True,
                'uitleg': 'Waar: het hoogteverschil bij stuwdammen zet potentiële energie van water om in elektriciteit.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Zonnepanelen wekken alleen elektriciteit op als de buitentemperatuur warmer is dan 30 graden Celsius.',
                'antwoord': False,
                'uitleg': 'Onwaar: zonnepanelen werken op lichtintensiteit en functioneren bij koud en helder weer juist zeer efficiënt.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'De internationale luchtvaart en scheepvaart zijn vanaf het allereerste begin volledig opgenomen in de bindende doelen van het Parijs-akkoord.',
                'antwoord': False,
                'uitleg': 'Onwaar: internationale luchtvaart en scheepvaart vallen grotendeels buiten de nationale afspraken van het Parijs-akkoord.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe noemen we energie afkomstig uit biologisch restafval zoals houtsnippers en mest?',
                'antwoord': 'biomassa',
                'uitleg': 'Biomassa is organisch materiaal dat gebruikt wordt om groene stroom, warmte of biobrandstoffen te maken.'
            }
        ]
    },
    {
        'file': 'h4_4.js',
        'id': 'ak-h4-4',
        'hoofdstuk': 4,
        'paragraaf': '4.4',
        'titel': 'Klimaatverandering in Europa',
        'korteUitleg': 'Europese gevolgen, regionale klimaatzones en de Europese Green Deal.',
        'icoon': '🇪🇺',
        'kleur': 'h4-thema',
        'theorie': """<h3>4.4 Klimaatverandering in Europa</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Continentale gevolgen, Europese Green Deal, klimaatzones, hittestress, waterstress, Mediterrane regio, Atlantische regio, Berggebieden, klimaatadaptatie.
</div>

<h4>1. Europa warmt sneller op dan het wereldgemiddelde</h4>
<p>Wanneer we inzoomen op het continentale schaalniveau van Europa, blijkt dat Europa sinds de pre-industriële tijd gemiddeld <b>ruim 2,1 °C</b> is opgewarmd. Dat is bijna twee keer zo snel als het wereldwijde gemiddelde van circa 1,1 °C. De afgelopen decennia volgen recordwarme jaren elkaar in hoog tempo op. Hittegolven duren langer, winters worden zachter en berggebieden verliezen in recordtempo gletsjerijs.</p>

<h4>2. Grote regionale verschillen binnen Europa</h4>
<p>Europa is geografisch gevarieerd, waardoor de gevolgen van klimaatverandering per regio sterk verschillen:</p>
<ul>
  <li><b>De Mediterrane regio (Zuid-Europa):</b> Deze regio wordt het hardst getroffen door extreme hitte en aanhoudende droogte. Dit leidt tot ernstige <i>waterstress</i> (tekort aan zoetwater), mislukte oogsten, toenemende <i>verwoestijning</i> en verwoestende bosbranden in landen als Spanje, Griekenland en Portugal.</li>
  <li><b>De Atlantische regio (o.a. Nederland, België, West-Frankrijk, VK):</b> Gekenmerkt door een stijgende zeespiegel, meer stormschade in de winter en een toename van extreem zware stortbuien die in steden en langs rivieren voor acute wateroverlast zorgen. Tegelijkertijd treden er in de zomer langere droogteperiodes op.</li>
  <li><b>Berggebieden (zoals de Alpen en Pyreneeën):</b> Zeer kwetsbaar voor temperatuurstijging. Gletsjers smelten in rap tempo weg, permafrost in rotswanden ontdooit (waardoor rotslawines en aardverschuivingen ontstaan) en het wintertoerisme staat onder zware druk door gebrek aan natuurlijke sneeuw.</li>
  <li><b>Het Noordpoolgebied en Noord-Europa:</b> Hier verdwijnt zee-ijs en landijs snel en ontdooit de permafrost. Aan de andere kant wordt het groeiseizoen voor de landbouw langer.</li>
  <li><b>De Continentale regio (Midden- en Oost-Europa):</b> Grotere extremen tussen hete zomers met bosbranden en overstromingen door rivieren in de lente en winter.</li>
</ul>

<h4>3. Klimaatadaptatie en de Europese Green Deal</h4>
<p>Om deze uitdagingen het hoofd te bieden, heeft de Europese Unie de <b>Europese Green Deal</b> gelanceerd. Het doel is om van Europa vóór 2050 het eerste klimaatneutrale continent ter wereld te maken, met als tussendoel minimaal 55% minder uitstoot in 2030.</p>
<p>Naast <i>mitigatie</i> (het verminderen van uitstoot) is <b>klimaatadaptatie</b> noodzakelijk: het aanpassen van de leefomgeving aan de onvermijdelijke gevolgen van klimaatverandering. Voorbeelden zijn:</p>
<ul>
  <li>Steden vergroenen met parken, groene daken en waterpleinen om hittestress tegen te gaan (steden zijn warmte-eilanden).</li>
  <li>Rivieren meer ruimte geven (zoals het Nederlandse project <i>Ruimte voor de Rivier</i>) om piekafvoeren veilig naar zee te leiden.</li>
  <li>Dijken versterken en duinen verbreden tegen de stijgende zeespiegel.</li>
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Hoeveel is het Europese continent gemiddeld opgewarmd sinds de industriële revolutie vergeleken met het wereldgemiddelde?',
                'opties': [
                    'Ongeveer 2,1 °C, wat bijna twee keer zo snel is als het wereldwijde gemiddelde',
                    'Slechts 0,2 °C, omdat de Atlantische Oceaan alle warmte tegenhoudt',
                    'Precies evenveel als elk ander continent op aarde',
                    'Europa is gemiddeld juist 1,5 °C kouder geworden'
                ],
                'antwoord': 0,
                'uitleg': 'Europa warmt sneller op dan andere continenten: al meer dan 2,1 °C ten opzichte van het pre-industriële tijdperk.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke Europese regio heeft vooral te maken met ernstige waterstress, hittegolven en verwoestende bosbranden?',
                'opties': [
                    'Het Scandinavische fjordenlandschap',
                    'De Mediterrane regio rond de Middellandse Zee',
                    'De Schotse Hooglanden',
                    'De Baltische staten'
                ],
                'antwoord': 1,
                'uitleg': 'Het Middellandse Zeegebied (Zuid-Europa) heeft zwaar te lijden onder droogte, hittegolven en bosbranden.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het hoofddoel van de Europese Green Deal van de Europese Unie?',
                'opties': [
                    'Alle grenzen binnen Europa permanent sluiten voor goederenvervoer',
                    'Van Europa vóór 2050 het eerste klimaatneutrale continent ter wereld maken',
                    'Alle landbouwgronden in Europa asfalteren voor zonnecentrales',
                    'Het verbieden van alle vormen van openbaar vervoer'
                ],
                'antwoord': 1,
                'uitleg': 'De Green Deal wil dat Europa in 2050 netto geen broeikasgassen meer uitstoot (klimaatneutraal).'
            },
            {
                'type': 'mc',
                'vraag': 'Wat gebeurt er in de Europese Alpen wanneer de permafrost in hoge rotswanden ontdooit?',
                'opties': [
                    'De bergen zakken direct in zee',
                    'Er ontstaan gevaarlijke rotslawines en bergstortingen doordat los gesteente niet meer bevroren vastzit',
                    'Er groeien spontaan tropische palmbomen op de bergtoppen',
                    'De rivieren vriezen permanent dicht'
                ],
                'antwoord': 1,
                'uitleg': 'Permafrost werkt als een soort natuurlijke lijm in de rotsen; ontdooiing leidt tot gevaarlijke bergstortingen.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaan we onder klimaatadaptatie in stedelijke gebieden?',
                'opties': [
                    'De stad inrichten met meer groen en waterberging om hitte en hoosbuien op te vangen',
                    'Alle ramen in de stad dichthouden zodat er geen warmte binnenkomt',
                    'Inwoners dwingen om alleen s nachts over straat te lopen',
                    'Het verhuizen van alle inwoners naar een ander werelddeel'
                ],
                'antwoord': 0,
                'uitleg': 'Adaptatie betekent aanpassen aan het veranderende klimaat, bijvoorbeeld door parken, wadi s en groene daken aan te leggen.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom zijn steden op warme zomerdagen vaak aanzienlijk heter dan het omliggende platteland (het zogeheten hitte-eilandeffect)?',
                'opties': [
                    'Omdat de zwaartekracht in een stad hoger is dan op het platteland',
                    'Omdat asfalt, steen en beton overdag veel hitte absorberen en s nachts langzaam uitstralen',
                    'Omdat stadsbewoners meer ademhalen dan mensen in dorpen',
                    'Omdat de zon in steden feller schijnt dan boven weilanden'
                ],
                'antwoord': 1,
                'uitleg': 'Donkere stenen oppervlakken nemen overdag veel zonnewarmte op en houden die warmte langdurig vast.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'In de Atlantische regio (zoals Nederland) kunnen in de toekomst zowel hevigere piekbuien als langere periodes van zomerdroogte voorkomen.',
                'antwoord': True,
                'uitleg': 'Waar: door de opwarming valt neerslag grilliger in kortere, hevigere buien, afgewisseld met drogere perioden.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'De gletsjers in de Alpen groeien sinds het jaar 2000 ieder jaar spectaculair aan.',
                'antwoord': False,
                'uitleg': 'Onwaar: de Alpengletsjers verliezen al tientallen jaren achtereen recordvolumes aan ijs en trekken zich snel terug.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Klimaatmitigatie betekent dat we maatregelen nemen om de uitstoot van broeikasgassen aan te pakken en zo verdere opwarming te voorkomen.',
                'antwoord': True,
                'uitleg': 'Waar: mitigatie pakt de oorzaak aan (uitstootbeperking), terwijl adaptatie inspeelt op de gevolgen.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe noemen we het beleidspakket van de Europese Unie dat als doel heeft om in 2050 klimaatneutraal te zijn?',
                'antwoord': 'green deal',
                'uitleg': 'De Europese Green Deal is het strategische actieplan van de EU voor een duurzame en klimaatneutrale economie.'
            }
        ]
    },
    {
        'file': 'h4_5.js',
        'id': 'ak-h4-5',
        'hoofdstuk': 4,
        'paragraaf': '4.5',
        'titel': 'Naar minder CO2-uitstoot in Nederland',
        'korteUitleg': 'Nederlands klimaatbeleid, energiedragers zoals waterstof en ruimtelijke conflicten.',
        'icoon': '🇳🇱',
        'kleur': 'h4-thema',
        'theorie': """<h3>4.5 Naar minder CO2-uitstoot in Nederland</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Nederlandse Klimaatwet, CO2-uitstoot per inwoner, ruimtelijk conflict, energiedrager, waterstof, energieopslag, netcongestie.
</div>

<h4>1. Nederland en de CO2-uitstoot</h4>
<p>Nederland heeft binnen Europa traditioneel een relatief hoge <b>CO2-uitstoot per inwoner</b>. Dit komt door verschillende structurele factoren:</p>
<ul>
  <li>Een omvangrijke chemische en zware industrie (onder andere in de haven van Rotterdam).</li>
  <li>Een zeer intensieve glastuinbouwsector die decennialang veel aardgas heeft gestookt om kassen te verwarmen en te verlichten.</li>
  <li>Een van de dichtstbevolkte en meest intensieve veehouderijsectoren ter wereld.</li>
  <li>Een groot aantal vrachtbewegingen en een druk snelwegennetwerk als logistiek knooppunt van Noordwest-Europa.</li>
</ul>
<p>Om aan de internationale verplichtingen van het Akkoord van Parijs te voldoen, heeft Nederland de <b>Klimaatwet</b> aangenomen. Deze wet verplicht de overheid om de uitstoot van broeikasgassen in 2030 met minimaal 55% te verminderen ten opzichte van 1990, en in 2050 met 95% tot 100%.</p>

<h4>2. Ruimtebeslag en ruimtelijke conflicten</h4>
<p>De overgang naar duurzame energiebronnen vraagt enorm veel landoppervlakte. Terwijl een traditionele gas- of kolencentrale weinig grond inneemt, vereisen zonneparken en windmolenparken vele hectaren ruimte. Nederland is echter een heel dichtbevolkt land met grote schaarste aan open ruimte. Hierdoor ontstaan <b>ruimtelijke conflicten</b>:</p>
<ul>
  <li><b>Windmolens op land:</b> Omwonenden protesteren vaak tegen windturbines vanwege horizonvervuiling, slagschaduw en geluidsoverlast (het zogeheten NIMBY-effect: <i>Not In My Back Yard</i>).</li>
  <li><b>Zonneparken op landbouwgrond:</b> Boeren en natuurorganisaties vinden dat vruchtbare landbouwgrond behouden moet blijven voor voedselproductie of natuurherstel in plaats van vol gelegd met zonnepanelen.</li>
  <li><b>Netcongestie:</b> Het Nederlandse elektriciteitsnet zit in veel regio s overvol doordat er massaal zonnepanelen, laadpalen en warmtepompen bijkomen. Bedrijven kunnen hierdoor geen nieuwe stroomaansluiting krijgen.</li>
</ul>

<h4>3. Energiedragers en energieopslag</h4>
<p>Omdat zon en wind niet op afroep beschikbaar zijn, is energieopslag noodzakelijk. Elektriciteit kan worden opgeslagen in batterijen, maar voor grootschalige seizoensopslag is <b>waterstof</b> veelbelovend.</p>
<p>Belangrijk verschil: waterstof is <i>geen primaire energiebron</i>, maar een <b>energiedrager</b>. Je moet het eerst maken door water te splitsen met behulp van elektriciteit (elektrolyse). Gebeurt dit met groene stroom van windparken of zonnepanelen, dan spreken we van <i>groene waterstof</i>. Nederland heeft het voordeel van een fijnmazig bestaand aardgasnetwerk, dat in de toekomst deels geschikt gemaakt kan worden voor het transport van waterstof.</p>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Waarom heeft Nederland in Europees verband van oudsher een relatief hoge CO2-uitstoot per inwoner?',
                'opties': [
                    'Door een sterke chemische industrie, intensieve glastuinbouw en veel transport',
                    'Omdat alle woningen in Nederland uitsluitend op bruinkool gestookt worden',
                    'Omdat er in Nederland geen enkele boom of bos groeit',
                    'Doordat Nederlanders gemiddeld twintig keer per jaar vliegen'
                ],
                'antwoord': 0,
                'uitleg': 'Zware havenindustrie, kassencomplexen en intensieve veehouderij zorgen voor een hoge CO2-uitstoot per capita.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste verschil tussen een energiebron en een energiedrager zoals waterstof?',
                'opties': [
                    'Een energiebron ontstaat altijd in kerncentrales; een energiedrager drijft op water',
                    'Een energiedrager komt niet kant-en-klaar in de natuur voor, maar moet eerst met energie geproduceerd worden',
                    'Een energiedrager kan nooit elektriciteit leveren',
                    'Een energiebron is altijd vloeibaar terwijl een energiedrager altijd een gas is'
                ],
                'antwoord': 1,
                'uitleg': 'Een energiedrager (zoals waterstof of een batterij) slaat energie op, maar moet eerst met behulp van een andere bron worden opgewekt.'
            },
            {
                'type': 'mc',
                'vraag': 'Hoe noemen we meningsverschillen en tegenstellingen tussen burgers, boeren en overheden over de bestemming van schaarse grond?',
                'opties': [
                    'Een demografische transitie',
                    'Een ruimtelijk conflict',
                    'Een continentale drift',
                    'Een culturele diffusie'
                ],
                'antwoord': 1,
                'uitleg': 'Een ruimtelijk conflict ontstaat wanneer verschillende partijen tegengestelde belangen hebben bij de inrichting van een gebied.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat houdt het probleem van netcongestie in Nederland in?',
                'opties': [
                    'Het internet valt dagelijks uit in het hele land',
                    'Het elektriciteitsnetwerk zit vol waardoor nieuwe windparken, zonnevelden of bedrijven niet aangesloten kunnen worden',
                    'De rivieren zijn overvol met vrachtschepen waardoor bruggen niet meer open kunnen',
                    'Er is te veel aardgas in de leidingen waardoor de druk wegvalt'
                ],
                'antwoord': 1,
                'uitleg': 'Netcongestie betekent file op het stroomnet doordat de capaciteit van kabels en transformatorstations ontoereikend is.'
            },
            {
                'type': 'mc',
                'vraag': 'Wanneer spreken we van zogeheten groene waterstof?',
                'opties': [
                    'Als de waterstof is gekleurd met een milieuvriendelijke kleurstof',
                    'Als waterstof wordt geproduceerd via elektrolyse met duurzame stroom uit zon of wind',
                    'Als de waterstof rechtstreeks uit steenkoolmijnen wordt gepompt',
                    'Als waterstof alleen in natuurgebieden wordt gebruikt'
                ],
                'antwoord': 1,
                'uitleg': 'Groene waterstof wordt gemaakt door water te splitsen met hernieuwbare zonne- of windenergie zonder CO2-uitstoot.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het wettelijke doel van de Nederlandse Klimaatwet voor de vermindering van broeikasgassen in 2030 ten opzichte van 1990?',
                'opties': [
                    'Minimaal 55% reductie van de uitstoot',
                    'Precies 10% toename van de uitstoot',
                    'Alle uitstoot in 2030 direct naar 0%',
                    'Er zijn in de wet geen jaartallen of percentages vastgelegd'
                ],
                'antwoord': 0,
                'uitleg': 'De Nederlandse Klimaatwet mikt op minimaal 55% CO2-reductie in 2030 ten opzichte van het ijkjaar 1990.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Zonne- en windparken nemen per geproduceerde kilowattuur aanzienlijk meer landoppervlakte in beslag dan een traditionele gascentrale.',
                'antwoord': True,
                'uitleg': 'Waar: hernieuwbare energiebronnen hebben een lagere energiedichtheid en vergen daarom veel meer ruimte.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Waterstof kan spontaan in grote ondergrondse gasvelden worden opgeboord zonder dat er eerst energie voor hoeft te worden opgewekt.',
                'antwoord': False,
                'uitleg': 'Onwaar: zuiver waterstofgas komt vrijwel niet los in de natuur voor en moet altijd eerst kunstmatig worden gefabriceerd.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Het bestaande Nederlandse leidingnetwerk voor aardgas kan in de toekomst deels worden hergebruikt voor het transport van waterstof.',
                'antwoord': True,
                'uitleg': 'Waar: de gasinfrastructuur kan na technische aanpassingen dienstdoen voor waterstoftransport.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welke energiedrager kan worden gemaakt door water met groene elektriciteit te splitsen via elektrolyse?',
                'antwoord': 'waterstof',
                'uitleg': 'Waterstof (H2) kan als schone energiedrager dienen voor zware industrie, transport en energieopslag.'
            }
        ]
    }
]

def balance_mc(vragen):
    mc_target = [0, 1, 2, 3, 0, 1]
    mc_idx = 0
    for v in vragen:
        if v['type'] == 'mc':
            target = mc_target[mc_idx % len(mc_target)]
            curr = v['antwoord']
            corr = v['opties'][curr]
            other = [o for i, o in enumerate(v['opties']) if i != curr]
            other.insert(target, corr)
            v['opties'] = other
            v['antwoord'] = target
            mc_idx += 1

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    for o in ONDERWERPEN:
        balance_mc(o['vragen'])
        path = os.path.join(BASE_DIR, o['file'])
        content = f"""/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §{o['paragraaf']} {o['titel']}
   buiteNLand 3 HAVO Hoofdstuk 4 (Energietransitie)
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
        print(f"Geschreven: {path} (vragen: {len(o['vragen'])}, theorie: {len(o['theorie'])} chars)")

if __name__ == '__main__':
    main()
