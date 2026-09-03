#!/usr/bin/env node
/* =========================================================
   tools/build_hoofdstukken.js
   Bouwt js/hoofdstukken.js — de EEN-BRON-VAN-WAARHEID voor hoofdstuk-
   (unit-)info per HAVO 3 vak. Leest per vak js/bootstrap.js + js/data/*.js
   in een node vm-sandbox (geen DOM/localStorage nodig) en verzamelt:
     - DURU.hoofdstukken (nr, titel, icoon, intro)
     - welk hoofdstuk elke geregistreerde examen/onderwerp bij hoort

   Gebruik:
     node tools/build_hoofdstukken.js          → schrijft js/hoofdstukken.js
     node tools/build_hoofdstukken.js --check  → schrijft NIET, exit 1 als
                                                  js/hoofdstukken.js verouderd is

   Zie ook: docs/ENGINE_SPEC.md (register/registerExamen contract).
   ========================================================= */
"use strict";

var fs = require("fs");
var path = require("path");
var vm = require("vm");

var ROOT = path.resolve(__dirname, "..");
var HAVO3_DIR = path.join(ROOT, "havo3");
var OUT_FILE = path.join(ROOT, "js", "hoofdstukken.js");

var VAKKEN = [
  "aardrijkskunde",
  "biologie",
  "duits",
  "economie",
  "engels",
  "frans",
  "geschiedenis",
  "maatschappijleer",
  "natuurkunde",
  "nederlands",
  "scheikunde",
  "wiskunde"
];

var CHECK_MODE = process.argv.indexOf("--check") !== -1;

/* ---------- Helpers ---------- */

// "Menselijke" sortering van bestandsnamen: examen_2 vóór examen_10.
function naturalCompare(a, b) {
  var re = /(\d+)|(\D+)/g;
  var pa = a.match(re) || [];
  var pb = b.match(re) || [];
  var len = Math.max(pa.length, pb.length);
  for (var i = 0; i < len; i++) {
    var xa = pa[i], xb = pb[i];
    if (xa === undefined) return -1;
    if (xb === undefined) return 1;
    var na = /^\d+$/.test(xa), nb = /^\d+$/.test(xb);
    if (na && nb) {
      var diff = parseInt(xa, 10) - parseInt(xb, 10);
      if (diff !== 0) return diff;
    } else if (xa !== xb) {
      return xa < xb ? -1 : 1;
    }
  }
  return 0;
}

function todayISO() {
  var d = new Date();
  var mm = ("0" + (d.getMonth() + 1)).slice(-2);
  var dd = ("0" + d.getDate()).slice(-2);
  return d.getFullYear() + "-" + mm + "-" + dd;
}

/* ---------- Per-vak sandbox opbouw ---------- */

function buildVak(vak, warnings) {
  var vakJsDir = path.join(HAVO3_DIR, vak, "js");
  var bootstrapPath = path.join(vakJsDir, "bootstrap.js");
  var dataDir = path.join(vakJsDir, "data");

  if (!fs.existsSync(bootstrapPath)) {
    warnings.push(vak + ": bootstrap.js ontbreekt — vak overgeslagen");
    return null;
  }

  // window === globalThis van de sandbox, net als in een echte browser,
  // zodat "window.DURU = window.DURU || {}" gevolgd door de bare
  // identifier "DURU.hoofdstukken = ..." allebei naar hetzelfde object wijzen.
  var sandbox = {};
  sandbox.window = sandbox;
  sandbox.console = console;
  var ctx = vm.createContext(sandbox);

  try {
    vm.runInContext(fs.readFileSync(bootstrapPath, "utf8"), ctx, { filename: bootstrapPath });
  } catch (e) {
    warnings.push(vak + "/js/bootstrap.js: " + e.message);
    return null;
  }

  sandbox.DURU = sandbox.DURU || {};
  sandbox.DURU.hoofdstukken = sandbox.DURU.hoofdstukken || [];
  sandbox.DURU.onderwerpen = sandbox.DURU.onderwerpen || [];
  sandbox.DURU.examens = sandbox.DURU.examens || [];
  sandbox.DURU._examenById = sandbox.DURU._examenById || {};

  // DURU.registerExamen wordt normaal gedefinieerd in exams.js — dat bestand
  // leunt op DOM/localStorage en wordt hier bewust NIET geladen. We geven
  // een minimale, contract-conforme stub (zie docs/ENGINE_SPEC.md) zodat
  // data-bestanden die registerExamen aanroepen toch zonder DOM draaien.
  if (typeof sandbox.DURU.registerExamen !== "function") {
    sandbox.DURU.registerExamen = function (ex) {
      if (!ex || !ex.id) return;
      ex.vragen = ex.vragen || [];
      sandbox.DURU.examens.push(ex);
      sandbox.DURU._examenById[ex.id] = ex;
    };
  }

  var dataFiles = [];
  if (fs.existsSync(dataDir)) {
    dataFiles = fs.readdirSync(dataDir)
      .filter(function (f) { return /\.js$/.test(f); })
      .sort(naturalCompare);
  }

  dataFiles.forEach(function (f) {
    var fp = path.join(dataDir, f);
    try {
      vm.runInContext(fs.readFileSync(fp, "utf8"), ctx, { filename: fp });
    } catch (e) {
      warnings.push(vak + "/js/data/" + f + ": " + e.message);
    }
  });

  var hoofdstukken = sandbox.DURU.hoofdstukken.map(function (h) {
    return { nr: h.nr, titel: h.titel, icoon: h.icoon, intro: h.intro };
  });

  var hoofdstukNrs = {};
  hoofdstukken.forEach(function (h) { hoofdstukNrs[String(h.nr)] = true; });

  var examenHoofdstuk = {};
  var aantalExamens = {};
  var examenZonderHoofdstuk = 0;
  sandbox.DURU.examens.forEach(function (ex) {
    if (!ex || !ex.id) return;
    if (ex.hoofdstuk === undefined || ex.hoofdstuk === null) {
      examenZonderHoofdstuk++;
      return;
    }
    examenHoofdstuk[ex.id] = ex.hoofdstuk;
    var k = String(ex.hoofdstuk);
    aantalExamens[k] = (aantalExamens[k] || 0) + 1;
    if (!hoofdstukNrs[k]) {
      warnings.push(vak + ": examen '" + ex.id + "' verwijst naar onbekend hoofdstuk " + ex.hoofdstuk + " (niet in DURU.hoofdstukken)");
    }
  });

  var onderwerpHoofdstuk = {};
  var aantalOnderwerpen = {};
  var onderwerpZonderHoofdstuk = 0;
  sandbox.DURU.onderwerpen.forEach(function (o) {
    if (!o || !o.id) return;
    if (o.hoofdstuk === undefined || o.hoofdstuk === null) {
      onderwerpZonderHoofdstuk++;
      return;
    }
    onderwerpHoofdstuk[o.id] = o.hoofdstuk;
    var k = String(o.hoofdstuk);
    aantalOnderwerpen[k] = (aantalOnderwerpen[k] || 0) + 1;
    if (!hoofdstukNrs[k]) {
      warnings.push(vak + ": onderwerp '" + o.id + "' verwijst naar onbekend hoofdstuk " + o.hoofdstuk + " (niet in DURU.hoofdstukken)");
    }
  });

  if (examenZonderHoofdstuk > 0) {
    warnings.push(vak + ": " + examenZonderHoofdstuk + " examen(s) zonder hoofdstuk-veld (niet meegenomen in manifest)");
  }
  if (onderwerpZonderHoofdstuk > 0) {
    warnings.push(vak + ": " + onderwerpZonderHoofdstuk + " onderwerp(en) zonder hoofdstuk-veld (niet meegenomen in manifest)");
  }

  return {
    hoofdstukken: hoofdstukken,
    examenHoofdstuk: examenHoofdstuk,
    onderwerpHoofdstuk: onderwerpHoofdstuk,
    aantalExamens: aantalExamens,
    aantalOnderwerpen: aantalOnderwerpen
  };
}

/* ---------- Main ---------- */

function main() {
  var warnings = [];
  var vakken = {};

  VAKKEN.forEach(function (vak) {
    var result = buildVak(vak, warnings);
    if (result) vakken[vak] = result;
  });

  var manifest = {
    gegenereerd: todayISO(),
    jaar: "2026-2027",
    vakken: vakken
  };

  var output = "/* AUTO-GEGENEREERD door tools/build_hoofdstukken.js — NIET handmatig bewerken. */\n"
    + "window.DURU_HOOFDSTUKKEN = " + JSON.stringify(manifest, null, 2) + ";\n";

  if (warnings.length > 0) {
    console.warn("Waarschuwingen (" + warnings.length + "):");
    warnings.forEach(function (w) { console.warn("  - " + w); });
  } else {
    console.warn("Geen waarschuwingen.");
  }

  // Korte samenvatting per vak, altijd getoond (check + normale run).
  console.warn("\nSamenvatting per vak:");
  Object.keys(vakken).forEach(function (vak) {
    var v = vakken[vak];
    var nrs = v.hoofdstukken.map(function (h) { return h.nr; }).join(",");
    console.warn("  " + vak + ": hoofdstukken=[" + nrs + "] aantalExamens=" + JSON.stringify(v.aantalExamens) + " aantalOnderwerpen=" + JSON.stringify(v.aantalOnderwerpen));
  });

  if (CHECK_MODE) {
    var existing = fs.existsSync(OUT_FILE) ? fs.readFileSync(OUT_FILE, "utf8") : null;
    var normalize = function (s) {
      return s == null ? null : s.replace(/"gegenereerd":\s*"[\d-]+"/, '"gegenereerd": "DATE"');
    };
    if (normalize(existing) !== normalize(output)) {
      console.error("\njs/hoofdstukken.js is VEROUDERD ten opzichte van de brondata. Draai `node tools/build_hoofdstukken.js` (zonder --check) om te regenereren.");
      process.exit(1);
    }
    console.warn("\njs/hoofdstukken.js is up-to-date.");
    process.exit(0);
  } else {
    fs.writeFileSync(OUT_FILE, output, "utf8");
    console.warn("\nGeschreven: " + path.relative(ROOT, OUT_FILE));
  }
}

main();
