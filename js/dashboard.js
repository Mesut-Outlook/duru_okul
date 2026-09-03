/* =========================================================
   Duru's Schoolhub — Statistics & Dashboard Panel
   Handles: parsing localStorage, calculating statistics,
            dynamic responsive SVG rendering, and table
            filtering/searching per Subject & Hoofdstuk.
   ========================================================= */

(function () {
  "use strict";

  // Global state for filtering
  window.allAttempts = [];
  window.currentTableFilter = "all";
  window.currentTableSearch = "";
  window.currentJaar = null;
  window.currentHoofdstukFilter = "all";

  // ── Schooljaar-register ───────────────────────────────────
  var HUIDIG_SCHOOLJAAR = '2026-2027';
  var JAAR_NIVEAU = { '2025-2026': 'MAVO 2', '2026-2027': 'HAVO 3' };

  var VAK_REGISTER = [
    { jaar:'2025-2026', id:'natuurkunde',          titel:'Natuurkunde (NASK)',    icoon:'⚛️', kleur:'blauw',  practiceKey:'duru_nask_v1',                examKey:'duru_nask_examens_v1' },
    { jaar:'2025-2026', id:'wiskunde',             titel:'Wiskunde',              icoon:'⚖️', kleur:'teal',   practiceKey:'duru_wiskunde_v1',            examKey:'duru_wiskunde_examens_v1' },
    { jaar:'2025-2026', id:'economie',             titel:'Economie',              icoon:'💶', kleur:'groen',  practiceKey:'duru_economi_v1',             examKey:'duru_economi_examens_v1' },
    { jaar:'2025-2026', id:'geschiedenis',         titel:'Geschiedenis',          icoon:'🕰️', kleur:'oranje', practiceKey:'duru_geschiedenis_v1',        examKey:'duru_geschiedenis_examens_v1' },
    { jaar:'2025-2026', id:'nederlands-spelling',  titel:'Spelling & Grammatica', icoon:'✍️', kleur:'oranje', practiceKey:'duru_nederlands_spelling_v1', examKey:'duru_nederlands_spelling_examens_v1' },
    { jaar:'2025-2026', id:'nederlands-begrijpend',titel:'Begrijpend Lezen',      icoon:'🧠', kleur:'oranje', practiceKey:null,                          examKey:'begrijpend_lezen_history', special:'begrijpend' },
    // ── 2026-2027 (HAVO 3) ──
    { jaar:'2026-2027', id:'nederlands',      titel:'Nederlands',      icoon:'📖', kleur:'oranje', practiceKey:'duru_2627_nederlands_v1',      examKey:'duru_2627_nederlands_examens_v1' },
    { jaar:'2026-2027', id:'engels',          titel:'Engels',          icoon:'🇬🇧', kleur:'oranje', practiceKey:'duru_2627_engels_v1',          examKey:'duru_2627_engels_examens_v1' },
    { jaar:'2026-2027', id:'frans',           titel:'Frans',           icoon:'🇫🇷', kleur:'oranje', practiceKey:'duru_2627_frans_v1',           examKey:'duru_2627_frans_examens_v1' },
    { jaar:'2026-2027', id:'duits',           titel:'Duits',           icoon:'🇩🇪', kleur:'oranje', practiceKey:'duru_2627_duits_v1',           examKey:'duru_2627_duits_examens_v1' },
    { jaar:'2026-2027', id:'wiskunde',        titel:'Wiskunde',        icoon:'⚖️', kleur:'teal',   practiceKey:'duru_2627_wiskunde_v1',        examKey:'duru_2627_wiskunde_examens_v1' },
    { jaar:'2026-2027', id:'natuurkunde',     titel:'Natuurkunde',     icoon:'⚛️', kleur:'blauw',  practiceKey:'duru_2627_natuurkunde_v1',     examKey:'duru_2627_natuurkunde_examens_v1' },
    { jaar:'2026-2027', id:'scheikunde',      titel:'Scheikunde',      icoon:'🧪', kleur:'teal',   practiceKey:'duru_2627_scheikunde_v1',      examKey:'duru_2627_scheikunde_examens_v1' },
    { jaar:'2026-2027', id:'biologie',        titel:'Biologie',        icoon:'🧬', kleur:'groen',  practiceKey:'duru_2627_biologie_v1',        examKey:'duru_2627_biologie_examens_v1' },
    { jaar:'2026-2027', id:'geschiedenis',    titel:'Geschiedenis',    icoon:'🕰️', kleur:'oranje', practiceKey:'duru_2627_geschiedenis_v1',    examKey:'duru_2627_geschiedenis_examens_v1' },
    { jaar:'2026-2027', id:'aardrijkskunde',  titel:'Aardrijkskunde',  icoon:'🗺️', kleur:'teal',   practiceKey:'duru_2627_aardrijkskunde_v1',  examKey:'duru_2627_aardrijkskunde_examens_v1' },
    { jaar:'2026-2027', id:'economie',        titel:'Economie',        icoon:'🏛️', kleur:'groen',  practiceKey:'duru_2627_economie_v1',        examKey:'duru_2627_economie_examens_v1' },
    { jaar:'2026-2027', id:'maatschappijleer',titel:'Maatschappijleer',icoon:'🏛️', kleur:'blauw',  practiceKey:'duru_2627_maatschappijleer_v1',examKey:'duru_2627_maatschappijleer_examens_v1' }
  ];

  // ── Initialization on DOM Ready ──────────────────────────
  document.addEventListener("DOMContentLoaded", function () {
    initTabs();
    initFiltersAndSearch();
    initVakKaartenToggle();
    initBackupRestore();
    loadDashboardData();

    window.addEventListener("storage", function (e) {
      if (e.key && (e.key.indexOf("duru_") === 0 || e.key.indexOf("begrijpend_lezen_") === 0)) {
        loadDashboardData();
      }
    });

    var resizeTimeout;
    window.addEventListener("resize", function () {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(function () {
        if (document.getElementById("statistieken-view").classList.contains("active")) {
          renderScoreTimeline(window.allAttempts);
        }
      }, 200);
    });
  });

  // ── Tab Navigation Logic ──────────────────────────────────
  function initTabs() {
    var tabs = document.querySelectorAll(".hub-tab");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) { t.classList.remove("active"); });
        tab.classList.add("active");

        var views = document.querySelectorAll(".hub-view");
        views.forEach(function (v) { v.classList.remove("active"); });

        var targetId = tab.getAttribute("data-target");
        var targetView = document.getElementById(targetId);
        if (targetView) {
          targetView.classList.add("active");
        }

        if (targetId === "statistieken-view") {
          loadDashboardData();
        } else if (targetId === "ouder-view" && typeof window.renderParentDashboard === "function") {
          window.renderParentDashboard();
        }
      });
    });
  }

  // ── Delegated toggle listener for per-subject detail panels ──
  function initVakKaartenToggle() {
    var grid = document.getElementById("vak-stats-grid");
    if (!grid) return;

    grid.addEventListener("click", function (e) {
      var btn = e.target;
      while (btn && btn !== grid) {
        if (btn.classList && btn.classList.contains("detail-toggle")) {
          var card = btn.closest ? btn.closest(".vak-stat-card") : null;
          if (!card) {
            var p = btn.parentNode;
            while (p && !p.classList.contains("vak-stat-card")) {
              p = p.parentNode;
            }
            card = p;
          }
          if (card) {
            var detail = card.querySelector(".vak-detail");
            if (detail) {
              var isOpen = detail.classList.contains("open");
              if (isOpen) {
                detail.classList.remove("open");
                btn.setAttribute("aria-expanded", "false");
                btn.querySelector(".detail-toggle__arrow").textContent = "▾";
              } else {
                detail.classList.add("open");
                btn.setAttribute("aria-expanded", "true");
                btn.querySelector(".detail-toggle__arrow").textContent = "▴";
              }
            }
          }
          break;
        }
        btn = btn.parentNode;
      }
    });
  }

  // ── Schooljaar helpers ─────────────────────────────────────
  function jaarHeeftData(jaar) {
    var rows = VAK_REGISTER.filter(function (v) { return v.jaar === jaar; });
    for (var i = 0; i < rows.length; i++) {
      var vak = rows[i];

      if (vak.special === "begrijpend") {
        try {
          var raw = localStorage.getItem(vak.examKey);
          if (raw) {
            var arr = JSON.parse(raw);
            if (Array.isArray(arr) && arr.length > 0) return true;
          }
        } catch (e) {}
        continue;
      }

      if (vak.practiceKey) {
        try {
          var pRaw = localStorage.getItem(vak.practiceKey);
          if (pRaw) {
            var pObj = JSON.parse(pRaw);
            if (pObj && ((pObj.xp && pObj.xp > 0) || (pObj.badges && Object.keys(pObj.badges).length > 0))) {
              return true;
            }
          }
        } catch (e) {}
      }

      if (vak.examKey) {
        try {
          var eRaw = localStorage.getItem(vak.examKey);
          if (eRaw) {
            var eObj = JSON.parse(eRaw);
            if (eObj && ((eObj.history && eObj.history.length > 0) || (eObj.beste && Object.keys(eObj.beste).length > 0))) {
              return true;
            }
          }
        } catch (e) {}
      }
    }
    return false;
  }

  function beschikbareJaren() {
    var set = {};
    VAK_REGISTER.forEach(function (v) { set[v.jaar] = true; });
    var jaren = Object.keys(set);
    jaren.sort().reverse();
    return jaren;
  }

  function bepaalCurrentJaar() {
    if (window.currentJaar) return window.currentJaar;
    var opgeslagen = null;
    try {
      opgeslagen = localStorage.getItem("duru_dashboard_jaar");
    } catch (e) {}

    if (opgeslagen === "2025-2026" || opgeslagen === "2026-2027") {
      return opgeslagen;
    }
    return HUIDIG_SCHOOLJAAR;
  }

  // ── Render jaar-kiezer ─────────────────────────────────────
  function renderJaarSelector(jaren, actief) {
    var container = document.getElementById("jaar-selector");
    if (!container) return;

    var html = "";
    var isHavo3 = (actief === "2026-2027");
    html += '<button type="button" class="jaar-chip' + (isHavo3 ? " jaar-chip--actief" : "") + '" ' +
              'role="tab" aria-selected="' + (isHavo3 ? "true" : "false") + '" data-jaar="2026-2027">' +
              "🎒 HAVO 3 (2026-2027)" +
            "</button>";

    var isMavo2 = (actief === "2025-2026");
    html += '<button type="button" class="jaar-chip' + (isMavo2 ? " jaar-chip--actief" : "") + '" ' +
              'role="tab" aria-selected="' + (isMavo2 ? "true" : "false") + '" data-jaar="2025-2026" style="opacity:' + (isMavo2 ? '1' : '0.7') + ';">' +
              "📁 MAVO 2 (Arşiv)" +
            "</button>";

    container.innerHTML = html;

    var chips = container.querySelectorAll(".jaar-chip");
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var jaar = chip.getAttribute("data-jaar");
        window.currentJaar = jaar;
        try {
          localStorage.setItem("duru_dashboard_jaar", jaar);
        } catch (e) {}
        loadDashboardData();
      });
    });
  }

  // ── Load & Parse Data ─────────────────────────────────────
  function loadDashboardData() {
    window.currentJaar = bepaalCurrentJaar();
    var jaren = beschikbareJaren();
    renderJaarSelector(jaren, window.currentJaar);

    var vakkenVanJaar = VAK_REGISTER.filter(function (v) { return v.jaar === window.currentJaar; });

    // 1. Calculate Practice XP and Badges
    var totalXP = 0;
    var totalBadges = 0;

    vakkenVanJaar.forEach(function (vak) {
      if (!vak.practiceKey) return;
      var prac = loadPracticeData(vak.practiceKey);
      if (!prac) return;
      totalXP += prac.xp || 0;
      var badges = prac.badges || {};
      totalBadges += Array.isArray(badges) ? badges.length : Object.keys(badges).length;
    });

    var xpEl = document.getElementById("stat-xp");
    var badgesEl = document.getElementById("stat-badges");
    if (xpEl) xpEl.textContent = totalXP;
    if (badgesEl) badgesEl.textContent = totalBadges;

    // 2. Aggregate exam attempts from all subjects
    var attempts = [];

    vakkenVanJaar.forEach(function (vak) {
      if (vak.special === "begrijpend") {
        loadBegrijpendLezenAttempts(attempts, vak.examKey);
      } else {
        loadDuruAttempts(attempts, vak.examKey, vak.id, vak.titel, vak.kleur);
      }
    });

    attempts.sort(function (a, b) {
      return b.timestamp - a.timestamp;
    });

    window.allAttempts = attempts;

    var examsEl = document.getElementById("stat-exams");
    var avgEl = document.getElementById("stat-gemiddelde");

    if (examsEl) examsEl.textContent = attempts.length;

    if (attempts.length > 0) {
      var sum = 0;
      attempts.forEach(function (att) { sum += att.cijfer; });
      var avg = sum / attempts.length;
      if (avgEl) avgEl.textContent = avg.toFixed(1).replace(".", ",");
    } else {
      if (avgEl) avgEl.textContent = "-";
    }

    // Render Components
    renderVakKaarten(attempts, vakkenVanJaar);
    renderHoofdstukStats(attempts, vakkenVanJaar);
    renderScoreTimeline(attempts);
    renderFilterBar(vakkenVanJaar);
    renderAttemptsTable();
  }
  window.loadDashboardData = loadDashboardData;

  // ── Helper: safeReadJson (supports user prefix & raw storage) ─
  function safeReadJson(logicalKey) {
    if (!logicalKey) return null;
    var raw = localStorage.getItem(logicalKey);
    if (!raw && typeof originalGetItem === "function") {
      try { raw = originalGetItem.call(localStorage, logicalKey); } catch (e) {}
    }
    if (!raw) {
      try {
        var activeUser = localStorage.getItem("duru_active_user") || sessionStorage.getItem("duru_active_user");
        if (activeUser) {
          raw = localStorage.getItem("user_" + activeUser + "_" + logicalKey);
        }
      } catch (e) {}
    }
    if (!raw) {
      try {
        for (var i = 0; i < localStorage.length; i++) {
          var k = localStorage.key(i);
          if (k === logicalKey || (k && k.indexOf(logicalKey) !== -1)) {
            raw = localStorage.getItem(k);
            if (raw) break;
          }
        }
      } catch (e) {}
    }
    if (!raw) return null;
    try {
      return JSON.parse(raw);
    } catch (e) {
      return null;
    }
  }

  // ── Helper: load practice object ──────────────────────────
  function loadPracticeData(storageKey) {
    var data = safeReadJson(storageKey);
    if (!data) return null;
    return {
      xp:       data.xp       || 0,
      badges:   data.badges   || {},
      beste:    data.beste    || {},
      gedaan:   data.gedaan   || {},
      pogingen: data.pogingen || {},
      titels:   data.titels   || {}
    };
  }

  // ── Helper parsing functions ──────────────────────────────
  function loadDuruAttempts(attemptsList, key, vakId, vakTitel, vakKleur) {
    var data = safeReadJson(key);
    if (data && data.history && Array.isArray(data.history)) {
      data.history.forEach(function (att) {
        var ts = parseDuruDate(att.datum);
        var pct = att.pct !== undefined ? att.pct : Math.round((att.goed / att.totaal) * 100);

        var cijferVal = 1 + (pct / 100) * 9;
        cijferVal = Math.round(cijferVal * 10) / 10;

        var hf = window.DURU_HF ? window.DURU_HF.vanAttempt(att, vakId) : null;

        attemptsList.push({
          timestamp: ts,
          datumStr: att.datum || "",
          vakId: vakId,
          vakTitel: vakTitel,
          vakKleur: vakKleur,
          hoofdstuk: hf ? hf.nr : null,
          hoofdstukTitel: hf ? hf.titel : "Overige toetsen",
          hoofdstukIcoon: hf ? hf.icoon : "📦",
          examId: att.examId || "",
          titel: att.examTitel || att.titel || "Proeftoets",
          goed: att.goed !== undefined ? att.goed : 0,
          totaal: att.totaal !== undefined ? att.totaal : 20,
          pct: pct,
          cijfer: cijferVal,
          geslaagd: cijferVal >= 5.5
        });
      });
    }
  }

  function loadBegrijpendLezenAttempts(attemptsList, key) {
    var history = safeReadJson(key || "begrijpend_lezen_history");
    if (history && Array.isArray(history)) {
      history.forEach(function (att) {
        var ts = new Date(att.timestamp || new Date());
        var score = att.score !== undefined ? att.score : 0;
        var total = att.total !== undefined ? att.total : 10;
        var gradeVal = parseFloat(String(att.grade || "").replace(",", "."));

        if (isNaN(gradeVal)) {
          gradeVal = 1 + (score / total) * 9;
        }
        gradeVal = Math.round(gradeVal * 10) / 10;

        var pct = Math.round((score / total) * 100);

        attemptsList.push({
          timestamp: ts,
          datumStr: formatDisplayDate(ts),
          vakId: "nederlands-begrijpend",
          vakTitel: "Begrijpend Lezen",
          vakKleur: "oranje",
          hoofdstuk: 1,
          hoofdstukTitel: "Tekstanalyse & Begrip",
          hoofdstukIcoon: "🧠",
          examId: att.startingText || "",
          titel: att.startingText || "Tekstanalyse",
          goed: score,
          totaal: total,
          pct: pct,
          cijfer: gradeVal,
          geslaagd: gradeVal >= 5.5
        });
      });
    }
  }

  function parseDuruDate(dateStr) {
    if (!dateStr) return new Date();
    try {
      var parts = dateStr.split(" ");
      if (parts.length < 2) return new Date(dateStr);
      var dateParts = parts[0].split("-");
      var timeParts = parts[1].split(":");
      if (dateParts.length < 3 || timeParts.length < 2) return new Date(dateStr);
      return new Date(
        parseInt(dateParts[2], 10),
        parseInt(dateParts[1], 10) - 1,
        parseInt(dateParts[0], 10),
        parseInt(timeParts[0], 10),
        parseInt(timeParts[1], 10)
      );
    } catch (e) {
      return new Date(dateStr);
    }
  }

  function formatDisplayDate(dateObj) {
    try {
      var d = dateObj.getDate();
      var m = dateObj.getMonth() + 1;
      var y = dateObj.getFullYear();
      var h = dateObj.getHours();
      var min = dateObj.getMinutes();

      if (d < 10) d = "0" + d;
      if (m < 10) m = "0" + m;
      if (h < 10) h = "0" + h;
      if (min < 10) min = "0" + min;

      return d + "-" + m + "-" + y + " " + h + ":" + min;
    } catch (e) {
      return "";
    }
  }

  // ── Render per-subject cards (Grouped by Hoofdstuk in Details) ─
  function renderVakKaarten(attempts, vakkenVanJaar) {
    var grid = document.getElementById("vak-stats-grid");
    if (!grid) return;

    if (!vakkenVanJaar || vakkenVanJaar.length === 0) {
      grid.innerHTML = '<p class="vak-stats-leeg">Nog geen gegevens voor schooljaar ' +
        escHtml(window.currentJaar || "") +
        '. Zodra Duru begint, verschijnt het hier! 🚀</p>';
      return;
    }

    var vakken = vakkenVanJaar.map(function (v) {
      return {
        id: v.id,
        titel: v.titel,
        icoon: v.icoon,
        kleur: v.kleur,
        practiceKey: v.practiceKey,
        hasPractice: !!v.practiceKey
      };
    });

    var html = "";

    vakken.forEach(function (vak) {
      var vakAttempts = attempts.filter(function (a) { return a.vakId === vak.id; });
      var examCount = vakAttempts.length;

      var prac = vak.hasPractice ? loadPracticeData(vak.practiceKey) : null;
      var pogingen = prac ? (prac.pogingen || {}) : {};
      var titels   = prac ? (prac.titels   || {}) : {};
      var beste    = prac ? (prac.beste    || {}) : {};

      var totalPogingen = 0;
      Object.keys(pogingen).forEach(function (tid) {
        totalPogingen += (pogingen[tid] || 0);
      });

      var topicSet = {};
      Object.keys(pogingen).forEach(function (tid) { topicSet[tid] = true; });
      Object.keys(beste).forEach(function (tid) { topicSet[tid] = true; });
      var topicIds = Object.keys(topicSet);
      var topicCount = topicIds.length;

      var avgCijfer = 0;
      var hoogsteCijfer = 0;
      if (examCount > 0) {
        var sumC = 0;
        vakAttempts.forEach(function (a) {
          sumC += a.cijfer;
          if (a.cijfer > hoogsteCijfer) hoogsteCijfer = a.cijfer;
        });
        avgCijfer = sumC / examCount;
      }

      var avgStr     = examCount > 0 ? avgCijfer.toFixed(1).replace(".", ",")     : "-";
      var hoogsteStr = examCount > 0 ? hoogsteCijfer.toFixed(1).replace(".", ",") : "-";
      var isEmpty    = (examCount === 0) && (!vak.hasPractice || totalPogingen === 0);

      html += '<div class="vak-stat-card vak-stat-card--' + vak.kleur + '">';

      // Header row
      html += '<div class="vak-stat-card__header">';
      html +=   '<span class="vak-stat-card__icoon">' + vak.icoon + '</span>';
      html +=   '<span class="vak-stat-card__naam">' + vak.titel + '</span>';
      html += '</div>';

      if (isEmpty) {
        html += '<p class="vak-stat-card__leeg">Nog niets gedaan &mdash; start een oefening! 🚀</p>';
      } else {
        var cijferKlasse = "";
        if (examCount > 0) {
          cijferKlasse = avgCijfer >= 5.5 ? " vak-cijfer--geslaagd" : " vak-cijfer--gezakt";
        }
        html += '<div class="vak-stat-card__cijfer-rij">';
        html +=   '<span class="vak-cijfer' + cijferKlasse + '">' + avgStr + '</span>';
        if (examCount > 0) {
          html += '<span class="vak-stat-card__hoogste">Hoogste: ' + hoogsteStr + '</span>';
        }
        html += '</div>';

        html += '<ul class="vak-metrics">';
        html +=   '<li class="vak-metric"><span class="vak-metric__icoon">🧪</span>';
        html +=     '<span>' + examCount + ' proeftoets' + (examCount === 1 ? '' : 'en') + ' gemaakt</span></li>';
        if (vak.hasPractice) {
          html += '<li class="vak-metric"><span class="vak-metric__icoon">🔁</span>';
          html +=   '<span>' + totalPogingen + ' keer geoefend</span></li>';
          html += '<li class="vak-metric"><span class="vak-metric__icoon">📚</span>';
          html +=   '<span>' + topicCount + ' onderwerp' + (topicCount === 1 ? '' : 'en') + ' geoefend</span></li>';
        }
        html += '</ul>';

        html += '<button class="detail-toggle" type="button" aria-expanded="false">';
        html +=   'Hoofdstuk Details <span class="detail-toggle__arrow">▾</span>';
        html += '</button>';

        // Detail panel (grouped by chapter)
        html += '<div class="vak-detail">';

        // Get chapters known for this subject from the real manifest (DURU_HF)
        var chapterDefs = window.DURU_HF.lijst(vak.id);

        // Renders one chapter-group-block (works for real chapters and for the
        // "Overige toetsen/oefeningen" catch-all group)
        var renderChapterGroupBlock = function (titleHtml, chAttempts, chPracticeTopics) {
          var block = "";

          if (chAttempts.length === 0 && chPracticeTopics.length === 0) {
            block += '<div class="chapter-group-block" style="opacity:0.8;">';
            block +=   '<div class="chapter-group-header">';
            block +=     '<div class="chapter-group-title">' + titleHtml + '</div>';
            block +=     '<div class="chapter-group-score" style="color:var(--grijs-licht);font-weight:normal;font-size:12px;">⏳ Nog geen proeftoets gemaakt</div>';
            block +=   '</div>';
            block += '</div>';
            return block;
          }

          var chSum = 0;
          var chMax = 0;
          chAttempts.forEach(function (a) {
            chSum += a.cijfer;
            if (a.cijfer > chMax) chMax = a.cijfer;
          });
          var chAvg = chAttempts.length > 0 ? (chSum / chAttempts.length) : 0;
          var chAvgStr = chAttempts.length > 0 ? chAvg.toFixed(1).replace(".", ",") : "—";
          var chBadgeCls = chAvg >= 5.5 ? "pass" : "fail";

          block += '<div class="chapter-group-block">';
          block +=   '<div class="chapter-group-header">';
          block +=     '<div class="chapter-group-title">' + titleHtml + '</div>';
          if (chAttempts.length > 0) {
            block +=   '<div class="chapter-group-score"><span class="badge-grade ' + chBadgeCls + '">Gem. ' + chAvgStr + '</span> (' + chAttempts.length + ' toetsen)</div>';
          }
          block +=   '</div>';

          // Proeftoetsen table
          if (chAttempts.length > 0) {
            block += '<table class="vak-detail-table">';
            block +=   '<thead><tr><th>Toets</th><th>Keer</th><th>Beste</th><th>Laatste</th><th>Datum</th></tr></thead>';
            block +=   '<tbody>';

            var examGroups = {};
            chAttempts.forEach(function (a) {
              var gKey = (a.examId && a.examId !== "") ? a.examId : a.titel;
              if (!examGroups[gKey]) {
                examGroups[gKey] = { titel: a.titel, attempts: [] };
              }
              examGroups[gKey].attempts.push(a);
            });

            Object.keys(examGroups).forEach(function (gKey) {
              var grp = examGroups[gKey];
              var atts = grp.attempts;
              atts.sort(function (a, b) { return a.timestamp - b.timestamp; });

              var bst = 0;
              atts.forEach(function (a) { if (a.cijfer > bst) bst = a.cijfer; });
              var last = atts[atts.length - 1];
              var lastKlasse = last.cijfer >= 5.5 ? "pass" : "fail";
              var bstKlasse  = bst >= 5.5 ? "pass" : "fail";
              var lastDate   = (last.datumStr || "").split(" ")[0];

              block += '<tr>';
              block +=   '<td><strong>' + escHtml(grp.titel) + '</strong></td>';
              block +=   '<td>&times;' + atts.length + '</td>';
              block +=   '<td><span class="badge-grade ' + bstKlasse + '">' + bst.toFixed(1).replace(".", ",") + '</span></td>';
              block +=   '<td><span class="badge-grade ' + lastKlasse + '">' + last.cijfer.toFixed(1).replace(".", ",") + '</span></td>';
              block +=   '<td style="font-size:12px;color:var(--grijs);">' + escHtml(lastDate) + '</td>';
              block += '</tr>';
            });

            block +=   '</tbody></table>';
          }

          // Practice topics table
          if (chPracticeTopics.length > 0) {
            block += '<div style="font-size:12px; font-weight:700; color:var(--grijs); margin:8px 0 4px;">🔁 Oefeningen:</div>';
            block += '<table class="vak-detail-table">';
            block +=   '<tbody>';
            chPracticeTopics.forEach(function (tid) {
              var tTitle = titels[tid] || tid;
              var pCount = pogingen[tid] || 0;
              var bScore = beste[tid] != null ? Math.round(beste[tid]) : null;

              block += '<tr>';
              block +=   '<td>' + escHtml(tTitle) + '</td>';
              block +=   '<td>&times;' + pCount + '</td>';
              block +=   '<td>' + (bScore != null ? '<span class="vak-score-badge">' + bScore + '%</span>' : '-') + '</td>';
              block += '</tr>';
            });
            block +=   '</tbody></table>';
          }

          block += '</div>'; // .chapter-group-block
          return block;
        };

        if (chapterDefs.length === 0) {
          html += '<p class="vak-detail__leeg">De hoofdstukken volgen zodra het lesmateriaal er is.</p>';
        } else {
          chapterDefs.forEach(function (chDef) {
            var chAttempts = vakAttempts.filter(function (a) { return a.hoofdstuk === chDef.nr; });
            var chPracticeTopics = topicIds.filter(function (tid) {
              return window.DURU_HF.vanOnderwerp(vak.id, tid) === chDef.nr;
            });
            var titleHtml = '<span>' + (chDef.icoon || "📖") + '</span><span>Hoofdstuk ' + chDef.nr + ': ' + escHtml(chDef.titel) + '</span>';
            html += renderChapterGroupBlock(titleHtml, chAttempts, chPracticeTopics);
          });
        }

        // Overige toetsen/oefeningen: attempts/onderwerpen die niet bij een getoond hoofdstuk horen
        var chapterNrs = {};
        chapterDefs.forEach(function (c) { chapterNrs[c.nr] = true; });
        var overigeAttempts = vakAttempts.filter(function (a) {
          return a.hoofdstuk == null || !chapterNrs[a.hoofdstuk];
        });
        var overigeTopics = topicIds.filter(function (tid) {
          var nr = window.DURU_HF.vanOnderwerp(vak.id, tid);
          return nr == null || !chapterNrs[nr];
        });
        if (overigeAttempts.length > 0 || overigeTopics.length > 0) {
          html += renderChapterGroupBlock('<span>📦</span><span>Overige toetsen</span>', overigeAttempts, overigeTopics);
        }

        html += '</div>'; // .vak-detail
      }

      html += '</div>'; // .vak-stat-card
    });

    grid.innerHTML = html;
  }

  // ── Render Dedicated Hoofdstuk Performance Matrix ─────────
  function renderHoofdstukStats(attempts, vakkenVanJaar) {
    var grid = document.getElementById("hoofdstuk-stats-grid");
    var filterBar = document.getElementById("hoofdstuk-filter-bar");
    if (!grid) return;

    var filterVak = window.currentHoofdstukFilter || "all";

    // 1. Build Filter Buttons
    if (filterBar) {
      var filterHtml = '<button class="filter-btn ' + (filterVak === "all" ? "active" : "") + '" data-hfilter="all" type="button">Alle Vakken</button>';
      (vakkenVanJaar || []).forEach(function (v) {
        var isActive = filterVak === v.id ? "active" : "";
        filterHtml += '<button class="filter-btn ' + isActive + '" data-hfilter="' + escHtml(v.id) + '" type="button">' + v.icoon + ' ' + escHtml(v.titel) + '</button>';
      });
      filterBar.innerHTML = filterHtml;

      var btns = filterBar.querySelectorAll(".filter-btn");
      btns.forEach(function (btn) {
        btn.addEventListener("click", function () {
          btns.forEach(function (b) { b.classList.remove("active"); });
          btn.classList.add("active");
          window.currentHoofdstukFilter = btn.getAttribute("data-hfilter");
          renderHoofdstukStats(window.allAttempts, vakkenVanJaar);
        });
      });
    }

    // 2. Aggregate all chapters
    var targetVakken = vakkenVanJaar;
    if (filterVak !== "all") {
      targetVakken = vakkenVanJaar.filter(function (v) { return v.id === filterVak; });
    }

    var chapterCardsHtml = "";

    targetVakken.forEach(function (vak) {
      var chapterDefs = window.DURU_HF.lijst(vak.id);

      var prac = vak.practiceKey ? loadPracticeData(vak.practiceKey) : null;
      var pogingenMap = prac ? (prac.pogingen || {}) : {};
      var geoefendeTopicIds = Object.keys(pogingenMap).filter(function (tid) {
        return (pogingenMap[tid] || 0) > 0;
      });

      if (chapterDefs.length === 0) {
        chapterCardsHtml += '<div class="hoofdstuk-card hoofdstuk-card--' + vak.kleur + '" style="opacity:0.75;">';
        chapterCardsHtml +=   '<div class="hoofdstuk-card__header"><div>';
        chapterCardsHtml +=     '<span class="hoofdstuk-card__badge">' + vak.icoon + ' ' + escHtml(vak.titel) + '</span>';
        chapterCardsHtml +=     '<div class="hoofdstuk-card__titel">De hoofdstukken volgen zodra het lesmateriaal er is.</div>';
        chapterCardsHtml +=   '</div></div>';
        chapterCardsHtml += '</div>';
        // geen return: de "Overige toetsen"-kaart hieronder laat losse resultaten
        // van dit vak alsnog zien (chapterDefs is leeg, dus de lus doet niets).
      }

      var chapterNrs = {};

      chapterDefs.forEach(function (chDef) {
        chapterNrs[chDef.nr] = true;

        var chAttempts = attempts.filter(function (a) {
          return a.vakId === vak.id && a.hoofdstuk === chDef.nr;
        });

        var examCount = chAttempts.length;
        var sumC = 0;
        var maxC = 0;
        var lastC = 0;
        var lastDatum = "-";

        if (examCount > 0) {
          chAttempts.forEach(function (a) {
            sumC += a.cijfer;
            if (a.cijfer > maxC) maxC = a.cijfer;
          });
          lastC = chAttempts[0].cijfer;
          lastDatum = (chAttempts[0].datumStr || "-").split(" ")[0];
        }

        var avgC = examCount > 0 ? (sumC / examCount) : 0;
        var avgStr = examCount > 0 ? avgC.toFixed(1).replace(".", ",") : "—";
        var maxStr = examCount > 0 ? maxC.toFixed(1).replace(".", ",") : "—";
        var lastStr = examCount > 0 ? lastC.toFixed(1).replace(".", ",") : "—";

        // Performance status classification
        var statusLabel = "Nog niet gestart";
        var statusCls   = "status-empty";
        var statusIcon  = "⏳";
        var advice      = "Begin met de theorie en start proeftoets 1!";

        if (examCount > 0) {
          if (avgC >= 8.5) {
            statusLabel = "Uitmuntend";
            statusCls   = "status-mastered";
            statusIcon  = "🌟";
            advice      = "Geweldig! Je beheerst dit hoofdstuk volledig.";
          } else if (avgC >= 7.0) {
            statusLabel = "Goed";
            statusCls   = "status-good";
            statusIcon  = "👍";
            advice      = "Heel goed! Nog 1 oefentoets voor de perfecte score.";
          } else if (avgC >= 5.5) {
            statusLabel = "Voldoende";
            statusCls   = "status-pass";
            statusIcon  = "✔️";
            advice      = "Voldoende! Oefen de fouten nog even door.";
          } else {
            statusLabel = "Aandachtspunt";
            statusCls   = "status-review";
            statusIcon  = "⚠️";
            advice      = "Herhaal de theorie en maak een herkansing.";
          }
        }

        // Toetsvoortgang: unieke proeftoetsen t.o.v. het echte aantal uit het manifest
        var examIdSet = {};
        chAttempts.forEach(function (a) {
          var k = (a.examId && a.examId !== "") ? a.examId : a.titel;
          examIdSet[k] = true;
        });
        var uniekeExamens = Object.keys(examIdSet).length;
        var examTotaal = window.DURU_HF.totaalExamens(vak.id, chDef.nr);
        var examVoortgangPct = examTotaal > 0 ? Math.min(100, Math.round((uniekeExamens / examTotaal) * 100)) : 0;

        // Oefenvoortgang: aantal onderwerpen met >=1 poging t.o.v. het manifest-totaal
        var oefTotaal = window.DURU_HF.totaalOnderwerpen(vak.id, chDef.nr);
        var oefGedaan = geoefendeTopicIds.filter(function (tid) {
          return window.DURU_HF.vanOnderwerp(vak.id, tid) === chDef.nr;
        }).length;
        var oefVoortgangPct = oefTotaal > 0 ? Math.min(100, Math.round((oefGedaan / oefTotaal) * 100)) : 0;

        chapterCardsHtml += '<div class="hoofdstuk-card hoofdstuk-card--' + vak.kleur + '">';
        chapterCardsHtml +=   '<div class="hoofdstuk-card__header">';
        chapterCardsHtml +=     '<div>';
        chapterCardsHtml +=       '<span class="hoofdstuk-card__badge">' + vak.icoon + ' ' + escHtml(vak.titel) + ' · H' + chDef.nr + '</span>';
        chapterCardsHtml +=       '<div class="hoofdstuk-card__titel">' + (chDef.icoon || "📖") + ' ' + escHtml(chDef.titel) + '</div>';
        if (chDef.intro) {
          chapterCardsHtml +=     '<div style="font-size:12px;color:var(--grijs);margin-top:2px;">' + escHtml(chDef.intro) + '</div>';
        }
        chapterCardsHtml +=     '</div>';
        chapterCardsHtml +=   '</div>';

        chapterCardsHtml +=   '<div class="hoofdstuk-card__grade-row">';
        chapterCardsHtml +=     '<div>';
        chapterCardsHtml +=       '<div class="hoofdstuk-card__grade" style="color:' + (avgC >= 5.5 ? 'var(--groen)' : (examCount > 0 ? 'var(--oranje)' : 'var(--grijs-licht)')) + ';">' + avgStr + '</div>';
        chapterCardsHtml +=       '<div style="font-size:11px;color:var(--grijs-licht);">Hoofdstuk Gemiddelde</div>';
        chapterCardsHtml +=     '</div>';
        chapterCardsHtml +=     '<span class="hoofdstuk-card__status ' + statusCls + '">';
        chapterCardsHtml +=       '<span>' + statusIcon + '</span> ' + statusLabel;
        chapterCardsHtml +=     '</span>';
        chapterCardsHtml +=   '</div>';

        // Proeftoetsen-voortgang
        chapterCardsHtml += '<div>';
        chapterCardsHtml +=   '<div style="display:flex;justify-content:space-between;font-size:11px;color:var(--grijs);margin-bottom:4px;">';
        chapterCardsHtml +=     '<span>Proeftoetsen</span>';
        chapterCardsHtml +=     '<span>' + (examTotaal > 0 ? (uniekeExamens + '/' + examTotaal + ' (' + examVoortgangPct + '%)') : (examCount + ' gemaakt')) + '</span>';
        chapterCardsHtml +=   '</div>';
        if (examTotaal > 0) {
          chapterCardsHtml += '<div class="hoofdstuk-progress-bar">';
          chapterCardsHtml +=   '<div class="hoofdstuk-progress-fill" style="width:' + examVoortgangPct + '%; background:' + (avgC >= 5.5 ? 'var(--hub-zacht)' : 'var(--oranje)') + ';"></div>';
          chapterCardsHtml += '</div>';
        }
        chapterCardsHtml += '</div>';

        // Oefenvoortgang (alleen tonen als het vak onderwerpen heeft voor dit hoofdstuk)
        if (oefTotaal > 0) {
          chapterCardsHtml += '<div style="margin-top:8px;">';
          chapterCardsHtml +=   '<div style="display:flex;justify-content:space-between;font-size:11px;color:var(--grijs);margin-bottom:4px;">';
          chapterCardsHtml +=     '<span>Geoefende onderwerpen</span>';
          chapterCardsHtml +=     '<span>' + oefGedaan + '/' + oefTotaal + ' (' + oefVoortgangPct + '%)</span>';
          chapterCardsHtml +=   '</div>';
          chapterCardsHtml +=   '<div class="hoofdstuk-progress-bar hoofdstuk-progress-bar--oefen">';
          chapterCardsHtml +=     '<div class="hoofdstuk-progress-fill hoofdstuk-progress-fill--oefen" style="width:' + oefVoortgangPct + '%;"></div>';
          chapterCardsHtml +=   '</div>';
          chapterCardsHtml += '</div>';
        }

        chapterCardsHtml +=   '<div class="hoofdstuk-card__metrics">';
        chapterCardsHtml +=     '<span>🏆 Hoogste: <strong>' + maxStr + '</strong></span>';
        chapterCardsHtml +=     '<span>⏱️ Laatste: <strong>' + lastStr + '</strong></span>';
        chapterCardsHtml +=     '<span>📅 Datum: ' + escHtml(lastDatum) + '</span>';
        chapterCardsHtml +=   '</div>';

        chapterCardsHtml +=   '<div class="hoofdstuk-card__footer">';
        chapterCardsHtml +=     '<span style="font-style:italic;">💡 ' + advice + '</span>';
        chapterCardsHtml +=   '</div>';
        chapterCardsHtml += '</div>';
      });

      // 📦 Overige toetsen: pogingen die niet bij een getoond hoofdstuk horen
      var overigeAttempts = attempts.filter(function (a) {
        return a.vakId === vak.id && (a.hoofdstuk == null || !chapterNrs[a.hoofdstuk]);
      });

      if (overigeAttempts.length > 0) {
        var ovSum = 0;
        var ovMax = 0;
        overigeAttempts.forEach(function (a) {
          ovSum += a.cijfer;
          if (a.cijfer > ovMax) ovMax = a.cijfer;
        });
        var ovAvg = ovSum / overigeAttempts.length;
        var ovLast = overigeAttempts[0].cijfer;
        var ovLastDatum = (overigeAttempts[0].datumStr || "-").split(" ")[0];
        var ovAvgStr = ovAvg.toFixed(1).replace(".", ",");
        var ovMaxStr = ovMax.toFixed(1).replace(".", ",");
        var ovLastStr = ovLast.toFixed(1).replace(".", ",");

        chapterCardsHtml += '<div class="hoofdstuk-card hoofdstuk-card--' + vak.kleur + '">';
        chapterCardsHtml +=   '<div class="hoofdstuk-card__header"><div>';
        chapterCardsHtml +=     '<span class="hoofdstuk-card__badge">' + vak.icoon + ' ' + escHtml(vak.titel) + ' · 📦</span>';
        chapterCardsHtml +=     '<div class="hoofdstuk-card__titel">📦 Overige toetsen</div>';
        chapterCardsHtml +=   '</div></div>';
        chapterCardsHtml +=   '<div class="hoofdstuk-card__grade-row">';
        chapterCardsHtml +=     '<div>';
        chapterCardsHtml +=       '<div class="hoofdstuk-card__grade" style="color:' + (ovAvg >= 5.5 ? 'var(--groen)' : 'var(--oranje)') + ';">' + ovAvgStr + '</div>';
        chapterCardsHtml +=       '<div style="font-size:11px;color:var(--grijs-licht);">Gemiddelde</div>';
        chapterCardsHtml +=     '</div>';
        chapterCardsHtml +=   '</div>';
        chapterCardsHtml +=   '<div class="hoofdstuk-card__metrics">';
        chapterCardsHtml +=     '<span>🏆 Hoogste: <strong>' + ovMaxStr + '</strong></span>';
        chapterCardsHtml +=     '<span>⏱️ Laatste: <strong>' + ovLastStr + '</strong></span>';
        chapterCardsHtml +=     '<span>📅 Datum: ' + escHtml(ovLastDatum) + '</span>';
        chapterCardsHtml +=   '</div>';
        chapterCardsHtml += '</div>';
      }
    });

    if (!chapterCardsHtml) {
      grid.innerHTML = '<p style="text-align:center;color:var(--grijs-licht);padding:24px;">Geen hoofdstukken gevonden voor dit filter.</p>';
    } else {
      grid.innerHTML = chapterCardsHtml;
    }
  }

  // ── Simple HTML escaping helper ───────────────────────────
  function escHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  // ── Render SVG Line Chart ─────────────────────────────────
  function renderScoreTimeline(attempts) {
    var container = document.getElementById("line-chart-container");
    if (!container) return;

    if (attempts.length === 0) {
      container.innerHTML = '<div style="display:flex; align-items:center; justify-content:center; height:100%; color:var(--grijs-licht); font-family:var(--font-tekst); font-size:14px; text-align:center;">' +
                              'Nog geen gemaakte toetsen.<br>Start met een oefentoets om je voortgang te zien! 🚀' +
                            '</div>';
      return;
    }

    var chartAttempts = attempts.slice().reverse();
    if (chartAttempts.length > 15) {
      chartAttempts = chartAttempts.slice(chartAttempts.length - 15);
    }

    var w = container.clientWidth || 530;
    var h = 240;
    var top = 20;
    var right = 20;
    var bottom = 40;
    var left = 30;

    var chartW = w - left - right;
    var chartH = h - top - bottom;

    function getY(grade) {
      return top + chartH - ((grade - 1) / 9) * chartH;
    }

    function getX(index) {
      if (chartAttempts.length <= 1) {
        return left + chartW / 2;
      }
      return left + (index / (chartAttempts.length - 1)) * chartW;
    }

    var svg = '<svg width="100%" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '" style="overflow:visible;">';

    svg += '<defs>';
    svg += '  <linearGradient id="chartFillGradient" x1="0" y1="0" x2="0" y2="1">';
    svg += '    <stop offset="0%" stop-color="var(--hub-hoofd)" stop-opacity="0.25"/>';
    svg += '    <stop offset="100%" stop-color="var(--hub-hoofd)" stop-opacity="0"/>';
    svg += '  </linearGradient>';
    svg += '</defs>';

    var gridGrades = [1, 3, 5.5, 8, 10];
    gridGrades.forEach(function (g) {
      var y = getY(g);
      var isPass = g === 5.5;
      var strokeStyle = isPass ? 'stroke="var(--groen)" stroke-dasharray="4,4" stroke-opacity="0.7"' : 'stroke="var(--lijn)" stroke-opacity="0.5"';

      svg += '  <line x1="' + left + '" y1="' + y + '" x2="' + (w - right) + '" y2="' + y + '" ' + strokeStyle + ' stroke-width="1" />';

      var textStyle = isPass ? 'fill="var(--groen)" font-weight="bold"' : 'fill="var(--grijs-licht)"';
      svg += '  <text x="' + (left - 8) + '" y="' + (y + 4) + '" text-anchor="end" class="svg-chart-text" ' + textStyle + '>' + g.toString().replace(".", ",") + '</text>';
    });

    var pathPoints = [];
    var fillPoints = ["M", getX(0), getY(1)];

    chartAttempts.forEach(function (att, index) {
      var x = getX(index);
      var y = getY(att.cijfer);
      pathPoints.push((index === 0 ? "M" : "L") + " " + x + " " + y);
      fillPoints.push("L " + x + " " + y);
    });

    fillPoints.push("L " + getX(chartAttempts.length - 1) + " " + getY(1));
    fillPoints.push("Z");

    svg += '  <path d="' + fillPoints.join(" ") + '" fill="url(#chartFillGradient)" />';

    if (chartAttempts.length > 1) {
      svg += '  <path d="' + pathPoints.join(" ") + '" fill="none" stroke="var(--hub-hoofd)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />';
    }

    chartAttempts.forEach(function (att, index) {
      var x = getX(index);
      var y = getY(att.cijfer);

      var colorHex = "var(--hub-hoofd)";
      if (att.vakKleur === "blauw") colorHex = "var(--blauw)";
      if (att.vakKleur === "teal") colorHex = "var(--teal)";
      if (att.vakKleur === "groen") colorHex = "var(--groen)";
      if (att.vakKleur === "oranje") colorHex = "var(--oranje)";

      svg += '  <circle cx="' + x + '" cy="' + y + '" r="5" class="svg-chart-dot" stroke="' + colorHex + '" ' +
                    'data-index="' + index + '" ' +
                    'data-vak="' + att.vakTitel + '" ' +
                    'data-titel="' + att.titel + '" ' +
                    'data-cijfer="' + att.cijfer.toFixed(1).replace(".", ",") + '" ' +
                    'data-datum="' + att.datumStr + '" />';
    });

    if (chartAttempts.length > 0) {
      var labelIndices = [];
      if (chartAttempts.length === 1) {
        labelIndices = [0];
      } else if (chartAttempts.length < 5) {
        for (var i = 0; i < chartAttempts.length; i++) labelIndices.push(i);
      } else {
        labelIndices = [0, Math.floor(chartAttempts.length / 2), chartAttempts.length - 1];
      }

      labelIndices.forEach(function (idx) {
        var x = getX(idx);
        var att = chartAttempts[idx];
        var dateOnly = (att.datumStr || "").split(" ")[0] || "";
        svg += '  <text x="' + x + '" y="' + (h - 12) + '" text-anchor="middle" class="svg-chart-text" fill="var(--grijs-licht)">' + dateOnly + '</text>';
      });
    }

    svg += "</svg>";
    container.innerHTML = svg;

    setupChartTooltips(container);
  }

  // ── Setup HTML tooltips for dots ──────────────────────────
  function setupChartTooltips(container) {
    var tooltip = document.getElementById("chart-tooltip");
    if (!tooltip) {
      tooltip = document.createElement("div");
      tooltip.id = "chart-tooltip";
      tooltip.style.position = "absolute";
      tooltip.style.background = "rgba(30, 41, 33, 0.95)";
      tooltip.style.color = "#fff";
      tooltip.style.padding = "8px 12px";
      tooltip.style.borderRadius = "8px";
      tooltip.style.fontSize = "12px";
      tooltip.style.fontFamily = "var(--font-tekst)";
      tooltip.style.pointerEvents = "none";
      tooltip.style.boxShadow = "0 4px 12px rgba(0,0,0,0.15)";
      tooltip.style.zIndex = "9999";
      tooltip.style.display = "none";
      tooltip.style.transition = "opacity 0.1s ease";
      tooltip.style.border = "1px solid rgba(255, 255, 255, 0.1)";
      tooltip.style.lineHeight = "1.4";
      document.body.appendChild(tooltip);
    }

    var dots = container.querySelectorAll(".svg-chart-dot");
    dots.forEach(function (dot) {
      dot.addEventListener("mouseenter", function (e) {
        var vak    = dot.getAttribute("data-vak");
        var titel  = dot.getAttribute("data-titel");
        var cijfer = dot.getAttribute("data-cijfer");
        var datum  = dot.getAttribute("data-datum");

        tooltip.innerHTML = "<strong>" + vak + "</strong>: " + titel + "<br>" +
                            "🎯 Cijfer: <strong>" + cijfer + "</strong><br>" +
                            "<span style='color:#b2c2b7; font-size:11px;'>📅 " + datum + "</span>";

        tooltip.style.display = "block";
        tooltip.style.opacity = "1";

        positionTooltip(e, tooltip);
      });

      dot.addEventListener("mousemove", function (e) {
        positionTooltip(e, tooltip);
      });

      dot.addEventListener("mouseleave", function () {
        tooltip.style.display = "none";
        tooltip.style.opacity = "0";
      });
    });
  }

  function positionTooltip(e, tooltip) {
    var tooltipWidth  = tooltip.offsetWidth;
    var tooltipHeight = tooltip.offsetHeight;

    var posX = e.pageX - tooltipWidth / 2;
    var posY = e.pageY - tooltipHeight - 14;

    if (posX < 10) posX = 10;
    if (posX + tooltipWidth > window.innerWidth - 10) posX = window.innerWidth - tooltipWidth - 10;

    tooltip.style.left = posX + "px";
    tooltip.style.top  = posY + "px";
  }

  // ── Render Exam Log Table (with Hoofdstuk column & search) ─
  function renderAttemptsTable() {
    var tbody = document.getElementById("exam-attempts-tbody");
    if (!tbody) return;

    var attempts = window.allAttempts || [];

    var filtered = attempts.filter(function (att) {
      if (window.currentTableFilter !== "all") {
        if (att.vakId !== window.currentTableFilter) {
          return false;
        }
      }

      if (window.currentTableSearch) {
        var query = window.currentTableSearch.toLowerCase();
        var matchTitle = (att.titel || "").toLowerCase().indexOf(query) !== -1;
        var matchVak   = (att.vakTitel || "").toLowerCase().indexOf(query) !== -1;
        var matchHf    = ("hoofdstuk " + (att.hoofdstuk || "")).toLowerCase().indexOf(query) !== -1 ||
                         ("h" + (att.hoofdstuk || "")).toLowerCase().indexOf(query) !== -1 ||
                         (att.hoofdstukTitel || "").toLowerCase().indexOf(query) !== -1;
        if (!matchTitle && !matchVak && !matchHf) {
          return false;
        }
      }

      return true;
    });

    if (filtered.length === 0) {
      tbody.innerHTML = '<tr>' +
                          '<td colspan="6" style="text-align:center; padding:32px; color:var(--grijs-licht);">' +
                            'Geen gemaakte toetsen gevonden met de geselecteerde filters.' +
                          '</td>' +
                        '</tr>';
      return;
    }

    var html = "";
    filtered.forEach(function (att) {
      var gradeClass     = att.geslaagd ? "pass" : "fail";
      var formattedGrade = att.cijfer.toFixed(1).replace(".", ",");
      var hfBadge = '<span class="chapter-badge" title="' + escHtml(att.hoofdstukTitel || "") + '">' + (att.hoofdstukIcoon || "📖") + ' ' + (att.hoofdstuk != null ? ('H' + att.hoofdstuk) : 'Overig') + '</span>';

      html += '<tr>' +
                '<td>' + att.datumStr + '</td>' +
                '<td><span class="subject-badge ' + att.vakKleur + '">' + att.vakTitel + '</span></td>' +
                '<td>' + hfBadge + '</td>' +
                '<td><strong>' + escHtml(att.titel) + '</strong></td>' +
                '<td>' + att.goed + ' / ' + att.totaal + ' <span style="color:var(--grijs-licht); font-size:12px;">(' + att.pct + '%)</span></td>' +
                '<td><span class="badge-grade ' + gradeClass + '">' + formattedGrade + '</span></td>' +
              '</tr>';
    });

    tbody.innerHTML = html;
  }

  // ── Render Filter Bar ─────────────────────────────────────
  function renderFilterBar(vakkenVanJaar) {
    var bar = document.getElementById("table-filter-bar");
    if (!bar) return;

    window.currentTableFilter = "all";

    var html = '<button class="filter-btn active" data-filter="all" type="button">Alles</button>';
    (vakkenVanJaar || []).forEach(function (vak) {
      html += '<button class="filter-btn" data-filter="' + escHtml(vak.id) + '" type="button">' + vak.icoon + ' ' + escHtml(vak.titel) + '</button>';
    });
    bar.innerHTML = html;

    bindFilterButtons();
  }

  function bindFilterButtons() {
    var filterButtons = document.querySelectorAll("#table-filter-bar .filter-btn");
    filterButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterButtons.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");

        window.currentTableFilter = btn.getAttribute("data-filter");
        renderAttemptsTable();
      });
    });
  }

  function initFiltersAndSearch() {
    var searchInput = document.getElementById("exam-search");
    if (searchInput) {
      searchInput.addEventListener("input", function () {
        window.currentTableSearch = searchInput.value;
        renderAttemptsTable();
      });
    }
  }

  // ── Backup & Restore Logic ──────────────────────────────
  function initBackupRestore() {
    var exportBtn = document.getElementById("backup-export-btn");
    var importBtn = document.getElementById("backup-import-btn");
    var fileInput = document.getElementById("backup-file-input");

    if (exportBtn) {
      exportBtn.addEventListener("click", function () {
        var backup = [];
        var seenKeys = {};
        for (var i = 0; i < localStorage.length; i++) {
          var rawKey = localStorage.key(i);
          if (!rawKey) continue;
          var logicalKey = rawKey;
          if (rawKey.indexOf("user_") === 0) {
            var parts = rawKey.split("_");
            if (parts.length >= 3) {
              logicalKey = parts.slice(2).join("_");
            }
          }
          if (logicalKey && (logicalKey.indexOf("duru_") === 0 || logicalKey.indexOf("begrijpend_lezen_") === 0)) {
            if (logicalKey === "duru_active_user" || logicalKey === "duru_users" || logicalKey === "duru_backup_imported" || logicalKey === "duru_encrypted_backup") {
              continue;
            }
            if (seenKeys[logicalKey]) continue;
            seenKeys[logicalKey] = true;

            var value = localStorage.getItem(logicalKey);
            if (value) {
              try {
                backup.push({
                  key: logicalKey,
                  val: JSON.parse(value)
                });
              } catch (e) {
                backup.push({
                  key: logicalKey,
                  val: value
                });
              }
            }
          }
        }

        if (backup.length === 0) {
          alert("Er is geen voortgang gevonden om te exporteren.");
          return;
        }

        var blob = new Blob([JSON.stringify(backup, null, 2)], { type: "application/json" });
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = "duru_okul_voortgang_" + new Date().toISOString().split('T')[0] + ".json";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      });
    }

    if (importBtn && fileInput) {
      importBtn.addEventListener("click", function () {
        fileInput.click();
      });

      fileInput.addEventListener("change", function (e) {
        var file = e.target.files[0];
        if (!file) return;

        var reader = new FileReader();
        reader.onload = function (evt) {
          try {
            var data = JSON.parse(evt.target.result);
            if (!Array.isArray(data)) {
              throw new Error("Ongeldig bestandsformaat. Verwacht een lijst met gegevens.");
            }

            var importedCount = 0;
            data.forEach(function (item) {
              if (item && item.key) {
                var valueStr = typeof item.val === "object" ? JSON.stringify(item.val) : String(item.val);
                localStorage.setItem(item.key, valueStr);
                importedCount++;
              }
            });

            if (importedCount > 0) {
              localStorage.setItem("duru_backup_imported", "true");
              alert("Succesvol " + importedCount + " onderdelen geïmporteerd! De pagina wordt nu herladen.");
              window.location.reload();
            } else {
              alert("Geen geldige gegevens gevonden in het bestand.");
            }
          } catch (err) {
            alert("Fout bij het laden van het bestand: " + err.message);
          }
        };
        reader.readAsText(file);
      });
    }
  }

})();
