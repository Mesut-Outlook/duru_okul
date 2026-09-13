#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 3 Additional 25-question Exams for Natuurkunde HAVO 3 Hoofdstuk 1:
- examen_45.js: Toets 45 — §1.1 Kracht bij beweging — Toets D (25 vragen)
- examen_46.js: Toets 46 — §1.2 Soorten beweging & Diagrammen — Toets D (25 vragen)
- examen_47.js: Toets 47 — §1.3 Kracht en versnelling — Toets D (25 vragen)
"""
import os, json, random

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/natuurkunde/js/data"
os.makedirs(DATA_DIR, exist_ok=True)

def balance_mc(questions):
    mc_indices = [i for i, q in enumerate(questions) if q.get("type") == "mc"]
    rnd = random.Random(questions[0].get("vraag", "") if questions else "")
    target_pattern = []
    while len(target_pattern) < len(mc_indices):
        blok = [0, 1, 2, 3]
        rnd.shuffle(blok)
        target_pattern += blok
    for idx, q_idx in enumerate(mc_indices):
        q = questions[q_idx]
        current_ans_idx = q["antwoord"]
        correct_text = q["opties"][current_ans_idx]
        new_ans_idx = target_pattern[idx] % len(q["opties"])
        if new_ans_idx != current_ans_idx:
            opts = [opt for i, opt in enumerate(q["opties"]) if i != current_ans_idx]
            opts.insert(new_ans_idx, correct_text)
            q["opties"] = opts
            q["antwoord"] = new_ans_idx

def write_examen(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    dumped = json.dumps(data, indent=2, ensure_ascii=False)
    content = f"/* =========================================================\n"
    content += f"   Duru's Natuurkunde (HAVO 3) — {data['titel']}\n"
    content += f"   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)\n"
    content += f"   ========================================================= */\n"
    content += f"DURU.registerExamen({dumped});\n"
    with open(path, "w", encoding="utf-8") as out:
        out.write(content)
    print(f"  [OK] Natuurkunde Examen saved: {filename} ({len(data['vragen'])} vragen)")

# -------------------------------------------------------------
# TOETS 45: §1.1 Kracht bij beweging — Toets D (25 vragen)
# -------------------------------------------------------------
ex45 = {
  "id": "ex-h3-natuurkunde-45",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Toets 45 — §1.1 Kracht bij beweging — Toets D (25 vragen)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🏎️",
  "duurMin": 35,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een scooter rijdt met een constante snelheid van 45 km/h op een rechte weg. De totale tegenwerkende wrijvingskracht bedraagt 320 N. Hoe groot is de voorwaartse motorkracht van de scooter?",
      "opties": ["Precies 320 N", "Groter dan 320 N", "Kleiner dan 320 N", "0 N"],
      "antwoord": 0,
      "uitleg": "Volgens de eerste wet van Newton is de resulterende kracht nul (Fres = 0 N) bij een constante snelheid. De voorwaartse motorkracht moet daarom exact gelijk zijn aan de totale tegenwerkende wrijvingskracht: Fmotor = Ftegen = 320 N."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de grootte van de luchtweerstand op een fietser als zijn snelheid verdubbelt van 15 km/h naar 30 km/h?",
      "opties": ["De luchtweerstand wordt 4 keer zo groot", "De luchtweerstand verdubbelt (wordt 2 keer zo groot)", "De luchtweerstand blijft gelijk", "De luchtweerstand wordt 8 keer zo groot"],
      "antwoord": 0,
      "uitleg": "De luchtweerstand is evenredig met het kwadraat van de snelheid (v²). Als de snelheid 2 keer zo groot wordt, neemt de luchtweerstand toe met een factor 2² = 4."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de bandenspanning van een stadsfiets te laag is (zachte banden), vervormt de band meer tijdens het rijden en neemt de rolweerstand daardoor toe.",
      "antwoord": True,
      "uitleg": "Waar. Bij een lagere bandenspanning vervormt de band sterker bij contact met het wegdek, waardoor er meer energie verloren gaat en de rolweerstand aanzienlijk toeneemt."
    },
    {
      "type": "invul",
      "vraag": "Een elektrische auto ondervindt tijdens het optrekken een motorkracht van 2400 N naar voren en een totale wrijvingskracht van 650 N naar achteren. Bereken de resulterende kracht Fres in newton (vul alleen het getal in):",
      "antwoord": "1750",
      "uitleg": "Fres = Fvooruit - Ftegen = 2400 N - 650 N = 1750 N in de voorwaartse bewegingsrichting."
    },
    {
      "type": "mc",
      "vraag": "Waarom bukt een schaatser op de 5000 meter diep voorover met de handen op de rug?",
      "opties": ["Om het frontale oppervlak A te verkleinen en zo de luchtweerstand te verminderen", "Om de rolweerstand met het ijs te verkleinen", "Om de zwaartekracht op zijn lichaam te verlagen", "Om meer wrijving met de lucht te creëren voor stabiliteit"],
      "antwoord": 0,
      "uitleg": "Door diep voorover te bukken verkleint de schaatser het frontale oppervlak (A). Omdat luchtweerstand recht evenredig is met het frontale oppervlak, daalt de luchtweerstand aanzienlijk."
    },
    {
      "type": "mc",
      "vraag": "Een parachutespringer springt uit een vliegtuig en opent zijn parachute nog niet. Wat gebeurt er met zijn snelheid en de luchtweerstand in de eerste seconden van de val?",
      "opties": ["Zijn valsnelheid neemt toe en daardoor neemt ook de luchtweerstand toe", "Zijn snelheid neemt toe maar de luchtweerstand blijft constant", "Zijn snelheid blijft constant en de luchtweerstand daalt naar nul", "Zijn snelheid neemt af omdat de zwaartekracht verdwijnt"],
      "antwoord": 0,
      "uitleg": "In het begin is de zwaartekracht groter dan de luchtweerstand, waardoor hij versnelt. Doordat zijn valsnelheid stijgt, neemt de opwaartse luchtweerstandskracht steeds verder toe."
    },
    {
      "type": "waaronwaar",
      "vraag": "Wanneer een parachutespringer zijn maximale eindsnelheid (terminal velocity) heeft bereikt, is de resulterende kracht op zijn lichaam gelijk aan nul (Fres = 0 N).",
      "antwoord": True,
      "uitleg": "Waar. Bij de constante eindsnelheid is de opwaartse luchtweerstandskracht precies even groot geworden als de neerwaartse zwaartekracht (Fw,l = Fz). De resulterende kracht is dan 0 N."
    },
    {
      "type": "invul",
      "vraag": "Een doos van 18 kg staat stil op de vloer van een magazijn. Bereken de zwaartekracht Fz op deze doos op aarde (gebruik g = 9,8 N/kg, vul het getal in met een komma of punt):",
      "antwoord": "176,4|176.4",
      "uitleg": "Fz = m · g = 18 kg · 9,8 N/kg = 176,4 N."
    },
    {
      "type": "mc",
      "vraag": "Welke maatregel vermindert de rolweerstand van een zware transportvrachtwagen het meest effectief?",
      "opties": ["De vrachtwagenbanden oppompen tot de aanbevolen hoge spanning", "Een aerodynamische dakspoiler op de cabine monteren", "De vrachtwagen lager bij het asfalt bouwen", "De ruitenwissers plat leggen tijdens het rijden"],
      "antwoord": 0,
      "uitleg": "Harde banden vervormen minder en verlagen direct de rolweerstand. Een dakspoiler vermindert de luchtweerstand, niet de rolweerstand."
    },
    {
      "type": "mc",
      "vraag": "Een kanoër peddelt op een rustig meer met een constante snelheid van 2,5 m/s. Hij oefent met zijn peddel een constante voorwaartse stuwkracht uit van 140 N. Hoe groot is de waterweerstand op de kano?",
      "opties": ["Precies 140 N", "70 N", "280 N", "0 N"],
      "antwoord": 0,
      "uitleg": "Bij constante snelheid is er sprake van krachtenevenwicht: Fres = 0 N. De tegenwerkende waterweerstand moet daarom precies gelijk zijn aan de stuwkracht: 140 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als op een bewegend voorwerp een resulterende kracht werkt die tegen de bewegingsrichting in wijst (Fres tegengesteld aan v), dan gaat het voorwerp versnellen.",
      "antwoord": False,
      "uitleg": "Onwaar. Een resulterende kracht die tegengesteld is aan de bewegingsrichting veroorzaakt een vertraging (het voorwerp remt af)."
    },
    {
      "type": "mc",
      "vraag": "Op een vrachtwagen werkt tijdens het rijden een voorwaartse motorkracht van 5000 N. De luchtweerstand bedraagt 3200 N en de rolweerstand is 1800 N. Wat is de toestand van de beweging?",
      "opties": ["De vrachtwagen rijdt met een constante snelheid", "De vrachtwagen trekt krachtig op", "De vrachtwagen remt plotseling af", "De vrachtwagen staat direct stil"],
      "antwoord": 0,
      "uitleg": "De totale tegenwerkende kracht is Ftegen = 3200 + 1800 = 5000 N. Aangezien Fvooruit = Ftegen = 5000 N, is Fres = 0 N. De vrachtwagen beweegt dus met constante snelheid."
    },
    {
      "type": "open",
      "vraag": "Leg in eigen woorden uit waarom een wielrenner bij windstil weer aanzienlijk meer moeite moet doen om zijn snelheid te verhogen van 30 km/h naar 40 km/h dan van 10 km/h naar 20 km/h.",
      "sleutelwoorden": ["luchtweerstand/wrijvingskracht", "kwadraat/kwadratisch/sterker stijgt/v²"],
      "minTreffers": 1,
      "modelantwoord": "De luchtweerstand neemt kwadratisch toe met de snelheid (v²). Bij hogere snelheden stijgt de luchtweerstand veel sterker voor elke extra km/h, waardoor er veel meer vermogen en spierkracht nodig is.",
      "uitleg": "Omdat Fw,l evenredig is met v², kost versnellen bij hoge snelheid veel meer kracht dan bij lage snelheid."
    },
    {
      "type": "mc",
      "vraag": "Een wielrenner rijdt met 36 km/h. Plotseling stopt hij met trappen. Welke krachten zorgen ervoor dat hij uiteindelijk tot stilstand komt?",
      "opties": ["De combinatie van rolweerstand en luchtweerstand", "Alleen de zwaartekracht", "De voorwaartse traagheidskracht", "De normaalkracht van het wegdek"],
      "antwoord": 0,
      "uitleg": "Zonder trappen is er geen voorwaartse kracht meer. De tegenwerkende wrijvingskrachten (rolweerstand van de banden en luchtweerstand) remmen de fietser af tot stilstand."
    },
    {
      "type": "mc",
      "vraag": "Welke vorm heeft de laagste luchtweerstandscoëfficiënt (Cw-waarde) bij gelijke frontale oppervlakte?",
      "opties": ["Een gestroomlijnde druppelvorm", "Een platte rechthoekige plaat", "Een holle halve bol gericht tegen de wind", "Een kubusvormig blok"],
      "antwoord": 0,
      "uitleg": "Een gestroomlijnde druppelvorm zorgt ervoor dat de lucht geleidelijk langs het oppervlak vloeit zonder grote wervelingen erachter, wat resulteert in de kleinste Cw-waarde."
    },
    {
      "type": "waaronwaar",
      "vraag": "De zwaartekracht op een voorwerp is op de maan kleiner dan op aarde, omdat de massa van het voorwerp op de maan afneemt.",
      "antwoord": False,
      "uitleg": "Onwaar. De massa van het voorwerp blijft overal gelijk (massa is de hoeveelheid materie). De zwaartekracht is op de maan kleiner omdat de valversnelling g op de maan veel kleiner is (ongeveer 1,6 N/kg)."
    },
    {
      "type": "invul",
      "vraag": "Een slee glijdt over de sneeuw met een voorwaartse trekkracht van 95 N. De wrijvingskracht met de sneeuw bedraagt 35 N. Bereken de resulterende kracht Fres in newton (vul alleen het getal in):",
      "antwoord": "60",
      "uitleg": "Fres = Ftrekkracht - Fwrijving = 95 N - 35 N = 60 N."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de resulterende kracht op een auto als de bestuurder het gaspedaal dieper intrapt waardoor de motorkracht groter wordt dan alle wrijvingskrachten samen?",
      "opties": ["Er ontstaat een positieve resulterende kracht in de rijrichting waardoor de auto versnelt", "De resulterende kracht blijft exact 0 N", "De auto gaat direct met een lagere constante snelheid rijden", "De auto komt meteen tot stilstand"],
      "antwoord": 0,
      "uitleg": "Als Fvooruit > Ftegen, dan is Fres > 0 in de bewegingsrichting. Het effect van een netto voorwaartse kracht is een versnelling."
    },
    {
      "type": "mc",
      "vraag": "Een lift hangt stil aan een staalkabel op de vierde verdieping. De totale massa van de lift inclusief passagiers is 800 kg. Neem g = 9,8 N/kg. Hoe groot is de spankracht in de kabel?",
      "opties": ["7840 N", "800 N", "0 N", "784 N"],
      "antwoord": 0,
      "uitleg": "Omdat de lift stilstaat, is Fres = 0 N. De opwaartse spankracht van de kabel moet gelijk zijn aan de neerwaartse zwaartekracht: Fspan = Fz = m · g = 800 · 9,8 = 7840 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "De rolweerstand van een voertuig is afhankelijk van de ruwheid en zachtheid van de ondergrond.",
      "antwoord": True,
      "uitleg": "Waar. Rijden over een zacht of modderig bospad geeft veel meer wiel- en bodemvervorming (en dus een veel hogere rolweerstand) dan rijden over glad asfalt."
    },
    {
      "type": "mc",
      "vraag": "Twee krachten werken langs dezelfde rechte lijn op een voorwerp: F1 = 120 N naar rechts en F2 = 75 N naar links. Wat is de resulterende kracht Fres?",
      "opties": ["45 N naar rechts", "195 N naar rechts", "45 N naar links", "0 N"],
      "antwoord": 0,
      "uitleg": "Omdat de krachten tegengesteld gericht zijn, trek je ze van elkaar af: Fres = 120 N - 75 N = 45 N in de richting van de grootste kracht (naar rechts)."
    },
    {
      "type": "mc",
      "vraag": "Tijdens een noodstop blokkeren de wielen van een personenauto. Welke kracht zorgt voor de vertraging van de auto?",
      "opties": ["De schuifwrijvingskracht tussen de banden en het wegdek", "De motorkracht die plotseling achteruit draait", "De normaalkracht die loodrecht omhoog werkt", "De zwaartekracht die naar beneden trekt"],
      "antwoord": 0,
      "uitleg": "Bij slippende banden zorgt de wrijvingskracht (schuifwrijving) tussen het rubber en het wegdek voor de remmende resulterende kracht."
    },
    {
      "type": "open",
      "vraag": "Beschrijf wat er gebeurt met de beweging van een parachutespringer op het moment dat hij zijn parachute opent bij een valsnelheid van 180 km/h.",
      "sleutelwoorden": ["vertraging/afremmen/remt af", "oppervlak/luchtweerstand/groter dan zwaartekracht"],
      "minTreffers": 1,
      "modelantwoord": "Het openen van het doek vergroot het frontale oppervlak enorm, waardoor de opwaartse luchtweerstand plotseling veel groter wordt dan de zwaartekracht. Hierdoor ontstaat een grote resulterende kracht omhoog en vertraagt de springer snel tot een veilige landingssnelheid.",
      "uitleg": "Door de enorme toename van Fw,l ontstaat een netto opwaartse remkracht waardoor de valsnelheid sterk afneemt."
    },
    {
      "type": "mc",
      "vraag": "Een sleepboot trekt een zeeschip met een constante snelheid de haven in. Welke bewering over de krachten is juist?",
      "opties": ["De trekkracht van de sleepboot is even groot als de totale wrijvingskracht van het water op het schip", "De trekkracht van de sleepboot is veel groter dan de wrijvingskracht", "De wrijvingskracht van het water is groter dan de trekkracht", "Er werken geen krachten op het schip"],
      "antwoord": 0,
      "uitleg": "Omdat de snelheid constant is, is de resulterende kracht nul. De voorwaartse trekkracht van de kabel is dus precies even groot als de tegenwerkende waterweerstand."
    },
    {
      "type": "mc",
      "vraag": "Waarom monteren raceauto's spoilers en een gladde bodemplaat?",
      "opties": ["Om de luchtstroming te optimaliseren en turbulentie/luchtweerstand te minimaliseren", "Om het gewicht van de auto te vergroten voor meer rolweerstand", "Om de zwaartekracht naar voren te buigen", "Om meer wrijving met de lucht te genereren"],
      "antwoord": 0,
      "uitleg": "Een aerodynamische vorm en gladde onderkant verminderen wervelingen en luchtweerstand, waardoor de auto met hetzelfde motorvermogen een hogere snelheid kan bereiken."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 46: §1.2 Soorten beweging & Diagrammen — Toets D (25 vragen)
# -------------------------------------------------------------
ex46 = {
  "id": "ex-h3-natuurkunde-46",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Toets 46 — §1.2 Soorten beweging & Diagrammen — Toets D (25 vragen)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "📈",
  "duurMin": 35,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Reken een snelheid van 90 km/h om naar meters per seconde (m/s):",
      "opties": ["25 m/s", "324 m/s", "20 m/s", "15 m/s"],
      "antwoord": 0,
      "uitleg": "Omrekenen van km/h naar m/s doe je door te delen door 3,6: 90 / 3,6 = 25 m/s."
    },
    {
      "type": "mc",
      "vraag": "Een sprinter legt een afstand van 100 meter af in precies 12,5 seconden. Wat is zijn gemiddelde snelheid vgem?",
      "opties": ["8,0 m/s", "12,5 m/s", "6,4 m/s", "9,8 m/s"],
      "antwoord": 0,
      "uitleg": "vgem = s / t = 100 m / 12,5 s = 8,0 m/s."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een afstand-tijd-diagram ((s,t)-diagram) stelt een horizontale rechte lijn voor dat het voorwerp stilstaat.",
      "antwoord": True,
      "uitleg": "Waar. Als de afstand s in de tijd t niet verandert, is de snelheid v = 0 m/s (het voorwerp staat stil)."
    },
    {
      "type": "invul",
      "vraag": "Reken een snelheid van 15 m/s om naar kilometer per uur (km/h, vul alleen het getal in):",
      "antwoord": "54",
      "uitleg": "Van m/s naar km/h vermenigvuldig je met 3,6: 15 · 3,6 = 54 km/h."
    },
    {
      "type": "mc",
      "vraag": "Hoe kun je in een (s,t)-diagram direct zien welk van twee bewegende voorwerpen de grootste snelheid heeft?",
      "opties": ["De grafieklijn met de steilste helling hoort bij de grootste snelheid", "De grafieklijn die het dichtst bij de horizontale as ligt", "De grafieklijn met de langste tijdsduur", "De grafieklijn die het vroegst begint"],
      "antwoord": 0,
      "uitleg": "De steilheid (helling) van de grafiek in een (s,t)-diagram stelt de snelheid voor: steilere lijn = grotere afstand per seconde = hogere snelheid."
    },
    {
      "type": "mc",
      "vraag": "Een auto rijdt met een constante snelheid van 20 m/s gedurende 15 seconden. Hoe groot is de afgelegde afstand s?",
      "opties": ["300 meter", "75 meter", "150 meter", "450 meter"],
      "antwoord": 0,
      "uitleg": "Bij een constante snelheid geldt: s = v · t = 20 m/s · 15 s = 300 meter."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een snelheid-tijd-diagram ((v,t)-diagram) kun je de afgelegde afstand bepalen door de oppervlakte onder de grafieklijn te berekenen.",
      "antwoord": True,
      "uitleg": "Waar. De oppervlakte onder de grafiek in een (v,t)-diagram komt overeen met de afgelegde afstand s (oppervlakte = v · t)."
    },
    {
      "type": "invul",
      "vraag": "Een trein versnelt eenparig vanuit stilstand (vbegin = 0 m/s) in 20 seconden naar een eindsnelheid van 30 m/s. Bereken de afgelegde afstand s in meters (vul alleen het getal in):",
      "antwoord": "300",
      "uitleg": "Voor een eenparige versnelling vanuit stilstand geldt de oppervlakte van een driehoek: s = 0,5 · basis · hoogte = 0,5 · 20 s · 30 m/s = 300 meter."
    },
    {
      "type": "mc",
      "vraag": "Wat voor soort beweging wordt weergegeven door een dalende rechte lijn in een (v,t)-diagram?",
      "opties": ["Een eenparig vertraagde beweging (gelijkmatig afremmen)", "Een eenparig versnelde beweging", "Een constante snelheid achteruit", "Een voorwerp dat stilstaat"],
      "antwoord": 0,
      "uitleg": "Een rechte dalende lijn in een (v,t)-diagram betekent dat de snelheid elke seconde met een vaste hoeveelheid afneemt: eenparig vertraagd."
    },
    {
      "type": "mc",
      "vraag": "Een wielrenner rijdt in 2,5 uur een afstand van 75 kilometer. Wat is zijn gemiddelde snelheid in km/h?",
      "opties": ["30 km/h", "25 km/h", "35 km/h", "20 km/h"],
      "antwoord": 0,
      "uitleg": "vgem = s / t = 75 km / 2,5 h = 30 km/h."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als een grafieklijn in een (s,t)-diagram steeds steiler omhoog buigt (een kromme lijn naar boven), dan rijdt het voertuig met een constante snelheid.",
      "antwoord": False,
      "uitleg": "Onwaar. Een steeds steiler wordende lijn in een (s,t)-diagram betekent dat de snelheid toeneemt; het voertuig versnelt dus."
    },
    {
      "type": "mc",
      "vraag": "Een metro versnelt vanuit stilstand naar 18 m/s in een tijd van 6,0 seconden. Bereken de versnelling a in m/s²:",
      "opties": ["3,0 m/s²", "108 m/s²", "0,33 m/s²", "12 m/s²"],
      "antwoord": 0,
      "uitleg": "Versnelling a = Δv / Δt = (18 - 0) m/s / 6,0 s = 3,0 m/s²."
    },
    {
      "type": "open",
      "vraag": "Op een stroboscopische foto van een rijdende speelgoedauto zie je dat de afstand tussen twee opeenvolgende lichtflitsen steeds kleiner wordt. Leg uit wat dit zegt over de beweging van de speelgoedauto.",
      "sleutelwoorden": ["vertraagt/vertraging/afremmen/langzamer", "minder afstand/minder meters"],
      "minTreffers": 1,
      "modelantwoord": "Omdat de tijd tussen twee flitsen constant is, legt de auto in elke tijdsinterval steeds minder afstand af. Dit betekent dat de snelheid afneemt en de auto dus vertraagt (afremt).",
      "uitleg": "Bij constante flitsintervallen betekent een kortere tussenafstand dat de snelheid daalt (vertraging)."
    },
    {
      "type": "mc",
      "vraag": "Een scooterrijder rijdt eerst 10 seconden met een constante snelheid van 10 m/s en remt daarna in 4 seconden eenparig af tot stilstand. Wat is de totale afgelegde afstand?",
      "opties": ["120 meter", "140 meter", "100 meter", "80 meter"],
      "antwoord": 0,
      "uitleg": "Deel 1 (constante snelheid): s1 = v · t = 10 · 10 = 100 m. Deel 2 (afremmen, driehoek): s2 = 0,5 · v · t = 0,5 · 10 · 4 = 20 m. Totaal = 100 + 20 = 120 meter."
    },
    {
      "type": "mc",
      "vraag": "Wat is de gemiddelde snelheid van een voertuig dat eenparig versnelt van 10 m/s naar 30 m/s?",
      "opties": ["20 m/s", "15 m/s", "25 m/s", "40 m/s"],
      "antwoord": 0,
      "uitleg": "Bij een eenparige versnelling is vgem precies het gemiddelde van begin- en eindsnelheid: vgem = (vbegin + veind) / 2 = (10 + 30) / 2 = 20 m/s."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een snelheid van 72 km/h is gelijk aan 20 m/s.",
      "antwoord": True,
      "uitleg": "Waar. 72 / 3,6 = 20 m/s (of omgekeerd: 20 · 3,6 = 72 km/h)."
    },
    {
      "type": "invul",
      "vraag": "Een vliegtuig vliegt met een kruissnelheid van 900 km/h. Bereken hoe ver het toestel vliegt in 20 minuten (vul het aantal kilometers in):",
      "antwoord": "300",
      "uitleg": "20 minuten is 20/60 = 1/3 uur. s = v · t = 900 km/h · (1/3) h = 300 km."
    },
    {
      "type": "mc",
      "vraag": "In een (v,t)-diagram is de grafieklijn een horizontale rechte lijn op de as v = 0 m/s. Wat doet het voorwerp?",
      "opties": ["Het voorwerp staat stil", "Het beweegt met een constante snelheid", "Het versnelt met 1 m/s²", "Het rijdt achteruit"],
      "antwoord": 0,
      "uitleg": "Als v = 0 m/s gedurende de tijd, is de snelheid nul en staat het voorwerp stil."
    },
    {
      "type": "mc",
      "vraag": "Een hardloper rent 400 meter in 80 seconden, rust 20 seconden uit, en wandelt daarna 200 meter terug in 100 seconden. Wat is zijn gemiddelde snelheid over de totale tijd van 200 seconden?",
      "opties": ["3,0 m/s", "4,0 m/s", "2,0 m/s", "5,0 m/s"],
      "antwoord": 0,
      "uitleg": "Totale afstand s = 400 + 200 = 600 m. Totale tijd t = 80 + 20 + 100 = 200 s. vgem = stotaal / ttotaal = 600 / 200 = 3,0 m/s."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een (v,t)-diagram heeft een eenparig vertraagde beweging altijd een horizontale grafieklijn.",
      "antwoord": False,
      "uitleg": "Onwaar. Een eenparig vertraagde beweging heeft een schuin omlaag lopende rechte lijn in een (v,t)-diagram. Een horizontale lijn betekent een constante snelheid."
    },
    {
      "type": "mc",
      "vraag": "Een personenauto remt op een natte weg af van 25 m/s naar stilstand in 5,0 seconden. Bereken de vertraging a in m/s²:",
      "opties": ["5,0 m/s²", "125 m/s²", "2,5 m/s²", "10 m/s²"],
      "antwoord": 0,
      "uitleg": "De verandering van snelheid is Δv = 25 m/s. a = Δv / t = 25 / 5,0 = 5,0 m/s²."
    },
    {
      "type": "mc",
      "vraag": "Hoe lang doet een geluidssignaal (snelheid v = 340 m/s) erover om een afstand van 1700 meter af te leggen door de lucht?",
      "opties": ["5,0 seconden", "2,0 seconden", "0,2 seconden", "578 seconden"],
      "antwoord": 0,
      "uitleg": "t = s / v = 1700 m / 340 m/s = 5,0 s."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom men bij een kromme lijn in een (v,t)-diagram de totale afgelegde weg kan bepalen door het tellen van roostervierkantjes.",
      "sleutelwoorden": ["oppervlak/oppervlakte", "breedte maal hoogte/tijd maal snelheid/meters/v maal t"],
      "minTreffers": 1,
      "modelantwoord": "De afgelegde weg komt overeen met de oppervlakte onder de (v,t)-grafiek. Elk roostervierkantje heeft een vaste breedte (tijd) en hoogte (snelheid), waardoor één vierkantje een vast aantal meters vertegenwoordigt (v · t). Het totaal aantal vierkantjes levert zo de totale afstand op.",
      "uitleg": "De totale oppervlakte onder de (v,t)-lijn geeft de afstand; door roostervierkantjes op te tellen bereken je die oppervlakte (Δv · Δt)."
    },
    {
      "type": "mc",
      "vraag": "Een schaatser legt een ronde van 400 meter af met een constante snelheid van 10 m/s. Hoeveel seconden duurt deze ronde?",
      "opties": ["40 seconden", "25 seconden", "4000 seconden", "4 seconden"],
      "antwoord": 0,
      "uitleg": "t = s / v = 400 m / 10 m/s = 40 s."
    },
    {
      "type": "mc",
      "vraag": "Welke eenheid hoort bij de versnelling in het SI-stelsel?",
      "opties": ["m/s²", "m/s", "km/h", "N/kg"],
      "antwoord": 0,
      "uitleg": "Versnelling is de toename van de snelheid per seconde: (m/s) / s = m/s²."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 47: §1.3 Kracht en versnelling — Toets D (25 vragen)
# -------------------------------------------------------------
ex47 = {
  "id": "ex-h3-natuurkunde-47",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Toets 47 — §1.3 Kracht en versnelling — Toets D (25 vragen)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🚀",
  "duurMin": 35,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke formule geeft de tweede wet van Newton weer?",
      "opties": ["Fres = m · a", "v = s / t", "Fz = m / g", "p = F / A"],
      "antwoord": 0,
      "uitleg": "De tweede wet van Newton luidt: Fres = m · a, waarin Fres de resulterende kracht is in newton (N), m de massa in kilogram (kg) en a de versnelling in m/s²."
    },
    {
      "type": "mc",
      "vraag": "Een kart met coureur heeft een totale massa van 150 kg. Tijdens het optrekken bedraagt de versnelling 4,0 m/s². Hoe groot is de resulterende kracht Fres?",
      "opties": ["600 N", "37,5 N", "154 N", "60 N"],
      "antwoord": 0,
      "uitleg": "Fres = m · a = 150 kg · 4,0 m/s² = 600 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een constante resulterende kracht is de versnelling van een voorwerp omgekeerd evenredig met zijn massa: een twee keer zo zwaar voorwerp krijgt bij dezelfde kracht een twee keer zo kleine versnelling.",
      "antwoord": True,
      "uitleg": "Waar. Volgens a = Fres / m leidt een verdubbeling van de massa bij gelijkblijvende kracht tot een halvering van de versnelling."
    },
    {
      "type": "invul",
      "vraag": "Op een bal met een massa van 0,5 kg werkt een netto slagkracht Fres van 40 N. Bereken de versnelling van de bal in m/s² (vul alleen het getal in):",
      "antwoord": "80",
      "uitleg": "a = Fres / m = 40 N / 0,5 kg = 80 m/s²."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'massatraagheid' (inertie) in de natuurkunde?",
      "opties": ["Het verschijnsel dat een voorwerp zich verzet tegen een verandering van zijn snelheid of richting", "Dat zware voorwerpen altijd langzamer vallen in een vacuüm", "Dat elk voorwerp na verloop van tijd vanzelf tot stilstand komt", "De wrijvingskracht die optreedt bij het rollen over asfalt"],
      "antwoord": 0,
      "uitleg": "Massatraagheid is de eigenschap van materie om zijn bewegingstoestand (snelheid en richting) te behouden tenzij er een resulterende kracht op werkt."
    },
    {
      "type": "mc",
      "vraag": "Waarom heeft een zwaar beladen goederentrein van 1.200.000 kg een veel langere remweg dan een lege trein van 300.000 kg bij dezelfde remkracht?",
      "opties": ["Vanwege de veel grotere massatraagheid heeft de zware trein een veel kleinere vertraging", "Omdat de zware trein minder rolweerstand ondervindt", "Omdat de zwaartekracht op de zware trein naar voren is gericht", "Omdat de snelheid van een zware trein automatisch toeneemt"],
      "antwoord": 0,
      "uitleg": "Volgens a = Fres / m levert dezelfde remkracht op een vier keer zo grote massa een vier keer zo kleine vertraging op (a is kleiner), waardoor de remweg veel langer wordt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om de tweede wet van Newton (Fres = m · a) correct toe te passen, moet de massa m altijd worden ingevuld in gram (g).",
      "antwoord": False,
      "uitleg": "Onwaar. In het SI-stelsel is de standaardeenheid voor massa de kilogram (kg). Massa's in grammen moeten eerst worden gedeeld door 1000."
    },
    {
      "type": "invul",
      "vraag": "Een personenauto met een massa van 1200 kg trekt op met een constante versnelling van 2,5 m/s². Bereken de resulterende kracht Fres in newton (vul alleen het getal in):",
      "antwoord": "3000",
      "uitleg": "Fres = m · a = 1200 kg · 2,5 m/s² = 3000 N."
    },
    {
      "type": "mc",
      "vraag": "Een tennisbal van 60 gram (0,060 kg) wordt geraakt door een racket en versnelt met 2500 m/s². Hoe groot is de resulterende slagkracht op de bal?",
      "opties": ["150 N", "150.000 N", "25 N", "15 N"],
      "antwoord": 0,
      "uitleg": "Fres = m · a = 0,060 kg · 2500 m/s² = 150 N."
    },
    {
      "type": "mc",
      "vraag": "Als op een voorwerp met massa m een resulterende kracht Fres werkt, krijgt het een versnelling a. Wat gebeurt er met de versnelling als de resulterende kracht 3 keer zo groot wordt gemaakt?",
      "opties": ["De versnelling wordt ook 3 keer zo groot", "De versnelling wordt 9 keer zo groot", "De versnelling wordt 3 keer zo klein", "De versnelling blijft hetzelfde"],
      "antwoord": 0,
      "uitleg": "Versnelling en resulterende kracht zijn recht evenredig: a = Fres / m. Als Fres verdrievoudigt, verdrievoudigt a ook."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij actie en reactie (de derde wet van Newton) werken de twee krachten altijd op hetzelfde voorwerp en heffen ze elkaar daarom altijd op.",
      "antwoord": False,
      "uitleg": "Onwaar. Actie en reactie werken altijd op TWEE VERSCHILLENDE voorwerpen (bijv. voet duwt tegen bal en bal duwt tegen voet). Ze heffen elkaar dus niet op!"
    },
    {
      "type": "mc",
      "vraag": "Tijdens een botsingtest van een auto oefent de muur een reactiekracht uit van 45.000 N op de voorkant van de auto. Hoe groot is de actiekracht die de auto op de muur uitoefent?",
      "opties": ["Precies 45.000 N", "0 N", "22.500 N", "90.000 N"],
      "antwoord": 0,
      "uitleg": "Volgens de derde wet van Newton (actie = -reactie) zijn de twee krachten precies even groot en tegengesteld gericht: Factie = Freactie = 45.000 N."
    },
    {
      "type": "open",
      "vraag": "Twee schaatsers, Lisa (50 kg) en Tom (80 kg), staan stil tegenover elkaar op spiegelglad ijs. Lisa duwt Tom met haar handen weg. Leg uit wie van beiden na de duw de grootste snelheid krijgt en waarom.",
      "sleutelwoorden": ["Lisa", "kleinere massa/lichter", "grotere versnelling/a = F/m"],
      "minTreffers": 1,
      "modelantwoord": "Volgens de derde wet van Newton oefenen ze tijdens het duwen een even grote kracht op elkaar uit. Omdat Lisa een kleinere massa heeft (50 kg < 80 kg), krijgt zij volgens a = F/m een grotere versnelling en bereikt zij dus de grootste snelheid.",
      "uitleg": "De krachten zijn gelijk (actie=-reactie). De schaatser met de kleinste massa krijgt de grootste versnelling en dus de hoogste snelheid."
    },
    {
      "type": "mc",
      "vraag": "Een scooter van 100 kg versnelt vanuit stilstand naar 20 m/s in 8,0 seconden. Bereken de benodigde resulterende kracht Fres:",
      "opties": ["250 N", "2000 N", "160 N", "50 N"],
      "antwoord": 0,
      "uitleg": "Eerst versnelling berekenen: a = Δv / t = 20 / 8,0 = 2,5 m/s². Vervolgens Fres = m · a = 100 kg · 2,5 m/s² = 250 N."
    },
    {
      "type": "mc",
      "vraag": "Een raceauto met een massa van 800 kg ondervindt tijdens het optrekken een totale wrijvingskracht van 1200 N. De motor levert een voorwaartse kracht van 5200 N. Wat is de versnelling van de auto?",
      "opties": ["5,0 m/s²", "6,5 m/s²", "1,5 m/s²", "4,0 m/s²"],
      "antwoord": 0,
      "uitleg": "Fres = Fmotor - Fwrijving = 5200 N - 1200 N = 4000 N. Versnelling a = Fres / m = 4000 N / 800 kg = 5,0 m/s²."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een raket kan in het luchtledige van de ruimte versnellen doordat de uitgestoten verbrandingsgassen naar achteren een reactiekracht naar voren uitoefenen op de raket.",
      "antwoord": True,
      "uitleg": "Waar. Dit is een direct gevolg van de derde wet van Newton: de raket duwt het gas naar achteren (actie), en het gas duwt de raket naar voren (reactie). Er is geen lucht nodig om tegen af te zetten."
    },
    {
      "type": "invul",
      "vraag": "Een atleet met een massa van 70 kg versnelt vanuit de startblokken met een resulterende kracht van 420 N. Bereken zijn versnelling in m/s² (vul alleen het getal in):",
      "antwoord": "6|6,0|6.0",
      "uitleg": "a = Fres / m = 420 N / 70 kg = 6,0 m/s²."
    },
    {
      "type": "mc",
      "vraag": "Een vrachtwagen rijdt met 80 km/h. De bestuurder remt krachtig af. Een losliggende kist op de laadvloer schuift naar voren tegen de cabine. Welke natuurkundige verklaring hoort hierbij?",
      "opties": ["Door de massatraagheid wil de kist zijn voorwaartse snelheid van 80 km/h behouden terwijl de truck vertraagt", "Er werkt een mysterieuze magische voorwaartse kracht op de kist", "De zwaartekracht trekt de kist plotseling naar voren", "De wrijvingskracht van de laadvloer duwt de kist naar voren"],
      "antwoord": 0,
      "uitleg": "Door massatraagheid behoudt een voorwerp zijn snelheid. Als de vrachtwagen afremt, blijft de kist met de oorspronkelijke snelheid vooruit bewegen totdat een kracht hem stopt."
    },
    {
      "type": "mc",
      "vraag": "Een liftcabine met een massa van 500 kg versnelt omhoog met 1,5 m/s². Neem g = 9,8 N/kg. Hoe groot is de opwaartse trekkracht Fkabel in de staalkabel?",
      "opties": ["5650 N", "4900 N", "750 N", "4150 N"],
      "antwoord": 0,
      "uitleg": "De zwaartekracht naar beneden is Fz = m · g = 500 · 9,8 = 4900 N. Voor een opwaartse versnelling is een netto kracht nodig van Fres = m · a = 500 · 1,5 = 750 N. Fkabel = Fz + Fres = 4900 + 750 = 5650 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als twee voorwerpen met verschillende massa's met dezelfde resulterende kracht worden voortgeduwd, krijgt het voorwerp met de grootste massa ook de grootste versnelling.",
      "antwoord": False,
      "uitleg": "Onwaar. Volgens a = Fres / m krijgt het zwaarste voorwerp juist de kleinste versnelling (omgekeerd evenredig verband)."
    },
    {
      "type": "mc",
      "vraag": "Een ijshockeypuck van 160 gram (0,16 kg) glijdt over het ijs en ondervindt een wrijvingskracht van 0,32 N. Wat is de vertraging van de puck?",
      "opties": ["2,0 m/s²", "0,051 m/s²", "0,50 m/s²", "5,0 m/s²"],
      "antwoord": 0,
      "uitleg": "a = Fres / m = 0,32 N / 0,16 kg = 2,0 m/s²."
    },
    {
      "type": "mc",
      "vraag": "Waarom is het verplicht om in een auto een veiligheidsgordel te dragen?",
      "opties": ["Om bij een botsing de noodzakelijke remkracht op het lichaam uit te oefenen zodat het niet door massatraagheid naar voren schiet", "Om de massa van de inzittenden te verkleinen", "Om de motor van de auto meer trekkracht te geven", "Om de zwaartekracht op te heffen"],
      "antwoord": 0,
      "uitleg": "Bij een plotselinge stop blijft het lichaam van de inzittende door massatraagheid met de oude snelheid naar voren bewegen. De veiligheidsgordel oefent de vereiste tegenkracht uit om het lichaam veilig mee af te remmen."
    },
    {
      "type": "open",
      "vraag": "Een geweer vuurt een kogel af. Tijdens het schot ervaart de schutter een voelbare 'terugslag' tegen zijn schouder. Verklaar dit verschijnsel met een natuurkundige wet.",
      "sleutelwoorden": ["derde wet van newton/actie en reactie/actie is reactie", "kracht op kogel/kracht op geweer/tegengesteld"],
      "minTreffers": 1,
      "modelantwoord": "Volgens de derde wet van Newton (actie = -reactie) treden krachten altijd in paren op. Het geweer oefent een grote voorwaartse kracht uit op de kogel om deze te versnellen; tegelijkertijd oefent de kogel een even grote, maar achterwaarts gerichte reactiekracht uit op het geweer.",
      "uitleg": "De terugslag is de reactiekracht van de kogel op het geweer (3e wet van Newton: Factie = -Freactie)."
    },
    {
      "type": "mc",
      "vraag": "Een vliegtuig met een massa van 60.000 kg heeft een startversnelling van 2,0 m/s². De wrijving met de landingsbaan en lucht is 30.000 N. Hoe groot moet de stuwkracht van de straalmotoren samen zijn?",
      "opties": ["150.000 N", "120.000 N", "90.000 N", "60.000 N"],
      "antwoord": 0,
      "uitleg": "Voor de versnelling is een resulterende kracht nodig van Fres = m · a = 60.000 · 2,0 = 120.000 N. Omdat Fstuw - Fwrijving = Fres, geldt Fstuw = Fres + Fwrijving = 120.000 + 30.000 = 150.000 N."
    },
    {
      "type": "mc",
      "vraag": "Welke combinatie van grootheden en SI-eenheden in de formule Fres = m · a is correct?",
      "opties": ["Kracht in newton (N), massa in kilogram (kg), versnelling in meter per seconde kwadraat (m/s²)", "Kracht in joule (J), massa in gram (g), versnelling in m/s", "Kracht in watt (W), massa in kg, versnelling in km/h", "Kracht in newton (N), massa in gram (g), versnelling in m/s²"],
      "antwoord": 0,
      "uitleg": "In het SI-stelsel geldt: 1 newton (N) = 1 kg · m/s²."
    }
  ]
}

if __name__ == "__main__":
    write_examen("examen_45.js", ex45)
    write_examen("examen_46.js", ex46)
    write_examen("examen_47.js", ex47)
    print("\n🎉 Alle 3 Natuurkunde Toetsen (25 vragen elk) succesvol aangemaakt!")
