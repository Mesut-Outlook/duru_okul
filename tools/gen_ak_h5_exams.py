"""
Script om Aardrijkskunde Hoofdstuk 5 Proeftoetsen (examen_21.js t/m examen_25.js) te genereren.
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
        'file': 'examen_21.js',
        'id': 'ex-h3-ak-21',
        'hoofdstuk': 5,
        'paragraaf': '5.1',
        'titel': 'Proeftoets 21 — §5.1 Wapengeweld wereldwijd',
        'icoon': '🌍',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste verschil tussen een staat en een natie (volk)?',
                'opties': [
                    'Een staat is een soeverein begrensd grondgebied met een bestuur; een natie is een groep mensen met een gedeelde culturele identiteit',
                    'Een staat heeft geen grondgebied en een natie wel',
                    'Een natie heeft altijd een eigen munt en een staat niet',
                    'Er is geen enkel inhoudelijk verschil tussen een staat en een natie'
                ],
                'antwoord': 0,
                'uitleg': 'Een staat is een politiek-juridische eenheid; een natie (of volk) is een sociaal-culturele groep.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat kenmerkt een binnenlands gewapend conflict (burgeroorlog)?',
                'opties': [
                    'Twee buitenlandse mogendheden vechten op volle zee',
                    'De strijd vindt plaats binnen de grenzen van één land tussen de regering en opstandelingen of tussen groepen onderling',
                    'Het conflict wordt uitsluitend via diplomatieke nota s uitgevochten',
                    'Er vechten alleen huursoldaten uit buurlanden zonder lokale inmenging'
                ],
                'antwoord': 1,
                'uitleg': 'Een burgeroorlog of intern conflict woedt tussen partijen binnen dezelfde staatsgrenzen.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Tot hoever reiken de officiële territoriale wateren van een kuststaat volgens het VN-Zeerechtverdrag?',
                'opties': [
                    'Slechts 1 kilometer uit de kust',
                    'Precies 500 meter vanaf het strand',
                    'Tot maximaal 12 zeemijl (ongeveer 22 kilometer) uit de kustlijn',
                    'Tot aan de overkant van de oceaan'
                ],
                'antwoord': 2,
                'uitleg': 'Territoriale wateren maken deel uit van het soevereine staatsgebied en reiken tot 12 zeemijl.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welke rol spelen desinformatie en nepnieuws in moderne hybride oorlogen?',
                'opties': [
                    'Ze zorgen voor vrede tussen strijdende partijen',
                    'Ze worden alleen gebruikt om computerspellen te testen',
                    'Ze vervangen alle wapens en legers volledig',
                    'Ze zaaien doelbewust verdeeldheid, verwarring en wantrouwen onder de burgerbevolking van de tegenstander'
                ],
                'antwoord': 3,
                'uitleg': 'Informatieoorlogvoering via sociale media ondermijnt het maatschappelijk vertrouwen en de weerbaarheid van een land.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Welk internationaal orgaan kan als enige bindende resoluties aannemen voor militair ingrijpen tegen een agressor?',
                'opties': [
                    'De Veiligheidsraad van de Verenigde Naties',
                    'Het Europees Parlement',
                    'Het Rode Kruis',
                    'De Wereldhandelsorganisatie'
                ],
                'antwoord': 0,
                'uitleg': 'Alleen de VN-Veiligheidsraad heeft het wettelijke mandaat om militair dwangoptreden goed te keuren.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn multinationale staten vaak gevoeliger voor interne conflicten dan homogene natiestaten?',
                'opties': [
                    'Omdat multinationale staten geen hoofdstad hebben',
                    'Omdat verschillende etnische groepen kunnen strijden om politieke macht, grondgebied of gelijke rechten',
                    'Omdat alle inwoners verplicht zijn dezelfde godsdienst aan te hangen',
                    'Omdat multinationale staten altijd armer zijn'
                ],
                'antwoord': 1,
                'uitleg': 'Tegenstellingen tussen rivaliserende bevolkingsgroepen kunnen door politieke leiders worden aangewakkerd tot geweld.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat gebeurt er bij cyberoorlogsvoering tussen staten?',
                'opties': [
                    'Militairen vechten met laserpistolen in de ruimte',
                    'Soldaten sturen elkaar handgeschreven brieven',
                    'Computersystemen van overheden, banken, ziekenhuizen of energienetten worden digitaal aangevallen en platgelegd',
                    'Alle internetkabels worden met scharen doorgeknipt'
                ],
                'antwoord': 2,
                'uitleg': 'Digitale aanvallen ontregelen vitale infrastructuur zonder dat er een conventioneel schot hoeft te vallen.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welke omschrijving past het best bij soevereiniteit van een staat?',
                'opties': [
                    'De verplichting om altijd naar buurlanden te luisteren',
                    'Het bezit van een koninklijke familie',
                    'Het recht om geen belastingen te heffen',
                    'Het exclusieve recht om binnen het eigen territorium zelf wetten te maken en het hoogste gezag uit te oefenen'
                ],
                'antwoord': 3,
                'uitleg': 'Soevereiniteit betekent dat een staat intern en extern onafhankelijk en zelfbeschikkend is.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is een bekend voorbeeld van een groot volk zonder eigen officiële staat?',
                'opties': [
                    'De Koerden in het Midden-Oosten',
                    'De Japanners in Azië',
                    'De IJslanders in Noord-Europa',
                    'De Fransen in West-Europa'
                ],
                'antwoord': 0,
                'uitleg': 'De circa 35 miljoen Koerden wonen verspreid over Turkije, Syrië, Irak en Iran en bezitten geen soevereine staat.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wanneer spreken onderzoekers van een interstate conflict?',
                'opties': [
                    'Wanneer twee dorpen in dezelfde gemeente ruziën over een voetbalveld',
                    'Wanneer twee of meer soevereine nationale staten gewapend met elkaar in oorlog zijn',
                    'Wanneer een land ruzie heeft met een multinational',
                    'Wanneer er alleen via de radio ruzie wordt gemaakt'
                ],
                'antwoord': 1,
                'uitleg': 'Interstate betekent letterlijk tussen staten: een traditionele oorlog tussen twee landen.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'In welke regio ter wereld was het aantal gewapende conflicten en slachtoffers de afgelopen decennia gemiddeld zeer hoog?',
                'opties': [
                    'In West-Europa en Scandinavië',
                    'Op Antarctica en Groenland',
                    'In sub-Sahara Afrika en het Midden-Oosten',
                    'In Australië en Nieuw-Zeeland'
                ],
                'antwoord': 2,
                'uitleg': 'Kwetsbare staten, armoede en grondstoffenstrijd concentreren gewapende conflicten vooral in sub-Sahara Afrika en het Midden-Oosten.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom werd in 1945 het Handvest van de Verenigde Naties opgesteld?',
                'opties': [
                    'Om het vliegen met vliegtuigen te verbieden',
                    'Om alle landen van de wereld samen te voegen tot één superstaat',
                    'Om het bezit van geld af te schaffen',
                    'Om toekomstige generaties te behoeden voor de gesel van oorlog en conflicten vreedzaam op te lossen'
                ],
                'antwoord': 3,
                'uitleg': 'Na de gruwelen van de Tweede Wereldoorlog wilden de geallieerden een internationaal systeem bouwen om vrede te waarborgen.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'Volgens het Handvest van de Verenigde Naties mag een land militair geweld gebruiken als het zichzelf moet verdedigen tegen een aanval.',
                'antwoord': True,
                'uitleg': 'Waar: Artikel 51 van het VN-Handvest erkent het inherente recht op individuele of collectieve zelfverdediging.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'Als er in een gewapende strijd minder dan 100 doden vallen, is er volgens internationale definities nooit sprake van een gewapend conflict.',
                'antwoord': False,
                'uitleg': 'Onwaar: de algemeen aanvaarde grens voor een gewapend conflict ligt op minimaal 25 doden in een kalenderjaar.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'Het territorium van een land bestaat uitsluitend uit het landoppervlak en nooit uit het luchtruim erboven.',
                'antwoord': False,
                'uitleg': 'Onwaar: het luchtruim boven het grondgebied valt integraal onder de soevereiniteit van de staat.'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'Buitenlandse inmenging kan een interne burgeroorlog veranderen in een geïnternationaliseerd conflict.',
                'antwoord': True,
                'uitleg': 'Waar: wanneer buurlanden of grootmachten troepen of wapens sturen, raakt het conflict geïnternationaliseerd.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'Een land waarvan de staatsgrenzen grotendeels samenvallen met het leefgebied van één enkel volk, heet een ....',
                'antwoord': 'natiestaat',
                'uitleg': 'Een natiestaat verenigt één overheersend volk binnen duidelijke politieke grenzen.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'De hoogste en onafhankelijke macht van een staat over zijn eigen grondgebied en bevolking, noemen we ....',
                'antwoord': 'soevereiniteit',
                'uitleg': 'Soevereiniteit betekent dat een staat niet ondergeschikt is aan het gezag van een andere macht.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem het minimumaantal dodelijke slachtoffers in een jaar dat vereist is om formeel te spreken van een gewapend conflict.',
                'sleutelwoorden': [
                    '25/vijfentwintig'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Er moeten ten minste 25 dodelijke slachtoffers vallen in één kalenderjaar.',
                'uitleg': 'De internationale Uppsala-norm hanteert 25 slachtoffers per jaar als ondergrens.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Geef een voorbeeld van een niet-militair middel dat gebruikt kan worden bij moderne hybride oorlogsvoering.',
                'sleutelwoorden': [
                    'cyber/desinformatie/propaganda/sanctie/nepnieuws/hacken'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Cyberaanvallen, desinformatiecampagnes of economische sancties zijn vormen van hybride oorlogsvoering.',
                'uitleg': 'Hybride oorlogsvoering omvat digitale ontwrichting, desinformatie en economische sabotage.'
            }
        ]
    },
    {
        'file': 'examen_22.js',
        'id': 'ex-h3-ak-22',
        'hoofdstuk': 5,
        'paragraaf': '5.2',
        'titel': 'Proeftoets 22 — §5.2 Oorzaken van gewapende conflicten',
        'icoon': '⚖️',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Waarom leidt de aanwezigheid van waardevolle delfstoffen zoals diamant of coltan in kwetsbare landen vaak tot oplaaiend geweld?',
                'opties': [
                    'Omdat gewapende milities en corrupte elites vechten om de controle over de mijnen om wapens en privémachten te financieren',
                    'Omdat de delfstoffen ontploffen zodra ze worden aangeraakt',
                    'Omdat buitenlandse toeristen alle mijnen bezoeken',
                    'Omdat mijnbouw verboden is door de natuurwetten'
                ],
                'antwoord': 0,
                'uitleg': 'Delfstoffen vormen een lucratieve inkomstenbron voor krijgsheren en milities om hun oorlogskas te vullen.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat gebeurde er tijdens de Koloniale Conferentie van Berlijn (1884-1885)?',
                'opties': [
                    'Alle Afrikaanse volkeren kregen hun eigen onafhankelijke staat',
                    'Europese mogendheden verdeelden het Afrikaanse continent onderling met willekeurige grenzen zonder de lokale volkeren te raadplegen',
                    'Er werd een verbod op de stoomtrein afgesproken',
                    'Afrikaanse koningen sloten vrede met Europa'
                ],
                'antwoord': 1,
                'uitleg': 'In Berlijn verdeelden Europese koloniale machten Afrika met potlood en liniaal, wat de kiem legde voor latere grensconflicten.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke demografische factor vergroot het risico op politieke instabiliteit en geweld in ontwikkelingslanden?',
                'opties': [
                    'Een zeer hoog percentage bejaarden in verzorgingstehuizen',
                    'Een krimpende bevolking zonder kinderen',
                    'Een grote jeugdbulge: een hoog percentage kansarme jongeren zonder werk of toekomstperspectief',
                    'Een gelijkmatige leeftijdsopbouw in alle provincies'
                ],
                'antwoord': 2,
                'uitleg': 'Een jeugdbulge gecombineerd met massale werkloosheid maakt jongeren vatbaar voor rekrutering door extremisten.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste kenmerk van een fragile state (kwetsbare staat)?',
                'opties': [
                    'Het land heeft te veel ziekenhuizen gebouwd',
                    'Het land is omringd door vier oceanen',
                    'De staat bezit de grootste goudvoorraad ter wereld',
                    'De overheid heeft geen monopolie op geweld en slaagt er niet in de basisveiligheid en rechtshandhaving te waarborgen'
                ],
                'antwoord': 3,
                'uitleg': 'In een falende staat ontbreekt effectief overheidsgezag en hebben warlords, criminele kartels of rebellen vrij spel.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Waarom noemen veiligheidsexperts klimaatverandering een threat multiplier?',
                'opties': [
                    'Omdat klimaatverandering bestaande spanningen rond drinkwater, landbouwgrond en armoede versterkt en versnelt',
                    'Omdat het weer altijd verbetert na een vredesverdrag',
                    'Omdat soldaten sneller kunnen marcheren bij regen',
                    'Omdat wapens beter functioneren bij hitte'
                ],
                'antwoord': 0,
                'uitleg': 'Klimaatstress verhoogt de druk op schaarse natuurlijke hulpbronnen, waardoor latent sluimerende conflicten ontbranden.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat speelde een doorslaggevende rol in de aanloop naar de Rwandese genocide in 1994?',
                'opties': [
                    'Een ruzie over de invoer van computers',
                    'Decennia van etnische haat en discriminatie die gevoed werden door koloniale bevoordeling van Tutsi s boven Hutu s',
                    'Een conflict over aardolieboringen in het Tanganyikameer',
                    'Een plotselinge vulkaanuitbarsting die de hoofdstad verwoestte'
                ],
                'antwoord': 1,
                'uitleg': 'Belgische kolonisatoren deelden de bevolking in etnische categorieën in en bevoordeelden de Tutsi-elite, wat diepe rancune zaaide.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke grondstof staat centraal in veel gewapende conflicten in het Midden-Oosten en de Kaspische Zee-regio?',
                'opties': [
                    'Kiezelzand',
                    'Bakstenen',
                    'Aardolie en aardgas',
                    'Brandhout'
                ],
                'antwoord': 2,
                'uitleg': 'Controle over gigantische olie- en gasvelden en pijpleidingroutes vormt een dominante geopolitieke inzet.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom vechten nomadische herders (zoals de Fulani) en sedentaire boeren in de Afrikaanse Sahel steeds vaker met elkaar?',
                'opties': [
                    'Omdat ze verschillende computersystemen gebruiken',
                    'Omdat de VN hen dwingt tot gevechten',
                    'Omdat ze ruzie hebben over sportuitslagen',
                    'Omdat door oprukkende verwoestijning en droogte vruchtbare graas- en landbouwgronden en waterputten extreem schaars zijn geworden'
                ],
                'antwoord': 3,
                'uitleg': 'Klimaatdruk dwingt herders zuidwaarts te trekken over de akkers van boeren, wat leidt tot bloedige botsingen.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is het gevaar wanneer een dictatoriale leider een minderheidsgroep als zondebok aanwijst voor economische crises?',
                'opties': [
                    'Dit kan leiden tot ontmenselijking, haatzaaien en gewelddadige vervolging van de minderheid',
                    'De economie herstelt zich hierdoor onmiddellijk',
                    'Alle minderheden verlaten spontaan de aarde',
                    'Er ontstaat vanzelf een stabiele democratie'
                ],
                'antwoord': 0,
                'uitleg': 'Het demoniseren van bevolkingsgroepen is een beproefde tactiek van extremisten om macht te consolideren.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is het begrip grondstoffenvloek (paradox of plenty)?',
                'opties': [
                    'Dat grondstoffen altijd verdwijnen zodra een mijnwerker ze aanraakt',
                    'Dat landen met een overvloed aan bodemschatten gemiddeld trager groeien, meer corruptie kennen en vaker burgeroorlogen beleven',
                    'Dat alle delfstoffen in Afrika van plastic blijken te zijn',
                    'Dat grondstoffen alleen gevonden worden in vredige landen'
                ],
                'antwoord': 1,
                'uitleg': 'Delfstoffenrijkdom trekt corrupte elites en rebellengroepen aan die strijden om de opbrengsten.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke rol spelen illegale wapenleveranties bij het in stand houden van gewapende conflicten?',
                'opties': [
                    'Wapenleveranties zorgen ervoor dat beide partijen snel stoppen met vechten',
                    'Wapens worden altijd gratis door ziekenhuizen verstrekt',
                    'Ze zorgen ervoor dat strijdende fracties de gevechten jarenlang kunnen blijven voortzetten en escaleren',
                    'Wapens hebben geen enkele invloed op het verloop van een oorlog'
                ],
                'antwoord': 2,
                'uitleg': 'De toevoer van lichte wapens (zoals Kalasjnikovs) houdt geweldscycli decennialang draaiende.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn grensconflicten tussen staten vaak zo moeilijk diplomatiek op te lossen?',
                'opties': [
                    'Omdat grenzen niet op landkaarten mogen worden getekend',
                    'Omdat diplomaten niet met elkaar mogen praten',
                    'Omdat grenzen uitsluitend door de natuur worden bepaald',
                    'Omdat staten hun soevereiniteit en controle over territorium en grondstoffen beschouwen als ononderhandelbare nationale belangen'
                ],
                'antwoord': 3,
                'uitleg': 'Territoriale claims raken aan nationale trots, staatssoevereiniteit en strategische economische reserves.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'In veel Afrikaanse landen lopen landsgrenzen dwars door de leefgebieden van dezelfde etnische groepen.',
                'antwoord': True,
                'uitleg': 'Waar: koloniale grenzen hielden geen rekening met stamgebieden, waardoor volkeren versnipperd raakten.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'Een land met enorme olievoorraden verandert automatisch in een welvarende en vreedzame democratie.',
                'antwoord': False,
                'uitleg': 'Onwaar: de grondstoffenvloek zorgt er vaak voor dat olie leidt tot corruptie, autoritair bestuur en strijd om de opbrengsten.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'Een jeugdbulge leidt in alle omstandigheden direct tot oorlog, ongeacht de beschikbaarheid van banen en scholing.',
                'antwoord': False,
                'uitleg': 'Onwaar: met goed onderwijs en een bloeiende arbeidsmarkt kan een jonge bevolking juist zorgen voor een economische bloei.'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'Klimaatverandering kan bestaande spanningen over schaarse grondstoffen doen escaleren.',
                'antwoord': True,
                'uitleg': 'Waar: toenemende droogte en voedselschaarste functioneren als dreigingsversterker voor gewapende conflicten.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'De term voor de situatie waarin een land rijk is aan delfstoffen maar daardoor juist ten prooi valt aan corruptie en oorlog, heet de grondstoffen....',
                'antwoord': 'vloek',
                'uitleg': 'De grondstoffenvloek (resource curse) verklaart waarom delfstoffenrijke staten vaak instabiel zijn.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'Een land waar de centrale overheid niet meer in staat is het geweldsmonopolie te handhaven, noemen we een .... state.',
                'antwoord': 'fragile',
                'uitleg': 'Een fragile state (falende staat) heeft de controle over veiligheid en wetshandhaving verloren.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem het Afrikaanse land waar in 1994 een beruchte volkenmoord plaatsvond tussen de Hutu-meerderheid en de Tutsi-minderheid.',
                'sleutelwoorden': [
                    'Rwanda'
                ],
                'minTreffers': 1,
                'modelantwoord': 'In Rwanda vond in 1994 de genocide plaats.',
                'uitleg': 'De genocide in Rwanda kostte aan circa 800.000 mensen het leven.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Leg uit waarom klimaatopwarming in defensiekringen wordt getypeerd als een dreigingsversterker.',
                'sleutelwoorden': [
                    'droogte/schaarste/water/voedsel/versterkt/spanning/conflicten'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Klimaatverandering verergert bestaande schaarste aan water en voedsel en wakkert daarmee spanningen en conflicten aan.',
                'uitleg': 'Klimaatstress vergroot de concurrentie om schaarse basisbehoeften.'
            }
        ]
    },
    {
        'file': 'examen_23.js',
        'id': 'ex-h3-ak-23',
        'hoofdstuk': 5,
        'paragraaf': '5.3',
        'titel': 'Proeftoets 23 — §5.3 Gevolgen van gewapende conflicten',
        'icoon': '🩹',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is een van de belangrijkste bepalingen uit de Verdragen van Genève over het beschermen van burgers?',
                'opties': [
                    'Burgers en medische instellingen mogen nooit het doelwit zijn van militaire aanvallen',
                    'Burgers moeten verplicht meevochten aan het front',
                    'Alle burgerwoningen mogen te allen tijde worden gevorderd en gesloopt',
                    'Burgers hebben geen enkel recht tijdens een oorlog'
                ],
                'antwoord': 0,
                'uitleg': 'Het humanitair oorlogsrecht eist dat strijdende partijen te allen tijde onderscheid maken tussen strijders en burgers.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is het belangrijkste verschil tussen een internationale vluchteling en een ontheemde?',
                'opties': [
                    'Vluchtelingen vluchten voor het weer; ontheemden voor soldaten',
                    'Een vluchteling is een internationale staatsgrens overgestoken; een ontheemde is binnen de eigen landsgrenzen gevlucht',
                    'Ontheemden hebben altijd een eigen woning',
                    'Vluchtelingen mogen geen medische hulp ontvangen'
                ],
                'antwoord': 1,
                'uitleg': 'Ontheemden (internally displaced persons) verblijven in eigen land en genieten daardoor minder internationale juridische bescherming.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke VN-organisatie is specifiek belast met de bescherming en opvang van vluchtelingen wereldwijd?',
                'opties': [
                    'De UNESCO',
                    'De Wereldbank',
                    'De UNHCR (Hoge Commissaris voor de Vluchtelingen)',
                    'Het Internationaal Monetair Fonds'
                ],
                'antwoord': 2,
                'uitleg': 'De UNHCR coördineert internationale hulpverlening en opvangkampen voor vluchtelingen.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welke juridische kwalificatie heeft het doelbewust uithongeren van een burgerbevolking tijdens een gewapende strijd?',
                'opties': [
                    'Een legale economische maatregel',
                    'Een toelaatbare militaire list',
                    'Een binnenlands bestuursbesluit',
                    'Een ernstige oorlogsmisdaad onder het internationaal recht'
                ],
                'antwoord': 3,
                'uitleg': 'Het uithongeren van burgers als oorlogsmethode is een schending van de Geneefse Conventies en het Statuut van Rome.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is het primaire doel van het Internationaal Strafhof (ICC) in Den Haag?',
                'opties': [
                    'Individuen berechten die verdacht worden van genocide, misdaden tegen de menselijkheid en oorlogsmisdaden',
                    'Bekeuringen uitdelen voor te hard varen op de Noordzee',
                    'Verkiezingsuitslagen van Europese landen bepalen',
                    'Wapenleveringen aan rebellen goedkeuren'
                ],
                'antwoord': 0,
                'uitleg': 'Het ICC is het permanente wereldwijde hof voor de berechting van de ernstigste internationale misdrijven.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is een kenmerkend fysiek gevolg van grootschalige oorlogen voor steden en dorpen?',
                'opties': [
                    'Alle gebouwen worden spontaan tien meter hoger',
                    'De totale verwoesting van basisinfrastructuur zoals waterleidingen, elektriciteitsnetten, bruggen en scholen',
                    'Er ontstaan vanzelf nieuwe bossen in de straten',
                    'Alle wegen veranderen in kanalen'
                ],
                'antwoord': 1,
                'uitleg': 'Het vernietigen van vitale nutsvoorzieningen stort de samenleving in een diepe humanitaire crisis.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn kinderen in conflictgebieden vaak extra kwetsbaar?',
                'opties': [
                    'Omdat kinderen geen honger kunnen voelen',
                    'Omdat kinderen verplicht zijn leiding te geven aan legers',
                    'Omdat ze te maken krijgen met trauma s, ondervoeding, gebrek aan scholing en het gevaar om gerekruteerd te worden als kindsoldaat',
                    'Omdat kinderen niet kunnen verhuizen'
                ],
                'antwoord': 2,
                'uitleg': 'Oorlog ontneemt kinderen onderwijs en veiligheid en beschadigt hun fysieke en geestelijke ontwikkeling langdurig.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat gebeurde er tijdens de genocide in Srebrenica in juli 1995?',
                'opties': [
                    'Er werd een vredesfestival georganiseerd',
                    'De stad werd uitgeroepen tot hoofdstad van Bosnië',
                    'Alle wapens werden ingeleverd bij de kerk',
                    'Bosnisch-Servische troepen vermoordden meer dan 8.000 moslimmannen en -jongens'
                ],
                'antwoord': 3,
                'uitleg': 'Het Internationaal Gerechtshof en het Joegoslavië-tribunaal oordeelden dat de slachting in Srebrenica genocide was.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is een humanitaire corridor in een oorlogsgebied?',
                'opties': [
                    'Een tijdelijk gedemilitariseerde zone of route waarlangs burgers veilig kunnen vluchten en hulpgoederen kunnen worden aangevoerd',
                    'Een ondergrondse schuilkelder voor generaals',
                    'Een museum over oude veldslagen',
                    'Een spoorlijn die uitsluitend voor munitie bestemd is'
                ],
                'antwoord': 0,
                'uitleg': 'Humanitaire corridors worden overeengekomen om burgers uit belegerde steden te evacueren en noodhulp te brengen.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is het psychologische gevolg van aanhoudend oorlogsgeweld op overlevenden?',
                'opties': [
                    'Mensen worden immuun voor alle ziektes',
                    'Veel mensen ontwikkelen een posttraumatische stressstoornis (PTSS), chronische angst en depressies',
                    'Overlevenden vergeten onmiddellijk wat er gebeurd is',
                    'Iedereen besluit spontaan soldaat te worden'
                ],
                'antwoord': 1,
                'uitleg': 'Onveiligheid, bombardementen en verlies van familieleden veroorzaken diepe psychologische trauma s over meerdere generaties.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat houdt de zogeheten tactiek van etnische zuivering in?',
                'opties': [
                    'Het schoonmaken van monumenten na een optocht',
                    'Het verplichten van alle inwoners om dezelfde kleding te dragen',
                    'Het met bruut geweld, moord en terreur verdrijven van een bepaalde etnische groep om een gebied homogeen te maken',
                    'Het geven van taallessen aan minderheden'
                ],
                'antwoord': 2,
                'uitleg': 'Etnische zuivering beoogt een gebied vrij te maken van een specifieke bevolkingsgroep door verdrijving en terreur.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welke internationale conventie verbiedt het gebruik van landmijnen die na de strijd nog jarenlang burgers verminken?',
                'opties': [
                    'Het Verdrag van Schengen',
                    'Het Kyoto-protocol',
                    'Het Verdrag van Maastricht',
                    'Het Verdrag van Ottawa (Mijnenconventie)'
                ],
                'antwoord': 3,
                'uitleg': 'Het Ottawa-verdrag uit 1997 verbiedt de inzet, productie en opslag van antipersoneelsmijnen.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'In moderne gewapende conflicten vallen veruit de meeste slachtoffers onder de burgerbevolking.',
                'antwoord': True,
                'uitleg': 'Waar: naar schatting 80 tot 90 procent van alle oorlogsslachtoffers tegenwoordig betreft burgers.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'Het Internationaal Strafhof in Den Haag kan alleen staten als geheel veroordelen en nooit individuele leiders of generaals.',
                'antwoord': False,
                'uitleg': 'Onwaar: het ICC berecht juist individuele personen die verdacht worden van oorlogsmisdaden en genocide.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'Het bombarderen van scholen en ziekenhuizen is volgens het oorlogsrecht toegestaan zolang het overdag gebeurt.',
                'antwoord': False,
                'uitleg': 'Onwaar: burgerdoelen en medische voorzieningen genieten absolute bescherming onder het humanitair oorlogsrecht.'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'Een persoon die binnen de grenzen van zijn eigen land vlucht voor oorlogsgeweld, heet een ontheemde.',
                'antwoord': True,
                'uitleg': 'Waar: ontheemden (internally displaced persons) steken geen officiële landsgrens over.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'De internationale wetten die burgers en krijgsgevangenen beschermen tijdens een oorlog, staan bekend als het oorlogs....',
                'antwoord': 'recht',
                'uitleg': 'Het internationaal humanitair oorlogsrecht reguleert wat wel en niet geoorloofd is tijdens gewapende strijd.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'Het permanente gerechtshof in Den Haag dat individuen berecht voor genocide en oorlogsmisdaden, heet het Internationaal ....',
                'antwoord': 'Strafhof',
                'uitleg': 'Het Internationaal Strafhof (ICC) zetelt in Den Haag.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem de Zwitserse stad waar de beroemde verdragen inzake het humanitair oorlogsrecht zijn gesloten.',
                'sleutelwoorden': [
                    'Geneve/Genève'
                ],
                'minTreffers': 1,
                'modelantwoord': 'De Verdragen van Genève vormen de kern van het oorlogsrecht.',
                'uitleg': 'In Genève werden de vier verdragen en aanvullende protocollen ondertekend.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Wat is het formele geografische onderscheid tussen een vluchteling en een ontheemde?',
                'sleutelwoorden': [
                    'grens/landsgrens/buitenland/binnenland'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Een vluchteling is een internationale landsgrens overgestoken, terwijl een ontheemde in het eigen land blijft.',
                'uitleg': 'Het oversteken van een staatsgrens bepaalt het juridische verschil tussen beiden.'
            }
        ]
    },
    {
        'file': 'examen_24.js',
        'id': 'ex-h3-ak-24',
        'hoofdstuk': 5,
        'paragraaf': '5.4',
        'titel': 'Proeftoets 24 — §5.4 Hoe rustig is Europa?',
        'icoon': '🛡️',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn er binnen de Europese Unie sinds haar oprichting geen gewapende conflicten meer uitgebroken tussen lidstaten?',
                'opties': [
                    'Omdat hechte economische verwevenheid, democratische rechtsstelsels en intensief diplomatiek overleg oorlog tussen lidstaten ondenkbaar hebben gemaakt',
                    'Omdat de EU alle legers van haar lidstaten heeft ontbonden',
                    'Omdat lidstaten van de EU geen wapens mogen bezitten',
                    'Omdat alle Europeanen precies dezelfde moedertaal spreken'
                ],
                'antwoord': 0,
                'uitleg': 'Europese integratie transformeerde aartsvijanden (zoals Duitsland en Frankrijk) in hechte democratische partners.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat was een belangrijke aanleiding voor het uiteenvallen van Joegoslavië in 1991?',
                'opties': [
                    'Een geschil over de invoering van de euro',
                    'Het opkomend nationalisme van leiders in de deelrepublieken na de dood van dictator Tito en de onafhankelijkheidsverklaringen van Slovenië en Kroatië',
                    'Een inval door buurland Oostenrijk',
                    'Een besluit van de Europese Unie om het land op te heffen'
                ],
                'antwoord': 1,
                'uitleg': 'Na het wegvallen van het communistische gezag laaiden etnisch-nationalistische sentimenten fel op.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welk verdrag maakte in 1995 een einde aan de bloedige burgeroorlog in Bosnië-Herzegovina?',
                'opties': [
                    'Het Verdrag van Versailles',
                    'Het Akkoord van Schengen',
                    'Het Verdrag van Dayton',
                    'Het Verdrag van Rome'
                ],
                'antwoord': 2,
                'uitleg': 'Het Dayton-akkoord verdeelde Bosnië-Herzegovina in twee entiteiten onder een overkoepelend bestuur.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom streeft een deel van de Catalanen naar afscheiding van Spanje (separatisme)?',
                'opties': [
                    'Omdat Catalonië een eigen leger wil opbouwen om Frankrijk aan te vallen',
                    'Omdat Catalonië een monarchie wil stichten',
                    'Omdat de Spaanse koning de taal Catalaans heeft verboden',
                    'Vanwege een sterke eigen culturele en taalkundige identiteit en de wens zelf over belastinginkomsten en bestuur te beschikken'
                ],
                'antwoord': 3,
                'uitleg': 'Economische grieven en een sterk nationaal zelfbewustzijn voeden het Catalaanse onafhankelijkheidsstreven.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat is de voornaamste geopolitieke reden waarom Rusland zich fel verzette tegen een mogelijk NAVO-lidmaatschap van Oekraïne?',
                'opties': [
                    'Rusland beschouwt Oekraïne als een strategische bufferstaat en traditionele invloedssfeer tussen Rusland en het Westen',
                    'Rusland wilde dat Oekraïne lid werd van de Europese Unie in plaats van de NAVO',
                    'Rusland wilde alle graanvelden in Oekraïne asfalteren',
                    'Rusland had geen enkele interesse in Oekraïne'
                ],
                'antwoord': 0,
                'uitleg': 'Moskou vreesde dat een westers georiënteerd Oekraïne de strategische veiligheid van Rusland zou ondermijnen.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is het verschil tussen het geografische werelddeel Europa en de politieke organisatie Europese Unie (EU)?',
                'opties': [
                    'Europa is kleiner dan de Europese Unie',
                    'Europa is het gehele continent (tot aan de Oeral); de EU is een politiek en economisch samenwerkingsverband van 27 lidstaten',
                    'De EU omvat ook alle landen in Noord-Afrika',
                    'Er is geen enkel verschil tussen Europa en de EU'
                ],
                'antwoord': 1,
                'uitleg': 'Niet alle Europese landen (zoals het VK, Noorwegen, Zwitserland, Oekraïne en Servië) zijn lid van de EU.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke autonome regio in het noorden van Spanje kende in de 20e eeuw gewelddadig terrorisme door de afscheidingsbeweging ETA?',
                'opties': [
                    'Andalusië',
                    'De Canarische Eilanden',
                    'Baskenland',
                    'Castilië'
                ],
                'antwoord': 2,
                'uitleg': 'De Baskische terreurbeweging ETA voerde decennialang een gewelddadige strijd voordat zij de wapens neerlegde.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Welke twee landen in Noord-Europa braken in 2022 met hun eeuwenlange neutraliteitspolitiek door lid te worden van de NAVO?',
                'opties': [
                    'Spanje en Italië',
                    'Ierland en Oostenrijk',
                    'Denemarken en Noorwegen',
                    'Finland en Zweden'
                ],
                'antwoord': 3,
                'uitleg': 'De Russische inval in Oekraïne deed de publieke opinie in Finland en Zweden massaal omslaan ten gunste van het NAVO-bondgenootschap.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men onder regionalisme binnen een Europese staat?',
                'opties': [
                    'Het streven van een regio naar meer behoud van de eigen identiteit, cultuur en zelfbestuur binnen de bestaande staat',
                    'Het opheffen van alle provincies in een land',
                    'Het verhuizen van alle regeringsgebouwen naar het platteland',
                    'Het verplicht stellen van één nationale dans'
                ],
                'antwoord': 0,
                'uitleg': 'Regionalisme benadrukt de eigenheid van een streek zonder noodzakelijk volledige onafhankelijkheid te eisen.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is een bufferstaat in de internationale geopolitiek?',
                'opties': [
                    'Een staat die uitsluitend treinen produceert',
                    'Een kleiner of neutraal land dat tussen twee rivaliserende grootmachten ligt en direct militair contact voorkomt',
                    'Een land dat geen grenzen met andere landen deelt',
                    'Een land dat geheel onder water ligt'
                ],
                'antwoord': 1,
                'uitleg': 'Historisch dienden landen als België, Polen of Oekraïne vaak als geopolitieke buffers tussen grootmachten.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat gebeurde er in 2014 op het schiereiland de Krim in Oekraïne?',
                'opties': [
                    'De Krim werd een zelfstandig lid van de Europese Unie',
                    'De bevolking trad toe tot de Verenigde Naties',
                    'Rusland bezette het schiereiland militair en annexeerde het in strijd met het internationaal recht',
                    'De Krim werd verkocht aan Turkije'
                ],
                'antwoord': 2,
                'uitleg': 'De illegale annexatie van de Krim in 2014 markeerde het begin van het militair conflict tussen Rusland en Oekraïne.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom zijn de criteria van Kopenhagen van belang voor landen die lid willen worden van de Europese Unie?',
                'opties': [
                    'Ze bepalen welke talen er op straat gesproken mogen worden',
                    'Ze verplichten een land om windmolens langs de kust te bouwen',
                    'Ze bepalen de maximale hoogte van gebouwen in de hoofdstad',
                    'Ze stellen strikte eisen aan een stabiele democratie, de rechtsstaat, mensenrechten en een functionerende markteconomie'
                ],
                'antwoord': 3,
                'uitleg': 'Kandidaat-lidstaten moeten aantoonbaar voldoen aan de Kopenhagen-criteria voor toetreding.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'Het Verdrag van Dayton maakte in 1995 een einde aan de oorlog in Bosnië-Herzegovina.',
                'antwoord': True,
                'uitleg': 'Waar: onder leiding van de VS werd in Dayton (Ohio) een vredesakkoord bereikt.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'Alle soevereine staten op het Europese continent zijn volwaardig lid van de Europese Unie.',
                'antwoord': False,
                'uitleg': 'Onwaar: landen als Noorwegen, Zwitserland, IJsland en het Verenigd Koninkrijk zijn geen lid van de EU.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'In Schotland heeft de bevolking in een referendum besloten om het Verenigd Koninkrijk met onmiddellijke ingang met geweld te verlaten.',
                'antwoord': False,
                'uitleg': 'Onwaar: in het vreedzame referendum van 2014 stemde een meerderheid van de Schotten (55%) tegen onafhankelijkheid.'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'Finland deelt een ruim 1.300 kilometer lange grens met Rusland.',
                'antwoord': True,
                'uitleg': 'Waar: door de toetreding van Finland tot de NAVO werd de directe NAVO-grens met Rusland meer dan verdubbeld.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'Het streven van een bevolkingsgroep om zich geheel af te scheiden van een staat en een eigen land te vormen, heet ....',
                'antwoord': 'separatisme',
                'uitleg': 'Separatisme richt zich op politieke en geografische afsplitsing.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'Zelfbestuur van een regio binnen de grenzen van een bestaande staat, noemen we ....',
                'antwoord': 'autonomie',
                'uitleg': 'Autonomie geeft een regio eigen wetgevende en bestuurlijke bevoegdheden binnen het staatsverband.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem de welvarende regio in het noordoosten van Spanje waar al jarenlang een sterke onafhankelijkheidsbeweging actief is.',
                'sleutelwoorden': [
                    'Catalonie/Catalonië'
                ],
                'minTreffers': 1,
                'modelantwoord': 'In Catalonië is een grote onafhankelijkheidsbeweging actief.',
                'uitleg': 'Catalonië streeft naar een zelfstandige Catalaanse republiek.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Geef een reden waarom de Europese integratie na 1945 wordt beschouwd als een groot stabiliteitsproject.',
                'sleutelwoorden': [
                    'oorlog/samenwerking/economie/handel/vrede/overleg'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Door hechte economische samenwerking en overleg is er tussen de lidstaten al decennialang geen oorlog meer geweest.',
                'uitleg': 'Economische integratie maakte gewapende strijd tussen aartsvijanden onrendabel en onmogelijk.'
            }
        ]
    },
    {
        'file': 'examen_25.js',
        'id': 'ex-h3-ak-25',
        'hoofdstuk': 5,
        'paragraaf': '5.5',
        'titel': 'Proeftoets 25 — §5.5 Nederland: oorlog en vrede',
        'icoon': '🕊️',
        'duurMin': 30,
        'vragen': [
            # MC 1: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Tegen welk machtig rijk vocht Nederland tijdens de Tachtigjarige Oorlog (1568-1648) voor zijn godsdienstvrijheid en onafhankelijkheid?',
                'opties': [
                    'Het Spaanse Rijk onder leiding van koning Filips II',
                    'Het Britse Rijk',
                    'Het Russische Tsarenrijk',
                    'Het Ottomaanse Rijk'
                ],
                'antwoord': 0,
                'uitleg': 'De Nederlandse Opstand richtte zich tegen het bewind van de Spaanse Habsburgers.'
            },
            # MC 2: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat gebeurde er tijdens de zogeheten politionele acties van Nederland in Indonesië (1947-1949)?',
                'opties': [
                    'De Nederlandse politie hielp bij verkeerscontroles in Jakarta',
                    'Het Nederlandse leger voerde grootschalige militaire operaties uit om de Indonesische onafhankelijkheidsstrijd met geweld neer te slaan',
                    'Nederland droeg de soevereiniteit zonder gevechten vreedzaam over',
                    'Indonesië werd een provincie van Nederland'
                ],
                'antwoord': 1,
                'uitleg': 'Onder de verhullende naam politionele acties vocht Nederland een bloedige koloniale dekolonisatieoorlog.'
            },
            # MC 3: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Wat schrijft Artikel 90 van de Nederlandse Grondwet expliciet voor aan de regering?',
                'opties': [
                    'Dat Nederland elk jaar zijn leger moet verdubbelen',
                    'Dat Nederland geen bondgenootschappen mag sluiten',
                    'Dat de regering de ontwikkeling van de internationale rechtsorde moet bevorderen',
                    'Dat Nederland alle wapens moet vernietigen'
                ],
                'antwoord': 2,
                'uitleg': 'Artikel 90 van de Grondwet vormt de juridische basis voor de actieve inzet van Nederland voor internationaal recht en vrede.'
            },
            # MC 4: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Waarom kwam het Nederlandse kabinet-Kok in april 2002 ten val?',
                'opties': [
                    'Vanwege een financieel schandaal rond de invoering van de euro',
                    'Omdat de minister-president met pensioen ging',
                    'Vanwege het verlies bij de gemeenteraadsverkiezingen',
                    'Naar aanleiding van het vernietigende NIOD-rapport over het falen van Dutchbat en de politieke leiding rond de val van Srebrenica'
                ],
                'antwoord': 3,
                'uitleg': 'Het voltallige kabinet trok zijn politieke conclusies uit het rapport over het drama in de Bosnische enclave.'
            },
            # MC 5: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Aan welke strikte voorwaarde moet worden voldaan voordat een Nederlands defensiebedrijf wapens of militaire apparatuur naar het buitenland mag exporteren?',
                'opties': [
                    'Er moet een officiële exportvergunning worden verleend door de Nederlandse overheid op basis van Europese mensenrechtencriteria',
                    'De koper moet altijd betalen met goudstaven',
                    'De wapens moeten minimaal honderd jaar oud zijn',
                    'Er is geen enkele vergunning nodig binnen de vrije wereldhandel'
                ],
                'antwoord': 0,
                'uitleg': 'Wapenexportvergunningen worden streng getoetst aan de Europese Gedragscode voor Wapenexport.'
            },
            # MC 6: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Wat is de rol van het Internationaal Gerechtshof in Den Haag?',
                'opties': [
                    'Bekeuringen uitschrijven aan automobilisten in Den Haag',
                    'Juridische geschillen tussen soevereine staten beslechten en adviezen uitbrengen aan de Verenigde Naties',
                    'Directe leiding geven aan de Nederlandse politie',
                    'Wapens produceren voor vredesmissies'
                ],
                'antwoord': 1,
                'uitleg': 'Het Internationaal Gerechtshof is het hoogste gerechtelijke orgaan van de VN voor geschillen tussen staten.'
            },
            # MC 7: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke Nederlandse stad staat wereldwijd bekend als de internationale hoofdstad van vrede en recht?',
                'opties': [
                    'Rotterdam',
                    'Utrecht',
                    'Den Haag',
                    'Eindhoven'
                ],
                'antwoord': 2,
                'uitleg': 'Den Haag herbergt onder andere het Vredespaleis, het Internationaal Gerechtshof en het Internationaal Strafhof.'
            },
            # MC 8: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat hield de tactiek van inundatie (het onder water zetten van land) in tijdens de vaderlandse geschiedenis?',
                'opties': [
                    'Het bouwen van zwembaden voor de soldaten',
                    'Het wassen van uniformen in de gracht',
                    'Het droogleggen van polders om sneller te kunnen rijden',
                    'Het opzettelijk openzetten van sluizen en doorsteken van dijken om een waterbarrière te creëren tegen een oprukkend vijandelijk leger (de Hollandse Waterlinie)'
                ],
                'antwoord': 3,
                'uitleg': 'Geïnundeerd land was te diep om doorheen te waden en te ondiep om met boten te bevaren.'
            },
            # MC 9: ans 0 (A)
            {
                'type': 'mc',
                'vraag': 'Op welke manier ondersteunt de Nederlandse krijgsmacht civiele autoriteiten in eigen land?',
                'opties': [
                    'Bij dijkbewaking, stormschade, overstromingshulp en bijstand aan de politie bij zware criminaliteit of terreurdreiging',
                    'Door belastingbrieven te bezorgen',
                    'Door les te geven op basisscholen',
                    'Door het openbaar vervoer permanent te besturen'
                ],
                'antwoord': 0,
                'uitleg': 'Nationale taken omvatten civiel-militaire bijstand bij grote calamiteiten en rampenbestrijding.'
            },
            # MC 10: ans 1 (B)
            {
                'type': 'mc',
                'vraag': 'Waarom was de vredesmissie van Dutchbat in Srebrenica militair gezien uiterst kwetsbaar?',
                'opties': [
                    'Omdat de soldaten geen uniformen hadden meegekregen',
                    'Omdat de blauwhelmen slechts licht bewapend waren, geen zwaar geschut hadden en afhankelijk waren van beloofde maar uitblijvende NAVO-luchtsteun',
                    'Omdat er te veel Nederlandse tanks in de enclave stonden',
                    'Omdat de VN-militairen de taal van de inwoners niet spraken'
                ],
                'antwoord': 1,
                'uitleg': 'Het VN-mandaat voor Dutchbat was vaag en de eenheid beschikte niet over voldoende vuurkracht tegen het Servische leger.'
            },
            # MC 11: ans 2 (C)
            {
                'type': 'mc',
                'vraag': 'Welke specialistische defensieproducten uit Nederland zijn internationaal toonaangevend bij moderne marineschepen?',
                'opties': [
                    'Houten roeispanen en ankers',
                    'Kanonskogels van gietijzer',
                    'Geavanceerde 3D-radarsystemen en doelzoekende vuurleidingssystemen',
                    'Duikpakken voor brandweerlieden'
                ],
                'antwoord': 2,
                'uitleg': 'De Nederlandse marine-elektronica en radarsystemen worden wereldwijd verkocht aan geallieerde marines.'
            },
            # MC 12: ans 3 (D)
            {
                'type': 'mc',
                'vraag': 'Wat is het Vredespaleis in Den Haag?',
                'opties': [
                    'Een hotel voor koninklijke gasten',
                    'Een museum voor moderne schilderkunst',
                    'Het hoofdkantoor van de Europese Unie',
                    'Het monumentale gerechtsgebouw waar onder andere het Internationaal Gerechtshof van de VN zetelt'
                ],
                'antwoord': 3,
                'uitleg': 'Het Vredespaleis werd begin 20e eeuw gebouwd als symbool en werkplaats voor de internationale arbitrage en vrede.'
            },
            # WAAR/ONWAAR (2 waar, 2 onwaar)
            # WOW 1: True
            {
                'type': 'waaronwaar',
                'vraag': 'Nederlandse militairen hebben deelgenomen aan internationale VN- en NAVO-missies in onder andere Afghanistan en Mali.',
                'antwoord': True,
                'uitleg': 'Waar: Nederland leverde troepen en helikopters aan de ISAF-missie in Uruzgan en de VN-missie MINUSMA in Mali.'
            },
            # WOW 2: False
            {
                'type': 'waaronwaar',
                'vraag': 'De Nederlandse Grondwet verbiedt de krijgsmacht om bondgenoten van de NAVO te verdedigen buiten de eigen landsgrenzen.',
                'antwoord': False,
                'uitleg': 'Onwaar: de verdediging van het bondgenootschappelijk territorium is een van de wettelijke hoofdtaken van de krijgsmacht.'
            },
            # WOW 3: False
            {
                'type': 'waaronwaar',
                'vraag': 'Tijdens de Tachtigjarige Oorlog hielden beide strijdende partijen zich strikt aan het moderne oorlogsrecht van Genève.',
                'antwoord': False,
                'uitleg': 'Onwaar: het oorlogsrecht van Genève ontstond pas in de 19e eeuw; in de 16e en 17e eeuw vonden talloze wreedheden plaats.'
            },
            # WOW 4: True
            {
                'type': 'waaronwaar',
                'vraag': 'Voor de export van militaire goederen en technologie vanuit Nederland is altijd toestemming van de ministeries vereist.',
                'antwoord': True,
                'uitleg': 'Waar: de Nederlandse overheid toetst wapenexportvergunningen aan strikte internationale wapenbeheersingscriteria.'
            },
            # INVUL 1
            {
                'type': 'invul',
                'vraag': 'Het monumentale gebouw in Den Haag waar het Internationaal Gerechtshof van de VN zetelt, heet het ....',
                'antwoord': 'Vredespaleis',
                'uitleg': 'Het Vredespaleis in Den Haag is het wereldwijde symbool van vrede en recht.'
            },
            # INVUL 2
            {
                'type': 'invul',
                'vraag': 'De historische militaire verdedigingslinie waarbij land opzettelijk onder water werd gezet om vijanden tegen te houden, heette de Hollandse ....',
                'antwoord': 'Waterlinie',
                'uitleg': 'De Hollandse Waterlinie benutte gecontroleerde inundatie als verdedigingswapen.'
            },
            # OPEN 1
            {
                'type': 'open',
                'vraag': 'Noem de naam van het Nederlandse legerbataljon dat in juli 1995 belast was met de beveiliging van Srebrenica.',
                'sleutelwoorden': [
                    'Dutchbat'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Dutchbat was het Nederlandse VN-bataljon in Srebrenica.',
                'uitleg': 'Dutchbat was gestationeerd in de Bosnische enclave.'
            },
            # OPEN 2
            {
                'type': 'open',
                'vraag': 'Geef een reden waarom de Nederlandse staat strenge vergunningseisen stelt aan de export van militaire goederen.',
                'sleutelwoorden': [
                    'mensenrechten/misbruik/oorlog/conflict/embargo/vrede/regering'
                ],
                'minTreffers': 1,
                'modelantwoord': 'Om te voorkomen dat wapens worden ingezet voor mensenrechtenschendingen of in escalerende oorlogsgebieden.',
                'uitleg': 'Wapenexportcontrole voorkomt dat militair materieel in verkeerde handen valt.'
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
   buiteNLand 3 HAVO Hoofdstuk 5 (Gewapende conflicten)
   ========================================================= */
DURU.registerExamen({{
  id: "{ex['id']}",
  hoofdstuk: {ex['hoofdstuk']},
  paragraaf: "{ex['paragraaf']}",
  hoofdstukTitel: "Hoofdstuk 5 — Gewapende conflicten",
  titel: "{ex['titel']}",
  vak: "Aardrijkskunde · HAVO 3 (H5)",
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
