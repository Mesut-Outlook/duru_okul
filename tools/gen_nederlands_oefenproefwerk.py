#!/usr/bin/env python3
"""Nederlands HAVO 3 · Oefenproefwerk A/B/C (examen_68…70.js, ex-h3-nederlands-68…70) — 2026-11-08.

Kullanıcı isteği: "son 1 hafta / 10 gündür yaptıklarından, sorumlu olduğu tüm bölümlerden karışık 3 test —
gerçek sınavda nasıl olacak görelim". Kapsam = Duru'nun 29-10…08-11 arasında çalıştığı stof:
Cursus 7 Spelling §7.2, §7.3 (+ bijv. nw -e/-en), §7.9, §7.10, §7.11 · Cursus 5 Grammatica §5.3, §5.5.

Her proefwerk: Deel A Spelling (1–11) → Deel B Grammatica (12–20), alle 7 paragrafen. ~De helft van de vragen
richt zich op Duru's fouten uit de laatste pogingen (zwakte-analyse: `python3 tools/zwakte.py nederlands --fouten`);
afleiders = haar echte foute antwoorden. Open vragen kort ("verbeter + waarom") op plek 7 en 15, niet aan het
eind (leeg laten stijgt naar het einde van de toets).

Draai: python3 tools/gen_nederlands_oefenproefwerk.py
Daarna: node tools/gate.js nederlands && node tools/open_check.js && node tools/teslim_check.js nederlands 68
"""
import json, os, random, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "havo3", "nederlands", "js", "data")
rng = random.Random("oefenproefwerk_2026_11_08")
EERSTE = 68


def mc(vraag, goed, fout, uitleg):
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": list(fout), "uitleg": uitleg}


def I(vraag, antwoord, uitleg):
    """Spellings-invul: altijd exact: True."""
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "exact": True, "uitleg": uitleg}


def W(stelling, waar, uitleg):
    return {"type": "waaronwaar", "vraag": stelling, "antwoord": waar,
            "uitleg": ("Waar. " if waar else "Niet waar. ") + uitleg}


def O(vraag, sleutels, model, uitleg, minT=1):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": minT,
            "modelantwoord": model, "uitleg": uitleg}


TOETSEN = []

# =====================================================================================================
# 68 · Oefenproefwerk A
# =====================================================================================================
TOETSEN.append(dict(letter="A", vragen=[
    # --- Deel A · Spelling ---
    I("____ (houden) jouw zus ook zo van paardrijden?", "houdt",
      "Het onderwerp is <i>jouw zus</i> (hij/zij), niet <i>jij</i>. De t valt alleen weg als <i>jij/je</i> achter de persoonsvorm staat. Dus: Houdt jouw zus …?"),
    mc("Kies de juiste vorm: <i>Vorige zomer ____ (fietsen) mijn ouders langs de hele Rijn.</i>",
       "fietsten", ["fietste", "fietsden", "fietsde"],
       "Stam fiets eindigt op s → 't kofschip X → -te. Het onderwerp (mijn ouders) is meervoud → -ten: fietsten."),
    W("In de zin <i>Wordt u al geholpen, meneer?</i> is de persoonsvorm goed gespeld.", True,
      "Bij <i>u</i> blijft de t staan, ook als u achter de persoonsvorm staat. Alleen bij jij/je valt de t weg."),
    I("De gemeente heeft de smalle weg langs de school vorig jaar ____ (verbreden).", "verbreed",
      "Stam verbreed; ver- krijgt geen ge-. Verlengen: de verbrede weg → d. Verbreed + d = verbreedd, maar je schrijft nooit twee d's aan het eind: verbreed."),
    I("Mijn broer heeft de hele zaterdagmiddag ____ (gamen).", "gegamed",
      "Engels werkwoord: kijk naar de uitspraak van de stam. Game klinkt als 'geem', eindigt op een m-klank → niet in 't kofschip X → ge + game + d = gegamed."),
    mc("Kies de juiste vorm: <i>Wat er gisteren in de les is ____ (gebeuren), vertel ik je morgen.</i>",
       "gebeurd", ["gebeurt", "gebeurdt", "gebeurde"],
       "<i>Is … gebeurd</i> is een voltooid deelwoord (hulpwerkwoord zijn). Verlengen: het gebeurde voorval → d. <i>Gebeurt</i> is tegenwoordige tijd: het gebeurt nu."),
    O("In de zin <i>Tijdens de les antwoordde de leerlingen heel enthousiast op de vragen van de docent.</i> staat één spelfout. Schrijf het foute woord verbeterd op en noem de regel.",
      ["antwoordden", "meervoud/meerdere personen"],
      "Het foute woord is antwoordde; dat moet antwoordden zijn. Het onderwerp is meervoud, dus de verleden tijd krijgt -den: antwoord + den.",
      "Stam antwoord (d niet in 't kofschip X) → -de; meervoud → -den: antwoordden.", minT=2),
    mc("Kies de juiste combinatie: <i>Van de twaalf deelnemers kwamen er maar ____ op tijd; de ____ moesten op de volgende bus wachten.</i>",
       "enkelen – anderen", ["enkele – andere", "enkelen – andere", "enkele – anderen"],
       "Beide woorden worden zelfstandig gebruikt en verwijzen naar personen (deelnemers) → allebei met n: enkelen, anderen."),
    I("Vul de juiste vorm van <i>klein</i> in: <i>Wij logeerden in een ____ hotel vlak bij zee.</i>", "klein",
      "Hotel is een het-woord en ervoor staat <i>een</i> → het bijvoeglijk naamwoord krijgt géén -e: een klein hotel (maar: het kleine hotel)."),
    W("In de zin <i>Ik heb twee jassen: een wollen en een leren.</i> zijn de stoffelijke bijvoeglijke naamwoorden goed gespeld.", True,
      "Stoffelijke bijvoeglijke naamwoorden (gemaakt van wol, leer) eindigen op -en: wollen, leren."),
    mc("Welk verkleinwoord is goed gespeld?",
       "hobby'tje", ["jockey'tje", "display'tje", "cowboy'tje"],
       "Bij hobby klinkt de y als ie → apostrof: hobby'tje. Bij jockey, display en cowboy hoort de y bij een tweeklank (ee/ei/oi) → geen apostrof: jockeytje, displaytje, cowboytje."),
    I("Verbeter het fout gespelde woord: <i>De auto reed met hoge snelheid door de barriere van de parkeergarage.</i>", "barrière",
      "Barrière spreek je uit met een open è-klank (als in 'pet') → accent grave: barrière. Niet é (aigu)."),
    W("<i>Mijn tante komt uit 's Hertogenbosch.</i> Deze plaatsnaam is goed gespeld.", False,
      "De officiële naam is 's-Hertogenbosch: na 's komt een streepje (net als 's-Gravenhage)."),
    # --- Deel B · Grammatica ---
    mc("<i>Mijn zus drinkt graag rode wijn en mijn moeder witte.</i> Wat voor samentrekking is dit?",
       "voorwaartse samentrekking", ["achterwaartse samentrekking", "geen samentrekking, het onderwerp verschilt", "foute samentrekking, de functie verschilt"],
       "<i>Drinkt graag</i> en <i>wijn</i> staan in het eerste deel en worden verderop weggelaten: … en mijn moeder [drinkt graag] witte [wijn]. Eerst genoemd, later weggelaten = voorwaarts."),
    O("In de zin <i>De gemeente heeft zijn plannen voor het nieuwe zwembad gepresenteerd.</i> staat een fout verwijswoord. Schrijf het goede verwijswoord op en leg uit waarom.",
      ["haar", "vrouwelijk"],
      "Het goede verwijswoord is haar, want gemeente is een vrouwelijk woord (een instantie, net als regering en politie).",
      "Gemeente, regering, politie: vrouwelijke woorden → bezittelijk voornaamwoord haar.", minT=2),
    I("Schrijf korter met een samentrekking en zet het streepje goed: <i>zomerjassen en winterjassen</i>.",
      "zomer- en winterjassen|zomer-en winterjassen",
      "Het gemeenschappelijke deel (jassen) staat achteraan en wordt in het eerste woord weggelaten → streepje direct na het eerste deel: zomer- en winterjassen."),
    mc("In welke zin is de samentrekking <b>onjuist</b>?",
       "Ik heb de soep gemaakt en de buren opgegeten.",
       ["Thijs zit in de vierde klas en zijn zus in de zesde.", "De buurman maait het gras en snoeit de heg.", "Lisa speelt viool en Daan gitaar."],
       "In 'Ik heb de soep gemaakt en de buren [hebben] opgegeten' verschilt de vorm van het weggelaten werkwoord (heb ↔ hebben). Een weggelaten woord moet precies dezelfde vorm hebben."),
    W("<i>Grote- en kleine pakketten</i>: hier hoort een streepje na <i>grote</i>.", False,
      "Weggelaten is het hele woord 'pakketten', geen deel van een samenstelling. Een streepje gebruik je alleen als je een deel van een woord weglaat: groot en klein → grote en kleine pakketten."),
    mc("Kies het juiste verwijswoord: <i>Het boek ____ ik van mijn oma kreeg, heb ik al drie keer gelezen.</i>",
       "dat", ["die", "wat", "wie"],
       "Boek is een het-woord (het boek) → betrekkelijk voornaamwoord dat. Die hoort bij de-woorden, wat bij niets/alles/iets."),
    mc("Welke zin is goed?",
       "Ik heb hun gisteren een berichtje gestuurd.",
       ["Ik heb hen gisteren een berichtje gestuurd.", "Hun hebben gisteren een berichtje gestuurd.", "Ik heb aan hun gisteren een berichtje gestuurd."],
       "Meewerkend voorwerp zonder voorzetsel → hun. Na een voorzetsel (aan, voor, met) → hen. Als onderwerp → zij, nooit hun."),
]))

# =====================================================================================================
# 69 · Oefenproefwerk B
# =====================================================================================================
TOETSEN.append(dict(letter="B", vragen=[
    # --- Deel A · Spelling ---
    I("____ (antwoorden) jouw zus altijd zo snel op berichtjes?", "antwoordt",
      "Het onderwerp is <i>jouw zus</i>, niet jij → stam + t: antwoord + t = antwoordt. Alleen bij jij/je achter de persoonsvorm valt de t weg."),
    mc("Welke vraag aan je klasgenoot is goed gespeld?",
       "Vind jij dit ook een goed idee?",
       ["Vindt jij dit ook een goed idee?", "Vint jij dit ook een goed idee?", "Vindt je dit ook een goed idee?"],
       "Jij/je staat achter de persoonsvorm → alleen de stam: vind. De d van de stam blijft altijd staan (vinden → vind)."),
    I("Vorig weekend ____ (oefenen) de muzikanten urenlang voor het concert.", "oefenden",
      "Stam oefen eindigt op n → niet in 't kofschip X → -de. Het onderwerp (de muzikanten) is meervoud → -den: oefenden."),
    W("<i>Het pakketje is gisteren al bezorgt.</i> Deze zin is goed gespeld.", False,
      "Bezorgd is een voltooid deelwoord. Verlengen: het bezorgde pakketje → d. Dus: is bezorgd."),
    mc("Welke vorm van <i>updaten</i> is goed in: <i>De app is vannacht automatisch ____.</i>",
       "geüpdatet", ["geüpdated", "geupdatet", "geüpdate"],
       "Stam update eindigt op een t-klank → 't kofschip X → t: geüpdatet. Trema op de u omdat ge- en up- botsen (ge-up)."),
    I("Vul de juiste vorm van <i>gebeuren</i> in: <i>Er ____ elke dag wel iets geks in onze klas.</i>", "gebeurt",
      "Tegenwoordige tijd, onderwerp 'er … iets' (enkelvoud) → stam + t: gebeurt. <i>Gebeurd</i> is het voltooid deelwoord (is gebeurd)."),
    O("In de zin <i>Mijn ouders hebben de zolder vorig jaar helemaal verbouwt.</i> staat één spelfout. Schrijf het foute woord verbeterd op en leg de regel uit.",
      ["verbouwd", "verlengen/kofschip"],
      "Het foute woord is verbouwt; dat moet verbouwd zijn. Verlengen: de verbouwde zolder → d (de w-klank zit niet in 't kofschip X).",
      "Voltooid deelwoord: verlengen (de verbouwde zolder) of 't kofschip X → verbouwd.", minT=2),
    mc("Kies de juiste combinatie: <i>In het asiel zaten zes katten: de ____ waren al geadopteerd, de ____ zochten nog een baasje.</i>",
       "zwarte – grijze", ["zwarten – grijzen", "zwarte – grijzen", "zwarten – grijze"],
       "Het zelfstandig gebruikte bijvoeglijk naamwoord verwijst naar dieren (katten), niet naar personen → geen n: zwarte, grijze."),
    I("Vul het stoffelijk bijvoeglijk naamwoord van <i>goud</i> in: <i>Oma draagt altijd haar ____ ketting.</i>", "gouden",
      "Stoffelijke bijvoeglijke naamwoorden eindigen op -en: van goud → gouden."),
    W("<i>Mijn ouders? Beide kwamen te laat.</i> Hier is <i>beide</i> goed gespeld.", False,
      "Beide verwijst hier zelfstandig naar personen (mijn ouders) → met n: Beiden kwamen te laat."),
    mc("Welke zin is helemaal goed gespeld?",
       "'s Avonds eet Ruben vaak pizza's met zijn vrienden.",
       ["s'Avonds eet Ruben vaak pizza's met zijn vrienden.", "'s Avonds eet Ruben vaak pizzas met zijn vrienden.", "'s Avonds eet Ruben vaak pizza'tjes met zijn vrienden."],
       "'s = des (weglating) → apostrof vóór de s; aan het begin van de zin krijgt het volgende woord de hoofdletter: 's Avonds. Pizza eindigt op een klinker → pizza's. Het verkleinwoord is pizzaatje (aa), zonder apostrof."),
    I("Verbeter het fout gespelde woord: <i>We hebben kaartjes gekocht voor de premiere van de nieuwe film.</i>", "première",
      "Première spreek je uit met een open è-klank (als in 'pet') → accent grave: première. Niet premiére."),
    W("<i>Geïnteresseerd</i>, <i>ruïne</i> en <i>zee-egel</i> zijn alle drie goed gespeld.", True,
      "Een trema zet je als twee klinkers anders verkeerd gelezen worden (ge-ïn, ru-ï). In een samenstelling (zee + egel) gebruik je een koppelteken, geen trema."),
    # --- Deel B · Grammatica ---
    mc("<i>Tim belt zijn opa en Sanne haar oma.</i> Welke omschrijving klopt?",
       "voorwaarts: 'belt' is weggelaten", ["achterwaarts: 'belt' is weggelaten", "voorwaarts: 'oma' is weggelaten", "achterwaarts: 'Sanne' is weggelaten"],
       "Belt staat in het eerste deel en wordt in het tweede deel weggelaten: … en Sanne [belt] haar oma. Eerst genoemd, later weggelaten = voorwaarts."),
    O("De zin <i>Op zaterdag werkt Noor in de bakkerij en Jens bezorgt kranten.</i> is na de samentrekking fout. Schrijf het tweede deel van de zin goed op.",
      ["bezorgt Jens/bezorgt hij"],
      "Op zaterdag werkt Noor in de bakkerij en bezorgt Jens kranten.",
      "'Op zaterdag' geldt ook voor het tweede deel (weggelaten). Na een bepaling vooraan komt de persoonsvorm vóór het onderwerp: … en [op zaterdag] bezorgt Jens kranten."),
    I("Schrijf korter met een samentrekking: <i>fietsbellen en fietslampjes</i>.", "fietsbellen en -lampjes|fietsbellen en - lampjes",
      "Het gemeenschappelijke deel (fiets) staat vooraan en wordt in het tweede woord weggelaten → streepje vóór het tweede deel: fietsbellen en -lampjes."),
    mc("Welke samentrekking is <b>achterwaarts</b>?",
       "zowel jonge als oude honden",
       ["Ik lees een boek en mijn zus een tijdschrift.", "Pim fietst naar school en Eva naar de sportschool.", "regenjassen en -laarzen"],
       "In 'zowel jonge [honden] als oude honden' staat het gemeenschappelijke woord achteraan en is het eerder weggelaten = achterwaarts. De andere drie zijn voorwaarts."),
    W("In <i>Er is niets wat ik liever doe dan zwemmen.</i> is het verwijswoord goed gekozen.", True,
      "Na niets, alles, iets en veel gebruik je wat: niets wat …"),
    mc("Kies het juiste verwijswoord: <i>Mijn fiets is kapot; ik moet ____ morgen laten maken.</i>",
       "hem", ["haar", "het", "hen"],
       "Fiets is een de-woord voor een ding → hem. Haar gebruik je voor vrouwelijke woorden (zoals gemeente, regering), het voor het-woorden."),
    I("Vul het juiste verwijswoord in (één woord): <i>Het onderwerp ____ we vandaag praten, is erg actueel.</i> (praten over iets)", "waarover",
      "Bij een zaak + voorzetsel gebruik je waar + voorzetsel: praten over het onderwerp → het onderwerp waarover we praten."),
]))

# =====================================================================================================
# 70 · Oefenproefwerk C
# =====================================================================================================
TOETSEN.append(dict(letter="C", vragen=[
    # --- Deel A · Spelling ---
    I("____ (rijden) u vandaag zelf naar de vergadering?", "rijdt",
      "Bij u blijft de t staan, ook als u achter de persoonsvorm staat: Rijdt u …? (stam rijd + t)."),
    mc("Kies de juiste vorm: <i>Gisteren ____ (wachten) wij een uur op de trein.</i>",
       "wachtten", ["wachten", "wachtte", "wachtden"],
       "Stam wacht eindigt op t → 't kofschip X → -te; meervoud (wij) → -ten: wacht + ten = wachtten (twee t's)."),
    I("Wij hebben de hele avond voor de toets ____ (leren).", "geleerd",
      "Stam leer eindigt op r → niet in 't kofschip X → ge + leer + d. Verlengen: de geleerde woorden → d."),
    W("In <i>Hoe laat word jij morgen opgehaald?</i> is de persoonsvorm goed gespeld.", True,
      "Jij staat achter de persoonsvorm → alleen de stam: word jij (zonder t)."),
    I("Gisteren ____ (skypen) ik een uur met mijn oom in Canada.", "skypete",
      "Engels werkwoord: stam skype klinkt als 'skaip', eindigt op een p-klank → 't kofschip X → -te: skypete."),
    mc("In welke zin is het werkwoord <b>goed</b> gespeld?",
       "Het ongeluk is gisteren op de A2 gebeurd.",
       ["Wat is er met je fiets gebeurt?", "Dat gebeurd me echt nooit meer.", "Er is vandaag niets bijzonders gebeurt."],
       "Met is/zijn → voltooid deelwoord met d (verlengen: het gebeurde). Zonder hulpwerkwoord, tegenwoordige tijd enkelvoud → gebeurt: dat gebeurt me nooit meer."),
    O("In de zin <i>Van de nieuwe leerlingen kwamen sommigen al in september, de andere pas na de herfstvakantie.</i> staat één fout. Schrijf het foute woord verbeterd op en leg uit waarom.",
      ["anderen", "personen/mensen"],
      "Het foute woord is andere; dat moet anderen zijn, want het wordt zelfstandig gebruikt en verwijst naar personen.",
      "Zelfstandig gebruikt bijvoeglijk naamwoord voor personen → met n: de anderen.", minT=2),
    mc("In welke zin is het bijvoeglijk naamwoord <b>fout</b> gespeld?",
       "Ze kreeg voor haar verjaardag een mooie cadeau.",
       ["Wij wonen al jaren in een oude boerderij.", "Hij kocht van zijn spaargeld een duur horloge.", "Dit is echt een moeilijke opdracht."],
       "Cadeau is een het-woord en ervoor staat een → geen -e: een mooi cadeau. Boerderij en opdracht zijn de-woorden → wel -e."),
    I("Vul in met of zonder n: <i>Er waren deze week veel ____ (ziek) op school.</i>", "zieken",
      "Het bijvoeglijk naamwoord wordt zelfstandig gebruikt en verwijst naar personen → met n: veel zieken."),
    W("In <i>Van alle tekeningen vind ik de kleurrijke het mooist.</i> moet <i>kleurrijke</i> met een n.", False,
      "Het verwijst naar zaken (tekeningen), niet naar personen → geen n: de kleurrijke."),
    mc("Bij welk rijtje zijn de meervouden van baby, cadeau en menu allemaal goed?",
       "baby's – cadeaus – menu's",
       ["babies – cadeau's – menu's", "baby's – cadeau's – menus", "babys – cadeaus – menu's"],
       "Baby: y klinkt als ie → baby's. Cadeau eindigt op au, dat blijft goed klinken met s → cadeaus. Menu eindigt op u → menu's."),
    I("Verbeter het fout gespelde woord: <i>Volgend jaar gaan we met de klas naar Belgie en Frankrijk.</i>", "België",
      "Bel-gi-ë: zonder trema zou je 'ie' als één klank lezen. Daarom een trema op de e: België."),
    W("Het verkleinwoord van <i>pony</i> schrijf je zonder apostrof: <i>ponytje</i>.", False,
      "Bij pony klinkt de y als ie → met apostrof: pony'tje (net als baby'tje en hobby'tje)."),
    # --- Deel B · Grammatica ---
    mc("Welke samentrekking is <b>juist</b>?",
       "Noor speelt hockey en Daan voetbal.",
       ["De kat ligt op de bank en de honden in de mand.", "Ik ruim mijn kamer op en mijn broer de keuken.", "De docent geeft uitleg en de leerlingen opdrachten."],
       "Een weggelaten woord moet precies dezelfde vorm hebben: speelt = speelt. Bij ligt/liggen, ruim/ruimt en geeft/geven verschilt de vorm → onjuist."),
    O("In de zin <i>Ik heb hen gisteren mijn nieuwe fiets laten zien.</i> staat een fout verwijswoord. Schrijf het goede woord op en leg uit waarom.",
      ["hun", "meewerkend/zonder voorzetsel"],
      "Het goede woord is hun: het is een meewerkend voorwerp zonder voorzetsel (aan wie laat ik de fiets zien?).",
      "Meewerkend voorwerp zonder voorzetsel → hun; na een voorzetsel → hen (aan hen).", minT=2),
    I("Schrijf korter met een samentrekking: <i>handschoenen en handtassen</i>.", "handschoenen en -tassen|handschoenen en - tassen",
      "Het gemeenschappelijke deel (hand) staat vooraan en wordt in het tweede woord weggelaten → streepje vóór het tweede deel: handschoenen en -tassen."),
    mc("<i>Zowel kinder- als volwassenenkaartjes zijn uitverkocht.</i> Wat voor samentrekking is dit?",
       "achterwaarts, op woordniveau", ["voorwaarts, op woordniveau", "achterwaarts, op zinsniveau", "voorwaarts, op zinsniveau"],
       "Een deel van een woord (-kaartjes) is weggelaten, met streepje → woordniveau. Het gemeenschappelijke deel staat achteraan → achterwaarts."),
    W("In <i>Lotte fietst en Mees loopt naar school.</i> is 'naar school' in het eerste deel weggelaten; dat is een achterwaartse samentrekking.", True,
      "Lotte fietst [naar school] en Mees loopt naar school: het weggelaten deel komt pas later → achterwaarts."),
    mc("Kies het juiste verwijswoord: <i>Het meisje ____ ik op het feest ontmoette, zit bij mij op hockey.</i>",
       "dat", ["die", "wat", "wie"],
       "Meisje is een het-woord (het meisje) → dat. Ook al is een meisje een persoon: het lidwoord beslist."),
    mc("Kies het juiste verwijswoord: <i>De politie heeft ____ onderzoek naar de inbraak afgerond.</i>",
       "haar", ["zijn", "hun", "hem"],
       "Politie is een vrouwelijk woord (instantie, net als gemeente en regering) → bezittelijk voornaamwoord haar."),
]))


# =====================================================================================================
# Bouwen en valideren (helpers als in gen_nederlands_c7_extra.py)
# =====================================================================================================
def kaal(s):
    return re.sub(r"<[^>]+>", "", s)


def schud(v):
    opts = [v["_goed"]] + v["_fout"]
    rng.shuffle(opts)
    out = {k: x for k, x in v.items() if not k.startswith("_")}
    out["opties"] = opts
    out["antwoord"] = opts.index(v["_goed"])
    keys = ["type", "niveau", "vraag", "opties", "antwoord", "uitleg", "hint"]
    return {k: out[k] for k in keys if k in out}


def langste(v):
    L = [len(kaal(o)) for o in v["opties"]]
    return all(i == v["antwoord"] or L[i] < L[v["antwoord"]] for i in range(len(L)))


def kortste(v):
    L = [len(o) for o in v["opties"]]
    return all(i == v["antwoord"] or L[i] > L[v["antwoord"]] for i in range(len(L)))


def ok(vragen):
    m = [v for v in vragen if v["type"] == "mc"]
    if len(m) < 2:
        return True
    s = [v["antwoord"] for v in m]
    if max(s.count(i) for i in set(s)) / len(s) > 0.4:
        return False
    if len(s) < 6:
        return True
    if any(all(a == s[i - p] for i, a in enumerate(s) if i >= p) for p in (2, 3, 4)):
        return False
    n = max(len(v["opties"]) for v in m)
    if sum(1 for i in range(1, len(s)) if s[i] == (s[i - 1] + 1) % n) / (len(s) - 1) >= 0.5:
        return False
    return True


def bouw(ruw):
    for _ in range(20000):
        vragen = [schud(v) if v["type"] == "mc" else dict(v) for v in ruw]
        if ok(vragen):
            return vragen
    raise SystemExit("geen geldige optievolgorde gevonden")


def controleer_regel_19(nr, vragen):
    """Het antwoord van een invul-vraag mag niet letterlijk in een andere vraag of optie van dezelfde toets staan."""
    for idx, inv in [(i, v) for i, v in enumerate(vragen) if v["type"] == "invul"]:
        for ant in inv["antwoord"].split("|"):
            a = ant.strip().lower()
            if len(a) < 3:
                continue
            pat = re.compile(r"(?<![a-zà-ÿ])" + re.escape(a) + r"(?![a-zà-ÿ])", re.I)
            for j, andere in enumerate(vragen):
                if j != idx and any(pat.search(t) for t in [kaal(andere["vraag"])] + [kaal(o) for o in andere.get("opties", [])]):
                    raise AssertionError(f"Regel 19 in examen_{nr}: invul #{idx+1} '{ant}' staat in vraag #{j+1}")


def schrijf(pad, kop, obj, fn):
    with open(pad, "w", encoding="utf-8") as f:
        f.write(kop + "\n" + fn + "(" + json.dumps(obj, ensure_ascii=False, indent=2) + ");\n")


KOP = "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Oefenproefwerk C5 + C7) — gegenereerd door tools/gen_nederlands_oefenproefwerk.py */"


def genereer(toetsen, eerste, kop, titel, paragraaf="eind", icoon="📝"):
    """Bouwt + valideert + schrijft examen_<eerste+i>.js. Ook gebruikt door gen_nederlands_foutentraining.py."""
    _genereer(toetsen, eerste, kop, titel, paragraaf, icoon)


def _genereer(TOETSEN, EERSTE, KOP, titel, paragraaf, icoon):
    alle_vragen = set()
    for i, t in enumerate(TOETSEN):
      nr = EERSTE + i
      assert len(t["vragen"]) == 20, (nr, len(t["vragen"]))
      vragen = bouw(t["vragen"])
      controleer_regel_19(nr, vragen)
      for v in vragen:
          assert v["vraag"] not in alle_vragen, v["vraag"]
          alle_vragen.add(v["vraag"])
          assert v.get("uitleg") and len(kaal(v["uitleg"])) >= 15, v["vraag"]
          if v["type"] == "open":
              q = kaal(v["vraag"]).lower()
              for s in v["sleutelwoorden"]:
                  for w in s.split("/"):
                      assert not (len(w) > 2 and w.lower() in q), (nr, w, q)
      m = [v for v in vragen if v["type"] == "mc"]
      lang, kort = sum(langste(v) for v in m), sum(kortste(v) for v in m)
      wo = [v for v in vragen if v["type"] == "waaronwaar"]
      onw = sum(not v["antwoord"] for v in wo)
      print(f"examen_{nr}: mc {len(m)} (langste {lang}, kortste {kort}), wow {len(wo)} (onwaar {onw}), "
            f"invul {sum(v['type'] == 'invul' for v in vragen)}, open {sum(v['type'] == 'open' for v in vragen)}, "
            f"volgorde {''.join(str(v['antwoord']) for v in m)}")
      assert lang / len(m) <= 0.4, (nr, "langste", lang, len(m))
      assert kort / len(m) <= 0.4, (nr, "kortste", kort, len(m))
      assert onw / len(wo) >= 0.35, (nr, "onwaar", onw, len(wo))
      schrijf(os.path.join(ROOT, f"examen_{nr}.js"), KOP,
              {"id": f"ex-h3-nederlands-{nr}", "hoofdstuk": 7, "hoofdstukTitel": "Cursus 7 — Spelling",
               "paragraaf": paragraaf, "titel": titel.format(nr=nr, letter=t["letter"]),
               "vak": "Nederlands · HAVO 3 (Cursus 5 + 7)", "icoon": icoon, "duurMin": 20, "vragen": vragen},
             "DURU.registerExamen")


if __name__ == "__main__":
    genereer(TOETSEN, EERSTE, KOP, "Toets {nr} — Oefenproefwerk {letter}: Spelling (C7) + Grammatica (C5)")
