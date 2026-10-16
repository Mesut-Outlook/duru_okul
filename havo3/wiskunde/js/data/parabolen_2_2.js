/* =========================================================
   Duru's Wiskunde (HAVO 3) — Onderwerp §2.2 Symmetrie en top
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.register({
  "id": "h2-parabolen-2",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Symmetrie en top",
  "korteUitleg": "Bereken de coördinaten van de top met het snijpunt met de y-as en de symmetrie, of met de snijpunten met de x-as.",
  "icoon": "⛰️",
  "kleur": "blauw",
  "theorie": "<h3>§2.2 Symmetrie en top</h3>\n<p>De <b>top</b> van een parabool ligt op de <b>symmetrieas</b>, de verticale lijn door de top. Twee punten van de parabool met dezelfde y-coördinaat liggen even ver links en rechts van de symmetrieas. Daarom ligt de top precies <b>midden</b> tussen twee van zulke punten.</p>\n<h4>Aanpak: coördinaten van de top berekenen</h4>\n<ol><li>Bereken de y-coördinaat van het snijpunt met de y-as (vul x = 0 in: dat geeft c).</li><li>Er is een ander punt met dezelfde y-coördinaat. Stel de vergelijking op en los hem op.</li><li>De x-coördinaat van de top ligt midden tussen de twee oplossingen.</li><li>Vul de x-coördinaat van de top in de formule in: dat geeft de y-coördinaat.</li><li>Schrijf de coördinaten van de top op.</li></ol>\n<div class=\"formule-box\">Voorbeeld: y = x² + 8x − 3<br>1 x = 0 → y = −3<br>2 x² + 8x − 3 = −3 → x² + 8x = 0 → x(x + 8) = 0 → x = 0 of x = −8<br>3 midden tussen 0 en −8: x = −4<br>4 y = (−4)² + 8 · −4 − 3 = −19<br>5 top (−4, −19)</div>\n<h4>Snijpunten met de x-as gebruiken</h4>\n<p>Staat de formule in de vorm y = (x − 3)(x + 7), dan is het handiger om de snijpunten met de x-as te gebruiken: (x − 3)(x + 7) = 0 geeft x = 3 of x = −7. De top ligt midden tussen 3 en −7, dus bij x = (3 + −7) / 2 = −2. Invullen: y = (−2 − 3)(−2 + 7) = −5 · 5 = −25. Top (−2, −25).</p>\n<p><b>Let op het teken:</b> bij de factor (x + 7) hoort x = −7, niet 7.</p>\n<h4>In context</h4><p>Bij een tunnel met h = 4,8a − 0,8a² los je 4,8a − 0,8a² = 0 op: a(4,8 − 0,8a) = 0, dus a = 0 of a = 6. De tunnel is 6 meter breed en in het midden (a = 3) is hij h = 4,8 · 3 − 0,8 · 9 = 7,2 meter hoog.</p>",
  "vragen": [
    {
      "type": "invoer",
      "vraag": "De parabool bij y = −2x² + 4x snijdt de y-as in (0, 0). Er is nog een punt op de parabool met y = 0. Bereken de x-coördinaat van dat punt.",
      "antwoord": "2",
      "uitleg": "−2x² + 4x = 0 → −2x² + 4x = 0 → x(−2x + 4) = 0 → x = 0 of x = 2. Het andere punt is (2, 0)."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = x² + 6x + 7.",
      "antwoord": "-3|−3",
      "uitleg": "1 Uit x = 0 volgt y = 7. 2 x² + 6x + 7 = 7 → x² + 6x = 0 → x(x + 6) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = (−3)² + 6 · (−3) + 7 = −2. 5 De top is (−3, −2)."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −2x² − 12x − 11.",
      "antwoord": "7",
      "uitleg": "1 Uit x = 0 volgt y = −11. 2 −2x² − 12x − 11 = −11 → −2x² − 12x = 0 → x(−2x − 12) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −2·(−3)² − 12 · (−3) − 11 = 7. 5 De top is (−3, 7)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −½x² + 4x − 11?",
      "uitleg": "1 Uit x = 0 volgt y = −11. 2 −½x² + 4x − 11 = −11 → −½x² + 4x = 0 → x(−½x + 4) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = −½·4² + 4 · 4 − 11 = −3. 5 De top is (4, −3).",
      "opties": [
        "(4, −35)",
        "(−4, −3)",
        "(4, −3)",
        "(4, −11)"
      ],
      "antwoord": 2
    },
    {
      "type": "invoer",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x + 1)(x + 3).",
      "antwoord": "-2|−2",
      "uitleg": "−(x + 1)(x + 3) = 0 → x = −1 of x = −3: de snijpunten met de x-as zijn (−1, 0) en (−3, 0). De top ligt midden tussen x = −1 en x = −3: x = (−1 + (−3)) / 2 = −2. y = −(−2 − (−1))(−2 − (−3)) = 1. Top (−2, 1)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = ½(x − 9)(x + 5) met de x-as?",
      "uitleg": "Los ½(x − 9)(x + 5) = 0 op: (x − 9) = 0 of (x + 5) = 0, dus x = 9 of x = −5. Let op het teken: bij (x + 3) hoort x = −3.",
      "opties": [
        "(5, 0) en (−9, 0)",
        "(−5, 0) en (9, 0)",
        "(0, −5) en (0, 9)",
        "(−5, 0) en (−9, 0)"
      ],
      "antwoord": 1
    },
    {
      "type": "invoer",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = (x − 9)(x − 7).",
      "antwoord": "-1|−1",
      "uitleg": "(x − 9)(x − 7) = 0 → x = 9 of x = 7: de snijpunten met de x-as zijn (9, 0) en (7, 0). De top ligt midden tussen x = 9 en x = 7: x = (9 + 7) / 2 = 8. y = (8 − 9)(8 − 7) = −1. Top (8, −1)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 3x² + 12x + 9?",
      "uitleg": "1 Uit x = 0 volgt y = 9. 2 3x² + 12x + 9 = 9 → 3x² + 12x = 0 → x(3x + 12) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = 3·(−2)² + 12 · (−2) + 9 = −3. 5 De top is (−2, −3).",
      "opties": [
        "(−2, −3)",
        "(2, −3)",
        "(−2, 45)",
        "(−2, 9)"
      ],
      "antwoord": 0
    },
    {
      "type": "invoer",
      "vraag": "De formule h = 3a − 0,25a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "12",
      "uitleg": "3a − 0,25a² = 0 → a(3 − 0,25a) = 0 → a = 0 of a = 3 / 0,25 = 12. De tunnel is 12 m breed. Midden: a = 6, h = 3 · 6 − 0,25 · 6² = 9 m."
    },
    {
      "type": "invoer",
      "vraag": "Gegeven is de formule y = x² + bx − 2. De x-coördinaat van de top van de parabool is 2. Bereken b.",
      "antwoord": "-4|−4",
      "uitleg": "De parabool snijdt de y-as in (0, -2). Het andere punt met y = -2 ligt even ver aan de andere kant van de top: x = 2 · 2 = 4. Invullen: 4² + b · 4 + (−2) = -2 → 16 + 4b = 0 → b = −4."
    },
    {
      "type": "invoer",
      "vraag": "Bij een hangbrug hoort de formule h = 0,05a² − 1a + 26. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "21",
      "uitleg": "P ligt op hoogte 26. Zelfde hoogte: 0,05a² − 1a = 0 → a = 0 of a = 1 / 0,05 = 20. Laagste punt in het midden: a = 10, h = 21 m."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = x² + 10x + 28.",
      "antwoord": "3",
      "uitleg": "1 Uit x = 0 volgt y = 28. 2 x² + 10x + 28 = 28 → x² + 10x = 0 → x(x + 10) = 0 → x = 0 of x = −10. 3 De x-coördinaat van de top ligt midden tussen 0 en −10: x = −5. 4 y = (−5)² + 10 · (−5) + 28 = 3. 5 De top is (−5, 3)."
    }
  ]
});
