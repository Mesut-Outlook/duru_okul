/* =========================================================
   Duru's Schoolhub — Veli / Baba Takip & İlerleme Paneli
   Sade tek sayfa (2026-09-22): özet → dikkat edilecekler → dersler
   (tıklayınca üniteler) → son denemeler. Yazdır = Ctrl+P (beforeprint → tam rapor).
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

  var VERWIJDERDE_EXAMENS = {
    "ex-h3-ak-72": 1, "ex-h3-ak-73": 1, "ex-h3-ak-74": 1, "ex-h3-ak-75": 1, "ex-h3-ak-76": 1,
    "ex-h3-ak-77": 1, "ex-h3-ak-78": 1, "ex-h3-ak-79": 1, "ex-h3-ak-80": 1, "ex-h3-ak-81": 1
  };

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
          if (att && att.examId && VERWIJDERDE_EXAMENS[att.examId]) return;
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
            geslaagd: window.DURU_CIJFER.geslaagd(c),
            examId: att.examId || null,
            duurSec: typeof att.duurSec === "number" ? att.duurSec : null,   // sinds 2026-10-09
            ruw: att            // voor de review: antwoorden + beoordelingen
          };
          vakAttempts.push(item);
          allAttempts.push(item);
        });
      }

      vakAttempts.sort(function (a, b) { return b.timestamp - a.timestamp; });

      var count = vakAttempts.length;
      var maxC = 0;
      var lastC = 0;
      var lastDatum = "-";

      if (count > 0) {
        vakAttempts.forEach(function (a) {
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

      // Gemiddelde = laatste poging per toets (DURU_CIJFER.gemiddeldeLaatste), zoals dashboard.js.
      var avgC = count > 0 ? window.DURU_CIJFER.gemiddeldeLaatste(vakAttempts, "cijfer") : 0;
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
        var chMax = 0;
        var chLast = 0;
        var chLastDate = "-";

        if (chCount > 0) {
          chAttempts.forEach(function (a) {
            if (a.cijfer > chMax) chMax = a.cijfer;
          });
          chLast = chAttempts[0].cijfer;
          chLastDate = chAttempts.length ? kortDatum(chAttempts[0].datumStr) : "-";
        }

        var chAvg = chCount > 0 ? window.DURU_CIJFER.gemiddeldeLaatste(chAttempts, "cijfer") : 0;

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
        var ovMax = 0;
        overigeAttempts.forEach(function (a) {
          if (a.cijfer > ovMax) ovMax = a.cijfer;
        });
        var ovAvg = window.DURU_CIJFER.gemiddeldeLaatste(overigeAttempts, "cijfer");
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
    var overallAvg = overallExamCount > 0 ? window.DURU_CIJFER.gemiddeldeLaatste(allAttempts, "cijfer") : 0;
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
  var openUnite = null;      // "<vakId>|<nr>": die unit toont zijn losse toetsen
  var toonAlleLog = false;
  var reviewPoging = null;   // open review (item uit allAttempts) of null
  var reviewIndex = {};      // data-review-sleutel → poging (per render opnieuw)
  var reviewFilterFout = false;
  var scrollVoorReview = 0;  // na "Geri" terug naar dezelfde plek in de lijst
  // Ana sayfa (2026-10-16): null = özet + vier grote knoppen; anders één sectie
  // ("dikkat" | "sure" | "dersler" | "log"). "hepsi" = alles onder elkaar, alleen bij printen.
  var bolum = null;

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

  /* ── Toetsduur (2026-10-09) ─────────────────────────────
     duurSec wordt pas sinds 9 oktober 2026 opgeslagen; oudere pogingen tellen
     niet mee in gemiddelden en tonen "—". */
  function metDuur(l) { return (l || []).filter(function (a) { return a.duurSec != null; }); }
  function gemDuur(l) {
    var m = metDuur(l);
    return m.length ? m.reduce(function (s, a) { return s + a.duurSec; }, 0) / m.length : null;
  }
  /* Kort (2026-10-10, telefoon): "12′" i.p.v. "12 dk", "1 sa 5′" i.p.v. "1 sa 05 dk". */
  function dk(sec) {
    if (sec == null) return "—";
    return sec < 60 ? "<1′" : Math.round(sec / 60) + "′";
  }
  function saDk(sec) {
    var m = Math.round((sec || 0) / 60);
    return m < 60 ? m + "′" : Math.floor(m / 60) + " sa" + (m % 60 ? " " + (m % 60) + "′" : "");
  }
  function dagSleutel(ts) { var d = new Date(ts); return d.getFullYear() + "-" + d.getMonth() + "-" + d.getDate(); }

  /* Günlük test süresi: laatste 14 dagen, per dag de som van duurSec. */
  function sureDagen(alle) {
    var vandaag = new Date(); vandaag.setHours(0, 0, 0, 0);
    var dagen = [];
    for (var i = 13; i >= 0; i--) {
      var d = new Date(vandaag.getTime() - i * 864e5);
      dagen.push({ d: d, sec: 0, n: 0 });
    }
    var index = {};
    dagen.forEach(function (x) { index[dagSleutel(x.d)] = x; });
    var periode = metDuur(alle).filter(function (a) { return index[dagSleutel(a.timestamp)]; });
    periode.forEach(function (a) { var x = index[dagSleutel(a.timestamp)]; x.sec += a.duurSec; x.n++; });
    return {
      dagen: dagen, periode: periode,
      toplam: periode.reduce(function (s, a) { return s + a.duurSec; }, 0),
      actief: dagen.filter(function (x) { return x.n; }),
      max: Math.max.apply(null, dagen.map(function (x) { return x.sec; })) || 1
    };
  }

  function sureKaart(alle) {
    var h = '<div class="ob-kaart"><h3>Günlük test süresi</h3>';
    if (!metDuur(alle).length) {
      return h + '<p class="ob-zacht ob-klein">Süre ölçümü 9 Ekim 2026\'da başladı. Duru yeni bir test çözdüğünde süreler burada görünür.</p></div>';
    }
    var sd = sureDagen(alle);
    var dagen = sd.dagen, periode = sd.periode, toplam = sd.toplam, actief = sd.actief, max = sd.max;
    var gun = ["Paz", "Pzt", "Sal", "Çar", "Per", "Cum", "Cmt"];
    h += '<div class="ob-feiten ts-feiten">' +
      '<span class="ob-feit">Çalıştığı günlerde ortalama <b>' + (actief.length ? saDk(toplam / actief.length) : "—") + '</b></span>' +
      '<span class="ob-feit">Test başına ortalama <b>' + dk(gemDuur(periode)) + '</b></span>' +
      '<span class="ob-feit">Son 14 günde toplam <b>' + saDk(toplam) + '</b></span></div>' +
      '<div class="ts-scroll"><div class="ts-binnen"><div class="ts-grafiek">' +
      dagen.map(function (x) {
        var leeg = !x.sec;
        return '<div class="ts-dag" title="' + x.d.toLocaleDateString("tr-TR") + ': ' + saDk(x.sec) + ', ' + x.n + ' test">' +
          '<span class="ts-min' + (leeg ? " leeg" : "") + '">' + (leeg ? "0" : dk(x.sec)) + '</span>' +
          '<span class="ts-staaf' + (leeg ? " leeg" : "") + '" style="height:' + (leeg ? 2 : Math.max(4, Math.round(x.sec / max * 130))) + 'px"></span></div>';
      }).join("") + '</div><div class="ts-as">' +
      dagen.map(function (x, i) {
        return '<span' + (i === 13 ? ' class="vandaag"' : '') + '><b>' + gun[x.d.getDay()] + '</b>' + x.d.getDate() + '/' +
          (x.d.getMonth() + 1) + '<br>' + (x.n ? x.n + " test" : "—") + '</span>';
      }).join("") + '</div></div></div>' +
      '<p class="ob-zacht ob-klein">Her sütun bir gün: o gün bitirdiği testlerin toplam süresi. Süre = testi açtığı andan teslim ettiği ana kadar, ' +
      'en fazla testin süresi (20 veya 30 dk). 9 Ekim 2026\'dan önceki denemelerin süresi bilinmiyor.</p></div>';
    return h;
  }

  /* Eén lijst per unit (2026-10-10): per toets één regel — laatste cijfer, titel,
     datum, gemiddelde duur / gegeven tijd — met de eerdere pogingen als kleine,
     aanklikbare cijfers eronder. Vroeger stond elke toets twee keer in beeld
     (süre-tabel + denemeler), op de telefoon dubbel scrollen. */
  function toetsGroepHtml(vakId, attempts) {
    var groep = {}, volg = [];
    nieuwstEerst(attempts).forEach(function (a) {
      var id = a.examId || a.titel;
      if (!groep[id]) { groep[id] = []; volg.push(id); }
      groep[id].push(a);
    });
    if (!volg.length) return "";
    titelsVoor(vakId);
    var lim = duurStand[vakId] || {};
    return '<ul class="ob-log ob-groep">' + volg.map(function (id) {
      var l = groep[id], g = gemDuur(l), max = lim[id];
      var hizli = g != null && max && g < max * 60 / 4 && !C.geslaagd(l[0].cijfer);
      return logItem(l[0], false, { duur: g, max: max, hizli: hizli, eerder: l.slice(1) });
    }).join("") + '</ul>';
  }

  /* Kort en relatief: "bugün 21:03", "dün 21:03", "Pzt 21:03" (deze week),
     "22 Eyl 21:03", ander jaar "22 Eyl 2025". Was "22-09-2026 21:03". */
  var AY = ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"];
  var GUN = ["Paz", "Pzt", "Sal", "Çar", "Per", "Cum", "Cmt"];
  function datumTijd(a) {
    var p = ontleedDatum(a.datumStr, a.timestamp);
    var d = new Date(a.timestamp);
    if (!a.timestamp || isNaN(d.getTime())) return p.datum + (p.tijd ? " " + p.tijd : "");
    var nu = new Date(); nu.setHours(0, 0, 0, 0);
    var dag = new Date(d); dag.setHours(0, 0, 0, 0);
    var verschil = Math.round((nu - dag) / 864e5);
    var dat = verschil === 0 ? "bugün" : verschil === 1 ? "dün"
      : verschil > 1 && verschil < 7 ? GUN[d.getDay()]
      : d.getDate() + " " + AY[d.getMonth()] + (d.getFullYear() !== nu.getFullYear() ? " " + d.getFullYear() : "");
    return dat + (p.tijd ? " " + p.tijd : "");
  }

  /* "Proeftoets 30 — §1.2 Exploitatie…" → "30 · §1.2 Exploitatie…" (nummer blijft, ruis weg). */
  function kortTitel(t) {
    return String(t || "").replace(/^(?:proef)?toets\s+(\d+)\s*[—–:-]\s*/i, "$1 · ");
  }
  var KORT_VAK = { aardrijkskunde: "Aardr.", natuurkunde: "Natuurk.", scheikunde: "Scheik.", geschiedenis: "Gesch.",
    maatschappijleer: "Maatsch.", nederlands: "Ned.", "nederlands-spelling": "Spelling", "nederlands-begrijpend": "Lezen",
    economie: "Econ.", wiskunde: "Wisk.", biologie: "Bio." };
  function kortVak(a) { return KORT_VAK[a.vakId] || a.vakTitel; }

  function reviewSleutel(a) {
    if (!heeftReview(a)) return "";
    var k = a.vakId + "|" + (a.ruw.attemptId || a.timestamp);
    reviewIndex[k] = a;
    return k;
  }

  /* Eén toetsregel: cijfer · (vak) toetsnaam · datum + duur. g = groepsinfo uit toetsGroepHtml. */
  function logItem(a, metVak, g) {
    // Alleen toetsen met opgeslagen antwoorden (HAVO 3-sites) zijn na te kijken.
    var sleutel = reviewSleutel(a);
    var duur = g ? g.duur : a.duurSec;
    var eerder = g && g.eerder.length ? '<span class="ob-eerder">Önceki ' + g.eerder.length + ':' +
      g.eerder.map(function (e) {
        var k = reviewSleutel(e);
        return ' <span class="ob-pil ' + C.klasse(e.cijfer, 1) + '"' + (k ? ' data-review="' + escapeHtml(k) +
          '" tabindex="0" role="button"' : '') + ' title="' + escapeHtml(datumTijd(e)) + '">' + C.tekst(e.cijfer) + '</span>';
      }).join("") + '</span>' : '';
    return '<li' + (sleutel ? ' class="ob-klik" data-review="' + escapeHtml(sleutel) + '" tabindex="0" role="button" ' +
        'title="Soruları ve cevapları göster"' : '') + '>' + pil(a.cijfer, 1) + '<span class="ob-t" title="' + escapeHtml(a.titel) + '">' +
      (metVak ? '<b class="ob-vk">' + a.vakIcoon + ' ' + escapeHtml(kortVak(a)) + '</b> ' : '') + escapeHtml(kortTitel(a.titel)) +
      '</span><span class="ob-meta"><span class="ob-zacht">' + escapeHtml(datumTijd(a)) + '</span>' +
      (duur == null ? '' : '<span class="ob-duur">' + dk(duur) + (g && g.max ? '<span class="ob-zacht"> / ' + g.max + '′</span>' : '') + '</span>') +
      (g && g.hizli ? '<span class="ts-hint" title="Not yetersiz ve süre, verilen sürenin dörtte birinden az">çok hızlı?</span>' : '') +
      '</span>' + (sleutel ? '<span class="ob-pijl" aria-hidden="true">›</span>' : '') + eerder + '</li>';
  }

  function heeftReview(a) {
    return !!(a && a.ruw && a.examId && Array.isArray(a.ruw.antwoorden) &&
              Array.isArray(a.ruw.beoordelingen) && selectedJaar === "2026-2027");
  }

  /* ── Review: de vragen van een toets ophalen ─────────────
     De vragen staan in havo3/<vak>/js/data/*.js. We lezen de <script>-lijst uit
     de index.html van het vak en voeren elk databestand uit met een nep-DURU
     die alleen registerExamen opvangt (zelfde techniek als
     tools/build_hoofdstukken.js). Alleen lezen: geen engine, geen localStorage.
     Resultaat per vak in het geheugen bewaard. */
  var examenCache = {};
  function laadExamens(vakId) {
    if (examenCache[vakId]) return examenCache[vakId];
    var basis = "./havo3/" + vakId + "/";
    examenCache[vakId] = fetch(basis + "index.html", { cache: "no-cache" })
      .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.text(); })
      .then(function (html) {
        var srcs = [], re = /<script[^>]+src="(js\/data\/[^"?]+)[^"]*"/g, m;
        while ((m = re.exec(html))) srcs.push(m[1]);
        return Promise.all(srcs.map(function (src) {
          return fetch(basis + src).then(function (r) { return r.ok ? r.text() : ""; });
        }));
      })
      .then(function (codes) {
        var examens = {};
        var nep = { registerExamen: function (e) { if (e && e.id) examens[e.id] = e; }, register: function () {} };
        codes.forEach(function (code) {
          try { new Function("DURU", "window", code)(nep, { DURU: nep }); } catch (e) { /* kapot bestand overslaan */ }
        });
        return examens;
      })
      .catch(function (e) { delete examenCache[vakId]; throw e; });
    return examenCache[vakId];
  }

  /* Antwoordweergave — gelijk aan toonAntwoord/juisteAntwoord in de
     exams.js van de vak-sites (alle twaalf identiek). */
  function toonAntwoord(v, antw) {
    if (antw === null || antw === undefined || antw === "") return "<i>(boş bırakmış)</i>";
    if (v.type === "mc") return escapeHtml(v.opties[antw]);
    if (v.type === "waaronwaar") return antw === 0 ? "Waar" : "Onwaar";
    return escapeHtml(antw);
  }
  function juisteAntwoord(v) {
    if (v.type === "mc") return escapeHtml(v.opties[v.antwoord]);
    if (v.type === "waaronwaar") return (v.antwoord === true || v.antwoord === "waar" || v.antwoord === 0) ? "Waar" : "Onwaar";
    if (v.type === "invul") return escapeHtml(String(v.antwoord).split("|")[0]);
    return escapeHtml(v.modelantwoord || "");
  }

  function renderReview(container) {
    var a = reviewPoging, att = a.ruw;
    container.innerHTML = '<div id="ob">' +
      '<div class="ob-kop"><button type="button" class="ob-knop" id="ob-terug">← Geri</button></div>' +
      '<div class="ob-kaart"><div class="ob-ozet">' +
        '<div class="ob-not ob-kleur-' + C.klasse(a.cijfer, 1) + '">' + C.tekst(a.cijfer) + '</div>' +
        '<p><b>' + a.vakIcoon + ' ' + escapeHtml(a.vakTitel) + '</b> — ' + escapeHtml(kortTitel(a.titel)) + '<br>' +
        '<span class="ob-zacht">' + escapeHtml(datumTijd(a)) + ' · ' + (att.goed != null ? att.goed : "?") +
        ' / ' + (att.totaal != null ? att.totaal : "?") + ' doğru</span></p></div></div>' +
      '<div class="ob-kaart" id="ob-review"><p class="ob-zacht">Sorular yükleniyor…</p></div></div>';
    bindEvents(container);

    laadExamens(a.vakId).then(function (examens) {
      if (reviewPoging !== a) return;               // intussen teruggegaan
      var box = document.getElementById("ob-review");
      if (!box) return;
      var ex = examens[a.examId];
      if (!ex || !Array.isArray(ex.vragen)) {
        box.innerHTML = '<p class="ob-zacht">Bu sınavın soruları bulunamadı.</p>';
        return;
      }
      var tel = { goed: 0, deels: 0, fout: 0 };
      var items = ex.vragen.map(function (v, i) {
        var b = att.beoordelingen[i] || { status: "fout" };
        var st = b.status === "goed" ? "goed" : (b.status === "deels" ? "deels" : "fout");
        tel[st]++;
        if (reviewFilterFout && st === "goed") return "";
        var kop = st === "goed" ? "✅ Doğru" : (st === "deels" ? "🟡 Kısmen doğru" : "❌ Yanlış");
        return '<li class="ob-rv ob-rv--' + st + '" value="' + (i + 1) + '">' +
          '<div class="ob-rv-kop">Soru ' + (i + 1) + ' — ' + kop + '</div>' +
          '<div class="ob-rv-vraag">' + v.vraag + '</div>' +
          (v.figuur ? '<div class="ob-rv-figuur">' + v.figuur + '</div>' : '') +
          '<div class="ob-rv-rij"><span>Duru\'nun cevabı:</span> ' + toonAntwoord(v, att.antwoorden[i]) + '</div>' +
          (st !== "goed" ? '<div class="ob-rv-rij"><span>Doğru cevap:</span> ' + juisteAntwoord(v) + '</div>' : '') +
          (v.uitleg ? '<div class="ob-rv-uitleg">💡 ' + v.uitleg + '</div>' : '') +
          '</li>';
      }).join("");
      box.innerHTML =
        '<div class="ob-rv-balk"><span><b>' + tel.goed + '</b> doğru · <b>' + tel.deels + '</b> kısmen · <b>' +
          tel.fout + '</b> yanlış</span>' +
        '<button type="button" class="ob-knop" id="ob-rv-filter">' +
          (reviewFilterFout ? "Tüm soruları göster" : "Sadece yanlışları göster") + '</button></div>' +
        '<ol class="ob-rv-lijst">' + items + '</ol>';
      var fb = document.getElementById("ob-rv-filter");
      if (fb) fb.addEventListener("click", function () { reviewFilterFout = !reviewFilterFout; renderParentDashboard(); });
    }).catch(function () {
      var box = document.getElementById("ob-review");
      if (box) box.innerHTML = '<p class="ob-zacht">Sorular yüklenemedi. Bağlantıyı kontrol edip tekrar deneyin.</p>';
    });
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
      // Alleen ISO-tekst mag door new Date(); "05-09-2026" leest de browser als
      // 9 mei (Amerikaans). Anders de tijdstempel gebruiken (al dd-mm geparsed).
      var d = /^\d{4}-\d{2}-\d{2}T/.test(str) ? new Date(str) : new Date(ts);
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

  /* Open toetsen per unit (2026-10-03): manifest-id's van dit hoofdstuk minus
     de examId's die Duru ooit gemaakt heeft. Zonder manifest (MAVO 2) totaal 0. */
  function toetsStand(c) {
    var HF = (selectedJaar === "2026-2027" && window.DURU_HOOFDSTUKKEN && window.DURU_HOOFDSTUKKEN.vakken &&
              window.DURU_HOOFDSTUKKEN.vakken[c.vakId]) || {};
    var map = HF.examenHoofdstuk || {};
    var ids = c.nr == null ? [] : Object.keys(map).filter(function (id) { return map[id] === c.nr; });
    var gedaan = {};
    (c.attempts || []).forEach(function (a) { if (a.examId) gedaan[a.examId] = 1; });
    var open = ids.filter(function (id) { return !gedaan[id]; });
    return { totaal: ids.length, gedaan: ids.length - open.length, open: open };
  }

  /* Toetsnamen voor de open-lijst: één keer per vak ophalen (laadExamens), daarna
     synchroon uit titelStand. "laden" → na het ophalen opnieuw tekenen. */
  var titelStand = {};
  var duurStand = {};   // examId → duurMin (voor "12 dk / 20")
  function titelsVoor(vakId) {
    if (titelStand[vakId]) return titelStand[vakId];
    titelStand[vakId] = "laden";
    laadExamens(vakId).then(function (ex) {
      var t = {}, d = {};
      Object.keys(ex).forEach(function (id) { t[id] = ex[id].titel || id; d[id] = ex[id].duurMin || 20; });
      titelStand[vakId] = t;
      duurStand[vakId] = d;
      renderParentDashboard();
    }).catch(function () { titelStand[vakId] = "fout"; renderParentDashboard(); });
    return "laden";
  }

  /* "48 / 120 açık" + balkje (gedaan deel groen). MAVO 2 zonder manifest: "N sınav". */
  function acikHtml(dk) {
    if (!dk) return "—";
    if (!dk.totaal) return dk.gedaan + " sınav";
    var open = dk.totaal - dk.gedaan;
    return '<span class="ob-acik"><span><b class="' + (open ? "ob-kleur-net" : "ob-kleur-goed") + '">' + open +
      '</b> / ' + dk.totaal + ' açık</span><span class="ob-acik-b" aria-hidden="true"><span style="width:' +
      Math.round(dk.gedaan / dk.totaal * 100) + '%"></span></span></span>';
  }
  function acikLijstHtml(vakId, s) {
    if (!s.totaal) return "";
    if (!s.open.length) return '<p class="ob-acik-lijst ob-kleur-goed">✓ Bu ünitenin bütün testleri en az bir kez çözüldü.</p>';
    var t = titelsVoor(vakId);
    var naam = function (id) { return typeof t === "object" && t[id] ? t[id] : id; };
    return '<div class="ob-acik-lijst"><b>Henüz çözülmemiş ' + s.open.length + ' test</b>' +
      (t === "laden" ? ' <span class="ob-zacht">— adlar yükleniyor…</span>' : '') +
      '<ol>' + s.open.map(function (id) { return '<li>' + escapeHtml(kortTitel(naam(id))) + '</li>'; }).join("") + '</ol></div>';
  }

  /* Dikkat (2026-10-03): begonnen units (≥1 toets gemaakt, nog toetsen open)
     waar 14+ dagen niets meer gebeurd is. Nooit-begonnen units tellen niet mee:
     dat zijn er te veel en ze zouden de echt vergeten unit verbergen. */
  function stilleUnites(r) {
    var uit = [];
    r.chapters.forEach(function (c) {
      if (c.nr == null || !c.count) return;
      var s = toetsStand(c);
      if (!s.gedaan || !s.open.length) return;
      var laatst = nieuwstEerst(c.attempts)[0];
      var dagen = Math.floor((Date.now() - (laatst.timestamp || 0)) / 864e5);
      if (dagen < 14) return;
      uit.push({ dagen: dagen, cls: "net", kop: c.vakIcoon + " " + c.vakTitel + " · " + (window.DURU_HF ? window.DURU_HF.kort(c.vakId, c.nr) : "H" + c.nr) + " " + c.titel,
        tekst: "<strong>" + dagen + " gündür</strong> çalışılmadı. Başlanmış (" + s.gedaan + "/" + s.totaal +
               " test yapıldı), " + s.open.length + " test açık." });
    });
    return uit.sort(function (a, b) { return b.dagen - a.dagen; });
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
      var naam = h.vakIcoon + " " + h.vakTitel + " · " + (window.DURU_HF ? window.DURU_HF.kort(h.vakId, h.nr) : "H" + h.nr) + " " + h.titel;
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

  /* ── Ana sayfa: vier grote knoppen, elk met een voorproefje van zijn sectie ── */
  var BOLUM_AD = { dikkat: "Dikkat edilecekler", dersler: "Dersler", log: "Son denemeler", sure: "Test süresi", ayarlar: "Ayarlar" };
  var IKON = {
    dikkat: '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    dersler: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    log: '<polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/>',
    sure: '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>'
  };

  function tegel(naam, ikon, titel, inhoud, extraKlas) {
    return '<button type="button" class="ob-tegel' + (extraKlas ? " " + extraKlas : "") + '" data-bolum="' + naam + '">' +
      '<span class="ob-t-kop"><span class="ob-t-ikon ob-t-ikon--' + naam + '" aria-hidden="true"><svg class="hic" viewBox="0 0 24 24">' + IKON[naam] + '</svg></span>' +
      '<span class="ob-t-naam">' + titel + '</span>' +
      '<svg class="hic ob-t-pijl" viewBox="0 0 24 24" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></span>' + inhoud + '</button>';
  }

  function tegelsHtml(secties, x) {
    var t = [];
    if (secties.dikkat) {
      var lijst = x.dikkat.concat(x.stil.slice(0, 3)), n = lijst.length;
      t.push(tegel("dikkat", "⚠️", "Dikkat edilecekler", n
        ? '<span class="ob-t-getal ob-kleur-' + lijst[0].cls + '">' + n + ' <small>ünite</small></span>' +
          '<span class="ob-t-rij">' + lijst.slice(0, 2).map(function (d) { return '<b class="ob-kleur-' + d.cls + '">●</b> ' + escapeHtml(d.kop); }).join("<br>") + '</span>' +
          (n > 2 ? '<span class="ob-t-alt">+' + (n - 2) + ' ünite daha</span>' : '')
        : '<span class="ob-t-getal ob-kleur-goed">✓</span><span class="ob-t-alt">Şu an tekrar gereken ünite yok.</span>',
        n ? "ob-t-" + lijst[0].cls : ""));
    }
    if (secties.dersler) {
      var ged = 0, tot = 0;
      x.vakken.forEach(function (v) { var k = x.dekkingen[v.id]; if (k) { ged += k.gedaan; tot += k.totaal; } });
      var met = x.vakken.filter(function (v) { return v.count > 0; }).sort(function (a, b) { return b.avgCijfer - a.avgCijfer; });
      t.push(tegel("dersler", "📚", "Dersler",
        (tot ? '<span class="ob-t-getal">' + ged + ' <small>/ ' + tot + ' test yapıldı</small></span>' +
               '<span class="ob-t-balk" aria-hidden="true"><span style="width:' + Math.round(ged / tot * 100) + '%"></span></span>'
             : '<span class="ob-t-getal">' + x.vakken.length + ' <small>ders</small></span>') +
        (tot ? '<span class="ob-t-alt">' + x.vakken.length + ' ders · ' + (tot - ged) + ' test açık</span>' : '') +
        '<span class="ob-t-pillen">' + met.slice(0, 7).map(function (v) {
          return '<span title="' + escapeHtml(v.titel) + '">' + pil(v.avgCijfer, v.count) + '</span>';
        }).join("") + (met.length > 7 ? '<span class="ob-t-alt">+' + (met.length - 7) + '</span>' : '') + '</span>'));
    }
    if (secties.log) {
      var a = x.alle[0];
      t.push(tegel("log", "🕑", "Son denemeler",
        '<span class="ob-t-getal ob-kleur-' + C.klasse(a.cijfer, 1) + '">' + C.tekst(a.cijfer) +
          ' <small>' + escapeHtml(kortVak(a)) + '<span class="ob-t-tijd"> · ' + escapeHtml(datumTijd(a)) + '</span></small></span>' +
        (x.alle.length > 1 ? '<span class="ob-t-pillen"><span class="ob-t-alt">Öncekiler:</span>' +
          x.alle.slice(1, 4).map(function (e) { return pil(e.cijfer, 1); }).join("") + '</span>' : '') +
        '<span class="ob-t-alt ob-t-hint">Bir denemeye tıklayınca sorular ve yanlışlar açılır</span>'));
    }
    if (secties.sure) {
      if (metDuur(x.alle).length) {
        var sd = sureDagen(x.alle);
        t.push(tegel("sure", "⏱", "Test süresi",
          '<span class="ob-t-getal">' + saDk(metDuur(x.week).reduce(function (s, a) { return s + a.duurSec; }, 0)) + ' <small>bu hafta</small></span>' +
          '<span class="ob-t-mini" aria-hidden="true">' + sd.dagen.map(function (g) {
            return '<span' + (g.sec ? ' style="height:' + Math.max(6, Math.round(g.sec / sd.max * 100)) + '%"' : ' class="leeg"') + '></span>';
          }).join("") + '</span>' +
          '<span class="ob-t-alt">Çalıştığı günlerde ortalama ' + (sd.actief.length ? saDk(sd.toplam / sd.actief.length) : "—") +
            ' · test başına ' + dk(gemDuur(sd.periode)) + '</span>'));
      } else {
        t.push(tegel("sure", "⏱", "Test süresi", '<span class="ob-t-getal">—</span>' +
          '<span class="ob-t-alt">Süre ölçümü 9 Ekim 2026\'da başladı.</span>'));
      }
    }
    return t.length ? '<div class="ob-tegels">' + t.join("") + '</div>' : '';
  }

  function zetBolum(naam) {
    if (naam === bolum) return;
    if (naam && !bolum) history.pushState({ vakIframe: false, obBolum: naam }, "", "");   // telefoon-terug = ana sayfa
    else if (!naam && history.state && history.state.obBolum) { history.back(); return; }  // popstate tekent
    bolum = naam; openVak = null; openUnite = null;
    renderParentDashboard();
    window.scrollTo(0, 0);
  }

  window.addEventListener("popstate", function (e) {
    var naam = e.state && e.state.obBolum || null;
    if (naam === bolum && !reviewPoging) return;
    bolum = naam; reviewPoging = null;
    renderParentDashboard();
    window.scrollTo(0, 0);
  });

  /* Yazdır / Ctrl+P: altijd het volledige rapport, ook vanaf de ana sayfa. */
  var bolumVoorPrint;
  window.addEventListener("beforeprint", function () {
    if (!document.body.classList.contains("ouder-actief") || reviewPoging) return;
    bolumVoorPrint = bolum; bolum = "hepsi"; renderParentDashboard();
  });
  window.addEventListener("afterprint", function () {
    if (bolumVoorPrint === undefined) return;
    bolum = bolumVoorPrint; bolumVoorPrint = undefined; renderParentDashboard();
  });

  /* ── Hoofdrender ─────────────────────────────────────── */
  function renderParentDashboard() {
    var container = document.getElementById("ouder-view");
    if (!container) return;
    // Cloud-sync hertekent elke 20 s: een open review blijft dan open.
    if (reviewPoging) { renderReview(container); return; }
    reviewIndex = {};

    var student = getActiveStudent();
    var r = collectParentReportData(student, selectedJaar);
    var alle = nieuwstEerst(r.allAttempts);
    var week = alle.filter(function (a) { return a.timestamp >= Date.now() - 7 * 864e5; });
    var dagen = {};
    week.forEach(function (a) { dagen[new Date(a.timestamp).toDateString()] = 1; });
    var dikkat = dikkatListesi(r);
    // Een unit die al om zijn cijfers in de lijst staat, niet nog eens als "stil" tonen.
    var stil = stilleUnites(r).filter(function (s) {
      return !dikkat.some(function (d) { return d.kop === s.kop; });
    });
    var heeft = r.overallExamCount > 0;
    // Voorbij schooljaar: "deze week" en "dikkat" zeggen dan niets meer.
    var archief = selectedJaar !== (window.DURU_HOOFDSTUKKEN && window.DURU_HOOFDSTUKKEN.jaar || "2026-2027");

    var h = '<div id="ob">';

    /* Kop: titel, jaar, printen (in een sectie: één balk ‹ Ana sayfa · titel · print, zie onder) */
    // Kop (2026-10-16): geen printknop (Ctrl+P drukt nog steeds het hele rapport), jaarkeuze → Ayarlar.
    var ayarKnop = '<button type="button" class="ob-knop ob-ayar" data-bolum="ayarlar" aria-label="Ayarlar">' +
      '<svg class="hic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg></button>';
    var kopHtml = '<div class="ob-kop"><div><h2>' + escapeHtml(student.charAt(0).toUpperCase() + student.slice(1)) +
         '\'nun durumu</h2><small>' + escapeHtml(selectedJaar) + ' · ' + niveauVan(selectedJaar) + '</small></div>' +
         ayarKnop + '</div>';
    var secties = {};
    secties.ayarlar = '<div class="ob-kaart"><h3>Ders yılı</h3><p class="ob-zacht ob-klein">Hangi yılın sonuçları gösterilsin?</p>' +
      '<div class="ob-seg ob-seg--blok" role="group" aria-label="Ders yılı">' +
      ['2026-2027', '2025-2026'].map(function (j) {
        return '<button type="button" class="ob-jaar" data-year="' + j + '" aria-pressed="' + (selectedJaar === j) + '">' +
          j + ' · ' + niveauVan(j) + '</button>';
      }).join("") + '</div></div>' +
      '<div class="ob-kaart"><h3>Rapor yazdırma</h3><p class="ob-zacht ob-klein">Tarayıcının yazdır komutu (Ctrl+P / ⌘P) ' +
      'her zaman tam raporu basar: özet, dikkat edilecekler, test süresi, dersler ve son denemeler.</p></div>';

    /* 1 — Özet */
    var durum = !heeft ? "Bu ders yılında henüz deneme yok. Duru bir proeftoets çözdüğünde sonuç burada görünür."
      : archief ? "Geçmiş ders yılı: " + r.overallExamCount + " deneme, yıl ortalaması " + C.tekst(r.overallAvg) + "."
      : C.geslaagd(r.overallAvg)
        ? (dikkat.length + stil.length ? "Genel durum iyi, ama aşağıda dikkat edilmesi gereken " +
             (dikkat.length + Math.min(3, stil.length)) + " konu var."
                         : "Genel durum iyi. Şu an endişe edilecek bir konu yok.")
        : "Genel ortalama geçme sınırının (5,5) altında. Aşağıdaki konulara birlikte bakmak iyi olur.";
    var kl = C.klasse(r.overallAvg, r.overallExamCount);
    var ozetHtml = '<div class="ob-kaart"><div class="ob-ozet">' +
           '<div class="ob-not ob-kleur-' + kl + '">' + (heeft ? C.tekst(r.overallAvg) : "—") + '</div>' +
           '<p>' + durum + '</p></div>' +
         (archief ? '</div>' : '<div class="ob-feiten">' +
           '<span class="ob-feit">Bu hafta <b>' + Object.keys(dagen).length + '</b> gün çalıştı</span>' +
           '<span class="ob-feit"><b>' + week.length + '</b> deneme (7 gün)</span>' +
           (metDuur(alle).length ? '<span class="ob-feit">Bu hafta testlerde <b>' +
             saDk(metDuur(week).reduce(function (s, a) { return s + a.duurSec; }, 0)) + '</b></span>' : '') +
           '<span class="ob-feit">Son çalışma: <b>' + (alle[0] ? gunOnce(alle[0].timestamp) +
             (ontleedDatum(alle[0].datumStr, alle[0].timestamp).tijd ? " " + ontleedDatum(alle[0].datumStr, alle[0].timestamp).tijd : "")
             : "—") + '</b></span>' +
         '</div></div>');

    /* 2 — Dikkat */
    if (heeft && !archief) {
      var dikkatLi = function (d) {
        return '<li class="' + d.cls + '"><b>' + escapeHtml(d.kop) + '</b>' + d.tekst + '</li>';
      };
      secties.dikkat = '<div class="ob-kaart"><h3>Dikkat edilecekler</h3>' +
        (dikkat.length || stil.length
          ? '<ul class="ob-dikkat">' + dikkat.map(dikkatLi).join("") + stil.slice(0, 3).map(dikkatLi).join("") + '</ul>' +
            (stil.length > 3 ? '<p class="ob-zacht ob-klein">+ ' + (stil.length - 3) +
              ' ünite daha uzun süredir çalışılmadı (en eski 3 gösteriliyor).</p>' : '')
          : '<div class="ob-rahat">✓ Şu an tekrar gereken ünite yok.</div>') +
        '</div>';
    }

    /* 2b — Günlük test süresi */
    if (heeft && !archief) secties.sure = sureKaart(alle);

    /* 3 — Dersler */
    // Ook vakken zonder poging tonen zolang er toetsen klaarstaan: die zijn dan helemaal "açık".
    var dekkingen = {};
    r.vakken.forEach(function (v) {
      var cfg = VAK_CONFIG.filter(function (x) { return x.jaar === selectedJaar && x.id === v.id; })[0] || {};
      dekkingen[v.id] = dekking(cfg, student);
    });
    var vakken = r.vakken.filter(function (v) { return v.count > 0 || (dekkingen[v.id] && dekkingen[v.id].totaal > 0); })
      .sort(function (a, b) { return (b.count > 0) - (a.count > 0) || a.avgCijfer - b.avgCijfer; });
    if (vakken.length) {
      var d = "";
      d += '<div class="ob-kaart"><h3>Dersler</h3><table class="ob-tabel"><thead><tr>' +
           '<th>Ders</th><th class="r">Ortalama</th><th>Gidiş</th><th class="r">Ort. süre</th>' +
           '<th class="r">Açık test</th><th class="r m-weg">Son çalışma</th></tr></thead><tbody>';
      vakken.forEach(function (v) {
        var dkg = dekkingen[v.id];
        var laatst = nieuwstEerst(v.attempts)[0];
        var open = openVak === v.id;
        d += '<tr class="ob-vak" data-vak="' + escapeHtml(v.id) + '" tabindex="0" aria-expanded="' + open + '">' +
             '<td class="ob-ders">' + v.icoon + ' ' + escapeHtml(v.titel) +
               '<span class="ob-ok">' + (open ? "▾" : "▸") + '</span></td>' +
             '<td class="r">' + pil(v.avgCijfer, v.count) + '</td>' +
             '<td>' + gidisHtml(v.attempts) + '</td>' +
             '<td class="r ob-sure' + (gemDuur(v.attempts) == null ? ' leeg' : '') + '">' + dk(gemDuur(v.attempts)) + '</td>' +
             '<td class="r">' + acikHtml(dkg) + '</td>' +
             '<td class="r m-weg ob-zacht">' + (laatst ? gunOnce(laatst.timestamp) : "—") + '</td></tr>';
        if (open) {
          r.chapters.filter(function (c) { return c.vakId === v.id && (c.count > 0 || toetsStand(c).totaal > 0); })
          .forEach(function (c) {
            var l = nieuwstEerst(c.attempts);
            var s = toetsStand(c);
            var sleutel = v.id + "|" + (c.nr != null ? c.nr : "overig");
            var uOpen = openUnite === sleutel;
            d += '<tr class="ob-unite" data-unite="' + escapeHtml(sleutel) + '" tabindex="0" aria-expanded="' + uOpen + '">' +
                 '<td>' + (c.nr != null ? (window.DURU_HF ? window.DURU_HF.kort(c.vakId, c.nr) : "H" + c.nr) + " · " : "") + escapeHtml(c.titel) +
                   '<span class="ob-ok">' + (uOpen ? "▾" : "▸") + '</span></td>' +
                 '<td class="r">' + pil(c.avgCijfer, c.count) + '</td><td>' + gidisHtml(c.attempts) + '</td>' +
                 '<td class="r ob-sure' + (gemDuur(c.attempts) == null ? ' leeg' : '') + '">' + dk(gemDuur(c.attempts)) + '</td>' +
                 '<td class="r">' + (s.totaal ? '<b class="' + (s.open.length ? "ob-kleur-net" : "ob-kleur-goed") + '">' +
                   s.gedaan + ' / ' + s.totaal + '</b> <span class="ob-zacht">yapıldı</span>' : c.count + ' deneme') + '</td>' +
                 '<td class="r m-weg ob-zacht">' + (l[0] ? gunOnce(l[0].timestamp) : "hiç başlanmadı") + '</td></tr>';
            if (uOpen) {
              d += '<tr class="ob-toetsen"><td colspan="6">' +
                   toetsGroepHtml(v.id, l) +
                   acikLijstHtml(v.id, s) + '</td></tr>';
            }
          });
        }
      });
      d += '</tbody></table>' +
           '<div class="ob-legenda">Derse tıklayınca üniteleri, üniteye tıklayınca sınav sonuçları ve henüz çözülmemiş testler açılır. Renkler: <span class="ob-pil goed">7+</span> iyi · ' +
           '<span class="ob-pil net">5,5–6,9</span> yeterli · <span class="ob-pil zwak">&lt;5,5</span> yetersiz. ' +
           'Gidiş = son 3 deneme, önceki 3 ile karşılaştırma. Ort. süre = testi açmasından teslim etmesine kadar geçen süre ' +
           '(9 Ekim 2026\'dan beri ölçülüyor); 12′ = 12 dakika; “/ 20′” testin verilen süresi; bir test birkaç kez çözüldüyse “Önceki” notlar altında (tıklanabilir); “çok hızlı?” = not yetersiz ve süre verilen sürenin dörtte birinden az.</div></div>';
      secties.dersler = d;
    }

    /* 4 — Son denemeler */
    if (alle.length) {
      var log = toonAlleLog ? alle : alle.slice(0, 8);
      secties.log = '<div class="ob-kaart"><h3>Son denemeler</h3><ul class="ob-log">' +
        log.map(function (a) { return logItem(a, true); }).join("") + '</ul>' +
        (alle.length > 8 ? '<p class="ob-meer-rij"><button type="button" class="ob-knop" id="ob-meer">' +
          (toonAlleLog ? "Daha az göster" : "Tümünü göster (" + alle.length + ")") + '</button></p>' : '') +
        '</div>';
    }

    if (bolum && bolum !== "hepsi" && !secties[bolum]) bolum = null;   // bv. na wissel naar vorig jaar
    if (bolum === "hepsi") {
      h += kopHtml + ozetHtml + ["dikkat", "sure", "dersler", "log"].map(function (k) { return secties[k] || ""; }).join("");
    } else if (bolum) {
      h += '<div class="ob-bolumbalk"><button type="button" class="ob-knop ob-ana" id="ob-ana">' +
        '<svg class="hic" viewBox="0 0 24 24" aria-hidden="true"><polyline points="15 18 9 12 15 6"/></svg>Ana sayfa</button>' +
        '<h2>' + BOLUM_AD[bolum] + '</h2></div><div class="ob-bolum">' + secties[bolum] + '</div>';
    } else {
      h += kopHtml + ozetHtml + tegelsHtml(secties, { dikkat: dikkat, stil: stil, alle: alle, week: week, vakken: vakken, dekkingen: dekkingen });
    }

    h += '</div>';
    container.innerHTML = h;
    // Telefoon: de grafiek scrolt; begin bij vandaag (rechts).
    container.querySelectorAll(".ts-scroll").forEach(function (el) { el.scrollLeft = el.scrollWidth; });
    bindEvents(container);
  }

  function bindEvents(container) {
    container.querySelectorAll(".ob-jaar").forEach(function (b) {
      b.addEventListener("click", function () {
        selectedJaar = b.getAttribute("data-year");
        reviewPoging = null;
        openVak = null; openUnite = null; toonAlleLog = false; bolum = null;
        renderParentDashboard();
      });
    });
    container.querySelectorAll("tr.ob-vak").forEach(function (tr) {
      function wissel() {
        var id = tr.getAttribute("data-vak");
        openVak = openVak === id ? null : id;
        openUnite = null;
        renderParentDashboard();
      }
      tr.addEventListener("click", wissel);
      tr.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); wissel(); }
      });
    });
    container.querySelectorAll("tr.ob-unite").forEach(function (tr) {
      function wissel() {
        var id = tr.getAttribute("data-unite");
        openUnite = openUnite === id ? null : id;
        renderParentDashboard();
      }
      tr.addEventListener("click", wissel);
      tr.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); wissel(); }
      });
    });
    container.querySelectorAll("[data-bolum]").forEach(function (b) {
      b.addEventListener("click", function () { zetBolum(b.getAttribute("data-bolum")); });
    });
    var ana = document.getElementById("ob-ana");
    if (ana) ana.addEventListener("click", function () { zetBolum(null); });
    var meer = document.getElementById("ob-meer");
    if (meer) meer.addEventListener("click", function () { toonAlleLog = !toonAlleLog; renderParentDashboard(); });
    container.querySelectorAll("[data-review]").forEach(function (li) {
      function open() {
        var a = reviewIndex[li.getAttribute("data-review")];
        if (!a) return;
        scrollVoorReview = window.scrollY;
        reviewPoging = a; reviewFilterFout = false;
        renderParentDashboard();
        window.scrollTo(0, 0);
      }
      li.addEventListener("click", function (e) { e.stopPropagation(); open(); });
      li.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); }
      });
    });
    var terug = document.getElementById("ob-terug");
    if (terug) terug.addEventListener("click", function () {
      reviewPoging = null;
      renderParentDashboard();
      window.scrollTo(0, scrollVoorReview);
    });
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
