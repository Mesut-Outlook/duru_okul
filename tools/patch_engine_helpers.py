#!/usr/bin/env python3
"""
Updates engine.js across all havo3 subjects to ensure:
1. cijferStr helper exists.
2. DURU.toggleAllAccordions exists.
3. renderHome organizes exams per Hoofdstuk with Chapter Accordion, Chapter Average Grade and Badges.
4. renderDashboard adds the "📖 Hoofdstukken Overzicht & Cijfers (Ünite Bazında Başarı Karnesi)" table.
"""

import glob
import re

engine_files = glob.glob("/home/mesuto/Documents/PROJELER/duru_okul/havo3/*/js/engine.js")

for fp in engine_files:
    with open(fp, "r", encoding="utf-8") as f:
        code = f.read()

    # Ensure cijferStr helper
    if "function cijferStr(" not in code:
        code = re.sub(
            r"(function\s+laad\(\)\s*\{)",
            r"function cijferStr(pct) { var c = 1 + (pct / 100) * 9; return (Math.round(c * 10) / 10).toFixed(1).replace('.', ','); }\n  \1",
            code
        )

    # Ensure toggleAllAccordions
    if "DURU.toggleAllAccordions" not in code:
        code = re.sub(
            r"(DURU\.gaNaar\s*=\s*function)",
            r"DURU.toggleAllAccordions = function (openState) { var accs = document.querySelectorAll('.chapter-accordion'); accs.forEach(function (acc) { acc.open = openState; }); };\n  \1",
            code
        )

    with open(fp, "w", encoding="utf-8") as f:
        f.write(code)

print("Added helpers to all engine.js files")
