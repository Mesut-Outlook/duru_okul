#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 4 new proeftoetsen (examen_24 to examen_27) for Economie HAVO 3, Hoofdstuk 4.
Strictly based on:
- Pincode 7e editie Havo onderbouw - H4 Produceren (4.1, 4.2, 4.3)
Quality gate compliant:
- Balanced mc answers (<= 40% per letter, exactly 3 A, 3 B, 3 C, 3 D)
- At least 35% onwaar in waaronwaar (50% onwaar: 2 True, 2 False)
- No 'invoer' in exam mode (only mc, waaronwaar, invul, open)
- Explanations >= 15 chars
- No question number prefixes
- No sleutelwoord leaks
- Exactly 20 questions per exam
"""

import json
import os

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/economie/js/data"

exams = [
    # Examen 24: 4.2 Bedrijfskosten, Arbeidsmarkt & Afschrijvingen
    {
        "id": "ex-h3-economie-24",
        "hoofdstuk": 4,
        "paragraaf": "4.2",
        "titel": "Proeftoets 24: Bedrijfskosten, Arbeidsmarkt & Afschrijvingen (Pincode 4.2)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "💼",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Welke kostenpost behoort volgens het Pincode-handboek tot de verkoopkosten van een onderneming?",
                "opties": [
                    "Reclamefolders, beursstands en online advertenties ter werving van klanten",
                    "De maandelijkse huur van het administratieve kantoorpand",
                    "De rente betaald over een hypothecaire lening bij de bank",
                    "Het vaste basissalaris van de financieel administrateur"
                ],
                "antwoord": 0,
                "uitleg": "Verkoopkosten zijn alle uitgaven die gemaakt worden om de afzet te bevorderen, zoals reclame, stands en promotiemateriaal."
            },
            {
                "type": "mc",
                "vraag": "Een verfwinkel koopt een automatische verfmengmachine voor € 30.000. De geschatte levensduur is 5 jaar en de restwaarde bedraagt € 5.000. Wat zijn de jaarlijkse afschrijvingskosten?",
                "opties": [
                    "€ 6.000 per jaar",
                    "€ 5.000 per jaar",
                    "€ 7.000 per jaar",
                    "€ 25.000 per jaar"
                ],
                "antwoord": 1,
                "uitleg": "Afschrijving per jaar = (Aanschafprijs € 30.000 - Restwaarde € 5.000) / 5 jaar = € 25.000 / 5 = € 5.000 per jaar."
            },
            {
                "type": "mc",
                "vraag": "Wat verstaan economen onder een 'krappe arbeidsmarkt' zoals beschreven in het praktijkvoorbeeld over PostNL?",
                "opties": [
                    "Er is massale werkloosheid en werkgevers kunnen de lonen flink verlagen",
                    "Bedrijven mogen volgens de wet geen uitzendkrachten meer inhuren",
                    "Er zijn veel openstaande vacatures en relatief weinig werkzoekenden om ze te vervullen",
                    "Alle postbezorgers werken uitsluitend nog als zelfstandige zonder personeel"
                ],
                "antwoord": 2,
                "uitleg": "Bij een krappe arbeidsmarkt is er een tekort aan arbeidskrachten ten opzichte van het aantal openstaande banen."
            },
            {
                "type": "mc",
                "vraag": "Waarom leidt een hoog ziekteverzuim in een krappe arbeidsmarkt tot extra hoge bedrijfskosten?",
                "opties": [
                    "Omdat de restwaarde van kapitaalgoederen door ziekteverzuim onmiddellijk afneemt",
                    "Omdat de overheid bij ziekteverzuim een verhoogd btw-tarief van 21% oplegt aan het bedrijf",
                    "Omdat werknemers bij ziekte automatisch een dubbel salaris krijgen uitbetaald door de bank",
                    "Omdat de werkgever het loon doorbetaalt en tegelijkertijd dure vervangers of overwerk moet inzetten"
                ],
                "antwoord": 3,
                "uitleg": "De werkgever betaalt het loon door én moet bij personeelsschaarste dure invalkrachten inhuren of overuren betalen."
            },
            {
                "type": "mc",
                "vraag": "Onder welke categorie bedrijfskosten valt de hypotheekrente die een bedrijf maandelijks betaalt over de lening voor haar bedrijfspand?",
                "opties": [
                    "Financieringskosten (rentekosten)",
                    "Verkoopkosten",
                    "Huisvestingskosten",
                    "Loonkosten"
                ],
                "antwoord": 0,
                "uitleg": "Rente over leningen en hypotheken behoort tot de financieringskosten (rentekosten) van een onderneming."
            },
            {
                "type": "mc",
                "vraag": "In welk geval worden loonkosten door een onderneming aangemerkt als variabele kosten?",
                "opties": [
                    "Wanneer vaste kantoormedewerkers een maandelijks salaris conform cao ontvangen",
                    "Wanneer oproepkrachten met een nulurencontract alleen worden ingezet tijdens piekdrukte",
                    "Wanneer de directeur een vast managementinkomen ontvangt ongeacht de productie",
                    "Wanneer werknemers een arbeidsovereenkomst voor onbepaalde tijd bezitten"
                ],
                "antwoord": 1,
                "uitleg": "Bij een nulurencontract of uitzendkrachten stijgen of dalen de loonkosten direct met het productievolume."
            },
            {
                "type": "mc",
                "vraag": "Waarom is de afschrijvingsperiode van kantoorcomputers en software meestal veel korter dan die van een bedrijfsauto?",
                "opties": [
                    "Omdat bedrijfsauto's wettelijk nooit in economische waarde mogen dalen",
                    "Omdat computers en software uitsluitend als variabele kosten worden geboekt",
                    "Omdat computers door razendsnelle technische ontwikkelingen veel sneller economisch verouderd zijn",
                    "Omdat de restwaarde van computers altijd gelijk is aan de oorspronkelijke aanschafprijs"
                ],
                "antwoord": 2,
                "uitleg": "Computers verouderen technologisch veel sneller dan voertuigen en moeten daarom na kortere tijd vervangen worden."
            },
            {
                "type": "mc",
                "vraag": "Een bezorgdienst koopt een elektrische bestelauto voor € 42.000. De restwaarde na 4 jaar is € 10.000. Wat is de boekwaarde van deze auto aan het einde van het tweede gebruiksjaar?",
                "opties": [
                    "€ 34.000",
                    "€ 18.000",
                    "€ 32.000",
                    "€ 26.000"
                ],
                "antwoord": 3,
                "uitleg": "Jaarlijkse afschrijving = (€ 42.000 - € 10.000) / 4 = € 8.000 per jaar. Einde jaar 2 = € 42.000 - (2 × € 8.000) = € 26.000."
            },
            {
                "type": "mc",
                "vraag": "Tot welke van de vier bedrijfskostengroepen behoort de maandelijkse rekening voor elektriciteit, gas en water van een werkplaats?",
                "opties": [
                    "Huisvestingskosten",
                    "Verkoopkosten",
                    "Financieringskosten",
                    "Loonkosten"
                ],
                "antwoord": 0,
                "uitleg": "Huur, gas, water, elektriciteit en onderhoud van het pand vallen onder de huisvestingskosten."
            },
            {
                "type": "mc",
                "vraag": "Een meubelbedrijf koopt een freesmachine voor € 80.000. Er wordt jaarlijks € 12.000 op afgeschreven. Na hoeveel jaar bereikt de machine haar restwaarde van € 8.000?",
                "opties": [
                    "Na 4 jaar",
                    "Na 6 jaar",
                    "Na 8 jaar",
                    "Na 5 jaar"
                ],
                "antwoord": 1,
                "uitleg": "Totaal af te schrijven bedrag = € 80.000 - € 8.000 = € 72.000. Aantal jaren = € 72.000 / € 12.000 = 6 jaar."
            },
            {
                "type": "mc",
                "vraag": "Welk belangrijk financieel voordeel heeft een onderneming wanneer zij flexkrachten met een nulurencontract inzet in plaats van louter personeel in vaste dienst?",
                "opties": [
                    "Flexkrachten zijn wettelijk verplicht om zonder enige pauze te werken",
                    "Het bedrijf hoeft over de omzet van flexkrachten geen omzetbelasting af te dragen",
                    "De loonkosten bewegen flexibel mee met de vraag en er worden geen lonen betaald bij stilstand",
                    "De vaste kosten van het machinepark dalen daardoor automatisch naar nul euro"
                ],
                "antwoord": 2,
                "uitleg": "Bij nulurencontracten betaal je alleen gewerkte uren; bij een dip in orders ontstaan er geen doorlopende loonkosten."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met de jaarlijkse afschrijvingskosten als een ondernemer besluit een machine twee jaar langer te blijven gebruiken dan gepland, bij gelijke restwaarde?",
                "opties": [
                    "De jaarlijkse afschrijvingskosten verdubbelen met onmiddellijke ingang",
                    "De afschrijvingskosten worden automatisch omgezet in variabele kosten",
                    "De oorspronkelijke aanschafprijs van de machine stijgt met terugwerkende kracht",
                    "De jaarlijkse afschrijvingskosten dalen omdat het af te schrijven bedrag over meer jaren wordt verdeeld"
                ],
                "antwoord": 3,
                "uitleg": "Door de noemer (gebruiksjaren) te vergroten, wordt het jaarlijkse afschrijvingsbedrag kleiner."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een krappe arbeidsmarkt moeten bedrijven vaak hogere salarissen en aantrekkelijkere voorwaarden bieden om geschikt personeel te werven.",
                "antwoord": True,
                "uitleg": "Door de concurrentie om schaars personeel moeten werkgevers betere beloningen en secundaire voorwaarden bieden."
            },
            {
                "type": "waaronwaar",
                "vraag": "Afschrijven op een machine betekent dat het bedrijf elk jaar daadwerkelijk een geldbedrag overboekt naar de bank van de fabrikant.",
                "antwoord": False,
                "uitleg": "Afschrijving is een interne boekhoudkundige waardevermindering; er vloeit op dat moment geen geld naar een externe fabrikant."
            },
            {
                "type": "waaronwaar",
                "vraag": "Huisvestingskosten van een winkelbedrijf bestaan uitsluitend uit advertentiekosten en het drukken van reclamefolders.",
                "antwoord": False,
                "uitleg": "Advertenties zijn verkoopkosten; huisvestingskosten omvatten huur, gas, water, elektra en onderhoud van het pand."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een apparaat aangeschaft voor € 20.000 met een restwaarde van € 2.000 dat in 6 jaar wordt afgeschreven, kost jaarlijks precies € 3.000 aan afschrijving.",
                "antwoord": True,
                "uitleg": "(€ 20.000 - € 2.000) / 6 = € 18.000 / 6 = € 3.000 per jaar."
            },
            {
                "type": "invul",
                "vraag": "Het geldbedrag dat een kapitaalgoed aan het einde van de gebruiksduur bij verkoop nog opbrengt heet de [restwaarde].",
                "antwoord": "restwaarde",
                "uitleg": "De restwaarde is de geschatte opbrengst bij uiteindelijke verkoop of inruil van een kapitaalgoed."
            },
            {
                "type": "invul",
                "vraag": "De economische situatie waarin er veel openstaande vacatures zijn maar weinig werkzoekenden noemen we een [krappe arbeidsmarkt|krapte op de arbeidsmarkt].",
                "antwoord": "krappe arbeidsmarkt|krapte op de arbeidsmarkt",
                "uitleg": "Bij een krappe arbeidsmarkt overtreft de vraag naar personeel het beschikbare aanbod van werkzoekenden."
            },
            {
                "type": "open",
                "vraag": "Noem de vier hoofdgroepen van bedrijfskosten die een onderneming volgens het Pincode-handboek maakt.",
                "sleutelwoorden": [
                    "loonkosten",
                    "huisvestingskosten",
                    "verkoopkosten",
                    "financieringskosten/rentekosten"
                ],
                "minTreffers": 3,
                "modelantwoord": "De vier hoofdgroepen zijn: 1. Loonkosten, 2. Huisvestingskosten, 3. Verkoopkosten en 4. Financieringskosten (rentekosten).",
                "uitleg": "Pincode onderscheidt loonkosten, huisvestingskosten, verkoopkosten en financieringskosten."
            },
            {
                "type": "open",
                "vraag": "Een industriële bakkerij schaft een deegkneedmachine aan voor € 32.000. Na 6 jaar intensief draaien is de geschatte restwaarde € 2.000. Bereken de jaarlijkse afschrijvingskosten en toon de berekening.",
                "sleutelwoorden": [
                    "30.000/dertigduizend",
                    "5.000/5000"
                ],
                "minTreffers": 1,
                "modelantwoord": "Jaarlijkse afschrijving = (€ 32.000 - € 2.000) / 6 jaar = € 30.000 / 6 = € 5.000 per jaar.",
                "uitleg": "Jaarlijkse afschrijving = (Aanschafwaarde - Restwaarde) / Gebruiksduur in jaren."
            }
        ]
    },

    # Examen 25: 4.3 Omzet, Inkoopwaarde & Brutowinst versus Nettowinst
    {
        "id": "ex-h3-economie-25",
        "hoofdstuk": 4,
        "paragraaf": "4.3",
        "titel": "Proeftoets 25: Omzet, Inkoopwaarde & Brutowinst versus Nettowinst (4.3)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "💶",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Een sportwinkel verkoopt in één maand 250 paar hardloopschoenen voor € 120 per stuk (excl. btw). De inkoopprijs was € 50 per paar. Wat is de inkoopwaarde van deze omzet?",
                "opties": [
                    "€ 12.500",
                    "€ 30.000",
                    "€ 17.500",
                    "€ 7.500"
                ],
                "antwoord": 0,
                "uitleg": "Inkoopwaarde van de omzet = afzet (250) × inkoopprijs (€ 50) = € 12.500."
            },
            {
                "type": "mc",
                "vraag": "Een boekhandel behaalt in een kwartaal een omzet van € 90.000. De inkoopwaarde van de verkochte boeken bedraagt € 55.000. Hoeveel bedraagt de brutowinst van deze winkel?",
                "opties": [
                    "€ 145.000",
                    "€ 35.000",
                    "€ 25.000",
                    "€ 45.000"
                ],
                "antwoord": 1,
                "uitleg": "Brutowinst = Omzet (€ 90.000) - Inkoopwaarde van de omzet (€ 55.000) = € 35.000."
            },
            {
                "type": "mc",
                "vraag": "Wat is in de economie de exacte betekenis van het begrip 'afzet'?",
                "opties": [
                    "De totale geldopbrengst van alle verkopen exclusief btw",
                    "De som van de loonkosten en huisvestingskosten in een jaar",
                    "Het totale aantal fysieke producten dat in een periode is verkocht",
                    "De nettowinst na aftrek van de verschuldigde inkomstenbelasting"
                ],
                "antwoord": 2,
                "uitleg": "Afzet is het aantal stuks, kilo's of eenheden; omzet is de geldopbrengst."
            },
            {
                "type": "mc",
                "vraag": "Een kledingzaak behaalt in een boekjaar een brutowinst van € 140.000. De totale overige bedrijfskosten (huur, lonen, energie) bedragen € 95.000. Wat is de nettowinst?",
                "opties": [
                    "€ 235.000",
                    "€ 50.000",
                    "€ 35.000",
                    "€ 45.000"
                ],
                "antwoord": 3,
                "uitleg": "Nettowinst = Brutowinst (€ 140.000) - Bedrijfskosten (€ 95.000) = € 45.000."
            },
            {
                "type": "mc",
                "vraag": "Welke formule toont de juiste relatie tussen brutowinst, bedrijfskosten en nettowinst?",
                "opties": [
                    "Nettowinst = Brutowinst - Bedrijfskosten",
                    "Nettowinst = Omzet + Inkoopwaarde van de omzet",
                    "Nettowinst = Afzet × Inkoopprijs per stuk",
                    "Nettowinst = Totale kosten - Brutowinst"
                ],
                "antwoord": 0,
                "uitleg": "Nettowinst ontstaat door van de brutowinst alle overige bedrijfskosten af te trekken."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met de brutowinst als een winkelier bij gelijkblijvende verkoopprijs en afzet een lagere inkoopprijs weet af te dwingen bij zijn leverancier?",
                "opties": [
                    "De brutowinst daalt direct evenredig met de korting",
                    "De brutowinst stijgt omdat het verschil tussen verkoopprijs en inkoopprijs groter wordt",
                    "De brutowinst blijft exact gelijk omdat de afzet niet verandert",
                    "De brutowinst verandert automatisch in een nettoverlies"
                ],
                "antwoord": 1,
                "uitleg": "Lagere inkoopprijs bij gelijkblijvende omzet verlaagt de inkoopwaarde en verhoogt dus de brutowinst."
            },
            {
                "type": "mc",
                "vraag": "Een speelgoedwinkel heeft een omzet van € 60.000 en een inkoopwaarde van € 38.000. De bedrijfskosten bedragen € 25.000. Welk financieel resultaat boekt de winkel?",
                "opties": [
                    "Een nettowinst van € 3.000",
                    "Een brutoverlies van € 2.000",
                    "Een nettoverlies van € 3.000",
                    "Een nettowinst van € 22.000"
                ],
                "antwoord": 2,
                "uitleg": "Brutowinst = € 60.000 - € 38.000 = € 22.000. Nettowinst = € 22.000 - € 25.000 = -€ 3.000 (dus nettoverlies)."
            },
            {
                "type": "mc",
                "vraag": "Een witgoedhandelaar verkoopt in een actieweek 80 wasmachines voor € 600 per stuk (excl. btw). Wat is de totale omzet van deze partij wasmachines?",
                "opties": [
                    "€ 4.800",
                    "€ 58.080",
                    "€ 36.000",
                    "€ 48.000"
                ],
                "antwoord": 3,
                "uitleg": "Omzet = Verkoopprijs × Afzet = € 600 × 80 = € 48.000."
            },
            {
                "type": "mc",
                "vraag": "Welke doeltreffende bedrijfseconomische maatregel kan een winkelier nemen om een nettoverlies om te buigen naar een gezonde nettowinst?",
                "opties": [
                    "Bezuinigen op overbodige bedrijfskosten en scherpere inkoopprijzen onderhandelen",
                    "De inkoopprijzen bij leveranciers vrijwillig met 20% verhogen",
                    "Goederen onder de inkoopprijs gratis weggeven aan het winkelend publiek",
                    "Stoppen met het administreren van de bedrijfskosten"
                ],
                "antwoord": 0,
                "uitleg": "Kostenreductie en scherpere inkoop vergroten de marge tussen opbrengst en totale kosten."
            },
            {
                "type": "mc",
                "vraag": "Een rijwielhandel koopt een e-bike in voor € 1.200 en verkoopt deze voor € 1.900 (beide bedragen exclusief btw). Hoeveel brutowinst realiseert de handelaar op deze e-bike?",
                "opties": [
                    "€ 1.200",
                    "€ 700",
                    "€ 3.100",
                    "€ 500"
                ],
                "antwoord": 1,
                "uitleg": "Brutowinst per stuk = Verkoopprijs (€ 1.900) - Inkoopprijs (€ 1.200) = € 700."
            },
            {
                "type": "mc",
                "vraag": "Waarom is het voor een ondernemer riskant om zich alleen blind te staren op een alsmaar stijgende omzet?",
                "opties": [
                    "Omdat een hogere omzet door de overheid wettelijk zwaarder beboet wordt",
                    "Omdat consumenten weigeren te kopen bij bedrijven met hoge omzetten",
                    "Omdat torenhoge inkoopkosten en bedrijfskosten ondanks een hoge omzet tot verlies kunnen leiden",
                    "Omdat omzet en afzet wettelijk altijd aan elkaar gelijk moeten zijn"
                ],
                "antwoord": 2,
                "uitleg": "Omzet zegt niets over winst als de inkoop- en bedrijfskosten nog sneller stijgen dan de omzet."
            },
            {
                "type": "mc",
                "vraag": "Een brillenwinkel realiseert een jaaromzet van € 200.000. De brutowinst bedraagt precies 60% van de omzet. Hoeveel bedraagt de inkoopwaarde van de verkochte brillen?",
                "opties": [
                    "€ 120.000",
                    "€ 60.000",
                    "€ 140.000",
                    "€ 80.000"
                ],
                "antwoord": 3,
                "uitleg": "Inkoopwaarde = 100% - 60% = 40% van de omzet. 0,40 × € 200.000 = € 80.000."
            },
            {
                "type": "waaronwaar",
                "vraag": "Wanneer de inkoopwaarde van de omzet hoger is dan de behaalde omzet, lijdt de ondernemer een brutoverlies.",
                "antwoord": True,
                "uitleg": "Als goederen voor minder geld worden verkocht dan ze in inkoop hebben gekost, is de brutowinst negatief."
            },
            {
                "type": "waaronwaar",
                "vraag": "De omzet van een onderneming is altijd precies gelijk aan het nettobedrag dat de eigenaar als winst mag behouden.",
                "antwoord": False,
                "uitleg": "Van de omzet moeten de inkoopwaarde en alle bedrijfskosten nog afgetrokken worden."
            },
            {
                "type": "waaronwaar",
                "vraag": "De inkoopwaarde van de omzet betreft uitsluitend de inkoopprijs van de goederen die in die periode daadwerkelijk zijn verkocht.",
                "antwoord": True,
                "uitleg": "Goederen die nog onverkocht in het magazijn liggen, behoren tot de voorraad en niet tot de inkoopwaarde van de omzet."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het aantal verkochte exemplaren noemen we de omzet en het totale ontvangen geldbedrag noemen we de afzet.",
                "antwoord": False,
                "uitleg": "Het aantal stuks is de afzet; de totale geldopbrengst is de omzet."
            },
            {
                "type": "invul",
                "vraag": "Het verschil tussen de omzet en de inkoopwaarde van de omzet noemen we de [brutowinst].",
                "antwoord": "brutowinst",
                "uitleg": "Brutowinst = Omzet minus inkoopwaarde van de verkochte goederen."
            },
            {
                "type": "invul",
                "vraag": "De uiteindelijke winst die overblijft nadat van de brutowinst alle overige bedrijfskosten zijn afgetrokken heet de [nettowinst].",
                "antwoord": "nettowinst",
                "uitleg": "Nettowinst = Brutowinst minus overige bedrijfskosten."
            },
            {
                "type": "open",
                "vraag": "Een kledingboetiek verkoopt in een maand 300 jurken voor € 70 per stuk (excl. btw). De inkoopprijs bedroeg € 30 per jurk. Bereken de omzet en de inkoopwaarde van deze jurken.",
                "sleutelwoorden": [
                    "21.000/eenentwintigduizend",
                    "9.000/negenduizend"
                ],
                "minTreffers": 2,
                "modelantwoord": "Omzet = 300 × € 70 = € 21.000. Inkoopwaarde van de omzet = 300 × € 30 = € 9.000.",
                "uitleg": "Omzet = afzet × verkoopprijs; Inkoopwaarde = afzet × inkoopprijs."
            },
            {
                "type": "open",
                "vraag": "Een bloemenzaak heeft een maandelijkse omzet van € 40.000 en een inkoopwaarde van € 18.000. De totale bedrijfskosten bedragen € 15.000. Bereken stapsgewijs de brutowinst en de nettowinst.",
                "sleutelwoorden": [
                    "22.000/tweeëntwintigduizend",
                    "7.000/zevenduizend"
                ],
                "minTreffers": 2,
                "modelantwoord": "Brutowinst = € 40.000 - € 18.000 = € 22.000. Nettowinst = € 22.000 - € 15.000 = € 7.000.",
                "uitleg": "Brutowinst = Omzet - Inkoopwaarde; Nettowinst = Brutowinst - Bedrijfskosten."
            }
        ]
    },

    # Examen 26: 4.3 Break-even Analyse, Btw-berekeningen & Bedrijfscasussen
    {
        "id": "ex-h3-economie-26",
        "hoofdstuk": 4,
        "paragraaf": "4.3",
        "titel": "Proeftoets 26: Break-even Analyse, Btw-berekeningen & Bedrijfscasussen (4.2 & 4.3)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "⚖️",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Een pizzeria heeft vaste constante kosten van € 3.600 per maand. De verkoopprijs van een pizza is € 10 en de variabele kosten zijn € 4 per pizza. Wat is de break-even afzet per maand?",
                "opties": [
                    "600 pizza's per maand",
                    "360 pizza's per maand",
                    "900 pizza's per maand",
                    "450 pizza's per maand"
                ],
                "antwoord": 0,
                "uitleg": "Dekkingsbijdrage per pizza = € 10 - € 4 = € 6. Break-even afzet = € 3.600 / € 6 = 600 pizza's per maand."
            },
            {
                "type": "mc",
                "vraag": "Een paar merksneakers kost in de winkel € 121 inclusief 21% btw. Wat is de verkoopprijs exclusief btw?",
                "opties": [
                    "€ 96",
                    "€ 100",
                    "€ 105",
                    "€ 110"
                ],
                "antwoord": 1,
                "uitleg": "Prijs excl. btw = Consumentenprijs / 1,21 = € 121 / 1,21 = € 100."
            },
            {
                "type": "mc",
                "vraag": "Welk van de volgende producten valt in Nederland onder het verlaagde btw-tarief van 9%?",
                "opties": [
                    "Een luxe spelcomputer bij een elektronicaketen",
                    "Een leren damesjas in een kledingboetiek",
                    "Een vers volkorenbrood bij de ambachtelijke bakker",
                    "Een fles designerparfum bij de drogisterij"
                ],
                "antwoord": 2,
                "uitleg": "Basisvoedingsmiddelen zoals brood vallen onder het lage 9%-tarief voor eerste levensbehoeften."
            },
            {
                "type": "mc",
                "vraag": "Een portretfotograaf heeft € 5.000 vaste kosten per jaar. Per fotoshoot rekent hij € 150 en zijn variabele kosten zijn € 50. Wat is zijn break-even omzet?",
                "opties": [
                    "€ 5.000",
                    "€ 10.000",
                    "€ 6.500",
                    "€ 7.500"
                ],
                "antwoord": 3,
                "uitleg": "Marge per shoot = € 150 - € 50 = € 100. Break-even afzet = € 5.000 / € 100 = 50 shoots. Break-even omzet = 50 × € 150 = € 7.500."
            },
            {
                "type": "mc",
                "vraag": "Een kapper rekent voor een was- en knipbeurt € 30 exclusief 9% btw. Welk bedrag betaalt de klant inclusief btw aan de kassa?",
                "opties": [
                    "€ 32,70",
                    "€ 36,30",
                    "€ 39,00",
                    "€ 33,00"
                ],
                "antwoord": 0,
                "uitleg": "Consumentenprijs = € 30 × 1,09 = € 32,70."
            },
            {
                "type": "mc",
                "vraag": "Waarom vormt de btw die een winkelier van consumenten ontvangt GEEN onderdeel van zijn eigen omzet of winst?",
                "opties": [
                    "Omdat de winkelier de btw direct moet omzetten in goudstaven bij de bank",
                    "Omdat de winkelier de ontvangen btw namens de overheid int en moet afdragen aan de Belastingdienst",
                    "Omdat de btw uitsluitend bestemd is als fooi voor het winkelpersoneel",
                    "Omdat de winkelier wettelijk verplicht is de btw aan het einde van de dag terug te storten"
                ],
                "antwoord": 1,
                "uitleg": "Btw is een indirecte belasting: de ondernemer int deze namens de staat en draagt deze af aan de fiscus."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met het break-evenpunt van een onderneming als de vaste constante kosten stijgen, terwijl de verkoopprijs en variabele kosten gelijk blijven?",
                "opties": [
                    "Het break-evenpunt daalt onmiddellijk naar nul stuks",
                    "De winst per verkocht product stijgt automatisch mee",
                    "Het break-evenpunt verschuift naar een hogere afzet (er moeten meer stuks worden verkocht om quitte te spelen)",
                    "Het break-evenpunt verandert nooit door schommelingen in vaste lasten"
                ],
                "antwoord": 2,
                "uitleg": "Hogere vaste lasten betekenen dat er meer stuks verkocht moeten worden om quitte te spelen."
            },
            {
                "type": "mc",
                "vraag": "Een bioscoopkaartje kost € 10,90 inclusief 9% btw. Hoeveel btw is in deze ticketprijs inbegrepen?",
                "opties": [
                    "€ 0,98",
                    "€ 1,90",
                    "€ 0,81",
                    "€ 0,90"
                ],
                "antwoord": 3,
                "uitleg": "Prijs excl. btw = € 10,90 / 1,09 = € 10,00. Btw-bedrag = € 10,90 - € 10,00 = € 0,90."
            },
            {
                "type": "mc",
                "vraag": "Wat verstaan economen onder de 'dekkingsbijdrage per stuk' van een product?",
                "opties": [
                    "De verkoopprijs per stuk verminderd met de variabele kosten per stuk (p - v)",
                    "De totale omzet vermenigvuldigd met het toepasselijke btw-percentage",
                    "De aanschafprijs van een kapitaalgoed gedeeld door de restwaarde",
                    "Het wettelijk minimumloon gedeeld door het aantal gewerkte uren"
                ],
                "antwoord": 0,
                "uitleg": "De dekkingsbijdrage (p - v) geeft aan welk deel van de verkoopprijs overblijft om de vaste kosten te dekken."
            },
            {
                "type": "mc",
                "vraag": "Een fietsenhandelaar koopt fietssloten in voor € 4 en verkoopt ze voor € 10 exclusief 21% btw. Wat rekent de consument af inclusief btw?",
                "opties": [
                    "€ 14,84",
                    "€ 12,10",
                    "€ 10,00",
                    "€ 11,21"
                ],
                "antwoord": 1,
                "uitleg": "Consumentenprijs = € 10 × 1,21 = € 12,10."
            },
            {
                "type": "mc",
                "vraag": "Een theater heeft vaste zaalhuur van € 1.800 per avond. Een kaartje kost € 25 en de variabele kosten per bezoeker zijn € 5. Bij hoeveel bezoekers draait het theater break-even?",
                "opties": [
                    "72 bezoekers",
                    "120 bezoekers",
                    "90 bezoekers",
                    "60 bezoekers"
                ],
                "antwoord": 2,
                "uitleg": "Dekkingsbijdrage = € 25 - € 5 = € 20 per bezoeker. Break-even afzet = € 1.800 / € 20 = 90 bezoekers."
            },
            {
                "type": "mc",
                "vraag": "Welke diensten zijn in Nederland volgens de belastingwetgeving doorgaans volledig vrijgesteld van btw?",
                "opties": [
                    "Benzineverkoop aan pompstations en autoschadeherstel",
                    "Kledingverkoop en verkoop van merkschoenen",
                    "Vluchten met commerciële luchtvaartmaatschappijen",
                    "Medische behandelingen door artsen en regulier schoolonderwijs"
                ],
                "antwoord": 3,
                "uitleg": "Gezondheidszorg en onderwijs zijn maatschappelijke sectoren die zijn vrijgesteld van btw."
            },
            {
                "type": "waaronwaar",
                "vraag": "Zodra een onderneming meer eenheden verkoopt dan de break-even afzet, begint zij werkelijk nettowinst te maken.",
                "antwoord": True,
                "uitleg": "Boven het break-evenpunt zijn alle constante vaste kosten gedekt en levert elke extra verkoop nettowinst op."
            },
            {
                "type": "waaronwaar",
                "vraag": "Op luxe artikelen zoals consumentenelektronica en designerkleding heft de overheid het verlaagde btw-tarief van 9%.",
                "antwoord": False,
                "uitleg": "Luxe artikelen en consumentenelektronica vallen onder het algemene hoge btw-tarief van 21%."
            },
            {
                "type": "waaronwaar",
                "vraag": "De verkoopprijs exclusief btw bereken je door de consumentenprijs inclusief 21% btw simpelweg met 0,79 te vermenigvuldigen.",
                "antwoord": False,
                "uitleg": "Je moet delen door 1,21; vermenigvuldigen met 0,79 levert een rekenkundige fout op omdat de prijs excl. btw 100% is."
            },
            {
                "type": "waaronwaar",
                "vraag": "Op het break-evenpunt zijn de totale opbrengsten (TO) exact gelijk aan de totale kosten (TK) en is de winst precies nul euro.",
                "antwoord": True,
                "uitleg": "Break-even betekent quitte spelen: TO = TK en de winst is exact € 0."
            },
            {
                "type": "invul",
                "vraag": "Het verkoopvolume waarbij een onderneming precies quitte speelt en de winst nul euro bedraagt heet de [break-even afzet|BEA].",
                "antwoord": "break-even afzet|BEA",
                "uitleg": "Break-even afzet is de afzet waarbij de totale opbrengst precies gelijk is aan de totale kosten."
            },
            {
                "type": "invul",
                "vraag": "Het verlaagde btw-tarief in Nederland voor eerste levensbehoeften bedraagt [9%|9 procent|9].",
                "antwoord": "9%|9 procent|9",
                "uitleg": "Het lage btw-tarief voor primaire goederen en diensten is 9%."
            },
            {
                "type": "open",
                "vraag": "Een foodtruck verkoopt smoothies voor € 5 per beker. De variabele kosten bedragen € 2 per beker. De vaste wekelijkse standplaatskosten zijn € 600. Bereken de break-even afzet per week. Toon de berekening.",
                "sleutelwoorden": [
                    "200/tweehonderd"
                ],
                "minTreffers": 1,
                "modelantwoord": "Dekkingsbijdrage per smoothie = € 5 - € 2 = € 3. Break-even afzet = € 600 / € 3 = 200 smoothies per week.",
                "uitleg": "Break-even afzet = Vaste kosten / (Verkoopprijs - Variabele kosten per eenheid)."
            },
            {
                "type": "open",
                "vraag": "Een designer salontafel kost in een meubelzaak € 605 inclusief 21% btw. Bereken de verkoopprijs exclusief btw en het btw-bedrag in euro's. Toon de tussenstappen.",
                "sleutelwoorden": [
                    "500/vijfhonderd",
                    "105/honderdvijf"
                ],
                "minTreffers": 2,
                "modelantwoord": "Prijs excl. btw = € 605 / 1,21 = € 500. Btw-bedrag = € 605 - € 500 = € 105.",
                "uitleg": "Prijs excl. btw = consumentenprijs / 1,21. Btw-bedrag = consumentenprijs - prijs excl. btw."
            }
        ]
    },

    # Examen 27: 4.1 Examentraining Hoofdstuk 4 — Produceren & Bedrijfseconomie (Integraal)
    {
        "id": "ex-h3-economie-27",
        "hoofdstuk": 4,
        "paragraaf": "4.1",
        "titel": "Proeftoets 27: Examentraining Hoofdstuk 4 — Produceren & Bedrijfseconomie (Integraal)",
        "vak": "Economie · HAVO 3 (Pincode)",
        "icoon": "🎓",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Waarom wordt het zelf bereiden van een gezinsmaaltijd in de eigen keuken economisch gezien NIET aangemerkt als produceren?",
                "opties": [
                    "Omdat het plaatsvindt binnen het huishouden voor eigen consumptie zonder markttransactie (zelfvoorziening)",
                    "Omdat bij een gezinsmaaltijd geen biologische ingrediënten worden benut",
                    "Omdat de Europese wetgeving het koken van maaltijden thuis streng verbiedt",
                    "Omdat een zelfbereide maaltijd geen enkele voedingswaarde heeft voor het gezin"
                ],
                "antwoord": 0,
                "uitleg": "Produceren is het maken van goederen/diensten door bedrijven voor anderen tegen betaling; thuis koken is zelfvoorziening."
            },
            {
                "type": "mc",
                "vraag": "Welke beloning hoort bij de productiefactor Kapitaal wanneer een onderneming geld leent bij een bank of machines inzet?",
                "opties": [
                    "Loon of salaris",
                    "Rente of huur",
                    "Pacht",
                    "Winst"
                ],
                "antwoord": 1,
                "uitleg": "De vergoeding voor de productiefactor kapitaal is rente (bij geldkapitaal) of huur (bij reëel kapitaal)."
            },
            {
                "type": "mc",
                "vraag": "Een meubelfabriek produceert met 10 werknemers in één maand tijd 500 houten tafels. Wat is de arbeidsproductiviteit per werknemer per maand?",
                "opties": [
                    "5 tafels per werknemer",
                    "500 tafels per werknemer",
                    "50 tafels per werknemer",
                    "25 tafels per werknemer"
                ],
                "antwoord": 2,
                "uitleg": "Arbeidsproductiviteit = Totale productie / Aantal werknemers = 500 / 10 = 50 tafels per werknemer per maand."
            },
            {
                "type": "mc",
                "vraag": "Een kledingmaker koopt stof en fournituren in voor € 15 per jurk. De energiekosten zijn € 2 per jurk. Hij verkoopt de jurk aan een boetiek voor € 45 (excl. btw). Wat is de toegevoegde waarde per jurk?",
                "opties": [
                    "€ 30 per jurk",
                    "€ 45 per jurk",
                    "€ 17 per jurk",
                    "€ 28 per jurk"
                ],
                "antwoord": 3,
                "uitleg": "Toegevoegde waarde = Verkoopprijs (€ 45) - Inkoopwaarde grond- en hulpstoffen (€ 15 + € 2 = € 17) = € 28 per jurk."
            },
            {
                "type": "mc",
                "vraag": "Waarom daalt de kostprijs per eenheid product wanneer een autofabriek overschakelt op grootschalige massaproductie (schaalvoordeel)?",
                "opties": [
                    "Omdat de totale constante vaste kosten over veel meer geproduceerde auto's worden verdeeld",
                    "Omdat de staalprijzen op de wereldmarkt bij massaproductie automatisch naar nul dalen",
                    "Omdat werknemers aan de lopende band wettelijk geen salaris meer ontvangen",
                    "Omdat over in serie geproduceerde goederen geen omzetbelasting verschuldigd is"
                ],
                "antwoord": 0,
                "uitleg": "Constante kosten (zoals fabriek en robots) worden bij grote volumes over veel meer stuks verdeeld (schaalvoordeel)."
            },
            {
                "type": "mc",
                "vraag": "Een schoenmaker koopt een zoolpersmachine voor € 18.000. De levensduur is 6 jaar en de restwaarde bedraagt € 3.000. Wat zijn de jaarlijkse afschrijvingskosten?",
                "opties": [
                    "€ 3.000 per jaar",
                    "€ 2.500 per jaar",
                    "€ 1.500 per jaar",
                    "€ 3.500 per jaar"
                ],
                "antwoord": 1,
                "uitleg": "Afschrijving per jaar = (€ 18.000 - € 3.000) / 6 jaar = € 15.000 / 6 = € 2.500 per jaar."
            },
            {
                "type": "mc",
                "vraag": "Een handelsonderneming behaalt een omzet van € 150.000. De inkoopwaarde van de omzet is € 90.000. De bedrijfskosten zijn € 40.000. Hoeveel bedraagt de nettowinst?",
                "opties": [
                    "€ 60.000",
                    "€ 50.000",
                    "€ 20.000",
                    "€ 10.000"
                ],
                "antwoord": 2,
                "uitleg": "Brutowinst = € 150.000 - € 90.000 = € 60.000. Nettowinst = Brutowinst (€ 60.000) - Bedrijfskosten (€ 40.000) = € 20.000."
            },
            {
                "type": "mc",
                "vraag": "Welke partij staat volgens de bedrijfseconomische theorie aan het allerlaatste einde van de bedrijfskolom?",
                "opties": [
                    "De consument",
                    "De groothandel",
                    "De transporteur",
                    "De detaillist (winkelier)"
                ],
                "antwoord": 3,
                "uitleg": "De bedrijfskolom eindigt bij de detaillist (winkelier); de consument staat er buiten omdat hij niet meer verder produceert."
            },
            {
                "type": "mc",
                "vraag": "Een koffiebar verkoopt 2.000 koppen koffie per maand voor € 3,50 per kop (excl. btw). De inkoopwaarde van de bonen en melk is € 0,50 per kop. De vaste kosten zijn € 3.000 per maand. Wat is de nettowinst per maand?",
                "opties": [
                    "€ 3.000 per maand",
                    "€ 4.000 per maand",
                    "€ 7.000 per maand",
                    "€ 1.000 per maand"
                ],
                "antwoord": 0,
                "uitleg": "Omzet = 2.000 × € 3,50 = € 7.000. Inkoopwaarde = 2.000 × € 0,50 = € 1.000. Brutowinst = € 6.000. Nettowinst = € 6.000 - € 3.000 = € 3.000."
            },
            {
                "type": "mc",
                "vraag": "Een consument koopt een laptop voor € 847 inclusief 21% btw. Hoeveel bedraagt de verkoopprijs exclusief btw?",
                "opties": [
                    "€ 669",
                    "€ 700",
                    "€ 750",
                    "€ 800"
                ],
                "antwoord": 1,
                "uitleg": "Prijs excl. btw = € 847 / 1,21 = € 700."
            },
            {
                "type": "mc",
                "vraag": "Welke factor zorgt ervoor dat de arbeidsproductiviteit van werknemers in een fabriek structureel toeneemt?",
                "opties": [
                    "Het verlengen van de wekelijkse werkduur zonder extra rustpauzes",
                    "Het verhogen van de btw op eindproducten door de overheid",
                    "Investeringen in geavanceerde machines, automatisering en scholing van het personeel",
                    "Het verlagen van de verkoopprijzen in de fabriekswinkel"
                ],
                "antwoord": 2,
                "uitleg": "Betere scholing, automatisering en modern gereedschap verhogen de output per gewerkt uur."
            },
            {
                "type": "mc",
                "vraag": "Wat laat de economische kringloop tussen gezinshuishoudens en bedrijfshuishoudens in essentie zien?",
                "opties": [
                    "Dat gezinnen alleen goederen ontvangen zonder ooit een tegenprestatie te leveren",
                    "Dat bedrijven geen salarissen uitkeren aan particuliere huishoudens",
                    "Dat geldstromen en goederen/arbeidsstromen in dezelfde richting door het land stromen",
                    "Dat geldstromen en reële stromen (arbeid en goederen) in tegengestelde richting circuleren"
                ],
                "antwoord": 3,
                "uitleg": "Gezinnen leveren arbeid en ontvangen geld (loon); met dat geld kopen zij goederen en vloeit het geld terug naar bedrijven."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Bruto Binnenlands Product (BBP) is gelijk aan de optelsom van alle toegevoegde waarden die in een land in één jaar worden geproduceerd.",
                "antwoord": True,
                "uitleg": "Het BBP meet de totale waardecreatie (productie) van alle bedrijven en de overheid in een land."
            },
            {
                "type": "waaronwaar",
                "vraag": "Wanneer de productieomvang van een fabriek verdubbelt, verdubbelen de constante vaste kosten automatisch ook.",
                "antwoord": False,
                "uitleg": "Constante kosten (zoals de huur van het gebouw) blijven gelijk, ongeacht hoeveel er geproduceerd wordt."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een winkelier die artikelen inkoopt voor € 40 en verkoopt voor € 100 exclusief btw, behaalt een brutowinst van € 60 per stuk.",
                "antwoord": True,
                "uitleg": "Brutowinst = Verkoopprijs (€ 100) - Inkoopprijs (€ 40) = € 60."
            },
            {
                "type": "waaronwaar",
                "vraag": "De consument maakt een essentieel onderdeel uit van de bedrijfskolom omdat hij goederen aankoopt en verbruikt.",
                "antwoord": False,
                "uitleg": "De consument staat buiten de bedrijfskolom; consumeren voegt geen waarde meer toe aan het product."
            },
            {
                "type": "invul",
                "vraag": "De productieomvang per werknemer in een bepaalde tijdseenheid noemen we de [arbeidsproductiviteit].",
                "antwoord": "arbeidsproductiviteit",
                "uitleg": "Arbeidsproductiviteit meet de prestatie per werknemer per uur, dag of jaar."
            },
            {
                "type": "invul",
                "vraag": "De jaarlijkse waardevermindering van kapitaalgoederen als gevolg van slijtage en veroudering heet [afschrijving|afschrijven|afschrijvingen].",
                "antwoord": "afschrijving|afschrijven|afschrijvingen",
                "uitleg": "Afschrijving is het boekhoudkundig verdelen van de aanschafkosten over de gebruiksjaren."
            },
            {
                "type": "open",
                "vraag": "Noem de vier letters van het ezelsbruggetje KANO en geef bij elke letter de bijbehorende productiefactor.",
                "sleutelwoorden": [
                    "kapitaal",
                    "arbeid",
                    "natuur",
                    "ondernemerschap"
                ],
                "minTreffers": 4,
                "modelantwoord": "K = Kapitaal, A = Arbeid, N = Natuur, O = Ondernemerschap.",
                "uitleg": "KANO staat voor de vier productiefactoren: Kapitaal, Arbeid, Natuur en Ondernemerschap."
            },
            {
                "type": "open",
                "vraag": "Een bakkerij produceert 10.000 broden per maand. De totale constante kosten zijn € 6.000 per maand. De variabele kosten bedragen € 0,80 per brood. Bereken de kostprijs per brood. Toon de berekening.",
                "sleutelwoorden": [
                    "14.000/veertienduizend",
                    "1,40/1.40"
                ],
                "minTreffers": 1,
                "modelantwoord": "Totale variabele kosten = 10.000 × € 0,80 = € 8.000. Totale kosten = € 6.000 + € 8.000 = € 14.000. Kostprijs per brood = € 14.000 / 10.000 = € 1,40 per brood.",
                "uitleg": "Kostprijs = Totale kosten / Productieomvang (TK / q)."
            }
        ]
    }
]

print("Verifying and writing exams 24 to 27...")
for idx, ex in enumerate(exams, 24):
    fname = f"{DATA_DIR}/examen_{idx}.js"
    # Verification checks
    assert len(ex["vragen"]) == 20, f"Examen {idx} has {len(ex['vragen'])} questions, expected 20"
    mc_counts = {}
    wo_onwaar = 0
    for v in ex["vragen"]:
        assert len(v.get("uitleg", "")) >= 15, f"Short explanation in {idx}: {v}"
        if v["type"] == "mc":
            mc_counts[v["antwoord"]] = mc_counts.get(v["antwoord"], 0) + 1
        elif v["type"] == "waaronwaar":
            if v["antwoord"] is False:
                wo_onwaar += 1
        elif v["type"] == "open":
            assert len(v["sleutelwoorden"]) >= v["minTreffers"], f"Invalid minTreffers in {idx}: {v}"
            for s in v["sleutelwoorden"]:
                for part in s.split("/"):
                    # ensure no exact match with question text
                    assert part.lower() not in v["vraag"].lower(), f"Leak in {idx}: {part} in {v['vraag']}"

    print(f"Examen {idx} MC distribution: {mc_counts}, Waaronwaar Onwaar: {wo_onwaar}/4")
    assert all(c <= 5 for c in mc_counts.values()), f"MC unbalanced in {idx}: {mc_counts}"
    assert wo_onwaar >= 1, f"Not enough onwaar in {idx}"

    content = f"/* =========================================================\n   Duru's Economie (HAVO 3) — {ex['titel']}\n   ========================================================= */\nDURU.registerExamen({json.dumps(ex, ensure_ascii=False, indent=2)});\n"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Written {fname}")

print("\nAll 4 exams written successfully!")
