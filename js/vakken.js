/* =========================================================
   Duru's Schoolhub — Vakregister (DURU_VAKKEN)
   Enkele bron voor "welke vakken bestaan er, in welk jaar, met
   welke storage-sleutels". Gebruikt door js/dashboard.js,
   js/ouder_dashboard.js en (voor de HAVO 3-kaarten) js/landing.js.

   Vóór 2026-09-04 stond deze lijst drie keer in de codebase:
   VAKKEN (landing), VAK_REGISTER (dashboard) en VAK_CONFIG (ouder).
   De laatste twee waren woord voor woord identiek. CLAUDE.md
   waarschuwde "vergeet er geen" — die waarschuwing wás het probleem.

   ⚠️ Sleutels zijn BEVROREN. Ze zijn de ingang tot Duru's opgeslagen
   resultaten; hernoemen betekent dat haar geschiedenis verdwijnt.
   2025-2026 (MAVO 2) heeft geen jaarcode in de sleutel — dat is
   historisch en blijft zo. Nieuwe jaren: duru_<jaarcode>_<slug>_v1.
   Zie docs/ENGINE_SPEC.md en CLAUDE.md → "Ders ekleme".
   ========================================================= */

(function () {
  "use strict";

  var VAKKEN = [
    // ── 2025-2026 · MAVO 2 (gearchiveerd, sleutels bevroren) ──
    { jaar: '2025-2026', id: 'natuurkunde',           titel: 'Natuurkunde (NASK)',    icoon: '⚛️', kleur: 'blauw',
      practiceKey: 'duru_nask_v1',                examKey: 'duru_nask_examens_v1' },
    { jaar: '2025-2026', id: 'wiskunde',              titel: 'Wiskunde',              icoon: '⚖️', kleur: 'teal',
      practiceKey: 'duru_wiskunde_v1',            examKey: 'duru_wiskunde_examens_v1' },
    { jaar: '2025-2026', id: 'economie',              titel: 'Economie',              icoon: '💶', kleur: 'groen',
      practiceKey: 'duru_economi_v1',             examKey: 'duru_economi_examens_v1' },
    { jaar: '2025-2026', id: 'geschiedenis',          titel: 'Geschiedenis',          icoon: '🕰️', kleur: 'oranje',
      practiceKey: 'duru_geschiedenis_v1',        examKey: 'duru_geschiedenis_examens_v1' },
    { jaar: '2025-2026', id: 'nederlands-spelling',   titel: 'Spelling & Grammatica', icoon: '✍️', kleur: 'oranje',
      practiceKey: 'duru_nederlands_spelling_v1', examKey: 'duru_nederlands_spelling_examens_v1' },
    { jaar: '2025-2026', id: 'nederlands-begrijpend', titel: 'Begrijpend Lezen',      icoon: '🧠', kleur: 'oranje',
      practiceKey: null,                          examKey: 'begrijpend_lezen_history', special: 'begrijpend' },

    // ── 2026-2027 · HAVO 3 (actief) ──
    // domein/beschrijving/href zijn er voor de landingskaarten; de panelen
    // negeren ze. Zo blijft het één rij per vak in plaats van twee lijsten.
    { jaar: '2026-2027', id: 'nederlands',      titel: 'Nederlands',      icoon: '📖', kleur: 'oranje',
      practiceKey: 'duru_2627_nederlands_v1',      examKey: 'duru_2627_nederlands_examens_v1',
      domein: 'talen', beschrijving: 'Lezen, schrijven & taal' },
    { jaar: '2026-2027', id: 'engels',          titel: 'Engels',          icoon: '🇬🇧', kleur: 'oranje',
      practiceKey: 'duru_2627_engels_v1',          examKey: 'duru_2627_engels_examens_v1',
      domein: 'talen', beschrijving: 'Reading, grammar & words' },
    { jaar: '2026-2027', id: 'frans',           titel: 'Frans',           icoon: '🇫🇷', kleur: 'oranje',
      practiceKey: 'duru_2627_frans_v1',           examKey: 'duru_2627_frans_examens_v1',
      domein: 'talen', beschrijving: 'Grammaire & vocabulaire' },
    { jaar: '2026-2027', id: 'duits',           titel: 'Duits',           icoon: '🇩🇪', kleur: 'oranje',
      practiceKey: 'duru_2627_duits_v1',           examKey: 'duru_2627_duits_examens_v1',
      domein: 'talen', beschrijving: 'Wörter, Fälle & grammatica' },
    { jaar: '2026-2027', id: 'wiskunde',        titel: 'Wiskunde',        icoon: '⚖️', kleur: 'teal',
      practiceKey: 'duru_2627_wiskunde_v1',        examKey: 'duru_2627_wiskunde_examens_v1',
      domein: 'exact', beschrijving: 'Algebra, meetkunde & meer' },
    { jaar: '2026-2027', id: 'natuurkunde',     titel: 'Natuurkunde',     icoon: '⚛️', kleur: 'blauw',
      practiceKey: 'duru_2627_natuurkunde_v1',     examKey: 'duru_2627_natuurkunde_examens_v1',
      domein: 'exact', beschrijving: 'Krachten, energie & meer' },
    { jaar: '2026-2027', id: 'scheikunde',      titel: 'Scheikunde',      icoon: '🧪', kleur: 'teal',
      practiceKey: 'duru_2627_scheikunde_v1',      examKey: 'duru_2627_scheikunde_examens_v1',
      domein: 'exact', beschrijving: 'Stoffen, atomen & reacties' },
    { jaar: '2026-2027', id: 'biologie',        titel: 'Biologie',        icoon: '🧬', kleur: 'groen',
      practiceKey: 'duru_2627_biologie_v1',        examKey: 'duru_2627_biologie_examens_v1',
      domein: 'exact', beschrijving: 'Groei, puberteit & voortplanting' },
    { jaar: '2026-2027', id: 'geschiedenis',    titel: 'Geschiedenis',    icoon: '🕰️', kleur: 'oranje',
      practiceKey: 'duru_2627_geschiedenis_v1',    examKey: 'duru_2627_geschiedenis_examens_v1',
      domein: 'mens',  beschrijving: 'Tijd, bronnen & gebeurtenissen' },
    { jaar: '2026-2027', id: 'aardrijkskunde',  titel: 'Aardrijkskunde',  icoon: '🗺️', kleur: 'teal',
      practiceKey: 'duru_2627_aardrijkskunde_v1',  examKey: 'duru_2627_aardrijkskunde_examens_v1',
      domein: 'mens',  beschrijving: 'Aarde, klimaat & mensen' },
    // 💶 en niet 🏛️: economie en maatschappijleer deelden vóór de samenvoeging
    // hetzelfde icoon in de panelen, terwijl de landingspagina ze al uit elkaar
    // hield. Het onderscheidende icoon wint.
    { jaar: '2026-2027', id: 'economie',        titel: 'Economie',        icoon: '💶', kleur: 'groen',
      practiceKey: 'duru_2627_economie_v1',        examKey: 'duru_2627_economie_examens_v1',
      domein: 'mens',  beschrijving: 'Geld, markt & keuzes' },
    { jaar: '2026-2027', id: 'maatschappijleer', titel: 'Maatschappijleer', icoon: '🏛️', kleur: 'blauw',
      practiceKey: 'duru_2627_maatschappijleer_v1', examKey: 'duru_2627_maatschappijleer_examens_v1',
      domein: 'mens',  beschrijving: 'Samenleven & rechten' }
  ];

  function vanJaar(jaar) {
    return VAKKEN.filter(function (v) { return v.jaar === jaar; });
  }

  function zoek(jaar, id) {
    for (var i = 0; i < VAKKEN.length; i++) {
      if (VAKKEN[i].jaar === jaar && VAKKEN[i].id === id) return VAKKEN[i];
    }
    return null;
  }

  /* De HAVO 3-vakken in de vorm die js/landing.js voor zijn kaarten gebruikt:
     id met 'h3-'-prefix, href naar de vaksite en sleutel zonder '_v1'. */
  function landingKaarten() {
    return vanJaar('2026-2027').map(function (v) {
      return {
        id: 'h3-' + v.id,
        titel: v.titel,
        icoon: v.icoon,
        domein: v.domein,
        beschrijving: v.beschrijving,
        href: './havo3/' + v.id + '/',
        sleutel: String(v.practiceKey || '').replace(/_v1$/, '')
      };
    });
  }

  window.DURU_VAKKEN = {
    alle: VAKKEN,
    vanJaar: vanJaar,
    zoek: zoek,
    landingKaarten: landingKaarten
  };
})();
