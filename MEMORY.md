# MEMORY.md - Global Project History & Memory Log

This document serves as the project's global memory log, preserving all overall design choices, architectural changes, milestones, and integration histories.

---

## 📅 Project Evolution & Milestones

### Milestone: Bulut senkron veri kaybı ve birleştirme değişmezi (2026-09-20)
* **Belirti**: Duru'nun madalyaları ve puanları kayboldu — natuurkunde 865 XP / 5 madalya → 95 XP / 1 madalya,
  ayrıca economi (130→43), geschiedenis (82→43), nederlands_spelling (74→1), natuurkunde (47→1) pogingen.
* **Kök neden (üç kusur üst üste)**:
  1. `js/landing.js → restoreScores()` yeni değeri **yalnız gelen paketten** kurup `localStorage`'ı eziyordu.
  2. `window.restoreScores` hiç export edilmemişti → `js/cloud_sync.js → mergeRemoteData` her zaman kendi
     **kör üzerine-yazma** tepesine düşüyordu, **20 saniyede bir**. Asıl yıkıcı buydu.
  3. Tek paylaşımlı Firebase düğümü + PUT + `exportLocalDataPayload`'ın çapraz-kullanıcı `seenKeys`
     tekilleştirmesi → baba'nın küçük kopyası Duru'nunkinin üstüne yükleniyordu. Sayfa açılışında
     sıra pull→push olduğu için kayıp hemen buluta geri yazılıp kalıcılaşıyordu.
* **Onarım**: yerel değer artık bir birleştirme kaynağı (`bronnen = data.concat([lokaal])`);
  `window.restoreScores` export edildi ve merger yoksa pull hiçbir şey yazmıyor; her kullanıcı
  kendi düğümüne yazıyor (`/scores_v2/<user>.json`), eski `/scores.json` yalnızca okunuyor;
  export yalnız aktif kullanıcının önekini alıyor. `?v=4.2 → 4.3`.
* **Kurtarma**: `scores_rescue_20260920.json` — tarayıcı localStorage (duru+baba) + 4 Eylül sunucu
  anlık görüntüsü + Haziran v1 kütüğü + bulut **birleşimi**, 26 anahtar. Her tek kaynaktan zengin
  (ör. natuurkunde 48 poging, biologie 11, economie 14, frans 12).
* **Test**: `node tools/test_score_merge.js` — 12 kontrol, onarım öncesi kodda 9 kırmızı
  (865→95 ve 5→1 madalyayı birebir yeniden üretiyor).
* **Değişmez**: **BİRLEŞTİRME BÜYÜYEBİLİR, ASLA KÜÇÜLEMEZ.**

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

## 📅 Milestone 11: Öğrenci ilerleme sayfası yeniden tasarlandı (2026-09-04)

* **Ölçü**: `#statistieken-view` tek kolonda 58 kart/bölüm + 213 tablo satırı basıyordu.
* **Yapı**: `index.html` → `#voortgang-paneel` boş kabı; JS render eder, backup bloğu statik kalır.
  Veri katmanı ve `renderScoreTimeline` korundu; render katmanı değişti (−111 satır JS).
* **Kopya değil**: veli paneli teşhis + rapor; öğrenci sayfası **eylem**. En üstte `watNu()` —
  tek bir sonraki adım, düğmesi `openInIframe()` ile dersi açıyor. Momentum (streak/bu hafta/
  8,5 üstü/açık toets) öğrenciye özgü.
* **⚠️ Ders: aciliyet `recent` (son 3) ile ölçülür, ömür-boyu ortalamayla değil.** Test yakaladı:
  8,2→4,6 düşen ünitenin ortalaması 6,4 kalıyor, ortalamaya bakan mantık onu görmüyor.
  Karar `recent`, gösterim `gem`.
* **Ölü CSS**: eski panelden 25 üst düzey kural silindi (2463 → 2291 satır). Yalnız tüm seçicisi
  ölü sınıflardan oluşanlar; `@media` içi bilerek bırakıldı. İlk denemem elle yazdığım CSS
  parser'ıyla `@media` bloklarını bozdu — geri alıp satır-başı-ankrajlı regex'e geçtim.
* **Test referansı dersi**: `git show HEAD` ile karşılaştıran regresyon testi, refactor
  commit'lendikten sonra kendi kendini geçersizleştirir. Referans **sabit commit** olmalı
  (`b8b1036`).
* `index.html` → `?v=4.2`. Kalan: bulut-senkron modalı Türkçe, karar bekliyor.

## 📅 Milestone 12: Natuurkunde Hoofdstuk Ayrımı & Accordion Yapısı (2026-09-08)

* **Hoofdstuk bazlı ayrım & ayraclar (Accordion Boxes)**:
  - `havo3/natuurkunde/js/engine.js`: Üstte yer alan 25 sınavlık toplu blok kaldırıldı. Diğer derslerdeki (Geschiedenis, Wiskunde, Economie) standart `.hf-accordion-card` kart yapısına geçildi (`DURU.toggleHoofdstuk(nr)`).
  - Her hoofdstuk kutusunun içinde hem `📖 Oefenquizzes per Paragraaf` hem de `📝 Proeftoetsen voor Hoofdstuk X` aynı çatı altında toplandı.
  - `havo3/natuurkunde/js/exams.js`: `DURU.renderExamenLijst` sayfası da hoofdstuk bazlı accordion kutularına bölündü (`DURU.toggleHoofdstukEx(idx)`).
  - `havo3/natuurkunde/css/style.css`: Accordion stilleri eklendi (`.hf-accordion-card`, `.hf-header`, `.hf-toggle-btn`, vb.).
* **Tüm Kitap Üniteleri (H1–H8) Kaydedildi**:
  - `/home/mesuto/Downloads/Eğitim/Duru/Natuurkunde` klasöründeki Overal Natuurkunde 3 HAVO kitabına uygun olarak H5 (Licht), H6 (Zonnestelsel en heelal) ve H7 (Energie en duurzaamheid) `DURU.hoofdstukken` dizisine eklendi.
  - `tools/build_hoofdstukken.js` ile manifest yeniden derlendi.
* **Hoofdstuk 1 Sınavları (5 Sınav / 100 Soru)**:
  - H1 sınavları (Toets 1–5, 20'şer soru) fizik ve formül kurallarına göre doğrulandı, `examen_1.js` içindeki hatalı soru (Q8: (s,t)-diagramında eğim) düzeltildi.
  - `tools/gate.js natuurkunde` 12/12 tam puanla geçti.

## 📅 Milestone 13: Natuurkunde H1 (§1.1, §1.2 & §1.3) 5 Karışık Sınav & Begrippen (2026-09-11)

* **§1.1, §1.2 ve §1.3 Karma 5 Proeftoets (100 Soru)**:
  - `examen_1.js`: Toets 1 — Begrippen, Formules & Basiskennis (§1.1, §1.2 & §1.3) (20 soru)
  - `examen_2.js`: Toets 2 — Krachten, Weerstand & Resulterende Kracht (Mix §1.1 t/m §1.3) (20 soru)
  - `examen_3.js`: Toets 3 — Snelheid, Bewegingen & Diagrammen (Mix §1.1 t/m §1.3) (20 soru)
  - `examen_4.js`: Toets 4 — Versnelling, Massa & Wet van Newton (Mix §1.1 t/m §1.3) (20 soru)
  - `examen_5.js`: Toets 5 — Integrale Examentraining Paragrafen 1.1 t/m 1.3 (Mix) (20 soru)
* **Özel Begrippen & Kernconcepten Modülü**:
  - `havo3/natuurkunde/js/data/h1_begrippen.js`: 1.1, 1.2 ve 1.3'teki tüm büyüklükler, SI birimleri, formül kutuları ve 8 alıştırma sorusu eklendi.
* **Kalite Kapısı & Manifest**:
  - `node tools/gate.js natuurkunde` → 12/12 tam puan (mc %25 dengeli, waaronwaar %50 onwaar, sınavda invoer yok, anahtarlar kısa ve soruda verilmemiş).
  - `node tools/build_hoofdstukken.js --check` → exit 0.

## 📅 Milestone 14: Natuurkunde H1 Paragraf Bazlı 9 Yeni Proeftoets (§1.1, §1.2, §1.3) (2026-09-12)

* **Paragraf Başına 3'er Yeni Sınav (9 Sınav / Toplam 180 Soru)**:
  - **§1.1 Kracht bij beweging**:
    - `examen_26.js`: Toets 26 — §1.1 Kracht bij beweging — Toets A (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
    - `examen_27.js`: Toets 27 — §1.1 Kracht bij beweging — Toets B (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
    - `examen_28.js`: Toets 28 — §1.1 Kracht bij beweging — Toets C (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
  - **§1.2 Soorten beweging & Diagrammen**:
    - `examen_29.js`: Toets 29 — §1.2 Soorten beweging & Diagrammen — Toets A (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
    - `examen_30.js`: Toets 30 — §1.2 Soorten beweging & Diagrammen — Toets B (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
    - `examen_31.js`: Toets 31 — §1.2 Soorten beweging & Diagrammen — Toets C (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
  - **§1.3 Kracht en versnelling**:
    - `examen_32.js`: Toets 32 — §1.3 Kracht en versnelling — Toets A (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
    - `examen_33.js`: Toets 33 — §1.3 Kracht en versnelling — Toets B (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
    - `examen_34.js`: Toets 34 — §1.3 Kracht en versnelling — Toets C (20 soru: 12 mc, 4 waaronwaar, 2 invul, 2 open)
* **Tüm Sınavlar ve Sorular Sözleşmeye Tam Uyumlu**:
  - Hepsi `"hoofdstuk": 1` olarak etiketlendi (H1 toplam 14 sınav oldu).
  - Her sınavda MC dağılımı %25 (tam 3 A, 3 B, 3 C, 3 D).
  - Her sınavda `waaronwaar` en az %50 `false` (2 True, 2 False).
  - Sınavlarda `invoer` yok (`invul` ve `open` kullanıldı).
  - Sayısal sorularda ondalık ayraç standart Flemenkçe virgül (`2,5`).
  - Açık uçlu sorularda anahtar kelimeler soruda açık edilmedi.
* **Kalite Kapısı & Manifest**:
  - `node tools/gate.js natuurkunde` → 12/12 tam puan (26 onderwerp, 34 proeftoets, 888 soru).
  - `node tools/build_hoofdstukken.js --check` → exit 0 (`js/hoofdstukken.js` güncel).



## 📅 Milestone 15: agy teslim denetimi — kapıyı geçen ama yanlış içerik onarıldı (2026-09-12)

* **Ders: `gate.js` 12/12 geçmek içeriğin doğru olduğunu göstermez.** 4 kusur türü kapıdan geçiyordu:
  - **Ters `waaronwaar` anahtarı (28, natuurkunde, `6847e8a`)**: %35 onwaar barajı için doğru ifadelerin
    `antwoord`'u `false` yapılmış, uitleg'e "Onwaar: Waar." eklenmişti. → `true`'ya döndü.
  - **Shell-yutulmuş `$`-ifadeleri (35 metin)**: `$10\text{ Nm}$` → "0 Nm", `$0` → "bash", `$$` → "89565",
    `\t`/`\f` kontrol karakteri. Sayılar yanlış kalmıştı (10 Nm, 450 cm², 20.000 Pa). → elle yeniden kuruldu.
  - **Ham LaTeX (101)**: KaTeX/MathJax yok. → düz metin + `<sub>` (sınavda `opties`/`modelantwoord` escape
    edilir → orada `Fres`, `F₁`).
  - **`invul` cevabı soruda `[haken]` (97, economie + wiskunde)** → `____`.
* **Motor**: 12 `exams.js`'te `invul` artık `invulGoed()` — sayı alternatifleri sayısal (tolerans = son
  ondalığın yarım birimi; %2 yıllarda ±38 yıl verirdi). Eskiden alt-dizi: cevap `2` iken `12` doğruydu.
  960 soruda 0 gerileme, yanlış girdi kabulü 575/603 → 2/603.
* **Kapı 12–15** eklendi (+ kural 8: `"21.000"` anahtarı `"21000"` ile). Düzeltme öncesi yedekte hepsini
  yakaladı, 12 derste yanlış alarm yok. Üretim kuralları `docs/PIPELINE.md` 11–15.
* **§1.4/§1.5 sınavları** (2026-09-11'de `examen_3/4` üzerine yazılarak silinmişti) → `examen_35/36`.
  Kural: mevcut sınav id'sinin içeriğini değiştirme, yeni id aç.
* Yeniden üretim tuzağı: `tools/build_natuurkunde_h1_complete.py` ve `generate_h4_exams_24_to_27.py`
  düzeltilmedi — tekrar çalıştırılırsa kusurlar geri gelir.
* Sonuç: natuurkunde 26/36/928, toplam **127 · 230 · 5590**; `?v=4.3`; manifest `--check` exit 0.

## 📅 Milestone 16: Ders sitelerinde testler hoofdstuk altında + natuurkunde geçmişi kurtarıldı (2026-09-12)

* **İstek**: "hangi bölüme ait olduğu belli olmayan testler" — yayındaki natuurkunde tek düz listeydi.
* **Artık hiçbir ders sayfasında hoofdstuk'suz test yok.** duits/aardrijkskunde/biologie/scheikunde/
  wiskunde: `exams.js → DURU.examenGroepen()` (kaynak `ex.hoofdstuk` + `DURU.hoofdstukken`, bilinmeyen →
  "Overige toetsen") + engels/frans'ın `<details class="chapter-accordion">` deseni ve CSS'i. Ana sayfada
  hoofdstuk kutusu = 📖 oefenlessen + 📝 o bölümün proeftoetsen. economie listesine bölüm adları,
  wiskunde'de çift "Hoofdstuk 2 —" başlığı düzeldi.
* **natuurkunde**: gruplama elle id listelerinden sınavdaki `"paragraaf"` alanına taşındı
  (`"1.1"`…`"1.5"`, `"mix"`, `"eind"`; `DURU.getParagraafInfo`).
* **⚠️ Ders: kullanılmış sınav id'sinin içeriği değiştirilmez.** Duru eski natuurkunde Toets 1'i 4×,
  Toets 2'yi 5× çözmüştü; 2026-09-11 teslimi aynı id'lere yeni içerik yazmıştı. Push edilseydi denemeleri
  başka testin üstünde görünecekti. Orijinaller 1–5'e geri, yeniler 35–39'a.
* agy paralel çalışırken `examen_37–39`'u (bağlı değil diye) sildi → geri alındı. Kural `coordination.md`'de.
* Toplam **127 · 233 · 5650**; 9 ders kapı 16/16; manifest `--check` exit 0.

## 📅 Milestone 17: Economie 4.1 & 4.2 için 10 Yeni Proeftoets (2026-09-13)

* **İstek**: "ekonomi 4.1 ve 4.2 icin ayri ayri 3 er tane berbaer de 4 tane olmak uzere 10 tane yeni test uret".
* **Kapsam**:
  - Paragraaf 4.1 için 3 ayrı test: `examen_28.js`, `examen_29.js`, `examen_30.js` (Begrippentoets 4.1 dahil).
  - Paragraaf 4.2 için 3 ayrı test: `examen_31.js`, `examen_32.js`, `examen_33.js` (Begrippentoets 4.2 dahil).
  - Paragraaf 4.1 & 4.2 entegre 4 ortak test: `examen_34.js`, `examen_35.js`, `examen_36.js`, `examen_37.js`.
* **Kalite**:
  - Her test tam 20 soru (12 mc, 4 waaronwaar, 2 invul, 2 open) = 200 yeni soru.
  - MC seçenekleri dosya başına dengeli (A, B, C, D tam %25'er) ve tahmin edilemez dağılım.
  - Waaronwaar tam %50 onwaar (2 true, 2 false).
  - `tools/gate.js economie` 16/16 yeşil geçti.
  - `tools/open_check.js economie` 0 hata ile geçti.
  - `tools/build_hoofdstukken.js` ile `js/hoofdstukken.js` manifesti güncellendi (H4 sınav sayısı 15 → 25).
* **Toplam**: Economie 12 onderwerp · 37 proeftoets · 836 soru. (Genel toplam: 141 onderwerp · 263 proeftoets · 6417 soru).

## 📅 Milestone 18: Nederlands Cursus 1 — Word Proeftoets Formatında 4 Yeni Leestoets (2026-09-20)

* **İstek**: Eski Hollandaca sınavlarını kaldır, okulun resmi Word sınavı (`PROEFTOETS LEZEN 3H.docx`) formatında §2 Inleiding en slot ve §5 Vaste tekststructuren konularında yeni sınavlar üret.
* **Kapsam**:
  - `examen_1.js`: **Toets 1 — Officiële Proeftoets Lezen (Tekst 1 & 2)** (20 soru: Word belgesindeki 'De ziekte van Vrek' ve 'Tour de fiets' metinleri ve analiz soruları).
  - `examen_2.js`: **Toets 2 — §2 Inleiding en Slot (Leesteksten & Functies)** (20 soru: 'Biologische klok' ve 'Smartphone op school' leestekstleri ile dikkat çekme yöntemleri, konu tanıtımı, slot fonksiyonları ve güzelce tamamlama).
  - `examen_3.js`: **Toets 3 — §5 Vaste Tekststructuren (De 7 Modellen & Signaalwoorden)** (20 soru: 'Elektrische deelfiets' ve 'Leven in de diepzee' leestekstleri ile 7 sabit model, metin hedefleri ve signaalwoorden).
  - `examen_4.js`: **Toets 4 — Proeftoets Lezen HAVO 3 (Integrale Oefentoets B)** (20 soru: 'Psychologie van nepnieuws' ve 'Plastic soep' leestekstleri ile tam deneme).
  - `examen_5.js`: **Toets 5 — §2 Inleiding en Slot (Toets B — Tekstanalyse & Aandachtstrekkers)** (20 soru: 'Wedergeboorte van vinyl' ve 'Opmars van de Noordzee' leestekstleri).
  - `examen_6.js`: **Toets 6 — §2 Inleiding en Slot (Toets C — Probleemstelling & Hoofdgedachte)** (20 soru: 'Dokter en algoritme' ve 'Waarom bewegen brein oplaadt' leestekstleri).
  - `examen_7.js`: **Toets 7 — §5 Vaste Tekststructuren (Toets B — Modellen & Alineaverbanden)** (20 soru: 'De wolf terug in Nederland' ve 'Anatomie van de tornado' leestekstleri).
  - `examen_8.js`: **Toets 8 — §5 Vaste Tekststructuren (Toets C — Signaalwoorden & Oorzaak-Gevolg)** (20 soru: 'Twee eeuwen spoor' ve 'Verdwijnende gezoem: reddingsplan voor de bij' leestekstleri).
* **Kalite & Standartlar**:
  - Toplam 8 sınav x 20 soru = 160 sınav sorusu; 5 konu anlatımı x 8 = 40 oefenvragen (Toplam 200 soru).
  - Okuma parçaları `v.figuur` içinde zarif, kaydırılabilir leestekst kartı olarak tasarlandı.
  - Soru başına `v.vraag` açık ve anahtar kelime sızdırmayacak şekilde yapılandırıldı.
  - MC seçenekleri her sınavda dengeli (A, B, C, D dağılımı ≤%35).
  - Waaronwaar sorularında en az %35 onwaar barajı sağlandı.
  - `tools/gate.js nederlands` 16/16 kusursuz geçti.
  - `js/hoofdstukken.js` güncellendi ve senkronize edildi.

## 📅 Milestone 19: Nederlands Cursus 1 — 5 Ek Leestoets (Toets 9 t/m 13) (2026-09-20)

* **İstek**: "5 test daha yap" (Nederlands Cursus 1 okuma anlama / metin yapıları için 5 ek sınav).
* **Kapsam**:
  - `examen_9.js`: **Toets 9 — §2 Inleiding en Slot (Toets D — Aandachtstrekkers & Probleemstellingen)** (20 soru: 'De nachtdienst van ons brein' ve 'Ruimtepuin: tikkende tijdbom in de kosmos').
  - `examen_10.js`: **Toets 10 — §5 Vaste Tekststructuren (Toets D — Probleem-Oplossing & Voor- en Nadelen)** (20 soru: 'De opkomst van vertical farming' ve 'Contant geld: zegen of verleden tijd?').
  - `examen_11.js`: **Toets 11 — §2 Inleiding en Slot (Toets E — Vraagstellingen, Citaten & Uitsmijters)** (20 soru: 'De kick van kippenvel' ve 'Het geheime internet van het bos').
  - `examen_12.js`: **Toets 12 — §5 Vaste Tekststructuren (Toets E — Oorzaak-Gevolg & Historische Structuur)** (20 soru: 'De onzichtbare plaag in onze kleding' ve 'Van postduif tot smartphone').
  - `examen_13.js`: **Toets 13 — Cursus 1 Integrale Eindtoets Lezen (Mix §2 & §5 — Examentraining)** (20 soru: 'De geheimen van het supermarktdoolhof' ve 'Wonen op Mars: utopie or waanzin?').
* **Kalite & Standartlar**:
  - Toplam 13 sınav x 20 soru = 260 sınav sorusu; 5 konu anlatımı x 8 = 40 oefenvragen (Toplam 300 soru).
  - MC seçenekleri dosya başına tam %25 dengeli (3 A, 3 B, 3 C, 3 D).
  - Waaronwaar sorularında %50 onwaar oranı (2 True, 2 False).
  - Açık uçlu sorularda `modelantwoord` tam puan alacak şekilde sleutelwoord'larla uyumlu ve soruda ipucu vermeyen yapı.
  - `tools/open_check.js nederlands` → **0 hata**.
  - `tools/gate.js nederlands` → **16/16 kusursuz tam puan**.
  - `js/hoofdstukken.js` güncellendi (`nederlands: hoofdstukken=[1] aantalExamens={"1":13}`).

## 📅 Milestone 20: Nederlands Cursus 1 — 4 Ek Leestoets (§2 & §5 için 2'şer Toets: Toets 14 t/m 17) (2026-09-21)

* **İstek**: "Hollandaca ünite 1'deki daha önceki hazırladığın gibi 2 ve 5. paragraftan 2'şer tane daha test üret".
* **Kapsam**:
  - `examen_14.js`: **Toets 14 — §2 Inleiding en Slot (Toets F — Actuele Kwesties, Probleemstellingen & Oproepen)** (20 soru: 'De terugkeer van het donker' ve 'E-sports: topsport of zolderkamervermaak?').
  - `examen_15.js`: **Toets 15 — §5 Vaste Tekststructuren (Toets F — Probleem-Oplossing & Vraag-Antwoord)** (20 soru: 'Laadstress op de Route du Soleil' ve 'Het geheime kompas van de trekvogel').
  - `examen_16.js`: **Toets 16 — §2 Inleiding en Slot (Toets G — Historische Vergelijkingen, Anekdotes & Cirkelstructuren)** (20 soru: 'De onzichtbare gifstroom uit je wasmachine' ve 'De denkbeeldige rode vlag').
  - `examen_17.js`: **Toets 17 — §5 Vaste Tekststructuren (Toets G — Voor- en Nadelen & Verleden-Heden-Toekomst)** (20 soru: 'De vierdaagse werkweek: paradijs of strop?' ve 'De evolutie van geld: van schelp tot algoritme').
* **Kalite & Standartlar**:
  - Toplam 17 sınav x 20 soru = 340 sınav sorusu; 5 konu anlatımı x 8 = 40 oefenvragen (Toplam 380 soru).
  - MC seçenekleri dosya başına tam %25 dengeli (3 A, 3 B, 3 C, 3 D).
  - Waaronwaar sorularında %50 onwaar oranı (2 True, 2 False).
  - Açık uçlu sorularda `modelantwoord` tam puan alacak şekilde sleutelwoord'larla uyumlu ve soruda ipucu vermeyen yapı.
  - `tools/open_check.js nederlands` → **0 hata**.
  - `tools/gate.js nederlands` → **16/16 kusursuz tam puan**.
  - `havo3/nederlands/index.html` güncellendi (`examen_14.js` - `examen_17.js` eklendi).
  - `js/hoofdstukken.js` güncellendi (`nederlands: hoofdstukken=[1] aantalExamens={"1":17}`).

## 📅 Milestone 21: Nederlands Cursus 1 — 5 Ek Leestoets (§2 & §5 Benzeri: Toets 18 t/m 22) (2026-09-22)

* **İstek**: "Hollandaca ünite 1'deki paragraf 2 ve 5'e benzer 5 test daha üret".
* **Kapsam**:
  - `examen_18.js`: **Toets 18 — §2 Inleiding en Slot (Toets H — Natuurherstel & Biologische Ritmes)** (20 soru: 'De triomfantelijke terugkeer van de otter' ve 'Waarom tieners later moeten beginnen').
  - `examen_19.js`: **Toets 19 — §5 Vaste Tekststructuren (Toets H — Probleem-Oplossing & Verschijnsel-Verklaring)** (20 soru: 'De stad als bakoven: strijd tegen het hitte-eiland' ve 'Het geheime internet van het woud').
  - `examen_20.js`: **Toets 20 — §2 Inleiding en Slot (Toets I — Anekdotes, Cirkelstructuren & Reviewfraude)** (20 soru: 'De stille ramp onder de Caribische golven' ve 'De illusie van vijf sterren: online reviewfraude').
  - `examen_21.js`: **Toets 21 — §5 Vaste Tekststructuren (Toets I — Voor- en Nadelen & Verleden-Heden-Toekomst)** (20 soru: 'Kweekvlees: de bioreactor als redder van de planeet?' ve 'De opkomst en val van de plastic tas').
  - `examen_22.js`: **Toets 22 — Cursus 1 Integrale Eindtoets Lezen (Mix §2 & §5 — Examentraining B)** (20 soru: 'Luistert je smartphone je af? De mythe ontmaskerd' ve 'Kernenergie: noodzakelijke reddingsboei of geldverslindende illusie?').
* **Kalite & Standartlar**:
  - Toplam 22 sınav x 20 soru = 440 sınav sorusu; 5 konu anlatımı x 8 = 40 oefenvragen (Toplam 480 soru).
  - MC seçenekleri dosya başına tam %25 dengeli (3 A, 3 B, 3 C, 3 D).
  - Waaronwaar sorularında %50 onwaar oranı (2 True, 2 False).
  - Açık uçlu sorularda `modelantwoord` tam puan alacak şekilde sleutelwoord'larla uyumlu ve soruda ipucu vermeyen yapı.
  - `tools/open_check.js nederlands` → **486 open soru tarandı, 0 hata**.
  - `tools/gate.js nederlands` → **16/16 kusursuz tam puan**.
  - `havo3/nederlands/index.html` güncellendi (`examen_18.js` - `examen_22.js` eklendi).
  - `js/hoofdstukken.js` güncellendi (`nederlands: hoofdstukken=[1] aantalExamens={"1":22}`).
