#!/usr/bin/env python3
"""
Generate Frans Unité 1 Proeftoetsen (5 exams x 20 questions = 100 questions)
Grandes Lignes 3 HAVO - Unité 1: Poste, like, partage
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

# EXAMEN 1: Vocabulaire & Mots-clés (Social Media, Communicatie, Vriendschap)
ex1 = {
  "id": "ex-h3-frans-1",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Toets 1 — Vocabulaire: Social Media, Vriendschap & Communicatie",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "📱",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent het Franse woord <b>'partager'</b>?", "opties": ["delen (op sociale media)", "verwijderen", "opslaan", "blokkeren"], "antwoord": 0, "uitleg": "'Partager' betekent 'delen', zoals in 'partager une photo'."},
    {"type": "mc", "vraag": "Wat is de Franse vertaling van <b>'een bericht sturen'</b>?", "opties": ["envoyer un message", "recevoir un coup de fil", "télécharger une vidéo", "fermer l'écran"], "antwoord": 0, "uitleg": "'Envoyer un message' betekent een bericht versturen."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'un ami virtuel'</b> een echte vriend die je elke dag op school ziet.", "antwoord": False, "uitleg": "Onwaar. 'Un ami virtuel' is een online/internetvriend."},
    {"type": "invul", "vraag": "Vul het Franse zelfstandig naamwoord in voor <i>smartphone / mobiele telefoon</i>: <i>J'ai perdu mon ... .</i>", "antwoord": "portable|smartphone|téléphone portable", "uitleg": "'Un portable' (of smartphone) is een mobiele telefoon."},
    {"type": "mc", "vraag": "Wat betekent <b>'supprimer un compte'</b>?", "opties": ["een account verwijderen", "een account aanmaken", "wachtwoord wijzigen", "een vriend toevoegen"], "antwoord": 0, "uitleg": "'Supprimer' betekent verwijderen of wissen."},
    {"type": "waaronwaar", "vraag": "Het Franse werkwoord <b>'liker'</b> betekent een foto of bericht leuk vinden op sociale media.", "antwoord": True, "uitleg": "Waar. 'Liker' is een leenwoord dat veel in modern Frans gebruikt wordt."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'wachtwoord'</i> naar het Frans: <i>N'oublie pas ton ... de passe.</i>", "antwoord": "mot", "uitleg": "'Le mot de passe' is het Franse woord voor wachtwoord."},
    {"type": "mc", "vraag": "Wat betekent de uitdrukking <b>'être accro aux réseaux sociaux'</b>?", "opties": ["verslaafd zijn aan sociale netwerken", "geen internetverbinding hebben", "een nieuw kanaal starten", "offline studeren"], "antwoord": 0, "uitleg": "'Être accro à' betekent ergens aan verslaafd / verknocht zijn."},
    {"type": "mc", "vraag": "Kies de juiste betekenis van <b>'un réseau social'</b>:", "opties": ["een sociaal netwerk (zoals Instagram of TikTok)", "een computerlokaal", "een schoolkrant", "een telefoonoplader"], "antwoord": 0, "uitleg": "'Un réseau social' (meervoud: réseaux sociaux) is een sociaal netwerk."},
    {"type": "waaronwaar", "vraag": "Het werkwoord <b>'télécharger'</b> betekent uitsluitend 'een foto printen op papier'.", "antwoord": False, "uitleg": "Onwaar. 'Télécharger' betekent downloaden of uploaden."},
    {"type": "invul", "vraag": "Vul het Franse woord in voor <i>vriendschap</i>: <i>L'... est très importante pour les adolescents.</i>", "antwoord": "amitié|amitie", "uitleg": "'L'amitié' betekent vriendschap."},
    {"type": "mc", "vraag": "Wat is <b>'un abonné'</b> op YouTube of Instagram?", "opties": ["een volger / abonnee", "een reclameboodschap", "een negatieve reactie", "een moderator"], "antwoord": 0, "uitleg": "'Un abonné' (follower/subscriber) is een volger of abonnee."},
    {"type": "open", "vraag": "Leg in het Nederlands uit wat een <b>'influenceur'</b> (of influenceuse) doet op sociale netwerken.", "sleutelwoorden": ["volgers/publiek/mensen", "beïnvloeden/producten/video/promoten/mening/content"], "minTreffers": 1, "modelantwoord": "Een influencer maakt content op sociale media en beïnvloedt de meningen, levensstijl of aankopen van volgers.", "uitleg": "Een influencer bereikt veel mensen online en maakt promotie of deelt vlogs/tips."},
    {"type": "mc", "vraag": "Wat betekent <b>'un écran'</b>?", "opties": ["een beeldscherm / scherm", "een muis", "een toetsenbord", "een koptelefoon"], "antwoord": 0, "uitleg": "'Un écran' is een scherm (van tv, telefoon of computer)."},
    {"type": "waaronwaar", "vraag": "De Franse uitdrukking <b>'passer du temps en ligne'</b> betekent 'tijd doorbrengen op het internet'.", "antwoord": True, "uitleg": "Waar. 'En ligne' betekent online."},
    {"type": "invul", "vraag": "Vertaal het werkwoord <i>reageren / commentaar geven</i> naar het Frans: <i>Tu peux ... sous ma vidéo.</i>", "antwoord": "commenter|réagir|reagir", "uitleg": "'Commenter' betekent een reactie achterlaten."},
    {"type": "mc", "vraag": "Wat betekent <b>'un internaute'</b>?", "opties": ["een internetgebruiker", "een astronaut", "een computertechnicus", "een cameraman"], "antwoord": 0, "uitleg": "'Un internaute' is een internetter / internetgebruiker."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'la notification'</b> betekent een pop-up melding op je telefoon.", "antwoord": True, "uitleg": "Waar. 'Une notification' is een melding of notificatie."},
    {"type": "invul", "vraag": "Vul het ontbrekende woord in: <i>Je vais ... une photo sur Instagram (plaatsen/posten).</i>", "antwoord": "poster|publier", "uitleg": "'Poster' of 'publier' betekent een bericht of foto plaatsen."},
    {"type": "mc", "vraag": "Wat betekent <b>'rester en contact avec des amis'</b>?", "opties": ["in contact blijven met vrienden", "ruzie maken met vrienden", "nieuwe klasgenoten ontmoeten", "je telefoon uitschakelen"], "antwoord": 0, "uitleg": "'Rester en contact' betekent contact houden."}
  ]
}

# EXAMEN 2: Grammaire (Présent: regelmatige werkwoorden op -er, être & avoir, ontkenning)
ex2 = {
  "id": "ex-h3-frans-2",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Toets 2 — Grammaire: Présent (-er werkwoorden, être, avoir & ontkenning)",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "📝",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Welke uitgang hoort bij <b>'nous'</b> bij regelmatige werkwoorden op -er?", "opties": ["-ons", "-ez", "-ent", "-es"], "antwoord": 0, "uitleg": "Bij 'nous' is de uitgang altijd '-ons' (bijv. nous parlons)."},
    {"type": "mc", "vraag": "Vervoeg <b>'être'</b> voor <i>vous</i>:", "opties": ["vous êtes", "vous sommes", "vous ont", "vous avez"], "antwoord": 0, "uitleg": "De vervoeging van être is: je suis, tu es, il/elle est, nous sommes, vous êtes, ils/elles sont."},
    {"type": "waaronwaar", "vraag": "De vorm van <b>'avoir'</b> bij <i>ils</i> is <i>'ils sont'</i>.", "antwoord": False, "uitleg": "Onwaar. 'Ils sont' is van être (zijn). Bij avoir is het 'ils ont' (zij hebben)."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>parler</b>: <i>Tu ... très bien français.</i>", "antwoord": "parles", "uitleg": "Bij 'tu' krijgt een -er werkwoord de uitgang -es: tu parles."},
    {"type": "mc", "vraag": "Hoe maak je de zin <i>'Je regarde la vidéo'</i> ontkennend?", "opties": ["Je ne regarde pas la vidéo.", "Je regarde ne pas la vidéo.", "Je pas regarde la vidéo.", "Je ne pas regarde la vidéo."], "antwoord": 0, "uitleg": "De ontkenning staat om de persoonsvorm: ne + werkwoord + pas."},
    {"type": "waaronwaar", "vraag": "Vóór een klinker of stomme h verandert <b>'ne'</b> in <b>'n\''</b> (bijv. <i>Il n'aime pas</i>).", "antwoord": True, "uitleg": "Waar. Voor een klinker trek je 'ne' samen tot 'n\''."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>avoir</b>: <i>Nous ... un nouveau projet au collège.</i>", "antwoord": "avons", "uitleg": "'Nous avons' betekent 'wij hebben'."},
    {"type": "mc", "vraag": "Kies de juiste vorm: <i>Les élèves ... (écouter) la musique.</i>", "opties": ["écoutent", "écoute", "écoutons", "écoutez"], "antwoord": 0, "uitleg": "Les élèves = ils/elles (meervoud), dus de uitgang is -ent."},
    {"type": "mc", "vraag": "Welke vorm van <b>être</b> past in de zin: <i>Emma ... toujours connectée.</i>?", "opties": ["est", "es", "suis", "sommes"], "antwoord": 0, "uitleg": "Emma = elle (3e persoon enkelvoud), dus 'est'."},
    {"type": "waaronwaar", "vraag": "Bij <b>'je'</b> eindigt de tegenwoordige tijd van een -er werkwoord op een <b>-s</b> (zoals <i>je habites</i>).", "antwoord": False, "uitleg": "Onwaar. Bij 'je' is de uitgang -e (j'habite). Bij 'tu' is het -es (tu habites)."},
    {"type": "invul", "vraag": "Vul de ontkenning in voor <i>(aime)</i>: <i>Il ... les jeux vidéo. (hij houdt niet van)</i>", "antwoord": "n'aime pas|naime pas", "uitleg": "Il n'aime pas (n' + aime + pas)."},
    {"type": "mc", "vraag": "Vervoeg <b>'partager'</b> bij <i>nous</i>:", "opties": ["nous partageons", "nous partagons", "nous partagez", "nous partagent"], "antwoord": 0, "uitleg": "Bij werkwoorden op -ger voeg je een extra 'e' toe voor de 'o' om de zachte g-klank te behouden: partageons."},
    {"type": "open", "vraag": "Leg uit waarom de zin <i>'Ils ont français'</i> iets anders betekent dan <i>'Ils sont français'</i>.", "sleutelwoorden": ["hebben/avoir", "zijn/être", "franse les/vak/nationaliteit/fransman"], "minTreffers": 1, "modelantwoord": "'Ils ont français' betekent 'Zij hebben Frans (les/vak)', terwijl 'Ils sont français' betekent 'Zij zijn Frans (nationaliteit)'.", "uitleg": "Ont komt van avoir (hebben), sont komt van être (zijn)."},
    {"type": "mc", "vraag": "Wat is de juiste vorm: <i>Vous ... (habiter) à Paris?</i>", "opties": ["habitez", "habitons", "habite", "habitent"], "antwoord": 0, "uitleg": "Bij 'vous' is de regelmatige uitgang -ez (habitez)."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'j\''</b> gebruik je als het werkwoord begint met een klinker (bijv. <i>j'adore</i>).", "antwoord": True, "uitleg": "Waar. Je wordt j' voor een klinker of stomme h."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>télécharger</b>: <i>Je ... une nouvelle application.</i>", "antwoord": "télécharge|telecharge", "uitleg": "Je télécharge (uitgang -e)."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Tu ... (zijn) sur TikTok et tu ... (hebben) 500 abonnés.</i>", "opties": ["es / as", "est / a", "suis / ai", "êtes / avez"], "antwoord": 0, "uitleg": "Tu es (jij bent) + tu as (jij hebt)."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Nous ne parlons pas anglais'</i> betekent 'Wij spreken wel Engels'.", "antwoord": False, "uitleg": "Onwaar. 'Ne...pas' betekent 'niet', dus 'Wij spreken geen Engels'."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>être</b>: <i>Moi et Lucas, nous ... très contents.</i>", "antwoord": "sommes", "uitleg": "Moi et Lucas = nous -> nous sommes."},
    {"type": "mc", "vraag": "Welke uitgangen horen bij regelmatige werkwoorden op <b>-er</b> (présent van je t/m ils)?", "opties": ["-e, -es, -e, -ons, -ez, -ent", "-s, -s, -t, -ons, -ez, -ent", "-e, -s, -e, -ons, -ez, -ent", "-is, -is, -it, -issons, -issez, -issent"], "antwoord": 0, "uitleg": "De vaste uitgangen van de -er groep zijn: -e, -es, -e, -ons, -ez, -ent."}
  ]
}

# EXAMEN 3: Stones & Communication (Zich voorstellen, online profiel, mening geven)
ex3 = {
  "id": "ex-h3-frans-3",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Toets 3 — Communication: Zich voorstellen, Sociale Media & Vragen stellen",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "💬",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vraag je beleefd aan iemand: <i>'Hoe heet jij?'</i> in het Frans?", "opties": ["Comment tu t'appelles ?", "Où tu habites ?", "Quel âge as-tu ?", "Qu'est-ce que tu fais ?"], "antwoord": 0, "uitleg": "'Comment tu t'appelles ?' betekent 'Hoe heet je?'."},
    {"type": "mc", "vraag": "Wat zeg je als je wilt zeggen: <i>'Ik ben 14 jaar oud'</i>?", "opties": ["J'ai 14 ans.", "Je suis 14 ans.", "J'habite 14 ans.", "Je fais 14 ans."], "antwoord": 0, "uitleg": "In het Frans gebruik je 'avoir' voor leeftijd: J'ai 14 ans (letterlijk: ik heb 14 jaar)."},
    {"type": "waaronwaar", "vraag": "Om te vragen <i>'Waar woon je?'</i> vraag je in het Frans: <i>'Où tu habites ?'</i>.", "antwoord": True, "uitleg": "Waar. 'Où' betekent 'waar'."},
    {"type": "invul", "vraag": "Vul aan om te zeggen <i>'Ik woon in Nederland'</i>: <i>J'habite ... Pays-Bas.</i>", "antwoord": "aux", "uitleg": "'Les Pays-Bas' is meervoud, dus voorzetsel 'aux' (à + les = aux)."},
    {"type": "mc", "vraag": "Hoe vraag je naar iemands mening over een post of foto?", "opties": ["Qu'est-ce que tu penses de ma photo ?", "Combien coûte cette photo ?", "Pourquoi tu vends cette photo ?", "Où est prise cette photo ?"], "antwoord": 0, "uitleg": "'Qu'est-ce que tu penses de...' betekent 'Wat vind je van...'."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'À mon avis'</b> betekent in het Nederlands 'Volgens mij / Naar mijn mening'.", "antwoord": True, "uitleg": "Waar. 'À mon avis' leidt een persoonlijke mening in."},
    {"type": "invul", "vraag": "Vul het vraagwoord in (Wat): <i>... tu fais sur ton téléphone ?</i>", "antwoord": "Qu'est-ce que|Que", "uitleg": "'Qu'est-ce que' betekent 'wat'."},
    {"type": "mc", "vraag": "Hoe reageer je enthousiast op een toffe foto van een vriend?", "opties": ["C'est super joli ! / C'est trop cool !", "C'est affreux et moche.", "Je n'aime pas du tout.", "Supprime vite ça."], "antwoord": 0, "uitleg": "'C'est super joli' of 'C'est trop cool' is een positieve reactie."},
    {"type": "mc", "vraag": "Wat vraag je als je wilt weten wat iemands favoriete app is?", "opties": ["Quelle est ton application préférée ?", "Où se trouve l'application ?", "Qui a créé cette application ?", "Combien pèse ton téléphone ?"], "antwoord": 0, "uitleg": "'Quelle est ton application préférée ?' vraagt naar de lievelingsapp."},
    {"type": "waaronwaar", "vraag": "Als iemand vraagt <i>'Tu as des frères et sœurs ?'</i> vraagt diegene naar je hobby's.", "antwoord": False, "uitleg": "Onwaar. Dit vraagt of je broers en zussen hebt."},
    {"type": "invul", "vraag": "Vul aan om te zeggen <i>'Ik ben dol op'</i>: <i>J'... écouter de la musique sur Spotify.</i>", "antwoord": "adore|aime", "uitleg": "J'adore (ik ben dol op) of J'aime (ik hou van)."},
    {"type": "mc", "vraag": "Hoe vraag je: <i>'Wil je mijn video liken en delen?'</i>", "opties": ["Tu veux liker et partager ma vidéo ?", "Tu dois effacer ma vidéo ?", "Tu as enregistré ma vidéo ?", "Tu vends ma vidéo ?"], "antwoord": 0, "uitleg": "'Tu veux liker et partager ma vidéo ?' is de juiste vraag."},
    {"type": "open", "vraag": "Schrijf in het Frans een korte introductiezin waarin je vertelt hoe je heet en hoe oud je bent.", "sleutelwoorden": ["m'appelle/je suis/nom", "j'ai/ans"], "minTreffers": 1, "modelantwoord": "Je m'appelle Duru et j'ai 14 ans.", "uitleg": "Standaardzin: 'Je m'appelle [naam] et j'ai [leeftijd] ans.'"},
    {"type": "mc", "vraag": "Wat betekent de beleefde afsluiting van een bericht: <b>'À plus !'</b> (of A+) ?", "opties": ["Tot later! / Tot ziens!", "Nooit meer!", "Gefeliciteerd!", "Welterusten!"], "antwoord": 0, "uitleg": "'À plus' (afkorting van à plus tard) betekent 'tot later'."},
    {"type": "waaronwaar", "vraag": "In een Franse chat betekent <b>'MDR'</b> (mort de rire) hetzelfde als het Engelse 'LOL' (lachen).", "antwoord": True, "uitleg": "Waar. 'Mort de rire' betekent letterlijk 'dood van het lachen'."},
    {"type": "invul", "vraag": "Vul het juiste voorzetsel in voor een stad: <i>J'habite ... Paris.</i>", "antwoord": "à|a", "uitleg": "Voor een stad gebruik je altijd 'à' (bijv. à Paris, à Amsterdam)."},
    {"type": "mc", "vraag": "Hoe vraag je of iemand online is?", "opties": ["Tu es en ligne ?", "Tu es à l'école ?", "Tu dors déjà ?", "Tu as fini tes devoirs ?"], "antwoord": 0, "uitleg": "'Tu es en ligne ?' betekent 'Ben je online?'."},
    {"type": "waaronwaar", "vraag": "De vraag <i>'Tu viens d'où ?'</i> betekent 'Waar ga je naartoe?'.", "antwoord": False, "uitleg": "Onwaar. Het betekent 'Waar kom je vandaan?' (komen uit)."},
    {"type": "invul", "vraag": "Vul in: <i>Enchanté(e) ! (Aangenaam) ... de faire ta connaissance !</i>", "antwoord": "Ravi|Contente|Content|Heureux", "uitleg": "'Ravi de faire ta connaissance' betekent 'blij om kennis te maken'."},
    {"type": "mc", "vraag": "Wat betekent <b>'Envoyez-moi un message privé (DM)'</b>?", "opties": ["Stuur me een privébericht", "Bel direct de politie", "Deel dit openbaar", "Plaats een video"], "antwoord": 0, "uitleg": "'Un message privé' is een privébericht (DM)."}
  ]
}

# EXAMEN 4: Leesvaardigheid & Tekstbegrip
ex4 = {
  "id": "ex-h3-frans-4",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Toets 4 — Leesvaardigheid: Profielen, Vlogs & Online Berichten",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Lees het profiel: <i>'Salut ! Moi c'est Maxime, 15 ans. Passionné de skate et de photo. Suivez mes aventures sur Insta !'</i><br>Wat is de hobby van Maxime?", "opties": ["Skateboarden en fotografie", "Voetballen en gitaar spelen", "Koken en reizen", "Gamen en tekenen"], "antwoord": 0, "uitleg": "Maxime schrijft: 'Passionné de skate et de photo'."},
    {"type": "mc", "vraag": "Lees het bericht: <i>'Attention les amis ! Mon compte a été piraté hier soir. Ne cliquez pas sur les liens reçus.'</i><br>Waarom waarschuwt de schrijver zijn vrienden?", "opties": ["Zijn account is gisterenavond gehackt", "Hij stopt voor altijd met sociale media", "Hij heeft een nieuwe telefoon gekocht", "Zijn wifi-verbinding is verbroken"], "antwoord": 0, "uitleg": "'Piraté' betekent gehackt."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Je passe environ deux heures par jour sur TikTok'</i> brengt de persoon 5 uur per dag door op TikTok.", "antwoord": False, "uitleg": "Onwaar. 'Deux heures' betekent 2 uur per dag."},
    {"type": "invul", "vraag": "Lees de zin: <i>'Ce soir à 18h, je fais un live pour répondre à vos questions.'</i><br>Hoe laat begint de live-uitzending? (in cijfers)", "antwoord": "18|18:00|18h|18.00|zes uur|6 uur", "uitleg": "18h = 18:00 uur (zes uur 's avonds)."},
    {"type": "mc", "vraag": "Lees de reactie: <i>'Bravo pour ta nouvelle vidéo, le montage est magnifique et très drôle !'</i><br>Wat vindt de reageerder van de video?", "opties": ["De montage is prachtig en heel grappig", "De video is veel te lang en saai", "De muziek staat veel te hard", "Het beeld is onscherp"], "antwoord": 0, "uitleg": "'Magnifique et très drôle' betekent prachtig en heel grappig."},
    {"type": "waaronwaar", "vraag": "Als er staat: <i>'Cliquez sur le lien dans ma bio pour voir l'article'</i> moet je op een link in de biografie klikken.", "antwoord": True, "uitleg": "Waar. 'Le lien dans ma bio' is de bekende bio-link op Instagram/TikTok."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'hier'</b> in: <i>'J'ai posté une vidéo hier'</i>?", "antwoord": "gisteren", "uitleg": "'Hier' betekent 'gisteren'."},
    {"type": "mc", "vraag": "Lees het forumbericht: <i>'Les écrans avant de dormir empêchent de trouver le sommeil rapidement.'</i><br>Wat is de conclusie van dit bericht?", "opties": ["Schermen voor het slapen belemmeren het snel in slaap vallen", "Schermen helpen je om dieper te slapen", "Iedereen moet 's nachts gamen", "Telefoons moeten opgeladen worden in bed"], "antwoord": 0, "uitleg": "'Empêchent de trouver le sommeil' betekent dat het in slaap vallen bemoeilijkt wordt."},
    {"type": "mc", "vraag": "Wat betekent het signaalwoord <b>'d'abord'</b> in een stappenplan?", "opties": ["eerst / allereerst", "tenslotte", "nooit", "plotseling"], "antwoord": 0, "uitleg": "'D'abord' betekent 'allereerst / om te beginnen'."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'ensuite'</b> betekent 'daarna / vervolgens'.", "antwoord": True, "uitleg": "Waar. 'Ensuite' geeft de volgende stap aan in een chronologische volgorde."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'vandaag'</i> naar het Frans: <i>... c'est mon anniversaire.</i>", "antwoord": "Aujourd'hui|Aujourdhui", "uitleg": "'Aujourd'hui' betekent vandaag."},
    {"type": "mc", "vraag": "Lees de vacature: <i>'Recherche jeune community manager pour animer notre page Instagram. Passionné et créatif.'</i><br>Naar wie zijn ze op zoek?", "opties": ["Een creatieve jongere om de Instagram-pagina te beheren", "Een fotomodel voor een modeshow", "Een wiskundeleraar voor bijles", "Een bezorger voor een restaurant"], "antwoord": 0, "uitleg": "'Animer notre page Instagram' is het beheren van de pagina door een community manager."},
    {"type": "open", "vraag": "Lees: <i>'Pour protéger vos données personnelles, ne partagez jamais votre mot de passe ni votre adresse avec des inconnus.'</i><br>Welke twee dingen mag je volgens deze tekst nooit delen met onbekenden?", "sleutelwoorden": ["wachtwoord/mot de passe", "adres/woonplaats/locatie/adresse"], "minTreffers": 2, "modelantwoord": "Je mag nooit je wachtwoord en je adres delen met onbekenden.", "uitleg": "De tekst vermeldt duidelijk 'mot de passe' (wachtwoord) en 'adresse' (adres)."},
    {"type": "mc", "vraag": "Wat betekent de term <b>'les données personnelles'</b>?", "opties": ["persoonlijke gegevens / privacydata", "geheime spelcodes", "schoolresultaten", "telefoonrekeningen"], "antwoord": 0, "uitleg": "'Données personnelles' zijn persoonsgegevens."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Ce jeu est totalement gratuit pour tous les utilisateurs'</i> moet je betalen om het spel te spelen.", "antwoord": False, "uitleg": "Onwaar. 'Gratuit' betekent gratis."},
    {"type": "invul", "vraag": "Wat betekent <b>'souvent'</b> in: <i>'Je regarde souvent des vidéos sur YouTube'</i>?", "antwoord": "vaak|dikwijls", "uitleg": "'Souvent' betekent 'vaak'."},
    {"type": "mc", "vraag": "Lees de uitnodiging: <i>'Rendez-vous samedi à 15h devant le cinéma pour fêter la fin des examens.'</i><br>Waar en wanneer ontmoeten ze elkaar?", "opties": ["Zaterdag om 15:00 uur voor de bioscoop", "Zondag om 10:00 uur op school", "Vrijdag om 20:00 uur in een restaurant", "Maandag om 08:30 uur op het plein"], "antwoord": 0, "uitleg": "'Samedi à 15h devant le cinéma' = zaterdag om 15u voor de bioscoop."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'toujours'</b> betekent 'nooit'.", "antwoord": False, "uitleg": "Onwaar. 'Toujours' betekent 'altijd' (of 'nog steeds'). 'Nooit' is 'jamais'."},
    {"type": "invul", "vraag": "Vul het Franse woord in voor <i>soms</i>: <i>... je préfère lire un livre sans mon téléphone.</i>", "antwoord": "Parfois|Quelquefois", "uitleg": "'Parfois' of 'quelquefois' betekent soms."},
    {"type": "mc", "vraag": "Wat is het hoofddoel van een artikel met de titel: <i>'Comment limiter son temps d'écran facilement ?'</i>", "opties": ["Tips geven om schermtijd eenvoudig te verminderen", "Nieuwe smartphones verkopen", "Uitleggen hoe je een betere gamer wordt", "Waarschuwen voor dure internetabonnementen"], "antwoord": 0, "uitleg": "'Limiter son temps d'écran' betekent schermtijd beperken."}
  ]
}

# EXAMEN 5: Eindtoets / Sınav Simülasyonu Unité 1 (Mix van alle onderdelen)
ex5 = {
  "id": "ex-h3-frans-5",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Toets 5 — Unité 1 Eindtoets (Mix & Examentraining)",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'partager des photos'</b>?", "opties": ["foto's delen", "foto's afdrukken", "foto's wissen", "camera instellen"], "antwoord": 0, "uitleg": "'Partager' is delen."},
    {"type": "mc", "vraag": "Kies de juiste vorm van <b>être</b>: <i>Nous ... ravis de vous rencontrer.</i>", "opties": ["sommes", "êtes", "sont", "suis"], "antwoord": 0, "uitleg": "Nous sommes (wij zijn)."},
    {"type": "waaronwaar", "vraag": "In het Frans zeg je <i>'J'ai 14 ans'</i> en niet <i>'Je suis 14 ans'</i>.", "antwoord": True, "uitleg": "Waar. Leeftijd gaat met het werkwoord avoir."},
    {"type": "invul", "vraag": "Vervoeg <b>regarder</b> voor <i>ils</i>: <i>Ils ... une vidéo sur YouTube.</i>", "antwoord": "regardent", "uitleg": "Uitgang bij ils/elles is -ent: regardent."},
    {"type": "mc", "vraag": "Hoe maak je een correcte ontkenning van: <i>'Elle a un smartphone'</i>?", "opties": ["Elle n'a pas de smartphone.", "Elle a pas un smartphone.", "Elle ne a pas un smartphone.", "Elle pas a smartphone."], "antwoord": 0, "uitleg": "Ontkenning: n'a pas. Let op: na ontkenning wordt 'un/une' vaak 'de' (n'a pas de smartphone)."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'un mot de passe'</b> betekent 'een mobiel abonnement'.", "antwoord": False, "uitleg": "Onwaar. 'Mot de passe' betekent wachtwoord."},
    {"type": "invul", "vraag": "Vul aan: <i>Comment tu ... ? (Hoe heet je?)</i>", "antwoord": "t'appelles|tappelles", "uitleg": "Comment tu t'appelles ?"},
    {"type": "mc", "vraag": "Welke zin betekent: <i>'Zij wonen in Parijs'</i>?", "opties": ["Ils habitent à Paris.", "Ils habite à Paris.", "Ils habitons à Paris.", "Ils habitez à Paris."], "antwoord": 0, "uitleg": "Ils habitent (uitgang -ent) + à Paris."},
    {"type": "mc", "vraag": "Wat betekent <b>'MDR'</b> in Franse sms-taal?", "opties": ["Mort de rire (heel hard lachen)", "Merci beaucoup", "Mon Dieu regarde", "Mardi de retour"], "antwoord": 0, "uitleg": "'Mort de rire' is het Franse equivalent van LOL."},
    {"type": "waaronwaar", "vraag": "De uitgang van regelmatige -er werkwoorden bij <b>'tu'</b> is <b>-es</b>.", "antwoord": True, "uitleg": "Waar (bijv. tu écoutes, tu parles)."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>avoir</b>: <i>Tu ... combien d'abonnés sur ta chaîne ?</i>", "antwoord": "as", "uitleg": "Tu as (jij hebt)."},
    {"type": "mc", "vraag": "Wat betekent <b>'un internaute'</b>?", "opties": ["een internetgebruiker", "een computerwinkel", "een wifi-router", "een programmeur"], "antwoord": 0, "uitleg": "'Un internaute' is een internetter."},
    {"type": "open", "vraag": "Leg uit hoe je in het Frans een beleefde reactie geeft als iemand vraagt: <i>'Qu'est-ce que tu penses de mon nouveau profil ?'</i>", "sleutelwoorden": ["joli/beau/super/cool/magnifique", "avis/trouve/pense"], "minTreffers": 1, "modelantwoord": "Je peux dire : 'À mon avis, c'est super joli et très stylé !' (Naar mijn mening is het heel mooi en stijlvol).", "uitleg": "Geef een positief oordeel met 'À mon avis...' of 'Je trouve que...'."},
    {"type": "mc", "vraag": "Welk voorzetsel hoort bij een land in het meervoud (zoals <i>les États-Unis</i>)?", "opties": ["aux", "au", "en", "à"], "antwoord": 0, "uitleg": "Bij meervoudige landen gebruik je 'aux' (aux États-Unis, aux Pays-Bas)."},
    {"type": "waaronwaar", "vraag": "Het werkwoord <b>'supprimer'</b> betekent 'opslaan in de cloud'.", "antwoord": False, "uitleg": "Onwaar. 'Supprimer' betekent wissen of verwijderen."},
    {"type": "invul", "vraag": "Vul de ontkenning in voor <i>(habite)</i>: <i>Je ... à Marseille. (ik woon niet)</i>", "antwoord": "n'habite pas|nhabite pas", "uitleg": "Je n'habite pas."},
    {"type": "mc", "vraag": "Wat betekent het signaalwoord <b>'ensuite'</b> in een tekst?", "opties": ["vervolgens / daarna", "gisteren", "nooit meer", "ten onrechte"], "antwoord": 0, "uitleg": "'Ensuite' geeft de volgende stap aan."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'gratuit'</b> dat iets gratis is.", "antwoord": True, "uitleg": "Waar. Gratuit = gratis."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (vriendschap): <i>Notre ... est très précieuse.</i>", "antwoord": "amitié|amitie", "uitleg": "L'amitié = de vriendschap."},
    {"type": "mc", "vraag": "Kies de juiste vorm van <b>être</b>: <i>Elles ... très actives sur les réseaux sociaux.</i>", "opties": ["sont", "ont", "sommes", "êtes"], "antwoord": 0, "uitleg": "Elles sont (zij zijn)."}
  ]
}

write_examen("examen_1.js", ex1)
write_examen("examen_2.js", ex2)
write_examen("examen_3.js", ex3)
write_examen("examen_4.js", ex4)
write_examen("examen_5.js", ex5)
print("Frans Unité 1 exams (1 to 5) generated successfully!")
