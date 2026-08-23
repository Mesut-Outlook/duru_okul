/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Proeftoets 2: Revolutie, Kaart van Europa & Neutraal NL
   ========================================================= */
(function () {
  "use strict";

  DURU.registerExamen({
    id: "ex-h3-geschiedenis-2",
    titel: "Proeftoets 2 — Revolutie, Nieuwe Kaart & Neutraal NL (1.3 - 1.5)",
    vak: "Geschiedenis · HAVO 3",
    icoon: "📜",
    duurMin: 15,
    vragen: [
      {
        id: "ges2_v1",
        type: "mc",
        vraag: "Wat gebeurde er tijdens de Februarirevolutie van 1917 in Rusland?",
        opties: [
          "Tsaar Nicolaas II trad af en Rusland werd een republiek met een voorlopige regering.",
          "Lenin greep direct de macht en stichtte de Sovjet-Unie.",
          "Rusland won de Eerste Wereldoorlog van Duitsland.",
          "De tsaar schafte de Doema definitief af."
        ],
        antwoord: 0,
        uitleg: "In februari 1917 leidde honger en muiterij tot het aftreden van tsaar Nicolaas II; Rusland werd een republiek."
      },
      {
        id: "ges2_v2",
        type: "invul",
        vraag: "De communistische raden van arbeiders en soldaten die in Rusland ontstonden, werden ____ genoemd.",
        antwoord: "sovjets|sovjet|raden",
        uitleg: "Het woord 'sovjet' betekent letterlijk raad."
      },
      {
        id: "ges2_v3",
        type: "waaronwaar",
        vraag: "Tijdens de Oktoberrevolutie van 1917 pleegden Lenin en de bolsjewieken een staatsgreep en maakten ze van Rusland een communistische eenpartijstaat.",
        antwoord: true,
        uitleg: "Waar! Lenin verbood alle andere politieke partijen en vestigde de 'dictatuur van het proletariaat'."
      },
      {
        id: "ges2_v4",
        type: "mc",
        vraag: "In welk jaar werd de Sovjet-Unie (USSR) officieel gesticht?",
        opties: [
          "1914",
          "1917",
          "1922",
          "1939"
        ],
        antwoord: 2,
        uitleg: "In 1922 verenigde communistisch Rusland zich met omliggende republieken tot de Sovjet-Unie."
      },
      {
        id: "ges2_v5",
        type: "mc",
        vraag: "Wat verstaan we onder het 'zelfbeschikkingsrecht' zoals voorgesteld door president Wilson?",
        opties: [
          "Het recht van een volk om zelf hun staatsgrenzen en bestuur te kiezen.",
          "Het recht van keizers om eigen wetten te maken.",
          "Het recht van grote staten om kleine buren te annexeren.",
          "Het recht van soldaten om dienst te weigeren."
        ],
        antwoord: 0,
        uitleg: "Zelfbeschikkingsrecht geeft volkeren de vrijheid om over hun eigen politieke toekomst en land te beslissen."
      },
      {
        id: "ges2_v6",
        type: "waaronwaar",
        vraag: "In de Vrede van Versailles (1919) werd afgesproken dat de schuld voor WO1 eerlijk verdeeld werd over alle Europese landen.",
        antwoord: false,
        uitleg: "Onwaar! In Versailles kreeg Duitsland de 'alleenschuld' opgelegd, plus gigantische herstelbetalingen en zwaar verlies van grondgebied en leger."
      },
      {
        id: "ges2_v7",
        type: "invul",
        vraag: "Welke erenaam kreeg de Turkse leider Mustafa Kemal nadat hij in 1923 de Republiek Turkije stichtte?",
        antwoord: "Atatürk|Ataturk|ataturk|atatürk",
        uitleg: "Mustafa Kemal kreeg de erenaam Atatürk ('Vader der Turken')."
      },
      {
        id: "ges2_v8",
        type: "mc",
        vraag: "Waarom sloten de Duitsers eind 1914 de Belgisch-Nederlandse grens af met de 'Draad des Doods'?",
        opties: [
          "Om te voorkomen dat Belgen naar het neutrale Nederland vluchtten of dat spionnen en brieven de grens overstaken.",
          "Om elektriciteit te leveren aan Nederlandse steden.",
          "Om de Rotterdamse haven af te sluiten.",
          "Om Nederlandse militairen gevangen te nemen."
        ],
        antwoord: 0,
        uitleg: "Het hek onder hoogspanning moest vluchtelingen, spionnen en illegale grens-overgangen verhinderen."
      },
      {
        id: "ges2_v9",
        type: "mc",
        vraag: "Wat hield het 'distributiestelsel' in Nederland in tijdens de Eerste Wereldoorlog?",
        opties: [
          "Iedereen kreeg gratis eten van de koningin.",
          "Schaarse basisproducten ging 'op de bon'; je had bonnen nodig én geld om eten en brandstof te kopen.",
          "Producten werden uitsluitend via de marine verdeeld.",
          "Al het voedsel werd geëxporteerd naar Duitsland."
        ],
        antwoord: 1,
        uitleg: "Omdat er tekorten ontstonden, verdeelde de overheid voedsel en steenkool eerlijk via distributiebonnen."
      },
      {
        id: "ges2_v10",
        type: "waaronwaar",
        vraag: "Bij de Grondwetsherziening van 1917 kregen zowel mannen als vrouwen in Nederland direct algemeen kiesrecht.",
        antwoord: false,
        uitleg: "Onwaar! In 1917 kregen alleen mannen algemeen kiesrecht. Vrouwen kregen pas twee jaar later (in 1919) algemeen kiesrecht."
      },
      {
        id: "ges2_v11",
        type: "invul",
        vraag: "Welke beroemde Nederlandse kunstbeweging werd in 1917 opgericht door onder meer Piet Mondriaan en Gerrit Rietveld?",
        antwoord: "De Stijl|de stijl|De stijl",
        uitleg: "De Stijl was een invloedrijke artistieke beweging gericht op strakke vormen, abstractie en primaire kleuren."
      },
      {
        id: "ges2_v12",
        type: "open",
        vraag: "Leg uit waarom de Grondwetsherziening van 1917 wordt gezien als een grote doorbraak in de Nederlandse politiek.",
        sleutelwoorden: [
          "kiesrecht/mannenkiesrecht/democratie",
          "schoolstrijd/gelijke financiering/bijzonder onderwijs"
        ],
        minTreffers: 1,
        modelantwoord: "In de Grondwetsherziening van 1917 werden twee langlopende conflicten opgelost: mannen kregen algemeen kiesrecht (kiesrechtkwestie) en bijzondere (gelovige) scholen kregen voortaan evenveel overheidsgeld als openbare scholen (schoolstrijd).",
        uitleg: "Door de kiesrechtkwestie en de schoolstrijd tegelijk op te lossen kwam er politieke vrede en een volwaardige democratie tot stand."
      }
    ]
  });
})();
