#!/usr/bin/env python3
"""Biologie HAVO 3 · Hoofdstuk 11 Voortplanting · §11.3 Zwangerschap (extra toetsen 57–61).
Schrijft havo3/biologie/js/data/examen_57..61.js (ex-h3-biologie-57..61).
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


EXAMENS = {
57: ("Groei van het ongeboren kind (bron 4)", "📏", [
    M("Een foetus weegt volgens bron 4 ongeveer 1000 g. Hoe oud is het kindje dan?",
      "Ongeveer zes maanden",
      ["Ongeveer twee maanden", "Ongeveer vier maanden", "Ongeveer negen maanden"],
      "In bron 4 weegt de foetus van zes maanden 1000 g en is hij 38 cm lang."),
    M("Tussen welke twee opeenvolgende foto's in bron 4 komt het kindje de meeste gram aan?",
      "Tussen de foto's van 6 en 9 maanden",
      ["Tussen de foto's van 1 en 2 maanden", "Tussen de foto's van 3 en 4 maanden", "Tussen de foto's van 4 en 5 maanden"],
      "Van 6 naar 9 maanden groeit het gewicht van 1000 g naar 3300 g: ruim 2000 g erbij."),
    M("Wat is volgens bron 4 al te zien bij het embryo van twee maanden?",
      "Het hartje klopt al en ledematen en ogen zijn te zien",
      ["Het kindje weegt al 320 g en is 25 cm lang", "Het kindje heeft al duidelijk wenkbrauwen en oogleden", "Het kindje is groot genoeg voor de geboorte"],
      "Het embryo van twee maanden is 4,5 cm en 5 g; het hartje klopt al en ledematen en ogen zijn te zien."),
    M("Wat gebeurt er volgens bron 4 vooral in de zesde maand?",
      "De hersenen ontwikkelen zich snel",
      ["De lippen, oogleden en wenkbrauwen worden afgemaakt", "Het hartje begint voor het eerst te kloppen", "Het kindje is volgroeid en klaar voor de geboorte"],
      "Bij de foetus van zes maanden staat in bron 4 dat de hersenen zich snel ontwikkelen."),
    M("Een vrouw is acht weken zwanger, maar niemand ziet het aan haar buik. Hoe komt dat?",
      "Het embryo is nog heel klein, een paar centimeter",
      ["Het embryo ligt nog buiten de baarmoeder", "De baarmoeder groeit pas na de geboorte", "De foetus heeft nog geen organen nodig"],
      "Het embryo is na twee maanden pas 4,5 cm; de buik wordt pas rond twintig weken dikker."),
    M("Welke volgorde van gebeurtenissen klopt, van vroeg naar laat?",
      "Hartje klopt, organen aangelegd, wenkbrauwen af, klaar voor de geboorte",
      ["Organen aangelegd, hartje klopt, klaar voor de geboorte, wenkbrauwen af",
       "Wenkbrauwen af, hartje klopt, organen aangelegd, klaar voor de geboorte",
       "Klaar voor de geboorte, wenkbrauwen af, organen aangelegd, hartje klopt"],
      "Bron 4: hartje bij 2 maanden, alle organen bij 3 maanden, wenkbrauwen bij 5 maanden, geboorteklaar bij 9 maanden."),
    M("Het embryo van één maand is 5 mm lang en het kind van negen maanden 50 cm. Ongeveer hoeveel keer zo lang is het kind?",
      "Ongeveer 100 keer zo lang",
      ["Ongeveer 10 keer zo lang", "Ongeveer 50 keer zo lang", "Ongeveer 1000 keer zo lang"],
      "50 cm is 500 mm, en 500 gedeeld door 5 is 100."),
    M("Welke bewering over bron 4 klopt?",
      "Een foetus van 3 maanden is 9 cm lang en weegt 60 g",
      ["Een embryo van 2 maanden is 25 cm lang en weegt 320 g", "Een foetus van 5 maanden is 50 cm lang en weegt 1000 g", "Een foetus van 9 maanden is 9 cm lang en weegt 60 g"],
      "De waarden uit de andere beweringen horen bij andere leeftijden in bron 4."),
    M("Op de foto van welke leeftijd in bron 4 zijn voor het eerst alle organen aangelegd?",
      "Drie maanden",
      ["Twee maanden", "Vijf maanden", "Negen maanden"],
      "Bij de foetus van drie maanden staat: alle organen zijn aangelegd."),
    W("Volgens bron 4 weegt een foetus van vier maanden meer dan 1000 g.", False,
      "Niet waar. Een foetus van vier maanden weegt ongeveer 200 g."),
    W("Het embryo van twee maanden weegt volgens bron 4 meer dan 100 g.", False,
      "Niet waar. Het embryo van twee maanden weegt 5 g."),
    W("Het embryo van één maand heeft volgens bron 4 al lippen, oogleden en wenkbrauwen.", False,
      "Niet waar. Die zijn pas bij de foetus van vijf maanden af."),
    W("Een foetus van zes maanden is volgens bron 4 langer dan 30 cm.", True,
      "Waar. Hij is 38 cm lang."),
    W("Bij de foetus van drie maanden zijn de lippen, oogleden en wenkbrauwen volgens bron 4 al af.", False,
      "Niet waar. Dat is pas bij vijf maanden zo; bij drie maanden zijn de organen aangelegd."),
    I("Een baby die klaar is voor de geboorte weegt volgens bron 4 ongeveer ____ gram.", "3300|3300 g|3300 gram",
      "Bron 4: de baby van negen maanden is 50 cm lang en weegt 3300 g."),
    I("De foetus van vier maanden is volgens bron 4 ongeveer ____ cm lang.", "20|20 cm",
      "Bron 4: foetus van 4 maanden, 20 cm en 200 g."),
    I("Het embryo van twee maanden is 4,5 cm lang en weegt volgens bron 4 ongeveer ____ gram.", "5|5 g|5 gram",
      "Bron 4: embryo van 2 maanden, 4,5 cm en 5 g."),
    I("Op de foto van zes maanden in bron 4 meet de foetus ____ cm.", "38|38 cm",
      "Bron 4: foetus van 6 maanden, 38 cm en 1000 g."),
    O("Een vrouw is acht weken zwanger. Leg uit waarom je daar aan haar buik nog niets van ziet.", ["klein/cm", "twintig/20/later"], 2,
      "Het embryo is nog heel klein, enkele centimeters. Pas rond twintig weken wordt de buik dikker.",
      "Het kindje is in de eerste twaalf weken nog klein; pas later, rond twintig weken, wordt de buik duidelijk dikker."),
    O("Noem twee verschillen tussen de foetus van drie maanden en die van negen maanden volgens bron 4.", ["lengte/langer/cm", "gewicht/zwaarder/gram"], 2,
      "De baby van negen maanden is veel langer (50 cm tegen 9 cm) en veel zwaarder (3300 g tegen 60 g).",
      "Het kind van negen maanden is langer en zwaarder en klaar voor de geboorte.")
]),
58: ("Placenta en navelstreng toepassen", "🔗", [
    M("Het bloed in de navelstrengader bevat veel zuurstof. Waar komt die zuurstof vandaan?",
      "Uit het bloed van de moeder, via de placenta",
      ["Uit de eigen longen van de foetus, die al ademen", "Uit het vruchtwater dat rond de foetus zit", "Uit de vruchtvliezen om de hele zak heen"],
      "De zuurstof gaat in de placenta van het bloed van de moeder naar het bloed van de foetus."),
    M("Een moeder eet een boterham. Hoe komen de voedingsstoffen daaruit bij het kindje?",
      "Via haar bloed, de placenta en de navelstreng",
      ["Via het vruchtwater, dat het kindje opdrinkt", "Via de vruchtvliezen, die stoffen doorlaten", "Direct door de huid van het kindje"],
      "Voedingsstoffen gaan via het bloed van de moeder door de placenta en de navelstrengader naar het kindje."),
    M("Welke bewering over de navelstreng is onjuist?",
      "Hij verbindt het kindje met de vruchtvliezen",
      ["Er lopen drie bloedvaten doorheen", "De navelstrengader brengt zuurstof naar het kindje", "Het stompje valt na enkele dagen af"],
      "De navelstreng verbindt het kindje met de placenta, niet met de vruchtvliezen."),
    M("Wat is het verschil tussen de taak van de vruchtvliezen en die van de placenta?",
      "De vliezen beschermen tegen stoten; de placenta zorgt voor uitwisseling van stoffen",
      ["De vliezen zorgen voor uitwisseling van stoffen; de placenta beschermt tegen stoten",
       "De vliezen voeren afvalstoffen af; de placenta houdt het vruchtwater vast",
       "De vliezen en de placenta doen precies hetzelfde werk"],
      "De vruchtvliezen met vruchtwater beschermen; in de placenta worden stoffen uitgewisseld."),
    M("Wat is de juiste route van zuurstof van moeder naar kind?",
      "Bloed moeder, placenta, navelstrengader, foetus",
      ["Bloed moeder, navelstrengslagader, placenta, foetus", "Foetus, navelstrengader, placenta, bloed moeder", "Placenta, bloed moeder, vruchtwater, foetus"],
      "Zuurstof gaat van het bloed van de moeder via de placenta en de navelstrengader naar de foetus."),
    M("De moeder stoot haar buik tegen een tafel. Welk deel beschermt het kindje daartegen?",
      "Het vruchtwater in de vruchtvliezen",
      ["De placenta, die als filter werkt", "De navelstreng, die om het kindje ligt", "De navelstrengslagaders"],
      "Vruchtvliezen met vruchtwater beschermen het kindje tegen stoten."),
    M("De verloskundige knijpt de navelstreng dicht en knipt hem door. Wat stopt hierdoor?",
      "De uitwisseling van stoffen tussen moeder en kind",
      ["Het beschermen tegen stoten door het vruchtwater", "De groei van de melkklieren van de moeder", "Het samentrekken van de baarmoeder"],
      "Zonder navelstreng is er geen verbinding met de placenta meer; de baby moet zelf ademen."),
    M("Hoeveel bloedvaten in de navelstreng vervoeren bloed van de foetus naar de placenta?",
      "Twee",
      ["Eén", "Drie", "Geen enkele"],
      "De twee navelstrengslagaders vervoeren het bloed van de foetus naar de placenta."),
    M("Wat gebeurt er met het bloed van de foetus dat via de navelstrengslagaders bij de placenta aankomt?",
      "Afvalstoffen gaan door de dunne vaatwand naar het bloed van de moeder",
      ["Het bloed stroomt rechtstreeks in de bloedvaten van de moeder", "Het bloed wordt in de placenta bewaard tot de geboorte", "Het bloed gaat via het vruchtwater naar buiten"],
      "In de placenta worden afvalstoffen uitgewisseld door de dunne wanden van de bloedvaten."),
    W("Het bloed in de navelstrengader bevat meer zuurstof dan het bloed in de navelstrengslagaders.", True,
      "Waar. De ader brengt zuurstof naar de foetus; de slagaders voeren afvalstoffen af."),
    W("De navelstrengslagaders vervoeren bloed van de placenta naar de foetus.", False,
      "Niet waar. Dat doet de navelstrengader; de slagaders vervoeren bloed van de foetus naar de placenta."),
    W("De foetus ademt in de baarmoeder zelf lucht in en uit.", False,
      "Niet waar. Pas zodra de baby geboren is, gaat hij zelf ademen."),
    W("De placenta groeit op de plaats waar de bevruchte eicel zich heeft ingenesteld.", True,
      "Waar. Daar groeit de moederkoek."),
    W("De placenta en de navelstreng vormen samen de zak met vloeistof waarin het kindje ligt.", False,
      "Niet waar. Die zak bestaat uit vruchtvliezen met vruchtwater."),
    I("Het bloed van moeder en kind komt in de placenta dicht langs elkaar, maar wordt niet ____.", "gemengd|vermengd",
      "De bloedvaten liggen dicht langs elkaar; stoffen worden uitgewisseld, het bloed mengt niet."),
    I("De placenta wordt ook wel de ____ genoemd.", "moederkoek|de moederkoek", "Placenta en moederkoek zijn hetzelfde."),
    I("Via de navelstrengslagaders gaan afvalstoffen, zoals ____, van het kindje naar de moeder.", "koolstofdioxide|CO2|co2", "Afvalstoffen zoals koolstofdioxide gaan via de navelstrengslagaders naar de moeder."),
    I("De placenta houdt veel schadelijke stoffen en ____ tegen.", "ziekteverwekkers|ziekteverwekker", "Veel schadelijke stoffen en ziekteverwekkers worden tegengehouden."),
    O("Leg uit waarom een schadelijke stof uit het bloed van de moeder toch bij het kindje kan komen, ook al werkt de placenta als filter.", ["dun/dicht", "alcohol/nicotine/drugs/rodehond/virus"], 2,
      "In de placenta liggen de bloedvaten dicht langs elkaar met dunne wanden, zodat stoffen worden uitgewisseld. Het filter houdt niet alles tegen: alcohol, nicotine, drugs en het rodehondvirus komen er wel doorheen.",
      "Het filter werkt maar gedeeltelijk: bij de dunne vaatwanden in de placenta kunnen onder andere alcohol en nicotine toch doorheen."),
    O("Noem twee verschillen tussen de navelstrengader en de navelstrengslagaders.", ["zuurstof/voedingsstoffen", "afvalstoffen/koolstofdioxide/afval"], 2,
      "De ader (één) vervoert zuurstof en voedingsstoffen naar het kindje; de slagaders (twee) vervoeren afvalstoffen, zoals koolstofdioxide, naar de placenta.",
      "De ader brengt zuurstof en voedingsstoffen naar het kind; de slagaders voeren afvalstoffen af.")
]),
59: ("Schadelijke stoffen en risico's", "🚭", [
    M("Hoe verandert volgens de tekst en bron 7 het risico van rodehond voor het kind in de eerste vier maanden?",
      "Het risico is het grootst bij besmetting in de eerste weken",
      ["Het risico is het grootst vlak voor het einde van de vierde maand", "Het risico blijft in alle weken precies gelijk", "Het risico bestaat alleen na de twaalfde week"],
      "Schadelijke stoffen hebben vooral veel effect in de eerste weken van de zwangerschap."),
    M("Een vrouw krijgt in week 5 rodehond en voelt zich nauwelijks ziek. Wie loopt het meeste risico?",
      "Het ongeboren kind, dat afwijkingen kan krijgen",
      ["Alleen de vrouw, die er heel ziek van wordt", "De verloskundige die haar onderzoekt", "Niemand, want de placenta houdt het virus tegen"],
      "Rodehond is niet gevaarlijk, behalve voor ongeboren kinderen; het virus komt via de placenta bij het embryo."),
    M("Welke combinatie noemt alleen stoffen die schadelijk zijn voor het ongeboren kind?",
      "Alcohol, nicotine en drugs",
      ["Zuurstof, voedingsstoffen en water", "Vruchtwater, nicotine en zuurstof", "Voedingsstoffen, alcohol en water"],
      "Alcohol, nicotine en drugs zijn schadelijk; zuurstof en voedingsstoffen heeft het kindje juist nodig."),
    M("Een kind is kleiner dan leeftijdsgenoten en heeft een verstandelijke beperking. Welke oorzaak past hierbij?",
      "Alcoholgebruik van de moeder tijdens de zwangerschap",
      ["Roken van de vader tijdens de bevalling", "Een keizersnede bij de geboorte", "Een stuitligging vlak voor de geboorte"],
      "Foetaal Alcohol Syndroom: de hersenen groeien niet goed, het kind is vaker verstandelijk beperkt en kleiner."),
    M("Een ziekenhuis volgt 200 zwangerschappen. Bij ongeveer hoeveel gaat er aan het begin van de zwangerschap iets mis met het embryo?",
      "Bij ongeveer 20",
      ["Bij ongeveer 10", "Bij ongeveer 50", "Bij ongeveer 2"],
      "Bij 1 op de 10 zwangerschappen gaat er iets mis; 1 op 10 van 200 is 20."),
    M("Waarom kan een vrouw met een zwangerschapsvermoeden beter meteen stoppen met roken?",
      "Schadelijke stoffen hebben vooral veel effect in de eerste weken",
      ["De placenta laat pas na de eerste maanden stoffen door", "Nicotine schaadt het kindje pas na de geboorte", "De vruchtvliezen beschermen in het begin nog niet"],
      "In de eerste weken ontstaan de organen, daarom is schade dan het grootst."),
    M("Welk effect van schadelijke stoffen noemt de tekst niet?",
      "Het kindje groeit sneller dan normaal",
      ["Het kindje groeit slechter dan normaal", "Het kindje kan afwijkingen krijgen", "Het kindje kan doodgaan"],
      "Volgens de tekst gaat het kindje slechter groeien, kan het afwijkingen krijgen of doodgaan."),
    M("Wat hebben alcohol, drugs, nicotine en het rodehondvirus gemeen?",
      "Ze kunnen alle vier via de placenta bij het embryo komen",
      ["Ze worden alle vier door de vruchtvliezen tegengehouden", "Ze veroorzaken alle vier hetzelfde syndroom FAS", "Ze zijn alle vier alleen schadelijk in de laatste maanden"],
      "De tekst noemt deze vier als stoffen die wél via de placenta bij het embryo kunnen komen."),
    M("Wat is de juiste volgorde van oorzaak naar gevolg bij Foetaal Alcohol Syndroom?",
      "Alcohol in bloed moeder, in bloed foetus, hersenen groeien slecht, FAS",
      ["Hersenen groeien slecht, alcohol in bloed moeder, in bloed foetus, FAS", "Alcohol in bloed foetus, in bloed moeder, FAS, hersenen groeien slecht", "FAS, alcohol in bloed moeder, in bloed foetus, hersenen groeien slecht"],
      "Alcohol komt via de placenta bij de foetus; de hersenen groeien niet goed en het kind krijgt FAS."),
    W("Een besmetting met rodehond in week 8 is gevaarlijker voor het kind dan in week 15.", True,
      "Waar. Bron 7: de kans op ernstige afwijkingen is het grootst in de eerste weken."),
    W("Rodehond is een ziekte die vooral gevaarlijk is voor kinderen van vijf jaar.", False,
      "Niet waar. De ziekte is niet gevaarlijk, behalve voor ongeboren kinderen."),
    W("Schadelijke stoffen die de placenta passeren, kunnen ervoor zorgen dat het kindje doodgaat.", True,
      "Waar. Het kindje kan slechter groeien, afwijkingen krijgen of doodgaan."),
    W("Een kind met FAS heeft vaker een verstandelijke beperking, maar is niet kleiner dan leeftijdsgenoten.", False,
      "Niet waar. Een kind met FAS is ook kleiner dan leeftijdsgenoten."),
    W("Een miskraam komt alleen voor na de twintigste week van de zwangerschap.", False,
      "Niet waar. Een miskraam komt vooral voor in de eerste twaalf weken."),
    I("Nicotine in het bloed van een zwangere vrouw komt uit ____.", "sigaretten|sigaret", "Nicotine komt uit sigaretten."),
    I("Het rodehondvirus kan bij ongeboren kinderen oogafwijkingen en ____verlies veroorzaken.", "gehoor",
      "Rodehond kan oogafwijkingen en gehoorverlies geven."),
    I("Bij een op de tien zwangerschappen gaat er in de eerste ____ weken iets mis met het embryo.", "twaalf|12",
      "Dat gebeurt in de eerste twaalf weken."),
    I("Rodehond is een ____ ziekte.", "besmettelijke|besmettelijk", "Rodehond is een besmettelijke ziekte."),
    O("Leg uit waarom een besmetting met rodehond in week 6 gevaarlijker is dan in week 16, ook al is de ziekte zelf niet gevaarlijk voor de moeder.", ["eerste weken/vroeg/begin", "afwijking/oogafwijking/gehoorverlies"], 2,
      "Schadelijke stoffen hebben vooral veel effect in de eerste weken van de zwangerschap. Dan kan het kindje ernstige afwijkingen krijgen, zoals oogafwijkingen en gehoorverlies.",
      "Vooral in de eerste weken is het kind kwetsbaar; het kan dan afwijkingen krijgen."),
    O("Een vriendin is zwanger en rookt. Welk advies geef je haar, en hoe bereikt de schadelijke stof het kindje?", ["placenta", "afwijking/doodgaan/slechter"], 2,
      "Ze moet stoppen: nicotine komt via de placenta bij het embryo. Het kindje gaat slechter groeien, kan afwijkingen krijgen of doodgaan.",
      "De nicotine passeert de placenta; het kindje kan slechter groeien, afwijkingen krijgen of doodgaan.")
]),
60: ("De bevalling toepassen", "👶", [
    M("Een vrouw heeft regelmatige weeën en haar vruchtwater loopt weg. In welke fase zit ze?",
      "De ontsluiting",
      ["De uitdrijving", "De nageboorte", "De indaling"],
      "Bij de ontsluiting gaat de baarmoedermond open en breken de vruchtvliezen."),
    M("De verloskundige zegt dat de baarmoedermond ver genoeg open is. Wat volgt er nu?",
      "Sterke persweeën duwen de baby naar buiten",
      ["De baby draait met het hoofdje naar beneden", "De vruchtvliezen en placenta komen naar buiten", "De navelstreng valt vanzelf af"],
      "Als de baarmoedermond ver genoeg open is, begint de uitdrijving."),
    M("Welke ligging van de baby maakt een geboorte via de vagina onmogelijk?",
      "Dwarsligging",
      ["Stuitligging", "Hoofdje tegen de baarmoedermond", "Hoofdje naar beneden na de indaling"],
      "Bij een dwarsligging kan de baby niet via de vagina geboren worden; dan volgt een keizersnede."),
    M("De indalingsweeën beginnen gemiddeld zes weken voor de bevalling. Rond welke week beginnen ze bij een zwangerschap van veertig weken?",
      "Rond week 34",
      ["Rond week 28", "Rond week 40", "Rond week 12"],
      "40 min 6 is 34."),
    M("Wat is het verschil tussen indalingsweeën en persweeën?",
      "Indalingsweeën laten het kindje goed liggen; persweeën duwen het naar buiten",
      ["Indalingsweeën duwen het kindje naar buiten; persweeën openen de baarmoedermond",
       "Indalingsweeën komen na de geboorte; persweeën komen er vóór",
       "Indalingsweeën zijn de weeën bij de nageboorte; persweeën bij de ontsluiting"],
      "Indalingsweeën zorgen voor de indaling; persweeën duwen de baby tijdens de uitdrijving naar buiten."),
    M("Waar maakt de chirurg bij een keizersnede een snee?",
      "Onder in de buik van de vrouw",
      ["Boven in de buik tegen de ribben", "In de wand van de vagina", "Aan de rugzijde van de vrouw"],
      "Bij een keizersnede maakt de chirurg een snee onder in de buik."),
    M("In welke volgorde verlaat wat het lichaam van de moeder bij de bevalling?",
      "Eerst de baby; daarna de placenta met vruchtvliezen en navelstrengresten",
      ["Eerst het vruchtwater; daarna de baby", "Eerst de placenta; daarna de baby", "Baby en placenta komen tegelijk naar buiten"],
      "Bij de uitdrijving komt de baby, bij de nageboorte de placenta met vruchtvliezen en resten navelstreng."),
    M("Hoe merkt een zwangere vrouw dat de indaling heeft plaatsgevonden?",
      "Haar buik zit lager",
      ["Haar buik zit hoger onder de ribben", "Haar buik wordt plotseling dunner doordat het kindje stopt met groeien", "Ze voelt het kindje voor het eerst bewegen"],
      "In bron 9 zit de buik na het indalen lager, omdat het hoofdje naar beneden ligt."),
    M("Welke fase van de bevalling hoort bij het openen van de baarmoedermond door weeën?",
      "De ontsluiting",
      ["De nageboorte", "De indaling", "De uitdrijving"],
      "Door de weeën gaat de baarmoedermond open; dat heet ontsluiting."),
    W("De placenta komt pas naar buiten nadat de baby geboren is.", True,
      "Waar. Dat gebeurt in de derde fase, de nageboorte."),
    W("Bij een keizersnede wordt de baby via de vagina geboren.", False,
      "Niet waar. De baby wordt via een snee onder in de buik gehaald."),
    W("De navelstreng wordt met één klem afgebonden en daarna doorgeknipt.", False,
      "Niet waar. De navelstreng wordt dichtgeknepen met twee klemmetjes en tussen die klemmetjes doorgeknipt."),
    W("Het stompje van de navelstreng valt na een paar dagen af.", True,
      "Waar. Het litteken dat overblijft is de navel."),
    W("Indalingsweeën zorgen ervoor dat de baarmoedermond opengaat.", False,
      "Niet waar. Indalingsweeën zorgen ervoor dat het kindje met het hoofdje naar beneden komt te liggen."),
    I("Bij een stuitligging worden de ____ eerst geboren en dan pas het hoofdje.", "billen", "Bij een stuitligging komen eerst de billen."),
    I("De navelstreng wordt tussen twee ____ doorgeknipt.", "klemmetjes|klemmen|klemmetje", "De verloskundige knijpt de navelstreng dicht met twee klemmetjes en knipt hem daartussen door."),
    I("De bevalling begint als de weeën met regelmatige ____ komen.", "tussenpozen",
      "Regelmatige tussenpozen zijn het teken dat de bevalling begint."),
    I("Vlak voor of tijdens de ontsluiting breken de ____ en loopt het vruchtwater naar buiten.", "vruchtvliezen|vliezen",
      "Als de vruchtvliezen breken, loopt het vruchtwater via de vagina naar buiten."),
    O("Een vrouw verwacht haar kindje over zes weken. Wat gebeurt er in die periode met het kindje en met haar buik?", ["lager/zakt", "hoofd/hoofdje"], 2,
      "De indalingsweeën beginnen: het kindje draait met het hoofdje naar beneden en ligt tegen de baarmoedermond. Haar buik zit hierdoor lager.",
      "Het kindje daalt in met het hoofdje naar beneden en de buik zit lager."),
    O("Leg uit waarom de baarmoedermond eerst moet opengaan voordat de baby geboren kan worden.", ["pers", "vagina/naar buiten"], 2,
      "Door de weeën gaat de baarmoedermond open (ontsluiting). Pas als hij ver genoeg open is, kunnen sterke persweeën de baby door de vagina naar buiten duwen.",
      "De baarmoedermond is de doorgang; pas als hij open is, duwen persweeën de baby via de vagina naar buiten.")
]),
61: ("Tweelingen, meerlingen en eicellen vergelijken", "👯", [
    M("Waar rijpen vaak de eicellen waaruit een twee-eiige tweeling ontstaat?",
      "In beide eierstokken tegelijk",
      ["Alleen in de linker eierstok", "In de baarmoeder na de bevruchting", "In de eileiders vlak na de innesteling"],
      "Vaak rijpt in beide eierstokken tegelijk een eicel."),
    M("Een echo toont twee kindjes die één placenta delen. Wat voor tweeling is dit?",
      "Eeneiig, met splitsing na de innesteling",
      ["Twee-eiig, met twee zaadcellen", "Twee-eiig, met twee eisprongen", "Eeneiig, met splitsing vóór de innesteling"],
      "Een twee-eiige tweeling heeft altijd twee placenta's; delen van een placenta komt alleen voor bij eeneiige tweelingen met late splitsing."),
    M("Welke volgorde beschrijft het ontstaan van een eeneiige tweeling?",
      "Bevruchting, splitsing van het bolletje cellen, innesteling, groei tot twee baby's",
      ["Splitsing van het bolletje cellen, bevruchting, innesteling, groei tot twee baby's", "Innesteling, bevruchting, splitsing van het bolletje cellen, groei tot twee baby's", "Bevruchting, innesteling, groei tot twee baby's, splitsing van het bolletje cellen"],
      "Eerst één bevruchting; tijdens de eerste delingen splitst het bolletje cellen zich in tweeën, daarna nestelen beide zich in."),
    M("De kans op een drieling is 1 op 6400, op een vierling 1 op een half miljoen. Hoeveel keer zo groot is de kans op een drieling?",
      "Ongeveer 80 keer zo groot",
      ["Ongeveer 8 keer zo groot", "Ongeveer 800 keer zo groot", "Ongeveer 8000 keer zo groot"],
      "500 000 gedeeld door 6400 is ongeveer 78."),
    M("Een ei heeft een taai vlies, geen laag gelei en geen kalkschaal. Van welk dier is het ei?",
      "Een vis",
      ["Een kip", "Een mens", "Een kikker"],
      "Een vissenei heeft alleen een taai vlies om de eicel."),
    M("Wat gebeurt er met een vogelei dat op het land ligt, als de kalkschaal ontbreekt?",
      "Het ei droogt uit",
      ["Het ei gaat vanzelf drijven", "Het embryo krijgt meer zuurstof", "Het embryo groeit sneller"],
      "De kalkschaal voorkomt dat het ei uitdroogt."),
    M("Welk onderdeel van een kippenei is de eigenlijke eicel?",
      "De dooier",
      ["Het eiwit", "De kalkschaal", "De luchtkamer"],
      "De dooier (eigeel) is de eigenlijke eicel en bevat het voedsel voor het embryo."),
    M("Een eeneiige tweeling lijkt sprekend op elkaar. Welk gegeven verklaart dat?",
      "Ze zijn ontstaan uit dezelfde bevruchte eicel",
      ["Ze komen uit dezelfde eierstok", "Ze delen altijd dezelfde placenta", "Ze zijn op hetzelfde moment geboren"],
      "Beide baby's ontstaan uit één bevruchte eicel."),
    M("Welke bewering over meerlingen is onjuist?",
      "Een vijfling komt natuurlijk even vaak voor als een tweeling",
      ["Een drieling komt ongeveer 1 keer op 6400 zwangerschappen voor", "Met meer baby's is er minder ruimte voor elke baby", "Bij een meerling is vroeggeboorte vaker een risico"],
      "Een vijfling is natuurlijk uiterst zeldzaam: 1 op de 40 miljoen."),
    W("Als bij een eeneiige tweeling de splitsing vóór de innesteling plaatsvindt, krijgt ieder embryo een eigen placenta.", True,
      "Waar. Alleen bij late splitsing delen ze de placenta."),
    W("Een twee-eiige tweeling ontstaat doordat één bevruchte eicel zich in tweeën splitst.", False,
      "Niet waar. Dat geldt voor een eeneiige tweeling; twee-eiig komt uit twee bevruchte eicellen."),
    W("Een vissenei bevat geen reservevoedsel voor het embryo.", False,
      "Niet waar. Het vissenei bevat reservevoedsel: dooier."),
    W("Een twee-eiige tweeling kan bestaan uit twee jongens.", True,
      "Waar. Het kunnen zussen of broers zijn, maar ook broer en zus."),
    W("De eicel van een zoogdier is omgeven door een harde kalkschaal.", False,
      "Niet waar. De eicel van een zoogdier is klein en heeft geen schaal."),
    I("Een twee-eiige tweeling ontstaat uit twee eicellen die bij de ____ tegelijk vrijkomen.", "eisprong",
      "Bij de eisprong komen twee eicellen tegelijk vrij."),
    I("Bij een vissenei blijft de ____ onderaan het visje bungelen.", "dooierzak",
      "Volgens bron 15 blijft de dooierzak onderaan hangen."),
    I("De laag gelei in een ei bestaat uit ____ en beschermt tegen stoten.", "eiwit",
      "De laag gelei bestaat uit eiwit, beschermt tegen stoten en levert vocht."),
    I("Zoogdieren 'leggen' hun eicellen als het ware in het ____.", "lichaam",
      "Het embryo groeit in de baarmoeder, dus binnen het lichaam van de moeder."),
    O("Twee baby's delen één placenta. Leg uit hoe dit bij een tweeling kan ontstaan.", ["eeneiig", "splits/innesteling"], 2,
      "Het is een eeneiige tweeling: het bolletje cellen splitste pas na de innesteling, zodat de embryo's de placenta en vruchtvliezen delen (bij 1 procent).",
      "Eeneiig, met splitsing na de innesteling."),
    O("Een moeder krijgt tegelijk een jongen en een meisje. Leg uit dat dit geen eeneiige tweeling kan zijn.", ["geslacht", "twee-eiig/twee eicellen"], 2,
      "Een eeneiige tweeling heeft altijd hetzelfde geslacht. Een jongen en een meisje zijn een twee-eiige tweeling uit twee eicellen.",
      "Eeneiig betekent hetzelfde geslacht; jongen en meisje komen uit twee eicellen.")
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_3_extra2_seed_57')
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {
            "id": f"ex-h3-biologie-{nr}",
            "hoofdstuk": 11,
            "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
            "paragraaf": "11.3",
            "titel": f"Toets {nr} — §11.3 {sub}",
            "vak": "Biologie · HAVO 3 (H11.3)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr
        }
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie H11.3) — gegenereerd door tools/gen_biologie_h11_3_extra2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
