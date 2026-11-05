#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.2 Wereldhandel: van kolonialisme tot nu (extra toetsen 111–115).
Schrijft havo3/aardrijkskunde/js/data/examen_111..115.js (ex-h3-ak-111..115).
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
111: ("Kolonialisme en handelskolonies", "🚢", [
    M("Wat moesten de overzeese gebieden volgens het boek verplicht leveren aan hun kolonisator?",
      "Grondstoffen en handelswaar zoals thee, koffie, tabak, suiker en specerijen",
      ["Afgewerkte machines en elektronica voor de zware industrie in de Europese steden",
       "Jaarlijkse belastinggelden en soldaten voor het leger van het moederland",
       "Scholen en ziekenhuizen voor de Europese kolonisten in de steden"],
      "Kolonies werden verplicht grondstoffen te leveren, zoals thee, koffie, tabak, suiker en specerijen.", 22),
    M("Rond het jaar 1900 haalden Europese landen nog altijd grondstoffen uit hun kolonies. Wat zegt dit over het handelskolonialisme?",
      "Het duurde van de 16e eeuw tot ver in de 20e eeuw, dus 1900 valt er nog binnen",
      ["Het was toen al voorbij, want het eindigde in de loop van de 18e eeuw",
       "Het begon pas in de 20e eeuw, dus rond 1900 bestond er nog geen enkele kolonie",
       "Het gold alleen voor Zuid-Amerika en was rond het jaar 1600 afgelopen"],
      "Het handelskolonialisme duurde van de 16e eeuw tot ver in de 20e eeuw.", 22),
    M("Wat laat de richting van de handelsroutes op bron 12 zien over het doel van de kolonies in Zuid-Amerika?",
      "Goederen gingen vooral van de kolonies naar Portugal, Spanje en Nederland: de kolonies dienden de kolonisator",
      ["Goederen gingen vooral van Europa naar de kolonies om de bewoners te voorzien van Europese producten en voedsel",
       "De routes lopen tussen alle kolonies onderling, waardoor ze zelfstandig handel dreven zonder Europa",
       "Alle routes eindigen in Noord-Amerika, waar de Europese handelaren hun grootste markt hadden gevonden"],
      "Op bron 12 lopen de routes naar Portugal, Spanje en Nederland: de kolonies leverden vooral handelswaar aan de kolonisator.", 23),
    M("Welke drie West-Europese landen worden in de tekst genoemd als landen die zoveel mogelijk gebieden overzee in hun macht probeerden te krijgen?",
      "Nederland, het Verenigd Koninkrijk en Frankrijk",
      ["Duitsland, Zweden en Polen",
       "Rusland, Italië en Oostenrijk",
       "Noorwegen, Denemarken en Finland"],
      "Vooral Nederland, het Verenigd Koninkrijk en Frankrijk probeerden gebieden overzee in hun macht te krijgen.", 22),
    M("Wat deed de VOC volgens de inleiding van de paragraaf in Azië?",
      "Ze veroverde gebieden en zette van daaruit lucratieve handelsroutes op",
      ["Ze bouwde scholen en leidde de inwoners op voor de handel in Europa",
       "Ze gebruikte alleen bestaande Aziatische routes zonder iets te veroveren",
       "Ze richtte kolonies op om er zilver te winnen voor de Spaanse kroon"],
      "De VOC veroverde gebieden in Azië en zette vanuit die gebieden handelsroutes op.", 22),
    M("Een leerling zegt: 'In de kolonies werd iedereen als gelijke van de Europeanen behandeld.' Wat is er volgens het boek mis met deze uitspraak?",
      "De bevolking werd overheerst en in veel gevallen niet als gelijke behandeld",
      ["Alleen in Azië werd de bevolking overheerst, in Zuid-Amerika niet",
       "De bevolking koos de Europese bestuurders zelf bij verkiezingen",
       "Alleen de rijke bovenlaag moest werken, de rest van de bevolking was volledig vrij om te gaan en staan waar men wilde"],
      "De bevolking werd overheerst en vaak niet als gelijke van de Europeanen behandeld.", 22),
    M("Wat is volgens de tekst vaak de positie van landen die vroeger zelf kolonies bezaten?",
      "Hoge-inkomenslanden met veel multinationals en een grote rol in de wereldhandel",
      ["Lage-inkomenslanden zonder multinationals en met een kleine rol in de wereldhandel",
       "Landen die hun welvaart volledig aan de eigen bodemschatten te danken hebben",
       "Landen die sinds het einde van het koloniale tijdperk geen handel meer drijven"],
      "Veel voormalige kolonisatoren zijn nog steeds hoge-inkomenslanden met een grote rol in de wereldhandel.", 22),
    M("Welke goederen werden volgens de tekst NIET als voorbeeld van koloniale handelswaar genoemd?",
      "Smartphones, computerchips en chipmachines",
      ["Thee, koffie en tabak",
       "Suiker, thee en specerijen",
       "Koffie, tabak en suiker"],
      "Voorbeelden van koloniale handelswaar zijn thee, koffie, tabak, suiker en specerijen; elektronica en chips horen bij de huidige wereldhandel.", 22),
    M("Wat betekent de legenda 'geen Europese invloed' op bron 12?",
      "Gebieden, vooral in het binnenland, waar geen Europese kolonie was gevestigd",
      ["Gebieden die als eerste onafhankelijk werden van hun Europese kolonisator in Zuid-Amerika",
       "Gebieden die alleen handel dreven met hun buurlanden in Afrika",
       "Gebieden waar uitsluitend Spaanse handelsposten waren gebouwd"],
      "Op bron 12 is te zien dat het binnenland lange tijd buiten de Europese koloniën bleef.", 23),
    W("Het gebruik van kolonies als leverancier van grondstoffen begon pas na 1900.", False,
      "Niet waar. Het handelskolonialisme duurde van de 16e eeuw tot ver in de 20e eeuw.", 22),
    W("Thee, koffie, tabak en suiker waren voorbeelden van producten uit de kolonies.", True,
      "Waar. Dit worden als voorbeelden genoemd, samen met allerlei specerijen.", 22),
    W("De winst van het handelskolonialisme kwam grotendeels terecht bij de bevolking van de kolonies.", False,
      "Niet waar. De kolonisatoren verdienden veel geld, de bevolking werd overheerst.", 22),
    W("Op bron 12 lopen handelsroutes naar drie Europese landen: Portugal, Spanje en Nederland.", True,
      "Waar. De legenda noemt precies deze drie bestemmingen.", 23),
    W("Voormalige kolonisatoren zoals Nederland hebben tegenwoordig een kleine rol in de wereldhandel.", False,
      "Niet waar. Veel van deze landen zijn nog steeds hoge-inkomenslanden met een grote rol.", 22),
    I("Een overzees gebied dat verplicht grondstoffen moest leveren aan een West-Europees land noem je een ____.", "kolonie|kolonien|koloniën",
      "Dit gebied is een kolonie.", 22),
    I("Het binnenland van Zuid-Amerika werd lange tijd niet gekoloniseerd, omdat dit deel moeilijk ____ was.", "bereikbaar", "Het binnenland was moeilijk bereikbaar.", 22),
    I("Al ____ jaren proberen landen invloed uit te oefenen tot ver over hun eigen landsgrenzen heen.", "honderden", "Landen proberen al honderden jaren invloed uit te oefenen over hun grenzen heen.", 22),
    I("Nederland ziet de periode van de VOC terug als een zwarte ____ in de geschiedenis.", "bladzijde|bladzij|pagina",
      "Het boek spreekt van een zwarte bladzijde.", 22),
    O("Leg uit hoe kolonisatoren aan hun overzeese gebieden veel geld verdienden.", ["grondstoffen/handelswaar", "onderdruk/overheers/uitbuit"], 2,
      "Zij dwongen de gebieden om grondstoffen zoals thee, koffie en suiker te leveren en overheersden en onderdrukten de bevolking.",
      "Het geld kwam uit verplichte grondstoffen en uit het onderdrukken van de bevolking.", 22),
    O("Vergelijk de huidige positie in de wereldeconomie van een voormalige kolonisator en van een voormalige handelskolonie.", ["multinational/hoge-inkomen/grote rol", "achter/laag"], 2,
      "Een voormalige kolonisator is vaak een hoge-inkomensland met multinationals, terwijl de welvaart in veel voormalige handelskolonies nog achterblijft.",
      "Voormalige kolonisatoren hebben een grote rol, in veel voormalige kolonies blijft de welvaart achter.", 22)
]),

112: ("Dekolonisatie en de nasleep", "🏳️", [
    M("Welke ontwikkeling zorgde ervoor dat het koloniale systeem vanaf het midden van de 20e eeuw onder druk kwam te staan?",
      "Toenemende internationale kritiek op het uitbuiten van kolonies",
      ["Een tekort aan schepen waardoor handel over zee onmogelijk werd",
       "De uitputting van alle grondstoffen in de overzeese gebieden",
       "Een verbod van de Verenigde Staten op alle handel met Europa"],
      "Vooral na 1945 zwol de internationale kritiek op het uitbuiten van kolonies aan.", 22),
    M("Wat veranderde er voor het bestuur van een gebied door de dekolonisatie?",
      "Het kreeg een eigen bestuur in plaats van bestuur door de kolonisator",
      ["Het kreeg een bestuur gekozen door de Europese Unie",
       "Het bleef bestuurd worden vanuit het moederland maar kreeg meer rechten",
       "Het kreeg een gezamenlijk bestuur van alle voormalige kolonies"],
      "Kolonies werden een eigen staat met een eigen bestuur.", 22),
    M("Een voormalige kolonie wordt onafhankelijk. Wat gebeurde er volgens het boek vaak met de handel met het oude moederland?",
      "Het moederland bleef veelal de belangrijkste handelspartner",
      ["De handel stopte meestal direct en volledig na de onafhankelijkheid",
       "De handel verschoof meteen helemaal naar de Verenigde Staten",
       "De handel werd verplicht door de Verenigde Naties geregeld"],
      "De banden werden niet altijd doorgesneden; het moederland was veelal nog de belangrijkste handelspartner.", 22),
    M("Sem zegt: 'Dankzij Nederland konden Suriname en Indonesië zich ontwikkelen.' Welk tegenargument past bij de tekst?",
      "De kolonies moesten grondstoffen leveren en de bevolking werd overheerst, dus vooral de kolonisator verdiende",
      ["Suriname en Indonesië zijn nooit een kolonie van een West-Europees land geweest",
       "Alleen de grondstoffen gingen naar Nederland, de winst bleef in de kolonies",
       "Nederland gaf beide gebieden rond 1900 vrijwillig onafhankelijkheid"],
      "Kolonies moesten grondstoffen leveren, de bevolking werd overheerst en de kolonisator verdiende het geld.", 24),
    M("Welk conflict speelde zich af in dezelfde tijd als de dekolonisatie, tussen westerse landen en landen rond de Sovjet-Unie?",
      "De Koude Oorlog",
      ["De chipoorlog",
       "De Tachtigjarige Oorlog",
       "De graanoorlog"],
      "De periode 1945-1990 was ook de periode van de Koude Oorlog.", 25),
    M("Een land was vroeger een groot koloniaal rijk. Een ander land was vroeger zijn kolonie en blijft qua welvaart achter. Wat laat dit zien?",
      "Het koloniale verleden heeft grote invloed op de huidige positie in de wereldeconomie",
      ["Het verleden speelt geen rol, alleen het aantal inwoners telt",
       "Alleen de ligging aan zee bepaalt de positie in de wereldeconomie",
       "De positie wordt uitsluitend bepaald door het klimaat van een land"],
      "Het koloniale verleden heeft nog grote invloed op de positie van landen in de wereldeconomie.", 22),
    M("Op kaarten uit 1937 en 1989 zie je dat veel koloniën zijn veranderd in zelfstandige landen. Welk begrip hoort bij deze ontwikkeling?",
      "Dekolonisatie",
      ["Handelskolonialisme",
       "Slowbalisering",
       "Globalisering"],
      "Het zelfstandig worden van kolonies noemen we dekolonisatie.", 25),
    M("Welke vorm van invloed over landsgrenzen heen gebeurt volgens de tekst NIET meer?",
      "Handelskolonialisme",
      ["Invloed via wereldwijd actieve multinationals",
       "Invloed via investeringen in andere landen",
       "Invloed via politieke keuzes in handelsrelaties"],
      "Landen hebben nog invloed over hun grenzen heen, maar niet meer in de vorm van handelskolonialisme.", 22),
    M("Hoe lang duurde de periode waarin bijna alle voormalige kolonies onafhankelijk werden ongeveer?",
      "Ongeveer 25 jaar",
      ["Ongeveer 250 jaar",
       "Ongeveer 2,5 jaar",
       "Ongeveer 100 jaar"],
      "In een periode van ongeveer 25 jaar werden bijna alle voormalige kolonies onafhankelijk.", 22),
    W("De internationale kritiek op het uitbuiten van kolonies zwol vooral na 1945 aan.", True,
      "Waar. Ook eerder was er discussie, maar na 1945 nam de kritiek sterk toe.", 22),
    W("Na 1945 bleven vrijwel alle kolonies nog eeuwenlang onder Europees bestuur.", False,
      "Niet waar. In ongeveer 25 jaar werden bijna alle voormalige kolonies onafhankelijk.", 22),
    W("Handelskolonialisme is vandaag nog steeds de manier waarop landen invloed uitoefenen buiten hun grenzen.", False,
      "Niet waar. Landen oefenen nog wel invloed uit, maar niet meer in de vorm van handelskolonialisme.", 22),
    W("De Koude Oorlog was een conflict tussen westerse landen en een groep landen rond de Sovjet-Unie.", True,
      "Waar. Dit conflict liep van 1945 tot 1990.", 25),
    W("Na de dekolonisatie hadden voormalige kolonisatoren niets meer te maken met hun oude kolonies.", False,
      "Niet waar. De banden werden niet altijd doorgesneden.", 22),
    I("Ook ten tijde van het handelskolonialisme was er al ____ over het koloniale systeem.", "discussie", "Er was al discussie over het koloniale systeem.", 22),
    I("Ook al was de oude kolonisator niet meer de baas, de ____ werden niet altijd doorgesneden.", "banden|handelsbanden", "De banden met het moederland werden niet altijd doorgesneden.", 22),
    I("De periode van de Koude Oorlog liep van 1945 tot ____.", "1990", "De periode 1945-1990 is ook de periode van de Koude Oorlog.", 25),
    I("De voormalige kolonies werden bij de dekolonisatie een eigen ____ met een eigen bestuur.", "staat|eigen staat", "Ze werden een eigen staat met een eigen bestuur.", 22),
    O("Beschrijf twee kenmerken van de dekolonisatie: de duur en het resultaat voor de kolonies.", ["25/vijfentwintig", "onafhankelijk/eigen staat/eigen bestuur/zelfstandig"], 2,
      "Het duurde ongeveer 25 jaar en bijna alle kolonies werden onafhankelijk met een eigen bestuur.",
      "Het duurde ongeveer 25 jaar en de kolonies werden onafhankelijke staten.", 22),
    O("Leg uit op welke manier de oude kolonisator ook na de onafhankelijkheid invloed kon houden.", ["handelspartner/handel", "banden"], 2,
      "De banden werden niet doorgesneden en het moederland bleef veelal de belangrijkste handelspartner.",
      "De banden bleven bestaan en het oude moederland was nog de belangrijkste handelspartner.", 22)
]),

113: ("Invloed van de VS en China: Nieuwe Zijderoute", "🛣️", [
    M("Waarom heten veel landen de Chinese investeringen volgens de tekst van harte welkom?",
      "China bemoeit zich vaak niet met hoe er in die landen met mensenrechten wordt omgegaan",
      ["China eist dat de landen daarvoor hun hele democratie volgens het Chinese model opnieuw inrichten",
       "De investeringen worden door de Verenigde Naties verplicht gesteld voor alle arme landen in de wereld",
       "China vraagt als tegenprestatie dat de landen hun taal en cultuur overnemen"],
      "China bemoeit zich vaak niet met de mensenrechten, wat de investeringen aantrekkelijk maakt.", 23),
    M("Wat hoopt China te bereiken met zijn wereldwijde investeringen in infrastructuur?",
      "Goede handelsrelaties creëren en zijn politieke invloed uitbreiden",
      ["Alle Europese handel via de eigen havens laten lopen en andere havens sluiten",
       "Voormalige koloniën van Europese landen overnemen en eigen bestuurders plaatsen",
       "Zijn eigen grenzen sluiten voor buitenlandse investeringen en producten"],
      "China hoopt wereldwijd goede handelsrelaties te creëren en zijn politieke invloed uit te breiden.", 23),
    M("Welke bedrijven noemt het boek als voorbeeld van multinationals die je over de hele wereld kunt vinden?",
      "McDonald's, Nike en Apple",
      ["Shell, Philips en Unilever",
       "Huawei, Lenovo en Alibaba",
       "Toyota, Samsung en Sony"],
      "McDonald's, Nike en Apple zijn voorbeelden van Amerikaanse multinationals.", 22),
    M("Wat concluderen de VN-rapporteurs in bron 15 over de behandeling van Oeigoeren?",
      "Ze worden willekeurig opgesloten en er zou sprake zijn van marteling en discriminatie",
      ["Ze krijgen van China een eigen zelfstandig gebied met eigen bestuur",
       "Ze werken vrijwillig in fabrieken die Europese bedrijven met chips beleveren",
       "Ze worden gelijk behandeld, maar mogen hun gebied niet verlaten"],
      "Oeigoeren worden volgens de VN willekeurig opgesloten en onderworpen aan mishandeling en discriminatie.", 25),
    M("Een Chinese krant wil de regering openlijk bekritiseren. Wat is volgens de tekst de situatie in China?",
      "Dat is niet toegestaan, want kritische journalistiek mag er niet en de meningsuiting is beperkt",
      ["Dat mag wel, maar alleen in kranten die in het buitenland worden gedrukt en verspreid onder lezers",
       "Dat mag wel, want China is een democratie met vrije verkiezingen",
       "Dat mag alleen als de krant eigendom is van een grote buitenlandse multinational met veel adverteerders"],
      "In China is geen democratie, is kritische journalistiek niet toegestaan en is vrijheid van meningsuiting beperkt.", 23),
    M("Welke gegevens toont bron 13 over chips?",
      "Over de grootste importeurs en exporteurs van chips",
      ["Over de grootste producenten van kopererts ter wereld",
       "Over de landen die deelnemen aan de graandeal",
       "Over de plaatsen waar Europese handelskolonies lagen"],
      "Bron 13 laat de grootste importeurs en exporteurs van chips zien.", 23),
    M("China investeerde in een stadion in Zambia (bron 14), in een gebied met veel kopererts. Wat is de meest logische reden?",
      "Koper is belangrijk voor elektronica, dus China wil goede banden met dit grondstoffengebied",
      ["Zambia betaalde het stadion helemaal zelf om minder afhankelijk te worden van China en andere landen",
       "China wilde vooral een nieuwe afzetmarkt voor voetbaltickets en sportkleding openen in Afrika",
       "Het stadion hoort bij Amerikaanse investeringen in sportinfrastructuur"],
      "In het gebied zit veel kopererts, een belangrijk metaal voor elektronica; investeren levert China goede handelsrelaties op.", 25),
    M("Met welke andere stap vergroot China zijn economische macht volgens de tekst?",
      "Het verstevigen van zijn militaire aanwezigheid in de Zuid-Chinese Zee",
      ["Het stoppen van alle exporten van chips naar Nederland",
       "Het opkopen van Amerikaanse multinationals als Apple en Nike",
       "Het sluiten van de Zwarte Zee voor het graantransport"],
      "China verstevigt zijn militaire aanwezigheid in de Zuid-Chinese Zee.", 23),
    M("Welke grootmacht heeft volgens het boek sinds 1945 de meeste invloed buiten de eigen grenzen?",
      "De Verenigde Staten",
      ["Het Verenigd Koninkrijk",
       "De Sovjet-Unie",
       "Frankrijk"],
      "De VS zijn sinds de Tweede Wereldoorlog het invloedrijkste land.", 22),
    W("Het Levy Mwanawasa Stadion in Zambia werd gebouwd dankzij investeringen van de Verenigde Staten.", False,
      "Niet waar. Het stadion kon gebouwd worden dankzij Chinese investeringen (bron 14).", 23),
    W("Gedwongen geboortebeperking wordt in bron 15 genoemd als vorm van discriminatie op medisch gebied.", True,
      "Waar. Bron 15 noemt dit als aanwijzing voor discriminatie van Oeigoeren.", 25),
    W("Veel landen weigeren Chinese investeringen omdat China zich te sterk bemoeit met hun mensenrechtenbeleid.", False,
      "Niet waar. Juist omdat China zich vaak niet bemoeit met mensenrechten, zijn de investeringen welkom.", 23),
    W("Chinese investeringen in infrastructuur vinden alleen plaats in Aziatische landen.", False,
      "Niet waar. Het gaat om landen over de hele wereld.", 23),
    W("De invloed van China groeit aan dezelfde kant van de Stille Oceaan als de Verenigde Staten.", False,
      "Niet waar. Het boek spreekt over de andere kant van de Stille Oceaan.", 22),
    I("Het Chinese investeringsproject in infrastructuur heet de Nieuwe ____.", "Zijderoute|zijderoute|Zijde Route",
      "Dit project heet de Nieuwe Zijderoute.", 23),
    I("Volgens bron 15 worden Oeigoeren opgesloten in heropvoedingskampen in de provincie ____.", "Xinjiang",
      "Het gaat om de provincie Xinjiang.", 25),
    I("Het stadion in bron 14 staat in de Zambiaanse stad ____.", "Ndola",
      "Het Levy Mwanawasa Stadion staat in Ndola.", 23),
    I("Bron 15 is naar een bericht van de NOS van 1 september ____.", "2022", "Bron 15 is naar een NOS-bericht van 1 september 2022.", 22),
    O("Waarom zijn Chinese investeringen voor veel landen aantrekkelijk, terwijl westerse landen en buurlanden er argwanend naar kijken?", ["welkom/aantrekkelijk/mensenrechten", "militair/macht/invloed"], 2,
      "Landen zijn blij met de investeringen omdat China zich niet met mensenrechten bemoeit, maar buurlanden zien de groeiende macht en de militaire aanwezigheid met argwaan.",
      "De investeringen zijn welkom door het ontbreken van bemoeienis met mensenrechten, maar de militaire macht en invloed van China maken anderen argwanend.", 23),
    O("Beschrijf hoe de invloed van de VS zich over de wereld uitstrekt en hoe die van China.", ["multinational/bedrijven", "investering/infrastructuur"], 2,
      "De VS zijn zichtbaar via multinationals als McDonald's, Nike en Apple; China breidt zijn invloed uit met grote investeringen in infrastructuur.",
      "De VS via multinationals, China via investeringen in infrastructuur.", 23)
]),

114: ("Politieke spanningen en de wereldhandel", "⚔️", [
    M("Een Nederlands bedrijf wil bepaalde chipmachines aan China verkopen. Wat is daarvan volgens het boek het gevolg van de chipoorlog?",
      "Voor bepaalde chipmachines exporteert Nederland niet meer naar China",
      ["Nederland verkoopt juist veel meer chipmachines naar China dan voorheen dankzij het conflict",
       "De Verenigde Naties bepalen voortaan zelf welk Nederlands bedrijf aan China mag leveren",
       "China mag chipmachines alleen nog via de Verenigde Staten kopen"],
      "Het handelsconflict tussen de VS en China leidde ertoe dat Nederland bepaalde chipmachines niet meer naar China exporteert.", 23),
    M("Waarom kijken buurlanden en westerse landen met argwaan naar de groei van China?",
      "China breidt zijn economische macht uit, onder meer met militaire aanwezigheid in de Zuid-Chinese Zee",
      ["China sluit zijn grenzen voor alle buitenlandse handel en bedrijven, ook in zijn eigen havens",
       "China wil zijn vroegere kolonies in Afrika terugkrijgen van de Europese landen die ze overnamen",
       "China weigert mee te doen aan de handel in chips en grondstoffen"],
      "China vergroot zijn economische macht en militaire aanwezigheid, wat tot politieke spanningen leidt.", 23),
    M("Wat maakte de graandeal tussen Rusland en Oekraïne mogelijk?",
      "Oekraïens graan kon ondanks de oorlog toch over de Zwarte Zee worden geëxporteerd",
      ["Russisch graan kon ondanks de handelsbeperkingen over de Oostzee naar Europese havens worden verscheept",
       "Oekraïens graan werd via het spoor gratis verdeeld onder arme landen",
       "Europese boeren mochten tijdelijk meer graan telen dan toegestaan"],
      "Door de graandeal kon Oekraïens graan ondanks de oorlog over de Zwarte Zee worden geëxporteerd.", 26),
    M("Welke landen krijgen volgens bron 16 vooral te maken met gevolgen van stijgende voedselprijzen?",
      "Minder welvarende landen in Afrika, Azië en het Midden-Oosten",
      ["Rijke Europese landen die zelf geen graan telen",
       "Landen rond de Zuid-Chinese Zee met een hoge welvaart",
       "Uitsluitend de landen die ook aan de oorlog meedoen"],
      "Voor minder welvarende landen in Afrika, Azië en het Midden-Oosten heeft het gevolgen voor de voedselzekerheid.", 26),
    M("Waarom kan een onderbreking van de Oekraïense export de voedselprijzen wereldwijd laten stijgen?",
      "Oekraïne is een van 's werelds grootste exporteurs van graan en andere voedingsmiddelen",
      ["Oekraïne bepaalt als enige land de prijs van al het graan en alle voedingsmiddelen op aarde",
       "Graan uit Oekraïne is altijd veel goedkoper dan graan uit alle andere landen",
       "Oekraïne is de grootste importeur van graan en verkoopt het daarna tegen hogere prijzen door"],
      "Door de grote rol van Oekraïne als exporteur kan elke onderbreking tot flink stijgende prijzen leiden.", 26),
    M("Een econoom zegt: 'Door politieke keuzes groeit de wereldhandel minder snel.' Welk begrip gebruikt hij hiervoor?",
      "Slowbalisering",
      ["Dekolonisatie",
       "Handelskolonialisme",
       "Global shift"],
      "Slowbalisering betekent dat de globalisering afremt, bijvoorbeeld door politieke spanningen.", 26),
    M("Welke is een politieke reden waarom twee landen geen handel met elkaar drijven?",
      "Ze zijn in conflict, bijvoorbeeld door oorlog of een handelsconflict",
      ["Ze hebben een verschillende taal, een ander klimaat en een andere hoofdstad",
       "Ze liggen aan verschillende oceanen op aarde",
       "Ze hebben een verschillend klimaat en landschap"],
      "Politieke spanningen of conflicten kunnen ervoor zorgen dat landen niet met elkaar handelen.", 24),
    M("Wat betekent het dat handelsrelaties 'onder invloed staan van politieke keuzes'?",
      "Landen bepalen op politieke gronden met wie ze handel drijven",
      ["Handel wordt volledig bepaald door de prijs van producten",
       "Handelspartners worden door de VN op basis van loting aan elk land toegewezen",
       "Alleen bedrijven, en nooit overheden, beslissen over wie met wie handelt"],
      "De chipoorlog laat zien dat handelsrelaties afhangen van keuzes van landen.", 23),
    M("Wat hebben de chipoorlog en het stoppen van de graandeal met elkaar gemeen?",
      "In beide gevallen beïnvloeden politieke spanningen de wereldhandel",
      ["In beide gevallen verbiedt de VN alle internationale handel",
       "In beide gevallen gaat het om export van voedingsmiddelen",
       "In beide gevallen zijn alleen Aziatische landen betrokken"],
      "Beide voorbeelden laten zien dat politieke spanningen de wereldhandel kunnen beïnvloeden.", 26),
    W("Door de graandeal werd Oekraïens graan via de Oostzee geëxporteerd.", False,
      "Niet waar. Het graan werd over de Zwarte Zee geëxporteerd.", 26),
    W("Een onderbreking van de Oekraïense export kan zorgen voor flink stijgende voedselprijzen.", True,
      "Waar. Dat staat in bron 16.", 26),
    W("Slowbalisering betekent dat de globalisering juist sneller gaat door politieke spanningen.", False,
      "Niet waar. Slowbalisering gaat over het afremmen van de globalisering.", 26),
    W("Westerse landen houden de groeiende macht van China argwanend in de gaten.", True,
      "Waar. Buurlanden en westerse landen letten goed op.", 23),
    W("Bij de chipoorlog gaat het om een conflict tussen Nederland en Oekraïne.", False,
      "Niet waar. De chipoorlog is een handelsconflict tussen de VS en China.", 23),
    I("De stijgende voedselprijzen hebben vooral gevolgen voor de ____zekerheid in minder welvarende landen.", "voedsel", "Het gaat om de voedselzekerheid in minder welvarende landen.", 23),
    I("Wereldwijd klinken ____ reacties op het besluit van Rusland om zich terug te trekken uit de graandeal.", "verontruste|geschrokken", "In bron 16 staat: verontruste reacties op het stoppen van de graandeal.", 26),
    I("Rusland trok zich in juli ____ terug uit de graandeal met Oekraïne.", "2023",
      "Het NOS-bericht van 17 juli 2023 meldt dit.", 26),
    I("China probeert zijn economische macht uit te breiden door zijn militaire aanwezigheid te ____.", "verstevigen|versterken|vergroten", "China verstevigt zijn militaire aanwezigheid.", 23),
    O("Noem twee politieke redenen waarom landen onderling geen handel drijven.", ["oorlog/conflict/spanning", "mensenrechten/handelsconflict/chip/macht"], 2,
      "Bijvoorbeeld door oorlog of conflict tussen de landen, of door een handelsconflict zoals de chipoorlog.",
      "Een oorlog of conflict en een handelsconflict zoals de chipoorlog.", 24),
    O("Beschrijf in een redenering hoe de oorlog tussen Rusland en Oekraïne kan leiden tot problemen in minder welvarende landen.", ["graan/export", "voedselprijzen/prijzen/voedselzekerheid"], 2,
      "De export van Oekraïens graan komt in gevaar, daardoor stijgen de voedselprijzen en komt de voedselzekerheid in minder welvarende landen in gevaar.",
      "Als de graanexport stokt, stijgen de voedselprijzen en lopen arme landen risico op voedselzekerheid.", 26)
]),

115: ("Fasen van de wereldhandel: van koloniën tot nu", "🗺️", [
    M("Welke volgorde van fasen klopt, van oud naar nieuw?",
      "Handelskolonialisme, dekolonisatie, politieke spanningen zoals de chipoorlog",
      ["Dekolonisatie, handelskolonialisme, politieke spanningen zoals de chipoorlog",
       "Politieke spanningen zoals de chipoorlog, handelskolonialisme, dekolonisatie",
       "Handelskolonialisme, politieke spanningen zoals de chipoorlog, dekolonisatie"],
      "Het handelskolonialisme begon in de 16e eeuw, de dekolonisatie volgde na 1945 en de chipoorlog hoort bij de huidige tijd.", 22),
    M("Welk kenmerk hoort bij de fase van het handelskolonialisme?",
      "Overzeese gebieden moesten grondstoffen leveren aan hun kolonisator",
      ["Landen zetten wereldwijd investeringsprojecten in infrastructuur op",
       "Landen beperken hun handel onderling door politieke spanningen en strenge importregels",
       "Gebieden werden zelfstandige staten met een eigen bestuur"],
      "Kolonies werden verplicht grondstoffen te leveren aan hun kolonisator.", 22),
    M("Een lesbrief zegt: 'Nederland verbiedt de export van bepaalde machines naar een grootmacht.' Bij welke ontwikkeling past dit?",
      "Politieke spanningen die de wereldhandel beïnvloeden",
      ["Het handelskolonialisme van de zestiende eeuw",
       "De dekolonisatie van kolonies na 1945",
       "De verplichte levering van specerijen"],
      "Dit voorbeeld hoort bij de chipoorlog, een voorbeeld van politieke spanningen in de handel.", 23),
    M("Bron 17 gaat over Niger. Bij welke fase van de wereldhandel hoort de onafhankelijkheid van zulke landen?",
      "De dekolonisatie na 1945",
      ["Het handelskolonialisme van de 16e eeuw",
       "De chipoorlog van de afgelopen jaren",
       "De graandeal over de Zwarte Zee"],
      "Niger werd in 1960 onafhankelijk, in de periode van de dekolonisatie.", 26),
    M("Wat laat het verschil tussen de exportpartners van Niger in 1995 en 2022 zien?",
      "Handelsrelaties zijn niet beperkt tot het oude moederland, maar verschuiven naar nieuwe partners",
      ["Niger exporteert in 2022 uitsluitend nog naar het vroegere moederland en zijn directe buren",
       "Niger handelt in 2022 alleen nog met de buurlanden Nigeria en Mali",
       "Niger voert in 2022 geen goederen meer uit omdat het sinds de onafhankelijkheid alles zelf gebruikt"],
      "In 2022 verschijnen nieuwe exportpartners zoals China en de Verenigde Arabische Emiraten.", 27),
    M("Wat hebben de VOC en de huidige multinationals gemeen?",
      "Het zijn bedrijven die wereldwijd handeldrijven",
      ["Ze veroveren gebieden en besturen daar kolonies",
       "Ze leveren uitsluitend grondstoffen aan hun thuisland",
       "Ze bestaan alleen in de zestiende eeuw"],
      "De VOC wordt de eerste multinational genoemd; ook huidige multinationals handelen over de hele wereld.", 22),
    M("Wat hebben handelskolonialisme en de invloed van grootmachten nu met elkaar gemeen?",
      "Landen proberen invloed uit te oefenen ver over hun eigen grenzen heen",
      ["In beide gevallen moeten gebieden verplicht grondstoffen leveren",
       "In beide gevallen worden de regels volledig bepaald door de Verenigde Naties",
       "In beide gevallen begon de invloed pas na 1990"],
      "Landen oefenen al honderden jaren invloed uit over hun eigen landsgrenzen heen.", 22),
    M("Welke twee ontwikkelingen speelden zich na 1945 tegelijk af?",
      "Kolonies werden onafhankelijk en de Verenigde Staten werden het invloedrijkste land",
      ["Het handelskolonialisme begon en de VOC werd opgericht",
       "De chipoorlog begon en Rusland trok zich terug uit de graandeal",
       "De Nieuwe Zijderoute werd aangelegd en het Verenigd Koninkrijk verliet de EU"],
      "Vanaf 1945 volgde de dekolonisatie en waren de VS het invloedrijkste land.", 22),
    M("Welk leerdoel van deze paragraaf gaat over politiek?",
      "Je begrijpt dat politieke spanningen de globalisering kunnen beïnvloeden",
      ["Je weet hoe je het bbp per hoofd van een land uitrekent en vergelijkt",
       "Je kunt de grootte van een bevolking op een kaart tekenen",
       "Je weet welke landen in de Europese Unie een eigen munt hebben"],
      "Dit is een van de leerdoelen van paragraaf 1.2.", 22),
    W("Niger werd in 1960 onafhankelijk.", True,
      "Waar. Dat staat in de opdracht bij bron 17.", 26),
    W("De totale waarde van de uitvoer van Niger was in 2022 lager dan in 1995.", False,
      "Niet waar. De waarde steeg van 448 miljoen dollar naar 3,24 miljard dollar.", 27),
    W("Het handelskolonialisme duurde van 1945 tot 1990.", False,
      "Niet waar. Het duurde van de 16e eeuw tot ver in de 20e eeuw.", 22),
    W("In bron 17 staat niet welk soort goederen Niger heeft vervoerd.", True,
      "Waar. Je moet dat afleiden uit de rol van het land in de wereldhandel.", 26),
    W("Slowbalisering heeft te maken met het versnellen van de wereldhandel.", False,
      "Niet waar. Het gaat om afremmen door politieke spanningen.", 26),
    I("Voor 1995 meldt bron 17 een totale waarde van de uitvoer van 448 ____ dollar.", "miljoen",
      "Bron 17 noemt 448 miljoen dollar.", 27),
    I("Het bedrag dat Niger in 2022 uitvoerde, was samen 3,24 ____ dollar waard.", "miljard",
      "Bron 17 noemt 3,24 miljard dollar.", 27),
    I("Sinds de ____ Wereldoorlog zijn de Verenigde Staten het invloedrijkste land.", "Tweede|tweede",
      "Het boek noemt de Tweede Wereldoorlog.", 22),
    I("Nigeria en Mali kampen al jaren met binnenlandse ____.", "conflicten|conflict", "Nigeria en Mali kampen met binnenlandse conflicten, maar toch wordt er veel met Niger gehandeld.", 22),
    O("Beschrijf de kenmerken van twee fasen van de wereldhandel uit deze paragraaf.", ["grondstoffen/kolonie", "onafhankelijk/dekolonisatie/chip/spanning"], 2,
      "In het handelskolonialisme moesten kolonies grondstoffen leveren; later werden de kolonies onafhankelijk en nu spelen politieke spanningen zoals de chipoorlog.",
      "Kolonies leverden grondstoffen, daarna werden ze onafhankelijk, nu zijn er spanningen.", 22),
    O("Vat in twee zinnen samen hoe de invloed van landen over hun grenzen heen is veranderd.", ["grondstoffen/overheers", "multinational/investering"], 2,
      "Vroeger overheersten landen overzeese gebieden voor grondstoffen; nu gaat het via multinationals en investeringen.",
      "Eerst overheersing voor grondstoffen, nu via multinationals en investeringen.", 22)
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
            "paragraaf": "1.2",
            "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
            "titel": f"Toets {nr} — §1.2 {sub}",
            "vak": "Aardrijkskunde · HAVO 3 (H1)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 §1.2) — gegenereerd door tools/gen_aardrijkskunde_h1_2_extra2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
