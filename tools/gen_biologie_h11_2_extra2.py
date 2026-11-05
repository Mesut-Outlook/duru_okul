#!/usr/bin/env python3
"""Biologie HAVO 3 · Hoofdstuk 11 Voortplanting · §11.2 Bevruchting (extra toetsen 52–56).
Schrijft havo3/biologie/js/data/examen_52..56.js (ex-h3-biologie-52..56).
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
52: ("Van zaadlozing tot innesteling lezen (bron 2 en 3)", "🔬", [
    M("Waar komen de zaadcellen volgens bron 2 eerst terecht na een zaadlozing?",
      "In de vagina, vlak bij de baarmoedermond",
      ["In de baarmoeder, vlak bij de eileiders",
       "In de eileiders, vlak bij de eierstokken",
       "In de urinebuis, vlak bij de baarmoedermond"],
      "Het sperma komt in de vagina, vlak bij de baarmoedermond. Van daaruit zwemmen de zaadcellen verder."),
    M("Welk deel van het lichaam van de vrouw passeren zaadcellen tussen de vagina en de eileider?",
      "De baarmoeder",
      ["De eierstok", "De blaas", "De zaadleider"],
      "De zaadcellen zwemmen via de baarmoeder de eileiders binnen."),
    M("Welke gebeurtenis gaat vooraf aan het ondoordringbaar worden van de buitenste laag van de eicel?",
      "De kop van een zaadcel dringt de eicel binnen",
      ["De eerste celdeling van de bevruchte eicel",
       "De innesteling in het baarmoederslijmvlies",
       "De afgifte van HCG door de vlokken"],
      "Pas nadat een zaadcel de eicel is binnengedrongen, wordt de buitenste laag ondoordringbaar."),
    M("Wat klopt volgens bron 2 over de grootte van de geslachtscellen?",
      "De eicel is veel groter dan een zaadcel",
      ["De zaadcel is veel groter dan de eicel",
       "Eicel en zaadcel zijn bijna even groot",
       "De eicel is net iets kleiner dan een zaadcel"],
      "In bron 2 is de eicel veel groter dan de zaadcellen."),
    M("Een bevruchte eicel deelt zich telkens opnieuw, waarbij elke cel zich splitst in twee. Hoeveel cellen zijn er na de derde deling?",
      "8 cellen",
      ["6 cellen", "9 cellen", "12 cellen"],
      "1 cel wordt 2, dan 4, dan 8 cellen: de aantallen verdubbelen bij elke deling."),
    M("Wanneer begint de bevruchte eicel volgens bron 3 voor het eerst te delen?",
      "Na enige uren",
      ["Pas na ongeveer zes dagen",
       "Pas na de innesteling",
       "Nog voor de bevruchting"],
      "Volgens bron 3 deelt het bolletje cellen zich al na enige uren, lang voor de innesteling na ongeveer zes dagen."),
    M("Hoeveel kernen zijn er vlak voor en vlak na de bevruchting, als je zaadcel en eicel samen telt?",
      "Twee kernen, daarna één kern",
      ["Eén kern, daarna twee kernen",
       "Twee kernen, daarna twee kernen",
       "Eén kern, daarna één kern"],
      "Zaadcel en eicel hebben elk een kern. Die versmelten tot één nieuwe kern."),
    M("Op welke twee plekken vinden bevruchting en innesteling plaats, in die volgorde?",
      "In de eileider, in het baarmoederslijmvlies",
      ["In de baarmoeder, in de eileider",
       "In de vagina, in de baarmoeder",
       "In de eierstok, in de eileider"],
      "De bevruchting vindt plaats in de eileider; de innesteling in het baarmoederslijmvlies."),
    M("Een zaadlozing heeft plaatsgevonden, maar de vrouw wordt niet zwanger. Welke verklaring past bij het boek?",
      "Er was geen rijpe eicel in de eileider toen de zaadcellen er aankwamen",
      ["De zaadcellen konden niet uit de vagina omdat het maar 3 mL sperma was",
       "De zaadcellen leven in de eileider maar een paar minuten",
       "De kern van de eicel kan nooit met een zaadcelkern versmelten"],
      "Bevruchting kan alleen als de zaadcellen in de eileider een rijpe eicel tegenkomen, bijvoorbeeld na een eisprong."),
    W("Zaadcellen zwemmen via de baarmoeder naar de eileiders.", True,
      "Waar. Vanuit de vagina zwemmen ze door de baarmoeder de eileiders binnen."),
    W("Bij een zaadlozing worden de zaadcellen rechtstreeks in de eileider afgegeven.", False,
      "Niet waar. Het sperma komt in de vagina, vlak bij de baarmoedermond; de zaadcellen zwemmen daarna zelf verder."),
    W("Na de bevruchting is er één nieuwe kern in de cel.", True,
      "Waar. De kernen van zaadcel en eicel versmelten tot één nieuwe kern."),
    W("Een vrouw is al zwanger op het moment dat de zaadcel de eicel bevrucht.", False,
      "Niet waar. Een vrouw is pas zwanger vanaf de innesteling, ongeveer zes dagen na de bevruchting."),
    W("Het bolletje cellen zet zich ongeveer zes uur na de bevruchting vast in het baarmoederslijmvlies.", False,
      "Niet waar. De innesteling vindt na ongeveer zes dagen plaats, niet na zes uur."),
    I("De zaadcellen kunnen in de eileider enkele ____ overleven.", "dagen", "Zaadcellen kunnen in de eileider enkele dagen overleven."),
    I("Bij een zaadlozing komt er ongeveer 3 ____ sperma in de vagina.", "mL|ml|milliliter", "Het gaat om ongeveer 3 mL sperma."),
    I("Het bolletje van delende cellen gaat na de bevruchting naar de ____.", "baarmoeder|de baarmoeder", "Het bolletje cellen gaat naar de baarmoeder."),
    I("Een bevruchte eicel die zich in twee cellen heeft gedeeld, deelt zich daarna tot ____ cellen.", "4|vier",
      "Twee cellen worden vier cellen, enzovoort."),
    O("Vergelijk bevruchting en innesteling: wat gebeurt er bij elk van de twee?", ["versmelt/versmelten/samensmelt", "vast/vastzetten/vastzit/nestelt"], 2,
      "Bij de bevruchting versmelten de kernen van zaadcel en eicel; bij de innesteling zet het bolletje cellen zich vast in het baarmoederslijmvlies.",
      "Bevruchting is het samensmelten van twee kernen; innesteling is het vastzetten van het bolletje cellen in de baarmoederwand."),
    O("Beschrijf wat er gebeurt vanaf het moment dat een zaadcel een rijpe eicel heeft bereikt, tot de eicel niet meer door andere zaadcellen bevrucht kan worden.", ["kop/binnen", "versmelt/kern", "ondoordringbaar/dicht"], 2,
      "De kop van de zaadcel dringt de eicel binnen, de kernen versmelten en de buitenste laag van de eicel wordt ondoordringbaar.",
      "De kop dringt binnen, daarna versmelten de kernen en wordt de buitenste laag van de eicel ondoordringbaar voor andere zaadcellen.")
]),

53: ("Voorbehoedmiddelen vergelijken en kiezen", "🛡️", [
    M("Waar kun je naast bron 6 ook terugvinden wat je moet doen als je een pil bent vergeten?",
      "In de bijsluiter van de pil",
      ["Op de verpakking van het condoom",
       "Op de achterkant van de pleister",
       "In het boekje van het spiraaltje"],
      "De informatie over een vergeten pil staat ook in de bijsluiter van de pil."),
    M("Een vrouw is meer dan één pil vergeten. Wat adviseert bron 6?",
      "Contact opnemen met haar arts",
      ["Alle vergeten pillen tegelijk innemen",
       "Gewoon doorgaan met de strip",
       "Stoppen en nooit meer de pil slikken"],
      "Bij meer dan één vergeten tablet staat in bron 6: neem contact op met uw arts."),
    M("Welk van deze voorbehoedmiddelen bevat nooit hormonen?",
      "Het condoom",
      ["De pleister", "Het staafje", "De pil"],
      "Een condoom is een barrière en bevat geen hormonen; pil, pleister en staafje geven hormonen af."),
    M("Welke twee middelen houden allebei de eisprong tegen met hormonen?",
      "De pil en het hormoonstaafje",
      ["Het condoom en het spiraaltje",
       "Sterilisatie en het condoom",
       "Het spiraaltje en sterilisatie"],
      "Pil en hormoonstaafje geven hormonen af die de eisprong voorkomen."),
    M("Waar zitten het spiraaltje en het hormoonstaafje, in deze volgorde?",
      "In de baarmoeder en onder de huid",
      ["Onder de huid en in de baarmoeder",
       "In de eileider en in de baarmoeder",
       "Op de huid en in de eierstok"],
      "Een arts plaatst het spiraaltje in de baarmoeder; het staafje wordt onder de huid geplaatst."),
    M("Wat hebben sterilisatie bij de vrouw en het condoom met elkaar gemeen?",
      "Bij beide komen zaadcellen niet bij de eicel",
      ["Beide beschermen ook tegen soa's",
       "Beide onderdrukken de ovulatie",
       "Beide geven hormonen af"],
      "Het condoom houdt zaadcellen tegen; bij een vrouw met doorgesneden eileiders kunnen zaadcellen niet bij de eicel komen."),
    M("Een nieuw middel voorkomt zwangerschap en is makkelijk te gebruiken, maar schaadt de gezondheid. Waarom is het geen goed voorbehoedmiddel?",
      "Het voldoet niet aan de eis dat het niet schadelijk is",
      ["Het voldoet niet aan de eis dat het zwangerschap voorkomt",
       "Het voldoet niet aan de eis dat het makkelijk in gebruik is",
       "Het voldoet niet aan de eis dat een arts het plaatst"],
      "Een goed voorbehoedmiddel voldoet aan drie eisen, waaronder dat het niet schadelijk is voor je gezondheid."),
    M("Welke methode vraagt van een stel dat zij in de vruchtbare periode geen geslachtsgemeenschap hebben?",
      "Periodieke onthouding",
      ["Coïtus interruptus",
       "Sterilisatie",
       "De morning-afterpil"],
      "Bij periodieke onthouding heeft het stel geen seks tijdens de vruchtbare periode van de vrouw."),
    M("Een vrouw slikt de pil. Waarom kiest haar partner toch voor een condoom erbij?",
      "Alleen het condoom beschermt tegen soa's",
      ["De pil werkt alleen op de oneven dagen",
       "Het condoom maakt de pil sterker",
       "De pil laat de zaadcellen sneller zwemmen"],
      "Het condoom is het enige voorbehoedmiddel dat ook beschermt tegen soa's."),
    W("Zowel een man als een vrouw kan zich laten steriliseren.", True,
      "Waar. Bij de man worden de zaadleiders doorgesneden, bij de vrouw de eileiders."),
    W("Een spiraaltje brengt de vrouw zelf in bij de baarmoedermond.", False,
      "Niet waar. Een arts plaatst het spiraaltje in de baarmoeder."),
    W("Na sterilisatie van de vrouw komen er geen eicellen meer vrij uit de eierstok.", False,
      "Niet waar. De eileiders zijn doorgesneden, zodat zaadcellen niet meer bij de eicel kunnen komen; de eicel kan nog wel vrijkomen."),
    W("De hormonen uit de anticonceptiepleister houden de eisprong tegen.", True,
      "Waar. De pleister geeft via de huid hormonen af die de eisprong tegenhouden."),
    W("Een vrouw die meer dan één pil is vergeten, mag gewoon doorgaan met haar strip.", False,
      "Niet waar. Bron 6 adviseert in dat geval contact op te nemen met de arts."),
    I("Een gesteriliseerde man of vrouw kan niet meer zwanger worden: sterilisatie is ____.", "definitief",
      "Sterilisatie is definitief."),
    I("Bij sterilisatie worden de zaadleiders of eileiders ____.", "doorgesneden|doorsneden|doorgeknipt", "Sterilisatie is het doorsnijden van de zaadleiders of eileiders."),
    I("De pil bevat de hormonen oestrogeen en ____.", "progesteron", "De pil bevat oestrogeen en progesteron."),
    I("De pil maakt het slijm bij de baarmoedermond ____, zodat zaadcellen moeilijker de baarmoeder in komen.", "dikker", "Dikker slijm houdt zaadcellen tegen."),
    O("Vergelijk de pil en het condoom: wat voorkomt elk van de twee?", ["eisprong/ovulatie/rijpen", "zaadcellen/zaadcel"], 2,
      "De pil voorkomt de eisprong; het condoom voorkomt dat zaadcellen bij de eicel komen.",
      "De pil houdt de eisprong tegen; het condoom houdt de zaadcellen tegen."),
    O("Een stel wil zeker geen kinderen meer. Noem een voorbehoedmiddel dat daarbij past en geef een reden.", ["sterilisatie/steriliseren", "definitief/blijvend/permanent"], 2,
      "Sterilisatie, want dat is definitief.",
      "Sterilisatie, omdat dit een definitieve oplossing is.")
]),

54: ("Embryo, vlokken en placenta (bron 8)", "👶", [
    M("Waar ligt de kiemschijf volgens bron 8?",
      "Binnenin het bolletje cellen",
      ["Aan de buitenkant van het bolletje cellen",
       "Op de steel naar de moeder",
       "In de wand van de eileider"],
      "De kiemschijf is een groepje cellen binnenin het bolletje cellen."),
    M("In welk weefsel groeien de vlokken tijdens de innesteling?",
      "In het baarmoederslijmvlies",
      ["In de wand van de eileider",
       "In de buitenste laag van de eicel",
       "In het vlies om de eierstok"],
      "De vlokken groeien tijdens de innesteling het baarmoederslijmvlies binnen."),
    M("Wat zit er in de placenta?",
      "Bloedvaten van het kindje en van de moeder",
      ["Alleen bloedvaten van de moeder",
       "Alleen bloedvaten van het kindje",
       "Zaadcellen en eicellen"],
      "In de placenta zitten bloedvaten van het kindje en van de moeder; daar worden stoffen uitgewisseld."),
    M("Welke stoffen geven de vlokken terug aan het bloed van de moeder?",
      "Afvalstoffen",
      ["Voedingsstoffen", "Warmte", "Hormonen van de moeder"],
      "De vlokken nemen voedingsstoffen en zuurstof op en geven afvalstoffen terug."),
    M("Welke volgorde van de ontwikkeling in bron 8 klopt?",
      "Holte met kiemschijf, vlokken in het slijmvlies, steel",
      ["Steel, holte met kiemschijf, vlokken in het slijmvlies",
       "Vlokken in het slijmvlies, steel, holte met kiemschijf",
       "Steel, vlokken in het slijmvlies, holte met kiemschijf"],
      "Eerst ontstaat de holte met kiemschijf, daarna groeien de vlokken in het slijmvlies en tussen vlokken en kiemschijf ontstaat al snel een steel."),
    M("Welke twee dingen blijven bij een zwangere vrouw achterwege dankzij HCG?",
      "De rijping van een nieuwe eicel en het afstoten van het slijmvlies",
      ["De vorming van de placenta en van de kiemschijf",
       "De werking van de eileiders en van de zaadleiders",
       "De innesteling en de vorming van de vlokken"],
      "HCG voorkomt dat een nieuwe eicel gaat rijpen en dat het baarmoederslijmvlies wordt afgestoten."),
    M("Een zwangerschapstest toont HCG aan. Welke gebeurtenis heeft dan al plaatsgevonden?",
      "De innesteling, want de vlokken maken HCG",
      ["Een tweede eisprong na de bevruchting",
       "Het afstoten van het baarmoederslijmvlies",
       "De ontwikkeling van een volledige placenta"],
      "De vlokken maken HCG; die groeien tijdens de innesteling in het baarmoederslijmvlies."),
    M("In welke paragraaf van het boek wordt de placenta verder behandeld?",
      "Paragraaf 11.3",
      ["Paragraaf 10.4", "Paragraaf 11.1", "Paragraaf 11.4"],
      "Het boek verwijst voor de placenta naar paragraaf 11.3."),
    M("Welke cellen van het bolletje vormen de vlokken?",
      "De buitenste cellen",
      ["De cellen van de kiemschijf",
       "De cellen van de steel",
       "De cellen in de holte"],
      "De buitenste cellen vormen uitstulpingen, de vlokken."),
    W("De vlokken groeien tijdens de innesteling het baarmoederslijmvlies binnen.", True,
      "Waar. Daar nemen ze voedingsstoffen en zuurstof op."),
    W("De kiemschijf vormt de buitenste cellen die het baarmoederslijmvlies binnengroeien.", False,
      "Niet waar. De buitenste cellen vormen de vlokken; de kiemschijf ligt binnenin en wordt het embryo."),
    W("Het embryo ontstaat uit de kiemschijf, die binnenin het bolletje cellen ligt.", True,
      "Waar. Uit de kiemschijf ontstaat het embryo."),
    W("HCG zorgt ervoor dat er elke maand een nieuwe eicel rijpt.", False,
      "Niet waar. HCG voorkomt juist dat er een nieuwe eicel gaat rijpen."),
    W("De vlokken geven voedingsstoffen af aan het bloed van de moeder en nemen daaruit afvalstoffen op.", False,
      "Niet waar. Het is omgekeerd: de vlokken nemen voedingsstoffen en zuurstof op en geven afvalstoffen terug."),
    I("Het zwangerschapshormoon HCG zorgt ervoor dat er geen ____ meer komt.", "menstruatie|de menstruatie", "HCG voorkomt dat het slijmvlies wordt afgestoten: er komt geen menstruatie meer."),
    I("Een zwangerschapstest kun je bij de apotheek, de drogist of via ____ kopen.", "internet", "Je kunt een zwangerschapstest ook via internet kopen."),
    I("Een zwangerschapstest toont aan of het hormoon HCG in de ____ aanwezig is.", "urine", "De test toont HCG aan in de urine."),
    I("De vlokken nemen voedingsstoffen en ____ op uit de bloedvaten van de moeder.", "zuurstof", "De vlokken nemen voedingsstoffen en zuurstof op en geven afvalstoffen terug."),
    O("Beschrijf hoe het bolletje cellen zich na de innesteling verder ontwikkelt: welke delen ontstaan er en wat doen ze?", ["kiemschijf", "vlokken/uitstulping/uitstulpingen", "steel/navelstreng"], 2,
      "In het bolletje ontstaat een holte met een kiemschijf waaruit het embryo ontstaat; de buitenste cellen vormen vlokken die voedingsstoffen opnemen, en er ontstaat een steel.",
      "Uit de kiemschijf ontstaat het embryo, de vlokken nemen stoffen op uit het bloed van de moeder en de steel wordt de navelstreng."),
    O("Waarom bevat de placenta bloedvaten van zowel de moeder als het kindje?", ["uitgewisseld/uitwisseling/uitwisselen/uitwisselt", "stoffen/zuurstof/voedingsstoffen"], 2,
      "Zo kunnen stoffen worden uitgewisseld tussen moeder en kind: voedingsstoffen en zuurstof gaan naar het kindje, afvalstoffen terug.",
      "Omdat daar stoffen worden uitgewisseld tussen het bloed van de moeder en dat van het kind.")
]),

55: ("Ivf toepassen: stappen, kansen en berekenen (bron 10)", "🧪", [
    M("Wat is de juiste volgorde van een ivf-behandeling?",
      "Hormonen geven, eicellen verwijderen, bevruchten in een schaaltje, bolletje terugplaatsen",
      ["Eicellen verwijderen, hormonen geven, bolletje terugplaatsen, bevruchten in een schaaltje",
       "Bevruchten in een schaaltje, hormonen geven, eicellen verwijderen, bolletje terugplaatsen",
       "Hormonen geven, bolletje terugplaatsen, eicellen verwijderen, bevruchten in een schaaltje"],
      "Eerst rijpen eicellen door hormonen, dan worden ze verwijderd, bevrucht en wordt een bolletje cellen teruggeplaatst."),
    M("Welk effect hebben de hormonen die de vrouw vooraf bij ivf krijgt?",
      "Er rijpen meerdere eicellen tegelijk",
      ["Er rijpt geen enkele eicel meer",
       "De eileiders worden opnieuw doorgankelijk",
       "De zaadcellen worden sneller"],
      "Door de hormonen rijpen er meerdere eicellen tegelijk."),
    M("Wanneer brengt de arts de bolletjes cellen terug in de baarmoeder?",
      "Enkele dagen na de bevruchting in het schaaltje",
      ["Meteen nadat de zaadcellen zijn toegevoegd",
       "Pas na negen maanden zwangerschap",
       "Vóórdat de eicellen zijn bevrucht"],
      "Enkele dagen na de bevruchting, als de eicellen zich hebben gedeeld, worden maximaal twee bolletjes cellen teruggeplaatst."),
    M("Ongeveer 1 op de 3 teruggeplaatste bolletjes cellen groeit uit tot een baby. Hoeveel baby's verwacht je ongeveer bij 6 teruggeplaatste bolletjes?",
      "Ongeveer 2 baby's",
      ["Ongeveer 3 baby's", "Ongeveer 4 baby's", "Ongeveer 6 baby's"],
      "6 gedeeld door 3 is 2."),
    M("Wat betekent het woord fertilisatie in in-vitrofertilisatie?",
      "Bevruchting",
      ["Innesteling", "Rijping", "Eisprong"],
      "Fertilisatie is bevruchting; in vitro betekent in glas."),
    M("Wat is niet gegarandeerd nadat de arts bolletjes cellen in de baarmoeder heeft gebracht?",
      "Dat ze zich innestelen",
      ["Dat de arts ze kan plaatsen",
       "Dat ze uit een bevruchte eicel komen",
       "Dat de vrouw een baarmoeder heeft"],
      "De bolletjes cellen kunnen zich gaan innestelen, maar dat gebeurt niet altijd."),
    M("Van wie komen de zaadcellen bij ivf?",
      "Van de man; de arts voegt ze toe aan de eicellen",
      ["Van de vrouw; de arts haalt ze uit haar lichaam",
       "Van een kweekbak in het lab zonder man",
       "Van de arts die de behandeling uitvoert"],
      "De arts doet de zaadcellen van de man bij de rijpe eicellen."),
    M("Waarin verschilt de plaats van de bevruchting bij ivf van een natuurlijke bevruchting?",
      "Bij ivf in een schaaltje, anders in de eileider",
      ["Bij ivf in de baarmoeder, anders in de eileider",
       "Bij ivf in de eileider, anders in de baarmoeder",
       "Bij ivf in de vagina, anders in de eierstok"],
      "Natuurlijk vindt bevruchting in de eileider plaats; bij ivf gebeurt het buiten het lichaam in een schaaltje."),
    M("Wat bevat het schaaltje bij ivf behalve eicellen en zaadcellen?",
      "Voedingsstoffen",
      ["Hormonen van de arts", "Slijmvlies van de moeder", "Het spiraaltje"],
      "De eicellen worden met zaadcellen in een schaaltje met voedingsstoffen gedaan."),
    W("Een ivf-behandeling begint met een hormoonbehandeling van de vrouw.", True,
      "Waar. Eerst krijgt de vrouw een behandeling met hormonen."),
    W("Bij ivf worden de zaadcellen in de eileider van de vrouw gebracht, waar de bevruchting plaatsvindt.", False,
      "Niet waar. De zaadcellen worden bij de eicellen in een schaaltje gedaan."),
    W("Niet elk teruggeplaatst bolletje cellen nestelt zich in.", True,
      "Waar. Dat gebeurt niet altijd."),
    W("Bij ivf mag een arts zoveel bolletjes cellen terugplaatsen als hij wil.", False,
      "Niet waar. De arts brengt maximaal twee bolletjes cellen terug."),
    W("Een bolletje cellen dat bij ivf wordt teruggeplaatst, noemt het boek ook een embryo.", True,
      "Waar. De arts brengt maximaal twee bolletjes cellen (embryo's) in de baarmoeder."),
    I("Bij ivf worden de rijpe eicellen uit de ____ gehaald.", "eierstokken|eierstok|de eierstokken",
      "De arts haalt rijpe cellen uit de eierstokken."),
    I("Een vrouw met verstopte eileiders is ____.", "onvruchtbaar",
      "Zij kan zonder hulp niet zwanger worden."),
    I("De eicellen die bij ivf in het schaaltje bevrucht zijn, gaan zich ____.", "delen|splitsen", "Na de bevruchting gaan de cellen zich delen."),
    I("Bij ivf laat een arts de eicellen ____ het lichaam van de vrouw bevruchten.", "buiten", "De bevruchting vindt buiten het lichaam plaats."),
    O("Leg uit waarom een arts de vrouw bij ivf eerst extra hormonen geeft.", ["meerdere/meer", "tegelijk/rijpen"], 2,
      "Door de hormonen rijpen er meerdere eicellen tegelijk, zodat er meer kans is op een baby.",
      "Er rijpen meerdere eicellen tegelijk, dus meer eicellen om te bevruchten."),
    O("Leg uit waarom ivf geen zekerheid op een kind geeft.", ["innesteling/innestelen/nestelt", "niet altijd/niet elk/niet alle/1 op de 3"], 2,
      "Niet elk bolletje cellen nestelt zich in; ongeveer 1 op de 3 bolletjes groeit uit tot een baby.",
      "Het innestelen gebeurt niet altijd; niet elk bolletje cellen groeit uit tot baby.")
]),

56: ("Noodgevallen en onbetrouwbare methoden: casussen", "🚨", [
    M("Een vrouw had zaterdag om 22.00 uur onbeschermde seks. Wanneer is het laatste moment om binnen 72 uur de morning-afterpil in te nemen?",
      "Maandag om 22.00 uur",
      ["Zondag om 10.00 uur", "Zondag om 22.00 uur", "Dinsdag om 22.00 uur"],
      "72 uur is drie dagen: zaterdag 22.00 uur plus drie dagen is maandag 22.00 uur."),
    M("Een vrouw nam een morning-afterpil, maar blijkt toch zwanger. Wat noemt het boek als mogelijkheid?",
      "Een abortus laten doen in een abortuskliniek",
      ["De morning-afterpil nogmaals innemen",
       "De zwangerschap laten steriliseren",
       "Een spiraaltje laten plaatsen"],
      "Als het voor een morning-afterpil te laat is en de vrouw zwanger is, kan zij in een abortuskliniek een abortus laten doen."),
    M("Een vrouw is 20 weken zwanger. Mag volgens het boek nog een abortus?",
      "Ja, want de grens ligt bij 24 weken",
      ["Ja, want de grens ligt bij 36 weken",
       "Nee, want de grens ligt bij 12 weken",
       "Nee, want een abortus is nooit toegestaan"],
      "Abortus mag alleen als de vrouw niet langer dan 24 weken zwanger is."),
    M("Wat hebben coïtus interruptus en periodieke onthouding volgens het boek gemeen?",
      "Beide zijn erg onbetrouwbaar",
      ["Beide beschermen ook tegen soa's",
       "Beide vragen om een kleine operatie",
       "Beide worden door een arts uitgevoerd"],
      "Het boek noemt beide methoden erg onbetrouwbaar."),
    M("Een man zegt: ik trek mij terug voor ik klaarkom, dus er kunnen geen zaadcellen in de vagina komen. Wat is zijn denkfout?",
      "Vóór de zaadlozing kan er al voorvocht met zaadcellen uitkomen",
      ["Na het terugtrekken blijven zaadcellen in de blaas achter",
       "Voorvocht maakt het slijmvlies van de vrouw dunner",
       "Zaadcellen zitten alleen in het sperma bij de eicel"],
      "Er komt al een beetje vocht uit de penis vóór de zaadlozing en daarin kunnen zaadcellen zitten."),
    M("Welke twee middelen kunnen allebei voorkomen dat een bevruchte eicel zich innestelt?",
      "Het spiraaltje en de morning-afterpil",
      ["De pil en de anticonceptiepleister",
       "Het condoom en sterilisatie",
       "De pleister en het hormoonstaafje"],
      "Het spiraaltje en de morning-afterpil voorkomen de innesteling; pil, pleister en staafje voorkomen de eisprong."),
    M("Zet de maatregelen in volgorde van vroeg naar laat bij het voorkomen van een ongewenste zwangerschap.",
      "Voorbehoedmiddel, morning-afterpil binnen 72 uur, abortus",
      ["Morning-afterpil, voorbehoedmiddel, abortus",
       "Abortus, voorbehoedmiddel, morning-afterpil binnen 72 uur",
       "Voorbehoedmiddel, abortus, morning-afterpil binnen 72 uur"],
      "Eerst probeert een stel zwangerschap met een voorbehoedmiddel te voorkomen, dan kan binnen 72 uur de morning-afterpil, en pas daarna een abortus."),
    M("Een stel wil over een paar jaar nog kinderen. Welk middel past dan niet?",
      "Sterilisatie, omdat dit definitief is",
      ["Het condoom, omdat dit niet schadelijk is",
       "De pil, omdat dit hormonen bevat",
       "Het spiraaltje, omdat een arts het plaatst"],
      "Sterilisatie is definitief; daarom kiezen mensen meestal pas voor sterilisatie als ze geen kinderen meer willen."),
    M("Een vrouw is gesteriliseerd. Waarom kan zij toch nog soa's oplopen?",
      "Sterilisatie beschermt niet tegen soa's",
      ["Soa's gaan alleen via de eileiders",
       "Na sterilisatie werkt het slijmvlies minder",
       "Soa's ontstaan door de hormonen van de pil"],
      "Alleen het condoom beschermt tegen soa's; sterilisatie voorkomt alleen dat zaadcellen bij de eicel komen."),
    W("Voor de morning-afterpil geldt: hoe eerder na de seks, hoe kleiner de kans op zwangerschap.", True,
      "Waar. Hoe eerder de pil wordt genomen, hoe kleiner de kans dat de vrouw zwanger wordt."),
    W("Na het slikken van de morning-afterpil heeft een vrouw nooit last van bijwerkingen.", False,
      "Niet waar. Soms geeft de pil bijwerkingen zoals overgeven en buikpijn."),
    W("Bij periodieke onthouding vindt de eisprong altijd precies op de 14e dag plaats.", False,
      "Niet waar. De eisprong kan ook vroeger of later zijn."),
    W("Voorvocht komt pas na de zaadlozing uit de penis.", False,
      "Niet waar. Het komt al vóór de zaadlozing uit de penis en kan zaadcellen bevatten."),
    W("Voor een abortus krijgt de vrouw in de kliniek eerst een gesprek.", True,
      "Waar. Ze moet er zeker van zijn dat ze de zwangerschap wil beëindigen."),
    I("De morning-afterpil kun je halen bij de drogist of de ____.", "apotheek|de apotheek",
      "De pil is bij de drogist of apotheek te krijgen."),
    I("De morning-afterpil geeft soms bijwerkingen zoals overgeven en ____.", "buikpijn", "Bijwerkingen zijn overgeven en buikpijn."),
    I("De morning-afterpil onderdrukt de ovulatie en voorkomt de ____ van de bevruchte eicel.", "innesteling|de innesteling", "De pil onderdrukt de ovulatie en voorkomt de innesteling."),
    I("Bij een abortus wordt het ____ uit de baarmoeder weggehaald.", "embryo|het embryo", "Bij een abortus haalt de arts het embryo uit de baarmoeder."),
    O("Een vrouw heeft onbeschermde seks gehad. Wat kan zij doen als het nog niet te laat is, en wat als ze toch zwanger blijkt?", ["morning-afterpil/morning after", "abortus"], 2,
      "Zij kan binnen 72 uur een morning-afterpil nemen; is ze toch zwanger, dan kan ze een abortus laten doen.",
      "Eerst een morning-afterpil innemen; als ze toch zwanger is, een abortus."),
    O("Een stel kiest voor periodieke onthouding. Leg uit welk risico zij lopen.", ["eisprong/ovulatie", "onbetrouwbaar/vroeger/later"], 2,
      "Het is moeilijk te bepalen wanneer de eisprong precies is; die kan vroeger of later zijn dan de 14e dag, dus de methode is onbetrouwbaar.",
      "De eisprong is moeilijk te voorspellen, dus de methode is onbetrouwbaar en kan alsnog zwanger maken.")
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_2_extra2_seed_19')
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {
            "id": f"ex-h3-biologie-{nr}",
            "hoofdstuk": 11,
            "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
            "paragraaf": "11.2",
            "titel": f"Toets {nr} — §11.2 {sub}",
            "vak": "Biologie · HAVO 3 (H11.2)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie H11.2) — gegenereerd door tools/gen_biologie_h11_2_extra2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
