#!/usr/bin/env python3
"""Biologie HAVO 3 · Hoofdstuk 11 Voortplanting · §11.3 Zwangerschap + §11.4 Je lijkt op ... (extra toetsen 71-74).
Schrijft havo3/biologie/js/data/examen_71..74.js (ex-h3-biologie-71..74).
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
71: ("Navelstreng, placenta en schadelijke stoffen", "🩸", [
    M("Een verpleegkundige telt de bloedvaten in een navelstreng. Wat vindt ze?",
      "Twee slagaders en één ader",
      ["Twee aders en één slagader", "Eén slagader en één ader", "Alleen aders, geen slagaders"],
      "Door de navelstreng lopen één navelstrengader en twee navelstrengslagaders."),
    M("Via welk bloedvat gaan afvalstoffen van het kindje naar de moeder?",
      "Via een navelstrengslagader",
      ["Via de navelstrengader", "Via de vruchtvliezen die om de foetus zitten", "Via de baarmoederwand zelf"],
      "De twee navelstrengslagaders vervoeren afvalstoffen van het kindje naar de moeder."),
    M("Waarin verschilt het bloed in de navelstrengader van het bloed in de navelstrengslagaders?",
      "Het bevat meer zuurstof en voedingsstoffen",
      ["Het bevat meer afvalstoffen", "Het bevat precies evenveel zuurstof", "Het stroomt van de foetus naar de placenta"],
      "De ader brengt zuurstof en voedingsstoffen naar het kindje; de slagaders voeren afvalstoffen af."),
    M("Wat gebeurt er in de placenta met het bloed van moeder en kind?",
      "Het stroomt dicht langs elkaar zonder te mengen",
      ["Het mengt zich tot één bloedstroom", "Het bloed van het kind stroomt de bloedvaten van de moeder in", "Het wordt gescheiden door een dikke spierlaag"],
      "De bloedvaten liggen dicht langs elkaar met dunne wanden; stoffen worden uitgewisseld, het bloed mengt niet."),
    M("Waar in het lichaam van de zwangere vrouw groeit de placenta?",
      "Op de plek in de baarmoeder waar de bevruchte eicel zich innestelde",
      ["In de eileider naast de eierstok", "Onderaan bij de vagina", "Aan de buitenkant van de baarmoeder"],
      "Op de plaats van de innesteling groeit de moederkoek of placenta."),
    M("Een vrouw rookt elke dag tijdens haar zwangerschap. Welk gevolg heeft dat voor het ongeboren kind?",
      "De stof uit sigaretten komt via de placenta bij het kind, dat slechter gaat groeien",
      ["De placenta houdt de stof volledig tegen, maar de rook beschadigt de vruchtvliezen", "De stof gaat via de navelstrengslagaders naar het kind en veroorzaakt FAS", "Alleen de moeder wordt er ziek van"],
      "Nicotine uit sigaretten komt via de placenta bij het embryo: het groeit slechter, kan afwijkingen krijgen of doodgaan. FAS komt van alcohol."),
    M("Welke uitspraak over de placenta als filter klopt?",
      "Veel schadelijke stoffen worden tegengehouden, maar alcohol en drugs komen er wél doorheen",
      ["Alle schadelijke stoffen worden tegengehouden, dus roken en drinken zijn veilig", "De placenta laat alleen zuurstof en voedingsstoffen door", "Alcohol wordt tegengehouden, maar het rodehondvirus komt er wél door"],
      "De placenta houdt veel schadelijke stoffen en ziekteverwekkers tegen, maar alcohol, drugs, nicotine en het rodehondvirus komen er wél doorheen."),
    M("Uit welke onderdelen bestaat de 'zak' waarin het kindje veilig ligt?",
      "Vruchtvliezen met vruchtwater",
      ["Placenta met navelstreng", "Baarmoederwand met placenta", "Navelstreng met vruchtvliezen"],
      "De zak bestaat uit vruchtvliezen met vruchtwater; placenta en navelstreng horen daar niet bij."),
    M("Een zwangere vrouw eet een appel. Welke weg leggen de voedingsstoffen af naar het kind?",
      "Bloed van de moeder, placenta, navelstrengader, foetus",
      ["Bloed van de moeder, vruchtwater, navelstrengslagader, foetus", "Maag van de moeder, vruchtvliezen, navelstreng, foetus", "Bloed van de foetus, placenta, navelstrengslagader, moeder"],
      "Voedingsstoffen gaan van het bloed van de moeder via de placenta en de navelstrengader naar het kindje."),
    W("Door de navelstreng lopen twee aders en één slagader.", False,
      "Niet waar. Er lopen één navelstrengader en twee navelstrengslagaders doorheen."),
    W("In de placenta stroomt het bloed van de moeder rechtstreeks het lichaam van het kind in.", False,
      "Niet waar. De bloedvaten liggen dicht langs elkaar, maar het bloed mengt niet; stoffen gaan door de dunne wanden."),
    W("Het rodehondvirus kan via de placenta bij het embryo komen.", True,
      "Waar. Ook alcohol, drugs en nicotine kunnen via de placenta bij het embryo komen."),
    W("Afvalstoffen van het kindje gaan via de navelstrengader naar de moeder.", False,
      "Niet waar. Afvalstoffen gaan via de twee navelstrengslagaders naar de moeder."),
    W("De navelstreng verbindt de foetus met de placenta.", True,
      "Waar. Via de navelstreng gaan de stoffen heen en weer tussen de placenta en de foetus."),
    I("Eén navelstrengader en twee navelstrengslagaders vormen samen ____ bloedvaten.", "drie|3",
      "Eén navelstrengader en twee navelstrengslagaders: dat zijn drie bloedvaten."),
    I("Het gas dat de foetus kwijt moet, gaat via de slagaders van de navelstreng weg en heet ____.", "koolstofdioxide|CO2|co2",
      "Koolstofdioxide is een afvalstof die via de navelstrengslagaders naar de moeder gaat."),
    I("In de placenta vindt de ____ van stoffen plaats tussen het bloed van moeder en kind.", "uitwisseling",
      "In de placenta worden stoffen tussen moeder en kind uitgewisseld."),
    I("Drinken van alcohol in de zwangerschap kan leiden tot Foetaal Alcohol ____.", "syndroom|Syndroom",
      "Foetaal Alcohol Syndroom (FAS): de hersenen groeien niet goed."),
    O("Leg in één zin uit hoe alcohol dat een zwangere vrouw drinkt bij haar kindje komt.", ["placenta", "bloed"], 2,
      "De alcohol komt in het bloed van de moeder en gaat via de placenta naar het bloed van het kindje.",
      "Alcohol, drugs en nicotine kunnen via de placenta bij het embryo komen."),
    O("Leg in één zin uit waarom het bloed in de navelstrengader meer zuurstof bevat dan het bloed in de slagaders.", ["moeder", "placenta"], 2,
      "De ader brengt bloed van de placenta naar het kindje, waar de zuurstof uit het bloed van de moeder is opgenomen.",
      "De navelstrengader vervoert zuurstof van de moeder naar het kindje; de slagaders voeren afvalstoffen af.")
]),
72: ("Embryo, foetus en bevalling", "🍼", [
    M("Hoe heet de eerste periode van twaalf weken na de innesteling?",
      "De embryonale fase",
      ["De fase van de nageboorte", "De foetusfase", "De indalingsfase van de weeën"],
      "In de eerste twaalf weken ontstaan alle organen; dit is de embryonale fase."),
    M("Vanaf wanneer noem je het ongeboren kind een foetus?",
      "Als alle organen zijn aangelegd en het kind alleen nog groeit",
      ["Zodra de eicel is bevrucht", "Zodra het kindje begint te bewegen in de buik", "Pas vanaf het moment van de geboorte"],
      "Aan het einde van de embryonale fase groeit het kindje alleen nog en heet het een foetus."),
    M("Een vrouw is tien weken zwanger. Wat merkt ze waarschijnlijk wél?",
      "Ze voelt zich moe en misselijk",
      ["Haar buik is duidelijk dikker geworden", "Ze voelt het kindje bewegen", "Haar kindje is al klaar voor de geboorte"],
      "In de eerste twaalf weken is aan de buik niet veel te zien; moe en misselijk zijn komt wel voor."),
    M("Na de geboorte van de baby duwen weeën nog iets naar buiten. Wat is dat?",
      "De placenta met vruchtvliezen en resten navelstreng",
      ["Het vruchtwater en de baarmoedermond", "De navelstreng en de baby", "De baarmoederspieren en de vagina"],
      "Dat is de nageboorte: de placenta met vruchtvliezen en resten navelstreng komen naar buiten."),
    M("Wat gebeurt er in het lichaam van de vrouw als ze een wee voelt?",
      "De spieren van de baarmoeder trekken samen",
      ["De baarmoedermond sluit zich weer", "De vruchtvliezen worden dikker", "De navelstreng wordt afgeknepen"],
      "Een wee is het samentrekken van de spieren van de baarmoeder."),
    M("Welke volgorde van de bevalling klopt?",
      "Ontsluiting, uitdrijving, nageboorte",
      ["Uitdrijving, ontsluiting, nageboorte", "Ontsluiting, nageboorte, uitdrijving", "Nageboorte, ontsluiting, uitdrijving"],
      "De bevalling gaat in drie fasen: eerst ontsluiting, dan uitdrijving en tot slot de nageboorte."),
    M("Een baby ligt met de billen naar beneden voor de baarmoedermond. Hoe heet dat?",
      "Stuitligging",
      ["Dwarsligging", "Hoofdligging", "Keizersnede"],
      "Bij een stuitligging worden de billen eerst geboren en dan pas het hoofdje."),
    M("Waar wordt de navelstreng doorgeknipt?",
      "Tussen twee klemmetjes in",
      ["Vlak onder de placenta voordat de bevalling begint", "Alleen bij een keizersnede, niet bij andere bevallingen", "Pas als het stompje zelf is afgevallen"],
      "De verloskundige knijpt de navelstreng dicht met twee klemmetjes en knipt hem daartussen door."),
    M("Twee zussen lijken sprekend op elkaar. Waaruit zijn ze ontstaan?",
      "Uit één bevruchte eicel die zich splitste",
      ["Uit twee eicellen die tegelijk vrijkwamen", "Uit twee zaadcellen en één eicel die twee keer werd bevrucht", "Uit één zaadcel die twee eicellen bevruchtte"],
      "Een eeneiige tweeling ontstaat uit één bevruchte eicel; het bolletje cellen splitst zich in tweeën."),
    W("Na het breken van de vruchtvliezen loopt het vruchtwater naar buiten.", True,
      "Waar. Dat gebeurt vlak voor of tijdens de ontsluiting."),
    W("In de eerste twaalf weken van de zwangerschap heet het kindje een foetus.", False,
      "Niet waar. In de eerste twaalf weken is het een embryo; daarna heet het een foetus."),
    W("Aan de buik van een vrouw die zes weken zwanger is, zie je al duidelijk dat ze zwanger is.", False,
      "Niet waar. In de eerste twaalf weken is aan de buik niet veel te zien; pas na ongeveer twintig weken wordt hij dikker."),
    W("Bij een twee-eiige tweeling heeft ieder kindje een eigen placenta.", True,
      "Waar. Bij een twee-eiige tweeling zijn er altijd twee placenta's."),
    W("Bij een dwarsligging wordt de baby gewoon via de vagina geboren.", False,
      "Niet waar. Bij een dwarsligging kan dat niet; de arts besluit dan tot een keizersnede."),
    I("Het litteken dat overblijft als het stompje van de navelstreng is afgevallen, is de ____.", "navel",
      "Het stompje valt na een paar dagen af; het litteken is de navel."),
    I("De sterke weeën die de baby tijdens de uitdrijving naar buiten duwen, heten ____weeën.", "pers",
      "Tijdens de uitdrijving duwen sterke persweeën de baby door de vagina naar buiten."),
    I("Zes weken voor de bevalling beginnen de ____weeën, waardoor het kindje met het hoofdje naar beneden komt te liggen.", "indalings|indaling",
      "Indalingsweeën zorgen voor de indaling van het kindje."),
    I("Een eeneiige tweeling is altijd van hetzelfde ____.", "geslacht",
      "Een eeneiige tweeling komt uit één eicel en is dus altijd van hetzelfde geslacht."),
    O("Wat gebeurt er in de fase van de nageboorte? Leg het in één zin uit.", ["placenta", "weeën/wee"], 2,
      "Een of meer weeën duwen de placenta met vruchtvliezen en resten van de navelstreng naar buiten.",
      "Na de geboorte van de baby duwen weeën de placenta naar buiten."),
    O("Leg in één zin uit hoe een eeneiige tweeling ontstaat.", ["eicel", "splits"], 2,
      "Een bevruchte eicel splitst zich tijdens de eerste delingen in twee bolletjes cellen, die allebei uitgroeien tot een baby.",
      "Eén bevruchte eicel splitst zich en uit elk deel groeit een kindje.")
]),
73: ("Chromosomen, geslacht en genen", "🧬", [
    M("Een onderzoeker telt de chromosomen in een huidcel van een mens. Wat telt ze?",
      "46 chromosomen, dus 23 paren",
      ["23 chromosomen, dus 23 paren", "46 chromosomen, dus 46 paren", "23 chromosomen, dus 12 paren"],
      "Een lichaamscel heeft 23 chromosomenparen, samen 46 chromosomen."),
    M("Hoeveel chromosomen heeft een zaadcel vergeleken met een gewone lichaamscel?",
      "De helft",
      ["Evenveel", "Twee keer zoveel", "Een kwart"],
      "Van elk paar komt één chromosoom in de zaadcel of eicel terecht: 23 in plaats van 46."),
    M("Welk geslachtschromosoom geeft een eicel altijd door aan het kind?",
      "Een X-chromosoom",
      ["Een Y-chromosoom", "Een X- of een Y-chromosoom, willekeurig", "Geen van beide"],
      "Een eicel geeft altijd een X-chromosoom door; een zaadcel geeft een X of een Y."),
    M("Een zaadcel met een Y-chromosoom bevrucht een eicel. Welk geslacht krijgt het kindje?",
      "Een jongen, want het kindje krijgt een X en een Y",
      ["Een meisje, want de eicel geeft altijd een Y door", "Een meisje, want het kindje krijgt twee Y-chromosomen", "Een jongen, want de eicel bepaalt het geslacht"],
      "De zaadcel geeft een X of een Y door; de zaadcel bepaalt dus het geslacht."),
    M("Welke omschrijving past bij een gen?",
      "Een stukje DNA met de code voor één eiwit",
      ["Een heel chromosoom met alle eigenschappen", "Een eiwit dat de eigenschap bepaalt", "Een andere naam voor een variant van een eigenschap"],
      "Een gen is de DNA-code voor één eiwit; eiwitten bepalen je eigenschappen."),
    M("Het gen voor de vorm van je oorlel heeft verschillende varianten. Hoe heten die varianten?",
      "Allelen",
      ["Genomen", "Chromosomen", "Geslachtschromosomen"],
      "Een variant van een gen heet een allel."),
    M("Hoeveel allelen heb je voor één gen en van wie komen ze?",
      "Twee: één van je vader en één van je moeder",
      ["Eén: van de ouder met de sterkste eigenschap", "Twee: allebei van je moeder via de eicel", "Vier: twee van elke ouder"],
      "Chromosomen komen in paren voor, dus heb je twee allelen: één van elke ouder."),
    M("Hoe is de lange draad in een chromosoom opgebouwd?",
      "Als een wenteltrap, waarvan elke trede uit twee onderdelen bestaat",
      ["Als een rechte draad zonder treden", "Als een bol van eiwitten", "Als een wenteltrap met treden van één onderdeel"],
      "Het molecuul lijkt op een wenteltrap; elke trede is opgebouwd uit twee stoffen."),
    M("Hoe zorgen genen voor een eigenschap zoals oogkleur?",
      "Het gen maakt volgens zijn code een eiwit, en eiwitten bepalen de eigenschap",
      ["Elk gen is zelf de eigenschap die je ziet", "Het gen bepaalt de eigenschap en eiwitten doen niets", "De eiwitten maken de genen aan"],
      "De volgorde van de onderdelen in het DNA is de code voor een eiwit; eiwitten regelen wat er in de cel gebeurt."),
    W("Een zaadcel bevat evenveel chromosomen als een bevruchte eicel.", False,
      "Niet waar. Een zaadcel heeft de helft, 23 chromosomen; de bevruchte eicel heeft er 46."),
    W("Een zaadcel kan een X- of een Y-chromosoom doorgeven.", True,
      "Waar. Daarom bepaalt de zaadcel of het kindje een jongen of meisje wordt."),
    W("Een allel is een variant van een gen.", True,
      "Waar. Bijvoorbeeld het gen voor oogkleur heeft de varianten blauw en bruin."),
    W("Een jongen heeft twee X-chromosomen als geslachtschromosomen.", False,
      "Niet waar. Een jongen heeft een X en een Y; een meisje heeft twee X-chromosomen."),
    W("Broers en zussen hebben precies dezelfde sets chromosomen van hun ouders gekregen.", False,
      "Niet waar. Ze krijgen niet precies dezelfde sets van 23 chromosomen en lijken daarom niet precies op elkaar."),
    I("De verzameling van alle chromosomen in een cel heet het ____.", "genoom",
      "Alle chromosomen samen noem je het genoom."),
    I("Het 23ste chromosomenpaar bestaat uit de ____chromosomen.", "geslachts",
      "Het 23ste paar zijn de geslachtschromosomen: XX of XY."),
    I("Weinig P-eiwit betekent weinig pigment, en daardoor zijn de ogen ____.", "blauw",
      "Bij weinig pigment kleuren de ogen blauw, bij veel pigment bruin."),
    I("Chromosomen zitten in de ____ van de cel.", "kern|celkern",
      "In de kernen van al je cellen zitten de chromosomen."),
    O("Leg in één zin uit waarom een kind op zijn ouders lijkt.", ["helft", "zaadcel/eicel"], 2,
      "Het kind krijgt de helft van zijn chromosomen van de moeder via de eicel en de helft van de vader via de zaadcel.",
      "Elke ouder geeft de helft van zijn chromosomen door via een eicel of zaadcel."),
    O("Leg in één zin uit waarom het geslacht van een kind van de vader afhangt.", ["zaadcel", "Y-chromosoom/Y"], 2,
      "De eicel geeft altijd een X door, maar de zaadcel geeft een X of een Y-chromosoom door.",
      "De zaadcel bepaalt of het kind een X of een Y-chromosoom van de vader krijgt.")
]),
74: ("Genotype, fenotype en aandoeningen", "🔬", [
    M("Marie heeft genen voor een grote lengte, maar eet te weinig en blijft kleiner. Wat bepaalt haar fenotype voor lengte?",
      "Haar genotype én de omgeving",
      ["Alleen haar genotype", "Alleen de omgeving", "Alleen de genen van één ouder"],
      "Het fenotype is soms het resultaat van genotype (aanleg) en omgeving."),
    M("Welke eigenschap is niet erfelijk?",
      "Een litteken na een val",
      ["De kleur van je ogen", "De vorm van je oorlel", "Kleurenblindheid"],
      "Veranderingen door een ongeluk, zoals een litteken, zijn niet erfelijk."),
    M("Wat valt onder het genotype van een persoon?",
      "Alle informatie op zijn genen",
      ["Alles wat je aan zijn lichaam ziet", "Alleen de genen voor oogkleur", "Zijn kleding en zijn kapsel"],
      "De informatie op al je genen samen heet het genotype."),
    M("Waarom lijken broers en zussen niet precies op elkaar?",
      "Ze krijgen niet precies dezelfde combinatie van chromosomen",
      ["Ze hebben verschillende ouders", "Ze krijgen allebei alle chromosomen van de vader", "Hun genen veranderen door wat ze leren"],
      "Elk kind krijgt van beide ouders de helft van de chromosomen, maar niet dezelfde sets."),
    M("Waardoor ontstaat het syndroom van Down?",
      "Door een extra chromosoom, waardoor cellen er 47 hebben",
      ["Door een ontbrekend chromosoom, waardoor cellen er 45 hebben", "Door het rodehondvirus tijdens de zwangerschap", "Door een litteken in het DNA"],
      "Kinderen met Down hebben 47 in plaats van 46 chromosomen."),
    M("Hoe verandert de kans op een kind met het Downsyndroom naarmate een vrouw ouder wordt?",
      "De kans wordt groter",
      ["De kans wordt kleiner", "De kans blijft altijd gelijk", "De kans hangt alleen van de leeftijd van de vader af"],
      "Als een vrouw ouder wordt, heeft ze een grotere kans op een kind met het Downsyndroom."),
    M("Bij welk onderzoek zuigt de arts cellen van de foetus op uit de placenta?",
      "Bij een vlokkentest",
      ["Bij een bloedonderzoek van de zwangere vrouw", "Bij een echo met de echoscoop", "Bij een keizersnede"],
      "Bij een vlokkentest zuigt de arts cellen uit de placenta op; die cellen zijn van de foetus."),
    M("Wat onderzoekt de arts bij allebei de vormen van onderzoek vóór de geboorte?",
      "Cellen van de foetus, op fouten in de chromosomen",
      ["Het bloed van de zwangere vrouw, op ziekteverwekkers", "De placenta, op hoe groot die al is", "De baarmoedermond, op hoe ver die open is"],
      "Bij een vruchtwaterpunctie en bij een vlokkentest worden cellen van de foetus onderzocht op fouten in de chromosomen."),
    M("Wat betekent het woord prenataal in prenataal onderzoek?",
      "Vóór de geboorte",
      ["Na de geboorte", "Tijdens de uitdrijving", "Door de vrouw zelf uitgevoerd"],
      "Prenataal betekent vóór de geboorte; een arts zoekt zo naar aandoeningen als het Downsyndroom."),
    W("Een kind met het Downsyndroom heeft in zijn cellen minder chromosomen dan andere kinderen.", False,
      "Niet waar. Het heeft 47 in plaats van 46 chromosomen: één te veel."),
    W("Kleurenblindheid is een erfelijke aandoening.", True,
      "Waar. Je erft kleurenblindheid van je ouders."),
    W("Wat je leert, zoals fietsen, is een erfelijke eigenschap.", False,
      "Niet waar. Leren hangt af van de omgeving; erfelijk is alleen wat in je genen zit."),
    W("Het fenotype is wat je ziet van een eigenschap, bijvoorbeeld blauwe ogen.", True,
      "Waar. Dat wat je ziet van een eigenschap heet het fenotype."),
    W("Een kind met het Downsyndroom is ontstaan uit een eicel met een chromosoom te veel.", True,
      "Waar. De eicel had 24 in plaats van 23 chromosomen, daardoor hebben de cellen van het kind er 47."),
    I("Een erfelijke ____ voor muziek betekent dat je er goed in kunt worden als je veel oefent.", "aanleg",
      "De aanleg is erfelijk, maar om echt goed te worden moet je oefenen."),
    I("Met een naald zuigt de arts bij een punctie een beetje ____ uit de baarmoeder; daarin zitten cellen van het ongeboren kind.", "vruchtwater",
      "In het vruchtwater zitten cellen van de foetus die de arts onderzoekt."),
    I("Kleurenblindheid is het gevolg van een fout in de ____ van één chromosoom.", "structuur",
      "Kleurenblindheid is een fout in de structuur van één chromosoom, en je erft het van je ouders."),
    I("Het Downsyndroom komt vaker voor bij kinderen van oudere ____.", "moeders|moeder|vrouwen",
      "Als een vrouw ouder wordt, wordt de kans op een kind met Down groter."),
    O("Twee eeneiige tweelingbroers groeiden gescheiden op en verschillen in gedrag. Leg in één zin uit waardoor dat komt.", ["omgeving", "genen/genotype"], 2,
      "Hun genen zijn gelijk, dus de verschillen komen door de omgeving waarin ze zijn opgegroeid.",
      "Bij gelijke genen komen verschillen door de omgeving."),
    O("Noem één onderzoek vóór de geboorte en leg in één zin uit wat de arts daarbij doet.", ["vruchtwater/vlok/placenta", "naald/cellen"], 2,
      "Bij een vruchtwaterpunctie zuigt de arts met een naald vruchtwater met cellen van de foetus uit de baarmoeder.",
      "Bij een vlokkentest zuigt de arts cellen uit de placenta op, bij een punctie neemt hij vruchtwater met een naald.")
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_extra3_seed_71')
    for nr, (sub, icoon, vr) in EXAMENS.items():
        par = '11.3' if nr <= 72 else '11.4'
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        kort = sum(all(len(o) > len(v['opties'][v['antwoord']]) for i, o in enumerate(v['opties']) if i != v['antwoord']) for v in vr if v['type'] == 'mc')
        assert kort / tot <= 0.4, f"examen_{nr}: juiste optie {kort}/{tot} keer kortste"
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {
            "id": f"ex-h3-biologie-{nr}",
            "hoofdstuk": 11,
            "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
            "paragraaf": par,
            "titel": f"Toets {nr} — §{par} {sub}",
            "vak": f"Biologie · HAVO 3 (H{par})",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie H{par}) — gegenereerd door tools/gen_biologie_h11_extra3_34.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
