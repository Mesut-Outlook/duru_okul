DURU.register({
  id: "sp-3",
  hoofdstuk: 1,
  paragraaf: "1.3",
  titel: "Voltooid deelwoord (vd)",
  korteUitleg: "Spelling van het voltooid deelwoord: regelmatige en onregelmatige vormen.",
  icoon: "🏁",
  theorie: `
    <h3>Voltooid deelwoord (vd)</h3>
    <p>Een voltooid deelwoord vertelt dat iets al <b>klaar</b> (voltooid) is. Je gebruikt het altijd in combinatie met een hulpwerkwoord (meestal <b>hebben</b>, <b>zijn</b> of <b>worden</b>).</p>

    <div class="esempio" style="background:#fffbeb; border: 1px solid #fde68a; border-radius: var(--radius); padding: 16px 20px; margin: 18px 0;">
      <p><i>Voorbeeld:</i> Ik <b>heb</b> mijn huiswerk <b>gemaakt</b>.</p>
      <p><i>Voorbeeld:</i> Wij <b>zijn</b> naar school <b>gegaan</b>.</p>
    </div>

    <h3>1. Regelmatige werkwoorden (eindigen op -d of -t)</h3>
    <p>Bij regelmatige werkwoorden begint het voltooid deelwoord meestal met <b>ge-</b> en eindigt het op een <b>-d</b> of <b>-t</b>. Om te weten of je een <b>d</b> of <b>t</b> schrijft, gebruik je weer <b>'t kofschip</b>:</p>

    <ul>
      <li>Zit de laatste letter van de stam-basis (hele werkwoord min -en) in <b>'t kofschip</b>? &rarr; Het voltooid deelwoord eindigt op een <b>t</b>.</li>
      <li>Zit de letter er <b>niet</b> in? &rarr; Het voltooid deelwoord eindigt op een <b>d</b>.</li>
    </ul>

    <div class="voorbeeld">
      <div class="vb-kop">📐 Voorbeeld: maken, kleden, spelen</div>
      <div class="stap"><b>maken</b> &rarr; stam-basis <i>mak-</i> (k zit in 't kofschip) &rarr; ge + maak + <b>t</b> = <b>gemaakt</b></div>
      <div class="stap"><b>kleden</b> &rarr; stam-basis <i>kled-</i> (d zit NIET in 't kofschip) &rarr; ge + kleed + <b>d</b> = <b>gekleed</b> (stam eindigt al op d, dus je voegt niks toe)</div>
      <div class="stap"><b>spelen</b> &rarr; stam-basis <i>spel-</i> (l zit NIET in 't kofschip) &rarr; ge + speel + <b>d</b> = <b>gespeeld</b></div>
    </div>

    <h3>2. Onregelmatige & sterke werkwoorden</h3>
    <p>Sterke en onregelmatige werkwoorden krijgen vaak <b>ge-</b> en eindigen meestal op <b>-en</b>, of veranderen van klank. Dit zijn de belangrijkste vormen uit je aantekeningen:</p>

    <div class="voorbeeld">
      <div class="vb-kop">📐 Voorbeelden uit je aantekeningen</div>
      <div class="stap"><b>zien</b> &rarr; <b>gezien</b></div>
      <div class="stap"><b>gaan</b> &rarr; <b>gegaan</b></div>
      <div class="stap"><b>kopen</b> &rarr; <b>gekocht</b></div>
      <div class="stap"><b>laten</b> &rarr; <b>gelaten</b></div>
      <div class="stap"><b>vergeten</b> &rarr; <b>vergeten</b> (zonder ge- aan het begin!)</div>
    </div>
  `,
  vragen: [
    {
      type: "mc", niveau: 1,
      vraag: "Welk hulpwerkwoord wordt gebruikt in de zin: 'Ik <b>heb</b> mijn fiets gemaakt.'?",
      opties: ["maken", "heb", "fiets", "gemaakt"],
      antwoord: 1,
      uitleg: "In deze zin is <b>heb</b> (van hebben) het hulpwerkwoord en <i>gemaakt</i> het voltooid deelwoord.",
      hint: "Het hulpwerkwoord helpt om de voltooide tijd te vormen."
    },
    {
      type: "waaronwaar", niveau: 1,
      vraag: "Het voltooid deelwoord van <b>vergeten</b> is <i>gevergeten</i>.",
      antwoord: false,
      uitleg: "Onwaar: werkwoorden die al beginnen met ver-, be-, ont-, of ge- krijgen geen extra 'ge-'. Het is gewoon <b>vergeten</b>.",
      hint: "Denk aan de aantekeningen: vergeten &rarr; vergeten."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul het juiste voltooid deelwoord in: 'Ik heb gisteren een taart ___ (maken).'",
      antwoord: "gemaakt",
      uitleg: "Het werkwoord is <i>maken</i>. De k zit in 't kofschip, dus het eindigt op een t: ge + maak + t = <b>gemaakt</b>.",
      hint: "maken &rarr; ge + maak + ?"
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul het juiste voltooid deelwoord in: 'Duru heeft een nieuwe jas ___ (kopen).'",
      antwoord: "gekocht",
      uitleg: "<i>Kopen</i> is een onregelmatig werkwoord. Het voltooid deelwoord is <b>gekocht</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul het juiste voltooid deelwoord in: 'Wij zijn vorige week naar het strand ___ (gaan).'",
      antwoord: "gegaan",
      uitleg: "<i>Gaan</i> is een onregelmatig werkwoord. Het voltooid deelwoord is <b>gegaan</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul het juiste voltooid deelwoord in: 'De voetballer heeft de hele wedstrijd ___ (spelen).'",
      antwoord: "gespeeld",
      uitleg: "De stam-basis van <i>spelen</i> is <i>spel-</i> (eindigt op l). De l zit niet in 't kofschip, dus het eindigt op een d: ge + speel + d = <b>gespeeld</b>."
    },
    {
      type: "mc", niveau: 2,
      vraag: "Wat is het juiste voltooid deelwoord van <b>reizen</b>?",
      opties: ["gereisd", "gereist", "gereizd", "gereistd"],
      antwoord: 0,
      uitleg: "Hele werkwoord is <i>reizen</i>. Stam-basis min -en eindigt op <b>z</b>. De z zit niet in 't kofschip, dus we schrijven een <b>d</b> aan het eind: <b>gereisd</b>.",
      hint: "Let op de z in reizen!"
    },
    {
      type: "waaronwaar", niveau: 2,
      vraag: "Het voltooid deelwoord van <b>kleden</b> is <i>gekleed</i>.",
      antwoord: true,
      uitleg: "Waar! De stam van kleden is <i>kleed</i> (eindigt op d). Omdat de d niet in 't kofschip zit, eindigt het op een d: ge + kleed + d = gekleed (één d aan het eind)."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul het juiste voltooid deelwoord in: 'Ik heb de dief in de straat ___ (zien).'",
      antwoord: "gezien",
      uitleg: "<i>Zien</i> is een sterk werkwoord. Het voltooid deelwoord is <b>gezien</b>."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Vul het juiste voltooid deelwoord in: 'De lerares heeft mijn vraag ___ (beantwoorden).'",
      antwoord: "beantwoord",
      uitleg: "Het werkwoord begint al met <i>be-</i>, dus geen 'ge-'. De stam-basis van <i>antwoorden</i> eindigt op d (niet in 't kofschip), dus: be + antwoord + d = <b>beantwoord</b> (met één d aan het eind).",
      hint: "Let op: begint met 'be-', en de stam eindigt al op d."
    },
    {
      type: "mc", niveau: 3,
      vraag: "Welke zin is correct gespeld?",
      opties: [
        "Hij heeft de brief gisteren verstuurd.",
        "Hij heeft de brief gisteren verstuurt.",
        "Hij heeft de brief gisteren verstuurdt."
      ],
      antwoord: 0,
      uitleg: "Het werkwoord is <i>versturen</i> (stam-basis min -en eindigt op r). R zit niet in 't kofschip, dus eindigt op d. Omdat het begint met ver-, schrijven we geen ge-: <b>verstuurd</b>."
    },
    {
      type: "waaronwaar", niveau: 3,
      vraag: "Het voltooid deelwoord van <b>verven</b> is <i>geverfd</i>.",
      antwoord: true,
      uitleg: "Waar! Hele werkwoord <i>verven</i> (stam-basis min -en eindigt op v). De v zit niet in 't kofschip, dus we schrijven een d aan het eind: <b>geverfd</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul het juiste voltooid deelwoord in: 'De leraar heeft ons op tijd ___ (laten) gaan.'",
      antwoord: "gelaten",
      uitleg: "<i>Laten</i> is een sterk werkwoord. Het voltooid deelwoord is <b>gelaten</b>."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Vul het juiste voltooid deelwoord in: 'Jij hebt ons erg ___ (verrassen) met je cijfer!'",
      antwoord: "verrast",
      uitleg: "Het werkwoord begint met <i>ver-</i> (geen ge-). De stam-basis van <i>verrassen</i> is <i>verras-</i> (eindigt op s). De s zit in 't kofschip, dus eindigt op t: ver + ras + t = <b>verrast</b>.",
      hint: "Begint met 'ver-', en de s zit in 't kofschip."
    },
    {
      type: "mc", niveau: 3,
      vraag: "Welke zin is correct gespeld?",
      opties: [
        "Het feest is gisteravond beeindigt.",
        "Het feest is gisteravond beëindigd.",
        "Het feest is gisteravond beëindigt."
      ],
      antwoord: 1,
      uitleg: "Het werkwoord is <i>beëindigen</i>. Stam-basis min -en eindigt op g. De g zit niet in 't kofschip, dus eindigt op d. Geen 'ge-' aan het begin want het begint met be-: <b>beëindigd</b>."
    }
  ]
});
