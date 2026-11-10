#!/usr/bin/env python3
"""Scheikunde HAVO 3 (H1) — Zwakte-toetsen 51–53 voor §1.4 Soorten mengsels en pH (TASK-43).
- Toets 51 (§1.4 A): Oplossingen, suspensies en troebele mengsels
- Toets 52 (§1.4 B): Emulsies, emulgatoren en ontmengen
- Toets 53 (§1.4 C): De pH-schaal, zuren, basen en indicatoren

Schrijft:
  havo3/scheikunde/js/data/examen_h1_51.js
  havo3/scheikunde/js/data/examen_h1_52.js
  havo3/scheikunde/js/data/examen_h1_53.js
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_scheikunde_h1_lib import M, W, I, O, schrijf, KORT, GETAL

EXAMENS = {
    51: (
        "1.4",
        "Toets 51 — §1.4 A: Oplossingen, suspensies en troebele mengsels",
        "🧪",
        [
            # 10 MC
            M(
                "Wat is een belangrijk gemeenschappelijk kenmerk van alle vloeibare oplossingen?",
                "Ze zijn volkomen helder, ongeacht of ze kleurloos of gekleurd zijn",
                [
                    "Ze zijn altijd kleurloos en laten nooit enige lichtstraal door",
                    "Ze bevatten uitsluitend vloeistoffen en nooit opgeloste vaste stoffen",
                    "Ze ontmengen vanzelf wanneer je ze een paar uur rustig laat staan",
                ],
                "Een oplossing is altijd helder (doorzichtig); je kunt erdoorheen kijken. Een oplossing kan kleurloos zijn (zoals kraanwater), maar ook gekleurd (zoals thee of limonade). (§1.4)",
            ),
            M(
                "Duru bekijkt een bekerglas met rode limonadesiroop gemengd met water. Het mengsel is donkerrood en helder. Welke conclusie is juist?",
                "Het is een oplossing, want de vloeistof is helder en doorzichtig",
                [
                    "Het is een suspensie, want een oplossing kan nooit een rode kleur hebben",
                    "Het is een emulsie, want er zitten twee verschillende kleurstoffen in",
                    "Het is een zuivere stof, want er zweven geen zichtbare deeltjes in",
                ],
                "Limonade is een helder mengsel waar je doorheen kunt kijken; het is dus een oplossing. Oplossingen hoeven niet kleurloos te zijn. (§1.4)",
            ),
            M(
                "In een versgeperst glas sinaasappelsap zweven fijne deeltjes vruchtvlees rond. Waarom noemen we dit mengsel een suspensie?",
                "Het is een troebel mengsel van een vaste stof fijn verdeeld in een vloeistof",
                [
                    "Het is een helder mengsel waarin de suikers volledig zijn neergeslagen",
                    "Het is een emulsie van twee vloeistoffen die door schudden niet mengen",
                    "Het is een nevel waarbij microscopisch kleine gasbellen zijn opgesloten",
                ],
                "Een suspensie is een troebel mengsel van een vaste stof (het vruchtvlees) in een vloeistof. (§1.4)",
            ),
            M(
                "Wat gebeurt er als je een reageerbuis met een suspensie van fijn krijtpoeder in water een dag op een rekje laat staan?",
                "De zwaardere krijtdeeltjes zakken naar de bodem en vormen een bezinksel",
                [
                    "De krijtdeeltjes lossen na verloop van tijd volledig op in het water",
                    "De krijtdeeltjes stijgen op en vormen een drijvende schuimkraag bovenop",
                    "De suspensie verandert vanzelf in een heldere, blauw gekleurde vloeistof",
                ],
                "In een suspensie lossen de vaste deeltjes niet op; door de zwaartekracht zakken ze na verloop van tijd naar de bodem (bezinken). (§1.4)",
            ),
            M(
                "Boven een brandende houtkachel zie je donkere rook opstijgen. Welke omschrijving van rook is scheikundig juist?",
                "Rook is een mengsel van fijne vaste stofdeeltjes zwevend in een gas",
                [
                    "Rook is een mengsel van fijne vloeistofdruppeltjes zwevend in een gas",
                    "Rook is een mengsel van twee gassen die niet goed met elkaar mengen",
                    "Rook is een helder gas waarin uitsluitend zuurstofmoleculen bewegen",
                ],
                "Rook bestaat uit zeer kleine vaste roetdeeltjes (vaste stof) die fijn verdeeld zijn in een gas (zoals lucht). (§1.4)",
            ),
            M(
                "Op een frisse herfstochtend hangt er dichte mist boven het weiland. Welk type mengsel is mist?",
                "Een nevel, want het zijn kleine vloeistofdruppels fijn verdeeld in een gas",
                [
                    "Een rook, want het zijn vaste ijsdeeltjes die in de lucht zweven",
                    "Een schuim, want er zitten gasbellen opgesloten in een vloeistoflaag",
                    "Een oplossing, want waterdamp is een helder en doorzichtig gas",
                ],
                "Mist is een nevel: zeer fijne vloeistofdruppeltjes water verdeeld in een gas (de buitenlucht). (§1.4)",
            ),
            M(
                "Tijdens een afwas ontstaat er een dikke laag bad- of afwasschuim. Wat is schuim precies?",
                "Een mengsel van een gas dat fijn verdeeld is in een vloeistof of vaste stof",
                [
                    "Een mengsel van twee vloeistoffen die elkaar voortdurend afstoten",
                    "Een troebel mengsel van een vaste stof fijn verdeeld in een gas",
                    "Een heldere oplossing waarin zeepdeeltjes volledig zijn opgelost",
                ],
                "Schuim is een mengsel waarin gasbellen fijn verdeeld zijn in een vloeistof (zoals zeepsop) of een vaste stof (zoals piepschuim). (§1.4)",
            ),
            M(
                "In de keuken wordt vloeibaar schuurmiddel gebruikt om een kookplaat schoon te maken. Waarom is dit schuurmiddel een suspensie?",
                "Het bevat microscopisch kleine vaste schuurkorrels die zweven in een vloeistof",
                [
                    "Het bestaat uit twee vloeistoffen die met een emulgator zijn gemengd",
                    "Het is een heldere oplossing waarin alle zouten geheel zijn opgelost",
                    "Het bevat gasbellen die in een harde vaste stof zijn ingekapseld",
                ],
                "Schuurmiddel is een suspensie: vaste schuurdeeltjes (zoals kalk- of krijtpoeder) die fijn verdeeld zijn in een vloeistof. (§1.4)",
            ),
            M(
                "Een maatcilinder bevat 40 mL van een heldere vloeistof. De massa van deze vloeistof is 32 g. Wat is de dichtheid?",
                "0,80 g/cm³",
                [
                    "1,30 g/cm³",
                    "72 g/cm³",
                    "0,08 g/cm³",
                ],
                "dichtheid = massa / volume = 32 g / 40 cm³ = 0,80 g/cm³ (onthoud: 1 mL = 1 cm³). (§1.1)",
            ),
            M(
                "In de winter slaat waterdamp uit de lucht bij temperaturen onder nul direct neer als witte ijskristallen op het gras. Hoe heet deze faseovergang?",
                "Rijpen",
                [
                    "Sublimeren",
                    "Condenseren",
                    "Stollen",
                ],
                "Rijpen is de directe faseovergang van de gasvormige fase naar de vaste fase (gas → vast). Sublimeren is precies andersom (vast → gas). (§1.3)",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "Een vloeibare oplossing is altijd een kleurloze vloeistof.",
                False,
                "Onwaar. Een oplossing kan zowel kleurloos (zoals water met zout) als gekleurd zijn (zoals thee of limonade). Het belangrijkste kenmerk is dat een oplossing helder is. (§1.4)",
            ),
            W(
                "In een suspensie zijn de deeltjes zo klein dat het mengsel altijd helder en doorzichtig blijft.",
                False,
                "Onwaar. Een suspensie is altijd een troebel mengsel; de vaste deeltjes zijn groot genoeg om het licht te verstrooien, waardoor je er niet doorheen kunt kijken. (§1.4)",
            ),
            W(
                "Haarlak die uit een spuitbus als fijne vloeistofdruppels in de lucht wordt gespoten, vormt een nevel.",
                True,
                "Waar. Een nevel is een mengsel van kleine vloeistofdruppeltjes fijn verdeeld in een gas (de lucht). (§1.4)",
            ),
            W(
                "Als je een troebel mengsel van zand en water met rust laat, zullen de zandkorrels na verloop van tijd naar de bodem zakken.",
                True,
                "Waar. Doordat de vaste deeltjes in een suspensie relatief zwaar zijn, zakken ze onder invloed van de zwaartekracht naar de bodem (bezinken). (§1.4)",
            ),
            W(
                "Slagroom op een taart is een voorbeeld van een schuim, omdat er luchtbelletjes in de room zijn geklopt.",
                True,
                "Waar. Schuim ontstaat wanneer een gas (zoals lucht) fijn verdeeld raakt in een vloeistof of vaste stof. (§1.4)",
            ),
            # 4 Invul
            I(
                "Een massief blokje kunststof heeft een massa van 150 g en een volume van 120 cm³. Bereken de dichtheid in g/cm³." + GETAL,
                "1,25|1.25|1,25 g/cm³|1.25 g/cm³",
                "ρ = m / V = 150 / 120 = 1,25 g/cm³. (§1.1)",
            ),
            I(
                "Vloeibare stikstof kookt bij een temperatuur van 77 K. Hoeveel graden Celsius (°C) is dat?" + GETAL,
                "-196|−196|-196 °C",
                "°C = K − 273 = 77 − 273 = −196 °C. (§1.3)",
            ),
            I(
                "Een maatbeker bevat 0,35 liter water. Hoeveel milliliter (mL) is dit volume?" + GETAL,
                "350|350 mL|350 ml",
                "1 L = 1000 mL, dus 0,35 L = 0,35 × 1000 = 350 mL. (§1.1)",
            ),
            I(
                "Hoeveel kubieke centimeter (cm³) is een volume van precies 250 mL?" + GETAL,
                "250|250 cm³|250 cm3",
                "1 mL is precies gelijk aan 1 cm³, dus 250 mL is 250 cm³. (§1.1)",
            ),
            # 1 Open
            O(
                "Leg in één zin uit wat het zichtbare verschil is tussen een oplossing en een suspensie als je erdoorheen probeert te kijken." + KORT,
                ["helder/doorzichtig", "troebel/ondoorschijnend"],
                2,
                "Een oplossing is helder zodat je erdoorheen kijkt, terwijl een suspensie troebel is en het licht tegenhoudt.",
                "Een oplossing is helder (doorzichtig); een suspensie is troebel waardoor je er niet doorheen kunt kijken. (§1.4)",
            ),
        ],
    ),
    52: (
        "1.4",
        "Toets 52 — §1.4 B: Emulsies, emulgatoren en ontmengen",
        "🧪",
        [
            # 10 MC
            M(
                "Wat is volgens de scheikunde de juiste omschrijving van een emulsie?",
                "Een troebel mengsel van twee vloeistoffen die van nature niet goed mengen",
                [
                    "Een heldere vloeistof waarin een vaste stof volledig is opgelost en verdeeld",
                    "Een mengsel van een gas dat fijn verdeeld is in een vloeistof",
                    "Een troebel mengsel van een vaste stof fijn verdeeld in een gas",
                ],
                "Een emulsie is een troebel mengsel van twee vloeistoffen die elkaar afstoten of niet vanzelf mengen, zoals olie en water. (§1.4)",
            ),
            M(
                "Als je slaolie en kraanwater zonder extra toevoeging flink schudt in een reageerbuis, ontstaat een troebel mengsel. Wat gebeurt er na een uur rust?",
                "Het mengsel scheidt zich weer vanzelf in twee afzonderlijke vloeistoflagen",
                [
                    "De olie en het water blijven blijvend gemengd als een heldere en kleurloze vloeistof",
                    "De olie zakt als vaste korrels naar de bodem van de reageerbuis",
                    "Het mengsel verdampt plotseling volledig door een chemische reactie",
                ],
                "Zonder emulgator is een emulsie niet stabiel; na enige tijd treedt ontmenging op en zie je weer twee aparte lagen. (§1.4)",
            ),
            M(
                "Wanneer een mengsel van plantaardige olie en water ontmengt, gaat de olie altijd bovenop drijven. Wat is hiervan de oorzaak?",
                "Plantaardige olie heeft een kleinere dichtheid dan water",
                [
                    "Plantaardige olie heeft een veel grotere dichtheid dan water",
                    "Plantaardige olie heeft een lagere kooktemperatuur dan water",
                    "Plantaardige olie lost sneller op in de omringende lucht",
                ],
                "Een stof met een lagere dichtheid drijft op een vloeistof met een hogere dichtheid. Omdat olie een kleinere dichtheid heeft dan water (ongeveer 0,9 g/cm³ tegenover 1,0 g/cm³), vormt olie de bovenlaag. (§1.4)",
            ),
            M(
                "Wat is de exacte functie van een emulgator in een mengsel van water en olie?",
                "Het zorgt ervoor dat de vloeistoffen fijn verdeeld blijven en niet ontmengen",
                [
                    "Het lost de vetdeeltjes volledig op zodat er een heldere, kleurloze vloeistof ontstaat",
                    "Het zorgt ervoor dat de vloeistof met de kleinste dichtheid direct zinkt",
                    "Het laat de vaste deeltjes in het mengsel veel sneller bezinken",
                ],
                "Een emulgator is een hulpstof die de vloeistofdruppels in een emulsie omhult, waardoor de twee vloeistoffen niet ontmengen maar gemengd blijven. (§1.4)",
            ),
            M(
                "Bij het bereiden van mayonaise wordt olie met azijn gemengd. Welke stof voegt de kok toe als natuurlijke emulgator?",
                "Eigeel, want daarin zitten stoffen die olie en water binden",
                [
                    "Kristalsuiker, want dat lost alle vette bestanddelen direct op in de azijn",
                    "Keukenzout, want dat verhoogt de kooktemperatuur van water",
                    "Extra azijn, want een zuur mengt van nature met alle oliën",
                ],
                "In mayonaise fungeert eigeel (met name de stof lecithine) als emulgator om de olie en het waterige azijnmengsel stabiel gemengd te houden. (§1.4)",
            ),
            M(
                "Welke uitspraak over een emulgator is scheikundig juist?",
                "Een emulgator houdt een emulsie stabiel, maar maakt er geen oplossing van",
                [
                    "Een emulgator maakt van elke troebele suspensie direct een volkomen heldere oplossing",
                    "Een emulgator zorgt ervoor dat watermoleculen spontaan ontleden in gassen",
                    "Een emulgator werkt alleen als je het mengsel verwarmt tot boven 100 °C",
                ],
                "Een emulgator houdt de vloeistoffen in een emulsie gemengd, maar de vloeistof blijft troebel; het wordt nooit een heldere oplossing. (§1.4)",
            ),
            M(
                "Welk van de onderstaande producten uit het dagelijks leven is een voorbeeld van een emulsie?",
                "Cosmetische huidcrème, waarin vette bestanddelen en water zijn gemengd",
                [
                    "Helder appelsap, waarin suikers, zuren en aroma's volledig zijn opgelost in water",
                    "Bier, waarin alcohol en water een helder doorzichtig mengsel vormen",
                    "Kraanwater, waarin uitsluitend opgeloste mineralen aanwezig zijn",
                ],
                "Huidcrème (en ook melk en mayonaise) is een emulsie van olie/vet en water met een emulgator. Helder appelsap en bier zijn oplossingen. (§1.4)",
            ),
            M(
                "In sportfietsen wordt carbonfiber gebruikt (koolstofvezels ingebed in een harde kunststofhars). Waarom is carbonfiber géén emulsie?",
                "Omdat het bestaat uit vaste vezels in een vaste kunststof en niet uit twee vloeistoffen",
                [
                    "Omdat carbonfiber een zuivere stof is die bestaat uit één atoomsoort",
                    "Omdat carbonfiber na verloop van tijd spontaan ontmengt in twee afzonderlijke vloeistoflagen",
                    "Omdat het materiaal volkomen helder en lichtdoorlatend is",
                ],
                "Carbonfiber is een bijzonder composietmateriaal van vaste vezels in kunststof (epoxy). Een emulsie bestaat daarentegen altijd uit twee vloeistoffen. (§1.4)",
            ),
            M(
                "Een kolf bevat 250 cm³ zonnebloemolie met een dichtheid van 0,92 g/cm³. Bereken de massa van deze olie.",
                "230 g",
                [
                    "272 g",
                    "22,5 g",
                    "250 g",
                ],
                "massa = dichtheid × volume = 0,92 g/cm³ × 250 cm³ = 230 g. (§1.1)",
            ),
            M(
                "Kaarsvet heeft een stoltraject tussen 52 °C en 58 °C. Wat kun je hieruit concluderen over de samenstelling van dit kaarsvet?",
                "Het is een mengsel van meerdere stoffen",
                [
                    "Het is een zuivere stof met een scherp stolpunt",
                    "Het is een emulsie die bij kamertemperatuur ontmengt",
                    "Het is een suspensie waarin vaste korrels bezinken",
                ],
                "Een zuivere stof heeft een vast smelt- of stolpunt (één constante temperatuur). Als er sprake is van een traject waarin de temperatuur verloopt, is het een mengsel. (§1.3)",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "Een emulgator zorgt ervoor dat twee vloeistoffen die elkaar normaal afstoten toch stabiel gemengd blijven.",
                True,
                "Waar. Dat is precies de werking van een emulgator (zoals eigeel in mayonaise). (§1.4)",
            ),
            W(
                "Bij het ontmengen van een mengsel van benzine en water vormt de vloeistof met de grootste dichtheid de bovenste laag.",
                False,
                "Onwaar. De vloeistof met de kleinste dichtheid drijft bovenop; de stof met de grootste dichtheid zakt omlaag. (§1.4)",
            ),
            W(
                "Volle melk is een troebel mengsel van kleine vetdruppeltjes in water en is daardoor een emulsie.",
                True,
                "Waar. Melk bestaat uit microscopisch kleine vetbolletjes die in water verdeeld zijn en door eiwitten gemengd worden gehouden. (§1.4)",
            ),
            W(
                "Door toevoegen van een emulgator verandert een troebele emulsie in een heldere oplossing.",
                False,
                "Onwaar. Een emulgator voorkomt alleen het ontmengen; het mengsel blijft troebel en wordt nooit een doorzichtige oplossing. (§1.4)",
            ),
            W(
                "Wanneer twee vloeistoffen zoals zuivere alcohol en water mengen tot een heldere vloeistof, noem je dit een oplossing.",
                True,
                "Waar. Mengsels van vloeistoffen die volkomen helder zijn en waarin je niet door troebeling wordt gehinderd, zijn oplossingen. (§1.4)",
            ),
            # 4 Invul
            I(
                "Een fles bevat 500 cm³ lampenolie met een dichtheid van 0,82 g/cm³. Bereken de massa van de lampenolie in gram." + GETAL,
                "410|410 g",
                "m = ρ × V = 0,82 × 500 = 410 g. (§1.1)",
            ),
            I(
                "Zuiver azijnzuur smelt bij 290 K. Hoeveel graden Celsius (°C) is dat?" + GETAL,
                "17|17 °C|17°C",
                "°C = K − 273 = 290 − 273 = 17 °C. (§1.3)",
            ),
            I(
                "Een smeerolie heeft een dichtheid van 0,88 g/cm³. Hoeveel kg/m³ is dat?" + GETAL,
                "880|880 kg/m³|880 kg/m3",
                "Omrekenen van g/cm³ naar kg/m³ doe je door te vermenigvuldigen met 1000: 0,88 × 1000 = 880 kg/m³. (§1.1)",
            ),
            I(
                "Een vloeistofmonster heeft een massa van 184 g en een dichtheid van 0,92 g/cm³. Bereken het volume in cm³." + GETAL,
                "200|200 cm³|200 cm3",
                "V = m / ρ = 184 / 0,92 = 200 cm³. (§1.1)",
            ),
            # 1 Open
            O(
                "Leg in één zin uit waarom een kok eigeel toevoegt bij het bereiden van mayonaise." + KORT,
                ["emulgator/ontmengen", "stabiel/gemengd"],
                1,
                "Eigeel dient als emulgator zodat de olie en het water niet ontmengen maar gemengd blijven.",
                "Eigeel werkt als emulgator en voorkomt dat de olie en het waterige azijn ontmengen in twee lagen. (§1.4)",
            ),
        ],
    ),
    53: (
        "1.4",
        "Toets 53 — §1.4 C: De pH-schaal, zuren, basen en indicatoren",
        "🧪",
        [
            # 10 MC
            M(
                "Welke pH-waarde heeft een volkomen neutrale vloeistof bij kamertemperatuur, zoals zuiver water?",
                "Precies pH 7",
                [
                    "Precies pH 0",
                    "Precies pH 14",
                    "Ongeveer pH 3",
                ],
                "Neutrale oplossingen hebben een pH van precies 7. Waarden onder 7 zijn zuur en waarden boven 7 zijn basisch. (§1.4)",
            ),
            M(
                "Vier bekers bevatten verschillende vloeistoffen: beker P heeft pH 1, beker Q heeft pH 4, beker R heeft pH 7 en beker S heeft pH 11. Welke beker bevat de meest zure vloeistof?",
                "Beker P met pH 1, want hoe lager de pH, des te zuurder de vloeistof",
                [
                    "Beker S met pH 11, want hoe hoger het getal op de schaal, des te sterker de zuurgraad is",
                    "Beker Q met pH 4, want pH 4 is de gemiddelde zuurwaarde van een oplossing",
                    "Beker R met pH 7, want pH 7 is het neutrale omslagpunt van alle vloeistoffen",
                ],
                "Bij zure oplossingen geldt: hoe lager het pH-getal, des te zuurder en agressiever de vloeistof is. pH 1 is dus veel zuurder dan pH 4. (§1.4)",
            ),
            M(
                "Wat gebeurt er met de zuurgraad en de pH van vers citroensap (pH 2,5) als je er een flinke hoeveelheid zuiver water bij giet?",
                "De vloeistof wordt minder zuur en de pH stijgt richting de 7",
                [
                    "De vloeistof wordt zuurder en de pH daalt naar 0",
                    "De vloeistof verandert direct in een sterk basische oplossing met pH 12",
                    "De pH blijft exact gelijk, want water verandert de zuurgraad niet",
                ],
                "Door water toe te voegen verdun je het zuur: de oplossing wordt minder zuur. Daardoor stijgt de pH richting de neutrale waarde van 7. (§1.4)",
            ),
            M(
                "Huishoudammonia heeft een pH van ongeveer 11. Wat gebeurt er met de pH als je ammonia verdunt met kraanwater?",
                "De oplossing wordt minder basisch en de pH daalt richting de 7",
                [
                    "De oplossing wordt basischer en de pH stijgt naar 14",
                    "De pH daalt onmiddellijk tot een sterk zure waarde van 1",
                    "De pH verandert niet, omdat water zelf geen base kan afbreken",
                ],
                "Door een basische oplossing te verdunnen met water neemt de basische werking af. De pH daalt dan richting de 7. (§1.4)",
            ),
            M(
                "Welke van de onderstaande stoffen uit het huishouden vormt opgelost in water een basische oplossing?",
                "Gootsteenontstopper (natriumhydroxide)",
                [
                    "Schoonmaakazijn",
                    "Bruisend mineraalwater",
                    "Citroensap",
                ],
                "Gootsteenontstopper, zeep en ammonia zijn basisch (pH > 7). Azijn, citroensap en koolzuurhoudend water zijn zuur (pH < 7). (§1.4)",
            ),
            M(
                "Hoe gebruik je pH-papier op de juiste manier om de zuurgraad van een onbekende vloeistof te bepalen?",
                "Je doopt het papier in de vloeistof en vergelijkt de kleur met de schaal op het doosje",
                [
                    "Je verwarmt het bevochtigde papier voorzichtig boven een gasvlam totdat het spontaan ontbrandt",
                    "Je weegt het papier op een analytische precisiebalans voor en na indompeling in de vloeistof",
                    "Je meet met een stopwatch nauwkeurig hoe lang het duurt voordat het papier in de vloeistof oplost",
                ],
                "Strookjes pH-papier verkleuren in een vloeistof; door de resulterende kleur te vergelijken met de kleurenschaal op het doosje lees je de pH af. (§1.4)",
            ),
            M(
                "Welke kleurverandering neem je waar wanneer je een strookje universeel pH-papier in geconcentreerd zoutzuur doopt?",
                "Het papier kleurt fel rood of oranje",
                [
                    "Het papier kleurt donkerblauw of paars",
                    "Het papier kleurt helder groen",
                    "Het papier blijft geheel wit en kleurloos",
                ],
                "In een zure oplossing kleurt pH-papier rood of oranje (lage pH). In een basische oplossing kleurt het groen, blauw of paars. (§1.4)",
            ),
            M(
                "Waarom moet je bij het schoonmaken met geconcentreerd zoutzuur veel voorzichtiger zijn dan met keukenazijn?",
                "Zoutzuur heeft een veel lagere pH dan azijn en tast de huid veel sterker aan",
                [
                    "Zoutzuur heeft een veel hogere pH en is daardoor een sterke base",
                    "Azijn is een zuivere stof, terwijl zoutzuur een ontmengde emulsie is",
                    "Zoutzuur heeft een kookpunt dat veel lager ligt dan het vriespunt van azijn",
                ],
                "Zoutzuur heeft een zeer lage pH (ongeveer 0 tot 1) en is veel agressiever dan tafelazijn (pH ongeveer 3). Zuren met een zeer lage pH tasten de huid ernstig aan. (§1.4)",
            ),
            M(
                "Een blokje zuiver aluminium heeft een dichtheid van 2,7 g/cm³ en een massa van 81 g. Bereken het volume van dit blokje.",
                "30 cm³",
                [
                    "219 cm³",
                    "0,033 cm³",
                    "54 cm³",
                ],
                "volume = massa / dichtheid = 81 g / 2,7 g/cm³ = 30 cm³. (§1.1)",
            ),
            M(
                "Men verwarmt zuiver waterijs totdat het smelt. Wat gebeurt er met de temperatuur zolang het ijs aan het smelten is?",
                "De temperatuur blijft constant op 0 °C totdat al het ijs gesmolten is",
                [
                    "De temperatuur stijgt geleidelijk van 0 °C naar 100 °C tijdens het smelten",
                    "De temperatuur daalt tijdelijk tot ver onder het nulpunt",
                    "De temperatuur schommelt onregelmatig tussen −10 °C en +10 °C",
                ],
                "Zuiver ijs is een zuivere stof en heeft een vast smeltpunt van 0 °C. Tijdens de faseovergang blijft de temperatuur constant. (§1.3)",
            ),
            # 5 Waaronwaar (2 onwaar)
            W(
                "Een vloeistof met een pH van 9 is zuurder dan een vloeistof met een pH van 3.",
                False,
                "Onwaar. Hoe lager het getal op de pH-schaal, des te zuurder de vloeistof is. pH 3 is zuur en pH 9 is basisch. (§1.4)",
            ),
            W(
                "Zuiver gedestilleerd water bevat geen zuren of basen en heeft een pH van precies 7.",
                True,
                "Waar. Zuiver water is neutraal en heeft bij kamertemperatuur exact pH 7. (§1.4)",
            ),
            W(
                "Wanneer je aan een bekerglas met azijn (pH 3) een liter zuiver water toevoegt, kan de vloeistof basisch worden met een pH van 9.",
                False,
                "Onwaar. Door verdunnen met neutraal water (pH 7) stijgt de pH van een zuur wel richting 7, maar het kan nooit basisch (boven 7) worden. (§1.4)",
            ),
            W(
                "Sterk basische oplossingen zoals gootsteenontstopper kunnen net als sterke zuren zeer agressief zijn voor de huid.",
                True,
                "Waar. Zowel vloeistoffen met een zeer lage pH als vloeistoffen met een zeer hoge pH zijn bijtend en gevaarlijk voor de huid. (§1.4)",
            ),
            W(
                "Het sap van rodekool kan gebruikt worden als indicator omdat het van kleur verandert als de zuurgraad verandert.",
                True,
                "Waar. Rodekoolsap kleurt rood in een zure omgeving en verandert via paars naar groen/geel in een basische omgeving. (§1.4)",
            ),
            # 4 Invul
            I(
                "Een glazen knikker heeft een volume van 15 cm³ en een dichtheid van 2,6 g/cm³. Bereken de massa in gram." + GETAL,
                "39|39 g",
                "m = ρ × V = 2,6 × 15 = 39 g. (§1.1)",
            ),
            I(
                "Vloeibare zuurstof kookt bij een temperatuur van −183 °C. Hoeveel Kelvin (K) is dit kookpunt?" + GETAL,
                "90|90 K",
                "K = °C + 273 = −183 + 273 = 90 K. (§1.3)",
            ),
            I(
                "Een monster vloeistof heeft een volume van 80 mL en een massa van 64 g. Bereken de dichtheid in g/cm³." + GETAL,
                "0,8|0.8|0,80|0.80|0,8 g/cm³|0.8 g/cm³",
                "ρ = m / V = 64 / 80 = 0,80 g/cm³ (1 mL = 1 cm³). (§1.1)",
            ),
            I(
                "Een fles bevat 600 mL schoonmaakazijn met een dichtheid van 1,05 g/cm³. Bereken de massa van de azijn in gram." + GETAL,
                "630|630 g",
                "m = ρ × V = 1,05 × 600 = 630 g. (§1.1)",
            ),
            # 1 Open
            O(
                "Je doopt pH-papier in een schoonmaakmiddel en het papier kleurt donkerblauw. Wat weet je dan over het schoonmaakmiddel?" + KORT,
                ["basisch/base/hoger dan 7/boven de 7"],
                1,
                "Het schoonmaakmiddel is basisch, want de pH is hoger dan 7.",
                "Blauw op pH-papier betekent een pH boven 7: de oplossing is basisch (§1.4).",
            ),
        ],
    ),
}

if __name__ == "__main__":
    schrijf(EXAMENS, seed=20261110)
