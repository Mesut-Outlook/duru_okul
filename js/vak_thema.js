/* =========================================================
   Duru's Schoolhub — thema voor de vak-sites (havo3/<vak>/)
   Laden in <head>, vóór de stylesheet, zodat er geen witte flits is.

   Volgt de keuze van de hub: localStorage 'duru_hub_theme'
   ('light' / 'dark'); zonder keuze het OS. Verandert de keuze in de
   hub (of een ander tabblad), dan komt er een 'storage'-event en
   schakelt deze pagina direct mee.

   Zet ook data-vak="<map>" op <html>: css/vak_dark.css geeft de
   blauwe vakken (engels, frans) daarmee hun eigen donkere tinten.
   De kleuren zelf staan in css/vak_dark.css — één bestand voor alle
   twaalf vakken, niet per vak.
   ========================================================= */
(function () {
  "use strict";
  var SLEUTEL = "duru_hub_theme";
  var root = document.documentElement;

  var m = /\/havo3\/([^\/]+)\//.exec(location.pathname);
  if (m) root.setAttribute("data-vak", m[1]);

  var mq = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;

  function keuze() {
    try { return window.localStorage.getItem(SLEUTEL); } catch (e) { return null; }
  }
  function pasToe() {
    var k = keuze();
    root.classList.toggle("dark", k ? k === "dark" : !!(mq && mq.matches));
  }

  pasToe();
  window.addEventListener("storage", function (e) {
    if (!e.key || e.key === SLEUTEL) pasToe();
  });
  if (mq && mq.addEventListener) mq.addEventListener("change", pasToe);
})();
