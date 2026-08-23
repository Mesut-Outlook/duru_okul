import os, json

base_dir = '/Users/mesutozdemir/_PROJELER/duru_okul/havo3/geschiedenis/js/data'
os.makedirs(base_dir, exist_ok=True)

# Helper function to generate Javascript file for practice quiz
def make_quiz_js(file_name, data):
    content = f"""/* =========================================================
   Duru's Geschiedenis (HAVO 3) — {data['titel']}
   Hoofdstuk {data['hoofdstuk']}: Paragraaf {data['paragraaf']}
   ========================================================= */
(function () {{
  "use strict";

  DURU.register({{
    id: "{data['id']}",
    hoofdstuk: {data['hoofdstuk']},
    paragraaf: "{data['paragraaf']}",
    titel: "{data['titel']}",
    korteUitleg: "{data['korteUitleg']}",
    icoon: "{data['icoon']}",
    kleur: "{data['kleur']}",
    theorie: `{data['theorie']}`,
    vragen: {json.dumps(data['vragen'], ensure_ascii=False, indent=6)}
  }});
}})();
"""
    with open(os.path.join(base_dir, file_name), 'w', encoding='utf-8') as f:
        f.write(content)

# Helper function to generate Javascript file for 20-question proeftoets
def make_exam_js(file_name, data):
    content = f"""/* =========================================================
   Duru's Geschiedenis (HAVO 3) — {data['titel']}
   ========================================================= */
(function () {{
  "use strict";

  DURU.registerExamen({{
    id: "{data['id']}",
    titel: "{data['titel']}",
    vak: "Geschiedenis · Hoofdstuk {data['hoofdstuk']}",
    hoofdstuk: {data['hoofdstuk']},
    hoofdstukTitel: "{data['hoofdstukTitel']}",
    icoon: "{data['icoon']}",
    duurMin: 20,
    vragen: {json.dumps(data['vragen'], ensure_ascii=False, indent=6)}
  }});
}})();
"""
    with open(os.path.join(base_dir, file_name), 'w', encoding='utf-8') as f:
        f.write(content)

print("Generator functions ready!")
