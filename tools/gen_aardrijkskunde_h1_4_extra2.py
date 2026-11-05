#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · Hoofdstuk 1 Wereldhandel in beweging · §1.4 Rol van Europa in de wereldhandel (extra toetsen 121–125).
Schrijft havo3/aardrijkskunde/js/data/examen_121..125.js (ex-h3-ak-121..125). Script: tools/gen_aardrijkskunde_h1_4_extra2.py
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
121: ("Lidmaatschap, samenwerking en kritiek", "🤝", [
    M("Welk land hoorde volgens het boek niet bij de eerste zes landen die samenwerkten?",
      "Spanje",
      ["Luxemburg", "België", "Italië"],
      "De eerste zes waren Duitsland, Frankrijk, Italië, Nederland, België en Luxemburg; Spanje hoort daar niet bij.", 38),
    M("Wat is het verschil in positie tussen Polen en Servië ten opzichte van de EU?",
      "Polen profiteert als lidstaat van de vrijhandel; Servië wil graag samenwerken",
      ["Servië profiteert als lidstaat van de vrijhandel; Polen wil graag samenwerken",
       "Beide landen zijn kandidaat-lidstaat en handelen niet met EU-landen",
       "Beide landen zijn lidstaat en zijn in 2020 uit de EU gestapt"],
      "Polen heeft als EU-land geprofiteerd van de vrijhandel; Servië staat bij de landen die graag willen samenwerken.", 38),
    M("Welke bewering over het Verenigd Koninkrijk klopt met het boek?",
      "Het VK is sinds 2020 geen lid meer, maar blijft een belangrijke exportbestemming",
      ["Het VK is nog steeds lid van de Unie, maar doet niet mee aan de interne markt",
       "Het VK is uit de Unie gestapt en handelt sindsdien niet meer met EU-landen",
       "Het VK is nooit lid geweest en staat nu als kandidaat-lidstaat op de lijst"],
      "Het VK verliet de EU in 2020, maar de Europese export is nog steeds mede op het VK gericht.", 39),
    M("Welke twee soorten kritiek noemt het boek naast de trage besluitvorming?",
      "Regels waar inwoners het niet mee eens zijn en strengere eisen voor bedrijven",
      ["Te lage uitkeringen voor inwoners en te weinig vakantiedagen voor alle werknemers",
       "Te hoge subsidies voor Britse boeren en te lage invoerrechten op alle medicijnen",
       "Te weinig lidstaten in de Unie en het ontbreken van een eigen volkslied"],
      "Inwoners vinden sommige EU-regels onwenselijk en bedrijven moeten zich aan strengere duurzaamheidsregels houden dan bedrijven buiten de EU.", 38),
    M("Welke uitspraak over Nederland en de oprichting van de EU is juist?",
      "Nederland deed al mee toen de samenwerking met zes landen begon",
      ["Nederland trad pas toe toen de EU al twaalf lidstaten telde",
       "De samenwerking begon met Duitsland en het VK als grote partners",
       "Nederland ging pas meedoen na de invoering van open grenzen"],
      "Nederland is een van de grondleggers en werkte vanaf het begin mee.", 38),
    M("Een Belgische student reist zonder paspoortcontrole naar Duitsland. Welk kenmerk van de EU hoort hierbij?",
      "De open grenzen tussen EU-landen",
      ["Het lidmaatschap van de G7 als groep",
       "De vrijhandelsverdragen met veertig landen",
       "De kandidaat-status van buurlanden"],
      "De handel is mede gemakkelijker geworden door de open grenzen tussen EU-landen.", 38),
    M("De EU begon met zes landen en telt er nu 27. Hoeveel keer zoveel lidstaten is dat ongeveer?",
      "Ongeveer 4,5 keer zoveel",
      ["Ongeveer 2,5 keer zoveel", "Ongeveer 6,5 keer zoveel", "Ongeveer 9,5 keer zoveel"],
      "27 gedeeld door 6 is 4,5.", 38),
    M("Welke bewering over de EU is onjuist?",
      "Bedrijven moeten aan de binnengrenzen nog zware belemmeringen overwinnen",
      ["De besluitvorming vanuit de EU verloopt vaak traag, terwijl de gevolgen groot zijn",
       "Nederland is een van de grondleggers van de Europese Unie",
       "De lidstaten werken samen op economisch en politiek terrein"],
      "Juist doordat de handelsbelemmeringen zijn weggenomen, is de handel tussen de lidstaten gemakkelijker geworden.", 38),
    M("Welke zin beschrijft de EU het best?",
      "Een samenwerkingsverband van 27 landen op economisch en politiek terrein",
      ["Een federale staat met één regering, één hoofdstad en één leger",
       "Een handelsorganisatie waar alle Europese landen automatisch bij horen",
       "Een militair verbond van de zes oprichters van destijds"],
      "De EU is geen land, maar een samenwerkingsverband van 27 lidstaten.", 38),
    W("Nederland behoorde tot de eerste landen die samenwerkten in steenkool en ijzererts.", True,
      "Waar. Nederland is een van de grondleggers van de EU.", 38),
    W("Duitsland en Frankrijk waren de enige twee landen aan het begin van de Europese samenwerking.", False,
      "Niet waar. Er deden zes landen mee: ook Italië, Nederland, België en Luxemburg.", 38),
    W("Boeren protesteerden in 2023 in Brussel omdat er volgens hen te weinig stikstofregels waren.", False,
      "Niet waar. Ze protesteerden juist tegen de stikstofmaatregelen.", 38),
    W("De 27 lidstaten werken samen op zowel economisch als politiek terrein.", True,
      "Waar. Dat staat letterlijk in de tekst over de EU.", 38),
    W("Landen die lid willen worden, hoeven geen eisen op het gebied van democratie te halen.", False,
      "Niet waar. Kandidaat-lidstaten moeten voldoen aan strenge regels op het gebied van financiën, corruptie en democratie.", 38),
    I("Kandidaat-lidstaten moeten aan strenge regels voldoen op het gebied van ____, corruptie en democratie.", "financiën|financien", "Kandidaat-lidstaten moeten voldoen op het gebied van financiën, corruptie en democratie.", 38),
    I("Een volksstemming over een belangrijke kwestie, zoals over het EU-lidmaatschap in het VK, heet een ____.", "referendum|volksraadpleging",
      "Het VK hield een referendum over het lidmaatschap.", 38),
    I("Landen die lid willen worden maar nog niet voldoen aan de eisen, zijn bijvoorbeeld Servië, Turkije en ____.", "Oekraïne|Oekraine",
      "Oekraïne, Turkije en Servië worden genoemd.", 38),
    I("Boeren uit Nederland, België en ____ protesteerden tegen regels vanuit de EU.", "Frankrijk",
      "Het boek noemt boerenprotesten in Nederland, België en Frankrijk.", 38),
    O("Leg uit waarom een Belgisch bedrijf nu gemakkelijker aan Duitse klanten verkoopt dan voor de EU-samenwerking.", ["belemmeringen/handelsbelemmeringen", "open grenzen/grenzen"], 2,
      "Door de samenwerking zijn de handelsbelemmeringen weggenomen en de open grenzen maken handel gemakkelijker.",
      "Handelsbelemmeringen zijn weggenomen en er zijn open grenzen tussen de EU-landen.", 38),
    O("Welk probleem zien critici in de snelheid van EU-besluiten en welke beroepsgroep protesteerde in 2023?", ["traag/langzaam", "boeren/agrariërs"], 2,
      "De besluitvorming verloopt vaak traag terwijl de gevolgen groot zijn, en boeren protesteerden in Brussel.",
      "De besluitvorming is traag en de boeren protesteerden.", 38)
]),

122: ("Industrie in West- en Oost-Europa", "🏭", [
    M("Welk bedrijf zou na 1990 het meest last hebben gehad van goedkope producenten elders in de wereld?",
      "Een West-Europese fabriek die kleding maakt met veel arbeiders",
      ["Een bedrijf dat in Europa medicijnen ontwikkelt en verkoopt",
       "Een fabriek die hoogwaardige robots voor de export bouwt",
       "Een fabrikant van technologisch geavanceerde personenauto's"],
      "Arbeidsintensieve bedrijven als kleding en textiel kregen last van concurrentie van elders.", 39),
    M("De oude zware industrie had last van 'alternatieve grondstoffen'. Wat wordt daar het best mee bedoeld?",
      "Materialen die steenkool en ijzererts in de industrie kunnen vervangen",
      ["Grondstoffen die de EU alleen nog uit de VS mag invoeren en verwerken",
       "Delfstoffen die uitsluitend in Oost-Europa worden gedolven en verhandeld",
       "Nieuwe belastingen op het gebruik van steenkool en ijzererts"],
      "De zware industrie kreeg last van concurrentie uit lagelonenlanden en van alternatieve grondstoffen.", 39),
    M("Welke gebeurtenis is geen gevolg van de de-industrialisatie in het Ruhrgebied?",
      "Een stijging van de steenkoolproductie",
      ["Het sluiten van veel hoogovens", "Het sluiten van veel mijnen", "Het sluiten van staalfabrieken"],
      "Juist de steenkoolproductie liep terug tot vrijwel nul; mijnen, hoogovens en staalfabrieken sloten.", 39),
    M("Wat hebben Polen, Tsjechië en Roemenië volgens de tekst gemeen?",
      "Het zijn Oost-Europese landen die groeiden dankzij vrijhandel in de EU",
      ["Het zijn oude industriegebieden waar na 1990 de mijnen en fabrieken sloten",
       "Het zijn kandidaat-lidstaten die nog helemaal geen vrijhandel kennen",
       "Het zijn landen die in 2020 de Europese Unie verlaten hebben"],
      "Deze drie landen hebben een grote economische groei gekend en geprofiteerd van de vrijhandel binnen de EU.", 39),
    M("Wat zegt de tekst over het tempo van de economische groei in Europese landen?",
      "Dat verschilt: de groei gaat niet overal even snel",
      ["De groei is in alle lidstaten precies even groot",
       "Alleen in West-Europa is de groei de laatste decennia gestegen",
       "In alle lidstaten is de economie de laatste decennia gekrompen"],
      "De groei van de economie van Europese landen gaat niet overal even snel.", 39),
    M("Welke combinatie van sector en probleem na 1990 klopt met het boek?",
      "Textiel: bedrijven kregen last van concurrentie uit lagelonenlanden",
      ["Medicijnen: bedrijven moesten vrijwel allemaal sluiten door hoge lonen",
       "Robots: de productie stortte in door het verdwijnen van mijnen",
       "Auto's: de assemblage verdween volledig uit alle Europese landen"],
      "Arbeidsintensieve bedrijven in textiel, kleding en schoenen hadden last van lagelonenlanden.", 39),
    M("Welk gegeven uit bron 27 helpt te verklaren dat fabrieken van west naar oost verhuizen?",
      "De koopkracht ligt in het oosten lager dan in het westen",
      ["De koopkracht in het oosten ligt boven het Europese gemiddelde",
       "In het oosten liggen vooral grote gebieden met zware industrie",
       "In het oosten werken nauwelijks arbeiders uit andere landen"],
      "Bron 27 toont een lagere koopkracht in het oosten; productie is daar goedkoper.", 41),
    M("Hoe verhoudt de komst van fabrieken naar Oost-Europa zich tot de situatie in het land van herkomst?",
      "Het ene land wint groei, het andere land verliest fabrieken",
      ["Beide landen krijgen er evenveel nieuwe fabrieken bij",
       "Beide landen verliezen hun fabrieken aan lagelonenlanden buiten Europa",
       "Geen van beide landen merkt iets van de verplaatsing"],
      "Een deel van de fabrieken is verplaatst: het ontvangende land groeit, het land van herkomst verliest.", 39),
    M("Wat is volgens het boek een kenmerk van de West-Europese industriegebieden die na 1990 in de problemen kwamen?",
      "Het waren oude gebieden met zware industrie",
      ["Het waren nieuwe gebieden met vooral hightechbedrijven",
       "Het waren havensteden met vooral dienstverlening en handel",
       "Het waren landbouwgebieden met vooral akkerbouw en veeteelt"],
      "Vooral de oude industriegebieden met zware industrie kwamen in de problemen.", 39),
    W("Zware industrie en arbeidsintensieve bedrijven kregen na 1990 last van lagelonenlanden.", True,
      "Waar. Beide groepen noemt het boek.", 39),
    W("Het boek rekent de kleding- en textielindustrie tot de zware industrie.", False,
      "Niet waar. Zware industrie is ijzer en staal en scheepsbouw; textiel en kleding zijn arbeidsintensief.", 39),
    W("Alleen West-Europese landen hebben geprofiteerd van de vrijhandel binnen de EU.", False,
      "Niet waar. Ook Oost-Europese landen als Polen en Tsjechië profiteerden sterk.", 39),
    W("Een deel van de fabrieken in Oost-Europa is daar neergezet door bedrijven uit andere Europese landen.", True,
      "Waar. Een deel is verplaatst vanuit andere Europese landen.", 39),
    W("De welvaart is gelijk verdeeld over Europa nu Oost-Europese landen sterk groeien.", False,
      "Niet waar. In het noordwesten liggen inkomens en koopkracht nog altijd hoger dan in het zuiden en oosten.", 38),
    I("Veel fabrieken in Oost-Europa zijn verplaatst vanuit andere Europese landen zoals ____.", "Duitsland",
      "Het boek noemt Duitsland als voorbeeld.", 39),
    I("De zware industrie omvat ijzer en staal en ____.", "scheepsbouw",
      "Zware industrie: ijzer en staal, scheepsbouw.", 39),
    I("Doordat fabrieken naar Oost-Europa verhuisden, verdwenen er in het land van herkomst ____.", "banen", "In het land van herkomst verdwenen banen.", 39),
    I("Arbeidsintensieve bedrijven maken textiel, kleding en ____.", "schoenen",
      "Textiel, kleding en schoenen.", 39),
    O("Leg uit waarom de komst van fabrieken goed is voor het ontvangende land maar nadelig voor het land van herkomst.", ["economische groei/groei", "banen/werkgelegenheid"], 2,
      "Het ontvangende land krijgt economische groei en banen erbij, het land van herkomst verliest banen.",
      "Groei en banen voor het ene land, verlies van banen voor het andere.", 39),
    O("Welk verband bestaat er tussen het verdwijnen van de industrie in een regio en de arbeidsmarkt?", ["werkloosheid/werklozen/werkloos", "mijnen/hoogovens/fabrieken"], 2,
      "Als mijnen, hoogovens en fabrieken verdwijnen, loopt de werkloosheid op.",
      "Door het sluiten van fabrieken loopt de werkloosheid op.", 39)
]),

123: ("Export, handelsblok en bescherming van de markt", "🚢", [
    M("Wat bedoelt het boek met 'productie voor de interne markt'?",
      "Producten die bestemd zijn voor afnemers binnen de EU zelf",
      ["Producten die alleen voor de eigen fabriek bedoeld zijn",
       "Producten die uitsluitend naar de VS worden verscheept",
       "Producten die alleen in de eigen winkelstraat verkocht worden"],
      "Naast productie voor de interne markt is de export vooral op de VS, het VK en China gericht.", 39),
    M("Een Chinees concern wil een Europees bedrijf overnemen. Welke maatregel hoort bij het beschermen van de interne markt?",
      "Strengere controle op buitenlandse investeringen",
      ["Het afschaffen van alle vrijhandelsverdragen",
       "Het verlagen van alle invoerrechten voor Aziatische waren",
       "Het sluiten van de binnengrenzen tussen lidstaten"],
      "De EU wil de controle op buitenlandse investeringen verstevigen.", 39),
    M("Welk land wordt in het boek niet genoemd als belangrijke exportbestemming van de EU, naast de interne markt?",
      "Brazilië",
      ["De Verenigde Staten", "China", "Het Verenigd Koninkrijk"],
      "Genoemd worden de VS, het VK en China.", 39),
    M("Welke keten van oorzaak en gevolg schetst het boek voor jouw aankopen?",
      "Uitdagingen voor de EU, meer bescherming, duurdere aankopen bij buitenlandse webshops",
      ["Meer bescherming van de markt, goedkopere aankopen, minder werk in de industrie nodig",
       "Duurdere aankopen, minder bescherming van de markt, nieuwe uitdagingen voor de EU zelf",
       "Goedkopere aankopen, meer open grenzen, hogere werkloosheid in de hele industrie"],
      "De uitdagingen kunnen tot meer bescherming leiden, waardoor aankopen op Temu of AliExpress duurder worden.", 39),
    M("Wat kenmerkt de Europese export volgens het boek?",
      "Divers, maar vooral hoogwaardige industriegoederen en medicijnen",
      ["Vooral ruwe grondstoffen en onbewerkte landbouwproducten",
       "Eenzijdig en bijna alleen uit kleding en schoenen bestaand",
       "Zeer klein en vooral uit diensten voor de buurlanden"],
      "De export is divers, vooral hoogwaardige industriegoederen en farmaceutische producten.", 38),
    M("Welke van deze zaken is geen uitdaging die het boek noemt voor de Europese handel?",
      "Het verdwijnen van de euro",
      ["Politieke spanningen", "Klimaatvraagstukken", "Technologische ontwikkelingen"],
      "Het boek noemt politieke spanningen, duurzaamheid, klimaatvraagstukken en technologische ontwikkelingen.", 39),
    M("Hoe kan meer bescherming van de interne markt uitpakken voor de industrie in de EU?",
      "Werkgelegenheid en industrieën blijven daardoor eerder behouden",
      ["De industrie verdwijnt daardoor sneller naar lagelonenlanden",
       "De industrie krijgt daardoor automatisch hogere exportcijfers",
       "De industrie hoeft zich daardoor niet meer aan regels te houden"],
      "Bescherming kan leiden tot het behoud van werkgelegenheid en industrieën.", 39),
    M("Wat betekent 'handelsblok' in de zin dat de EU een belangrijk handelsblok vormt?",
      "Een groep landen die onderling handel makkelijk maakt",
      ["Een gebouw in Brussel waar alle goederen worden opgeslagen en gekeurd",
       "Een lijst met producten die buiten Europa verboden zijn en blijven",
       "Een groep bedrijven die samen één enkel product in massa maakt"],
      "De EU treedt als blok op in de wereldhandel.", 39),
    M("De EU wil de exportcontroles van de interne markt beter stroomlijnen. Wat zegt dat over haar koers?",
      "Ze wil haar interne markt beter beschermen en controleren",
      ["Ze wil de interne markt juist volledig openstellen voor iedereen",
       "Ze wil de eigen export zo veel mogelijk beperken of stoppen",
       "Ze wil alle vrijhandelsverdragen binnen een jaar opzeggen"],
      "Stroomlijnen van exportcontroles hoort bij het beschermen van de interne markt.", 39),
    W("Een deel van de Europese productie is bedoeld voor de interne markt zelf.", True,
      "Waar. Naast productie voor de interne markt gaat de export vooral naar de VS, het VK en China.", 39),
    W("Het succes van de EU in de wereldhandel hangt van meerdere factoren af.", True,
      "Waar. Politieke spanningen, duurzaamheid, klimaat en technologie spelen mee.", 39),
    W("Volgens het boek richt de Europese export zich vooral op Afrika.", False,
      "Niet waar. De export is vooral gericht op de VS, het VK en China.", 39),
    W("De EU heeft vrijhandelsverdragen gesloten met minder dan tien landen en regio's.", False,
      "Niet waar. Het zijn er meer dan veertig.", 38),
    W("De EU wil de controle op buitenlandse investeringen juist verminderen.", False,
      "Niet waar. De EU wil die controle verstevigen.", 39),
    I("In het ____ van Europa liggen de gemiddelde inkomens en de koopkracht hoger dan in het zuiden en oosten.", "noordwesten|noordwesten van europa", "In het noordwesten zijn inkomens en koopkracht het hoogst.", 39),
    I("Aankopen op Temu of ____ kunnen door de uitdagingen voor de EU duurder worden.", "AliExpress", "Het boek noemt Temu en AliExpress.", 38),
    I("De EU is geen land en daarom ook geen lid van de ____.", "G7", "De EU is geen lid van de G7, maar doet wel mee aan de bijeenkomsten.", 39),
    I("De EU zal de controle op buitenlandse investeringen ____.", "verstevigen|versterken|aanscherpen|verscherpen", "De EU gaat de controle op buitenlandse investeringen verstevigen.", 39),
    O("Leg uit hoe meer bescherming van de Europese markt gevolgen kan hebben voor de industrie en voor jouw eigen aankopen.", ["werkgelegenheid/banen", "duurder"], 2,
      "Industrie en werkgelegenheid blijven behouden, maar aankopen bij buitenlandse webwinkels worden duurder.",
      "Het behoudt banen, maar aankopen worden duurder.", 39),
    O("Noem twee redenen waarom de EU een sterke positie heeft in de wereldhandel.", ["vrijhandelsverdragen/verdragen", "hoogwaardige/industriegoederen/medicijnen/farmaceutische"], 2,
      "Door vrijhandelsverdragen met meer dan veertig landen en door de export van hoogwaardige industriegoederen en medicijnen.",
      "Vrijhandelsverdragen en hoogwaardige industriegoederen.", 38)
]),

124: ("ESG en duurzaamheidsregels", "🌱", [
    M("Wie heeft bepaald dat bedrijven moeten rapporteren over ESG?",
      "De Europese Unie",
      ["De G7", "De Chinese overheid", "Elk bedrijf voor zichzelf"],
      "De EU heeft bepaald dat bedrijven sinds 2024 moeten rapporteren.", 40),
    M("Wat bedoelt de tekst met de 'last' die bedrijven buiten de EU minder ervaren?",
      "Strengere milieu- en sociale regels",
      ["Hogere invoerrechten op eigen producten",
       "Strengere grenscontroles bij de export",
       "Zwaardere belastingen op hun winst"],
      "Bedrijven buiten de EU ervaren minder last van strengere milieu- en sociale regels.", 40),
    M("Op welke twee plekken komt duurzaamheid terug in deze paragraaf?",
      "Bij de ESG-rapportage van bedrijven en als toekomstuitdaging voor de EU-handel",
      ["Alleen bij de oprichting van de EU en bij de G7-bijeenkomsten van leiders",
       "Bij het sluiten van mijnen en bij de verkoop van auto's door Skoda in Tsjechië",
       "Bij de vrijhandelsverdragen en bij de uitslag van het referendum in het VK"],
      "ESG gaat over duurzaamheid, en duurzaamheid wordt ook genoemd als uitdaging voor de toekomst.", 40),
    M("Welke twee voorbeelden laten zien dat strenge duurzaamheidsregels weerstand oproepen?",
      "De boerenprotesten en de zorg van bedrijven over een concurrentieachterstand",
      ["De uitslag van het referendum en de val van een regering in Brussel",
       "De stakingen in de havens en de sluiting van veel scholen in Europa",
       "De sluiting van de mijnen en de verhuizing van autofabrieken naar het oosten"],
      "Boeren protesteerden tegen stikstofregels en bedrijven vrezen een achterstand.", 40),
    M("Welke koppeling tussen ESG-letter en voorbeeld klopt?",
      "G: behoorlijk bestuur, ook bij de leveranciers",
      ["E: een veilige werkomgeving en mensenrechten",
       "S: het beperken van CO2-uitstoot en grondstoffen",
       "G: aandacht voor diversiteit op de werkvloer"],
      "G staat voor bestuur; E voor milieu; S voor mens.", 40),
    M("Hoeveel jaar na het vertrek van het VK uit de EU werd de ESG-rapportage verplicht?",
      "Vier jaar later",
      ["Twee jaar later", "Zes jaar later", "Tien jaar later"],
      "Het VK vertrok in 2020, de rapportage geldt sinds 2024.", 40),
    M("Een ondernemer zegt: 'ESG maakt ons minder concurrerend.' Welke zin uit de bron ondersteunt dat?",
      "Bedrijven buiten de EU ervaren minder last van strengere milieu- en sociale regels",
      ["Bedrijven buiten de EU betalen meer belasting dan Europese bedrijven in de EU",
       "Bedrijven binnen de EU mogen alleen aan de interne markt verkopen en niet exporteren",
       "Bedrijven in China mogen geen grondstoffen uit Europa invoeren of verwerken"],
      "De angst is dat EU-bedrijven op achterstand komen.", 40),
    M("Wat valt niet onder ESG?",
      "Het verlagen van invoerrechten op schoenen",
      ["Het beperken van de CO2-uitstoot van fabrieken",
       "Het respecteren van de mensenrechten van personeel",
       "Behoorlijk bestuur bij alle leveranciers"],
      "Invoerrechten zijn handelsbeleid, geen ESG-waarde.", 40),
    M("Welke ESG-waarde sluit het meest aan bij de klimaatvraagstukken die de EU als uitdaging noemt?",
      "Milieu (Environmental)",
      ["Mens (Social)", "Bestuur (Governance)", "Handel (Trading)"],
      "Klimaat hangt samen met het gebruik van grondstoffen en CO2-uitstoot, dus milieu.", 40),
    W("ESG gaat over duurzaamheid, werknemers en de manier waarop bedrijven bestuurd worden.", True,
      "Waar. Dat staat in de tekst bij bron 30.", 40),
    W("De EU heeft bepaald dat bedrijven pas vanaf 2030 over ESG hoeven te rapporteren.", False,
      "Niet waar. Het geldt sinds 2024.", 40),
    W("Volgens de bron zijn de ESG-regels in China strenger dan in de EU.", False,
      "Niet waar. Bedrijven buiten de EU ervaren minder last van strenge regels.", 40),
    W("Milieu, mens en bestuur zijn volgens bron 30 inmiddels vaste waarden voor bedrijven in Nederland.", True,
      "Waar. Zo begint de tekst.", 40),
    W("Rapporteren over ESG is volgens bron 30 vrijblijvend voor bedrijven in de EU.", False,
      "Niet waar. Bedrijven moeten rapporteren.", 40),
    I("Bron 30 komt uit het tijdschrift Geografie van november ____.", "2023", "Bron 30 is van Raffael Argiolu, Geografie, november 2023.", 40),
    I("De EU heeft bepaald dat bedrijven sinds ____ moeten rapporteren hoe ze met ESG bezig zijn.", "2024", "Sinds 2024 moeten bedrijven in de EU over ESG rapporteren.", 40),
    I("De G van ESG gaat over behoorlijk bestuur, ook in bedrijven die goederen ____.", "aanleveren|leveren", "Behoorlijk bestuur geldt ook voor bedrijven die goederen aanleveren.", 40),
    I("Bron 30 stelt dat China niet zo ____ doet.", "moeilijk", "In bron 30 staat: China doet niet zo moeilijk.", 40),
    O("Leg uit waarom verplichte ESG-regels een Europees bedrijf kunnen benadelen ten opzichte van een Chinees bedrijf.", ["achterstand/concurrentie", "minder last/minder regels/minder strenge"], 2,
      "Een Europees bedrijf kan op achterstand komen, omdat bedrijven buiten de EU minder last hebben van regels.",
      "Een achterstand in de concurrentie, want Chinese bedrijven hebben minder last van regels.", 40),
    O("Noem twee manieren waarop duurzaamheid een rol speelt in de Europese handel volgens deze paragraaf.", ["ESG/rapporteren/rapportage", "klimaat/uitdaging/toekomst"], 2,
      "Bedrijven moeten rapporteren over ESG, en klimaat en duurzaamheid zijn een uitdaging voor de toekomst van de EU-handel.",
      "ESG-rapportage en klimaat als uitdaging voor de toekomst.", 40)
]),

125: ("Examentraining bronnen en redeneren", "🎓", [
    M("Bron 26 toont een protest in Brussel in 2023. Welke vraag kun je met deze bron het best beantwoorden?",
      "Welke kritiek bestaat er op Europese regels?",
      ["Hoe groot is de koopkracht in Brussel?",
       "Welke landen willen nog toetreden tot de EU?",
       "Hoeveel steenkool wordt er in Europa gewonnen?"],
      "Bron 26 laat boeren zien die protesteren tegen stikstofmaatregelen.", 38),
    M("Bron 29 toont de assemblage in een Skoda-fabriek in Tsjechië. Welk thema uit de paragraaf illustreert dit?",
      "De groei van de industrie in Oost-Europa door EU-vrijhandel",
      ["Het sluiten van de zware industrie in West-Europa na 1990",
       "De ESG-rapportage van grote Europese bedrijven vanaf 2024",
       "Het vertrek van het Verenigd Koninkrijk uit de Unie in 2020"],
      "Tsjechië heeft van de vrijhandel geprofiteerd en de auto-industrie groeide.", 39),
    M("Waarvoor zou je bron 30 (de tekst over ESG) gebruiken?",
      "Om uit te leggen waarom bedrijven een achterstand vrezen",
      ["Om de koopkracht in Europa te vergelijken met andere delen",
       "Om de fabriekslocaties van autobouwers in kaart te brengen",
       "Om de uitslag van het Britse referendum te verklaren aan klasgenoten"],
      "Bron 30 gaat over ESG en de angst voor een achterstand.", 40),
    M("Wat bedoelt het boek met de kop 'Krimp en groei'?",
      "Krimp in oude West-Europese industriegebieden en groei in Polen en Tsjechië",
      ["Krimp van de EU door het VK en groei door nieuwe kandidaat-lidstaten",
       "Krimp van de export naar China en groei van de export naar de VS",
       "Krimp van de bevolking in het zuiden en groei in het noordwesten"],
      "Het onderdeel gaat over regio's die inkrompen en landen die groeiden.", 39),
    M("Welke is geen leerdoel van deze paragraaf?",
      "Je kunt de stappen van de Brexit stap voor stap uitleggen",
      ["Je weet welke positie Europa inneemt in de wereldhandel",
       "Je begrijpt welke gevolgen bewegingen in de wereldhandel in Europa hebben",
       "Je kunt beschrijven met welke veranderingen Europa rekening moet houden"],
      "De drie leerdoelen gaan over de positie van Europa, de gevolgen en de veranderingen.", 38),
    M("Welk probleem blijkt uit bron 26 en bron 30 samen?",
      "Strenge duurzaamheidsregels geven weerstand bij boeren en bedrijven",
      ["Open grenzen veroorzaken een tekort aan arbeiders in de industrie",
       "Vrijhandel veroorzaakt een sterke stijging van de koopkracht overal",
       "Grondstoffen veroorzaken ruzie tussen Oost- en West-Europa"],
      "Boeren protesteren tegen stikstofregels, bedrijven vrezen een achterstand door ESG.", 40),
    M("Een klasgenoot zegt: 'Vrijhandel in de EU is alleen goed voor Oost-Europa.' Welk tegenargument past bij het boek?",
      "Door verplaatsing van fabrieken verdwenen banen in landen als Duitsland",
      ["Oost-Europese landen zijn nooit gegroeid door de vrijhandel in de EU",
       "In Duitsland namen de banen toe doordat fabrieken naar buiten vertrokken",
       "Vrijhandel was alleen mogelijk binnen de eigen landsgrenzen van elk bedrijf"],
      "Verplaatsing naar Tsjechië betekende verlies van banen in Duitsland.", 39),
    M("Politieke spanningen met een grote handelspartner (VS, VK of China). Wat is een risico voor de Europese export?",
      "Het kan lastiger worden om daar te verkopen",
      ["De interne markt verdwijnt direct en volledig",
       "Alle vrijhandelsverdragen worden daardoor automatisch verlengd",
       "De lidstaten verliezen hun open binnengrenzen meteen"],
      "Politieke spanningen noemt het boek als factor voor het succes van de EU.", 39),
    M("Welke conclusie past bij de paragraaf als geheel?",
      "Europa profiteert van de wereldhandel, maar kent ook krimp en nieuwe uitdagingen",
      ["Europa heeft geen enkel probleem meer door de wereldhandel",
       "Europa verliest alle export en moet zich daarom volledig afsluiten",
       "Europa bestaat inmiddels uit één overal gelijk welvarende economie"],
      "De paragraaf laat kansen en problemen zien.", 41),
    W("Bron 29 laat een voorbeeld zien van industriegroei in Oost-Europa.", True,
      "Waar. Het gaat om de assemblage in een Skoda-fabriek in Tsjechië.", 39),
    W("Bron 26 toont boeren die in Brussel protesteren voor strengere stikstofregels.", False,
      "Niet waar. Ze protesteren juist tegen stikstofmaatregelen.", 38),
    W("Nederland is volgens het boek geen van de oprichters van de EU.", False,
      "Niet waar. Nederland is een van de grondleggers.", 38),
    W("De EU kan door de uitdagingen kiezen voor meer bescherming van de eigen interne markt.", True,
      "Waar. Dat is een mogelijk gevolg.", 39),
    W("Volgens het boek is de VS geen belangrijke exportbestemming van de EU.", False,
      "Niet waar. De VS, het VK en China worden genoemd.", 39),
    I("Het succes van de EU hangt af van politieke spanningen, klimaat, technologie en ____.", "duurzaamheid",
      "Duurzaamheid wordt als uitdaging genoemd.", 39),
    I("De automerken Skoda, Toyota, Peugeot, Citroën, DS Automobile en ____ hebben allemaal fabrieken in Tsjechië.", "Hyundai", "Hyundai heeft net als de andere merken een fabriek in Tsjechië.", 39),
    I("In Tsjechië groeide dankzij de vrijhandel binnen de EU de ____-industrie.", "auto|auto's", "In Tsjechië groeide de auto-industrie.", 38),
    I("Concurrentie uit landen met zeer lage loonkosten komt volgens de tekst uit ____landen.", "lagelonen",
      "Dat zijn lagelonenlanden.", 39),
    O("Vergelijk de economische ontwikkeling van oude West-Europese industriegebieden met die van Polen en Tsjechië.", ["werkloosheid/sluiten/sluiting/krimp", "groei"], 2,
      "In oude West-Europese industriegebieden sloten bedrijven en liep de werkloosheid op, terwijl Polen en Tsjechië groeiden.",
      "Krimp en werkloosheid in het westen, groei in Polen en Tsjechië.", 39),
    O("Noem twee regels of maatregelen vanuit de EU waar bedrijven of inwoners iets van merken.", ["rapporteren/ESG", "stikstof/stikstofmaatregelen", "controle/investeringen"], 2,
      "Bedrijven moeten rapporteren over ESG, boeren krijgen stikstofmaatregelen en de EU controleert buitenlandse investeringen.",
      "ESG-rapportage, stikstofmaatregelen en controle op investeringen.", 39)
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('ak_h1_4_extra2_seed_121')
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
            "paragraaf": "1.4",
            "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
            "titel": f"Toets {nr} — §1.4 {sub}",
            "vak": "Aardrijkskunde · HAVO 3 (H1)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 §1.4) — gegenereerd door tools/gen_aardrijkskunde_h1_4_extra2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
