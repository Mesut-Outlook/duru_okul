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
      nr: 5,
      titel: "Licht",
      icoon: "🔦",
      kleur: "h5-thema",
      intro: "Licht en beeld, breking van licht, construeren bij bolle en holle lenzen, oogafwijkingen (bijziend en verziend) en rekenen aan lenzen (lenzenformule en vergroting).",
    },
    {
      nr: 6,
      titel: "Zonnestelsel en heelal",
      icoon: "🪐",
      kleur: "h6-thema",
      intro: "Ons zonnestelsel en planeten op schaal, de aarde en de maan (schijngestalten), krachten in het heelal (zwaartekracht en planeetbanen), de Melkweg en astronomisch onderzoek.",
    },
    {
      nr: 7,
      titel: "Energie en duurzaamheid",
      icoon: "🌿",
      kleur: "h7-thema",
      intro: "Energieomzettingen, verbrandingswarmte, rekenen met energie en rendement (η = Enuttig / Ein · 100%), energiegebruik in huis, milieu-impact en duurzame energiebronnen.",
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

  /* Helper voor eenduidige paragraaf/alt-bölüm herkenning */
  DURU.getParagraafInfo = function (item, isExamen) {
    if (!item) return { code: "", nr: "", label: "", tagClass: "" };
    if (!isExamen) {
      var p = item.paragraaf || "";
      return {
        code: p ? ("§" + p) : "§1.0",
        nr: p || "1.0",
        label: p ? ("Paragraaf " + p) : "Kernbegrippen",
        tagClass: p === "1.0" ? "begrippen" : "oefen"
      };
    }
    // Examens
    var t = item.titel || "";
    var m = t.match(/§\s*(\d+\.\d+)/);
    if (m) {
      return {
        code: "§" + m[1],
        nr: m[1],
        label: "Paragraaf " + m[1],
        tagClass: "toets"
      };
    }
    if (t.indexOf("Mix") !== -1 || (t.indexOf("1.1") !== -1 && t.indexOf("1.2") !== -1) ||
        item.id === "ex-h3-natuurkunde-1" || item.id === "ex-h3-natuurkunde-2" || item.id === "ex-h3-natuurkunde-3" ||
        item.id === "ex-h3-natuurkunde-4" || item.id === "ex-h3-natuurkunde-5") {
      return {
        code: "Mix §1.1–1.3",
        nr: "1.mix",
        label: "Integrale Toets (§1.1 t/m §1.3)",
        tagClass: "mix"
      };
    }
    if (t.indexOf("Eindtoets") !== -1 || item.id === "ex-h3-natuurkunde-10" || item.id === "ex-h3-natuurkunde-15" ||
        item.id === "ex-h3-natuurkunde-20" || item.id === "ex-h3-natuurkunde-25") {
      return {
        code: "Eindtoets H" + (item.hoofdstuk || ""),
        nr: "eind",
        label: "Eindtoets Hoofdstuk " + (item.hoofdstuk || ""),
        tagClass: "eind"
      };
    }
    var mapIds = {
      "ex-h3-natuurkunde-6": "2.1", "ex-h3-natuurkunde-7": "2.2", "ex-h3-natuurkunde-8": "2.3", "ex-h3-natuurkunde-9": "2.4",
      "ex-h3-natuurkunde-11": "3.1", "ex-h3-natuurkunde-12": "3.2", "ex-h3-natuurkunde-13": "3.3", "ex-h3-natuurkunde-14": "3.4",
      "ex-h3-natuurkunde-16": "4.1", "ex-h3-natuurkunde-17": "4.2", "ex-h3-natuurkunde-18": "4.3", "ex-h3-natuurkunde-19": "4.4",
      "ex-h3-natuurkunde-21": "8.1", "ex-h3-natuurkunde-22": "8.2", "ex-h3-natuurkunde-23": "8.3", "ex-h3-natuurkunde-24": "8.4",
      "ex-h3-natuurkunde-35": "1.4", "ex-h3-natuurkunde-36": "1.5"
    };
    if (mapIds[item.id]) {
      var pNr = mapIds[item.id];
      return {
        code: "§" + pNr,
        nr: pNr,
        label: "Paragraaf " + pNr,
        tagClass: "toets"
      };
    }
    return {
      code: "H" + (item.hoofdstuk || 1),
      nr: String(item.hoofdstuk || 1),
      label: "Hoofdstuk " + (item.hoofdstuk || 1),
      tagClass: "toets"
    };
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
