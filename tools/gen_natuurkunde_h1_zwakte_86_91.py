#!/usr/bin/env python3
"""Natuurkunde HAVO 3 · H1 — 6 zwakte-toetsen 86–91 (Opus, 2026-11-14).

Bron: Duru's pogingen 68–80 (2026-11-13/14) + resultaten van de Claude-artifact "Natuurkunde Training H1".
Eén zwak concept per toets (vergelijkbare vragen bij elkaar, zoals gevraagd), ~15 vragen focus +
~5 herhaling van de andere zwakke punten. Eenvoudige stap eerst (leeg ≠ fout).

- 86: afstand bij versnellen/remmen — s = v_gem · t (gaf Δv/t als afstand, ~10×)
- 87: delen of vermenigvuldigen — a = F/m, F = m·a, m = Fz/g, t = Δv/a
- 88: constante snelheid / stilstand — Fres = 0, krachten zijn er wél (wrijving 0 N, arbeid 0 J)
- 89: stopafstand en botsen — reactieafstand ~ v, remweg ~ v², langere botstijd → kleinere kracht
- 90: arbeid — cm/km/kJ omrekenen, kracht per paard, W = 0 en negatieve arbeid
- 91: diagrammen lezen — (s,t)-helling, (v,t)-oppervlakte (met SVG-diagrammen)
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_economie_toetsen_96_115 import M, W, I, O, plaats, langste_aandeel, kortste_aandeel  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'natuurkunde', 'js', 'data')


def nl(x):
    return (f"{x:g}").replace(".", ",")


def graf(soort, lijnen, tmax, ymax):
    """Klein (s,t)- of (v,t)-diagram als inline SVG. lijnen = [(label, [(t, y), ...]), ...]."""
    W_, H_, L, B = 280, 170, 42, 140
    bx, by = (W_ - L - 12) / tmax, (B - 12) / ymax
    X = lambda t: L + t * bx
    Y = lambda y: B - y * by
    eenheid = "s (m)" if soort == "s" else "v (m/s)"
    p = [f'<svg viewBox="0 0 {W_} {H_ + 8}" width="280" style="max-width:100%;display:block;margin:8px 0" '
         f'font-size="11" fill="currentColor" stroke="currentColor">',
         f'<line x1="{L}" y1="{B}" x2="{W_ - 6}" y2="{B}"/><line x1="{L}" y1="{B}" x2="{L}" y2="6"/>',
         f'<text x="{W_ - 6}" y="{B + 28}" text-anchor="end" stroke="none">t (s)</text>',
         f'<text x="4" y="12" stroke="none">{eenheid}</text>']
    ts, ys = set(), set()
    for label, pts in lijnen:
        p.append('<polyline fill="none" stroke-width="2.5" points="'
                 + " ".join(f"{X(t):.0f},{Y(y):.0f}" for t, y in pts) + '"/>')
        if label:
            t, y = pts[-1]
            p.append(f'<text x="{X(t) + 4:.0f}" y="{Y(y) - 4:.0f}" stroke="none" font-weight="bold">{label}</text>')
        ts |= {t for t, _ in pts}
        ys |= {y for _, y in pts}
    for t in sorted(ts):
        p.append(f'<text x="{X(t):.0f}" y="{B + 14}" text-anchor="middle" stroke="none">{nl(t)}</text>')
        if t:
            p.append(f'<line x1="{X(t):.0f}" y1="{B}" x2="{X(t):.0f}" y2="{Y(ymax):.0f}" stroke-dasharray="2 3" stroke-width="0.6"/>')
    for y in sorted(ys):
        p.append(f'<text x="{L - 5}" y="{Y(y) + 4:.0f}" text-anchor="end" stroke="none">{nl(y)}</text>')
        if y:
            p.append(f'<line x1="{L}" y1="{Y(y):.0f}" x2="{W_ - 12}" y2="{Y(y):.0f}" stroke-dasharray="2 3" stroke-width="0.6"/>')
    return "".join(p) + "</svg>"


EEN_ZIN = " <i>(Eén korte zin is genoeg.)</i>"

EXAMENS = {
86: ("Toets 86 — Herhaling H1: Afstand bij versnellen en remmen (s = v_gem · t)", "🚗", [
    M("Een auto trekt op van 0 naar 20 m/s in 8,0 s. Hoe groot is de gemiddelde snelheid?",
      "10 m/s", ["20 m/s", "2,5 m/s", "160 m/s"],
      "Vanuit stilstand eenparig versnellen: v_gem = (0 + 20) / 2 = 10 m/s. 2,5 is Δv / t: dat is de versnelling, geen snelheid."),
    M("Dezelfde auto trekt op van 0 naar 20 m/s in 8,0 s. Welke afstand legt hij af?",
      "80 m", ["2,5 m", "160 m", "10 m"],
      "s = v_gem · t = 10 · 8,0 = 80 m. 2,5 (m/s²) is de versnelling. 160 m krijg je als je vergeet dat de gemiddelde snelheid de helft is."),
    I("Een scooter versnelt eenparig van 0 tot 14 m/s in 7,0 s. Bereken de afgelegde afstand in m.",
      "49|49 m",
      "v_gem = 14 / 2 = 7,0 m/s. s = v_gem · t = 7,0 · 7,0 = 49 m. (Δv / t = 2,0 m/s² is de versnelling, niet de afstand.)"),
    M("Met welke formule bereken je de afstand bij eenparig versnellen vanuit stilstand?",
      "s = ½ · v_eind · t", ["s = Δv / t", "s = v_eind · t", "s = v_eind / t"],
      "Gemiddelde snelheid = ½ · v_eind, dus s = ½ · v_eind · t. Δv / t is de formule voor de versnelling a."),
    M("Een fietser remt eenparig van 8,0 m/s tot stilstand in 4,0 s. Hoe lang is de remweg?",
      "16 m", ["2,0 m", "32 m", "0,5 m"],
      "v_gem = 8,0 / 2 = 4,0 m/s. Remweg = 4,0 · 4,0 = 16 m. 2,0 is de vertraging (m/s²); 32 m is zonder de helft."),
    W("Met Δv / t bereken je de afgelegde afstand.",
      False, "Onwaar: Δv / t geeft de versnelling in m/s². Voor de afstand gebruik je s = v_gem · t."),
    W("Een auto versnelt eenparig van 10 m/s naar 30 m/s. De gemiddelde snelheid is dan 20 m/s.",
      True, "Waar: v_gem = (10 + 30) / 2 = 20 m/s."),
    M("Een trein versnelt eenparig van 10 m/s naar 30 m/s in 20 s. Welke afstand legt de trein af?",
      "400 m", ["1,0 m", "600 m", "200 m"],
      "v_gem = (10 + 30) / 2 = 20 m/s. s = 20 · 20 = 400 m. 1,0 is de versnelling; 600 m is met de eindsnelheid gerekend."),
    I("Een bus remt eenparig van 14 m/s tot stilstand in 6,0 s. Bereken de remweg in m.",
      "42|42 m",
      "v_gem = 14 / 2 = 7,0 m/s. Remweg = 7,0 · 6,0 = 42 m."),
    M("Je rekent Δv / t uit en krijgt 1,5. Welke eenheid hoort bij dit antwoord?",
      "m/s²", ["m", "m/s", "s"],
      "Δv / t is de versnelling, in m/s². Het is dus géén afstand in meter."),
    I("Een auto trekt eenparig op van 0 tot 24 m/s in 10 s. Stap 1: hoe groot is de gemiddelde snelheid in m/s?",
      "12|12 m/s",
      "v_gem = (0 + 24) / 2 = 12 m/s."),
    I("Een auto trekt eenparig op van 0 tot 24 m/s in 10 s. Stap 2: bereken nu de afgelegde afstand in m.",
      "120|120 m",
      "s = v_gem · t = 12 · 10 = 120 m."),
    M("In een (v,t)-diagram loopt een rechte lijn van (0 s; 0 m/s) naar (6,0 s; 18 m/s). Welke afstand is afgelegd?",
      "54 m", ["3,0 m", "108 m", "18 m"],
      "Afstand = oppervlakte onder de lijn = ½ · 6,0 · 18 = 54 m. Dat is hetzelfde als v_gem · t = 9,0 · 6,0. 3,0 is de versnelling."),
    W("De remweg bij eenparig remmen tot stilstand bereken je met ½ · v_begin · t_rem.",
      True, "Waar: de gemiddelde snelheid is de helft van de beginsnelheid, dus remweg = ½ · v_begin · t_rem."),
    M("Een hardloper versnelt in 3,0 s van 0 tot 9,0 m/s en loopt daarna nog 5,0 s met 9,0 m/s. Hoeveel meter legt hij in totaal af?",
      "58,5 m", ["72 m", "45 m", "3,0 m"],
      "Versnellen: ½ · 9,0 · 3,0 = 13,5 m. Constant: 9,0 · 5,0 = 45 m. Totaal 58,5 m. 72 m is 9,0 · 8,0 (vergeten dat hij eerst langzamer liep)."),
    M("Een kar van 50 kg versnelt met 2,0 m/s². Hoe groot is de resulterende kracht?",
      "100 N", ["25 N", "0,04 N", "52 N"],
      "Fres = m · a = 50 · 2,0 = 100 N. Delen (25 N) hoort niet bij deze formule."),
    W("90 km/h is hetzelfde als 25 m/s.",
      True, "Waar: 90 / 3,6 = 25 m/s."),
    M("Een scooter rijdt met constante snelheid. De motorkracht is 300 N. Hoe groot is de totale wrijvingskracht?",
      "300 N", ["0 N", "600 N", "150 N"],
      "Constante snelheid: Fres = 0 N, dus de wrijving is even groot als de motorkracht: 300 N. De wrijving is niet 0 N."),
    W("Bij een twee keer zo grote snelheid wordt de remweg twee keer zo groot.",
      False, "Onwaar: de remweg is evenredig met v². Twee keer zo snel geeft 2² = 4 keer zo'n lange remweg."),
    O("Je weet de beginsnelheid en de eindsnelheid. Hoe bereken je de gemiddelde snelheid?" + EEN_ZIN,
      ["optellen/opgeteld/optelt/samen/som/plus/+", "delen door 2/deel door 2/deelt door 2/gedeeld door 2/door twee/helft"], 1,
      "Beginsnelheid plus eindsnelheid, gedeeld door 2.",
      "v_gem = (v_begin + v_eind) / 2. Daarna: s = v_gem · t."),
]),

87: ("Toets 87 — Herhaling H1: Delen of vermenigvuldigen? (a = F / m, F = m · a)", "➗", [
    M("Welke formule geeft de versnelling als je Fres en m weet?",
      "a = Fres / m", ["a = Fres · m", "a = m / Fres", "a = Fres − m"],
      "Uit Fres = m · a volgt a = Fres / m. Je deelt de kracht door de massa."),
    M("Op een kist van 150 kg werkt een resulterende kracht van 600 N. Hoe groot is de versnelling?",
      "4,0 m/s²", ["90000 m/s²", "0,25 m/s²", "450 m/s²"],
      "a = Fres / m = 600 / 150 = 4,0 m/s². 90000 is vermenigvuldigd; 0,25 is m / F (omgekeerd gedeeld)."),
    I("Een auto van 1200 kg krijgt een resulterende kracht van 2400 N. Bereken de versnelling in m/s².",
      "2|2,0|2 m/s²",
      "a = Fres / m = 2400 / 1200 = 2,0 m/s²."),
    M("Een sprinter van 80 kg versnelt met 1,5 m/s². Hoe groot is de resulterende kracht?",
      "120 N", ["53 N", "0,019 N", "81,5 N"],
      "Fres = m · a = 80 · 1,5 = 120 N. Hier vermenigvuldig je; 53 N is 80 / 1,5 (gedeeld)."),
    I("Een winkelkar van 25 kg versnelt met 0,80 m/s². Bereken de resulterende kracht in N.",
      "20|20 N",
      "Fres = m · a = 25 · 0,80 = 20 N."),
    M("Op een koffer werkt een zwaartekracht van 196,2 N (g = 9,81 N/kg). Wat is de massa?",
      "20 kg", ["1925 kg", "0,05 kg", "186 kg"],
      "Fz = m · g, dus m = Fz / g = 196,2 / 9,81 = 20 kg. 1925 kg krijg je als je vermenigvuldigt."),
    I("Een appel heeft een massa van 400 g. Bereken de zwaartekracht in N (g = 9,81 N/kg). Reken eerst om naar kg.",
      "3,9|3,92|3,924",
      "400 g = 0,400 kg. Fz = m · g = 0,400 · 9,81 = 3,9 N."),
    M("Een scooter versnelt met 2,0 m/s² van 0 tot 10 m/s. Hoe lang duurt dat?",
      "5,0 s", ["20 s", "0,20 s", "12 s"],
      "a = Δv / t, dus t = Δv / a = 10 / 2,0 = 5,0 s. 0,20 s is a / Δv (omgekeerd)."),
    W("Uit a = Fres / m volgt Fres = a / m.",
      False, "Onwaar: Fres = m · a. Je vermenigvuldigt de massa met de versnelling."),
    W("Hoe groter de massa bij dezelfde resulterende kracht, hoe kleiner de versnelling.",
      True, "Waar: a = Fres / m. Een grotere m in de noemer geeft een kleinere a."),
    M("Je wilt de massa uitrekenen uit Fres = m · a. Wat doe je?",
      "Fres delen door a", ["Fres vermenigvuldigen met a", "a delen door Fres", "a aftrekken van Fres"],
      "m = Fres / a. Controle: 1200 = m · 3 → m = 1200 / 3 = 400."),
    I("Een resulterende kracht van 3600 N geeft een bestelbus een versnelling van 2,4 m/s². Bereken de massa in kg.",
      "1500|1500 kg",
      "m = Fres / a = 3600 / 2,4 = 1500 kg."),
    M("Een kracht van 500 N werkt als resulterende kracht op een kist van 1000 kg. Welk antwoord klopt?",
      "a = 0,50 m/s²", ["a = 500000 m/s²", "a = 2,0 m/s²", "a = 5,0 m/s²"],
      "a = Fres / m = 500 / 1000 = 0,50 m/s². Een zware kist en een kleine kracht: dan hoort er een kleine versnelling bij."),
    W("Een zware vrachtwagen en een lichte auto krijgen dezelfde resulterende kracht. De vrachtwagen versnelt dan sneller.",
      False, "Onwaar: a = Fres / m. De vrachtwagen heeft een grotere massa, dus een kleinere versnelling."),
    M("Een fietser met fiets (samen 90 kg) remt. De resulterende kracht is 180 N. Hoe groot is de vertraging?",
      "2,0 m/s²", ["16200 m/s²", "0,5 m/s²", "270 m/s²"],
      "a = Fres / m = 180 / 90 = 2,0 m/s². Ook bij remmen deel je de kracht door de massa."),
    M("Een auto trekt eenparig op van 0 tot 16 m/s in 4,0 s. Welke afstand legt hij af?",
      "32 m", ["4,0 m", "64 m", "20 m"],
      "s = v_gem · t = 8,0 · 4,0 = 32 m. 4,0 is de versnelling (Δv / t)."),
    W("Een kracht van 2,5 kN is hetzelfde als 2500 N.",
      True, "Waar: 1 kN = 1000 N, dus 2,5 kN = 2500 N."),
    M("Een auto heeft bij 30 km/h een remweg van 10 m. Hoe lang is de remweg bij 90 km/h (zelfde weg, zelfde remmen)?",
      "90 m", ["30 m", "40 m", "270 m"],
      "90 km/h is 3 keer zo snel. De remweg wordt 3² = 9 keer zo lang: 9 · 10 = 90 m."),
    W("Een parachutist daalt met constante snelheid. De luchtweerstand is dan even groot als zijn zwaartekracht.",
      True, "Waar: constante snelheid betekent Fres = 0 N, dus Flucht = Fz."),
    O("Uit a = Fres / m: hoe bereken je Fres als je m en a weet?" + EEN_ZIN,
      ["vermenigvuldig/vermenigvuldigen/keer/maal/x"], 1,
      "Je vermenigvuldigt de massa met de versnelling.",
      "Fres = m · a: massa keer versnelling. Delen hoort bij a = Fres / m."),
]),

88: ("Toets 88 — Herhaling H1: Constante snelheid en stilstand (Fres = 0 N)", "⚖️", [
    M("Een auto rijdt met constante snelheid over een rechte weg. Wat geldt?",
      "Fres = 0 N: de aandrijfkracht is even groot als de wrijving",
      ["Er werken geen krachten op de auto, dus alles is 0 N",
       "De aandrijfkracht is groter dan de wrijving, anders stopt hij",
       "De wrijvingskracht is 0 N, want de snelheid verandert niet"],
      "Bij constante snelheid werken er wél krachten, maar ze heffen elkaar op: aandrijfkracht = wrijving, Fres = 0 N."),
    M("Een fietser rijdt met constante snelheid. Zijn trapkracht is 45 N. Hoe groot is de totale wrijvingskracht?",
      "45 N", ["0 N", "90 N", "22,5 N"],
      "Constante snelheid: Fres = 0 N. De wrijving is dus even groot als de trapkracht: 45 N."),
    I("Een vrachtwagen rijdt met constante snelheid. De motorkracht is 3500 N. Hoe groot is de totale tegenwerkende kracht in N?",
      "3500|3500 N|3,5 kN",
      "Constante snelheid → Fres = 0 N → tegenwerkende kracht = motorkracht = 3500 N."),
    M("Een auto rijdt met constante snelheid. De motorkracht is 900 N, de rolweerstand 350 N. Hoe groot is de luchtweerstand?",
      "550 N", ["1250 N", "0 N", "900 N"],
      "Rolweerstand + luchtweerstand = 900 N, dus luchtweerstand = 900 − 350 = 550 N. Optellen (1250 N) klopt niet."),
    I("Een zwemmer zwemt met constante snelheid. Zijn stuwkracht is 60 N. Hoe groot is de weerstand van het water in N?",
      "60|60 N",
      "Constante snelheid → Fres = 0 N → weerstand = stuwkracht = 60 N."),
    W("Bij constante snelheid is de wrijvingskracht 0 N.",
      False, "Onwaar: de wrijving is er wel, maar is even groot als de aandrijfkracht. Alleen Fres is 0 N."),
    W("Een lift gaat met constante snelheid omhoog. De spankracht in de kabel is dan even groot als de zwaartekracht.",
      True, "Waar: constante snelheid, dus Fres = 0 N en Fspan = Fz."),
    M("Een lift met een massa van 600 kg gaat met constante snelheid omhoog (g = 9,81 N/kg). Hoe groot is de spankracht in de kabel?",
      "5886 N", ["0 N", "600 N", "11772 N"],
      "Fz = m · g = 600 · 9,81 = 5886 N. Constante snelheid → Fspan = Fz = 5886 N."),
    M("Een parachutist van 80 kg daalt met constante snelheid (g = 9,81 N/kg). Hoe groot is de luchtweerstand?",
      "785 N", ["0 N", "80 N", "1570 N"],
      "Fz = 80 · 9,81 = 785 N. Constante snelheid → Flucht = Fz = 785 N."),
    W("Als de aandrijfkracht groter wordt dan de wrijving, gaat de auto versnellen.",
      True, "Waar: dan is Fres niet meer 0 N en wijst hij naar voren, dus de auto versnelt."),
    M("Een fietser rijdt met constante snelheid en stopt dan met trappen. Wat gebeurt er?",
      "Hij vertraagt, want alleen de wrijving werkt nog",
      ["Hij rijdt met constante snelheid door, want Fres blijft 0 N",
       "Hij versnelt, want de trapkracht remt hem niet meer af",
       "Hij staat meteen stil, want er is geen kracht naar voren"],
      "Zonder trapkracht blijft alleen de wrijving over: Fres wijst naar achteren, dus hij vertraagt (geleidelijk)."),
    I("Een auto rijdt met constante snelheid. De motorkracht is 1200 N en de luchtweerstand 700 N. Hoe groot is de rolweerstand in N?",
      "500|500 N",
      "Rolweerstand + luchtweerstand = motorkracht: rolweerstand = 1200 − 700 = 500 N."),
    M("Een kist staat stil op de vloer. De zwaartekracht op de kist is 300 N. Hoe groot is de kracht van de vloer op de kist?",
      "300 N", ["0 N", "600 N", "150 N"],
      "Stilstand: Fres = 0 N. De vloer duwt dus met 300 N omhoog, even groot als Fz."),
    W("Een kracht kan alleen arbeid verrichten als de snelheid verandert.",
      False, "Onwaar: W = F · s. Ook bij constante snelheid verricht bijvoorbeeld de motorkracht arbeid, want de auto legt afstand af."),
    M("Een fietser rijdt met constante snelheid 2,0 km tegen een wrijving van 25 N in. Hoeveel arbeid verricht zijn spierkracht?",
      "50 kJ", ["0 J", "50 J", "12,5 J"],
      "Spierkracht = wrijving = 25 N. 2,0 km = 2000 m. W = 25 · 2000 = 50000 J = 50 kJ. Constante snelheid betekent niet W = 0."),
    M("Een bus remt eenparig van 20 m/s tot stilstand in 5,0 s. Hoe lang is de remweg?",
      "50 m", ["4,0 m", "100 m", "25 m"],
      "v_gem = 20 / 2 = 10 m/s. Remweg = 10 · 5,0 = 50 m. 4,0 is de vertraging."),
    M("Een resulterende kracht van 900 N werkt op een kar van 300 kg. Hoe groot is de versnelling?",
      "3,0 m/s²", ["270000 m/s²", "0,33 m/s²", "1200 m/s²"],
      "a = Fres / m = 900 / 300 = 3,0 m/s²."),
    W("Bij dezelfde snelheidsverandering geeft een langere botstijd een kleinere kracht op de inzittenden.",
      True, "Waar: langere botstijd → kleinere vertraging → kleinere kracht (F = m · a)."),
    W("4,5 m/s is sneller dan 18 km/h.",
      False, "Onwaar: 18 km/h = 18 / 3,6 = 5 m/s. Dat is sneller dan 4,5 m/s."),
    O("Een auto rijdt met constante snelheid. Waarom is de wrijvingskracht dan níet 0 N?" + EEN_ZIN,
      ["even groot/gelijk/opheffen/heffen/motorkracht/aandrijfkracht/tegenwerk"], 1,
      "Omdat de wrijving even groot is als de motorkracht; ze heffen elkaar op.",
      "Fres = 0 N betekent: de krachten zijn even groot en tegengesteld, niet dat ze er niet zijn."),
]),

89: ("Toets 89 — Herhaling H1: Stopafstand en botsen (v, v² en botstijd)", "🛑", [
    M("Met welke formule bereken je de reactieafstand?",
      "s_r = v · t_r", ["s_r = v² · t_r", "s_r = v / t_r", "s_r = ½ · v · t_r"],
      "Tijdens de reactietijd rijd je nog met constante snelheid door: s_r = v · t_r."),
    M("Een auto rijdt 72 km/h. De reactietijd is 1,0 s. Hoe groot is de reactieafstand?",
      "20 m", ["72 m", "7,2 m", "40 m"],
      "72 km/h = 72 / 3,6 = 20 m/s. s_r = 20 · 1,0 = 20 m. 72 m is zonder omrekenen."),
    I("Een motorrijder rijdt 108 km/h en reageert pas na 0,9 s op een overstekend hert. Hoeveel meter rijdt hij in die tijd door?",
      "27|27 m",
      "108 / 3,6 = 30 m/s. s_r = 30 · 0,9 = 27 m."),
    M("De snelheid wordt 2 keer zo groot; de reactietijd blijft gelijk. Wat gebeurt er met de reactieafstand?",
      "Die wordt 2 keer zo groot", ["Die wordt 4 keer zo groot", "Die blijft gelijk", "Die wordt 2 keer zo klein"],
      "s_r = v · t_r: de reactieafstand is evenredig met v (niet met v²)."),
    M("De snelheid wordt 2 keer zo groot; de remkracht blijft gelijk. Wat gebeurt er met de remweg?",
      "Die wordt 4 keer zo groot", ["Die wordt 2 keer zo groot", "Die wordt 8 keer zo groot", "Die blijft gelijk"],
      "De remweg is evenredig met v²: 2² = 4 keer zo groot."),
    I("Een scooter heeft bij 30 km/h een remweg van 6 m. Wat wordt de remweg in m als hij 60 km/h rijdt?",
      "24|24 m",
      "Twee keer zo snel → 2² = 4 keer zo'n lange remweg: 4 · 6 = 24 m."),
    I("Bij 40 km/h is de remweg van een auto 9 m. Bereken de remweg bij 120 km/h (zelfde weg, zelfde remmen) in m.",
      "81|81 m",
      "120 km/h is 3 keer zo snel → 3² = 9 keer zo'n lange remweg: 9 · 9 = 81 m."),
    M("Bij 100 km/h is de remweg van een auto 20 m. Hoe lang is de remweg bij 50 km/h (zelfde weg, zelfde remmen)?",
      "5 m", ["10 m", "40 m", "80 m"],
      "Half zo snel → (½)² = ¼ van de remweg: 20 / 4 = 5 m."),
    W("Als de snelheid 3 keer zo groot wordt, wordt de reactieafstand 9 keer zo groot.",
      False, "Onwaar: de reactieafstand is evenredig met v, dus 3 keer zo groot. Alleen de remweg gaat met v² (9 keer)."),
    W("Als de snelheid 3 keer zo groot wordt, wordt de remweg 9 keer zo groot.",
      True, "Waar: remweg ~ v², dus 3² = 9 keer zo groot."),
    M("Bij een botsing is de snelheidsverandering hetzelfde, maar de botstijd wordt langer. Wat gebeurt er met de vertraging en de kracht?",
      "Beide worden kleiner",
      ["Beide worden groter", "De vertraging wordt kleiner, de kracht groter", "Beide blijven gelijk"],
      "a = Δv / t: langere t → kleinere vertraging. F = m · a → kleinere kracht."),
    M("Twee gelijke auto's botsen met dezelfde snelheid. Auto A deukt 0,30 m in, auto B 0,90 m. Wat geldt voor de kracht op de inzittenden van B?",
      "Die is 3 keer zo klein", ["Die is 3 keer zo groot", "Die is 9 keer zo klein", "Die is even groot"],
      "B remt af over een 3 keer zo lange afstand, dus de kracht is 3 keer zo klein. Meer indeuken = veiliger."),
    W("Een airbag maakt de botstijd langer; daardoor wordt de kracht op je hoofd kleiner.",
      True, "Waar: langere botstijd → kleinere vertraging → kleinere kracht."),
    M("Waarom is de binnenkant van een fietshelm van zacht schuim?",
      "Het schuim deukt in, zodat het hoofd over een langere afstand afremt",
      ["Het schuim maakt de botstijd korter, zodat de klap sneller voorbij is",
       "Schuim is licht, zodat je nek minder zwaar belast wordt bij een val",
       "Het schuim veert terug, zodat je hoofd met meer snelheid terugkaatst"],
      "Langere remafstand en botstijd voor het hoofd → kleinere vertraging → kleinere kracht."),
    W("Een kortere botstijd is veiliger, want dan is de botsing sneller voorbij.",
      False, "Onwaar: een kortere botstijd geeft een grotere vertraging en dus een grotere kracht."),
    I("Een auto rijdt 54 km/h. De reactietijd is 1,0 s en de remweg 20 m. Bereken de stopafstand in m.",
      "35|35 m",
      "54 / 3,6 = 15 m/s → reactieafstand 15 · 1,0 = 15 m. Stopafstand = 15 + 20 = 35 m."),
    M("Een bestuurder heeft alcohol gedronken. Welk deel van de stopafstand wordt daardoor langer?",
      "Alleen de reactieafstand", ["Alleen de remweg", "De remweg en de reactieafstand evenveel", "Geen van beide"],
      "Alcohol maakt de reactietijd langer, dus de reactieafstand. De remmen en de weg veranderen niet."),
    M("Een auto remt eenparig van 20 m/s tot stilstand in 4,0 s. Hoe lang is de remweg?",
      "40 m", ["80 m", "5,0 m", "8,0 m"],
      "Remweg = ½ · v · t = ½ · 20 · 4,0 = 40 m. 5,0 is de vertraging (Δv / t)."),
    M("Een hamer slaat een spijker 1,0 cm het hout in met een gemiddelde kracht van 500 N. Hoeveel arbeid is dat?",
      "5,0 J", ["500 J", "50 J", "0,50 J"],
      "1,0 cm = 0,010 m. W = F · s = 500 · 0,010 = 5,0 J. Met 1,0 (cm) rekenen geeft 500 J."),
    O("Waarom zorgt een langere botstijd voor een kleinere kracht?" + EEN_ZIN,
      ["vertraging/vertraagt/geleidelijk/langzamer/minder snel/kleinere versnelling"], 1,
      "Omdat de snelheid geleidelijker afneemt, is de vertraging kleiner en dus ook de kracht.",
      "a = Δv / t wordt kleiner bij een langere t, en F = m · a dus ook."),
]),

90: ("Toets 90 — Herhaling H1: Arbeid (cm, km en kJ; wanneer is W = 0?)", "🏋️", [
    M("Reken om: 2,5 kJ = …",
      "2500 J", ["250 J", "0,0025 J", "25 J"],
      "1 kJ = 1000 J, dus 2,5 kJ = 2500 J."),
    M("Reken om: 3 cm = …",
      "0,03 m", ["0,3 m", "300 m", "0,003 m"],
      "1 m = 100 cm, dus 3 cm = 3 / 100 = 0,03 m."),
    I("Een hamer slaat een spijker 2,0 cm het hout in met een gemiddelde kracht van 400 N. Bereken de arbeid in J. Reken eerst cm om naar m.",
      "8|8,0|8 J",
      "2,0 cm = 0,020 m. W = F · s = 400 · 0,020 = 8,0 J. Met 2,0 (cm) rekenen geeft 800: veel te groot."),
    M("Een timmerman drijft met één klap een nagel 0,5 cm diep in een balk; de hamer duwt gemiddeld met 1200 N. Hoeveel joule is dat?",
      "6,0 J", ["600 J", "0,6 J", "2400 J"],
      "0,5 cm = 0,005 m. W = 1200 · 0,005 = 6,0 J. 600 J is zonder omrekenen; 2400 is 1200 / 0,5 (gedeeld)."),
    I("Een fietser rijdt 3,0 km met constante snelheid tegen een wrijving van 50 N. Bereken de arbeid van zijn spierkracht in kJ.",
      "150|150 kJ",
      "3,0 km = 3000 m. W = 50 · 3000 = 150000 J = 150 kJ."),
    M("Een kar wordt met 200 N over 1,5 km getrokken. Hoeveel arbeid verricht de trekkracht?",
      "300 kJ", ["300 J", "3,0 kJ", "133 J"],
      "1,5 km = 1500 m. W = 200 · 1500 = 300000 J = 300 kJ. 300 J krijg je als je de km niet omrekent."),
    I("Vier paarden trekken samen een kar 200 m ver. Samen verrichten ze 280 kJ arbeid. Stap 1: hoe groot is de trekkracht van de vier paarden samen in N?",
      "1400|1400 N",
      "280 kJ = 280000 J. F = W / s = 280000 / 200 = 1400 N."),
    I("Vier paarden trekken samen een kar 200 m ver met samen 280 kJ arbeid. Stap 2: hoe groot is de kracht van één paard in N?",
      "350|350 N",
      "Samen 1400 N, verdeeld over 4 paarden: 1400 / 4 = 350 N per paard."),
    M("Je draagt een tas 10 m ver over een vlakke vloer. Hoeveel arbeid verricht je spierkracht (omhoog) op de tas?",
      "0 J, want de kracht staat loodrecht op de beweging",
      ["Veel, want je moet de tas de hele tijd vasthouden",
       "10 J, want je hebt de tas 10 m ver gedragen",
       "Negatief, want de tas gaat niet omhoog maar opzij"],
      "Je spierkracht wijst omhoog, de beweging is horizontaal. Kracht loodrecht op de beweging → W = 0 J."),
    W("Je duwt hard tegen een muur die niet beweegt. Je spierkracht verricht dan arbeid.",
      False, "Onwaar: de muur verplaatst niet, s = 0 m, dus W = F · s = 0 J (ook al word je moe)."),
    W("Een appel valt 2,0 m uit een boom. Tijdens de val is de arbeid van de zwaartekracht groter dan 0 J.",
      True, "Waar: de zwaartekracht wijst omlaag en de bal beweegt omlaag, dus W > 0."),
    M("Een bal wordt recht omhoog gegooid en valt terug tot dezelfde hoogte. Hoeveel arbeid verricht de zwaartekracht over de hele rit?",
      "0 J: omhoog negatief, omlaag even veel positief",
      ["Negatief, want de bal gaat eerst omhoog",
       "Positief, want de bal valt aan het eind",
       "Twee keer zoveel als bij alleen vallen"],
      "Omhoog: W = −Fz · h. Omlaag: W = +Fz · h. Samen 0 J, want begin- en eindhoogte zijn gelijk."),
    M("Een last van 50 kg wordt met constante snelheid 4,0 m omhoog getild (g = 9,81 N/kg). Hoeveel arbeid kost dat?",
      "1962 J", ["200 J", "123 J", "1250 J"],
      "F = Fz = 50 · 9,81 = 490,5 N. W = 490,5 · 4,0 = 1962 J. 123 J is 490,5 / 4,0: je moet vermenigvuldigen, niet delen."),
    W("De wrijvingskracht verricht negatieve arbeid, want hij werkt tegen de beweging in.",
      True, "Waar: kracht tegen de beweging in → W = −F · s."),
    W("Een doos twee keer zo hoog tillen kost vier keer zoveel arbeid.",
      False, "Onwaar: W = F · s. Twee keer zo hoog = twee keer zoveel arbeid (niet vier)."),
    I("Een surfer vaart met constante snelheid 30 m. De windkracht is 200 N. Hoeveel arbeid verricht de weerstand van het water in J? Let op het teken.",
      "-6000|−6000|-6000 J|−6000 J|-6 kJ",
      "Constante snelheid → weerstand = 200 N, tegen de beweging in. W = −200 · 30 = −6000 J."),
    M("Een trein trekt eenparig op van 0 tot 30 m/s in 60 s. Welke afstand legt hij af?",
      "900 m", ["0,5 m", "1800 m", "30 m"],
      "s = v_gem · t = 15 · 60 = 900 m. 0,5 is de versnelling."),
    M("Een resulterende kracht van 1500 N geeft een kar een versnelling van 3,0 m/s². Wat is de massa?",
      "500 kg", ["4500 kg", "0,002 kg", "1503 kg"],
      "m = Fres / a = 1500 / 3,0 = 500 kg."),
    W("De reactieafstand is evenredig met de snelheid.",
      True, "Waar: s_r = v · t_r. Twee keer zo snel = twee keer zo'n lange reactieafstand."),
    O("Waarom verricht de zwaartekracht geen arbeid op een bal die over een vlakke tafel rolt?" + EEN_ZIN,
      ["loodrecht/haaks/90/hoogte/niet omlaag/niet naar beneden"], 1,
      "Omdat de zwaartekracht loodrecht op de beweging staat.",
      "De bal gaat niet omlaag; een kracht loodrecht op de beweging verricht geen arbeid."),
]),

91: ("Toets 91 — Herhaling H1: Diagrammen lezen ((s,t) en (v,t))", "📈", [
    M("Een skateboarder rijdt volgens dit (s,t)-diagram. Hoe beweegt hij?" + graf("s", [("", [(0, 0), (6, 30)])], 6, 30),
      "Constante snelheid", ["Versnellen", "Stilstand", "Vertragen"],
      "In een (s,t)-diagram betekent een schuine rechte lijn: elke seconde evenveel meter → constante snelheid."),
    M("Dit (s,t)-diagram hoort bij een hond in het park. Wat doet de hond?" + graf("s", [("", [(0, 20), (6, 20)])], 6, 30),
      "Stilstand", ["Constante snelheid", "Versnellen", "Vertragen"],
      "De afstand verandert niet: het voorwerp staat stil. (In een (v,t)-diagram zou dit constante snelheid zijn!)"),
    M("Kijk goed: dit is een (v,t)-diagram van een fietser. Welke beweging maakt zij?" + graf("v", [("", [(0, 8), (6, 8)])], 6, 10),
      "Constante snelheid", ["Stilstand", "Versnellen", "Vertragen"],
      "In een (v,t)-diagram betekent een horizontale lijn: de snelheid blijft 8 m/s → constante snelheid."),
    M("Een tram vertrekt bij de halte. Zijn snelheid zie je in dit (v,t)-diagram. Wat doet de tram?" + graf("v", [("", [(0, 0), (6, 12)])], 6, 12),
      "Versnellen", ["Constante snelheid", "Stilstand", "Vertragen"],
      "De snelheid neemt toe van 0 tot 12 m/s → versnellen (eenparig, want de lijn is recht)."),
    M("Hoe groot is de snelheid in dit (s,t)-diagram?" + graf("s", [("", [(0, 0), (5, 40)])], 5, 40),
      "8,0 m/s", ["200 m/s", "40 m/s", "0,125 m/s"],
      "Helling = Δs / Δt = 40 / 5 = 8,0 m/s. 0,125 is 5 / 40 (omgekeerd)."),
    I("Een roeiboot vaart volgens deze grafiek. Hoeveel meter vaart de boot in 10 s?" + graf("v", [("", [(0, 6), (10, 6)])], 10, 8),
      "60|60 m",
      "Oppervlakte onder de lijn = rechthoek: 6 · 10 = 60 m."),
    M("Welke afstand is afgelegd volgens dit (v,t)-diagram?" + graf("v", [("", [(0, 0), (8, 16)])], 8, 16),
      "64 m", ["128 m", "2,0 m", "16 m"],
      "Oppervlakte = driehoek = ½ · 8 · 16 = 64 m. 128 m is zonder ½; 2,0 is de versnelling (16 / 8)."),
    I("Bereken met dit (v,t)-diagram de versnelling in m/s²." + graf("v", [("", [(0, 0), (4, 12)])], 4, 12),
      "3|3,0|3 m/s²",
      "a = Δv / Δt = 12 / 4 = 3,0 m/s² (de helling van de lijn)."),
    W("Wie de oppervlakte tussen een (v,t)-lijn en de tijd-as uitrekent, vindt het aantal meters dat is afgelegd.",
      True, "Waar: oppervlakte = v · t = afstand."),
    W("Loopt de lijn in een plaats-tijd-grafiek vlak (evenwijdig aan de t-as), dan rijdt de auto met een vaste snelheid.",
      False, "Onwaar: in een (s,t)-diagram is een horizontale lijn stilstand. Alleen in een (v,t)-diagram is het constante snelheid."),
    W("In een (s,t)-diagram geeft een steilere lijn een grotere snelheid.",
      True, "Waar: de helling van een (s,t)-diagram is de snelheid."),
    M("Hoeveel meter is er in totaal afgelegd volgens dit (v,t)-diagram?" + graf("v", [("", [(0, 0), (4, 8), (10, 8)])], 10, 8),
      "64 m", ["80 m", "48 m", "2,0 m"],
      "Driehoek ½ · 4 · 8 = 16 m plus rechthoek 6 · 8 = 48 m. Totaal 64 m."),
    M("Een auto remt volgens dit (v,t)-diagram. Hoe lang is de remweg?" + graf("v", [("", [(0, 10), (5, 0)])], 5, 10),
      "25 m", ["50 m", "2,0 m", "10 m"],
      "Oppervlakte = ½ · 5 · 10 = 25 m. 2,0 is de vertraging (10 / 5)."),
    W("In een (v,t)-diagram betekent een lijn die daalt naar 0 dat het voorwerp achteruit rijdt.",
      False, "Onwaar: de snelheid wordt kleiner, dus het voorwerp remt af (vertraagt) tot stilstand."),
    M("Wie is sneller, A of B?" + graf("s", [("A", [(0, 0), (4, 20)]), ("B", [(0, 0), (4, 40)])], 4, 40),
      "B, met 10 m/s", ["A, met 5 m/s", "Allebei even snel", "B, met 40 m/s"],
      "B: 40 / 4 = 10 m/s. A: 20 / 4 = 5 m/s. De steilste lijn in een (s,t)-diagram is het snelst."),
    M("Een auto rijdt met constante snelheid. De motorkracht is 1500 N. Hoe groot is de totale wrijvingskracht?",
      "1500 N", ["0 N", "3000 N", "750 N"],
      "Constante snelheid: Fres = 0 N, dus wrijving = motorkracht = 1500 N."),
    M("Je geeft een speelgoedauto van 3,0 kg een duw: Fres = 12 N. Met welke versnelling komt hij in beweging?",
      "4,0 m/s²", ["36 m/s²", "0,25 m/s²", "15 m/s²"],
      "a = Fres / m = 12 / 3,0 = 4,0 m/s²."),
    I("Bij 20 km/h is de remweg van een fiets 5 m. Bereken de remweg bij 40 km/h (zelfde weg, zelfde remmen) in m.",
      "20|20 m",
      "Twee keer zo snel → 4 keer zo'n lange remweg: 4 · 5 = 20 m."),
    W("Een kracht van 300 N tilt een doos 2,0 m op. De arbeid is dan 600 J.",
      True, "Waar: W = F · s = 300 · 2,0 = 600 J."),
    O("Hoe haal je de afgelegde afstand uit een (v,t)-diagram?" + EEN_ZIN,
      ["oppervlakte/oppervlak/opp"], 1,
      "Je berekent de oppervlakte onder de lijn.",
      "Afstand = oppervlakte onder de (v,t)-lijn."),
]),
}


def main():
    rng = random.Random("natuurkunde_h1_zwakte_86_91")
    for nr in sorted(EXAMENS):
        titel, icoon, vr = EXAMENS[nr]
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
               f"   Gegenereerd door tools/gen_natuurkunde_h1_zwakte_86_91.py\n"
               f"   ========================================================= */\n")
        with open(os.path.join(ROOT, f"examen_{nr}.js"), "w", encoding="utf-8") as f:
            f.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")


if __name__ == "__main__":
    main()
