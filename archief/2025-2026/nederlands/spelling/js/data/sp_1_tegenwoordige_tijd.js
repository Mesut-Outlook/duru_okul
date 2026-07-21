DURU.register({
  id: "sp-1",
  hoofdstuk: 1,
  paragraaf: "1.1",
  titel: "Tegenwoordige tijd (tt)",
  korteUitleg: "Regels voor de tegenwoordige tijd: stam, stam+t en het hele werkwoord.",
  icoon: "⏳",
  theorie: `
    <h3>Tegenwoordige tijd (tt)</h3>
    <p>De tegenwoordige tijd is de tijd van <b>nu</b>. De basisregel voor de spelling in de tegenwoordige tijd is heel eenvoudig:</p>

    <ul>
      <li><b>Ik</b> &rarr; <b>stam</b> (de kortste vorm van het werkwoord)</li>
      <li><b>Hij / zij / het / u</b> &rarr; <b>stam + t</b></li>
      <li><b>Wij / jullie / zij (meervoud)</b> &rarr; <b>hele werkwoord</b></li>
    </ul>

    <div class="voorbeeld">
      <div class="vb-kop">📐 Voorbeeld: werken</div>
      <div class="stap"><b>Ik:</b> ik werk (stam)</div>
      <div class="stap"><b>Hij/zij/het:</b> hij werk<b>t</b> (stam + t)</div>
      <div class="stap"><b>Wij/jullie/zij:</b> wij werken (hele werkwoord)</div>
    </div>

    <h3>⚠️ Let op bij d/t-werkwoorden</h3>
    <p>Bij werkwoorden waarvan de stam op een <b>d</b> eindigt (zoals <i>worden</i> of <i>vinden</i>), hoor je de <b>t</b> niet, maar je schrijft hem wel bij de hij-vorm!</p>

    <div class="voorbeeld">
      <div class="vb-kop">📐 Voorbeeld: vinden & worden</div>
      <div class="stap"><b>Ik:</b> ik vin<b>d</b> / ik wor<b>d</b> (stam)</div>
      <div class="stap"><b>Hij/zij/het:</b> hij vin<b>dt</b> / hij wor<b>dt</b> (stam + <b>t</b>)</div>
      <div class="stap"><b>Wij:</b> wij vinden / wij worden (hele werkwoord)</div>
    </div>

    <div class="info-box let-op">
      <span class="kop">⚠️ Uitzondering bij je/jij</span>
      <p>Als <b>je</b> of <b>jij</b> <i>achter</i> de persoonsvorm staat, schrijf je <b>geen t</b>!</p>
      <p><i>Voorbeeld:</i> Word <b>jij</b> morgen veertien jaar? (Geen t!)</p>
      <p><i>Voorbeeld:</i> Jij word<b>t</b> morgen veertien jaar. (Wel een t, want jij staat ervoor!)</p>
    </div>

    <div class="info-box tip">
      <span class="kop">💡 Smurfen-truc</span>
      <p>Twijfel je of er een <b>t</b> achter moet? Vervang het werkwoord door <b>smurfen</b> of <b>lopen</b>. Hoor je een t? Dan schrijf je ook een t!</p>
      <p><i>Zin:</i> Hij vindt/vind? &rarr; Hij loop<b>t</b>. Je hoort een <b>t</b>, dus: hij vin<b>dt</b>.</p>
      <p><i>Zin:</i> Vind/Vindt jij? &rarr; Loop jij? Je hoort <b>geen t</b>, dus: Vin<b>d</b> jij.</p>
    </div>
  `,
  vragen: [
    {
      type: "mc", niveau: 1,
      vraag: "Wat is de stam van het werkwoord <b>worden</b>?",
      opties: ["wordt", "word", "worden", "worgt"],
      antwoord: 1,
      uitleg: "De stam is de kortste vorm van het werkwoord (ik-vorm). Voor <i>worden</i> is dat <b>word</b>.",
      hint: "De stam vind je door van het hele werkwoord -en af te halen: word(en)."
    },
    {
      type: "waaronwaar", niveau: 1,
      vraag: "In de zin 'Duru loop<b>t</b> in de tuin' is het werkwoord juist gespeld.",
      antwoord: true,
      uitleg: "Ja! Het onderwerp is Duru (zij), dus we gebruiken: stam + t. De stam van lopen is <i>loop</i>, plus t &rarr; <i>loopt</i>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (tegenwoordige tijd): 'Ik ___ (vinden) dat een heel goed idee.'",
      antwoord: "vind",
      uitleg: "Het onderwerp is 'ik', dus we schrijven alleen de stam: <b>vind</b>.",
      hint: "Haal -en van vinden af."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (tegenwoordige tijd): 'Zij ___ (vinden) Nederlands een leuk vak.' (enkelvoud)",
      antwoord: "vindt",
      uitleg: "Het onderwerp is 'zij' (enkelvoud), dus we schrijven stam + t: vind + t = <b>vindt</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (tegenwoordige tijd): 'Duru ___ (worden) deze week veertien jaar.'",
      antwoord: "wordt",
      uitleg: "Duru is 'zij' (enkelvoud), dus we gebruiken stam + t: word + t = <b>wordt</b>."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Vul de juiste vorm in (tegenwoordige tijd): '___ (worden) jij morgen ook getest?'",
      antwoord: "word",
      uitleg: "Het onderwerp 'jij' staat <i>achter</i> het werkwoord. Dan schrijven we alleen de stam, dus <b>geen t</b>: <b>word</b>.",
      hint: "Denk aan de smurfen-truc: 'Smurf jij morgen ook?' (Je hoort geen t)."
    },
    {
      type: "mc", niveau: 1,
      vraag: "Welke zin is correct gespeld?",
      opties: [
        "Wat gebeurt er vandaag?",
        "Wat gebeurd er vandaag?",
        "Wat gebeurdt er vandaag?"
      ],
      antwoord: 0,
      uitleg: "Het is tegenwoordige tijd (gebeuren). Het onderwerp is 'wat' (enkelvoud), dus stam + t: gebeur + t = <b>gebeurt</b>.",
      hint: "Vervang gebeuren door lopen: 'Wat loopt er vandaag?' (Je hoort een t)."
    },
    {
      type: "waaronwaar", niveau: 2,
      vraag: "De zin 'Jij wordt morgen opgehaald.' is goed gespeld.",
      antwoord: true,
      uitleg: "Het onderwerp 'jij' staat <i>voor</i> de persoonsvorm, dus schrijven we stam + t: word + t = <b>wordt</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (tegenwoordige tijd): 'De leraar ___ (antwoorden) op mijn vraag.'",
      antwoord: "antwoordt",
      uitleg: "De leraar is 'hij', dus stam + t: antwoord + t = <b>antwoordt</b>.",
      hint: "De stam van antwoorden eindigt al op een d."
    },
    {
      type: "mc", niveau: 2,
      vraag: "Wat is de juiste spelling in deze zin?<br>'Waarom ___ (verhuizen) jullie naar Utrecht?'",
      opties: ["verhuisdt", "verhuizen", "verhuist", "verhuisen"],
      antwoord: 1,
      uitleg: "Het onderwerp is 'jullie' (meervoud), dus we gebruiken het hele werkwoord: <b>verhuizen</b>.",
      hint: "Kijk goed naar het onderwerp van de zin."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Vul de juiste vorm in (tegenwoordige tijd): 'Dat ___ (betekenen) dat we klaar zijn.'",
      antwoord: "betekent",
      uitleg: "Het onderwerp is 'dat' (enkelvoud), dus stam + t: beteken + t = <b>betekent</b>."
    },
    {
      type: "waaronwaar", niveau: 2,
      vraag: "In de zin 'Meld je nu aan!' is het werkwoord juist gespeld.",
      antwoord: true,
      uitleg: "Dit is een gebiedende wijs (of met 'je' achter de persoonsvorm). We gebruiken hier alleen de stam: <b>meld</b>."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Vul de juiste vorm in (tegenwoordige tijd): 'De hond ___ (bijten) in het speeltje.'",
      antwoord: "bijt",
      uitleg: "De hond is 'hij/het', dus stam + t. De stam van bijten is <i>bijt</i>. Omdat de stam al op een -t eindigt, voegen we geen extra t toe: <b>bijt</b>."
    },
    {
      type: "mc", niveau: 3,
      vraag: "Welke zin is correct gespeld?",
      opties: [
        "Jij red het wel alleen.",
        "Jij redt het wel alleen.",
        "Jij red dt het wel alleen."
      ],
      antwoord: 1,
      uitleg: "Het onderwerp 'jij' staat voor het werkwoord (redden), dus stam + t: red + t = <b>redt</b>.",
      hint: "Zet lopen in de plaats: 'Jij loopt het wel.'"
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Vul de juiste vorm in (tegenwoordige tijd): '___ (melden) hij zich morgen aan?'",
      antwoord: "meldt",
      uitleg: "Het onderwerp is 'hij'. Ook als 'hij' erachter staat, schrijf je gewoon stam + t: meld + t = <b>meldt</b>. Alleen bij 'je/jij' vervalt de t!",
      hint: "Vergelijk met lopen: 'Loopt hij zich morgen aan?' (Je hoort een t, dus wel een t schrijven)."
    }
  ]
});
