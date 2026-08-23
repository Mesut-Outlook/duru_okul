/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 1.1: De moderne beleving van tijd
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h1-1",
    hoofdstuk: 1,
    paragraaf: "1.1",
    titel: "De moderne beleving van tijd",
    korteUitleg: "Tijdzones, spoorwegen, la belle époque, vooruitgangsgeloof en de eerste moderne Olympische Spelen.",
    icoon: "⏱️",
    theorie: `
<h3>1.1 De moderne beleving van tijd</h3>

<p>Rond het jaar 1900 begon in grote delen van Europa de nieuwe eeuw op precies hetzelfde moment. Dat was heel nieuw, want daarvoor had elke stad of elk dorp zijn eigen tijd, gebaseerd op de stand van de zon (zonnetijd).</p>

<h4>Spoorwegen en landelijke tijd</h4>
<p>Voor de opkomende spoorwegen was het lastig dat elke plaats een andere tijd had. Om een strakke dienstregeling te kunnen maken, hadden de spoorwegen één landelijke standaardtijd nodig.</p>
<ul>
  <li><b>De telegraaf (1846):</b> Vanaf 1846 werden stationsklokken in Groot-Brittannië via telegraafdraden met elkaar verbonden. De klokken werden afgesteld op de sterrenwacht van <b>Greenwich</b> (Londen).</li>
  <li><b>Tijdzones (1891):</b> Door het toenemende internationale treinverkeer werd Europa in 1891 opgedeeld in drie tijdzones: West-Europese tijd (Greenwich), Midden-Europese tijd en Oost-Europese tijd (2 uur voor op Greenwich).</li>
  <li><b>Nederland:</b> Nederland koos in eerste instantie voor de Amsterdamse tijd/Greenwich-tijd. Pas tijdens de Duitse bezetting in 1940 werd de Midden-Europese tijd ingevoerd, die we nu nog steeds gebruiken.</li>
</ul>

<div class="info-box tip">
  <span class="kop">💡 Zomertijd</span>
  Op 30 april 1916 voerden Duitsland en Oostenrijk voor het eerst de <b>zomertijd</b> in om kolen en energie te besparen voor de oorlogsvoering. Pas in 1977 voerde Nederland de zomertijd definitief opnieuw in.
</div>

<h4>La belle époque (1890–1914)</h4>
<p>De periode van 1890 tot het uitbreken van de Eerste Wereldoorlog in 1914 wordt achteraf door de Fransen <b>la belle époque</b> ("het mooie tijdperk") genoemd.</p>
<div class="formule-box">
  <span class="formule">Kenmerken van la belle époque:</span>
  <small>
    • Groeiende welvaart en democratie<br>
    • Kortere werkdagen, hogere lonen en verbod op kinderarbeid<br>
    • Nieuwe uitvindingen: telefoon, gloeilamp, film (bioscoop)<br>
    • Medische revolutie: betere hygiëne en minder ziektes<br>
    • Opkomst van toerisme en cultuur (boeken van Tolstoi, Hugo, Dickens)<br>
    • <b>Vooruitgangsgeloof:</b> het rotsvaste idee dat het leven steeds beter zou worden door wetenschap en techniek.
  </small>
</div>

<h4>De moderne Olympische Spelen (1896)</h4>
<p>In 1896 werden in Athene voor het eerst de <b>moderne Olympische Spelen</b> georganiseerd, een initiatief van de Franse baron <b>Pierre de Coubertin</b>.</p>
<ul>
  <li><b>Waarom in 1896?</b> De Spelen pasten perfect bij de moderne industriële samenleving: mensen werkten op kantoor en zochten lichaamsbeweging. De trein maakte reizen naar Griekenland mogelijk, en de pas uitgevonden <i>stopwatch</i> maakte nauwkeurige tijdmeting (in tienden van seconden) mogelijk.</li>
  <li><b>Nationalisme:</b> Sport werd ook gebruikt om jongens fysiek sterk, gedisciplineerd en weerbaar te maken voor het nationale leger.</li>
</ul>
    `,
    vragen: [
      {
        id: "h1_1_v1",
        niveau: 1,
        type: "mc",
        vraag: "Waarom werd in de 19e eeuw een landelijke standaardtijd noodzakelijk?",
        opties: [
          "Omdat de fabrieken precies om 08:00 uur moesten openen.",
          "Omdat de spoorwegen een betrouwbare dienstregeling nodig hadden.",
          "Omdat de kerkklokken niet meer goed werkten.",
          "Omdat de telegraaf anders geen berichten kon versturen."
        ],
        antwoord: 1,
        uitleg: "Met de opkomst van de trein en spoorwegen was het onmogelijk om een dienstregeling te maken als elke stad zijn eigen zonne-tijd aanhield."
      },
      {
        id: "h1_1_v2",
        niveau: 1,
        type: "waaronwaar",
        vraag: "In 1891 werd Europa opgedeeld in drie verschillende tijdzones.",
        antwoord: true,
        uitleg: "Waar! Om het internationale treinverkeer te stroomlijnen werd Europa in 1891 verdeeld in West-Europese, Midden-Europese en Oost-Europese tijd."
      },
      {
        id: "h1_1_v3",
        niveau: 1,
        type: "invoer",
        vraag: "Hoe noemden de Fransen de periode 1890-1914 achteraf, wat 'het mooie tijdperk' betekent?",
        antwoord: "la belle époque|la belle epoque|belle epoque|belle époque",
        uitleg: "'La belle époque' verwijst naar de periode van vrede, welvaart en culturele bloei vlak voor de Eerste Wereldoorlog."
      },
      {
        id: "h1_1_v4",
        niveau: 2,
        type: "mc",
        vraag: "Wat wordt bedoeld met het begrip 'vooruitgangsgeloof' rond 1900?",
        opties: [
          "Het geloof dat de kerk steeds machtiger zou worden in Europa.",
          "Het idee dat de mensheid door wetenschap, techniek en industrie steeds beter en gelukkiger zou worden.",
          "Het idee dat de mensheid sneller kon reizen door het geloof.",
          "Het vertrouwen dat er nooit meer oorlog zou komen tussen Europese landen."
        ],
        antwoord: 1,
        uitleg: "Het vooruitgangsgeloof was het optimistische idee dat de maatschappij door technologische vernieuwingen en wetenschap continu vooruitging."
      },
      {
        id: "h1_1_v5",
        niveau: 2,
        type: "mc",
        vraag: "Wie was de Franse initiator van de moderne Olympische Spelen in 1896?",
        opties: [
          "Victor Hugo",
          "Pierre de Coubertin",
          "Koning Willem III",
          "Tsaar Nicolaas II"
        ],
        antwoord: 1,
        uitleg: "Baron Pierre de Coubertin blies de klassieke Olympische Spelen in 1896 in Athene nieuw leven in."
      },
      {
        id: "h1_1_v6",
        niveau: 2,
        type: "waaronwaar",
        vraag: "De eerste zomertijd werd in 1916 door Duitsland en Oostenrijk ingevoerd om kolen en energie voor de oorlogsvoering te besparen.",
        antwoord: true,
        uitleg: "Waar! Door de klok een uur vooruit te zetten bleef het 's avonds langer licht, waardoor er minder steenkool werd gebruikt voor verlichting."
      },
      {
        id: "h1_1_v7",
        niveau: 3,
        type: "mc",
        vraag: "Op welke manier droeg het nationalisme bij aan de populariteit van de moderne Olympische Spelen?",
        opties: [
          "Landen wilden laten zien dat hun atleten de sterkste waren en sport maakte de jeugd weerbaar voor het leger.",
          "De Olympische Spelen vervingen alle nationale legers.",
          "Alleen neutrale landen mochten meedoen aan de Spelen.",
          "Het nationalisme zorgde ervoor dat alle landen dezelfde vlag gebruikten."
        ],
        antwoord: 0,
        uitleg: "Sport werd gezien als een internationale krachtmeting tussen staten, en overheden zagen sport als een goede manier om jonge mannen fit en gedisciplineerd te maken voor militaire dienst."
      },
      {
        id: "h1_1_v8",
        niveau: 3,
        type: "invoer",
        vraag: "Bij welke Engelse plaats staat de bekende sterrenwacht waarop de internationale standaardtijd werd afgestemd?",
        antwoord: "Greenwich|greenwich",
        uitleg: "De nulmeridiaan en de standaardtijd werden afgesteld op de Koninklijke Sterrenwacht in Greenwich bij Londen."
      }
    ]
  });
})();
