#!/usr/bin/env python3
"""Nederlands HAVO 3 · Gemengd A/B/C (examen_76…78.js, ex-h3-nederlands-76…78) — 2026-11-20.

Per toets (20 vragen): 8x C7 spelling (n/-e, apostrof, accent, trema) + 7x C5 (hun/hen, voor-/achterwaarts, streepje,
verwijswoorden) + 3x C1 lezen (korte tekst, structuur / absolute bewering / signaalwoord) + 2x dt (herhaling).
Afleiders = Duru's echte foute antwoorden (zwakte-analyse). Niet kopiëren uit examen_75 (nog niet gemaakt).
Draai: cd tools && python3 gen_nederlands_gemengd_20261120.py
"""
import random
import gen_nederlands_oefenproefwerk as gp
from gen_nederlands_oefenproefwerk import mc, I, W, O

gp.rng = random.Random("gemengd_2026_11_20")
EERSTE = 76
KOP = "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Gemengd C7 + C5 + C1) — gegenereerd door tools/gen_nederlands_gemengd_20261120.py */"


def _schud(v):  # als gp.schud, maar behoudt 'figuur' (leestekst)
    opts = [v["_goed"]] + v["_fout"]
    gp.rng.shuffle(opts)
    out = {k: x for k, x in v.items() if not k.startswith("_")}
    out["opties"] = opts
    out["antwoord"] = opts.index(v["_goed"])
    keys = ["type", "niveau", "figuur", "vraag", "opties", "antwoord", "uitleg", "hint"]
    return {k: out[k] for k in keys if k in out}


gp.schud = _schud


def tekst(titel, alineas):
    p = "".join(f'<p style="margin-bottom:10px;"><strong>[{i}]</strong> {a}</p>' for i, a in enumerate(alineas, 1))
    return ('<div class="leestekst-card" style="background:#f8fafc; border:1px solid #cbd5e1; border-left:4px solid #15803d; '
            'border-radius:12px; padding:16px 20px; margin-bottom:14px; font-size:14.5px; line-height:1.65; color:#1e293b;">'
            f'<div style="font-weight:800; color:#15803d; margin-bottom:10px;">📄 {titel}</div>{p}</div>')


def met_tekst(fig, vragen):
    for v in vragen:
        v["figuur"] = fig
    return vragen


TXT_A = tekst("Snoepwikkels op het schoolplein", [
    "Na elke pauze ligt het schoolplein vol snoepwikkels en lege drinkpakjes. Ook de conciërge raapt dagelijks twee volle zakken afval op. Hoe krijgen we een schoon plein?",
    "De oorzaak is simpel: er staan maar twee prullenbakken, helemaal aan de rand van het plein. Wie snel naar binnen moet, laat het afval daarom gewoon vallen.",
    "Een oplossing is meer prullenbakken midden op het plein plaatsen. Daarnaast kan elke klas een week lang de pleindienst doen, zodat leerlingen zelf zien hoeveel afval er ligt.",
    "Kortom: met meer prullenbakken en een pleindienst blijft het plein schoon.",
])
TXT_B = tekst("Een pauze zonder telefoon", [
    "Op steeds meer scholen mogen leerlingen hun telefoon niet meer gebruiken tijdens de pauze. Is dat een goed idee?",
    "Een groot voordeel is dat leerlingen elkaar weer echt aanspreken. In plaats van naar een scherm te staren, praten ze met elkaar of voetballen ze op het plein.",
    "Daar staat tegenover dat een telefoon ook handig is. Leerlingen kunnen er een rooster mee opzoeken of een ouder bellen als de les uitvalt. Bovendien voelen sommige leerlingen zich betutteld.",
    "Al met al wegen de voordelen voor de meeste scholen zwaarder dan de nadelen.",
])
TXT_C = tekst("Waarom krijg je rimpelvingers in bad?", [
    "Wie lang in bad zit, krijgt rimpelige vingers en tenen. Dat zie je bij bijna iedereen. Waarom gebeurt dat?",
    "Vroeger dachten wetenschappers dat de huid door het water opzwelt. Dat blijkt niet te kloppen: bij mensen met beschadigde zenuwen blijven de vingers glad.",
    "De huidige verklaring is dat het zenuwstelsel de bloedvaatjes in de vingertoppen samentrekt. Daardoor ontstaan rimpels, die zorgen voor meer grip op natte voorwerpen.",
    "Dankzij die rimpels pak je dus ook in de regen makkelijker iets vast.",
])

TOETSEN = []

# =====================================================================================================
# 76 · Gemengd A
# =====================================================================================================
TOETSEN.append(dict(letter="A", vragen=[
    mc("Kies de juiste combinatie: <i>Op het schoolplein stonden ____ te wachten; de ____ waren al naar binnen gegaan.</i>",
       "enkelen – overigen", ["enkele – overige", "enkelen – overige", "enkele – overigen"],
       "Beide woorden staan zelfstandig (zonder zelfstandig naamwoord erachter) en gaan over personen → allebei met n: enkelen, overigen."),
    mc("Welke zin met twee bijvoeglijke naamwoorden is goed gespeld?",
       "Ik koop een leuk boek en een mooie pen.",
       ["Ik koop een leuke boek en een mooie pen.", "Ik koop een leuk boek en een mooi pen.", "Ik koop een leuke boek en een mooi pen."],
       "Boek is een het-woord met <i>een</i> ervoor → geen -e: een leuk boek. Pen is een de-woord → wel -e: een mooie pen."),
    I("Vul in: <i>Alle ____ (aanwezig) kregen na afloop een glaasje limonade.</i>", "aanwezigen",
      "Zelfstandig gebruikt en het gaat om personen (meervoud) → met n: aanwezigen."),
    mc("Welke zin over een huis aan de gracht is goed gespeld?",
       "Ze woont in het kleine huis aan de gracht.",
       ["Ze woont in het klein huis aan de gracht.", "Ze woont in een kleine huis aan de gracht.", "Ze woont in de klein huis aan de gracht."],
       "Na <i>het</i> krijgt het bijvoeglijk naamwoord altijd -e: het kleine huis. Zonder -e kan het alleen na <i>een</i> bij een het-woord: een klein huis."),
    mc("Welke rij met foto en menu in het meervoud is goed gespeld?",
       "foto's – menu's", ["fotos – menu's", "foto's – menus", "fotos – menus"],
       "Na een klinker die lang klinkt maar enkel geschreven wordt (o, u) krijg je een apostrof in het meervoud: foto's, menu's."),
    I("Verbeter het fout gespelde woord: <i>Voor het toetje maakt mijn moeder een creme met vers fruit.</i>", "crème",
      "Crème spreek je uit met een open è-klank (zoals in 'pet') → accent grave: crème."),
    O("In de zin <i>De wandelroute is door de gemeente al twee keer verlengt.</i> staat één spelfout. Schrijf het foute woord verbeterd op en noem de regel.",
      ["verlengd", "voltooid"],
      "Het foute woord is verlengt; het moet verlengd zijn. Het is een voltooid deelwoord: verleng + d (de verlengde route).",
      "Voltooid deelwoord: verleng het woord (de verlengde route) en je hoort een d. Daarom: verlengd.", minT=2),
    mc("Welk woord voor een oud, vervallen gebouw is goed gespeld?",
       "ruïne", ["ruine", "ruiïne", "ruïnne"],
       "Zonder trema lees je de <i>ui</i> als één klank (zoals in 'huis'). Het trema op de i laat zien dat u en i apart klinken: ru-ï-ne."),
    I("Mijn oom ____ (verhuizen) volgende maand naar Gent.", "verhuist",
      "Onderwerp is <i>mijn oom</i> (hij) → stam + t: verhuis + t = verhuist."),
    W("In de zin <i>De jongste mochten als eerste kiezen.</i> is de spelling juist.", False,
      "Het gaat om meerdere personen en het woord staat zelfstandig → met n: de jongsten mochten als eerste kiezen."),
    # --- C1 lezen ---
    *met_tekst(TXT_A, [
        mc("Tekst A gaat over snoepwikkels op het schoolplein. Welke tekststructuur geeft de opbouw het best weer?",
           "probleem-oplossing", ["voor- en nadelen", "verschijnsel-verklaring", "historische structuur"],
           "Alinea 1-2 beschrijven het probleem (afval) en de oorzaak, alinea 3 geeft de oplossing → probleem-oplossing."),
        W("Volgens alinea 2 staat er geen enkele prullenbak op het schoolplein.", False,
          "Let op extreme woorden als <i>geen enkele</i>: er staan wel twee prullenbakken, alleen aan de rand van het plein."),
        mc("Welk signaalwoord leidt de samenvatting in alinea 4 in?",
           "Kortom", ["Bovendien", "Daarnaast", "Bijvoorbeeld"],
           "<i>Kortom</i> kondigt een samenvatting of conclusie aan; <i>daarnaast</i> en <i>bovendien</i> voegen iets toe."),
    ]),
    # --- C5 ---
    mc("Kies de juiste combinatie: <i>De boer ____ de koeien melkt en het paard ____ in de wei staat, horen bij dezelfde hoeve.</i>",
       "die – dat", ["dat – die", "die – die", "dat – dat"],
       "De boer is een de-woord → die. Het paard is een het-woord → dat."),
    mc("Kies de juiste combinatie: <i>De Belgische regering presenteert ____ plannen, terwijl België trots is op ____ chocolade.</i>",
       "haar – zijn", ["zijn – haar", "haar – haar", "zijn – zijn"],
       "Een regering is een instantie (vrouwelijk) → haar. De naam van een land is een het-woord → zijn."),
    mc("Welke zin over bedanken voor hulp is helemaal goed?",
       "Ik wil hen graag bedanken voor hun hulp.",
       ["Ik wil hun graag bedanken voor hen hulp.", "Ik wil hun graag bedanken voor hun hulp.", "Ik wil hen graag bedanken voor hen hulp."],
       "Wie wil ik bedanken? Hen (lijdend voorwerp). Hun hulp: bezittelijk voornaamwoord → hun."),
    W("In <i>Mijn ouders vinden dat ik hun vaker moet bellen.</i> is hun goed gebruikt.", False,
      "Wie moet ik bellen? Hen: lijdend voorwerp → hen. Hun is alleen goed bij een meewerkend voorwerp zonder voorzetsel of als bezittelijk voornaamwoord."),
    mc("<i>Anna eet een appel en Tim een peer.</i> Welke omschrijving klopt?",
       "voorwaarts: 'eet' staat in het eerste deel",
       ["achterwaarts: 'eet' staat in het eerste deel", "voorwaarts: 'eet' staat in het tweede deel", "achterwaarts: 'eet' staat in het tweede deel"],
       "Het woord <i>eet</i> staat vooraan, in het eerste deel, en wordt in het tweede deel weggelaten → voorwaarts."),
    W("<i>Kleding- en schoenwinkels</i> is een achterwaartse samentrekking.", True,
      "Het gemeenschappelijke deel <i>winkels</i> staat achteraan en wordt in het eerste woord weggelaten → achterwaarts, met streepje."),
    mc("Je schrijft over schoeisel in een lijstje. Welke woordgroep met laarzen is goed geschreven?",
       "bruine en zwarte laarzen", ["bruine- en zwarte laarzen", "bruine en- zwarte laarzen", "bruin- en zwarte laarzen"],
       "Er valt geen deel van een woord weg (het zijn losse bijvoeglijke naamwoorden) → geen streepje."),
]))

# =====================================================================================================
# 77 · Gemengd B
# =====================================================================================================
TOETSEN.append(dict(letter="B", vragen=[
    mc("Kies de juiste combinatie: <i>Op de open dag kwamen ____ een kijkje nemen, maar ____ schreven zich in.</i>",
       "velen – weinigen", ["velen – weinige", "vele – weinigen", "vele – weinige"],
       "Beide woorden staan zelfstandig en gaan over personen → met n: velen, weinigen."),
    mc("Welke zin over een schrift en een tafel is goed gespeld?",
       "Het nieuwe schrift ligt op de grote tafel.",
       ["Het nieuw schrift ligt op de grote tafel.", "Het nieuwe schrift ligt op de groot tafel.", "Het nieuwe schrift ligt op het grote tafel."],
       "Na <i>het</i> en <i>de</i> krijgt het bijvoeglijk naamwoord -e: het nieuwe schrift, de grote tafel. Let wel: tafel is een de-woord, dus niet <i>het</i>."),
    I("Vul in: <i>De sterken helpen de ____ (zwak) bij het oversteken.</i>", "zwakken",
      "Zelfstandig gebruikt en het gaat om personen → met n: zwakken."),
    mc("Welke combinatie is goed? <i>Op tafel stonden een ____ kandelaar en een ____ vaas.</i>",
       "zilveren – glazen", ["zilvere – glazene", "zilveren – glaze", "zilver – glas"],
       "Stoffelijke bijvoeglijke naamwoorden (gemaakt van zilver, glas) eindigen op -en: zilveren, glazen."),
    mc("Welke rij met radio en cadeau is goed gespeld?",
       "radio's – cadeautje", ["radios – cadeautje", "radio's – cadeau'tje", "radios – cadeau'tje"],
       "Radio: de o klinkt lang maar is enkel geschreven → radio's. Cadeau eindigt op een geschreven tweeklank (au) → geen apostrof: cadeautje."),
    I("Verbeter het fout gespelde woord: <i>Het publiek bleef staan voor de laatste scene van het toneelstuk.</i>", "scène",
      "Scène klinkt met een open è-klank (zoals in 'pet') → accent grave: scène."),
    O("In de zin <i>Het oude schoolgebouw wordt volgend jaar helemaal verbouwt.</i> staat één spelfout. Schrijf het foute woord verbeterd op en noem de regel.",
      ["verbouwd", "voltooid"],
      "Het foute woord is verbouwt; het moet verbouwd zijn. Het is een voltooid deelwoord: verbouw + d (het verbouwde gebouw).",
      "Voltooid deelwoord: verleng het woord (het verbouwde gebouw) en je hoort een d. Daarom: verbouwd.", minT=2),
    mc("Welk woord voor 'belangstelling hebben' is goed gespeld?",
       "geïnteresseerd", ["geinteresseerd", "geínteresseerd", "ge-interesseerd"],
       "Zonder trema lees je <i>ei</i> als één klank. De ï laat zien dat de i apart klinkt: ge-ï-nteresseerd."),
    I("Mijn zus ____ (verwachten) morgen een pakketje.", "verwacht",
      "Onderwerp is <i>mijn zus</i> (zij) → stam + t. De stam verwacht eindigt al op een t, dus er komt er geen tweede bij."),
    W("In de zin <i>De oudste hielpen de jongste met de opdracht.</i> is de spelling juist.", False,
      "Het gaat om meerdere personen, zelfstandig gebruikt → met n: de oudsten hielpen de jongsten."),
    *met_tekst(TXT_B, [
        mc("Hoe is Tekst B (pauze zonder telefoon) opgebouwd?",
           "voor- en nadelen", ["probleem-oplossing", "historische structuur", "verschijnsel-verklaring"],
           "De tekst zet voordelen (alinea 2) tegenover nadelen (alinea 3) en weegt ze af in alinea 4 → voor- en nadelen."),
        W("Volgens alinea 3 is een telefoon op school altijd nutteloos.", False,
          "Let op <i>altijd</i>. Alinea 3 zegt juist dat een telefoon handig is, bijvoorbeeld om een rooster op te zoeken."),
        mc("Welke woorden in alinea 3 laten zien dat nu de nadelen beginnen?",
           "Daar staat tegenover", ["Een groot voordeel", "In plaats van", "Al met al"],
           "<i>Daar staat tegenover</i> zet iets tegenover het voorgaande (de voordelen). <i>Al met al</i> staat pas in de slotalinea."),
    ]),
    mc("Kies het juiste verwijswoord: <i>Alles ____ je op het bord ziet, moet je overschrijven.</i>",
       "wat", ["dat", "die", "wie"],
       "Na alles, niets, iets en veel gebruik je <i>wat</i>: alles wat je ziet."),
    mc("Kies de juiste combinatie: <i>De directie legt ____ besluit uit, en Londen is beroemd om ____ grote klok.</i>",
       "haar – zijn", ["zijn – haar", "haar – haar", "zijn – zijn"],
       "De directie is een instantie → haar. Londen is een stad (het-woord) → zijn."),
    mc("Kies de juiste combinatie: <i>Ik zag mijn buren bij de bushalte en vroeg ____ de weg; daarna liep ik met ____ mee.</i>",
       "hun – hen", ["hen – hun", "hun – hun", "hen – hen"],
       "Ik vroeg hun de weg: meewerkend voorwerp zonder voorzetsel → hun. Met hen: na een voorzetsel → hen."),
    W("In <i>De ouders zijn blij dat hun kinderen zo goed meedoen.</i> is hun goed gebruikt.", True,
      "Hun staat hier voor <i>kinderen</i> als bezittelijk voornaamwoord: hun kinderen."),
    mc("<i>Zowel dames- als herenkleding is afgeprijsd.</i> Welke omschrijving klopt?",
       "achterwaarts: 'kleding' staat achteraan",
       ["voorwaarts: 'kleding' staat achteraan", "achterwaarts: 'dames' staat vooraan", "voorwaarts: 'heren' staat vooraan"],
       "Het gemeenschappelijke deel <i>kleding</i> staat achteraan en wordt in het eerste woord weggelaten → achterwaarts."),
    W("<i>Papa bakt een taart en mama een cake.</i> is een achterwaartse samentrekking, want <i>bakt</i> wordt later weggelaten.", False,
      "Het woord staat vooraan en wordt later weggelaten → voorwaarts. Achterwaarts is het omgekeerde: het woord staat achteraan."),
    mc("Je beschrijft een huis in een lijstje. Welke woordgroep met deuren is goed geschreven?",
       "voor- en achterdeur", ["voor en achterdeur", "voor-en achterdeur", "voor- en -achterdeur"],
       "Voor[deur] en achterdeur: een deel van een samenstelling valt weg → streepje direct achter het eerste deel, met een spatie erna."),
]))

# =====================================================================================================
# 78 · Gemengd C
# =====================================================================================================
TOETSEN.append(dict(letter="C", vragen=[
    mc("Kies de juiste combinatie: <i>Van de klas deden ____ mee aan het toernooi en ____ keken toe.</i>",
       "sommigen – anderen", ["sommige – andere", "sommigen – andere", "sommige – anderen"],
       "Beide woorden staan zelfstandig en gaan over personen → met n: sommigen, anderen."),
    mc("Kies de juiste combinatie: <i>Ik woon in een ____ appartement met een ____ balkon.</i>",
       "gezellig – groot", ["gezellige – grote", "gezellig – grote", "gezellige – groot"],
       "Appartement en balkon zijn allebei het-woorden met <i>een</i> ervoor → geen -e: een gezellig appartement, een groot balkon."),
    I("Vul in: <i>Op de vergadering waren ____ (veel) het niet eens met het voorstel.</i>", "velen",
      "Zelfstandig gebruikt en het gaat om personen → met n: velen."),
    mc("Welke zin over een jasje en een kapstok is goed gespeld?",
       "Het leren jasje hangt aan de oude kapstok.",
       ["Het lere jasje hangt aan de oude kapstok.", "Het leren jasje hangt aan de oud kapstok.", "Het leren jasje hangt aan het oude kapstok."],
       "Stoffelijk bijvoeglijk naamwoord (van leer) → leren. Kapstok is een de-woord → de oude kapstok."),
    mc("Welke zin over baby's en een pony is goed gespeld?",
       "Ik zag twee baby's en een pony'tje bij de boerderij.",
       ["Ik zag twee babies en een pony'tje bij de boerderij.", "Ik zag twee baby's en een ponytje bij de boerderij.", "Ik zag twee babies en een ponytje bij de boerderij."],
       "Bij baby en pony klinkt de y als ie → meervoud baby's en verkleinwoord pony'tje, beide met apostrof."),
    I("Verbeter het fout gespelde woord: <i>Wij zaten urenlang in een knus cafe op de hoek.</i>", "café",
      "Café wordt uitgesproken met een gesloten é-klank (zoals in 'twee') → accent aigu: café."),
    O("In de zin <i>De winkel is gisteren gesloten omdat de eigenaar was verhuist.</i> staat één spelfout. Schrijf het foute woord verbeterd op en noem de regel.",
      ["verhuisd", "voltooid"],
      "Het foute woord is verhuist; het moet verhuisd zijn. Het is een voltooid deelwoord: verhuis + d (de verhuisde eigenaar).",
      "Voltooid deelwoord: verleng het woord (de verhuisde eigenaar) en je hoort een d. Daarom: verhuisd.", minT=2),
    mc("Welk woord voor 'goedgelovig' is goed gespeld?",
       "naïef", ["naief", "naíef", "naïëf"],
       "Zonder trema lees je <i>aie</i>/<i>ei</i> als één klank. De ï laat zien dat de i apart klinkt: na-ïef."),
    I("____ (vinden) jij die film ook zo spannend?", "vind",
      "Jij staat achter de persoonsvorm → alleen de stam: vind. De d van de stam blijft altijd staan."),
    W("In de zin <i>De meesten vonden het een leuke avond.</i> is de spelling juist.", True,
      "Meesten staat zelfstandig en gaat over personen (meervoud) → met n."),
    *met_tekst(TXT_C, [
        mc("Welke vaste structuur zit er achter Tekst C over rimpelvingers?",
           "verschijnsel-verklaring", ["probleem-oplossing", "voor- en nadelen", "historische structuur"],
           "Alinea 1 beschrijft een verschijnsel (rimpelvingers), de rest geeft verklaringen → verschijnsel-verklaring."),
        W("Volgens alinea 2 zwellen de vingers bij iedereen op door het water, zonder uitzondering.", False,
          "Let op <i>iedereen</i> en <i>zonder uitzondering</i>. Alinea 2 noemt juist een uitzondering: bij beschadigde zenuwen blijven de vingers glad."),
        mc("Welk voordeel hebben de rimpels volgens alinea 3?",
           "Je hebt meer grip op natte voorwerpen", ["Je vingers worden beter doorbloed", "De huid zwelt minder op", "Je zenuwen worden beschermd"],
           "Alinea 3: de rimpels zorgen voor meer grip op natte voorwerpen."),
    ]),
    mc("Kies het juiste verwijswoord: <i>Niets ____ ik probeerde, hielp tegen de hoofdpijn.</i>",
       "wat", ["dat", "die", "wie"],
       "Na niets, alles, iets en veel gebruik je <i>wat</i>: niets wat ik probeerde."),
    mc("Welke zin over de brandweer en Utrecht is goed?",
       "De brandweer wil haar kazerne verbouwen en Utrecht wil zijn centrum autovrij maken.",
       ["De brandweer wil zijn kazerne verbouwen en Utrecht wil haar centrum autovrij maken.", "De brandweer wil haar kazerne verbouwen en Utrecht wil haar centrum autovrij maken.", "De brandweer wil zijn kazerne verbouwen en Utrecht wil zijn centrum autovrij maken."],
       "Instanties zoals de brandweer zijn vrouwelijk → haar. Een stad is een het-woord → zijn."),
    mc("Kies de juiste vorm: <i>Ik heb mijn nichtjes lang niet gezien. Ik ga ____ morgen bellen.</i>",
       "hen", ["hun", "zij", "hunne"],
       "Wie ga ik bellen? Hen: lijdend voorwerp → hen. Hun gebruik je bij een meewerkend voorwerp zonder voorzetsel."),
    W("In <i>Wij schreven hen een kaartje.</i> is hen goed gebruikt.", False,
      "Aan wie schreven wij een kaartje? Meewerkend voorwerp zonder voorzetsel → hun: wij schreven hun een kaartje."),
    mc("In welke van deze vier zinnen zie je een samentrekking waarbij het woord <b>vooraan</b> blijft staan?",
       "Fenna maakt de soep en Jesse de salade.",
       ["Fenna maakt en Jesse bakt de soep.", "Zowel rood- als wittekool staat op het menu.", "Fenna maakt de soep, Jesse maakt de salade."],
       "Bij voorwaarts staat het weggelaten woord (maakt) vooraan en valt het later weg. De tweede zin is achterwaarts, de derde is geen samentrekking."),
    W("<i>Boekenkasten en -planken</i> is een achterwaartse samentrekking.", False,
      "Het gemeenschappelijke deel <i>boeken</i> staat vooraan en valt later weg → voorwaarts."),
    mc("Je beschrijft een linkshandige gitarist. Welke woordgroep met handen is goed geschreven?",
       "linker- en rechterhand", ["linker en rechterhand", "linker-en rechterhand", "linker en- rechterhand"],
       "Linker[hand] en rechterhand: een deel van een samenstelling valt weg → streepje direct achter het eerste deel."),
]))

if __name__ == "__main__":
    gp.genereer(TOETSEN, EERSTE, KOP, "Toets {nr} — Gemengd: spelling, grammatica en lezen ({letter})",
                paragraaf="mix", icoon="🔀")
