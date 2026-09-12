import json
import os

# Function to validate exam requirements
def validate_exam(exam_data, filename):
    vragen = exam_data["vragen"]
    assert len(vragen) == 20, f"{filename}: moet exact 20 vragen hebben, heeft {len(vragen)}"
    
    mc_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    ww_counts = {True: 0, False: 0}
    type_counts = {}
    
    for idx, v in enumerate(vragen):
        t = v["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
        assert "vraag" in v and v["vraag"], f"{filename} vraag {idx+1}: geen vraag tekst"
        assert not v["vraag"].strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")), f"{filename} vraag {idx+1}: vraag start met nummer"
        assert "uitleg" in v and len(v["uitleg"]) > 10, f"{filename} vraag {idx+1}: uitleg te kort of leeg"
        
        if t == "mc":
            assert len(v["opties"]) == 4, f"{filename} vraag {idx+1}: mc moet 4 opties hebben"
            ans = v["antwoord"]
            assert ans in [0, 1, 2, 3], f"{filename} vraag {idx+1}: ongeldig mc antwoord {ans}"
            mc_counts[ans] += 1
        elif t == "waaronwaar":
            ans = v["antwoord"]
            assert isinstance(ans, bool), f"{filename} vraag {idx+1}: waaronwaar moet boolean zijn"
            ww_counts[ans] += 1
        elif t == "invul":
            assert "antwoord" in v and len(str(v["antwoord"])) > 0, f"{filename} vraag {idx+1}: invul antwoord ontbreekt"
        elif t == "open":
            assert "sleutelwoorden" in v and len(v["sleutelwoorden"]) >= 1, f"{filename} vraag {idx+1}: open mist sleutelwoorden"
            assert "minTreffers" in v and v["minTreffers"] <= len(v["sleutelwoorden"]), f"{filename} vraag {idx+1}: minTreffers > sleutelwoorden"
            assert "modelantwoord" in v and len(v["modelantwoord"]) > 10, f"{filename} vraag {idx+1}: modelantwoord te kort"
            for sw in v["sleutelwoorden"]:
                for alt in sw.split("/"):
                    alt_clean = alt.strip().lower()
                    assert alt_clean not in v["vraag"].lower(), f"{filename} vraag {idx+1}: sleutelwoord '{alt}' komt voor in de vraag!"
        else:
            raise ValueError(f"{filename}: ongeldig type {t}")
            
    assert type_counts.get("mc", 0) == 12, f"{filename}: moet 12 mc hebben, heeft {type_counts.get('mc')}"
    assert type_counts.get("waaronwaar", 0) == 4, f"{filename}: moet 4 waaronwaar hebben, heeft {type_counts.get('waaronwaar')}"
    assert type_counts.get("invul", 0) == 2, f"{filename}: moet 2 invul hebben, heeft {type_counts.get('invul')}"
    assert type_counts.get("open", 0) == 2, f"{filename}: moet 2 open hebben, heeft {type_counts.get('open')}"
    
    # Check MC balance (each position max 40% -> max 4 out of 12; here exactly 3 each = 25%)
    for opt, cnt in mc_counts.items():
        assert cnt <= 4, f"{filename}: mc antwoord {opt} komt {cnt} keer voor (> 4)"
    
    # Check waaronwaar (at least 35% onwaar -> at least 2 False out of 4)
    assert ww_counts[False] >= 2, f"{filename}: waaronwaar onwaar te weinig ({ww_counts[False]}/4)"
    print(f"✓ {filename} is 100% geldig en gebalanceerd (12 mc: {mc_counts}, 4 wow: {ww_counts}, 2 invul, 2 open)")

print("Helper script klaar.")
