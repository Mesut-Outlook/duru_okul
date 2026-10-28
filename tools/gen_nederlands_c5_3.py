#!/usr/bin/env python3
"""Nederlands HAVO 3 · Cursus 5 §3 Samentrekking (boek p. 210–211).

Schrijft havo3/nederlands/js/data/c5_3.js (onderwerp, 8 oefenvragen) en
examen_37.js … examen_43.js (ex-h3-nederlands-37…43, 20 vragen per toets).
Bij mc staat het juiste antwoord in de bron EERST; de generator schudt de opties
(seed 'c5_3') tot de verdeling per bestand gate-proof is (kural 3 en 16).
Let op: een al gemaakte toets-id nooit opnieuw genereren met andere inhoud.
"""
import json, os, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "havo3", "nederlands", "js", "data")
rng = random.Random("c5_3")


def mc(vraag, goed, fout, uitleg, **kw):
    return dict(type="mc", vraag=vraag, opties=[goed] + fout, uitleg=uitleg, **kw)


def wo(vraag, antwoord, uitleg, **kw):
    assert uitleg.startswith("Waar." if antwoord else "Niet waar."), vraag
    return dict(type="waaronwaar", vraag=vraag, antwoord=antwoord, uitleg=uitleg, **kw)


def inv(vraag, antwoord, uitleg):
    return dict(type="invul", vraag=vraag, antwoord=antwoord, uitleg=uitleg)


def op(vraag, sleutels, minimum, model, uitleg):
    return dict(type="open", vraag=vraag, sleutelwoorden=sleutels, minTreffers=minimum,
                modelantwoord=model, uitleg=uitleg)


def ivo(vraag, antwoord, uitleg, **kw):
    return dict(type="invoer", vraag=vraag, antwoord=antwoord, uitleg=uitleg, **kw)


NIV = ["woordniveau", "woordgroepsniveau", "zinsniveau"]


def schud(vragen):
    """Schud mc-opties; herhaal tot geen index > 40% en geen periodiek patroon."""
    mcs = [v for v in vragen if v["type"] == "mc"]
    for _ in range(500):
        idx = []
        for v in mcs:
            goed = v["_goed"] if "_goed" in v else v["opties"][0]
            v["_goed"] = goed
            opts = list(v["_orig"] if "_orig" in v else v["opties"])
            v["_orig"] = opts
            rng.shuffle(opts)
            v["opties"] = opts
            v["antwoord"] = opts.index(goed)
            idx.append(v["antwoord"])
        n = len(idx)
        if n < 2:
            break
        if max(idx.count(i) for i in set(idx)) > 0.4 * n and n >= 4:
            continue
        stappen = sum(1 for a, b in zip(idx, idx[1:]) if b == a + 1)
        if stappen >= 0.6 * (n - 1):
            continue
        if any(all(idx[i] == idx[i + p] for i in range(n - p)) for p in (2, 3, 4) if n >= 2 * p):
            continue
        break
    for v in mcs:
        v.pop("_goed", None)
        v.pop("_orig", None)
    return vragen


def uniek_langst(v):
    lens = [len(o) for o in v["opties"]]
    goed = lens[v["antwoord"]]
    return goed == max(lens) and lens.count(goed) == 1


# ---------------------------------------------------------------- theorie
THEORIE = """
<h3>1. Wat is samentrekking?</h3>
<p>Soms komt een woorddeel, een woord of een zinsdeel twee keer voor in een woordgroep of zin. Je kunt het dan één keer noemen en de tweede keer <b>weglaten</b>. Dat heet <b>samentrekking</b>. Door identieke (delen van) woorden of zinsdelen weg te laten, formuleer je <b>korter</b>, zonder dat de betekenis verandert.</p>
<div class="formule-box"><b>Samentrekking</b> = een woorddeel, woord of zinsdeel dat op een andere plek in de woordgroep of zin al voorkomt, wordt weggelaten.<br><i>schoenendozen en schoenenkasten</i> → <i>schoenendozen en <b>-kasten</b></i></div>

<h3>2. Voorwaarts of achterwaarts?</h3>
<ul>
  <li><b>Voorwaartse samentrekking</b>: het gemeenschappelijke deel wordt in het <b>eerste</b> deel genoemd en <b>verderop</b> weggelaten: <i>fietsbellen en -lampjes</i>, <i>Mila eet een appel en Sem een peer</i>.</li>
  <li><b>Achterwaartse samentrekking</b>: het gemeenschappelijke deel wordt in het <b>laatste</b> deel genoemd en <b>daarvóór</b> weggelaten: <i>zomer- en wintertijd</i>, <i>rode en groene appels</i>.</li>
</ul>

<h3>3. Drie niveaus</h3>
<table class="nask">
  <tr><th>Niveau</th><th>Wat valt weg?</th><th>Streepje?</th><th>Voorbeeld</th></tr>
  <tr><td><b>Woordniveau</b></td><td>een deel van een samengesteld woord</td><td><b>ja</b>, op de plek van het weggelaten woorddeel</td><td><i>regenjas en -laarzen</i> (voorwaarts)<br><i>in- en uitgang</i> (achterwaarts)</td></tr>
  <tr><td><b>Woordgroepsniveau</b></td><td>een of meer hele woorden binnen een woordgroep</td><td>nee</td><td><i>verse en gedroogde kruiden</i><br><i>zowel dikke als dunne boeken</i></td></tr>
  <tr><td><b>Zinsniveau</b></td><td>een of meer zinsdelen (ow, pv, rest van het gezegde, lv, mv, bwb) die twee keer voorkomen</td><td>nee</td><td><i>Lotte leest een strip en Bram (leest) een roman.</i><br><i>Ik was (de borden) en jij droogt de borden.</i></td></tr>
</table>

<div class="voorbeeld"><div class="vb-kop">Voorbeeld: zinsniveau</div>
<div class="stap"><i>Na de training heeft Daan zijn schoenen schoongemaakt en zijn tas ingepakt.</i></div>
<div class="stap">In het tweede deel zijn weggelaten: de bwb <i>na de training</i>, de pv <i>heeft</i> en het ow <i>Daan</i>. Ze staan in het eerste deel → <b>voorwaartse</b> samentrekking op <b>zinsniveau</b>. Geen streepje!</div></div>

<div class="info-box let-op"><h4>Let op</h4>
<ul>
  <li>Een streepje schrijf je <b>alleen op woordniveau</b>. Dus <i>lange en korte broeken</i>, niet <i>lange- en korte broeken</i>.</li>
  <li>Je mag alleen weglaten wat <b>precies hetzelfde</b> is: <i>Mijn opa heeft een hond en mijn oma (heeft) een kat</i> is goed.</li>
  <li>Niet elke <i>en</i> is een samentrekking: in <i>Ik was de borden en jij droogt ze af</i> is niets weggelaten.</li>
</ul></div>

<h3>4. Ongelijkwaardige samentrekking</h3>
<p>In <i>zowel bruine- als ijsberen</i> is <i>beren</i> na <i>bruine</i> een los woord (bruine beren), maar na <i>ijs</i> een deel van een samenstelling (ijsberen). Ook in <i>de overstap van de basis- naar de middelbare school</i> zijn de delen niet gelijkwaardig: <i>basisschool</i> is één woord, <i>middelbare school</i> zijn twee woorden. Zo'n <b>ongelijkwaardige samentrekking</b> werd vroeger afgekeurd, maar wordt <b>tegenwoordig geaccepteerd</b>.</p>
<div class="info-box tip"><h4>Tip: zo vind je de samentrekking</h4>
<p>Vul het weggelaten deel weer in. Lees je dan een volledige, logische woordgroep of zin? Kijk waar het gemeenschappelijke deel wél staat: eerst genoemd → voorwaarts; laatst genoemd → achterwaarts.</p></div>
"""

ONDERWERP_VRAGEN = [
    mc("Wat bedoelen we met samentrekking?",
       "Je laat een deel weg dat elders al genoemd wordt",
       ["Je voegt twee zinnen samen met een komma ertussen",
        "Je herhaalt een woord om het extra te benadrukken",
        "Je vervangt een zelfstandig naamwoord door een voornaamwoord"],
       "Bij samentrekking laat je een identiek woorddeel, woord of zinsdeel weg dat op een andere plek in de woordgroep of zin al voorkomt.",
       niveau=1, hint="Denk aan 'korter formuleren'."),
    wo("In 'regen- en zonnedagen' is het woorddeel 'regen' weggelaten.", False,
       "Niet waar. Het weggelaten woorddeel is 'dagen': regendagen en zonnedagen.",
       niveau=1, hint="Vul het streepje weer aan."),
    mc("Is 'appeltaart en -gebak' een voorwaartse of een achterwaartse samentrekking?",
       "voorwaarts", ["achterwaarts", "geen samentrekking"],
       "Voorwaarts: 'appel' wordt in het eerste deel genoemd en verderop weggelaten (appelgebak).",
       niveau=1, hint="Waar staat het gemeenschappelijke deel: eerst of laatst?"),
    mc("Op welk niveau is de samentrekking in 'gekookte en gebakken eieren'?",
       "woordgroepsniveau", ["woordniveau", "zinsniveau"],
       "Woordgroepsniveau: het hele woord 'eieren' is na 'gekookte' weggelaten; daarom geen streepje.",
       niveau=2, hint="Valt er een deel van een woord of een heel woord weg?"),
    ivo("Schrijf korter met een samentrekking op woordniveau: 'zwemles en zwembad'.",
        "zwemles en -bad|zwemles en - bad",
        "Voorwaartse samentrekking op woordniveau: 'zwem' staat in het eerste woord; in het tweede woord vervang je het door een streepje: zwemles en -bad.",
        niveau=2, hint="Op woordniveau gebruik je een streepje."),
    wo("Bij samentrekking op woordgroepsniveau zet je een streepje op de plek van het weggelaten woord.", False,
       "Niet waar. Een streepje schrijf je alleen op woordniveau, als er een deel van een samengesteld woord wegvalt.",
       niveau=2, hint="Streepje = alleen woorddelen."),
    mc("Welk zinsdeel is weggelaten in 'Ruben speelt gitaar en Sanne drums'?",
       "de persoonsvorm", ["het onderwerp", "het lijdend voorwerp", "de bijwoordelijke bepaling"],
       "In het tweede deel ontbreekt 'speelt': Sanne (speelt) drums. Dat is de persoonsvorm.",
       niveau=3, hint="Vul het tweede deel aan tot een hele zin."),
    wo("Tegenwoordig is een ongelijkwaardige samentrekking als 'zowel zwarte- als ijsberen' toegestaan.", True,
       "Waar. Vroeger werd zo'n samentrekking afgekeurd, omdat 'beren' na 'zwarte' een los woord is en na 'ijs' een deel van een samenstelling; tegenwoordig is hij toegestaan.",
       niveau=3, hint="Vroeger fout, nu ...?"),
]

# ---------------------------------------------------------------- toetsen
VW = ["voorwaarts", "achterwaarts", "geen samentrekking"]

T37 = ("Herkennen & voor- of achterwaarts", "🔍", [
    mc("In welke woordgroep is sprake van samentrekking?", "hand- en voetbal",
       ["handdoek en zeep", "voetbal en tennis", "een bal en een doel"],
       "In 'hand- en voetbal' is 'bal' na 'hand' weggelaten (handbal en voetbal). In de andere woordgroepen is niets weggelaten."),
    mc("Is 'zomer- en wintertijd' een voorwaartse of een achterwaartse samentrekking?", VW[1], [VW[0], VW[2]],
       "Achterwaarts: 'tijd' wordt in het laatste deel genoemd en daarvóór weggelaten (zomertijd)."),
    mc("Welke soort samentrekking zie je in 'kastdeuren en -planken'?", VW[0], [VW[1], VW[2]],
       "Voorwaarts: 'kast' staat in het eerste woord en wordt verderop weggelaten (kastplanken)."),
    mc("Welk woorddeel is weggelaten in 'in- en uitgang'?", "gang (achter in-)",
       ["in (voor uitgang)", "uit (voor gang)", "en (tussen de delen)"],
       "Achter 'in-' is 'gang' weggelaten: ingang en uitgang."),
    wo("Bij voorwaartse samentrekking wordt het gemeenschappelijke deel in het eerste deel genoemd en verderop weggelaten.", True,
       "Waar. Bijvoorbeeld 'theelepels en -kopjes': 'thee' staat vooraan en valt verderop weg."),
    wo("Bij achterwaartse samentrekking staat het gemeenschappelijke deel helemaal vooraan in de woordgroep.", False,
       "Niet waar. Bij achterwaartse samentrekking staat het gemeenschappelijke deel in het laatste deel en wordt het daarvóór weggelaten."),
    mc("Welke zin bevat een achterwaartse samentrekking?", "Ik vind zwarte en witte katten even lief.",
       ["Ik zie een zwarte kat en een witte hond.", "Mijn zus aait de kat en mijn broer de hond.",
        "Kattenvoer en -bakken staan in de schuur."],
       "In 'zwarte en witte katten' is 'katten' na 'zwarte' weggelaten; het staat in het laatste deel, dus achterwaarts."),
    mc("Welke zin bevat een voorwaartse samentrekking?", "Mila eet een appel en Sem een peer.",
       ["Mila eet een appel en Sem eet een peer.", "Mila en Sem eten graag fruit.",
        "Rode en groene appels liggen op tafel."],
       "In 'Mila eet een appel en Sem een peer' is 'eet' verderop weggelaten. Het staat in het eerste deel, dus voorwaarts."),
    inv("Welk woord is weggelaten in deze vraag? 'Wil je een grote of een kleine pizza?' Schrijf alleen het weggelaten woord op.",
        "pizza", "Na 'een grote' is 'pizza' weggelaten: een grote (pizza) of een kleine pizza."),
    mc("Welke soort samentrekking is 'Neem jij de groene of de rode tas?'", VW[1], [VW[0], VW[2]],
       "Achterwaarts: 'tas' staat in het laatste deel en is na 'de groene' weggelaten."),
    inv("Welk woord is weggelaten in: 'Thomas bestelde een milkshake en zijn vriendin een ijsje'?",
        "bestelde", "In het tweede deel ontbreekt de persoonsvorm: zijn vriendin (bestelde) een ijsje."),
    mc("Is de samentrekking in 'Kees schildert de deur en Fatma het hek' voorwaarts of achterwaarts?", VW[0], [VW[1], VW[2]],
       "Voorwaarts: 'schildert' staat in het eerste deel en is verderop weggelaten: Fatma (schildert) het hek."),
    wo("In 'leraren en leerlingen' is sprake van samentrekking.", False,
       "Niet waar. 'Leraren' en 'leerlingen' zijn twee verschillende woorden; er is geen gemeenschappelijk deel weggelaten."),
    wo("In 'oud- en nieuwjaar' is sprake van achterwaartse samentrekking.", True,
       "Waar. 'Jaar' staat in het laatste deel en is na 'oud' weggelaten: oudjaar en nieuwjaar."),
    mc("Waarom gebruik je samentrekking?", "Je kunt korter formuleren zonder betekenisverlies",
       ["Je kunt een zin langer maken met extra woorden", "Je verbindt twee zinnen altijd met een komma",
        "Je herhaalt woorden om ze te benadrukken in een zin"],
       "Door identieke (delen van) woorden of zinsdelen weg te laten, formuleer je korter. De betekenis blijft hetzelfde."),
    op("Leg uit wat het verschil is tussen voorwaartse en achterwaartse samentrekking.",
       ["eerste/eerst/vooraan/voorop", "laatste/achteraan/later/verderop/daarvoor"], 1,
       "Bij voorwaartse samentrekking noem je het gemeenschappelijke deel eerst en laat je het verderop weg; bij achterwaartse noem je het als laatste en laat je het daarvoor weg.",
       "Voorwaarts: eerst genoemd, verderop weggelaten (kastdeuren en -planken). Achterwaarts: als laatste genoemd, daarvóór weggelaten (zomer- en wintertijd)."),
    mc("Welk woorddeel is weggelaten in 'land- en tuinbouw'?", "bouw", ["land", "tuin", "en"],
       "Na 'land' is 'bouw' weggelaten: landbouw en tuinbouw."),
    mc("Welke samentrekking is voorwaarts?", "boekenkast en -plank",
       ["fiets- en autosleutels", "ochtend- en avondspits", "voor- en achterdeur"],
       "In 'boekenkast en -plank' staat 'boeken' in het eerste woord en valt het verderop weg. De andere drie zijn achterwaarts."),
    wo("In 'De buren gaan naar Spanje en wij naar Italië' is in het tweede deel het werkwoord 'gaan' weggelaten.", True,
       "Waar. Wij (gaan) naar Italië: de persoonsvorm 'gaan' is weggelaten."),
    op("Leg uit waarom 'Jasmijn hockeyt op zaterdag en Noor op zondag' een voorwaartse samentrekking bevat.",
       ["eerste deel/eerst/vooraan/voorop", "weggelaten/weg/niet herhaald/ontbreekt"], 1,
       "Het werkwoord staat in het eerste deel van de zin en wordt in het tweede deel weggelaten: Noor (hockeyt) op zondag.",
       "Het gemeenschappelijke deel (de persoonsvorm) staat eerst en valt verderop weg; dat is voorwaarts."),
])

T38 = ("Woord-, woordgroeps- of zinsniveau", "🪜", [
    mc("Op welk niveau is de samentrekking in 'keuken- en badkamertegels'?", NIV[0], [NIV[1], NIV[2]],
       "Woordniveau: een deel van een samengesteld woord ('tegels') is weggelaten; daarom staat er een streepje."),
    mc("Op welk niveau is de samentrekking in 'blauwe en paarse ballonnen'?", NIV[1], [NIV[0], NIV[2]],
       "Woordgroepsniveau: het hele woord 'ballonnen' is na 'blauwe' weggelaten; geen streepje."),
    mc("Op welk niveau is de samentrekking in 'Lotte leest een strip en Bram een roman'?", NIV[2], [NIV[0], NIV[1]],
       "Zinsniveau: het zinsdeel 'leest' (persoonsvorm) is weggelaten: Bram (leest) een roman."),
    wo("Bij samentrekking op woordniveau zet je een streepje op de plek van het weggelaten woorddeel.", True,
       "Waar. Bijvoorbeeld 'regenjas en -laarzen' of 'in- en uitgang'."),
    wo("Bij samentrekking op zinsniveau zet je een streepje op de plek van het weggelaten zinsdeel.", False,
       "Niet waar. Op zinsniveau schrijf je geen streepje: 'Lotte leest een strip en Bram een roman.'"),
    wo("Bij samentrekking op woordgroepsniveau worden een of meer hele woorden binnen een woordgroep weggelaten.", True,
       "Waar. Bijvoorbeeld 'verse en gedroogde kruiden': 'kruiden' is na 'verse' weggelaten."),
    mc("Welke schrijfwijze is correct?", "hoofd- en bijzinnen",
       ["hoofd en bijzinnen", "hoofd- en -bijzinnen", "hoofd en -bijzinnen"],
       "Achterwaarts op woordniveau: het streepje komt op de plek van het weggelaten deel 'zinnen', dus direct achter 'hoofd'."),
    mc("Welke schrijfwijze van deze woordgroep is correct?", "verse en gedroogde kruiden",
       ["verse- en gedroogde kruiden", "verse en -gedroogde kruiden", "verse -en gedroogde kruiden"],
       "Woordgroepsniveau: er valt een heel woord weg, dus geen streepje."),
    inv("Schrijf korter met een samentrekking op woordniveau: 'zwembroek en zwembril'.",
        "zwembroek en -bril|zwembroek en - bril",
        "Voorwaarts op woordniveau: 'zwem' staat in het eerste woord en wordt in het tweede vervangen door een streepje."),
    inv("Schrijf korter met een samentrekking op woordniveau: 'basketbal en voetbal'.",
        "basket- en voetbal|basket-en voetbal|basket - en voetbal",
        "Achterwaarts op woordniveau: 'bal' staat in het laatste woord; achter 'basket' komt een streepje."),
    mc("Op welk niveau is de samentrekking in 'Ik heb gisteren mijn kamer opgeruimd en mijn huiswerk gemaakt'?",
       NIV[2], [NIV[0], NIV[1]],
       "Zinsniveau: in het tweede deel zijn de zinsdelen 'ik', 'heb' en 'gisteren' weggelaten."),
    mc("Op welk niveau is de samentrekking in 'zowel dikke als dunne boeken'?", NIV[1], [NIV[0], NIV[2]],
       "Woordgroepsniveau: het hele woord 'boeken' is na 'dikke' weggelaten."),
    mc("Welke woordgroep of zin bevat een samentrekking op woordgroepsniveau?", "oude en nieuwe foto's",
       ["foto- en videocamera's", "Lisa maakt foto's en Ruben video's", "foto's en video's"],
       "In 'oude en nieuwe foto's' is het hele woord 'foto's' na 'oude' weggelaten. 'Foto- en videocamera's' is woordniveau, de zin met Lisa is zinsniveau."),
    mc("Welke zin bevat een samentrekking op zinsniveau?",
       "Wij gaan op de fiets naar school en jullie met de bus.",
       ["Wij hebben groene en gele fietsen.", "Fietsbellen en -lampjes zijn kapot.",
        "Wij fietsen elke dag naar school, omdat het mooi weer is."],
       "In het tweede deel zijn de zinsdelen 'gaan' en 'naar school' weggelaten: jullie (gaan) met de bus (naar school)."),
    op("Leg uit waarom je in 'rode en groene appels' geen streepje schrijft.",
       ["heel woord/hele woord/hele woorden/woordgroepsniveau/woordgroep", "woordniveau/woorddeel/deel van een woord"], 1,
       "Er valt een heel woord weg ('appels'), geen deel van een woord. Het is woordgroepsniveau; een streepje gebruik je alleen op woordniveau.",
       "Streepje = alleen bij een weggelaten woorddeel (woordniveau). Hier valt het hele woord 'appels' weg."),
    mc("Waarom staat er een streepje in 'koffie- en theekopjes'?", "een woorddeel van een samenstelling ontbreekt",
       ["er een heel zinsdeel uit de zin is weggelaten", "de twee woorden samen een tegenstelling vormen",
        "er een bijvoeglijk naamwoord is weggelaten"],
       "'Kopjes' is een deel van de samenstelling 'koffiekopjes'. Op woordniveau zet je een streepje."),
    wo("'Kleine en grote honden' is een samentrekking op woordniveau.", False,
       "Niet waar. Het hele woord 'honden' is weggelaten; dat is woordgroepsniveau."),
    wo("In 'zowel warme als koude dranken' staat het gemeenschappelijke woord achteraan; het is dus een achterwaartse samentrekking op woordgroepsniveau.", True,
       "Waar. 'Dranken' staat in het laatste deel en is na 'warme' weggelaten; er valt een heel woord weg."),
    mc("Welk zinsdeel ontbreekt na 'Jesse' in 'Sanne heeft een kat en Jesse twee konijnen'?",
       "de persoonsvorm", ["het onderwerp", "het lijdend voorwerp", "de bijwoordelijke bepaling"],
       "Jesse (heeft) twee konijnen: de persoonsvorm 'heeft' is weggelaten."),
    op("Maak van deze twee zinnen één zin met een samentrekking op zinsniveau: 'Emma speelt piano. Lucas speelt drums.'",
       ["lucas drums"], 1, "Emma speelt piano en Lucas drums.",
       "De persoonsvorm 'speelt' laat je in het tweede deel weg: voorwaartse samentrekking op zinsniveau."),
])

ZD = ["persoonsvorm", "onderwerp", "lijdend voorwerp", "meewerkend voorwerp", "bijwoordelijke bepaling"]

T39 = ("Welk zinsdeel is weggelaten?", "🧱", [
    mc("Welk zinsdeel is weggelaten in het tweede deel van 'Fleur kocht een jurk en Mees een pak'?",
       ZD[0], [ZD[1], ZD[2], ZD[4]],
       "Mees (kocht) een pak: de persoonsvorm 'kocht' is weggelaten."),
    mc("Welk zinsdeel is weggelaten in het tweede deel van 'Daan schreef een brief en stuurde hem naar zijn oma'?",
       ZD[1], [ZD[0], ZD[2], ZD[3]],
       "(Daan) stuurde hem naar zijn oma: het onderwerp 'Daan' is weggelaten."),
    mc("Welk zinsdeel is weggelaten in 'Mijn broer wast en mijn zus droogt de borden'?",
       ZD[2], [ZD[0], ZD[1], ZD[4]],
       "Mijn broer wast (de borden): het lijdend voorwerp 'de borden' is in het eerste deel weggelaten (achterwaarts)."),
    mc("Welk zinsdeel is in 'Oma gaf de kinderen een snoepje en daarna een knuffel' naast het onderwerp en de persoonsvorm weggelaten?",
       ZD[3], [ZD[2], ZD[4], "naamwoordelijk gezegde"],
       "(Oma gaf de kinderen) daarna een knuffel: ook het meewerkend voorwerp 'de kinderen' is weggelaten."),
    mc("Welk zinsdeel is in 'Op zaterdag werkt Ilse in de bakkerij en Joris in de supermarkt' naast de persoonsvorm weggelaten?",
       ZD[4], [ZD[2], ZD[1], ZD[3]],
       "Joris (werkt op zaterdag) in de supermarkt: ook de bijwoordelijke bepaling 'op zaterdag' is weggelaten."),
    mc("Welke zinsdelen zijn weggelaten na 'mijn tante' in 'Mijn oom is bakker en mijn tante ook'?",
       "persoonsvorm en naamwoordelijk gezegde",
       ["onderwerp en persoonsvorm", "persoonsvorm en lijdend voorwerp", "lijdend voorwerp en meewerkend voorwerp"],
       "Mijn tante (is bakker) ook: de persoonsvorm 'is' en het naamwoordelijk deel 'bakker' zijn weggelaten."),
    inv("Schrijf de persoonsvorm op die is weggelaten in: 'Wij vertrekken morgen naar Parijs en onze buren naar Rome.'",
        "vertrekken", "Onze buren (vertrekken morgen) naar Rome: de persoonsvorm is 'vertrekken'."),
    inv("Welke bijwoordelijke bepaling is in het tweede deel weggelaten? 'Na het eten ruimt Sophie de tafel af en wast Tim de pannen.'",
        "na het eten", "(Na het eten) wast Tim de pannen: de bijwoordelijke bepaling van tijd is weggelaten."),
    inv("Welk onderwerp is in het tweede deel weggelaten? 'De docent deelde de toetsen uit en gaf een korte uitleg.'",
        "docent", "(De docent) gaf een korte uitleg: het onderwerp 'de docent' is weggelaten."),
    wo("In 'Mijn zus wil een hond en mijn broer een kat' is in het tweede deel de persoonsvorm 'wil' weggelaten.", True,
       "Waar. Mijn broer (wil) een kat."),
    wo("In 'Tess heeft haar kamer geverfd en nieuwe gordijnen opgehangen' is in het tweede deel alleen het lijdend voorwerp weggelaten.", False,
       "Niet waar. In het tweede deel zijn het onderwerp 'Tess' en de persoonsvorm 'heeft' weggelaten; 'nieuwe gordijnen' is het lijdend voorwerp en staat er gewoon."),
    mc("Welke zinsdelen ontbreken na 'Rik' in 'Gisteren heeft Mohammed gevoetbald en Rik gezwommen'?",
       "persoonsvorm en bijwoordelijke bepaling",
       ["onderwerp en lijdend voorwerp", "persoonsvorm en lijdend voorwerp",
        "meewerkend voorwerp en bijwoordelijke bepaling"],
       "(Gisteren heeft) Rik gezwommen: de persoonsvorm 'heeft' en de bijwoordelijke bepaling 'gisteren' zijn weggelaten."),
    mc("Welke woorden zijn na 'wij' weggelaten in 'Jullie hebben de prijs gewonnen en wij de beker'?",
       "hebben … gewonnen", ["hebben … de prijs", "gewonnen", "de prijs"],
       "Wij (hebben) de beker (gewonnen): de persoonsvorm en de rest van het werkwoordelijk gezegde zijn weggelaten."),
    mc("Wat is er weggelaten in 'De kat ligt op de bank en de hond in zijn mand'?",
       "de persoonsvorm 'ligt'", ["het onderwerp 'de kat'", "de bepaling 'op de bank'", "het lijdend voorwerp 'de hond'"],
       "De hond (ligt) in zijn mand: de persoonsvorm is weggelaten."),
    mc("In welke zin is het lijdend voorwerp weggelaten?", "Ik schil en mijn moeder snijdt de aardappels.",
       ["Ik schil de aardappels en mijn moeder de uien.", "Ik schil de aardappels en snijd de uien.",
        "Ik schil de aardappels, maar mijn moeder kookt."],
       "Ik schil (de aardappels): het lijdend voorwerp is in het eerste deel weggelaten (achterwaarts)."),
    mc("In welke zin is de persoonsvorm weggelaten?", "Mijn vader rijdt een Volvo en mijn oom een Opel.",
       ["Mijn vader rijdt en mijn oom repareert de Volvo.", "Mijn vader kocht een Volvo en reed er meteen mee weg.",
        "Mijn vader rijdt een Volvo en mijn oom rijdt een Opel."],
       "Mijn oom (rijdt) een Opel: de persoonsvorm is weggelaten."),
    op("Welke twee zinsdelen zijn in het tweede deel van 'Op school draagt Aya een rok en Mila een broek' weggelaten? Noem ze allebei.",
       ["persoonsvorm/pv", "bijwoordelijke bepaling/bwb/bepaling van plaats"], 2,
       "De persoonsvorm (draagt) en de bijwoordelijke bepaling (op school): Mila (draagt op school) een broek.",
       "Vul het tweede deel aan: 'Op school draagt Mila een broek.' Dan zie je welke zinsdelen zijn weggelaten."),
    wo("In 'Ik heb mijn opa een kaart gestuurd en mijn oma een pakketje' zijn in het tweede deel het onderwerp, de persoonsvorm en een deel van het werkwoordelijk gezegde weggelaten.", True,
       "Waar. (Ik heb) mijn oma een pakketje (gestuurd)."),
    wo("In 'Tim verft de muur en Ella het plafond' is 'het plafond' het weggelaten zinsdeel.", False,
       "Niet waar. 'Het plafond' staat er gewoon; weggelaten is de persoonsvorm 'verft': Ella (verft) het plafond."),
    mc("Wat is er na 'mijn moeder' weggelaten in 'Bij het ontbijt drinkt mijn vader koffie en mijn moeder thee'?",
       "drinkt en bij het ontbijt", ["drinkt en koffie", "bij het ontbijt en koffie", "mijn vader en drinkt"],
       "(Bij het ontbijt drinkt) mijn moeder thee: de persoonsvorm en de bijwoordelijke bepaling zijn weggelaten."),
])

T40 = ("Zinnen samentrekken", "✂️", [
    mc("Welke zin is de juiste samentrekking van 'Noor bakt een taart. Sven bakt koekjes.'?",
       "Noor bakt een taart en Sven koekjes.",
       ["Noor bakt een taart en bakt Sven koekjes.", "Noor en Sven bakken een taart en koekjes.",
        "Noor een taart en Sven bakt koekjes."],
       "De persoonsvorm 'bakt' noem je één keer en laat je in het tweede deel weg."),
    inv("Schrijf korter met een samentrekking op woordniveau: 'herfstbladeren en herfstkleuren'.",
        "herfstbladeren en -kleuren|herfstbladeren en - kleuren",
        "Voorwaarts op woordniveau: 'herfst' valt in het tweede woord weg en wordt een streepje."),
    inv("Schrijf korter met een samentrekking op woordniveau: 'brandweerauto en politieauto'.",
        "brandweer- en politieauto|brandweer-en politieauto|brandweer - en politieauto",
        "Achterwaarts op woordniveau: 'auto' staat in het laatste woord; achter 'brandweer' komt een streepje."),
    inv("Schrijf korter met een samentrekking op woordniveau: 'regenjas en regenlaarzen'.",
        "regenjas en -laarzen|regenjas en - laarzen",
        "Voorwaarts op woordniveau: regenjas en -laarzen."),
    inv("Schrijf korter met een samentrekking op woordniveau: 'linkerhand en rechterhand'.",
        "linker- en rechterhand|linker-en rechterhand|linker - en rechterhand",
        "Achterwaarts op woordniveau: linker- en rechterhand."),
    mc("Welke samentrekking van 'dagcrème en nachtcrème' is correct?", "dag- en nachtcrème",
       ["dag en nachtcrème", "dagcrème en -nacht", "dag- en -nachtcrème"],
       "Achterwaarts op woordniveau: alleen achter 'dag' komt een streepje, op de plek van het weggelaten 'crème'."),
    mc("Welke samentrekking van 'voorjaarsvakantie en zomervakantie' is correct?", "voorjaars- en zomervakantie",
       ["voorjaars en zomervakantie", "voorjaarsvakantie en -zomer", "voorjaars- en -zomervakantie"],
       "'Vakantie' staat in het laatste woord; achter 'voorjaars' komt het streepje."),
    mc("Welke zin is de juiste samentrekking van 'Ik heb een rode trui. Ik heb een blauwe trui.'?",
       "Ik heb een rode en een blauwe trui.",
       ["Ik heb een rode- en een blauwe trui.", "Ik heb een rode trui en een blauwe -trui.",
        "Ik heb een rode en een blauwe- trui."],
       "Op woordgroepsniveau valt het hele woord 'trui' weg; je schrijft geen streepje."),
    op("Maak één zin met een samentrekking: 'Mijn broer gaat naar Groningen. Mijn zus gaat naar Utrecht.'",
       ["zus naar utrecht"], 1, "Mijn broer gaat naar Groningen en mijn zus naar Utrecht.",
       "De persoonsvorm 'gaat' laat je in het tweede deel weg (voorwaarts, zinsniveau)."),
    op("Maak één zin met een samentrekking: 'Yara heeft de afwas gedaan. Yara heeft de vuilnisbak buitengezet.'",
       ["gedaan en de vuilnisbak/gedaan en heeft de vuilnisbak"], 1,
       "Yara heeft de afwas gedaan en de vuilnisbak buitengezet.",
       "Het onderwerp 'Yara' en de persoonsvorm 'heeft' noem je één keer; in het tweede deel laat je ze weg."),
    op("Maak één zin met een achterwaartse samentrekking: 'Ik was de auto. Mijn vader poetst de auto.'",
       ["was en mijn vader poetst"], 1, "Ik was en mijn vader poetst de auto.",
       "Het lijdend voorwerp 'de auto' noem je alleen in het laatste deel; daarvóór laat je het weg."),
    mc("Welke zin is een juiste samentrekking van 'Lisa leest een boek. Lisa luistert naar muziek.'?",
       "Lisa leest een boek en luistert naar muziek.",
       ["Lisa leest een boek en Lisa naar muziek.", "Lisa leest een boek en luistert Lisa naar muziek.",
        "Lisa leest en luistert een boek naar muziek."],
       "Alleen het onderwerp 'Lisa' is in beide zinnen hetzelfde; dat laat je in het tweede deel weg."),
    wo("'Kinder- en jeugdboeken' is correct geschreven.", True,
       "Waar. Achterwaarts op woordniveau: kinderboeken en jeugdboeken."),
    wo("'School en sportspullen' (met de betekenis schoolspullen en sportspullen) is correct geschreven.", False,
       "Niet waar. Er valt een woorddeel weg, dus er hoort een streepje: school- en sportspullen."),
    wo("'Lange- en korte broeken' is correct geschreven.", False,
       "Niet waar. Op woordgroepsniveau schrijf je geen streepje: lange en korte broeken."),
    mc("Welke zin is correct geschreven?", "In onze wijk zijn twee kleuter- en basisscholen.",
       ["In onze wijk zijn twee kleuter -en basisscholen.", "In onze wijk zijn twee kleuter en -basisscholen.",
        "In onze wijk zijn twee kleuter- en -basisscholen."],
       "Achterwaarts op woordniveau: het streepje staat direct achter 'kleuter', op de plek van 'scholen'."),
    mc("Welke zin is een juiste samentrekking van 'Op maandag sport Iris. Op maandag zingt Jaimy.'?",
       "Op maandag sport Iris en zingt Jaimy.",
       ["Op maandag sport en zingt Iris en Jaimy.", "Op maandag sport Iris en Jaimy zingt.",
        "Iris sport en Jaimy op maandag zingt."],
       "De bijwoordelijke bepaling 'op maandag' laat je in het tweede deel weg; de woordvolgorde (zingt Jaimy) blijft gelijk."),
    inv("Vul de juiste samentrekking op woordniveau in: 'Op het station zijn de ____ goed aangegeven.' Bedoeld wordt: de ingang en de uitgang.",
        "in- en uitgang|in-en uitgang|in - en uitgang",
        "Achterwaarts op woordniveau: de in- en uitgang."),
    mc("Je wilt 'Sem fietst naar school. Sem neemt de bus naar huis.' samentrekken. Wat laat je weg?",
       "het onderwerp Sem in het tweede deel",
       ["de persoonsvorm fietst in het tweede deel", "de bepaling naar school in het eerste deel",
        "het onderwerp Sem in het eerste deel"],
       "Alleen 'Sem' komt twee keer voor. Je noemt het eerst en laat het verderop weg: Sem fietst naar school en neemt de bus naar huis."),
    op("Maak één woordgroep-samentrekking: 'Ik koop witte schoenen. Ik koop zwarte schoenen.'",
       ["witte en zwarte/zwarte en witte"], 1, "Ik koop witte en zwarte schoenen.",
       "Het woord 'schoenen' noem je één keer; na 'witte' laat je het weg (achterwaarts, woordgroepsniveau)."),
])

T41 = ("Fouten & ongelijkwaardige samentrekking", "⚖️", [
    wo("Een ongelijkwaardige samentrekking wordt tegenwoordig geaccepteerd.", True,
       "Waar. Vroeger werd zo'n samentrekking afgekeurd, nu is hij toegestaan."),
    mc("Welke samentrekking is ongelijkwaardig?", "zowel groene- als ijsthee",
       ["zowel groene als zwarte thee", "zowel ijs- als muntthee", "zowel thee als koffie"],
       "'Thee' is na 'groene' een los woord (groene thee) maar na 'ijs' een deel van een samenstelling (ijsthee)."),
    mc("Waarom werd 'de overstap van de basis- naar de middelbare school' vroeger afgekeurd?",
       "'basisschool' is één woord, 'middelbare school' zijn twee woorden",
       ["'basis' en 'middelbare' zijn allebei bijvoeglijke naamwoorden",
        "achter 'basis' mag nooit een streepje staan in een zin",
        "het weggelaten woord 'school' staat niet aan het eind van de zin"],
       "De delen zijn niet gelijkwaardig: een woorddeel (basis-) en een los bijvoeglijk naamwoord (middelbare)."),
    op("Leg uit waarom 'In dit natuurpark leven zowel zwarte- als ijsberen' een ongelijkwaardige samentrekking is.",
       ["bijvoeglijk/los woord/twee woorden/woordgroep", "samenstelling/samengesteld/één woord/een woord/woorddeel/deel van"], 1,
       "'Beren' is na 'zwarte' een los woord (zwarte beren), maar na 'ijs' een deel van de samenstelling 'ijsberen'.",
       "Het weggelaten deel speelt in beide delen een andere rol: los woord tegenover woorddeel."),
    wo("In 'zowel zwarte- als ijsberen' wordt het weggelaten deel 'beren' na 'zwarte' als een los woord gelezen en na 'ijs' als deel van een samenstelling.", True,
       "Waar. Daarom heet dit een ongelijkwaardige samentrekking."),
    mc("Welke schrijfwijze is NIET correct?", "zomer en winterjassen",
       ["zomer- en winterjassen", "dikke en dunne jassen", "jassenrekken en -haken"],
       "Bij 'zomer en winterjassen' ontbreekt het streepje achter 'zomer' (zomerjassen)."),
    mc("Welke van deze schrijfwijzen is fout?", "warme- en koude dranken",
       ["warme en koude dranken", "fris- en sportdranken", "drankautomaten en -bekers"],
       "Op woordgroepsniveau schrijf je geen streepje: warme en koude dranken."),
    wo("In 'Mijn neef studeert in Delft en mijn nicht in Leiden' is de samentrekking fout, omdat er een streepje had moeten staan.", False,
       "Niet waar. Dit is zinsniveau ('studeert' is weggelaten); daar schrijf je geen streepje. De zin is correct."),
    wo("In 'Hij at een appel en zij een banaan' is de samentrekking correct, omdat 'at' in beide delen dezelfde vorm heeft.", True,
       "Waar. Zij (at) een banaan: het weggelaten woord is precies hetzelfde."),
    mc("In welke zin is de samentrekking fout, omdat het weggelaten woord niet precies hetzelfde is?",
       "Ik heb een hond en mijn ouders een kat.",
       ["Wij hebben een hond en onze buren een kat.", "Ik heb een hond en een kat.",
        "Mijn opa heeft een hond en mijn oma een kat."],
       "Aanvullen geeft 'mijn ouders (heb) een kat', maar het moet 'hebben' zijn. Je mag alleen identieke woorden weglaten."),
    wo("Je mag bij samentrekking alleen woorden of woorddelen weglaten die precies hetzelfde zijn als wat wel genoemd wordt.", True,
       "Waar. Samentrekking betekent: identieke (delen van) woorden of zinsdelen weglaten."),
    mc("Welke samentrekking is gelijkwaardig?", "zowel kleine als grote beren",
       ["zowel kleine- als ijsberen", "van de basis- naar de middelbare school", "zowel zure- als karnemelk"],
       "In 'zowel kleine als grote beren' is 'beren' twee keer een los woord. De andere drie mengen een woorddeel met een los woord."),
    op("Vind jij het goed dat een samentrekking als 'zowel bruine- als ijsberen' tegenwoordig geaccepteerd wordt? Geef je mening en een reden.",
       ["korter/kort/onduidelijk/verwarrend/begrijpelijk/handig/lezen/snap/logisch"], 1,
       "Ja, want het is korter en iedereen begrijpt wat er bedoeld wordt. (Of: nee, want het is verwarrend dat 'beren' een keer los en een keer vast hoort.)",
       "Een mening met een reden is goed, bijvoorbeeld dat het korter is of juist verwarrend."),
    mc("Welke zin bevat een ongelijkwaardige samentrekking?", "We verkopen zowel verse- als diepvriesgroenten.",
       ["We verkopen zowel verse als bevroren groenten.", "We verkopen zowel diepvries- als blikgroenten.",
        "We verkopen verse groenten en ook diepvriesvis."],
       "'Groenten' is na 'verse' een los woord, maar na 'diepvries' een deel van een samenstelling."),
    wo("'Zowel diepvries- als blikgroenten' is een ongelijkwaardige samentrekking.", False,
       "Niet waar. Diepvriesgroenten en blikgroenten zijn allebei samenstellingen; de samentrekking is gelijkwaardig."),
    mc("Wat is er fout aan 'Ik heb een rode- en een blauwe fiets'?",
       "na 'rode' hoort geen streepje: hele woorden zijn weg",
       ["'fiets' moet hier in het meervoud, omdat het er twee zijn", "voor 'fiets' moet ook nog een streepje komen",
        "er is niets fout aan; de zin is helemaal correct"],
       "Dit is woordgroepsniveau ('een rode (fiets) en een blauwe fiets'): geen streepje."),
    mc("Wat is er fout aan 'De bibliotheek heeft studie en leesruimtes' (bedoeld: studieruimtes en leesruimtes)?",
       "na 'studie' ontbreekt een streepje",
       ["na 'leesruimtes' ontbreekt een streepje", "'studie' moet 'studies' zijn", "er is niets fout; de zin is correct"],
       "Op woordniveau zet je een streepje op de plek van het weggelaten woorddeel: studie- en leesruimtes."),
    wo("'De overstap van de basis- naar de middelbare school' wordt tegenwoordig als correct geaccepteerd.", True,
       "Waar. Deze ongelijkwaardige samentrekking werd vroeger afgekeurd, maar is nu toegestaan."),
    inv("Schrijf de woordgroep correct op: 'grote- en kleine kamers'.",
        "grote en kleine kamers",
        "Woordgroepsniveau: er valt een heel woord weg ('kamers'), dus geen streepje."),
    inv("Schrijf correct met een samentrekking: 'vakantiebaantjes en weekendbaantjes'.",
        "vakantie- en weekendbaantjes|vakantie-en weekendbaantjes|vakantie - en weekendbaantjes",
        "Achterwaarts op woordniveau: het streepje komt achter 'vakantie'."),
])

NV = ["woordniveau, voorwaarts", "woordniveau, achterwaarts", "woordgroepsniveau, voorwaarts",
      "woordgroepsniveau, achterwaarts", "zinsniveau, voorwaarts", "zinsniveau, achterwaarts"]

T42 = ("Gemengd", "🔀", [
    mc("Op welk niveau is de samentrekking in 'Mijn tante verkoopt bloemen en mijn oom planten'?", NIV[2], [NIV[0], NIV[1]],
       "Zinsniveau: de persoonsvorm 'verkoopt' is weggelaten."),
    mc("Is 'sinaasappel- en appelsap' voorwaarts of achterwaarts?", VW[1], [VW[0], VW[2]],
       "Achterwaarts: 'sap' staat in het laatste woord en is na 'sinaasappel' weggelaten."),
    inv("Welk woord is in 'Wij ruilen oude voor nieuwe telefoons' na 'oude' weggelaten?",
        "telefoons|telefoon", "Wij ruilen oude (telefoons) voor nieuwe telefoons."),
    wo("'Mijn moeder bakt en mijn vader eet de pannenkoeken' is een voorwaartse samentrekking.", False,
       "Niet waar. 'De pannenkoeken' staat in het laatste deel en is daarvóór weggelaten: achterwaarts."),
    wo("Samentrekking kan voorkomen op woordniveau, woordgroepsniveau en zinsniveau.", True,
       "Waar. Dat zijn de drie niveaus uit de theorie."),
    mc("Welke zin bevat GEEN samentrekking?", "Lars en Julia gaan samen naar de film.",
       ["Lars gaat naar de film en Julia naar het theater.", "Lars kiest zoute en Julia zoete popcorn.",
        "Film- en theaterkaartjes zijn duur."],
       "In 'Lars en Julia gaan samen naar de film' is niets weggelaten: Lars en Julia vormen samen het onderwerp."),
    mc("Welke combinatie klopt voor 'thee- en koffiekopjes'?", NV[1], [NV[0], NV[3], NV[4]],
       "Er valt een woorddeel weg (kopjes), dus woordniveau; het staat in het laatste deel, dus achterwaarts."),
    mc("Welke combinatie klopt voor 'Sara drinkt thee en Bilal koffie'?", NV[4], [NV[5], NV[2], NV[0]],
       "De persoonsvorm 'drinkt' is weggelaten (zinsniveau) en staat in het eerste deel (voorwaarts)."),
    mc("Welke combinatie klopt voor 'zowel lange als korte broeken'?", NV[3], [NV[2], NV[1], NV[5]],
       "Het hele woord 'broeken' valt weg (woordgroepsniveau) en staat in het laatste deel (achterwaarts)."),
    mc("Welke combinatie klopt voor 'tennisrackets en -ballen'?", NV[0], [NV[1], NV[2], NV[5]],
       "Er valt een woorddeel weg (tennis), met streepje: woordniveau. Het staat in het eerste deel: voorwaarts."),
    inv("Schrijf korter met een samentrekking op woordniveau: 'sportschoenen en sporttassen'.",
        "sportschoenen en -tassen|sportschoenen en - tassen",
        "Voorwaarts op woordniveau: sportschoenen en -tassen."),
    op("Maak van deze zinnen één zin met samentrekking: 'Robin wint de eerste wedstrijd. Robin verliest de tweede wedstrijd.'",
       ["en verliest"], 1, "Robin wint de eerste wedstrijd en verliest de tweede.",
       "Het onderwerp 'Robin' laat je in het tweede deel weg. Je mag ook 'wedstrijd' één keer weglaten: Robin wint de eerste en verliest de tweede wedstrijd."),
    wo("In 'kaas- en worstbroodjes' is 'broodjes' het weggelaten woorddeel.", True,
       "Waar. Kaasbroodjes en worstbroodjes: na 'kaas' is 'broodjes' weggelaten."),
    wo("In 'Ik heb mijn tas ingepakt en mijn jas aangetrokken' zijn in het tweede deel het onderwerp en de persoonsvorm weggelaten.", True,
       "Waar. (Ik heb) mijn jas aangetrokken."),
    mc("Wat is er na 'Sara' weggelaten in 'Iedere zomer gaat Ruben kamperen en Sara zeilen'?",
       "persoonsvorm en bijwoordelijke bepaling",
       ["alleen het onderwerp", "persoonsvorm, onderwerp en lijdend voorwerp", "alleen de bijwoordelijke bepaling"],
       "(Iedere zomer gaat) Sara zeilen: de persoonsvorm 'gaat' en de bwb 'iedere zomer' zijn weggelaten."),
    mc("Waar staat het streepje bij een voorwaartse samentrekking op woordniveau?", "aan het begin van het tweede deel",
       ["aan het eind van het eerste deel", "helemaal aan het eind van de woordgroep", "er komt nooit een streepje bij"],
       "Bijvoorbeeld 'zwembroek en -bril': het streepje staat vóór 'bril', op de plek van het weggelaten 'zwem'."),
    mc("Waar staat het streepje bij een achterwaartse samentrekking op woordniveau?", "aan het eind van het eerste deel",
       ["aan het begin van het tweede deel", "voor en achter het tweede deel", "er komt nooit een streepje bij"],
       "Bijvoorbeeld 'linker- en rechterhand': het streepje staat achter 'linker', op de plek van het weggelaten 'hand'."),
    inv("Welk woorddeel is weggelaten in 'Zowel grond- als oppervlaktewater raakt vervuild'?",
        "water", "Grondwater en oppervlaktewater: na 'grond' is 'water' weggelaten."),
    op("Leg uit waarom je in 'Ik zag Jan en hij mij' geen streepje gebruikt.",
       ["zinsniveau/zinsdeel/persoonsvorm/pv/heel woord/hele woord/hele woorden"], 1,
       "Er is een heel zinsdeel weggelaten (de persoonsvorm 'zag'): hij (zag) mij. Dat is zinsniveau, en daar gebruik je geen streepje.",
       "Een streepje hoort alleen bij woordniveau."),
    wo("Door samentrekking verandert de betekenis van een zin.", False,
       "Niet waar. Je formuleert korter, maar de betekenis blijft hetzelfde."),
])

T43 = ("Eindtoets §5.3", "🎯", [
    mc("Welke zin bevat zowel een samentrekking op woordniveau als een op zinsniveau?",
       "Wij kopen teken- en leesboeken en de buren puzzels.",
       ["Wij kopen dikke tekenboeken en de buren dunne leesboeken.", "Wij kopen teken- en leesboeken voor school.",
        "Wij kopen dikke en dunne boeken voor school."],
       "'Teken- en leesboeken' is woordniveau; 'de buren (kopen) puzzels' is zinsniveau."),
    mc("Wat is er weggelaten in 'De trainer gaf de spelers tips en de keeper een compliment'?",
       "de trainer en gaf", ["de spelers en tips", "de trainer en tips", "gaf en de spelers"],
       "(De trainer gaf) de keeper een compliment: het onderwerp en de persoonsvorm zijn weggelaten."),
    inv("Welk voltooid deelwoord is in het tweede deel weggelaten? 'Wij hebben gisteren een film gekeken en onze vrienden een serie.'",
        "gekeken", "Onze vrienden (hebben gisteren) een serie (gekeken)."),
    wo("In 'Vanochtend heeft Mo zijn fiets gerepareerd en Daan zijn brommer' is in het tweede deel ook de bijwoordelijke bepaling 'vanochtend' weggelaten.", True,
       "Waar. (Vanochtend heeft) Daan zijn brommer (gerepareerd)."),
    mc("Is 'Ik was de borden en jij droogt ze af' een samentrekking?", "nee, er is niets weggelaten",
       ["ja, voorwaarts op zinsniveau", "ja, achterwaarts op zinsniveau", "ja, op woordgroepsniveau"],
       "Beide delen zijn volledige zinnen; 'ze' is een verwijswoord, geen samentrekking."),
    mc("Welke zin is een correcte samentrekking van 'In de winter schaatst Lotte. In de winter skiet Pieter.'?",
       "In de winter schaatst Lotte en skiet Pieter.",
       ["In de winter schaatst Lotte en Pieter skiet.", "In de winter schaatst en skiet Lotte en Pieter.",
        "In de winter schaatst Lotte en skiet Pieter ook in de winter."],
       "De bijwoordelijke bepaling 'in de winter' laat je in het tweede deel weg; de woordvolgorde blijft 'skiet Pieter'."),
    mc("Welke samentrekking is fout geschreven?", "lees en schrijfvaardigheid",
       ["lees- en schrijfvaardigheid", "spreek- en luistervaardigheid", "taalvaardigheid en -kennis"],
       "Achter 'lees' ontbreekt het streepje: lees- en schrijfvaardigheid."),
    op("Een leerling schrijft: 'Mijn vader werkt bij een bank en mijn moeder bij een ziekenhuis.' Benoem het soort samentrekking (niveau én richting).",
       ["zinsniveau", "voorwaarts/voorwaartse"], 2,
       "Een voorwaartse samentrekking op zinsniveau: 'werkt' staat in het eerste deel en is in het tweede deel weggelaten.",
       "Er valt een heel zinsdeel weg (persoonsvorm) → zinsniveau; het staat eerst → voorwaarts."),
    op("Herschrijf met een achterwaartse samentrekking op woordniveau: 'De bovenverdieping en de benedenverdieping zijn verbouwd.'",
       ["boven- en benedenverdieping/boven-en benedenverdieping/boven - en benedenverdieping"], 1,
       "De boven- en benedenverdieping zijn verbouwd.",
       "'Verdieping' noem je alleen in het laatste woord; achter 'boven' komt een streepje."),
    mc("Welk woorddeel is weggelaten in 'Zowel tuin- als kamerplanten hebben water nodig'?",
       "planten na tuin-", ["kamer na tuin-", "tuin na kamer", "water na planten"],
       "Tuinplanten en kamerplanten: na 'tuin' is 'planten' weggelaten."),
    wo("In 'Het concert begon om acht uur en eindigde om elf uur' is het onderwerp in het tweede deel weggelaten.", True,
       "Waar. (Het concert) eindigde om elf uur."),
    wo("In 'De les begint om negen en eindigt om tien uur' is 'uur' door een voorwaartse samentrekking weggelaten.", False,
       "Niet waar. 'Uur' staat in het laatste deel en is daarvóór weggelaten (om negen uur): dat is achterwaarts."),
    mc("In welke zin is (onder andere) een meewerkend voorwerp weggelaten?",
       "Ik heb mijn oma een boek gegeven en een kaart gestuurd.",
       ["Ik heb mijn oma een boek en mijn opa een kaart gegeven.",
        "Ik geef mijn oma een boek en mijn opa geeft een kaart.", "Mijn oma en opa krijgen een boek en een kaart."],
       "(Ik heb mijn oma) een kaart gestuurd: ook het meewerkend voorwerp 'mijn oma' is weggelaten."),
    mc("Welke uitspraak over samentrekking is juist?", "Bij zinsniveau laat je hele zinsdelen weg zonder streepje.",
       ["Bij woordgroepsniveau zet je een streepje na het bijvoeglijk naamwoord.",
        "Bij woordniveau laat je een heel zinsdeel weg en zet je een komma.",
        "Bij zinsniveau mag je alleen de persoonsvorm weglaten."],
       "Op zinsniveau vallen hele zinsdelen weg (ow, pv, lv, mv, bwb ...) en schrijf je geen streepje."),
    inv("Welk lijdend voorwerp is in het eerste deel weggelaten? 'Ik schrijf en mijn vriend verstuurt de uitnodigingen.'",
        "uitnodigingen", "Ik schrijf (de uitnodigingen): achterwaartse samentrekking op zinsniveau."),
    mc("Welke soort samentrekking zie je in 'Fenna zingt en Jesse speelt het nieuwe lied'?", VW[1], [VW[0], VW[2]],
       "'Het nieuwe lied' staat in het laatste deel en is daarvóór weggelaten: Fenna zingt (het nieuwe lied)."),
    mc("Welke zin is NIET correct geschreven?", "Ik pluk rode- en witte bessen.",
       ["Ik pluk rode en witte bessen.", "Ik pluk vandaag aard- en bosbessen.", "Ik pluk bessen en bramen."],
       "'Rode en witte bessen' is woordgroepsniveau: geen streepje."),
    op("Een leerling schrijft 'de overstap van de basis- naar de middelbare school'. De docent zegt dat dit vroeger fout werd gerekend. Leg uit waarom.",
       ["samenstelling/één woord/een woord/woorddeel", "bijvoeglijk/los woord/losse woorden/twee woorden/woordgroep", "ongelijkwaardig/ongelijk"], 1,
       "'Basisschool' is één woord (een samenstelling), maar 'middelbare school' bestaat uit twee losse woorden. Het is een ongelijkwaardige samentrekking.",
       "Vroeger moest een samentrekking gelijkwaardig zijn; tegenwoordig wordt deze vorm geaccepteerd."),
    wo("Bij een samentrekking op woordgroepsniveau schrijf je een streepje als het weggelaten woord een zelfstandig naamwoord is.", False,
       "Niet waar. Op woordgroepsniveau schrijf je nooit een streepje, ook niet bij een zelfstandig naamwoord."),
    inv("Schrijf korter met een voorwaartse samentrekking op woordniveau: 'voetbalclubs en voetbalvelden'.",
        "voetbalclubs en -velden|voetbalclubs en - velden",
        "Voetbalclubs en -velden: 'voetbal' valt in het tweede woord weg."),
])

TOETSEN = [(37, T37), (38, T38), (39, T39), (40, T40), (41, T41), (42, T42), (43, T43)]

HEAD_EX = "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 5 §5.3 Samentrekking) — gegenereerd door tools/gen_nederlands_c5_3.py */\n"
HEAD_ON = "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 5) — gegenereerd door tools/gen_nederlands_c5_3.py */\n"


def schrijf(pad, kop, functie, obj):
    with open(pad, "w", encoding="utf-8") as f:
        f.write(kop + functie + "(" + json.dumps(obj, ensure_ascii=False, indent=2) + ");\n")


def main():
    vragen = schud(ONDERWERP_VRAGEN)
    schrijf(os.path.join(ROOT, "c5_3.js"), HEAD_ON, "DURU.register", {
        "id": "c5-3-samentrekking", "hoofdstuk": 5, "paragraaf": "5.3",
        "titel": "§3 Samentrekking",
        "korteUitleg": "Voorwaartse en achterwaartse samentrekking op woord-, woordgroeps- en zinsniveau herkennen en gebruiken.",
        "icoon": "🧩", "theorie": THEORIE, "vragen": vragen})
    teksten = set()
    for nr, (sub, icoon, vr) in TOETSEN:
        assert len(vr) == 20, (nr, len(vr))
        for v in vr:
            assert v["vraag"] not in teksten, v["vraag"]
            teksten.add(v["vraag"])
        schud(vr)
        langst = sum(uniek_langst(v) for v in vr if v["type"] == "mc")
        n_mc = sum(v["type"] == "mc" for v in vr)
        wos = [v for v in vr if v["type"] == "waaronwaar"]
        print(f"examen_{nr}: mc={n_mc} langst={langst} wo={len(wos)} onwaar={sum(not v['antwoord'] for v in wos)}")
        schrijf(os.path.join(ROOT, f"examen_{nr}.js"), HEAD_EX, "DURU.registerExamen", {
            "id": f"ex-h3-nederlands-{nr}", "hoofdstuk": 5, "hoofdstukTitel": "Cursus 5 — Grammatica",
            "paragraaf": "5.3", "titel": f"Toets {nr} — §5.3 {sub}",
            "vak": "Nederlands · HAVO 3 (Cursus 5)", "icoon": icoon, "duurMin": 20, "vragen": vr})
    assert len(THEORIE) >= 1500


if __name__ == "__main__":
    main()
