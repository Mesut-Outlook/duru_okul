#!/usr/bin/env python3
"""Nederlands HAVO 3 · Foutentraining A/B/C (examen_71…73.js, ex-h3-nederlands-71…73) — 2026-11-08.

Kullanıcı isteği: "Duru'nun Nederlands'ta son 10 sınavda yaptığı yanlış ve boşlardan oluşan 3 test".
Bron: buluttaki son 10 poging (48, 67, 63, 61, 41, 38, 68 ×2, 69, 70), vraag voor vraag. Patronen:
  1. voor-/achterwaarts systematisch omgekeerd (11×) → stapsgewijs: eerst "waar staat het woord wél?"
  2. verwijzen: het meisje → die, regering/gemeente/politie → zijn/hun, dingen → het, niets wat/dat
  3. hun/hen  4. streepje (heel woord vs deel van een woord)  5. functie/getal + woordvolgorde
  6. gebeurd/gebeurt, vt mv -den, Wordt u, Engelse ww  7. -n (enkelen/beiden/anderen), een klein hotel
  8. apostrof/accent (spraytje, café, kiwi's)
Open vragen: één taak per vraag ("leg in één zin uit …") — Duru schreef bij "verbeter + waarom" steeds alleen
de verbeterde zin. Elke toets: Deel A Grammatica (1–14) → Deel B Spelling (15–20).

Draai: python3 tools/gen_nederlands_foutentraining.py
Daarna: node tools/gate.js nederlands && node tools/open_check.js && node tools/teslim_check.js nederlands 71
"""
import random
import gen_nederlands_oefenproefwerk as gp
from gen_nederlands_oefenproefwerk import mc, I, W, O

gp.rng = random.Random("foutentraining_2026_11_08")
EERSTE = 71
KOP = "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Foutentraining C5 + C7) — gegenereerd door tools/gen_nederlands_foutentraining.py */"

VOOR = "Voorwaarts = het woord dat je weglaat staat <b>vooraan</b> (in het eerste deel) en valt later weg. Achterwaarts = het woord staat <b>achteraan</b> en valt eerder weg. Kijk dus waar het woord wél staat, niet waar het gat zit."

TOETSEN = []

# =====================================================================================================
# 71 · Foutentraining A
# =====================================================================================================
TOETSEN.append(dict(letter="A", vragen=[
    # --- Deel A · Grammatica ---
    mc("<i>Emma eet een appel en Joris een peer.</i> Welk woord is weggelaten, en waar staat dat woord wél?",
       "'eet' – het staat vooraan, in het eerste deel",
       ["'eet' – het staat achteraan, in het tweede deel", "'peer' – het staat vooraan, in het eerste deel", "'Joris' – het staat achteraan, in het tweede deel"],
       "… en Joris [eet] een peer. Het weggelaten woord <i>eet</i> staat wél in het eerste deel, dus vooraan."),
    mc("Het weggelaten woord staat wél in het eerste deel en valt in het tweede deel weg. Hoe heet zo'n samentrekking?",
       "voorwaartse samentrekking", ["achterwaartse samentrekking", "ongelijkwaardige samentrekking", "geen samentrekking"],
       VOOR),
    mc("<i>Zowel de linker- als de rechterdeur klemt.</i> Welke omschrijving klopt?",
       "achterwaarts: '-deur' staat achteraan", ["voorwaarts: '-deur' staat vooraan", "voorwaarts: 'linker' staat vooraan", "achterwaarts: 'linker' staat achteraan"],
       "Linker[deur] en rechterdeur: het gemeenschappelijke deel <i>deur</i> staat achteraan en valt eerder weg → achterwaarts. " + VOOR),
    W("<i>Ik koop brood bij de bakker en mijn broer kaas bij de kaasboer.</i> is een achterwaartse samentrekking.", False,
      "<i>Koop</i> staat vooraan (eerste deel) en valt later weg: … en mijn broer [koopt] kaas. Dat is voorwaarts."),
    mc("Kies het juiste verwijswoord: <i>Het kind ____ in de rij voor mij stond, kreeg het laatste ijsje.</i>",
       "dat", ["die", "wat", "wie"],
       "Kind is een het-woord (het kind) → dat. Ook bij personen beslist het lidwoord: het meisje dat, het kind dat."),
    mc("Welke zin met hun of hen is goed?",
       "Wij hebben hun de weg gewezen.",
       ["Wij hebben hen de weg gewezen.", "Wij hebben de weg aan hun gewezen.", "Hun hebben ons de weg gewezen."],
       "Meewerkend voorwerp zónder voorzetsel → hun. Na een voorzetsel (aan hen) → hen. Als onderwerp → zij."),
    O("Leg in één zin uit waarom je <i>Ik gaf hun een cadeau</i> schrijft, maar <i>Ik gaf een cadeau aan hen</i>.",
      ["voorzetsel"],
      "Zonder voorzetsel schrijf je hun (meewerkend voorwerp); na een voorzetsel zoals aan schrijf je hen.",
      "Hun = meewerkend voorwerp zonder voorzetsel. Hen = na een voorzetsel (aan, voor, met, op)."),
    mc("Kies het juiste verwijswoord: <i>De directie heeft ____ besluit aan alle ouders uitgelegd.</i>",
       "haar", ["zijn", "hun", "het"],
       "Directie is een vrouwelijk woord (op -ie, een instantie, net als regering, gemeente, politie) → haar."),
    mc("Kies het juiste verwijswoord: <i>Waar is mijn telefoon? Ik kan ____ nergens vinden.</i>",
       "hem", ["het", "haar", "hen"],
       "Telefoon is een de-woord voor een ding → hem. <i>Het</i> gebruik je alleen voor het-woorden (het boek → het)."),
    W("In <i>Alles dat je zegt, schrijf ik op.</i> is het verwijswoord goed gekozen.", False,
      "Na alles, niets, iets en veel gebruik je wat: alles wat je zegt."),
    mc("Waarom is deze samentrekking fout? <i>Mijn zus woont in Utrecht en mijn ouders in Zwolle.</i>",
       "Het getal verschilt (woont ↔ wonen)", ["De functie verschilt", "Er is niets fout", "Het is een achterwaartse samentrekking"],
       "Bij mijn ouders hoort <i>wonen</i>, niet <i>woont</i>. Het weggelaten woord moet precies dezelfde vorm hebben."),
    O("De zin <i>Na school gaat Ilse naar hockey en Bram speelt piano.</i> is fout. Schrijf het tweede deel van de zin goed op.",
      ["speelt Bram/speelt hij"],
      "Na school gaat Ilse naar hockey en speelt Bram piano.",
      "'Na school' geldt ook voor het tweede deel. Na een bepaling vooraan komt eerst de persoonsvorm: en [na school] speelt Bram piano."),
    W("In <i>houten en plastic stoelen</i> schrijf je geen streepje, omdat <i>stoelen</i> een heel woord is.", True,
      "Er valt een heel woord weg (stoelen), geen deel van een woord → geen streepje."),
    I("Schrijf korter met een samentrekking: <i>speeltuinen en speelvelden</i>.", "speeltuinen en -velden|speeltuinen en - velden",
      "Het gemeenschappelijke deel (speel) staat vooraan en valt in het tweede woord weg → streepje vóór het tweede deel: speeltuinen en -velden."),
    # --- Deel B · Spelling ---
    mc("Kies de juiste vorm: <i>Is er vandaag op school iets bijzonders ____ (gebeuren)?</i>",
       "gebeurd", ["gebeurt", "gebeurdt", "gebeurde"],
       "<i>Is … gebeurd</i>: voltooid deelwoord bij <i>is/zijn</i>. Verlengen: het gebeurde ongeluk → d."),
    I("Vorige maand ____ (verhuizen) onze buren naar Groningen.", "verhuisden",
      "Stam verhuis (s) → 't kofschip X? De s komt van een z (verhuizen) → -de. Onderwerp meervoud (onze buren) → -den: verhuisden."),
    W("In <i>Word u ook zo moe van lange vergaderingen?</i> is de persoonsvorm goed gespeld.", False,
      "Bij u blijft de t altijd staan, ook als u achter de persoonsvorm staat: Wordt u …?"),
    I("Ik heb de foto's gisteren naar mijn oma ____ (mailen).", "gemaild",
      "Stam mail eindigt op een l-klank → niet in 't kofschip X → ge + mail + d = gemaild."),
    mc("Kies de juiste combinatie: <i>De twee broers? ____ spelen in hetzelfde team, maar de ____ jongens uit de klas niet.</i>",
       "Beiden – andere", ["Beide – andere", "Beiden – anderen", "Beide – anderen"],
       "<i>Beiden</i> staat zelfstandig voor personen → met n. <i>Andere</i> staat vóór een zelfstandig naamwoord (jongens) → zonder n."),
    I("Verbeter het fout gespelde woord: <i>Na de wedstrijd dronken we iets in het cafe naast het stadion.</i>", "café",
      "Café spreek je uit met een gesloten é-klank (als in 'thee') → accent aigu: café. Bij een open klank (première) schrijf je è."),
]))

# =====================================================================================================
# 72 · Foutentraining B
# =====================================================================================================
TOETSEN.append(dict(letter="B", vragen=[
    # --- Deel A · Grammatica ---
    mc("<i>Lisa schrijft een brief en Mo een kaart.</i> Waar staat <i>schrijft</i>, het woord dat in het tweede deel wegvalt, en wat voor samentrekking is het dus?",
       "vooraan → voorwaartse samentrekking",
       ["achteraan → achterwaartse samentrekking", "vooraan → achterwaartse samentrekking", "achteraan → voorwaartse samentrekking"],
       "<i>Schrijft</i> staat in het eerste deel = vooraan → voorwaarts. " + VOOR),
    mc("<i>Zowel winter- als zomerbanden zijn in de aanbieding.</i> Welke omschrijving klopt?",
       "achterwaarts: 'banden' staat achteraan", ["voorwaarts: 'banden' staat vooraan", "achterwaarts: 'winter' staat achteraan", "voorwaarts: 'zomer' staat vooraan"],
       "Winter[banden] en zomerbanden: <i>banden</i> staat achteraan en valt eerder weg → achterwaarts."),
    W("<i>hand- en voetbal</i> is een voorwaartse samentrekking.", False,
      "Het gemeenschappelijke deel <i>bal</i> staat achteraan (voetbal) en valt eerder weg (hand[bal]) → achterwaarts."),
    mc("<i>De winkel verkoopt fietsen en de garage auto's.</i> Wat voor samentrekking is dit?",
       "voorwaartse samentrekking", ["achterwaartse samentrekking", "samentrekking op woordniveau", "geen samentrekking"],
       "<i>Verkoopt</i> staat vooraan en valt later weg: … en de garage [verkoopt] auto's → voorwaarts, op zinsniveau."),
    mc("Kies het juiste verwijswoord: <i>Het meisje ____ de hoofdrol speelt, zit bij mij in de klas.</i>",
       "dat", ["die", "wat", "wie"],
       "Meisje is een het-woord (het meisje) → dat. Dat het een persoon is, maakt niet uit: het lidwoord beslist."),
    mc("In welke zin over de trainer staat een <b>fout</b> verwijswoord?",
       "De trainer gaf hen een compliment.",
       ["De trainer was trots op hen.", "De trainer gaf hun een compliment.", "Zij kregen een compliment van de trainer."],
       "Meewerkend voorwerp zonder voorzetsel → hun: de trainer gaf hun een compliment. <i>Trots op hen</i> is goed (na voorzetsel)."),
    O("Leg in één zin uit waarom je <i>het meisje dat</i> schrijft en niet <i>het meisje die</i>.",
      ["het-woord/lidwoord"],
      "Meisje is een het-woord: het lidwoord beslist, niet of het een persoon is, dus dat.",
      "Het-woord → dat; de-woord → die. Ook voor personen: het meisje dat, het kind dat."),
    mc("Welk verwijswoord hoort op de puntjes? <i>De regering presenteerde in de Tweede Kamer ____ klimaatplan.</i>",
       "haar", ["zijn", "hun", "het"],
       "Regering is een vrouwelijk woord (op -ing) → haar."),
    mc("Kies het juiste verwijswoord: <i>Ik heb een nieuwe laptop gekregen. Ik gebruik ____ elke dag.</i>",
       "hem", ["het", "haar", "hen"],
       "Laptop is een de-woord voor een ding → hem."),
    W("In <i>Er is iets wat ik je moet vertellen.</i> is het verwijswoord goed gekozen.", True,
      "Na iets, niets, alles en veel gebruik je wat."),
    mc("Waarom is deze samentrekking fout? <i>Deze film duurt drie uur en vind ik veel te lang.</i>",
       "De functie verschilt", ["Het getal verschilt", "Er is niets fout", "Het is een voorwaartse samentrekking"],
       "<i>Deze film</i> is in het eerste deel onderwerp, maar in het tweede deel lijdend voorwerp (ik vind deze film te lang). Een weggelaten woord moet dezelfde functie hebben."),
    mc("Welke zin is goed na de samentrekking?",
       "Morgen gaat Anne naar de tandarts en haalt Tom zijn rijbewijs.",
       ["Morgen gaat Anne naar de tandarts en Tom haalt zijn rijbewijs.", "Morgen Anne gaat naar de tandarts en haalt Tom zijn rijbewijs.", "Morgen gaat Anne naar de tandarts en Tom zijn rijbewijs haalt."],
       "'Morgen' geldt voor beide delen. Na een bepaling vooraan komt eerst de persoonsvorm: en [morgen] haalt Tom zijn rijbewijs."),
    W("<i>Natte- en droge doekjes</i> schrijf je met een streepje na <i>natte</i>.", False,
      "Er valt een heel woord weg (doekjes), geen deel van een woord → geen streepje: natte en droge doekjes."),
    O("Leg in één zin uit waarom je in <i>tennis- en voetbalclubs</i> wél een streepje schrijft.",
      ["deel/stuk"],
      "Er valt een deel van een woord weg (clubs hoort bij tennisclubs), daarom schrijf je een streepje.",
      "Streepje = er valt een deel van een samenstelling weg. Valt er een heel woord weg, dan geen streepje."),
    # --- Deel B · Spelling ---
    I("Vul de juiste vorm van <i>gebeuren</i> in: <i>Wat is er met je arm ____?</i>", "gebeurd",
      "<i>Is … gebeurd</i>: voltooid deelwoord bij is/zijn → verlengen: het gebeurde → d."),
    mc("Kies de juiste vorm: <i>Gisteren ____ (leggen) de bouwvakkers de nieuwe stoeptegels.</i>",
       "legden", ["legde", "legten", "legte"],
       "Stam leg eindigt op g → niet in 't kofschip X → -de. Onderwerp meervoud (de bouwvakkers) → -den: legden."),
    I("Mijn zus heeft haar hele kamer opnieuw ____ (stylen).", "gestyled",
      "Engels werkwoord: style klinkt als 'stail', eindigt op een l-klank → niet in 't kofschip X → gestyled."),
    W("In <i>Vindt u het goed als ik het raam opendoe?</i> is de persoonsvorm goed gespeld.", True,
      "Bij u blijft de t staan, ook achter de persoonsvorm: Vindt u …? Alleen bij jij/je valt de t weg."),
    I("Vul in met of zonder n: <i>Van alle kandidaten waren er maar ____ (enkel) geschikt.</i>", "enkelen",
      "Zelfstandig gebruikt en het verwijst naar personen (kandidaten) → met n: enkelen."),
    mc("Welk verkleinwoord is <b>fout</b> gespeld?",
       "spray'tje", ["pony'tje", "baby'tje", "jockeytje"],
       "In spray hoort de y bij de klank 'ee' (sprée) → geen apostrof: spraytje. Bij pony en baby klinkt de y als ie → pony'tje, baby'tje."),
]))

# =====================================================================================================
# 73 · Foutentraining C
# =====================================================================================================
TOETSEN.append(dict(letter="C", vragen=[
    # --- Deel A · Grammatica ---
    mc("In welke samentrekking staat het gemeenschappelijke woord <b>achteraan</b> (achterwaarts)?",
       "zowel bruine als witte bonen",
       ["Sem leest een strip en Iris een roman.", "Wij gaan naar Parijs en jullie naar Rome.", "boekenkasten en -planken"],
       "Zowel bruine [bonen] als witte bonen: <i>bonen</i> staat achteraan → achterwaarts. In de andere drie staat het weggelaten woord vooraan."),
    mc("<i>Oma breit een sjaal en opa een muts.</i> Wat voor samentrekking is dit, en waarom?",
       "voorwaarts, want 'breit' staat vooraan",
       ["achterwaarts, want 'breit' staat vooraan", "achterwaarts, want 'breit' ontbreekt achteraan", "voorwaarts, want 'muts' staat achteraan"],
       "Kijk waar het woord wél staat: <i>breit</i> staat vooraan → voorwaarts. Dat het gat achteraan zit, maakt het niet achterwaarts."),
    W("<i>Schoolboeken en -tassen</i> is een voorwaartse samentrekking.", True,
      "Het gemeenschappelijke deel <i>school</i> staat vooraan en valt later weg → voorwaarts, op woordniveau."),
    mc("<i>Zowel lees- als schrijfopdrachten tellen mee voor je cijfer.</i> Wat voor samentrekking is dit?",
       "achterwaarts, op woordniveau", ["voorwaarts, op woordniveau", "achterwaarts, op zinsniveau", "voorwaarts, op zinsniveau"],
       "Een deel van een woord (-opdrachten) valt weg → woordniveau. Het staat achteraan → achterwaarts."),
    mc("Kies het juiste verwijswoord: <i>Het kind ____ ik gisteren met zijn huiswerk hielp, heeft een 8 gehaald.</i>",
       "dat", ["die", "wat", "wie"],
       "Kind is een het-woord → dat (het kind dat …)."),
    mc("Kies de juiste combinatie: <i>Mijn neven kwamen langs. Ik gaf ____ limonade en speelde met ____ een spelletje.</i>",
       "hun – hen", ["hen – hun", "hun – hun", "hen – hen"],
       "Ik gaf hun limonade: meewerkend voorwerp zonder voorzetsel → hun. Met hen: na een voorzetsel → hen."),
    O("Leg in één zin uit waarom het <i>De politie heeft haar onderzoek afgerond</i> is en niet <i>zijn onderzoek</i>.",
      ["vrouwelijk"],
      "Politie is een vrouwelijk woord (een instantie, net als regering en gemeente), dus haar.",
      "Instanties zoals politie, regering, gemeente en directie zijn vrouwelijk → haar."),
    mc("Kies het juiste verwijswoord: <i>Amsterdam is trots op ____ grachten.</i>",
       "zijn", ["haar", "hun", "het"],
       "Namen van steden en landen zijn het-woorden (onzijdig) → zijn. Instanties zoals de gemeente en de regering zijn vrouwelijk → haar."),
    mc("Kies het juiste verwijswoord: <i>Heb je de nieuwe stoel al gezien? Ik vind ____ heel mooi.</i>",
       "hem", ["het", "haar", "hen"],
       "Stoel is een de-woord voor een ding → hem."),
    W("In <i>Er is niets dat ik zo lekker vind als pannenkoeken.</i> is het verwijswoord goed gekozen.", False,
      "Na niets gebruik je wat: er is niets wat ik zo lekker vind."),
    mc("Klopt deze samentrekking? <i>De hond blaft hard en de katten heel zacht.</i>",
       "Nee, het getal verschilt (blaft ↔ blaffen)",
       ["Nee, de functie verschilt", "Ja, het is een voorwaartse samentrekking", "Ja, het is een achterwaartse samentrekking"],
       "Bij de katten hoort <i>blaffen</i>, niet <i>blaft</i>. Het weggelaten werkwoord moet dezelfde vorm hebben."),
    mc("In welke zin is de woordvolgorde <b>fout</b>?",
       "In de pauze eet Kim een broodje en Lars drinkt melk.",
       ["In de pauze eet Kim een broodje en drinkt Lars melk.", "Kim eet in de pauze een broodje en Lars drinkt melk.", "In de pauze eet Kim een broodje en Lars een appel."],
       "'In de pauze' geldt voor beide delen → na de bepaling eerst de persoonsvorm: en [in de pauze] drinkt Lars melk."),
    W("In <i>oude- en nieuwe fietsen</i> is het streepje goed.", False,
      "Er valt een heel woord weg (fietsen) → geen streepje: oude en nieuwe fietsen."),
    O("Schrijf korter met een samentrekking: <i>kinderboeken en kinderliedjes</i>. Zeg er in één zin bij waar het streepje staat.",
      ["-liedjes"],
      "kinderboeken en -liedjes: het streepje staat vóór het tweede deel, omdat kinder vooraan staat.",
      "Het gemeenschappelijke deel (kinder) staat vooraan → streepje vóór het tweede deel: kinderboeken en -liedjes."),
    # --- Deel B · Spelling ---
    mc("Welke zin bevat géén spelfout?",
       "Dit gebeurt elke maandag opnieuw.",
       ["Dit gebeurd elke maandag opnieuw.", "Het is gisteren gebeurt.", "Wat is er gebeurt met de lamp?"],
       "Zonder hulpwerkwoord, tegenwoordige tijd enkelvoud → gebeurt. Met is/zijn → voltooid deelwoord gebeurd."),
    I("Tijdens de vakantie ____ (logeren) wij bij onze tante in Zeeland.", "logeerden",
      "Stam logeer eindigt op r → niet in 't kofschip X → -de. Onderwerp meervoud (wij) → -den: logeerden."),
    W("Het voltooid deelwoord van <i>skaten</i> is <i>geskatet</i>.", True,
      "Skate klinkt als 'skeet', eindigt op een t-klank → 't kofschip X → geskatet."),
    I("____ (worden) u morgen ook om acht uur verwacht?", "wordt",
      "Bij u blijft de t staan, ook als u achter de persoonsvorm staat: Wordt u …?"),
    mc("Welke zin is helemaal goed?",
       "Veel jongeren gingen naar het concert.",
       ["Veel jongere gingen naar het concert.", "De oudsten zus van Sam ging ook mee.", "Beide gingen samen met hun vrienden."],
       "Jongeren: zelfstandig gebruikt voor personen → met n. Vóór een zelfstandig naamwoord geen n: de oudste zus. Zelfstandig voor personen: beiden."),
    I("Verbeter het fout gespelde woord: <i>We aten in de pauze twee kiwis en een appel.</i>", "kiwi's",
      "Kiwi eindigt op een klinker (i); zonder apostrof zou je 'kie-wis' lezen → kiwi's."),
]))

if __name__ == "__main__":
    gp.genereer(TOETSEN, EERSTE, KOP, "Toets {nr} — Foutentraining {letter}: jouw fouten uit de laatste 10 toetsen",
                paragraaf="mix", icoon="🎯")
