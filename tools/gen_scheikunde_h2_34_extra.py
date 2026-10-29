#!/usr/bin/env python3
"""Scheikunde HAVO 3 · H2 Bouwstenen van stoffen · extra proeftoetsen §2.3 Formuletaal (57, 58) en §2.4 Atoombouw (59, 60, 61).
Schrijft havo3/scheikunde/js/data/examen_h2_57.js ... examen_h2_61.js (ex-h3-sch-h2-57..61).
Bron: Chemie Overal HAVO 3, hoofdstuk 2 (OCR inbox/2026-2027/scheikunde). Atoommassa's staan in elke vraag zelf.
Notatie in de data: {H2SO4} -> H<sub>2</sub>SO<sub>4</sub>; [14,6]C -> <sup>14</sup><sub>6</sub>C.
Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random, re, subprocess, difflib

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'scheikunde', 'js', 'data')
SCRIPT = os.path.basename(__file__)


def tx(s):
    s = re.sub(r'\{([^}]*)\}', lambda m: re.sub(r'(?<=[A-Za-z)])(\d+)', r'<sub>\1</sub>', m.group(1)), s)
    return re.sub(r'\[(\d+),(\d+)\]', r'<sup>\1</sup><sub>\2</sub>', s)


def nl(x, d):
    return f"{x:.{d}f}".replace('.', ',')


def M(vraag, goed, fout, uitleg):
    return {"type": "mc", "vraag": tx(vraag), "_goed": tx(goed), "_fout": [tx(f) for f in fout], "uitleg": tx(uitleg)}


def W(vraag, antwoord, uitleg):
    assert uitleg.startswith("Waar.") if antwoord else uitleg.startswith("Niet waar.")
    return {"type": "waaronwaar", "vraag": tx(vraag), "antwoord": antwoord, "uitleg": tx(uitleg)}


def I(vraag, antwoord, uitleg):
    assert "____" in vraag
    return {"type": "invul", "vraag": tx(vraag), "antwoord": antwoord, "uitleg": tx(uitleg)}


def O(vraag, sleutels, min_, model, uitleg):
    assert 1 <= min_ <= len(sleutels)
    return {"type": "open", "vraag": tx(vraag), "sleutelwoorden": sleutels, "minTreffers": min_,
            "modelantwoord": tx(model), "uitleg": tx(uitleg)}


def plaats(vragen, rng):
    """Schud mc-opties tot: <=40% op een index, geen periode 2-4, <60% '+1'-stappen."""
    mcs = [v for v in vragen if v["type"] == "mc"]
    for _ in range(5000):
        pos = [rng.randrange(len(v["_fout"]) + 1) for v in mcs]
        if max(pos.count(i) for i in set(pos)) / len(pos) > 0.4:
            continue
        if len(pos) < 6:
            break
        if any(all(a == pos[i - p] for i, a in enumerate(pos) if i >= p) for p in (2, 3, 4)):
            continue
        n = max(len(v["_fout"]) + 1 for v in mcs)
        if sum(pos[i + 1] == (pos[i] + 1) % n for i in range(len(pos) - 1)) / (len(pos) - 1) >= 0.6:
            continue
        break
    else:
        raise SystemExit("geen geldige volgorde gevonden")
    for v, p in zip(mcs, pos):
        opties = list(v.pop("_fout"))
        rng.shuffle(opties)
        opties.insert(p, v.pop("_goed"))
        v["opties"], v["antwoord"] = opties, p
    return vragen


def langste_aandeel(vragen):
    mcs = [v for v in vragen if v["type"] == "mc"]
    n = sum(all(len(o) < len(v["opties"][v["antwoord"]]) for i, o in enumerate(v["opties"]) if i != v["antwoord"]) for v in mcs)
    return n, len(mcs)


# atoommassa's (u) zoals in de vragen vermeld
A = {"H": 1.008, "C": 12.01, "N": 14.01, "O": 16.00, "F": 19.00, "P": 30.97, "S": 32.07, "Cl": 35.45, "Br": 79.90}


def mm(**kw):
    return sum(A[k] * n for k, n in kw.items())


# ---------- berekende waarden ----------
sf6 = mm(S=1, F=6)                       # 146,07
br2 = mm(Br=2)                           # 159,80
br2s = mm(Br=2, S=1)                     # 191,87
so2 = mm(S=1, O=2)
h2o = mm(H=2, O=1)
pct_br_br2s = mm(Br=2) / br2s * 100      # 83,3
pct_s_so2 = A["S"] / so2 * 100           # 50,1
pct_h_h2o = 2 * A["H"] / h2o * 100       # 11,2
pct_s_sf6 = A["S"] / sf6 * 100           # 22,0
assert (nl(sf6, 2), nl(br2, 2), nl(br2s, 2)) == ("146,07", "159,80", "191,87")
assert (nl(pct_br_br2s, 1), nl(pct_s_so2, 1), nl(pct_h_h2o, 1), nl(pct_s_sf6, 1)) == ("83,3", "50,1", "11,2", "22,0")
assert nl(2 * h2o, 2) == "36,03"
gem1 = 0.25 * 6 + 0.75 * 8               # 7,5
gem2 = 0.20 * 50 + 0.80 * 52             # 51,6
gem3 = 0.70 * 10 + 0.30 * 11             # 10,3
assert (nl(gem1, 1), nl(gem2, 1), nl(gem3, 1)) == ("7,5", "51,6", "10,3")

# =====================================================================
# §2.3 Formuletaal
# =====================================================================
T57 = ("Formules lezen en schrijven", "🔤", [
    M("Cafeïne heeft de formule {C8H10N4O2}. Uit hoeveel atomen bestaat één cafeïnemolecuul?", "24",
      ["4", "18", "26"], "Tel de indexen op: 8 + 10 + 4 + 2 = 24 atomen. Het getal 4 is het aantal atoomsoorten (C, H, N en O)."),
    M("Hoe schrijf je zes moleculen zwaveldioxide op?", "6 {SO2}",
      ["{S6O12}", "{SO12}", "6 {S2O}"],
      "De coëfficiënt 6 staat vóór de formule en geeft het aantal moleculen aan. De formule {SO2} zelf verander je niet."),
    M("Wat geeft de 4 in 2 {CH4} aan?", "het aantal waterstofatomen in één molecuul methaan",
      ["het aantal methaanmoleculen", "het totale aantal atomen in de stof", "het aantal koolstofatomen"],
      "De 4 is een index: er zitten vier waterstofatomen in één molecuul. De coëfficiënt 2 geeft het aantal moleculen aan."),
    M("Hoeveel waterstofatomen zitten er in totaal in 2 moleculen alcohol, {C2H6O} (figuur 2.21)?", "12",
      ["6", "8", "18"], "Eén molecuul heeft 6 waterstofatomen, dus 2 moleculen hebben 2 × 6 = 12 waterstofatomen."),
    M("Duru zoekt de formule van fluor op in tabel 2.22. Wat vindt ze?", "{F2}",
      ["F", "Fl", "{F3}"], "Fluor is een van de zeven stoffen waarvan de moleculen uit twee keer dezelfde atoomsoort bestaan: {F2}."),
    M("Een zwaveldioxidemolecuul heeft evenveel atomen als een molecuul van een andere stof uit figuur 2.21. Welke stof is dat?", "koolstofdioxide",
      ["ammoniak", "methaan", "alcohol"],
      "{SO2} heeft 1 + 2 = 3 atomen, net als {CO2}. Ammoniak ({NH3}) heeft 4 atomen, methaan ({CH4}) 5 en alcohol ({C2H6O}) 9."),
    M("Je hebt 2 moleculen {SO2}. Hoeveel atomen zijn dat samen?", "6",
      ["3", "4", "5"], "Eén molecuul {SO2} heeft 1 + 2 = 3 atomen. Twee moleculen hebben 2 × 3 = 6 atomen."),
    M("Een molecuul bestaat uit één zwavelatoom en zes fluoratomen. Wat is de formule?", "{SF6}",
      ["{S6F}", "{S6F6}", "6 SF"], "Het zwavelatoom komt één keer voor (index 1 laat je weg) en fluor zes keer: {SF6}."),
    M("Een molecuul bestaat alleen uit koolstof-, waterstof- en zuurstofatomen: 20 atomen in totaal. Er zijn evenveel koolstof- als zuurstofatomen en twee keer zoveel waterstof- als koolstofatomen. Wat is de formule?",
      "{C5H10O5}", ["{C4H8O4}", "{C10H5O5}", "{C5H5O10}"],
      "Noem het aantal C-atomen n. Dan is O = n en H = 2n, samen 4n = 20, dus n = 5: {C5H10O5}."),
    M("Welke kleur heeft een zuurstofatoom in de modelvoorstelling van een watermolecuul (figuur 2.19)?", "rood",
      ["wit", "zwart", "blauw"], "In figuur 2.19 is waterstof wit en zuurstof rood."),
    W("Twee moleculen koolstofdioxide bevatten samen 2 koolstofatomen en 4 zuurstofatomen.", True, "Waar. Elk molecuul {CO2} heeft 1 koolstof- en 2 zuurstofatomen, dus 2 × 1 = 2 en 2 × 2 = 4."),
    W("Het getal 2 in 2 {CO2} geeft aan dat er twee koolstofatomen in één molecuul zitten.", False,
      "Niet waar. De 2 vóór de formule is de coëfficiënt: het aantal moleculen. Elk molecuul heeft maar één koolstofatoom."),
    W("Stikstof als stof heeft de formule {N2}: de moleculen bestaan uit twee stikstofatomen.", True,
      "Waar. Stikstof is een van de zeven stoffen uit tabel 2.22."),
    W("Methaan ({CH4}) hoort bij de zeven stoffen waarvan de moleculen uit twee keer dezelfde atoomsoort bestaan.", False,
      "Niet waar. Methaan heeft twee atoomsoorten (C en H) en is dus een verbinding. De zeven stoffen staan in tabel 2.22."),
    W("In de modelvoorstelling van 5 {H2O} (figuur 2.20) zie je in totaal 15 atomen.", True,
      "Waar. Elk watermolecuul heeft 3 atomen, dus 5 × 3 = 15."),
    I("Hoeveel atomen bevat 4 {NH3} in totaal? (Geef een getal.)  ____", "16|zestien",
      "Eén molecuul {NH3} heeft 1 + 3 = 4 atomen. Vier moleculen hebben 4 × 4 = 16 atomen."),
    I("Hoe heet de stof met de formule {N2}? ____", "stikstof",
      "{N2} is stikstof, een van de zeven stoffen uit tabel 2.22 (Br I N Cl H O F)."),
    I("Je hebt drie moleculen zwavelzuur, {H2SO4}. Hoeveel zuurstofatomen is dat samen? (Geef een getal.)  ____", "12|twaalf",
      "Eén molecuul zwavelzuur heeft 4 zuurstofatomen. Drie moleculen hebben 3 × 4 = 12 zuurstofatomen."),
    O("Een klasgenoot zegt dat 5 {H2O} (figuur 2.20) één groot molecuul met vijftien atomen is. Leg uit wat er niet klopt.",
      ["losse/aparte/afzonderlijke/vijf moleculen/5 moleculen", "coëfficiënt/coefficient", "3 atomen/drie atomen"], 2,
      "Het getal 5 vóór de formule is de coëfficiënt en geeft het aantal moleculen aan. Het zijn dus vijf losse watermoleculen met elk drie atomen (twee H en één O), samen vijftien atomen.",
      "De coëfficiënt geeft het aantal moleculen aan: het zijn vijf losse moleculen met elk drie atomen, geen één groot molecuul."),
    O("Noem twee voordelen van het gebruik van een formule in plaats van telkens een modelvoorstelling te tekenen.",
      ["sneller/snel/eenvoudiger/makkelijker/simpeler", "taalonafhankelijk/wereldwijd/in alle talen/overal ter wereld/internationaal"], 2,
      "Een formule is sneller en eenvoudiger op te schrijven dan een tekening, en ze is taalonafhankelijk: {H2O} betekent over de hele wereld hetzelfde.",
      "Het boek noemt: een formule is een snellere en eenvoudigere manier om stoffen weer te geven en ze is taalonafhankelijk."),
])

T58 = ("Namen en rekenen met massa's", "🧮", [
    M("Wat is de systematische naam van {P2O3}?", "difosfortrioxide",
      ["fosfortrioxide", "difosfordrioxide", "difosforoxide"],
      "Fosfor komt twee keer voor (di) en zuurstof drie keer (tri + oxide): difosfortrioxide."),
    M("Wat is de formule van difosfortrisulfide?", "{P2S3}",
      ["{P3S2}", "{PS3}", "{P2S}"], "'Difosfor' = 2 P-atomen, 'trisulfide' = 3 S-atomen: {P2S3}."),
    M("Wat is de systematische naam van {Cl2O}?", "dichloormono-oxide",
      ["chloormono-oxide", "dichloordioxide", "monochloormono-oxide"],
      "Chloor komt twee keer voor (di) en zuurstof één keer. Bij de tweede atoomsoort schrijf je 'mono' wel: dichloormono-oxide."),
    M("Wat is de formule van koolstoftetrafluoride?", "{CF4}",
      ["{C4F}", "{C4F4}", "{CF}"], "Koolstof komt één keer voor (geen voorvoegsel, geen index) en fluor vier keer (tetra): {CF4}."),
    M("Bereken de molecuulmassa van {SF6} (S = 32,07 u; F = 19,00 u).", "146,07 u",
      ["51,07 u", "114,00 u", "211,42 u"], "32,07 + 6 × 19,00 = 32,07 + 114,00 = 146,07 u."),
    M("Wat is de massa van een molecuul broom, {Br2} (Br = 79,90 u)?", "159,80 u",
      ["79,90 u", "158,80 u", "319,60 u"], "Een broommolecuul heeft twee bromatomen: 2 × 79,90 = 159,80 u."),
    M("Wat is het massapercentage zwavel in {SO2} (S = 32,07 u; O = 16,00 u; één decimaal)?", "50,1%",
      ["33,3%", "25,0%", "66,7%"], "Molecuulmassa {SO2} = 32,07 + 2 × 16,00 = 64,07 u. Zwavel: 32,07 / 64,07 × 100% = 50,1%."),
    M("Wat is het massapercentage waterstof in water, {H2O} (H = 1,008 u; O = 16,00 u; één decimaal)?", "11,2%",
      ["5,9%", "66,7%", "88,8%"], "Molecuulmassa = 2 × 1,008 + 16,00 = 18,016 u. Waterstof: 2,016 / 18,016 × 100% = 11,2%."),
    M("Waarom druk je de massa van atomen en moleculen uit in u en niet in gram?", "Omdat de massa van één atoom of molecuul veel kleiner is dan 1 gram of 1 mg",
      ["Omdat de massa van atomen elke dag verandert", "Omdat atomen geen massa hebben in gram", "Omdat u de officiële eenheid voor de massa van een stof in de pot is"],
      "De massa van één atoom of molecuul is zo klein dat gram en milligram onhandig zijn. 1,00 u komt overeen met 1,66·10<sup>-27</sup> kg."),
    M("Welke formule hoort bij fosforpentafluoride?", "{PF5}",
      ["{P5F}", "{P5F5}", "{PF}"], "Fosfor komt één keer voor (geen 'mono', geen index) en fluor vijf keer (penta): {PF5}."),
    W("Komt de tweede atoomsoort in de formule maar één keer voor, dan zet je 'mono' voor de naam van die atoomsoort.", True,
      "Waar. Daarom is {CO} koolstofmono-oxide. Bij de eerste atoomsoort laat je 'mono' weg."),
    W("De systematische naam van {CS2} is monokoolstofdisulfide.", False,
      "Niet waar. Koolstof is de eerste atoomsoort en komt één keer voor, dus geen 'mono': koolstofdisulfide."),
    W("Methaan en ammoniak zijn systematische namen.", False,
      "Niet waar. Het zijn triviale namen: alledaagse namen waaraan je niet kunt zien welke atoomsoorten in de moleculen zitten."),
    W("De molecuulmassa van een stof vind je door de atoommassa's van alle atomen in één molecuul op te tellen.", True,
      "Waar. Je vermenigvuldigt elke atoommassa met de index en telt de uitkomsten op."),
    W("Een molecuul {Br2} heeft dezelfde massa in u als één broomatoom.", False,
      "Niet waar. Een molecuul {Br2} bestaat uit twee bromatomen en is dus twee keer zo zwaar als één broomatoom."),
    I("Geef de systematische naam van {NF3}. ____", "stikstoftrifluoride",
      "Stikstof komt één keer voor (geen voorvoegsel) en fluor drie keer (tri): stikstoftrifluoride."),
    I("Bereken de totale massa van 2 moleculen water, 2 {H2O} (H = 1,008 u; O = 16,00 u). Geef alleen het getal, met twee decimalen.  ____", "36,03|36.03",
      "Eén molecuul {H2O} is 18,016 u. Twee moleculen: 2 × 18,016 = 36,03 u."),
    I("Bereken het massapercentage zwavel in {SF6} (S = 32,07 u; F = 19,00 u). Geef alleen het getal, met één decimaal.  ____", "22,0|22|22.0",
      "Molecuulmassa {SF6} = 146,07 u. Zwavel: 32,07 / 146,07 × 100% = 22,0%."),
    O("Bereken het massapercentage broom in {Br2S} (Br = 79,90 u; S = 32,07 u; één decimaal). Laat zien hoe je rekent.",
      ["191,87/191.87", "159,80/159,8/159.80", "83,3/83.3"], 2,
      "Molecuulmassa {Br2S} = 2 × 79,90 + 32,07 = 191,87 u. Massa broom = 2 × 79,90 = 159,80 u. Massapercentage = 159,80 / 191,87 × 100% = 83,3%.",
      "Eerst de molecuulmassa (191,87 u), dan de massa van broom (159,80 u), delen en × 100%: 83,3%."),
    O("Leg stap voor stap uit hoe je de systematische naam van {N2S3} afleidt uit de formule.",
      ["indexen/index", "voorvoegsel/voorvoegsels/di/tri", "achtervoegsel/-ide/sulfide"], 2,
      "Je kijkt naar de symbolen en indexen: N heeft index 2 (voorvoegsel di) en S heeft index 3 (voorvoegsel tri). De tweede atoomsoort krijgt het achtervoegsel -ide. De naam is distikstoftrisulfide.",
      "Met de indexen kies je de numerieke voorvoegsels (di, tri); de tweede atoomsoort krijgt een achtervoegsel (sulfide): distikstoftrisulfide."),
])

# =====================================================================
# §2.4 Atoombouw
# =====================================================================
T59 = ("Atoommodellen en hun geschiedenis", "⚛️", [
    M("In welk jaar presenteerde Joseph John Thomson zijn atoommodel?", "1904",
      ["1808", "1911", "1941"], "Thomson presenteerde zijn model in 1904, bijna 100 jaar na Dalton (1808) en een paar jaar vóór Rutherford (1911)."),
    M("Wat gebeurde er bij het experiment met het dunne gouden folie met bijna alle radioactieve deeltjes?", "Ze gingen recht door het folie heen",
      ["Ze kaatsten bijna allemaal terug", "Ze bleven in het folie steken", "Ze werden bijna allemaal afgebogen"],
      "Bijna alle deeltjes gingen recht door het gouden folie heen, zonder het aan te tasten."),
    M("Wat zei Dalton over de diameter van atomen?", "Die is uniek voor iedere atoomsoort",
      ["Die is voor alle atoomsoorten gelijk", "Die verandert als het atoom warm wordt", "Die is voor atomen van een stof niet te bepalen"],
      "Volgens Dalton hebben atomen van verschillende atoomsoorten een verschillende omvang; de diameter is uniek voor iedere atoomsoort."),
    M("Welk deeltje werd uit atomen gehaald bij de experimenten die niet bij het model van Dalton pasten?", "het elektron",
      ["het proton", "het neutron", "de atoomkern"],
      "Er werden negatief geladen deeltjes uit een atoom gehaald: de elektronen. Dat past niet bij een massieve, ondeelbare bol."),
    M("Waarom moeten er volgens Rutherford ook positieve deeltjes in een atoom zitten?", "Omdat atomen elektrisch neutraal zijn",
      ["Omdat elektronen elkaar aantrekken", "Omdat de atoomkern anders ongeladen is", "Omdat atomen bijna geen lege ruimte hebben"],
      "Elektronen zijn negatief. Atomen blijken elektrisch neutraal, dus er moeten ook positieve deeltjes zijn: de protonen."),
    M("Wat is de lading van een proton ten opzichte van die van een elektron?", "even groot, maar tegengesteld",
      ["twee keer zo groot en negatief", "even groot en ook negatief", "nul, het proton is ongeladen"],
      "Een proton heeft lading 1+ en een elektron 1–: even groot, maar tegengesteld."),
    M("Welke deeltjes vormen samen de atoomkern?", "protonen en neutronen",
      ["protonen en elektronen", "neutronen en elektronen", "alleen protonen"],
      "In de atoomkern zitten de protonen (1+) en de neutronen (0). De elektronen zitten in een wolk rondom de kern."),
    M("Welke combinatie van atoommodel en kenmerk klopt?", "Thomson – elektronen zitten verdeeld in het atoom",
      ["Dalton – het atoom heeft een atoomkern", "Rutherford – het atoom is een massieve bol", "Thomson – alle protonen zitten in de kern"],
      "Thomson vergeleek zijn model met een krentenbol: de elektronen zitten als krenten in het deeg. De kern past bij Rutherford; de massieve bol bij Dalton."),
    M("Wat uit het werk van Dalton wordt tegenwoordig nog steeds gebruikt?", "de kleuren voor verschillende atoomsoorten in modelvoorstellingen",
      ["het idee dat atomen niet deelbaar zijn", "het idee dat atomen massieve bollen zijn", "het idee dat alle atomen even groot zijn"],
      "Dalton gebruikte kleuren om atoomsoorten weer te geven; die worden nog steeds gebruikt in modelvoorstellingen van moleculen (tabel 2.12)."),
    M("Hoeveel jaar zat er ongeveer tussen het model van Thomson (1904) en dat van Rutherford (1911)?", "7 jaar",
      ["17 jaar", "70 jaar", "107 jaar"], "1911 – 1904 = 7 jaar: 'een paar jaar na Thomson'."),
    W("Volgens het atoommodel van Dalton bestaan atomen uit nog kleinere deeltjes.", False,
      "Niet waar. Volgens Dalton zijn atomen niet op te delen in kleinere deeltjes; het zijn de kleinst mogelijke bouwstenen."),
    W("Bij het experiment met het gouden folie gingen bijna alle deeltjes recht door het folie heen.", True,
      "Waar. Daardoor kon het model van Thomson niet kloppen; het atoom bestaat grotendeels uit lege ruimte."),
    W("Volgens het model van Rutherford is de atoomkern negatief geladen.", False,
      "Niet waar. In de kern zitten de positieve protonen en de ongeladen neutronen, dus de kern is positief geladen."),
    W("Neutronen zijn ongeladen deeltjes die in de atoomkern zitten.", True,
      "Waar. Het neutron heeft lading 0 en komt in de atoomkern voor."),
    W("Het atoommodel van Rutherford lijkt sterk op het model dat nu nog steeds in de scheikunde wordt gebruikt.", True,
      "Waar. Met de ontdekking van het neutron was het model van Rutherford compleet."),
    I("Hoe noemden de oude Grieken de kleinste ondeelbare delen waar stoffen uit bestaan? ____", "atomos",
      "De oude Grieken noemden ze 'atomos', wat 'ondeelbaar' betekent."),
    I("Het deeltje in de atoomkern met een lading van 1+ heet het ____.", "proton|protonen",
      "Het proton heeft een lading van 1+ en zit in de atoomkern; symbool p."),
    I("Uit hoeveel soorten bouwstenen bestaat een atoom volgens het model van Rutherford? (Geef een getal.)  ____", "3|drie",
      "Protonen, neutronen en elektronen: drie soorten bouwstenen."),
    O("Leg uit hoe het experiment met het gouden folie liet zien dat het atoommodel van Thomson niet kon kloppen.",
      ["recht door/doorheen/gingen door/dwars door", "ondoordringbar/dichte laag/geen lege ruimte", "lege ruimte/leeg"], 2,
      "Bijna alle deeltjes gingen recht door het folie. Als atomen zoals bij Thomson massief waren, zouden de goudatomen een ondoordringbare laag vormen. Het atoom moet dus grotendeels uit lege ruimte bestaan.",
      "Doordat bijna alle deeltjes door het folie gingen, kan een atoom geen dichte, ondoordringbare bol zijn: het bestaat voor meer dan 99% uit lege ruimte."),
    O("Leg uit waarom atomen volgens het model van Rutherford elektrisch neutraal zijn.",
      ["protonen/proton", "elektronen/elektron", "evenveel/gelijk aantal/even veel/even groot/opheffen/compenseren"], 2,
      "Een atoom heeft evenveel protonen (1+) als elektronen (1–). De positieve en negatieve ladingen zijn even groot en heffen elkaar op.",
      "Het aantal protonen is gelijk aan het aantal elektronen en de ladingen zijn even groot maar tegengesteld, dus het atoom is neutraal."),
])

T60 = ("Atoomnummer, massagetal en isotopen", "🔢", [
    M("Aan welke twee gegevens kun je het aantal neutronen in een atoom bepalen?", "het massagetal en het atoomnummer",
      ["het atoomnummer en de lading", "het massagetal en het aantal elektronen", "de relatieve atoommassa en het atoomnummer"],
      "Neutronen = massagetal – atoomnummer (aantal protonen)."),
    M("Hoeveel neutronen heeft een atoom K-39 (atoomnummer 19)?", "20",
      ["19", "39", "58"], "Neutronen = massagetal – protonen = 39 – 19 = 20."),
    M("Een atoom heeft massagetal 35 en 18 neutronen. Hoeveel protonen heeft het?", "17",
      ["18", "35", "53"], "Protonen = massagetal – neutronen = 35 – 18 = 17."),
    M("Welke deeltjes tellen mee voor het massagetal van een atoom?", "protonen en neutronen",
      ["protonen en elektronen", "neutronen en elektronen", "alleen de elektronen"],
      "Het massagetal is de som van het aantal protonen en neutronen in de atoomkern."),
    M("Hoeveel elektronen heeft een neutraal atoom C-14 (tabel 2.31)?", "6",
      ["8", "14", "20"], "Koolstof heeft atoomnummer 6, dus 6 protonen en in een neutraal atoom ook 6 elektronen. De 14 is het massagetal."),
    M("Welke notatie met massagetal linksboven en atoomnummer linksonder hoort bij Cl-35 (atoomnummer 17)?", "[35,17]Cl",
      ["[17,35]Cl", "[35,18]Cl", "[18,17]Cl"], "Het massagetal (35) staat linksboven en het atoomnummer (17) linksonder het symbool: [35,17]Cl."),
    M("Wat is hetzelfde bij alle isotopen van één atoomsoort?", "het aantal protonen",
      ["het aantal neutronen", "het massagetal", "het aantal deeltjes in de kern"],
      "Isotopen hebben hetzelfde aantal protonen (atoomnummer) maar een verschillend aantal neutronen en dus een verschillend massagetal."),
    M("Hoeveel deeltjes zitten er in de atoomkern van [14,6]C?", "14",
      ["6", "8", "20"], "De kern bevat 6 protonen en 8 neutronen: samen 14 deeltjes, gelijk aan het massagetal."),
    M("Waarom hebben isotopen van één atoomsoort een verschillende massa?", "Ze hebben een verschillend aantal neutronen en elk neutron weegt ongeveer 1 u",
      ["Ze hebben een verschillend aantal protonen", "Ze hebben een verschillend aantal elektronen", "Ze hebben een verschillend atoomnummer"],
      "Isotopen hebben evenveel protonen maar een ander aantal neutronen. Omdat een neutron ongeveer 1 u weegt, verschilt de massa."),
    M("Een atoom heeft atoomnummer 26. Welke bewering klopt?", "Elk atoom met 26 protonen is een ijzeratoom",
      ["Een ijzeratoom heeft altijd 26 neutronen", "Een ijzeratoom heeft altijd massagetal 26", "Een ijzeratoom heeft 26 verschillende isotopen"],
      "Het aantal protonen bepaalt de atoomsoort. Het aantal neutronen kan verschillen, dus het massagetal niet altijd hetzelfde."),
    W("Isotopen van één atoomsoort hebben een gelijk aantal neutronen.", False,
      "Niet waar. Isotopen hebben juist een verschillend aantal neutronen, maar hetzelfde aantal protonen."),
    W("In de atoomkern van een koolstofatoom zitten altijd 6 protonen.", True,
      "Waar. Het aantal protonen is gelijk aan het atoomnummer en dat is voor koolstof altijd 6; alleen het aantal neutronen kan verschillen."),
    W("C-13 en C-14 hebben een verschillend atoomnummer.", False,
      "Niet waar. Beide zijn koolstof en hebben 6 protonen; ze verschillen alleen in het aantal neutronen."),
    W("De massa van een elektron is afgerond 0 u.", True,
      "Waar. Protonen en neutronen hebben elk een massa van nagenoeg 1 u, elektronen van afgerond 0 u."),
    W("Een neutraal atoom heeft altijd evenveel protonen als neutronen.", False,
      "Niet waar. Evenveel protonen als elektronen, maar het aantal neutronen kan afwijken, bijvoorbeeld bij [14,6]C (6 protonen, 8 neutronen)."),
    I("Hoeveel neutronen heeft een atoom Na-23 (atoomnummer 11)? (Geef een getal.)  ____", "12|twaalf",
      "Neutronen = massagetal – atoomnummer = 23 – 11 = 12."),
    I("Een atoom heeft atoomnummer 29 en 34 neutronen. Wat is het massagetal? (Geef een getal.)  ____", "63",
      "Massagetal = protonen + neutronen = 29 + 34 = 63."),
    I("Schrijf de isotoop met atoomnummer 17 en 20 neutronen in de notatie symbool-massagetal (bijvoorbeeld C-14).  ____", "Cl-37|Cl37",
      "Massagetal = 17 + 20 = 37; het symbool bij atoomnummer 17 is Cl: Cl-37."),
    O("Een deeltje heeft 16 protonen, 16 neutronen en 18 elektronen. Bepaal het massagetal en de lading van dit deeltje en leg uit hoe je dat doet.",
      ["32", "2–/2-/2 negatief/tweevoudig negatief/2 min", "optellen/som/bij elkaar"], 2,
      "Je telt de protonen en neutronen bij elkaar op: 16 + 16 = 32. Lading = 16 positieve lading – 18 negatieve lading = 2–.",
      "Het massagetal is 32 (16 + 16). Met 16 protonen en 18 elektronen is het deeltje 2– geladen."),
    O("Leg uit waarom de massa van een atoom vrijwel helemaal in de atoomkern zit.",
      ["protonen/proton", "neutronen/neutron", "0 u/geen massa/verwaarloosbaar/bijna niets/nagenoeg niets/afgerond 0"], 2,
      "Protonen en neutronen hebben elk een massa van ongeveer 1 u en zitten in de atoomkern. Elektronen hebben een massa van afgerond 0 u, dus ze voegen vrijwel niets toe.",
      "De kern bevat de protonen en neutronen (elk ongeveer 1 u); de elektronen wegen afgerond 0 u."),
])

T61 = ("Relatieve atoommassa en eindniveau", "🧲", [
    M("Een atoomsoort komt in de natuur voor als twee isotopen: 25% heeft een massa van 6 u en 75% heeft een massa van 8 u. Wat is de relatieve atoommassa?", "7,5 u",
      ["7,0 u", "6,5 u", "7,8 u"], "Gewogen gemiddelde: 0,25 × 6 + 0,75 × 8 = 1,5 + 6,0 = 7,5 u."),
    M("Wat gebeurt er met het atoomnummer als je een neutron aan de atoomkern toevoegt?", "Het atoomnummer blijft gelijk",
      ["Het atoomnummer wordt 1 groter", "Het atoomnummer wordt 1 kleiner", "Het atoomnummer wordt twee keer zo groot"],
      "Het atoomnummer is het aantal protonen. Een extra neutron verandert alleen het massagetal: je krijgt een andere isotoop."),
    M("Waarom is het atoomnummer uniek voor iedere atoomsoort?", "Geen twee atoomsoorten hebben hetzelfde aantal protonen",
      ["Geen twee atoomsoorten hebben hetzelfde aantal neutronen", "Elk atoom heeft een ander aantal elektronen", "Isotopen hebben allemaal een ander atoomnummer"],
      "Elke atoomsoort heeft een uniek aantal protonen in de kern, en dat aantal is het atoomnummer."),
    M("Hoeveel verschillende isotopen van chloor komen volgens het boek in de natuur voor?", "2",
      ["1", "3", "4"], "Cl-35 en Cl-37: twee isotopen."),
    M("Hoeveel protonen, neutronen en elektronen heeft een neutraal atoom [31,15]P?", "15 protonen, 16 neutronen, 15 elektronen",
      ["15 protonen, 31 neutronen, 15 elektronen", "16 protonen, 15 neutronen, 16 elektronen", "15 protonen, 16 neutronen, 16 elektronen"],
      "Protonen = atoomnummer = 15. Neutronen = 31 – 15 = 16. In een neutraal atoom zijn er evenveel elektronen als protonen: 15."),
    M("Wat is de massa van een neutraal atoom met 7 protonen, 7 neutronen en 7 elektronen ongeveer in u?", "14 u",
      ["7 u", "21 u", "28 u"], "Protonen en neutronen tellen elk 1 u, elektronen afgerond 0 u: 7 + 7 = 14 u."),
    M("Welke bewering over Cl-35 en Cl-37 klopt?", "Ze hebben hetzelfde atoomnummer maar een verschillend massagetal",
      ["Ze hebben een verschillend atoomnummer en hetzelfde massagetal", "Ze hebben hetzelfde aantal neutronen maar een verschillend aantal protonen", "Ze zijn twee verschillende atoomsoorten"],
      "Beide zijn chloor met 17 protonen. Cl-37 heeft twee neutronen meer dan Cl-35."),
    M("Welk van de volgende getallen kan nooit een massagetal zijn?", "35,45",
      ["35", "37", "14"], "Een massagetal is altijd een geheel getal. 35,45 u is de relatieve atoommassa van chloor."),
    M("Een neutraal fluoratoom neemt één elektron op. Wat verandert er?", "Het deeltje wordt negatief geladen (1–); protonen en neutronen blijven gelijk",
      ["Het atoomnummer wordt 1 groter", "Het massagetal wordt 1 groter", "Het deeltje wordt positief geladen"],
      "Een extra elektron geeft een lading van 1–. Het aantal protonen (atoomnummer) en neutronen, en dus het massagetal, blijft gelijk."),
    M("Hoe komt de relatieve atoommassa van chloor (35,45 u) volgens het boek ongeveer tot stand?", "0,75 × 35 + 0,25 × 37",
      ["(35 + 37) / 2", "0,25 × 35 + 0,75 × 37", "35 + 37"],
      "Ongeveer 75% van de chlooratomen is Cl-35 en ongeveer 25% Cl-37: een gewogen gemiddelde."),
    W("In een natuurlijk monster chloor komen meer Cl-35 dan Cl-37 atomen voor.", True,
      "Waar. Ongeveer 75% is Cl-35 en ongeveer 25% is Cl-37; daarom ligt 35,45 u dicht bij 35 u."),
    W("Een Cl-37 atoom heeft een groter atoomnummer dan een Cl-35 atoom.", False,
      "Niet waar. Beide hebben atoomnummer 17; Cl-37 heeft alleen twee neutronen meer."),
    W("Het aantal protonen van een atoom kun je aflezen in het periodiek systeem.", True,
      "Waar. Het aantal protonen is gelijk aan het atoomnummer."),
    W("De relatieve atoommassa van een atoomsoort ligt altijd precies in het midden tussen de massa's van de isotopen.", False,
      "Niet waar. Het is een gewogen gemiddelde: de isotoop die vaker voorkomt telt zwaarder mee."),
    W("Als een atoom een elektron opneemt, verandert het atoomnummer.", False,
      "Niet waar. Het atoomnummer is het aantal protonen en dat verandert niet; alleen de lading verandert."),
    I("Een atoomsoort bestaat voor 20% uit een isotoop van 50 u en voor 80% uit een isotoop van 52 u. Wat is de relatieve atoommassa? Geef alleen het getal, met één decimaal.  ____", "51,6|51.6",
      "Gewogen gemiddelde: 0,20 × 50 + 0,80 × 52 = 10,0 + 41,6 = 51,6 u."),
    I("Hoe heet het deeltje met een massa van afgerond 0 u en een lading van 1–? ____", "elektron|elektronen",
      "Het elektron heeft een lading van 1– en een massa van afgerond 0 u; symbool e<sup>–</sup>."),
    I("Hoeveel deeltjes (protonen, neutronen en elektronen samen) heeft een neutraal atoom [12,6]C in totaal? (Geef een getal.)  ____", "18|achttien",
      "6 protonen + 6 neutronen (12 – 6) + 6 elektronen = 18 deeltjes."),
    O("Bereken de relatieve atoommassa van een atoomsoort die voor 70% uit een isotoop met een massa van 10 u bestaat en voor 30% uit een isotoop met een massa van 11 u. Laat zien hoe je rekent.",
      ["7,0/7.0", "3,3/3.3", "10,3/10.3"], 2,
      "Gewogen gemiddelde: 0,70 × 10 + 0,30 × 11 = 7,0 + 3,3 = 10,3 u.",
      "Vermenigvuldig elke isotoopmassa met het aandeel en tel op: 7,0 + 3,3 = 10,3 u."),
    O("Leg uit hoe je in het vakje van een atoomsoort in het periodiek systeem het atoomnummer en de relatieve atoommassa van elkaar onderscheidt en wat elk getal betekent.",
      ["linksonder/onder het symbool", "linksboven/boven het symbool/boven", "protonen/proton", "gewogen gemiddelde/gemiddelde/isotopen"], 3,
      "Het atoomnummer staat linksonder het symbool en geeft het aantal protonen aan. De relatieve atoommassa staat linksboven in het vakje en is een gewogen gemiddelde van de massa's van de isotopen.",
      "Atoomnummer = aantal protonen (onder het symbool); relatieve atoommassa = gewogen gemiddelde van de isotopen (boven het symbool)."),
])

# nr: (paragraaf, deeltitel-tuple, vak-label)
EXAMENS = {57: ("2.3", T57), 58: ("2.3", T58), 59: ("2.4", T59), 60: ("2.4", T60), 61: ("2.4", T61)}
PARA_NAAM = {"2.3": "Formuletaal", "2.4": "Atoombouw"}


def sig(t):
    """woordverzameling; te gelijk = (bijna) dezelfde woorden. Andere stof/getal in dezelfde sjabloonvraag telt als andere vraag."""
    return set(re.findall(r'[^\W_]+', t))


def norm(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).lower().strip()


def bestaande():
    js = ("const fs=require('fs'),p=process.argv[1],o=[];global.DURU={registerExamen:e=>o.push(e),register:e=>o.push(e)};"
          "for(const f of fs.readdirSync(p).filter(f=>/^(examen|h2_)/.test(f)&&!/^examen_h2_(5[7-9]|6[01])\\.js$/.test(f))){"
          "try{eval(fs.readFileSync(p+'/'+f,'utf8'))}catch(e){}}"
          "console.log(JSON.stringify(o.flatMap(e=>(e.vragen||[]).map(v=>[e.id,v.vraag]))))")
    return json.loads(subprocess.check_output(['node', '-e', js, ROOT]))


def main():
    rng = random.Random(SCRIPT)
    oud = [(i, norm(t)) for i, t in bestaande()]
    nieuw = []
    for nr, (para, (deel, icoon, vr)) in EXAMENS.items():
        assert [v["type"] for v in vr].count("mc") == 10 and [v["type"] for v in vr].count("waaronwaar") == 5 \
            and [v["type"] for v in vr].count("invul") == 3 and [v["type"] for v in vr].count("open") == 2 and len(vr) == 20, nr
        assert sum(1 for v in vr if v["type"] == "waaronwaar" and not v["antwoord"]) >= 2, nr
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        for v in vr:
            t = norm(v["vraag"])
            for i, o in oud + nieuw:
                r = difflib.SequenceMatcher(None, t, o).ratio()
                assert r < 0.9 or len(sig(t) ^ sig(o)) > 1, f"te gelijk ({r:.2f}) examen {nr} vs {i}: {v['vraag'][:80]}"
                if r >= 0.8:  # sjabloonvraag ("Wat is de systematische naam van ...?") met andere stof: handmatig bekijken
                    print(f"  let op ({r:.2f}) examen {nr} vs {i}: {t[:70]}  <>  {o[:70]}")
            nieuw.append((f"nieuw-{nr}", t))
            if v["type"] == "invul":
                a = [x.strip().lower() for x in v["antwoord"].split("|")]
                assert not any(x and x in t for x in a if len(x) > 2), f"antwoord in vraag: {v['vraag']}"
        titel = f"Toets {nr} — §{para} {deel}"
        ex = {"id": f"ex-h3-sch-h2-{nr}", "hoofdstuk": 2, "paragraaf": para, "titel": titel,
              "vak": f"Scheikunde · HAVO 3 (H2 — §{para})", "icoon": icoon, "duurMin": 30, "vragen": vr}
        kop = (f"/* =========================================================\n"
               f"   Duru's Scheikunde (HAVO 3) — {titel}\n"
               f"   Hoofdstuk 2 (Chemie Overal), §{para} {PARA_NAAM[para]}. 20 vragen · 30 minuten. Alleen wat in het boek staat.\n"
               f"   gegenereerd door tools/{SCRIPT}\n"
               f"   ========================================================= */\n")
        with open(os.path.join(ROOT, f"examen_h2_{nr}.js"), 'w', encoding='utf-8') as f:
            f.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_h2_{nr}.js  {titel}  (juiste=langste {n}/{tot})")


if __name__ == '__main__':
    main()
