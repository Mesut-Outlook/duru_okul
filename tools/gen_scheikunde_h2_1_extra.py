#!/usr/bin/env python3
"""Scheikunde HAVO 3 · H2 Bouwstenen van stoffen · §2.1 Macro en micro — extra proeftoetsen 50-56.
Schrijft havo3/scheikunde/js/data/examen_h2_50.js … examen_h2_56.js (ex-h3-sch-h2-50 … 56).
Bron: boek p. 60-65 (Chemie Overal) — alleen wat daar staat. mc-volgorde geseed.
Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'scheikunde', 'js', 'data')


def M(vraag, goed, fout, uitleg):
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": fout, "uitleg": uitleg}


def W(vraag, antwoord, uitleg):
    return {"type": "waaronwaar", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def I(vraag, antwoord, uitleg):
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def O(vraag, sleutels, min_, model, uitleg=None):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": min_,
            "modelantwoord": model, "uitleg": uitleg or model}


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


# ---------------------------------------------------------------- inhoud
EXAMENS = {}

# 50 — begrippen macro / micro / molecuul
EXAMENS[50] = ("Begrippen macro, micro en molecuul", "📖", [
    M("Wat bedoel je in de scheikunde met het microniveau?",
      "de heel kleine deeltjes waaruit stoffen bestaan, die je niet met je zintuigen kunt waarnemen",
      ["alles wat je alleen met een loep of een microscoop kunt bekijken, zoals kleine korreltjes",
       "de kleine hoeveelheden stof die je in een reageerbuis gebruikt",
       "alle eigenschappen van een stof die je kunt meten met een thermometer"],
      "Het microniveau gaat over de heel kleine deeltjes waaruit stoffen bestaan; die kun je niet met je zintuigen waarnemen."),
    M("Op welk niveau hoort de stofeigenschap geur, die je met je neus waarneemt?",
      "op het macroniveau, want je neemt de geur met een zintuig waar",
      ["op het microniveau, want geur komt van zeer kleine deeltjes",
       "op het microniveau, want geur kun je niet zien",
       "op geen van beide niveaus, want geur is geen eigenschap van een stof"],
      "Alles van een stof wat je met je zintuigen kunt waarnemen noem je het macroniveau; geur neem je met je neus waar."),
    M("Je ruikt vanaf de andere kant van de kamer een geurstokje, maar je ziet niets van het potje naar je neus gaan. Wat volgt hieruit?",
      "De geurstof bestaat uit heel kleine, onzichtbare deeltjes die vrij kunnen bewegen",
      ["De geurstof bestaat uit één groot deeltje dat in zijn geheel door de lucht naar je neus zweeft",
       "De geurstof verdwijnt in het potje en wordt in je neus opnieuw gemaakt",
       "De geurstof is geen echte stof, want je kunt hem niet zien"],
      "De geurstof beweegt van het potje naar je neus zonder dat je het ziet, dus moet hij uit heel kleine, onzichtbare deeltjes bestaan."),
    M("Een glas zuiver water bevat heel veel moleculen. Wat geldt voor die moleculen?",
      "Ze zijn allemaal hetzelfde: watermoleculen",
      ["Ze zijn allemaal verschillend, want elk molecuul heeft een eigen vorm",
       "Ze zijn deels watermoleculen en deels luchtmoleculen",
       "Ze zijn hetzelfde, maar alleen in de vaste fase"],
      "De moleculen van een zuivere stof zijn allemaal hetzelfde; water bestaat uit watermoleculen."),
    M("Hoe groot is één triljoen volgens het boek?",
      "een 1 met achttien nullen",
      ["een 1 met zes nullen", "een 1 met negen nullen", "een 1 met twaalf nullen, net als een biljoen"],
      "Eén triljoen is een 1 met achttien nullen."),
    M("Waarom kun je één enkel molecuul niet zien?",
      "Een molecuul is zo klein dat je er pas een zichtbare stof van krijgt met heel veel moleculen",
      ["Een molecuul is doorzichtig, daarom is het niet te zien",
       "Een molecuul beweegt te snel om op te merken",
       "Een molecuul heeft geen vaste plaats in de stof"],
      "Moleculen zijn zo klein dat zelfs één suikerkorrel al triljoenen moleculen bevat; je enkele molecuul zie je niet."),
    M("Welke van deze gegevens over een zuivere stof is een eigenschap op macroniveau?",
      "het kookpunt dat je met een thermometer meet",
      ["de moleculen zitten dicht tegen elkaar aan en trillen",
       "de stof bestaat uit één soort moleculen",
       "de moleculen bewegen vrij langs elkaar"],
      "Een kookpunt kun je meten en daardoor waarnemen: dat is macroniveau. De andere opties beschrijven moleculen (microniveau)."),
    M("Welke zin is een beschrijving op microniveau?",
      "De moleculen van water en olijfolie vormen twee aparte lagen",
      ["De olijfolie drijft op het water", "Het mengsel is na het schudden troebel", "Je ziet twee vloeistoflagen in het glas"],
      "Zodra het over moleculen gaat, beschrijf je het microniveau. De andere zinnen beschrijven wat je ziet (macro)."),
    M("Waarom wil je bij scheikunde ook het microniveau gebruiken?",
      "om eigenschappen van stoffen te kunnen verklaren die je niet met waarneembare kenmerken kunt verklaren",
      ["omdat het macroniveau in de scheikunde niet bestaat",
       "omdat stoffen alleen op microniveau een geur hebben",
       "omdat je met het microniveau stoffen sneller kunt maken"],
      "Bij scheikunde wil je zo veel mogelijk eigenschappen van stoffen verklaren; veel daarvan verklaar je op microniveau."),
    M("Een stof bevat volgens een onderzoek drie verschillende soorten moleculen. Wat is deze stof?",
      "een mengsel",
      ["een zuivere stof", "een niet-ontleedbare stof", "een stof in de gasfase"],
      "Een zuivere stof bevat één soort moleculen; een mengsel bevat verschillende soorten moleculen."),
    W("Geur is een stofeigenschap die je met je neus (reukzintuig) waarneemt.", True,
      "Waar. Je neemt de geur van een stof met je reukzintuig waar; dat is macroniveau."),
    W("De geur van een stof kun je volledig verklaren met waarneembare kenmerken.", False,
      "Niet waar. Je kunt de geur niet verklaren met waarneembare kenmerken; daarvoor heb je het microniveau nodig."),
    W("De geurdeeltjes die in je neus komen, noem je moleculen.", True,
      "Waar. De geurdeeltjes die bij je neus komen, zijn moleculen."),
    W("Een triljoen is een 1 met zes nullen.", False,
      "Niet waar. Een triljoen is een 1 met achttien nullen."),
    W("Moleculen zijn zo klein dat zelfs een enkele suikerkorrel er triljoenen bevat.", True,
      "Waar. Daarom kun je een enkel molecuul niet zien."),
    I("De stof suiker bestaat op microniveau uit suiker____.", "moleculen",
      "De stof suiker bestaat uit suikermoleculen."),
    I("Alles van een stof dat je met je zintuigen kunt waarnemen, noem je het ____niveau.", "macro",
      "Wat je met je zintuigen waarneemt, hoort bij het macroniveau."),
    I("Eén triljoen is een 1 met ____ nullen. (schrijf een getal of woord)", "achttien|18",
      "Eén triljoen is een 1 met achttien nullen."),
    O("Leg uit waarom je een geurstokje in een kamer op afstand kunt ruiken, terwijl je de geurstof niet ziet reizen.",
      ["deeltjes/moleculen", "klein", "bewegen/verplaatsen/verspreiden"], 2,
      "De geurstof bestaat uit heel kleine deeltjes (moleculen) die vrij kunnen bewegen en zich zo van het potje naar je neus verplaatsen."),
    O("Leg het verschil uit tussen het macroniveau en het microniveau.",
      ["zintuigen/waarnemen/waarneembaar", "deeltjes/moleculen", "klein"], 2,
      "Het macroniveau is alles wat je met je zintuigen kunt waarnemen; het microniveau gaat over de heel kleine deeltjes (moleculen) waaruit stoffen bestaan en dat kun je niet waarnemen."),
])

# 51 — deeltjesmodel en fasen
EXAMENS[51] = ("Fasen op microniveau", "🧊", [
    M("IJs is water in de vaste fase. Wat doen de watermoleculen in een ijsblokje?",
      "Ze zitten dicht op elkaar gestapeld en trillen op hun plek",
      ["Ze bewegen vrij langs elkaar heen en blijven toch tegen elkaar aan",
       "Ze bewegen met grote snelheid op grote afstand van elkaar",
       "Ze staan helemaal stil en bewegen op geen enkele manier"],
      "In de vaste fase zitten de moleculen dicht op elkaar gestapeld en trillen ze op hun plek."),
    M("In welke fase zitten de moleculen tegen elkaar aan, maar kunnen ze vrij langs elkaar bewegen?",
      "in de vloeibare fase",
      ["in de vaste fase", "in de gasfase", "in elke fase, want de moleculen bewegen overal"],
      "In een vloeistof zitten de moleculen nog steeds tegen elkaar aan, maar ze kunnen vrij langs elkaar bewegen."),
    M("Wat gebeurt er met de moleculen als een vloeistof verdampt tot gas?",
      "Ze gaan met grote snelheid op grote afstand van elkaar bewegen",
      ["Ze gaan dichter op elkaar zitten en blijven daarna op hun plek trillen",
       "Ze blijven tegen elkaar aan zitten, maar bewegen minder snel",
       "Ze verdwijnen, want een gas bestaat niet uit moleculen"],
      "In de gasfase bewegen de moleculen op grote snelheid en afstand van elkaar."),
    M("Moleculen in een gas komen elkaar tegen. Wat gebeurt er dan?",
      "Ze botsen soms tegen elkaar, maar blijven niet bij elkaar zitten",
      ["Ze blijven aan elkaar vastzitten, zoals in een vloeistof",
       "Ze gaan op hun plek trillen, zoals in een vaste stof",
       "Ze botsen nooit, want ze zitten te ver uit elkaar"],
      "Moleculen in een gas botsen zo nu en dan, maar blijven niet bij elkaar zoals in de vaste en vloeibare fase."),
    M("Water smelt bij 0 °C. In welke fase is water bij -5 °C?",
      "in de vaste fase, de moleculen trillen dan op hun plek",
      ["in de vloeibare fase, de moleculen bewegen dan vrij langs elkaar",
       "in de gasfase, de moleculen bewegen dan op grote afstand van elkaar",
       "in de vloeibare fase, de moleculen staan dan ver uit elkaar"],
      "Onder het smeltpunt is water vast: de moleculen zitten dicht op elkaar gestapeld en trillen op hun plek."),
    M("Wat verandert er op microniveau als ijs smelt?",
      "De moleculen gaan vrij langs elkaar bewegen in plaats van op hun plek te trillen",
      ["De moleculen worden zelf groter en vullen daardoor steeds meer ruimte",
       "De moleculen komen ver van elkaar te zitten en bewegen heel snel",
       "De moleculen veranderen in een andere soort moleculen"],
      "Bij smelten gaat de vaste fase over in de vloeibare: de moleculen kunnen dan vrij langs elkaar bewegen."),
    M("Je giet water uit een glas in een kom en het water neemt de vorm van de kom aan. Wat is de verklaring op microniveau?",
      "De moleculen kunnen vrij langs elkaar bewegen, dus de vloeistof is makkelijk vervormbaar",
      ["De moleculen trillen op hun plek, dus de vloeistof past zich vanzelf aan de kom aan",
       "De moleculen zitten ver uit elkaar en vullen de hele kom",
       "De moleculen veranderen bij het schenken in een andere soort"],
      "Doordat moleculen in een vloeistof vrij langs elkaar bewegen, is een vloeistof op macroniveau makkelijk vervormbaar."),
    M("Waarom heb je heel veel moleculen bij elkaar nodig om een stof echt te kunnen zien?",
      "Een enkel molecuul is veel te klein; pas een enorme hoeveelheid bij elkaar zie je als stof",
      ["Moleculen worden pas zichtbaar als ze snel genoeg bewegen en botsen",
       "Moleculen zijn alleen zichtbaar als ze in de gasfase zitten",
       "Moleculen kleuren pas als ze met andere stoffen gemengd zijn"],
      "Je hebt heel veel moleculen dicht bij elkaar nodig om een stof te zien, bijvoorbeeld de triljoenen moleculen in een suikerkorrel."),
    M("Bij welke faseverandering gaat een stof direct van de vaste fase naar de gasfase?",
      "sublimeren",
      ["smelten", "verdampen", "condenseren"],
      "De vaste stof koolstofdioxide sublimeert: het gaat rechtstreeks van vast naar gas."),
    M("Een modeltekening laat bolletjes zien die dicht op elkaar gestapeld staan en op hun plek trillen. Welke macro-waarneming hoort daarbij?",
      "een stof die niet uit zichzelf van vorm verandert",
      ["een stof die je kunt schenken en die de vorm van het vat aanneemt",
       "een stof die je niet kunt zien en die een hele kamer vult",
       "een stof die je kunt ruiken op grote afstand"],
      "Een vaste stof verandert op macroniveau niet uit zichzelf van vorm, omdat de moleculen op hun plek blijven."),
    W("In de vaste fase kunnen de moleculen van hun plek weg bewegen.", False,
      "Niet waar. In de vaste fase trillen de moleculen op hun plek, maar ze kunnen niet van hun plek weg."),
    W("In de vloeibare fase zitten de moleculen nog steeds tegen elkaar aan.", True,
      "Waar. Alleen in de gasfase zitten ze niet meer tegen elkaar aan."),
    W("Moleculen in een gas blijven na een botsing bij elkaar zitten, zoals in een vloeistof.", False,
      "Niet waar. In een gas botsen de moleculen soms, maar ze blijven niet bij elkaar."),
    W("In modeltekeningen van de fasen stel je de moleculen voor als bolletjes.", True,
      "Waar. In figuur 2.3 zijn de moleculen als bolletjes weergegeven."),
    W("Een vloeistof is op microniveau netter geordend dan een vaste stof.", False,
      "Niet waar. Een vloeistof is een rommeliger geheel dan een vaste stof."),
    I("In de ____fase bewegen de moleculen met grote snelheid op grote afstand van elkaar.", "gas",
      "Dat beschrijft de gasfase."),
    I("Als een vaste stof rechtstreeks overgaat in een gas, heet die faseverandering ____.", "sublimeren|sublimatie|sublimeert",
      "Rechtstreeks van vast naar gas heet sublimeren."),
    I("IJs verandert bij 0 °C in vloeibaar water. Deze faseverandering heet ____.", "smelten|smelt",
      "Van vast naar vloeibaar heet smelten."),
    O("Beschrijf wat er op microniveau verschilt tussen water als ijs en water als vloeistof.",
      ["trillen/trilt", "vrij", "langs elkaar/tegen elkaar"], 2,
      "In ijs trillen de moleculen op hun plek; in vloeibaar water kunnen de moleculen vrij langs elkaar bewegen, terwijl ze nog tegen elkaar aan zitten."),
    O("Beschrijf hoe moleculen zich gedragen in een gas en wat er gebeurt als ze elkaar tegenkomen.",
      ["snel/snelheid", "afstand", "botsen/botsing/botsten"], 2,
      "In een gas bewegen de moleculen op grote snelheid en afstand van elkaar. Komen ze elkaar tegen, dan botsen ze, maar ze blijven niet bij elkaar."),
])

# 52 — tekeningen en modellen (beschreven in woorden)
EXAMENS[52] = ("Modeltekeningen lezen en maken", "✏️", [
    M("Een tekening toont enkele bolletjes die ver uit elkaar staan en met grote snelheid bewegen. Welke fase is dat?",
      "de gasfase",
      ["de vaste fase", "de vloeibare fase", "een oplossing"],
      "Bolletjes die ver uit elkaar staan en snel bewegen, horen bij een gas."),
    M("Een tekening toont witte bolletjes (suiker) en blauwe bolletjes (water) gelijkmatig door elkaar. Wat laat deze tekening zien?",
      "een oplossing van suiker in water",
      ["een emulsie van suiker en water", "een zuivere stof met twee soorten bolletjes", "twee lagen die elkaar niet mengen"],
      "Gelijkmatig verdeelde suikermoleculen tussen watermoleculen vormen een oplossing."),
    M("Een tekening toont onderin een laag blauwe bolletjes (water) en erboven een laag andere bolletjes (olijfolie). Wat zie je op macroniveau?",
      "olijfolie die op het water drijft",
      ["een helder mengsel zonder lagen", "een vaste stof in water", "olijfolie die oplost in het water"],
      "Twee lagen moleculen horen bij macro: olijfolie die op het water blijft drijven."),
    M("Je tekent een mengsel van alcohol en water dat goed mengt. Hoe teken je de bolletjes?",
      "bolletjes van twee kleuren gelijkmatig door elkaar",
      ["bolletjes van één kleur gelijkmatig verdeeld over de hele tekening", "twee lagen bolletjes van twee kleuren", "alle bolletjes dicht op elkaar in één hoek"],
      "Bij een goed mengsel (oplossing) staan de verschillende soorten moleculen gelijkmatig door elkaar."),
    M("Je tekent hoe alcohol verdampt uit een alcohol-watermengsel dat verwarmd wordt tot ongeveer 80 °C. Wat teken je?",
      "alcoholbolletjes die ver uit elkaar boven de vloeistof zweven, terwijl de watermoleculen achterblijven",
      ["watermoleculen die ver uit elkaar boven de vloeistof zweven, terwijl de alcoholmoleculen achterblijven",
       "alcohol- en watermoleculen die samen ver uit elkaar boven de vloeistof zweven",
       "alcoholbolletjes die in watermoleculen veranderen en in de vloeistof blijven"],
      "Alcohol verdampt uit het mengsel (gas: ver uit elkaar), het water blijft achter."),
    M("Hoe teken je de moleculen van een zuivere stof?",
      "alle bolletjes hetzelfde",
      ["bolletjes van twee kleuren door elkaar", "bolletjes van drie verschillende soorten", "elk bolletje een andere kleur"],
      "Een zuivere stof bevat één soort moleculen, dus teken je alle bolletjes hetzelfde."),
    M("In een tekening van een mengsel is een deel van de bolletjes rood en een deel groen. Wat betekent dat?",
      "Er zijn twee soorten moleculen in het mengsel aanwezig",
      ["De moleculen zijn warm (rood) of koud (groen)", "De rode moleculen zijn vast en de groene moleculen zijn vloeibaar", "Er is één soort molecuul in twee verschillende fasen"],
      "Verschillende kleuren stellen verschillende soorten moleculen voor."),
    M("Hoe verschillen de tekeningen van de vaste en de vloeibare fase van water?",
      "vast: dicht gestapeld; vloeibaar: nog tegen elkaar, maar rommeliger",
      ["vast: ver uit elkaar; vloeibaar: dicht op elkaar gestapeld en netjes geordend", "vast: rommelig door elkaar; vloeibaar: netjes gestapeld", "vast: in twee lagen; vloeibaar: in één laag"],
      "In de vaste fase staan de bolletjes dicht gestapeld, in de vloeibare fase liggen ze nog tegen elkaar maar rommeliger."),
    M("Waarom gebruik je in deze paragraaf bolletjes om moleculen te tekenen?",
      "Je gebruikt het meest eenvoudige model waarmee je waarnemingen op macroniveau kunt verklaren",
      ["Moleculen zijn in werkelijkheid altijd perfect rond en massief van binnen", "Bolletjes laten alle details van een molecuul zien", "Andere vormen mag je in de scheikunde nooit tekenen"],
      "Een nieuw, ingewikkelder model volgt in de volgende paragraaf; hier is het bolletjesmodel genoeg."),
    M("Je tekent een emulsie van wasbenzine en water die is ontmengd. Wat teken je?",
      "twee lagen: een laag wasbenzinemoleculen die op de laag watermoleculen ligt",
      ["wasbenzine- en watermoleculen gelijkmatig door elkaar verdeeld", "alle bolletjes dezelfde kleur in één laag", "alle bolletjes ver uit elkaar zoals in een gas"],
      "Wasbenzine en water mengen niet goed: de moleculen vormen twee lagen."),
    W("In een tekening van een zuivere stof gebruik je rondjes van verschillende kleuren.", False,
      "Niet waar. Een zuivere stof bevat één soort moleculen, dus alle rondjes hebben dezelfde kleur."),
    W("In een tekening van een gas staan de bolletjes ver uit elkaar.", True,
      "Waar. In de gasfase zitten de moleculen op grote afstand van elkaar."),
    W("In een tekening van een ontmengde emulsie zijn de twee soorten bolletjes gelijkmatig door elkaar verdeeld.", False,
      "Niet waar. In een emulsie die ontmengt, vormen de moleculen twee lagen."),
    W("In een tekening van een vloeistof liggen de bolletjes tegen elkaar aan.", True,
      "Waar. In de vloeibare fase zitten de moleculen tegen elkaar aan."),
    W("Je gebruikt steeds het meest eenvoudige model waarmee je een waarneming kunt verklaren.", True,
      "Waar. Je gebruikt steeds het meest eenvoudige model."),
    I("In de modeltekeningen van deze paragraaf stelt elk bolletje één ____ voor.", "molecuul",
      "In deze modellen is een molecuul een bolletje."),
    I("In een tekening van een gas staan de bolletjes op grote ____ van elkaar.", "afstand",
      "Moleculen in een gas zitten op grote afstand van elkaar."),
    I("Voor verschillende soorten moleculen gebruik je in een tekening rondjes van verschillende ____.", "kleuren|kleur",
      "Verschillende kleuren staan voor verschillende soorten moleculen."),
    O("Beschrijf hoe je met een modeltekening laat zien dat alcohol en water een heldere oplossing vormen.",
      ["kleur/kleuren", "door elkaar/gelijkmatig/verdeeld/gemengd", "bolletjes/rondjes"], 2,
      "Je gebruikt bolletjes van twee kleuren (alcohol en water) en tekent ze gelijkmatig door elkaar verdeeld."),
    O("Beschrijf hoe je de moleculen tekent in een emulsie van wasbenzine en water die ontmengt.",
      ["laag/lagen", "twee", "kleur/kleuren/soorten"], 2,
      "Je tekent twee lagen: een laag met bolletjes van de ene kleur (water) en daarop een laag met bolletjes van de andere kleur (wasbenzine)."),
])

# 53 — rekenen en afleiden
EXAMENS[53] = ("Rekenen en afleiden", "🔢", [
    M("Je tekent een modelvoorstelling van lucht met 50 bolletjes. Lucht bestaat voor ongeveer 20% uit zuurstof en 80% uit stikstof. Hoeveel bolletjes van elke soort teken je?",
      "10 zuurstof en 40 stikstof",
      ["40 zuurstof en 10 stikstof", "25 zuurstof en 25 stikstof", "20 zuurstof en 30 stikstof"],
      "20% van 50 = 10 zuurstofbolletjes en 80% van 50 = 40 stikstofbolletjes."),
    M("Je tekent lucht met 25 bolletjes. Hoeveel daarvan zijn stikstof?",
      "20",
      ["5", "10", "15"],
      "80% van 25 = 20 stikstofbolletjes (de andere 5 zijn zuurstof)."),
    M("Hoe schrijf je één triljoen als een macht van tien?",
      "10<sup>18</sup>",
      ["10<sup>12</sup>", "10<sup>9</sup>", "10<sup>6</sup>"],
      "Een triljoen is een 1 met achttien nullen, dus 10<sup>18</sup>."),
    M("Koolstofdioxide sublimeert bij 194,7 K. In welke fase is het bij 180 K?",
      "vast, want 180 K is lager dan het sublimatiepunt",
      ["gas, want 180 K is lager dan het sublimatiepunt", "vloeibaar, want 180 K ligt dicht bij het sublimatiepunt", "gas, want koolstofdioxide is altijd een gas"],
      "Onder het sublimatiepunt (194,7 K) is koolstofdioxide een vaste stof."),
    M("Koolstofdioxide sublimeert bij 194,7 K. In welke fase is het bij 200 K?",
      "gas, want 200 K is hoger dan het sublimatiepunt",
      ["vast, want 200 K is hoger dan het sublimatiepunt", "vloeibaar, want koolstofdioxide smelt eerst", "vast, want sublimeren is van gas naar vast"],
      "Boven het sublimatiepunt is koolstofdioxide een gas."),
    M("Een suikerkorrel, een suikerklont en een kom suiker worden elk opgelost in een liter water. Welk mengsel bevat de meeste suikermoleculen?",
      "dat met de kom suiker",
      ["dat met de suikerkorrel", "dat met de suikerklont", "alle drie evenveel, want het water is evenveel"],
      "Hoe meer suiker, hoe meer suikermoleculen in dezelfde liter water."),
    M("Cola bevat onder andere water, koolstofdioxide, suiker en fosforzuur. Hoeveel soorten moleculen bevat cola minstens?",
      "vier",
      ["één", "twee", "drie"],
      "Elke stof heeft een eigen soort moleculen; vier stoffen betekent minstens vier soorten moleculen."),
    M("In een tekening van lucht zijn er 20 stikstofbolletjes en 5 zuurstofbolletjes. Hoe klopt de verhouding met de werkelijkheid?",
      "Dat klopt: stikstof is vier keer zo talrijk als zuurstof",
      ["Dat klopt niet: er moeten evenveel stikstof- als zuurstofbolletjes zijn", "Dat klopt niet: zuurstof komt vaker voor dan stikstof", "Dat klopt: zuurstof is vier keer zo talrijk als stikstof"],
      "Lucht is ongeveer 80% stikstof en 20% zuurstof: 4 : 1."),
    M("Wat is de schrijfwijze van twee triljoen?",
      "een 2 met achttien nullen",
      ["een 2 met negen nullen", "een 1 met twee nullen", "een 2 met twee nullen, achter elkaar"],
      "Eén triljoen is een 1 met achttien nullen, twee triljoen een 2 met achttien nullen."),
    M("Een tekening heeft 12 bolletjes: 3 witte en 9 blauwe. Welk deel van de bolletjes is wit?",
      "25%",
      ["33%", "75%", "3%"],
      "3 van de 12 is een kwart: 25%."),
    W("Een triljoen is een 1 met achttien nullen.", True,
      "Waar. Dat is de definitie uit het boek."),
    W("Lucht bestaat voor ongeveer 80% uit zuurstof en 20% uit stikstof.", False,
      "Niet waar. Lucht bestaat voor ongeveer 20% uit zuurstof en 80% uit stikstof."),
    W("In een modeltekening van lucht teken je meer stikstofbolletjes dan zuurstofbolletjes.", True,
      "Waar. Stikstof komt in lucht het meest voor."),
    W("Koolstofdioxide is bij 180 K een gas, want 180 K is lager dan 194,7 K.", False,
      "Niet waar. Onder het sublimatiepunt is koolstofdioxide vast."),
    W("In een tekening met 10 bolletjes lucht teken je 5 bolletjes zuurstof.", False,
      "Niet waar. 20% van 10 is 2 zuurstofbolletjes."),
    I("Lucht bestaat voor ongeveer 80% uit ____. (naam van de stof)", "stikstof",
      "Lucht is ongeveer 80% stikstof en 20% zuurstof."),
    I("In een tekening met 20 bolletjes lucht teken je ____ bolletjes zuurstof. (getal)", "4|vier",
      "20% van 20 = 4."),
    I("Twee triljoen is een 2 met ____ nullen. (schrijf een getal of woord)", "achttien|18",
      "Een triljoen heeft achttien nullen, twee triljoen ook."),
    O("Je moet lucht tekenen met 50 bolletjes. Leg uit hoeveel bolletjes je van elke soort tekent.",
      ["10", "40"], 2,
      "Lucht bestaat voor 20% uit zuurstof: 10 bolletjes, en voor 80% uit stikstof: 40 bolletjes."),
    O("Leg uit waarom het microbeeld van een kom suiker in een liter water er anders uitziet dan dat van één suikerkorrel in een liter water.",
      ["meer/veel/groter", "moleculen/deeltjes", "verhouding/drukker/dichter"], 2,
      "In de kom zitten veel meer suikermoleculen; die zitten dan in dezelfde hoeveelheid water, dus de verhouding verandert en het is drukker."),
])

# 54 — dagelijkse situaties
EXAMENS[54] = ("Toepassen in het dagelijks leven", "🥤", [
    M("Je spuit parfum aan de ene kant van een kamer en na een tijdje ruikt iemand aan de andere kant het ook. Wat verklaart dit op microniveau?",
      "Geurmoleculen bewegen door de kamer tot bij zijn neus",
      ["Het parfum verdampt tot één grote druppel die door de lucht zweeft", "De geur is geen stof en reist daarom vanzelf", "De parfummoleculen blijven op hun plek trillen en de geur komt daarbij"],
      "Geurmoleculen zijn heel klein en kunnen vrij bewegen, zodat ze zich door de kamer verspreiden."),
    M("Je roert suiker door je thee en ziet de suiker niet meer. Wat is er gebeurd?",
      "De suikermoleculen zitten verdeeld tussen de watermoleculen",
      ["De suiker is volledig verdwenen en niet meer in het mengsel aanwezig", "De suiker is veranderd in watermoleculen", "De suikermoleculen zijn opgelost in zichzelf"],
      "De suikermoleculen zijn niet weg, ze zijn gelijkmatig verdeeld tussen de watermoleculen: een oplossing."),
    M("Wasbenzine en water zijn gemengd, maar je ziet twee lagen. Wat is de reden?",
      "De moleculen van beide stoffen mengen niet goed",
      ["Wasbenzine bestaat uit grotere bolletjes dan water", "Water is een gas en wasbenzine een vloeistof", "De moleculen van beide stoffen zijn exact hetzelfde"],
      "Wasbenzine en water mengen niet goed: de moleculen vormen twee lagen en je kunt beide stoffen zien."),
    M("Waarom is cola een mengsel?",
      "Het bevat verschillende soorten moleculen, zoals water, suiker en fosforzuur",
      ["Het bevat uitsluitend colamoleculen, namelijk één enkele soort deeltje, net als een zuivere stof", "Het is een vloeistof en vloeistoffen zijn altijd mengsels", "Het bevat bubbels, en bubbels zijn een andere stof"],
      "Cola bevat meerdere stoffen en dus verschillende soorten moleculen."),
    M("Waarom mag je niet spreken van colamoleculen?",
      "Cola bevat meer stoffen en dus verschillende soorten moleculen, niet één soort",
      ["Omdat cola alleen uit losse atomen bestaat en helemaal niet uit moleculen zoals andere stoffen", "Omdat cola een vaste stof is", "Omdat cola geen eigenschappen heeft"],
      "Cola is een mengsel; alleen de afzonderlijke stoffen hebben eigen moleculen."),
    M("Je fönt een hond met een blauwe vacht en de blauwe kleur verdwijnt. Wat gebeurt er op macroniveau?",
      "Het water verdampt en het blauwe kopersulfaat wordt weer wit",
      ["Het kopersulfaat verdampt uit de vacht en alleen het water blijft over", "Het water wordt blauw door de hete lucht", "De kleur zakt in de vacht en wordt onzichtbaar"],
      "Wit kopersulfaat wordt blauw met water; als het water verdampt, verdwijnt de blauwe kleur."),
    M("Waarom gebruikt een weerman modellen?",
      "Het weer is te groot om als geheel te zien; met modellen voorspelt hij het",
      ["Het weer bestaat uit moleculen die allemaal te klein zijn om te zien", "Een weerman heeft geen eigen waarnemingen en moet dus altijd modellen gebruiken", "Modellen zijn exact gelijk aan het weer, daarom werken ze zo goed"],
      "Modellen gebruik je ook voor dingen die te groot zijn om te zien, zoals het weer."),
    M("Een leerling zegt: 'Ik zie de moleculen van suiker door een goede loep.' Wat klopt er niet?",
      "Moleculen zijn te klein om met een loep te zien; je ziet een stof pas met triljoenen moleculen",
      ["Suiker bestaat niet uit moleculen, daarom zie je niets", "Moleculen zijn alleen in de gasfase te zien, niet in vaste stoffen", "Een loep maakt moleculen juist onzichtbaar omdat het licht ze afbuigt"],
      "Een enkel molecuul is niet te zien; zelfs één suikerkorrel bevat triljoenen moleculen."),
    M("Waarom lijkt een helder mengsel van alcohol en water op zuiver water?",
      "De moleculen zijn gelijkmatig verdeeld, dus er zijn geen aparte lagen te zien",
      ["Alcoholmoleculen zijn onzichtbaar maar watermoleculen zijn dat niet", "De alcohol is helemaal verdwenen en alleen het water is nog over", "Alcohol en water zijn eigenlijk dezelfde stof met verschillende namen"],
      "Alcohol en water mengen goed; je krijgt een heldere oplossing."),
    M("Je meet dat een vloeistof kookt bij één bepaalde temperatuur (kookpunt). Wat past hierbij?",
      "een zuivere stof, die op microniveau één soort moleculen bevat",
      ["een mengsel, dat op microniveau toch maar één soort moleculen bevat", "een mengsel, dat op microniveau verschillende soorten bevat", "een zuivere stof, die op microniveau meerdere soorten bevat"],
      "Zuivere stoffen hebben een kookpunt; mengsels een kooktraject."),
    W("Je ruikt een geurstokje op afstand omdat geurmoleculen door de kamer bewegen.", True,
      "Waar. De geurmoleculen verplaatsen zich door de kamer."),
    W("Een glas cola bevat alleen watermoleculen en suikermoleculen.", False,
      "Niet waar. Cola bevat ook onder andere koolstofdioxide en fosforzuur."),
    W("Bij een ontmengde emulsie van olijfolie en water kun je beide stoffen nog zien.", True,
      "Waar. De stoffen vormen twee lagen en zijn dus nog zichtbaar."),
    W("Een weerman gebruikt modellen om het weer te voorspellen.", True,
      "Waar. Modellen gebruik je ook voor dingen die te groot zijn om te zien."),
    W("Als je een blauwe hond fönt, wordt de vacht juist nog blauwer.", False,
      "Niet waar. De blauwe kleur verdwijnt als het water verdampt."),
    I("Cola is een mengsel van onder andere water, koolstofdioxide, suiker en ____.", "fosforzuur",
      "Dat staat in het boek."),
    I("Een weerman gebruikt ____ om het weer te voorspellen.", "modellen|model",
      "Een model is een versimpelde weergave van de werkelijkheid."),
    I("Het witte kopersulfaat kleurt blauw door contact met ____.", "water",
      "Wit kopersulfaat wordt blauw kopersulfaatpentahydraat als het met water in contact komt."),
    O("Leg uit waarom cola op microniveau een mengsel is en geen zuivere stof.",
      ["verschillende/meerdere", "soorten", "moleculen"], 2,
      "Cola bevat verschillende soorten moleculen (water, suiker, fosforzuur), een zuivere stof heeft maar één soort."),
    O("Leg uit waarom het fönnen van een blauwe hond de blauwe kleur laat verdwijnen.",
      ["water", "verdampen/verdampt/droog/weg", "wit"], 2,
      "Het water in de vacht verdampt, waardoor het blauwe kopersulfaat weer wit wordt."),
])

# 55 — opdrachten uit het boek
EXAMENS[55] = ("Opgaven en experimenten uit het boek", "📘", [
    M("Opgave 2: 'Water- en ethermoleculen mengen slecht.' en 'Er ontstaat een tweelagensysteem.' Welke zin hoort bij welk niveau?",
      "zin 1 microniveau (moleculen), zin 2 macroniveau (je ziet het)",
      ["zin 1 macroniveau (je ziet het), zin 2 microniveau (moleculen)", "beide zinnen macroniveau", "beide zinnen microniveau"],
      "De eerste zin gaat over moleculen (micro), de tweede over wat je ziet (macro)."),
    M("Zout mengt goed met water, zand slecht. Welk niveau beschrijft dit?",
      "macroniveau, je neemt het waar",
      ["microniveau, want het gaat om deeltjes", "beide niveaus tegelijk", "geen enkel niveau, want zand en zout zijn vast"],
      "Dat je het kunt waarnemen, maakt het een eigenschap op macroniveau."),
    M("'Honden met een blauwe vacht lopen op straat.' Op welk niveau is deze beschrijving?",
      "macroniveau, want je ziet de blauwe vacht",
      ["microniveau, want de verf zit op moleculen", "microniveau, want het gaat om een stof", "geen van beide niveaus"],
      "Je kunt de kleur zien, dus macroniveau."),
    M("Een alcohol-watermengsel wordt verwarmd tot ongeveer 80 °C. Wat blijft er achter?",
      "water",
      ["alcohol", "evenveel alcohol als water", "geen van beide"],
      "Alcohol verdampt, het water blijft achter."),
    M("Waar gebruik je in de scheikunde een model voor?",
      "voor dingen die te klein of te groot zijn om te zien",
      ["alleen voor dingen die je met je zintuigen kunt zien", "alleen voor stoffen in de vaste fase", "om de werkelijkheid exact na te maken"],
      "Je gebruikt modellen voor te kleine dingen (moleculen) en soms te grote (zonnestelsel, weer)."),
    M("Wat is een nadeel van een model?",
      "Het is een versimpelde weergave en dus niet de hele werkelijkheid",
      ["Je kunt er geen enkele waarneming op microniveau mee verklaren", "Het kan alleen voor stoffen in de gasfase gebruikt worden", "Je moet het bij elke stof opnieuw verzinnen"],
      "Een model is een versimpelde weergave van de werkelijkheid."),
    M("Wat onderzoek je in experiment 'Daar zit een luchtje aan'?",
      "hoe een geur zich door een lokaal verspreidt",
      ["hoe stoffen onder hoge druk van vorm veranderen", "welke drie stoffen je herkent", "hoe snel een gas koud wordt"],
      "Het experiment onderzoekt hoe een geur zich door een lokaal verspreidt."),
    M("Wat probeer je in 'Kalk, gips, soda of …'?",
      "drie stoffen te herkennen",
      ["geuren te verspreiden", "stoffen onder hoge druk te zetten", "moleculen te tellen"],
      "In dit experiment probeer je drie stoffen te herkennen."),
    M("Wat laat de demonstratie 'Stoffen onder druk' zien?",
      "wat er gebeurt als je stoffen onder hoge druk zet",
      ["hoe een stof zich in een lokaal door lucht verspreidt", "welke stof een kookpunt heeft", "wat een oplossing is"],
      "De demonstratie laat zien wat er met stoffen onder hoge druk gebeurt."),
    M("Een kleine hoeveelheid zuurstofgas mengt met water. Wat teken je?",
      "weinig zuurstofbolletjes verspreid tussen veel watermoleculen",
      ["veel zuurstofbolletjes tussen maar weinig watermoleculen", "twee even grote lagen zuurstof en water", "alleen watermoleculen, want zuurstof lost nooit op"],
      "Een kleine hoeveelheid zuurstof betekent weinig zuurstofmoleculen tussen het water."),
    W("Zand en zout verschillen op macroniveau in hoe goed ze mengen met water.", True,
      "Waar. Zout mengt goed met water, zand slecht."),
    W("'Honden met een blauwe vacht' is een beschrijving op microniveau.", False,
      "Niet waar. Dat is wat je ziet: macroniveau."),
    W("Als alcohol uit een alcohol-watermengsel verdampt, blijft het water achter.", True,
      "Waar. Alcohol verdampt bij ongeveer 80 °C."),
    W("Een voordeel van modellen is dat ze de werkelijkheid exact weergeven.", False,
      "Niet waar. Een model is een versimpelde weergave."),
    W("Je gebruikt modellen ook voor dingen die te groot zijn om te zien, zoals het zonnestelsel.", True,
      "Waar. Een model gebruik je voor dingen die te klein zijn om te zien, maar soms ook voor dingen die te groot zijn."),
    I("Als water en ether slecht mengen, ontstaat een ____-lagensysteem.", "twee",
      "Er ontstaan twee lagen."),
    I("In 'Kalk, gips, soda of …' probeer je ____ stoffen te herkennen. (getal)", "3|drie",
      "Het gaat om drie stoffen."),
    I("Een model is een ____ weergave van de werkelijkheid.", "versimpelde|vereenvoudigde|eenvoudige",
      "Een model is een versimpelde weergave."),
    O("Noem één voordeel en één nadeel van het gebruik van modellen.",
      ["voorstellen/verklaren/uitleggen/voorspellen", "versimpeld/vereenvoudigd/niet exact/niet precies"], 2,
      "Voordeel: je kunt je iets voorstellen bij moleculen en waarnemingen verklaren. Nadeel: een model is versimpeld, dus niet exact."),
    O("Leg uit waarom de zin 'Bij het samenvoegen van water en ether ontstaat een tweelagensysteem' een beschrijving op macroniveau is.",
      ["zintuigen/zintuig", "waarnemen/waarneembaar/zien/ogen", "moleculen/deeltjes"], 2,
      "Je kunt het tweelagensysteem met je zintuigen waarnemen (zien); de zin gaat niet over losse moleculen."),
])

# 56 — eindniveau
EXAMENS[56] = ("Eindniveau — redeneren", "🎯", [
    M("Lucht bestaat uit zuurstof en stikstof. Wat volgt hieruit?",
      "Lucht is een mengsel van twee soorten moleculen",
      ["Lucht is een zuivere stof, want het is één gas", "Lucht heeft slechts één soort molecuul, omdat het een gas is", "Lucht heeft geen moleculen omdat je het niet kunt zien"],
      "Een mengsel bevat verschillende soorten moleculen."),
    M("Een vloeistof is helder. Kun je alleen daaruit zeggen of het een zuivere stof of een mengsel is?",
      "Nee, ook een oplossing is helder; je moet bijvoorbeeld het kookpunt meten",
      ["Ja, een helder uiterlijk betekent altijd een zuivere stof", "Ja, helder betekent altijd een mengsel van meerdere stoffen", "Nee, want een zuivere stof bestaat in de praktijk niet"],
      "Een oplossing van suiker in water lijkt op zuiver water."),
    M("Welke uitspraak is juist?",
      "Verschillende stoffen bestaan uit verschillende soorten moleculen",
      ["Alle stoffen bestaan uit precies dezelfde soort moleculen", "Alle moleculen van een mengsel zijn precies aan elkaar gelijk", "Moleculen van verschillende stoffen verschillen alleen in hun kleur en grootte"],
      "Dat staat in de samenvatting."),
    M("Een leerling tekent een gas met bolletjes dicht op elkaar. Wat is daar fout aan?",
      "In een gas zitten de moleculen op grote afstand van elkaar",
      ["In een gas bestaan geen moleculen, alleen losse stof", "In een gas staan moleculen stil en raken ze elkaar nooit", "In een gas zitten de moleculen allemaal op hun eigen plek vast"],
      "Moleculen in een gas bewegen snel en op grote afstand van elkaar."),
    M("Waarom blijft het bolletjesmodel voor deze paragraaf voldoende?",
      "Het is het eenvoudigste model waarmee je de waarnemingen kunt verklaren",
      ["Het is het enige model dat in de scheikunde bestaat", "Het toont alle details van een molecuul, ook de atomen erin", "Een ingewikkelder model werkt voor moleculen niet goed"],
      "Je gebruikt steeds het meest eenvoudige model."),
    M("Waarom hoort een emulsie niet bij de oplossingen?",
      "De moleculen verspreiden zich niet gelijkmatig maar vormen twee lagen",
      ["Een emulsie bestaat uit slechts één soort moleculen", "Een emulsie bevat geen vloeistoffen maar alleen vaste stoffen", "Een emulsie is altijd een vaste stof"],
      "Bij een oplossing zijn de moleculen gelijkmatig verdeeld."),
    M("Een suikeroplossing bestaat uit suiker en water. Hoeveel soorten moleculen bevat deze minimaal?",
      "twee",
      ["één", "drie", "vier"],
      "Suikermoleculen en watermoleculen."),
    M("Een stof heeft een smelttraject. Wat weet je dan?",
      "Het is een mengsel met verschillende soorten moleculen",
      ["Het is een zuivere stof, want die bevat één soort moleculen", "Het is een gas", "Het is een niet-ontleedbare stof"],
      "Mengsels hebben een smelttraject."),
    M("Wat kun je volgens het boek met de huidige modellen behalve waarnemingen verklaren?",
      "macro-eigenschappen van nieuwe stoffen voorspellen",
      ["moleculen met een microscoop zichtbaar maken", "de werkelijkheid in alle details exact namaken", "alle onbekende stoffen met zekerheid herkennen"],
      "Modellen kunnen eigenschappen van nieuwe stoffen voorspellen."),
    M("Je verwarmt een alcohol-watermengsel tot ongeveer 80 °C. Wat zie je op macroniveau?",
      "De alcohol verdampt en het water blijft achter",
      ["Het water verdampt en de alcohol blijft achter", "Beide stoffen verdampen even snel", "Er verandert niets"],
      "Alcohol verdampt uit het mengsel."),
    W("Een oplossing en een emulsie zien er op macroniveau allebei helder uit.", False,
      "Niet waar. Een oplossing is helder, een emulsie vormt twee lagen."),
    W("Een mengsel van drie vloeistoffen bestaat niet uit één soort moleculen.", True,
      "Waar. Meerdere stoffen betekent meerdere soorten moleculen."),
    W("Een macro-eigenschap als het smeltpunt kun je op microniveau verklaren met een model.", True,
      "Waar. Dat is het doel van modellen."),
    W("Alle moleculen in een mengsel zijn hetzelfde.", False,
      "Niet waar. Een mengsel bevat verschillende soorten."),
    W("Een tekening van een zuivere vloeistof heeft bolletjes van twee kleuren.", False,
      "Niet waar. Eén kleur."),
    I("Een zuivere stof heeft een vast ____punt en een kookpunt.", "smelt",
      "Zuivere stoffen hebben een smeltpunt en een kookpunt."),
    I("Een mengsel heeft geen kookpunt maar een ____.", "kooktraject",
      "Mengsels hebben een kooktraject."),
    I("Een stof die uit één soort moleculen bestaat, is een ____ stof.", "zuivere",
      "Zuivere stoffen bevatten één soort moleculen."),
    O("Een leerling zegt: 'Een helder mengsel kan geen mengsel zijn van twee stoffen.' Leg uit waarom dat niet klopt.",
      ["oplossing", "moleculen", "verdeeld/gelijkmatig"], 2,
      "Een oplossing is helder, maar het is wel een mengsel: de moleculen van beide stoffen zijn gelijkmatig verdeeld."),
    O("Geef een voorbeeld van twee stoffen die slecht mengen en leg uit hoe de moleculen dan op microniveau zitten.",
      ["olijfolie/wasbenzine/ether", "laag/lagen", "niet/verspreiden"], 2,
      "Olijfolie en water mengen slecht: de moleculen verspreiden zich niet door elkaar maar vormen twee lagen."),
])


def norm(t):
    return re.sub(r'[^a-z0-9]+', ' ', re.sub(r'<[^>]+>', '', t.lower())).strip()


def check(nr, vr, bestaand):
    typen = [v["type"] for v in vr]
    assert (typen.count("mc"), typen.count("waaronwaar"), typen.count("invul"), typen.count("open")) == (10, 5, 3, 2), nr
    assert sum(1 for v in vr if v["type"] == "waaronwaar" and not v["antwoord"]) >= 2, nr
    for v in vr:
        t = norm(v["vraag"])
        assert t not in bestaand, (nr, "dubbel", v["vraag"])
        bestaand.add(t)
        if v["type"] == "mc":
            kort = len(max(v["opties"], key=len))
            assert len(v["opties"]) == 4
            assert not any(len(o) > 4 and norm(o) == t for o in v["opties"])
        if v["type"] == "waaronwaar":
            assert v["uitleg"].startswith(("Waar.", "Niet waar.")), v["vraag"]
        if v["type"] == "invul":
            assert "____" in v["vraag"], v["vraag"]
            for a in v["antwoord"].split("|"):
                assert a.lower() not in v["vraag"].lower().replace("____", ""), (nr, a, v["vraag"])
        if v["type"] == "open":
            groepen = v["sleutelwoorden"]
            assert 1 <= v["minTreffers"] <= len(groepen)
            vl, ml = v["vraag"].lower(), v["modelantwoord"].lower()
            for g in groepen:
                alts = g.split("/")
                assert not any(a in vl for a in alts), (nr, g, v["vraag"])
            treffers = sum(any(a in ml for a in g.split("/")) for g in groepen)
            assert treffers >= v["minTreffers"], (nr, "model", v["vraag"])


def bestaande_vragen():
    """Alle vraagteksten uit de bestaande H2-bestanden (niet 50-56)."""
    s = set()
    for f in os.listdir(ROOT):
        m = re.match(r'(examen_h2_(\d+)|h2_\d+|examen_\d+)\.js$', f)
        if not m or (m.group(2) and 50 <= int(m.group(2)) <= 61):
            continue
        txt = open(os.path.join(ROOT, f), encoding='utf-8').read()
        for q in re.findall(r'"vraag":\s*"((?:[^"\\]|\\.)*)"', txt):
            s.add(norm(json.loads('"' + q + '"')))
    return s


def main():
    rng = random.Random('gen_scheikunde_h2_1_extra.py')
    bestaand = bestaande_vragen()
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        check(nr, vr, bestaand)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_h2_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {"id": f"ex-h3-sch-h2-{nr}", "hoofdstuk": 2, "paragraaf": "2.1",
              "titel": f"Toets {nr} — §2.1 {sub}", "vak": "Scheikunde · HAVO 3 (H2 — §2.1)",
              "icoon": icoon, "duurMin": 30, "vragen": vr}
        kop = (f"/* =========================================================\n"
               f"   Duru's Scheikunde (HAVO 3) — Toets {nr} — §2.1 {sub}\n"
               f"   Hoofdstuk 2 (Chemie Overal), §2.1 Macro en micro. 20 vragen · 30 minuten. Alleen wat in het boek staat.\n"
               f"   Gegenereerd door tools/gen_scheikunde_h2_1_extra.py\n"
               f"   ========================================================= */\n")
        schrijf(os.path.join(ROOT, f'examen_h2_{nr}.js'), kop,
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_h2_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
