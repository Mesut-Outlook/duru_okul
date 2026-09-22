/* =========================================================
   Duru's Wiskunde (HAVO 3) — Begrippen H1 §1.1–1.2
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.1–1.2 (met aantekeningen docent)
   ========================================================= */
DURU.register({
  "id": "h1-begrippen",
  "hoofdstuk": 1,
  "paragraaf": "1.1–1.2",
  "titel": "Begrippen & Kernconcepten — Lineaire formules",
  "korteUitleg": "Richtingscoëfficiënt, startgetal, evenwijdig, snijpunt en het stappenplan: alle begrippen van §1.1 en §1.2.",
  "icoon": "📖",
  "kleur": "blauw",
  "theorie": "<h3>Begrippen H1 · Lineaire formules (§1.1 en §1.2)</h3>\n<p>Hieronder staan alle begrippen uit paragraaf 1.1 <i>Lineaire formules opstellen</i> en 1.2 <i>Lijnen snijden</i>. Je docent heeft vooral geoefend met: de richtingscoëfficiënt uit twee punten berekenen (let op mintekens!), het startgetal vinden door een punt in te vullen, evenwijdige lijnen en het snijpunt van twee lijnen berekenen.</p>\n<h4>Lineaire formule en lineair verband</h4>\n<div class=\"formule-box\"><code>y = ax + b</code><br>• <b>a</b> = <b>richtingscoëfficiënt</b> (ander woord: <b>hellingsgetal</b>)<br>• <b>b</b> = <b>startgetal</b> = de y-coördinaat van het snijpunt met de y-as, dus het punt (0, b)</div>\n<p>De grafiek van een lineaire formule is een rechte lijn. Een verband waarbij y elke stap evenveel toeneemt, heet een <b>lineair verband</b>. De volgorde maakt niet uit: y = 2 − 1/3x is hetzelfde als y = −1/3x + 2 (a = −1/3, b = 2). Bij y = −x + 2 is a = −1.</p>\n<h4>Richtingscoëfficiënt berekenen</h4>\n<div class=\"formule-box\"><code>richtingscoëfficiënt = toename tweede coördinaat / toename eerste coördinaat</code><br>Voorbeeld: door (−1, 3) en (3, 11): a = (11 − 3) / (3 − (−1)) = 8 / 4 = 2.</div>\n<p>In een grafiek maak je een <b>trapje</b>: zoveel naar rechts, zoveel omhoog (+) of omlaag (−).</p>\n<ul><li><b>Stijgende lijn</b>: richtingscoëfficiënt positief. Hoe groter, hoe <b>steiler</b>.</li><li><b>Dalende lijn</b>: richtingscoëfficiënt negatief.</li><li><b>Horizontale lijn</b>: richtingscoëfficiënt 0, formule y = getal (bijv. y = −4).</li></ul>\n<h4>Startgetal berekenen door invullen</h4>\n<p>Weet je a, vul dan de coördinaten van één punt in bij y = ax + b en los b op. Voorbeeld: a = 5, punt (7, 13): 13 = 35 + b, dus b = −22. Ligt het punt op de y-as (x = 0), dan lees je b direct af.</p>\n<p><b>Ligt een punt op de lijn?</b> Vul de x-coördinaat in. Komt precies de y-coördinaat eruit, dan ligt het punt erop; anders niet.</p>\n<h4>Evenwijdig</h4>\n<p>Lijnen die <b>evenwijdig</b> lopen, hebben <b>dezelfde richtingscoëfficiënt</b> (maar een ander startgetal). Ze hebben nooit een snijpunt. Lijn door (1, 7) evenwijdig aan y = 6x − 12: a = 6, 7 = 6 + b, dus y = 6x + 1.</p>\n<h4>Snijpunt van twee lijnen — stappenplan</h4>\n<ol><li>Stel bij elke lijn een formule op.</li><li>Stel de twee formules aan elkaar gelijk: dat is de <b>vergelijking</b>.</li><li>Los de vergelijking op → de <b>x-coördinaat</b> van het snijpunt.</li><li>Vul die x in bij één formule → de <b>y-coördinaat</b>.</li><li><b>Controleer</b>: vul x ook in bij de andere formule.</li></ol>\n<p>Het <b>snijpunt met de y-as</b> vind je met x = 0, het <b>snijpunt met de x-as</b> met y = 0. Twee lijnen met hetzelfde startgetal snijden elkaar op de y-as.</p>\n<table><tr><th>Begrip</th><th>Betekenis</th></tr><tr><td>assenstelsel</td><td>x-as (horizontaal) en y-as (verticaal); ze snijden elkaar in de oorsprong O(0, 0)</td></tr><tr><td>coördinaten</td><td>(eerste coördinaat, tweede coördinaat) = (x, y)</td></tr><tr><td>toename</td><td>hoeveel een coördinaat groter wordt (kan ook negatief zijn)</td></tr><tr><td>snijpunt</td><td>punt dat op beide lijnen ligt</td></tr><tr><td>schets</td><td>grafiek zonder precieze tabel: let op startgetal en stijgend/dalend</td></tr></table>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Hoe heet de a in de formule y = ax + b?",
      "opties": [
        "startgetal",
        "snijpunt",
        "coördinaat",
        "richtingscoëfficiënt"
      ],
      "antwoord": 3,
      "uitleg": "a is de richtingscoëfficiënt (ook: hellingsgetal). b is het startgetal."
    },
    {
      "type": "invoer",
      "vraag": "Een ander woord voor richtingscoëfficiënt is het ____.",
      "antwoord": "hellingsgetal|het hellingsgetal|helling",
      "uitleg": "In het boek worden richtingscoëfficiënt en hellingsgetal door elkaar gebruikt."
    },
    {
      "type": "mc",
      "vraag": "Wat stelt het startgetal b in y = ax + b voor in de grafiek?",
      "opties": [
        "de x-coördinaat van het snijpunt met de x-as",
        "hoe steil de lijn loopt",
        "de y-coördinaat van het snijpunt met de y-as",
        "het snijpunt van twee lijnen"
      ],
      "antwoord": 2,
      "uitleg": "Bij x = 0 is y = b. De lijn snijdt de y-as dus in (0, b)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een lijn met een negatieve richtingscoëfficiënt is een stijgende lijn.",
      "antwoord": false,
      "uitleg": "Onwaar. Negatieve richtingscoëfficiënt = dalende lijn. Positief = stijgend."
    },
    {
      "type": "invoer",
      "vraag": "Lijnen met dezelfde richtingscoëfficiënt en een verschillend startgetal lopen ____.",
      "antwoord": "evenwijdig|parallel",
      "uitleg": "Dezelfde richtingscoëfficiënt = evenwijdig. Ze snijden elkaar nooit."
    },
    {
      "type": "mc",
      "vraag": "Richtingscoëfficiënt = toename tweede coördinaat / ...",
      "opties": [
        "toename startgetal",
        "toename eerste coördinaat",
        "tweede coördinaat",
        "eerste coördinaat"
      ],
      "antwoord": 1,
      "uitleg": "a = toename y / toename x = toename tweede coördinaat / toename eerste coördinaat."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om het snijpunt van twee lijnen te berekenen, stel je de twee formules aan elkaar gelijk.",
      "antwoord": true,
      "uitleg": "Waar. In het snijpunt is y bij beide lijnen gelijk, dus ax + b = cx + d. Daaruit volgt de x-coördinaat."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij een horizontale lijn?",
      "opties": [
        "y = −4",
        "y = −4x",
        "y = x − 4",
        "y = 4x + 4"
      ],
      "antwoord": 0,
      "uitleg": "Een horizontale lijn heeft richtingscoëfficiënt 0: y = 0 · x + b = b, dus bijvoorbeeld y = −4."
    }
  ]
});
