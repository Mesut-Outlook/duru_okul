#!/usr/bin/env python3
"""
Generate Frans Unité 8 Proeftoetsen (5 exams x 20 questions = 100 questions)
Grandes Lignes 3 HAVO - Unité 8: Le pont (Passé Composé met Être, Cito & Eindbalans)
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

# EXAMEN 36: Vocabulaire U8 (Eindbalans HAVO 3, Toekomst, Beroepen & School)
ex36 = {
  "id": "ex-h3-frans-36",
  "hoofdstuk": 8,
  "hoofdstukTitel": "Unité 8 — Le pont",
  "titel": "Toets 1 — Vocabulaire: School, Beroepen, Toekomst & Eindbalans",
  "vak": "Frans · HAVO 3 (U8)",
  "icoon": "🎓",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'l'avenir'</b> in het Frans?", "opties": ["de toekomst", "het verleden", "het heden", "het rapport"], "antwoord": 0, "uitleg": "'L'avenir' betekent de toekomst."},
    {"type": "mc", "vraag": "Vertaal naar het Nederlands: <b>'réussir ses examens'</b>:", "opties": ["slagen voor je examens", "zakken voor je examens", "een toets vergeten", "spieken bij een toets"], "antwoord": 0, "uitleg": "'Réussir' betekent slagen / succesvol afronden (zakken = échouer / rater)."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le baccalauréat'</b> (of 'le bac') is het Franse eindexamendiploma van de middelbare school.", "antwoord": True, "uitleg": "Waar. 'Le bac' is het bekende eindexamen in Frankrijk."},
    {"type": "invul", "vraag": "Vertaal het woord <i>beroep / vak</i> naar het Frans: <i>Quel ... veux-tu faire plus tard ?</i>", "antwoord": "métier|metier|profession", "uitleg": "'Un métier' (of une profession) = een beroep."},
    {"type": "mc", "vraag": "Wat is <b>'le collège'</b> en <b>'le lycée'</b> in het Franse schoolsysteem?", "opties": ["Collège is onderbouw (11-15 jaar) en lycée is bovenbouw (15-18 jaar)", "Collège is universiteit en lycée is basisschool", "Het zijn twee verschillende privéscholen", "Collège is alleen voor sportopleidingen"], "antwoord": 0, "uitleg": "In Frankrijk: école primaire -> collège -> lycée -> université."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'échouer à un test'</b> een hoog cijfer halen.", "antwoord": False, "uitleg": "Onwaar. 'Échouer' betekent zakken / niet slagen."},
    {"type": "invul", "vraag": "Vertaal het woord <i>leraar / lerares</i> naar het Frans: <i>Notre ... de français est très sympa.</i>", "antwoord": "professeur|prof|enseignant|professeure", "uitleg": "'Le professeur' (of le prof) is de leraar."},
    {"type": "mc", "vraag": "Wat betekent <b>'faire des études supérieures'</b>?", "opties": ["hoger onderwijs / studeren aan hbo of universiteit", "naar de basisschool gaan", "een tussenjaar nemen om te reizen", "direct fulltime gaan werken"], "antwoord": 0, "uitleg": "'Études supérieures' = hoger onderwijs / vervolgstudie."},
    {"type": "mc", "vraag": "Wat is <b>'un stage'</b>?", "opties": ["een stage / werkervaringsperiode", "een schoolgebouw", "een diploma-uitreiking", "een studielening"], "antwoord": 0, "uitleg": "'Un stage' is een stage."},
    {"type": "waaronwaar", "vraag": "Het Franse cijfersysteem op school loopt van <b>0 tot 20</b> (waarbij 10/20 de voldoende-grens is).", "antwoord": True, "uitleg": "Waar. In Frankrijk beoordeelt men op een schaal van 20 (10 = la moyenne / voldoende)."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (voldoende / gemiddelde): <i>J'ai obtenu la ... en maths (12/20).</i>", "antwoord": "moyenne", "uitleg": "'La moyenne' is het gemiddelde / de voldoende (10/20 of hoger)."},
    {"type": "mc", "vraag": "Wat betekent <b>'un emploi du temps'</b>?", "opties": ["een lesrooster / weekschema", "een klok", "een schoolagenda", "een vakantiekalender"], "antwoord": 0, "uitleg": "'L'emploi du temps' is het lesrooster."},
    {"type": "open", "vraag": "Leg uit hoe de cijferbeoordeling op Franse scholen werkt (maximumscore en voldoende-grens).", "sleutelwoorden": ["20/twintig/schaal van 20", "10/tien/voldoende/moyenne"], "minTreffers": 2, "modelantwoord": "Franse scholen beoordelen op een schaal van 0 tot 20. Een score van 10/20 (la moyenne) geldt als de minimale voldoende.", "uitleg": "Cijfers lopen van 0 tot 20, waarbij 10/20 de voldoende is."},
    {"type": "mc", "vraag": "Wat is <b>'la récréation'</b> (of 'la récré')?", "opties": ["de schoolpauze / het speelkwartier", "de gymnastiekles", "het nablijven na schooltijd", "het examenlokaal"], "antwoord": 0, "uitleg": "'La récré' (récréation) is de pauze op het schoolplein."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'avoir de bonnes notes'</b> betekent goede cijfers halen op school.", "antwoord": True, "uitleg": "Waar. 'Une note' is een schoolcijfer."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (huiswerk): <i>Je dois faire mes ... pour demain.</i>", "antwoord": "devoirs", "uitleg": "'Les devoirs' is het huiswerk."},
    {"type": "mc", "vraag": "Wat betekent <b>'un médecin'</b> en <b>'un infirmier / une infirmière'</b>?", "opties": ["een arts / dokter en een verpleegkundige", "een leraar en een directeur", "een advocaat en een rechter", "een piloot en een stewardess"], "antwoord": 0, "uitleg": "Médecin = dokter, infirmier/infirmière = verpleegkundige."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'l'avocat'</b> betekent zowel een advocaat (beroep) als een avocado (vrucht).", "antwoord": True, "uitleg": "Waar. 'Un avocat' kan een advocaat of een avocado betekenen."},
    {"type": "invul", "vraag": "Vertaal het woord <i>kennis / weten</i>: <i>Les ... sont la clé du succès.</i>", "antwoord": "connaissances|savoirs", "uitleg": "'Les connaissances' = kennis."},
    {"type": "mc", "vraag": "Wat betekent de feestelijke uitroep <b>'Félicitations pour ton diplôme !'</b>?", "opties": ["Gefeliciteerd met je diploma!", "Succes met je herkansing!", "Waarom ben je gezakt?", "Kom morgen naar school."], "antwoord": 0, "uitleg": "'Félicitations !' = Van harte gefeliciteerd!"}
  ]
}

# EXAMEN 37: Grammaire U8 (Passé Composé met ÊTRE: bewegingswerkwoorden & accord)
ex37 = {
  "id": "ex-h3-frans-37",
  "hoofdstuk": 8,
  "hoofdstukTitel": "Unité 8 — Le pont",
  "titel": "Toets 2 — Grammaire: Passé Composé met Être & Voltooid Deelwoord Accord",
  "vak": "Frans · HAVO 3 (U8)",
  "icoon": "🏃",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Welke groep werkwoorden wordt in de passé composé vervoegd met <b>être</b> (in plaats van avoir)?", "opties": ["De werkwoorden van beweging/verandering (la maison d'être) en wederkerende werkwoorden", "Alle regelmatige werkwoorden op -er", "Alleen werkwoorden die met eten te maken hebben", "Uitsluitend onpersoonlijke werkwoorden"], "antwoord": 0, "uitleg": "De 'huiswerkwoorden' van beweging (aller, venir, partir, arriver, etc.) en wederkerende werkwoorden gaan met être."},
    {"type": "mc", "vraag": "Wat is de gouden regel voor het voltooid deelwoord bij <b>être</b>?", "opties": ["Het voltooid deelwoord past zich aan aan het onderwerp (+e bij vrouwelijk, +s bij meervoud)", "Het voltooid deelwoord verandert nooit", "Het voltooid deelwoord krijgt altijd een -x", "Er mag geen hulpwerkwoord gebruikt worden"], "antwoord": 0, "uitleg": "Bij être krijgt het deelwoord accord: +e voor vrouwelijk, +s voor meervoud (bijv. elle est allée, ils sont partis)."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Marie est allé à Paris'</i> is grammaticaal fout omdat er een <b>-e</b> achter 'allé' ontbreekt (moet zijn: <i>Marie est allée</i>).", "antwoord": True, "uitleg": "Waar. Marie is vrouwelijk, dus bij être: allée met extra -e."},
    {"type": "invul", "vraag": "Vul de juiste passé composé in voor <i>elle (partir)</i>: <i>Hier soir, elle est ... à 20h.</i>", "antwoord": "partie", "uitleg": "Elle est partie (+e voor vrouwelijk enkelvoud)."},
    {"type": "mc", "vraag": "Kies de juiste vorm voor <i>'Zij (vrouwelijk meervoud) zijn aangekomen'</i>:", "opties": ["Elles sont arrivées", "Elles ont arrivé", "Elles sont arrivé", "Elles sont arrivés"], "antwoord": 0, "uitleg": "Elles sont arrivées (vrouwelijk meervoud: +es)."},
    {"type": "waaronwaar", "vraag": "Het werkwoord <b>rester</b> (blijven) wordt vervoegd met <b>avoir</b> in de passé composé.", "antwoord": False, "uitleg": "Onwaar. 'Rester' is een bewegingswerkwoord en wordt vervoegd met <b>être</b>: il est resté, elle est restée."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>être</b>: <i>Mes amis ... tombés dans la cour.</i>", "antwoord": "sont", "uitleg": "Mes amis (ils) -> sont tombés."},
    {"type": "mc", "vraag": "Welk werkwoord hoort NIET in het rijtje van être-werkwoorden?", "opties": ["manger (eten)", "aller (gaan)", "venir (komen)", "partir (vertrekken)"], "antwoord": 0, "uitleg": "'Manger' gaat met avoir (j'ai mangé). Aller, venir en partir gaan met être."},
    {"type": "mc", "vraag": "Wat is de passé composé van <b>naître</b> (geboren worden) voor <i>elle</i>?", "opties": ["Elle est née", "Elle a né", "Elle est né", "Elle a naît"], "antwoord": 0, "uitleg": "Naître -> né; elle est née (met extra -e)."},
    {"type": "waaronwaar", "vraag": "Het voltooid deelwoord van <b>venir</b> is <b>venu</b> (bijv. <i>ils sont venus</i>).", "antwoord": True, "uitleg": "Waar. Venir -> venu; ils sont venus (+s voor meervoud)."},
    {"type": "invul", "vraag": "Vul aan (zij zijn binnengekomen): <i>Les filles sont ... dans la classe. (entrer)</i>", "antwoord": "entrées|entrees", "uitleg": "Les filles = vrouwelijk meervoud -> entrées (+es)."},
    {"type": "mc", "vraag": "Wat is het voltooid deelwoord van <b>descendre</b> (naar beneden gaan)?", "opties": ["descendu", "descendé", "descendi", "descendant"], "antwoord": 0, "uitleg": "Descendre -> descendu (il est descendu)."},
    {"type": "open", "vraag": "Leg uit waarom de twee zinnen <i>'Paul est parti'</i> en <i>'Sophie et Emma sont parties'</i> verschillende uitgangen hebben op het voltooid deelwoord.", "sleutelwoorden": ["paul/mannelijk enkelvoud/geen extra e", "sophie en emma/vrouwelijk meervoud/es/extra e en s", "être/accord/aanpassen"], "minTreffers": 2, "modelantwoord": "Omdat bij het hulpwerkwoord être het voltooid deelwoord zich aanpast aan het onderwerp: Paul is mannelijk enkelvoud (parti), terwijl Sophie en Emma vrouwelijk meervoud zijn (+es -> parties).", "uitleg": "Accord bij être: mannelijk enkelvoud = parti, vrouwelijk meervoud = parties."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Thomas et Lucas ... (gaan) au cinéma et Clara les ... (volgen).</i>", "opties": ["sont allés / a suivis", "ont allé / a suivi", "sont allés / a suivi", "sont allé / ont suivi"], "antwoord": 2, "uitleg": "Thomas et Lucas sont allés (mannelijk meervoud met être) + Clara a suivi (met avoir)."},
    {"type": "waaronwaar", "vraag": "Het werkwoord <b>mourir</b> (sterven) heeft als voltooid deelwoord <b>mort</b> (bijv. <i>il est mort</i>).", "antwoord": True, "uitleg": "Waar. Mourir -> mort (elle est morte)."},
    {"type": "invul", "vraag": "Vul het voltooid deelwoord in van <b>sortir</b> (vrouwelijk meervoud): <i>Mes sœurs sont ... avec leurs copines.</i>", "antwoord": "sorties", "uitleg": "Sortir -> sorties (+es)."},
    {"type": "mc", "vraag": "Wat betekent <b>'Elle est tombée amoureux / amoureuse'</b>?", "opties": ["Zij is verliefd geworden", "Zij is op de grond gevallen", "Zij heeft een ongeluk gehad", "Zij is boos weggelopen"], "antwoord": 0, "uitleg": "'Tomber amoureux/amoureuse' = verliefd worden."},
    {"type": "waaronwaar", "vraag": "Bij <b>avoir</b> krijgt het voltooid deelwoord in principe NOOIT een extra -e of -s gebaseerd op het onderwerp.", "antwoord": True, "uitleg": "Waar. Bij avoir past het deelwoord zich niet aan aan het onderwerp (bijv. 'Elle a parlé', 'Elles ont mangé')."},
    {"type": "invul", "vraag": "Vul aan: <i>À quelle heure es-tu ... à la maison hier ? (aankomen voor een jongen)</i>", "antwoord": "arrivé|arrive", "uitleg": "Arrivé (mannelijk enkelvoud)."},
    {"type": "mc", "vraag": "Welke zin is grammaticaal 100% foutloos?", "opties": ["Les élèves sont retournés au collège après les vacances.", "Les élèves ont retourné au collège.", "Les élèves sont retourné au collège.", "Les élèves sont retournées (voor jongens)."], "antwoord": 0, "uitleg": "Les élèves (mannelijk meervoud) -> sont retournés (+s)."}
  ]
}

# EXAMEN 38: Stones & Communication U8 (Signaalwoorden, Examenstrategieën & Cito-training)
ex38 = {
  "id": "ex-h3-frans-38",
  "hoofdstuk": 8,
  "hoofdstukTitel": "Unité 8 — Le pont",
  "titel": "Toets 3 — Communication & Cito: Signaalwoorden, Tekstverbanden & Strategie",
  "vak": "Frans · HAVO 3 (U8)",
  "icoon": "🎯",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Welk Frans signaalwoord geeft een <b>tegenstelling</b> aan?", "opties": ["Mais / Pourtant / Cependant", "Car / Parce que", "Donc / Par conséquent", "D'abord / Ensuite"], "antwoord": 0, "uitleg": "'Mais', 'pourtant' en 'cependant' geven een tegenstelling aan (maar / echter / toch)."},
    {"type": "mc", "vraag": "Welk signaalwoord drukt een <b>reden of oorzaak</b> uit (want / omdat)?", "opties": ["Car / Parce que", "Donc / Ainsi", "Bien que / Malgré", "Enfin / Finalement"], "antwoord": 0, "uitleg": "'Car' en 'parce que' betekenen want / omdat."},
    {"type": "waaronwaar", "vraag": "Het Franse signaalwoord <b>'donc'</b> betekent 'dus / daarom' en leidt een gevolg of conclusie in.", "antwoord": True, "uitleg": "Waar. 'Donc' betekent dus / bijgevolg."},
    {"type": "invul", "vraag": "Vul het Franse signaalwoord in voor <i>maar / echter</i>: <i>Il aime le foot, ... il préfère le tennis.</i>", "antwoord": "mais|cependant|pourtant", "uitleg": "'Mais' = maar."},
    {"type": "mc", "vraag": "Wat is een slimme Cito-leesstrategie als je een onbekend Frans woord tegenkomt?", "opties": ["Kijken naar de context van de zin en letten op herkenbare stammen of internationale leenwoorden", "Direct stoppen met lezen en een willekeurig antwoord kiezen", "Elk onbekend woord overslaan zonder de alinea te begrijpen", "Alleen de laatste zin van de tekst lezen"], "antwoord": 0, "uitleg": "Contextaanwijzingen en woordstammen helpen de betekenis af te leiden."},
    {"type": "waaronwaar", "vraag": "De titel en tussenkopjes van een Franse tekst geven direct inzicht in het hoofdonderwerp van de alinea's.", "antwoord": True, "uitleg": "Waar. Oriënterend lezen van koppen bespaart veel tijd."},
    {"type": "invul", "vraag": "Vertaal het signaalwoord <i>ten eerste / om te beginnen</i> naar het Frans: <i>... , analysons les faits.</i>", "antwoord": "D'abord|Premièrement|Premierement", "uitleg": "'D'abord' of 'premièrement'."},
    {"type": "mc", "vraag": "Wat betekent het signaalwoord <b>'enfin'</b> of <b>'finalement'</b>?", "opties": ["tenslotte / uiteindelijk", "allereerst", "plotseling", "nooit meer"], "antwoord": 0, "uitleg": "'Enfin' en 'finalement' sluiten een opsomming of verhaal af."},
    {"type": "mc", "vraag": "Welk signaalwoord geeft een <b>voorbeeld</b> aan?", "opties": ["Par exemple", "Par hasard", "Par cœur", "Par contre"], "antwoord": 0, "uitleg": "'Par exemple' betekent bijvoorbeeld."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'par contre'</b> betekent 'daarentegen / aan de andere kant'.", "antwoord": True, "uitleg": "Waar. 'Par contre' geeft een contrast aan."},
    {"type": "invul", "vraag": "Wat betekent het signaalwoord <b>'aussi'</b> aan het begin van een toevoeging?", "antwoord": "ook|tevens|eveneens", "uitleg": "'Aussi' betekent ook / eveneens."},
    {"type": "mc", "vraag": "Wat betekent <b>'selon le texte'</b> in een Cito-vraag?", "opties": ["volgens de tekst", "ondanks de tekst", "buiten de tekst", "in tegenstelling tot de auteur"], "antwoord": 0, "uitleg": "'Selon le texte' = volgens de tekst."},
    {"type": "open", "vraag": "Noem drie belangrijke Franse signaalwoorden: één voor tegenstelling, één voor oorzaak, en één voor gevolg.", "sleutelwoorden": ["mais/pourtant/cependant", "car/parce que", "donc/alors/ainsi"], "minTreffers": 3, "modelantwoord": "Tegenstelling: 'mais' (maar), Oorzaak: 'parce que' (omdat), Gevolg: 'donc' (dus).", "uitleg": "Mais (tegenstelling), parce que/car (oorzaak), donc (gevolg)."},
    {"type": "mc", "vraag": "Wat betekent <b>'Qu'est-ce qui est vrai selon le dernier paragraphe ?'</b>?", "opties": ["Wat is waar volgens de laatste alinea?", "Wat is onjuist volgens de inleiding?", "Waarom stopt de auteur met schrijven?", "Wie heeft de laatste alinea geschreven?"], "antwoord": 0, "uitleg": "'Vrai selon le dernier paragraphe' = waar volgens de laatste alinea."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'le but'</b> in een examenvraag betekent 'het doel van de tekst of van de auteur'.", "antwoord": True, "uitleg": "Waar. 'Le but du texte' = het doel van de tekst."},
    {"type": "invul", "vraag": "Vertaal het vraagwoord <i>Waarom</i> naar het Frans: <i>... l'auteur a-t-il écrit cet article ?</i>", "antwoord": "Pourquoi", "uitleg": "'Pourquoi' = waarom."},
    {"type": "mc", "vraag": "Wat betekent <b>'De quoi s'agit-il dans ce texte ?'</b>?", "opties": ["Waarover gaat het in deze tekst?", "Hoeveel woorden telt deze tekst?", "Waar is deze tekst gedrukt?", "Wanneer is de auteur geboren?"], "antwoord": 0, "uitleg": "'De quoi s'agit-il' = waar gaat het over."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'surtout'</b> betekent 'vooral / in het bijzonder'.", "antwoord": True, "uitleg": "Waar. 'Surtout' = vooral."},
    {"type": "invul", "vraag": "Wat betekent het signaalwoord <b>'grâce à'</b>?", "antwoord": "dankzij|met dank aan", "uitleg": "'Grâce à' betekent dankzij (positieve oorzaak; négatief: à cause de = wegens/door)."},
    {"type": "mc", "vraag": "Wat betekent <b>'à cause de'</b>?", "opties": ["door / wegens (met een negatieve oorzaak)", "dankzij een geweldige gebeurtenis", "zonder reden", "ongeacht de gevolgen"], "antwoord": 0, "uitleg": "'À cause de' = vanwege / door (ongunstige oorzaak)."}
  ]
}

# EXAMEN 39: Leesvaardigheid U8 (Cito-teksten HAVO 3 Niveau, Maatschappij & Jongeren)
ex39 = {
  "id": "ex-h3-frans-39",
  "hoofdstuk": 8,
  "hoofdstukTitel": "Unité 8 — Le pont",
  "titel": "Toets 4 — Leesvaardigheid: Cito-Tekstbegrip, Maatschappij & Milieu",
  "vak": "Frans · HAVO 3 (U8)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Lees het artikel: <i>'En France, de plus en plus de lycéens s'engagent pour le climat en participant à des marches pour la planète et en nettoyant les forêts locales le week-end.'</i><br>Hoe zetten steeds meer Franse middelbare scholieren zich in voor het klimaat?", "opties": ["Door mee te doen aan klimaatmarsen en bossen schoon te maken in het weekend", "Door bomen te kappen", "Door te staken tegen huiswerk", "Door alleen nog online les te volgen"], "antwoord": 0, "uitleg": "'Marches pour la planète et nettoyant les forêts'."},
    {"type": "mc", "vraag": "Lees de alinea: <i>'Bien que les smartphones soient interdits en classe dans les collèges français, certains professeurs les autorisent ponctuellement pour des activités pédagogiques ou des quiz en ligne.'</i><br>Wanneer mogen telefoons bij uitzondering wel gebruikt worden?", "opties": ["Bij specifieke educatieve activiteiten of online quizzen van de docent", "Tijdens de lunchpauze in het lokaal", "Wanneer leerlingen zich vervelen", "Tijdens officiële eindexamens"], "antwoord": 0, "uitleg": "'Pour des activités pédagogiques ou des quiz'."},
    {"type": "waaronwaar", "vraag": "Het signaalwoord <b>'bien que'</b> betekent 'hoewel / alhoewel'.", "antwoord": True, "uitleg": "Waar. 'Bien que' leidt een concessie/tegenstelling in (hoewel)."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'interdit'</b> in een schoolreglement?", "antwoord": "verboden|niet toegestaan", "uitleg": "'Interdit' = verboden."},
    {"type": "mc", "vraag": "Lees het bericht: <i>'Grâce au développement des pistes cyclables à Paris, le nombre de déplacements à vélo a triplé en seulement trois ans.'</i><br>Wat is het gevolg van de nieuwe fietspaden in Parijs?", "opties": ["Het aantal fietsritten is in drie jaar tijd verdrievoudigd", "Er zijn minder fietsers dan voorheen", "Het autoverkeer staat overal stil", "Fietsen is verboden geworden in het centrum"], "antwoord": 0, "uitleg": "'A triplé' = is verdrievoudigd."},
    {"type": "waaronwaar", "vraag": "Het werkwoord <b>'tripler'</b> betekent halveren.", "antwoord": False, "uitleg": "Onwaar. 'Tripler' betekent verdrievoudigen (drie keer zoveel worden)."},
    {"type": "invul", "vraag": "Lees: <i>'Un séjour de deux semaines en immersion totale.'</i><br>Hoeveel weken duurt dit taalverblijf?", "antwoord": "2|twee|deux", "uitleg": "Deux semaines = twee weken."},
    {"type": "mc", "vraag": "Wat betekent <b>'en immersion totale'</b> bij een taalcursus?", "opties": ["volledig ondergedompeld in de taal en cultuur (bijv. in een gastgezin)", "alleen online via een app leren", "met een Nederlandse klasgenoot op een hotelkamer", "zonder ooit een woord Frans te spreken"], "antwoord": 0, "uitleg": "Volledige taalbad-ervaring (immersion)."},
    {"type": "mc", "vraag": "Lees de conclusie: <i>'En résumé, apprendre une langue étrangère dès le plus jeune âge facilite grandement l'ouverture d'esprit et les opportunités professionnelles.'</i><br>Wat is volgens de auteur het grote voordeel van jong een vreemde taal leren?", "opties": ["Het bevordert een open blik op de wereld en biedt meer carrièremogelijkheden", "Het maakt andere schoolvakken overbodig", "Je hoeft nooit meer te studeren", "Je mag gratis reizen met de trein"], "antwoord": 0, "uitleg": "'Ouverture d'esprit et opportunités professionnelles'."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'en résumé'</b> leidt een samenvatting / conclusie in.", "antwoord": True, "uitleg": "Waar. 'En résumé' = samenvattend."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'faciliter'</b>?", "antwoord": "vergemakkelijken|makkelijker maken|bevorderen", "uitleg": "'Faciliter' = vergemakkelijken."},
    {"type": "mc", "vraag": "Lees de stelling: <i>'Malgré les difficultés initiales, Juliette a réussi à s'intégrer parfaitement dans son nouveau lycée à Bordeaux.'</i><br>Wat betekent het signaalwoord 'Malgré'?", "opties": ["Ondanks", "Dankzij", "Omdat", "Zonder"], "antwoord": 0, "uitleg": "'Malgré' = ondanks."},
    {"type": "open", "vraag": "Lees: <i>'Le recyclage des déchets et la réduction de l'utilisation du plastique sont les deux priorités environnementales de la commune.'</i><br>Wat zijn de twee milieuprioriteiten van de gemeente?", "sleutelwoorden": ["recycling/afval/afvalscheiding/déchets", "plastic/gebruik/vermindering/reductie"], "minTreffers": 2, "modelantwoord": "1. Afvalrecycling (le recyclage des déchets), 2. Vermindering van plasticgebruik (la réduction du plastique).", "uitleg": "Recyclage des déchets en réduction du plastique."},
    {"type": "mc", "vraag": "Wat betekent <b>'les déchets'</b> in milieuteksten?", "opties": ["afval / vuilnis", "verse groenten", "nieuwe gebouwen", "elektrische auto's"], "antwoord": 0, "uitleg": "'Les déchets' = afval / vuilnis."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'quotidien'</b> (bijv. <i>la vie quotidienne</i>) betekent 'het dagelijks leven'.", "antwoord": True, "uitleg": "Waar. 'Quotidien' = dagelijks."},
    {"type": "invul", "vraag": "Wat betekent <b>'améliorer'</b> in: <i>'Ce projet vise à améliorer la qualité de vie des habitants'</i>?", "antwoord": "verbeteren|beter maken", "uitleg": "'Améliorer' = verbeteren."},
    {"type": "mc", "vraag": "Lees het advies: <i>'Il est essentiel de dormir au moins huit heures par nuit pour rester concentré durant les cours.'</i><br>Hoeveel uur slaap per nacht wordt minimaal aangeraden voor scholieren?", "opties": ["Minimaal 8 uur", "Maximaal 5 uur", "Precies 12 uur", "Slaap maakt niet uit"], "antwoord": 0, "uitleg": "'Au moins huit heures par nuit' = minimaal 8 uur."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'au moins'</b> betekent 'hoogstens / maximaal'.", "antwoord": False, "uitleg": "Onwaar. 'Au moins' betekent 'minstens / minimaal'. Hoogstens is 'au plus / au maximum'."},
    {"type": "invul", "vraag": "Wat betekent het woord <b>'efficace'</b> in: <i>'Une méthode efficace pour apprendre le vocabulaire'</i>?", "antwoord": "effectief|doeltreffend|efficiënt|succesvol", "uitleg": "'Efficace' = effectief / doeltreffend."},
    {"type": "mc", "vraag": "Wat is het hoofddoel van een Franse Cito-examentekst over jongeren en maatschappelijke betrokkenheid?", "opties": ["Informatie geven over actuele thema's en nagaan of je de kern en argumenten begrijpt", "Je grammaticaal dictee afnemen", "Controleren of je alle werkwoorden uit je hoofd kent", "Je Frans laten vertalen in het Latijn"], "antwoord": 0, "uitleg": "Tekstbegrip en inzicht in standpunten en argumenten."}
  ]
}

# EXAMEN 40: Het Grote Eindexamen Frans HAVO 3 (Volledige Curriculum-Mix)
ex40 = {
  "id": "ex-h3-frans-40",
  "hoofdstuk": 8,
  "hoofdstukTitel": "Unité 8 — Le pont",
  "titel": "Toets 5 — Grote Eindtoets Frans HAVO 3 (Examen-Simulatie U1-U8)",
  "vak": "Frans · HAVO 3 (U8)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "Kies de juiste passé composé met <b>être</b>: <i>Hier, Juliette ... (vertrekken) à huit heures.</i>", "opties": ["est partie", "a parti", "est parti", "est partit"], "antwoord": 0, "uitleg": "Juliette (vrouwelijk) + être -> est partie (+e)."},
    {"type": "mc", "vraag": "Welk delend lidwoord hoort in: <i>Au petit-déjeuner, je mange ... (wat) pain avec ... (wat) confiture.</i>?", "opties": ["du / de la", "de la / du", "de l' / des", "le / la"], "antwoord": 0, "uitleg": "Du pain (mannelijk) en de la confiture (vrouwelijk)."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Nous allons visiter le Louvre'</i> staat het werkwoord in de futur composé.", "antwoord": True, "uitleg": "Waar. Allons + visiter = futur composé."},
    {"type": "invul", "vraag": "Vervoeg <b>faire</b> voor <i>vous</i>: <i>Qu'est-ce que vous ... ce soir ?</i>", "antwoord": "faites", "uitleg": "Vous faites."},
    {"type": "mc", "vraag": "Wat is het vrouwelijk enkelvoud van <b>beau</b> en <b>vieux</b>?", "opties": ["belle / vieille", "beaue / vielle", "belles / vieilles", "bel / vieux"], "antwoord": 0, "uitleg": "Beau -> belle en vieux -> vieille."},
    {"type": "waaronwaar", "vraag": "Het Franse signaalwoord <b>'cependant'</b> betekent 'daarom'.", "antwoord": False, "uitleg": "Onwaar. 'Cependant' betekent 'echter / desalniettemin'. 'Daarom' is 'donc / c'est pourquoi'."},
    {"type": "invul", "vraag": "Vul het juiste bezittelijk voornaamwoord in: <i>C'est ... (mijn) amie Emma.</i>", "antwoord": "mon", "uitleg": "Mon amie (vóór een klinker gebruik je mon in plaats van ma)."},
    {"type": "mc", "vraag": "Hoe vraag je beleefd om de rekening in een restaurant?", "opties": ["L'addition, s'il vous plaît !", "Donnez-moi la carte !", "Combien coûte le serveur ?", "Où est la sortie ?"], "antwoord": 0, "uitleg": "L'addition, s'il vous plaît !"},
    {"type": "mc", "vraag": "Wat is de vergrotende trap van <b>bon</b> (goed)?: <i>Cette pizza est ... que l'autre.</i>", "opties": ["meilleure", "plus bonne", "aussi bonne", "la plus bonne"], "antwoord": 0, "uitleg": "Meilleure (bon -> meilleur; pizza is vrouwelijk -> meilleure)."},
    {"type": "waaronwaar", "vraag": "In het Frans zeg je <i>'J'ai 14 ans'</i> met het werkwoord <b>avoir</b>.", "antwoord": True, "uitleg": "Waar. Leeftijd wordt uitgedrukt met avoir."},
    {"type": "invul", "vraag": "Vervoeg <b>prendre</b> voor <i>ils/elles</i>: <i>Ils ... le train pour Paris.</i>", "antwoord": "prennent", "uitleg": "Ils prennent (dubbele n)."},
    {"type": "mc", "vraag": "Wat betekent <b>'tout droit'</b> bij een routebeschrijving?", "opties": ["rechtdoor", "rechtsaf", "linksaf", "omkeren"], "antwoord": 0, "uitleg": "Tout droit = rechtdoor."},
    {"type": "open", "vraag": "Leg in het kort uit wat de twee belangrijkste verschillen zijn tussen de <b>passé composé met avoir</b> en de <b>passé composé met être</b>.", "sleutelwoorden": ["avoir/geen aanpassing/meeste werkwoorden", "être/beweging/huis/accord/past zich aan/vrouwelijk/meervoud"], "minTreffers": 2, "modelantwoord": "1. Werkwoorden met être zijn bewegingswerkwoorden (of wederkerend), terwijl de meeste andere werkwoorden met avoir gaan. 2. Bij être past het voltooid deelwoord zich aan aan het onderwerp (+e bij vrouwelijk, +s bij meervoud), bij avoir niet.", "uitleg": "Être = bewegingswerkwoorden + accord met onderwerp; Avoir = meeste werkwoorden, geen accord met onderwerp."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Hier, les filles ... (arriver) à l'heure et elles ... (manger) une crêpe.</i>", "opties": ["sont arrivées / ont mangé", "ont arrivé / ont mangé", "sont arrivés / sont mangées", "étaient / mangeaient"], "antwoord": 0, "uitleg": "Sont arrivées (met être en +es) + ont mangé (met avoir)."},
    {"type": "waaronwaar", "vraag": "De ontkenning <b>'ne ... jamais'</b> betekent 'niets'.", "antwoord": False, "uitleg": "Onwaar. 'Ne...jamais' is 'nooit'. 'Niets' is 'ne...rien'."},
    {"type": "invul", "vraag": "Vertaal het woord <i>zakgeld</i> naar het Frans in drie woorden: <i>L'... de ... .</i>", "antwoord": "argent de poche", "uitleg": "L'argent de poche."},
    {"type": "mc", "vraag": "Wat is het meervoud van <b>un nouveau manteau</b>?", "opties": ["de nouveaux manteaux", "des nouveaus manteaus", "de nouvelles manteaux", "des nouveau manteaux"], "antwoord": 0, "uitleg": "De nouveaux manteaux (beide -x in meervoud)."},
    {"type": "waaronwaar", "vraag": "In Frankrijk is 14 juli (le 14 juillet) de nationale feestdag.", "antwoord": True, "uitleg": "Waar. Quatorze Juillet = Fête nationale."},
    {"type": "invul", "vraag": "Vertaal het signaalwoord <i>omdat</i> naar het Frans: <i>Je suis fatigué ... j'ai mal dormi.</i>", "antwoord": "parce que|car|puisque", "uitleg": "Parce que of car."},
    {"type": "mc", "vraag": "Wat betekent <b>'Réussir son année scolaire'</b>?", "opties": ["Overgaan naar het volgende schooljaar / slagen", "Zakken en blijven zitten", "Van school wisselen", "Spijbelen tijdens de les"], "antwoord": 0, "uitleg": "Réussir = slagen / succesvol overgaan."}
  ]
}

write_examen("examen_36.js", ex36)
write_examen("examen_37.js", ex37)
write_examen("examen_38.js", ex38)
write_examen("examen_39.js", ex39)
write_examen("examen_40.js", ex40)
print("Frans Unité 8 exams (36 to 40) generated successfully!")
