/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §3.3 Gevolgen voor de bestemmingsgebieden
   buiteNLand 3 HAVO Hoofdstuk 3 (Migratie)
   ========================================================= */
DURU.register({
  id: "ak-h3-3",
  hoofdstuk: 3,
  paragraaf: "3.3",
  titel: "Gevolgen voor de bestemmingsgebieden",
  korteUitleg: "Multiculturele samenleving, integratie, acculturatie, segregatie en arbeidsmarktverhoudingen.",
  icoon: "🏙️",
  kleur: "h3-thema",
  theorie: `<h3>3.3 Gevolgen voor de bestemmingsgebieden</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Multiculturele samenleving, acculturatie, integratie, segregatie (ruimtelijk en sociaal), ontmoeting en spanningen.
</div>

<h4>1. De multiculturele samenleving</h4>
<p>Doordat steeds meer verschillende groepen mensen uit verschillende culturen in hetzelfde land komen te wonen, ontstaat een <b>multiculturele samenleving</b>. Hierin leven groepen met uiteenlopende culturele waarden, talen, godsdiensten en leefgewoonten naast en met elkaar. Dit zie je overal ter wereld vooral terug in de grote steden (zoals Amsterdam, Rotterdam, Londen, Parijs en New York), waar honderden nationaliteiten samenwonen.</p>

<h4>2. Cultuuroverdracht en aanpassing</h4>
<p>Hoe gaan immigranten en de ontvangende samenleving met elkaars cultuur om? Geografen onderscheiden twee stappen:</p>
<ul>
  <li><b>Acculturatie:</b> Wanneer kenmerken van een andere cultuur worden overgenomen. Dat gebeurt bijvoorbeeld wanneer migranten de taal van het bestemmingsgebied leren, of wanneer een migrant een restaurant of winkel opent met eten uit het herkomstgebied.</li>
  <li><b>Integratie:</b> Wanneer een migrant steeds meer gewoonten van het bestemmingsgebied overneemt.</li>
</ul>

<h4>3. Segregatie: Ruimtelijke scheiding in de stad</h4>
<p>Een belangrijk geografisch vraagstuk in steden is <b>segregatie</b>: het ruimtelijk of sociaal gescheiden wonen van bevolkingsgroepen op basis van etniciteit of inkomensniveau:</p>
<ul>
  <li><b>Ruimtelijke segregatie:</b> Bepaalde groepen concentreren zich in specifieke wijken (bijvoorbeeld door goedkope sociale huurwoningen), waardoor zogenoemde 'etnische wijken' ontstaan met eigen winkels en gebedshuizen.</li>
  <li><b>Sociale segregatie:</b> Mensen hebben in het dagelijks leven (school, sportclub, vriendenkring) nauwelijks contact met andere bevolkingsgroepen, waardoor wederzijds onbegrip en vooroordelen kunnen toenemen.</li>
</ul>`,
  vragen: [
    {
        "type": "mc",
        "vraag": "Wat verstaat men onder een <b>multiculturele samenleving</b>?",
        "opties": [
            "Een samenleving waarin mensen met verschillende culturele achtergronden samenleven",
            "Een land waarin iedereen exact dezelfde religie belijdt",
            "Een staat waar uitsluitend mensen wonen die in het land zelf geboren zijn",
            "Een samenleving zonder enige vorm van wetgeving of overheid"
        ],
        "antwoord": 0,
        "uitleg": "In een multiculturele samenleving wonen groepen met verschillende culturen, talen en gewoonten samen."
    },
    {
        "type": "mc",
        "vraag": "Wat is het verschil tussen <b>acculturatie</b> en <b>integratie</b>?",
        "opties": [
            "Acculturatie geldt alleen voor toeristen; integratie voor expats",
            "Acculturatie betekent dat kenmerken van een andere cultuur worden overgenomen (bijvoorbeeld de taal leren); integratie betekent dat een migrant steeds meer gewoonten van het bestemmingsgebied overneemt",
            "Acculturatie is verboden volgens de wet; integratie is verplicht",
            "Er bestaat geen enkel verschil tussen beide begrippen"
        ],
        "antwoord": 1,
        "uitleg": "Acculturatie is het overnemen van cultuurkenmerken door contact; integratie is het steeds meer overnemen van gewoonten van het bestemmingsgebied."
    },
    {
        "type": "waaronwaar",
        "vraag": "Acculturatie betekent dat culturen elkaar over en weer beïnvloeden door langdurig contact, bijvoorbeeld in eetcultuur en muziek.",
        "antwoord": true,
        "uitleg": "Waar. Acculturatie is wederzijdse culturele beïnvloeding."
    },
    {
        "type": "waaronwaar",
        "vraag": "Ruimtelijke segregatie betekent dat verschillende bevolkingsgroepen gelijkmatig over alle straten van de stad verspreid wonen.",
        "antwoord": false,
        "uitleg": "Niet waar. Segregatie betekent juist dat groepen gescheiden van elkaar wonen in aparte wijken of buurten."
    },
    {
        "type": "invoer",
        "vraag": "Hoe noemt men de ruimtelijke of sociale scheiding van bevolkingsgroepen in een stad?",
        "antwoord": "segregatie",
        "uitleg": "Segregatie is de scheiding van groepen in wijken of sociale kringen."
    },
    {
        "type": "invoer",
        "vraag": "Welke term beschrijft dat een migrant steeds meer de gewoonten van het bestemmingsgebied overneemt?",
        "antwoord": "integratie",
        "uitleg": "Integratie is het proces waarbij een migrant steeds meer gewoonten van het bestemmingsgebied overneemt."
    },
    {
        "type": "mc",
        "vraag": "Wat is een veelvoorkomende oorzaak van ruimtelijke segregatie in grote steden?",
        "opties": [
            "Wettelijke verplichting om per nationaliteit in een afgesloten wijk te wonen",
            "Het feit dat iedereen in een grote stad exact evenveel verdient",
            "Verschillen in inkomen en de concentratie van goedkope sociale huurwoningen in bepaalde buurten",
            "Het ontbreken van openbaar vervoer tussen stadswijken"
        ],
        "antwoord": 2,
        "uitleg": "Inkomensverschillen en de ligging van goedkope sociale huurwoningen sturen waar nieuwkomers kunnen wonen."
    },
    {
        "type": "mc",
        "vraag": "Welk voorbeeld illustreert het begrip <b>acculturatie</b> in Nederland?",
        "opties": [
            "Het sluiten van alle internationale restaurants in een stad",
            "Het verbieden van vreemde talen op straat",
            "De verplichte emigratie van buitenlandse werknemers",
            "Het overnemen van Surinaamse roti, Turkse pizza en Indische nasi in de dagelijkse Nederlandse keuken"
        ],
        "antwoord": 3,
        "uitleg": "Het opnemen van gerechten en gebruiken uit migrantenculturen in het dagelijks leven is een klassiek voorbeeld van acculturatie."
    }
]
});
