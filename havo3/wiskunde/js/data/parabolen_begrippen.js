/* =========================================================
   Duru's Wiskunde (HAVO 3) — Begrippen H2 Parabolen
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.register({
  "id": "h2-parabolen-begrippen",
  "hoofdstuk": 2,
  "paragraaf": "begrippen",
  "titel": "Begrippen & Kernconcepten — Parabolen",
  "korteUitleg": "Parabool, berg- en dalparabool, top, symmetrieas, de drie vormen en wat a, b en c je vertellen.",
  "icoon": "📖",
  "kleur": "blauw",
  "theorie": "<h3>Begrippen H2 · Parabolen</h3>\n<p>Alle begrippen uit hoofdstuk 2 op een rij. Ken je ze, dan begrijp je de opdrachten in de toets meteen.</p>\n<ul><li><b>kwadratische formule</b> — formule met x² als hoogste macht, zoals y = x² − 4x + 1.</li><li><b>parabool</b> — de grafiek bij een kwadratische formule.</li><li><b>dalparabool</b> — opening naar boven; het getal voor x² is positief; de top is het laagste punt.</li><li><b>bergparabool</b> — opening naar beneden; het getal voor x² is negatief; de top is het hoogste punt.</li><li><b>top</b> — het hoogste (bergparabool) of laagste (dalparabool) punt van de parabool.</li><li><b>symmetrieas</b> — de verticale lijn door de top, bijvoorbeeld x = 3.</li><li><b>snijpunt met de y-as</b> — het punt (0, c); je vindt het door x = 0 in te vullen.</li><li><b>snijpunten met de x-as</b> — punten (…, 0); je vindt ze door y = 0 te stellen en de vergelijking op te lossen.</li><li><b>oorsprong</b> — het punt (0, 0). Bij c = 0 gaat de parabool erdoor.</li><li><b>algemene vorm</b> — y = ax² + bx + c.</li><li><b>vorm y = a(x − s)(x − t)</b> — hieruit lees je de snijpunten met de x-as af: (s, 0) en (t, 0).</li><li><b>vorm y = a(x − p)² + q</b> — hieruit lees je de top (p, q) af.</li><li><b>smaller / breder</b> — hoe verder a van 0, hoe smaller; hoe dichter bij 0, hoe breder.</li><li><b>haakjes wegwerken</b> — een formule zonder haakjes schrijven, bijvoorbeeld met een <b>vermenigvuldigtabel</b>.</li><li><b>ontbinden in factoren</b> — het omgekeerde: x² + 8x = x(x + 8). Handig om ax² + bx = 0 op te lossen.</li><li><b>kwadratische vergelijking</b> — vergelijking met x², bijvoorbeeld x² − 6x = 0 of (x − 3)(x + 7) = 0.</li></ul>\n<h4>De aanpak voor de top in vijf stappen</h4><ol><li>Snijpunt met de y-as: x = 0 → y = c.</li><li>Ander punt met y = c: los ax² + bx = 0 op.</li><li>x-coördinaat van de top = midden tussen de oplossingen.</li><li>y-coördinaat: x-coördinaat invullen.</li><li>Coördinaten opschrijven.</li></ol>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Hoe heet de grafiek bij een kwadratische formule?",
      "uitleg": "De grafiek bij een kwadratische formule zoals y = x² − 4x + 1 is een parabool.",
      "opties": [
        "een rechte lijn",
        "een hyperbool",
        "een exponentiële kromme",
        "een parabool"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat is de top van een bergparabool?",
      "uitleg": "Bij een bergparabool is de top het hoogste punt, bij een dalparabool het laagste punt.",
      "opties": [
        "het snijpunt met de x-as",
        "het snijpunt met de y-as",
        "het hoogste punt van de parabool",
        "het laagste punt van de parabool"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Wat is de algemene vorm van een kwadratische formule?",
      "uitleg": "y = ax² + bx + c is de algemene vorm. De vormen y = a(x − s)(x − t) en y = a(x − p)² + q kun je daarin omschrijven.",
      "opties": [
        "y = a(x − p)² + q",
        "y = ax² + bx + c",
        "y = ax + b",
        "y = b · gᵗ"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Wat weet je als in y = ax² + bx + c geldt b = 0?",
      "uitleg": "b = 0 geeft y = ax² + c; de top is (0, c) en ligt op de y-as.",
      "opties": [
        "de parabool is een bergparabool",
        "de top ligt op de y-as",
        "de grafiek is een rechte lijn",
        "de parabool gaat door de oorsprong"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Welke parabool is het smalst?",
      "uitleg": "Hoe verder a van 0 af ligt, hoe smaller. −4 ligt het verst van 0.",
      "opties": [
        "y = −4x² + 1",
        "y = 2x² + 1",
        "y = x² + 1",
        "y = −½x² + 1"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Bij welke formule kun je de snijpunten met de x-as direct aflezen?",
      "uitleg": "Uit a(x − s)(x − t) = 0 volgt x = s of x = t: de snijpunten (s, 0) en (t, 0).",
      "opties": [
        "y = a(x − s)(x − t)",
        "y = ax² + c",
        "y = ax² + bx + c",
        "y = a(x − p)² + q"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Hoe vind je met de snijpunten met de x-as de x-coördinaat van de top?",
      "uitleg": "De top ligt op de symmetrieas, precies midden tussen de twee snijpunten met de x-as.",
      "opties": [
        "vul x = 0 in",
        "neem de grootste x-coördinaat",
        "neem het getal midden tussen de twee x-coördinaten",
        "tel de twee x-coördinaten op"
      ],
      "antwoord": 2
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet het hoogste of laagste punt van een parabool? (één woord)",
      "antwoord": "top|de top",
      "uitleg": "Het hoogste punt van een bergparabool en het laagste punt van een dalparabool heet de top."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet de lijn waarin een parabool symmetrisch is? (één woord)",
      "antwoord": "symmetrieas|de symmetrieas",
      "uitleg": "De symmetrieas is de verticale lijn door de top."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij y = −3x² + 6x hoort een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. a = −3 is negatief: een bergparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De parabool bij y = 2x² − 8x gaat door de oorsprong.",
      "antwoord": true,
      "uitleg": "Waar. c = 0: bij x = 0 is y = 0."
    },
    {
      "type": "waaronwaar",
      "vraag": "(x + 4)² is hetzelfde als x² + 16.",
      "antwoord": false,
      "uitleg": "Onwaar. (x + 4)² = (x + 4)(x + 4) = x² + 8x + 16. De term 8x vergeet je snel."
    }
  ]
});
