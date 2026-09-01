#!/usr/bin/env python3
"""
Generate Frans Unité 2 Proeftoetsen (5 exams x 20 questions = 100 questions)
Grandes Lignes 3 HAVO - Unité 2: Du temps pour moi
"""
import os, json

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/frans/js/data"
os.makedirs(DATA_DIR, exist_ok=True)

def balance_mc(questions):
    mc_indices = [i for i, q in enumerate(questions) if q.get("type") == "mc"]
    target_pattern = [0, 1, 2, 3] * (len(mc_indices) // 4 + 2)
    for idx, q_idx in enumerate(mc_indices):
        q = questions[q_idx]
        current_ans_idx = q["antwoord"]
        correct_text = q["opties"][current_ans_idx]
        new_ans_idx = target_pattern[idx] % len(q["opties"])
        if new_ans_idx != current_ans_idx:
            opts = [opt for i, opt in enumerate(q["opties"]) if i != current_ans_idx]
            opts.insert(new_ans_idx, correct_text)
            q["opties"] = opts
            q["antwoord"] = new_ans_idx

def write_examen(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    content = f"""/* Proeftoets {data['titel']}
   Grandes Lignes 3 HAVO Unité {data['hoofdstuk']} */
DURU.registerExamen({json.dumps(data, indent=2, ensure_ascii=False)});
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [✓] Frans Examen saved: {filename}")

# EXAMEN 6: Vocabulaire U2 (Vrije tijd, Sport, Muziek & Hobby's)
ex6 = {
  "id": "ex-h3-frans-6",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Unité 2 — Du temps pour moi",
  "titel": "Toets 1 — Vocabulaire: Vrije tijd, Sport, Muziek & Hobby's",
  "vak": "Frans · HAVO 3 (U2)",
  "icoon": "🎸",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent de uitdrukking <b>'avoir du temps libre'</b>?", "opties": ["vrije tijd hebben", "te laat komen", "een klok kopen", "geen tijd meer hebben"], "antwoord": 0, "uitleg": "'Le temps libre' is vrije tijd."},
    {"type": "mc", "vraag": "Vertaal naar het Nederlands: <b>'faire de l'équitation'</b>:", "opties": ["paardrijden", "wielrennen", "zeilen", "schaatsen"], "antwoord": 0, "uitleg": "'L'équitation' betekent paardrijden."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'jouer de la guitare'</b> gitaar spelen.", "antwoord": True, "uitleg": "Waar. Bij muziekinstrumenten gebruik je 'jouer de' (jouer de la guitare, jouer du piano)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>wedstrijd / toernooi</i> naar het Frans: <i>Samedi, j'ai un ... de football.</i>", "antwoord": "match|tournoi", "uitleg": "'Un match' (of tournoi) is een wedstrijd."},
    {"type": "mc", "vraag": "Wat betekent <b>'s'entraîner'</b> voor een sporter?", "opties": ["trainen / oefenen", "de trein nemen", "een blessure oplopen", "stoppen met sport"], "antwoord": 0, "uitleg": "'S'entraîner' betekent trainen."},
    {"type": "waaronwaar", "vraag": "Bij balsporten gebruik je het werkwoord <b>'jouer à'</b> (bijv. <i>jouer au tennis</i>, <i>jouer au basket</i>).", "antwoord": True, "uitleg": "Waar. Balsporten = jouer à (au foot, au tennis); instrumenten = jouer de (du piano)."},
    {"type": "invul", "vraag": "Vul het ontbrekende woord in voor <i>tekenen / schilderen</i>: <i>Mon passe-temps préféré, c'est le ... .</i>", "antwoord": "dessin|dessiner|peinture", "uitleg": "'Le dessin' is tekenen."},
    {"type": "mc", "vraag": "Wat betekent de Franse uitdrukking <b>'faire la grasse matinée'</b>?", "opties": ["uitslapen (lekker lang in bed blijven liggen)", "vroeg opstaan om te gaan rennen", "ontbijten met veel vet", "een ochtendwandeling maken"], "antwoord": 0, "uitleg": "'Faire la grasse matinée' betekent heerlijk uitslapen."},
    {"type": "mc", "vraag": "Wat is <b>'une séance d'entraînement'</b>?", "opties": ["een trainingssessie / training", "een bioscoopvoorstelling", "een muziekconcert", "een schooltoets"], "antwoord": 0, "uitleg": "'Une séance d'entraînement' is een trainingssessie."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'les loisirs'</b> betekent 'huiswerkopdrachten'.", "antwoord": False, "uitleg": "Onwaar. 'Les loisirs' betekent vrijetijdsbesteding / hobby's."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (zwemmen): <i>En été, j'adore ... dans la mer.</i>", "antwoord": "nager|faire de la natation", "uitleg": "'Nager' betekent zwemmen."},
    {"type": "mc", "vraag": "Wat betekent <b>'écouter un morceau de musique'</b>?", "opties": ["een muzieknummer / muziekstuk luisteren", "een instrument repareren", "een liedje componeren", "naar de radio luisteren"], "antwoord": 0, "uitleg": "'Un morceau de musique' is een muziekstuk / track."},
    {"type": "open", "vraag": "Leg het verschil uit in Frans taalgebruik tussen <i>'jouer au football'</i> en <i>'faire du football'</i>.", "sleutelwoorden": ["sport/spel/jouer", "beoefenen/doen/faire"], "minTreffers": 1, "modelantwoord": "Beide betekenen voetballen, maar bij 'jouer à' ligt de nadruk op het spelen van de balsport, en bij 'faire de' op sportbeoefening in het algemeen.", "uitleg": "'Jouer au foot' en 'faire du foot' zijn beide correct in het Frans."},
    {"type": "mc", "vraag": "Wat betekent <b>'faire de l'escalade'</b>?", "opties": ["rotsklimmen / muurklimmen", "langlaufen", "wandelen in het park", "parachutespringen"], "antwoord": 0, "uitleg": "'L'escalade' betekent klimmen / bergbeklimmen."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'sortir avec des copains'</b> betekent 'uitgaan / afspreken met vrienden'.", "antwoord": True, "uitleg": "Waar. 'Sortir' betekent uitgaan / naar buiten gaan."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>vereniging / sportclub</i>: <i>Je suis membre d'un ... de tennis.</i>", "antwoord": "club", "uitleg": "'Un club de tennis' is een tennisclub."},
    {"type": "mc", "vraag": "Wat is <b>'un terrain de sport'</b>?", "opties": ["een sportveld", "een gymzaal", "een kleedkamer", "een tribune"], "antwoord": 0, "uitleg": "'Un terrain' is een sportveld of terrein."},
    {"type": "waaronwaar", "vraag": "Het Franse werkwoord <b>'gagner'</b> betekent 'verliezen'.", "antwoord": False, "uitleg": "Onwaar. 'Gagner' betekent winnen (of verdienen). Verliezen is 'perdre'."},
    {"type": "invul", "vraag": "Vertaal het werkwoord <i>zingen</i> naar het Frans: <i>Elle adore ... dans une chorale.</i>", "antwoord": "chanter", "uitleg": "'Chanter' betekent zingen."},
    {"type": "mc", "vraag": "Wat betekent <b>'un passe-temps'</b>?", "opties": ["een tijdverdrijf / hobby", "een ov-chipkaart", "een kalender", "een wekker"], "antwoord": 0, "uitleg": "'Un passe-temps' is een tijdverdrijf / hobby."}
  ]
}

# EXAMEN 7: Grammaire U2 (Futur Composé: aller + infinitif & werkwoorden faire, aller, prendre)
ex7 = {
  "id": "ex-h3-frans-7",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Unité 2 — Du temps pour moi",
  "titel": "Toets 2 — Grammaire: Futur Composé (aller + inf) & Werkwoorden (faire, aller, prendre)",
  "vak": "Frans · HAVO 3 (U2)",
  "icoon": "⏱️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vorm je de <b>futur composé</b> (de nabije toekomst) in het Frans?", "opties": ["vervoeging van aller + hele werkwoord (infinitif)", "vervoeging van avoir + voltooid deelwoord", "vervoeging van être + hele werkwoord", "stam + uitgangen -ai, -as, -a"], "antwoord": 0, "uitleg": "Futur composé = vorm van aller in de tegenwoordige tijd + infinitif (bijv. je vais faire)."},
    {"type": "mc", "vraag": "Vervoeg <b>'aller'</b> bij <i>ils/elles</i>:", "opties": ["vont", "allons", "allez", "vas"], "antwoord": 0, "uitleg": "De vervoeging van aller is: je vais, tu vas, il va, nous allons, vous allez, ils vont."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Nous allons regarder un film'</i> staat in de passé composé (verleden tijd).", "antwoord": False, "uitleg": "Onwaar. 'Allons regarder' is de futur composé (wij gaan een film kijken)."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>faire</b>: <i>Qu'est-ce que vous ... ce week-end ?</i>", "antwoord": "faites", "uitleg": "Vous faites (onregelmatig!)."},
    {"type": "mc", "vraag": "Wat is de juiste vorm van <b>faire</b> bij <i>ils</i>?", "opties": ["font", "faisons", "faisez", "fait"], "antwoord": 0, "uitleg": "Ils/elles font (let op: niet 'faisez' maar 'vous faites' en 'ils font')."},
    {"type": "waaronwaar", "vraag": "De vervoeging van <b>prendre</b> bij <i>je</i> en <i>tu</i> is <b>je prends</b> en <b>tu prends</b>.", "antwoord": True, "uitleg": "Waar. Je prends, tu prends, il prend, nous prenons, vous prenez, ils prennent."},
    {"type": "invul", "vraag": "Maak de futur composé (ik ga spelen): <i>Je ... jouer au tennis demain.</i>", "antwoord": "vais", "uitleg": "Je vais jouer (aller + infinitif)."},
    {"type": "mc", "vraag": "Welk lidwoord hoort bij <b>faire</b> voor een vrouwelijk woord (zoals <i>natation</i>)?", "opties": ["de la", "du", "de l'", "des"], "antwoord": 0, "uitleg": "Faire + de la natation (vrouwelijk enkelvoud)."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Il fait ... vélo et il joue ... piano.</i>", "opties": ["du / du", "au / du", "de la / au", "du / au"], "antwoord": 0, "uitleg": "Faire du vélo (mannelijk) en jouer du piano (instrument = jouer de)."},
    {"type": "waaronwaar", "vraag": "De ontkenning in de futur composé komt rond het hulpwerkwoord <i>aller</i> (bijv. <i>Je ne vais pas dormir</i>).", "antwoord": True, "uitleg": "Waar. 'Ne' staat voor 'vais' en 'pas' direct erna: ne vais pas dormir."},
    {"type": "invul", "vraag": "Vul de juiste vorm van <b>prendre</b> in: <i>Nous ... le bus pour aller au club de sport.</i>", "antwoord": "prenons", "uitleg": "Nous prenons."},
    {"type": "mc", "vraag": "Welke vorm van <b>aller</b> hoort bij <i>tu</i>?", "opties": ["vas", "vais", "va", "allez"], "antwoord": 0, "uitleg": "Tu vas (jij gaat)."},
    {"type": "open", "vraag": "Vertaal de volgende zin naar correct Frans in de futur composé: <i>'Morgen gaan wij trainen in het park.'</i>", "sleutelwoorden": ["demain/nous allons/on va", "entraîner/sentrainer/faire/sport"], "minTreffers": 1, "modelantwoord": "Demain, nous allons nous entraîner dans le parc. (of: Demain, on va s'entraîner dans le parc.)", "uitleg": "Futur composé: nous allons + s'entraîner / aller s'entraîner."},
    {"type": "mc", "vraag": "Kies de juiste vorm van <b>faire</b>: <i>Tu ... (doen) du judo le mercredi après-midi.</i>", "opties": ["fais", "fait", "faisons", "font"], "antwoord": 0, "uitleg": "Tu fais (met -s)."},
    {"type": "waaronwaar", "vraag": "Bij <b>ils/elles prennent</b> schrijf je de 'n' dubbel.", "antwoord": True, "uitleg": "Waar. Ils prennent / elles prennent heeft een dubbele n en stomme -ent."},
    {"type": "invul", "vraag": "Vul aan met het juiste lidwoord: <i>Mon frère fait ... escalade.</i>", "antwoord": "de l'|de l", "uitleg": "'Escalade' begint met een klinker, dus 'de l''. De + l' = de l'."},
    {"type": "mc", "vraag": "Hoe zeg je: <i>'Zij gaan hun vrienden ontmoeten'</i> in de futur composé?", "opties": ["Ils vont rencontrer leurs amis.", "Ils vont rencontrons leurs amis.", "Ils ont rencontré leurs amis.", "Ils vont rencontre leurs amis."], "antwoord": 0, "uitleg": "Aller (vont) + hele werkwoord (rencontrer)."},
    {"type": "waaronwaar", "vraag": "De vorm van <b>faire</b> bij <i>il/elle</i> is <b>il fait</b> (met een -t).", "antwoord": True, "uitleg": "Waar. Je fais, tu fais, il/elle fait."},
    {"type": "invul", "vraag": "Vul de futur composé in voor <i>nous (partir)</i>: <i>Ce soir, nous ... partir à 20h.</i>", "antwoord": "allons", "uitleg": "Nous allons partir."},
    {"type": "mc", "vraag": "Wat betekent de zin: <i>'Qu'est-ce que tu vas faire plus tard ?'</i>", "opties": ["Wat ga je later doen?", "Wat heb je gisteren gedaan?", "Waar ben je nu aan het werk?", "Hoe laat kom je thuis?"], "antwoord": 0, "uitleg": "'Vas faire' = ga je doen; 'plus tard' = later."}
  ]
}

# EXAMEN 8: Stones & Communication U2 (Afspreken, plannen maken & voorstellen)
ex8 = {
  "id": "ex-h3-frans-8",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Unité 2 — Du temps pour moi",
  "titel": "Toets 3 — Communication: Afspreken, Voorstellen doen & Tijdstippen",
  "vak": "Frans · HAVO 3 (U2)",
  "icoon": "🗓️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe stel je spontaan voor: <i>'Zullen we naar de bioscoop gaan?'</i>", "opties": ["On va au cinéma ?", "Pourquoi tu vas au cinéma ?", "Le cinéma est fermé ?", "Combien coûte le cinéma ?"], "antwoord": 0, "uitleg": "'On va au cinéma ?' of 'Si on allait au cinéma ?' is een natuurlijk Frans voorstel."},
    {"type": "mc", "vraag": "Hoe reageer je enthousiast op een voorstel van een vriend?", "opties": ["Bonne idée ! / Avec plaisir !", "Non, c'est nul.", "Je n'ai pas envie.", "Je dois faire le ménage."], "antwoord": 0, "uitleg": "'Bonne idée !' (Goed idee!) of 'Avec plaisir !' (Graag!)."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'Ça te dit de...'</b> betekent 'Heb je zin om... / Lijkt het je leuk om...'.", "antwoord": True, "uitleg": "Waar. 'Ça te dit de jouer aux jeux vidéo ?' = Heb je zin om te gamen?"},
    {"type": "invul", "vraag": "Vertaal de dag <i>woensdag</i> naar het Frans: <i>Je n'ai pas école le ... après-midi.</i>", "antwoord": "mercredi", "uitleg": "Mercredi = woensdag."},
    {"type": "mc", "vraag": "Hoe zeg je beleefd dat je helaas niet kunt afspreken?", "opties": ["Désolé(e), je ne peux pas, je suis occupé(e).", "Dégage, je ne veux pas te voir.", "Tu es trop ennuyeux.", "Je déteste tout le monde."], "antwoord": 0, "uitleg": "'Désolé, je ne peux pas' is de standaard beleefde afwijzing."},
    {"type": "waaronwaar", "vraag": "De vraag <i>'À quelle heure on se retrouve ?'</i> vraagt waar het feest plaatsvindt.", "antwoord": False, "uitleg": "Onwaar. Het vraagt hoe laat we elkaar ontmoeten."},
    {"type": "invul", "vraag": "Vul aan om te vragen <i>'Waar spreken we af?'</i>: <i>... on se donne rendez-vous ?</i>", "antwoord": "Où|Ou", "uitleg": "'Où' betekent waar."},
    {"type": "mc", "vraag": "Hoe vraag je: <i>'Wat doe je dit weekend?'</i>", "opties": ["Qu'est-ce que tu fais ce week-end ?", "Pourquoi tu pars ce week-end ?", "Où étais-tu le week-end dernier ?", "Quand commence le week-end ?"], "antwoord": 0, "uitleg": "'Qu'est-ce que tu fais ce week-end ?' vraagt naar de weekendplannen."},
    {"type": "mc", "vraag": "Wat betekent het antwoord: <b>'Ça me convient parfaitement !'</b>?", "opties": ["Dat komt mij perfect uit!", "Dat vind ik heel vervelend.", "Ik weet het nog niet zeker.", "Ik heb geen tijd."], "antwoord": 0, "uitleg": "'Ça me convient' betekent dat het goed/passend uitkomt."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'samedi prochain'</b> afgelopen zaterdag.", "antwoord": False, "uitleg": "Onwaar. 'Prochain' betekent volgend/aanstaand. Afgelopen zaterdag is 'samedi dernier'."},
    {"type": "invul", "vraag": "Vertaal de dag <i>zaterdag</i> naar het Frans: <i>On se voit ... ?</i>", "antwoord": "samedi", "uitleg": "Samedi = zaterdag."},
    {"type": "mc", "vraag": "Hoe vraag je hoe laat het is?", "opties": ["Quelle heure est-il ?", "Combien d'heures tu as ?", "Quel jour sommes-nous ?", "Quelle est la date ?"], "antwoord": 0, "uitleg": "'Quelle heure est-il ?' of 'Il est quelle heure ?'."},
    {"type": "open", "vraag": "Schrijf een kort Frans berichtje waarin je een vriend uitnodigt om zaterdag om 14:00 uur te gaan voetballen in het park.", "sleutelwoorden": ["samedi/14h/quatorze", "football/foot/parc/jouer/on va"], "minTreffers": 1, "modelantwoord": "Salut ! Ça te dit de jouer au foot samedi à 14h dans le parc ?", "uitleg": "Gebruik 'Ça te dit de...' of 'On va jouer au foot samedi à 14h...'."},
    {"type": "mc", "vraag": "Wat betekent: <b>'Je n'ai pas envie de sortir ce soir'</b>?", "opties": ["Ik heb geen zin om vanavond uit te gaan", "Ik mag niet uitgaan van mijn ouders", "Ik heb geen geld om uit te gaan", "Mijn vrienden zijn al vertrokken"], "antwoord": 0, "uitleg": "'Avoir envie de' = zin hebben in; 'ne pas avoir envie' = geen zin hebben."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'À tout à l'heure'</b> betekent dat je elkaar over enkele uren / straks weer ziet.", "antwoord": True, "uitleg": "Waar. 'À tout à l'heure' = tot straks / tot zo."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>afspraak</i>: <i>J'ai un ... chez le dentiste à 16h.</i>", "antwoord": "rendez-vous|rendez vous", "uitleg": "'Un rendez-vous' is een afspraak."},
    {"type": "mc", "vraag": "Hoe zeg je: <i>'Het is kwart over drie'</i> in het Frans?", "opties": ["Il est trois heures et quart.", "Il est trois heures moins le quart.", "Il est trois heures et demie.", "Il est quatre heures."], "antwoord": 0, "uitleg": "'Et quart' = kwart over."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Il est six heures et demie'</i> betekent dat het half zeven is (6:30 uur).", "antwoord": True, "uitleg": "Waar. In het Frans zeg je 'zes uur en een half' voor half zeven."},
    {"type": "invul", "vraag": "Vul aan voor <i>kwart voor</i>: <i>Il est cinq heures ... le quart.</i>", "antwoord": "moins", "uitleg": "'Moins le quart' betekent kwart voor."},
    {"type": "mc", "vraag": "Wat betekent <b>'On remet ça à plus tard'</b>?", "opties": ["We stellen het uit naar later", "We beginnen direct opnieuw", "We annuleren alles voor altijd", "We nodigen meer mensen uit"], "antwoord": 0, "uitleg": "'Remettre à plus tard' betekent uitstellen naar een later tijdstip."}
  ]
}

# EXAMEN 9: Leesvaardigheid U2 (Vrijetijdsgidsen, Sportclubs & Activiteiten)
ex9 = {
  "id": "ex-h3-frans-9",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Unité 2 — Du temps pour moi",
  "titel": "Toets 4 — Leesvaardigheid: Vrijetijdsgidsen, Sportclubs & Activiteiten",
  "vak": "Frans · HAVO 3 (U2)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Lees de poster: <i>'Club de Musique Jeunes : cours de guitare et batterie tous les mercredis de 14h à 17h. Inscription gratuite pour les moins de 16 ans.'</i><br>Voor wie is de inschrijving gratis?", "opties": ["Voor jongeren onder de 16 jaar", "Voor alle volwassenen", "Alleen voor docenten", "Voor niemand"], "antwoord": 0, "uitleg": "'Inscription gratuite pour les moins de 16 ans' = gratis voor onder de 16."},
    {"type": "mc", "vraag": "Lees het bericht: <i>'En raison du mauvais temps, le tournoi d'athlétisme est reporté à dimanche prochain.'</i><br>Waarom is het toernooi verplaatst?", "opties": ["Vanwege het slechte weer", "Omdat er te weinig deelnemers waren", "Omdat de trainer ziek is", "Wegens een feestdag"], "antwoord": 0, "uitleg": "'En raison du mauvais temps' = wegens het slechte weer; 'reporté' = uitgesteld."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Le centre sportif est ouvert tous les jours sauf le lundi'</i> is het sportcentrum op maandag gesloten.", "antwoord": True, "uitleg": "Waar. 'Sauf le lundi' betekent 'behalve op maandag'."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'sauf'</b> in een openingstijdenoverzicht?", "antwoord": "behalve|uitgezonderd", "uitleg": "'Sauf' betekent behalve of uitgezonderd."},
    {"type": "mc", "vraag": "Lees het interview: <i>'Je m'entraîne trois fois par semaine pour préparer le championnat régional de natation.'</i><br>Hoe vaak per week traint deze zwemmer?", "opties": ["Drie keer per week", "Elke dag", "Eén keer per maand", "Alleen in het weekend"], "antwoord": 0, "uitleg": "'Trois fois par semaine' = drie keer per week."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'le championnat'</b> betekent het kampioenschap.", "antwoord": True, "uitleg": "Waar. 'Le championnat' is het kampioenschap / de competitie."},
    {"type": "invul", "vraag": "Lees: <i>'Tarif réduit : 5 euros pour les étudiants.'</i><br>Wat is de gereduceerde prijs voor studenten in euro's?", "antwoord": "5|5 euro|5 euros|vijf", "uitleg": "5 euros."},
    {"type": "mc", "vraag": "Wat is het doel van de advertentie: <i>'Venez découvrir nos cours de danse hip-hop ! Premier cours d'essai offert sans engagement.'</i>?", "opties": ["Mensen uitnodigen voor een gratis proefles hiphopdans", "Professionele dansschoenen verkopen", "Een dansvoorstelling in het theater aankondigen", "Vrijwilligers werven voor de garderobe"], "antwoord": 0, "uitleg": "'Cours d'essai offert' = gratis proefles aangeboden."},
    {"type": "mc", "vraag": "Wat betekent het signaalwoord <b>'pendant'</b>?", "opties": ["tijdens / gedurende", "na afloop van", "voorafgaand aan", "ondanks"], "antwoord": 0, "uitleg": "'Pendant' betekent tijdens of gedurende (bijv. pendant les vacances)."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Les inscriptions débutent le 1er septembre'</i> betekent dat de inschrijvingen sluiten op 1 september.", "antwoord": False, "uitleg": "Onwaar. 'Débutent' komt van débuter (beginnen / van start gaan)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'week-end'</i> of <i>'zaterdag en zondag'</i> naar het Frans in één woord: <i>Passe un bon ... !</i>", "antwoord": "week-end|weekend", "uitleg": "Un bon week-end."},
    {"type": "mc", "vraag": "Lees de sms: <i>'Je suis en retard de 10 minutes, attendez-moi devant la piscine !'</i><br>Hoeveel minuten vertraging heeft de afzender?", "opties": ["10 minuten", "30 minuten", "1 uur", "Geen enkele minuut"], "antwoord": 0, "uitleg": "'En retard de 10 minutes' = 10 minuten te laat."},
    {"type": "open", "vraag": "Lees: <i>'Pour participer à la randonnée en montagne, il est obligatoire d'avoir de bonnes chaussures de marche et une gourde d'eau.'</i><br>Welke twee dingen zijn verplicht mee te nemen?", "sleutelwoorden": ["goede wandelschoenen/schoenen/chaussures", "fles water/waterfles/water/bidon/gourde"], "minTreffers": 2, "modelantwoord": "Goede wandelschoenen en een veldfles / waterfles met water.", "uitleg": "Verplicht zijn: 'bonnes chaussures de marche' en 'une gourde d'eau'."},
    {"type": "mc", "vraag": "Wat betekent de term <b>'sans engagement'</b> in een abonnement?", "opties": ["vrijblijvend / zonder contractuele verplichting", "alleen voor professionele sporters", "met een boete bij opzegging", "uitsluitend contant betalen"], "antwoord": 0, "uitleg": "'Sans engagement' = vrijblijvend / zonder vast contract."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'annulé'</b> op een mededelingenbord betekent dat het evenement afgelast / geannuleerd is.", "antwoord": True, "uitleg": "Waar. 'Annulé' betekent afgelast."},
    {"type": "invul", "vraag": "Wat betekent <b>'chaque semaine'</b> in het Nederlands?", "antwoord": "elke week|iedere week", "uitleg": "'Chaque semaine' betekent elke / iedere week."},
    {"type": "mc", "vraag": "Lees de aankondiging: <i>'Fête de la musique le 21 juin : des concerts gratuits dans toute la ville de 18h à minuit !'</i><br>Wat is er bijzonder aan de concerten tijdens het Franse Fête de la musique?", "opties": ["Ze zijn gratis en vinden plaats in de hele stad", "Ze zijn alleen toegankelijk met een duur VIP-ticket", "Ze worden uitsluitend binnen in kerken gehouden", "Ze duren maar 10 minuten per artiest"], "antwoord": 0, "uitleg": "Het bekende Franse Fête de la musique biedt overal gratis openluchtconcerten."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'minuit'</b> betekent 'het middaguur (12:00 uur overdag)'.", "antwoord": False, "uitleg": "Onwaar. 'Minuit' is middernacht (00:00 uur). Het middaguur is 'midi'."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'middag (12:00 uur)'</i> naar het Frans: <i>On mange à ... .</i>", "antwoord": "midi", "uitleg": "'Midi' is 12 uur 's middags."},
    {"type": "mc", "vraag": "Wat betekent <b>'du lundi au vendredi'</b>?", "opties": ["van maandag tot en met vrijdag", "alleen op maandag en vrijdag", "in het weekend", "de hele maandag"], "antwoord": 0, "uitleg": "'Du...au...' betekent 'van...tot (en met)'."}
  ]
}

# EXAMEN 10: Eindtoets Unité 2 (Mix & Examentraining)
ex10 = {
  "id": "ex-h3-frans-10",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Unité 2 — Du temps pour moi",
  "titel": "Toets 5 — Unité 2 Eindtoets (Mix & Examentraining)",
  "vak": "Frans · HAVO 3 (U2)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'faire la grasse matinée'</b>?", "opties": ["heerlijk uitslapen", "vroeg ontbijten", "intensief fitnessen", "studeren voor een toets"], "antwoord": 0, "uitleg": "Uitslapen in het weekend."},
    {"type": "mc", "vraag": "Kies de juiste vorm van de futur composé: <i>Demain, nous ... (faire) une randonnée.</i>", "opties": ["allons faire", "allons faisons", "vont faire", "avons fait"], "antwoord": 0, "uitleg": "Nous allons + hele werkwoord (faire)."},
    {"type": "waaronwaar", "vraag": "Bij het bespelen van een muziekinstrument gebruik je in het Frans <b>jouer de</b> (bijv. <i>jouer du piano</i>).", "antwoord": True, "uitleg": "Waar. Instrument = jouer de; sport = jouer à."},
    {"type": "invul", "vraag": "Vervoeg <b>faire</b> bij <i>vous</i>: <i>Qu'est-ce que vous ... ce soir ?</i>", "antwoord": "faites", "uitleg": "Vous faites."},
    {"type": "mc", "vraag": "Welk lidwoord hoort in: <i>Lucas fait ... équitation le samedi.</i>?", "opties": ["de l'", "du", "de la", "des"], "antwoord": 0, "uitleg": "Équitation begint met een klinker, dus 'de l''."},
    {"type": "waaronwaar", "vraag": "De vorm van <b>aller</b> bij <i>ils</i> is <i>'ils vont'</i>.", "antwoord": True, "uitleg": "Waar (je vais, tu vas, il va, nous allons, vous allez, ils vont)."},
    {"type": "invul", "vraag": "Vervoeg <b>prendre</b> bij <i>ils</i>: <i>Ils ... le train pour aller à Lyon.</i>", "antwoord": "prennent", "uitleg": "Ils prennent (dubbele n)."},
    {"type": "mc", "vraag": "Hoe stel je voor om af te spreken?", "opties": ["Ça te dit d'aller en ville ?", "Pourquoi tu habites en ville ?", "La ville est trop grande.", "Je déteste la ville."], "antwoord": 0, "uitleg": "'Ça te dit de...' is de ideale formule voor een voorstel."},
    {"type": "mc", "vraag": "Wat betekent <b>'Il est quatre heures et quart'</b>?", "opties": ["Het is kwart over vier (16:15)", "Het is kwart voor vier (15:45)", "Het is half vijf (16:30)", "Het is vier uur stipt"], "antwoord": 0, "uitleg": "'Et quart' = kwart over."},
    {"type": "waaronwaar", "vraag": "De ontkenning van <i>'Je vais sortir'</i> is <i>'Je ne sortirai pas'</i> in de futur composé.", "antwoord": False, "uitleg": "Onwaar. In de futur composé staat de ontkenning rond aller: 'Je ne vais pas sortir'."},
    {"type": "invul", "vraag": "Vul het vraagwoord in (Hoe laat): <i>... heure commence le film ?</i>", "antwoord": "À quelle|A quelle|Quelle", "uitleg": "À quelle heure = hoe laat."},
    {"type": "mc", "vraag": "Wat betekent <b>'s'entraîner'</b>?", "opties": ["trainen / oefenen", "de trein missen", "een kaartje kopen", "rusten op de bank"], "antwoord": 0, "uitleg": "S'entraîner = sporten/trainen."},
    {"type": "open", "vraag": "Leg uit waarom de constructie <i>'Je vais jouer'</i> de futur composé wordt genoemd en wat het uitdrukt.", "sleutelwoorden": ["aller/infinitif/hele werkwoord", "toekomst/nabije toekomst/plannen/gaan doen"], "minTreffers": 1, "modelantwoord": "Het bestaat uit de tegenwoordige tijd van aller + infinitif en drukt een gebeurtenis uit die in de nabije toekomst gaat plaatsvinden.", "uitleg": "Futur composé = aller + infinitief, geeft toekomstige handelingen weer."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Tu ... (aller) jouer au foot et après tu ... (prendre) une douche.</i>", "opties": ["vas / prends", "vais / prend", "va / prenez", "vont / prennent"], "antwoord": 0, "uitleg": "Tu vas + tu prends."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'sauf'</b> betekent 'altijd'.", "antwoord": False, "uitleg": "Onwaar. 'Sauf' betekent 'behalve / uitgezonderd'."},
    {"type": "invul", "vraag": "Vertaal de dag <i>zondag</i> naar het Frans: <i>Le ... , je me repose à la maison.</i>", "antwoord": "dimanche", "uitleg": "Dimanche = zondag."},
    {"type": "mc", "vraag": "Wat betekent <b>'un passe-temps'</b>?", "opties": ["een hobby / vrijetijdsbesteding", "een horloge", "een paspoort", "een bioscoopbon"], "antwoord": 0, "uitleg": "'Un passe-temps' is een hobby."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'Avec plaisir !'</b> betekent 'Graag! / Met plezier!'.", "antwoord": True, "uitleg": "Waar. Dit is een positieve reactie op een uitnodiging."},
    {"type": "invul", "vraag": "Vul aan voor <i>half</i>: <i>Il est dix heures et ... . (10:30 uur)</i>", "antwoord": "demie|demi", "uitleg": "'Et demie' = en een half (half elf)."},
    {"type": "mc", "vraag": "Vervoeg <b>faire</b> voor <i>ils/elles</i>:", "opties": ["font", "faisent", "faisez", "faisons"], "antwoord": 0, "uitleg": "Ils/elles font."}
  ]
}

write_examen("examen_6.js", ex6)
write_examen("examen_7.js", ex7)
write_examen("examen_8.js", ex8)
write_examen("examen_9.js", ex9)
write_examen("examen_10.js", ex10)
print("Frans Unité 2 exams (6 to 10) generated successfully!")
