/* =========================================================
   js/ouder_analyse.js — "Gelişim analizi" voor het ouderpaneel (2026-11-08)
   Pure functies, schrijft niets. Input = de pogingen-items die
   ouder_dashboard.js → collectParentReportData() al bouwt
   ({examId, hoofdstuk, cijfer, timestamp, ruw:{antwoorden, beoordelingen}}).
   Per vak → hoofdstuk → paragraaf: toetsen / gemaakt / gemiddelde laatste poging /
   gidiş / leeg-percentage, plus "dikkat noktaları" (regels hieronder) en handmatige
   notities uit js/ouder_notities.js (geschreven bij de zwakte-analyse, skill zwakte-toetsen).
   Manifest: DURU_HOOFDSTUKKEN.vakken[vak].examenInfo[id] = [titel, datum, paragraaf, typen].
   Laadvolgorde: hoofdstukken.js → hoofdstuk_util.js → cijfer_util.js → ouder_notities.js → ouder_analyse.js.
   ========================================================= */
(function () {
  "use strict";
  var C = window.DURU_CIJFER;

  function info(vakId) {
    var m = window.DURU_HOOFDSTUKKEN && window.DURU_HOOFDSTUKKEN.vakken[vakId];
    return m || { hoofdstukken: [], examenHoofdstuk: {}, examenInfo: {} };
  }
  function parLabel(p) {
    return { "": "Genel", mix: "Karışık", eind: "Eindtoets", begrippen: "Begrippen" }[p] ||
      (/^\d/.test(p) ? "§" + p : p);
  }
  function parSort(p) {   // §'ler sırayla, sonra begrippen / karışık / eind / genel
    if (/^\d/.test(p)) return p.split(".").map(function (n) { return ("000" + n).slice(-3); }).join(".");
    return { begrippen: "x1", mix: "x2", eind: "x3", "": "x4" }[p] || "x5" + p;
  }
  function isLeeg(antw, i) {
    return !antw || i >= antw.length || antw[i] === null || antw[i] === undefined || antw[i] === "";
  }
  function status(cijfer, gemaakt) {
    if (!gemaakt) return "leeg";
    if (cijfer < C.DREMPEL) return "zwak";
    if (cijfer < 7) return "net";
    if (C.examenklaar(cijfer) && gemaakt >= 2) return "klaar";
    return "goed";
  }
  // gidiş = gemiddelde laatste 3 pogingen vs de 3 daarvoor (zelfde regel als de rest van het paneel)
  function gidis(chrono) {
    if (chrono.length < 4) return null;
    var n = Math.min(3, chrono.length - 3 >= 3 ? 3 : chrono.length - 3);
    var laatste = chrono.slice(-3), eerder = chrono.slice(-3 - n, -3);
    return C.gemiddelde(laatste, "cijfer") - C.gemiddelde(eerder, "cijfer");
  }
  function pct(a, b) { return b ? Math.round(100 * a / b) : 0; }

  function vak(vakId, items) {
    var M = info(vakId), ei = M.examenInfo || {};
    var chrono = (items || []).slice().sort(function (a, b) { return a.timestamp - b.timestamp; });

    // vraag-niveau tellingen (alleen pogingen met antwoorden, d.w.z. 2026-2027)
    var q = { n: 0, leeg: 0, begin: [0, 0], eind: [0, 0], open: [0, 0] };
    var parLeeg = {};
    chrono.forEach(function (a) {
      var r = a.ruw || {}, b = r.beoordelingen, antw = r.antwoorden;
      if (!Array.isArray(b) || !Array.isArray(antw)) return;
      var e = ei[a.examId] || [], typen = (e[3] && e[3].length === b.length) ? e[3] : "";
      var p = e[2] || "", pl = parLeeg[a.hoofdstuk + "|" + p] || (parLeeg[a.hoofdstuk + "|" + p] = [0, 0]);
      b.forEach(function (_, i) {
        var l = isLeeg(antw, i) ? 1 : 0;
        if (typen[i] === "o") { q.open[0]++; q.open[1] += l; return; }
        q.n++; q.leeg += l; pl[0]++; pl[1] += l;
        var deel = i < b.length / 3 ? q.begin : i >= 2 * b.length / 3 ? q.eind : null;
        if (deel) { deel[0]++; deel[1] += l; }
      });
    });

    // structuur hoofdstuk → paragraaf
    var hfs = (M.hoofdstukken || []).map(function (h) {
      return { nr: h.nr, naam: window.DURU_HF ? window.DURU_HF.kort(vakId, h.nr) : "H" + h.nr,
        titel: h.titel, par: {}, pogingen: [] };
    });
    var hfIdx = {}; hfs.forEach(function (h) { hfIdx[h.nr] = h; });
    Object.keys(M.examenHoofdstuk || {}).forEach(function (id) {
      var h = hfIdx[M.examenHoofdstuk[id]]; if (!h) return;
      var p = (ei[id] || [])[2] || "";
      (h.par[p] || (h.par[p] = { p: p, label: parLabel(p), toetsen: 0, ids: {}, pogingen: [] })).toetsen++;
      h.par[p].ids[id] = true;
    });
    chrono.forEach(function (a) {
      var h = hfIdx[a.hoofdstuk]; if (!h) return;
      h.pogingen.push(a);
      var p = (ei[a.examId] || [])[2] || "";
      if (h.par[p] && h.par[p].ids[a.examId]) h.par[p].pogingen.push(a);
    });

    var actief = hfs.filter(function (h) { return h.pogingen.length; });
    actief.forEach(function (h) {
      h.cijfer = C.gemiddeldeLaatste(h.pogingen, "cijfer");
      h.paragrafen = Object.keys(h.par).sort(function (a, b) { return parSort(a) < parSort(b) ? -1 : 1; })
        .map(function (k) {
          var x = h.par[k], laatste = C.laatstePerToets(x.pogingen), pl = parLeeg[h.nr + "|" + k] || [0, 0];
          x.gemaakt = laatste.length;
          x.cijfer = x.gemaakt ? C.gemiddeldeLaatste(x.pogingen, "cijfer") : null;
          x.gidis = gidis(x.pogingen);
          x.leegPct = pct(pl[1], pl[0]);
          x.status = status(x.cijfer, x.gemaakt);
          delete x.ids;
          return x;
        });
      h.status = status(h.cijfer, C.laatstePerToets(h.pogingen).length);
    });

    // ---- dikkat noktaları (ernst: hoog > mid > info > goed) ----
    var punten = [];
    function punt(ernst, tekst) { punten.push({ ernst: ernst, tekst: tekst }); }
    actief.forEach(function (h) {
      var klaar = [];
      h.paragrafen.forEach(function (x) {
        var waar = x.p ? h.naam + " " + x.label : h.naam;
        if (x.status === "leeg" && /^\d/.test(x.p))
          punt("mid", waar + " henüz hiç çalışılmadı — " + x.toetsen + " test bekliyor.");
        else if (x.status === "zwak" && x.gemaakt >= 2)
          punt("hoog", waar + ": son denemelerin ortalaması " + C.tekst(x.cijfer) + " — bu konu tekrar çalışılmalı.");
        else if (x.status === "net" && x.gemaakt >= 2)
          punt("mid", waar + ": ortalama " + C.tekst(x.cijfer) + " — geçiyor ama sağlam değil.");
        if (x.gidis !== null && x.gidis <= -1)
          punt("mid", waar + " düşüşte (son 3 test öncekilerden " + C.tekst(-x.gidis) + " puan düşük).");
        if (x.leegPct >= 20 && x.gemaakt >= 2)
          punt("mid", waar + ": boş bıraktığı soru oranı %" + x.leegPct + ".");
        if (x.status === "klaar") klaar.push(x.label);
      });
      if (klaar.length) punt("goed", h.naam + " sınava hazır" + (klaar[0] === "Genel" ? "." : ": " + klaar.join(", ") + "."));
    });
    var leegPct = pct(q.leeg, q.n), lb = pct(q.begin[1], q.begin[0]), le = pct(q.eind[1], q.eind[0]);
    // vak-brede punten krijgen een `soort` → overzicht() bundelt ze over alle vakken
    if (leegPct >= 10) punten.push({ ernst: leegPct >= 20 ? "hoog" : "mid", soort: "leeg",
      tekst: "Boş bıraktığı soru oranı %" + leegPct + " (açık sorular hariç)." });
    if (le >= 15 && le >= 2 * Math.max(lb, 1)) punten.push({ ernst: "mid", soort: "eind",
      tekst: "Boş bırakma testin sonuna doğru artıyor: başta %" + lb + ", sonda %" + le + "." });
    var openPct = pct(q.open[1], q.open[0]);
    if (q.open[0] >= 5 && openPct >= 50) punten.push({ ernst: "hoog", soort: "open",
      tekst: "Açık soruların %" + openPct + " kadarı boş." });

    var notities = (window.DURU_OUDER_NOTITIES || {})[vakId];
    if (notities) notities.punten.forEach(function (n) {
      punten.push({ ernst: n.ernst || "mid", tekst: n.tekst, notitie: notities.datum });
    });
    var rang = { hoog: 0, mid: 1, info: 2, goed: 3 };
    punten.sort(function (a, b) { return rang[a.ernst] - rang[b.ernst]; });

    return {
      vakId: vakId, pogingen: chrono.length,
      cijfer: C.gemiddeldeLaatste(chrono, "cijfer"),
      leegPct: leegPct, leegBegin: lb, leegEind: le, openN: q.open[0], openLeegPct: openPct,
      hoofdstukken: actief, punten: punten
    };
  }

  // Over alle vakken: vak-brede patronen gebundeld + de belangrijkste concrete punten.
  function overzicht(lijst) {
    var uit = [], open = lijst.filter(function (a) { return a.openN >= 5; });
    var openVeel = open.filter(function (a) { return a.openLeegPct >= 50; });
    if (openVeel.length) {
      var n = 0, l = 0;
      open.forEach(function (a) { n += a.openN; l += Math.round(a.openN * a.openLeegPct / 100); });
      uit.push({ ernst: "hoog", soort: "open", tekst: "Açık (yazılı) soruları çoğunlukla boş bırakıyor: " +
        (openVeel.length === open.length ? open.length + " dersin hepsinde" : open.length + " dersin " + openVeel.length + "'inde") +
        " yarıdan fazlası boş (toplam %" + pct(l, n) +
        "). Kısa bir cümle bile puan getirir — bunu konuşmak en hızlı kazanç." });
    }
    var eind = lijst.filter(function (a) { return a.punten.some(function (p) { return p.soort === "eind"; }); });
    if (eind.length >= 2) uit.push({ ernst: "mid", soort: "eind", tekst: "Testin son üçte birinde daha çok soru boş kalıyor (" +
      eind.map(function (a) { return a.titel; }).join(", ") + ") — süreyi yönetmek veya önce bildiği soruları yapmak işe yarar." });
    var rang = { hoog: 0, mid: 1 }, concreet = [];
    lijst.forEach(function (a) {
      a.punten.forEach(function (p) {
        if (!p.soort && rang[p.ernst] !== undefined) concreet.push({ ernst: p.ernst, vak: a.titel, vakId: a.vakId, tekst: p.tekst, notitie: p.notitie });
      });
    });
    concreet.sort(function (a, b) { return rang[a.ernst] - rang[b.ernst]; });
    return { algemeen: uit, punten: concreet };
  }

  window.DURU_ANALYSE = { vak: vak, overzicht: overzicht, parLabel: parLabel };
})();
