# Genereert natuurkunde examen_72/73/74 (§1.3 Kracht en versnelling, toets E/F/G)
import json

def mc(v, c, w, pos, u):
    o = list(w); o.insert(pos, c)
    return {"type": "mc", "vraag": v, "opties": o, "antwoord": pos, "uitleg": u}

def ww(v, a, u):
    return {"type": "waaronwaar", "vraag": v, "antwoord": a, "uitleg": ("Waar: " if a else "Onwaar: ") + u}

def num(x, unit, dec):
    s = f"{x:.{dec}f}"
    forms = {s, s.replace(".", ",")}
    t = f"{x:g}"; forms |= {t, t.replace(".", ",")}
    return "|".join(sorted(forms) + [f + " " + unit for f in sorted(forms)])

def inv(v, x, unit, dec, u):
    return {"type": "invul", "vraag": v, "antwoord": num(x, unit, dec), "uitleg": u}

def op(v, m, k, u):
    return {"type": "open", "vraag": v, "modelantwoord": m, "minTreffers": 1, "sleutelwoorden": k, "uitleg": u}

def close(a, b): assert abs(a - b) < 1e-9, (a, b)

# ---- rekencontrole ----
close(4.0*3.0, 12); close(50/20, 2.5); close(5.0*9.8, 49); close(15/5, 3.0); close((500-150)/50, 7.0); close(4000/1000, 4.0)
close(16*0+ (24/ (16)) *0 + 24, 24)  # placeholder (zie invul E1: a=(150-30)/48)
close((150-30)/48, 2.5); close(90/15, 6.0); close((85-25)/75, 0.8); close(20/40*10, 5.0)
close(90-60, 30); close(34/0.17, 200); close(9.0/0.45, 20); close(900*1.5+400, 1750); close(12/4*50, 150)
close((0.40*9.8-1.2)/0.40, 6.8); close(120/80, 1.5); close(6/1.5, 4.0); close(48/6, 8); close(3*1.0, 3)
close((150-30)/60, 2.0); close(6000/1500, 4.0); close(7.5*9.8, 73.5); close((100-20)/40*5, 10.0)
close(800*2.5+350, 2350); close(20/ (180/90)/2*8*0+ 8*8/(2*2.0), 16); close(500*2.0, 1000)
close(80*9.8-80*2.0, 624); close(1500*(10-4)/3, 3000); close(0.16*30/0.02, 240); close((1100-700)/1000, 0.4)
close(60000/120000, 0.5); close((54000-6000)/240000*20, 4.0); close(15/(4500/900), 3.0)
close(((180-55)/25)*4/2*4, 40); close((12/6*220+70), 510)

E = [
 mc("Wat wordt in de natuurkunde bedoeld met de <b>resulterende kracht</b> op een voorwerp?",
    "De som van alle krachten op het voorwerp, rekening houdend met hun richting",
    ["De grootste van alle krachten die op het voorwerp werken, los van de richting",
     "Alleen de kracht die de motor of de spieren in de bewegingsrichting leveren",
     "De kracht die het voorwerp zelf uitoefent op de grond of de lucht eromheen"], 2,
    "De resulterende kracht is de vectoriële som van alle krachten. Pas daarmee volgt de versnelling uit F<sub>res</sub> = m · a."),
 mc("Een slee glijdt naar rechts over het ijs en wordt langzamer. In welke richting wijst de resulterende kracht?",
    "Naar links, tegen de bewegingsrichting in",
    ["Naar rechts, in de bewegingsrichting",
     "Naar boven, loodrecht op het ijs",
     "Er is geen resulterende kracht, want de slee beweegt"], 0,
    "Een vertraging betekent dat de snelheid afneemt. Dat kan alleen als de resulterende kracht tegen de bewegingsrichting in wijst."),
 mc("Een kar met een massa van 4,0 kg versnelt met 3,0 m/s². Hoe groot is de resulterende kracht die daarvoor nodig is?",
    "12 N", ["7 N", "1,3 N", "0,75 N"], 3,
    "F<sub>res</sub> = m · a = 4,0 × 3,0 = 12 N. Optellen van m en a (7) of delen (1,3) is een veelgemaakte fout."),
 mc("Een doos van 20 kg wordt voortgeduwd met een resulterende kracht van 50 N. Wat is de versnelling van de doos?",
    "2,5 m/s²", ["1000 m/s²", "0,4 m/s²", "30 m/s²"], 1,
    "a = F<sub>res</sub> / m = 50 / 20 = 2,5 m/s². Vermenigvuldigen geeft 1000, en F en m omdraaien geeft 0,4."),
 mc("Hoe groot is de zwaartekracht op een pakket van 5,0 kg? Neem g = 9,8 N/kg.",
    "49 N", ["0,51 N", "14,8 N", "4,9 N"], 3,
    "F<sub>z</sub> = m · g = 5,0 × 9,8 = 49 N."),
 mc("Een scooter trekt op van 0 m/s naar 15 m/s in 5,0 s. Wat is de gemiddelde versnelling?",
    "3,0 m/s²", ["75 m/s²", "0,33 m/s²", "20 m/s²"], 0,
    "a = Δv / t = 15 / 5,0 = 3,0 m/s². Delen door de tijd, niet vermenigvuldigen."),
 mc("Een fietser en zijn fiets hebben samen een massa van 50 kg. Hij trapt met een voorwaartse kracht van 500 N terwijl de tegenwerkende krachten samen 150 N zijn. Wat is zijn versnelling?",
    "7,0 m/s²", ["13 m/s²", "10 m/s²", "0,14 m/s²"], 2,
    "F<sub>res</sub> = 500 − 150 = 350 N, dus a = 350 / 50 = 7,0 m/s². Wie de weerstand vergeet krijgt 10, wie optelt krijgt 13."),
 mc("Een auto van 1000 kg remt met een resulterende remkracht van 4000 N. Hoe groot is de vertraging?",
    "4,0 m/s²", ["4000 m/s²", "0,25 m/s²", "40 m/s²"], 3,
    "a = F / m = 4000 / 1000 = 4,0 m/s². De vertraging is even groot als een versnelling, maar met de richting tegen de beweging in."),
 mc("Welke formule is een juiste omwerking van F<sub>res</sub> = m · a om de <b>massa</b> te berekenen?",
    "m = F<sub>res</sub> / a", ["m = F<sub>res</sub> · a", "m = a / F<sub>res</sub>", "m = F<sub>res</sub> − a"], 1,
    "Deel beide kanten van F<sub>res</sub> = m · a door a, dan staat er m = F<sub>res</sub> / a."),
 mc("Een voorwerp versnelt vanuit stilstand door een constante resulterende kracht. Welke vorm heeft het (v,t)-diagram?",
    "Een rechte, schuin oplopende lijn die in de oorsprong begint",
    ["Een horizontale lijn op de hoogte van de eindsnelheid", "Een kromme lijn die steeds steiler omhoog gaat", "Een rechte lijn die schuin naar beneden loopt"], 2,
    "Bij constante F<sub>res</sub> en massa is a constant. Dan groeit v elke seconde evenveel: een rechte schuine lijn vanuit (0,0)."),
 mc("Een ruimtesonde in de lege ruimte (praktisch geen wrijving) schakelt zijn motor aan met een constante kracht. Wat gebeurt er met de snelheid?",
    "Die neemt steeds verder toe",
    ["Die wordt na korte tijd constant", "Die neemt eerst toe en daarna weer af", "Die blijft nul, want er is geen lucht"], 0,
    "Zonder tegenwerkende kracht is F<sub>res</sub> gelijk aan de motorkracht. Er is dus een constante versnelling en de snelheid groeit door."),
 ww("Als de resulterende kracht op een voorwerp 0 N is, verandert de snelheid van het voorwerp niet.", True,
    "Bij F<sub>res</sub> = 0 N is a = 0 m/s². De snelheid blijft constant (ook als die niet nul is)."),
 ww("Bij dezelfde resulterende kracht krijgt een voorwerp van 10 kg een grotere versnelling dan een voorwerp van 5 kg.", False,
    "Het zwaardere voorwerp krijgt juist de kleinste versnelling, want a = F / m."),
 ww("Een resulterende kracht die schuin op de bewegingsrichting staat, kan de bewegingsrichting van een voorwerp veranderen.", True,
    "Een kracht die niet precies in of tegen de bewegingsrichting werkt, geeft een richtingsverandering (en ook een versnelling of vertraging)."),
 ww("Een kar van 5,0 kg die door 20 N wordt voortgeduwd (zonder wrijving) versnelt met 100 m/s².", False,
    "a = F / m = 20 / 5,0 = 4,0 m/s². Vermenigvuldigen in plaats van delen geeft de foute waarde 100."),
 inv("Een kar van 16 kg wordt voortgeduwd met 150 N. De wrijvingskracht is 30 N. Hoe groot is de versnelling van de kar (in m/s²)?" if False else
     "Een winkelkar van 48 kg krijgt een duwkracht van 150 N en ondervindt 30 N wrijving. Hoe groot is de versnelling in m/s²?",
     2.5, "m/s²", 1, "F<sub>res</sub> = 150 − 30 = 120 N, dus a = 120 / 48 = 2,5 m/s²."),
 inv("Een slee van 15 kg wordt zonder wrijving voortgeduwd met 90 N. Hoe groot is de versnelling in m/s²?",
     6.0, "m/s²", 1, "a = F<sub>res</sub> / m = 90 / 15 = 6,0 m/s²."),
 inv("Een fietser met fiets (75 kg) trapt met 85 N vooruit. De tegenwerkende krachten zijn samen 25 N. Wat is zijn versnelling in m/s²?",
     0.8, "m/s²", 1, "F<sub>res</sub> = 85 − 25 = 60 N, dus a = 60 / 75 = 0,8 m/s²."),
 inv("Een trolley van 40 kg staat stil en krijgt een resulterende kracht van 20 N gedurende 10 s. Welke snelheid heeft hij daarna in m/s?",
     5.0, "m/s", 1, "a = 20 / 40 = 0,5 m/s². Na 10 s geldt v = a · t = 0,5 × 10 = 5,0 m/s."),
 op("Een auto rijdt met een constante snelheid van 90 km/h over een rechte weg terwijl de motor wel een kracht levert. Leg uit hoe dat mogelijk is.",
    "De motorkracht (voorwaarts) is even groot als de tegenwerkende krachten (wrijving en luchtweerstand). De resulterende kracht is daardoor 0 N, dus de versnelling is 0 m/s² en de snelheid blijft constant.",
    ["resulterende kracht/nettokracht", "weerstand/wrijving/tegenwerkende"],
    "De motorkracht houdt de tegenwerkende krachten in evenwicht: F<sub>res</sub> = 0 N, dus a = 0 en de snelheid verandert niet."),
]

F = [
 mc("Een fietser trapt met 90 N vooruit. De tegenwind werkt met 60 N tegen. Wat is de resulterende kracht?",
    "30 N, in de rijrichting", ["150 N, in de rijrichting", "30 N, tegen de rijrichting in", "60 N, in de rijrichting"], 1,
    "De krachten werken tegen elkaar in: 90 − 60 = 30 N. De grootste kracht wint, dus Fres wijst in de rijrichting."),
 mc("Een ijshockeypuck van 0,17 kg krijgt een slag met een kracht van 34 N. Hoe groot is zijn versnelling?",
    "200 m/s²", ["5,8 m/s²", "0,0050 m/s²", "34 m/s²"], 3,
    "a = F / m = 34 / 0,17 = 200 m/s²."),
 mc("Een bal van 450 g wordt weggeschopt met een resulterende kracht van 9,0 N. Wat is de versnelling?",
    "20 m/s²", ["0,020 m/s²", "4050 m/s²", "2,0 m/s²"], 0,
    "Reken eerst de massa om: 450 g = 0,45 kg. Dan a = 9,0 / 0,45 = 20 m/s². Wie 450 invult krijgt 0,020."),
 mc("Een auto van 900 kg versnelt met 1,5 m/s². De totale tegenwerkende kracht is 400 N. Hoe groot is de motorkracht?",
    "1750 N", ["950 N", "1350 N", "400 N"], 2,
    "F<sub>res</sub> = m · a = 900 × 1,5 = 1350 N. De motor moet ook de weerstand overwinnen: 1350 + 400 = 1750 N."),
 mc("Een kar van 50 kg trekt op. In het (v,t)-diagram loopt de lijn recht van 0 m/s naar 12 m/s in 4,0 s. Hoe groot is de resulterende kracht?",
    "150 N", ["600 N", "48 N", "16,7 N"], 3,
    "a = 12 / 4,0 = 3,0 m/s². Dan F<sub>res</sub> = m · a = 50 × 3,0 = 150 N."),
 mc("Een kist beweegt naar rechts en wordt langzamer. Welke richting heeft de resulterende kracht?",
    "Naar links, tegen de bewegingsrichting in", ["Naar rechts, in de bewegingsrichting", "Omhoog, loodrecht op de beweging", "De resulterende kracht is 0 N"], 0,
    "Een vertraging komt van een resulterende kracht tegen de bewegingsrichting in."),
 mc("Een steen van 0,40 kg valt van een brug. De gemiddelde luchtweerstand is 1,2 N en g = 9,8 N/kg. Wat is de gemiddelde versnelling?",
    "6,8 m/s²", ["9,8 m/s²", "3,0 m/s²", "2,7 m/s²"], 1,
    "F<sub>z</sub> = 0,40 × 9,8 = 3,92 N. F<sub>res</sub> = 3,92 − 1,2 = 2,72 N. a = 2,72 / 0,40 = 6,8 m/s²."),
 mc("Een fietser met fiets (80 kg) rijdt 6,0 m/s en remt met een constante resulterende kracht van 120 N. Na hoeveel seconden staat hij stil?",
    "4,0 s", ["0,25 s", "9,0 s", "1,5 s"], 2,
    "a = 120 / 80 = 1,5 m/s². Remtijd t = Δv / a = 6,0 / 1,5 = 4,0 s."),
 mc("Een winkelwagen krijgt van een resulterende kracht van 48 N een versnelling van 6,0 m/s². Wat is zijn massa?",
    "8,0 kg", ["288 kg", "0,125 kg", "42 kg"], 3,
    "m = F<sub>res</sub> / a = 48 / 6,0 = 8,0 kg."),
 mc("Je zet bij een voorwerp van vaste massa de resulterende kracht F uit tegen de versnelling a. Wat is de vorm van de grafiek?",
    "Een rechte lijn door de oorsprong, want F en a zijn evenredig",
    ["Een horizontale lijn, want F verandert niet met a", "Een dalende lijn, want F en a zijn omgekeerd evenredig", "Een kromme lijn die steeds steiler wordt"], 0,
    "F = m · a met vaste m is een rechte lijn door de oorsprong, met de massa als helling."),
 mc("Twee karren, A (2,0 kg) en B (6,0 kg), krijgen allebei een versnelling van 1,5 m/s². Wat is de verhouding F<sub>B</sub> : F<sub>A</sub> van de resulterende krachten?",
    "3 : 1", ["1 : 3", "1 : 1", "9 : 1"], 1,
    "Bij gelijke a is F evenredig met m. B heeft 3 keer zoveel massa, dus 3 keer zoveel kracht nodig."),
 ww("Een voorwerp met een grote massa kan toch een grote versnelling krijgen als de resulterende kracht groot genoeg is.", True,
    "a = F / m: een grote massa wordt gecompenseerd door een nog grotere kracht."),
 ww("Als een auto versnelt, is de motorkracht gelijk aan de som van de tegenwerkende krachten.", False,
    "Gelijk betekent F<sub>res</sub> = 0 N en dus geen versnelling. Bij versnellen is de motorkracht groter dan de tegenwerkende krachten."),
 ww("Bij een vertraging wijst de resulterende kracht tegen de bewegingsrichting in.", True,
    "Alleen een resulterende kracht tegen de beweging in kan de snelheid kleiner maken."),
 ww("Een kracht van 1 N geeft een voorwerp van 1 kg een versnelling van 9,8 m/s².", False,
    "1 N geeft 1 kg een versnelling van 1 m/s². De 9,8 hoort bij de zwaartekracht (g in N/kg)."),
 inv("Een bakfiets met lading (60 kg) wordt vooruit geduwd met 150 N tegen 30 N wrijving. Wat is de versnelling in m/s²?",
     2.0, "m/s²", 1, "F<sub>res</sub> = 150 − 30 = 120 N, dus a = 120 / 60 = 2,0 m/s²."),
 inv("Een auto van 1500 kg remt met een resulterende remkracht van 6000 N. Hoe groot is de vertraging in m/s²?",
     4.0, "m/s²", 1, "a = 6000 / 1500 = 4,0 m/s²."),
 inv("Een blok van 7,5 kg ligt op een tafel. Hoe groot is de zwaartekracht erop in N? Neem g = 9,8 N/kg.",
     73.5, "N", 1, "F<sub>z</sub> = m · g = 7,5 × 9,8 = 73,5 N."),
 inv("Een slee van 40 kg staat stil. Hij wordt getrokken met 100 N, de wrijving is 20 N. Welke snelheid heeft de slee na 5,0 s in m/s?",
     10.0, "m/s", 0, "F<sub>res</sub> = 80 N, a = 80 / 40 = 2,0 m/s². Dan v = a · t = 2,0 × 5,0 = 10 m/s."),
 op("Je schopt een bal over een vlakke grasmat. De snelheid van de bal wordt steeds kleiner totdat hij stilligt. Leg uit welke kracht daarvoor zorgt.",
    "Er werkt een tegenwerkende wrijvingskracht (rolweerstand en luchtweerstand) op de bal, tegen de bewegingsrichting in. Daardoor is de resulterende kracht tegen de beweging in en krijgt de bal een vertraging, totdat hij stilstaat.",
    ["wrijving/rolweerstand/weerstand", "vertraging/afremmen"],
    "Zonder tegenwerkende wrijving zou de bal met constante snelheid doorrollen. De wrijving geeft een Fres tegen de beweging in en dus een vertraging."),
]

G = [
 mc("Een auto van 800 kg trekt op van 0 naar 72 km/h in 8,0 s. De tegenwerkende krachten zijn samen 350 N. Hoe groot is de motorkracht?",
    "2350 N", ["1650 N", "2000 N", "5760 N"], 3,
    "72 km/h = 20 m/s, a = 20 / 8,0 = 2,5 m/s². F<sub>res</sub> = 800 × 2,5 = 2000 N en daarbovenop 350 N weerstand: 2350 N."),
 mc("Een fietser met fiets (90 kg) rijdt met 8,0 m/s en remt met een constante resulterende kracht van 180 N. Hoe lang is zijn remweg?",
    "16 m", ["32 m", "4,0 m", "8,0 m"], 1,
    "a = 180 / 90 = 2,0 m/s², remtijd = 8,0 / 2,0 = 4,0 s. Gemiddelde snelheid 4,0 m/s, dus remweg = 4,0 × 4,0 = 16 m."),
 mc("Een auto (1000 kg) trekt een aanhanger (500 kg) op een gladde weg zonder wrijving. Samen versnellen ze met 2,0 m/s². Hoe groot is de kracht van de koppeling op de aanhanger?",
    "1000 N", ["3000 N", "2000 N", "1500 N"], 2,
    "Voor de aanhanger alleen geldt F = m · a = 500 × 2,0 = 1000 N. Die kracht komt via de koppeling van de auto."),
 mc("Een parachutist van 80 kg valt met een versnelling van 2,0 m/s² naar beneden. Neem g = 9,8 N/kg. Hoe groot is de luchtweerstand?",
    "624 N", ["784 N", "944 N", "160 N"], 0,
    "F<sub>z</sub> = 80 × 9,8 = 784 N. F<sub>res</sub> = 80 × 2,0 = 160 N. De luchtweerstand is F<sub>z</sub> − F<sub>res</sub> = 624 N."),
 mc("Een auto van 1500 kg remt zo dat in het (v,t)-diagram de lijn rechtdoor loopt van 10 m/s naar 4,0 m/s in 3,0 s. Wat is de resulterende kracht?",
    "3000 N, tegen de bewegingsrichting in",
    ["3000 N, in de bewegingsrichting", "9000 N, tegen de bewegingsrichting in", "4500 N, tegen de bewegingsrichting in"], 3,
    "a = (4,0 − 10) / 3,0 = −2,0 m/s². F<sub>res</sub> = 1500 × 2,0 = 3000 N, en door de vertraging wijst die tegen de beweging in."),
 mc("De resulterende kracht op een voorwerp wordt 3 keer zo groot en de massa wordt 2 keer zo groot. Wat gebeurt er met de versnelling?",
    "Die wordt 1,5 keer zo groot", ["Die wordt 6 keer zo groot", "Die wordt 3 keer zo groot", "Die blijft gelijk"], 2,
    "a = F / m. De factor wordt 3 / 2 = 1,5."),
 mc("Een honkbal van 0,16 kg vliegt met 30 m/s in de handschoen en staat na 0,020 s stil. Wat is de gemiddelde kracht op de bal?",
    "240 N", ["4,8 N", "2400 N", "9375 N"], 1,
    "a = 30 / 0,020 = 1500 m/s². F = m · a = 0,16 × 1500 = 240 N."),
 mc("Een auto van 1000 kg rijdt met constante snelheid; de motorkracht is 700 N. De motorkracht wordt 1100 N, de weerstand blijft gelijk. Wat is nu de versnelling?",
    "0,40 m/s²", ["1,1 m/s²", "0,70 m/s²", "1,8 m/s²"], 0,
    "Eerst was F<sub>res</sub> = 0, dus de weerstand is 700 N. Nu is F<sub>res</sub> = 1100 − 700 = 400 N en a = 400 / 1000 = 0,40 m/s²."),
 mc("Waarom kan een fietser bij hoge snelheid minder hard versnellen, ook als hij even hard blijft trappen?",
    "De luchtweerstand is groter, dus de resulterende kracht is kleiner",
    ["De massa van de fietser neemt toe bij hogere snelheid", "De zwaartekracht op de fietser neemt af bij hogere snelheid", "De trapkracht werkt dan alleen loodrecht op de beweging"], 3,
    "De luchtweerstand neemt toe met de snelheid. Bij gelijke trapkracht wordt F<sub>res</sub> = F<sub>trap</sub> − F<sub>w</sub> kleiner, dus ook a."),
 mc("Een trein van 120 ton krijgt een motorkracht van 60 kN. De weerstand is te verwaarlozen. Wat is de versnelling?",
    "0,50 m/s²", ["2,0 m/s²", "5,0 m/s²", "500 m/s²"], 1,
    "120 ton = 120 000 kg en 60 kN = 60 000 N. Dan a = 60 000 / 120 000 = 0,50 m/s²."),
 mc("Een auto remt met een constante remkracht tot stilstand. De beginsnelheid is twee keer zo groot, de massa en remkracht blijven gelijk. Wat gebeurt er met de remtijd?",
    "Die wordt 2 keer zo lang", ["Die wordt 4 keer zo lang", "Die blijft gelijk", "Die wordt 2 keer zo kort"], 0,
    "De vertraging a blijft gelijk. Remtijd t = Δv / a is dus evenredig met de beginsnelheid."),
 ww("Voor dezelfde versnelling heeft een voorwerp van 90 kg een drie keer zo grote resulterende kracht nodig als een voorwerp van 30 kg.", True,
    "F = m · a: bij gelijke a is F evenredig met m, en 90 kg is 3 keer 30 kg."),
 ww("Bij het optrekken is de resulterende kracht gelijk aan de motorkracht plus de tegenwerkende krachten.", False,
    "De tegenwerkende krachten werken tegen de motorkracht in, dus je trekt ze af: F<sub>res</sub> = F<sub>motor</sub> − F<sub>weerstand</sub>."),
 ww("Bij een constante kracht in de bewegingsrichting groeit de snelheid elke seconde met dezelfde waarde.", True,
    "Constante F<sub>res</sub> en massa geven een constante versnelling, dus een gelijke snelheidstoename per seconde."),
 ww("Als de remkracht van een auto twee keer zo groot wordt, wordt de remtijd vanaf dezelfde snelheid ook twee keer zo groot.", False,
    "Een dubbele kracht geeft een dubbele vertraging en dus een halve remtijd."),
 inv("Een trein van 240 000 kg heeft een motorkracht van 54 kN. De weerstand is 6,0 kN. Welke snelheid heeft de trein na 20 s vanuit stilstand in m/s?",
     4.0, "m/s", 1, "F<sub>res</sub> = 54 000 − 6000 = 48 000 N. a = 48 000 / 240 000 = 0,20 m/s². v = 0,20 × 20 = 4,0 m/s."),
 inv("Een auto van 900 kg rijdt met 54 km/h en remt met een constante remkracht van 4500 N. Na hoeveel seconden staat de auto stil?",
     3.0, "s", 1, "54 km/h = 15 m/s. a = 4500 / 900 = 5,0 m/s². t = 15 / 5,0 = 3,0 s."),
 inv("Een kist van 25 kg staat stil en wordt voortgetrokken met 180 N. De wrijving is 55 N. Welke afstand legt de kist af in 4,0 s? Antwoord in m.",
     40.0, "m", 0, "a = (180 − 55) / 25 = 5,0 m/s². Na 4,0 s is v = 20 m/s, de gemiddelde snelheid is 10 m/s, dus s = 10 × 4,0 = 40 m."),
 inv("Een bobslee van 220 kg bereikt vanuit stilstand 12 m/s in 6,0 s. De wrijving is 70 N. Hoe groot is de voorwaartse kracht in N?",
     510.0, "N", 0, "a = 12 / 6,0 = 2,0 m/s². F<sub>res</sub> = 220 × 2,0 = 440 N. Voorwaartse kracht = 440 + 70 = 510 N."),
 op("Een bal wordt recht omhoog gegooid. Leg uit waarom de snelheid van de bal afneemt terwijl hij nog steeds omhoog beweegt.",
    "Op de bal werkt de zwaartekracht naar beneden. Die kracht wijst tegen de bewegingsrichting in, dus de resulterende kracht is naar beneden en de bal krijgt een vertraging. Daardoor neemt de snelheid af, ook al beweegt de bal nog omhoog.",
    ["zwaartekracht/gravitatie", "vertraging/negatieve versnelling/afremmen"],
    "Snelheid en kracht kunnen tegengesteld gericht zijn. De zwaartekracht geeft een vertraging omhoog, tot de snelheid 0 is en de bal weer valt."),
]

def herpos(vr, doel):
    ms = [q for q in vr if q["type"] == "mc"]
    for q, t in zip(ms, doel):
        c = q["opties"].pop(q["antwoord"]); q["opties"].insert(t, c); q["antwoord"] = t

def schrijf(nr, lab, vr, icoon):
    assert [len(vr)] == [20] and sum(q["type"]=="mc" for q in vr)==11
    ww_ = [q for q in vr if q["type"]=="waaronwaar"]; assert len(ww_)==4 and sum(q["antwoord"] for q in ww_)==2
    d = {"id": f"ex-h3-natuurkunde-{nr}", "hoofdstuk": 1, "paragraaf": "1.3",
         "titel": f"Toets {nr} — §1.3 Kracht en versnelling — Toets {lab}",
         "vak": "Natuurkunde · HAVO 3 (H1)", "icoon": icoon, "duurMin": 30, "vragen": vr}
    kop = (f"/* =========================================================\n   Duru's Natuurkunde (HAVO 3) — {d['titel']}\n"
           "   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)\n"
           "   ========================================================= */\n")
    open(f"havo3/natuurkunde/js/data/examen_{nr}.js", "w", encoding="utf-8").write(
        kop + "DURU.registerExamen(" + json.dumps(d, ensure_ascii=False, indent=2) + ");\n")
    print(nr, [q["antwoord"] for q in vr if q["type"]=="mc"])

herpos(F, [1,3,0,0,2,3,1,2,0,3,1])
schrijf(72, "E", E, "⚡"); schrijf(73, "F", F, "🚀"); schrijf(74, "G", G, "🏎️")
