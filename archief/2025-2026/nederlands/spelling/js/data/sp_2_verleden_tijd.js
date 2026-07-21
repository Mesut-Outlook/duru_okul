DURU.register({
  id: "sp-2",
  hoofdstuk: 1,
  paragraaf: "1.2",
  titel: "Verleden tijd (vt)",
  korteUitleg: "Zwakke werkwoorden met 't kofschip en sterke onregelmatige werkwoorden.",
  icoon: "📜",
  theorie: `
    <h3>Verleden tijd (vt)</h3>
    <p>In de verleden tijd maken we onderscheid tussen <b>zwakke werkwoorden</b> (veranderen niet van klank) en <b>sterke werkwoorden</b> (veranderen wel van klank).</p>

    <h3>1. Zwakke werkwoorden: het kofschip-trucje</h3>
    <p>Om te weten of een zwak werkwoord in de verleden tijd op <b>-te(n)</b> of op <b>-de(n)</b> eindigt, gebruiken we <b>'t kofschip</b> (medeklinkers: <b>t, k, f, s, ch, p</b>):</p>

    <ol>
      <li>Neem het hele werkwoord (bijv. <i>maken</i>).</li>
      <li>Haal er <b>-en</b> af om de stam-basis te vinden &rarr; <i>mak-</i>.</li>
      <li>Kijk naar de laatste letter van deze stam-basis: de <b>k</b>.</li>
      <li>Zit de <b>k</b> in <b>'t ko<b>f</b>s<b>ch</b>i<b>p</b></b>? <b>Ja!</b> &rarr; Uitgang is <b>-te</b> (enkelvoud) of <b>-ten</b> (meervoud).</li>
      <li>Zit de letter er <b>niet</b> in? &rarr; Uitgang is <b>-de</b> of <b>-den</b>.</li>
    </ol>

    <div class="voorbeeld">
      <div class="vb-kop">📐 Voorbeeld: maken & vinden</div>
      <div class="stap"><b>maken</b> &rarr; stam-basis <i>mak-</i> (k zit in 't kofschip) &rarr; ik/hij <b>maakte</b>, wij <b>maakten</b></div>
      <div class="stap"><b>branden</b> &rarr; stam-basis <i>brand-</i> (d zit NIET in 't kofschip) &rarr; ik/hij <b>brandde</b>, wij <b>brandden</b></div>
    </div>

    <div class="info-box let-op">
      <span class="kop">⚠️ Let op bij v/z-werkwoorden!</span>
      <p>Kijk altijd naar de letter van het hele werkwoord min <b>-en</b>, NIET naar de ik-vorm!</p>
      <p><i>Bijvoorbeeld:</i> <b>reizen</b>. Haal -en eraf &rarr; stam-basis eindigt op <b>z</b>. De <b>z</b> zit niet in 't kofschip, dus: ik <b>reisde</b> (en niet reisde met -te, ook al is de ik-vorm 'ik reis').</p>
      <p><i>Bijvoorbeeld:</i> <b>leven</b>. Haal -en eraf &rarr; stam-basis eindigt op <b>v</b>. De <b>v</b> zit niet in 't kofschip, dus: ik <b>leefde</b>.</p>
    </div>

    <h3>2. Sterke & onregelmatige werkwoorden</h3>
    <p>Sterke werkwoorden veranderen van klank in de verleden tijd. Je moet deze vormen uit je hoofd leren!</p>

    <div class="voorbeeld">
      <div class="vb-kop">📐 Voorbeelden uit je aantekeningen</div>
      <div class="stap"><b>zien</b> &rarr; ik/hij <b>zag</b>, wij <b>zagen</b></div>
      <div class="stap"><b>lopen</b> &rarr; ik/hij <b>liep</b>, wij <b>liepen</b></div>
      <div class="stap"><b>kopen</b> &rarr; ik/hij <b>kocht</b>, wij <b>kochten</b></div>
      <div class="stap"><b>vinden</b> &rarr; ik/hij <b>vond</b>, wij <b>vonden</b></div>
    </div>
  `,
  vragen: [
    {
      type: "mc", niveau: 1,
      vraag: "Welke medeklinkers zitten er in de hulpregels van <b>'t kofschip</b>?",
      opties: ["t, k, f, s, ch, p", "t, g, f, s, ch, b", "d, k, f, s, j, p", "t, k, f, l, ch, p"],
      antwoord: 0,
      uitleg: "De medeklinkers in 't kofschip zijn <b>t, k, f, s, ch, p</b> (de klinkers o, i en e tellen niet mee).",
      hint: "Spel het woord 'kofschip' en haal de klinkers (o, i) weg."
    },
    {
      type: "waaronwaar", niveau: 1,
      vraag: "De verleden tijd van <b>kopen</b> is <i>koopte</i>.",
      antwoord: false,
      uitleg: "Onwaar: <i>kopen</i> is een onregelmatig werkwoord. De verleden tijd is <b>kocht</b> (enkelvoud) of <b>kochten</b> (meervoud).",
      hint: "Denk aan de aantekeningen: kopen &rarr; kocht."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (verleden tijd): 'Gisteren ___ (fietsen) wij naar school.'",
      antwoord: "fietsten",
      uitleg: "De stam-basis van <i>fietsen</i> is <i>fiets-</i> (eindigt op <b>s</b>). De s zit in 't kofschip, en het onderwerp is 'wij' (meervoud), dus: fiets + ten = <b>fietsten</b>.",
      hint: "Let op: het is verleden tijd én meervoud (wij)!"
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (verleden tijd): 'Duru ___ (maken) vorige week haar huiswerk af.'",
      antwoord: "maakte",
      uitleg: "De stam-basis van <i>maken</i> is <i>mak-</i> (eindigt op <b>k</b>). De k zit in 't kofschip. Onderwerp is Duru (enkelvoud), dus: maak + te = <b>maakte</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (verleden tijd): 'Ik ___ (vinden) gisteren mijn sleutel terug.'",
      antwoord: "vond",
      uitleg: "<i>Vinden</i> is een sterk werkwoord. De verleden tijd is <b>vond</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (verleden tijd): 'De brandweer ___ (redden) de kat uit de boom.'",
      antwoord: "redde",
      uitleg: "De stam-basis van <i>redden</i> is <i>red-</i> (eindigt op <b>d</b>). De d zit niet in 't kofschip. Onderwerp is de brandweer (enkelvoud), dus red + de = <b>redde</b>.",
      hint: "red + de = redde. Je schrijft dubbel-d!"
    },
    {
      type: "mc", niveau: 2,
      vraag: "Wat is de verleden tijd van <b>reizen</b> in de zin:<br>'Wij ___ vorig jaar naar Spanje.'?",
      opties: ["reisten", "reisden", "reizden", "reizten"],
      antwoord: 1,
      uitleg: "Het hele werkwoord is <i>reizen</i>. Min -en krijgen we <i>reiz-</i>. De <b>z</b> zit niet in 't kofschip. Dus we voegen -den toe: reis + den = <b>reisden</b>.",
      hint: "Kijk naar de z van reizen. Zit de z in 't kofschip?"
    },
    {
      type: "waaronwaar", niveau: 2,
      vraag: "De verleden tijd van <b>lopen</b> is <i>loopte</i>.",
      antwoord: false,
      uitleg: "Onwaar: lopen is een sterk werkwoord. De verleden tijd is <b>liep</b> (of liepen)."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (verleden tijd): 'Hij ___ (antwoorden) niet op mijn bericht.'",
      antwoord: "antwoordde",
      uitleg: "Zwak werkwoord: de stam-basis van <i>antwoorden</i> is <i>antwoord-</i> (eindigt op <b>d</b>). De d zit niet in 't kofschip. Dus: antwoord + de = <b>antwoordde</b> (met dubbel-d).",
      hint: "Zwak werkwoord dat eindigt op -d krijgt -de erachter."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Vul de juiste vorm in (verleden tijd meervoud): 'De leerlingen ___ (verhuizen) naar een ander lokaal.'",
      antwoord: "verhuisden",
      uitleg: "Hele werkwoord: <i>verhuizen</i>. Stam-basis min -en eindigt op <b>z</b>. De z zit niet in 't kofschip. Meervoud krijgt dus -den: verhuis + den = <b>verhuisden</b>.",
      hint: "Denk aan de z in verhuizen."
    },
    {
      type: "mc", niveau: 3,
      vraag: "Welke zin is correct gespeld in de verleden tijd?",
      opties: [
        "De leraar vertelde een spannend verhaal.",
        "De leraar verteldede een spannend verhaal.",
        "De leraar vertelte een spannend verhaal."
      ],
      antwoord: 0,
      uitleg: "Hele werkwoord is <i>vertellen</i>. De stam-basis eindigt op <b>l</b>. De l zit niet in 't kofschip, dus stam + de: vertel + de = <b>vertelde</b>."
    },
    {
      type: "waaronwaar", niveau: 3,
      vraag: "De verleden tijd van <b>verven</b> (meervoud) is <i>verfden</i>.",
      antwoord: true,
      uitleg: "Waar! Hele werkwoord is <i>verven</i>. Stam-basis min -en eindigt op <b>v</b>. De v zit niet in 't kofschip, dus we voegen -den toe: verf + den = <b>verfden</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de verleden tijd in: 'Wij ___ (zien) gisteren een mooie vogel.'",
      antwoord: "zagen",
      uitleg: "<i>Zien</i> is een sterk werkwoord. De verleden tijd meervoud is <b>zagen</b>."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Vul de verleden tijd in: 'De dief ___ (vluchten) door het raam.'",
      antwoord: "vluchtte",
      uitleg: "Zwak werkwoord: de stam-basis van <i>vluchten</i> is <i>vlucht-</i> (eindigt op <b>t</b>). De t zit in 't kofschip, dus we voegen -te toe: vlucht + te = <b>vluchtte</b> (met dubbel-t).",
      hint: "Zit de t in 't kofschip? Ja, dus stam + te."
    },
    {
      type: "mc", niveau: 3,
      vraag: "Welke zin is correct gespeld?",
      opties: [
        "Zij wedden vorig jaar dat het zou gaan regenen.",
        "Zij weddenen vorig jaar dat het zou gaan regenen.",
        "Zij wedten vorig jaar dat het zou gaan regenen."
      ],
      antwoord: 0,
      uitleg: "Het werkwoord is <i>wedden</i>. De verleden tijd meervoud is wed + den = <b>wedden</b>. Het ziet er hetzelfde uit als de tegenwoordige tijd meervoud!"
    }
  ]
});
