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

  // Vakregister komt uit js/vakken.js — zelfde bron als js/dashboard.js.
  var VAK_CONFIG = window.DURU_VAKKEN.alle;

  function getActiveStudent() {
    var raw = localStorage.getItem("duru_active_user") || sessionStorage.getItem("duru_active_user");
    return raw ? raw.trim() : "duru";
  }

  /* Ruwe lees: langs de prefix-override van landing.js heen.
     localStorage.getItem() plakt daar automatisch de ACTIEVE gebruiker voor de
     sleutel. Voor dit paneel is dat verkeerd: Baba kijkt, maar het rapport gaat
     over Duru. We adresseren de sleutels dus exact. */
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
       1. de leerling over wie het rapport gaat → user_<leerling>_<sleutel>
       2. sleutels van vóór multi-user          → <sleutel> zonder prefix
     De vorige versie eindigde met een scan door heel localStorage die op
     SUBSTRING matchte (k.indexOf(logicalKey) !== -1). Die kon
     'user_baba_duru_2627_engels_v1' teruggeven terwijl om Duru's cijfers werd
     gevraagd — andermans gegevens in het rapport. Raden is hier nooit beter
     dan niets vinden. */
  function readStorageKey(logicalKey, user) {
    var kandidaten = [];
    if (user) kandidaten.push("user_" + user + "_" + logicalKey);
    kandidaten.push(logicalKey);

    for (var i = 0; i < kandidaten.length; i++) {
      var val = leesRuw(kandidaten[i]);
      if (val) {
        try { return JSON.parse(val); } catch (e) { return null; }
      }
    }
    return null;
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
    if (avgCijfer >= window.DURU_CIJFER.TOP) return { label: "Mükemmel / Çok Başarılı", class: "rating-excellent", icon: "🌟" };
    if (avgCijfer >= window.DURU_CIJFER.GOED) return { label: "İyi / Başarılı", class: "rating-good", icon: "👍" };
    if (window.DURU_CIJFER.geslaagd(avgCijfer)) return { label: "Geçer / Yeterli", class: "rating-pass", icon: "✔️" };
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
          if (isNaN(c)) c = window.DURU_CIJFER.vanPct(pct);
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
            geslaagd: window.DURU_CIJFER.geslaagd(c)
          };
          vakAttempts.push(item);
          allAttempts.push(item);
        });
      } else if (exData && Array.isArray(exData.history)) {
        exData.history.forEach(function (att) {
          var pct = att.pct != null ? att.pct : Math.round((att.goed / (att.totaal || 10)) * 100);
          var c = window.DURU_CIJFER.vanPct(pct);
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
            geslaagd: window.DURU_CIJFER.geslaagd(c)
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
          if (!window.DURU_CIJFER.geslaagd(a.cijfer)) {
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
          } else if (window.DURU_CIJFER.examenklaar(a.cijfer)) {
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
          if (chAvg >= window.DURU_CIJFER.TOP) advice = "Duru bu üniteyi tam anlamıyla kavramış. Okul sınavına hazır! 🌟";
          else if (chAvg >= window.DURU_CIJFER.GOED) advice = "Başarılı ve iyi durumda. 1 deneme daha çözerek 9+ alabilir.";
          else if (window.DURU_CIJFER.geslaagd(chAvg)) advice = "Geçer notta. Sınavdan önce yanlış yaptığı soruları gözden geçirmeli.";
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

  /* ─────────────────────────────────────────────────────────
     Weergave — herontwerp 2026-09.
     Één leesvolgorde: status → cijferschaal → aandachtspunten
     → vakken, met detailweergaven achter tabs.
     ───────────────────────────────────────────────────────── */

  var actieveView = "overzicht";   // blijft bewaard tussen renders
  var gekozenVak  = null;
  var logFilter   = { q: "", vak: "", res: "" };
  var laatsteCtx  = null;          // laatst berekende rapport, voor het printrapport
  var printGekoppeld = false;      // beforeprint/afterprint maar één keer koppelen
  var printBezig  = false;

  /* Cijferlogica komt uit js/cijfer_util.js — formule en slaaggrens staan
     daar één keer. Hier alleen de vertaling naar de tokens van dit paneel. */
  var C = window.DURU_CIJFER;

  function fmtC(c) { return C.tekst(c); }
  function cijferKlasse(c, count) { return C.klasse(c, count); }
  function schaalPos(c) { return C.positie(c); }

  var KLASSE_KLEUR = {
    goed: "var(--ouder-goed)",
    net:  "var(--ouder-net)",
    zwak: "var(--ouder-zwak)",
    none: "var(--ouder-mut)"
  };

  function cijferKleur(c, count) {
    return KLASSE_KLEUR[C.klasse(c, count)];
  }
  function kortDatum(s) { var d = String(s || "").split(" ")[0]; return d || "—"; }
  function niveauVan(jaar) { return jaar === "2026-2027" ? "HAVO 3" : "MAVO 2"; }
  function hfChip(nr) {
    return '<span class="ouder-hf-chip">' + (nr != null ? "H" + nr : "—") + "</span>";
  }

  /* Toetsvoortgang van een vak: som over zijn hoofdstukken. */
  function vakVoortgang(v) {
    var tot = 0, gedaan = 0;
    v.chapters.forEach(function (c) {
      if (!c.examTotaal) return;
      tot += c.examTotaal;
      gedaan += Math.round((c.progressPct / 100) * c.examTotaal);
    });
    return { tot: tot, gedaan: gedaan, pct: tot > 0 ? Math.round((gedaan / tot) * 100) : 0 };
  }

  function miniSchaal(c, count) {
    return '' +
      '<span class="ouder-mini-schaal-wrap">' +
        '<span class="ouder-mini-schaal">' +
          '<span class="ouder-mini-schaal-vul" style="width:' + schaalPos(c) + '%;background:' + cijferKleur(c, count) + '"></span>' +
          '<span class="ouder-mini-schaal-drempel"></span>' +
        '</span>' +
        '<span class="ouder-mini-schaal-c" style="color:' + cijferKleur(c, count) + '">' +
          (count ? fmtC(c) : "—") +
        '</span>' +
      '</span>';
  }

  function pill(c, count, tekst) {
    return '<span class="ouder-pill ouder-pill--' + cijferKlasse(c, count) + '">' +
      (tekst != null ? tekst : (count ? fmtC(c) : "henüz yok")) + '</span>';
  }

  /* ── Cijferschaal: de Nederlandse 1–10 schaal als echt meetlint ── */
  function schaalHtml(report) {
    var h = '<div class="ouder-schaal-track"></div><div class="ouder-schaal-drempel"></div>';

    report.vakken.forEach(function (v) {
      if (!v.count) return;
      h += '<span class="ouder-schaal-vak" style="left:' + schaalPos(v.avgCijfer) + '%;background:' +
           cijferKleur(v.avgCijfer, v.count) + '" title="' + escapeHtml(v.titel) + ' — ' + fmtC(v.avgCijfer) + '"></span>';
    });

    if (report.overallExamCount > 0) {
      h += '<span class="ouder-schaal-mij" style="left:' + schaalPos(report.overallAvg) + '%;color:' +
           cijferKleur(report.overallAvg, 1) + '"><span class="ouder-schaal-mij-punt"></span></span>';
    }
    return h;
  }

  /* ── Weergave 1: Genel Bakış ─────────────────────────── */
  function viewOverzicht(report, zwakke, sterke) {
    var h = '<div class="ouder-odak">';

    h += '<section class="ouder-dikkat' + (zwakke.length ? '' : ' is-schoon') + '">';
    if (zwakke.length) {
      h += '<h3>Önce buraya bakın</h3>' +
           '<p class="ouder-dikkat-uitleg">Geçme sınırının (5,5) altında kalan üniteler. Her satır, Duru\'nun bu hafta tekrar etmesi gereken tek bir konuyu gösteriyor.</p>' +
           '<div class="ouder-dikkat-lijst">';
      zwakke.slice(0, 5).forEach(function (c) {
        h += '<div class="ouder-dikkat-rij">' +
               '<span class="ouder-dikkat-vak">' + (c.vakIcoon || "") + ' ' + escapeHtml(c.vakTitel) + ' ' + hfChip(c.nr) +
                 (daaltNog(c) ? ' <span class="ouder-daalt" title="Son denemeler öncekilerden daha düşük">düşüyor</span>' : '') + '</span>' +
               '<span class="ouder-dikkat-cijfer">' + fmtC(c.avgCijfer) +
                 '<small>' + c.count + ' deneme</small></span>' +
               '<span class="ouder-dikkat-actie">' + escapeHtml(c.titel) + ' — ' + escapeHtml(c.advice) + '</span>' +
             '</div>';
      });
      h += '</div>';
    } else if (report.overallExamCount > 0) {
      h += '<h3>Şu an tekrar gereken ünite yok</h3>' +
           '<p class="ouder-dikkat-uitleg">Tüm ünitelerin ortalaması geçme sınırının üstünde. Duru istikrarlı gidiyor.</p>';
    } else {
      h += '<h3>Bu dönem henüz kayıt yok</h3>' +
           '<p class="ouder-dikkat-uitleg">Duru bir proeftoets çözdüğünde sonuçlar burada belirir.</p>';
    }
    h += '</section>';

    var actieveVakTel = report.vakken.filter(function (v) { return v.count > 0; }).length;
    h += '<div class="ouder-zij">' +
      '<div class="ouder-mini">' +
        '<span class="ouder-mini-label">Son 7 gün</span>' +
        '<span class="ouder-mini-waarde">' + report.recent7DaysCount + '</span>' +
        '<span class="ouder-mini-sub">deneme çözüldü</span>' +
      '</div>' +
      '<div class="ouder-mini">' +
        '<span class="ouder-mini-label">Sınava hazır ünite</span>' +
        '<span class="ouder-mini-waarde">' + sterke.length + '</span>' +
        '<span class="ouder-mini-sub">ortalaması 8,5 ve üstü</span>' +
      '</div>' +
      '<div class="ouder-mini">' +
        '<span class="ouder-mini-label">Aktif ders</span>' +
        '<span class="ouder-mini-waarde">' + actieveVakTel +
          '<small> / ' + report.vakken.length + '</small></span>' +
        '<span class="ouder-mini-sub">bu yıl en az bir deneme çözülen</span>' +
      '</div>' +
      '<div class="ouder-mini">' +
        '<span class="ouder-mini-label">Emek</span>' +
        '<span class="ouder-mini-waarde">' + report.totalXP.toLocaleString("tr-TR") + '<small> XP</small></span>' +
        '<span class="ouder-mini-sub">' + report.totalBadges + ' rozet kazanıldı</span>' +
      '</div>' +
    '</div></div>';

    h += '<div class="ouder-sec-kop"><h3>Dersler</h3>' +
         '<p>En çok ilgi bekleyen ders en üstte. Bir derse tıklayın — ünite kırılımı açılır.</p></div>';

    var gesorteerd = report.vakken.slice().sort(function (a, b) {
      if (!a.count && b.count) return 1;
      if (a.count && !b.count) return -1;
      return a.avgCijfer - b.avgCijfer;
    });

    h += '<div class="ouder-vak-lijst">';
    gesorteerd.forEach(function (v) {
      var vg = vakVoortgang(v);
      h += '<button type="button" class="ouder-vak-rij" data-open-vak="' + escapeHtml(v.id) + '">' +
        '<span class="ouder-vak-naam">' +
          '<span class="ouder-vak-ico">' + (v.icoon || "") + '</span>' +
          '<span class="ouder-vak-tekst">' +
            '<span class="ouder-vak-titel">' + escapeHtml(v.titel) + '</span>' +
            '<span class="ouder-vak-meta">' + v.count + ' deneme · ' + v.chapterCount + ' ünite</span>' +
          '</span>' +
        '</span>' +
        miniSchaal(v.avgCijfer, v.count) +
        '<span class="ouder-spark-cel">' + sparkline(v.attempts) + trendHtml(v.attempts) + '</span>' +
        '<span class="ouder-voortgang">' +
          (vg.tot > 0 ? vg.gedaan + "/" + vg.tot + " proeftoets" : "—") +
          '<span class="ouder-voortgang-bar"><span class="ouder-voortgang-vul" style="width:' + vg.pct + '%"></span></span>' +
        '</span>' +
        '<span class="ouder-voortgang ouder-datum-cel">' + escapeHtml(kortDatum(v.lastDatum)) + '</span>' +
        '<span class="ouder-chev">›</span>' +
      '</button>';
    });
    h += '</div>';

    return h;
  }

  /* ── Weergave 2: Dersler ─────────────────────────────── */
  function viewVakken(report) {
    var h = '<div class="ouder-sec-kop"><h3>Ders detayı</h3>' +
            '<p>Bir ders seçin; üniteleri, ilerlemesi ve sınav geçmişi aşağıda.</p></div>';

    h += '<div class="ouder-chips">';
    report.vakken.forEach(function (v) {
      h += '<button type="button" class="ouder-chip" data-kies-vak="' + escapeHtml(v.id) + '" aria-pressed="' +
           (gekozenVak === v.id ? "true" : "false") + '">' + (v.icoon || "") + ' ' + escapeHtml(v.titel) +
           (v.count ? "" : ' <small>· boş</small>') + '</button>';
    });
    h += '</div>';

    var gekozen = null;
    report.vakken.forEach(function (v) { if (v.id === gekozenVak) gekozen = v; });
    if (!gekozen) {
      return h + '<div class="ouder-tabel-wrap"><div class="ouder-leeg">Yukarıdan bir ders seçin.</div></div>';
    }

    return h + vakDetailHtml(gekozen, true);
  }

  /* Eén vak volledig uitgeschreven. Gedeeld door de tab-weergave en het
     printrapport; het printrapport laat de toetsgeschiedenis weg, omdat het
     logboek verderop elke poging al opsomt. */
  function vakDetailHtml(gekozen, metGeschiedenis) {
    var h = '';
    var vg = vakVoortgang(gekozen);
    h += '<div class="ouder-vd-kop">' +
      '<span class="ouder-vak-ico ouder-vak-ico--groot">' + (gekozen.icoon || "") + '</span>' +
      '<div><h3>' + escapeHtml(gekozen.titel) + '</h3>' +
        '<span class="ouder-vak-meta">' + gekozen.chapterCount + ' ünite · ' + gekozen.count +
        ' deneme · son çalışma ' + escapeHtml(kortDatum(gekozen.lastDatum)) + '</span></div>' +
      '<div class="ouder-vd-stats">' +
        '<div><span class="ouder-vd-label">Ortalama</span>' +
          '<span class="ouder-vd-waarde" style="color:' + cijferKleur(gekozen.avgCijfer, gekozen.count) + '">' +
          (gekozen.count ? fmtC(gekozen.avgCijfer) : "—") + '</span></div>' +
        '<div><span class="ouder-vd-label">En iyi</span>' +
          '<span class="ouder-vd-waarde">' + (gekozen.count ? fmtC(gekozen.maxCijfer) : "—") + '</span></div>' +
        '<div><span class="ouder-vd-label">Proeftoets</span>' +
          '<span class="ouder-vd-waarde">' + (vg.tot > 0 ? vg.gedaan + "/" + vg.tot : "—") + '</span></div>' +
      '</div>' +
    '</div>';

    if (!gekozen.chapters.length) {
      h += '<div class="ouder-tabel-wrap"><div class="ouder-leeg">Bu ders için henüz ünite verisi yok.</div></div>';
    } else {
      h += '<div class="ouder-hf-grid">';
      gekozen.chapters.forEach(function (c) {
        var aandacht = c.count > 0 && !C.geslaagd(c.avgCijfer);
        h += '<article class="ouder-hf-kaart' + (aandacht ? " is-aandacht" : "") + '">' +
          '<div class="ouder-hf-kop">' +
            '<div>' +
              '<span class="ouder-hf-nr">' + (c.nr != null ? "Hoofdstuk " + c.nr : "Ünitesiz") + '</span>' +
              '<span class="ouder-hf-titel">' + escapeHtml(c.titel) + '</span>' +
            '</div>' +
            pill(c.avgCijfer, c.count) +
          '</div>' +
          '<div class="ouder-hf-stats">' +
            '<div><span class="ouder-hf-stat-label">Deneme</span>' +
              '<span class="ouder-hf-stat-waarde">' + c.count +
              (c.examTotaal > 0 ? " · %" + c.progressPct : "") + '</span></div>' +
            // Geen onderwerpen in dit vak? Dan is een lege balk geen informatie
            // maar ruis — die suggereert achterstand die er niet is (frans).
            (c.oefTotaal > 0
              ? '<div><span class="ouder-hf-stat-label">Alıştırma</span>' +
                '<span class="ouder-hf-stat-waarde">' + c.oefGedaan + "/" + c.oefTotaal + '</span></div>'
              : '') +
            '<div><span class="ouder-hf-stat-label">Son</span>' +
              '<span class="ouder-hf-stat-waarde">' +
              (c.count ? fmtC(c.lastCijfer) + " · " + escapeHtml(c.lastDatum) : "—") + '</span></div>' +
          '</div>' +
          '<p class="ouder-hf-advies">' + (aandacht ? "<b>Tekrar önerilir.</b> " : "") + escapeHtml(c.advice) + '</p>' +
        '</article>';
      });
      h += '</div>';
    }

    if (metGeschiedenis && gekozen.attempts.length) {
      h += '<div class="ouder-sec-kop"><h3>Sınav geçmişi</h3><p>' +
           escapeHtml(gekozen.titel) + ' · yeniden eskiye</p></div>';
      h += '<div class="ouder-tabel-wrap"><table class="ouder-tabel"><thead><tr>' +
        '<th class="ouder-streep"></th><th>Tarih</th><th>Ünite</th><th>Sınav</th>' +
        '<th>Doğru</th><th>Yüzde</th><th>Not</th></tr></thead><tbody>';
      gekozen.attempts.forEach(function (a) {
        h += '<tr>' +
          '<td class="ouder-streep" style="background:' + cijferKleur(a.cijfer, 1) + '"></td>' +
          '<td class="ouder-num">' + escapeHtml(kortDatum(a.datumStr)) + '</td>' +
          '<td>' + hfChip(a.hoofdstuk) + '</td>' +
          '<td>' + escapeHtml(a.titel) + '</td>' +
          '<td class="ouder-num">' + a.goed + "/" + a.totaal + '</td>' +
          '<td class="ouder-num">%' + a.pct + '</td>' +
          '<td>' + pill(a.cijfer, 1) + '</td>' +
        '</tr>';
      });
      h += '</tbody></table></div>';
    }

    return h;
  }

  /* ── Weergave 3: Üniteler ────────────────────────────── */
  function viewUnits(report) {
    var lijst = report.chapters.slice().sort(function (a, b) {
      if (!a.count && b.count) return 1;
      if (a.count && !b.count) return -1;
      return a.avgCijfer - b.avgCijfer;
    });

    var h = '<div class="ouder-sec-kop"><h3>Ünite teşhisi</h3>' +
            '<p>Tüm derslerin üniteleri, en zayıftan en güçlüye. Duru\'nun neyi tekrar etmesi gerektiği bu sırada.</p></div>';

    if (!lijst.length) {
      return h + '<div class="ouder-tabel-wrap"><div class="ouder-leeg">Bu dönem için ünite verisi bulunamadı.</div></div>';
    }

    h += '<div class="ouder-tabel-wrap"><table class="ouder-tabel"><thead><tr>' +
      '<th class="ouder-streep"></th><th>Ders</th><th>Ünite</th><th>Deneme</th>' +
      '<th>İlerleme</th><th>En iyi</th><th>Ortalama</th><th>Son çalışma</th>' +
      '</tr></thead><tbody>';
    lijst.forEach(function (c) {
      h += '<tr>' +
        '<td class="ouder-streep" style="background:' + cijferKleur(c.avgCijfer, c.count) + '"></td>' +
        '<td><span class="ouder-vak-inline">' + (c.vakIcoon || "") + ' <b>' + escapeHtml(c.vakTitel) + '</b></span></td>' +
        '<td>' + hfChip(c.nr) + ' ' + escapeHtml(c.titel) + '</td>' +
        '<td class="ouder-num">' + c.count + '</td>' +
        '<td class="ouder-num ouder-voortgang-cel">' +
          (c.examTotaal > 0 ? "%" + c.progressPct : "—") +
          '<span class="ouder-voortgang-bar"><span class="ouder-voortgang-vul" style="width:' + c.progressPct + '%"></span></span>' +
        '</td>' +
        '<td class="ouder-num">' + (c.count ? fmtC(c.maxCijfer) : "—") + '</td>' +
        '<td>' + pill(c.avgCijfer, c.count) + '</td>' +
        '<td class="ouder-num">' + escapeHtml(c.lastDatum) + '</td>' +
      '</tr>';
    });
    h += '</tbody></table></div>';
    return h;
  }

  /* ── Weergave 4: Günlük ──────────────────────────────── */
  function logRijen(report) {
    var q = logFilter.q.toLowerCase();
    return report.allAttempts.filter(function (a) {
      if (logFilter.vak && a.vakId !== logFilter.vak) return false;
      if (logFilter.res === "zwak" && C.geslaagd(a.cijfer)) return false;
      if (logFilter.res === "goed" && a.cijfer < C.GOED) return false;
      if (q &&
          String(a.titel).toLowerCase().indexOf(q) === -1 &&
          String(a.vakTitel).toLowerCase().indexOf(q) === -1) return false;
      return true;
    });
  }

  function logTabelHtml(report) {
    var rijen = logRijen(report);
    if (!rijen.length) {
      // Hiç kayıt yoksa bu bir filtre sorunu değil — doğru sebebi söyle.
      return '<div class="ouder-leeg">' +
        (report.allAttempts.length
          ? "Bu filtrelerle eşleşen deneme yok. Aramayı temizleyip tekrar deneyin."
          : "Bu dönemde henüz çözülmüş bir sınav yok.") +
        '</div>';
    }
    var t = '<table class="ouder-tabel"><thead><tr><th class="ouder-streep"></th>' +
      '<th>Tarih</th><th>Ders</th><th>Ünite</th><th>Sınav</th>' +
      '<th>Doğru</th><th>Yüzde</th><th>Not</th><th>Sonuç</th></tr></thead><tbody>';
    rijen.forEach(function (a) {
      t += '<tr>' +
        '<td class="ouder-streep" style="background:' + cijferKleur(a.cijfer, 1) + '"></td>' +
        '<td class="ouder-num">' + escapeHtml(kortDatum(a.datumStr)) + '</td>' +
        '<td>' + (a.vakIcoon || "") + ' ' + escapeHtml(a.vakTitel) + '</td>' +
        '<td>' + hfChip(a.hoofdstuk) + '</td>' +
        '<td>' + escapeHtml(a.titel) + '</td>' +
        '<td class="ouder-num">' + a.goed + "/" + a.totaal + '</td>' +
        '<td class="ouder-num">%' + a.pct + '</td>' +
        '<td class="ouder-num"><b>' + fmtC(a.cijfer) + '</b></td>' +
        '<td><span class="ouder-pill ouder-pill--' + (a.geslaagd ? "goed" : "zwak") + '">' +
          (a.geslaagd ? "geslaagd" : "onvoldoende") + '</span></td>' +
      '</tr>';
    });
    return t + '</tbody></table>';
  }

  function viewLogboek(report) {
    var h = '<div class="ouder-sec-kop"><h3>Çalışma günlüğü</h3>' +
            '<p>Kayıtlı her deneme, en yenisi üstte.</p></div>';

    h += '<div class="ouder-filters">' +
      '<input type="search" id="ouder-log-zoek" class="ouder-zoek" placeholder="Sınav veya ders adında ara…" ' +
        'aria-label="Günlükte ara" value="' + escapeHtml(logFilter.q) + '">' +
      '<select id="ouder-log-vak" class="ouder-zoek ouder-zoek--kort" aria-label="Derse göre filtrele">' +
        '<option value="">Tüm dersler</option>';
    report.vakken.forEach(function (v) {
      if (!v.count) return;
      h += '<option value="' + escapeHtml(v.id) + '"' +
           (logFilter.vak === v.id ? " selected" : "") + '>' + escapeHtml(v.titel) + '</option>';
    });
    h += '</select>' +
      '<select id="ouder-log-res" class="ouder-zoek ouder-zoek--kort" aria-label="Sonuca göre filtrele">' +
        '<option value=""' + (logFilter.res === "" ? " selected" : "") + '>Tüm sonuçlar</option>' +
        '<option value="zwak"' + (logFilter.res === "zwak" ? " selected" : "") + '>Sadece 5,5 altı</option>' +
        '<option value="goed"' + (logFilter.res === "goed" ? " selected" : "") + '>Sadece 7,0 ve üstü</option>' +
      '</select>' +
    '</div>';

    h += '<div class="ouder-tabel-wrap" id="ouder-log-tabel">' + logTabelHtml(report) + '</div>';
    return h;
  }

  /* ── Rapportcache ────────────────────────────────────────
     collectParentReportData loopt langs 12 vakken × hoofdstukken × pogingen.
     Dat draaide bij élke tabwissel, jaarwissel en bij de sync elke 20s opnieuw.
     De handtekening hieronder kijkt alleen naar de RUWE strings — lengte plus
     kop en staart — zodat we weten of er iets veranderd is zonder te parsen;
     juist het parsen en aggregeren is het dure deel. */

  var rapportCache = { sleutel: null, ctx: null };

  function opslagHandtekening(student, jaar) {
    var delen = [student, jaar];
    var rijen = window.DURU_VAKKEN.vanJaar(jaar);

    for (var i = 0; i < rijen.length; i++) {
      var sleutels = [rijen[i].practiceKey, rijen[i].examKey];
      for (var j = 0; j < sleutels.length; j++) {
        var k = sleutels[j];
        if (!k) continue;
        var raw = leesRuw("user_" + student + "_" + k) || leesRuw(k) || "";
        // Nieuwe pogingen worden vóóraan in history gezet, dus de kop verandert;
        // lengte + staart vangen bewerkingen verderop in het object af.
        delen.push(k + ":" + raw.length + ":" + raw.slice(0, 48) + raw.slice(-48));
      }
    }
    return delen.join("|");
  }

  function haalContext(student, jaar) {
    var sleutel = opslagHandtekening(student, jaar);
    if (rapportCache.sleutel === sleutel && rapportCache.ctx) {
      return rapportCache.ctx;
    }

    var report = collectParentReportData(student, jaar);
    var ctx = {
      report: report,
      zwakke: report.chapters.filter(function (c) {
        return c.count > 0 && !C.geslaagd(c.avgCijfer);
      }).sort(function (a, b) {
        // Dalend gaat vóór stabiel-laag: een vak dat wegzakt is urgenter dan
        // een vak dat al langer op hetzelfde lage niveau staat.
        var da = daaltNog(a) ? 0 : 1, db = daaltNog(b) ? 0 : 1;
        if (da !== db) return da - db;
        return a.avgCijfer - b.avgCijfer;
      }),
      sterke: report.chapters.filter(function (c) {
        return c.count > 0 && C.examenklaar(c.avgCijfer);
      })
    };

    rapportCache = { sleutel: sleutel, ctx: ctx };
    return ctx;
  }

  /* ── Verloop: sparkline en richting ──────────────────────
     De cijferschaal laat zien wáár Duru staat, niet welke kant het op gaat.
     Een vak dat van 4,6 naar 5,5 klimt en een vak dat van 7,0 naar 5,5 zakt
     zagen er in het paneel identiek uit — terwijl dat tegengesteld nieuws is. */

  function sparkline(attempts) {
    var punten = (attempts || []).slice(0, 8).reverse();   // oud → nieuw
    if (punten.length < 2) return '<span class="ouder-spark-leeg">–</span>';

    var b = 62, h = 18, p = 3;
    var stap = (b - p * 2) / (punten.length - 1);
    var xy = punten.map(function (a, i) {
      return [
        p + i * stap,
        h - p - (C.positie(a.cijfer) / 100) * (h - p * 2)
      ];
    });

    var d = xy.map(function (q, i) {
      return (i ? "L" : "M") + q[0].toFixed(1) + " " + q[1].toFixed(1);
    }).join(" ");

    var eind = xy[xy.length - 1];
    var kleur = cijferKleur(punten[punten.length - 1].cijfer, 1);
    var drempelY = (h - p - (C.positie(C.DREMPEL) / 100) * (h - p * 2)).toFixed(1);

    return '<svg class="ouder-spark" width="' + b + '" height="' + h +
             '" viewBox="0 0 ' + b + ' ' + h + '" role="img" aria-label="Son ' +
             punten.length + ' denemenin gidişi">' +
             '<line x1="0" y1="' + drempelY + '" x2="' + b + '" y2="' + drempelY +
               '" stroke="var(--ouder-mut)" stroke-width="1" stroke-dasharray="2,2" opacity=".45" />' +
             '<path d="' + d + '" fill="none" stroke="' + kleur + '" stroke-width="1.5" ' +
               'stroke-linecap="round" stroke-linejoin="round" />' +
             '<circle cx="' + eind[0].toFixed(1) + '" cy="' + eind[1].toFixed(1) +
               '" r="2.3" fill="' + kleur + '" />' +
           '</svg>';
  }

  /* Laatste 3 pogingen t.o.v. de 3 daarvóór. Minder dan 4 pogingen: geen
     uitspraak — één toets is geen trend. Onder 0,3 punt verschil: vlak. */
  function trendVan(attempts) {
    if (!attempts || attempts.length < 4) return null;
    var recent = attempts.slice(0, 3);
    var ouder  = attempts.slice(3, 6);
    if (!ouder.length) return null;

    var d = C.gemiddelde(recent, "cijfer") - C.gemiddelde(ouder, "cijfer");
    if (Math.abs(d) < 0.3) return { delta: d, richting: "vlak" };
    return { delta: d, richting: d > 0 ? "op" : "neer" };
  }

  /* Hoofdstuk dat wegzakt: gebruikt voor de urgentie-sortering en de badge. */
  function daaltNog(hoofdstuk) {
    var t = trendVan(hoofdstuk && hoofdstuk.attempts);
    return !!t && t.richting === "neer";
  }

  function trendHtml(attempts) {
    var t = trendVan(attempts);
    if (!t || t.richting === "vlak") return "";
    var op = t.richting === "op";
    return '<span class="ouder-trend ouder-trend--' + (op ? "op" : "neer") +
             '" title="Son 3 deneme, önceki 3 denemeye göre">' +
             (op ? "▲" : "▼") + C.tekst(Math.abs(t.delta)) + '</span>';
  }

  /* ── Volledig printrapport ───────────────────────────────
     Op het scherm staat maar één tab in de DOM (dat houdt het snel), maar de
     browser print uitsluitend wat in de DOM staat. Zonder deze stap levert
     "Yazdır / PDF" alleen de op dat moment open tab op. Daarom zetten we vlak
     vóór het printen alle vier de secties neer en na afloop de schermweergave
     terug. Werkt ook bij Ctrl+P, niet alleen via de knop. */

  function printSectie(titel, inhoud) {
    return '<section class="ouder-print-sectie">' +
             '<h3 class="ouder-print-kop">' + escapeHtml(titel) + '</h3>' +
             inhoud +
           '</section>';
  }

  function toonVolledigRapport() {
    if (printBezig || !laatsteCtx) return;
    var houder = document.querySelector("#ouder-view .ouder-views");
    if (!houder) return;
    printBezig = true;

    var r = laatsteCtx.report;
    var bewaardVak = gekozenVak;
    var bewaardFilter = logFilter;
    logFilter = { q: "", vak: "", res: "" };   // een rapport is altijd volledig

    // Alle vakken met resultaten, niet alleen de gekozen. De toetsgeschiedenis
    // per vak laten we weg: het logboek verderop somt elke poging al op.
    var vakDelen = "";
    r.vakken.forEach(function (v) {
      if (v.count) vakDelen += vakDetailHtml(v, false);
    });
    if (!vakDelen) {
      vakDelen = '<div class="ouder-leeg">Bu dönemde çözülmüş sınav yok.</div>';
    }

    houder.innerHTML =
      printSectie("Genel bakış", viewOverzicht(r, laatsteCtx.zwakke, laatsteCtx.sterke)) +
      printSectie("Ders detayı", vakDelen) +
      printSectie("Ünite teşhisi", viewUnits(r)) +
      printSectie("Çalışma günlüğü", viewLogboek(r));

    logFilter = bewaardFilter;
    gekozenVak = bewaardVak;
  }

  function herstelSchermweergave() {
    if (!printBezig) return;
    printBezig = false;
    renderParentDashboard();   // herstelt de actieve tab én alle event-handlers
  }

  function koppelPrintEvents() {
    if (printGekoppeld) return;
    printGekoppeld = true;
    window.addEventListener("beforeprint", toonVolledigRapport);
    window.addEventListener("afterprint", herstelSchermweergave);
  }

  /* ── Hoofdrender ─────────────────────────────────────── */
  function renderParentDashboard() {
    var container = document.getElementById("ouder-view");
    if (!container) return;

    var student = getActiveStudent();
    var ctx = haalContext(student, selectedJaar);
    var report = ctx.report;
    var zwakke = ctx.zwakke;
    var sterke = ctx.sterke;
    laatsteCtx = ctx;

    var heeftData = report.overallExamCount > 0;
    var avgStr = heeftData ? fmtC(report.overallAvg) : "–";

    var zin;
    if (!heeftData) {
      zin = "Bu ders yılında henüz kayıtlı bir deneme yok. Duru bir proeftoets çözdüğünde sonuç burada görünür.";
    } else if (zwakke.length) {
      zin = "Duru son 7 günde <strong>" + report.recent7DaysCount + " deneme</strong> çözdü ve genel ortalaması " +
            "<strong>" + avgStr + "</strong>. <strong>" + zwakke.length + " ünite</strong> geçme sınırının altında — " +
            "en acili <strong>" + escapeHtml(zwakke[0].vakTitel) +
            (zwakke[0].nr != null ? " H" + zwakke[0].nr : "") + "</strong>.";
    } else {
      zin = "Duru son 7 günde <strong>" + report.recent7DaysCount + " deneme</strong> çözdü ve genel ortalaması " +
            "<strong>" + avgStr + "</strong>. Şu an geçme sınırının altında ünite yok.";
    }

    var uniekeUnits = report.chapters.filter(function (c) { return c.count > 0; }).length;
    var actieveVakTel = report.vakken.filter(function (v) { return v.count > 0; }).length;

    var tabs = [
      { id: "overzicht", label: "Genel Bakış", tel: null },
      { id: "vakken",    label: "Dersler",     tel: actieveVakTel },
      { id: "units",     label: "Üniteler",    tel: uniekeUnits },
      { id: "logboek",   label: "Günlük",      tel: report.overallExamCount }
    ];

    var html = '<div class="ouder-wrap">';

    /* Kop: wie, welk jaar, printen */
    html += '<div class="ouder-bar">' +
      '<div class="ouder-bar-ident">' +
        '<span class="ouder-avatar">👨‍👧</span>' +
        '<span class="ouder-bar-tekst">' +
          '<span class="ouder-bar-naam">Veli paneli</span>' +
          '<span class="ouder-bar-sub">' + escapeHtml(student) + ' · ' +
            escapeHtml(selectedJaar) + ' · ' + niveauVan(selectedJaar) + '</span>' +
        '</span>' +
      '</div>' +
      '<div class="ouder-seg" role="group" aria-label="Ders yılı">' +
        '<button type="button" class="ouder-year-btn" data-year="2026-2027" aria-pressed="' +
          (selectedJaar === "2026-2027" ? "true" : "false") + '">2026-2027 · HAVO 3</button>' +
        '<button type="button" class="ouder-year-btn" data-year="2025-2026" aria-pressed="' +
          (selectedJaar === "2025-2026" ? "true" : "false") + '">2025-2026 · MAVO 2</button>' +
      '</div>' +
      '<button type="button" id="ouder-print-btn" class="ouder-btn" ' +
        'title="Dört bölümün tamamı tek raporda yazdırılır">🖨 Tam raporu yazdır</button>' +
    '</div>';

    /* Status */
    html += '<section class="ouder-status">' +
      '<p class="ouder-eyebrow">' + escapeHtml(selectedJaar) + ' · ' + niveauVan(selectedJaar) + '</p>' +
      '<h2 class="ouder-h1">Duru\'nun Karnesi</h2>' +
      '<p class="ouder-zin">' + zin + '</p>' +
    '</section>';

    /* Cijferschaal */
    html += '<div class="ouder-schaal-blok">' +
      '<div class="ouder-schaal-kop">' +
        '<span class="ouder-schaal-cijfer" style="color:' + cijferKleur(report.overallAvg, report.overallExamCount) + '">' +
          avgStr + '</span>' +
        '<span class="ouder-schaal-label">genel ortalama · <b>' + report.overallExamCount +
          ' deneme</b> · <b>%' + report.passRate + '</b> geçti</span>' +
      '</div>' +
      '<div class="ouder-schaal">' + schaalHtml(report) + '</div>' +
      '<div class="ouder-schaal-uiteinden"><span>1,0</span><span>10,0</span></div>' +
      '<div class="ouder-schaal-legenda">' +
        '<span><i class="ouder-dot" style="background:var(--ouder-zwak)"></i> 1,0 – 5,4 onvoldoende</span>' +
        '<span><i class="ouder-dot" style="background:var(--ouder-net)"></i> 5,5 – 6,9 voldoende</span>' +
        '<span><i class="ouder-dot" style="background:var(--ouder-goed)"></i> 7,0 – 10 goed</span>' +
        '<span class="ouder-legenda-uitleg">Küçük noktalar: her dersin ortalaması</span>' +
      '</div>' +
    '</div>';

    /* Tabs */
    html += '<nav class="ouder-tabs" role="tablist">';
    tabs.forEach(function (t) {
      html += '<button type="button" role="tab" class="ouder-tab" data-ouder-view="' + t.id + '" aria-selected="' +
        (actieveView === t.id ? "true" : "false") + '">' + t.label +
        (t.tel != null ? '<span class="ouder-tab-tel">' + t.tel + '</span>' : "") + '</button>';
    });
    html += '</nav>';

    /* Weergaven — alleen de actieve wordt gebouwd (zie wisselView) */
    html += '<div class="ouder-views">' + bouwView(ctx) + '</div>';

    html += '<p class="ouder-voet">Notlar Hollanda ölçeğinde (1,0 – 10,0), <code>cijfer = 1 + yüzde/100 × 9</code> ' +
      'ile hesaplanır; geçme sınırı 5,5. Ünite kırılımı <code>js/hoofdstukken.js</code> manifestinden gelir.</p>';

    html += '</div>';

    container.innerHTML = html;
    bindParentEvents(report);
  }

  /* Kopbalk, jaarknoppen, tabs en printen: staan buiten .ouder-views en
     overleven dus een tabwissel. Eén keer koppelen per volledige render. */
  function bindKopEvents() {
    var container = document.getElementById("ouder-view");
    if (!container) return;

    container.querySelectorAll(".ouder-year-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        selectedJaar = btn.getAttribute("data-year");
        gekozenVak = null;
        renderParentDashboard();
      });
    });

    container.querySelectorAll("[data-ouder-view]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        wisselView(btn.getAttribute("data-ouder-view"));
      });
    });

    koppelPrintEvents();
    var printBtn = document.getElementById("ouder-print-btn");
    if (printBtn) printBtn.addEventListener("click", function () { window.print(); });
  }

  /* Alles binnen .ouder-views. Wordt opnieuw gekoppeld na elke viewwissel. */
  function bindViewEvents(report) {
    var houder = document.querySelector("#ouder-view .ouder-views");
    if (!houder) return;

    houder.querySelectorAll("[data-open-vak]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        gekozenVak = btn.getAttribute("data-open-vak");
        wisselView("vakken");
      });
    });

    houder.querySelectorAll("[data-kies-vak]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        gekozenVak = btn.getAttribute("data-kies-vak");
        wisselView("vakken");
      });
    });

    /* Günlük-filters: alleen de tabel hertekenen, focus blijft staan */
    var zoek = document.getElementById("ouder-log-zoek");
    var fVak = document.getElementById("ouder-log-vak");
    var fRes = document.getElementById("ouder-log-res");
    var tabel = document.getElementById("ouder-log-tabel");

    function hertekenLog() {
      if (!tabel) return;
      tabel.innerHTML = logTabelHtml(report);
    }
    if (zoek) zoek.addEventListener("input", function () { logFilter.q = zoek.value; hertekenLog(); });
    if (fVak) fVak.addEventListener("change", function () { logFilter.vak = fVak.value; hertekenLog(); });
    if (fRes) fRes.addEventListener("change", function () { logFilter.res = fRes.value; hertekenLog(); });
  }

  function bindParentEvents(report) {
    bindKopEvents();
    bindViewEvents(report);
  }

  function bouwView(ctx) {
    if (actieveView === "overzicht") return viewOverzicht(ctx.report, ctx.zwakke, ctx.sterke);
    if (actieveView === "vakken")    return viewVakken(ctx.report);
    if (actieveView === "units")     return viewUnits(ctx.report);
    return viewLogboek(ctx.report);
  }

  /* Tabwissel vervangt alleen de inhoud van .ouder-views. De statusband en de
     cijferschaal blijven staan — die veranderen niet door van tab te wisselen,
     en opnieuw opbouwen kostte eerst een volledige herberekening. */
  function wisselView(naam) {
    actieveView = naam;

    var houder = document.querySelector("#ouder-view .ouder-views");
    if (!houder || !laatsteCtx) { renderParentDashboard(); return; }

    houder.innerHTML = bouwView(laatsteCtx);

    var container = document.getElementById("ouder-view");
    container.querySelectorAll("[data-ouder-view]").forEach(function (b) {
      b.setAttribute("aria-selected", String(b.getAttribute("data-ouder-view") === naam));
    });

    bindViewEvents(laatsteCtx.report);
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
