#!/usr/bin/env python3
# Genereert natuurkunde examen_66/67/68 (§1.1 Kracht bij beweging, Toets E/F/G)
import json, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'havo3', 'natuurkunde', 'js', 'data')

def mc(v, juist, fout, pos, u):
    o = list(fout); o.insert(pos, juist)
    assert len(o) == 4
    return {"type": "mc", "vraag": v, "opties": o, "antwoord": pos, "uitleg": u}

def ww(v, ant, u):
    return {"type": "waaronwaar", "vraag": v, "antwoord": ant, "uitleg": ("Waar: " if ant else "Onwaar: ") + u}

def inv(v, waarde, eenh, u, alt=()):
    s = ('%g' % waarde)
    c = s.replace('.', ',')
    a = [c] if c == s else [c, s]
    a += [x + ' ' + eenh for x in a]
    a += list(alt)
    return {"type": "invul", "vraag": v, "antwoord": "|".join(a), "uitleg": u}

def op(v, model, kw, u):
    return {"type": "open", "vraag": v, "modelantwoord": model, "minTreffers": 1, "sleutelwoorden": kw, "uitleg": u}

def write(nr, letter, vragen):
    assert len(vragen) == 20
    t = [q['type'] for q in vragen]
    assert (t.count('mc'), t.count('waaronwaar'), t.count('invul'), t.count('open')) == (11, 4, 4, 1)
    ww_t = [q['antwoord'] for q in vragen if q['type'] == 'waaronwaar']
    assert sum(ww_t) == 2
    titel = f"Toets {nr} — §1.1 Kracht bij beweging — Toets {letter}"
    d = {"id": f"ex-h3-natuurkunde-{nr}", "hoofdstuk": 1, "paragraaf": "1.1", "titel": titel,
         "vak": "Natuurkunde · HAVO 3 (H1)", "icoon": "🚴", "duurMin": 30, "vragen": vragen}
    kop = (f"/* =========================================================\n"
           f"   Duru's Natuurkunde (HAVO 3) — {titel}\n"
           f"   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)\n"
           f"   ========================================================= */\n")
    with open(os.path.join(OUT, f"examen_{nr}.js"), 'w', encoding='utf-8') as f:
        f.write(kop + "DURU.registerExamen(" + json.dumps(d, ensure_ascii=False, indent=2) + ");\n")
    print(nr, 'mc-posities', [q['antwoord'] for q in vragen if q['type'] == 'mc'])

# ---------------- Toets E (basis) ----------------
assert 4800 - 1950 == 2850
assert round(8.0 * 9.81, 2) == 78.48
assert 85 + 70 - 120 == 35
assert 4.5 * 30 == 135
E = [
 mc("Welke grootheid zet je op de <b>horizontale as</b> van een (v,t)-diagram?",
    "De tijd t in seconden", ["De snelheid v in m/s", "De afstand s in meter", "De kracht F in newton"], 1,
    "In een (v,t)-diagram staat de tijd op de horizontale as en de snelheid op de verticale as."),
 mc("Een trein trekt op en wordt elke seconde precies 2 m/s sneller. Welk soort beweging is dit?",
    "Een eenparig versnelde beweging", ["Een eenparige beweging", "Een eenparig vertraagde beweging", "Een beweging met Fres = 0 N"], 3,
    "Neemt de snelheid elke seconde met dezelfde hoeveelheid toe, dan is de beweging eenparig versneld."),
 mc("Een boek ligt stil op een tafel. Wat geldt er voor de resulterende kracht op het boek?",
    "Fres is 0 N: de krachten heffen elkaar op", ["Fres wijst omlaag, want de zwaartekracht werkt altijd", "Fres wijst omhoog, want de tafel duwt terug", "Fres is net zo groot als de zwaartekracht"], 0,
    "Het boek staat stil, dus de resulterende kracht is nul: de zwaartekracht en de kracht van de tafel zijn even groot en tegengesteld."),
 mc("Een kist wordt met 3 N naar rechts en met 5 N naar links getrokken. Wat is de richting van de resulterende kracht?",
    "Naar links, in de richting van de grootste kracht", ["Naar rechts, omdat de kleinste kracht wint", "Naar links, want de krachten tellen op tot 8 N", "Naar rechts, want de krachten tellen op tot 8 N"], 1,
    "Tegengestelde krachten trek je van elkaar af; Fres wijst in de richting van de grootste kracht."),
 mc("Een (v,t)-diagram toont drie delen: eerst een stijgende rechte lijn, dan een horizontale lijn en tot slot een dalende rechte lijn. Welke volgorde van bewegingen hoort hierbij?",
    "Eenparig versneld, eenparig, eenparig vertraagd", ["Eenparig vertraagd, eenparig, eenparig versneld", "Eenparig, eenparig versneld, eenparig vertraagd", "Eenparig versneld, eenparig vertraagd, eenparig"], 1,
    "Stijgende lijn = snelheid neemt toe, horizontale lijn = constante snelheid, dalende lijn = snelheid neemt af."),
 mc("Een trein rijdt met een constante snelheid van 90 km/h over een recht stuk spoor. Welke uitspraak over de krachten klopt?",
    "De motorkracht is even groot als de totale weerstand", ["De motorkracht is groter dan de totale weerstand", "De motorkracht is kleiner dan de totale weerstand", "Er werkt geen enkele weerstandskracht op de trein"], 3,
    "Bij een constante snelheid is Fres = 0 N, dus Fmotor = Ftegen."),
 mc("Welke grafiek in een (v,t)-diagram hoort bij een vertraagde beweging die <b>niet</b> eenparig vertraagd is?",
    "Een dalende lijn die gekromd is", ["Een dalende rechte lijn", "Een horizontale lijn", "Een stijgende gekromde lijn"], 0,
    "Neemt de snelheid af maar niet met steeds dezelfde hoeveelheid per seconde, dan is de lijn dalend maar niet recht."),
 mc("Met welke formule bereken je de zwaartekracht op een voorwerp met massa m?",
    "Fz = m · g", ["Fz = m / g", "Fz = g / m", "Fz = m + g"], 2,
    "De zwaartekracht is massa maal valversnelling: Fz = m · g, met g = 9,81 N/kg."),
 mc("Een vel papier valt langzamer naar beneden dan hetzelfde vel als het tot een prop is gevouwen. Wat is de oorzaak?",
    "Op het vel is de luchtweerstand groter dan op de prop", ["Het vel heeft een andere zwaartekracht, want de massa verandert", "Op het vel werkt geen zwaartekracht, alleen luchtweerstand", "De prop wordt door de lucht naar beneden geduwd"], 3,
    "De massa en dus de zwaartekracht blijven gelijk, maar het vel heeft meer oppervlak en dus meer luchtweerstand."),
 mc("Welk symbool met omschrijving hoort bij de <b>resulterende kracht</b>?",
    "Fres, de som van alle krachten op het voorwerp", ["Fz, de kracht waarmee de aarde aan het voorwerp trekt", "Fmotor, de kracht die een voertuig vooruit duwt", "Ftegen, de som van lucht- en rolweerstand"], 1,
    "De resulterende kracht Fres is de som van alle krachten die op het voorwerp werken."),
 mc("Welke omschrijving past het best bij het begrip <b>snelheid</b>?",
    "De afstand die een voorwerp per seconde aflegt", ["De tijd die een voorwerp nodig heeft voor één meter", "De som van alle krachten op een voorwerp", "De kracht die een voorwerp vooruit duwt"], 2,
    "Snelheid is de afstand die je per seconde aflegt; de eenheid is m/s of km/h."),
 ww("Als de som van alle krachten op een voorwerp 0 N is, kan het voorwerp toch met een constante snelheid blijven bewegen.", True,
    "Fres = 0 N betekent dat de snelheid niet verandert: het voorwerp staat stil of beweegt met constante snelheid."),
 ww("In een (v,t)-diagram is de grafiek van een eenparig versnelde beweging een horizontale lijn.", False,
    "een horizontale lijn hoort bij een constante snelheid. Eenparig versneld geeft een stijgende rechte lijn."),
 ww("De zwaartekracht op een voorwerp wordt groter als de massa van het voorwerp groter wordt.", True,
    "Fz = m · g: bij dezelfde g geldt een grotere massa, dus een grotere zwaartekracht."),
 ww("Krachten die in dezelfde richting werken, trek je van elkaar af om de resulterende kracht te vinden.", False,
    "krachten in dezelfde richting werken samen en tel je bij elkaar op. Alleen tegengestelde krachten trek je van elkaar af."),
 inv("Een sleepboot trekt met 4800 N naar voren. De totale waterweerstand is 1950 N naar achteren. Bereken de resulterende kracht in N.",
     4800 - 1950, "N", "Fres = 4800 N − 1950 N = 2850 N, naar voren."),
 inv("Een voorwerp heeft een massa van 8,0 kg. Bereken de zwaartekracht in N (g = 9,81 N/kg).",
     78.48, "N", "Fz = m · g = 8,0 kg · 9,81 N/kg = 78,48 N.", alt=["78,5", "78.5", "78,5 N", "78"]),
 inv("Lars trekt met 85 N en Mila met 70 N een slee naar rechts. De wrijvingskracht van de sneeuw is 120 N naar links. Hoe groot is de resulterende kracht in N?",
     35, "N", "Samen trekken ze met 85 + 70 = 155 N naar rechts; Fres = 155 − 120 = 35 N naar rechts."),
 inv("Bereken de afstand in meter die een skater aflegt in 30 s, als haar snelheid steeds 4,5 m/s is.",
     135, "m", "Afstand = snelheid · tijd = 4,5 m/s · 30 s = 135 m."),
 op("Leg uit hoe je aan het (v,t)-diagram van een fietstocht kunt zien wanneer de fietser vertraagt, en wat dat zegt over de krachten die op de fietser werken.",
    "Vertraagt de fietser, dan daalt de grafiek: de snelheid neemt af. Dat betekent dat de tegenwerkende kracht (weerstand) groter is dan de voorwaartse kracht. De resulterende kracht wijst dan tegen de bewegingsrichting in.",
    ["daalt/daling/afnemen/afneemt", "tegenwerkende kracht/weerstand/tegenwerkend"],
    "Een dalende lijn betekent afnemende snelheid; dan is Ftegen > Fvoorwaarts en wijst Fres tegen de bewegingsrichting in."),
]
# mix volgorde: mc/ww/invul/open afwisselen zoals ex61 (alle mc eerst)
write(66, "E", E)

# ---------------- Toets F (gemiddeld) ----------------
assert 2150 - (640 + 410) == 1100
assert 85 - 25 == 60
assert round(686 / 9.8, 6) == 70
assert 10 / 8 * 6 == 7.5
F = [
 mc("Een basketbal valt naar beneden. De zwaartekracht op de bal is 6,0 N en de luchtweerstand is 1,5 N. Welke uitspraak klopt?",
    "De bal versnelt naar beneden met Fres = 4,5 N", ["De bal valt met een constante snelheid", "De bal vertraagt naar beneden met Fres = 4,5 N", "De bal versnelt naar beneden met Fres = 7,5 N"], 1,
    "De luchtweerstand werkt omhoog, de zwaartekracht omlaag: Fres = 6,0 − 1,5 = 4,5 N omlaag, dus de snelheid neemt toe."),
 mc("Een skater rolt zonder zich af te zetten over een vlakke weg. Welke beweging maakt zij?",
    "Een vertraagde beweging door de wrijvingskrachten", ["Een eenparige beweging, want er werkt geen kracht", "Een eenparig versnelde beweging door de zwaartekracht", "Een versnelde beweging, want de lucht duwt haar voort"], 3,
    "Rolweerstand en luchtweerstand werken tegen de beweging in en niets duwt haar vooruit: Fres wijst tegen de bewegingsrichting in."),
 mc("Een kist glijdt over de vloer en komt tot stilstand. Wat zorgt voor de vertraging?",
    "De wrijvingskracht werkt tegen de bewegingsrichting in", ["De zwaartekracht trekt de kist terug", "De kist heeft geen voorwaartse kracht meer, dus er werkt niets", "De eerdere duwkracht werkt nog na en remt af"], 0,
    "Er is geen voorwaartse kracht meer; alleen de wrijvingskracht tegen de beweging in blijft over, dus de kist vertraagt."),
 mc("Een kraan hijst een container met constante snelheid omhoog. Hoe verhoudt de kracht van de kabel zich tot de zwaartekracht?",
    "De kabelkracht is even groot als de zwaartekracht", ["De kabelkracht is groter dan de zwaartekracht", "De kabelkracht is kleiner dan de zwaartekracht", "De kabelkracht is 0 N, want de beweging is eenparig"], 0,
    "Bij een constante snelheid is Fres = 0 N: de kabelkracht omhoog is gelijk aan de zwaartekracht omlaag."),
 mc("Op een wagentje werken horizontaal twee krachten. Bij welke combinatie vertraagt het naar rechts bewegende wagentje?",
    "25 N naar rechts en 40 N naar links", ["30 N naar rechts en 20 N naar links", "45 N naar rechts en 45 N naar links", "40 N naar rechts en 25 N naar links"], 2,
    "Het wagentje vertraagt als Fres tegen de bewegingsrichting in wijst: de kracht naar links moet de grootste zijn."),
 mc("Een voorwerp start met 0 m/s en heeft na 4,0 s een snelheid van 8,0 m/s. De beweging is eenparig versneld. Wat is de snelheid na 2,0 s?",
    "4,0 m/s", ["2,0 m/s", "8,0 m/s", "6,0 m/s"], 3,
    "Bij een eenparig versnelde beweging neemt de snelheid elke seconde evenveel toe: 2,0 m/s per seconde, dus na 2,0 s is v = 4,0 m/s."),
 mc("Een auto trekt op met een constante motorkracht. Terwijl de snelheid toeneemt, wordt de luchtweerstand groter. Wat gebeurt er met de resulterende kracht?",
    "Fres neemt af, want de weerstand wordt groter", ["Fres neemt toe, want de snelheid neemt toe", "Fres blijft gelijk, want de motorkracht is constant", "Fres wordt meteen nul zodra de auto rijdt"], 1,
    "Fres = Fmotor − Ftegen. Bij een grotere Ftegen en een gelijke Fmotor wordt Fres kleiner."),
 mc("Waarom beweegt een stilstaande, zware kist niet als je er zachtjes tegenaan duwt?",
    "De wrijvingskracht is even groot als de duwkracht, dus Fres = 0 N", ["De zwaartekracht is groter dan de duwkracht, dus Fres = 0 N", "Een kracht heeft alleen effect op voorwerpen met lage massa", "De kist is te zwaar, dus de duwkracht telt niet mee"], 2,
    "De wrijvingskracht heft de duwkracht precies op; Fres = 0 N, dus de snelheid blijft 0 m/s."),
 mc("Een auto trekt op: in de eerste 6 s neemt de snelheid toe van 0 naar 12 m/s, daarna rijdt hij 10 s met 12 m/s en vervolgens remt hij in 4 s af tot stilstand. In welk tijdsinterval is Fres = 0 N?",
    "Tussen t = 6 s en t = 16 s", ["Tussen t = 0 s en t = 6 s", "Tussen t = 16 s en t = 20 s", "Op geen enkel moment"], 0,
    "Fres = 0 N als de snelheid constant is: tussen 6 s en 16 s."),
 mc("Van een scooter zijn de snelheden gemeten: bij t = 0 s is v = 20 m/s, bij 1 s is v = 16 m/s, bij 2 s is v = 12 m/s en bij 3 s is v = 8 m/s. Welk soort beweging is dit?",
    "Eenparig vertraagd", ["Eenparig versneld", "Versneld, maar niet eenparig", "Eenparig"], 3,
    "De snelheid neemt elke seconde met 4 m/s af: een eenparig vertraagde beweging."),
 mc("Welke uitspraak over de <b>luchtweerstand</b> op een bewegend voorwerp is juist?",
    "Hij werkt tegen de bewegingsrichting van het voorwerp in", ["Hij werkt altijd omlaag, in de richting van de zwaartekracht", "Hij werkt mee met de bewegingsrichting van het voorwerp", "Hij werkt alleen op voorwerpen die stilstaan"], 1,
    "De luchtweerstand is een tegenwerkende kracht: hij wijst tegen de bewegingsrichting in."),
 ww("Een auto kan met constante snelheid rijden terwijl de motor een grote kracht levert.", True,
    "als de tegenwerkende krachten even groot zijn als de motorkracht, is Fres = 0 N en blijft de snelheid constant."),
 ww("Een auto die vertraagt heeft altijd een motorkracht van 0 N.", False,
    "de motor kan nog werken; vertragen betekent alleen dat de tegenwerkende kracht groter is dan de motorkracht."),
 ww("Een voorwerp waarop een resulterende kracht van 10 N naar rechts werkt, beweegt altijd naar rechts.", False,
    "het voorwerp kan ook naar links bewegen en dan vertragen: Fres bepaalt de verandering van snelheid, niet de bewegingsrichting."),
 ww("Bij een eenparig vertraagde beweging neemt de snelheid elke seconde met dezelfde hoeveelheid af.", True,
    "dat is precies wat eenparig vertraagd betekent: een dalende rechte lijn in het (v,t)-diagram."),
 inv("Op een auto werkt een motorkracht van 2150 N. De luchtweerstand is 640 N en de rolweerstand is 410 N. Hoe groot is de resulterende kracht in N?",
     1100, "N", "Ftegen = 640 + 410 = 1050 N. Fres = 2150 − 1050 = 1100 N naar voren."),
 inv("Een fietster rijdt met constante snelheid en levert een voorwaartse kracht van 85 N. De rolweerstand is 25 N. Hoe groot is de luchtweerstand in N?",
     60, "N", "Bij constante snelheid geldt Fvoor = Ftegen = 85 N. Fluchtweerstand = 85 − 25 = 60 N."),
 inv("Op een persoon werkt een zwaartekracht van 686 N (g = 9,8 N/kg). Hoeveel kg bedraagt zijn massa?",
     70, "kg", "m = Fz / g = 686 N / 9,8 N/kg = 70 kg."),
 inv("Een scooter versnelt eenparig vanuit stilstand tot 10 m/s in 8 s. Hoeveel m/s is zijn snelheid na 6 s?",
     7.5, "m/s", "Per seconde neemt v toe met 10/8 = 1,25 m/s. Na 6 s: 1,25 · 6 = 7,5 m/s."),
 op("Een skateboarder staat stil, zet zich een paar keer af en stopt daarna met afzetten. Beschrijf per fase de resulterende kracht en de beweging.",
    "Bij het afzetten is de voorwaartse kracht groter dan de wrijving: Fres wijst naar voren en de skateboarder versnelt. Na het stoppen met afzetten werken alleen nog tegenwerkende krachten: Fres wijst tegen de beweging in, dus hij vertraagt tot hij stilstaat.",
    ["versnellen/versneld/versnelt/optrekken", "vertragen/vertraagd/vertraagt/afremmen"],
    "Voorwaartse kracht groter dan wrijving geeft versnellen; zonder voorwaartse kracht geeft de wrijving een vertraging."),
]
write(67, "F", F)

# ---------------- Toets G (toetsniveau) ----------------
assert 60 + 45 - 130 == -25
assert round(15 * 1.6, 1) == 24.0
assert round(0.40 * 9.81, 1) == 3.9
assert 24 / 60 * 45 == 18
assert 450 - 380 == 70
assert 9600 - (2100 + 1400) == 6100
assert round(0.85 * 9.81, 1) == 8.3
assert 10.5 / 14 * 8 == 6
assert 1850 / 5 == 370
G = [
 mc("Op een kar werken horizontaal drie krachten: 60 N naar rechts, 45 N naar rechts en 130 N naar links. Wat is de resulterende kracht?",
    "25 N naar links", ["25 N naar rechts", "35 N naar links", "235 N naar links"], 3,
    "Naar rechts: 60 + 45 = 105 N. Naar links: 130 N. Fres = 130 − 105 = 25 N naar links."),
 mc("Een auto rijdt met een constante snelheid. Op een zachter wegdek wordt de rolweerstand plotseling groter, terwijl de motorkracht gelijk blijft. Wat gebeurt er?",
    "De auto vertraagt, want Fmotor is kleiner dan Ftegen", ["De auto versnelt, want de rolweerstand helpt de beweging", "De snelheid blijft gelijk, want de motorkracht verandert niet", "De auto staat meteen stil, want Fres is groter dan Fmotor"], 1,
    "Door de grotere Ftegen is Fres tegen de bewegingsrichting in gericht: de snelheid neemt af."),
 mc("Een koffer heeft een massa van 15 kg. Op de maan is g = 1,6 N/kg. Hoe groot is de zwaartekracht op de koffer op de maan?",
    "24 N", ["147 N", "15 N", "9,4 N"], 2,
    "Fz = m · g = 15 kg · 1,6 N/kg = 24 N. De massa blijft 15 kg; alleen de zwaartekracht is kleiner."),
 mc("Een voorwerp met een massa van 0,40 kg valt en bereikt een constante snelheid. Hoe groot is dan de luchtweerstand (g = 9,81 N/kg)?",
    "3,9 N", ["0,41 N", "39 N", "0 N"], 2,
    "Bij constante snelheid is Fres = 0 N, dus de luchtweerstand is even groot als Fz = 0,40 · 9,81 = 3,9 N."),
 mc("Waarom tel je bij een rijdende auto op een vlakke weg de zwaartekracht niet mee voor de horizontale resulterende kracht?",
    "De zwaartekracht werkt verticaal, niet in de bewegingsrichting", ["De zwaartekracht is te klein om invloed te hebben op de auto", "De zwaartekracht werkt alleen op voorwerpen die stilstaan", "De zwaartekracht wordt altijd opgeheven door de motorkracht"], 0,
    "Voor de horizontale beweging tellen alleen horizontale krachten mee; de zwaartekracht werkt omlaag."),
 mc("Een trein versnelt eenparig vanuit stilstand tot 24 m/s in 60 s. Wat is zijn snelheid na 45 s?",
    "18 m/s", ["15 m/s", "20 m/s", "22 m/s"], 1,
    "Per seconde neemt v toe met 24/60 = 0,40 m/s. Na 45 s: 0,40 · 45 = 18 m/s."),
 mc("Een kist wordt met 200 N naar rechts geduwd en de wrijvingskracht is 200 N naar links, waardoor de kist met een constante snelheid beweegt. Plotseling komt de kist op ijs, waar de wrijving verdwijnt. Wat gebeurt er?",
    "De kist versnelt in de richting van de duwkracht", ["De kist blijft met constante snelheid bewegen", "De kist komt direct tot stilstand", "De kist vertraagt tot hij stilstaat"], 3,
    "Zonder wrijving is Fres = 200 N in de bewegingsrichting: de snelheid neemt toe."),
 mc("De trekkracht van een boot op een waterskiër stijgt van 380 N naar 450 N. De totale weerstand blijft 380 N. Wat is de resulterende kracht op de waterskiër?",
    "70 N naar voren", ["830 N naar voren", "70 N naar achteren", "450 N naar voren"], 0,
    "Fres = 450 − 380 = 70 N, in de richting van de trekkracht: de waterskiër versnelt."),
 mc("Een lift beweegt omhoog en vertraagt, voordat hij stopt. Hoe verhoudt de kabelkracht zich tot de zwaartekracht op de lift?",
    "De kabelkracht is kleiner dan de zwaartekracht", ["De kabelkracht is groter dan de zwaartekracht", "De kabelkracht is even groot als de zwaartekracht", "De kabelkracht is 0 N tijdens het vertragen"], 2,
    "De lift beweegt omhoog en vertraagt: Fres wijst omlaag, dus Fkabel (omhoog) is kleiner dan Fz (omlaag)."),
 mc("In een (v,t)-diagram ligt de grafiek van een voorwerp gedurende 10 s precies op de tijdas (v = 0 m/s). Wat betekent dit?",
    "Het voorwerp staat stil en Fres is 0 N", ["De snelheid is constant en niet nul; Fres wijst vooruit", "Het voorwerp vertraagt en Fres wijst achteruit", "Het voorwerp keert om en Fres wijst achteruit"], 1,
    "v = 0 m/s betekent stilstand; de snelheid verandert niet, dus Fres = 0 N."),
 mc("Een fietser rijdt met constante snelheid tegen de wind in. Plotseling valt de wind weg, terwijl de trapkracht gelijk blijft. Wat gebeurt er?",
    "De fietser versnelt doordat Ftegen kleiner wordt", ["De fietser vertraagt omdat de wind wegvalt", "De snelheid blijft gelijk omdat de trapkracht gelijk blijft", "De fietser komt direct tot stilstand zonder wind"], 3,
    "Zonder tegenwind is de luchtweerstand kleiner: Fvoor > Ftegen, dus Fres wijst vooruit en de snelheid neemt toe."),
 ww("Bij een eenparig vertraagde beweging wijst de resulterende kracht tegen de bewegingsrichting in.", True,
    "de snelheid neemt af, dus Fres is tegen de bewegingsrichting in gericht."),
 ww("Als de motorkracht van een auto twee keer zo groot wordt, wordt de resulterende kracht altijd precies twee keer zo groot.", False,
    "Fres = Fmotor − Ftegen; de tegenwerkende kracht verandert niet mee, dus Fres wordt niet precies verdubbeld."),
 ww("Op een voorwerp kunnen meer dan twee krachten werken terwijl de resulterende kracht toch 0 N is.", True,
    "de som van alle krachten telt: bijvoorbeeld 30 N + 20 N naar rechts en 50 N naar links geeft Fres = 0 N."),
 ww("Bij een eenparig versnelde beweging wordt de resulterende kracht steeds groter.", False,
    "bij een eenparig versnelde beweging neemt de snelheid elke seconde even veel toe en is Fres constant."),
 inv("Een trekker trekt een aanhanger met een kracht van 9,6 kN naar voren. De rolweerstand is 2,1 kN en de luchtweerstand is 1,4 kN. Bereken Fres in N.",
     6100, "N", "Ftegen = 2100 + 1400 = 3500 N. Fres = 9600 − 3500 = 6100 N.", alt=["6,1 kN", "6,1"]),
 inv("Een rugzak heeft een massa van 850 g. Bereken de zwaartekracht in N (g = 9,81 N/kg).",
     8.3, "N", "m = 0,850 kg. Fz = 0,850 · 9,81 = 8,34 N, afgerond 8,3 N.", alt=["8,34", "8.34", "8,34 N"]),
 inv("Een scooter versnelt eenparig van 0 naar 14 m/s in 8 s. Na hoeveel seconden heeft hij een snelheid van 10,5 m/s?",
     6, "s", "Per seconde neemt v toe met 14/8 = 1,75 m/s. 10,5 / 1,75 = 6 s."),
 inv("Een auto rijdt met constante snelheid; de motorkracht is 1850 N. De luchtweerstand is vier keer zo groot als de rolweerstand. Hoeveel N bedraagt de rolweerstand?",
     370, "N", "Bij constante snelheid is Ftegen = 1850 N = 4x + x = 5x, dus de rolweerstand x = 370 N."),
 op("Een fietser trapt vanuit stilstand met een constante kracht van 100 N. In het (v,t)-diagram is de grafiek eerst steil en wordt daarna steeds vlakker. Verklaar dit met de krachten op de fietser.",
    "De trapkracht blijft gelijk, maar de luchtweerstand wordt groter naarmate de snelheid toeneemt. Daardoor wordt de resulterende kracht steeds kleiner en neemt de snelheid steeds langzamer toe, dus de lijn wordt vlakker.",
    ["luchtweerstand/weerstand/tegenwerkende kracht", "resulterende kracht/Fres"],
    "Ftegen neemt toe met de snelheid, dus Fres = Fvoor − Ftegen neemt af en de snelheidstoename per seconde wordt kleiner."),
]
write(68, "G", G)
