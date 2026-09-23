/* =========================================================
   Duru's Scheikunde (HAVO 3) — Systematische namen
   Hoofdstuk 7 — Paragraaf 7.2 (Chemie Overal)
   ========================================================= */
DURU.register({
  "id": "sch-h7-2-systematische-namen",
  "hoofdstuk": 7,
  "paragraaf": "7.2",
  "titel": "Systematische Namen — Alkanen & Alkenen",
  "korteUitleg": "Alkanen en alkenen, homologe reeksen, isomerie, polymeren en de regels voor het geven van systematische namen aan (vertakte) koolwaterstoffen.",
  "icoon": "⛓️",
  "kleur": "h7-thema",
  "theorie": `<h3>7.2 Systematische namen</h3>
<p><b>Alkanen</b> zijn verzadigde koolwaterstoffen: hun moleculen bevatten uitsluitend enkelvoudige (C—C) bindingen. Alkanen kunnen onvertakt of vertakt zijn. De verhouding tussen het aantal C- en H-atomen in alkanen is n : (2n + 2); de algemene formule is dus <b>C<sub>n</sub>H<sub>2n+2</sub></b>. De eerste zes onvertakte alkanen vormen samen een <b>homologe reeks</b>: een reeks stoffen met een constante verhouding tussen het aantal C- en H-atomen.</p>
<table class="nask">
<thead><tr><th>naam</th><th>molecuulformule</th></tr></thead>
<tbody>
<tr><td>methaan</td><td>CH<sub>4</sub></td></tr>
<tr><td>ethaan</td><td>C<sub>2</sub>H<sub>6</sub></td></tr>
<tr><td>propaan</td><td>C<sub>3</sub>H<sub>8</sub></td></tr>
<tr><td>butaan</td><td>C<sub>4</sub>H<sub>10</sub></td></tr>
<tr><td>pentaan</td><td>C<sub>5</sub>H<sub>12</sub></td></tr>
<tr><td>hexaan</td><td>C<sub>6</sub>H<sub>14</sub></td></tr>
</tbody>
</table>

<h4>Alkenen</h4>
<p><b>Alkenen</b> bevatten net als alkanen alleen C- en H-atomen, maar hebben één dubbele binding (C=C): ze zijn dus <b>onverzadigd</b>. Door die dubbele binding hebben alkenen twee H-atomen minder dan de overeenkomstige alkaan met evenveel C-atomen. De algemene formule van de alkenen is <b>C<sub>n</sub>H<sub>2n</sub></b>. Ook alkenen kunnen onvertakt of vertakt zijn.</p>

<h4>Isomerie</h4>
<p>Bij grotere moleculen zijn er vaak meerdere structuurformules mogelijk bij dezelfde molecuulformule. Zo horen er bij de molecuulformule C<sub>4</sub>H<sub>10</sub> twee verschillende moleculen: butaan (onvertakt) en methylpropaan (vertakt). Stoffen die dezelfde molecuulformule hebben, maar een verschillende structuurformule (en dus verschillende stofeigenschappen en systematische naam), noem je <b>isomeren</b> van elkaar. Dit verschijnsel heet <b>isomerie</b>.</p>

<h4>Polymeren</h4>
<p>Onverzadigde koolwaterstoffen (alkenen) kunnen via hun dubbele binding met elkaar reageren tot lange ketens: <b>polymeren</b> ("poly" betekent veel). De kleine bouwsteentjes waaruit een polymeer is opgebouwd, heten <b>monomeren</b>. Polyetheen (PE) wordt bijvoorbeeld gemaakt met etheen als monomeer, en polypropeen (PP) met propeen als monomeer.</p>

<h4>Systematische naamgeving van alkanen</h4>
<p>De naam van een onvertakt alkaan (de <b>stamnaam</b>) hoort bij het aantal C-atomen en eindigt altijd op <b>-aan</b>.</p>
<div class="formule-box">
  <b>Stappenplan naamgeving vertakt alkaan:</b><br>
  1. Zoek de langste onvertakte keten op (de <b>hoofdketen</b>); de naam is gelijk aan het onvertakte alkaan met evenveel C-atomen.<br>
  2. Zoek de vertakkingen op (<b>alkylgroepen</b>, uitgang -yl in plaats van -aan, bijv. -CH<sub>3</sub> = methyl). Gebruik bij herhaling een voorvoegsel (di-, tri-, tetra-…) en zet de naam van de vertakking(en) vóór de naam van de hoofdketen.<br>
  3. Nummer de C-atomen van de hoofdketen zo, dat de vertakkingen zo laag mogelijke nummers krijgen. Zet de nummers vóór de naam, gescheiden door een komma tussen getallen en een streepje tussen getal en letter.
</div>
<div class="voorbeeld">
  <span class="vb-kop">Voorbeeld</span>
  <span class="stap">Het vertakte alkaan met als hoofdketen pentaan en één methylgroep aan het tweede C-atoom heet <b>2-methylpentaan</b>.</span>
</div>

<h4>Systematische naamgeving van alkenen</h4>
<p>De naamgeving van alkenen werkt net als bij alkanen, met twee aanvullingen: de uitgang is <b>-een</b> in plaats van -aan, en vanaf vier C-atomen geef je de plaats van de dubbele binding aan met een cijfer. Je nummert de hoofdketen zo, dat dit cijfer zo laag mogelijk is. Zo heet H<sub>2</sub>C=CH—CH<sub>2</sub>—CH<sub>3</sub> <b>but-1-een</b> en H<sub>3</sub>C—CH=CH—CH<sub>3</sub> <b>but-2-een</b>.</p>

<div class="begrippen-box">
  <li><b>Alkaan:</b> verzadigde koolwaterstof, algemene formule C<sub>n</sub>H<sub>2n+2</sub>, naam eindigt op -aan.</li>
  <li><b>Alkeen:</b> onverzadigde koolwaterstof met één C=C-binding, algemene formule C<sub>n</sub>H<sub>2n</sub>, naam eindigt op -een.</li>
  <li><b>Homologe reeks:</b> reeks stoffen met een constante verhouding tussen het aantal C- en H-atomen.</li>
  <li><b>Isomeren:</b> stoffen met dezelfde molecuulformule maar een verschillende structuurformule.</li>
  <li><b>Alkylgroep:</b> een vertakking van een koolstofketen (bijv. methylgroep, ethylgroep).</li>
</div>`,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de algemene formule van de <b>alkanen</b>?",
      "opties": [
        "C<sub>n</sub>H<sub>2n+2</sub>",
        "C<sub>n</sub>H<sub>2n</sub>",
        "C<sub>n</sub>H<sub>n</sub>",
        "C<sub>n+1</sub>H<sub>2n</sub>"
      ],
      "antwoord": 0,
      "uitleg": "Alkanen zijn verzadigde koolwaterstoffen met algemene formule CnH2n+2 (n = aantal C-atomen)."
    },
    {
      "type": "mc",
      "vraag": "Waarom zijn alkanen <b>verzadigde</b> koolwaterstoffen?",
      "opties": [
        "Ze bevatten een C=C-binding",
        "Ze bevatten alleen enkelvoudige (C—C) bindingen",
        "Ze zijn altijd vertakt",
        "Ze bevatten stikstofatomen"
      ],
      "antwoord": 1,
      "uitleg": "Verzadigd betekent dat er geen dubbele bindingen tussen C-atomen voorkomen, alleen enkelvoudige bindingen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Alkenen hebben de algemene formule C<sub>n</sub>H<sub>2n</sub> en bevatten één dubbele binding tussen twee C-atomen.",
      "antwoord": true,
      "uitleg": "Waar: door de dubbele binding hebben alkenen twee H-atomen minder dan de overeenkomstige alkaan."
    },
    {
      "type": "mc",
      "vraag": "Butaan (C₄H₁₀) en methylpropaan zijn twee verschillende stoffen met dezelfde molecuulformule maar een andere structuurformule. Hoe noem je dit verschijnsel?",
      "opties": [
        "Isomerie",
        "Destillatie",
        "Polymerisatie",
        "Homologie"
      ],
      "antwoord": 0,
      "uitleg": "Isomerie is het verschijnsel dat verschillende stoffen dezelfde molecuulformule hebben, maar een verschillende structuurformule."
    },
    {
      "type": "waaronwaar",
      "vraag": "Isomeren hebben altijd precies dezelfde stofeigenschappen, omdat ze dezelfde molecuulformule hebben.",
      "antwoord": false,
      "uitleg": "Onwaar: isomeren hebben een verschillende structuurformule en daardoor ook verschillende stofeigenschappen."
    },
    {
      "type": "mc",
      "vraag": "Polyetheen wordt gemaakt van etheen. Hoe noem je zo’n klein molecuul (zoals etheen) waaruit een polymeer is opgebouwd?",
      "opties": [
        "Een isomeer",
        "Een polymeer",
        "Een alkaan",
        "Een monomeer"
      ],
      "antwoord": 3,
      "uitleg": "Een monomeer is het kleine bouwsteenmolecuul waaruit, via reactie van de dubbele binding, een polymeer (lange keten) wordt opgebouwd."
    },
    {
      "type": "invoer",
      "niveau": 1,
      "vraag": "Hoe heet de vertakking met formule -CH₃ in de systematische naamgeving? (uitgang -yl)",
      "antwoord": "methyl|methylgroep",
      "uitleg": "De vertakking -CH3 heet een methylgroep; de uitgang -yl vervangt de uitgang -aan van het alkaan."
    },
    {
      "type": "mc",
      "vraag": "Welke uitgang krijgt de naam van een <b>alkeen</b> (in plaats van -aan bij alkanen)?",
      "opties": [
        "-yl",
        "-ol",
        "-een",
        "-ine"
      ],
      "antwoord": 2,
      "uitleg": "Alkenen krijgen de uitgang -een, bijvoorbeeld etheen, propeen en buteen."
    },
    {
      "type": "mc",
      "vraag": "Bij etheen en propeen staat geen plaatsnummer in de naam, bij but-1-een wel. Vanaf hoeveel C-atomen in de hoofdketen is dat plaatsnummer van de dubbele binding nodig?",
      "opties": [
        "Vanaf 2 C-atomen",
        "Vanaf 3 C-atomen",
        "Vanaf 4 C-atomen",
        "Dat is nooit nodig"
      ],
      "antwoord": 2,
      "uitleg": "Vanaf vier C-atomen zijn er meerdere posities voor de dubbele binding mogelijk, dus dan geef je die met een cijfer aan (bijv. but-1-een, but-2-een)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij het nummeren van een vertakt alkaan mag je altijd vanaf beide zijden van de hoofdketen beginnen; het resultaat maakt niet uit.",
      "antwoord": false,
      "uitleg": "Onwaar: je moet nummeren zodat de vertakkingen zo laag mogelijke nummers krijgen, dus het beginpunt maakt wel degelijk uit."
    }
  ]
});
