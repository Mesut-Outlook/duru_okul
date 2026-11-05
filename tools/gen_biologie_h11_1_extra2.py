#!/usr/bin/env python3
"""Biologie HAVO 3 · Hoofdstuk 11 Voortplanting · §11.1 Man en vrouw (extra toetsen 47–51).
Schrijft havo3/biologie/js/data/examen_47..51.js (ex-h3-biologie-47..51).
mc-volgorde willekeurig (geseed), opnieuw geschud tot gate-regels 3/16/17 kloppen.
"""
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


EXAMENS = {
47: ("Zaadcellen: van zaadbal tot zaadlozing", "🧬", [
    M("Op welke plek komt het sperma tijdens een zaadlozing in de urinebuis terecht?",
      "Bij de prostaat",
      ["Bij de bijballen", "Bij de zaadblaasjes", "Bij de zaadballen"],
      "Bij de prostaat komt het sperma in de urinebuis en verlaat het via de penis het lichaam."),
    M("Hoe komen de hormonen uit de hypofyse bij de zaadballen?",
      "Via het bloed",
      ["Via de zaadleiders", "Via de urinebuis", "Via de bijballen"],
      "De hormonen uit de hypofyse komen via het bloed bij de zaadballen, waarna de zaadballen zaadcellen gaan maken."),
    M("Welke bewering over de mannelijke voortplantingsorganen is onjuist?",
      "De zaadleiders voegen zaadvocht toe aan de zaadcellen",
      ["De bijballen slaan zaadcellen op tot de volgende zaadlozing",
       "De zaadballen maken zaadcellen en het hormoon testosteron",
       "Het sperma verlaat de man via de urinebuis en de penis"],
      "Zaadvocht wordt toegevoegd door de zaadblaasjes en de prostaat. De zaadleiders vervoeren de zaadcellen alleen."),
    M("In de zaadballen worden zeventig miljoen zaadcellen per dag gemaakt. Hoeveel zijn dat ongeveer in één week?",
      "Ongeveer 490 miljoen",
      ["Ongeveer 210 miljoen", "Ongeveer 700 miljoen", "Ongeveer 350 miljoen"],
      "7 dagen × 70 miljoen = 490 miljoen zaadcellen."),
    M("Een zaadcel is ongeveer 0,05 mm lang (bron 2). Hoeveel zaadcellen passen achter elkaar op een lengte van 1 mm?",
      "Ongeveer 20 zaadcellen",
      ["Ongeveer 5 zaadcellen", "Ongeveer 50 zaadcellen", "Ongeveer 200 zaadcellen"],
      "1 mm gedeeld door 0,05 mm is 20."),
    M("Welke volgorde van gebeurtenissen in de puberteit van een jongen klopt?",
      "Hormonen uit de hypofyse, zaadcelproductie, vruchtbaar, eerste zaadlozing merken",
      ["Zaadcelproductie, hormonen uit de hypofyse, eerste zaadlozing, vruchtbaar",
       "Eerste zaadlozing, hormonen uit de hypofyse, zaadcelproductie, vruchtbaar",
       "Hormonen uit de hypofyse, eerste zaadlozing, zaadcelproductie, vruchtbaar"],
      "De hypofyse geeft hormonen af, de zaadballen gaan zaadcellen maken, de jongen is dan vruchtbaar en merkt dat aan zijn eerste zaadlozing."),
    M("Wat zou je verwachten als de zaadballen geen testosteron meer maakten?",
      "De zaadballen stoppen met het maken van zaadcellen",
      ["De bijballen gaan de zaadcellen zelf maken",
       "De prostaat gaat veel meer zaadvocht maken",
       "De hypofyse stopt met het afgeven van FSH"],
      "Door testosteron blijven de zaadballen zaadcellen maken. Zonder testosteron stopt die productie."),
    M("Wat is het verschil tussen de zwellichamen en de zaadleiders?",
      "Zwellichamen maken de penis stijf; zaadleiders vervoeren zaadcellen",
      ["Zwellichamen vervoeren zaadcellen; zaadleiders maken de penis stijf",
       "Zwellichamen slaan zaadcellen op; zaadleiders vullen zich met bloed",
       "Zwellichamen maken zaadvocht; zaadleiders maken de penis stijf"],
      "De zwellichamen vullen zich met bloed (erectie). De zaadleiders vervoeren zaadcellen naar de urinebuis."),
    M("Welke combinatie van orgaan en product klopt?",
      "Zaadbal: zaadcellen; zaadblaasje: zaadvocht",
      ["Bijbal: zaadvocht; zaadbal: sperma",
       "Prostaat: zaadcellen; zaadleider: testosteron",
       "Zaadleider: zaadvocht; bijbal: testosteron"],
      "De zaadballen maken zaadcellen. De zaadblaasjes (en de prostaat) voegen zaadvocht toe."),
    W("Tussen twee zaadlozingen worden de zaadcellen in de bijballen bewaard.", True,
      "Waar. Zaadcellen worden tot de volgende zaadlozing in de bijballen opgeslagen."),
    W("De zaadballen krijgen het seintje om zaadcellen te maken van de prostaat.", False,
      "Niet waar. Het seintje komt van hormonen uit de hypofyse."),
    W("Een zaadcel is groter dan een eicel.", False, "Niet waar. Een eicel is veel groter dan een zaadcel."),
    W("In de puberteit maken jongens hun zaadcellen voor het eerst in de bijballen.", False,
      "Niet waar. Zaadcellen worden in de zaadballen gemaakt; de bijballen slaan ze alleen op."),
    W("Een natte droom is een zaadlozing die plaatsvindt terwijl een jongen slaapt.", True, "Waar. Een zaadlozing tijdens de slaap heet een natte droom."),
    I("De zaadballen en de bijballen liggen samen in de ____.", "balzak|de balzak", "De zaadballen en de bijballen liggen in de balzak."),
    I("Een zaadcel bestaat uit een kop met de celkern en een ____.", "staart|de staart",
      "Een zaadcel heeft een kop met celkern en een staart."),
    I("Tijdens een zaadlozing knijpt een spiertje de urinebuis dicht, zodat er geen ____ uit de penis kan komen.", "urine", "Een spiertje tussen de prostaat en de urineblaas knijpt de urinebuis dicht, dus er komt geen urine uit."),
    I("Als een jongen seksueel opgewonden is, krijgt hij een ____: zijn penis wordt stijf.", "erectie|een erectie", "Bij een erectie wordt de penis stijf doordat er extra bloed naar de zwellichamen gaat."),
    O("Leg uit wat er in de zaadballen verandert wanneer de hypofyse in de puberteit hormonen afgeeft.", ["zaadcellen/zaadcel", "testosteron"], 2,
      "De zaadballen gaan zaadcellen maken en ook testosteron, waardoor ze zaadcellen blijven maken.",
      "Er is een seintje voor de zaadballen: ze maken zaadcellen en testosteron."),
    O("Leg uit waarom een jongen van acht nog geen meisje zwanger kan maken.", ["hypofyse/hormonen/hormoon", "zaadcellen/zaadcel/vruchtbaar"], 2,
      "Zijn hypofyse geeft nog geen hormonen af, dus de zaadballen maken nog geen zaadcellen en hij is nog niet vruchtbaar.",
      "De hypofyse geeft nog geen hormonen af, daardoor ontstaan er nog geen zaadcellen.")
]),
48: ("Eicel en vrouwelijke geslachtsorganen", "🧬", [
    M("Een meisje van elf jaar heeft nog geen rijpe eicellen. Wat geldt voor haar?",
      "Ze kan nog niet zwanger worden",
      ["Ze is al vruchtbaar maar nog niet ongesteld", "Ze kan al zwanger worden door haar onrijpe eicellen", "Ze maakt dan nog geen onrijpe eicellen aan"],
      "Een meisje is pas vruchtbaar als haar eicellen rijp worden. Dan pas kan ze zwanger worden."),
    M("Wat doet een onrijpe eicel als de eierstokken een seintje van de hypofyse krijgen?",
      "De eicel neemt vocht en voedingsstoffen op",
      ["De eicel verlaat meteen de eierstok", "De eicel splitst zich in tweeën", "De eicel deelt zich meteen in vier cellen"],
      "De onrijpe eicel neemt vocht en voedingsstoffen op en gaat zo rijpen."),
    M("Een pasgeboren meisje heeft ongeveer 400 000 eicellen in haar twee eierstokken samen. Hoeveel zitten er gemiddeld in één eierstok?",
      "Ongeveer 200 000",
      ["Ongeveer 100 000", "Ongeveer 400 000", "Ongeveer 800 000"],
      "400 000 gedeeld door twee eierstokken is 200 000."),
    M("Welke bewering over de eicel en de zaadcel klopt?",
      "De eicel is veel groter dan de zaadcel",
      ["De zaadcel is groter dan de eicel doordat hij een staart heeft",
       "De eicel en de zaadcel zijn ongeveer even groot",
       "De eicel kan zich zelf voortbewegen met een staart"],
      "Bron 5: een eicel is veel groter dan een zaadcel."),
    M("Welke bewering over de vrouwelijke geslachtsorganen is onjuist?",
      "De eileider is de opening waardoor de urine het lichaam verlaat",
      ["De eierstokken bevatten onrijpe eicellen vanaf de geboorte",
       "De vagina en de urinebuis hebben twee aparte openingen",
       "De binnenkant van de baarmoeder is bedekt met slijmvlies"],
      "De urine verlaat het lichaam via de urinebuis. De eileider vervoert de eicel."),
    M("Welk van de volgende organen hoort niet bij de vrouwelijke geslachtsorganen?",
      "Het zaadblaasje",
      ["De kleine schaamlip", "De eileider", "De baarmoeder"],
      "Het zaadblaasje hoort bij de geslachtsorganen van de man."),
    M("Hoe merkt een jongen dat hij vruchtbaar is en hoe merkt een meisje dat?",
      "Jongen: eerste zaadlozing; meisje: voor het eerst ongesteld",
      ["Jongen: voor het eerst ongesteld; meisje: eerste zaadlozing",
       "Jongen: eerste erectie; meisje: eerste eisprong gevoeld",
       "Jongen: natte droom; meisje: eerste zaadlozing"],
      "Een jongen merkt het aan zijn eerste zaadlozing, een meisje aan haar eerste menstruatie."),
    M("Welke cel ligt bij een pasgeboren meisje al in haar eierstokken?",
      "Een eicel die nog moet rijpen",
      ["Een eicel die klaar is voor bevruchting", "Een zaadcel die later rijp wordt", "Een follikel met een gele kleur"],
      "Meisjes worden geboren met onrijpe eicellen in hun eierstokken."),
    M("Welke combinatie van orgaan en functie klopt?",
      "Eierstok: bevat onrijpe eicellen; eileider: vervoert de eicel",
      ["Eileider: bevat onrijpe eicellen; eierstok: vervoert de eicel",
       "Baarmoeder: eicellen laten rijpen; vagina: onrijpe eicellen bewaren",
       "Eierstok: eicel vervoeren; baarmoeder: onrijpe eicellen bevatten"],
      "De eicellen liggen in de eierstokken; de eileider vervoert een eicel naar de baarmoeder."),
    W("Een meisje kan pas zwanger worden als haar eicellen rijp zijn.", True,
      "Waar. Een meisje is vruchtbaar als haar eicellen rijp worden."),
    W("Een eicel bevat weinig voedingsstoffen, zodat hij klein en beweeglijk blijft.", False,
      "Niet waar. Een eicel is groot omdat hij veel voedingsstoffen bevat."),
    W("Zowel de zaadballen als de eierstokken komen bij mensen in tweevoud voor.", True,
      "Waar. Een man heeft twee zaadballen en een vrouw heeft twee eierstokken."),
    W("Een meisje merkt dat ze vruchtbaar is doordat ze een natte droom krijgt.", False,
      "Niet waar. Ze merkt het doordat ze voor het eerst ongesteld is."),
    W("Een rijpende eicel groeit doordat hij vocht en voedingsstoffen opneemt.", True,
      "Waar. Daardoor wordt de eicel rijp."),
    I("Net als bij jongens start de puberteit bij meisjes als de hypofyse ____ afgeeft.", "hormonen|hormoon", "In de puberteit geeft de hypofyse hormonen af; daarna gaan eicellen rijpen."),
    I("De voortplantingscel van een vrouw heet de ____.", "eicel|de eicel|eicellen",
      "De voortplantingscellen van een vrouw zijn eicellen."),
    I("De vagina en de urinebuis van een vrouw zijn twee verschillende ____.", "buizen|buis", "In bron 6 zie je dat de vagina en de urinebuis twee verschillende buizen zijn."),
    I("In bron 6 zie je bij de vrouwelijke geslachtsorganen kleine en ____ schaamlippen.", "grote|grote schaamlippen", "Bij de vrouw horen kleine en grote schaamlippen."),
    O("Leg uit waarom de eierstokken in de puberteit hun eicellen gaan laten rijpen.", ["hypofyse", "hormonen/hormoon/seintje"], 2,
      "De hypofyse geeft hormonen af die de eierstokken een seintje geven, waardoor de eicellen gaan rijpen.",
      "Hormonen uit de hypofyse geven de eierstokken een seintje om eicellen te laten rijpen."),
    O("Waarvoor dient de voorraad voedingsstoffen in een eicel?", ["bevrucht/bevruchting/bevruchten", "nodig"], 2,
      "De voedingsstoffen zijn nodig als de eicel wordt bevrucht.",
      "Ze zijn nodig als een eicel wordt bevrucht.")
]),
49: ("Menstruatiecyclus: verloop en timing", "🧬", [
    M("Een vrouw heeft een cyclus van 28 dagen. Wat gebeurt er op dag 5 in haar eierstok?",
      "Een eicel rijpt in een follikel",
      ["De follikel barst open en de eicel komt vrij", "De eicel gaat dood in de eileider", "Het gele lichaam maakt veel progesteron"],
      "In de eerste veertien dagen rijpt er een eicel in een follikel."),
    M("Wat is er in de baarmoeder veranderd op dag 12 vergeleken met dag 2?",
      "Het slijmvlies is dikker en heeft meer bloedvaten",
      ["Het slijmvlies is volledig losgelaten", "Er zit nu een rijpe eicel in de baarmoeder", "Het slijmvlies is dunner maar beter doorbloed"],
      "Zodra een eicel begint te rijpen wordt het slijmvlies dikker en komen er meer bloedvaten in."),
    M("Wat gebeurt er met de follikel als de eicel niet bevrucht is?",
      "De follikel sterft af",
      ["De follikel groeit uit tot een tweede eicel", "De follikel wordt het nieuwe slijmvlies", "De follikel verhuist naar de baarmoeder"],
      "Bron 7: als de eicel niet bevrucht is, sterft ook de follikel af."),
    M("Een vrouw is ongeveer eens in de 28 dagen ongesteld. Hoeveel menstruaties heeft ze ongeveer in twaalf weken?",
      "Ongeveer drie menstruaties",
      ["Ongeveer twee menstruaties", "Ongeveer vier menstruaties", "Ongeveer zes menstruaties"],
      "28 dagen zijn vier weken, dus in twaalf weken zijn dat ongeveer drie cycli."),
    M("Een vrouw met een cyclus van 28 dagen is op dag 13. Wat geldt voor haar?",
      "Ze zit in haar vruchtbare periode",
      ["Ze heeft nu haar menstruatie", "Haar slijmvlies laat nu los", "Haar eicel is al afgestorven"],
      "De dagen rond de eisprong (ongeveer dag 14) vormen de vruchtbare periode."),
    M("Welke bewering over de menstruatiecyclus is onjuist?",
      "Het baarmoederslijmvlies laat los vlak voor de eisprong",
      ["In de eerste veertien dagen rijpt er een eicel", "De menstruatie volgt als er geen bevruchting is", "De cyclus duurt ongeveer vier weken"],
      "Het slijmvlies laat ongeveer twee weken ná de eisprong los (menstruatie)."),
    M("Hoeveel tijd zit er ongeveer tussen de eisprong en de menstruatie?",
      "Ongeveer veertien dagen later",
      ["Ongeveer twee dagen na elkaar", "Ongeveer zeven dagen later", "Ongeveer een maand later"],
      "Het verdikte slijmvlies laat twee weken na de eisprong los."),
    M("Hoeveel eicellen rijpen er in een gewone cyclus bij een vrouw?",
      "Eén eicel",
      ["Twee eicellen, één in elke eierstok", "Veertien eicellen, één per dag", "Tien tot twintig eicellen"],
      "Bij een vrouw rijpt elke cyclus één eicel."),
    M("Via welke weg kunnen zaadcellen bij de eicel komen?",
      "Via de vagina en de baarmoeder naar de eileider",
      ["Via de urinebuis en de eierstok naar de baarmoeder", "Via de eileider en de baarmoeder naar de vagina", "Via de eierstok en de eileider naar de vagina"],
      "Zaadcellen komen via de vagina en de baarmoeder bij de eicel in de eileider."),
    W("In de eerste helft van de cyclus wordt het baarmoederslijmvlies steeds dikker.", True,
      "Waar. Het slijmvlies wordt dikker en bloedvatrijker."),
    W("De follikel barst open rond dag 28 van de cyclus.", False,
      "Niet waar. De follikel barst rond dag 14 open (ovulatie)."),
    W("Een eicel rijpt in de baarmoeder en komt daarna in de eierstok.", False,
      "Niet waar. De eicel rijpt in de eierstok en komt in de eileider."),
    W("De menstruatie ontstaat doordat een bevruchte eicel zich in het slijmvlies nestelt.", False,
      "Niet waar. Menstruatie volgt juist als de eicel niet is bevrucht."),
    W("Na de menstruatie begint de menstruatiecyclus opnieuw.", True,
      "Waar. Hierna begint de cyclus weer opnieuw."),
    I("Een eicel kan na de eisprong ongeveer 12 tot 24 ____ bevrucht worden.", "uur|uren", "De eicel leeft na de eisprong nog 12 tot 24 uur."),
    I("Het bloed tijdens de menstruatie wordt opgevangen met maandverband of ____.", "tampons|tampon", "Maandverband of tampons vangen het bloed op."),
    I("Een menstruatiecyclus van 28 dagen duurt ____ weken.", "vier|4",
      "28 dagen zijn vier weken."),
    I("Een andere naam voor de eisprong is ____.", "ovulatie|de ovulatie", "Eisprong en ovulatie betekenen hetzelfde."),
    O("Beschrijf wat er gebeurt met de eicel en met het verdikte slijmvlies als er geen bevruchting plaatsvindt.", ["dood/sterft/sterven", "los/loslaten/afgestoten"], 2,
      "De eicel gaat dood en het verdikte slijmvlies laat los en verlaat met wat bloed de vagina.",
      "De eicel sterft en het slijmvlies laat los; dat is de menstruatie."),
    O("Leg uit waarom een vrouw alleen rond de eisprong zwanger kan worden.", ["uur/uren", "bevrucht/bevruchten/bevruchting"], 2,
      "De eicel leeft na de ovulatie maar 12 tot 24 uur en kan alleen in die tijd bevrucht worden.",
      "Na de eisprong leeft de eicel maar 12 tot 24 uur, dus alleen dan is bevruchting mogelijk.")
]),
50: ("Hormonen: FSH, LH, oestrogeen en progesteron", "🧬", [
    M("Een medicijn blokkeert rond dag 14 de werking van LH. Wat is het meest waarschijnlijke gevolg?",
      "Er vindt geen ovulatie plaats",
      ["De follikel groeit niet meer", "Het slijmvlies laat direct los", "De hypofyse maakt geen FSH meer"],
      "Een stijging van LH zorgt voor de ovulatie. Zonder LH blijft de ovulatie uit."),
    M("Een vrouw krijgt in de eerste helft van de cyclus extra progesteron. Wat gebeurt er met FSH en LH?",
      "Ze worden geremd, dus er rijpen geen eicellen",
      ["Ze worden extra aangemaakt, dus er rijpen meer eicellen", "Ze blijven gelijk, dus de eicel rijpt gewoon", "Alleen LH wordt geremd, FSH stijgt juist"],
      "Progesteron remt de hypofysehormonen FSH en LH."),
    M("Welke twee hormonen komen uit de hypofyse?",
      "FSH en LH",
      ["Oestrogeen en LH", "FSH en progesteron", "Oestrogeen en progesteron"],
      "FSH en LH komen uit de hypofyse; oestrogeen en progesteron uit de follikel."),
    M("Wat is de juiste volgorde bij het starten van de ovulatie?",
      "Oestrogeenpiek, LH-stijging, ovulatie",
      ["LH-stijging, oestrogeenpiek, ovulatie", "Ovulatie, oestrogeenpiek, LH-stijging", "Oestrogeenpiek, ovulatie, LH-stijging"],
      "Veel oestrogeen stimuleert LH en de stijging van LH veroorzaakt de ovulatie."),
    M("Wat hebben oestrogeen en progesteron samen gemeen?",
      "Beide laten het baarmoederslijmvlies dikker worden",
      ["Beide starten de ovulatie", "Beide worden vooral vóór de ovulatie gemaakt", "Beide worden door de hypofyse gemaakt"],
      "Volgens bron 13 stimuleren beide hormonen dat het slijmvlies dikker wordt."),
    M("Hoeveel hormonen uit de follikel worden in bron 13 genoemd?",
      "Twee: oestrogeen en progesteron",
      ["Eén: alleen oestrogeen", "Drie: FSH, LH en oestrogeen", "Vier: FSH, LH, oestrogeen en progesteron"],
      "Bron 13 noemt de follikelhormonen oestrogeen en progesteron."),
    M("Welke bewering over de hormonen is onjuist?",
      "FSH wordt gemaakt door de follikel en LH door het gele lichaam",
      ["LH start de ovulatie en stimuleert het gele lichaam", "FSH stimuleert de groei van de follikel", "Oestrogeen remt de productie van FSH"],
      "FSH en LH komen allebei uit de hypofyse."),
    M("Bij welk moment in de cyclus komt het gele lichaam voor?",
      "Na de ovulatie",
      ["Vóór de ovulatie", "Tijdens de menstruatie", "Aan het begin van de cyclus"],
      "Na de ovulatie wordt de lege follikel het gele lichaam."),
    M("Welk hormoon remt de FSH-productie, zodat er niet nog meer eicellen gaan rijpen?",
      "Oestrogeen uit de groeiende follikel",
      ["Progesteron uit de hypofyse", "Testosteron uit de eierstok", "LH uit het gele lichaam"],
      "Oestrogeen remt FSH, waardoor er geen andere eicellen meer rijpen."),
    W("Oestrogeen wordt in de eerste helft van de cyclus gemaakt door de groeiende follikel.", True,
      "Waar. Vóór de ovulatie maakt de follikel vooral oestrogeen."),
    W("Progesteron wordt gemaakt door de hypofyse en laat eicellen rijpen.", False,
      "Niet waar. Progesteron komt uit het gele lichaam en remt FSH en LH."),
    W("Als de productie van oestrogeen en progesteron stopt, start de hypofyse weer met FSH.", True,
      "Waar. Daardoor begint de cyclus opnieuw."),
    W("De follikel wordt het gele lichaam voordat de ovulatie plaatsvindt.", False,
      "Niet waar. Pas ná de ovulatie wordt de lege follikel het gele lichaam."),
    W("Oestrogeen kan zowel de FSH-productie remmen als de LH-productie starten.", True,
      "Waar. Oestrogeen remt FSH; een grote hoeveelheid stimuleert LH."),
    I("FSH staat voor follikel ____ hormoon.", "stimulerend",
      "FSH is het follikel stimulerend hormoon."),
    I("De lege follikel wordt geel doordat hij geel gekleurd ____ opneemt.", "vet",
      "Hij neemt geel gekleurd vet op."),
    I("Het gele lichaam wordt ook wel het corpus ____ genoemd.", "luteum",
      "Corpus luteum is de andere naam."),
    I("Hormonen uit de hypofyse en de follikel regelen samen de ____.", "menstruatiecyclus|de menstruatiecyclus|cyclus",
      "Bron 12 laat zien hoe dat gaat."),
    O("Leg uit waarom er in de tweede helft van de cyclus geen nieuwe ovulatie plaatsvindt.", ["progesteron", "remt/remmen/geremd"], 2,
      "Het gele lichaam maakt progesteron en dat remt de hypofysehormonen, waardoor er geen eicellen rijpen en geen ovulatie komt.",
      "Progesteron remt FSH en LH, dus er is geen nieuwe eisprong."),
    O("Beschrijf hoe een nieuwe menstruatiecyclus begint nadat de productie van oestrogeen en progesteron is gestopt.", ["hypofyse", "FSH/follikel"], 2,
      "De hypofyse start weer met FSH, waardoor een nieuwe follikel gaat groeien en de cyclus opnieuw begint.",
      "De hypofyse maakt weer FSH en de follikel gaat groeien.")
]),
51: ("Man en vrouw vergeleken", "🧬", [
    M("Welke overeenkomst bestaat er tussen een zaadbal en een eierstok?",
      "In beide organen bevinden zich voortplantingscellen",
      ["Beide organen maken testosteron aan", "Beide organen slaan sperma op", "Beide organen liggen in de balzak"],
      "Zaadcellen ontstaan in de zaadballen, eicellen liggen in de eierstokken."),
    M("Wat is het verschil tussen een ovulatie en een zaadlozing?",
      "Bij een ovulatie komt een eicel vrij; bij een zaadlozing komt sperma naar buiten",
      ["Bij een ovulatie komt sperma vrij; bij een zaadlozing komt een eicel naar buiten",
       "Bij een ovulatie komen eicellen en zaadvocht vrij; bij een zaadlozing alleen zaadcellen",
       "Bij een ovulatie komt bloed vrij; bij een zaadlozing komt een eicel naar buiten"],
      "De rijpe eicel komt bij de ovulatie vrij uit de eierstok. Bij een zaadlozing komt het sperma via de penis naar buiten."),
    M("Welk orgaan geeft bij zowel jongens als meisjes in de puberteit hormonen af?",
      "De hypofyse",
      ["De prostaat", "De baarmoeder", "De bijbal"],
      "De puberteit start bij jongens en meisjes als de hypofyse hormonen afgeeft."),
    M("Wat hebben de zaadleider en de eileider met elkaar gemeen?",
      "Beide vervoeren voortplantingscellen",
      ["Beide voegen vocht toe aan de cellen", "Beide laten de cellen rijpen", "Beide maken hormonen aan"],
      "De zaadleider vervoert zaadcellen, de eileider vervoert eicellen."),
    M("Welke uitspraak over het aantal voortplantingscellen is juist?",
      "Een man maakt per dag meer zaadcellen dan een meisje bij de geboorte eicellen heeft",
      ["Een meisje heeft bij de geboorte meer eicellen dan een man in een week zaadcellen maakt",
       "Een man maakt per dag evenveel zaadcellen als een meisje eicellen heeft",
       "Een vrouw maakt per dag meer eicellen dan een man zaadcellen"],
      "Zeventig miljoen zaadcellen per dag is veel meer dan ongeveer 400 000 onrijpe eicellen."),
    M("Via het bloed bereiken hormonen uit de hypofyse bij een meisje welk orgaan?",
      "De eierstokken",
      ["De baarmoeder", "De vagina", "De eileiders"],
      "Hormonen uit de hypofyse geven de eierstokken een seintje."),
    M("Waarom krijgt een loopse teef soms een broekje aan?",
      "Om het bloed op te vangen",
      ["Om reuen af te schrikken met een lokstof", "Om haar warm te houden na de eisprong", "Om de eisprong sneller op gang te brengen"],
      "Een broekje vangt het bloed op van de gezwollen schaamlippen."),
    M("Wanneer krijgt een teefje belangstelling voor reuen?",
      "Na de eisprong",
      ["Voor de eisprong", "Tijdens de eerste dag van het bloedverlies", "Een half jaar na de eisprong"],
      "Na de eisprong krijgt het teefje interesse in mannetjeshonden."),
    M("Wat gebeurt er met een eicel van een teefje als er geen bevruchting plaatsvindt?",
      "De eicel sterft",
      ["De eicel rijpt nog een tweede keer", "De eicel verlaat het lichaam met de urine", "De eicel blijft rijp tot het volgende half jaar"],
      "Als er geen bevruchting is, sterft de eicel."),
    W("Zowel zaadballen als follikels maken hormonen.", True,
      "Waar. Zaadballen maken testosteron, follikels oestrogeen en progesteron."),
    W("Alleen bij vrouwen speelt de hypofyse een rol bij de voortplanting.", False,
      "Niet waar. Bij jongens zorgen hormonen uit de hypofyse ook voor het starten van de zaadcelproductie."),
    W("De menstruatiecyclus van een vrouw wordt net als de puberteit geregeld door hormonen.", True,
      "Waar. De hypofyse en de follikel regelen de cyclus met hormonen."),
    W("Feromonen zijn hormonen uit de hypofyse.", False,
      "Niet waar. Feromonen zijn lokstoffen in de urine."),
    W("De voedingsstoffen in de eicel zijn nodig wanneer de eicel wordt bevrucht.", True,
      "Waar. Daarom is de eicel groot."),
    I("In de zaadballen worden per dag wel ____ miljoen zaadcellen gemaakt.", "zeventig|70",
      "Er worden wel zeventig miljoen zaadcellen per dag gemaakt."),
    I("Bij vogels ontbreekt de baarmoeder, daarom komt er bij hen geen ____ voor.", "menstruatie|de menstruatie", "Zonder baarmoeder geen menstruatie; vogels hebben wel een eisprong."),
    I("Naast de mens menstrueren ook de mensapen, zoals de ____.", "chimpansee|chimpansees|de chimpansee",
      "Mensapen zoals chimpansees menstrueren."),
    I("Vrouwtjeskippen hebben iedere ____ een eisprong.", "dag",
      "Hennen hebben dagelijks een eisprong."),
    O("Noem twee overeenkomsten tussen de puberteit van jongens en van meisjes.", ["hypofyse/hormonen", "vruchtbaar"], 2,
      "Bij beiden geeft de hypofyse hormonen af en na de puberteit zijn ze vruchtbaar.",
      "De hypofyse geeft hormonen af en daarna zijn jongens en meisjes vruchtbaar."),
    O("Noem twee kenmerken waaraan je ziet dat een teefje loops is.", ["schaamlippen/schaamlip", "bloed"], 2,
      "De schaamlippen zwellen op en ze verliest wat bloed.",
      "Gezwollen schaamlippen en een beetje bloedverlies.")
])
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_1_extra2_seed_47')
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        mcs = [v for v in vr if v["type"] == "mc"]
        k = sum(all(len(o) > len(v["opties"][v["antwoord"]]) for i, o in enumerate(v["opties"]) if i != v["antwoord"]) for v in mcs)
        assert k / len(mcs) <= 0.4, f"examen_{nr}: juiste optie {k}/{len(mcs)} keer kortste"
        assert sum(v["type"] == "waaronwaar" and v["antwoord"] is False for v in vr) >= 2
        ex = {
            "id": f"ex-h3-biologie-{nr}",
            "hoofdstuk": 11,
            "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
            "paragraaf": "11.1",
            "titel": f"Toets {nr} — §11.1 {sub}",
            "vak": "Biologie · HAVO 3 (H11.1)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie H11.1) — gegenereerd door tools/gen_biologie_h11_1_extra2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
