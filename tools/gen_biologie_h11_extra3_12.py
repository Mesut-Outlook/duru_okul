#!/usr/bin/env python3
"""Biologie HAVO 3 · Hoofdstuk 11 Voortplanting · §11.1 & §11.2 zwakte-toetsen (examen_67..70).
Schrijft havo3/biologie/js/data/examen_67..70.js (ex-h3-biologie-67..70).
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


def kortste_aandeel(vragen):
    mcs = [v for v in vragen if v["type"] == "mc"]
    n = sum(all(len(o) > len(v["opties"][v["antwoord"]]) for i, o in enumerate(v["opties"]) if i != v["antwoord"]) for v in mcs)
    return n, len(mcs)


EXAMENS = {
67: ("11.1", "De mannelijke geslachtsorganen, zaadcellen en erectie", "♂️", [
    M("Waar worden zaadcellen bewaard tot de zaadlozing?",
      "In de bijballen",
      ["In de zaadblaasjes", "In de prostaat", "In de zaadleiders"],
      "Zaadcellen worden gemaakt in de zaadballen en bewaard in de bijballen tot de zaadlozing."),
    M("In welk orgaan ontstaan de zaadcellen?",
      "In de zaadballen",
      ["In de bijballen", "In de prostaat", "In de zaadblaasjes"],
      "In de zaadballen worden wel 70 miljoen zaadcellen per dag gemaakt."),
    M("Welke organen leveren het zaadvocht dat bij de zaadcellen komt?",
      "De zaadblaasjes en de prostaat",
      ["De bijballen en de zaadleiders", "De urineblaas en de urinebuis", "De zaadballen en de bijballen"],
      "De zaadblaasjes en de prostaat voegen zaadvocht toe. Zaadvocht met zaadcellen heet samen sperma."),
    M("Wat gebeurt er in de penis bij een erectie?",
      "Extra bloed vult de bloedvaten in de penis",
      ["De penis vult zich met zaadvocht", "De spieren in de penis trekken samen", "De zaadleiders trekken de penis stijf"],
      "Bij seksuele opwinding gaat er extra bloed naar de zwellichamen in de penis. Daardoor wordt de penis stijf."),
    M("Welke weg leggen zaadcellen af tot ze het lichaam verlaten?",
      "Zaadbal, bijbal, zaadleider, urinebuis",
      ["Bijbal, zaadbal, urinebuis, zaadleider", "Zaadbal, zaadleider, bijbal, urinebuis", "Zaadleider, zaadbal, bijbal, urinebuis"],
      "Zaadcellen ontstaan in de zaadbal, worden bewaard in de bijbal en gaan via de zaadleider en de urinebuis naar buiten."),
    M("Wat voorkomt dat urine meekomt bij de zaadlozing?",
      "Een spiertje knijpt de urinebuis dicht",
      ["De prostaat maakt de urine dikker", "De zaadleiders nemen de urine op", "De nieren maken even geen urine"],
      "Een spiertje tussen de prostaat en de urineblaas knijpt de urinebuis dicht, dus er komt geen urine mee."),
    M("Welk orgaan zet in de puberteit de zaadballen aan het werk?",
      "De hypofyse",
      ["De prostaat", "De bijbal", "De zaadleider"],
      "Hormonen uit de hypofyse komen via het bloed bij de zaadballen. Dan gaan ze zaadcellen maken."),
    M("Hoeveel zaadballen en bijballen heeft een man?",
      "Twee van elk",
      ["Eén van elk", "Twee zaadballen en één bijbal", "Eén zaadbal en twee bijballen"],
      "Een man heeft twee zaadballen en twee bijballen."),
    M("Wat is de eerste stap van een zaadlozing?",
      "Spiertjes in de bijballen persen de zaadcellen de zaadleiders in",
      ["Spiertjes in de prostaat persen de zaadcellen de urinebuis in",
       "De zaadblaasjes persen de zaadcellen de bijballen in",
       "Spiertjes in de zaadballen persen zaadvocht naar de blaas"],
      "Eerst persen spiertjes in de bijballen de zaadcellen de zaadleiders in. Daarna komt er zaadvocht bij."),
    W("Zaadcellen worden gemaakt in de bijballen.", False,
      "Niet waar. Zaadcellen worden gemaakt in de zaadballen en bewaard in de bijballen."),
    W("Tijdens een natte droom heeft een jongen een zaadlozing.", True,
      "Waar. Een natte droom is een zaadlozing in de slaap."),
    W("Een jongen is vruchtbaar vanaf zijn eerste zaadlozing.", True,
      "Waar. Vanaf dat moment maakt hij zaadcellen en kan hij een meisje zwanger maken."),
    W("Zaadvocht komt uit de zaadblaasjes en de prostaat.", True,
      "Waar. Die twee organen voegen zaadvocht toe aan de zaadcellen."),
    W("Tijdens een zaadlozing kan er ook urine uit de penis komen.", False,
      "Niet waar. Een spiertje knijpt de urinebuis dicht, dus er komt geen urine mee."),
    I("Zaadcellen samen met zaadvocht noemen we ____.", "sperma",
      "Zaadvocht en zaadcellen samen heten sperma."),
    I("Het zakje waarin de zaadballen en bijballen liggen, heet de ____.", "balzak|de balzak",
      "De zaadballen en bijballen liggen in de balzak."),
    I("De penis wordt stijf doordat extra bloed naar de ____ gaat.", "zwellichamen|de zwellichamen",
      "De zwellichamen in de penis vullen zich met bloed."),
    I("Het hormoon dat de zaadballen maken heet ____.", "testosteron",
      "Door testosteron blijven de zaadballen zaadcellen maken."),
    O("Op welke manier bereiken de hormonen uit de hypofyse de zaadballen?",
      ["bloed/bloedbaan", "vervoerd/transport/stroomt"], 2,
      "De hormonen worden vanuit de hypofyse met het bloed vervoerd naar de zaadballen.",
      "Via het bloed worden de hormonen naar de zaadballen vervoerd."),
    O("Waarom kan een jongen na zijn eerste zaadlozing een meisje zwanger maken?",
      ["zaadcellen/zaadcel", "bevrucht/bevruchten/eicel/zwanger"], 2,
      "Hij maakt dan zaadcellen. Een zaadcel kan een eicel bevruchten.",
      "Hij maakt zaadcellen die een eicel kunnen bevruchten.")
]),

68: ("11.1", "De vrouwelijke organen, eicellen en de hormooncyclus", "♀️", [
    M("Hoe liggen de vagina en de urinebuis bij een vrouw?",
      "Het zijn twee buizen met elk een eigen opening",
      ["Ze komen uit in één gemeenschappelijke opening", "De vagina mondt uit in de urinebuis", "De urinebuis mondt uit in de baarmoeder"],
      "De vagina en de urinebuis zijn twee verschillende buizen met twee verschillende openingen."),
    M("Een eicel is groter dan een zaadcel. Hoe komt dat?",
      "Ze bevat veel voedingsstoffen voor later",
      ["Ze heeft veel meer celkernen dan een zaadcel", "Ze heeft een lange staart om te kunnen zwemmen", "Ze bevat veel vocht uit de eileider"],
      "Een eicel bevat veel voedingsstoffen. Die zijn nodig als de eicel wordt bevrucht."),
    M("Wat is een eisprong?",
      "De eicel komt uit het blaasje in de eileider",
      ["Het slijmvlies laat los en komt naar buiten", "De zaadcel en de eicel smelten samen", "Het bolletje cellen zet zich vast in het slijmvlies"],
      "Na ongeveer veertien dagen is de eicel rijp. Het blaasje barst open en de eicel komt in de eileider."),
    M("Wat gebeurt er door de stijging van LH?",
      "De eisprong treedt op",
      ["De menstruatie begint", "Er gaat een nieuwe eicel rijpen", "Het slijmvlies wordt dikker"],
      "Door de stijging van LH treedt de ovulatie op."),
    M("Wat gebeurt er na de ovulatie met het lege blaasje in de eierstok?",
      "Het groeit en neemt geel vet op",
      ["Het verdwijnt direct uit de eierstok", "Het wordt een nieuwe onrijpe eicel", "Het groeit uit tot de placenta"],
      "Het lege blaasje groeit en neemt geel gekleurd vet op. Het heet dan het gele lichaam."),
    M("Hoeveel eicellen heeft een meisje bij de geboorte ongeveer?",
      "Ongeveer 400 000",
      ["Ongeveer 70 miljoen", "Ongeveer 28", "Ongeveer 14"],
      "Meisjes worden geboren met ongeveer 400 000 onrijpe eicellen in de eierstokken."),
    M("Wat doet het hormoon FSH aan het begin van de cyclus?",
      "Het laat een blaasje met een eicel groeien",
      ["Het laat de eisprong plaatsvinden", "Het houdt het slijmvlies dik en doorbloed", "Het remt de rijping van eicellen"],
      "FSH uit de hypofyse stimuleert de groei van het blaasje waarin de eicel rijpt."),
    M("Wat gebeurt er met het slijmvlies als er geen bevruchting is?",
      "Het slijmvlies laat los en gaat met wat bloed naar buiten",
      ["Het slijmvlies wordt dikker tot de volgende cyclus", "Het slijmvlies wordt in het bloed opgenomen", "Het slijmvlies gaat naar de eileiders"],
      "Het verdikte slijmvlies laat los en druppelt met wat bloed uit de vagina. Dat is de menstruatie."),
    M("Hoelang blijft een eicel na de eisprong in leven?",
      "12 tot 24 uur",
      ["Ongeveer 3 dagen", "Ongeveer 6 dagen", "Ongeveer 2 weken"],
      "Na de eisprong blijft de eicel 12 tot 24 uur in de eileider leven."),
    W("Zonder bevruchting laat het slijmvlies ongeveer twee weken na de ovulatie los.", True,
      "Waar. Dan begint de menstruatie."),
    W("Vanaf de puberteit is een meisje ongeveer eens in de 28 dagen ongesteld.", True,
      "Waar. Vanaf de puberteit rijpen er eicellen en is een meisje ongeveer eens in de vier weken ongesteld: de menstruatiecyclus."),
    W("Aan het begin van de cyclus geeft de hypofyse FSH af.", True,
      "Waar. FSH stimuleert de groei van het blaasje met de eicel."),
    W("In de puberteit worden bij een meisje nieuwe eicellen gevormd.", False,
      "Niet waar. Ze wordt geboren met ongeveer 400 000 onrijpe eicellen. In de puberteit gaan ze rijpen."),
    W("Een teef die loops is, menstrueert net als een mens.", False,
      "Niet waar. Alleen mensapen menstrueren. Een teef die loops is verliest bloed, maar dat komt niet uit de baarmoeder."),
    I("Het blaasje met vocht rond de rijpende eicel noem je de ____.", "follikel|de follikel",
      "De eicel rijpt in een blaasje, de follikel."),
    I("Het hormoon dat het slijmvlies na de ovulatie dik houdt, heet ____.", "progesteron",
      "Progesteron remt FSH en LH en houdt het slijmvlies dik en goed doorbloed."),
    I("Na de ovulatie krijgt het lege blaasje een nieuwe naam: het ____ ____ (twee woorden).", "gele lichaam|het gele lichaam|corpus luteum",
      "Het gele lichaam (corpus luteum) maakt progesteron."),
    I("Het blaasje met de eicel maakt vóór de ovulatie een hormoon dat FSH remt: ____.", "oestrogeen",
      "Oestrogeen remt FSH, dus er rijpt maar één eicel tegelijk."),
    O("Waarom begint de menstruatie als de eicel niet bevrucht is?",
      ["hormoon/hormonen/oestrogeen/progesteron", "afneemt/daalt/dalen/minder/afnemen/nemen af/neemt af"], 2,
      "De productie van oestrogeen en progesteron neemt af. Daardoor laat het slijmvlies los.",
      "De hormonen oestrogeen en progesteron nemen af, dus het slijmvlies laat los."),
    O("Welke invloed heeft de hypofyse op de start van de eicelrijping in de puberteit?",
      ["hormonen/hormoon/FSH", "eierstok/eierstokken/rijpen/follikel"], 2,
      "De hypofyse geeft hormonen af aan het bloed. Die geven de eierstokken een seintje om eicellen te laten rijpen.",
      "De hypofyse geeft hormonen af die de eierstokken aanzetten tot rijping.")
]),

69: ("11.2", "Bevruchting, deling, kiemschijf, vlokken en HCG", "🔬", [
    M("Waar vindt de bevruchting meestal plaats?",
      "In de eileider",
      ["In de baarmoeder", "In de vagina", "In de eierstok"],
      "De zaadcellen zwemmen de eileider in. Daar komen ze de rijpe eicel tegen."),
    M("Wat gebeurt er met de eicel als één zaadcel is binnengedrongen?",
      "Andere zaadcellen kunnen de eicel niet meer binnen",
      ["De eicel valt uit elkaar", "De eicel gaat dood", "De eicel stuurt de zaadcel terug"],
      "De buitenste laag van de eicel wordt ondoordringbaar. Zo bevrucht maar één zaadcel de eicel."),
    M("Waaruit ontstaat het embryo?",
      "Uit een groepje cellen binnenin het bolletje",
      ["Uit de buitenste cellen van het bolletje", "Uit de holte in het bolletje", "Uit het baarmoederslijmvlies"],
      "Binnenin het bolletje zit een groepje cellen. Daaruit ontstaat het embryo."),
    M("Wat doen de vlokken die in het baarmoederslijmvlies groeien?",
      "Ze nemen voeding en zuurstof op uit moederbloed",
      ["Ze breken het baarmoederslijmvlies weer af", "Ze duwen het bolletje terug naar de eileider", "Ze maken de zaadcellen in de eileider onschadelijk"],
      "De vlokken nemen voedingsstoffen en zuurstof op uit het bloed van de moeder en geven afvalstoffen af."),
    M("Wat doet het zwangerschapshormoon met de eierstok?",
      "Er gaat geen nieuwe eicel rijpen",
      ["Er komen twee eicellen tegelijk vrij", "De eisprong gebeurt vaker", "De eierstok maakt zaadcellen"],
      "Het zwangerschapshormoon voorkomt dat er een nieuwe eicel gaat rijpen."),
    M("Wat doet het zwangerschapshormoon met het baarmoederslijmvlies?",
      "Het slijmvlies wordt niet afgestoten",
      ["Het slijmvlies laat meteen los", "Het slijmvlies wordt dunner", "Het slijmvlies groeit uit tot placenta"],
      "Dankzij dit hormoon blijft het slijmvlies zitten. Een zwangere vrouw wordt dus niet ongesteld."),
    M("Wat toont een zwangerschapstest aan in de urine?",
      "Het zwangerschapshormoon",
      ["Zaadcellen", "Eicellen", "Het hormoon FSH"],
      "Een zwangerschapstest toont het zwangerschapshormoon aan in de urine."),
    M("Wat vormen de vlokken later in de baarmoeder?",
      "De placenta",
      ["Het hartje van het kindje", "De baarmoeder", "De eierstok"],
      "De vlokken groeien in het baarmoederslijmvlies en worden later de placenta."),
    M("Na hoeveel dagen zet het bolletje cellen zich vast in het slijmvlies?",
      "Na ongeveer zes dagen",
      ["Na ongeveer twee dagen", "Na ongeveer twaalf dagen", "Na ongeveer vier weken"],
      "Na ongeveer zes dagen zet het bolletje zich vast in het baarmoederslijmvlies."),
    W("Bevruchting is het versmelten van de kern van een zaadcel met de kern van een eicel.", True,
      "Waar. Er ontstaat dan één nieuwe kern."),
    W("Een zwangerschapstest toont zaadcellen aan in de urine.", False,
      "Niet waar. De test toont het zwangerschapshormoon aan."),
    W("Een zwangere vrouw wordt gewoon om de 28 dagen ongesteld.", False,
      "Niet waar. Het slijmvlies blijft zitten, dus er is geen menstruatie."),
    W("De vlokken van het embryo worden later de placenta.", True,
      "Waar. De vlokken groeien in het slijmvlies en worden de placenta."),
    W("Zaadcellen kunnen enkele dagen in het lichaam van de vrouw leven.", True,
      "Waar. Ze kunnen in de eileider enkele dagen overleven."),
    I("Na ongeveer zes dagen zet het bolletje zich vast. Dat noem je de ____.", "innesteling|de innesteling",
      "Na ongeveer zes dagen zet het bolletje zich vast. Dat heet innesteling."),
    I("Uit welk groepje cellen in het bolletje groeit het embryo? Uit de ____.", "kiemschijf|de kiemschijf",
      "Uit de kiemschijf ontstaat het embryo."),
    I("Het zwangerschapshormoon dat de vlokken maken, wordt afgekort als ____.", "HCG|hcg",
      "HCG zorgt dat het slijmvlies niet wordt afgestoten."),
    I("Uit de steel bij het embryo ontstaat later de ____.", "navelstreng|de navelstreng",
      "Uit de steel ontstaat de navelstreng."),
    O("Waarom wordt het baarmoederslijmvlies niet afgestoten als je zwanger bent?",
      ["geel lichaam/gele lichaam/corpus luteum", "progesteron"], 2,
      "Het zwangerschapshormoon zorgt dat het gele lichaam progesteron blijft maken. Daardoor blijft het slijmvlies dik.",
      "Het gele lichaam blijft progesteron maken."),
    O("Welke twee stoffen nemen de vlokken op uit het bloed van de moeder?",
      ["voedingsstoffen/voedsel/nutriënten", "zuurstof/O2"], 2,
      "De vlokken nemen voedingsstoffen en zuurstof op uit het bloed van de moeder.",
      "Voedingsstoffen en zuurstof.")
]),

70: ("11.2", "Anticonceptie, voorbehoedmiddelen en noodgevallen", "🛡️", [
    M("Welk voorbehoedmiddel beschermt ook tegen soa's?",
      "Het condoom",
      ["De pil", "Het hormoonstaafje", "De pleister"],
      "Alleen een condoom beschermt ook tegen soa's."),
    M("Hoe werkt de pil?",
      "Er rijpen geen eicellen, dus geen eisprong",
      ["De zaadcellen worden gedood in de vagina", "De eileiders worden permanent afgesloten door de pil", "Het baarmoederslijmvlies lost helemaal op"],
      "De pil houdt de eisprong tegen. Ook wordt het slijm bij de baarmoedermond dikker."),
    M("Waar zit een hormoonstaafje?",
      "Onder de huid",
      ["In de baarmoeder", "In de eierstok", "In de vagina"],
      "Het hormoonstaafje zit onder de huid en geeft hormonen af die de eisprong tegenhouden."),
    M("Wat gebeurt er bij de sterilisatie van een man?",
      "De zaadleiders worden doorgesneden",
      ["De zaadballen worden weggehaald", "De prostaat wordt weggehaald", "De urinebuis wordt dichtgemaakt"],
      "Bij sterilisatie worden de zaadleiders doorgesneden. Dat is definitief."),
    M("Heeft een gesteriliseerde man nog een zaadlozing?",
      "Ja, maar het zaadvocht bevat geen zaadcellen",
      ["Nee, er komt helemaal niets meer uit", "Nee, hij kan geen erectie meer krijgen", "Ja, maar het is alleen urine"],
      "De zaadblaasjes en de prostaat maken nog zaadvocht. Er zitten alleen geen zaadcellen meer in."),
    M("Waarom is coïtus interruptus onbetrouwbaar?",
      "Er zitten al zaadcellen in het vocht vooraf",
      ["De eisprong is dan altijd al voorbij", "De vrouw is dan juist niet vruchtbaar", "De zaadcellen kunnen niet in de eileider komen"],
      "Ook vóór het klaarkomen kan er al vocht met zaadcellen uit de penis komen."),
    M("Hoelang na seks kun je de morning-afterpil nog innemen?",
      "Tot uiterlijk 72 uur",
      ["Tot uiterlijk 12 uur", "Tot uiterlijk 7 dagen", "Tot uiterlijk 4 weken"],
      "De morning-afterpil moet binnen 72 uur worden ingenomen. Hoe eerder, hoe beter."),
    M("Hoe werkt het voorbehoedmiddel dat een arts in de baarmoeder plaatst?",
      "Zaadcellen worden minder vruchtbaar",
      ["Het sluit de eileiders af", "Het doodt alle zaadcellen in de vagina", "Het remt de eisprong met hormonen onder de huid"],
      "Het maakt zaadcellen minder vruchtbaar en voorkomt dat een bevruchte eicel zich innestelt."),
    M("Tot hoeveel weken mag een arts een embryo laten verwijderen?",
      "Tot 24 weken zwangerschap",
      ["Tot 6 weken zwangerschap", "Tot 12 weken zwangerschap", "Tot 36 weken zwangerschap"],
      "Dat mag alleen als de vrouw niet langer dan 24 weken zwanger is."),
    W("Een gesteriliseerde vrouw heeft doorgesneden eileiders.", True,
      "Waar. Daardoor kunnen zaadcellen de eicel niet meer bereiken."),
    W("De pil beschermt ook tegen soa's.", False,
      "Niet waar. Alleen een condoom beschermt ook tegen soa's."),
    W("Bij coïtus interruptus weet je zeker dat een vrouw niet zwanger wordt.", False,
      "Niet waar. In het vocht dat eerder vrijkomt kunnen al zaadcellen zitten."),
    W("De morning-afterpil onderdrukt de ovulatie en voorkomt innesteling.", True,
      "Waar. Daarom moet je hem snel innemen."),
    W("Periodieke onthouding is een betrouwbaar voorbehoedmiddel.", False,
      "Niet waar. De eisprong is moeilijk te bepalen en hoeft niet op de 14e dag te zijn."),
    I("Het vocht dat al vóór het klaarkomen uit de penis kan komen en zaadcellen kan bevatten, heet ____.", "voorvocht|het voorvocht",
      "In het voorvocht kunnen al zaadcellen zitten."),
    I("De twee hormonen in de pil zijn oestrogeen en ____.", "progesteron",
      "De pil bevat oestrogeen en progesteron."),
    I("Een arts plaatst dit voorbehoedmiddel in de baarmoeder. Om het steeltje zit een koperdraad. Het heet het ____.", "spiraaltje|het spiraaltje",
      "Een spiraaltje wordt door een arts in de baarmoeder geplaatst."),
    I("Een vrouw die niet zwanger wil blijven, kan in een kliniek een ____ laten doen.", "abortus|een abortus",
      "Een abortus mag alleen tot 24 weken zwangerschap."),
    O("Waarom blijft een gesteriliseerde vrouw elke maand ongesteld worden?",
      ["eierstok/eierstokken/hormonen", "slijmvlies/baarmoeder"], 2,
      "De eierstokken maken nog hormonen. Daardoor wordt het slijmvlies elke maand dikker en laat het weer los.",
      "De eierstokken werken door en het slijmvlies laat los."),
    O("Welke twee dingen doet de pil om zwangerschap te voorkomen?",
      ["eisprong/ovulatie/rijping/rijpen", "slijm/baarmoedermond/dikker/taaier"], 2,
      "De pil houdt de rijping van eicellen en de eisprong tegen. Ook wordt het slijm bij de baarmoedermond dikker.",
      "Geen eisprong en dikker slijm bij de baarmoedermond.")
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_extra3_seed_67_70')
    for nr, (paragraaf, sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        vr = plaats([dict(v) for v in vr], rng)
        n_l, tot = langste_aandeel(vr)
        assert n_l / tot <= 0.4, f"examen_{nr}: juiste optie {n_l}/{tot} keer langste (>0.4)"
        n_k, _ = kortste_aandeel(vr)
        assert n_k / tot <= 0.4, f"examen_{nr}: juiste optie {n_k}/{tot} keer kortste (>0.4)"
        ex = {
            "id": f"ex-h3-biologie-{nr}",
            "hoofdstuk": 11,
            "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
            "paragraaf": paragraaf,
            "titel": f"Toets {nr} — §{paragraaf} {sub}",
            "vak": f"Biologie · HAVO 3 (H{paragraaf})",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie H{paragraaf}) — gegenereerd door tools/gen_biologie_h11_extra3_12.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr} (§{paragraaf}): 20 vragen, juiste langste {n_l}/{tot}, kortste {n_k}/{tot}")


if __name__ == '__main__':
    main()
