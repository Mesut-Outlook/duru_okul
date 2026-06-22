/* Extra Proeftoets 31 — Inkomstenbelasting & Loonbelasting II */
DURU.registerExamen({
  id: "ex-extra-inkomsten-loonbelasting-2",
  titel: "Extra Proeftoets 31 — Inkomstenbelasting & Loonbelasting II",
  vak: "Economie · Belastingen",
  icoon: "💶",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is het verschil tussen brutoloon en nettoloon?",
      opties: [
        "Brutoloon is het salaris dat je op je bankrekening krijgt; nettoloon is vóór aftrek van belastingen.",
        "Brutoloon is het afgesproken loon vóór aftrek van belastingen; nettoloon is het bedrag dat je daadwerkelijk ontvangt.",
        "Er is geen verschil; het zijn twee woorden voor precies hetzelfde bedrag.",
        "Nettoloon is inclusief btw en brutoloon is exclusief btw."
      ],
      antwoord: 1,
      uitleg: "Het **brutoloon** is het loon dat je met je werkgever afspreekt. Hier moeten nog belastingen en premies vanaf. Het **nettoloon** is wat er overblijft en op je bankrekening wordt gestort."
    },
    {
      type: "waaronwaar",
      vraag: "Het nettoloon van een werknemer is altijd hoger dan het brutoloon.",
      antwoord: false,
      uitleg: "Onwaar. Het nettoloon is altijd **lager** dan het brutoloon, omdat er loonbelasting en premies van het brutoloon worden ingehouden."
    },
    {
      type: "invul",
      vraag: "Welke overheidsinstantie is in Nederland verantwoordelijk voor het heffen en innen van belastingen?",
      antwoord: "Belastingdienst|de Belastingdienst|fiscus|de fiscus",
      uitleg: "De **Belastingdienst** (ook wel de fiscus genoemd) is de instantie die de belastingen namens de rijksoverheid regelt en collecteert."
    },
    {
      type: "mc",
      vraag: "Waarom houdt een werkgever maandelijks loonbelasting in op het brutoloon?",
      opties: [
        "Zodat de werkgever dit geld zelf als winst kan houden.",
        "Zodat de werknemer aan het eind van het jaar niet in één keer een groot bedrag aan inkomstenbelasting hoeft te betalen.",
        "Omdat de werkgever hiermee de btw van de winkel betaalt.",
        "Dat doet een werkgever niet; de werknemer moet dit elke maand zelf overmaken."
      ],
      antwoord: 1,
      uitleg: "De loonbelasting dient als een **voorheffing**. Door dit maandelijks in te houden, betaal je de inkomstenbelasting in kleine stukjes vooruit, wat achteraf grote betalingsproblemen voorkomt."
    },
    {
      type: "waaronwaar",
      vraag: "Loonbelasting is een directe belasting omdat je deze rechtstreeks over je inkomen betaalt.",
      antwoord: true,
      uitleg: "Waar. Belastingen over inkomen, winst en vermogen die je rechtstreeks aan de overheid betaalt, zijn **directe belastingen**."
    },
    {
      type: "mc",
      vraag: "Stel, Duru verdient een brutoloon van € 800,- per maand. De werkgever houdt € 120,- aan loonbelasting en premies in. Hoeveel nettoloon krijgt Duru op haar bankrekening?",
      opties: [
        "€ 920,-",
        "€ 800,-",
        "€ 680,-",
        "€ 120,-"
      ],
      antwoord: 2,
      uitleg: "Nettoloon = Brutoloon - Inhoudingen. Dus € 800 - € 120 = **€ 680,-**."
    },
    {
      type: "invul",
      vraag: "Loonbelasting wordt ingehouden op je salaris als vooruitbetaling. Welk economisch woord gebruiken we voor deze vooruitbetaling?",
      antwoord: "voorheffing|voorafheffing|voorheffingen",
      uitleg: "Loonbelasting is een **voorheffing** (vooruitbetaling) op de uiteindelijke inkomstenbelasting."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er als aan het eind van het jaar blijkt dat er via de loonbelasting te veel belasting is ingehouden op je loon?",
      opties: [
        "Dan ben je dat geld kwijt; de Belastingdienst geeft nooit geld terug.",
        "Dan moet je alsnog een boete betalen.",
        "Dan krijg je het te veel betaalde bedrag terug van de Belastingdienst.",
        "Dan krijgt je werkgever dat geld als bonus."
      ],
      antwoord: 2,
      uitleg: "Als er te veel is ingehouden, krijg je het verschil **terug** na het doen van je jaarlijkse belastingaangifte."
    },
    {
      type: "waaronwaar",
      vraag: "Een indirecte belasting betaal je rechtstreeks over je salaris aan de Belastingdienst.",
      antwoord: false,
      uitleg: "Onwaar. Een indirecte belasting zit verwerkt in de prijs van goederen en diensten (zoals btw en accijns). Belasting over je salaris is een **directe** belasting."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende belastingen is een directe belasting?",
      opties: [
        "Btw op een nieuwe spelcomputer.",
        "Inkomstenbelasting over je salaris.",
        "Accijns op een blikje cola.",
        "Invoerrechten op kleding uit Amerika."
      ],
      antwoord: 1,
      uitleg: "**Inkomstenbelasting** betaal je rechtstreeks over je eigen inkomen aan de fiscus, dus dit is een directe belasting."
    },
    {
      type: "invul",
      vraag: "Hoe heet het loon dat in je arbeidsovereenkomst staat, dus het bedrag waar nog geen belasting van af is gehaald?",
      antwoord: "brutoloon|bruto loon|bruto-loon",
      uitleg: "Het loon vóór aftrek van belastingen en premies heet het **brutoloon**."
    },
    {
      type: "open",
      vraag: "Leg uit waarom het nettoloon dat je ontvangt lager is dan het brutoloon dat je met je werkgever hebt afgesproken.",
      sleutelwoorden: ["loonbelasting/loonheffing", "premies/volksverzekeringen", "afgedragen/ingehouden", "belastingdienst/overheid"],
      minTreffers: 2,
      modelantwoord: "De werkgever is wettelijk verplicht om een deel of het brutoloon in te houden voor de loonbelasting en premies volksverzekeringen. Dit ingehouden deel wordt rechtstreeks afgedragen aan de Belastingdienst. Wat overblijft is het nettoloon.",
      uitleg: "Het verschil tussen bruto en netto ontstaat door de verplichte inhouding van loonheffing (belasting en premies)."
    },
    {
      type: "mc",
      vraag: "Wie is er verantwoordelijk voor het daadwerkelijk overmaken van de ingehouden loonbelasting naar de Belastingdienst?",
      opties: [
        "De werknemer zelf, elke maand via een acceptgiro.",
        "De bank van de werknemer.",
        "De werkgever.",
        "De gemeente waarin de werknemer woont."
      ],
      antwoord: 2,
      uitleg: "De **werkgever** houdt de loonbelasting in en zorgt ervoor dat dit geld netjes wordt afgedragen aan de Belastingdienst."
    },
    {
      type: "waaronwaar",
      vraag: "Loonbelasting is een jaarlijkse belasting die je pas achteraf over het hele jaar berekent en betaalt.",
      antwoord: false,
      uitleg: "Onwaar. **Inkomstenbelasting** wordt over het hele jaar berekend. **Loonbelasting** wordt elke maand (per loonperiode) direct ingehouden op je salaris."
    },
    {
      type: "open",
      vraag: "Wat betekent het dat de loonbelasting een 'voorheffing' is op de inkomstenbelasting?",
      sleutelwoorden: ["vooruitbetaling/vooraf betaald", "maandelijks ingehouden/elk loonstrookje", "eind van het jaar verrekenen", "inkomstenbelasting definitief"],
      minTreffers: 2,
      modelantwoord: "Loonbelasting is een voorheffing omdat het een maandelijks voorschot is op de inkomstenbelasting. Aan het eind van het jaar berekent de Belastingdienst de definitieve inkomstenbelasting en verrekent dit met de al betaalde loonbelasting.",
      uitleg: "Loonbelasting is een vooruitbetaling zodat je achteraf niet in één keer de hele inkomstenbelasting hoeft te betalen."
    }
  ]
});
