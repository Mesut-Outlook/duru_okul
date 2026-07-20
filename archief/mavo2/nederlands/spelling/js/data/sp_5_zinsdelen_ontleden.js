DURU.register({
  id: "sp-5",
  hoofdstuk: 2,
  paragraaf: "2.2",
  titel: "Zinsdelen ontleden",
  korteUitleg: "Leer zinsdelen benoemen: persoonsvorm, onderwerp, gezegde, lijdend en meewerkend voorwerp.",
  icoon: "🧠",
  theorie: `
    <h3>Grammatica — Zinsdelen ontleden</h3>
    <p>Als je een zin gaat ontleden, verdeel je de zin in stukjes (zinsdelen) en geef je ze een naam. Gebruik daarvoor de handige <b>trucjes</b> uit je aantekeningen!</p>

    <h3>De 5 belangrijkste zinsdelen</h3>

    <ul>
      <li><b>Persoonsvorm (Pv)</b> &rarr; Het werkwoord dat verandert als je de zin in een andere tijd zet (tegenwoordige tijd &harr; verleden tijd).
        <br><i>Trucje:</i> Maak een ja/nee-vraag van de zin. De Pv staat dan vooraan!
      </li>
      <li><b>Onderwerp (Ow)</b> &rarr; Wie of wat doet het?
        <br><i>Vraag:</i> <b>Wie of wat + persoonsvorm (Pv)?</b>
      </li>
      <li><b>Werkwoordelijk gezegde (Wg)</b> &rarr; Alle werkwoorden in de zin.
      </li>
      <li><b>Lijdend voorwerp (Lv)</b> &rarr; Wie of wat ondergaat de handeling?
        <br><i>Vraag:</i> <b>Wat of wie + onderwerp (Ow) + werkwoordelijk gezegde (Wg)?</b>
      </li>
      <li><b>Meewerkend voorwerp (Mv)</b> &rarr; Aan wie of voor wie?
        <br><i>Vraag:</i> <b>Aan wie / voor wie + Ow + Wg + Lv?</b>
        <br><i>Trucje:</i> Je kunt er vaak 'aan' of 'voor' voor zetten of weglaten.
      </li>
    </ul>

    <div class="voorbeeld">
      <div class="vb-kop">📐 Uitgewerkt voorbeeld</div>
      <div class="stap"><b>Zin:</b> De jongen geeft het meisje een boek.</div>
      <div class="stap"><b>Stap 1 (Pv):</b> Zet in verleden tijd: 'De jongen <i>gaf</i>...' &rarr; Pv = <b>geeft</b>.</div>
      <div class="stap"><b>Stap 2 (Ow):</b> Wie geeft? &rarr; Ow = <b>De jongen</b>.</div>
      <div class="stap"><b>Stap 3 (Wg):</b> Alle werkwoorden &rarr; Wg = <b>geeft</b>.</div>
      <div class="stap"><b>Stap 4 (Lv):</b> Wat geeft de jongen? &rarr; Lv = <b>een boek</b>.</div>
      <div class="stap"><b>Stap 5 (Mv):</b> Aan wie geeft de jongen een boek? &rarr; Mv = <b>het meisje</b> (aan het meisje).</div>
    </div>

    <div class="info-box tip">
      <span class="kop">💡 Vaste volgorde bij ontleden</span>
      <p>Ontleed altijd in deze volgorde om fouten te voorkomen: <b>Pv &rarr; Wg &rarr; Ow &rarr; Lv &rarr; Mv</b>.</p>
    </div>
  `,
  vragen: [
    {
      type: "mc", niveau: 1,
      vraag: "Hoe vind je de <b>persoonsvorm (Pv)</b> van een zin?",
      opties: [
        "Door te vragen: 'Wie of wat + Pv?'",
        "Door de zin in een andere tijd te zetten of er een vraagzin van te maken.",
        "Door te zoeken naar alle zelfstandige naamwoorden.",
        "Door te vragen: 'Aan wie of voor wie?'"
      ],
      antwoord: 1,
      uitleg: "De persoonsvorm is het werkwoord dat verandert van tijd. Ook komt de Pv vooraan te staan als je er een ja/nee-vraag van maakt.",
      hint: "Denk aan het trucje uit je aantekeningen: 'Pv &rarr; ww dat verandert bij tijd'."
    },
    {
      type: "waaronwaar", niveau: 1,
      vraag: "In de zin 'Duru leest een spannend boek.' is <b>Duru</b> het onderwerp (Ow).",
      antwoord: true,
      uitleg: "Ja! Vraag: Wie leest? Antwoord: <b>Duru</b>. Dus Duru is het onderwerp."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Wat is de <b>persoonsvorm (Pv)</b> in de volgende zin?<br>'Mijn broer heeft gisteravond een film gekeken.'",
      antwoord: "heeft",
      uitleg: "Als we de zin in een andere tijd zetten: 'Mijn broer <b>had</b> een film gekeken.', verandert <i>heeft</i> in <i>had</i>. Dus <b>heeft</b> is de persoonsvorm.",
      hint: "Verander de tijd van de zin (verleden tijd)."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Wat is het <b>werkwoordelijk gezegde (Wg)</b> in de zin?<br>'Mijn broer heeft gisteravond een film gekeken.' (Scheid de werkwoorden met een spatie)",
      antwoord: "heeft gekeken",
      uitleg: "Het werkwoordelijk gezegde bestaat uit alle werkwoorden in de zin: <b>heeft gekeken</b>.",
      hint: "Zoek naar alle werkwoorden."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Wat is het <b>onderwerp (Ow)</b> in de zin?<br>'De grote hond blaft naar de postbode.'",
      antwoord: "De grote hond",
      uitleg: "De persoonsvorm is <i>blaft</i>. Vraag: Wie of wat blaft? Antwoord: <b>De grote hond</b>.",
      hint: "Neem het hele zinsdeel mee, niet alleen 'hond'."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Wat is het <b>lijdend voorwerp (Lv)</b> in de zin?<br>'Duru maakt haar wiskundesommen.'",
      antwoord: "haar wiskundesommen",
      uitleg: "Pv/Wg = <i>maakt</i>, Ow = <i>Duru</i>. Vraag: Wat maakt Duru? Antwoord: <b>haar wiskundesommen</b>.",
      hint: "Wat + onderwerp + gezegde?"
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Wat is het <b>meewerkend voorwerp (Mv)</b> in de zin?<br>'De opa geeft zijn kleindochter een cadeautje.'",
      antwoord: "zijn kleindochter",
      uitleg: "Vraag: Aan wie geeft opa een cadeautje? Antwoord: (aan) <b>zijn kleindochter</b>. Dus <i>zijn kleindochter</i> is het meewerkend voorwerp.",
      hint: "Vraag: Aan/voor wie + Ow + Wg + Lv?"
    },
    {
      type: "waaronwaar", niveau: 2,
      vraag: "In de zin 'Ik stuurde hem een bericht.' is <b>hem</b> het lijdend voorwerp (Lv).",
      antwoord: false,
      uitleg: "Onwaar: <i>een bericht</i> is het lijdend voorwerp (Wat stuurde ik?). <i>Hem</i> is het meewerkend voorwerp (Aan wie stuurde ik het?)."
    },
    {
      type: "mc", niveau: 2,
      vraag: "Wat is het <b>lijdend voorwerp (Lv)</b> in de zin:<br>'De leraar legt de moeilijke som uit aan de leerlingen.'?",
      opties: ["de leraar", "de moeilijke som", "de leerlingen", "legt uit"],
      antwoord: 1,
      uitleg: "Vraag: Wat legt de leraar uit? Antwoord: <b>de moeilijke som</b>.",
      hint: "Het lijdend voorwerp ondergaat de handeling."
    },
    {
      type: "waaronwaar", niveau: 1,
      vraag: "Het <b>meewerkend voorwerp (Mv)</b> geeft antwoord op de vraag: 'Aan wie?' of 'Voor wie?'",
      antwoord: true,
      uitleg: "Ja, dit klopt helemaal! 'Mv &rarr; aan wie/voor wie'."
    },
    {
      type: "invoer", niveau: 2,
      vraag: "Wat is de <b>persoonsvorm (Pv)</b> in de zin?<br>'Morgen gaan we met de hele klas naar de dierentuin.'",
      antwoord: "gaan",
      uitleg: "Als we de zin in een andere tijd zetten: 'Morgen <b>gingen</b> we...', verandert <i>gaan</i> in <i>gingen</i>. Dus <b>gaan</b> is de persoonsvorm.",
      hint: "Maak er een vraagzin van: 'Gaan we morgen...?'"
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Wat is het <b>meewerkend voorwerp (Mv)</b> in de zin?<br>'Duru schenkt haar moeder een kopje thee in.'",
      antwoord: "haar moeder",
      uitleg: "Vraag: Voor wie schenkt Duru een kopje thee in? Antwoord: (voor) <b>haar moeder</b>.",
      hint: "Voor wie doet Duru dit?"
    },
    {
      type: "mc", niveau: 3,
      vraag: "Welk zinsdeel is <b>de taart</b> in de zin:<br>'De bakker bakt een heerlijke taart voor de klant.'?",
      opties: [
        "Onderwerp (Ow)",
        "Lijdend voorwerp (Lv)",
        "Meewerkend voorwerp (Mv)",
        "Werkwoordelijk gezegde (Wg)"
      ],
      antwoord: 1,
      uitleg: "Vraag: Wat bakt de bakker? Antwoord: een heerlijke taart. Dus het is het <b>lijdend voorwerp (Lv)</b>. (Let op: 'voor de klant' is het meewerkend voorwerp!)",
      hint: "Stel de wat-vraag."
    },
    {
      type: "waaronwaar", niveau: 3,
      vraag: "In de zin 'Zij heeft haar broertje geholpen.' is <b>haar broertje</b> het meewerkend voorwerp (Mv).",
      antwoord: false,
      uitleg: "Onwaar: <i>helpen</i> krijgt een lijdend voorwerp. Vraag: Wie heeft zij geholpen? Antwoord: <b>haar broertje</b> (lijdend voorwerp)."
    },
    {
      type: "invoer", niveau: 3,
      vraag: "Wat is het <b>onderwerp (Ow)</b> in de zin?<br>'Op de zolder liggen nog oude boeken van opa.'",
      antwoord: "oude boeken van opa|oude boeken",
      uitleg: "Pv is <i>liggen</i>. Vraag: Wie of wat liggen op de zolder? Antwoord: <b>oude boeken van opa</b>."
    }
  ]
});
