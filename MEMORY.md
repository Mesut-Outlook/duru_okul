# MEMORY.md - Global Project History & Memory Log

This document serves as the project's global memory log, preserving all overall design choices, architectural changes, milestones, and integration histories.

---

## 📅 Project Evolution & Milestones

### Milestone 1: Merging Subprojects (2026-06-03)
* **Goal**: Consolidate Duru's separate school module sites under a single repository/origin to easily run and sync progress.
* **Result**: natural sciences (NASK), math (Wiskunde), economy (Economie), and Dutch (begrijpend-lezen and spelling) were embedded as subfolders in this repository.

### Milestone 2: Custom Local Network Server (server.py)
* **Goal**: Allow access to the school hub from other devices in the local network (LAN) such as tablets or phones.
* **Result**: Implemented `server.py`, a custom HTTP server listening on Port 8125. Automatically logs attempts and syncs local storage.

### Milestone 3: Storage Interception & Safari Compatibility
* **Goal**: Intercept exam/practice scores saved inside child iframes and sync them to the server `/api/score` endpoint.
* **Result**: In `js/landing.js`, overrode `Storage.prototype.setItem` securely with a try-catch block to prevent illegal invocation errors in Safari and Chrome.

### Milestone 4: Database Expansion (Spelling & Reading comprehension)
* **Result**:
  - spelling was expanded to include exactly 12 full exams.
  - begrijpend-lezen was expanded to include 10 standardized exams (with a Meester Max AI enabler).

### Milestone 5: Stats Dashboard Integration (2026-06-15)
* **Goal**: Create a comprehensive dashboard showing all exams, attempts, success rates, and performance charts on the home page.
* **Implementation Details**:
  1. **UI Views**: Replaced the landing page header with a Tab Selector toggling between **Mijn vakken** (default) and **Mijn prestaties & statistieken**.
  2. **Aggregated Counters**: Total XP (accumulated across all subjects), Total Badges, Completed Exams, and overall average Dutch Grade (scale 1.0 to 10.0).
  3. **SVG Line Chart**: Draws a responsive, chronological timeline plot of the last 15 proeftoetsen/exams. Includes gridlines, a custom green dashed pass line (5.5), and hover tooltips for all datadots.
  4. **Subject Analytics Card Grid**: Computes individual course statistics: number of tests, average grade, max grade, and displays interactive themed progress bars.
  5. **Logs & Attempts Table**: Detailed list of all attempts. Features instant client-side keyword search (by subject or test title) and filter buttons.

### Milestone 6: Proeftoets Card Enhancements (2026-06-16)
* **Goal**: Show completion status (done/not done) and the latest score on each proeftoets card across all subjects (NASK, Wiskunde, Economie, Spelling & Grammatica, Begrijpend Lezen).
* **Implementation Details**:
  - Render a status badge (`✓ Gemaakt` or `Nog niet gemaakt`) on each card inside the subject exam lists.
  - Display both `🏆 Beste cijfer` and `⏱️ Laatste cijfer` on each card.
  - Fallback logic checks raw log history if `EX.laatste` is missing for old stored objects.
  - Begrijpend Lezen checks `begrijpend_lezen_history` to show best and latest grades dynamically with contrast styles on selected cards.
  - Updated the subject-specific dashboards (NASK, Wiskunde, Economie, Spelling) to display all registered exams (both completed and uncompleted ones) sorted in numerical order.
  - Updated the main landing dashboard's subject details tables (`js/dashboard.js`) to sort the listed prooftests in numerical order.
  - Implemented automatic progress restoration by creating a `GET /api/score` endpoint in `server.py` and a fetch loader in `js/landing.js` that pulls synced scores on load and populates `localStorage`.

### Milestone 7: Spelling and Economy Expansions, Server Synchronization, and Geschiedenis Module (2026-06-20)
* **Goal**: Expand content libraries for Spelling and Economy, ensure robust local server synchronization, and introduce a brand new course module for History.
* **Implementation Details**:
  - **Spelling Module Expansion**: Added 5 new prooftests (ex-sp-33 to ex-sp-37) with 15 questions each.
  - **Recovery Engine**: Standardized recovery logic (`laadEx`) in all subject engines to correctly fall back and restore missing `beste` and `laatste` scores from history.
  - **Server Synchronization & Recovery**: Implemented a `GET /api/score` endpoint on `server.py` to retrieve all scores. Expanded `js/landing.js` to automatically fetch and merge historical scores on page load, ensuring complete progress restoration across different sessions/devices.
  - **Economy Module Content Redesign**: Added 15 new extra exams (ex-21 to ex-35). Replaced 11 existing extra exams containing out-of-scope chapters with questions strictly targeting Sections 6.1-6.4 (De overheid), maintaining a clean, localized curriculum scope.
  - **Geschiedenis Module Integration**: Created and embedded a completely new "Geschiedenis" (History) subject focusing on WO I & II. Configured its 4 core study subchapters, 30 practice exams, and integrated it into the landing page dashboard and stats views.

### Milestone 8: Geschiedenis Vocabulary Exam Expansion (2026-06-21)
* **Goal**: Expand the History module with 15 new vocabulary-focused exams (ex-41 to ex-55) to enhance definition learning and word retention.
* **Implementation Details**:
  - **Exams Created**: Added exactly 15 new exams (`examen_41.js` to `examen_55.js`) with 15 questions each.
  - **Question Types**: Excluded the True/False ('waaronwaar') type. All questions consist purely of Multiple Choice ('mc') and Fill-in-the-blank ('invul') question types (8 mc, 7 invul each) to test definitions.
  - **Integration**: Loaded all 15 scripts in the Geschiedenis `index.html` file and updated CLAUDE.md.

### Milestone 9: History Exam Expansion for Definitions and Important Figures (2026-06-21)
* **Goal**: Create 10 new exams (ex-56 to ex-65) with 15 questions each targeting definitions, expressions, key terms, and important historical figures of Chapter 4.
* **Implementation Details**:
  - **Exams Created**: Created `examen_56.js` through `examen_65.js` with 15 questions each.
  - **Topics Covered**: Systematically covers W-B-M-N, Franz Ferdinand, Sarajevo, loopgraven, Weimarrepubliek, hyperinflatie, Beurskrach, stempelen, dictators (Hitler, Stalin, Mussolini, Colijn), appeasement, Blitzkrieg, keerpunten (Stalingrad, Pearl Harbor), Holocaust (Rassenwetten, Kristallnacht, Wannsee, kampen), bezet Nederland (Seyss-Inquart, NSB, Mussert, Arbeitseinsatz, Februaristaking), Hongerwinter, Jappenkampen, and the atomic bombs.
  - **Question Types**: Balanced mix of Multiple Choice ('mc'), True/False ('waaronwaar'), and Fill-in-the-blank ('invul') types.
  - **Integration**: Loaded all 10 scripts in the Geschiedenis `index.html` file and updated CLAUDE.md.

### Milestone 10: GitHub Pages Support and Auto-Deployment (2026-06-22)
* **Goal**: Support running the application on GitHub Pages dynamically, configure automatic deploy on git pushes, and upload to remote repository.
* **Implementation Details**:
  - **Environment Detection**: Updated `js/landing.js` to detect if the app is hosted on `github.io` (`isGitHubPages`).
  - **Graceful Degrade**: Bypassed local network API calls (`/api/score` POST and GET) when running on GitHub Pages to prevent useless 404 network warnings, while preserving full client-side local storage features.
  - **Deploy Configuration**: Added a `.nojekyll` file at the root to prevent Jekyll processing of folders. Created `.github/workflows/deploy.yml` to automatically build and deploy the project to GitHub Pages via GitHub Actions on every push to the `main` branch.

### Milestone 11: Inkomstenbelasting & Loonbelasting Exam Expansion (2026-06-22)
* **Goal**: Expand the Economy module with 5 new exam files focusing on "Inkomstenbelasting & Loonbelasting" to strengthen understanding of direct taxes, gross/net salary calculations, loonheffingskorting rules, and progressive tax brackets.
* **Implementation Details**:
  - **Exams Created**: Added `examen_36_extra_inkomsten_loonbelasting_2.js` through `examen_40_extra_inkomsten_loonbelasting_6.js` (Extra Proeftoets 31 to 35) with exactly 15 questions each.
  - **Topics Covered**: Gross/net salaries, roles of employee/employer/Belastingdienst, loonheffingskorting rules for multiple jobs, tax bracket (schijventarief) math, DigiD, draagkrachtbeginsel, solidarity, and tax refunds vs additional payments.
  - **Integration**: Loaded all 5 scripts in the `economi/index.html` file.

### Milestone 12: Consument & Sociale Zekerheid Exam Expansions (2026-06-22)
* **Goal**: Add 4 new extra practice exams for the Economie module to cover "Consument & Overheid" and "Sociale Zekerheid & Zorg".
* **Implementation Details**:
  - **Exams Created**: Created `examen_41_extra_consument_overheid_2.js` through `examen_44_extra_sociale_zekerheid_4.js` (Extra Proeftoets 4B, 4C, 5B, and 5C) containing 10 questions each with answers, model open answers, and detailed explanations.
  - **Topics Covered**: Consumentenbescherming, Wet koop op afstand (bedenktijd), Autoriteit Consument & Markt (ACM), mededinging, warranties, UWV/SVB functions, omslagstelsel vs kapitaaldekkingstelsel, eigen risico logic, and Participatiewet/Bijstand criteria.
  - **Integration**: Loaded all 4 scripts in the `economi/index.html` file.

### Milestone 13: Client-side User Authentication & Backup Encryption (2026-06-22)
* **Goal**: Protect student progress privacy when hosted publicly on GitHub, and allow separate progress accounts on the same browser.
* **Implementation Details**:
  - **Symmetric Encryption**: Encrypted the main progress backup file (`scores_backup.json`) using a custom symmetric XOR cipher with a key derived from Duru's password (`12341234`), rendering the repository backup unreadable to public viewers.
  - **Active User Storage Prefixes**: Intercepted the browser's `Storage.prototype` (`getItem`, `setItem`, `removeItem`) for both the main window and same-origin subfolders within the `iframe`. If a user is logged in, all application progress keys (beginning with `duru_` or `begrijpend_lezen_`) are transparently prefixed with `user_<username>_`.
  - **Authentication Screen**: Designed a responsive login/register overlay in `index.html` styled with the dark theme. Added support for password hashing (`simpleHash`), "Remember Me" sessions, and a new user registration workflow.
  - **Duru Decryption Restore**: Logging in as `"duru"` with `"12341234"` triggers a one-time fetch and decryption of `scores_backup.json`, restoring her historical grades into her specific account prefix `user_duru_`.
  - **Log Out UI**: Added a user status badge and a logout button in the header topbar.

### Milestone 14: Economics Out-of-Scope Question Cleanup (2026-06-22)
* **Goal**: Audit and align all 44 economics exams to ensure no questions test topics outside of the official Chapter 6 theory (Sections 6.1-6.4).
* **Implementation Details**:
  - **Auditing**: Wrote a scanning script to detect out-of-scope keywords (ACM, cartels, consumer rights/protection, price elasticity, marktvormen, trade barriers). Identified 19 violating questions across 6 exam files.
  - **Rewriting Exams**: Entirely rewrote `examen_9_extra_consument.js`, `examen_41_extra_consument_overheid_2.js`, and `examen_42_extra_consument_overheid_3.js` to target in-scope topics: "Collectieve Voorzieningen", "De Overheid als Bestuurder (Rijksoverheid)", and "Provincie & Lokale Besturen".
  - **Replacing Questions**: Replaced individual out-of-scope questions in `examen_20_extra_mix_2.js` (Q4 and Q10), `examen_25_extra_eindtoets_mix_3.js` (Q13), and `examen_35_extra_eindtoets_mix_4.js` (Q6 and Q12) with in-scope concepts (private sector, public debt, municipal structures, non-tax revenues).
  - **Validation**: Verified all modified files have valid JavaScript syntax and confirm 0 violations remain.

### Milestone 15: Economics Exam Additions for Duru's Notes (2026-06-23)
* **Goal**: Add two new 15-question exams (Extra Proeftoets 38 & 39) targeting important Chapter 6 topics/notes specified by Duru.
* **Implementation Details**:
  - **Exams Created**: Added `examen_45_extra_belangrijke_notities_1.js` (Extra Proeftoets 38, Paragraphs 6.1 & 6.2) and `examen_46_extra_belangrijke_notities_2.js` (Extra Proeftoets 39, Paragraphs 6.3 & 6.4) with exactly 15 questions each.
  - **Question Distribution**: 6 mc, 4 waaronwaar, 3 invul, and 2 open questions per exam.

### Milestone 16: Local Storage Data Migration (2026-06-23)
* **Goal**: Ensure Duru's local progress completed before logging in/registering is not lost and is successfully migrated to her prefixed user account profile.
* **Implementation Details**:
  - **Migration Function**: Created `migratePreExistingLocalScores(username)` in `js/landing.js` that scans `localStorage` for any unprefixed keys (e.g. starting with `duru_` or `begrijpend_lezen_`), merges them with any existing prefixed data using the native `restoreScores` logic, and removes the old plain keys.
  - **Login Integration**: Integrated migration during user registration, regular login, and first-time decrypt backup logins (where local data is merged into `parsedScores` before being restored to prefixed keys).

### Milestone 17: Multi-Agent Exam Expansion (2026-06-23)
* **Goal**: Expand Chapter 6 exam database by 17 new high-quality exams (5 general exams, 12 subtopic-specific exams).
* **Implementation Details**:
  - **Coordinated Approach**: Wrote `coordination.md` and spawned 3 parallel `self` subagents to divide the work: General Writer (5 general exams covering all H6), Political Writer (6 subtopic exams covering 6.1 and 6.2), and Financial Writer (6 subtopic exams covering 6.3 and 6.4).
  - **Exams Created**: Added `examen_47` to `examen_51` (general) and `examen_52` to `examen_63` (subtopic).
  - **Schema Conformance**: Verified that all 17 files conform to the 15-question structure (6 mc, 4 waaronwaar, 3 invul, 2 open), use comma decimal notation, and have fully translated Dutch explanations.
  - **Syntax Validation**: Checked all generated files using `node -c` and resolved all syntax issues.

---


## 🛠️ Storage & Data Structures

* **Subject Practice Progress Keys**:
  - NASK: `duru_nask_v1`
  - Wiskunde: `duru_wiskunde_v1`
  - Economie: `duru_economi_v1`
  - Spelling: `duru_nederlands_spelling_v1`
  - Geschiedenis: `duru_geschiedenis_v1`
  - *Data Format*: `{ xp: Number, streak: Number, badges: Object }` (badges object keys are badge IDs).

* **Subject Exam Attempts Keys**:
  - NASK: `duru_nask_examens_v1`
  - Wiskunde: `duru_wiskunde_examens_v1`
  - Economie: `duru_economi_examens_v1`
  - Spelling: `duru_nederlands_spelling_examens_v1`
  - Geschiedenis: `duru_geschiedenis_examens_v1`
  - *Data Format*: `{ history: [ { examTitel: String, datum: String, goed: Number, totaal: Number, pct: Number } ] }`
  
* **Reading Comprehension Key**:
  - Key: `begrijpend_lezen_history`
  - *Data Format*: Flat array of attempts: `[ { timestamp: ISOString, score: Number, total: Number, grade: String, startingText: String } ]`
