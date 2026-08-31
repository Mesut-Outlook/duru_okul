/* =========================================================
   Duru's Schoolhub — Veli / Baba Takip & İlerleme Paneli
   (Parent / Father Progress Monitoring Dashboard & Report)
   ========================================================= */

(function () {
  "use strict";

  var HUIDIG_JAAR = "2026-2027";
  var selectedJaar = HUIDIG_JAAR;
  var selectedUser = null;

  var VAK_CONFIG = [
    // 2026-2027 (HAVO 3)
    { jaar: "2026-2027", id: "economie",        titel: "Economie",        icoon: "🏛️", kleur: "groen",  practiceKey: "duru_2627_economie_v1",        examKey: "duru_2627_economie_examens_v1" },
    { jaar: "2026-2027", id: "wiskunde",        titel: "Wiskunde",        icoon: "⚖️", kleur: "teal",   practiceKey: "duru_2627_wiskunde_v1",        examKey: "duru_2627_wiskunde_examens_v1" },
    { jaar: "2026-2027", id: "natuurkunde",     titel: "Natuurkunde",     icoon: "⚛️", kleur: "blauw",  practiceKey: "duru_2627_natuurkunde_v1",     examKey: "duru_2627_natuurkunde_examens_v1" },
    { jaar: "2026-2027", id: "biologie",        titel: "Biologie",        icoon: "🧬", kleur: "groen",  practiceKey: "duru_2627_biologie_v1",        examKey: "duru_2627_biologie_examens_v1" },
    { jaar: "2026-2027", id: "scheikunde",      titel: "Scheikunde",      icoon: "🧪", kleur: "teal",   practiceKey: "duru_2627_scheikunde_v1",      examKey: "duru_2627_scheikunde_examens_v1" },
    { jaar: "2026-2027", id: "geschiedenis",    titel: "Geschiedenis",    icoon: "🕰️", kleur: "oranje", practiceKey: "duru_2627_geschiedenis_v1",    examKey: "duru_2627_geschiedenis_examens_v1" },
    { jaar: "2026-2027", id: "aardrijkskunde",  titel: "Aardrijkskunde",  icoon: "🗺️", kleur: "teal",   practiceKey: "duru_2627_aardrijkskunde_v1",  examKey: "duru_2627_aardrijkskunde_examens_v1" },
    { jaar: "2026-2027", id: "nederlands",      titel: "Nederlands",      icoon: "📖", kleur: "oranje", practiceKey: "duru_2627_nederlands_v1",      examKey: "duru_2627_nederlands_examens_v1" },
    { jaar: "2026-2027", id: "engels",          titel: "Engels",          icoon: "🇬🇧", kleur: "oranje", practiceKey: "duru_2627_engels_v1",          examKey: "duru_2627_engels_examens_v1" },
    { jaar: "2026-2027", id: "frans",           titel: "Frans",           icoon: "🇫🇷", kleur: "oranje", practiceKey: "duru_2627_frans_v1",           examKey: "duru_2627_frans_examens_v1" },
    { jaar: "2026-2027", id: "duits",           titel: "Duits",           icoon: "🇩🇪", kleur: "oranje", practiceKey: "duru_2627_duits_v1",           examKey: "duru_2627_duits_examens_v1" },
    { jaar: "2026-2027", id: "maatschappijleer",titel: "Maatschappijleer",icoon: "🏛️", kleur: "blauw",  practiceKey: "duru_2627_maatschappijleer_v1",examKey: "duru_2627_maatschappijleer_examens_v1" },

    // 2025-2026 (MAVO 2 Archive)
    { jaar: "2025-2026", id: "economie",        titel: "Economie",        icoon: "💶", kleur: "groen",  practiceKey: "duru_economi_v1",             examKey: "duru_economi_examens_v1" },
    { jaar: "2025-2026", id: "geschiedenis",    titel: "Geschiedenis",    icoon: "🕰️", kleur: "oranje", practiceKey: "duru_geschiedenis_v1",        examKey: "duru_geschiedenis_examens_v1" },
    { jaar: "2025-2026", id: "natuurkunde",     titel: "Natuurkunde (NASK)",icoon: "⚛️", kleur: "blauw",practiceKey: "duru_nask_v1",                examKey: "duru_nask_examens_v1" },
    { jaar: "2025-2026", id: "wiskunde",        titel: "Wiskunde",        icoon: "⚖️", kleur: "teal",   practiceKey: "duru_wiskunde_v1",            examKey: "duru_wiskunde_examens_v1" },
    { jaar: "2025-2026", id: "nederlands-spelling",titel: "Spelling",     icoon: "✍️", kleur: "oranje", practiceKey: "duru_nederlands_spelling_v1", examKey: "duru_nederlands_spelling_examens_v1" },
    { jaar: "2025-2026", id: "nederlands-begrijpend",titel: "Begrijpend Lezen",icoon: "🧠", kleur: "oranje", practiceKey: null,                          examKey: "begrijpend_lezen_history", special: "begrijpend" }
  ];

  function getActiveStudent() {
    return selectedUser || localStorage.getItem("duru_active_user") || sessionStorage.getItem("duru_active_user") || "duru";
  }

  function readStorageKey(rawKey, user) {
    var u = user || getActiveStudent();
    var prefixedKey = "user_" + u + "_" + rawKey;
    var val = localStorage.getItem(prefixedKey);
    if (!val) {
      val = localStorage.getItem(rawKey);
    }
    if (!val) return null;
    try {
      return JSON.parse(val);
    } catch (e) {
      return null;
    }
  }

  function parseDate(datumStr) {
    if (!datumStr) return new Date();
    try {
      var parts = datumStr.split(" ");
      if (parts.length >= 2) {
        var dParts = parts[0].split("-");
        var tParts = parts[1].split(":");
        if (dParts.length === 3 && tParts.length >= 2) {
          return new Date(parseInt(dParts[2], 10), parseInt(dParts[1], 10) - 1, parseInt(dParts[0], 10), parseInt(tParts[0], 10), parseInt(tParts[1], 10));
        }
      }
      return new Date(datumStr);
    } catch (e) {
      return new Date();
    }
  }

  function getPerformanceRating(avgCijfer, examCount) {
    if (examCount === 0) return { label: "Henüz Başlanmadı", color: "#9ca3af", icon: "⏳", class: "status-none" };
    if (avgCijfer >= 8.5) return { label: "Üstün Başarılı (Mükemmel)", color: "#16a34a", icon: "🌟", class: "status-excellent" };
    if (avgCijfer >= 7.0) return { label: "Çok İyi", color: "#0d9488", icon: "👍", class: "status-good" };
    if (avgCijfer >= 5.5) return { label: "Geçer / Başarılı", color: "#2563eb", icon: "✔️", class: "status-pass" };
    return { label: "Destek & Tekrar Önerilir", color: "#dc2626", icon: "⚠️", class: "status-warning" };
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

    rows.forEach(function (vak) {
      var pData = vak.practiceKey ? readStorageKey(vak.practiceKey, studentName) : null;
      var exData = vak.examKey ? readStorageKey(vak.examKey, studentName) : null;

      // XP & Badges
      if (pData) {
        totalXP += pData.xp || 0;
        var b = pData.badges || {};
        totalBadges += Array.isArray(b) ? b.length : Object.keys(b).length;
      }

      // History
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
          var item = {
            vakId: vak.id,
            vakTitel: vak.titel,
            vakIcoon: vak.icoon,
            titel: att.examTitel || "Proeftoets",
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

      // Sort vak attempts descending
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
              toets: a.titel,
              cijfer: a.cijfer,
              datum: a.datumStr,
              pct: a.pct
            });
          } else if (a.cijfer >= 8.5) {
            strongAreas.push({
              vak: vak.titel,
              icoon: vak.icoon,
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
        rating: getPerformanceRating(avgC, count)
      });
    });

    allAttempts.sort(function (a, b) { return b.timestamp - a.timestamp; });

    var overallExamCount = allAttempts.length;
    var overallSum = 0;
    allAttempts.forEach(function (a) { overallSum += a.cijfer; });
    var overallAvg = overallExamCount > 0 ? (overallSum / overallExamCount) : 0;
    var passedExams = allAttempts.filter(function (a) { return a.geslaagd; }).length;
    var passRate = overallExamCount > 0 ? Math.round((passedExams / overallExamCount) * 100) : 0;

    // Recent 7 days activity
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

        <div class="ouder-actions">
          <div class="ouder-year-toggles">
            <button type="button" class="ouder-year-btn ${selectedJaar === "2026-2027" ? "active" : ""}" data-year="2026-2027">
              🎒 HAVO 3 (2026-2027)
            </button>
            <button type="button" class="ouder-year-btn ${selectedJaar === "2025-2026" ? "active" : ""}" data-year="2025-2026">
              📚 MAVO 2 (2025-2026)
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
                ? "Duru'nun 5.5 barajının altında kaldığı konular aşağıda listelenmiştir. Bu sınavları 1 kez daha çözmesi tavsiye edilir."
                : "Duru girdiği tüm deneme sınavlarında 5.5 barajını başarıyla aşmıştır. Çalışma temposunu düzenli tutması başarısını perçinleyecektir."}
            </p>
          </div>
        </div>
        ${report.weakAreas.length > 0 ? `
          <div class="ouder-alerts-list">
            ${report.weakAreas.map(function(w) {
              return `
                <div class="ouder-alert-item">
                  <span class="ouder-alert-vak">${w.icoon} ${escapeHtml(w.vak)}</span>
                  <span class="ouder-alert-toets"><strong>${escapeHtml(w.toets)}</strong></span>
                  <span class="ouder-alert-grade">${w.cijfer.toFixed(1).replace(".", ",")} <small>(%${w.pct})</small></span>
                  <span class="ouder-alert-date">${escapeHtml(w.datum)}</span>
                </div>
              `;
            }).join("")}
          </div>
        ` : ""}
      </div>

      <!-- ── 3. Ders Bazında Başarı Karnesi (Vakken Rapport) ─────────── -->
      <section class="ouder-section">
        <div class="ouder-section-header">
          <h3>📊 Ders Bazında Başarı Karnesi</h3>
          <small>${selectedJaar} Dönemi Tüm Dersler</small>
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
                <th>Durum Değerlendirmesi</th>
              </tr>
            </thead>
            <tbody>
              ${report.vakken.map(function(v) {
                var avgGrade = v.count > 0 ? v.avgCijfer.toFixed(1).replace(".", ",") : "—";
                var maxGrade = v.count > 0 ? v.maxCijfer.toFixed(1).replace(".", ",") : "—";
                var lastGrade = v.count > 0 ? v.lastCijfer.toFixed(1).replace(".", ",") : "—";
                return `
                  <tr>
                    <td>
                      <div class="ouder-vak-cell">
                        <span class="ouder-vak-ico">${v.icoon}</span>
                        <strong>${escapeHtml(v.titel)}</strong>
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
                      <span class="ouder-rating-badge ${v.rating.class}">
                        ${v.rating.icon} ${v.rating.label}
                      </span>
                    </td>
                  </tr>
                `;
              }).join("")}
            </tbody>
          </table>
        </div>
      </section>

      <!-- ── 4. Son Sınavlar ve Detaylı Çalışma Günlüğü ───────────────── -->
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
                    <td><strong>${escapeHtml(att.titel)}</strong></td>
                    <td>${att.goed} / ${att.totaal}</td>
                    <td>%${att.pct}</td>
                    <td><strong>${att.cijfer.toFixed(1).replace(".", ",")}</strong></td>
                    <td>
                      <span class="ouder-grade-pill ${att.geslaagd ? "pass" : "fail"}">
                        ${att.geslaagd ? "✅ Başarılı" : "❌ Tekrar Et"}
                      </span>
                    </td>
                    <td style="text-align:center;">
                      <button type="button" class="ouder-btn-delete-att" data-vak="${escapeHtml(att.vakId)}" data-datum="${escapeHtml(att.datumStr)}" data-titel="${escapeHtml(att.titel)}" title="Bu deneme kaydını sil" style="background:none;border:none;cursor:pointer;font-size:15px;padding:4px 8px;border-radius:6px;opacity:0.7;transition:all 0.15s ease;">
                        🗑️
                      </button>
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

    // Bind delete button listeners
    var deleteBtns = container.querySelectorAll(".ouder-btn-delete-att");
    deleteBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var vakId = btn.getAttribute("data-vak");
        var datumStr = btn.getAttribute("data-datum");
        var examTitel = btn.getAttribute("data-titel");

        if (confirm("'" + examTitel + " (" + datumStr + ")' sınav kaydını silmek istediğinizden emin misiniz?")) {
          deleteAttempt(vakId, datumStr, examTitel);
        }
      });
    });

    // Bind event listeners
    var printBtn = document.getElementById("ouder-print-btn");
    if (printBtn) {
      printBtn.addEventListener("click", function () {
        window.print();
      });
    }

    var yearBtns = container.querySelectorAll(".ouder-year-btn");
    yearBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        selectedJaar = btn.getAttribute("data-year");
        renderParentDashboard();
      });
    });
  }

  /**
   * Belirtilen sınav kaydını yerel depolamadan siler ve puanları yeniden hesaplar
   */
  function deleteAttempt(vakId, datumStr, examTitel) {
    var rows = VAK_CONFIG.filter(function (v) { return v.id === vakId; });
    var student = getActiveStudent();

    rows.forEach(function (vak) {
      if (!vak.examKey) return;

      var targetKeys = [
        vak.examKey,
        "user_" + student + "_" + vak.examKey,
        "user_duru_" + vak.examKey,
        "user_baba_" + vak.examKey
      ];

      targetKeys.forEach(function (key) {
        try {
          var raw = localStorage.getItem(key);
          if (!raw) return;
          var data = JSON.parse(raw);

          if (Array.isArray(data)) {
            // Begrijpend lezen
            data = data.filter(function (a) {
              return !(a.timestamp === datumStr || a.startingText === examTitel);
            });
            localStorage.setItem(key, JSON.stringify(data));
          } else if (data && Array.isArray(data.history)) {
            data.history = data.history.filter(function (a) {
              return !(a.datum === datumStr || (a.examTitel === examTitel && a.datum === datumStr));
            });

            // Recalculate beste and laatste
            data.beste = {};
            data.laatste = {};
            for (var i = data.history.length - 1; i >= 0; i--) {
              var att = data.history[i];
              if (att && att.examId) {
                if (data.beste[att.examId] == null || att.pct > data.beste[att.examId]) {
                  data.beste[att.examId] = att.pct;
                }
                data.laatste[att.examId] = att.pct;
              }
            }

            localStorage.setItem(key, JSON.stringify(data));
          }
        } catch (e) {
          console.warn("deleteAttempt error:", e);
        }
      });
    });

    // Re-render and push to Cloud
    renderParentDashboard();
    if (typeof window.renderVakken === "function") window.renderVakken();
    if (typeof window.loadDashboardData === "function") window.loadDashboardData();
    if (window.CloudSync && typeof window.CloudSync.push === "function") {
      window.CloudSync.push(true);
    }
  }

  /**
   * 29 Ağustos'taki hatalı / boş 0% test kayıtlarını otomatik temizler
   */
  function purgeInvalidTestAttempts() {
    var examKeys = [
      "duru_2627_biologie_examens_v1",
      "duru_biologie_examens_v1",
      "duru_nask_examens_v1"
    ];

    var userPrefixes = ["", "user_duru_", "user_baba_", "user_veli_", "user_mesut_"];

    examKeys.forEach(function (baseKey) {
      userPrefixes.forEach(function (prefix) {
        var fullKey = prefix + baseKey;
        try {
          var raw = localStorage.getItem(fullKey);
          if (!raw) return;
          var data = JSON.parse(raw);

          if (data && Array.isArray(data.history)) {
            var originalLen = data.history.length;
            data.history = data.history.filter(function (att) {
              // 0% ve 0 doğru olan 29 Ağustos denemelerini kaldır
              var isZero = (att.pct === 0 || att.goed === 0);
              var isTargetDate = att.datum && att.datum.indexOf("29-08-2026") !== -1;
              var isTargetToets = (att.examTitel && (att.examTitel.indexOf("Levensfasen") !== -1 || att.examTitel.indexOf("Cellen") !== -1));
              return !(isZero && isTargetDate && isTargetToets);
            });

            if (data.history.length !== originalLen) {
              // Recalculate
              data.beste = {};
              data.laatste = {};
              for (var i = data.history.length - 1; i >= 0; i--) {
                var a = data.history[i];
                if (a && a.examId) {
                  if (data.beste[a.examId] == null || a.pct > data.beste[a.examId]) {
                    data.beste[a.examId] = a.pct;
                  }
                  data.laatste[a.examId] = a.pct;
                }
              }
              localStorage.setItem(fullKey, JSON.stringify(data));
            }
          }
        } catch (e) {}
      });
    });
  }

  function escapeHtml(str) {
    return String(str == null ? "" : str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  // Hook into DOM Ready
  document.addEventListener("DOMContentLoaded", function () {
    purgeInvalidTestAttempts();

    // Check if parent tab was clicked
    var tabs = document.querySelectorAll(".hub-tab");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        if (tab.getAttribute("data-target") === "ouder-view") {
          renderParentDashboard();
        }
      });
    });

    // Auto-refresh when storage changes
    window.addEventListener("storage", function () {
      if (document.getElementById("ouder-view") && document.getElementById("ouder-view").classList.contains("active")) {
        renderParentDashboard();
      }
    });
  });

  window.renderParentDashboard = renderParentDashboard;
  window.purgeInvalidTestAttempts = purgeInvalidTestAttempts;

})();
