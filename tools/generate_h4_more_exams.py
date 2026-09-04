#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 5 new proeftoetsen (examen_19 to examen_23) for Economie HAVO 3, Hoofdstuk 4.1 & 4.2.
Strictly based on:
Pincode 7e editie Havo onderbouw - H4 Produceren 4.1-4.2.pdf
Each exam has exactly 20 questions: 12 mc, 4 waaronwaar, 2 invul, 2 open.
Quality gate compliant:
- Balanced mc answers (<= 40% per letter)
- At least 35% onwaar in waaronwaar
- No 'invoer' in exam mode
- Explanations >= 15 chars
- No question number prefixes
- No sleutelwoord leaks
"""

import json, os, re

exams = [
    {
        "id": "ex-h3-economie-19",
        "hoofdstuk": 4,
        "paragraaf": "4.1",
        "titel": "Proeftoets 19: Productieprocessen, Kringloop & Bedrijfskolom (4.1)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "🔄",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat laat de economische kringloop tussen gezinshuishoudens en bedrijfshuishoudens in de basis zien?",
                "opties": [
                    "Gezinnen leveren productiefactoren zoals arbeid en ontvangen loon; bedrijven leveren goederen en diensten en ontvangen geld voor consumptie.",
                    "Bedrijven betalen alleen belasting aan de overheid en gezinnen sparen al hun inkomsten op een buitenlandse bank.",
                    "Gezinnen produceren alle consumptiegoederen zelf thuis via zelfvoorziening zonder tussenkomst van geld.",
                    "Er is alleen een stroom van munten en biljetten zonder dat er ooit goederen worden overgedragen."
                ],
                "antwoord": 0,
                "uitleg": "In de kringloop leveren gezinnen arbeid/productiefactoren tegen beloning (loon), en kopen met dat geld goederen en diensten bij bedrijven."
            },
            {
                "type": "mc",
                "vraag": "In de kringloop worden twee stromen onderscheiden: geldstromen en reële stromen (goederen en diensten / productiefactoren). Welke stroom hoort bij het betalen van brood bij de bakker?",
                "opties": [
                    "Een geldstroom van het gezinshuishouden naar het bedrijfshuishouden.",
                    "Een goederenstroom van het gezinshuishouden naar het bedrijfshuishouden.",
                    "Een productiefactorstroom van het bedrijf naar het gezin.",
                    "Een overdrachtsstroom van de Europese Unie naar de bakker."
                ],
                "antwoord": 0,
                "uitleg": "Het afrekenen van een aankoop is een geldstroom van de consument (gezin) naar de onderneming (bedrijf)."
            },
            {
                "type": "mc",
                "vraag": "Waarom is er bij een gezin dat thuis groenten uit eigen tuin eet sprake van 'zelfvoorziening'?",
                "opties": [
                    "Zij produceren goederen voor eigen gebruik zonder tussenkomst van een bedrijf of markttransactie.",
                    "Omdat groente uit eigen tuin altijd vrijgesteld is van de Europese natuurwetgeving.",
                    "Omdat de groenten worden verkocht op een wekelijkse biologische boerenmarkt.",
                    "Zij moeten hiervoor verplicht een inschrijving hebben bij de Kamer van Koophandel."
                ],
                "antwoord": 0,
                "uitleg": "Zelfvoorziening betekent dat consumenten zelf goederen voortbrengen of diensten leveren voor hun eigen behoeften."
            },
            {
                "type": "mc",
                "vraag": "Bekijk de bedrijfskolom van katoen: Katoenboer (€ 0,40) → Stoffenweverij (€ 1,10) → Kledingfabriek (€ 3,50) → Groothandel (€ 5,00) → Kledingwinkel (€ 12,00). Wat is de toegevoegde waarde van de stoffenweverij?",
                "opties": [
                    "€ 0,70 per eenheid katoenstof.",
                    "€ 0,40 per eenheid katoenstof.",
                    "€ 1,10 per eenheid katoenstof.",
                    "€ 2,40 per eenheid katoenstof."
                ],
                "antwoord": 0,
                "uitleg": "Toegevoegde waarde = Verkoopprijs (€ 1,10) - Inkoopwaarde ruw katoen (€ 0,40) = € 0,70."
            },
            {
                "type": "mc",
                "vraag": "Welke schakel voegt in de hierboven genoemde katoen-bedrijfskolom in euro's de meeste waarde toe aan het uiteindelijke kledingstuk?",
                "opties": [
                    "De kledingwinkel (detailhandel)",
                    "De kledingfabriek",
                    "De stoffenweverij",
                    "De katoenboer"
                ],
                "antwoord": 0,
                "uitleg": "De kledingwinkel koopt in voor € 5,00 en verkoopt voor € 12,00. Toegevoegde waarde = € 7,00 (het hoogste bedrag in de kolom)."
            },
            {
                "type": "mc",
                "vraag": "Wat is het belangrijkste kenmerk van een 'dienstverlenend bedrijf' zoals een bezorgdienst of transportonderneming?",
                "opties": [
                    "Zij leveren niet-tastbare werkzaamheden voor anderen in plaats van fysieke tastbare goederen te fabriceren.",
                    "Zij mogen volgens de wet geen winst maken of personeel in dienst nemen.",
                    "Zij gebruiken uitsluitend de productiefactor natuur en geen kapitaalgoederen.",
                    "Zij verkopen uitsluitend grondstoffen aan fabrieken in het buitenland."
                ],
                "antwoord": 0,
                "uitleg": "Dienstverleners leveren onstoffelijke prestaties (zoals vervoer, advies of reparatie) voor klanten."
            },
            {
                "type": "mc",
                "vraag": "Een meubelmakerij koopt planken hout en schroeven in voor € 60. De timmerman maakt er een boekenrek van en verkoopt dit voor € 150. Hoe wordt het verschil van € 90 genoemd?",
                "opties": [
                    "De toegevoegde waarde van de meubelmakerij.",
                    "De afschrijvingskosten van de zaagmachine.",
                    "De inkoopwaarde van het boekenrek.",
                    "De consumentenprijs inclusief btw."
                ],
                "antwoord": 0,
                "uitleg": "Het verschil tussen de verkoopprijs en de ingekochte materialen/diensten van derden is de gecreëerde toegevoegde waarde (€ 150 - € 60 = € 90)."
            },
            {
                "type": "mc",
                "vraag": "Onder welke productiefactor valt een bestelbus die een schildersbedrijf gebruikt om verf en ladders naar klussen te rijden?",
                "opties": [
                    "Kapitaal (kapitaalgoederen)",
                    "Natuur",
                    "Arbeid",
                    "Ondernemerschap"
                ],
                "antwoord": 0,
                "uitleg": "Voertuigen, machines en gereedschappen die worden gebruikt in het productieproces vallen onder Kapitaal."
            },
            {
                "type": "mc",
                "vraag": "Wat is een kenmerkend voorbeeld van de productiefactor 'Natuur' bij een waterkrachtcentrale?",
                "opties": [
                    "Het stromende rivierwater dat de turbines aandrijft.",
                    "De stalen generator die elektriciteit opwekt.",
                    "Het maandsalaris van de controlerend ingenieur.",
                    "De lening die bij de bank is afgesloten voor de bouw van de dam."
                ],
                "antwoord": 0,
                "uitleg": "Natuur omvat alle onbewerkte natuurlijke elementen en energiebronnen, zoals stromend water, wind en zonlicht."
            },
            {
                "type": "mc",
                "vraag": "Waarom behoort een groothandel wel tot de bedrijfskolom van een product, maar een consument niet?",
                "opties": [
                    "De groothandel voegt waarde toe door opslag en transport tussen producent en winkelier, terwijl de consument het product verbruikt.",
                    "De consument betaalt contant geld en de groothandel gebruikt alleen girale overboekingen.",
                    "De groothandel produceert altijd alle grondstoffen zelfstandig in eigen fabrieken.",
                    "Omdat de wet bepaalt dat consumenten geen economische handelingen mogen verrichten."
                ],
                "antwoord": 0,
                "uitleg": "De bedrijfskolom omvat alle bedrijven die meewerken aan de totstandkoming en distributie tot de winkel. De consument gebruikt het product op."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er als een fabriek de assemblage van onderdelen niet meer met de hand laat doen, maar een gerobotiseerde lopende band installeert?",
                "opties": [
                    "Er vindt robotisering plaats, waardoor de arbeidsproductiviteit toeneemt.",
                    "De onderneming verandert van een productiebedrijf in een handelsonderneming.",
                    "De productiefactor kapitaal verdwijnt volledig uit het bedrijf.",
                    "De totale toegevoegde waarde van de fabriek wordt direct gereduceerd tot nul."
                ],
                "antwoord": 0,
                "uitleg": "Robotisering betekent dat robots werkzaamheden overnemen, wat zorgt voor een hogere productie per werknemer (arbeidsproductiviteit)."
            },
            {
                "type": "mc",
                "vraag": "Wat is de beloning die hoort bij de productiefactor 'Arbeid'?",
                "opties": [
                    "Loon of salaris voor de geleverde lichamelijke of geestelijke inspanning.",
                    "Pacht voor het gebruik van een perceel grond.",
                    "Rente over het geïnvesteerde vermogen in machines.",
                    "Winst die overblijft na aftrek van alle bedrijfskosten."
                ],
                "antwoord": 0,
                "uitleg": "De inkomensbeloning voor de productiefactor Arbeid is loon of salaris."
            },
            {
                "type": "waaronwaar",
                "vraag": "Wanneer Duru een taart bakt om op de verjaardag van haar broer op te eten, is dit een economische handeling van een productiebedrijf.",
                "antwoord": False,
                "uitleg": "Dit is zelfvoorziening binnen het gezinshuishouden; er is geen sprake van een bedrijf dat voor anderen produceert."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een supermarkt is een voorbeeld van een handelsonderneming omdat zij producten inkoopt en doorverkoopt zonder de producten te veranderen.",
                "antwoord": True,
                "uitleg": "Handelsondernemingen veranderen niets wezenlijks aan de goederen, maar zorgen voor distributie en assortiment."
            },
            {
                "type": "waaronwaar",
                "vraag": "De grond en het perceel waarop een fabriekscomplex gebouwd is vallen onder de productiefactor Kapitaal.",
                "antwoord": False,
                "uitleg": "Grond en vestigingsplaats zijn natuurlijke hulpbronnen en vallen onder de productiefactor Natuur."
            },
            {
                "type": "waaronwaar",
                "vraag": "Door mechanisatie in de landbouw, zoals het gebruik van maaidorsers, is de arbeidsproductiviteit per boer enorm gestegen ten opzichte van vroeger.",
                "antwoord": True,
                "uitleg": "Dankzij zware machines kan één boer tegenwoordig in dezelfde tijd vele malen meer graan oogsten dan met handarbeid."
            },
            {
                "type": "invul",
                "vraag": "Het maken van goederen of leveren van diensten door bedrijven voor anderen noemen we in de economie [produceren|productie].",
                "antwoord": "produceren|productie",
                "uitleg": "Produceren is het voortbrengen van goederen en diensten door ondernemingen voor afnemers."
            },
            {
                "type": "invul",
                "vraag": "De hoeveelheid producten of diensten die een werknemer in een bepaalde tijd kan maken heet de [arbeidsproductiviteit].",
                "antwoord": "arbeidsproductiviteit",
                "uitleg": "Arbeidsproductiviteit = productieomvang gedeeld door het aantal ingezette medewerkers."
            },
            {
                "type": "open",
                "vraag": "Een kaasfabriek produceert in een jaar tijd 450.000 kazen met behulp van 25 werknemers. Bereken de jaarlijkse arbeidsproductiviteit per werknemer en schrijf de formule op.",
                "sleutelwoorden": [
                    "450000 / 25",
                    "18000/18.000 kazen"
                ],
                "minTreffers": 1,
                "modelantwoord": "Formule: Arbeidsproductiviteit = Totale productie / Aantal medewerkers. Berekening: 450.000 / 25 = 18.000 kazen per werknemer per jaar.",
                "uitleg": "De totale output gedeeld door de personeelsomvang geeft de prestatie per werknemer."
            },
            {
                "type": "open",
                "vraag": "Noem de twee belangrijkste redenen waarom bedrijven streven naar een zo hoog mogelijke arbeidsproductiviteit.",
                "sleutelwoorden": [
                    "loonkosten per product dalen/lagere kosten",
                    "meer winst/betere concurrentiepositie/sneller produceren"
                ],
                "minTreffers": 1,
                "modelantwoord": "1. De loonkosten per product dalen omdat werknemers sneller werken. 2. Het bedrijf kan meer winst maken of scherpere verkoopprijzen hanteren ten opzichte van concurrenten.",
                "uitleg": "Hogere productiviteit verlaagt de kostprijs per product en verhoogt het rendement."
            }
        ]
    },
    {
        "id": "ex-h3-economie-20",
        "hoofdstuk": 4,
        "paragraaf": "4.2",
        "titel": "Proeftoets 20: Kostenstructuur, Vaste lasten & Afschrijvingsanalyse (4.2)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "📊",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Een kledingboetiek koopt 500 jurken in voor € 30 per stuk. De boetiek heeft daarnaast € 8.000 aan bedrijfskosten (huur pand, personeel, energie). Wat zijn de totale kosten van deze handelsonderneming?",
                "opties": [
                    "€ 23.000",
                    "€ 15.000",
                    "€ 8.000",
                    "€ 38.000"
                ],
                "antwoord": 0,
                "uitleg": "Totale kosten = Inkoopwaarde van de omzet (500 × € 30 = € 15.000) + Bedrijfskosten (€ 8.000) = € 23.000."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met de inkoopwaarde van de omzet als een meubelzaak in een maand 40% minder bankstellen verkoopt dan verwacht?",
                "opties": [
                    "De inkoopwaarde van de omzet daalt met 40% omdat er minder goederen zijn doorverkocht.",
                    "De inkoopwaarde van de omzet blijft exact gelijk aan de maandelijkse huur.",
                    "De inkoopwaarde van de omzet verdubbelt automatisch door inflatie.",
                    "De inkoopwaarde van de omzet verandert in een constante kostenpost."
                ],
                "antwoord": 0,
                "uitleg": "Inkoopwaarde van de omzet betreft de inkoop van daadwerkelijk verkochte stuks; verkoop je minder, dan daalt deze post rechtstreeks (variabel)."
            },
            {
                "type": "mc",
                "vraag": "Welke van de volgende kostenposten behoort tot de 'huisvestingskosten' van een bakkerij?",
                "opties": [
                    "De energierekening voor gas en elektriciteit om de bakkerij en winkel te verwarmen en te verlichten.",
                    "Het meel en de gist die nodig zijn voor het bakken van volkorenbrood.",
                    "De advertenties die wekelijks in de lokale huis-aan-huis krant worden geplaatst.",
                    "De rente over een banklening voor de aanschaf van een bezorgbus."
                ],
                "antwoord": 0,
                "uitleg": "Huisvestingskosten zijn alle uitgaven voor het bedrijfspand: huur/hypotheek, gemeentelijke heffingen, gas, water en elektriciteit."
            },
            {
                "type": "mc",
                "vraag": "Een schoenenfabriek heeft € 40.000 constante kosten per maand. De variabele kosten zijn € 15 per schoen. Wat zijn de totale kosten bij een productie van 2.000 paar schoenen?",
                "opties": [
                    "€ 70.000",
                    "€ 30.000",
                    "€ 40.000",
                    "€ 110.000"
                ],
                "antwoord": 0,
                "uitleg": "TVK = 2.000 × € 15 = € 30.000. TK = TCK (€ 40.000) + TVK (€ 30.000) = € 70.000."
            },
            {
                "type": "mc",
                "vraag": "Wat is de kostprijs per paar schoenen bij deze productie van 2.000 paar (TK = € 70.000)?",
                "opties": [
                    "€ 35,00",
                    "€ 15,00",
                    "€ 20,00",
                    "€ 55,00"
                ],
                "antwoord": 0,
                "uitleg": "Kostprijs per eenheid = TK / q = € 70.000 / 2.000 = € 35,00 per paar schoenen."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met de kostprijs per paar schoenen als de fabriek haar productie opschaalt naar 4.000 paar schoenen (TCK = € 40.000, variabele kosten € 15 per paar)?",
                "opties": [
                    "De kostprijs daalt van € 35,00 naar € 25,00 per paar.",
                    "De kostprijs stijgt naar € 50,00 per paar.",
                    "De kostprijs blijft exact gelijk op € 35,00 per paar.",
                    "De kostprijs daalt naar exact € 0,00 per paar."
                ],
                "antwoord": 0,
                "uitleg": "Bij 4.000 paar: TVK = 4.000 × € 15 = € 60.000. TK = € 40.000 + € 60.000 = € 100.000. Kostprijs = € 100.000 / 4.000 = € 25,00."
            },
            {
                "type": "mc",
                "vraag": "Waarom daalt de kostprijs per stuk bij een hogere productieomvang?",
                "opties": [
                    "Omdat de constante kosten over een groter aantal producten worden verdeeld (schaalvoordeel).",
                    "Omdat de overheid bij massaproductie de btw op grondstoffen kwijtscheldt.",
                    "Omdat de variabele kosten per stuk automatisch nul worden.",
                    "Omdat de werknemers bij meer productie geen salaris meer ontvangen."
                ],
                "antwoord": 0,
                "uitleg": "De vaste lasten (TCK) blijven gelijk en worden uitgesmeerd over meer stuks, waardoor TCK / q daalt."
            },
            {
                "type": "mc",
                "vraag": "Een drukkerij schaft een industriële snijmachine aan voor € 48.000. De machine gaat 6 jaar mee en de verwachte restwaarde is € 6.000. Wat is het jaarlijkse afschrijvingsbedrag?",
                "opties": [
                    "€ 7.000 per jaar",
                    "€ 8.000 per jaar",
                    "€ 6.000 per jaar",
                    "€ 42.000 per jaar"
                ],
                "antwoord": 0,
                "uitleg": "Afschrijving per jaar = (€ 48.000 - € 6.000) / 6 = € 42.000 / 6 = € 7.000."
            },
            {
                "type": "mc",
                "vraag": "Onder welke hoofdcategorie van kosten vallen de jaarlijkse afschrijvingskosten van een machine in de boekhouding?",
                "opties": [
                    "Constante kosten, want de afschrijving wordt elk jaar als vast bedrag ingeboekt ongeacht de productie.",
                    "Variabele kosten, want machines slijten alleen als het regent.",
                    "Inkoopwaarde van de omzet, want de machine is ooit ingekocht.",
                    "Verkoopkosten, want machines worden na afloop verkocht."
                ],
                "antwoord": 0,
                "uitleg": "Afschrijvingen zijn vaste, constante bedrijfskosten; het bedrag staat voor de gehele gebruiksduur vooraf vast."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de term 'restwaarde' van een kapitaalgoed precies?",
                "opties": [
                    "De geschatte verkoopopbrengst van het productiemiddel aan het einde van de gebruiksduur.",
                    "De totale winst die het apparaat heeft gegenereerd gedurende zijn levensduur.",
                    "De oorspronkelijke catalogusprijs op de aankoopfactuur.",
                    "Het bedrag dat aan reparaties is uitgegeven tijdens het eerste gebruiksjaar."
                ],
                "antwoord": 0,
                "uitleg": "De restwaarde is wat een machine, bestelauto of computer na afloop van de gebruiksjaren bij verkoop of inruil nog opbrengt."
            },
            {
                "type": "mc",
                "vraag": "In welke situatie kunnen loonkosten van personeel worden beschouwd als 'variabele kosten'?",
                "opties": [
                    "Wanneer personeel werkt op een nulurencontract of via een uitzendbureau en alleen wordt opgeroepen bij drukte.",
                    "Wanneer personeel een vast maandsalaris ontvangt met een vast contract voor onbepaalde tijd.",
                    "Wanneer de directeur van het bedrijf een vaste dertiende maand krijgt uitgekeerd.",
                    "Loonkosten kunnen volgens de economische theorie nooit variabel zijn."
                ],
                "antwoord": 0,
                "uitleg": "Oproepkrachten en uitzendkrachten worden flexibel ingezet; hun loonsom groeit mee met de productie (variabel)."
            },
            {
                "type": "mc",
                "vraag": "Wat zijn verkoopkosten voor een online kledingwinkel?",
                "opties": [
                    "De kosten voor verpakkingsdozen, verzendlabels en reclamecampagnes op internet.",
                    "De huur van het hoofdkantoor in Amsterdam.",
                    "De inkoopfacturen van ingekochte broeken en overhemden.",
                    "De hypotheekrente voor het centrale magazijnpand."
                ],
                "antwoord": 0,
                "uitleg": "Verkoopkosten zijn alle kosten die direct te maken hebben met de promotie en het afleveren van verkochte goederen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Wanneer een fabriek door een staking twee weken stilstaat en q = 0, dalen de totale kosten naar precies nul euro.",
                "antwoord": False,
                "uitleg": "Alleen de variabele kosten worden nul; de constante kosten (huur, afschrijving, vaste rente) lopen gewoon door."
            },
            {
                "type": "waaronwaar",
                "vraag": "De formule voor de kostprijs per product is de totale kosten vermenigvuldigd met het aantal geproduceerde goederen (TK × q).",
                "antwoord": False,
                "uitleg": "Fout, de kostprijs is Totale kosten GEDEELD door de productieomvang (TK / q)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een handelsonderneming maakt onderscheid tussen de inkoopwaarde van de omzet en overige bedrijfskosten om haar brutowinst en nettowinst te kunnen bepalen.",
                "antwoord": True,
                "uitleg": "Omzet - inkoopwaarde = brutowinst; brutowinst - bedrijfskosten = nettowinst."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het aanschaffen van een extra vrachtwagen leidt tot hogere constante kosten door extra jaarlijkse afschrijving en motorrijtuigenbelasting.",
                "antwoord": True,
                "uitleg": "Uitbreiding van kapitaalgoederen verhoogt de vaste jaarlijkse lasten (constante kosten)."
            },
            {
                "type": "invul",
                "vraag": "De kosten die samenhangen met het pand, zoals huur, erfpacht en energiekosten, noemen we [huisvestingskosten].",
                "antwoord": "huisvestingskosten",
                "uitleg": "Huisvestingskosten betreffen alle kosten van het onderkomen van het bedrijf."
            },
            {
                "type": "invul",
                "vraag": "Kosten die niet veranderen bij een verandering van de productieomvang heten [constante kosten|vaste kosten].",
                "antwoord": "constante kosten|vaste kosten",
                "uitleg": "Constante of vaste kosten blijven gelijk op de korte termijn."
            },
            {
                "type": "open",
                "vraag": "Een transportbedrijf koopt een nieuwe trekker voor € 120.000. Na 5 jaar trouwe dienst schat het bedrijf de restwaarde op € 30.000. Bereken de jaarlijkse afschrijvingskosten en geef de tussenstap.",
                "sleutelwoorden": [
                    "120000 - 30000 = 90000",
                    "90000 / 5",
                    "18000/18.000 euro"
                ],
                "minTreffers": 2,
                "modelantwoord": "Totale waardevermindering = € 120.000 - € 30.000 = € 90.000. Afschrijving per jaar = € 90.000 / 5 = € 18.000 per jaar.",
                "uitleg": "Afschrijving per jaar = (Aanschafwaarde - Restwaarde) / Aantal gebruiksjaren."
            },
            {
                "type": "open",
                "vraag": "Leg uit waarom de totale kosten van een fabriek NIET verdubbelen als de productie verdubbelt van 5.000 naar 10.000 stuks.",
                "sleutelwoorden": [
                    "constante kosten/vaste kosten blijven gelijk",
                    "alleen variabele kosten verdubbelen/stijgen"
                ],
                "minTreffers": 1,
                "modelantwoord": "Totale kosten bestaan uit constante en variabele kosten (TK = TCK + TVK). Bij een verdubbeling van de productie verdubbelen alleen de variabele kosten; de constante kosten blijven gelijk. Daardoor stijgen de totale kosten met minder dan 100%.",
                "uitleg": "Omdat TCK constant blijft, stijgt TK minder hard dan de productie."
            }
        ]
    },
    {
        "id": "ex-h3-economie-21",
        "hoofdstuk": 4,
        "paragraaf": "4.1",
        "titel": "Proeftoets 21: Productiefactoren KANO, Bedrijfstypen & Efficiëntie (4.1)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "🏭",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "De vier productiefactoren worden afgekort met KANO. Waar staat de letter 'O' voor in dit ezelsbruggetje?",
                "opties": [
                    "Ondernemerschap: het organiseren van productie en het dragen van financieel risico.",
                    "Omzetbelasting: het heffen van btw over verkochte consumptiegoederen.",
                    "Overheid: de wetgevende macht die subsidies verstrekt aan boeren.",
                    "Opleidingsniveau: het aantal gevolgde schooljaren van de werknemers."
                ],
                "antwoord": 0,
                "uitleg": "KANO staat voor Kapitaal, Arbeid, Natuur en Ondernemerschap."
            },
            {
                "type": "mc",
                "vraag": "Welke beloning ontvangt een ondernemer voor het inzetten van de productiefactor Ondernemerschap?",
                "opties": [
                    "Winst, als vergoeding voor het genomen risico en leidinggeven.",
                    "Pacht, voor het ter beschikking stellen van landbouwgrond.",
                    "Loon, als vast contractueel salaris per gewerkt uur.",
                    "Rente, als vergoeding van de spaarbank over zijn betaalrekening."
                ],
                "antwoord": 0,
                "uitleg": "De inkomensbeloning voor ondernemerschap is winst."
            },
            {
                "type": "mc",
                "vraag": "Een agrariër verhuurt 10 hectare akkerbouwgrond aan een naburige teler van suikerbieten. Welke vergoeding ontvangt de agrariër hiervoor?",
                "opties": [
                    "Pacht, dit is de economische beloning voor de productiefactor Natuur.",
                    "Loon, voor de arbeid die de bietenplant verricht.",
                    "Winst, berekend als percentage van de suikerprijs.",
                    "Dividend, als aandeelhouder van de suikerunie."
                ],
                "antwoord": 0,
                "uitleg": "De vergoeding voor het ter beschikking stellen van grond of natuurlijke hulpbronnen heet pacht."
            },
            {
                "type": "mc",
                "vraag": "Welke onderneming is een zuiver voorbeeld van een 'productieonderneming'?",
                "opties": [
                    "Een meubelfabriek die van ruw hout en bekledingsstof eetkamerstoelen fabriceert.",
                    "Een groentekraam op de markt die appels van een veiling doorverkoopt.",
                    "Een makelaarskantoor dat bemiddelt bij de aankoop van woningen.",
                    "Een kledingwinkel die merkkleding inkoopt bij groothandels."
                ],
                "antwoord": 0,
                "uitleg": "Een productieonderneming bewerkt grondstoffen en halffabricaten tot nieuwe goederen."
            },
            {
                "type": "mc",
                "vraag": "Wat is een belangrijk verschil tussen een handelsonderneming en een dienstverlenend bedrijf?",
                "opties": [
                    "Een handelsonderneming verkoopt tastbare fysieke goederen; een dienstverlener levert niet-tastbare werkzaamheden.",
                    "Een handelsonderneming maakt nooit winst; een dienstverlener maakt altijd 100% winst.",
                    "Een dienstverlener gebruikt uitsluitend grondstoffen uit het buitenland.",
                    "Een handelsonderneming heeft geen personeel of gebouw nodig."
                ],
                "antwoord": 0,
                "uitleg": "Handelaren leveren tastbare spullen door; dienstverleners leveren onstoffelijke diensten (zoals transport, knippen, repareren)."
            },
            {
                "type": "mc",
                "vraag": "In een fietsenfabriek werkten in 2022 40 monteurs die samen 16.000 fietsen assembleerden. In 2023 installeerde de fabriek robots: met 30 monteurs werden 18.000 fietsen gemaakt. Met hoeveel fietsen steeg de arbeidsproductiviteit per monteur per jaar?",
                "opties": [
                    "Met 200 fietsen per werknemer (van 400 naar 600 fietsen).",
                    "Met 400 fietsen per werknemer.",
                    "Met 1.000 fietsen per werknemer.",
                    "De arbeidsproductiviteit is niet gestegen maar gedaald."
                ],
                "antwoord": 0,
                "uitleg": "In 2022: 16.000 / 40 = 400 fietsen. In 2023: 18.000 / 30 = 600 fietsen. Stijging = 600 - 400 = 200 fietsen per werknemer."
            },
            {
                "type": "mc",
                "vraag": "Wat is de betekenis van 'mechanisatie' in een bakkerij?",
                "opties": [
                    "Het vervangen van handmatig kneden van deeg door elektrische deegkneedmachines.",
                    "Het vervangen van de bakker door een geautomatiseerde internetwebsite.",
                    "Het stoppen met het bakken van witbrood ten gunste van roggebrood.",
                    "Het ontslaan van alle winkeldames achter de toonbank."
                ],
                "antwoord": 0,
                "uitleg": "Mechanisatie is het inzetten van machines en apparaten om zware fysieke handarbeid over te nemen of te verlichten."
            },
            {
                "type": "mc",
                "vraag": "Welke stelling over de bedrijfskolom is economisch juist?",
                "opties": [
                    "In elke opeenvolgende schakel van de bedrijfskolom wordt economische waarde toegevoegd aan het product.",
                    "De bedrijfskolom bevat uitsluitend bedrijven uit de primaire landbouwsector.",
                    "Hoe meer schakels een bedrijfskolom telt, hoe goedkoper het eindproduct altijd wordt voor de consument.",
                    "De consument vormt de laatste en belangrijkste schakel binnen de bedrijfskolom."
                ],
                "antwoord": 0,
                "uitleg": "Elke schakel in de keten bewerkt, vervoert of distribueert het product en voegt zo waarde toe."
            },
            {
                "type": "mc",
                "vraag": "Waarom investeren moderne logistieke bedrijven in geautomatiseerde sorteersystemen voor pakketten?",
                "opties": [
                    "Om per werknemer meer pakketten per uur te kunnen verwerken (arbeidsproductiviteit verhogen).",
                    "Omdat kartonnen dozen niet meer met de hand mogen worden aangeraakt volgens de wet.",
                    "Om de energiekosten terug te brengen naar exact nul euro.",
                    "Omdat er dan geen kapitaalgoederen meer nodig zijn in het magazijn."
                ],
                "antwoord": 0,
                "uitleg": "Automatisering verhoogt de snelheid en capaciteit per werknemer, waardoor de stukskosten dalen."
            },
            {
                "type": "mc",
                "vraag": "Een meubelzaak verkoopt een eikenhouten tafel voor € 800 aan een consument. De meubelzaak kocht de tafel in bij de fabrikant voor € 450. Welke toegevoegde waarde levert de meubelzaak?",
                "opties": [
                    "€ 350",
                    "€ 450",
                    "€ 800",
                    "€ 1.250"
                ],
                "antwoord": 0,
                "uitleg": "Toegevoegde waarde = Verkoopprijs (€ 800) - Inkoopwaarde (€ 450) = € 350."
            },
            {
                "type": "mc",
                "vraag": "Welke productiefactor stelt een belegger beschikbaar als hij € 50.000 leent aan een startende onderneming om machines te kopen?",
                "opties": [
                    "Kapitaal (vermogen)",
                    "Arbeid",
                    "Natuur",
                    "Zelfvoorziening"
                ],
                "antwoord": 0,
                "uitleg": "Geld dat beschikbaar wordt gesteld om productiemiddelen te financieren valt onder de productiefactor Kapitaal."
            },
            {
                "type": "mc",
                "vraag": "Wat is de beloning die de belegger uit de vorige vraag ontvangt over zijn uitgeleende geld?",
                "opties": [
                    "Rente (interest)",
                    "Loon",
                    "Pacht",
                    "Accijns"
                ],
                "antwoord": 0,
                "uitleg": "De vergoeding voor het uitlenen of beschikbaar stellen van geldkapitaal is rente."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het koken van soep door een chef-kok in een restaurantkeuken is een vorm van zelfvoorziening.",
                "antwoord": False,
                "uitleg": "De kok kookt als beroep voor gasten tegen betaling; dit is produceren door een onderneming."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een verhoging van de arbeidsproductiviteit leidt er altijd toe dat een fabriek direct de helft van haar werknemers moet ontslaan.",
                "antwoord": False,
                "uitleg": "Hogere productiviteit kan ook gebruikt worden om bij gelijkblijvend personeel veel meer producten te fabriceren en de afzet te laten groeien."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij robotisering nemen computers en industriële robots taken over van menselijke arbeiders aan de productielijn.",
                "antwoord": True,
                "uitleg": "Robotisering is een vergevorderde vorm van automatisering waarbij robots fysieke en sturende taken uitvoeren."
            },
            {
                "type": "waaronwaar",
                "vraag": "De inkomensbeloning voor de productiefactor Ondernemerschap is winst.",
                "antwoord": True,
                "uitleg": "Ondernemers dragen financieel risico en worden beloond met de winst van de zaak."
            },
            {
                "type": "invul",
                "vraag": "De beloning voor de inzet van kapitaal in de vorm van geleend geld noemen we [rente|interest].",
                "antwoord": "rente|interest",
                "uitleg": "Rente is de inkomensbeloning voor de productiefactor Kapitaal."
            },
            {
                "type": "invul",
                "vraag": "Wanneer machines menselijke handkracht vervangen noemen we dat [mechanisatie].",
                "antwoord": "mechanisatie",
                "uitleg": "Mechanisatie is het inzetten van machines ter vervanging van fysieke arbeid."
            },
            {
                "type": "open",
                "vraag": "Een tapijtenweverij maakte in 2021 met 15 wevers 30.000 m² tapijt. In 2022 schaffen zij automatische weefgetouwen aan: 12 wevers produceren nu 36.000 m² tapijt. Bereken de arbeidsproductiviteit in m² tapijt per wever voor beide jaren.",
                "sleutelwoorden": [
                    "30000 / 15 = 2000",
                    "36000 / 12 = 3000"
                ],
                "minTreffers": 2,
                "modelantwoord": "In 2021: 30.000 / 15 = 2.000 m² per wever. In 2022: 36.000 / 12 = 3.000 m² per wever. De arbeidsproductiviteit steeg met 1.000 m² per wever.",
                "uitleg": "Arbeidsproductiviteit = Totale productie / Aantal medewerkers."
            },
            {
                "type": "open",
                "vraag": "Leg aan de hand van het begrip 'toegevoegde waarde' uit waarom een kopje cappuccino in een grand café € 4,00 kost, terwijl de inkoop van de melk en koffiebonen slechts € 0,35 bedraagt.",
                "sleutelwoorden": [
                    "waarde toevoegen/personeel/barista",
                    "huisvesting/huur/terras/sfeer/bedrijfskosten"
                ],
                "minTreffers": 1,
                "modelantwoord": "Het café voegt waarde toe door de bonen te malen, melk op te schuimen (arbeid van de barista), de ambiance en het terras te bieden (huisvesting/kapitaal) en service te verlenen. Uit die toegevoegde waarde (€ 3,65) moeten personeel, huur, energie en winst worden betaald.",
                "uitleg": "Toegevoegde waarde dekt de inzet van alle productiefactoren van de horecaonderneming."
            }
        ]
    },
    {
        "id": "ex-h3-economie-22",
        "hoofdstuk": 4,
        "paragraaf": "4.2",
        "titel": "Proeftoets 22: Berekeningen Kosten, Omzetwaarde & Afschrijvingen (4.2)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "🧮",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Een bakker koopt een professionele heteluchtoven voor € 24.000. De geschatte levensduur is 8 jaar. De schroothandelaar geeft na 8 jaar nog € 4.000 voor de oven (restwaarde). Hoeveel schrijft de bakker jaarlijks af?",
                "opties": [
                    "€ 2.500 per jaar",
                    "€ 3.000 per jaar",
                    "€ 4.000 per jaar",
                    "€ 20.000 per jaar"
                ],
                "antwoord": 0,
                "uitleg": "Jaarlijkse afschrijving = (€ 24.000 - € 4.000) / 8 = € 20.000 / 8 = € 2.500 per jaar."
            },
            {
                "type": "mc",
                "vraag": "Wat is de boekwaarde van deze heteluchtoven na afloop van het 3e gebruiksjaar (aanschaf € 24.000, jaarlijkse afschrijving € 2.500)?",
                "opties": [
                    "€ 16.500",
                    "€ 19.000",
                    "€ 21.500",
                    "€ 14.000"
                ],
                "antwoord": 0,
                "uitleg": "Na 3 jaar is afgeschreven: 3 × € 2.500 = € 7.500. Boekwaarde = € 24.000 - € 7.500 = € 16.500."
            },
            {
                "type": "mc",
                "vraag": "Een fabrikant van skateboards heeft de volgende kostenfunctie per maand: TK = 12.000 + 25q, waarin q het aantal skateboards is. Wat zijn de totale kosten bij het maken van 400 skateboards?",
                "opties": [
                    "€ 22.000",
                    "€ 12.000",
                    "€ 10.000",
                    "€ 32.000"
                ],
                "antwoord": 0,
                "uitleg": "TVK = 25 × 400 = € 10.000. TK = € 12.000 (TCK) + € 10.000 (TVK) = € 22.000."
            },
            {
                "type": "mc",
                "vraag": "Wat is de kostprijs per skateboard bij deze productie van 400 stuks (TK = € 22.000)?",
                "opties": [
                    "€ 55,00 per skateboard",
                    "€ 25,00 per skateboard",
                    "€ 30,00 per skateboard",
                    "€ 75,00 per skateboard"
                ],
                "antwoord": 0,
                "uitleg": "Kostprijs = TK / q = € 22.000 / 400 = € 55,00 per skateboard."
            },
            {
                "type": "mc",
                "vraag": "Wat zijn de constante kosten per skateboard bij 400 stuks als TCK = € 12.000 bedraagt?",
                "opties": [
                    "€ 30,00 per stuk",
                    "€ 25,00 per stuk",
                    "€ 12,00 per stuk",
                    "€ 45,00 per stuk"
                ],
                "antwoord": 0,
                "uitleg": "Constante kosten per stuk = TCK / q = € 12.000 / 400 = € 30,00 per stuk."
            },
            {
                "type": "mc",
                "vraag": "Stel dat de fabrikant de productie verdubbelt naar 800 skateboards. Wat worden dan de constante kosten per stuk (TCK = € 12.000)?",
                "opties": [
                    "€ 15,00 per stuk",
                    "€ 30,00 per stuk",
                    "€ 60,00 per stuk",
                    "€ 7,50 per stuk"
                ],
                "antwoord": 0,
                "uitleg": "Constante kosten per stuk = € 12.000 / 800 = € 15,00 per stuk (de vaste kosten per stuk halveren)."
            },
            {
                "type": "mc",
                "vraag": "Onder welke kostenpost vallen de rentelasten van een hypothecaire lening die is afgesloten voor de aankoop van een kantoorpand?",
                "opties": [
                    "Rentekosten (en onderdeel van de huisvestingskosten)",
                    "Loonkosten voor kantoormedewerkers",
                    "Verkoopkosten voor marketing",
                    "Inkoopwaarde van de voorraad"
                ],
                "antwoord": 0,
                "uitleg": "Rente over geleend geld voor een pand valt onder rentekosten en vormt een vast onderdeel van de huisvestingslasten."
            },
            {
                "type": "mc",
                "vraag": "Een winkelbedrijf betaalt een vast basissalaris aan 4 verkopers van in totaal € 10.000 per maand. Als er deze maand geen enkele klant in de winkel komt, hoeveel bedragen deze loonkosten dan?",
                "opties": [
                    "€ 10.000, want de vaste contractuele salarissen zijn constante kosten.",
                    "€ 0, want bij nul omzet hoeft er nooit loon betaald te worden.",
                    "€ 5.000, want de helft wordt door de gemeente betaald.",
                    "€ 20.000, wegens boetes van de vakbond."
                ],
                "antwoord": 0,
                "uitleg": "Vaste salarissen lopen door op basis van het arbeidscontract en zijn constante lasten."
            },
            {
                "type": "mc",
                "vraag": "Waarom schrijft een onderneming een computer in 3 jaar tijd af, terwijl een stenen magazijn in 30 jaar wordt afgeschreven?",
                "opties": [
                    "Een computer veroudert technisch veel sneller en raakt sneller achterhaald dan een duurzaam gebouw.",
                    "Omdat een computer geen elektriciteit gebruikt.",
                    "Omdat computers wettelijk verboden zijn in een magazijn.",
                    "Omdat stenen magazijnen geen aanschafwaarde hebben."
                ],
                "antwoord": 0,
                "uitleg": "De economische levensduur van ICT-apparatuur is kort door snelle technische ontwikkelingen."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met de totale variabele kosten (TVK) als de productie van 1.000 naar 3.000 stuks stijgt?",
                "opties": [
                    "De totale variabele kosten worden drie keer zo hoog (verdrievoudigen).",
                    "De totale variabele kosten blijven exact gelijk.",
                    "De totale variabele kosten dalen naar een derde.",
                    "De totale variabele kosten verdwijnen uit de balans."
                ],
                "antwoord": 0,
                "uitleg": "Variabele kosten zijn evenredig afhankelijk van het volume: 3x zoveel productie betekent 3x zoveel grondstoffen en variabele kosten."
            },
            {
                "type": "mc",
                "vraag": "Een juwelier koopt ringdoosjes, inpakpapier en fluwelen zakjes in. Hoe classificeert de juwelier deze kosten?",
                "opties": [
                    "Variabele verkoopkosten, want hoe meer sieraden er worden verkocht, hoe meer verpakkingsmateriaal er nodig is.",
                    "Constante huisvestingskosten, want de doosjes liggen in het pand.",
                    "Inkoopwaarde van de omzet, want het zijn gouden sieraden.",
                    "Afschrijvingskosten op de winkelvitrine."
                ],
                "antwoord": 0,
                "uitleg": "Verpakkingen en verzendmaterialen bewegen mee met het aantal verkopen en behoren tot de variabele verkoopkosten."
            },
            {
                "type": "mc",
                "vraag": "Wat is het gevolg voor een bedrijf als de rente op de kapitaalmarkt stijgt en het bedrijf een nieuwe lening moet afsluiten?",
                "opties": [
                    "De rentekosten van het bedrijf stijgen, waardoor de totale bedrijfskosten toenemen.",
                    "De inkoopwaarde van de omzet daalt automatisch.",
                    "De arbeidsproductiviteit van het personeel verdubbelt direct.",
                    "Het bedrijf hoeft geen afschrijvingen meer te berekenen."
                ],
                "antwoord": 0,
                "uitleg": "Hogere leenrente leidt direct tot hogere rentekosten voor de onderneming."
            },
            {
                "type": "waaronwaar",
                "vraag": "De restwaarde van een machine kan nooit lager zijn dan de aanschafwaarde.",
                "antwoord": True,
                "uitleg": "Machines slijten en dalen in waarde; de restwaarde na gebruik is altijd lager dan de oorspronkelijke aanschafprijs."
            },
            {
                "type": "waaronwaar",
                "vraag": "De totale constante kosten per maand stijgen automatisch als een winkelier in december meer omzet behaalt dan in november.",
                "antwoord": False,
                "uitleg": "De totale constante kosten (zoals de maandhuur van het pand) blijven precies gelijk."
            },
            {
                "type": "waaronwaar",
                "vraag": "De jaarlijkse afschrijvingskosten worden berekend door de restwaarde af te trekken van de aanschafwaarde en dit te delen door het aantal gebruiksjaren.",
                "antwoord": True,
                "uitleg": "Formule: Afschrijving per jaar = (Aanschafwaarde - Restwaarde) / Gebruiksjaren."
            },
            {
                "type": "waaronwaar",
                "vraag": "Verzendkosten voor het opsturen van online bestellingen naar klanten zijn een voorbeeld van constante bedrijfskosten.",
                "antwoord": False,
                "uitleg": "Verzendkosten stijgen met elk extra verzonden pakketje en zijn dus variabele verkoopkosten."
            },
            {
                "type": "invul",
                "vraag": "De boekhoudkundige waardevermindering van kapitaalgoederen over de tijd noemen we [afschrijving|afschrijven|afschrijvingskosten].",
                "antwoord": "afschrijving|afschrijven|afschrijvingskosten",
                "uitleg": "Afschrijving is het verdelen van de waardevermindering over de gebruiksjaren."
            },
            {
                "type": "invul",
                "vraag": "Het bedrag waarvoor een machine na afloop van de gebruiksperiode nog kan worden verkocht is de [restwaarde].",
                "antwoord": "restwaarde",
                "uitleg": "De restwaarde is de opbrengst bij inruil of verkoop aan het einde van de levensduur."
            },
            {
                "type": "open",
                "vraag": "Een grafisch ontwerper koopt een computerinstallatie voor € 3.600. Na 3 jaar intensief gebruik wordt de computer verkocht voor een restwaarde van € 600. Bereken de jaarlijkse afschrijvingskosten en geef de berekening weer.",
                "sleutelwoorden": [
                    "3600 - 600 = 3000",
                    "3000 / 3",
                    "1000/1.000 euro"
                ],
                "minTreffers": 2,
                "modelantwoord": "Totale afschrijving = € 3.600 - € 600 = € 3.000. Jaarlijkse afschrijving = € 3.000 / 3 = € 1.000 per jaar.",
                "uitleg": "Afschrijvingskosten per jaar = (Aanschafwaarde - Restwaarde) / Aantal gebruiksjaren."
            },
            {
                "type": "open",
                "vraag": "Een onderneming heeft € 60.000 constante kosten per jaar. De variabele kosten zijn € 20 per product. Bereken de kostprijs per eenheid bij een productie van 3.000 producten per jaar.",
                "sleutelwoorden": [
                    "3000 * 20 = 60000",
                    "60000 + 60000 = 120000",
                    "120000 / 3000",
                    "40/40 euro"
                ],
                "minTreffers": 2,
                "modelantwoord": "TVK = 3.000 × € 20 = € 60.000. TK = € 60.000 (TCK) + € 60.000 (TVK) = € 120.000. Kostprijs per product = € 120.000 / 3.000 = € 40,00.",
                "uitleg": "Totale kosten gedeeld door productieomvang levert de eenheidskostprijs op."
            }
        ]
    },
    {
        "id": "ex-h3-economie-23",
        "hoofdstuk": 4,
        "paragraaf": "4.1",
        "titel": "Proeftoets 23: Integratie Casussen H4.1 en H4.2 — Van Grondstof tot Kostprijs (Pincode)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "🏆",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Casus biologische boerderijwinkel: De boer verbouwt aardbeien op eigen land en verkoopt potjes aardbeienjam in zijn boerderijwinkel. Welke twee rollen combineert de boer hier in de bedrijfskolom?",
                "opties": [
                    "Oerproducent (aardbeien telen) en detaillist/winkelier (jam direct aan consumenten verkopen).",
                    "Groothandel en internationale importeur van tropisch fruit.",
                    "Uitsluitend consument en overheidsambtenaar.",
                    "Bankier en projectontwikkelaar."
                ],
                "antwoord": 0,
                "uitleg": "De boer teelt de grondstof (oerproductie) en verkoopt zelf aan de eindconsument (detailhandel); dit is ketenintegratie."
            },
            {
                "type": "mc",
                "vraag": "Wat is een groot voordeel voor de boer van het direct verkopen van jam in zijn eigen boerderijwinkel?",
                "opties": [
                    "Hij hoeft geen winstmarge af te staan aan tussenhandelaren zoals groothandels en supermarkten.",
                    "Hij hoeft geen aardbeien meer te plukken.",
                    "Hij mag gratis machines gebruiken van de overheid.",
                    "De grond waarop hij teelt heeft geen water of zonlicht meer nodig."
                ],
                "antwoord": 0,
                "uitleg": "Door het overslaan van tussenschakels behoudt de boer zelf de volledige toegevoegde waarde en winstmarge."
            },
            {
                "type": "mc",
                "vraag": "In de boerderijwinkel bedragen de personeelskosten voor winkelmedewerkers € 2.000 per maand. Tot welke kostencategorie van de boerderij behoren deze uitgaven?",
                "opties": [
                    "Loonkosten",
                    "Huisvestingskosten",
                    "Inkoopwaarde van de omzet",
                    "Rentekosten"
                ],
                "antwoord": 0,
                "uitleg": "Salarissen en vergoedingen voor personeel vallen onder de loonkosten."
            },
            {
                "type": "mc",
                "vraag": "Wat voor soort kosten zijn de glazen jampotjes en etiketten die per verkocht potje jam worden gebruikt?",
                "opties": [
                    "Variabele kosten, want hoe meer jam er wordt gemaakt en verkocht, hoe meer potjes en deksels er nodig zijn.",
                    "Constante kosten, want potjes bederven niet.",
                    "Afschrijvingskosten op de tractor.",
                    "Rentekosten over de hypotheek."
                ],
                "antwoord": 0,
                "uitleg": "Verpakkingsmateriaal dat per product wordt verbruikt is een typische variabele kostenpost."
            },
            {
                "type": "mc",
                "vraag": "De boer heeft een etiketteermachine aangeschaft voor € 10.000. De levensduur is 4 jaar en de restwaarde na 4 jaar is € 2.000. Hoeveel bedragen de afschrijvingskosten per jaar?",
                "opties": [
                    "€ 2.000 per jaar",
                    "€ 2.500 per jaar",
                    "€ 8.000 per jaar",
                    "€ 10.000 per jaar"
                ],
                "antwoord": 0,
                "uitleg": "Afschrijving per jaar = (€ 10.000 - € 2.000) / 4 = € 8.000 / 4 = € 2.000 per jaar."
            },
            {
                "type": "mc",
                "vraag": "Casus PostNL: PostNL zag de brievenbuspost krimpen en het aantal bezorgde pakketten stijgen. Waarom kan een krappe arbeidsmarkt leiden tot hogere bedrijfskosten voor een pakketbezorger?",
                "opties": [
                    "Omdat er een tekort is aan bezorgers, waardoor werkgevers hogere lonen en bonussen moeten bieden om personeel te vinden.",
                    "Omdat bestelbussen duurder worden als het regent.",
                    "Omdat er minder benzine in een vrachtwagen past.",
                    "Omdat de consument geen postzegels meer mag kopen."
                ],
                "antwoord": 0,
                "uitleg": "Een krappe arbeidsmarkt betekent schaarste aan arbeidskrachten, waardoor lonen stijgen en de loonkosten toenemen."
            },
            {
                "type": "mc",
                "vraag": "Welke kostenpost bij PostNL daalt automatisch wanneer het totale brievenbuspostvolume fors afneemt?",
                "opties": [
                    "De variabele transport- en sorteerkosten voor brieven.",
                    "De vaste huur van het hoofdkantoor in Den Haag.",
                    "De afschrijving op reeds aangeschafte sorteercentra.",
                    "De rente over bestaande langlopende bedrijfsleningen."
                ],
                "antwoord": 0,
                "uitleg": "Minder brieven betekent minder variabele handelingen, minder brandstof en minder variabele verwerkingskosten."
            },
            {
                "type": "mc",
                "vraag": "Casus Natrium-zwavelbatterij: Een wetenschappelijk artikel meldt een nieuwe superbatterij van goedkope grondstoffen (zwavel en natrium) die drie keer zoveel energie opslaat en langer meegaat. Welk economisch kostenvoordeel levert dit op voor autofabrikanten?",
                "opties": [
                    "De variabele materiaalkosten voor accupakketten dalen aanzienlijk, waardoor elektrische auto's goedkoper geproduceerd kunnen worden.",
                    "De autofabrikant hoeft geen werknemers meer in dienst te nemen.",
                    "De huur van de autofabriek daalt naar nul euro.",
                    "Er hoeft geen belasting meer over de auto betaald te worden."
                ],
                "antwoord": 0,
                "uitleg": "Goedkopere grondstoffen verlagen de inkoopwaarde en de variabele productiekosten per auto."
            },
            {
                "type": "mc",
                "vraag": "Wat is het gevolg voor de consument als autobatterijen een veel langere levensduur hebben?",
                "opties": [
                    "De jaarlijkse afschrijvingskosten van de elektrische auto dalen omdat de auto over meer jaren gebruikt kan worden.",
                    "De auto verbruikt per kilometer twee keer zoveel elektriciteit.",
                    "De auto mag niet meer op de openbare weg rijden.",
                    "De consument moet elk jaar een nieuwe batterij kopen."
                ],
                "antwoord": 0,
                "uitleg": "Een langere levensduur betekent dat het kapitaalgoed langer meegaat, waardoor de jaarlijkse waardevermindering (afschrijving) lager uitvalt."
            },
            {
                "type": "mc",
                "vraag": "Casus Duurzaamheid bij Volvo: Waarom kan de overstap naar duurzame bekleding uit gerecyclede petflessen de maatschappelijke kosten verlagen?",
                "opties": [
                    "Omdat er minder milieuschade en broeikasgassen ontstaan door de veehouderij en afvalplastic wordt hergebruikt.",
                    "Omdat petflessen gratis uit de kraan stromen.",
                    "Omdat koeien dan geen gras meer eten.",
                    "Omdat elektrische auto's dan geen banden meer nodig hebben."
                ],
                "antwoord": 0,
                "uitleg": "Minder afhankelijkheid van intensieve veeteelt vermindert de ecologische voetafdruk en maatschappelijke milieukosten."
            },
            {
                "type": "mc",
                "vraag": "Wat is het verschil tussen brutowinst en nettowinst bij een onderneming?",
                "opties": [
                    "Brutowinst is omzet minus inkoopwaarde; nettowinst is wat er echt overblijft nadat alle overige bedrijfskosten van de brutowinst zijn afgetrokken.",
                    "Brutowinst is altijd lager dan de nettowinst.",
                    "Nettowinst is het bedrag dat aan btw wordt afgedragen aan de overheid.",
                    "Brutowinst is het totale spaargeld van de directeur bij de bank."
                ],
                "antwoord": 0,
                "uitleg": "Brutowinst = Omzet - Inkoopwaarde van de omzet. Nettowinst = Brutowinst - Bedrijfskosten."
            },
            {
                "type": "mc",
                "vraag": "Waarom is kennis van de kostprijs per product noodzakelijk voordat een ondernemer zijn uiteindelijke verkoopprijs vaststelt?",
                "opties": [
                    "Om te zorgen dat de verkoopprijs hoog genoeg is om alle kosten te dekken en een gewenste winstmarge over te houden.",
                    "Omdat de bank de kostprijs verplicht stelt voor het openen van een betaalrekening.",
                    "Omdat de consument aan de kassa altijd om de kostprijs vraagt.",
                    "Om te voorkomen dat het product te snel uitverkocht raakt."
                ],
                "antwoord": 0,
                "uitleg": "Verkoopprijs = Kostprijs + Winstopslag (+ btw voor consumenten). Zonder kostprijs kan men verlies lijden."
            },
            {
                "type": "waaronwaar",
                "vraag": "De rente die een onderneming maandelijks aan de bank betaalt voor een lening voor machines is een variabele kostenpost.",
                "antwoord": False,
                "uitleg": "Rentekosten over een lening liggen contractueel vast en zijn een constante kostenpost."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een winkelier die artikelen inkoopt voor € 50 en verkoopt voor € 90 heeft een brutowinst van € 40 per artikel.",
                "antwoord": True,
                "uitleg": "Brutowinst per artikel = Verkoopprijs (€ 90) - Inkoopprijs (€ 50) = € 40."
            },
            {
                "type": "waaronwaar",
                "vraag": "Als een bedrijf 10 jaar lang jaarlijks € 3.000 afschrijft op een machine met € 0 restwaarde, was de aanschafwaarde € 30.000.",
                "antwoord": True,
                "uitleg": "10 jaar × € 3.000 = € 30.000 totale aanschafwaarde."
            },
            {
                "type": "waaronwaar",
                "vraag": "De productiefactor Natuur levert als inkomensbeloning winst op.",
                "antwoord": False,
                "uitleg": "De beloning voor de productiefactor Natuur is pacht. Winst hoort bij Ondernemerschap."
            },
            {
                "type": "invul",
                "vraag": "De inkomensbeloning die hoort bij de productiefactor Natuur noemen we [pacht].",
                "antwoord": "pacht",
                "uitleg": "Pacht is de vergoeding voor het gebruik van grond en natuurlijke elementen."
            },
            {
                "type": "invul",
                "vraag": "Het voordeel dat ontstaat wanneer vaste kosten over steeds grotere productieaantallen worden verdeeld heet [schaalvoordeel|schaalvoordelen].",
                "antwoord": "schaalvoordeel|schaalvoordelen",
                "uitleg": "Schaalvoordelen zorgen voor lagere vaste kosten per eenheid bij schaalvergroting."
            },
            {
                "type": "open",
                "vraag": "Een pizzeria heeft € 4.500 constante kosten per maand (huur, afschrijving ovens, verzekering). De variabele kosten voor meel, kaas, tomaten en bezorging zijn € 2,50 per pizza. Bereken de kostprijs per pizza als er deze maand 3.000 pizza's worden gebakken.",
                "sleutelwoorden": [
                    "3000 * 2,50 = 7500",
                    "4500 + 7500 = 12000",
                    "12000 / 3000",
                    "4/4 euro/€ 4"
                ],
                "minTreffers": 2,
                "modelantwoord": "TVK = 3.000 × € 2,50 = € 7.500. TK = € 4.500 (TCK) + € 7.500 (TVK) = € 12.000. Kostprijs per pizza = € 12.000 / 3.000 = € 4,00 per pizza.",
                "uitleg": "Totale kosten zijn € 12.000, gedeeld door 3.000 stuks geeft een kostprijs van € 4,00."
            },
            {
                "type": "open",
                "vraag": "Noem de vier categorieën waarin bedrijfskosten van een onderneming volgens het lesboek worden onderverdeeld en geef bij één categorie een concreet voorbeeld.",
                "sleutelwoorden": [
                    "loonkosten",
                    "huisvestingskosten",
                    "verkoopkosten",
                    "rentekosten"
                ],
                "minTreffers": 3,
                "modelantwoord": "De vier categorieën zijn: 1. Loonkosten (bv. salaris van winkelpersoneel), 2. Huisvestingskosten (bv. huur van het bedrijfspand of energiekosten), 3. Verkoopkosten (bv. reclame en verzenddozen), 4. Rentekosten (bv. rente over een banklening).",
                "uitleg": "Dit zijn de vier officiële bedrijfskostencategorieën uit het tekstboek Pincode."
            }
        ]
    }
]

# Balance mc options in each exam
for ex in exams:
    mc_idx = 0
    for v in ex["vragen"]:
        if v["type"] == "mc":
            opts = v["opties"]
            ans = v["antwoord"]
            target = mc_idx % len(opts)
            mc_idx += 1
            if target != ans:
                correct = opts[ans]
                other = opts[target]
                opts[target] = correct
                opts[ans] = other
                v["antwoord"] = target

base_dir = "havo3/economie/js/data"
for i, ex in enumerate(exams, start=19):
    fn = f"{base_dir}/examen_{i}.js"
    content = f"/* =========================================================\n" \
              f"   Duru's Economie (HAVO 3) — {ex['titel']}\n" \
              f"   ========================================================= */\n" \
              f"DURU.registerExamen(\n" + json.dumps(ex, indent=2, ensure_ascii=False) + "\n);\n"
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {fn} ({len(ex['vragen'])} vragen)")

