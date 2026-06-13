/* =========================================================
   Duru's Wiskunde Academie — Oefentoetsen (Examen-modus)
   Apart van de oefenquiz. Gebruikt een EIGEN opslag-sleutel,
   dus de XP/medailles/scores van de gewone oefeningen blijven
   altijd onaangeroerd.
   ========================================================= */
(function () {
  "use strict";

  /* ---------- Registratie ---------- */
  DURU.examens = DURU.examens || [];
  DURU._examenById = {};
  DURU.registerExamen = function (ex) {
    if (!ex || !ex.id) return;
    ex.vragen = ex.vragen || [];
    DURU.examens.push(ex);
    DURU._examenById[ex.id] = ex;
  };

  /* ---------- Eigen opslag (raakt de oefen-voortgang NIET) ---------- */
  var EX_SLEUTEL = "duru_wiskunde_examens_v1";
  function laadEx() {
    try {
      var d = JSON.parse(localStorage.getItem(EX_SLEUTEL));
      if (d) {
        d.history = d.history || [];
        return d;
      }
    } catch (e) {}
    return { beste: {}, laatste: {}, history: [] };
  }
  function bewaarEx() { try { localStorage.setItem(EX_SLEUTEL, JSON.stringify(EX)); } catch (e) {} }
  var EX = laadEx();

  var app = function () { return document.getElementById("app"); };
  function esc(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  /* ---------- Timer (wordt netjes gestopt bij verlaten) ---------- */
  var T = null; // examen-state
  DURU._stopExamTimer = function () { if (T && T.interval) { clearInterval(T.interval); T.interval = null; } };

  /* ---------- Lijst met oefentoetsen ---------- */
  DURU.renderExamenLijst = function () {
    DURU._stopExamTimer();
    var h = '<div class="terug" onclick="DURU.gaNaar(\'home\')">← Terug naar overzicht</div>';
    h += '<div class="sectie-titel"><h3>📝 Oefentoetsen</h3><div class="lijn"></div></div>';
    h += '<p style="margin:0 4px 16px;color:var(--grijs)">Doe een toets op tijd, net als op school! Je krijgt aan het eind je cijfer én bij elke vraag te zien <b>hoe je het moet doen</b>. Deze toetsen tellen los van je oefen-punten — daar gebeurt niets mee.</p>';
    h += '<div class="examen-lijst">';
    DURU.examens.forEach(function (ex) {
      var best = EX.beste[ex.id];
      h += '<div class="examen-card" onclick="DURU.examenStart(\'' + ex.id + '\')">' +
        '<div class="ex-ico">' + (ex.icoon || "📝") + '</div>' +
        '<h4>' + esc(ex.titel) + '</h4>' +
        '<div class="ex-meta">' + esc(ex.vak || "") + '<br><b>' + ex.vragen.length + ' vragen</b> · ⏱️ ' + (ex.duurMin || 20) + ' min</div>' +
        (best != null
          ? '<div class="ex-best" style="color:' + (best >= 55 ? 'var(--groen)' : 'var(--oranje)') + '">Beste cijfer: ' + cijfer(best) + ' (' + best + '%)</div>'
          : '<div class="ex-best" style="color:var(--grijs-licht)">Nog niet gemaakt</div>') +
        '<div style="margin-top:14px"><span class="btn klein">▶️ Start toets</span></div>' +
        '</div>';
    });
    h += '</div>';

    // Toetshistorie & Foutanalyse sectie
    EX.history = EX.history || [];
    if (EX.history.length > 0) {
      h += '<div class="sectie-titel" style="margin-top:40px"><h3>📜 Jouw toetshistorie & foutanalyse</h3><div class="lijn"></div></div>';
      h += '<p style="margin:0 4px 16px;color:var(--grijs)">Bekijk hier je gemaakte proeftoetsen terug. Je kunt precies zien welke vragen je fout had en de uitleg opnieuw doorlezen!</p>';
      h += '<div class="history-table-wrapper" style="overflow-x:auto; background:var(--wit); border-radius:18px; box-shadow:var(--schaduw); border:1px solid var(--lijn); padding:16px;">';
      h += '<table class="nask" style="width:100%; border-collapse:collapse;">';
      h += '<thead><tr style="border-bottom:2px solid var(--lijn);"><th>Datum</th><th>Toets</th><th>Goed</th><th>Cijfer</th><th style="text-align:right;">Actie</th></tr></thead>';
      h += '<tbody>';
      EX.history.forEach(function (att) {
        var c = cijfer(att.pct);
        var cls = att.pct >= 55 ? 'color:var(--groen); font-weight:800;' : 'color:var(--oranje); font-weight:800;';
        h += '<tr style="border-bottom:1px solid var(--lijn);">';
        h += '<td>' + att.datum + '</td>';
        h += '<td style="text-align:left;"><b>' + esc(att.examTitel) + '</b></td>';
        h += '<td>' + att.goed + ' / ' + att.totaal + '</td>';
        h += '<td style="' + cls + '">' + c + ' (' + att.pct + '%)</td>';
        h += '<td style="text-align:right;"><button class="btn klein" style="padding:6px 12px; font-size:12px;" onclick="DURU.renderPastAttemptReview(\'' + att.attemptId + '\')">🔍 Review</button></td>';
        h += '</tr>';
      });
      h += '</tbody></table></div>';
    }

    app().innerHTML = h;
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  function cijfer(pct) {
    // Nederlands schoolcijfer 1–10 (10% = 1, 100% = 10), 1 decimaal
    var c = 1 + (pct / 100) * 9;
    return (Math.round(c * 10) / 10).toString().replace(".", ",");
  }

  /* ---------- Start ---------- */
  DURU.examenStart = function (id) {
    var ex = DURU._examenById[id];
    if (!ex) return DURU.renderExamenLijst();
    DURU._stopExamTimer();
    T = {
      ex: ex,
      i: 0,
      antwoorden: new Array(ex.vragen.length).fill(null),
      resterend: (ex.duurMin || 20) * 60,
      interval: null,
      klaar: false
    };
    T.interval = setInterval(tik, 1000);
    renderVraag();
  };

  function tik() {
    if (!T) return;
    T.resterend--;
    var el = document.getElementById("ex-timer");
    if (el) {
      el.textContent = "⏱️ " + mmss(T.resterend);
      if (T.resterend <= 60) el.parentElement.classList.add("bijna");
    }
    if (T.resterend <= 0) { DURU._stopExamTimer(); levereIn(true); }
  }
  function mmss(s) { var m = Math.floor(s / 60), r = s % 60; return (m < 10 ? "0" : "") + m + ":" + (r < 10 ? "0" : "") + r; }

  /* ---------- Vraag renderen ---------- */
  function renderVraag() {
    var ex = T.ex, v = ex.vragen[T.i], n = ex.vragen.length;
    var gegeven = T.antwoorden[T.i];

    var h = '<div class="terug" onclick="DURU.examenAfbreken()">← Stoppen</div>';
    h += '<div class="kaart view"><div class="quiz-wrap">';

    h += '<div class="examen-top">' +
      '<span class="ex-titel">' + (ex.icoon || "📝") + ' ' + esc(ex.titel) + '</span>' +
      '<span class="timer"><span id="ex-timer">⏱️ ' + mmss(T.resterend) + '</span></span>' +
      '<span class="ex-info">Vraag ' + (T.i + 1) + ' van ' + n + '</span>' +
      '</div>';
    h += '<div class="examen-voortgang"><span style="width:' + ((T.i + 1) / n * 100) + '%"></span></div>';

    h += '<div class="vraag-kaart">';
    h += '<div style="font-size:12px;font-weight:800;color:var(--grijs-licht);letter-spacing:.5px">VRAAG ' + (T.i + 1) + '</div>';
    h += '<div class="vraag-tekst">' + v.vraag + '</div>';
    if (v.figuur) h += '<div class="vraag-figuur">' + v.figuur + '</div>';

    if (v.type === "mc" || v.type === "waaronwaar") {
      var opties = v.type === "waaronwaar" ? ["Waar", "Onwaar"] : v.opties;
      h += '<div class="opties">';
      opties.forEach(function (opt, idx) {
        var letter = v.type === "waaronwaar" ? (idx === 0 ? "✔" : "✗") : String.fromCharCode(65 + idx);
        var sel = gegeven === idx ? " gekozen" : "";
        h += '<button class="optie' + sel + '" onclick="DURU.examenKies(' + idx + ')">' +
          '<span class="letter">' + letter + '</span><span>' + esc(opt) + '</span></button>';
      });
      h += '</div>';
    } else if (v.type === "open") {
      h += '<textarea class="open-veld" id="ex-open" placeholder="Typ hier je antwoord..." oninput="DURU.examenTyp(this.value)">' + esc(gegeven || "") + '</textarea>';
      h += '<div class="veld-hint">Let op je spelling — dit wordt automatisch nagekeken.</div>';
    } else if (v.type === "invul") {
      h += '<input class="invul-veld" id="ex-open" autocomplete="off" placeholder="Typ hier je antwoord..." value="' + esc(gegeven || "") + '" oninput="DURU.examenTyp(this.value)">';
      h += '<div class="veld-hint">Let op je spelling — dit wordt automatisch nagekeken.</div>';
    }
    h += '</div>';

    // dot-navigatie
    h += '<div class="dot-nav">';
    for (var d = 0; d < n; d++) {
      var cls = "dot";
      if (T.antwoorden[d] !== null && T.antwoorden[d] !== "") cls += " beantwoord";
      if (d === T.i) cls += " huidig";
      h += '<button class="' + cls + '" onclick="DURU.examenGa(' + d + ')">' + (d + 1) + '</button>';
    }
    h += '</div>';

    h += '<div class="examen-knoppen">';
    h += T.i > 0 ? '<button class="btn ghost klein" onclick="DURU.examenGa(' + (T.i - 1) + ')">← Vorige</button>' : '<span></span>';
    if (T.i < n - 1) h += '<button class="btn klein" onclick="DURU.examenGa(' + (T.i + 1) + ')">Volgende →</button>';
    else h += '<button class="btn teal klein" onclick="DURU.examenInleveren()">✅ Inleveren</button>';
    h += '</div>';

    h += '</div></div>';
    app().innerHTML = h;
    var f = document.getElementById("ex-open");
    if (f) f.focus();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  /* ---------- Interactie ---------- */
  DURU.examenKies = function (idx) { T.antwoorden[T.i] = idx; renderVraag(); };
  DURU.examenTyp = function (val) { T.antwoorden[T.i] = val; var dot = document.querySelectorAll(".dot")[T.i]; if (dot) { if (val && val.trim()) dot.classList.add("beantwoord"); else dot.classList.remove("beantwoord"); } };
  DURU.examenGa = function (idx) { if (idx < 0 || idx >= T.ex.vragen.length) return; T.i = idx; renderVraag(); };

  DURU.examenAfbreken = function () {
    if (confirm("Wil je stoppen met de toets? Je antwoorden worden NIET opgeslagen.")) {
      DURU._stopExamTimer(); T = null; DURU.renderExamenLijst();
    }
  };

  DURU.examenInleveren = function () {
    var onbeantwoord = T.antwoorden.filter(function (a) { return a === null || a === ""; }).length;
    var msg = onbeantwoord > 0
      ? "Je hebt nog " + onbeantwoord + " vraag/vragen niet beantwoord. Toch inleveren?"
      : "Klaar? Lever je toets in en bekijk je cijfer!";
    if (confirm(msg)) levereIn(false);
  };

  /* ---------- Nakijken ---------- */
  function normaliseer(s) {
    return String(s == null ? "" : s).toLowerCase()
      .replace(/[.,;:!?'"()·]/g, " ")
      .replace(/\s+/g, " ").trim();
  }
  function beoordeel(v, antw) {
    // geeft "goed" | "fout" | "deels" + of het meetelt als goed
    if (v.type === "mc") {
      return { status: antw === v.antwoord ? "goed" : "fout", punt: antw === v.antwoord ? 1 : 0 };
    }
    if (v.type === "waaronwaar") {
      var juist = (v.antwoord === true || v.antwoord === "waar" || v.antwoord === 0) ? 0 : 1;
      return { status: antw === juist ? "goed" : "fout", punt: antw === juist ? 1 : 0 };
    }
    if (v.type === "invul") {
      var inv = normaliseer(antw);
      var alts = String(v.antwoord).split("|").map(normaliseer);
      var ok = inv !== "" && alts.some(function (a) { return inv === a || inv.indexOf(a) !== -1; });
      return { status: ok ? "goed" : "fout", punt: ok ? 1 : 0 };
    }
    // open: tel sleutelwoorden
    var tekst = normaliseer(antw);
    if (!tekst) return { status: "fout", punt: 0 };
    var sleutels = (v.sleutelwoorden || []).map(normaliseer);
    var nodig = v.minTreffers || Math.max(1, Math.ceil(sleutels.length / 2));
    var treffers = 0;
    sleutels.forEach(function (woordgroep) {
      // een "sleutel" mag meerdere alternatieven hebben gescheiden door /
      var alt = woordgroep.split("/").map(function (x) { return x.trim(); });
      if (alt.some(function (a) { return a && tekst.indexOf(a) !== -1; })) treffers++;
    });
    if (sleutels.length === 0) return { status: tekst.length > 3 ? "deels" : "fout", punt: tekst.length > 3 ? 1 : 0 };
    if (treffers >= sleutels.length) return { status: "goed", punt: 1 };
    if (treffers >= nodig) return { status: "deels", punt: 1 };
    if (treffers > 0) return { status: "deels", punt: 0 };
    return { status: "fout", punt: 0 };
  }

  function levereIn(autoTijd) {
    DURU._stopExamTimer();
    T.klaar = true;
    var ex = T.ex, n = ex.vragen.length, goed = 0;
    var beoordelingen = ex.vragen.map(function (v, i) {
      var b = beoordeel(v, T.antwoorden[i]);
      goed += b.punt;
      return b;
    });
    var pct = Math.round((goed / n) * 100);
    if (EX.beste[ex.id] == null || pct > EX.beste[ex.id]) EX.beste[ex.id] = pct;
    EX.laatste[ex.id] = pct;

    // Sla de poging op in de geschiedenis
    var attemptId = "att_" + Date.now();
    var datumStr = new Date().toLocaleString("nl-NL", { day: "2-digit", month: "2-digit", year: "numeric", hour: "2-digit", minute: "2-digit" });
    
    var historyEntry = {
      attemptId: attemptId,
      examId: ex.id,
      examTitel: ex.titel,
      datum: datumStr,
      goed: goed,
      totaal: n,
      pct: pct,
      antwoorden: JSON.parse(JSON.stringify(T.antwoorden)),
      beoordelingen: JSON.parse(JSON.stringify(beoordelingen))
    };
    EX.history = EX.history || [];
    EX.history.unshift(historyEntry); // Poging toevoegen aan het begin

    bewaarEx();
    renderResultaat(pct, goed, n, beoordelingen, autoTijd);
  }

  /* ---------- Resultaat + review (hoe doe je het) ---------- */
  function renderResultaat(pct, goed, n, beoord, autoTijd) {
    var ex = T.ex;
    var c = cijfer(pct);
    var emoji, kop;
    if (pct >= 80) { emoji = "🏆"; kop = "Uitmuntend!"; }
    else if (pct >= 55) { emoji = "🎉"; kop = "Geslaagd!"; }
    else if (pct >= 40) { emoji = "💪"; kop = "Bijna! Nog even oefenen."; }
    else { emoji = "📚"; kop = "Eerst nog wat oefenen."; }

    var omtrek = 2 * Math.PI * 70, vol = omtrek * (1 - pct / 100);
    var h = '<div class="kaart view"><div class="resultaat">';
    if (autoTijd) h += '<div class="info-box let-op" style="text-align:left"><span class="kop">⏰ De tijd was om!</span> Je toets is automatisch ingeleverd.</div>';
    h += '<div class="emoji">' + emoji + '</div><h2>' + kop + '</h2>';
    h += '<div class="score-ring"><svg width="170" height="170">' +
      '<circle cx="85" cy="85" r="70" fill="none" stroke="#e2e8f0" stroke-width="14"/>' +
      '<circle cx="85" cy="85" r="70" fill="none" stroke="url(#g2)" stroke-width="14" stroke-linecap="round" stroke-dasharray="' + omtrek + '" stroke-dashoffset="' + vol + '" transform="rotate(-90 85 85)"/>' +
      '<defs><linearGradient id="g2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d9488"/><stop offset="1" stop-color="#14b8a6"/></linearGradient></defs>' +
      '</svg><div class="pct">' + c + '</div></div>';
    h += '<div class="samenvatting"><b>' + goed + ' van de ' + n + '</b> goed · ' + pct + '% · cijfer <b>' + c + '</b></div>';
    h += '<div class="acties">' +
      '<button class="btn teal" onclick="DURU.examenStart(\'' + ex.id + '\')">🔁 Opnieuw maken</button>' +
      '<button class="btn ghost" onclick="DURU.renderExamenLijst()">📝 Andere toets</button>' +
      '<button class="btn oranje" onclick="DURU.gaNaar(\'home\')">🏠 Home</button>' +
      '</div></div></div>';

    // Review
    h += '<div class="sectie-titel" style="margin-top:30px"><h3>🔎 Nakijken — zo doe je het</h3><div class="lijn"></div></div>';
    h += '<p style="margin:0 4px 8px;color:var(--grijs)">Bekijk bij elke vraag het goede antwoord en de uitleg. Zo leer je het voor de échte toets!</p>';
    h += '<div class="filter-rij">' +
      '<button class="btn ghost klein" onclick="DURU.reviewFilter(\'alle\')">Alles</button>' +
      '<button class="btn ghost klein" onclick="DURU.reviewFilter(\'fout\')">Alleen fout/deels</button></div>';
    h += '<div id="review-lijst">';
    ex.vragen.forEach(function (v, i) {
      h += reviewItem(v, i, T.antwoorden[i], beoord[i]);
    });
    h += '</div>';

    app().innerHTML = h;
    if (pct >= 55) DURU._confettiExam && DURU._confettiExam();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function toonAntwoord(v, antw) {
    if (antw === null || antw === "") return "<i>(niet beantwoord)</i>";
    if (v.type === "mc") return esc(v.opties[antw]);
    if (v.type === "waaronwaar") return antw === 0 ? "Waar" : "Onwaar";
    return esc(antw);
  }
  function juisteAntwoord(v) {
    if (v.type === "mc") return esc(v.opties[v.antwoord]);
    if (v.type === "waaronwaar") return (v.antwoord === true || v.antwoord === "waar" || v.antwoord === 0) ? "Waar" : "Onwaar";
    if (v.type === "invul") return esc(String(v.antwoord).split("|")[0]);
    return esc(v.modelantwoord || "");
  }

  function reviewItem(v, i, antw, b) {
    var klas = b.status === "goed" ? "goed" : (b.status === "deels" ? "deels" : "fout");
    var ico = b.status === "goed" ? "✅" : (b.status === "deels" ? "🟡" : "❌");
    var kop = b.status === "goed" ? "Goed!" : (b.status === "deels" ? "Gedeeltelijk goed" : "Fout");
    var h = '<div class="review-item ' + klas + '" data-status="' + b.status + '">';
    h += '<div class="r-kop">' + ico + ' Vraag ' + (i + 1) + ' — ' + kop + '</div>';
    h += '<div class="r-vraag">' + v.vraag + '</div>';
    if (v.figuur) h += '<div class="vraag-figuur" style="justify-content:flex-start">' + v.figuur + '</div>';
    h += '<div class="r-rij"><span class="lbl">Jouw antwoord:</span> <span class="jouw ' + (b.status === "goed" ? "goed-tekst" : (b.status === "fout" ? "fout-tekst" : "")) + '">' + toonAntwoord(v, antw) + '</span></div>';
    if (b.status !== "goed") h += '<div class="r-rij"><span class="lbl">Goede antwoord:</span> ' + juisteAntwoord(v) + '</div>';
    if ((v.type === "open") && v.modelantwoord) h += '<div class="r-rij"><span class="lbl">Voorbeeldantwoord:</span> ' + esc(v.modelantwoord) + '</div>';
    if (v.uitleg) h += '<div class="r-uitleg">💡 <b>Zo doe je het:</b> ' + v.uitleg + '</div>';
    h += '</div>';
    return h;
  }

  DURU.reviewFilter = function (mode) {
    var items = document.querySelectorAll("#review-lijst .review-item");
    items.forEach(function (el) {
      var st = el.getAttribute("data-status");
      el.style.display = (mode === "alle" || st !== "goed") ? "" : "none";
    });
  };

  /* ---------- simpele confetti (eigen, los van engine) ---------- */
  DURU._confettiExam = function () {
    var c = document.getElementById("confetti"); if (!c) return;
    c.width = innerWidth; c.height = innerHeight;
    var ctx = c.getContext("2d");
    var kl = ["#0d9488", "#14b8a6", "#ec4899", "#f97316", "#fbbf24", "#2563eb"], p = [];
    for (var i = 0; i < 120; i++) p.push({ x: Math.random() * c.width, y: -20 - Math.random() * 300, r: 4 + Math.random() * 6, k: kl[(Math.random() * kl.length) | 0], vx: -2 + Math.random() * 4, vy: 2 + Math.random() * 4, rot: Math.random() * 6, vr: -0.2 + Math.random() * 0.4 });
    var f = 0;
    (function teken() {
      ctx.clearRect(0, 0, c.width, c.height);
      p.forEach(function (q) { q.x += q.vx; q.y += q.vy; q.vy += 0.08; q.rot += q.vr; ctx.save(); ctx.translate(q.x, q.y); ctx.rotate(q.rot); ctx.fillStyle = q.k; ctx.fillRect(-q.r / 2, -q.r / 2, q.r, q.r * 1.6); ctx.restore(); });
      if (++f < 150) requestAnimationFrame(teken); else ctx.clearRect(0, 0, c.width, c.height);
    })();
  };

  /* ---------- Bekijk eerdere pogingen (Review uit geschiedenis) ---------- */
  DURU.renderPastAttemptReview = function (attemptId) {
    var att = EX.history.find(function (h) { return h.attemptId === attemptId; });
    if (!att) return DURU.renderExamenLijst();

    var ex = DURU._examenById[att.examId];
    if (!ex) {
      alert("Fout: Toetsgegevens konden niet worden geladen.");
      return DURU.renderExamenLijst();
    }

    var c = cijfer(att.pct);
    var emoji, kop;
    if (att.pct >= 80) { emoji = "🏆"; kop = "Uitmuntend!"; }
    else if (att.pct >= 55) { emoji = "🎉"; kop = "Geslaagd!"; }
    else if (att.pct >= 40) { emoji = "💪"; kop = "Bijna! Nog even oefenen."; }
    else { emoji = "📚"; kop = "Eerst nog wat oefenen."; }

    var omtrek = 2 * Math.PI * 70, vol = omtrek * (1 - att.pct / 100);
    
    var h = '<div class="terug" onclick="DURU.renderExamenLijst()">← Terug naar toetshistorie</div>';
    h += '<div class="kaart view"><div class="resultaat">';
    h += '<div style="font-size:12px; font-weight:800; color:var(--grijs-licht); margin-bottom:8px; letter-spacing:0.5px;">RESULTAAT VAN ' + att.datum.toUpperCase() + '</div>';
    h += '<div class="emoji">' + emoji + '</div><h2>' + kop + '</h2>';
    h += '<div class="score-ring"><svg width="170" height="170">' +
      '<circle cx="85" cy="85" r="70" fill="none" stroke="#e2e8f0" stroke-width="14"/>' +
      '<circle cx="85" cy="85" r="70" fill="none" stroke="url(#g3)" stroke-width="14" stroke-linecap="round" stroke-dasharray="' + omtrek + '" stroke-dashoffset="' + vol + '" transform="rotate(-90 85 85)"/>' +
      '<defs><linearGradient id="g3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d9488"/><stop offset="1" stop-color="#14b8a6"/></linearGradient></defs>' +
      '</svg><div class="pct">' + c + '</div></div>';
    h += '<div class="samenvatting"><b>' + att.goed + ' van de ' + att.totaal + '</b> goed · ' + att.pct + '% · cijfer <b>' + c + '</b></div>';
    h += '<div class="acties">' +
      '<button class="btn groen" onclick="DURU.examenStart(\'' + ex.id + '\')">🔁 Opnieuw proberen</button>' +
      '<button class="btn ghost" onclick="DURU.renderExamenLijst()">📝 Toetshistorie</button>' +
      '</div></div></div>';

    // Review
    h += '<div class="sectie-titel" style="margin-top:30px"><h3>🔎 Nakijken — foutanalyse & uitleg</h3><div class="lijn"></div></div>';
    h += '<p style="margin:0 4px 8px;color:var(--grijs)">Bekijk bij elke vraag het goede antwoord en de uitleg. Leer van de fouten die je destijds hebt gemaakt.</p>';
    h += '<div class="filter-rij">' +
      '<button class="btn ghost klein" onclick="DURU.reviewFilter(\'alle\')">Alles</button>' +
      '<button class="btn ghost klein" onclick="DURU.reviewFilter(\'fout\')">Alleen fout/deels</button></div>';
    h += '<div id="review-lijst">';
    ex.vragen.forEach(function (v, i) {
      h += reviewItem(v, i, att.antwoorden[i], att.beoordelingen[i]);
    });
    h += '</div>';

    app().innerHTML = h;
    window.scrollTo({ top: 0, behavior: "smooth" });
  };
})();
