/* =========================================================
   Duru's Schoolhub — Statistics & Dashboard Panel
   Handles: parsing localStorage, calculating statistics,
            dynamic responsive SVG rendering, and table
            filtering/searching.
   ========================================================= */

(function () {
  "use strict";

  // Global state for filtering
  window.allAttempts = [];
  window.currentTableFilter = "all";
  window.currentTableSearch = "";

  // ── Initialization on DOM Ready ──────────────────────────
  document.addEventListener("DOMContentLoaded", function () {
    initTabs();
    initFiltersAndSearch();
    initVakKaartenToggle();
    loadDashboardData();

    // Listen for storage events (e.g. if student completes quiz in an iframe)
    window.addEventListener("storage", function (e) {
      if (e.key && (e.key.indexOf("duru_") === 0 || e.key.indexOf("begrijpend_lezen_") === 0)) {
        loadDashboardData();
      }
    });

    // Handle window resize to redraw SVG chart responsively
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
        // Toggle active class on tabs
        tabs.forEach(function (t) { t.classList.remove("active"); });
        tab.classList.add("active");

        // Toggle active class on views
        var views = document.querySelectorAll(".hub-view");
        views.forEach(function (v) { v.classList.remove("active"); });

        var targetId = tab.getAttribute("data-target");
        var targetView = document.getElementById(targetId);
        if (targetView) {
          targetView.classList.add("active");
        }

        // Draw / refresh charts if moving to statistics tab
        if (targetId === "statistieken-view") {
          loadDashboardData();
        }
      });
    });
  }

  // ── Delegated toggle listener for per-subject detail panels ──
  function initVakKaartenToggle() {
    var grid = document.getElementById("vak-stats-grid");
    if (!grid) return;

    grid.addEventListener("click", function (e) {
      // Walk up from the click target to find a .detail-toggle button
      var btn = e.target;
      while (btn && btn !== grid) {
        if (btn.classList && btn.classList.contains("detail-toggle")) {
          var card = btn.closest ? btn.closest(".vak-stat-card") : null;
          if (!card) {
            // fallback for older browsers: traverse parentNode
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

  // ── Load & Parse Data ─────────────────────────────────────
  function loadDashboardData() {
    // 1. Calculate Practice XP and Badges
    var practiceKeys = [
      { key: "duru_nask_v1" },
      { key: "duru_wiskunde_v1" },
      { key: "duru_economi_v1" },
      { key: "duru_nederlands_spelling_v1" }
    ];

    var totalXP = 0;
    var totalBadges = 0;

    practiceKeys.forEach(function (sub) {
      try {
        var data = JSON.parse(localStorage.getItem(sub.key));
        if (data) {
          if (data.xp) totalXP += data.xp;
          if (data.badges) {
            // Badges is either object or array
            if (Array.isArray(data.badges)) {
              totalBadges += data.badges.length;
            } else {
              totalBadges += Object.keys(data.badges).length;
            }
          }
        }
      } catch (e) {
        console.warn("Could not parse key: " + sub.key, e);
      }
    });

    // Populate Overview Card Values
    var xpEl = document.getElementById("stat-xp");
    var badgesEl = document.getElementById("stat-badges");
    if (xpEl) xpEl.textContent = totalXP;
    if (badgesEl) badgesEl.textContent = totalBadges;

    // 2. Aggregate exam attempts from all subjects
    var attempts = [];

    // NASK
    loadDuruAttempts(attempts, "duru_nask_examens_v1", "natuurkunde", "Natuurkunde", "blauw");
    // Wiskunde
    loadDuruAttempts(attempts, "duru_wiskunde_examens_v1", "wiskunde", "Wiskunde", "teal");
    // Economie
    loadDuruAttempts(attempts, "duru_economi_examens_v1", "economie", "Economie", "groen");
    // Spelling
    loadDuruAttempts(attempts, "duru_nederlands_spelling_examens_v1", "nederlands-spelling", "Spelling", "oranje");
    // Begrijpend Lezen
    loadBegrijpendLezenAttempts(attempts);

    // Sort by timestamp descending (newest first)
    attempts.sort(function (a, b) {
      return b.timestamp - a.timestamp;
    });

    window.allAttempts = attempts;

    // Populate overall totals
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
    renderVakKaarten(attempts);
    renderScoreTimeline(attempts);
    renderAttemptsTable();
  }

  // ── Helper: load practice object (pogingen / titels / beste) ──
  function loadPracticeData(storageKey) {
    try {
      var data = JSON.parse(localStorage.getItem(storageKey));
      if (!data) return null;
      return {
        xp:      data.xp      || 0,
        badges:  data.badges  || {},
        beste:   data.beste   || {},
        gedaan:  data.gedaan  || {},
        pogingen: data.pogingen || {},
        titels:  data.titels  || {}
      };
    } catch (e) {
      console.warn("Could not parse practice key: " + storageKey, e);
      return null;
    }
  }

  // ── Helper parsing functions ──────────────────────────────
  function loadDuruAttempts(attemptsList, key, vakId, vakTitel, vakKleur) {
    try {
      var data = JSON.parse(localStorage.getItem(key));
      if (data && data.history && Array.isArray(data.history)) {
        data.history.forEach(function (att) {
          var ts = parseDuruDate(att.datum);
          var pct = att.pct !== undefined ? att.pct : Math.round((att.goed / att.totaal) * 100);

          // Nederlands schoolcijfer 1–10 (10% = 1, 100% = 10)
          var cijferVal = 1 + (pct / 100) * 9;
          cijferVal = Math.round(cijferVal * 10) / 10; // round to 1 decimal place

          attemptsList.push({
            timestamp: ts,
            datumStr: att.datum || "",
            vakId: vakId,
            vakTitel: vakTitel,
            vakKleur: vakKleur,
            examId: att.examId || "",
            titel: att.examTitel || "Proeftoets",
            goed: att.goed !== undefined ? att.goed : 0,
            totaal: att.totaal !== undefined ? att.totaal : 10,
            pct: pct,
            cijfer: cijferVal,
            geslaagd: cijferVal >= 5.5
          });
        });
      }
    } catch (e) {
      console.warn("Error loading attempts for " + key, e);
    }
  }

  // Parses Begrijpend Lezen attempts
  function loadBegrijpendLezenAttempts(attemptsList) {
    try {
      var history = JSON.parse(localStorage.getItem("begrijpend_lezen_history"));
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
    } catch (e) {
      console.warn("Error loading Begrijpend Lezen history", e);
    }
  }

  function parseDuruDate(dateStr) {
    if (!dateStr) return new Date();
    try {
      // Expecting "DD-MM-YYYY HH:mm"
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

  // ── Render per-subject cards ──────────────────────────────
  function renderVakKaarten(attempts) {
    var grid = document.getElementById("vak-stats-grid");
    if (!grid) return;

    // Subject definitions (practice subjects + begrijpend lezen)
    var vakken = [
      {
        id: "natuurkunde",
        titel: "Natuurkunde (NASK)",
        icoon: "⚛️",
        kleur: "blauw",
        practiceKey: "duru_nask_v1",
        hasPractice: true
      },
      {
        id: "wiskunde",
        titel: "Wiskunde",
        icoon: "⚖️",
        kleur: "teal",
        practiceKey: "duru_wiskunde_v1",
        hasPractice: true
      },
      {
        id: "economie",
        titel: "Economie",
        icoon: "💶",
        kleur: "groen",
        practiceKey: "duru_economi_v1",
        hasPractice: true
      },
      {
        id: "nederlands-spelling",
        titel: "Spelling & Grammatica",
        icoon: "✍️",
        kleur: "oranje",
        practiceKey: "duru_nederlands_spelling_v1",
        hasPractice: true
      },
      {
        id: "nederlands-begrijpend",
        titel: "Begrijpend Lezen",
        icoon: "🧠",
        kleur: "oranje",
        practiceKey: null,
        hasPractice: false
      }
    ];

    var html = "";

    vakken.forEach(function (vak) {
      // Exam attempts for this subject
      var vakAttempts = attempts.filter(function (a) { return a.vakId === vak.id; });
      var examCount = vakAttempts.length;

      // Practice data (only for practice subjects)
      var prac = vak.hasPractice ? loadPracticeData(vak.practiceKey) : null;
      var pogingen = prac ? (prac.pogingen || {}) : {};
      var titels   = prac ? (prac.titels   || {}) : {};
      var beste    = prac ? (prac.beste    || {}) : {};

      // Total practice sessions = sum of all pogingen values
      var totalPogingen = 0;
      Object.keys(pogingen).forEach(function (tid) {
        totalPogingen += (pogingen[tid] || 0);
      });

      // Distinct topics = union of keys in pogingen and beste
      var topicSet = {};
      Object.keys(pogingen).forEach(function (tid) { topicSet[tid] = true; });
      Object.keys(beste).forEach(function (tid) { topicSet[tid] = true; });
      var topicIds = Object.keys(topicSet);
      var topicCount = topicIds.length;

      // Grade stats from exam attempts
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

      var avgStr      = examCount > 0 ? avgCijfer.toFixed(1).replace(".", ",")     : "-";
      var hoogsteStr  = examCount > 0 ? hoogsteCijfer.toFixed(1).replace(".", ",") : "-";

      // Empty state: nothing at all
      var isEmpty = (examCount === 0) && (!vak.hasPractice || totalPogingen === 0);

      // ── Build card HTML ───────────────────────────────────
      html += '<div class="vak-stat-card vak-stat-card--' + vak.kleur + '">';

      // Header row
      html += '<div class="vak-stat-card__header">';
      html +=   '<span class="vak-stat-card__icoon">' + vak.icoon + '</span>';
      html +=   '<span class="vak-stat-card__naam">' + vak.titel + '</span>';
      html += '</div>';

      if (isEmpty) {
        // Empty state
        html += '<p class="vak-stat-card__leeg">Nog niets gedaan &mdash; start een oefening! 🚀</p>';
      } else {
        // Big cijfer
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

        // Metric rows
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

        // Details toggle
        html += '<button class="detail-toggle" type="button" aria-expanded="false">';
        html +=   'Details <span class="detail-toggle__arrow">▾</span>';
        html += '</button>';

        // Detail panel (hidden by default)
        html += '<div class="vak-detail">';

        // ── Proeftoetsen sub-table ────────────────────────
        if (examCount > 0) {
          // Group by examId (fall back to titel when examId empty)
          var examGroups = {};
          vakAttempts.forEach(function (a) {
            var gKey = (a.examId && a.examId !== "") ? a.examId : a.titel;
            if (!examGroups[gKey]) {
              examGroups[gKey] = {
                titel: a.titel,
                attempts: []
              };
            }
            examGroups[gKey].attempts.push(a);
          });

          html += '<h4 class="vak-detail__kop">🧪 Proeftoetsen</h4>';
          html += '<table class="vak-detail-table">';
          html +=   '<thead><tr>';
          html +=     '<th>Onderwerp</th>';
          html +=     '<th>Aantal keer</th>';
          html +=     '<th>Beste cijfer</th>';
          html +=     '<th>Laatste cijfer</th>';
          html +=     '<th>Laatste datum</th>';
          html +=   '</tr></thead>';
          html +=   '<tbody>';

          Object.keys(examGroups).forEach(function (gKey) {
            var grp = examGroups[gKey];
            var grpAttempts = grp.attempts;

            // Sort group ascending by timestamp to find last
            grpAttempts.sort(function (a, b) { return a.timestamp - b.timestamp; });

            var best = 0;
            grpAttempts.forEach(function (a) {
              if (a.cijfer > best) best = a.cijfer;
            });
            var last = grpAttempts[grpAttempts.length - 1];
            var lastCijfer = last.cijfer;
            var lastDatum  = (last.datumStr || "").split(" ")[0] || last.datumStr;
            var lastKlasse = lastCijfer >= 5.5 ? "pass" : "fail";
            var bestKlasse = best >= 5.5 ? "pass" : "fail";

            html += '<tr>';
            html +=   '<td><strong>' + escHtml(grp.titel) + '</strong></td>';
            html +=   '<td>&times; ' + grpAttempts.length + ' keer</td>';
            html +=   '<td><span class="badge-grade ' + bestKlasse + '">' + best.toFixed(1).replace(".", ",") + '</span></td>';
            html +=   '<td><span class="badge-grade ' + lastKlasse + '">' + lastCijfer.toFixed(1).replace(".", ",") + '</span></td>';
            html +=   '<td style="color:var(--grijs);font-size:13px;">' + escHtml(lastDatum) + '</td>';
            html += '</tr>';
          });

          html +=   '</tbody></table>';
        } else {
          html += '<p class="vak-detail__leeg">Nog geen proeftoetsen gemaakt.</p>';
        }

        // ── Oefenen per onderwerp sub-table (not for begrijpend) ──
        if (vak.hasPractice) {
          html += '<h4 class="vak-detail__kop" style="margin-top:16px;">🔁 Oefenen per onderwerp</h4>';
          if (topicCount > 0) {
            html += '<table class="vak-detail-table">';
            html +=   '<thead><tr>';
            html +=     '<th>Onderwerp</th>';
            html +=     '<th>Geoefend</th>';
            html +=     '<th>Beste score</th>';
            html +=   '</tr></thead>';
            html +=   '<tbody>';

            topicIds.forEach(function (tid) {
              var topicTitel = titels[tid] || tid;
              var pogCount   = pogingen[tid] || 0;
              var besteScore = beste[tid] !== undefined ? beste[tid] : null;

              html += '<tr>';
              html +=   '<td>' + escHtml(topicTitel) + '</td>';
              html +=   '<td>&times; ' + pogCount + ' keer</td>';
              html +=   '<td>';
              if (besteScore !== null) {
                var bPct = Math.round(besteScore);
                html += '<span class="vak-score-badge">' + bPct + '%</span>';
              } else {
                html += '<span style="color:var(--grijs-licht);">-</span>';
              }
              html +=   '</td>';
              html += '</tr>';
            });

            html +=   '</tbody></table>';
          } else {
            html += '<p class="vak-detail__leeg">Nog geen oefeningen gedaan.</p>';
          }
        }

        html += '</div>'; // .vak-detail
      }

      html += '</div>'; // .vak-stat-card
    });

    grid.innerHTML = html;
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

    // Chart timeline needs oldest attempts first
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

    // Gradients
    svg += '<defs>';
    svg += '  <linearGradient id="chartFillGradient" x1="0" y1="0" x2="0" y2="1">';
    svg += '    <stop offset="0%" stop-color="var(--hub-hoofd)" stop-opacity="0.25"/>';
    svg += '    <stop offset="100%" stop-color="var(--hub-hoofd)" stop-opacity="0"/>';
    svg += '  </linearGradient>';
    svg += '</defs>';

    // Horizontal grid lines (grades 10, 8, 5.5, 3, 1)
    var gridGrades = [1, 3, 5.5, 8, 10];
    gridGrades.forEach(function (g) {
      var y = getY(g);
      var isPass = g === 5.5;
      var strokeStyle = isPass ? 'stroke="var(--groen)" stroke-dasharray="4,4" stroke-opacity="0.7"' : 'stroke="var(--lijn)" stroke-opacity="0.5"';

      svg += '  <line x1="' + left + '" y1="' + y + '" x2="' + (w - right) + '" y2="' + y + '" ' + strokeStyle + ' stroke-width="1" />';

      var textStyle = isPass ? 'fill="var(--groen)" font-weight="bold"' : 'fill="var(--grijs-licht)"';
      svg += '  <text x="' + (left - 8) + '" y="' + (y + 4) + '" text-anchor="end" class="svg-chart-text" ' + textStyle + '>' + g.toString().replace(".", ",") + '</text>';
    });

    // Build path elements
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

    // Draw Fill
    svg += '  <path d="' + fillPoints.join(" ") + '" fill="url(#chartFillGradient)" />';

    // Draw Line
    if (chartAttempts.length > 1) {
      svg += '  <path d="' + pathPoints.join(" ") + '" fill="none" stroke="var(--hub-hoofd)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />';
    }

    // Draw Data Dots
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

    // Render X axis labels
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

  // ── Render Exam Log Table ─────────────────────────────────
  function renderAttemptsTable() {
    var tbody = document.getElementById("exam-attempts-tbody");
    if (!tbody) return;

    var attempts = window.allAttempts || [];

    // Filter list
    var filtered = attempts.filter(function (att) {
      // 1. Filter by category tab
      if (window.currentTableFilter !== "all") {
        if (att.vakId !== window.currentTableFilter) {
          return false;
        }
      }

      // 2. Filter by search query
      if (window.currentTableSearch) {
        var query = window.currentTableSearch.toLowerCase();
        var matchTitle = att.titel.toLowerCase().indexOf(query) !== -1;
        var matchVak   = att.vakTitel.toLowerCase().indexOf(query) !== -1;
        if (!matchTitle && !matchVak) {
          return false;
        }
      }

      return true;
    });

    if (filtered.length === 0) {
      tbody.innerHTML = '<tr>' +
                          '<td colspan="5" style="text-align:center; padding:32px; color:var(--grijs-licht);">' +
                            'Geen gemaakte toetsen gevonden met de geselecteerde filters.' +
                          '</td>' +
                        '</tr>';
      return;
    }

    var html = "";
    filtered.forEach(function (att) {
      var gradeClass    = att.geslaagd ? "pass" : "fail";
      var formattedGrade = att.cijfer.toFixed(1).replace(".", ",");

      html += '<tr>' +
                '<td>' + att.datumStr + '</td>' +
                '<td><span class="subject-badge ' + att.vakKleur + '">' + att.vakTitel + '</span></td>' +
                '<td><strong>' + att.titel + '</strong></td>' +
                '<td>' + att.goed + ' / ' + att.totaal + ' <span style="color:var(--grijs-licht); font-size:12px;">(' + att.pct + '%)</span></td>' +
                '<td><span class="badge-grade ' + gradeClass + '">' + formattedGrade + '</span></td>' +
              '</tr>';
    });

    tbody.innerHTML = html;
  }

  // ── Bind search and filter events ─────────────────────────
  function initFiltersAndSearch() {
    // 1. Category Filter Buttons
    var filterButtons = document.querySelectorAll("#table-filter-bar .filter-btn");
    filterButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterButtons.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");

        window.currentTableFilter = btn.getAttribute("data-filter");
        renderAttemptsTable();
      });
    });

    // 2. Search Input box
    var searchInput = document.getElementById("exam-search");
    if (searchInput) {
      searchInput.addEventListener("input", function () {
        window.currentTableSearch = searchInput.value;
        renderAttemptsTable();
      });
    }
  }

})();
