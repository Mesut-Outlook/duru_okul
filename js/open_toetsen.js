/* =========================================================
   Duru's Schoolhub — "Open toetsen" in de toetslijst van elk vak
   Eén bestand voor alle 12 HAVO 3-vaksites (geen 12 kopieën).
   Wordt NA js/exams.js geladen en wikkelt DURU.renderExamenLijst:
   na het tekenen van de lijst komen er
     - filterknoppen  Alle · Nog niet gemaakt · Onvoldoende · Gemaakt
       (keuze bewaard in localStorage "ot_filter_v1", bewust zonder
       duru_-voorvoegsel zodat het niet naar de cloud gesynct wordt);
     - per hoofdstuk een balk "x van y gemaakt · z nog open" met
       "▶ Volgende open toets" (start de eerste niet-gemaakte toets);
     - een status-klasse op elke kaart (ot-open / ot-zwak / ot-goed).
   Werkt op de gerenderde DOM: elke engine tekent .examen-card met
   onclick="DURU.examenStart('<id>')", de groepering verschilt per vak
   (details.chapter-accordion, .hf-accordion-card, of geen).
   Status komt uit dezelfde sleutel als de engine: duru_2627_<map>_examens_v1.
   Leest alleen, schrijft geen resultaten.
   ========================================================= */
(function () {
  "use strict";
  if (!window.DURU || typeof DURU.renderExamenLijst !== "function") return;

  var map = document.documentElement.getAttribute("data-vak") ||
    ((location.pathname.match(/havo3\/([^\/]+)/) || [])[1]);
  if (!map) return;
  var SLEUTEL = "duru_2627_" + map + "_examens_v1";
  var FILTER_SLEUTEL = "ot_filter_v1";
  var FILTERS = [
    ["alle", "Alle"],
    ["open", "Nog niet gemaakt"],
    ["zwak", "Onvoldoende"],
    ["gemaakt", "Gemaakt"]
  ];

  function lees(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function schrijf(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  // pct van de beste poging, of null als de toets nooit gemaakt is
  function besteScores() {
    var d = null;
    try { d = JSON.parse(lees(SLEUTEL)); } catch (e) {}
    d = d || {};
    var beste = {};
    Object.keys(d.beste || {}).forEach(function (id) { beste[id] = d.beste[id]; });
    (d.history || []).forEach(function (a) {
      if (a && a.examId && (beste[a.examId] == null || a.pct > beste[a.examId])) beste[a.examId] = a.pct;
    });
    return beste;
  }
  // cijfer = 1 + pct/100*9 → onvoldoende (< 5,5) ⇔ pct < 50
  function status(pct) { return pct == null ? "open" : (pct < 50 ? "zwak" : "goed"); }
  function past(st, f) {
    return f === "alle" || (f === "open" && st === "open") || (f === "zwak" && st === "zwak") ||
      (f === "gemaakt" && st !== "open");
  }

  function stijl() {
    if (document.getElementById("ot-stijl")) return;
    var s = document.createElement("style");
    s.id = "ot-stijl";
    s.textContent =
      ".ot-filters{display:flex;flex-wrap:wrap;gap:8px;margin:0 4px 16px}" +
      ".ot-chip{font:inherit;font-weight:700;font-size:15px;cursor:pointer;display:inline-flex;align-items:center;gap:8px;" +
        "padding:6px 14px;border-radius:99px;border:2px solid var(--lijn);background:var(--kaart);color:var(--inkt)}" +
      ".ot-chip b{font-variant-numeric:tabular-nums;font-size:13px;padding:0 8px;border-radius:99px;background:var(--lijn)}" +
      ".ot-chip[aria-pressed=true]{background:var(--paars);border-color:var(--paars);color:#fff}" +
      ".ot-chip.ot-open[aria-pressed=true]{background:var(--oranje);border-color:var(--oranje)}" +
      ".ot-chip[aria-pressed=true] b{background:rgba(255,255,255,.25)}" +
      ".ot-chip:focus-visible,.ot-volgende:focus-visible{outline:3px solid var(--oranje);outline-offset:2px}" +
      ".ot-balk{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin:4px 0 14px;padding:10px 14px;" +
        "border-radius:14px;background:var(--kaart);border:1px solid var(--lijn)}" +
      ".ot-voortgang{flex:1 1 220px;min-width:0;display:grid;gap:6px}" +
      ".ot-tel{font-size:14px;color:var(--grijs);font-variant-numeric:tabular-nums}" +
      ".ot-tel strong{color:var(--oranje)}" +
      ".ot-staaf{height:8px;border-radius:99px;background:var(--lijn);overflow:hidden}" +
      ".ot-staaf span{display:block;height:100%;border-radius:99px;background:var(--groen)}" +
      ".ot-volgende{font:inherit;font-weight:800;font-size:15px;cursor:pointer;border:0;border-radius:12px;" +
        "padding:9px 14px;background:var(--oranje);color:#fff;white-space:nowrap}" +
      ".ot-volgende[disabled]{cursor:default;background:var(--groen-zacht);color:var(--groen)}" +
      ".examen-card.ot-open{border:2px solid var(--oranje);box-shadow:inset 4px 0 0 var(--oranje)}" +
      ".examen-card.ot-goed{opacity:.75}" +
      ".examen-card.ot-goed:hover{opacity:1}" +
      ".ot-weg{display:none!important}" +
      ".ot-leeg{margin:4px 4px 14px;color:var(--grijs);font-size:15px}";
    document.head.appendChild(s);
  }

  // De groep (hoofdstuk) waar een kaart bij hoort; zonder hoofdstuk-container de lijst zelf.
  function groepVan(kaart) {
    return kaart.closest("details.chapter-accordion, .hf-accordion-card") || kaart.parentElement;
  }
  // Waar de balk komt: bovenaan de inhoud van de groep.
  function zetBalk(groep, el) {
    if (groep.matches("details")) {
      var sum = groep.querySelector(":scope > summary");
      sum.insertAdjacentElement("afterend", el);
    } else if (groep.classList.contains("hf-accordion-card")) {
      var body = groep.querySelector(".hf-body") || groep;
      body.insertBefore(el, body.firstChild);
    } else {
      groep.insertAdjacentElement("beforebegin", el);
    }
  }

  function verrijk() {
    var kaarten = [].slice.call(document.querySelectorAll(".examen-card[onclick*='examenStart']"));
    if (!kaarten.length) return;
    stijl();
    var beste = besteScores();
    var groepen = [];
    kaarten.forEach(function (k) {
      var m = (k.getAttribute("onclick") || "").match(/examenStart\('([^']+)'\)/);
      if (!m) return;
      k.otId = m[1];
      k.otStatus = status(beste[m[1]]);
      k.classList.remove("ot-open", "ot-zwak", "ot-goed");
      k.classList.add("ot-" + k.otStatus);
      var g = groepVan(k);
      if (groepen.indexOf(g) < 0) { groepen.push(g); g.otKaarten = []; }
      g.otKaarten.push(k);
    });

    var filter = lees(FILTER_SLEUTEL) || "open";
    if (!FILTERS.some(function (f) { return f[0] === filter; })) filter = "open";

    // Filterknoppen boven de eerste groep
    var balk = document.createElement("div");
    balk.className = "ot-filters";
    balk.setAttribute("role", "group");
    balk.setAttribute("aria-label", "Toetsen filteren");
    balk.innerHTML = FILTERS.map(function (f) {
      var n = kaarten.filter(function (k) { return past(k.otStatus, f[0]); }).length;
      return '<button type="button" class="ot-chip' + (f[0] === "open" ? " ot-open" : "") + '" data-ot="' + f[0] +
        '" aria-pressed="' + (f[0] === filter) + '">' + f[1] + " <b>" + n + "</b></button>";
    }).join("");
    groepen[0].insertAdjacentElement("beforebegin", balk);

    // Per groep: voortgang + volgende open toets + lege-melding
    groepen.forEach(function (g) {
      var tot = g.otKaarten.length;
      var open = g.otKaarten.filter(function (k) { return k.otStatus === "open"; });
      var gemaakt = tot - open.length;
      var el = document.createElement("div");
      el.className = "ot-balk";
      el.innerHTML =
        '<div class="ot-voortgang"><div class="ot-tel">' + gemaakt + " van " + tot + " gemaakt · " +
          (open.length ? "<strong>" + open.length + " nog open</strong>" : "alles gemaakt 🎉") + "</div>" +
          '<div class="ot-staaf" aria-hidden="true"><span style="width:' + Math.round(gemaakt / tot * 100) + '%"></span></div></div>' +
        (open.length
          ? '<button type="button" class="ot-volgende" data-ot-start="' + open[0].otId + '">▶ Volgende open toets</button>'
          : '<button type="button" class="ot-volgende" disabled>✓ Klaar</button>');
      zetBalk(g, el);
      var leeg = document.createElement("div");
      leeg.className = "ot-leeg ot-weg";
      el.insertAdjacentElement("afterend", leeg);
      g.otLeeg = leeg;
    });

    function pasToe() {
      kaarten.forEach(function (k) { k.classList.toggle("ot-weg", !past(k.otStatus, filter)); });
      // Lijsten/paragraafblokken zonder zichtbare kaart verbergen
      var lijsten = [];
      kaarten.forEach(function (k) { if (lijsten.indexOf(k.parentElement) < 0) lijsten.push(k.parentElement); });
      lijsten.forEach(function (l) {
        var zicht = l.querySelector(".examen-card:not(.ot-weg)");
        var g = groepVan(l.querySelector(".examen-card"));
        var blok = (l.parentElement && l.parentElement !== g && !l.parentElement.matches(".hf-body, .chapter-content") &&
          g.contains(l.parentElement)) ? l.parentElement : l;
        blok.classList.toggle("ot-weg", !zicht);
      });
      groepen.forEach(function (g) {
        var zicht = g.otKaarten.some(function (k) { return !k.classList.contains("ot-weg"); });
        g.otLeeg.textContent = filter === "open" ? "Alle toetsen van dit hoofdstuk zijn gemaakt. Goed bezig! 🎉"
          : "Geen toetsen in deze selectie.";
        g.otLeeg.classList.toggle("ot-weg", zicht);
      });
      [].forEach.call(balk.querySelectorAll("[data-ot]"), function (b) {
        b.setAttribute("aria-pressed", String(b.getAttribute("data-ot") === filter));
      });
    }
    balk.addEventListener("click", function (e) {
      var b = e.target.closest("[data-ot]");
      if (!b) return;
      filter = b.getAttribute("data-ot");
      schrijf(FILTER_SLEUTEL, filter);
      pasToe();
    });
    groepen.forEach(function (g) {
      var knop = g.otLeeg.previousElementSibling.querySelector("[data-ot-start]");
      if (knop) knop.addEventListener("click", function (e) {
        e.stopPropagation();
        DURU.examenStart(knop.getAttribute("data-ot-start"));
      });
    });
    pasToe();
  }

  var origineel = DURU.renderExamenLijst;
  DURU.renderExamenLijst = function () {
    var r = origineel.apply(this, arguments);
    try { verrijk(); } catch (e) { if (window.console) console.warn("open_toetsen:", e); }
    return r;
  };
})();
