"""Duits H1 (Umgebung & Wetter): 10 herhalingstoetsen ex-h3-duits-63…72.
Woorden en grammatica uit de eerdere H1-toetsen (Lernliste p. 48–49, Sprachmittel, Grammatik p. 50).
Gebruik: python3 tools/gen_duits_h1_herhaling.py havo3/duits/js/data <bestaande-vragen.json>
⚠️ Niet opnieuw draaien op gepubliceerde ids: de inhoud van een gemaakte toets mag niet veranderen."""
import json, random, sys

OUT = sys.argv[1]
def norm(t): return " ".join(t.lower().split())
GEZIEN = {norm(t) for t in json.load(open(sys.argv[2]))}

# ---------- woordenbank (alleen woorden uit eerdere H1-toetsen) ----------
# (lidwoord, woord, meervoud of None, Nederlands)
ZN = [
    ("der", "Berg", "Berge", "de berg"), ("der", "Fluss", "Flüsse", "de rivier"), ("der", "See", "Seen", "het meer"),
    ("das", "Meer", "Meere", "de zee"), ("die", "Insel", "Inseln", "het eiland"), ("der", "Strand", "Strände", "het strand"),
    ("der", "Wald", "Wälder", "het bos"), ("das", "Dorf", "Dörfer", "het dorp"), ("die", "Stadt", "Städte", "de stad"),
    ("der", "Ort", "Orte", "de plaats"), ("die", "Gegend", "Gegenden", "de streek"), ("die", "Umgebung", None, "de omgeving"),
    ("die", "Natur", None, "de natuur"), ("das", "Land", "Länder", "het land"), ("der", "Himmel", None, "de lucht"),
    ("die", "Wolke", "Wolken", "de wolk"), ("die", "Sonne", None, "de zon"), ("der", "Wind", None, "de wind"),
    ("der", "Regen", None, "de regen"), ("der", "Schnee", None, "de sneeuw"), ("das", "Gewitter", "Gewitter", "het onweer"),
    ("das", "Wetter", None, "het weer"), ("der", "Verkehr", None, "het verkeer"), ("der", "Fels", "Felsen", "de rots"),
    ("die", "Decke", "Decken", "het plafond"), ("der", "Ausblick", "Ausblicke", "het uitzicht"), ("der", "Schutz", None, "de bescherming"),
    ("die", "Nahrung", None, "de voeding"), ("die", "Auswirkung", "Auswirkungen", "het effect"), ("die", "Begeisterung", None, "het enthousiasme"),
    ("der", "Klimawandel", None, "de klimaatverandering"), ("der", "Naturschutz", None, "de natuurbescherming"),
    ("der", "Anzug", "Anzüge", "het pak"), ("der", "Wasserfall", "Wasserfälle", "de waterval"),
]
WW = [("wandern", "wandelen"), ("zelten", "kamperen"), ("grillen", "barbecueën"), ("klettern", "klimmen"),
      ("beobachten", "observeren"), ("zerstören", "verwoesten"), ("erfahren", "te weten komen"), ("gestalten", "vormgeven"),
      ("sehen", "zien"), ("achten auf", "letten op"), ("sich auskennen", "bekend zijn met"), ("sich beschäftigen mit", "zich bezighouden met")]
BN = [("ruhig", "rustig"), ("hektisch", "druk"), ("glatt", "glad"), ("eng", "nauw"), ("stolz", "trots"),
      ("zuverlässig", "betrouwbaar"), ("langweilig", "saai"), ("hügelig", "heuvelachtig"), ("heiß", "heet"), ("kalt", "koud"),
      ("windig", "winderig"), ("oft", "vaak"), ("immer", "altijd"), ("insgesamt", "in totaal"), ("unbedingt", "per se"),
      ("also", "dus"), ("gespannt", "benieuwd"), ("abends", "'s avonds"), ("gleich", "zo meteen")]
WEER = [("es regnet", "het regent"), ("es schneit", "het sneeuwt"), ("es friert", "het vriest"), ("es hagelt", "het hagelt"),
        ("die Sonne scheint", "de zon schijnt"), ("es ist windig", "het waait"), ("es ist heiß", "het is heet"), ("es ist glatt", "het is glad")]
MAAND = [("Januar", "januari", "Winter"), ("Februar", "februari", "Winter"), ("März", "maart", "Frühling"), ("April", "april", "Frühling"),
         ("Mai", "mei", "Frühling"), ("Juni", "juni", "Sommer"), ("Juli", "juli", "Sommer"), ("August", "augustus", "Sommer"),
         ("September", "september", "Herbst"), ("Oktober", "oktober", "Herbst"), ("November", "november", "Herbst"), ("Dezember", "december", "Winter")]
SEIZ = {"Frühling": "de lente", "Sommer": "de zomer", "Herbst": "de herfst", "Winter": "de winter"}
RICHT = [("im Norden", "in het noorden"), ("im Süden", "in het zuiden"), ("im Osten", "in het oosten"), ("im Westen", "in het westen")]
TEGEN = {"im Norden": "im Süden", "im Süden": "im Norden", "im Osten": "im Westen", "im Westen": "im Osten"}
VERGR = [("warm", "wärmer", "warmer"), ("kalt", "kälter", "kouder"), ("gut", "besser", "beter"), ("viel", "mehr", "meer"),
         ("heiß", "heißer", "heter"), ("ruhig", "ruhiger", "rustiger"), ("schön", "schöner", "mooier"), ("langweilig", "langweiliger", "saaier")]
VERGR_ZIN = {"warm": ["Im Juli ist es ____ als im Mai.", "Im Süden ist es ____ als im Norden.", "Heute ist es ____ als gestern."],
             "kalt": ["Im Januar ist es ____ als im Oktober.", "In den Bergen ist es ____ als am Strand.", "Im Norden ist es ____ als im Süden."],
             "gut": ["Heute ist das Wetter ____ als gestern.", "Morgen wird das Wetter ____ als heute.", "Der Ausblick ist hier ____ als dort."],
             "viel": ["Im Herbst regnet es ____ als im Sommer.", "Im Gebirge schneit es ____ als im Dorf.", "In der Stadt gibt es ____ Verkehr als im Dorf."],
             "heiß": ["Im August ist es ____ als im Juni.", "Am Strand ist es ____ als im Wald.", "Im Süden ist es im Sommer ____ als im Norden."],
             "ruhig": ["Das Dorf ist ____ als die Stadt.", "Der See ist heute ____ als das Meer.", "Im Wald ist es ____ als in der Stadt."],
             "schön": ["Der Ausblick vom Berg ist ____ als vom Turm.", "Das Wetter im Mai ist ____ als im März.", "Die Insel ist ____ als die Stadt."],
             "langweilig": ["Dieser Film ist ____ als der andere.", "Der Regentag war ____ als der Sonnentag.", "Die Stadt ist im Winter ____ als im Sommer."]}
VERGR_FOUT = {"wärmer": ["warmer", "mehr warm", "am wärmer"], "kälter": ["kalter", "mehr kalt", "kältest"], "besser": ["guter", "güter", "mehr gut"],
              "mehr": ["vieler", "mehrer", "viel mehr als"], "heißer": ["heiser", "mehr heiß", "heißest"], "ruhiger": ["mehr ruhig", "rühiger", "ruhigst"],
              "schöner": ["schoner", "mehr schön", "schönst"], "langweiliger": ["mehr langweilig", "langweilger", "langweiligst"]}

# ---------- vervoeging ----------
PERS = ["ich", "du", "er", "wir", "ihr", "sie"]
VORM = {"sein": dict(zip(PERS, ["war", "warst", "war", "waren", "wart", "waren"])),
        "haben": dict(zip(PERS, ["hatte", "hattest", "hatte", "hatten", "hattet", "hatten"])),
        "werden": dict(zip(PERS, ["werde", "wirst", "wird", "werden", "werdet", "werden"]))}
ONDW = [("Ich", "ich", "ik"), ("Du", "du", "jij"), ("Lisa", "er", "Lisa"), ("Tom", "er", "Tom"), ("Wir", "wir", "wij"),
        ("Ihr", "ihr", "jullie"), ("Die Kinder", "sie", "de kinderen"), ("Meine Eltern", "sie", "mijn ouders"), ("Man", "er", "men")]
ZIN = {
    "sein": ["____ gestern im Wald.", "____ letzte Woche am See.", "____ im Sommer auf einer Insel.", "____ am Wochenende in den Bergen.",
             "____ heute Morgen am Strand.", "____ im Herbst in einem kleinen Dorf.", "____ gestern Abend sehr müde.", "____ im Juli im Süden."],
    "haben": ["____ gestern viel Spaß im Schnee.", "____ letzten Sommer einen tollen Ausblick.", "____ im Urlaub schönes Wetter.",
              "____ beim Wandern keine Jacke dabei.", "____ am See ein kleines Zelt.", "____ im Winter oft kalte Füße.", "____ gestern keine Zeit."],
    "werden": ["____ beim Klettern schnell müde.", "____ im Winter oft krank.", "____ bei Gewitter immer nervös.", "____ in der Sonne schnell rot.",
               "____ in der Stadt schnell hektisch."],
}
UITLEG_TABEL = {"sein": "sein (verleden tijd): ich war, du warst, er war, wir waren, ihr wart, sie waren",
                "haben": "haben (verleden tijd): ich hatte, du hattest, er hatte, wir hatten, ihr hattet, sie hatten",
                "werden": "werden (tegenwoordige tijd): ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden"}

def k(rng, l): return l[rng.randrange(len(l))]
def lu(u): return u if len(u) >= 30 else "Lernliste H1: " + u

def MC(v, goed, fout, u):
    opts = [goed] + [f for f in dict.fromkeys(fout) if f != goed]
    assert len(opts) >= 4, (v, opts)
    return {"type": "mc", "vraag": v, "_opts": opts[:4], "uitleg": lu(u)}
def WO(v, w, u): return {"type": "waaronwaar", "vraag": v, "antwoord": w, "uitleg": ("Waar. " if w else "Onwaar. ") + u}
def IN(v, a, u): return {"type": "invul", "vraag": v, "antwoord": a, "uitleg": lu(u)}
def OP(v, m, s, n, u): return {"type": "open", "vraag": v, "modelantwoord": m, "sleutelwoorden": s, "minTreffers": n, "uitleg": u}
def alt(w): return "|".join(dict.fromkeys([w, w.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")]))

# ---------- vraagtypen ----------
def zn_de_nl(rng):
    a, w, _, nl = k(rng, ZN); fout = [z[3] for z in rng.sample(ZN, 6) if z[3] != nl]
    zin = k(rng, ["Wat betekent '{}'?", "Welke vertaling hoort bij '{}'?", "Vertaal '{}' naar het Nederlands. Kies het juiste antwoord."])
    return MC(zin.format(f"{a} {w}"), nl, fout, f"{a} {w} = {nl}.")

def zn_nl_de(rng):
    a, w, _, nl = k(rng, ZN); andere = [x for x in ["der", "die", "das"] if x != a]
    fout = [f"{andere[0]} {w}", f"{andere[1]} {w}"] + [f"{z[0]} {z[1]}" for z in rng.sample(ZN, 3) if z[1] != w]
    zin = k(rng, ["Hoe zeg je '{}' in het Duits (met het juiste lidwoord)?", "Wat is '{}' in het Duits? Let op het lidwoord.", "Kies de goede Duitse vertaling van '{}'."])
    return MC(zin.format(nl), f"{a} {w}", fout, f"{nl} = {a} {w}. Leer het lidwoord altijd mee.")

def zn_invul_de(rng):
    a, w, _, nl = k(rng, ZN)
    zin = k(rng, ["Vertaal naar het Duits (met lidwoord): '{}'.", "Schrijf het Duitse woord met lidwoord voor '{}'.", "Hoe heet '{}' in het Duits? Schrijf ook het lidwoord."])
    return IN(zin.format(nl), alt(f"{a} {w}") + "|" + alt(w), f"{nl} = {a} {w}.")

def zn_invul_nl(rng):
    a, w, _, nl = k(rng, ZN); kaal = nl.split(" ", 1)[1]
    zin = k(rng, ["Vertaal naar het Nederlands: '{}'.", "Wat betekent '{}' in het Nederlands?", "Schrijf de Nederlandse vertaling van '{}'."])
    return IN(zin.format(f"{a} {w}"), f"{nl}|{kaal}", f"{a} {w} = {nl}.")

def lidwoord(rng):
    a, w, _, nl = k(rng, ZN)
    zin = k(rng, ["Welk lidwoord hoort bij '{}' ({})?", "Kies het lidwoord: '____ {}' ({}).", "Is het der, die of das: '{}' ({})?"])
    return MC(zin.format(w, nl), a, [x for x in ["der", "die", "das", "den"] if x != a],
              f"Het is {a} {w}." + (" Woorden op -ung zijn altijd 'die'." if w.endswith("ung") else ""))

def lidwoord_invul(rng):
    a, w, _, nl = k(rng, ZN)
    return IN(k(rng, ["Vul het lidwoord in (der, die of das): '____ {}' ({}).", "Welk lidwoord (der/die/das) hoort bij {} ({})?"]).format(w, nl), a, f"{a} {w} = {nl}.")

def lidwoord_wo(rng, waar):
    a, w, _, nl = k(rng, ZN); g = a if waar else k(rng, [x for x in ["der", "die", "das"] if x != a])
    return WO(f"Het Duitse woord voor '{nl}' is '{g} {w}'.", waar, f"Het is {a} {w}.")

def meervoud(rng):
    a, w, mv, nl = k(rng, [z for z in ZN if z[2] and z[2] != z[1]])
    fout = {w + "en", w + "s", w + "e", mv.replace("ä", "a").replace("ö", "o").replace("ü", "u"), mv + "n", w + "er"}
    return MC(k(rng, ["Wat is het meervoud van '{} {}'?", "Kies het juiste meervoud: '{} {}' → die …"]).format(a, w), f"die {mv}",
              [f"die {f}" for f in fout if f != mv], f"{a} {w} – die {mv} ({nl}).")

def meervoud_invul(rng):
    a, w, mv, nl = k(rng, [z for z in ZN if z[2] and z[2] != z[1]])
    return IN(k(rng, ["Schrijf het meervoud van '{} {}' (met of zonder lidwoord).", "Meervoud: {} {} – die ____"]).format(a, w), alt(f"die {mv}") + "|" + alt(mv), f"{a} {w} – die {mv}.")

def meervoud_wo(rng, waar):
    a, w, mv, nl = k(rng, [z for z in ZN if z[2] and z[2] != z[1]])
    g = mv if waar else k(rng, [x for x in [w + "en", w + "s", mv.replace("ä", "a").replace("ö", "o").replace("ü", "u")] if x != mv])
    return WO(f"Het meervoud van '{a} {w}' is 'die {g}'.", waar, f"{a} {w} – die {mv}.")

def ww_de_nl(rng):
    de, nl = k(rng, WW + BN); fout = [x[1] for x in rng.sample(WW + BN, 6) if x[1] != nl]
    return MC(k(rng, ["Wat betekent '{}'?", "Welke Nederlandse vertaling past bij '{}'?"]).format(de), nl, fout, f"{de} = {nl}.")

def ww_nl_de(rng):
    de, nl = k(rng, WW + BN); fout = [x[0] for x in rng.sample(WW + BN, 6) if x[0] != de]
    return MC(k(rng, ["Hoe zeg je '{}' in het Duits?", "Welk Duits woord betekent '{}'?"]).format(nl), de, fout, f"{nl} = {de}.")

def ww_invul(rng):
    de, nl = k(rng, WW + BN)
    if rng.random() < 0.5:
        return IN(k(rng, ["Vertaal naar het Duits: '{}'.", "Schrijf het Duitse woord voor '{}'."]).format(nl), alt(de), f"{nl} = {de}.")
    return IN(k(rng, ["Vertaal naar het Nederlands: '{}'.", "Wat betekent '{}'? Schrijf de Nederlandse vertaling."]).format(de), nl, f"{de} = {nl}.")

def betekenis_wo(rng, waar):
    de, nl = k(rng, WW + BN + [(f"{z[0]} {z[1]}", z[3]) for z in ZN])
    g = nl if waar else k(rng, [x[1] for x in WW + BN if x[1] != nl])
    return WO(f"'{de[0].upper() + de[1:]}' betekent '{g}'.", waar, f"{de} = {nl}.")

def vervoeg(rng, ww=None, invul=False):
    ww = ww or k(rng, ["sein", "haben", "werden"])
    S, p, _ = k(rng, ONDW); zin = f"{S} {k(rng, ZIN[ww])}"; goed = VORM[ww][p]
    tijd = "verleden tijd" if ww != "werden" else "tegenwoordige tijd"
    if invul:
        return IN(f"Vul de juiste vorm van {ww} ({tijd}) in: '{zin}'", goed, f"{UITLEG_TABEL[ww]}. Bij '{S}' hoort '{goed}'.")
    fout = [f for f in dict.fromkeys(VORM[ww].values()) if f != goed]
    rng.shuffle(fout)
    return MC(f"Kies de juiste vorm van {ww} ({tijd}): '{zin}'", goed, fout, f"{UITLEG_TABEL[ww]}. Bij '{S}' hoort '{goed}'.")

def sein_of_haben(rng, invul=False):
    ww = k(rng, ["sein", "haben"]); S, p, _ = k(rng, ONDW); zin = f"{S} {k(rng, ZIN[ww])}"; goed = VORM[ww][p]
    ander = "haben" if ww == "sein" else "sein"
    reden = "ergens zijn of een toestand (müde) → sein" if ww == "sein" else "iets hebben (Spaß, Wetter, Zeit, Zelt …) → haben"
    if invul:
        return IN(f"Vul in (sein of haben, verleden tijd): '{zin}'", goed, f"{reden}. Bij '{S}': {goed}.")
    return MC(f"sein of haben? Kies de juiste vorm in de verleden tijd: '{zin}'", goed,
              [VORM[ander][p]] + [f for f in VORM[ww].values() if f != goed][:1] + [VORM[ander][q] for q in PERS if VORM[ander][q] != VORM[ander][p]][:2],
              f"{reden}. Bij '{S}': {goed}.")

def vervoeg_wo(rng, waar):
    ww = k(rng, ["sein", "haben", "werden"]); S, p, _ = k(rng, ONDW); goed = VORM[ww][p]
    g = goed if waar else k(rng, [f for f in VORM[ww].values() if f != goed])
    zin = f"{S} {k(rng, ZIN[ww])}".replace("____", g)
    return WO(f"De zin '{zin}' is grammaticaal correct.", waar, f"{UITLEG_TABEL[ww]}. Bij '{S}' hoort '{goed}'.")

def vergr(rng, invul=False):
    b, v, nl = k(rng, VERGR)
    ctx = k(rng, VERGR_ZIN[b])
    if invul:
        return IN(f"Vul de vergrotende trap in van '{b}': '{ctx}'", alt(v), f"{b} → {v} ({nl}).")
    return MC(f"Wat is de vergrotende trap van '{b}' in de zin '{ctx}'?", v, VERGR_FOUT[v], f"{b} → {v} ({nl})." + (" Met umlaut!" if any(c in v for c in "äöü") and not any(c in b for c in "äöü") else ""))

def weer(rng):
    de, nl = k(rng, WEER); fout = [x[0] for x in WEER if x[0] != de]; rng.shuffle(fout)
    return MC(k(rng, ["Hoe zeg je '{}' in het Duits?", "Welke Duitse zin betekent '{}'?"]).format(nl), de, fout, f"{nl} = {de}.")

def weer_invul(rng):
    de, nl = k(rng, WEER)
    return IN(f"Vertaal naar het Duits: '{nl[0].upper() + nl[1:]}'.", alt(de) + "|" + alt(de[0].upper() + de[1:]), f"{nl} = {de}.")

def maand(rng):
    de, nl, s = k(rng, MAAND)
    if rng.random() < 0.5:
        fout = [f"im {x}" for x in SEIZ if x != s]
        return MC(f"Bij welk jaargetijde hoort 'im {de}'?", f"im {s}", fout, f"{nl[0].upper() + nl[1:]} valt in {SEIZ[s]} (im {s}).")
    fout = [f"in {de}", f"am {de}", f"um {de}"]
    return MC(f"Hoe zeg je 'in {nl}' in het Duits?", f"im {de}", fout, f"Bij maanden en seizoenen gebruik je 'im': im {de}.")

def maand_invul(rng):
    de, nl, s = k(rng, MAAND)
    if rng.random() < 0.5:
        return IN(f"Vertaal naar het Duits: 'in {nl}'.", alt(f"im {de}"), f"im + maand: im {de}.")
    return IN(f"Vertaal naar het Duits: 'in {SEIZ[s]}'.", alt(f"im {s}"), f"im + seizoen: im {s}.")

def maand_wo(rng, waar):
    de, nl, s = k(rng, MAAND); g = s if waar else k(rng, [x for x in SEIZ if x != s])
    return WO(f"'Im {de}' hoort bij 'im {g}'.", waar, f"{nl[0].upper() + nl[1:]} valt in {SEIZ[s]} (im {s}).")

def richting(rng):
    de, nl = k(rng, RICHT)
    if rng.random() < 0.5:
        return MC(f"Wat is het tegenovergestelde van '{de}'?", TEGEN[de], [x[0] for x in RICHT if x[0] not in (de, TEGEN[de])] + ["im Winter"],
                  f"{de} ({nl}) ↔ {TEGEN[de]}.")
    return MC(f"Hoe zeg je '{nl}' in het Duits?", de, [x[0] for x in RICHT if x[0] != de], f"{nl} = {de}.")

OPEN = [
    ("Gisteren waren wij in het bos en het was koud.", "Gestern waren wir im Wald und es war kalt.", ["gestern", "waren", "Wald", "war", "kalt"], 4),
    ("In het zuiden schijnt de zon, in het noorden regent het.", "Im Süden scheint die Sonne, im Norden regnet es.", ["Süden/Sueden", "scheint", "Sonne", "Norden", "regnet"], 4),
    ("Vorige zomer hadden wij mooi weer aan zee.", "Letzten Sommer hatten wir schönes Wetter am Meer.", ["Sommer", "hatten", "Wetter", "Meer"], 3),
    ("In de winter wordt het koud en het sneeuwt.", "Im Winter wird es kalt und es schneit.", ["Winter", "wird", "kalt", "schneit"], 3),
    ("Het dorp ligt aan een meer en de streek is rustig.", "Das Dorf liegt an einem See und die Gegend ist ruhig.", ["Dorf", "See", "Gegend", "ruhig"], 3),
    ("Jij was gisteren op het strand, maar het was winderig.", "Du warst gestern am Strand, aber es war windig.", ["warst", "Strand", "war", "windig"], 3),
    ("Wij zijn benieuwd naar het uitzicht.", "Wir sind gespannt auf den Ausblick.", ["gespannt", "auf", "Ausblick"], 2),
    ("In de stad is het verkeer druk.", "In der Stadt ist der Verkehr hektisch.", ["Stadt", "Verkehr", "hektisch"], 2),
    ("Morgen wordt het warmer dan vandaag.", "Morgen wird es wärmer als heute.", ["wird", "wärmer/waermer", "als", "heute"], 3),
    ("Jullie hadden in de bergen veel sneeuw.", "Ihr hattet in den Bergen viel Schnee.", ["hattet", "Bergen", "Schnee"], 2),
    ("Er zijn veel rivieren en bossen in Duitsland.", "Es gibt viele Flüsse und Wälder in Deutschland.", ["gibt", "Flüsse/Fluesse", "Wälder/Waelder"], 2),
    ("In april regent het vaak.", "Im April regnet es oft.", ["April", "regnet", "oft"], 2),
]
GEBRUIKT = set()
def vertaal_open(rng):
    nl, de, s, n = k(rng, [o for o in OPEN if o[0] not in GEBRUIKT])
    s = [x for x in s if not any(a.lower() in nl.lower() for a in x.split("/"))]
    n = min(n, len(s) - 1) if len(s) > 2 else len(s)
    return OP(f"Vertaal naar het Duits: '{nl}'", de, s, n, f"Bijvoorbeeld: {de}")

def zin_mc(rng):
    nl, de, s, n = k(rng, OPEN); GEBRUIKT.add(nl)
    woorden = de.split()
    fout = []
    for a, b in [("war ", "hatte "), ("waren", "hatten"), ("hatten", "waren"), ("wird", "werdet"), ("warst", "wart"), ("hattet", "wart"),
                 ("Im ", "In "), ("im ", "in "), ("die Sonne", "der Sonne"), ("Das Dorf", "Der Dorf"), ("wärmer", "warmer"), ("Flüsse", "Flussen"),
                 ("gespannt auf", "stolz auf"), ("hektisch", "ruhig"), ("oft", "immer"), ("schneit", "regnet"), ("Wald", "See"), ("kalt", "heiß")]:
        if a in de: fout.append(de.replace(a, b, 1))
    if len(fout) < 3: fout += [de.replace(woorden[0], woorden[0] + " auch", 1), " ".join(woorden[1:2] + woorden[:1] + woorden[2:])]
    rng.shuffle(fout)
    return MC(f"Welke Duitse zin is de goede vertaling van '{nl}'?", de, fout, f"Goed: {de}")

T = {k_: globals()[k_] for k_ in ["zn_de_nl", "zn_nl_de", "zn_invul_de", "zn_invul_nl", "lidwoord", "lidwoord_invul", "meervoud", "meervoud_invul",
                                    "ww_de_nl", "ww_nl_de", "ww_invul", "weer", "weer_invul", "maand", "maand_invul", "richting", "zin_mc", "vertaal_open"]}
T.update({"sein": lambda r: vervoeg(r, "sein"), "haben": lambda r: vervoeg(r, "haben"), "werden": lambda r: vervoeg(r, "werden"),
          "sein_i": lambda r: vervoeg(r, "sein", True), "haben_i": lambda r: vervoeg(r, "haben", True), "werden_i": lambda r: vervoeg(r, "werden", True),
          "soh": sein_of_haben, "soh_i": lambda r: sein_of_haben(r, True), "vergr": vergr, "vergr_i": lambda r: vergr(r, True)})
WOT = {"lidwoord_wo": lidwoord_wo, "meervoud_wo": meervoud_wo, "betekenis_wo": betekenis_wo, "vervoeg_wo": vervoeg_wo, "maand_wo": maand_wo}

# 10 toetsen: titel + 20 slots (10 mc · 4 waaronwaar [2 waar/2 onwaar] · 5 invul · 1 open)
TOETSEN = [
    ("Woorden Duits → Nederlands (3)", ["zn_de_nl"] * 5 + ["ww_de_nl"] * 5 + ["betekenis_wo:T", "betekenis_wo:F", "betekenis_wo:F", "lidwoord_wo:T"] + ["zn_invul_nl"] * 3 + ["ww_invul"] * 2 + ["vertaal_open"]),
    ("Woorden Nederlands → Duits (3)", ["zn_nl_de"] * 5 + ["ww_nl_de"] * 3 + ["weer"] * 2 + ["lidwoord_wo:F", "betekenis_wo:T", "lidwoord_wo:T", "betekenis_wo:F"] + ["zn_invul_de"] * 3 + ["ww_invul", "weer_invul"] + ["vertaal_open"]),
    ("Lidwoorden & meervouden (2)", ["lidwoord"] * 5 + ["meervoud"] * 5 + ["lidwoord_wo:T", "meervoud_wo:F", "lidwoord_wo:F", "meervoud_wo:T"] + ["lidwoord_invul"] * 2 + ["meervoud_invul"] * 3 + ["vertaal_open"]),
    ("Grammatik: sein & haben in de verleden tijd (gemengd 2)", ["sein"] * 3 + ["haben"] * 3 + ["soh"] * 4 + ["vervoeg_wo:T", "vervoeg_wo:F", "vervoeg_wo:F", "vervoeg_wo:T"] + ["sein_i", "haben_i", "soh_i", "soh_i", "sein_i"] + ["vertaal_open"]),
    ("Grammatik: werden & de vergrotende trap", ["werden"] * 5 + ["vergr"] * 5 + ["vervoeg_wo:F", "vervoeg_wo:T", "vervoeg_wo:T", "vervoeg_wo:F"] + ["werden_i"] * 3 + ["vergr_i"] * 2 + ["vertaal_open"]),
    ("Weer, maanden, seizoenen & windrichtingen (2)", ["weer"] * 3 + ["maand"] * 4 + ["richting"] * 3 + ["maand_wo:T", "maand_wo:F", "maand_wo:F", "maand_wo:T"] + ["weer_invul"] * 2 + ["maand_invul"] * 3 + ["vertaal_open"]),
    ("Werkwoorden & bijvoeglijke naamwoorden uit de Lernliste", ["ww_de_nl"] * 5 + ["ww_nl_de"] * 5 + ["betekenis_wo:F", "betekenis_wo:T", "betekenis_wo:T", "betekenis_wo:F"] + ["ww_invul"] * 5 + ["vertaal_open"]),
    ("Zinnen vertalen (NL → DE)", ["zin_mc"] * 6 + ["weer", "soh", "vergr", "werden"] + ["vervoeg_wo:T", "vervoeg_wo:F", "betekenis_wo:F", "maand_wo:T"] + ["weer_invul", "soh_i", "vergr_i", "zn_invul_de", "werden_i"] + ["vertaal_open"]),
    ("Woorden & grammatica H1 gemengd (3)", ["zn_de_nl", "zn_nl_de", "lidwoord", "meervoud", "ww_de_nl", "sein", "haben", "werden", "vergr", "maand"] + ["lidwoord_wo:F", "vervoeg_wo:T", "meervoud_wo:T", "betekenis_wo:F"] + ["zn_invul_de", "soh_i", "werden_i", "meervoud_invul", "weer_invul"] + ["vertaal_open"]),
    ("Eindtoets H1 (3, alles door elkaar)", ["zin_mc", "zin_mc", "zn_nl_de", "ww_nl_de", "soh", "soh", "werden", "vergr", "meervoud", "richting"] + ["vervoeg_wo:F", "betekenis_wo:T", "maand_wo:F", "lidwoord_wo:T"] + ["zn_invul_de", "ww_invul", "soh_i", "vergr_i", "maand_invul"] + ["vertaal_open"]),
]

def mc_volgorde(rng, n):
    while True:
        p = [rng.randrange(4) for _ in range(n)]
        if max(p.count(x) for x in range(4)) > 0.4 * n: continue
        if sum((b - a) % 4 == 1 for a, b in zip(p, p[1:])) >= 0.5 * (n - 1): continue
        if any(p[i:i + q] == p[i + q:i + 2 * q] for q in (2, 3, 4) for i in range(n - 2 * q + 1)): continue
        return p

for i, (titel, plan) in enumerate(TOETSEN):
    nr = 63 + i; rng = random.Random(nr * 101); vragen = []; GEBRUIKT.clear()
    assert len(plan) == 20, (titel, len(plan))
    for slot in plan:
        naam, _, tf = slot.partition(":")
        for _ in range(500):
            v = WOT[naam](rng, tf == "T") if tf else T[naam](rng)
            if norm(v["vraag"]) not in GEZIEN: break
        else: raise SystemExit(f"geen unieke vraag: {slot}")
        GEZIEN.add(norm(v["vraag"])); vragen.append(v)
    mcs = [v for v in vragen if v["type"] == "mc"]; pos = iter(mc_volgorde(rng, len(mcs)))
    for v in mcs:
        o = v.pop("_opts"); rest = o[1:]; rng.shuffle(rest); j = next(pos); rest.insert(j, o[0]); v["opties"] = rest; v["antwoord"] = j
    ex = {"id": f"ex-h3-duits-{nr}", "hoofdstuk": 1, "hoofdstukTitel": "Umgebung & Wetter", "titel": f"Proeftoets {nr} — {titel}",
          "duurMin": 20, "vak": "Duits HAVO 3 — Hoofdstuk 1", "icoon": "🌲", "vragen": vragen}
    with open(f"{OUT}/examen_{nr}.js", "w") as f:
        f.write(f"/* Proeftoets ex-h3-duits-{nr} — {titel}\n   Neue Kontakte 3 HAVO Hoofdstuk 1 — herhaling van woorden & grammatica uit eerdere H1-toetsen\n   (gegenereerd met tools/gen_duits_h1_herhaling.py) */\n")
        f.write("DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
print("geschreven: 63 … 72")
