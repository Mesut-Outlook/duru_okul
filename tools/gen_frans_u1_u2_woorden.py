# -*- coding: utf-8 -*-
"""Frans U1 + U2 woordentoetsen ex-h3-frans-41…60 + U3 61…70 (2026-11-19).

Bron: Grandes Lignes 3 HAVO, Vocabulaire p. 48–49 (U1) en p. 86–87 (U2), van de boekpagina's
overgenomen. Wit blok = beide richtingen, blauw blok = alleen FR → NL (boekinstructie).
  41–48  U1 per blok (A, B, E, F) × (oefenen FR→NL, toets NL→FR)
  49     U1 gemengd
  50–57  U2 per blok × (oefenen, toets)
  58     U2 gemengd
  59–60  U1 + U2 gemengd (met verwarwoorden: attendre/arrêter, tard/tôt, garder …)
Deterministisch (vaste seed per toets). Nieuwe id's — nooit opnieuw draaien nadat Duru ze maakte.
"""
import json, os, random, re, unicodedata

DATA = os.path.join(os.path.dirname(__file__), "..", "havo3", "frans", "js", "data")

# (frans, nederlands, blauw)  — blauw = alleen herkennen (FR → NL)
U1 = {
 "A": [("la photo","de foto"),("le message","het bericht"),("la réaction","de reactie"),
       ("le commentaire","het commentaar"),("le site (web)","de (web)site"),("l'appli (v)","de app"),
       ("les réseaux sociaux","de social media"),("le portable","de mobiele telefoon"),
       ("l'addition (v)","de rekening"),("dire","zeggen"),("penser","denken"),("attendre","wachten"),
       ("utiliser","gebruiken"),("travailler","werken"),("payer","betalen"),("j'y vais","ik ga weg"),
       ("il voit","hij ziet"),("donne-moi","geef mij"),("j'ai vu","ik heb gezien"),
       ("amuse-toi bien","veel plezier"),("on était","wij waren"),("tu vas bien?","gaat het goed met je?"),
       ("bienvenue","welkom"),("à plus","tot later"),("grâce à","dankzij"),("devant","voor (plaats)"),
       ("derrière","achter"),("près de","dichtbij"),("heureux, -euse","gelukkig"),("drôle","grappig")],
 "B": [("les gens","de mensen"),("la tête","het hoofd"),("le temps","de tijd"),("le truc","het ding"),
       ("presque","bijna"),("pourtant","toch"),("maintenant","nu"),("avoir besoin (de)","nodig hebben"),
       ("oublier","vergeten"),("arrêter","stoppen"),("né(e)","geboren"),("facile","makkelijk"),
       ("nouveau, nouvelle","nieuw"),("premier, première","eerste"),("vieux, vieille","oud"),
       ("bon, bonne","goed"),
       ("le conseil","het advies",1),("la raison","de reden",1),("la dent","de tand",1),
       ("le sens de l'humour","het gevoel voor humor",1),("faire attention à","opletten",1),
       ("télécharger","downloaden",1),("garder","bewaren",1),("montrer","laten zien",1)],
 "E": [("la meilleure amie","de beste vriendin"),("marrant(e)","grappig"),("intelligent(e)","slim"),
       ("méchant(e)","gemeen"),("égoïste","egoïstisch"),("timide","verlegen"),("paresseux, -euse","lui"),
       ("souvent","vaak"),("une fois par semaine","een keer per week"),("je la connais","ik ken haar"),
       ("au club de sport","op de sportclub"),("à l'école","op school"),("au travail","op het werk"),
       ("chez des amis","bij vrienden"),("regarder la télé","televisie kijken"),("faire du sport","sporten"),
       ("jouer de la guitare","gitaar spelen"),("bavarder","kletsen")],
 "F": [("l'or (m)","het goud"),("l'argent (m)","het geld, het zilver"),("le prix","de prijs"),
       ("le parfum","de smaak"),("par an","per jaar"),("cent","honderd"),("mille","duizend"),
       ("un million","een miljoen"),("impossible","onmogelijk"),("pauvre","arm"),("cher, chère","duur"),
       ("américain(e)","Amerikaans"),("mieux","beter"),("vendre","verkopen"),("exister","bestaan"),
       ("savoir","weten"),
       ("le visiteur","de bezoeker",1),("le concours","de wedstrijd",1),("le cerveau","de hersenen",1),
       ("en moyenne","gemiddeld",1),("admirer","bewonderen",1),("prouver","bewijzen",1),
       ("compter","(mee)tellen",1),("fêter","vieren",1)],
}
U2 = {
 "A": [("commencer","beginnen"),("passer","doorbrengen"),("avoir l'air","eruit zien"),
       ("avoir le temps (de)","tijd hebben (om)"),("avoir envie (de)","zin hebben (om)"),
       ("se reposer","uitrusten"),("se retrouver","elkaar treffen"),("je me lève","ik sta op"),
       ("jouer à la console","gamen"),("discuter","kletsen"),("rigoler","lachen"),("appeler","bellen"),
       ("faire les magasins","winkelen"),("faire du sport","sporten"),("faire la grasse matinée","uitslapen"),
       ("je pourrai","ik zal kunnen"),("l'entrée (v)","de ingang"),("le cours","de les"),
       ("l'épisode (m)","de aflevering"),("jusqu'à","tot"),("chez moi","bij mij"),("plutôt","nogal"),
       ("tard","laat"),("tôt","vroeg"),("déjà","al"),("dur","hard, moeilijk"),("mort(e)","dood"),
       ("fatigué(e)","moe"),("prochain(e)","volgende"),("c'était","het was")],
 "B": [("le début","het begin"),("la vie","het leven"),("l'argent (m)","het geld"),
       ("le temps libre","de vrije tijd"),("la fois","de keer"),("le jeu","het spel"),
       ("le magazine","het tijdschrift"),("selon","volgens"),("aider","helpen"),("réfléchir","nadenken"),
       ("lire","lezen"),("haut(e)","hoog"),("chaque","ieder"),("comme","als, zoals"),("parfois","soms"),
       ("en plus","bovendien"),
       ("l'écran (m)","het scherm",1),("l'avis (m)","de mening",1),("le champion","de kampioen",1),
       ("l'entraînement (m)","de training",1),("il faut","je moet",1),("j'avais","ik had",1),
       ("connaître","kennen",1),("même","zelfs",1)],
 "E": [("suivre","volgen"),("garder (quelqu'un)","(op iemand) passen"),("espérer","hopen"),
       ("aller au restaurant","naar het restaurant gaan"),("aller à la salle de sport","naar de sportschool gaan"),
       ("faire du fitness","fitnessen"),("sortir","uitgaan"),("faire la vaisselle","afwassen"),
       ("faire les courses","boodschappen doen"),("ça me rend fou","daar word ik gek van"),
       ("plein (de)","een heleboel"),("d'abord","ten eerste"),("intéressant(e)","interessant"),
       ("passionnant(e)","boeiend"),("pas mal","niet slecht"),("nul(le)","waardeloos"),
       ("ennuyeux, -euse","saai"),("terrible","vreselijk")],
 "F": [("le voyage","de reis"),("le monde","de wereld"),("la tête","het hoofd"),("l'endroit (m)","de plek"),
       ("la vitesse","de snelheid"),("la victime","het slachtoffer"),("l'habitant (m)","de inwoner"),
       ("le jour","de dag"),("déranger","storen"),("choisir","kiezen"),("j'en ai assez","ik heb er genoeg van"),
       ("long, longue","lang"),("amoureux, -euse","verliefd"),("curieux, -euse","nieuwsgierig"),
       ("l'étoile (v)","de ster",1),("le moyen","het middel",1),("le scientifique","de wetenschapper",1),
       ("la trottinette","de step",1),("l'entreprise (v)","het bedrijf",1),("l'espace (m)","de ruimte",1),
       ("le commerce","de handel",1),("il finira","hij zal eindigen",1),("à l'intérieur","binnen",1),
       ("polluant(e)","vervuilend",1)],
}
BLOK = {"A": "blok A", "B": "blok B", "E": "blok E", "F": "blok F"}
U3 = {
 "A": [("la gare","het station"),("le train","de trein"),("le car","de streekbus"),("l'avion (m)","het vliegtuig"),
       ("la voiture","de auto"),("la direction","de richting"),("les renseignements","de inlichtingen"),
       ("le départ","het vertrek"),("la destination","de bestemming"),("l'arrivée (v)","de aankomst"),
       ("la neige","de sneeuw"),("le sandwich","het broodje"),("l'aller-retour (m)","het retourtje"),
       ("à cause de","vanwege"),("en face de","tegenover"),("dans une heure","over een uur"),
       ("bienvenue","welkom"),("agréable","prettig"),("seul(e)","alleen"),("je suis désolé(e)","het spijt me"),
       ("je serai","ik zal zijn"),("il fait froid","het is koud"),("aider","helpen"),("continuer","doorgaan"),
       ("monter","instappen"),("chercher","ophalen, zoeken"),("demander","vragen"),
       ("rendre visite à","(iemand) bezoeken"),("descendre","uitstappen"),("entendre","horen")],
 "B": [("le désert","de woestijn"),("le travail","het werk"),("le centre-ville","het centrum"),
       ("le quartier","de wijk"),("le gâteau","het gebak"),("le temps libre","de vrije tijd"),
       ("l'arabe (m)","het Arabisch (taal)"),("marocain(e)","Marokkaans"),("seulement","slechts"),
       ("sauf","behalve"),("heureusement","gelukkig maar"),("tout","alles"),("au printemps","in het voorjaar"),
       ("simple","eenvoudig"),("découvrir","ontdekken"),("partir","vertrekken"),
       ("la pollution","de vervuiling",1),("le sable","het zand",1),("l'avantage (m)","het voordeel",1),
       ("l'inconvénient (m)","het nadeel",1),("nombreux, -euse","veel, vele",1),("manquer","missen",1),
       ("vivre","wonen",1),("j'irai","ik zal gaan",1)],
 "E": [("blaguer","grappen maken"),("j'aurai","ik zal hebben/krijgen"),("la vue (sur)","het uitzicht (op)"),
       ("les sports d'hiver","de wintersport"),("le vêtement","het kledingstuk"),("le lit","het bed"),
       ("le patron","de baas"),("à côté (de)","naast"),("moi aussi","ik ook"),("au camping","op de camping"),
       ("le petit déjeuner","het ontbijt"),("le déjeuner","de lunch"),("le diner","het avondeten"),
       ("délicieux, -euse","heerlijk"),("mauvais(e)","slecht"),("propre","schoon"),("sale","vies"),
       ("ridicule","belachelijk")],
 "F": [("le métier","het beroep"),("la solution","de oplossing"),("la petite annonce","de advertentie"),
       ("le journal","de krant"),("le rendez-vous","de afspraak"),("la pluie","de regen"),("contre","tegen"),
       ("tous les ans","ieder jaar"),("avant","voor (tijd)"),("sur","op"),("principal(e)","belangrijkste"),
       ("recyclable","recyclebaar"),("rester","blijven"),("inventer","bedenken, uitvinden"),("trouver","vinden"),
       ("ressembler à","lijken op"),
       ("le vétérinaire","de dierenarts",1),("la qualité","de goede eigenschap",1),("la reine","de koningin",1),
       ("l'environnement (m)","het milieu",1),("écolo(gique)","milieubewust",1),("construire","bouwen",1),
       ("voler","vliegen",1),("diminuer","verminderen",1)],
}
PAG = {(3, "A"): 124, (3, "B"): 124, (3, "E"): 125, (3, "F"): 125, (1, "A"): 48, (1, "B"): 48, (1, "E"): 49, (1, "F"): 49, (2, "A"): 86, (2, "B"): 86, (2, "E"): 87, (2, "F"): 87}

def woord(t, u, b):
    return {"fr": t[0], "nl": t[1], "blauw": len(t) > 2, "u": u, "b": b}

def kaal(s):  # accenten weg
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def toon_fr(fr):  # weergave: "(v)" / "(m)" laten staan, rest zoals in boek
    return fr

def fr_alts(fr):
    s = re.sub(r"\s*\((v|m)\)", "", fr).replace("?", "").strip()
    alts = []
    if ", " in s:                       # heureux, -euse / nouveau, nouvelle
        a, b = s.split(", ", 1)
        alts += [a, (a[: a.rfind("eux")] + "euse") if b == "-euse" else b]
    else:
        alts.append(re.sub(r"\((e|le)\)", "", s).replace("  ", " ").strip())   # marrant(e) → marrant
    out = []
    for a in alts:
        a = re.sub(r"\s*\([^)]*\)", "", a).strip()  # (de) / (web) / (quelqu'un) optioneel
        out.append(a)
        core = re.sub(r"^(le |la |les |un |une |l')", "", a)
        if core != a: out.append(core)
    out += [kaal(a) for a in out if kaal(a) != a]
    return "|".join(dict.fromkeys(out))

def nl_alts(nl):
    out = []
    for p in re.split(r",\s*", nl):
        p = re.sub(r"\s*\([^)]*\)", "", p).replace("?", "").strip()
        out.append(p)
        core = re.sub(r"^(de |het |een )", "", p)
        if core != p: out.append(core)
    return "|".join(dict.fromkeys(out))

def kern_ok(alts):  # substring-nakijken: korte sleutels zouden fout goedrekenen
    return all(len(a) >= 4 for a in alts.split("|"))

def soort(w):
    f = w["fr"]
    if re.match(r"^(le |la |les |l'|un )", f): return "nw"
    if re.search(r"(er|ir|re|oir)$", f) and " " not in f: return "ww"
    return "x"

BIJNA = [{"intéressant(e)", "passionnant(e)"}, {"sortir", "aller au restaurant"}]

def zelfde(p, w):
    """Zelfde betekenis of zelfde Frans woord (drôle/marrant, la tête in U1 én U2, l'argent …)."""
    if any({p["fr"], w["fr"]} <= g for g in BIJNA): return True
    if {p["fr"], w["fr"]} == {"avant", "devant"}: return False   # voor (tijd) ≠ voor (plaats)
    return bool(set(nl_alts(p["nl"]).split("|")) & set(nl_alts(w["nl"]).split("|")) or
                set(fr_alts(p["fr"]).split("|")) & set(fr_alts(w["fr"]).split("|")))

def afleiders(w, pool, kant, rnd, n=3):
    pool = [p for p in pool if not zelfde(p, w)]
    gelijk = [p for p in pool if soort(p) == soort(w) and p[kant] != w[kant]]
    rest = [p for p in pool if p not in gelijk and p[kant] != w[kant]]
    rnd.shuffle(gelijk); rnd.shuffle(rest)
    gekozen, gezien = [], {w[kant]}
    for p in gelijk + rest:
        if p[kant] not in gezien:
            gekozen.append(p[kant]); gezien.add(p[kant])
        if len(gekozen) == n: break
    # goed antwoord niet steeds het kortste / langste (gate 17, teslim KISA): ruil zo nodig één afleider
    goed = len(w[kant])
    extra = [p[kant] for p in pool if p[kant] not in gezien]
    if gekozen and all(len(g) > goed for g in gekozen):
        korter = [e for e in extra if len(e) <= goed]
        if korter: gekozen[-1] = rnd.choice(korter)
    elif gekozen and all(len(g) < goed for g in gekozen):
        langer = [e for e in extra if len(e) >= goed]
        if langer: gekozen[-1] = rnd.choice(langer)
    return gekozen

# --- vraagsjablonen (gevarieerd zodat geen vraag letterlijk in twee toetsen staat) ---
# Weinig woorden van ≥4 letters in de sjablonen: teslim_check vergelijkt woordensets, en een lang
# sjabloon maakt elke vraag een "kopie" van de vorige. Geen "voor" (= ook een antwoord: devant).
T_FRNL = ["Wat betekent <b>{fr}</b>?", "<b>{fr}</b> = ?", "<b>{fr}</b> betekent …", "NL van <b>{fr}</b>?"]
T_NLFR = ["Hoe zeg je <b>{nl}</b> in het Frans?", "<b>{nl}</b> = ? (Frans)", "<b>{nl}</b> in het Frans is …", "Frans: <b>{nl}</b> = ?"]
T_INV_NLFR = ["Vertaal: <b>{nl}</b> → Frans", "In het Frans: <b>{nl}</b>", "Frans: <b>{nl}</b> = …", "<b>{nl}</b> → FR"]
T_INV_FRNL = ["Vertaal: <b>{fr}</b> → NL", "In het Nederlands: <b>{fr}</b>", "NL: <b>{fr}</b> = …", "<b>{fr}</b> → NL"]
T_WO = ["<b>{fr}</b> = <i>{nl}</i>", "<b>{fr}</b> → <i>{nl}</i>", "<i>{nl}</i> = <b>{fr}</b>", "Klopt: <b>{fr}</b> = <i>{nl}</i>?"]

GEBRUIKT = set()
WO_PAREN = set()

def bestaande_vragen():
    s = set()
    for f in os.listdir(DATA):
        txt = open(os.path.join(DATA, f), encoding="utf-8").read()
        s.update(re.findall(r'"vraag":\s*"((?:[^"\\]|\\.)*)"', txt))
    return s

def tekst(sjablonen, k, **kw):
    for i in range(len(sjablonen)):
        t = sjablonen[(k + i) % len(sjablonen)].format(**kw)
        if t not in GEBRUIKT:
            GEBRUIKT.add(t); return t
    basis = sjablonen[k % len(sjablonen)].format(**kw)
    for extra in (" (Unité %s)" % kw.get("u"), " (Unité %s, nog een keer)" % kw.get("u"), " (herhaling)", " (herhaling 2)", " (herhaling 3)"):
        if basis + extra not in GEBRUIKT: break
    t = basis + extra
    GEBRUIKT.add(t); return t

def bron(w):
    return "Unité %d, p. %d, %s%s" % (w["u"], PAG[(w["u"], w["b"])], BLOK[w["b"]], " (blauw: alleen herkennen)" if w["blauw"] else "")

def mc_frnl(w, pool, rnd, k):
    opts = afleiders(w, pool, "nl", rnd) + [w["nl"]]
    rnd.shuffle(opts)
    return {"type": "mc", "vraag": tekst(T_FRNL, k, fr=w["fr"].rstrip("?"), u=w["u"]), "opties": opts, "antwoord": opts.index(w["nl"]),
            "uitleg": "<b>%s</b> = %s. (%s)" % (w["fr"], w["nl"], bron(w))}

def mc_nlfr(w, pool, rnd, k):
    opts = afleiders(w, pool, "fr", rnd) + [w["fr"]]
    rnd.shuffle(opts)
    return {"type": "mc", "vraag": tekst(T_NLFR, k, nl=w["nl"], u=w["u"]), "opties": opts, "antwoord": opts.index(w["fr"]),
            "uitleg": "%s = <b>%s</b>. (%s)" % (w["nl"], w["fr"], bron(w))}

ALLE = []
EXTRA_FR = {"on était": "nous étions|nous etions", "le truc": "la chose|chose", "pourtant": "quand même|quand meme|tout de même",
            "mieux": "meilleur", "l'épisode (m)": "episode", "rigoler": "rire", "se retrouver": "retrouver",
            "se reposer": "reposer", "le magazine": "magazine", "parfois": "quelquefois|de temps en temps",
            "en plus": "de plus", "plein (de)": "beaucoup de", "j'en ai assez": "j'en ai marre|j en ai marre",
            "d'abord": "premièrement|premierement|tout d'abord", "le parfum": "le goût|goût|gout|saveur"}
EXTRA_NL = {"le conseil": "raad", "pourtant": "toch", "montrer": "tonen", "souvent": "dikwijls",
            "égoïste": "egoistisch|egoïst|egoist", "regarder la télé": "tv kijken|tv-kijken", "discuter": "praten|discussi",
            "faire du fitness": "fitness", "plein (de)": "veel|een hoop", "l'entreprise (v)": "onderneming",
            "l'habitant (m)": "bewoner", "l'épisode (m)": "episode"}
EXTRA_FR.update({"le diner": "le dîner|dîner|diner", "l'aller-retour (m)": "aller retour|aller-retour",
                 "le centre-ville": "le centre|centre", "à côté (de)": "a cote", "le petit déjeuner": "petit dejeuner"})
EXTRA_NL.update({"le car": "bus|touringcar", "le sandwich": "sandwich", "l'aller-retour (m)": "retour",
                 "le journal": "dagblad", "le patron": "chef|werkgever", "agréable": "aangenaam|fijn",
                 "heureusement": "gelukkig", "seulement": "alleen", "le diner": "diner|avondmaal",
                 "les renseignements": "informatie", "la petite annonce": "advertentie|annonce"})
VERVANG_NL = {"garder (quelqu'un)": "op iemand passen|oppassen|passen op"}

def syn(w, kant):
    f = fr_alts if kant == "fr" else nl_alts
    alts = (VERVANG_NL[w["fr"]] if kant == "nl" and w["fr"] in VERVANG_NL else f(w[kant])).split("|")
    alts += [a for a in (EXTRA_FR if kant == "fr" else EXTRA_NL).get(w["fr"], "").split("|") if a and a not in alts]
    for p in ALLE:
        if p is not w and zelfde(p, w) and not (kant == "fr" and p["blauw"]):
            alts += [a for a in f(p[kant]).split("|") if a not in alts]
    return "|".join(alts)

def inv_nlfr(w, k):
    return {"type": "invul", "vraag": tekst(T_INV_NLFR, k, nl=w["nl"], u=w["u"]), "antwoord": syn(w, "fr"),
            "uitleg": "%s = <b>%s</b>. Let op de spelling en de accenten. (%s)" % (w["nl"], w["fr"], bron(w))}

def inv_frnl(w, k):
    return {"type": "invul", "vraag": tekst(T_INV_FRNL, k, fr=w["fr"].rstrip("?"), u=w["u"]), "antwoord": syn(w, "nl"),
            "uitleg": "<b>%s</b> = %s. (%s)" % (w["fr"], w["nl"], bron(w))}

def wo(w, pool, rnd, k, waar):
    nl = w["nl"]
    if not waar:   # niet twee keer hetzelfde foute paar in verschillende toetsen (teslim KOPYA)
        nl = next(n for n in afleiders(w, pool, "nl", rnd, 6) if (w["fr"], n) not in WO_PAREN)
    WO_PAREN.add((w["fr"], nl))
    return {"type": "waaronwaar", "vraag": tekst(T_WO, k, fr=w["fr"].rstrip("?"), nl=nl, u=w["u"]), "antwoord": waar,
            "uitleg": ("Waar. " if waar else "Onwaar. ") + "<b>%s</b> = %s%s. (%s)" % (
                w["fr"], w["nl"], "" if waar else " (niet: " + nl + ")", bron(w))}

# Verwarwoorden: Duru schreef 'attendre' voor 'stoppen' (examen_u1_vocab_1 #12).
VERWAR = [
 ("<i>Stoppen</i> is in het Frans:", ["arrêter", "attendre", "acheter", "aider"], 0,
  "<b>arrêter</b> = stoppen (U1 blok B). <b>attendre</b> = wachten (U1 blok A) — die twee worden vaak verwisseld."),
 ("<i>Wachten</i> is in het Frans:", ["arrêter", "attendre", "entendre", "appeler"], 1,
  "<b>attendre</b> = wachten (U1 blok A); <b>arrêter</b> = stoppen."),
 ("<i>Le film commence ___, à 7 heures du matin!</i> (vroeg)", ["tard", "tôt", "déjà", "plutôt"], 1,
  "<b>tôt</b> = vroeg, <b>tard</b> = laat (U2 blok A)."),
 ("Wat betekent <b>garder</b> in <i>Je garde mon petit frère</i>?", ["bewaren", "(op iemand) passen", "wachten", "laten zien"], 1,
  "<b>garder quelqu'un</b> = op iemand passen (U2 blok E). Zonder persoon betekent garder: bewaren (U1 blok B)."),
 ("<i>Le café est ___ l'école.</i> (vóór)", ["derrière", "près de", "devant", "chez"], 2,
  "<b>devant</b> = voor (plaats), <b>derrière</b> = achter, <b>près de</b> = dichtbij (U1 blok A)."),
 ("Welk woord betekent <b>soms</b>?", ["souvent", "parfois", "presque", "pourtant"], 1,
  "<b>parfois</b> = soms (U2 blok B), <b>souvent</b> = vaak (U1 blok E), <b>presque</b> = bijna, <b>pourtant</b> = toch."),
 ("Welk woord betekent <b>het goud</b>?", ["l'argent", "l'or", "le prix", "le parfum"], 1,
  "<b>l'or</b> = het goud; <b>l'argent</b> = het geld én het zilver (U1 blok F)."),
 ("Welke twee zijn tegenstellingen?", ["nouveau ↔ vieux", "bon ↔ facile", "cher ↔ américain", "drôle ↔ marrant"], 0,
  "<b>nouveau</b> (nieuw) ↔ <b>vieux</b> (oud). drôle en marrant betekenen allebei grappig."),
 ("Wat betekent <b>payer</b>?", ["denken", "betalen", "werken", "gebruiken"], 1,
  "<b>payer</b> = betalen; <b>penser</b> = denken (U1 blok A) — ze beginnen allebei met een p."),
 ("Wat betekent <b>discuter</b> (U2) en welk U1-woord betekent hetzelfde?", ["lachen — rigoler", "kletsen — bavarder", "bellen — appeler", "lezen — lire"], 1,
  "<b>discuter</b> (U2 blok A) en <b>bavarder</b> (U1 blok E) betekenen allebei kletsen."),
 # U3 (index 10–)
 ("<i>Je me lave les mains ___ le dîner.</i> (vóór, tijd)", ["devant", "avant", "en face de", "à côté de"], 1,
  "<b>avant</b> = voor in de tijd (U3 blok F). <b>devant</b> = voor een plek (U1 blok A): <i>devant l'école</i>."),
 ("<i>J'ai perdu mes clés. Je les ___ partout, mais je ne les ___ pas!</i>", ["cherche — trouve", "trouve — cherche", "demande — entends", "continue — reste"], 0,
  "<b>chercher</b> = zoeken, <b>trouver</b> = vinden (U3): ik zoek ze overal, maar ik vind ze niet."),
 ("Wat is het tegenovergestelde van <b>monter</b> (in de trein)?", ["partir", "descendre", "rester", "continuer"], 1,
  "<b>monter</b> = instappen, <b>descendre</b> = uitstappen (U3 blok A)."),
 ("<i>Mon pantalon est ___ : je l'ai lavé hier!</i>", ["sale", "propre", "mauvais", "ridicule"], 1,
  "<b>propre</b> = schoon, <b>sale</b> = vies (U3 blok E). Gewassen = schoon → propre."),
 ("Welk werkwoord betekent <b>horen</b>?", ["attendre", "entendre", "demander", "rendre visite à"], 1,
  "<b>entendre</b> = horen (U3 blok A); <b>attendre</b> = wachten (U1 blok A) — één letter verschil."),
 ("<i>Je ___ à la maison, je ne pars pas.</i> (blijven)", ["pars", "reste", "descends", "trouve"], 1,
  "<b>rester</b> = blijven, <b>partir</b> = vertrekken (U3)."),
 ("Wat betekent <b>le car</b>?", ["de auto", "de streekbus", "de trein", "het station"], 1,
  "<b>le car</b> = de streekbus, niet de auto! De auto = <b>la voiture</b> (U3 blok A)."),
 # herhaling 71–80 (index 17–), nieuwe zinnen — niet letterlijk gelijk aan 59/60/69/70
 ("<i>Le bus ne vient pas. Je ___ depuis vingt minutes!</i>", ["arrête", "attends", "entends", "oublie"], 1,
  "<b>attendre</b> = wachten: ik wacht al twintig minuten. <b>arrêter</b> = stoppen (U1 blok B)."),
 ("<i>___ de parler, s'il te plaît! Je travaille.</i> (stop)", ["Attends", "Arrête", "Aide", "Appelle"], 1,
  "<b>arrête</b> = stop (arrêter, U1 blok B). <b>attends</b> = wacht (attendre)."),
 ("<i>Je suis ___ : je me suis levé à cinq heures.</i>", ["mort", "fatigué", "drôle", "heureux"], 1,
  "<b>fatigué(e)</b> = moe (U2 blok A). Vroeg opstaan → moe."),
 ("<i>Ce film est ___ : je dors après dix minutes.</i>", ["passionnant", "ennuyeux", "marrant", "intéressant"], 1,
  "<b>ennuyeux</b> = saai (U2 blok E); <b>passionnant</b> = boeiend."),
 ("<i>Il ne fait pas ses devoirs, il dort toute la journée. Il est ___.</i>", ["timide", "paresseux", "méchant", "égoïste"], 1,
  "<b>paresseux</b> = lui (U1 blok E)."),
 ("<i>Pour aller à Paris, je ___ dans le train à Lille.</i> (instappen)", ["descends", "monte", "reste", "pars"], 1,
  "<b>monter</b> = instappen, <b>descendre</b> = uitstappen (U3 blok A)."),
 ("<i>Ma chambre est ___ : il y a des vêtements partout.</i>", ["propre", "sale", "délicieuse", "simple"], 1,
  "<b>sale</b> = vies, <b>propre</b> = schoon (U3 blok E)."),
 ("<i>Il y a un café ___ la gare.</i> (tegenover)", ["à cause de", "en face de", "dans une heure", "sauf"], 1,
  "<b>en face de</b> = tegenover; <b>à cause de</b> = vanwege (U3 blok A)."),
 ("Welk woord hoort <b>niet</b> bij reizen (U3)?", ["la gare", "le lit", "le départ", "l'arrivée"], 1,
  "<b>le lit</b> = het bed (U3 blok E). La gare, le départ, l'arrivée horen bij reizen (blok A)."),
]

def verwar(i):
    v, o, a, u = VERWAR[i]
    GEBRUIKT.add(v)
    return {"type": "mc", "vraag": v, "opties": list(o), "antwoord": a, "uitleg": u}

def lekt(tekst, alts):
    """teslim_check-regel 4: invul-antwoord (≥4 tekens, heel woord) mag nergens anders in de toets staan."""
    for a in alts:
        if len(a) >= 4 and re.search(r"(^|[^a-zà-ÿ0-9])" + re.escape(a) + r"($|[^a-zà-ÿ0-9])", tekst, re.I):
            return True
    return False

def maak(woorden, pool, seed, richting, extra=()):
    """richting 'frnl' (oefenen) of 'nlfr' (toets) of 'mix'. 20 vragen; invul-woorden komen nergens anders voor."""
    rnd = random.Random(seed)
    plan = {"frnl": dict(mc_frnl=7, inv_frnl=4, wo=4, mc_nlfr=3, inv_nlfr=2),
            "nlfr": dict(mc_nlfr=6, inv_nlfr=7, mc_frnl=3, wo=3, inv_frnl=1),
            "mix":  dict(mc_frnl=5, mc_nlfr=4, inv_nlfr=5, inv_frnl=2, wo=4)}[richting]
    groot = max(plan, key=plan.get); plan[groot] -= len(extra)
    vragen = [verwar(i) for i in extra]
    verwar_tekst = " ".join(q["vraag"] + " " + " ".join(q["opties"]) for q in vragen)
    vrij = list(woorden); rnd.shuffle(vrij)
    alts = []                      # alle invul-antwoorden van deze toets
    k = seed
    # 1 · invul eerst, met verse woorden die nergens anders (verwarvragen) staan
    for soortv in ("inv_nlfr", "inv_frnl"):
        for _ in range(plan[soortv]):
            k += 1
            for w in vrij:
                if soortv == "inv_nlfr" and w["blauw"]: continue
                al = syn(w, "fr" if soortv == "inv_nlfr" else "nl").split("|")
                if not kern_ok("|".join(al)) or lekt(verwar_tekst, al + [a[:-1] for a in al if len(a) >= 6]): continue  # ook stam: arrêter ~ arrête
                if soortv == "inv_frnl" and any(len(a.split()) > 2 for a in al): continue  # lange NL-zin: te streng
                vrij.remove(w); alts += al
                vragen.append(inv_nlfr(w, k) if soortv == "inv_nlfr" else inv_frnl(w, k)); break
            else:
                raise SystemExit("geen invul-woord meer (seed %d)" % seed)
    schoon = lambda w: not lekt(w["fr"], alts) and not lekt(w["nl"], alts)
    vrij = [w for w in vrij if schoon(w)]
    pool = [w for w in pool if schoon(w)]
    oud = [w for w in woorden if schoon(w) and w not in vrij]  # al als invul gebruikt → nooit
    n_wo = 0; gebruikt = []; klaar = set()
    for soortv in ("mc_frnl", "mc_nlfr", "wo"):
        for _ in range(plan[soortv]):
            k += 1
            kand = [w for w in vrij if soortv != "mc_nlfr" or not w["blauw"]]
            # blauwe woorden voorrang bij FR→NL, zodat ze aan bod komen
            if soortv != "mc_nlfr":
                kand.sort(key=lambda w: not w["blauw"])
            if kand:
                w = kand[0]; vrij.remove(w)
            else:   # blok op: woord nog eens, in een andere vraagvorm
                kand = [w for w in gebruikt if (w["fr"], soortv) not in klaar and (soortv != "mc_nlfr" or not w["blauw"])]
                w = rnd.choice(kand)
            gebruikt.append(w); klaar.add((w["fr"], soortv))
            if soortv == "mc_frnl": q = mc_frnl(w, pool, rnd, k)
            elif soortv == "mc_nlfr": q = mc_nlfr(w, pool, rnd, k)
            else:
                n_wo += 1; q = wo(w, pool, rnd, k, n_wo % 2 == 0)
            vragen.append(q)
    rnd.shuffle(vragen)
    # goed-positie gelijk verdeeld: elk blok van 4 mc's krijgt 0..3 in willekeurige volgorde
    mcs = [q for q in vragen if q["type"] == "mc"]
    while True:   # gate 16: < 60 % van de overgangen +1
        volg = []
        while len(volg) < len(mcs):
            blok = [0, 1, 2, 3]; rnd.shuffle(blok); volg += blok
        volg = volg[:len(mcs)]
        plus1 = sum(1 for a, b in zip(volg, volg[1:]) if b == (a + 1) % 4)
        if plus1 < 0.5 * (len(volg) - 1): break
    for q, pos in zip(mcs, volg):
        goed = q["opties"].pop(q["antwoord"]); q["antwoord"] = pos; q["opties"].insert(pos, goed)
    return vragen

def schrijf(nr, data):
    pad = os.path.join(DATA, "examen_%d.js" % nr)
    kop = "/* %s\n   Grandes Lignes 3 HAVO — gegenereerd door tools/gen_frans_u1_u2_woorden.py (2026-11-19) */\n" % data["titel"]
    open(pad, "w", encoding="utf-8").write(kop + "DURU.registerExamen(" + json.dumps(data, indent=2, ensure_ascii=False) + ");\n")
    print("examen_%d.js  %s  (%d vragen)" % (nr, data["titel"], len(data["vragen"])))

def toets(nr, hf, titel, vragen, duur=15):
    assert len(vragen) == 20, (nr, len(vragen))
    return {"id": "ex-h3-frans-%d" % nr, "hoofdstuk": hf,
            "hoofdstukTitel": {1: "Unité 1 — Poste, like, partage", 2: "Unité 2 — Du temps pour moi", 3: "Unité 3 — En route!"}[hf],
            "titel": titel, "vak": "Frans · HAVO 3", "icoon": "🔤", "duurMin": duur, "vragen": vragen}

def main():
    GEBRUIKT.update(bestaande_vragen())
    w1 = {b: [woord(t, 1, b) for t in l] for b, l in U1.items()}
    w2 = {b: [woord(t, 2, b) for t in l] for b, l in U2.items()}
    alle1 = sum(w1.values(), []); alle2 = sum(w2.values(), [])
    ALLE.extend(alle1 + alle2)
    nr = 41
    for u, ws, alle, hf in ((1, w1, alle1, 1), (2, w2, alle2, 2)):
        for b in "ABEF":
            p = PAG[(u, b)]
            schrijf(nr, toets(nr, hf, "Woorden U%d · p. %d %s · oefenen (FR → NL)" % (u, p, BLOK[b]),
                              maak(ws[b], ws[b], nr * 7, "frnl"))); nr += 1
            schrijf(nr, toets(nr, hf, "Woorden U%d · p. %d %s · toets (NL → FR)" % (u, p, BLOK[b]),
                              maak(ws[b], ws[b], nr * 7, "nlfr"))); nr += 1
        extra = (0, 4, 8) if u == 1 else (2, 9)
        schrijf(nr, toets(nr, hf, "Woorden U%d · gemengd (alle blokken, beide richtingen)" % u,
                          maak(alle, alle, nr * 7, "mix", extra), 20)); nr += 1
    beide = alle1 + alle2
    schrijf(nr, toets(nr, 2, "Woorden U1 + U2 · gemengd A (met verwarwoorden)",
                      maak(beide, beide, nr * 7, "mix", (1, 3, 6)), 20)); nr += 1
    schrijf(nr, toets(nr, 2, "Woorden U1 + U2 · gemengd B (met verwarwoorden)",
                      maak(beide, beide, nr * 7, "mix", (5, 7)), 20)); nr += 1

def main_u3():
    """U3 (2026-11-19): ex-h3-frans-61…70. Los van main(), zodat 41–60 (al gemaakt) nooit herschreven worden."""
    GEBRUIKT.update(bestaande_vragen())
    w = {u: {b: [woord(t, u, b) for t in l] for b, l in d.items()} for u, d in ((1, U1), (2, U2), (3, U3))}
    alle = {u: sum(w[u].values(), []) for u in w}
    ALLE.extend(alle[1] + alle[2] + alle[3])
    nr = 61
    for b in "ABEF":
        p = PAG[(3, b)]
        schrijf(nr, toets(nr, 3, "Woorden U3 · p. %d %s · oefenen (FR → NL)" % (p, BLOK[b]),
                          maak(w[3][b], w[3][b], nr * 7, "frnl"))); nr += 1
        schrijf(nr, toets(nr, 3, "Woorden U3 · p. %d %s · toets (NL → FR)" % (p, BLOK[b]),
                          maak(w[3][b], w[3][b], nr * 7, "nlfr"))); nr += 1
    schrijf(nr, toets(nr, 3, "Woorden U3 · gemengd (alle blokken, beide richtingen)",
                      maak(alle[3], alle[3], nr * 7, "mix", (11, 12, 13, 16)), 20)); nr += 1
    drie = alle[1] + alle[2] + alle[3]
    schrijf(nr, toets(nr, 3, "Woorden U1 + U2 + U3 · gemengd (met verwarwoorden)",
                      maak(drie, drie, nr * 7, "mix", (10, 14, 15)), 20)); nr += 1

def main_herhaling():
    """Herhaling U1–U3 (2026-11-21): ex-h3-frans-71…80. Per unité oefenen / toets / gemengd + U1–U3 eindtoets."""
    GEBRUIKT.update(bestaande_vragen())
    w = {u: {b: [woord(t, u, b) for t in l] for b, l in d.items()} for u, d in ((1, U1), (2, U2), (3, U3))}
    alle = {u: sum(w[u].values(), []) for u in w}
    ALLE.extend(alle[1] + alle[2] + alle[3])
    verwar_per_u = {1: (17, 18, 21), 2: (19, 20), 3: (22, 23, 24, 25)}
    nr = 71
    for u in (1, 2, 3):
        schrijf(nr, toets(nr, u, "Woorden U%d · herhaling · oefenen (FR → NL)" % u,
                          maak(alle[u], alle[u], nr * 11, "frnl"))); nr += 1
        schrijf(nr, toets(nr, u, "Woorden U%d · herhaling · toets (NL → FR)" % u,
                          maak(alle[u], alle[u], nr * 11, "nlfr"))); nr += 1
        schrijf(nr, toets(nr, u, "Woorden U%d · herhaling · gemengd (in zinnen)" % u,
                          maak(alle[u], alle[u], nr * 11, "mix", verwar_per_u[u]), 20)); nr += 1
    drie = alle[1] + alle[2] + alle[3]
    schrijf(nr, toets(nr, 3, "Woorden U1 + U2 + U3 · eindtoets (herhaling)",
                      maak(drie, drie, nr * 11, "mix"), 20)); nr += 1

if __name__ == "__main__":
    import sys
    # 41–70 zijn al gemaakt: standaard alleen 71–80. `--u1u2` / `--u3` herschrijven oude toetsen — NIET doen.
    main() if "--u1u2" in sys.argv else main_u3() if "--u3" in sys.argv else main_herhaling()
