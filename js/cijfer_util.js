/* =========================================================
   Duru's Schoolhub — Cijfer Utility (DURU_CIJFER)
   Enkele, gedeelde bron voor het Nederlandse cijfer (1,0 – 10,0)
   en de slaaggrens. Gebruikt door js/dashboard.js en
   js/ouder_dashboard.js — geen eigen formule meer per paneel.

   Vóór 2026-09-04 stonden `1 + pct/100*9` en `>= 5.5` op ~20
   losse plekken: in kleurkeuzes, badge-klassen, adviesteksten,
   filters en de grafiek-as. Eén schoolregel die verandert,
   betekende ze allemaal terugvinden.

   Kleur hoort NIET hier: elk paneel heeft zijn eigen tokens
   (--ouder-goed vs --groen). Gedeeld is de indeling (klasse),
   niet de opmaak.
   ========================================================= */

(function () {
  "use strict";

  // Slaaggrens en schaal — de enige plek waar deze getallen staan.
  var DREMPEL = 5.5;   // geslaagd vanaf
  var GOED    = 7.0;   // "goed" vanaf
  var TOP     = 8.5;   // "uitstekend" vanaf — examenklaar
  var MIN     = 1.0;
  var MAX     = 10.0;

  /* Percentage → cijfer. cijfer = 1 + pct/100 * 9, op 1 decimaal. */
  function vanPct(pct) {
    var p = Number(pct);
    if (!isFinite(p)) p = 0;
    return Math.round((MIN + (p / 100) * (MAX - MIN)) * 10) / 10;
  }

  /* Goed/totaal → cijfer. */
  function van(goed, totaal) {
    var t = Number(totaal);
    if (!isFinite(t) || t <= 0) return MIN;
    return vanPct((Number(goed) || 0) / t * 100);
  }

  function geslaagd(cijfer) {
    return Number(cijfer) >= DREMPEL;
  }

  /* Indeling voor badges/pillen. `aantal` = 0 betekent: nog geen data. */
  function klasse(cijfer, aantal) {
    if (aantal !== undefined && !aantal) return "none";
    var c = Number(cijfer);
    if (c >= GOED) return "goed";
    if (c >= DREMPEL) return "net";
    return "zwak";
  }

  function examenklaar(cijfer) {
    return Number(cijfer) >= TOP;
  }

  /* Weergave met komma als decimaalteken (docs/DOC_STANDARD.md). */
  function tekst(cijfer, aantal) {
    if (aantal !== undefined && !aantal) return "—";
    var c = Number(cijfer);
    if (!isFinite(c)) return "—";
    return c.toFixed(1).replace(".", ",");
  }

  /* Positie op de 1–10 schaal, in procenten. Voor de cijferschaal
     in het ouder-paneel en de grafiek-as in het leerling-paneel. */
  function positie(cijfer) {
    var c = Number(cijfer);
    if (!isFinite(c)) c = MIN;
    return Math.max(0, Math.min(100, ((c - MIN) / (MAX - MIN)) * 100));
  }

  /* Gemiddelde van een lijst pogingen (of getallen). 0 bij leeg. */
  function gemiddelde(lijst, veld) {
    if (!lijst || !lijst.length) return 0;
    var som = 0, n = 0;
    for (var i = 0; i < lijst.length; i++) {
      var w = veld ? lijst[i][veld] : lijst[i];
      w = Number(w);
      if (isFinite(w)) { som += w; n++; }
    }
    return n ? som / n : 0;
  }

  window.DURU_CIJFER = {
    DREMPEL: DREMPEL,
    GOED: GOED,
    TOP: TOP,
    MIN: MIN,
    MAX: MAX,
    van: van,
    vanPct: vanPct,
    geslaagd: geslaagd,
    klasse: klasse,
    examenklaar: examenklaar,
    tekst: tekst,
    positie: positie,
    gemiddelde: gemiddelde
  };
})();
