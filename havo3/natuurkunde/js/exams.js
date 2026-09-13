/* =========================================================
   Duru's Natuurkunde Academie — Oefentoetsen (Examen-modus)
   Apart van de oefenquiz. Gebruikt een EIGEN opslag-sleutel,
   dus de XP/medailles/scores van de gewone oefeningen blijven
   altijd onaangeroerd.
   ========================================================= */
(function () {
  "use strict";

  function hoofdstukTitelVan(nr) {
    if (nr == null) return "";
    var lijst = (window.DURU && DURU.hoofdstukken) || [];
    for (var i = 0; i < lijst.length; i++) {
      if (lijst[i].nr === nr) return lijst[i].titel;
    }
    return "Hoofdstuk " + nr;
  }

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
  var EX_SLEUTEL = "duru_2627_natuurkunde_examens_v1";
  function laadEx() {
    var d = null;
    try { d = JSON.parse(localStorage.getItem(EX_SLEUTEL)); } catch (e) {}
    if (!d || typeof d !== "object") d = {};
    d.beste   = d.beste   || {};
    d.laatste = d.laatste || {};
    d.history = d.history || [];
    // Herstel 'beste' en 'laatste' uit de history (history is leidend, nieuwste vooraan)
    // zodat de resultaten op de kaarten nooit verloren gaan.
    for (var i = 0; i < d.history.length; i++) {
      var a = d.history[i];
      if (!a || !a.examId || a.pct == null) continue;
      if (d.beste[a.examId] == null || a.pct > d.beste[a.examId]) d.beste[a.examId] = a.pct;
      if (d.laatste[a.examId] == null) d.laatste[a.examId] = a.pct; // eerste = nieuwste poging
    }
    return d;
  }
  function bewaarEx() { try { localStorage.setItem(EX_SLEUTEL, JSON.stringify(EX)); } catch (e) {} }
  var EX = laadEx();

  var app = function () { return document.getElementById("app"); };
  function esc(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  /* ---------- Timer (wordt netjes gestopt bij verlaten) ---------- */
  var T = null; // examen-state
  DURU._stopExamTimer = function () { if (T && T.interval) { clearInterval(T.interval); T.interval = null; } };

  /* ---------- Helper voor examen card HTML ---------- */
  function bouwExamenCard(ex) {
    var best = EX.beste[ex.id];
    var laatste = (EX.laatste && EX.laatste[ex.id] !== undefined) ? EX.laatste[ex.id] : null;
    if (laatste == null && EX.history) {
      var attempts = EX.history.filter(function (a) { return a.examId === ex.id; });
      if (attempts.length > 0) {
        laatste = attempts[0].pct;
      }
    }

    var pInfo = DURU.getParagraafInfo ? DURU.getParagraafInfo(ex, true) : { code: "§1." + (ex.hoofdstuk || 1), tagClass: "toets" };

    var statusHtml = '';
    if (best != null) {
      statusHtml += '<div style="margin-top: 10px; display: flex; flex-direction: column; gap: 4px;">' +
        '<div style="font-size: 11px; font-weight: 800; display: inline-flex; align-items: center; gap: 4px; color: var(--groen); background: var(--groen-zacht); padding: 2px 8px; border-radius: 99px; width: fit-content;">' +
          '<span>✓</span> Gemaakt' +
        '</div>' +
        '<div class="ex-best" style="color:' + (best >= 55 ? 'var(--groen)' : 'var(--oranje)') + '; font-size: 13px;">🏆 Beste cijfer: ' + cijfer(best) + ' (' + best + '%)</div>';
      if (laatste != null) {
        statusHtml += '<div class="ex-laatste" style="color:' + (laatste >= 55 ? 'var(--groen)' : 'var(--oranje)') + '; font-size: 13px; font-weight: 800;">⏱️ Laatste cijfer: ' + cijfer(laatste) + ' (' + laatste + '%)</div>';
      }
      statusHtml += '</div>';
    } else {
      statusHtml += '<div style="margin-top: 10px; display: flex; flex-direction: column; gap: 4px;">' +
        '<div style="font-size: 11px; font-weight: 800; display: inline-flex; align-items: center; gap: 4px; color: var(--grijs); background: var(--lijn); padding: 2px 8px; border-radius: 99px; width: fit-content;">' +
          'Nog niet gemaakt' +
        '</div>' +
        '<div class="ex-best" style="color:var(--grijs-licht); font-size: 13px;">🏆 Beste: -</div>' +
      '</div>';
    }

    return '<div class="examen-card" onclick="DURU.examenStart(\'' + ex.id + '\')">' +
      '<div class="card-type-row">' +
        '<span class="card-type-label toets">📝 Proeftoets</span>' +
        '<span class="paragraaf-tag ' + (pInfo.tagClass || "") + '">' + pInfo.code + '</span>' +
      '</div>' +
      '<div class="ex-ico" style="margin-top:6px;">' + (ex.icoon || "📝") + '</div>' +
      '<h4>' + esc(ex.titel) + '</h4>' +
      '<div class="ex-meta">' + esc(ex.vak || "") + '<br><b>' + ex.vragen.length + ' vragen</b> · ⏱️ ' + (ex.duurMin || 20) + ' min</div>' +
      statusHtml +
      '<div style="margin-top:14px"><span class="btn klein">▶️ Start toets</span></div>' +
    '</div>';
  }

  function bouwExamenParagraafSecties(hfNr, exLijst) {
    var out = "";
    if (hfNr === 1) {
      var sectiesH1 = [
        {
          titel: "Paragraaf 1.1 — Kracht bij beweging",
          ico: "🏎️",
          tag: "§1.1",
          sleutel: "1.1"
        },
        {
          titel: "Paragraaf 1.2 — Soorten beweging & Diagrammen",
          ico: "📈",
          tag: "§1.2",
          sleutel: "1.2"
        },
        {
          titel: "Paragraaf 1.3 — Kracht en Versnelling (F = m · a)",
          ico: "🚀",
          tag: "§1.3",
          sleutel: "1.3"
        },
        {
          titel: "Paragraaf 1.4 — Veiligheid, Remweg & Stopafstand",
          ico: "🛑",
          tag: "§1.4",
          sleutel: "1.4"
        },
        {
          titel: "Paragraaf 1.5 — Arbeid en Energieomzetting",
          ico: "🚴",
          tag: "§1.5",
          sleutel: "1.5"
        },
        {
          titel: "Integrale Toetstraining — Mix Paragrafen 1.1 t/m 1.3",
          ico: "🎯",
          tag: "Mix §1.1–1.3",
          sleutel: "1.mix"
        },
        {
          titel: "Hoofdstuk 1 — Integrale Eindtoets",
          ico: "🏆",
          tag: "Eindtoets H1",
          sleutel: "eind"
        }
      ];
      // groepering uit het paragraaf-veld van de toets (DURU.getParagraafInfo), niet uit id-lijsten
      var sleutelVan = function (e) { return DURU.getParagraafInfo(e, true).nr; };

      sectiesH1.forEach(function (s) {
        var matched = exLijst.filter(function (e) { return sleutelVan(e) === s.sleutel; });
        if (matched.length === 0) return;
        out += '<div class="paragraaf-groep">' +
          '<div class="paragraaf-groep-header">' +
            '<div class="paragraaf-groep-titel"><span>' + s.ico + '</span> ' + s.titel + '</div>' +
            '<div class="paragraaf-groep-meta">' +
              '<span class="paragraaf-tag ' + (s.tag.indexOf('Mix') !== -1 ? 'mix' : '') + '">' + s.tag + '</span>' +
              '<span class="hf-badge paars">📝 ' + matched.length + ' toetsen</span>' +
            '</div>' +
          '</div>' +
          '<div class="examen-lijst">';
        matched.forEach(function (ex) {
          out += bouwExamenCard(ex);
        });
        out += '</div></div>';
      });

      var handledIds = {};
      sectiesH1.forEach(function(s){ handledIds[s.sleutel] = true; });
      var rest = exLijst.filter(function(e){ return !handledIds[sleutelVan(e)]; });
      if (rest.length > 0) {
        out += '<div class="paragraaf-groep">' +
          '<div class="paragraaf-groep-header">' +
            '<div class="paragraaf-groep-titel"><span>📚</span> Overige Oefentoetsen H1</div>' +
            '<div class="paragraaf-groep-meta">' +
              '<span class="hf-badge paars">📝 ' + rest.length + ' toetsen</span>' +
            '</div>' +
          '</div>' +
          '<div class="examen-lijst">';
        rest.forEach(function (ex) {
          out += bouwExamenCard(ex);
        });
        out += '</div></div>';
      }
    } else {
      var paraEx = [];
      var eindEx = [];
      exLijst.forEach(function (ex) {
        var p = DURU.getParagraafInfo(ex, true);
        if (p.tagClass === "eind" || (ex.titel && ex.titel.indexOf("Eindtoets") !== -1)) {
          eindEx.push(ex);
        } else {
          paraEx.push(ex);
        }
      });

      if (paraEx.length > 0) {
        out += '<div class="paragraaf-groep">' +
          '<div class="paragraaf-groep-header">' +
            '<div class="paragraaf-groep-titel"><span>📌</span> Deeltoetsen per Paragraaf (H' + hfNr + ')</div>' +
            '<div class="paragraaf-groep-meta">' +
              '<span class="paragraaf-tag">§' + hfNr + '.x</span>' +
              '<span class="hf-badge paars">📝 ' + paraEx.length + ' toetsen</span>' +
            '</div>' +
          '</div>' +
          '<div class="examen-lijst">';
        paraEx.forEach(function (ex) {
          out += bouwExamenCard(ex);
        });
        out += '</div></div>';
      }

      if (eindEx.length > 0) {
        out += '<div class="paragraaf-groep">' +
          '<div class="paragraaf-groep-header">' +
            '<div class="paragraaf-groep-titel"><span>🎯</span> Hoofdstuk Eindtoets (Integrale Herhaling)</div>' +
            '<div class="paragraaf-groep-meta">' +
              '<span class="paragraaf-tag eind">Eindtoets H' + hfNr + '</span>' +
              '<span class="hf-badge paars">📝 ' + eindEx.length + ' toets</span>' +
            '</div>' +
          '</div>' +
          '<div class="examen-lijst">';
        eindEx.forEach(function (ex) {
          out += bouwExamenCard(ex);
        });
        out += '</div></div>';
      }
    }
    return out;
  }

  /* ---------- Lijst met oefentoetsen ---------- */
  DURU.renderExamenLijst = function () {
    DURU._stopExamTimer();
    var h = '<div class="terug" onclick="DURU.gaNaar(\'home\')">← Terug naar overzicht</div>';
    h += '<div class="sectie-titel"><h3>📝 Oefentoetsen per Hoofdstuk &amp; Paragraaf</h3><div class="lijn"></div></div>';
    h += '<p style="margin:0 4px 16px;color:var(--grijs)">Doe een toets op tijd, net als op school! Kies hieronder een Hoofdstuk of filter direct op een specifieke paragraaf.</p>';

    // Groepeer op hoofdstuk
    var groepen = {};
    DURU.examens.forEach(function (ex) {
      var hfNr = ex.hoofdstuk || 1;
      var hfObj = null;
      (DURU.hoofdstukken || []).forEach(function(hh) { if (hh.nr === hfNr) hfObj = hh; });
      var hfKey = hfObj ? ("Hoofdstuk " + hfObj.nr + " — " + hfObj.titel) : ("Hoofdstuk " + hfNr);
      if (!groepen[hfNr]) groepen[hfNr] = { obj: hfObj, nr: hfNr, titel: hfKey, lijst: [] };
      groepen[hfNr].lijst.push(ex);
    });

    var hfNummers = Object.keys(groepen).map(Number).sort(function(a,b){ return a-b; });

    // Filter & Navigatie balk
    h += '<div class="hf-filter-wrap">';
    h +=   '<div class="hf-filter-title">⚡ Snel filteren &amp; navigeren per hoofdstuk:</div>';
    h +=   '<div class="hf-filter-pills">';
    h +=     '<button class="hf-filter-pill actief" id="hf-ex-pill-all" onclick="DURU.filterHoofdstukEx(0)">🌟 Alle Hoofdstukken (' + DURU.examens.length + ' toetsen)</button>';
    hfNummers.forEach(function(hfNr) {
      var g = groepen[hfNr];
      h +=   '<button class="hf-filter-pill" id="hf-ex-pill-' + hfNr + '" onclick="DURU.filterHoofdstukEx(' + hfNr + ')">' +
               ((g.obj && g.obj.icoon) || "⚛️") + ' H' + hfNr + ' (' + g.lijst.length + ')' +
             '</button>';
    });
    h +=   '</div>';
    h +=   '<div class="hf-acties-row">';
    h +=     '<button class="hf-actie-knop" onclick="DURU.toggleAlleHoofdstukkenEx(true)">📖 Klap alles uit</button>';
    h +=     '<button class="hf-actie-knop" onclick="DURU.toggleAlleHoofdstukkenEx(false)">🔒 Klap alles in</button>';
    h +=   '</div>';
    h += '</div>';

    hfNummers.forEach(function (hfNr) {
      var g = groepen[hfNr];
      var exLijst = g.lijst;
      var isOpen = (hfNr === 1);

      h += '<div class="hf-accordion-card ' + (isOpen ? 'open' : '') + '" id="hf-ex-card-' + hfNr + '" data-hf-nr="' + hfNr + '">' +
        '<div class="hf-header" onclick="DURU.toggleHoofdstukEx(' + hfNr + ')">' +
          '<div class="hf-ico">' + ((g.obj && g.obj.icoon) || "⚛️") + '</div>' +
          '<div class="hf-info">' +
            '<h3>' + esc(g.titel) + '</h3>' +
            '<div class="hf-meta-badges">' +
              '<span class="hf-badge groen">📝 ' + exLijst.length + ' Proeftoetsen (' + (exLijst.reduce(function(s, e){ return s + e.vragen.length; }, 0)) + ' vragen)</span>' +
            '</div>' +
          '</div>' +
          '<button class="hf-toggle-btn" id="hf-ex-label-' + hfNr + '">' + (isOpen ? '▲ Klap in' : '▼ Open Toetsen') + '</button>' +
        '</div>' +
        '<div class="hf-body" id="hf-ex-content-' + hfNr + '" style="display:' + (isOpen ? 'block' : 'none') + ';">';

      // Bouw geordende paragrafen/sub-secties
      h += bouwExamenParagraafSecties(hfNr, exLijst);

      h += '</div></div>'; // Einde hf-body en hf-accordion-card
    });

    DURU.toggleHoofdstukEx = function(hfNr) {
      var card = document.getElementById("hf-ex-card-" + hfNr);
      var content = document.getElementById("hf-ex-content-" + hfNr);
      var label = document.getElementById("hf-ex-label-" + hfNr);
      if (!content) return;
      var isHidden = content.style.display === "none";
      content.style.display = isHidden ? "block" : "none";
      if (card) {
        if (isHidden) card.classList.add("open");
        else card.classList.remove("open");
      }
      if (label) label.textContent = isHidden ? "▲ Klap in" : "▼ Open Toetsen";
    };

    DURU.filterHoofdstukEx = function(hfNr) {
      document.querySelectorAll('.hf-filter-pill').forEach(function(pill) {
        pill.classList.remove('actief');
      });
      var activePill = document.getElementById(hfNr === 0 ? 'hf-ex-pill-all' : ('hf-ex-pill-' + hfNr));
      if (activePill) activePill.classList.add('actief');

      document.querySelectorAll('[id^="hf-ex-card-"]').forEach(function(card) {
        var cardNr = parseInt(card.getAttribute('data-hf-nr'), 10);
        if (hfNr === 0 || cardNr === hfNr) {
          card.style.display = 'block';
          if (hfNr !== 0) {
            card.classList.add('open');
            var content = card.querySelector('.hf-body');
            if (content) content.style.display = 'block';
            var btn = card.querySelector('.hf-toggle-btn');
            if (btn) btn.textContent = '▲ Klap in';
            card.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        } else {
          card.style.display = 'none';
        }
      });
    };

    DURU.toggleAlleHoofdstukkenEx = function(open) {
      document.querySelectorAll('[id^="hf-ex-card-"]').forEach(function(card) {
        var content = card.querySelector('.hf-body');
        var btn = card.querySelector('.hf-toggle-btn');
        if (open) {
          card.classList.add('open');
          if (content) content.style.display = 'block';
          if (btn) btn.textContent = '▲ Klap in';
        } else {
          card.classList.remove('open');
          if (content) content.style.display = 'none';
          if (btn) btn.textContent = '▼ Open Toetsen';
        }
      });
    };

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
  // mc-opties per poging schudden: in de data staat het goede antwoord vaak op een voorspelbare plek
  // (spread.py zette het op 0,1,2,3,0,1,…). Antwoorden en beoordelingen blijven in de ORIGINELE index
  // opgeslagen, dus oude pogingen, nakijken en review veranderen niet. Opties die naar elkaar of naar
  // een plek verwijzen ("geen van beide", "alle bovenstaande") blijven in de vaste volgorde.
  var VASTE_VOLGORDE = /geen van|beide|bovenstaande|alle (?:antwoorden|opties)|all of the above|none of the above|toutes les r|keine der|alle Antworten/i;
  function optieVolgorde(v) {
    if (v.type !== "mc" || !v.opties) return null;
    var orde = v.opties.map(function (_, i) { return i; });
    if (v.opties.some(function (o) { return VASTE_VOLGORDE.test(String(o)); })) return orde;
    for (var i = orde.length - 1; i > 0; i--) {
      var j = (Math.random() * (i + 1)) | 0, t = orde[i]; orde[i] = orde[j]; orde[j] = t;
    }
    return orde;
  }

  DURU.examenStart = function (id) {
    var ex = DURU._examenById[id];
    if (!ex) return DURU.renderExamenLijst();
    DURU._stopExamTimer();
    T = {
      ex: ex,
      i: 0,
      antwoorden: new Array(ex.vragen.length).fill(null),
      volgorde: ex.vragen.map(optieVolgorde),
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
      var orde = (v.type === "mc" && T.volgorde && T.volgorde[T.i]) || opties.map(function (_, i) { return i; });
      h += '<div class="opties">';
      orde.forEach(function (idx, pos) {
        var opt = opties[idx];
        var letter = v.type === "waaronwaar" ? (idx === 0 ? "✔" : "✗") : String.fromCharCode(65 + pos);
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
    else h += '<button class="btn groen klein" onclick="DURU.examenInleveren()">✅ Inleveren</button>';
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
      .replace(/[.,;:!?'"()·\u2018\u2019\u201c\u201d\u02bc`\u00b4]/g, " ")
      .replace(/\s+/g, " ").trim();
  }
  // invul nakijken (ENGINE_SPEC): getal-antwoorden numeriek, tekst-antwoorden zoals voorheen.
  // Zonder dit telde "12" of "0,2" goed bij antwoord "2" (indexOf op tekst).
  function leesGetal(s) {
    var m = String(s == null ? "" : s).replace(/−/g, "-").match(/-?\d+(?:[.,]\d+)*/);
    if (!m) return null;
    var g = m[0], dec = 0;
    if (/^-?\d{1,3}(\.\d{3})+$/.test(g)) g = g.replace(/\./g, "");            // 16.000 = zestienduizend
    else if (g.indexOf(",") !== -1) g = g.replace(/\./g, "").replace(",", "."); // 1,5 / 1.234,5
    if (g.indexOf(".") !== -1) dec = g.length - g.indexOf(".") - 1;
    return { waarde: parseFloat(g), decimalen: dec };
  }
  // "15", "15 m/s", "2,0 m/s²", "3 m/s2", "18h", "9%" — een getal met hooguit een eenheid erachter
  function isGetalAntwoord(a) {
    return /^\s*[-−]?\d+(?:[.,]\d+)*\s*(?:[a-zA-Zµμ°%€\/²³^().·Ω ]*[a-zA-Z\/^]\d)?[a-zA-Zµμ°%€\/²³^().·Ω ]*$/.test(a);
  }
  function invulGoed(antw, v) {
    var inv = normaliseer(antw);
    if (inv === "") return false;
    var getal = leesGetal(antw);
    var tekstAlts = [];
    var goed = String(v.antwoord).split("|").some(function (a) {
      if (isGetalAntwoord(a)) {
        var verwacht = leesGetal(a);
        if (!getal || !verwacht) return false;
        // tolerantie: expliciet, anders een halve eenheid van de laatste gegeven decimaal (12,5 -> 0,05; 1914 -> 0,5)
        var tol = v.tolerantie != null ? v.tolerantie : 0.5 * Math.pow(10, -verwacht.decimalen) + 1e-9;
        return Math.abs(getal.waarde - verwacht.waarde) <= tol;
      }
      tekstAlts.push(normaliseer(a));
      return false;
    });
    return goed || tekstAlts.some(function (a) { return a && (inv === a || inv.indexOf(a) !== -1); });
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
      var ok = invulGoed(antw, v);
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
      hoofdstuk: (ex.hoofdstuk != null ? ex.hoofdstuk : null),
      hoofdstukTitel: hoofdstukTitelVan(ex.hoofdstuk),
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
      '<circle cx="85" cy="85" r="70" fill="none" stroke="var(--paars)" stroke-width="14" stroke-linecap="round" stroke-dasharray="' + omtrek + '" stroke-dashoffset="' + vol + '" transform="rotate(-90 85 85)"/>' +
      '</svg><div class="pct">' + c + '</div></div>';
    h += '<div class="samenvatting"><b>' + goed + ' van de ' + n + '</b> goed · ' + pct + '% · cijfer <b>' + c + '</b></div>';
    h += '<div class="acties">' +
      '<button class="btn groen" onclick="DURU.examenStart(\'' + ex.id + '\')">🔁 Opnieuw maken</button>' +
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
    var kl = ["#6d28d9", "#ec4899", "#f97316", "#fbbf24", "#16a34a", "#2563eb"], p = [];
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
      '<circle cx="85" cy="85" r="70" fill="none" stroke="var(--paars)" stroke-width="14" stroke-linecap="round" stroke-dasharray="' + omtrek + '" stroke-dashoffset="' + vol + '" transform="rotate(-90 85 85)"/>' +
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
