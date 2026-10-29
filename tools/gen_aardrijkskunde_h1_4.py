#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.4 Rol van Europa in de wereldhandel (boek p. 38-41).
Schrijft havo3/aardrijkskunde/js/data/examen_87..91.js (ex-h3-ak-87..91). Geen onderwerp (h1_4.js bestaat al).
mc-volgorde willekeurig (geseed), opnieuw geschud tot gate-regels 3/16/17 kloppen.
Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
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


BEGRIPPEN = [
    ("EU", "De Europese Unie: 27 Europese lidstaten die samenwerken op economisch en politiek terrein; de EU is geen land."),
    ("G7", "Groep van zeven landen die op economisch terrein samenwerken; de EU is geen lid maar neemt wel deel aan de bijeenkomsten."),
    ("lidstaat", "Een land dat lid is van de EU; alle 27 lidstaten hebben een gemiddeld of hoog welvaartsniveau."),
    ("kandidaat-lidstaat", "Een land dat lid wil worden van de EU en daarvoor aan strenge regels op het gebied van financiën, corruptie en democratie moet voldoen."),
    ("handelsbelemmering", "Regel in landen die handel voor buitenlandse bedrijven vaak lastiger maakt."),
    ("vrijhandel", "Handel waarbij grenzen tussen gebieden en regels zo veel mogelijk worden weggenomen."),
    ("vrijhandelsverdrag", "Afspraak waarmee handelsbelemmeringen worden weggenomen; de EU heeft zulke verdragen met meer dan veertig landen en regio's."),
    ("multipolaire wereldeconomie", "Economie waarbij op meerdere plaatsen in de wereld belangrijke economische kerngebieden liggen."),
    ("lagelonenland", "Land waar de lonen laag zijn, waardoor het productie van Europese bedrijven kan overnemen."),
    ("zware industrie", "Industrie zoals ijzer en staal en scheepsbouw; veel oude industriegebieden in West-Europa draaiden hierop."),
    ("arbeidsintensief", "Bedrijven die veel arbeiders nodig hebben, zoals in textiel, kleding en schoenen."),
    ("de-industrialisatie", "Het verdwijnen van de industrie uit een gebied, zoals in het Ruhrgebied (mijnen, hoogovens en staalfabrieken sloten)."),
    ("handelsblok", "Groep landen die samen handel drijven; de EU is een belangrijk handelsblok met export vooral naar de VS, het VK en China."),
    ("ESG", "Environmental & Social Governance: bedrijven houden rekening met milieu, mens en bestuur."),
    ("koopkracht", "Wat inwoners kunnen kopen met hun inkomen; in het noordwesten van Europa is die gemiddeld hoger dan in het zuiden en oosten."),
]

# ---------------------------------------------------------------- Proeftoets 87: begrippen & feiten
T87 = [
    M("Waarom is de EU geen lid van de G7?",
      "De G7 bestaat uit zeven landen en de EU is zelf geen land",
      ["De EU heeft een te laag welvaartsniveau om zich aan te sluiten",
       "De EU werkt op economisch terrein niet met andere landen samen",
       "De EU mag van de G7-landen niet aan bijeenkomsten meedoen"],
      "De G7 is een groep van zeven landen. De EU is geen land en dus geen lid, maar neemt wel deel aan de bijeenkomsten.", 38),
    M("Welke zes landen werkten als eerste samen als grondleggers van de EU?",
      "Duitsland, Frankrijk, Italië, Nederland, België en Luxemburg",
      ["Duitsland, Frankrijk, Spanje, Nederland, België en Denemarken",
       "Frankrijk, Italië, Nederland, Zweden, Oostenrijk en Luxemburg",
       "Duitsland, Italië, Nederland, België, Luxemburg en Polen"],
      "De eerste samenwerking was tussen Duitsland, Frankrijk, Italië, Nederland, België en Luxemburg.", 38),
    M("Waarover wilden de eerste zes landen samenwerken?",
      "De onderlinge handel in steenkool en ijzererts regelen",
      ["De onderlinge handel in olie en aardgas regelen",
       "De uitwisseling van auto’s en machines regelen",
       "De verkoop van landbouwproducten aan Azië regelen"],
      "In eerste instantie ging het om het reguleren van de onderlinge handel in steenkool en ijzererts.", 38),
    M("Uit hoeveel lidstaten bestaat de EU tegenwoordig volgens het boek?",
      "27", ["25", "28", "31"],
      "De EU bestaat uit 27 Europese lidstaten, die samenwerken op economisch en politiek terrein.", 38),
    M("Waaruit bestaat de huidige Europese export vooral?",
      "Hoogwaardige industriegoederen en farmaceutische producten",
      ["Grondstoffen en halffabricaten voor de zware industrie",
       "Textiel, kleding en schoenen uit arbeidsintensieve bedrijven",
       "Landbouwproducten en onbewerkt hout uit het oosten"],
      "De export is divers, maar bestaat vooral uit hoogwaardige industriegoederen (auto’s, robots) en medicijnen.", 38),
    M("Waaraan hebben Europese landen hun sterke positie in de wereldhandel vooral te danken?",
      "Vrijhandelsverdragen met meer dan veertig landen en regio’s",
      ["De lage lonen die in alle lidstaten worden betaald",
       "De grote voorraden steenkool en ijzererts in de bodem",
       "Een verbod op de invoer uit landen buiten Europa"],
      "De sterke positie komt door vrijhandelsverdragen met meer dan veertig landen en regio’s.", 38),
    M("Welk land verliet in 2020 de EU na een referendum?",
      "Het Verenigd Koninkrijk", ["Ierland", "Zweden", "Denemarken"],
      "Sinds 2020 heeft het Verenigd Koninkrijk de EU verlaten, na een referendum over het lidmaatschap.", 38),
    M("Wat moeten kandidaat-lidstaten volgens het boek kunnen doen om lid te worden?",
      "Voldoen aan strenge regels op het gebied van financiën, corruptie en democratie",
      ["Eerst lid worden van de G7 en daarna een referendum houden",
       "Hun grenzen sluiten voor alle bedrijven uit andere landen en hun lonen verhogen",
       "Hun eigen handelsverdragen met andere landen opzeggen en het geld inleveren"],
      "Kandidaat-lidstaten moeten aan strenge regels voldoen op het gebied van financiën, corruptie en democratie.", 38),
    M("In welk deel van Europa liggen de gemiddelde inkomens en de koopkracht hoger dan in andere delen?",
      "In het noordwesten", ["In het zuiden", "In het oosten", "In het zuidoosten"],
      "In het noordwesten van Europa liggen de gemiddelde inkomens en de koopkracht hoger dan in het zuiden en oosten.", 38),
    M("Wat maakt de handel tussen EU-landen volgens het boek gemakkelijker?",
      "Het wegnemen van handelsbelemmeringen en de open grenzen",
      ["De hogere belastingen die buitenlandse bedrijven moeten betalen",
       "De gezamenlijke taal die in alle lidstaten wordt gesproken",
       "Het verbod voor bedrijven om uit lagelonenlanden te importeren"],
      "Door de samenwerking zijn de handelsbelemmeringen weggenomen en zijn de grenzen tussen EU-landen open.", 38),
    W("De EU is geen land.", True,
      "Waar. De EU is een samenwerkingsverband van lidstaten en daarom ook geen lid van de G7.", 38),
    W("Bij het referendum in het Verenigd Koninkrijk was een grote meerderheid van de bevolking tegen lidmaatschap van de EU.", False,
      "Niet waar. Het ging om een nipte meerderheid.", 38),
    W("De 27 EU-landen hebben allemaal een laag welvaartsniveau.", False,
      "Niet waar. Het zijn allemaal landen met een gemiddeld of hoog welvaartsniveau.", 38),
    W("De EU-landen handelen veel met elkaar en met de rest van de wereld.", True,
      "Waar. Er wordt veel gehandeld, onderling en met de rest van de wereld.", 38),
    W("Oekraïne, Turkije en Servië zijn al lid van de EU.", False,
      "Niet waar. Deze landen zouden graag samenwerken met EU-landen zonder handelsbelemmeringen, maar zijn geen lid.", 38),
    I("De EU is geen lid van de G7, maar neemt wel deel aan de ____ van de G7.",
      "bijeenkomsten|bijeenkomst|vergaderingen|topbijeenkomsten",
      "De EU neemt deel aan de bijeenkomsten van de G7 zonder lid te zijn.", 38),
    I("Een land dat lid wil worden van de EU en nog aan strenge regels moet voldoen, heet een ____-lidstaat.",
      "kandidaat|kandidaat-",
      "Zo’n land heet een kandidaat-lidstaat.", 38),
    I("De Europese export bestaat vooral uit hoogwaardige industriegoederen en ____ producten (medicijnen).",
      "farmaceutische|farmaceutisch",
      "Medicijnen zijn farmaceutische producten.", 38),
    O("Leg uit waarom de onderlinge handel in de EU gemakkelijker is dan vroeger.",
      ["belemmering", "grenzen"], 2,
      "Door de samenwerking zijn de handelsbelemmeringen tussen de landen weggenomen en zijn er open grenzen.",
      "Door de samenwerking zijn handelsbelemmeringen weggenomen en door de open grenzen verloopt de handel soepeler.", 38),
    O("Noem twee kritiekpunten die inwoners of bedrijven op de EU hebben.",
      ["traag", "regels", "duurzaamheid"], 2,
      "De besluitvorming verloopt vaak traag en inwoners en bedrijven moeten zich aan regels houden (bijvoorbeeld strengere duurzaamheidsregels) waar ze het niet mee eens zijn.",
      "Kritiek: de besluitvorming vanuit de EU verloopt vaak traag, terwijl de gevolgen groot zijn; inwoners en bedrijven moeten zich aan regels houden waar ze het niet mee eens zijn.", 38),
]

# ---------------------------------------------------------------- Proeftoets 88: oorzaak & gevolg
T88 = [
    M("Waarom kwamen veel oude industriegebieden in West-Europa na 1990 in de problemen?",
      "Ze kregen concurrentie uit lagelonenlanden en van alternatieve grondstoffen",
      ["Ze kregen geen toegang meer tot de interne markt van de EU voor hun producten",
       "De EU verbood de zware industrie in de West-Europese lidstaten volledig",
       "Er waren te weinig inwoners om de grote fabrieken en mijnen te bemannen"],
      "Zware industrie en arbeidsintensieve bedrijven hadden last van concurrentie uit lagelonenlanden en alternatieve grondstoffen.", 39),
    M("Wat was een gevolg van het sluiten van mijnen, hoogovens en staalfabrieken?",
      "De werkloosheid liep snel op",
      ["De koopkracht in die gebieden steeg snel",
       "De werkgelegenheid in de industrie groeide",
       "Er kwamen minder handelsbelemmeringen"],
      "Mijnen, hoogovens en staalfabrieken moesten sluiten en de werkloosheid liep snel op.", 39),
    M("Waardoor kenden landen als Polen, Tsjechië en Roemenië een grote economische groei?",
      "Ze profiteerden van de vrijhandel binnen de EU",
      ["Ze waren als enige landen vrijgesteld van EU-regels",
       "Ze sloten hun grenzen voor goedkope importproducten",
       "Ze hadden de meeste zware industrie van Europa"],
      "Deze Oost-Europese landen hebben geprofiteerd van de vrijhandel binnen de EU.", 39),
    M("Wat was een gevolg voor Duitsland van het verplaatsen van autofabrieken naar Tsjechië?",
      "Er verdwenen banen in Duitsland",
      ["Er kwamen extra banen in de Duitse auto-industrie bij",
       "De Duitse koopkracht steeg door de lagere lonen",
       "De Duitse export van auto’s kwam volledig tot stilstand"],
      "De verplaatsing van fabrieken vanuit onder meer Duitsland leidde in Duitsland tot het verdwijnen van banen.", 39),
    M("Welke verklaring ligt voor de hand voor het verplaatsen van fabrieken van Duitsland naar Tsjechië?",
      "In Tsjechië is de koopkracht lager, dus waarschijnlijk ook de lonen",
      ["De koopkracht is in Tsjechië hoger, dus kunnen bedrijven er meer verkopen",
       "Tsjechië heeft meer zware industrie dan het Ruhrgebied",
       "Tsjechië ligt buiten de EU, waardoor er geen regels gelden"],
      "Bron 27 laat een lagere koopkracht in Tsjechië zien; lagere lonen maken produceren daar goedkoper, en lidmaatschap van de EU maakt vrijhandel mogelijk.", 41),
    M("Waarom zijn sommige EU-bedrijven bang voor een achterstand door ESG-regels?",
      "Bedrijven buiten de EU ervaren minder last van strengere milieu- en sociale regels",
      ["Bedrijven buiten de EU moeten meer rapporteren dan bedrijven in de EU",
       "ESG-regels maken produceren in de EU goedkoper dan in China",
       "De EU verplicht ook bedrijven in China om ESG toe te passen"],
      "Bedrijven buiten de EU hebben minder last van strengere regels, dus kunnen EU-bedrijven op achterstand komen.", 40),
    M("Wat kan een gevolg zijn als de EU haar interne markt meer gaat beschermen?",
      "Aankopen op Temu of AliExpress kunnen duurder worden",
      ["Aankopen op Temu of AliExpress worden altijd goedkoper",
       "Webwinkels buiten de EU krijgen er meer klanten bij",
       "Europese bedrijven mogen niets meer exporteren"],
      "Meer bescherming van de interne markt kan leiden tot behoud van werkgelegenheid, maar jouw aankopen op Temu of AliExpress kunnen duurder worden.", 39),
    M("Waarom protesteerden boeren in Nederland, België en Frankrijk tegen de EU?",
      "Ze moeten zich houden aan regels waar ze het niet mee eens zijn",
      ["De EU heeft te weinig regels voor de landbouw ingevoerd",
       "Hun producten mogen niet meer binnen de EU worden verkocht",
       "Er is te weinig handel met landen buiten de EU"],
      "Inwoners moeten zich soms houden aan EU-regels, zoals stikstofmaatregelen, waar ze het niet mee eens zijn.", 38),
    M("Welke bedrijven hadden in West-Europa na 1990 vooral last van lagelonenlanden?",
      "Arbeidsintensieve bedrijven, zoals in de textiel, kleding en schoenen",
      ["Bedrijven die medicijnen en andere farmaceutische producten maken",
       "Fabrikanten die robots en hoogwaardige machines exporteren",
       "Autofabrikanten die vooral naar de VS en China uitvoeren"],
      "Naast zware industrie hadden vooral de arbeidsintensieve bedrijven last van concurrentie uit lagelonenlanden.", 39),
    M("Wat is volgens het boek een mogelijk gevolg van de toekomstige uitdagingen voor de EU?",
      "De EU beschermt de eigen interne markt meer",
      ["De EU stopt alle handel met de VS, het VK en China",
       "De EU voert alle handelsbelemmeringen in Europa weer in",
       "De EU laat buitenlandse investeringen ongecontroleerd toe"],
      "De EU kan bijvoorbeeld de controle op buitenlandse investeringen verstevigen en exportcontroles stroomlijnen.", 39),
    W("Doordat mijnen, hoogovens en staalfabrieken sloten, daalde de werkloosheid in de oude industriegebieden.", False,
      "Niet waar. De werkloosheid liep juist snel op.", 39),
    W("Tsjechië heeft geprofiteerd van de vrijhandel binnen de EU en kende economische groei.", True,
      "Waar. In Tsjechië groeide bijvoorbeeld de auto-industrie.", 39),
    W("De verplaatsing van autofabrieken van Duitsland naar Tsjechië leverde Duitsland extra banen op.", False,
      "Niet waar. In Duitsland leidde dit tot het verdwijnen van banen.", 39),
    W("Strengere duurzaamheidsregels kunnen EU-bedrijven in het nadeel zetten ten opzichte van bedrijven buiten de EU.", True,
      "Waar. Bedrijven buiten de EU ervaren minder last van strengere milieu- en sociale regels.", 40),
    W("Arbeidsintensieve bedrijven in de textiel, kleding en schoenen kregen last van concurrentie uit lagelonenlanden.", True,
      "Waar. Dat gold ook voor de zware industrie.", 39),
    I("Door de concurrentie van lagelonenlanden moesten mijnen en hoogovens sluiten en liep de ____ snel op.",
      "werkloosheid", "De werkloosheid liep snel op.", 39),
    I("Bedrijven in textiel, kleding en schoenen hebben veel werknemers nodig; het zijn ____ bedrijven.",
      "arbeidsintensieve|arbeidsintensief", "Dit zijn arbeidsintensieve bedrijven.", 39),
    I("Het verdwijnen van de industrie uit een gebied heet ____.",
      "de-industrialisatie|deindustrialisatie|industrialisatie",
      "Dit heet de-industrialisatie, zoals in het Ruhrgebied.", 40),
    O("Leg uit waarom veel West-Europese industriegebieden na 1990 in de problemen kwamen.",
      ["lagelonenlanden/lage lonen", "concurrent", "werkloosheid"], 2,
      "Zware industrie en arbeidsintensieve bedrijven kregen concurrentie uit lagelonenlanden en van alternatieve grondstoffen; fabrieken en mijnen sloten en de werkloosheid liep op.",
      "Zware industrie en arbeidsintensieve bedrijven hadden last van concurrentie uit lagelonenlanden en alternatieve grondstoffen; mijnen en fabrieken sloten en de werkloosheid liep op.", 39),
    O("Leg uit waarom Oost-Europese landen als Polen en Roemenië economisch groeiden.",
      ["vrijhandel", "lidmaatschap", "fabrieken/auto-industrie"], 2,
      "Door hun EU-lidmaatschap profiteerden ze van de vrijhandel in de EU; fabrieken, zoals in de auto-industrie, werden daarheen verplaatst.",
      "Mede door hun EU-lidmaatschap hebben ze geprofiteerd van de vrijhandel; zo groeide in Tsjechië de auto-industrie doordat fabrieken werden verplaatst.", 39),
]

# ---------------------------------------------------------------- Proeftoets 89: bronnen 26-30
T89 = [
    M("Wat is te zien op bron 26?",
      "Boeren die in 2023 in Brussel protesteren tegen stikstofmaatregelen",
      ["Boeren die in 2023 in Brussel juichen over nieuwe EU-subsidies",
       "Werknemers die in 2020 in Londen protesteren tegen de brexit",
       "Boeren die in 2023 in Parijs protesteren tegen lage koopkracht"],
      "Bron 26 toont boeren die in 2023 in Brussel protesteren tegen stikstofmaatregelen.", 38),
    M("Waar gaat bron 28 over?",
      "De verdeling van de beroepsbevolking en de steenkoolproductie in het Ruhrgebied",
      ["De verdeling van de beroepsbevolking en de autoproductie in Tsjechië",
       "De koopkracht en de werkloosheid van de inwoners van alle EU-landen",
       "De export en de import van het Ruhrgebied naar de VS en China"],
      "Bron 28 laat de verdeling van de beroepsbevolking in het Ruhrgebied zien, met de steenkoolproductie als lijn.", 39),
    M("Wat gebeurt er in bron 28 met het aandeel industrie en mijnbouw tussen 1965 en 2023?",
      "Het daalt van ruim de helft naar ongeveer een kwart",
      ["Het stijgt van ongeveer een kwart naar ruim de helft",
       "Het blijft de hele periode rond de zestig procent",
       "Het verdwijnt volledig vóór het jaar 2000"],
      "Het aandeel industrie/mijnbouw in het Ruhrgebied neemt sterk af, terwijl de diensten groeien.", 39),
    M("Wat laat de lijn van de steenkoolproductie in bron 28 zien?",
      "Een daling van ruim negentig miljoen ton in 1965 tot vrijwel nul rond 2019",
      ["Een stijging van vrijwel nul in 1965 tot ruim negentig miljoen ton",
       "Een gelijkblijvende productie van ongeveer vijftig miljoen ton",
       "Een halvering tot ongeveer vijfenveertig miljoen ton in 2023"],
      "De steenkoolproductie in het Ruhrgebied loopt terug van ruim 90 miljoen ton in 1965 tot vrijwel nul.", 39),
    M("Welke sector heeft in bron 28 in 2023 het grootste aandeel in de beroepsbevolking?",
      "De diensten", ["De industrie en mijnbouw", "De landbouw en bosbouw", "Alle sectoren ongeveer even groot"],
      "In 2023 werkt het grootste deel van de beroepsbevolking in het Ruhrgebied in de dienstensector.", 39),
    M("Wat geven de blauwe pijlen in bron 27 aan?",
      "Arbeidsmigratie",
      ["Verplaatsing van bedrijven en diensten",
       "Gebieden met zware industrie",
       "Het centrum van Europa"],
      "In de legenda van bron 27 staan de blauwe pijlen voor arbeidsmigratie en de rode pijlen voor verplaatsing van bedrijven en diensten.", 39),
    M("Welke richting wijzen de rode pijlen (verplaatsing van bedrijven en diensten) in bron 27 vooral aan?",
      "Van het centrum naar het oosten en het zuiden",
      ["Van het oosten naar het centrum en het noorden",
       "Van het zuiden naar het noordwesten",
       "Van het noordwesten naar Noord-Amerika"],
      "Laagwaardige bedrijven en diensten worden verplaatst van het centrum naar gebieden met een lagere koopkracht in het oosten en zuiden.", 39),
    M("Wat laat bron 29 zien?",
      "De assemblage van een auto in een Škoda-fabriek in Tsjechië",
      ["Een hoogoven in een grote staalfabriek in het Ruhrgebied",
       "Een textielfabriek met veel arbeiders in Roemenië",
       "Een medicijnenfabriek met veel robots in Polen"],
      "Bron 29 toont de assemblage in een Škoda-fabriek in Tsjechië, voorbeeld van de groei van de auto-industrie.", 39),
    M("Welke drie waarden zijn de kern van ESG volgens bron 30?",
      "Milieu, mens en bestuur",
      ["Markt, mens en bestuur", "Milieu, macht en belasting", "Milieu, arbeid en winst"],
      "ESG gaat over milieu, mens en bestuur: duurzaamheid, werknemers en de manier waarop bedrijven bestuurd worden.", 40),
    M("Sinds wanneer moeten bedrijven in de EU volgens bron 30 rapporteren over ESG?",
      "Sinds 2024", ["Sinds 2020", "Sinds 2022", "Sinds 2026"],
      "De EU heeft bepaald dat bedrijven sinds 2024 moeten rapporteren hoe ze met ESG bezig zijn.", 40),
    W("Volgens bron 28 is de steenkoolproductie in het Ruhrgebied in 2023 vrijwel nul.", True,
      "Waar. De lijn van de steenkoolproductie daalt tot (bijna) nul.", 39),
    W("Bron 28 laat zien dat het aandeel van de diensten in de beroepsbevolking tussen 1965 en 2023 is afgenomen.", False,
      "Niet waar. Het aandeel diensten neemt juist toe.", 39),
    W("Bron 27 laat zien dat de koopkracht in het noordwesten van Europa gemiddeld hoger ligt dan in het oosten.", True,
      "Waar. In het noordwesten liggen de inkomens en de koopkracht hoger dan in het zuiden en oosten.", 38),
    W("In bron 29 wordt een auto geassembleerd in een fabriek in Duitsland.", False,
      "Niet waar. Het is een Škoda-fabriek in Tsjechië.", 39),
    W("Bron 26 gaat over boeren die protesteren tegen de brexit.", False,
      "Niet waar. De boeren protesteren tegen stikstofmaatregelen.", 38),
    I("Bron 28 laat de verdeling van de beroepsbevolking zien in het ____, een oud mijn- en industriegebied in Duitsland.",
      "Ruhrgebied|Ruhr", "Bron 28 gaat over het Ruhrgebied.", 39),
    I("Bron 29 toont de assemblage in een ____-fabriek in Tsjechië.",
      "Škoda|Skoda", "Het gaat om een Škoda-fabriek.", 39),
    I("In bron 28 loopt de productie van ____ (in miljoen ton) terug tot vrijwel nul.",
      "steenkool", "De lijn in bron 28 laat de steenkoolproductie zien.", 39),
    O("Beschrijf aan de hand van bron 28 hoe de verdeling van de beroepsbevolking in het Ruhrgebied tussen 1965 en 2023 is veranderd.",
      ["industrie", "diensten", "steenkool"], 2,
      "Het aandeel mensen in industrie en mijnbouw is sterk gedaald, het aandeel in de diensten is flink gegroeid en de steenkoolproductie daalde naar vrijwel nul.",
      "Het aandeel in de industrie nam sterk af, het aandeel in de diensten nam toe.", 39),
    O("Beschrijf aan de hand van bron 27 waar de koopkracht in Europa gemiddeld het hoogst en waar het laagst is.",
      ["noordwest", "oost", "zuid"], 2,
      "De koopkracht is het hoogst in het noordwesten en lager in het zuiden en het oosten.",
      "In het noordwesten liggen de inkomens en koopkracht hoger dan in het zuiden en oosten.", 38),
]

# ---------------------------------------------------------------- Proeftoets 90: toepassen
T90 = [
    M("Een Duitse autofabriek sluit en de productie gaat naar Roemenië. Wat is het waarschijnlijke gevolg voor Roemenië?",
      "Er komen banen bij en de economie groeit",
      ["De werkloosheid loopt snel op door de nieuwe fabriek",
       "De koopkracht daalt omdat er minder wordt geproduceerd",
       "Het land moet de EU verlaten vanwege de concurrentie"],
      "Oost-Europese landen groeien door vrijhandel en verplaatste fabrieken; in het land van vertrek verdwijnen banen.", 39),
    M("Een land met veel corruptie wil lid worden van de EU. Wat moet het volgens het boek eerst doen?",
      "Voldoen aan strenge regels op het gebied van corruptie, financiën en democratie",
      ["Zijn eigen handelsverdragen met andere landen opzeggen",
       "Eerst lid worden van de G7 en daarna een referendum houden",
       "Zijn lonen verhogen tot het niveau van Duitsland"],
      "Kandidaat-lidstaten moeten voldoen aan strenge regels op het gebied van financiën, corruptie en democratie.", 38),
    M("Een Nederlandse boer is boos over een nieuwe stikstofregel. Welke kritiek op de EU past hierbij?",
      "Inwoners moeten zich houden aan regels waar ze het niet altijd mee eens zijn",
      ["De EU neemt besluiten veel te snel en zonder overleg",
       "De EU heeft de handel met landen buiten Europa verboden",
       "De EU laat bedrijven buiten Europa strengere regels volgen"],
      "Boerenprotesten in Nederland, België en Frankrijk gingen tegen regels vanuit de EU.", 38),
    M("Een Poolse fabrikant verkoopt auto’s aan Franse klanten. Wat maakt dat gemakkelijk mogelijk?",
      "De handelsbelemmeringen tussen EU-landen zijn weggenomen",
      ["De regels voor buitenlandse bedrijven zijn juist verscherpt",
       "Polen is lid van de G7 en handelt daardoor vrij",
       "Frankrijk heeft zijn eigen auto-industrie volledig stopgezet"],
      "Door de samenwerking in de EU zijn handelsbelemmeringen weggenomen en is handel gemakkelijker geworden.", 38),
    M("Een Westeuropees bedrijf maakt kleding met veel arbeiders. Welk probleem verwacht je?",
      "Concurrentie van bedrijven uit lagelonenlanden",
      ["Te weinig vraag naar medicijnen uit Europa",
       "Een tekort aan steenkool en ijzererts",
       "Te strenge exportcontroles van de VS"],
      "Arbeidsintensieve bedrijven in kleding, textiel en schoenen hadden last van lagelonenlanden.", 39),
    M("Welke maatregel past bij het beschermen van de interne markt van de EU?",
      "Meer controle op buitenlandse investeringen",
      ["Alle controles op de grens van de EU afschaffen",
       "Nieuwe handelsbelemmeringen tussen EU-landen invoeren",
       "Het aantal lidstaten van de EU verdubbelen"],
      "De EU wil bijvoorbeeld de controle op buitenlandse investeringen verstevigen en exportcontroles beter stroomlijnen.", 39),
    M("Welke ontwikkelingen bepalen volgens het boek de toekomst van de EU in de wereldhandel?",
      "Politieke spanningen, duurzaamheid, klimaatvraagstukken en technologische ontwikkelingen",
      ["Alleen de hoogte van de lonen in de lidstaten en in Azië",
       "Vooral het aantal mijnen en hoogovens in West-Europa",
       "Het aantal inwoners en de oppervlakte van de lidstaten"],
      "Het succes hangt af van hoe goed men omgaat met deze uitdagingen.", 39),
    M("Naast de interne markt is de Europese export vooral gericht op welke landen?",
      "De VS, het VK en China",
      ["Rusland, India en Brazilië", "Japan, Canada en Australië", "Turkije, Servië en Oekraïne"],
      "De export is vooral gericht op de VS, het VK en China.", 39),
    M("Een bedrijf zorgt voor een veilige werkomgeving en respecteert mensenrechten. Welke ESG-waarde past hierbij?",
      "Mens", ["Milieu", "Bestuur", "Markt"],
      "Diversiteit, mensenrechten en een veilige werkomgeving horen bij ‘mens’.", 40),
    M("Een bedrijf beperkt het gebruik van grondstoffen en zijn CO2-uitstoot. Welke ESG-waarde past hierbij?",
      "Milieu", ["Mens", "Bestuur", "Winst"],
      "Grondstoffen en CO2-uitstoot horen bij ‘milieu’.", 40),
    W("Een land als Servië kan zonder voorwaarden lid van de EU worden.", False,
      "Niet waar. Kandidaat-lidstaten moeten aan strenge regels voldoen.", 38),
    W("Als de EU de eigen interne markt meer beschermt, kan dat leiden tot behoud van werkgelegenheid en industrieën.", True,
      "Waar. Dat noemt het boek als mogelijk gevolg.", 39),
    W("Een fabriek die van Duitsland naar Tsjechië verhuist, levert Duitsland extra banen op.", False,
      "Niet waar. In Duitsland verdwijnen dan banen.", 39),
    W("Een EU-bedrijf dat strengere regels moet volgen dan een bedrijf buiten de EU, kan daardoor een achterstand oplopen.", True,
      "Waar. Dat is de angst van sommige bedrijven.", 40),
    W("Politieke spanningen kunnen van invloed zijn op de toekomst van de EU in de wereldhandel.", True,
      "Waar. Ze horen bij de uitdagingen die het boek noemt.", 39),
    I("Een Duitse autobouwer opent een fabriek in Polen. Polen heeft als EU-lid geprofiteerd van de ____ binnen de EU.",
      "vrijhandel", "Vrijhandel binnen de EU gaf Oost-Europese landen groei.", 39),
    I("Een bedrijf let op diversiteit, mensenrechten en een veilige werkomgeving. Binnen ESG hoort dit bij de waarde ____.",
      "mens", "Dit hoort bij ‘mens’.", 40),
    I("Een land dat lid wil worden van de EU moet voldoen aan strenge regels op het gebied van financiën, ____ en democratie.",
      "corruptie", "Het gaat om financiën, corruptie en democratie.", 38),
    O("Een Duitse autofabrikant verplaatst een deel van zijn productie naar Tsjechië. Beschrijf één gevolg voor Duitsland en één voor Tsjechië.",
      ["banen", "groei"], 2,
      "In Duitsland verdwijnen banen; in Tsjechië groeit de auto-industrie en groeit de economie.",
      "Voor Duitsland verdwijnen er banen, voor Tsjechië groeit de economie en de auto-industrie.", 39),
    O("Je bestelt regelmatig spullen op Temu of AliExpress. Leg uit waarom je dit misschien merkt als de EU de eigen markt meer gaat beschermen.",
      ["duurder", "controle"], 2,
      "De EU verstevigt de controle op buitenlandse investeringen en exportcontroles; hierdoor worden aankopen op Temu of AliExpress duurder.",
      "Door meer controle op buitenlandse investeringen en exportcontroles worden aankopen duurder.", 39),
]

# ---------------------------------------------------------------- Proeftoets 91: eindniveau
T91 = [
    M("Wat is het verschil tussen Europa en de Europese Unie?",
      "Europa is een werelddeel, de EU een verbond van 27 landen",
      ["Europa is een samenwerkingsverband, de EU is een werelddeel",
       "Europa bestaat uit 27 landen die allemaal lid zijn van de EU",
       "Europa en de EU zijn twee namen voor precies hetzelfde gebied"],
      "Niet alle landen van Europa zijn lid van de EU; de EU bestaat uit 27 lidstaten.", 38),
    M("Welke uitspraak over de welvaart in de EU klopt?",
      "De welvaart is niet gelijk verdeeld; het noordwesten scoort hoger dan het zuiden en oosten",
      ["De welvaart is overal in de EU precies even groot, ook in het zuiden en oosten",
       "Het zuiden en oosten hebben de hoogste inkomens en de grootste koopkracht",
       "Alleen landen die al sinds de oprichting lid zijn hebben een hoge koopkracht"],
      "Niet iedereen profiteert evenveel; de gemiddelde inkomens en koopkracht zijn in het noordwesten hoger.", 38),
    M("Welke beschrijving past bij de geschiedenis van de EU volgens het boek?",
      "Van zes landen die steenkool en ijzererts regelden naar 27 lidstaten, zonder het VK sinds 2020",
      ["Van 27 landen die steenkool en ijzererts regelden naar zes lidstaten",
       "Van zes landen die steenkool en ijzererts regelden naar 27 lidstaten, waarna Turkije in 2020 toetrad",
       "Van twaalf landen die handel in olie regelden naar 27 lidstaten"],
      "Zes landen regelden eerst de handel in steenkool en ijzererts; nu zijn er 27 lidstaten en het VK is vertrokken.", 38),
    M("Wat is een gevolg van de multipolaire wereldeconomie in Europa, vooral in West-Europa?",
      "De economische groei is minder dan in andere delen van de wereld",
      ["De economische groei is groter dan in alle andere delen van de wereld",
       "De industrie is overal in West-Europa verder gegroeid",
       "De werkloosheid is in West-Europa vrijwel verdwenen"],
      "In West-Europa is de groei minder dan elders en industriegebieden hebben last van lagelonenlanden.", 41),
    M("Een land verhoogt de invoerheffing op buitenlandse schoenen. Hoe heet zo’n regel?",
      "Een handelsbelemmering", ["Een vrijhandelsverdrag", "Een kandidaat-lidstaat", "Een multipolaire economie"],
      "Een handelsbelemmering is een regel die handel voor buitenlandse bedrijven lastiger maakt.", 38),
    M("Welke kritiek op de EU sluit aan bij het boek?",
      "De besluitvorming verloopt vaak traag, terwijl de gevolgen groot zijn",
      ["De besluitvorming gaat te snel en zonder overleg met de lidstaten",
       "De EU heeft te weinig vrijhandelsverdragen met andere landen",
       "De EU laat te veel bedrijven van buiten Europa toe op de markt"],
      "Kritiek: trage besluitvorming met grote gevolgen en regels waar inwoners het niet mee eens zijn.", 38),
    M("Welke landen worden genoemd als landen die graag met EU-landen willen samenwerken zonder handelsbelemmeringen?",
      "Oekraïne, Turkije en Servië",
      ["Rusland, Noorwegen en Zwitserland", "Polen, Tsjechië en Roemenië", "China, India en Brazilië"],
      "Oekraïne, Turkije en Servië zouden graag handel drijven met EU-landen zonder handelsbelemmeringen.", 38),
    M("Welk land noemt het boek als voorbeeld van groei van de auto-industrie door vrijhandel binnen de EU?",
      "Tsjechië", ["Duitsland", "Frankrijk", "Italië"],
      "In Tsjechië groeide de auto-industrie (bron 29); een deel van de fabrieken kwam uit onder meer Duitsland.", 39),
    M("Hoe hangt de de-industrialisatie van het Ruhrgebied samen met ontwikkelingen in Oost-Europa?",
      "Productie verdween uit West-Europa en groeide in Tsjechië dankzij vrijhandel en lagere kosten",
      ["Productie verdween uit Oost-Europa en groeide juist in het Ruhrgebied door vrijhandel",
       "Beide gebieden verloren hun industrie door het verdwijnen van de steenkool",
       "Oost-Europa nam de industrie over door een verbod op Duitse export en import"],
      "West-Europese industriegebieden kregen concurrentie, terwijl Oost-Europese landen groeiden dankzij de EU.", 39),
    M("Welke combinatie past bij wat het boek over de EU in de wereldhandel zegt?",
      "Sterke export door vrijhandelsverdragen, maar ongelijke welvaart",
      ["Zwakke export ondanks vrijhandelsverdragen en gelijke welvaart in Europa",
       "Sterke export door handelsbelemmeringen en overal een hoge koopkracht",
       "Geen export naar de VS, het VK en China en overal gelijke welvaart"],
      "De EU heeft een sterke positie, maar de welvaart is niet gelijk verdeeld.", 38),
    W("Alle landen van Europa zijn lid van de EU.", False,
      "Niet waar. Landen als Oekraïne, Turkije en Servië zijn geen lid.", 38),
    W("De EU heeft vrijhandelsverdragen met meer dan veertig landen en regio’s.", True,
      "Waar. Daaraan danken Europese landen hun sterke positie.", 38),
    W("De Europese export bestaat vooral uit grondstoffen zoals steenkool en ijzererts.", False,
      "Niet waar. De export bestaat vooral uit hoogwaardige industriegoederen en medicijnen.", 38),
    W("In Oost-Europa groeide de economie sterk, terwijl in West-Europa oude industriegebieden in de problemen kwamen.", True,
      "Waar. Dit zijn twee gevolgen van de verschuivingen in de wereldhandel.", 39),
    W("In een multipolaire wereldeconomie ligt het economische kerngebied op één plek in de wereld.", False,
      "Niet waar. In een multipolaire economie liggen op meerdere plaatsen belangrijke kerngebieden.", 41),
    I("Een regel die handel voor buitenlandse bedrijven lastiger maakt, heet een ____.",
      "handelsbelemmering|handelsbelemmeringen", "Dat is een handelsbelemmering.", 38),
    I("In een ____ wereldeconomie liggen op meerdere plaatsen in de wereld belangrijke economische kerngebieden.",
      "multipolaire", "Dat is een multipolaire wereldeconomie.", 41),
    I("De EU heeft vrijhandelsverdragen met meer dan ____ landen en regio’s.",
      "veertig|40", "Het gaat om meer dan veertig landen en regio’s.", 38),
    O("Noem drie uitdagingen voor de toekomst van de Europese handel.",
      ["politieke spanning", "duurzaam", "klimaat", "technologisch/technologie"], 3,
      "Politieke spanningen, duurzaamheid, klimaatvraagstukken en technologische ontwikkelingen; de EU kan de eigen markt meer beschermen.",
      "De toekomst hangt af van politieke spanningen, duurzaamheid, klimaatvraagstukken en technologische ontwikkelingen.", 39),
    O("Een klasgenoot zegt: ‘De EU is alleen maar goed voor de handel.’ Geef één argument vóór en één argument tegen.",
      ["belemmering/vrijhandel", "traag/regels"], 2,
      "Voor: handelsbelemmeringen zijn weggenomen en er is vrijhandel. Tegen: de besluitvorming verloopt vaak traag en inwoners moeten regels volgen waar ze het niet mee eens zijn.",
      "Voor: er zijn handelsbelemmeringen weggenomen. Tegen: de besluitvorming is traag en er zijn regels waar mensen het niet mee eens zijn.", 38),
]

EXAMENS = {
    87: ("Begrippen en feiten over de EU", "🇪🇺", T87),
    88: ("Oorzaak en gevolg: industrie en vrijhandel", "🏭", T88),
    89: ("Bronnen 26–30: Ruhrgebied, koopkracht en ESG", "🗺️", T89),
    90: ("Toepassen op nieuwe situaties", "🧩", T90),
    91: ("Eindniveau: Europa in de wereldhandel", "🎓", T91),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('ak_h1_4')
    assert 8 <= len(BEGRIPPEN) <= 18 + 0 or len(BEGRIPPEN) <= 18, len(BEGRIPPEN)
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        t = [v["type"] for v in vr]
        assert (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (10, 5, 3, 2), (nr, t)
        assert sum(1 for v in vr if v["type"] == "waaronwaar" and v["antwoord"] is False) >= 2
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {"id": f"ex-h3-ak-{nr}", "hoofdstuk": 1, "paragraaf": "1.4",
              "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
              "titel": f"Proeftoets {nr} — §1.4 {sub}", "vak": "Aardrijkskunde · HAVO 3 (H1)",
              "icoon": icoon, "duurMin": 20, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 §1.4) — gegenereerd door tools/gen_aardrijkskunde_h1_4.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
