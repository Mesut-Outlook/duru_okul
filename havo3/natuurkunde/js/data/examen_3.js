/* Proeftoets 3 — Natuurkunde HAVO 3: Hoofdstuk 1 (Kracht en beweging - Deel 3)
   Focus: Paragraaf 1.4 — Veiligheid in het verkeer, reactietijd, remweg en stopafstand.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-3",
  titel: "Toets 3 — Verkeersveiligheid, Remweg & Stopafstand",
  vak: "Natuurkunde · HAVO 3 (H1)",
  icoon: "🚗",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de juiste formule voor de totale <b>stopafstand (s_stop)</b>?",
      opties: [
        "s_stop = s_reactie + s_rem",
        "s_stop = s_reactie × s_rem",
        "s_stop = s_rem - s_reactie",
        "s_stop = (s_reactie + s_rem) / 2"
      ],
      antwoord: 0,
      uitleg: "De totale stopafstand is de som van de reactieafstand (afstand afgelegd tijdens reactietijd) en de remweg (afstand afgelegd tijdens het remmen): s_stop = s_reactie + s_rem."
    },
    {
      type: "mc",
      vraag: "Tijdens de <b>reactietijd</b> rijdt een automobilist met constante snelheid door. Welke bewegingssoort is dit?",
      opties: [
        "Eenparig vertraagde beweging",
        "Eenparige beweging (constante snelheid)",
        "Eenparig versnelde beweging",
        "Niet-eenparige vertraging"
      ],
      antwoord: 1,
      uitleg: "Voordat de bestuurder het rempedaal indrukt, reageert hij alleen; de auto remt nog niet en behoudt zijn constante snelheid (eenparige beweging)."
    },
    {
      type: "invul",
      vraag: "Een auto rijdt met <b>72 km/h</b> (20 m/s). De bestuurder heeft een reactietijd van <b>0,8 s</b>. Bereken de reactieafstand in meters.",
      antwoord: "16|16 m|16,0|16,0 m",
      uitleg: "s_reactie = v × t_reactie = 20 m/s × 0,8 s = 16 meter."
    },
    {
      type: "mc",
      vraag: "Als de beginsnelheid van een auto <b>2 keer zo groot</b> wordt, wat gebeurt er dan met de <b>remweg</b> (bij gelijke remkracht en wegdek)?",
      opties: [
        "De remweg wordt 2 keer zo lang",
        "De remweg blijft hetzelfde",
        "De remweg wordt 4 keer zo lang (2²)",
        "De remweg wordt 8 keer zo lang"
      ],
      antwoord: 2,
      uitleg: "De remweg is evenredig met het kwadraat van de beginsnelheid (s_rem ~ v²). Bij 2× zo hoge snelheid wordt de remweg 2² = 4 keer zo lang!"
    },
    {
      type: "waaronwaar",
      vraag: "Het gebruik van een mobiele telefoon tijdens het rijden vergroot de <b>remweg</b> van de auto direct.",
      antwoord: false,
      uitleg: "Niet waar. Afleiding door een telefoon vergroot de <b>reactietijd</b> (en dus de reactieafstand). De mechanische remweg van de auto zelf verandert niet, maar de totale stopafstand wordt wel veel groter."
    },
    {
      type: "invul",
      vraag: "Een auto rijdt met 15 m/s en remt in 3,0 seconden gelijkmatig af tot stilstand. Bereken de remweg (s_rem) in meters via de formule s = 0,5 × v × t.",
      antwoord: "22,5|22,5 m",
      uitleg: "s_rem = 0,5 × v × t_rem = 0,5 × 15 m/s × 3,0 s = 22,5 meter."
    },
    {
      type: "mc",
      vraag: "Welke factor heeft <b>geen</b> invloed op de lengte van de mechanische remweg?",
      opties: [
        "Het profiel van de autobanden",
        "Gladheid van het wegdek door regen of ijzel",
        "De kwaliteit van de remmen",
        "De alcoholconsumptie van de bestuurder"
      ],
      antwoord: 3,
      uitleg: "Alcohol beïnvloedt de hersenen en verhoogt de reactietijd van de bestuurder, maar heeft geen effect op de mechanische remweg van de auto."
    },
    {
      type: "invul",
      vraag: "Een automobilist rijdt op een natte weg. Zijn reactieafstand is 14 meter en zijn remweg is 28 meter. Wat is zijn totale stopafstand in meters?",
      antwoord: "42|42 m",
      uitleg: "s_stop = s_reactie + s_rem = 14 m + 28 m = 42 meter."
    },
    {
      type: "mc",
      vraag: "Wat is het natuurkundige doel van een <b>kreukelzone</b> bij een autobotsing?",
      opties: [
        "De botsingstijd (remtijd) vergroten waardoor de botskracht kleiner wordt",
        "De massa van de auto vergroten",
        "De snelheid van de auto voor de botsing verlagen",
        "De auto zo stijf en onbuigzaam mogelijk maken"
      ],
      antwoord: 0,
      uitleg: "Door in te deuken verlengt de kreukelzone de botstijd (Δt). Volgens a = Δv / Δt wordt de vertraging kleiner en daardoor is de botskracht F = m × a op de inzittenden veel kleiner."
    },
    {
      type: "waaronwaar",
      vraag: "Een veiligheidsgordel rekt tijdens een zware botsing een klein beetje mee om de remtijd van het lichaam te verlengen.",
      antwoord: true,
      uitleg: "Waar. Door het gecontroleerde meerekken wordt de remtijd van het lichaam verlengd en de piekkracht op het lichaam verlaagd."
    },
    {
      type: "mc",
      vraag: "Waarom loopt een <b>airbag</b> direct na het opblazen weer snel leeg via kleine openingen?",
      opties: [
        "Omdat de lucht te warm wordt",
        "Om ruimte te maken voor de hulpdiensten en te voorkomen dat de bestuurder terugkaatst of stikt",
        "Om de auto sneller tot stilstand te brengen",
        "Omdat het gas giftig is voor het stuur"
      ],
      antwoord: 1,
      uitleg: "Het gecontroleerd leeglopen dempt de klap zachtjes (absorbeert energie), voorkomt dat het hoofd hard terugveert, en zorgt dat de bestuurder niet klem komt te zitten."
    },
    {
      type: "invul",
      vraag: "Een bromfiets rijdt met 45 km/h (12,5 m/s). De remvertraging is 5,0 m/s². Hoeveel seconden duurt het remmen tot stilstand?",
      antwoord: "2,5|2,5 s|2,5 sec",
      uitleg: "t_rem = v / a = 12,5 m/s / 5,0 m/s² = 2,5 seconden."
    },
    {
      type: "mc",
      vraag: "Een auto heeft bij 50 km/h een remweg van 12 meter. Wat is de remweg van dezelfde auto op hetzelfde wegdek als de snelheid 100 km/h is?",
      opties: [
        "24 meter",
        "36 meter",
        "48 meter",
        "60 meter"
      ],
      antwoord: 2,
      uitleg: "100 km/h is 2× zo snel als 50 km/h. De remweg wordt 2² = 4 keer zo lang: 12 m × 4 = 48 meter."
    },
    {
      type: "waaronwaar",
      vraag: "Op een spiegelglad wegdek (ijzel) is de maximale remkracht veel kleiner, waardoor de remvertraging daalt en de remweg veel langer wordt.",
      antwoord: true,
      uitleg: "Waar. Weinig grip betekent minder remkracht tussen band en wegdek, dus een lagere vertraging a en een veel langere remweg."
    },
    {
      type: "invul",
      vraag: "Een fietser heeft bij 20 km/h een stopafstand van 9,0 m (reactieafstand = 4,0 m, remweg = 5,0 m). Als hij zijn snelheid verdubbelt naar 40 km/h bij dezelfde reactietijd (0,72 s), wordt de reactieafstand 8,0 m en de remweg 20,0 m. Wat is dan de nieuwe totale stopafstand in meters?",
      antwoord: "28|28 m|28,0|28,0 m",
      uitleg: "s_stop = s_reactie + s_rem = 8,0 m + 20,0 m = 28 meter."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er in het (v,t)-diagram tijdens een noodstop?",
      opties: [
        "Eerst een dalende lijn, daarna een horizontale lijn",
        "Direct een verticale lijn naar beneden",
        "Een stijgende lijn gevolgd door een dalende lijn",
        "Eerst een horizontale lijn (reactiefase), daarna een steil dalende lijn naar de nul-as (remfase)"
      ],
      antwoord: 3,
      uitleg: "Tijdens de reactietijd blijft v constant (horizontaal). Zodra er geremd wordt, daalt v gelijkmatig naar 0 (dalende rechte lijn)."
    },
    {
      type: "waaronwaar",
      vraag: "Een fietshelm beschermt het hoofd doordat het piepschuim indeukt bij een val, waardoor de remweg van het hoofd iets groter en de botstijd langer wordt.",
      antwoord: true,
      uitleg: "Waar. Het samendrukken van het schuim verlengt de impacttijd en vermindert de piekversnelling op de hersenen."
    },
    {
      type: "invul",
      vraag: "Een scooterrijder rijdt met 10 m/s. Zijn reactietijd is 1,0 s en zijn remtijd is 2,0 s. Bereken de totale afstand die hij aflegt vanaf het zien van het gevaar tot stilstand (in meters).",
      antwoord: "20|20 m|20,0",
      uitleg: "s_reactie = 10 m/s × 1,0 s = 10 m. s_rem = 0,5 × 10 m/s × 2,0 s = 10 m. s_stop = 10 + 10 = 20 meter."
    },
    {
      type: "open",
      vraag: "Leg in je eigen woorden uit waarom in woonwijken een maximumsnelheid van 30 km/h veel veiliger is dan 50 km/h. Verwerk daarin het effect op de <b>stopafstand</b> en de <b>botssnelheid</b>.",
      sleutelwoorden: ["stopafstand korter/veel korter", "reactieafstand kleiner", "remweg kwadratisch/veel kleiner/kracht kleiner"],
      minTreffers: 2,
      modelantwoord: "Bij 30 km/h is zowel de reactieafstand als de remweg aanzienlijk korter dan bij 50 km/h (de remweg is bij 30 km/h minder dan de helft van die bij 50 km/h). De totale stopafstand is daardoor veel kleiner, waardoor een auto veel eerder stilstaat en een aanrijding vaker voorkomen kan worden, of de resterende botssnelheid veel lager is.",
      uitleg: "Lagere snelheid betekent kortere reactieafstand én een kwadratisch veel kortere remweg, waardoor de overlevingskans van voetgangers enorm toeneemt."
    },
    {
      type: "open",
      vraag: "Leg met behulp van de begrippen <b>vertraging</b> en <b>kracht</b> uit hoe een veiligheidsgordel voorkomt dat iemand door de voorruit vliegt.",
      sleutelwoorden: ["kracht uitoefent/tegenhoudt", "vertraagt/meevertraagt met de auto", "traagheid"],
      minTreffers: 2,
      modelantwoord: "Door traagheid wil het lichaam van de passagier met constante snelheid doorbewegen als de auto plots stopt. De veiligheidsgordel oefent een achterwaartse kracht uit op het lichaam, waardoor het lichaam samen met de auto gelijkmatig vertraagt en niet met hoge snelheid tegen het stuur of door de voorruit gelanceerd wordt.",
      uitleg: "De gordel levert de benodigde tegenkracht F om de massa m van de passagier af te remmen (F = m × a)."
    }
  ]
});
