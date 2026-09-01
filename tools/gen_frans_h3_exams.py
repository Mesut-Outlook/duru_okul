#!/usr/bin/env python3
"""
Generate Frans Unité 3 Proeftoetsen (5 exams x 20 questions = 100 questions)
Grandes Lignes 3 HAVO - Unité 3: En route!
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

# EXAMEN 11: Vocabulaire U3 (Reizen, Vervoer, Vakantie & Richtingen)
ex11 = {
  "id": "ex-h3-frans-11",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unité 3 — En route!",
  "titel": "Toets 1 — Vocabulaire: Reizen, Vervoer, Vakantie & Richtingen",
  "vak": "Frans · HAVO 3 (U3)",
  "icoon": "🚆",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'la gare'</b> in het Frans?", "opties": ["het treinstation", "de luchthaven", "de bushalte", "het benzinestation"], "antwoord": 0, "uitleg": "'La gare' is het treinstation."},
    {"type": "mc", "vraag": "Vertaal naar het Nederlands: <b>'prendre l'avion'</b>:", "opties": ["het vliegtuig nemen", "de trein nemen", "een auto huren", "fietsen"], "antwoord": 0, "uitleg": "'Prendre l'avion' betekent het vliegtuig nemen."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'un billet de train'</b> betekent een treinkaartje.", "antwoord": True, "uitleg": "Waar. 'Un billet' is een kaartje / ticket."},
    {"type": "invul", "vraag": "Vertaal het woord <i>koffer / bagage</i> naar het Frans: <i>Je prépare ma ... pour les vacances.</i>", "antwoord": "valise|bagage", "uitleg": "'La valise' is de koffer."},
    {"type": "mc", "vraag": "Wat betekent de richtingaanwijzing <b>'tout droit'</b>?", "opties": ["rechtdoor", "naar rechts", "naar links", "omkeren"], "antwoord": 0, "uitleg": "'Tout droit' betekent rechtdoor."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'tourner à gauche'</b> naar rechts afslaan.", "antwoord": False, "uitleg": "Onwaar. 'À gauche' is naar links. Naar rechts is 'à droite'."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>enkele reis</i>: <i>Un aller-... pour Paris, s'il vous plaît.</i>", "antwoord": "simple", "uitleg": "'Un aller simple' is een enkele reis. Een retour is 'un aller-retour'."},
    {"type": "mc", "vraag": "Wat is <b>'un aller-retour'</b>?", "opties": ["een retourticket (heen en terug)", "een enkele reis", "een dagkaart voor de metro", "een zitplaatsreservering"], "antwoord": 0, "uitleg": "'Un aller-retour' is een retourkaartje."},
    {"type": "mc", "vraag": "Wat betekent <b>'le quai'</b> op een Frans treinstation?", "opties": ["het perron / spoor", "de wachtruimte", "het loket", "de kaartjesautomaat"], "antwoord": 0, "uitleg": "'Le quai' is het perron (bijv. Voie 3, Quai B)."},
    {"type": "waaronwaar", "vraag": "Het werkwoord <b>'voyager'</b> betekent 'reizen'.", "antwoord": True, "uitleg": "Waar. 'Voyager' betekent reizen."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (fiets): <i>Aux Pays-Bas, on se déplace souvent à ... .</i>", "antwoord": "vélo|velo|bicyclette", "uitleg": "'À vélo' (of à bicyclette) = op de fiets."},
    {"type": "mc", "vraag": "Wat betekent <b>'rater le train'</b>?", "opties": ["de trein missen", "op tijd aankomen bij de trein", "een zitplaats reserveren", "in de verkeerde coupé stappen"], "antwoord": 0, "uitleg": "'Rater' betekent missen (rater le bus/train)."},
    {"type": "open", "vraag": "Leg uit wat het verschil is tussen <i>'un aller simple'</i> en <i>'un aller-retour'</i> bij het kopen van een treinkaartje.", "sleutelwoorden": ["enkele reis/heen", "retour/terug/heen en terug"], "minTreffers": 2, "modelantwoord": "Een 'aller simple' is alleen een heentreis (enkele reis), terwijl een 'aller-retour' een ticket is voor de heen- én terugreis (retour).", "uitleg": "Aller simple = enkele reis; aller-retour = retour."},
    {"type": "mc", "vraag": "Wat betekent <b>'la voie'</b> op het station?", "opties": ["het spoor (bijv. spoor 4)", "de stationsklok", "de uitgang", "de bagagekluis"], "antwoord": 0, "uitleg": "'La voie' is het spoornummer (Voie 1, Voie 2)."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le carrefour'</b> betekent 'het kruispunt'.", "antwoord": True, "uitleg": "Waar. 'Un carrefour' is een kruispunt."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>rotonde</i>: <i>Au ..., prenez la deuxième sortie.</i>", "antwoord": "rond-point|rondpoint", "uitleg": "'Le rond-point' is de rotonde."},
    {"type": "mc", "vraag": "Wat betekent <b>'loger dans un hôtel'</b>?", "opties": ["verblijven / overnachten in een hotel", "een hotel bouwen", "in een tent slapen", "een woning verkopen"], "antwoord": 0, "uitleg": "'Loger' betekent overnachten / logeren."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'en retard'</b> betekent 'te vroeg aankomen'.", "antwoord": False, "uitleg": "Onwaar. 'En retard' betekent te laat / vertraagd. Op tijd is 'à l'heure'."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'vliegtuig'</i> naar het Frans: <i>L'... décolle à 14h30.</i>", "antwoord": "avion", "uitleg": "'L'avion' is het vliegtuig."},
    {"type": "mc", "vraag": "Wat betekent <b>'composter son billet'</b> op Franse stations?", "opties": ["je treinkaartje afstempelen / valideren in een automaat", "je kaartje weggooien in de prullenbak", "een nieuw ticket betalen", "je paspoort laten controleren"], "antwoord": 0, "uitleg": "'Composter' is het verplicht afstempelen van een geel papieren treinkaartje in Frankrijk."}
  ]
}

# EXAMEN 12: Grammaire U3 (Passé Composé met avoir: regelmatige deelwoorden & ontkenning)
ex12 = {
  "id": "ex-h3-frans-12",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unité 3 — En route!",
  "titel": "Toets 2 — Grammaire: Passé Composé met Avoir (Deelwoorden & Ontkenning)",
  "vak": "Frans · HAVO 3 (U3)",
  "icoon": "⏱️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vorm je het voltooid deelwoord (participe passé) van regelmatige werkwoorden op <b>-er</b> (zoals <i>visiter</i>)?", "opties": ["stam + é (visité)", "stam + i (visiti)", "stam + u (visitu)", "stam + ait (visitait)"], "antwoord": 0, "uitleg": "Werkwoorden op -er krijgen een -é in de passé composé: parler -> parlé, visiter -> visité."},
    {"type": "mc", "vraag": "Wat is het voltooid deelwoord van regelmatige werkwoorden op <b>-ir</b> (zoals <i>finir</i>)?", "opties": ["fini", "finé", "finu", "finissant"], "antwoord": 0, "uitleg": "Deelwoord van -ir is -i: finir -> fini, choisir -> choisi."},
    {"type": "waaronwaar", "vraag": "De passé composé met avoir bestaat altijd uit twee delen: het hulpwerkwoord (avoir) + het voltooid deelwoord.", "antwoord": True, "uitleg": "Waar. Bijv: J'ai (hulpwerkwoord) + visité (voltooid deelwoord)."},
    {"type": "invul", "vraag": "Vul het voltooid deelwoord in van <b>regarder</b>: <i>Nous avons ... un documentaire sur Paris.</i>", "antwoord": "regardé|regarde", "uitleg": "Regarder -> regardé."},
    {"type": "mc", "vraag": "Wat is het voltooid deelwoord van <b>attendre</b> (regelmatig op -re)?", "opties": ["attendu", "attendé", "attendi", "attendant"], "antwoord": 0, "uitleg": "Werkwoorden op -re krijgen meestal -u: attendre -> attendu, vendre -> vendu."},
    {"type": "waaronwaar", "vraag": "Het voltooid deelwoord van <b>avoir</b> is <b>été</b>.", "antwoord": False, "uitleg": "Onwaar. Het deelwoord van avoir is 'eu' (gehad). 'Été' is het deelwoord van être (geweest)."},
    {"type": "invul", "vraag": "Vul de passé composé in voor <i>tu (visiter)</i>: <i>Tu ... le musée du Louvre ? (heb jij bezocht)</i>", "antwoord": "as visité|as visite", "uitleg": "Tu as visité."},
    {"type": "mc", "vraag": "Hoe maak je een zin in de passé composé ontkennend (bijv. <i>J'ai mangé</i>)?", "opties": ["Je n'ai pas mangé.", "J'ai ne mangé pas.", "J'ai mangé pas.", "Je pas ai mangé."], "antwoord": 0, "uitleg": "De ontkenning (ne...pas) staat om het hulpwerkwoord: n'ai pas mangé."},
    {"type": "mc", "vraag": "Wat is het voltooid deelwoord van <b>faire</b>?", "opties": ["fait", "faisé", "fai", "faisu"], "antwoord": 0, "uitleg": "Faire -> fait (j'ai fait)."},
    {"type": "waaronwaar", "vraag": "Het voltooid deelwoord van <b>prendre</b> is <b>pris</b>.", "antwoord": True, "uitleg": "Waar. Prendre -> pris (j'ai pris le train)."},
    {"type": "invul", "vraag": "Vul het voltooid deelwoord in van <b>choisir</b>: <i>Elle a ... une belle destination de vacances.</i>", "antwoord": "choisi", "uitleg": "Choisir -> choisi."},
    {"type": "mc", "vraag": "Kies de juiste vorm van de passé composé: <i>Hier, les touristes ... (acheter) des souvenirs.</i>", "opties": ["ont acheté", "sont acheté", "ont achetés", "avaient acheté"], "antwoord": 0, "uitleg": "Les touristes (ils) -> ont acheté."},
    {"type": "open", "vraag": "Vertaal de zin naar het Frans in de passé composé: <i>'Gisteren heb ik mijn trein gemist.'</i>", "sleutelwoorden": ["hier", "j'ai raté/j'ai manqué/perdu", "mon train/le train"], "minTreffers": 2, "modelantwoord": "Hier, j'ai raté mon train. (of: Hier, j'ai manqué mon train.)", "uitleg": "Hier = gisteren; j'ai raté = ik heb gemist; mon train = mijn trein."},
    {"type": "mc", "vraag": "Wat is de juiste vorm: <i>Vous ... (entendre) l'annonce à la gare ?</i>", "opties": ["avez entendu", "êtes entendu", "avez entendé", "avez entendus"], "antwoord": 0, "uitleg": "Vous avez entendu (entendre -> entendu)."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Ils n'ont pas fini leurs devoirs'</i> betekent 'Zij hebben hun huiswerk niet afgemaakt'.", "antwoord": True, "uitleg": "Waar. N'ont pas fini = hebben niet afgemaakt."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>avoir</b>: <i>Moi et mon ami, nous ... voyagé en Espagne.</i>", "antwoord": "avons", "uitleg": "Nous avons voyagé."},
    {"type": "mc", "vraag": "Wat is het voltooid deelwoord van <b>voir</b> (zien)?", "opties": ["vu", "voyé", "vis", "voire"], "antwoord": 0, "uitleg": "Voir -> vu (j'ai vu la Tour Eiffel)."},
    {"type": "waaronwaar", "vraag": "Het voltooid deelwoord van <b>boire</b> (drinken) is <b>bu</b>.", "antwoord": True, "uitleg": "Waar. Boire -> bu (j'ai bu un café)."},
    {"type": "invul", "vraag": "Vul het voltooid deelwoord in van <b>dormir</b>: <i>J'ai très bien ... à l'hôtel.</i>", "antwoord": "dormi", "uitleg": "Dormir -> dormi."},
    {"type": "mc", "vraag": "Welke zin is grammaticaal 100% correct in de passé composé?", "opties": ["Nous avons passé de très bonnes vacances en France.", "Nous sommes passé de très bonnes vacances.", "Nous avons passons de bonnes vacances.", "Nous ont passé de bonnes vacances."], "antwoord": 0, "uitleg": "'Passer des vacances' gaat met avoir: nous avons passé."},
  ]
}

# EXAMEN 13: Stones & Communication U3 (De weg vragen, treinkaartje kopen, op reis)
ex13 = {
  "id": "ex-h3-frans-13",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unité 3 — En route!",
  "titel": "Toets 3 — Communication: De weg vragen & wijzen, Kaartjes kopen & Op reis",
  "vak": "Frans · HAVO 3 (U3)",
  "icoon": "🗺️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vraag je beleefd naar de weg naar het station?", "opties": ["Pardon monsieur, pour aller à la gare, s'il vous plaît ?", "Où tu as mis la gare ?", "Pourquoi la gare est loin ?", "Combien pèse la gare ?"], "antwoord": 0, "uitleg": "'Pardon, pour aller à..., s'il vous plaît ?' is de standaard beleefde vraag."},
    {"type": "mc", "vraag": "Wat zeg je als je aan het loket een enkeltje naar Nice wilt kopen?", "opties": ["Je voudrais un aller simple pour Nice, s'il vous plaît.", "Donne-moi un train vers Nice maintenant.", "Combien coûte la ville de Nice ?", "Je vends mon billet de Nice."], "antwoord": 0, "uitleg": "'Je voudrais un aller simple pour...' (Ik wil graag een enkele reis naar...)."},
    {"type": "waaronwaar", "vraag": "De instructie <b>'Prenez la première rue à droite'</b> betekent 'Neem de eerste straat links'.", "antwoord": False, "uitleg": "Onwaar. 'À droite' is naar rechts."},
    {"type": "invul", "vraag": "Vul het ontbrekende woord in (rechtdoor): <i>Allez tout ... jusqu'au feu rouge.</i>", "antwoord": "droit", "uitleg": "'Tout droit' betekent rechtdoor."},
    {"type": "mc", "vraag": "Wat betekent: <b>'Le musée se trouve en face de la cathédrale'</b>?", "opties": ["Het museum bevindt zich tegenover de kathedraal", "Het museum is gesloten wegens verbouwing", "Het museum ligt achter het bos", "Het museum is ver weg van de kerk"], "antwoord": 0, "uitleg": "'En face de' betekent tegenover."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'C'est à cinq minutes à pied'</b> betekent dat het 5 minuten lopen is.", "antwoord": True, "uitleg": "Waar. 'À pied' = te voet / lopen."},
    {"type": "invul", "vraag": "Vul aan om te vragen naar het spoor: <i>Le train part de quelle ... ? (welk spoor)</i>", "antwoord": "voie|quai", "uitleg": "'Quelle voie' (of quel quai) = welk spoor."},
    {"type": "mc", "vraag": "Hoe vraag je naar de vertrektijd van de bus?", "opties": ["À quelle heure part le bus pour l'aéroport ?", "Pourquoi le bus est rouge ?", "Où dort le chauffeur du bus ?", "Combien de roues a le bus ?"], "antwoord": 0, "uitleg": "'À quelle heure part le bus...' vraagt naar de vertrektijd."},
    {"type": "mc", "vraag": "Wat betekent <b>'Est-ce que je dois changer de train ?'</b>?", "opties": ["Moet ik overstappen van trein?", "Moet ik mijn koffer betalen?", "Moet ik een ander shirt aandoen?", "Moet ik sneller rennen?"], "antwoord": 0, "uitleg": "'Changer de train' betekent overstappen."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'Bon voyage !'</b> betekent 'Goede reis!'.", "antwoord": True, "uitleg": "Waar. 'Bon voyage !' wenst iemand een goede reis."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (alsjeblieft/alstublieft formeel): <i>Un café, ... .</i>", "antwoord": "s'il vous plaît|sil vous plait|s'il vous plait", "uitleg": "S'il vous plaît."},
    {"type": "mc", "vraag": "Wat antwoordt een passant als je vraagt of het ver weg is en het blijkt heel dichtbij te zijn?", "opties": ["Non, c'est tout près d'ici !", "Oui, c'est à 50 kilomètres.", "Prenez un avion.", "Je ne sais pas où je suis."], "antwoord": 0, "uitleg": "'Tout près d'ici' betekent heel dichtbij hier."},
    {"type": "open", "vraag": "Schrijf een Franse dialoogzin waarin je aan de conducteur vraagt of deze trein rechtstreeks naar Parijs rijdt.", "sleutelwoorden": ["train", "direct/paris", "est-ce que/va"], "minTreffers": 1, "modelantwoord": "Excusez-moi, est-ce que ce train est direct pour Paris ?", "uitleg": "'Ce train est direct pour Paris ?' is een heldere en natuurlijke vraag."},
    {"type": "mc", "vraag": "Wat betekent <b>'Traversez la place'</b>?", "opties": ["Steek het plein over", "Parkeer op het plein", "Koop iets op het plein", "Blijf staan op het plein"], "antwoord": 0, "uitleg": "'Traverser' betekent oversteken."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'le feu rouge'</b> betekent het verkeerslicht / stoplicht.", "antwoord": True, "uitleg": "Waar. 'Le feu rouge' is het stoplicht."},
    {"type": "invul", "vraag": "Vul het voorzetsel in voor <i>naast</i>: <i>La boulangerie est ... de la pharmacie.</i>", "antwoord": "à côté|a cote", "uitleg": "'À côté de' betekent naast."},
    {"type": "mc", "vraag": "Hoe vraag je hoeveel een kaartje kost?", "opties": ["Combien coûte ce billet ?", "Quelle couleur a ce billet ?", "Quand est imprimé ce billet ?", "Où va ce billet ?"], "antwoord": 0, "uitleg": "'Combien coûte...' vraagt naar de prijs."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Le train a 15 minutes de retard'</i> betekent dat de trein 15 minuten te vroeg is.", "antwoord": False, "uitleg": "Onwaar. 'De retard' betekent vertraging."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>aankomst</i>: <i>Regarde le panneau des ... . (Arrivées / Départs)</i>", "antwoord": "arrivées|arrivees|arrivées", "uitleg": "Les arrivées = de aankomsten; les départs = de vertrekken."},
    {"type": "mc", "vraag": "Wat zeg je als je iemand bedankt voor de uitleg van de weg?", "opties": ["Merci beaucoup pour votre aide, bonne journée !", "Au revoir et payez-moi.", "Je ne vous crois pas.", "Vous marchez trop lentement."], "antwoord": 0, "uitleg": "'Merci beaucoup pour votre aide' is de beleefde dankzegging."}
  ]
}

# EXAMEN 14: Leesvaardigheid U3 (Dienstregelingen, Reisblogs & Reisadvertenties)
ex14 = {
  "id": "ex-h3-frans-14",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unité 3 — En route!",
  "titel": "Toets 4 — Leesvaardigheid: Dienstregelingen, Reisblogs & Reisadvertenties",
  "vak": "Frans · HAVO 3 (U3)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Lees het bord op het station: <i>'TGV 6612 destination Marseille - Départ 10h15 - Voie 4. Train complet.'</i><br>Wat betekent 'Train complet'?", "opties": ["De trein is helemaal volgeboekt / uitverkocht", "De trein is geannuleerd", "De trein stopt op elk tussenstation", "De trein heeft 10 minuten vertraging"], "antwoord": 0, "uitleg": "'Complet' betekent volzet / uitverkocht."},
    {"type": "mc", "vraag": "Lees de blogpost: <i>'Nous avons passé une semaine formidable dans un camping en Bretagne. La plage était à seulement 200 mètres de notre tente !'</i><br>Waar verbleef deze familie?", "opties": ["Op een camping in Bretagne dichtbij het strand", "In een luxe hotel in het centrum van Parijs", "In een berghut in de Alpen", "Op een cruiseschip op de Middellandse Zee"], "antwoord": 0, "uitleg": "'Camping en Bretagne' en 'la plage était à 200 mètres'."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Le vol AF 1234 est retardé en raison d'une grève'</i> heeft de vlucht vertraging vanwege een staking.", "antwoord": True, "uitleg": "Waar. 'Une grève' is een staking in het Frans."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'une grève'</b> in het Nederlands?", "antwoord": "staking|werkstaking", "uitleg": "'Une grève' betekent een staking."},
    {"type": "mc", "vraag": "Lees het hotelbordje: <i>'Le petit-déjeuner est servi de 7h00 à 10h30 dans la salle à manger au rez-de-chaussée.'</i><br>Waar en tot hoe laat kun je ontbijten?", "opties": ["Op de begane grond tot 10:30 uur", "Op de eerste verdieping tot 11:00 uur", "In je eigen kamer tot 09:00 uur", "Bij het zwembad de hele dag"], "antwoord": 0, "uitleg": "'Rez-de-chaussée' = begane grond; 'jusqu'à 10h30'."},
    {"type": "waaronwaar", "vraag": "Het Franse begrip <b>'le rez-de-chaussée'</b> betekent het dakappartement van een gebouw.", "antwoord": False, "uitleg": "Onwaar. 'Le rez-de-chaussée' is de begane grond."},
    {"type": "invul", "vraag": "Lees: <i>'Chambre double avec vue sur la mer.'</i><br>Welk uitzicht heeft deze tweepersoonskamer?", "antwoord": "zeezicht|uitzicht op zee|zee", "uitleg": "Vue sur la mer = uitzicht op zee."},
    {"type": "mc", "vraag": "Wat is het advies in dit reisbericht: <i>'Pensez à composter votre billet avant de monter dans le train pour éviter une amende.'</i>?", "opties": ["Vergeet niet je kaartje te ontwaarden om een boete te vermijden", "Koop drankjes in de restauratiewagon", "Houd je paspoort altijd in de hand", "Reis alleen met handbagage"], "antwoord": 0, "uitleg": "'Une amende' betekent een boete; 'composter votre billet' = afstempelen."},
    {"type": "mc", "vraag": "Wat betekent het Franse woord <b>'une amende'</b>?", "opties": ["een geldboete", "een kortingsbon", "een reischeque", "een bagagelabel"], "antwoord": 0, "uitleg": "'Une amende' is een boete."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'tous les quarts d'heure'</b> betekent 'elk kwartier (om de 15 minuten)'.", "antwoord": True, "uitleg": "Waar. Un quart d'heure = een kwartier."},
    {"type": "invul", "vraag": "Wat betekent het signaalwoord <b>'d'abord'</b> in een reisverslag?", "antwoord": "eerst|allereerst", "uitleg": "'D'abord' betekent eerst / om te beginnen."},
    {"type": "mc", "vraag": "Lees de aanbieding: <i>'Offre spéciale été : -30% sur les billets de TGV pour les jeunes de 12 à 25 ans avec la carte Avantage.'</i><br>Hoeveel korting krijgen jongeren met de kaart?", "opties": ["30% korting", "50% korting", "12% korting", "Gratis reizen"], "antwoord": 0, "uitleg": "-30% (dertig procent korting)."},
    {"type": "open", "vraag": "Lees: <i>'En cas de perte de vos bagages, veuillez vous présenter immédiatement au guichet des objets trouvés situé au terminal 2.'</i><br>Waar moet je naartoe als je je bagage kwijt bent?", "sleutelwoorden": ["loket/balie/guichet/bureau", "gevonden voorwerpen/objets trouvés", "terminal 2"], "minTreffers": 2, "modelantwoord": "Naar het loket voor gevonden voorwerpen (objets trouvés) in terminal 2.", "uitleg": "Guichet des objets trouvés in terminal 2."},
    {"type": "mc", "vraag": "Wat betekent <b>'les objets trouvés'</b>?", "opties": ["gevonden voorwerpen", "verloren paspoorten", "souvenirwinkels", "taxfree artikelen"], "antwoord": 0, "uitleg": "'Objets trouvés' zijn gevonden voorwerpen."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'La navette pour l'aéroport est gratuite pour tous les clients de l'hôtel'</i> is het pendelbusje gratis.", "antwoord": True, "uitleg": "Waar. 'La navette' is een pendelbus/shuttle en 'gratuite' betekent gratis."},
    {"type": "invul", "vraag": "Vertaal het woord <i>pendelbus / shuttle</i> naar het Frans: <i>Prenez la ... aéroport.</i>", "antwoord": "navette", "uitleg": "'La navette' is de pendelbus."},
    {"type": "mc", "vraag": "Wat betekent het bordje <b>'Accès interdit aux piétons'</b>?", "opties": ["Verboden toegang voor voetgangers", "Alleen voor fietsers", "Voetgangers oversteekplaats", "Parkeren verboden"], "antwoord": 0, "uitleg": "'Piétons' zijn voetgangers en 'accès interdit' is verboden toegang."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'départ immédiat'</b> op een stationsbord betekent dat de trein over 2 uur pas vertrekt.", "antwoord": False, "uitleg": "Onwaar. 'Immédiat' betekent onmiddellijk / nu direct."},
    {"type": "invul", "vraag": "Wat betekent het woord <b>'vers'</b> in: <i>'Le train roule vers le sud'</i>?", "antwoord": "naar|in de richting van|richting", "uitleg": "'Vers' betekent naar / in de richting van."},
    {"type": "mc", "vraag": "Wat is de hoofdgedachte van een artikel met de kop: <i>'Les meilleures destinations pour voyager en train en France'</i>?", "opties": ["De mooiste Franse reisbestemmingen die goed bereikbaar zijn met de trein", "Waarom vliegtickets goedkoper zijn dan treintickets", "Hoe je een treinstation ontwerpt", "Geschiedenis van de Franse stoomlocomotief"], "antwoord": 0, "uitleg": "Het artikel beveelt mooie treinbestemmingen aan in Frankrijk."}
  ]
}

# EXAMEN 15: Eindtoets Unité 3 (Mix & Examentraining)
ex15 = {
  "id": "ex-h3-frans-15",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unité 3 — En route!",
  "titel": "Toets 5 — Unité 3 Eindtoets (Mix & Examentraining)",
  "vak": "Frans · HAVO 3 (U3)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'un aller-retour'</b>?", "opties": ["een retourticket (heen en terug)", "een enkele reis", "een gereserveerde stoel", "een bagagetoeslag"], "antwoord": 0, "uitleg": "Retourkaartje."},
    {"type": "mc", "vraag": "Kies de juiste passé composé: <i>L'été dernier, nous ... (visiter) les châteaux de la Loire.</i>", "opties": ["avons visité", "sommes visité", "avez visité", "ont visité"], "antwoord": 0, "uitleg": "Nous avons visité (avoir + visité)."},
    {"type": "waaronwaar", "vraag": "De instructie <b>'Tournez à droite au carrefour'</b> betekent 'Sla linksaf op het kruispunt'.", "antwoord": False, "uitleg": "Onwaar. 'À droite' is rechtsaf."},
    {"type": "invul", "vraag": "Vul het voltooid deelwoord in van <b>faire</b>: <i>Qu'est-ce que tu as ... pendant les vacances ?</i>", "antwoord": "fait", "uitleg": "Faire -> fait (tu as fait)."},
    {"type": "mc", "vraag": "Hoe vraag je beleefd naar het treinstation?", "opties": ["Pardon, pour aller à la gare, s'il vous plaît ?", "Où est le cinéma ?", "Combien coûte le train ?", "Je veux un vélo."], "antwoord": 0, "uitleg": "'Pour aller à la gare, s'il vous plaît ?'."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'la voie'</b> op het station betekent 'het spoor'.", "antwoord": True, "uitleg": "Waar. Voie 1 = Spoor 1."},
    {"type": "invul", "vraag": "Maak de ontkenning in de passé composé: <i>Je ... (regarder / niet) la télévision hier soir.</i>", "antwoord": "n'ai pas regardé|n'ai pas regarde|nai pas regarde", "uitleg": "Je n'ai pas regardé."},
    {"type": "mc", "vraag": "Wat is het voltooid deelwoord van <b>prendre</b>?", "opties": ["pris", "prendu", "prendé", "prenant"], "antwoord": 0, "uitleg": "Prendre -> pris (j'ai pris le bus)."},
    {"type": "mc", "vraag": "Wat betekent <b>'tout droit'</b>?", "opties": ["rechtdoor", "naar rechts", "naar links", "terug"], "antwoord": 0, "uitleg": "'Tout droit' is rechtdoor."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'une valise'</b> betekent een rugzak.", "antwoord": False, "uitleg": "Onwaar. 'Une valise' is een koffer. Een rugzak is 'un sac à dos'."},
    {"type": "invul", "vraag": "Vul het voltooid deelwoord in van <b>finir</b>: <i>Ils ont ... leur voyage à Nice.</i>", "antwoord": "fini", "uitleg": "Finir -> fini."},
    {"type": "mc", "vraag": "Wat betekent de term <b>'une grève'</b> in het nieuws over het openbaar vervoer?", "opties": ["een staking", "een kortingsactie", "een nieuw treinspoor", "een feestdag"], "antwoord": 0, "uitleg": "Une grève = een staking."},
    {"type": "open", "vraag": "Leg in het Nederlands uit hoe je in Frankrijk aan een loket vraagt: <i>'Mag ik twee retourtjes naar Parijs in de tweede klas?'</i>", "sleutelwoorden": ["deux/2", "aller-retour/allers-retours", "paris", "deuxième/seconde/classe"], "minTreffers": 2, "modelantwoord": "'Je voudrais deux allers-retours pour Paris en deuxième classe, s'il vous plaît.'", "uitleg": "Deux allers-retours pour Paris en deuxième classe, s'il vous plaît."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Hier, elle ... (avoir) peur mais elle ... (prendre) l'avion.</i>", "opties": ["a eu / a pris", "est eu / est pris", "a eu / a prendu", "avait / prend"], "antwoord": 0, "uitleg": "Elle a eu (avoir -> eu) + elle a pris (prendre -> pris)."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le rond-point'</b> betekent de rotonde.", "antwoord": True, "uitleg": "Waar. Le rond-point = de rotonde."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>te voet</i>: <i>Le camping est à dix minutes à ... de la mer.</i>", "antwoord": "pied", "uitleg": "À pied = te voet / lopen."},
    {"type": "mc", "vraag": "Wat betekent <b>'rater sa correspondance'</b>?", "opties": ["je overstap missen", "je brief kwijtraken", "een verkeerde reservering maken", "te vroeg vertrekken"], "antwoord": 0, "uitleg": "'La correspondance' is de overstap (trein/vlucht)."},
    {"type": "waaronwaar", "vraag": "Het voltooid deelwoord van <b>voir</b> (zien) is <b>vu</b>.", "antwoord": True, "uitleg": "Waar. J'ai vu = ik heb gezien."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (enkele reis): <i>Un aller-... pour Lyon, s'il vous plaît.</i>", "antwoord": "simple", "uitleg": "Un aller simple."},
    {"type": "mc", "vraag": "Welke vorm van <b>avoir</b> hoort bij <i>ils</i> in de passé composé?", "opties": ["ont", "sont", "avons", "avez"], "antwoord": 0, "uitleg": "Ils ont + voltooid deelwoord (bijv. ils ont voyagé)."}
  ]
}

write_examen("examen_11.js", ex11)
write_examen("examen_12.js", ex12)
write_examen("examen_13.js", ex13)
write_examen("examen_14.js", ex14)
write_examen("examen_15.js", ex15)
print("Frans Unité 3 exams (11 to 15) generated successfully!")
