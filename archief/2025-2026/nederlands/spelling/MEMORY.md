# MEMORY.md - Spelling & Grammatica Module History & Decisions

This document serves as the project's memory log for the **Spelling & Grammatica** module under `nederlands/spelling/`, preserving design choices, features, and key configurations.

---

## 📅 Project Evolution & Milestones

### Milestone 1: Module Creation & Initial Setup
* **Structure**: Created a self-contained DURU-engine module inside `nederlands/spelling/` with its own `index.html`, `css/style.css`, `js/bootstrap.js`, `js/engine.js`, and `js/exams.js`.
* **Storage Keys**:
  - Regular Quizzes: `duru_nederlands_spelling_v1`
  - Exam History: `duru_nederlands_spelling_examens_v1`
* **Data Modules**:
  - Created 5 practice alıştırmalar (quizzes):
    1. `sp_1_tegenwoordige_tijd.js` (tt)
    2. `sp_2_verleden_tijd.js` (vt)
    3. `sp_3_voltooid_deelwoord.js` (vd)
    4. `sp_4_voegwoorden_interpunctie.js` (conjunctions & punctuation)
    5. `sp_5_zinsdelen_ontleden.js` (cument parsing)
  - Created 2 initial exams:
    1. `examen_1_werkwoordspelling.js` (verb spelling)
    2. `examen_2_gemengd_ontleden.js` (grammar and spelling)

### Milestone 2: UI Integration & Storage Bugfix
* **Dashboard Link**: Linked spelling into the main dashboard dropdown under 'Nederlands' via `js/landing.js`.
* **Storage Interceptor Fix**: Overrode `win.Storage.prototype.setItem` inside `js/landing.js` instead of overriding `win.localStorage.setItem` directly. This prevents `Illegal invocation` errors in Safari/Chrome which was previously causing the app to crash and hide the exam result screen.
* **SVG Gradient Fix**: Rather than referencing ID gradients (which fail to render in Safari inside iframes), we styled the circular progress rings inside `engine.js` and `exams.js` to use a solid color `stroke="var(--paars)"`.

### Milestone 3: Expansion to 12 Exams
* **User Requirement**: Create 10 more exams to expand the database.
* **Implementation**: Added 10 new exam files (`ex-sp-3` through `ex-sp-12`) under `js/data/`:
  - `examen_3_voegwoorden_interpunctie.js` (Proeftoets 3)
  - `examen_4_zinsdelen_ontleden.js` (Proeftoets 4)
  - `examen_5_hoofdletters_leestekens.js` (Proeftoets 5)
  - `examen_6_woordbenoemen.js` (Proeftoets 6)
  - `examen_7_tegenwoordige_tijd.js` (Proeftoets 7)
  - `examen_8_verleden_tijd.js` (Proeftoets 8)
  - `examen_9_voltooid_deelwoord.js` (Proeftoets 9)
  - `examen_10_sterke_zwakke_ww.js` (Proeftoets 10)
  - `examen_11_gemengde_spelling.js` (Proeftoets 11)
  - `examen_12_eindtoets.js` (Proeftoets 12 - Grote Eindtoets)
* Linked all 10 new exams in `nederlands/spelling/index.html`.

---

## 🛠️ Key Technical Details

### Local Server Log Format
The Python custom server (`server.py`) automatically captures scores starting with `duru_` and logs them into `scores.json` and `scores_log.txt`.
* **Example Log Entry**:
  `[2026-06-15 19:25:36] IP: 192.168.68.120 | Key: duru_nederlands_spelling_examens_v1`
  `  📝 EXAM DONE: Proeftoets 1 — Werkwoordspelling (tt, vt, vd) | Score: 87% (13/15 correct)`
