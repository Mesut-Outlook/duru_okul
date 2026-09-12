# -*- coding: utf-8 -*-
import sys
from build_natuurkunde_h1_textbook_exams import check_and_save

# =========================================================================
# EXAMEN 26: §1.1 Kracht bij beweging — Toets A
# =========================================================================
q26 = [
    # MC 1..12 (3 A, 3 B, 3 C, 3 D)
    { # 1 (A)
        "type": "mc",
        "vraag": "Wat wordt er weergegeven op de verticale as van een (v,t)-diagram?",
        "opties": [
            "De snelheid van het voorwerp (in m/s of km/h)",
            "De totale afgelegde afstand in meters",
            "De tijd die verstreken is in seconden",
            "De resulterende kracht in newton"
        ],
        "antwoord": 0,
        "uitleg": "In een (v,t)-diagram staat op de verticale as de snelheid v (in m/s of km/h) en op de horizontale as de tijd t (in s)."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "Wat voor soort beweging stelt een stijgende rechte lijn voor in een (v,t)-diagram?",
        "opties": [
            "Een eenparige beweging met constante snelheid",
            "Een eenparig versnelde beweging",
            "Een eenparig vertraagde beweging",
            "Een stilstaand voorwerp"
        ],
        "antwoord": 1,
        "uitleg": "Een stijgende rechte lijn in een (v,t)-diagram betekent dat de snelheid elke seconde met precies dezelfde hoeveelheid toeneemt: een eenparig versnelde beweging."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "Wat betekent het als de grafiek in een (v,t)-diagram een horizontale lijn is boven de tijdas?",
        "opties": [
            "Het voorwerp staat stil",
            "De versnelling van het voorwerp neemt toe",
            "De snelheid is constant (eenparige beweging)",
            "De resulterende kracht is groter dan nul"
        ],
        "antwoord": 2,
        "uitleg": "Een horizontale lijn in een (v,t)-diagram betekent dat de snelheid gelijk blijft in de tijd. De beweging is dan eenparig (constante snelheid)."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "Wat verstaat men in de natuurkunde onder de 'resulterende kracht' (Fres)?",
        "opties": [
            "Altijd alleen de motorkracht van het voertuig",
            "De zwaarste tegenwerkende kracht die op het voorwerp werkt",
            "De kracht die overblijft nadat alle wrijving is verdwenen",
            "De optelsom van alle krachten samen, die hetzelfde effect heeft als alle afzonderlijke krachten"
        ],
        "antwoord": 3,
        "uitleg": "De resulterende kracht (Fres) is de somkracht van alle krachten die tegelijk op een voorwerp werken. Hij heeft hetzelfde effect op de beweging als alle losse krachten samen."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "Abdul trekt met 63 N naar rechts aan een winkelwagentje en Inez trekt met 59 N in dezelfde richting naar rechts. Hoe groot is hun gezamenlijke voorwaartse kracht?",
        "opties": [
            "122 N naar rechts",
            "4 N naar rechts",
            "73 N naar rechts",
            "3717 N naar rechts"
        ],
        "antwoord": 0,
        "uitleg": "Krachten die in precies dezelfde richting werken mag je bij elkaar optellen: 63 N + 59 N = 122 N naar rechts (zie voorbeeld 1 uit het boek)."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "Sarah trekt met 73 N naar links aan hetzelfde winkelwagentje, terwijl Abdul en Inez samen met 122 N naar rechts trekken. Hoe groot is de resulterende kracht?",
        "opties": [
            "195 N naar rechts",
            "49 N naar rechts",
            "49 N naar links",
            "0 N, ze heffen elkaar op"
        ],
        "antwoord": 1,
        "uitleg": "Bij tegengestelde krachten trek je de kleinste van de grootste af: Fres = 122 N - 73 N = 49 N in de richting van de grootste kracht (naar rechts)."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Welke twee tegenwerkende krachten werken er horizontaal op een rijdende auto of fietser?",
        "opties": [
            "Zwaartekracht en normaalkracht",
            "Spierkracht en veerkracht",
            "Luchtweerstandskracht en rolweerstandskracht",
            "Motorkracht en magnetische kracht"
        ],
        "antwoord": 2,
        "uitleg": "In horizontale richting bestaat de tegenwerkende weerstandskracht (Ftegen) uit de luchtweerstandskracht (Fw,l) en de rolweerstandskracht (Fw,r)."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Een fietser rijdt met een constante snelheid van 18 km/h over een vlakke weg. Wat kun je met zekerheid zeggen over de resulterende kracht?",
        "opties": [
            "De resulterende kracht is gelijk aan de trapkracht",
            "De resulterende kracht wijst naar voren",
            "De resulterende kracht is groter dan de tegenwerkende wrijving",
            "De resulterende kracht is exact gelijk aan 0 N"
        ],
        "antwoord": 3,
        "uitleg": "Bij een constante snelheid verandert de snelheid niet. Volgens de wetten van Newton heffen de voorwaartse kracht en de tegenwerkende krachten elkaar precies op: Fres = 0 N."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "Wat gebeurt er met de snelheid van een voorwerp als de motorkracht groter is dan de tegenwerkende krachten (Fvooruit > Ftegen)?",
        "opties": [
            "De snelheid neemt toe (versnelde beweging)",
            "De snelheid neemt af (vertraagde beweging)",
            "De snelheid blijft exact constant",
            "Het voorwerp komt onmiddellijk tot stilstand"
        ],
        "antwoord": 0,
        "uitleg": "Als Fvooruit > Ftegen werkt de resulterende kracht in de richting van de beweging. Het voorwerp krijgt een versnelling: de snelheid neemt toe."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Wat gebeurt er met de snelheid van een auto als de bestuurder het gaspedaal loslaat en de rem intrapt (Fvooruit < Ftegen)?",
        "opties": [
            "De snelheid blijft gelijk doordat massa meewerkt",
            "De snelheid neemt af (vertraagde beweging)",
            "De auto versnelt achteruit",
            "De auto verandert direct van richting"
        ],
        "antwoord": 1,
        "uitleg": "Wanneer de tegenwerkende krachten groter zijn dan de voorwaartse kracht, wijst de resulterende kracht tegen de beweging in. De auto remt af (vertraagde beweging)."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "In welke situatie uit het dagelijks leven is de resulterende kracht op het voorwerp gelijk aan nul (Fres = 0 N)?",
        "opties": [
            "Een wielrenner die vanuit stilstand wegsprint bij de start",
            "Een steen die van een flatgebouw naar beneden valt en versnelt",
            "Een regendruppel die met een constante snelheid loodrecht naar beneden valt",
            "Een auto die krachtig moet remmen voor een stoplicht"
        ],
        "antwoord": 2,
        "uitleg": "Als een regendruppel met een constante snelheid valt, is de snelheid onveranderlijk. De opwaartse luchtweerstand is dan precies even groot als de neerwaartse zwaartekracht, waardoor Fres = 0 N."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Twee personen duwen een auto door de sneeuw. Ieder oefent een kracht van 300 N uit. De auto beweegt met een constante snelheid. Hoe groot is de wrijvingskracht van de sneeuw?",
        "opties": [
            "300 N in de duwrichting",
            "150 N tegen de duwrichting in",
            "0 N, want er is geen wrijving",
            "600 N tegen de duwrichting in"
        ],
        "antwoord": 3,
        "uitleg": "De twee personen leveren samen 300 + 300 = 600 N voorwaarts. Omdat de auto met een constante snelheid beweegt, moet Fres = 0 N zijn. De tegenwerkende wrijvingskracht is dus 600 N."
    },
    # Waaronwaar 13..16 (2 Waar, 2 Onwaar)
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "Een voorwerp dat met een constante snelheid in een rechte lijn beweegt, ondervindt een resulterende kracht van 0 N.",
        "antwoord": True,
        "uitleg": "Waar. Bij een constante snelheid heffen alle voorwaartse en tegenwerkende krachten elkaar volledig op, zodat Fres = 0 N."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "In een (v,t)-diagram stelt een dalende rechte lijn een eenparig vertraagde beweging voor.",
        "antwoord": True,
        "uitleg": "Waar. De snelheid neemt per seconde met een gelijke hoeveelheid af; dit is de definitie van eenparig vertraagd."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Als op een rijdende auto een resulterende kracht in de bewegingsrichting werkt, blijft de snelheid van de auto gelijk.",
        "antwoord": False,
        "uitleg": "Onwaar. Een resulterende kracht in de bewegingsrichting veroorzaakt een versnelling: de snelheid neemt toe."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "De resulterende kracht van twee krachten van 40 N en 30 N die in tegengestelde richting werken is 70 N.",
        "antwoord": False,
        "uitleg": "Onwaar. Omdat de krachten tegengesteld gericht zijn trek je ze van elkaar af: 40 N - 30 N = 10 N."
    },
    # Invul 17..18
    { # 17
        "type": "invul",
        "vraag": "Noem het type diagram waarin de snelheid tegen de tijd wordt uitgezet: een [...]-diagram.",
        "antwoord": "(v,t)",
        "uitleg": "In een (v,t)-diagram staat op de y-as de snelheid (v) en op de x-as de tijd (t)."
    },
    { # 18
        "type": "invul",
        "vraag": "Als twee mensen een auto voortduwen met samen 600 N en de wrijvingskracht op een glad stuk ijs zakt naar 500 N, dan is de resulterende kracht gelijk aan [...] N.",
        "antwoord": "100",
        "uitleg": "Fres = Fvooruit - Ftegen = 600 N - 500 N = 100 N in voorwaartse richting."
    },
    # Open 19..20
    { # 19
        "type": "open",
        "vraag": "Leg uit wat er met de beweging van een voorwerp gebeurt als de motorkracht en de tegenwerkende krachten precies even groot zijn.",
        "sleutelwoorden": ["constante snelheid/eenparig", "stilstand/blijft stil", "Fres is nul/heffen elkaar op"],
        "minTreffers": 1,
        "modelantwoord": "De krachten heffen elkaar op waardoor Fres = 0 N. Het voorwerp beweegt dan met een constante snelheid (eenparig) of staat stil.",
        "uitleg": "Als de krachten gelijk zijn aan elkaar is de resulterende kracht 0 N. De snelheid verandert niet."
    },
    { # 20
        "type": "open",
        "vraag": "Twee krachten van 80 N en 50 N trekken in dezelfde richting aan een kist. Bereken de resulterende kracht en vermeld de eenheid.",
        "sleutelwoorden": ["130 N/130 newton", "optellen/zelfde richting"],
        "minTreffers": 1,
        "modelantwoord": "Fres = 80 N + 50 N = 130 N.",
        "uitleg": "Omdat de krachten in dezelfde richting werken, tel je ze bij elkaar op: 80 + 50 = 130 newton."
    }
]

check_and_save("ex-h3-natuurkunde-26", 26, "Toets 26 — §1.1 Kracht bij beweging — Toets A", "🏎️", q26)

# =========================================================================
# EXAMEN 27: §1.1 Kracht bij beweging — Toets B
# =========================================================================
q27 = [
    # MC 1..12 (3 A, 3 B, 3 C, 3 D)
    { # 1 (A)
        "type": "mc",
        "vraag": "Waarom neemt de luchtweerstand van een fietser toe naarmate hij harder gaat fietsen?",
        "opties": [
            "Omdat hij per seconde meer luchtdeeltjes moet opzij duwen",
            "Omdat zijn banden warmer worden en meer grip krijgen",
            "Omdat de zwaartekracht op de fietser toeneemt bij hogere snelheid",
            "Omdat de rolweerstand automatisch verandert in luchtweerstand"
        ],
        "antwoord": 0,
        "uitleg": "Bij een hogere snelheid botst de fietser per seconde tegen veel meer luchtmoleculen, waardoor de luchtweerstandskracht kwadratisch toeneemt met de snelheid."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "Tessa rijdt op haar hoverboard met constante snelheid. Als ze gaat hurken, merkt ze dat ze versnelt. Wat is hiervan de natuurkundige verklaring?",
        "opties": [
            "Door te hurken levert de elektromotor opeens meer vermogen",
            "Door te hurken wordt haar frontale oppervlak kleiner, waardoor de luchtweerstand afneemt",
            "Haar massa neemt door het hurken aanzienlijk af",
            "De zwaartekracht trekt haar nu schuin naar voren"
        ],
        "antwoord": 1,
        "uitleg": "Door te hurken verkleint Tessa haar frontale oppervlak. De tegenwerkende luchtweerstand wordt kleiner dan de motorkracht, waardoor Fres > 0 en ze versnelt (zie opdracht 12 uit het boek)."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "Een vallende golfbal heeft een massa van 0,050 kg (zwaartekracht Fz = 0,49 N). Op een bepaald moment is de luchtweerstand 0,10 N. Hoe groot is de resulterende kracht en wat gebeurt er met de snelheid?",
        "opties": [
            "Fres = 0,59 N omlaag; de golfbal vertraagt",
            "Fres = 0,39 N omhoog; de golfbal vertraagt",
            "Fres = 0,39 N omlaag; de snelheid wordt groter",
            "Fres = 0 N; de golfbal valt met constante snelheid"
        ],
        "antwoord": 2,
        "uitleg": "Fres = Fz - Fw,l = 0,49 N - 0,10 N = 0,39 N naar beneden gericht. Omdat Fres in de bewegingsrichting werkt, versnelt de golfbal (opdracht 13)."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "Patricia fietst met constante snelheid naar school en levert een trapkracht van 120 N. De volgende dag heeft ze flinke tegenwind, maar ze wil met exact dezelfde snelheid fietsen. Wat moet er met haar trapkracht gebeuren?",
        "opties": [
            "Haar trapkracht moet precies 120 N blijven",
            "Haar trapkracht moet afnemen naar minder dan 120 N",
            "Haar trapkracht wordt automatisch nul",
            "Haar trapkracht moet groter worden dan 120 N"
        ],
        "antwoord": 3,
        "uitleg": "Door de tegenwind neemt de tegenwerkende luchtweerstand toe. Om bij deze grotere weerstand nog steeds een constante snelheid (Fres = 0 N) te houden, moet ze harder trappen (opdracht 9)."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "Achmed gooit een tennisbal recht omhoog. Welke krachten werken er op de bal op het moment dat de bal omhoog beweegt (na het verlaten van de hand)?",
        "opties": [
            "De zwaartekracht naar beneden en de luchtweerstand naar beneden",
            "Alleen de spierkracht van Achmed naar boven",
            "De zwaartekracht naar beneden en de spierkracht naar boven",
            "De zwaartekracht naar beneden en de luchtweerstand naar boven"
        ],
        "antwoord": 0,
        "uitleg": "Zodra de bal los is, werkt er geen spierkracht meer op. De zwaartekracht trekt altijd omlaag. Omdat de bal omhoog beweegt, werkt de luchtweerstand tegen de beweging in: ook omlaag! (opdracht 6)."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "Op een auto werken twee horizontale krachten: de motorkracht van 1800 N naar voren en een totale weerstand van 1400 N naar achteren. Wat is de resulterende kracht?",
        "opties": [
            "3200 N naar voren",
            "400 N naar voren",
            "400 N naar achteren",
            "0 N"
        ],
        "antwoord": 1,
        "uitleg": "Fres = Fmotor - Ftegen = 1800 N - 1400 N = 400 N in de richting van de grootste kracht (naar voren)."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Tijdens een autorace rijdt een racewagen met zijn topsnelheid van 310 km/h over het rechte stuk. Hoe verhouden de motorkracht en de tegenwerkende weerstand zich op dat moment?",
        "opties": [
            "De motorkracht is veel groter dan de tegenwerkende weerstand",
            "De tegenwerkende weerstand is groter dan de motorkracht",
            "De motorkracht en de tegenwerkende weerstand zijn precies even groot",
            "Er werkt op topsnelheid helemaal geen weerstand meer"
        ],
        "antwoord": 2,
        "uitleg": "Op topsnelheid rijdt de auto met een constante snelheid. Dan geldt volgens de eerste wet van Newton dat Fres = 0 N, dus Fmotor = Ftegen (zie voorbeeld 2 fase II)."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Hoe ziet de grafiek in een (v,t)-diagram eruit als een auto eenparig afremt tot stilstand?",
        "opties": [
            "Een stijgende rechte lijn vanaf de oorsprong",
            "Een horizontale rechte lijn boven de nulwaarde",
            "Een kromme lijn die steeds steiler omhoog loopt",
            "Een dalende rechte lijn die eindigt op de tijdas (v = 0)"
        ],
        "antwoord": 3,
        "uitleg": "Eenparig afremmen betekent dat de snelheid gelijkmatig daalt: een rechte lijn omlaag die bij stilstand de as v = 0 raakt."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "Een parachutist springt uit een vliegtuig en opent zijn parachute. Direct na het openen is de luchtweerstand groter dan de zwaartekracht. Wat gebeurt er met zijn snelheid?",
        "opties": [
            "Zijn snelheid naar beneden neemt af (hij vertraagt)",
            "Zijn snelheid neemt toe",
            "Hij blijft met constante snelheid vallen",
            "Hij begint onmiddellijk omhoog te vliegen"
        ],
        "antwoord": 0,
        "uitleg": "Omdat de opwaartse luchtweerstand groter is dan de neerwaartse zwaartekracht, is de resulterende kracht omhoog gericht (tegen de beweging in). Hij valt dus trager naar beneden (vertraagt)."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Twee trekkers trekken bij een wedstrijd aan hetzelfde zware betonnen blok. Trekker A trekt met 15 kN naar links en Trekker B met 15 kN naar rechts. Wat gebeurt er met het blok?",
        "opties": [
            "Het blok versnelt naar trekker A",
            "Het blok blijft in rust omdat de resulterende kracht 0 N is",
            "Het blok versnelt naar trekker B",
            "Het blok breekt en beweegt met 30 kN naar voren"
        ],
        "antwoord": 1,
        "uitleg": "Beide krachten zijn even groot en tegengesteld gericht: Fres = 15 kN - 15 kN = 0 N. Het blok blijft op zijn plaats."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "Een wielrenster rijdt door een scherpe bocht op een wielerbaan met constante baansnelheid. Waarom is de resulterende kracht in de bocht toch NIET nul?",
        "opties": [
            "Omdat ze harder moet trappen in de bocht",
            "Omdat haar snelheid steeds toeneemt",
            "Omdat de richting van haar beweging voortdurend verandert",
            "Omdat de zwaartekracht in een bocht wegvalt"
        ],
        "antwoord": 2,
        "uitleg": "Een kracht kan niet alleen de grootte van de snelheid veranderen, maar ook de richting van de beweging. Om een bocht te maken is altijd een resulterende zijwaartse kracht nodig (opdracht 11 en theorie §1.1/1.3)."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Welke eenheid hoort bij de grootheid 'kracht' in het SI-stelsel?",
        "opties": [
            "Kilogram (kg)",
            "Meter per seconde (m/s)",
            "Joule (J)",
            "Newton (N)"
        ],
        "antwoord": 3,
        "uitleg": "De standaardeenheid van kracht in het SI-stelsel is de newton, afgekort met het symbool N."
    },
    # Waaronwaar 13..16 (2 Waar, 2 Onwaar)
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "Als een wielrenster stopt met trappen, vertraagt haar fiets doordat de rolweerstand en de luchtweerstand tegen de beweging in werken.",
        "antwoord": True,
        "uitleg": "Waar. Zonder aandrijfkracht werken alleen de weerstandskrachten tegen de beweging in, waardoor Fres tegen de beweging in wijst en de fietser vertraagt."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "Bij een regendruppel die zijn constante eindsnelheid heeft bereikt, is de zwaartekracht precies even groot als de opwaartse luchtweerstand.",
        "antwoord": True,
        "uitleg": "Waar. De snelheid is dan constant en verandert niet meer, wat betekent dat Fres = 0 N en Fz = Fw,l."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Op een voorwerp dat stilstaat op een tafel werken helemaal geen krachten.",
        "antwoord": False,
        "uitleg": "Onwaar. Er werken wel degelijk krachten op: de zwaartekracht omlaag en de normaalkracht van de tafel omhoog. Omdat ze even groot zijn heffen ze elkaar op (Fres = 0 N)."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Als de motorkracht van een auto twee keer zo groot is als de tegenwerkende weerstand, rijdt de auto met een constante snelheid.",
        "antwoord": False,
        "uitleg": "Onwaar. Als de motorkracht groter is dan de weerstand, is er een resulterende kracht voorwaarts en versnelt de auto."
    },
    # Invul 17..18
    { # 17
        "type": "invul",
        "vraag": "De som van de luchtweerstandskracht en de rolweerstandskracht noem je de totale [...] kracht.",
        "antwoord": "tegenwerkende",
        "uitleg": "De krachten die de voorwaartse beweging belemmeren noem je samen de tegenwerkende krachten (Ftegen = Fw,l + Fw,r)."
    },
    { # 18
        "type": "invul",
        "vraag": "Een tennisbal van 0,060 kg ondervindt een zwaartekracht van 0,60 N. Als hij omhoog vliegt en de luchtweerstand 0,15 N bedraagt, is de totale resulterende kracht omlaag gelijk aan [...] N.",
        "antwoord": "0,75",
        "uitleg": "Als de bal omhoog beweegt, werken zowel Fz (0,60 N) als Fw,l (0,15 N) naar beneden: Fres = 0,60 + 0,15 = 0,75 N omlaag."
    },
    # Open 19..20
    { # 19
        "type": "open",
        "vraag": "Beschrijf wat er gebeurt met de luchtweerstand op een vallende regendruppel vanaf het moment dat hij uit de wolk valt tot het moment dat hij een constante snelheid heeft.",
        "sleutelwoorden": ["luchtweerstand neemt toe/wordt groter", "tot gelijk aan zwaartekracht/Fres nul"],
        "minTreffers": 1,
        "modelantwoord": "In het begin valt de druppel snel en versnelt hij. Naarmate zijn snelheid toeneemt, wordt de luchtweerstand steeds groter totdat deze gelijk is aan de zwaartekracht (Fres = 0 N).",
        "uitleg": "Luchtweerstand stijgt met de snelheid tot hij even groot is als de zwaartekracht."
    },
    { # 20
        "type": "open",
        "vraag": "Een fietser oefent 90 N trapkracht uit en heeft 40 N rolweerstand en 50 N luchtweerstand. Bepaal de waarde van de resulterende kracht.",
        "sleutelwoorden": ["0 N/nul newton", "heffen elkaar op/in evenwicht"],
        "minTreffers": 1,
        "modelantwoord": "Fvooruit = 90 N en Ftegen = 40 + 50 = 90 N. Fres = 90 - 90 = 0 N.",
        "uitleg": "De voorwaartse kracht en tegenwerkende krachten zijn exact gelijk: 90 - 90 = 0 N."
    }
]

check_and_save("ex-h3-natuurkunde-27", 27, "Toets 27 — §1.1 Kracht bij beweging — Toets B", "🏎️", q27)

# =========================================================================
# EXAMEN 28: §1.1 Kracht bij beweging — Toets C
# =========================================================================
q28 = [
    # MC 1..12 (3 A, 3 B, 3 C, 3 D)
    { # 1 (A)
        "type": "mc",
        "vraag": "In figuur 1.6 van het boek wordt een autorace in vier fasen verdeeld. In fase I trekt de raceauto snel op. Welke uitspraak over de krachten in fase I is juist?",
        "opties": [
            "De motorkracht is veel groter dan de tegenwerkende weerstandskrachten",
            "De motorkracht is precies even groot als de tegenwerkende wrijving",
            "De tegenwerkende wrijving is groter dan de motorkracht",
            "De resulterende kracht is exact gelijk aan nul"
        ],
        "antwoord": 0,
        "uitleg": "Bij het optrekken (versnellen) moet de motorkracht groter zijn dan de tegenwerkende krachten, zodat Fres naar voren wijst."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "In fase III van dezelfde autorace remt de coureur eenparig af voor een bocht. Welke uitspraak over de resulterende kracht in fase III is juist?",
        "opties": [
            "De resulterende kracht werkt naar voren in de rijrichting",
            "De resulterende kracht werkt naar achteren (tegen de bewegingsrichting in)",
            "De resulterende kracht is nul omdat de vertraging constant is",
            "Er werkt alleen nog maar zwaartekracht op de auto"
        ],
        "antwoord": 1,
        "uitleg": "Tijdens het afremmen is de tegenwerkende kracht (remkracht + weerstand) groter dan de voorwaartse kracht, waardoor Fres tegen de bewegingsrichting in wijst."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "In fase IV staat de raceauto stil in de pitstraat. Hoe groot is de resulterende kracht op de stilstaande auto?",
        "opties": [
            "Gelijk aan de massa van de auto vermenigvuldigd met de topsnelheid",
            "Oneindig groot omdat de remmen vaststaan",
            "Fres = 0 N",
            "Gelijk aan de maximale motorkracht"
        ],
        "antwoord": 2,
        "uitleg": "Als een voorwerp stilstaat en blijft stilstaan, verandert de snelheid niet. De resulterende kracht is dan Fres = 0 N."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "Een vrachtwagen rijdt op de snelweg met een constante snelheid van 80 km/h. De luchtweerstand is 2200 N en de rolweerstand is 800 N. Hoeveel voorwaartse kracht levert de motor?",
        "opties": [
            "1400 N",
            "2200 N",
            "800 N",
            "3000 N"
        ],
        "antwoord": 3,
        "uitleg": "Totale weerstand = 2200 N + 800 N = 3000 N. Omdat de vrachtwagen met constante snelheid rijdt, moet Fmotor = Ftegen = 3000 N zijn om Fres = 0 N te houden."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "Jan fietst in 5 seconden vanuit stilstand eenparig naar 3,0 m/s. Welke vorm heeft zijn (v,t)-grafiek gedurende deze eerste 5 seconden?",
        "opties": [
            "Een rechte stijgende lijn van (0, 0) naar (5, 3)",
            "Een horizontale rechte lijn op hoogte v = 3",
            "Een dalende kromme lijn naar de tijdas",
            "Een verticale lijn op het tijdstip t = 5"
        ],
        "antwoord": 0,
        "uitleg": "Eenparig versnellen vanuit stilstand betekent dat de snelheid gelijkmatig toeneemt vanaf 0 m/s: een rechte stijgende lijn (opdracht 14)."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "Vervolgens fietst Jan 15 seconden lang met de constante snelheid van 3,0 m/s door. Hoe groot is de resulterende kracht op Jan tijdens deze 15 seconden?",
        "opties": [
            "Gelijk aan zijn gewicht in newton",
            "0 N",
            "45 N",
            "15 N"
        ],
        "antwoord": 1,
        "uitleg": "Tijdens de 15 seconden met constante snelheid verandert de snelheid niet, dus is de resulterende kracht Fres = 0 N."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Waarom heeft een stroomlijn (zoals bij een gestroomlijnde ligfiets of sportwagen) invloed op de snelheid?",
        "opties": [
            "Omdat de zwaartekracht daardoor kleiner wordt",
            "Omdat de rolweerstand van de banden direct naar nul zakt",
            "Omdat de luchtweerstandskracht daardoor aanzienlijk kleiner wordt",
            "Omdat de motor door stroomlijning automatisch meer toeren maakt"
        ],
        "antwoord": 2,
        "uitleg": "Een goede stroomlijn zorgt dat de lucht makkelijker om het voertuig vloeit. De luchtweerstandscoëfficiënt en weerstandskracht nemen af, waardoor het voertuig bij dezelfde motorkracht sneller kan rijden."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Drie kinderen trekken aan een touw. Anna trekt met 40 N naar links, Bram trekt met 25 N naar links, en Daan trekt met 65 N naar rechts. Wat is de toestand van het touw?",
        "opties": [
            "Het touw versnelt met 130 N naar rechts",
            "Het touw versnelt met 15 N naar links",
            "Het touw versnelt met 25 N naar rechts",
            "Het touw is in evenwicht (Fres = 0 N) en versnelt niet"
        ],
        "antwoord": 3,
        "uitleg": "Kracht naar links = 40 + 25 = 65 N. Kracht naar rechts = 65 N. Fres = 65 - 65 = 0 N: evenwicht."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "Een tennisbal wordt met een racket geraakt. Tijdens het contactmoment buigt het racketblad door en vervormt de bal. Welke twee uitwerkingen kan een kracht hebben op een voorwerp?",
        "opties": [
            "Verandering van de beweging (snelheid/richting) én vervorming van het voorwerp",
            "Verandering van de chemische samenstelling én gewichtstoename",
            "Toename van de atoommassa én temperatuursdaling",
            "Verandering van volume zonder enige vormverandering"
        ],
        "antwoord": 0,
        "uitleg": "Een kracht kan twee dingen veroorzaken: een dynamisch effect (verandering van snelheid of bewegingsrichting) en een statisch effect (tijdelijke of blijvende vervorming)."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Wat gebeurt er met de rolweerstand van een fiets als je de banden stevig oppompt tot de aanbevolen spanning?",
        "opties": [
            "De rolweerstand wordt groter doordat de band stijver is",
            "De rolweerstand wordt kleiner doordat de band minder vervormt op het wegdek",
            "De rolweerstand verandert niet, alleen de luchtweerstand verandert",
            "De rolweerstand wordt precies nul"
        ],
        "antwoord": 1,
        "uitleg": "Harde banden vervormen veel minder bij het rollen over de weg. Daardoor is het contactvlak kleiner en daalt de rolweerstand aanzienlijk."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "Een parachutist valt met constante snelheid naar beneden. Plotseling klapt een harde windvlaag van opzij tegen hem aan. Wat gebeurt er met zijn beweging?",
        "opties": [
            "Hij valt direct twee keer zo snel naar beneden",
            "Zijn verticale snelheid wordt direct nul",
            "Zijn bewegingsrichting verandert doordat er een zijwaartse kracht bij komt",
            "Zijn totale resulterende kracht blijft exact nul"
        ],
        "antwoord": 2,
        "uitleg": "De zijwaartse windkracht levert een resulterende kracht opzij op, waardoor de parachutist afbuigt en zijn bewegingsrichting verandert."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Als op een boot een voorwaartse motorkracht van 500 N werkt en een tegenwerkende waterweerstand van 350 N, in welke richting versnelt de boot en met welke resulterende kracht?",
        "opties": [
            "Naar achteren met 850 N",
            "Naar voren met 850 N",
            "Naar achteren met 150 N",
            "Naar voren met 150 N"
        ],
        "antwoord": 3,
        "uitleg": "Fres = Fvooruit - Ftegen = 500 N - 350 N = 150 N in voorwaartse richting."
    },
    # Waaronwaar 13..16 (2 Waar, 2 Onwaar)
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "Wanneer twee krachten die op één voorwerp werken elkaar opheffen, heeft dat hetzelfde effect als wanneer er helemaal geen krachten op werken.",
        "antwoord": True,
        "uitleg": "Waar. In beide gevallen is Fres = 0 N en behoudt het voorwerp zijn constante snelheid of stilstand."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "In een (v,t)-diagram geeft het steiler worden van een kromme lijn aan dat de versnelling toeneemt.",
        "antwoord": True,
        "uitleg": "Waar. Hoe steiler de (v,t)-grafiek loopt, hoe sneller de snelheid per seconde toeneemt."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Als een auto 100 km/h rijdt, is de resulterende kracht altijd 100 N.",
        "antwoord": False,
        "uitleg": "Onwaar. Als de snelheid constant 100 km/h is, is de versnelling nul en is de resulterende kracht 0 N."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Luchtweerstand werkt altijd in de richting waarin de zwaartekracht trekt.",
        "antwoord": False,
        "uitleg": "Onwaar. Weerstandskrachten werken altijd tegen de richting van de beweging in, ongeacht de zwaartekracht."
    },
    # Invul 17..18
    { # 17
        "type": "invul",
        "vraag": "Als een wielrenster op een rechte weg rijdt met constante snelheid en Ftegen = 85 N is, dan levert zij een trapkracht van [...] N.",
        "antwoord": "85",
        "uitleg": "Omdat de snelheid constant is, geldt Fres = 0 N, dus Ftrap = Ftegen = 85 N."
    },
    { # 18
        "type": "invul",
        "vraag": "De kracht die ontstaat doordat banden over het wegdek rollen en vervormen heet de [...] kracht.",
        "antwoord": "rolweerstands",
        "uitleg": "De weerstandskracht tussen rollende wielen en het wegoppervlak heet de rolweerstandskracht (Fw,r)."
    },
    # Open 19..20
    { # 19
        "type": "open",
        "vraag": "Noem de twee verschillende tegenwerkende wrijvingskrachten die optreden bij een fietser die over asfalt rijdt.",
        "sleutelwoorden": ["luchtweerstand/luchtweerstandskracht", "rolweerstand/rolweerstandskracht"],
        "minTreffers": 2,
        "modelantwoord": "De luchtweerstandskracht (Fw,l) en de rolweerstandskracht (Fw,r).",
        "uitleg": "Luchtweerstand ontstaat door botsing met luchtmoleculen en rolweerstand door vervorming van de banden op de weg."
    },
    { # 20
        "type": "open",
        "vraag": "Leg uit waarom een auto die met 120 km/h op cruisecontrol rijdt veel meer brandstof per kilometer verbruikt dan dezelfde auto die 80 km/h rijdt.",
        "sleutelwoorden": ["luchtweerstand veel hoger/groter", "meer motorkracht nodig"],
        "minTreffers": 1,
        "modelantwoord": "Bij 120 km/h is de luchtweerstand veel groter dan bij 80 km/h. De motor moet een veel grotere kracht leveren om de snelheid constant te houden, wat extra brandstof kost.",
        "uitleg": "Luchtweerstand stijgt sterk met de snelheid, waardoor de motor harder moet werken."
    }
]

check_and_save("ex-h3-natuurkunde-28", 28, "Toets 28 — §1.1 Kracht bij beweging — Toets C", "🏎️", q28)

print("§1.1 afgerond.")
