#!/usr/bin/env python3
"""Biologie HAVO 3 · H11 Voortplanting · §11.4 Je lijkt op ... (boek p. 146-151).
Schrijft havo3/biologie/js/data/h11_4.js + examen_15/16/17.js (ex-h3-biologie-15..17).
mc-volgorde willekeurig (geseed). Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen."""
import json, os, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'biologie', 'js', 'data')


def M(vraag, goed, fout, uitleg):
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": fout, "uitleg": uitleg}


def W(vraag, antwoord, uitleg):
    return {"type": "waaronwaar", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def I(vraag, antwoord, uitleg):
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def O(vraag, sleutels, min_, model, uitleg):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": min_,
            "modelantwoord": model, "uitleg": uitleg}


def plaats(vragen, rng):
    """Schud mc-opties tot: ≤40% op één index, geen periode 2–4, <60% '+1'-stappen."""
    mcs = [v for v in vragen if v["type"] == "mc"]
    for _ in range(5000):
        pos = [rng.randrange(len(v["_fout"]) + 1) for v in mcs]
        if max(pos.count(i) for i in set(pos)) / len(pos) > 0.4:
            continue
        if len(pos) < 6:  # gate 16 kijkt pas vanaf 6 mc
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



BEGRIPPEN = [
    ("chromosoom", "Een draadvormig onderdeel in de celkern dat voor een groot deel uit DNA bestaat en erfelijke informatie bevat."),
    ("DNA", "De stof waaruit chromosomen grotendeels bestaan en die de bouwbeschrijving van je lichaam bevat."),
    ("genoom", "Alle chromosomen van een organisme samen."),
    ("chromosomenpaar", "Twee dezelfde chromosomen die samen een paar vormen; een mens heeft er 23 in elke lichaamscel."),
    ("geslachtschromosomen", "Het 23ste chromosomenpaar, dat bepaalt of je een jongen of een meisje bent (XX of XY)."),
    ("bevruchting", "Het samensmelten van de kern van de eicel met de kern van de zaadcel, waardoor een bevruchte eicel met 46 chromosomen ontstaat."),
    ("gen", "Het stukje DNA dat informatie geeft voor één eigenschap; het is de DNA-code voor één eiwit."),
    ("allel", "Een variant van een gen, bijvoorbeeld het allel voor blauwe of bruine ogen."),
    ("genotype", "De informatie op al je genen samen."),
    ("fenotype", "Dat wat je ziet van een eigenschap, bijvoorbeeld blauwe ogen of blond haar."),
    ("erfelijke eigenschap", "Een eigenschap die je van je ouders hebt gekregen en die volledig door je genen wordt bepaald."),
    ("niet-erfelijke eigenschap", "Een eigenschap waarvan het fenotype volledig door de omgeving wordt bepaald, zoals een litteken of een tatoeage."),
    ("aangeboren aandoening", "Een afwijking of aandoening waarmee een baby wordt geboren."),
    ("syndroom van Down", "Een aandoening door een fout in het aantal chromosomen: de cellen hebben 47 in plaats van 46 chromosomen."),
    ("prenataal onderzoek", "Onderzoek vóór de geboorte, bijvoorbeeld om aandoeningen als het Downsyndroom op te sporen."),
    ("vruchtwaterpunctie", "Prenataal onderzoek waarbij een arts met een naald vruchtwater met cellen van de foetus uit de baarmoeder zuigt."),
    ("vlokkentest", "Prenataal onderzoek waarbij een arts cellen uit de placenta opzuigt en de chromosomen onderzoekt."),
    ("eeneiige tweeling", "Een tweeling met precies hetzelfde genotype, gebruikt in onderzoek naar erfelijkheid en omgeving."),
]

THEORIE = """
<h3>11.4 Je lijkt op ...</h3>
<h4>Waar zit jouw bouwbeschrijving?</h4>
<p>In de kernen van al je cellen zitten een soort 'draden': de <b>chromosomen</b>. Chromosomen bestaan voor een groot deel uit de stof <b>DNA</b>. Je DNA bevat de <b>bouwbeschrijving</b> van je lichaam: de kleur van je ogen, je bloedgroep, de vorm van je oorlel, de samenstelling van je verteringssappen, enzovoort.</p>
<div class="formule-box">
<b>Elke cel</b> heeft <b>23 chromosomenparen</b> = <b>46 chromosomen</b> in totaal.<br>
Alle chromosomen samen heten het <b>genoom</b>.
</div>
<p>Bij 22 paren zijn de vorm en de grootte van beide chromosomen gelijk. Het <b>23ste paar</b> bestaat uit de <b>geslachtschromosomen</b>: die bepalen of je een jongen of een meisje bent.</p>
<ul>
  <li><b>Vrouwen</b> hebben twee dezelfde geslachtschromosomen: <b>XX</b>.</li>
  <li><b>Mannen</b> hebben verschillende geslachtschromosomen: een <b>X</b> en een <b>Y</b> (<b>XY</b>).</li>
</ul>

<h4>Waardoor lijk je op je ouders?</h4>
<p>Je ouders hebben ieder de <b>helft</b> van hun chromosomen aan jou doorgegeven: je moeder via de <b>eicel</b>, je vader via de <b>zaadcel</b>.</p>
<ul>
  <li>Van elk chromosomenpaar komt één chromosoom in de eicel of zaadcel terecht. Een eicel en een zaadcel hebben dus <b>23 chromosomen</b>.</li>
  <li>Bij de <b>bevruchting</b> smelt de kern van de eicel samen met de kern van de zaadcel. De <b>bevruchte eicel</b> heeft 46 chromosomen: 23 van je vader en 23 van je moeder.</li>
  <li>Broers en zussen krijgen hun chromosomen ook van jullie ouders, maar <b>niet precies dezelfde sets</b> van 23. Daarom hebben ze niet precies dezelfde eigenschappen.</li>
</ul>
<div class="info-box tip"><span class="kop">Jongen of meisje?</span>
<p>Een <b>eicel</b> geeft altijd een <b>X</b>-chromosoom door. Een <b>zaadcel</b> geeft een <b>X</b> of een <b>Y</b> door. De zaadcel 'bepaalt' dus of het kindje een jongen (XY) of een meisje (XX) wordt.</p></div>

<h4>Hoe zitten de eigenschappen op de chromosomen?</h4>
<p>De meeste eigenschappen worden niet bepaald door een heel chromosomenpaar, maar door kleine stukjes van de chromosomen. Het stukje DNA dat informatie geeft voor één eigenschap heet een <b>gen</b>, bijvoorbeeld het gen voor oogkleur. Een variant van een gen heet een <b>allel</b>, bijvoorbeeld de allelen 'blauw' en 'bruin'.</p>
<ul>
  <li>Chromosomen komen in paren voor, dus een gen bestaat uit <b>twee allelen</b>: op elk chromosoom één.</li>
  <li>Voor veel eigenschappen zijn er meer dan twee allelen (voor oogkleur ook een allel voor groene ogen).</li>
  <li>Aan een eigenschap als oogkleur werken meestal <b>meerdere genen</b> samen.</li>
</ul>

<h4>Zijn alle eigenschappen erfelijk?</h4>
<div class="formule-box">
<b>Genotype</b> = de informatie op al je genen samen.<br>
<b>Fenotype</b> = dat wat je ziet van een eigenschap (blauwe ogen, blond haar).
</div>
<table class="nask">
<tr><th>Soort eigenschap</th><th>Wat bepaalt het fenotype?</th><th>Voorbeeld</th></tr>
<tr><td>Erfelijk</td><td>Alleen het genotype</td><td>oogkleur, vorm van je oorlel</td></tr>
<tr><td>Aanleg + omgeving</td><td>Genotype én omgeving</td><td>goed gitaar spelen (aanleg + oefenen)</td></tr>
<tr><td>Niet erfelijk</td><td>Alleen de omgeving</td><td>kleding, tatoeage, litteken</td></tr>
</table>

<h4>Hoe ontstaan aangeboren aandoeningen?</h4>
<p>Een baby met een afwijking is geboren met een <b>aangeboren aandoening</b>. Die kan op drie manieren ontstaan:</p>
<ol>
  <li><b>Schadelijke stoffen of ziekteverwekkers</b> die via de placenta bij het ongeboren kind komen. Voorbeeld: het rodehondvirus kan oogafwijkingen of gehoorproblemen geven.</li>
  <li><b>Een fout in het aantal chromosomen</b>. Voorbeeld: het <b>syndroom van Down</b>; die kinderen hebben <b>47</b> in plaats van 46 chromosomen, omdat ze zijn ontstaan uit een eicel met 24 in plaats van 23 chromosomen. Hoe ouder de vrouw, hoe groter de kans op een kind met het Downsyndroom.</li>
  <li><b>Een fout in de structuur van één chromosoom</b>, bijvoorbeeld een extra stukje DNA of een stukje dat van plaats is gewisseld. Voorbeeld: <b>kleurenblindheid</b>, een erfelijke aandoening.</li>
</ol>
<div class="info-box let-op"><span class="kop">Let op</span>
<p>Een litteken door een ongeluk is <b>niet erfelijk</b>. Kleurenblindheid is dat wel: je erft het van je ouders.</p></div>
<h4>Prenataal onderzoek</h4>
<p>Aandoeningen zoals het Downsyndroom kunnen al tijdens de zwangerschap worden ontdekt met <b>prenataal onderzoek</b> (onderzoek vóór de geboorte). Dat kan op twee manieren:</p>
<ul>
  <li><b>Vruchtwaterpunctie</b>: een arts zuigt met een naald een beetje vruchtwater uit de baarmoeder. Daarin zitten cellen van de foetus; de arts onderzoekt de chromosomen.</li>
  <li><b>Vlokkentest</b>: de arts zuigt cellen uit de <b>placenta</b> op. Ook daarin zitten cellen van de foetus, die worden onderzocht op fouten in de chromosomen.</li>
</ul>

<h4>Hoe bepaalt DNA je erfelijke eigenschappen?</h4>
<p>Elk chromosoom bevat een lang <b>DNA-molecuul</b> dat op een <b>wenteltrap</b> lijkt. Elke trede bestaat uit twee stoffen. De volgorde van vier soorten onderdelen vormt de <b>code voor het maken van eiwitten</b>. Een gen is de DNA-code voor <b>één eiwit</b>. Eiwitten regelen alles wat er in een cel gebeurt en bepalen zo je eigenschappen.</p>
<div class="info-box tip"><span class="kop">Voorbeeld: oogkleur</span>
<p>De kleur van je ogen wordt bepaald door het gen <b>OCA2</b> op chromosoom 15. Dit gen codeert voor het <b>P-eiwit</b>, dat pigment maakt en opslaat in je ogen. Veel pigment geeft bruine ogen, weinig pigment blauwe ogen. Mensen met blauwe ogen hebben een kleine verandering in het OCA2-gen, waardoor ze weinig P-eiwit aanmaken.</p></div>

<h4>Tweelingonderzoek (toepassen)</h4>
<p>Hoe zoek je uit of een eigenschap vooral door genen of door de omgeving wordt bepaald? Onderzoekers vergelijken <b>eeneiige tweelingen</b> (precies hetzelfde genotype) met <b>twee-eiige tweelingen</b> (net als gewone broers en zussen een verschillend genotype). Zijn eeneiige tweelingen vaker allebei roker dan twee-eiige, dan is roken voor een deel erfelijk bepaald. Vooral waardevol zijn eeneiige tweelingen die <b>gescheiden zijn opgegroeid</b>: hun genotype is gelijk, de omgeving verschillend. Verschillen in hun fenotype komen dus door de omgeving.</p>
"""

ONDERWERP_VRAGEN = [
    {"type": "mc", "niveau": 1, "vraag": "Hoeveel chromosomen zitten er in een gewone lichaamscel van een mens?",
     "_goed": "46, in 23 paren", "_fout": ["23, in 23 paren", "23, in 11 paren", "92, in 46 paren"],
     "uitleg": "Elke lichaamscel heeft 23 chromosomenparen, dus 46 chromosomen.", "hint": "Denk aan het aantal paren."},
    {"type": "mc", "niveau": 1, "vraag": "Welke geslachtschromosomen heeft een man?",
     "_goed": "Een X en een Y", "_fout": ["Twee X-chromosomen", "Twee Y-chromosomen", "Alleen een Y"],
     "uitleg": "Mannen hebben XY, vrouwen XX.", "hint": "Een man heeft twee verschillende geslachtschromosomen."},
    {"type": "mc", "niveau": 2, "vraag": "Wat is een allel?",
     "_goed": "Een variant van een gen", "_fout": ["Een stukje van een eiwit", "Een groep chromosomen", "Een onderdeel van de celkern"],
     "uitleg": "Een gen kan verschillende varianten hebben; zo'n variant heet een allel.", "hint": "Denk aan blauw en bruin bij oogkleur."},
    {"type": "mc", "niveau": 3, "vraag": "Een jongen heeft een litteken door een val van zijn fiets. Wat geldt voor dit litteken?",
     "_goed": "Het is niet erfelijk", "_fout": ["Het is erfelijk bepaald", "Het zit in zijn genotype", "Hij geeft het via zaadcellen door"],
     "uitleg": "Veranderingen door een ongeluk zijn niet erfelijk; het fenotype wordt hier door de omgeving bepaald.",
     "hint": "Wat heeft het litteken veroorzaakt?"},
    {"type": "waaronwaar", "niveau": 1, "vraag": "Een zaadcel bevat 23 chromosomen.",
     "antwoord": True, "uitleg": "Waar. Van ieder paar komt één chromosoom in de zaadcel terecht.", "hint": "Half zoveel als een lichaamscel."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "De eicel bepaalt of een kindje een jongen of een meisje wordt.",
     "antwoord": False, "uitleg": "Niet waar. De eicel geeft altijd een X door; de zaadcel (X of Y) bepaalt het geslacht.",
     "hint": "Welke cel kan X of Y doorgeven?"},
    {"type": "waaronwaar", "niveau": 2, "vraag": "Het fenotype is de informatie op al je genen samen.",
     "antwoord": False, "uitleg": "Niet waar. Dat is het genotype; het fenotype is wat je ziet van een eigenschap.", "hint": "Fenotype = wat je ziet."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "Een gen is de DNA-code voor één eiwit.",
     "antwoord": True, "uitleg": "Waar. Eiwitten regelen wat er in een cel gebeurt en bepalen zo je eigenschappen.", "hint": "Denk aan het P-eiwit."},
    {"type": "invoer", "niveau": 2, "vraag": "Bij het syndroom van Down hebben de cellen 47 in plaats van 46 ... Welk woord ontbreekt?",
     "antwoord": "chromosomen", "uitleg": "Het Downsyndroom ontstaat door een fout in het aantal chromosomen.", "hint": "Er is er een te veel."},
    {"type": "invoer", "niveau": 2, "vraag": "Een arts zuigt met een naald een beetje vruchtwater uit de baarmoeder om cellen van de foetus te onderzoeken. Hoe heet dit onderzoek?",
     "antwoord": "vruchtwaterpunctie|de vruchtwaterpunctie", "uitleg": "Bij een vruchtwaterpunctie wordt vruchtwater met cellen van de foetus onderzocht.", "hint": "Het onderzoek heeft het woord vruchtwater erin."},
]

EXAMENS = {
15: ("Begrippen en bouw", "🧬", [
    M("Wat zijn chromosomen?", "Draden in de celkern die grotendeels uit DNA bestaan",
      ["Eiwitten in het celplasma die de genen van de cel maken", "Kleine cellen waarin de erfelijke informatie ligt opgeslagen", "Ronde blaasjes die vrij in de celkern ronddrijven"],
      "Chromosomen zitten in de celkern en bestaan voor een groot deel uit DNA."),
    M("Hoeveel chromosomenparen heeft een lichaamscel van een mens?", "23", ["46", "22", "24"],
      "Elke cel heeft 23 paren, dus 46 chromosomen in totaal."),
    M("Hoe noem je alle chromosomen van een organisme samen?", "Het genoom", ["Het genotype", "Het fenotype", "Het allel"],
      "Alle chromosomen samen heten het genoom."),
    M("Welke geslachtschromosomen heeft een vrouw?", "XX", ["XY", "YY", "X"],
      "Vrouwen hebben twee dezelfde geslachtschromosomen: XX."),
    M("Wat is een gen?", "Een stukje DNA dat informatie geeft voor één eigenschap",
      ["Een heel chromosomenpaar met alle eigenschappen van je lichaam", "Een stof in de cel die haar de nodige energie geeft", "Een variant van een chromosoom in de celkern"],
      "Een gen is een klein stukje van een chromosoom dat informatie geeft voor één eigenschap."),
    M("Wat is het genotype?", "De informatie op al je genen samen",
      ["Alles wat je van een eigenschap kunt zien", "Het aantal chromosomen in je cellen", "De invloed van je omgeving op je lijf"],
      "Het genotype is de informatie op al je genen samen. Wat je ziet heet het fenotype."),
    M("Welke eigenschap is het fenotype van een persoon?", "Blauwe ogen", ["Het allel voor bruine ogen", "Het gen voor oogkleur", "Twee X-chromosomen"],
      "Het fenotype is wat je ziet van een eigenschap, zoals blauwe ogen. Gen en allel zitten in het genotype."),
    M("Hoe is het DNA-molecuul gebouwd?", "Als een wenteltrap met treden van twee stoffen",
      ["Als een rechte ketting van losse eiwitten in de kern", "Als een bolletje van opgerold vet in het celplasma", "Als een rij losse ronde cellen in het weefsel"],
      "Het DNA-molecuul lijkt op een wenteltrap; elke trede bestaat uit twee stoffen."),
    M("Hoeveel allelen heeft een mens van één gen?", "Twee, op elk chromosoom van het paar één",
      ["Eén, op het chromosoom van de vader", "Vier, twee van elke ouder", "Zoveel als er varianten bestaan"],
      "Chromosomen komen in paren voor, dus een gen bestaat uit twee allelen: op elk chromosoom één."),
    W("Chromosomen zitten in de celkern.", True, "Waar. In de kernen van al je cellen zitten chromosomen."),
    W("Een eicel bevat 46 chromosomen.", False, "Niet waar. Een eicel bevat 23 chromosomen, de helft van een lichaamscel."),
    W("Het 23ste chromosomenpaar bestaat uit de geslachtschromosomen.", True, "Waar. Bij 22 paren zijn beide chromosomen gelijk; het 23ste paar bepaalt het geslacht."),
    W("Een gen bestaat altijd uit precies één allel.", False, "Niet waar. Omdat chromosomen in paren voorkomen, bestaat een gen uit twee allelen."),
    W("Het genoom is het stukje DNA voor één eigenschap.", False, "Niet waar. Dat is een gen. Het genoom zijn alle chromosomen samen."),
    I("Alle chromosomen samen noem je het ____.", "genoom|het genoom", "Het genoom is de verzameling van alle chromosomen."),
    I("Een variant van een gen heet een ____.", "allel|het allel", "Zo'n variant, bijvoorbeeld blauw of bruin, noem je een allel."),
    I("Dat wat je ziet van een eigenschap heet het ____.", "fenotype|het fenotype", "Het fenotype is wat je van een eigenschap kunt zien."),
    I("Chromosomen bestaan voor een groot deel uit de stof ____.", "DNA|dna", "Chromosomen bestaan grotendeels uit DNA."),
    O("Leg uit wat het verschil is tussen genotype en fenotype.",
      ["genen", "ziet/zien/zichtbaar"], 2,
      "Het genotype is de informatie op al je genen samen; het fenotype is wat je ziet van een eigenschap.",
      "Genotype = informatie op de genen; fenotype = wat je ziet."),
    O("Beschrijf hoe het geslacht wordt bepaald door de geslachtschromosomen van man en vrouw.",
      ["XX", "XY"], 2,
      "Een vrouw heeft twee X-chromosomen (XX) en een man een X- en een Y-chromosoom (XY).",
      "Vrouw XX, man XY."),
]),
16: ("Functies en processen", "🧪", [
    M("Hoeveel chromosomen heeft de bevruchte eicel?", "46", ["23", "92", "47"],
      "De bevruchte eicel heeft 23 chromosomen van de vader en 23 van de moeder: 46."),
    M("Wat gebeurt er bij de bevruchting?", "De kern van de eicel smelt samen met de kern van de zaadcel",
      ["De eicel en de zaadcel verdelen hun chromosomen over twee cellen", "De zaadcel geeft alle 46 chromosomen aan de eicel", "De eicel haalt de chromosomen uit het bloed van de moeder"],
      "Bij de bevruchting smelten de kernen van eicel en zaadcel samen."),
    M("Welke cel bepaalt of een kind een jongen of een meisje wordt?", "De zaadcel, want die geeft een X of een Y door",
      ["De eicel, want die geeft een X of een Y door", "De zaadcel, want die geeft altijd een X door", "De eicel, want die geeft altijd een Y door"],
      "De eicel geeft altijd een X door. De zaadcel geeft een X of een Y door en bepaalt dus het geslacht."),
    M("Waarom hebben broers en zussen niet precies dezelfde eigenschappen?", "Ze krijgen niet precies dezelfde sets van 23 chromosomen",
      ["Ze krijgen alle chromosomen van maar één van beide ouders", "Ze krijgen elk een ander aantal chromosomen dan jij", "Ze krijgen hun genen pas na de geboorte van de ouders"],
      "Ieder kind krijgt een andere set van 23 chromosomen van de ouders."),
    M("Wat doen eiwitten in een cel?", "Ze regelen wat er in de cel gebeurt en bepalen zo je eigenschappen",
      ["Ze slaan alle erfelijke informatie van de hele cel op", "Ze vormen de treden van de wenteltrap van het DNA", "Ze verdelen de cel in tweeën bij de bevruchting"],
      "Eiwitten regelen alles wat er in een cel gebeurt en bepalen zo je eigenschappen."),
    M("Wat codeert het gen OCA2?", "Het P-eiwit, dat pigment maakt en opslaat",
      ["Het pigment zelf, dat de ogen een kleur geeft", "Het allel voor bruine ogen bij de mens", "Het X-chromosoom van de moeder of vader"],
      "OCA2 codeert voor het P-eiwit; dat zorgt voor het maken en opslaan van pigment in je ogen."),
    M("Waardoor hebben mensen met blauwe ogen blauwe ogen?", "Ze maken weinig P-eiwit en dus weinig pigment",
      ["Ze maken veel P-eiwit en dus veel pigment in de ogen", "Ze missen chromosoom 15 in al hun lichaamscellen", "Ze hebben een extra X-chromosoom in de cellen"],
      "Een kleine verandering in het OCA2-gen geeft weinig P-eiwit en dus weinig pigment: blauwe ogen."),
    M("Hoe werkt een vlokkentest?", "De arts zuigt cellen uit de placenta op en onderzoekt de chromosomen",
      ["De arts zuigt vruchtwater uit de baarmoeder en onderzoekt de chromosomen", "De arts maakt een echo van de foetus en telt de chromosomen", "De arts neemt bloed af bij de moeder en onderzoekt de chromosomen"],
      "Bij een vlokkentest worden cellen uit de placenta onderzocht op fouten in de chromosomen."),
    M("Waarom heeft een kind met het Downsyndroom 47 chromosomen?", "Het is ontstaan uit een eicel met 24 chromosomen",
      ["Het is ontstaan uit een zaadcel met 22 chromosomen", "Het heeft een stukje DNA te veel op één chromosoom", "Het heeft van beide ouders alle 46 chromosomen"],
      "Het kind is ontstaan uit een eicel met 24 in plaats van 23 chromosomen."),
    W("Een zaadcel geeft een X-chromosoom of een Y-chromosoom door.", True, "Waar. Daardoor bepaalt de zaadcel het geslacht."),
    W("Bij de bevruchting krijgt de bevruchte eicel 23 chromosomen van de vader en 23 van de moeder.", True, "Waar. Samen 46 chromosomen."),
    W("Een gen is de DNA-code voor meerdere verschillende eiwitten.", False, "Niet waar. Een gen is de DNA-code voor één eiwit."),
    W("Bij een vruchtwaterpunctie onderzoekt een arts cellen uit de placenta.", False, "Niet waar. Bij een vruchtwaterpunctie gaat het om cellen van de foetus in het vruchtwater; cellen uit de placenta onderzoek je met een vlokkentest."),
    W("Het rodehondvirus kan via de placenta bij het ongeboren kind komen.", True, "Waar. Schadelijke stoffen en ziekteverwekkers kunnen zo een aangeboren aandoening geven."),
    I("Bij de ____ smelt de kern van de eicel samen met de kern van de zaadcel.", "bevruchting|de bevruchting", "Bij de bevruchting ontstaat een bevruchte eicel."),
    I("Onderzoek vóór de geboorte heet ____ onderzoek.", "prenataal|prenatale", "Prenataal onderzoek vindt voor de geboorte plaats."),
    I("De code voor het maken van eiwitten zit in de volgorde van de onderdelen van het ____.", "DNA|dna|DNA-molecuul", "De volgorde van vier onderdelen in het DNA vormt de code."),
    I("Een eicel geeft altijd het ____-chromosoom door.", "X|x", "De eicel geeft altijd een X door."),
    O("Leg uit hoe je aan je chromosomen komt en waardoor je op je ouders lijkt.",
      ["eicel", "zaadcel", "helft/23"], 2,
      "Je moeder geeft de helft van haar chromosomen door via de eicel, je vader via de zaadcel. Bij de bevruchting smelten die samen tot 46 chromosomen.",
      "Eicel en zaadcel hebben elk 23 chromosomen."),
    O("Leg uit hoe het OCA2-gen de kleur van je ogen bepaalt.",
      ["eiwit", "pigment"], 2,
      "Het OCA2-gen is de code voor het P-eiwit. Dat eiwit maakt en slaat pigment op: veel pigment geeft bruine, weinig pigment blauwe ogen.",
      "Gen geeft code voor een eiwit; het eiwit maakt pigment."),
]),
17: ("Toepassen en redeneren", "🔍", [
    M("Een vrouw is bevrucht met een zaadcel met een Y-chromosoom. Wat wordt het kind?", "Een jongen, XY", ["Een meisje, XY", "Een jongen, YY", "Een meisje, XX"],
      "Een eicel geeft X, de zaadcel Y: het kind heeft XY en is een jongen."),
    M("Lisa kan goed tekenen. Wat zegt dit over haar fenotype?", "Het is het resultaat van aanleg en van oefenen",
      ["Het wordt alleen bepaald door haar genotype, niet door oefenen", "Het wordt alleen bepaald door haar omgeving, niet door genen", "Het is niet te verklaren door haar genen of omgeving"],
      "Voor eigenschappen als tekenen is de aanleg erfelijk, maar om goed te worden moet je oefenen: genotype en omgeving."),
    M("Een man heeft een tatoeage. Waarom geeft hij die niet door aan zijn kinderen?", "Het is een niet-erfelijke eigenschap die uit de omgeving komt",
      ["Het is een erfelijke eigenschap die in zijn genen zit", "Het zit in zijn Y-chromosoom maar niet in de zaadcel", "Het is een allel dat hij van zijn moeder kreeg"],
      "Een tatoeage bepaal je zelf; het fenotype komt volledig uit de omgeving en niet uit het genotype."),
    M("Een moeder van 40 is zwanger. Wat is waar over de kans op het Downsyndroom?", "De kans is groter dan bij een vrouw van 25",
      ["De kans is kleiner dan bij een vrouw van 25", "De kans is even groot als bij een vrouw van 25", "De kans hangt alleen af van het geslacht van het kind"],
      "Als een vrouw ouder wordt, heeft ze een grotere kans op een kind met het Downsyndroom."),
    M("Een kind wordt geboren met een oogafwijking. De moeder had tijdens de zwangerschap het rodehondvirus. Hoe is de afwijking ontstaan?", "Het virus is via de placenta bij het kind gekomen",
      ["Er zat een fout in het aantal chromosomen van het kind", "Er zat een fout in de structuur van een chromosoom", "Het kind heeft een extra X-chromosoom gekregen"],
      "Ziekteverwekkers kunnen via de placenta bij het ongeboren kind komen en een aangeboren aandoening geven."),
    M("Kleurenblindheid ontstaat door een fout in de structuur van één chromosoom. Wat betekent dit?", "Je erft het van je ouders",
      ["Je krijgt het door schadelijke stoffen tijdens de zwangerschap", "Je cellen hebben 47 chromosomen", "Je krijgt het door je omgeving"],
      "Kleurenblindheid is een erfelijke aandoening; je erft het van je ouders."),
    M("Twee eeneiige tweelingen zijn gescheiden opgegroeid en verschillen in lengte. Waardoor komt dat?", "Door verschillen in hun omgeving",
      ["Door verschillen in hun genotype", "Door verschillen in hun geslachtschromosomen", "Door verschillen in hun aantal chromosomen"],
      "Eeneiige tweelingen hebben hetzelfde genotype; verschillen in fenotype komen dus door de omgeving."),
    M("Waarom zijn eeneiige tweelingen die gescheiden zijn opgegroeid zo waardevol voor onderzoek?", "Hun genotype is gelijk en hun omgeving is verschillend",
      ["Hun genotype is verschillend en hun omgeving is gelijk", "Hun genotype en hun omgeving zijn allebei gelijk", "Ze hebben samen precies 46 chromosomen"],
      "Zo kun je zien hoeveel verschil de omgeving maakt bij hetzelfde genotype."),
    M("Een arts wil bij een zwangere vrouw de chromosomen van de foetus onderzoeken. Wat kan de arts doen?", "Een vruchtwaterpunctie of een vlokkentest",
      ["Een bloedtest bij de vader of een echo", "Een gehoortest of een bloedtest", "Een echo of een röntgenfoto"],
      "Prenataal onderzoek kan met een vruchtwaterpunctie of een vlokkentest."),
    W("Als eeneiige tweelingen vaker allebei roken dan twee-eiige tweelingen, is roken voor een deel erfelijk bepaald.", True,
      "Waar. Eeneiige tweelingen hebben precies hetzelfde genotype, twee-eiige niet."),
    W("Twee-eiige tweelingen hebben precies hetzelfde genotype.", False, "Niet waar. Twee-eiige tweelingen hebben net als gewone broers en zussen een verschillend genotype."),
    W("Een litteken na een ongeluk is een erfelijke eigenschap.", False, "Niet waar. Veranderingen door een ongeluk zijn niet erfelijk."),
    W("Een kind met het Downsyndroom heeft 47 chromosomen in zijn cellen.", True, "Waar. Dat is één meer dan de gewone 46."),
    W("Je bloedgroep wordt bepaald door je genen en is dus erfelijk.", True, "Waar. Of je gaat roken hangt daarentegen af van je omgeving."),
    I("Bij een ____ zuigt de arts met een naald vruchtwater uit de baarmoeder.", "vruchtwaterpunctie|de vruchtwaterpunctie", "In het vruchtwater zitten cellen van de foetus."),
    I("Het syndroom van Down ontstaat door een fout in het ____ chromosomen.", "aantal|aantal van de", "Er zijn 47 in plaats van 46 chromosomen."),
    I("Een baby die met een afwijking geboren wordt, heeft een ____ aandoening.", "aangeboren|een aangeboren", "Een aandoening waarmee je geboren bent is aangeboren."),
    I("Een zaadcel bepaalt het geslacht omdat die een X- of een ____-chromosoom doorgeeft.", "Y|y", "Een zaadcel geeft een X of een Y door."),
    O("Noem de drie manieren waarop een aangeboren aandoening kan ontstaan en geef bij één een voorbeeld.",
      ["schadelijke", "aantal", "structuur"], 3,
      "Door schadelijke stoffen of ziekteverwekkers (bijvoorbeeld rodehond), door een fout in het aantal chromosomen (Downsyndroom) of door een fout in de structuur van één chromosoom (kleurenblindheid).",
      "Drie oorzaken: stoffen/ziekteverwekkers, aantal, structuur."),
    O("Een eeneiige tweeling groeit gescheiden op. Wat kun je uit verschillen en overeenkomsten tussen hen leren?",
      ["genotype", "omgeving"], 2,
      "Hun genotype is gelijk, dus verschillen komen door de omgeving; overeenkomsten komen vooral door de genen.",
      "Gelijk genotype, andere omgeving."),
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)




def main():
    rng = random.Random('bio_h11_4')
    vragen = plaats([dict(v) for v in ONDERWERP_VRAGEN], rng)
    onderwerp = {
        "id": "bio-h11-4-je-lijkt-op", "hoofdstuk": 11, "paragraaf": "11.4",
        "titel": "Je lijkt op ...",
        "korteUitleg": "Chromosomen, genen en allelen, genotype en fenotype, aangeboren aandoeningen, prenataal onderzoek en hoe DNA je eigenschappen bepaalt.",
        "icoon": "🧬", "kleur": "h11-thema", "theorie": THEORIE, "vragen": vragen,
    }
    schrijf(os.path.join(ROOT, 'h11_4.js'),
            "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Biologie · H11 Voortplanting §11.4) — gegenereerd door tools/gen_biologie_h11_4.py */\n",
            "DURU.register(" + json.dumps(onderwerp, ensure_ascii=False, indent=2) + ");\n")
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {"id": f"ex-h3-biologie-{nr}", "hoofdstuk": 11, "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
              "paragraaf": "11.4", "titel": f"Toets {nr} — §11.4 {sub}", "vak": "Biologie · HAVO 3 (H11.4)",
              "icoon": icoon, "duurMin": 20, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie · H11.4) — gegenereerd door tools/gen_biologie_h11_4.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
