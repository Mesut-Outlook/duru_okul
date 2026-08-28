/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Hoofdstukken overzicht
  DURU.hoofdstukken = [
    {
      nr: 1,
      titel: "Kracht en beweging",
      icoon: "🏎️",
      kleur: "h1-thema",
      intro: "Krachten, soorten bewegingen, (v,t)- en (s,t)-diagrammen, de tweede wet van Newton (Fres = m·a), verkeersveiligheid en arbeid (W = F·s).",
    },
    {
      nr: 2,
      titel: "Elektriciteit",
      icoon: "⚡",
      kleur: "h2-thema",
      intro: "Lading, spanning, stroomsterkte, wet van Ohm (R = U/I), serie- en parallelschakelingen, vermogen (P = U·I), kWh-energie en elektromagnetisme.",
    },
    {
      nr: 3,
      titel: "Straling",
      icoon: "☢️",
      kleur: "h3-thema",
      intro: "Elektromagnetisch spectrum (IR, UV, röntgen), atoombouw, kernstraling (alfa, bèta, gamma), halveringstijd, medische toepassingen en kernenergie.",
    },
    {
      nr: 4,
      titel: "Stoffen en materialen",
      icoon: "🧱",
      kleur: "h4-thema",
      intro: "Stofeigenschappen, dichtheid (ρ = m/V), drijven en zinken, soortelijke warmte (Q = m·c·ΔT), warmtetransport (geleiding, stroming, straling), soortelijke weerstand (R = ρ·l/A) en sensoren (NTC, PTC, LDR).",
    },
    {
      nr: 8,
      titel: "Krachten gebruiken",
      icoon: "🪚",
      kleur: "h8-thema",
      intro: "Hefbomen, draaipunt en arm, moment van een kracht (M = F·r), de hefboomwet in evenwicht, overbrengingen (vaste en losse katrollen, takels, tandwielen), druk (p = F/A) en hydraulische vloeistofdruk (Wet van Pascal).",
    }
  ];

  DURU.onderwerpen = [];
  DURU._byId = {};

  DURU.register = function (onderwerp) {
    if (!onderwerp || !onderwerp.id) {
      console.warn("DURU.register: onderwerp zonder id genegeerd", onderwerp);
      return;
    }
    onderwerp.vragen = onderwerp.vragen || [];
    DURU.onderwerpen.push(onderwerp);
    DURU._byId[onderwerp.id] = onderwerp;
  };

  DURU.getOnderwerp = function (id) { return DURU._byId[id]; };
  DURU.onderwerpenVan = function (nr) {
    return DURU.onderwerpen.filter(function (o) { return o.hoofdstuk === nr; });
  };
})();

// Storage delegation to parent window
if (window.parent && window.parent !== window && window.parent.localStorage) {
  Storage.prototype.getItem = function(key) {
    return window.parent.localStorage.getItem(key);
  };
  Storage.prototype.setItem = function(key, value) {
    window.parent.localStorage.setItem(key, value);
  };
  Storage.prototype.removeItem = function(key) {
    window.parent.localStorage.removeItem(key);
  };
}
