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

### Milestone 15: Geschiedenis HAVO 3 — Hoofdstuk 1: De Eerste Wereldoorlog (2026-08-23)
* **Goal**: Build complete theory, practice quizzes (onderwerpen), and full proeftoetsen (exams) for HAVO 3 History Hoofdstuk 1 (De Eerste Wereldoorlog) based on the official Geschiedeniswerkplaats 3 HAVO textbook chapter.
* **Implementation Details**:
  - **Source Material**: Processed 10-page textbook PDF (`Geschiedeniswerkplaats 3 havo - Hoofdstuk 1 De Eerste Wereldoorlog.pdf`) via PyMuPDF + macOS Vision OCR.
  - **Bootstrap Setup**: Updated `havo3/geschiedenis/js/bootstrap.js` with Hoofdstuk 1 metadata (De Eerste Wereldoorlog 1900–1920).
  - **Practice Quizzes (Onderwerpen)**: Created 5 detailed Javascript data modules in `havo3/geschiedenis/js/data/`:
    1. `h1_1_tijd.js`: Paragraaf 1.1 — De moderne beleving van tijd (Greenwich-tijd, spoorwegen, la belle époque, vooruitgangsgeloof, Olympische Spelen 1896, 8 vragen).
    2. `h1_2_grote_oorlog.js`: Paragraaf 1.2 — De Grote Oorlog (Centralen vs Geallieerden, nationalisme/militarisme/wapenwedloop/bondgenootschappen, moord op Frans Ferdinand in Sarajevo 28 juni 1914, Schlieffenplan, loopgraven, Armeense genocide, 11-11-1918 11u, 8 vragen).
    3. `h1_3_rusland.js`: Paragraaf 1.3 — Revolutie in Rusland (Tsarenrijk Nicolaas II, Bloedige Zondag 1905, Februarirevolutie 1917, Lenin, Oktoberrevolutie 1917, bolsjewieken, hamer en sikkel, Rode Leger, Tsjeka, stichting Sovjet-Unie 1922, 8 vragen).
    4. `h1_4_nieuwe_kaart.js`: Paragraaf 1.4 — De nieuwe kaart van Europa (Vrede van Versailles 1919, alleenschuld Duitsland, herstelbetalingen, Volkenbond, zelfbeschikkingsrecht Wilson, nieuwe staten, stichting Republiek Turkije 1923 o.l.v. Atatürk, volkenruil, 8 vragen).
    5. `h1_5_neutraal_nederland.js`: Paragraaf 1.5 — Neutraal Nederland (mobilisatie, 1 miljoen Belgische vluchtelingen, Draad des Doods, schaarste & distributie 'op de bon', Grondwetsherziening 1917: algemeen mannenkiesrecht + vrouwenkiesrecht 1919 + schoolstrijd, vergissing van Troelstra, De Stijl & Mondriaan, 8 vragen).
  - **Proeftoetsen (Exams)**:
    - Updated `examen_1.js`: Proeftoets 1 — De Grote Oorlog & Oorzaken (12 exam vragen).
    - Created `examen_2.js`: Proeftoets 2 — Revolutie, Nieuwe Kaart & Neutraal NL (12 exam vragen).
  - **Integration & Validation**: Updated `havo3/geschiedenis/index.html` loading order. Validated all JavaScript modules using Node.js stub execution (`SUCCESS! Registered onderwerpen: 5 and examens: 2`).

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

### Milestone 18: Five More General Exams (2026-06-23)
* **Goal**: Add 5 more general exams covering the entire Chapter 6 to further build up the exam database.
* **Implementation Details**:
  - **Exams Created**: Added `examen_64_extra_algemeen_6.js` to `examen_68_extra_algemeen_10.js` (Extra Proeftoets 57 - 61) with exactly 15 questions each.
  - **Schema Conformance**: Verified that all 5 files conform to the 15-question structure (6 mc, 4 waaronwaar, 3 invul, 2 open), use comma decimal notation, and have fully translated Dutch explanations.
  - **Syntax Validation**: Checked all files using `node -c` and confirmed no errors.

### Milestone 19: Another Five General Exams (2026-06-23)
* **Goal**: Add 5 more general exams covering the entire Chapter 6 to further build up the exam database.
* **Implementation Details**:
  - **Exams Created**: Added `examen_69_extra_algemeen_11.js` to `examen_73_extra_algemeen_15.js` (Extra Proeftoets 62 - 66) with exactly 15 questions each.
  - **Schema Conformance**: Verified that all 5 files conform to the 15-question structure (6 mc, 4 waaronwaar, 3 invul, 2 open), use comma decimal notation, and have fully translated Dutch explanations.
  - **Syntax Validation**: Checked all files using `node -c` and confirmed no errors.

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

---

## 📅 Milestone 7: MAVO 2 → HAVO 3 geçişi + ortak dokümantasyon yapısı (2026-07-20)
* **Hedef**: Duru HAVO 3'e geçti. MAVO 2 içeriğini arşivleyip, yeni HAVO 3 dönemi için altyapı
  (ortak dokümantasyon + belge→sınav üretim hattı + Opus↔agy koordinasyonu) kurmak.
* **Sonuç**:
  1. **Kanonik `docs/`** oluşturuldu: `ENGINE_SPEC.md` (DURU veri sözleşmesinin tek doğru kaynağı,
     4 SPEC.md'deki tekrarı toplar), `DOC_STANDARD.md` (tüm CLAUDE.md/MEMORY.md için ortak iskelet +
     dil kuralı: dev-dokümanları Türkçe, öğrenci-içeriği Flamanca), `PIPELINE.md` (belge→sınav hattı
     + model/agent politikası).
  2. **Kök `CLAUDE.md`** HAVO 3 dönemine göre yeniden yazıldı: arşiv, `docs/` işaretçileri, model
     politikası (planlama=Opus, üretim=Sonnet/Haiku alt-agent veya agy), ders-ekleme 6 dokunma noktası.
  3. **`coordination.md`** Opus↔agy protokolüne oturtuldu (görev şeması + durum döngüsü). agy'nin
     canlı olduğu doğrulandı (16:15'te yokladı). agy = Google Antigravity SDK; mevcut kullanım
     `nederlands/begrijpend-lezen/generate_exam_agy.py`.
  4. **`inbox/`** açıldı (ders materyali bırakma alanı; PDF/Word/görsel).
* **Kim**: Opus (plan + tüm altyapı dosyaları).
* **TASK-01 tamamlandı (2026-07-20)**: 5 MAVO 2 dersi `git mv` ile `archief/mavo2/`'ye taşındı;
  `js/landing.js` `renderVakken` aktif/arşiv ayrımı + açılır "Archief (MAVO 2)" bölümü + HAVO 3
  placeholder; `css/style.css` tema-güvenli `.archief-*`/`.havo3-placeholder`; `index.html` `?v=2.6`.
  Global localStorage anahtarları değişmedi → eski skorlar/dashboard korunuyor.
* **TASK-02 tamamlandı (2026-07-20)**: HAVO 3 landing yeniden tasarlandı — sıcak-arkadaşça tarz,
  alan-gruplu düzen (Talen / Exact & Natuur / Mens & Maatschappij). `js/landing.js`'e `domein` alanı
  + 12 tipik HAVO 3 dersi (`binnenkort:true`); `renderVakken` alanlara göre gruplar, `maakVakKaartHavo3`
  sıcak kartlar basar, `leesVakData` ilerlemeyi `duru_h3_<vak>_v1`'den okur; `css/style.css` scoped
  `.havo3-*` (tema-güvenli); `index.html` `?v=2.7` + yeni hero. Dersler tipik pakket (Duru'nun gerçek
  listesi gelince güncellenecek).
* **Sıradaki**: (1) Duru'nun gerçek HAVO 3 pakketini `VAKKEN`'e işle. (2) İlk ders içeriği gelince
  `havo3/<vak>/` sitesini `duru_h3_<vak>_v1` slug'ıyla kur, kartı `binnenkort:false` + `href` yap,
  `sleutel:'duru_h3_<vak>'` ekle (kart ilerleme/cijfer gösterir). (3) Dashboard/statistieken view'ını
  da HAVO 3 sıcak temaya uyarlamak (henüz yapılmadı; ayrı iş).

### Milestone 8: Ders yılı bazlı arşivleme (2026-07-20)
* **Hedef**: Arşivi seviye ("mavo2") yerine **ders yılına** göre düzenlemek (2025-2026, 2026-2027…).
* **Sonuç**: `git mv archief/mavo2 → archief/2025-2026`. `js/landing.js` href'leri güncellendi;
  arşiv entry'lerine `jaar` alanı; `renderArchief` **yıla göre gruplar** (`JAAR_NIVEAU` tablosu:
  2025-2026→MAVO 2, 2026-2027→HAVO 3); landing'de "Archief — vorige schooljaren" başlığı altında
  yıl grupları. `index.html` hero'ya güncel ders yılı (2026-2027); `?v=2.8`.
* **Kural**: Bir ders yılı bitince o yılın dersleri `archief/<schooljaar>/<vak>/`'e taşınır +
  `VAKKEN`'de `jaar` işaretlenir + `JAAR_NIVEAU`'ye satır eklenir.
* **Kim**: Opus.

### Milestone 16: Geschiedeniswerkplaats 3 HAVO — Complete Integration of Chapters 1 to 6 (2026-08-23)
* **Goal**: Expand Geschiedenis HAVO 3 to fully cover all 6 chapters of the *Geschiedeniswerkplaats 3 HAVO* textbook (De Eerste Wereldoorlog, Tussen de oorlogen, De Tweede Wereldoorlog, De wereld na 1945, Nederland na 1945, and Naar de wereld van nu).
* **Implementation Details**:
  - **OCR Text Extraction**: Processed scanned PDF textbooks for Hoofdstuk 1 through 6 using PyMuPDF and macOS Vision OCR (`VNRecognizeTextRequest`), extracting ~300,000 characters of full curriculum text into `inbox/`.
  - **Chapter Structure & Metadata**: Configured `DURU.hoofdstukken` in `havo3/geschiedenis/js/bootstrap.js` to define all 6 chapters with custom icons, color themes, and introductory descriptions.
  - **Practice Modules**: Generated 30 practice subchapter JS files (`h1_1_tijd.js` through `h6_5_klimaat.js`) with comprehensive theory summaries (`<h3>/<h4>`, `info-box`, `formule-box`) and 240 interactive practice questions with explanations.
  - **20-Question Proeftoetsen**: Created 30 full proeftoets files (`examen_1.js` through `examen_30.js`), with exactly 5 20-question proeftoetsen per chapter (600 exam questions total, 840 questions combined across all modules).
  - **Interactive Chapter Accordion UI**: Redesigned `havo3/geschiedenis/js/engine.js` and `exams.js` to render each chapter as an interactive, collapsible Chapter Card (`.hf-accordion-card`), allowing students to expand/collapse any chapter with a single click.
  - **Cache Control & Deployment**: Added `?v=3.7` cache-busting query strings to all 60 script tags in `index.html` and root `index.html`. Validated full Node execution (840 questions registered clean), committed, and deployed to GitHub Pages (`main`).

### Milestone 17: Moderne Wiskunde 2 HAVO/VWO — Hoofdstuk 2: Statistiek Integration (2026-08-25)
* **Goal**: Convert Duru's *Moderne Wiskunde 2 havo-vwo - Hoofdstuk 2 Statistiek.pdf* into complete interactive practice modules and exam proeftoetsen targeting school exams.
* **Implementation Details**:
  - **OCR Extraction**: Rendered 19 PDF pages to PNG (`pdftoppm`) and extracted 57,431 characters of full textbook text (`tesseract nld+eng`).
  - **Bootstrap Setup**: Configured `DURU.hoofdstukken` in `havo3/wiskunde/js/bootstrap.js` for Hoofdstuk 2 (Statistiek).
  - **5 Practice Subchapters**:
    1. `h2_1_verhoudingstabel.js`: Paragraaf 2.1 — Verhoudingstabel & Percentages (berekeningen via 1, korting, totaal vs 100%, stijging).
    2. `h2_2_cirkeldiagram.js`: Paragraaf 2.2 — Cirkeldiagram (sectoren, 100% = 360°, hoek berekenen `(deel/totaal)*360°`, diagram aflezen/tekenen).
    3. `h2_3_frequentietabel.js`: Paragraaf 2.3 — Frequentietabel, staafdiagram en lijndiagram (frequentie, staaf- en lijndiagrammen, tijdverloop).
    4. `h2_4_centrummaten.js`: Paragraaf 2.4 — Gemiddelde, modus en mediaan (centrummaten berekenen bij getallenrijen en frequentietabellen).
    5. `h2_5_steelbladdiagram.js`: Paragraaf 2.5 — Steelbladdiagram (steel en bladeren, geordende data, centrummaten en waarden aflezen).
  - **5 Proeftoetsen**: Created 5 full 15-question exam files (`examen_1.js` through `examen_5.js`) with 75 total exam questions (109 questions combined across all modules).
  - **Validation & HTML Integration**: Added script tags to `havo3/wiskunde/index.html` (`?v=2.0`), bumped root `index.html` (`?v=3.8`), and validated clean execution with Node.js stub test.

### Milestone 18: buiteNLand 3 HAVO — Hoofdstuk 1 (Wereldhandel in beweging) & Hoofdstuk 2 (Schatkist aarde?) (2026-08-30)
* **Goal**: Process Duru's textbook PDF (`Aardrijkskunde_3havo_Leerwerkboek_Hoofdstuk_1.pdf` - 45 pages covering both Hoofdstuk 1 and Hoofdstuk 2) into complete chapter structures, interactive theory modules, and 10 full 20-question proeftoetsen (5 per chapter, 200 exam questions total, 280 questions overall) with strict quality gate validation.
* **Implementation Details**:
  - **OCR Text Extraction**: Converted 45 scanned PDF pages to PNG (`pdftoppm`) and performed OCR extraction (`tesseract nld+eng`) using local traineddata (`scratch/tessdata/nld.traineddata`), yielding 133,721 characters of full textbook text.
  - **Chapter Division**:
    - **Hoofdstuk 1: Wereldhandel in beweging**: §1.1 Kantelt het economisch wereldbeeld?, §1.2 Wereldhandel: van kolonialisme tot nu, §1.3 Grondstoffen op de wereldmarkt, §1.4 Rol van Europa in de wereldhandel, §1.5 Rol van Nederland in de wereldhandel.
    - **Hoofdstuk 2: Schatkist aarde?**: §2.1 De geschiedenis van de aarde, §2.2 Het dagboek van de aarde, §2.3 Het gebruik van delfstoffen, §2.4 Delfstoffen in Europa, §2.5 Delfstoffen in Nederland.
  - **10 Full 20-Question Proeftoetsen**:
    - `examen_1.js` to `examen_5.js`: 5 proeftoetsen for Hoofdstuk 1 (100 exam questions).
    - `examen_6.js` to `examen_10.js`: 5 proeftoetsen for Hoofdstuk 2 (100 exam questions).
  - **10 Practice Onderwerpen**: Created `h1_1.js` through `h2_5.js` with comprehensive theory (>1500 chars) and 8 practice questions each (80 practice questions).
  - **Quality Gates & Validation**:
    - Ran `tools/spread.py` to ensure perfectly balanced MCQ option rotation ({"0":30, "1":30, "2":30, "3":30} general distribution, no option >40%).
    - Ran `tools/open_check.js` to ensure short, scorable keywords (1-3 words) with no keywords leaked in questions.
    - Passed all 12 rules of `tools/gate.js` with 0 errors (`SONUC: 12 gecti, 0 kaldi`).
  - **UI Integration**: Enhanced `havo3/aardrijkskunde/js/exams.js`, `bootstrap.js`, and `style.css` with accordion cards grouped by chapter. Updated `index.html` with script tags (`?v=3.8`).

### Milestone 19: Begrippen, Personen & Gebeurtenissen Standard for All Chapters & Tests (2026-08-30)
* **Goal**: Establish a permanent project-wide rule and workflow standard: for every course and for every chapter separately, extract all definitions/terms (*begrippen*), key figures (*personen*), critical events/dates (*gebeurtenissen*), and exam keywords; place them into a dedicated glossary/study section (`Begrippen & Kernconcepten`); and automatically create a dedicated vocabulary test (`Begrippentoets`) testing exclusively these terms whenever "test hazırla" is requested.
* **Implementation Details**:
  - **Pipeline Standard**: Formally added the Begrippen & Kernconcepten protocol to `docs/PIPELINE.md`.
  - **Agent Guidelines**: Updated root `CLAUDE.md` to mandate that any future test preparation ("test hazırla") triggers this two-fold extraction and generation process automatically for each individual chapter and subject.



### Milestone 20: Hoofdstuk-bazlı istatistik — tek doğru kaynak (manifest) (2026-09-02)
* **Sorun**: Ünite (hoofdstuk) kırılımı `js/dashboard.js` + `js/ouder_dashboard.js` içine **elle yazılmış
  ve uydurma** iki `HOOFDSTUK_REGISTRY` kopyasından besleniyordu; 12 dersin 8'inde gerçek
  `DURU.hoofdstukken` ile uyuşmuyordu (wiskunde H2↔"H1 Lineaire Formules", biologie H10↔"H1 Organen",
  frans 8 hoofdstuk↔2, natuurkunde H1-4+H8↔1, aardrijkskunde/economie/scheikunde/engels benzeri).
* **Çözüm — manifest mimarisi**:
  - `tools/build_hoofdstukken.js`: her `havo3/<vak>/js/bootstrap.js` + `js/data/*.js`'i node `vm`
    sandbox'ında çalıştırıp `js/hoofdstukken.js` üretir (hoofdstuk listesi, examId→hoofdstuk,
    onderwerpId→hoofdstuk, ünite başına sınav/onderwerp sayısı). `--check` modu bayat manifest'te exit 1.
  - `js/hoofdstuk_util.js`: ortak `window.DURU_HF` API (`lijst/meta/vanAttempt/vanOnderwerp/
    totaalExamens/totaalOnderwerpen`). İki dashboard da yalnız bunu kullanır; ayrı liste YOK.
  - `index.html`: `hoofdstukken.js` → `hoofdstuk_util.js` → `landing.js` sırasıyla yüklenir (`?v=3.9`).
* **⚠️ KRİTİK TUZAK — `ex-h3-<vak>-N` id'sindeki `h3` HOOFDSTUK DEĞİL, NIVEAU'dur (HAVO 3).**
  Sınav id'sinden hoofdstuk çıkarmaya çalışan her regex yanlıştır; hoofdstuk'suz her kayıt sahte
  olarak "H3"e düşer. Fallback zinciri: `att.hoofdstuk` → manifest `examenHoofdstuk[examId]` →
  başlıkta `Hoofdstuk N` → `null` ("Overige toetsen"). Tahmin (`floor((n-1)/5)+1`) yasak.
* **Veri düzeltmeleri**: natuurkunde examen_1-25 → H1/2/3/4/8, scheikunde `examen_h1_*`→H1 &
  `examen_1-5`→H2, biologie examen_1-5→H10. 12 dersin `exams.js`'i başlığı `DURU.hoofdstukken`'den
  okur, hoofdstuk'suz sınavı `null` kaydeder (eskiden hepsi yanlışça H1'di).
* **Yeni ölçüler**: ünite kartlarında gemiddeld/hoogste/laatste cijfer + **toetsvoortgang**
  (benzersiz çözülen/gerçek toplam) + **oefenvoortgang** (≥1 poging yapılmış onderwerp/toplam).
  Sahte `maxExams:5` sabiti kaldırıldı (economie'de ünite başına 3 sınav var).
* **Oefen→hoofdstuk eşlemesi düzeldi**: eski `/h(\d+)_/` regex'i `ak-h1-2`, `sch-h1-3-…`,
  `bio-h10-1-…`, `h2-1-…` gibi gerçek id'leri hiç yakalamıyordu → artık manifest üzerinden.
* **Dil**: Duru'nun gördüğü her yer (12 `engine.js` ünite tablosu + `index.html` + `dashboard.js`)
  Flamancaya çevrildi; **veli sayfası (`ouder_dashboard.js`) bilinçli olarak Türkçe kalır**.
* **Doğrulama**: 12 `engine.js` + tüm data/exams dosyalarında `node --check`;
  `node tools/build_hoofdstukken.js --check` exit 0; headless DOM-stub harness ile hem öğrenci
  hem veli dashboard'u render edilip ünite kırılımı, "Overige toetsen" ve oranlar doğrulandı.

---

## 📅 Milestone 9: Veli panelinin yeniden tasarımı (2026-09-03)

* **Sorun**: `ouder_dashboard.js`'in render katmanı 4 eşit KPI kartı + iki dev tablo + açılır satır
  kırılımından ibaretti. Her blok kart olduğu için hiyerarşi yoktu; "Baba bugün neye baksın?"
  sorusunun cevabı sayfanın hiçbir yerinde tek bakışta okunmuyordu. Notlar metin olarak vardı ama
  5,5 geçme sınırına göre nerede durdukları görünmüyordu.
* **Yapılan**: Yalnız **render katmanı** (eski satır 399–825) değişti. `collectParentReportData`
  ve `VAK_CONFIG` **olduğu gibi korundu** — manifest entegrasyonu ve iki-yıl desteği zaten doğruydu.
  - **Cijferschaal**: Hollanda 1–10 ölçeği gerçek bir cetvel olarak çizildi (`.ouder-schaal*`).
    5,5 eşiği çizgiyle işaretli; büyük nokta genel ortalama, küçük noktalar her dersin ortalaması.
    Hangi dersin sınırın hangi tarafında olduğu tek bakışta okunuyor.
  - **"Önce buraya bakın"** paneli: sayfadaki tek vurgulu blok (sol kenarında `--ouder-zwak` şerit).
    Ortalaması 5,5 altındaki **hoofdstuk**'lar (attempt değil) en zayıftan sıralı, her biri
    manifest'ten gelen `advice` ile.
  - **Sekmeli görünüm** (`data-ouder-view`): `overzicht` / `vakken` / `units` / `logboek`.
    Yalnız aktif görünüm HTML'e basılır → tek seferde basılan DOM ~4 kat küçüldü.
    `actieveView` + `gekozenVak` + `logFilter` modül düzeyinde tutulur; yıl değişimi ve
    `cloud_sync.js`'in periyodik `renderParentDashboard()` çağrısı seçimi artık sıfırlamıyor.
  - **Ders listesi** ortalamaya göre artan sıralı (en çok ilgi bekleyen üstte); eski tablo alfabetikti.
  - Günlük filtreleri (arama/ders/sonuç) yalnız tabloyu yeniden çizer → yazarken odak kaybolmuyor.
* **Renk sözleşmesi (ÖNEMLİ)**: anlam renkleri marka yeşilinden **ayrıldı**.
  `--ouder-goed/net/zwak` + `-zacht` tonları `#ouder-view` üzerinde tanımlı, `html.dark #ouder-view`'de
  yeniden tanımlanır. Yeşil artık "iyi" demek, marka rengi değil. Proje tokenleri (`--wit`, `--inkt`,
  `--lijn`, `--font-titel/tekst`, `--schaduw-sm`) korundu; koyu tema `html.dark` mekanizmasında kaldı.
* **Kaldırılanlar**: `.ouder-kpi-*`, `.ouder-header-card`, `.ouder-insight-*`, `.ouder-grade-pill`,
  `.ouder-vak-breakdown-*` ve `window.toggleOuderVakBreakdown` (inline `onclick`'ler de gitti).
  Repo genelinde bunlara kalan referans yok (grep ile doğrulandı).
* **Ölçüler**: `css/style.css` 2656 → 2163 satır (-493), `js/ouder_dashboard.js` 839 → 936 satır.
  `index.html`'de tüm `?v=3.8` → **`?v=3.9`**.
* **Doğrulama**: `node --check js/ouder_dashboard.js` temiz. Headless DOM-stub harness ile gerçek
  veri (Frans H1/H3 + Geschiedenis H1) render edildi: genel ortalama **6,6** elle hesapla birebir
  (7,3 · 4,6 · 5,5 · 9,1), zayıf ünite tespiti Frans H3'ü (5,05) yakaladı, dört görünüm de
  `undefined`/`NaN` üretmeden render oldu, veri olmayan yıl boş-durum metnine düştü.
* **Tasarım önizlemesi** (onay için, canlıya girmeden önce paylaşıldı):
  https://claude.ai/code/artifact/2d374d3a-59a1-4217-8acc-d070aca3123f

### Ek (aynı gün) — yarım kalan işler kapatıldı

* **Manifest bayatlığı giderildi**: `node tools/build_hoofdstukken.js --check` exit 1 veriyordu
  (`95572da`'dan beri). Yeniden üretildi → **exit 0**. Kaçan veri: 6 economie sınavı
  (`ex-h3-economie-13..18`) → economie H1 `3→6`, H4 `3→6`. Bu sınavlar "Overige toetsen"e
  düşüyordu, artık doğru üniteye yazılıyor. Başka ders etkilenmedi (diff 10 satır).
* **`maatschappijleer` + `nederlands` uyarıları bilinçli bırakıldı**: `bootstrap.js`'te
  `DURU.hoofdstukken = []` (materyal yok). Smoke-test sınavlarına ünite numarası vermek
  **uydurma metadata** olurdu — projenin daha önce bedelini ödediği hata. Alan boş kaldı.
* **`CLAUDE.md` doluluk tablosu baştan sayıldı** — ciddi bayattı: `engels`/`frans`/`duits`
  "smoke-test 0/1/5" yazıyordu, gerçekte 30/40 proeftoets'leri var; `economie` "0/1/20" yazıyordu,
  gerçek 12/18/456. Yeni toplam: **126 onderwerp · 205 proeftoets · 5082 soru**.
  Sayım yöntemi doğrulandı (geschiedenis 840 = eski tablodaki değer).
* **`docs/ENGINE_SPEC.md` boşluğu kapatıldı**: "tek doğru kaynak" olan Sözleşme 2'de
  (`registerExamen`) **`hoofdstuk` alanı hiç yazmıyordu**, oysa CLAUDE.md zorunlu diyor ve tüm
  manifest hattı buna dayanıyor. Bu boşluk `ex-h3-*` niveau tuzağının kaçmasına zemin hazırlamıştı.
  Alan + niveau tuzağı + "ünite uydurma" kuralı spec'e eklendi.
* **Yeni açık iş**: `frans` 40 proeftoets'e sahip ama **0 onderwerp** — 12 ders içinde tek böyle.
  Oefenvoortgang hep %0 görünüyor. `coordination.md`'ye TODO olarak yazıldı.

## 📅 Milestone 10: Pano denetimi + Faz 1 optimizasyonu (2026-09-04)

Öğrenci ve veli panoları için ölçüme dayalı denetim yapıldı (8 bulgu, artifact olarak sunuldu),
Faz 1 uygulandı.

* **Yazdırma regresyonu onarıldı** (2026-09-03'te ben yapmıştım): tek-sekme-DOM stratejisi
  yazdırmayı bozuyordu. `beforeprint`/`afterprint` kancaları + `vakDetailHtml()` ayrıştırması.
* **`scores.json` v2**: append-only anlık görüntü kütüğü → anahtar-bazlı sözlük + `history`
  birleştirme. **27,3 MB → 0,58 MB, 287 poging, sıfır kayıp.** Yan dosya `events.jsonl`
  (poging başına ~100 B). `GET /api/score` liste döndürmeye devam ediyor → `restoreScores()`
  sözleşmesi bozulmadı. v1 otomatik göç + backup.
* **POST debounce** (`queueScoreSync`): sınav başına ~20 istek → 1. `sendBeacon` ile kapanışta flush.
* **Yan bulgu**: boş günlükte yanlış sebep gösteriliyordu ("filtrelerle eşleşmedi" ≠ "hiç veri yok").
* **Ölçüm yöntemi**: göç öncesi/sonrası anahtar başına benzersiz `attemptId` kümeleri karşılaştırıldı;
  yazdırma yolu headless harness'ta `beforeprint` kancası tetiklenerek 4 bölüm de doğrulandı.
* **Faz 2 (bekliyor)**: parça-eşleşmeli storage taramasını kaldır (çok-kullanıcı veri sızıntısı
  riski), `js/vakken.js` tek ders kaynağı, `js/cijfer_util.js` tek not mantığı.
* `index.html` → `?v=4.0`.

### Faz 2 (aynı gün) — tek kaynak refactor'ları

* **Çok-kullanıcı sızıntısı kapandı**: iki panodaki substring-taramalı storage fallback'i kaldırıldı.
  Ayrıca veli panelinin ilk denemesi `localStorage.getItem(key)` idi; landing.js override'ı bunu
  **aktif kullanıcıyla** önekliyordu — Baba bakarken Duru'nun raporu isteniyordu, yanlıştı.
  Yeni `leesRuw()` `originalGetItem` ile ham okuyor, kişiyi açıkça adresliyor.
* **`js/vakken.js` (`DURU_VAKKEN`)**: ders listesi 3 → 1. `VAK_REGISTER` ve `VAK_CONFIG` zaten
  kelimesi kelimesine aynıydı. Arşiv dersleri landing'de bırakıldı (iç içe `onderwerpen` taşıyan
  navigasyon, istatistik karşılığı yok). HAVO 3 economie ikonu `🏛️`→`💶` (maatschappijleer ile
  çakışıyordu) — tek bilinçli davranış değişikliği.
* **`js/cijfer_util.js` (`DURU_CIJFER`)**: formül + eşikler tek yerde. Renk paylaşılmıyor;
  panoların tokenları farklı, ortak olan sınıflandırma. Kalan ham `5.5`/formül: 0.
* **Regresyon testi**: türetilen değerler `git show HEAD` ile karşılaştırıldı —
  **tüm storage anahtarları byte-byte aynı**, 12 landing kartı eski href/sleutel/id/domein ile
  eşleşiyor, cijfer formülü 7 yüzdede aynı sonucu veriyor.
* **Yükleme sırası kritik**: `vakken.js` → `cijfer_util.js` → … → `ouder_dashboard.js`
  (sonuncusu `DURU_CIJFER`'i yüklenme anında okuyor).
* **Faz 3 (bekliyor)**: rapor önbelleği + kısmi yeniden çizim, sparkline/trend oku,
  onderwerp'siz derste alıştırma çubuğunu gizle.

### Faz 3 (aynı gün) — hız + okunabilirlik; pano denetimi kapandı

* **Rapor önbelleği**: `haalContext()` ham string uzunluğu + ilk/son 48 karakterden imza üretiyor,
  parse etmeden. Sekme/yıl/senkron artık gereksiz yere yeniden hesaplamıyor.
* **Kısmi çizim**: `wisselView()` yalnız `.ouder-views`'i değiştiriyor. `bindParentEvents` ikiye
  bölündü (`bindKopEvents` / `bindViewEvents`) — kopbalk `.ouder-views` dışında olduğu için
  tabwissel'de handler'ları hayatta kalıyor.
* **Sparkline + trend**: 62×18 inline SVG (kütüphane yok), 5,5 eşiği kesik çizgi, son nokta vurgulu.
  Trend = son 3 ile önceki 3'ün farkı; <4 deneme → hüküm yok, <0,3 puan → düz.
  "Önce buraya bakın" artık **düşüş trendindekini** sabit-düşük olandan önce sıralıyor.
* **frans alıştırma çubuğu** veli panelinde gizlendi (0 onderwerp). Öğrenci panosunda zaten doğruydu.
* **Faz 3 testi** önbellek geçersizleştirmeyi ölçüyor — bayat önbellek en olası regresyondu.
* **Harness dersi**: üç kez stub eksikliği (`window.addEventListener`, `document.querySelector`,
  `setAttribute`) test hatası olarak göründü. Headless harness gerçek DOM'un yalnız kullanılan
  yüzeyini taklit ediyor; yeni DOM API'si kullanınca stub'ı da genişlet.
* `index.html` → `?v=4.1`. **Pano denetiminin 8 bulgusunun 8'i kapandı.**
