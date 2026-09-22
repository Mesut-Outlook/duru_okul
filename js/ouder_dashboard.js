/* =========================================================
   Duru's Schoolhub — Veli / Baba Takip & İlerleme Paneli
   Sade tek sayfa (2026-09-22): özet → dikkat edilecekler → dersler
   (tıklayınca üniteler) → son denemeler. Yazdır = window.print().
   ========================================================= */

(function () {
  "use strict";

  var selectedJaar = "2026-2027";

  // Vakregister komt uit js/vakken.js — zelfde bron als js/dashboard.js.
  var VAK_CONFIG = window.DURU_VAKKEN.alle;

  /* Het ouderpaneel toont altijd de LEERLING. Tot 2026-09-22 gaf dit de
     actieve gebruiker terug — ingelogd als baba las het paneel dus babas
     eigen (oude) kopie in plaats van Duru's resultaten. */
  function getActiveStudent() {
    var raw = localStorage.getItem("duru_active_user") || sessionStorage.getItem("duru_active_user");
    var u = raw ? raw.trim().toLowerCase() : "duru";
    return (u === "baba" || u === "veli" || u === "mesut") ? "duru" : u;
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
      var parts = String(dateStr).trim().split(" ");
      if (parts.length < 2) return new Date(dateStr);
      var dp = parts[0].replace(/,$/, "").split("-");
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
          chLastDate = chAttempts.length ? kortDatum(chAttempts[0].datumStr) : "-";
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
        var ovLastDate = overigeAttempts.length ? kortDatum(overigeAttempts[0].datumStr) : "-";

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
     Weergave — vereenvoudigd 2026-09-22 (goedgekeurd via
     preview/ouder_basit.html). Eén pagina, vier blokken:
       1. Özet      — groot gemiddelde + één zin + deze week
       2. Dikkat    — max. 3 units, beslist op de LAATSTE 3 pogingen
       3. Dersler   — tabel; klik op een vak → units klappen open
       4. Son denemeler — 8 regels + "Tümünü göster"
     Weg: 1–10-liniaal, XP/rozetten, 4 tabbladen, lijsten van 25+
     sterke/zwakke punten. Regels (dekking, gidiş, dikkat) zijn dezelfde
     als op Duru's eigen pagina, zodat beide panelen hetzelfde zeggen.
     ───────────────────────────────────────────────────────── */

  var C = window.DURU_CIJFER;
  var openVak = null;        // blijft bewaard tussen renders (cloud-sync hertekent elke 20 s)
  var toonAlleLog = false;

  function nieuwstEerst(l) {
    return (l || []).slice().sort(function (a, b) { return (b.timestamp || 0) - (a.timestamp || 0); });
  }
  function gem(l) { return C.gemiddelde(l, "cijfer"); }
  function pil(c, n) {
    return '<span class="ob-pil ' + C.klasse(c, n) + '">' + (n ? C.tekst(c) : "—") + '</span>';
  }
  function niveauVan(jaar) { return jaar === "2026-2027" ? "HAVO 3" : "MAVO 2"; }

  /* Gidiş: laatste 3 pogingen tegen de 3 daarvoor (zelfde regel als dashboard.js). */
  function gidis(lijst) {
    var l = nieuwstEerst(lijst);
    if (l.length < 4) return { r: "yok" };
    var d = gem(l.slice(0, 3)) - gem(l.slice(3, 6));
    if (Math.abs(d) < 0.3) return { r: "vlak", d: d };
    return { r: d > 0 ? "op" : "neer", d: d };
  }
  function gidisHtml(lijst) {
    var g = gidis(lijst);
    if (g.r === "yok") return '<span class="ob-gidis vlak">—</span>';
    if (g.r === "vlak") return '<span class="ob-gidis vlak">→ sabit</span>';
    return '<span class="ob-gidis ' + g.r + '">' + (g.r === "op" ? "↑ iyileşiyor" : "↓ düşüyor") + '</span>';
  }

  function gunOnce(ts) {
    if (!ts) return "—";
    var gun = Math.floor((Date.now() - ts) / 864e5);
    if (gun <= 0) return "bugün";
    if (gun === 1) return "dün";
    return gun + " gün önce";
  }

  /* Datum-parsing (ook gebruikt door collectParentReportData). */
  function ontleedDatum(s, ts) {
    if (!s && !ts) return { datum: "—", tijd: "" };
    var str = String(s || "").trim();
    if (/^\d{4}-\d{2}-\d{2}T/.test(str) || (ts && isNaN(str))) {
      var d = new Date(str || ts);
      if (!isNaN(d.getTime())) {
        var pad = function (n) { return n < 10 ? "0" + n : String(n); };
        var dat = pad(d.getDate()) + "-" + pad(d.getMonth() + 1) + "-" + d.getFullYear();
        var tij = pad(d.getHours()) + ":" + pad(d.getMinutes());
        return { datum: dat, tijd: tij };
      }
    }
    var m = str.match(/^(\d{1,2}[-.\/]\d{1,2}[-.\/]\d{2,4})\s*,?\s*(?:(?:om|at)\s*)?(\d{1,2}:\d{2}(?::\d{2})?)?/i);
    if (m) {
      var dat2 = m[1].replace(/\//g, "-").replace(/\./g, "-");
      var tij2 = m[2] ? m[2].slice(0, 5) : "";
      return { datum: dat2, tijd: tij2 };
    }
    var d2 = new Date(str);
    if (!isNaN(d2.getTime())) {
      var pad2 = function (n) { return n < 10 ? "0" + n : String(n); };
      return {
        datum: pad2(d2.getDate()) + "-" + pad2(d2.getMonth() + 1) + "-" + d2.getFullYear(),
        tijd: pad2(d2.getHours()) + ":" + pad2(d2.getMinutes())
      };
    }
    return { datum: str.replace(/[,;]+$/, "").trim(), tijd: "" };
  }

  function kortDatum(s) {
    var p = ontleedDatum(s);
    return p.datum || "—";
  }


  /* Dekking: aantal verschillende examId's / manifest-totaal — dezelfde regel
     als de vakkaarten (landing.js → leesVakData) en dashboard.js. Gemaakte
     toetsen die niet in het manifest staan tellen aan beide kanten mee.
     Zonder manifest (MAVO 2) is er geen totaal: dan alleen "N sınav". */
  function dekking(vak, student) {
    var uit = { gedaan: 0, totaal: 0 };
    var HF = (vak.jaar === "2026-2027" && window.DURU_HOOFDSTUKKEN && window.DURU_HOOFDSTUKKEN.vakken &&
              window.DURU_HOOFDSTUKKEN.vakken[vak.id]) || {};
    var inM = HF.examenHoofdstuk || {};
    Object.keys(HF.aantalExamens || {}).forEach(function (nr) { uit.totaal += Number(HF.aantalExamens[nr]) || 0; });
    var EX = vak.examKey ? readStorageKey(vak.examKey, student) : null;
    if (!EX || Array.isArray(EX)) return null;   // begrijpend lezen: andere vorm
    var uniek = {};
    (EX.history || []).forEach(function (h) { if (h && h.examId) uniek[h.examId] = 1; });
    Object.keys(uniek).forEach(function (id) { uit.gedaan++; if (uit.totaal && !(id in inM)) uit.totaal++; });
    return uit;
  }

  /* Dikkat: units waarvan de laatste 3 pogingen onder 5,5 liggen, of die
     duidelijk (≥ 1 punt) zakken. Beslist op recent, NIET op het levens-
     gemiddelde (zie CLAUDE.md → "Aciliyet"). Maximaal 3. */
  function dikkatListesi(r) {
    var uit = [];
    r.chapters.forEach(function (h) {
      if (!h.count || h.nr == null) return;
      var l = nieuwstEerst(h.attempts);
      var son = gem(l.slice(0, 3));
      var g = gidis(l);
      var naam = h.vakIcoon + " " + h.vakTitel + " · H" + h.nr + " " + h.titel;
      if (!C.geslaagd(son)) {
        uit.push({ ernst: 0, son: son, cls: "zwak", kop: naam,
          tekst: "Son " + Math.min(3, l.length) + " denemenin ortalaması <strong>" + C.tekst(son) +
                 "</strong> — geçme sınırı 5,5. " +
                 (g.r === "op" ? "Yükselişte, ama henüz sınırın altında; biraz daha tekrar iyi olur."
                               : "Bu üniteyi tekrar etmesi iyi olur.") });
      } else if (g.r === "neer" && g.d <= -1) {
        uit.push({ ernst: 1, son: son, cls: "net", kop: naam,
          tekst: "Notları düşüyor: son 3 denemede " + C.tekst(son) + ", öncesinde " + C.tekst(son - g.d) + "." });
      }
    });
    uit.sort(function (a, b) { return a.ernst - b.ernst || a.son - b.son; });
    return uit.slice(0, 3);
  }

  /* ── Hoofdrender ─────────────────────────────────────── */
  function renderParentDashboard() {
    var container = document.getElementById("ouder-view");
    if (!container) return;

    var student = getActiveStudent();
    var r = collectParentReportData(student, selectedJaar);
    var alle = nieuwstEerst(r.allAttempts);
    var week = alle.filter(function (a) { return a.timestamp >= Date.now() - 7 * 864e5; });
    var dagen = {};
    week.forEach(function (a) { dagen[new Date(a.timestamp).toDateString()] = 1; });
    var dikkat = dikkatListesi(r);
    var heeft = r.overallExamCount > 0;
    // Voorbij schooljaar: "deze week" en "dikkat" zeggen dan niets meer.
    var archief = selectedJaar !== (window.DURU_HOOFDSTUKKEN && window.DURU_HOOFDSTUKKEN.jaar || "2026-2027");

    var h = '<div id="ob">';

    /* Kop: titel, jaar, printen */
    h += '<div class="ob-kop"><div><h2>' + escapeHtml(student.charAt(0).toUpperCase() + student.slice(1)) +
         '\'nun durumu</h2><small>' + escapeHtml(selectedJaar) + ' · ' + niveauVan(selectedJaar) + '</small></div>' +
         '<div class="ob-kop-rechts">' +
           '<div class="ob-seg" role="group" aria-label="Ders yılı">' +
             ['2026-2027', '2025-2026'].map(function (j) {
               return '<button type="button" class="ob-jaar" data-year="' + j + '" aria-pressed="' +
                 (selectedJaar === j) + '">' + j + ' · ' + niveauVan(j) + '</button>';
             }).join("") +
           '</div>' +
           '<button type="button" class="ob-knop" id="ob-print">🖨 Yazdır</button>' +
         '</div></div>';

    /* 1 — Özet */
    var durum = !heeft ? "Bu ders yılında henüz deneme yok. Duru bir proeftoets çözdüğünde sonuç burada görünür."
      : archief ? "Geçmiş ders yılı: " + r.overallExamCount + " deneme, yıl ortalaması " + C.tekst(r.overallAvg) + "."
      : C.geslaagd(r.overallAvg)
        ? (dikkat.length ? "Genel durum iyi, ama aşağıda dikkat edilmesi gereken " + dikkat.length + " konu var."
                         : "Genel durum iyi. Şu an endişe edilecek bir konu yok.")
        : "Genel ortalama geçme sınırının (5,5) altında. Aşağıdaki konulara birlikte bakmak iyi olur.";
    var kl = C.klasse(r.overallAvg, r.overallExamCount);
    h += '<div class="ob-kaart"><div class="ob-ozet">' +
           '<div class="ob-not ob-kleur-' + kl + '">' + (heeft ? C.tekst(r.overallAvg) : "—") + '</div>' +
           '<p>' + durum + '</p></div>' +
         (archief ? '</div>' : '<div class="ob-feiten">' +
           '<span class="ob-feit">Bu hafta <b>' + Object.keys(dagen).length + '</b> gün çalıştı</span>' +
           '<span class="ob-feit"><b>' + week.length + '</b> deneme (7 gün)</span>' +
           '<span class="ob-feit">Son çalışma: <b>' + (alle[0] ? gunOnce(alle[0].timestamp) : "—") + '</b></span>' +
         '</div></div>');

    /* 2 — Dikkat */
    if (heeft && !archief) {
      h += '<div class="ob-kaart"><h3>Dikkat edilecekler</h3>' +
        (dikkat.length
          ? '<ul class="ob-dikkat">' + dikkat.map(function (d) {
              return '<li class="' + d.cls + '"><b>' + escapeHtml(d.kop) + '</b>' + d.tekst + '</li>';
            }).join("") + '</ul>'
          : '<div class="ob-rahat">✓ Şu an tekrar gereken ünite yok.</div>') +
        '</div>';
    }

    /* 3 — Dersler */
    var vakken = r.vakken.filter(function (v) { return v.count > 0; })
      .sort(function (a, b) { return a.avgCijfer - b.avgCijfer; });
    if (vakken.length) {
      h += '<div class="ob-kaart"><h3>Dersler</h3><table class="ob-tabel"><thead><tr>' +
           '<th>Ders</th><th class="r">Ortalama</th><th>Gidiş</th>' +
           '<th class="r m-weg">Yapılan sınav</th><th class="r m-weg">Son çalışma</th></tr></thead><tbody>';
      vakken.forEach(function (v) {
        var cfg = VAK_CONFIG.filter(function (x) { return x.jaar === selectedJaar && x.id === v.id; })[0] || {};
        var dk = dekking(cfg, student);
        var laatst = nieuwstEerst(v.attempts)[0];
        var open = openVak === v.id;
        h += '<tr class="ob-vak" data-vak="' + escapeHtml(v.id) + '" tabindex="0" aria-expanded="' + open + '">' +
             '<td class="ob-ders">' + v.icoon + ' ' + escapeHtml(v.titel) +
               '<span class="ob-ok">' + (open ? "▾" : "▸") + '</span></td>' +
             '<td class="r">' + pil(v.avgCijfer, v.count) + '</td>' +
             '<td>' + gidisHtml(v.attempts) + '</td>' +
             '<td class="r m-weg">' + (!dk ? "—" : dk.totaal ? dk.gedaan + " / " + dk.totaal : dk.gedaan + " sınav") + '</td>' +
             '<td class="r m-weg ob-zacht">' + (laatst ? gunOnce(laatst.timestamp) : "—") + '</td></tr>';
        if (open) {
          r.chapters.filter(function (c) { return c.vakId === v.id && c.count > 0; }).forEach(function (c) {
            var l = nieuwstEerst(c.attempts);
            h += '<tr class="ob-unite"><td>' + (c.nr != null ? "H" + c.nr + " · " : "") + escapeHtml(c.titel) + '</td>' +
                 '<td class="r">' + pil(c.avgCijfer, c.count) + '</td><td>' + gidisHtml(c.attempts) + '</td>' +
                 '<td class="r m-weg">' + c.count + ' deneme</td>' +
                 '<td class="r m-weg ob-zacht">' + (l[0] ? gunOnce(l[0].timestamp) : "—") + '</td></tr>';
          });
        }
      });
      h += '</tbody></table>' +
           '<div class="ob-legenda">Bir derse tıklayınca üniteleri açılır. Renkler: <span class="ob-pil goed">7+</span> iyi · ' +
           '<span class="ob-pil net">5,5–6,9</span> yeterli · <span class="ob-pil zwak">&lt;5,5</span> yetersiz. ' +
           'Gidiş = son 3 deneme, önceki 3 ile karşılaştırma.</div></div>';
    }

    /* 4 — Son denemeler */
    if (alle.length) {
      var log = toonAlleLog ? alle : alle.slice(0, 8);
      h += '<div class="ob-kaart"><h3>Son denemeler</h3><ul class="ob-log">' +
        log.map(function (a) {
          return '<li>' + pil(a.cijfer, 1) + '<span class="ob-t">' + a.vakIcoon + ' ' + escapeHtml(a.vakTitel) +
                 ' — ' + escapeHtml(a.titel) + '</span><span class="ob-zacht">' +
                 escapeHtml(kortDatum(a.datumStr)) + '</span></li>';
        }).join("") + '</ul>' +
        (alle.length > 8 ? '<p class="ob-meer-rij"><button type="button" class="ob-knop" id="ob-meer">' +
          (toonAlleLog ? "Daha az göster" : "Tümünü göster (" + alle.length + ")") + '</button></p>' : '') +
        '</div>';
    }

    h += '</div>';
    container.innerHTML = h;
    bindEvents(container);
  }

  function bindEvents(container) {
    container.querySelectorAll(".ob-jaar").forEach(function (b) {
      b.addEventListener("click", function () {
        selectedJaar = b.getAttribute("data-year");
        openVak = null; toonAlleLog = false;
        renderParentDashboard();
      });
    });
    container.querySelectorAll("tr.ob-vak").forEach(function (tr) {
      function wissel() {
        var id = tr.getAttribute("data-vak");
        openVak = openVak === id ? null : id;
        renderParentDashboard();
      }
      tr.addEventListener("click", wissel);
      tr.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); wissel(); }
      });
    });
    var meer = document.getElementById("ob-meer");
    if (meer) meer.addEventListener("click", function () { toonAlleLog = !toonAlleLog; renderParentDashboard(); });
    var pr = document.getElementById("ob-print");
    if (pr) pr.addEventListener("click", function () { window.print(); });
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
