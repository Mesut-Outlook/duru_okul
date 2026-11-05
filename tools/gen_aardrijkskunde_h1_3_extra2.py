#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.3 Verschillen tussen rollen in de wereldhandel (extra toetsen 116–120).
Schrijft havo3/aardrijkskunde/js/data/examen_116..120.js (ex-h3-ak-116..120).
mc-volgorde willekeurig (geseed), opnieuw geschud tot gate-regels 3/16/17 kloppen.
"""
import json, os, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'aardrijkskunde', 'js', 'data')


def _u(uitleg, pg):
    return f"{uitleg} (boek p. {pg})"


def M(vraag, goed, fout, uitleg, pg):
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": fout, "uitleg": _u(uitleg, pg)}


def W(vraag, antwoord, uitleg, pg):
    return {"type": "waaronwaar", "vraag": vraag, "antwoord": antwoord, "uitleg": _u(uitleg, pg)}


def I(vraag, antwoord, uitleg, pg):
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "uitleg": _u(uitleg, pg)}


def O(vraag, sleutels, min_, model, uitleg, pg):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": min_,
            "modelantwoord": model, "uitleg": _u(uitleg, pg)}


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
116: ("Exploitatie- en vestigingskolonies: de koloniale erfenis", "🏛️", [
    M("Een kolonisator neemt een overzees gebied in bezit, vooral om de natuurlijke hulpbronnen naar het eigen land te halen. Welk type kolonie ontstaat daardoor?",
      "Een exploitatiekolonie, waar de hulpbronnen centraal staan",
      ["Een vestigingskolonie, waar de kolonisten centraal staan",
       "Een lagelonenland, waar de goedkope arbeiders centraal staan",
       "Een moederland, waar de eigen bevolking centraal staat"],
      "Bij een exploitatiekolonie eiste de kolonisator de natuurlijke hulpbronnen van het land op.", 28),
    M("Wat kenmerkt een vestigingskolonie volgens het boek?",
      "Immigranten vestigden zich en richtten het land in naar het model van het moederland",
      ["De kolonisator haalde de bodemschatten weg en liet de lokale bevolking verder volledig met rust",
       "Het land bleef onder eigen bestuur terwijl er alleen op beperkte schaal handel werd gedreven door kooplieden",
       "Er kwamen geen nieuwe bewoners, maar wel veel zendelingen, soldaten en ambtenaren uit Europa"],
      "In een vestigingskolonie herinrichtten immigranten het land naar het voorbeeld van het moederland.", 28),
    M("Welke economische rol hebben veel voormalige exploitatiekolonies sinds de dekolonisatie nog steeds?",
      "Vooral het exporteren van onbewerkte grondstoffen",
      ["Het assembleren van hightech eindproducten",
       "Het leveren van financiële diensten aan banken",
       "Het beheren van grote internationale havens"],
      "Sinds de dekolonisatie is hun belangrijkste economische rol nog steeds de export van onbewerkte grondstoffen.", 28),
    M("Een voormalige exploitatiekolonie wil meer verdienen aan haar export. Wat levert volgens het boek meer op dan haar huidige exportproduct?",
      "Het exporteren van bewerkte producten in plaats van onbewerkte grondstoffen",
      ["Het exporteren van nog grotere hoeveelheden onbewerkte grondstoffen naar dezelfde afnemers",
       "Het verhogen van de invoerrechten op alle producten uit het voormalige moederland",
       "Het sluiten van de grenzen voor alle buitenlandse multinationals en investeerders"],
      "Met onbewerkte grondstoffen verdienen landen minder dan met bewerkte producten.", 28),
    M("Welke bewering over de huidige welvaart van voormalige koloniën past bij de tekst?",
      "Vestigingskolonies zijn vaak welvarend, exploitatiekolonies hebben vaak een lage welvaart",
      ["Voormalige exploitatiekolonies zijn bijna altijd welvarender dan voormalige vestigingskolonies",
       "Het type kolonie heeft geen verband met de welvaart die een land nu heeft",
       "Alle voormalige koloniën hebben na de dekolonisatie dezelfde hoge welvaart gekregen"],
      "Exploitatiekolonies hebben nu vaak een lage welvaart, vestigingskolonies zoals de VS en Canada een hoge.", 28),
    M("Bron 20 laat zien dat er in een voormalige exploitatiekolonie steeds meer producten worden bewerkt. Wat concludeert het boek over de inkomens?",
      "De inkomens zijn nog steeds laag, het kan een lagelonenland blijven",
      ["De inkomens stijgen automatisch tot het niveau van het moederland",
       "De inkomens zijn laag omdat er helemaal niets meer wordt bewerkt",
       "De inkomens spelen geen rol in de rol van het land in de wereldhandel"],
      "Er worden steeds meer producten bewerkt, maar de inkomens blijven in veel oud-kolonies nog laag.", 28),
    M("Welke vraag uit de intro van de paragraaf laat zien waarom 'ontwikkeling' een discutabele term is?",
      "Als een land ontwikkeld is, stopt het dan met ontwikkelen?",
      ["Hoeveel kolonies zijn er in de negentiende eeuw geweest?",
       "Welk land exporteert wereldwijd de meeste onbewerkte grondstoffen?",
       "Welke multinationals vestigen zich het liefst in lagelonenlanden?"],
      "De intro vraagt of een ontwikkeld land stopt met ontwikkelen en of arme landen onderontwikkeld zijn.", 28),
    M("Wat laat de legenda van bron 18 (wereldwijde verdeling van export) naast inkomensgroepen zien?",
      "Een indeling in regio's, zoals Noord-Amerika, sub-Sahara Afrika en Zuid-Azië",
      ["Een indeling naar de vroegere kolonisator, zoals Nederland, Frankrijk en Spanje",
       "Een indeling naar politiek systeem, zoals democratie en dictatuur per land",
       "Een indeling naar het belangrijkste exportproduct, zoals olie, graan en textiel"],
      "In de legenda staan regio's zoals Noord-Amerika, sub-Sahara Afrika, Zuid-Azië en Europa en Rusland.", 28),
    M("Welk rijtje bevat uitsluitend landen die het boek noemt als voormalige vestigingskolonies?",
      "Verenigde Staten, Australië, Nieuw-Zeeland en Canada",
      ["Brazilië, Vietnam, Australië en Canada",
       "Verenigde Staten, Brazilië, Nieuw-Zeeland en Vietnam",
       "Canada, Nieuw-Zeeland, Vietnam en Brazilië"],
      "Het boek noemt de VS, Australië, Nieuw-Zeeland en Canada als vestigingskolonies met hoge welvaart.", 28),
    W("Een vestigingskolonie was vooral bedoeld om natuurlijke hulpbronnen naar het moederland te verschepen.", False,
      "Niet waar. Dat is een exploitatiekolonie; in een vestigingskolonie vestigden immigranten zich en richtten ze het land in.", 28),
    W("Voormalige exploitatiekolonies hebben nu doorgaans een hogere welvaart dan voormalige vestigingskolonies.", False,
      "Niet waar. Het is andersom: exploitatiekolonies hebben vaak een lage welvaart, vestigingskolonies een hoge.", 28),
    W("Volgens de intro kunnen landen niet met elkaar worden vergeleken, omdat 'ontwikkeling' een discutabele term is.", False,
      "Niet waar. Toch kunnen landen worden vergeleken en kun je iets zeggen over de verschillen in welvaart.", 28),
    W("Bron 18 laat de verdeling van de wereldwijde export zien.", True,
      "Waar. Bron 18 heet 'Wereldwijde verdeling van export'.", 28),
    W("Een deel van de oud-exploitatiekolonies behoort tot de lagelonenlanden.", True,
      "Waar. Er is een deel van deze oud-kolonies waar de inkomens nog steeds laag zijn.", 28),
    I("In de intro van de paragraaf staat de vraag: zijn arme landen ____?", "onderontwikkeld", "De intro vraagt: Zijn arme landen onderontwikkeld?", 28),
    I("Brazilië heeft ruim twee keer meer ____ dan Vietnam en een veel groter oppervlakte.", "inwoners", "Brazilië heeft ruim twee keer meer inwoners dan Vietnam.", 28),
    I("India wordt in bron 18 ingedeeld als ____-middeninkomensland.", "lage|lage-", "India is een lage-middeninkomensland.", 28),
    I("Brazilië heeft een veel groter oppervlakte dan Vietnam, maar ze exporteren ongeveer ____.", "evenveel|even veel", "Brazilië en Vietnam exporteren ongeveer evenveel.", 28),
    O("Leg uit waarom een voormalige exploitatiekolonie met haar huidige export vaak weinig verdient.", ["onbewerkt/onbewerkte", "minder/lager"], 2,
      "Zij exporteert vooral onbewerkte grondstoffen en daarmee verdient een land minder dan met bewerkte producten.",
      "Ze exporteren onbewerkte grondstoffen; dat levert minder op dan bewerkte producten.", 28),
    O("Noem twee verschillen tussen een exploitatiekolonie en een vestigingskolonie.", ["hulpbronnen/grondstoffen", "immigranten/kolonisten", "moederland"], 2,
      "In een exploitatiekolonie werden de hulpbronnen opgeëist; in een vestigingskolonie vestigden immigranten zich en richtten het land in naar het moederland.",
      "Bij de ene gaat het om hulpbronnen, bij de andere vestigen immigranten zich.", 28)
]),

117: ("Interne en externe oorzaken en het politieke systeem", "🗳️", [
    M("In een land is het onderwijs slecht geregeld. Wat voor oorzaak voor een lage ontwikkeling is dat volgens het boek?",
      "Een interne oorzaak, die binnen het land zelf ligt",
      ["Een externe oorzaak, die buiten het land zelf ligt",
       "Een koloniale oorzaak, die in het moederland ligt",
       "Een mondiale oorzaak, die bij de VN ligt"],
      "De manier waarop het onderwijs is geregeld is een voorbeeld van een interne oorzaak.", 28),
    M("Waarom noemt het boek de export van onbewerkte grondstoffen door een oud-kolonie een externe oorzaak?",
      "Omdat de oorzaak buiten het land zelf ligt, in het koloniale verleden",
      ["Omdat de regering van dat land de export zelf strikt heeft verboden",
       "Omdat het onderwijs in dat land al decennia slecht is geregeld",
       "Omdat grondstoffen alleen buiten de landsgrenzen te vinden zijn"],
      "Een externe oorzaak ligt buiten het land zelf, zoals de koloniale rol als grondstoffenleverancier.", 28),
    M("Welke voorbeelden van interne oorzaken noemt de tekst?",
      "Het onderwijs, de rechten van mensen en de manier van besturen",
      ["De ligging aan zee, het klimaat en de hoeveelheid grondstoffen",
       "De koloniale grenzen, de handelsroutes en het moederland",
       "De hoogte van invoerrechten, de dollarkoers en het aantal havens"],
      "Onderwijs, rechten van mensen en bestuur liggen binnen het land zelf.", 28),
    M("Een multinational zoekt een land voor een nieuwe fabriek. Welk land trekt volgens het boek eerder multinationals aan?",
      "Een land met meer vrijheid, democratie en minder corruptie",
      ["Een land waar één persoon snel alle besluiten neemt",
       "Een land met zo weinig regels dat niemand toezicht houdt",
       "Een land waar de overheid niets in onderwijs investeert"],
      "In een land met meer vrijheid en democratie vestigen multinationals zich eerder.", 28),
    M("Welke groepen blijven volgens de tekst weg uit een land waar één persoon de macht heeft en corruptie voorkomt?",
      "Toeristen en buitenlandse investeerders",
      ["Alle eigen inwoners en de lokale boeren",
       "Uitsluitend de leden van de Verenigde Naties",
       "Vooral de vroegere kolonisten en hun nakomelingen"],
      "Toeristen en buitenlandse investeerders blijven weg uit een land met een dictatoriaal politiek systeem.", 28),
    M("Welke uitgaven van de overheid komen volgens het boek ten goede aan de ontwikkeling van een land?",
      "Investeringen in onderwijs, gezondheidszorg en basisvoorzieningen",
      ["Investeringen in leger, politie en grensbewaking in plaats van scholen",
       "Subsidies voor het vertrek van multinationals naar het buitenland",
       "Uitgaven aan paleizen en feesten voor de regerende leider"],
      "Als de overheid investeert in onderwijs, gezondheidszorg en basisvoorzieningen, komt dat de ontwikkeling ten goede.", 28),
    M("Wat is het gevolg als een dictatoriaal land door buitenlandse partners wordt gemeden?",
      "Het land kan zich daardoor minder goed ontwikkelen",
      ["Het land ontwikkelt zich sneller door zelfstandigheid",
       "Het land krijgt juist meer multinationals binnen",
       "Het land wordt meteen lid van een handelsblok"],
      "Zonder buitenlandse samenwerking kan het land zich minder ontwikkelen.", 28),
    M("Wat heeft SDG 16 'Vrede, justitie en sterke publieke diensten' met het politieke systeem te maken?",
      "Het gaat over hoe een land wordt bestuurd, zoals rechtspraak en publieke diensten",
      ["Het gaat alleen over de hoogte van het bbp per hoofd en de verdeling van welvaart",
       "Het gaat over de export van onbewerkte grondstoffen naar andere landen en continenten",
       "Het gaat over het aantal kolonies dat een land vroeger had en nu nog heeft"],
      "Het politieke systeem is de manier waarop een land wordt bestuurd; justitie en publieke diensten horen daarbij.", 32),
    M("Welke kenmerken wijzen bij het bepalen van de stabiliteit van een land op een lage stabiliteit?",
      "Een burgeroorlog, geen persvrijheid en veel corruptie",
      ["Vrije verkiezingen, persvrijheid en kleine ongelijkheid",
       "Vrijheid van geloof en het recht om te demonstreren",
       "Een hoge Gini-coëfficiënt en een klein aantal inwoners"],
      "Burgeroorlog, geen persvrijheid, aantasting van mensenrechten en veel corruptie horen bij lage stabiliteit.", 30),
    W("Hoe een land wordt bestuurd heeft volgens het boek geen invloed op de vestiging van multinationals.", False,
      "Niet waar. In een land met één machthebber en corruptie vestigen zich weinig multinationals.", 28),
    W("Een dictatoriaal land is geen populaire samenwerkingspartner.", True,
      "Waar. Dat staat letterlijk in het boek.", 28),
    W("In een land met veel vrijheid en democratie vestigen multinationals zich juist minder snel.", False,
      "Niet waar. Daar kan de handel juist tot ontwikkeling komen.", 28),
    W("De huidige rol van een land in de wereldhandel wordt alleen bepaald door interne oorzaken.", False,
      "Niet waar. Ook externe oorzaken uit het verleden spelen een rol.", 28),
    W("De rol van landen in de wereldhandel is beïnvloed door oorzaken uit het verleden.", True,
      "Waar. Het boek noemt kolonialisme als voorbeeld.", 28),
    I("De Sustainable Development Goals zijn opgesteld door alle ____ landen die lid zijn van de Verenigde Naties.", "193", "Alle 193 VN-landen stelden de 17 doelen op.", 28),
    I("In een land met meer vrijheid en democratie kan de ____ tot ontwikkeling komen.", "handel", "In een vrij, democratisch land kan de handel tot ontwikkeling komen.", 28),
    I("De SDG's proberen bij te dragen aan de ontwikkeling van het ____.", "welzijn", "De SDG's willen bijdragen aan de ontwikkeling van het welzijn.", 28),
    I("SDG's zijn in het Nederlands de duurzame ____doelen.", "ontwikkelings", "SDG staat voor duurzame ontwikkelingsdoelen.", 28),
    O("Leg uit waarom zich weinig multinationals vestigen in een land waar één persoon alle macht heeft.", ["corruptie", "vrijheden/vrijheid", "investeerders/investeringen"], 2,
      "Mensen hebben er weinig vrijheden en er is corruptie. Buitenlandse investeerders en toeristen blijven weg.",
      "Er is weinig vrijheid en er is corruptie, dus investeerders blijven weg.", 28),
    O("Geef een voorbeeld van een interne en een externe oorzaak van verschillen tussen landen.", ["onderwijs/rechten/bestuur", "grondstoffen/kolonialisme/verleden"], 2,
      "Intern: de manier waarop het onderwijs is geregeld. Extern: de export van onbewerkte grondstoffen door een voormalige kolonie door het koloniale verleden.",
      "Intern is het onderwijs; extern is het koloniale verleden met de export van grondstoffen.", 28)
]),

118: ("De Gini-coëfficiënt en sociale ongelijkheid", "⚖️", [
    M("Welk land in bron 21 heeft de kleinste sociale ongelijkheid?",
      "Slowakije",
      ["Nederland", "Zweden", "India"],
      "Slowakije heeft de laagste Gini-coëfficiënt (0,24) in bron 21.", 31),
    M("Welke volgorde zet landen uit bron 21 op van kleine naar grote sociale ongelijkheid?",
      "Nederland, Zweden, India, Kameroen",
      ["Zweden, Nederland, Kameroen, India",
       "India, Zweden, Nederland, Kameroen",
       "Kameroen, India, Zweden, Nederland"],
      "De Gini-coëfficiënten zijn Nederland 0,26, Zweden 0,30, India 0,33 en Kameroen 0,42.", 31),
    M("Land A heeft een Gini-coëfficiënt van 0,20 en land B van 0,45. Wat concludeer je?",
      "De sociale ongelijkheid is in land B groter dan in land A",
      ["De sociale ongelijkheid is in land A groter dan in land B",
       "De sociale ongelijkheid is in beide landen precies even groot",
       "Land B is welvarender dan land A, omdat het getal hoger is"],
      "Hoe hoger de Gini-coëfficiënt, hoe groter de sociale ongelijkheid.", 31),
    M("Wat meet de Gini-coëfficiënt?",
      "Hoe ongelijk de welvaart binnen een land is verdeeld",
      ["Hoeveel welvaart een land in totaal heeft opgebouwd",
       "Hoeveel een land per jaar aan het buitenland verkoopt",
       "Hoeveel mensen er in een land onder de armoedegrens leven"],
      "De Gini-coëfficiënt geeft de sociale ongelijkheid aan met een getal tussen 0 en 1.", 29),
    M("Waarom zegt een hoog bbp per hoofd weinig over de sociale ongelijkheid in een land?",
      "Het is een gemiddelde en toont niet hoe welvaart is verdeeld",
      ["Het telt alleen de inkomens van de allerarmsten in een land mee",
       "Het is een getal dat alleen voor exportproducten wordt berekend",
       "Het wordt elk jaar door de VN op nul teruggezet voor elk land"],
      "Niet in alle landen is de welvaart even goed verdeeld, ook niet bij een hoog bbp per hoofd.", 29),
    M("Wat gebeurt er volgens de tekst wanneer de sociale ongelijkheid in een land groot is?",
      "Slechts weinig mensen profiteren van de groeiende welvaart",
      ["Iedereen profiteert in dezelfde mate van de groeiende welvaart",
       "De welvaart groeit niet meer, omdat de export stilvalt",
       "De overheid kan geen belasting meer van de bevolking innen"],
      "Bij grote sociale ongelijkheid profiteren maar weinig mensen van de groeiende welvaart.", 29),
    M("Land A heeft een Gini-coëfficiënt van 0,30 en land B van 0,50. De Gini-coëfficiënt van land C ligt ertussen. Welke waarde past daarbij?",
      "0,38",
      ["0,24", "0,28", "0,55"],
      "Alleen 0,38 ligt tussen 0,30 en 0,50.", 29),
    M("Welke twee landen uit bron 21 liggen qua Gini-coëfficiënt het dichtst bij elkaar?",
      "Kameroen en de Verenigde Staten",
      ["Nederland en Slowakije",
       "India en Zweden",
       "Brazilië en Kameroen"],
      "Het verschil tussen Kameroen en de VS is maar 0,01; bij de andere paren is het groter.", 31),
    M("Een land verandert de verdeling van welvaart zodat de Gini-coëfficiënt van 0,50 naar 0,38 gaat. Wat is er gebeurd?",
      "De sociale ongelijkheid is kleiner geworden",
      ["De sociale ongelijkheid is groter geworden",
       "Het land is ineens een hoge-inkomensland geworden",
       "Het land heeft de export van grondstoffen gestaakt"],
      "Een lager getal dichter bij 0 betekent een kleinere sociale ongelijkheid.", 29),
    W("India (0,33) heeft een kleinere sociale ongelijkheid dan Zweden (0,30).", False,
      "Niet waar. Een hoger getal betekent grotere ongelijkheid, dus India is ongelijker dan Zweden.", 31),
    W("De Verenigde Staten hebben een lagere Gini-coëfficiënt dan Nederland.", False,
      "Niet waar. De VS hebben 0,41 en Nederland 0,26.", 31),
    W("De Gini-coëfficiënten in bron 21 zijn van het jaar 2022.", True,
      "Waar. In de tabel staat 'Gini-coëfficiënt (2022)'.", 31),
    W("In bron 21 heeft Zweden een lagere Gini-coëfficiënt dan de Verenigde Staten.", True,
      "Waar. Zweden heeft 0,30 en de VS 0,41.", 31),
    W("De Gini-coëfficiënt kan waarden tussen 1 en 100 aannemen.", False,
      "Niet waar. De Gini-coëfficiënt is een getal tussen 0 en 1.", 29),
    I("Hoe dichter de Gini-coëfficiënt bij het getal ____ ligt, hoe kleiner de sociale ongelijkheid.", "0|nul",
      "Dicht bij 0 betekent een kleine sociale ongelijkheid.", 29),
    I("Het land met de grootste sociale ongelijkheid in bron 21 is ____.", "Brazilië|Brazilie",
      "Brazilië heeft de hoogste Gini-coëfficiënt (0,52).", 31),
    I("De Gini-coëfficiënt van Nederland is volgens bron 21 ____.", "0,26",
      "Nederland heeft 0,26.", 31),
    I("De Gini-coëfficiënt van de Verenigde Staten is volgens bron 21 ____.", "0,41",
      "De VS hebben 0,41.", 31),
    O("Leg uit waarom een land met een hoog bbp per hoofd toch een grote sociale ongelijkheid kan hebben.", ["verdeeld/verdeling", "profiteren/weinig mensen"], 2,
      "Niet in alle landen is de welvaart even goed verdeeld. Bij grote ongelijkheid profiteren maar weinig mensen van de groeiende welvaart.",
      "De welvaart is slecht verdeeld, dus weinig mensen profiteren ervan.", 29),
    O("Land A heeft een Gini-coëfficiënt van 0,50 en land B van 0,25. Leg uit wat dit zegt over de sociale ongelijkheid in beide landen.", ["groter/hoger", "dichter bij 0/dichter bij nul/kleiner"], 2,
      "In land A is de sociale ongelijkheid groter, want hoe dichter bij 0 de Gini-coëfficiënt ligt, hoe kleiner de ongelijkheid.",
      "In land A is de ongelijkheid groter; dichter bij 0 is kleiner.", 29)
]),

119: ("De SDG's en de manier waarop landen zich ontwikkelen", "🎯", [
    M("Welk doel hoort bij SDG 14?",
      "Leven in het water",
      ["Leven op het land", "Klimaatactie", "Schoon water en sanitair"],
      "In bron 19 staat SDG 14 voor 'Leven in het water'.", 29),
    M("Welk SDG gaat vooral over de ontwikkeling van welvaart en welzijn en niet direct over het milieu?",
      "Geen armoede",
      ["Klimaatactie", "Leven in het water", "Leven op het land"],
      "Geen armoede gaat over welvaart en welzijn; de andere doelen gaan over milieu en natuur.", 31),
    M("Over welke SDG's gaat het artikel over meisjes in het onderwijs (bron 22) vooral?",
      "Kwaliteitsonderwijs en gendergelijkheid",
      ["Klimaatactie, leven in het water en leven op het land",
       "Betaalbare energie en duurzame steden en gemeenschappen",
       "Vrede, justitie en partnerschap"],
      "Het artikel gaat over onderwijs voor meisjes: kwaliteitsonderwijs en gendergelijkheid.", 31),
    M("Wat gebeurt er volgens Rosling (bron 22) als vrouwen onderwijs hebben gevolgd?",
      "Moeders besluiten minder kinderen te krijgen en meer kinderen blijven leven",
      ["Moeders krijgen juist meer kinderen, waardoor de bevolking sneller groeit",
       "Kinderen krijgen minder aandacht, omdat moeders meer gaan werken",
       "De beroepsbevolking wordt kleiner doordat vrouwen stoppen met werken"],
      "Goed opgeleide moeders besluiten minder kinderen te krijgen en meer kinderen blijven leven.", 31),
    M("Wat zegt bron 22 over de achterstand van meisjes in het lager onderwijs?",
      "Ze hebben die bijna weggewerkt, 90 procent tegen 92 procent van de jongens",
      ["Meisjes lopen nog ver achter: 40 procent tegen 92 procent van de jongens",
       "Meisjes gaan vaker naar school: 92 procent tegen 90 procent van de jongens",
       "Meisjes en jongens gaan elk voor precies 100 procent naar school"],
      "Wereldwijd gaat 90 procent van de meisjes naar de lagere school tegen 92 procent van de jongens.", 31),
    M("Welke twee zaken proberen de SDG's volgens het boek vooral te bereiken?",
      "Minder ongelijkheid en meer aandacht voor het milieu en de leefomgeving",
      ["Meer export van grondstoffen en minder rekening houden met het milieu",
       "Meer macht voor rijke landen en minder inspraak voor arme landen in de VN",
       "Minder handel tussen landen en meer controle op de landsgrenzen"],
      "De SDG's streven naar minder ongelijkheid en meer aandacht voor milieu en leefomgeving.", 29),
    M("Waarvoor worden de SDG's tegenwoordig volgens het boek gebruikt?",
      "Als richtlijn voor een betere inrichting van de samenleving",
      ["Als wet die elk land direct moet uitvoeren op straffe van boetes",
       "Als lijst van landen die lid mogen worden van de Verenigde Naties",
       "Als meetlat voor de omvang van de wereldwijde goederenexport"],
      "De SDG's worden gebruikt als richtlijn voor een betere inrichting van de samenleving.", 29),
    M("Wat zegt het boek over de manier waarop naar ontwikkeling wordt gekeken?",
      "Die is de afgelopen jaren vaak veranderd en is onderwerp van discussie",
      ["Die staat al sinds de koloniale tijd onomstreden vast in alle landen",
       "Die wordt alleen bepaald door de hoogte van het bbp per hoofd van een land",
       "Die is door de VN verboden om nog verder te laten bespreken"],
      "Hoe naar ontwikkeling wordt gekeken is vaak veranderd en onderwerp van discussie.", 29),
    M("Een gemeente wil minder CO2 uitstoten. Bij welk SDG past dat het best?",
      "Klimaatactie",
      ["Kwaliteitsonderwijs", "Gendergelijkheid", "Geen armoede"],
      "Het terugdringen van CO2-uitstoot past bij SDG 13 'Klimaatactie'.", 29),
    W("De SDG's zijn opgesteld door de lage- en middeninkomenslanden die lid zijn van de Verenigde Naties.", False,
      "Niet waar. Alle 193 lidstaten van de VN stelden de SDG's op.", 29),
    W("In de opdracht verdeel je de SDG's in een venndiagram over welvaart en welzijn, duurzaamheid of allebei.", True,
      "Waar. Dat is het venndiagram in de opdracht.", 31),
    W("Volgens Rosling wordt de beroepsbevolking minder divers als vrouwen onderwijs hebben gevolgd.", False,
      "Niet waar. De beroepsbevolking wordt juist meer divers.", 31),
    W("Een hoge-inkomensland als Zweden hoeft zich volgens de SDG's op geen enkel punt verder te ontwikkelen.", False,
      "Niet waar. Ook veel hoge-inkomenslanden hebben nog een flinke slag te slaan.", 29),
    W("SDG 16 en SDG 17 behoren tot de zeventien duurzame ontwikkelingsdoelen.", True,
      "Waar. SDG 16 is 'Vrede, justitie en sterke publieke diensten' en SDG 17 'Partnerschap om doelstellingen te bereiken'.", 29),
    I("SDG 10 heet 'Ongelijkheid ____'.", "verminderen",
      "SDG 10 is 'Ongelijkheid verminderen'.", 29),
    I("SDG 16 heet 'Vrede, justitie en sterke publieke ____'.", "diensten",
      "SDG 16 is 'Vrede, justitie en sterke publieke diensten'.", 29),
    I("SDG 17 heet 'Partnerschap om doelstellingen te ____'.", "bereiken",
      "SDG 17 is 'Partnerschap om doelstellingen te bereiken'.", 29),
    I("Het eerste SDG, 'Geen armoede', heeft nummer ____.", "1|één|een",
      "Geen armoede is SDG 1.", 29),
    O("Leg uit waarom de SDG's laten zien dat ook rijke landen zich nog moeten ontwikkelen.", ["ongelijkheid", "milieu/klimaat/duurzaam"], 2,
      "De SDG's gaan over minder ongelijkheid en meer rekening houden met het milieu, en daar hebben ook hoge-inkomenslanden nog een flinke slag te slaan.",
      "Ook rijke landen hebben ongelijkheid en milieuproblemen waaraan ze moeten werken.", 29),
    O("Noem twee gevolgen die het onderwijzen van meisjes volgens Rosling heeft voor een samenleving.", ["divers/diverser", "minder kinderen", "investeren/tijd en energie"], 2,
      "De beroepsbevolking wordt meer divers en goed opgeleide moeders krijgen minder kinderen; er wordt ook meer tijd en energie in het onderwijs van elk kind geïnvesteerd.",
      "Meer diverse beroepsbevolking en minder kinderen per moeder.", 31)
]),

120: ("Landenvergelijking: Congo, VS, Zuid-Afrika en de BRICS", "🌍", [
    M("Welke rol heeft de Democratische Republiek Congo in de wereldhandel volgens bron 23?",
      "Het leveren van onbewerkte natuurlijke hulpbronnen, vooral koper",
      ["Het leveren van gevarieerde industriële eindproducten, vooral machines",
       "Het leveren van financiële diensten aan het moederland, vooral België",
       "Het leveren van landbouwproducten aan de VS, vooral graan"],
      "De export van Dem. Rep. Congo bestaat vooral uit koperproducten, onbewerkte hulpbronnen.", 32),
    M("Het bbp per hoofd van de VS (€ 60.000) is hoeveel keer zo groot als dat van Dem. Rep. Congo (€ 1000)?",
      "60 keer",
      ["6 keer", "16 keer", "600 keer"],
      "60.000 gedeeld door 1000 is 60.", 32),
    M("Welke productgroepen staan in de exportgrafiek van de Verenigde Staten in bron 23?",
      "Auto's en onderdelen, fossiele brandstoffen en machineonderdelen",
      ["Koperproducten, fossiele brandstoffen en machineonderdelen",
       "Auto's en onderdelen, koperproducten en bananen uit Zuid-Amerika",
       "Machineonderdelen, koperproducten en vooral textiel en schoenen"],
      "De VS exporteren onder andere auto's en onderdelen, fossiele brandstoffen en machineonderdelen.", 33),
    M("Uit hoeveel landen bestaat het BRICS-verbond inmiddels volgens bron 24?",
      "Uit tien landen",
      ["Uit vijf landen", "Uit zeven landen", "Uit twaalf landen"],
      "Naast de vijf leden van het eerste uur zijn er vijf nieuwe leden bijgekomen, samen tien.", 37),
    M("Waarom wordt Zuid-Afrika steeds meer een concurrent van de VS bij druiventeelt en wijnexport?",
      "Doordat het economische zwaartepunt van de wereld verschuift",
      ["Doordat de VS hun druivenvelden hebben omgezet in industriegebieden",
       "Doordat Zuid-Afrika de invoerrechten op Amerikaanse wijn heeft verhoogd",
       "Doordat Europa geen wijn meer wil invoeren uit Amerika"],
      "Het boek koppelt de concurrentie van Zuid-Afrika aan het verschuiven van het economische zwaartepunt.", 36),
    M("Welk bijzonder kenmerk heeft Zuid-Afrika volgens de atlasopdracht?",
      "Het is het enige land met drie hoofdsteden",
      ["Het is het enige land zonder hoofdstad",
       "Het is het enige land met vier hoofdsteden",
       "Het is het enige land met één hoofdstad aan zee"],
      "Zuid-Afrika is het enige land met drie hoofdsteden.", 36),
    M("Welk land is een nieuw lid van de BRICS volgens bron 24?",
      "Ethiopië",
      ["Mexico", "Turkije", "Zuid-Korea"],
      "Egypte, Ethiopië, Iran, de VAE en Indonesië zijn toegetreden.", 37),
    M("Wat zeggen de Gini-coëfficiënten in de tabel bij bron 23 over beide landen?",
      "De ongelijkheid is in Dem. Rep. Congo (0,45) iets groter dan in de VS (0,40)",
      ["De ongelijkheid is in de VS (0,45) iets groter dan in Dem. Rep. Congo (0,40)",
       "De ongelijkheid is in beide landen precies gelijk, namelijk 0,45",
       "De VS hebben bijna geen ongelijkheid, Dem. Rep. Congo wel"],
      "Dem. Rep. Congo heeft Gini 0,45, de VS 0,40.", 32),
    M("Welk SDG past het best bij een land met een bbp per hoofd van € 1000?",
      "Geen armoede",
      ["Klimaatactie", "Leven in het water", "Partnerschap"],
      "Een laag bbp per hoofd wijst op armoede, dus past SDG 1 'Geen armoede'.", 32),
    W("De VS verdienen het grootste deel van hun exportwaarde aan landbouwproducten.", False,
      "Niet waar. Landbouw is maar 1 procent van de totale exportwaarde.", 34),
    W("De VS zijn volgens de tekst de op één na kleinste landbouwexporteur ter wereld.", False,
      "Niet waar. De VS zijn de grootste landbouwexporteur ter wereld.", 34),
    W("Egypte, Iran en Indonesië behoorden tot de leden van het eerste uur van de BRICS.", False,
      "Niet waar. De leden van het eerste uur waren Brazilië, Rusland, China, India en Zuid-Afrika; de rest is later toegetreden.", 37),
    W("Rob de Wijk stelt dat mensenrechten bij de nieuwe BRICS-leden niet hoog op de agenda staan.", True,
      "Waar. Dat is zijn kritiek in bron 24.", 37),
    W("De Zuid-Afrikaanse druivenplukker plukt druiven waarvan wijn wordt gemaakt die naar Europa wordt geëxporteerd.", True,
      "Waar. Dat staat bij de foto van de druivenplukker.", 35),
    I("De landbouwexport van de Verenigde Staten is meer dan ____ miljard dollar waard.", "200", "Landbouwproducten leveren de VS meer dan 200 miljard dollar op.", 34),
    I("De B van BRICS staat voor ____.", "Brazilië|Brazilie",
      "De B staat voor Brazilië.", 37),
    I("Het BRICS-verbond is in ____ opgericht.", "2009",
      "De BRICS-groep is in 2009 opgericht.", 37),
    I("Zuid-Afrika ligt op de kruising van twee ____.", "oceanen",
      "Zuid-Afrika ligt op de kruising van twee oceanen.", 36),
    O("Welke zorg heeft hoogleraar Rob de Wijk over de uitbreiding van de BRICS en waarom?", ["antiwesters/antiwesterse", "mensenrechten", "dictatoriale/dictatoriaal"], 2,
      "Hij vindt het zorgelijk omdat de nieuwe leden een antiwesterse houding hebben; dictatoriale landen worden belangrijker en mensenrechten staan niet hoog op de agenda.",
      "De nieuwe leden zijn antiwesters en dictatoriaal, mensenrechten krijgen weinig aandacht.", 37),
    O("Leg uit waarom landbouw voor de VS economisch weinig belangrijk is, ook al zijn zij de grootste landbouwexporteur.", ["1 procent/één procent", "auto's/machineonderdelen/fossiele brandstoffen"], 2,
      "Landbouw is maar 1 procent van de totale exportwaarde; de rest komt uit andere export zoals auto's, machineonderdelen en fossiele brandstoffen.",
      "Het is maar 1 procent; de rest zijn auto's en machineonderdelen.", 34)
])
}

def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('ak_h1_2_extra2_seed_111')
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        t = [v["type"] for v in vr]
        assert (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (9, 5, 4, 2), (nr, t)
        assert sum(1 for v in vr if v["type"] == "waaronwaar" and v["antwoord"] is False) >= 2
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {
            "id": f"ex-h3-ak-{nr}",
            "hoofdstuk": 1,
            "paragraaf": "1.3",
            "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
            "titel": f"Toets {nr} — §1.3 {sub}",
            "vak": "Aardrijkskunde · HAVO 3 (H1)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 §1.3) — gegenereerd door tools/gen_aardrijkskunde_h1_3_extra2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
