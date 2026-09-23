#!/usr/bin/env python3
"""
gen_duits_extra.py — Volledige generator voor de ontbrekende Duits onderwerpen (h1_4..h6_4)
en proeftoetsen (examen_31..36) op basis van Neue Kontakte 3 HAVO (TASK-17).
"""
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "havo3", "duits", "js", "data")

ONDERWERPEN = [
    # H1 §1.4
    {
        "id": "dui-h1-4",
        "hoofdstuk": 1,
        "paragraaf": "1.4",
        "titel": "Wortschatz & Lesekompetenz: Lernliste Deutsch & Landschaftsbeschreibung",
        "korteUitleg": "Actieve woordenschat uit teksten en video's over klimaat, natuurbehoud, windrichtingen en het beschrijven van landschappen.",
        "icoon": "🌲",
        "kleur": "blauw",
        "theorie": """
    <h3>1.4 Wortschatz & Lesekompetenz: Lernliste Deutsch & Landschaftsbeschreibung</h3>
    <div class="info-box">
      <b>Kernfocus:</b> Verdieping van de woordenschat uit <i>Neue Kontakte Kapitel 1</i>. Naast basiswoorden voor het weer leer je actieve begrippen uit authentieke reportages (Sehen & Hören) en leesteksten over klimaat, natuur en geografie.
    </div>

    <h4>1. Lernliste Deutsch: Klimawandel, Natur & Aktivität</h4>
    <p>In de teksten en luisterfragmenten van Kapitel 1 komen belangrijke themawoorden aan bod die je actief moet beheersen:</p>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:#e8f0fe;">
        <th style="padding:6px;border:1px solid #ccc;">Duits 🇩🇪</th>
        <th style="padding:6px;border:1px solid #ccc;">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid #ccc;">Voorbeeldzin</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>der Klimawandel</b></td><td style="padding:6px;border:1px solid #ccc;">de klimaatverandering</td><td style="padding:6px;border:1px solid #ccc;">Der Klimawandel hat Auswirkungen auf die Alpen.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>die Auswirkung, -en</b></td><td style="padding:6px;border:1px solid #ccc;">het gevolg, de uitwerking</td><td style="padding:6px;border:1px solid #ccc;">Welche Auswirkung hat die Hitze auf die Natur?</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>der Naturschutz</b></td><td style="padding:6px;border:1px solid #ccc;">de natuurbescherming</td><td style="padding:6px;border:1px solid #ccc;">Viele Jugendliche engagieren sich für Naturschutz.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>die Nahrung</b></td><td style="padding:6px;border:1px solid #ccc;">de voeding / het voedsel</td><td style="padding:6px;border:1px solid #ccc;">Blumen bieten den Bienen wertvolle Nahrung.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>zerstören</b></td><td style="padding:6px;border:1px solid #ccc;">verwoesten, vernielen</td><td style="padding:6px;border:1px solid #ccc;">Das Unwetter hat das kleine Gartenhaus zerstört.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>die Begeisterung</b></td><td style="padding:6px;border:1px solid #ccc;">het enthousiasme</td><td style="padding:6px;border:1px solid #ccc;">Ich teile seine Begeisterung für die Fotografie.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>sich auskennen</b></td><td style="padding:6px;border:1px solid #ccc;">op de hoogte zijn, de weg weten</td><td style="padding:6px;border:1px solid #ccc;">Wer sich im Gebirge nicht auskennt, braucht Hilfe.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>zuverlässig</b></td><td style="padding:6px;border:1px solid #ccc;">betrouwbaar</td><td style="padding:6px;border:1px solid #ccc;">Diese Wetterstation liefert zuverlässige Daten.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>der Fels, -en / klettern</b></td><td style="padding:6px;border:1px solid #ccc;">de rots / klimmen</td><td style="padding:6px;border:1px solid #ccc;">Sie klettern vorsichtig über die nassen Felsen.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>der Ausblick</b></td><td style="padding:6px;border:1px solid #ccc;">het uitzicht</td><td style="padding:6px;border:1px solid #ccc;">Vom Aussichtsturm hat man einen tollen Ausblick.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>beobachten</b></td><td style="padding:6px;border:1px solid #ccc;">observeren, bekijken</td><td style="padding:6px;border:1px solid #ccc;">Mit dem Fernglas kann man Wildtiere beobachten.</td></tr>
    </table>

    <h4>2. Windrichtingen en Landschappen (Himmelsrichtungen & Landschaft)</h4>
    <p>Bij windrichtingen gebruik je in het Duits altijd het voorzetsel <b>im</b> (in dem):</p>
    <ul>
      <li><code>im Norden</code> = in het noorden | <code>im Osten</code> = in het oosten</li>
      <li><code>im Süden</code> = in het zuiden | <code>im Westen</code> = in het westen</li>
    </ul>
    <p>Natuur- en omgevingsbegrippen:</p>
    <ul>
      <li><b>die Umgebung</b> (de omgeving) / <b>die Gegend</b> (de streek, streekstreek)</li>
      <li><b>der Ort, -e</b> (de plaats) / <b>das Dorf, Dörfer</b> (het dorp)</li>
      <li><b>das Meer</b> (de zee - let op: het meer in het Nederlands is in het Duits <i>der See</i>!)</li>
      <li><b>die Insel, -n</b> (het eiland) | <b>wandern</b> (een stevige wandeling maken) | <b>zelten</b> (kamperen in een tent)</li>
      <li><b>glatt</b> (glad) | <b>hektisch</b> (druk, hectisch) | <b>ruhig</b> (rustig, vredig)</li>
    </ul>

    <h4>3. Sprachmittel: Een landschap en streek omschrijven</h4>
    <div class="formule-box">
      • <b>Wie ist die Gegend?</b> (Hoe is de streek?)<br>
      • <i>In Süddeutschland ist die Landschaft sehr hügelig und bergig.</i><br>
      • <i>Bei Frankfurt gibt es viele bekannte Flüsse und ruhige Seen.</i><br>
      • <i>Am Meer ist es im Herbst oft stürmisch und regnerisch.</i><br>
      • <i>Es ist hier nicht so hektisch wie in einer Großstadt.</i>
    </div>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent de Duitse uitdrukking 'sich auskennen'?",
                "opties": [
                    "Ergens de weg weten of goed op de hoogte zijn",
                    "Zichzelf voorstellen aan vreemden",
                    "Iets helemaal verwoesten",
                    "Zich haasten om de trein te halen"
                ],
                "antwoord": 0,
                "uitleg": "'Sich auskennen' betekent ergens bekend mee zijn of goed de weg weten (bijv. in de bergen)."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits woord betekent 'het uitzicht'?",
                "opties": [
                    "der Naturschutz",
                    "der Ausblick",
                    "der Fels",
                    "die Auswirkung"
                ],
                "antwoord": 1,
                "uitleg": "'Der Ausblick' betekent het uitzicht (vanaf een toren of berg)."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Duits 'in het noorden'?",
                "opties": [
                    "am Norden",
                    "nach Norden",
                    "im Norden",
                    "vom Norden"
                ],
                "antwoord": 2,
                "uitleg": "Bij windrichtingen gebruik je in het Duits het voorzetsel 'im' (im Norden, im Süden, im Osten, im Westen)."
            },
            {
                "type": "mc",
                "vraag": "Wat is het grote verschil tussen 'das Meer' en 'der See'?",
                "opties": [
                    "Das Meer is een rivier en der See is een beek",
                    "Das Meer is het strand en der See is een eiland",
                    "Beide woorden betekenen precies hetzelfde",
                    "Das Meer is de zee en der See is een binnenmeer"
                ],
                "antwoord": 3,
                "uitleg": "Valse vriend: 'das Meer' betekent de zee, terwijl 'der See' een zoetwatermeer op het land is."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse werkwoord 'zelten' betekent barbecueën in de tuin.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Zelten' betekent kamperen in een tent. Barbecueën is 'grillen'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'die Nahrung' betekent voeding of voedsel.",
                "antwoord": True,
                "uitleg": "Waar! 'Die Nahrung' betekent voeding (bijvoorbeeld nectar en stuifmeel als voeding voor bijen)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het woord 'zuverlässig' betekent dat iets gevaarlijk en glad is.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Zuverlässig' betekent betrouwbaar. Glad is in het Duits 'glatt'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord tussen haakjes naar het Duits: 'Wir müssen die seltene Natur (beschermen/bescherming).' Vul het Duitse zelfstandig naamwoord in met lidwoord (der Naturschutz).",
                "antwoord": "der Naturschutz|Naturschutz",
                "uitleg": "Natuurbescherming is 'der Naturschutz'."
            },
            {
                "type": "invoer",
                "vraag": "Wat is het Duitse woord voor 'het eiland' (met lidwoord)?",
                "antwoord": "die Insel|Insel",
                "uitleg": "'Die Insel' betekent het eiland (meervoud: die Inseln)."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het werkwoord tussen haakjes: 'Die Forscher (observeren) die Vögel im Wald.'",
                "antwoord": "beobachten",
                "uitleg": "Observeren of bekijken is in het Duits 'beobachten'."
            }
        ]
    },

    # H2 §2.4
    {
        "id": "dui-h2-4",
        "hoofdstuk": 2,
        "paragraaf": "2.4",
        "titel": "Wortschatz & Lesekompetenz: Lernliste Deutsch, Slackline & Medische Zorg",
        "korteUitleg": "Woordenschat uit teksten over lichaamsbeheersing, evenwicht, sportuitdagingen en medicijnen bij de apotheek.",
        "icoon": "🩺",
        "kleur": "oranje",
        "theorie": """
    <h3>2.4 Wortschatz & Lesekompetenz: Lernliste Deutsch, Slackline & Medische Zorg</h3>
    <div class="info-box">
      <b>Thema:</b> Verdieping van <i>Neue Kontakte Kapitel 2</i>. Naast de lichaamsdelen leer je hier woordenschat over motoriek, training, sportblessures en een bezoek aan de apotheek of arts.
    </div>

    <h4>1. Lernliste Deutsch: Körperbeherrschung & Bewegung (Auf der Slackline)</h4>
    <p>In de leestekst en video over de slackline leer je woorden over beweging en fysieke uitdagingen:</p>
    <ul>
      <li><b>der Schritt, -e</b> = de stap (<i>einen Schritt nach vorn machen</i>)</li>
      <li><b>der Gleichgewichtssinn</b> = het evenwichtsgevoel (<i>den Gleichgewichtssinn trainieren</i>)</li>
      <li><b>die Muskeln anspannen</b> = de spieren aanspannen (tegenovergestelde: <i>locker lassen</i>)</li>
      <li><b>sich gewöhnen an (+ 4e naamval)</b> = wennen aan (<i>Man muss sich an das Seil gewöhnen</i>)</li>
      <li><b>die Herausforderung</b> = de uitdaging (<i>eine sportliche Herausforderung</i>)</li>
      <li><b>der Versuch, -e</b> = de poging (<i>beim ersten Versuch</i>)</li>
      <li><b>gelingen</b> = lukken (<i>Es ist mir gelungen</i> = het is me gelukt)</li>
      <li><b>das Lampenfieber</b> = de plankenkoorts (spanning voor een optreden)</li>
      <li><b>der Schluckauf</b> = de hik (<i>den Schluckauf loswerden</i>)</li>
      <li><b>die Geste, -n</b> = het gebaar (lichaamstaal)</li>
    </ul>

    <h4>2. In de Apotheek en bij de Dokter (Wortschatz B & Praxis)</h4>
    <p>Als je ziek bent of een blessure oploopt, heb je de volgende vaktermen nodig:</p>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:#fff3e0;">
        <th style="padding:6px;border:1px solid #ccc;">Duits 🇩🇪</th>
        <th style="padding:6px;border:1px solid #ccc;">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid #ccc;">Functie / Toelichting</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>die Praxis, Praxen</b></td><td style="padding:6px;border:1px solid #ccc;">de dokterspraktijk</td><td style="padding:6px;border:1px solid #ccc;">De werkruimte van de huisarts</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>das Rezept, -e</b></td><td style="padding:6px;border:1px solid #ccc;">het doktersrecept</td><td style="padding:6px;border:1px solid #ccc;">Briefje voor de apotheek om medicijnen te krijgen</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>das Medikament, -e</b></td><td style="padding:6px;border:1px solid #ccc;">het medicijn</td><td style="padding:6px;border:1px solid #ccc;">Middel tegen ziekte of pijn</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>die Salbe, -n</b></td><td style="padding:6px;border:1px solid #ccc;">de zalf</td><td style="padding:6px;border:1px solid #ccc;">Smeer je op een zere plek of wond</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>das Pflaster, -</b></td><td style="padding:6px;border:1px solid #ccc;">de pleister</td><td style="padding:6px;border:1px solid #ccc;">Op een klein sneetje plakken</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>der Verband, Verbände</b></td><td style="padding:6px;border:1px solid #ccc;">het verband</td><td style="padding:6px;border:1px solid #ccc;">Om een verstuikte enkel of arm binden</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>bluten / die Wunde</b></td><td style="padding:6px;border:1px solid #ccc;">bloeden / de wond</td><td style="padding:6px;border:1px solid #ccc;">Die Wunde blutet stark.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>Gute Besserung!</b></td><td style="padding:6px;border:1px solid #ccc;">Van harte beterschap!</td><td style="padding:6px;border:1px solid #ccc;">Vaste wens aan iemand die ziek is</td></tr>
    </table>

    <h4>3. Sprachmittel: Klachten en gebeurtenissen vertellen</h4>
    <div class="formule-box">
      • <b>Was fehlt Ihnen?</b> (Wat scheelt eraan? / Wat mankeert u?)<br>
      • <i>Ich habe mir beim Sport das Knie verletzt.</i> (Ik heb bij het sporten mijn knie bezeerd.)<br>
      • <i>Der Arzt hat mir ein Rezept für Tabletten und eine Salbe gegeben.</i><br>
      • <i>Ich wünsche dir eine schnelle Erholung und gute Besserung!</i>
    </div>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat wenst een Duitser als iemand ziek is of in bed ligt?",
                "opties": [
                    "Guten Appetit!",
                    "Gute Besserung!",
                    "Viel Erfolg!",
                    "Herzlichen Glückwunsch!"
                ],
                "antwoord": 1,
                "uitleg": "'Gute Besserung!' betekent van harte beterschap in het Duits."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Duitse woord 'die Herausforderung'?",
                "opties": [
                    "De ontspanning",
                    "De uitnodiging",
                    "De uitdaging",
                    "De blessure"
                ],
                "antwoord": 2,
                "uitleg": "'Die Herausforderung' is de uitdaging (bijvoorbeeld een moeilijke sportprestatie)."
            },
            {
                "type": "mc",
                "vraag": "Wat haal je bij de apotheek op basis van een doktersrecept?",
                "opties": [
                    "das Medikament",
                    "der Gleichgewichtssinn",
                    "der Schluckauf",
                    "das Lampenfieber"
                ],
                "antwoord": 0,
                "uitleg": "Met een recept haal je bij de apotheek 'das Medikament' (het medicijn)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de term 'das Lampenfieber' in het Duits?",
                "opties": [
                    "Gevaarlijke koorts door een infectie",
                    "Hoge temperatuur in een ziekenhuiskamer",
                    "Zenuwen voor een examen of toets",
                    "Gezonde spanning of plankenkoorts voor een optreden"
                ],
                "antwoord": 3,
                "uitleg": "'Das Lampenfieber' is plankenkoorts (podiumvrees of spanning voor de schijnwerpers)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'das Pflaster' betekent een gipsverband voor een gebroken been.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Das Pflaster' is een pleister voor kleine wondjes. Gips is 'der Gipsverband'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse werkwoord 'gelingen' betekent lukken of slagen.",
                "antwoord": True,
                "uitleg": "Waar! 'Gelingen' betekent lukken (bijv. 'Es wird mir gelingen')."
            },
            {
                "type": "waaronwaar",
                "vraag": "De vraag 'Was fehlt Ihnen?' betekent 'Hoeveel geld mist u?' bij de bank.",
                "antwoord": False,
                "uitleg": "Onwaar! Bij de arts betekent 'Was fehlt Ihnen?' wat er aan de hand is of wat de patiënt mankeert."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord tussen haakjes: 'Der Arzt schreibt mir ein (doktersrecept) für die Apotheke.'",
                "antwoord": "Rezept|das Rezept",
                "uitleg": "Een doktersrecept is in het Duits 'das Rezept'."
            },
            {
                "type": "invoer",
                "vraag": "Wat is het Duitse woord voor 'de zalf' (met lidwoord)?",
                "antwoord": "die Salbe|Salbe",
                "uitleg": "'Die Salbe' betekent de zalf."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord tussen haakjes: 'Man muss beim Balancieren die Muskeln (aanspannen).' Vul het Duitse werkwoord in.",
                "antwoord": "anspannen",
                "uitleg": "Spieren aanspannen is 'anspannen'."
            }
        ]
    },

    # H3 §3.4
    {
        "id": "dui-h3-4",
        "hoofdstuk": 3,
        "paragraaf": "3.4",
        "titel": "Wortschatz & Grammatik: Lernliste Deutsch, Bahnhof & Voltooid Deelwoord Modalverben",
        "korteUitleg": "Woordenschat over het treinstation, kabelbanen en aansluitingen, plus de voltooide tijd (Partizip Perfekt) van modale hulpwerkwoorden.",
        "icoon": "🚆",
        "kleur": "groen",
        "theorie": """
    <h3>3.4 Wortschatz & Grammatik: Lernliste Deutsch, Bahnhof & Voltooid Deelwoord Modalverben</h3>
    <div class="info-box">
      <b>Focus:</b> Verdieping van <i>Kapitel 3 (Unterwegs & Reisen)</i>. Je leert specifieke stations- en reiswoordenschat uit de Lernliste en het voltooid deelwoord (Partizip Perfekt) van de modale werkwoorden <i>können, müssen, dürfen, wollen, wissen</i>.
    </div>

    <h4>1. Lernliste Deutsch & Am Fernbahnhof</h4>
    <p>Op grote Duitse stations (Hauptbahnhof / Fernbahnhof) en in berggebieden zie je deze vaste begrippen:</p>
    <ul>
      <li><b>der Fernbahnhof</b> = het langeafstandsstation (voor ICE- en IC-treinen)</li>
      <li><b>die Seilbahn, -en</b> = de kabelbaan (in de bergen)</li>
      <li><b>das Gleis, -e</b> = het spoor / perron (<i>Der Zug fährt von Gleis 4 ab</i>)</li>
      <li><b>die Verbindung, -en</b> = de verbinding (<i>eine schnelle Verbindung nach Berlin</i>)</li>
      <li><b>der Anschluss, Anschlüsse</b> = de aansluiting (<i>den Anschluss verpassen</i> = de aansluiting missen)</li>
      <li><b>die Verspätung</b> = de vertraging (<i>zehn Minuten Verspätung haben</i>)</li>
      <li><b>die Auskunft, Auskünfte</b> = de inlichting / informatiebalie</li>
      <li><b>umsteigen</b> = overstappen (<i>In Köln müssen wir umsteigen</i>)</li>
      <li><b>die Hin- und Rückfahrt</b> = de retourreis (tegenover <i>einfache Fahrt</i> = enkele reis)</li>
      <li><b>die Fahrkarte / das Ticket</b> = het treinkaartje</li>
    </ul>

    <h4>2. Grammatik: Het Voltooid Deelwoord van Modale Werkwoorden</h4>
    <p>In paragraaf 3.2 leerde je de verleden tijd (Präteritum: <i>konnte, musste, durfte, wollte, wusste</i>). Soms heb je echter de voltooide tijd nodig (Perfekt met haben):</p>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:#e8f5e9;">
        <th style="padding:6px;border:1px solid #ccc;">Hele werkwoord</th>
        <th style="padding:6px;border:1px solid #ccc;">Präteritum (verleden tijd)</th>
        <th style="padding:6px;border:1px solid #ccc;">Voltooid deelwoord (Partizip)</th>
        <th style="padding:6px;border:1px solid #ccc;">Voorbeeldzin</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>können</b></td><td style="padding:6px;border:1px solid #ccc;">ich konnte</td><td style="padding:6px;border:1px solid #ccc;"><b>gekonnt</b></td><td style="padding:6px;border:1px solid #ccc;">Er hat das wirklich gut gekonnt.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>müssen</b></td><td style="padding:6px;border:1px solid #ccc;">ich musste</td><td style="padding:6px;border:1px solid #ccc;"><b>gemusst</b></td><td style="padding:6px;border:1px solid #ccc;">Ich habe gestern zur Schule gemusst.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>dürfen</b></td><td style="padding:6px;border:1px solid #ccc;">ich durfte</td><td style="padding:6px;border:1px solid #ccc;"><b>gedurft</b></td><td style="padding:6px;border:1px solid #ccc;">Wir haben das leider nicht gedurft.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>wollen</b></td><td style="padding:6px;border:1px solid #ccc;">ich wollte</td><td style="padding:6px;border:1px solid #ccc;"><b>gewollt</b></td><td style="padding:6px;border:1px solid #ccc;">Sie hat das so gewollt.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>wissen</b></td><td style="padding:6px;border:1px solid #ccc;">ich wusste</td><td style="padding:6px;border:1px solid #ccc;"><b>gewusst</b></td><td style="padding:6px;border:1px solid #ccc;">Das habe ich damals nicht gewusst!</td></tr>
    </table>
    <div class="info-box">
      <b>Belangrijke uitzondering:</b> Als er nog een <i>ander werkwoord</i> in de zin staat, gebruikt het Duits de dubbele infinitief: <i>"Ich habe nicht kommen können"</i> (in plaats van gekonnt). Alleen als het modale werkwoord zelfstandig staat, gebruik je <i>gekonnt, gewollt, gewusst</i>.
    </div>

    <h4>3. Sprachmittel: Informatie vragen op het station</h4>
    <div class="formule-box">
      • <b>Fährt dieser Zug direkt nach München?</b> (Rijdt deze trein direct naar München?)<br>
      • <i>Nein, Sie müssen in Hannover einmal umsteigen.</i><br>
      • <i>Hat der Anschlusszug aus Frankfurt Verspätung?</i><br>
      • <i>Gleiswechsel: Der ICE nach Hamburg fährt heute von Gleis 7 ab.</i>
    </div>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat is het juiste voltooid deelwoord van 'wissen' (weten)?",
                "opties": [
                    "gewusst",
                    "gewisst",
                    "gewollt",
                    "gekonnt"
                ],
                "antwoord": 0,
                "uitleg": "Het voltooid deelwoord van 'wissen' is 'gewusst' (bijv. 'Das habe ich nicht gewusst')."
            },
            {
                "type": "mc",
                "vraag": "Hoe heet het spoor of perron waar de trein vertrekt in het Duits?",
                "opties": [
                    "der Anschluss",
                    "die Seilbahn",
                    "das Gleis",
                    "die Verbindung"
                ],
                "antwoord": 2,
                "uitleg": "'Das Gleis' betekent het spoor (bijv. 'Der Zug fährt von Gleis 3')."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de stationsmededeling 'Der Zug hat zehn Minuten Verspätung'?",
                "opties": [
                    "De trein vertrekt tien minuten vroeger",
                    "De trein stopt op tien verschillende stations",
                    "De trein rijdt tien minuten sneller",
                    "De trein heeft tien minuten vertraging"
                ],
                "antwoord": 3,
                "uitleg": "'Verspätung' betekent vertraging."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits werkwoord gebruik je voor overstappen van de ene naar de andere trein?",
                "opties": [
                    "abfahren",
                    "umsteigen",
                    "einsteigen",
                    "aussteigen"
                ],
                "antwoord": 1,
                "uitleg": "'Umsteigen' betekent overstappen. 'Einsteigen' is instappen en 'aussteigen' is uitstappen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het voltooid deelwoord van 'können' is 'gekönnt' met een umlaut.",
                "antwoord": False,
                "uitleg": "Onwaar! Het voltooid deelwoord verliest de umlaut: 'gekonnt' (zonder umlaut)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een 'Seilbahn' is een kabelbaan die toeristen naar bergtoppen brengt.",
                "antwoord": True,
                "uitleg": "Waar! 'Die Seilbahn' is de kabelbaan in bergachtige gebieden."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'einfache Fahrt' betekent een reis zonder bagage.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Einfache Fahrt' betekent een enkele reis (tegenover 'Hin- und Rückfahrt' = retour)."
            },
            {
                "type": "invoer",
                "vraag": "Vul het juiste voltooid deelwoord in van 'müssen': 'Er hat gestern leider zu Hause bleiben (moeten).' Vul het Duitse voltooid deelwoord 'gemusst' in.",
                "antwoord": "gemusst",
                "uitleg": "Het voltooid deelwoord van müssen is 'gemusst'."
            },
            {
                "type": "invoer",
                "vraag": "Wat is het Duitse woord voor 'aansluiting' (bijv. van een trein)?",
                "antwoord": "der Anschluss|Anschluss",
                "uitleg": "'Der Anschluss' betekent de aansluiting."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste vorm in: 'Wir müssen am Hauptbahnhof in eine andere Bahn (overstappen).' Vul het hele werkwoord in.",
                "antwoord": "umsteigen",
                "uitleg": "Overstappen is 'umsteigen'."
            }
        ]
    },

    # H4 §4.4
    {
        "id": "dui-h4-4",
        "hoofdstuk": 4,
        "paragraaf": "4.4",
        "titel": "Grammatik & Wortschatz: Dativ (3e naamval) der- & ein-Gruppe + Feiertage",
        "korteUitleg": "De 3e naamval (Dativ) van lidwoorden en bezittelijke voornaamwoorden, plus woordenschat over feesten en de Lernliste.",
        "icoon": "🎪",
        "kleur": "paars",
        "theorie": """
    <h3>4.4 Grammatik & Wortschatz: Dativ (3e naamval) der- & ein-Gruppe + Feiertage</h3>
    <div class="info-box">
      <b>Grammatica-aanvulling:</b> In hoofdstuk 4 leerde je de 1e en 4e naamval. Het leerboek <i>Neue Kontakte</i> behandelt op pagina 35 echter ook de <b>3e naamval (Dativ)</b> voor de der-Gruppe en de ein-Gruppe!
    </div>

    <h4>1. De 3e naamval (Dativ) van de der-Gruppe</h4>
    <p>De 3e naamval gebruik je voor het <b>meewerkend voorwerp</b> (aan wie? voor wie?) en na vaste Dativ-voorzetsels:</p>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:#f3e5f5;">
        <th style="padding:6px;border:1px solid #ccc;">Naamval</th>
        <th style="padding:6px;border:1px solid #ccc;">Mannelijk</th>
        <th style="padding:6px;border:1px solid #ccc;">Vrouwelijk</th>
        <th style="padding:6px;border:1px solid #ccc;">Onzijdig</th>
        <th style="padding:6px;border:1px solid #ccc;">Meervoud</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>1. Nominativ (onderwerp)</b></td><td style="padding:6px;border:1px solid #ccc;">der Mann</td><td style="padding:6px;border:1px solid #ccc;">die Frau</td><td style="padding:6px;border:1px solid #ccc;">das Kind</td><td style="padding:6px;border:1px solid #ccc;">die Kinder</td></tr>
      <tr style="background:#ede7f6;"><td style="padding:6px;border:1px solid #ccc;"><b>3. Dativ (meew. voorwerp)</b></td><td style="padding:6px;border:1px solid #ccc;"><b>dem</b> Mann</td><td style="padding:6px;border:1px solid #ccc;"><b>der</b> Frau</td><td style="padding:6px;border:1px solid #ccc;"><b>dem</b> Kind</td><td style="padding:6px;border:1px solid #ccc;"><b>den</b> Kinder<b>n</b></td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>4. Akkusativ (lijd. voorwerp)</b></td><td style="padding:6px;border:1px solid #ccc;">den Mann</td><td style="padding:6px;border:1px solid #ccc;">die Frau</td><td style="padding:6px;border:1px solid #ccc;">das Kind</td><td style="padding:6px;border:1px solid #ccc;">die Kinder</td></tr>
    </table>
    <div class="formule-box">
      <b>Belangrijke meervoudsregel Dativ:</b> In de 3e naamval meervoud krijgt het lidwoord <b>den</b> én krijgt het zelfstandig naamwoord een extra <b>-n</b> achteraan (bijv. <i>den Kindern, den Freunden</i>), behalve als het meervoud al op -n of -s eindigt (<i>den Frauen, den Autos</i>).
    </div>

    <h4>2. De 3e naamval van de ein-Gruppe (en bezittelijke voornaamwoorden)</h4>
    <p>Woorden als <i>ein, kein, mein, dein, sein, ihr, unser, euer, ihr, Ihr</i> volgen dezelfde uitgangen:</p>
    <ul>
      <li>Mannelijk: <b>einem / meinem</b> Vater (<i>Ich helfe meinem Vater</i>)</li>
      <li>Vrouwelijk: <b>einer / meiner</b> Mutter (<i>Ich schenke meiner Mutter Blumen</i>)</li>
      <li>Onzijdig: <b>einem / unserem</b> Kind (<i>Wir geben dem Kind ein Spielzeug</i>)</li>
      <li>Meervoud: <b>keinen / unseren</b> Freunde<b>n</b> (<i>mit unseren Freunden</i>)</li>
    </ul>

    <h4>3. Lernliste: Feiern, Street-Art & Feiertage</h4>
    <p>Nieuwe begrippen uit de leesteksten van Kapitel 4:</p>
    <ul>
      <li><b>Weihnachten</b> = Kerstmis (<i>zu Weihnachten</i>)</li>
      <li><b>Ostern</b> = Pasen (<i>zu Ostern</i>) | <b>Silvester</b> = Oud en Nieuw (31 december)</li>
      <li><b>der Feiertag, -e</b> = de officiële feestdag (vrije dag)</li>
      <li><b>die Leidenschaft</b> = de passie, passievolle hobby</li>
      <li><b>das Schnäppchen</b> = het buitenkansje, voordelige koopje</li>
      <li><b>umsonst</b> = gratis, kosteloos</li>
      <li><b>die Schatten</b> = de schaduwen (bij tekenen / street-art)</li>
      <li><b>anschauen</b> = bekijken (<i>Wir wollen uns die Kunst anschauen</i>)</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat is het juiste lidwoord in de 3e naamval (Dativ) voor een vrouwelijk woord: 'Ich gebe ____ Frau das Buch'?",
                "opties": [
                    "die",
                    "der",
                    "dem",
                    "den"
                ],
                "antwoord": 1,
                "uitleg": "In de 3e naamval (Dativ) wordt het vrouwelijk lidwoord 'die' omgevormd tot 'der'."
            },
            {
                "type": "mc",
                "vraag": "Welke extra letter krijgt het zelfstandig naamwoord in de 3e naamval meervoud (bijv. mit den Kind...)?",
                "opties": [
                    "-s",
                    "-e",
                    "-n",
                    "-er"
                ],
                "antwoord": 2,
                "uitleg": "In de 3e naamval meervoud krijgt het zelfstandig naamwoord een extra '-n' (den Kindern, den Freunden)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Duitse woord 'das Schnäppchen'?",
                "opties": [
                    "Een duur cadeau",
                    "Een lekker gebakje",
                    "Een entreeticket",
                    "Een voordelig koopje"
                ],
                "antwoord": 3,
                "uitleg": "'Das Schnäppchen' betekent een voordelig koopje of buitenkansje."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het bezittelijk voornaamwoord: 'Er hilft ____ (zijn) Vater bei der Gartenarbeit.'",
                "opties": [
                    "seinem",
                    "seinen",
                    "seiner",
                    "sein"
                ],
                "antwoord": 0,
                "uitleg": "'Helfen' vraagt de 3e naamval (Dativ). 'Der Vater' is mannelijk, dus 'seinem Vater'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In het Duits betekent 'umsonst' dat een evenement geannuleerd is.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Umsonst' betekent gratis of kosteloos (bijv. 'Konzert umsonst')."
            },
            {
                "type": "waaronwaar",
                "vraag": "'Silvester' is de Duitse benaming voor Oudjaarsavond (31 december).",
                "antwoord": True,
                "uitleg": "Waar! In Duitsland heet Oudjaarsdag en de jaarovergang 'Silvester'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het mannelijke lidwoord in de 3e naamval is 'den' (den Mann).",
                "antwoord": False,
                "uitleg": "Onwaar! In de 3e naamval mannelijk is het 'dem Mann'. 'Den Mann' is de 4e naamval (Akkusativ)."
            },
            {
                "type": "invoer",
                "vraag": "Vul het juiste lidwoord in de 3e naamval in (onzijdig): 'Wir schenken ____ Kind ein Fahrrad.'",
                "antwoord": "dem",
                "uitleg": "In de 3e naamval onzijdig (das Kind) is het lidwoord 'dem'."
            },
            {
                "type": "invoer",
                "vraag": "Wat is het Duitse woord voor 'Pasen'?",
                "antwoord": "Ostern",
                "uitleg": "Pasen heet in het Duits 'Ostern'."
            },
            {
                "type": "invoer",
                "vraag": "Vul het bezittelijk voornaamwoord in de 3e naamval in (vrouwelijk): 'Ich danke ____ (mijn) Mutter für die Hilfe.'",
                "antwoord": "meiner",
                "uitleg": "Bij de 3e naamval vrouwelijk krijgt mein de uitgang -er: 'meiner Mutter'."
            }
        ]
    },

    # H5 §5.4
    {
        "id": "dui-h5-4",
        "hoofdstuk": 5,
        "paragraaf": "5.4",
        "titel": "Wortschatz & Lesekompetenz: Lernliste Deutsch, Sollicitatie & Toekomstplannen",
        "korteUitleg": "Woordenschat over solliciteren, levensloop, Abitur, stage, hbo/universiteit en toekomstplannen.",
        "icoon": "💼",
        "kleur": "roze",
        "theorie": """
    <h3>5.4 Wortschatz & Lesekompetenz: Lernliste Deutsch, Sollicitatie & Toekomstplannen</h3>
    <div class="info-box">
      <b>Thema:</b> Verdieping van <i>Kapitel 5 (Zukunft & Berufe)</i>. Je leert de essentiële woordenschat rondom solliciteren, diploma's, vervolgopleidingen en carrièrekeuzes uit de Lernliste.
    </div>

    <h4>1. Lernliste Deutsch: Solliciteren en Studie</h4>
    <p>Belangrijke begrippen uit de reportages over beroepskeuze en toekomstdromen:</p>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:#fce4ec;">
        <th style="padding:6px;border:1px solid #ccc;">Duits 🇩🇪</th>
        <th style="padding:6px;border:1px solid #ccc;">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid #ccc;">Toelichting / Voorbeeldzin</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>sich bewerben um</b></td><td style="padding:6px;border:1px solid #ccc;">solliciteren naar</td><td style="padding:6px;border:1px solid #ccc;">Ich bewerbe mich um einen Ausbildungsplatz.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>der Lebenslauf, -läufe</b></td><td style="padding:6px;border:1px solid #ccc;">het cv / de levensloop</td><td style="padding:6px;border:1px solid #ccc;">Ein tabellarischer Lebenslauf gehört zur Bewerbung.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>das Abitur (Abi)</b></td><td style="padding:6px;border:1px solid #ccc;">het vwo-eindexamendiploma</td><td style="padding:6px;border:1px solid #ccc;">Nach dem Abitur kann man an die Universität.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>die Oberstufe</b></td><td style="padding:6px;border:1px solid #ccc;">de bovenbouw (van de middelbare school)</td><td style="padding:6px;border:1px solid #ccc;">In der Oberstufe wählt man Schwerpunktfächer.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>ein Zwischenjahr einlegen</b></td><td style="padding:6px;border:1px solid #ccc;">een tussenjaar nemen</td><td style="padding:6px;border:1px solid #ccc;">Viele Jugendliche reisen nach der Schule ein Jahr.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>sich kümmern um</b></td><td style="padding:6px;border:1px solid #ccc;">zorgen voor</td><td style="padding:6px;border:1px solid #ccc;">Krankenpfleger kümmern sich um Patienten.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>die Tätigkeiten (mv)</b></td><td style="padding:6px;border:1px solid #ccc;">de werkzaamheden</td><td style="padding:6px;border:1px solid #ccc;">Welche Tätigkeiten gehören zu diesem Beruf?</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>sich anstrengen</b></td><td style="padding:6px;border:1px solid #ccc;">zich inspannen / hard werken</td><td style="padding:6px;border:1px solid #ccc;">Man muss sich anstrengen, um gute Noten zu bekommen.</td></tr>
    </table>

    <h4>2. Beroepen, Opleidingen & Bedrijfsleven (Wortschatz B)</h4>
    <p>Onderscheid de verschillende onderwijs- en werkvormen in Duitsland:</p>
    <ul>
      <li><b>das Unternehmen, -</b> / <b>die Firma</b> = de onderneming, het bedrijf</li>
      <li><b>das Praktikum, Praktika</b> = de stage (<i>ein Praktikum machen</i>)</li>
      <li><b>die Fachhochschule</b> = het hbo (hoger beroepsonderwijs)</li>
      <li><b>das Studium</b> = de universitaire studie (bijv. <i>Jura</i> = rechten, <i>Medizin</i> = geneeskunde, <i>Wirtschaft</i> = economie)</li>
      <li><b>der Nebenjob, -s</b> = het bijbaantje naast school (<i>Geld verdienen</i>)</li>
      <li><b>die Auszeit</b> = de pauze / sabbatperiode / tussenjaar</li>
      <li><b>der Mediendesigner / die Mediendesignerin</b> = grafisch / multimedia ontwerper</li>
      <li><b>der Krankenpfleger / die Krankenschwester</b> = verpleegkundige</li>
    </ul>

    <h4>3. Sprachmittel: Praten over de toekomst</h4>
    <div class="formule-box">
      • <b>Was willst du später werden?</b> (Wat wil je later worden?)<br>
      • <i>Ich möchte gern im Bereich Medien und Design arbeiten.</i><br>
      • <i>Nach dem Schulabschluss mache ich zuerst ein Praktikum in einem Unternehmen.</i><br>
      • <i>Ich habe meinen Lebenslauf geschrieben und schicke heute die Bewerbung ab.</i>
    </div>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent de Duitse uitdrukking 'sich bewerben um'?",
                "opties": [
                    "Solliciteren naar een baan of opleidingsplek",
                    "Een bedrijf overnemen",
                    "Ontslag nemen bij een werkgever",
                    "Op vakantie gaan naar het buitenland"
                ],
                "antwoord": 0,
                "uitleg": "'Sich bewerben um' betekent solliciteren naar (bijv. een baan of stage)."
            },
            {
                "type": "mc",
                "vraag": "Wat is in Duitsland het 'Abitur' (vaak afgekort als Abi)?",
                "opties": [
                    "Een getuigschrift van de basisschool",
                    "Een rijbewijs voor vrachtwagens",
                    "Het hoogste schoolexamendiploma (vwo) waarmee je naar de universiteit mag",
                    "Een bewijs van inschrijving bij het arbeidsbureau"
                ],
                "antwoord": 2,
                "uitleg": "Het 'Abitur' is het vwo-eindexamen van het Gymnasium waarmee men toegang krijgt tot de universiteit."
            },
            {
                "type": "mc",
                "vraag": "Welk studiegebied betekent 'Jura' in het Duits?",
                "opties": [
                    "Geneeskunde",
                    "Rechten / rechtsgeleerdheid",
                    "Aardrijkskunde",
                    "Economie en handel"
                ],
                "antwoord": 1,
                "uitleg": "'Jura' is de Duitse term voor de rechtenstudie."
            },
            {
                "type": "mc",
                "vraag": "Wat is een 'Lebenslauf' in een sollicitatiebrief?",
                "opties": [
                    "Een aanbeveling van een docent",
                    "Een medische verklaring van een arts",
                    "Het contract met de werkgever",
                    "Het cv (overzicht van opleidingen en werkervaring)"
                ],
                "antwoord": 3,
                "uitleg": "De 'Lebenslauf' is het curriculum vitae (cv)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'ein Zwischenjahr einlegen' betekent dat je blijft zitten op school.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Ein Zwischenjahr einlegen' betekent een tussenjaar (gap year) nemen om te reizen of te werken."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'das Praktikum' betekent een stage lopen bij een bedrijf.",
                "antwoord": True,
                "uitleg": "Waar! 'Das Praktikum' is de stage."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het werkwoord 'sich anstrengen' betekent heerlijk luieren op de bank.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Sich anstrengen' betekent zich inspannen of hard je best doen. Luieren is 'faulenzen'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord tussen haakjes: 'Sie arbeitet bei einem großen (onderneming/bedrijf).' Vul het Duitse zelfstandig naamwoord in (das Unternehmen).",
                "antwoord": "Unternehmen|das Unternehmen",
                "uitleg": "Een onderneming is 'das Unternehmen'."
            },
            {
                "type": "invoer",
                "vraag": "Wat is het Duitse woord voor een 'bijbaantje'?",
                "antwoord": "der Nebenjob|Nebenjob",
                "uitleg": "Een bijbaantje is 'der Nebenjob'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het werkwoord tussen haakjes: 'Die Krankenschwester (zorgt voor) den kranken Patienten.' Vul de persoonsvorm van kümmern in.",
                "antwoord": "kümmert sich|kümmert",
                "uitleg": "Zorgen voor is 'sich kümmern um' (sie kümmert sich)."
            }
        ]
    },

    # H6 §6.4
    {
        "id": "dui-h6-4",
        "hoofdstuk": 6,
        "paragraaf": "6.4",
        "titel": "Grammatik & Wortschatz: Vaste Voorzetsels met Dativ & Akkusativ + Hulpdiensten",
        "korteUitleg": "Vaste voorzetsels die altijd de 3e naamval (Dativ) of altijd de 4e naamval (Akkusativ) krijgen, plus reddingswerk en hulpdiensten.",
        "icoon": "🚑",
        "kleur": "geel",
        "theorie": """
    <h3>6.4 Grammatik & Wortschatz: Vaste Voorzetsels met Dativ & Akkusativ + Hulpdiensten</h3>
    <div class="info-box">
      <b>Grammaticaal Hoogtepunt:</b> In hoofdstuk 6 (pagina 35 van Neue Kontakte) leer je de <b>vaste voorzetsels</b>. Na deze voorzetsels hoef je niet te ontleden: het voorzetsel bepaalt 100% zeker of er een 3e of 4e naamval volgt!
    </div>

    <h4>1. Vaste voorzetsels met de 3e naamval (Dativ)</h4>
    <p>Onthoud het bekende rijtje uit je hoofd:</p>
    <div class="formule-box" style="background:#fffde7;font-size:1.05em;">
      <b>Dativ-voorzetsels (altijd 3e naamval):</b><br>
      <b>aus — bei — mit — nach — seit — von — zu</b>
    </div>
    <ul>
      <li><b>aus</b> (uit): <i>Er kommt aus <b>dem</b> Haus.</i></li>
      <li><b>bei</b> (bij): <i>Ich schlafe bei <b>meinem</b> Freund.</i> (let op samentrekking: <i>beim</i> = bei dem)</li>
      <li><b>mit</b> (met): <i>Wir fahren mit <b>der</b> U-Bahn.</i></li>
      <li><b>nach</b> (naar / na): <i>Nach <b>der</b> Schule gehen wir zum Sport.</i></li>
      <li><b>seit</b> (sinds): <i>Seit <b>einem</b> Jahr wohnt sie in Berlin.</i></li>
      <li><b>von</b> (van): <i>Das ist ein Brief von <b>meiner</b> Oma.</i> (samentrekking: <i>vom</i> = von dem)</li>
      <li><b>zu</b> (naar): <i>Kommst du mit zu <b>den</b> Freunden?</i> (samentrekkingen: <i>zum</i> = zu dem, <i>zur</i> = zu der)</li>
    </ul>

    <h4>2. Vaste voorzetsels met de 4e naamval (Akkusativ)</h4>
    <p>Deze voorzetsels worden altijd gevolgd door de 4e naamval:</p>
    <div class="formule-box" style="background:#e0f7fa;font-size:1.05em;">
      <b>Akkusativ-voorzetsels (altijd 4e naamval):</b><br>
      <b>bis — durch — für — gegen — ohne — um</b>
    </div>
    <ul>
      <li><b>bis</b> (tot): <i>Der Zug fährt bis <b>den</b> nächsten Bahnhof.</i></li>
      <li><b>durch</b> (door): <i>Das Auto fährt durch <b>den</b> langen Tunnel.</i> (der Tunnel -> den Tunnel)</li>
      <li><b>für</b> (voor): <i>Das Geschenk ist für <b>meinen</b> Bruder.</i></li>
      <li><b>gegen</b> (tegen): <i>Der Radfahrer fuhr gegen <b>einen</b> Baum.</i></li>
      <li><b>ohne</b> (zonder): <i>Ohne <b>meinen</b> Ausweis darf ich nicht mit.</i></li>
      <li><b>um</b> (om / rondom): <i>Wir laufen um <b>den</b> schönen See.</i></li>
    </ul>

    <h4>3. Woordenschat: Hulpdiensten, Noodgevallen & Vrijwilligerswerk</h4>
    <p>Begrippen rond burgerhulp en reddingswerk (Lernliste & Wortschatz B):</p>
    <ul>
      <li><b>die Feuerwehr</b> = de brandweer | <b>der Krankenwagen</b> = de ambulance</li>
      <li><b>die Polizei</b> = de politie | <b>der Katastrophenschutz</b> = de rampenbestrijding</li>
      <li><b>die DLRG</b> = Deutsche Lebens-Rettungs-Gesellschaft (reddingsbrigade aan het water)</li>
      <li><b>der Diebstahl</b> = de diefstal | <b>der Ausweis</b> = het identiteitsbewijs</li>
      <li><b>das Portmonee</b> = de portemonnee | <b>Anzeige erstatten</b> = aangifte doen bij de politie</li>
      <li><b>die ehrenamtliche Arbeit</b> = het vrijwilligerswerk | <b>spenden</b> = doneren</li>
      <li><b>Feuer!</b> (Brand!) | <b>Hilfe!</b> (Help!) | <b>Vorsicht!</b> (Pas op!)</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Welk voorzetsel hoort in het rijtje van vaste 3e naamval (Dativ): aus, bei, mit, nach, seit, von, ...?",
                "opties": [
                    "zu",
                    "durch",
                    "ohne",
                    "gegen"
                ],
                "antwoord": 0,
                "uitleg": "'Zu' hoort bij de vaste Dativ-voorzetsels (aus, bei, mit, nach, seit, von, zu)."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het lidwoord na het Akkusativ-voorzetsel 'für': 'Das ist ein Geschenk für ____ (de) Vater.'",
                "opties": [
                    "dem",
                    "den",
                    "der",
                    "des"
                ],
                "antwoord": 1,
                "uitleg": "'Für' vraagt altijd de 4e naamval (Akkusativ). Mannelijk 'der Vater' wordt 'den Vater'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Duitse uitdrukking 'Anzeige erstatten'?",
                "opties": [
                    "Een advertentie in de krant plaatsen",
                    "Vrijwilliger worden bij de brandweer",
                    "Aangifte doen bij de politie",
                    "Geld inzamelen voor een goed doel"
                ],
                "antwoord": 2,
                "uitleg": "'Anzeige erstatten' betekent officieel aangifte doen bij de politie (bijv. na een diefstal)."
            },
            {
                "type": "mc",
                "vraag": "Welk voorzetsel vereist altijd de 4e naamval (Akkusativ)?",
                "opties": [
                    "mit",
                    "nach",
                    "von",
                    "ohne"
                ],
                "antwoord": 3,
                "uitleg": "'Ohne' staat in het vaste rijtje van de 4e naamval: bis, durch, für, gegen, ohne, um."
            },
            {
                "type": "waaronwaar",
                "vraag": "Na het voorzetsel 'mit' gebruik je altijd de 4e naamval (Akkusativ).",
                "antwoord": False,
                "uitleg": "Onwaar! 'Mit' is een vast voorzetsel met de 3e naamval (Dativ): mit dem Bus, mit der Bahn."
            },
            {
                "type": "waaronwaar",
                "vraag": "De DLRG is in Duitsland de reddingsorganisatie die actief is op en rond het water.",
                "antwoord": True,
                "uitleg": "Waar! De DLRG (Deutsche Lebens-Rettungs-Gesellschaft) bewaakt stranden, meren en rivieren."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'die Feuerwehr' betekent de politiehelikopter.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Die Feuerwehr' is de brandweer."
            },
            {
                "type": "invoer",
                "vraag": "Vul het juiste lidwoord in na het Dativ-voorzetsel 'mit': 'Wir fahren mit ____ (de) Bus zur Schule.'",
                "antwoord": "dem",
                "uitleg": "Mannelijk 'der Bus' wordt in de 3e naamval na 'mit': 'mit dem Bus'."
            },
            {
                "type": "invoer",
                "vraag": "Vul het juiste voorzetsel in dat 'zonder' betekent: 'Er geht ____ (zonder) seine Jacke nach draußen.'",
                "antwoord": "ohne",
                "uitleg": "Zonder is 'ohne' (vaste 4e naamval)."
            },
            {
                "type": "invoer",
                "vraag": "Wat roep je in het Duits als er plotseling vlammen uitslaan? Vul het Duitse woord in (één woord met uitroepteken niet verplicht).",
                "antwoord": "Feuer|Feuer!",
                "uitleg": "Bij brand roept men 'Feuer!'."
            }
        ]
    }
]

EXAMENS = [
    # Toets 31 (H1)
    {
        "id": "ex-h3-duits-31",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Umgebung & Wetter",
        "titel": "Toets 31 — H1 Integrale Woordenschat, Lezen & Omgeving",
        "duurMin": 20,
        "vak": "Duits HAVO 3 — Hoofdstuk 1",
        "icoon": "🌲",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Welk Duits begrip omschrijft 'de gevolgen van de opwarming van de aarde'?",
                "opties": [
                    "die Auswirkungen des Klimawandels",
                    "die Begeisterung für den Naturschutz",
                    "die Ausblicke auf das Gebirge",
                    "die Unwetter in der Großstadt"
                ],
                "antwoord": 0,
                "uitleg": "'Die Auswirkungen des Klimawandels' betekent de gevolgen of uitwerkingen van de klimaatverandering."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste Duitse uitdrukking voor 'benieuwd zijn naar de bergen'?",
                "opties": [
                    "auf die Berge klettern",
                    "gespannt sein auf die Berge",
                    "die Berge beobachten",
                    "sich in den Bergen auskennen"
                ],
                "antwoord": 1,
                "uitleg": "'Gespannt sein auf' betekent benieuwd zijn naar."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Duits dat je op de camping in een tent verblijft?",
                "opties": [
                    "Wir wandern im Wald.",
                    "Wir grillen am See.",
                    "Wir zelten auf dem Campingplatz.",
                    "Wir frieren am Strand."
                ],
                "antwoord": 2,
                "uitleg": "'Zelten' betekent kamperen in een tent."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste combinatie van lidwoord en voorzetsel: 'Wir fahren ____ (in het oosten) von Deutschland.'",
                "opties": [
                    "am Osten",
                    "nach Osten",
                    "vom Osten",
                    "im Osten"
                ],
                "antwoord": 3,
                "uitleg": "Bij windrichtingen gebruik je 'im' (im Osten, im Westen, im Norden, im Süden)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de waarschuwing 'Vorsicht, die Straße ist spiegelglatt!'?",
                "opties": [
                    "Pas op, de weg is spiegelglad door ijzel of vorst!",
                    "Kijk uit, er ligt veel modder op de rijbaan!",
                    "Let op, de weg is afgesloten wegens werkzaamheden!",
                    "Pas op, er is dichte mist in de vallei!"
                ],
                "antwoord": 0,
                "uitleg": "'Glatt' betekent glad; 'spiegelglatt' is spiegelglad."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits zelfstandig naamwoord betekent 'de natuurbescherming'?",
                "opties": [
                    "die Umgebung",
                    "der Naturschutz",
                    "der Klimawandel",
                    "das Gewitter"
                ],
                "antwoord": 1,
                "uitleg": "'Der Naturschutz' betekent de natuurbescherming."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het werkwoord 'zerstören' in een verslag over een zware storm?",
                "opties": [
                    "voorspellen",
                    "ontdekken",
                    "verwoesten of vernielen",
                    "beschermen"
                ],
                "antwoord": 2,
                "uitleg": "'Zerstören' betekent verwoesten of kapotmaken."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vertaling: 'Van de toren heeft men een prachtig uitzicht over het dal.'",
                "opties": [
                    "Vom Turm hat man eine tolle Begeisterung.",
                    "Vom Turm hat man eine gute Nahrung.",
                    "Vom Turm hat man eine ruhige Umgebung.",
                    "Vom Turm hat man einen herrlichen Ausblick über das Tal."
                ],
                "antwoord": 3,
                "uitleg": "'Der Ausblick' is het uitzicht."
            },
            {
                "type": "mc",
                "vraag": "Wat is het meervoud van 'der Fels' (de rots) in het Duits?",
                "opties": [
                    "die Felsen",
                    "die Felse",
                    "die Felsenisse",
                    "die Felsenmänner"
                ],
                "antwoord": 0,
                "uitleg": "Het meervoud van 'der Fels' is 'die Felsen'."
            },
            {
                "type": "mc",
                "vraag": "Welk woord vult de zin correct aan: 'Er ist ein ____ (betrouwbare) Wetterexperte.'?",
                "opties": [
                    "hektischer",
                    "zuverlässiger",
                    "glatter",
                    "enger"
                ],
                "antwoord": 1,
                "uitleg": "'Zuverlässig' betekent betrouwbaar."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het als iemand zegt: 'Ich kenne mich hier in den Bergen gut aus'?",
                "opties": [
                    "Ik ben hier nog nooit eerder geweest.",
                    "Ik wil hier zo snel mogelijk weg.",
                    "Ik weet hier goed de weg en ken het gebied.",
                    "Ik vind de bergen veel te gevaarlijk."
                ],
                "antwoord": 2,
                "uitleg": "'Sich auskennen' betekent goed de weg weten of ergens mee vertrouwd zijn."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits woord betekent 'het eiland'?",
                "opties": [
                    "die Gegend",
                    "das Dorf",
                    "der Ort",
                    "die Insel"
                ],
                "antwoord": 3,
                "uitleg": "'Die Insel' betekent het eiland (bijv. Rügen of Sylt)."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "In het Duits betekent 'das Meer' een klein zoetwatermeer op het platteland.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Das Meer' is de zee (zout water). Een zoetwatermeer heet in het Duits 'der See'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse werkwoord 'beobachten' betekent aandachtig observeren of bekijken.",
                "antwoord": True,
                "uitleg": "Waar! 'Beobachten' betekent observeren (bijvoorbeeld vogels of het weer)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'hektisch' betekent vredig, doodstil en ontspannen.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Hektisch' betekent druk en jachtig. Rustig is 'ruhig'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het begrip 'die Nahrung' verwijst naar voedingsstoffen of eten voor mensen en dieren.",
                "antwoord": True,
                "uitleg": "Waar! 'Die Nahrung' betekent voeding of voedsel."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het Duitse woord in voor 'klimmen': 'Die Bergsteiger ____ vorsichtig über die steile Wand.'",
                "antwoord": "klettern",
                "uitleg": "Klimmen is in het Duits 'klettern'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'Wir machen Ferien (in het zuiden) von Österreich.' Vul het juiste voorzetsel plus windrichting in (im Süden).",
                "antwoord": "im Süden",
                "uitleg": "In het zuiden vertaal je met 'im Süden'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem twee natuurlijke kenmerken waarmee je een Duitse landstreek kunt omschrijven.",
                "modelantwoord": "Je kunt de streek omschrijven met heuvels, bergen, bossen, meren of rivieren.",
                "sleutelwoorden": [
                    "heuvel/berg/bos/meer/rivier",
                    "Wald/Berg/See/Fluss"
                ],
                "minTreffers": 1,
                "uitleg": "Landschapskenmerken zijn bijvoorbeeld bergen (Berge), bossen (Wälder) of rivieren (Flüsse)."
            },
            {
                "type": "open",
                "vraag": "Leg uit wat er bedoeld wordt met het begrip natuurbehoud en geef een Duits synoniem.",
                "modelantwoord": "Het beschermen van planten en dieren, aangeduid met het woord Naturschutz.",
                "sleutelwoorden": [
                    "bescherm/beheer/milieu",
                    "Naturschutz"
                ],
                "minTreffers": 1,
                "uitleg": "Natuurbescherming is in het Duits 'der Naturschutz'."
            }
        ]
    },

    # Toets 32 (H2)
    {
        "id": "ex-h3-duits-32",
        "hoofdstuk": 2,
        "hoofdstukTitel": "Gesundheit & Körper",
        "titel": "Toets 32 — H2 Integrale Woordenschat, Gezondheid & Apotheek",
        "duurMin": 20,
        "vak": "Duits HAVO 3 — Hoofdstuk 2",
        "icoon": "🩺",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent de term 'der Gleichgewichtssinn' die men traint op een slackline?",
                "opties": [
                    "het evenwichtsgevoel",
                    "de spierkracht in de benen",
                    "de ademhalingstechniek",
                    "de reactiesnelheid"
                ],
                "antwoord": 0,
                "uitleg": "'Der Gleichgewichtssinn' is het evenwichtsorgaan of het evenwichtsgevoel."
            },
            {
                "type": "mc",
                "vraag": "Welk voorwerp plak je op een klein sneetje in je vinger?",
                "opties": [
                    "eine Tablette",
                    "ein Pflaster",
                    "eine Salbe",
                    "ein Rezept"
                ],
                "antwoord": 1,
                "uitleg": "Een pleister heet in het Duits 'das Pflaster'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de wens 'Gute Besserung!'?",
                "opties": [
                    "Gefeliciteerd met je overwinning!",
                    "Goede reis naar huis!",
                    "Van harte beterschap!",
                    "Eet smakelijk!"
                ],
                "antwoord": 2,
                "uitleg": "'Gute Besserung!' wens je iemand toe die ziek of gewond is."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits woord betekent 'de dokterspraktijk'?",
                "opties": [
                    "das Krankenhaus",
                    "die Apotheke",
                    "das Wartezimmer",
                    "die Praxis"
                ],
                "antwoord": 3,
                "uitleg": "'Die Praxis' is de dokterspraktijk van de behandelend arts."
            },
            {
                "type": "mc",
                "vraag": "Wat geeft een arts aan de patiënt mee om medicijnen op te halen bij de apotheek?",
                "opties": [
                    "das Rezept",
                    "die Versicherung",
                    "das Pflaster",
                    "die Geste"
                ],
                "antwoord": 0,
                "uitleg": "'Das Rezept' is het officiële doktersvoorschrift of doktersrecept."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Duitse werkwoord 'bluten'?",
                "opties": [
                    "genezen",
                    "bloeden",
                    "hoesten",
                    "ontspannen"
                ],
                "antwoord": 1,
                "uitleg": "'Bluten' betekent bloeden (bijvoorbeeld uit een open wond)."
            },
            {
                "type": "mc",
                "vraag": "Hoe noemt men in het Duits 'plankenkoorts' of nervositeit voor een presentatie?",
                "opties": [
                    "der Schluckauf",
                    "die Herausforderung",
                    "das Lampenfieber",
                    "der Gleichgewichtssinn"
                ],
                "antwoord": 2,
                "uitleg": "'Das Lampenfieber' is plankenkoorts of spanning voor een optreden."
            },
            {
                "type": "mc",
                "vraag": "Wat smeer je op een pijnlijke spier of een verstuikte enkel?",
                "opties": [
                    "ein Rezept",
                    "eine Tablette",
                    "ein Pflaster",
                    "eine Salbe"
                ],
                "antwoord": 3,
                "uitleg": "'Die Salbe' is zalf."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste Duitse woord voor 'de uitdaging': 'Für Sportler ist dieser Wettkampf eine große ____.'",
                "opties": [
                    "Herausforderung",
                    "Besserung",
                    "Praxis",
                    "Wunde"
                ],
                "antwoord": 0,
                "uitleg": "'Die Herausforderung' is de uitdaging."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Duitse werkwoord 'gelingen'?",
                "opties": [
                    "mislukken",
                    "lukken / slagen",
                    "vallen",
                    "wennen"
                ],
                "antwoord": 1,
                "uitleg": "'Gelingen' betekent lukken of slagen (bijv. 'Der Trick ist gelungen')."
            },
            {
                "type": "mc",
                "vraag": "Welke betekenis heeft 'der Schluckauf' in de volksmond?",
                "opties": [
                    "de verkoudheid",
                    "de spierpijn",
                    "de hik",
                    "de koorts"
                ],
                "antwoord": 2,
                "uitleg": "'Der Schluckauf' is de hik."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de vraag van de dokter: 'Was fehlt Ihnen denn?'?",
                "opties": [
                    "Welke zorgverzekering heeft u?",
                    "Wanneer bent u voor het laatst hier geweest?",
                    "Hoeveel weegt u op dit moment?",
                    "Wat scheelt eraan? / Waar heeft u last van?"
                ],
                "antwoord": 3,
                "uitleg": "'Was fehlt Ihnen?' is de standaardvraag van de Duitse arts: wat scheelt eraan?"
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse zelfstandig naamwoord 'der Schritt' betekent een harde val op de grond.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Der Schritt' betekent de pas of de stap (bijv. einen Schritt gehen)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het werkwoord 'sich gewöhnen an' betekent ergens aan wennen.",
                "antwoord": True,
                "uitleg": "Waar! 'Sich gewöhnen an' betekent wennen aan (bijvoorbeeld aan een wiebelende kabel)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het woord 'die Praxis' betekent uitsluitend een praktijkles op school.",
                "antwoord": False,
                "uitleg": "Onwaar! In medische context betekent 'die Praxis' de dokterspraktijk of tandartspraktijk."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een 'Verband' wordt gebruikt om een gewricht te fixeren of een wond te verbinden.",
                "antwoord": True,
                "uitleg": "Waar! 'Der Verband' is het medische verband."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'Ich hole die verordneten (medicijnen) aus der Apotheke.' Vul het Duitse woord in (Medikamente).",
                "antwoord": "Medikamente|die Medikamente",
                "uitleg": "Medicijnen zijn in het Duits 'die Medikamente'."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste wens in bij ziekte: 'Ich wünsche dir gute ____ (beterschap)!'",
                "antwoord": "Besserung",
                "uitleg": "De vaste uitdrukking is 'Gute Besserung!'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Welke standaardvraag stelt een Duitse arts aan het begin van het consult?",
                "modelantwoord": "De arts vraagt naar je klachten met de vaste vraag: Was fehlt Ihnen?",
                "sleutelwoorden": [
                    "Was fehlt Ihnen/fehlt",
                    "klachten/Beschwerden"
                ],
                "minTreffers": 1,
                "uitleg": "De vaste vraag van de arts luidt 'Was fehlt Ihnen?' (Wat scheelt eraan?)."
            },
            {
                "type": "open",
                "vraag": "Noem twee hulpmiddelen uit het EHBO-kistje of de apotheek bij een schaafwond.",
                "modelantwoord": "Je gebruikt een pleister, zalf of een verband om de wond te verzorgen.",
                "sleutelwoorden": [
                    "pleister/zalf/verband",
                    "Pflaster/Salbe/Verband"
                ],
                "minTreffers": 1,
                "uitleg": "Medische hulpmiddelen zijn das Pflaster, die Salbe of der Verband."
            }
        ]
    },

    # Toets 33 (H3)
    {
        "id": "ex-h3-duits-33",
        "hoofdstuk": 3,
        "hoofdstukTitel": "Unterwegs & Reisen",
        "titel": "Toets 33 — H3 Reizen, Station & Voltooid Deelwoord",
        "duurMin": 20,
        "vak": "Duits HAVO 3 — Hoofdstuk 3",
        "icoon": "🚆",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat is het juiste voltooid deelwoord van het modale hulpwerkwoord 'können'?",
                "opties": [
                    "gekonnt",
                    "gekönnt",
                    "gekannt",
                    "konnte"
                ],
                "antwoord": 0,
                "uitleg": "Het voltooid deelwoord van können is 'gekonnt' (zonder umlaut)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de afkorting 'Hbf' op Duitse stationsborden?",
                "opties": [
                    "Hafenbahnhof",
                    "Hauptbahnhof",
                    "Haltestelle Bus Fernverkehr",
                    "Hochgeschwindigkeitsbahn"
                ],
                "antwoord": 1,
                "uitleg": "'Hbf' staat voor 'Hauptbahnhof' (centraal station)."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits woord betekent 'de kabelbaan' in de bergen?",
                "opties": [
                    "die Autobahn",
                    "die U-Bahn",
                    "die Seilbahn",
                    "die Straßenbahn"
                ],
                "antwoord": 2,
                "uitleg": "'Die Seilbahn' is de kabelbaan."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste voltooid deelwoord: 'Das habe ich wirklich nicht ____ (weten).' ",
                "opties": [
                    "gewollt",
                    "gemusst",
                    "gedurft",
                    "gewusst"
                ],
                "antwoord": 3,
                "uitleg": "Het voltooid deelwoord van wissen is 'gewusst'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het stationsbericht 'Der ICE nach Berlin fährt heute von Gleis 5 ab'?",
                "opties": [
                    "De sneltrein naar Berlijn vertrekt vandaag vanaf spoor 5.",
                    "De trein uit Berlijn arriveert met 5 minuten vertraging.",
                    "Reizigers naar Berlijn moeten overstappen op perron 5.",
                    "De trein naar Berlijn stopt op 5 verschillende stations."
                ],
                "antwoord": 0,
                "uitleg": "'Gleis 5' betekent spoor 5."
            },
            {
                "type": "mc",
                "vraag": "Wat is de Duitse term voor een retourkaartje bij de trein?",
                "opties": [
                    "einfache Fahrt",
                    "Hin- und Rückfahrt",
                    "Gleiswechsel",
                    "die Auskunft"
                ],
                "antwoord": 1,
                "uitleg": "'Hin- und Rückfahrt' is een retourtje (heen en terug)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Duitse werkwoord 'umsteigen'?",
                "opties": [
                    "instappen",
                    "uitstappen",
                    "overstappen",
                    "vertrekken"
                ],
                "antwoord": 2,
                "uitleg": "'Umsteigen' is overstappen op een andere trein of bus."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste voltooid deelwoord van 'wollen': 'Das hat mein Bruder so ____.'",
                "opties": [
                    "gewellt",
                    "wollte",
                    "gewusst",
                    "gewollt"
                ],
                "antwoord": 3,
                "uitleg": "Het voltooid deelwoord van wollen is 'gewollt'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de term 'der Anschluss' bij het reizen per spoor?",
                "opties": [
                    "de aansluitende trein / aansluiting",
                    "de prijs van het ticket",
                    "het bagagedepot",
                    "de restauratiewagen"
                ],
                "antwoord": 0,
                "uitleg": "'Der Anschluss' is de aansluiting op een volgende trein of bus."
            },
            {
                "type": "mc",
                "vraag": "Wat is het juiste voltooid deelwoord van 'müssen'?",
                "opties": [
                    "gemüsst",
                    "gemusst",
                    "musste",
                    "gemacht"
                ],
                "antwoord": 1,
                "uitleg": "Het voltooid deelwoord van müssen is 'gemusst' (zonder umlaut)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent 'die Auskunft' in een stationshal?",
                "opties": [
                    "de nooduitgang",
                    "het bagagerek",
                    "de inlichting / informatiedesk",
                    "de kaartjesautomaat"
                ],
                "antwoord": 2,
                "uitleg": "'Die Auskunft' is de inlichting of informatiebalie."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het als een trein 'zehn Minuten Verspätung' heeft?",
                "opties": [
                    "De trein rijdt 10 km/h langzamer",
                    "De rit duurt 10 minuten korter",
                    "Er zijn nog 10 zitplaatsen vrij",
                    "De trein arriveert 10 minuten later dan gepland"
                ],
                "antwoord": 3,
                "uitleg": "'Verspätung' betekent vertraging."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het voltooid deelwoord van 'dürfen' is 'gedurft' zonder umlaut.",
                "antwoord": True,
                "uitleg": "Waar! Net als gekonnt en gemusst verliest ook 'gedurft' zijn umlaut."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'einfache Fahrt' betekent dat de treinreis gratis is voor kinderen.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Einfache Fahrt' is een enkele reis."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een 'Fernbahnhof' is een station speciaal bedoeld voor langeafstandstreinen zoals ICE en IC.",
                "antwoord": True,
                "uitleg": "Waar! 'Fernverkehr' betreft het langeafstandsvervoer per spoor."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'das Gleis' betekent de conducteur van de trein.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Das Gleis' betekent het spoor of perronspoor."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste vorm in: 'Wir haben in Frankfurt den nächsten Zug (overstappen).' Vul het hele werkwoord in.",
                "antwoord": "umsteigen",
                "uitleg": "Overstappen is in het Duits 'umsteigen'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'Der Zug fährt von (spoor) 4 ab.'",
                "antwoord": "Gleis",
                "uitleg": "Spoor is in het Duits 'das Gleis'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Hoe vraag je bij het loket beleefd of je moet overstappen voor de reis naar Hamburg?",
                "modelantwoord": "Muss ich bei der Fahrt nach Hamburg umsteigen?",
                "sleutelwoorden": [
                    "umsteigen",
                    "Muss ich/muss man"
                ],
                "minTreffers": 1,
                "uitleg": "Vraag met 'umsteigen', bijvoorbeeld: 'Muss ich nach Hamburg umsteigen?'."
            },
            {
                "type": "open",
                "vraag": "Noem het Duitse voltooid deelwoord van de werkwoorden 'können' en 'wissen'.",
                "modelantwoord": "De voltooide deelwoorden zijn gekonnt en gewusst.",
                "sleutelwoorden": [
                    "gekonnt",
                    "gewusst"
                ],
                "minTreffers": 2,
                "uitleg": "De voltooide deelwoorden zijn gekonnt en gewusst."
            }
        ]
    },

    # Toets 34 (H4)
    {
        "id": "ex-h3-duits-34",
        "hoofdstuk": 4,
        "hoofdstukTitel": "Veranstaltungen & Feiern",
        "titel": "Toets 34 — H4 Dativ (3e naamval), Feesten & Evenementen",
        "duurMin": 20,
        "vak": "Duits HAVO 3 — Hoofdstuk 4",
        "icoon": "🎪",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Welke vorm krijgt het lidwoord in de 3e naamval (Dativ) bij een mannelijk zelfstandig naamwoord?",
                "opties": [
                    "dem",
                    "den",
                    "der",
                    "des"
                ],
                "antwoord": 0,
                "uitleg": "In de 3e naamval mannelijk verandert 'der' in 'dem' (bijv. dem Mann)."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met het zelfstandig naamwoord in de 3e naamval meervoud (bijv. mit den Kind...)?",
                "opties": [
                    "Het krijgt een extra -s achteraan",
                    "Het krijgt een extra -n achteraan (behalve bij meervoud op -n of -s)",
                    "Het verandert helemaal niet van vorm",
                    "Het krijgt altijd een extra umlaut"
                ],
                "antwoord": 1,
                "uitleg": "In de 3e naamval meervoud krijgt het zelfstandig naamwoord een extra -n (den Kindern, den Freunden)."
            },
            {
                "type": "mc",
                "vraag": "Hoe heet het traditionele christelijke voorjaarsfeest in Duitsland?",
                "opties": [
                    "Weihnachten",
                    "Silvester",
                    "Ostern",
                    "Karneval"
                ],
                "antwoord": 2,
                "uitleg": "Pasen heet in het Duits 'Ostern'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het woord 'umsonst' als het gaat om een straatfestival?",
                "opties": [
                    "verboden voor minderjarigen",
                    "alleen toegankelijk met reservering",
                    "heel erg duur",
                    "gratis / kosteloos toegankelijk"
                ],
                "antwoord": 3,
                "uitleg": "'Umsonst' betekent gratis of kosteloos."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste Dativ-vorm van het bezittelijk voornaamwoord: 'Ich schenke ____ (mijn) Mutter ein Buch.'",
                "opties": [
                    "meiner",
                    "meine",
                    "meinem",
                    "meinen"
                ],
                "antwoord": 0,
                "uitleg": "Vrouwelijk in de 3e naamval (Dativ) krijgt de uitgang -er: 'meiner Mutter'."
            },
            {
                "type": "mc",
                "vraag": "Wat is een 'Schnäppchen' in een Duitse winkel?",
                "opties": [
                    "een kassabon",
                    "een voordelig koopje",
                    "een kortingsbon",
                    "een beschadigd product"
                ],
                "antwoord": 1,
                "uitleg": "'Das Schnäppchen' is een voordelig koopje."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm voor het meervoud in de Dativ: 'Wir reisen mit unseren ____ (vrienden).' ",
                "opties": [
                    "Freunde",
                    "Freund",
                    "Freunden",
                    "Freundes"
                ],
                "antwoord": 2,
                "uitleg": "In de Dativ meervoud krijgt het woord Freunde een extra -n: 'unseren Freunden'."
            },
            {
                "type": "mc",
                "vraag": "Wat vieren mensen in Duitsland op de avond van 31 december?",
                "opties": [
                    "Ostern",
                    "Pfingsten",
                    "Weihnachten",
                    "Silvester"
                ],
                "antwoord": 3,
                "uitleg": "Oud en Nieuw heet in het Duits 'Silvester'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het lidwoord: 'Der Lehrer hilft ____ (het) Kind bei den Aufgaben.'",
                "opties": [
                    "dem",
                    "das",
                    "des",
                    "den"
                ],
                "antwoord": 0,
                "uitleg": "Onzijdig 'das Kind' wordt in de 3e naamval (Dativ) 'dem Kind'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Duitse woord 'die Leidenschaft'?",
                "opties": [
                    "het verdriet",
                    "de passie / grote liefhebberij",
                    "de vermoeidheid",
                    "de ruzie"
                ],
                "antwoord": 1,
                "uitleg": "'Die Leidenschaft' betekent de passie of grote passievolle hobby."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits werkwoord betekent 'bekijken' (bijvoorbeeld schilderijen of street-art)?",
                "opties": [
                    "darstellen",
                    "überzeugen",
                    "anschauen",
                    "auswählen"
                ],
                "antwoord": 2,
                "uitleg": "'Sich etwas anschauen' betekent iets bekijken."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de feestdag 'Weihnachten' in het Nederlands?",
                "opties": [
                    "Pasen",
                    "Pinksteren",
                    "Hemelvaart",
                    "Kerstmis"
                ],
                "antwoord": 3,
                "uitleg": "'Weihnachten' is Kerstmis."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "In de 3e naamval (Dativ) verandert het vrouwelijke lidwoord 'die' in 'der'.",
                "antwoord": True,
                "uitleg": "Waar! In de Dativ wordt die Frau -> der Frau."
            },
            {
                "type": "waaronwaar",
                "vraag": "Als een meervoud in het Duits al eindigt op -s (zoals Autos), krijgt het in de Dativ nog een extra -n.",
                "antwoord": False,
                "uitleg": "Onwaar! Woorden die al eindigen op -s of -n krijgen in de Dativ meervoud géén extra -n (mit den Autos)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een 'Feiertag' is in Duitsland een officiële vrije dag wegens een nationale of religieuze herdenking.",
                "antwoord": True,
                "uitleg": "Waar! 'Der Feiertag' is een officiële feestdag waarop scholen en winkels gesloten zijn."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'der Bleistift' betekent een spuitbus met graffiti-verf.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Der Bleistift' is gewoon een potlood om mee te schetsen."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het juiste lidwoord in de 3e naamval in: 'Ich danke ____ (de) Vater für das schöne Geschenk.'",
                "antwoord": "dem",
                "uitleg": "Mannelijk 'der Vater' wordt in de 3e naamval 'dem Vater'."
            },
            {
                "type": "invul",
                "vraag": "Wat is het Duitse woord voor de feestdag 'Oud en Nieuw' (31 december)?",
                "antwoord": "Silvester",
                "uitleg": "Oud en Nieuw heet in het Duits 'Silvester'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Leg uit waarom 'mit den Freunden' een extra n achteraan krijgt in het Duits.",
                "modelantwoord": "In de derde naamval meervoud krijgt het zelfstandig naamwoord een extra n.",
                "sleutelwoorden": [
                    "derde naamval/Dativ",
                    "meervoud"
                ],
                "minTreffers": 1,
                "uitleg": "In de Dativ meervoud krijgt het zelfstandig naamwoord een extra -n (den Freunden)."
            },
            {
                "type": "open",
                "vraag": "Welke twee lidwoorden gebruik je in de 3e naamval enkelvoud voor respectievelijk mannelijk en vrouwelijk?",
                "modelantwoord": "Voor mannelijk gebruik je dem en voor vrouwelijk gebruik je der.",
                "sleutelwoorden": [
                    "dem",
                    "der"
                ],
                "minTreffers": 2,
                "uitleg": "De Dativ-lidwoorden zijn dem (mannelijk) en der (vrouwelijk)."
            }
        ]
    },

    # Toets 35 (H5)
    {
        "id": "ex-h3-duits-35",
        "hoofdstuk": 5,
        "hoofdstukTitel": "Zukunft & Berufe",
        "titel": "Toets 35 — H5 Beroepen, Sollicitatie & Opleidingen",
        "duurMin": 20,
        "vak": "Duits HAVO 3 — Hoofdstuk 5",
        "icoon": "💼",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Welk document stuur je mee bij een sollicitatie om je opleiding en werkervaring te tonen?",
                "opties": [
                    "der Lebenslauf",
                    "das Praktikum",
                    "die Auszeit",
                    "das Studium"
                ],
                "antwoord": 0,
                "uitleg": "'Der Lebenslauf' is het cv."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de afkorting 'das Abi' in het Duitse onderwijssysteem?",
                "opties": [
                    "de toelatingstest voor het mbo",
                    "het vwo-eindexamendiploma (Abitur)",
                    "het stagecontract bij een bedrijf",
                    "het getuigschrift van de basisschool"
                ],
                "antwoord": 1,
                "uitleg": "'Das Abi' is de afkorting voor het Abitur (vwo-eindexamen)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het als een student 'Jura studiert' aan de universiteit?",
                "opties": [
                    "Hij studeert archeologie",
                    "Hij studeert medicijnen",
                    "Hij studeert rechten",
                    "Hij volgt een koksopleiding"
                ],
                "antwoord": 2,
                "uitleg": "'Jura' is de rechtenstudie."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits werkwoord betekent 'solliciteren naar een baan'?",
                "opties": [
                    "sich beschäftigen mit",
                    "anfangen",
                    "faulenzen",
                    "sich bewerben um"
                ],
                "antwoord": 3,
                "uitleg": "'Sich bewerben um' betekent solliciteren naar."
            },
            {
                "type": "mc",
                "vraag": "Wat is in Duitsland een 'Fachhochschule'?",
                "opties": [
                    "een hogeschool voor hoger beroepsonderwijs (hbo)",
                    "een internaat voor topsporters",
                    "een lagere school voor beroepsoriëntatie",
                    "een muziekschool"
                ],
                "antwoord": 0,
                "uitleg": "'Die Fachhochschule' is de Duitse tegenhanger van het Nederlandse hbo."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitdrukking 'ein Zwischenjahr einlegen'?",
                "opties": [
                    "zakken voor het eindexamen",
                    "een tussenjaar nemen na het behalen van je diploma",
                    "meteen beginnen met een voltijdbaan",
                    "overstappen naar een andere schoolklas"
                ],
                "antwoord": 1,
                "uitleg": "'Ein Zwischenjahr einlegen' betekent een tussenjaar nemen."
            },
            {
                "type": "mc",
                "vraag": "Welk Duits woord betekent 'het bedrijf' of 'de onderneming'?",
                "opties": [
                    "die Auszeit",
                    "der Traum",
                    "das Unternehmen",
                    "das Praktikum"
                ],
                "antwoord": 2,
                "uitleg": "'Das Unternehmen' is de onderneming of het bedrijf."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het werkwoord 'sich anstrengen'?",
                "opties": [
                    "uitrusten na een drukke dag",
                    "solliciteren via het internet",
                    "zich zorgen maken over geld",
                    "zich flink inspannen om iets te bereiken"
                ],
                "antwoord": 3,
                "uitleg": "'Sich anstrengen' betekent hard werken of je ergens voor inspannen."
            },
            {
                "type": "mc",
                "vraag": "Welk beroep wordt aangeduid met 'der Krankenpfleger'?",
                "opties": [
                    "de verpleegkundige (mannelijk)",
                    "de fysiotherapeut",
                    "de dierenarts",
                    "de apotheker"
                ],
                "antwoord": 0,
                "uitleg": "'Der Krankenpfleger' is de mannelijke verpleegkundige."
            },
            {
                "type": "mc",
                "vraag": "Wat voor werkzaamheden verricht een 'Mediendesigner' hoofdzakelijk in een onderneming?",
                "opties": [
                    "het bereiden van maaltijden in de kantine",
                    "het ontwerpen van digitale media, websites en grafische uitingen",
                    "het verplegen van zieke werknemers",
                    "het besturen van vrachtwagens"
                ],
                "antwoord": 1,
                "uitleg": "Een 'Mediendesigner' ontwerpt grafische en digitale media, lay-outs en animaties."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent 'sich kümmern um Patienten'?",
                "opties": [
                    "patienten naar huis sturen",
                    "medicijnen verkopen aan patienten",
                    "zorgen voor en aandacht geven aan patiënten",
                    "patiënten administreren in het computersysteem"
                ],
                "antwoord": 2,
                "uitleg": "'Sich kümmern um' betekent zorgen voor."
            },
            {
                "type": "mc",
                "vraag": "Wat is 'die Oberstufe' op een Duits Gymnasium?",
                "opties": [
                    "de gymzaal op de bovenste verdieping",
                    "de eerste klas van de brugklas",
                    "de kantine voor docenten",
                    "de bovenbouw van de middelbare school"
                ],
                "antwoord": 3,
                "uitleg": "'Die Oberstufe' is de bovenbouw."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'das Praktikum' betekent een wetenschappelijk natuurkunde-experiment in een lab.",
                "antwoord": False,
                "uitleg": "Onwaar! In onderwijs- en beroepscontext betekent 'das Praktikum' een stage bij een bedrijf."
            },
            {
                "type": "waaronwaar",
                "vraag": "Met het 'Abitur' op zak mag je je direct inschrijven aan een Duitse universiteit.",
                "antwoord": True,
                "uitleg": "Waar! Het Abitur geeft algemene toegang tot het wetenschappelijk onderwijs."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het werkwoord 'faulenzen' betekent dat je overuren draait op je werkplek.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Faulenzen' betekent luieren of lekker nietsdoen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het woord 'die Tätigkeiten' verwijst naar de dagelijkse taken en werkzaamheden in een beroep.",
                "antwoord": True,
                "uitleg": "Waar! 'Die Tätigkeiten' zijn de taken of werkzaamheden."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'Ich mache im Sommer ein vierwöchiges (stage) bei BMW.' Vul het Duitse woord in.",
                "antwoord": "Praktikum|das Praktikum",
                "uitleg": "Een stage is in het Duits 'das Praktikum'."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste vaste voorzetselvorm in: 'Er bewirbt sich ____ (om/naar) einen Ausbildungsplatz.'",
                "antwoord": "um",
                "uitleg": "De vaste combinatie is 'sich bewerben um'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Welke twee studierichtingen worden in het Duits aangeduid met de termen 'Jura' en 'Medizin'?",
                "modelantwoord": "Dat zijn de studies rechten en geneeskunde.",
                "sleutelwoorden": [
                    "rechten/recht",
                    "geneeskunde/medicijnen"
                ],
                "minTreffers": 2,
                "uitleg": "Jura is rechten en Medizin is geneeskunde."
            },
            {
                "type": "open",
                "vraag": "Wat stuurt een sollicitant op naar een bedrijf als hij solliciteert naar een vacature?",
                "modelantwoord": "Een sollicitant stuurt een motivatiebrief en een cv oftewel Lebenslauf.",
                "sleutelwoorden": [
                    "Lebenslauf/cv",
                    "Bewerbung/brief"
                ],
                "minTreffers": 1,
                "uitleg": "Bij een sollicitatie stuur je een 'Bewerbung' met 'Lebenslauf' (cv)."
            }
        ]
    },

    # Toets 36 (H6)
    {
        "id": "ex-h3-duits-36",
        "hoofdstuk": 6,
        "hoofdstukTitel": "In Aktion & Hilfsbereitschaft",
        "titel": "Toets 36 — H6 Vaste Voorzetsels, Noodgevallen & Vrijwilligerswerk",
        "duurMin": 20,
        "vak": "Duits HAVO 3 — Hoofdstuk 6",
        "icoon": "🚑",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Welke naamval volgt ALTIJD na de voorzetsels: aus, bei, mit, nach, seit, von, zu?",
                "opties": [
                    "de 3e naamval (Dativ)",
                    "de 4e naamval (Akkusativ)",
                    "de 1e naamval (Nominativ)",
                    "de 2e naamval (Genitiv)"
                ],
                "antwoord": 0,
                "uitleg": "De voorzetsels aus, bei, mit, nach, seit, von, zu worden altijd gevolgd door de 3e naamval (Dativ)."
            },
            {
                "type": "mc",
                "vraag": "Welke naamval volgt ALTIJD na de voorzetsels: bis, durch, für, gegen, ohne, um?",
                "opties": [
                    "de 3e naamval (Dativ)",
                    "de 4e naamval (Akkusativ)",
                    "de 1e naamval (Nominativ)",
                    "de 2e naamval (Genitiv)"
                ],
                "antwoord": 1,
                "uitleg": "De voorzetsels bis, durch, für, gegen, ohne, um regeren altijd de 4e naamval (Akkusativ)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de term 'die ehrenamtliche Arbeit'?",
                "opties": [
                    "goed betaald leidinggevend werk",
                    "parttime werk in een supermarkt",
                    "vrijwilligerswerk zonder betaling voor een goed doel",
                    "stage lopen tijdens de studie"
                ],
                "antwoord": 2,
                "uitleg": "'Ehrenamtliche Arbeit' is vrijwilligerswerk."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het lidwoord na het Dativ-voorzetsel 'aus': 'Er kommt aus ____ (de) Haus.'",
                "opties": [
                    "das",
                    "den",
                    "des",
                    "dem"
                ],
                "antwoord": 3,
                "uitleg": "'Aus' vraagt de 3e naamval. Onzijdig 'das Haus' wordt 'dem Haus'."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste lidwoord na het Akkusativ-voorzetsel 'durch': 'Der Radfahrer fährt durch ____ (de) Tunnel.'",
                "opties": [
                    "den",
                    "dem",
                    "der",
                    "das"
                ],
                "antwoord": 0,
                "uitleg": "'Durch' vraagt de 4e naamval. Mannelijk 'der Tunnel' wordt 'den Tunnel'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent 'Anzeige erstatten' op het politiebureau?",
                "opties": [
                    "een paspoort verlengen",
                    "aangifte doen van een misdrijf of diefstal",
                    "een bekeuring contant betalen",
                    "een getuigenverklaring intrekken"
                ],
                "antwoord": 1,
                "uitleg": "'Anzeige erstatten' betekent aangifte doen bij de politie."
            },
            {
                "type": "mc",
                "vraag": "Welke organisatie zorgt in Duitsland voor de veiligheid en redding op en rond het water?",
                "opties": [
                    "die Feuerwehr",
                    "das THW",
                    "die DLRG",
                    "die Polizei"
                ],
                "antwoord": 2,
                "uitleg": "De DLRG (Deutsche Lebens-Rettungs-Gesellschaft) is de reddingsbrigade aan het water."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm na 'ohne': 'Wir können ohne ____ (onze) Lehrerin nicht losgehen.'",
                "opties": [
                    "unserer",
                    "unserem",
                    "unser",
                    "unsere"
                ],
                "antwoord": 3,
                "uitleg": "'Ohne' vraagt de 4e naamval. Vrouwelijk blijft in de 4e naamval 'unsere'."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste voorzetsel voor 'bij': 'Ich übernachte heute ____ (bij) meinem Freund.'",
                "opties": [
                    "bei",
                    "durch",
                    "für",
                    "gegen"
                ],
                "antwoord": 0,
                "uitleg": "'Bij' is in het Duits 'bei' (met de 3e naamval: meinem Freund)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Duitse woord 'der Diebstahl'?",
                "opties": [
                    "de verkeersovertreding",
                    "de diefstal",
                    "de ontruiming",
                    "het ongeluk"
                ],
                "antwoord": 1,
                "uitleg": "'Der Diebstahl' betekent de diefstal."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de waarschuwingskreet 'Vorsicht!'?",
                "opties": [
                    "Dankjewel!",
                    "Kom binnen!",
                    "Pas op! / Voorzichtig!",
                    "Alles veilig!"
                ],
                "antwoord": 2,
                "uitleg": "'Vorsicht!' betekent pas op of wees voorzichtig."
            },
            {
                "type": "mc",
                "vraag": "Wat is het Duitse woord voor de ambulance?",
                "opties": [
                    "der Unfallwagen",
                    "das Polizeiauto",
                    "das Feuerwehrboot",
                    "der Krankenwagen"
                ],
                "antwoord": 3,
                "uitleg": "'Der Krankenwagen' is de ziekenwagen / ambulance."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Na het Duitse voorzetsel 'für' moet het zinsdeel altijd in de 4e naamval (Akkusativ) staan.",
                "antwoord": True,
                "uitleg": "Waar! 'Für' is een vast voorzetsel met de 4e naamval (bijv. für meinen Vater)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het voorzetsel 'von' regeert altijd de 4e naamval.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Von' hoort bij het vaste Dativ-rijtje (3e naamval): von meinem Bruder."
            },
            {
                "type": "waaronwaar",
                "vraag": "De hulpdienst 'die Feuerwehr' blust branden en helpt bij technische noodgevallen.",
                "antwoord": True,
                "uitleg": "Waar! 'Die Feuerwehr' is de brandweer."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Duitse woord 'der Ausweis' betekent de portemonnee voor contant geld.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Der Ausweis' is het identiteitsbewijs. De portemonnee is 'das Portmonee'."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het juiste voorzetsel in dat 'naar' betekent (vast Dativ-voorzetsel): 'Wir gehen jetzt ____ (naar) der Schule.'",
                "antwoord": "zu",
                "uitleg": "'Zu' is het vaste Dativ-voorzetsel (zur Schule = zu der Schule)."
            },
            {
                "type": "invul",
                "vraag": "Vul het juiste voorzetsel in dat 'tegen' betekent (vast Akkusativ-voorzetsel): 'Das Auto prallte ____ (tegen) einen Baum.'",
                "antwoord": "gegen",
                "uitleg": "'Gegen' regeert altijd de 4e naamval (Akkusativ)."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem het vaste rijtje van zeven voorzetsels die altijd de 3e naamval (Dativ) krijgen.",
                "modelantwoord": "De zeven voorzetsels met de derde naamval zijn aus, bei, mit, nach, seit, von en zu.",
                "sleutelwoorden": [
                    "aus",
                    "bei",
                    "mit",
                    "nach",
                    "seit",
                    "von",
                    "zu"
                ],
                "minTreffers": 4,
                "uitleg": "De vaste Dativ-voorzetsels zijn: aus, bei, mit, nach, seit, von, zu."
            },
            {
                "type": "open",
                "vraag": "Noem het vaste rijtje van zes voorzetsels die altijd de 4e naamval (Akkusativ) krijgen.",
                "modelantwoord": "De zes voorzetsels met de vierde naamval zijn bis, durch, für, gegen, ohne en um.",
                "sleutelwoorden": [
                    "bis",
                    "durch",
                    "für",
                    "gegen",
                    "ohne",
                    "um"
                ],
                "minTreffers": 4,
                "uitleg": "De vaste Akkusativ-voorzetsels zijn: bis, durch, für, gegen, ohne, um."
            }
        ]
    }
]

def generate():
    for item in ONDERWERPEN:
        fname = f"h{item['hoofdstuk']}_4.js"
        fpath = os.path.join(DATA_DIR, fname)
        code = f"/* Onderwerp {item['paragraaf']} — {item['titel']}\n   Neue Kontakte 3 HAVO Hoofdstuk {item['hoofdstuk']} */\nDURU.register({json.dumps(item, indent=2, ensure_ascii=False)});\n"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Geschreven onderwerp: {fname}")

    for item in EXAMENS:
        idx = item['id'].replace("ex-h3-duits-", "")
        fname = f"examen_{idx}.js"
        fpath = os.path.join(DATA_DIR, fname)
        code = f"/* Proeftoets {item['id']} — {item['titel']}\n   Neue Kontakte 3 HAVO Hoofdstuk {item['hoofdstuk']} */\nDURU.registerExamen({json.dumps(item, indent=2, ensure_ascii=False)});\n"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Geschreven examen: {fname}")

if __name__ == "__main__":
    generate()
