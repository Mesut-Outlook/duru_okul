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

# EXAMEN 1: H1 Theme Words & Begrippen (20 questions)
ex1 = {
  "id": "ex-h3-eng-1",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Hoofdstuk 1 — The world around you",
  "titel": "Toets 1 — Theme Words: Culture, Identity & Customs",
  "vak": "Engels · HAVO 3 (H1)",
  "icoon": "🌍",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Which English noun translates directly to <i>gastvrijheid</i>?", "opties": ["Hospitality", "Heritage", "Diversity", "Habit"], "antwoord": 0, "uitleg": "Hospitality betekent gastvrijheid."},
    {"type": "mc", "vraag": "Which term refers to an oversimplified image or generalized idea about a group of people?", "opties": ["Stereotype", "Custom", "Destination", "Identity"], "antwoord": 0, "uitleg": "A stereotype is een stereotiep beeld of vooroordeel."},
    {"type": "waaronwaar", "vraag": "A <b>native speaker</b> is someone who learned a language as an adult during university.", "antwoord": False, "uitleg": "Onwaar. A native speaker spreekt de taal vanaf de geboorte als moedertaal."},
    {"type": "invul", "vraag": "Fill in the English word for <i>diversiteit / verscheidenheid</i>: <i>Our school values cultural ... in the classroom.</i>", "antwoord": "diversity", "uitleg": "Diversity betekent diversiteit."},
    {"type": "mc", "vraag": "What does the noun <b>heritage</b> mean?", "opties": ["Cultural traditions and historical background passed down through generations", "A special visa required for European travel", "A flight schedule between London and Amsterdam", "A traditional British breakfast recipe"], "antwoord": 0, "uitleg": "Heritage is cultureel erfgoed en achtergrond."},
    {"type": "waaronwaar", "vraag": "If someone is <b>fluent</b> in a language, they speak it smoothly and easily without constant hesitations.", "antwoord": True, "uitleg": "Waar. Fluent betekent vloeiend taalgebruik."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>A pupil who travels to another country to attend school is an ... student.</i>", "antwoord": "exchange|exchange student", "uitleg": "Exchange student is een uitwisselingsstudent."},
    {"type": "mc", "vraag": "Choose the best synonym for <b>custom</b>: <i>It is a local custom to remove your shoes before entering.</i>", "opties": ["Tradition", "Airport", "Passport", "Accident"], "antwoord": 0, "uitleg": "Custom betekent traditie of gewoonte."},
    {"type": "mc", "vraag": "What does the adjective <b>multicultural</b> describe?", "opties": ["A society comprising many distinct cultural or ethnic groups", "A single isolated village with one family", "A language without irregular verbs", "A factory producing electronic goods"], "antwoord": 0, "uitleg": "Multicultural betekent multicultureel."},
    {"type": "waaronwaar", "vraag": "The word <b>destination</b> refers to the starting point of an international journey.", "antwoord": False, "uitleg": "Onwaar. Destination is de eindbestemming, niet het vertrekpunt."},
    {"type": "invul", "vraag": "Fill in the noun (identiteit): <i>Your native language is closely connected to your personal ... .</i>", "antwoord": "identity", "uitleg": "Identity betekent identiteit."},
    {"type": "mc", "vraag": "What does <b>culture shock</b> mean when moving abroad?", "opties": ["Feeling disoriented or confused when experiencing an unfamiliar way of life", "An electric shock caused by foreign plug sockets", "Winning a prize in a cultural quiz competition", "Learning to cook traditional foreign dishes"], "antwoord": 0, "uitleg": "Culture shock is de verwarring bij het aanpassen aan een nieuwe cultuur."},
    {"type": "open", "vraag": "Explain in your own words why mutual hospitality is important during an international exchange program.", "sleutelwoorden": ["welcome/respect/host/feel/home", "comfortable/culture/friendly/kind"], "minTreffers": 1, "modelantwoord": "Hospitality makes foreign exchange students feel welcome, comfortable and respected in a new environment.", "uitleg": "Gastvrijheid zorgt ervoor dat buitenlandse studenten zich snel thuis en welkom voelen."},
    {"type": "mc", "vraag": "Which phrase describes a daily repetitive routine?", "opties": ["A habit", "A heritage", "A destination", "A diversity"], "antwoord": 0, "uitleg": "A habit is een vaste gewoonte."},
    {"type": "waaronwaar", "vraag": "Cultural <b>diversity</b> in a city means that only one single culture is allowed to exist.", "antwoord": False, "uitleg": "Onwaar. Diversity betekent juist verscheidenheid aan vele culturen."},
    {"type": "invul", "vraag": "Fill in the adjective (buitenlands): <i>Learning a ... language opens many international doors.</i>", "antwoord": "foreign", "uitleg": "Foreign betekent buitenlands."},
    {"type": "mc", "vraag": "What does the word <b>community</b> mean in a neighborhood context?", "opties": ["A group of people living together in the same area sharing common interests", "A government office where passports are stamped", "An international airport terminal", "A high-speed train connection"], "antwoord": 0, "uitleg": "Community is een hechte gemeenschap van bewoners."},
    {"type": "waaronwaar", "vraag": "Stereotypes are always 100% accurate and describe every single individual perfectly.", "antwoord": False, "uitleg": "Onwaar. Stereotypes zijn versimpelde generalisaties en kloppen vaak niet voor individuen."},
    {"type": "invul", "vraag": "Complete the phrase: <i>First impressions are important when making a good ... on new classmates.</i>", "antwoord": "impression", "uitleg": "'Make a good impression' betekent een goede indruk maken."},
    {"type": "mc", "vraag": "Which word is an antonym (opposite) of <b>foreign</b>?", "opties": ["Native / Local", "Multicultural", "Distant", "International"], "antwoord": 0, "uitleg": "Native of local is het tegenovergestelde van foreign."}
  ]
}

# EXAMEN 2: H1 Grammar (Present Simple vs Continuous) (20 questions)
ex2 = {
  "id": "ex-h3-eng-2",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Hoofdstuk 1 — The world around you",
  "titel": "Toets 2 — Grammar: Present Simple vs. Present Continuous",
  "vak": "Engels · HAVO 3 (H1)",
  "icoon": "⏱️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Choose the correct sentence in the <b>Present Continuous</b>:", "opties": ["Listen! The choir is singing a traditional Scottish song.", "Listen! The choir sings a traditional song.", "Listen! The choir are sing a traditional song.", "Listen! The choir was singing currently."], "antwoord": 0, "uitleg": "'Listen!' is het signaalwoord voor de Present Continuous (is singing)."},
    {"type": "mc", "vraag": "Which verb form completes the routine: <i>Mark usually ... his bike to school.</i>", "opties": ["rides", "is riding", "ride", "are riding"], "antwoord": 0, "uitleg": "'Usually' duidt op een routine (Present Simple). Mark = he, dus rides."},
    {"type": "waaronwaar", "vraag": "Verbs like <i>understand, believe, know</i> are commonly used with -ing in the Present Continuous.", "antwoord": False, "uitleg": "Onwaar. Dit zijn state verbs en staan in de Present Simple."},
    {"type": "invul", "vraag": "Fill in the correct form of <i>(to play)</i>: <i>Right now, the exchange students ... tennis in the park.</i>", "antwoord": "are playing", "uitleg": "Exchange students is meervoud + right now -> are playing."},
    {"type": "mc", "vraag": "Which of the following questions is correctly structured in the <b>Present Simple</b>?", "opties": ["Does your host family live near London?", "Do your host family lives near London?", "Is your host family live near London?", "Does your host family lives near London?"], "antwoord": 0, "uitleg": "Does + hele werkwoord (live)."},
    {"type": "waaronwaar", "vraag": "Scientific facts like <i>'The Earth revolves around the Sun'</i> are expressed using the Present Simple.", "antwoord": True, "uitleg": "Waar. Algemene feiten staan altijd in de Present Simple."},
    {"type": "invul", "vraag": "Fill in the negative form of <i>(to speak)</i>: <i>Sophie ... Spanish, but she is learning it now.</i>", "antwoord": "does not speak|doesn't speak", "uitleg": "Sophie (she) -> does not speak / doesn't speak."},
    {"type": "mc", "vraag": "Which signal word belongs typically to the <b>Present Continuous</b>?", "opties": ["At the moment", "Every Sunday", "Always", "Seldom"], "antwoord": 0, "uitleg": "'At the moment' geeft aan dat iets nu bezig is."},
    {"type": "mc", "vraag": "Why is <i>'I am preferring tea over coffee'</i> incorrect in standard English?", "opties": ["Prefer is a state verb expressing personal preference and cannot take the continuous -ing form", "Prefer requires the auxiliary verb does in positive statements", "Coffee is a plural noun in British English", "Tea cannot be used as an object in continuous tenses"], "antwoord": 0, "uitleg": "Prefer is een toestandswerkwoord: 'I prefer tea'."},
    {"type": "waaronwaar", "vraag": "The sentence <i>'Look! It is snowing outside'</i> uses the Present Continuous because the action is happening right now.", "antwoord": True, "uitleg": "Waar. 'Look!' geeft een actie aan die op dit moment plaatsvindt."},
    {"type": "invul", "vraag": "Fill in the correct form of <i>(to do)</i>: <i>What ... you ... right now?</i>", "antwoord": "are doing|are you doing", "uitleg": "Present Continuous vraagzin: What are you doing?"},
    {"type": "mc", "vraag": "Choose the correct form: <i>Water ... at zero degrees Celsius.</i>", "opties": ["freezes", "is freezing", "freeze", "are freezing"], "antwoord": 0, "uitleg": "Natuurfeit -> Present Simple (freezes)."},
    {"type": "open", "vraag": "Explain the clear difference in meaning between: <i>'I live in Amsterdam'</i> and <i>'I am living in Amsterdam this month'</i>.", "sleutelwoorden": ["permanent/habit/routine", "temporary/short/month/now"], "minTreffers": 1, "modelantwoord": "'I live in Amsterdam' is permanent (Present Simple), while 'I am living in Amsterdam this month' is temporary (Present Continuous).", "uitleg": "De Simple geeft een permanente situatie aan; de Continuous een tijdelijke situatie."},
    {"type": "mc", "vraag": "Which of the following sentences expresses a fixed timetable?", "opties": ["The flight to New York departs at 10:15 tomorrow morning.", "The flight is departing every week normally.", "The flight departed right now.", "The flight does departing at 10."], "antwoord": 0, "uitleg": "Vaste dienstregelingen staan in de Present Simple."},
    {"type": "waaronwaar", "vraag": "In the sentence <i>'She has two brothers'</i>, the verb <i>has</i> expresses possession and is in the Present Simple.", "antwoord": True, "uitleg": "Waar. Bezit wordt uitgedrukt in de Present Simple."},
    {"type": "invul", "vraag": "Fill in the correct form of <i>(to watch)</i>: <i>Be quiet! Dad ... the evening news.</i>", "antwoord": "is watching", "uitleg": "Dad (he) + is watching nu op dit moment."},
    {"type": "mc", "vraag": "Which sentence correctly uses a state verb without the continuous -ing form?", "opties": ["Do you understand the grammar rule now?", "Are you understanding the grammar rule now?", "Does you understand the grammar rule now?", "Do you understands the grammar rule now?"], "antwoord": 0, "uitleg": "Understand is een state verb: 'Do you understand?'."},
    {"type": "waaronwaar", "vraag": "The negative Present Simple form for <i>we (to drink)</i> is <i>we isn't drinking</i>.", "antwoord": False, "uitleg": "Onwaar. Het is 'we don't drink' (Simple) of 'we aren't drinking' (Continuous)."},
    {"type": "invul", "vraag": "Fill in the correct form of <i>(to go)</i>: <i>My grandparents ... to the cinema every Friday evening.</i>", "antwoord": "go", "uitleg": "Grandparents (meervoud) + routine -> go."},
    {"type": "mc", "vraag": "Which adverb of frequency means almost never?", "opties": ["Rarely / Seldom", "Usually", "Always", "Frequently"], "antwoord": 0, "uitleg": "Rarely / seldom betekent zelden of bijna nooit."}
  ]
}

# EXAMEN 3: H1 Stones & Speaking (20 questions)
ex3 = {
  "id": "ex-h3-eng-3",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Hoofdstuk 1 — The world around you",
  "titel": "Toets 3 — Stones & Skills: Social Interactions & Opinions",
  "vak": "Engels · HAVO 3 (H1)",
  "icoon": "💬",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Which phrase is the standard polite greeting when meeting someone for the first time?", "opties": ["Pleased to meet you! / Nice to meet you!", "What are you doing here?", "Give me your identification.", "Why did you come to this place?"], "antwoord": 0, "uitleg": "'Pleased to meet you' is de standaard beleefde begroeting."},
    {"type": "mc", "vraag": "How do you introduce yourself formally in front of a group?", "opties": ["Let me introduce myself: my name is Duru.", "Look at me, I am talking now.", "Everybody listen to my voice.", "I command you to hear my name."], "antwoord": 0, "uitleg": "'Let me introduce myself' is de vaste beleefde formule."},
    {"type": "waaronwaar", "vraag": "The phrase <i>'As far as I'm concerned'</i> is used to order drinks at a cafe.", "antwoord": False, "uitleg": "Onwaar. Het betekent 'wat mij betreft' en leidt een mening in."},
    {"type": "invul", "vraag": "Complete the phrase to state an opinion: <i>In my ..., living abroad is a great life experience.</i>", "antwoord": "opinion|view", "uitleg": "'In my opinion' (naar mijn mening)."},
    {"type": "mc", "vraag": "How do you politely disagree with someone during a discussion?", "opties": ["I see what you mean, but I look at it somewhat differently.", "You are talking nonsense.", "Stop talking immediately.", "Nobody agrees with your silly ideas."], "antwoord": 0, "uitleg": "'I see what you mean, but...' toont respect voor de ander."},
    {"type": "waaronwaar", "vraag": "The phrase <i>'I'm really into photography'</i> means you enjoy photography as a hobby.", "antwoord": True, "uitleg": "Waar. 'To be into something' betekent ergens dol op zijn / als hobby hebben."},
    {"type": "invul", "vraag": "Complete the question: <i>What do you like doing in your ... time?</i>", "antwoord": "free|spare", "uitleg": "'Free time' of 'spare time' betekent vrije tijd."},
    {"type": "mc", "vraag": "What is the best reaction when someone says: <i>'Thank you so much for your hospitality!'</i>?", "opties": ["You're very welcome! It was a pleasure hosting you.", "I know I am the best.", "Pay me immediately.", "Don't say that word again."], "antwoord": 0, "uitleg": "'You're very welcome!' is het juiste gastvrije antwoord."},
    {"type": "mc", "vraag": "Which phrase asks for another person's viewpoint on school uniforms?", "opties": ["What do you think of school uniforms?", "Why do you wear socks?", "Can I take your jacket?", "Where is the uniform store located?"], "antwoord": 0, "uitleg": "'What do you think of...' vraagt naar iemands mening."},
    {"type": "waaronwaar", "vraag": "The expression <i>'That's a very good point'</i> indicates that you strongly disagree with the speaker.", "antwoord": False, "uitleg": "Onwaar. Het betekent dat je het een heel goed argument vindt."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>Where are you from ...?</i>", "antwoord": "originally", "uitleg": "'Where are you from originally?' vraagt naar iemands oorspronkelijke herkomst."},
    {"type": "mc", "vraag": "How do you ask about someone's daily routine?", "opties": ["What does a typical day in your school look like?", "Why are you looking at your watch?", "When did you buy that bag?", "How much was your ticket?"], "antwoord": 0, "uitleg": "Dit vraagt naar een typische dagindeling."},
    {"type": "open", "vraag": "Write a short polite response concurring with a classmate who states that speaking multiple tongues brings immense benefits on trips abroad.", "sleutelwoorden": ["completely/definitely/concur/same view/agree", "valuable/helpful/practical/essential/advantage"], "minTreffers": 1, "modelantwoord": "I completely agree with you. Knowing different languages makes traveling much easier and more enjoyable.", "uitleg": "Een instemmend antwoord bevestigt de stelling op een vriendelijke en overtuigende manier."},
    {"type": "mc", "vraag": "Which informal closing is appropriate for an email to a pen friend?", "opties": ["All the best, / Take care,", "Yours faithfully, Sir,", "Sincerely yours, Director,", "I hereby conclude this document,"], "antwoord": 0, "uitleg": "'All the best' of 'Take care' is informeel en vriendelijk."},
    {"type": "waaronwaar", "vraag": "In English conversation, nodding and saying <i>'I see'</i> shows that you are actively listening to the speaker.", "antwoord": True, "uitleg": "Waar. Dit toont actieve luistervaardigheid."},
    {"type": "invul", "vraag": "Complete the phrase: <i>I completely ... with what you just said.</i>", "antwoord": "agree", "uitleg": "'I completely agree' (ik ben het er helemaal mee eens)."},
    {"type": "mc", "vraag": "How do you ask someone to repeat what they said politely?", "opties": ["Could you repeat that, please? I didn't quite catch it.", "Speak louder now!", "What is wrong with your voice?", "Say it again fast!"], "antwoord": 0, "uitleg": "Beleefd herhaling vragen doe je met 'Could you repeat that, please?'."},
    {"type": "waaronwaar", "vraag": "Starting an email to a friend with <i>'Dear Sir or Madam,'</i> is considered natural and casual in English.", "antwoord": False, "uitleg": "Onwaar. 'Dear Sir or Madam' is uiterst formeel voor officiële brieven."},
    {"type": "invul", "vraag": "Complete the email opening: <i>Thanks for your email! How are ... going?</i>", "antwoord": "things", "uitleg": "'How are things going?' is een populaire informele openingszin."},
    {"type": "mc", "vraag": "What does the expression <i>'I'm fond of animals'</i> mean?", "opties": ["I really like and care about animals", "I am afraid of animals", "I hunt wild animals", "I sell pets online"], "antwoord": 0, "uitleg": "'To be fond of' betekent erg gesteld zijn op / leuk vinden."}
  ]
}

# EXAMEN 4: H1 Reading & Writing (20 questions)
ex4 = {
  "id": "ex-h3-eng-4",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Hoofdstuk 1 — The world around you",
  "titel": "Toets 4 — Reading Skills & Informal Writing",
  "vak": "Engels · HAVO 3 (H1)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "What is <b>skimming</b> in reading comprehension?", "opties": ["Reading quickly over a text to get the general idea or main message", "Looking specifically for a single date or phone number", "Reading every single word with a magnifying glass", "Translating a text word for word into Dutch"], "antwoord": 0, "uitleg": "Skimmen is oriënterend en snel lezen om de hoofdgedachte te vatten."},
    {"type": "mc", "vraag": "What is <b>scanning</b> in reading strategy?", "opties": ["Looking through a text rapidly to locate specific information like a name or date", "Reading aloud in front of the whole class", "Summarizing the entire book in 500 words", "Checking spelling mistakes with red ink"], "antwoord": 0, "uitleg": "Scannen is zoekend lezen naar specifieke details."},
    {"type": "waaronwaar", "vraag": "In English writing, each new paragraph should introduce a new main idea or topic.", "antwoord": True, "uitleg": "Waar. Elke alinea behandelt één duidelijke kernidee."},
    {"type": "invul", "vraag": "Fill in the reading term: <i>Looking quickly through a text for a specific word or number is called ... .</i>", "antwoord": "scanning|scan", "uitleg": "Scanning is zoekend lezen."},
    {"type": "mc", "vraag": "What is a <b>topic sentence</b> in an English paragraph?", "opties": ["The sentence (often the first) that states the main idea of the paragraph", "The very last word of a book chapter", "The title written on the front cover", "A footnote explaining grammar rules"], "antwoord": 0, "uitleg": "De topic sentence bevat de kernboodschap van de alinea."},
    {"type": "waaronwaar", "vraag": "Informal emails between penpals should be written in strict legal language without contractions.", "antwoord": False, "uitleg": "Onwaar. Informele mails mogen samentrekkingen (don't, I'm) en vriendelijke taal bevatten."},
    {"type": "invul", "vraag": "Complete the email closing: <i>Write back ...!</i>", "antwoord": "soon", "uitleg": "'Write back soon!' (schrijf snel terug!)."},
    {"type": "mc", "vraag": "Which linking word is used to show a contrast between two ideas?", "opties": ["However / On the other hand", "Furthermore / In addition", "Therefore / As a result", "Firstly / To begin with"], "antwoord": 0, "uitleg": "'However' geeft een tegenstelling aan."},
    {"type": "mc", "vraag": "Which linking word is used to add extra supporting information?", "opties": ["In addition / Moreover", "Nevertheless", "Despite", "Although"], "antwoord": 0, "uitleg": "'In addition' en 'Moreover' voegen informatie toe."},
    {"type": "waaronwaar", "vraag": "Headings and subheadings help readers predict what a text section will be about.", "antwoord": True, "uitleg": "Waar. Tussenkopjes geven structuur en overzicht."},
    {"type": "invul", "vraag": "Fill in the connector for contrast: <i>She studied very hard; ..., she found the test challenging.</i>", "antwoord": "however|nevertheless", "uitleg": "'However' of 'nevertheless' drukt een tegenstelling uit."},
    {"type": "mc", "vraag": "What should you check during the proofreading stage of your writing?", "opties": ["Spelling, punctuation, grammar, and paragraph organization", "The price of the paper in the store", "The speed of your typing keyboard", "The color of your desk lamp"], "antwoord": 0, "uitleg": "Proofreading is het nakijken op spelling, grammatica en leestekens."},
    {"type": "open", "vraag": "Name two visual elements that can help you understand the main topic of an English article before reading the full text.", "sleutelwoorden": ["headline/title/heading", "pictures/photos/captions/subheadings/diagrams"], "minTreffers": 1, "modelantwoord": "Headlines/titles and pictures or photos with captions give immediate clues about the article topic.", "uitleg": "Koppen, tussenkopjes en afbeeldingen geven direct inzicht in het onderwerp."},
    {"type": "mc", "vraag": "What is the purpose of an introductory paragraph in an article?", "opties": ["To introduce the subject, grab the reader's attention, and outline what follows", "To say goodbye to the reader", "To list the names of all printing staff", "To provide blank space for drawing"], "antwoord": 0, "uitleg": "De inleiding introduceert het onderwerp en wekt interesse."},
    {"type": "waaronwaar", "vraag": "Using full capital letters for an entire email is considered shouting and poor netiquette in English.", "antwoord": True, "uitleg": "Waar. Hoofdletters voor hele zinnen komt over als schreeuwen."},
    {"type": "invul", "vraag": "Complete the phrase: <i>First of ..., let's look at the background of the exchange program.</i>", "antwoord": "all", "uitleg": "'First of all' (allereerst)."},
    {"type": "mc", "vraag": "Which word indicates a cause-and-effect relationship?", "opties": ["Therefore / Because of this", "Although", "Whereas", "Instead"], "antwoord": 0, "uitleg": "'Therefore' geeft een oorzaak-gevolgrelatie aan."},
    {"type": "waaronwaar", "vraag": "When reading an unfamiliar English word, looking at the surrounding context words can often help you deduce its meaning.", "antwoord": True, "uitleg": "Waar. Contextuele aanwijzingen helpen onbekende woorden te begrijpen."},
    {"type": "invul", "vraag": "Fill in the connector: <i>I was very tired. ... a result, I went to sleep early.</i>", "antwoord": "as", "uitleg": "'As a result' (als gevolg daarvan)."},
    {"type": "mc", "vraag": "What is a concluding paragraph designed to do?", "opties": ["Summarize the main points and provide a final thought or conclusion", "Introduce three completely unrelated new topics", "Copy the entire introduction word for word", "Ask the reader for their home address"], "antwoord": 0, "uitleg": "De conclusie vat de kernpunten samen en rondt de tekst af."}
  ]
}

# EXAMEN 5: H1 Hoofdstuk Eindtoets (Mix & Sınav Simülasyonu) (20 questions)
ex5 = {
  "id": "ex-h3-eng-5",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Hoofdstuk 1 — The world around you",
  "titel": "Toets 5 — Hoofdstuk 1 Eindtoets (Mix & Examen)",
  "vak": "Engels · HAVO 3 (H1)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "What does the word <b>multicultural</b> mean?", "opties": ["Representing or containing several cultural traditions and backgrounds", "Belonging strictly to a single historical family", "Dealing exclusively with space technology", "Speaking only one single dialect"], "antwoord": 0, "uitleg": "Multicultural betekent multicultureel."},
    {"type": "mc", "vraag": "Choose the correct verb: <i>Liam ... (to live) in Manchester, but this term he ... (to study) in Rotterdam.</i>", "opties": ["lives / is studying", "is living / studies", "live / study", "lived / are studying"], "antwoord": 0, "uitleg": "Wonen = permanente situatie (lives); deze term = tijdelijk (is studying)."},
    {"type": "waaronwaar", "vraag": "The phrase <i>'In my opinion'</i> is used to state an objective mathematical calculation.", "antwoord": False, "uitleg": "Onwaar. 'In my opinion' leidt een persoonlijke mening in."},
    {"type": "invul", "vraag": "Fill in the missing noun: <i>Eating turkey at Christmas is a beloved British ... .</i>", "antwoord": "tradition|custom", "uitleg": "Tradition of custom betekent traditie."},
    {"type": "mc", "vraag": "Which phrase is the best informal closing for an email to a friend?", "opties": ["Take care,", "I remain your obedient servant,", "To whom it may concern,", "Yours faithfully,"], "antwoord": 0, "uitleg": "'Take care' is een warme informele afsluiting."},
    {"type": "waaronwaar", "vraag": "A <b>stereotype</b> is an individualized, carefully verified psychological analysis of one specific person.", "antwoord": False, "uitleg": "Onwaar. Een stereotype is een overgesimplificeerd vooroordeel over een groep."},
    {"type": "invul", "vraag": "Fill in the correct Present Continuous form: <i>Listen! The teacher ... (to explain) the assignment right now.</i>", "antwoord": "is explaining", "uitleg": "The teacher (she/he) + is explaining."},
    {"type": "mc", "vraag": "What does <b>heritage</b> refer to?", "opties": ["Valued traditions, monuments, and culture passed down through generations", "A temporary passport stamp", "A type of modern electric scooter", "The daily lunch menu at a cafeteria"], "antwoord": 0, "uitleg": "Heritage is cultureel erfgoed."},
    {"type": "mc", "vraag": "Which question correctly asks for someone's viewpoint?", "opties": ["How do you feel about exchange programs?", "Why do you have two shoes?", "Where is the departure gate?", "When did the clock strike twelve?"], "antwoord": 0, "uitleg": "'How do you feel about...' vraagt naar een mening."},
    {"type": "waaronwaar", "vraag": "State verbs like <i>hate, know, love</i> are typically used in the Present Continuous with -ing.", "antwoord": False, "uitleg": "Onwaar. State verbs staan in de Present Simple."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>She speaks three languages ... and without any hesitation.</i>", "antwoord": "fluently|fluent", "uitleg": "Fluently betekent vloeiend."},
    {"type": "mc", "vraag": "What is the primary function of a <b>topic sentence</b>?", "opties": ["To express the main idea of a paragraph clearly", "To list the names of all dictionary publishers", "To translate foreign nouns into Latin", "To end an email formally"], "antwoord": 0, "uitleg": "De topic sentence formuleert de kern van de alinea."},
    {"type": "open", "vraag": "Why is cultural diversity considered an advantage in modern international schools?", "sleutelwoorden": ["learn/different/cultures/perspectives", "respect/understand/open/world"], "minTreffers": 1, "modelantwoord": "Cultural diversity allows students to learn about different perspectives, traditions and promotes mutual understanding and respect.", "uitleg": "Diversiteit verrijkt de school doordat leerlingen kennismaken met andere perspectieven en elkaars cultuur leren respecteren."},
    {"type": "mc", "vraag": "Which negative Present Simple statement is grammatically correct?", "opties": ["My parents don't speak French.", "My parents doesn't speaks French.", "My parents isn't speak French.", "My parents not speak French."], "antwoord": 0, "uitleg": "Parents (meervoud) -> don't speak."},
    {"type": "waaronwaar", "vraag": "In an English email, the greeting <i>'Hi Sarah,'</i> should be followed by a comma.", "antwoord": True, "uitleg": "Waar. In het Engels volgt er na de aanhef een komma."},
    {"type": "invul", "vraag": "Complete the sentence: <i>We experienced great ... from our host family in Edinburgh.</i>", "antwoord": "hospitality", "uitleg": "Hospitality betekent gastvrijheid."},
    {"type": "mc", "vraag": "Which linking word indicates addition of new information?", "opties": ["Furthermore / In addition", "However", "Although", "Instead"], "antwoord": 0, "uitleg": "'Furthermore' voegt extra informatie toe."},
    {"type": "waaronwaar", "vraag": "The sentence <i>'Look! The plane takes off'</i> is grammatically correct for an event happening right now.", "antwoord": False, "uitleg": "Onwaar. Voor een handeling die nu bezig is moet het zijn: 'The plane is taking off'."},
    {"type": "invul", "vraag": "Complete the phrase: <i>Let me ... myself: my name is Duru.</i>", "antwoord": "introduce", "uitleg": "'Let me introduce myself'."},
    {"type": "mc", "vraag": "What does <b>skimming</b> mean when preparing for a reading test?", "opties": ["Reading quickly through a text to understand the main gist or overall idea", "Translating every sentence word by word", "Memorizing every irregular past tense verb", "Underlining only numbers in blue pen"], "antwoord": 0, "uitleg": "Skimmen is snel scannend lezen voor de hoofdlijn."}
  ]
}

write_examen("examen_1.js", ex1)
write_examen("examen_2.js", ex2)
write_examen("examen_3.js", ex3)
write_examen("examen_4.js", ex4)
write_examen("examen_5.js", ex5)
print("Hoofdstuk 1 exams (1 to 5) generated successfully!")
