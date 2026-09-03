#!/usr/bin/env python3
"""
Regenerates all onderwerpen and exams with unique question phrasing and validated sleutelwoorden.
"""

import os
import json
import re

# 1. First regenerate all onderwerpen
import gen_duits_all_onderwerpen

# 2. Update exam generators with unique phrasing and valid sleutelwoorden

# H1 Updates:
with open("tools/gen_duits_h1_exams.py", "r", encoding="utf-8") as f:
    h1_code = f.read()

h1_code = h1_code.replace(
    'Wat is de hoofdstad van Duitsland?',
    'Welke stad is de bondshoofdstad en regeringszetel van Duitsland?'
).replace(
    'Welke zin is grammaticaal helemaal correct?',
    'Welke zin over het weer en het weekend is grammaticaal helemaal correct?'
)

with open("tools/gen_duits_h1_exams.py", "w", encoding="utf-8") as f:
    f.write(h1_code)

# H2 Updates:
with open("tools/gen_duits_h2_exams.py", "r", encoding="utf-8") as f:
    h2_code = f.read()

h2_code = h2_code.replace(
    'Kies het juiste voornaamwoord (3e naamval): \'Wie geht es ____ (jou) heute?\'',
    'Vul het juiste persoonlijke voornaamwoord in: \'Hallo Thomas, wie geht es ____ (jou) heute?\''
).replace(
    'Welke zin is grammaticaal helemaal correct?',
    'Welke zin over het doktersbezoek is grammaticaal helemaal correct?'
)

with open("tools/gen_duits_h2_exams.py", "w", encoding="utf-8") as f:
    f.write(h2_code)

# H3 Updates:
with open("tools/gen_duits_h3_exams.py", "r", encoding="utf-8") as f:
    h3_code = f.read()

h3_code = h3_code.replace(
    'Wat is de hoofdstad van Oostenrijk (Österreich)?',
    'Welke historische stad aan de Donau is de hoofdstad van Oostenrijk?'
).replace(
    'Waarom gebruik je bij \'mit\' altijd de 3e naamval (bijv. mit dem Zug)?',
    'Waarom zeg je \'mit dem Zug\' en niet \'mit den Zug\' in het Duits?'
).replace(
    'Welke zin is grammaticaal helemaal correct?',
    'Welke zin over de treinreis en overstappen is grammaticaal helemaal correct?'
)

with open("tools/gen_duits_h3_exams.py", "w", encoding="utf-8") as f:
    f.write(h3_code)

# H4 Updates:
with open("tools/gen_duits_h4_exams.py", "r", encoding="utf-8") as f:
    h4_code = f.read()

h4_code = h4_code.replace(
    'Vul het juiste lidwoord in (4e naamval van der Kuchen): \'Er isst ____ Kuchen.\'',
    'Vul het juiste lidwoord van de 4e naamval in voor der Kuchen: \'Lukas isst ____ leckeren Kuchen.\''
).replace(
    'Wat betekent de term \'Eintritt frei\' op een festivalposter?',
    'Wat houdt de mededeling \'Eintritt frei\' in bij een openluchtconcert?'
).replace(
    'Wat is het Duitse woord voor \'Kerstmis\'?',
    'Hoe heet het traditionele feest van Kerstmis in het Duits?'
).replace(
    'Wat betekent de Duitse carnavalskreet \'Kölle Alaaf\' en in welke stad hoort deze thuis?',
    'In welke stad klinkt tijdens de optocht de bekende kreet \'Kölle Alaaf\' en wat wordt er gevierd?'
).replace(
    'Welke zin is grammaticaal helemaal correct?',
    'Welke zin over het verjaardagsfeest en uitnodigingen is grammaticaal helemaal correct?'
)

with open("tools/gen_duits_h4_exams.py", "w", encoding="utf-8") as f:
    f.write(h4_code)

# H5 Updates:
with open("tools/gen_duits_h5_exams.py", "r", encoding="utf-8") as f:
    h5_code = f.read()

h5_code = h5_code.replace(
    'Wat is het hoogste schoolcijfer in Duitsland?',
    'Welk cijfer staat in het Duitse rapport- en beoordelingssysteem voor \'sehr gut\'?'
).replace(
    'Wat is het Duitse woord voor \'de toekomst\'?',
    'Hoe vertaal je het begrip \'de toekomst\' naar het Duits?'
).replace(
    'Wat is het verschil in het Duits tussen \'studieren\' en \'lernen\'?',
    'Waarvoor gebruik je het werkwoord \'studieren\' in tegenstelling tot \'lernen\'?'
).replace(
    '"sleutelwoorden": ["universiteit/hogeschool", "schoolwerk/huiswerk", "studie"],',
    '"sleutelwoorden": ["universiteit/hogeschool", "schoolwerk/huiswerk", "hoger onderwijs"],'
).replace(
    'Welke zin is grammaticaal helemaal correct?',
    'Welke zin met sterke werkwoorden (lezen en talen spreken) is grammaticaal helemaal correct?'
)

with open("tools/gen_duits_h5_exams.py", "w", encoding="utf-8") as f:
    f.write(h5_code)

# H6 Updates:
with open("tools/gen_duits_h6_exams.py", "r", encoding="utf-8") as f:
    h6_code = f.read()

h6_code = h6_code.replace(
    'Wat is het alarmnummer voor de politie in Duitsland?',
    'Welk alarmnummer toets je in Duitsland in als je dringend de politie nodig hebt?'
).replace(
    'Wat is het Duitse woord voor \'de brandweer\'?',
    'Hoe noem je de hulpdienst die branden blust in het Duits?'
).replace(
    'Het Duitse woord \'der Unfall\' betekent \'de overwinning\'.',
    'De Duitse term \'der Unfall\' betekent \'de sportieve overwinning\'.'
).replace(
    'Hoe worden de letters \'p\', \'t\' en \'k\' in het Duits uitgesproken?',
    'Op welke manier spreek je de Duitse plofklanken \'p\', \'t\' en \'k\' uit?'
).replace(
    'Vertaal het woord: \'(De brandweer)\'',
    'Vertaal de naam van de blusdienst: \'(De brandweer)\''
).replace(
    'Wat is het hoogste schoolcijfer in Duitsland?',
    'Welk cijfer is in Duitsland het allerbeste toetscijfer?'
).replace(
    'Wat betekent het woord \'die Verspätung\'?',
    'Wat betekent de treinterm \'die Verspätung\' op een Duits vertrekbord?'
).replace(
    'Wat is de hoofdstad van Duitsland?',
    'Wat is de naam van de Duitse hoofdstad?'
)

with open("tools/gen_duits_h6_exams.py", "w", encoding="utf-8") as f:
    f.write(h6_code)

print("All generator scripts patched. Running generators...")

import subprocess
import sys

subprocess.run([sys.executable, "tools/gen_duits_all_onderwerpen.py"], check=True)
subprocess.run([sys.executable, "tools/gen_duits_h1_exams.py"], check=True)
subprocess.run([sys.executable, "tools/gen_duits_h2_exams.py"], check=True)
subprocess.run([sys.executable, "tools/gen_duits_h3_exams.py"], check=True)
subprocess.run([sys.executable, "tools/gen_duits_h4_exams.py"], check=True)
subprocess.run([sys.executable, "tools/gen_duits_h5_exams.py"], check=True)
subprocess.run([sys.executable, "tools/gen_duits_h6_exams.py"], check=True)

print("All files regenerated!")
