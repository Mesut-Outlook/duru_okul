#!/usr/bin/env python3
import os
import json

BASE_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/engels"
DATA_DIR = os.path.join(BASE_DIR, "js/data")
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
   Stepping Stones 3 HAVO Hoofdstuk {data['hoofdstuk']} */
DURU.registerExamen({json.dumps(data, indent=2, ensure_ascii=False)});
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [✓] Examen saved: {filename}")

# EXAMEN 16: H4 Theme Words (Extreme Sports & Survival) (20 questions)
ex16 = {
  "id": "ex-h3-eng-16",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Hoofdstuk 4 — To the extreme",
  "titel": "Toets 1 — Theme Words: Extreme Sports & Survival",
  "vak": "Engels · HAVO 3 (H4)",
  "icoon": "⚡",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "How is a mountain <b>avalanche</b> accurately described?", "opties": ["A large mass of snow, ice, and rock falling rapidly down a mountainside", "A sudden heavy thunderstorm in a tropical jungle", "A high-speed speedboat race on a calm lake", "A hot volcanic lava eruption in Hawaii"], "antwoord": 0, "uitleg": "An avalanche is een lawine."},
    {"type": "mc", "vraag": "What does physical <b>endurance</b> mean?", "opties": ["The ability to withstand difficult, prolonged effort or pain without giving up", "The speed at which you can type on a smartphone keyboard", "The balance needed to stand on one foot for ten seconds", "The warmth provided by a winter woolen scarf"], "antwoord": 0, "uitleg": "Endurance is uithoudingsvermogen."},
    {"type": "waaronwaar", "vraag": "<b>Dehydration</b> is a serious condition caused by losing too much body water without drinking enough fluids.", "antwoord": True, "uitleg": "Waar. Dehydration is uitdroging door vochtgebrek."},
    {"type": "invul", "vraag": "Fill in the English word for <i>sneeuwstorm</i>: <i>Hikers took shelter in a cave during the freezing ... .</i>", "antwoord": "blizzard|snowstorm", "uitleg": "Blizzard is een zware sneeuwstorm."},
    {"type": "mc", "vraag": "Which definition describes someone who is completely <b>fearless</b>?", "opties": ["Showing no fear, extremely brave and bold", "Being constantly terrified of insects", "Walking with hiking sticks", "Refusing to wear safety helmets"], "antwoord": 0, "uitleg": "Fearless betekent onverschrokken en dapper."},
    {"type": "waaronwaar", "vraag": "The word <b>wilderness</b> refers to a busy shopping street in central London.", "antwoord": False, "uitleg": "Onwaar. Wilderness is ongerepte woeste natuur."},
    {"type": "invul", "vraag": "Fill in the noun (uitrusting): <i>Make sure all your climbing ... is checked for safety.</i>", "antwoord": "equipment|gear", "uitleg": "Equipment / gear is uitrusting."},
    {"type": "mc", "vraag": "What is an <b>adrenaline rush</b>?", "opties": ["A sudden surge of energy and excitement produced by the body in stressful or thrilling situations", "A sudden feeling of deep tiredness after eating lunch", "A headache caused by loud music", "A cold shower after intense exercise"], "antwoord": 0, "uitleg": "Een adrenalinestoot bij spanning of gevaar."},
    {"type": "mc", "vraag": "What is the meaning of <b>altitude</b> in mountaineering?", "opties": ["The height of an object or point in relation to sea level", "The weight of a climber's backpack in kilograms", "The thickness of climbing ropes", "The temperature inside a mountain tent"], "antwoord": 0, "uitleg": "Altitude is de hoogte boven zeeniveau."},
    {"type": "waaronwaar", "vraag": "A <b>rescue team</b> is a specialized group trained to locate and save people in dangerous outdoor emergencies.", "antwoord": True, "uitleg": "Waar. Een reddingsteam redt mensen in nood."},
    {"type": "invul", "vraag": "Fill in the noun (overwinning / triomf): <i>Reaching the summit after four days was a great personal ... for the team.</i>", "antwoord": "triumph|victory|achievement", "uitleg": "Triumph / victory is een triomf of overwinning."},
    {"type": "mc", "vraag": "What is a major physical <b>obstacle</b> during an obstacle run?", "opties": ["A challenging physical barrier like a high wall, mud pit, or rope climb", "A gentle grassy hill in a city park", "A bottle of cold sports drink", "A pair of clean white socks"], "antwoord": 0, "uitleg": "Een obstakel is een zware hindernis."},
    {"type": "open", "vraag": "Why is proper thermal clothing essential for mountaineers attempting to survive high-altitude blizzards?", "sleutelwoorden": ["warmth/temperature/body/protect", "hypothermia/frostbite/freezing/cold"], "minTreffers": 1, "modelantwoord": "Thermal clothing keeps body heat in and prevents dangerous hypothermia and frostbite in freezing weather.", "uitleg": "Thermokleding houdt lichaamswarmte vast en voorkomt onderkoeling en bevriezing."},
    {"type": "mc", "vraag": "What does <b>courage</b> mean?", "opties": ["The mental or moral strength to face danger, fear, or difficulty", "The ability to run fast in sneakers", "The habit of staying indoors when it rains", "The skill of repairing broken bicycles"], "antwoord": 0, "uitleg": "Courage is moed en dapperheid."},
    {"type": "waaronwaar", "vraag": "Extreme sports athletes never wear protective gear because helmets reduce the adrenaline rush.", "antwoord": False, "uitleg": "Onwaar. Professionele atleten gebruiken geavanceerde veiligheidsuitrusting."},
    {"type": "invul", "vraag": "Fill in the noun (uithoudingsvermogen / energie): <i>Elite athletes build tremendous ... through daily endurance training.</i>", "antwoord": "stamina|endurance", "uitleg": "Stamina / endurance is uithoudingsvermogen."},
    {"type": "mc", "vraag": "Which sport involves jumping from an aircraft and free-falling before opening a parachute?", "opties": ["Skydiving", "Bouldering", "White-water rafting", "Cross-country skiing"], "antwoord": 0, "uitleg": "Skydiving is parachutespringen."},
    {"type": "waaronwaar", "vraag": "Oxygen levels are significantly lower at high altitudes above 6,000 meters.", "antwoord": True, "uitleg": "Waar. Op grote hoogte is de luchtdruk en zuurstofconcentratie lager."},
    {"type": "invul", "vraag": "Fill in the missing adjective (ongerept / wild): <i>They spent two weeks exploring the Alaskan ... .</i>", "antwoord": "wilderness", "uitleg": "Wilderness (wildernis)."},
    {"type": "mc", "vraag": "What is an <b>expedition</b>?", "opties": ["An organized journey undertaken by a group with a specific purpose, such as exploration or scientific research", "A quick trip to the local supermarket", "A five-minute warm-up exercise before running", "A casual conversation on the phone"], "antwoord": 0, "uitleg": "Een expeditie is een georganiseerde ontdekkingsreis."}
  ]
}

# EXAMEN 17: H4 Grammar (Comparatives & Modals) (20 questions)
ex17 = {
  "id": "ex-h3-eng-17",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Hoofdstuk 4 — To the extreme",
  "titel": "Toets 2 — Grammar: Comparatives, Superlatives & Modals",
  "vak": "Engels · HAVO 3 (H4)",
  "icoon": "🏔️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Choose the correct comparative form: <i>Climbing in winter is ... (risky) than in summer.</i>", "opties": ["riskier", "more risky", "riskiest", "as risky"], "antwoord": 0, "uitleg": "Woorden op -y krijgen -ier: riskier than."},
    {"type": "mc", "vraag": "What is the irregular comparative and superlative of <b>far</b>?", "opties": ["Farther / Further - The farthest / furthest", "Farer - The farest", "More far - The most far", "Furtherer - The furtherest"], "antwoord": 0, "uitleg": "Far -> further / farther -> the furthest / farthest."},
    {"type": "waaronwaar", "vraag": "The modal verb <b>mustn't</b> is used to give friendly advice rather than expressing a strict prohibition.", "antwoord": False, "uitleg": "Onwaar. 'Mustn't' drukt een strikt verbod uit (mag absoluut niet). Voor advies gebruik je 'shouldn't'."},
    {"type": "invul", "vraag": "Fill in the superlative of <i>(high)</i>: <i>Mount Everest is the ... mountain in the world.</i>", "antwoord": "highest", "uitleg": "High -> higher -> the highest."},
    {"type": "mc", "vraag": "Which modal verb is used to convey a strict personal obligation or urgent necessity?", "opties": ["Must / Have to", "Might", "Could", "May"], "antwoord": 0, "uitleg": "Must / have to geeft een sterke verplichting of noodzaak aan."},
    {"type": "waaronwaar", "vraag": "The comparative form of <i>dangerous</i> is <i>more dangerous</i> because it has three syllables.", "antwoord": True, "uitleg": "Waar. Bij lange bijvoeglijke naamwoorden gebruik je 'more'."},
    {"type": "invul", "vraag": "Fill in the comparative of <i>(bad)</i>: <i>The blizzard was even ... than the weather forecast predicted.</i>", "antwoord": "worse", "uitleg": "De onregelmatige vergrotende trap van bad is worse."},
    {"type": "mc", "vraag": "Choose the correct equality sentence:", "opties": ["Rock climbing is not as dangerous as base jumping.", "Rock climbing is not as dangerous than base jumping.", "Rock climbing is not so more dangerous as base jumping.", "Rock climbing is not as danger as base jumping."], "antwoord": 0, "uitleg": "Gelijkheid / ongelijkheid: (not) as ... as."},
    {"type": "mc", "vraag": "Why is <i>'You should to wear a helmet'</i> grammatically incorrect?", "opties": ["Modal verbs like should must be followed directly by the bare infinitive without 'to'", "Should cannot be used for safety gear", "Helmet requires a plural ending", "Wear must be in the past tense"], "antwoord": 0, "uitleg": "Na modale hulpwerkwoorden (should, can, must) komt het hele werkwoord ZONDER to."},
    {"type": "waaronwaar", "vraag": "The sentence <i>'You don't have to pay'</i> means paying is strictly forbidden by law.", "antwoord": False, "uitleg": "Onwaar. 'Don't have to' betekent dat het niet hoeft (geen verplichting), niet dat het verboden is."},
    {"type": "invul", "vraag": "Fill in the superlative of <i>(good)</i>: <i>This is the ... climbing gear I have ever used.</i>", "antwoord": "best", "uitleg": "Good -> better -> the best."},
    {"type": "mc", "vraag": "Choose the correct sentence for advice:", "opties": ["You should drink plenty of water to prevent dehydration.", "You must to drink water.", "You ought drink water.", "You shouldn't drink any fluids."], "antwoord": 0, "uitleg": "'You should drink' is correct advies."},
    {"type": "open", "vraag": "Explain the clear distinction between telling someone that an action is forbidden versus stating that it is not required.", "sleutelwoorden": ["prohibited/illegal/not allowed/banned", "unnecessary/optional/choice/freedom"], "minTreffers": 1, "modelantwoord": "'Must not' is a strict prohibition (forbidden), while 'don't have to' means there is no obligation (it is optional).", "uitleg": "Must not is een verbod; don't have to betekent dat het niet verplicht is."},
    {"type": "mc", "vraag": "Choose the correct form: <i>This canyon is ... (deep) than the Grand Canyon.</i>", "opties": ["deeper", "more deep", "deepest", "as deep"], "antwoord": 0, "uitleg": "Deep (1 lettergreep) -> deeper."},
    {"type": "waaronwaar", "vraag": "The superlative of <i>exciting</i> is <i>the most exciting</i>.", "antwoord": True, "uitleg": "Waar. Exciting -> more exciting -> the most exciting."},
    {"type": "invul", "vraag": "Fill in the modal verb (verbod): <i>You ... touch the emergency flares unless there is a real crisis.</i>", "antwoord": "must not|mustn't", "uitleg": "Must not / mustn't (verbod)."},
    {"type": "mc", "vraag": "Which sentence expresses ability in the past?", "opties": ["He could climb steep icy cliffs even when he was a teenager.", "He can climb cliffs right now.", "He will can climb cliffs tomorrow.", "He is climbing cliffs."], "antwoord": 0, "uitleg": "'Could' drukt bekwaamheid in het verleden uit."},
    {"type": "waaronwaar", "vraag": "In English, two-syllable adjectives ending in -y (like <i>heavy</i>) form their comparative with <i>more heavy</i>.", "antwoord": False, "uitleg": "Onwaar. Woorden op -y veranderen in -ier (heavier)."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>Skiing is as thrilling ... snowboarding.</i>", "antwoord": "as", "uitleg": "As ... as (even ... als)."},
    {"type": "mc", "vraag": "Which superlative form correctly describes the fastest runner?", "opties": ["He is the fastest runner on our cross-country team.", "He is the most fast runner.", "He is the faster runner of all.", "He is fast than everybody."], "antwoord": 0, "uitleg": "The fastest (overtreffende trap van fast)."}
  ]
}

# EXAMEN 18: H4 Stones & Safety Warnings (20 questions)
ex18 = {
  "id": "ex-h3-eng-18",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Hoofdstuk 4 — To the extreme",
  "titel": "Toets 3 — Stones & Skills: Safety Warnings & Encouragement",
  "vak": "Engels · HAVO 3 (H4)",
  "icoon": "⚠️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Which phrase is used to shout an immediate, urgent warning on a slippery rock ledge?", "opties": ["Watch out! / Look out!", "Excuse me, what time is it?", "How lovely the view is!", "Please take my picture."], "antwoord": 0, "uitleg": "'Watch out!' of 'Look out!' waarschuwt acuut voor direct gevaar."},
    {"type": "mc", "vraag": "How do you give strong advice to prevent a fatal mistake?", "opties": ["Whatever you do, don't unclip your safety harness.", "Maybe you could unclip if you feel like it.", "It would be funny to unclip.", "Unclipping is very fashionable."], "antwoord": 0, "uitleg": "'Whatever you do, don't...' legt maximale nadruk op wat men moet vermijden."},
    {"type": "waaronwaar", "vraag": "The phrase <i>'Keep going, you've got this!'</i> is used to encourage someone facing a tough challenge.", "antwoord": True, "uitleg": "Waar. Dit is een veelgebruikte aanmoediging."},
    {"type": "invul", "vraag": "Complete the warning: <i>Be ... not to step on loose rocks near the edge!</i>", "antwoord": "careful", "uitleg": "'Be careful' (wees voorzichtig)."},
    {"type": "mc", "vraag": "How do you reassure someone who is nervous before their first tandem parachute jump?", "opties": ["Take deep breaths, stay calm, and trust your certified instructor.", "You will probably crash into the forest.", "I have never seen such a terrifying plane.", "Jump without listening to the guide."], "antwoord": 0, "uitleg": "Rustig blijven ademen en vertrouwen op de instructeur stelt gerust."},
    {"type": "waaronwaar", "vraag": "In safety rules, imperative verbs like <i>'Always wear your helmet'</i> are polite but authoritative.", "antwoord": True, "uitleg": "Waar. De gebiedende wijs geeft duidelijke veiligheidsinstructies."},
    {"type": "invul", "vraag": "Complete the phrase: <i>Make ... you drink enough water during the trek.</i>", "antwoord": "sure|certain", "uitleg": "'Make sure' (zorg ervoor dat)."},
    {"type": "mc", "vraag": "Which expression shows personal determination and excitement before a race?", "opties": ["I'm ready for this challenge! Let's do it!", "I want to sleep all day.", "Why did my alarm ring?", "I dislike running in sneakers."], "antwoord": 0, "uitleg": "Toont vastberadenheid en enthousiasme."},
    {"type": "mc", "vraag": "What is the standard emergency signal when lost in the wilderness?", "opties": ["Three blasts on a whistle or three flashes of light at regular intervals", "Singing pop songs loudly", "Waving a single leaf once", "Building five sandcastles"], "antwoord": 0, "uitleg": "Het universele noodsignaal is drie opeenvolgende signalen (fluit of licht)."},
    {"type": "waaronwaar", "vraag": "The phrase <i>'Don't give up now'</i> tells someone to abandon their climb immediately.", "antwoord": False, "uitleg": "Onwaar. Het betekent juist 'geef nu niet op!' (volhouden)."},
    {"type": "invul", "vraag": "Complete the encouraging phrase: <i>You are ... at the summit! Just ten more meters!</i>", "antwoord": "almost|nearly", "uitleg": "'Almost / nearly at the summit'."},
    {"type": "mc", "vraag": "How do you express fear in a terrifying situation?", "opties": ["My heart was pounding and I was terrified of falling.", "I was thinking about eating pancakes.", "I found the rocks very colorful.", "I checked my watch twice."], "antwoord": 0, "uitleg": "'My heart was pounding' drukt spanning en angst uit."},
    {"type": "open", "vraag": "Write three essential safety rules for hikers walking on high mountain trails.", "sleutelwoorden": ["marked/stay/follow/path", "water/hydration/thermal/gear/forecast"], "minTreffers": 1, "modelantwoord": "1. Always stay on marked trails. 2. Carry plenty of water and thermal gear. 3. Check the weather forecast before leaving.", "uitleg": "Goede bergregels: blijf op het pad, neem water/uitrusting mee en controleer het weer."},
    {"type": "mc", "vraag": "Which phrase advises someone not to touch unknown wild mushrooms?", "opties": ["Under no circumstances should you consume wild mushrooms in the forest.", "Wild mushrooms are fun to throw.", "Taste every mushroom you find.", "Pick all mushrooms for lunch."], "antwoord": 0, "uitleg": "Duidelijke waarschuwing tegen giftige paddenstoelen."},
    {"type": "waaronwaar", "vraag": "Wearing bright reflective clothing helps rescue helicopters spot hikers in emergencies.", "antwoord": True, "uitleg": "Waar. Felle kleding vergroot de zichtbaarheid voor reddingsteams."},
    {"type": "invul", "vraag": "Complete the warning: <i>Whatever you ..., do not leave the marked path!</i>", "antwoord": "do", "uitleg": "'Whatever you do' (wat je ook doet)."},
    {"type": "mc", "vraag": "What is the best reaction when a partner says: <i>'I can't feel my fingers due to the freezing cold!'</i>?", "opties": ["Put on your thermal gloves immediately and warm your hands inside your jacket.", "Take off your shoes and jump in the snow.", "Drink freezing cold ice water.", "Wait three hours without moving."], "antwoord": 0, "uitleg": "Direct thermische handschoenen aandoen en opwarmen voorkomt bevriezing."},
    {"type": "waaronwaar", "vraag": "The phrase <i>'Hold on tight!'</i> means you should let go of the safety rope immediately.", "antwoord": False, "uitleg": "Onwaar. Het betekent 'houd je stevig vast!'."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>Take a deep breath and stay ... .</i>", "antwoord": "calm", "uitleg": "'Stay calm' (blijf rustig)."},
    {"type": "mc", "vraag": "Which word describes the final successful arrival at the top of a mountain?", "opties": ["Reaching the summit", "Crossing the river", "Entering the cave", "Checking the map"], "antwoord": 0, "uitleg": "'Reaching the summit' is het bereiken van de bergtop."}
  ]
}

# EXAMEN 19: H4 Reading & Adventure Stories (20 questions)
ex19 = {
  "id": "ex-h3-eng-19",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Hoofdstuk 4 — To the extreme",
  "titel": "Toets 4 — Reading Skills: Survival Narratives & Chronology",
  "vak": "Engels · HAVO 3 (H4)",
  "icoon": "🏕️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Why are chronological time markers (e.g. <i>At dawn, three hours later, by midnight</i>) vital in survival stories?", "opties": ["They establish the clear timeline of events and build suspense as conditions worsen", "They replace the names of all the characters", "They translate mountain names into English", "They prove the book was printed on recycled paper"], "antwoord": 0, "uitleg": "Tijdaanduidingen maken de chronologie en spanningsopbouw duidelijk."},
    {"type": "mc", "vraag": "What is <b>hypothermia</b> in cold-weather survival texts?", "opties": ["A dangerously low core body temperature caused by prolonged exposure to freezing conditions", "An allergic reaction to high mountain flowers", "A type of rapid downhill skiing technique", "A high fever caused by tropical mosquitoes"], "antwoord": 0, "uitleg": "Onderkoeling (hypothermie) door extreme kou."},
    {"type": "waaronwaar", "vraag": "In adventure literature, the <b>protagonist</b> is the main character who faces and overcomes conflicts.", "antwoord": True, "uitleg": "Waar. De protagonist is de hoofdpersoon."},
    {"type": "invul", "vraag": "Fill in the survival term (onderkoeling): <i>The wet clothing accelerated the hiker's ... .</i>", "antwoord": "hypothermia", "uitleg": "Hypothermia is onderkoeling."},
    {"type": "mc", "vraag": "What does a <b>turning point</b> in an extreme adventure story signify?", "opties": ["A critical moment when a major change occurs, altering the outcome of the survival ordeal", "The moment a hiker turns around to tie their shoelaces", "The page where the publisher's address is listed", "A road sign pointing towards a restaurant"], "antwoord": 0, "uitleg": "Het kantelpunt waarop de overlevingskansen drastisch veranderen."},
    {"type": "waaronwaar", "vraag": "Survival stories always conclude with the characters giving up in the first paragraph.", "antwoord": False, "uitleg": "Onwaar. Het genre draait juist om volharding en overwinning op tegenslag."},
    {"type": "invul", "vraag": "Fill in the noun (schuilplaats): <i>They built an emergency snow ... to survive the freezing night.</i>", "antwoord": "shelter|cave", "uitleg": "Shelter is een schuilplaats."},
    {"type": "mc", "vraag": "What does the expression <i>'against all odds'</i> mean in a triumphant survival story?", "opties": ["Achieving success or survival despite immense difficulty and low probability", "Playing an unfair game of roulette", "Counting only even numbers on a map", "Travelling with two identical backpacks"], "antwoord": 0, "uitleg": "'Against all odds' betekent tegen alle verwachtingen in slagen."},
    {"type": "mc", "vraag": "What role does <b>suspense</b> play in adventure narratives?", "opties": ["It creates a state of intense excitement and anxiety about what will happen next", "It reduces the vocabulary level of the text", "It tells the reader the ending on page one", "It removes adjectives from every sentence"], "antwoord": 0, "uitleg": "Spanning (suspense) houdt de lezer geboeid en nieuwsgierig."},
    {"type": "waaronwaar", "vraag": "Sensory descriptions (like the howling wind, biting frost, blinding snow) help readers visualize the harsh environment.", "antwoord": True, "uitleg": "Waar. Zintuiglijke details maken het barre landschap levendig."},
    {"type": "invul", "vraag": "Fill in the time connector: <i>At ..., as the sun rose, the rescue helicopter finally spotted their flare.</i>", "antwoord": "dawn|sunrise", "uitleg": "'At dawn' (bij het ochtendgloren)."},
    {"type": "mc", "vraag": "Why is Aaron Ralston's canyon survival story (127 Hours) famous worldwide?", "opties": ["Because he demonstrated extreme mental endurance and self-rescue under life-threatening conditions", "Because he won a gold medal in the Olympic 100 meters", "Because he discovered a new species of mountain goat", "Because he designed a popular smartphone app"], "antwoord": 0, "uitleg": "Ralston overleefde een extreme beklemming door ongekende mentale veerkracht."},
    {"type": "open", "vraag": "What character qualities are essential for an explorer surviving stranded in the wilderness?", "sleutelwoorden": ["resourceful/clever/mindset/smart", "determination/patience/courage/perseverance/calm"], "minTreffers": 1, "modelantwoord": "Resourcefulness, mental calmness, determination, and perseverance are critical qualities for wilderness survival.", "uitleg": "Vindingrijkheid, kalmte, vastberadenheid en doorzettingsvermogen zijn cruciaal."},
    {"type": "mc", "vraag": "What is meant by <b>frostbite</b>?", "opties": ["Injury to body tissues caused by exposure to extreme cold, often affecting fingers and toes", "A cold scoop of vanilla ice cream", "A winter holiday in Canada", "A gentle bite from a pet rabbit"], "antwoord": 0, "uitleg": "Frostbite is bevriezing van lichaamsweefsel (zoals vingers of tenen)."},
    {"type": "waaronwaar", "vraag": "Reading past tenses carefully helps you distinguish between past background events and immediate actions in a narrative.", "antwoord": True, "uitleg": "Waar. Werkwoordstijden helpen de volgorde van gebeurtenissen te begrijpen."},
    {"type": "invul", "vraag": "Complete the phrase: <i>They held on to the hope of ... until the very end.</i>", "antwoord": "survival|rescue", "uitleg": "Hope of survival / rescue."},
    {"type": "mc", "vraag": "What does a triumphant ending in a travel narrative evoke in the reader?", "opties": ["A sense of relief, admiration, and inspiration", "Complete confusion about grammar", "Anger at the weather forecast", "Disinterest in travel"], "antwoord": 0, "uitleg": "Opluchting en bewondering voor de menselijke veerkracht."},
    {"type": "waaronwaar", "vraag": "An emergency distress flare emits bright red light and smoke to signal location to rescuers.", "antwoord": True, "uitleg": "Waar. Noodsignaalfakkels geven felrood licht en rook."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>The mountaineers faced a life-or-... decision on the ridge.</i>", "antwoord": "death", "uitleg": "A life-or-death decision (een kwestie van leven of dood)."},
    {"type": "mc", "vraag": "What is the theme of many extreme sports biographies?", "opties": ["Pushing human physical and psychological boundaries to achieve greatness", "Learning how to cook breakfast quickly", "Buying discounted sports clothes in malls", "Memorizing train station schedules"], "antwoord": 0, "uitleg": "Het verleggen van menselijke fysieke en mentale grenzen."}
  ]
}

# EXAMEN 20: H4 Hoofdstuk Eindtoets (Mix & Sınav Simülasyonu) (20 questions)
ex20 = {
  "id": "ex-h3-eng-20",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Hoofdstuk 4 — To the extreme",
  "titel": "Toets 5 — Hoofdstuk 4 Eindtoets (Mix & Examen)",
  "vak": "Engels · HAVO 3 (H4)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "What is an <b>avalanche</b>?", "opties": ["A rapid flow of snow, ice, and debris down a steep mountain slope", "A calm summer breeze over a mountain meadow", "A shallow stream of clean drinking water", "A newly paved mountain tunnel for cars"], "antwoord": 0, "uitleg": "Een lawine is een plotselinge sneeuwmassa die van de berg raast."},
    {"type": "mc", "vraag": "Choose the correct comparative: <i>This mountain ridge is ... (dangerous) than the standard tourist trail.</i>", "opties": ["more dangerous", "dangerouser", "most dangerous", "as dangerous"], "antwoord": 0, "uitleg": "Dangerous (3 lettergrepen) -> more dangerous than."},
    {"type": "waaronwaar", "vraag": "The modal verb <b>should</b> indicates a strict legal prohibition punishable by jail time.", "antwoord": False, "uitleg": "Onwaar. 'Should' geeft een advies; voor een verbod gebruik je 'mustn't'."},
    {"type": "invul", "vraag": "Fill in the English word for <i>uithoudingsvermogen</i>: <i>Running an ultra-marathon requires immense ... .</i>", "antwoord": "endurance|stamina", "uitleg": "Endurance / stamina is uithoudingsvermogen."},
    {"type": "mc", "vraag": "Which phrase is the most effective safety warning on a mountain ridge?", "opties": ["Watch out! The ledge is narrow and slippery.", "Good afternoon, what a lovely jacket!", "Where can I buy ice cream?", "Look at the colorful little flowers."], "antwoord": 0, "uitleg": "'Watch out!' waarschuwt direct voor gevaar."},
    {"type": "waaronwaar", "vraag": "<b>Dehydration</b> occurs when the body does not receive sufficient water and electrolytes.", "antwoord": True, "uitleg": "Waar. Dehydration is uitdroging."},
    {"type": "invul", "vraag": "Fill in the superlative of <i>(bad)</i>: <i>This was the ... blizzard in fifty years.</i>", "antwoord": "worst", "uitleg": "Bad -> worse -> the worst."},
    {"type": "mc", "vraag": "What is the core meaning of the adjective <b>fearless</b> in extreme sports?", "opties": ["Brave, courageous, and showing no fear in dangerous situations", "Afraid of heights and mountains", "Refusing to drink clean water", "Walking without hiking boots"], "antwoord": 0, "uitleg": "Fearless betekent onverschrokken."},
    {"type": "mc", "vraag": "Choose the correct modal sentence for advice:", "opties": ["You should pack extra thermal layers before climbing.", "You must to pack layers.", "You ought pack layers.", "You shouldn't pack any warm clothes."], "antwoord": 0, "uitleg": "'You should pack' (je zou moeten inpakken)."},
    {"type": "waaronwaar", "vraag": "The phrase <i>'Keep going, you've got this!'</i> is used to encourage someone facing exhaustion.", "antwoord": True, "uitleg": "Waar. Dit is een positieve aanmoediging."},
    {"type": "invul", "vraag": "Fill in the noun (reddingsteam): <i>The mountain ... team rescued the trapped climbers.</i>", "antwoord": "rescue", "uitleg": "Rescue team is het reddingsteam."},
    {"type": "mc", "vraag": "What does <b>altitude</b> refer to?", "opties": ["The elevation or height above sea level", "The weight of a backpack in pounds", "The speed of downhill skiing", "The length of climbing ropes"], "antwoord": 0, "uitleg": "Altitude is de hoogte boven zeeniveau."},
    {"type": "open", "vraag": "Why is keeping a calm mindset essential when dealing with an emergency in the wilderness?", "sleutelwoorden": ["panic/prevent/mistakes/clear/think", "rational/decisions/safe/smart"], "minTreffers": 1, "modelantwoord": "Staying calm prevents panic, allows you to think clearly, and helps you make safe, smart survival decisions.", "uitleg": "Kalmte voorkomt paniek en stelt je in staat om verstandige beslissingen te nemen."},
    {"type": "mc", "vraag": "Choose the correct sentence of equality:", "opties": ["Hiking is not as exhausting as running a marathon.", "Hiking is not as exhausting than a marathon.", "Hiking is not so exhausting than running.", "Hiking is not more exhaust as running."], "antwoord": 0, "uitleg": "(Not) as ... as."},
    {"type": "waaronwaar", "vraag": "An <b>adrenaline rush</b> produces physical tiredness and puts you to sleep immediately.", "antwoord": False, "uitleg": "Onwaar. Een adrenalinestoot geeft juist een explosie van energie en alertheid."},
    {"type": "invul", "vraag": "Complete the warning: <i>Whatever you do, don't ... unclipped from the safety line!</i>", "antwoord": "unclip|stay|unhook", "uitleg": "Don't unclip (maak je niet los)."},
    {"type": "mc", "vraag": "What is a <b>blizzard</b>?", "opties": ["A severe snowstorm with strong winds and intense cold", "A gentle spring rain shower", "A warm sunny day in the desert", "A calm fog over a city harbor"], "antwoord": 0, "uitleg": "Een zware sneeuwstorm met harde wind."},
    {"type": "waaronwaar", "vraag": "The comparative form of <i>good</i> is <i>gooder</i>.", "antwoord": False, "uitleg": "Onwaar. Good -> better -> the best."},
    {"type": "invul", "vraag": "Complete the phrase: <i>They reached the mountain ... just before sunset.</i>", "antwoord": "summit|peak|top", "uitleg": "Summit / peak / top (bergtop)."},
    {"type": "mc", "vraag": "Which phrase describes pushing beyond your normal limits?", "opties": ["Pushing yourself to the extreme", "Taking a lazy afternoon nap", "Watching television on the couch", "Ordering food online"], "antwoord": 0, "uitleg": "'Pushing yourself to the extreme' betekent je uiterste grenzen verleggen."}
  ]
}

write_examen("examen_16.js", ex16)
write_examen("examen_17.js", ex17)
write_examen("examen_18.js", ex18)
write_examen("examen_19.js", ex19)
write_examen("examen_20.js", ex20)
print("Hoofdstuk 4 exams (16 to 20) generated successfully!")
