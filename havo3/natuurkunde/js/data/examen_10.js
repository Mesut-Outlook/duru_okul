/* Proeftoets 10 — Natuurkunde HAVO 3: Hoofdstuk 2 (Elektriciteit - Integrale Eindtoets)
   Focus: Volledig Hoofdstuk 2 (§2.1 t/m §2.5) — Elektromagnetisme, inductie, schakelingen en gemengde berekeningen.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-10",
  titel: "Toets 10 — Integrale Eindtoets Hoofdstuk 2 (Elektriciteit)",
  vak: "Natuurkunde · HAVO 3 (H2)",
  icoon: "🏆",
  duurMin: 35,
  vragen: [
    {
      type: "mc",
      vraag: "Wat ontstaat er rondom een stroomdraad waar een elektrische stroom doorheen loopt?",
      opties: [
        "Een magnetisch veld",
        "Een zwaartekrachtveld",
        "Een radioactief veld",
        "Geen enkel veld"
      ],
      antwoord: 0,
      uitleg: "Elke elektrische stroom wekt een magnetisch veld op om de draad. Dit is de basis van elektromagnetisme."
    },
    {
      type: "mc",
      vraag: "Hoe kun je een <b>elektromagneet</b> sterker maken?",
      opties: [
        "Door de stroomsterkte te verlagen",
        "Door een weekijzeren kern in de spoel te plaatsen, meer windingen te gebruiken en de stroomsterkte te verhogen",
        "Door de spoel van plastic te maken",
        "Door de spoel af te koelen tot het vriespunt"
      ],
      antwoord: 1,
      uitleg: "De magneetkracht van een spoel neemt toe bij: 1) meer windingen, 2) grotere stroomsterkte I, 3) een ijzeren kern."
    },
    {
      type: "waaronwaar",
      vraag: "Een elektromagneet kun je in- en uitschakelen door de stroomkring te openen of te sluiten, in tegenstelling tot een permanente magneet.",
      antwoord: true,
      uitleg: "Waar. Als de stroom stopt, verdwijnt het magnetische veld direct (ideaal voor schroothijskranen en deurbellen)."
    },
    {
      type: "mc",
      vraag: "Hoe wekt een <b>dynamo of generator</b> in een elektriciteitscentrale spanning op (inductie)?",
      opties: [
        "Door water direct door een koperdraad te pompen",
        "Door twee batterijen tegen elkaar te wrijven",
        "Door een magneet en een koperen spoel ten opzichte van elkaar te laten bewegen/draaien",
        "Door statische lading met een wollen doek op te wekken"
      ],
      antwoord: 2,
      uitleg: "Door een veranderend magnetisch veld in een spoel (draaiende magneet of draaiende spoel) ontstaat inductiespanning."
    },
    {
      type: "invul",
      vraag: "Een waterkoker van 1840 W is aangesloten op 230 V. Bereken de weerstand van het verwarmingselement in Ohm.",
      antwoord: "28,75|28,8|29|28,75 Ω",
      uitleg: "I = P / U = 1840 / 230 = 8,0 A. R = U / I = 230 / 8,0 = 28,75 Ω."
    },
    {
      type: "mc",
      vraag: "In een serieschakeling zitten twee weerstanden: R_1 = 40 Ω en R_2 = 60 Ω op een bron van 20 V. Hoe groot is de spanning U_2 over weerstand R_2?",
      opties: [
        "8 V",
        "10 V",
        "20 V",
        "12 V"
      ],
      antwoord: 3,
      uitleg: "R_tot = 100 Ω. I = 20 / 100 = 0,2 A. U_2 = 0,2 A × 60 Ω = 12 V (over R_1 staat 8 V; samen 20 V)."
    },
    {
      type: "waaronwaar",
      vraag: "In een parallelschakeling is de totale stroomsterkte altijd groter dan de stroomsterkte door elk van de afzonderlijke takken.",
      antwoord: true,
      uitleg: "Waar. De hoofdstroom is de som van alle takstromen: I_tot = I_1 + I_2 + ..."
    },
    {
      type: "invul",
      vraag: "Drie identieke lampen van elk 40 W staan parallel geschakeld op 230 V. Hoeveel Watt vermogen levert de bron in totaal?",
      antwoord: "120|120 W|120 watt",
      uitleg: "P_tot = 40 + 40 + 40 = 120 W."
    },
    {
      type: "invul",
      vraag: "Een straalkachel van 1500 W (1,5 kW) staat per dag 4 uur aan gedurende 30 dagen in de winter. Hoeveel kWh energie is dit in totaal?",
      antwoord: "180|180 kWh|180,0",
      uitleg: "Totale tijd = 4 h/dag × 30 dagen = 120 uur. E = 1,5 kW × 120 h = 180 kWh."
    },
    {
      type: "mc",
      vraag: "Waarom wordt elektriciteit over grote afstanden getransporteerd onder <b>zeer hoge spanning</b> (hoogspanningsmasten tot 380.000 V)?",
      opties: [
        "Om de stroomsterkte I zo klein mogelijk te maken, waardoor er veel minder energieverlies door warmteontwikkeling in de kabels is",
        "Omdat elektronen anders te langzaam bewegen",
        "Omdat vogels anders niet op de kabels kunnen zitten",
        "Omdat de transformator anders ontploft"
      ],
      antwoord: 0,
      uitleg: "Bij hoogspanning is voor hetzelfde vermogen (P = U × I) een veel kleinere stroom I nodig. Omdat kabelverlies schaalt met I² × R, bespaart dit enorm veel energie."
    },
    {
      type: "waaronwaar",
      vraag: "Twee magnetische noordpolen trekken elkaar met grote kracht aan.",
      antwoord: false,
      uitleg: "Niet waar. Gelijke polen (N-N of Z-Z) stoten elkaar af. Alleen N en Z trekken elkaar aan."
    },
    {
      type: "invul",
      vraag: "Een fietsdynamo levert 6,0 V en een stroom van 0,50 A aan de koplamp. Hoeveel Watt vermogen heeft de koplamp?",
      antwoord: "3|3 W|3,0|3,0 W",
      uitleg: "P = U × I = 6,0 V × 0,50 A = 3,0 W."
    },
    {
      type: "mc",
      vraag: "Wat is het doel van een <b>aardlekschakelaar</b> in de meterkast?",
      opties: [
        "Meten hoeveel kWh je verbruikt",
        "Uitschakelen zodra er stroom 'weglekt' naar de aarde (bijv. via een menselijk lichaam), ter bescherming tegen elektrocutie",
        "De spanning verhogen naar 400 V",
        "Voorkomen dat er bliksem in de meterkast slaat"
      ],
      antwoord: 1,
      uitleg: "Een aardlekschakelaar vergelijkt de heenstroom met de terugstroom. Als er meer dan 30 mA weglekt, schakelt hij binnen milliseconden de stroom uit."
    },
    {
      type: "invul",
      vraag: "Over een weerstand van 500 Ω staat een spanning van 25 V. Hoeveel milliampère (mA) stroom loopt er door de weerstand?",
      antwoord: "50|50 mA|50mA",
      uitleg: "I = U / R = 25 / 500 = 0,05 A = 50 mA."
    },
    {
      type: "waaronwaar",
      vraag: "Als je twee weerstanden van 100 Ω in serie schakelt is de vervangingsweerstand 200 Ω; schakel je ze parallel dan is de vervangingsweerstand 50 Ω.",
      antwoord: true,
      uitleg: "Waar. Serie: 100 + 100 = 200 Ω. Parallel: 100 / 2 = 50 Ω."
    },
    {
      type: "mc",
      vraag: "Een föhn van 1200 W wordt aangesloten op 230 V. Bereken de stroomsterkte door de föhn.",
      opties: [
        "0,19 A",
        "2,6 A",
        "5,2 A",
        "12 A"
      ],
      antwoord: 2,
      uitleg: "I = P / U = 1200 W / 230 V ≈ 5,22 A."
    },
    {
      type: "invul",
      vraag: "Een LED-lamp van 8 W brandt 500 uur. Hoeveel kWh energie heeft de lamp verbruikt?",
      antwoord: "4|4 kWh|4,0",
      uitleg: "P = 8 W = 0,008 kW. E = 0,008 kW × 500 h = 4 kWh."
    },
    {
      type: "waaronwaar",
      vraag: "Een transformator werkt uitsluitend op <b>wisselspanning</b> omdat er een continu veranderend magnetisch veld nodig is om inductiespanning op te wekken.",
      antwoord: true,
      uitleg: "Waar. Bij constante gelijkspanning (zoals een batterij) verandert het magnetische veld niet en wekt de secundaire spoel geen spanning op."
    },
    {
      type: "open",
      vraag: "Leg uit hoe een <b>relais</b> (automatische schakelaar met elektromagneet) werkt en waarom dit gebruikt wordt om met een kleine veilige stroomkring een zware machine met hoge stroom in te schakelen.",
      sleutelwoorden: ["elektromagneet trekt anker/schakelaar aan", "stuurstroomkring gescheiden van hoofdstroomkring", "veiligheid/geen zware schakelaar met hoge stroom in handen"],
      minTreffers: 2,
      modelantwoord: "In een relais loopt een kleine stuurstroom door een spoel. Deze wordt daardoor magnetisch en trekt een ijzeren hefboom (het anker) aan. Hierdoor sluit een zware schakelaar in een tweede, gescheiden stroomkring met hoge spanning/stroom. Dit zorgt ervoor dat de gebruiker alleen de veilige laagspanningsknop hoeft te bedienen en beschermd blijft tegen gevaarlijk hoge stromen.",
      uitleg: "Kern: stuurkring bekrachtigt elektromagneet -> sluit fysieke schakelaar in de zware werkkring."
    },
    {
      type: "open",
      vraag: "Vergelijk een <b>serieschakeling</b> en een <b>parallelschakeling</b> op de volgende drie punten: 1) stroomverdeling, 2) spanningsverdeling, 3) wat er gebeurt als één lampje kapotgaat.",
      sleutelwoorden: ["serie stroom gelijk / parallel stroom telt op", "serie spanning verdeelt / parallel spanning overal gelijk", "serie alles uit / parallel andere blijven branden"],
      minTreffers: 3,
      modelantwoord: "1. Stroomsterkte: Bij serie is de stroom overal gelijk (I_tot = I_1 = I_2); bij parallel verdeelt de hoofdstroom zich over de takken (I_tot = I_1 + I_2).\n2. Spanning: Bij serie verdeelt de bronspanning zich over de weerstanden (U_tot = U_1 + U_2); bij parallel staat over elke tak de volle bronspanning (U_tot = U_1 = U_2).\n3. Defect: Bij serie gaat bij één kapot lampje de hele kring open en alles uit; bij parallel blijft de rest gewoon onafhankelijk doordraaien.",
      uitleg: "Volledige vergelijking op stroom, spanning en stroomonderbreking."
    }
  ]
});
