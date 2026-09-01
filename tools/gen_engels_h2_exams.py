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

# EXAMEN 6: H2 Theme Words & Begrippen (Crime & Justice) (20 questions)
ex6 = {
  "id": "ex-h3-eng-6",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Hoofdstuk 2 — Crime",
  "titel": "Toets 1 — Theme Words: Crime, Law & Investigation",
  "vak": "Engels · HAVO 3 (H2)",
  "icoon": "🔍",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "What is the specific definition of <b>burglary</b>?", "opties": ["Illegally breaking into a building or home with the intent to steal", "Stealing money directly from a bank teller using a weapon", "Picking someone's pocket on a crowded subway train", "Downloading copyrighted music illegally online"], "antwoord": 0, "uitleg": "Burglary is inbraak in een gebouw."},
    {"type": "mc", "vraag": "What is a <b>suspect</b> in a criminal case?", "opties": ["A person thought to be guilty of a crime or offense", "The police officer in charge of the detective squad", "The lawyer representing the victim in court", "A judge who signs the official search warrant"], "antwoord": 0, "uitleg": "A suspect is de verdachte."},
    {"type": "waaronwaar", "vraag": "If a defendant is found <b>innocent</b> by a jury, it means they are declared guilty and sent to prison.", "antwoord": False, "uitleg": "Onwaar. Innocent betekent onschuldig."},
    {"type": "invul", "vraag": "Fill in the English word for <i>getuige</i>: <i>The police interviewed an eye-... who saw the robbery take place.</i>", "antwoord": "witness", "uitleg": "An eyewitness is een ooggetuige."},
    {"type": "mc", "vraag": "What does <b>evidence</b> mean in court?", "opties": ["Facts, signs or physical items that prove whether someone is guilty or not", "The uniform worn by high court judges in England", "The fee paid to hire a private defense attorney", "The duration of the trial proceedings"], "antwoord": 0, "uitleg": "Evidence is hard bewijsmateriaal."},
    {"type": "waaronwaar", "vraag": "A <b>clue</b> is a piece of evidence or information that leads detectives closer to solving a crime.", "antwoord": True, "uitleg": "Waar. A clue is een aanwijzing of spoor."},
    {"type": "invul", "vraag": "Fill in the missing noun (dief): <i>The ... escaped through the back alley with the stolen jewels.</i>", "antwoord": "thief|burglar|robber", "uitleg": "Een dief die steelt is in het Engels a thief of a burglar."},
    {"type": "mc", "vraag": "What is the crime of taking items from an open shop without paying called?", "opties": ["Shoplifting", "Burglary", "Robbery", "Kidnapping"], "antwoord": 0, "uitleg": "Shoplifting is winkeldiefstal."},
    {"type": "mc", "vraag": "What is the primary duty of a <b>jury</b> in British and American criminal trials?", "opties": ["To review the evidence and deliver a verdict of guilty or not guilty", "To arrest suspects on the street with handcuffs", "To enforce traffic regulations in the city", "To write new legal statutes in parliament"], "antwoord": 0, "uitleg": "De jury velt het oordeel (schuldig of onschuldig)."},
    {"type": "waaronwaar", "vraag": "<b>Robbery</b> involves stealing from a person or place using violence, physical force, or threats.", "antwoord": True, "uitleg": "Waar. Robbery is diefstal met geweld of bedreiging (overval)."},
    {"type": "invul", "vraag": "Fill in the word for <i>rechter</i>: <i>The ... ordered silence in the courtroom before delivering the sentence.</i>", "antwoord": "judge", "uitleg": "Judge is de rechter."},
    {"type": "mc", "vraag": "What does being held <b>in custody</b> mean for an arrested suspect?", "opties": ["Being kept in protective detention or jail by the police during the investigation", "Being allowed to go on holiday abroad freely", "Receiving a monetary reward from the government", "Working as an undercover police officer"], "antwoord": 0, "uitleg": "In custody betekent in hechtenis op het politiebureau."},
    {"type": "open", "vraag": "Explain the difference between stealing secretly versus taking items through violent threats.", "sleutelwoorden": ["property/belongings/taking/quietly", "violence/threats/force/weapon/attack"], "minTreffers": 1, "modelantwoord": "Theft involves secretly taking someone's property, whereas robbery specifically relies on physical violence or intimidation against a person.", "uitleg": "Theft is diefstal van eigendommen; robbery is een gewelddadige overval met bedreiging."},
    {"type": "mc", "vraag": "What is <b>phishing</b> in modern cybercrime?", "opties": ["Fraudulent emails designed to trick victims into sharing passwords and bank data", "Fishing in prohibited nature lakes during winter", "Installing anti-virus software on school computers", "Selling secondhand computers online"], "antwoord": 0, "uitleg": "Phishing is digitale identiteitsfraude via valse mails."},
    {"type": "waaronwaar", "vraag": "Cybercriminals only operate inside physical bank buildings during daylight hours.", "antwoord": False, "uitleg": "Onwaar. Cybercrime vindt online plaats via computernetwerken over de hele wereld."},
    {"type": "invul", "vraag": "Fill in the noun (rechtszaak): <i>The murder ... lasted for three grueling weeks.</i>", "antwoord": "trial|court case", "uitleg": "A trial is een rechtszaak."},
    {"type": "mc", "vraag": "What is a <b>detective</b>?", "opties": ["A specialized police officer who investigates crimes and gathers evidence", "A security guard working in a shopping mall", "A lawyer defending suspects in court", "A witness who testifies under oath"], "antwoord": 0, "uitleg": "A detective is een rechercheur die misdrijven onderzoekt."},
    {"type": "waaronwaar", "vraag": "DNA samples and fingerprints found at a crime scene are considered physical <b>evidence</b>.", "antwoord": True, "uitleg": "Waar. Vingerafdrukken en DNA zijn fysiek bewijs."},
    {"type": "invul", "vraag": "Fill in the missing word (straf): <i>The judge decided on a severe ... for the criminal.</i>", "antwoord": "punishment|sentence", "uitleg": "Punishment of sentence is de straf."},
    {"type": "mc", "vraag": "Which phrase describes someone who had no involvement in a crime?", "opties": ["Completely innocent", "Proven guilty", "Held in custody", "Under suspicion"], "antwoord": 0, "uitleg": "Completely innocent betekent volkomen onschuldig."}
  ]
}

# EXAMEN 7: H2 Grammar (Past Simple vs Past Continuous) (20 questions)
ex7 = {
  "id": "ex-h3-eng-7",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Hoofdstuk 2 — Crime",
  "titel": "Toets 2 — Grammar: Past Simple vs. Past Continuous",
  "vak": "Engels · HAVO 3 (H2)",
  "icoon": "⏳",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Choose the correct sentence combination:", "opties": ["While the security guard was patrolling the building, he saw a suspicious figure.", "While the security guard patrolled, he was seeing a suspicious figure.", "While the guard is patrolling, he saw a figure yesterday.", "While the guard was patrolled, he saw a figure."], "antwoord": 0, "uitleg": "'While was patrolling' (achtergrondhandeling) werd onderbroken door 'he saw' (korte handeling)."},
    {"type": "mc", "vraag": "Which sentence is correctly in the <b>Past Simple</b>?", "opties": ["The burglar stole three priceless paintings last night.", "The burglar was stealing three paintings last night completely.", "The burglar did stole three paintings.", "The burglar steals three paintings yesterday."], "antwoord": 0, "uitleg": "Past Simple van steal is stole."},
    {"type": "waaronwaar", "vraag": "In negative Past Simple sentences, you use <i>didn't</i> followed by the past tense form (e.g. <i>didn't broke</i>).", "antwoord": False, "uitleg": "Onwaar. Na didn't komt altijd het hele werkwoord (didn't break)."},
    {"type": "invul", "vraag": "Fill in the Past Continuous form of <i>(to sleep)</i>: <i>At midnight, the entire neighborhood ... soundly.</i>", "antwoord": "was sleeping", "uitleg": "Neighborhood (enkelvoud) -> was sleeping."},
    {"type": "mc", "vraag": "Which conjunction is most commonly used right before a <b>Past Continuous</b> clause?", "opties": ["While", "Yesterday", "Ago", "Tomorrow"], "antwoord": 0, "uitleg": "'While' leidt de duurvorm in het verleden in (bijv. While I was watching...)."},
    {"type": "waaronwaar", "vraag": "The sentence <i>'When the alarm went off, the robbers dropped the bag'</i> has both actions in the Past Simple because they happened one after the other.", "antwoord": True, "uitleg": "Waar. Opeenvolgende gebeurtenissen staan beide in de Past Simple."},
    {"type": "invul", "vraag": "Fill in the irregular Past Simple form of <i>(to catch)</i>: <i>The police officer ... the fleeing suspect after a short chase.</i>", "antwoord": "caught", "uitleg": "Catch -> caught."},
    {"type": "mc", "vraag": "Choose the correct form: <i>They ... (to watch) a crime documentary when the power suddenly went out.</i>", "opties": ["were watching", "was watching", "watched", "are watching"], "antwoord": 0, "uitleg": "They -> were watching."},
    {"type": "mc", "vraag": "Why is <i>'What did you saw at the crime scene?'</i> grammatically incorrect?", "opties": ["Did must be followed by the base form 'see', not the past form 'saw'", "You requires the auxiliary verb were instead of did", "Saw can only be used with third-person subjects", "At must be changed to in"], "antwoord": 0, "uitleg": "Na 'did' komt het hele werkwoord: 'What did you see?'."},
    {"type": "waaronwaar", "vraag": "The Past Continuous form for <i>we (to investigate)</i> is <i>we was investigating</i>.", "antwoord": False, "uitleg": "Onwaar. Bij 'we' hoort 'were investigating'."},
    {"type": "invul", "vraag": "Fill in the negative Past Simple form of <i>(to hear)</i>: <i>The witness ... anything suspicious that evening.</i>", "antwoord": "did not hear|didn't hear", "uitleg": "Did not hear / didn't hear."},
    {"type": "mc", "vraag": "Which sentence correctly connects consecutive completed actions in the Past Simple?", "opties": ["The detective arrived at the scene, examined the lock, and interviewed the owner.", "The detective was arriving, was examining, and was interviewing.", "The detective did arrived and examined.", "The detective arrives yesterday at noon."], "antwoord": 0, "uitleg": "Een reeks opeenvolgende voltooide handelingen staat in de Past Simple."},
    {"type": "open", "vraag": "Explain why the Past Continuous is used in: <i>'At 10 PM last night, I was studying for my English exam.'</i>", "sleutelwoorden": ["in progress/ongoing/happening/specific time/past"], "minTreffers": 1, "modelantwoord": "The Past Continuous is used because the action was ongoing/in progress at that exact specific moment in the past (10 PM).", "uitleg": "De Past Continuous geeft aan dat de handeling op dat exacte tijdstip in het verleden aan de gang was."},
    {"type": "mc", "vraag": "Choose the correct verb form: <i>While the detective ... (to examine) the footprints, it started to rain.</i>", "opties": ["was examining", "examined", "were examining", "is examining"], "antwoord": 0, "uitleg": "Detective (he/she) -> was examining."},
    {"type": "waaronwaar", "vraag": "The word <i>ago</i> always points to a finished time in the past and requires the Past Simple (e.g. <i>two days ago</i>).", "antwoord": True, "uitleg": "Waar. 'Ago' is een vast signaalwoord voor de Past Simple."},
    {"type": "invul", "vraag": "Fill in the irregular Past Simple form of <i>(to find)</i>: <i>Forensic experts ... the missing weapon in the bushes.</i>", "antwoord": "found", "uitleg": "De onregelmatige verleden tijd van to find is found."},
    {"type": "mc", "vraag": "Which question is formed correctly in the <b>Past Continuous</b>?", "opties": ["Were you waiting for the bus when the accident happened?", "Did you was waiting for the bus?", "Was you waiting for the bus?", "Are you waiting for the bus yesterday?"], "antwoord": 0, "uitleg": "'Were you waiting' is de correcte vraagvorm voor you in de Past Continuous."},
    {"type": "waaronwaar", "vraag": "In the sentence <i>'I didn't saw him'</i>, the grammar is completely correct.", "antwoord": False, "uitleg": "Onwaar. Het moet zijn: 'I didn't see him'."},
    {"type": "invul", "vraag": "Fill in the correct form of <i>(to drive)</i>: <i>The suspect ... a stolen black car when the police stopped him.</i>", "antwoord": "was driving", "uitleg": "Suspect (he) -> was driving."},
    {"type": "mc", "vraag": "What is the past simple of <b>to leave</b>?", "opties": ["Left", "Leaved", "Was left", "Leaving"], "antwoord": 0, "uitleg": "De onregelmatige verleden tijd van to leave is left."}
  ]
}

# EXAMEN 8: H2 Stones & Police Reporting (20 questions)
ex8 = {
  "id": "ex-h3-eng-8",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Hoofdstuk 2 — Crime",
  "titel": "Toets 3 — Stones & Skills: Incident Reporting & Statements",
  "vak": "Engels · HAVO 3 (H2)",
  "icoon": "🚨",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "How do you politely state your purpose at an English police reception desk?", "opties": ["I would like to report an incident, please.", "Give me some money immediately.", "Why is this police station open?", "Where are the criminals kept?"], "antwoord": 0, "uitleg": "'I would like to report an incident' is de juiste professionele opening."},
    {"type": "mc", "vraag": "Which phrase correctly describes a suspect's build?", "opties": ["He was tall, with broad shoulders and an athletic build.", "He was built from heavy wooden planks.", "He weighed 400 seasons.", "His construction was very fast."], "antwoord": 0, "uitleg": "'Athletic build' beschrijft een sportief en gespierd postuur."},
    {"type": "waaronwaar", "vraag": "A <b>tattoo</b> is a permanent design or mark made on skin with ink.", "antwoord": True, "uitleg": "Waar. Een tattoo is een permanente huidtekening."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>The victim requested a copy of the police ... for insurance claims.</i>", "antwoord": "report", "uitleg": "Police report is het proces-verbaal / politieverslag."},
    {"type": "mc", "vraag": "How do you describe someone's approximate age in English?", "opties": ["She appeared to be in her late twenties.", "She was having 28 years.", "She counted 28 winters.", "Her age was made of 28."], "antwoord": 0, "uitleg": "'In her late twenties' is de natuurlijke Engelse formulering."},
    {"type": "waaronwaar", "vraag": "A <b>scar</b> on someone's face is a temporary piece of makeup that washes away with water.", "antwoord": False, "uitleg": "Onwaar. Een scar is een permanent litteken."},
    {"type": "invul", "vraag": "Fill in the preposition: <i>The incident took place ... approximately 4:30 PM.</i>", "antwoord": "at", "uitleg": "Bij een specifiek tijdstip gebruik je 'at'."},
    {"type": "mc", "vraag": "What is the best way to describe what a suspect was wearing?", "opties": ["He was wearing a grey hoodie, dark jeans, and white trainers.", "He dressed himself into blue trousers yesterday.", "His clothing was having shoes.", "He had a shirt on his body."], "antwoord": 0, "uitleg": "'He was wearing...' is de standaard uitdrukking voor kledingbeschrijvingen."},
    {"type": "mc", "vraag": "Which question would a police officer ask a witness to identify the time of an event?", "opties": ["What time did you first notice anything unusual?", "What is your favorite television series?", "Can you cook dinner for us?", "Where did you buy your jacket?"], "antwoord": 0, "uitleg": "Dit vraagt naar het exacte tijdstip van verdachte observaties."},
    {"type": "waaronwaar", "vraag": "In a formal witness statement, presenting events out of order without dates is considered best practice.", "antwoord": False, "uitleg": "Onwaar. Een getuigenverklaring moet strikt chronologisch en nauwkeurig zijn."},
    {"type": "invul", "vraag": "Complete the phrase: <i>The suspect fled on foot towards the main railway ... .</i>", "antwoord": "station", "uitleg": "Railway station is het treinstation."},
    {"type": "mc", "vraag": "What does the expression <i>'to flee on foot'</i> mean?", "opties": ["To run away on one's own feet instead of using a vehicle", "To walk slowly while holding hands", "To buy new athletic shoes", "To climb a tree for safety"], "antwoord": 0, "uitleg": "'Flee on foot' betekent te voet wegvluchten."},
    {"type": "open", "vraag": "Write a short physical description of a suspect based on: age (mid-30s), hair (short dark), clothing (blue jacket).", "sleutelwoorden": ["mid-thirties/30s/jacket/hair/wearing"], "minTreffers": 1, "modelantwoord": "The suspect was in his mid-thirties, with short dark hair, and was wearing a blue jacket.", "uitleg": "Een complete beschrijving combineert leeftijd, haar en kleding helder."},
    {"type": "mc", "vraag": "Which phrase expresses that you did not see clearly due to darkness?", "opties": ["It was too dark to get a clear look at his face.", "I closed my eyes because I was sleepy.", "The lights were so bright I had to wear sunglasses.", "I wasn't interested in looking."], "antwoord": 0, "uitleg": "Dit verklaart duidelijk waarom de getuige het gezicht niet goed kon zien."},
    {"type": "waaronwaar", "vraag": "Emergency services in the UK can be contacted by dialing 999.", "antwoord": True, "uitleg": "Waar. In het Verenigd Koninkrijk is 999 het alarmnummer."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>Can you give a detailed ... of the vehicle?</i>", "antwoord": "description", "uitleg": "A detailed description is een gedetailleerde beschrijving."},
    {"type": "mc", "vraag": "What is meant by a <i>distinguishing feature</i> on a suspect?", "opties": ["A unique mark such as a scar, tattoo, or birthmark that makes identification easier", "A standard pair of black socks", "The price tag on their jacket", "A generic hairstyle shared by millions"], "antwoord": 0, "uitleg": "Een opvallend uiterlijk kenmerk (litteken, tatoeage) helpt bij identificatie."},
    {"type": "waaronwaar", "vraag": "The word <i>hoodie</i> refers to a vehicle used exclusively by police detectives.", "antwoord": False, "uitleg": "Onwaar. Een hoodie is een trui met capuchon."},
    {"type": "invul", "vraag": "Complete the phrase: <i>The car was heading north towards the ... .</i>", "antwoord": "motorway|highway|city", "uitleg": "Motorway / highway (snelweg)."},
    {"type": "mc", "vraag": "What does a witness confirm when signing their official statement?", "opties": ["That the recorded information is true and accurate to the best of their memory", "That they agree to pay for the police investigation", "That they will appear on television tomorrow", "That they want to become a police officer"], "antwoord": 0, "uitleg": "Ondertekening bevestigt dat de verklaring naar waarheid is afgelegd."}
  ]
}

# EXAMEN 9: H2 Reading & Mystery Analysis (20 questions)
ex9 = {
  "id": "ex-h3-eng-9",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Hoofdstuk 2 — Crime",
  "titel": "Toets 4 — Reading Skills: Crime Fiction & Investigative Texts",
  "vak": "Engels · HAVO 3 (H2)",
  "icoon": "🕵️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "What is a <b>red herring</b> in detective mystery stories?", "opties": ["A misleading clue designed to distract investigators and readers from the real culprit", "A type of fish eaten by detectives during stakeouts", "A red signal light on a police car", "A special code used to unlock police computers"], "antwoord": 0, "uitleg": "Een red herring is een dwaalspoor in een detectiveverhaal."},
    {"type": "mc", "vraag": "What does the term <b>alibi</b> mean for a criminal suspect?", "opties": ["Evidence proving that the person was in a different place when the crime occurred", "The confession signed by the guilty party", "The secret nickname of a detective", "A monetary fine paid to avoid trial"], "antwoord": 0, "uitleg": "Een alibi bewijst dat de verdachte ten tijde van het misdrijf ergens anders was."},
    {"type": "waaronwaar", "vraag": "In mystery stories, the <b>motive</b> explains why someone would want to commit a particular crime.", "antwoord": True, "uitleg": "Waar. Het motief verklaart de beweegreden achter het misdrijf."},
    {"type": "invul", "vraag": "Fill in the literary term (motief): <i>Detectives searched for a financial ... behind the sudden theft.</i>", "antwoord": "motive", "uitleg": "Motive is het motief."},
    {"type": "mc", "vraag": "What is the <b>climax</b> of a detective story?", "opties": ["The most intense, dramatic turning point where the mystery is finally unraveled", "The list of copyright details on the first page", "The biographical note about the author", "The price printed on the back cover"], "antwoord": 0, "uitleg": "De climax is het hoogtepunt waarin het mysterie wordt ontrafeld."},
    {"type": "waaronwaar", "vraag": "A <b>culprit</b> is the person responsible for committing the crime or wrongdoing.", "antwoord": True, "uitleg": "Waar. Culprit betekent de dader / schuldige."},
    {"type": "invul", "vraag": "Fill in the noun (dwaalspoor): <i>The torn receipt was just a clever red ... planted by the burglar.</i>", "antwoord": "herring", "uitleg": "Red herring is een dwaalspoor."},
    {"type": "mc", "vraag": "Which phrase describes reading between the lines to deduce hidden meaning?", "opties": ["Making an inference", "Reading out loud", "Copying words", "Memorizing verbs"], "antwoord": 0, "uitleg": "'Making an inference' is het trekken van conclusies uit impliciete aanwijzingen."},
    {"type": "mc", "vraag": "What does a <b>forensic scientist</b> do in an investigation?", "opties": ["Applies scientific methods to analyze physical evidence like hair, glass, and DNA", "Arrests criminals in high-speed car pursuits", "Interviews journalists on television", "Sells security alarm systems"], "antwoord": 0, "uitleg": "Forensische experts analyseren fysiek bewijsmateriaal wetenschappelijk."},
    {"type": "waaronwaar", "vraag": "An anonymous tip means that the person providing information refuses to reveal their identity.", "antwoord": True, "uitleg": "Waar. Anoniem betekent zonder naam."},
    {"type": "invul", "vraag": "Fill in the term (alibi): <i>His boss confirmed his ...: he was at work until 6 PM.</i>", "antwoord": "alibi", "uitleg": "Alibi is het alibi."},
    {"type": "mc", "vraag": "Why are transition words like <i>meanwhile, suddenly, consequently</i> important in crime narratives?", "opties": ["They clarify the timeline and cause-effect connections between simultaneous events", "They make the font size appear larger", "They replace nouns in all dialogue", "They translate the story into German"], "antwoord": 0, "uitleg": "Signaalwoorden maken de chronologie en spanningsopbouw helder."},
    {"type": "open", "vraag": "Why is establishing an accurate chronological sequence of hours essential for detectives solving a mystery?", "sleutelwoorden": ["verify/check/confirm/whereabouts", "suspect/alibi/present/evidence"], "minTreffers": 1, "modelantwoord": "An accurate timeline allows detectives to verify suspects' alibis and determine who was present at the crime scene.", "uitleg": "Een tijdlijn maakt het mogelijk om alibi's te controleren en verdachten uit te sluiten."},
    {"type": "mc", "vraag": "What does <b>circumstantial evidence</b> mean?", "opties": ["Evidence that relies on an inference to connect it to a conclusion of fact", "A signed confession with video proof", "A confession made directly in front of the judge", "Fingerprints found directly on the murder weapon"], "antwoord": 0, "uitleg": "Indirect bewijs (circumstantial) wijst op een vermoeden maar levert geen 100% direct bewijs."},
    {"type": "waaronwaar", "vraag": "In classic detective fiction by Arthur Conan Doyle, Sherlock Holmes uses deduction to solve complex mysteries.", "antwoord": True, "uitleg": "Waar. Sherlock Holmes staat bekend om zijn logische deductie."},
    {"type": "invul", "vraag": "Fill in the noun (dader): <i>The detective finally unmasked the true ... in the final chapter.</i>", "antwoord": "culprit|criminal", "uitleg": "Culprit / criminal is de dader."},
    {"type": "mc", "vraag": "Which phrase describes a sudden unexpected plot development in a mystery?", "opties": ["A plot twist", "A chapter heading", "A table of contents", "A glossary term"], "antwoord": 0, "uitleg": "A plot twist is een onverwachte wending in het verhaal."},
    {"type": "waaronwaar", "vraag": "A <b>motive</b> is always purely accidental and never involves emotions like jealousy, greed, or revenge.", "antwoord": False, "uitleg": "Onwaar. Motieven zijn vaak gebaseerd op hebzucht, jaloezie of wraak."},
    {"type": "invul", "vraag": "Complete the phrase: <i>The detective searched for a missing ... in the chain of events.</i>", "antwoord": "link", "uitleg": "A missing link is een ontbrekende schakel."},
    {"type": "mc", "vraag": "What is the tone of a formal crime report written for an insurance company?", "opties": ["Objective, factual and precise", "Emotional, dramatic and poetic", "Casual and humorous with slang", "Angry and demanding"], "antwoord": 0, "uitleg": "Een officieel schaderapport moet objectief en feitelijk zijn."}
  ]
}

# EXAMEN 10: H2 Hoofdstuk Eindtoets (Mix & Sınav Simülasyonu) (20 questions)
ex10 = {
  "id": "ex-h3-eng-10",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Hoofdstuk 2 — Crime",
  "titel": "Toets 5 — Hoofdstuk 2 Eindtoets (Mix & Examen)",
  "vak": "Engels · HAVO 3 (H2)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "What is the key difference between <b>theft</b> and <b>burglary</b>?", "opties": ["Burglary specifically involves illegally entering a building or house to steal", "Theft is only punishable by community service", "Burglary is committed strictly outdoors in public parks", "There is no distinction in criminal law"], "antwoord": 0, "uitleg": "Burglary is inbraak in een pand."},
    {"type": "mc", "vraag": "Choose the correct verb combination: <i>While the alarm ... (to ring), the thieves ... (to flee) through the emergency exit.</i>", "opties": ["was ringing / fled", "rang / were fleeing", "is ringing / flee", "was rung / fled"], "antwoord": 0, "uitleg": "Was ringing (duurvorm) + fled (korte voltooide actie)."},
    {"type": "waaronwaar", "vraag": "In an English court, the <b>jury</b> decides whether the defendant is guilty or innocent.", "antwoord": True, "uitleg": "Waar. De jury velt het vonnis over schuld."},
    {"type": "invul", "vraag": "Fill in the English word for <i>litteken</i>: <i>The suspect had a noticeable ... on his left cheek.</i>", "antwoord": "scar", "uitleg": "Scar is een litteken."},
    {"type": "mc", "vraag": "Which phrase is used to give a formal report of a crime at a police station?", "opties": ["I'd like to report a burglary, please.", "Can you give me free transport home?", "Why are you wearing a police badge?", "I want to visit the cell block."], "antwoord": 0, "uitleg": "'I'd like to report a burglary' is de correcte opening."},
    {"type": "waaronwaar", "vraag": "A suspect who has a solid <b>alibi</b> was definitely present at the scene of the crime when it occurred.", "antwoord": False, "uitleg": "Onwaar. Een alibi bewijst juist dat de verdachte ergens anders was."},
    {"type": "invul", "vraag": "Fill in the Past Simple of <i>(to break)</i>: <i>Someone ... into the school office last Friday.</i>", "antwoord": "broke", "uitleg": "Break into -> broke into."},
    {"type": "mc", "vraag": "What does being found <b>guilty</b> mean?", "opties": ["Being legally convicted of committing the crime", "Being awarded a financial compensation", "Being cleared of all charges immediately", "Being invited to join the jury"], "antwoord": 0, "uitleg": "Guilty betekent schuldig bevonden."},
    {"type": "mc", "vraag": "Choose the correct Past Continuous sentence:", "opties": ["The detective was inspecting the crime scene when the rain started.", "The detective were inspecting the crime scene yesterday.", "The detective did inspecting the room.", "The detective was inspect the scene."], "antwoord": 0, "uitleg": "Detective (he) -> was inspecting."},
    {"type": "waaronwaar", "vraag": "DNA evidence and fingerprints are examples of physical <b>evidence</b>.", "antwoord": True, "uitleg": "Waar. Dit is fysiek bewijs."},
    {"type": "invul", "vraag": "Fill in the noun (getuige): <i>The key ... identified the suspect in a police line-up.</i>", "antwoord": "witness", "uitleg": "Witness is getuige."},
    {"type": "mc", "vraag": "What is a <b>red herring</b> in a detective story?", "opties": ["A false clue designed to lead investigators in the wrong direction", "A special police siren color", "A delicious fish dinner for the team", "A type of forensic fingerprint powder"], "antwoord": 0, "uitleg": "Een dwaalspoor in een mysterie."},
    {"type": "open", "vraag": "Why is it crucial for an eyewitness to give their statement as soon as possible after an incident?", "sleutelwoorden": ["fresh/memory/forget/details/accurate/clear"], "minTreffers": 1, "modelantwoord": "Memories fade quickly, so giving a statement immediately ensures the details are fresh, accurate, and reliable.", "uitleg": "Herinneringen vervagen snel; direct verslag doen waarborgt de betrouwbaarheid van details."},
    {"type": "mc", "vraag": "Choose the correct negative Past Simple sentence:", "opties": ["The witness didn't recognize the driver of the car.", "The witness didn't recognized the driver.", "The witness wasn't recognize the driver.", "The witness don't recognized the car."], "antwoord": 0, "uitleg": "Didn't + hele werkwoord (recognize)."},
    {"type": "waaronwaar", "vraag": "The word <b>phishing</b> refers to traditional deep-sea fishing with wooden rods in Scotland.", "antwoord": False, "uitleg": "Onwaar. Phishing is online identiteitsfraude."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>The suspect was held in police ... overnight.</i>", "antwoord": "custody", "uitleg": "In custody betekent in hechtenis."},
    {"type": "mc", "vraag": "How do you describe someone wearing a garment with a hood?", "opties": ["He was wearing a hoodie.", "He was having a cape.", "He dressed in blankets.", "He held an umbrella."], "antwoord": 0, "uitleg": "A hoodie is een capuchontrui."},
    {"type": "waaronwaar", "vraag": "The emergency phone number for police, ambulance and fire brigade in the UK is 999.", "antwoord": True, "uitleg": "Waar. 999 is het Britse alarmnummer."},
    {"type": "invul", "vraag": "Complete the phrase: <i>The burglar fled on ... towards the metro.</i>", "antwoord": "foot", "uitleg": "'On foot' (te voet)."},
    {"type": "mc", "vraag": "What is the <b>culprit</b> in an investigation?", "opties": ["The person who committed the crime", "The police chief", "The innocent bystander", "The judge's assistant"], "antwoord": 0, "uitleg": "Culprit is de dader."}
  ]
}

write_examen("examen_6.js", ex6)
write_examen("examen_7.js", ex7)
write_examen("examen_8.js", ex8)
write_examen("examen_9.js", ex9)
write_examen("examen_10.js", ex10)
print("Hoofdstuk 2 exams (6 to 10) generated successfully!")
