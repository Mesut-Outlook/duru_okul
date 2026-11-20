#!/usr/bin/env python3
"""Scheikunde HAVO 3 — 3 gemengde toetsen H1 + H2 (examen_h2_80…82), 2026-11-20.
Per toets 20 vragen: 12 H2 (§2.3/§2.4 zwaar, ook §2.1/§2.2) + 8 H1 (§1.1/§1.3/§1.4); 10 mc / 6 w-o / 3 invul / 1 open.
Gericht op Duru's fouten (zwakte.py --fouten, 2026-11-20): systematische naam/formule, molecuulmassa, index vs coëfficiënt,
isotopen/massa deeltjes, §1.4 mengsels (suspensie/emulsie/nevel/rook), kelvin, faseveranderingen, dichtheid.
Getallen worden hier berekend (atoommassa-tabel AT, zoals in het boek: H 1,008; C 12,01; N 14,01; O 16,00; S 32,07).
Hergebruikt tx/M/W/I/O + plaats van gen_scheikunde_basis.py (importeert alleen; schrijft niets van oude toetsen).
"""
import importlib.util, json, os, random, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location("basis", os.path.join(HIER, "gen_scheikunde_basis.py"))
B = importlib.util.module_from_spec(_s); _s.loader.exec_module(B)   # main() draait NIET (staat achter __main__)
M, W, I, O, plaats, langste_aandeel, tx = B.M, B.W, B.I, B.O, B.plaats, B.langste_aandeel, B.tx
ROOT = B.ROOT

AT = {"H": 1.008, "C": 12.01, "N": 14.01, "O": 16.00, "S": 32.07}


def mm(f):
    """molecuulmassa uit formule als 'C2H6O'"""
    return sum(AT[s] * int(n or 1) for s, n in re.findall(r'([A-Z][a-z]?)(\d*)', f))


def nl(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")


def kortste_aandeel(vr):
    mcs = [v for v in vr if v["type"] == "mc"]
    return sum(all(len(o) > len(v["opties"][v["antwoord"]]) for i, o in enumerate(v["opties"]) if i != v["antwoord"]) for v in mcs), len(mcs)


def paar(p, v):
    v["_p"] = p
    return v


# ---------- berekeningen ----------
c2h6o = mm("C2H6O"); assert nl(c2h6o) == "46,07"
h2s = mm("H2S"); h2s_som = AT["H"] + AT["S"]; h2s_prod = 2 * AT["H"] * AT["S"]
n2o = mm("N2O"); assert nl(n2o) == "44,02"
h_pct = 2 * AT["H"] / mm("H2O") * 100
h_pct_half = AT["H"] / mm("H2O") * 100
o_pct = AT["O"] / mm("H2O") * 100
at_h2so4_2 = 2 * (2 + 1 + 4)
o_in_3h2so4 = 3 * 4
gem = 0.9 * 20 + 0.1 * 22; gem_simpel = (20 + 22) / 2
c14_n = 14 - 6
massagetal_p = 15 + 16
al_massa = 25 * 2.7
dichtheid_fe = 15.8 / 2.0
massa_olie = 400 * 0.75
k85 = 85 + 273
na23_n = 23 - 11

EXAMENS = {
80: ("Toets 80 — Gemengd H1 + H2 (A)", "🔀", [
    # ---- H2 §2.3 (7)
    paar("2.3", M("Hoe heet {N2O3} volgens de systematische naamgeving?", "Distikstoftrioxide",
      ["Tristikstofdioxide", "Stikstoftrioxide", "Monostikstofdistrioxide"],
      "Twee stikstofatomen (di) en drie zuurstofatomen (tri); de eerste atoomsoort krijgt alleen een voorvoegsel als er meer dan één is (§2.3).")),
    paar("2.3", M("Wat is de formule van difosforpentaoxide?", "{P2O5}", ["{P5O2}", "{PO5}", "{P2O}"],
      "Di = 2 fosforatomen, penta = 5 zuurstofatomen: P₂O₅ (§2.3).")),
    paar("2.3", M(f"Wat is de molecuulmassa van {{H2S}} (H = 1,008 u; S = 32,07 u)?", f"{nl(h2s)} u",
      [f"{nl(h2s_som)} u", f"{nl(h2s_prod)} u", f"{nl(h2s * 2)} u"],
      f"Index 2 bij H meetellen en optellen, niet vermenigvuldigen: 2 × 1,008 + 32,07 = {nl(h2s)} u.")),
    paar("2.3", M("Hoeveel atomen zitten er in totaal in 2 {H2SO4}?", str(at_h2so4_2), ["7", "9", "16"],
      "De coëfficiënt 2 vermenigvuldigt de hele formule: 2 × (2 + 1 + 4) = 14 atomen.")),
    paar("2.3", W("{NO2} heet monostikstofdioxide.", False, "De eerste atoomsoort krijgt geen 'mono': stikstofdioxide.")),
    paar("2.3", I("Wat is de molecuulmassa van {C2H6O} (C = 12,01 u; H = 1,008 u; O = 16,00 u)? ____ u", nl(c2h6o),
      f"2 × 12,01 + 6 × 1,008 + 16,00 = {nl(c2h6o)} u.", 0.01)),
    paar("2.3", O("Bij welke atoomsoort in een systematische naam laat je 'mono' weg?", "eerste",
      "Bij de eerste atoomsoort.", "Koolstofdioxide, niet monokoolstofdioxide (§2.3).")),
    # ---- H2 §2.4 (3)
    paar("2.4", M("Welke bewering over de massa van deeltjes in een atoom klopt?",
      "Een proton en een neutron wegen elk ongeveer 1 u en een elektron wegt afgerond 0 u",
      ["Een elektron wegt ongeveer evenveel als een proton", "Een proton wegt ongeveer 1 kg en een neutron 0 kg", "Een neutron wegt afgerond 0 u en een proton 1 u"],
      "Protonen en neutronen zijn zwaar (±1 u), elektronen verwaarloosbaar licht (§2.4).")),
    paar("2.4", W("Het massagetal van een atoom is gelijk aan het aantal protonen.", False,
      "Massagetal = protonen + neutronen; het aantal protonen is het atoomnummer.")),
    paar("2.4", I(f"Koolstof (atoomnummer 6) heeft de isotoop C-14. Het aantal neutronen in een C-14-atoom is ____.", str(c14_n),
      f"14 − 6 = {c14_n} neutronen.")),
    # ---- H2 §2.2, §2.1
    paar("2.2", M("Welke van deze stoffen is een verbinding?", "Ammoniak ({NH3})",
      ["Stikstof ({N2})", "Waterstof ({H2})", "Chloor ({Cl2})"], "Alleen ammoniak heeft moleculen met meer dan één atoomsoort (§2.2).")),
    paar("2.1", W("Op microniveau liggen de moleculen in een vloeistof tegen elkaar aan, maar ze kunnen langs elkaar schuiven.", True,
      "Daardoor is een vloeistof vervormbaar maar nauwelijks samendrukbaar (§2.1).")),
    # ---- H1 (8)
    paar("1.4", M("Waaruit bestaat nevel?", "Vloeistofdruppeltjes fijn verdeeld in een gas",
      ["Vaste deeltjes fijn verdeeld in een gas", "Gasbelletjes fijn verdeeld in een vloeistof", "Vloeistofdruppeltjes fijn verdeeld in een andere vloeistof"],
      "Nevel = vloeistof in gas; rook = vaste stof in gas (§1.4).")),
    paar("1.4", M("Een schoonmaakmiddel is agressiever dan azijn (pH 3). Welke pH kan het middel hebben?", "pH 1", ["pH 5", "pH 7", "pH 9"],
      "Hoe zuurder, hoe lager de pH en hoe agressiever; pH 1 is zuurder dan pH 3.")),
    paar("1.4", M("Waarvoor gebruik je een emulgator?", "Om twee vloeistoffen goed gemengd te laten blijven",
      ["Om een emulsie in een oplossing te veranderen", "Om de pH van een mengsel te verlagen", "Om een troebel mengsel helder te maken"],
      "Een emulgator houdt de druppeltjes verdeeld; het mengsel blijft een troebele emulsie.")),
    paar("1.4", W("Een suspensie is een troebel mengsel van twee vloeistoffen.", False,
      "Dat is een emulsie; een suspensie is een vaste stof in een vloeistof.")),
    paar("1.3", M(f"Wat is 85 °C in kelvin?", f"{k85} K", [f"{273 - 85} K", f"−{273 - 85} K", "273 K"], "Tel 273 op: 85 + 273 = 358 K.")),
    paar("1.3", W("Een smeltpunt van 250 K ligt onder 0 °C.", True, "250 − 273 = −23 °C.")),
    paar("1.1", W("Het smeltpunt van een zuivere stof is bij 1 g en bij 1 kg hetzelfde.", True,
      "Een stofeigenschap hangt niet af van de hoeveelheid.")),
    paar("1.1", I("Een ijzeren spijker weegt 15,8 g en heeft een inhoud van 2,0 cm³. Wat is de dichtheid in g/cm³? <i>(Alleen het getal.)</i>",
      nl(dichtheid_fe, 1) + "|" + f"{dichtheid_fe:.1f}", f"15,8 / 2,0 = {nl(dichtheid_fe, 1)} g/cm³.")),
]),
81: ("Toets 81 — Gemengd H1 + H2 (B)", "🧩", [
    # ---- H2 §2.4 (6)
    paar("2.4", M("Welke notatie hoort bij de isotoop zuurstof-17 (atoomnummer 8)?", "[17,8]O", ["[8,17]O", "[17,9]O", "[9,8]O"],
      "Massagetal linksboven (17), atoomnummer linksonder (8).")),
    paar("2.4", M("Wat hebben alle isotopen van waterstof gemeenschappelijk?", "Het aantal protonen", ["Het aantal neutronen", "Het massagetal", "De massa van het atoom"],
      "Isotopen verschillen alleen in neutronen; atoomnummer (protonen) is gelijk.")),
    paar("2.4", M("Een atoomsoort bestaat voor 90% uit atomen van 20 u en voor 10% uit atomen van 22 u. Wat is de relatieve atoommassa?", f"{nl(gem, 1)} u",
      [f"{nl(gem_simpel, 1)} u", "20,0 u", "22,2 u"], f"Gewogen gemiddelde: 0,90 × 20 + 0,10 × 22 = {nl(gem, 1)} u, niet het gewone gemiddelde.")),
    paar("2.4", W("Een proton en een elektron hebben dezelfde massa.", False, "Een proton weegt ongeveer 1 u, een elektron afgerond 0 u.")),
    paar("2.4", W("Een elektron heeft een massa van afgerond 0 u.", True, "Elektronen zijn veel lichter dan protonen en neutronen.")),
    paar("2.4", I("Een neutraal atoom heeft massagetal 40 en 21 neutronen. Het atoomnummer is ____.", str(40 - 21), "40 − 21 = 19 protonen = atoomnummer.")),
    # ---- H2 §2.3 (3)
    paar("2.3", M("Wat is de formule van de stof stikstof (niet van het losse atoom)?", "{N2}", ["N", "{N2O}", "{NH3}"], "Stikstof bestaat uit moleculen met twee atomen: N₂ (tabel 2.22).")),
    paar("2.3", I("Hoeveel zuurstofatomen zitten er in 3 {H2SO4}? ____", str(o_in_3h2so4), "3 × 4 = 12 (coëfficiënt × index).")),
    paar("2.3", O("Wat betekent de 3 en wat betekent de 2 in 3 {H2O}?", "molecu",
      "De 3 is de coëfficiënt (drie moleculen), de 2 is de index (twee waterstofatomen per molecuul).", "§2.3.")),
    # ---- H2 §2.2 (2), §2.1 (1)
    paar("2.2", M("Welke twee symbolen horen bij zilver en goud?", "Ag en Au", ["Au en Ag", "Zi en Go", "Ag en Gd"], "Ag (argentum) = zilver, Au (aurum) = goud (tabel 2.13).")),
    paar("2.2", M("Welke symbolen horen bij kalium en calcium?", "K en Ca", ["Ka en C", "Ca en K", "K en Cl"], "Kalium = K (kalium), calcium = Ca (tabel 2.13).")),
    paar("2.1", W("Gasmoleculen zitten ver uit elkaar en bewegen snel.", True, "Dat kenmerkt de gasfase (§2.1).")),
    # ---- H1 (8)
    paar("1.1", M("Een dichtheid van 2,7 g/cm³ is gelijk aan …", "2700 kg/m³", ["2,7 kg/m³", "0,0027 kg/m³", "27 kg/m³"], "× 1000: g/cm³ → kg/m³.")),
    paar("1.1", W("Een kleine en een grote hoeveelheid van dezelfde zuivere stof hebben dezelfde dichtheid.", True, "Dichtheid is massa per volume en een stofeigenschap.")),
    paar("1.1", I("Benzine heeft een dichtheid van 0,75 g/mL. Hoeveel gram weegt 400 mL benzine? ____ g", f"{massa_olie:.0f}", f"0,75 × 400 = {massa_olie:.0f} g.")),
    paar("1.3", M("Hoe heet de faseverandering stof X (s) → stof X (g)?", "Sublimeren", ["Verdampen", "Smelten", "Rijpen"], "Vast → gas heet sublimeren; gas → vast is rijpen.")),
    paar("1.3", W("Tijdens het koken van een zuivere stof stijgt de temperatuur steeds verder.", False, "Tijdens het koken blijft de temperatuur gelijk (kookpunt).")),
    paar("1.4", M("Waarom is een emulsie troebel?", "De druppeltjes van de ene vloeistof in de andere zijn zo groot dat het licht niet doorgelaten wordt",
      ["De deeltjes zijn zo klein dat ze het licht tegenhouden", "Er zit een gas opgelost in de vloeistof", "De twee vloeistoffen reageren tot een nieuwe stof"],
      "Bij een oplossing zijn de deeltjes klein; bij een emulsie zijn de druppeltjes groot.")),
    paar("1.4", M("Wat is rook volgens het boek?", "Een vaste stof fijn verdeeld in een gas",
      ["Een vloeistof fijn verdeeld in een gas", "Een gas fijn verdeeld in een vaste stof", "Een vaste stof opgelost in een vloeistof"], "Rook: vast in gas; nevel: vloeistof in gas; schuim: gas in vast/vloeistof.")),
    paar("1.4", W("Een oplossing is altijd kleurloos, want je kunt er doorheen kijken.", False, "Een oplossing is helder, maar kan een kleur hebben.")),
]),
82: ("Toets 82 — Gemengd H1 + H2 (C)", "🎯", [
    # ---- H2 §2.3 (4)
    paar("2.3", M("Wat is de formule van dichloormonoxide?", "{Cl2O}", ["{ClO2}", "{Cl2O2}", "{ClO}"], "Di = 2 chlooratomen, mono = 1 zuurstofatoom.")),
    paar("2.3", M("Wat is het massapercentage waterstof in water (H = 1,008 u; O = 16,00 u)?", f"{nl(h_pct)}%",
      [f"{nl(h_pct_half)}%", f"{nl(o_pct)}%", "33,33%"], f"2 × 1,008 / 18,016 × 100% = {nl(h_pct)}%.")),
    paar("2.3", W("In 3 {H2O} zitten drie waterstofatomen.", False, "3 × 2 = 6 waterstofatomen.")),
    paar("2.3", I("Wat is de molecuulmassa van {N2O} (N = 14,01 u; O = 16,00 u)? ____ u", nl(n2o), f"2 × 14,01 + 16,00 = {nl(n2o)} u.", 0.01)),
    # ---- H2 §2.4 (4)
    paar("2.4", M("In de natuur is ongeveer 75% van de chlooratomen Cl-35 en de rest Cl-37. Welk deel is Cl-37?", "Ongeveer een kwart",
      ["Ongeveer driekwart", "Precies de helft", "Alle chlooratomen"], "100% − 75% = 25%.")),
    paar("2.4", M("Welke deeltjes zitten in de atoomkern?", "Protonen en neutronen", ["Protonen en elektronen", "Neutronen en elektronen", "Alleen protonen"],
      "De kern bevat protonen en neutronen; de elektronen zitten in de wolk eromheen.")),
    paar("2.4", W("Een neutraal atoom met atoomnummer 11 heeft 11 elektronen.", True, "Aantal elektronen = aantal protonen in een neutraal atoom.")),
    paar("2.4", I(f"Natrium-23 heeft atoomnummer 11. Het aantal neutronen is ____.", str(na23_n), f"23 − 11 = {na23_n}.")),
    # ---- H2 §2.2 (2), §2.1 (2)
    paar("2.2", M("Welke van deze atoomsoorten is een edelgas?", "Neon", ["Fluor", "Natrium", "Zwavel"], "Neon staat in groep 18, de edelgassen.")),
    paar("2.2", O("Wat hebben atoomsoorten in dezelfde groep van het periodiek systeem gemeen?", "eigenschappen",
      "Ze hebben vergelijkbare eigenschappen.", "§2.2.")),
    paar("2.1", M("Welke bewering beschrijft de stof op microniveau?", "De geurmoleculen bewegen vrij tussen de luchtmoleculen",
      ["De vloeistof is troebel en heeft een gele kleur", "Het poeder lost helder op in warm water", "De stof smelt bij een temperatuur van 63 °C"],
      "Moleculen kun je niet zien: dat is microniveau; de rest neem je waar.")),
    paar("2.1", W("In een vaste stof bewegen de moleculen vrij langs elkaar.", False, "In een vaste stof trillen de moleculen op hun plek.")),
    # ---- H1 (8)
    paar("1.4", M("In welk product zijn olie en water gemengd tot een emulsie?", "Mayonaise", ["Rook", "Limonade zonder vruchtvlees", "Sinaasappelsap met vruchtvlees"],
      "Mayonaise is olie in water met eigeel als emulgator.")),
    paar("1.4", M("Welke oplossing is het basischst?", "pH 12", ["pH 9", "pH 7", "pH 3"], "Hoe hoger de pH boven 7, hoe basischer.")),
    paar("1.4", W("Gootsteenontstopper heeft een lagere pH dan azijn.", False, "Gootsteenontstopper is basisch (pH hoger dan 7); azijn is zuur.")),
    paar("1.3", M("Welke van deze temperaturen is het laagst?", "260 K", ["−10 °C", "−5 °C", "0 °C"], "260 K = −13 °C; zet alles om naar dezelfde schaal.")),
    paar("1.3", W("Een stof met een smeltpunt van 300 K is bij 20 °C vast.", True, "20 °C = 293 K, lager dan het smeltpunt van 300 K.")),
    paar("1.3", I("Je schrijft stof Z (l) → stof Z (s). Hoe heet deze faseverandering? ____", "stollen|stolling|het stollen", "Vloeibaar → vast = stollen.")),
    paar("1.1", M("Een blokje van 25 cm³ is gemaakt van aluminium (2,7 g/cm³). Wat is de massa?", f"{nl(al_massa, 1)} g",
      [f"{nl(25 / 2.7, 1)} g", f"{nl(25 + 2.7, 1)} g", f"{nl(2.7 / 25)} g"], "massa = dichtheid × volume = 2,7 × 25 = 67,5 g.")),
    paar("1.1", W("Een stof met een grotere massa heeft altijd een grotere dichtheid.", False, "Dichtheid hangt ook van het volume af.")),
]),
}


def main():
    for nr, (titel, icoon, vr) in EXAMENS.items():
        t = [v["type"] for v in vr]
        assert len(vr) == 20 and (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (10, 6, 3, 1), (nr, t)
        assert sum(v["type"] == "waaronwaar" and v["antwoord"] is False for v in vr) >= 3, nr
        h2 = [v["_p"] for v in vr if v["_p"].startswith("2")]; assert len(h2) == 12, (nr, len(h2))
        for seed in range(500):
            rng = random.Random(f"sch_gem_20261120_{nr}_{seed}")
            plaatsed = plaats([dict(v) for v in vr], rng)
            n, tot = langste_aandeel(plaatsed); k, _ = kortste_aandeel(plaatsed)
            if n / tot <= 0.4 and k / tot <= 0.3:
                break
        else:
            raise SystemExit(f"{nr}: geen goede plaatsing")
        # open-vragen en I/W krijgen zelfde volgorde; mc-plaatsing willekeurig → daarna verdelen (zwak eerst niet nodig)
        verdeling = {}
        for v in vr: verdeling[v["_p"]] = verdeling.get(v["_p"], 0) + 1
        for i, v in enumerate(plaatsed, 1):
            v.pop("_p"); plaatsed[i - 1] = {"id": f"sch-h2-{nr}_v{i}", **v}
        ex = {"id": f"ex-h3-sch-h2-{nr}", "titel": titel, "vak": "Scheikunde · HAVO 3 (H2)", "hoofdstuk": 2,
              "paragraaf": "mix", "icoon": icoon, "duurMin": 25, "vragen": plaatsed}
        with open(os.path.join(ROOT, f"examen_h2_{nr}.js"), "w", encoding="utf-8") as f:
            f.write("/* Examen conform DURU ENGINE_SPEC (HAVO 3 Scheikunde H2) — gegenereerd door tools/gen_scheikunde_gemengd_20261120.py */\n")
            f.write("DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_h2_{nr}: langste {n}/{tot}, kortste {k}/{tot}; § {dict(sorted(verdeling.items()))}")


if __name__ == "__main__":
    main()
