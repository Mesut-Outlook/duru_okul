#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.5 Rol van Nederland in de wereldhandel (extra toetsen 102–105).
Schrijft havo3/aardrijkskunde/js/data/examen_102..105.js (ex-h3-ak-102..105).
10 MC, 5 Waaronwaar, 3 Invul, 2 Open.
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
102: ("Mondiale positie, mainports & doorvoer", "🚢", [
    M("Welke twee andere landen staan samen met Nederland al jarenlang in de top 3 van de globaliseringsindex?",
      "Zwitserland en België",
      ["Duitsland en het Verenigd Koninkrijk",
       "Frankrijk en de Verenigde Staten",
       "Noorwegen en het uitgestrekte Canada"],
      "Nederland staat samen met Zwitserland en België in de top 3 van de globaliseringsindex.", 42),
    M("Wat betekent het als een land zeer hoog scoort op de globaliseringsindex?",
      "Dat het land economisch, sociaal en politiek heel sterk verbonden is met het buitenland",
      ["Dat het land economisch volledig zelfvoorzienend is en principieel vrijwel geen goederen uit het buitenland importeert",
       "Dat het land over de grootste oppervlakte en de meeste inwoners ter wereld beschikt",
       "Dat alle binnenlandse bedrijven verplicht eigendom zijn van buitenlandse investeerders"],
      "De index meet hoe sterk een land met het buitenland verbonden is.", 42),
    M("Welke positie neemt de haven van Amsterdam in binnen Europa wat betreft de overslag van handelswaar?",
      "De vierde grootste haven van Europa",
      ["De allergrootste haven van Europa",
       "De tiende grootste haven van Europa",
       "De vijftigste haven op de ranglijst"],
      "Hoewel kleiner dan Rotterdam, is de haven van Amsterdam de vierde haven van Europa.", 42),
    M("Waarom worden grote logistieke knooppunten zoals de haven van Rotterdam en Schiphol 'mainports' genoemd?",
      "Omdat zij fungeren als onmisbare overslagpunten voor internationale stromen van goederen en passagiers",
      ["Omdat zij uitsluitend goederen en ruwe grondstoffen overladen die specifiek bestemd zijn voor de Nederlandse binnenlandse markt",
       "Omdat zij volledig worden gefinancierd door donaties van de Verenigde Naties en de Wereldbank",
       "Omdat er alleen vrachtwagens mogen rijden die rijden op bio-brandstof en groene stroom"],
      "Een mainport is een belangrijk internationaal knooppunt voor goederen- of passagiersstromen.", 42),
    M("Wat gebeurt er met een groot deel van de goederen die in de havens van Rotterdam en Amsterdam binnenkomen?",
      "Zij worden direct doorgevoerd naar andere landen binnen het Europese achterland",
      ["Zij worden allemaal binnen de provincie Zuid-Holland geconsumeerd door de bevolking",
       "Zij worden ter plekke verbrand om elektriciteit op te wekken voor de zware industrie",
       "Zij worden voor minstens tien jaar opgeslagen in ondergrondse bunkers bij Schiphol"],
      "Nederland fungeert als distributieland: ingevoerde goederen worden doorgevoerd naar Europa.", 42),
    M("Hoeveel landen zijn er ter wereld groter dan Nederland als je kijkt naar de totale landoppervlakte?",
      "132 landen",
      ["Precies 28 verschillende landen",
       "Precies 70 soevereine landen",
       "Slechts 3 Europese buurlanden"],
      "132 landen zijn groter in oppervlakte, en meer dan 70 hebben een grotere bevolking.", 42),
    M("Op welke plaats staat Nederland op de mondiale ranglijst als je kijkt naar de omvang van het totale bbp?",
      "Op plek 28",
      ["Op plek 3",
       "Op plek 70",
       "Op plek 132"],
      "Nederland staat op plek 28 van de wereldranglijst qua totale bbp.", 42),
    M("Welk kenmerk van de Nederlandse economie verklaart de hoge notering op de globaliseringsindex?",
      "Nederland heeft een open economie die van oudsher sterk gericht is op internationale handel",
      ["Nederland weigert principieel om goederen van buiten de Europese Unie te importeren",
       "Nederland heft de allerhoogste invoerrechten van alle ontwikkelde industriële economieën",
       "Nederland verbiedt buitenlandse multinationals om vestigingen op zijn grondgebied te openen"],
      "De open en internationaal georiënteerde economie zorgt voor een zeer hoge score op de index.", 42),
    M("Naar welke groep landen exporteert Nederland het grootste deel van zijn handelsgoederen?",
      "Naar de directe Europese buurlanden, met name Duitsland en België",
      ["Naar afgelegen en kleinschalige eilandstaten in het Caribisch gebied en het zuiden van Oceanië",
       "Uitsluitend naar Centraal-Afrikaanse ontwikkelingslanden",
       "Vrijwel alleen naar Latijns-Amerikaanse landbouwstaten"],
      "De export van Nederland is vooral gericht op buurlanden in Europa.", 42),
    M("Wat is de rol van Schiphol in de Nederlandse economie?",
      "Schiphol functioneert als mainport voor internationaal passagiers- en hoogwaardig luchtvrachtverkeer",
      ["Schiphol dient uitsluitend als opslagplaats voor overtollige ruwe aardolie en steenkool",
       "Schiphol is wettelijk uitsluitend bestemd voor kleinschalige binnenlandse vluchten tussen Amsterdam, Rotterdam en Eindhoven",
       "Schiphol is een militair vliegveld waar geen civiele vracht mag worden overgeslagen"],
      "Luchthaven Schiphol is een belangrijke mainport die Nederland verbindt met de hele wereld.", 42),
    W("Er zijn meer dan honderd landen die qua oppervlakte groter zijn dan Nederland.", True, "Waar. Er zijn 132 landen groter dan Nederland als je naar de oppervlakte kijkt.", 42),
    W("De haven van Amsterdam behoort qua overgezette handelswaar niet eens tot de top 20 van Europa.", False,
      "Niet waar. De haven van Amsterdam is de vierde grootste haven van Europa.", 42),
    W("In Nederland zijn er meer dan zeventig landen met een grotere bevolking.", True,
      "Waar. Qua bevolking zijn er meer dan 70 landen groter dan Nederland.", 42),
    W("Een mainport is een kleine regionale haven die alleen lokale vissersboten ontvangt.", False,
      "Niet waar. Een mainport is een belangrijk knooppunt voor internationale handel en transport.", 42),
    W("Veel goederen die in Rotterdam binnenkomen, worden doorgevoerd naar Duitsland en andere Europese landen.", True,
      "Waar. Nederland heeft een belangrijke doorvoerfunctie voor het Europese achterland.", 42),
    I("Een belangrijke haven of luchthaven voor de internationale wereldhandel noem je een ____.", "mainport",
      "Dat noem je een mainport.", 42),
    I("Op de wereldranglijst van het totale bbp staat Nederland op plek ____.", "28|achtentwintig",
      "Nederland staat op plek 28.", 42),
    I("De rangorde die meet hoe sterk een land met het buitenland verbonden is, heet de globaliserings____.", "index",
      "Dat heet de globaliseringsindex.", 42),
    O("Leg uit wat een brainport is. Gebruik de regio rond Eindhoven als voorbeeld.", ["kennis/kenniseconomie", "hightech/technische/technologie", "universiteit/onderzoek"], 2, "Een brainport is een gebied dat een grote rol speelt in de kenniseconomie, met veel hightechbedrijven, universiteiten en onderzoeksinstituten. Rond Eindhoven zitten bijvoorbeeld ASML en de Technische Universiteit.", "Brainport = gebied met een grote rol in de kenniseconomie: veel hightechbedrijven, universiteiten en onderzoeksinstituten (begrippenlijst p. 52).", 42),
    O("Noem twee Nederlandse mainports die essentieel zijn voor de internationale handel.", ["haven van Rotterdam/Rotterdam", "Schiphol/luchthaven Schiphol"], 2,
      "De haven van Rotterdam en luchthaven Schiphol.",
      "Rotterdam en Schiphol.", 42)
]),

103: ("Brainport Eindhoven & hightechindustrie", "💡", [
    M("Welke stad of regio in Nederland wordt ook wel de 'slimste regio ter wereld' genoemd?",
      "De regio Brainport Eindhoven",
      ["De regio Zuid-Limburg rondom Heerlen",
       "De regio van de Waddeneilanden",
       "Het landelijke gebied van de Achterhoek"],
      "Eindhoven wordt internationaal vaak de slimste regio ter wereld genoemd.", 42),
    M("Met welke onderwijsinstelling werkt het bedrijfsleven in de regio Eindhoven nauw samen?", "De Technische Universiteit Eindhoven", ["De Universiteit van Amsterdam", "De Hogeschool Rotterdam", "De Universiteit Leiden"], "In de regio Eindhoven is er een hechte samenwerking tussen het bedrijfsleven en de Technische Universiteit, gesteund door de overheid.", 43),
    M("Welk percentage van de geavanceerde chipmachines die ASML bouwt, wordt geëxporteerd naar het buitenland?",
      "Ongeveer 95 procent",
      ["Precies 10 procent",
       "Ongeveer 50 procent",
       "Slechts 5 procent"],
      "ASML exporteert maar liefst 95% van zijn geproduceerde machines wereldwijd.", 43),
    M("Wat is een belangrijke vestigingsplaatsfactor voor hightechbedrijven in de regio Eindhoven?",
      "De aanwezigheid van aanvullende bedrijven en onderzoeksinstituten op de High Tech Campus",
      ["De directe nabijheid van omvangrijke ondergrondse steenkoolmijnen en zware ijzerertsvoorraden in de bodem",
       "Het feit dat de lonen voor ingenieurs er lager liggen dan in Zuidoost-Azië",
       "De directe ligging aan een diepe zeehaven voor gigantische containerschepen"],
      "Bedrijven vullen elkaar aan en werken samen op broedplaatsen zoals de High Tech Campus.", 42),
    M("Hoeveel mensen wonen er in een straal van 150 kilometer rondom Eindhoven met een hoge koopkracht?",
      "Circa 40 miljoen mensen",
      ["Circa 2 miljoen mensen",
       "Minder dan 500.000 mensen",
       "Meer dan 200 miljoen mensen"],
      "In een straal van 150 km rond Eindhoven wonen 40 miljoen mensen met een bovengemiddelde koopkracht.", 43),
    M("Welke vorm van samenwerking vormt de kracht van de hightechsector in Brainport Eindhoven?",
      "Een hechte samenwerking tussen het innovatieve bedrijfsleven, de Technische Universiteit en de overheid",
      ["Een strategische samenwerking tussen traditionele Brabantse akkerbouwers en de Europese Centrale Bank in Frankfurt",
       "Een verplicht verbond waarbij de overheid alle aandelen van chipfabrikanten opkoopt",
       "Een geheim militair pact tussen de provincie Noord-Brabant en buitenlandse legers"],
      "De samenwerking tussen overheid, universiteit (TU/e) en bedrijfsleven (triple helix) is cruciaal.", 43),
    M("Wat verstaat men onder het begrip 'hoogwaardige maakindustrie'?",
      "Industriële productie door vernieuwende hightechbedrijven die veel kennis en technologie toepassen",
      ["Het ambachtelijk en handmatig spinnen en weven van katoenen stoffen in kleinschalige Brabantse dorpswerkplaatsen",
       "De grootschalige winning van grind en zand langs rivieroevers voor de woningbouw",
       "Het louter overladen van containers in zeehavens zonder enige bewerking van goederen"],
      "Hoogwaardige maakindustrie draait om kennisintensieve, technologische fabricage.", 42),
    M("Waarom bracht de president van Zuid-Korea samen met koning Willem-Alexander een officieel bezoek aan ASML?",
      "Omdat Zuid-Koreaanse elektronicagiganten zoals Samsung sterk afhankelijk zijn van de chipmachines van ASML",
      ["Omdat de Zuid-Koreaanse overheid de import van chipmachines uit Nederland officieel wilde verbieden op de eigen binnenlandse markt",
       "Omdat men in Eindhoven een nieuwe fabriek voor traditionele landbouwtractoren wilde openen",
       "Omdat de Zuid-Koreaanse president wilde investeren in Brabantse bloembollenteelt"],
      "Zuid-Korea is een grote producent van microchips en heeft de machines van ASML hard nodig.", 42),
    M("Welke bekende multinational legde historisch de basis voor de technologische ontwikkeling van Eindhoven?",
      "Philips",
      ["Shell",
       "Unilever",
       "AkzoNobel"],
      "Philips begon in Eindhoven met gloeilampen en legde de basis voor de elektronica- en hightechregio.", 42),
    M("Wat is een 'broedplaats' in de context van Brainport Eindhoven?",
      "Een plek van onderzoek en vernieuwing waar innovatieve bedrijven en onderzoekers elkaar ontmoeten en versterken",
      ["Een streng beveiligd provinciaal natuurgebied waar kwetsbare en zeldzame weidevogels beschermd worden tegen natuurlijke vijanden",
       "Een kantoorgebouw waarin uitsluitend buitenlandse ambassadeurs mogen vergaderen",
       "Een opslagloods voor overtollige landbouwmachines en afgedankte fabrieksapparatuur"],
      "Een broedplaats (zoals de High Tech Campus) stimuleert innovatie en kruisbestuiving tussen bedrijven.", 42),
    W("ASML exporteert ongeveer 95 procent van al zijn machines naar klanten buiten Nederland.", True,
      "Waar. Bijna de gehele productie van ASML gaat naar chipfabrikanten wereldwijd.", 43),
    W("In een straal van 150 kilometer rondom Eindhoven wonen slechts 5 miljoen potentiële consumenten.", False,
      "Niet waar. Binnen die straal wonen maar liefst 40 miljoen koopkrachtige mensen.", 43),
    W("De Technische Universiteit Eindhoven werkt nauw samen met hightechbedrijven in de regio.", True,
      "Waar. Deze samenwerking levert goed opgeleid personeel en gezamenlijk onderzoek op.", 43),
    W("Brainport Eindhoven dankt zijn succes vooral aan het handmatig in elkaar zetten van goedkope kleding.", False,
      "Niet waar. Het succes berust op kennis, innovatie en hoogwaardige hightechproducten.", 42),
    W("Bedrijven als ASML, DAF en Philips worden beschouwd als toonaangevende multinationals.", True,
      "Waar. Dit zijn bedrijven met vestigingen en afzetmarkten in vele landen.", 42),
    I("Het hightechbedrijf in Veldhoven dat wereldleider is in chipmachines heet ____.", "ASML",
      "Dat is ASML.", 43),
    I("Een gebied met een hoge concentratie aan hightechbedrijven en kennisinstellingen noem je een ____port.", "brain",
      "Dat is een brainport.", 42),
    I("Een plek van onderzoek en vernieuwing waar bedrijven elkaar aanvullen heet een ____plaats.", "broed",
      "Dat heet een broedplaats.", 42),
    O("Noem twee gunstige vestigingsplaatsfactoren voor hightechbedrijven in de regio Brainport Eindhoven.", ["aanvullende/broedplaats/campus", "opgeleid/universiteit/afzetmarkt"], 2,
      "Aanwezigheid van aanvullende bedrijven (broedplaatsen zoals High Tech Campus) en een goed opgeleide technische beroepsbevolking.",
      "Aanwezigheid van broedplaatsen en een goed opgeleide beroepsbevolking.", 42),
    O("Waarom is de afzetmarkt van Brainport Eindhoven zo gunstig gelegen?", ["150 kilometer/straal", "40 miljoen mensen/hoge koopkracht"], 2,
      "Omdat er binnen een straal van 150 kilometer rondom Eindhoven maar liefst 40 miljoen mensen met een hoge koopkracht wonen.",
      "Binnen 150 km wonen 40 miljoen mensen met een hoge koopkracht.", 43)
]),

104: ("Welvaart, ongelijkheid & armoede", "📊", [
    M("Wat betekent een Gini-coëfficiënt van 0,26 voor Nederland in vergelijking met andere landen?",
      "Dat de sociale ongelijkheid in Nederland relatief laag is vergeleken met veel andere landen",
      ["Dat Nederland officieel geregistreerd staat als het allerarmste land van de gehele Europese Unie",
       "Dat alle inkomensverschillen in Nederland volledig zijn opgeheven",
       "Dat meer dan de helft van de bevolking onder de absolute armoedegrens leeft"],
      "Een Gini-score van 0,26 wijst op een relatief lage inkomensongelijkheid.", 43),
    M("Wat verstaat men in een welvarend land als Nederland onder 'relatieve armoede'?",
      "Mensen hebben moeite om mee te doen in de maatschappij of noodzakelijke uitgaven zoals energie te betalen",
      ["Mensen hebben door extreme voedselschaarste letterlijk geen enkele maaltijd meer en sterven massaal de hongerdood",
       "Mensen hebben geen eigen tropisch vakantie-eiland in de Stille Oceaan",
       "Mensen weigeren principieel om met briefgeld of pinpas te betalen"],
      "Relatieve armoede betekent dat men financieel achterblijft bij de heersende levensstandaard.", 43),
    M("In welk type gebieden in Nederland zijn de verschillen tussen de rijkste en armste wijken het sterkst gegroeid?",
      "In de grote steden",
      ["In kleine plattelandsdorpen in Drenthe",
       "Uitsluitend op de Waddeneilanden",
       "In de open heidegebieden van de Veluwe"],
      "Met name in de grote steden zijn de contrasten tussen rijke en arme buurten toegenomen.", 43),
    M("Welk maatschappelijk verschijnsel illustreert dat sommige groepen in Nederland moeite hebben om rond te komen?",
      "De toename van het aantal mensen dat noodgedwongen gebruikmaakt van de voedselbank",
      ["De opvallende en plotselinge daling van het totale aantal verkochte tweedehands fietsen in stadscentra",
       "Het feit dat alle middelbare scholen hun deuren definitief hebben gesloten",
       "Het verbod van de overheid op het bezit van meer dan één spaarrekening"],
      "De groeiende vraag bij voedselbanken wijst op financiële nood bij kwetsbare huishoudens.", 43),
    M("Waarom maakt de overheid zich zorgen over toenemende armoede en sociale ongelijkheid?",
      "Omdat grote ongelijkheid kan leiden tot maatschappelijke spanningen die de economische groei belemmeren",
      ["Omdat vermogende en hoogopgeleide burgers dan door de overheid verplicht worden om te verhuizen naar het buitenland",
       "Omdat er dan te weinig luxe jachten in de jachthavens kunnen aanmeren",
       "Omdat buitenlandse toeristen weigeren musea in de grote steden te bezoeken"],
      "Sociale spanningen door ongelijkheid tasten de stabiliteit en economische groei aan.", 43),
    M("Op welke manieren probeert de Nederlandse overheid sociale ongelijkheid actief tegen te gaan?",
      "Door te investeren in goede gezondheidszorg, kwalitatief onderwijs en gelijke kansen voor iedereen",
      ["Door het wettelijk opleggen van een eenmalige dwangboete van negentig procent op alle vormen van particulier spaargeld",
       "Door alle particuliere ondernemingen en supermarkten te nationaliseren",
       "Door het verplicht stellen van hetzelfde salaris voor alle beroepen in het land"],
      "Investeringen in onderwijs en zorg moeten gelijke ontwikkelingskansen bieden.", 43),
    M("Wat is kenmerkend voor de gemiddelde welvaart in Nederland vergeleken met het wereldwijde gemiddelde?",
      "Nederland heeft een hoog gemiddeld besteedbaar inkomen en een lage werkloosheid",
      ["Nederland heeft de hoogste werkloosheid van alle landen in West-Europa",
       "Het doorsnee inkomen van Nederlanders ligt onder het niveau van ontwikkelingslanden",
       "Nederland kent helemaal geen werkende bevolking meer door verregaande automatisering"],
      "Over het geheel genomen is Nederland een welvarend land met hoge inkomens en weinig werkloosheid.", 43),
    M("Wat betekent het begrip 'sociale ongelijkheid' precies in de aardrijkskunde?",
      "Ongelijke verdeling van welvaart, kansen en privileges tussen verschillende groepen mensen",
      ["Het statistische verschil in gemiddelde jaartemperatuur tussen stedelijke agglomeraties en het omringende platteland",
       "Het aantal verschillende talen dat binnen één land officieel gesproken wordt",
       "Het verschil in reistijd tussen de Randstad en de noordelijke provincies"],
      "Sociale ongelijkheid betreft verschillen in inkomen, welvaart en ontwikkelingskansen.", 43),
    M("Waarom profiteert niet iedere inwoner van Nederland evenveel van de internationale handelsrol van ons land?",
      "Omdat de economische opbrengsten vooral terechtkomen bij hoogopgeleiden en aandeelhouders van multinationals",
      ["Omdat de nationale overheid alle belastinginkomsten en handelswinsten direct integraal overmaakt naar buurland Duitsland",
       "Omdat alleen mensen die vloeiend Chinees spreken een baan in de handel mogen aannemen",
       "Omdat alle producten die in Rotterdam binnenkomen gratis worden uitgedeeld aan toeristen"],
      "Niet iedereen beschikt over de gevraagde opleiding of vaardigheden om mee te profiteren.", 42),
    M("Welke rekening vormt voor huishoudens in relatieve armoede vaak een acuut probleem?",
      "De maandelijkse energierekening voor gas en elektriciteit",
      ["De jaarlijkse belastingaanslag op het bezit van een privé-helikopter",
       "De verplichte bijdrage aan de exploitatie van een commerciële golfbaan",
       "De abonnementskosten voor het bezoeken van buitenlandse operatheaters"],
      "Veel huishoudens in armoede ervaren acute stress door hoge kosten voor energie.", 43),
    W("In Nederland heeft de Gini-coëfficiënt een waarde van 0,26.", True,
      "Waar. Dit geeft aan dat de inkomensverschillen relatief beperkt zijn.", 43),
    W("In Nederland bestaat helemaal geen armoede meer omdat iedereen overvloedig rijk is.", False,
      "Niet waar. Er is nog steeds sprake van relatieve armoede en groeiend voedselbankgebruik.", 43),
    W("Grote sociale ongelijkheid kan leiden tot spanningen die de economische ontwikkeling schaden.", True,
      "Waar. Spanningen en wantrouwen belemmeren de stabiliteit van de samenleving.", 43),
    W("De Nederlandse overheid investeert onder meer in onderwijs om kansenongelijkheid te bestrijden.", True,
      "Waar. Goed onderwijs is een belangrijke hefboom voor gelijke kansen.", 43),
    W("In grote steden zijn de verschillen tussen de rijkste en armste wijken de afgelopen jaren geheel verdwenen.", False,
      "Niet waar. Juist in grote steden zijn de contrasten tussen wijken vaak toegenomen.", 43),
    I("Het getal tussen 0 en 1 dat de mate van inkomensongelijkheid weergeeft heet de ____-coëfficiënt.", "Gini|gini",
      "Dat is de Gini-coëfficiënt.", 43),
    I("Armoede in een rijk land waarbij mensen achterblijven bij de algemene levensstandaard heet ____ armoede.", "relatieve|relatief",
      "Dat heet relatieve armoede.", 43),
    I("Een organisatie die gratis voedselpakketten verstrekt aan gezinnen in nood is de ____bank.", "voedsel",
      "Dat is de voedselbank.", 43),
    O("Waarom leidt toenemende sociale ongelijkheid volgens economen en geografen tot problemen?", ["spanning/onrust", "belemmer/groei"], 2,
      "Het kan leiden tot sociale spanningen en die belemmeren de gezonde groei van economie en samenleving.",
      "Ongelijkheid leidt tot sociale spanningen en remt de economische groei.", 43),
    O("Noem twee terreinen waarin de Nederlandse overheid investeert om kansenongelijkheid terug te dringen.", ["onderwijs/scholen", "gezondheidszorg/zorg/gelijke kansen"], 2,
      "De overheid investeert in kwalitatief onderwijs en goede gezondheidszorg.",
      "Onderwijs en gezondheidszorg.", 43)
]),

105: ("Handelsstromen, grondstoffen & bronnen", "📈", [
    M("Wat is volgens bron 34 het aandeel van fossiele brandstoffen in de totale Nederlandse exportwaarde?",
      "Ongeveer 16 procent van de totale exportwaarde",
      ["Slechts 1 procent van de totale exportwaarde",
       "Meer dan 80 procent van de totale exportwaarde",
       "Precies 50 procent van de totale exportwaarde"],
      "Volgens bron 34 bestaat 16% van de Nederlandse export uit fossiele brandstoffen.", 43),
    M("Hoe kan het dat fossiele brandstoffen 16 procent van de export vormen, terwijl Nederland die nauwelijks zelf wint?",
      "Nederland importeert ruwe aardolie via Rotterdam, raffineert dit en exporteert de verwerkte brandstoffen weer",
      ["Nederland heeft recentelijk onverwacht gigantische nieuwe reserves aan aardolie en schaliegas ontdekt onder de zandgronden van de Veluwe",
       "Nederland koopt op papier alle olievoorraden van Saudi-Arabië op zonder transport",
       "Het betreft een rekenfout van het Centraal Bureau voor de Statistiek die nooit gecorrigeerd is"],
      "Nederland importeert ruwe olie, bewerkt die in raffinaderijen en voert brandstoffen door.", 45),
    M("Welke twee landen zijn volgens bron 34 veruit de grootste exportpartners van Nederland voor fossiele brandstoffen?",
      "Duitsland (19,4%) en België (3,3%)",
      ["De grote wereldmachten China en de Verenigde Staten",
       "De opkomende economieën Brazilië en Zuid-Afrika",
       "De geïndustrialiseerde eilandstaten Japan en Australië"],
      "Duitsland en België zijn de belangrijkste afnemers van onze geraffineerde brandstoffen.", 43),
    M("Uit welke landen importeren Duitse handelaren volgens bron 32 veel snijrozen?",
      "Uit Oost-Afrikaanse landen zoals Kenia en Zambia",
      ["Uitsluitend uit de noordelijke toendra's van Noorwegen",
       "Alleen uit woestijngebieden in Noord-Afrika",
       "Vrijwel geheel uit Alaska en Groenland"],
      "Kenia en Zambia hebben een ideaal klimaat voor de teelt van snijrozen.", 42),
    M("Waarom is een bedrijf als Dutch Flower Group een typische multinational in de sierteelt?",
      "Het heeft vestigingen en kantoren in meerdere landen zoals Kenia, de VS, Duitsland en Nederland",
      ["Het bedrijf kweekt en oogst al zijn snijbloemen strikt genomen uitsluitend in één enkele familieglastuinbouwkas in het Westland",
       "Het is volledig in handen van de Verenigde Naties en maakt geen enkele winst",
       "Het weigert bloemen per vliegtuig of vrachtwagen over landsgrenzen te vervoeren"],
      "Een multinational heeft kantoren, vestigingen en productie in meerdere landen.", 44),
    M("Welke eenheid wordt in bron 32 gebruikt om de Duitse import van snijrozen aan te geven?",
      "In miljoenen stuks",
      ["In miljarden euro's",
       "In duizenden kilogrammen",
       "In honderdtallen vazen"],
      "Bron 32 geeft de Duitse import van snijrozen weer in miljoenen stuks.", 42),
    M("Naar welk werelddeel exporteert Nederland het grootste deel van zijn geavanceerde chipmachines volgens bron 33?",
      "Naar Azië (waaronder Taiwan, Zuid-Korea en China)",
      ["Naar Afrika ten zuiden van de Sahara",
       "Uitsluitend naar Zuid-Amerikaanse landen",
       "Naar Antarctica voor wetenschappelijke expedities"],
      "De grootste chipfabrikanten (zoals TSMC en Samsung) bevinden zich in Azië.", 43),
    M("Waarom is het klimaat in Kenia en Ethiopië zo gunstig voor de grootschalige rozenteelt?",
      "De combinatie van veel zonuren, gunstige temperaturen en voldoende hoogland voor een stabiel klimaat",
      ["Omdat er op de equatoriale hoogvlaktes het hele jaar door een strenge vorst heerst die alle schadelijke insecten en schimmels doodt",
       "Omdat er uitsluitend 's nachts zonlicht schijnt waardoor bloemen sneller groeien",
       "Omdat rozenstruiken alleen groeien op actieve vulkanische lavastromen"],
      "Het equatoriale hooglandklimaat biedt ideale natuurlijke groeiomstandigheden voor rozen.", 44),
    M("Wat illustreert de route van snijrozen van Kenia via Nederland naar Duitsland over de wereldeconomie?",
      "De sterke mondiale handelsverwevenheid waarbij Nederland als centrale handels- en doorvoerdraaischijf fungeert",
      ["Dat kwetsbare bederfelijke consumptiegoederen volgens Europese wetgeving uitsluitend over land per goederentrein vervoerd mogen worden",
       "Dat Duitsland weigert om rechtstreeks handelsovereenkomsten met Afrika te sluiten",
       "Dat snijbloemen na transport pas na tien jaar verkocht hoeven te worden in de winkel"],
      "Nederland fungeert als logistieke draaischijf (hub) in mondiale waardeketens.", 44),
    M("Wat is de totale waarde van de Nederlandse goederenexport volgens de gegevens in bron 34?",
      "Circa 627 miljard euro",
      ["Precies 50 miljard euro",
       "Minder dan 10 miljard euro",
       "Ruim 5000 miljard euro"],
      "In bron 34 wordt de totale exportwaarde van Nederland vermeld als € 627 miljard.", 45),
    W("In bron 32 wordt de Duitse import van snijrozen uitgedrukt in miljoenen.", True,
      "Waar. De getallen geven aantallen in miljoenen weer.", 42),
    W("Nederland haalt alle geëxporteerde aardolie zelf uit de Nederlandse bodem.", False,
      "Niet waar. Nederland importeert ruwe olie via Rotterdam en verwerkt deze in raffinaderijen.", 45),
    W("Duitsland is een van de belangrijkste exportbestemmingen voor Nederlandse brandstoffen.", True,
      "Waar. Duitsland neemt bijna 20 procent van deze export af.", 43),
    W("Chipmachines van ASML worden voornamelijk verkocht aan klanten binnen de Benelux.", False,
      "Niet waar. ASML exporteert 95 procent wereldwijd, vooral naar grote producenten in Azië en de VS.", 43),
    W("Kenia en Zambia exporteren snijrozen mede dankzij hun gunstige teeltklimaat.", True,
      "Waar. Het klimaat is uitermate geschikt voor de rozenteelt.", 44),
    I("Volgens bron 34 bestaat ongeveer ____ procent van de Nederlandse export uit fossiele brandstoffen.", "16|zestien",
      "Dat is 16 procent.", 43),
    I("Een bloemenbedrijf met vestigingen in Kenia, Nederland en Duitsland is een multi____.", "national",
      "Dat is een multinational.", 44),
    I("De grootste afnemers van Nederlandse chipmachines bevinden zich op het continent ____.", "Azië|Azie",
      "Dat is Azië.", 43),
    O("Leg met een getal uit het boek uit of de sociale ongelijkheid in Nederland groot of klein is.", ["0,26/0.26", "gini", "laag/klein"], 3, "De Gini-coëfficiënt van Nederland is 0,26. Dat is laag, dus de sociale ongelijkheid is klein.", "Nederland heeft een Gini-coëfficiënt van 0,26: de sociale ongelijkheid is laag.", 43),
    O("Waarom fungeert een bedrijf als Dutch Flower Group als spil in de sierteeltketen?", ["importeert/import/invoer", "kenia/afrika/lagelonenland", "exporteert/export/duitsland"], 2,
      "Het importeert snijrozen uit lagelonenlanden zoals Kenia en exporteert deze door naar afzetmarkten zoals Duitsland.",
      "Het importeert bloemen uit Afrika en exporteert ze naar Duitsland en Europa.", 44)
])
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('ak_h1_5_extra_seed_77')
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        t = [v["type"] for v in vr]
        assert (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (10, 5, 3, 2), (nr, t)
        assert sum(1 for v in vr if v["type"] == "waaronwaar" and v["antwoord"] is False) >= 2
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        print(f"examen_{nr}: {len(vr)} vragen, juiste optie langste {n}/{tot}")
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {
            "id": f"ex-h3-ak-{nr}",
            "hoofdstuk": 1,
            "paragraaf": "1.5",
            "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
            "titel": f"Proeftoets {nr} — §1.5 {sub}",
            "vak": "Aardrijkskunde · HAVO 3 (H1)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        pad = os.path.join(ROOT, f"examen_{nr}.js")
        kop = f"// Aardrijkskunde HAVO 3 · Proeftoets {nr} (§1.5 {sub})\n"
        schrijf(pad, kop, "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")


if __name__ == '__main__':
    main()
