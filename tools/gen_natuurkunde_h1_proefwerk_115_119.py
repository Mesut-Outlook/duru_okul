#!/usr/bin/env python3
"""Natuurkunde HAVO 3 · H1 — proefwerk-stijl toetsen 115–119 (Opus, 2026-11-15).

Verzoek gebruiker: "5 nieuwe gemengde toetsen zoals ze op het echte proefwerk kunnen komen".
Vorm = eindopgaven uit het boek (Sophia uitrijden, sledehonden, noodstop-(v,t), airbag, klimtouw, 0–100):
per toets 4–5 contexten met deelvragen a/b/c, alle §1.1–1.5, reken- én uitlegvragen.
Gewicht blijft op de zwaktes (delen/keer, omrekenen, v_gem, remweg ~ v², arbeid 0/−, stop = reactie + rem).
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_economie_toetsen_96_115 import M, W, I, O, plaats, langste_aandeel, kortste_aandeel  # noqa: E402
from gen_natuurkunde_h1_zwakte_86_91 import EEN_ZIN, ROOT, graf  # noqa: E402

EXAMENS = {
115: ("eind", "Toets 115 — Proefwerk H1 (oefenen zoals het echt is) — A", "📝", [
    # Context 1: Emma fietst naar school
    I("Emma fietst 4,5 km naar school en doet daar 15 minuten over. Bereken haar gemiddelde snelheid in km/h.",
      "18|18 km/h", "15 min = 0,25 h. v = s : t = 4,5 : 0,25 = 18 km/h."),
    I("Emma fietst 4,5 km in 15 minuten. Hoeveel m/s is haar gemiddelde snelheid?",
      "5|5,0|5 m/s|5,0 m/s", "4,5 km in 0,25 h = 18 km/h. Van km/h naar m/s deel je door 3,6: 18 : 3,6 = 5 m/s. (Of: 4500 m : 900 s = 5 m/s.)"),
    M("Emma moet onderweg 2 minuten wachten voor een stoplicht. Wat betekent dat voor haar gemiddelde snelheid over de hele rit?",
      "Die wordt lager, want de tijd wordt langer",
      ["Die blijft gelijk, want ze fietst even hard", "Die wordt hoger, want ze rust even uit", "Die wordt 0 km/h, want ze staat stil"],
      "Gemiddelde snelheid = totale afstand : totale tijd. Het wachten telt mee in de tijd, de afstand blijft gelijk → lager."),
    M("Een stuk van de rit fietst Emma met constante snelheid. Hoe ziet dat stuk eruit in een (s,t)-diagram?",
      "Een schuine rechte lijn omhoog", ["Een horizontale lijn", "Een kromme lijn die steeds steiler wordt", "Een rechte lijn die daalt"],
      "Constante snelheid: elke seconde evenveel meter erbij → rechte, schuine lijn. Horizontaal in een (s,t)-diagram = stilstaan."),
    # Context 2: vrachtwagen trekt op
    I("Een vrachtwagen van 12 000 kg trekt op bij groen licht: in 20 s van 0 tot 54 km/h. Reken 54 km/h om naar m/s.",
      "15|15 m/s", "54 : 3,6 = 15 m/s."),
    I("De vrachtwagen trekt in 20 s op van 0 tot 54 km/h. Bereken de versnelling in m/s².",
      "0,75|0.75|0,75 m/s²", "Eerst omrekenen: 54 km/h = 15 m/s. a = Δv : t = 15 : 20 = 0,75 m/s²."),
    I("Bereken de resulterende kracht op de vrachtwagen van 12 000 kg die in 20 s optrekt van 0 tot 54 km/h.",
      "9000|9 000|9000 N|9 000 N", "54 km/h = 15 m/s; a = 15 : 20 = 0,75 m/s²; Fres = m · a = 12 000 · 0,75 = 9000 N."),
    I("Hoeveel meter legt de vrachtwagen af tijdens het eenparig optrekken (van 0 tot 54 km/h in 20 s)?",
      "150|150 m", "54 km/h = 15 m/s. v_gem = (0 + 15) : 2 = 7,5 m/s. s = v_gem · t = 7,5 · 20 = 150 m."),
    W("Daarna rijdt de vrachtwagen met een constante snelheid van 54 km/h. De motorkracht is dan 0 N.",
      False, "Onwaar: bij constante snelheid is Fres = 0 N, niet de motorkracht. De motor moet de weerstand opheffen: Fmotor = Fw."),
    # Context 3: noodstop
    I("Een automobilist rijdt 72 km/h (= 20 m/s) en ziet een kind oversteken. Zijn reactietijd is 0,9 s. Bereken de reactieafstand in m.",
      "18|18 m", "Tijdens de reactietijd rijdt de auto nog met constante snelheid: s = v · t = 20 · 0,9 = 18 m."),
    I("Daarna remt de auto vanaf 72 km/h tot stilstand, met een vertraging van 8,0 m/s². Bereken de remtijd in s.",
      "2,5|2.5|2,5 s", "72 km/h = 20 m/s. t = Δv : a = 20 : 8,0 = 2,5 s."),
    I("Bereken de remweg van deze auto (72 km/h, remvertraging 8,0 m/s²).",
      "25|25 m", "Remtijd = 20 : 8,0 = 2,5 s; v_gem = (20 + 0) : 2 = 10 m/s; remweg = 10 · 2,5 = 25 m."),
    I("Bereken de stopafstand van deze automobilist: 72 km/h, reactietijd 0,9 s, remvertraging 8,0 m/s².",
      "43|43 m", "Reactieafstand 20 · 0,9 = 18 m + remweg 10 · 2,5 = 25 m → stopafstand 43 m."),
    M("De bestuurder heeft alcohol gedronken: zijn reactietijd is 2 keer zo lang. Wat verandert er?",
      "Alleen de reactieafstand wordt 2 keer zo groot",
      ["De stopafstand wordt precies 2 keer zo groot", "De remweg wordt 2 keer zo groot",
       "Reactieafstand en remweg worden allebei 2 keer zo groot"],
      "De reactietijd bepaalt alleen de reactieafstand. Het remmen zelf gaat even snel, dus de remweg blijft gelijk."),
    M("Dezelfde auto rijdt nu 36 km/h in plaats van 72 km/h (zelfde remmen). Wat gebeurt er met de remweg?",
      "Die wordt 4 keer zo klein", ["Die wordt 2 keer zo klein", "Die blijft even groot", "Die wordt 8 keer zo klein"],
      "De remweg hangt af van v²: half zo snel → ½ · ½ = ¼ van de remweg, dus 4 keer zo klein."),
    # Context 4: botsen
    O("Leg uit hoe een airbag ervoor zorgt dat de kracht op je hoofd kleiner wordt." + EEN_ZIN,
      ["langer/langere/tijd/oppervlak/verlengt/zachter"], 1,
      "De botsing duurt langer (en de kracht wordt verdeeld over een groter oppervlak), dus de kracht is kleiner.",
      "Een airbag verlengt de tijd van de botsing voor je hoofd en verdeelt de kracht over een groter oppervlak → kleinere kracht."),
    W("Een kreukelzone maakt de botstijd korter, zodat de auto sneller stilstaat en de inzittenden veiliger zijn.",
      False, "Onwaar: de kreukelzone maakt de botstijd juist LANGER. Langer afremmen → kleinere vertraging → kleinere kracht."),
    # Context 5: arbeid
    M("Een verhuizer duwt een kast met constante snelheid 5,0 m over de vloer. De wrijvingskracht is 240 N. Hoe groot is de duwkracht?",
      "240 N", ["0 N", "480 N", "Meer dan 240 N, anders schuift de kast niet"], "Constante snelheid → Fres = 0 N → duwkracht = wrijvingskracht = 240 N."),
    I("Bereken de arbeid die de verhuizer verricht als hij de kast met constante snelheid 5,0 m verschuift (wrijving 240 N).",
      "1200|1 200|1200 J|1 200 J", "W = F · s = 240 · 5,0 = 1200 J."),
    M("De kast schuift met constante snelheid, dus hij krijgt er geen bewegingsenergie bij. In welke energie wordt de arbeid van de verhuizer omgezet?",
      "Warmte, door de wrijving", ["Bewegingsenergie van de kast", "Chemische energie in de kast", "Elektrische energie"],
      "De wrijving verricht even veel negatieve arbeid. Die energie wordt omgezet in warmte (vloer en kast worden een beetje warm)."),
]),

116: ("eind", "Toets 116 — Proefwerk H1 (oefenen zoals het echt is) — B", "📝", [
    # Context 1: sledehonden
    I("Zes sledehonden trekken een slee vanuit stilstand 15 m vooruit. Elke hond trekt met 50 N; er is geen wrijving. Bereken de arbeid die één hond verricht in J.",
      "750|750 J", "W = F · s = 50 · 15 = 750 J."),
    I("Zes honden trekken elk met 50 N de slee 15 m vooruit. Hoeveel kJ arbeid verrichten ze samen?",
      "4,5|4.5|4,5 kJ", "Per hond 50 · 15 = 750 J; samen 6 · 750 = 4500 J = 4,5 kJ."),
    M("Er is geen wrijving. Wat gebeurt er met de arbeid die de honden verrichten?",
      "Die wordt bewegingsenergie van de slee", ["Die verdwijnt, want de honden worden moe", "Die wordt omgezet in zwaartekracht op de slee", "Die blijft opgeslagen in de spieren van de honden"],
      "Arbeid is overgedragen energie. Zonder wrijving wordt alle arbeid bewegingsenergie: de slee gaat steeds sneller."),
    W("Daarna stoppen de honden met trekken. De wrijving van de sneeuw verricht dan negatieve arbeid en de slee gaat langzamer.",
      True, "Waar: de wrijving werkt tegen de beweging in → negatieve arbeid → bewegingsenergie wordt warmte → slee vertraagt."),
    # Context 2: trein (v,t)
    M("Het diagram hoort bij een treinrit tussen twee stations. Hoe beweegt de trein in het middelste deel (40 s tot 100 s)?"
      + graf("v", [("", [(0, 0), (40, 20), (100, 20), (120, 0)])], 120, 24),
      "Hij rijdt met constante snelheid", ["Hij staat stil", "Hij versnelt", "Hij remt af"],
      "Tussen 40 en 100 s is de lijn horizontaal bij 20 m/s: de snelheid verandert niet → constante snelheid."),
    I("De trein uit het diagram gaat in de eerste 40 s van 0 naar 20 m/s. Bereken de versnelling in m/s².",
      "0,5|0.5|0,50|0,5 m/s²", "a = Δv : t = 20 : 40 = 0,5 m/s²."),
    I("Bereken hoeveel meter de trein aflegt tijdens het optrekken (van t = 0 tot t = 40 s)."
      + graf("v", [("", [(0, 0), (40, 20), (100, 20), (120, 0)])], 120, 24),
      "400|400 m", "Oppervlakte driehoek: ½ · 40 · 20 = 400 m (of v_gem 10 m/s · 40 s)."),
    I("Bereken de totale afstand die de trein aflegt in de 120 s van het diagram."
      + graf("v", [("", [(0, 0), (40, 20), (100, 20), (120, 0)])], 120, 24),
      "1800|1 800|1800 m|1 800 m", "Optrekken 400 m + constant 60 · 20 = 1200 m + remmen ½ · 20 · 20 = 200 m → 1800 m."),
    I("Bereken de gemiddelde snelheid van de trein over de hele rit van 120 s in m/s."
      + graf("v", [("", [(0, 0), (40, 20), (100, 20), (120, 0)])], 120, 24),
      "15|15 m/s", "Totale afstand = oppervlakte = 400 + 1200 + 200 = 1800 m. v_gem = s : t = 1800 : 120 = 15 m/s."),
    # Context 3: parachutist
    I("Een parachutist heeft met uitrusting een massa van 80 kg. Bereken de zwaartekracht op hem (g = 9,81 N/kg).",
      "785|784,8|784|780|785 N|784,8 N|784.8", "Fz = m · g = 80 · 9,81 = 784,8 N ≈ 785 N."),
    M("Na een tijdje valt de parachutist met een constante snelheid van 50 m/s. Welke uitspraak klopt dan?",
      "Luchtweerstand en zwaartekracht zijn even groot",
      ["Er werkt geen luchtweerstand meer", "De zwaartekracht is groter dan de luchtweerstand", "De luchtweerstand is groter dan de zwaartekracht"],
      "Constante snelheid → Fres = 0 N → luchtweerstand omhoog = zwaartekracht omlaag."),
    M("Dan gaat de parachute open: de luchtweerstand wordt veel groter dan de zwaartekracht. Wat gebeurt er met de parachutist?",
      "Hij gaat langzamer vallen", ["Hij gaat omhoog", "Hij gaat sneller vallen", "Zijn snelheid blijft gelijk"],
      "Fres wijst nu omhoog, tegen de beweging in → hij vertraagt. Hij gaat niet omhoog: hij valt alleen minder snel."),
    W("Na het openen valt hij weer met een constante (lagere) snelheid. Dan is de luchtweerstand weer gelijk aan de zwaartekracht.",
      True, "Waar: weer constante snelheid → weer Fres = 0 N → Fw = Fz, nu bij een lagere snelheid."),
    # Context 4: scooter remt
    I("Een scooter (met bestuurder 130 kg) rijdt 45 km/h en remt in 2,5 s tot stilstand. Reken 45 km/h om naar m/s.",
      "12,5|12.5|12,5 m/s", "45 : 3,6 = 12,5 m/s."),
    I("De scooter remt in 2,5 s van 45 km/h tot stilstand. Bereken de vertraging in m/s².",
      "5|5,0|5 m/s²|5,0 m/s²", "45 km/h = 12,5 m/s. a = Δv : t = 12,5 : 2,5 = 5 m/s²."),
    I("Bereken de remkracht op de scooter met bestuurder (130 kg), die in 2,5 s van 45 km/h tot stilstand remt.",
      "650|650 N", "12,5 m/s : 2,5 s = 5 m/s² vertraging; F = m · a = 130 · 5 = 650 N."),
    I("Hoeveel meter schuift de scooter nog door tijdens dat remmen van 2,5 s (vanaf 45 km/h)?",
      "15,6|15,63|15,625|16|15.6|15.63|15.625|15,6 m", "v_gem = 12,5 : 2 = 6,25 m/s. Remweg = 6,25 · 2,5 ≈ 15,6 m."),
    # Context 5: veiligheid
    M("Waarom is een autogordel veilig bij een botsing?",
      "Hij houdt je op je plek en rekt iets mee, dus de botstijd wordt langer",
      ["Hij maakt de auto lichter, waardoor de botsing een stuk minder hard aankomt",
       "Hij maakt de botstijd korter, dus de botsing is sneller voorbij",
       "Hij trekt je naar achteren, waardoor de auto zelf minder hard tegen iets botst"],
      "De gordel houdt je op je plaats en rekt een beetje → je remt langer af → kleinere vertraging → kleinere kracht."),
    M("Twee gelijke auto's botsen even hard. Auto A deukt 0,6 m in, auto B maar 0,2 m. In welke auto werkt de kleinste kracht op de inzittenden?",
      "In auto A", ["In auto B", "In beide even groot", "Dat hangt alleen af van de massa van de inzittenden"],
      "Auto A remt over een langere afstand en dus langere tijd af → kleinere vertraging → kleinere kracht."),
    O("Leg uit waarom de stopafstand altijd groter is dan de remweg." + EEN_ZIN,
      ["reactie/reactieafstand/reactietijd/reageren"], 1,
      "Bij de stopafstand komt de reactieafstand er nog bij.",
      "Stopafstand = reactieafstand + remweg. Tijdens je reactietijd rijd je nog op volle snelheid door."),
]),

117: ("eind", "Toets 117 — Proefwerk H1 (oefenen zoals het echt is) — C", "📝", [
    # Context 1: acceleratie 0–100
    M("In een autofolder staat: 'Acceleratie 0–100: 5,0 seconden'. Wat betekent dat natuurkundig?",
      "De snelheid gaat in 5,0 s van 0 naar 100 km/h",
      ["De auto rijdt 100 km in 5,0 s", "De auto rijdt 100 m in 5,0 s", "De auto rijdt 5,0 s lang 100 km/h"],
      "Acceleratie = versnelling: de snelheid neemt in 5,0 s toe van 0 tot 100 km/h. Het gaat niet over afstand."),
    I("Reken 100 km/h om naar m/s.",
      "27,8|27,78|28|27.8|27.78|27,8 m/s", "100 : 3,6 ≈ 27,8 m/s."),
    I("De auto gaat in 5,0 s van 0 naar 100 km/h. Bereken de versnelling in m/s².",
      "5,6|5,56|5,55|5.6|5.56|5,6 m/s²", "100 km/h ≈ 27,8 m/s. a = Δv : t = 27,8 : 5,0 ≈ 5,6 m/s²."),
    I("De auto van 1500 kg gaat in 5,0 s van 0 naar 100 km/h. Bereken de resulterende kracht in N.",
      "8400|8 400|8300|8 300|8340|8 340|8333|8 333|8325|8400 N|8 400 N|8333 N", "a ≈ 5,6 m/s²; Fres = m · a = 1500 · 5,6 ≈ 8400 N (met 5,56 kom je op 8333 N)."),
    W("Een zwaardere auto met dezelfde resulterende kracht krijgt een kleinere versnelling.",
      True, "Waar: a = Fres : m. Grotere massa bij dezelfde kracht → kleinere versnelling."),
    # Context 2: fietstocht met pauze
    I("Jan fietst een tocht van 24 km. Met pauze erbij is hij 1 uur en 30 minuten onderweg. Bereken zijn gemiddelde snelheid over de hele tocht in km/h.",
      "16|16 km/h", "1 h 30 min = 1,5 h. v = 24 : 1,5 = 16 km/h."),
    I("Van die 1 uur en 30 minuten zat Jan 15 minuten stil (pauze). Bereken zijn gemiddelde snelheid tijdens het fietsen zelf in km/h.",
      "19,2|19.2|19,2 km/h", "Fietstijd = 90 − 15 = 75 min = 1,25 h. v = 24 : 1,25 = 19,2 km/h."),
    M("De fietscomputer van Jan geeft een lagere gemiddelde snelheid aan dan hij meestal fietste. Hoe kan dat?",
      "De pauze telt mee in de tijd", ["De afstand wordt verkeerd gemeten", "Hij fietste steeds langzamer", "De computer telt de pauze als extra afstand"],
      "Tijdens de pauze loopt de tijd door, maar de afstand niet → totale afstand : totale tijd wordt lager."),
    # Context 3: hijskraan
    I("Een hijskraan tilt een container van 2000 kg met constante snelheid omhoog. Hoe groot is de kracht in de kabel in N (g = 9,81 N/kg)?",
      "19620|19 620|19600|19 600|19620 N|19 620 N", "Constante snelheid → kabelkracht = Fz = 2000 · 9,81 = 19 620 N."),
    I("De kraan tilt de container (2000 kg) met constante snelheid 18 m omhoog. Bereken de arbeid van de kabelkracht in kJ.",
      "353|353,2|353,16|353.2|350|353 kJ|353,2 kJ", "F = Fz = 2000 · 9,81 = 19 620 N; W = F · s = 19 620 · 18 = 353 160 J ≈ 353 kJ."),
    M("Welke arbeid verricht de zwaartekracht op de container tijdens het hijsen?",
      "Negatieve arbeid, even groot als die van de kabel",
      ["Positieve arbeid, even groot als die van de kabel", "Geen arbeid, want de snelheid is constant", "Negatieve arbeid, maar veel kleiner dan die van de kabel"],
      "Zwaartekracht omlaag, beweging omhoog → negatief. Constante snelheid: krachten even groot, dus arbeid ook even groot (samen 0 J)."),
    W("Daarna hangt de container stil in de lucht. De kabelkracht verricht dan nog steeds arbeid.",
      False, "Onwaar: de container beweegt niet, s = 0 m → W = F · s = 0 J. Er werkt wel een kracht, maar geen arbeid."),
    # Context 4: noodstop
    I("In de bebouwde kom ziet een bestuurder die 54 km/h (= 15 m/s) rijdt een kind de straat op rennen. Hij reageert na 0,8 s. Hoeveel meter rijdt hij nog door voordat hij gaat remmen?",
      "12|12 m", "s = v · t = 15 · 0,8 = 12 m."),
    I("Op een nat wegdek haalt de bestuurder maar 6,0 m/s² remvertraging. Hoeveel seconden duurt het remmen vanaf 54 km/h?",
      "2,5|2.5|2,5 s", "t = Δv : a = 15 : 6,0 = 2,5 s."),
    I("Hoeveel meter heeft hij op dat natte wegdek nodig om vanaf 54 km/h stil te staan (alleen het remmen)?",
      "18,75|18,8|18.75|18.8|19|18,75 m", "Remtijd 15 : 6,0 = 2,5 s; v_gem = 7,5 m/s; remweg = 7,5 · 2,5 = 18,75 m."),
    I("Het kind staat 30 m voor de auto als de bestuurder het ziet (54 km/h, reactietijd 0,8 s, nat wegdek 6,0 m/s²). Hoeveel meter is zijn totale stopafstand?",
      "30,75|30,8|30.75|30.8|31|30,75 m", "Reactieafstand 15 · 0,8 = 12 m + remweg 7,5 · 2,5 = 18,75 m → 30,75 m. Dat is meer dan 30 m: de auto komt net te laat tot stilstand!"),
    M("Het regent: op het natte wegdek is de remvertraging kleiner. Wat verandert er?",
      "De remweg wordt langer, de reactieafstand blijft gelijk",
      ["De reactieafstand wordt langer, de remweg blijft gelijk", "Alleen de reactietijd wordt langer", "Remweg en reactieafstand worden allebei korter"],
      "Kleinere vertraging → langer remmen → langere remweg. De reactieafstand hangt alleen af van snelheid en reactietijd."),
    # Context 5: klimtouw
    M("Een klimmer gebruikt een touw dat kan uitrekken. Waarom is dat veiliger bij een val?",
      "De val wordt over een langere tijd afgeremd, dus de kracht is kleiner",
      ["Het touw is lichter, dus de klimmer valt minder hard", "De klimmer valt dan minder diep naar beneden", "De zwaartekracht op de klimmer wordt kleiner"],
      "Het rekken verlengt de tijd van het afremmen → kleinere vertraging → kleinere kracht op de klimmer (net als een kreukelzone)."),
    I("Een klimmer van 60 kg wordt door het touw afgeremd met een vertraging van 20 m/s². Bereken de resulterende kracht op de klimmer in N.",
      "1200|1 200|1200 N|1 200 N", "Fres = m · a = 60 · 20 = 1200 N."),
    O("Op de verpakking staat: vervang het touw na een flinke val. Waarom?" + EEN_ZIN,
      ["vervormd/vervorming/blijvend/plastisch/uitgerekt/kapot/zwakker"], 1,
      "Het touw is blijvend (plastisch) vervormd en rekt niet meer goed mee.",
      "Na een flinke val is het touw plastisch vervormd: het rekt niet meer zoals eerst en vangt een volgende val slechter op."),
]),

118: ("eind", "Toets 118 — Proefwerk H1 (oefenen zoals het echt is) — D", "📝", [
    # Context 1: skateboarder
    I("Een skateboarder (met board 45 kg) zet af vanuit stilstand. De resulterende kracht is 90 N. Bereken zijn versnelling in m/s².",
      "2|2,0|2 m/s²|2,0 m/s²", "a = Fres : m = 90 : 45 = 2 m/s²."),
    I("De skateboarder (45 kg, Fres = 90 N) zet 3,0 s lang af vanuit stilstand. Bereken zijn snelheid na 3,0 s in m/s.",
      "6|6,0|6 m/s|6,0 m/s", "a = 90 : 45 = 2 m/s²; v = a · t = 2 · 3,0 = 6 m/s."),
    I("Hoeveel meter legt de skateboarder (45 kg, Fres = 90 N) af tijdens die 3,0 s afzetten vanuit stilstand?",
      "9|9,0|9 m|9,0 m", "a = 2 m/s², eindsnelheid 2 · 3,0 = 6 m/s; v_gem = 3 m/s; s = 3 · 3,0 = 9 m."),
    O("Daarna zet hij niet meer af en rolt hij uit op een vlakke weg. Hij wordt steeds langzamer. Door welke kracht(en)?" + EEN_ZIN,
      ["wrijving/weerstand/luchtweerstand/rolweerstand"], 1,
      "Door de wrijving (rolweerstand en luchtweerstand).",
      "Rolweerstand en luchtweerstand werken tegen de beweging in → Fres naar achteren → vertragen."),
    # Context 2: (s,t) twee lopers
    M("Lopers A en B lopen 100 m. Kijk naar het (s,t)-diagram. Wie loopt het snelst?"
      + graf("s", [("A", [(0, 0), (20, 100)]), ("B", [(0, 0), (25, 100)])], 25, 100),
      "Loper A", ["Loper B", "Ze lopen even snel", "Dat kun je niet zien in een (s,t)-diagram"],
      "In een (s,t)-diagram geldt: hoe steiler de lijn, hoe groter de snelheid. A is na 20 s al bij 100 m, B pas na 25 s."),
    I("Loper A loopt 100 m in 20 s. Bereken zijn snelheid in m/s.",
      "5|5,0|5 m/s|5,0 m/s", "v = s : t = 100 : 20 = 5 m/s."),
    I("Hoeveel meter per seconde haalt loper B, die pas na 25 s over de finish komt?",
      "4|4,0|4 m/s|4,0 m/s", "v = s : t = 100 : 25 = 4 m/s."),
    W("Loper B blijft na de finish staan. Zijn lijn in het (s,t)-diagram loopt daarna horizontaal.",
      True, "Waar: stilstaan = de afstand verandert niet meer → horizontale lijn in een (s,t)-diagram."),
    # Context 3: auto op snelweg
    M("Op de A2 staat de cruise control aan: de auto houdt precies dezelfde snelheid vast. De motor levert 900 N. Hoeveel tegenwerkende kracht is er dan?",
      "900 N", ["0 N", "1800 N", "Minder dan 900 N, anders rijdt de auto niet"], "Constante snelheid → Fres = 0 N → Ftegen = Fmotor = 900 N."),
    I("De motor duwt de auto met 900 N vooruit over een afstand van 10 km. Bereken de arbeid van de motorkracht in kJ.",
      "9000|9 000|9000 kJ|9 000 kJ", "10 km = 10 000 m. W = 900 · 10 000 = 9 000 000 J = 9000 kJ."),
    M("De bestuurder gaat langzamer rijden: van 120 km/h naar 100 km/h. Wat gebeurt er met de luchtweerstand?",
      "Die wordt kleiner", ["Die wordt groter", "Die blijft even groot", "Die wordt 0 N"],
      "De luchtweerstand hangt af van de snelheid: langzamer rijden → minder luchtweerstand."),
    I("Reken 120 km/h om naar m/s.",
      "33,3|33,33|33|33.3|33.33|33,3 m/s", "120 : 3,6 ≈ 33,3 m/s."),
    I("Op de A2 (120 km/h) kijkt de bestuurder even naar zijn telefoon en reageert pas na 1,2 s op een file. Hoeveel meter is hij dan nog op volle snelheid doorgereden?",
      "40|40 m", "120 km/h ≈ 33,3 m/s; s = v · t = 33,3 · 1,2 ≈ 40 m."),
    # Context 4: botsproef
    I("Bij een botsproef rijdt een auto van 1200 kg met 15 m/s tegen een muur en staat na 0,12 s stil. Bereken de vertraging in m/s².",
      "125|125 m/s²", "a = Δv : t = 15 : 0,12 = 125 m/s²."),
    I("Bereken de kracht op de auto van 1200 kg die bij de botsproef in 0,12 s van 15 m/s tot stilstand komt.",
      "150000|150 000|150000 N|150 000 N", "a = 15 : 0,12 = 125 m/s²; F = m · a = 1200 · 125 = 150 000 N."),
    M("Een auto met een betere kreukelzone doet 3 keer zo lang over dezelfde botsing. Wat gebeurt er met de kracht?",
      "Die wordt 3 keer zo klein", ["Die wordt 3 keer zo groot", "Die wordt 9 keer zo klein", "Die blijft even groot"],
      "3 keer zo lange tijd → vertraging 3 keer zo klein → F = m · a ook 3 keer zo klein."),
    W("Bij een botsing vangt het opgeblazen kussen je hoofd én borst op, zodat de kracht over meer plekken tegelijk verdeeld wordt.",
      True, "Waar: het kussen raakt je hoofd en borst over een groot oppervlak, en het verlengt de botstijd."),
    # Context 5: arbeid
    M("Vier leerlingen zijn in de gymzaal bezig. Bij wie verricht de spierkracht arbeid volgens de natuurkunde?",
      "Je duwt een winkelwagen 10 m vooruit",
      ["Je duwt zo hard je kunt tegen een muur", "Je houdt een zware tas stil vast", "Je draagt een tas horizontaal (je kracht is omhoog)"],
      "Arbeid alleen als er verplaatsing is in de richting van de kracht. Muur en stilhouden: geen verplaatsing; tas dragen: kracht loodrecht op de beweging."),
    I("Bij het kogelstoten strekt Fleur haar arm: ze duwt de kogel 1,6 m ver met een kracht van 250 N. Hoeveel joule arbeid verricht haar spierkracht?",
      "400|400 J", "W = F · s = 250 · 1,6 = 400 J."),
    M("Welke energieomzetting vindt plaats als de kogelstootster de kogel wegduwt?",
      "Chemische energie (voedsel) wordt bewegingsenergie",
      ["Bewegingsenergie wordt chemische energie", "Warmte wordt bewegingsenergie", "Elektrische energie wordt warmte"],
      "De spierkracht draagt chemische energie uit voedsel over aan de kogel, in de vorm van bewegingsenergie."),
]),

119: ("eind", "Toets 119 — Proefwerk H1 (oefenen zoals het echt is) — E", "📝", [
    # Context 1: wielrenner
    I("Een wielrenner heeft met fiets een massa van 75 kg. Bereken de zwaartekracht op renner en fiets in N (g = 9,81 N/kg).",
      "736|735,75|735,8|735|740|736 N|735.75", "Fz = m · g = 75 · 9,81 = 735,75 ≈ 736 N."),
    I("In een bergetappe komt de renner (75 kg met fiets) 1200 m hoger. Bereken de arbeid tegen de zwaartekracht in kJ.",
      "883|882,9|882|880|882.9|883 kJ|882,9 kJ", "W = F · s = 735,75 · 1200 = 882 900 J ≈ 883 kJ."),
    W("In de afdaling verricht de zwaartekracht positieve arbeid op de renner.",
      True, "Waar: zwaartekracht omlaag en de renner gaat omlaag → kracht en beweging dezelfde kant op → positieve arbeid."),
    M("Op een vlak stuk rijdt de renner met constante snelheid. De weerstand is 40 N. Hoeveel arbeid verricht hij per kilometer?",
      "40 kJ", ["40 J", "4 kJ", "40 000 kJ"],
      "Trapkracht = weerstand = 40 N. W = 40 · 1000 m = 40 000 J = 40 kJ."),
    # Context 2: uitrijden
    I("Sophia fietst 5,0 m/s, stopt met trappen en rolt eenparig vertraagd 50 m door tot ze stilstaat. Bereken haar gemiddelde snelheid tijdens het uitrijden.",
      "2,5|2.5|2,5 m/s", "v_gem = (5,0 + 0) : 2 = 2,5 m/s."),
    I("Sophia rolt vanaf 5,0 m/s eenparig 50 m uit tot stilstand. Bereken hoeveel seconden het uitrijden duurt.",
      "20|20 s", "v_gem = 2,5 m/s; t = s : v_gem = 50 : 2,5 = 20 s."),
    I("Bereken de vertraging van Sophia tijdens het uitrijden (vanaf 5,0 m/s, 50 m tot stilstand).",
      "0,25|0.25|0,25 m/s²", "Uitrijtijd = 50 : 2,5 = 20 s; a = Δv : t = 5,0 : 20 = 0,25 m/s²."),
    I("Sophia en haar fiets hebben samen 80 kg massa. Bereken de tegenwerkende kracht tijdens het uitrijden (5,0 m/s → 0 over 50 m).",
      "20|20 N", "Vertraging 0,25 m/s² (zie hierboven); F = m · a = 80 · 0,25 = 20 N."),
    M("Welke arbeid verricht de tegenwerkende kracht op Sophia tijdens de 50 m uitrijden?",
      "−1000 J", ["+1000 J", "0 J", "−50 J"], "W = F · s = 20 · 50 = 1000 J (negatieve arbeid, want tegen de beweging in)."),
    M("Wat gebeurt er met de bewegingsenergie van Sophia tijdens het uitrijden?",
      "Die wordt omgezet in warmte", ["Die wordt omgezet in chemische energie", "Die blijft gelijk", "Die verdwijnt zonder dat er iets mee gebeurt"],
      "De weerstand verricht negatieve arbeid: de bewegingsenergie wordt warmte. Energie verdwijnt nooit."),
    # Context 3: noodstop (v,t)
    M("Dit is het (v,t)-diagram van een noodstop. Tot welk tijdstip is de bestuurder nog aan het reageren?"
      + graf("v", [("", [(0, 15), (0.8, 15), (3.8, 0)])], 4, 16),
      "Tot t = 0,8 s", ["Tot t = 0 s", "Tot t = 3,8 s", "Tot t = 3,0 s"],
      "Tijdens de reactietijd is de snelheid nog constant (horizontale lijn). Bij 0,8 s begint de lijn te dalen: dan wordt er geremd."),
    I("Bereken met het diagram de reactieafstand in m."
      + graf("v", [("", [(0, 15), (0.8, 15), (3.8, 0)])], 4, 16),
      "12|12 m", "Rechthoek onder de horizontale lijn: 15 · 0,8 = 12 m."),
    I("Bereken met het diagram de remweg in m."
      + graf("v", [("", [(0, 15), (0.8, 15), (3.8, 0)])], 4, 16),
      "22,5|22.5|22,5 m", "Driehoek van 0,8 s tot 3,8 s: ½ · 3,0 · 15 = 22,5 m."),
    I("Bereken met het diagram de remvertraging in m/s²."
      + graf("v", [("", [(0, 15), (0.8, 15), (3.8, 0)])], 4, 16),
      "5|5,0|5 m/s²|5,0 m/s²", "Remmen duurt 3,8 − 0,8 = 3,0 s. a = Δv : t = 15 : 3,0 = 5 m/s²."),
    I("Bereken met het diagram de stopafstand in m."
      + graf("v", [("", [(0, 15), (0.8, 15), (3.8, 0)])], 4, 16),
      "34,5|34.5|34,5 m", "Reactieafstand 15 · 0,8 = 12 m + remweg ½ · 3,0 · 15 = 22,5 m → 34,5 m."),
    # Context 4: sleepboot
    I("Een sleepboot trekt een schip met constante snelheid. De trekkracht is 25 kN. Hoe groot is de waterweerstand op het schip in N?",
      "25000|25 000|25000 N|25 000 N", "Constante snelheid → weerstand = trekkracht = 25 kN = 25 000 N."),
    M("De sleepboot trekt nu met 30 kN. De weerstand is eerst nog 25 kN. Wat gebeurt er met het schip?",
      "Het versnelt, met Fres = 5 kN", ["Het vertraagt, met Fres = 5 kN", "Het vaart even snel door", "Het versnelt, met Fres = 55 kN"],
      "Tegengestelde krachten trek je af: 30 − 25 = 5 kN vooruit → versnellen. 55 kN is opgeteld."),
    I("Het schip heeft een massa van 500 000 kg en Fres = 5000 N. Bereken de versnelling in m/s².",
      "0,01|0.01|0,010|0,01 m/s²", "a = Fres : m = 5000 : 500 000 = 0,01 m/s². Een zwaar schip versnelt heel langzaam."),
    # Context 5
    M("Een brommer rijdt eerst 15 km/h en daarna 45 km/h. Hoe verandert de remweg (zelfde remkracht)?",
      "Die wordt 9 keer zo lang", ["Die wordt 3 keer zo lang", "Die wordt 6 keer zo lang", "Die blijft even lang"],
      "45 km/h is 3 keer zo snel. Remweg ~ v²: 3 · 3 = 9 keer zo lang."),
    O("Leg uit waarom een auto die met constante snelheid rijdt toch motorkracht nodig heeft." + EEN_ZIN,
      ["weerstand/wrijving/luchtweerstand/rolweerstand/tegenwerkende"], 1,
      "Om de weerstand op te heffen: Fmotor = Fw, dus Fres = 0 N.",
      "Zonder motorkracht zou alleen de weerstand overblijven en vertraagt de auto. Bij constante snelheid is Fmotor = Fw."),
]),
}


def main():
    rng = random.Random("natuurkunde_h1_proefwerk_115_119")
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
              "vak": "Natuurkunde · HAVO 3 (H1)", "icoon": icoon, "duurMin": 45, "vragen": vr}
        kop = (f"/* =========================================================\n   Duru's Natuurkunde (HAVO 3) — {titel}\n"
               f"   Gegenereerd door tools/gen_natuurkunde_h1_proefwerk_115_119.py\n"
               f"   ========================================================= */\n")
        with open(os.path.join(ROOT, f"examen_{nr}.js"), "w", encoding="utf-8") as f:
            f.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")


if __name__ == "__main__":
    main()
