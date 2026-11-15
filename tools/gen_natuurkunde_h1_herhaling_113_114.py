#!/usr/bin/env python3
"""Natuurkunde HAVO 3 · H1 — herhalingstoetsen 113–114 (Opus, 2026-11-15).

Analyse laatste 15 pogingen (105 … 98, ~75 fouten):
  rekenregel kiezen (vermenigvuldigt i.p.v. delen: a = F:m, a = Δv:t, m = Fz:g, s = v·t) ≈ 22,
  omrekenen (g→kg, kJ↔J, km→m, min→h, km/h→m/s) ≈ 12, diagram ≈ 8, arbeid 0/teken ≈ 7,
  remweg = stop − reactie (telt op) 5.
113 = rekenregel kiezen (+ 'kan dat?'), 114 = omrekenen + arbeid + diagram + remweg.
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_economie_toetsen_96_115 import M, W, I, O, plaats, langste_aandeel, kortste_aandeel  # noqa: E402
from gen_natuurkunde_h1_zwakte_86_91 import EEN_ZIN, ROOT, graf  # noqa: E402

DEEL = ["delen/deel/deelt/gedeeld/door/gedeelt"]

EXAMENS = {
113: ("mix", "Toets 113 — Herhaling: delen of keer? (rekenregel kiezen)", "➗", [
    M("Je zoekt de versnelling a. Je kent Fres en de massa m. Welke berekening maak je?",
      "a = Fres : m", ["a = Fres · m", "a = m : Fres", "a = Fres − m"],
      "Uit Fres = m · a volgt a = Fres : m. Je deelt de kracht door de massa. Vermenigvuldigen geeft een veel te groot getal."),
    I("De roeiers geven hun boot (120 kg) samen een resulterende kracht van 210 N. Met hoeveel m/s² versnelt de boot?",
      "1,75|1.75|1,8|1,75 m/s²|1,8 m/s²", "a = Fres : m = 210 : 120 = 1,75 m/s². Wie vermenigvuldigt, krijgt 25 200 m/s²: dat kan niet."),
    W("Een kar van 25 kg krijgt Fres = 75 N. Sam rekent: a = 75 · 25 = 1875 m/s². Dat klopt.",
      False, "Onwaar: Sam vermenigvuldigde. a = 75 : 25 = 3 m/s². 1875 m/s² is sneller dan een raket: altijd even checken!"),
    M("Je berekent de versnelling van een fiets en vindt 3000 m/s². Wat is het beste?",
      "Opnieuw rekenen, dit kan niet",
      ["Het antwoord opschrijven, het klopt", "Er m/s achter zetten", "Het getal afronden op 3000"],
      "Een fiets haalt hooguit een paar m/s². Een enorm getal betekent meestal dat je hebt vermenigvuldigd in plaats van gedeeld."),
    M("Welke berekening geeft de resulterende kracht, als massa en versnelling bekend zijn?",
      "Fres = m · a", ["Fres = m : a", "Fres = a : m", "Fres = m + a"],
      "De formule staat al goed: Fres = m · a. Hier vermenigvuldig je dus wél: massa keer versnelling."),
    I("Een motor met rijder heeft samen een massa van 250 kg en versnelt met 2,4 m/s². Bereken de resulterende kracht in N.",
      "600|600 N", "Fres = m · a = 250 · 2,4 = 600 N. Je zoekt de kracht, dus vermenigvuldigen."),
    M("Je zoekt de versnelling. Je kent de snelheidsverandering Δv en de tijd t. Welke berekening maak je?",
      "a = Δv : t", ["a = Δv · t", "a = t : Δv", "a = Δv + t"],
      "Versnelling = hoeveel m/s er per seconde bij komt: a = Δv : t. Je deelt door de tijd."),
    I("Een skiër gaat in 6,0 s van 4,0 m/s naar 19 m/s. Bereken de versnelling in m/s².",
      "2,5|2.5|2,50|2,5 m/s²", "Δv = 19 − 4,0 = 15 m/s. a = Δv : t = 15 : 6,0 = 2,5 m/s². Eerst het verschil, dan delen."),
    W("Een auto remt in 8,0 s van 24 m/s tot stilstand. Sam rekent: de vertraging is 24 · 8,0 = 192 m/s². Dat klopt.",
      False, "Onwaar: Sam vermenigvuldigde. a = Δv : t = 24 : 8,0 = 3 m/s² vertraging (a = −3 m/s²)."),
    I("Een rolschaatser vertrekt uit stilstand en versnelt 5,0 s lang met 1,4 m/s². Bereken zijn eindsnelheid in m/s.",
      "7|7,0|7.0|7 m/s", "Elke seconde komt er 1,4 m/s bij: v = a · t = 1,4 · 5,0 = 7 m/s. Hier vermenigvuldig je wél."),
    M("Je zoekt de massa. Je kent de zwaartekracht Fz en g = 9,81 N/kg. Welke berekening maak je?",
      "m = Fz : g", ["m = Fz · g", "m = g : Fz", "m = Fz − g"],
      "Uit Fz = m · g volgt m = Fz : g. Je deelt de zwaartekracht door 9,81."),
    I("De zwaartekracht op een kinderfiets is 147 N. Hoeveel kg is de fiets? (g = 9,81 N/kg)",
      "15|14,98|14,99|15,0|14.98|14.99|15 kg", "m = Fz : g = 147 : 9,81 ≈ 15 kg. Vermenigvuldigen geeft 1442 kg: een kinderfiets zo zwaar als een auto."),
    M("Een voorwerp beweegt met constante snelheid. Met welke formule bereken je de afstand?",
      "s = v · t", ["s = v : t", "s = t : v", "s = v + t"],
      "Afstand = snelheid keer tijd: s = v · t. Elke seconde leg je v meter af, dus vermenigvuldigen."),
    I("Hoeveel meter legt een trein af die 40 seconden lang steeds 25 m/s rijdt?",
      "1000|1 000|1000 m|1 000 m", "s = v · t = 25 · 40 = 1000 m."),
    I("Een kart versnelt eenparig vanuit stilstand tot 14 m/s. Stap 1: hoe groot is de gemiddelde snelheid in m/s?",
      "7|7,0|7.0|7 m/s", "Bij eenparig versnellen vanuit stilstand: v_gem = (0 + 14) : 2 = 7 m/s."),
    I("Dezelfde kart versnelt in 6,0 s eenparig van 0 naar 14 m/s (v_gem uit stap 1). Stap 2: bereken de afstand in m.",
      "42|42 m", "s = v_gem · t = 7 · 6,0 = 42 m. Niet 14 · 6 = 84 m: dan vergeet je de helft."),
    M("Bij een noodstop is de stopafstand 48 m. Daarvan is 14 m reactieafstand. Welk deel is remweg?",
      "34 m", ["62 m", "3,4 m", "672 m"],
      "Stopafstand = reactieafstand + remweg, dus remweg = 48 − 14 = 34 m. 62 m is opgeteld: dat is langer dan de stopafstand zelf."),
    W("De remweg is altijd korter dan de stopafstand, want de reactieafstand komt er nog bij.",
      True, "Waar: stopafstand = reactieafstand + remweg. Remweg = stopafstand − reactieafstand: aftrekken, niet optellen."),
    M("Een fietser met fiets (80 kg) trapt met 120 N vooruit. De weerstand is 40 N. Hoe groot is de versnelling?",
      "1 m/s²", ["2 m/s²", "1,5 m/s²", "6400 m/s²"],
      "Eerst Fres = 120 − 40 = 80 N, dan a = Fres : m = 80 : 80 = 1 m/s². 2 m/s² = opgeteld, 1,5 m/s² = weerstand vergeten."),
    O("Je kent de massa van een slee en de resulterende kracht erop. Welke rekenbewerking geeft de versnelling?" + EEN_ZIN,
      DEEL, 1, "Delen: a = Fres : m.", "a = Fres : m, dus je deelt de kracht door de massa."),
]),

114: ("mix", "Toets 114 — Herhaling: omrekenen, arbeid en diagrammen", "🔁", [
    M("Hoeveel kilogram is 250 g?",
      "0,25 kg", ["250 000 kg", "2,5 kg", "25 kg"],
      "1 kg = 1000 g, dus 250 g = 250 : 1000 = 0,25 kg. Van gram naar kilogram deel je door 1000."),
    I("Wat is de zwaartekracht op een telefoon van 180 g, in N? Reken eerst om naar kg (g = 9,81 N/kg).",
      "1,8|1,77|1,766|1,77 N|1,8 N|1.8|1.77", "Eerst 180 g = 0,180 kg. Fz = m · g = 0,180 · 9,81 ≈ 1,8 N."),
    W("Een zak suiker van 400 g. Sam rekent: Fz = 400 · 9,81 = 3924 N. Dat klopt.",
      False, "Onwaar: Sam rekende niet om. 400 g = 0,400 kg, dus Fz = 0,400 · 9,81 ≈ 3,9 N."),
    M("Hoeveel joule is 1 kJ?",
      "1000 J", ["100 J", "0,001 J", "10 J"],
      "Kilo betekent 1000: 1 kJ = 1000 J, net als 1 km = 1000 m."),
    I("Een kraan verricht 85 kJ arbeid. Hoeveel J is dat?",
      "85000|85 000|85000 J|85 000 J", "Van kJ naar J vermenigvuldig je met 1000: 85 · 1000 = 85 000 J."),
    I("Een fietser verricht 7500 J arbeid. Hoeveel kJ is dat?",
      "7,5|7.5|7,5 kJ", "Van J naar kJ deel je door 1000: 7500 : 1000 = 7,5 kJ."),
    M("Tijdens een tocht van 3,0 km werkt er steeds 25 N weerstand op een fietser. Hoeveel arbeid verricht hij tegen die weerstand in?",
      "75 kJ", ["75 000 kJ", "75 J", "8,3 kJ"],
      "3,0 km = 3000 m. W = F · s = 25 · 3000 = 75 000 J = 75 kJ. 75 J: km niet omgerekend; 75 000 kJ: J en kJ verward."),
    I("Een sleepboot trekt met 400 N een bootje 1,5 km ver. Bereken de arbeid in kJ.",
      "600|600 kJ", "1,5 km = 1500 m. W = 400 · 1500 = 600 000 J = 600 kJ."),
    M("Arbeid en energie druk je uit in dezelfde eenheid. Welke eenheid is dat?",
      "joule (J)", ["watt (W)", "newton (N)", "newton per kilogram (N/kg)"],
      "Arbeid en energie in joule. Watt is vermogen (energie per seconde), newton is kracht."),
    M("Hoeveel uur is 30 minuten?",
      "0,5 h", ["30 h", "0,3 h", "1800 h"],
      "1 uur = 60 minuten, dus 30 min = 30 : 60 = 0,5 h. 0,3 h is fout: een uur heeft geen 100 minuten."),
    I("Een wandelaar loopt 6,0 km in 90 minuten. Bereken zijn gemiddelde snelheid in km/h.",
      "4|4,0|4.0|4 km/h", "90 min = 1,5 h. v = s : t = 6,0 : 1,5 = 4 km/h."),
    M("Een scooter rijdt 90 km/h. Hoeveel m/s is dat?",
      "25 m/s", ["324 m/s", "9 m/s", "90 m/s"],
      "Van km/h naar m/s deel je door 3,6: 90 : 3,6 = 25 m/s. 324 m/s is keer 3,6: de verkeerde kant op."),
    W("Je draagt een krat 15 m horizontaal. De kracht van je armen (omhoog) verricht daarbij arbeid.",
      False, "Onwaar: je armen duwen omhoog, maar het krat beweegt horizontaal. Kracht loodrecht op de beweging → W = 0 J."),
    M("Een gewichtheffer houdt een halter 4 seconden stil boven zijn hoofd. Hoeveel arbeid verricht hij in die 4 seconden?",
      "0 J, want de halter beweegt niet", ["Veel, want het is zwaar", "Evenveel als bij het optillen", "Negatieve arbeid"],
      "W = F · s en s = 0 m, dus W = 0 J. Moe worden betekent nog geen arbeid in de natuurkunde."),
    M("Je gooit een bal recht omhoog. Wat voor arbeid verricht de zwaartekracht terwijl de bal stijgt?",
      "Negatieve arbeid", ["Positieve arbeid", "Geen arbeid", "Eerst negatief, dan nul"],
      "Zwaartekracht omlaag, beweging omhoog: tegen de beweging in → negatieve arbeid."),
    I("Een kraan hijst een pallet van 60 kg met constante snelheid naar 2,5 m hoogte (g = 9,81 N/kg). Hoeveel joule arbeid verricht de kraan?",
      "1472|1471,5|1471|1470|1 472|1 471,5|1471.5|1472 J|1471,5 J",
      "Eerst de kracht: F = Fz = 60 · 9,81 = 588,6 N. Dan W = F · s = 588,6 · 2,5 ≈ 1472 J."),
    M("Wat doet het voorwerp in dit (v,t)-diagram?" + graf("v", [("", [(0, 6), (5, 6)])], 5, 8),
      "Het beweegt met constante snelheid", ["Het staat stil", "Het versnelt", "Het remt af"],
      "In een (v,t)-diagram staat de snelheid omhoog. Horizontaal bij 6 m/s = steeds 6 m/s: constante snelheid, niet stilstaan."),
    I("Hoeveel meter legt de auto uit dit (v,t)-diagram in 8 seconden af?"
      + graf("v", [("", [(0, 0), (4, 10), (8, 10)])], 8, 12),
      "60|60 m", "Afstand = oppervlakte. Driehoek 0–4 s: ½ · 4 · 10 = 20 m. Rechthoek 4–8 s: 4 · 10 = 40 m. Samen 60 m."),
    M("Een scooter rijdt 2 keer zo hard (zelfde weg, zelfde remmen). Wat gebeurt er met de remweg?",
      "4 keer zo lang", ["2 keer zo lang", "Even lang", "8 keer zo lang"],
      "De remweg hangt af van v²: 2 keer zo snel → 2 · 2 = 4 keer zo lange remweg."),
    O("Je moet 2,5 km invullen in W = F · s. Wat doe je eerst met de 2,5 km?" + EEN_ZIN,
      ["meter/2500/omrekenen/omzetten/m"], 1, "Omrekenen naar meter: 2500 m.",
      "In W = F · s moet s in meter: 2,5 km = 2500 m."),
]),
}


def main():
    rng = random.Random("natuurkunde_h1_herhaling_113_114")
    for nr in sorted(EXAMENS):
        par, titel, icoon, vr = EXAMENS[nr]
        assert len(vr) == 20, f"examen_{nr}: {len(vr)} vragen"
        t = [v["type"] for v in vr]
        vr = plaats([dict(v) for v in vr], rng)
        n_lang, tot = langste_aandeel(vr)
        n_kort, _ = kortste_aandeel(vr)
        print(f"examen_{nr}: {t.count('mc')} mc / {t.count('waaronwaar')} w-o / {t.count('invul')} invul / "
              f"{t.count('open')} open · langste {n_lang}/{tot}, kortste {n_kort}/{tot}")
        assert n_lang / tot <= 0.4 and n_kort / tot <= 0.4, f"examen_{nr}: juiste optie te vaak langste/kortste"
        ex = {"id": f"ex-h3-natuurkunde-{nr}", "hoofdstuk": 1, "paragraaf": par, "titel": titel,
              "vak": "Natuurkunde · HAVO 3 (H1)", "icoon": icoon, "duurMin": 30, "vragen": vr}
        kop = (f"/* =========================================================\n   Duru's Natuurkunde (HAVO 3) — {titel}\n"
               f"   Gegenereerd door tools/gen_natuurkunde_h1_herhaling_113_114.py\n"
               f"   ========================================================= */\n")
        with open(os.path.join(ROOT, f"examen_{nr}.js"), "w", encoding="utf-8") as f:
            f.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")


if __name__ == "__main__":
    main()
