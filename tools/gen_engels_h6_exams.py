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

# EXAMEN 26: H6 Theme Words (Careers, Workplace & Skills) (20 questions)
ex26 = {
  "id": "ex-h3-eng-26",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Hoofdstuk 6 — Your future",
  "titel": "Toets 1 — Theme Words: Careers, Jobs, Qualifications & Skills",
  "vak": "Engels · HAVO 3 (H6)",
  "icoon": "💼",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "What is the crucial difference between an <b>employer</b> and an <b>employee</b>?", "opties": ["An employer is the person or company that hires workers; an employee is the individual hired to work", "An employer is a high school student; an employee is a university professor", "There is no difference in British labour law", "An employee owns the entire company"], "antwoord": 0, "uitleg": "Employer = werkgever; employee = werknemer."},
    {"type": "mc", "vraag": "What is a <b>vacancy</b> in an organization?", "opties": ["An available job opening that a company wants to fill with a new employee", "A summer holiday period for senior managers", "A special bonus added to monthly wages", "A broken office computer waiting for repair"], "antwoord": 0, "uitleg": "A vacancy is een openstaande vacature."},
    {"type": "waaronwaar", "vraag": "A <b>resume (CV)</b> is a document detailing your educational background, employment history, and skills.", "antwoord": True, "uitleg": "Waar. Een CV geeft een overzicht van opleiding, werkervaring en competenties."},
    {"type": "invul", "vraag": "Fill in the English word for <i>stage</i>: <i>She completed a six-month ... at a graphic design agency.</i>", "antwoord": "internship", "uitleg": "Internship is het Engelse woord voor stage."},
    {"type": "mc", "vraag": "What does having strong <b>teamwork skills</b> involve?", "opties": ["Collaborating constructively, communicating openly, and supporting colleagues to achieve common goals", "Working entirely alone in an isolated room without speaking to anyone", "Playing multiplayer video games during office hours", "Leaving team meetings early without notice"], "antwoord": 0, "uitleg": "Teamwork omvat constructieve samenwerking en open communicatie."},
    {"type": "waaronwaar", "vraag": "An <b>apprenticeship</b> provides practical on-the-job training combined with structured classroom study.", "antwoord": True, "uitleg": "Waar. Een apprenticeship combineert praktijkleren met theorie."},
    {"type": "invul", "vraag": "Fill in the noun (sollicitatiegesprek): <i>He prepared thoroughly for his upcoming job ... with the director.</i>", "antwoord": "interview", "uitleg": "Job interview is het sollicitatiegesprek."},
    {"type": "mc", "vraag": "What are <b>qualifications</b> in a professional context?", "opties": ["Official diplomas, degrees, or certifications that demonstrate a person's competence to perform a role", "The clothing styles preferred by office staff", "The speed at which an employee drinks coffee", "The brand of laptop provided by an employer"], "antwoord": 0, "uitleg": "Kwalificaties zijn officiële diploma's en certificaten."},
    {"type": "mc", "vraag": "What is a <b>salary</b>?", "opties": ["A fixed regular payment, typically paid on a monthly basis, by an employer to an employee", "A voluntary tip given to restaurant waiters", "A fine paid for parking incorrectly at work", "A discount coupon for office supplies"], "antwoord": 0, "uitleg": "Salary is een vast maandelijks salaris."},
    {"type": "waaronwaar", "vraag": "A <b>freelancer</b> is someone who works for themselves and provides services to multiple clients on contract.", "antwoord": True, "uitleg": "Waar. Een freelancer is zelfstandig ondernemer."},
    {"type": "invul", "vraag": "Fill in the noun for <i>loopbaan / carrière</i>: <i>Duru aims to pursue a rewarding ... in modern education.</i>", "antwoord": "career", "uitleg": "Career betekent loopbaan of carrière."},
    {"type": "mc", "vraag": "What does the word <b>ambition</b> mean?", "opties": ["A strong desire and determination to achieve success, goals, or distinction in life", "The total number of hours worked per week", "The cost of commuting to work by train", "A feeling of boredom during meetings"], "antwoord": 0, "uitleg": "Ambition is de gedrevenheid om doelen te bereiken."},
    {"type": "open", "vraag": "Why are interpersonal qualities like problem-solving and communication increasingly valued alongside academic certificates?", "sleutelwoorden": ["colleagues/clients/flexible/adapt/team", "workplace/practical/collaboration/real"], "minTreffers": 1, "modelantwoord": "Soft skills allow employees to adapt, communicate clearly with clients and colleagues, and solve unexpected workplace problems effectively.", "uitleg": "Sociale vaardigheden en flexibiliteit zijn onmisbaar om goed samen te werken en problemen op te lossen."},
    {"type": "mc", "vraag": "What is a <b>degree</b> in higher education?", "opties": ["An academic qualification awarded by a university upon successful completion of a course of study", "The temperature inside a lecture hall", "The angle of an architect's drafting table", "A discount card for university textbooks"], "antwoord": 0, "uitleg": "A degree is een academische graad / universitair diploma."},
    {"type": "waaronwaar", "vraag": "An <b>application letter</b> should just be a blank page with your phone number scrawled in pencil.", "antwoord": False, "uitleg": "Onwaar. Een sollicitatiebrief moet een gestructureerde motivatie en profielschets bevatten."},
    {"type": "invul", "vraag": "Fill in the noun (verantwoordelijkheid): <i>Leadership roles require taking full ... for team results.</i>", "antwoord": "responsibility", "uitleg": "Responsibility betekent verantwoordelijkheid."},
    {"type": "mc", "vraag": "What does <b>full-time employment</b> typically mean in Europe?", "opties": ["Working around 36 to 40 hours per week under a standard employment contract", "Working 5 hours on Saturday mornings only", "Working only on national bank holidays", "Working 100 hours without sleep"], "antwoord": 0, "uitleg": "Fulltime werk is gemiddeld 36-40 uur per week."},
    {"type": "waaronwaar", "vraag": "In modern workplaces, being adaptable and willing to learn new digital tools is essential for career longevity.", "antwoord": True, "uitleg": "Waar. Flexibiliteit en een leergierige houding zijn essentieel op de arbeidsmarkt."},
    {"type": "invul", "vraag": "Complete the phrase: <i>She demonstrated excellent leadership ... during the group project.</i>", "antwoord": "skills|qualities|abilities", "uitleg": "Leadership skills / qualities."},
    {"type": "mc", "vraag": "Which word is a synonym for <b>profession</b>?", "opties": ["Occupation / Career", "Vacation", "Hobby", "Accident"], "antwoord": 0, "uitleg": "Occupation of career is een synoniem voor profession."}
  ]
}

# EXAMEN 27: H6 Grammar (Passive Voice & Second Conditional) (20 questions)
ex27 = {
  "id": "ex-h3-eng-27",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Hoofdstuk 6 — Your future",
  "titel": "Toets 2 — Grammar: Passive Voice & Second Conditional",
  "vak": "Engels · HAVO 3 (H6)",
  "icoon": "🎯",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Which sentence is correctly in the <b>Passive Voice</b> (Past Simple)?", "opties": ["The new software engineer was hired by the tech firm yesterday.", "The tech firm hired the software engineer yesterday.", "The software engineer is hiring new candidates right now.", "The tech firm was hire the software engineer."], "antwoord": 0, "uitleg": "'Was hired' is de lijdende vorm in de verleden tijd (was + voltooid deelwoord)."},
    {"type": "mc", "vraag": "Which sentence correctly represents a <b>Second Conditional</b> (hypothetical situation)?", "opties": ["If I had more experience, I would apply for that senior managerial role.", "If I have more experience, I would apply for that role.", "If I will have more experience, I applied for that role.", "If I would have experience, I had applied."], "antwoord": 0, "uitleg": "If + Past Simple (had), resultaat = would + hele werkwoord (would apply)."},
    {"type": "waaronwaar", "vraag": "In the <i>if-clause</i> of a Second Conditional sentence, you should use <i>would</i> (e.g. <i>If I would know</i>).", "antwoord": False, "uitleg": "Onwaar. In de if-bijzin gebruik je de Past Simple, NOOIT would."},
    {"type": "invul", "vraag": "Convert to Passive (Present Simple): <i>Millions of resumes ... (to submit) online every week.</i>", "antwoord": "are submitted", "uitleg": "Resumes (meervoud) -> are submitted."},
    {"type": "mc", "vraag": "Choose the correct Second Conditional sentence for giving advice:", "opties": ["If I were you, I would accept the internship offer immediately.", "If I was you, I will accept the internship offer.", "If I am you, I would accept the offer.", "If I would be you, I accepted the offer."], "antwoord": 0, "uitleg": "'If I were you, I would...' is de formele en correcte adviesconstructie."},
    {"type": "waaronwaar", "vraag": "The preposition <b>by</b> is used in passive sentences to introduce the agent who performed the action (e.g. <i>written by Shakespeare</i>).", "antwoord": True, "uitleg": "Waar. 'By' introduceert de handelende persoon in een passieve zin."},
    {"type": "invul", "vraag": "Fill in the correct form: <i>If he ... (to speak) fluent German, he would get the international job in Berlin.</i>", "antwoord": "spoke", "uitleg": "If + Past Simple: spoke."},
    {"type": "mc", "vraag": "Convert to Passive (Past Simple): <i>Alexander Bell invented the telephone in 1876.</i>", "opties": ["The telephone was invented by Alexander Bell in 1876.", "The telephone has been invented in 1876 by Bell.", "The telephone were invented by Bell in 1876.", "The telephone is invented by Bell in 1876."], "antwoord": 0, "uitleg": "The telephone (enkelvoud) -> was invented by... in 1876."},
    {"type": "mc", "vraag": "Why is <i>'The contracts was signed by both parties'</i> grammatically incorrect?", "opties": ["Contracts is plural, requiring 'were signed' rather than 'was signed'", "Signed cannot be used in the passive voice", "By must be replaced with from", "Both must be removed"], "antwoord": 0, "uitleg": "Contracts is meervoud, dus vereist 'were signed'."},
    {"type": "waaronwaar", "vraag": "The Second Conditional is used for real, highly probable situations happening tomorrow morning.", "antwoord": False, "uitleg": "Onwaar. De Second Conditional is voor denkbeeldige, hypothetische of onwaarschijnlijke situaties."},
    {"type": "invul", "vraag": "Complete the Second Conditional: <i>What would you do if you ... (to win) one million euros?</i>", "antwoord": "won", "uitleg": "If + Past Simple: won."},
    {"type": "mc", "vraag": "Choose the correct Passive sentence (Present Simple):", "opties": ["English is spoken in dozens of countries worldwide.", "English speaks in dozens of countries worldwide.", "English was spoken in countries worldwide right now.", "English has speak in countries."], "antwoord": 0, "uitleg": "English (enkelvoud) -> is spoken."},
    {"type": "open", "vraag": "Rewrite this active sentence into the passive voice: <i>'The director approved the new budget yesterday.'</i>", "sleutelwoorden": ["the new budget was approved by the director yesterday/was approved"], "minTreffers": 1, "modelantwoord": "The new budget was approved by the director yesterday.", "uitleg": "Lijdende vorm: The new budget was approved by the director yesterday."},
    {"type": "mc", "vraag": "Choose the correct verb form: <i>If we lived closer to London, we ... (to visit) the science museum more often.</i>", "opties": ["would visit", "will visit", "visited", "have visited"], "antwoord": 0, "uitleg": "Second Conditional resultaat = would + hele werkwoord (would visit)."},
    {"type": "waaronwaar", "vraag": "In formal business English, the Passive Voice is often chosen to emphasize the outcome rather than the individual worker.", "antwoord": True, "uitleg": "Waar. De lijdende vorm legt de focus op het proces of resultaat."},
    {"type": "invul", "vraag": "Fill in the verb (Past Simple Passive): <i>The emails ... (to send) to all staff members at 9 AM.</i>", "antwoord": "were sent", "uitleg": "Emails (meervoud) -> were sent."},
    {"type": "mc", "vraag": "Which sentence correctly expresses an unreal wish about the present?", "opties": ["I wish I had more free time to practice coding.", "I wish I have more free time.", "I wish I will have more time.", "I wish I am having more time."], "antwoord": 0, "uitleg": "'I wish + Past Simple' (had) drukt een denkbeeldige wens uit in het heden."},
    {"type": "waaronwaar", "vraag": "The past participle of <i>to build</i> is <i>builded</i>.", "antwoord": False, "uitleg": "Onwaar. Build -> built -> built."},
    {"type": "invul", "vraag": "Complete the Second Conditional: <i>If she had a driver's license, she ... drive to work.</i>", "antwoord": "would|could", "uitleg": "Resultaat = would / could drive."},
    {"type": "mc", "vraag": "Choose the correct Passive sentence:", "opties": ["Coffee is grown in tropical mountain regions.", "Coffee grows people in mountain regions.", "Coffee were grown in tropical regions currently.", "Coffee are grown in mountain regions."], "antwoord": 0, "uitleg": "Coffee (enkelvoud) -> is grown."}
  ]
}

# EXAMEN 28: H6 Stones & Job Interviews (20 questions)
ex28 = {
  "id": "ex-h3-eng-28",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Hoofdstuk 6 — Your future",
  "titel": "Toets 3 — Stones & Skills: Interview Etiquette & Strengths",
  "vak": "Engels · HAVO 3 (H6)",
  "icoon": "👔",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "How do you respond professionally when an interviewer asks: <i>'Could you tell us about yourself?'</i>?", "opties": ["Certainly! I am an ambitious student with a strong passion for languages and problem-solving.", "Why do you want to know my private life?", "Look at my social media profile on your phone.", "I prefer not to talk about myself."], "antwoord": 0, "uitleg": "Een beknopte, enthousiaste introductie van je achtergrond en kwaliteiten."},
    {"type": "mc", "vraag": "What is the best way to highlight your personal strengths in an interview?", "opties": ["My key strengths are reliability, punctuality, and excellent communication skills, illustrated by my school projects.", "I am better than everyone else in the world.", "I never make any mistakes ever.", "I don't have any particular strengths."], "antwoord": 0, "uitleg": "Kwaliteiten benoemen met concrete voorbeelden toont professionaliteit."},
    {"type": "waaronwaar", "vraag": "In a job interview, arriving ten minutes early demonstrates punctuality and respect for the employer.", "antwoord": True, "uitleg": "Waar. Op tijd komen toont punctualiteit en respect."},
    {"type": "invul", "vraag": "Complete the interview phrase: <i>I am writing to ... for the advertised internship position.</i>", "antwoord": "apply", "uitleg": "'To apply for a position' (solliciteren)."},
    {"type": "mc", "vraag": "How should you answer when asked about a personal weakness?", "opties": ["Identify an area for improvement and describe the constructive steps you take to develop it.", "Say you have zero flaws and are completely perfect.", "Criticize your previous teachers for your low grades.", "Refuse to answer the question."], "antwoord": 0, "uitleg": "Een ontwikkelpunt benoemen en laten zien hoe je eraan werkt."},
    {"type": "waaronwaar", "vraag": "Chewing gum loudly and looking at your smartphone during a job interview is considered excellent professional etiquette.", "antwoord": False, "uitleg": "Onwaar. Dit is onbeleefd en onprofessioneel."},
    {"type": "invul", "vraag": "Complete the phrase: <i>I look forward to ... from you regarding my application.</i>", "antwoord": "hearing", "uitleg": "'Look forward to hearing from you'."},
    {"type": "mc", "vraag": "Which phrase expresses that you handle stress effectively?", "opties": ["I stay calm under pressure, prioritize urgent tasks, and focus on practical solutions.", "When I get stressed, I shout at my colleagues.", "I go home immediately whenever work becomes difficult.", "Stress causes me to delete company files."], "antwoord": 0, "uitleg": "Toont stressbestendigheid en oplossingsgerichtheid."},
    {"type": "mc", "vraag": "What is the appropriate dress code for a corporate office job interview?", "opties": ["Smart, professional, and neat attire suitable for the company culture", "Beachwear with flip-flops and sunglasses", "Torn sweatpants and a dirty gaming t-shirt", "A medieval knight armor costume"], "antwoord": 0, "uitleg": "Verzorgde en representatieve kleding."},
    {"type": "waaronwaar", "vraag": "Asking thoughtful questions about the company and team at the end of the interview shows genuine interest and initiative.", "antwoord": True, "uitleg": "Waar. Vragen stellen toont oprechte motivatie en interesse."},
    {"type": "invul", "vraag": "Complete the question you can ask the interviewer: <i>What does a typical day look ... in this role?</i>", "antwoord": "like", "uitleg": "'What does it look like?' (hoe ziet het eruit?)."},
    {"type": "mc", "vraag": "Which phrase is the standard polite opening for a formal letter when you know the recipient's surname (Dr. Adams)?", "opties": ["Dear Dr. Adams,", "Hey Adams,", "Hi there friend,", "What's going on Adams,"], "antwoord": 0, "uitleg": "'Dear Dr. Adams,' is de correcte formele aanhef."},
    {"type": "open", "vraag": "Why is sending a short follow-up note after an interview considered good professional practice?", "sleutelwoorden": ["gratitude/appreciation/polite/manner/courtesy", "reiterate/interest/impression/enthusiasm/candidate"], "minTreffers": 1, "modelantwoord": "It shows polite gratitude for the interviewer's time, leaves a positive lasting impression, and reaffirms your enthusiasm for the position.", "uitleg": "Een bedankmail toont beleefdheid, laat een goede indruk achter en onderstreept je enthousiasme."},
    {"type": "mc", "vraag": "If you address a formal letter to <i>'Dear Sir or Madam,'</i>, how should you sign off at the end?", "opties": ["Yours faithfully,", "Best regards buddy,", "Lots of love,", "See you next week,"], "antwoord": 0, "uitleg": "Bij 'Dear Sir or Madam' hoort traditioneel 'Yours faithfully,'."},
    {"type": "waaronwaar", "vraag": "When you know the recipient's name (e.g. <i>Dear Ms. Henderson,</i>), the correct formal sign-off is <i>Yours sincerely,</i>.", "antwoord": True, "uitleg": "Waar. Bij een bekende naam gebruik je 'Yours sincerely,'."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>I have ... my CV and references for your review.</i>", "antwoord": "attached|enclosed", "uitleg": "'Attached / enclosed my CV'."},
    {"type": "mc", "vraag": "What is the best way to explain why you want to work for a specific company?", "opties": ["Your company's innovative projects and collaborative culture strongly align with my career ambitions.", "I heard you have free coffee in the break room.", "My parents forced me to send twenty random applications today.", "I just need money to buy concert tickets."], "antwoord": 0, "uitleg": "Verbindt de bedrijfscultuur en projecten met jouw eigen ambities."},
    {"type": "waaronwaar", "vraag": "Maintaining steady eye contact and offering a firm handshake (or polite nod) conveys confidence and engagement.", "antwoord": True, "uitleg": "Waar. Oogcontact straalt zelfvertrouwen en betrokkenheid uit."},
    {"type": "invul", "vraag": "Complete the formal closing: <i>Yours ..., Duru Özdemir.</i>", "antwoord": "sincerely|faithfully", "uitleg": "Yours sincerely / faithfully."},
    {"type": "mc", "vraag": "What should you never do on your resume (CV)?", "opties": ["Include false information or fabricated work qualifications", "List your real contact details clearly", "Highlight your genuine language skills", "Organize work history in reverse chronological order"], "antwoord": 0, "uitleg": "Liegen op je CV is verboden en leidt tot direct ontslag."}
  ]
}

# EXAMEN 29: H6 Reading & Job Ad Analysis (20 questions)
ex29 = {
  "id": "ex-h3-eng-29",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Hoofdstuk 6 — Your future",
  "titel": "Toets 4 — Reading Skills: Vacancy Advertisements & Profiles",
  "vak": "Engels · HAVO 3 (H6)",
  "icoon": "📄",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "What are <b>requirements</b> in a job vacancy advertisement?", "opties": ["The mandatory qualifications, skills, and experience an applicant must possess to be considered", "The list of cafeteria lunch options provided by the company", "The paint color of the office desks", "The hobbies of the CEO"], "antwoord": 0, "uitleg": "Requirements zijn de verplichte functie-eisen."},
    {"type": "mc", "vraag": "What does <b>competitive salary</b> mean in a job listing?", "opties": ["A wage that matches or exceeds the average market rate for similar positions in that industry", "A salary decided by a boxing match between employees", "A salary that decreases every month", "A zero-euro volunteer contract"], "antwoord": 0, "uitleg": "Een marktconform en aantrekkelijk salaris."},
    {"type": "waaronwaar", "vraag": "The <b>job description</b> outlines the primary tasks, duties, and responsibilities associated with the role.", "antwoord": True, "uitleg": "Waar. De functieomschrijving beschrijft taken en verantwoordelijkheden."},
    {"type": "invul", "vraag": "Fill in the recruitment term (openstaande vacature): <i>The international school posted an urgent ... for a biology teacher.</i>", "antwoord": "vacancy|job opening", "uitleg": "Vacancy / job opening is een vacature."},
    {"type": "mc", "vraag": "What does <b>deadline for applications</b> signify?", "opties": ["The final date and time by which job application materials must be received", "The day the new building opens", "The date the company was founded in 1990", "The time the daily mail arrives"], "antwoord": 0, "uitleg": "De uiterste inzenddatum voor sollicitaties."},
    {"type": "waaronwaar", "vraag": "If an advertisement states <i>'Fluency in English is essential'</i>, candidates who speak no English will be shortlisted immediately.", "antwoord": False, "uitleg": "Onwaar. 'Essential' betekent dat het een strikte vereiste is."},
    {"type": "invul", "vraag": "Fill in the noun (voordeel / extraatje): <i>Company ... include a gym membership and private health insurance.</i>", "antwoord": "benefits|perks", "uitleg": "Benefits / perks zijn secundaire arbeidsvoorwaarden."},
    {"type": "mc", "vraag": "What does <b>hybrid working</b> mean in contemporary employment advertisements?", "opties": ["A working model combining remote home office days with in-person office days", "Driving only hybrid electric cars to meetings", "Working exclusively during nighttime hours", "Sharing a single desk with four colleagues simultaneously"], "antwoord": 0, "uitleg": "Hybride werken combineert thuiswerken met kantoordagen."},
    {"type": "mc", "vraag": "What is the role of <b>references</b> in an application process?", "opties": ["Previous employers or teachers who can verify an applicant's work ethic, character, and competence", "Books recommended by the library", "Dictionary definitions of job titles", "Computer passwords stored on a server"], "antwoord": 0, "uitleg": "Referenties zijn contactpersonen die jouw kwaliteiten kunnen bevestigen."},
    {"type": "waaronwaar", "vraag": "A <b>cover letter</b> should be tailored specifically to the company and role you are applying for.", "antwoord": True, "uitleg": "Waar. Een motivatiebrief moet afgestemd zijn op de specifieke functie."},
    {"type": "invul", "vraag": "Fill in the noun (kandidaat / sollicitant): <i>Over fifty qualified ... applied for the management position.</i>", "antwoord": "applicants|candidates", "uitleg": "Applicants / candidates (sollicitanten)."},
    {"type": "mc", "vraag": "What does <b>hands-on experience</b> mean?", "opties": ["Practical, direct knowledge and skills gained from actually performing a task or job", "Wearing protective latex gloves at all times", "Writing notes using a fountain pen", "Working as a massage therapist"], "antwoord": 0, "uitleg": "Hands-on experience is praktische werkervaring."},
    {"type": "open", "vraag": "Why is it important for an applicant to align their motivation letter with the criteria listed in a job advert?", "sleutelwoorden": ["demonstrate/align/fit/qualification/criteria", "stand out/employer/hiring/shortlist/selection"], "minTreffers": 1, "modelantwoord": "Matching keywords shows the employer clearly that your profile satisfies their exact requirements and criteria.", "uitleg": "Trefwoorden laten de werkgever direct zien dat jouw profiel aansluit op de functie-eisen."},
    {"type": "mc", "vraag": "What is meant by a <b>probation period</b> in a new employment contract?", "opties": ["An initial trial period during which both employer and employee assess if the fit is right", "A mandatory legal punishment for late arrivals", "A training camp in the military", "A five-year unpaid internship"], "antwoord": 0, "uitleg": "Een proeftijd waarin beide partijen de samenwerking beoordelen."},
    {"type": "waaronwaar", "vraag": "Job advertisements only look for technical skills and completely ignore communication and teamwork.", "antwoord": False, "uitleg": "Onwaar. Soft skills (communicatie, samenwerking) worden vrijwel altijd gevraagd."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>Candidates must be able to work under ... and meet tight deadlines.</i>", "antwoord": "pressure", "uitleg": "'Work under pressure' (onder druk werken)."},
    {"type": "mc", "vraag": "What does <b>equal opportunity employer</b> signify in a vacancy?", "opties": ["The organization does not discriminate based on race, gender, religion, age, or disability", "Every employee receives the exact same salary regardless of position", "All applicants are hired on the spot without an interview", "The company operates only on weekends"], "antwoord": 0, "uitleg": "Gelijke kansen voor iedereen zonder discriminatie."},
    {"type": "waaronwaar", "vraag": "Scanning a job vacancy for bullet points allows you to find key requirements quickly.", "antwoord": True, "uitleg": "Waar. Opsommingstekens geven direct overzicht van de functie-eisen."},
    {"type": "invul", "vraag": "Complete the phrase: <i>We offer excellent opportunities for career ... and promotion.</i>", "antwoord": "growth|development|advancement", "uitleg": "Career growth / development / advancement."},
    {"type": "mc", "vraag": "What is the purpose of an <b>exit interview</b> when leaving a job?", "opties": ["To provide feedback about your work experience and reasons for moving on to help the company improve", "To lock the office door behind you", "To surrender your passport to the manager", "To demand double wages for your last week"], "antwoord": 0, "uitleg": "Een eindgesprek waarin feedback wordt gegeven over de werkervaring."}
  ]
}

# EXAMEN 30: H6 Hoofdstuk Eindtoets (Mix & Sınav Simülasyonu) (20 questions)
ex30 = {
  "id": "ex-h3-eng-30",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Hoofdstuk 6 — Your future",
  "titel": "Toets 5 — Hoofdstuk 6 Eindtoets (Mix & Examen)",
  "vak": "Engels · HAVO 3 (H6)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "How do the roles of an <b>employer</b> and an <b>employee</b> differ in the workplace?", "opties": ["An employer hires workers and manages the organization; an employee works for the company in exchange for a salary", "An employer is a volunteer; an employee owns the business", "There is no difference in modern English", "An employee hires the manager"], "antwoord": 0, "uitleg": "Employer = werkgever; employee = werknemer."},
    {"type": "mc", "vraag": "Choose the correct Passive sentence (Past Simple):", "opties": ["The successful candidate was chosen by the recruitment panel yesterday.", "The recruitment panel was chose the candidate yesterday.", "The candidate is chosen yesterday.", "The candidate were chosen by the panel yesterday."], "antwoord": 0, "uitleg": "Candidate (enkelvoud) -> was chosen by... yesterday."},
    {"type": "waaronwaar", "vraag": "A <b>resume (CV)</b> should include your educational qualifications, work experience, and key skills.", "antwoord": True, "uitleg": "Waar. Een CV bevat je opleiding, ervaring en competenties."},
    {"type": "invul", "vraag": "Fill in the English word for <i>stage</i>: <i>During her gap year, she completed an ... at an international law firm.</i>", "antwoord": "internship", "uitleg": "Internship is een stage."},
    {"type": "mc", "vraag": "Choose the correct Second Conditional sentence:", "opties": ["If I had more time, I would learn how to code in Python.", "If I have more time, I would learn coding.", "If I will have time, I learned coding.", "If I would have time, I had learned."], "antwoord": 0, "uitleg": "If + Past Simple (had), resultaat = would + hele werkwoord (would learn)."},
    {"type": "waaronwaar", "vraag": "In the <i>if-clause</i> of a Second Conditional sentence, using <i>would</i> is standard grammar.", "antwoord": False, "uitleg": "Onwaar. In het if-deel gebruik je de Past Simple, NOOIT would."},
    {"type": "invul", "vraag": "Fill in the noun (sollicitatiegesprek): <i>She received an invitation for a formal job ... next Thursday.</i>", "antwoord": "interview", "uitleg": "Job interview is een sollicitatiegesprek."},
    {"type": "mc", "vraag": "How do you politely sign off a formal letter addressed to <i>'Dear Mr. Peterson,'</i>?", "opties": ["Yours sincerely,", "Yours faithfully,", "Best regards buddy,", "Catch you later,"], "antwoord": 0, "uitleg": "Bij een bekende naam gebruik je 'Yours sincerely,'."},
    {"type": "mc", "vraag": "What is a <b>vacancy</b>?", "opties": ["An open job position available to be filled by a new worker", "A scheduled holiday for school students", "An emergency fire drill in an office", "A broken printer in the hallway"], "antwoord": 0, "uitleg": "A vacancy is een openstaande vacature."},
    {"type": "waaronwaar", "vraag": "If you address a formal application letter to <i>'Dear Sir or Madam,'</i>, you should sign off with <i>Yours faithfully,</i>.", "antwoord": True, "uitleg": "Waar. Bij 'Dear Sir or Madam' hoort 'Yours faithfully,'."},
    {"type": "invul", "vraag": "Convert to Passive (Present Simple): <i>German and French ... (to teach) at our high school.</i>", "antwoord": "are taught", "uitleg": "German and French (meervoud) -> are taught."},
    {"type": "mc", "vraag": "What does <b>teamwork</b> require in the workplace?", "opties": ["Active listening, clear communication, mutual support, and cooperation", "Ignoring colleagues and working with headphones on all day", "Arriving two hours late to every team meeting", "Refusing to share any information"], "antwoord": 0, "uitleg": "Teamwork vraagt om actieve communicatie en samenwerking."},
    {"type": "open", "vraag": "Explain how learning English fluently in secondary school creates valuable advantages for higher education and future employment across the world.", "sleutelwoorden": ["international/worldwide/multinational/abroad/foreign", "opportunity/career/profession/study/doors"], "minTreffers": 1, "modelantwoord": "English is the global language of business, science, and higher education, opening doors to study abroad and international career opportunities.", "uitleg": "Engels is de wereldtaal van wetenschap en internationale handel en biedt toegang tot buitenlandse studies en carrières."},
    {"type": "mc", "vraag": "Choose the correct advice sentence:", "opties": ["If I were in your position, I would accept the job offer.", "If I am in your position, I will accepted the offer.", "If I would be you, I accepted the job.", "If I was you, I am accept the job."], "antwoord": 0, "uitleg": "'If I were in your position, I would accept...' is de juiste vorm."},
    {"type": "waaronwaar", "vraag": "An <b>apprenticeship</b> is strictly an unpaid five-minute computer tutorial.", "antwoord": False, "uitleg": "Onwaar. Een apprenticeship is een volwaardig leerwerktraject met praktische ervaring en theorie."},
    {"type": "invul", "vraag": "Fill in the noun (salaris): <i>Employees receive their monthly ... on the 25th of each month.</i>", "antwoord": "salary|wage|pay", "uitleg": "Salary / wage is het salaris."},
    {"type": "mc", "vraag": "Which phrase describes a document you attach to your application letter?", "opties": ["I have attached my curriculum vitae for your consideration.", "I deleted my application file yesterday.", "Where is the post office located?", "I do not have any papers."], "antwoord": 0, "uitleg": "'I have attached my CV...' verwijst formeel naar de bijlage."},
    {"type": "waaronwaar", "vraag": "The Passive Voice is formed using a form of <i>to be</i> + the past participle (3e rijtje).", "antwoord": True, "uitleg": "Waar. To be + voltooid deelwoord."},
    {"type": "invul", "vraag": "Complete the phrase: <i>She demonstrated strong problem-solving ... during the internship.</i>", "antwoord": "skills|abilities", "uitleg": "Problem-solving skills / abilities."},
    {"type": "mc", "vraag": "What is meant by an <b>internship</b>?", "opties": ["A temporary position with an organization to gain practical work experience in a field", "A permanent contract as the company president", "A ten-year paid holiday in the Caribbean", "A university exam without any questions"], "antwoord": 0, "uitleg": "Een stage om praktijkervaring op te doen in een vakgebied."}
  ]
}

write_examen("examen_26.js", ex26)
write_examen("examen_27.js", ex27)
write_examen("examen_28.js", ex28)
write_examen("examen_29.js", ex29)
write_examen("examen_30.js", ex30)
print("Hoofdstuk 6 exams (26 to 30) generated successfully!")
