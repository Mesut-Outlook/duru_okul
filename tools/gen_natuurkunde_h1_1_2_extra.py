import json
OUT = 'havo3/natuurkunde/js/data/'

def fmt(x):
    s = ('%g' % x) if x == int(x) else ('%.2f' % x).rstrip('0')
    return s

def mc(vraag, juist, fout, pos, uitleg):
    o = list(fout); o.insert(pos, juist)
    assert len(o) == 4
    return dict(type='mc', vraag=vraag, opties=o, antwoord=pos, uitleg=uitleg)

def ww(vraag, waar, uitleg):
    return dict(type='waaronwaar', vraag=vraag, antwoord=waar, uitleg=('Waar: ' if waar else 'Onwaar: ') + uitleg)

def inv(vraag, val, unit, uitleg, dec=1):
    v = round(val, dec)
    c = ('%.*f' % (dec, v)).replace('.', ',') if dec else str(int(v))
    alts = {c, c.replace(',', '.'), fmt(v).replace('.', ','), fmt(v)}
    alts |= {a + ' ' + unit for a in list(alts)}
    ant = '|'.join(sorted(alts, key=lambda a: (len(a), a)))
    return dict(type='invul', vraag=vraag, antwoord=ant, uitleg=uitleg)

def op(vraag, model, kw, uitleg):
    return dict(type='open', vraag=vraag, modelantwoord=model, minTreffers=1, sleutelwoorden=kw, uitleg=uitleg)

def write(nr, letter, icoon, vragen):
    assert len(vragen) == 20
    assert sum(v['type'] == 'mc' for v in vragen) == 11
    ex = dict(id=f'ex-h3-natuurkunde-{nr}', hoofdstuk=1, paragraaf='1.2',
              titel=f'Toets {nr} — §1.2 Soorten beweging & Diagrammen — Toets {letter}',
              vak='Natuurkunde · HAVO 3 (H1)', icoon=icoon, duurMin=30, vragen=vragen)
    head = (f"/* =========================================================\n   Duru's Natuurkunde (HAVO 3) — {ex['titel']}\n"
            "   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)\n"
            "   ========================================================= */\n")
    open(OUT + f'examen_{nr}.js', 'w', encoding='utf-8').write(
        head + 'DURU.registerExamen(' + json.dumps(ex, ensure_ascii=False, indent=2) + ');\n')

# ---------------- E (basis) ----------------
a1 = 2100 / 300; assert a1 == 7.0
a3 = (15 - 0) / 5.0; assert a3 == 3.0
a4 = 9.0 * 12; assert a4 == 108
a2 = 45 / 3.6; assert a2 == 12.5
assert 18 / 3.6 == 5.0 and 20 * 3.6 == 72
E = [
 mc("Wat betekent een horizontale lijn in een (s,t)-diagram?", "Het voorwerp staat stil op dezelfde plaats", ["Het voorwerp beweegt met constante snelheid", "Het voorwerp trekt eenparig op", "Het voorwerp remt eenparig af"], 2, "Als s niet verandert terwijl de tijd verstrijkt, legt het voorwerp geen afstand af: het staat stil."),
 mc("Met welke formule bereken je de gemiddelde snelheid uit afstand s en tijd t?", "v<sub>gem</sub> = s / t", ["v<sub>gem</sub> = t / s", "v<sub>gem</sub> = s × t", "v<sub>gem</sub> = s − t"], 0, "Snelheid is de afstand per seconde: v = s / t, met s in m en t in s geeft dat m/s."),
 mc("Wat is de juiste eenheid van versnelling?", "m/s²", ["m/s", "km/h", "m²/s"], 3, "De versnelling geeft aan hoeveel m/s er elke seconde bij komt: (m/s) per s = m/s²."),
 mc("Hoe bereken je de snelheidsverandering Δv?", "Δv = v<sub>eind</sub> − v<sub>begin</sub>", ["Δv = v<sub>begin</sub> − v<sub>eind</sub>", "Δv = v<sub>eind</sub> + v<sub>begin</sub>", "Δv = v<sub>eind</sub> / v<sub>begin</sub>"], 1, "Δv is het verschil tussen de eindsnelheid en de beginsnelheid: Δv = v_eind − v_begin."),
 mc("Wat geeft de steilheid (helling) van de lijn in een (s,t)-diagram aan?", "De snelheid van het voorwerp", ["De versnelling van het voorwerp", "De afgelegde afstand", "De tijd die het voorwerp nodig heeft"], 1, "Hoe steiler de lijn in een (s,t)-diagram, hoe meer afstand per seconde: de steilheid is de snelheid."),
 mc("Wat kun je bepalen met de oppervlakte onder de grafieklijn in een (v,t)-diagram?", "De afgelegde afstand", ["De versnelling", "De gemiddelde snelheid", "De eindsnelheid"], 3, "Afstand = snelheid × tijd, en dat is precies de oppervlakte onder de lijn in een (v,t)-diagram."),
 mc("Een fietser rijdt met 18 km/h. Hoeveel is dat in m/s?", "5,0 m/s", ["64,8 m/s", "50 m/s", "18 m/s"], 0, "Van km/h naar m/s deel je door 3,6: 18 / 3,6 = 5,0 m/s."),
 mc("In een (s,t)-diagram loopt de lijn steeds steiler omhoog. Wat voor beweging is dit?", "Een eenparig versnelde beweging", ["Een eenparige beweging", "Een eenparig vertraagde beweging", "Een stilstaande beweging"], 2, "Een steeds steilere lijn betekent dat de snelheid toeneemt: het voorwerp versnelt."),
 mc("In een (v,t)-diagram loopt de grafieklijn recht omlaag naar v = 0 m/s. Wat voor beweging is dit?", "Een eenparig vertraagde beweging", ["Een eenparig versnelde beweging", "Een beweging met constante snelheid", "Een beweging waarbij het voorwerp stilstaat"], 3, "Een rechte, dalende lijn in een (v,t)-diagram: de snelheid neemt gelijkmatig af tot het voorwerp stilstaat."),
 mc("Wat is de versnelling a precies?", "De verandering van de snelheid per seconde", ["De afstand die je per seconde aflegt", "De totale afgelegde afstand gedeeld door de tijd", "De snelheid op het eindpunt van de beweging"], 1, "De versnelling is de snelheidsverandering per seconde: a = Δv / t."),
 mc("Welke eenheid is NIET geschikt voor een snelheid?", "kg/m", ["cm/s", "km/h", "m/s"], 2, "Snelheid is lengte per tijd. Kilogram is een massa, dus kg/m is geen snelheid."),
 ww("Een rechte, schuin oplopende lijn in een (s,t)-diagram hoort bij een beweging met constante snelheid.", True, "De helling is overal gelijk, dus de snelheid verandert niet."),
 ww("Bij een eenparige beweging is de versnelling gelijk aan 0 m/s².", True, "Er is geen snelheidsverandering, dus Δv = 0 en daarmee a = 0 m/s²."),
 ww("Als de snelheid van een voorwerp 0 m/s is, is de versnelling altijd ook 0 m/s².", False, "Een auto die net begint op te trekken heeft op dat moment v = 0 m/s, maar wel een versnelling groter dan 0."),
 ww("Een snelheid van 20 m/s is gelijk aan 36 km/h.", False, "20 m/s × 3,6 = 72 km/h. Delen door 3,6 doe je alleen van km/h naar m/s."),
 inv("Een hardloper legt in 5,0 minuten 2100 m af. Wat is zijn gemiddelde snelheid in m/s?", a1, "m/s", "5,0 min = 300 s, dus v = 2100 / 300 = 7,0 m/s."),
 inv("Een bromfiets rijdt met een snelheid van 45 km/h. Reken dit om naar m/s.", a2, "m/s", "45 / 3,6 = 12,5 m/s."),
 inv("Een auto trekt eenparig op van 0 m/s naar 15 m/s in 5,0 s. Bereken de versnelling in m/s².", a3, "m/s²", "a = Δv / t = (15 − 0) / 5,0 = 3,0 m/s²."),
 inv("Een scooter rijdt 12 s lang met een constante snelheid van 9,0 m/s. Hoeveel meter legt de scooter in die tijd af?", a4, "m", "s = v × t = 9,0 × 12 = 108 m.", 0),
 op("Leg uit hoe een eenparige beweging en een eenparig versnelde beweging er in een (v,t)-diagram verschillend uitzien.",
    "Bij een eenparige beweging is de snelheid constant: de grafiek is een horizontale lijn. Bij een eenparig versnelde beweging is er sprake van een snelheid die gelijkmatig toeneemt: de grafiek is een schuin oplopende rechte lijn.",
    ["horizontaal/horizontale", "toeneemt/stijgt/oploopt"], "Constante snelheid geeft een horizontale lijn; gelijkmatig toenemende snelheid geeft een schuin oplopende rechte lijn."),
]
# mc-volgorde positions E: 2,0,3,1,1,3,0,2,3,1,2
write(69, 'E', '📈', E)

# ---------------- F (gemiddeld) ----------------
f1 = 5400 / 90; assert f1 == 60.0
f2 = (20 - 0) / 8.0; assert f2 == 2.5
f3 = 0.5 * 6.0 * 9.0; assert f3 == 27.0
f4 = 8.0 * 5.0 + 0.5 * 3.0 * 8.0; assert f4 == 52.0
assert 144 / 3.6 == 40 and abs(35 * 3.6 - 126) < 1e-9
F = [
 mc("In een (s,t)-diagram loopt de lijn van voorwerp A steiler dan die van voorwerp B. Wat betekent dat?", "A heeft een grotere snelheid dan B", ["A heeft een grotere versnelling dan B", "A heeft een grotere afstand afgelegd dan B", "A staat stil en B beweegt"], 1, "Steilheid in een (s,t)-diagram is snelheid: steiler betekent meer meters per seconde."),
 mc("Een trein rijdt met 144 km/h. Hoeveel is dat in m/s?", "40 m/s", ["518 m/s", "400 m/s", "25 m/s"], 3, "144 / 3,6 = 40 m/s."),
 mc("Een vliegtuig vliegt met 35 m/s. Hoeveel is dat in km/h?", "126 km/h", ["9,7 km/h", "35 km/h", "1260 km/h"], 0, "Van m/s naar km/h vermenigvuldig je met 3,6: 35 × 3,6 = 126 km/h."),
 mc("In een tabel hoort bij t = 0, 2, 4 en 6 s de snelheid v = 0, 3, 6 en 9 m/s. Welke beweging is dit?", "Een eenparig versnelde beweging", ["Een beweging met constante snelheid", "Een eenparig vertraagde beweging", "Een beweging met stilstand"], 2, "Elke 2 s komt er 3 m/s bij: de snelheid neemt gelijkmatig toe."),
 mc("Een (s,t)-tabel geeft bij t = 0, 1, 2 en 3 s de afstand s = 0, 2, 6 en 12 m. Wat kun je zeggen over de beweging?", "De afgelegde afstand per seconde wordt steeds groter, dus het voorwerp versnelt", ["Het voorwerp legt elke seconde evenveel afstand af", "De afgelegde afstand per seconde wordt steeds kleiner, dus het voorwerp remt", "Het voorwerp staat na 3 s stil"], 1, "Per seconde komt er 2, dan 4, dan 6 m bij: de snelheid neemt toe."),
 mc("Een voorwerp heeft een versnelling van −2 m/s². Wat betekent dat?", "De snelheid neemt elke seconde met 2 m/s af", ["De snelheid is 2 m/s en het voorwerp beweegt achteruit", "De snelheid neemt elke seconde met 2 m/s toe", "Het voorwerp heeft geen snelheid meer"], 3, "Een negatieve versnelling betekent dat Δv negatief is: het voorwerp vertraagt met 2 m/s per seconde."),
 mc("Op een stroboscopische foto liggen de beelden van een bewegende bal even ver uit elkaar. Wat zegt dat?", "De bal beweegt met constante snelheid", ["De bal versnelt eenparig", "De bal vertraagt eenparig", "De bal staat stil"], 0, "Gelijke afstanden in gelijke tijdstippen betekent constante snelheid."),
 mc("Een voorwerp versnelt vanuit stilstand tot v<sub>eind</sub> in t seconden. Hoe bereken je de afgelegde afstand?", "s = ½ × t × v<sub>eind</sub>", ["s = t × v<sub>eind</sub>", "s = v<sub>eind</sub> / t", "s = ½ × v<sub>eind</sub> / t"], 2, "De oppervlakte onder de lijn is een driehoek: ½ × basis × hoogte = ½ × t × v_eind."),
 mc("Een (v,t)-diagram toont van 0 tot 4 s een horizontale lijn op 6 m/s en van 4 tot 10 s een horizontale lijn op 0 m/s. Welke beschrijving klopt?", "Eerst constante snelheid, daarna stilstand", ["Eerst stilstand, daarna constante snelheid", "Eerst versnellen, daarna vertragen", "Eerst constante snelheid, daarna eenparig vertragen"], 1, "Op v = 6 m/s verandert de snelheid niet; op v = 0 m/s staat het voorwerp stil."),
 mc("Twee auto's rijden dezelfde ronde op hetzelfde circuit. Auto 1 heeft een kortere rondetijd dan auto 2. Wat geldt dan?", "Auto 1 heeft een grotere gemiddelde snelheid", ["Auto 1 heeft een kleinere gemiddelde snelheid", "Auto 1 heeft een grotere versnelling", "Beide auto's hebben dezelfde gemiddelde snelheid"], 3, "Bij gelijke afstand s geldt v = s / t: kleinere t geeft grotere v."),
 mc("Een voorwerp heeft een versnelling van 0 m/s². Wat weet je dan zeker?", "De snelheid verandert niet", ["Het voorwerp staat stil", "Het voorwerp beweegt met 0 km/h", "De afgelegde afstand is nul"], 2, "a = 0 betekent Δv = 0: de snelheid blijft gelijk. Dat kan een constante snelheid of stilstand zijn."),
 ww("In een (v,t)-diagram lees je de snelheid af op de verticale as.", True, "De (v,t)-notatie betekent: v op de verticale as en t op de horizontale as."),
 ww("Een kromme lijn in een (s,t)-diagram die steeds vlakker wordt hoort bij een eenparig vertraagde beweging.", True, "Een vlakkere helling betekent een afnemende snelheid."),
 ww("Een voorwerp met een grote versnelling heeft altijd ook een grote snelheid.", False, "Een auto die net optrekt heeft een grote versnelling maar nog een kleine snelheid."),
 ww("Een voorwerp dat eenparig remt tot stilstand heeft een gemiddelde snelheid die gelijk is aan zijn beginsnelheid.", False, "De snelheid daalt van v_begin naar 0, dus de gemiddelde snelheid is de helft van de beginsnelheid."),
 inv("Een circuit is 5400 m lang. Een coureur rijdt een ronde in 90 s. Bereken zijn gemiddelde snelheid in m/s.", f1, "m/s", "v = s / t = 5400 / 90 = 60 m/s."),
 inv("Een auto remt eenparig af van 20 m/s naar stilstand in 8,0 s. Bereken de grootte van de vertraging in m/s².", f2, "m/s²", "Δv = 0 − 20 = −20 m/s, dus |a| = 20 / 8,0 = 2,5 m/s²."),
 inv("Een voorwerp versnelt eenparig vanuit stilstand en bereikt na 6,0 s een snelheid van 9,0 m/s. Bereken de afgelegde afstand in meter.", f3, "m", "s = ½ × 6,0 × 9,0 = 27 m.", 0),
 inv("Een voorwerp rijdt 5,0 s met 8,0 m/s en remt daarna eenparig af tot stilstand in 3,0 s. Bereken de totale afgelegde afstand in meter.", f4, "m", "Eerst 8,0 × 5,0 = 40 m, daarna ½ × 3,0 × 8,0 = 12 m. Totaal 52 m.", 0),
 op("Een (v,t)-diagram toont eerst een stijgende rechte lijn, dan een horizontale lijn en daarna een dalende rechte lijn. Beschrijf de beweging in drie delen.",
    "In het eerste deel versnelt het voorwerp eenparig: de snelheid neemt gelijkmatig toe. In het tweede deel is de snelheid constant en beweegt het voorwerp eenparig. In het derde deel vertraagt het voorwerp eenparig: de snelheid neemt gelijkmatig af.",
    ["versnelt/versneld/toeneemt", "constant/gelijk", "vertraagt/vertraagd/afneemt"], "Stijgende lijn = versnellen, horizontale lijn = constante snelheid, dalende lijn = vertragen."),
]
write(70, 'F', '📉', F)

# ---------------- G (toetsniveau) ----------------
g1 = 2700 / 360; assert g1 == 7.5
g2 = 0.5 * 4.0 * 12 + 12 * 6.0; assert g2 == 96
g3 = 108 / 3.6; t3 = g3 / 1.5; g3s = 0.5 * t3 * g3; assert t3 == 20 and g3s == 300
g4 = (14 + 26) / 2 * 5.0; assert g4 == 100
assert (6 / 2, 12 / 3, 4 / 4) == (3, 4, 1) and 72 / 3.6 == 20 and 36 / 3.6 == 10 and (20 - 10) / 5 == 2
assert (10 - 2) / 4 == 2 and 3 * 4 == 12 and 0.5 * 6 * 12 == 36
G = [
 mc("Een voorwerp is op t = 0, 2, 5 en 9 s op s = 0, 6, 18 en 22 m. In welk tijdsinterval is de snelheid het grootst?", "Van 2 tot 5 s", ["Van 0 tot 2 s", "Van 5 tot 9 s", "In alle intervallen is de snelheid gelijk"], 3, "Snelheden: 6/2 = 3,0 m/s, 12/3 = 4,0 m/s en 4/4 = 1,0 m/s. Het tweede interval is het snelst."),
 mc("Bij dezelfde beweging (s = 0, 6, 18, 22 m op t = 0, 2, 5, 9 s) wil je de gemiddelde snelheid over het hele traject weten. Wat is die?", "2,4 m/s", ["2,7 m/s", "4,0 m/s", "1,0 m/s"], 1, "v_gem = totale afstand / totale tijd = 22 / 9 = 2,4 m/s. Het gemiddelde van de drie deelsnelheden (2,7 m/s) is niet hetzelfde."),
 mc("Een auto trekt eenparig op vanuit stilstand. Hoeveel keer zo groot wordt de afgelegde afstand als de optrektijd twee keer zo lang is (zelfde versnelling)?", "4 keer zo groot", ["2 keer zo groot", "8 keer zo groot", "Even groot"], 2, "De eindsnelheid wordt 2× zo groot én de tijd ook 2×, dus de oppervlakte onder de lijn wordt 2 × 2 = 4× zo groot."),
 mc("In een (v,t)-diagram loopt de lijn recht van 12 m/s naar 0 m/s in 6,0 s. Hoeveel meter legt het voorwerp in die tijd af?", "36 m", ["72 m", "18 m", "2,0 m"], 0, "De oppervlakte is een driehoek: ½ × 6,0 × 12 = 36 m. Zonder het ½-deel krijg je 72 m."),
 mc("Wat is de (v,t)-grafiek van een voorwerp dat stilstaat?", "Een horizontale lijn op v = 0 m/s", ["Een horizontale lijn boven de t-as", "Een stijgende rechte lijn", "Een rechte lijn die omlaag loopt"], 3, "Stilstand betekent v = 0 m/s voor elk tijdstip: de lijn ligt op de t-as."),
 mc("Een voorwerp heeft op t = 0 s een snelheid van 2,0 m/s en op t = 4,0 s een snelheid van 10 m/s, met een rechte lijn ertussen in het (v,t)-diagram. Hoe groot is de versnelling?", "2,0 m/s²", ["2,5 m/s²", "3,0 m/s²", "8,0 m/s²"], 2, "a = Δv / t = (10 − 2,0) / 4,0 = 2,0 m/s². Delen door de eindsnelheid (2,5) of rekenen vanaf 0 (3,0) klopt niet."),
 mc("Fietser A rijdt met 18 km/h en fietser B met 4,5 m/s. Wie rijdt het snelst?", "A, want 18 km/h is 5,0 m/s", ["B, want 4,5 kleiner is dan 18 maar B heeft een SI-eenheid", "B, want 4,5 m/s is meer dan 18 km/h", "Ze rijden even snel"], 1, "Reken eerst om naar dezelfde eenheid: 18 / 3,6 = 5,0 m/s, en dat is meer dan 4,5 m/s."),
 mc("In een (s,t)-diagram snijden de lijnen van twee fietsers elkaar op t = 20 s. Wat betekent dat?", "Op dat moment zijn ze op dezelfde plaats", ["Op dat moment hebben ze dezelfde snelheid", "Op dat moment hebben ze dezelfde versnelling", "Op dat moment staan beide fietsers stil"], 0, "Een snijpunt in een (s,t)-diagram betekent dezelfde s op dezelfde t: ze zijn op dezelfde plek. De hellingen (snelheden) kunnen verschillen."),
 mc("Welke eenheid heeft de oppervlakte onder een (v,t)-grafiek als v in m/s en t in s staat?", "Meter", ["Meter per seconde", "Meter per seconde kwadraat", "Seconde"], 3, "(m/s) × s = m: de oppervlakte is een afstand."),
 mc("Een auto start vanuit stilstand met een constante versnelling van 3,0 m/s². Wat is zijn snelheid na 4,0 s?", "12 m/s", ["7,0 m/s", "0,75 m/s", "48 m/s"], 2, "Elke seconde komt er 3,0 m/s bij: v = a × t = 3,0 × 4,0 = 12 m/s."),
 mc("Een voorwerp remt af van 72 km/h naar 36 km/h in 5,0 s. Wat is de grootte van de vertraging in m/s²?", "2,0 m/s²", ["7,2 m/s²", "3,6 m/s²", "10 m/s²"], 1, "72 km/h = 20 m/s en 36 km/h = 10 m/s. Δv = 10 m/s in 5,0 s geeft 2,0 m/s²."),
 ww("Het (v,t)-diagram van een eenparig versnelde beweging vanuit stilstand is een rechte lijn die door de oorsprong gaat.", True, "Op t = 0 is v = 0 en daarna neemt v gelijkmatig toe: een rechte lijn vanuit (0,0)."),
 ww("Als twee lijnen in een (s,t)-diagram elkaar snijden, hebben beide voorwerpen op dat moment dezelfde plaats.", True, "Dezelfde s op dezelfde t betekent dezelfde plek, ook al verschilt de snelheid."),
 ww("Een voorwerp met een dalende lijn in het (v,t)-diagram legt een negatieve afstand af.", False, "De snelheid neemt af, maar de oppervlakte onder de lijn en dus de afstand blijft positief."),
 ww("De gemiddelde snelheid van een heen- en terugreis met 60 km/h heen en 40 km/h terug is precies 50 km/h.", False, "De terugreis duurt langer dan de heenreis, dus de gemiddelde snelheid is lager dan 50 km/h (namelijk 48 km/h)."),
 inv("Een wielrenner rijdt 2,7 km in 6,0 minuten. Hoe groot is zijn gemiddelde snelheid in m/s?", g1, "m/s", "2,7 km = 2700 m en 6,0 min = 360 s, dus v = 2700 / 360 = 7,5 m/s."),
 inv("Een voorwerp versnelt in 4,0 s eenparig van 0 naar 12 m/s en rijdt daarna nog 6,0 s met 12 m/s. Bereken de totale afstand in meter.", g2, "m", "Eerst ½ × 4,0 × 12 = 24 m, daarna 12 × 6,0 = 72 m. Totaal 96 m.", 0),
 inv("Een trein rijdt 108 km/h en remt eenparig af met een vertraging van 1,5 m/s² tot stilstand. Bereken de remafstand in meter.", g3s, "m", "v = 30 m/s, remtijd = 30 / 1,5 = 20 s, afstand = ½ × 20 × 30 = 300 m.", 0),
 inv("Een auto versnelt eenparig in 5,0 s van 14 m/s naar 26 m/s. Bereken de afgelegde afstand in meter.", g4, "m", "v_gem = (14 + 26) / 2 = 20 m/s, dus s = 20 × 5,0 = 100 m.", 0),
 op("Fietser A en fietser B vertrekken tegelijk. A beweegt eenparig, B trekt eenparig versneld op. Beschrijf hoe hun (s,t)-grafieken verschillen.",
    "De grafiek van A is een rechte lijn met constante helling. De grafiek van B is een kromme lijn die steeds steiler omhoog loopt, omdat de snelheid van B toeneemt.",
    ["rechte lijn/recht", "kromme/gekromd/bocht"], "Constante snelheid geeft een rechte lijn, toenemende snelheid een steeds steilere kromme lijn."),
]
write(71, 'G', '🏁', G)

for nm, S in (('E', E), ('F', F), ('G', G)):
    print(nm, [v['antwoord'] for v in S if v['type'] == 'mc'])
