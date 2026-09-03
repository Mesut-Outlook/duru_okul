#!/usr/bin/env python3
"""
Ensures all havo3/*/js/exams.js save hoofdstuk and hoofdstukTitel in historyEntry.
"""

import os
import glob
import re

exam_files = glob.glob("/home/mesuto/Documents/PROJELER/duru_okul/havo3/*/js/exams.js")

for fp in exam_files:
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for historyEntry object definition
    pattern = r"(var\s+historyEntry\s*=\s*\{[^}]*examTitel:\s*ex\.titel,)([^}]*\};)"
    
    def repl(m):
        prefix = m.group(1)
        suffix = m.group(2)
        if "hoofdstuk:" in suffix:
            return m.group(0)
        insert = "\n      hoofdstuk: ex.hoofdstuk || 1,\n      hoofdstukTitel: ex.hoofdstukTitel || ('Hoofdstuk ' + (ex.hoofdstuk || 1)),"
        return prefix + insert + suffix

    new_content, count = re.subn(pattern, repl, content)
    if count > 0 and new_content != content:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {fp}")
    else:
        print(f"Already up to date or no match: {fp}")
