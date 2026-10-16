/* =========================================================
   Duru's Schoolhub — Hoofdstuk Utility (DURU_HF)
   Enkele, gedeelde helper voor hoofdstuk-informatie op basis
   van het gegenereerde manifest window.DURU_HOOFDSTUKKEN
   (zie js/hoofdstukken.js). Gebruikt door zowel js/dashboard.js
   als js/ouder_dashboard.js — geen eigen hoofdstuk-data hier,
   alleen lookup-logica.
   ========================================================= */

(function () {
  "use strict";

  // ── Manifest-toegang ───────────────────────────────────────
  function manifestVakken() {
    return (window.DURU_HOOFDSTUKKEN && window.DURU_HOOFDSTUKKEN.vakken) || {};
  }

  function vakData(vakId) {
    if (!vakId) return null;
    var id = String(vakId).toLowerCase();
    var vakken = manifestVakken();
    return vakken[id] || null;
  }

  // ── lijst(vakId): alle hoofdstukken van een vak ────────────
  function lijst(vakId) {
    var vd = vakData(vakId);
    if (!vd || !vd.hoofdstukken || !vd.hoofdstukken.length) return [];

    return vd.hoofdstukken.map(function (h) {
      return {
        nr: h.nr,
        label: h.label,
        titel: h.titel,
        icoon: h.icoon || "📖",
        intro: h.intro || "",
        aantalExamens: totaalExamens(vakId, h.nr),
        aantalOnderwerpen: totaalOnderwerpen(vakId, h.nr)
      };
    });
  }

  // ── meta(vakId, nr): metadata van één hoofdstuk of null ────
  function meta(vakId, nr) {
    var vd = vakData(vakId);
    if (!vd || !vd.hoofdstukken) return null;

    for (var i = 0; i < vd.hoofdstukken.length; i++) {
      if (vd.hoofdstukken[i].nr === nr) {
        var h = vd.hoofdstukken[i];
        return {
          nr: h.nr,
          titel: h.titel,
          icoon: h.icoon || "📖",
          intro: h.intro || ""
        };
      }
    }
    return null;
  }

  // ── vanAttempt(att, vakId): hoofdstuk van een poging, of null ──
  // Volgorde (eerste match wint, geen gokwerk):
  //   1. manifest examenHoofdstuk[att.examId] (actueel: wiskunde Statistiek ging van 2 → 90)
  //   2. att.hoofdstuk (in de poging opgeslagen)
  //   3. att.examTitel / att.titel matcht /Hoofdstuk\s*(\d+)/i
  //   4. geen match → null (examId zegt niets: "ex-h3-..." is het niveau)
  function vanAttempt(att, vakId) {
    if (!att) return null;
    var vid = vakId || att.vakId;
    var nr = null;

    var vd = vakData(vid);
    if (vd && vd.examenHoofdstuk && att.examId !== undefined && att.examId !== null &&
        vd.examenHoofdstuk[att.examId] !== undefined) {
      nr = vd.examenHoofdstuk[att.examId];
    } else {
      if (att.hoofdstuk !== undefined && att.hoofdstuk !== null) {
        nr = att.hoofdstuk;
      } else {
        // LET OP: uit het examId valt GEEN hoofdstuk af te leiden. Alle ids zien
        // eruit als "ex-h3-<vak>-N", waarbij h3 het NIVEAU (HAVO 3) is en niet het
        // hoofdstuk. Alleen een expliciete "Hoofdstuk N" in de titel is betrouwbaar.
        var titelBron = att.examTitel || att.titel;
        var t = (titelBron !== undefined && titelBron !== null) ? String(titelBron) : "";
        var tm = t.match(/Hoofdstuk\s*(\d+)/i);
        if (tm) {
          nr = parseInt(tm[1], 10);
        }
      }
    }

    if (nr === null || nr === undefined || isNaN(nr)) return null;

    var m2 = meta(vid, nr);
    var titel = (m2 && m2.titel) ? m2.titel : (att.hoofdstukTitel || ("Hoofdstuk " + nr));
    var icoon = (m2 && m2.icoon) ? m2.icoon : "📖";

    return { nr: nr, titel: titel, icoon: icoon };
  }

  // ── vanOnderwerp(vakId, onderwerpId): hoofdstuk-nr of null ──
  function vanOnderwerp(vakId, onderwerpId) {
    var vd = vakData(vakId);
    if (!vd || !vd.onderwerpHoofdstuk || onderwerpId === undefined || onderwerpId === null) {
      return null;
    }
    var nr = vd.onderwerpHoofdstuk[onderwerpId];
    return (nr === undefined) ? null : nr;
  }

  // ── totaalExamens(vakId, nr): aantal proeftoetsen (0 = onbekend) ──
  function totaalExamens(vakId, nr) {
    var vd = vakData(vakId);
    if (!vd || !vd.aantalExamens) return 0;
    var v = vd.aantalExamens[String(nr)];
    return (typeof v === "number") ? v : 0;
  }

  // ── totaalOnderwerpen(vakId, nr): aantal onderwerpen (0 = onbekend) ──
  function totaalOnderwerpen(vakId, nr) {
    var vd = vakData(vakId);
    if (!vd || !vd.aantalOnderwerpen) return 0;
    var v = vd.aantalOnderwerpen[String(nr)];
    return (typeof v === "number") ? v : 0;
  }

  // ── kort(vakId, nr): "H2", of het label van een niet-boekhoofdstuk ("Herhaling MAVO 2") ──
  function kort(vakId, nr) {
    var h = (vakData(vakId) || {}).hoofdstukken || [];
    for (var i = 0; i < h.length; i++) if (h[i].nr === nr && h[i].label) return h[i].label;
    return "H" + nr;
  }

  window.DURU_HF = {
    kort: kort,
    lijst: lijst,
    meta: meta,
    vanAttempt: vanAttempt,
    vanOnderwerp: vanOnderwerp,
    totaalExamens: totaalExamens,
    totaalOnderwerpen: totaalOnderwerpen
  };
})();
