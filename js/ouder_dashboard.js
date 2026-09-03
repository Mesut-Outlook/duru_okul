/* =========================================================
   Duru's Schoolhub — Veli / Baba Takip & İlerleme Paneli
   Özellikler:
   - Genel Başarı Skoru (Hollanda 1-10 not sistemi)
   - Karnede Herhangi Bir Derse Tıklandığında Ünite ve Sınav Kırılımları
   - Hoofdstuk (Ünite) Bazlı Başarı & Teşhis Karnesi
   - Güçlü & Geliştirilmesi Gereken Konular (Aandachtspunten)
   - Tarihli Sınav ve Çalışma Günlüğü (Tüm denemeler)
   - Tek Tıkla Yazdır / PDF İndir (Print-friendly format)
   ========================================================= */

(function () {
  "use strict";

  var selectedJaar = "2026-2027";

  var VAK_CONFIG = [
    // 2025-2026 (MAVO 2)
    { jaar: "2025-2026", id: "natuurkunde",          titel: "Natuurkunde (NASK)",    icoon: "⚛️", kleur: "blauw",  practiceKey: "duru_nask_v1",                examKey: "duru_nask_examens_v1" },
    { jaar: "2025-2026", id: "wiskunde",             titel: "Wiskunde",              icoon: "⚖️", kleur: "teal",   practiceKey: "duru_wiskunde_v1",            examKey: "duru_wiskunde_examens_v1" },
    { jaar: "2025-2026", id: "economie",             titel: "Economie",              icoon: "💶", kleur: "groen",  practiceKey: "duru_economi_v1",             examKey: "duru_economi_examens_v1" },
    { jaar: "2025-2026", id: "geschiedenis",         titel: "Geschiedenis",          icoon: "🕰️", kleur: "oranje", practiceKey: "duru_geschiedenis_v1",        examKey: "duru_geschiedenis_examens_v1" },
    { jaar: "2025-2026", id: "nederlands-spelling",  titel: "Spelling & Grammatica", icoon: "✍️", kleur: "oranje", practiceKey: "duru_nederlands_spelling_v1", examKey: "duru_nederlands_spelling_examens_v1" },
    { jaar: "2025-2026", id: "nederlands-begrijpend",titel: "Begrijpend Lezen",      icoon: "🧠", kleur: "oranje", practiceKey: null,                          examKey: "begrijpend_lezen_history", special: "begrijpend" },
    // 2026-2027 (HAVO 3)
    { jaar: "2026-2027", id: "nederlands",      titel: "Nederlands",      icoon: "📖", kleur: "oranje", practiceKey: "duru_2627_nederlands_v1",      examKey: "duru_2627_nederlands_examens_v1" },
    { jaar: "2026-2027", id: "engels",          titel: "Engels",          icoon: "🇬🇧", kleur: "oranje", practiceKey: "duru_2627_engels_v1",          examKey: "duru_2627_engels_examens_v1" },
    { jaar: "2026-2027", id: "frans",           titel: "Frans",           icoon: "🇫🇷", kleur: "oranje", practiceKey: "duru_2627_frans_v1",           examKey: "duru_2627_frans_examens_v1" },
    { jaar: "2026-2027", id: "duits",           titel: "Duits",           icoon: "🇩🇪", kleur: "oranje", practiceKey: "duru_2627_duits_v1",           examKey: "duru_2627_duits_examens_v1" },
    { jaar: "2026-2027", id: "wiskunde",        titel: "Wiskunde",        icoon: "⚖️", kleur: "teal",   practiceKey: "duru_2627_wiskunde_v1",        examKey: "duru_2627_wiskunde_examens_v1" },
    { jaar: "2026-2027", id: "natuurkunde",     titel: "Natuurkunde",     icoon: "⚛️", kleur: "blauw",  practiceKey: "duru_2627_natuurkunde_v1",     examKey: "duru_2627_natuurkunde_examens_v1" },
    { jaar: "2026-2027", id: "scheikunde",      titel: "Scheikunde",      icoon: "🧪", kleur: "teal",   practiceKey: "duru_2627_scheikunde_v1",      examKey: "duru_2627_scheikunde_examens_v1" },
    { jaar: "2026-2027", id: "biologie",        titel: "Biologie",        icoon: "🧬", kleur: "groen",  practiceKey: "duru_2627_biologie_v1",        examKey: "duru_2627_biologie_examens_v1" },
    { jaar: "2026-2027", id: "geschiedenis",    titel: "Geschiedenis",    icoon: "🕰️", kleur: "oranje", practiceKey: "duru_2627_geschiedenis_v1",    examKey: "duru_2627_geschiedenis_examens_v1" },
    { jaar: "2026-2027", id: "aardrijkskunde",  titel: "Aardrijkskunde",  icoon: "🗺️", kleur: "teal",   practiceKey: "duru_2627_aardrijkskunde_v1",  examKey: "duru_2627_aardrijkskunde_examens_v1" },
    { jaar: "2026-2027", id: "economie",        titel: "Economie",        icoon: "🏛️", kleur: "groen",  practiceKey: "duru_2627_economie_v1",        examKey: "duru_2627_economie_examens_v1" },
    { jaar: "2026-2027", id: "maatschappijleer",titel: "Maatschappijleer",icoon: "🏛️", kleur: "blauw",  practiceKey: "duru_2627_maatschappijleer_v1",examKey: "duru_2627_maatschappijleer_examens_v1" }
  ];

  function getActiveStudent() {
    var raw = localStorage.getItem("duru_active_user") || sessionStorage.getItem("duru_active_user");
    return raw ? raw.trim() : "duru";
  }

  function readStorageKey(logicalKey, user) {
    var val = localStorage.getItem(logicalKey);
    if (!val && user) {
      val = localStorage.getItem("user_" + user + "_" + logicalKey);
    }
    if (!val) {
      val = localStorage.getItem("user_duru_" + logicalKey);
    }
    if (!val) {
      try {
        for (var i = 0; i < localStorage.length; i++) {
          var k = localStorage.key(i);
          if (k === logicalKey || (k && k.indexOf(logicalKey) !== -1)) {
            val = localStorage.getItem(k);
            if (val) break;
          }
        }
      } catch (e) {}
    }
    if (!val) return null;
    try {
      return JSON.parse(val);
    } catch (e) {
      return null;
    }
  }

  function parseDate(dateStr) {
    if (!dateStr) return new Date();
    try {
      var parts = dateStr.split(" ");
      if (parts.length < 2) return new Date(dateStr);
      var dp = parts[0].split("-");
      var tp = parts[1].split(":");
      if (dp.length < 3 || tp.length < 2) return new Date(dateStr);
      return new Date(
        parseInt(dp[2], 10),
        parseInt(dp[1], 10) - 1,
        parseInt(dp[0], 10),
        parseInt(tp[0], 10),
        parseInt(tp[1], 10)
      );
    } catch (e) {
      return new Date(dateStr);
    }
  }

  function getPerformanceRating(avgCijfer, count) {
    if (count === 0 || !avgCijfer) return { label: "Henüz Sınav Yok", class: "rating-none", icon: "⏳" };
    if (avgCijfer >= 8.5) return { label: "Mükemmel / Çok Başarılı", class: "rating-excellent", icon: "🌟" };
    if (avgCijfer >= 7.0) return { label: "İyi / Başarılı", class: "rating-good", icon: "👍" };
    if (avgCijfer >= 5.5) return { label: "Geçer / Yeterli", class: "rating-pass", icon: "✔️" };
    return { label: "Geliştirilmeli (Tekrar)", class: "rating-warning", icon: "⚠️" };
  }

  function collectParentReportData(user, schoolJaar) {
    var studentName = user || getActiveStudent();
    var rows = VAK_CONFIG.filter(function (v) { return v.jaar === schoolJaar; });

    var totalXP = 0;
    var totalBadges = 0;
    var allAttempts = [];
    var vakReportList = [];
    var weakAreas = [];
    var strongAreas = [];
    var chapterReportList = [];

    rows.forEach(function (vak) {
      var pData = vak.practiceKey ? readStorageKey(vak.practiceKey, studentName) : null;
      var exData = vak.examKey ? readStorageKey(vak.examKey, studentName) : null;

      if (pData) {
        totalXP += pData.xp || 0;
        var b = pData.badges || {};
        totalBadges += Array.isArray(b) ? b.length : Object.keys(b).length;
      }

      var vakAttempts = [];
      if (vak.special === "begrijpend" && Array.isArray(exData)) {
        exData.forEach(function (att) {
          var score = att.score || 0;
          var tot = att.total || 10;
          var pct = Math.round((score / tot) * 100);
          var c = parseFloat(String(att.grade || "").replace(",", "."));
          if (isNaN(c)) c = 1 + (pct / 100) * 9;
          c = Math.round(c * 10) / 10;
          var item = {
            vakId: vak.id,
            vakTitel: vak.titel,
            vakIcoon: vak.icoon,
            hoofdstuk: 1,
            hoofdstukTitel: "Tekstanalyse & Begrip",
            hoofdstukIcoon: "🧠",
            titel: att.startingText || "Tekstanalyse",
            datumStr: att.timestamp || "",
            timestamp: new Date(att.timestamp || new Date()).getTime(),
            goed: score,
            totaal: tot,
            pct: pct,
            cijfer: c,
            geslaagd: c >= 5.5
          };
          vakAttempts.push(item);
          allAttempts.push(item);
        });
      } else if (exData && Array.isArray(exData.history)) {
        exData.history.forEach(function (att) {
          var pct = att.pct != null ? att.pct : Math.round((att.goed / (att.totaal || 10)) * 100);
          var c = 1 + (pct / 100) * 9;
          c = Math.round(c * 10) / 10;
          var hf = window.DURU_HF ? window.DURU_HF.vanAttempt(att, vak.id) : null;
          var item = {
            vakId: vak.id,
            vakTitel: vak.titel,
            vakIcoon: vak.icoon,
            hoofdstuk: hf ? hf.nr : null,
            hoofdstukTitel: hf ? hf.titel : "Diğer sınavlar",
            hoofdstukIcoon: hf ? hf.icoon : "📦",
            titel: att.examTitel || att.titel || "Proeftoets",
            datumStr: att.datum || "",
            timestamp: parseDate(att.datum).getTime(),
            goed: att.goed != null ? att.goed : 0,
            totaal: att.totaal != null ? att.totaal : 20,
            pct: pct,
            cijfer: c,
            geslaagd: c >= 5.5
          };
          vakAttempts.push(item);
          allAttempts.push(item);
        });
      }

      vakAttempts.sort(function (a, b) { return b.timestamp - a.timestamp; });

      var count = vakAttempts.length;
      var sumC = 0;
      var maxC = 0;
      var lastC = 0;
      var lastDatum = "-";

      if (count > 0) {
        vakAttempts.forEach(function (a) {
          sumC += a.cijfer;
          if (a.cijfer > maxC) maxC = a.cijfer;
          if (a.cijfer < 5.5) {
            weakAreas.push({
              vak: vak.titel,
              icoon: vak.icoon,
              hoofdstuk: a.hoofdstuk,
              hoofdstukTitel: a.hoofdstukTitel,
              toets: a.titel,
              cijfer: a.cijfer,
              datum: a.datumStr,
              pct: a.pct
            });
          } else if (a.cijfer >= 8.5) {
            strongAreas.push({
              vak: vak.titel,
              icoon: vak.icoon,
              hoofdstuk: a.hoofdstuk,
              hoofdstukTitel: a.hoofdstukTitel,
              toets: a.titel,
              cijfer: a.cijfer,
              datum: a.datumStr,
              pct: a.pct
            });
          }
        });
        lastC = vakAttempts[0].cijfer;
        lastDatum = vakAttempts[0].datumStr || "-";
      }

      var avgC = count > 0 ? (sumC / count) : 0;
      var pBeste = (pData && pData.beste) ? Object.keys(pData.beste).length : 0;
      var exBeste = (exData && exData.beste) ? Object.keys(exData.beste).length : 0;
      var completionPct = count > 0 ? Math.min(100, Math.round(((pBeste + exBeste) / Math.max(1, pBeste + 5)) * 100)) : 0;

      // Build subject chapters array — echte data uit het manifest (DURU_HF), geen gokwerk
      var chapterDefs = window.DURU_HF ? window.DURU_HF.lijst(vak.id) : [];
      var pogingenMap = (pData && pData.pogingen) ? pData.pogingen : {};
      var geoefendeTopicIds = Object.keys(pogingenMap).filter(function (tid) {
        return (pogingenMap[tid] || 0) > 0;
      });
      var chapterNrs = {};

      var subjectChapters = [];
      chapterDefs.forEach(function (ch) {
        chapterNrs[ch.nr] = true;

        var chAttempts = vakAttempts.filter(function (a) { return a.hoofdstuk === ch.nr; });
        var chCount = chAttempts.length;
        var chSum = 0;
        var chMax = 0;
        var chLast = 0;
        var chLastDate = "-";

        if (chCount > 0) {
          chAttempts.forEach(function (a) {
            chSum += a.cijfer;
            if (a.cijfer > chMax) chMax = a.cijfer;
          });
          chLast = chAttempts[0].cijfer;
          chLastDate = (chAttempts[0].datumStr || "-").split(" ")[0];
        }

        var chAvg = chCount > 0 ? (chSum / chCount) : 0;

        // Toetsvoortgang o.b.v. het echte aantal proeftoetsen uit het manifest
        var examIdSet = {};
        chAttempts.forEach(function (a) {
          var k = (a.examId && a.examId !== "") ? a.examId : a.titel;
          examIdSet[k] = true;
        });
        var uniekeExamens = Object.keys(examIdSet).length;
        var examTotaal = window.DURU_HF ? window.DURU_HF.totaalExamens(vak.id, ch.nr) : 0;
        var chProgressPct = examTotaal > 0 ? Math.min(100, Math.round((uniekeExamens / examTotaal) * 100)) : 0;

        // Oefenvoortgang: aantal onderwerpen met >=1 poging t.o.v. manifest-totaal
        var oefTotaal = window.DURU_HF ? window.DURU_HF.totaalOnderwerpen(vak.id, ch.nr) : 0;
        var oefGedaan = geoefendeTopicIds.filter(function (tid) {
          return window.DURU_HF && window.DURU_HF.vanOnderwerp(vak.id, tid) === ch.nr;
        }).length;
        var oefVoortgangPct = oefTotaal > 0 ? Math.min(100, Math.round((oefGedaan / oefTotaal) * 100)) : 0;

        var advice = "Henüz başlanmadı.";
        if (chCount > 0) {
          if (chAvg >= 8.5) advice = "Duru bu üniteyi tam anlamıyla kavramış. Okul sınavına hazır! 🌟";
          else if (chAvg >= 7.0) advice = "Başarılı ve iyi durumda. 1 deneme daha çözerek 9+ alabilir.";
          else if (chAvg >= 5.5) advice = "Geçer notta. Sınavdan önce yanlış yaptığı soruları gözden geçirmeli.";
          else advice = "⚠️ Tekrar önerilir! Bu ünitenin gramer/kelime testlerini 1 kez daha çözmeli.";
        }

        var chObj = {
          vakId: vak.id,
          vakTitel: vak.titel,
          vakIcoon: vak.icoon,
          vakKleur: vak.kleur,
          nr: ch.nr,
          titel: ch.titel,
          icoon: ch.icoon || "📖",
          thema: ch.intro || "",
          count: chCount,
          examTotaal: examTotaal,
          progressPct: chProgressPct,
          oefTotaal: oefTotaal,
          oefGedaan: oefGedaan,
          oefVoortgangPct: oefVoortgangPct,
          avgCijfer: chAvg,
          maxCijfer: chMax,
          lastCijfer: chLast,
          lastDatum: chLastDate,
          rating: getPerformanceRating(chAvg, chCount),
          advice: advice,
          attempts: chAttempts,
          overig: false
        };

        subjectChapters.push(chObj);
        chapterReportList.push(chObj);
      });

      // 📦 Diğer sınavlar: hiçbir hoofdstuk'a bağlanamayan pogingen
      var overigeAttempts = vakAttempts.filter(function (a) {
        return a.hoofdstuk == null || !chapterNrs[a.hoofdstuk];
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
        var ovLastDate = (overigeAttempts[0].datumStr || "-").split(" ")[0];

        var overigChObj = {
          vakId: vak.id,
          vakTitel: vak.titel,
          vakIcoon: vak.icoon,
          vakKleur: vak.kleur,
          nr: null,
          titel: "Diğer sınavlar",
          icoon: "📦",
          thema: "",
          count: overigeAttempts.length,
          examTotaal: 0,
          progressPct: 0,
          oefTotaal: 0,
          oefGedaan: 0,
          oefVoortgangPct: 0,
          avgCijfer: ovAvg,
          maxCijfer: ovMax,
          lastCijfer: ovLast,
          lastDatum: ovLastDate,
          rating: getPerformanceRating(ovAvg, overigeAttempts.length),
          advice: "Bu sınavlar henüz bir üniteyle eşleştirilemedi.",
          attempts: overigeAttempts,
          overig: true
        };

        subjectChapters.push(overigChObj);
        chapterReportList.push(overigChObj);
      }

      vakReportList.push({
        id: vak.id,
        titel: vak.titel,
        icoon: vak.icoon,
        kleur: vak.kleur,
        count: count,
        avgCijfer: avgC,
        maxCijfer: maxC,
        lastCijfer: lastC,
        lastDatum: lastDatum,
        completionPct: completionPct,
        rating: getPerformanceRating(avgC, count),
        chapterCount: chapterDefs.length,
        chapters: subjectChapters,
        attempts: vakAttempts
      });
    });

    allAttempts.sort(function (a, b) { return b.timestamp - a.timestamp; });

    var overallExamCount = allAttempts.length;
    var overallSum = 0;
    allAttempts.forEach(function (a) { overallSum += a.cijfer; });
    var overallAvg = overallExamCount > 0 ? (overallSum / overallExamCount) : 0;
    var passedExams = allAttempts.filter(function (a) { return a.geslaagd; }).length;
    var passRate = overallExamCount > 0 ? Math.round((passedExams / overallExamCount) * 100) : 0;

    var nowTs = Date.now();
    var sevenDaysAgo = nowTs - (7 * 24 * 60 * 60 * 1000);
    var recent7DaysCount = allAttempts.filter(function (a) { return a.timestamp >= sevenDaysAgo; }).length;

    return {
      studentName: studentName,
      schoolJaar: schoolJaar,
      totalXP: totalXP,
      totalBadges: totalBadges,
      overallExamCount: overallExamCount,
      overallAvg: overallAvg,
      passRate: passRate,
      recent7DaysCount: recent7DaysCount,
      lastActivityDate: allAttempts.length > 0 ? allAttempts[0].datumStr : "-",
      vakken: vakReportList,
      chapters: chapterReportList,
      allAttempts: allAttempts,
      weakAreas: weakAreas,
      strongAreas: strongAreas
    };
  }

  function renderParentDashboard() {
    var container = document.getElementById("ouder-view");
    if (!container) return;

    var student = getActiveStudent();
    var report = collectParentReportData(student, selectedJaar);

    var rating = getPerformanceRating(report.overallAvg, report.overallExamCount);
    var avgStr = report.overallExamCount > 0 ? report.overallAvg.toFixed(1).replace(".", ",") : "—";

    var html = `
      <!-- ── Veli Başlık ve Kontrol Çubuğu ──────────────────────────── -->
      <div class="ouder-header-card">
        <div class="ouder-header-left">
          <div class="ouder-avatar">👨‍👧</div>
          <div>
            <h2 class="ouder-title">Duru'nun Başarı &amp; İlerleme Raporu</h2>
            <p class="ouder-subtitle">
              Öğrenci: <strong>${escapeHtml(student.toUpperCase())}</strong> · 
              Dönem: <strong>${escapeHtml(selectedJaar)} (${selectedJaar === "2026-2027" ? "HAVO 3" : "MAVO 2"})</strong>
            </p>
          </div>
        </div>

        <div class="ouder-header-actions">
          <div class="ouder-year-toggles">
            <button type="button" class="ouder-year-btn ${selectedJaar === "2026-2027" ? "active" : ""}" data-year="2026-2027">
              🎒 HAVO 3 (2026-2027)
            </button>
            <button type="button" class="ouder-year-btn ${selectedJaar === "2025-2026" ? "active" : ""}" data-year="2025-2026" style="opacity:${selectedJaar === "2025-2026" ? "1" : "0.7"};">
              📁 MAVO 2 (Arşiv)
            </button>
          </div>
          <button type="button" id="ouder-print-btn" class="ouder-btn-print" title="Yazdır / PDF Kaydet">
            🖨️ Raporu Yazdır / PDF İndir
          </button>
        </div>
      </div>

      <!-- ── 1. Üst Yönetici Özet Kartları (KPIs) ────────────────────── -->
      <div class="ouder-kpi-grid">
        <div class="ouder-kpi-card highlight">
          <span class="ouder-kpi-icon">🎓</span>
          <div class="ouder-kpi-info">
            <span class="ouder-kpi-label">Genel Not Ortalaması</span>
            <div class="ouder-kpi-val-row">
              <span class="ouder-kpi-val">${avgStr}</span>
              <span class="ouder-kpi-badge ${rating.class}">${rating.label}</span>
            </div>
            <span class="ouder-kpi-sub">Hollanda Not Skalası (1.0 – 10.0)</span>
          </div>
        </div>

        <div class="ouder-kpi-card">
          <span class="ouder-kpi-icon">📝</span>
          <div class="ouder-kpi-info">
            <span class="ouder-kpi-label">Toplam Çözülen Deneme</span>
            <span class="ouder-kpi-val">${report.overallExamCount} <small style="font-size:14px;color:var(--grijs-licht);">Sınav</small></span>
            <span class="ouder-kpi-sub">Başarı Oranı: <strong>%${report.passRate}</strong> Geçti (≥5.5)</span>
          </div>
        </div>

        <div class="ouder-kpi-card">
          <span class="ouder-kpi-icon">⚡</span>
          <div class="ouder-kpi-info">
            <span class="ouder-kpi-label">Kazanılan Emek &amp; XP</span>
            <span class="ouder-kpi-val">${report.totalXP.toLocaleString()} <small style="font-size:14px;color:var(--grijs-licht);">XP</small></span>
            <span class="ouder-kpi-sub">Kazanılan Rozetler: <strong>${report.totalBadges} Medalya</strong> 🏅</span>
          </div>
        </div>

        <div class="ouder-kpi-card">
          <span class="ouder-kpi-icon">📅</span>
          <div class="ouder-kpi-info">
            <span class="ouder-kpi-label">Son Çalışma &amp; Ritim</span>
            <span class="ouder-kpi-val" style="font-size:18px;line-height:1.4;">${report.lastActivityDate !== "-" ? report.lastActivityDate : "Henüz Kayıt Yok"}</span>
            <span class="ouder-kpi-sub">Son 7 Günde: <strong>${report.recent7DaysCount} Sınav Çözüldü</strong> 🔥</span>
          </div>
        </div>
      </div>

      <!-- ── 2. Akıllı Veli Destek & Uyarı Kutusu (Aandachtspunten) ───── -->
      <div class="ouder-insight-card ${report.weakAreas.length > 0 ? "has-alerts" : "all-clear"}">
        <div class="ouder-insight-header">
          <span class="ouder-insight-icon">${report.weakAreas.length > 0 ? "⚠️" : "🌟"}</span>
          <div>
            <h3 class="ouder-insight-title">${report.weakAreas.length > 0 ? "Baba İçin Dikkat & Tekrar Önerilen Konular" : "Harika Gidiyor! Tüm Sınavlarda Başarılı"}</h3>
            <p class="ouder-insight-desc">
              ${report.weakAreas.length > 0 
                ? "Duru'nun 5.5 barajının altında kaldığı ünite ve sınavlar aşağıda listelenmiştir. Bu sınavları 1 kez daha çözmesi okul sınavı için büyük avantaj sağlayacaktır."
                : "Duru girdiği tüm deneme sınavlarında 5.5 barajını başarıyla aşmıştır. Çalışma temposunu düzenli tutması başarısını perçinleyecektir."}
            </p>
          </div>
        </div>
        ${report.weakAreas.length > 0 ? `
          <div class="ouder-alerts-list">
            ${report.weakAreas.map(function(w) {
              return `
                <div class="ouder-alert-item">
                  <span class="ouder-alert-vak">${w.icoon} ${escapeHtml(w.vak)} · ${w.hoofdstuk != null ? ("H" + w.hoofdstuk) : "📦"}</span>
                  <span class="ouder-alert-toets"><strong>${escapeHtml(w.toets)}</strong></span>
                  <span class="ouder-alert-grade">${w.cijfer.toFixed(1).replace(".", ",")} <small>(%${w.pct})</small></span>
                  <span class="ouder-alert-date">${escapeHtml(w.datum)}</span>
                </div>
              `;
            }).join("")}
          </div>
        ` : ""}
      </div>

      <!-- ── 3. Ders Bazında Genel Başarı Karnesi (Tıklandığında Ünite ve Sınav Kırılımlı) ── -->
      <section class="ouder-section" style="margin-top:28px;">
        <div class="ouder-section-header">
          <div>
            <h3>📊 Ders Bazında Genel Başarı Karnesi</h3>
            <small>Bir derse tıklayarak o derste çözülen sınavları ve <strong>ünite kırılımlarını</strong> anında açabilirsiniz</small>
          </div>
        </div>

        <div class="ouder-table-wrapper">
          <table class="ouder-table">
            <thead>
              <tr>
                <th>Ders</th>
                <th>Tamamlanma</th>
                <th>Çözülen Sınav</th>
                <th>En Yüksek Not</th>
                <th>Son Not</th>
                <th>Ders Ortalaması</th>
                <th>Durum &amp; Kırılım</th>
              </tr>
            </thead>
            <tbody>
              ${report.vakken.map(function(v) {
                var avgGrade = v.count > 0 ? v.avgCijfer.toFixed(1).replace(".", ",") : "—";
                var maxGrade = v.count > 0 ? v.maxCijfer.toFixed(1).replace(".", ",") : "—";
                var lastGrade = v.count > 0 ? v.lastCijfer.toFixed(1).replace(".", ",") : "—";
                
                var breakdownHtml = `
                  <tr id="ouder-breakdown-${v.id}" class="ouder-vak-breakdown-row" style="display:none;">
                    <td colspan="7" class="ouder-vak-breakdown-cell">
                      <div class="ouder-breakdown-container">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                          <h4 style="margin:0;font-size:15px;color:var(--hub-hoofd);font-weight:800;">
                            ${v.icoon} ${escapeHtml(v.titel)} — Ünite ve Sınav Kırılımları
                          </h4>
                          <span style="font-size:12px;color:var(--grijs);">Toplam ${v.count} sınav yapıldı</span>
                        </div>

                        ${v.chapters.map(function(ch) {
                          var chAvg = ch.count > 0 ? ch.avgCijfer.toFixed(1).replace(".", ",") : "—";
                          return `
                            <div class="ouder-chapter-card">
                              <div class="ouder-chapter-header">
                                <div class="ouder-chapter-title">
                                  <span>${ch.icoon}</span>
                                  <span>${ch.overig ? escapeHtml(ch.titel) : ("Hoofdstuk " + ch.nr + ": " + escapeHtml(ch.titel))}</span>
                                  ${ch.thema ? `<span style="font-size:12px;font-weight:normal;color:var(--grijs);">(${escapeHtml(ch.thema)})</span>` : ""}
                                </div>
                                <div style="display:flex;align-items:center;gap:8px;">
                                  <span class="ouder-grade-pill ${ch.count > 0 && ch.avgCijfer >= 5.5 ? "pass" : (ch.count > 0 ? "fail" : "none")}">
                                    Ünite Ortalaması: ${chAvg}
                                  </span>
                                  <span style="font-size:12px;font-weight:700;color:var(--grijs);">(${ch.examTotaal > 0 ? (ch.count + "/" + ch.examTotaal + " sınav") : (ch.count + " sınav")})</span>
                                </div>
                              </div>

                              ${ch.oefTotaal > 0 ? `
                                <div style="display:flex;align-items:center;gap:8px;padding:2px 0 8px;font-size:12px;color:var(--grijs);">
                                  <span>🔁 Oefenvoortgang:</span>
                                  <div class="ouder-progress-bar" style="width:80px;"><div class="ouder-progress-fill" style="width:${ch.oefVoortgangPct}%;"></div></div>
                                  <span>${ch.oefGedaan}/${ch.oefTotaal} onderwerpen (%${ch.oefVoortgangPct})</span>
                                </div>
                              ` : ""}

                              ${ch.attempts.length > 0 ? `
                                <table class="ouder-exam-table">
                                  <thead>
                                    <tr>
                                      <th>Sınav Adı</th>
                                      <th>Doğru / Toplam</th>
                                      <th>Başarı (%)</th>
                                      <th>Not (Cijfer)</th>
                                      <th>Sınav Tarihi</th>
                                      <th>Sonuç</th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                    ${ch.attempts.map(function(att) {
                                      return `
                                        <tr>
                                          <td><strong>${escapeHtml(att.titel)}</strong></td>
                                          <td>${att.goed} / ${att.totaal}</td>
                                          <td>%${att.pct}</td>
                                          <td><strong style="color:${att.geslaagd ? 'var(--groen)' : 'var(--oranje)'};font-size:14px;">${att.cijfer.toFixed(1).replace(".", ",")}</strong></td>
                                          <td style="color:var(--grijs);font-size:12px;">${escapeHtml(att.datumStr)}</td>
                                          <td>
                                            <span class="ouder-grade-pill ${att.geslaagd ? "pass" : "fail"}">
                                              ${att.geslaagd ? "✅ Başarılı" : "❌ Tekrar Et"}
                                            </span>
                                          </td>
                                        </tr>
                                      `;
                                    }).join("")}
                                  </tbody>
                                </table>
                              ` : `
                                <div style="padding:8px 10px;font-size:12px;color:var(--grijs-licht);font-style:italic;">
                                  ⏳ Bu üniteden henüz sınav çözülmedi${ch.examTotaal > 0 ? " (" + ch.examTotaal + " deneme sınavı hazır)" : ""}.
                                </div>
                              `}
                            </div>
                          `;
                        }).join("")}
                      </div>
                    </td>
                  </tr>
                `;

                return `
                  <tr class="ouder-vak-row-clickable" onclick="window.toggleOuderVakBreakdown('${v.id}')">
                    <td>
                      <div class="ouder-vak-cell">
                        <span class="ouder-vak-ico">${v.icoon}</span>
                        <div>
                          <strong>${escapeHtml(v.titel)}</strong><br>
                          <small style="color:var(--hub-hoofd);font-weight:700;">${v.chapterCount} Ünite</small>
                        </div>
                      </div>
                    </td>
                    <td style="min-width:130px;">
                      <div class="ouder-progress-wrap">
                        <div class="ouder-progress-bar"><div class="ouder-progress-fill" style="width:${v.completionPct}%;"></div></div>
                        <span class="ouder-progress-text">%${v.completionPct}</span>
                      </div>
                    </td>
                    <td><strong>${v.count}</strong> sınav</td>
                    <td><span class="ouder-badge-subtle">${maxGrade}</span></td>
                    <td>${lastGrade}</td>
                    <td>
                      <span class="ouder-grade-pill ${v.count > 0 && v.avgCijfer >= 5.5 ? "pass" : (v.count > 0 ? "fail" : "none")}">
                        ${avgGrade}
                      </span>
                    </td>
                    <td>
                      <button type="button" class="ouder-btn-breakdown" id="btn-toggle-${v.id}" onclick="event.stopPropagation(); window.toggleOuderVakBreakdown('${v.id}');">
                        🔍 Sınav &amp; Ünite Kırılımı ▾
                      </button>
                    </td>
                  </tr>
                  ${breakdownHtml}
                `;
              }).join("")}
            </tbody>
          </table>
        </div>
      </section>

      <!-- ── 4. Hoofdstuk (Ünite) Bazında Teşhis & Başarı Karnesi ─────── -->
      <section class="ouder-section" style="margin-top:28px;">
        <div class="ouder-section-header">
          <div>
            <h3>📖 Hoofdstuk (Ünite) Bazında Teşhis &amp; Başarı Karnesi</h3>
            <small>Okul sınavları ünite bazında yapıldığı için her ünitenin durumu ayrı takip edilir</small>
          </div>
        </div>

        <div class="ouder-table-wrapper">
          <table class="ouder-table">
            <thead>
              <tr>
                <th>Ders &amp; Ünite</th>
                <th>Ünite Konusu</th>
                <th>Toets İlerleme</th>
                <th>Oefen İlerleme</th>
                <th>Çözülen Sınav</th>
                <th>En İyi Not</th>
                <th>Son Not</th>
                <th>Ünite Notu</th>
                <th>Durum &amp; Veli Tavsiyesi</th>
              </tr>
            </thead>
            <tbody>
              ${report.chapters.map(function(ch) {
                var chAvgStr = ch.count > 0 ? ch.avgCijfer.toFixed(1).replace(".", ",") : "—";
                var chMaxStr = ch.count > 0 ? ch.maxCijfer.toFixed(1).replace(".", ",") : "—";
                var chLastStr = ch.count > 0 ? ch.lastCijfer.toFixed(1).replace(".", ",") : "—";
                return `
                  <tr>
                    <td>
                      <div class="ouder-vak-cell">
                        <span class="ouder-vak-ico">${ch.vakIcoon}</span>
                        <div>
                          <strong>${escapeHtml(ch.vakTitel)}</strong><br>
                          <span style="font-size:12px;color:var(--hub-hoofd);font-weight:700;">${ch.overig ? escapeHtml(ch.titel) : ("H" + ch.nr + ": " + escapeHtml(ch.titel))}</span>
                        </div>
                      </div>
                    </td>
                    <td style="font-size:12px;color:var(--grijs);max-width:200px;">
                      ${escapeHtml(ch.thema || (ch.overig ? "" : "Genel"))}
                    </td>
                    <td style="min-width:110px;">
                      <div class="ouder-progress-wrap">
                        <div class="ouder-progress-bar"><div class="ouder-progress-fill" style="width:${ch.progressPct}%;"></div></div>
                        <span class="ouder-progress-text">%${ch.progressPct}</span>
                      </div>
                    </td>
                    <td style="min-width:110px;">
                      ${ch.oefTotaal > 0 ? `
                        <div class="ouder-progress-wrap">
                          <div class="ouder-progress-bar"><div class="ouder-progress-fill" style="width:${ch.oefVoortgangPct}%;"></div></div>
                          <span class="ouder-progress-text">%${ch.oefVoortgangPct}</span>
                        </div>
                      ` : `<span style="color:var(--grijs-licht);font-size:12px;">—</span>`}
                    </td>
                    <td><strong>${ch.count}</strong>${ch.examTotaal > 0 ? " / " + ch.examTotaal : ""}</td>
                    <td><span class="ouder-badge-subtle">${chMaxStr}</span></td>
                    <td>${chLastStr}</td>
                    <td>
                      <span class="ouder-grade-pill ${ch.count > 0 && ch.avgCijfer >= 5.5 ? "pass" : (ch.count > 0 ? "fail" : "none")}">
                        ${chAvgStr}
                      </span>
                    </td>
                    <td>
                      <div style="display:flex;flex-direction:column;gap:4px;">
                        <span class="ouder-rating-badge ${ch.rating.class}" style="align-self:flex-start;">
                          ${ch.rating.icon} ${ch.rating.label}
                        </span>
                        <span style="font-size:11px;color:var(--grijs);font-style:italic;">${ch.advice}</span>
                      </div>
                    </td>
                  </tr>
                `;
              }).join("")}
            </tbody>
          </table>
        </div>
      </section>

      <!-- ── 5. Son Sınavlar ve Detaylı Çalışma Günlüğü ───────────────── -->
      <section class="ouder-section" style="margin-top:28px;">
        <div class="ouder-section-header">
          <h3>📋 Detaylı Sınav ve Aktivite Günlüğü</h3>
          <small>Tarihe göre sıralı tüm deneme sonuçları</small>
        </div>

        <div class="ouder-table-wrapper">
          <table class="ouder-table">
            <thead>
              <tr>
                <th>Tarih &amp; Saat</th>
                <th>Ders</th>
                <th>Hoofdstuk</th>
                <th>Sınav / Konu</th>
                <th>Doğru / Toplam Soru</th>
                <th>Başarı (%)</th>
                <th>Not (Cijfer)</th>
                <th>Sonuç</th>
              </tr>
            </thead>
            <tbody>
              ${report.allAttempts.length === 0 ? `
                <tr>
                  <td colspan="8" style="text-align:center;padding:32px;color:var(--grijs-licht);">
                    Bu dönem için henüz tamamlanmış sınav kaydı bulunmamaktadır.
                  </td>
                </tr>
              ` : report.allAttempts.map(function(att, idx) {
                return `
                  <tr>
                    <td style="color:var(--grijs);font-size:13px;">${escapeHtml(att.datumStr)}</td>
                    <td>
                      <span class="ouder-badge-subtle">${escapeHtml(att.vakIcoon || "")} ${escapeHtml(att.vakTitel)}</span>
                    </td>
                    <td><span class="chapter-badge">${escapeHtml(att.hoofdstukIcoon || "📖")} ${att.hoofdstuk != null ? ("H" + att.hoofdstuk) : "Overig"}</span></td>
                    <td><strong>${escapeHtml(att.titel)}</strong></td>
                    <td>${att.goed} / ${att.totaal}</td>
                    <td>%${att.pct}</td>
                    <td><strong style="color:${att.geslaagd ? 'var(--groen)' : 'var(--oranje)'};">${att.cijfer.toFixed(1).replace(".", ",")}</strong></td>
                    <td>
                      <span class="ouder-grade-pill ${att.geslaagd ? "pass" : "fail"}">
                        ${att.geslaagd ? "✅ Başarılı" : "❌ Tekrar Et"}
                      </span>
                    </td>
                  </tr>
                `;
              }).join("")}
            </tbody>
          </table>
        </div>
      </section>
    `;

    container.innerHTML = html;

    bindParentEvents();
  }

  function toggleOuderVakBreakdown(vakId) {
    var row = document.getElementById("ouder-breakdown-" + vakId);
    var btn = document.getElementById("btn-toggle-" + vakId);
    if (!row) return;

    var isHidden = row.style.display === "none";
    row.style.display = isHidden ? "table-row" : "none";
    if (btn) {
      btn.innerHTML = isHidden ? "▴ Kapat" : "🔍 Sınav &amp; Ünite Kırılımı ▾";
    }
  }
  window.toggleOuderVakBreakdown = toggleOuderVakBreakdown;

  function bindParentEvents() {
    var yearButtons = document.querySelectorAll(".ouder-year-btn");
    yearButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        selectedJaar = btn.getAttribute("data-year");
        renderParentDashboard();
      });
    });

    var printBtn = document.getElementById("ouder-print-btn");
    if (printBtn) {
      printBtn.addEventListener("click", function () {
        window.print();
      });
    }
  }

  function escapeHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  window.renderParentDashboard = renderParentDashboard;
  window.collectParentReportData = collectParentReportData;

})();
