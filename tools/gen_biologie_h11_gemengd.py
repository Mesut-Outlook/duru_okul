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


# Elke toets: 4 blokken van 5 vragen (§11.1, §11.2, §11.3, §11.4), in die volgorde.
EXAMENS = {
75: ("A", "🧬", [
    # §11.1
    M("In een bloedonderzoek van een meisje van 14 jaar stijgt het hormoon FSH. Hoe bereikt dit hormoon de eierstok?",
      "De hypofyse geeft het af aan het bloed, dat het naar de eierstok brengt",
      ["Het gaat via de buikholte naar de eierstok", "Zenuwen brengen het rechtstreeks naar de follikel", "De baarmoeder maakt het en geeft het via het slijmvlies door"],
      "De hypofyse geeft FSH en LH af aan het bloed; zo komen ze bij de eierstok en de follikel."),
    W("De lege follikel maakt na de eisprong vooral progesteron.", True,
      "Waar. De lege follikel heet het gele lichaam en maakt vooral progesteron."),
    M("Welke route legt een zaadcel af tot hij het lichaam van de man verlaat?",
      "Zaadbal, bijbal, zaadleider, urinebuis",
      ["Zaadbal, zaadleider, bijbal, urinebuis", "Bijbal, zaadbal, prostaat, zaadleider", "Zaadbal, zaadblaasje, bijbal, urinebuis"],
      "Zaadcellen worden in de zaadbal gemaakt, in de bijbal bewaard en bij de zaadlozing via de zaadleider naar de urinebuis geperst."),
    I("Sperma bestaat uit zaadcellen en het ____ uit de zaadblaasjes en de prostaat.", "zaadvocht",
      "Het mengsel van zaadcellen en zaadvocht heet sperma."),
    M("Een meisje heeft vandaag een ovulatie. Welk deel van haar eierstok barst daarbij open?",
      "De follikel",
      ["Het baarmoederslijmvlies", "De baarmoedermond", "Het gele lichaam"],
      "Bij de eisprong barst de follikel in de eierstok open en komt de rijpe eicel vrij. Wat van de follikel overblijft, wordt het gele lichaam."),
    # §11.2
    W("Het zwangerschapshormoon HCG wordt gemaakt door de hypofyse van de moeder.", False,
      "Niet waar. HCG wordt gemaakt door de vlokken van het embryo."),
    O("Leg in één zin uit waarom een vrouw die zwanger is geworden niet meer ongesteld wordt.", ["HCG", "slijmvlies/afgestoten"], 2,
      "De vlokken van het embryo maken HCG; dat voorkomt dat het baarmoederslijmvlies wordt afgestoten en dat een nieuwe eicel gaat rijpen, dus komt er geen menstruatie.",
      "HCG van het embryo houdt het slijmvlies vast: er is geen afstoting meer, dus geen menstruatie."),
    M("Wat nemen de vlokken van het embryo op uit het bloed van de moeder?",
      "Voedingsstoffen en zuurstof",
      ["Alleen voedingsstoffen, want zuurstof is nog niet nodig", "Alleen zuurstof, want voedsel zit al in de eicel", "Voedingsstoffen en afvalstoffen"],
      "De vlokken nemen voedingsstoffen én zuurstof op en geven afvalstoffen terug aan het bloed van de moeder."),
    I("Bij sterilisatie van een vrouw worden de ____ doorgesneden.", "eileiders|eileider",
      "De eicellen komen nog wel vrij, maar de zaadcellen kunnen er niet meer bij."),
    M("Een man heeft zich laten steriliseren. Wat merkt hij bij een zaadlozing?",
      "Er komt nog sperma naar buiten, maar zonder zaadcellen",
      ["Er komt helemaal geen vocht meer naar buiten", "Er komt alleen nog voorvocht naar buiten", "Er komen wel zaadcellen, maar zonder staart"],
      "Zaadvocht wordt nog toegevoegd; alleen de zaadcellen kunnen niet meer door de doorgesneden zaadleiders."),
    # §11.3
    M("Hoeveel bloedvaten lopen er door de navelstreng en waar gaat het bloed heen?",
      "Drie: één ader naar het kindje en twee slagaders naar de placenta",
      ["Twee: één ader naar het kindje en één slagader naar de placenta", "Drie: twee aders naar het kindje en één slagader naar de placenta", "Drie: alle drie brengen zuurstofrijk bloed van de moeder naar het kindje"],
      "Eén navelstrengader brengt zuurstof en voedingsstoffen naar het kindje; twee slagaders voeren afvalstoffen af."),
    W("In de placenta vermengt het bloed van de moeder zich met het bloed van het kindje.", False,
      "Niet waar. De bloedvaten liggen dicht langs elkaar en stoffen worden uitgewisseld, maar het bloed mengt niet."),
    O("Leg in één zin uit hoe zuurstof van de moeder bij het ongeboren kind komt.", ["placenta", "navelstrengader/ader"], 2,
      "De zuurstof gaat in de placenta door de dunne vaatwanden van het bloed van de moeder naar het bloed van het kindje en gaat dan via de navelstrengader naar het kindje.",
      "Via de placenta en daarna via de navelstrengader."),
    I("Wanneer de placenta met vruchtvliezen naar buiten komt, heet dat de ____.", "nageboorte",
      "De nageboorte is de derde fase van de bevalling."),
    M("Een zwangere vrouw drinkt regelmatig wijn. Wat gebeurt er met de alcohol?",
      "De alcohol gaat via de placenta naar het bloed van het kindje",
      ["De placenta houdt alle alcohol tegen, want hij werkt als filter", "De alcohol blijft in het vruchtwater en bereikt het bloed niet", "De vruchtvliezen breken de alcohol af"],
      "De placenta houdt veel stoffen tegen, maar alcohol, drugs, nicotine en het rodehondvirus komen er wel doorheen."),
    # §11.4
    W("Elke eicel van een vrouw bevat 23 chromosomen, waaronder een X; een Y heeft ze niet.", True,
      "Waar. Een zaadcel geeft een X of een Y door; de eicel altijd een X."),
    M("Wat bedoelt de biologie met het woord gen?",
      "De DNA-code voor één eiwit",
      ["Een compleet chromosomenpaar", "De som van alle chromosomen in een cel", "Een eigenschap die je kunt zien"],
      "Een gen is een stukje DNA met de code voor één eiwit; eiwitten bepalen je eigenschappen."),
    I("Alles wat je van een eigenschap kunt zien, heet het ____.", "fenotype",
      "Het fenotype is wat je ziet, bijvoorbeeld blauwe ogen."),
    M("Een arts doet een vruchtwaterpunctie. Waar haalt hij de cellen van het ongeboren kind vandaan?",
      "Uit het vruchtwater rond de foetus",
      ["Uit de placenta", "Uit het bloed van de moeder", "Uit de navelstreng"],
      "In het vruchtwater zitten cellen van de foetus; de arts onderzoekt hun chromosomen."),
    W("Elk kind dat met een afwijking wordt geboren, heeft die van zijn ouders geërfd.", False,
      "Niet waar. Aangeboren kan ook komen door schadelijke stoffen of door een fout in het aantal chromosomen."),
]),
76: ("B", "🔬", [
    # §11.1
    M("Een jongen krijgt zijn eerste zaadlozing. Welk hormoon zorgt ervoor dat zijn zaadballen zaadcellen blijven maken?",
      "Testosteron",
      ["Oestrogeen uit de bijballen", "Progesteron uit de prostaat", "HCG uit de zaadblaasjes"],
      "De zaadballen maken testosteron en dankzij dat hormoon blijven ze zaadcellen maken."),
    M("Een jongen heeft zaadcellen gemaakt die nog niet naar buiten zijn gekomen. In welk orgaan wachten ze op de zaadlozing?",
      "In de bijballen",
      ["In de zaadblaasjes", "In de prostaat", "In de zwellichamen"],
      "De bijballen liggen tegen de zaadballen aan en bewaren de zaadcellen tot de zaadlozing."),
    O("Leg in één zin uit wat er met de follikel gebeurt na de eisprong en welk hormoon die daarna vooral maakt.", ["geel lichaam/corpus luteum", "progesteron"], 2,
      "De lege follikel groeit onder invloed van LH uit tot het gele lichaam (corpus luteum) en maakt vooral progesteron.",
      "De lege follikel wordt het gele lichaam en maakt progesteron."),
    I("Een zaadcel bestaat uit een kop en een ____.", "staart",
      "De kop bevat de kern; met de staart zwemt de zaadcel."),
    W("Bij een vrouw komen de vagina en de urinebuis uit in dezelfde buis.", False,
      "Niet waar. De vagina en de urinebuis zijn twee verschillende buizen met twee openingen."),
    # §11.2
    M("Welk deel van het jonge embryo maakt het hormoon dat een zwangerschapstest aantoont?",
      "De vlokken",
      ["De kiemschijf", "De steel", "De holte"],
      "De vlokken maken HCG; de test toont HCG aan in de urine."),
    W("Voorvocht komt vóór de zaadlozing uit de penis en kan al zaadcellen bevatten.", True,
      "Waar. Daarom is coïtus interruptus een erg onbetrouwbare methode."),
    M("Hoe voorkomt de pil een zwangerschap?",
      "Er rijpen geen eicellen en het slijm bij de baarmoedermond wordt dikker",
      ["Hij doodt de zaadcellen in de vagina", "Hij sluit de eileiders af", "Hij laat het slijmvlies loslaten voordat de eicel er is"],
      "De pil bevat oestrogeen en progesteron: geen rijpende eicellen, geen eisprong en dikker slijm."),
    I("Het hormoonstaafje wordt onder de ____ geplaatst.", "huid",
      "Het staafje geeft hormonen af die een eisprong voorkomen."),
    M("Een vrouw heeft gisteren onbeschermd seks gehad en wil niet zwanger worden. Wat kan ze doen?",
      "De morning-afterpil nemen, hoe eerder hoe beter en binnen 72 uur",
      ["Alsnog een condoom gebruiken, want dat werkt ook achteraf", "De gewone pil twee keer zo snel achter elkaar slikken", "Wachten op haar menstruatie en dan een sterilisatie laten doen"],
      "De morning-afterpil onderdrukt de ovulatie en voorkomt innesteling; hoe eerder, hoe kleiner de kans op zwangerschap."),
    # §11.3
    W("Twee-eiige baby's delen samen één placenta en dezelfde vruchtvliezen.", False,
      "Niet waar. Een twee-eiige tweeling heeft altijd twee placenta's en elk eigen vruchtvliezen."),
    M("Welk bloedvat in de navelstreng bevat het zuurstofrijkste bloed?",
      "De navelstrengader",
      ["Een van de navelstrengslagaders", "Beide navelstrengslagaders", "Alle drie evenveel"],
      "De ader brengt zuurstof naar het kindje; de slagaders voeren afvalstoffen af."),
    O("Leg in één zin uit waarom een kindje tijdens de zwangerschap niet zelf lucht hoeft te halen.", ["zuurstof", "placenta/navelstreng/moeder"], 2,
      "Het kindje krijgt zuurstof uit het bloed van de moeder via de placenta en de navelstreng, dus zijn longen hoeven nog niet te werken.",
      "De zuurstof komt uit het bloed van de moeder via de placenta."),
    M("In welke volgorde gebeuren ontsluiting, uitdrijving en nageboorte tijdens een bevalling?",
      "Ontsluiting, uitdrijving, nageboorte",
      ["Uitdrijving, ontsluiting, nageboorte", "Ontsluiting, nageboorte, uitdrijving", "Nageboorte, ontsluiting, uitdrijving"],
      "Eerst gaat de baarmoedermond open, dan wordt de baby geboren en daarna komt de placenta."),
    I("Een wee is het samentrekken van de ____ van de baarmoeder.", "spieren|spier",
      "Weeën zijn samentrekkingen van de baarmoederspieren."),
    # §11.4
    M("Een eicel heeft altijd een X-chromosoom, een zaadcel een X of een Y. Wie bepaalt dan of het kindje een jongen of meisje wordt?",
      "De zaadcel, doordat die een X of een Y doorgeeft",
      ["De eicel, doordat die een X of een Y doorgeeft", "De moeder, want zij draagt het kindje", "Het toeval na de innesteling"],
      "Een zaadcel met een Y geeft een jongen, een zaadcel met een X een meisje."),
    W("Een litteken dat je door een ongeluk hebt, kun je aan je kinderen doorgeven.", False,
      "Niet waar. Een litteken is niet erfelijk; alleen je genen geef je door."),
    M("Iemand heeft aanleg om lang te worden, maar eet jarenlang erg weinig en blijft kleiner. Wat is hier aan de hand?",
      "Het fenotype wordt bepaald door genotype én omgeving",
      ["Het genotype is door het weinige eten veranderd", "De eigenschap is niet erfelijk", "Het fenotype wordt helemaal bepaald door de omgeving"],
      "Aanleg is erfelijk, maar het resultaat hangt ook af van de omgeving."),
    W("Bij een vlokkentest zuigt de arts cellen uit de placenta op.", True,
      "Waar. In die cellen van de placenta zitten cellen van de foetus, die worden onderzocht op fouten in de chromosomen."),
    I("Een kind met het syndroom van Down heeft ____ chromosomen in elke cel.", "47",
      "Normaal zijn het er 46; kinderen met Down hebben een extra chromosoom."),
]),
77: ("C", "📋", [
    # §11.1
    W("Het hormoon oestrogeen wordt gemaakt door de hypofyse.", False,
      "Niet waar. De hypofyse maakt FSH en LH; oestrogeen komt uit de follikel."),
    M("Wat gebeurt er in de eierstok als de hoeveelheid LH sterk stijgt?",
      "De eisprong vindt plaats en de eicel komt vrij",
      ["De follikel begint pas te groeien en maakt oestrogeen", "Het slijmvlies laat los en de menstruatie begint", "De follikel maakt voor het eerst progesteron"],
      "Een LH-piek start de ovulatie: de rijpe eicel komt uit de follikel."),
    M("Wat is de taak van de eileider?",
      "De eicel opvangen en doorgeven",
      ["De eicel laten rijpen in een follikel", "Het embryo laten uitgroeien tot een baby", "Oestrogeen maken voor het slijmvlies"],
      "De eicel komt na de eisprong in de eileider; daar kan ook de bevruchting plaatsvinden."),
    I("Zaadblaasjes en prostaat maken vocht; samen met de zaadcellen vormt dat het ____ dat de penis verlaat.", "sperma",
      "Zaadblaasjes en prostaat voegen zaadvocht toe aan de zaadcellen."),
    M("Een man heeft een zaadlozing. Welke reden zorgt ervoor dat de urine dan niet naar buiten kan?",
      "Een spiertje knijpt de urinebuis dicht",
      ["De zaadleider sluit de urinebuis af", "De urineblaas is dan altijd leeg", "De zwellichamen drukken de urinebuis dicht"],
      "Dat spiertje knijpt de urinebuis dicht, zodat alleen sperma naar buiten komt."),
    # §11.2
    M("Wat doet het zwangerschapshormoon HCG?",
      "Geen nieuwe eicelrijping en geen afstoting van het slijmvlies",
      ["Het veroorzaakt de eisprong", "Het laat het slijmvlies juist loskomen", "Het maakt het slijm bij de baarmoedermond dikker"],
      "HCG van de vlokken zorgt dat er geen menstruatie komt en geen nieuwe eicel rijpt."),
    W("Een gesteriliseerde vrouw heeft geen eisprong meer.", False,
      "Niet waar. De eicellen komen nog vrij; alleen de eileiders zijn doorgesneden, zodat de zaadcellen er niet bij kunnen."),
    M("Welk onderdeel van het jonge bolletje cellen groeit uit tot het embryo zelf?",
      "Uit de kiemschijf",
      ["Uit de vlokken", "Uit de steel", "Uit de holte"],
      "De vlokken worden de placenta, de steel de navelstreng en de kiemschijf het embryo."),
    O("Leg in één zin uit hoe de pil een eisprong voorkomt.", ["oestrogeen/progesteron/hormonen", "rijpen/rijpt/rijp"], 2,
      "De pil bevat de hormonen oestrogeen en progesteron; die zorgen ervoor dat er geen eicellen rijpen, dus is er geen eisprong.",
      "Hormonen in de pil houden de eicel tegen die moet rijpen."),
    I("Een baby die ontstaat uit ivf heet ook wel een ____baby.", "reageerbuis",
      "Bij ivf worden eicellen buiten het lichaam bevrucht, letterlijk 'in glas'."),
    # §11.3
    M("Wat gebeurt er in de eerste twaalf weken na de innesteling?",
      "Alle organen worden aangelegd",
      ["Het kindje groeit alleen nog", "De buik van de vrouw wordt duidelijk dikker", "Het kindje wordt geboren"],
      "Dit is de embryonale fase; daarna heet het kindje foetus."),
    W("Bij een eeneiige tweeling is het mogelijk dat de ene baby een jongen en de andere een meisje is.", False,
      "Niet waar. Een eeneiige tweeling is altijd van hetzelfde geslacht."),
    M("Een tweeling heeft twee placenta's en bestaat uit een jongen en een meisje. Wat voor tweeling is dit?",
      "Een twee-eiige tweeling",
      ["Een eeneiige tweeling met splitsing vóór de innesteling", "Een eeneiige tweeling met splitsing ná de innesteling", "Dat kan bij geen enkele tweeling"],
      "Twee-eiig: twee eicellen en twee zaadcellen, elk geslacht mogelijk."),
    O("Leg in één zin uit waarom de navelstreng na de geboorte wordt doorgeknipt.", ["ademen", "placenta/uitwisseling"], 2,
      "Zodra de baby geboren is gaat hij zelf ademen en heeft hij de placenta niet meer nodig voor de uitwisseling van stoffen.",
      "De baby ademt zelf en heeft de placenta niet meer nodig."),
    M("Een zwangere vrouw voelt haar kindje bewegen en haar buik wordt dikker. Hoe ver is de zwangerschap ongeveer?",
      "Rond week twintig",
      ["Ongeveer vier weken", "Ongeveer acht weken", "Ongeveer veertig weken"],
      "Pas als de foetus ongeveer twintig weken oud is, wordt de buik dikker."),
    # §11.4
    W("Van elk gen heb je één allel van je vader en één van je moeder.", True,
      "Waar. Je krijgt de helft van je chromosomen van je vader en de helft van je moeder."),
    I("Een gen is de code voor één ____.", "eiwit",
      "Eiwitten bepalen alles wat er in een cel gebeurt en dus je eigenschappen."),
    M("Welke eigenschap is volledig bepaald door de omgeving?",
      "Een litteken na een val van de fiets",
      ["De vorm van je oorlel", "De kleur van je ogen", "Je bloedgroep"],
      "Een litteken is niet erfelijk; erfelijke eigenschappen liggen in de genen."),
    W("Het gen voor oogkleur kan de varianten blauw en bruin hebben; zo'n variant heet een allel.", True,
      "Waar. Een variant van een gen heet een allel."),
    I("Kinderen met het syndroom van Down zijn meestal ontstaan uit een eicel met ____ chromosomen in plaats van 23.", "24",
      "Het boek: kinderen met Down zijn meestal ontstaan uit een eicel met 24 chromosomen, in plaats van 23. Daardoor hebben ze 47 chromosomen."),
]),
78: ("D", "🧪", [
    # §11.1
    M("Welke volgorde aan het begin van de menstruatiecyclus klopt?",
      "FSH, groei van de follikel, oestrogeen",
      ["Oestrogeen, FSH, groei van de follikel, eisprong", "Groei van de follikel, LH, progesteron, eisprong", "Oestrogeen, eisprong, FSH, groei van de follikel"],
      "FSH stimuleert de groei van de follikel; de groeiende follikel maakt oestrogeen."),
    I("In de menstruatiecyclus is de ____ het moment waarop de follikel openbarst.", "ovulatie",
      "Eisprong en ovulatie betekenen hetzelfde."),
    M("Welke bewering over de zaadcel is juist?",
      "De kern zit in de kop",
      ["De zaadcel is groter dan de eicel doordat hij veel voedingsstoffen bevat", "De zaadcel heeft geen kern", "De zaadcel wordt in de prostaat gemaakt"],
      "Een zaadcel is veel kleiner dan een eicel en wordt in de zaadbal gemaakt."),
    O("Leg in één zin uit waarom er na de eisprong geen nieuwe eicel meer rijpt.", ["progesteron", "FSH/hypofyse"], 2,
      "Het gele lichaam maakt progesteron en dat remt de productie van FSH en LH uit de hypofyse, dus rijpt er geen nieuwe eicel.",
      "Progesteron remt FSH uit de hypofyse."),
    W("Het gele lichaam is de follikel die na de eisprong leeg is.", True,
      "Waar. De lege follikel heet vanaf dat moment het gele lichaam."),
    # §11.2
    M("Na de innesteling maakt het gele lichaam nog steeds progesteron. Welk effect heeft dat op het slijmvlies?",
      "Het blijft dik en doorbloed, dus geen menstruatie",
      ["Het laat los, zodat de innesteling kan beginnen", "Het wordt dunner zodat het embryo kan groeien", "Het verandert in de placenta"],
      "Progesteron houdt het slijmvlies dik en doorbloed; zo blijft er plaats voor het embryo."),
    W("Voorvocht en zaadvocht zijn twee namen voor hetzelfde vocht.", False,
      "Niet waar. Voorvocht komt vóór de zaadlozing uit de penis; zaadvocht wordt tijdens de zaadlozing toegevoegd."),
    I("Ivf betekent in-vitro-____, dat is letterlijk bevruchting in glas.", "fertilisatie",
      "Fertilisatie is bevruchting; vitro is glas."),
    M("Een spiraaltje werkt doordat...",
      "het zaadcellen minder vruchtbaar maakt en innesteling voorkomt",
      ["het geen eicel laat rijpen, net als de pil", "het de eileiders afsluit zodat zaadcellen er niet bij kunnen", "het elke dag oestrogeen afgeeft onder de huid"],
      "Het spiraaltje zit in de baarmoeder en voorkomt dat een bevruchte eicel zich vastzet."),
    M("Een bolletje cellen is vijf dagen oud. Wat is er dan ontstaan?",
      "Een holte met daarin de kiemschijf",
      ["Een navelstreng met drie bloedvaten", "Een foetus met alle organen", "Het gele lichaam met progesteron"],
      "Vijf dagen na de bevruchting ontstaat in het bolletje cellen een holte met daarin de kiemschijf. De vlokken groeien pas tijdens de innesteling."),
    # §11.3
    I("Het kindje wordt beschermd door de vruchtvliezen en het ____.", "vruchtwater",
      "De zak met vloeistof beschermt het kindje tegen stoten."),
    M("Wat gebeurt er in de eerste fase van de bevalling?",
      "De baarmoedermond gaat open en de vliezen breken",
      ["Persweeën duwen het kindje naar buiten", "De moederkoek komt los en wordt uitgedreven", "Het kindje draait met het hoofdje naar beneden"],
      "De eerste fase heet ontsluiting."),
    W("Het bloed in de navelstrengslagaders is rijk aan zuurstof.", False,
      "Niet waar. De slagaders voeren afvalstoffen van het kindje naar de moeder; de ader brengt de zuurstof."),
    M("Waarom wordt bij een dwarsligging een keizersnede gedaan?",
      "Geboorte via de vagina is dan onmogelijk",
      ["De baarmoedermond gaat dan niet open", "De moederkoek komt dan eerst naar buiten", "De navelstreng is dan te kort"],
      "Bij een keizersnede haalt een chirurg de baby via een snee onder in de buik."),
    W("Elk embryo van een twee-eiige tweeling heeft een eigen placenta en eigen vruchtvliezen.", True,
      "Waar. Een twee-eiige tweeling heeft altijd twee placenta's."),
    # §11.4
    M("Hoeveel chromosomen zitten er in een zaadcel en hoeveel in een bevruchte eicel?",
      "23 en 46",
      ["46 en 46", "23 en 23", "46 en 92"],
      "Bij de bevruchting smelten de kernen samen: 23 plus 23 is 46."),
    O("Leg in één zin uit waarom broers en zussen niet precies op elkaar lijken, hoewel ze dezelfde ouders hebben.", ["chromosomen", "andere/verschillende/niet dezelfde"], 2,
      "Elke eicel en zaadcel krijgt een andere set van 23 chromosomen, dus broers en zussen hebben niet precies dezelfde genen.",
      "Ze krijgen niet dezelfde sets chromosomen."),
    M("Welke omschrijving past bij het genotype?",
      "Alle genen van een persoon samen",
      ["Alles wat je van een eigenschap kunt zien", "De invloed van de omgeving op je uiterlijk", "Het aantal chromosomen in een cel"],
      "Het genotype zijn de genen; het fenotype is wat je ziet."),
    W("Een kind met aanleg voor gitaarspelen wordt vanzelf goed zonder te oefenen.", False,
      "Niet waar. Het fenotype is het resultaat van genotype (aanleg) én omgeving (oefenen)."),
    I("Een arts die tijdens de zwangerschap een vlokkentest doet, verricht ____ onderzoek.", "prenataal",
      "Voorbeelden zijn de vruchtwaterpunctie en de vlokkentest."),
]),
}
# open-vraag-posities (1-based): niet als laatste
OPEN_POS = {75: (7, 13), 76: (3, 13), 77: (9, 14), 78: (4, 17)}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_gemengd_seed_75')
    for nr, (letter, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        tel = {t: sum(v["type"] == t for v in vr) for t in ("mc", "waaronwaar", "invul", "open")}
        assert tel == {"mc": 9, "waaronwaar": 5, "invul": 4, "open": 2}, (nr, tel)
        assert tuple(i + 1 for i, v in enumerate(vr) if v["type"] == "open") == OPEN_POS[nr], nr
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {
            "id": f"ex-h3-biologie-{nr}",
            "hoofdstuk": 11,
            "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
            "paragraaf": "mix",
            "titel": f"Toets {nr} — H11 gemengd {letter}: proefwerk Voortplanting",
            "vak": "Biologie · HAVO 3 (H11)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie H11 gemengd) — gegenereerd door tools/gen_biologie_h11_gemengd.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen {tel}, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
