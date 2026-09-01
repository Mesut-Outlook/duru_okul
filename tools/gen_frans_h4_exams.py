#!/usr/bin/env python3
"""
Generate Frans Unité 4 Proeftoetsen (5 exams x 20 questions = 100 questions)
Grandes Lignes 3 HAVO - Unité 4: Le pont (Cultuur, Francofonie & Tussenbalans)
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

# EXAMEN 16: Vocabulaire U4 (Parijs, Franse Regio's, Monumenten & Cultuur)
ex16 = {
  "id": "ex-h3-frans-16",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Unité 4 — Le pont",
  "titel": "Toets 1 — Vocabulaire: Parijs, Monumenten, Regio's & Franse Cultuur",
  "vak": "Frans · HAVO 3 (U4)",
  "icoon": "🗼",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat is <b>'la Seine'</b>?", "opties": ["de beroemde rivier die door Parijs stroomt", "een Franse bergketen in de Alpen", "een nationaal feest in juli", "het grootste plein van Frankrijk"], "antwoord": 0, "uitleg": "De Seine is de rivier die Parijs doorkruist."},
    {"type": "mc", "vraag": "Wat betekent het woord <b>'un chef-d'œuvre'</b>?", "opties": ["een meesterwerk (bijv. de Mona Lisa in het Louvre)", "een beroemde chef-kok", "een middeleeuws kasteel", "een toegangskaartje"], "antwoord": 0, "uitleg": "'Un chef-d'œuvre' is een meesterwerk in kunst of literatuur."},
    {"type": "waaronwaar", "vraag": "De Franse feestdag <b>'le 14 juillet'</b> viert de nationale feestdag van Frankrijk (Quatorze Juillet).", "antwoord": True, "uitleg": "Waar. 14 juli is de Franse nationale feestdag (herdenking van de bestorming van de Bastille)."},
    {"type": "invul", "vraag": "Vertaal het Franse woord voor <i>kasteel</i>: <i>Le ... de Versailles est magnifique.</i>", "antwoord": "château|chateau", "uitleg": "Un château = een kasteel."},
    {"type": "mc", "vraag": "Wat is <b>'la Francophonie'</b>?", "opties": ["het geheel van alle landen en mensen over de wereld die Frans spreken", "een speciale Franse muziekschool", "het Franse parlement in Parijs", "een Frans telefoonbedrijf"], "antwoord": 0, "uitleg": "La Francophonie omvat alle Franssprekende landen (zoals Frankrijk, België, Canada, Senegal, etc.)."},
    {"type": "waaronwaar", "vraag": "In het noordwesten van Frankrijk ligt de regio <b>la Bretagne</b>, bekend om haar ruige kust en pannenkoeken (crêpes).", "antwoord": True, "uitleg": "Waar. Bretagne staat bekend om haar kusten, menhirs en galettes/crêpes."},
    {"type": "invul", "vraag": "Vul de naam in van het beroemde schilderij van Da Vinci in het Louvre: <i>La ... (Mona Lisa)</i>.", "antwoord": "Joconde|joconde", "uitleg": "In het Frans heet de Mona Lisa 'La Joconde'."},
    {"type": "mc", "vraag": "Wat betekent <b>'un arrondissement'</b> in Parijs?", "opties": ["een stadswijk / stadsdistrict (Parijs heeft er 20)", "een metrolijn", "een toeristische bus", "een grote boulevard"], "antwoord": 0, "uitleg": "Parijs is opgedeeld in 20 genummerde arrondissementen."},
    {"type": "mc", "vraag": "Wat is <b>'un monument historique'</b>?", "opties": ["een historisch monument of erfgoedgebouw", "een oud geschiedenisboek", "een standbeeld van een koning", "een archeologisch museum"], "antwoord": 0, "uitleg": "Een beschermd historisch monument."},
    {"type": "waaronwaar", "vraag": "De regio <b>la Côte d'Azur</b> ligt in het uiterste noorden van Frankrijk aan de Noordzee.", "antwoord": False, "uitleg": "Onwaar. La Côte d'Azur ligt in het zonnige zuidoosten aan de Middellandse Zee (Franse Rivièra)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>hoofdstad</i> naar het Frans: <i>Paris est la ... de la France.</i>", "antwoord": "capitale", "uitleg": "'La capitale' = de hoofdstad."},
    {"type": "mc", "vraag": "Wat is <b>'le Mont-Saint-Michel'</b>?", "opties": ["een beroemd getijdeneiland met abdij in Normandië", "de hoogste bergtop van de Pyreneeën", "een skistation in de Alpen", "een kasteel in het zuiden van Frankrijk"], "antwoord": 0, "uitleg": "Le Mont-Saint-Michel is het iconische getijdeneiland in Normandië."},
    {"type": "open", "vraag": "Noem twee landen (buiten Frankrijk) waar Frans een officiële taal is.", "sleutelwoorden": ["belgië/belgique", "zwitserland/suisse", "canada/québec/quebec", "senegal/marokko/maroc/luxemburg/luxembourg"], "minTreffers": 2, "modelantwoord": "België (Belgique), Zwitserland (Suisse), Canada of Luxemburg.", "uitleg": "Landen van de Francofonie zijn o.a. België, Zwitserland, Canada, Luxemburg, Monaco, Senegal."},
    {"type": "mc", "vraag": "Wat betekent <b>'une coutume locale'</b>?", "opties": ["een lokale traditie of gewoonte", "een streekkostuum", "een lokale supermarkt", "een dialectwoord"], "antwoord": 0, "uitleg": "'Une coutume' is een gebruik / traditie."},
    {"type": "waaronwaar", "vraag": "De beroemde heuvel in Parijs waar de Sacré-Cœur staat en schilders werken heet <b>Montmartre</b>.", "antwoord": True, "uitleg": "Waar. Montmartre is de bekende kunstenaarswijk op de heuvel in Parijs."},
    {"type": "invul", "vraag": "Vertaal het woord <i>schilder / kunstenaar</i> naar het Frans: <i>Claude Monet est un célèbre ... impressionniste.</i>", "antwoord": "peintre|artiste", "uitleg": "'Un peintre' is een schilder."},
    {"type": "mc", "vraag": "Wat is <b>'la gastronomie française'</b>?", "opties": ["de Franse eetcultuur en kookkunst", "een Frans kooktijdschrift", "een sterrenrestaurant in Lyon", "een cursus voor bakkers"], "antwoord": 0, "uitleg": "'La gastronomie' is de verfijnde kookkunst en eetcultuur."},
    {"type": "waaronwaar", "vraag": "Het bekende museum met een glazen piramide in Parijs is <b>le Musée du Louvre</b>.", "antwoord": True, "uitleg": "Waar. De glazen piramide staat op de binnenplaats van het Louvre."},
    {"type": "invul", "vraag": "Vertaal het woord <i>strand</i> naar het Frans: <i>En été, les touristes vont à la ... .</i>", "antwoord": "plage", "uitleg": "'La plage' is het strand."},
    {"type": "mc", "vraag": "Wat betekent de term <b>'un habitant'</b>?", "opties": ["een inwoner / bewoner", "een kledingstuk", "een oud huis", "een gewoontedier"], "antwoord": 0, "uitleg": "'Un habitant' is een inwoner."}
  ]
}

# EXAMEN 17: Grammaire U4 (Grote herhaling Présent, Passé Composé & Bezittelijke voornaamwoorden)
ex17 = {
  "id": "ex-h3-frans-17",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Unité 4 — Le pont",
  "titel": "Toets 2 — Grammaire: Grote Herhaling Tijden & Bezittelijke Voornaamwoorden",
  "vak": "Frans · HAVO 3 (U4)",
  "icoon": "📝",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Welk bezittelijk voornaamwoord gebruik je voor <i>'onze'</i> bij een meervoudig woord (zoals <i>nos amis</i>)?", "opties": ["nos", "notre", "leur", "vos"], "antwoord": 0, "uitleg": "Notre vriend (enkelvoud), nos vrienden (meervoud)."},
    {"type": "mc", "vraag": "Kies de juiste combinatie voor <i>'zijn/haar'</i>: <i>Lucas parle avec ... mère et ... père.</i>", "opties": ["sa / son", "son / sa", "ses / son", "son / son"], "antwoord": 0, "uitleg": "Mère is vrouwelijk (sa mère), père is mannelijk (son père)."},
    {"type": "waaronwaar", "vraag": "Voor een vrouwelijk woord dat begint met een klinker (bijv. <i>amie</i>) gebruik je <b>mon / ton / son</b> in plaats van ma / ta / sa.", "antwoord": True, "uitleg": "Waar. Om twee klinkers achter elkaar te voorkomen zeg je 'mon amie' en 'son école'."},
    {"type": "invul", "vraag": "Vul het juiste bezittelijk voornaamwoord in (hun): <i>Les élèves ont oublié ... livres.</i>", "antwoord": "leurs", "uitleg": "Livres is meervoud, dus 'leurs livres' (hun boeken)."},
    {"type": "mc", "vraag": "Welke ontkenning betekent <i>'nooit'</i> in het Frans?", "opties": ["ne ... jamais", "ne ... pas", "ne ... rien", "ne ... plus"], "antwoord": 0, "uitleg": "'Ne...jamais' betekent 'nooit' (bijv. Je ne fume jamais)."},
    {"type": "waaronwaar", "vraag": "De ontkenning <b>'ne ... rien'</b> betekent 'niets' (bijv. <i>Je n'ai rien vu</i> = Ik heb niets gezien).", "antwoord": True, "uitleg": "Waar. 'Ne...rien' betekent 'niets'."},
    {"type": "invul", "vraag": "Vervoeg <b>pouvoir</b> (kunnen) voor <i>je</i>: <i>Je ... parler français.</i>", "antwoord": "peux", "uitleg": "Je peux, tu peux, il peut, nous pouvons, vous pouvez, ils peuvent."},
    {"type": "mc", "vraag": "Wat is de passé composé van <b>écrire</b> (schrijven)?", "opties": ["écrit", "écrivé", "écrivu", "écri"], "antwoord": 0, "uitleg": "Écrire -> écrit (j'ai écrit une lettre)."},
    {"type": "mc", "vraag": "Welke zin staat in de <b>futur composé</b>?", "opties": ["Nous allons visiter le musée d'Orsay.", "Nous avons visité le musée d'Orsay.", "Nous visitons le musée d'Orsay.", "Nous visitions le musée."], "antwoord": 0, "uitleg": "Aller (allons) + visiter (infinitif) = futur composé."},
    {"type": "waaronwaar", "vraag": "Het bezittelijk voornaamwoord <b>'leur'</b> krijgt een <b>-s</b> als het zelfstandig naamwoord erachter meervoud is (bijv. <i>leurs maisons</i>).", "antwoord": True, "uitleg": "Waar. Leur maison (enkelvoud) vs. leurs maisons (meervoud)."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>vouloir</b> (willen): <i>Nous ... réserver une chambre d'hôtel.</i>", "antwoord": "voulons", "uitleg": "Nous voulons."},
    {"type": "mc", "vraag": "Wat is de passé composé van <b>lire</b> (lezen)?", "opties": ["lu", "lisé", "liré", "lis"], "antwoord": 0, "uitleg": "Lire -> lu (j'ai lu un livre)."},
    {"type": "open", "vraag": "Leg uit waarom je in het Frans <i>'mon école'</i> zegt en niet <i>'ma école'</i>, hoewel 'école' een vrouwelijk woord is.", "sleutelwoorden": ["klinker/klinkers/vowel", "uitspraak/klank/botsen/klinkerbosting"], "minTreffers": 1, "modelantwoord": "Omdat 'école' begint met een klinker. Om klinkerbotsing te voorkomen verandert 'ma' in 'mon' (mon école).", "uitleg": "Vóór een klinker of stomme h gebruik je mon/ton/son om de uitspraak vloeiend te houden."},
    {"type": "mc", "vraag": "Kies de juiste vorm: <i>Tu as ... (begrijpen) l'explication du professeur ?</i>", "opties": ["compris", "comprené", "comprendu", "compri"], "antwoord": 0, "uitleg": "Comprendre -> compris (j'ai compris)."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Je ne sais rien'</i> betekent 'Ik weet het niet'.", "antwoord": False, "uitleg": "Onwaar. Het betekent 'Ik weet niets' (ne...rien = niets)."},
    {"type": "invul", "vraag": "Vul de juiste vorm in van <b>savoir</b> (weten): <i>Vous ... où se trouve la station de métro ?</i>", "antwoord": "savez", "uitleg": "Vous savez."},
    {"type": "mc", "vraag": "Welk woord vult de zin correct aan: <i>C'est ... (mijn) amie Juliette.</i>?", "opties": ["mon", "ma", "mes", "sa"], "antwoord": 0, "uitleg": "Mon amie (amie begint met een klinker)."},
    {"type": "waaronwaar", "vraag": "De ontkenning <b>'ne ... plus'</b> betekent 'niet meer' (bijv. <i>Je n'ai plus faim</i> = Ik heb geen honger meer).", "antwoord": True, "uitleg": "Waar. 'Ne...plus' betekent 'niet meer'."},
    {"type": "invul", "vraag": "Vul de ontkenning in voor <i>(nooit)</i>: <i>Elle ... voyage seule en avion. (zij reist nooit)</i>", "antwoord": "ne voyage jamais|n'a jamais voyagé", "uitleg": "Elle ne voyage jamais."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Hier, ils ... (avoir) un accident mais ils ... (aller) bien maintenant.</i>", "opties": ["ont eu / vont", "sont eu / vont", "ont eu / allent", "avaient / va"], "antwoord": 0, "uitleg": "Ils ont eu (passé composé) + ils vont (présent)."}
  ]
}

# EXAMEN 18: Stones & Communication U4 (Toeristische informatie, mening & cultuurervaring)
ex18 = {
  "id": "ex-h3-frans-18",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Unité 4 — Le pont",
  "titel": "Toets 3 — Communication: Toeristengids, Ervaringen vertellen & Cultuur",
  "vak": "Frans · HAVO 3 (U4)",
  "icoon": "🗺️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vraag je bij het Office de Tourisme om een stadsplattegrond?", "opties": ["Bonjour, avez-vous un plan de la ville, s'il vous plaît ?", "Où puis-je vendre ma carte ?", "La ville est-elle fermée aujourd'hui ?", "Donnez-moi toutes vos brochures gratuites."], "antwoord": 0, "uitleg": "'Avez-vous un plan de la ville ?' (Heeft u een plattegrond van de stad?)."},
    {"type": "mc", "vraag": "Wat vertel je als je wilt zeggen dat je vakantie geweldig was?", "opties": ["Mes vacances étaient vraiment inoubliables et superbes !", "J'ai détesté chaque seconde de mon séjour.", "Il a plu tous les jours sans arrêt.", "Je n'ai rien fait du tout."], "antwoord": 0, "uitleg": "'Inoubliables et superbes' betekent onvergetelijk en geweldig."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'Ça vaut le détour'</b> betekent dat een bezienswaardigheid zeker een omweg / bezoek waard is.", "antwoord": True, "uitleg": "Waar. 'Valoir le détour' = de moeite van het bezoeken waard zijn."},
    {"type": "invul", "vraag": "Vertaal het woord <i>toegangskaartje / entree</i> naar het Frans: <i>Quel est le prix du ... d'entrée ?</i>", "antwoord": "billet|ticket", "uitleg": "'Le billet d'entrée' (of ticket d'entrée) is het toegangskaartje."},
    {"type": "mc", "vraag": "Hoe vraag je of er korting is voor studenten / scholieren?", "opties": ["Est-ce qu'il y a un tarif réduit pour les étudiants / jeunes ?", "Pourquoi les jeunes doivent payer ?", "L'entrée est-elle interdite aux étudiants ?", "Puis-je entrer sans payer ?"], "antwoord": 0, "uitleg": "'Un tarif réduit' betekent een gereduceerd tarief / kortingstarief."},
    {"type": "waaronwaar", "vraag": "In Frankrijk is het gebruikelijk om in winkels bij binnenkomst <i>'Bonjour Madame / Bonjour Monsieur'</i> te zeggen.", "antwoord": True, "uitleg": "Waar. Beleefdheid en groeten is een essentieel onderdeel van de Franse cultuur."},
    {"type": "invul", "vraag": "Vul aan om te zeggen <i>'Ik raad aan'</i>: <i>Je vous ... de visiter le château le matin.</i>", "antwoord": "conseille|recommande", "uitleg": "'Conseiller' of 'recommander' = aanraden."},
    {"type": "mc", "vraag": "Wat vraag je als je wilt weten welke tentoonstelling er nu te zien is?", "opties": ["Quelle est l'exposition temporaire en ce moment ?", "Pourquoi ce musée a été construit ?", "Qui a nettoyé le musée hier ?", "Combien pèsent les tableaux ?"], "antwoord": 0, "uitleg": "'Une exposition' is een tentoonstelling."},
    {"type": "mc", "vraag": "Wat betekent de waarschuwing <b>'Interdit de prendre des photos avec flash'</b> in een museum?", "opties": ["Verboden te fotograferen met flitser", "Fotograferen is overal verplicht", "U moet uw camera afgeven", "Flitsers zijn gratis verkrijgbaar"], "antwoord": 0, "uitleg": "'Interdit de...' = verboden te..."},
    {"type": "waaronwaar", "vraag": "De vraag <i>'Qu'est-ce qu'il y a à visiter à Lyon ?'</i> vraagt wat er te bezichtigen valt in Lyon.", "antwoord": True, "uitleg": "Waar. 'Qu'est-ce qu'il y a à visiter' = wat valt er te bezoeken/bezichtigen."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (bezienswaardigheid): <i>La Tour Eiffel est une ... incontournable.</i>", "antwoord": "attraction|visite|curiosité|curiosite", "uitleg": "'Une attraction / curiosité touristique' is een bezienswaardigheid."},
    {"type": "mc", "vraag": "Hoe zeg je dat je een schilderij heel indrukwekkend vindt?", "opties": ["Ce tableau est vraiment impressionnant !", "Ce tableau est très ennuyeux.", "Je ne comprends rien à ce dessin.", "Effacez ce tableau rapidement."], "antwoord": 0, "uitleg": "'Impressionnant' betekent indrukwekkend."},
    {"type": "open", "vraag": "Schrijf een korte Franse aanbeveling waarin je een vriend adviseert om 's avonds de verlichte Eiffeltoren te gaan bekijken.", "sleutelwoorden": ["tour eiffel", "soir/illuminée/lumières/nuit", "conseille/magnifique/recommande/regarder/voir"], "minTreffers": 2, "modelantwoord": "Je te conseille d'aller voir la Tour Eiffel le soir, elle est magnifiquement illuminée !", "uitleg": "Adviseer met 'Je te conseille de voir la Tour Eiffel le soir...'."},
    {"type": "mc", "vraag": "Wat betekent <b>'un séjour linguistique'</b>?", "opties": ["een taalreis / taalverblijf in het buitenland om de taal te leren", "een woordenboek voor toeristen", "een taaltoets op school", "een tolkdienst op het vliegveld"], "antwoord": 0, "uitleg": "'Un séjour linguistique' is een taalreis."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'C'est fermé pour travaux'</b> betekent dat het gebouw open is voor feestelijke activiteiten.", "antwoord": False, "uitleg": "Onwaar. 'Fermé pour travaux' betekent gesloten wegens werkzaamheden / verbouwing."},
    {"type": "invul", "vraag": "Vul aan om te zeggen <i>'Volgens de gids'</i>: <i>... le guide touristique, ce monument date du 17e siècle.</i>", "antwoord": "Selon|D'après|D apres", "uitleg": "'Selon' of 'd'après' betekent volgens."},
    {"type": "mc", "vraag": "Hoe vraag je naar de sluitingstijd van het kasteel?", "opties": ["À quelle heure ferme le château ?", "Pourquoi le château a fermé ?", "Qui a ouvert les portes du château ?", "Quand le château a-t-il été détruit ?"], "antwoord": 0, "uitleg": "'À quelle heure ferme...' vraagt naar de sluitingstijd."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'gratuit pour les moins de 18 ans'</b> betekent dat jongeren onder de 18 jaar geen entree hoeven te betalen.", "antwoord": True, "uitleg": "Waar. Gratuit = gratis."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'souvenir'</i> naar het Frans: <i>J'ai acheté un petit ... de Paris.</i>", "antwoord": "souvenir", "uitleg": "Un souvenir."},
    {"type": "mc", "vraag": "Wat betekent de afsluitende opmerking: <b>'Je garde d'excellents souvenirs de mon voyage'</b>?", "opties": ["Ik bewaar uitstekende herinneringen aan mijn reis", "Ik heb al mijn geld uitgegeven aan souvenirs", "Ik ben mijn tas vergeten op reis", "Ik wil nooit meer terug naar Frankrijk"], "antwoord": 0, "uitleg": "'Garder d'excellents souvenirs' betekent fantastische herinneringen overhouden."}
  ]
}

# EXAMEN 19: Leesvaardigheid U4 (Cultuurartikelen, Reisverslagen & Bezienswaardigheden)
ex19 = {
  "id": "ex-h3-frans-19",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Unité 4 — Le pont",
  "titel": "Toets 4 — Leesvaardigheid: Cultuurgidsen, Monumenten & Francofonie",
  "vak": "Frans · HAVO 3 (U4)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Lees de gids: <i>'Le musée du Louvre accueille plus de 9 millions de visiteurs chaque année. Il abrite des milliers d'œuvres d'art, dont la célèbre Joconde.'</i><br>Hoeveel bezoekers ontvangt het Louvre jaarlijks?", "opties": ["Meer dan 9 miljoen bezoekers", "Precies 1 miljoen bezoekers", "Ongeveer 500.000 bezoekers", "Minder dan 2 miljoen bezoekers"], "antwoord": 0, "uitleg": "'Plus de 9 millions de visiteurs chaque année'."},
    {"type": "mc", "vraag": "Lees het verslag: <i>'Lors de notre voyage en Normandie, nous avons visité les plages du Débarquement et dégusté du délicieux fromage local.'</i><br>Wat heeft de reiziger in Normandië gedaan?", "opties": ["De landingsstranden bezocht en lokale kaas geproefd", "In de bergen geskied en fondue gegeten", "De Eiffeltoren beklommen", "Een surfcursus gevolgd aan de Middellandse Zee"], "antwoord": 0, "uitleg": "Normandië: plages du Débarquement en fromage local."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'L'accès au sommet de la Tour Eiffel est fermé en raison des vents violents'</i> is de top gesloten vanwege harde wind.", "antwoord": True, "uitleg": "Waar. 'Vents violents' = hevige wind."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'le sommet'</b> van een toren of berg?", "antwoord": "de top|top|bergtop|hoogste punt", "uitleg": "'Le sommet' is de top."},
    {"type": "mc", "vraag": "Lees de infobalie-instructie: <i>'Audioguides disponibles en français, anglais, espagnol et néerlandais au point d'accueil.'</i><br>In welke talen zijn er onder andere audiogidsen beschikbaar?", "opties": ["Ook in het Nederlands", "Alleen in het Frans", "Uitsluitend in het Chinees", "Niet beschikbaar"], "antwoord": 0, "uitleg": "'Néerlandais' is Nederlands."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'néerlandais'</b> betekent 'Noors'.", "antwoord": False, "uitleg": "Onwaar. 'Néerlandais' is Nederlands. Noors is 'norvégien'."},
    {"type": "invul", "vraag": "Lees: <i>'Visite guidée tous les samedis à 14h30.'</i><br>Om welk type rondleiding gaat het hier?", "antwoord": "rondleiding met gids|begeleide rondleiding|gids", "uitleg": "'Visite guidée' = rondleiding met een gids."},
    {"type": "mc", "vraag": "Wat is het advies in deze reisgids: <i>'Il est fortement conseillé de réserver vos billets en ligne plusieurs semaines à l'avance pour éviter les longues files d'attente.'</i>?", "opties": ["Boek je tickets ruim van tevoren online om lange wachtrijen te vermijden", "Koop kaartjes pas 5 minuten voor sluitingstijd bij het loket", "Bezoek het museum alleen als het regent", "Neem geen identiteitsbewijs mee"], "antwoord": 0, "uitleg": "'Réserver en ligne à l'avance' om wachtrijen te vermijden."},
    {"type": "mc", "vraag": "Wat betekent <b>'une file d'attente'</b>?", "opties": ["een wachtrij", "een ticketautomaat", "een kluisje", "een uitgang"], "antwoord": 0, "uitleg": "'Une file d'attente' is een wachtrij."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'situé au cœur de la ville'</b> betekent dat een monument in het centrum van de stad ligt.", "antwoord": True, "uitleg": "Waar. 'Au cœur de la ville' = in het hart / centrum van de stad."},
    {"type": "invul", "vraag": "Wat betekent het signaalwoord <b>'cependant'</b> in een leestekst?", "antwoord": "echter|toch|daarentegen", "uitleg": "'Cependant' betekent echter / desalniettemin."},
    {"type": "mc", "vraag": "Lees het artikel over Québec: <i>'Au Québec, province francophone du Canada, plus de 80% de la population a le français comme langue maternelle.'</i><br>Wat is de officiële moedertaal van meer dan 80% van de bevolking in Québec?", "opties": ["Frans", "Engels", "Spaans", "Duits"], "antwoord": 0, "uitleg": "In Québec spreekt meer dan 80% Frans als moedertaal."},
    {"type": "open", "vraag": "Lees: <i>'Les crêpes et le cidre sont les spécialités culinaires les plus réputées de la région Bretagne.'</i><br>Welke twee bekende streekspecialiteiten uit Bretagne worden hier genoemd?", "sleutelwoorden": ["crêpes/pannekoeken/pannenkoeken", "cidre/cider/appelwijn/appelsap"], "minTreffers": 2, "modelantwoord": "Crêpes (pannenkoeken) en cidre (cider).", "uitleg": "De tekst noemt 'les crêpes' en 'le cidre'."},
    {"type": "mc", "vraag": "Wat betekent het woord <b>'réputé'</b> in een culinaire tekst?", "opties": ["beroemd / hoog aangeschreven", "heel goedkoop", "verboden", "ongezond"], "antwoord": 0, "uitleg": "'Réputé' betekent bekend / gerenommeerd."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Le château a été construit au 16e siècle'</i> is het kasteel gebouwd in de 16e eeuw.", "antwoord": True, "uitleg": "Waar. 16e siècle = zestiende eeuw."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'le siècle'</b>?", "antwoord": "eeuw|de eeuw", "uitleg": "'Un siècle' is een eeuw (100 jaar)."},
    {"type": "mc", "vraag": "Lees het bord: <i>'Boutique de souvenirs et librairie ouvertes tous les jours de 10h à 19h.'</i><br>Tot hoe laat is de boekwinkel en souvenirshop geopend?", "opties": ["Tot 19:00 uur", "Tot 10:00 uur", "Tot middernacht", "Alleen 's ochtends"], "antwoord": 0, "uitleg": "19h = 19:00 uur (zeven uur 's avonds)."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'la librairie'</b> betekent 'de bibliotheek waar je gratis boeken leent'.", "antwoord": False, "uitleg": "Onwaar. 'Une librairie' is een boekwinkel (waar je boeken koopt). Een bibliotheek is 'une bibliothèque'."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'bibliotheek'</i> naar het Frans: <i>J'emprunte des livres à la ... .</i>", "antwoord": "bibliothèque|bibliotheque", "uitleg": "'La bibliothèque' = de bibliotheek."},
    {"type": "mc", "vraag": "Wat is het hoofddoel van een toeristische brochure met de titel: <i>'Découvrez les secrets insolites de Paris'</i>?", "opties": ["Bijzondere en onbekende plekjes in Parijs laten ontdekken", "Nieuwe metrolijnen aanleggen", "Waarschuwen voor hotels", "Geschiedenislessen geven over de Franse koningen"], "antwoord": 0, "uitleg": "'Insolite' betekent ongewoon / verrassend / buiten de gebaande paden."}
  ]
}

# EXAMEN 20: Eindtoets Unité 4 (Tussenbalans & Examentraining)
ex20 = {
  "id": "ex-h3-frans-20",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Unité 4 — Le pont",
  "titel": "Toets 5 — Unité 4 Tussenbalans & Examentraining (U1-U4 Mix)",
  "vak": "Frans · HAVO 3 (U4)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'la Francophonie'</b>?", "opties": ["alle Franssprekende landen en gebieden ter wereld", "de Franse nationale spoorwegen", "een Frans festival in Parijs", "een Frans woordenboek"], "antwoord": 0, "uitleg": "De gemeenschap van Franssprekende landen."},
    {"type": "mc", "vraag": "Kies het juiste bezittelijk voornaamwoord: <i>C'est ... (mijn) école.</i>", "opties": ["mon", "ma", "mes", "sa"], "antwoord": 0, "uitleg": "Mon école (école begint met een klinker)."},
    {"type": "waaronwaar", "vraag": "De ontkenning <b>'ne ... jamais'</b> betekent 'nooit'.", "antwoord": True, "uitleg": "Waar. Ne...jamais = nooit."},
    {"type": "invul", "vraag": "Vervoeg <b>pouvoir</b> voor <i>nous</i>: <i>Nous ... visiter le musée demain.</i>", "antwoord": "pouvons", "uitleg": "Nous pouvons."},
    {"type": "mc", "vraag": "Wat is het voltooid deelwoord van <b>écrire</b>?", "opties": ["écrit", "écrivé", "écri", "écrivu"], "antwoord": 0, "uitleg": "Écrire -> écrit."},
    {"type": "waaronwaar", "vraag": "In Frankrijk is <b>'une librairie'</b> een bibliotheek waar je gratis boeken kunt lenen.", "antwoord": False, "uitleg": "Onwaar. 'Librairie' is een boekhandel. Een bibliotheek is 'une bibliothèque'."},
    {"type": "invul", "vraag": "Vul het juiste bezittelijk voornaamwoord in (hun): <i>Ils aiment ... nouveau professeur.</i>", "antwoord": "leur", "uitleg": "Leur professeur (enkelvoud)."},
    {"type": "mc", "vraag": "Welke rivier stroomt door Parijs?", "opties": ["La Seine", "La Loire", "Le Rhône", "La Tamise"], "antwoord": 0, "uitleg": "De Seine."},
    {"type": "mc", "vraag": "Wat betekent <b>'un chef-d'œuvre'</b>?", "opties": ["een meesterwerk in de kunst", "een beroemde kok", "een koninklijk kasteel", "een toegangspas"], "antwoord": 0, "uitleg": "Un chef-d'œuvre = een meesterwerk."},
    {"type": "waaronwaar", "vraag": "De passé composé van <i>lire</i> (lezen) is <b>j'ai lu</b>.", "antwoord": True, "uitleg": "Waar. Lire -> lu."},
    {"type": "invul", "vraag": "Vul de ontkenning in voor <i>niets</i>: <i>Je n'ai ... compris à cet exercice.</i>", "antwoord": "rien", "uitleg": "Ne...rien = niets (n'ai rien compris)."},
    {"type": "mc", "vraag": "Hoe vraag je beleefd naar een stadsplattegrond?", "opties": ["Avez-vous un plan de la ville, s'il vous plaît ?", "Où est votre voiture ?", "Je veux un livre gratuit.", "Fermez la porte."], "antwoord": 0, "uitleg": "'Avez-vous un plan de la ville ?'."},
    {"type": "open", "vraag": "Leg uit wat het verschil is tussen <i>'notre maison'</i> en <i>'nos maisons'</i> in het Frans.", "sleutelwoorden": ["notre/ons/één huis/enkelvoud", "nos/onze/meerdere huizen/meervoud"], "minTreffers": 2, "modelantwoord": "'Notre maison' betekent 'ons huis' (enkelvoud), terwijl 'nos maisons' 'onze huizen' (meervoud) betekent.", "uitleg": "Notre = enkelvoud; nos = meervoud."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Hier, nous ... (bezoeken) le château et nous ... (zien) de magnifiques jardins.</i>", "opties": ["avons visité / avons vu", "sommes visité / sommes vu", "avons visité / voyons", "avions visité / voyions"], "antwoord": 0, "uitleg": "Nous avons visité + nous avons vu."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le siècle'</b> betekent een decennium (10 jaar).", "antwoord": False, "uitleg": "Onwaar. 'Un siècle' is een eeuw (100 jaar)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'hoofdstad'</i> naar het Frans: <i>Paris est la ... de la France.</i>", "antwoord": "capitale", "uitleg": "La capitale."},
    {"type": "mc", "vraag": "Wat betekent <b>'Ça vaut le détour'</b>?", "opties": ["Het is zeker de moeite waard om te bezoeken", "De weg is afgesloten voor verkeer", "Het is veel te duur", "Het duurt erg lang"], "antwoord": 0, "uitleg": "Valoir le détour = de moeite waard zijn."},
    {"type": "waaronwaar", "vraag": "De ontkenning <b>'ne ... plus'</b> betekent 'helemaal niet'.", "antwoord": False, "uitleg": "Onwaar. 'Ne...plus' betekent 'niet meer'."},
    {"type": "invul", "vraag": "Vervoeg <b>vouloir</b> bij <i>ils</i>: <i>Ils ... apprendre le français.</i>", "antwoord": "veulent", "uitleg": "Ils veulent (zij willen)."},
    {"type": "mc", "vraag": "Op welke datum valt de nationale feestdag van Frankrijk?", "opties": ["Le 14 juillet (14 juli)", "Le 1er janvier", "Le 25 décembre", "Le 5 mai"], "antwoord": 0, "uitleg": "14 juli (Quatorze Juillet)."}
  ]
}

write_examen("examen_16.js", ex16)
write_examen("examen_17.js", ex17)
write_examen("examen_18.js", ex18)
write_examen("examen_19.js", ex19)
write_examen("examen_20.js", ex20)
print("Frans Unité 4 exams (16 to 20) generated successfully!")
