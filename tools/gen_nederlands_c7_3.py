#!/usr/bin/env python3
"""Nederlands HAVO 3 · Cursus 7 Spelling §3 'Met of zonder n?' (boek p. 246–247).

Schrijft havo3/nederlands/js/data/c7_3.js (onderwerp) en examen_30…36.js (ex-h3-nederlands-30…36).
Vuistregel van het boek: een telwoord/bijv. nw. is zelfstandig gebruikt als je er GEEN zelfstandig
naamwoord uit de zin (of de zin ervoor) achter kunt invullen. Daarom staan zinnen met een n-vorm
voor personen nergens naast een persoonsnaamwoord in het meervoud dat je erachter zou kunnen invullen.

Draai: python3 tools/gen_nederlands_c7_3.py   (daarna node tools/gate.js nederlands --only=h7)
"""
import json, os, random, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "havo3", "nederlands", "js", "data")
rng = random.Random("c7_3")

# ---- regels (uitleg + redenen-opties) ------------------------------------------------------------
U = {
    "P": "Het telwoord is zelfstandig gebruikt (je kunt er geen zelfstandig naamwoord uit de zin achter invullen) en verwijst naar personen, dus met n.",
    "Z": "Het telwoord is zelfstandig gebruikt, maar verwijst naar dingen of dieren, dus zonder n.",
    "B": "Het woord is niet-zelfstandig (bijvoeglijk) gebruikt: er staat een zelfstandig naamwoord achter, dus zonder n.",
    "T": "Tientallen, honderden, (tien)duizenden en miljoenen schrijf je altijd met n, ook als het om dingen of dieren gaat.",
    "AP": "Een zelfstandig gebruikt bijvoeglijk naamwoord dat naar meer personen verwijst, krijgt in het meervoud een n.",
    "AE": "Het zelfstandig gebruikte bijvoeglijk naamwoord verwijst naar één persoon (enkelvoud): het eindigt op -e, zonder n.",
    "AZ": "Een zelfstandig gebruikt bijvoeglijk naamwoord dat naar zaken (dingen) verwijst, eindigt op -e en krijgt geen n.",
    "ST": "Een stoffelijk bijvoeglijk naamwoord (gouden, zilveren, houten, wollen) eindigt al op -en; er komt geen extra e of n bij.",
}
REDEN = {
    "P": "Het telwoord wordt zelfstandig gebruikt en verwijst naar personen.",
    "Z": "Het woord wordt zelfstandig gebruikt, maar verwijst naar dingen of dieren.",
    "B": "Het woord staat bijvoeglijk: er volgt een zelfstandig naamwoord.",
    "T": "Woorden als tientallen en honderden krijgen altijd een n.",
    "AP": "Het is een zelfstandig gebruikt bijvoeglijk naamwoord voor meer personen.",
    "AE": "Het zelfstandig gebruikte bijvoeglijk naamwoord slaat op één persoon.",
    "AZ": "Het zelfstandig gebruikte bijvoeglijk naamwoord verwijst naar zaken.",
    "ST": "Het is een stoffelijk bijvoeglijk naamwoord dat al op -en eindigt.",
}


def mc(vraag, goed, fout, uitleg):
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": list(fout), "uitleg": uitleg}


def G(zin, a, b, uitleg):
    """Twee open plekken; a en b = (juiste vorm, foute vorm). Opties = alle 4 combinaties."""
    combos = [f"{x} – {y}" for x in a for y in b]
    goed = f"{a[0]} – {b[0]}"
    return mc(f"Kies de juiste combinatie: <i>{zin}</i>", goed, [c for c in combos if c != goed], uitleg)


def E(zin, goed, fout, code, extra=""):
    return mc(f"Kies de juiste vorm: <i>{zin}</i>", goed, [fout], (U[code] + " " + extra).strip())


def R(vraag, code, extra=""):
    andere = rng.sample([k for k in REDEN if k != code and REDEN[k] != REDEN[code]], 3)
    return mc(vraag, REDEN[code], [REDEN[k] for k in andere], (U[code] + " " + extra).strip())


def W(stelling, waar, uitleg):
    return {"type": "waaronwaar", "vraag": stelling, "antwoord": waar,
            "uitleg": ("Waar. " if waar else "Niet waar. ") + uitleg}


def O(vraag, sleutels, model, uitleg, minT=1):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": minT,
            "modelantwoord": model, "uitleg": uitleg}


# ---- toetsen ---------------------------------------------------------------------------------------
TOETSEN = []

# 30 · Telwoorden
TOETSEN.append(("Telwoorden: zelfstandig of niet?", "🔢", [
    G("___ denken dat een spin een insect is, maar ___ spinnen hebben acht poten.", ("Velen", "Vele"), ("alle", "allen"),
      "Velen: zelfstandig gebruikt en het gaat om mensen → met n. Alle spinnen: er volgt een zelfstandig naamwoord (bijvoeglijk) → zonder n."),
    G("Ik kocht tien strips op de rommelmarkt; ___ waren gescheurd, maar ___ zagen er nog prima uit.", ("sommige", "sommigen"), ("de meeste", "de meesten"),
      "Beide telwoorden verwijzen naar strips (dingen). Je kunt 'strips' erachter invullen, dus allebei zonder n."),
    G("Toen de brandweer arriveerde, waren ___ al naar buiten gevlucht, maar ___ lagen nog te slapen.", ("de meesten", "de meeste"), ("enkelen", "enkele"),
      "De meesten en enkelen zijn zelfstandig gebruikt en verwijzen naar personen (er staat geen zelfstandig naamwoord in de zin dat je kunt invullen) → allebei met n."),
    G("Bij de verkiezingen stemden ___ voor het eerst, en ___ jonge kiezers twijfelden tot het laatste moment.", ("velen", "vele"), ("vele", "velen"),
      "Velen (eerste plek): zelfstandig, personen → met n. Vele jonge kiezers: er volgt een zelfstandig naamwoord → bijvoeglijk, zonder n."),
    G("De boer heeft twintig kippen. ___ leggen elke dag een ei, maar ___ zijn al te oud.", ("De meeste", "De meesten"), ("enkele", "enkelen"),
      "Het gaat om kippen (dieren), en 'kippen' kun je erachter invullen. Dus allebei zonder n."),
    G("Bij de marathon liepen ___ mee, maar slechts ___ lopers haalden de finish binnen drie uur.", ("duizenden", "duizende"), ("enkele", "enkelen"),
      "Duizenden heeft altijd een n. Enkele lopers: er volgt een zelfstandig naamwoord → zonder n."),
    G("Op de camping hadden ___ tenten een lekkend dak, dus ___ sliepen die nacht in de kantine.", ("enkele", "enkelen"), ("velen", "vele"),
      "Enkele tenten: bijvoeglijk gebruikt → zonder n. Velen: zelfstandig, het gaat om mensen (niet om tenten) → met n."),
    G("Sanne en Daan hebben ___ een bijbaan, maar ___ banen zijn slecht betaald.", ("beiden", "beide"), ("beide", "beiden"),
      "Beiden = Sanne en Daan, twee personen, zelfstandig gebruikt → met n. Beide banen: er volgt een zelfstandig naamwoord → zonder n."),
    E("In de bibliotheek staan ___ boeken over de Tweede Wereldoorlog.", "honderden", "honderde", "T"),
    E("Van de bloemen in de vaas zijn ___ al verwelkt.", "enkele", "enkelen", "Z", "Het gaat om bloemen."),
    E("Na de voorstelling bleven ___ nog lang in de zaal napraten.", "velen", "vele", "P", "Velen = veel mensen."),
    E("Onze hond kreeg vier puppy's en ___ hebben een zwarte vlek op hun neus.", "sommige", "sommigen", "Z", "Het gaat om puppy's (dieren)."),
    R("Waarom schrijf je <b>sommige</b> zonder n in: <i>Ik heb veel planten op mijn kamer, maar sommige gaan bijna dood.</i>?", "Z", "Het gaat om planten."),
    R("Waarom schrijf je <b>tientallen</b> met een n in: <i>Op het plein lagen tientallen ballonnen.</i>?", "T"),
    W("Telwoorden als enkele, vele, weinige en sommige kunnen zowel zelfstandig als niet-zelfstandig gebruikt worden.", True,
      "Ze kunnen vóór een zelfstandig naamwoord staan (enkele boeken) of zelfstandig (enkelen kwamen te laat)."),
    W("Een telwoord is zelfstandig gebruikt als er een zelfstandig naamwoord direct achter staat.", False,
      "Dan is het juist niet-zelfstandig (bijvoeglijk) gebruikt. Zelfstandig betekent: je kunt er geen zelfstandig naamwoord achter invullen."),
    W("In de zin 'Weinigen weten dat een giraf maar zeven halswervels heeft' is weinigen juist gespeld.", True,
      "Weinigen is zelfstandig gebruikt en verwijst naar mensen, dus met n."),
    W("In de zin 'Alle bezoekers moeten hun jas ophangen' moet je allen schrijven.", False,
      "Er volgt een zelfstandig naamwoord (bezoekers), dus is 'alle' bijvoeglijk gebruikt: zonder n."),
    O("Leg uit waarom <i>enkelen</i> met een n wordt geschreven in: <i>Tijdens het examen waren enkelen erg zenuwachtig.</i>",
      ["personen/mensen/leerlingen", "zelfstandig/geen zelfstandig naamwoord/niets achter/invullen"],
      "Enkelen wordt zelfstandig gebruikt (er staat geen zelfstandig naamwoord achter dat je uit de zin kunt invullen) en het verwijst naar personen. Dan schrijf je het met n.",
      U["P"]),
    O("Leg uit waarom je <i>de meeste</i> zonder n schrijft in: <i>Ik heb veel spelletjes, maar de meeste speel ik nooit.</i>",
      ["geen personen/dingen/zaken/voorwerpen", "invullen/aanvullen/erbij denken/zelfstandig naamwoord"],
      "Het gaat niet om personen maar om dingen: je kunt 'spelletjes' erachter invullen. Daarom schrijf je de meeste zonder n.",
      U["Z"]),
]))

# 31 · Bijvoeglijke naamwoorden: personen of zaken
TOETSEN.append(("Bijvoeglijke naamwoorden: personen of zaken?", "👥", [
    G("In de bus sta je op voor ___ en ___.", ("ouderen", "oudere"), ("zwangeren", "zwangere"),
      "Ouderen en zwangeren zijn zelfstandig gebruikte bijvoeglijke naamwoorden voor meer personen → in het meervoud met n."),
    G("Van alle jurken in de winkel vond ik de ___ het mooist, maar de ___ was te duur.", ("rode", "roden"), ("blauwe", "blauwen"),
      "De rode en de blauwe verwijzen naar jurken (zaken) → op -e, zonder n."),
    G("De ___ kreeg een beker en de ___ mochten het volgend jaar opnieuw proberen.", ("snelste", "snelsten"), ("langzaamsten", "langzaamste"),
      "De snelste = één persoon (kreeg) → -e. De langzaamsten = meer personen (mochten) → meervoud met n."),
    G("Mijn moeder koopt dure schoenen, maar ik draag liever ___; de ___ vind ik het mooist.", ("goedkope", "goedkopen"), ("zwarte", "zwarten"),
      "Goedkope en zwarte verwijzen naar schoenen (zaken) → op -e, zonder n."),
    G("De ___ in het ziekenhuis kregen op zondag bezoek van ___ uit het dorp.", ("zieken", "zieke"), ("bekenden", "bekende"),
      "Zieken en bekenden zijn zelfstandig gebruikte bijvoeglijke naamwoorden voor meer personen → met n."),
    G("Ik heb een oude en een nieuwe fiets. De ___ gebruik ik voor school, de ___ voor uitstapjes.", ("oude", "ouden"), ("nieuwe", "nieuwen"),
      "Het gaat om fietsen (zaken) → op -e, zonder n."),
    G("De ___ van de klas wist het antwoord meteen, de ___ hadden meer tijd nodig.", ("slimste", "slimsten"), ("anderen", "andere"),
      "De slimste = één persoon (wist) → -e. De anderen = de andere personen, zelfstandig gebruikt → met n."),
    G("Het museum heeft veel schilderijen: de ___ hangen beneden, de ___ op zolder.", ("moderne", "modernen"), ("oudste", "oudsten"),
      "Moderne en oudste verwijzen naar schilderijen (zaken) → zonder n."),
    E("De ___ van de klas mag als eerste een spreekbeurtonderwerp kiezen.", "jongste", "jongsten", "AE", "Mag = enkelvoud, één persoon."),
    E("In de hongerwinter hadden de ___ het het zwaarst.", "armen", "arme", "AP"),
    E("Van alle taarten op tafel vind ik de ___ het lekkerst.", "zoetste", "zoetsten", "AZ", "Het gaat om een taart."),
    E("Als ___ heb je op school recht op een gebarentolk.", "dove", "doven", "AE", "'Als dove' slaat op één persoon (je)."),
    R("Waarom staat <b>blinden</b> met een n in: <i>Voor blinden zijn er boeken in braille.</i>?", "AP"),
    R("Waarom eindigt <b>gele</b> zonder n in: <i>Van alle tulpen vind ik de gele het mooist.</i>?", "AZ"),
    W("Zelfstandig gebruikte bijvoeglijke naamwoorden die personen aanduiden, eindigen in het enkelvoud op -e.", True,
      "Bijvoorbeeld: de oudere, een zieke. In het meervoud komt er een n bij: de ouderen, de zieken."),
    W("In de zin 'De rijken in dit land betalen meer belasting' is rijken juist gespeld.", True,
      "Rijken verwijst naar meer personen, dus meervoud met n."),
    W("Een zelfstandig gebruikt bijvoeglijk naamwoord dat naar dingen verwijst, krijgt in het meervoud een n, zoals in 'Ik koop de goedkopen'.", False,
      "Bij zaken eindigt het op -e zonder n: Ik koop de goedkope."),
    W("In 'De oudste van het gezin mag voorin zitten' moet je oudsten schrijven.", False,
      "Het gaat om één persoon (mag), dus enkelvoud: de oudste, zonder n."),
    O("Leg uit wat het verschil in betekenis is tussen <i>de jongere</i> en <i>de jongeren</i>.",
      ["één/enkelvoud/1 persoon", "meer/meervoud/meerdere/groep"],
      "De jongere is één jonge persoon (enkelvoud); de jongeren zijn meerdere jonge personen (meervoud, met n).",
      "Zelfstandig gebruikte bijvoeglijke naamwoorden voor personen eindigen in het enkelvoud op -e en krijgen in het meervoud een n."),
    O("Leg uit waarom <i>goedkope</i> zonder n wordt geschreven in: <i>Van de twee laptops koop ik de goedkope.</i>",
      ["dingen/zaken/geen personen/voorwerpen/apparaat"],
      "Goedkope verwijst naar een laptop, een ding en geen persoon. Bij zaken eindigt het zelfstandig gebruikte bijvoeglijk naamwoord op -e, zonder n.",
      U["AZ"]),
]))

# 32 · Stoffelijke bijvoeglijke naamwoorden + tientallen/honderden
TOETSEN.append(("Stoffelijke bijvoeglijke naamwoorden en tientallen", "🥇", [
    G("Mijn oma bewaart haar ringen in een kistje: de ___ draagt ze elke dag, de ___ alleen op feestdagen.", ("zilveren", "zilverene"), ("gouden", "goudene"),
      "Zilveren en gouden zijn stoffelijke bijvoeglijke naamwoorden die al op -en eindigen: er komt geen e of n bij."),
    G("Er kwamen ___ kijken naar de optocht, en ___ hadden zich verkleed.", ("tienduizenden", "tienduizende"), ("velen", "vele"),
      "Tienduizenden heeft altijd een n. Velen = veel mensen, zelfstandig gebruikt → met n."),
    G("Mijn moeder heeft twee soorten borden: de ___ gebruikt ze dagelijks, de ___ alleen met kerst.", ("stenen", "stenene"), ("porseleinen", "porseleinene"),
      "Stenen en porseleinen zijn stoffelijke bijvoeglijke naamwoorden (materiaal) die al op -en eindigen."),
    G("In de sloot zwommen ___ kikkervisjes, en ___ hadden al pootjes.", ("honderden", "honderde"), ("sommige", "sommigen"),
      "Honderden: altijd met n. Sommige verwijst naar kikkervisjes (dieren) → zonder n."),
    G("De gemeente kreeg ___ klachten over de parkeerregels; de ___ gingen over de hoge tarieven.", ("tientallen", "tientalle"), ("meeste", "meesten"),
      "Tientallen: altijd met n. De meeste verwijst naar klachten (zaken) → zonder n."),
    G("Bij de boerderij staan twee hekken: het ___ is nieuw, het ___ is al eeuwen oud.", ("houten", "houtene"), ("ijzeren", "ijzerene"),
      "Houten en ijzeren zijn stoffelijke bijvoeglijke naamwoorden; ze eindigen al op -en."),
    G("Op de rommelmarkt stonden ___ kraampjes, en ___ verkochten alleen boeken.", ("honderden", "honderde"), ("enkele", "enkelen"),
      "Honderden: altijd met n. Enkele verwijst naar kraampjes (je kunt 'kraampjes' invullen) → zonder n."),
    G("De trui van mijn opa is te klein, maar de ___ van mijn oom past wel; ___ truien heb ik niet.", ("katoenen", "katoenene"), ("andere", "anderen"),
      "Katoenen is stoffelijk en eindigt al op -en. Andere truien: er volgt een zelfstandig naamwoord → zonder n."),
    E("Het stadion was gevuld met ___ supporters.", "duizenden", "duizende", "T"),
    E("In de vitrine liggen veel ringen; de ___ zijn het duurst.", "gouden", "goudene", "ST"),
    E("Op het filmpje van de influencer reageerden ___ binnen een uur.", "miljoenen", "miljoene", "T"),
    E("Van de lepels in de la zijn de ___ het oudst.", "zilveren", "zilverene", "ST"),
    R("Waarom krijgt <b>wollen</b> geen extra e of n in: <i>Van al mijn sokken draag ik de wollen het liefst.</i>?", "ST"),
    R("Waarom schrijf je <b>honderden</b> met een n in: <i>Er lagen honderden schelpen op het strand.</i>?", "T"),
    W("Stoffelijke bijvoeglijke naamwoorden eindigen altijd op een e.", False,
      "Ze eindigen al op -en: gouden, zilveren, houten. Er komt geen e achter."),
    W("Tientallen schrijf je met n, ook als het over dingen gaat, zoals in 'tientallen fietsen'.", True,
      "Tientallen, honderden, duizenden en miljoenen hebben altijd een n."),
    W("In de zin 'Ik vind de houtene stoelen mooier' is houtene juist gespeld.", False,
      "Houten is een stoffelijk bijvoeglijk naamwoord en eindigt al op -en: de houten stoelen."),
    W("Een stoffelijk bijvoeglijk naamwoord geeft aan van welk materiaal iets gemaakt is.", True,
      "Bijvoorbeeld gouden (van goud), wollen (van wol), stenen (van steen)."),
    O("Leg uit waarom je in <i>Ik heb drie kettingen; de gouden draag ik het vaakst</i> niet <i>goudene</i> schrijft.",
      ["stoffelijk/materiaal/stof", "-en/eindigt al/op en"],
      "Gouden is een stoffelijk bijvoeglijk naamwoord (het geeft het materiaal aan) en eindigt al op -en. Daar komt geen extra e bij.",
      U["ST"]),
    O("Leg uit waarom <i>duizenden</i> met een n wordt geschreven in: <i>In het voorjaar bloeien er duizenden tulpen in de Bollenstreek.</i>",
      ["altijd", "tientallen/honderden/miljoenen/hoeveelheid"],
      "Duizenden hoort bij de woorden tientallen, honderden, duizenden en miljoenen: die schrijf je altijd met n, ook als het om dingen gaat.",
      U["T"]),
]))

# 33 · Betekenisverschil
TOETSEN.append(("Betekenisverschil: met of zonder n", "🔍", [
    G("Mijn vader en mijn oom zijn ___ fan van Feyenoord en ze kijken ___ wedstrijden samen.", ("beiden", "beide"), ("alle", "allen"),
      "Beiden = mijn vader en mijn oom (personen), zelfstandig gebruikt → met n. Alle wedstrijden: bijvoeglijk → zonder n."),
    G("De ___ buurtbewoners boden de ___ hulp aan bij hun huiswerk.", ("oudere", "ouderen"), ("jongeren", "jongere"),
      "Oudere buurtbewoners: er volgt een zelfstandig naamwoord → bijvoeglijk, zonder n. De jongeren: zelfstandig gebruikt, meer personen (hun huiswerk) → met n."),
    G("Na een uur ging de ___ met een taxi naar huis, maar de ___ bleven tot het einde van het feest.", ("zieke", "zieken"), ("anderen", "andere"),
      "De zieke = één persoon (ging) → -e. De anderen = de andere personen → met n."),
    G("De ___ van de twee zussen won de quiz, en ___ in de zaal klapten voor haar.", ("jongste", "jongsten"), ("velen", "vele"),
      "De jongste = één persoon (won) → -e. Velen = veel mensen in de zaal → met n."),
    G("Tim en Noor vonden ___ de film saai, maar ___ bezoekers waren enthousiast.", ("beiden", "beide"), ("andere", "anderen"),
      "Beiden = Tim en Noor → met n. Andere bezoekers: er volgt een zelfstandig naamwoord → zonder n."),
    mc("Wat is het verschil tussen <i>De oudere bewoner hielp de jongere.</i> en <i>De oudere bewoner hielp de jongeren.</i>?",
       "In de eerste zin helpt hij één jong persoon, in de tweede meerdere.",
       ["In de eerste zin helpt hij meerdere jongeren, in de tweede één persoon.",
        "Er is geen verschil; beide spellingen betekenen precies hetzelfde.",
        "In de tweede zin gaat het om jonge dieren in plaats van mensen."],
       "De jongere is enkelvoud (één persoon). De jongeren is meervoud: zelfstandig gebruikt bijvoeglijk naamwoord voor meer personen krijgt een n."),
    mc("Wat is het verschil tussen <i>Sommige gasten vonden het eten lekker, maar andere niet.</i> en <i>Sommige gasten vonden het eten lekker, maar anderen niet.</i>?",
       "Met 'andere' bedoel je andere gasten, met 'anderen' andere mensen in het algemeen.",
       ["Met 'anderen' bedoel je andere gasten, met 'andere' andere mensen in het algemeen.",
        "'Andere' slaat op één persoon en 'anderen' op meerdere personen.",
        "Er is geen verschil; je kiest zelf of je de n wel of niet schrijft."],
       "Zonder n kun je het zelfstandig naamwoord uit de zin (gasten) erachter invullen: andere gasten. Met n is het zelfstandig gebruikt en gaat het om andere mensen in het algemeen."),
    mc("Een goudhandelaar hangt op: <i>Wij kopen uw oude en gebruikte sieraden, bij voorkeur antieken.</i> Wat is hier fout?",
       "'antieken' moet 'antieke' zijn, want het verwijst naar sieraden.",
       ["'gebruikte' moet 'gebruikten' zijn, want het gaat om meer sieraden.",
        "'oude' moet 'ouden' zijn, omdat het woord in het meervoud staat.",
        "Er is niets fout; alle bijvoeglijke naamwoorden zijn goed gespeld."],
       "Antieke verwijst naar sieraden (zaken). Een zelfstandig gebruikt bijvoeglijk naamwoord voor zaken eindigt op -e, zonder n. 'Antieken' zou over personen gaan."),
    mc("In welke zin gaat het om <b>personen</b>?",
       "De meesten waren al vertrokken toen wij aankwamen.",
       ["De meeste waren al verwelkt toen wij aankwamen.",
        "De meeste lagen al op de grond toen wij aankwamen.",
        "De meeste waren al uitverkocht toen wij aankwamen."],
       "Alleen 'de meesten' heeft een n; een zelfstandig gebruikt telwoord met n verwijst naar personen."),
    mc("Wat is het verschil tussen <i>Beiden waren te laat.</i> en <i>Beide waren te laat.</i>?",
       "Bij 'beiden' gaat het om twee personen, bij 'beide' om twee dingen, zoals treinen.",
       ["Bij 'beiden' gaat het om twee dingen, bij 'beide' om twee personen, zoals zussen.",
        "'Beiden' is meervoud en 'beide' is enkelvoud, verder is de betekenis gelijk.",
        "'Beiden' zet je aan het begin van een zin en 'beide' midden in een zin."],
       "Zelfstandig gebruikte telwoorden krijgen alleen een n als ze naar personen verwijzen."),
    E("De ___ van de groep hielp de kleintjes met de opdracht.", "oudste", "oudsten", "AE", "Hielp = enkelvoud, één persoon."),
    E("Ook de ___ deden mee aan de sponsorloop, samen met een begeleider.", "slechtzienden", "slechtziende", "AP"),
    R("Waarom staat <b>werklozen</b> met een n in: <i>De gemeente helpt werklozen aan een baan.</i>?", "AP"),
    W("In 'De oudere bewoners trakteerden de jongere op taart' gaat het om één jonge persoon.", True,
      "De jongere zonder n is enkelvoud: één persoon. Met n (de jongeren) zouden het er meer zijn."),
    W("'Beiden' gebruik je voor twee dingen en 'beide' voor twee personen.", False,
      "Het is andersom: beiden (met n) voor personen, beide (zonder n) voor dingen of dieren."),
    W("In 'Er waren veel gasten; sommige bleven tot middernacht' verwijst sommige terug naar gasten.", True,
      "Zonder n kun je het zelfstandig naamwoord uit de zin ervoor invullen: sommige gasten."),
    W("In 'Van mijn kopjes zijn de blauwen het mooist' is blauwen juist gespeld.", False,
      "Het gaat om kopjes (zaken), dus zonder n: de blauwe."),
    O("Op de deur van een kantoor hangt: <i>Geen vreemde binnenlaten.</i> Leg uit wat hier fout is.",
      ["vreemden", "personen/mensen/meervoud"],
      "Er moet 'vreemden' staan. Het gaat om personen in het meervoud, en een zelfstandig gebruikt bijvoeglijk naamwoord voor personen krijgt dan een n.",
      U["AP"] + " Met 'vreemde' zou het over één persoon gaan."),
    O("Leg het betekenisverschil uit tussen <i>Enkele spelers waren blij, maar andere niet.</i> en <i>Enkele spelers waren blij, maar anderen niet.</i>",
      ["andere spelers/terug", "mensen/personen/algemeen/iedereen"],
      "In de eerste zin gaat het om andere spelers (je kunt 'spelers' invullen). In de tweede zin gaat het om andere mensen in het algemeen, dus niet alleen spelers.",
      "Zonder n verwijst het telwoord terug naar het zelfstandig naamwoord in de zin; met n is het zelfstandig gebruikt voor personen."),
    O("Leg uit waarom <i>beide</i> zonder n wordt geschreven in: <i>Ik heb een fiets en een step, maar beide zijn kapot.</i>",
      ["dingen/zaken/geen personen/voorwerpen"],
      "Beide verwijst naar een fiets en een step: dingen en geen personen. Dan schrijf je het zonder n.",
      U["Z"]),
]))

# 34 · Foutenjacht
TOETSEN.append(("Foutenjacht: vind en verbeter", "🕵️", [
    mc("Welke zin over de vergeten regenjassen is juist gespeld?",
       "Velen hadden hun regenjas vergeten.",
       ["Vele hadden hun regenjas vergeten.", "Velen kinderen hadden hun regenjas vergeten.", "Allen kinderen hadden hun regenjas vergeten."],
       "Velen is zelfstandig gebruikt en verwijst naar personen → met n. Vóór een zelfstandig naamwoord (kinderen) schrijf je vele/alle zonder n."),
    mc("In welke zin over aantallen is het vetgedrukte woord <b>fout</b> gespeld?",
       "Ik heb <b>honderde</b> foto's op mijn telefoon.",
       ["Er stonden <b>tientallen</b> auto's in de file.", "<b>Sommigen</b> vinden spruitjes heerlijk.", "Van de koekjes zijn er <b>enkele</b> verbrand."],
       "Honderden schrijf je altijd met n. De andere woorden zijn juist."),
    mc("Welke zin met een zelfstandig gebruikt bijvoeglijk naamwoord bevat een fout?",
       "Van de twee jassen kies ik de warmsten.",
       ["De ouderen in het dorp kregen een kerstpakket.", "Als nieuwe in de klas moest Mila even wennen.", "De zieken lagen op de eerste verdieping."],
       "Warmste verwijst naar een jas (zaak) → zonder n: de warmste. De andere zinnen zijn juist."),
    mc("Welke zin over de sieraden is helemaal juist?",
       "Van alle sieraden vind ik de zilveren het mooist.",
       ["Van alle sieraden vind ik de zilverene het mooist.", "Van allen sieraden vind ik de zilveren het mooist.", "Van alle sieraden vind ik de zilvere het mooist."],
       "Zilveren is stoffelijk en eindigt al op -en. Alle sieraden: bijvoeglijk → zonder n."),
    mc("In welke zin is de vorm van <b>beide/beiden</b> fout?",
       "Mijn opa en oma fietsen <b>beide</b> elke dag.",
       ["<b>Beide</b> zussen spelen hockey.", "Ik heb twee laptops, maar <b>beide</b> zijn traag.", "Ruben en Iris zijn <b>beiden</b> jarig in mei."],
       "Opa en oma zijn personen en er volgt geen zelfstandig naamwoord → beiden, met n."),
    mc("Welke van deze vier zinnen bevat een fout tegen de meervouds-n?",
       "De rijke betalen in dit land de meeste belasting.",
       ["De meesten kwamen met de fiets naar het feest.", "Er kwamen tienduizenden mensen naar de Dam.", "Van de pennen in mijn etui doen de meeste het niet."],
       "De rijken (meer personen, betalen) → met n. De andere zinnen zijn juist."),
    G("Toen het brandalarm afging, bleven ___ rustig zitten, maar de ___ renden in paniek naar buiten.", ("enkelen", "enkele"), ("meesten", "meeste"),
      "Enkelen en de meesten zijn zelfstandig gebruikt en verwijzen naar personen → allebei met n."),
    G("In het park staan ___ bankjes; de ___ zijn net geverfd.", ("tientallen", "tientalle"), ("meeste", "meesten"),
      "Tientallen: altijd met n. De meeste verwijst naar bankjes (zaken) → zonder n."),
    G("Mijn buurvrouw verzamelt theepotten: de ___ staan in de kast, de ___ op de vensterbank.", ("porseleinen", "porseleinene"), ("koperen", "koperene"),
      "Porseleinen en koperen zijn stoffelijke bijvoeglijke naamwoorden die al op -en eindigen."),
    G("Na de toets kreeg de ___ een compliment, en de ___ kregen een herkansing.", ("beste", "besten"), ("zwakkeren", "zwakkere"),
      "De beste = één persoon (kreeg) → -e. De zwakkeren = meer personen (kregen) → met n."),
    E("Bij de bushalte stonden ___ te wachten in de stromende regen.", "enkelen", "enkele", "P"),
    E("Ik heb drie jassen, maar de ___ is te warm voor de lente.", "dikste", "diksten", "AZ", "Het gaat om een jas."),
    R("Waarom is <b>enkelen</b> fout in: <i>Van de broodjes waren er nog enkelen over.</i>?", "Z", "Het gaat om broodjes, dus: enkele."),
    R("Waarom is <b>goudene</b> fout in: <i>Ze droeg een goudene armband.</i>?", "ST", "Goed is: een gouden armband."),
    W("De zin 'Sommigen dieren slapen de hele winter' is juist gespeld.", False,
      "Er volgt een zelfstandig naamwoord (dieren), dus bijvoeglijk: sommige dieren, zonder n."),
    W("De zin 'Velen weten niet dat een tomaat een vrucht is' is juist gespeld.", True,
      "Velen is zelfstandig gebruikt en verwijst naar mensen, dus met n."),
    W("De zin 'Op de vensterbank staan twee houten en een stenen beeldje' is juist gespeld.", True,
      "Houten en stenen zijn stoffelijke bijvoeglijke naamwoorden; die eindigen al op -en."),
    W("De zin 'In de bus zaten veel oudere' is juist gespeld.", False,
      "Het gaat om meer personen, dus: veel ouderen, met n."),
    O("Verbeter de fout en leg uit: <i>Honderde fans wachtten bij de artiesteningang op de zanger.</i>",
      ["honderden", "altijd"],
      "Het moet 'honderden' zijn: tientallen, honderden, duizenden en miljoenen schrijf je altijd met n.",
      U["T"]),
    O("Verbeter de fout en leg uit: <i>Jesse en Fleur helpen mij beide met verhuizen.</i>",
      ["beiden", "personen/mensen/twee mensen"],
      "Het moet 'beiden' zijn: het woord is zelfstandig gebruikt en verwijst naar twee personen, Jesse en Fleur.",
      U["P"]),
]))

# 35 · Gemengd
TOETSEN.append(("Gemengd oefenen", "🔀", [
    G("Op de veerboot naar Texel stonden ___ auto's, en de ___ hadden een fietsendrager.", ("honderden", "honderde"), ("meeste", "meesten"),
      "Honderden: altijd met n. De meeste verwijst naar auto's (zaken) → zonder n."),
    G("Van de twee films vond ik de ___ spannender, en ___ in de bioscoop schrokken van het einde.", ("eerste", "eersten"), ("velen", "vele"),
      "De eerste verwijst naar een film → zonder n. Velen = veel mensen → met n."),
    G("De ___ die binnenkwamen, kregen een gratis drankje, maar de ___ moesten betalen.", ("eersten", "eerste"), ("laatsten", "laatste"),
      "De eersten en de laatsten verwijzen naar personen (kwamen binnen, moesten betalen) en zijn zelfstandig gebruikt → met n."),
    G("Mijn tante heeft zeven katten; ___ slapen op haar bed, en ___ jagen 's nachts op muizen.", ("sommige", "sommigen"), ("andere", "anderen"),
      "Het gaat om katten (dieren) → allebei zonder n."),
    G("In deze winkel verkopen ze ___ tassen en ___ mutsen.", ("leren", "lerene"), ("wollen", "wollene"),
      "Leren en wollen zijn stoffelijke bijvoeglijke naamwoorden (van leer, van wol) die al op -en eindigen."),
    G("Alleen de ___ mochten meedoen aan de finale, dus de ___ deelnemers keken toe vanaf de tribune.", ("snelsten", "snelste"), ("andere", "anderen"),
      "De snelsten = meer personen, zelfstandig gebruikt → met n. Andere deelnemers: er volgt een zelfstandig naamwoord → zonder n."),
    G("Na de presentatie kwamen er ___ vragen, maar slechts ___ werden beantwoord.", ("tientallen", "tientalle"), ("enkele", "enkelen"),
      "Tientallen: altijd met n. Enkele verwijst naar vragen (zaken) → zonder n."),
    G("De ___ op de foto is mijn opa, en achter hem staan ___ uit zijn dorp.", ("oudste", "oudsten"), ("bekenden", "bekende"),
      "De oudste = één persoon (is) → -e. Bekenden = meer personen → met n."),
    E("In de rij voor de achtbaan stonden ___ al twee uur te wachten.", "velen", "vele", "P"),
    E("Van de schoenen in de uitverkoop pasten mij maar ___.", "weinige", "weinigen", "Z", "Het gaat om schoenen."),
    R("Waarom staat <b>eersten</b> met een n in: <i>De eersten die de finish haalden, kregen een medaille.</i>?", "P"),
    R("Waarom schrijf je <b>zilveren</b> zonder extra e in: <i>Van de bekers glanst de zilveren het mooist.</i>?", "ST"),
    W("In 'Duizenden vogels trokken naar het zuiden' is de n in duizenden juist, ook al gaat het om dieren.", True,
      "Duizenden heeft altijd een n, of het nu om mensen, dieren of dingen gaat."),
    W("'Enkele' in 'Enkele van de vissen waren ziek' moet met n, omdat het om meer dan één vis gaat.", False,
      "Het gaat om vissen (dieren), niet om personen: enkele, zonder n."),
    W("In 'De armen in de stad kregen gratis soep' heeft armen een n, omdat het om meer personen gaat.", True,
      "Armen is een zelfstandig gebruikt bijvoeglijk naamwoord voor personen in het meervoud."),
    W("In 'Ik heb rode en blauwe pennen; de blauwen zijn op' is blauwen juist gespeld.", False,
      "Het gaat om pennen (zaken): de blauwe, zonder n."),
    O("Leg uit waarom je <i>sommigen</i> met een n schrijft in: <i>Sommigen vinden huiswerk zinloos.</i>",
      ["personen/mensen", "zelfstandig/geen zelfstandig naamwoord/niets achter/invullen"],
      "Sommigen is zelfstandig gebruikt (er staat geen zelfstandig naamwoord achter) en verwijst naar personen. Dan schrijf je het met n.",
      U["P"]),
    O("Leg uit waarom <i>leren</i> geen extra e krijgt in: <i>Ik heb twee jassen; de leren is het warmst.</i>",
      ["stoffelijk/materiaal/stof/van leer", "-en/eindigt al/op en"],
      "Leren is een stoffelijk bijvoeglijk naamwoord (de jas is van leer) en eindigt al op -en. Er komt geen e bij.",
      U["ST"]),
    mc("Welke zin over de duikplank is juist gespeld?",
       "Weinigen durfden van de hoge duikplank te springen.",
       ["Weinige durfden van de hoge duikplank te springen.",
        "Weinigen kinderen durfden van de duikplank te springen.",
        "Weinig kinderen durfde van de hoge duikplank te springen."],
       "Weinigen is zelfstandig gebruikt en verwijst naar personen → met n."),
    mc("In welke zin over school is het vetgedrukte woord <b>fout</b>?",
       "Op het schoolplein stonden <b>tientalle</b> fietsen.",
       ["De <b>zieken</b> kregen een bos bloemen.", "Ik koop de <b>goedkope</b> schoenen.", "<b>Velen</b> waren het niet eens met de regel."],
       "Tientallen schrijf je altijd met n."),
]))

# 36 · Eindtoets §7.3
TOETSEN.append(("Eindtoets met of zonder n", "🎯", [
    G("Volgens de krant protesteerden ___ in Den Haag, maar slechts ___ werden gearresteerd.", ("duizenden", "duizende"), ("enkelen", "enkele"),
      "Duizenden: altijd met n. Enkelen = enkele personen, zelfstandig gebruikt → met n."),
    G("In de kelder staan ___ flessen wijn, en ___ zijn al dertig jaar oud.", ("honderden", "honderde"), ("sommige", "sommigen"),
      "Honderden: altijd met n. Sommige verwijst naar flessen (zaken) → zonder n."),
    G("Opa gaf mij twee horloges: het ___ draag ik elke dag, het ___ ligt in een kluis.", ("stalen", "stalene"), ("gouden", "goudene"),
      "Stalen en gouden zijn stoffelijke bijvoeglijke naamwoorden die al op -en eindigen."),
    G("Op de camping waren de ___ al vroeg wakker, maar de ___ sliepen uit tot de middag.", ("ouderen", "oudere"), ("jongeren", "jongere"),
      "Ouderen en jongeren zijn zelfstandig gebruikte bijvoeglijke naamwoorden voor meer personen → met n."),
    G("Er zijn veel soorten appels: de ___ zijn zuur, de ___ juist zoet.", ("groene", "groenen"), ("rode", "roden"),
      "Groene en rode verwijzen naar appels (zaken) → op -e, zonder n."),
    G("Na de storm lagen er ___ takken op straat en waren ___ daken beschadigd.", ("honderden", "honderde"), ("enkele", "enkelen"),
      "Honderden: altijd met n. Enkele daken: er volgt een zelfstandig naamwoord → zonder n."),
    G("Lot en Mees zingen ___ in een koor, en ___ concerten zijn in de kerk.", ("beiden", "beide"), ("sommige", "sommigen"),
      "Beiden = Lot en Mees (personen) → met n. Sommige concerten: bijvoeglijk → zonder n."),
    G("Voor ___ is het museum gratis; ___ betalen tien euro.", ("werklozen", "werkloze"), ("anderen", "andere"),
      "Werklozen = meer personen → met n. Anderen = andere personen, zelfstandig gebruikt → met n."),
    E("In de schoenenwinkel twijfelde ik lang, maar uiteindelijk nam ik toch de ___.", "dure", "duren", "AZ", "Het gaat om schoenen."),
    E("In de nacht van oud op nieuw werden er ___ vuurpijlen afgestoken.", "miljoenen", "miljoene", "T"),
    R("Waarom staat <b>blinde</b> zonder n in: <i>De blinde stak met zijn geleidehond de straat over.</i>?", "AE"),
    R("Waarom staat <b>weinige</b> zonder n in: <i>Slechts weinige toeristen bezoeken dit eiland.</i>?", "B"),
    mc("Welke zin over de tomaten is helemaal juist?",
       "De meeste tomaten zijn rijp, maar sommige zijn nog groen.",
       ["De meesten tomaten zijn rijp, maar sommige zijn nog groen.",
        "De meeste tomaten zijn rijp, maar sommigen zijn nog groen.",
        "De meesten tomaten zijn rijp, maar sommigen zijn nog groen."],
       "Vóór 'tomaten' bijvoeglijk → de meeste. Sommige verwijst naar tomaten (zaken) → zonder n."),
    mc("Welke zin over het betalen in de winkel bevat een fout?",
       "Bij de kassa vroegen enkele of ze mochten pinnen.",
       ["Bij de kassa vroegen enkelen of ze mochten pinnen.", "Velen wilden contant betalen.", "Van de bonnetjes waren er enkele kwijt."],
       "Enkele in de eerste zin verwijst naar personen en is zelfstandig gebruikt → enkelen, met n."),
    W("Een zelfstandig gebruikt telwoord dat naar personen verwijst, schrijf je met n.", True,
      "Bijvoorbeeld: velen, sommigen, enkelen, beiden, allen."),
    W("In het spreekwoord 'Vele handen maken licht werk' moet vele met n, omdat handen bij personen horen.", False,
      "Er volgt een zelfstandig naamwoord (handen), dus is vele bijvoeglijk gebruikt: zonder n."),
    W("Een zelfstandig gebruikt bijvoeglijk naamwoord voor zaken eindigt meestal op -e.", True,
      "Bijvoorbeeld: Ik neem de goedkope. Alleen stoffelijke bijvoeglijke naamwoorden (gouden, zilveren) eindigen op -en."),
    W("Tientallen en miljoenen schrijf je alleen met n als het om mensen gaat.", False,
      "Tientallen, honderden, duizenden en miljoenen hebben altijd een n."),
    O("Leg uit waarom <i>gouden</i> geen extra e of n krijgt in: <i>Ik heb drie medailles; de gouden hangen aan de muur.</i>",
      ["stoffelijk/materiaal/stof/van goud", "-en/eindigt al/op en"],
      "Gouden is een stoffelijk bijvoeglijk naamwoord (van goud) en eindigt al op -en. Er komt geen extra e of n bij.",
      U["ST"]),
    O("Leg uit waarom <i>beide</i> in <i>Ik heb twee katten en beide zijn zwart</i> zonder n staat, maar <i>beiden</i> in <i>Jan en Petra werken beiden in de zorg</i> met n.",
      ["dieren/geen personen", "personen/mensen"],
      "In de eerste zin verwijst beide naar katten, dus dieren: zonder n. In de tweede zin verwijst beiden naar Jan en Petra, twee personen: met n.",
      "Een zelfstandig gebruikt telwoord krijgt alleen een n als het naar personen verwijst."),
]))

# ---- onderwerp (oefenen) --------------------------------------------------------------------------
THEORIE = """
<h3>1. Telwoorden: zelfstandig of niet-zelfstandig?</h3>
<p>Telwoorden als <i>enkele, vele, weinige, sommige, alle, beide</i> kun je op twee manieren gebruiken:</p>
<ul>
  <li><b>Niet-zelfstandig (bijvoeglijk):</b> er staat een zelfstandig naamwoord achter, of je kunt er een zelfstandig naamwoord uit de zin (of de zin ervoor) achter invullen. Je schrijft het telwoord dan <b>zonder n</b>.<br><i>Bijna <b>alle</b> leerlingen hebben een eigen mobiel.</i> · <i><b>Enkele</b> van de gevonden kastanjes werden gebruikt voor een herfststuk.</i></li>
  <li><b>Zelfstandig:</b> je kunt er geen zelfstandig naamwoord achter invullen. Duidt het telwoord <b>personen</b> aan, dan schrijf je het <b>met n</b>.<br><i><b>Allen</b> kregen een oproep voor de griepprik, maar <b>sommigen</b> zijn niet komen opdagen.</i></li>
</ul>
<div class="formule-box"><b>Vuistregel telwoorden</b><br>zelfstandig gebruikt + personen → <b>met n</b> (velen, enkelen, sommigen, beiden, de meesten)<br>bijvoeglijk gebruikt óf dingen/dieren → <b>zonder n</b> (vele boeken, de meeste zijn romans)</div>
<div class="info-box let-op"><h4>Let op: altijd met n</h4><p><i>Tientallen, honderden, (tien)duizenden</i> en <i>miljoenen</i> hebben <b>altijd</b> een n, ook bij dingen: <i>tientallen fietsen, duizenden tulpen</i>.</p></div>

<h3>2. Zelfstandig gebruikte bijvoeglijke naamwoorden</h3>
<p>Ook een bijvoeglijk naamwoord kan zelfstandig gebruikt worden: <i>de oudere, de zieken, de goedkope</i>.</p>
<ul>
  <li><b>Personen:</b> in het enkelvoud eindigen ze op <b>-e</b>, in het meervoud krijgen ze een <b>n</b>: <i>Als <b>jongere</b> kun je eenzame <b>ouderen</b> helpen.</i></li>
  <li><b>Zaken (dingen):</b> ze eindigen meestal op <b>-e</b>, <b>zonder n</b>: <i>Van de twee laptops koop ik de <b>goedkope</b>.</i></li>
  <li><b>Stoffelijke bijvoeglijke naamwoorden</b> (het materiaal: goud, zilver, hout, wol, steen) eindigen al op <b>-en</b>; daar komt niets bij: <i>meer dan dertig <b>zilveren</b> en enkele kostbare <b>gouden</b></i>.</li>
</ul>
<div class="voorbeeld"><div class="vb-kop">Voorbeeld: betekenisverschil</div>
<div class="stap"><i>De oudere bewoners trakteerden de <b>jongere</b>.</i> → één jong persoon.</div>
<div class="stap"><i>De oudere bewoners trakteerden de <b>jongeren</b>.</i> → meerdere jonge personen.</div>
<div class="stap"><i>Enkele dames waren lovend, maar <b>andere</b> niet.</i> → andere dames.</div>
<div class="stap"><i>Enkele dames waren lovend, maar <b>anderen</b> niet.</i> → andere mensen in het algemeen.</div></div>
<div class="info-box tip"><h4>Stappenplan</h4><p>1. Staat er een zelfstandig naamwoord achter of kun je er een uit de zin invullen? → zonder n.<br>2. Is het tientallen/honderden/duizenden/miljoenen? → altijd n.<br>3. Gaat het om personen in het meervoud? → met n.<br>4. Gaat het om dingen of dieren? → zonder n (stoffelijk: gewoon -en).</p></div>
"""

OEFEN = [
    {"type": "mc", "niveau": 1, "vraag": "Wanneer schrijf je een zelfstandig gebruikt telwoord met n?",
     "_goed": "Als het naar personen verwijst.", "_fout": ["Als het naar dingen verwijst.", "Als er een zelfstandig naamwoord achter staat.", "Alleen aan het begin van een zin."],
     "uitleg": U["P"], "hint": "Denk aan: velen, sommigen, beiden."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "Honderden en duizenden schrijf je altijd met n.", "antwoord": True,
     "uitleg": "Waar. " + U["T"], "hint": "Ook bij dingen: honderden boeken."},
    {"type": "mc", "niveau": 1, "vraag": "Kies de juiste vorm: <i>___ vinden de nieuwe schooltijden te vroeg.</i>",
     "_goed": "Velen", "_fout": ["Vele"], "uitleg": U["P"] + " Velen = veel mensen.", "hint": "Gaat het om personen?"},
    {"type": "mc", "niveau": 2, "vraag": "Kies de juiste vorm: <i>Ik heb tien knuffels, maar ___ zijn al heel oud.</i>",
     "_goed": "sommige", "_fout": ["sommigen"], "uitleg": U["Z"] + " Het gaat om knuffels.", "hint": "Kun je 'knuffels' erachter invullen?"},
    {"type": "waaronwaar", "niveau": 2, "vraag": "In 'Van de drie truien neem ik de groenen' is groenen juist gespeld.", "antwoord": False,
     "uitleg": "Niet waar. " + U["AZ"] + " Goed is: de groene.", "hint": "Truien zijn zaken."},
    {"type": "mc", "niveau": 2, "vraag": "Kies de juiste vorm: <i>Ook de ___ in het verpleeghuis kregen een bloemetje.</i>",
     "_goed": "ouderen", "_fout": ["oudere"], "uitleg": U["AP"], "hint": "Gaat het om één of meer personen?"},
    {"type": "mc", "niveau": 2, "vraag": "Welke vorm is juist? <i>Op tafel lagen twee armbanden; de ___ was van mijn moeder.</i>",
     "_goed": "zilveren", "_fout": ["zilverene", "zilvere", "zilverenen"], "uitleg": U["ST"], "hint": "Zilver is een materiaal."},
    {"type": "waaronwaar", "niveau": 3, "vraag": "In 'De oudere bewoners trakteerden de jongeren' gaat het om meerdere jonge personen.", "antwoord": True,
     "uitleg": "Waar. Jongeren heeft een n: meervoud, meerdere personen. De jongere (zonder n) is één persoon.", "hint": "Let op de n aan het eind."},
]
# ---- bouwen ---------------------------------------------------------------------------------------
def schud(v):
    """Zet _goed/_fout om naar opties + antwoord (willekeurige plek)."""
    opts = [v["_goed"]] + v["_fout"]
    rng.shuffle(opts)
    out = {k: x for k, x in v.items() if not k.startswith("_")}
    out["opties"] = opts
    out["antwoord"] = opts.index(v["_goed"])
    # sleutelvolgorde zoals in de bestaande bestanden
    keys = ["type", "niveau", "vraag", "opties", "antwoord", "uitleg", "hint"]
    return {k: out[k] for k in keys if k in out}


def langste(v):
    L = [len(o.replace("<b>", "").replace("</b>", "")) for o in v["opties"]]
    return all(i == v["antwoord"] or L[i] < L[v["antwoord"]] for i in range(len(L)))


def ok(vragen):
    m = [v for v in vragen if v["type"] == "mc"]
    s = [v["antwoord"] for v in m]
    if max(s.count(i) for i in set(s)) / len(s) > 0.4:
        return False
    if any(all(a == s[i - p] for i, a in enumerate(s) if i >= p) for p in (2, 3, 4)):
        return False
    n = max(len(v["opties"]) for v in m)
    if sum(1 for i in range(1, len(s)) if s[i] == (s[i - 1] + 1) % n) / (len(s) - 1) >= 0.5:
        return False
    return True


def bouw(ruw):
    for _ in range(5000):
        vragen = [schud(v) if v["type"] == "mc" else v for v in ruw]
        if ok(vragen):
            return vragen
    raise SystemExit("geen geldige optievolgorde gevonden")


def schrijf(pad, kop, obj, fn):
    with open(pad, "w", encoding="utf-8") as f:
        f.write(kop + "\n" + fn + "(" + json.dumps(obj, ensure_ascii=False, indent=2) + ");\n")


alle_vragen = set()
for i, (sub, icoon, ruw) in enumerate(TOETSEN):
    nr = 30 + i
    assert len(ruw) == 20, (nr, len(ruw))
    vragen = bouw(ruw)
    for v in vragen:
        assert v["vraag"] not in alle_vragen, v["vraag"]
        alle_vragen.add(v["vraag"])
        if v["type"] == "open":
            q = re.sub(r"<[^>]+>", " ", v["vraag"]).lower()
            for s in v["sleutelwoorden"]:
                for w in s.split("/"):  # geen enkel alternatief mag al in de vraag staan (open_check.js)
                    assert not (len(w) > 2 and w.lower() in q), (nr, w)
    m = [v for v in vragen if v["type"] == "mc"]
    lang = sum(langste(v) for v in m)
    assert lang / len(m) <= 0.5, (nr, lang, len(m))
    wo = [v for v in vragen if v["type"] == "waaronwaar"]
    print(f"examen_{nr}: mc {len(m)} (juist=langste {lang}), wow {len(wo)} (onwaar {sum(not v['antwoord'] for v in wo)}), "
          f"open {sum(v['type'] == 'open' for v in vragen)}, volgorde {''.join(str(v['antwoord']) for v in m)}")
    schrijf(os.path.join(ROOT, f"examen_{nr}.js"),
            "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 7 Spelling §3 Met of zonder n?) — gegenereerd door tools/gen_nederlands_c7_3.py */",
            {"id": f"ex-h3-nederlands-{nr}", "hoofdstuk": 7, "hoofdstukTitel": "Cursus 7 — Spelling", "paragraaf": "7.3",
             "titel": f"Toets {nr} — §7.3 {sub}", "vak": "Nederlands · HAVO 3 (Cursus 7)", "icoon": icoon, "duurMin": 20,
             "vragen": vragen}, "DURU.registerExamen")

oefen = bouw(OEFEN)
assert len(THEORIE) >= 1500
schrijf(os.path.join(ROOT, "c7_3.js"),
        "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 7 Spelling §3) — gegenereerd door tools/gen_nederlands_c7_3.py */",
        {"id": "c7-3-met-of-zonder-n", "hoofdstuk": 7, "paragraaf": "7.3", "titel": "§3 Met of zonder n?",
         "korteUitleg": "Wanneer schrijf je velen, sommigen, beiden, ouderen met n — en wanneer juist niet?",
         "icoon": "✒️", "theorie": THEORIE, "vragen": oefen}, "DURU.register")
print("c7_3.js: theorie", len(THEORIE), "tekens,", len(oefen), "oefenvragen")
