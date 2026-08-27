/* Proeftoets 8 — Natuurkunde HAVO 3: Hoofdstuk 2 (Elektriciteit - Deel 3)
   Focus: Paragraaf 2.3 — Serie- en parallelschakelingen, vervangingsweerstand en huisinstallatie.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-8",
  titel: "Toets 8 — Serie- en Parallelschakelingen Berekenen",
  vak: "Natuurkunde · HAVO 3 (H2)",
  icoon: "🔌",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat geldt voor de <b>stroomsterkte</b> in een <b>serieschakeling</b> met drie weerstanden?",
      opties: [
        "De stroomsterkte is overal in de kring even groot: I_tot = I_1 = I_2 = I_3",
        "De stroomsterkte verdeelt zich over de drie weerstanden",
        "De eerste weerstand krijgt alle stroom, de laatste niets",
        "De stroomsterkte is gelijk aan de som van de spanningen"
      ],
      antwoord: 0,
      uitleg: "In een onvertakte serieschakeling is er maar één stroompad; de stroomsterkte is overal exact gelijk."
    },
    {
      type: "mc",
      vraag: "Wat geldt voor de <b>spanning</b> over de afzonderlijke takken in een <b>parallelschakeling</b>?",
      opties: [
        "De spanning verdeelt zich over de takken",
        "De spanning over elke tak is gelijk aan de bronspanning: U_tot = U_1 = U_2",
        "De spanning is nul in de verste tak",
        "De tak met de grootste weerstand krijgt de meeste spanning"
      ],
      antwoord: 1,
      uitleg: "In een parallelschakeling staat over elke parallelle tak direct de volledige bronspanning."
    },
    {
      type: "invul",
      vraag: "In een serieschakeling zijn twee weerstanden opgenomen: R_1 = 30 Ω en R_2 = 45 Ω. Bereken de totale vervangingsweerstand R_tot in Ohm.",
      antwoord: "75|75 Ω|75 ohm",
      uitleg: "In serie tellen weerstanden op: R_tot = R_1 + R_2 = 30 + 45 = 75 Ω."
    },
    {
      type: "invul",
      vraag: "Een serieschakeling van R_1 = 20 Ω en R_2 = 30 Ω is aangesloten op een spanningsbron van 10 V. Bereken de hoofdstroomsterkte I in Ampère.",
      antwoord: "0,2|0,2 A|0,20|0,20 A",
      uitleg: "R_tot = 20 + 30 = 50 Ω. I = U / R_tot = 10 V / 50 Ω = 0,2 A."
    },
    {
      type: "mc",
      vraag: "In de vorige vraag (U = 10 V, I = 0,2 A, R_1 = 20 Ω, R_2 = 30 Ω): hoeveel Volt is de deelspanning over R_1?",
      opties: ["2 V", "4 V", "6 V", "10 V"],
      antwoord: 1,
      uitleg: "U_1 = I × R_1 = 0,2 A × 20 Ω = 4 V (over R_2 staat 0,2 × 30 = 6 V; samen 4 + 6 = 10 V)."
    },
    {
      type: "waaronwaar",
      vraag: "In een huishouden zijn alle stopcontacten en lampen in <b>serie</b> geschakeld.",
      antwoord: false,
      uitleg: "Niet waar. Apparaten in huis zijn <b>parallel</b> geschakeld, zodat elk apparaat 230 V krijgt en onafhankelijk in- en uitgeschakeld kan worden."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er in een <b>serieschakeling</b> van kerstboomlampjes als één lampje doorbrandt?",
      opties: [
        "De andere lampjes gaan feller branden",
        "Alle lampjes gaan uit omdat de stroomkring onderbroken is",
        "Alleen dat ene lampje gaat uit, de rest blijft branden",
        "Er ontstaat kortsluiting"
      ],
      antwoord: 1,
      uitleg: "Bij serie onderbreekt één defect lampje de gehele stroomkring, waardoor alle lampjes doven."
    },
    {
      type: "invul",
      vraag: "Twee identieke weerstanden van elk 60 Ω staan parallel geschakeld. Wat is de totale vervangingsweerstand in Ohm?",
      antwoord: "30|30 Ω|30 ohm",
      uitleg: "Bij 2 gelijke parallelle weerstanden: R_tot = R / 2 = 60 / 2 = 30 Ω (of via 1/R = 1/60 + 1/60 = 2/60 -> R = 30 Ω)."
    },
    {
      type: "invul",
      vraag: "In een parallelschakeling loopt door tak 1 een stroom van 1,2 A en door tak 2 een stroom van 2,3 A. Hoeveel Ampère is de totale hoofdstroom die de spanningsbron levert?",
      antwoord: "3,5|3,5 A|3,50",
      uitleg: "I_tot = I_1 + I_2 = 1,2 A + 2,3 A = 3,5 A."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de totale vervangingsweerstand van een schakeling als je er een extra weerstand <b>parallel</b> aan toevoegt?",
      opties: [
        "De totale weerstand wordt groter",
        "De totale weerstand wordt kleiner",
        "De totale weerstand blijft exact gelijk",
        "De totale weerstand wordt oneindig groot"
      ],
      antwoord: 1,
      uitleg: "Een extra parallelle tak biedt een extra stroompad, waardoor de totale weerstand DAALT en de totale stroom toeneemt."
    },
    {
      type: "waaronwaar",
      vraag: "In een parallelschakeling loopt door de tak met de <b>kleinste weerstand</b> de <b>grootste stroom</b>.",
      antwoord: true,
      uitleg: "Waar. Omdat U gelijk is, geldt I = U / R: de tak met de minste weerstand laat de meeste stroom door."
    },
    {
      type: "invul",
      vraag: "Een lamp (R_1 = 100 Ω) en een radio (R_2 = 150 Ω) staan parallel op 230 V. Bereken de stroom door de lamp (in Ampère, afgerond op 1 decimaal).",
      antwoord: "2,3|2,3 A",
      uitleg: "I_lamp = U / R_1 = 230 V / 100 Ω = 2,3 A."
    },
    {
      type: "mc",
      vraag: "Een huisgroep in de meterkast is beveiligd met een automatische zekering van <b>16 A</b> op 230 V. Wat gebeurt er als de totale stroomsterkte door aangesloten apparaten oploopt naar 19 A?",
      opties: [
        "De apparaten krijgen meer spanning",
        "De zekering schakelt de groep automatisch uit ter voorkoming van oververhitting en brand (overbelasting)",
        "De stroom daalt vanzelf zonder dat er iets gebeurt",
        "De netspanning zakt naar 100 V"
      ],
      antwoord: 1,
      uitleg: "De zekering springt open bij overbelasting (I > 16 A) om de bedrading tegen oververhitting en brand te beschermen."
    },
    {
      type: "invul",
      vraag: "Drie gelijke lampjes van elk 15 Ω staan in serie op een 9 V batterij. Bereken de stroomsterkte in Ampère.",
      antwoord: "0,2|0,2 A|0,20",
      uitleg: "R_tot = 15 + 15 + 15 = 45 Ω. I = U / R_tot = 9 V / 45 Ω = 0,2 A."
    },
    {
      type: "waaronwaar",
      vraag: "Als je twee lampjes van serie naar parallel overschakelt op dezelfde batterij, gaan beide lampjes feller branden.",
      antwoord: true,
      uitleg: "Waar. In parallel krijgt elk lampje de volledige batterijspanning en trekt meer stroom, dus branden ze veel feller (maar de batterij raakt sneller leeg)."
    },
    {
      type: "mc",
      vraag: "Twee weerstanden R_1 = 20 Ω en R_2 = 30 Ω staan parallel op een spanningsbron van 12 V. Hoe groot is de totale stroomsterkte I_tot?",
      opties: [
        "0,24 A",
        "0,60 A",
        "1,00 A",
        "1,20 A"
      ],
      antwoord: 2,
      uitleg: "I_1 = 12 / 20 = 0,6 A. I_2 = 12 / 30 = 0,4 A. I_tot = 0,6 + 0,4 = 1,0 A."
    },
    {
      type: "invul",
      vraag: "In de vorige vraag (U = 12 V, I_tot = 1,0 A): bereken de totale vervangingsweerstand R_tot in Ohm (via R = U / I_tot).",
      antwoord: "12|12 Ω|12 ohm",
      uitleg: "R_tot = U / I_tot = 12 V / 1,0 A = 12 Ω."
    },
    {
      type: "waaronwaar",
      vraag: "Kortsluiting ontstaat wanneer de stroomkring een pad krijgt met nagenoeg 0 Ohm weerstand, waardoor de stroomsterkte extreem hoog wordt.",
      antwoord: true,
      uitleg: "Waar. Bij R ≈ 0 wordt I = U / R gigantisch groot, wat leidt tot vonken, smelten van draden of brand."
    },
    {
      type: "open",
      vraag: "Leg aan de hand van stroom en spanning uit waarom apparaten in huis parallel worden aangesloten en niet in serie.",
      sleutelwoorden: ["elk apparaat 230 V / gelijke spanning", "onafhankelijk aan/uit zetten", "bij serie gaat alles uit / spanning verdeelt"],
      minTreffers: 2,
      modelantwoord: "1. Spanning: In een parallelschakeling staat over elk apparaat de volle 230 V netspanning, zodat elk apparaat op zijn ontwerpspanning werkt. (In serie zou de 230 V zich verdelen en krijgen apparaten te weinig spanning).\n2. Onafhankelijkheid: Elk apparaat heeft een eigen stroomtak. Als je één apparaat uitschakelt of als een lamp kapotgaat, blijven alle andere apparaten gewoon werken.",
      uitleg: "Twee hoofdredenen: constante 230 V spanning overal + onafhankelijke bediening per apparaat."
    },
    {
      type: "open",
      vraag: "In een stekkerdoos sluit iemand tegelijkertijd een waterkoker (9 A), een broodrooster (4 A) en een frituurpan (8 A) aan op dezelfde 16 A groep. Beredeneer of de zekering uitschakelt.",
      sleutelwoorden: ["totale stroom optellen / I_tot = 9 + 4 + 8 = 21 A", "21 A is groter dan 16 A", "overbelasting / zekering slaat door/schakelt uit"],
      minTreffers: 2,
      modelantwoord: "Omdat de apparaten parallel staan op de groep, tellen de stromen bij elkaar op: I_tot = 9 A + 4 A + 8 A = 21 A. De zekering van de groep is berekend op maximaal 16 A. Omdat 21 A > 16 A is er sprake van overbelasting en zal de zekering (groepsschakelaar) direct uitschakelen om oververhitting van de bedrading te voorkomen.",
      uitleg: "Totale stroom = 21 A; dit overschrijdt de 16 A grens van de zekering."
    }
  ]
});
