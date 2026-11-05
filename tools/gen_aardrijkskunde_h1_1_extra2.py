#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.1 Kantelt het economisch wereldbeeld? (extra toetsen 106–110).
Schrijft havo3/aardrijkskunde/js/data/examen_106..110.js (ex-h3-ak-106..110).
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
106: ("Oorzaken van globalisering: vervoer, ICT en handelsregels", "🚢", [
    M("Een Nederlandse kaasboer mag zijn kaas voortaan zonder extra heffing in een buurland verkopen, omdat beide landen een handelsverdrag sloten. Wat is er verdwenen?",
      "Een handelsbelemmering, waardoor handel vrijer wordt",
      ["Een productieketen, waardoor de kaas in meer landen wordt gemaakt",
       "Een lagelonenland, waardoor kaas goedkoper wordt",
       "Een multinational, waardoor de kaas in elk land bekend wordt"],
      "Strenge regels en extra belasting zijn handelsbelemmeringen; als die verdwijnen, wordt handel over de grens makkelijker.", 16),
    M("Waarom noemt het boek de ontwikkelingen in de ICT als oorzaak van globalisering?",
      "Berichten en mailtjes bereiken iedereen met internet binnen een mum van tijd",
      ["Door internet hoeven er geen goederen meer over de wereld vervoerd te worden",
       "Door internet worden handelsbelemmeringen automatisch afgeschaft in alle landen",
       "Dankzij internet kunnen bedrijven overal ter wereld dezelfde lonen betalen"],
      "Met ICT en internet verloopt communicatie tussen bedrijven wereldwijd razendsnel, en dat maakt samenwerken over grote afstanden makkelijk.", 16),
    M("Twee handelsgebieden schaffen onderling steeds meer regels af. Welke situatie ontstaat daardoor?",
      "Vrijhandel tussen die gebieden",
      ["Een nieuwe handelsbelemmering",
       "Een opgesplitste productieketen",
       "Een multipolaire wereldeconomie"],
      "Wanneer er tussen handelsgebieden steeds minder regels zijn en bedrijven wereldwijd kunnen handelen, spreken we van vrijhandel.", 17),
    M("Wat kunnen bedrijven doen wanneer er tussen handelsgebieden steeds minder regels zijn?",
      "Ze kunnen wereldwijd handel drijven",
      ["Ze mogen alleen in eigen land verkopen",
       "Ze moeten extra belasting betalen",
       "Ze moeten buitenlandse fabrieken sluiten"],
      "Met minder regels tussen handelsgebieden kunnen bedrijven wereldwijd handelen.", 17),
    M("Welke van deze ontwikkelingen is geen oorzaak van globalisering volgens §1.1?",
      "Het invoeren van strengere invoerbelasting",
      ["Het goedkoper en sneller worden van het vervoer",
       "Het opheffen van veel handelsbelemmeringen",
       "De vooruitgang in de ICT en het internet"],
      "Vervoer, ICT en het opheffen van handelsbelemmeringen bevorderen globalisering; extra belasting op import werkt juist tegen.", 17),
    M("Een land voert weer extra belasting in op alle buitenlandse goederen. Wat gebeurt er dan met de vrijhandel met dat land?",
      "Die neemt af, want er is weer een handelsbelemmering",
      ["Die neemt toe, want buitenlandse bedrijven worden gelokt",
       "Die blijft gelijk, want belasting heeft geen invloed",
       "Die verdubbelt, want goederen worden daardoor goedkoper"],
      "Extra belasting is een handelsbelemmering en werkt dus tegen vrijhandel en globalisering.", 17),
    M("Wat kon je vroeger verwachten als je een brief per schip naar de andere kant van de wereld stuurde?",
      "Soms pas na jaren een antwoord",
      ["Binnen een dag een antwoord",
       "Altijd binnen een week een antwoord",
       "Zeker binnen enkele maanden een antwoord"],
      "Per zeilschip was je soms langer dan een jaar onderweg, dus een antwoord kon jaren op zich laten wachten.", 16),
    M("Welke uitspraak over vervoer past bij het verhaal van het boek over globalisering?",
      "Vervoer gaat steeds sneller en wordt steeds goedkoper",
      ["Vervoer wordt steeds duurder en gaat ook nog wat sneller",
       "Vervoer gaat steeds langzamer maar wordt veiliger",
       "Vervoer verandert niet, alleen de regels veranderen"],
      "Sneller en goedkoper vervoer is een van de redenen dat gebieden steeds meer met elkaar verbonden raken.", 16),
    M("Waarom breiden veel grote bedrijven hun activiteiten uit naar gebieden over de grens?",
      "Ze zoeken de beste manier om er geld mee te verdienen",
      ["Ze willen vooral het eigen land beschermen tegen import",
       "Ze moeten dit van de overheid doen om te mogen groeien",
       "Ze willen alle handelsbelemmeringen weer invoeren"],
      "Bedrijven gaan op zoek naar de beste manier om geld te verdienen, en dat kan over de grens.", 16),
    W("Door goedkoper vervoer wordt het voor bedrijven aantrekkelijker om activiteiten in het buitenland uit te breiden.", True,
      "Waar. Sneller en goedkoper vervoer maakt het makkelijker en voordeliger om over de grens te werken.", 16),
    W("Vroeger konden bedrijven zonder enige beperking goederen in het buitenland verkopen; handelsbelemmeringen zijn pas recent bedacht.", False,
      "Niet waar. Lange tijd waren er juist strenge regels of extra belasting, waardoor handel over de grens vaak niet mogelijk was.", 16),
    W("Met een goede internetverbinding bereiken mailtjes tegenwoordig vrijwel direct iemand aan de andere kant van de wereld.", True,
      "Waar. De ICT maakt het mogelijk dat berichten binnen een mum van tijd aankomen.", 16),
    W("Een brief naar de andere kant van de wereld leverde per zeilschip meestal binnen enkele dagen een antwoord op.", False,
      "Niet waar. Het zeilschip deed er soms langer dan een jaar over, dus een antwoord kwam pas veel later.", 16),
    W("Het opheffen van handelsbelemmeringen maakt het voor bedrijven moeilijker om wereldwijd te handelen.", False,
      "Niet waar. Zonder handelsbelemmeringen ontstaat vrijhandel en kunnen bedrijven juist makkelijker wereldwijd handelen.", 17),
    I("Strenge regels of extra belasting die handel over de grens tegenhouden, heten ____.", "handelsbelemmeringen|handelsbelemmering",
      "Dat zijn handelsbelemmeringen.", 16),
    I("Tegenwoordig varen grote schepen met goederen binnen een paar ____ van Azië naar Europa.", "weken", "Schepen varen tegenwoordig binnen een paar weken van Azië naar Europa.", 16),
    I("Tegenwoordig vlieg je in ongeveer een ____ naar de andere kant van de wereld.", "dag|etmaal",
      "Je vliegt tegenwoordig in een dag naar de andere kant van de wereld.", 16),
    I("Doordat veel landen zijn gaan ____, kon vrijhandel ontstaan.", "samenwerken|samenwerking",
      "Landen werken samen en dat leidt tot vrijhandel.", 17),
    O("Noem de twee technische ontwikkelingen uit §1.1 die het bedrijven makkelijker maakten hun activiteiten over de grens uit te breiden.", ["vervoer/transport/schepen", "ICT/internet/communicatie"], 2,
      "Het vervoer is sneller en goedkoper geworden, en dankzij ICT en internet bereiken berichten iedereen binnen een mum van tijd.",
      "Vervoer werd sneller en goedkoper en de ICT ontwikkelde zich, waardoor communicatie vlot ging.", 16),
    O("Leg uit waarom het afschaffen van handelsbelemmeringen bijdraagt aan globalisering.", ["vrijhandel/minder regels", "samenwerk/samenwerking/samenwerken", "verbonden/verbinding"], 2,
      "Doordat handelsbelemmeringen zijn opgeheven, gaan landen samenwerken en ontstaat vrijhandel met minder regels, waardoor gebieden steeds meer met elkaar verbonden raken.",
      "Zonder handelsbelemmeringen kunnen landen samenwerken en ontstaat vrijhandel, waardoor gebieden meer verbonden raken.", 17)
]),

107: ("Multinationals, lonen en de productieketen", "🏢", [
    M("Welke bedrijven noemt het boek als bekende voorbeelden van big tech?",
      "Apple, Microsoft, Amazon en Google",
      ["Shell, Philips, Unilever, Heineken",
       "Toyota, Samsung, Volkswagen en Nike",
       "Coca-Cola, McDonald's, Ikea en Adidas"],
      "Big tech-bedrijven zoals Apple, Microsoft, Amazon en Google zijn wereldwijd bekende multinationals.", 17),
    M("Welke reden noemt het boek, naast verkopen via het internet, voor bedrijven om zich in een ander land te vestigen?",
      "De lonen zijn er lager dan in het land waar het bedrijf vandaan komt",
      ["De grenzen zijn in dat land strenger zodat concurrenten buiten blijven",
       "De belasting op ingevoerde goederen is in dat land altijd het hoogst",
       "Het vervoer naar dat land duurt langer dan naar andere landen"],
      "Laat je je producten maken in een land met lage lonen, dan kost het product veel minder.", 17),
    M("Welke landen noemt het boek als voorbeelden van landen waar de lonen laag zijn?",
      "Indonesië, India en Bangladesh",
      ["Zwitserland, Noorwegen en Duitsland",
       "Japan, Taiwan en Zuid-Korea",
       "Brazilië, Saoedi-Arabië en Qatar"],
      "Indonesië, India en Bangladesh zijn voorbeelden van landen met lage lonen.", 17),
    M("Tot welke groep landen rekent het boek China, waar nog steeds veel productielocaties staan?",
      "Een midden-inkomensland",
      ["Een hoge-inkomensland",
       "Een laag-inkomensland",
       "Een zeer arm ontwikkelingsland"],
      "China is een midden-inkomensland waar nog steeds veel productielocaties staan.", 17),
    M("Een telefoon heeft een scherm uit Zuid-Korea, een chip uit Taiwan en wordt in China in elkaar gezet. Welk begrip past hierbij?",
      "Een opgesplitste productieketen",
      ["Een multipolaire wereldeconomie",
       "Een handelsbelemmering",
       "Een big tech-bedrijf"],
      "Verschillende onderdelen van een eindproduct worden in verschillende landen gemaakt: de productieketen is opgesplitst.", 17),
    M("Uit welke landen komen veel grote multinationals volgens het boek?",
      "Uit hoge-inkomenslanden, waar de lonen hoog zijn",
      ["Uit lage-inkomenslanden, waar de lonen laag zijn",
       "Uit landen zonder enige handelsbelemmering",
       "Uit landen met het hoogste aantal inwoners"],
      "Veel grote multinationals komen uit hoge-inkomenslanden; productie daar is duur door de hoge lonen.", 17),
    M("Hoe kunnen big tech-bedrijven hun producten verkopen en toch veel geld verdienen aan hun klanten?",
      "Ze verkopen via het web en vergaren data over hun klanten",
      ["Ze verkopen alleen in fysieke winkels en rekenen hoge tarieven",
       "Ze laten klanten betalen voor ieder bezoek aan de website",
       "Ze krijgen subsidie van de regering voor elke geleverde bestelling"],
      "Via het web verkopen ze producten en verzamelen ze data over klanten, waar ze veel geld mee verdienen.", 17),
    M("Wat zijn Alibaba en Temu volgens het boek?",
      "Chinese multinationals die wereldwijd spullen verkopen",
      ["Amerikaanse big tech-bedrijven die vooral data verzamelen",
       "Europese bedrijven die alleen in eigen land actief zijn",
       "Aziatische overheden die handelsregels bepalen"],
      "Alibaba en Temu zijn Chinese multinationals die wereldwijd verkopen.", 17),
    M("Waarom staan er in China nog steeds veel productielocaties?",
      "Het is een midden-inkomensland waar veel wordt geproduceerd",
      ["Alle onderdelen van een product worden in China gemaakt",
       "Er zijn in China al jaren geen handelsbelemmeringen meer",
       "Westerse landen verbieden productie op eigen bodem sinds kort"],
      "In een midden-inkomensland als China staan nog steeds veel productielocaties.", 17),
    W("Apple en Microsoft worden in het boek genoemd als bekende big tech-bedrijven.", True,
      "Waar. Samen met Amazon en Google zijn dit voorbeelden van big tech.", 17),
    W("Big tech-bedrijven verdienen alleen aan de verkoop van producten; met data van klanten verdienen ze niets.", False,
      "Niet waar. Zij vergaren ook data over klanten en verdienen daar veel geld mee.", 17),
    W("In landen als Indonesië, India en Bangladesh zijn de lonen laag.", True,
      "Waar. Dat maakt productie daar voor multinationals goedkoop.", 17),
    W("Laat je producten maken in landen waar de lonen hoog zijn, dan kost het product veel minder.", False,
      "Niet waar. Hoge lonen maken een product juist duurder; lage lonen maken het goedkoper.", 17),
    W("Alibaba en Temu zijn Amerikaanse big tech-bedrijven.", False,
      "Niet waar. Het zijn Chinese multinationals.", 17),
    I("Meta verdient veel geld met het verkopen van ____ op Facebook, Instagram en WhatsApp.", "advertenties|advertentie|reclame", "Meta verdient zijn geld vooral met advertenties op zijn apps.", 18),
    I("Landen waar de lonen laag zijn, noemen we ____.", "lagelonenlanden|lagelonenland|lage-lonenlanden",
      "Dat zijn lagelonenlanden.", 17),
    I("Veel snijbloemen die op de veiling van Aalsmeer worden verkocht, komen per vliegtuig uit ____.", "Kenia", "De snijbloemen komen per vliegtuig uit Kenia.", 18),
    I("Katoen uit ____ wordt in Turkije tot garen gesponnen, in India geweven en in Bangladesh tot spijkerbroeken genaaid.", "Kazachstan", "Het katoen komt uit Kazachstan.", 18),
    O("Leg uit waarom een multinational uit een rijk land zijn spullen laat maken in een land waar werknemers weinig verdienen.", ["kosten/goedkoper/goedkoop", "lonen/loon", "winst/verdienen/geld"], 2,
      "De kosten zijn veel lager en het product dus goedkoper, omdat de lonen laag zijn; zo is er meer winst te maken.",
      "De lonen zijn laag, dus de kosten zijn minder en het product is goedkoper.", 17),
    O("Beschrijf wat het opsplitsen van een productieketen inhoudt en geef een voorbeeld.", ["onderdelen", "verschillende landen/meerdere landen/andere landen", "eindproduct"], 2,
      "Verschillende onderdelen van een eindproduct worden in verschillende landen gemaakt, bijvoorbeeld katoen dat in meerdere landen tot spijkerbroeken wordt verwerkt.",
      "Onderdelen van het eindproduct worden in verschillende landen gemaakt.", 17)
]),

108: ("Global shift en multipolaire wereldeconomie", "🌏", [
    M("Op een kaart staan China, India, Brazilië en Indonesië als 'nieuwe groeimarkten'. Wat zegt dat over deze landen?",
      "Hun economische invloed in de wereld neemt gestaag toe",
      ["Hun economische invloed in de wereld neemt snel af",
       "Zij voeren geen enkel product meer uit naar het Westen",
       "Zij zijn alleen nog afnemers van producten uit het Westen"],
      "Nieuwe groeimarkten krijgen steeds meer invloed, terwijl oude markten aan invloed verliezen.", 17),
    M("Wie domineerden van oorsprong de wereldhandel?",
      "De westerse landen",
      ["De oliestaten op het Arabische schiereiland",
       "De landen in Zuidoost-Azië",
       "De landen in Oost-Europa"],
      "Van oorsprong waren het met name de westerse landen die de wereldhandel domineerden.", 17),
    M("Singapore is een belangrijke handelspartner van Europese landen. Wat past daarbij?",
      "Het ligt in Azië, waar het economische zwaartepunt naartoe verschuift",
      ["Het ligt in Europa, waar het economische zwaartepunt blijft liggen",
       "Het ligt in Zuid-Amerika, waar de oude markten zich bevinden",
       "Het ligt in Afrika, waar de meeste productielocaties zijn"],
      "Singapore is een Aziatische handelspartner; Azië is het gebied waar het zwaartepunt naartoe verschuift.", 17),
    M("Naast Azië krijgen ook de oliestaten op het Arabische schiereiland, Brazilië en Oost-Europa steeds meer invloed. Wat ontstaat daardoor?",
      "Een multipolaire wereldeconomie, met meerdere centra",
      ["Een wereldeconomie waarin één enkel land alles bepaalt",
       "Een wereldeconomie zonder enige onderlinge handel meer",
       "Een wereldeconomie die weer volledig westers wordt"],
      "Als er wereldwijd meerdere belangrijke economische gebieden zijn, spreken we van een multipolaire wereldeconomie.", 17),
    M("Een Europese winkelier haalt zijn spullen steeds vaker uit Zuid- en Zuidoost-Azië in plaats van uit Europa. Waarvan is dat een voorbeeld?",
      "Van de global shift van goederenproductie naar Azië",
      ["Van het ontstaan van nieuwe handelsbelemmeringen",
       "Van het verdwijnen van de multipolaire wereldeconomie",
       "Van een toename van de westerse dominantie"],
      "De verschuiving van het economische zwaartepunt naar Azië heet de global shift.", 17),
    M("Wat betekent de global shift voor de positie van Europese landen?",
      "Ze verliezen een deel van hun oude invloed als handelsmacht",
      ["Ze krijgen een steeds sterkere dominante positie in de wereld",
       "Ze stoppen volledig met het importeren van goederen uit Azië",
       "Ze worden de belangrijkste productiegebieden van de wereld"],
      "Oude markten, zoals de westerse landen, verliezen aan invloed.", 17),
    M("Waarvan is de sponsoring van het EK voetbal door Visit Qatar volgens de inleiding een voorbeeld?",
      "Van de toenemende invloed van de landen buiten Europa",
      ["Van de afnemende invloed van de oliestaten in de wereld",
       "Van een handelsbelemmering voor het land Qatar zelf",
       "Van het verdwijnen van de global shift in de wereld"],
      "In de inleiding staat dat Visit Qatar hoofdsponsor was van een Europees voetbaltoernooi, wat de groeiende rol van landen buiten Europa laat zien.", 16),
    M("Welke verklaring past bij het verschuiven van het economisch zwaartepunt naar Azië?",
      "Lage lonen en minder handelsbelemmeringen maken productie daar aantrekkelijk",
      ["Hogere belasting op import maakt productie in Azië voor bedrijven aantrekkelijk",
       "Strengere regels voor buitenlandse bedrijven trekken juist veel multinationals aan",
       "Langzamer en duurder vervoer zorgt ervoor dat productie dichtbij blijft"],
      "Multinationals zoeken lage lonen en vrijhandel op; daardoor verplaatst de productie naar Azië.", 17),
    M("Wat laten de twee fasen van verplaatsing van goederenproductie op de kaart oude en nieuwe economische centra zien?",
      "Dat de goederenproductie in twee fasen naar nieuwe centra verplaatste",
      ["Dat de goederenproductie vanuit Azië weer naar Europa is teruggekeerd",
       "Dat de goederenproductie in twee landen tegelijk helemaal is gestopt",
       "Dat de handelsbelemmeringen in twee stappen zijn ingevoerd door landen"],
      "De kaart toont een eerste en tweede fase van verplaatsing van goederenproductie naar nieuwe centra.", 17),
    W("Elektrische auto's en gadgets worden steeds vaker in China geproduceerd.", True,
      "Waar. Dat staat in de inleiding van de paragraaf.", 16),
    W("Brazilië en Oost-Europa verliezen steeds meer invloed in de wereldeconomie.", False,
      "Niet waar. Juist deze gebieden krijgen steeds meer invloed.", 17),
    W("Van oorsprong werd de wereldhandel gedomineerd door Zuid- en Zuidoost-Azië.", False,
      "Niet waar. Van oorsprong waren het met name de westerse landen die de wereldhandel domineerden.", 17),
    W("In de inleiding staat dat flink wat voetballers van Europese competities naar Saudi-Arabië verhuizen.", True,
      "Waar. Dit is een voorbeeld van groeiende invloed van landen buiten Europa.", 16),
    W("Met de global shift verplaatst het economische zwaartepunt van de wereld zich.", True,
      "Waar. Het economische zwaartepunt schuift op naar Azië.", 17),
    I("Belangrijke Aziatische handelspartners van Europese landen zijn Japan, ____, Singapore en Zuid-Korea.", "Taiwan", "Japan, Taiwan, Singapore en Zuid-Korea zijn belangrijke Aziatische handelspartners.", 17),
    I("Naast Qatar staan ook Abu Dhabi en ____ vast op de Formule 1-kalender.", "Bahrein", "Abu Dhabi en Bahrein staan al vast op de kalender.", 17),
    I("Veel Formule 1-races worden van oudsher op Europese circuits gereden, zoals Monaco, Spa en ____.", "Monza", "Namen als Monaco, Spa en Monza horen bij de klassieke Europese circuits.", 17),
    I("Visit Qatar was hoofdsponsor van het EK voetbal in het jaar ____.", "2024",
      "Het ging om het EK voetbal 2024.", 16),
    O("Leg uit wat we de global shift noemen.", ["zwaartepunt/centrum/verschuiving", "Azië/Oost-Azië/Zuid-Azië/Zuidoost-Azië"], 2,
      "De global shift is de verschuiving van het economische zwaartepunt van de westerse landen naar Zuid-, Zuidoost- en Oost-Azië.",
      "Het economisch zwaartepunt verschuift van het Westen naar Azië.", 17),
    O("Noem twee gebieden buiten Azië die steeds meer invloed krijgen en leg uit waarom dit past bij een multipolaire wereld.", ["olie/oliestaten/Arabisch", "Brazilië", "Oost-Europa", "meerdere/verschillende"], 3,
      "De oliestaten op het Arabische schiereiland, Brazilië en Oost-Europa krijgen meer invloed, dus er zijn wereldwijd meerdere belangrijke economische gebieden.",
      "Oliestaten en Brazilië krijgen meer invloed, dus er zijn meerdere economische gebieden.", 17)
]),

109: ("Rode Zee: kwetsbare handelsroutes (bron 10)", "⚓", [
    M("Welke combinatie van producten en herkomstlanden noemt bron 10?",
      "Avocado's uit Kenia, gember uit China en druiven uit India",
      ["Avocado's uit India, gember uit Kenia en druiven uit China",
       "Avocado's uit China, gember uit India en druiven uit Kenia",
       "Avocado's uit Kenia, gember uit India en druiven uit China"],
      "Bron 10 noemt avocado's uit Kenia, gember uit China en druiven uit India.", 20),
    M("Wat dwingt de schepen volgens bron 10 door de aanvallen in de Rode Zee?",
      "Een andere route te varen",
      ["Hun lading te lossen in Egypte",
       "Terug te keren naar Azië",
       "De lading te laten wachten"],
      "Door de aanvallen moeten schepen een andere route varen.", 20),
    M("Wat laat het artikel over de Rode Zee zien over de wereld?",
      "Een conflict in één gebied raakt winkels in andere werelddelen",
      ["Een conflict blijft altijd beperkt tot de directe omgeving",
       "Importeurs kunnen altijd direct overstappen op eigen producten",
       "Een conflict zorgt automatisch voor vrijhandel met nabije landen"],
      "Gebieden zijn met elkaar verbonden: problemen in de Rode Zee treffen Nederlandse importeurs.", 20),
    M("De schepen moeten langer varen door de aanvallen. Welke ontwikkeling uit §1.1 wordt hierdoor tijdelijk tegengewerkt?",
      "Het sneller worden van het vervoer",
      ["Het afschaffen van handelsbelemmeringen",
       "De ontwikkeling van de ICT",
       "Het opsplitsen van productieketens"],
      "Een omweg maakt het vervoer langzamer, terwijl sneller vervoer juist globalisering bevordert.", 20),
    M("Voor de aanvallen voeren 100 containerschepen per week door de Rode Zee. Hoeveel durven er volgens de daling van meer dan 90 procent nog?",
      "Minder dan 10 schepen per week",
      ["Ongeveer 50 schepen per week",
       "Zo'n 25 tot 30 schepen per week",
       "Ongeveer 90 schepen per week"],
      "Een daling van meer dan 90 procent laat minder dan een tiende van de schepen over.", 20),
    M("Een supermarkt krijgt tomaten per vrachtwagen uit Spanje en druiven per schip uit India via de Rode Zee. Welk product loopt dan waarschijnlijk het meeste vertraging op?",
      "De druiven uit India, omdat die via de onveilige zeeroute komen",
      ["De tomaten uit Spanje, omdat die over land worden vervoerd",
       "Beide producten precies evenveel, want de route maakt niets uit",
       "Geen van beide, want verse producten worden nooit vervoerd"],
      "De druiven reizen over zee langs de Rode Zee en moeten omvaren; de tomaten niet.", 20),
    M("Waarom is een actueel nieuwsbericht zoals bron 10 handig om globalisering uit te leggen?",
      "Het toont een actueel voorbeeld van afhankelijke gebieden",
      ["Het bewijst dat globalisering al volledig is gestopt",
       "Het toont dat alle producten in Nederland zelf worden geteeld",
       "Het laat zien dat handelsbelemmeringen weer overal zijn ingevoerd"],
      "Het artikel toont hoe Kenia, China, India en Nederland via de wereldhandel met elkaar verbonden zijn.", 20),
    M("Hoe reageren Nederlandse importeurs volgens bron 10 op de situatie?",
      "Ze worden met de dag nerveuzer",
      ["Ze verhogen direct alle prijzen",
       "Ze stoppen met importeren voor altijd",
       "Ze kopen alleen nog eigen producten"],
      "De importeurs worden met de dag nerveuzer.", 20),
    M("Wat is het effect van de aanvallen op de wereldhandel volgens bron 10?",
      "Een tijdelijke verstoring van de aanvoer van goederen",
      ["Een blijvende stijging van het aantal schepen in de Rode Zee",
       "Een einde aan alle handel met Azië",
       "Een verbetering van de houdbaarheid van producten"],
      "De aanvoer van goederen raakt verstoord doordat schepen omvaren.", 20),
    W("Gember uit China en druiven uit India horen bij de producten die Nederlandse importeurs per schip ontvangen.", True,
      "Waar. Dat noemt bron 10 als voorbeelden.", 20),
    W("Avocado's, gember en druiven groeien vooral in koele omstandigheden.", False,
      "Niet waar. Het zijn plantaardige producten die in warme omstandigheden groeien.", 20),
    W("Het aantal containerschepen dat de Rode Zee aandurft, is met bijna tien procent gedaald.", False,
      "Niet waar. De daling bedraagt meer dan 90 procent.", 20),
    W("Een conflict in de Rode Zee kan gevolgen hebben voor winkels in Nederland, wat past bij globalisering.", True,
      "Waar. Gebieden in de wereld zijn met elkaar verbonden.", 20),
    W("Volgens bron 10 wachten importeurs rustig af, omdat de houdbaarheid van de producten geen enkel risico loopt.", False,
      "Niet waar. De houdbaarheidsdatum komt gevaarlijk dichtbij.", 20),
    I("De aanvallen op schepen in de Rode Zee zijn uitgevoerd door de ____-rebellen.", "Houthi|Houthi's|houthi",
      "Het gaat om Houthi-rebellen.", 20),
    I("Het containerschip dat in maart 2021 zes dagen vastzat in het Suezkanaal, heette de Ever ____.", "Given", "De Ever Given liep vast in het Suezkanaal.", 10),
    I("Bron 10 is vrij naar een nieuwsbericht van de ____ uit januari 2024.", "NOS",
      "Het artikel is vrij naar de NOS.", 20),
    I("Avocado's, gember en druiven zijn ____ producten die groeien in warme omstandigheden.", "plantaardige|plantaardig",
      "Het zijn plantaardige producten.", 20),
    O("Leg uit welk probleem aanvallen op schepen veroorzaken voor Nederlandse importeurs van vers fruit.", ["andere route/omweg/langere route", "houdbaarheid/houdbaar/bederven"], 2,
      "De schepen moeten een andere, langere route varen en daardoor komt de houdbaarheidsdatum van de producten in gevaar.",
      "Schepen moeten een omweg varen en daardoor kan het fruit bederven voordat het aankomt.", 20),
    O("Leg uit waarom Nederlandse importeurs avocado's niet uit eigen land halen, maar uit Kenia.", ["klimaat/warm/warmte/temperatuur", "groeien/kweken/verbouwen/geteeld"], 1,
      "Avocado's groeien in warme omstandigheden, dus het klimaat in Nederland is daarvoor niet geschikt.",
      "Avocado's groeien alleen in warme omstandigheden en het klimaat in Nederland is daarvoor niet geschikt.", 20)
]),

110: ("Vietnam en de kanteling van het wereldbeeld (bron 11)", "🇻🇳", [
    M("Wat veranderde er vanaf 1986 voor buitenlandse investeerders in Vietnam?",
      "Ze waren welkom om te investeren en productie te vestigen",
      ["Ze mochten alleen nog goederen uit Vietnam kopen en doorverkopen",
       "Ze moesten extra belasting betalen op elke investering daar",
       "Ze werden verplicht hun fabrieken in Vietnam te sluiten"],
      "Vanaf 1986 waren multinationals welkom om te investeren en een deel van hun productie in Vietnam te vestigen.", 20),
    M("Welke sector leverde in 1995 meer dan de helft van de Vietnamese exportwaarde?",
      "De primaire sector",
      ["De secundaire sector",
       "De tertiaire sector",
       "De quartaire sector"],
      "In 1995 kwam meer dan 50 procent van de export uit de primaire sector.", 20),
    M("Welke bewering over de Vietnamese export tussen 1995 en 2022 klopt?",
      "De totale exportwaarde groeide met bijna 394 miljard dollar",
      ["De totale exportwaarde groeide met ongeveer 40 miljard dollar",
       "De totale exportwaarde bleef vrijwel gelijk aan 5 miljard dollar",
       "De totale exportwaarde daalde met bijna 394 miljard dollar"],
      "De export steeg van 5,15 naar 399 miljard dollar, een toename van ongeveer 394 miljard.", 21),
    M("Waardoor werd de sterke groei van de handel van Vietnam met het buitenland mogelijk?",
      "Doordat handelsbelemmeringen werden opgeheven en vrijhandel ontstond",
      ["Doordat Vietnam nieuwe handelsbelemmeringen invoerde tegen import",
       "Doordat Vietnam zijn grenzen steeds dicht bleef houden",
       "Doordat alle buitenlandse investeerders zich terugtrokken uit het land"],
      "Veel handelsbelemmeringen werden opgeheven, waardoor vrijhandel mogelijk werd.", 20),
    M("Welk product hoort volgens bron 11 bij de export van Vietnam in 1995?",
      "Vis en zeevruchten",
      ["Elektrische apparaten",
       "Smartphones en laptops",
       "Auto's en machines"],
      "Bron 11 laat voor 1995 onder meer vis en zeevruchten zien.", 21),
    M("Welke conclusie past bij bron 11 samen met de kaart van oude en nieuwe economische centra?",
      "Vietnam ligt in een gebied waar de productie naartoe verschuift",
      ["Vietnam ligt in een gebied waar de productie juist wegtrekt",
       "Vietnam hoort bij de oude markten die steeds meer invloed winnen",
       "Vietnam heeft geen enkel verband met de global shift in Azië"],
      "Vietnam in Zuidoost-Azië past bij de verplaatsing van productie naar Azië.", 21),
    M("Vietnam stelt zich open voor buitenlandse investeerders. Welk proces wordt daardoor versterkt?",
      "Globalisering: Vietnam raakt meer verbonden met andere landen",
      ["Het afsluiten van Vietnam voor de wereldhandel en investeringen",
       "De terugkeer van handelsbelemmeringen in Zuidoost-Azië",
       "Het verdwijnen van alle opgesplitste productieketens in Azië"],
      "Hoe meer gebieden met elkaar verbonden raken, hoe sterker de globalisering.", 20),
    M("Welke sector leverde in 2022 het overgrote deel van de Vietnamese exportwaarde?",
      "De industrie met producten zoals elektrische apparaten",
      ["De primaire sector met producten zoals hout en visserij",
       "De dienstensector met producten zoals toerisme en handel",
       "De landbouw met producten zoals zeevruchten en rijst"],
      "In 2022 kwam het overgrote deel van de export uit industriële producten.", 20),
    M("Wat laat de verandering in de exportproducten van Vietnam zien?",
      "Dat Vietnam is opgeschoven van primaire naar industriële goederen",
      ["Dat Vietnam is teruggevallen op de export van primaire grondstoffen",
       "Dat Vietnam helemaal geen enkel product meer exporteert naar buiten",
       "Dat Vietnam zijn eigen industrie volledig heeft afgeschaft sinds 1995"],
      "Bron 11 toont dat industriële producten in 2022 het grootste deel van de export uitmaken.", 21),
    W("In 1995 had Vietnam een totale exportwaarde van minder dan tien miljard dollar.", True,
      "Waar. De totale waarde was 5,15 miljard dollar.", 21),
    W("De exportwaarde van Vietnam is tussen 1995 en 2022 ruim zeven keer zo groot geworden.", False,
      "Niet waar. De export steeg van 5,15 naar 399 miljard dollar, ruim 75 keer zoveel.", 21),
    W("In 2022 bestond de Vietnamese export vooral uit producten van de primaire sector.", False,
      "Niet waar. In 2022 kwam het overgrote deel uit industriële producten.", 20),
    W("Het opheffen van handelsbelemmeringen heeft bijgedragen aan de groei van de Vietnamese export.", True,
      "Waar. Daardoor werd vrijhandel mogelijk en konden multinationals investeren.", 20),
    W("Vietnam is in het boek een voorbeeld van een land dat meegroeide met de verschuiving van handelspatronen.", True,
      "Waar. Dat is de vraag over Vietnam in de opdrachten.", 21),
    I("De totale exportwaarde van Vietnam bedroeg in 2022 ____ miljard dollar.", "399",
      "In 2022 bedroeg de exportwaarde 399 miljard dollar.", 21),
    I("Lang was Vietnam afgesloten voor buitenlandse ____.", "bedrijven|multinationals", "Vietnam was lang afgesloten voor buitenlandse bedrijven.", 20),
    I("De totale exportwaarde van Vietnam is tussen 1995 en 2022 meer dan ____ keer zo groot geworden.", "75", "399 gedeeld door 5,15 is ongeveer 77, dus meer dan 75 keer zo groot.", 20),
    I("Het totaal van wat Vietnam in 1995 uitvoerde, was ____ miljard dollar waard.", "5,15|5.15", "In 1995 was de totale exportwaarde 5,15 miljard dollar.", 21),
    O("Welke twee veranderingen vanaf 1986 maakten het mogelijk dat de export van Vietnam zo sterk steeg?", ["multinationals/buitenlandse bedrijven", "handelsbelemmeringen/vrijhandel"], 2,
      "Buitenlandse multinationals waren welkom om te investeren en veel handelsbelemmeringen werden opgeheven, waardoor vrijhandel mogelijk werd.",
      "Multinationals mochten investeren en handelsbelemmeringen werden opgeheven.", 20),
    O("Hoe laten bron 11 en de kaart met oude en nieuwe economische centra samen zien in welke richting het wereldbeeld verschuift?", ["global shift", "Azië/Zuidoost-Azië/Oost-Azië", "productie/industrie"], 2,
      "Vietnam in Zuidoost-Azië groeit in industriële productie; dat is de global shift van het economisch zwaartepunt naar Azië.",
      "De global shift: industriële productie verschuift naar Azië, zoals Vietnam laat zien.", 21)
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('ak_h1_1_extra2_seed_106')
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
            "paragraaf": "1.1",
            "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
            "titel": f"Toets {nr} — §1.1 {sub}",
            "vak": "Aardrijkskunde · HAVO 3 (H1)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 §1.1) — gegenereerd door tools/gen_aardrijkskunde_h1_1_extra2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
