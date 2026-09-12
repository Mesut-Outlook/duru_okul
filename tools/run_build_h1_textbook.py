import sys
from make_all_textbook_exams import check_and_save
import data_h1_1
import data_h1_2
import data_h1_3

print("=== START GENERATIE 9 EXAMENS HOOFDSTUK 1 ===")

# §1.1
check_and_save("ex-h3-natuurkunde-26", 26, "Toets 26 — §1.1 Kracht bij beweging — Toets A", "🏎️", data_h1_1.q26)
check_and_save("ex-h3-natuurkunde-27", 27, "Toets 27 — §1.1 Kracht bij beweging — Toets B", "🏎️", data_h1_1.q27)
check_and_save("ex-h3-natuurkunde-28", 28, "Toets 28 — §1.1 Kracht bij beweging — Toets C", "🏎️", data_h1_1.q28)

# §1.2
check_and_save("ex-h3-natuurkunde-29", 29, "Toets 29 — §1.2 Soorten beweging & Diagrammen — Toets A", "📈", data_h1_2.q29)
check_and_save("ex-h3-natuurkunde-30", 30, "Toets 30 — §1.2 Soorten beweging & Diagrammen — Toets B", "📈", data_h1_2.q30)
check_and_save("ex-h3-natuurkunde-31", 31, "Toets 31 — §1.2 Soorten beweging & Diagrammen — Toets C", "📈", data_h1_2.q31)

# §1.3
check_and_save("ex-h3-natuurkunde-32", 32, "Toets 32 — §1.3 Kracht en versnelling — Toets A", "🚀", data_h1_3.q32)
check_and_save("ex-h3-natuurkunde-33", 33, "Toets 33 — §1.3 Kracht en versnelling — Toets B", "🚀", data_h1_3.q33)
check_and_save("ex-h3-natuurkunde-34", 34, "Toets 34 — §1.3 Kracht en versnelling — Toets C", "🚀", data_h1_3.q34)

print("=== ALLE 9 EXAMENS SUCCESVOL GEBOUWD ===")
