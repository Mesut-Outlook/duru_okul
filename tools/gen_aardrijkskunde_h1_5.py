#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.5 Rol van Nederland in de wereldhandel (boek p. 42-49).
Schrijft havo3/aardrijkskunde/js/data/examen_92..96.js (ex-h3-ak-92..96). Alleen proeftoetsen; h1_5.js blijft ongewijzigd.
mc-volgorde willekeurig (geseed), opnieuw geschud tot gate-regels 3/16 kloppen.
Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'aardrijkskunde', 'js', 'data')


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


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


BEGRIPPEN = [
    ("afzetmarkt", "Een gebied waar bedrijven hun goederen en producten verkopen."),
    ("brainport", "Een gebied dat een grote rol speelt in de kenniseconomie, met een hoge dichtheid aan hightechbedrijven, universiteiten en onderzoeksinstituten."),
    ("globaliseringsindex", "Een rangorde van landen naar hoe gericht ze zijn op het buitenland; je leest eraan af hoe sterk een land met het buitenland verbonden is."),
    ("mainport", "Een belangrijke haven of luchthaven voor de internationale handel, zoals de haven van Rotterdam en Schiphol."),
    ("multinational", "Een bedrijf dat in meerdere landen is gevestigd, zoals ASML, DAF en Philips."),
    ("vestigingsplaatsfactor", "Een reden waarom een bedrijf zich op een bepaalde plek vestigt, zoals aanvullende bedrijven, een goed opgeleide beroepsbevolking en nabije afzetmarkten."),
    ("broedplaats", "Een plek van onderzoek en vernieuwing waar bedrijven elkaar aanvullen en ondersteunen, zoals de High Tech Campus in Eindhoven."),
    ("hoogwaardige maakindustrie", "Industrie met vernieuwende (innovatieve) hightechbedrijven, die je veel in de regio Eindhoven vindt."),
    ("Gini-coëfficiënt", "Een getal tussen 0 en 1 dat aangeeft hoe ongelijk een land is; Nederland heeft 0,26, dus een lage sociale ongelijkheid."),
    ("relatieve armoede", "Armoede in een rijk land, waar sommige mensen moeite hebben om bijvoorbeeld de energierekening te betalen."),
    ("open economie", "Een economie die sterk op het buitenland is gericht, waardoor Nederland hoog scoort op de globaliseringsindex."),
    ("doorvoer", "Producten die vanuit de hele wereld de haven van Amsterdam of Rotterdam binnenkomen en daarna naar landen in Europa worden vervoerd."),
    ("sociale ongelijkheid", "Verschillen tussen rijk en arm; als ze groot worden, kunnen ze leiden tot sociale spanningen die de groei van de economie belemmeren."),
    ("importeren", "Producten uit het buitenland invoeren; Nederlandse bedrijven doen dat vanuit de hele wereld."),
    ("exporteren", "Producten naar het buitenland uitvoeren; Nederland doet dat vooral naar de buurlanden."),
]

BR = " (boek p. "
EXAMENS = {
92: ("Begrippen en feiten", "📘", [
    M("Op welke plaats staat Nederland op de wereldranglijst als je kijkt naar het totale bbp?", "Op plek 28", ["Op plek 3", "Op plek 70", "Op plek 132"],
      "Nederland staat qua totale bbp op plek 28 van de wereldranglijst. De 132 en de 70 gaan over het aantal landen dat groter is in oppervlakte en bevolking, en plek 3 is de plaats op de globaliseringsindex." + BR + "42)"),
    M("Hoeveel landen zijn er groter dan Nederland als je kijkt naar de oppervlakte?", "132 landen", ["28 landen", "70 landen", "3 landen"],
      "Er zijn 132 landen groter dan Nederland qua oppervlakte. Meer dan 70 landen hebben een grotere bevolking." + BR + "42)"),
    M("Wat kun je aflezen op de globaliseringsindex?", "Hoe sterk een land verbonden is met het buitenland", ["Hoe hoog het bbp per inwoner van een land is", "Hoeveel multinationals er in een land zijn gevestigd", "Hoe groot de sociale ongelijkheid in een land is"],
      "Op de globaliseringsindex lees je af hoe sterk een land verbonden is met het buitenland." + BR + "42)"),
    M("Met welke twee landen staat Nederland al jaren in de top 3 van de globaliseringsindex?", "Zwitserland en België", ["Duitsland en Frankrijk", "Singapore en Zwitserland", "België en Luxemburg"],
      "Nederland staat samen met Zwitserland en België al jaren in de top 3." + BR + "42)"),
    M("Wat is een mainport?", "Een belangrijke haven of luchthaven voor de internationale handel", ["Een regio met veel hightechbedrijven en universiteiten", "Een gebied waar bedrijven hun producten verkopen", "Een land dat goederen vooral importeert en doorverkoopt"],
      "Rotterdam is een belangrijke haven voor internationale handel en daarmee een echte mainport. Schiphol is dat ook. Een regio met hightechbedrijven is een brainport." + BR + "42)"),
    M("Wat is een brainport?", "Een gebied met veel hightechbedrijven, universiteiten en onderzoeksinstituten", ["Een haven die vooral goederen doorvoert naar het achterland", "Een luchthaven met verbindingen naar alle werelddelen", "Een stad met een groot aantal scholen en universiteiten"],
      "Een brainport is een gebied met een grote rol in de kenniseconomie en een hoge dichtheid aan hightechbedrijven, universiteiten en onderzoeksinstituten." + BR + "42)"),
    M("Welke drie multinationals worden genoemd bij brainport Eindhoven?", "ASML, DAF en Philips", ["ASML, Shell en Unilever", "DAF, Heineken en Philips", "Philips, KLM en ASML"],
      "Bij brainport Eindhoven worden de multinationals ASML, DAF en Philips genoemd." + BR + "42)"),
    M("Wat betekent het woord afzetmarkt?", "Een gebied waar bedrijven hun goederen en producten verkopen", ["Een plek waar bedrijven hun grondstoffen inkopen", "Een gebied waar bedrijven hun nieuwe fabrieken bouwen", "Een beurs waar bedrijven hun aandelen verhandelen"],
      "Een afzetmarkt is een gebied waar bedrijven hun goederen en producten verkopen." + BR + "43)"),
    M("Wat betekent een Gini-coëfficiënt van 0,26 voor Nederland?", "De sociale ongelijkheid is laag", ["De sociale ongelijkheid is hoog", "Een kwart van de mensen leeft in armoede", "De werkloosheid is precies 26 procent"],
      "Met een Gini-coëfficiënt van 0,26 is de sociale ongelijkheid in Nederland laag." + BR + "43)"),
    M("Hoeveel procent van de machines van ASML wordt geëxporteerd?", "95 procent", ["25 procent", "40 procent", "50 procent"],
      "De chipmachines van ASML worden voor 95 procent geëxporteerd." + BR + "43)"),
    W("Luchthaven Schiphol is net als de haven van Rotterdam een mainport.", True,
      "Waar. Het boek noemt Rotterdam een echte mainport en zegt dat Schiphol ook zo'n mainport is." + BR + "42)"),
    W("De haven van Amsterdam is groter dan de haven van Rotterdam.", False,
      "Niet waar. De haven van Amsterdam is kleiner dan die van Rotterdam, maar wel de vierde grootste haven van Europa." + BR + "42)"),
    W("Nederland staat al jaren in de top 3 van de globaliseringsindex.", True,
      "Waar. Nederland staat samen met Zwitserland en België al jaren in de top 3." + BR + "42)"),
    W("Een Gini-coëfficiënt van 0,26 betekent dat de sociale ongelijkheid in Nederland hoog is.", False,
      "Niet waar. Bij 0 is iedereen gelijk. Met 0,26 is de sociale ongelijkheid in Nederland laag." + BR + "43)"),
    W("ASML in Veldhoven is de grootste producent van chipmachines ter wereld.", True,
      "Waar. ASML is de grootste producent van chipmachines ter wereld." + BR + "43)"),
    I("Een gebied waar bedrijven hun goederen en producten verkopen, heet een ____.", "afzetmarkt|afzetmarkten|de afzetmarkt",
      "Dat is een afzetmarkt." + BR + "43)"),
    I("Het getal tussen 0 en 1 dat aangeeft hoe ongelijk een land is, heet de ____-coëfficiënt.", "Gini|gini",
      "De Gini-coëfficiënt geeft de sociale ongelijkheid aan." + BR + "43)"),
    I("Op de ____ kun je aflezen hoe sterk een land verbonden is met het buitenland.", "globaliseringsindex|de globaliseringsindex",
      "De globaliseringsindex is een rangorde van landen naar hoe gericht ze zijn op het buitenland." + BR + "42)"),
    O("Wat is een afzetmarkt? Leg ook uit waarom de regio rond Eindhoven een interessante afzetmarkt heeft.", ["verkop", "40 miljoen", "koopkracht"], 2,
      "Een afzetmarkt is een gebied waar bedrijven hun producten verkopen. Binnen 150 kilometer rond Eindhoven wonen 40 miljoen mensen met een bovengemiddelde koopkracht.",
      "Een gebied waar bedrijven hun producten verkopen. Rond Eindhoven wonen 40 miljoen mensen met veel koopkracht." + BR + "43)"),
    O("Noem drie multinationals die in brainport Eindhoven zijn gevestigd.", ["ASML", "DAF", "Philips"], 3,
      "Genoemd worden ASML, DAF en Philips.",
      "ASML, DAF en Philips." + BR + "42)"),
]),
93: ("Oorzaak en gevolg", "🔗", [
    M("Waarom staat Nederland al jaren in de top 3 van de globaliseringsindex?", "Nederland heeft een open, op het buitenland gerichte economie", ["Nederland is qua oppervlakte een van de grootste landen van Europa", "Nederland heeft qua totaal bbp de hoogste plaats van de wereld", "Nederland heeft de meeste multinationals van alle landen ter wereld"],
      "Dat komt mede doordat Nederland een open en sterk op het buitenland gerichte economie heeft." + BR + "42)"),
    M("Waarom is West-Europa een goede afzetmarkt voor internationale bedrijven?", "Het is dichtbevolkt en de inwoners hebben een hoge koopkracht", ["Het is dunbevolkt en de grond is er erg goedkoop", "Er zijn weinig handelsbelemmeringen met Azië en Afrika", "De bevolking neemt er sterk toe door immigratie"],
      "West-Europa is dichtbevolkt en de inwoners hebben gemiddeld een hoge koopkracht." + BR + "51)"),
    M("Wat is een gevolg van de toenemende armoede in Nederland?", "Steeds meer mensen maken gebruik van de voedselbank", ["Steeds meer mensen verhuizen naar het buitenland", "Steeds minder mensen hebben een baan in de industrie", "Steeds meer mensen werken voor een multinational"],
      "Een van de gevolgen van de toenemende armoede is dat steeds meer mensen gebruikmaken van de voedselbank." + BR + "43)"),
    M("Wat kan het gevolg zijn van ongelijkheid en armoede voor de samenleving?", "Sociale spanningen die de groei van de economie belemmeren", ["Hogere uitgaven aan onderwijs die de groei bevorderen", "Een lagere Gini-coëfficiënt in alle grote steden van het land", "Een grotere afzetmarkt voor goedkope producten uit het buitenland"],
      "Ongelijkheid en armoede kunnen leiden tot sociale spanningen. Dit belemmert de groei van de economie en samenleving." + BR + "43)"),
    M("Waarom zijn Duitsland en België de grootste exportpartners van Nederland?", "Het zijn buurlanden waar Nederland veel naartoe exporteert", ["Het zijn de enige landen die zelf geen grondstoffen hebben", "Het zijn de enige Europese landen met een mainport aan de kust", "Het zijn de landen met de hoogste Gini-coëfficiënt van Europa"],
      "Nederlandse bedrijven exporteren veel, met name naar onze buurlanden." + BR + "42)"),
    M("Hoe kan het dat 16 procent van de Nederlandse export uit fossiele brandstoffen bestaat, terwijl Nederland zelf niet genoeg wint?", "Er worden veel brandstoffen ingevoerd en weer uitgevoerd", ["Nederland koopt ze in het buitenland en slaat ze op", "Nederlandse bedrijven maken ze uit andere grondstoffen", "De brandstoffen worden in Nederland gewonnen en verwerkt"],
      "In de havens worden veel producten ingevoerd, die veelal worden doorgevoerd naar andere landen. Daardoor bestaat een groot deel van de export uit fossiele brandstoffen." + BR + "42)"),
    M("Waarom is de High Tech Campus een broedplaats voor onderzoek en vernieuwing?", "Bedrijven vullen elkaar aan en ondersteunen elkaar", ["Bedrijven concurreren er om dezelfde kennis", "Bedrijven huren er goedkope fabriekshallen", "Bedrijven liggen er vlak bij de haven"],
      "Een gunstige vestigingsplaatsfactor is de aanwezigheid van bedrijven die elkaar aanvullen en ondersteunen. De High Tech Campus is daar een voorbeeld van." + BR + "42)"),
    M("Waarom importeren Duitse bloemenhandelaren snijrozen uit Kenia en Zambia?", "Die landen hebben een ideaal klimaat voor de bloementeelt", ["Daar zijn de invoerrechten op bloemen afgeschaft", "Daar hebben Nederlandse kwekers geen concurrentie", "Daar liggen de grootste vliegvelden van Afrika"],
      "Een belangrijke vestigingsplaatsfactor voor deze landen is het ideale klimaat voor de bloementeelt." + BR + "44)"),
    M("Waarom is Dutch Flower Group een multinational?", "Het bedrijf heeft kantoren in meerdere landen", ["Het bedrijf verkoopt alleen aan het buitenland", "Het bedrijf is eigendom van de overheid", "Het bedrijf importeert alleen uit Afrika"],
      "Dutch Flower Group heeft kantoren in Kenia, de VS en Duitsland en is daarom een multinational." + BR + "44)"),
    M("Wat doet de Nederlandse overheid om armoede en ongelijkheid tegen te gaan?", "Ze investeert in zorg, onderwijs en gelijke kansen", ["Ze verbiedt de export van alle fossiele brandstoffen", "Ze beperkt de import van producten uit lagelonenlanden", "Ze verhoogt de prijzen van producten in winkels"],
      "De overheid investeert in gezondheidszorg, onderwijs en gelijke kansen voor iedereen." + BR + "43)"),
    W("Doordat Nederland een open economie heeft, scoort het hoog op de globaliseringsindex.", True,
      "Waar. Nederland heeft een open en sterk op het buitenland gerichte economie." + BR + "42)"),
    W("Ongelijkheid en armoede bevorderen de groei van de economie en de samenleving.", False,
      "Niet waar. Ongelijkheid en armoede kunnen leiden tot sociale spanningen en belemmeren de groei." + BR + "43)"),
    W("De Nederlandse export van fossiele brandstoffen bestaat vooral uit brandstoffen die in Nederland zelf zijn gewonnen.", False,
      "Niet waar. Nederland haalt zelf niet genoeg fossiele brandstoffen uit de grond; veel wordt ingevoerd en doorgevoerd." + BR + "42)"),
    W("Nederland heeft een hoge welvaart, dus er is in Nederland geen armoede meer.", False,
      "Niet waar. Desondanks blijft er sprake van relatieve armoede." + BR + "43)"),
    W("De haven van Rotterdam is een belangrijke motor in de import en export van producten.", True,
      "Waar. Rotterdam is een belangrijke haven voor de internationale handel." + BR + "42)"),
    I("Veel ingevoerde producten worden vanuit onze havens ____ naar landen binnen Europa.", "doorgevoerd",
      "Vanuit de hele wereld worden producten ingevoerd die veelal worden doorgevoerd naar landen binnen Europa." + BR + "42)"),
    I("Door toenemende armoede maken steeds meer mensen gebruik van de ____.", "voedselbank|voedselbanken|de voedselbank",
      "Een van de gevolgen van toenemende armoede is dat steeds meer mensen naar de voedselbank gaan." + BR + "43)"),
    I("Ongelijkheid en armoede kunnen leiden tot sociale ____.", "spanningen|spanning",
      "Ongelijkheid en armoede kunnen leiden tot sociale spanningen." + BR + "43)"),
    O("Leg uit waarom de regio Eindhoven zo aantrekkelijk is voor hightechbedrijven.", ["aanvullen/ondersteunen/broedplaats", "opgeleid/beroepsbevolking", "40 miljoen/koopkracht"], 2,
      "Bedrijven ondersteunen elkaar, er is een goed opgeleide technische beroepsbevolking en er zijn afzetmarkten met veel koopkracht in de buurt.",
      "Bedrijven vullen elkaar aan en ondersteunen elkaar, er is een goed opgeleide technische beroepsbevolking en er wonen 40 miljoen mensen met veel koopkracht dichtbij." + BR + "42-43)"),
    O("Leg uit hoe ongelijkheid en armoede de economie kunnen schaden en wat de overheid daartegen doet.", ["spanning", "groei", "onderwijs/gezondheidszorg/gelijke kansen"], 2,
      "Ongelijkheid en armoede geven sociale spanningen en belemmeren de groei. De overheid investeert in gezondheidszorg, onderwijs en gelijke kansen.",
      "Er ontstaan sociale spanningen die de groei belemmeren. De overheid investeert in onderwijs, gezondheidszorg en gelijke kansen." + BR + "43)"),
]),
94: ("Bronnen en kaarten", "📊", [
    M("Bron 32 is een cirkeldiagram over de Duitse import van snijrozen in 2020 (in miljoenen). Welk land levert het grootste deel?", "Nederland", ["Kenia", "Zambia", "Ecuador"],
      "In bron 32 heeft Nederland veruit het grootste deel (1042,2 miljoen), daarna Kenia (296,2 miljoen)." + BR + "42)"),
    M("In bron 32 levert Nederland 1042,2 miljoen aan Duitsland en Kenia 296,2 miljoen. Wat is de beste vergelijking?", "Nederland levert ruim drie keer zoveel als Kenia", ["Nederland levert ruim tien keer zoveel als Kenia", "Nederland levert ongeveer twee keer zoveel als Kenia", "Nederland en Kenia leveren ongeveer evenveel"],
      "1042,2 : 296,2 is ongeveer 3,5. Nederland levert dus ruim drie keer zoveel als Kenia." + BR + "42)"),
    M("Bron 34 laat zien naar welke landen Nederland fossiele brandstoffen exporteert. Welk land heeft het grootste aandeel?", "België, met 33,7 procent", ["Duitsland, met 19,4 procent", "Het Verenigd Koninkrijk, met 5,5 procent", "Frankrijk, met 4,1 procent"],
      "België heeft met 33,7 procent het grootste aandeel, daarna Duitsland met 19,4 procent." + BR + "43)"),
    M("In bron 34 gaat 19,4 procent van de export van fossiele brandstoffen naar Duitsland. Welke omschrijving past het best?", "Bijna een vijfde deel", ["Ongeveer de helft", "Ongeveer een tiende deel", "Ruim een derde deel"],
      "19,4 procent is bijna 20 procent, dus bijna een vijfde deel." + BR + "43)"),
    M("In bron 34 gaat 33,7 procent naar België en 19,4 procent naar Duitsland. Hoeveel gaat samen naar deze twee buurlanden?", "Ruim de helft", ["Ongeveer een derde", "Ongeveer een kwart", "Bijna driekwart"],
      "33,7 plus 19,4 is 53,1 procent, dus ruim de helft." + BR + "43)"),
    M("Bron 33 is een kaart met pijlen die de wereldwijde export van chipmachines laten zien. In welke eenheid zijn de getallen weergegeven?", "In miljarden dollars (2017-2020)", ["In miljoenen euro per jaar", "In aantal machines per dag", "In procenten van de wereldhandel"],
      "De pijlen tonen de export van chipmachines in miljarden dollars over de jaren 2017 tot en met 2020." + BR + "43)"),
    M("Op bron 33 gaan vanuit Nederland pijlen naar Azië en de Verenigde Staten. Welk Aziatisch land importeert de meeste chipmachines uit Nederland?", "Taiwan, met 13,1 miljard dollar", ["China, met 4,1 miljard dollar", "Japan, met 11,2 miljard dollar", "Singapore, met 3,8 miljard dollar"],
      "De dikste pijl vanuit Nederland gaat naar Taiwan (13,1 miljard dollar). Daarna volgt China (7,1 miljard dollar)." + BR + "43)"),
    M("De totale Nederlandse export is 627 miljard euro. Volgens bron 34 bestaat 16 procent daarvan uit fossiele brandstoffen. Hoeveel is dat ongeveer?", "Ongeveer 100 miljard euro", ["Ongeveer 10 miljard euro", "Ongeveer 160 miljard euro", "Ongeveer 39 miljard euro"],
      "16 procent van 627 miljard is 0,16 x 627 = 100,3 miljard euro." + BR + "45)"),
    M("Op bron 31 bezoeken twee mensen een bedrijf in Eindhoven. Wie zijn dat?", "De president van Zuid-Korea en koning Willem-Alexander", ["De president van China en koning Willem-Alexander", "De president van Zuid-Korea en de premier van Nederland", "De president van Taiwan en de burgemeester van Eindhoven"],
      "Bron 31 toont de president van Zuid-Korea en koning Willem-Alexander op bezoek bij ASML in Eindhoven." + BR + "42)"),
    M("Wat laat bron 32 zien over de snijrozen in 2020?", "Duitsland importeert de meeste rozen nog steeds uit Nederland", ["Duitsland importeert de meeste rozen uit Kenia", "Duitsland importeert geen rozen meer uit Zambia", "Duitsland importeert evenveel rozen uit alle landen"],
      "Nederland heeft het grootste aandeel in de Duitse import van snijrozen, ondanks dat ook Kenia en Zambia leveren." + BR + "42)"),
    W("In bron 32 levert Kenia meer snijrozen aan Duitsland dan Nederland.", False,
      "Niet waar. Nederland levert 1042,2 miljoen, Kenia 296,2 miljoen." + BR + "42)"),
    W("Volgens bron 34 gaat samen meer dan de helft van de Nederlandse export van fossiele brandstoffen naar België en Duitsland.", True,
      "Waar. 33,7 procent plus 19,4 procent is 53,1 procent." + BR + "43)"),
    W("In bron 34 krijgen de Verenigde Staten een groter deel van de export van fossiele brandstoffen dan Duitsland.", False,
      "Niet waar. De Verenigde Staten krijgen 5 procent, Duitsland 19,4 procent." + BR + "43)"),
    W("De pijlen in bron 33 laten de export van chipmachines in miljarden dollars zien.", True,
      "Waar. Het gaat om de export van chipmachines over de jaren 2017-2020." + BR + "43)"),
    W("In bron 32 levert Nederland meer snijrozen aan Duitsland dan alle andere landen in het diagram samen.", True,
      "Waar. Nederland 1042,2; Kenia, Zambia, Ethiopië, Ecuador en overige landen samen ongeveer 371 (296,2 + 29,8 + 25 + 7,9 + 11,8)." + BR + "42)"),
    I("In bron 34 gaat het grootste deel van de Nederlandse export van fossiele brandstoffen naar ____.", "België|Belgie",
      "Met 33,7 procent heeft België het grootste aandeel." + BR + "43)"),
    I("Bron 32 laat zien welk land de meeste snijrozen levert aan Duitsland: ____.", "Nederland",
      "Nederland levert 1042,2 miljoen snijrozen." + BR + "42)"),
    I("16 procent van een totale export van 627 miljard euro is afgerond ____ miljard euro.", "100|100,3|100,32",
      "0,16 x 627 = 100,32, afgerond 100 miljard euro." + BR + "45)"),
    O("Bron 34 toont dat vooral twee landen fossiele brandstoffen uit Nederland afnemen. Verklaar waarom Duitsland en België de grootste exportpartners zijn.", ["buur", "grens/dichtbij/nabij"], 1,
      "Het zijn buurlanden die dichtbij liggen, dus vervoer is gemakkelijk.",
      "Het zijn buurlanden van Nederland: ze liggen dichtbij, dus de producten zijn gemakkelijk te vervoeren." + BR + "42)"),
    O("Nederland haalt zelf niet genoeg fossiele brandstoffen uit de grond, maar 16 procent van de export bestaat er wel uit. Hoe kan dat?", ["haven/Rotterdam", "import/invoer/ingevoerd", "doorvo/doorgevoer"], 2,
      "Brandstoffen worden in de havens ingevoerd en daarna doorgevoerd naar andere landen, zodat ze toch in de export tellen.",
      "Via de haven van Rotterdam worden veel brandstoffen ingevoerd (import) en doorgevoerd naar landen binnen Europa." + BR + "45)"),
]),
95: ("Toepassen", "🧩", [
    M("Een Aziatisch bedrijf zoekt een plek in Nederland voor een vestiging naast andere hightechbedrijven. Welke regio ligt het meest voor de hand?", "Brainport Eindhoven", ["De haven van Rotterdam", "De regio rond Schiphol", "De haven van Amsterdam"],
      "In de regio Eindhoven vind je veel innovatieve hightechbedrijven. Rotterdam en Schiphol zijn mainports voor handel en vervoer." + BR + "42)"),
    M("Een nieuw hightechbedrijf zoekt een vestigingsplaats. Welke combinatie past bij de kracht van brainport Eindhoven?", "Bedrijven die elkaar aanvullen en een goed opgeleide beroepsbevolking", ["Veel goedkope grond en een laag opgeleide beroepsbevolking", "Een grote haven en veel grondstoffen in de bodem", "Weinig concurrenten en geen universiteit in de buurt"],
      "Gunstige vestigingsplaatsfactoren zijn bedrijven die elkaar aanvullen, een goed opgeleide technische beroepsbevolking en nabije afzetmarkten." + BR + "42)"),
    M("Welk land scoort waarschijnlijk het laagst op de globaliseringsindex?", "Een land dat bijna niet handelt met het buitenland", ["Een land met veel multinationals", "Een land met een grote haven", "Een land dat veel exporteert naar buurlanden"],
      "De index laat zien hoe gericht een land is op het buitenland. Een land dat nauwelijks handelt, scoort laag." + BR + "42)"),
    M("De Gini-coëfficiënt van een land stijgt van 0,26 naar 0,40. Wat betekent dat?", "De sociale ongelijkheid in het land is groter geworden", ["De sociale ongelijkheid in het land is kleiner geworden", "Het bbp van het land is met 40 procent gestegen", "De werkloosheid in het land is met 14 procent gedaald"],
      "Bij 0 is iedereen gelijk, bij 1 heeft een persoon alle welvaart. Een hoger getal betekent dus meer ongelijkheid." + BR + "43)"),
    M("Een gezin in een grote stad kan de energierekening niet betalen, terwijl Nederland welvarend is. Welk begrip past daarbij?", "Relatieve armoede", ["Een open economie", "Een brainport", "Doorvoer"],
      "Ondanks de hoge welvaart blijft er in Nederland sprake van relatieve armoede." + BR + "43)"),
    M("Een politicus wil veel handelsbelemmeringen invoeren. Waarom is dat vooral nadelig voor Nederland?", "Nederland verdient veel aan handel met het buitenland", ["Nederland heeft zelf genoeg grondstoffen en bedrijven", "Nederland heeft een lage Gini-coëfficiënt nodig", "Nederland heeft geen afzetmarkt in de buurlanden"],
      "Nederland heeft een open, op het buitenland gerichte economie en is gebaat bij open wereldhandel." + BR + "42)"),
    M("Een fabrikant van machines zoekt een vestiging dicht bij veel kopers. Welk argument over Eindhoven past het best?", "Binnen 150 kilometer wonen 40 miljoen mensen met veel koopkracht", ["Binnen 15 kilometer wonen 40 miljoen mensen met veel koopkracht", "Binnen 150 kilometer wonen 4 miljoen mensen met weinig koopkracht", "Binnen 500 kilometer wonen 40 miljoen mensen zonder koopkracht"],
      "In een straal van 150 kilometer rond Eindhoven wonen 40 miljoen mensen met een bovengemiddeld hoge koopkracht." + BR + "43)"),
    M("De gemeente wil armoede verminderen. Welk beleid sluit aan bij wat het boek noemt?", "Investeren in onderwijs en gelijke kansen", ["De uitkeringen verlagen en de voedselbank sluiten", "De export van fossiele brandstoffen verhogen", "De haven van Rotterdam uitbreiden met een tweede terminal"],
      "De overheid investeert in gezondheidszorg, onderwijs en gelijke kansen voor iedereen." + BR + "43)"),
    M("Een schip uit Azië komt aan in Rotterdam en de lading gaat direct door naar Duitsland. Welk begrip uit de paragraaf past daarbij?", "Doorvoer naar landen binnen Europa", ["Export van een Nederlands product", "Een afzetmarkt voor Nederlandse bedrijven", "Relatieve armoede in de haven"],
      "In de havens worden producten ingevoerd die veelal doorgevoerd worden naar landen binnen Europa." + BR + "42)"),
    M("Wat wordt Eindhoven weleens genoemd?", "De slimste regio in de wereld", ["De grootste haven van Europa", "De drukste luchthaven van de wereld", "De rijkste stad van Europa"],
      "Eindhoven wordt weleens de slimste regio in de wereld genoemd." + BR + "42)"),
    W("Een bedrijf met kantoren in meerdere landen, zoals Dutch Flower Group, is een multinational.", True,
      "Waar. Dutch Flower Group heeft kantoren in Kenia, de VS en Duitsland." + BR + "44)"),
    W("Een bedrijf dat 95 procent van zijn machines exporteert, is sterk afhankelijk van buitenlandse afzetmarkten.", True,
      "Waar. ASML exporteert 95 procent van zijn chipmachines, dus de buitenlandse afnemers zijn heel belangrijk." + BR + "43)"),
    W("Een land met een Gini-coëfficiënt van 0,9 heeft een lage sociale ongelijkheid.", False,
      "Niet waar. Hoe dichter bij 1, hoe groter de ongelijkheid. Bij 0,9 is de ongelijkheid hoog." + BR + "43)"),
    W("Nederland profiteert van een wereld waarin alle landen hun grenzen sluiten voor buitenlandse handel.", False,
      "Niet waar. Nederland is juist gebaat bij een open wereldeconomie." + BR + "42)"),
    W("In de grote steden worden de verschillen tussen de rijkste en armste wijken steeds groter.", True,
      "Waar. Met name in de grote steden zijn er steeds grotere verschillen tussen de rijkste en armste wijken." + BR + "43)"),
    I("Een bedrijf dat in meerdere landen is gevestigd, noem je een ____.", "multinational|multinationals|de multinational",
      "Multinationals als ASML, DAF en Philips zijn in Nederland gevestigd." + BR + "42)"),
    I("Nederland is gebaat bij een open ____.", "wereldeconomie|economie",
      "Nederland heeft een open en sterk op het buitenland gerichte economie." + BR + "42)"),
    I("Bij een Gini-coëfficiënt van 0 is iedereen ____.", "gelijk|hetzelfde",
      "Bij 0 is iedereen gelijk, bij 1 heeft één iemand alle welvaart." + BR + "43)"),
    O("Een Amerikaans bedrijf overweegt zich in Nederland te vestigen. Welke twee argumenten kun je geven om voor de regio Eindhoven te kiezen?", ["opgeleid/beroepsbevolking", "koopkracht/40 miljoen", "aanvullen/ondersteunen/broedplaats"], 2,
      "Er is een goed opgeleide technische beroepsbevolking, bedrijven ondersteunen elkaar en er wonen 40 miljoen mensen met veel koopkracht dichtbij.",
      "Er is een goed opgeleide technische beroepsbevolking en dichtbij wonen 40 miljoen mensen met veel koopkracht; bedrijven ondersteunen elkaar." + BR + "42-43)"),
    O("Niet iedereen in Nederland profiteert van de rol in de wereldhandel. Leg dit uit met een voorbeeld.", ["ongelijk/verschil", "armoede/voedselbank/energierekening"], 2,
      "Hoewel Nederland welvarend is, blijft er armoede en nemen de verschillen toe. Sommigen kunnen de energierekening niet betalen.",
      "Er blijft armoede en de ongelijkheid groeit: sommige mensen kunnen hun energierekening niet betalen en gaan naar de voedselbank." + BR + "43)"),
]),
96: ("Eindniveau", "🏆", [
    M("Welke combinatie van feiten laat zien dat Nederland een klein land is met een grote rol in de wereldhandel?", "Veel landen zijn groter, maar Nederland staat 28e op bbp en in de top 3 van de globaliseringsindex", ["Veel landen zijn kleiner en Nederland staat 28e op bbp en in de top 3 van de globaliseringsindex", "Veel landen zijn groter en Nederland staat 3e op bbp en 28e op de globaliseringsindex", "Veel landen zijn groter en Nederland staat 28e op bbp maar niet in de top 3 van de globaliseringsindex"],
      "Er zijn 132 landen groter qua oppervlakte, maar Nederland staat 28e op bbp en al jaren in de top 3 van de globaliseringsindex." + BR + "42)"),
    M("Wat is het verschil tussen een mainport en een brainport?", "Een mainport is een haven of luchthaven voor handel, een brainport is een regio met kenniseconomie", ["Een mainport is een regio met kenniseconomie, een brainport is een haven of luchthaven", "Een mainport ligt in Nederland, een brainport ligt altijd in het buitenland", "Een mainport is een grote haven, een brainport is een kleine haven"],
      "Rotterdam en Schiphol zijn mainports voor internationale handel. Eindhoven is een brainport met veel hightechbedrijven en kennis." + BR + "42)"),
    M("Welke bewering over Nederland klopt?", "De ongelijkheid is laag, maar er is wel relatieve armoede", ["De sociale ongelijkheid is hoog en er is geen armoede", "De sociale ongelijkheid is laag en er is geen enkele armoede", "De sociale ongelijkheid is hoog doordat het inkomen daalt"],
      "De Gini-coëfficiënt is 0,26 (lage ongelijkheid), desondanks blijft er sprake van relatieve armoede." + BR + "43)"),
    M("Welke drie vestigingsplaatsfactoren noemt het boek voor brainport Eindhoven?", "Bedrijven die elkaar aanvullen, een goed opgeleide beroepsbevolking en nabije afzetmarkten", ["Goedkope grond, lage belastingen en veel grondstoffen in de regio", "Een grote haven, een eigen luchthaven en een snelle spoorlijn naar Duitsland", "Een gunstig klimaat, goedkope arbeid en weinig regels voor bedrijven"],
      "Het gaat om aanvullende bedrijven, een goed opgeleide (technische) beroepsbevolking en de nabijheid van interessante afzetmarkten." + BR + "42-43)"),
    M("ASML maakt 400 chipmachines. Hoeveel daarvan gaan volgens het boek naar het buitenland?", "380 machines", ["200 machines", "300 machines", "395 machines"],
      "95 procent van 400 is 0,95 x 400 = 380 machines." + BR + "43)"),
    M("Waarom is het riskant voor Nederland als veel landen handelsbelemmeringen invoeren?", "Nederland leeft van import, export en doorvoer via zijn havens", ["Nederland verliest dan zijn eigen grondstoffen aan het buitenland", "Nederland krijgt dan een hogere Gini-coëfficiënt", "Nederland moet dan minder exporteren naar Azië dan naar Afrika"],
      "Nederland heeft een open economie met een grote rol in import, export en doorvoer en is dus gebaat bij open handel." + BR + "42)"),
    M("Dutch Flower Group importeert rozen uit Kenia en exporteert ze naar Duitsland. Wat laat dit zien?", "Nederlandse bedrijven verdienen ook als schakel tussen andere landen", ["Nederlandse bedrijven kweken alle rozen zelf in Kenia", "Nederlandse bedrijven krijgen steeds minder werk in de handel", "Nederlandse bedrijven mogen geen producten uit Kenia invoeren"],
      "Het bedrijf voert in en weer uit en is zo een schakel in de wereldhandel, met kantoren in Kenia, de VS en Duitsland." + BR + "44)"),
    M("Wat is de belangrijkste conclusie als de ongelijkheid in grote steden verder toeneemt?", "Er ontstaan spanningen die de groei kunnen belemmeren", ["Er ontstaan meer multinationals die de groei bevorderen", "Er ontstaat een grotere afzetmarkt die de groei bevordert", "Er ontstaat meer export die de ongelijkheid verkleint"],
      "Ongelijkheid en armoede kunnen leiden tot sociale spanningen en dat belemmert de groei van de economie." + BR + "43)"),
    M("Waarom wordt de haven van Rotterdam een echte mainport genoemd?", "Het is een belangrijke haven voor de internationale handel en de grootste van Europa", ["Het is een belangrijke haven voor de visserij en de grootste van Europa", "Het is een belangrijke haven voor de internationale handel en de kleinste van Europa", "Het is een belangrijke haven voor passagiers en de grootste van Azië"],
      "Rotterdam is de grootste haven van Europa en een belangrijke haven voor de internationale handel; daarmee is het een echte mainport." + BR + "42)"),
    M("Welke omschrijving past bij een open economie zoals die van Nederland?", "Een economie die sterk op het buitenland is gericht", ["Een economie die vooral voor de eigen bevolking produceert", "Een economie die geen handelsbelemmeringen kent", "Een economie waarin de overheid alle bedrijven bezit"],
      "Nederland heeft een open en sterk op het buitenland gerichte economie. Daardoor scoort het hoog op de globaliseringsindex." + BR + "42)"),
    W("Nederland staat samen met Zwitserland en Duitsland in de top 3 van de globaliseringsindex.", False,
      "Niet waar. Het zijn Zwitserland en België." + BR + "42)"),
    W("ASML exporteert bijna al zijn chipmachines.", True,
      "Waar. ASML exporteert 95 procent van zijn machines." + BR + "43)"),
    W("In heel Nederland worden de verschillen tussen rijk en arm kleiner.", False,
      "Niet waar. De sociale ongelijkheid is redelijk stabiel, maar in veel plaatsen gegroeid." + BR + "43)"),
    W("Nederland heeft een lage werkloosheid en een stijgend gemiddeld besteedbaar inkomen.", True,
      "Waar. Dat zegt het boek over Nederland op weg naar 2030." + BR + "43)"),
    W("Een afzetmarkt is een gebied waar bedrijven hun grondstoffen inkopen.", False,
      "Niet waar. Een afzetmarkt is een gebied waar bedrijven hun goederen en producten verkopen." + BR + "43)"),
    I("ASML is wereldwijd de grootste producent van ____.", "chipmachines|chipmachine",
      "ASML in Veldhoven is de grootste producent van chipmachines ter wereld." + BR + "43)"),
    I("In een straal van ____ kilometer rond Eindhoven wonen 40 miljoen mensen met een hoge koopkracht.", "150|honderdvijftig",
      "Binnen 150 kilometer rond Eindhoven wonen 40 miljoen mensen." + BR + "43)"),
    I("De haven van ____ is kleiner dan die van Rotterdam, maar wel de vierde grootste haven van Europa.", "Amsterdam",
      "De haven van Amsterdam is de vierde grootste haven van Europa." + BR + "42)"),
    O("Nederland is een klein land maar speelt een grote rol in de wereldhandel. Geef twee verklaringen uit de paragraaf.", ["haven/Rotterdam/Schiphol/mainport", "Eindhoven/ASML/hightech/brainport", "multinational", "open"], 2,
      "Nederland heeft mainports als Rotterdam en Schiphol, hightechbedrijven in brainport Eindhoven, veel multinationals en een open economie.",
      "Nederland heeft mainports zoals de haven van Rotterdam en Schiphol, hightech in Eindhoven, en een open economie." + BR + "42)"),
    O("Beoordeel de stelling: Nederland profiteert van de wereldhandel, dus iedereen in Nederland heeft er evenveel voordeel van.", ["armoede/ongelijk", "voedselbank/energierekening", "grote steden/wijken"], 2,
      "De stelling klopt niet. Er is armoede en ongelijkheid; in grote steden zijn de verschillen tussen wijken groot en sommigen gebruiken de voedselbank.",
      "Niet iedereen profiteert: er is armoede en ongelijkheid, vooral in grote steden, waar mensen naar de voedselbank gaan." + BR + "43)"),
]),
}


def main():
    rng = random.Random('ak_h1_5')
    assert 8 <= len(BEGRIPPEN) <= 18, len(BEGRIPPEN)
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        t = [v["type"] for v in vr]
        assert (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (10, 5, 3, 2), (nr, t)
        assert sum(1 for v in vr if v["type"] == "waaronwaar" and not v["antwoord"]) >= 2, nr
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {"id": f"ex-h3-ak-{nr}", "hoofdstuk": 1, "paragraaf": "1.5",
              "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
              "titel": f"Proeftoets {nr} — §1.5 {sub}", "vak": "Aardrijkskunde · HAVO 3 (H1)",
              "icoon": icoon, "duurMin": 20, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 §1.5) — gegenereerd door tools/gen_aardrijkskunde_h1_5.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
