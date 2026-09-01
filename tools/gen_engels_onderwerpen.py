#!/usr/bin/env python3
"""
Generates all 18 Onderwerpen (Theory & Oefenquizzes) for HAVO 3 Engels (Stepping Stones)
- Hoofdstuk 1: The world around you (1.1, 1.2, 1.3)
- Hoofdstuk 2: Crime (2.1, 2.2, 2.3)
- Hoofdstuk 3: Science & technology (3.1, 3.2, 3.3)
- Hoofdstuk 4: To the extreme (4.1, 4.2, 4.3)
- Hoofdstuk 5: Going green (5.1, 5.2, 5.3)
- Hoofdstuk 6: Your future (6.1, 6.2, 6.3)
"""

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

def write_onderwerp(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    content = f"""/* Onderwerp {data['paragraaf']} — {data['titel']}
   Stepping Stones 3 HAVO Hoofdstuk {data['hoofdstuk']} */
DURU.register({json.dumps(data, indent=2, ensure_ascii=False)});
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [✓] Onderwerp saved: {filename}")

# ==========================================
# 1. THE WORLD AROUND YOU
# ==========================================
h1_1 = {
  "id": "eng-h1-1",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Theme Words: Culture, Identity & Customs",
  "korteUitleg": "Kernwoorden over cultuur, tradities, internationale vriendschappen en identiteit.",
  "icoon": "🌍",
  "kleur": "h1-thema",
  "theorie": """
    <h3>1.1 Theme Words: Culture, Identity & Customs</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Culture, customs, tradition, multicultural, identity, diversity, community, foreign, exchange student, destination, stereotype, impression, global, habit, hospitality, heritage, background, fluent, native speaker.
    </div>
    <h4>1. Woordenschat: Cultuur en Samenleving</h4>
    <p>In dit hoofdstuk leer je hoe je in het Engels praat over verschillende culturen, gewoontes en je eigen achtergrond:</p>
    <table class="theorie-tabel">
      <tr><th>Engels Begrip</th><th>Nederlandse Betekenis</th><th>Voorbeeldzin</th></tr>
      <tr><td><b>Culture</b></td><td>Cultuur</td><td>Every country has its own unique <i>culture</i> and values.</td></tr>
      <tr><td><b>Customs / Traditions</b></td><td>Gewoontes / Tradities</td><td>Eating turkey at Thanksgiving is an American <i>tradition</i>.</td></tr>
      <tr><td><b>Multicultural</b></td><td>Multicultureel</td><td>London is a vibrant, <i>multicultural</i> city with people from all over the world.</td></tr>
      <tr><td><b>Identity</b></td><td>Identiteit</td><td>Your language and roots are an essential part of your personal <i>identity</i>.</td></tr>
      <tr><td><b>Diversity</b></td><td>Diversiteit / Verscheidenheid</td><td>Our school celebrates cultural <i>diversity</i> during International Week.</td></tr>
      <tr><td><b>Hospitality</b></td><td>Gastvrijheid</td><td>We were touched by the warm <i>hospitality</i> of our host family in Ireland.</td></tr>
      <tr><td><b>Stereotype</b></td><td>Stereotype / Vooroordeel</td><td>It is a common <i>stereotype</i> that all Dutch people wear wooden clogs.</td></tr>
      <tr><td><b>Heritage</b></td><td>Erfgoed / Achtergrond</td><td>She is proud of her Scottish <i>heritage</i> and family history.</td></tr>
    </table>
    <h4>2. Reizen en Internationale Vriendschappen</h4>
    <p>Handige woorden wanneer je naar het buitenland reist of buitenlandse scholieren ontmoet:</p>
    <ul>
      <li><b>Exchange student:</b> Een uitwisselingsstudent die tijdelijk op een buitenlandse school studeert.</li>
      <li><b>Destination:</b> De bestemming van je reis (bijv. <i>Our final destination is Edinburgh</i>).</li>
      <li><b>Fluent:</b> Vloeiend een taal spreken (<i>She is fluent in both English and Dutch</i>).</li>
      <li><b>Native speaker:</b> Iemand die een taal als moedertaal spreekt.</li>
      <li><b>Habit:</b> Een dagelijkse gewoonte of routine.</li>
    </ul>
    <h4>3. Tips voor Woordenschatverwerving</h4>
    <p>Leer woorden altijd in een contextzin en let op woordcombinaties (collocations) zoals <i>make an impression</i>, <i>experience a culture shock</i> en <i>show great hospitality</i>.</p>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "What is the English word for <i>gastvrijheid</i>?", "opties": ["Hospitality", "Heritage", "Diversity", "Stereotype"], "antwoord": 0, "uitleg": "Hospitality betekent gastvrijheid."},
    {"type": "mc", "niveau": 1, "vraag": "Which word describes a fixed, oversimplified image or idea of a particular type of person or group?", "opties": ["Destination", "Stereotype", "Custom", "Habit"], "antwoord": 1, "uitleg": "A stereotype is een stereotiep beeld of generalisatie."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "A <b>native speaker</b> is someone who learned a language as a foreign language in high school.", "antwoord": False, "uitleg": "Onwaar. A native speaker heeft de taal als moedertaal geleerd."},
    {"type": "invoer", "niveau": 1, "vraag": "Complete the sentence with the correct noun (verscheidenheid): <i>The festival celebrated cultural ... in the city.</i>", "antwoord": "diversity", "uitleg": "Diversity betekent verscheidenheid of diversiteit."},
    {"type": "mc", "niveau": 2, "vraag": "What does the word <b>heritage</b> refer to?", "opties": ["The traditions, languages and achievements passed down through generations", "A daily train schedule for commuters", "A type of passport for exchange students", "An expensive hotel in a foreign capital"], "antwoord": 0, "uitleg": "Heritage verwijst naar cultureel erfgoed en familietradities."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "If you are <b>fluent</b> in English, you can speak and understand the language easily and smoothly.", "antwoord": True, "uitleg": "Waar. Fluent betekent vloeiend."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the missing word: <i>A student who goes abroad to study at a partner school is an ... student.</i>", "antwoord": "exchange|exchange student", "uitleg": "Exchange student is de juiste term."},
    {"type": "mc", "niveau": 3, "vraag": "Choose the best synonym for <b>custom</b> in this context: <i>It is a local custom to shake hands when greeting someone.</i>", "opties": ["Tradition", "Airport", "Passport", "Accident"], "antwoord": 0, "uitleg": "Custom betekent gewoonte of traditie (tradition)."}
  ]
}

h1_2 = {
  "id": "eng-h1-2",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Grammar: Present Simple vs. Present Continuous",
  "korteUitleg": "Het verschil tussen gewoontes/feiten (Present Simple) en bezigheden die nu plaatsvinden (Continuous).",
  "icoon": "⏱️",
  "kleur": "h1-thema",
  "theorie": """
    <h3>1.2 Grammar: Present Simple vs. Present Continuous</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> Present Simple (feiten, gewoontes, routines) vs. Present Continuous (nu bezig, tijdelijk), signaalwoorden en toestandswerkwoorden (state verbs).
    </div>
    <h4>1. Present Simple (O.T.T.)</h4>
    <p>Je gebruikt de <b>Present Simple</b> voor:</p>
    <ul>
      <li><b>Feiten en algemene waarheden:</b> <i>The sun rises in the east. Dutch people love cycling.</i></li>
      <li><b>Gewoontes, routines en regelmaat:</b> <i>I always brush my teeth before bed. She practices piano on Mondays.</i></li>
      <li><b>Vaste dienstregelingen:</b> <i>The train departs at 08:30.</i></li>
    </ul>
    <p><b>Vorm:</b> He/She/It krijgt <b>stam + s</b> (shit-regel). Vragen en ontkenningen maken met <b>do / does</b> + hele werkwoord:</p>
    <ul>
      <li><i>Positive:</i> He live<b>s</b> in Utrecht.</li>
      <li><i>Negative:</i> He <b>does not (doesn't) live</b> in Utrecht.</li>
      <li><i>Question:</i> <b>Does</b> he <b>live</b> in Utrecht?</li>
    </ul>
    <p><b>Signaalwoorden:</b> <i>always, usually, often, sometimes, rarely, never, every day/week, on Fridays</i>.</p>
    <h4>2. Present Continuous (Duurvorm)</h4>
    <p>Je gebruikt de <b>Present Continuous</b> voor:</p>
    <ul>
      <li><b>Acties die nu op dit moment bezig zijn:</b> <i>Look! Duru is reading her English book.</i></li>
      <li><b>Tijdelijke situaties:</b> <i>He is staying with an English host family this week.</i></li>
    </ul>
    <p><b>Vorm:</b> Vorm van <b>to be (am / is / are) + werkwoord-ing</b>.</p>
    <ul>
      <li><i>Positive:</i> They <b>are studying</b> for their test right now.</li>
      <li><i>Negative:</i> She <b>is not (isn't) watching</b> TV at the moment.</li>
      <li><i>Question:</i> <b>Are</b> you <b>listening</b> to me?</li>
    </ul>
    <p><b>Signaalwoorden:</b> <i>now, at the moment, currently, right now, Look!, Listen!</i>.</p>
    <h4>3. Toestandswerkwoorden (State Verbs)</h4>
    <p>Werkwoorden van gevoel, mening of bezit staan vrijwel nooit in de continuous (geen -ing):</p>
    <p><i>like, love, hate, know, understand, believe, want, need, prefer, belong, remember</i>.<br>
    ✅ <i>I <b>understand</b> this rule.</i> (NIET: <s>I am understanding</s>)</p>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which sentence is in the correct <b>Present Continuous</b> form?", "opties": ["Listen! The birds are singing outside.", "Listen! The birds sings outside.", "Listen! The birds is singing outside.", "Listen! The birds sing outside right now."], "antwoord": 0, "uitleg": "The birds is meervoud (are) + singing. 'Listen!' is het signaalwoord."},
    {"type": "mc", "niveau": 1, "vraag": "Choose the correct verb form: <i>My brother always ... his homework before dinner.</i>", "opties": ["finishes", "is finishing", "finish", "are finishing"], "antwoord": 0, "uitleg": "'Always' geeft een gewoonte aan (Present Simple). My brother (he) krijgt stam + es."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "Verbs of emotion and thought like <i>know, believe, like</i> are regularly used in the Present Continuous form with -ing.", "antwoord": False, "uitleg": "Onwaar. Dit zijn state verbs en staan in de Present Simple."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the correct form of the verb <i>(to play)</i>: <i>Look! The children ... football in the garden right now.</i>", "antwoord": "are playing", "uitleg": "Children is meervoud, en 'right now' vraagt om de continuous: are playing."},
    {"type": "mc", "niveau": 2, "vraag": "Which question is grammatically correct in the <b>Present Simple</b>?", "opties": ["Does your sister speak Spanish fluently?", "Do your sister speaks Spanish fluently?", "Is your sister speak Spanish fluently?", "Does your sister speaks Spanish fluently?"], "antwoord": 0, "uitleg": "Bij 'your sister' (she) gebruik je 'Does' + het hele werkwoord (speak)."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "The sentence <i>'Water boils at 100 degrees Celsius'</i> is in the Present Simple because it states a scientific fact.", "antwoord": True, "uitleg": "Waar. Algemene feiten en natuurwetten staan in de Present Simple."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the negative Present Simple form of <i>(to like)</i>: <i>Emma ... spicy food.</i>", "antwoord": "does not like|doesn't like", "uitleg": "Emma (she) -> does not like / doesn't like."},
    {"type": "mc", "niveau": 3, "vraag": "Why is <i>'I am knowing the answer'</i> incorrect in standard English?", "opties": ["Because 'know' is a state verb and is not used in the continuous form", "Because the subject 'I' always requires an -s ending", "Because continuous requires the auxiliary verb 'do'", "Because 'knowing' is an irregular past participle"], "antwoord": 0, "uitleg": "'Know' is een toestandswerkwoord en staat in de Simple: 'I know the answer'."}
  ]
}

h1_3 = {
  "id": "eng-h1-3",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Stones & Skills: Social Interaction & Informal Writing",
  "korteUitleg": "Vaste spreekstenen (Stones) voor kennismaken, meningen vragen/geven en informele e-mails.",
  "icoon": "💬",
  "kleur": "h1-thema",
  "theorie": """
    <h3>1.3 Stones & Skills: Social Interaction & Informal Writing</h3>
    <div class="info-box">
      <b>Communicatieve vaardigheden:</b> Speaking Stones voor kennismaken, je mening formuleren, beleefd vragen stellen en de opbouw van een informele e-mail.
    </div>
    <h4>1. Speaking Stones: Kennismaken en Voorstellen</h4>
    <p>Gebruik deze vaste Engelse zinnen in gesprekken met leeftijdgenoten of gastgezinnen:</p>
    <ul>
      <li><i>Let me introduce myself: my name is Duru and I'm from the Netherlands.</i></li>
      <li><i>Nice to meet you! / Pleased to meet you!</i></li>
      <li><i>Where are you from originally?</i></li>
      <li><i>What do you like doing in your free time?</i></li>
      <li><i>I'm really into sports and photography.</i></li>
    </ul>
    <h4>2. Speaking Stones: Meningen Vragen en Geven</h4>
    <table class="theorie-tabel">
      <tr><th>Mening Vragen</th><th>Mening Geven</th><th>Instemmen / Oneens zijn</th></tr>
      <tr><td>What do you think of...?</td><td>In my opinion,...</td><td>I completely agree with you.</td></tr>
      <tr><td>How do you feel about...?</td><td>As far as I'm concerned,...</td><td>That's a very good point.</td></tr>
      <tr><td>Do you agree that...?</td><td>Personally, I believe that...</td><td>I see what you mean, but...</td></tr>
    </table>
    <h4>3. Schrijfvaardigheid: De Informele E-mail</h4>
    <p>Een informele e-mail aan een penvriend(in) of uitwisselingsstudent heeft een vaste structuur:</p>
    <ul>
      <li><b>Aanhef (Greeting):</b> <i>Hi Liam, / Dear Sarah,</i> (met een komma!)</li>
      <li><b>Openingszin (Opening):</b> <i>Thanks for your email! How are things? / I hope you're doing well.</i></li>
      <li><b>Hoofdtekst (Body):</b> Verdeel je verhaal in duidelijke alinea's (bijv. school, hobby's, plannen).</li>
      <li><b>Afsluiting (Closing phrase):</b> <i>Let me know what you think. / Write back soon! / Hope to hear from you.</i></li>
      <li><b>Ondertekening (Sign-off):</b> <i>Best wishes, / All the best, / Take care,</i> gevolgd door je voornaam.</li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which phrase is the most appropriate opening for an <b>informal</b> email to an exchange student?", "opties": ["Hi Chloe, thanks for your message! How are you doing?", "Dear Sir or Madam, I am writing to inform you...", "To whom it may concern,", "Yours sincerely, Mr. Johnson"], "antwoord": 0, "uitleg": "'Hi Chloe,...' is vriendelijk, informeel en perfect voor een leeftijdgenoot."},
    {"type": "mc", "niveau": 1, "vraag": "How do you politely express that you agree with someone's opinion?", "opties": ["I completely agree with you on that.", "You are entirely mistaken.", "I don't care at all.", "Why are you saying that?"], "antwoord": 0, "uitleg": "'I completely agree with you on that' toont duidelijke instemming."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "The phrase <i>'In my opinion, school uniforms create a sense of unity'</i> is used to express a personal viewpoint.", "antwoord": True, "uitleg": "Waar. 'In my opinion' leidt een persoonlijke mening in."},
    {"type": "invoer", "niveau": 1, "vraag": "Complete the phrase to introduce yourself: <i>Let me ... myself: my name is Duru.</i>", "antwoord": "introduce", "uitleg": "'Introduce' (voorstellen) completeert de vaste spreeksteen."},
    {"type": "mc", "niveau": 2, "vraag": "Which of the following is a polite way to <b>disagree</b> in a discussion?", "opties": ["I see what you mean, but I look at it differently.", "That makes no sense whatsoever.", "Shut up, you don't know anything.", "I refuse to listen to your opinion."], "antwoord": 0, "uitleg": "'I see what you mean, but...' toont respect en formuleert een tegenargument."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "In an informal email, you should finish with <i>'Yours faithfully,'</i> followed by your full legal name.", "antwoord": False, "uitleg": "Onwaar. 'Yours faithfully' is zeer formeel. Informeel gebruik je 'Best wishes,' of 'Take care,'."},
    {"type": "invoer", "niveau": 2, "vraag": "Complete the informal sign-off: <i>Hope to hear from you soon. Take ...!</i>", "antwoord": "care", "uitleg": "'Take care' (pas goed op jezelf) is een vaste afsluiting."},
    {"type": "mc", "niveau": 3, "vraag": "What is the primary function of the phrase <i>'As far as I'm concerned'</i>?", "opties": ["To introduce a personal perspective or opinion", "To ask for driving directions in a new city", "To complain about bad hotel service", "To order food in a restaurant"], "antwoord": 0, "uitleg": "'As far as I'm concerned' betekent 'wat mij betreft'."}
  ]
}

# ==========================================
# 2. CRIME
# ==========================================
h2_1 = {
  "id": "eng-h2-1",
  "hoofdstuk": 2,
  "paragraaf": "2.1",
  "titel": "Theme Words: Crime, Law & Investigation",
  "korteUitleg": "Kernbegrippen rond misdaad, politieonderzoek, rechtbank en digitale criminaliteit.",
  "icoon": "🔍",
  "kleur": "h2-thema",
  "theorie": """
    <h3>2.1 Theme Words: Crime, Law & Investigation</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Suspect, witness, evidence, investigation, detective, clue, criminal, theft, burglary, robbery, judge, court, jury, trial, guilty, innocent, punishment, custody, fraud, cybercrime, phishing.
    </div>
    <h4>1. Soorten Misdrijven (Types of Crime)</h4>
    <p>In het Engels bestaan er specifieke termen voor verschillende vormen van diefstal en criminaliteit:</p>
    <table class="theorie-tabel">
      <tr><th>Misdrijf</th><th>Betekenis & Voorbeeld</th></tr>
      <tr><td><b>Theft</b></td><td>Diefstal in het algemeen (de dader is een <i>thief</i>).</td></tr>
      <tr><td><b>Burglary</b></td><td>Inbraak in een gebouw/huis (de dader is een <i>burglar</i>).</td></tr>
      <tr><td><b>Robbery</b></td><td>Gewapende overval of beroving met geweld/dreiging (de dader is een <i>robber</i>).</td></tr>
      <tr><td><b>Shoplifting</b></td><td>Winkeldiefstal (stelen uit een open winkel).</td></tr>
      <tr><td><b>Cybercrime / Phishing</b></td><td>Digitale criminaliteit en online identiteitsfraude.</td></tr>
    </table>
    <h4>2. Politieonderzoek en Forensische Termen</h4>
    <ul>
      <li><b>Suspect:</b> De verdachte van het misdrijf.</li>
      <li><b>Witness:</b> Een getuige die iets gezien of gehoord heeft.</li>
      <li><b>Evidence:</b> Hard bewijsmateriaal (vingerafdrukken, camerabeelden, DNA).</li>
      <li><b>Clue:</b> Een aanwijzing of spoor dat leidt naar de dader.</li>
      <li><b>In custody:</b> In hechtenis / vastgehouden op het politiebureau.</li>
    </ul>
    <h4>3. De Rechtbank (The Justice System)</h4>
    <p>Als een verdachte voor de rechter (<b>judge</b>) moet verschijnen, vindt er een rechtszaak (<b>trial</b>) plaats. In Engelse rechtbanken beslist een <b>jury</b> (twaalf burgers) of de verdachte schuldig (<b>guilty</b>) of onschuldig (<b>innocent</b>) is, waarna de rechter de straf (<b>punishment / sentence</b>) oplegt.</p>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "What is the difference between <b>theft</b> and <b>burglary</b>?", "opties": ["Burglary specifically involves illegally breaking into a building or house", "Theft is only committed online via computers", "Burglary is a legal sport in the UK", "There is no difference in meaning"], "antwoord": 0, "uitleg": "Burglary is inbraak (het binnendringen in een gebouw om te stelen)."},
    {"type": "mc", "niveau": 1, "vraag": "What is a <b>witness</b> in a police investigation?", "opties": ["A person who saw or heard the event take place", "The person accused of committing the crime", "The judge presiding over the trial", "A police officer who makes the arrest"], "antwoord": 0, "uitleg": "A witness is een getuige."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "If a suspect is found <b>guilty</b> in court, it means they did not commit the crime.", "antwoord": False, "uitleg": "Onwaar. 'Guilty' betekent schuldig."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the English word for <i>bewijsmateriaal</i>: <i>The police found crucial DNA ... at the crime scene.</i>", "antwoord": "evidence", "uitleg": "Evidence is het Engelse woord voor bewijs / bewijsmateriaal."},
    {"type": "mc", "niveau": 2, "vraag": "What role does a <b>jury</b> have in an English court of law?", "opties": ["They listen to the evidence and decide whether the defendant is guilty or innocent", "They write the laws in parliament", "They arrest criminals on the street", "They defend the victim free of charge"], "antwoord": 0, "uitleg": "De jury (van 12 burgers) oordeelt over schuld of onschuld."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "A <b>clue</b> is a piece of information or evidence that helps solve a mystery or crime.", "antwoord": True, "uitleg": "Waar. A clue is een aanwijzing of spoor."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the missing word (onschuldig): <i>The suspect was declared completely ... by the court.</i>", "antwoord": "innocent", "uitleg": "Innocent betekent onschuldig."},
    {"type": "mc", "niveau": 3, "vraag": "What does <b>phishing</b> mean in modern cybercrime?", "opties": ["Tricking people into revealing passwords and financial details via fake emails or websites", "Catching fish illegally in nature reserves", "Stealing physical laptops from classrooms", "Downloading music without headphones"], "antwoord": 0, "uitleg": "Phishing is het online ontfutselen van gevoelige inlog- en bankgegevens via valse berichten."}
  ]
}

h2_2 = {
  "id": "eng-h2-2",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Grammar: Past Simple vs. Past Continuous",
  "korteUitleg": "Voltooide verleden tijd (Simple) versus een handeling die aan de gang was in het verleden (Continuous).",
  "icoon": "⏳",
  "kleur": "h2-thema",
  "theorie": """
    <h3>2.2 Grammar: Past Simple vs. Past Continuous</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> Past Simple (voltooid verleden) vs. Past Continuous (achtergrondhandeling / duurvorm in het verleden), en voegwoorden <i>when</i> en <i>while</i>.
    </div>
    <h4>1. Past Simple (O.V.T.)</h4>
    <p>Gebruik de <b>Past Simple</b> voor handelingen die in het verleden zijn begonnen én afgesloten:</p>
    <ul>
      <li><i>Regelmatige werkwoorden:</i> stam + <b>-ed</b> (<i>walked, played, watched</i>).</li>
      <li><i>Onregelmatige werkwoorden:</i> 2e rijtje uit je hoofd (<i>bought, saw, wrote, went, broke</i>).</li>
      <li><i>Ontkenningen & Vragen:</i> <b>did / didn't</b> + hele werkwoord (<i>Did you see the suspect? I didn't lock the door.</i>).</li>
    </ul>
    <p><b>Signaalwoorden:</b> <i>yesterday, last night/week/year, two days ago, in 2020</i>.</p>
    <h4>2. Past Continuous (Duurvorm in het verleden)</h4>
    <p>Gebruik de <b>Past Continuous</b> voor een handeling die op een bepaald moment in het verleden bezig was:</p>
    <p><b>Vorm:</b> <b>was / were + werkwoord-ing</b>.</p>
    <ul>
      <li><i>I / He / She / It:</i> <b>was</b> studying</li>
      <li><i>You / We / They:</i> <b>were</b> sleeping</li>
      <li><i>Ontkenning:</i> was not (wasn't) / were not (weren't)</li>
    </ul>
    <h4>3. De Combinatie: When & While</h4>
    <p>Vaak wordt een lange achtergrondhandeling (Past Continuous) onderbroken door een korte gebeurtenis (Past Simple):</p>
    <div class="voorbeeld-box">
      <i>While the detective <b>was examining</b> the room, he <b>found</b> a mysterious letter.</i><br>
      <i>The alarm <b>went off</b> when the burglar <b>was climbing</b> through the window.</i>
    </div>
    <ul>
      <li><b>While + Past Continuous:</b> <i>while I was walking home...</i></li>
      <li><b>When + Past Simple:</b> <i>when the lights suddenly went out...</i></li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Choose the correct verb combination: <i>While we ... dinner, the doorbell suddenly ... .</i>", "opties": ["were eating / rang", "ate / was ringing", "was eating / rang", "are eating / rings"], "antwoord": 0, "uitleg": "'While we were eating' (lange handeling) werd onderbroken door 'rang' (korte handeling)."},
    {"type": "mc", "niveau": 1, "vraag": "Which sentence is grammatically correct in the <b>Past Simple</b>?", "opties": ["The police arrested the thief yesterday afternoon.", "The police was arresting the thief yesterday afternoon.", "The police did arrested the thief yesterday afternoon.", "The police arrests the thief yesterday afternoon."], "antwoord": 0, "uitleg": "'Yesterday' vraagt om de Past Simple (arrested)."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "The Past Continuous form of <i>they (to sleep)</i> is <i>they was sleeping</i>.", "antwoord": False, "uitleg": "Onwaar. Bij 'they' gebruik je 'were sleeping'."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the correct Past Continuous form of <i>(to walk)</i>: <i>At 9 PM last night, I ... home from the sports club.</i>", "antwoord": "was walking", "uitleg": "I -> was + walking."},
    {"type": "mc", "niveau": 2, "vraag": "Which conjunction is usually followed by the <b>Past Continuous</b> to indicate an ongoing background activity?", "opties": ["While", "Yesterday", "Ago", "Never"], "antwoord": 0, "uitleg": "'While' wordt gevolgd door de Past Continuous (bijv. 'While she was reading...')."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "In negative Past Simple sentences, you use <i>didn't</i> followed by the base form of the verb (e.g. <i>didn't go</i>).", "antwoord": True, "uitleg": "Waar. Na didn't komt altijd het hele werkwoord (infinitief)."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the irregular Past Simple form of <i>(to break)</i>: <i>The burglar ... the kitchen window to get inside.</i>", "antwoord": "broke", "uitleg": "Het verleden tijdsvorm van break is broke."},
    {"type": "mc", "niveau": 3, "vraag": "What was happening in this sentence: <i>'Sarah was driving when she heard the news on the radio.'</i>?", "opties": ["Sarah was in the middle of driving when the news suddenly came on", "Sarah finished driving before she turned on the radio", "Sarah never drives while listening to the radio", "Sarah will drive home tomorrow afternoon"], "antwoord": 0, "uitleg": "'Was driving' was de doorlopende handeling die onderbroken werd door het nieuwsbericht."}
  ]
}

h2_3 = {
  "id": "eng-h2-3",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Stones & Skills: Reporting Crimes & Witness Statements",
  "korteUitleg": "Vaste spreekstenen voor het doen van aangifte, signalementen beschrijven en getuigenissen.",
  "icoon": "🚨",
  "kleur": "h2-thema",
  "theorie": """
    <h3>2.3 Stones & Skills: Reporting Crimes & Witness Statements</h3>
    <div class="info-box">
      <b>Communicatieve vaardigheden:</b> Aangifte doen bij de politie (reporting an incident), een verdachte beschrijven (physical description) en een formele getuigenverklaring opstellen.
    </div>
    <h4>1. Speaking Stones: Aangifte Doen bij de Politie</h4>
    <p>Als je in het buitenland slachtoffer of getuige bent van een misdrijf, gebruik je deze zinnen:</p>
    <ul>
      <li><i>I'd like to report a theft / a lost item.</i></li>
      <li><i>My backpack was stolen while I was waiting for the bus.</i></li>
      <li><i>It happened around 4 PM near the central station.</i></li>
      <li><i>Could you give me a copy of the police report for my insurance?</i></li>
    </ul>
    <h4>2. Speaking Stones: Signalement van een Verdachte (Physical Description)</h4>
    <table class="theorie-tabel">
      <tr><th>Kenmerk</th><th>Engelse Formulering</th></tr>
      <tr><td><b>Lengte & Postuur</b></td><td>He was in his late twenties, tall and of athletic build.</td></tr>
      <tr><td><b>Uiterlijk & Gezicht</b></td><td>She had shoulder-length curly brown hair and blue eyes.</td></tr>
      <tr><td><b>Kleding</b></td><td>The suspect was wearing a dark hoodie, grey trackpants and black sneakers.</td></tr>
      <tr><td><b>Bijzondere kenmerken</b></td><td>He had a distinctive tattoo on his left forearm and a small scar on his chin.</td></tr>
    </table>
    <h4>3. Schrijfvaardigheid: Een Getuigenverklaring (Witness Statement)</h4>
    <p>Let bij het schrijven van een verslag op de <b>chronologische volgorde</b>:</p>
    <ol>
      <li><b>Tijd en plaats:</b> <i>On Tuesday 14 October, at approximately 15:30...</i></li>
      <li><b>Wat je zelf aan het doen was:</b> <i>I was walking along High Street towards the library.</i></li>
      <li><b>De gebeurtenis:</b> <i>Suddenly, I noticed two men running out of the jewellery store.</i></li>
      <li><b>Vluchtrichting & Details:</b> <i>They fled in a black sedan heading north towards the motorway.</i></li>
    </ol>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "How do you start when reporting a stolen bicycle at an English police station?", "opties": ["I would like to report a stolen bicycle, please.", "Can I buy a new bicycle from you?", "Where is the nearest bike rental shop?", "I don't like cycling in this town."], "antwoord": 0, "uitleg": "'I would like to report a stolen bicycle' is de officiële en beleefde opening."},
    {"type": "mc", "niveau": 1, "vraag": "Which phrase correctly describes a suspect's approximate age?", "opties": ["He appeared to be in his mid-thirties.", "He was having 30 years.", "He counted 30 seasons.", "His age was made of 30."], "antwoord": 0, "uitleg": "'In his mid-thirties' is de standaard Engelse formulering."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "A <b>scar</b> is a permanent mark left on the skin after a wound has healed.", "antwoord": True, "uitleg": "Waar. A scar is een litteken."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the missing word for <i>aangifte doen</i>: <i>I need to ... a theft to the police.</i>", "antwoord": "report", "uitleg": "'To report a theft' betekent aangifte doen van diefstal."},
    {"type": "mc", "niveau": 2, "vraag": "Why is chronological order crucial in a formal witness statement?", "opties": ["It clearly shows the exact sequence of events for the investigators", "It makes the story rhyme like a poem", "It allows the witness to hide important facts", "It translates the text automatically into French"], "antwoord": 0, "uitleg": "Chronologische volgorde toont de exacte opeenvolging van gebeurtenissen."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "The word <i>hoodie</i> refers to a type of heavy winter boot used by police officers.", "antwoord": False, "uitleg": "Onwaar. A hoodie is een capuchontrui."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the preposition: <i>The suspect was ... his early twenties.</i>", "antwoord": "in", "uitleg": "Je zegt 'in his early twenties'."},
    {"type": "mc", "niveau": 3, "vraag": "What does the phrase <i>'athletic build'</i> mean when describing a suspect?", "opties": ["Strong, fit and muscular physique", "Extremely thin and fragile", "Wearing expensive designer glasses", "Walking with a wooden cane"], "antwoord": 0, "uitleg": "'Athletic build' betekent een gespierd en sportief postuur."}
  ]
}

# ==========================================
# 3. SCIENCE & TECHNOLOGY
# ==========================================
h3_1 = {
  "id": "eng-h3-1",
  "hoofdstuk": 3,
  "paragraaf": "3.1",
  "titel": "Theme Words: Inventions, AI & Modern Gadgets",
  "korteUitleg": "Kernwoorden over innovatie, kunstmatige intelligentie, apparaten en wetenschap.",
  "icoon": "🔬",
  "kleur": "h3-thema",
  "theorie": """
    <h3>3.1 Theme Words: Inventions, AI & Modern Gadgets</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Innovation, artificial intelligence (AI), device, algorithm, breakthrough, experiment, laboratory, gadget, robotics, virtual reality (VR), automated, rechargeable, efficient, discover, invent, sensor, network, developer, software.
    </div>
    <h4>1. Wetenschap en Uitvindingen</h4>
    <table class="theorie-tabel">
      <tr><th>Engels Begrip</th><th>Nederlandse Betekenis</th><th>Voorbeeldzin</th></tr>
      <tr><td><b>Innovation</b></td><td>Vernieuwing / Innovatie</td><td>Continuous <i>innovation</i> is essential in tech.</td></tr>
      <tr><td><b>Breakthrough</b></td><td>Doorbraak</td><td>Scientists achieved a major medical <i>breakthrough</i>.</td></tr>
      <tr><td><b>Discover vs. Invent</b></td><td>Ontdekken vs. Uitvinden</td><td>Newton <i>discovered</i> gravity; Edison <i>invented</i> the light bulb.</td></tr>
      <tr><td><b>Artificial Intelligence</b></td><td>Kunstmatige Intelligentie</td><td><i>AI</i> algorithms can process data faster than humans.</td></tr>
      <tr><td><b>Rechargeable</b></td><td>Oplaadbaar</td><td>This headset features a fast <i>rechargeable</i> battery.</td></tr>
      <tr><td><b>Efficient</b></td><td>Efficiënt / Zuinig</td><td>Solar cells have become much more <i>efficient</i>.</td></tr>
    </table>
    <h4>2. Digitale Apparaten en Technologie</h4>
    <ul>
      <li><b>Gadget / Device:</b> Een handig elektronisch apparaatje (smartphone, smartwatch, drone).</li>
      <li><b>Virtual Reality (VR):</b> Een computergegenereerde virtuele 3D-wereld.</li>
      <li><b>Sensor:</b> Een meetinstrument dat licht, beweging of temperatuur registreert.</li>
      <li><b>Automated:</b> Volledig computergestuurd zonder menselijke tussenkomst.</li>
    </ul>
    <h4>3. Ontdekken (Discover) vs. Uitvinden (Invent)</h4>
    <p>Let goed op het verschil:<br>
    - <b>Discover:</b> Iets vinden dat al bestond in de natuur (<i>Columbus discovered America, Marie Curie discovered radium</i>).<br>
    - <b>Invent:</b> Iets nieuws ontwerpen en maken dat nog niet bestond (<i>Alexander Graham Bell invented the telephone</i>).</p>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "What is the crucial difference between <b>discover</b> and <b>invent</b>?", "opties": ["Discover means finding something existing in nature; invent means creating a new device", "Discover is used for apps; invent is used for books", "There is no difference in modern English", "Invent is only used by professors in laboratories"], "antwoord": 0, "uitleg": "Ontdekken is iets bestaands vinden; uitvinden is iets nieuws ontwerpen."},
    {"type": "mc", "niveau": 1, "vraag": "What does <b>AI</b> stand for in modern technology?", "opties": ["Artificial Intelligence", "Automated Internet", "Advanced Invention", "Applied Industry"], "antwoord": 0, "uitleg": "AI staat voor Artificial Intelligence (Kunstmatige Intelligentie)."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "A <b>rechargeable</b> battery must be thrown away immediately after it runs empty once.", "antwoord": False, "uitleg": "Onwaar. Een rechargeable batterij kan opnieuw opgeladen worden."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the missing noun for <i>doorbraak</i>: <i>The research team celebrated a major scientific ... in cancer treatment.</i>", "antwoord": "breakthrough", "uitleg": "Breakthrough is het Engelse woord voor een doorbraak."},
    {"type": "mc", "niveau": 2, "vraag": "Which adjective describes a machine or process that works quickly and produces good results without wasting energy or time?", "opties": ["Efficient", "Broken", "Slow", "Dangerous"], "antwoord": 0, "uitleg": "Efficient betekent doelmatig en zuinig."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "A <b>sensor</b> is a electronic component that detects physical changes like temperature, motion, or light.", "antwoord": True, "uitleg": "Waar. Een sensor meet fysieke signalen."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the correct verb: <i>Thomas Edison ... the first practical electric light bulb in 1879.</i>", "antwoord": "invented", "uitleg": "Invented (uitvinden) is de juiste term voor de gloeilamp."},
    {"type": "mc", "niveau": 3, "vraag": "What does <b>Virtual Reality (VR)</b> technology allow users to do?", "opties": ["Experience and interact with an immersive computer-generated 3D environment", "Print physical documents on paper faster", "Make traditional phone calls without a microphone", "Measure the speed of wind with an analog needle"], "antwoord": 0, "uitleg": "VR biedt een immersieve, computergegenereerde 3D-ervaring."}
  ]
}

h3_2 = {
  "id": "eng-h3-2",
  "hoofdstuk": 3,
  "paragraaf": "3.2",
  "titel": "Grammar: Present Perfect vs. Past Simple",
  "korteUitleg": "V.T.T. (Present Perfect) voor ervaringen/resultaten nu versus O.V.T. (Past Simple) voor afgesloten tijd.",
  "icoon": "⌛",
  "kleur": "h3-thema",
  "theorie": """
    <h3>3.2 Grammar: Present Perfect vs. Past Simple</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> Present Perfect (ervaringen, resultaat in het heden, onbepaalde tijd) vs. Past Simple (afgesloten tijdstip), signaalwoorden <i>ever, never, already, yet, just, for, since</i>.
    </div>
    <h4>1. Present Perfect (V.T.T.)</h4>
    <p>Gebruik de <b>Present Perfect</b> in de volgende situaties:</p>
    <ul>
      <li><b>Ervaringen in je leven tot nu toe:</b> <i>Have you ever used a VR headset? I have never visited Silicon Valley.</i></li>
      <li><b>Handelingen begonnen in het verleden die nu nog duren:</b> <i>She has lived in Cambridge since 2018.</i></li>
      <li><b>Resultaat is nu zichtbaar/belangrijk:</b> <i>I have lost my phone (so I can't call you now).</i></li>
    </ul>
    <p><b>Vorm:</b> <b>have / has + voltooid deelwoord (3e rijtje / -ed)</b>.</p>
    <ul>
      <li><i>He/She/It:</i> <b>has</b> invented / has seen</li>
      <li><i>I/You/We/They:</i> <b>have</b> developed / have written</li>
    </ul>
    <h4>2. Signaalwoorden van de Present Perfect</h4>
    <table class="theorie-tabel">
      <tr><th>Signaalwoord</th><th>Gebruik & Positie</th><th>Voorbeeldzin</th></tr>
      <tr><td><b>Ever / Never</b></td><td>In vragen / ontkenningen (ooit / nooit)</td><td><i>Have you ever built a robot?</i></td></tr>
      <tr><td><b>Already</b></td><td>Al (bevestigend, middenin de zin)</td><td><i>Scientists have already tested the prototype.</i></td></tr>
      <tr><td><b>Yet</b></td><td>Nog (in ontkenningen en vragen, aan het einde)</td><td><i>I haven't charged my laptop yet.</i></td></tr>
      <tr><td><b>Just</b></td><td>Zojuist / net</td><td><i>The rocket has just launched.</i></td></tr>
      <tr><td><b>Since</b></td><td>Vanaf een specifiek startpunt in de tijd</td><td><i>since 2015, since last week, since 9 o'clock</i></td></tr>
      <tr><td><b>For</b></td><td>Gedurende een tijdsduur</td><td><i>for three years, for two hours, for days</i></td></tr>
    </table>
    <h4>3. Het Verschil met de Past Simple</h4>
    <p>Zodra er een <b>afgesloten tijdstip</b> wordt genoemd (<i>yesterday, in 2019, two days ago, when I was ten</i>), MOET je de <b>Past Simple</b> gebruiken:</p>
    <p>✅ <i>Tim Berners-Lee <b>invented</b> the World Wide Web in 1989.</i> (Past Simple)<br>
    ✅ <i>The internet <b>has changed</b> our daily lives completely.</i> (Present Perfect - resultaat nu)</p>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which sentence correctly uses the <b>Present Perfect</b>?", "opties": ["She has developed a revolutionary new mobile application.", "She have develop a revolutionary new mobile application.", "She developed a new app in 2021 already.", "She is develop a revolutionary app since yesterday."], "antwoord": 0, "uitleg": "She has + voltooid deelwoord (developed)."},
    {"type": "mc", "niveau": 1, "vraag": "Choose the correct signal word: <i>Have you received your new tablet ...?</i>", "opties": ["yet", "yesterday", "since", "ago"], "antwoord": 0, "uitleg": "'Yet' staat aan het einde van vraagzinnen in de Present Perfect."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "You should use the Present Perfect when an exact finished time in the past is mentioned, such as <i>'in 1995'</i>.", "antwoord": False, "uitleg": "Onwaar. Bij een afgesloten tijdstip gebruik je de Past Simple."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in <i>since</i> or <i>for</i>: <i>Dr. Watson has worked in this laboratory ... five years.</i>", "antwoord": "for", "uitleg": "'For' gebruik je voor een tijdsduur (five years)."},
    {"type": "mc", "niveau": 2, "vraag": "Choose the correct verb form: <i>Steve Jobs ... Apple in 1976.</i>", "opties": ["founded", "has founded", "have founded", "is founding"], "antwoord": 0, "uitleg": "'In 1976' is een afgesloten tijdstip, dus Past Simple (founded)."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "The word <i>since</i> is used with a specific starting point in time (e.g. <i>since Monday</i>).", "antwoord": True, "uitleg": "Waar. 'Since' geeft het startpunt aan."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the correct Present Perfect form of <i>(to see)</i>: <i>I ... never ... such an incredible drone demonstration before.</i>", "antwoord": "have seen", "uitleg": "I have + never + seen."},
    {"type": "mc", "niveau": 3, "vraag": "Why is <i>'I have bought this laptop two days ago'</i> grammatically incorrect?", "opties": ["Because 'two days ago' specifies a finished point in the past, requiring the Past Simple 'bought'", "Because 'laptop' requires the auxiliary verb 'has'", "Because 'bought' cannot be used with technology", "Because 'have' can only be used with future dates"], "antwoord": 0, "uitleg": "'Two days ago' is een afgesloten tijdstip -> 'I bought this laptop two days ago'."}
  ]
}

h3_3 = {
  "id": "eng-h3-3",
  "hoofdstuk": 3,
  "paragraaf": "3.3",
  "titel": "Stones & Skills: Explaining Tech & Giving Instructions",
  "korteUitleg": "Vaste zinnen voor het uitleggen van apparaten, stapsgewijze instructies en tech reviews.",
  "icoon": "⚙️",
  "kleur": "h3-thema",
  "theorie": """
    <h3>3.3 Stones & Skills: Explaining Tech & Giving Instructions</h3>
    <div class="info-box">
      <b>Communicatieve vaardigheden:</b> Uitleggen hoe een apparaat werkt (explaining how it works), stapsgewijze instructies geven (step-by-step instructions) en voor- en nadelen bespreken.
    </div>
    <h4>1. Speaking Stones: Uitleggen Hoe Iets Werkt</h4>
    <ul>
      <li><i>This device is designed to track your daily physical activity.</i></li>
      <li><i>It allows you to control your home lighting using your voice.</i></li>
      <li><i>The main advantage of this gadget is its compact size and long battery life.</i></li>
      <li><i>The downside is that it requires a constant internet connection.</i></li>
    </ul>
    <h4>2. Signaalwoorden voor Instructies (Sequencing Words)</h4>
    <p>Gebruik bij het geven van technische handleidingen duidelijke volgordewoorden:</p>
    <ul>
      <li><b>First / First of all:</b> <i>First, plug the cable into the charging port.</i></li>
      <li><b>Next / Then:</b> <i>Then, press and hold the power button for three seconds.</i></li>
      <li><b>After that:</b> <i>After that, open the companion app on your smartphone.</i></li>
      <li><b>Finally:</b> <i>Finally, follow the on-screen instructions to connect to Wi-Fi.</i></li>
    </ul>
    <h4>3. Schrijfvaardigheid: Een Gadget Review</h4>
    <p>In een recensie van een technologisch product weeg je altijd de plussen en minnen tegen elkaar af:</p>
    <div class="voorbeeld-box">
      <b>Pros (Voordelen):</b> user-friendly interface, durable build, fast charging.<br>
      <b>Cons (Nadelen):</b> expensive price tag, limited storage capacity.<br>
      <b>Verdict (Oordeel):</b> <i>Overall, I would highly recommend this device to anyone who loves music.</i>
    </div>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which sequencing word is best suited to start a technical instruction guide?", "opties": ["First of all,", "Finally,", "Suddenly,", "Eventually,"], "antwoord": 0, "uitleg": "'First of all' leidt de allereerste stap in."},
    {"type": "mc", "niveau": 1, "vraag": "What is the meaning of the word <b>downside</b> in a gadget review?", "opties": ["A disadvantage or drawback", "A positive feature", "The battery charger", "The retail price"], "antwoord": 0, "uitleg": "'Downside' betekent nadeel / minpunt."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "The word <i>user-friendly</i> means that a device is complicated and difficult to operate.", "antwoord": False, "uitleg": "Onwaar. 'User-friendly' betekent juist gebruiksvriendelijk en eenvoudig."},
    {"type": "invoer", "niveau": 1, "vraag": "Complete the phrase: <i>The main ... of this smartwatch is its incredible battery life.</i>", "antwoord": "advantage|benefit", "uitleg": "'Advantage' (voordeel) past perfect in deze context."},
    {"type": "mc", "niveau": 2, "vraag": "Which phrase expresses a final overall recommendation?", "opties": ["Overall, I would highly recommend this product to students.", "First, insert the micro SIM card.", "Why is the screen flashing red?", "This button switches off the device."], "antwoord": 0, "uitleg": "'Overall, I would highly recommend...' vormt het eindoordeel."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "In a product review, <b>pros and cons</b> refer to the positive and negative aspects of the item.", "antwoord": True, "uitleg": "Waar. Pros = voordelen, cons = nadelen."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the missing word: <i>..., turn on the device by pressing the main power button.</i>", "antwoord": "next|then|first", "uitleg": "'Next' of 'Then' verbindt instructiestappen."},
    {"type": "mc", "niveau": 3, "vraag": "What is the function of the phrase <i>'This feature enables you to...'</i>?", "opties": ["To explain what capability a specific feature provides to the user", "To ask for a technical refund at customer service", "To warn users about dangerous high voltage", "To shut down the operating system"], "antwoord": 0, "uitleg": "'Enables you to...' legt uit wat een functie mogelijk maakt."}
  ]
}

# ==========================================
# 4. TO THE EXTREME
# ==========================================
h4_1 = {
  "id": "eng-h4-1",
  "hoofdstuk": 4,
  "paragraaf": "4.1",
  "titel": "Theme Words: Extreme Sports, Survival & Endurance",
  "korteUitleg": "Kernwoorden over extreme sporten, overleven in de wildernis en fysieke uitdagingen.",
  "icoon": "⚡",
  "kleur": "h4-thema",
  "theorie": """
    <h3>4.1 Theme Words: Extreme Sports, Survival & Endurance</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Adrenaline, endurance, survival, extreme sports, challenge, obstacle, courage, fearless, mountaineering, equipment, rescue team, expedition, blizzard, avalanche, dehydration, risk, stamina, triumph, altitude, wilderness.
    </div>
    <h4>1. Extreme Sporten en Uitdagingen</h4>
    <table class="theorie-tabel">
      <tr><th>Engels Begrip</th><th>Nederlandse Betekenis</th><th>Voorbeeldzin</th></tr>
      <tr><td><b>Endurance / Stamina</b></td><td>Uithoudingsvermogen</td><td>Marathon runners need incredible <i>endurance</i>.</td></tr>
      <tr><td><b>Adrenaline rush</b></td><td>Adrenalinestoot</td><td>Skydiving gives you an unforgettable <i>adrenaline rush</i>.</td></tr>
      <tr><td><b>Courage / Fearless</b></td><td>Moed / Onverschrokken</td><td>It takes immense <i>courage</i> to climb Mount Everest.</td></tr>
      <tr><td><b>Obstacle / Challenge</b></td><td>Obstakel / Uitdaging</td><td>The athletes overcame every grueling <i>obstacle</i>.</td></tr>
      <tr><td><b>Equipment / Gear</b></td><td>Uitrusting / Materiaal</td><td>Always inspect your climbing <i>equipment</i> carefully.</td></tr>
    </table>
    <h4>2. Overleven in de Wildernis (Survival)</h4>
    <ul>
      <li><b>Wilderness:</b> Ongerepte, woeste natuur ver van de bewoonde wereld.</li>
      <li><b>Avalanche:</b> Een lawine van sneeuw en ijs op een berghelling.</li>
      <li><b>Blizzard:</b> Een hevige sneeuwstorm met zware windstoten.</li>
      <li><b>Dehydration:</b> Ernstig vochttekort / uitdroging.</li>
      <li><b>Rescue team:</b> Een professioneel reddingsteam dat vermiste personen zoekt.</li>
      <li><b>Altitude:</b> De hoogte boven zeeniveau (bijv. <i>high altitude causes oxygen shortage</i>).</li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "What is the English word for a mass of snow and ice falling rapidly down a mountain?", "opties": ["Avalanche", "Blizzard", "Wilderness", "Endurance"], "antwoord": 0, "uitleg": "An avalanche is een sneeuwlawine."},
    {"type": "mc", "niveau": 1, "vraag": "Which word means the physical ability to sustain prolonged stressful effort or activity?", "opties": ["Endurance", "Altitude", "Equipment", "Triumph"], "antwoord": 0, "uitleg": "Endurance (of stamina) is uithoudingsvermogen."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "<b>Dehydration</b> occurs when your body does not have enough water and fluids to function properly.", "antwoord": True, "uitleg": "Waar. Dehydration is uitdroging door vochttekort."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the English word for <i>uitrusting</i>: <i>Before descending the cave, double-check all safety ... .</i>", "antwoord": "equipment|gear", "uitleg": "Equipment (of gear) betekent uitrusting."},
    {"type": "mc", "niveau": 2, "vraag": "What does being <b>fearless</b> mean?", "opties": ["Showing no fear, brave and courageous", "Being terrified of heights", "Refusing to wear safety helmets", "Travelling without a compass"], "antwoord": 0, "uitleg": "Fearless betekent onverschrokken en zonder angst."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "A <b>blizzard</b> is a gentle summer breeze with light sunshine.", "antwoord": False, "uitleg": "Onwaar. A blizzard is een zware sneeuwstorm."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the missing word for <i>reddingsteam</i>: <i>The helicopter ... team arrived just in time.</i>", "antwoord": "rescue", "uitleg": "Rescue team is het reddingsteam."},
    {"type": "mc", "niveau": 3, "vraag": "Why is <b>altitude</b> a critical factor for mountaineers climbing peaks above 8,000 meters?", "opties": ["Because the air pressure drops and oxygen levels become dangerously low", "Because the sun sets earlier at the top of mountains", "Because smartphones stop playing music at high altitudes", "Because hiking boots become heavier in cold weather"], "antwoord": 0, "uitleg": "Op grote hoogte is er minder zuurstof beschikbaar in de lucht."}
  ]
}

h4_2 = {
  "id": "eng-h4-2",
  "hoofdstuk": 4,
  "paragraaf": "4.2",
  "titel": "Grammar: Comparatives, Superlatives & Modals",
  "korteUitleg": "Trappen van vergelijking (er/est, more/most) en hulpwerkwoorden van verplichting en advies.",
  "icoon": "🏔️",
  "kleur": "h4-thema",
  "theorie": """
    <h3>4.2 Grammar: Comparatives, Superlatives & Modals</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> Vergrotende en overtreffende trap (Comparatives & Superlatives), onregelmatige vormen, (not) as ... as, en modale hulpwerkwoorden (<i>must, have to, should, can, could</i>).
    </div>
    <h4>1. Trappen van Vergelijking (Comparatives & Superlatives)</h4>
    <table class="theorie-tabel">
      <tr><th>Type Adjectief</th><th>Stellend</th><th>Vergrotend (+er / more)</th><th>Overtreffend (+est / most)</th></tr>
      <tr><td>1 lettergreep</td><td>Fast / Hard</td><td>Faster / Harder than</td><td>The fastest / hardest</td></tr>
      <tr><td>Eindigt op -y</td><td>Risky / Heavy</td><td>Riskier / Heavier than</td><td>The riskiest / heaviest</td></tr>
      <tr><td>2+ lettergrepen</td><td>Dangerous</td><td>More dangerous than</td><td>The most dangerous</td></tr>
      <tr><td><b>Onregelmatig</b></td><td>Good / Bad / Far</td><td>Better / Worse / Further</td><td>The best / worst / furthest</td></tr>
    </table>
    <h4>2. Gelijkheid: (Not) as ... as</h4>
    <ul>
      <li><i>Rock climbing is <b>as exciting as</b> surfing.</i> (Even spannend als)</li>
      <li><i>Running a 5k is <b>not as exhausting as</b> a full marathon.</i> (Niet zo vermoeiend als)</li>
    </ul>
    <h4>3. Modale Hulpwerkwoorden (Modals of Obligation & Advice)</h4>
    <ul>
      <li><b>Must / Have to:</b> Noodzaak en verplichting (<i>You must wear a helmet on the ski slopes</i>).</li>
      <li><b>Mustn't:</b> Verbod (<i>You mustn't leave the marked trail</i>).</li>
      <li><b>Should / Ought to:</b> Advies en aanbeveling (<i>You should drink plenty of water during the hike</i>).</li>
      <li><b>Can / Could:</b> Mogelijkheid en vermogen (<i>He can climb steep cliffs without ropes</i>).</li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which sentence correctly uses the <b>comparative</b> form?", "opties": ["Mount Everest is higher than Mont Blanc.", "Mount Everest is more high than Mont Blanc.", "Mount Everest is highest than Mont Blanc.", "Mount Everest is as high than Mont Blanc."], "antwoord": 0, "uitleg": "High is 1 lettergreep -> higher than."},
    {"type": "mc", "niveau": 1, "vraag": "What is the irregular superlative form of <b>bad</b>?", "opties": ["The worst", "The baddest", "The more bad", "The worse"], "antwoord": 0, "uitleg": "Bad -> worse -> the worst."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "You use <b>should</b> to express a strict legal prohibition punishable by law.", "antwoord": False, "uitleg": "Onwaar. 'Should' geeft advies (je zou moeten). Voor een verbod gebruik je 'mustn't'."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the superlative of <i>(dangerous)</i>: <i>Free solo climbing is one of the ... sports in the world.</i>", "antwoord": "most dangerous", "uitleg": "Dangerous heeft 3 lettergrepen -> most dangerous."},
    {"type": "mc", "niveau": 2, "vraag": "Which modal verb expresses strong necessity or obligation?", "opties": ["Must", "Might", "Could", "May"], "antwoord": 0, "uitleg": "'Must' drukt een sterke verplichting of noodzaak uit."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "The sentence <i>'This trail is not as difficult as the north ridge'</i> means both trails have the exact same difficulty.", "antwoord": False, "uitleg": "Onwaar. 'Not as difficult as' betekent dat het minder moeilijk is."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the comparative form of <i>(good)</i>: <i>Quality hiking boots are much ... than ordinary sneakers for mountain trekking.</i>", "antwoord": "better", "uitleg": "Good -> better."},
    {"type": "mc", "niveau": 3, "vraag": "Choose the correct advice for an injured hiker:", "opties": ["You should rest your ankle and avoid putting weight on it.", "You mustn't never call mountain rescue.", "You have to run fast down the slope.", "You shouldn't drink any fluids."], "antwoord": 0, "uitleg": "'You should rest your ankle' is het juiste medische advies."}
  ]
}

h4_3 = {
  "id": "eng-h4-3",
  "hoofdstuk": 4,
  "paragraaf": "4.3",
  "titel": "Stones & Skills: Safety Warnings & Giving Advice",
  "korteUitleg": "Vaste zinnen voor veiligheidswaarschuwingen, aanmoedigingen en survival survivalgidsen.",
  "icoon": "⚠️",
  "kleur": "h4-thema",
  "theorie": """
    <h3>4.3 Stones & Skills: Safety Warnings & Giving Advice</h3>
    <div class="info-box">
      <b>Communicatieve vaardigheden:</b> Waarschuwingen geven (safety warnings), aanmoedigen (encouragement), angst/opwinding uitdrukken en overlevingstips formuleren.
    </div>
    <h4>1. Speaking Stones: Waarschuwen voor Gevaar</h4>
    <ul>
      <li><i>Watch out! The rocks ahead are extremely slippery.</i></li>
      <li><i>Be careful not to lose your footing on the steep ledge.</i></li>
      <li><i>Whatever you do, don't drink unboiled stream water.</i></li>
      <li><i>Make sure you always carry an emergency whistle and thermal blanket.</i></li>
    </ul>
    <h4>2. Speaking Stones: Aanmoedigen en Geruststellen</h4>
    <table class="theorie-tabel">
      <tr><th>Aanmoediging</th><th>Situatie</th></tr>
      <tr><td><i>Keep going, you're almost at the summit!</i></td><td>Tijdens een zware klim</td></tr>
      <tr><td><i>Don't give up now, you've got this!</i></td><td>Wanneer iemand moe is</td></tr>
      <tr><td><i>Take a deep breath and stay calm.</i></td><td>Bij paniek of angst</td></tr>
    </table>
    <h4>3. Schrijfvaardigheid: Een Survival Gids (How-To Guide)</h4>
    <p>Gebruik bij het schrijven van veiligheidsinstructies de <b>gebiedende wijs (Imperative)</b>:</p>
    <ul>
      <li>✅ <i><b>Stay</b> in your shelter during a blizzard.</i></li>
      <li>✅ <i><b>Do not attempt</b> to cross a frozen lake alone.</i></li>
      <li>✅ <i><b>Signal</b> three times with your flashlight to indicate distress.</i></li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which phrase is used to give an urgent safety warning on a mountain trail?", "opties": ["Watch out! The rocks are very loose.", "Good morning, how was your breakfast?", "I think green is my favourite colour.", "Can you lend me your pencil?"], "antwoord": 0, "uitleg": "'Watch out!' is de directe waarschuwing voor gevaar."},
    {"type": "mc", "niveau": 1, "vraag": "What is the best way to encourage a tired climbing partner?", "opties": ["Keep going, you're doing great and we're almost at the top!", "You are way too slow, I am leaving you here.", "This mountain is far too difficult for beginners.", "Give up immediately."], "antwoord": 0, "uitleg": "Positieve aanmoediging helpt de klimmer door te zetten."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "In safety instructions, using the imperative form (e.g. <i>'Stay calm'</i>) is clear and direct.", "antwoord": True, "uitleg": "Waar. De gebiedende wijs is helder en doelmatig in instructies."},
    {"type": "invoer", "niveau": 1, "vraag": "Complete the warning: <i>Be ... not to step on the thin ice!</i>", "antwoord": "careful", "uitleg": "'Be careful' betekent wees voorzichtig."},
    {"type": "mc", "niveau": 2, "vraag": "What should you do if someone is experiencing a panic attack during an outdoor adventure?", "opties": ["Tell them to take slow, deep breaths and reassure them calmly", "Shout at them and run away into the forest", "Tell them dangerous wolves are approaching", "Force them to climb twice as fast"], "antwoord": 0, "uitleg": "Rustig ademen en kalmeren is de juiste aanpak."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "The phrase <i>'Whatever you do, don't panic'</i> emphasizes that staying calm is the highest priority.", "antwoord": True, "uitleg": "Waar. 'Whatever you do, don't...' legt sterke nadruk op wat je moet vermijden."},
    {"type": "invoer", "niveau": 2, "vraag": "Complete the encouraging phrase: <i>Don't ... up, you can do it!</i>", "antwoord": "give", "uitleg": "'Don't give up' betekent geef niet op."},
    {"type": "mc", "niveau": 3, "vraag": "Why is <i>'Make sure you always check your gear'</i> an effective safety rule?", "opties": ["It clearly states a mandatory preventive action before starting the activity", "It is written in French for tourists", "It promises that accidents are 100% impossible", "It allows hikers to climb in the dark"], "antwoord": 0, "uitleg": "'Make sure you always...' formuleert een duidelijke preventieve veiligheidsregel."}
  ]
}

# ==========================================
# 5. GOING GREEN
# ==========================================
h5_1 = {
  "id": "eng-h5-1",
  "hoofdstuk": 5,
  "paragraaf": "5.1",
  "titel": "Theme Words: Environment, Climate & Sustainability",
  "korteUitleg": "Kernwoorden over duurzaamheid, klimaatverandering, hernieuwbare energie en ecosystemen.",
  "icoon": "🌱",
  "kleur": "h5-thema",
  "theorie": """
    <h3>5.1 Theme Words: Environment, Climate & Sustainability</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Sustainability, climate change, carbon footprint, global warming, renewable energy, solar panels, wind turbine, ecosystem, endangered species, biodiversity, deforestation, recycle, pollution, greenhouse effect, eco-friendly, conservation, organic.
    </div>
    <h4>1. Klimaat en Milieu (The Environment)</h4>
    <table class="theorie-tabel">
      <tr><th>Engels Begrip</th><th>Nederlandse Betekenis</th><th>Voorbeeldzin</th></tr>
      <tr><td><b>Sustainability</b></td><td>Duurzaamheid</td><td>Our company aims for 100% <i>sustainability</i> by 2030.</td></tr>
      <tr><td><b>Carbon footprint</b></td><td>Koolstofvoetafdruk / CO2-uitstoot</td><td>Flying less reduces your personal <i>carbon footprint</i>.</td></tr>
      <tr><td><b>Global warming</b></td><td>Opwarming van de aarde</td><td><i>Global warming</i> leads to rising sea levels and heatwaves.</td></tr>
      <tr><td><b>Renewable energy</b></td><td>Hernieuwbare / Duurzame energie</td><td>Wind and solar power are forms of <i>renewable energy</i>.</td></tr>
      <tr><td><b>Deforestation</b></td><td>Ontbossing</td><td><i>Deforestation</i> in the Amazon destroys habitats.</td></tr>
      <tr><td><b>Endangered species</b></td><td>Bedreigde diersoorten</td><td>Tigers and polar bears are <i>endangered species</i>.</td></tr>
      <tr><td><b>Biodiversity</b></td><td>Biodiversiteit</td><td>Healthy wetlands support rich plant and animal <i>biodiversity</i>.</td></tr>
    </table>
    <h4>2. Groene Gewoontes en Oplossingen</h4>
    <ul>
      <li><b>Eco-friendly / Green:</b> Milieuvriendelijk geproduceerd of ontworpen.</li>
      <li><b>Recycle:</b> Materialen (plastic, glas, papier) hergebruiken in plaats van weggooien.</li>
      <li><b>Organic food:</b> Biologisch voedsel geteeld zonder kunstmatige pesticiden.</li>
      <li><b>Conservation:</b> Het beschermen en behouden van de natuur en wilde dieren.</li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "What is the meaning of <b>carbon footprint</b>?", "opties": ["The total amount of greenhouse gases generated by our actions and lifestyle", "The physical size of your shoe", "The black soot left by coal power plants on trees", "A new brand of recycled sneakers"], "antwoord": 0, "uitleg": "Carbon footprint is de totale hoeveelheid broeikasgassen (CO2) die iemands levensstijl veroorzaakt."},
    {"type": "mc", "niveau": 1, "vraag": "Which of the following is an example of <b>renewable energy</b>?", "opties": ["Solar power generated by rooftop panels", "Burning diesel fuel in large generators", "Using coal in traditional thermal plants", "Nuclear fission reactors"], "antwoord": 0, "uitleg": "Zonne-energie is een onuitputtelijke hernieuwbare energiebron."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "<b>Deforestation</b> means planting millions of new trees in urban parks.", "antwoord": False, "uitleg": "Onwaar. Deforestation is grootschalige ontbossing (het kappen van bomen)."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the English term for <i>bedreigde diersoort</i>: <i>The giant panda is an ... species.</i>", "antwoord": "endangered", "uitleg": "Endangered species betekent bedreigde soort."},
    {"type": "mc", "niveau": 2, "vraag": "What does the term <b>biodiversity</b> refer to?", "opties": ["The variety of plant and animal life in a particular habitat or ecosystem", "The number of electric cars sold in Europe", "The chemical formula for clean drinking water", "The amount of plastic packaging in supermarkets"], "antwoord": 0, "uitleg": "Biodiversiteit is de verscheidenheid aan levensvormen in een leefgebied."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "Products labeled as <b>eco-friendly</b> are designed to inflict minimal damage on the environment.", "antwoord": True, "uitleg": "Waar. Eco-friendly betekent milieuvriendelijk."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the missing verb (hergebruiken/recyclen): <i>We should always ... plastic bottles and aluminium cans.</i>", "antwoord": "recycle", "uitleg": "Recycle is het Engelse werkwoord voor recyclen."},
    {"type": "mc", "niveau": 3, "vraag": "Why is nature <b>conservation</b> vital for future generations?", "opties": ["It protects ecosystems, natural resources, and prevents wildlife extinction", "It makes airline tickets cheaper for vacationers", "It increases industrial coal mining in river basins", "It eliminates the need for solar panels"], "antwoord": 0, "uitleg": "Natuurbescherming (conservation) behoudt ecosystemen en voorkomt uitsterven."}
  ]
}

h5_2 = {
  "id": "eng-h5-2",
  "hoofdstuk": 5,
  "paragraaf": "5.2",
  "titel": "Grammar: Future Forms & First Conditional",
  "korteUitleg": "Toekomende tijden (will vs. going to vs. present continuous) en voorwaardelijke zinnen (First Conditional).",
  "icoon": "🌱",
  "kleur": "h5-thema",
  "theorie": """
    <h3>5.2 Grammar: Future Forms & First Conditional</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> <i>Will</i> (voorspellingen, spontane besluiten) vs. <i>Going to</i> (plannen, bedoelingen, zichtbaar bewijs) vs. Present Continuous (vaste afspraken), en de First Conditional (<i>if + present simple, will + hele ww</i>).
    </div>
    <h4>1. Toekomende Tijden (Future Forms)</h4>
    <table class="theorie-tabel">
      <tr><th>Vorm</th><th>Wanneer Gebruiken?</th><th>Voorbeeldzin</th></tr>
      <tr><td><b>Will + hele ww</b></td><td>Voorspelling zonder direct bewijs, spontaan besluit, belofte</td><td><i>I think temperatures will rise. I'll open the window!</i></td></tr>
      <tr><td><b>Be going to + hele ww</b></td><td>Vast plan, intentie, of voorspelling met direct zichtbaar bewijs</td><td><i>We are going to install solar panels next month. Look at those dark clouds, it is going to rain!</i></td></tr>
      <tr><td><b>Present Continuous</b></td><td>Vaste persoonlijke afspraak met tijd/plaats</td><td><i>We are meeting the green council at 2 PM tomorrow.</i></td></tr>
    </table>
    <h4>2. De First Conditional (Reële Voorwaarde)</h4>
    <p>Je gebruikt de <b>First Conditional</b> voor reële situaties in de toekomst die waarschijnlijk gebeuren als aan een voorwaarde wordt voldaan:</p>
    <div class="voorbeeld-box">
      <b>Structuur:</b> <i>If + Present Simple, ... will + hele werkwoord</i><br><br>
      <i>If we <b>recycle</b> more plastic, we <b>will reduce</b> ocean pollution.</i><br>
      <i>Global temperatures <b>will increase</b> if countries <b>do not cut</b> emissions.</i>
    </div>
    <ul>
      <li>In het <b>if-deel</b> mag NOOIT <i>will</i> staan! (Dus: <s>If it will rain</s> ❌ -> <i>If it rains</i> ✅).</li>
      <li>Het resultaatdeel bevat <b>will / won't + hele werkwoord</b>.</li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which sentence is a grammatically correct <b>First Conditional</b>?", "opties": ["If we invest in solar energy, we will save money on electricity.", "If we will invest in solar energy, we save money.", "If we invest in solar energy, we saved money.", "If we invested in solar energy, we will save money."], "antwoord": 0, "uitleg": "If + Present Simple (invest), resultaat = will + hele werkwoord (will save)."},
    {"type": "mc", "niveau": 1, "vraag": "Look at the dark storm clouds in the sky! Which future form is correct?", "opties": ["It is going to rain very soon.", "It will rain maybe next year.", "It rains yesterday afternoon.", "It was raining currently."], "antwoord": 0, "uitleg": "Bij direct zichtbaar bewijs gebruik je 'be going to' (it is going to rain)."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "In the <i>if-clause</i> of a First Conditional sentence, you should always use <i>will</i>.", "antwoord": False, "uitleg": "Onwaar. In het if-deel gebruik je de Present Simple, NOOIT will."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the correct verb form: <i>If sea levels rise, many coastal cities ... be flooded.</i>", "antwoord": "will", "uitleg": "Het resultaatdeel van de First Conditional krijgt 'will'."},
    {"type": "mc", "niveau": 2, "vraag": "Someone rings your doorbell. You make a spontaneous decision right now. What do you say?", "opties": ["I'll get it!", "I am going to get it yesterday.", "I get it every day.", "I have got it since morning."], "antwoord": 0, "uitleg": "Voor spontane beslissingen ter plekke gebruik je 'will' / 'I'll'."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "The negative form of <i>will</i> in future sentences is <i>won't</i> (will not).", "antwoord": True, "uitleg": "Waar. Won't is de samentrekking van will not."},
    {"type": "invoer", "niveau": 2, "vraag": "Complete the First Conditional sentence: <i>If you ... (to turn) off the lights, you will save electricity.</i>", "antwoord": "turn", "uitleg": "If + Present Simple: turn."},
    {"type": "mc", "niveau": 3, "vraag": "Why is <i>'If the factory will pollute the river, fish will die'</i> incorrect?", "opties": ["Because the conditional 'if' clause must be in the Present Simple ('pollutes')", "Because 'fish' is always singular", "Because 'die' cannot be combined with will", "Because factories are not allowed in English sentences"], "antwoord": 0, "uitleg": "In de if-bijzin gebruik je de Present Simple: 'If the factory pollutes...'."}
  ]
}

h5_3 = {
  "id": "eng-h5-3",
  "hoofdstuk": 5,
  "paragraaf": "5.3",
  "titel": "Stones & Skills: Proposing Green Ideas & Debating",
  "korteUitleg": "Vaste zinnen voor het voorstellen van duurzame ideeën, beleefd debatteren en overtuigen.",
  "icoon": "🗣️",
  "kleur": "h5-thema",
  "theorie": """
    <h3>5.3 Stones & Skills: Proposing Green Ideas & Debating</h3>
    <div class="info-box">
      <b>Communicatieve vaardigheden:</b> Duurzame initiatieven voorstellen (making suggestions), overtuigende argumenten formuleren (persuasive debating) en meningen nuanceren.
    </div>
    <h4>1. Speaking Stones: Duurzame Suggesties Doen</h4>
    <table class="theorie-tabel">
      <tr><th>Suggestie Formule</th><th>Voorbeeldzin</th></tr>
      <tr><td><i>Why don't we...?</i></td><td>Why don't we organise a tree-planting day at school?</td></tr>
      <tr><td><i>How about / What about + -ing?</i></td><td>How about banning single-use plastic bottles in the canteen?</td></tr>
      <tr><td><i>We could easily...</i></td><td>We could easily install recycling bins in every classroom.</td></tr>
      <tr><td><i>I suggest that we...</i></td><td>I suggest that we encourage students to cycle to school.</td></tr>
    </table>
    <h4>2. Speaking Stones: Debatteren en Overtuigen</h4>
    <ul>
      <li><i>The main reason why we need change is that climate change affects everyone.</i></li>
      <li><i>On the one hand solar energy is clean, but on the other hand installation costs are high.</i></li>
      <li><i>There is clear scientific evidence that recycling reduces waste.</i></li>
      <li><i>I understand your concern about costs, but in the long run it saves money.</i></li>
    </ul>
    <h4>3. Schrijfvaardigheid: Een Overtuigend Voorstel (Green Proposal)</h4>
    <p>Een overtuigend voorstel (bijv. aan de schoolleiding) bevat:</p>
    <ol>
      <li><b>Het probleem (The Issue):</b> <i>Our school generates excessive plastic waste daily.</i></li>
      <li><b>De voorgestelde oplossing (The Solution):</b> <i>We propose placing water refill stations in all hallways.</i></li>
      <li><b>De voordelen (The Benefits):</b> <i>This will cut plastic waste by 80% and promote healthy habits.</i></li>
    </ol>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which phrase is grammatically correct when suggesting a green initiative?", "opties": ["How about introducing recycling bins in the school cafeteria?", "How about to introduce recycling bins?", "Why don't we introducing recycling bins?", "Let's to introduce recycling bins."], "antwoord": 0, "uitleg": "'How about' wordt gevolgd door een werkwoord met -ing (introducing)."},
    {"type": "mc", "niveau": 1, "vraag": "How do you present two contrasting viewpoints in a formal debate?", "opties": ["On the one hand..., but on the other hand...", "First of all..., and finally...", "Because of..., despite of...", "Since yesterday..., until tomorrow..."], "antwoord": 0, "uitleg": "'On the one hand..., on the other hand...' weegt twee kanten af."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "The phrase <i>'In the long run'</i> means doing something that only matters for the next five minutes.", "antwoord": False, "uitleg": "Onwaar. 'In the long run' betekent op de lange termijn."},
    {"type": "invoer", "niveau": 1, "vraag": "Complete the suggestion: <i>Why ... we start a school vegetable garden?</i>", "antwoord": "don't|dont", "uitleg": "'Why don't we...' is de vaste formule."},
    {"type": "mc", "niveau": 2, "vraag": "What is the primary goal of a persuasive green proposal to the school principal?", "opties": ["To explain an environmental problem and convince leadership to implement a specific solution", "To ask for an extra week of summer vacation", "To complain about cafeteria sandwich prices", "To describe the history of medieval agriculture"], "antwoord": 0, "uitleg": "Een proposal overtuigt de leiding met een helder probleem en een haalbare oplossing."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "Using factual scientific data strengthens your arguments in an environmental debate.", "antwoord": True, "uitleg": "Waar. Feiten en wetenschappelijk bewijs maken een betoog overtuigend."},
    {"type": "invoer", "niveau": 2, "vraag": "Complete the phrase: <i>I ... that we install motion sensors for the classroom lighting.</i>", "antwoord": "suggest|propose", "uitleg": "'I suggest' of 'I propose' (ik stel voor)."},
    {"type": "mc", "niveau": 3, "vraag": "How can you politely acknowledge someone's counter-argument before presenting your own point?", "opties": ["I understand your concern regarding the budget, however, this investment pays for itself.", "Your argument is completely wrong and useless.", "I refuse to discuss financial matters with you.", "Nobody cares about the costs."], "antwoord": 0, "uitleg": "'I understand your concern..., however...' erkent het bezwaar beleefd alvorens een tegenargument te geven."}
  ]
}

# ==========================================
# 6. YOUR FUTURE
# ==========================================
h6_1 = {
  "id": "eng-h6-1",
  "hoofdstuk": 6,
  "paragraaf": "6.1",
  "titel": "Theme Words: Careers, Jobs, Qualifications & Skills",
  "korteUitleg": "Kernbegrippen rond beroepskeuze, solliciteren, vaardigheden en de arbeidsmarkt.",
  "icoon": "💼",
  "kleur": "h6-thema",
  "theorie": """
    <h3>6.1 Theme Words: Careers, Jobs, Qualifications & Skills</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Career, profession, ambition, qualification, resume / CV, job interview, employer, employee, salary, apprenticeship, degree, skills, teamwork, responsibility, application letter, vacancy, internship, freelance.
    </div>
    <h4>1. Beroepen en de Arbeidsmarkt (The Workplace)</h4>
    <table class="theorie-tabel">
      <tr><th>Engels Begrip</th><th>Nederlandse Betekenis</th><th>Voorbeeldzin</th></tr>
      <tr><td><b>Career</b></td><td>Loopbaan / Carrière</td><td>She wants to pursue a <i>career</i> in veterinary medicine.</td></tr>
      <tr><td><b>Employer vs. Employee</b></td><td>Werkgever vs. Werknemer</td><td>The <i>employer</i> hired five new enthusiastic <i>employees</i>.</td></tr>
      <tr><td><b>Vacancy</b></td><td>Openstaande vacature</td><td>The hospital posted a <i>vacancy</i> for a pediatric nurse.</td></tr>
      <tr><td><b>Salary / Wage</b></td><td>Salaris / Loon</td><td>He earns a competitive monthly <i>salary</i>.</td></tr>
      <tr><td><b>Internship / Apprenticeship</b></td><td>Stage / Leerwerkplek</td><td>An <i>internship</i> gives you hands-on practical experience.</td></tr>
    </table>
    <h4>2. Solliciteren en Kwalificaties</h4>
    <ul>
      <li><b>Resume / CV (Curriculum Vitae):</b> Een beknopt overzicht van je opleiding, werkervaring en vaardigheden.</li>
      <li><b>Application letter:</b> Een motivatiebrief waarin je uitlegt waarom jij geschikt bent voor de baan.</li>
      <li><b>Job interview:</b> Het officiële sollicitatiegesprek met de werkgever.</li>
      <li><b>Qualifications:</b> Je officiële diploma's en certificaten.</li>
      <li><b>Skills:</b> Je vaardigheden (bijv. <i>communication skills, problem-solving, teamwork</i>).</li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "What is the difference between an <b>employer</b> and an <b>employee</b>?", "opties": ["An employer is the boss/company that hires; an employee is the person who works there", "An employer is a student; an employee is a teacher", "There is no difference in British English", "An employee owns the business"], "antwoord": 0, "uitleg": "Employer = werkgever; employee = werknemer."},
    {"type": "mc", "niveau": 1, "vraag": "What is a <b>vacancy</b> in a company?", "opties": ["An available job opening that needs to be filled", "A summer holiday taken by the manager", "A special bonus payment for good work", "A broken office computer"], "antwoord": 0, "uitleg": "A vacancy is een openstaande vacature."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "A <b>resume (CV)</b> is a document detailing your education, work experience, and key skills.", "antwoord": True, "uitleg": "Waar. Een CV bevat je opleiding, ervaring en vaardigheden."},
    {"type": "invoer", "niveau": 1, "vraag": "Fill in the English word for <i>stage</i>: <i>During the summer, Duru completed a four-week ... at a media company.</i>", "antwoord": "internship", "uitleg": "Internship is het Engelse woord voor stage."},
    {"type": "mc", "niveau": 2, "vraag": "What does having good <b>teamwork skills</b> mean?", "opties": ["Being able to cooperate effectively and communicate well with colleagues", "Working completely alone without talking to anyone", "Playing video games during office hours", "Arriving late to every meeting"], "antwoord": 0, "uitleg": "Teamwork is het vermogen om goed samen te werken."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "An <b>apprenticeship</b> combines practical on-the-job training with classroom study.", "antwoord": True, "uitleg": "Waar. Een apprenticeship is een leerwerktraject."},
    {"type": "invoer", "niveau": 2, "vraag": "Fill in the missing word (sollicitatiegesprek): <i>She was invited for a job ... next Tuesday.</i>", "antwoord": "interview", "uitleg": "Job interview betekent sollicitatiegesprek."},
    {"type": "mc", "niveau": 3, "vraag": "What is the primary objective of an <b>application letter</b>?", "opties": ["To explain why you are interested in the vacancy and why your profile fits the role", "To ask for an immediate advance on your salary", "To criticize the company's website design", "To list your favorite movies and holiday destinations"], "antwoord": 0, "uitleg": "Een sollicitatiebrief licht toe waarom jij geschikt en gemotiveerd bent voor de functie."}
  ]
}

h6_2 = {
  "id": "eng-h6-2",
  "hoofdstuk": 6,
  "paragraaf": "6.2",
  "titel": "Grammar: Passive Voice & Second Conditional",
  "korteUitleg": "De lijdende vorm (Passive) en denkbeeldige voorwaardelijke zinnen (Second Conditional).",
  "icoon": "🎯",
  "kleur": "h6-thema",
  "theorie": """
    <h3>6.2 Grammar: Passive Voice & Second Conditional</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> De lijdende vorm (Passive Voice: <i>am/is/are + V3</i> en <i>was/were + V3</i>) en de Second Conditional (<i>If + Past Simple, would + hele ww</i>).
    </div>
    <h4>1. De Lijdende Vorm (Passive Voice)</h4>
    <p>In de lijdende vorm is het onderwerp de <b>ontvanger</b> van de handeling. Wie de handeling uitvoert (de <i>agent</i>) is onbekend of minder belangrijk.</p>
    <p><b>Vorm:</b> Vorm van <b>to be + voltooid deelwoord (Past Participle / 3e rijtje)</b>.</p>
    <table class="theorie-tabel">
      <tr><th>Tijd</th><th>Actieve Zin (Active)</th><th>Lijdende Vorm (Passive)</th></tr>
      <tr><td><b>Present Simple</b></td><td>They produce electric cars here.</td><td>Electric cars <b>are produced</b> here.</td></tr>
      <tr><td><b>Past Simple</b></td><td>The company hired Sarah yesterday.</td><td>Sarah <b>was hired</b> yesterday.</td></tr>
    </table>
    <p>Wil je toch noemen wie het deed? Gebruik dan <b>by</b>: <i>The email was sent <b>by</b> the manager.</i></p>
    <h4>2. De Second Conditional (Denkbeeldige Situatie)</h4>
    <p>Gebruik de <b>Second Conditional</b> voor hypothetische, onwaarschijnlijke of denkbeeldige situaties in het heden of de toekomst:</p>
    <div class="voorbeeld-box">
      <b>Structuur:</b> <i>If + Past Simple, ... would + hele werkwoord</i><br><br>
      <i>If I <b>had</b> more free time, I <b>would learn</b> Japanese.</i><br>
      <i>What job <b>would</b> you <b>choose</b> if money <b>wasn't</b> an issue?</i>
    </div>
    <ul>
      <li>In de if-bijzin staat de <b>Past Simple</b> (NIET <i>would</i>!).</li>
      <li>In de hoofdzin staat <b>would / wouldn't + hele werkwoord</b>.</li>
      <li>Bij <i>I / he / she</i> mag je in formele taal ook <i>were</i> gebruiken: <i>If I were you, I would accept the job offer.</i></li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which sentence is in the <b>Passive Voice</b>?", "opties": ["The new candidate was interviewed by the manager yesterday.", "The manager interviewed the new candidate yesterday.", "The candidate is answering every question confidently.", "The manager will call the candidate tomorrow."], "antwoord": 0, "uitleg": "'Was interviewed' is de lijdende vorm (to be + voltooid deelwoord)."},
    {"type": "mc", "niveau": 1, "vraag": "Which sentence correctly represents a <b>Second Conditional</b> structure?", "opties": ["If I won the lottery, I would travel around the world.", "If I win the lottery, I would travel around the world.", "If I will win the lottery, I traveled around the world.", "If I would win the lottery, I won."], "antwoord": 0, "uitleg": "If + Past Simple (won), resultaat = would + hele werkwoord (would travel)."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "In the <i>if-clause</i> of a Second Conditional sentence, you must use <i>would</i>.", "antwoord": False, "uitleg": "Onwaar. In het if-deel gebruik je de Past Simple (bijv. 'If I knew...'), nooit 'would'."},
    {"type": "invoer", "niveau": 1, "vraag": "Convert to Passive (Past Simple): <i>The company founded the branch in 2010. -> The branch ... founded in 2010.</i>", "antwoord": "was", "uitleg": "The branch (enkelvoud) -> was founded."},
    {"type": "mc", "niveau": 2, "vraag": "What does the idiom <i>'If I were in your shoes, I would...'</i> express?", "opties": ["Giving advice by imagining yourself in the other person's situation", "Asking to borrow someone's footwear for an interview", "Complaining about tight shoes", "Refusing to attend a meeting"], "antwoord": 0, "uitleg": "'If I were in your shoes' betekent 'als ik in jouw schoenen stond' (advies)."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "The Passive Voice is often used in formal and business English when the focus is on the action rather than who performed it.", "antwoord": True, "uitleg": "Waar. De lijdende vorm legt de nadruk op de handeling of het resultaat."},
    {"type": "invoer", "niveau": 2, "vraag": "Complete the Second Conditional: <i>If she ... (to have) more experience, she would get promoted.</i>", "antwoord": "had", "uitleg": "If + Past Simple: had."},
    {"type": "mc", "niveau": 3, "vraag": "Why is <i>'The documents was signed yesterday'</i> grammatically incorrect?", "opties": ["Because 'documents' is plural, requiring 'were signed' instead of 'was signed'", "Because 'signed' cannot be used in passive sentences", "Because 'yesterday' requires the Present Simple", "Because 'documents' must be placed after the verb"], "antwoord": 0, "uitleg": "Documents is meervoud, dus vereist 'were signed'."}
  ]
}

h6_3 = {
  "id": "eng-h6-3",
  "hoofdstuk": 6,
  "paragraaf": "6.3",
  "titel": "Stones & Skills: Job Interviews & Formal Application",
  "korteUitleg": "Vaste zinnen voor sollicitatiegesprekken, sterke/zwakke punten en formele brieven.",
  "icoon": "👔",
  "kleur": "h6-thema",
  "theorie": """
    <h3>6.3 Stones & Skills: Job Interviews & Formal Application</h3>
    <div class="info-box">
      <b>Communicatieve vaardigheden:</b> Sollicitatiegesprekken voeren (job interview etiquette), kwaliteiten beschrijven (strengths & weaknesses) en formele e-mailconventies.
    </div>
    <h4>1. Speaking Stones: Vragen en Antwoorden in een Sollicitatiegesprek</h4>
    <table class="theorie-tabel">
      <tr><th>Vraag van de Werkgever</th><th>Professioneel Antwoord</th></tr>
      <tr><td><i>Could you tell us a bit about yourself?</i></td><td><i>Certainly! I'm a motivated student with a strong passion for languages and teamwork.</i></td></tr>
      <tr><td><i>What are your greatest strengths?</i></td><td><i>My main strengths are reliability, problem-solving and excellent communication skills.</i></td></tr>
      <tr><td><i>How do you handle working under pressure?</i></td><td><i>I stay calm, prioritize urgent tasks and focus on finding solutions.</i></td></tr>
      <tr><td><i>Why are you interested in this position?</i></td><td><i>I believe this role aligns perfectly with my ambition to gain practical experience.</i></td></tr>
    </table>
    <h4>2. Schrijfvaardigheid: De Formele Sollicitatiebrief (Formal Application Letter)</h4>
    <p>Let op de strikte conventies van formele correspondentie in het Engels:</p>
    <ul>
      <li><b>Aanhef (Formal Salutation):</b><br>
        - Naam bekend: <i>Dear Mr. Davis, / Dear Ms. Wilson,</i><br>
        - Naam onbekend: <i>Dear Sir or Madam,</i></li>
      <li><b>Reden van schrijven (Opening statement):</b><br>
        <i>I am writing to apply for the position of junior assistant, as advertised on your website.</i></li>
      <li><b>Afsluiting & Bijlagen:</b><br>
        <i>I have attached my curriculum vitae for your consideration. / I look forward to hearing from you.</i></li>
      <li><b>Ondertekening (Formal Sign-off):</b><br>
        - Bij <i>Dear Sir or Madam</i> -> <i>Yours faithfully,</i><br>
        - Bij <i>Dear Mr./Ms. [Naam]</i> -> <i>Yours sincerely,</i></li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "niveau": 1, "vraag": "Which opening is the most appropriate for a <b>formal</b> job application letter when you know the manager's name (Mr. Clark)?", "opties": ["Dear Mr. Clark,", "Hey Clark,", "Hi there buddy,", "What's up Mr. Clark,"], "antwoord": 0, "uitleg": "'Dear Mr. Clark,' is de correcte formele aanhef."},
    {"type": "mc", "niveau": 1, "vraag": "If you begin a formal letter with <i>'Dear Sir or Madam,'</i>, how should you sign off at the end?", "opties": ["Yours faithfully,", "Best regards buddy,", "Love and hugs,", "Catch you later,"], "antwoord": 0, "uitleg": "Bij 'Dear Sir or Madam' hoort traditioneel 'Yours faithfully,'."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "In a formal job interview, it is recommended to describe your strengths with clear practical examples.", "antwoord": True, "uitleg": "Waar. Concrete voorbeelden maken je kwaliteiten overtuigend."},
    {"type": "invoer", "niveau": 1, "vraag": "Complete the formal sentence: <i>I am writing to ... for the position of sales assistant.</i>", "antwoord": "apply", "uitleg": "'To apply for a position' betekent solliciteren naar een functie."},
    {"type": "mc", "niveau": 2, "vraag": "How can you professionally explain a personal weakness during an interview?", "opties": ["Acknowledge the area of improvement and explain the active steps you take to overcome it", "Pretend that you are 100% perfect in every possible way", "Blame your former teachers for your mistakes", "Refuse to answer any difficult questions"], "antwoord": 0, "uitleg": "Een verbeterpunt benoemen en laten zien hoe je eraan werkt toont zelfinzicht."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "When you address a letter to <i>'Dear Ms. Jenkins,'</i>, you should close with <i>'Yours sincerely,'</i>.", "antwoord": True, "uitleg": "Waar. Bij een bekende naam gebruik je 'Yours sincerely,'."},
    {"type": "invoer", "niveau": 2, "vraag": "Complete the phrase: <i>I have ... my CV for your review.</i>", "antwoord": "attached|enclosed", "uitleg": "'Attached' (als bijlage toegevoegd) is het juiste woord."},
    {"type": "mc", "niveau": 3, "vraag": "What is the primary function of the sentence <i>'I look forward to hearing from you at your earliest convenience'</i>?", "opties": ["To conclude a formal letter politely while expressing anticipation for a reply", "To demand an immediate cash payment", "To schedule a mandatory phone call in ten seconds", "To reject a job offer permanently"], "antwoord": 0, "uitleg": "Het is een beleefde formele slotzin die uitziet naar een reactie."}
  ]
}

# Write all 18 Onderwerpen
all_onderwerpen = [
  ("h1_1.js", h1_1), ("h1_2.js", h1_2), ("h1_3.js", h1_3),
  ("h2_1.js", h2_1), ("h2_2.js", h2_2), ("h2_3.js", h2_3),
  ("h3_1.js", h3_1), ("h3_2.js", h3_2), ("h3_3.js", h3_3),
  ("h4_1.js", h4_1), ("h4_2.js", h4_2), ("h4_3.js", h4_3),
  ("h5_1.js", h5_1), ("h5_2.js", h5_2), ("h5_3.js", h5_3),
  ("h6_1.js", h6_1), ("h6_2.js", h6_2), ("h6_3.js", h6_3)
]

for filename, data in all_onderwerpen:
    write_onderwerp(filename, data)

print("\n🎉 ALL 18 ONDERWERPEN SUCCESSFULLY GENERATED!")
