#!/usr/bin/env python3
"""Natuurkunde HAVO 3 · H1 — gemengde proeftoetsen 120–122 (2026-11-20).

Doel: elke toets dekt §1.1–§1.5 (alles H1), met nadruk op de laatste fouten van Duru (proefwerk 115–119,
herhaling 113–114): v = s/t + (v,t)-oppervlakte, Fres = m·a (delen/keer), remweg ~ v² / stopafstand,
omrekenen (km/h↔m/s, g→kg, kJ↔J, min→h), arbeid (0 J / teken / F = W:s).
Verdeling per toets (§1.1/1.2/1.3/1.4/1.5): 120 = 2/6/4/4/4 · 121 = 3/4/4/6/3 · 122 = 2/4/5/3/6.
Alle getallen worden hier berekend. Schrijft havo3/natuurkunde/js/data/examen_120..122.js.
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_economie_toetsen_96_115 import M, W, I, O, plaats, langste_aandeel, kortste_aandeel  # noqa: E402
from gen_natuurkunde_h1_zwakte_86_91 import EEN_ZIN, ROOT, graf, nl  # noqa: E402

G = 9.81


def f(x, d=None):
    """Nederlandse notatie; d = vaste decimalen; duizendtallen >= 10000 met spatie."""
    s = f"{x:,.{d}f}" if d is not None else f"{x:,g}"
    if d is None and abs(x) >= 1e6:
        s = f"{x:,.0f}"
    return s.replace(",", " ").replace(".", ",") if abs(x) >= 10000 else s.replace(",", "").replace(".", ",")


def ant(x, unit="", dec=()):
    """Antwoordvarianten voor invul: komma, punt, met eenheid, evt. afrondingen."""
    waarden = [x] + [round(x, d) if d else round(x) for d in dec]
    out = []
    for w in waarden:
        w = int(w) if float(w).is_integer() else w
        for s in (nl(w), str(w), (f"{w:,}".replace(",", " ") if abs(w) >= 1000 else None)):
            if s and s not in out:
                out.append(s)
                if unit:
                    out.append(f"{s} {unit}")
    return "|".join(out)


def opp(punten):
    """Oppervlakte onder een (t,v)-lijn (trapezium-regel)."""
    return sum((punten[i + 1][0] - punten[i][0]) * (punten[i][1] + punten[i + 1][1]) / 2 for i in range(len(punten) - 1))


def remweg(v, a):
    t = v / a
    return v / 2 * t


# ---------------------------------------------------------------- toets 120
def t120():
    q = []
    # §1.1 (2)
    m = 0.750
    q.append(I(f"Je koopt een zakje rijst van 750 gram. Wat is de zwaartekracht op dit zakje in N (g = 9,81 N/kg)? Reken gram eerst om naar kg.",
               ant(m * G, "N", (1, 2)), f"750 g = 0,750 kg. Fz = m · g = 0,750 · 9,81 ≈ {f(m*G,1)} N. Wie 750 · 9,81 doet, vergeet g → kg en krijgt 7357 N."))
    q.append(W("Een bromfiets rijdt met constante snelheid over een vlakke weg. De motorkracht is dan groter dan de wrijvingskracht.",
               False, "Onwaar: constante snelheid betekent Fres = 0 N. De motorkracht en de wrijvingskracht zijn dan precies even groot."))
    # §1.2 (6)
    s_, t_ = 6.3, 18 / 60
    q.append(I(f"Sven legt op zijn fiets {f(s_)} km af in 18 minuten tijd. Hoeveel km/h is zijn gemiddelde snelheid?",
               ant(s_ / t_, "km/h"), f"18 min = {f(t_)} h. v = s : t = {f(s_)} : {f(t_)} = {f(s_/t_)} km/h. Niet 6,3 · 18 = 113 km/h: dat is delen vergeten."))
    v = 144
    q.append(M(f"Een hogesnelheidstrein rijdt {v} km/h. Hoeveel m/s is dat?",
               f"{f(v/3.6)} m/s", [f"{f(v*3.6)} m/s", f"{f(v/36)} m/s", f"{v} m/s"],
               f"Van km/h naar m/s deel je door 3,6: {v} : 3,6 = {f(v/3.6)} m/s. {f(v*3.6)} m/s is keer 3,6: de verkeerde kant op."))
    pts = [(0, 0), (5, 12), (9, 12), (12, 0)]
    q.append(I("Bereken de afgelegde afstand in meters tijdens de 12 seconden van dit (v,t)-diagram." + graf("v", [("", pts)], 12, 14),
               ant(opp(pts), "m"), "Afstand = oppervlakte onder de lijn. Driehoek 0–5 s: ½ · 5 · 12 = 30 m. Rechthoek 5–9 s: 4 · 12 = 48 m. Driehoek 9–12 s: ½ · 3 · 12 = 18 m. Samen 96 m."))
    q.append(M("Dit is een (s,t)-diagram. Wat doet het voorwerp tussen 10 s en 20 s?" + graf("s", [("", [(0, 0), (10, 40), (20, 40), (30, 100)])], 30, 100),
               "Het staat stil", ["Het beweegt met constante snelheid", "Het versnelt", "Het remt af"],
               "In een (s,t)-diagram staat de afstand omhoog. Horizontaal = de afstand verandert niet = stilstaan. (In een (v,t)-diagram zou horizontaal juist constante snelheid zijn.)"))
    q.append(W("Emma wacht onderweg 2 minuten bij een stoplicht. Die 2 minuten tellen mee in de totale tijd, dus haar gemiddelde snelheid wordt lager.",
               True, "Waar: v_gem = totale afstand : totale tijd, en de wachttijd hoort bij die totale tijd."))
    v8, t8 = 15, 8.0
    q.append(I(f"Een bromfiets versnelt eenparig uit stilstand in {f(t8)} s tot {v8} m/s. Hoeveel meter legt hij in die tijd af?",
               ant(v8 / 2 * t8, "m"), f"v_gem = (0 + {v8}) : 2 = {f(v8/2)} m/s. s = v_gem · t = {f(v8/2)} · {f(t8)} = {f(v8/2*t8)} m. Niet {v8} · {f(t8)} = {f(v8*t8)} m: dan vergeet je de helft."))
    # §1.3 (4)
    m3, v3, t3 = 1200, 72 / 3.6, 6.0
    q.append(I(f"Een auto van {m3} kg gaat in {f(t3)} s van stilstand naar 72 km/h. Bereken de resulterende kracht in N.",
               ant(m3 * v3 / t3, "N", (0,)), f"72 km/h = 72 : 3,6 = 20 m/s. a = Δv : t = 20 : {f(t3)} ≈ {f(v3/t3,2)} m/s². Fres = m · a = {m3} · {f(v3/t3,2)} ≈ {f(m3*v3/t3)} N."))
    m4, Fv, Fw = 50, 180, 30
    q.append(M(f"Een kar van {m4} kg wordt met {Fv} N vooruit geduwd. De wrijving is {Fw} N. Hoe groot is de versnelling?",
               f"{f((Fv-Fw)/m4)} m/s²", [f"{f(Fv/m4)} m/s²", f"{f((Fv+Fw)/m4)} m/s²", f"{f((Fv-Fw)*m4)} m/s²"],
               f"Eerst Fres = {Fv} − {Fw} = {Fv-Fw} N. Dan a = Fres : m = {Fv-Fw} : {m4} = {f((Fv-Fw)/m4)} m/s². {f(Fv/m4)}: wrijving vergeten; {f((Fv-Fw)*m4)}: vermenigvuldigd in plaats van gedeeld."))
    q.append(W("Bij dezelfde resulterende kracht is de versnelling 2 keer zo groot als de massa 2 keer zo groot is.",
               False, "Onwaar: a = Fres : m. Een grotere massa geeft een kleinere versnelling: bij 2 keer zo grote massa is a de helft."))
    q.append(M("Een lift trekt op naar boven. Vergelijk de kracht in de kabel met de zwaartekracht op de lift.",
               "Groter dan de zwaartekracht", ["Even groot als de zwaartekracht", "Kleiner dan de zwaartekracht", "Nul"],
               "De lift versnelt omhoog, dus Fres wijst omhoog: de kabelkracht is groter dan Fz. Pas bij constante snelheid zijn ze even groot."))
    # §1.4 (4)
    q.append(M("Een auto rijdt 3 keer zo snel (zelfde weg, zelfde remmen). Wat gebeurt er met de remweg?",
               "9 keer zo lang", ["3 keer zo lang", "6 keer zo lang", "Even lang"],
               "De remweg hangt af van v²: 3 keer zo snel → 3 · 3 = 9 keer zo lange remweg."))
    v5, a5 = 90 / 3.6, 5.0
    q.append(I(f"Een automobilist remt met {f(a5)} m/s² vanaf 90 km/h. Welke afstand legt hij nog af tot hij stilstaat?",
               ant(remweg(v5, a5), "m"), f"90 km/h = {f(v5)} m/s. Remtijd t = v : a = {f(v5)} : {f(a5)} = {f(v5/a5)} s. v_gem = {f(v5/2,1)} m/s. Remweg = {f(v5/2,1)} · {f(v5/a5)} = {f(remweg(v5,a5),1)} m. Niet {f(v5)} · {f(v5/a5)}: dan vergeet je de helft."))
    v6, tr, a6 = 54 / 3.6, 0.8, 7.5
    sr = v6 * tr
    q.append(I(f"Een automobilist rijdt 54 km/h, heeft een reactietijd van {f(tr)} s en remt met {f(a6)} m/s². Bereken de stopafstand in m.",
               ant(sr + remweg(v6, a6), "m"), f"54 km/h = {f(v6)} m/s. Reactieafstand = {f(v6)} · {f(tr)} = {f(sr)} m. Remtijd = {f(v6)} : {f(a6)} = {f(v6/a6)} s, remweg = {f(v6/2,1)} · {f(v6/a6)} = {f(remweg(v6,a6))} m. Stopafstand = {f(sr)} + {f(remweg(v6,a6))} = {f(sr+remweg(v6,a6))} m."))
    q.append(W("Wie de remweg wil weten, telt de reactieafstand bij de stopafstand op.",
               False, "Onwaar: stopafstand = reactieafstand + remweg. De remweg is dus stopafstand − reactieafstand: aftrekken, niet optellen."))
    # §1.5 (4)
    F7, s7 = 175, 6.0
    q.append(I(f"Een verhuizer sleept een kist met constante snelheid {f(s7)} m over de vloer. De wrijvingskracht is {F7} N. Hoeveel arbeid verricht hij in J?",
               ant(F7 * s7, "J"), f"Constante snelheid → zijn kracht is even groot als de wrijving: F = {F7} N. W = F · s = {F7} · {f(s7)} = {f(F7*s7)} J."))
    F8, s8 = 15, 12
    q.append(I(f"Tegen een weerstand van {F8} N trapt een wielrenner {s8} km ver. Bereken de verrichte arbeid in kJ.",
               ant(F8 * s8, "kJ"), f"{s8} km = {s8*1000} m. W = F · s = {F8} · {s8*1000} = {f(F8*s8*1000)} J = {F8*s8} kJ. Vergeet je km → m, dan krijg je {F8*s8} J: duizend keer te klein."))
    q.append(M("Je draagt een rugzak 20 m horizontaal. Hoeveel arbeid verricht je spierkracht (die wijst omhoog) daarbij?",
               "0 J, want de kracht staat loodrecht op de beweging", ["Veel, want de rugzak is zwaar", "Positieve arbeid", "Negatieve arbeid"],
               "De spierkracht wijst omhoog, de beweging is horizontaal: kracht loodrecht op de verplaatsing → W = 0 J."))
    m9, h9 = 25, 3.0
    q.append(O("Een gewichtheffer houdt een halter 4 s vast zonder te bewegen. Waarom is zijn arbeid 0 J?" + EEN_ZIN,
               ["verplaatsing/s = 0/0 m/geen afstand/geen beweging/niet verplaatst"], 1,
               "De halter beweegt niet (s = 0 m), dus W = F · s = 0 J.", "W = F · s en de verplaatsing is 0 m, dus de arbeid is 0 J."))
    return q


# ---------------------------------------------------------------- toets 121
def t121():
    q = []
    # §1.1 (3)
    m = 0.450
    q.append(M("Een voetbal heeft een massa van 450 g. Hoe groot is de zwaartekracht (g = 9,81 N/kg)?",
               f"{f(m*G,2)} N", [f"{f(m*1000*G)} N", f"{f(m/G,4)} N", f"{f(m,2)} N"],
               f"450 g = 0,450 kg. Fz = m · g = 0,450 · 9,81 ≈ {f(m*G,2)} N. {f(m*1000*G)} N: niet omgerekend; {f(m/G,3)} N: gedeeld door g."))
    q.append(O("Een trein rijdt met een steeds even grote snelheid over recht spoor. Hoeveel N bedraagt Fres?" + EEN_ZIN,
               ["0/nul/geen/evenwicht/gelijk/even groot"], 1, "0 N: de motorkracht en de weerstand zijn even groot.",
               "Constante snelheid → Fres = 0 N, dus de krachten heffen elkaar op."))
    Fz = 49
    q.append(I(f"De zwaartekracht op een zak aardappelen is {Fz} N (g = 9,81 N/kg). Hoeveel kg is de zak?",
               ant(Fz / G, "kg", (1, 2)), f"m = Fz : g = {Fz} : 9,81 ≈ {f(Fz/G,1)} kg. Vermenigvuldigen geeft {f(Fz*G)} kg: een zak aardappelen zo zwaar als een auto kan niet."))
    # §1.2 (4)
    s1, t1 = 9.0, 45 / 60
    q.append(I(f"Een skiër legt {f(s1)} km af in 45 minuten. Bereken zijn gemiddelde snelheid in km/h.",
               ant(s1 / t1, "km/h"), f"45 min = {f(t1)} h. v = s : t = {f(s1)} : {f(t1)} = {f(s1/t1)} km/h. Niet 9,0 : 45 = 0,2: min → h vergeten."))
    q.append(M("Wat doet het voorwerp in dit (v,t)-diagram?" + graf("v", [("", [(0, 12), (8, 0)])], 8, 14),
               "Hij remt geleidelijk af", ["Het beweegt met constante snelheid", "Het versnelt", "Het staat stil"],
               "In een (v,t)-diagram staat de snelheid omhoog. De lijn daalt van 12 naar 0 m/s: de snelheid wordt steeds kleiner → afremmen."))
    pts = [(0, 0), (4, 8), (10, 8)]
    q.append(I("Welke weg (in m) heeft de auto na 10 s afgelegd? Gebruik de oppervlakte onder de lijn." + graf("v", [("", pts)], 10, 10),
               ant(opp(pts), "m"), "Afstand = oppervlakte. Driehoek 0–4 s: ½ · 4 · 8 = 16 m. Rechthoek 4–10 s: 6 · 8 = 48 m. Samen 64 m."))
    q.append(W("Wil je de afstand uit een (v,t)-diagram halen, dan bereken je de oppervlakte onder de lijn.",
               True, "Waar: s = v · t is een rechthoek met breedte t en hoogte v. Dus oppervlakte onder de lijn = afstand."))
    # §1.3 (4)
    v2, v1, t2 = 90 / 3.6, 36 / 3.6, 6.0
    q.append(M(f"Een auto trekt op van 36 km/h naar 90 km/h in {f(t2)} seconden. Wat is de versnelling?",
               f"{f((v2-v1)/t2)} m/s²", [f"{f((90-36)/t2)} m/s²", f"{f(v2/t2,1)} m/s²", f"{f((v2-v1)*t2)} m/s²"],
               f"Eerst alles in m/s: 36 km/h = 10 m/s, 90 km/h = 25 m/s. Δv = 15 m/s. a = Δv : t = 15 : {f(t2)} = {f((v2-v1)/t2)} m/s². {f((90-36)/t2)}: km/h niet omgerekend; {f(v2/t2,1)}: begin-snelheid vergeten; {f((v2-v1)*t2)}: vermenigvuldigd."))
    m3, Fv, Fw = 90, 135, 45
    q.append(I(f"Iemand duwt een zware bakfiets (totaal {m3} kg) met {Fv} N vooruit, terwijl {Fw} N wrijving tegenwerkt. Hoeveel is a in m/s²?",
               ant((Fv - Fw) / m3, "m/s²"), f"Fres = {Fv} − {Fw} = {Fv-Fw} N. a = Fres : m = {Fv-Fw} : {m3} = {f((Fv-Fw)/m3)} m/s²."))
    q.append(W("Een hardloper loopt steeds 3,0 m/s. Dan is zijn versnelling ook 3,0 m/s².",
               False, "Onwaar: versnelling = verandering van snelheid per seconde. Bij constante snelheid verandert er niets: a = 0 m/s²."))
    q.append(M("Massa en Fres worden allebei 3 keer zo groot. Wat doet de versnelling a?",
               "Die blijft even groot", ["Ook 3 keer zo groot", "9 keer zo groot, want 3 · 3", "3 keer zo klein"],
               "a = Fres : m. Teller en noemer worden allebei 3 keer zo groot: 3 : 3 = 1. De versnelling verandert niet."))
    # §1.4 (6)
    v4a, v4b, r4 = 30, 90, 6.0
    q.append(I(f"Bij {v4a} km/h remt een auto over {f(r4)} m. Over hoeveel meter remt dezelfde auto vanaf {v4b} km/h?",
               ant(r4 * (v4b / v4a) ** 2, "m"), f"{v4b} km/h is {v4b//v4a} keer zo snel → remweg {v4b//v4a}² = {(v4b//v4a)**2} keer zo lang: {f(r4)} · {(v4b//v4a)**2} = {f(r4*(v4b/v4a)**2)} m. Niet {v4b//v4a} keer."))
    v5, a5 = 108 / 3.6, 6.0
    q.append(I(f"Bij 108 km/h trapt een chauffeur op de rem; de vertraging is {f(a5)} m/s². Wat is de remweg in m?",
               ant(remweg(v5, a5), "m"), f"108 km/h = {f(v5)} m/s. Remtijd = {f(v5)} : {f(a5)} = {f(v5/a5)} s. v_gem = {f(v5/2)} m/s. Remweg = {f(v5/2)} · {f(v5/a5)} = {f(remweg(v5,a5))} m."))
    v6, tr, a6 = 36 / 3.6, 1.2, 5.0
    sr = v6 * tr
    q.append(I(f"Een moe geworden bestuurder rijdt 36 km/h, heeft een reactietijd van {f(tr)} s en remt met {f(a6)} m/s². Bereken de stopafstand in m.",
               ant(sr + remweg(v6, a6), "m"), f"36 km/h = {f(v6)} m/s. Reactieafstand = {f(v6)} · {f(tr)} = {f(sr)} m. Remweg = {f(v6/2)} · ({f(v6)} : {f(a6)}) = {f(remweg(v6,a6))} m. Stopafstand = {f(sr)} + {f(remweg(v6,a6))} = {f(sr+remweg(v6,a6))} m."))
    q.append(M("Een bestuurder is moe en reageert langzamer. Welk deel van de stopafstand wordt daardoor groter?",
               "De reactieafstand", ["De remweg", "Allebei evenveel", "Geen van beide, die blijven gelijk"],
               "Reactieafstand = v · reactietijd, dus een langere reactietijd geeft een langere reactieafstand. De remweg hangt van snelheid en remmen af."))
    q.append(M("Twee gelijke auto's botsen even hard. Auto A deukt 0,30 m in, auto B 0,90 m. In welke auto is de kracht kleiner?",
               "In auto B", ["In auto A", "In allebei even groot", "Dat is niet te zeggen"],
               "Bij dezelfde beginsnelheid staat B over een langere afstand (en tijd) stil. Een grotere botstijd/inzakweg geeft een kleinere kracht."))
    q.append(W("Een kreukelzone verlengt de botstijd, daardoor is de kracht op de inzittenden kleiner.",
               True, "Waar: dezelfde Δv in een langere tijd geeft een kleinere vertraging, dus volgens Fres = m · a ook een kleinere kracht."))
    # §1.5 (3)
    q.append(M("Je rolt een bal over een horizontale vloer. Hoeveel arbeid verricht de zwaartekracht daarbij?",
               "0 J, want Fz staat loodrecht op de beweging", ["Positieve arbeid", "Negatieve arbeid", "Evenveel als bij vallen, want Fz blijft gelijk"],
               "Fz wijst omlaag, de bal beweegt horizontaal: kracht loodrecht op de verplaatsing → W = 0 J."))
    F8, s8 = 350, 2.4
    q.append(I(f"Een kar wordt met {F8} N over {f(s8)} km voortgetrokken. Bereken de arbeid in kJ.",
               ant(F8 * s8, "kJ"), f"{f(s8)} km = {f(s8*1000)} m. W = F · s = {F8} · {f(s8*1000)} = {f(F8*s8*1000)} J = {f(F8*s8)} kJ."))
    q.append(W("Een remkracht die een auto afremt verricht negatieve arbeid.",
               True, "Waar: de remkracht werkt tegen de bewegingsrichting in, dus W = F · s is negatief."))
    return q


# ---------------------------------------------------------------- toets 122
def t122():
    q = []
    # §1.1 (2)
    m = 18.5
    q.append(I(f"Bereken Fz in N voor een koffer van {f(m,1)} kg (g = 9,81 N/kg).",
               ant(m * G, "N", (0,)), f"Fz = m · g = {f(m,1)} · 9,81 ≈ {f(m*G)} N."))
    q.append(W("Een voorwerp van 1 kg heeft op aarde ongeveer 10 N zwaartekracht.",
               True, "Waar: Fz = m · g = 1 · 9,81 ≈ 10 N. Handig voor controleren: 1 kg ≈ 10 N."))
    # §1.2 (4)
    v1, t1 = 25, 2.0
    q.append(M(f"Een trein rijdt {f(t1)} minuten lang met een constante snelheid van {v1} m/s. Hoeveel meter legt hij af?",
               f"{f(v1*t1*60)} m", [f"{f(v1*t1)} m", f"{f(v1*60)} m", f"{f(v1*t1*3.6)} m"],
               f"{f(t1)} min = {f(t1*60)} s. s = v · t = {v1} · {f(t1*60)} = {f(v1*t1*60)} m. {f(v1*t1)} m: minuten niet omgerekend; {f(v1*60)} m: maar 1 minuut."))
    s2, t2 = 150, 1.5
    q.append(M(f"Een auto rijdt {s2} km in 1 uur en 30 minuten. Wat is zijn gemiddelde snelheid?",
               f"{f(s2/t2)} km/h", [f"{f(s2/1.3,0)} km/h", f"{f(s2*t2)} km/h", f"{f(s2+30)} km/h"],
               f"1 h 30 min = 1,5 h. v = s : t = {s2} : 1,5 = {f(s2/t2)} km/h. 1 h 30 min is niet 1,3 h: een uur heeft 60 minuten, geen 100."))
    pts = [(0, 0), (6, 10), (14, 10), (16, 0)]
    q.append(I("Een fietser beweegt zoals in dit diagram. Wat is zijn totale verplaatsing in meter na 16 s?" + graf("v", [("", pts)], 16, 12),
               ant(opp(pts), "m"), "Driehoek 0–6 s: ½ · 6 · 10 = 30 m. Rechthoek 6–14 s: 8 · 10 = 80 m. Driehoek 14–16 s: ½ · 2 · 10 = 10 m. Samen 120 m."))
    q.append(W("Wil je een snelheid in m/s uitrekenen, dan reken je de afstand om naar meter en de tijd naar seconden.",
               True, "Waar: m/s = meter per seconde. Dus km → m (· 1000) en min → s (· 60) voordat je deelt."))
    # §1.3 (5)
    m3, a3 = 150, 2.2
    q.append(M(f"Een bromfiets met bestuurder ({m3} kg) trekt op met {f(a3)} m/s². Hoe groot is de resulterende kracht?",
               f"{f(m3*a3)} N", [f"{f(m3/a3,0)} N", f"{f(m3+a3,1)} N", f"{f(m3*a3/10,1)} N"],
               f"Fres = m · a = {m3} · {f(a3)} = {f(m3*a3)} N. Je zoekt de kracht, dus vermenigvuldigen. {f(m3/a3,0)} N is gedeeld."))
    q.append(M("Welke berekening geeft de massa als Fres en a bekend zijn?",
               "m = Fres : a", ["m = Fres · a", "m = a : Fres", "m = Fres − a"],
               "Uit Fres = m · a volgt m = Fres : a. Je deelt de kracht door de versnelling."))
    m5, Fm, Fw = 4000, 9500, 3500
    q.append(I(f"Een vrachtwagen van {m5} kg wordt met een motorkracht van {Fm} N vooruit gedreven. De weerstand is {Fw} N. Bereken de versnelling in m/s².",
               ant((Fm - Fw) / m5, "m/s²"), f"Fres = {Fm} − {Fw} = {Fm-Fw} N. a = Fres : m = {Fm-Fw} : {m5} = {f((Fm-Fw)/m5)} m/s²."))
    m6, a6 = 900, 6.0
    q.append(M(f"Bij het remmen krijgt een auto ({m6} kg) een vertraging van {f(a6)} m/s². Wat is de remkracht?",
               f"{f(m6*a6)} N", [f"{f(m6/a6)} N", f"{f(m6+a6)} N", f"{f(m6*a6/1000,1)} N"],
               f"Fres = m · a = {m6} · {f(a6)} = {f(m6*a6)} N. {f(m6/a6)} N is gedeeld in plaats van vermenigvuldigd."))
    q.append(W("Als de resulterende kracht op een voorwerp 0 N is, staat het voorwerp altijd stil.",
               False, "Onwaar: Fres = 0 N betekent a = 0, dus de snelheid verandert niet. Het voorwerp staat stil óf beweegt met constante snelheid."))
    # §1.4 (3)
    q.append(M("De remweg bij 40 km/h is 8,0 m. Hoe groot is de remweg bij 80 km/h (zelfde auto, zelfde remmen)?",
               "32 m", ["16 m", "64 m", "24 m"],
               "2 keer zo snel → 2² = 4 keer zo lange remweg: 8,0 · 4 = 32 m. 16 m = alleen keer 2."))
    v6, tr, a6 = 72 / 3.6, 0.75, 4.0
    sr = v6 * tr
    q.append(I(f"Een auto rijdt 72 km/h, de reactietijd is {f(tr)} s en de vertraging bij remmen is {f(a6)} m/s². Bereken de stopafstand in m.",
               ant(sr + remweg(v6, a6), "m"), f"72 km/h = {f(v6)} m/s. Reactieafstand = {f(v6)} · {f(tr)} = {f(sr)} m. Remweg = {f(v6/2)} · ({f(v6)} : {f(a6)}) = {f(remweg(v6,a6))} m. Stopafstand = {f(sr)} + {f(remweg(v6,a6))} = {f(sr+remweg(v6,a6))} m."))
    q.append(W("Rijdt iemand twee keer zo snel, dan is de reactieafstand vier keer zo lang.",
               False, "Onwaar: reactieafstand = v · t_reactie, dus 2 keer zo groot. Alleen de remweg wordt 4 keer zo groot (v²)."))
    # §1.5 (6)
    q.append(W("Een skiër glijdt een piste af. Zijn zwaartekracht verricht daarbij positieve arbeid.",
               True, "Waar: de zwaartekracht wijst omlaag en de renner beweegt omlaag, dus kracht en beweging hebben dezelfde richting: W is positief."))
    F2, s2 = 35, 2.0
    q.append(I(f"Op een vlak stuk fietst iemand met constante snelheid; de weerstand is {F2} N. Hoeveel arbeid verricht hij op {f(s2)} km? Geef je antwoord in kJ.",
               ant(F2 * s2, "kJ"), f"Constante snelheid → zijn kracht = weerstand = {F2} N. s = {f(s2)} km = {f(s2*1000)} m. W = {F2} · {f(s2*1000)} = {f(F2*s2*1000)} J = {f(F2*s2)} kJ."))
    m3, h3 = 70, 1.8
    q.append(I(f"Een kist van {m3} kg wordt met constante snelheid {f(h3)} m omhoog gehesen (g = 9,81 N/kg). Hoeveel arbeid verricht de kabelkracht in J?",
               ant(m3 * G * h3, "J", (0,)), f"Constante snelheid → F = Fz = {m3} · 9,81 = {f(m3*G,1)} N. W = F · s = {f(m3*G,1)} · {f(h3)} ≈ {f(m3*G*h3)} J."))
    q.append(M("Bij welke situatie verricht de spierkracht arbeid volgens de natuurkunde?",
               "Een leerling trekt een kar 5 m vooruit", ["Een leerling duwt tegen een muur die niet beweegt",
                "Een leerling draagt een koffer 10 m horizontaal", "Een leerling staat stil met een zware tas"],
               "Arbeid vraagt een kracht én een verplaatsing in (bijna) dezelfde richting. Bij de kar is dat zo; muur en stilstaan: s = 0; koffer dragen: kracht loodrecht op de beweging."))
    W3, s3 = 84, 40
    q.append(I(f"Een kraan verricht {W3} kJ arbeid over een afstand van {s3} m. Hoe groot is de kracht in N?",
               ant(W3 * 1000 / s3, "N"), f"{W3} kJ = {W3*1000} J. F = W : s = {W3*1000} : {s3} = {f(W3*1000/s3)} N."))
    q.append(O("Je draagt een tas 20 m horizontaal. Verricht je spierkracht arbeid? Leg uit." + EEN_ZIN,
               ["loodrecht/haaks/90/niet in de richting/omhoog", "nee/geen/0/nul"], 1,
               "Nee: de kracht wijst omhoog en de beweging is horizontaal (loodrecht), dus W = 0 J.",
               "Kracht loodrecht op de verplaatsing verricht geen arbeid: W = 0 J."))
    return q


EXAMENS = {
    120: ("Toets 120 — Gemengd H1 (A)", "🧩", t120),
    121: ("Toets 121 — Gemengd H1 (B)", "🧩", t121),
    122: ("Toets 122 — Gemengd H1 (C)", "🧩", t122),
}


def main():
    rng = random.Random("natuurkunde_gemengd_20261120")
    for nr in sorted(EXAMENS):
        titel, icoon, fn = EXAMENS[nr]
        vr = fn()
        assert len(vr) == 20, f"examen_{nr}: {len(vr)} vragen"
        t = [v["type"] for v in vr]
        vr = plaats([dict(v) for v in vr], rng)
        n_lang, tot = langste_aandeel(vr)
        n_kort, _ = kortste_aandeel(vr)
        print(f"examen_{nr}: {t.count('mc')} mc / {t.count('waaronwaar')} w-o / {t.count('invul')} invul / "
              f"{t.count('open')} open · langste {n_lang}/{tot}, kortste {n_kort}/{tot}")
        assert n_lang / tot <= 0.4 and n_kort / tot <= 0.4, f"examen_{nr}: juiste optie te vaak langste/kortste"
        ex = {"id": f"ex-h3-natuurkunde-{nr}", "hoofdstuk": 1, "paragraaf": "mix", "titel": titel,
              "vak": "Natuurkunde · HAVO 3 (H1)", "icoon": icoon, "duurMin": 30, "vragen": vr}
        kop = (f"/* =========================================================\n   Duru's Natuurkunde (HAVO 3) — {titel}\n"
               f"   Gegenereerd door tools/gen_natuurkunde_gemengd_20261120.py\n"
               f"   ========================================================= */\n")
        with open(os.path.join(ROOT, f"examen_{nr}.js"), "w", encoding="utf-8") as fh:
            fh.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")


if __name__ == "__main__":
    main()
