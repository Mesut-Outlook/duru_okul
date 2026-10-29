#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.4 Rol van Europa in de wereldhandel (extra toetsen 98–101).
Schrijft havo3/aardrijkskunde/js/data/examen_98..101.js (ex-h3-ak-98..101).
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
98: ("De Europese Unie: interne markt & handelsblok", "🇪🇺", [
    M("Hoeveel lidstaten telt de Europese Unie momenteel volgens het leerboek?",
      "27 Europese lidstaten",
      ["12 Europese lidstaten in totaal",
       "45 Europese lidstaten in totaal",
       "Precies 50 soevereine lidstaten"],
      "Tegenwoordig bestaat de EU uit 27 lidstaten die economisch en politiek samenwerken.", 38),
    M("Waarom is de Europese Unie officieel geen lid van de G7, maar neemt zij wel deel?",
      "Omdat de G7 een groep van individuele landen is en de EU een samenwerkingsverband vormt",
      ["Omdat de EU principieel weigert deel te nemen aan economische besprekingen met de Verenigde Staten en Canada",
       "Omdat de EU niet beschikt over een eigen gemeenschappelijke munt",
       "Omdat de G7 alleen toegankelijk is voor landen uit het zuidelijk halfrond"],
      "De G7 is een groep van zeven landen; de EU is geen land maar schuift wel aan bij bijeenkomsten.", 38),
    M("Waarmee begon de Europese economische samenwerking na de Tweede Wereldoorlog?",
      "Met het reguleren van de onderlinge handel in steenkool en ijzererts tussen zes landen",
      ["Met een gezamenlijk militair verdedigingsverdrag tegen piraterij en smokkel op de gehele Atlantische Oceaan",
       "Met de invoering van de euro als giraal betaalmiddel in alle Europese steden",
       "Met een verbod op alle import van graan en textiel uit Aziatische landen"],
      "Zes landen (waaronder Nederland) begonnen met samenwerking in steenkool en staal/ijzererts.", 38),
    M("Aan welke drie strenge voorwaarden moeten kandidaat-lidstaten voldoen om toe te mogen treden tot de EU?",
      "Voorwaarden op het gebied van financiën, corruptiebestrijding en democratie",
      ["Voorwaarden op het gebied van taalvaardigheid, godsdienst en legeromvang",
       "Het bezitten van grote eigen voorraden aardgas en steenkool in de bodem",
       "Het verplicht invoeren van de Duitse taal in het basis- en voortgezet onderwijs"],
      "Kandidaat-lidstaten moeten financieel gezond zijn, corruptie tegengaan en een stabiele democratie hebben.", 38),
    M("Welke landen worden in het boek genoemd als kandidaat-lidstaten die graag willen toetreden tot de EU?",
      "Oekraïne, Turkije en Servië",
      ["Zwitserland, Noorwegen en IJsland",
       "Het Verenigd Koninkrijk, Canada en Japan",
       "Rusland, Wit-Rusland en Kazachstan"],
      "Landen als Oekraïne, Turkije en Servië willen graag toetreden tot de interne markt zonder belemmeringen.", 38),
    M("Wat gebeurde er in 2020 met het lidmaatschap van het Verenigd Koninkrijk?",
      "Het Verenigd Koninkrijk verliet de EU (Brexit) na een referendum waarin een nipte meerderheid voor vertrek stemde",
      ["Het Verenigd Koninkrijk werd voor onbepaalde tijd geschorst omdat het categorisch weigerde om de euro in te voeren",
       "Het Verenigd Koninkrijk fuseerde economisch volledig met de Republiek Ierland",
       "Het Verenigd Koninkrijk nam alle 26 overige lidstaten over als kolonies"],
      "Na het referendum over het lidmaatschap verliet het VK in 2020 definitief de Europese Unie.", 38),
    M("Wat is een belangrijk punt van kritiek van burgers en boeren op het bestuur van de EU?",
      "De besluitvorming verloopt traag en burgers moeten zich houden aan regels waar ze het niet mee eens zijn",
      ["De Europese Commissie heft principieel geen enkele vorm van belasting op buitenlandse luxegoederen",
       "De EU verbiedt inwoners om op vakantie te gaan naar andere lidstaten",
       "De EU dwingt alle boeren om uitsluitend nog snijbloemen te kweken"],
      "Inwoners en boeren klagen over trage besluiten en strenge regels rondom stikstof en duurzaamheid.", 38),
    M("Wat laten de boerenprotesten in 2023 in Brussel (bron 26) zien?",
      "Het verzet van agrariërs tegen strenge Europese milieuregels zoals stikstofmaatregelen",
      ["Een feestelijke viering van het 50-jarig bestaan van het Europees Parlement",
       "Een grootschalig protest tegen de oneerlijke concurrentie door spotgoedkope Noord-Amerikaanse landbouwproducten",
       "Een eis van boeren om alle grenzen binnen Europa met slagbomen af te sluiten"],
      "Boeren uit Nederland, België en Frankrijk protesteerden massaal tegen het Europese stikstofbeleid.", 38),
    M("Welk belangrijk handelsvoordeel hebben bedrijven binnen de Europese Unie?",
      "Vrijhandel en open binnengrenzen zonder invoerrechten of grenscontroles tussen lidstaten",
      ["Gegarandeerde winstuitkeringen die maandelijks door de Europese Centrale Bank worden betaald",
       "Vrijstelling van alle milieuregels en sociale verplichtingen tegenover werknemers",
       "Het recht om zonder vergunning goederen te dumpen op de Aziatische afzetmarkt"],
      "Door het wegnemen van handelsbelemmeringen kunnen goederen vrij tussen lidstaten circuleren.", 38),
    M("Welk welvaartsniveau kenmerkt de 27 lidstaten van de Europese Unie?",
      "Alle 27 lidstaten hebben een gemiddeld of hoog welvaartsniveau",
      ["Alle 27 lidstaten behoren tot de allerarmste ontwikkelingslanden ter wereld",
       "Twaalf lidstaten zijn extreem rijk en de overige vijftien leven in absolute armoede",
       "De welvaart is in iedere Europese stad en streek exact tot op de euro gelijk verdeeld"],
      "De 27 landen van de EU zijn allemaal landen met een gemiddeld tot hoog welvaartsniveau.", 38),
    W("De Europese Unie is een soevereine staat met een eigen zetel als stemgerechtigd land in de G7.", False,
      "Niet waar. De EU is een samenwerkingsverband van 27 landen en neemt als organisatie deel aan de G7.", 38),
    W("Inwoners van de EU profiteren van open grenzen en vrij verkeer van goederen tussen lidstaten.", True,
      "Waar. Handelsbelemmeringen tussen de 27 lidstaten zijn weggenomen.", 38),
    W("Alle landen op het Europese continent zijn automatisch volwaardig lid van de EU.", False,
      "Niet waar. Landen moeten eerst voldoen aan strenge toelatingseisen voor financiën en democratie.", 38),
    W("Het Verenigd Koninkrijk is in 2020 uit de Europese Unie gestapt na een volksraadpleging.", True,
      "Waar. Na de uitslag van het referendum vond de Brexit plaats in 2020.", 38),
    W("Bedrijven binnen de EU ervaren minder strenge duurzaamheidsregels dan bedrijven in China.", False,
      "Niet waar. Europese bedrijven moeten zich juist aan veel strengere milieu- en duurzaamheidsregels houden.", 38),
    I("Het aantal lidstaten van de Europese Unie is momenteel ____.", "27|zevenentwintig",
      "De EU telt 27 lidstaten.", 38),
    I("De groep van zeven grote economisch samenwerkende industrielanden heet de ____.", "G7|G-7",
      "Dat is de G7.", 38),
    I("Het vertrek van het Verenigd Koninkrijk uit de Europese Unie wordt aangeduid als de ____.", "Brexit|brexit",
      "Dit vertrek heet de Brexit.", 38),
    O("Waarom begonnen zes Europese landen oorspronkelijk met economische samenwerking na de oorlog?", ["steenkool/kolen", "ijzererts/staal"], 2,
      "Zij wilden de onderlinge handel in steenkool en ijzererts reguleren om vrede en welvaart te bevorderen.",
      "Om samen te werken op het gebied van steenkool en ijzererts.", 38),
    O("Noem twee kritiekpunten die burgers of bedrijven hebben op het functioneren van de EU.", ["traag/trage", "strenge regels/duurzaamheid/stikstof"], 2,
      "De besluitvorming verloopt vaak traag en bedrijven ervaren strengere regels rondom stikstof en duurzaamheid.",
      "Besluitvorming is traag en men heeft last van strenge regels.", 38)
]),

99: ("Verschuivingen in de Europese industrie", "🏭", [
    M("Wat gebeurde er na 1990 met de zware industrie in veel West-Europese regio's?",
      "Veel mijnen, hoogovens en staalfabrieken moesten sluiten door hevige concurrentie uit lagelonenlanden",
      ["De zware industrie groeide met meer dan driehonderd procent dankzij nieuwe steenkoolvondsten",
       "Alle West-Europese fabrieken werden genationaliseerd door de centrale overheid in Brussel",
       "De zware industrie verhuisde met massale overheidssubsidies direct naar het centrum van wereldsteden zoals Londen en Parijs"],
      "Oude industriegebieden kregen zware klappen door concurrentie uit lagelonenlanden en alternatieve grondstoffen.", 39),
    M("Welke industriële sectoren in West-Europa kregen na 1990 de zwaarste klappen?",
      "Zware industrie (ijzer, staal, scheepsbouw) en arbeidsintensieve textiel- en schoenenbedrijven",
      ["Uitsluitend de hightech chipmachine-industrie, softwareontwikkeling en de geavanceerde ruimtevaartsector",
       "Alleen biologische landbouwbedrijven, kleinschalige kaasboerderijen en gespecialiseerde kasteeltbedrijven",
       "De farmaceutische industrie en fabrikanten van medische robots"],
      "Vooral zware industrie en arbeidsintensieve sectoren zoals textiel verloren de concurrentiestrijd.", 39),
    M("Wat verstaat men in de geografie onder het begrip 'de-industrialisatie'?",
      "De afname van het belang en de werkgelegenheid van de industriële sector in een regio",
      ["Het verplicht slopen van alle kantoorgebouwen ten gunste van landbouwgrond",
       "De overgang van een diensteneconomie naar een economie die uitsluitend op mijnbouw draait",
       "Het volledig verbieden van machines en computers in productieprocessen"],
      "De-industrialisatie is het proces waarbij industriële bedrijvigheid en banen in een gebied sterk afnemen.", 40),
    M("Welk beroemd Duits industriegebied maakte tussen 1965 en 2023 een enorme de-industrialisatie door?",
      "Het Ruhrgebied",
      ["Beieren rondom München",
       "De havenstad Hamburg",
       "Het Zwarte Woud"],
      "In bron 28 zie je de de-industrialisatie en het sluiten van kolenmijnen in het Ruhrgebied.", 40),
    M("Welke sector ving een groot deel van de verloren banen op na de sluiting van fabrieken in het Ruhrgebied?",
      "De dienstensector (tertiaire sector)",
      ["De traditionele akkerbouw en veeteelt",
       "De grootschalige walvisvaart op de Noordzee",
       "Uitsluitend de buitenlandse diplomatieke dienst"],
      "Het aandeel werkenden in de dienstensector nam sterk toe terwijl industrie en mijnbouw krompen.", 40),
    M("Waarom verplaatsten westerse autofabrikanten na de val van het communisme fabrieken naar Midden- en Oost-Europa?",
      "Vanwege de lagere loonkosten en de vrije toegang tot de Europese markt na toetreding tot de EU",
      ["Omdat er in West-Europa helemaal geen wegen meer aangelegd mochten worden",
       "Omdat men in Oost-Europa auto's uitsluitend van hout en glas wilde bouwen",
       "Omdat het bouwen van personenauto's in West-Europa door strenge wetgeving plotseling geheel verboden werd door het parlement"],
      "Landen als Tsjechië boden goedkopere geschoolde arbeidskrachten en profiteerden van EU-vrijhandel.", 39),
    M("Welk bekend automerk heeft zijn hoofdproductie en assemblage in Tsjechië gevestigd?",
      "Skoda (onderdeel van Volkswagen Group)",
      ["Ferrari",
       "Volvo",
       "Rolls-Royce"],
      "In bron 29 zie je de moderne assemblage van Skoda in Tsjechië.", 39),
    M("Wat was het economische gevolg voor Tsjechië, Polen en Roemenië van hun toetreding tot de EU?",
      "Zij kenden de afgelopen decennia een aanzienlijke economische groei door toename van buitenlandse investeringen",
      ["Zij raakten al hun binnenlandse fabrieken en werkgelegenheid binnen twee jaar volledig kwijt aan West-Europa",
       "Hun nationale economie kromp met meer dan negentig procent als direct gevolg van de meedogenloze concurrentie",
       "Zij moesten hun gehele bevolking verplicht laten verhuizen naar Duitsland"],
      "Vrijhandel en verplaatsing van fabrieken stimuleerden een sterke economische inhaalslag in Oost-Europa.", 39),
    M("Wat was het keerzijde-effect voor West-Europese landen zoals Duitsland van de fabrieksverplaatsingen naar het oosten?",
      "Het verdwijnen van industriële banen voor laag- en middelbaar opgeleide fabrieksarbeiders",
      ["Het plotseling instorten van alle elektriciteitsnetwerken in de grote steden",
       "Het plotseling invoeren van een permanent Europees importverbod op traditionele industriële consumptiegoederen",
       "Het verlies van alle academische universiteiten in het Ruhrgebied"],
      "Verplaatsing van productie leidt in het herkomstland vaak tot werkloosheid en banenverlies in fabrieken.", 39),
    M("Waaruit bestaat de huidige export van de Europese Unie tegenwoordig voornamelijk?",
      "Hoogwaardige industriegoederen (zoals auto's en machines) en farmaceutische producten",
      ["Onbewerkte ruwe aardolie, zeldzame aardmetalen en tropisch hardhout uit eigen uitgestrekte oerwouden",
       "Ruwe diamant en ongeslepen mineralen voor de zware industrie",
       "Uitsluitend goedkope confectiekleding en plastic speelgoed"],
      "Europa blinkt wereldwijd uit in hoogwaardige kapitaalgoederen, machines, auto's en medicijnen.", 38),
    W("In het Ruhrgebied is de steenkoolwinning na 1965 vrijwel volledig verdwenen.", True,
      "Waar. Mijnen sloten door concurrentie en alternatieve energiedragers.", 40),
    W("Oost-Europese landen hebben economisch zwaar geleden onder de open binnengrenzen van de EU.", False,
      "Niet waar. Landen als Tsjechië en Polen hebben juist sterk geprofiteerd van vrijhandel en investeringen.", 39),
    W("De-industrialisatie betekent dat de industrie in een gebied een steeds grotere rol gaat spelen.", False,
      "Niet waar. Het betekent juist dat de industriële bedrijvigheid en werkgelegenheid afnemen.", 40),
    W("De auto-industrie in Tsjechië is mede gegroeid door verplaatsing van fabrieken vanuit Duitsland.", True,
      "Waar. Lagere loonkosten maakten Tsjechië aantrekkelijk voor concerns als Volkswagen/Skoda.", 39),
    W("Arbeidsintensieve bedrijven zoals textielbedrijven bleven na 1990 probleemloos in West-Europa floreren.", False,
      "Niet waar. Deze bedrijven verhuisden massaal naar lagelonenlanden buiten Europa.", 39),
    I("Het proces waarbij industrie verdwijnt en de werkgelegenheid daarin afneemt heet de-____.", "industrialisatie",
      "Dat heet de-industrialisatie.", 40),
    I("Het bekendste voormalige zware-industriegebied in Duitsland is het ____gebied.", "Ruhr|Roer",
      "Dat is het Ruhrgebied.", 40),
    I("Het Tsjechische automerk dat onderdeel is van de Volkswagen Group is ____.", "Skoda|Škoda",
      "Dat is Skoda.", 39),
    O("Noem twee oorzaken waardoor West-Europese zware industriegebieden na 1990 in de problemen kwamen.", ["lagelonenlanden/concurrentie", "alternatieve grondstoffen/sluiting mijnen"], 2,
      "Zij hadden zware concurrentie uit lagelonenlanden en kregen te maken met alternatieve grondstoffen en energiebronnen.",
      "Concurrentie uit lagelonenlanden en alternatieve grondstoffen.", 39),
    O("Waarom verhuisden veel industriële bedrijven na 2004 naar landen als Polen en Tsjechië?", ["lagere loonkosten/lonen", "vrijhandel/open grenzen/EU"], 2,
      "Vanwege de lagere loonkosten en de vrije toegang tot de Europese markt na toetreding tot de EU.",
      "Lagere lonen en vrijhandel binnen de EU.", 39)
]),

100: ("Welvaartsverschillen & ESG-normen", "💶", [
    M("Hoe is de welvaart en koopkracht geografisch verdeeld over de Europese Unie volgens bron 27?",
      "In het noordwesten liggen de inkomens en koopkracht gemiddeld hoger dan in het zuiden en het oosten",
      ["In Midden- en Oost-Europa ligt de gemiddelde koopkracht per huishouden ruim drie keer zo hoog als in Duitsland",
       "In Zuid-Europese landen verdienen modale werknemers gemiddeld bijna het dubbele van werknemers in Nederland",
       "De koopkracht is in alle 27 lidstaten exact gelijk verdeeld over de bevolking"],
      "Bron 27 laat zien dat Noordwest-Europa een hogere gemiddelde koopkracht per inwoner heeft.", 38),
    M("Waar staat de afkorting ESG voor in het moderne bedrijfsleven?",
      "Environmental, Social & Governance (Milieu, Mens en Bestuur)",
      ["European Social Growth (Europese Sociale Groei)",
       "Economic Standard Goods (Economische Standaard Goederen)",
       "Energy Supply Guarantee (Energie Levering Garantie)"],
      "ESG staat voor Environmental (milieu), Social (mens/maatschappij) en Governance (behoorlijk bestuur).", 40),
    M("Wat houdt het onderdeel 'Environmental' (milieu) van ESG praktisch in voor een onderneming?",
      "Rekening houden met duurzaamheid, zuinig grondstoffengebruik en het terugdringen van CO2-uitstoot",
      ["Het verplicht planten van tien eikenbomen in de directiekamer van het bedrijf",
       "Het volledig stoppen met het gebruik van elektriciteit tijdens kantooruren",
       "Het exporteren van al het fabrieksafval naar landen buiten de EU"],
      "Bij het milieu-aspect let een bedrijf op grondstoffen, energie en CO2-uitstoot.", 40),
    M("Wat houdt het onderdeel 'Social' (mens) van ESG in?",
      "Aandacht voor goede werkomstandigheden, mensenrechten, veiligheid en diversiteit op de werkvloer",
      ["Het organiseren van wekelijkse gratis bioscoopavonden voor de hele buurt",
       "Het wettelijk verbieden van individuele salarisonderhandelingen tussen directieleden en werknemersorganisaties",
       "Het verplicht aannemen van uitsluitend familieleden van de directeur"],
      "Het sociale aspect betreft veiligheid, diversiteit, mensenrechten en eerlijke behandeling van personeel.", 40),
    M("Wat houdt het onderdeel 'Governance' (bestuur) van ESG in?",
      "Zorgen voor behoorlijk, eerlijk en transparant ondernemingsbestuur, ook in de toeleveringsketen",
      ["Het verplicht overdragen van alle dagelijkse bedrijfsleiding aan de ambtenaren van de Europese Commissie in Brussel",
       "Het geheimhouden van alle financiële jaarverslagen voor de belastingdienst",
       "Het afschaffen van alle officiële contracten en afspraken met leveranciers"],
      "Governance gaat over integer bestuur, openheid en het voorkomen van fraude en corruptie.", 40),
    M("Vanaf welk jaar zijn grote Europese bedrijven wettelijk verplicht om te rapporteren over hun ESG-prestaties?",
      "Sinds 2024",
      ["Al sinds 1950",
       "Pas vanaf het jaar 2090",
       "Rapportage is in Europa voor altijd vrijblijvend"],
      "De EU heeft bepaald dat bedrijven sinds 2024 verplicht moeten rapporteren over hun ESG-beleid.", 40),
    M("Welke vrees hebben sommige Europese ondernemers ten aanzien van de strenge ESG-eisen?",
      "Zij vrezen een concurrentieachterstand ten opzichte van bedrijven uit landen zoals China, die minder strenge regels kennen",
      ["Zij zijn ernstig bezorgd dat vakbonden zullen weigeren mee te werken aan veilige en gezonde werkomstandigheden",
       "Zij vrezen dat de invoering van ESG-richtlijnen ertoe leidt dat de gemeenschappelijke munt binnen een maand instort",
       "Zij zijn bang dat de Europese Unie alle fabrieken in eigendom zal nemen"],
      "Ondernemers vrezen dat concurrenten buiten de EU goedkoper produceren omdat zij minder milieu- en sociale regels naleven.", 40),
    M("Aan welke mondiale doelstellingen van de Verenigde Naties zijn de ESG-waarden nauw gekoppeld?",
      "Aan de Sustainable Development Goals (SDG's)",
      ["Aan de spelregels van het wereldkampioenschap voetbal",
       "Aan de toelatingseisen voor het Eurovisie Songfestival",
       "Aan de verdragen over de verkenning van de planeet Mars"],
      "ESG sluit direct aan bij de duurzame ontwikkelingsdoelen (SDG's) van de VN.", 40),
    M("Welke stroom van arbeidskrachten zie je volgens bron 27 binnen de Europese Unie?",
      "Arbeidsmigratie van landen met lagere koopkracht (Zuid- en Oost-Europa) naar het welvarende noordwesten",
      ["Een massale structurele verhuizing van hoogopgeleide Duitse ingenieurs naar kleinschalige Roemeense landbouwbedrijven",
       "Het vertrek van alle Franse artsen naar mijnbouwregio's in Noord-Zweden",
       "Arbeidsmigratie is binnen de Europese Unie bij wet ten strengste verboden"],
      "Werknemers verhuizen tijdelijk of permanent naar landen met hogere lonen in Noordwest-Europa.", 38),
    M("Waarom blijven er ondanks de vrijhandel toch flinke welvaartsverschillen bestaan binnen de EU?",
      "Omdat economische startposities, opleidingsniveaus en infrastructuur historisch sterk uiteenlopen tussen regio's",
      ["Omdat de Europese Commissie alle ontwikkelingssubsidies uitsluitend toekent aan de allerrijkste industriële metropolen",
       "Omdat arme landen verplicht een boete moeten betalen aan de rijke landen",
       "Omdat er tussen lidstaten nog steeds strenge toltarieven worden geheven"],
      "Historische verschillen in industrialisatie en scholing verdwijnen niet zomaar in enkele decennia.", 38),
    W("In Noordwest-Europa ligt de gemiddelde koopkracht per inwoner hoger dan in Zuid- en Oost-Europa.", True,
      "Waar. Dit is duidelijk te zien op de thematische kaart in bron 27.", 38),
    W("ESG staat voor Economie, Samenleving en Geldzaken.", False,
      "Niet waar. Het staat voor Environmental (milieu), Social (mens) en Governance (bestuur).", 40),
    W("Vanaf 2024 moeten grote bedrijven in de EU verplicht rapporteren over hun ESG-beleid.", True,
      "Waar. De EU heeft deze rapportageverplichting ingevoerd.", 40),
    W("Bedrijven in China ervaren dezelfde strenge milieu- en mensenrechtenregels als bedrijven in Nederland.", False,
      "Niet waar. Bedrijven buiten de EU ervaren doorgaans veel minder last van strenge regels.", 40),
    W("Arbeidsmigratie binnen de EU loopt voornamelijk van welvarende naar minder welvarende regio's.", False,
      "Niet waar. Mensen trekken juist van lagere inkomenslanden naar landen met meer werk en hogere lonen.", 38),
    I("De drie pijlers van ESG zijn milieu, mens en ____.", "bestuur",
      "De drie pijlers zijn milieu, mens en bestuur.", 40),
    I("De wereldwijde duurzaamheidsdoelen van de Verenigde Naties worden afgekort als ____.", "SDG's|SDG|SDGs",
      "Dat zijn de SDG's.", 40),
    I("Het verhuizen van mensen naar een ander EU-land om daar te gaan werken heet arbeids____.", "migratie",
      "Dat heet arbeidsmigratie.", 38),
    O("Waarom maken sommige Europese bedrijven zich zorgen over de invoering van strenge ESG-regels?", ["achterstand/concurrentie", "buiten de EU/China/minder regels"], 2,
      "Zij vrezen een concurrentieachterstand ten opzichte van bedrijven buiten de EU (zoals in China) die minder last hebben van strenge regels.",
      "Zij zijn bang op achterstand te worden gezet door concurrenten buiten de EU.", 40),
    O("Geef één voorbeeld van een maatregel die valt onder de 'E' (Environmental) en één onder de 'S' (Social) van ESG.", ["CO2-uitstoot/grondstoffen/duurzaamheid", "veiligheid/werkomgeving/mensenrechten/diversiteit"], 2,
      "Onder milieu valt het verminderen van CO2-uitstoot en onder sociaal het zorgen voor een veilige werkomgeving en mensenrechten.",
      "Milieu: CO2-uitstoot of grondstoffen; Sociaal: veilige werkomgeving of mensenrechten.", 40)
]),

101: ("Examentraining §1.4 Europa in de wereldhandel", "🎓", [
    M("Aan welke factor heeft de Europese Unie haar sterke positie in de wereldhandel vooral te danken?",
      "Aan vrijhandelsverdragen met meer dan veertig landen en regio's over de hele wereld",
      ["Aan het volledig ontbreken van enige vorm van industriële productie",
       "Aan het historische feit dat de Europese Unie alle denkbare douanetarieven en invoerrechten mondiaal heeft afgeschaft",
       "Aan de gigantische export van goedkoop ruw ijzererts naar Afrika"],
      "Handelsovereenkomsten met ruim 40 partners wereldwijd versterken de Europese handelspositie.", 38),
    M("Op welke drie grote handelspartners buiten de interne markt is de Europese export voornamelijk gericht?",
      "Op de Verenigde Staten, het Verenigd Koninkrijk en China",
      ["Op de Zuid-Amerikaanse handelsstaten Brazilië, Argentinië en Chili",
       "Op de Oceanische landen Australië, Nieuw-Zeeland en Fiji",
       "Op de Sub-Saharische economieën Zuid-Afrika, Kenia en Nigeria"],
      "Buiten de interne markt zijn de VS, het VK en China de drie belangrijkste afzetmarkten van de EU.", 39),
    M("Wat kan een belangrijk gevolg zijn als de EU besluit haar interne markt sterker te beschermen?",
      "Striktere controle op buitenlandse investeringen en scherpere exportcontroles",
      ["Het direct ontmantelen en fysiek afbreken van alle buitenlandse industriële fabrieken in Midden- en Oost-Europa",
       "Het verplicht sluiten van alle zeehavens voor vrachtschepen",
       "Het stopzetten van alle betalingsverkeer in euro's"],
      "Om strategische industrieën en banen te behouden kan de EU investeringen en export strenger controleren.", 39),
    M("Wat kan een consument in Nederland ervan merken als de EU de interne markt meer gaat beschermen?",
      "Aankopen op buitenlandse platforms zoals AliExpress of Temu worden duurder door invoerrechten en controles",
      ["Alle buitenlandse webwinkels en digitale marktplaatsen worden binnen het Nederlandse internetdomein geblokkeerd",
       "Het versturen van e-mails naar het buitenland wordt wettelijk verboden",
       "Supermarkten mogen alleen nog voedsel uit de eigen gemeente verkopen"],
      "Beschermingsmaatregelen maken goedkope bestellingen van buiten de EU vaak duurder voor de consument.", 39),
    M("Welke grote uitdagingen bepalen de toekomst van de Europese handel op het wereldtoneel?",
      "Politieke spanningen, duurzaamheids- en klimaatvraagstukken en snelle technologische ontwikkelingen",
      ["Het plotselinge tekort aan scheepvaartroutes en zout water op de noordelijke Atlantische Oceaan",
       "De door Brussel voorgestelde verplichte terugkeer naar het klassieke Latijn als voertaal in de handel",
       "Een algeheel mondiaal verbod van de Verenigde Naties op het varen met grote containerschepen"],
      "De EU moet laveren tussen geopolitieke spanningen, klimaatdoelen en technologie.", 39),
    M("Wat is een kenmerk van hoogwaardige industriegoederen die Europa exporteert?",
      "Er is veel kennis, hoogwaardige technologie en gespecialiseerd kapitaal voor nodig",
      ["Zij kunnen binnen twee minuten door iedereen thuis met de hand gemaakt worden",
       "Zij bevatten uitsluitend onbewerkte landbouwgrondstoffen en mineralen zonder enige industriële toevoeging",
       "Zij zijn altijd goedkoper dan producten uit lagelonenlanden"],
      "Hoogwaardige goederen zoals robots, chipmachines en auto's vereisen veel kennis en kapitaal.", 38),
    M("Waarom leidt het ontstaan van een multipolaire wereldeconomie tot extra uitdagingen voor de EU?",
      "Omdat Europa te maken heeft met opkomende economische machtsblokken zoals China en India die zware concurrentie bieden",
      ["Omdat alle andere continenten gezamenlijk hebben besloten om voortaan helemaal geen internationale handel meer te drijven",
       "Omdat de Noord- en Zuidpool economisch samensmelten tot één wereldmacht",
       "Omdat de Verenigde Staten alle handelsbanden met de wereld hebben verbroken"],
      "In een multipolaire wereld verliest het Westen zijn monopolie en ontstaan nieuwe rivaliserende centra.", 41),
    M("Welke zes landen werkten als eerste samen in wat later de EU werd?", "Duitsland, Frankrijk, Italië, Nederland, België en Luxemburg", ["Nederland, België, Luxemburg, Spanje, Portugal en Griekenland", "Duitsland, Frankrijk, Verenigd Koninkrijk, Nederland, Denemarken en Zweden", "Frankrijk, Italië, Spanje, Polen, Oostenrijk en Nederland"], "Eerst werkten Duitsland, Frankrijk, Italië, Nederland, België en Luxemburg samen om de handel in steenkool en ijzererts te regelen.", 38),
    M("Welke sector is in West-Europa de afgelopen decennia het sterkst gegroeid ten koste van de industrie?",
      "De commerciële en publieke dienstensector",
      ["De traditionele turfwinning en houtkap",
       "De kleinschalige textielnijverheid aan huis",
       "De visserij op zoetwatermosselen"],
      "De dienstensector vormt tegenwoordig het overgrote deel van de werkgelegenheid in West-Europa.", 40),
    M("Waarom zijn handelsverdragen met meer dan veertig landen zo cruciaal voor de Europese economie?",
      "Omdat Europese bedrijven hierdoor gemakkelijker en zonder hoge invoertarieven kunnen exporteren naar grote afzetmarkten",
      ["Omdat de Europese Unie volgens internationaal recht verplicht wordt om alle openstaande buitenlandse staatsschulden kwijt te schelden",
       "Omdat de EU anders geen paspoorten meer mag uitgeven aan burgers",
       "Omdat buitenlandse presidenten dan verplicht in Brussel moeten komen wonen"],
      "Vrijhandelsverdragen verlagen handelsbarrières en openen markten voor Europese exporteurs.", 38),
    W("Buiten de interne markt zijn de VS, het VK en China de belangrijkste afzetmarkten van de EU.", True,
      "Waar. De Europese export richt zich vooral op deze drie grote handelspartners.", 39),
    W("Bescherming van de Europese interne markt zal ertoe leiden dat goedkope pakketjes van Temu juist nog goedkoper worden.", False,
      "Niet waar. Scherpere controles en invoerheffingen maken dit soort aankopen juist duurder.", 39),
    W("Hoogwaardige industriegoederen zoals auto's en robots vormen een belangrijk onderdeel van de Europese export.", True,
      "Waar. Europa staat bekend om hoogwaardige industriële technologie.", 38),
    W("Een multipolaire wereldeconomie betekent dat de wereld door slechts één enkel land wordt gedomineerd.", False,
      "Niet waar. Multipolair betekent dat er meerdere economische en politieke machtscentra zijn.", 41),
    W("Europa telt meer landen dan de 27 lidstaten die momenteel aangesloten zijn bij de EU.", True,
      "Waar. Er zijn ongeveer 50 landen op het Europese continent, waarvan er 27 lid zijn van de EU.", 38),
    I("De economie waarin meerdere machtsblokken de wereldhandel domineren noem je een multi____ wereldeconomie.", "polaire",
      "Dat is een multipolaire wereldeconomie.", 41),
    I("Twee van de grootste exportproducten van Europa zijn auto's en farmaceutische ____.", "producten|medicijnen",
      "Dat zijn farmaceutische producten (medicijnen).", 38),
    I("Chinese webwinkels zoals AliExpress en ____ kunnen te maken krijgen met strengere Europese importregels.", "Temu|temu",
      "Dat zijn winkels zoals Temu.", 39),
    O("Noem twee manieren waarop de EU haar eigen interne markt in de toekomst beter kan gaan beschermen.", ["buitenlandse investeringen/investeringen", "exportcontroles/importcontroles/controles"], 2,
      "Door de controle op buitenlandse investeringen te verstevigen en de export- en importcontroles aan de grens aan te scherpen.",
      "Controle op buitenlandse investeringen en betere exportcontroles.", 39),
    O("Leg uit waarom consumenten in Europa het kunnen gaan merken als de EU de eigen markt strenger beschermt.", ["aankopen duurder/pakketjes duurder/AliExpress/Temu", "invoerrechten/heffingen/controles"], 2,
      "Aankopen op goedkope buitenlandse platforms zoals Temu of AliExpress worden duurder door strengere controles en invoerrechten.",
      "Aankopen op buitenlandse webshops worden duurder door heffingen en controles.", 39)
])
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('ak_h1_4_extra_seed_55')
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        t = [v["type"] for v in vr]
        assert (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (10, 5, 3, 2), (nr, t)
        assert sum(1 for v in vr if v["type"] == "waaronwaar" and v["antwoord"] is False) >= 2
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {
            "id": f"ex-h3-ak-{nr}",
            "hoofdstuk": 1,
            "paragraaf": "1.4",
            "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
            "titel": f"Proeftoets {nr} — §1.4 {sub}",
            "vak": "Aardrijkskunde · HAVO 3 (H1)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 §1.4) — gegenereerd door tools/gen_aardrijkskunde_h1_4_extra.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
