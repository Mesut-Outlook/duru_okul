#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.5 Rol van Nederland in de wereldhandel (extra toetsen 126–130).
Schrijft havo3/aardrijkskunde/js/data/examen_126..130.js (ex-h3-ak-126..130).
9 MC, 5 Waaronwaar, 4 Invul, 2 Open. Script: gen_aardrijkskunde_h1_5_extra2.py.
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
126: ("Open economie en positie van Nederland", "🌍", [
    M("Een leerling zegt: 'Nederland is klein, dus het speelt nauwelijks een rol in de wereldhandel.' Welk feit uit de paragraaf spreekt dit het best tegen?",
      "Nederland staat al jaren in de top 3 van de globaliseringsindex",
      ["Nederland heeft de grootste landoppervlakte van heel Europa",
       "Meer dan 70 landen hebben een kleinere bevolking dan Nederland",
       "Nederland haalt al zijn grondstoffen uit de eigen bodem"],
      "Nederland is klein, maar staat al jaren in de top 3 van de globaliseringsindex en speelt een grote rol in de wereldhandel.", 42),
    M("Welke van deze uitspraken over de mondiale positie van Nederland is onjuist?",
      "Slechts enkele landen hebben een grotere bevolking dan Nederland",
      ["Nederland staat op plek 28 van de wereldranglijst voor het totale bbp",
       "Er zijn 132 landen die in oppervlakte groter zijn dan Nederland",
       "Nederlandse bedrijven importeren producten vanuit de hele wereld"],
      "Meer dan 70 landen hebben een grotere bevolking dan Nederland, dus niet slechts enkele.", 42),
    M("Nederland staat op plek 28 van de bbp-ranglijst, terwijl 132 landen groter zijn in oppervlakte. Wat laat dit zien?",
      "Dat een groot bbp niet afhangt van een grote oppervlakte",
      ["Dat de grootste landen altijd het hoogste bbp hebben",
       "Dat het bbp van een land vooral door zijn inwonertal bepaald wordt",
       "Dat Nederland meer inwoners heeft dan al die grotere landen"],
      "Nederland is klein in oppervlakte, maar heeft toch een groot bbp.", 42),
    M("Een land sluit zijn grenzen grotendeels voor buitenlandse bedrijven en producten. Wat gebeurt er waarschijnlijk met zijn score op de globaliseringsindex?",
      "Die daalt, want het land is minder sterk met het buitenland verbonden",
      ["Die stijgt, want het land beschermt zijn eigen economie beter",
       "Die blijft gelijk, want de index meet alleen de oppervlakte van een land",
       "Die stijgt, want er komen daardoor meer multinationals naar het land"],
      "De index geeft aan hoe sterk een land met het buitenland verbonden is; sluit je de grenzen, dan daalt die verbondenheid.", 42),
    M("Veel multinationals hebben zich in Nederland gevestigd. Waarom past dit bij de hoge score op de globaliseringsindex?",
      "Multinationals zijn in meerdere landen actief en verbinden Nederland zo met het buitenland",
      ["Multinationals betalen in Nederland de hoogste lonen van Europa en trekken daardoor veel buitenlandse werknemers aan",
       "Multinationals produceren uitsluitend voor de Nederlandse thuismarkt",
       "Multinationals zorgen ervoor dat Nederland veel minder hoeft te importeren"],
      "Multinationals zijn in meerdere landen gevestigd; dat laat zien hoe sterk Nederland met het buitenland verbonden is.", 42),
    M("Welke houding past bij een land dat gebaat is bij een open wereldeconomie?",
      "Het wil dat handel met andere landen zo min mogelijk belemmerd wordt",
      ["Het legt hoge belastingen op alle producten uit het buitenland",
       "Het verbiedt buitenlandse bedrijven zich op zijn grondgebied te vestigen",
       "Het koopt alleen producten van eigen bedrijven om werk te behouden"],
      "Nederland heeft een open, op het buitenland gerichte economie en is gebaat bij weinig handelsbelemmeringen.", 42),
    M("Hoe hangen vrijhandel en mainports samen met de hoge globaliseringsindex van Nederland?",
      "Weinig handelsbelemmeringen en grote havens maken veel internationale handel mogelijk",
      ["Hoge invoerrechten en kleine havens houden de handel zoveel mogelijk binnen de landsgrenzen van het land",
       "Strenge quota en veel staatsbedrijven beperken de buitenlandse handel",
       "Een grote landoppervlakte en een groot aantal inwoners zorgen voor handel"],
      "Vrijhandel en mainports zorgen voor veel contact met het buitenland en dus voor een hoge score op de index.", 44),
    M("Land A scoort veel lager dan Nederland op de globaliseringsindex. Wat kun je daaruit afleiden?",
      "Dat land A minder sterk met het buitenland verbonden is dan Nederland",
      ["Dat land A een kleinere oppervlakte heeft dan Nederland",
       "Dat land A minder inwoners heeft dan Nederland",
       "Dat land A een hogere Gini-coëfficiënt heeft dan Nederland"],
      "De globaliseringsindex meet alleen hoe sterk een land met het buitenland verbonden is, niet de grootte of ongelijkheid.", 42),
    M("De Verenigde Staten willen niet dat ASML bepaalde chipmachines aan China verkoopt. Wat laat dit zien over een land als Nederland?",
      "Dat Nederlandse bedrijven last kunnen krijgen van politieke spanningen tussen andere landen",
      ["Dat Nederland zelf bepaalt aan welke landen ASML mag verkopen",
       "Dat politieke spanningen alleen gevolgen hebben voor landen die zelf geen handel met het buitenland drijven",
       "Dat handel tussen landen nooit door de politiek beïnvloed wordt"],
      "Politieke spanningen (de chipoorlog) kunnen de handel van een sterk verweven land als Nederland raken.", 46),
    W("Een land met een kleine oppervlakte kan toch hoog scoren op de globaliseringsindex.", True,
      "Waar. Nederland is klein, maar staat al jaren in de top 3.", 42),
    W("Omdat Nederland op plek 28 van de bbp-ranglijst staat, hebben meer dan 28 landen een hoger bbp.", False,
      "Niet waar. Op plek 28 staan 27 landen boven Nederland.", 42),
    W("Op de globaliseringsindex scoort een land hoog als het weinig contact met het buitenland heeft.", False,
      "Niet waar. De index meet hoe sterk een land met het buitenland verbonden is.", 42),
    W("Doordat veel multinationals in Nederland gevestigd zijn, is dat goed te zien aan de globaliseringsindex.", True,
      "Waar. Dit sluit aan bij de hoge score van Nederland.", 42),
    W("Nederlandse bedrijven importeren producten vanuit de hele wereld.", True,
      "Waar. Nederland importeert vanuit de hele wereld en exporteert veel.", 42),
    I("Nederland heeft een ____ en sterk op het buitenland gerichte economie.", "open",
      "Het is een open economie.", 42),
    I("Meer dan 70 landen hebben een grotere ____ dan Nederland.", "bevolking|inwonertal|aantal inwoners",
      "Meer dan 70 landen hebben een grotere bevolking.", 42),
    I("Nederlandse bedrijven exporteren veel, met name naar onze ____.", "buurlanden|buurland",
      "De export gaat vooral naar de buurlanden.", 42),
    I("Samen met Nederland en België staat ____ al jaren in de top 3 van de globaliseringsindex.", "Zwitserland",
      "Dat is Zwitserland.", 42),
    O("Leg uit waarom een klein land als Nederland toch een grote rol speelt in de wereld. Geef twee verklaringen uit de paragraaf.",
      ["globaliseringsindex/top 3", "multinational", "import/importeren/export/exporteren", "haven/mainport/schiphol"], 2,
      "Nederland staat al jaren in de top 3 van de globaliseringsindex. Er zijn veel multinationals gevestigd en we importeren en exporteren veel, onder meer via de haven van Rotterdam.",
      "Verklaringen: top 3 van de globaliseringsindex, veel multinationals, veel import en export, mainports.", 42),
    O("Waarom is Nederland als handelsland gebaat bij weinig handelsbelemmeringen?",
      ["export/exporteren/afzet", "import/importeren/invoer", "haven/mainport/doorvoer"], 2,
      "Nederland exporteert veel en heeft afzetmarkten nodig. Daarnaast importeren we veel producten en gaat er via de haven veel handel door Nederland.",
      "Een open economie leeft van import, export en doorvoer; handelsbelemmeringen vormen dan een bedreiging.", 42)
]),

127: ("Havens, mainports en doorvoer", "⚓", [
    M("Een container met schoenen uit Azië komt in Rotterdam aan en gaat daarna per vrachtwagen naar een ander Europees land. Wat laat dit zien?",
      "Dat producten uit het buitenland vaak worden doorgevoerd naar landen binnen Europa",
      ["Dat de haven van Rotterdam vooral goederen overslaat die bestemd zijn voor Nederlandse consumenten",
       "Dat producten uit Azië Europa uitsluitend via Schiphol binnenkomen",
       "Dat Nederlandse havens geen internationale handel afhandelen"],
      "Vanuit de hele wereld komen producten binnen die veelal worden doorgevoerd naar landen binnen Europa.", 42),
    M("Schiphol is geen haven. Waarom hoort het volgens de paragraaf toch in dezelfde categorie als Rotterdam?",
      "Het is net als Rotterdam een belangrijk knooppunt voor de internationale handel",
      ["Het ligt aan zee en ontvangt net als Rotterdam grote zeeschepen met containers",
       "Het slaat net als Rotterdam alleen goederen op die in Nederland blijven",
       "Het is net als Rotterdam de grootste luchthaven van de hele wereld"],
      "De paragraaf noemt zowel de haven van Rotterdam als luchthaven Schiphol een mainport.", 42),
    M("Door een staking ligt de haven van Rotterdam een week stil. Waarom merken ook bedrijven in andere Europese landen dat?",
      "Veel producten die daar binnenkomen, gaan van Rotterdam door naar die landen",
      ["Alle bedrijven in Europa zijn eigendom van Nederlandse multinationals",
       "Andere landen hebben zelf geen havens waar schepen kunnen aanleggen",
       "Rotterdam produceert zelf alle producten die in Europa verkocht worden"],
      "Nederlandse havens voeren veel producten door naar landen binnen Europa.", 42),
    M("Welke bewering over de goederen die in Nederlandse havens binnenkomen klopt NIET?",
      "Vrijwel alle binnengekomen goederen blijven in Nederland",
      ["Ze komen vanuit de hele wereld naar Nederland",
       "Een deel wordt doorgevoerd naar andere Europese landen",
       "De haven van Rotterdam is een belangrijke schakel in import en export"],
      "Producten worden veelal doorgevoerd naar landen binnen Europa; ze blijven dus niet allemaal in Nederland.", 42),
    M("Op grond waarvan staat de haven van Amsterdam volgens de paragraaf hoog op de lijst van Europese havens?",
      "Op grond van de hoeveelheid handelswaar die er wordt overgezet",
      ["Op grond van het aantal passagiers en cruiseschepen dat er jaarlijks vertrekt",
       "Op grond van het aantal inwoners van de stad Amsterdam",
       "Op grond van de totale lengte van de kades in de haven"],
      "De haven is de vierde van Europa, gezien de hoeveelheid handelswaar die er wordt overgezet.", 42),
    M("Een journalist schrijft: 'Nederland is slechts een doorgangsland zonder eigen productie.' Welk gegeven uit de paragraaf past daar niet bij?",
      "Er is ook hoogwaardige maakindustrie, zoals de hightechbedrijven in de regio Eindhoven",
      ["Nederlandse bedrijven importeren vanuit de hele wereld",
       "Een deel van de ingevoerde producten gaat naar andere landen",
       "Rotterdam is een belangrijke haven voor internationale handel"],
      "De hoogwaardige maakindustrie (bijvoorbeeld ASML in Veldhoven) laat zien dat Nederland ook zelf produceert.", 42),
    M("Een bedrijf wil een product snel door de lucht de wereld insturen. Welke Nederlandse mainport past daar het best bij?",
      "Luchthaven Schiphol",
      ["De haven van Rotterdam",
       "De haven van Amsterdam",
       "De High Tech Campus in Eindhoven"],
      "Schiphol is de mainport in de lucht; Rotterdam is de mainport over water.", 42),
    M("Waarheen exporteren Nederlandse bedrijven volgens de paragraaf met name?",
      "Naar de buurlanden",
      ["Naar landen in Zuid-Amerika", "Naar de Verenigde Staten", "Naar landen in Oost-Azië"],
      "Nederlandse bedrijven exporteren veel, met name naar de buurlanden.", 42),
    M("Een buitenlands bedrijf zoekt in Europa een plek waar producten uit de hele wereld aankomen en doorgaan. Welke Nederlandse locatie past daarbij?",
      "De haven van Rotterdam",
      ["De High Tech Campus in Eindhoven",
       "De Technische Universiteit in Eindhoven",
       "Het hoofdkantoor van ASML in Veldhoven"],
      "Rotterdam is de grootste haven van Europa en een echte mainport.", 42),
    W("De haven van Rotterdam is een mainport.", True,
      "Waar. Het is een echte mainport.", 42),
    W("Een mainport is een gebied met veel hightechbedrijven en kennisinstellingen.", False,
      "Niet waar. Dat is een brainport; een mainport is een belangrijke haven of luchthaven.", 42),
    W("De haven van Amsterdam is de grootste haven van Europa.", False,
      "Niet waar. Amsterdam is kleiner dan Rotterdam en de vierde haven van Europa.", 42),
    W("Producten die in Nederland aankomen, worden veelal doorgevoerd naar landen binnen Europa.", True,
      "Waar. Dat is de doorvoerfunctie van de Nederlandse havens.", 42),
    W("Schiphol is net als de haven van Rotterdam een belangrijk punt voor de internationale handel.", True,
      "Waar. Beide zijn mainports.", 42),
    I("Nederland is een klein land, maar speelt een vrij grote rol in de ____.", "wereldhandel|wereld handel",
      "Nederland speelt een grote rol in de wereldhandel.", 42),
    I("Sinds een aantal ____ draagt in ons land de hoogwaardige maakindustrie bij aan de economie.", "decennia|tientallen jaren",
      "Sinds een aantal decennia draagt de hoogwaardige maakindustrie bij.", 42),
    I("Ook hebben zich veel ____ in Nederland gevestigd.", "multinationals|multinational",
      "Veel multinationals hebben zich in Nederland gevestigd.", 42),
    I("In de rij van Europese havens komt Amsterdam na Rotterdam: het is de ____ grootste haven.", "vierde|4e|4de",
      "Amsterdam is de vierde haven van Europa.", 42),
    O("Leg uit waarom een storing in de haven van Rotterdam gevolgen heeft voor andere landen dan alleen Nederland.",
      ["doorvoer/doorgevoerd/doorvoeren", "ingevoerd/invoer/import", "wereld/overal/internationaal"], 2,
      "Veel producten uit de hele wereld worden in Rotterdam ingevoerd en daarna doorgevoerd naar andere landen. Die landen zijn daar dus van afhankelijk.",
      "Rotterdam is een mainport: producten worden ingevoerd en doorgevoerd naar andere Europese landen.", 42),
    O("Waarom is de haven van Amsterdam een belangrijke haven, hoewel ze kleiner is dan die van Rotterdam?",
      ["vierde/4e", "handelswaar/goederen/overgezet", "doorgevoerd/doorvoer"], 2,
      "Amsterdam is de vierde haven van Europa door de hoeveelheid handelswaar die er wordt overgezet. Producten worden hier ingevoerd en doorgevoerd.",
      "Amsterdam is de vierde haven van Europa, gezien de hoeveelheid handelswaar (p. 42).", 42)
]),

128: ("Brainport: vestigingsfactoren en ASML", "🔬", [
    M("Welke van de onderstaande factoren noemt de paragraaf NIET als gunstig voor hightechbedrijven in de regio Eindhoven?",
      "Een kustligging met een diepe zeehaven voor containerschepen",
      ["De aanwezigheid van bedrijven die elkaar aanvullen en ondersteunen",
       "Een goed opgeleide technische beroepsbevolking in de regio",
       "De nabijheid van interessante afzetmarkten voor producten"],
      "De drie genoemde factoren zijn aanvullende bedrijven, een goed opgeleide beroepsbevolking en nabije afzetmarkten.", 43),
    M("Ongeveer 95 procent van de machines van ASML wordt geëxporteerd. Welk deel blijft dus niet naar het buitenland gaan?",
      "Ongeveer 5 procent",
      ["Ongeveer 95 procent", "Ongeveer 50 procent", "Ongeveer 15 procent"],
      "100 minus 95 is 5 procent.", 43),
    M("In een straal van 150 kilometer rond Eindhoven wonen 40 miljoen mensen. Waarom is dat voor bedrijven gunstig?",
      "Die mensen hebben een bovengemiddeld hoge koopkracht en zijn dus mogelijke kopers",
      ["Die mensen zijn allemaal werkzaam bij de Technische Universiteit of bij ASML in Veldhoven",
       "Die mensen kopen uitsluitend producten die in Nederland geproduceerd zijn",
       "Die mensen zorgen voor goedkope arbeidskrachten in de maakindustrie"],
      "Het gaat om een interessante afzetmarkt: veel mensen met een bovengemiddeld hoge koopkracht.", 43),
    M("Waarom is het voor een hightechbedrijf handig om vlak bij een technische universiteit te zitten?",
      "Het kan er goed opgeleide technici vinden en met onderzoekers samenwerken",
      ["Het hoeft er geen belasting te betalen over zijn winst en krijgt er subsidie voor elk product",
       "Het krijgt er gratis grondstoffen van de universiteit geleverd",
       "Het kan er alle producten rechtstreeks aan studenten verkopen"],
      "In de regio werken het bedrijfsleven en de Technische Universiteit nauw samen en is de beroepsbevolking goed opgeleid.", 43),
    M("Een directeur zegt: 'Hier vind ik toeleveranciers en onderzoekers die precies aansluiten bij mijn werk.' Welke vestigingsplaatsfactor noemt hij?",
      "De aanwezigheid van bedrijven die elkaar aanvullen en ondersteunen",
      ["De nabijheid van een grote afzetmarkt",
       "Een goed opgeleide beroepsbevolking",
       "Het lage prijsniveau van bedrijfsgrond en woningen in de regio"],
      "Dit is de eerste factor uit de paragraaf: bedrijven die elkaar aanvullen, zoals op de High Tech Campus.", 42),
    M("Een personeelsmanager zegt: 'Ik vind hier gemakkelijk technici met een passende opleiding.' Welke vestigingsplaatsfactor noemt zij?",
      "Een goed opgeleide technische beroepsbevolking",
      ["De nabijheid van een grote afzetmarkt",
       "De aanwezigheid van aanvullende bedrijven",
       "Het ruime aanbod van goedkope arbeidskrachten"],
      "De tweede factor is de goed opgeleide (technische) beroepsbevolking.", 43),
    M("Wat is een mogelijk gevolg voor ASML als veel landen hun grenzen sluiten voor handel?",
      "Het bedrijf kan zijn machines moeilijker verkopen, want bijna alles gaat naar het buitenland",
      ["Het bedrijf verkoopt juist meer machines in Nederland zelf, omdat de buitenlandse concurrenten wegvallen",
       "Het bedrijf heeft geen last, want de afzetmarkt is Nederland",
       "Het bedrijf kan dan sneller groeien dankzij minder concurrentie"],
      "ASML exporteert 95 procent van zijn machines en is dus sterk afhankelijk van open grenzen.", 43),
    M("Waarom wordt de regio volgens de samenvatting ook wel brainport Eindhoven genoemd?",
      "Omdat er veel technische bedrijven zijn gevestigd en het een broedplaats is voor technische vernieuwing",
      ["Omdat er veel havens en luchthavens liggen waarlangs kennis en grondstoffen het land binnenkomen en doorgaan",
       "Omdat alle inwoners van de regio aan de universiteit studeren en daar meteen aan het werk gaan",
       "Omdat de regio de grootste afzetmarkt van heel Europa heeft"],
      "De samenvatting noemt veel technische bedrijven en een broedplaats voor technische vernieuwing.", 51),
    M("Welke rol speelt de overheid volgens de paragraaf in de regio Eindhoven?",
      "Ze steunt de hechte samenwerking tussen het bedrijfsleven en de Technische Universiteit",
      ["Ze is zelf eigenaar van bedrijven als ASML, DAF en Philips en stuurt de productie aan via de universiteit",
       "Ze verbiedt buitenlandse bedrijven zich in de regio te vestigen om werk te behouden",
       "Ze bepaalt welke chipmachines ASML mag bouwen"],
      "De samenwerking tussen bedrijfsleven en Technische Universiteit wordt gesteund door de overheid.", 43),
    W("De president van Zuid-Korea bezocht samen met de koning ASML in Eindhoven.", True,
      "Waar. Bron 31 toont dit bezoek.", 42),
    W("DAF is net als Philips een multinational in de regio Eindhoven.", True,
      "Waar. Genoemd worden ASML, DAF en Philips.", 42),
    W("De mensen rond Eindhoven hebben een lagere koopkracht dan gemiddeld.", False,
      "Niet waar. Zij hebben een bovengemiddeld hoge koopkracht.", 43),
    W("Brainport Eindhoven staat vooral bekend om de grootschalige overslag van containers.", False,
      "Niet waar. Dat past bij een mainport; Eindhoven staat bekend om hightech en kennis.", 42),
    W("Philips is een van de multinationals in brainport Eindhoven.", True,
      "Waar. Genoemd worden ASML, DAF en Philips.", 42),
    I("De High Tech ____ van de Technische Universiteit Eindhoven is een broedplaats van onderzoek en vernieuwing.", "Campus|campus",
      "Dat is de High Tech Campus.", 42),
    I("Eindhoven wordt weleens de ____ regio in de wereld genoemd.", "slimste",
      "Eindhoven wordt de slimste regio genoemd.", 42),
    I("ASML is gevestigd in de plaats ____, bij Eindhoven.", "Veldhoven",
      "ASML zit in Veldhoven.", 43),
    I("Sinds enkele decennia draagt ook de hoogwaardige ____industrie bij aan de Nederlandse economie.", "maak",
      "Dat is de hoogwaardige maakindustrie.", 42),
    O("Leg uit waarom de nabijheid van een afzetmarkt belangrijk is voor een producent van machines.",
      ["kopers/klanten/verkopen", "koopkracht/geld", "afstand/dichtbij/transport"], 2,
      "Een producent wil zijn machines verkopen aan veel kopers met voldoende koopkracht. Als die kopers dichtbij zitten, is het transport korter.",
      "Een afzetmarkt is een gebied waar bedrijven hun producten verkopen; bij Eindhoven wonen veel mensen met hoge koopkracht.", 43),
    O("Leg uit hoe de samenwerking tussen bedrijven, universiteit en overheid brainport Eindhoven sterker maakt.",
      ["onderzoek/vernieuwing/innovatie", "opgeleid/personeel/kennis", "steun/gesteund/subsidie"], 2,
      "Bedrijven en universiteit werken samen aan onderzoek en vernieuwing. Er is goed opgeleid personeel en de overheid steunt dit.",
      "Samenwerking zorgt voor vernieuwing en goed opgeleid personeel, gesteund door de overheid.", 43)
]),

129: ("Welvaart, ongelijkheid en beleid", "⚖️", [
    M("De tekst zegt: 'Terwijl sommigen verre vakantiebestemmingen en dure telefoons kunnen kiezen, hebben anderen het financieel zwaar.' Wat wil de schrijver hiermee laten zien?",
      "Dat de verschillen tussen rijk en arm binnen een welvarend land groot kunnen zijn",
      ["Dat verre vakanties en dure telefoons in Nederland binnenkort door de overheid verboden worden",
       "Dat alle Nederlanders gelijk profiteren van de hoge welvaart",
       "Dat telefoons voor de meeste mensen te duur zijn om te kopen"],
      "Ondanks de hoge welvaart zijn er grote verschillen tussen mensen.", 43),
    M("Een ander Europees land heeft een lagere sociale ongelijkheid dan Nederland. Welke Gini-coëfficiënt past daarbij?",
      "0,18", ["0,31", "0,44", "0,62"],
      "Nederland heeft 0,26. Een lagere ongelijkheid betekent een waarde dichter bij 0.", 43),
    M("De sociale ongelijkheid in Nederland verandert landelijk nauwelijks, maar groeit in veel plaatsen. Wat betekent dat?",
      "Landelijk veranderde weinig, maar op veel plekken werden de verschillen groter",
      ["De ongelijkheid is overal in het land evenveel toegenomen",
       "De ongelijkheid is in veel plaatsen juist sterk afgenomen",
       "De ongelijkheid is landelijk sterk gegroeid, maar lokaal gedaald"],
      "Landelijk is de situatie ongeveer gelijk gebleven, maar in veel plaatsen zijn de verschillen toegenomen.", 43),
    M("Een gemeente organiseert gratis huiswerkbegeleiding voor kinderen uit arme wijken. Onder welke overheidsinvestering uit de tekst valt dit het best?",
      "Onderwijs",
      ["Gezondheidszorg", "Voedselbank", "Energievoorziening"],
      "De overheid investeert in gezondheidszorg, onderwijs en gelijke kansen voor iedereen.", 43),
    M("Een buitenlandse student zegt: 'In Nederland is geen armoede, want de werkloosheid is laag.' Wat is het beste weerwoord?",
      "Ook in een welvarend land is er relatieve armoede, bijvoorbeeld door een te hoge energierekening",
      ["Armoede bestaat alleen in landen met een hoge werkloosheid en een lage welvaart per inwoner",
       "De Nederlandse overheid heeft armoede officieel afgeschaft",
       "Armoede is er alleen op het platteland en niet in de steden"],
      "Ondanks de hoge welvaart blijft er sprake van relatieve armoede.", 43),
    M("Welke van deze uitspraken over de welvaart in Nederland is onjuist?",
      "Het gemiddeld besteedbaar inkomen daalt",
      ["De Gini-coëfficiënt is 0,26",
       "Steeds meer mensen gebruiken de voedselbank",
       "In sommige grote plaatsen zijn de verschillen tussen wijken gegroeid"],
      "Het gemiddeld besteedbaar inkomen stijgt, dus niet daalt.", 43),
    M("Welke waarde kan een Gini-coëfficiënt volgens het boek NIET hebben?",
      "1,4", ["0,26", "0", "0,98"],
      "De Gini-coëfficiënt is een getal tussen 0 en 1.", 51),
    M("Het gemiddeld besteedbaar inkomen stijgt. Waarom bewijst dat niet dat niemand in Nederland moeite heeft om rond te komen?",
      "Een gemiddelde zegt niets over de verdeling: sommigen verdienen veel, anderen weinig",
      ["Een gemiddelde telt alleen de inkomens van de armste huishoudens in de grote plaatsen mee",
       "Een gemiddelde wordt alleen berekend over mensen zonder werk",
       "Een gemiddelde geldt alleen voor mensen in de grote steden"],
      "Gemiddeld stijgt het inkomen, maar de verschillen blijven en relatieve armoede bestaat.", 43),
    M("Waarom hoort investeren in gezondheidszorg en onderwijs bij het beleid tegen sociale ongelijkheid?",
      "Omdat het mensen betere kansen geeft, ongeacht hun afkomst of inkomen",
      ["Omdat het de koopkracht van de rijkste huishoudens beperkt",
       "Omdat het de import van goederen uit het buitenland vermindert",
       "Omdat het de voedselbanken overbodig maakt voor het hele land"],
      "De overheid wil met zorg, onderwijs en gelijke kansen de problemen tegengaan.", 43),
    W("Een Gini-coëfficiënt van 1 betekent dat iedereen even veel verdient.", False,
      "Niet waar. Bij 0 is iedereen gelijk.", 51),
    W("Ook in een welvarend land kunnen mensen moeite hebben om hun energierekening te betalen.", True,
      "Waar. Dat staat in de tekst over relatieve armoede.", 43),
    W("De sociale ongelijkheid in Nederland is de laatste jaren overal sterk gedaald.", False,
      "Niet waar. Ze is redelijk stabiel en in veel plaatsen gegroeid.", 43),
    W("Vergeleken met andere Europese landen heeft Nederland een hoge welvaart.", True,
      "Waar. Dat staat aan het begin van het stukje.", 43),
    W("Het gemiddeld besteedbaar inkomen stijgt en de werkloosheid is laag.", True,
      "Waar. Toch blijft er sprake van relatieve armoede.", 43),
    I("Ongelijkheid en armoede kunnen sociale spanningen geven en belemmeren de groei van de ____ en samenleving.", "economie",
      "Dat belemmert de groei van economie en samenleving.", 43),
    I("De overheid investeert in gezondheidszorg, onderwijs en ____ kansen voor iedereen.", "gelijke|gelijk",
      "Het gaat om gelijke kansen.", 43),
    I("Met name in de grote ____ zijn er steeds grotere verschillen tussen de rijkste en armste wijken.", "steden|stad",
      "Dat gebeurt vooral in de grote steden.", 43),
    I("Sociale ongelijkheid in Nederland is landelijk gezien redelijk ____.", "stabiel|constant",
      "Ze is redelijk stabiel.", 43),
    O("Een leerling zegt: 'Nederland is rijk, dus niemand heeft hier geldzorgen.' Leg uit waarom dit niet klopt.",
      ["relatieve armoede/armoede", "energierekening/voedselbank", "gemiddeld/verschillen"], 2,
      "Er is nog steeds relatieve armoede. Sommige mensen kunnen de energierekening niet betalen en gaan naar de voedselbank. Het gemiddelde zegt niets over de verschillen.",
      "Ook in een welvarend land is er relatieve armoede; sommigen hebben moeite met de energierekening en gebruiken de voedselbank.", 43),
    O("Waarom zegt een Gini-coëfficiënt van 0,26 niet dat alle Nederlanders even rijk zijn?",
      ["verschil/verschillen/ongelijkheid", "relatieve armoede/armoede", "nul"], 2,
      "Alleen bij nul is iedereen gelijk. 0,26 is laag, maar er blijven verschillen en er is relatieve armoede.",
      "Gini 0 betekent volledige gelijkheid; 0,26 is laag maar niet nul.", 43)
]),

130: ("Handelsstromen: bloemen, brandstoffen en chips", "🌹", [
    M("De totale Nederlandse export is 627 miljard euro. Welk deel bestaat volgens het boek NIET uit fossiele brandstoffen?",
      "84 procent", ["16 procent", "48 procent", "94 procent"],
      "16 procent is fossiel, dus 100 min 16 is 84 procent niet.", 45),
    M("Wat hebben de twee grootste exportpartners van Nederland, Duitsland en België, gemeen?",
      "Het zijn buurlanden van Nederland",
      ["Het zijn landen buiten Europa", "Het zijn landen met een grote haven aan de oceaan", "Het zijn landen zonder eigen industrie"],
      "Nederland exporteert met name naar de buurlanden.", 42),
    M("Wie leverden volgens de opdracht over bron 32 van oudsher snijrozen aan Duitsland?",
      "Nederlandse kwekers", ["Kwekers uit Ecuador", "Duitse kwekers", "Keniaanse kwekers"],
      "Van oudsher leveren Nederlandse kwekers snijrozen aan Duitsland.", 44),
    M("In hoeveel landen heeft Dutch Flower Group volgens de opdracht kantoren?",
      "In drie landen", ["In twee landen", "In vier landen", "In vijf landen"],
      "Het bedrijf heeft kantoren in Kenia, de VS en Duitsland.", 44),
    M("Dutch Flower Group importeert rozen uit Kenia en exporteert ze naar Duitsland. Welke stap is import en welke export?",
      "Het inkopen van rozen in Kenia is import; het verkopen aan Duitsland is export",
      ["Het inkopen van rozen in Kenia is export; het verkopen aan Duitsland is import, want het gaat om bloemen",
       "Het inkopen van rozen in Kenia en het verkopen aan Duitsland is allebei import",
       "Het inkopen van rozen in Kenia en het verkopen aan Duitsland is allebei export"],
      "Import is invoer uit het buitenland, export is uitvoer naar het buitenland.", 44),
    M("Duitsland is afnemer van Nederlandse snijrozen en van Nederlandse fossiele brandstoffen. Wat laat dit zien?",
      "Dat Duitsland voor Nederland een belangrijke handelspartner voor verschillende producten is",
      ["Dat Duitsland geen eigen bloemen of brandstoffen kan produceren",
       "Dat Nederland alleen met Duitsland handel mag drijven",
       "Dat Duitsland de enige afzetmarkt voor Nederland is"],
      "Duitsland is een belangrijke afzetmarkt voor bloemen en een van de grootste exportpartners.", 43),
    M("Welke berekening geeft de waarde van de export van fossiele brandstoffen uit een totale export van 627 miljard euro en een aandeel van 16 procent?",
      "627 × 0,16", ["627 : 16", "627 × 16", "627 × 1,6"],
      "16 procent is 0,16 keer het totaal; dat is ongeveer 100 miljard euro.", 45),
    M("Welke bewering is onjuist, gezien het voorbeeld van fossiele brandstoffen en snijrozen?",
      "Nederland exporteert alleen producten die het zelf maakt of wint",
      ["Nederland voert sommige producten eerst in en voert ze later gewoon weer uit naar andere landen",
       "Een deel van de export is eerst geïmporteerd",
       "Handelsbedrijven halen producten uit verschillende landen"],
      "Nederland haalt zelf te weinig fossiele brandstoffen uit de grond; en snijrozen worden geïmporteerd en doorverkocht.", 45),
    M("Duitse bloemenhandelaren kopen inmiddels ook snijrozen in Afrikaanse landen. Wat betekent dat voor kwekers die snijrozen aan Duitsland leveren?",
      "Ze krijgen concurrentie van kwekers uit andere landen",
      ["Ze hoeven geen snijrozen meer aan Duitsland te leveren",
       "Ze verkopen voortaan alleen nog in Afrikaanse landen",
       "Ze krijgen een groter aandeel in de Duitse bloemenhandel"],
      "Duitse handelaren importeren snijrozen inmiddels uit andere landen, dus er is meer concurrentie.", 44),
    W("De totale waarde van de Nederlandse export is 627 miljoen euro.", False,
      "Niet waar. Het gaat om 627 miljard euro.", 45),
    W("Kenia importeert veel snijrozen uit Duitsland.", False,
      "Niet waar. Duitse handelaren importeren snijrozen uit Kenia.", 44),
    W("Dutch Flower Group heeft een kantoor in de Verenigde Staten.", True,
      "Waar. Het heeft kantoren in Kenia, de VS en Duitsland.", 44),
    W("Fossiele brandstoffen vormen minder dan een kwart van de Nederlandse export.", True,
      "Waar. Het aandeel is 16 procent.", 45),
    W("ASML exporteert het grootste deel van zijn chipmachines.", True,
      "Waar. Het gaat om 95 procent.", 43),
    I("Duitsland is een belangrijke ____markt voor bloemen.", "afzet",
      "Het is een afzetmarkt.", 44),
    I("Een belangrijke reden voor deze landen is het ideale ____ voor de bloementeelt.", "klimaat",
      "Het klimaat is ideaal.", 44),
    I("Duitse handelaren importeren veel snijrozen uit Kenia en ____.", "Zambia",
      "Ook uit Zambia.", 44),
    I("ASML exporteert ongeveer ____ procent van zijn chipmachines.", "95|vijfennegentig",
      "Dat is 95 procent.", 43),
    O("Leg uit wat het betekent dat Nederland sterk op het buitenland gericht is. Gebruik één voorbeeld met bloemen of chipmachines.",
      ["export/exporteert/exporteren/uitvoer", "import/importeert/importeren/invoer", "afzetmarkt/klanten/kopers"], 2,
      "Nederland importeert en exporteert veel. ASML exporteert 95 procent van zijn chipmachines en Dutch Flower Group importeert rozen uit Kenia om ze naar klanten in Duitsland te exporteren.",
      "Nederland importeert en exporteert veel; bedrijven als ASML hebben vooral klanten in het buitenland.", 43),
    O("Leg uit waarom een bloemenbedrijf als Dutch Flower Group kiest voor kantoren in zowel Kenia als Duitsland.",
      ["klimaat/teelt/kwekers", "afzetmarkt/verkopen/klanten"], 2,
      "In Kenia is het klimaat ideaal voor de teelt van rozen. In Duitsland zit een grote afzetmarkt met klanten die de rozen kopen.",
      "Kenia heeft een ideaal klimaat voor de teelt; Duitsland is een belangrijke afzetmarkt.", 44)
])
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('ak_h1_5_extra2_seed_311')
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        t = [v["type"] for v in vr]
        assert (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (9, 5, 4, 2), (nr, t)
        assert sum(1 for v in vr if v["type"] == "waaronwaar" and v["antwoord"] is False) >= 2
        for v in vr:
            if v['type']=='open':
                q=v['vraag'].lower(); m=v['modelantwoord'].lower()
                assert v['minTreffers']<=len(v['sleutelwoorden'])
                assert sum(any(a in m for a in g.lower().split('/')) for g in v['sleutelwoorden'])==len(v['sleutelwoorden']), (nr,v['vraag'])
                assert not any(a in q for g in v['sleutelwoorden'] for a in g.lower().split('/')), (nr,v['vraag'])
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        print(f"examen_{nr}: {len(vr)} vragen, juiste optie langste {n}/{tot}")
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {
            "id": f"ex-h3-ak-{nr}",
            "hoofdstuk": 1,
            "paragraaf": "1.5",
            "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
            "titel": f"Toets {nr} — §1.5 {sub}",
            "vak": "Aardrijkskunde · HAVO 3 (H1)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        pad = os.path.join(ROOT, f"examen_{nr}.js")
        kop = f"// Aardrijkskunde HAVO 3 · Toets {nr} (§1.5 {sub})\n"
        schrijf(pad, kop, "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")


if __name__ == '__main__':
    main()
