# -*- coding: utf-8 -*-
# Schrijft examen_75/76/77 (natuurkunde §1.4). Pure rekencontrole met assert.
import json, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'havo3', 'natuurkunde', 'js', 'data')

def mc(v, good, bad, pos, uitleg):
    o = list(bad); o.insert(pos, good)
    return {"type": "mc", "vraag": v, "opties": o, "antwoord": pos, "uitleg": uitleg}
def ww(v, a, uitleg):
    return {"type": "waaronwaar", "vraag": v, "antwoord": a, "uitleg": ("Waar: " if a else "Onwaar: ") + uitleg}
def inv(v, a, uitleg):
    return {"type": "invul", "vraag": v, "antwoord": a, "uitleg": uitleg}
def op(v, model, keys, uitleg):
    return {"type": "open", "vraag": v, "modelantwoord": model, "minTreffers": 1, "sleutelwoorden": keys, "uitleg": uitleg}

# ---- rekencontrole ----
assert 54/3.6 == 15
assert abs(6.0*0.70-4.2) < 1e-9 and abs(18/2*4.0-36) < 1e-9 and 10*0.9+11 == 20 and 15/3.0 == 5.0
assert 1200*6.0 == 7200 and 15/3.0 == 5 and abs(15/2*5.0-37.5) < 1e-9
assert 90/3.6*0.80 == 20 and 20+62 == 82
v=15; s=0.50; a=v*v/(2*s); assert a == 225 and 800*a == 180000
assert abs(126/3.6*0.8-28) < 1e-9
assert 40**2/(2*8.0) == 100 and 20**2/(2*50) == 4.0
assert round(5.0*(70/30)**2) == 27 and 20*(1.2-0.6) == 12
assert 30/(12/2) == 5.0
assert (36-24)/15 == 0.8 and 14/(3000/1500) == 7.0
assert 25**2/(2*62.5) == 5.0 and 1100*5.0 == 5500
assert 15*0.9 == 13.5 and 15/3.0 == 5.0 and abs(13.5+15/2*5.0-51) < 1e-9
assert 1.0/(20/2) == 0.10
assert 5.0*0.8 == 4.0 and 5.0**2/(2*2.5) == 5.0 and 12-4.0-5.0 == 3.0
assert 20/5.0 == 4.0 and 0.25*4 == 1.0

C = [
 mc("Wat wordt bij een noodstop bedoeld met de <b>reactieafstand</b>?",
    "De afstand die je aflegt tussen het zien van het gevaar en het begin van het remmen",
    ["De afstand die je aflegt vanaf het intrappen van de rem tot je stilstaat",
     "De totale afstand die je aflegt van het zien van het gevaar tot stilstand",
     "De afstand waarover de voorkant van de auto bij een botsing indeukt"], 2,
    "De reactieafstand leg je af tijdens de reactietijd, voordat de rem wordt ingetrapt. De afstand tijdens het remmen is de remweg."),
 mc("Welke situatie geeft bij dezelfde snelheid een <b>grotere reactieafstand</b>?",
    "De bestuurder kijkt even op zijn telefoon",
    ["Het wegdek is nat en glad door de regen", "De banden van de auto hebben nog maar weinig profiel",
     "De auto is zwaar beladen met bagage"], 0,
    "Afleiding verlengt de reactietijd, dus is s = v · t bij dezelfde snelheid groter. Wegdek, banden en lading beïnvloeden alleen de remweg."),
 mc("In het (v,t)-diagram van een noodstop zie je eerst een horizontaal stuk. Wat stelt dit horizontale stuk voor?",
    "De reactietijd, waarin de snelheid gelijk blijft",
    ["De remtijd, waarin de snelheid constant afneemt", "Het moment waarop de auto precies stilstaat",
     "De botstijd waarin de kreukelzone indeukt"], 3,
    "Tijdens de reactietijd rem je nog niet, dus de snelheid verandert niet en de grafiek loopt horizontaal."),
 mc("Wat gebeurt er met de reactieafstand en de remweg als je langzamer gaat rijden?",
    "Beide worden kleiner",
    ["Alleen de remweg wordt kleiner", "Alleen de reactieafstand wordt kleiner", "Beide blijven even groot"], 1,
    "Zowel de reactieafstand als de remweg zijn kleiner bij een lagere beginsnelheid."),
 mc("Waardoor vermindert de schuimlaag in een helm de kracht op je hoofd bij een val?",
    "De schuimlaag deukt in, waardoor het hoofd langer de tijd krijgt om tot stilstand te komen",
    ["De schuimlaag zorgt dat het hoofd tijdens de val minder snel naar beneden valt",
     "De schuimlaag zorgt dat het hoofd juist korter in contact is met de grond",
     "De schuimlaag maakt het hoofd lichter, zodat de kracht automatisch kleiner is"], 1,
    "Door het indeuken wordt de remweg en de tijd van de botsing groter. Daardoor is de vertraging kleiner en dus ook de kracht (F = m · a)."),
 mc("Waartegen beschermt een goed afgestelde <b>hoofdsteun</b> in een auto?",
    "Tegen nekklachten (whiplash) als iemand de auto van achteren aanrijdt",
    ["Tegen letsel aan het gezicht door het dashboard bij een frontale botsing",
     "Tegen rondvliegend glas na een zijdelingse botsing",
     "Tegen het uit de stoel schuiven tijdens een noodstop"], 3,
    "Bij een aanrijding van achteren versnellen auto en passagiers; het hoofd kan naar achteren slaan. De hoofdsteun voorkomt dat."),
 mc("Wat is de functie van de extra stevige <b>kooi</b> waarin de inzittenden van een auto zitten?",
    "De cabine wordt bij een botsing niet ingedrukt",
    ["De kooi deukt gecontroleerd in en verlengt zo de botstijd",
     "De kooi zorgt ervoor dat de auto een kortere remweg heeft",
     "De kooi zorgt ervoor dat de bestuurder sneller reageert"], 0,
    "De kooi blijft intact en beschermt de inzittenden. Het indeuken is juist de taak van de kreukelzone."),
 mc("Een bromfiets rijdt met 54 km/h. Hoe groot is deze snelheid in m/s?",
    "15 m/s", ["9,0 m/s", "194 m/s", "3,6 m/s"], 2,
    "Van km/h naar m/s deel je door 3,6: 54 : 3,6 = 15 m/s."),
 mc("Bij welke combinatie is de <b>remweg</b> van een auto het kleinst?",
    "Goede banden op een droge weg met een lege auto",
    ["Versleten banden op een droge weg met een lege auto",
     "Goede banden op een natte weg met een lege auto",
     "Goede banden op een droge weg met een zwaar beladen auto"], 3,
    "De remweg is kleiner bij een goed wegdek, goede banden en een niet zwaar beladen voertuig."),
 mc("Waarom verkleint een <b>airbag</b> de kracht op een inzittende bij een botsing?",
    "De airbag vergroot de remweg en verdeelt de kracht over een groter oppervlak",
    ["De airbag verkleint de massa van de inzittende tijdens de botsing",
     "De airbag zorgt dat de inzittende juist sneller tot stilstand komt",
     "De airbag verhoogt de snelheid van de inzittende vlak voor de botsing"], 0,
    "Een airbag geeft de inzittende meer remweg en tijd en verdeelt de kracht over een groter oppervlak."),
 mc("Bij een botsing is de snelheidsverandering van een inzittende gelijk, maar de botstijd wordt langer. Wat gebeurt er met de vertraging?",
    "De vertraging wordt kleiner", ["De vertraging wordt groter", "De vertraging blijft gelijk", "De vertraging wordt precies nul"], 2,
    "Vertraging = Δv / Δt. Bij gelijke Δv en een grotere Δt wordt de vertraging kleiner."),
 ww("Bij dezelfde snelheid heeft een bestuurder zonder afleiding een kleinere reactieafstand dan een bestuurder die afgeleid is.", True,
    "Een goede concentratie geeft een kortere reactietijd, dus een kleinere reactieafstand."),
 ww("Een goed profiel op de banden verkleint de reactieafstand van een auto.", False,
    "Het bandenprofiel verkleint de remweg, niet de reactieafstand. Die hangt af van de reactietijd en de snelheid."),
 ww("Bij een botsing blijven de inzittenden met de snelheid van de auto doorbewegen totdat ze ergens tegenaan botsen.", True,
    "De inzittenden bewegen even snel als de auto. Daarom houdt de gordel hen op hun plaats."),
 ww("Een airbag blijft na de botsing volledig opgeblazen, zodat de inzittenden ook tegen een tweede klap beschermd blijven.", False,
    "Een airbag loopt na de botsing snel weer leeg, onder andere om te voorkomen dat je stikt."),
 inv("Een fietser rijdt met 6,0 m/s en heeft een reactietijd van 0,70 s. Hoeveel meter bedraagt zijn reactieafstand?",
     "4,2|4,2 m|4,2 meter|4.2", "s = v · t = 6,0 · 0,70 = 4,2 m."),
 inv("Een auto remt met constante vertraging in 4,0 s af van 18 m/s tot stilstand. Hoeveel meter bedraagt de remweg?",
     "36|36 m|36 meter", "De gemiddelde snelheid is 18 / 2 = 9,0 m/s. s = 9,0 · 4,0 = 36 m."),
 inv("Een scooter rijdt met 10 m/s, heeft een reactietijd van 0,90 s en een remweg van 11 m. Hoeveel meter bedraagt de stopafstand?",
     "20|20 m|20 meter", "s_reactie = 10 · 0,90 = 9,0 m. s_stop = 9,0 + 11 = 20 m."),
 inv("Een auto remt in 3,0 s van 15 m/s tot stilstand. Hoeveel m/s² bedraagt de gemiddelde vertraging?",
     "5|5,0|5 m/s²|5,0 m/s²|5.0", "a = Δv / Δt = 15 / 3,0 = 5,0 m/s²."),
 op("Leg uit waarom het voor de veiligheid van de inzittenden gunstig is dat de voorkant van een auto bij een botsing indeukt.",
    "Doordat de voorkant indeukt, duurt de botsing langer. Daardoor is de vertraging van de auto en van de inzittenden kleiner. Omdat F = m · a is ook de kracht op de inzittenden dan kleiner.",
    ["botstijd/tijdsduur/langer", "vertraging/versnelling"],
    "De kreukelzone verlengt de botstijd, waardoor de vertraging en dus de kracht kleiner worden."),
]

D = [
 mc("Een automobilist op 126 km/h heeft 0,80 s nodig om op een gevaar te reageren. Welke afstand rijdt de auto in die tijd nog door?",
    "28 m", ["35 m", "101 m", "8,0 m"], 1,
    "126 km/h = 126 : 3,6 = 35 m/s. s = 35 · 0,80 = 28 m."),
 mc("Een auto rijdt eerst met 36 km/h en later met 72 km/h. De reactietijd en de remkracht zijn steeds gelijk. Hoe veranderen reactieafstand en remweg?",
    "De reactieafstand wordt 2 keer zo groot, de remweg 4 keer zo groot",
    ["De reactieafstand wordt 4 keer zo groot, de remweg 2 keer zo groot",
     "Zowel de reactieafstand als de remweg wordt 2 keer zo groot",
     "Zowel de reactieafstand als de remweg wordt 4 keer zo groot"], 3,
    "s_reactie = v · t is recht evenredig met v. De remweg groeit kwadratisch met v (2² = 4)."),
 mc("Welke factor beïnvloedt de <b>reactieafstand</b> wel, maar de remweg niet?",
    "Het gebruik van medicijnen die slaperig maken",
    ["Het profiel van de banden van de auto", "Het onderhoud van de remmen van de auto", "Een nat wegdek door de regen"], 3,
    "Medicijnen, alcohol en vermoeidheid verlengen de reactietijd. Banden, remmen en wegdek bepalen de remweg."),
 mc("Hoe verschilt het (v,t)-diagram van een noodstop op een glad wegdek van dat op een droog wegdek?",
    "Het dalende stuk loopt minder steil, de remtijd is langer",
    ["Het horizontale stuk is langer, het dalende stuk even steil",
     "Het dalende stuk loopt steiler, de remtijd is korter",
     "De beginsnelheid is lager, het dalende stuk even steil"], 0,
    "Op een glad wegdek is de remkracht kleiner, dus de vertraging kleiner: de grafiek daalt minder steil en het remmen duurt langer."),
 mc("Een auto deukt bij een botsing 0,25 m in. Een andere auto, met dezelfde massa en snelheid, deukt 1,0 m in. Hoe verhouden de gemiddelde krachten zich?",
    "De kracht is bij de tweede auto 4 keer zo klein",
    ["De kracht is bij de tweede auto 4 keer zo groot",
     "De kracht is bij de tweede auto 16 keer zo klein",
     "De kracht is bij beide auto's even groot"], 2,
    "Een 4 keer zo grote indeukafstand betekent 4 keer zo lange botstijd, een 4 keer zo kleine vertraging en dus een 4 keer zo kleine kracht."),
 mc("Waarom schiet een inzittende zonder gordel bij een frontale botsing naar voren?",
    "Hij blijft met de beginsnelheid doorbewegen terwijl de auto al stilstaat",
    ["De botsing geeft hem een extra duw naar voren", "De zwaartekracht trekt hem bij het remmen naar voren",
     "Zijn massa wordt tijdens het remmen groter"], 1,
    "Zonder krachten blijft een voorwerp met dezelfde snelheid bewegen. De inzittende beweegt door totdat hij ergens tegenaan botst."),
 mc("De schuimlaag in de helm van een autocoureur is na een crash <b>plastisch</b> vervormd. Wat betekent dit?",
    "De schuimlaag blijft ingedeukt, dus de helm moet worden vervangen",
    ["De schuimlaag veert terug, dus de helm kan opnieuw gebruikt worden",
     "De schuimlaag is volledig verdwenen door de klap",
     "De schuimlaag is groter geworden en beschermt beter"], 0,
    "Plastische vervorming is blijvend. De schuimlaag kan een volgende klap niet meer goed opvangen."),
 mc("Een auto remt met constante vertraging van 20 m/s tot stilstand. Wat is de gemiddelde snelheid tijdens het remmen?",
    "10 m/s", ["20 m/s", "5,0 m/s", "40 m/s"], 2,
    "De gemiddelde snelheid is (20 + 0) / 2 = 10 m/s."),
 mc("Wat stelt de oppervlakte van het schuin dalende stuk in het (v,t)-diagram van een noodstop voor?",
    "De afgelegde weg tijdens het remmen, de remweg",
    ["De afgelegde weg vóór het remmen, de reactieafstand", "De tijd die het remmen duurt, de remtijd",
     "De grootte van de vertraging in m/s²"], 0,
    "De oppervlakte onder een (v,t)-grafiek is de afgelegde afstand; het dalende stuk hoort bij het remmen."),
 mc("Een auto remt met een vaste remkracht. Hoe verandert de vertraging als de massa van de auto (door lading) twee keer zo groot wordt?",
    "De vertraging wordt 2 keer zo klein", ["De vertraging wordt 2 keer zo groot", "De vertraging blijft gelijk", "De vertraging wordt 4 keer zo klein"], 3,
    "a = F / m. Bij gelijke kracht en dubbele massa halveert de vertraging."),
 mc("Een auto rijdt 20 m/s en remt met een vertraging van 5,0 m/s². Hoe lang duurt het remmen tot stilstand?",
    "4,0 s", ["0,25 s", "100 s", "15 s"], 1,
    "Δt = Δv / a = 20 / 5,0 = 4,0 s."),
 ww("Bij een botsing is de gemiddelde kracht op de inzittenden groter naarmate de botstijd korter is (bij dezelfde snelheidsverandering).", True,
    "Een kortere botstijd geeft een grotere vertraging en dus een grotere kracht."),
 ww("Tijdens het remmen tot stilstand is de gemiddelde snelheid gelijk aan de beginsnelheid.", False,
    "De snelheid daalt gelijkmatig naar 0, dus de gemiddelde snelheid is de helft van de beginsnelheid."),
 ww("Bij dezelfde remkracht heeft een zwaar beladen auto een kleinere remweg dan een lege auto.", False,
    "Door de grotere massa is de vertraging kleiner en dus de remweg groter."),
 ww("Een helm verdeelt de kracht bij een val over een groter oppervlak van het hoofd.", True,
    "Naast het verlengen van de remweg verdeelt een helm de kracht over een groter oppervlak."),
 inv("Een auto van 1200 kg remt met een gemiddelde vertraging van 6,0 m/s². Hoeveel newton bedraagt de remkracht?",
     "7200|7200 N|7,2 kN|7,2 kN", "F = m · a = 1200 · 6,0 = 7200 N."),
 inv("Een vrachtwagen remt met een vertraging van 3,0 m/s² vanaf 15 m/s tot stilstand. Hoeveel meter bedraagt de remweg?",
     "37,5|37,5 m|37,5 meter|37.5", "Remtijd = 15 / 3,0 = 5,0 s. Gemiddelde snelheid 7,5 m/s. s = 7,5 · 5,0 = 37,5 m."),
 inv("Een bestuurder rijdt 90 km/h en ziet een ree oversteken. Hij heeft 0,80 s nodig om te reageren en legt na het intrappen van de rem nog 62 m af. Hoeveel meter heeft hij in totaal nodig om stil te staan?",
     "82|82 m|82 meter", "90 km/h = 25 m/s. s_reactie = 25 · 0,80 = 20 m. s_stop = 20 + 62 = 82 m."),
 inv("Een auto van 800 kg rijdt met 15 m/s tegen een muur en deukt 0,50 m in tot stilstand. Hoeveel newton bedraagt de gemiddelde kracht?",
     "180000|180000 N|180 kN|180", "Gemiddelde snelheid 7,5 m/s, botstijd 0,50 / 7,5 = 0,0667 s. a = 15 / 0,0667 = 225 m/s². F = 800 · 225 = 180 000 N."),
 op("Leg uit waarom iemand die tijdens het rijden een berichtje typt een grotere stopafstand heeft, terwijl de remweg van de auto niet verandert.",
    "Door de afleiding is de reactietijd langer. In die tijd rijdt de auto nog met dezelfde constante snelheid door, dus de reactieafstand wordt groter. De remweg hangt alleen af van snelheid, remkracht en wegdek. De stopafstand is de som van beide en wordt dus groter.",
    ["reactietijd/reactie", "constante snelheid/doorrijdt/doorrijden"],
    "Afleiding verlengt de reactietijd en dus de reactieafstand; de remweg blijft gelijk."),
]

E = [
 mc("Een auto rijdt met 144 km/h en remt met een constante vertraging van 8,0 m/s² tot stilstand. Hoe groot is de remweg?",
    "100 m", ["200 m", "320 m", "5,0 m"], 3,
    "144 km/h = 40 m/s. Remtijd = 40 / 8,0 = 5,0 s, gemiddelde snelheid 20 m/s: s = 20 · 5,0 = 100 m."),
 mc("Een auto remt vanaf 20 m/s en komt na een remweg van 50 m tot stilstand. Hoe groot is de gemiddelde vertraging?",
    "4,0 m/s²", ["2,5 m/s²", "8,0 m/s²", "0,40 m/s²"], 2,
    "Gemiddelde snelheid 10 m/s, remtijd = 50 / 10 = 5,0 s. a = 20 / 5,0 = 4,0 m/s²."),
 mc("Bij 30 km/h is de remweg van een auto 5,0 m. Hoe groot is de remweg bij 70 km/h onder dezelfde omstandigheden?",
    "27 m", ["12 m", "35 m", "54 m"], 0,
    "De remweg is evenredig met v². Verhouding (70 / 30)² = 5,44, dus 5,0 · 5,44 = 27 m."),
 mc("Auto A en auto B rijden 20 m/s met een gelijke remweg. De reactietijd van A is 0,60 s en die van B is 1,2 s. Hoeveel groter is de stopafstand van B?",
    "12 m", ["24 m", "36 m", "0 m"], 0,
    "Het verschil in reactietijd is 0,60 s. Het verschil in afstand is 20 · 0,60 = 12 m."),
 mc("Twee auto's met dezelfde massa en snelheid botsen. Auto A deukt 0,40 m in, auto B 1,20 m. Wat is de verhouding van de gemiddelde krachten?",
    "FA is 3 keer zo groot als FB",
    ["FB is 3 keer zo groot als FA", "FA is 9 keer zo groot als FB",
     "FA en FB zijn gelijk omdat massa en snelheid gelijk zijn"], 1,
    "Een 3 keer zo grote indeukafstand geeft een 3 keer zo lange botstijd en dus een 3 keer zo kleine kracht."),
 mc("In het (v,t)-diagram van een noodstop is de oppervlakte van het dalende driehoekje 30 m en de beginsnelheid 12 m/s. Hoe lang duurt het remmen?",
    "5,0 s", ["2,5 s", "0,40 s", "360 s"], 3,
    "Oppervlakte driehoek = 1/2 · v · t, dus t = 2 · 30 / 12 = 5,0 s."),
 mc("Een auto rijdt met 15 m/s. De stopafstand is 36 m, waarvan 24 m remweg. Hoe groot is de reactietijd?",
    "0,80 s", ["2,4 s", "1,6 s", "0,40 s"], 2,
    "s_reactie = 36 - 24 = 12 m. t = s / v = 12 / 15 = 0,80 s."),
 mc("Een auto wordt van achteren aangereden en versnelt naar voren, ook de stoel en de romp. Waarom kan zonder hoofdsteun het hoofd naar achteren slaan?",
    "Het hoofd blijft even op zijn plaats terwijl stoel en romp naar voren versnellen",
    ["Het hoofd wordt door de veiligheidsgordel naar achteren getrokken",
     "Het hoofd is lichter dan de romp en versnelt daarom naar achteren",
     "De airbag duwt het hoofd tegen de rugleuning van de stoel"], 1,
    "Het hoofd volgt de versnelling niet meteen; ten opzichte van de romp beweegt het naar achteren. De hoofdsteun vangt dat op."),
 mc("De reactietijd wordt langer, terwijl de remvertraging gelijk blijft. Hoe verandert het (v,t)-diagram van de noodstop?",
    "Het horizontale deel wordt langer, het dalende deel blijft even steil",
    ["Het dalende deel wordt steiler, het horizontale deel blijft even lang",
     "Het horizontale deel blijft even lang, het dalende deel wordt minder steil",
     "Beide delen worden korter, de beginsnelheid blijft gelijk"], 3,
    "Een langere reactietijd verlengt alleen het horizontale deel. De steilheid van het dalende deel (de vertraging) verandert niet."),
 mc("Een auto van 1500 kg rijdt met 14 m/s en remt met een constante remkracht van 3,0 kN. Hoe lang duurt het remmen tot stilstand?",
    "7,0 s", ["3,5 s", "0,14 s", "28 s"], 0,
    "a = F / m = 3000 / 1500 = 2,0 m/s². Δt = 14 / 2,0 = 7,0 s."),
 mc("Welke maatregel verkleint zowel de reactieafstand als de remweg?",
    "Het rijden met een lagere beginsnelheid",
    ["Het gebruik van banden met meer profiel", "Het rijden als een uitgeruste, geconcentreerde bestuurder",
     "Het rijden met een minder zwaar beladen auto"], 2,
    "Een lagere snelheid verkleint beide afstanden. De andere maatregelen werken op slechts één van de twee."),
 ww("Bij dezelfde remkracht heeft een auto met een grotere massa een kleinere vertraging.", True,
    "a = F / m: bij een grotere massa en gelijke kracht is de vertraging kleiner."),
 ww("Als de snelheid van een auto verdubbelt bij gelijke reactietijd, wordt de reactieafstand vier keer zo groot.", False,
    "s = v · t: bij dubbele snelheid wordt de reactieafstand 2 keer zo groot. Het is de remweg die 4 keer zo groot wordt."),
 ww("Als bij een botsing de vertraging van een inzittende kleiner is, is ook de kracht op die inzittende kleiner.", True,
    "F = m · a: bij gelijke massa hoort een kleinere vertraging bij een kleinere kracht."),
 ww("Een airbag verkleint de kracht op een inzittende doordat de remweg van de inzittende korter wordt.", False,
    "Een airbag vergroot de remweg van de inzittende, waardoor de vertraging en dus de kracht kleiner worden."),
 inv("Een auto van 1100 kg rijdt met 90 km/h en komt na een remweg van 62,5 m tot stilstand. Hoeveel newton bedraagt de gemiddelde remkracht?",
     "5500|5500 N|5,5 kN|5,5", "90 km/h = 25 m/s. a = v² / (2s) = 625 / 125 = 5,0 m/s². F = 1100 · 5,0 = 5500 N."),
 inv("Een auto rijdt met 54 km/h en de reactietijd is 0,90 s. Daarna remt hij met een vertraging van 3,0 m/s² tot stilstand. Hoeveel meter bedraagt de stopafstand?",
     "51|51 m|51 meter", "54 km/h = 15 m/s. s_reactie = 15 · 0,90 = 13,5 m. Remtijd 15 / 3,0 = 5,0 s, remweg 7,5 · 5,0 = 37,5 m. Samen 51 m."),
 inv("Een auto van 1250 kg botst met 72 km/h tegen een muur en deukt 1,0 m in tot stilstand. Hoeveel seconden duurt de botsing?",
     "0,10|0,1|0,10 s|0,1 s|0.1", "72 km/h = 20 m/s. Gemiddelde snelheid 10 m/s. t = 1,0 / 10 = 0,10 s."),
 inv("Een fietser rijdt met 5,0 m/s en ziet op 12 m afstand een obstakel. Zijn reactietijd is 0,80 s en daarna remt hij met 2,5 m/s². Hoeveel meter voor het obstakel staat hij stil?",
     "3,0|3|3 m|3,0 m|3 meter", "Reactieafstand 5,0 · 0,80 = 4,0 m. Remweg = 5,0² / (2 · 2,5) = 5,0 m. Stopafstand 9,0 m, dus 12 - 9,0 = 3,0 m over."),
 op("Een fietser valt en slaat met zijn hoofd tegen de straat. Leg uit hoe de schuimlaag in zijn helm de kracht op het hoofd verkleint.",
    "De schuimlaag deukt in (indeukt) tijdens de klap. Daardoor duurt het langer voordat het hoofd stilstaat en is de remweg groter. De vertraging is dan kleiner en dus ook de kracht (F = m · a). De helm verdeelt de kracht bovendien over een groter oppervlak.",
    ["indeuken/indeukt/vervormt", "botstijd/tijdsduur/langer"],
    "Het indeuken verlengt de botstijd; de vertraging en dus de kracht worden kleiner."),
]

def schrijf(nr, tit, vragen):
    assert len(vragen) == 20
    assert sum(v["type"] == "mc" for v in vragen) == 11
    for v in vragen:
        if v["type"] == "mc": assert len(set(v["opties"])) == 4
    ww_ = [v["antwoord"] for v in vragen if v["type"] == "waaronwaar"]
    assert ww_.count(True) == 2 and ww_.count(False) == 2
    d = {"id": "ex-h3-natuurkunde-%d" % nr, "hoofdstuk": 1, "paragraaf": "1.4",
         "titel": "Toets %d — §1.4 Veiligheid, Remweg & Stopafstand — Toets %s" % (nr, tit),
         "vak": "Natuurkunde · HAVO 3 (H1)", "icoon": "🚗", "duurMin": 30, "vragen": vragen}
    kop = ("/* =========================================================\n"
           "   Duru's Natuurkunde (HAVO 3) — Toets %d — §1.4 Veiligheid, Remweg & Stopafstand — Toets %s\n"
           "   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)\n"
           "   ========================================================= */\n") % (nr, tit)
    with open(os.path.join(OUT, "examen_%d.js" % nr), "w", encoding="utf-8") as f:
        f.write(kop + "DURU.registerExamen(" + json.dumps(d, ensure_ascii=False, indent=2) + ");\n")
    print(nr, [v["antwoord"] for v in vragen if v["type"] == "mc"])

schrijf(75, "C", C); schrijf(76, "D", D); schrijf(77, "E", E)
