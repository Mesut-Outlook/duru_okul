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

  // Vakregister komt uit js/vakken.js — één bron voor alle drie de panelen.
  var VAK_REGISTER = window.DURU_VAKKEN.alle;

  // ── Initialization on DOM Ready ──────────────────────────
  document.addEventListener("DOMContentLoaded", function () {
    initTabs();
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


  window.loadDashboardData = loadDashboardData;

  // ── Helper: safeReadJson (supports user prefix & raw storage) ─
  /* Ruwe lees: langs de prefix-override van landing.js heen, zodat we sleutels
     exact kunnen adresseren in plaats van impliciet via de actieve gebruiker. */
  function leesRuw(sleutel) {
    try {
      if (typeof originalGetItem === "function") {
        return originalGetItem.call(localStorage, sleutel);
      }
      return localStorage.getItem(sleutel);
    } catch (e) {
      return null;
    }
  }

  /* Exacte, geordende lookup — nooit raden.
       1. de ingelogde leerling  → user_<gebruiker>_<sleutel>
       2. sleutels van vóór multi-user → <sleutel> zonder prefix
     De vorige versie eindigde met een scan door heel localStorage die op
     SUBSTRING matchte; die kon de gegevens van een ándere gebruiker
     teruggeven (zie ouder_dashboard.js voor dezelfde correctie). */
  function safeReadJson(logicalKey) {
    if (!logicalKey) return null;

    var actieveUser = null;
    try {
      actieveUser = localStorage.getItem("duru_active_user") ||
                    sessionStorage.getItem("duru_active_user");
    } catch (e) {}

    var kandidaten = [];
    if (actieveUser) kandidaten.push("user_" + actieveUser + "_" + logicalKey);
    kandidaten.push(logicalKey);

    for (var i = 0; i < kandidaten.length; i++) {
      var raw = leesRuw(kandidaten[i]);
      if (raw) {
        try { return JSON.parse(raw); } catch (e) { return null; }
      }
    }
    return null;
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

        var cijferVal = window.DURU_CIJFER.vanPct(pct);
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
          geslaagd: window.DURU_CIJFER.geslaagd(cijferVal)
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
          geslaagd: window.DURU_CIJFER.geslaagd(gradeVal)
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



  // ── Simple HTML escaping helper ───────────────────────────
  /* ─────────────────────────────────────────────────────────
     Voortgangspaneel — herontwerp 2026-09.

     Stond eerst als één kolom onder elkaar: 4 KPI-kaarten, 12 vakkaarten,
     41 hoofdstukkaarten, de grafiek én een logboek van 200+ rijen. Om te
     zien wat je moest doen, moest je langs alles scrollen.

     Nu leest de pagina in één volgorde: WAT NU? → waar sta je (cijferschaal)
     → momentum → details achter tabs. Anders dan het ouderpaneel (dat
     diagnose en een printbaar rapport geeft) staat hier de VOLGENDE STAP
     bovenaan: Duru wil weten wat ze moet doen, niet hoe het met haar gaat.
     ───────────────────────────────────────────────────────── */

  var C = window.DURU_CIJFER;

  var actieveTab  = "overzicht";
  var logFilter   = { q: "", vak: "" };
  var laatsteModel = null;

  var KLASSE_KLEUR = {
    goed: "var(--st-goed)",
    net:  "var(--st-net)",
    zwak: "var(--st-zwak)",
    none: "var(--st-mut)"
  };

  function fmtC(c) { return C.tekst(c); }
  function kleurVan(c, n) { return KLASSE_KLEUR[C.klasse(c, n)]; }
  function kortDatum(s) { return String(s || "").split(" ")[0] || "—"; }

  function pil(c, n, tekst) {
    return '<span class="st-pil st-pil--' + C.klasse(c, n) + '">' +
      (tekst != null ? tekst : (n ? fmtC(c) : "nieuw")) + '</span>';
  }

  /* ── Model: vakken → hoofdstukken → pogingen ────────────── */
  function bouwModel(attempts, vakkenVanJaar) {
    var vakken = vakkenVanJaar.map(function (vak) {
      var eigen = attempts.filter(function (a) { return a.vakId === vak.id; });
      var defs = window.DURU_HF ? window.DURU_HF.lijst(vak.id) : [];
      var gezien = {};

      var hfs = defs.map(function (ch) {
        gezien[ch.nr] = true;
        var lijst = eigen.filter(function (a) { return a.hoofdstuk === ch.nr; });
        var uniek = {};
        lijst.forEach(function (a) { uniek[a.examId || a.titel] = 1; });
        var gedaan = Object.keys(uniek).length;
        var exTot = window.DURU_HF ? window.DURU_HF.totaalExamens(vak.id, ch.nr) : 0;
        return {
          nr: ch.nr, titel: ch.titel, icoon: ch.icoon || "📖", vak: vak,
          lijst: lijst, count: lijst.length, gem: C.gemiddelde(lijst, "cijfer"),
          beste: lijst.length ? Math.max.apply(null, lijst.map(function (a) { return a.cijfer; })) : 0,
          laatsteDatum: lijst.length ? kortDatum(lijst[0].datumStr) : "—",
          // recent = de laatste 3 toetsen. Voor "wat nu?" telt waar je NU staat,
          // niet je gemiddelde over het hele jaar: een hoofdstuk dat van 8,2
          // naar 4,6 zakt houdt een gemiddelde van 6,4 en zou anders onzichtbaar
          // blijven, terwijl dat juist het urgentste is.
          recent: C.gemiddelde(lijst.slice(0, 3), "cijfer"),
          gedaan: gedaan, exTotaal: exTot,
          over: Math.max(0, exTot - gedaan),
          vg: exTot ? Math.min(100, Math.round((gedaan / exTot) * 100)) : 0
        };
      });

      // Toetsen die aan geen enkel hoofdstuk hangen — niet verstoppen.
      var overig = eigen.filter(function (a) { return a.hoofdstuk == null || !gezien[a.hoofdstuk]; });
      if (overig.length) {
        // Gemaakte toetsen die niet (meer) in het manifest staan: tel ze als
        // gedaan én in het totaal, anders staat er "0/10 toetsen" naast een 7,3.
        var uniekOverig = {};
        overig.forEach(function (a) { uniekOverig[a.examId || a.titel] = 1; });
        var nOverig = Object.keys(uniekOverig).length;
        hfs.push({
          nr: null, titel: "Overige toetsen", icoon: "📦", vak: vak,
          lijst: overig, count: overig.length, gem: C.gemiddelde(overig, "cijfer"),
          recent: C.gemiddelde(overig.slice(0, 3), "cijfer"),
          beste: Math.max.apply(null, overig.map(function (a) { return a.cijfer; })),
          laatsteDatum: kortDatum(overig[0].datumStr),
          gedaan: nOverig, exTotaal: nOverig, over: 0, vg: 100
        });
      }

      var tot = 0, ged = 0;
      hfs.forEach(function (h) { tot += h.exTotaal; ged += Math.min(h.gedaan, h.exTotaal); });

      return {
        vak: vak, pogingen: eigen, count: eigen.length,
        gem: C.gemiddelde(eigen, "cijfer"),
        beste: eigen.length ? Math.max.apply(null, eigen.map(function (a) { return a.cijfer; })) : 0,
        laatsteDatum: eigen.length ? kortDatum(eigen[0].datumStr) : "—",
        hfs: hfs, gedaan: ged, exTotaal: tot,
        vg: tot ? Math.round((ged / tot) * 100) : 0
      };
    });

    var alleHf = [];
    vakken.forEach(function (v) { v.hfs.forEach(function (h) { alleHf.push(h); }); });

    var nu = attempts.length ? attempts[0].timestamp : Date.now();

    return {
      attempts: attempts,
      vakken: vakken,
      actief: vakken.filter(function (v) { return v.count > 0; }),
      alleHf: alleHf,
      gem: C.gemiddelde(attempts, "cijfer"),
      geslaagdN: attempts.filter(function (a) { return a.geslaagd; }).length,
      week: attempts.filter(function (a) { return a.timestamp >= nu - 7 * 864e5; }),
      streak: berekenStreak(attempts, nu),
      open: vakken.reduce(function (s, v) { return s + Math.max(0, v.exTotaal - v.gedaan); }, 0)
    };
  }

  /* Aantal dagen op rij met minstens één toets, geteld vanaf de laatste dag. */
  function berekenStreak(attempts, nu) {
    if (!attempts.length) return 0;
    var dagen = {};
    attempts.forEach(function (a) { dagen[new Date(a.timestamp).toDateString()] = 1; });
    var n = 0, d = new Date(nu);
    while (dagen[d.toDateString()]) { n++; d.setDate(d.getDate() - 1); }
    return n;
  }

  /* ── Verloop ───────────────────────────────────────────── */
  function trendVan(lijst) {
    if (!lijst || lijst.length < 4) return null;
    var recent = lijst.slice(0, 3), ouder = lijst.slice(3, 6);
    if (!ouder.length) return null;
    var d = C.gemiddelde(recent, "cijfer") - C.gemiddelde(ouder, "cijfer");
    if (Math.abs(d) < 0.3) return { d: d, r: "vlak" };
    return { d: d, r: d > 0 ? "op" : "neer" };
  }

  function trendHtml(lijst) {
    var t = trendVan(lijst);
    if (!t || t.r === "vlak") return "";
    var op = t.r === "op";
    return '<span class="st-trend st-trend--' + (op ? "op" : "neer") +
      '" title="Je laatste 3 toetsen vergeleken met de 3 daarvoor">' +
      (op ? "▲" : "▼") + fmtC(Math.abs(t.d)) + '</span>';
  }

  function daalt(h) { var t = trendVan(h && h.lijst); return !!t && t.r === "neer"; }

  function sparkline(lijst) {
    var p = (lijst || []).slice(0, 8).reverse();
    if (p.length < 2) return '<span class="st-spark-leeg">–</span>';

    var b = 60, h = 18, m = 3, stap = (b - m * 2) / (p.length - 1);
    var xy = p.map(function (a, i) {
      return [m + i * stap, h - m - (C.positie(a.cijfer) / 100) * (h - m * 2)];
    });
    var d = xy.map(function (q, i) {
      return (i ? "L" : "M") + q[0].toFixed(1) + " " + q[1].toFixed(1);
    }).join(" ");
    var e = xy[xy.length - 1];
    var k = kleurVan(p[p.length - 1].cijfer, 1);
    var dy = (h - m - (C.positie(C.DREMPEL) / 100) * (h - m * 2)).toFixed(1);

    return '<svg class="st-spark" width="' + b + '" height="' + h + '" viewBox="0 0 ' + b + ' ' + h +
      '" role="img" aria-label="Verloop van je laatste ' + p.length + ' toetsen">' +
      '<line x1="0" y1="' + dy + '" x2="' + b + '" y2="' + dy +
        '" stroke="var(--st-mut)" stroke-width="1" stroke-dasharray="2,2" opacity=".45"/>' +
      '<path d="' + d + '" fill="none" stroke="' + k + '" stroke-width="1.5" ' +
        'stroke-linecap="round" stroke-linejoin="round"/>' +
      '<circle cx="' + e[0].toFixed(1) + '" cy="' + e[1].toFixed(1) + '" r="2.3" fill="' + k + '"/></svg>';
  }

  /* ── "Wat nu?" ──────────────────────────────────────────
     De volgorde IS het advies: wegzakken eerst (daar verlies je het snelst),
     dan onvoldoende, dan bijna-examenklaar, dan nog niet begonnen. */
  function watNu(model) {
    var gedaan = model.alleHf.filter(function (h) { return h.count > 0; });
    var zwak = gedaan.filter(function (h) { return !C.geslaagd(h.recent); })
                     .sort(function (a, b) { return a.recent - b.recent; });

    var dalend = zwak.filter(daalt);
    var wegzakkend = gedaan.filter(function (h) {
      return daalt(h) && C.geslaagd(h.recent) && zwak.indexOf(h) === -1;
    }).sort(function (a, b) { return a.recent - b.recent; });

    var hf = null, label, titel, waarom, knop;

    if (dalend.length) {
      hf = dalend[0];
      label = "Eerst dit";
      titel = "Herhaal " + hf.vak.titel + hfLabel(hf) + " — " + hf.titel;
      waarom = "Je laatste toetsen gingen omlaag naar " + fmtC(hf.recent) +
               ". Dit zakt weg, dus hier beginnen levert het meeste op.";
      knop = "Ga oefenen";
    } else if (zwak.length) {
      hf = zwak[0];
      label = "Eerst dit";
      titel = "Oefen " + hf.vak.titel + hfLabel(hf) + " — " + hf.titel;
      waarom = "Je staat hier op " + fmtC(hf.recent) +
               ", nog onder de 5,5. Eén goede toets tilt je erboven.";
      knop = "Ga oefenen";
    } else if (wegzakkend.length) {
      hf = wegzakkend[0];
      label = "Let op";
      titel = "Frist " + hf.vak.titel + hfLabel(hf) + " even op";
      waarom = "Je stond hier hoger, maar je laatste toetsen zakken richting " +
               fmtC(hf.recent) + ". Nu bijsturen is makkelijker dan straks inhalen.";
      knop = "Ga oefenen";
    } else {
      var bijna = gedaan.filter(function (h) {
        return h.recent >= C.GOED && !C.examenklaar(h.recent);
      }).sort(function (a, b) { return b.recent - a.recent; });

      if (bijna.length) {
        hf = bijna[0];
        label = "Bijna klaar";
        titel = "Nog één toets voor " + hf.vak.titel + hfLabel(hf);
        waarom = "Je staat op " + fmtC(hf.recent) +
                 ". Vanaf 8,5 ben je klaar voor de schooltoets — dat is dichtbij.";
        knop = "Pak die 8,5";
      } else {
        var nieuw = model.alleHf.filter(function (h) { return h.count === 0 && h.exTotaal > 0; });
        if (nieuw.length) {
          hf = nieuw[0];
          label = "Nieuw";
          titel = "Begin met " + hf.vak.titel + hfLabel(hf) + " — " + hf.titel;
          waarom = "Dit hoofdstuk heb je nog niet geoefend. " +
                   hf.exTotaal + " proeftoetsen staan klaar.";
          knop = "Beginnen";
        } else if (model.attempts.length) {
          label = "Top";
          titel = "Je staat overal voldoende";
          waarom = "Alle hoofdstukken staan boven de 5,5. Kies zelf een vak om scherp te blijven.";
          knop = null;
        } else {
          label = "Start";
          titel = "Nog geen toetsen dit schooljaar";
          waarom = "Kies een vak op het tabblad “Mijn vakken” en maak je eerste proeftoets.";
          knop = null;
        }
      }
    }

    return { label: label, titel: titel, waarom: waarom, knop: knop, hf: hf };
  }

  function hfLabel(hf) { return hf.nr != null ? " H" + hf.nr : ""; }

  /* ── Onderdelen ────────────────────────────────────────── */
  function schaalHtml(model) {
    var h = '<div class="st-schaal-track"></div><div class="st-schaal-drempel"></div>';
    model.actief.forEach(function (v) {
      h += '<span class="st-schaal-vak" style="left:' + C.positie(v.gem) + '%;background:' +
        kleurVan(v.gem, v.count) + '" title="' + escHtml(v.vak.titel) + ' — ' + fmtC(v.gem) + '"></span>';
    });
    if (model.attempts.length) {
      h += '<span class="st-schaal-mij" style="left:' + C.positie(model.gem) + '%;color:' +
        kleurVan(model.gem, 1) + '"><span class="st-schaal-punt"></span></span>';
    }
    return h;
  }

  function miniSchaal(c, n) {
    return '<span class="st-mschaal-wrap"><span class="st-mschaal">' +
      '<span class="st-mschaal-vul" style="width:' + C.positie(c) + '%;background:' + kleurVan(c, n) + '"></span>' +
      '<span class="st-mschaal-drempel"></span></span>' +
      '<span class="st-mschaal-c" style="color:' + kleurVan(c, n) + '">' + (n ? fmtC(c) : "—") + '</span></span>';
  }

  function vakRij(v) {
    var aantalHf = v.hfs.filter(function (h) { return h.nr != null; }).length;
    return '<button type="button" class="st-vakrij" data-open-vak="' + escHtml(v.vak.id) + '">' +
      '<span class="st-vaknaam"><span class="st-vakico">' + (v.vak.icoon || "") + '</span>' +
      '<span class="st-vaktekst"><span class="st-vaktitel">' + escHtml(v.vak.titel) + '</span>' +
      '<span class="st-vakmeta">' + v.count + (v.count === 1 ? ' poging' : ' pogingen') + ' · ' +
        aantalHf + (aantalHf === 1 ? ' hoofdstuk' : ' hoofdstukken') + '</span></span></span>' +
      miniSchaal(v.gem, v.count) +
      '<span class="st-spark-cel">' + sparkline(v.pogingen) + trendHtml(v.pogingen) + '</span>' +
      '<span class="st-vg">' + (v.exTotaal ? v.gedaan + "/" + v.exTotaal + " toetsen" : "—") +
        '<span class="st-vg-bar"><span class="st-vg-vul" style="width:' + v.vg + '%"></span></span></span>' +
      '<span class="st-chev">›</span></button>';
  }

  /* ── Tabbladen ─────────────────────────────────────────── */
  function tabOverzicht(model) {
    // Vakken zonder inhoud én zonder pogingen (bv. een smoke-test-vak) niet
    // tonen: dezelfde regel als het tabblad "Vakken".
    var gesorteerd = model.vakken.filter(function (v) { return v.exTotaal > 0 || v.count > 0; }).sort(function (a, b) {
      if (!a.count && b.count) return 1;
      if (a.count && !b.count) return -1;
      return a.gem - b.gem;
    });

    return '<div class="st-sec-kop"><h3>Mijn vakken</h3>' +
      '<p>Het vak dat de meeste aandacht vraagt staat bovenaan. Klik om te oefenen.</p></div>' +
      '<div class="st-vaklijst">' + gesorteerd.map(vakRij).join("") + '</div>' +
      '<div class="st-sec-kop"><h3>Score verloop</h3><p>Je laatste 15 proeftoetsen.</p></div>' +
      '<div class="chart-card"><div class="svg-container" id="line-chart-container"></div></div>';
  }

  function tabVakken(model) {
    var metInhoud = model.vakken.filter(function (v) { return v.exTotaal > 0 || v.count > 0; });
    if (!metInhoud.length) {
      return '<div class="st-leeg">Voor dit schooljaar staat er nog geen lesmateriaal klaar.</div>';
    }

    return '<div class="st-sec-kop"><h3>Per vak</h3>' +
      '<p>Hoeveel proeftoetsen heb je al gemaakt, en hoe sta je ervoor?</p></div>' +
      '<div class="st-kaartgrid">' + metInhoud.map(function (v) {
        var over = Math.max(0, v.exTotaal - v.gedaan);
        return '<article class="st-kaart">' +
          '<div class="st-kaartkop"><div>' +
            '<span class="st-kaartnr">' + v.count + ' toetsen gemaakt</span>' +
            '<span class="st-kaarttitel">' + (v.vak.icoon || "") + ' ' + escHtml(v.vak.titel) + '</span>' +
          '</div>' + pil(v.gem, v.count, v.count ? null : "nog niets") + '</div>' +
          '<div class="st-kaartstats">' +
            '<div><span class="st-slabel">Voortgang</span><span class="st-swaarde">' +
              (v.exTotaal ? v.gedaan + "/" + v.exTotaal + " · " + v.vg + "%" : "—") + '</span></div>' +
            '<div><span class="st-slabel">Beste</span><span class="st-swaarde">' +
              (v.count ? fmtC(v.beste) : "—") + '</span></div>' +
            '<div><span class="st-slabel">Laatst</span><span class="st-swaarde">' +
              escHtml(v.laatsteDatum) + '</span></div>' +
          '</div>' +
          (v.exTotaal ? '<span class="st-vg-bar"><span class="st-vg-vul" style="width:' + v.vg + '%"></span></span>' : '') +
          '<p class="st-kaartactie">' + (over > 0
            ? "Nog <b>" + over + (over === 1 ? " proeftoets" : " proeftoetsen") + "</b> te gaan."
            : (v.exTotaal ? "Alle proeftoetsen gemaakt. 🎉" : "Nog geen proeftoetsen beschikbaar.")) +
          '</p>' +
          '<button type="button" class="st-kaartknop" data-open-vak="' + escHtml(v.vak.id) + '">Ga oefenen →</button>' +
        '</article>';
      }).join("") + '</div>';
  }

  function tabHoofdstukken(model) {
    var lijst = model.alleHf.slice().sort(function (a, b) {
      if (!a.count && b.count) return 1;
      if (a.count && !b.count) return -1;
      var da = daalt(a) ? 0 : 1, db = daalt(b) ? 0 : 1;
      if (da !== db) return da - db;
      return a.gem - b.gem;
    });

    if (!lijst.length) {
      return '<div class="st-leeg">Nog geen hoofdstukken voor dit schooljaar.</div>';
    }

    return '<div class="st-sec-kop"><h3>Per hoofdstuk</h3>' +
      '<p>Van &ldquo;moet nog oefenen&rdquo; naar &ldquo;klaar voor de schooltoets&rdquo;.</p></div>' +
      '<div class="st-kaartgrid">' + lijst.map(function (h) {
        var letOp = h.count > 0 && !C.geslaagd(h.gem);
        var actie = !h.count
          ? "Nog niet begonnen — " + h.exTotaal + " toetsen staan klaar."
          : C.examenklaar(h.gem) ? "Klaar voor de schooltoets. 🌟"
          : h.gem >= C.GOED ? "Goed bezig. Nog één toets voor een 8,5."
          : C.geslaagd(h.gem) ? "Voldoende. Kijk je fouten na en probeer het nog eens."
          : "Herhaal dit hoofdstuk — begin met de oefenvragen.";

        return '<article class="st-kaart' + (letOp ? " st-kaart--letop" : "") + '">' +
          '<div class="st-kaartkop"><div>' +
            '<span class="st-kaartnr">' + (h.vak.icoon || "") + ' ' + escHtml(h.vak.titel) +
              (h.nr != null ? " · H" + h.nr : "") + '</span>' +
            '<span class="st-kaarttitel">' + escHtml(h.titel) + '</span>' +
          '</div>' + pil(h.gem, h.count) + '</div>' +
          '<div class="st-kaartstats">' +
            '<div><span class="st-slabel">Gemaakt</span><span class="st-swaarde">' +
              (h.exTotaal ? h.gedaan + "/" + h.exTotaal : h.gedaan) + '</span></div>' +
            '<div><span class="st-slabel">Beste</span><span class="st-swaarde">' +
              (h.count ? fmtC(h.beste) : "—") + '</span></div>' +
            '<div><span class="st-slabel">Laatst</span><span class="st-swaarde">' +
              escHtml(h.laatsteDatum) + '</span></div>' +
          '</div>' +
          '<p class="st-kaartactie">' + (daalt(h) ? "<b>Let op: dit gaat omlaag.</b> " : "") + actie + '</p>' +
          '<button type="button" class="st-kaartknop" data-open-vak="' + escHtml(h.vak.id) + '">Ga oefenen →</button>' +
        '</article>';
      }).join("") + '</div>';
  }

  function logRijen(model) {
    return model.attempts.filter(function (a) {
      if (logFilter.vak && a.vakId !== logFilter.vak) return false;
      if (logFilter.q &&
          String(a.titel).toLowerCase().indexOf(logFilter.q) === -1 &&
          String(a.vakTitel).toLowerCase().indexOf(logFilter.q) === -1) return false;
      return true;
    });
  }

  function logTabelHtml(model) {
    var r = logRijen(model);
    if (!r.length) {
      return '<div class="st-leeg">' + (model.attempts.length
        ? "Geen toetsen gevonden. Pas je zoekopdracht aan."
        : "Nog geen toetsen gemaakt dit schooljaar.") + '</div>';
    }

    return '<table class="st-tabel"><thead><tr><th class="st-streep"></th>' +
      '<th>Datum</th><th>Vak</th><th>H</th><th>Toets</th><th>Goed</th><th>Cijfer</th></tr></thead><tbody>' +
      r.map(function (a) {
        return '<tr><td class="st-streep" style="background:' + kleurVan(a.cijfer, 1) + '"></td>' +
          '<td class="st-num">' + escHtml(kortDatum(a.datumStr)) + '</td>' +
          '<td>' + escHtml(a.vakTitel) + '</td>' +
          '<td><span class="st-chip">' + (a.hoofdstuk != null ? "H" + a.hoofdstuk : "—") + '</span></td>' +
          '<td>' + escHtml(a.titel) + '</td>' +
          '<td class="st-num">' + a.goed + '/' + a.totaal + '</td>' +
          '<td>' + pil(a.cijfer, 1) + '</td></tr>';
      }).join("") + '</tbody></table>';
  }

  function tabLogboek(model) {
    var h = '<div class="st-sec-kop"><h3>Logboek</h3><p>Alles wat je gemaakt hebt, nieuwste eerst.</p></div>';
    h += '<div class="st-filters">' +
      '<input type="search" id="st-zoek" class="st-zoek" placeholder="Zoek een toets…" ' +
        'aria-label="Zoeken in het logboek" value="' + escHtml(logFilter.q) + '">' +
      '<select id="st-vakfilter" class="st-zoek st-zoek--kort" aria-label="Filter op vak">' +
        '<option value="">Alle vakken</option>';
    model.actief.forEach(function (v) {
      h += '<option value="' + escHtml(v.vak.id) + '"' +
        (logFilter.vak === v.vak.id ? " selected" : "") + '>' + escHtml(v.vak.titel) + '</option>';
    });
    h += '</select></div><div class="st-tabelwrap" id="st-logtabel">' + logTabelHtml(model) + '</div>';
    return h;
  }

  function bouwTab(model) {
    if (actieveTab === "overzicht")    return tabOverzicht(model);
    if (actieveTab === "vakken")       return tabVakken(model);
    if (actieveTab === "hoofdstukken") return tabHoofdstukken(model);
    return tabLogboek(model);
  }

  /* ── Hoofdrender ───────────────────────────────────────── */
  function renderVoortgang(model) {
    var houder = document.getElementById("voortgang-paneel");
    if (!houder) return;

    laatsteModel = model;

    var W = watNu(model);
    var heeft = model.attempts.length > 0;
    var niveau = JAAR_NIVEAU[window.currentJaar] || "";
    var jaren = beschikbareJaren();

    var h = '<div class="st-wrap">';

    /* Kop + jaarkiezer */
    h += '<div class="st-bar"><div class="st-ident"><span class="st-avatar">👩‍🎓</span>' +
      '<span><span class="st-barnaam">Mijn voortgang</span>' +
      '<span class="st-barsub">' + escHtml(window.currentJaar) + ' · ' + escHtml(niveau) + '</span></span></div>';
    if (jaren.length > 1) {
      h += '<div class="st-seg" role="group" aria-label="Schooljaar">';
      jaren.forEach(function (j) {
        h += '<button type="button" class="st-jaar" data-jaar="' + escHtml(j) + '" aria-pressed="' +
          (j === window.currentJaar) + '">' + escHtml(j) + ' · ' + escHtml(JAAR_NIVEAU[j] || "") + '</button>';
      });
      h += '</div>';
    }
    h += '</div>';

    /* Status */
    // Geen tweede "Hoi Duru" en geen derde keer het schooljaar: de hero van
    // de hub en de kopbalk hierboven zeggen dat al.
    h += '<section class="st-status">' +
      '<p class="st-zin">' + (heeft
        ? "Je gemiddelde dit schooljaar is <strong>" + fmtC(model.gem) + "</strong>" +
          (C.geslaagd(model.gem) ? " — boven de 5,5, goed bezig!" : " — nog even doorzetten naar de 5,5.")
        : "Nog geen toetsen dit schooljaar. Kies een vak en begin — je resultaten verschijnen hier meteen.") +
      '</p></section>';

    /* Wat nu? */
    h += '<div class="st-watnu">' +
      '<span class="st-watnu-label">' + escHtml(W.label) + '</span>' +
      '<span class="st-watnu-titel">' + escHtml(W.titel) + '</span>' +
      '<span class="st-watnu-waarom">' + escHtml(W.waarom) + '</span>' +
      (W.knop && W.hf
        ? '<button type="button" class="st-watnu-knop" data-open-vak="' + escHtml(W.hf.vak.id) + '">' +
          escHtml(W.knop) + ' →</button>'
        : '') +
      '</div>';

    /* Cijferschaal */
    h += '<div class="st-schaal-blok"><div class="st-schaal-kop">' +
      '<span class="st-schaal-cijfer" style="color:' + kleurVan(model.gem, model.attempts.length) + '">' +
        (heeft ? fmtC(model.gem) : "–") + '</span>' +
      '<span class="st-schaal-label">jouw gemiddelde · <b>' + model.attempts.length +
        '</b> toetsen · <b>' +
        (heeft ? Math.round(model.geslaagdN / model.attempts.length * 100) : 0) +
        '%</b> voldoende</span></div>' +
      '<div class="st-schaal">' + schaalHtml(model) + '</div>' +
      '<div class="st-schaal-uit"><span>1,0</span><span>10,0</span></div></div>';

    /* Momentum */
    var st = model.streak;
    // Noemer = hoofdstukken waarin je al geoefend hebt (zelfde getal als het
    // tabblad "Hoofdstukken"), niet alle hoofdstukken van alle vakken.
    var geoefend = model.alleHf.filter(function (x) { return x.count > 0 && x.nr != null; });
    var klaar = geoefend.filter(function (x) { return C.examenklaar(x.gem); }).length;
    var exTot = model.vakken.reduce(function (s, v) { return s + v.exTotaal; }, 0);
    var exGed = model.vakken.reduce(function (s, v) { return s + v.gedaan; }, 0);
    h += '<div class="st-momentum">' +
      '<div class="st-mom' + (st >= 2 ? " st-mom--vlam" : "") + '">' +
        '<span class="st-momlabel">Op rij</span>' +
        '<span class="st-momwaarde">' + st + '<small> ' + (st === 1 ? "dag" : "dagen") + '</small></span>' +
        '<span class="st-momsub">' + (st >= 2 ? "Mooie reeks — hou vol! 🔥" : "Oefen morgen weer voor een reeks") + '</span></div>' +
      '<div class="st-mom"><span class="st-momlabel">Deze week</span>' +
        '<span class="st-momwaarde">' + model.week.length + '</span>' +
        '<span class="st-momsub">toetsen gemaakt' +
        (model.week.length ? " · gem. " + fmtC(C.gemiddelde(model.week, "cijfer")) : "") + '</span></div>' +
      '<div class="st-mom"><span class="st-momlabel">Klaar voor de toets</span>' +
        '<span class="st-momwaarde">' + klaar + '<small> / ' + geoefend.length + '</small></span>' +
        '<span class="st-momsub">van je geoefende hoofdstukken staan op 8,5+</span></div>' +
      '<div class="st-mom"><span class="st-momlabel">Proeftoetsen gedaan</span>' +
        '<span class="st-momwaarde">' + exGed + '<small> / ' + exTot + '</small></span>' +
        '<span class="st-momsub">verschillende toetsen gemaakt</span></div>' +
      '</div>';

    /* Tabs */
    var tabs = [
      { id: "overzicht",    label: "Overzicht",    tel: null },
      { id: "vakken",       label: "Vakken",       tel: model.actief.length },
      { id: "hoofdstukken", label: "Hoofdstukken", tel: geoefend.length },
      { id: "logboek",      label: "Logboek",      tel: model.attempts.length }
    ];
    h += '<nav class="st-tabs" role="tablist">';
    tabs.forEach(function (t) {
      h += '<button type="button" role="tab" class="st-tab" data-st-tab="' + t.id + '" aria-selected="' +
        (actieveTab === t.id) + '">' + t.label +
        (t.tel != null ? '<span class="st-tel">' + t.tel + '</span>' : "") + '</button>';
    });
    h += '</nav>';

    h += '<div class="st-views">' + bouwTab(model) + '</div>';
    h += '</div>';

    houder.innerHTML = h;

    bindKopEvents(model);
    bindTabEvents(model);

    // De grafiek meet zijn eigen breedte, dus pas ná het invoegen tekenen.
    if (actieveTab === "overzicht") renderScoreTimeline(model.attempts);
  }

  function wisselTab(naam, model) {
    actieveTab = naam;
    var views = document.querySelector("#voortgang-paneel .st-views");
    if (!views) { renderVoortgang(model); return; }

    views.innerHTML = bouwTab(model);
    document.querySelectorAll("#voortgang-paneel [data-st-tab]").forEach(function (b) {
      b.setAttribute("aria-selected", String(b.getAttribute("data-st-tab") === naam));
    });
    bindTabEvents(model);
    if (naam === "overzicht") renderScoreTimeline(model.attempts);
  }

  function bindKopEvents(model) {
    document.querySelectorAll("#voortgang-paneel .st-jaar").forEach(function (b) {
      b.addEventListener("click", function () {
        var j = b.getAttribute("data-jaar");
        try { localStorage.setItem("duru_dashboard_jaar", j); } catch (e) {}
        window.currentJaar = j;
        actieveTab = "overzicht";
        logFilter = { q: "", vak: "" };
        loadDashboardData();
      });
    });

    document.querySelectorAll("#voortgang-paneel [data-st-tab]").forEach(function (b) {
      b.addEventListener("click", function () { wisselTab(b.getAttribute("data-st-tab"), model); });
    });
  }

  function bindTabEvents(model) {
    var views = document.querySelector("#voortgang-paneel .st-views");
    if (!views) return;

    // "Ga oefenen": open het vak in de iframe-shell van de hub (landing.js).
    document.querySelectorAll("#voortgang-paneel [data-open-vak]").forEach(function (b) {
      if (b.dataset.stGebonden) return;
      b.dataset.stGebonden = "1";
      b.addEventListener("click", function () {
        var id = b.getAttribute("data-open-vak");
        var vak = null;
        model.vakken.forEach(function (v) { if (v.vak.id === id) vak = v.vak; });
        if (!vak) return;
        if (typeof window.openInIframe === "function") {
          window.openInIframe("./havo3/" + id + "/", vak.icoon || "📘", vak.titel);
        }
      });
    });

    var zoek = document.getElementById("st-zoek");
    var vakf = document.getElementById("st-vakfilter");
    var tab  = document.getElementById("st-logtabel");
    function herteken() { if (tab) tab.innerHTML = logTabelHtml(model); }
    if (zoek) zoek.addEventListener("input", function () { logFilter.q = zoek.value.toLowerCase(); herteken(); });
    if (vakf) vakf.addEventListener("change", function () { logFilter.vak = vakf.value; herteken(); });
  }

  function loadDashboardData() {
    window.currentJaar = bepaalCurrentJaar();

    var vakkenVanJaar = VAK_REGISTER.filter(function (v) { return v.jaar === window.currentJaar; });

    var attempts = [];
    vakkenVanJaar.forEach(function (vak) {
      if (vak.special === "begrijpend") {
        loadBegrijpendLezenAttempts(attempts, vak.examKey);
      } else {
        loadDuruAttempts(attempts, vak.examKey, vak.id, vak.titel, vak.kleur);
      }
    });
    attempts.sort(function (a, b) { return b.timestamp - a.timestamp; });
    window.allAttempts = attempts;

    renderVoortgang(bouwModel(attempts, vakkenVanJaar));
  }


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

    var gridGrades = [1, 3, window.DURU_CIJFER.DREMPEL, 8, 10];
    gridGrades.forEach(function (g) {
      var y = getY(g);
      var isPass = g === window.DURU_CIJFER.DREMPEL;
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
