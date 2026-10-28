#!/usr/bin/env python3
"""Begrippen-modules + begrippentoetsen voor Nederlands HAVO 3, Cursus 5 (§3, §5) en Cursus 7 (§2, §3).

Schrijft havo3/nederlands/js/data/{c5_begrippen,c7_begrippen,examen_51,examen_52}.js.
Bron: Noordhoff Nederlands HAVO 3, Cursus 5 p. 210-215, Cursus 7 p. 244-247
(inbox/2026-2027/nederlands/nederlands_cursus7_en_cursus5_tum_bolumler.pdf).
mc-opties worden geseed geschud (antwoord = index van de juiste optie na schudden).
"""
import json
import os
import random

DATA = os.path.join(os.path.dirname(__file__), "..", "havo3", "nederlands", "js", "data")


def mc(vraag, juist, fout, uitleg, **extra):
    return dict(type="mc", vraag=vraag, opties=[juist] + fout, antwoord=0, uitleg=uitleg, **extra)


def wo(vraag, antwoord, uitleg):
    return dict(type="waaronwaar", vraag=vraag, antwoord=antwoord, uitleg=uitleg)


def invul(vraag, antwoord, uitleg):
    return dict(type="invul", vraag=vraag, antwoord=antwoord, uitleg=uitleg)


def invoer(vraag, antwoord, uitleg, **extra):
    return dict(type="invoer", vraag=vraag, antwoord=antwoord, uitleg=uitleg, **extra)


def open_(vraag, sleutels, min_t, model, uitleg):
    return dict(type="open", vraag=vraag, sleutelwoorden=sleutels, minTreffers=min_t,
                modelantwoord=model, uitleg=uitleg)


def schud(vragen, rng):
    # juiste optie per blok van 4 mc's op een geschudde positie 0-3 (gate-regel 3: <=40% per index)
    doelen = []
    for v in vragen:
        if v["type"] != "mc":
            continue
        if not doelen:
            doelen = rng.sample(range(4), 4)
        juist, rest = v["opties"][0], v["opties"][1:]
        rng.shuffle(rest)
        rest.insert(doelen.pop(), juist)
        v["opties"], v["antwoord"] = rest, rest.index(juist)
    return vragen


# ---------------------------------------------------------------- Cursus 7
C7_THEORIE = """
<h3>Begrippenlijst Cursus 7 — Spelling (§2 en §3)</h3>
<p>Alle vaktermen uit <b>§2 Trema, apostrof, accenten en cedille</b> en <b>§3 Met of zonder n?</b> op een rij. Ken ze zo dat je ze kunt <i>uitleggen</i> én met een eigen voorbeeld kunt laten zien.</p>

<div class="formule-box">
<h4>§2 — Tekens tegen uitspraakproblemen</h4>
<ul>
  <li><b>Trema</b> (¨): teken op een klinker dat aangeeft dat een nieuwe lettergreep begint, zodat twee klinkers niet samen als één klank worden uitgesproken: <i>beïnvloeden, Indiër, reeën, variëren</i>. Ook in sommige leenwoorden: <i>fröbelen, kür, patiënt</i>.</li>
  <li><b>Koppelteken</b> (-): in <b>samenstellingen</b> waarin klinkers botsen gebruik je geen trema maar een koppelteken: <i>auto-eigenaar, bio-economie, maffia-achtig</i>.</li>
  <li><b>Samenstelling</b>: woord dat uit twee (of meer) zelfstandige woorden is gemaakt (<i>auto + eigenaar</i>).</li>
  <li><b>Apostrof</b> ('): wordt gebruikt (1) voor een <b>-s</b> na woorden op de enkele klinkers <i>a, i, o, u, y</i> (<i>buggy's, Emma's boek, ski's</i>); (2) als <b>weglatingsteken</b> (<i>Hans' gitaar, 's morgens, 's-Hertogenbosch</i>); (3) in afleidingen en meervouden van <b>afkortingen</b> (<i>cd's, sms'je, wc's</i>); (4) in <b>verkleinwoorden op -y</b> na een medeklinker (<i>pony'tje</i>, maar <i>spraytje</i>).</li>
  <li><b>Weglatingsteken</b>: apostrof die laat zien dat er letters zijn weggelaten (<i>'s = des</i>) of die de bezits-s vervangt na een sisklank (<i>Hans' gitaar</i>).</li>
  <li><b>Accent aigu</b> (´): <i>café, passé</i>; ook als <b>klemtoonteken</b> om een woord(deel) te benadrukken (<i>vóórkomen, twéé</i>).</li>
  <li><b>Accent grave</b> (`): <i>caissière, fin de siècle, à</i>.</li>
  <li><b>Accent circonflexe</b> (^): <i>gemêleerd, moment suprême, maître</i>.</li>
  <li><b>Klemtoonteken</b>: accent aigu op alle klinkers van de beklemtoonde lettergreep, behalve bij drie klinkers: dan alleen op de eerste twee (<i>móói, éénmaal</i>). <i>Een</i> krijgt alleen accenten als het het telwoord 1 is én je het moet benadrukken.</li>
  <li><b>Cedille</b> (¸): haakje onder de c (ç) waardoor de c als <b>s</b> klinkt vóór a, o of u: <i>Curaçao, François, reçu</i>. Zonder cedille klinkt c daar als k (<i>cacao, cursus</i>).</li>
  <li><b>Leenwoord</b>: woord dat uit een andere taal is overgenomen (<i>crème fraîche, caissière, saté</i>).</li>
</ul>
</div>

<div class="formule-box">
<h4>§3 — Met of zonder n?</h4>
<ul>
  <li><b>Telwoord</b>: woord dat een aantal of hoeveelheid aangeeft: <i>alle, beide, enkele, vele, weinige, sommige, tientallen</i>.</li>
  <li><b>Zelfstandig gebruikt telwoord</b>: telwoord zonder zelfstandig naamwoord erachter, dat je ook niet uit de zin kunt aanvullen. Duidt het <b>personen</b> aan, dan krijgt het een <b>n</b>: <i>Allen kregen een oproep; sommigen kwamen niet.</i></li>
  <li><b>Niet-zelfstandig (bijvoeglijk) gebruikt telwoord</b>: staat bij een zelfstandig naamwoord (<i>alle leerlingen</i>) of verwijst naar zaken (<i>enkele van de kastanjes</i>) → <b>geen n</b>.</li>
  <li><b>Tientallen, honderden, (tien)duizenden, miljoenen</b> krijgen <b>altijd</b> een n.</li>
  <li><b>Zelfstandig gebruikt bijvoeglijk naamwoord</b>: bijvoeglijk naamwoord zonder zelfstandig naamwoord erachter. Voor <b>personen</b>: enkelvoud -e, meervoud -<b>n</b> (<i>een jongere, de ouderen</i>). Voor <b>zaken</b>: -e (<i>heel mooie</i>).</li>
  <li><b>Stoffelijk bijvoeglijk naamwoord</b>: geeft aan waarvan iets gemaakt is en eindigt al op -en: <i>zilveren, gouden, houten, wollen</i>. Zelfstandig gebruikt blijft het zo: <i>dertig zilveren en enkele gouden</i>.</li>
  <li><b>Meervouds-n</b>: de n die het meervoud aangeeft bij zelfstandig gebruikte woorden voor personen.</li>
</ul>
</div>

<div class="info-box tip">
<h4>Ezelsbruggetje</h4>
<p><b>Trema</b> = binnen één woord; <b>koppelteken</b> = tussen twee delen van een samenstelling. <b>n</b> = mensen (zelfstandig gebruikt); zaken en dieren = geen n.</p>
</div>
"""

C7_OEFEN = [
    mc("Welk begrip hoort bij deze omschrijving: 'teken dat aangeeft dat er een nieuwe lettergreep begint, zodat twee klinkers niet samensmelten'?",
       "het trema", ["het accent grave", "de cedille", "de apostrof"],
       "Het trema (¨) voorkomt dat twee klinkers als één klank worden gelezen: beïnvloeden, ideeën.",
       niveau=1, hint="Denk aan ideeën en reeën."),
    mc("Wat zet je in de samenstelling zee + egel tussen de botsende klinkers?",
       "een koppelteken", ["een trema", "een apostrof", "een accent aigu"],
       "In samenstellingen gebruik je geen trema maar een koppelteken: zee-egel.",
       niveau=1, hint="Het gaat om twee losse woorden die aan elkaar zijn gezet."),
    wo("De cedille zorgt ervoor dat een c vóór a, o of u als een k klinkt.", False,
       "Niet waar. Het is precies andersom: met cedille (ç) klinkt de c als s (Curaçao); zonder cedille klinkt hij daar als k (cacao)."),
    wo("Een weglatingsteken is een apostrof die laat zien dat er letters zijn weggelaten, zoals in 's avonds.", True,
       "Waar. In 's avonds staat 's voor des; de apostrof is hier een weglatingsteken."),
    invoer("Hoe heet het accent in het woord caissière?", "accent grave|grave",
           "De streep van linksboven naar rechtsonder (è) heet accent grave.", niveau=2,
           hint="Aigu, grave of circonflexe?"),
    mc("Hoe noem je 'beiden' in de zin: Beiden kwamen te laat?",
       "een zelfstandig gebruikt telwoord", ["een stoffelijk bijvoeglijk naamwoord",
                                             "een bijvoeglijk gebruikt telwoord", "een leenwoord met een trema"],
       "Er staat geen zelfstandig naamwoord achter en het duidt personen aan: zelfstandig gebruikt telwoord met n.",
       niveau=2, hint="Staat er een zelfstandig naamwoord achter?"),
    wo("Een stoffelijk bijvoeglijk naamwoord zoals 'houten' krijgt zelfstandig gebruikt een extra -e: houtene.", False,
       "Niet waar. Stoffelijke bijvoeglijke naamwoorden eindigen al op -en en blijven zo: 'drie houten en twee ijzeren'."),
    invoer("Welk begrip uit §2 hoort bij de accenten in: 'Ik zei níét morgen, maar vandaag'?",
           "klemtoonteken|klemtoontekens|klemtoon",
           "Hier wordt het accent aigu gebruikt om een woord te benadrukken: het is een klemtoonteken.",
           niveau=2, hint="Het accent geeft hier nadruk aan."),
]

C7_TOETS = [
    mc("Begrip: in welk woord is het trema gebruikt om twee klinkers uit elkaar te houden?",
       "coëfficiënt", ["gemêleerd", "reçu", "fin de siècle"],
       "In coëfficiënt houden de trema's o-e en i-e uit elkaar. gemêleerd heeft een circonflexe, reçu een cedille, fin de siècle een accent grave."),
    mc("Welk leesteken gebruik je in de samenstelling foto + album?",
       "koppelteken: foto-album", ["trema op de a: fotoälbum", "apostrof: foto'album", "geen teken: fotoalbum"],
       "Samenstelling waarin klinkers botsen (o-a): koppelteken, geen trema."),
    mc("Wat is een samenstelling?",
       "een woord dat bestaat uit twee of meer zelfstandige woorden",
       ["een woord dat uit een andere taal is overgenomen, zoals saté of café",
        "een woord waarvan letters zijn weggelaten",
        "een woord waarin twee klinkers samen één klank vormen"],
       "Een samenstelling is een woord gevormd uit zelfstandige woorden (radio + omroep). Een overgenomen woord is een leenwoord."),
    mc("In welke van deze vormen is de apostrof een weglatingsteken?",
       "'s zomers", ["opa's", "cd's", "Emma's fiets"],
       "In 's zomers staat 's voor des: er zijn letters weggelaten. Bij opa's, cd's en Emma's fiets voorkomt de apostrof een uitspraakprobleem."),
    mc("Hoe heet het teken onder de c in reçu?",
       "cedille", ["trema", "accent aigu", "koppelteken"],
       "De cedille (ç) laat de c als s klinken vóór a, o of u."),
    mc("Welk accent staat er in het woord crêpe?",
       "accent circonflexe", ["accent aigu", "accent grave", "accent aigu als klemtoonteken"],
       "Het dakje (ê) is een accent circonflexe, net als in gemêleerd."),
    mc("Wanneer schrijf je 'een' met accenten (één)?",
       "als het het telwoord 1 is en je het moet benadrukken",
       ["altijd als 'een' aan het begin van de zin staat",
        "als 'een' een lidwoord is voor een het-woord",
        "nooit, want 'een' krijgt alleen een trema"],
       "Accenten op een zet je alleen als het het telwoord 1 is en uitgesproken moet worden met nadruk: één."),
    mc("Wanneer noem je een telwoord 'zelfstandig gebruikt'?",
       "als er geen zelfstandig naamwoord achter staat en je er ook geen kunt aanvullen",
       ["als het telwoord altijd een hoofdletter krijgt",
        "als er een zelfstandig naamwoord direct achter staat",
        "als het telwoord in het meervoud op -e eindigt"],
       "Zelfstandig gebruikt = zonder zelfstandig naamwoord erachter, ook niet aan te vullen uit de zin."),
    mc("Welk woord is een stoffelijk bijvoeglijk naamwoord?",
       "wollen", ["ouderen", "sommigen", "tientallen"],
       "Wollen geeft aan waarvan iets gemaakt is (wol) en eindigt al op -en."),
    mc("Welk soort woord is 'zieken' in: De zieken werden als eerste geholpen?",
       "zelfstandig gebruikt bijvoeglijk naamwoord", ["stoffelijk bijvoeglijk naamwoord",
                                                      "bijvoeglijk gebruikt telwoord", "samenstelling met koppelteken"],
       "Ziek is een bijvoeglijk naamwoord; zonder zelfstandig naamwoord erachter en voor personen in het meervoud: zieken."),
    wo("Het trema gebruik je ook in samenstellingen waarin twee klinkers botsen, zoals in radioomroep.", False,
       "Niet waar. In samenstellingen gebruik je een koppelteken: radio-omroep."),
    wo("Het accent aigu kan ook een klemtoonteken zijn, bijvoorbeeld in 'Dat is écht waar'.", True,
       "Waar. Het accent aigu wordt ook gebruikt om een woord(deel) te benadrukken."),
    wo("Tientallen, honderden en duizenden schrijf je altijd met een n.", True,
       "Waar. Deze telwoorden krijgen altijd een n: tientallen euro's, honderden fans."),
    wo("Een meervouds-n krijgen zelfstandig gebruikte bijvoeglijke naamwoorden vooral als ze zaken aanduiden.", False,
       "Niet waar. De meervouds-n hoort bij personen (de ouderen); voor zaken gebruik je -e (heel mooie)."),
    wo("Een apostrof gebruik je in het verkleinwoord van baby: baby'tje.", True,
       "Waar. Verkleinwoorden op -y voorafgegaan door een medeklinker krijgen een apostrof: baby'tje, pony'tje."),
    invul("Hoe noem je een woord dat uit een andere taal is overgenomen, zoals croissant of saté?",
          "leenwoord", "Een leenwoord is uit een andere taal overgenomen; leenwoorden hebben vaak accenten (saté, café)."),
    invul("Welk teken (één woord) zet je in de samenstelling milieu + impact?",
          "koppelteken", "milieu-impact: samenstelling met botsende klinkers → koppelteken."),
    invul("Welk accent (alleen het Franse woord) staat er in het woord café?",
          "aigu", "De streep van rechtsboven naar linksonder (é) is een accent aigu."),
    open_("Leg uit wat het verschil is tussen een trema en een koppelteken, en geef van allebei een voorbeeld.",
          ["samenstelling/samengesteld/twee woorden", "lettergreep/uitspraak/klinkers"], 1,
          "Allebei voorkomen dat botsende klinkers als één klank worden uitgesproken. Een trema staat binnen één woord (ideeën, beïnvloeden); een koppelteken zet je in een samenstelling van twee woorden (zee-egel, auto-eigenaar).",
          "Trema = binnen één woord; koppelteken = tussen de delen van een samenstelling."),
    open_("Leg uit waarom 'enkele' in 'Enkele van de appels waren rot' geen n krijgt.",
          ["personen/mensen", "zaken/dingen/aanvullen/naamwoord"], 1,
          "Enkele verwijst naar appels: dat zijn zaken, geen personen. Bovendien kun je 'appels' aanvullen. Daarom schrijf je het zonder n.",
          "Alleen zelfstandig gebruikte telwoorden die personen aanduiden krijgen een n."),
]

# ---------------------------------------------------------------- Cursus 5
C5_THEORIE = """
<h3>Begrippenlijst Cursus 5 — Grammatica (§3 en §5)</h3>
<p>Alle vaktermen uit <b>§3 Samentrekking</b> en <b>§5 Verwijzen</b>. Je moet ze kunnen <i>herkennen</i> in een zin en kunnen <i>uitleggen</i>.</p>

<div class="formule-box">
<h4>§3 — Samentrekking</h4>
<ul>
  <li><b>Samentrekking</b>: een identiek woorddeel, woord of zinsdeel weglaten omdat het al op een andere plek in de woordgroep of zin staat. Zo formuleer je korter: <i>voor- en nadelen, dikke en dunne sokken</i>.</li>
  <li><b>Voorwaartse samentrekking</b>: het gemeenschappelijke deel staat in het <b>eerste</b> deel en wordt verderop weggelaten: <i>kerstballen en -slingers</i>.</li>
  <li><b>Achterwaartse samentrekking</b>: het gemeenschappelijke deel staat in het <b>laatste</b> deel en wordt daarvóór weggelaten: <i>in- en uitademen</i>.</li>
  <li><b>Woordniveau</b>: een woorddeel wordt weggelaten; op die plek schrijf je een <b>streepje</b>: <i>theepot en -doos, binnen- en buitenland</i>.</li>
  <li><b>Woordgroepsniveau</b>: binnen een woordgroep worden hele woorden weggelaten, <b>zonder streepje</b>: <i>bloeiende planten en struiken; gele en rode paprika's</i>.</li>
  <li><b>Zinsniveau</b>: een of meer <b>zinsdelen</b> die twee keer voorkomen worden weggelaten, zonder streepje: <i>Didi bakt pannenkoeken en Ivan een pizza</i> (pv weggelaten).</li>
  <li><b>Zinsdelen</b>: persoonsvorm (<b>pv</b>), onderwerp (<b>ow</b>), gezegde (<b>gez</b>; werkwoordelijk gezegde <b>wg</b>), lijdend voorwerp (<b>lv</b>), meewerkend voorwerp (<b>mv</b>), bijwoordelijke bepaling (<b>bwb</b>).</li>
  <li><b>Ongelijkwaardige samentrekking</b>: samentrekking waarbij het weggelaten deel in de twee delen niet dezelfde functie of vorm heeft, bijvoorbeeld <i>zowel bruine- als ijsberen</i> of <i>van de basis- naar de middelbare school</i>. Vroeger afgekeurd, tegenwoordig geaccepteerd.</li>
</ul>
</div>

<div class="formule-box">
<h4>§5 — Verwijzen</h4>
<ul>
  <li><b>Verwijswoord</b>: woord dat terugwijst naar een of meer woorden die eerder genoemd zijn (<i>hij, zij, het, die, dat, wat, waarop</i> …).</li>
  <li><b>Antecedent</b>: het woord (of de woordgroep, of de hele zin) waarnaar een verwijswoord verwijst.</li>
  <li><b>Geslacht</b>: de-woorden zijn <b>mannelijk</b> (verwijzen met <i>hij/hem/zijn</i>) of <b>vrouwelijk</b> (<i>zij/ze/haar</i>); het-woorden zijn <b>onzijdig</b> (<i>het/zijn, dit/dat</i>).</li>
  <li><b>Het-woorden</b>: ook namen van landen, provincies, steden en clubs, en alle <b>verkleinwoorden</b>: <i>Amsterdam en zijn parkeerproblemen</i>.</li>
  <li><b>Vrouwelijke uitgangen</b>: veel de-woorden op <i>-de, -heid, -ie, -iek, -ij, -ing, -nis, -schap, -st, -te, -teit, -theek, -uur</i> zijn vrouwelijk, net als vrouwelijke personen en dieren (<i>de actrice, de leeuwin</i>).</li>
  <li><b>Lijdend voorwerp (lv)</b>: in het meervoud verwijs je ernaar met <b>hen</b>; ook <b>na een voorzetsel</b> gebruik je hen.</li>
  <li><b>Meewerkend voorwerp (mv)</b> zonder voorzetsel: <b>hun</b>. <b>Hun</b> is ook het <b>bezittelijk voornaamwoord</b> (<i>hun auto</i>).</li>
  <li><b>Onbepaald voornaamwoord</b>: <i>alles, niets, iets, veel</i> … Ernaar verwijs je met <b>wat</b>, net als naar <i>dat/datgene</i>, een <b>overtreffende trap</b> (<i>het mooiste wat</i>) en een <b>hele zin</b>.</li>
  <li><b>Daar/waar + voorzetsel</b> (<i>waarop, daarmee</i>) gebruik je bij dieren en dingen; <b>voorzetsel + wie</b> (<i>van wie, met wie</i>) bij personen.</li>
</ul>
</div>

<div class="info-box tip">
<h4>Hen of hun?</h4>
<p>Kun je er <i>aan</i> of <i>voor</i> voor zetten? Dan is het een meewerkend voorwerp → <b>hun</b>. Lijdend voorwerp of na een voorzetsel → <b>hen</b>. Onderwerp → <b>zij/ze</b>, nooit <i>hun</i>.</p>
</div>
"""

C5_OEFEN = [
    mc("Hoe heet het woord waarnaar een verwijswoord terugwijst?",
       "het antecedent", ["het lijdend voorwerp", "de persoonsvorm", "het klemtoonteken"],
       "Het woord (of de woordgroep of zin) waarnaar een verwijswoord verwijst, heet het antecedent.",
       niveau=1, hint="Het begrip begint met een a."),
    mc("Welk soort samentrekking is 'in- en uitademen'?",
       "achterwaartse samentrekking", ["voorwaartse samentrekking", "ongelijkwaardige samentrekking",
                                       "samentrekking op zinsniveau"],
       "Het gemeenschappelijke deel (ademen) staat achteraan en is daarvóór weggelaten: achterwaarts.",
       niveau=1, hint="Waar staat het deel dat je maar één keer leest?"),
    wo("Bij samentrekking op woordgroepsniveau schrijf je een streepje op de plek van het weggelaten woord.", False,
       "Niet waar. Alleen op woordniveau (weggelaten woorddeel) schrijf je een streepje: theepot en -doos."),
    wo("Verkleinwoorden zijn altijd het-woorden, dus je verwijst ernaar met 'het' of 'dat'.", True,
       "Waar. Alle verkleinwoorden zijn onzijdig: het meisje, dat ..."),
    invoer("Welk verwijswoord gebruik je in het meervoud als lijdend voorwerp: hen of hun?", "hen",
           "Lijdend voorwerp en na een voorzetsel: hen. Meewerkend voorwerp zonder voorzetsel: hun.",
           niveau=2, hint="Ik zie ... morgen."),
    mc("Wat is een ongelijkwaardige samentrekking?",
       "een samentrekking waarbij het weggelaten deel niet dezelfde functie of vorm heeft",
       ["een samentrekking waarbij je een streepje vergeet te schrijven",
        "een samentrekking waarbij het onderwerp twee keer genoemd wordt",
        "een samentrekking waarbij een verwijswoord het antecedent vervangt"],
       "Bij 'zowel bruine- als ijsberen' heeft het weggelaten deel niet dezelfde functie; vroeger afgekeurd, nu geaccepteerd.",
       niveau=3, hint="Denk aan 'van de basis- naar de middelbare school'."),
    invoer("Op welk niveau is 'Sanne leest een strip en Bram een roman' samengetrokken? (woord, woordgroep of zin)",
           "zin|zinsniveau",
           "De persoonsvorm 'leest' (een zinsdeel) is weggelaten: samentrekking op zinsniveau.",
           niveau=2, hint="Welk deel is weggelaten: een woorddeel, een woord in een groep of een zinsdeel?"),
    mc("Welk verwijswoord gebruik je bij personen na een voorzetsel, zoals in 'de trainer ... ik praatte'?",
       "met wie", ["waarmee", "met wat", "daarmee"],
       "Bij personen gebruik je voorzetsel + wie; waarmee/daarmee is voor dieren en dingen.",
       niveau=2, hint="Gaat het om een persoon of een ding?"),
]

C5_TOETS = [
    mc("Begrip: wat is een verwijswoord?",
       "een woord dat terugwijst naar iets wat eerder genoemd is",
       ["een woord dat altijd een meervouds-n krijgt",
        "een woord dat in een samentrekking op zinsniveau wordt weggelaten",
        "een woord dat de persoonsvorm van de zin vormt"],
       "Een verwijswoord (hij, die, dat, waarop …) wijst terug naar een eerder genoemd antecedent."),
    mc("Wat is samentrekking?",
       "een identiek (deel van een) woord of zinsdeel weglaten omdat het al elders staat",
       ["een samenstelling van twee woorden met een koppelteken",
        "een verwijswoord gebruiken in plaats van het antecedent",
        "twee zinnen verbinden met een voegwoord zonder komma"],
       "Bij samentrekking laat je een identiek woorddeel, woord of zinsdeel weg om korter te formuleren."),
    mc("Welk soort samentrekking is 'damesfietsen en -schoenen'?",
       "voorwaartse samentrekking op woordniveau",
       ["achterwaartse samentrekking op woordniveau",
        "voorwaartse samentrekking op zinsniveau",
        "achterwaartse samentrekking op woordgroepsniveau"],
       "'dames' staat in het eerste deel en wordt verderop weggelaten (streepje): voorwaarts, woordniveau."),
    mc("Welk soort samentrekking is 'warme en koude dranken'?",
       "achterwaartse samentrekking op woordgroepsniveau",
       ["voorwaartse samentrekking op woordgroepsniveau",
        "achterwaartse samentrekking op woordniveau",
        "voorwaartse samentrekking op zinsniveau"],
       "Het hele woord 'dranken' staat achteraan en is bij 'warme' weggelaten, zonder streepje: achterwaarts, woordgroepsniveau."),
    mc("Welk zinsdeel is weggelaten in 'Mila speelt viool en haar broer gitaar'?",
       "de persoonsvorm", ["het onderwerp", "het lijdend voorwerp", "het meewerkend voorwerp"],
       "Voluit: ... en haar broer speelt gitaar. De persoonsvorm 'speelt' is weggelaten (zinsniveau)."),
    mc("Naar welk soort woorden verwijs je met 'het' en 'dat'?",
       "onzijdige woorden (het-woorden)", ["vrouwelijke de-woorden", "mannelijke de-woorden",
                                           "woorden in het meervoud, zoals de kinderen"],
       "Het en dit/dat horen bij het-woorden, die onzijdig zijn."),
    mc("Welk zelfstandig naamwoord is vrouwelijk volgens de uitgangen uit §5?",
       "de gezondheid", ["de tafel", "de verwarmingsketel", "de bezem"],
       "Woorden op -heid zijn vrouwelijk: de gezondheid ... zij/haar."),
    mc("Hoe heet 'hun' in de zin: De buren zijn verhuisd; hun tuin staat te koop?",
       "bezittelijk voornaamwoord", ["lijdend voorwerp in het meervoud", "onderwerp", "onbepaald voornaamwoord"],
       "Hun tuin = de tuin van hen: hier is hun een bezittelijk voornaamwoord."),
    mc("Welk woord is een onbepaald voornaamwoord?",
       "niets", ["waarop", "hem", "haar"],
       "Niets, alles, iets en veel zijn onbepaalde voornaamwoorden; ernaar verwijs je met 'wat'."),
    mc("Wat gebruik je bij dieren en dingen in plaats van 'voorzetsel + wie'?",
       "daar/waar + voorzetsel", ["voorzetsel + wat", "voorzetsel + die", "voorzetsel + hen of hun"],
       "Bij dieren en dingen: waarop, daarmee, waarover. Bij personen: op wie, met wie."),
    wo("Bij achterwaartse samentrekking staat het gemeenschappelijke deel in het eerste deel van de samentrekking.", False,
       "Niet waar. Bij achterwaartse samentrekking staat het gemeenschappelijke deel in het laatste deel (in- en uitademen)."),
    wo("Namen van landen, provincies, steden en clubs zijn het-woorden.", True,
       "Waar. Daarom: Utrecht en zijn grachten, Ajax en zijn supporters."),
    wo("Hun mag je gebruiken als onderwerp, bijvoorbeeld: Hun hebben de wedstrijd gewonnen.", False,
       "Niet waar. Als onderwerp gebruik je zij of ze: Zij hebben de wedstrijd gewonnen."),
    wo("Een ongelijkwaardige samentrekking zoals 'zowel bruine- als ijsberen' wordt tegenwoordig geaccepteerd.", True,
       "Waar. Vroeger werd zo'n samentrekking afgekeurd, tegenwoordig wordt hij geaccepteerd."),
    wo("Bij samentrekking op zinsniveau kunnen ook meerdere zinsdelen tegelijk weggelaten worden.", True,
       "Waar. Bijvoorbeeld: Op de barbecue heb ik een kip gegrild en een vis geroosterd (bwb, pv en ow weggelaten)."),
    invul("Hoe heet het woord of de woordgroep waarnaar een verwijswoord verwijst?",
          "antecedent", "Het antecedent is het woord (of de woordgroep of zin) waarnaar het verwijswoord verwijst."),
    invul("Wat schrijf je op de plek van het weggelaten woorddeel bij samentrekking op woordniveau? (één woord)",
          "streepje|liggend streepje", "Op woordniveau zet je een streepje: binnen- en buitenland."),
    invul("Welk verwijswoord gebruik je naar een hele zin, een overtreffende trap of 'alles'?",
          "wat", "Naar dat/datgene, onbepaalde voornaamwoorden, overtreffende trappen en hele zinnen verwijs je met 'wat'."),
    open_("Leg uit wat het verschil is tussen voorwaartse en achterwaartse samentrekking. Geef van allebei een voorbeeld.",
          ["eerste/eerst/begin", "laatste/achteraan/einde/laatst"], 2,
          "Bij voorwaartse samentrekking staat het gemeenschappelijke deel in het eerste deel en wordt het verderop weggelaten (kerstballen en -slingers). Bij achterwaartse samentrekking staat het in het laatste deel en wordt het daarvóór weggelaten (in- en uitademen).",
          "Voorwaarts: eerst genoemd, later weggelaten. Achterwaarts: later genoemd, eerder weggelaten."),
    open_("Leg uit wanneer je 'hen' en wanneer je 'hun' gebruikt als verwijswoord.",
          ["lijdend voorwerp/lv/voorzetsel", "meewerkend voorwerp/mv/bezittelijk"], 2,
          "Hen gebruik je als lijdend voorwerp en na een voorzetsel (ik zie hen, voor hen). Hun gebruik je als meewerkend voorwerp zonder voorzetsel (ik geef hun een cadeau) en als bezittelijk voornaamwoord (hun huis).",
          "hen = lv of na voorzetsel; hun = mv zonder voorzetsel of bezittelijk voornaamwoord."),
]


def onderwerp(id_, hf, titel, kort, icoon, theorie, vragen):
    return dict(id=id_, hoofdstuk=hf, paragraaf="begrippen", titel=titel, korteUitleg=kort,
                icoon=icoon, theorie=theorie, vragen=vragen)


def examen(nr, hf, hftitel, cursus, titel, icoon, vragen):
    return {"id": f"ex-h3-nederlands-{nr}", "hoofdstuk": hf, "hoofdstukTitel": hftitel,
            "paragraaf": "eind", "titel": f"Toets {nr} — {titel}",
            "vak": f"Nederlands · HAVO 3 (Cursus {cursus})", "icoon": icoon, "duurMin": 20,
            "vragen": vragen}


def schrijf(naam, kop, functie, obj):
    pad = os.path.join(DATA, naam)
    with open(pad, "w", encoding="utf-8") as f:
        f.write(f"/* {kop} */\n{functie}({json.dumps(obj, ensure_ascii=False, indent=2)});\n")
    print("geschreven:", pad, len(obj["vragen"]), "vragen")


def main():
    rng = random.Random("begrippen_c5_c7")
    schrijf("c7_begrippen.js", "Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 7)", "DURU.register",
            onderwerp("c7-begrippen", 7, "Begrippen & Kernconcepten — Cursus 7 (§2 & §3)",
                      "Alle spellingbegrippen uit §2 (trema, apostrof, accenten, cedille) en §3 (met of zonder n).",
                      "📖", C7_THEORIE, schud(C7_OEFEN, rng)))
    schrijf("c5_begrippen.js", "Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 5)", "DURU.register",
            onderwerp("c5-begrippen", 5, "Begrippen & Kernconcepten — Cursus 5 (§3 & §5)",
                      "Alle grammaticabegrippen uit §3 (samentrekking) en §5 (verwijzen).",
                      "📖", C5_THEORIE, schud(C5_OEFEN, rng)))
    schrijf("examen_51.js", "Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 7)", "DURU.registerExamen",
            examen(51, 7, "Cursus 7 — Spelling", 7, "Begrippentoets Cursus 7 (§2 & §3)", "📖", schud(C7_TOETS, rng)))
    schrijf("examen_52.js", "Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 5)", "DURU.registerExamen",
            examen(52, 5, "Cursus 5 — Grammatica", 5, "Begrippentoets Cursus 5 (§3 & §5)", "📖", schud(C5_TOETS, rng)))


if __name__ == "__main__":
    main()
