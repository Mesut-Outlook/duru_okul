#!/usr/bin/env python3
"""Nederlands HAVO 3 · Cursus 7 §2 Trema, apostrof, accenten en cedille (boek p. 244–245).
Schrijft havo3/nederlands/js/data/c7_2.js (onderwerp) + examen_23…29.js (ex-h3-nederlands-23…29).
mc-volgorde willekeurig (geseed), opnieuw geschud tot gate-regels 3/16 kloppen.
⚠️ Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'nederlands', 'js', 'data')


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


THEORIE = """
<h3>Waarom tekens op of bij letters?</h3>
<p>Om <b>uitspraakproblemen</b> te voorkomen gebruik je in het Nederlands soms een <b>trema</b>, een <b>apostrof</b>, een <b>accent</b> of een <b>cedille</b>.</p>

<h3>1. Het trema (¨)</h3>
<div class="formule-box">Het trema laat zien dat er met die klinker een <b>nieuwe lettergreep</b> begint: twee klinkers worden dan <b>niet</b> samen als één klank uitgesproken.</div>
<ul>
  <li>Om te voorkomen dat twee klinkers samen worden uitgesproken: <i>beïnvloeden, Indiër, reeën, variëren</i>.</li>
  <li>Geen trema als er geen uitspraakprobleem is: <i>beantwoord, deodorant, ontdooiing</i>.</li>
  <li>In sommige <b>leenwoorden</b>: <i>fröbelen, kür, patiënt</i>.</li>
</ul>
<div class="info-box let-op"><h4>Let op: samenstellingen</h4>
<p>In een <b>samenstelling</b> gebruik je geen trema, maar een <b>koppelteken</b>: <i>auto-eigenaar, bio-economie, maffia-achtig</i>.</p></div>

<h3>2. De apostrof (')</h3>
<ul>
  <li>Om uitspraakproblemen te voorkomen als je een <b>-s</b> schrijft achter woorden die eindigen op de <b>enkele klinkers a, i, o, u en y</b>: <i>buggy's, Emma's boek, ski's</i>.<br>Geen apostrof nodig in: <i>Lines tas, loverboys, niveaus</i>.</li>
  <li>Als <b>weglatingsteken</b>: <i>Hans' gitaar, 's-Hertogenbosch, 's morgens</i>.</li>
  <li>In afleidingen en meervouden van <b>afkortingen</b>: <i>cd's, sms'je, wc's</i>.</li>
  <li>In <b>verkleinwoorden op -y voorafgegaan door een medeklinker</b>: <i>pony'tje</i> (maar: <i>spraytje</i>).</li>
</ul>

<h3>3. Accenten</h3>
<p>Er zijn drie accenten; ze komen bijna alleen voor op de letter <b>e</b>:</p>
<table class="nask"><tr><th>accent</th><th>voorbeelden</th></tr>
<tr><td>accent aigu (é)</td><td><i>café, passé</i></td></tr>
<tr><td>accent grave (è)</td><td><i>caissière, fin de siècle</i></td></tr>
<tr><td>accent circonflexe (ê)</td><td><i>gemêleerd, moment suprême</i></td></tr></table>
<p>Veel minder vaak op andere letters: <i>twee à drie schepjes, maître</i>.</p>
<div class="info-box tip"><h4>Klemtoon-accent</h4>
<p>Het accent aigu gebruik je ook om een woord(deel) te <b>benadrukken</b>. Het staat dan op alle klinkers van de lettergreep, behalve bij drie opeenvolgende klinkers: dan krijgen alleen de eerste twee een accent (<i>móói, ééuw</i>).</p>
<div class="voorbeeld"><div class="vb-kop">Voorbeelden</div>
<p class="stap"><i>Een ongeluk moet je zien te voorkómen.</i></p>
<p class="stap"><i>Sander heeft geen twéé fietsen, maar drie!</i></p>
<p class="stap">Maar: <i>Kan een van jullie de boodschappen doen?</i> Je kunt <i>een</i> hier alleen als het cijfer 1 uitspreken, dus accenten zijn niet nodig.</p></div></div>

<h3>4. De cedille (ç)</h3>
<p>De cedille onder de c zorgt ervoor dat een <b>c als s</b> klinkt wanneer die voor een <b>a, o of u</b> staat: <i>Curaçao, François, reçu</i>.<br>Normaal klinkt de c in die gevallen als <b>k</b>: <i>cacao, clubrecord, cursus</i>.</p>
"""

ONDERWERP_VRAGEN = [
    {"type": "mc", "niveau": 1, "vraag": "Waarom gebruik je trema's, apostrofs, accenten en cedilles?",
     "_goed": "Om uitspraakproblemen te voorkomen",
     "_fout": ["Om meervouden en verkleinwoorden te maken", "Om de woordsoort aan te geven", "Om leenwoorden te herkennen"],
     "uitleg": "Volgens de theorie gebruik je deze tekens om uitspraakproblemen te voorkomen.",
     "hint": "Denk aan hoe je het woord zonder het teken zou uitspreken."},
    {"type": "mc", "niveau": 1, "vraag": "Kies de juiste spelling: <i>Mijn opa komt uit ...</i> (het land met de hoofdstad Rome)",
     "_goed": "Italië", "_fout": ["Italie", "Italïe", "Itali-e"],
     "uitleg": "Itali-ë: met het trema begint een nieuwe lettergreep; zonder trema lees je 'ie' als één klank.",
     "hint": "Spreek het woord in lettergrepen uit."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "In <i>Emma's boek</i> voorkomt de apostrof dat je <i>Emmas</i> met een korte a uitspreekt.",
     "antwoord": True, "uitleg": "Waar. Emma eindigt op de enkele klinker a; met de apostrof blijft de a lang.",
     "hint": "Op welke letter eindigt Emma?"},
    {"type": "waaronwaar", "niveau": 1, "vraag": "In samenstellingen zoals <i>zonne-energie</i> gebruik je een trema.",
     "antwoord": False, "uitleg": "Niet waar. In samenstellingen gebruik je bij klinkerbotsing een koppelteken, geen trema.",
     "hint": "Kijk naar het streepje in het woord."},
    {"type": "invoer", "niveau": 2, "vraag": "Schrijf correct over (er ontbreekt een trema): <i>Australier</i>",
     "antwoord": "Australiër", "uitleg": "Australi-ër: het trema op de e laat zien dat 'ie' hier geen klank vormt.",
     "hint": "Vergelijk met Indiër."},
    {"type": "invoer", "niveau": 2, "vraag": "Schrijf het meervoud van <i>auto</i>.",
     "antwoord": "auto's", "uitleg": "Auto eindigt op de enkele klinker o: auto's, zodat de o lang klinkt.",
     "hint": "Eindigt het woord op a, i, o, u of y?"},
    {"type": "mc", "niveau": 2, "vraag": "Wat doet een cedille?",
     "_goed": "Een c klinkt als s voor a, o of u",
     "_fout": ["Een c klinkt als k voor e of i", "Een s klinkt als z voor a, o of u", "Een c wordt stil voor a, o of u"],
     "uitleg": "De cedille (ç) zorgt dat de c voor a, o of u als s klinkt: Curaçao, François, reçu.",
     "hint": "Denk aan François."},
    {"type": "mc", "niveau": 1, "vraag": "Welk accent staat er op de e in <i>café</i>?",
     "_goed": "accent aigu", "_fout": ["accent grave", "accent circonflexe", "trema"],
     "uitleg": "In café staat een accent aigu (é), het streepje van linksonder naar rechtsboven.",
     "hint": "Aigu = é, grave = è, circonflexe = ê."},
]

EXAMENS = {
23: ("Trema", "🔤", [
    M("Kies de juiste spelling van het meervoud van <i>idee</i>.", "ideeën", ["ideeen", "idee-en", "ideëen"],
      "I-dee-ën: het trema laat zien dat met de laatste e een nieuwe lettergreep begint. Zonder trema lees je 'eee' als één klank."),
    M("Kies het juist gespelde woord voor 'gedichten als kunstvorm'.", "poëzie", ["poezie", "poézie", "poeëzie"],
      "Po-ë-zie: zonder trema zou je 'oe' als één klank lezen (poe-zie)."),
    M("Kies de juiste spelling: <i>Reclame kan je keuzes sterk ...</i>", "beïnvloeden", ["beinvloeden", "be-invloeden", "bëinvloeden"],
      "Be-ïn-vloe-den: zonder trema lees je 'ei' als één klank. Be- is een voorvoegsel, geen samenstelling, dus geen koppelteken."),
    M("Hoe schrijf je iemand die uit India komt?", "Indiër", ["Indier", "Indiëer", "India-er"],
      "Indi-ër: het trema op de e voorkomt dat je 'ie' als één klank leest."),
    M("Kies de juiste spelling: <i>In het bos zagen we drie ...</i> (meervoud van ree)", "reeën", ["reeen", "ree-en", "reeëen"],
      "Ree-ën: het trema laat zien dat de laatste e een nieuwe lettergreep begint."),
    W("In het woord <i>beantwoord</i> is een trema nodig, omdat de e en de a botsen.", False,
      "Niet waar. 'ea' wordt niet als één klank uitgesproken; er is geen uitspraakprobleem, dus beantwoord zonder trema."),
    W("Het trema in <i>variëren</i> voorkomt dat je 'ie' als één klank leest.", True,
      "Waar. Zonder trema lees je va-rie-ren; met trema spreek je va-ri-ë-ren uit."),
    I("Schrijf het woord correct over (er ontbreekt een trema): <i>naief</i>", "naïef",
      "Na-ïef: zonder trema lees je 'ai' als één klank."),
    I("Schrijf correct over: <i>reunie</i>", "reünie",
      "Re-ü-nie: zonder trema lees je 'eu' als één klank (zoals in 'neus')."),
    M("In welk woord is <b>geen</b> trema nodig?", "deodorant", ["coördinatie", "egoïst", "ruïne"],
      "In deodorant vormen e en o samen geen klank, dus er is geen uitspraakprobleem. De andere woorden hebben wel een trema."),
    M("Welk leenwoord is juist gespeld?", "fröbelen", ["frobelen", "fröbbelen", "freubelen"],
      "Fröbelen is een leenwoord dat volgens de theorie een trema krijgt (net als kür en patiënt)."),
    M("Kies de juiste spelling: <i>De schaatsster reed een prachtige vrije ...</i>", "kür", ["kur", "kuur", "kûr"],
      "Kür is een leenwoord met een trema (umlaut), genoemd in de theorie."),
    M("Kies de juiste spelling: <i>De huisarts heeft vandaag twintig ... gezien.</i>", "patiënten", ["patienten", "pati-enten", "patiénten"],
      "Pati-ën-ten: zonder trema lees je 'ie' als één klank."),
    W("In de samenstelling <i>auto-eigenaar</i> gebruik je een koppelteken in plaats van een trema.", True,
      "Waar. In samenstellingen gebruik je bij klinkerbotsing een koppelteken, geen trema."),
    W("Het woord <i>ontdooiing</i> schrijf je met een trema op de i: <i>ontdooiïng</i>.", False,
      "Niet waar. Volgens de theorie is in ontdooiing geen trema nodig: er ontstaat geen uitspraakprobleem."),
    I("Schrijf het meervoud van <i>knie</i>.", "knieën",
      "Knie-ën: het trema laat zien dat de laatste e een nieuwe lettergreep begint."),
    M("Wat is de functie van een trema?", "Het laat zien dat een nieuwe lettergreep begint",
      ["Het geeft aan dat je de klinker lang uitspreekt", "Het laat zien welke lettergreep de klemtoon krijgt", "Het maakt van een c een s-klank"],
      "Het trema voorkomt dat twee klinkers samen als één klank worden uitgesproken: er begint een nieuwe lettergreep."),
    M("Kies de juiste spelling: <i>Het werelddeel waar China ligt heet ...</i>", "Azië", ["Azie", "Aziè", "Aziee"],
      "Azi-ë: zonder trema lees je 'ie' als één klank."),
    O("Leg uit waarom je <i>geüpload</i> met een trema schrijft.",
      ["eu", "klank/uitspraak/uitgesproken/lezen/lees"], 1,
      "Zonder trema zou je 'eu' als één klank lezen (zoals in 'neus'). Het trema laat zien dat de u bij een nieuwe lettergreep hoort: ge-üp-load.",
      "Het trema voorkomt dat e en u samen als de klank 'eu' worden uitgesproken."),
    O("Leg uit waarom <i>discussiëren</i> een trema heeft, maar <i>discussie</i> niet.",
      ["ie", "lettergreep/klank/uitspraak/uitgesproken"], 1,
      "In discussiëren zou je 'ie' + e verkeerd samen lezen; het trema laat zien dat de ë een nieuwe lettergreep begint (dis-cus-si-ë-ren). In discussie is 'ie' gewoon één klank, daar is geen probleem.",
      "Een trema is alleen nodig als er een uitspraakprobleem is."),
]),
24: ("Apostrof", "✍️", [
    M("Kies de juiste meervoudsvorm van <i>buggy</i>.", "buggy's", ["buggys", "buggies", "buggy-s"],
      "Buggy eindigt op de enkele klinker y; bij een -s zet je dan een apostrof: buggy's."),
    M("Kies de juiste spelling: <i>Dat is ... boek.</i> (het boek van Emma)", "Emma's", ["Emmas", "Emma-s", "Emmaas"],
      "Emma eindigt op de enkele klinker a: Emma's boek, zodat de a lang blijft."),
    M("Hoe schrijf je het meervoud van <i>ski</i>?", "ski's", ["skis", "skies", "ski-s"],
      "Ski eindigt op de enkele klinker i: ski's."),
    M("Welk meervoud is juist gespeld?", "niveaus", ["niveau's", "niveaux", "niveaus'"],
      "Niveau eindigt niet op een enkele klinker (eau); er is geen uitspraakprobleem, dus geen apostrof: niveaus."),
    M("Kies de juiste spelling: <i>Ik leen ... tas.</i> (de tas van Line)", "Lines", ["Line's", "Lines'", "Linès"],
      "Line eindigt op een e. Dat is niet een van de klinkers a, i, o, u, y, dus geen apostrof: Lines tas."),
    M("Kies de juiste spelling: <i>Dit is ... gitaar.</i> (de gitaar van Hans)", "Hans'", ["Hans's", "Hanses", "Hans-s"],
      "Hans eindigt al op een s; de bezits-s wordt weggelaten en de apostrof is het weglatingsteken: Hans' gitaar."),
    M("Hoe schrijf je de naam van de hoofdstad van Noord-Brabant?", "'s-Hertogenbosch", ["'s Hertogenbosch", "s'-Hertogenbosch", "s-Hertogenbosch"],
      "'s staat voor 'des' (weglatingsteken). In deze plaatsnaam volgt een koppelteken: 's-Hertogenbosch."),
    M("Kies de juiste spelling: <i>Sem gaat ... altijd hardlopen.</i> (in de ochtend)", "'s morgens", ["s'morgens", "smorgens", "'s-morgens"],
      "'s morgens = des morgens. De apostrof staat vóór de s (weglatingsteken), zonder koppelteken."),
    M("Kies de juiste meervoudsvorm van de afkorting <i>cd</i>.", "cd's", ["cds", "cd-s", "ceedees"],
      "In meervouden van afkortingen gebruik je een apostrof: cd's."),
    M("Wat is het juiste verkleinwoord van <i>sms</i>?", "sms'je", ["smsje", "sms-je", "sms'tje"],
      "In afleidingen van afkortingen gebruik je een apostrof: sms'je."),
    M("Kies het juiste verkleinwoord van <i>pony</i>.", "pony'tje", ["ponytje", "pony-tje", "poneytje"],
      "Pony eindigt op -y met een medeklinker (n) ervoor: dan schrijf je een apostrof: pony'tje."),
    M("Kies het juiste verkleinwoord van <i>spray</i>.", "spraytje", ["spray'tje", "spray-tje", "sprayje"],
      "In spray staat een klinker (a) vóór de y, dus geen apostrof: spraytje."),
    W("In <i>loverboys</i> is geen apostrof nodig, omdat het woord niet op een enkele klinker eindigt.", True,
      "Waar. Loverboy eindigt op 'oy'; er is geen uitspraakprobleem, dus loverboys zonder apostrof."),
    W("Het meervoud van <i>wc</i> schrijf je als <i>wcs</i>, zonder apostrof.", False,
      "Niet waar. In meervouden van afkortingen gebruik je een apostrof: wc's."),
    W("Het verkleinwoord van <i>cowboy</i> is <i>cowboy'tje</i>, omdat het woord op een y eindigt.", False,
      "Niet waar. De apostrof komt alleen bij -y na een medeklinker (pony'tje). In cowboy staat een o vóór de y: cowboytje."),
    W("In <i>'s avonds</i> is de apostrof een weglatingsteken.", True,
      "Waar. 's avonds staat voor 'des avonds'; de apostrof geeft aan dat er letters zijn weggelaten."),
    M("In welk geval is de apostrof een <b>weglatingsteken</b>?", "zo'n", ["opa's", "tv's", "pony'tje"],
      "Zo'n = zo een: er zijn letters weggelaten. Bij opa's, tv's en pony'tje voorkomt de apostrof een uitspraakprobleem of hoort hij bij een afkorting."),
    M("Welk rijtje meervouden (opa, kiwi, bureau) is helemaal goed gespeld?", "opa's – kiwi's – bureaus",
      ["opas – kiwi's – bureau's", "opa's – kiwis – bureau's", "opa's – kiwi's – bureau's"],
      "Opa en kiwi eindigen op een enkele klinker (apostrof); bureau eindigt op 'eau' (geen apostrof)."),
    O("Leg uit waarom je <i>foto's</i> met een apostrof schrijft.",
      ["klinker", "uitspraak/uitgesproken/lees/klank/kort/lang"], 1,
      "Foto eindigt op de enkele klinker o. Zonder apostrof zou je fotos lezen met een korte o; de apostrof zorgt dat de o lang blijft.",
      "Bij een -s achter de enkele klinkers a, i, o, u en y zet je een apostrof om uitspraakproblemen te voorkomen."),
    O("Waarom schrijf je <i>Hans' mobiel</i> en niet <i>Hans's mobiel</i>?",
      ["weglating/weggelaten/weglatingsteken/valt weg", "eindigt/sisklank/al op een"], 1,
      "Hans eindigt al op een s. De bezits-s wordt weggelaten en de apostrof is het weglatingsteken.",
      "Bij namen op een s(-klank) laat je de bezits-s weg en schrijf je alleen een apostrof."),
]),
25: ("Accenten en cedille", "🎨", [
    M("Kies de juiste spelling: <i>We drinken koffie in het ...</i>", "café", ["cafe", "cafè", "cafê"],
      "Café schrijf je met een accent aigu (é)."),
    M("Kies de juiste spelling: <i>De ... scant je boodschappen.</i>", "caissière", ["caissiere", "caissiére", "caissiêre"],
      "Caissière schrijf je met een accent grave (è)."),
    M("Welk accent staat er in <i>gemêleerd</i>?", "accent circonflexe", ["accent grave en aigu", "accent aigu op de e", "accent grave op de e"],
      "Het dakje op de e (ê) is een accent circonflexe."),
    M("Welke drie accenten noemt de theorie?", "aigu, grave en circonflexe",
      ["aigu, trema en cedille", "grave, cedille en apostrof", "circonflexe, trema en aigu"],
      "De drie accenten zijn accent aigu (é), accent grave (è) en accent circonflexe (ê). Trema en cedille zijn geen accenten."),
    M("Kies de juiste spelling van de Franse uitdrukking voor 'het hoogtepunt'.", "moment suprême", ["moment supreme", "moment suprème", "moment supréme"],
      "Moment suprême schrijf je met een accent circonflexe (ê)."),
    M("Kies de juiste spelling: <i>Je hebt twee ... drie schepjes suiker nodig.</i>", "à", ["a", "á", "â"],
      "In 'twee à drie' (= ongeveer twee of drie) staat een accent grave op de a."),
    M("Kies de juiste spelling: <i>Ik woon op ... en mijn vriend woont op Aruba.</i>", "Curaçao", ["Curacao", "Curaçáo", "Curacào"],
      "In Curaçao klinkt de c voor de a als s; daarom krijgt die c een cedille."),
    M("Wat doet de cedille onder de c in <i>François</i>?", "De c klinkt als een s",
      ["De c klinkt als een k", "De c klinkt als een g", "De c wordt niet uitgesproken"],
      "Door de cedille klinkt de c voor een a, o of u als s."),
    W("Accenten komen bijna alleen voor op de letter e.", True,
      "Waar. Volgens de theorie staan accenten bijna altijd op de e; veel minder vaak op andere letters (à, maître)."),
    W("In <i>Kan een van jullie de boodschappen doen?</i> moet je <i>één</i> schrijven, want het gaat om één persoon.", False,
      "Niet waar. Je kunt een hier alleen als het cijfer 1 uitspreken; daarom zijn accenten niet nodig."),
    W("In <i>cacao</i> en <i>cursus</i> klinkt de c als een k, dus is er geen cedille nodig.", True,
      "Waar. Normaal klinkt de c voor a, o en u als k; alleen als hij als s moet klinken, komt er een cedille."),
    W("Een klemtoonteken op drie opeenvolgende klinkers zet je op alle drie: <i>móóí</i>.", False,
      "Niet waar. Bij drie opeenvolgende klinkers krijgen alleen de eerste twee een accent: móói."),
    I("Schrijf het woord correct over met het juiste accent: <i>premiere</i> (de eerste voorstelling van een film)", "première",
      "Première schrijf je met een accent grave (è)."),
    I("Schrijf correct met accenten: <i>creme fraiche</i>", "crème fraîche",
      "Crème fraîche: accent grave op de e van crème, accent circonflexe op de i van fraîche."),
    I("Schrijf correct met cedille: <i>recu</i> (een bewijs van betaling)", "reçu",
      "In reçu klinkt de c voor de u als s, dus krijgt hij een cedille."),
    M("Welke zin bevat een accent dat een woord <b>benadrukt</b>?", "Sander heeft geen twéé fietsen, maar drie!",
      ["Na de film aten we saté met heel veel pindasaus.", "De vriendelijke caissière gaf me het bonnetje mee.", "Mijn oom draagt vandaag een gemêleerde wollen trui."],
      "In twéé staat het accent aigu om het woord te benadrukken. In saté, caissière en gemêleerd hoort het accent bij de spelling van het woord."),
    M("Wat is het verschil tussen <i>vóórkomen</i> en <i>voorkómen</i>?", "vóórkomen = gebeuren, voorkómen = verhinderen",
      ["vóórkomen = verhinderen, voorkómen = gebeuren", "beide betekenen hetzelfde, alleen de klemtoon verschilt", "vóórkomen = vooraan staan, voorkómen = te laat zijn"],
      "Het klemtoonaccent maakt het verschil duidelijk: iets kan vóórkomen (gebeuren); een ongeluk moet je voorkómen (verhinderen)."),
    M("Waarom heeft <i>façade</i> een cedille?", "Zonder cedille klinkt de c voor een a als k",
      ["Zonder cedille klinkt de c voor een a als s", "De cedille geeft aan waar de klemtoon ligt", "De cedille laat zien dat de a lang is"],
      "Voor a, o en u klinkt de c normaal als k. In façade moet hij als s klinken, dus komt er een cedille."),
    O("Leg uit waarom je <i>zes</i> met een accent schrijft in: <i>Hij heeft geen vier, maar zés kinderen!</i>",
      ["nadruk/benadruk/klemtoon", "woord/getal/aantal"], 1,
      "Het accent aigu benadrukt het woord: hij heeft niet vier, maar wel zés kinderen.",
      "Het accent aigu gebruik je ook om een woord(deel) te benadrukken."),
    O("Leg uit waarom je <i>een</i> zonder accenten schrijft in <i>een van de drie</i>.",
      ["cijfer/getal/telwoord", "alleen/maar op één manier/niet anders/geen verwarring"], 1,
      "Je kunt een hier alleen als het cijfer 1 uitspreken; er is geen verwarring met het lidwoord, dus accenten zijn niet nodig.",
      "Een accent is alleen nodig als je een woord anders zou kunnen lezen."),
]),
26: ("Koppelteken of trema", "🔗", [
    M("Kies de juiste spelling van de samenstelling van <i>auto</i> + <i>eigenaar</i>.", "auto-eigenaar", ["autoeigenaar", "autoëigenaar", "auto-ëigenaar"],
      "In een samenstelling gebruik je bij klinkerbotsing een koppelteken, geen trema: auto-eigenaar."),
    M("Kies de juiste spelling: <i>zee</i> + <i>egel</i>", "zee-egel", ["zeeëgel", "zeeegel", "zee-ëgel"],
      "Samenstelling met klinkerbotsing: koppelteken. Dus zee-egel."),
    M("Kies de juiste spelling: <i>bio</i> + <i>economie</i>", "bio-economie", ["bioeconomie", "bioëconomie", "bio-ëconomie"],
      "Samenstelling met klinkerbotsing (o + e): koppelteken, geen trema."),
    M("Kies de juiste spelling: <i>maffia</i> + <i>achtig</i>", "maffia-achtig", ["maffiaachtig", "maffiaächtig", "maffia-ächtig"],
      "Twee a's botsen in een samenstelling: koppelteken, zoals in de theorie: maffia-achtig."),
    I("Schrijf de samenstelling van <i>zonne</i> + <i>energie</i> correct.", "zonne-energie",
      "In een samenstelling met klinkerbotsing (e + e) zet je een koppelteken."),
    I("Schrijf de samenstelling van <i>radio</i> + <i>uitzending</i> correct.", "radio-uitzending",
      "O + u botsen in de samenstelling: koppelteken."),
    W("In samenstellingen gebruik je bij klinkerbotsing een koppelteken en geen trema.", True,
      "Waar. Dat staat in de theorie: auto-eigenaar, bio-economie, maffia-achtig."),
    W("Het woord <i>coördinatie</i> is een samenstelling en krijgt daarom een koppelteken: <i>co-ordinatie</i>.", False,
      "Niet waar. Coördinatie is geen samenstelling van twee zelfstandige woorden; je schrijft het met een trema."),
    W("In <i>taxichauffeur</i> is geen koppelteken nodig, omdat er geen klinkers botsen.", True,
      "Waar. Taxi + chauffeur: i en ch botsen niet, dus taxichauffeur aan elkaar."),
    M("Welke samenstelling met <i>taxi</i> is juist gespeld?", "taxi-industrie", ["taxiïndustrie", "taxiindustrie", "taxi-ïndustrie"],
      "Taxi + industrie: twee i's botsen in een samenstelling, dus een koppelteken."),
    M("In welk woord is het koppelteken <b>fout</b> gebruikt?", "radio-zender", ["radio-omroep", "auto-ongeluk", "piano-uitvoering"],
      "In radiozender botsen geen klinkers (o + z), dus geen koppelteken. De andere woorden hebben klinkerbotsing."),
    M("Kies de juiste spelling van het voltooid deelwoord van <i>interesseren</i>.", "geïnteresseerd", ["ge-interesseerd", "geinteresseerd", "ge-ïnteresseerd"],
      "Ge- is een voorvoegsel, geen los woord: geen koppelteken. Zonder trema lees je 'ei', dus: geïnteresseerd."),
    M("Kies de juiste spelling van het voltooid deelwoord van <i>isoleren</i>.", "geïsoleerd", ["geisoleerd", "ge-isoleerd", "geïsoléerd"],
      "Zonder trema lees je 'ei' als één klank; ge- is een voorvoegsel, dus trema: geïsoleerd."),
    M("Kies de juiste spelling van het voltooid deelwoord van <i>accepteren</i>.", "geaccepteerd", ["geäccepteerd", "ge-accepteerd", "geaccepteërd"],
      "E en a vormen samen geen klank, dus er is geen uitspraakprobleem: geaccepteerd zonder trema."),
    M("Kies de juiste spelling van het voltooid deelwoord van <i>kopiëren</i>.", "gekopieerd", ["gekopiëerd", "gekopiëërd", "ge-kopieerd"],
      "In gekopieerd lees je vanzelf ko-pi-eerd; er is geen uitspraakprobleem, dus geen trema (anders dan in kopiëren)."),
    M("Welk rijtje met trema, koppelteken of geen van beide is helemaal goed gespeld?", "poëzie – zee-egel – geaccepteerd",
      ["poezie – zee-egel – geaccepteerd", "poëzie – zeeëgel – geaccepteerd", "poëzie – zee-egel – geäccepteerd"],
      "Poëzie (trema), zee-egel (samenstelling: koppelteken), geaccepteerd (geen uitspraakprobleem)."),
    W("In het woord <i>buiig</i> (met veel regenbuien) is geen trema nodig.", True,
      "Waar. Buiig schrijf je zonder trema: 'ii' lees je nooit als één klank, dus er is geen uitspraakprobleem."),
    M("Welk woord is <b>fout</b> gespeld?", "Indier", ["Indiër", "ideeën", "reünie"],
      "Juist is Indiër: zonder trema lees je 'ie' als één klank."),
    O("Maak twee samenstellingen met <i>radio</i> als eerste deel: één met en één zonder streepje. Leg kort uit waarom.",
      ["radio-uitzending/radio-omroep/radio-installatie/radio-interview/radio-opname/radio-actie/radio-uitvoering",
       "radiozender/radiostation/radioprogramma/radiotoestel/radiomaker/radioreclame/radiospot/radiobericht/radioquiz",
       "klinker/botsen/botsing/uitspraak"], 2,
      "Radio-uitzending: de o en de u botsen, dus een koppelteken. Radiozender: o en z botsen niet, dus aan elkaar.",
      "In een samenstelling zet je alleen een koppelteken als er klinkers botsen."),
    O("Leg uit waarom je <i>auto-eigenaar</i> met een koppelteken schrijft en <i>beïnvloeden</i> met een trema.",
      ["samenstelling", "voorvoegsel/afleiding/geen samenstelling/één woord/1 woord"], 1,
      "Auto-eigenaar is een samenstelling van twee woorden (auto + eigenaar): bij klinkerbotsing een koppelteken. Beïnvloeden is geen samenstelling (be- is een voorvoegsel), dus daar gebruik je een trema.",
      "Koppelteken in samenstellingen; trema in andere woorden."),
]),
27: ("Foutenjacht in zinnen", "🔍", [
    M("Welk woord in deze zin is fout gespeld? <i>Tijdens de reünie lazen de oud-leerlingen poezie voor in het café.</i>",
      "poezie", ["reünie", "café", "oud-leerlingen"],
      "Juist is poëzie: zonder trema lees je 'oe' als één klank."),
    M("Welk woord in deze zin is fout gespeld? <i>De caissière gaf François het reçu van zijn twee cds.</i>",
      "cds", ["caissière", "François", "reçu"],
      "Meervoud van een afkorting krijgt een apostrof: cd's."),
    M("Welk woord in deze zin is fout gespeld? <i>s Avonds kijkt mijn opa graag naar oude foto's van Curaçao.</i>",
      "s Avonds", ["opa", "foto's", "Curaçao"],
      "Juist is 's Avonds: de apostrof is een weglatingsteken (des avonds) en staat vóór de s."),
    M("Welk woord in deze zin is fout gespeld? <i>Na het auto-ongeluk moest de autoeigenaar zijn paraplu's en ski's ophalen.</i>",
      "autoeigenaar", ["auto-ongeluk", "paraplu's", "ski's"],
      "Juist is auto-eigenaar: samenstelling met klinkerbotsing, dus een koppelteken."),
    M("Welk woord in deze zin is fout gespeld? <i>De Indiër bestelde in het restaurant crème fraiche bij zijn soep.</i>",
      "fraiche", ["Indiër", "restaurant", "crème"],
      "Juist is fraîche, met een accent circonflexe op de i."),
    M("Welk woord in deze zin is fout gespeld? <i>In de krant stonden twee artikelen over de financien van de gemeente en de knieën van de keeper.</i>",
      "financien", ["artikelen", "gemeente", "knieën"],
      "Juist is financiën: zonder trema lees je 'ie' als één klank."),
    M("Welk woord in deze zin is fout gespeld? <i>Emmas vader heeft geen twéé, maar drie auto's en een pony'tje.</i>",
      "Emmas", ["twéé", "auto's", "pony'tje"],
      "Juist is Emma's: Emma eindigt op de enkele klinker a."),
    M("Welk woord in deze zin is fout gespeld? <i>De opticien in 's-Hertogenbosch verkoopt ook zonnebrillen.</i>",
      "opticien", ["'s-Hertogenbosch", "zonnebrillen", "verkoopt"],
      "Juist is opticiën: zonder trema lees je 'ie' als één klank."),
    W("Deze zin is foutloos gespeld: <i>Op de markt kochten we kiwi's, mango's en een bosje radijs voor de baby's van de buren.</i>", True,
      "Waar. Kiwi, mango en baby eindigen op een enkele klinker (i, o, y): kiwi's, mango's, baby's."),
    W("Deze zin is foutloos gespeld: <i>Mijn zus werkt als caissiere bij een supermarkt in Azië.</i>", False,
      "Niet waar. Juist is caissière, met een accent grave."),
    W("Deze zin is foutloos gespeld: <i>De conciërge heeft de foto's van de schoolreünie geüpload.</i>", True,
      "Waar. Conciërge, foto's, schoolreünie en geüpload zijn allemaal juist gespeld."),
    W("Deze zin is foutloos gespeld: <i>Het journaal meldde in een radio-uitzending dat er reeen op de snelweg liepen.</i>", False,
      "Niet waar. Juist is reeën: het trema laat zien dat de laatste e een nieuwe lettergreep begint."),
    I("Verbeter het fout gespelde woord in de zin: <i>De gemeente wil de burgers niet beinvloeden met reclame.</i>", "beïnvloeden",
      "Be-ïn-vloe-den: zonder trema lees je 'ei' als één klank."),
    I("Verbeter het fout gespelde woord: <i>Na de voorstelling kreeg de actrice een staande ovatie bij de premiere.</i>", "première",
      "Première schrijf je met een accent grave."),
    I("Verbeter het fout gespelde woord: <i>De docent wilde met de klas over het onderwerp discussieren.</i>", "discussiëren",
      "Dis-cus-si-ë-ren: het trema laat zien dat de ë een nieuwe lettergreep begint."),
    I("Verbeter het fout gespelde woord: <i>Op vakantie in Frankrijk ontmoette ik een aardige Francaise.</i>", "Française",
      "In Française klinkt de c voor de a als s: cedille."),
    M("Hoeveel fouten staan er in deze zin? <i>De tvs in het cafe toonden een reportage over de ruïne in Italië.</i>",
      "2", ["1", "3", "4"],
      "Twee fouten: tv's (afkorting) en café (accent aigu). Ruïne en Italië zijn juist."),
    M("Hoeveel fouten staan er in deze zin? <i>Lars vader brengt zijn zoon zonder gene te laat naar de creche.</i>",
      "3", ["1", "2", "4"],
      "Drie fouten: Lars' vader (weglatingsteken), gêne (accent circonflexe) en crèche (accent grave)."),
    O("Zoek de fout in deze zin, verbeter het woord en noem de regel: <i>Tijdens de vakantie op Curacao maakte Noor veel foto's.</i>",
      ["curaçao", "cedille/ç", "als een s/als s/s-klank"], 1,
      "Curaçao moet met een cedille: zonder cedille klinkt de c voor de a als k, met cedille als s.",
      "De cedille zorgt dat een c voor a, o of u als s klinkt."),
    O("Zoek de fout in deze zin, verbeter het woord en leg de regel uit: <i>Na het concert bleef het meisje met haar twee paraplus bij de uitgang staan.</i>",
      ["paraplu's", "klinker", "uitspraak/lees/klank/uitgesproken/kort/lang"], 1,
      "Paraplu's: paraplu eindigt op de enkele klinker u. Met de apostrof voorkom je dat je de u kort uitspreekt.",
      "Bij een -s achter de enkele klinkers a, i, o, u en y zet je een apostrof."),
]),
28: ("Gemengd (examenniveau)", "🎯", [
    M("Kies de juiste spelling: <i>De ... van het kasteel trekt veel toeristen.</i>", "ruïne", ["ruine", "ru-ine", "ruïnne"],
      "Ru-ï-ne: zonder trema lees je 'ui' als één klank."),
    M("Kies het juiste meervoud van <i>zee</i>.", "zeeën", ["zeeen", "zee's", "zeeëen"],
      "Zee-ën: het trema laat zien dat de laatste e een nieuwe lettergreep begint."),
    M("Kies het juiste meervoud van <i>menu</i>.", "menu's", ["menus", "menu-s", "menuus"],
      "Menu eindigt op de enkele klinker u: menu's."),
    M("Kies het juiste meervoud van <i>cadeau</i>.", "cadeaus", ["cadeau's", "cadeaux", "kado's"],
      "Cadeau eindigt op 'eau', geen enkele klinker: geen apostrof (net als niveaus en bureaus)."),
    M("Kies de juiste spelling: <i>Mijn broer wil later ... maken bij een grote bank.</i>", "carrière", ["carriere", "carriére", "carrièrre"],
      "Carrière schrijf je met een accent grave."),
    M("Kies de juiste spelling: <i>De stroomsterkte meet je in ...</i>", "ampère", ["ampere", "ampére", "ampêre"],
      "Ampère schrijf je met een accent grave."),
    M("Kies de juiste spelling: <i>Bij de Indonesische afhaal bestellen we altijd ...</i>", "saté", ["sate", "satè", "satee"],
      "Saté schrijf je met een accent aigu."),
    M("Kies de juiste spelling: <i>De ... van het oude stadhuis wordt gerestaureerd.</i>", "façade", ["facade", "fassade", "façadé"],
      "In façade klinkt de c voor de a als s: cedille."),
    M("In welk woord staat een <b>accent grave</b>?", "caissière", ["café", "gemêleerd", "Curaçao"],
      "Caissière heeft een accent grave (è). Café: aigu; gemêleerd: circonflexe; Curaçao: cedille."),
    M("In welk woord is de apostrof gebruikt in een <b>afkorting</b>?", "wc's", ["opa's", "pony'tje", "'s nachts"],
      "Wc is een afkorting; in het meervoud krijgt die een apostrof. Opa's en pony'tje: uitspraak; 's nachts: weglatingsteken."),
    W("<i>Hobby's</i> schrijf je met een apostrof omdat het woord eindigt op een y.", True,
      "Waar. Achter de enkele klinkers a, i, o, u en y zet je bij een -s een apostrof: hobby's."),
    W("<i>Horloges</i> schrijf je met een apostrof: <i>horloge's</i>.", False,
      "Niet waar. Horloge eindigt op een e; dat is geen van de klinkers a, i, o, u, y. Dus horloges zonder apostrof."),
    W("Een cedille staat altijd onder de letter c.", True,
      "Waar. De cedille staat onder de c (ç) en laat de c als s klinken voor a, o of u."),
    W("Voor nadruk gebruik je een accent circonflexe, zoals in <i>Dat is vêêl te duur!</i>", False,
      "Niet waar. Om een woord te benadrukken gebruik je het accent aigu: véél."),
    I("Schrijf correct over: <i>coordinatie</i>", "coördinatie",
      "Co-ör-di-na-tie: zonder trema lees je 'oo' als één klank."),
    I("Schrijf correct over: <i>egoist</i>", "egoïst",
      "E-go-ïst: zonder trema lees je 'oi' als één klank."),
    I("Schrijf correct over: <i>geemigreerd</i>", "geëmigreerd",
      "Ge-ë-mi-greerd: zonder trema lees je 'ee' als één klank."),
    M("Kies de juiste spelling: <i>We liepen met z'n ... naar huis.</i>", "drieën", ["drieen", "drie-en", "drieëen"],
      "Drie-ën: het trema laat zien dat de laatste e een nieuwe lettergreep begint."),
    O("Leg uit waarom je <i>ski's</i> met een apostrof schrijft, maar <i>bureaus</i> zonder.",
      ["klinker", "op eau/geen uitspraakprobleem/lang/klank/uitspraak"], 1,
      "Ski eindigt op de enkele klinker i: zonder apostrof zou je de i kort lezen. Bureau eindigt op 'eau'; daar is geen uitspraakprobleem, dus geen apostrof.",
      "Alleen achter de enkele klinkers a, i, o, u en y zet je een apostrof voor de -s."),
    O("Leg uit waarom je <i>Curaçao</i> met een cedille schrijft, maar <i>cacao</i> niet.",
      ["als een s/als s/s-klank/klinkt als s", "als een k/als k/k-klank/klinkt als k"], 1,
      "In Curaçao moet de c voor de a als s klinken, daarom een cedille. In cacao klinkt de c gewoon als k, dus geen cedille.",
      "De cedille laat een c voor a, o of u als s klinken; normaal klinkt hij daar als k."),
]),
29: ("Eindtoets", "🏁", [
    M("Kies de juiste spelling: <i>Het museum heeft schilderijen uit Nederland en ...</i>", "België", ["Belgie", "Belgïe", "Belgiëe"],
      "Belgi-ë: zonder trema lees je 'ie' als één klank."),
    M("Kies de juiste spelling van het voltooid deelwoord van <i>eren</i>.", "geëerd", ["geeerd", "ge-eerd", "geërd"],
      "Ge-ëerd: zonder trema lees je 'eee' verkeerd; ge- is een voorvoegsel, dus geen koppelteken."),
    M("Kies de juiste spelling: <i>De school heeft het contract met de busmaatschappij ...</i>", "beëindigd", ["beeindigd", "be-eindigd", "bëeindigd"],
      "Be-ëin-digd: zonder trema lees je 'ee' als één klank. Be- is een voorvoegsel: trema, geen koppelteken."),
    M("Kies het juiste meervoud van <i>baby</i>.", "baby's", ["babys", "babies", "baby-s"],
      "Baby eindigt op de enkele klinker y: baby's."),
    M("Kies het juiste verkleinwoord van <i>baby</i>.", "baby'tje", ["babytje", "baby-tje", "babyetje"],
      "Baby eindigt op -y met een medeklinker (b) ervoor: baby'tje."),
    M("Kies het juiste verkleinwoord van <i>dvd</i>.", "dvd'tje", ["dvdtje", "dvd-tje", "dvd'je"],
      "In afleidingen van afkortingen gebruik je een apostrof: dvd'tje."),
    M("Kies het juiste verkleinwoord van <i>reisbureau</i>.", "reisbureautje", ["reisbureau'tje", "reisbureau-tje", "reisburootje"],
      "Bureau eindigt niet op een enkele klinker en ook niet op -y: geen apostrof, dus reisbureautje."),
    M("Kies de juiste spelling: <i>Mijn oma woont in ...</i> (de officiële naam van Den Haag)", "'s-Gravenhage", ["'s Gravenhage", "s'-Gravenhage", "s-Gravenhage"],
      "'s (= des) is een weglatingsteken; in deze plaatsnaam volgt een koppelteken, net als in 's-Hertogenbosch."),
    M("Kies de juiste spelling: <i>Met ... vriend ga ik naar de film.</i> (de vriend van Klaas)", "Klaas'", ["Klaas's", "Klaases", "Klaas-s"],
      "Klaas eindigt op een s: de bezits-s valt weg en de apostrof is het weglatingsteken."),
    M("Kies de juiste spelling: <i>De film speelt zich af rond 1900, in de tijd van de ...</i>", "fin de siècle", ["fin de siecle", "fin de siécle", "fin de sièkle"],
      "Fin de siècle schrijf je met een accent grave."),
    M("Welke uitspraak over het trema is juist?", "Het staat op de klinker waarmee een nieuwe lettergreep begint",
      ["Het staat op de eerste klinker van de twee botsende klinkers", "Het staat altijd op de letter e aan het eind van een woord", "Het staat op de klinker die de klemtoon van het woord krijgt"],
      "Het trema staat op de klinker die een nieuwe lettergreep begint: re-ë-en, be-ïn-vloe-den."),
    W("In <i>reeën</i> staat het trema op de e waarmee een nieuwe lettergreep begint.", True,
      "Waar. Ree-ën: de ë begint de nieuwe lettergreep."),
    W("Het verkleinwoord van <i>paraplu</i> schrijf je met een apostrof: <i>paraplu'tje</i>.", False,
      "Niet waar. De apostrof in verkleinwoorden hoort alleen bij -y na een medeklinker (pony'tje). Juist is parapluutje."),
    W("In <i>François</i> zorgt de cedille ervoor dat de c als een s klinkt, omdat er een o na komt.", True,
      "Waar. Voor a, o en u klinkt de c normaal als k; de cedille maakt er een s-klank van."),
    W("In het woord <i>deodorant</i> moet je een trema schrijven: <i>deödorant</i>.", False,
      "Niet waar. E en o vormen samen geen klank, dus geen trema: deodorant."),
    I("Schrijf correct over: <i>geexporteerd</i>", "geëxporteerd",
      "Ge-ëx-por-teerd: zonder trema lees je 'ee' als één klank."),
    I("Schrijf correct over met cedille: <i>garcon</i> (Frans voor 'jongen' of 'ober')", "garçon",
      "In garçon klinkt de c voor de o als s: cedille."),
    I("Schrijf de samenstelling van <i>video</i> + <i>opname</i> correct.", "video-opname",
      "Twee o's botsen in een samenstelling: koppelteken."),
    O("Leg uit waarom <i>beantwoord</i> geen trema heeft, maar <i>beïnvloeden</i> wel.",
      ["ei", "klank/uitspraak/uitgesproken/lees/lezen"], 1,
      "In beïnvloeden zou je 'ei' als één klank lezen; het trema voorkomt dat. In beantwoord vormen e en a samen geen klank, dus is er geen uitspraakprobleem.",
      "Een trema is alleen nodig als twee klinkers anders samen als één klank worden gelezen."),
    O("Neem over en zet trema's, apostrofs, accenten of cedilles waar nodig: <i>De opas van Maarten aten in het cafe een crepe met creme fraiche.</i>",
      ["opa's", "café", "crêpe", "crème fraîche"], 2,
      "De opa's van Maarten aten in het café een crêpe met crème fraîche.",
      "Opa's (enkele klinker a + s), café (aigu), crêpe (circonflexe), crème (grave) en fraîche (circonflexe op de i)."),
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('c7_2')
    vragen = plaats([dict(v) for v in ONDERWERP_VRAGEN], rng)
    onderwerp = {
        "id": "c7-2-trema-apostrof", "hoofdstuk": 7, "paragraaf": "7.2",
        "titel": "Trema, apostrof, accenten en cedille",
        "korteUitleg": "Gebruik trema, apostrof, accenten en cedille op de juiste manier om uitspraakproblemen te voorkomen.",
        "icoon": "✏️", "theorie": THEORIE, "vragen": vragen,
    }
    schrijf(os.path.join(ROOT, 'c7_2.js'),
            "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 7 Spelling §2) — gegenereerd door tools/gen_nederlands_c7_2.py */\n",
            "DURU.register(" + json.dumps(onderwerp, ensure_ascii=False, indent=2) + ");\n")
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {"id": f"ex-h3-nederlands-{nr}", "hoofdstuk": 7, "hoofdstukTitel": "Cursus 7 — Spelling",
              "paragraaf": "7.2", "titel": f"Toets {nr} — §7.2 {sub}", "vak": "Nederlands · HAVO 3 (Cursus 7)",
              "icoon": icoon, "duurMin": 20, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 7 §2) — gegenereerd door tools/gen_nederlands_c7_2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
