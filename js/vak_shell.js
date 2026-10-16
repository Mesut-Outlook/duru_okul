/* =========================================================
   Vak-shell (2026-10-16) — één bestand voor alle 12 havo3/<vak>/-sites.
   Claude Design "Duru — toetsen & voortgang" (goedgekeurd).

   Laadt NA engine.js (laatste script in elke havo3/<vak>/index.html) en
   verandert niets aan de engines zelf:
   - eigen kop van het vak verborgen (de hub-balk toont de vaknaam al);
     de 💎🔥🏅-chips stonden voor wie alleen toetsen maakt altijd op 0
   - onderbalk Leren · Toetsen · Voortgang (vervangt de 4 hero-knoppen)
   - "Leren": volgende open toets + hoofdstukken met paragrafen als rijen
   - "Voortgang" = oude dashboard + medailles in één pagina (de oude
     dashboard-tabel liep op de telefoon 751px breed)
   - na elke render van een engine (MutationObserver op #app): resultaat
     opent met alleen de fouten, toetslijst zonder dubbele toetshistorie
   Leest dezelfde localStorage-sleutels als de engine; schrijft niets.
   ========================================================= */
(function () {
  "use strict";
  if (!window.DURU || typeof DURU.gaNaar !== "function") return;
  var app = document.getElementById("app");
  var VAK = document.documentElement.getAttribute("data-vak") || "";
  if (!app || !VAK) return;
  if (window.top !== window.self) document.documentElement.classList.add("vs-ingebed");

  function lees(sleutel) {
    try { return JSON.parse(localStorage.getItem(sleutel)) || {}; } catch (e) { return {}; }
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }
  // Zelfde regels als js/cijfer_util.js (niet geladen in de vaksites).
  function cijfer(pct) { return Math.round((1 + (pct || 0) / 100 * 9) * 10) / 10; }
  function tekst(c) { return c == null ? "—" : c.toFixed(1).replace(".", ","); }
  function klasse(c) { return c == null ? "none" : c < 5.5 ? "zwak" : c < 7 ? "net" : "goed"; }
  function pil(c) { return '<span class="vs-pil vs-pil--' + klasse(c) + '">' + tekst(c) + '</span>'; }
  function laatstePerToets(hist) {
    var gezien = {}, uit = [];
    hist.forEach(function (a) { if (a.examId && !gezien[a.examId]) { gezien[a.examId] = 1; uit.push(a); } });
    return uit;
  }
  function gem(hist) {
    var l = laatstePerToets(hist);
    if (!l.length) return null;
    return Math.round(l.reduce(function (s, a) { return s + cijfer(a.pct); }, 0) / l.length * 10) / 10;
  }
  function ico(pad, extra) {
    return '<svg class="vs-ic' + (extra ? " " + extra : "") + '" viewBox="0 0 24 24" aria-hidden="true">' + pad + '</svg>';
  }
  var IC = {
    leren: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    toetsen: '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
    voortgang: '<line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/>',
    neer: '<polyline points="6 9 12 15 18 9"/>', op: '<polyline points="18 15 12 9 6 15"/>',
    verder: '<polyline points="9 18 15 12 9 6"/>', play: '<polygon points="6 4 20 12 6 20 6 4"/>'
  };

  function data() {
    var EX = lees("duru_2627_" + VAK + "_examens_v1");
    return {
      P: lees("duru_2627_" + VAK + "_v1"),
      hist: (EX.history || []).filter(function (a) { return a && typeof a.pct === "number"; })
    };
  }
  function examensVan(nr) { return (DURU.examens || []).filter(function (e) { return e.hoofdstuk === nr; }); }
  function hfNaam(h) { return typeof DURU.hfNaam === "function" ? DURU.hfNaam(h) : "Hoofdstuk " + h.nr; }
  function hfChip(h) { return h.label ? "★" : h.nr; }

  /* Volgende open toets: eerst in het hoofdstuk waar Duru het laatst mee bezig was. */
  function volgendeToets(hist) {
    var gedaan = {};
    hist.forEach(function (a) { gedaan[a.examId] = 1; });
    var laatst = hist[0] && DURU._examenById && DURU._examenById[hist[0].examId];
    var volgorde = (DURU.hoofdstukken || []).slice();
    if (laatst && laatst.hoofdstuk != null) {
      volgorde.sort(function (a, b) { return (b.nr === laatst.hoofdstuk) - (a.nr === laatst.hoofdstuk); });
    }
    for (var i = 0; i < volgorde.length; i++) {
      var open = examensVan(volgorde[i].nr).filter(function (e) { return !gedaan[e.id]; });
      if (open.length) return { ex: open[0], h: volgorde[i] };
    }
    return null;
  }

  /* ---------- Leren ---------- */
  var openHf = null;
  function renderLeren() {
    var d = data();
    var hfs = DURU.hoofdstukken || [];
    var v = volgendeToets(d.hist);
    if (openHf == null) {
      var laatst = d.hist[0] && DURU._examenById && DURU._examenById[d.hist[0].examId];
      openHf = laatst && laatst.hoofdstuk != null ? laatst.hoofdstuk : (hfs[0] && hfs[0].nr);
    }
    var h = '<div class="vs-pagina">';
    if (v) {
      h += '<button type="button" class="vs-verder" onclick="DURU.examenStart(\'' + esc(v.ex.id) + '\')">' +
        '<span class="vs-verder-t"><small>' + (d.hist.length ? "Verder waar je was" : "Begin hier") + '</small>' +
        '<b>' + esc((v.h.label ? v.h.label : "H" + v.h.nr) + " · " + v.ex.titel) + '</b>' +
        '<span>' + v.ex.vragen.length + ' vragen · ' + (v.ex.duurMin || 20) + ' min</span></span>' +
        '<span class="vs-verder-play">' + ico(IC.play) + '</span></button>';
    }
    h += '<div class="vs-kop">Hoofdstukken</div>';
    var getoond = 0;
    hfs.forEach(function (hf) {
      var ow = DURU.onderwerpenVan ? DURU.onderwerpenVan(hf.nr) : [];
      var ex = examensVan(hf.nr);
      var ids = {};
      ex.forEach(function (e) { ids[e.id] = 1; });
      var eigen = d.hist.filter(function (a) { return ids[a.examId]; });
      var gedaan = laatstePerToets(eigen).length;
      var g = gem(eigen);
      if (!ow.length && !ex.length) return;
      getoond++;
      var open = openHf === hf.nr;
      h += '<section class="vs-hf' + (open ? " open" : "") + '">' +
        '<button type="button" class="vs-hfkop" aria-expanded="' + open + '" onclick="DURU.vsToggleHf(' + hf.nr + ')">' +
        '<span class="vs-nr vs-nr--' + (gedaan ? klasse(g) : "none") + '">' + hfChip(hf) + '</span>' +
        '<span class="vs-hft"><b>' + esc(hf.label || hf.titel) + '</b><span>' +
          (gedaan ? 'Toetsen ' + gedaan + ' / ' + ex.length + ' · gem. ' + tekst(g)
                  : (ex.length ? 'Nog niet begonnen · ' + ex.length + (ex.length === 1 ? ' toets' : ' toetsen') : ow.length + ' onderwerpen')) +
        '</span></span>' + ico(open ? IC.op : IC.neer, "vs-zacht") + '</button>';
      if (open) {
        ow.forEach(function (o) {
          var b = (d.P.beste || {})[o.id] || 0;
          h += '<button type="button" class="vs-par" onclick="DURU.gaNaar(\'theorie\',\'' + esc(o.id) + '\')">' +
            '<span class="vs-pnr">' + esc(o.paragraaf || "") + '</span><span class="vs-pt">' + esc(o.titel) + '</span>' +
            '<span class="vs-mini" title="Beste score oefenvragen: ' + b + '%"><span style="width:' + b + '%"></span></span></button>';
        });
        if (ex.length) {
          h += '<button type="button" class="vs-par vs-par--toets" onclick="DURU.vsNaarToetsen()">' +
            '<span class="vs-pnr">' + ico(IC.toetsen) + '</span><span class="vs-pt">' + ex.length +
            (ex.length === 1 ? ' proeftoets' : ' proeftoetsen') + ' van dit hoofdstuk</span>' + ico(IC.verder, "vs-zacht") + '</button>';
        }
      }
      h += '</section>';
    });
    // Vak zonder hoofdstukken (bv. maatschappijleer zolang er geen materiaal is): alles in één lijst.
    if (!getoond) {
      h = h.replace('<div class="vs-kop">Hoofdstukken</div>', '<div class="vs-kop">Oefenen</div>');
      h += '<section class="vs-hf">' + (DURU.onderwerpen || []).map(function (o) {
        return '<button type="button" class="vs-par" onclick="DURU.gaNaar(\'theorie\',\'' + esc(o.id) + '\')">' +
          '<span class="vs-pnr">' + esc(o.paragraaf || "") + '</span><span class="vs-pt">' + esc(o.titel) + '</span></button>';
      }).join("") + ((DURU.examens || []).length ? '<button type="button" class="vs-par vs-par--toets" onclick="DURU.vsNaarToetsen()">' +
        '<span class="vs-pnr">' + ico(IC.toetsen) + '</span><span class="vs-pt">Alle proeftoetsen (' + DURU.examens.length + ')</span>' +
        ico(IC.verder, "vs-zacht") + '</button>' : '') + '</section>';
    }
    h += '</div>';
    app.innerHTML = h;
    zetTab("leren");
  }
  DURU.vsToggleHf = function (nr) { openHf = openHf === nr ? -1 : nr; renderLeren(); };
  DURU.vsNaarToetsen = function () { DURU.gaNaar("examens"); };

  /* ---------- Voortgang (dashboard + medailles) ---------- */
  var toonAlleHist = false;
  function renderVoortgang() {
    // Medailles: de engine kent ze (privé); laat haar de pagina tekenen en neem de rij over.
    var medailles = "", behaald = 0, totaal = 0;
    try {
      bezig = true;
      origGaNaar("badges");
      var rij = app.querySelector(".badge-rij");
      if (rij) {
        totaal = rij.querySelectorAll(".badge").length;
        behaald = rij.querySelectorAll(".badge.behaald").length;
        medailles = rij.outerHTML;
      }
    } catch (e) { /* zonder medailles verder */ } finally { bezig = false; }

    var d = data();
    var alleEx = DURU.examens || [];
    var g = gem(d.hist);
    var beste = d.hist.length ? Math.max.apply(null, d.hist.map(function (a) { return cijfer(a.pct); })) : null;
    var gedaan = laatstePerToets(d.hist).length;

    var h = '<div class="vs-pagina">';
    h += '<div class="vs-stats">' +
      '<div class="vs-stat"><small>Gemiddeld</small><b class="vs-kl--' + klasse(g) + '">' + tekst(g) + '</b><span>laatste per toets</span></div>' +
      '<div class="vs-stat"><small>Beste</small><b class="vs-kl--' + klasse(beste) + '">' + tekst(beste) + '</b><span>' + d.hist.length + ' pogingen</span></div>' +
      '<div class="vs-stat"><small>Gemaakt</small><b>' + gedaan + '<i> / ' + alleEx.length + '</i></b><span>toetsen</span></div></div>';

    h += '<div class="vs-kop">Per hoofdstuk</div><section class="vs-kaart">';
    (DURU.hoofdstukken || []).forEach(function (hf) {
      var ex = examensVan(hf.nr);
      if (!ex.length) return;
      var ids = {};
      ex.forEach(function (e) { ids[e.id] = 1; });
      var eigen = d.hist.filter(function (a) { return ids[a.examId]; });
      var n = laatstePerToets(eigen).length, gh = gem(eigen);
      h += '<div class="vs-rij"><span class="vs-nr vs-nr--' + (n ? klasse(gh) : "none") + '">' + hfChip(hf) + '</span>' +
        '<span class="vs-rt"><b>' + esc(hf.label || hf.titel) + '</b><span class="vs-balk"><span style="width:' +
        Math.round(n / ex.length * 100) + '%"></span></span></span>' +
        '<span class="vs-tel">' + n + '/' + ex.length + '</span>' + pil(n ? gh : null) + '</div>';
    });
    h += '</section>';

    if (medailles) {
      h += '<div class="vs-kop">Medailles <span>' + behaald + ' van ' + totaal + '</span></div>' +
        '<section class="vs-kaart vs-medailles">' + medailles + '</section>';
    }

    h += '<div class="vs-kop">Toetshistorie</div>';
    if (!d.hist.length) {
      h += '<section class="vs-kaart vs-leeg">Nog geen toetsen gemaakt. Kies hieronder <b>Toetsen</b> om te beginnen.</section>';
    } else {
      var lijst = toonAlleHist ? d.hist : d.hist.slice(0, 10);
      h += '<section class="vs-kaart">' + lijst.map(function (a) {
        var kan = a.attemptId && Array.isArray(a.antwoorden);
        return '<button type="button" class="vs-rij vs-hist"' + (kan ? ' onclick="DURU.renderPastAttemptReview(\'' + esc(a.attemptId) + '\')"' : ' disabled') + '>' +
          pil(cijfer(a.pct)) + '<span class="vs-rt"><b>' + esc(a.examTitel || "Proeftoets") + '</b><span>' +
          esc(String(a.datum || "").split(" ")[0]) + ' · ' + a.goed + ' / ' + a.totaal + ' goed</span></span>' +
          (kan ? '<span class="vs-fout">Fouten ' + ico(IC.verder) + '</span>' : '') + '</button>';
      }).join("") +
      (d.hist.length > 10 ? '<button type="button" class="vs-meer" onclick="DURU.vsAlleHist()">' +
        (toonAlleHist ? "Minder tonen" : "Alle " + d.hist.length + " tonen") + '</button>' : '') + '</section>';
    }
    h += '<p class="vs-reset"><button type="button" onclick="DURU.reset()">Voortgang van dit vak wissen</button></p>';
    h += '</div>';
    app.innerHTML = h;
    zetTab("voortgang");
  }
  DURU.vsAlleHist = function () { toonAlleHist = !toonAlleHist; renderVoortgang(); };

  /* ---------- Onderbalk ---------- */
  var nav = document.createElement("nav");
  nav.className = "vs-nav";
  nav.setAttribute("aria-label", "Vak");
  nav.innerHTML = [["leren", "Leren", "home"], ["toetsen", "Toetsen", "examens"], ["voortgang", "Voortgang", "dashboard"]]
    .map(function (t) {
      return '<button type="button" data-vs-tab="' + t[0] + '" onclick="DURU.gaNaar(\'' + t[2] + '\')">' +
        ico(IC[t[0]]) + '<span>' + t[1] + '</span></button>';
    }).join("");
  document.body.appendChild(nav);
  document.body.classList.add("vs-actief");

  function zetTab(naam) {
    nav.querySelectorAll("[data-vs-tab]").forEach(function (b) {
      b.setAttribute("aria-current", b.getAttribute("data-vs-tab") === naam ? "page" : "false");
    });
  }

  /* ---------- Routes ---------- */
  var origGaNaar = DURU.gaNaar;
  var bezig = false;
  DURU.gaNaar = function (route, arg) {
    if (DURU._stopExamTimer) DURU._stopExamTimer();
    if (route === "home") { window.scrollTo(0, 0); return renderLeren(); }
    if (route === "dashboard" || route === "badges") { window.scrollTo(0, 0); return renderVoortgang(); }
    zetTab(route === "examens" ? "toetsen" : "leren");
    return origGaNaar(route, arg);
  };
  ["renderExamenLijst", "examenStart", "renderPastAttemptReview"].forEach(function (fn) {
    var orig = DURU[fn];
    if (typeof orig !== "function") return;
    DURU[fn] = function () { zetTab("toetsen"); return orig.apply(this, arguments); };
  });

  /* ---------- Na elke engine-render opruimen ---------- */
  function naRender() {
    if (bezig) return;
    // Startpagina van de engine (eerste load, of een interne renderHome) → Leren.
    if (app.querySelector(".hero.view")) return renderLeren();

    var inToets = !!app.querySelector(".dot-nav") || (!!app.querySelector(".quiz-wrap") && !app.querySelector(".resultaat"));
    document.body.classList.toggle("vs-in-toets", inToets);

    // "← Terug naar overzicht" is dubbel met de onderbalk; "← Stoppen" (toets) blijft.
    app.querySelectorAll(".terug").forEach(function (t) {
      if (/gaNaar\('home'\)/.test(t.getAttribute("onclick") || "")) t.classList.add("vs-weg");
    });

    // Toetslijst: toetshistorie staat nu in Voortgang; uitleg-alinea onder de titel weg.
    var tabel = app.querySelector(".history-table-wrapper");
    if (tabel && !app.querySelector("#review-lijst")) {
      var p = tabel.previousElementSibling;
      while (p && !p.classList.contains("sectie-titel")) { var vorige = p.previousElementSibling; p.remove(); p = vorige; }
      if (p) p.remove();
      tabel.remove();
    }
    // Toetskaarten → smalle rijen: laatste cijfer (of leeg vakje) · titel + 20 vragen · 20 min · ›.
    // Kaart-element en onclick blijven (open_toetsen.js filtert en telt op .examen-card).
    var kaarten = app.querySelectorAll(".examen-card:not([data-vs])");
    if (kaarten.length && !app.querySelector("#review-lijst")) {
      var hist = data().hist;
      kaarten.forEach(function (k) {
        var m = /examenStart\('([^']+)'\)/.exec(k.getAttribute("onclick") || "");
        var ex = m && DURU._examenById && DURU._examenById[m[1]];
        if (!ex) return;
        k.setAttribute("data-vs", "1");
        var eigen = hist.filter(function (a) { return a.examId === ex.id; });
        k.innerHTML = (eigen.length ? pil(cijfer(eigen[0].pct)) : '<span class="vs-open" aria-label="Nog niet gemaakt"></span>') +
          '<span class="vs-rt"><b>' + esc(ex.titel) + '</b><span>' + ex.vragen.length + ' vragen · ' + (ex.duurMin || 20) + ' min' +
          (eigen.length ? ' · ' + eigen.length + '× gemaakt' : '') + '</span></span>' + ico(IC.verder, "vs-zacht");
        k.classList.add("vs-kort");
      });
    }

    var eerste = app.querySelector(".sectie-titel");
    if (eerste && eerste.nextElementSibling && eerste.nextElementSibling.tagName === "P" && app.querySelector(".examen-card")) {
      eerste.nextElementSibling.classList.add("vs-weg");
    }

    // Resultaat/review: standaard alleen fouten; knoppen Fout (n) / Alles.
    var lijst = app.querySelector("#review-lijst");
    if (lijst && !lijst.dataset.vs) {
      lijst.dataset.vs = "1";
      var fout = lijst.querySelectorAll('.review-item:not([data-status="goed"])').length;
      var rij = app.querySelector(".filter-rij");
      if (rij) {
        rij.classList.add("vs-seg");
        rij.innerHTML = '<button type="button" data-f="fout">Fout (' + fout + ')</button><button type="button" data-f="alle">Alles</button>';
        var zet = function (f) {
          DURU.reviewFilter(f);
          rij.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-f") === f)); });
        };
        rij.querySelectorAll("button").forEach(function (b) { b.addEventListener("click", function () { zet(b.getAttribute("data-f")); }); });
        zet(fout ? "fout" : "alle");
        if (rij.previousElementSibling && rij.previousElementSibling.tagName === "P") rij.previousElementSibling.classList.add("vs-weg");
      }
      app.querySelectorAll('.acties .btn[onclick*="gaNaar(\'home\')"]').forEach(function (b) { b.classList.add("vs-weg"); });
    }
  }
  new MutationObserver(function () { naRender(); }).observe(app, { childList: true });

  // De engine tekent de startpagina op DOMContentLoaded (vóór of na ons): vang beide.
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", naRender);
  else naRender();
})();
