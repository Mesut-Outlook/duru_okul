/* =========================================================
   Duru's Wiskunde Academie — Engine
   Routing · voortgang (XP/streak/badges) · quizmotor · effecten
   ========================================================= */
(function () {
  "use strict";
  var app = document.getElementById("app");

  /* ---------------- Voortgang (localStorage) ---------------- */
  var SLEUTEL = "duru_wiskunde_v1";
  var P = laad();

  function laad() {
    try {
      var d = JSON.parse(localStorage.getItem(SLEUTEL));
      if (d) return d;
    } catch (e) {}
    return { xp: 0, streak: 0, badges: {}, beste: {}, gedaan: {} };
  }
  function bewaar() { try { localStorage.setItem(SLEUTEL, JSON.stringify(P)); } catch (e) {} }

  function updateStats() {
    document.getElementById("stat-xp").textContent = P.xp;
    document.getElementById("stat-streak").textContent = P.streak;
    document.getElementById("stat-badges").textContent = Object.keys(P.badges).length;
  }

  /* ---------------- Badges ---------------- */
  var BADGES = [
    { id: "start",    ico: "🚀", naam: "Eerste stap",         check: function () { return P.xp >= 10; } },
    { id: "vergelijk",ico: "⚖️", naam: "Vergelijkingsmeester", check: function () { return klaarHoofdstuk(8); } },
    { id: "vlam",     ico: "🔥", naam: "10 op rij",           check: function () { return (P.maxStreak || 0) >= 10; } },
    { id: "ster",     ico: "⭐", naam: "Perfecte test",        check: function () { return P.perfect; } },
    { id: "prof",     ico: "🎓", naam: "Wiskunde-professor",   check: function () { return P.xp >= 500; } },
    { id: "rekenwonder", ico: "🧮", naam: "Rekenwonder",       check: function () { return P.xp >= 200; } },
  ];
  function klaarHoofdstuk(nr) {
    var ow = DURU.onderwerpenVan(nr);
    return ow.length > 0 && ow.every(function (o) { return (P.beste[o.id] || 0) >= 70; });
  }
  function checkBadges() {
    var nieuw = [];
    BADGES.forEach(function (b) {
      if (!P.badges[b.id] && b.check()) { P.badges[b.id] = Date.now(); nieuw.push(b); }
    });
    if (nieuw.length) { bewaar(); nieuw.forEach(function (b) { toast("🏅 Nieuwe medaille: " + b.naam + "!"); }); }
    updateStats();
  }

  /* ---------------- Toast & confetti ---------------- */
  var toastTimer;
  function toast(tekst) {
    var t = document.getElementById("toast");
    t.textContent = tekst; t.classList.add("toon");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.remove("toon"); }, 2600);
  }

  function confetti() {
    var c = document.getElementById("confetti");
    c.width = innerWidth; c.height = innerHeight;
    var ctx = c.getContext("2d");
    var kleuren = ["#0d9488", "#14b8a6", "#ec4899", "#f97316", "#fbbf24", "#2563eb"];
    var deeltjes = [];
    for (var i = 0; i < 140; i++) {
      deeltjes.push({
        x: Math.random() * c.width, y: -20 - Math.random() * c.height * 0.5,
        r: 4 + Math.random() * 6, kl: kleuren[(Math.random() * kleuren.length) | 0],
        vx: -2 + Math.random() * 4, vy: 2 + Math.random() * 4, rot: Math.random() * 6,
        vr: -0.2 + Math.random() * 0.4
      });
    }
    var frames = 0;
    (function teken() {
      ctx.clearRect(0, 0, c.width, c.height);
      deeltjes.forEach(function (p) {
        p.x += p.vx; p.y += p.vy; p.vy += 0.08; p.rot += p.vr;
        ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.rot);
        ctx.fillStyle = p.kl; ctx.fillRect(-p.r / 2, -p.r / 2, p.r, p.r * 1.6); ctx.restore();
      });
      frames++;
      if (frames < 150) requestAnimationFrame(teken);
      else ctx.clearRect(0, 0, c.width, c.height);
    })();
  }

  /* ---------------- Routing ---------------- */
  DURU.gaNaar = function (route, arg) {
    if (DURU._stopExamTimer) DURU._stopExamTimer(); // examen-timer netjes stoppen
    window.scrollTo({ top: 0, behavior: "smooth" });
    if (route === "home") return renderHome();
    if (route === "theorie") return renderTheorie(arg);
    if (route === "quiz") return renderQuizStart(arg);
    if (route === "badges") return renderBadges();
    if (route === "examens") return DURU.renderExamenLijst();
    renderHome();
  };

  /* ---------------- Home ---------------- */
  function renderHome() {
    var totaalVragen = DURU.onderwerpen.reduce(function (s, o) { return s + o.vragen.length; }, 0);
    var html = "";

    html += '<section class="hero view">' +
      '<div class="mascotte">🧮</div>' +
      '<div><h2>Hoi Duru! Klaar om te rekenen? 🔢</h2>' +
      '<p>Welkom in jouw eigen Wiskunde-academie. Leer alles over <b>vergelijkingen</b>, ' +
      'oefen met ' + totaalVragen + ' vragen en verzamel medailles. Jij gaat die toets máken! 💪</p>' +
      '<div class="hero-cta">' +
      '<button class="btn teal" onclick="DURU.gaNaar(\'theorie\',\'' + (DURU.onderwerpen[0] ? DURU.onderwerpen[0].id : "") + '\')">▶️ Begin met leren</button>' +
      '<button class="btn ghost" onclick="DURU.gaNaar(\'examens\')">📝 Oefentoetsen</button>' +
      '<button class="btn ghost" onclick="DURU.gaNaar(\'badges\')">🏅 Mijn medailles</button>' +
      '</div></div></section>';

    // Oefentoetsen-sectie (op tijd, met cijfer en uitleg)
    if (DURU.examens && DURU.examens.length) {
      html += '<div class="sectie-titel"><h3>📝 Oefentoetsen — test jezelf op tijd!</h3><div class="lijn"></div></div>';
      html += '<p style="margin:0 4px 14px;color:var(--grijs)">Doe een echte proeftoets met een klok. Aan het eind krijg je je cijfer én bij elke vraag <b>hoe je het moet doen</b>.</p>';
      html += '<div class="grid cols-3">';
      DURU.examens.forEach(function (ex) {
        html += '<div class="topic-card" onclick="DURU.gaNaar(\'examens\')">' +
          '<div class="ico" style="background:var(--teal-zacht)">' + (ex.icoon || "📝") + '</div>' +
          '<h4>' + ex.titel + '</h4>' +
          '<p>' + (ex.vragen.length) + ' vragen · ⏱️ ' + (ex.duurMin || 20) + ' min</p>' +
          '<span class="tag">Proeftoets</span></div>';
      });
      html += '</div>';
    }

    DURU.hoofdstukken.forEach(function (h) {
      var ow = DURU.onderwerpenVan(h.nr);
      if (!ow.length) return;
      html += '<div class="sectie-titel"><h3>' + h.icoon + ' Hoofdstuk ' + h.nr + ' — ' + h.titel + '</h3><div class="lijn"></div></div>';
      html += '<p style="margin:0 4px 14px;color:var(--grijs)">' + h.intro + '</p>';
      html += '<div class="grid cols-3">';
      ow.forEach(function (o, i) {
        var beste = P.beste[o.id] || 0;
        html += '<div class="topic-card ' + h.kleur + '" onclick="DURU.gaNaar(\'theorie\',\'' + o.id + '\')">' +
          '<span class="badge-num">' + (o.paragraaf || (h.nr + "." + (i + 1))) + '</span>' +
          '<div class="ico">' + (o.icoon || h.icoon) + '</div>' +
          '<h4>' + o.titel + '</h4>' +
          '<p>' + (o.korteUitleg || "") + '</p>' +
          '<span class="tag">' + o.vragen.length + ' vragen</span>' +
          '<div class="mini-progress"><span style="width:' + beste + '%"></span></div>' +
          (beste ? '<small style="color:var(--groen);font-weight:800">Beste score: ' + beste + '%</small>' : '<small style="color:var(--grijs-licht)">Nog niet gedaan</small>') +
          '</div>';
      });
      html += '</div>';
    });

    html += '<div class="footer">Gemaakt met 🔢 en 💙 voor Duru · Wiskunde MAVO 2</div>';
    app.innerHTML = html;
    updateStats();
  }

  /* ---------------- Theorie ---------------- */
  function renderTheorie(id) {
    var o = DURU.getOnderwerp(id);
    if (!o) return renderHome();
    var html = '<div class="terug" onclick="DURU.gaNaar(\'home\')">← Terug naar overzicht</div>';
    html += '<div class="kaart view"><div class="theorie">';
    html += '<h2>' + (o.paragraaf ? o.paragraaf + " " : "") + o.titel + '</h2>';
    html += (o.theorie || "<p>(Nog geen theorie.)</p>");
    html += '</div></div>';
    html += '<div style="margin-top:22px;text-align:center">' +
      '<button class="btn teal" onclick="DURU.gaNaar(\'quiz\',\'' + o.id + '\')">✅ Start de oefentoets (' + o.vragen.length + ' vragen)</button>' +
      '</div>';
    // navigatie volgende/vorige
    var idx = DURU.onderwerpen.indexOf(o);
    html += '<div class="quiz-acties" style="margin-top:18px">';
    if (idx > 0) html += '<button class="btn ghost klein" onclick="DURU.gaNaar(\'theorie\',\'' + DURU.onderwerpen[idx - 1].id + '\')">← ' + DURU.onderwerpen[idx - 1].titel + '</button>'; else html += '<span></span>';
    if (idx < DURU.onderwerpen.length - 1) html += '<button class="btn ghost klein" onclick="DURU.gaNaar(\'theorie\',\'' + DURU.onderwerpen[idx + 1].id + '\')">' + DURU.onderwerpen[idx + 1].titel + ' →</button>';
    html += '</div>';
    app.innerHTML = html;
  }

  /* ---------------- Quiz ---------------- */
  var Q = null; // huidige quiz-state

  function renderQuizStart(id) {
    var o = DURU.getOnderwerp(id);
    if (!o || !o.vragen.length) return renderTheorie(id);
    var vragen = shuffle(o.vragen.slice());
    Q = { onderwerp: o, vragen: vragen, i: 0, goed: 0, beantwoord: false };
    renderVraag();
  }

  function renderVraag() {
    var v = Q.vragen[Q.i];
    var totaal = Q.vragen.length;
    var pct = Math.round((Q.i / totaal) * 100);
    var niveau = v.niveau || 1;

    var html = '<div class="terug" onclick="DURU.bevestigStop()">← Stoppen</div>';
    html += '<div class="kaart view"><div class="quiz-wrap">';
    html += '<div class="quiz-head"><div class="voortgang"><div class="bar"><span style="width:' + pct + '%"></span></div></div>' +
      '<div class="teller">Vraag ' + (Q.i + 1) + ' / ' + totaal + '</div></div>';

    html += '<div class="vraag-kaart">';
    html += '<span class="vraag-niveau niveau-' + niveau + '">' + ["", "Makkelijk", "Gemiddeld", "Uitdaging ★"][niveau] + '</span>';
    html += '<div class="vraag-tekst">' + v.vraag + '</div>';
    if (v.figuur) html += '<div class="vraag-figuur">' + v.figuur + '</div>';

    if (v.type === "invoer") {
      html += '<div class="invoer-rij">' +
        '<input id="antw-invoer" type="text" inputmode="decimal" autocomplete="off" placeholder="..." onkeydown="if(event.key===\'Enter\')DURU.checkInvoer()">' +
        (v.eenheid ? '<span class="eenheid">' + v.eenheid + '</span>' : '') +
        '<button class="btn klein" onclick="DURU.checkInvoer()">Controleer</button></div>';
    } else {
      // mc of waar/onwaar
      var opties = v.type === "waaronwaar" ? ["Waar", "Onwaar"] : v.opties;
      html += '<div class="opties">';
      opties.forEach(function (opt, idx) {
        var letter = v.type === "waaronwaar" ? (idx === 0 ? "✔" : "✗") : String.fromCharCode(65 + idx);
        html += '<button class="optie" data-idx="' + idx + '" onclick="DURU.kiesOptie(' + idx + ')">' +
          '<span class="letter">' + letter + '</span><span>' + opt + '</span></button>';
      });
      html += '</div>';
    }

    if (v.hint) html += '<div class="hint-tekst" id="hint">💡 ' + v.hint + '</div>';

    html += '<div class="feedback" id="feedback"></div>';

    html += '<div class="quiz-acties">';
    html += v.hint ? '<button class="btn ghost klein" onclick="document.getElementById(\'hint\').classList.add(\'toon\')">💡 Hint</button>' : '<span></span>';
    html += '<button class="btn klein" id="volgende-btn" style="display:none" onclick="DURU.volgende()">Volgende →</button>';
    html += '</div>';

    html += '</div></div></div>';
    app.innerHTML = html;
    Q.beantwoord = false;
    var inp = document.getElementById("antw-invoer");
    if (inp) inp.focus();
  }

  function normaliseer(s) {
    return String(s).toLowerCase().trim()
      .replace(",", ".").replace(/\s+/g, "")
      .replace("km/u", "km/h");
  }

  DURU.checkInvoer = function () {
    if (Q.beantwoord) return;
    var v = Q.vragen[Q.i];
    var inp = document.getElementById("antw-invoer");
    var ruw = inp.value;
    if (ruw.trim() === "") { inp.focus(); return; }
    var goed = false;
    var getalAntw = parseFloat(normaliseer(ruw));
    var verwacht = parseFloat(normaliseer(v.antwoord));
    if (!isNaN(getalAntw) && !isNaN(verwacht)) {
      var tol = v.tolerantie != null ? v.tolerantie : Math.max(Math.abs(verwacht) * 0.02, 0.01);
      goed = Math.abs(getalAntw - verwacht) <= tol;
    } else {
      // tekstvergelijking (eventueel meerdere goede antwoorden via |)
      var opties = String(v.antwoord).split("|").map(normaliseer);
      goed = opties.indexOf(normaliseer(ruw)) !== -1;
    }
    inp.disabled = true;
    verwerk(goed, v);
  };

  DURU.kiesOptie = function (idx) {
    if (Q.beantwoord) return;
    var v = Q.vragen[Q.i];
    var juist = v.type === "waaronwaar"
      ? (idx === 0) === (v.antwoord === true || v.antwoord === "waar" || v.antwoord === 0)
      : idx === v.antwoord;
    var knoppen = app.querySelectorAll(".optie");
    var goedIdx = v.type === "waaronwaar" ? (v.antwoord === true || v.antwoord === "waar" || v.antwoord === 0 ? 0 : 1) : v.antwoord;
    knoppen.forEach(function (k, i) {
      k.classList.add("uit");
      if (i === goedIdx) k.classList.add("goed");
      if (i === idx && !juist) k.classList.add("fout");
    });
    verwerk(juist, v);
  };

  function verwerk(goed, v) {
    Q.beantwoord = true;
    var fb = document.getElementById("feedback");
    if (goed) {
      Q.goed++;
      P.streak++; P.maxStreak = Math.max(P.maxStreak || 0, P.streak);
      var punten = 10 + (v.niveau || 1) * 5 + (P.streak >= 3 ? 5 : 0);
      P.xp += punten;
      fb.className = "feedback goed toon";
      fb.innerHTML = '<div class="fb-kop">🎉 Goed gedaan, Duru! +' + punten + ' XP</div>' +
        (v.uitleg ? '<div class="uitleg">' + v.uitleg + '</div>' : '');
      if (P.streak > 0 && P.streak % 5 === 0) toast("🔥 " + P.streak + " op rij! Topper!");
    } else {
      P.streak = 0;
      fb.className = "feedback fout toon";
      var juistTekst = "";
      if (v.type === "invoer") juistTekst = "Het juiste antwoord is <b>" + v.antwoord + (v.eenheid ? " " + v.eenheid : "") + "</b>.";
      else if (v.type === "waaronwaar") juistTekst = "Het juiste antwoord is <b>" + ((v.antwoord === true || v.antwoord === "waar" || v.antwoord === 0) ? "Waar" : "Onwaar") + "</b>.";
      else juistTekst = "Het juiste antwoord is <b>" + String.fromCharCode(65 + v.antwoord) + ": " + v.opties[v.antwoord] + "</b>.";
      fb.innerHTML = '<div class="fb-kop">💪 Bijna! Niet erg, zo leer je het.</div>' +
        '<div class="uitleg">' + juistTekst + (v.uitleg ? "<br>" + v.uitleg : "") + '</div>';
    }
    bewaar(); updateStats();
    var vb = document.getElementById("volgende-btn");
    vb.style.display = "inline-flex";
    vb.textContent = Q.i === Q.vragen.length - 1 ? "Bekijk resultaat 🏁" : "Volgende →";
    vb.focus();
  }

  DURU.volgende = function () {
    Q.i++;
    if (Q.i >= Q.vragen.length) return renderResultaat();
    renderVraag();
  };

  DURU.bevestigStop = function () {
    if (Q.i === 0 && !Q.beantwoord) return DURU.gaNaar("theorie", Q.onderwerp.id);
    if (confirm("Wil je echt stoppen? Je voortgang in deze toets gaat verloren.")) DURU.gaNaar("theorie", Q.onderwerp.id);
  };

  /* ---------------- Resultaat ---------------- */
  function renderResultaat() {
    var o = Q.onderwerp;
    var totaal = Q.vragen.length;
    var pct = Math.round((Q.goed / totaal) * 100);
    if (pct >= (P.beste[o.id] || 0)) P.beste[o.id] = pct;
    if (pct === 100) P.perfect = true;
    bewaar();

    var emoji, kop, msg;
    if (pct === 100) { emoji = "🏆"; kop = "PERFECT, Duru!"; msg = "Alles goed! Je bent er helemaal klaar voor!"; }
    else if (pct >= 80) { emoji = "🌟"; kop = "Super gedaan!"; msg = "Bijna alles goed. Nog even die laatste puntjes!"; }
    else if (pct >= 60) { emoji = "👍"; kop = "Goed bezig!"; msg = "Je bent op de goede weg. Oefen nog een keer en je wordt nog beter."; }
    else { emoji = "💪"; kop = "Blijven oefenen!"; msg = "Lees de theorie nog eens rustig door en probeer het opnieuw. Jij kan dit!"; }

    var omtrek = 2 * Math.PI * 70;
    var vol = omtrek * (1 - pct / 100);

    var html = '<div class="kaart view"><div class="resultaat">';
    html += '<div class="emoji">' + emoji + '</div>';
    html += '<h2>' + kop + '</h2>';
    html += '<div class="score-ring"><svg width="170" height="170">' +
      '<circle cx="85" cy="85" r="70" fill="none" stroke="#e2e8f0" stroke-width="14"/>' +
      '<circle cx="85" cy="85" r="70" fill="none" stroke="url(#g)" stroke-width="14" stroke-linecap="round" ' +
      'stroke-dasharray="' + omtrek + '" stroke-dashoffset="' + vol + '" transform="rotate(-90 85 85)"/>' +
      '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d9488"/><stop offset="1" stop-color="#06b6d4"/></linearGradient></defs>' +
      '</svg><div class="pct">' + pct + '%</div></div>';
    html += '<div class="samenvatting">Je had <b>' + Q.goed + ' van de ' + totaal + '</b> vragen goed.<br>' + msg + '</div>';
    html += '<div class="acties">' +
      '<button class="btn teal" onclick="DURU.gaNaar(\'quiz\',\'' + o.id + '\')">🔁 Opnieuw oefenen</button>' +
      '<button class="btn ghost" onclick="DURU.gaNaar(\'theorie\',\'' + o.id + '\')">📖 Lees theorie</button>' +
      '<button class="btn oranje" onclick="DURU.gaNaar(\'home\')">🏠 Naar overzicht</button>' +
      '</div></div></div>';
    app.innerHTML = html;
    if (pct >= 80) confetti();
    checkBadges();
  }

  /* ---------------- Badges-pagina ---------------- */
  function renderBadges() {
    var html = '<div class="terug" onclick="DURU.gaNaar(\'home\')">← Terug naar overzicht</div>';
    html += '<div class="kaart view"><div class="theorie">';
    html += '<h2>🏅 Mijn medailles</h2><p>Verzamel ze allemaal door goed te oefenen!</p>';
    html += '<div class="badge-rij">';
    BADGES.forEach(function (b) {
      html += '<div class="badge ' + (P.badges[b.id] ? "behaald" : "") + '">' +
        '<div class="b-ico">' + b.ico + '</div><div class="b-naam">' + b.naam + '</div></div>';
    });
    html += '</div>';
    html += '<h3>📊 Jouw voortgang</h3><table class="nask"><tr><th>Onderwerp</th><th>Beste score</th></tr>';
    DURU.onderwerpen.forEach(function (o) {
      var b = P.beste[o.id] || 0;
      html += '<tr><td style="text-align:left">' + (o.paragraaf || "") + ' ' + o.titel + '</td><td>' + (b ? b + "%" : "—") + '</td></tr>';
    });
    html += '</table>';
    html += '<p style="margin-top:20px"><button class="btn ghost klein" onclick="DURU.reset()">🗑️ Voortgang wissen</button></p>';
    html += '</div></div>';
    app.innerHTML = html;
  }

  DURU.reset = function () {
    if (confirm("Weet je zeker dat je alle voortgang wilt wissen?")) {
      P = { xp: 0, streak: 0, badges: {}, beste: {}, gedaan: {} };
      bewaar(); updateStats(); DURU.gaNaar("home");
    }
  };

  /* ---------------- Util ---------------- */
  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = (Math.random() * (i + 1)) | 0; var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* ---------------- Start ---------------- */
  document.addEventListener("DOMContentLoaded", function () {
    updateStats();
    renderHome();
  });
  // val-back als DOM al klaar is
  if (document.readyState !== "loading") { updateStats(); renderHome(); }
})();
