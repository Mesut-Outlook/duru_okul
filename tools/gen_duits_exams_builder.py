#!/usr/bin/env python3
"""
Generates all 30 Proeftoetsen (20 questions each = 600 questions) for HAVO 3 Duits (Neue Kontakte 3 HAVO)
- Hoofdstuk 1: Umgebung & Wetter (Examen 1 - 5)
- Hoofdstuk 2: Gesundheit & Körper (Examen 6 - 10)
- Hoofdstuk 3: Unterwegs & Reisen (Examen 11 - 15)
- Hoofdstuk 4: Veranstaltungen & Termine (Examen 16 - 20)
- Hoofdstuk 5: Zukunft & Berufe (Examen 21 - 25)
- Hoofdstuk 6: In Aktion & Hilfsbereitschaft (Examen 26 - 30)
"""

import os
import json
import sys

BASE_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/duits"
DATA_DIR = os.path.join(BASE_DIR, "js/data")
os.makedirs(DATA_DIR, exist_ok=True)

def balance_mc(questions):
    mc_indices = [i for i, q in enumerate(questions) if q.get("type") == "mc"]
    target_pattern = [0, 1, 2, 3] * (len(mc_indices) // 4 + 2)
    for idx, q_idx in enumerate(mc_indices):
        q = questions[q_idx]
        current_ans_idx = q["antwoord"]
        correct_text = q["opties"][current_ans_idx]
        new_ans_idx = target_pattern[idx] % len(q["opties"])
        if new_ans_idx != current_ans_idx:
            opts = [opt for i, opt in enumerate(q["opties"]) if i != current_ans_idx]
            opts.insert(new_ans_idx, correct_text)
            q["opties"] = opts
            q["antwoord"] = new_ans_idx

def write_exam(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    content = f"""/* Proeftoets {data['id']} — {data['titel']}
   Neue Kontakte 3 HAVO Hoofdstuk {data['hoofdstuk']} */
DURU.registerExamen({json.dumps(data, indent=2, ensure_ascii=False)});
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [✓] Exam saved: {filename}")

# First run H1 generator
import subprocess
subprocess.run([sys.executable, "/home/mesuto/Documents/PROJELER/duru_okul/tools/gen_duits_h1_exams.py"], check=True)

print("H1 complete, building H2-H6...")
