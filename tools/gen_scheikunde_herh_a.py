#!/usr/bin/env python3
"""Scheikunde HAVO 3 (H2) — Herhalings-toetsen 64–67 (TASK-45).
- Toets 64 (§2.2 Herhaling A): Bouw van moleculen en atomen
- Toets 65 (§2.2 Herhaling B): Modellen, symbolen en formules
- Toets 66 (H2 Herhaling gemengd A): Begrippen, macro en micro
- Toets 67 (H2 Herhaling gemengd B): Atomen, isotopen en massa

Schrijft:
  havo3/scheikunde/js/data/examen_h2_64.js
  havo3/scheikunde/js/data/examen_h2_65.js
  havo3/scheikunde/js/data/examen_h2_66.js
  havo3/scheikunde/js/data/examen_h2_67.js
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_scheikunde_h1_lib import M, W, I, O, schrijf, KORT, GETAL

EXAMENS = {
    64: (
        "2.2",
        "Toets 64 — §2.2 Herhaling A: Bouw van moleculen en atomen",
        "⚛️",
        [
            # 10 MC
            M(
                "Zijn moleculen de allerkleinste bouwstenen waaruit een stof kan bestaan?",
                "Nee, want moleculen zijn zelf weer opgebouwd uit nog kleinere deeltjes: atomen",
                [
                    "Ja, moleculen zijn de kleinst mogelijke deeltjes en kunnen niet verder worden gesplitst",
                    "Ja, alleen een gas bestaat uit atomen, vloeistoffen bestaan uit ondeelbare moleculen",
                    "Nee, moleculen bestaan uitsluitend uit elektronen die los door de ruimte vliegen",
                ],
                "Moleculen zijn niet ondeelbaar; ze zijn opgebouwd uit aan elkaar gebonden atomen. (§2.2)",
            ),
            M(
                "Hoeveel verschillende atoomsoorten zijn er momenteel officieel bekend in het periodiek systeem?",
                "Honderdachttien atoomsoorten in totaal",
                [
                    "Meer dan duizend verschillende atoomsoorten",
                    "Ongeveer twintig verschillende atoomsoorten",
                    "Miljoenen, omdat elke stof een eigen unieke atoomsoort bezit",
                ],
                "Er zijn circa 118 verschillende atoomsoorten bekend. Met deze bouwstenen kunnen miljoenen verschillende stoffen worden gevormd. (§2.2)",
            ),
            M(
                "Wanneer noemen we een zuivere stof in de scheikunde een verbinding (ontleedbare stof)?",
                "Als de moleculen van de stof zijn opgebouwd uit twee of meer verschillende atoomsoorten",
                [
                    "Als de stof altijd een heldere vloeistof blijft bij gewone kamertemperatuur",
                    "Als alle moleculen in de stof uitsluitend uit één enkele atoomsoort zijn opgebouwd",
                    "Als de stof bestaat uit een volkomen homogeen mengsel van meerdere zuivere vloeistoffen",
                ],
                "Een verbinding is een stof waarvan de moleculen uit twee of meer verschillende atoomsoorten bestaan (zoals water: H en O). (§2.2)",
            ),
            M(
                "Aceton (C3H6O) en glucose (C6H12O6) bevatten beide uitsluitend koolstof-, waterstof- en zuurstofatomen. Waarom zijn het toch twee totaal verschillende stoffen?",
                "De aantallen atomen per molecuul en de onderlinge rangschikking van de atomen zijn verschillend",
                [
                    "In aceton zijn alle atomen vloeibaar van aard, terwijl in vaste glucose exact dezelfde atomen voorkomen",
                    "De zuurstofatomen in aceton zijn veel zwaarder dan de zuurstofatomen in glucose",
                    "Glucose is een mengsel en aceton is een element dat niet ontleed kan worden",
                ],
                "Hoewel beide stoffen dezelfde drie atoomsoorten (C, H, O) bevatten, bepalen het aantal atomen in het molecuul en de chemische structuur de specifieke stofeigenschappen. (§2.2)",
            ),
            M(
                "Uit hoeveel verschillende atoomsoorten is een molecuul glucose (C6H12O6) opgebouwd?",
                "Uit 3 verschillende atoomsoorten (koolstof, waterstof en zuurstof)",
                [
                    "Uit 24 verschillende atoomsoorten, omdat elk atoom in de formule apart telt",
                    "Uit 6 verschillende atoomsoorten",
                    "Uit 12 verschillende atoomsoorten",
                ],
                "Een glucosemolecuul bevat 24 atomen in totaal, maar deze behoren tot slechts 3 verschillende atoomsoorten: C, H en O. (§2.2)",
            ),
            M(
                "Welke van de onderstaande stoffen is een niet-ontleedbare stof (element)?",
                "Zuurstofgas (O2), omdat de moleculen uit slechts één atoomsoort bestaan",
                [
                    "Koolstofdioxide (CO2), omdat het een volkomen kleurloos en reukloos samengesteld gas is",
                    "Keukenzout (NaCl), omdat het uit kleine kristallen bestaat",
                    "Water (H2O), omdat het een zuivere en neutrale vloeistof is",
                ],
                "Zuurstofgas (O2) bestaat uit één atoomsoort (alleen zuurstofatomen) en kan dus niet ontleed worden in andere stoffen. (§2.2)",
            ),
            M(
                "Van welke zeven elementen bestaan de moleculen in de natuur altijd uit twee aan elkaar gebonden atomen van dezelfde soort?",
                "Broom, jood, stikstof, chloor, waterstof, zuurstof en fluor",
                [
                    "IJzer, koper, goud, zilver, lood, tin en kwik",
                    "Helium, neon, argon, krypton, xenon, radon en oganesson",
                    "Koolstof, silicium, zwavel, fosfor, natrium, kalium en calcium",
                ],
                "De zeven twee-atomige elementen zijn Br2, I2, N2, Cl2, H2, O2 en F2 (handig te onthouden als BrINClHOF). (§2.2)",
            ),
            M(
                "Wat stelde de Engelse wetenschapper John Dalton aan het begin van de negentiende eeuw over atomen?",
                "Elke atoomsoort heeft zijn eigen massa en afmeting, en atomen kunnen niet worden vernietigd",
                [
                    "Atomen bestaan uit een positieve kern met daaromheen cirkelende elektronen",
                    "Atomen veranderen bij elke temperatuurstijging spontaan in een andere atoomsoort",
                    "Atomen zijn holle gasbellen die bij verhitting knappen en verdwijnen",
                ],
                "Dalton zag atomen als massieve, ondeelbare bolletjes die bij reacties niet verloren gaan maar alleen anders gerangschikt worden. (§2.2)",
            ),
            M(
                "Welke beweging voeren de deeltjes uit wanneer water bevroren is tot ijs?",
                "Ze zitten dicht op elkaar gepakt op een vaste plaats en trillen rondom hun evenwichtsstand",
                [
                    "Ze staan volkomen stil en vertonen absoluut geen enkele beweging",
                    "Ze vliegen kriskras door elkaar met snelheden van honderden meters per seconde",
                    "Ze bewegen vrij langs elkaar heen waardoor de stof direct vloeibaar wordt",
                ],
                "In een vaste stof kunnen moleculen niet van hun plek af; ze trillen voortdurend op hun vaste positie in het kristalrooster. (§2.1)",
            ),
            M(
                "Waarom kan een vloeistof zoals water wel vloeien en van vorm veranderen, maar niet zomaar worden samengeperst?",
                "De moleculen raken elkaar nog voortdurend aan, maar kunnen wel gemakkelijk langs elkaar heen glijden",
                [
                    "De moleculen raken elkaar helemaal niet meer aan en bewegen op grote afstand van elkaar",
                    "De moleculen breken bij het schenken direct af in losse atomen",
                    "De moleculen zetten bij elke beweging sterk uit waardoor het volume toeneemt",
                ],
                "In een vloeistof zitten de moleculen nog tegen elkaar aan (vast volume), maar ze hebben geen vaste plaats en glijden langs elkaar heen (geen vaste vorm). (§2.1)",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "Moleculen zijn de allerkleinste deeltjes in de natuur en kunnen met geen enkele chemische reactie verder gesplitst worden.",
                False,
                "Onwaar. Moleculen bestaan uit atomen; bij chemische reacties worden moleculen gesplitst en opnieuw gerangschikt. (§2.2)",
            ),
            W(
                "Er zijn in de natuur en laboratoria meer dan 10.000 verschillende atoomsoorten ontdekt.",
                False,
                "Onwaar. Er zijn circa 118 verschillende atoomsoorten bekend. (§2.2)",
            ),
            W(
                "Een molecuul waterstofgas (H2) bestaat uit twee identieke waterstofatomen die chemisch aan elkaar zijn verbonden.",
                True,
                "Waar. H2 is een twee-atomig molecuul van het element waterstof. (§2.2)",
            ),
            W(
                "Stoffen met dezelfde atoomsoorten kunnen toch heel verschillende eigenschappen hebben als de moleculen anders zijn opgebouwd.",
                True,
                "Waar. Bijvoorbeeld aceton en glucose, of koolstofmono-oxide en koolstofdioxide. (§2.2)",
            ),
            W(
                "In een vaste stof blijven moleculen op hun vaste plek, maar ze trillen wel voortdurend.",
                True,
                "Waar. Moleculen in een vaste stof staan nooit stil, ze trillen op hun plek. (§2.1)",
            ),
            # 4 Invul
            I(
                "Het symbool voor zilver is ____.",
                "Ag",
                "Zilver heeft het symbool Ag; het symbool begint met een andere letter dan de naam (§2.2).",
            ),
            I(
                "Eén triljoen is een 1 met precies ____ nullen." + GETAL,
                "18|achttien",
                "Eén triljoen is 1.000.000.000.000.000.000 (een 1 met 18 nullen). (§2.1)",
            ),
            I(
                "Het scheikundige symbool voor het edelmetaal goud is ____.",
                "Au",
                "Goud heeft het symbool Au (§2.2).",
            ),
            I(
                "Welk scheikundig elementsymbool hoort bij ijzer? ____",
                "Fe",
                "IJzer heeft het symbool Fe (§2.2).",
            ),
            # 1 Open
            O(
                "Leg in één korte zin uit waarom aceton (C3H6O) en glucose (C6H12O6) verschillende stoffen zijn, hoewel ze uit dezelfde atoomsoorten bestaan." + KORT,
                ["aantal/verhouding", "rangschikking/structuur/bouw/gerangschikt"],
                1,
                "Het aantal atomen per molecuul en de manier waarop de atomen gerangschikt zijn, verschillen.",
                "De eigenschappen verschillen doordat het aantal atomen en de rangschikking van de atomen in het molecuul anders zijn (§2.2).",
            ),
        ],
    ),
    65: (
        "2.2",
        "Toets 65 — §2.2 Herhaling B: Modellen, symbolen en formules",
        "🔬",
        [
            # 10 MC
            M(
                "In welk type molecuulmodel worden atomen weergegeven als bollen die direct tegen elkaar aan zitten, zonder zichtbare verbindingsstaafjes?",
                "In een space-filling model",
                [
                    "In een ball-and-stick model met dunne verbindingsstokjes",
                    "In een schematisch atoommodel van Rutherford",
                    "In een periodiek systeem der elementen",
                ],
                "In een space-filling model worden atomen weergegeven als bollen die elkaar direct overlappen en raken. (§2.2)",
            ),
            M(
                "Wat stellen de verbindingsstaafjes voor in een ball-and-stick model van een molecuul?",
                "De chemische bindingen waarmee de atomen aan elkaar vastzitten",
                [
                    "De banen waarin elektronen met lichtsnelheid rondcirkelen",
                    "De lege ruimtes tussen twee verschillende vloeistoffen",
                    "De temperatuurverschillen tussen de atomen in het molecuul",
                ],
                "In een ball-and-stick model stellen de bollen de atomen voor en de staafjes de chemische bindingen daartussen. (§2.2)",
            ),
            M(
                "Wat is het juiste scheikundige symbool voor het edelmetaal zilver?",
                "Ag",
                [
                    "Zi",
                    "Zv",
                    "Au",
                ],
                "Zilver heeft als chemisch symbool Ag; Au is het symbool van goud. (§2.2)",
            ),
            M(
                "Welk symbool hoort bij het zware giftige metaal lood?",
                "Pb",
                [
                    "Ld",
                    "Lo",
                    "Hg",
                ],
                "Lood heeft als symbool Pb; Hg is het symbool voor kwik. (§2.2)",
            ),
            M(
                "Welk scheikundig symbool hoort bij het vloeibare metaal kwik?",
                "Hg",
                [
                    "Kw",
                    "K (afgeleid van Kalium)",
                    "Sn",
                ],
                "Kwik heeft als symbool Hg; K is kalium en Sn is tin. (§2.2)",
            ),
            M(
                "In de scheikundige notatie 4 CO2, wat geven het getal 4 en het getal 2 precies aan?",
                "Er zijn 4 moleculen koolstofdioxide, en elk molecuul bevat 2 zuurstofatomen",
                [
                    "Er zijn 2 moleculen koolstofdioxide, en elk molecuul bevat 4 zuurstofatomen",
                    "Er zijn in totaal 4 atomen in het hele mengsel aanwezig",
                    "Het cijfer 4 geeft aan dat het mengsel 4 graden Celsius warm is",
                ],
                "Het getal vóór de formule geeft het aantal moleculen aan; het getal verlaagd rechtsonder geeft het aantal van die atoomsoort in één molecuul aan. (§2.2)",
            ),
            M(
                "Hoeveel atomen zitten er in totaal in 3 moleculen waterstofperoxide (3 H2O2)?",
                "12 atomen in totaal (6 waterstofatomen en 6 zuurstofatomen)",
                [
                    "4 atomen in totaal (2 waterstofatomen en 2 zuurstofatomen)",
                    "7 atomen in totaal (3 waterstof- en 4 zuurstofatomen)",
                    "6 atomen in totaal (3 moleculen van elk 2 atomen)",
                ],
                "Eén molecuul H2O2 bevat 2 + 2 = 4 atomen. In 3 moleculen zitten dus 3 × 4 = 12 atomen. (§2.2)",
            ),
            M(
                "Wat is het verschil in betekenis tussen het symbool O en de formule O2?",
                "O staat voor één los zuurstofatoom, O2 staat voor een molecuul zuurstofgas",
                [
                    "O is een vaste stof en O2 is altijd een vloeistof",
                    "O is een verbinding en O2 is een niet-ontleedbare stof",
                    "Er is geen enkel verschil, beide notaties betekenen exact hetzelfde",
                ],
                "O geeft de atoomsoort of één los atoom zuurstof aan; O2 is de molecuulformule van de zuivere stof zuurstofgas. (§2.2)",
            ),
            M(
                "Waarom is stikstofgas genoteerd als N2 en niet als losse N-atomen?",
                "Omdat stikstofatomen in de natuur altijd paarsgewijs een twee-atomig molecuul vormen",
                [
                    "Omdat stikstof alleen kan bestaan als het opgelost is in vloeibare stikstof",
                    "Omdat stikstof uit twee verschillende atoomsoorten is opgebouwd",
                    "Omdat het getal 2 aangeeft dat stikstof in periode 2 van het periodiek systeem staat",
                ],
                "Stikstof behoort tot de 7 twee-atomige elementen (BrINClHOF) waarvan de atomen altijd moleculen van twee atomen vormen. (§2.2)",
            ),
            M(
                "Wat weet je over de moleculen in een glas met zuiver gedestilleerd water?",
                "Alle moleculen zijn volkomen identiek aan elkaar (alleen H2O-moleculen)",
                [
                    "De moleculen zijn allemaal verschillend van grootte en samenstelling",
                    "De helft van de moleculen bestaat uit suiker en de andere helft uit zout",
                    "In zuiver water zitten helemaal geen moleculen, alleen losse elektronen",
                ],
                "Een zuivere stof bestaat op microniveau uit slechts één soort moleculen; alle moleculen in zuiver water zijn exact hetzelfde. (§2.1)",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "In een space-filling model worden chemische bindingen tussen atomen zichtbaar gemaakt met lange dunne staafjes.",
                False,
                "Onwaar. In een space-filling model zitten de atoombollen direct tegen elkaar gedrukt zonder staafjes; staafjes zitten in een ball-and-stick model. (§2.2)",
            ),
            W(
                "Het scheikundige symbool voor het metaal koper is Kp.",
                False,
                "Onwaar. Het symbool voor koper is Cu. (§2.2)",
            ),
            W(
                "Als een formule geen getal rechtsonder een atoomsymbool heeft staan (zoals de C in CO2), betekent dit dat dat atoom één keer in het molecuul voorkomt.",
                True,
                "Waar. Het getal 1 wordt in de scheikunde als index altijd weggelaten. (§2.2)",
            ),
            W(
                "Koper heeft als chemisch symbool Cu.",
                True,
                "Waar. Cu staat voor koper. (§2.2)",
            ),
            W(
                "In drie moleculen methaan (3 CH4) zitten in totaal vijftien atomen.",
                True,
                "Waar. 1 C + 4 H = 5 atomen per molecuul; 3 × 5 = 15 atomen. (§2.2)",
            ),
            # 4 Invul
            I(
                "In de formule 5 H2O noemt men het grote getal 5 dat vóór de formule staat de ____.",
                "coëfficiënt|coefficient",
                "De coëfficiënt geeft het aantal moleculen aan. (§2.2)",
            ),
            I(
                "In de formule H2O noemt men het kleine cijfer 2 dat verlaagd rechtsonder staat de ____.",
                "index",
                "De index geeft het aantal atomen van die soort in één molecuul aan. (§2.2)",
            ),
            I(
                "Hoeveel atomen zitten er in totaal in één molecuul H2O2?" + GETAL,
                "4|vier",
                "H2O2: 2 waterstofatomen + 2 zuurstofatomen = 4 atomen (§2.2).",
            ),
            I(
                "Tin wordt in reactievergelijkingen aangeduid met het symbool ____.",
                "Sn",
                "Tin heeft het symbool Sn (van Stannum). (§2.2)",
            ),
            # 1 Open
            O(
                "Wat is het verschil in weergave van een molecuul tussen een ball-and-stick model en een space-filling model?" + KORT,
                ["staafjes/stokjes/bindingen", "tegen elkaar/overlappen/aaneengesloten/raken"],
                1,
                "In een ball-and-stick model zijn bindingen staafjes; in een space-filling model zitten de bollen tegen elkaar.",
                "Een ball-and-stick model toont staafjes tussen de bollen; een space-filling model toont atomen direct tegen elkaar aan (§2.2).",
            ),
        ],
    ),
    66: (
        "mix",
        "Toets 66 — H2 Herhaling gemengd A: Begrippen, macro en micro",
        "🧪",
        [
            # 10 MC
            M(
                "Wat bedoelt een scheikundige precies met het 'microniveau' van een stof?",
                "De wereld van de allerkleinste deeltjes (moleculen en atomen) die je met geen enkele microscoop kunt zien",
                [
                    "Alles wat je met een gewone loep of een biologische microscoop kunt bekijken",
                    "Alle direct meetbare macroscopische stofeigenschappen die je met laboratoriumapparatuur rechtstreeks afleest",
                    "Een reageerbuis waarin een uiterst kleine hoeveelheid vloeistof wordt verwarmd",
                ],
                "Het microniveau beschrijft atomen en moleculen; deze deeltjes zijn zo onvoorstelbaar klein dat ze zelfs met de sterkste microscoop niet als gewone voorwerpen zichtbaar zijn. (§2.1)",
            ),
            M(
                "Welke van de onderstaande eigenschappen behoort tot het 'macroniveau' van een zuivere stof?",
                "De kooktemperatuur en de dichtheid die je met je zintuigen of meetinstrumenten kunt vaststellen",
                [
                    "Het feit dat de stof uit slechts één soort moleculen is opgebouwd",
                    "De specifieke ruimtelijke vorm waarin de atomen aan elkaar vastzitten",
                    "Het exacte aantal negatieve elektronen dat zich in de buitenste schil van de afzonderlijke atomen bevindt",
                ],
                "Het macroniveau omvat alles wat je direct met je zintuigen kunt waarnemen of meten (zoals fase, kleur, smaak en kookpunt). De moleculaire opbouw hoort bij het microniveau. (§2.1)",
            ),
            M(
                "Hoe verspreidt de geur van geurstokjes zich vanuit een flesje door een hele woonkamer?",
                "Ontelbare microscopisch kleine geurmoleculen verdampen en bewegen vrij door de lucht",
                [
                    "Eén enkel groot geurdeeltje stijgt op en blijft stil in het midden van de kamer hangen",
                    "De vloeistof zendt onzichtbare lichtstralen uit die de geurzenuwen prikkelen",
                    "De luchtmoleculen veranderen door een chemische reactie spontaan in parfum",
                ],
                "Geurstoffen bestaan uit vluchtige moleculen die verdampen en zich door willekeurige beweging (diffusie) tussen de luchtmoleculen verspreiden. (§2.1)",
            ),
            M(
                "Een vloeistofmonster bevat op microniveau drie verschillende soorten moleculen. Om wat voor soort stof gaat het?",
                "Om een mengsel van drie verschillende stoffen",
                [
                    "Om een niet-ontleedbare stof (element)",
                    "Om een zuivere stof met een vaste kooktemperatuur",
                    "Om een enkel molecuul dat in drie delen is gebroken",
                ],
                "Als een vloeistof verschillende soorten moleculen bevat, is het per definitie een mengsel van verschillende stoffen. (§2.1)",
            ),
            M(
                "Wat gebeurt er op microniveau wanneer je een lepel suiker oplost in warm water?",
                "De suikermoleculen laten los van de suikerkorrel en verdelen zich gelijkmatig tussen de watermoleculen",
                [
                    "De suikermoleculen vallen door de warmte volledig uiteen in losse koolstof-, waterstof- en zuurstofatomen",
                    "De suikermoleculen smelten samen tot één gigantisch suikeratoom",
                    "De watermoleculen veranderen door het roeren spontaan in zoete alcohol",
                ],
                "Bij het oplossen van suiker blijven de suikermoleculen intact; ze verspreiden zich homogeen tussen de watermoleculen tot een heldere oplossing. (§2.1)",
            ),
            M(
                "Waarom maken scheikundigen veelvuldig gebruik van modellen (zoals bolletjesmodellen)?",
                "Omdat moleculen en atomen veel te klein zijn om direct te zien en een model helpt processen te verklaren",
                [
                    "Omdat echte moleculen te zwaar zijn om veilig in een laboratorium te bewaren",
                    "Omdat een model altijd precies dezelfde massa en afmeting heeft als het echte deeltje",
                    "Omdat experimenten verboden zijn als er geen houten model van de stof aanwezig is",
                ],
                "Modellen zijn vereenvoudigde voorstellingen van de werkelijkheid die helpen om onzichtbare verschijnselen op microniveau begrijpelijk te maken. (§2.1)",
            ),
            M(
                "Hoe geef je de faseovergang van verdampende alcohol scheikundig correct weer in symbolen?",
                "alcohol (l) → alcohol (g)",
                [
                    "alcohol (s) → alcohol (l)",
                    "alcohol (g) → alcohol (s)",
                    "alcohol (l) → water (g) + suiker (s)",
                ],
                "Bij verdampen gaat een stof over van de vloeibare fase (l voor liquid) naar de gasvormige fase (g voor gas): alcohol (l) → alcohol (g). (§1.3 / §2.1)",
            ),
            M(
                "Welke faseovergang vindt plaats wanneer vast jood bij zachte verwarming direct overgaat in paarse damp zonder eerst vloeibaar te worden?",
                "Sublimeren (van vaste fase direct naar gasfase)",
                [
                    "Condenseren (van gasvormige fase naar vloeibare fase)",
                    "Verdampen (van vloeistoffase naar gasfase)",
                    "Rijpen (van gasfase direct naar vaste fase)",
                ],
                "Sublimeren is de directe overgang van vast naar gas. Rijpen is het omgekeerde proces (gas naar vast). (§1.3 / §2.1)",
            ),
            M(
                "Een leerling meet tijdens het verwarmen van een zuivere stof elke minuut de temperatuur: 20 °C, 35 °C, 50 °C, 50 °C, 50 °C, 65 °C. Wat is het smeltpunt?",
                "50 °C, want tijdens de faseovergang van een zuivere stof blijft de temperatuur constant",
                [
                    "65 °C, omdat dit het hoogste getal uit de meetreeks is",
                    "20 °C, omdat elke zuivere stof begint te smelten bij kamertemperatuur",
                    "35 °C, omdat dit het gemiddelde is van de eerste twee metingen",
                ],
                "Bij een zuivere stof blijft de temperatuur tijdens het smelten gelijk (een horizontaal stuk in de grafiek). De constante waarde van 50 °C is dus het smeltpunt. (§1.3)",
            ),
            M(
                "Wat gebeurt er met de temperatuur wanneer je een vloeibaar mengsel (zoals wijn) aan de kook brengt en laat doorkoken?",
                "De temperatuur loopt tijdens het koken langzaam op doordat de samenstelling verandert",
                [
                    "De temperatuur blijft exact constant op één vaste kooktemperatuur",
                    "De temperatuur daalt direct terug naar het vriespunt van water",
                    "De vloeistof kookt zonder dat er enige warmte aan te pas komt",
                ],
                "Een mengsel heeft geen vast kookpunt maar een kooktraject: tijdens het koken stijgt de temperatuur geleidelijk doordat de stofsamenstelling verandert. (§1.3)",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "In een zuivere vloeistof zijn alle moleculen exact aan elkaar gelijk.",
                True,
                "Waar. Een zuivere stof bevat slechts één soort moleculen. (§2.1)",
            ),
            W(
                "Tijdens het koken van zuiver water blijft de temperatuur constant op 100 °C zolang er water verdampt.",
                True,
                "Waar. Zuiver water heeft een vast kookpunt van 100 °C. (§1.3)",
            ),
            W(
                "Wanneer een mengsel stolt, blijft de temperatuur gedurende het hele stolproces volkomen gelijk.",
                False,
                "Onwaar. Een mengsel heeft een stoltraject; de temperatuur zakt tijdens het stollen langzaam. (§1.3)",
            ),
            W(
                "Het microniveau omvat stofeigenschappen die je gemakkelijk met een eenvoudige handloep kunt zien.",
                False,
                "Onwaar. Moleculen zijn veel te klein voor een loep of gewone microscoop. (§2.1)",
            ),
            W(
                "In een gas bewegen de moleculen met grote snelheid kriskras door elkaar en botsen ze voortdurend.",
                True,
                "Waar. Gasdeeltjes hebben grote onderlinge afstanden en bewegen vrij. (§2.1)",
            ),
            # 4 Invul
            I(
                "De faseovergang waarbij een vloeistof verandert in een vaste stof noemen we ____.",
                "stollen|het stollen",
                "Stollen is de faseovergang van vloeibaar naar vast. (§1.3)",
            ),
            I(
                "Een getal met een 1 en achttien nullen heet een ____.",
                "triljoen",
                "Een 1 met 18 nullen is een triljoen — niet 6 of 12 nullen (§2.1).",
            ),
            I(
                "De vaste temperatuur waarbij een zuivere vloeistof overgaat in een gas, noemen we het ____.",
                "kookpunt",
                "Een zuivere stof heeft een vast kookpunt. (§1.3)",
            ),
            I(
                "Wanneer een mengsel geleidelijk overgaat van vloeistof naar gas over een temperatuurgebied, spreken we van een ____.",
                "kooktraject",
                "Een mengsel heeft een kooktraject in plaats van een vast kookpunt. (§1.3)",
            ),
            # 1 Open
            O(
                "Waarom vertoont de temperatuur-tijdgrafiek van een smeltende zuivere stof een horizontaal stuk, terwijl die van een mengsel schuin omhooggaat?" + KORT,
                ["smeltpunt/vaste temperatuur/constant", "smelttraject/traject/oploopt/stijgt"],
                1,
                "Een zuivere stof smelt bij één vaste constante temperatuur, terwijl een mengsel een smelttraject heeft waarbij de temperatuur oploopt.",
                "Een zuivere stof heeft een scherp smeltpunt (constante temperatuur); een mengsel heeft een smelttraject (§1.3).",
            ),
        ],
    ),
    67: (
        "mix",
        "Toets 67 — H2 Herhaling gemengd B: Atomen, isotopen en massa",
        "⚖️",
        [
            # 10 MC
            M(
                "Wat bereken je door de relatieve atoommassa's van alle atomen in een molecuul bij elkaar op te tellen?",
                "De molecuulmassa van de stof in atomaire massa-eenheden (u)",
                [
                    "Het totale aantal protonen in de atoomkernen van het molecuul",
                    "Het kookpunt van de vloeistof in graden Celsius",
                    "De dichtheid van de stof in gram per kubieke centimeter",
                ],
                "De molecuulmassa (in u) is gelijk aan de som van de atoommassa's van alle atomen waaruit het molecuul bestaat. (§2.3 / §2.4)",
            ),
            M(
                "Wat zijn isotopen van een bepaalde atoomsoort?",
                "Atomen met hetzelfde aantal protonen, maar een verschillend aantal neutronen in de kern",
                [
                    "Atomen met hetzelfde aantal neutronen, maar een verschillend aantal protonen",
                    "Moleculen die bestaan uit dezelfde atomen maar een andere kleur hebben",
                    "Atomen die spontaan veranderen in edelgassen bij kamertemperatuur",
                ],
                "Isotopen zijn atomen van dezelfde atoomsoort (zelfde aantal protonen / atoomnummer) met een andere massa door een afwijkend aantal neutronen in de kern. (§2.4)",
            ),
            M(
                "Waarom staat bij chloor in het periodiek systeem een atoommassa van 35,45 u en geen heel getal?",
                "Omdat het een gewogen gemiddelde is van de in de natuur voorkomende isotopen van chloor",
                [
                    "Omdat chlooratomen voortdurend stukjes van hun protonen verliezen",
                    "Omdat een chlooratoom precies 35 protonen en 0,45 elektronen bevat",
                    "Omdat de massa van een elektron gelijk is aan 0,45 u",
                ],
                "In de natuur komen twee chloorisotopen voor (Cl-35 en Cl-37). De atoommassa van 35,45 u is het gemiddelde op basis van hoe vaak elke isotoop voorkomt. (§2.4)",
            ),
            M(
                "Welke subatomaire deeltjes bevinden zich samen in de atoomkern van een atoom?",
                "De positief geladen protonen en de neutrale neutronen",
                [
                    "De negatief geladen elektronen en de neutrale neutronen",
                    "Uitsluitend de negatief geladen elektronen",
                    "Alleen losse moleculen die met staafjes zijn verbonden",
                ],
                "De atoomkern bestaat uit protonen (positief geladen) en neutronen (geen lading). De elektronen bewegen in de elektronenwolk rondom de kern. (§2.4)",
            ),
            M(
                "Een atoom van de atoomsoort natrium bezit 11 protonen en 12 neutronen in de kern. Wat is het massagetal van dit natriumatoom?",
                "23 (namelijk 11 protonen + 12 neutronen)",
                [
                    "11 (alleen het aantal protonen)",
                    "1 (het verschil tussen neutronen en protonen)",
                    "132 (het product van protonen en neutronen)",
                ],
                "massagetal = aantal protonen + aantal neutronen = 11 + 12 = 23. (§2.4)",
            ),
            M(
                "Een neutraal atoom van koolstof heeft atoomnummer 6. Hoeveel elektronen bewegen er in de elektronenwolk rondom de kern?",
                "Precies 6 elektronen, want in een neutraal atoom is het aantal elektronen gelijk aan het aantal protonen",
                [
                    "12 elektronen, want koolstof heeft massagetal 12",
                    "0 elektronen, omdat een neutraal atoom geen ladingdragers heeft",
                    "18 elektronen, overeenkomend met het edelgas argon",
                ],
                "In een elektrisch neutraal atoom compenseert de negatieve lading van de elektronen precies de positieve lading van de protonen. Er zijn dus evenveel elektronen als protonen. (§2.4)",
            ),
            M(
                "Bereken de molecuulmassa van water (H2O). Gegeven zijn de atoommassa's: H = 1,01 u en O = 16,00 u.",
                "18,02 u",
                [
                    "17,01 u",
                    "33,01 u",
                    "16,00 u",
                ],
                "molecuulmassa H2O = (2 × 1,01 u) + (1 × 16,00 u) = 2,02 + 16,00 = 18,02 u. (§2.3)",
            ),
            M(
                "Bereken de molecuulmassa van koolstofdioxide (CO2). Gegeven: C = 12,01 u en O = 16,00 u.",
                "44,01 u",
                [
                    "28,01 u",
                    "56,02 u",
                    "32,00 u",
                ],
                "molecuulmassa CO2 = 12,01 u + (2 × 16,00 u) = 12,01 + 32,00 = 44,01 u. (§2.3)",
            ),
            M(
                "Wat bepaalt tot welke atoomsoort een bepaald atoom behoort?",
                "Het unieke aantal protonen in de atoomkern (het atoomnummer)",
                [
                    "Het totale aantal neutronen aanwezig in de kernen van alle isotopen",
                    "De aggregatietoestand waarin de stof verkeert",
                    "De grootte van de reageerbuis waarin het atoom zich bevindt",
                ],
                "Het aantal protonen (atoomnummer) is uniek voor elke atoomsoort: elk atoom met 6 protonen is altijd koolstof, elk atoom met 7 protonen is altijd stikstof. (§2.4)",
            ),
            M(
                "Welke elektrische lading hebben protonen, neutronen en elektronen respectievelijk?",
                "Protonen zijn positief (1+), neutronen zijn neutraal (0) en elektronen zijn negatief (1−)",
                [
                    "Protonen zijn negatief (1−), neutronen zijn positief (1+) en elektronen zijn neutraal (0)",
                    "Alle drie de deeltjes hebben exact dezelfde positieve elektrische lading",
                    "Protonen zijn neutraal (0), neutronen zijn negatief (1−) en elektronen zijn positief (1+)",
                ],
                "Protonen hebben lading 1+, elektronen hebben lading 1- en neutronen zijn ongeladen (neutraal). (§2.4)",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "Twee isotopen van dezelfde atoomsoort hebben altijd exact hetzelfde aantal protonen in de kern.",
                True,
                "Waar. Het aantal protonen bepaalt de atoomsoort en is voor alle isotopen gelijk. (§2.4)",
            ),
            W(
                "De massa van een elektron is ongeveer even groot als de massa van een proton.",
                False,
                "Onwaar. Een proton is bijna 2000 keer zo zwaar als een elektron; de elektronenmassa is verwaarloosbaar. (§2.4)",
            ),
            W(
                "In het periodiek systeem der elementen zijn alle atoomsoorten gerangschikt op oplopend atoomnummer.",
                True,
                "Waar. Het atoomnummer loopt op van 1 bij waterstof tot 118 bij oganesson. (§2.2 / §2.4)",
            ),
            W(
                "Het massagetal van een atoom is gelijk aan het aantal protonen vermenigvuldigd met het aantal elektronen.",
                False,
                "Onwaar. Het massagetal is de som van het aantal protonen en het aantal neutronen. (§2.4)",
            ),
            W(
                "De atomaire massa-eenheid u wordt gebruikt omdat de massa van atomen in grammen onpraktisch klein is.",
                True,
                "Waar. 1 u is ongeveer 1,66 × 10^-27 kg. (§2.3 / §2.4)",
            ),
            # 4 Invul
            I(
                "Bereken de molecuulmassa van ammoniak (NH3). Gegeven: N = 14,01 u en H = 1,01 u." + GETAL,
                "17,04|17.04|17,04 u|17.04 u",
                "molecuulmassa NH3 = 14,01 + (3 × 1,01) = 17,04 u. (§2.3)",
            ),
            I(
                "Een atoom van de isotoop koolstof-14 (C-14) heeft atoomnummer 6 en massagetal 14. Hoeveel neutronen zitten er in de kern van dit atoom?" + GETAL,
                "8|acht",
                "aantal neutronen = massagetal − atoomnummer = 14 − 6 = 8. (§2.4)",
            ),
            I(
                "Wat is de totale massa in u van één methaanmolecuul (CH4)? Gegeven: C = 12,01 u en H = 1,01 u." + GETAL,
                "16,05|16.05|16,05 u|16.05 u",
                "molecuulmassa CH4 = 12,01 + (4 × 1,01) = 16,05 u. (§2.3)",
            ),
            I(
                "Een fluoratoom heeft atoomnummer 9 en massagetal 19. Hoeveel neutronen bevat de kern van dit fluoratoom?" + GETAL,
                "10|tien",
                "aantal neutronen = massagetal − atoomnummer = 19 − 9 = 10. (§2.4)",
            ),
            # 1 Open
            O(
                "Leg in één korte zin uit wat het verschil is tussen het atoomnummer en het massagetal van een atoom." + KORT,
                ["protonen", "neutronen/kerndeeltjes/som/totaal"],
                1,
                "Het atoomnummer is het aantal protonen, terwijl het massagetal de som van protonen en neutronen is.",
                "Atoomnummer = aantal protonen in de kern; massagetal = totale aantal protonen plus neutronen in de kern (§2.4).",
            ),
        ],
    ),
}

if __name__ == "__main__":
    schrijf(EXAMENS, seed=20261110, hf=2)
