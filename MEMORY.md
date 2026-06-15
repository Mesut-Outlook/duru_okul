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

---

## 🛠️ Storage & Data Structures

* **Subject Practice Progress Keys**:
  - NASK: `duru_nask_v1`
  - Wiskunde: `duru_wiskunde_v1`
  - Economie: `duru_economi_v1`
  - Spelling: `duru_nederlands_spelling_v1`
  - *Data Format*: `{ xp: Number, streak: Number, badges: Object }` (badges object keys are badge IDs).

* **Subject Exam Attempts Keys**:
  - NASK: `duru_nask_examens_v1`
  - Wiskunde: `duru_wiskunde_examens_v1`
  - Economie: `duru_economi_examens_v1`
  - Spelling: `duru_nederlands_spelling_examens_v1`
  - *Data Format*: `{ history: [ { examTitel: String, datum: String, goed: Number, totaal: Number, pct: Number } ] }`
  
* **Reading Comprehension Key**:
  - Key: `begrijpend_lezen_history`
  - *Data Format*: Flat array of attempts: `[ { timestamp: ISOString, score: Number, total: Number, grade: String, startingText: String } ]`
