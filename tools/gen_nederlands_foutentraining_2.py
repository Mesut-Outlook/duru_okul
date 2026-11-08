#!/usr/bin/env python3
"""Nederlands HAVO 3 · Foutentraining D/E (examen_74…75.js, ex-h3-nederlands-74…75) — 2026-11-08.

Tweede ronde na Foutentraining A/B/C (71–73). Duru maakte 72 drie keer met steeds dezelfde foute antwoorden
→ aanpak gewijzigd (skill zwakte-toetsen: twee rondes onveranderd = andere aanpak):
  - contrastparen in één vraag (het meisje dat / de jongen die · pen → hem / schrift → het · gemeente → haar / Utrecht → zijn)
  - eerst de stap ("welk lidwoord hoort bij meisje?"), dan de toepassing
  - "waarom" eerst als meerkeuze, met haar eigen redenering als afleider ("omdat een meisje vrouwelijk is")
  - één open vraag met zinsbegin ("Maak de zin af: … want …") — 5 "leg uit"-vragen bleven leeg
Spelling ging goed in 71–73; alleen -n en apostrof blijven.

Draai: cd tools && python3 gen_nederlands_foutentraining_2.py
"""
import random
import gen_nederlands_oefenproefwerk as gp
from gen_nederlands_oefenproefwerk import mc, I, W, O

gp.rng = random.Random("foutentraining_2_2026_11_08")
EERSTE = 74
KOP = "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Foutentraining C5 + C7, ronde 2) — gegenereerd door tools/gen_nederlands_foutentraining_2.py */"

TOETSEN = []

# =====================================================================================================
# 74 · Foutentraining D
# =====================================================================================================
TOETSEN.append(dict(letter="D", vragen=[
    mc("Welk lidwoord hoort bij het woord <i>meisje</i>?",
       "het", ["de", "een", "die"],
       "Het meisje. Het lidwoord is <i>het</i>, ook al is een meisje een vrouwelijk persoon. Dat lidwoord bepaalt straks het verwijswoord."),
    mc("Kies de juiste combinatie: <i>Het meisje ____ naast Sem zit en de jongen ____ achter hem zit, zijn een tweeling.</i>",
       "dat – die", ["die – die", "die – dat", "dat – dat"],
       "Het meisje → dat (het-woord). De jongen → die (de-woord). Het lidwoord beslist, niet of het een jongen of een meisje is."),
    mc("Waarom schrijf je <i>het meisje dat</i>?",
       "Omdat meisje een het-woord is",
       ["Omdat een meisje vrouwelijk is", "Omdat het over een persoon gaat", "Omdat je na een persoon altijd dat schrijft"],
       "Alleen het lidwoord telt: het meisje → dat, de vrouw → die. Vrouwelijk of mannelijk speelt hier geen rol."),
    mc("<i>Mijn rugzak is te klein. Ik ga ____ ruilen.</i> Welk woord hoort op de puntjes?",
       "hem", ["het", "haar", "hen"],
       "Rugzak is een de-woord (de rugzak) voor een ding → hem. <i>Het</i> gebruik je alleen voor het-woorden."),
    mc("Kies de juiste combinatie: <i>Ik heb een nieuwe pen en een nieuw schrift. Ik gebruik ____ voor wiskunde en ____ voor Nederlands.</i>",
       "hem – het", ["het – het", "hem – hem", "het – hem"],
       "De pen (de-woord) → hem. Het schrift (het-woord) → het. Kijk dus eerst naar het lidwoord."),
    mc("Kies de juiste combinatie: <i>De gemeente Utrecht wil ____ parken groter maken, want Utrecht is trots op ____ groen.</i>",
       "haar – zijn", ["zijn – zijn", "haar – haar", "zijn – haar"],
       "De gemeente is een instantie (vrouwelijk) → haar. Utrecht is de naam van een stad: steden en landen zijn het-woorden → zijn."),
    W("In <i>Nederland is bekend om zijn molens.</i> is het verwijswoord goed gekozen.", True,
      "Namen van landen en steden zijn het-woorden (onzijdig) → zijn."),
    W("In <i>Alles dat je nodig hebt, staat op de lijst.</i> is het verwijswoord goed.", False,
      "Na alles, niets, iets en veel gebruik je wat: alles wat je nodig hebt."),
    mc("Kies de juiste combinatie: <i>Ik heb mijn vriendinnen geholpen. Ik legde ____ de som uit en liep daarna met ____ naar de kantine.</i>",
       "hun – hen", ["hen – hun", "hun – hun", "hen – hen"],
       "Ik legde hun de som uit: meewerkend voorwerp zonder voorzetsel → hun. Met hen: na een voorzetsel → hen."),
    mc("Waarom is het <i>Ik gaf hun een boek</i> en niet <i>Ik gaf hen een boek</i>?",
       "Het is een meewerkend voorwerp zonder voorzetsel",
       ["Het is een lijdend voorwerp", "Er staat een voorzetsel voor", "Hun is het onderwerp van de zin"],
       "Aan wie gaf ik een boek? Aan hen → zonder 'aan' wordt dat hun (meewerkend voorwerp). Lijdend voorwerp of na een voorzetsel → hen."),
    mc("<i>Jesse koopt een broodje en Noa een salade.</i> Waar staat het weggelaten woord <i>koopt</i> wél?",
       "vooraan, in het eerste deel → voorwaarts",
       ["achteraan, in het tweede deel → achterwaarts", "vooraan, in het eerste deel → achterwaarts", "nergens, het is geen samentrekking"],
       "<i>Koopt</i> staat in het eerste deel = vooraan → voorwaarts. Kijk waar het woord wél staat, niet waar het gat zit."),
    O("Maak de zin af: <i>Het is 'het meisje dat' en niet 'het meisje die', want …</i>",
      ["het-woord/lidwoord"],
      "… want meisje is een het-woord: het lidwoord beslist, niet of het een meisje is.",
      "Het-woord → dat, de-woord → die. Bij personen ook: het meisje dat, het kind dat, de jongen die."),
    mc("<i>Zowel appel- als perentaart staat op het menu.</i> Welke omschrijving klopt?",
       "achterwaarts: '-taart' staat achteraan",
       ["voorwaarts: '-taart' staat vooraan", "voorwaarts: 'appel' staat vooraan", "achterwaarts: 'peren' staat achteraan"],
       "Appel[taart] en perentaart: <i>taart</i> staat achteraan en valt eerder weg → achterwaarts."),
    W("<i>Fietssloten en -bellen</i> is een achterwaartse samentrekking.", False,
      "Het gemeenschappelijke deel <i>fiets</i> staat vooraan en valt later weg → voorwaarts."),
    mc("Maak de zin goed af: <i>Vanavond kijkt mama een film en …</i>",
       "leest papa een boek.", ["papa leest een boek.", "papa een boek leest.", "een boek papa leest."],
       "'Vanavond' geldt ook voor het tweede deel. Na een bepaling vooraan komt eerst de persoonsvorm: en [vanavond] leest papa een boek."),
    W("<i>Op maandag zwemt Fenna en Ruben tennist.</i> is goed na de samentrekking.", False,
      "'Op maandag' geldt voor beide delen → eerst de persoonsvorm: … en tennist Ruben."),
    mc("Welke woordgroep is goed geschreven?",
       "warme en koude truien", ["warme- en koude truien", "warme en- koude truien", "warm- en koude truien"],
       "Er valt een heel woord weg (truien), geen deel van een woord → geen streepje."),
    W("In <i>zomer- en wintertruien</i> is het streepje goed, omdat er een deel van een woord wegvalt.", True,
      "Zomer[truien] en wintertruien: een deel van een samenstelling valt weg → streepje."),
    I("Vul in met of zonder n: <i>Van de dertig leerlingen hadden er maar ____ (weinig) hun huiswerk af.</i>", "weinigen",
      "Zelfstandig gebruikt en het verwijst naar personen (leerlingen) → met n: weinigen."),
    mc("Welk rijtje verkleinwoorden is helemaal goed?",
       "spraytje – pony'tje", ["spray'tje – pony'tje", "spraytje – ponytje", "spray'tje – ponytje"],
       "Spray: de y hoort bij de klank 'ee' → geen apostrof (spraytje). Pony: de y klinkt als ie → apostrof (pony'tje)."),
]))

# =====================================================================================================
# 75 · Foutentraining E
# =====================================================================================================
TOETSEN.append(dict(letter="E", vragen=[
    mc("Welk lidwoord hoort bij <i>kind</i>, en welk verwijswoord dus?",
       "het → dat", ["de → die", "het → die", "de → dat"],
       "Het kind → dat. Eerst het lidwoord zoeken, dan weet je het verwijswoord."),
    mc("Kies het juiste verwijswoord: <i>Het meisje ____ de prijs won, mocht een speech geven.</i>",
       "dat", ["die", "wat", "wie"],
       "Het meisje → dat (het-woord). Niet die, ook al is het een meisje."),
    mc("Kies de juiste combinatie: <i>Het jongetje ____ huilde en de moeder ____ hem troostte, zaten op een bankje.</i>",
       "dat – die", ["die – die", "die – dat", "dat – dat"],
       "Het jongetje (verkleinwoorden zijn altijd het-woorden) → dat. De moeder → die."),
    mc("Waarom schrijf je <i>Mijn fiets? Ik heb hem gisteren gerepareerd.</i> en niet <i>het</i>?",
       "Omdat fiets een de-woord is",
       ["Omdat een fiets mannelijk is", "Omdat het alleen voor personen is", "Omdat je hem voor alle dingen gebruikt"],
       "De fiets → hem. Het boek → het. Bij dingen kijk je naar het lidwoord."),
    mc("<i>Mijn jas is nat. Ik hang ____ even over de verwarming.</i> Welk verwijswoord hoort op de puntjes?",
       "hem", ["het", "haar", "hen"],
       "De jas (de-woord, een ding) → hem."),
    mc("<i>Waar is mijn boek? Ik kan ____ nergens vinden.</i> Welk verwijswoord hoort op de puntjes?",
       "het", ["hem", "haar", "hen"],
       "Het boek is een het-woord → het. Vergelijk: de jas → hem."),
    mc("Welk verwijswoord hoort op de puntjes? <i>De politie vraagt burgers om hulp bij ____ onderzoek.</i>",
       "haar", ["zijn", "hun", "het"],
       "Politie is een instantie en vrouwelijk → haar (net als regering, gemeente, directie)."),
    mc("Kies het juiste verwijswoord: <i>Rotterdam is beroemd om ____ grote haven.</i>",
       "zijn", ["haar", "hun", "het"],
       "Rotterdam is een stad; namen van steden en landen zijn het-woorden → zijn. Niet haar: dat is voor instanties zoals de gemeente."),
    W("<i>Haar</i> gebruik je voor instanties zoals de regering en de gemeente, <i>zijn</i> voor steden en landen zoals Utrecht en Frankrijk.", True,
      "Instanties zijn vrouwelijk → haar. Steden en landen zijn het-woorden → zijn."),
    W("In <i>Is er iets dat ik voor je kan doen?</i> is het verwijswoord goed.", False,
      "Na iets (en niets, alles, veel) gebruik je wat: is er iets wat ik voor je kan doen?"),
    mc("Je schrijft over je buren. Welke van deze zinnen moet je nog verbeteren?",
       "Ik heb hen een kaartje gestuurd.",
       ["Ik heb een kaartje aan hen gestuurd.", "Ik heb hun een kaartje gestuurd.", "Zij hebben een kaartje van mij gekregen."],
       "Meewerkend voorwerp zonder voorzetsel → hun: ik heb hun een kaartje gestuurd. Na 'aan' → hen."),
    O("Maak de zin af: <i>In 'De trainer gaf hen een compliment' moet hen 'hun' zijn, want …</i>",
      ["meewerkend/geen voorzetsel/zonder voorzetsel"],
      "… want het is een meewerkend voorwerp zonder voorzetsel (aan wie gaf de trainer een compliment?).",
      "Meewerkend voorwerp zonder voorzetsel → hun. Na een voorzetsel → hen."),
    mc("<i>Zowel rode als groene paprika's liggen in de schaal.</i> Welk woord staat er maar één keer, en waar?",
       "'paprika's' – achteraan → achterwaarts",
       ["'paprika's' – achteraan → voorwaarts", "'rode' – vooraan → voorwaarts", "'groene' – achteraan → achterwaarts"],
       "Zowel rode [paprika's] als groene paprika's: het woord staat achteraan → achterwaarts."),
    mc("<i>Daan bestelt friet en Lotte een pizza.</i> Wat voor samentrekking is dit?",
       "voorwaartse samentrekking", ["achterwaartse samentrekking", "samentrekking op woordniveau", "geen samentrekking"],
       "<i>Bestelt</i> staat vooraan en valt later weg: … en Lotte [bestelt] een pizza → voorwaarts."),
    W("<i>Voetbalschoenen en -sokken</i> is een achterwaartse samentrekking.", False,
      "Het gemeenschappelijke deel <i>voetbal</i> staat vooraan en valt later weg → voorwaarts."),
    mc("Welke zin over het weekend is goed?",
       "Zaterdag werkt Mila in de winkel en past Joep op zijn zusje.",
       ["Zaterdag werkt Mila in de winkel en Joep past op zijn zusje.", "Zaterdag Mila werkt in de winkel en past Joep op zijn zusje.", "Zaterdag werkt Mila in de winkel en Joep op zijn zusje past."],
       "'Zaterdag' geldt voor beide delen → na de bepaling eerst de persoonsvorm: en [zaterdag] past Joep op zijn zusje."),
    W("<i>In de zomer zwemmen wij in zee en fietsen jullie langs de kust.</i> is goed na de samentrekking.", True,
      "Na de bepaling 'in de zomer' komt in beide delen eerst de persoonsvorm: zwemmen wij … fietsen jullie."),
    mc("In welke woordgroep is het streepje <b>goed</b>?",
       "hoofd- en bijzaken", ["lange- en korte broeken", "dikke- en dunne boeken", "zware- en lichte tassen"],
       "Bij hoofd[zaken] en bijzaken valt een deel van een woord weg → streepje. In de andere drie valt een heel woord weg → geen streepje."),
    I("Vul in met of zonder n: <i>De twee zussen? ____ (beide) zitten op dansles.</i>", "beiden",
      "Zelfstandig gebruikt voor personen (de zussen) → met n: Beiden zitten op dansles."),
    mc("Welk verkleinwoord of meervoud moet je verbeteren?",
       "display'tje", ["hobby'tje", "baby's", "jockeytje"],
       "In display hoort de y bij de klank 'ee' → geen apostrof: displaytje. Hobby en baby: y klinkt als ie → hobby'tje, baby's."),
]))

if __name__ == "__main__":
    gp.genereer(TOETSEN, EERSTE, KOP, "Toets {nr} — Foutentraining {letter}: jouw fouten uit de laatste toetsen",
                paragraaf="mix", icoon="🎯")
