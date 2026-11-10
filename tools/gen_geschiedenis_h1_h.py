#!/usr/bin/env python3
"""Geschiedenis HAVO 3 (H1) — Herhalings-toetsen 72–75 voor §1.4 en §1.5 (TASK-44).
- Toets 72 (§1.4 Herhaling A): Verdrag van Versailles en bepalingen voor Duitsland
- Toets 73 (§1.4 Herhaling B): De nieuwe kaart van Europa en het Midden-Oosten
- Toets 74 (§1.5 Herhaling A): Neutraal Nederland, vluchtelingen en mobilisatie
- Toets 75 (§1.5 Herhaling B): Grondwet 1917, Troelstra en De Stijl

Schrijft:
  havo3/geschiedenis/js/data/examen_72.js
  havo3/geschiedenis/js/data/examen_73.js
  havo3/geschiedenis/js/data/examen_74.js
  havo3/geschiedenis/js/data/examen_75.js
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_geschiedenis_h1_lib import M, W, I, O, schrijf

KORT = " <i>(Eén korte zin is genoeg.)</i>"

EXAMENS = {
    72: (
        "1.4",
        "Proeftoets 72 — §1.4 Herhaling A: Verdrag van Versailles en bepalingen voor Duitsland",
        "📜",
        [
            # 10 MC
            M(
                "In welk jaar werd het officiële vredesverdrag met Duitsland in het paleis nabij Parijs ondertekend?",
                "In 1919 (het Verdrag van Versailles)",
                [
                    "In 1918 (direct bij de wapenstilstand)",
                    "In 1914 (bij het begin van de vijandelijkheden)",
                    "In 1923 (tijdens de Vrede van Lausanne)",
                ],
                "De wapenstilstand was op 11 november 1918, maar het officiële vredesverdrag van Versailles werd in juni 1919 gesloten (§1.4).",
            ),
            M(
                "Welke geallieerde regeringsleider eiste tijdens de vredesconferentie de zwaarste straffen en de hoogste herstelbetalingen?",
                "De Franse premier Georges Clemenceau",
                [
                    "De Amerikaanse president Woodrow Wilson",
                    "De Britse premier David Lloyd George",
                    "De Russische revolutionaire leider Vladimir Lenin",
                ],
                "Clemenceau wilde Duitsland zo zwaar mogelijk straffen en militair verlammen om een nieuwe Franse invasie te voorkomen (§1.4).",
            ),
            M(
                "In welke munteenheid werd Duitsland in het Verdrag van Versailles verplicht om herstelbetalingen te voldoen?",
                "In goudmarken, gekoppeld aan een vaste hoeveelheid zuiver goud",
                [
                    "In moderne euro's, overgemaakt via een centrale Europese bankinstelling",
                    "In Amerikaanse dollars, geleend bij banken in New York",
                    "In Franse franken, rechtstreeks overgemaakt naar Parijs",
                ],
                "Duitsland moest herstelbetalingen doen in miljarden goudmarken, omdat die munt een vaste goudwaarde had en bestand was tegen inflatie (§1.4).",
            ),
            M(
                "Welke militaire beperking werd Duitsland in het Verdrag van Versailles expliciet opgelegd?",
                "Duitsland kreeg een strikt verbod op duikboten, tanks en militaire vliegtuigen",
                [
                    "Duitsland mocht onbeperkt duikboten bouwen, mits ze geen zware torpedo's droegen",
                    "Duitsland behield zijn volledige militaire luchtmacht ter verdediging van de grens",
                    "Duitsland moest zijn volledige infanterie opheffen en alleen een vloot behouden",
                ],
                "Het Verdrag van Versailles verbood Duitsland tanks, duikboten en een militaire luchtmacht (§1.4).",
            ),
            M(
                "Waarom wekte artikel 231 van het vredesverdrag enorme woede bij de Duitse bevolking?",
                "Duitsland werd gedwongen de volledige alleenschuld voor het uitbreken van de oorlog te erkennen",
                [
                    "Duitsland moest al zijn spoorwegen, scheepswerven en fabrieken afstaan aan het pas opgerichte Polen",
                    "Duitsland werd verplicht om direct toe te treden als permanente voorzitter van de Volkenbond",
                    "Duitsland mocht volgens dit artikel geen eigen grondwet of parlement meer bezitten",
                ],
                "Artikel 231 legde de exclusieve schuld voor de oorlog bij Duitsland en zijn bondgenoten; Duitsers zagen dit als een vernederend dictaat (§1.4).",
            ),
            M(
                "Welk gebied werd in 1919 aan Polen toegekend, waardoor Oost-Pruisen geografisch werd afgesneden van het moederland Duitsland?",
                "De Poolse Corridor, een strook land die Polen toegang gaf tot de Oostzee",
                [
                    "Het Sudetenland, een strategisch bergachtig grensgebied met de nieuwe staat Tsjecho-Slowakije",
                    "Het Ruhrgebied, het belangrijkste zware industriegebied aan de Rijn",
                    "Tirol, een Oostenrijkse bergregio die deels naar Italië ging",
                ],
                "De Poolse Corridor sneed Oost-Pruisen territoriaal af van de rest van Duitsland en zorgde voor een havenverbinding aan de Oostzee voor Polen (§1.4).",
            ),
            M(
                "Tot welke maximale omvang werd de Duitse landmacht teruggebracht volgens de vredesbepalingen?",
                "Tot maximaal 100.000 soldaten",
                [
                    "Tot maximaal 500.000 soldaten",
                    "Tot maximaal 25.000 gardisten die uitsluitend in Berlijn mochten blijven",
                    "Tot exact 1.000.000 grenswachters langs de Rijn en de oostgrens",
                ],
                "Het Duitse leger mocht nog slechts 100.000 man tellen, meer niet (§1.4).",
            ),
            M(
                "Welke grote mogendheid werd na 1919 geen lid van de Volkenbond, ondanks dat haar eigen president het plan had bedacht?",
                "De Verenigde Staten, omdat het Amerikaanse Congres weigerde het verdrag goed te keuren",
                [
                    "Japan, omdat het land geen nieuwe koloniën kreeg",
                    "Frankrijk, omdat de regering uitsluitend militaire allianties vertrouwde",
                    "Italië, omdat het land geen overzeese koloniën kreeg toegewezen",
                ],
                "Het Amerikaanse parlement (Congres) wilde terugkeren naar een isolationistische politiek en weigerde toetreding tot de Volkenbond (§1.4).",
            ),
            M(
                "Welke drie leiders worden de Grote Drie van de vredesconferentie genoemd?",
                "Wilson, Lloyd George en Clemenceau",
                [
                    "Wilson, Lenin en Clemenceau",
                    "Lloyd George, Kemal en Wilson",
                    "Clemenceau, Troelstra en Lloyd George",
                ],
                "De Grote Drie: Wilson (VS), Lloyd George (Groot-Brittannië) en Clemenceau (Frankrijk) (§1.4).",
            ),
            M(
                "Polen en Tsjechen kregen na 1918 een eigen staat. Welk principe zat daarachter?",
                "Elk volk moet zelf kunnen bepalen onder welke staat of regering het wil leven",
                [
                    "De overwinnaars van de oorlog mogen zelf beslissen welke koloniën zij inlijven",
                    "Alle Europese vorstenhuizen behouden automatisch het erfrecht op hun troon",
                    "Elk land heeft het soevereine recht om zelfstandig chemische wapens te bezitten",
                ],
                "Het zelfbeschikkingsrecht stelde dat volkeren (zoals Polen of Tsjechen) het recht hadden op een eigen soevereine nationale staat (§1.4).",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "Duitsland mocht na de Eerste Wereldoorlog volgens de vredesvoorwaarden zijn militaire vliegtuigen gewoon behouden.",
                False,
                "Onwaar. Duitsland kreeg een totaalverbod op een militaire luchtmacht (§1.4).",
            ),
            W(
                "In het Verdrag van Versailles werd bepaald dat de geallieerden de schuld voor de oorlog gelijkmatig over alle deelnemende landen verdeelden.",
                False,
                "Onwaar. Artikel 231 legde de alleenschuld eenzijdig bij Duitsland en zijn bondgenoten (§1.4).",
            ),
            W(
                "Frankrijk kreeg door het Verdrag van Versailles het in 1871 verloren gegane gebied aan de oostgrens weer terug van Duitsland.",
                True,
                "Waar. Dit grensgebied was in 1871 door Duitsland ingenomen en kwam in 1919 weer bij Frankrijk (§1.4).",
            ),
            W(
                "De Volkenbond werd opgericht met als hoofddoel toekomstige oorlogen te voorkomen door internationale samenwerking.",
                True,
                "Waar. De organisatie moest geschillen tussen landen vreedzaam oplossen via overleg (§1.4).",
            ),
            W(
                "De Amerikaanse president Woodrow Wilson wilde met zijn plannen een rechtvaardige en duurzame wereldvrede tot stand brengen.",
                True,
                "Waar. Wilson pleitte voor open diplomatie, ontwapening en zelfbeschikkingsrecht voor volkeren (§1.4).",
            ),
            # 4 Invul
            I(
                "Lloyd George, een van de Grote Drie, was de premier van ____.",
                "Groot-Brittannië|Groot Brittannië|Engeland|Brittannië",
                "Lloyd George was de Britse premier (§1.4).",
            ),
            I(
                "Het grensgebied dat Duitsland in 1919 verplicht moest afstaan aan Frankrijk, heette ____.",
                "Elzas-Lotharingen|Elzas Lotharingen",
                "Elzas-Lotharingen ging terug naar Frankrijk (§1.4).",
            ),
            I(
                "Het beruchte schuld-artikel uit het Verdrag van Versailles droeg het nummer artikel ____.",
                "231",
                "Artikel 231 bevatte de gehate 'alleenschuld' (§1.4).",
            ),
            I(
                "Het Verdrag van Versailles kwam in 1919; de wapenstilstand was al in ____ 1918.",
                "november",
                "De wapenstilstand ging in op 11 november 1918, het verdrag volgde in 1919 (§1.4).",
            ),
            # 1 Open
            O(
                "Noem één wapen dat Duitsland na het Verdrag van Versailles niet meer mocht hebben." + KORT,
                ["duikboten/duikboot/luchtmacht/vliegtuigen/vliegtuig/tanks/tank"],
                1,
                "Duitsland mocht maximaal 100.000 soldaten hebben en geen duikboten of militaire vliegtuigen bezitten.",
                "Duitsland kreeg een leger van maximaal 100.000 man en een verbod op tanks, duikboten en militaire vliegtuigen (§1.4).",
            ),
        ],
    ),
    73: (
        "1.4",
        "Proeftoets 73 — §1.4 Herhaling B: De nieuwe kaart van Europa en het Midden-Oosten",
        "🗺️",
        [
            # 10 MC
            M(
                "Aan de Oostzee maakten Letland, Litouwen en een derde noordelijke staat zich los uit het tsarenrijk. Hoe noemen we deze groep van drie staten?",
                "De Baltische staten (of Baltische republieken)",
                [
                    "De Zuid-Slavische Balkanstaten",
                    "De Kaukasische bergstaten",
                    "De neutrale Scandinavische staten",
                ],
                "Aan de Oostzee maakten Estland, Letland en Litouwen (de Baltische staten) zich los uit het voormalige Russische tsarenrijk (§1.4).",
            ),
            M(
                "Wat bleef er na de oorlog over van het eens zo machtige Oostenrijk?",
                "Een klein, Duitstalig republiekje in de Alpenregio",
                [
                    "Een Frans mandaatgebied onder toezicht van de Volkenbond",
                    "Een groot koninkrijk waarin alle Zuid-Slaven verenigd waren",
                    "Een provincie die direct werd samengevoegd met de Sovjet-Unie",
                ],
                "Oostenrijk verloor Hongarije, Tsjechië en grote stukken land en bleef over als een klein Duitstalig staatje (§1.4).",
            ),
            M(
                "Welke twee nieuwe zelfstandige staten ontstonden direct door het opbreken van de dubbelmonarchie Oostenrijk-Hongarije?",
                "Hongarije en Tsjecho-Slowakije",
                [
                    "Joegoslavië en Bulgarije",
                    "Polen en de Sovjet-Unie",
                    "Albanië en Griekenland",
                ],
                "Na de Eerste Wereldoorlog viel de dubbelmonarchie uiteen; Oostenrijk en Hongarije werden gescheiden en Tsjecho-Slowakije werd een nieuwe staat (§1.4).",
            ),
            M(
                "Welke volkeren werden na 1918 samengevoegd in de nieuwe staat die later het koninkrijk Joegoslavië ging heten?",
                "Onder meer Serviërs, Kroaten, Slovenen en Bosniërs",
                [
                    "Uitsluitend Tsjechen, Slowaken en Duitstalige Sudeten",
                    "Alleen Roemenen, Bulgaren en Grieken",
                    "Uitsluitend Oostenrijkers en Hongaren",
                ],
                "Het Koninkrijk van Serviërs, Kroaten en Slovenen (later Joegoslavië) verenigde verschillende Zuid-Slavische volken op de Balkan (§1.4).",
            ),
            M(
                "Welk motief van de geallieerden leidde ertoe dat Griekse strijdkrachten in mei 1919 overstaken naar Turkije?",
                "De overwinnaars van de oorlog wilden grote delen van het Ottomaanse Rijk verdelen",
                [
                    "De Geallieerden wilden het leger van Mustafa Kemal actief steunen tegen de sultan",
                    "De sultan had de buitenlandse machten gevraagd om de Turkse havens militair te bezetten",
                    "De Volkenbond wilde een neutrale internationale hoofdstad vestigen in West-Azië",
                ],
                "De Geallieerden wilden het Ottomaanse Rijk ontmantelen en gaven Griekenland toestemming om delen van West-Anatolië te bezetten (§1.4).",
            ),
            M(
                "Uit welk uitgestrekt gebied slaagden de Turkse nationalistische troepen onder leiding van Kemal erin de bezettingsmacht te verdrijven?",
                "Uit Anatolië",
                [
                    "Uitsluitend uit het historische centrum van de belegerde havenstad",
                    "Uit de berggebieden van Noord-Syrië en Irak",
                    "Uit de zuidelijke provincies van het Russische Rijk",
                ],
                "Mustafa Kemal organiseerde het nationale verzet en verdreef het Griekse leger tussen 1919 en 1922 volledig uit Anatolië (§1.4).",
            ),
            M(
                "Welke ingrijpende politieke verandering voerde Mustafa Kemal door voordat de moderne republiek werd gesticht?",
                "Hij schafte het eeuwenoude sultanaat formeel af",
                [
                    "Hij maakte van Turkije een mandaatgebied van Groot-Brittannië",
                    "Hij liet zichzelf kronen tot de nieuwe absolute sultan",
                    "Hij sloot een militair bondgenootschap met de tsaar van Rusland",
                ],
                "In november 1922 schafte het Turkse parlement het sultanaat af, waarmee een einde kwam aan het Ottomaanse Rijk; in 1923 werd de republiek uitgeroepen (§1.4).",
            ),
            M(
                "Welke politieke leidersrol bekleedde Mustafa Kemal nadat in oktober 1923 de Republiek Turkije officieel was uitgeroepen?",
                "Hij werd gekozen tot de allereerste president van de republiek",
                [
                    "Hij werd ingehuldigd als de nieuwe religieuze sultan",
                    "Hij werd benoemd tot Brits gouverneur-generaal van het Midden-Oosten",
                    "Hij trad af en werd opperbevelhebber van de geallieerde vredestroepen",
                ],
                "Kemal (later Atatürk genoemd) werd de eerste president van de nieuwe seculiere Republiek Turkije (§1.4).",
            ),
            M(
                "Wat werd in 1923 bij het verdrag tussen Turkije en Griekenland afgesproken over elkaars minderheden?",
                "Er kwam een verplichte volkenruil van circa 1,7 miljoen mensen",
                [
                    "Er werd een ruil van 2,2 miljoen soldaten tussen de legers afgesproken",
                    "Alle minderheden kregen een eigen onafhankelijke staat toegewezen",
                    "Alle inwoners moesten verplicht emigreren naar de Verenigde Staten",
                ],
                "Het Verdrag van Lausanne regelde een verplichte volkenruil van ongeveer 1,7 miljoen mensen: circa 1,2 miljoen Grieken verlieten Turkije en 500.000 Turken verlieten Griekenland (§1.4).",
            ),
            M(
                "Welke bevolkingsgroep vormde het grootste deel van de mensen die tijdens de volkenruil van 1923 moesten verhuizen?",
                "Circa 1,2 miljoen christelijke Grieken die al generaties in Turkije woonden",
                [
                    "Circa 500.000 islamitische Turken die woonden in West-Thracië en Griekenland",
                    "Miljoenen Armeense vluchtelingen die naar West-Europa trokken",
                    "Honderdduizenden Britse en Franse soldaten die terugkeerden naar huis",
                ],
                "De grootste groep bij de volkenruil bestond uit ongeveer 1,2 miljoen Grieks-orthodoxe christenen die uit Turkije naar Griekenland werden gedeporteerd (§1.4).",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "Mustafa Kemal liet zich na de overwinning op de Grieken kronen tot de nieuwe sultan van het Ottomaanse Rijk.",
                False,
                "Onwaar. Kemal schafte het sultanaat juist af en werd president van de nieuwe republiek (§1.4).",
            ),
            W(
                "De herstelde staat Polen werd na 1918 uitsluitend gevormd uit grondgebied dat voorheen bij Oostenrijk-Hongarije hoorde.",
                False,
                "Onwaar. Polen kreeg ook grote gebieden van het voormalige Duitse Keizerrijk en het Russische Rijk (§1.4).",
            ),
            W(
                "In het Verdrag van Lausanne van 1923 werden de definitieve grenzen van de nieuwe Republiek Turkije internationaal erkend.",
                True,
                "Waar. Dit verdrag verving het eerdere ongunstige Verdrag van Sèvres en legde de moderne grenzen vast (§1.4).",
            ),
            W(
                "Het uiteenvallen van Oostenrijk-Hongarije leidde ertoe dat miljoenen mensen plotseling in nieuwe nationale staten kwamen te wonen.",
                True,
                "Waar. Staten zoals Tsjecho-Slowakije, Oostenrijk, Hongarije en Joegoslavië ontstonden op het grondgebied van de dubbelmonarchie (§1.4).",
            ),
            W(
                "De volkenruil tussen Griekenland en Turkije gebeurde op basis van religie: orthodoxe christenen moesten naar Griekenland en moslims naar Turkije.",
                True,
                "Waar. Religieuze identiteit bepaalde wie moest verhuizen (§1.4).",
            ),
            # 4 Invul
            I(
                "De drie staten die zich aan de Oostzee losmaakten van Rusland, waren Litouwen, Letland en ____.",
                "Estland",
                "Estland, Letland en Litouwen vormden samen de Baltische staten (§1.4).",
            ),
            I(
                "Mustafa Kemal vestigde de nieuwe regering van de onafhankelijke Turkse staat in de stad ____.",
                "Ankara",
                "Kemal maakte van Ankara de nieuwe hoofdstad van de republiek (§1.4).",
            ),
            I(
                "In het Verdrag van Lausanne werd een gedwongen volkenruil afgesproken van in totaal circa ____ miljoen mensen.",
                "1,7|1.7",
                "In totaal ging het om circa 1,7 miljoen mensen (1,2 miljoen Grieken en 500.000 Turken) (§1.4).",
            ),
            I(
                "In het voorjaar van 1919 begon het conflict met een amfibische landing van het Griekse leger in de havenstad ____.",
                "Smyrna|Izmir",
                "De Griekse inval begon in de havenstad Smyrna (het huidige Izmir) (§1.4).",
            ),
            # 1 Open
            O(
                "Waarom was de uitkomst van de Vrede van Lausanne in 1923 voor Turkije veel gunstiger dan het eerdere Verdrag van Sèvres?" + KORT,
                ["grenzen/Anatolië/grondgebied/Anatolie", "onafhankelijk/republiek/erkend/bezetting"],
                1,
                "Turkije behield heel Anatolië en werd internationaal erkend als een onafhankelijke staat.",
                "Bij Lausanne werden de grenzen herzien: heel Anatolië bleef Turks en de bezetting werd beëindigd (§1.4).",
            ),
        ],
    ),
    74: (
        "1.5",
        "Proeftoets 74 — §1.5 Herhaling A: Neutraal Nederland, vluchtelingen en mobilisatie",
        "🛡️",
        [
            # 10 MC
            M(
                "Waarom riep de Nederlandse regering in de zomer van 1914 direct 200.000 militairen op om paraat te staan aan de grens?",
                "Om de grenzen te bewaken en een buitenlandse invasie gewapenderhand af te schrikken",
                [
                    "Om zich aan te sluiten bij het Duitse leger voor een verrassingsaanval op Frankrijk",
                    "Om de Britse marine actief bij te staan tijdens de algehele handelsblokkade van de Noordzee",
                    "Om de Russische revolutie met Nederlandse troepen de kop in te drukken",
                ],
                "Nederland was neutraal en wilde een schending van zijn grondgebied voorkomen; daarom hield het 200.000 man gemobiliseerd aan de grens (§1.5).",
            ),
            M(
                "Wat gebeurde er met de Belgische bevolking na de plotselinge Duitse inval in augustus 1914?",
                "Ruim 1 miljoen Belgen vluchtten naar Nederland, waarvan er ongeveer 100.000 de hele oorlog bleven",
                [
                    "Slechts enkele tientallen rijke families wisten per boot naar Engeland te ontkomen",
                    "Alle Belgische burgers werden door het gemobiliseerde Nederlandse leger direct over de grens teruggestuurd",
                    "Precies 2,5 miljoen vluchtelingen kregen blijvend het Nederlandse staatsburgerschap",
                ],
                "In 1914 vluchtten ruim 1 miljoen Belgen de grens over; na de eerste paniek keerden velen terug, maar zo'n 100.000 bleven tot 1918 (§1.5).",
            ),
            M(
                "Waardoor vonden honderden smokkelaars en vluchtelingen de dood bij het Duitse grensraster tussen België en Nederland?",
                "Door elektrocutie als gevolg van een dodelijke hoogspanning van 2000 volt",
                [
                    "Doordat ze verstrikt raakten in gewoon prikkeldraad en door dorst en honger omkwamen",
                    "Doordat ze werden aangevallen door speciale speurhonden van de douane",
                    "Door gifgaswolken die permanent langs het hekwerk werden verspreid",
                ],
                "De Duitse bezetter zette een hoogspanningshek (ca. 2000 volt) langs de grens. Wie de draad aanraakte, stierf door elektrocutie (§1.5).",
            ),
            M(
                "Welk direct gevolg hadden de Britse vlootblokkade en de Duitse onderzeebootaanvallen voor de grote Nederlandse havenstad aan de Maas?",
                "De internationale scheepvaart viel grotendeels stil en er ontstond grote werkloosheid",
                [
                    "De haven werd definitief overgenomen door de Duitse keizerlijke marine als officiële duikbootbasis",
                    "De haven groeide explosief door de smokkel van Amerikaanse wapens naar Berlijn",
                    "De haven werd verplaatst naar het IJsselmeer om bombardementen te vermijden",
                ],
                "Door de zeeblokkade en zeemijnen liepen nauwelijks nog zeeschepen Rotterdam binnen, waardoor de aanvoer van grondstoffen stokte (§1.5).",
            ),
            M(
                "Hoe werkte het systeem van bonkaarten tijdens de Eerste Wereldoorlog in Nederland?",
                "Met een bon kreeg je het recht om een schaars artikel tegen de officiële maximumprijs te kopen",
                [
                    "Tegen inlevering van een bon kreeg iedereen alle benodigde levensmiddelen en brandstof geheel gratis mee",
                    "De bonnen waren uitsluitend bedoeld voor buitenlandse vluchtelingen in opvangkampen",
                    "Wie over een bon beschikte, mocht onbeperkte hoeveelheden suiker en bloem inslaan",
                ],
                "Distributiebonnen waren géén gratis tegoedbonnen; ze gaven burgers het recht om een strikt afgepaste hoeveelheid te kopen tegen een door de overheid vastgestelde prijs (§1.5).",
            ),
            M(
                "Wat ontstond er in Nederland doordat schaarse goederen op de bon gingen en de vraag naar eten groot bleef?",
                "Een zwarte markt waar handelaren goederen illegaal tegen extreem hoge woekerprijzen verkochten",
                [
                    "Een officiële landelijke veiling waar de koningin en ministers wekelijks gratis steenkool uitdeelden",
                    "Een staatswinkel waar alle producten zonder bonkaart te koop waren",
                    "Een ruilhandel waarin uitsluitend goudmarken als wettig betaalmiddel golden",
                ],
                "Schaarste leidde tot een illegale zwarte markt; wie rijk was kon daar buiten de bonnen om schaarse producten kopen tegen torenhoge prijzen (§1.5).",
            ),
            M(
                "Aan welke essentiële brandstof ontstond in Nederland tijdens de oorlog een nijpend gebrek voor huishoudens en fabrieken?",
                "Aan steenkool, waardoor treinen minder reden en mensen 's winters in de kou zaten",
                [
                    "Aan aardgas, doordat alle ondergrondse toevoerleidingen vanuit het Russische Rijk waren afgesloten",
                    "Aan benzine, omdat alle automotoren uitsluitend op elektriciteit werkten",
                    "Aan kernenergie, doordat de reactoren stilgelegd moesten worden",
                ],
                "Steenkool was de belangrijkste brandstof voor verwarming, treinen en fabrieken; door de blokkade en importstop ontstond ernstige brandstofschaarste (§1.5).",
            ),
            M(
                "Hoe organiseerden burgers en gemeenten de opvang van de plotselinge stroom Belgische vluchtelingen in 1914?",
                "Ze werden gastvrij ondergebracht in scholen, tentenkampen, loodsen en bij particuliere gezinnen",
                [
                    "Ze werden verplicht tewerkgesteld als dwangarbeiders in de zware steenkoolmijnen van Zuid-Limburg",
                    "Ze werden uitsluitend opgesloten in zwaarbewaakte strafkampen aan de kust",
                    "Ze moesten op het strand bivakkeren totdat de vrede getekend was",
                ],
                "Gemeenten en burgers vingen de vluchtelingen massaal op in provisorische opvangkampen, loodsen, scholen en huiskamers (§1.5).",
            ),
            M(
                "Waarom richtte Nederland de Nederlandsche Overzee Trustmaatschappij (N.O.T.) op tijdens de oorlog?",
                "Om aan de Britten te garanderen dat ingevoerde goederen niet werden doorgevoerd naar Duitsland",
                [
                    "Om stiekem munitie en zware artillerie te leveren aan het Franse leger aan het Westfront",
                    "Om de Belgische vluchtelingen van banen te voorzien in de landbouw",
                    "Om de goudvoorraad van de Nederlandsche Bank naar Amerika te verhuizen",
                ],
                "De N.O.T. controleerde de invoer en garandeerde aan Engeland dat goederen in Nederland bleven en niet bij de Duitsers terechtkwamen (§1.5).",
            ),
            M(
                "Welk gevaar liepen Nederlandse koopvaardijschepen op de Noordzee ondanks de officiële neutraliteit?",
                "Ze liepen het risico getorpedeerd te worden door Duitse duikboten of op zeemijnen te lopen",
                [
                    "Ze werden bij het verlaten van de haven automatisch in beslag genomen door het neutrale Zweden",
                    "Ze mochten alleen nog 's nachts varen zonder enige verlichting",
                    "Ze werden verplicht om onder de vlag van Oostenrijk-Hongarije te varen",
                ],
                "Tijdens de onbeperkte duikbootoorlog torpedeerden Duitse duikboten ook neutrale schepen en tienduizenden zeemijnen maakten de zee levensgevaarlijk (§1.5).",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "Distributiebonnen gaven Nederlandse gezinnen het recht om voedsel en brandstof gratis bij de winkelier op te halen.",
                False,
                "Onwaar. Met een bon mocht je het product kopen, maar je moest er gewoon voor betalen (§1.5).",
            ),
            W(
                "De draadafsluiting aan de grens was een gewoon hekwerk waar vluchtelingen zonder gevaar onderdoor konden kruipen.",
                False,
                "Onwaar. Het hekwerk stond onder dodelijke hoogspanning van ca. 2000 volt (§1.5).",
            ),
            W(
                "Nederland hield tijdens de hele Eerste Wereldoorlog een gemobiliseerd leger van 200.000 soldaten op de been.",
                True,
                "Waar. De mobilisatie duurde van 1914 tot 1918 om de neutraliteit gewapenderhand te kunnen verdedigen (§1.5).",
            ),
            W(
                "Door de blokkade van de scheepvaart ontstond in Nederland een bloeiende zwarte markt voor schaarse goederen.",
                True,
                "Waar. Smokkelaars en handelaren vroegen woekerprijzen aan mensen met veel geld (§1.5).",
            ),
            W(
                "Van de meer dan één miljoen Belgische vluchtelingen bleven er ongeveer honderdduizend gedurende de gehele oorlogsperiode in Nederland.",
                True,
                "Waar. Ongeveer 100.000 Belgen bleven tot het einde van de oorlog in 1918 (§1.5).",
            ),
            # 4 Invul
            I(
                "Het paraat houden en oproepen van het leger ter verdediging van de grenzen heet ____.",
                "mobilisatie|de mobilisatie",
                "Nederland hield zijn troepen vier jaar lang gemobiliseerd (§1.5).",
            ),
            I(
                "De havenstad die zwaar getroffen werd doordat de internationale scheepvaart stilviel, was ____.",
                "Rotterdam",
                "Rotterdam zag zijn havenactiviteit vrijwel volledig stilvallen door de blokkade (§1.5).",
            ),
            I(
                "De dodelijke elektrische versperring langs de grens tussen Nederland en België stond bekend als de Draad des ____.",
                "Doods",
                "Aan de Draad des Doods stierven honderden vluchtelingen en smokkelaars (§1.5).",
            ),
            I(
                "Het verdelen van schaarse levensmiddelen via bonkaarten door de overheid heet het ____.",
                "distributiestelsel|distributiesysteem",
                "Via het distributiestelsel bepaalde de overheid wie wat mocht kopen (§1.5).",
            ),
            # 1 Open
            O(
                "Leg uit waarom een distributiebon tijdens de Eerste Wereldoorlog geen gratis voedsel betekende." + KORT,
                ["betalen/prijs/kopen", "recht/toewijzing/afpassen/maximumprijs"],
                1,
                "Een bon gaf alleen het recht om een product te kopen; men moest er gewoon voor betalen.",
                "Een distributiebon was geen waardebon, maar een aankoopbewijs waarmee je tegen betaling een schaars artikel kon kopen (§1.5).",
            ),
        ],
    ),
    75: (
        "1.5",
        "Proeftoets 75 — §1.5 Herhaling B: Grondwet 1917, Troelstra en De Stijl",
        "⚖️",
        [
            # 10 MC
            M(
                "Welke twee langdurige politieke strijdpunten werden met de historische Grondwet van 1917 tegelijkertijd opgelost?",
                "De schoolstrijd en de strijd om het algemeen kiesrecht",
                [
                    "De neutraliteitspolitiek en de afschaffing van de monarchie",
                    "De invoering van de zomertijd en de sluiting van de grenzen",
                    "De herstelbetalingen aan België en de ontwapening van het leger",
                ],
                "De pacificatie van 1917 loste zowel de schoolstrijd (financiële gelijkstelling bijzonder onderwijs) als de kiesrechtkwestie op (§1.5).",
            ),
            M(
                "Vanaf welk jaar mochten Nederlandse vrouwen voor het eerst zelf actief naar de stembus gaan om te stemmen?",
                "Vanaf 1919, toen de wet op het actieve vrouwenkiesrecht werd aangenomen",
                [
                    "Al direct in 1917, tegelijk met de officiële invoering van het algemeen mannenkiesrecht",
                    "Pas in 1945, na afloop van de Tweede Wereldoorlog",
                    "Al in 1896, bij de oprichting van de moderne Olympische Spelen",
                ],
                "In 1917 kregen vrouwen alleen passief kiesrecht (gekozen worden); het actieve kiesrecht (zelf stemmen) kregen ze pas in 1919 (§1.5).",
            ),
            M(
                "Waarom liep de oproep tot revolutie van de socialistische voorman Troelstra in november 1918 op een fiasco uit?",
                "De overgrote meerderheid van het volk en het leger bleef loyaal aan de democratie en de regering",
                [
                    "Troelstra werd direct bij zijn aankomst in Den Haag gearresteerd door buitenlandse bezettingstroepen",
                    "De koningin vluchtte in paniek naar Engeland waardoor het doel verdween",
                    "De arbeiders waren te druk met het vieren van de overwinning op Duitsland",
                ],
                "Troelstra overschatte de revolutiegeest van de Nederlandse arbeiders; er was amper steun en het leger weigerde mee te doen (§1.5).",
            ),
            M(
                "Waar verzamelden zich in november 1918 tienduizenden burgers in Den Haag om hun trouw aan de monarchie te betonen?",
                "Op het grote grasveld van het Malieveld, ter ondersteuning van het Nederlandse koningshuis",
                [
                    "Op het Binnenhof direct voor de Ridderzaal, om de socialistische ministers van de regering toe te spreken",
                    "Op de Dam in Amsterdam, om een nieuwe republiek uit te roepen",
                    "Op het Vrijthof in Maastricht, ter ere van de teruggekeerde grenswachters",
                ],
                "Op het Malieveld in Den Haag vond een gigantische manifestatie van trouw aan koningin Wilhelmina plaats, waarbij de paarden van haar koets werden ontkoppeld (§1.5).",
            ),
            M(
                "Welke kleurencombinatie werd consequent toegepast door de kunstenaars van De Stijl?",
                "De primaire kleuren rood, geel en blauw, aangevuld met wit, grijs en zwart",
                [
                    "Uitsluitend gedempte pastelkleuren zoals zachtroze, lichtgroen en warm oranje",
                    "Alleen aardetinten zoals bruin, donkergroen en okergeel",
                    "Uitsluitend felle neonkleuren zonder enig gebruik van wit of zwart",
                ],
                "De kunstenaars van De Stijl (1917) gebruikten uitsluitend de drie primaire kleuren (rood, geel, blauw) en de zogeheten 'niet-kleuren' (wit, grijs, zwart) (§1.5).",
            ),
            M(
                "Welk beroemd ontwerp staat op naam van de Utrechtse ontwerper Gerrit Rietveld?",
                "De Rietveld-stoel",
                [
                    "Het schilderij met ontelbare kleine kleurvlakken van De Stijl",
                    "Het schilderij De Aardappeleters met donkere, realistische penseelstreken",
                    "Het bronzen standbeeld van Pieter Jelles Troelstra in Den Haag",
                ],
                "Gerrit Rietveld ontwierp de Rietveld-stoel; Victory Boogie Woogie is geschilderd door Piet Mondriaan (§1.5).",
            ),
            M(
                "Wie was de schilder van De Stijl die wereldwijde faam verwierf met zijn composities van zwarte lijnen en rechthoekige kleurvlakken?",
                "Piet Mondriaan",
                [
                    "Gerrit Rietveld",
                    "Vincent van Gogh",
                    "Pieter Jelles Troelstra",
                ],
                "Piet Mondriaan was de schilder die de beeldtaal van De Stijl ontwikkelde; Rietveld paste deze principes toe op meubels en architectuur (§1.5).",
            ),
            M(
                "Wat hield de oplossing van de schoolstrijd in de Grondwet van 1917 precies in?",
                "Bijzondere (confessionele) scholen kregen voortaan evenveel geld van de overheid als de scholen van de staat",
                [
                    "Alle christelijke scholen moesten met onmiddellijke ingang worden omgevormd tot neutrale staatsscholen",
                    "Kinderen mochten voortaan zelf kiezen of ze wel of niet naar school gingen",
                    "Het schoolgeld werd verdubbeld om de kosten van de mobilisatie te dekken",
                ],
                "De financiële gelijkstelling hield in dat het bijzonder onderwijs (zoals katholieke en protestantse scholen) voortaan volledig door het Rijk werd bekostigd (§1.5).",
            ),
            M(
                "Wat hield het passief kiesrecht in dat vrouwen in Nederland in 1917 verkregen?",
                "Vrouwen mochten zich verkiesbaar stellen voor politieke functies, maar nog niet zelf stemmen",
                [
                    "Vrouwen mochten anoniem naar de stembus via een verplichte schriftelijke volmacht van hun echtgenoot",
                    "Vrouwen kregen automatisch de helft van alle zetels in de Tweede Kamer",
                    "Vrouwen mochten alleen meebeslissen over het plaatselijke dorpsbestuur",
                ],
                "Passief kiesrecht betekent dat je gekozen mag worden; pas in 1919 kregen vrouwen ook actief kiesrecht (zelf mogen stemmen) (§1.5).",
            ),
            M(
                "In welk oorlogsjaar werd het invloedrijke tijdschrift en de kunstbeweging De Stijl opgericht?",
                "In 1917",
                [
                    "In 1914",
                    "In 1919",
                    "In 1923",
                ],
                "De kunstbeweging De Stijl werd in 1917 in Nederland opgericht door onder anderen Theo van Doesburg en Piet Mondriaan (§1.5).",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "De kunstschilder van De Stijl ontwierp de beroemde Rietveld-stoel.",
                False,
                "Onwaar. Gerrit Rietveld ontwierp de stoel; Mondriaan was kunstschilder (§1.5).",
            ),
            W(
                "In 1917 kregen Nederlandse vrouwen direct tegelijkertijd het actief én het passief kiesrecht.",
                False,
                "Onwaar. In 1917 kregen vrouwen alleen passief kiesrecht; het actief kiesrecht volgde pas in 1919 (§1.5).",
            ),
            W(
                "De mislukte poging van Troelstra om in november 1918 een revolutie uit te roepen, staat in de geschiedenis bekend als de vergissing van Troelstra.",
                True,
                "Waar. Troelstra dacht ten onrechte dat Nederland rijp was voor een revolutie (§1.5).",
            ),
            W(
                "De kunstenaars van De Stijl gebruikten naast rood, geel en blauw ook de niet-kleuren wit, grijs en zwart.",
                True,
                "Waar. Dit strakke kleurgebruik was kenmerkend voor hun abstracte vormgeving (§1.5).",
            ),
            W(
                "De financiële gelijkstelling van het bijzonder onderwijs maakte een einde aan de decennialange schoolstrijd.",
                True,
                "Waar. Confessionele en openbare scholen kregen vanaf 1917 dezelfde financiële steun van de overheid (§1.5).",
            ),
            # 4 Invul
            I(
                "Gerrit Rietveld ontwierp niet alleen wereldberoemde meubels, maar werkte ook als vernieuwend ____.",
                "architect",
                "Rietveld was meubelmaker en architect (o.a. het Rietveld Schröderhuis) (§1.5).",
            ),
            I(
                "De koningin die in november 1918 op het Malieveld massaal werd toegejuicht door het volk, was koningin ____.",
                "Wilhelmina",
                "Koningin Wilhelmina genoot enorme populariteit onder het volk (§1.5).",
            ),
            I(
                "Sinds 1917 krijgt het bijzonder onderwijs evenveel geld als het ____ onderwijs.",
                "openbaar|openbare",
                "Financiële gelijkstelling: bijzonder en openbaar onderwijs kregen evenveel geld (§1.5).",
            ),
            I(
                "Het beroemde, onvoltooide abstracte schilderij van Piet Mondriaan heet Victory Boogie ____.",
                "Woogie|woogie",
                "Mondriaan werkte in New York aan Victory Boogie Woogie (§1.5).",
            ),
            # 1 Open
            O(
                "Leg in één korte zin uit waarom de revolutiepoging van Troelstra in november 1918 mislukte." + KORT,
                ["amper steun/weinig steun/geen steun/geen aanhang", "loyaal/koningin/democratie/regering"],
                1,
                "Hij kreeg amper steun van arbeiders en soldaten, die massaal kozen voor trouw aan de koningin.",
                "Troelstra kreeg vrijwel geen aanhang onder het volk en de militairen bleven loyaal aan het gezag (§1.5).",
            ),
        ],
    ),
}

if __name__ == "__main__":
    schrijf(EXAMENS, seed=20261110)
