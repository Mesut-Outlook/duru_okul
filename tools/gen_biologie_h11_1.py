#!/usr/bin/env python3
"""Biologie HAVO 3 · Hoofdstuk 11 Voortplanting · §11.1 Man en vrouw (boek p. 128-133).
Schrijft havo3/biologie/js/data/h11_1.js (onderwerp) + examen_6/7/8.js (ex-h3-biologie-6..8).
mc-volgorde willekeurig (geseed), opnieuw geschud tot gate-regels 3/16 kloppen.
Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'biologie', 'js', 'data')


def M(vraag, goed, fout, uitleg, niveau=None):
    d = {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": fout, "uitleg": uitleg}
    if niveau:
        d["niveau"] = niveau
    return d


def W(vraag, antwoord, uitleg, niveau=None):
    d = {"type": "waaronwaar", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}
    if niveau:
        d["niveau"] = niveau
    return d


def I(vraag, antwoord, uitleg):
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def Iv(vraag, antwoord, uitleg, niveau=2):
    return {"type": "invoer", "niveau": niveau, "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def O(vraag, sleutels, min_, model, uitleg):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": min_,
            "modelantwoord": model, "uitleg": uitleg}


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


BEGRIPPEN = [
    ("zaadcel", "De voortplantingscel van de man; zaadcellen worden in de zaadballen gemaakt."),
    ("eicel", "De voortplantingscel van de vrouw; een eicel is veel groter dan een zaadcel omdat ze veel voedingsstoffen bevat."),
    ("zaadbal", "Het orgaan in de balzak waar zaadcellen en het hormoon testosteron worden gemaakt."),
    ("bijbal", "Het orgaan waar zaadcellen worden opgeslagen tot de volgende zaadlozing."),
    ("testosteron", "Het hormoon uit de zaadballen waardoor de zaadballen zaadcellen blijven maken."),
    ("zaadlozing", "Het naar buiten komen van de zaadcellen via de penis."),
    ("erectie", "Het stijf worden van de penis doordat extra bloed naar de zwellichamen gaat."),
    ("sperma", "Het mengsel van zaadvocht en zaadcellen."),
    ("eierstok", "Het orgaan waarin de (onrijpe) eicellen liggen; een vrouw heeft er twee."),
    ("eileider", "De buis die de eicel van de eierstok naar de baarmoeder vervoert."),
    ("menstruatiecyclus", "Wat er van de ene menstruatie tot de volgende gebeurt; hij duurt ongeveer 28 dagen."),
    ("follikel", "Het blaasje in de eierstok waarin een eicel rijpt."),
    ("ovulatie", "Het vrijkomen van een rijpe eicel uit de eierstok (eisprong)."),
    ("baarmoederslijmvlies", "De bloedvatrijke laag aan de binnenkant van de baarmoeder die dikker wordt en bij menstruatie loslaat."),
    ("oestrogeen", "Hormoon van de follikel dat vooral vóór de ovulatie wordt gemaakt en FSH remt."),
    ("progesteron", "Hormoon van het gele lichaam dat na de ovulatie FSH en LH remt."),
    ("FSH", "Follikel stimulerend hormoon uit de hypofyse; het stimuleert de groei van de follikel."),
    ("LH", "Luteïniserend hormoon uit de hypofyse; het start de ovulatie en laat het gele lichaam ontstaan."),
    ("geel lichaam", "De lege follikel na de ovulatie (corpus luteum), die progesteron maakt."),
]

THEORIE = """
<h3>11.1 Man en vrouw</h3>
<p>Voor voortplanting heb je twee soorten <b>voortplantingscellen</b> nodig: de <b>zaadcellen</b> van de man en de <b>eicellen</b> van de vrouw. Samen kunnen ze een kindje laten groeien. In de puberteit komt dit proces op gang: <b>hormonen</b> uit de <b>hypofyse</b> sturen de voortplantingsorganen aan.</p>

<h3>Wanneer is een jongen vruchtbaar?</h3>
<p>In de puberteit maken jongens voor het eerst zaadcellen. De productie komt op gang door hormonen uit de hypofyse. Die komen via het bloed bij de <b>zaadballen</b>, die dan zaadcellen gaan maken. Vanaf dat moment is een jongen <b>vruchtbaar</b>: hij kan een meisje zwanger maken. De zaadballen maken ook het hormoon <b>testosteron</b>. Door testosteron blijven de zaadballen zaadcellen maken.</p>
<p>Een jongen merkt aan zijn eerste <b>zaadlozing</b> dat hij vruchtbaar is: de zaadcellen komen dan via de <b>penis</b> naar buiten. Soms gebeurt dat als hij slaapt; dat heet een <b>natte droom</b>.</p>

<h4>De geslachtsorganen van de man</h4>
<ul>
  <li><b>Zaadballen</b>: hier worden wel zeventig miljoen zaadcellen per dag gemaakt. Een man heeft er twee.</li>
  <li><b>Bijballen</b>: hier worden de zaadcellen opgeslagen tot de volgende zaadlozing. Een man heeft er twee.</li>
  <li><b>Balzak</b>: hierin liggen de zaadballen en de bijballen.</li>
  <li><b>Zaadleiders</b>, <b>zaadblaasjes</b>, <b>prostaat</b>, <b>urinebuis</b>, <b>penis</b> (met <b>zwellichamen</b>, eikel en voorhuid).</li>
</ul>
<div class="info-box tip"><span class="kop">Erectie</span>
<p>Als een jongen seksueel opgewonden is, krijgt hij een <b>erectie</b>: zijn penis wordt stijf doordat er extra bloed naar de <b>zwellichamen</b> gaat. De zwellichamen bevatten veel bloedvaten die zich vullen met bloed. Het bloed blijft tijdens de erectie in de zwellichamen zitten.</p></div>

<h4>De zaadlozing in drie stappen</h4>
<ol>
  <li>Spiertjes in de bijballen trekken samen en persen de zaadcellen de zaadleiders in.</li>
  <li>De zaadcellen komen langs de zaadblaasjes en de prostaat. Die voegen <b>zaadvocht</b> toe. Het mengsel van zaadvocht en zaadcellen heet <b>sperma</b>.</li>
  <li>Bij de prostaat komt het sperma in de urinebuis. Via de urinebuis verlaat het sperma de penis.</li>
</ol>
<div class="info-box let-op"><span class="kop">Let op: geen urine tijdens een zaadlozing</span>
<p>Een spiertje tussen de prostaat en de urineblaas knijpt de urinebuis dicht. Daardoor kan er tijdens een zaadlozing geen urine uit de penis komen.</p></div>

<h3>Wanneer is een meisje vruchtbaar?</h3>
<p>Meisjes worden geboren met ongeveer 400 000 <b>onrijpe eicellen</b> in twee <b>eierstokken</b>. Een meisje is vruchtbaar als die eicellen <b>rijp</b> worden. Dat gebeurt voor het eerst in de puberteit: hormonen uit de hypofyse geven de eierstokken een seintje en een onrijpe eicel neemt vocht en voedingsstoffen op. Een meisje merkt dat ze vruchtbaar is als ze voor het eerst <b>ongesteld</b> is.</p>
<p>Een eicel is veel groter dan een zaadcel, omdat ze veel voedingsstoffen bevat. Die zijn nodig als de eicel wordt bevrucht.</p>
<h4>De geslachtsorganen van de vrouw</h4>
<ul>
  <li><b>Eierstokken</b>: hier liggen de (onrijpe) eicellen.</li>
  <li><b>Eileiders</b>: ze vervoeren de eicel naar de <b>baarmoeder</b>.</li>
  <li><b>Baarmoeder</b>, <b>vagina</b>, <b>clitoris</b>, kleine en grote <b>schaamlippen</b>.</li>
</ul>
<p>De vagina en de urinebuis zijn twee verschillende buizen en hebben dus twee verschillende openingen.</p>

<h3>De menstruatiecyclus</h3>
<p>Vanaf de puberteit is een meisje ongeveer eens in de <b>28 dagen</b> (vier weken) ongesteld, ofwel zij heeft haar <b>menstruatie</b>. Wat er van de ene menstruatie tot de volgende gebeurt, heet de <b>menstruatiecyclus</b>.</p>
<ol>
  <li><b>Een eicel rijpt</b> in een van de eierstokken. De eicel ligt in een blaasje: de <b>follikel</b>. De rijpende eicel neemt vocht met voedingsstoffen op en groeit.</li>
  <li><b>Het baarmoederslijmvlies wordt dikker.</b> Zodra een eicel begint te rijpen, wordt het slijmvlies aan de binnenkant van de baarmoeder dikker en komen er meer bloedvaten in. Zo wordt de baarmoeder geschikt om een baby te laten groeien.</li>
  <li><b>Ovulatie.</b> Na ongeveer veertien dagen is de eicel rijp. De follikel barst open en de rijpe eicel komt in de eileider. Dit heet <b>eisprong</b> of <b>ovulatie</b>.</li>
  <li><b>Menstruatie.</b> Meestal vindt er geen bevruchting plaats en gaat de eicel dood. Het verdikte slijmvlies laat dan twee weken later los en druppelt met wat bloed uit de vagina.</li>
</ol>
<div class="info-box tip"><span class="kop">Vruchtbare periode</span>
<p>Na de eisprong blijft de eicel 12 tot 24 uur in de eileider leven. Zaadcellen kunnen via de vagina en de baarmoeder bij de eicel in de eileider komen en deze bevruchten. De dagen rond de eisprong vormen de <b>vruchtbare periode</b> van de vrouw.</p></div>

<h3>Hormonen regelen de cyclus</h3>
<p>De menstruatiecyclus wordt geregeld door hormonen uit de follikel (<b>oestrogeen</b> en <b>progesteron</b>) en twee hormonen uit de hypofyse: <b>FSH</b> (follikel stimulerend hormoon) en <b>LH</b> (luteïniserend hormoon).</p>
<ol>
  <li>Aan het begin van de cyclus geeft de hypofyse FSH af. FSH stimuleert de groei van de follikel.</li>
  <li>De groeiende follikel maakt oestrogeen. Oestrogeen remt de FSH-productie, zodat er geen nieuwe eicellen rijpen. Veel oestrogeen stimuleert de productie van LH.</li>
  <li>Door de stijging van LH treedt de ovulatie op.</li>
  <li>Na de ovulatie laat LH de lege follikel groeien en geel gekleurd vet opnemen. Hij heet nu het <b>gele lichaam</b> (corpus luteum).</li>
  <li>Het gele lichaam maakt progesteron. Progesteron remt FSH en LH, dus er rijpen geen eicellen meer.</li>
  <li>Is de eicel niet bevrucht, dan neemt de productie van oestrogeen en progesteron af en komt de menstruatie op gang. Daarna start de hypofyse weer met FSH en begint de cyclus opnieuw.</li>
</ol>
<table class="nask"><tr><th>hormoon</th><th>gemaakt door</th><th>effect</th></tr>
<tr><td>FSH</td><td>hypofyse</td><td>stimuleert de follikelgroei</td></tr>
<tr><td>LH</td><td>hypofyse</td><td>LH-piek start de ovulatie; stimuleert het gele lichaam</td></tr>
<tr><td>oestrogeen</td><td>follikel (vóór ovulatie)</td><td>remt FSH, dikker slijmvlies, piek start LH</td></tr>
<tr><td>progesteron</td><td>gele lichaam (na ovulatie)</td><td>remt FSH en LH, slijmvlies blijft dik en goed doorbloed</td></tr></table>

<div class="formule-box">Volgorde: eicel rijpt &rarr; slijmvlies wordt dikker &rarr; ovulatie &rarr; slijmvlies wordt afgestoten (menstruatie)</div>

<h3>Toepassen: worden dieren ongesteld?</h3>
<ul>
  <li><b>Vogels</b> hebben geen baarmoeder en dus geen menstruatie, wel een eisprong. Hennen hebben zelfs elke dag een eisprong.</li>
  <li>Alle vrouwtjeszoogdieren hebben een baarmoeder, maar alleen <b>mensapen</b> zoals chimpansees menstrueren. Bij andere zoogdieren wordt het slijmvlies weer opgenomen in het bloed.</li>
  <li>Een <b>teef</b> die vruchtbaar wordt, is <b>loops</b>: de schaamlippen zwellen op, bloedvaatjes gaan stuk en ze verliest wat bloed. Dat komt niet uit de baarmoeder. Na ongeveer anderhalve week krijgt ze haar eisprong. <b>Feromonen</b> (lokstoffen) in haar urine trekken reuen aan.</li>
</ul>
"""

ONDERWERP_VRAGEN = [
    M("Hoeveel zaadcellen maken de zaadballen ongeveer per dag?", "ongeveer 70 miljoen", ["ongeveer 400 000", "ongeveer 7 000", "ongeveer 28"],
      "In de zaadballen worden wel zeventig miljoen zaadcellen per dag gemaakt.", 1),
    M("Wat gebeurt er met een eicel die niet bevrucht wordt?", "Ze gaat dood en het slijmvlies laat los", ["Ze blijft maanden in de eileider leven", "Ze wordt opgeslagen in de bijbal", "Ze rijpt verder in de baarmoeder"],
      "Meestal vindt er geen bevruchting plaats: de eicel gaat dood en het verdikte slijmvlies komt later los (menstruatie).", 2),
    M("Waar komt de naam luteïniserend hormoon vandaan?", "Van het gele lichaam (corpus luteum) dat door LH ontstaat", ["Van de eicel die door dit hormoon rijpt", "Van de hypofyse waar dit hormoon wordt gemaakt", "Van het baarmoederslijmvlies dat dikker wordt"],
      "LH laat de lege follikel groeien tot het gele lichaam (corpus luteum). Daar komt de naam luteïniserend hormoon vandaan.", 3),
    M("Wat is de juiste volgorde in de menstruatiecyclus?", "Eicel rijpt, slijmvlies dikker, ovulatie, menstruatie", ["Ovulatie, eicel rijpt, menstruatie, slijmvlies dikker", "Menstruatie, ovulatie, slijmvlies dikker, eicel rijpt", "Slijmvlies dikker, menstruatie, eicel rijpt, ovulatie"],
      "Eerst begint de eicel te rijpen, dan wordt het slijmvlies dikker, dan volgt de eisprong en daarna de menstruatie.", 3),
    W("Alle vrouwtjeszoogdieren menstrueren.", False,
      "Niet waar. Alleen mensapen zoals chimpansees menstrueren; bij andere zoogdieren wordt het slijmvlies weer opgenomen in het bloed.", 2),
    W("Een meisje maakt pas in de puberteit nieuwe eicellen aan.", False,
      "Niet waar. Meisjes worden geboren met ongeveer 400 000 onrijpe eicellen. In de puberteit gaan ze rijpen.", 2),
    W("De puberteit begint bij jongens en meisjes doordat de hypofyse hormonen afgeeft.", True,
      "Waar. Bij jongens gaan de zaadballen zaadcellen maken, bij meisjes gaan eicellen rijpen.", 1),
    W("Tijdens de menstruatie gebruikt een vrouw maandverband of tampons om het bloed op te vangen.", True,
      "Waar. Het verdikte slijmvlies druppelt met wat bloed uit de vagina.", 1),
    Iv("Hoe heet de buis waardoor het sperma de penis verlaat?", "urinebuis|de urinebuis",
       "Het sperma komt bij de prostaat in de urinebuis en verlaat zo de penis."),
    Iv("Hoe heet het blaasje in de eierstok waarin een eicel rijpt?", "follikel|de follikel",
       "De eicel ligt tijdens het rijpen in een blaasje: de follikel."),
]

EXAMENS = {
6: ("Begrippen & bouw", "🧬", [
    M("Waar worden zaadcellen gemaakt?", "In de zaadballen", ["In de bijballen", "In de prostaat", "In de zaadblaasjes"],
      "In de zaadballen ontstaan de zaadcellen. De bijballen slaan ze alleen op."),
    M("Waar worden zaadcellen opgeslagen tot de volgende zaadlozing?", "In de bijballen", ["In de zaadleiders", "In de zaadblaasjes", "In de balzak zelf"],
      "De zaadcellen worden opgeslagen in de bijballen. De balzak is het zakje waarin zaadballen en bijballen liggen."),
    M("Wat is sperma?", "Een mengsel van zaadvocht en zaadcellen", ["Een mengsel van urine en zaadcellen", "Het vocht dat de bijballen maken", "Een hormoon uit de hypofyse"],
      "Zaadblaasjes en prostaat voegen zaadvocht toe aan de zaadcellen. Dat mengsel heet sperma."),
    M("Welk orgaan vervoert de eicel naar de baarmoeder?", "De eileider", ["De eierstok", "De vagina", "De urinebuis"],
      "De eileider vervoert eicellen naar de baarmoeder. In de eierstokken liggen de eicellen."),
    M("Met hoeveel onrijpe eicellen wordt een meisje ongeveer geboren?", "Ongeveer 400 000", ["Ongeveer 70 miljoen", "Ongeveer 4 000", "Ongeveer 14 000"],
      "Meisjes worden geboren met ongeveer 400 000 onrijpe eicellen. De 70 miljoen is het aantal zaadcellen dat zaadballen per dag maken."),
    M("Waarom is een eicel veel groter dan een zaadcel?", "Ze bevat veel voedingsstoffen", ["Ze heeft een lange staart", "Ze heeft meer celkernen", "Ze bevat veel zaadvocht"],
      "Een eicel bevat veel voedingsstoffen die nodig zijn als ze wordt bevrucht."),
    M("Welk orgaan hoort bij de geslachtsorganen van de man?", "De prostaat", ["De eileider", "De baarmoeder", "De clitoris"],
      "De prostaat is een mannelijk geslachtsorgaan. Eileider, baarmoeder en clitoris horen bij de vrouw."),
    M("Wat zijn zwellichamen?", "Bloedvatrijke delen in de penis die bij een erectie vol bloed lopen", ["Delen van de zaadbal waar zaadcellen rijpen", "Klieren die zaadvocht aan het sperma toevoegen", "Spiertjes die de urinebuis dichtknijpen"],
      "In de zwellichamen zitten veel bloedvaten. Bij een erectie gaat er extra bloed heen, waardoor de penis stijf wordt."),
    M("Wat is het gele lichaam?", "De lege follikel na de ovulatie", ["Het verdikte baarmoederslijmvlies", "Een onrijpe eicel in de eierstok", "Het blaasje voor de eisprong"],
      "Na de ovulatie groeit de lege follikel en neemt geel vet op. Hij heet dan het gele lichaam (corpus luteum)."),
    W("Een man heeft twee zaadballen en twee bijballen.", True,
      "Waar. Zaadballen en bijballen liggen samen in de balzak."),
    W("De vagina en de urinebuis van de vrouw zijn dezelfde buis met één opening.", False,
      "Niet waar. De vagina en de urinebuis zijn twee verschillende buizen met twee openingen."),
    W("Een zaadcel is veel groter dan een eicel.", False,
      "Niet waar. Een eicel is veel groter dan een zaadcel."),
    W("Zaadballen en bijballen liggen in de balzak.", True,
      "Waar. De balzak is het zakje waarin beide organen liggen."),
    W("Meisjes worden geboren met onrijpe eicellen in de eierstokken.", True,
      "Waar. Ze worden pas rijp in en na de puberteit."),
    I("De zaadballen maken het hormoon ____, waardoor ze zaadcellen blijven maken.", "testosteron",
      "Door testosteron blijven de zaadballen zaadcellen maken."),
    I("Een zaadlozing tijdens de slaap heet een natte ____.", "droom",
      "Soms komt een zaadlozing als een jongen slaapt. Dat heet een natte droom."),
    I("De binnenkant van de baarmoeder is bedekt met baarmoeder____.", "slijmvlies",
      "De binnenkant van de baarmoeder is bedekt met baarmoederslijmvlies."),
    I("De voortplantingscellen van een man heten ____.", "zaadcellen|zaadcel|de zaadcellen",
      "De voortplantingscellen van de man zijn zaadcellen, die van de vrouw eicellen."),
    O("Leg uit waarom een eicel veel groter is dan een zaadcel.", ["voedingsstof", "bevrucht"], 2,
      "Een eicel bevat veel voedingsstoffen. Die zijn nodig als de eicel wordt bevrucht.",
      "Een eicel is zo groot doordat ze veel voedingsstoffen bevat; die zijn nodig na de bevruchting."),
    O("Beschrijf wat er in het lichaam van een jongen gebeurt waardoor hij in de puberteit vruchtbaar wordt.", ["hypofyse", "hormoon/hormonen", "zaadcellen"], 2,
      "De hypofyse geeft hormonen af. Die komen via het bloed bij de zaadballen, die dan zaadcellen gaan maken.",
      "Hormonen uit de hypofyse laten de zaadballen zaadcellen maken; vanaf dan is een jongen vruchtbaar."),
]),
7: ("Functies & processen", "⚙️", [
    M("Wat gebeurt er als eerste bij een zaadlozing?", "Spiertjes in de bijballen persen de zaadcellen de zaadleiders in", ["De zwellichamen persen de zaadcellen de urinebuis in", "De prostaat laat de zaadcellen los in de zaadblaasjes", "De urineblaas knijpt de zaadcellen de penis uit"],
      "Spiertjes in de bijballen trekken samen en persen de zaadcellen de zaadleiders in."),
    M("Wat voegen de zaadblaasjes en de prostaat toe aan de zaadcellen?", "Zaadvocht", ["Urine", "Testosteron", "Bloed"],
      "Zaadblaasjes en prostaat voegen zaadvocht toe."),
    M("Waarom komt er tijdens een zaadlozing geen urine uit de penis?", "Een spiertje knijpt de urinebuis bij de urineblaas dicht", ["De urineblaas is tijdens een zaadlozing altijd helemaal leeg", "De zaadleiders pompen de urine terug naar de nieren", "De urinebuis loopt dan door de prostaat naar de zaadleiders"],
      "Een spiertje tussen de prostaat en de urineblaas knijpt de urinebuis dicht."),
    M("Wat gebeurt er tijdens de eisprong?", "De follikel barst open en de eicel komt in de eileider", ["De eicel komt los uit het baarmoederslijmvlies en blijft liggen", "De follikel verdwijnt in de eileider en rijpt daar verder", "De eicel gaat dood in de eierstok en laat los"],
      "De follikel barst open en de rijpe eicel komt in de eileider."),
    M("Hoe lang blijft een eicel na de eisprong in de eileider leven?", "12 tot 24 uur", ["1 tot 2 weken", "2 tot 4 dagen", "ongeveer 28 dagen"],
      "Na de eisprong blijft de eicel 12 tot 24 uur in de eileider leven."),
    M("Wat gebeurt er met het baarmoederslijmvlies als de eicel niet bevrucht is?", "Het laat los en verlaat met wat bloed de vagina", ["Het wordt nog dikker en blijft ruim een maand zitten", "Het gaat via de eileider terug naar de eierstok om te rijpen", "Het wordt omgezet in een nieuwe follikel in de baarmoeder"],
      "Het slijmvlies is niet meer nodig en laat los: dat is de menstruatie."),
    M("Wat doet FSH aan het begin van de menstruatiecyclus?", "Het stimuleert de groei van de follikel", ["Het start de ovulatie", "Het remt de LH-productie", "Het maakt het slijmvlies dunner"],
      "FSH stimuleert de groei van de follikel. LH start de ovulatie."),
    M("Wat zorgt ervoor dat de ovulatie plaatsvindt?", "Een stijging van de LH-concentratie in het bloed", ["Een stijging van de FSH-concentratie", "Een daling van de oestrogeenconcentratie", "Een stijging van de progesteronconcentratie"],
      "Door de stijging (piek) van LH treedt de ovulatie op."),
    M("Welk effect heeft oestrogeen vóór de ovulatie?", "Het remt FSH, zodat er geen nieuwe eicel rijpt", ["Het laat de lege follikel groeien en geel worden", "Het start meteen de menstruatie van de vrouw", "Het stimuleert de FSH-productie van de hypofyse sterk"],
      "Oestrogeen remt de productie van FSH, zodat er geen nieuwe eicellen rijpen; het maakt ook het slijmvlies dikker."),
    W("Een menstruatiecyclus duurt ongeveer 28 dagen.", True,
      "Waar. Dat is ongeveer vier weken."),
    W("FSH remt de groei van de follikel.", False,
      "Niet waar. FSH (follikel stimulerend hormoon) stimuleert de groei van de follikel."),
    W("Hormonen uit de hypofyse zorgen dat de zaadballen zaadcellen gaan maken.", True,
      "Waar. Die hormonen komen via het bloed bij de zaadballen."),
    W("Het gele lichaam produceert progesteron.", True,
      "Waar. De lege follikel heet na de ovulatie het gele lichaam en maakt vooral progesteron."),
    W("Tijdens de menstruatie wordt het baarmoederslijmvlies dikker.", False,
      "Niet waar. Tijdens de menstruatie laat het slijmvlies los; het wordt dikker als een eicel gaat rijpen."),
    I("Het vrijkomen van een rijpe eicel uit de eierstok heet eisprong of ____.", "ovulatie",
      "Het vrijkomen van een rijpe eicel heet eisprong of ovulatie."),
    I("Na de ovulatie heet de lege follikel het gele ____.", "lichaam",
      "De lege follikel heet na de ovulatie het gele lichaam (corpus luteum)."),
    I("Het mengsel van zaadvocht en zaadcellen heet ____.", "sperma",
      "Het mengsel van zaadvocht en zaadcellen heet sperma."),
    I("De menstruatie begint doordat de productie van oestrogeen en ____ afneemt.", "progesteron",
      "Als de eicel niet bevrucht is, neemt de productie van oestrogeen en progesteron af. Daardoor komt de menstruatie op gang."),
    O("Beschrijf de weg van de zaadcellen vanaf de bijballen tot ze het lichaam verlaten.", ["zaadleider", "prostaat", "urinebuis"], 2,
      "Via de zaadleiders gaan de zaadcellen langs de zaadblaasjes en de prostaat naar de urinebuis, en zo verlaten ze via de penis het lichaam.",
      "Bijbal, zaadleider, langs zaadblaasjes en prostaat, urinebuis, penis."),
    O("Beschrijf wat er in de eerste veertien dagen van de cyclus gebeurt in de eierstok en de baarmoeder.", ["rijp", "slijmvlies", "dikker/bloedvaten"], 2,
      "In de eierstok rijpt een eicel. In de baarmoeder wordt het slijmvlies dikker en komen er meer bloedvaten in.",
      "Een eicel rijpt in de follikel en het slijmvlies wordt dikker met meer bloedvaten."),
]),
8: ("Toepassen & redeneren", "🔍", [
    M("Een vrouw heeft een cyclus van 28 dagen. Dag 1 is de eerste dag van haar menstruatie. Op welke dag vindt de eisprong ongeveer plaats?", "Op ongeveer dag 14", ["Op ongeveer dag 1", "Op ongeveer dag 7", "Op ongeveer dag 28"],
      "Na ongeveer veertien dagen is de eicel rijp en vindt de eisprong plaats."),
    M("Een jongen wordt wakker met een nat beddengoed na een droom. Wat is er gebeurd?", "Hij heeft een zaadlozing gehad tijdens zijn slaap", ["Zijn zwellichamen hebben urine afgegeven aan het beddengoed", "Zijn prostaat heeft tijdens de nacht bloed verloren", "Zijn bijballen zijn geleegd doordat hij een erectie kreeg"],
      "Een zaadlozing tijdens de slaap heet een natte droom. Het is ook het teken dat hij vruchtbaar is."),
    M("Wat betekent het als een meisje voor het eerst ongesteld is?", "Er zijn eicellen gaan rijpen, ze is vruchtbaar", ["Ze maakt voor het eerst zaadcellen aan in haar eierstokken", "Haar eierstokken zijn leeg geraakt en stoppen met werken", "Haar baarmoeder is volgroeid maar nog niet actief"],
      "Een meisje merkt aan haar eerste menstruatie dat ze vruchtbaar is."),
    M("Waarom beginnen de eicellen van een meisje in de puberteit te rijpen?", "Hormonen uit de hypofyse geven de eierstokken een seintje", ["De eierstokken maken dan zelf honderdduizenden nieuwe eicellen", "De baarmoeder geeft een signaal aan de eierstokken", "Er komt in de puberteit testosteron vrij uit de eileiders"],
      "De puberteit start als de hypofyse hormonen afgeeft; die geven de eierstokken een seintje."),
    M("Een vrouw slikt een medicijn dat aan het begin van de cyclus de werking van FSH tegenhoudt. Wat is het gevolg?", "De follikel gaat niet groeien en er rijpt geen eicel", ["De ovulatie vindt een week eerder plaats dan normaal", "Het gele lichaam maakt extra veel progesteron aan", "Het slijmvlies laat direct los en de vrouw menstrueert"],
      "FSH stimuleert de groei van de follikel. Zonder FSH groeit de follikel niet en rijpt er geen eicel."),
    M("Wanneer kan een eicel bevrucht worden door een zaadcel?", "Op de dagen rond de eisprong", ["Alleen tijdens de menstruatie", "In de week na de menstruatie", "Op elke dag van de cyclus"],
      "De dagen rond de eisprong vormen de vruchtbare periode van de vrouw."),
    M("Welk dier heeft geen baarmoeder en dus geen menstruatie?", "Een hen", ["Een chimpansee", "Een koe", "Een teef"],
      "Vogels hebben geen baarmoeder. Alle vrouwtjeszoogdieren, ook koeien en teven, hebben er wel een."),
    M("Een loopse teef verliest bloed. Waar komt dat bloed vandaan?", "Uit de schaamlippen waar bloedvaatjes stuk gaan", ["Uit de baarmoeder, doordat het slijmvlies loslaat", "Uit de eileiders, die door de feromonen opzwellen", "Uit de urinebuis, door de lokstoffen in de urine"],
      "De schaamlippen zwellen op, waardoor bloedvaatjes stuk gaan. Het bloed komt niet uit de baarmoeder, dus het is geen menstruatie."),
    M("Een jongen krijgt een erectie. Wat gebeurt er in zijn penis?", "Extra bloed gaat naar de zwellichamen", ["Het bloed stroomt juist uit de zwellichamen weg", "De zwellichamen vullen zich met zaadvocht", "De urinebuis vult zich met sperma"],
      "Door extra bloed in de zwellichamen wordt de penis stijf. Het bloed blijft tijdens de erectie in de zwellichamen zitten."),
    W("Bij vrouwtjeshonden komt de eisprong ongeveer anderhalve week nadat ze loops zijn geworden.", True,
      "Waar. Dat staat in het boek bij het voorbeeld van de teef."),
    W("Feromonen in de urine van een teefje trekken reuen aan.", True,
      "Waar. Feromonen zijn lokstoffen."),
    W("Een hen heeft maar één keer per jaar een eisprong.", False,
      "Niet waar. Hennen hebben zelfs iedere dag een eisprong."),
    W("Bij een erectie stroomt bloed uit de zwellichamen weg.", False,
      "Niet waar. Er gaat extra bloed naar de zwellichamen, dat tijdens de erectie blijft zitten."),
    W("Na ongeveer een half jaar begint bij een teefje die niet is bevrucht de volgende cyclus.", True,
      "Waar. Als er geen bevruchting plaatsvindt, begint de volgende cyclus pas na ongeveer een half jaar."),
    I("Lokstoffen in de urine van een teefje die reuen aantrekken heten ____.", "feromonen|feromoon",
      "Die lokstoffen noem je feromonen."),
    I("Een teefje dat vruchtbaar wordt, is ____.", "loops",
      "Je zegt dat het teefje loops is."),
    I("Een kip heeft wel een eisprong maar geen ____, dus geen menstruatie.", "baarmoeder|de baarmoeder",
      "Vogels hebben geen baarmoeder en dus geen menstruatie."),
    I("Een jongen krijgt een ____ als zijn penis stijf wordt door extra bloed.", "erectie",
      "Bij seksuele opwinding krijgt hij een erectie."),
    O("Leg uit waarom vogels geen menstruatie hebben, maar wel een eisprong.", ["baarmoeder", "slijmvlies"], 1,
      "Vogels hebben geen baarmoeder, dus geen slijmvlies dat kan loslaten. Hun eicellen rijpen wel en komen vrij.",
      "Menstruatie is het loslaten van baarmoederslijmvlies; zonder baarmoeder is er geen menstruatie."),
    O("Beschrijf hoe de follikel en de hypofyse samen zorgen dat de eisprong plaatsvindt.", ["oestrogeen", "LH"], 2,
      "De follikel maakt oestrogeen. Veel oestrogeen stimuleert de hypofyse tot productie van LH. De stijging van LH zorgt voor de ovulatie.",
      "Veel oestrogeen uit de follikel geeft de hypofyse een seintje om meer LH te maken; de LH-stijging start de ovulatie."),
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_1')
    vragen = plaats([dict(v) for v in ONDERWERP_VRAGEN], rng)
    assert len(vragen) == 10
    onderwerp = {
        "id": "bio-h11-1-man-en-vrouw", "hoofdstuk": 11, "paragraaf": "11.1",
        "titel": "Man en vrouw",
        "korteUitleg": "Geslachtsorganen van man en vrouw, zaadlozing, eicelrijping en de hormonen die de menstruatiecyclus regelen.",
        "icoon": "🧬", "kleur": "h11-thema", "theorie": THEORIE, "vragen": vragen,
    }
    assert len(THEORIE) >= 2500 and 10 <= len(BEGRIPPEN) <= 20
    schrijf(os.path.join(ROOT, 'h11_1.js'),
            "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Biologie H11 Voortplanting §11.1) — gegenereerd door tools/gen_biologie_h11_1.py */\n",
            "DURU.register(" + json.dumps(onderwerp, ensure_ascii=False, indent=2) + ");\n")
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {"id": f"ex-h3-biologie-{nr}", "hoofdstuk": 11, "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
              "paragraaf": "11.1", "titel": f"Toets {nr} — §11.1 {sub}", "vak": "Biologie · HAVO 3 (H11.1)",
              "icoon": icoon, "duurMin": 20, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie H11.1) — gegenereerd door tools/gen_biologie_h11_1.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
