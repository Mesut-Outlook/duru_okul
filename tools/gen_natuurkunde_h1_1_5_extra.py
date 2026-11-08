#!/usr/bin/env python3
"""Genereert natuurkunde ex-h3-natuurkunde-78/79/80 (§1.5 Arbeid, Toets C/D/E)."""
import json, os

def mc(vraag, juist, fout, pos, uitleg):
    o = list(fout); o.insert(pos, juist)
    return {"type": "mc", "vraag": vraag, "opties": o, "antwoord": pos, "uitleg": uitleg}
def ww(vraag, waar, uitleg):
    return {"type": "waaronwaar", "vraag": vraag, "antwoord": waar, "uitleg": uitleg}
def inv(vraag, antw, uitleg):
    return {"type": "invul", "vraag": vraag, "antwoord": antw, "uitleg": uitleg}
def op(vraag, model, keys, uitleg):
    return {"type": "open", "vraag": vraag, "modelantwoord": model, "minTreffers": 1, "sleutelwoorden": keys, "uitleg": uitleg}

# ---- reken-controles ----
assert 70*6.0 == 420 and 250*40 == 10000
assert 150*12 == 1800 and 2000/(250*0.40) == 20 and 8.0*25 == 200 and 20*10*3.0 == 600
assert 75*1 == 75 and 480000/600/4 == 200 and (50-20)*10 == 300 and 2.5e6 == 2500000
assert 40*10*2.5 == 1000
assert 54000/300/6 == 30 and 45*2000/1000 == 90 and 500*10*12/1000 == 60 and 3200*15/1000 == 48
assert (90-30)*40 == 2400 and 2000*3000 == 6_000_000 and abs(25*9.81*4/1000-0.98) < 0.005
assert 80*10*1500/1000 == 1200 and 900/150 == 6.0 and (150*0.80)/40 == 3.0
assert 600*0.0040 == 2.4 and (200+150-100)*15 == 3750 and 12e6/600 == 20000
assert 350*10*(1.2+0.80) == 7000 and (175*2-280)*80 == 5600 and 90*10*120/1000 == 108 and 3*35*90 == 9450
assert 5000*20 == 100000

C = [
 mc("Wat betekent <b>arbeid</b> in de natuurkunde?",
    "De hoeveelheid energie die een kracht aan een voorwerp overdraagt",
    ["De hoeveelheid kracht die een voorwerp nodig heeft om te blijven bewegen",
     "De mate van inspanning die je lichaam voelt tijdens het duwen",
     "De tijd die een voorwerp nodig heeft om een afstand af te leggen"], 2,
    "Arbeid is overgedragen energie. Het begrip is in de natuurkunde veel beperkter dan in het dagelijks taalgebruik."),
 mc("Een leerling duwt een kar met 70 N over 6,0 m, in de richting van de kracht. Hoeveel arbeid verricht zij?",
    "420 J", ["76 J", "12 J", "42 J"], 0, "W = F × s = 70 N × 6,0 m = 420 J."),
 mc("In welke situatie verricht jouw spierkracht <b>geen</b> arbeid?",
    "Je duwt uit alle macht tegen een muur die niet beweegt",
    ["Je trekt een slee een stuk voort over de sneeuw",
     "Je schopt een stilstaande bal ver het veld in",
     "Je duwt een stilstaande fiets op gang"], 3,
    "Arbeid vraagt een verplaatsing in de richting van de kracht. De muur beweegt niet (s = 0 m), dus W = 0 J."),
 mc("Welke eenheid is gelijk aan 1 joule?",
    "1 newtonmeter (N·m)", ["1 newton per meter (N/m)", "1 kilogram keer meter (kg·m)", "1 newton keer seconde (N·s)"], 1,
    "Uit W = F × s volgt dat de eenheid van arbeid N × m = J is."),
 mc("Een hondenslee beweegt met constante snelheid. De honden trekken met 120 N. Hoe groot is de schuifwrijvingskracht?",
    "120 N, tegengesteld aan de beweging",
    ["0 N, want de snelheid is constant", "Kleiner dan 120 N, anders zou de slee stilstaan",
     "Groter dan 120 N, anders zou de slee versnellen"], 1,
    "Bij constante snelheid is de resulterende kracht 0 N. De wrijvingskracht is dus even groot als de trekkracht, maar tegengesteld gericht."),
 mc("Een curlingsteen glijdt na de afzet uit over het ijs. Welke kracht verricht hierbij negatieve arbeid?",
    "De schuifwrijvingskracht van het ijs", ["De zwaartekracht op de steen", "De spierkracht van de speler", "De kracht die de steen op het ijs uitoefent"], 3,
    "De schuifwrijvingskracht werkt tegen de verplaatsing in en zet bewegingsenergie om in warmte."),
 mc("Een kogelstoter stoot een kogel weg. Welke energieomzetting vindt plaats?",
    "Chemische energie wordt omgezet in bewegingsenergie (en warmte)",
    ["Bewegingsenergie wordt omgezet in chemische energie", "Warmte wordt volledig omgezet in bewegingsenergie",
     "Elektrische energie wordt omgezet in bewegingsenergie"], 0,
    "De spierkracht verricht arbeid. Daarbij wordt chemische energie (uit voedsel) overgedragen als bewegingsenergie."),
 mc("Wanneer verricht een kracht <b>negatieve</b> arbeid?",
    "Als de kracht tegen de verplaatsing in werkt",
    ["Als de kracht kleiner is dan de zwaartekracht", "Als de kracht loodrecht op de verplaatsing staat", "Als de kracht op een stilstaand voorwerp werkt"], 2,
    "Een kracht tegen de verplaatsing in haalt bewegingsenergie weg. Dat is negatieve arbeid."),
 mc("Een kracht verplaatst een voorwerp over een afstand s. Wat gebeurt er met de arbeid als de afstand verdubbelt en de kracht gelijk blijft?",
    "De arbeid wordt twee keer zo groot", ["De arbeid blijft gelijk", "De arbeid wordt vier keer zo groot", "De arbeid wordt twee keer zo klein"], 3,
    "W = F × s: bij gelijke F is de arbeid recht evenredig met s."),
 mc("Een windsurfer beweegt met constante snelheid. De windkracht is 250 N. Hij legt 40 m af. Hoeveel arbeid verricht de weerstandskracht?",
    "-10000 J", ["+10000 J", "0 J", "-250 J"], 1,
    "Bij constante snelheid is de weerstandskracht 250 N, tegengesteld aan de verplaatsing: W = -250 N × 40 m = -10000 J."),
 mc("Op een bal die over een vlakke tafel rolt werkt de zwaartekracht wel, maar de arbeid ervan is 0 J. Wat is de reden?",
    "De zwaartekracht staat loodrecht op de verplaatsing",
    ["De zwaartekracht werkt niet op voorwerpen die bewegen", "De bal beweegt daarvoor te langzaam", "De zwaartekracht wordt opgeheven door de wrijving"], 2,
    "Alleen de kracht in de richting van de verplaatsing verricht arbeid. De zwaartekracht wijst omlaag, de beweging is horizontaal."),
 ww("Arbeid is overgedragen energie en wordt dus net als energie uitgedrukt in joule.", True,
    "Waar: arbeid is de hoeveelheid overgedragen energie, dus ook in joule."),
 ww("Een kogelstootster die een kogel stilhoudt, verricht natuurkundig arbeid zolang zij kracht blijft zetten.", False,
    "Onwaar: zonder verplaatsing is s = 0 m en dus W = 0 J, hoe moe de spieren ook worden."),
 ww("Bij constante snelheid is de arbeid van de weerstandskracht even groot als die van de voorwaartse kracht, maar negatief.", True,
    "Waar: de krachten zijn even groot en tegengesteld, de verplaatsing is gelijk. De arbeid heeft dus hetzelfde getal met tegengesteld teken."),
 ww("Als je dezelfde kracht over de halve afstand uitoefent, verricht je twee keer zoveel arbeid.", False,
    "Onwaar: W = F × s. Bij de halve afstand is de arbeid de helft."),
 inv("Een sleper trekt een kist met een kracht van 150 N over 12 m in de richting van de kracht. Bereken de verrichte arbeid in joule.",
     "1800|1800 J|1,8 kJ|1.8 kJ", "W = F × s = 150 N × 12 m = 1800 J."),
 inv("Derk tilt een gewicht steeds 0,40 m omhoog met 250 N. Hij wil in totaal 2000 J arbeid verrichten. Hoe vaak moet hij de oefening herhalen?",
     "20|20 keer|20x|20 maal", "Per keer: 250 N × 0,40 m = 100 J. Aantal keer = 2000 J / 100 J = 20."),
 inv("Een curlingsteen glijdt 25 m uit over het ijs tot stilstand. De schuifwrijvingskracht is 8,0 N. Hoeveel bewegingsenergie (in joule) had de steen aan het begin?",
     "200|200 J", "De negatieve arbeid van de wrijving haalt alle bewegingsenergie weg: 8,0 N × 25 m = 200 J."),
 inv("Een verhuizer tilt een doos van 20 kg met constante snelheid 3,0 m op (g = 10 N/kg). Hoeveel joule arbeid verricht zijn spierkracht?",
     "600|600 J", "Tilkracht = zwaartekracht = 20 × 10 = 200 N. W = 200 N × 3,0 m = 600 J."),
 op("Een curlingsteen glijdt over het ijs. Leg uit waarom spelers soms voor de steen uit vegen.",
    "Door te vegen wordt het ijs gladder en wordt de schuifwrijvingskracht kleiner. De wrijving verricht dan minder negatieve arbeid, dus verliest de steen minder bewegingsenergie en glijdt hij verder.",
    ["wrijving/wrijvingskracht/schuifwrijvingskracht", "verder/minder energie/minder bewegingsenergie"],
    "Vegen verkleint de wrijving; daardoor is er minder negatieve arbeid en glijdt de steen verder door."),
]

D = [
 mc("Een fietser rijdt met constante snelheid tegen een weerstandskracht van 75 N in. Hoeveel arbeid verricht hij per meter?",
    "75 J", ["0 J", "7,5 J", "750 J"], 1, "Bij constante snelheid is de voorwaartse kracht 75 N. Per meter: W = 75 N × 1,0 m = 75 J."),
 mc("Vier paarden trekken samen een kar over 600 m. Samen verrichten ze 480 kJ arbeid. Hoeveel kracht oefent elk paard uit?",
    "200 N", ["800 N", "3200 N", "120 N"], 3,
    "Totale kracht = W / s = 480000 J / 600 m = 800 N. Gedeeld over vier paarden: 200 N per paard."),
 mc("Acht paarden trekken een koets. De totale arbeid over een route blijft gelijk, maar er gaan paarden vanuit het gespan af. Wat gebeurt er met de kracht per paard?",
    "Die wordt groter, want dezelfde totale kracht wordt over minder paarden verdeeld",
    ["Die wordt kleiner, want elk paard heeft minder te dragen", "Die blijft gelijk, want de afstand verandert niet",
     "Die wordt kleiner, want de totale arbeid is nu minder"], 0,
    "Totale arbeid en afstand gelijk betekent dezelfde totale kracht. Die moet door minder paarden worden geleverd."),
 mc("Een windsurfer beweegt met constante snelheid. Wat gebeurt er met de arbeid van de windkracht?",
    "Die wordt via de wrijving omgezet in warmte",
    ["Die wordt omgezet in extra bewegingsenergie", "Die wordt opgeslagen in het zeil", "Die verdwijnt omdat de snelheid niet verandert"], 2,
    "De bewegingsenergie blijft gelijk. De weerstandskracht verricht even grote negatieve arbeid, waardoor de energie in warmte eindigt."),
 mc("Welke arbeid verricht de zwaartekracht op een opstijgende raket?",
    "Negatieve arbeid, want de kracht werkt tegen de beweging in",
    ["Positieve arbeid, want de raket beweegt", "Geen arbeid, want de raket verlaat de aarde", "Geen arbeid, want de zwaartekracht blijft constant"], 3,
    "De zwaartekracht wijst omlaag en de raket gaat omhoog: kracht tegen verplaatsing, dus negatieve arbeid."),
 mc("Je loopt vooruit met een boodschappentas omhooggehouden. Welke arbeid verricht de spierkracht waarmee je de tas draagt?",
    "Geen arbeid, want de kracht staat loodrecht op de verplaatsing",
    ["Positieve arbeid, want je spieren gebruiken energie", "Negatieve arbeid, want de tas is zwaar", "Positieve arbeid, want de tas verplaatst mee"], 1,
    "De draagkracht wijst omhoog, de verplaatsing is horizontaal. Dan is er geen arbeid van die kracht."),
 mc("Op een kar werkt 50 N voorwaarts en 20 N wrijving. De kar vertrekt uit stilstand en rijdt 10 m. Hoeveel bewegingsenergie heeft de kar dan?",
    "300 J", ["500 J", "200 J", "700 J"], 0,
    "Resulterende kracht = 50 N - 20 N = 30 N. De totale arbeid is 30 N × 10 m = 300 J, en dat wordt bewegingsenergie."),
 mc("Sophia stopt met trappen en rijdt uit tot stilstand. Wat geldt voor de negatieve arbeid van de weerstandskracht?",
    "Die is even groot als de bewegingsenergie waarmee ze begon",
    ["Die is altijd kleiner dan de bewegingsenergie die ze kwijtraakt", "Die is nul, want de snelheid daalt vanzelf", "Die is positief, want er ontstaat warmte"], 2,
    "Alle bewegingsenergie verdwijnt door de negatieve arbeid van de weerstandskracht en wordt warmte."),
 mc("Hoeveel joule is 2,5 MJ?",
    "2500000 J", ["250000 J", "2500 J", "25000000 J"], 1, "1 MJ = 1 000 000 J, dus 2,5 MJ = 2 500 000 J."),
 mc("Een kist van 40 kg wordt met constante snelheid 2,5 m omhoog getild (g = 10 N/kg). Welke arbeid verricht de zwaartekracht hierbij?",
    "-1000 J", ["+1000 J", "-400 J", "0 J"], 3,
    "Fz = 40 × 10 = 400 N, omlaag. De verplaatsing is omhoog, dus W = -400 N × 2,5 m = -1000 J."),
 mc("Je fietst met constante snelheid een berg op. Waarom moet je meer kracht zetten dan op vlak terrein?",
    "De zwaartekracht werkt ook tegen je beweging in",
    ["Je hebt bergop minder bewegingsenergie", "De snelheid neemt bergop vanzelf af", "De wrijving met het wegdek verdwijnt bergop"], 2,
    "Bij constante snelheid moet de voorwaartse kracht alle tegenwerkende krachten opheffen. Bergop komt de zwaartekracht erbij."),
 ww("Als een voorwerp met constante snelheid beweegt, is de totale arbeid van alle krachten samen 0 J.", True,
    "Waar: bij constante snelheid verandert de bewegingsenergie niet, dus de totale arbeid is nul."),
 ww("Twee honden trekken een slee elk met 60 N over 10 m. De totale arbeid is dan 600 J.", False,
    "Onwaar: beide honden verrichten 60 N × 10 m = 600 J, samen dus 1200 J."),
 ww("De zwaartekracht verricht positieve arbeid op een voorwerp dat naar beneden valt.", True,
    "Waar: de zwaartekracht wijst omlaag, net als de verplaatsing, dus de arbeid is positief."),
 ww("Een kracht die loodrecht op de verplaatsing staat, verricht negatieve arbeid.", False,
    "Onwaar: een loodrechte kracht verricht geen arbeid (W = 0 J). Negatieve arbeid vraagt een kracht tegen de verplaatsing in."),
 inv("Zes sledehonden trekken samen een slee over 300 m. Samen verrichten ze 54 kJ arbeid. Hoeveel newton kracht oefent elke hond uit?",
     "30|30 N", "Totale kracht = 54000 J / 300 m = 180 N. Per hond: 180 N / 6 = 30 N."),
 inv("Een fietser ondervindt 45 N weerstand en fietst 2,0 km met constante snelheid. Hoeveel kJ arbeid verricht zijn spierkracht?",
     "90|90 kJ|90000|90000 J", "Voorwaartse kracht = 45 N. W = 45 N × 2000 m = 90000 J = 90 kJ."),
 inv("Een hijskraan tilt een last van 500 kg met constante snelheid 12 m omhoog (g = 10 N/kg). Hoeveel kJ arbeid verricht de kraan?",
     "60|60 kJ|60000|60000 J", "F = 500 × 10 = 5000 N. W = 5000 N × 12 m = 60000 J = 60 kJ."),
 inv("Een auto remt met een gemiddelde wrijvingskracht van 3200 N over een afstand van 15 m tot stilstand. Hoeveel kJ bewegingsenergie is omgezet in warmte?",
     "48|48 kJ|48000|48000 J", "W = F × s = 3200 N × 15 m = 48000 J = 48 kJ."),
 op("Een skater rijdt met constante snelheid over een vlakke weg. Leg uit waarom zijn bewegingsenergie niet verandert, terwijl hij steeds kracht zet.",
    "De voorwaartse kracht is even groot als de weerstandskracht. De positieve arbeid van de voorwaartse kracht is even groot als de negatieve arbeid van de weerstandskracht, dus de totale arbeid is nul. De energie die hij toevoert wordt omgezet in warmte.",
    ["even groot/gelijk/evenwicht", "negatieve/tegengesteld/warmte"],
    "De totale arbeid is nul, dus de bewegingsenergie blijft gelijk; de toegevoerde energie eindigt als warmte."),
]

E = [
 mc("Een kar wordt vanuit stilstand over 40 m getrokken met 90 N voorwaarts. De wrijvingskracht is 30 N. Hoeveel bewegingsenergie heeft de kar na 40 m?",
    "2400 J", ["3600 J", "1200 J", "4800 J"], 3, "Resulterende kracht = 90 N - 30 N = 60 N. Bewegingsenergie = 60 N × 40 m = 2400 J."),
 mc("Een auto rijdt met constante snelheid; de motor levert 2000 N voorwaarts over 3,0 km. Welke uitspraak over de totale arbeid en de energie is juist?",
    "De totale arbeid is 0 J; de arbeid van de motor wordt warmte",
    ["De totale arbeid is 6,0 MJ; de auto krijgt bewegingsenergie", "De totale arbeid is 6,0 MJ; alles wordt warmte",
     "De totale arbeid is 0 J; de auto verliest bewegingsenergie"], 1,
    "De motor verricht +6,0 MJ, de weerstand -6,0 MJ. Totaal 0 J, bewegingsenergie gelijk, de energie eindigt als warmte."),
 mc("Een container van 25 kg wordt met constante snelheid 4,0 m hoger gehesen (g = 9,81 N/kg). Hoeveel arbeid verricht de hijskracht?",
    "0,98 kJ", ["9,8 kJ", "0,25 kJ", "2,5 kJ"], 0, "F = 25 × 9,81 = 245 N. W = 245 N × 4,0 m = 981 J, ongeveer 0,98 kJ."),
 mc("Een wielrenner (samen met fiets 80 kg) klimt 1500 hoogtemeters (g = 10 N/kg). Hoeveel arbeid levert hij tegen de zwaartekracht?",
    "1200 kJ", ["120 kJ", "12000 kJ", "1,5 kJ"], 2, "F = 80 × 10 = 800 N. W = 800 N × 1500 m = 1 200 000 J = 1200 kJ."),
 mc("Een fietser heeft 900 J bewegingsenergie en rijdt zonder te trappen 150 m uit tot stilstand. Hoe groot is de gemiddelde weerstandskracht?",
    "6,0 N", ["0,17 N", "15 N", "60 N"], 3, "De negatieve arbeid is 900 J: F × 150 m = 900 J, dus F = 900 / 150 = 6,0 N."),
 mc("Een fietser rijdt met dezelfde constante snelheid eerst over vlak terrein en daarna bergop. De weerstand is gelijk. Hoe verandert de arbeid per meter van zijn spierkracht?",
    "Die wordt groter, want hij werkt ook tegen de zwaartekracht in",
    ["Die blijft gelijk, want de snelheid is gelijk", "Die wordt kleiner, want bergop gaat hij langzamer", "Die wordt nul, want de bewegingsenergie verandert niet"], 1,
    "Bergop moet de voorwaartse kracht ook de zwaartekracht compenseren; dus meer kracht en meer arbeid per meter."),
 mc("Een kracht van 150 N versnelt een steen over 0,80 m vanuit stilstand (geen wrijving). Daarna glijdt de steen 40 m over ruw ijs tot stilstand. Hoe groot is de gemiddelde wrijvingskracht?",
    "3,0 N", ["120 N", "150 N", "0,33 N"], 0,
    "Bewegingsenergie = 150 N × 0,80 m = 120 J. Die verdwijnt door wrijvingsarbeid: F × 40 m = 120 J, dus F = 3,0 N."),
 mc("Een bal wordt omhooggegooid en valt terug naar de beginhoogte (geen luchtweerstand). Welke arbeid verricht de zwaartekracht over de hele rit?",
    "0 J, de negatieve en positieve arbeid zijn even groot",
    ["Positief, want de bal valt uiteindelijk omlaag", "Negatief, want de bal verliest bewegingsenergie omhoog", "Twee keer zoveel als omhoog, want de bal valt ook terug"], 2,
    "Omhoog is de arbeid negatief, omlaag over dezelfde afstand even groot en positief. Samen 0 J."),
 mc("Een spijker gaat per slag 0,40 cm het hout in met een gemiddelde kracht van 600 N. Hoeveel arbeid verricht de hamer per slag?",
    "2,4 J", ["240 J", "1500 J", "0,24 J"], 1, "0,40 cm = 0,0040 m. W = 600 N × 0,0040 m = 2,4 J."),
 mc("Twee mensen duwen een auto vanuit stilstand 15 m ver, met 200 N en 150 N in dezelfde richting. De wrijving is 100 N. Hoeveel bewegingsenergie heeft de auto dan?",
    "3750 J", ["5250 J", "3000 J", "6750 J"], 0, "Resulterende kracht = 200 + 150 - 100 = 250 N. Bewegingsenergie = 250 N × 15 m = 3750 J."),
 mc("Een trein remt tot stilstand en verliest 12 MJ bewegingsenergie over 600 m. Hoe groot is de gemiddelde remkracht?",
    "20 kN", ["2,0 kN", "200 kN", "5,0 kN"], 3, "F = W / s = 12 000 000 J / 600 m = 20 000 N = 20 kN."),
 ww("Een remkracht van 5000 N die een auto over 20 m tot stilstand brengt, verricht -100 kJ arbeid.", True,
    "Waar: de remkracht werkt tegen de beweging in. W = -5000 N × 20 m = -100 000 J = -100 kJ."),
 ww("Als je een voorwerp met constante snelheid 3,0 m omhoog tilt, verrichten spierkracht en zwaartekracht allebei positieve arbeid.", False,
    "Onwaar: de spierkracht verricht positieve arbeid, maar de zwaartekracht werkt omlaag en verricht even grote negatieve arbeid."),
 ww("Een kist die met constante snelheid een helling op wordt getrokken, krijgt steeds meer bewegingsenergie omdat de trekkracht positieve arbeid verricht.", False,
    "Onwaar: de snelheid is constant, dus de bewegingsenergie blijft gelijk. De arbeid van de trekkracht wordt gecompenseerd door negatieve arbeid van wrijving en zwaartekracht."),
 ww("Voor een auto die vanuit stilstand versnelt is de totale arbeid gelijk aan de bewegingsenergie die de auto erbij krijgt.", True,
    "Waar: de totale arbeid van alle krachten is de overgedragen energie, en die verschijnt als bewegingsenergie."),
 inv("Een heftruck tilt een pallet van 350 kg met constante snelheid eerst 1,2 m en daarna nog 0,80 m omhoog (g = 10 N/kg). Hoeveel joule arbeid verricht de heftruck in totaal?",
     "7000|7000 J|7 kJ|7,0 kJ|7.0 kJ", "F = 350 × 10 = 3500 N. Totale hoogte 2,0 m: W = 3500 N × 2,0 m = 7000 J."),
 inv("Twee mannen duwen een auto 80 m ver vanuit stilstand, ieder met 175 N. De wrijving is 280 N. Hoeveel joule bewegingsenergie heeft de auto na 80 m?",
     "5600|5600 J|5,6 kJ|5.6 kJ", "Resulterende kracht = 2 × 175 - 280 = 70 N. Bewegingsenergie = 70 N × 80 m = 5600 J."),
 inv("Een fietser van 90 kg (met fiets) klimt 120 hoogtemeters (g = 10 N/kg). Hoeveel kJ arbeid verricht hij tegen de zwaartekracht?",
     "108|108 kJ|108000|108000 J", "F = 90 × 10 = 900 N. W = 900 N × 120 m = 108 000 J = 108 kJ."),
 inv("Drie honden trekken een slee 90 m ver met constante snelheid, ieder met 35 N. Hoeveel joule aan warmte ontstaat door de wrijving?",
     "9450|9450 J|9,45 kJ|9.45 kJ", "Totale trekkracht = 3 × 35 = 105 N, gelijk aan de wrijving. W = 105 N × 90 m = 9450 J, en die wordt warmte."),
 op("Een auto remt met een kleinere remkracht dan eerst, vanaf dezelfde snelheid. Leg uit waarom de remweg dan langer wordt.",
    "De auto heeft dezelfde bewegingsenergie, en die moet door de negatieve arbeid van de remkracht verdwijnen. Arbeid is W = F × s. Bij een kleinere kracht is dus een grotere afstand nodig om dezelfde energie in warmte om te zetten.",
    ["bewegingsenergie/energie", "afstand/verplaatsing"],
    "Dezelfde bewegingsenergie moet door W = F × s worden weggenomen; kleinere F betekent grotere s."),
]

KOP = "/* =========================================================\n   Duru's Natuurkunde (HAVO 3) — %s\n   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)\n   ========================================================= */\n"
for nr, letter, vr in ((78, "C", C), (79, "D", D), (80, "E", E)):
    assert len(vr) == 20 and [v["type"] for v in vr].count("mc") == 11
    titel = f"Toets {nr} — §1.5 Arbeid en Energieomzetting — Toets {letter}"
    d = {"id": f"ex-h3-natuurkunde-{nr}", "hoofdstuk": 1, "paragraaf": "1.5", "titel": titel,
         "vak": "Natuurkunde · HAVO 3 (H1)", "icoon": "⚙️", "duurMin": 30, "vragen": vr}
    p = os.path.join("havo3/natuurkunde/js/data", f"examen_{nr}.js")
    open(p, "w", encoding="utf-8").write(KOP % titel + "DURU.registerExamen(" + json.dumps(d, ensure_ascii=False, indent=2) + ");\n")
    print(p, [v["antwoord"] for v in vr if v["type"] == "mc"])
