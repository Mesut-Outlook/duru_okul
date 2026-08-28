/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 1.2: De Grote Oorlog
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h1-2",
    hoofdstuk: 1,
    paragraaf: "1.2",
    titel: "De Grote Oorlog",
    korteUitleg: "Oorzaken van WO1, de vonk in Sarajevo, het Schlieffenplan, de loopgravenoorlog en het einde in 1918.",
    icoon: "⚔️",
    theorie: `
<h3>1.2 De Grote Oorlog (1914–1918)</h3>

<p>In augustus 1914 brak een enorme Europese strijd uit die vier jaar zou duren: de <b>Eerste Wereldoorlog</b> (toen "De Grote Oorlog" genoemd).</p>

<h4>De twee bondgenootschappen</h4>
<ul>
  <li><b>De Geallieerden:</b> Groot-Brittannië, Frankrijk, Rusland (tot 1918), Italië (vanaf 1915) en de Verenigde Staten (vanaf 1917).</li>
  <li><b>De Centralen:</b> Duitsland, Oostenrijk-Hongarije, het Ottomaanse Rijk en Bulgarije.</li>
</ul>

<h4>Dieper liggende oorzaken van de oorlog</h4>
<div class="formule-box">
  <span class="formule">Vier hoofd-oorzaken van de Eerste Wereldoorlog:</span>
  <small>
    1. <b>Nationalisme:</b> Grote liefde voor het eigen volk en overtuiging dat het eigen land superieur was.<br>
    2. <b>Militarisme:</b> Verheerlijking van het leger, soldaten en militaire waarden.<br>
    3. <b>Wapenwedloop:</b> Race tussen Europese landen om het sterkste en modernste leger/vloot op te bouwen.<br>
    4. <b>Bondgenootschappen:</b> Geheim verweven netwerk van afspraken (als X aangevallen wordt, helpt Y).
  </small>
</div>

<h4>De aanleiding (de vonk): Sarajevo, 28 juni 1914</h4>
<p>Op <b>28 juni 1914</b> werd de Oostenrijkse troonopvolger <b>Frans Ferdinand</b> en zijn vrouw Sophie in Sarajevo (Bosnië) doodgeschoten door <b>Gavrilo Princip</b>, een 19-jarige Servische nationalist. Oostenrijk verklaarde Servie de oorlog op 28 juli 1914. Door het netwerk van bondgenootschappen raakte heel Europa binnen een week in oorlog.</p>

<h4>Het verloop van de strijd</h4>
<ul>
  <li><b>Het Schlieffenplan:</b> Duitsland wilde een tweefrontenoorlog voorkomen door Frankrijk in 7 weken te verslaan via het neutrale België, en daarna de troepen naar Rusland te sturen. De Belgische tegenstand en Britse inval vertraagden het plan.</li>
  <li><b>Westfront (Loopgravenoorlog):</b> Aan de rivier de Marne werd de Duitse opmars gestopt. Vanaf eind 1914 groef men zich in langs een 700 km lang front van de Belgische kust tot de Zwitserse grens. Miljoenen soldaten kwamen om door machinegeweren, granaten en gifgas.</li>
  <li><b>Oostfront:</b> Duitsland en Oostenrijk vochten tegen Rusland. In 1917 stortte het tsarenrijk in; in maart 1918 sloot de nieuwe communistische regering de <b>Vrede van Brest-Litovsk</b>.</li>
  <li><b>Keerpunt 1917–1918:</b> De VS verklaarden in april 1917 de oorlog aan Duitsland. Vanaf 1918 kwamen maandelijks 250.000 verse Amerikaanse soldaten. Tanks, vliegtuigen en zware artillerie braken de Duitse weerstand.</li>
  <li><b>Wapenstilstand:</b> Op <b>11 november 1918 om 11:00 uur</b> (11-11-11u) ging de wapenstilstand in. Duitsland capituleerde. In totaal kwamen 10 miljoen militairen om.</li>
</ul>

<div class="info-box let-op">
  <span class="kop">⚠️ Armeense Genocide (1915)</span>
  Tijdens de oorlog beschuldigde de Ottomaanse overheid haar christelijke Armeense onderdanen van samenwerking met Rusland. Dit leidde vanaf april 1915 tot de deportatie en executie van meer dan één miljoen Armeniërs (dodenmarsen in de woestijn van Syrië en Irak).
</div>
    `,
    vragen: [
      {
        id: "h1_2_v1",
        niveau: 1,
        type: "mc",
        vraag: "Welke landen vormden bij het uitbreken van de Eerste Wereldoorlog de kern van de Centralen?",
        opties: [
          "Duitsland en Oostenrijk-Hongarije",
          "Groot-Brittannië en Frankrijk",
          "Rusland en Italië",
          "Nederland en België"
        ],
        antwoord: 0,
        uitleg: "De Centralen dankten hun naam aan hun centrale ligging in Europa: Duitsland en Oostenrijk-Hongarije (later aangevuld met het Ottomaanse Rijk)."
      },
      {
        id: "h1_2_v2",
        niveau: 1,
        type: "invoer",
        vraag: "Op welke datum en in welke stad werd de Oostenrijkse kroonprins Frans Ferdinand neergeschoten?",
        antwoord: "28 juni 1914|Sarajevo|28 juni 1914 in Sarajevo",
        uitleg: "De moord op Frans Ferdinand vond plaats op 28 juni 1914 in Sarajevo, de hoofdstad van Bosnië."
      },
      {
        id: "h1_2_v3",
        niveau: 1,
        type: "mc",
        vraag: "Wat hield het Duitse 'Schlieffenplan' in?",
        opties: [
          "Direct Rusland aanvallen en daarna Groot-Brittannië via de zee veroveren.",
          "Frankrijk snel verslaan via neutraal België, om daarna alle troepen naar het oostfront tegen Rusland te sturen.",
          "Een geheim verbond sluiten met de Verenigde Staten.",
          "Nederland bezetten om de haven van Rotterdam te gebruiken."
        ],
        antwoord: 1,
        uitleg: "Het Schlieffenplan was ontworpen om een uitputtende tweefrontenoorlog te voorkomen door Frankrijk in bliksemtempo via België uit te schakelen."
      },
      {
        id: "h1_2_v4",
        niveau: 2,
        type: "waaronwaar",
        vraag: "Een 'tweefrontenoorlog' betekent dat een land tegelijkertijd aan twee verschillende grenzen tegen twee vijanden moet vechten.",
        antwoord: true,
        uitleg: "Waar! Duitsland moest aan het Westfront vechten tegen Frankrijk/Groot-Brittannië en aan het Oostfront tegen Rusland."
      },
      {
        id: "h1_2_v5",
        niveau: 2,
        type: "mc",
        vraag: "Welke gebeurtenis in 1917 gaf de doorslag ten gunste van de Geallieerden aan het westfront?",
        opties: [
          "Het aftreden van de Duitse keizer.",
          "De overgave van België aan Duitsland.",
          "De deelname van de Verenigde Staten aan de oorlog aan de zijde van de Geallieerden.",
          "De uitvinding van de telegraaf."
        ],
        antwoord: 2,
        uitleg: "De deelname van de VS bracht honderdduizenden verse troepen, enorme industriële capaciteit en geld naar het Westfront."
      },
      {
        id: "h1_2_v6",
        niveau: 2,
        type: "invoer",
        vraag: "Op welke bekende datum ging de wapenstilstand van de Eerste Wereldoorlog in (dag-maand-jaar)?",
        antwoord: "11 november 1918|11-11-1918|11/11/1918",
        uitleg: "De wapenstilstand ging in op de elfde van de elfde maand om elf uur 's morgens: 11 november 1918 om 11:00 uur."
      },
      {
        id: "h1_2_v7",
        niveau: 3,
        type: "mc",
        vraag: "Wat is het verschil tussen een 'oorzaak' en de 'aanleiding' van de Eerste Wereldoorlog?",
        opties: [
          "Een oorzaak is de druppel die de emmer doet overlopen; de aanleiding speelt al tientallen jaren.",
          "De aanleiding vond plaats in 1918; de oorzaken ontstonden pas na de Vrede van Versailles.",
          "Er is geen verschil; beide begrippen betekenen exact hetzelfde.",
          "Oorzaken zijn dieper liggende spanningen die al langer opbouwen (militarisme, wapenwedloop); de aanleiding is de directe vonk (de moord in Sarajevo)."
        ],
        antwoord: 3,
        uitleg: "Oorzaken (militarisme, nationalisme, bondgenootschappen) bouwden gedurende tientallen jaren spanning op; de moord in Sarajevo was de directe aanleiding (vonk) waardoor het kruitvat ontplofte."
      },
      {
        id: "h1_2_v8",
        niveau: 3,
        type: "waaronwaar",
        vraag: "In het Ottomaanse Rijk leidden verdenkingen van samenwerking met Rusland in 1915 tot de deportatie en genocide op meer dan 1 miljoen Armeniërs.",
        antwoord: true,
        uitleg: "Waar! Vanaf april 1915 werden Armeense leiders geëxecuteerd en de Armeense bevolking op dodenmarsen door de woestijn gestuurd."
      }
    ]
  });
})();
