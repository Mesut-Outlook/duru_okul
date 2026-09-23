/* =========================================================
   Duru's Scheikunde (HAVO 3) — Ontleding
   Hoofdstuk 4 — Paragraaf 4.2 (Chemie Overal, Reacties en energie)
   ========================================================= */
DURU.register({
  id: "sch-h4-2-ontleding",
  hoofdstuk: 4,
  paragraaf: "4.2",
  titel: "Ontleding",
  korteUitleg: "Eén beginstof en twee of meer reactieproducten: thermolyse, elektrolyse en fotolyse, en het opstellen van ontledingsvergelijkingen.",
  icoon: "⚗️",
  kleur: "h4-thema",
  theorie: `<h3>4.2 Ontleding</h3>
<p>Een <b>ontledingsreactie</b> is een reactie met precies <b>één beginstof</b>, die uiteenvalt tot <b>twee of meer reactieproducten</b>. Dit kunnen niet-ontleedbare stoffen zijn (zoals metalen of zuurstofgas), maar ook verbindingen. Zo ontstaat bij de ontleding van magnesiumchloride (MgCl<sub>2</sub>) het niet-ontleedbare magnesium (Mg) én chloor (Cl<sub>2</sub>).</p>
<p>Het grote verschil met een verbrandingsreactie is dat je bij een ontleding <b>geen zuurstof</b> nodig hebt. De meeste ontledingsreacties zijn <b>endotherm</b>: je moet er voortdurend energie in stoppen, anders stopt de reactie.</p>
<h4>Drie soorten ontledingsreacties</h4>
<div class="begrippen-box">
  <ul>
    <li><b>Thermolyse</b> — ontleding door <b>warmte</b>. Voorbeeld: in een kalkoven wordt kalksteen (CaCO<sub>3</sub>) voortdurend verhit tot ongebluste kalk (CaO) en koolstofdioxide (CO<sub>2</sub>).</li>
    <li><b>Elektrolyse</b> — ontleding door <b>elektrische stroom</b>. Voorbeeld: van gesmolten bauxiet (Al<sub>2</sub>O<sub>3</sub>) wordt aluminium gemaakt door er stroom doorheen te leiden. Dit kost veel energie, daarom is aluminium relatief prijzig.</li>
    <li><b>Fotolyse</b> — ontleding door <b>licht</b>. Dit is vaak een ongewenste reactie: kleur- en smaakstoffen in bier gaan bijvoorbeeld langzaam kapot als het licht op de fles schijnt (daarom worden bierflesjes vaak bruin gemaakt).</li>
  </ul>
</div>
<p>Een uitzondering vormen enkele <b>exotherme</b> ontledingsreacties: bij het ontleden van natriumazide (NaN<sub>3</sub>) in een airbag komt in zeer korte tijd veel stikstofgas vrij, waardoor de airbag zich razendsnel opblaast. Om deze exotherme reactie op gang te brengen is wel eerst een kleine verbrandingsreactie nodig.</p>
<h4>Vergelijkingen van ontledingsreacties opstellen</h4>
<p>Bij een ontledingsreactie zet je alleen de formule van de beginstof voor de pijl (er is immers maar één beginstof). Vaak kun je aan de formule van de beginstof aflezen welke reactieproducten kunnen ontstaan.</p>
<div class="voorbeeld">
  <div class="vb-kop">Voorbeeld 1 — Fotolyse van zilverchloride (AgCl)</div>
  <div class="stap">Alleen de beginstof voor de pijl: AgCl → Ag + Cl<sub>2</sub></div>
  <div class="stap">Kloppend maken: 2 AgCl → 2 Ag + Cl<sub>2</sub></div>
</div>
<div class="voorbeeld">
  <div class="vb-kop">Voorbeeld 2 — Ontleding van vlugzout (N<sub>2</sub>H<sub>6</sub>CO<sub>3</sub>)</div>
  <div class="stap">Formules opschrijven: N<sub>2</sub>H<sub>6</sub>CO<sub>3</sub> → NH<sub>3</sub> + CO<sub>2</sub> + H<sub>2</sub>O</div>
  <div class="stap">Kloppend maken: N<sub>2</sub>H<sub>6</sub>CO<sub>3</sub> → 2 NH<sub>3</sub> + CO<sub>2</sub> + H<sub>2</sub>O</div>
</div>
<p>Let op het verschil tussen <b>ontleden</b> en <b>scheiden</b>: bij scheiden ga je uit van een <b>mengsel</b> (bijvoorbeeld een suspensie van krijt en water) waarbij géén nieuwe stof ontstaat. Bij ontleden ga je juist uit van één <b>zuivere stof</b> en ontstaan er door een chemische reactie nieuwe stoffen.</p>`,
  vragen: [
    {
      type: "mc",
      vraag: "Hoe zou je een ontledingsreactie het beste omschrijven?",
      opties: [
        "Een reactie met precies één beginstof en twee of meer reactieproducten",
        "Een reactie met twee beginstoffen en één reactieproduct",
        "Een reactie waarbij altijd zuurstof nodig is",
        "Een reactie die alleen bij kamertemperatuur verloopt"
      ],
      antwoord: 0,
      uitleg: "Een ontledingsreactie heeft altijd precies één beginstof, die uiteenvalt in twee of meer reactieproducten."
    },
    {
      type: "mc",
      vraag: "Hoe heet het ontleden van kalksteen (CaCO3) tot ongebluste kalk (CaO) en koolstofdioxide in een kalkoven?",
      opties: [
        "Destillatie",
        "Thermolyse",
        "Fotolyse",
        "Elektrolyse"
      ],
      antwoord: 1,
      uitleg: "Ontleding door middel van warmte (verhitten) heet thermolyse."
    },
    {
      type: "mc",
      vraag: "Met welke methode wordt aluminium gewonnen uit gesmolten bauxiet (Al2O3)?",
      opties: [
        "Door verhitting zonder elektrische stroom",
        "Door blootstelling aan zonlicht",
        "Door elektrolyse: elektrische stroom door het gesmolten bauxiet leiden",
        "Door het te mengen met koud water"
      ],
      antwoord: 2,
      uitleg: "De ontleding van bauxiet tot aluminium gebeurt door elektrolyse, wat veel energie kost."
    },
    {
      type: "mc",
      vraag: "Om welke reden krijgen bierflesjes vaak een bruine kleur?",
      opties: [
        "Om het bier langer warm te houden",
        "Om het gewicht van de fles te verminderen",
        "Om de fles beter herkenbaar te maken in de winkel",
        "Om fotolyse van kleur- en smaakstoffen door licht te vertragen"
      ],
      antwoord: 3,
      uitleg: "Licht kan kleur- en smaakstoffen in bier door fotolyse afbreken. Bruin glas houdt een deel van dat licht tegen."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een ontledingsreactie is er, net als bij een verbranding, altijd zuurstof nodig.",
      antwoord: false,
      uitleg: "Onwaar: bij een ontledingsreactie is geen zuurstof nodig. Dat is juist een belangrijk verschil met een verbrandingsreactie."
    },
    {
      type: "waaronwaar",
      vraag: "De meeste ontledingsreacties zijn endotherm: je moet er voortdurend energie in stoppen.",
      antwoord: true,
      uitleg: "Waar: op de exotherme uitzonderingen (zoals de airbagreactie) na, is voor de meeste ontledingsreacties steeds warmte, licht of stroom nodig."
    },
    {
      type: "invoer",
      vraag: "Vul de ontbrekende coëfficiënt in: AgCl → ... Ag + Cl<sub>2</sub> wordt kloppend als je 2 AgCl → 2 Ag + Cl<sub>2</sub> schrijft. Hoeveel Ag-atomen (coëfficiënt) staan er dan links en rechts?",
      antwoord: "2|twee",
      uitleg: "2 AgCl → 2 Ag + Cl2: links en rechts staan telkens 2 zilveratomen (Ag), zodat de vergelijking klopt."
    },
    {
      type: "invoer",
      vraag: "Vul de ontbrekende coëfficiënt in: N2H6CO3 → ... NH3 + CO2 + H2O (ontleding van vlugzout).",
      antwoord: "2|twee",
      uitleg: "N2H6CO3 → 2 NH3 + CO2 + H2O. Zo kloppen alle atoomsoorten links en rechts."
    },
    {
      type: "invoer",
      vraag: "Hoe heet de ontleding van een stof door middel van elektrische stroom?",
      antwoord: "elektrolyse",
      uitleg: "Ontleding door elektrische stroom heet elektrolyse."
    }
  ]
});
