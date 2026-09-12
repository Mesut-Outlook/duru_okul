# -*- coding: utf-8 -*-
import json
import os
import re

OUTPUT_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/natuurkunde/js/data"

def check_and_save(exam_id, exam_num, title, icon, questions):
    assert len(questions) == 20, f"{exam_id} has {len(questions)} questions, expected 20"
    
    mc = [q for q in questions if q["type"] == "mc"]
    wow = [q for q in questions if q["type"] == "waaronwaar"]
    invul = [q for q in questions if q["type"] == "invul"]
    open_q = [q for q in questions if q["type"] == "open"]
    
    assert len(mc) == 12, f"{exam_id} has {len(mc)} mc, expected 12"
    assert len(wow) == 4, f"{exam_id} has {len(wow)} waaronwaar, expected 4"
    assert len(invul) == 2, f"{exam_id} has {len(invul)} invul, expected 2"
    assert len(open_q) == 2, f"{exam_id} has {len(open_q)} open, expected 2"
    
    mc_dist = {0: 0, 1: 0, 2: 0, 3: 0}
    for q in mc:
        mc_dist[q["antwoord"]] += 1
    for k, v in mc_dist.items():
        assert v == 3, f"{exam_id} MC option {k} has count {v}, expected 3"
        
    wow_false = sum(1 for q in wow if q["antwoord"] is False)
    assert wow_false >= 2, f"{exam_id} has only {wow_false} false waaronwaar, expected >= 2"
    
    for q in open_q:
        assert q["minTreffers"] <= len(q["sleutelwoorden"]), f"minTreffers > len in {q['vraag']}"
        for kw in q["sleutelwoorden"]:
            for alt in kw.split("/"):
                alt_clean = alt.strip().lower()
                # word boundary check or clean substring
                # Ensure word isn't leaked in question
                pattern = r'\b' + re.escape(alt_clean) + r'\b'
                assert not re.search(pattern, q["vraag"].lower()), f"Keyword '{alt_clean}' found as whole word in: {q['vraag']}"

    for i, q in enumerate(questions):
        assert not re.match(r'^\s*\d+\.\s', q["vraag"]), f"Question {i+1} has number prefix: {q['vraag']}"
        assert len(q.get("uitleg", "").strip()) >= 15, f"Question {i+1} uitleg too short: {q.get('uitleg')}"
        if q["type"] == "mc":
            assert len(q["opties"]) == 4, f"Question {i+1} does not have 4 options"
            s = [re.sub(r'<[^>]+>', '', opt).lower().strip() for opt in q["opties"]]
            assert len(set(s)) == len(s), f"Question {i+1} has duplicate options: {q['opties']}"

    content = f"""/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets {exam_num} — {title}
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({{
  "id": "{exam_id}",
  "hoofdstuk": 1,
  "titel": "{title}",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "{icon}",
  "duurMin": 30,
  "vragen": {json.dumps(questions, ensure_ascii=False, indent=4)}
}});
"""
    filepath = os.path.join(OUTPUT_DIR, f"examen_{exam_num}.js")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ Aangemaakt: examen_{exam_num}.js ({title})")
