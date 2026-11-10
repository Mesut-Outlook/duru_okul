#!/usr/bin/env python3
"""Engels HAVO 3 · H1 Part one — examen_41..46 (3x Grammar, 3x Woorden) STRIKT uit het boek
(inbox/2026-2027/engels/engels_h01_*; Part one p.A38-A57, Learning corner p.A76-A79). Zodra Duru een toets maakte: id-inhoud niet meer wijzigen."""
import json, os, random, re, subprocess, difflib, glob
from gen_engels_h1_boek import M, W, I, O, plaats, rangschik, langste_aandeel, schrijf, norm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', 'havo3', 'engels', 'js', 'data')

# ---------------- Grammar A — compounds ----------------
G_A = rangschik(
 [M("Which compound completes the sentence? <i>Is there ____ in the kitchen that I can carry for you?</i>", "anything", ["nowhere", "nobody", "somewhere"],
    "Any- + -thing (things) in een vraag: 'Is there anything I can do?' (Grammar 1, boek p.A54)."),
  M("Which compound completes the sentence? <i>____ was laughing when the teacher walked in, so the room was very loud.</i>", "Everybody", ["Nobody", "Something", "Somewhere"],
    "Every- + -body (people): iedereen lachte (Grammar 1, boek p.A54)."),
  M("Which compound completes the sentence? <i>We have looked ____ for her, but she is not in the house.</i>", "anywhere", ["everyone", "something", "nobody"],
    "-where = plaatsen: any- + -where = ergens, in een ontkenning/vraag (Grammar 1, boek p.A54)."),
  M("Which of these compounds says something about a <b>place</b>?", "nowhere", ["nobody", "everyone", "something"],
    "-where = plaats: no- + -where = nergens; -body/-one = mensen; -thing = dingen (boek p.A54)."),
  M("Which spelling is correct for the compound of <i>no</i> + <i>one</i>?", "no one", ["noone", "none one", "no ones"],
    "Note! The compound no- + -one is written as two words: no one (boek p.A54)."),
  M("Which compound completes the sentence? <i>I was at home all day, but ____ called me.</i>", "nobody", ["anywhere", "something", "everyone"],
    "No- + -body = niemand (any-/no- : mensen, boek p.A54)."),
  M("Which compound completes the sentence? <i>Mum put ____ nice in my lunchbox: a chocolate bar.</i>", "something", ["nowhere", "nobody", "anywhere"],
    "Some- + -thing = iets (boek p.A54)."),
  M("Which compound completes the dialogue? <i>'Did you go on holiday?' 'No, we didn't go ____.'</i>", "anywhere", ["somewhere", "nowhere", "everyone"],
    "In een ontkende zin gebruik je any-: 'we didn't go anywhere' (boek p.A54-A55)."),
  M("Which sentence uses a <b>gerund</b> correctly?", "Dancing in the rain is fun.",
    ["Dance in the rain is fun.", "Danced in the rain is fun.", "To dancing in the rain is fun."],
    "Een gerund (verb + -ing) is een werkwoord dat als zelfstandig naamwoord wordt gebruikt (Grammar 2, boek p.A56).")],
 [W("The compound <i>nowhere</i> says something about places.", True, "Waar. No- + -where = nergens; -where = plaatsen (boek p.A54)."),
  W("The compound <i>anywhere</i> is used for people.", False, "Niet waar. -body / -one verwijzen naar mensen; -where naar plaatsen (boek p.A54)."),
  W("<i>Everybody</i> and <i>everyone</i> both say something about people.", True, "Waar. -body / -one = mensen (boek p.A54)."),
  W("The compound <i>something</i> is a combination of <i>some</i> and <i>where</i>.", False, "Niet waar. Something = some + thing; some + where = somewhere (boek p.A54)."),
  W("The compound <i>nobody</i> is a combination of <i>no</i> and <i>body</i>.", True, "Waar. No- + -body = niemand (boek p.A54).")],
 [I("Mum asked: <i>Does ____ want a cup of tea?</i> (any + person)", "anyone|anybody", "Vraag + any- + -one/-body (boek p.A54)."),
  I("The shop was closed, so there was ____ we could buy. (no + thing)", "nothing", "No- + -thing = niets (boek p.A54)."),
  I("I love this town: there are parks ____. (every + place)", "everywhere", "Every- + -where = overal (boek p.A54)."),
  I("Look! ____ left a bag under the table. (some + person)", "someone|somebody", "Some- + -one/-body = iemand (boek p.A54)."),
  I("Dear class, ____ is ready for the test: pens, paper and rulers. (every + thing)", "everything", "Every- + -thing = alles (boek p.A54).")],
 O("Write one English sentence with the compound you make from <i>no</i> + <i>where</i> and tell what it refers to.",
   ["nowhere", "place/places"], 2, "I could find my keys nowhere. Nowhere refers to a place.",
   "Nowhere = no + where: het verwijst naar een plaats (boek p.A54).")
)

# ---------------- Grammar B — gerund / to + infinitive ----------------
G_B = rangschik(
 [M("Which form completes the sentence? <i>Amy and Joe miss ____ football together on Fridays.</i>", "playing", ["to play", "play", "played"],
    "To miss + gerund (verb + -ing): 'We miss playing...' (Grammar 2, boek p.A56)."),
  M("Choose the correct form: <i>Pete hopes ____ the final next week.</i>", "to win", ["winning", "win", "won"],
    "To hope + to + infinitive (boek p.A56)."),
  M("Look at the verbs in Grammar 2. Which verb is followed by an -ing form?", "to dislike", ["to hope", "to refuse", "to expect"],
    "To (dis)like, to love, to miss, to avoid + gerund; to hope, to ask, to refuse, to expect + to + infinitive (boek p.A56)."),
  M("Which form completes the sentence? <i>Our neighbours asked us ____ their cat while they are away.</i>", "to feed", ["feeding", "feed", "fed"],
    "To + infinitive na het lijdend voorwerp (us): 'asked us to feed' (boek p.A56)."),
  M("Which form completes the sentence? <i>It is not easy ____ a new language in a few weeks.</i>", "to learn", ["learn", "learned", "to learning"],
    "To + infinitive na een bijvoeglijk naamwoord dat een mening geeft (easy): boek p.A56."),
  M("Which sentence about school lunch is correct?", "We avoid eating sweets before dinner.",
    ["We avoid to eat sweets before dinner.", "We avoid eat sweets before dinner.", "We avoid ate sweets before dinner."],
    "To avoid + gerund (boek p.A56)."),
  M("Which form completes the sentence? <i>____ horror films at night can be scary.</i>", "Watching", ["To watching", "Watch", "Watched"],
    "Een gerund kan als onderwerp van de zin staan: 'Watching ... can be scary.' (boek p.A56)."),
  M("Which form completes the sentence? <i>Remind your brother ____ his keys.</i>", "to take", ["taking", "take", "took"],
    "To + infinitive na het lijdend voorwerp: 'remind your brother to take' (boek p.A56)."),
  M("What is a <b>gerund</b>?", "A verb + -ing that is used as a noun", ["A verb in the past tense that is used as an adjective", "A verb with to in front that is used only after adjectives", "An -ing form that is used only after the verb to be"],
    "A verb + -ing (gerund) is a verb that is used as a noun (boek p.A56).")],
 [W("The verb <i>to refuse</i> is followed by <b>to + infinitive</b>, as in <i>She refused to answer</i>.", True, "Waar. To hope, to ask, to refuse, to expect + to + infinitive (boek p.A56)."),
  W("The verb <i>to miss</i> is followed by <b>to + infinitive</b>, as in <i>I miss to see you</i>.", False, "Niet waar. To miss + gerund: 'I miss swimming.' (boek p.A56)."),
  W("To + infinitive can be used after the object of a sentence: <i>I asked him to help.</i>", True, "Waar. Zie 'I asked him to read a book' (boek p.A56)."),
  W("A gerund never ends in <i>-ing</i>.", False, "Niet waar. A gerund always ends in -ing (boek p.A56)."),
  W("After adjectives that express an opinion, such as <i>wonderful</i>, you often use to + infinitive.", True, "Waar. 'It is wonderful to have a lot of friends.' (boek p.A56).")],
 [I("Leo loves ____ dinner for his family. (cook)", "cooking", "To love + gerund (boek p.A56)."),
  I("We expect ____ at six o'clock. (arrive)", "to arrive", "To expect + to + infinitive (boek p.A56)."),
  I("She refused ____ her notes with me. (give)", "to give", "To refuse + to + infinitive (boek p.A56)."),
  I("I dislike ____ up early on Sundays. (get)", "getting", "To dislike + gerund (boek p.A56)."),
  I("Mum asked me ____ the dishes. (wash)", "to wash", "To + infinitive na het lijdend voorwerp (me): boek p.A56.")],
 O("Which verb form follows <i>to love</i> and <i>to miss</i>? Answer in one English sentence.",
   ["gerund/-ing/ing"], 1, "After to love and to miss you use a gerund (verb + -ing).",
   "To avoid wordt gevolgd door een gerund (verb + -ing), zoals in 'We avoid travelling during rush hour' (boek p.A56).")
)

# ---------------- Grammar C — gemengd ----------------
G_C = rangschik(
 [M("Which compound completes the sentence? <i>My grandparents have ____ in their garden: roses, tulips and apple trees.</i>", "everything", ["nowhere", "nobody", "somebody"],
    "Every- + -thing = alles (boek p.A54)."),
  M("Which form completes the sentence? <i>We love ____ the old castle on Saturdays.</i>", "visiting", ["to visit", "visit", "visited"],
    "To love + gerund (boek p.A56)."),
  M("Which compound completes the sentence? <i>The room was dark and I could see ____.</i>", "nothing", ["anything", "everything", "somewhere"],
    "No- + -thing = niets (boek p.A54)."),
  M("Which compound completes the dialogue? <i>'Can you hear that?' 'No, I can't hear ____.'</i>", "anything", ["nothing", "everything", "somewhere"],
    "Ontkenning + any- + -thing (boek p.A54)."),
  M("Which sentence about a visitor is correct?", "Someone is waiting outside.", ["Someones is waiting outside.", "Some one are waiting outside.", "Somewhere is waiting outside."],
    "Some- + -one = iemand, één woord, enkelvoud (boek p.A54)."),
  M("Which sentence about Tom and his next holiday is correct?", "Tom hopes to meet you again soon.", ["Tom hopes meeting you again soon.", "Tom hopes meet you again soon.", "Tom hopes met you again soon."],
    "To hope + to + infinitive (boek p.A56)."),
  M("Which form completes the sentence? <i>We invited our teacher ____ to the concert.</i>", "to come", ["coming", "come", "came"],
    "To + infinitive na het lijdend voorwerp (our teacher): boek p.A56."),
  M("Which of these four sentences contains a mistake?", "He refuses paying for the ticket.",
    ["I miss living near the beach.", "We expect to win the match.", "Reading before bed is relaxing."],
    "To refuse + to + infinitive: 'He refuses to pay'. De andere zinnen kloppen (boek p.A56)."),
  M("Which compound completes the sentence? <i>____ was at the party: the whole class came.</i>", "Everyone", ["Nobody", "Somewhere", "Anything"],
    "Every- + -one = iedereen (boek p.A54).")],
 [W("<i>Nobody</i> and <i>no one</i> mean the same.", True, "Waar. No- + -body / -one: beide verwijzen naar mensen (boek p.A54)."),
  W("You can use the compound <i>somewhere</i> to talk about a person.", False, "Niet waar. -where = plaatsen; voor mensen gebruik je -body/-one (boek p.A54)."),
  W("In <i>I miss swimming</i>, the word <i>swimming</i> is a gerund.", True, "Waar. To miss + gerund (boek p.A56)."),
  W("The sentence <i>He avoids to speak in public</i> is correct.", False, "Niet waar. To avoid + gerund: 'He avoids speaking in public.' (boek p.A56)."),
  W("The compound <i>nothing</i> is used when there is not one single thing.", True, "Waar. No- + -thing = niets (boek p.A54).")],
 [I("Hello? Is ____ there? I can't see a light on. (any + person)", "anyone|anybody", "Vraag + any- + -one/-body (boek p.A54)."),
  I("My brother dislikes ____ his room. (clean)", "cleaning", "To dislike + gerund (boek p.A56)."),
  I("We hope ____ you at the party. (see)", "to see", "To hope + to + infinitive (boek p.A56)."),
  I("I looked ____ for my phone, but it was lost. (every + place)", "everywhere", "Every- + -where = overal (boek p.A54)."),
  I("I need to tell you ____ important. (some + thing)", "something", "Some- + -thing = iets (boek p.A54).")],
 O("Write one English sentence about a chore that people hate: use the compound for <i>niemand</i> and a verb + gerund.",
   ["nobody/no one", "ing"], 2, "Nobody likes cleaning the bathroom.",
   "No- + -body = niemand; to like + gerund (boek p.A54 en p.A56).")
)

# ---------------- Woorden A — Describing people ----------------
W_A = rangschik(
 [M("<i>My uncle never listens to other opinions and always blames people: he is very <b>judgmental</b>.</i> What does <b>judgmental</b> mean?", "veroordelend", ["ruimdenkend", "beleefd", "hard"],
    "Judgmental = veroordelend; open-minded = ruimdenkend (Theme words, Describing people, boek p.A76)."),
  M("Which English word means <i>ruimdenkend</i>?", "open-minded", ["intolerant", "harsh", "earnest"], "Open-minded = ruimdenkend (boek p.A76)."),
  M("<i>You can trust Mia: she is always <b>sincere</b> and says what she really thinks.</i> What does <b>sincere</b> mean?", "oprecht", ["verstandig", "gevoelig", "aanhoudend"], "Sincere = oprecht (boek p.A76)."),
  M("<i>Ben is very <b>sensitive</b>: he cries when he sees a sad film.</i> What does <b>sensitive</b> mean?", "gevoelig", ["verstandig", "hard", "oppervlakkig"],
    "Sensitive = gevoelig; sensible = verstandig (boek p.A76)."),
  M("Which English word means <i>verstandig</i>?", "sensible", ["sensitive", "persistent", "tolerant"], "Sensible = verstandig (boek p.A76)."),
  M("<i>Her <b>harsh</b> words really hurt me.</i> What does <b>harsh</b> mean?", "hard", ["attent", "aanhoudend", "serieus"], "Harsh = hard (boek p.A76)."),
  M("What is the opposite of <i>respectful</i>?", "disrespectful", ["polite", "sincere", "tolerant"], "(Dis)respectful = (on)eerbiedig (boek p.A76)."),
  M("<i>The <b>earnest</b> student listened closely and took notes of everything.</i> What does <b>earnest</b> mean?", "serieus", ["beleefd", "aanhoudend", "kinderachtig"], "Earnest = serieus (boek p.A76)."),
  M("<i>The salesman was so <b>persistent</b> that he called us five times.</i> What does <b>persistent</b> mean?", "aanhoudend", ["beleefd", "bedachtzaam", "oprecht"], "Persistent = aanhoudend (boek p.A76).")],
 [W("The English Theme word <i>earnest</i> means <i>serieus</i> in Dutch.", True, "Waar. Earnest = serieus (boek p.A76)."),
  W("Someone who is <i>persistent</i> gives up very quickly (<i>persistent</i> = <i>snel opgevend</i>).", False, "Niet waar. Persistent = aanhoudend: je geeft niet snel op (boek p.A76)."),
  W("<i>Tolerant</i> and <i>intolerant</i> are opposites: (in)tolerant.", True, "Waar. (In)tolerant = (in)tolerant (boek p.A76)."),
  W("The English Theme word <i>judgmental</i> means <i>ruimdenkend</i>.", False, "Niet waar. Judgmental = veroordelend; ruimdenkend = open-minded (boek p.A76)."),
  W("The English Theme word <i>polite</i> means <i>beleefd</i>.", True, "Waar. Polite = beleefd (boek p.A76).")],
 [I("Don't be so ____! You are fourteen, not four. (kinderachtig)", "childish", "Childish = kinderachtig (boek p.A76)."),
  I("Our teacher is very ____: she always asks if you need any help. (attent)", "thoughtful", "Thoughtful = attent, bedachtzaam (boek p.A76)."),
  I("Aisha is no longer ____ in football; she wants to try tennis. (geïnteresseerd)", "interested", "(Un)interested = (on)geïnteresseerd (boek p.A76)."),
  I("He is ____ and won't change his mind, even when everyone shows him he is wrong. (koppig)", "stubborn", "Stubborn = koppig (boek p.A76)."),
  I("Her friendships are ____: she only cares about looks and never talks about real feelings. (oppervlakkig)", "superficial", "Superficial = oppervlakkig (boek p.A76).")],
 O("Explain in one English sentence the difference between <i>sensible</i> and <i>sensitive</i>.",
   ["wise/reasonable/practical/good sense/clever/verstandig", "feelings/emotional/easily hurt/gevoelig/cry"], 2,
   "Sensible means that you have good sense and make wise choices; sensitive means that you have strong feelings and are easily hurt.",
   "Sensible = verstandig; sensitive = gevoelig (boek p.A76).")
)

# ---------------- Woorden B — Social interactions ----------------
W_B = rangschik(
 [M("Which English Theme phrase means <i>contact verliezen met</i>?", "to lose touch with", ["to blend in", "to share with", "to have in common"], "To lose touch with = contact verliezen met (Social interactions, boek p.A76)."),
  M("<i>Danny and I have a lot in <b>common</b>: we both love chess.</i> What does <b>to have in common</b> mean?", "gemeen hebben", ["het uitmaken", "tijd doorbrengen met", "contact verliezen met"],
    "To have in common = gemeen hebben (boek p.A76)."),
  M("A travelling <i>kameraad</i> is called a ____. Which Theme word fits?", "companion", ["acquaintance", "outcast", "peer"], "Companion = kameraad (boek p.A76)."),
  M("A dog is famous for being <i>trouw</i> to its owner: it is ____. Which Theme word fits?", "loyal", ["formal", "informal", "outcast"], "Loyal = trouw (boek p.A76)."),
  M("<i>Ella had no friends in class and felt like an <b>outcast</b>.</i> What does <b>outcast</b> mean?", "buitenbeentje", ["leeftijdsgenoot", "collega", "kennis"], "Outcast = buitenbeentje (boek p.A76)."),
  M("New students want <i>erbij horen</i>: they want ____ with the group. Which Theme phrase fits?", "to blend in", ["to help each other out", "to share with", "to lose touch with"], "To blend in = erbij horen (boek p.A76)."),
  M("<i>All my <b>peers</b> have a smartphone, so I want one too.</i> What does <b>peers</b> mean?", "leeftijdsgenoten", ["kennissen", "kameraden", "collega's"], "Peer = leeftijdsgenoot (boek p.A76)."),
  M("A party in jeans and T-shirts is a(n) ____ (<i>informeel</i>) party. Which Theme word fits?", "informal", ["formal", "loyal", "peer"], "(In)formal = (in)formeel (boek p.A76)."),
  M("Neighbours who always <i>elkaar helpen</i> ____. Which Theme phrase fits?", "help each other out", ["lose touch with each other", "share with each other", "blend in with each other"], "To help each other out = elkaar helpen (boek p.A76).")],
 [W("A <i>peer</i> is a person of your own age (<i>leeftijdsgenoot</i>).", True, "Waar. Peer = leeftijdsgenoot (boek p.A76)."),
  W("An <i>acquaintance</i> is a very close friend.", False, "Niet waar. Acquaintance = kennis, geen goede vriend (boek p.A76)."),
  W("The Theme phrase <i>to share with</i> means <i>delen met</i>.", True, "Waar. To share with = delen met (boek p.A76)."),
  W("An <i>outcast</i> is a very popular person in the group.", False, "Niet waar. Outcast = buitenbeentje: iemand die er niet bij hoort (boek p.A76)."),
  W("A <i>loyal</i> friend stays with you: <i>loyal</i> means <i>trouw</i>.", True, "Waar. Loyal = trouw (boek p.A76).")],
 [I("We want to ____ more time with our grandparents. (doorbrengen)", "spend", "To spend time with = tijd doorbrengen met (boek p.A76)."),
  I("Julia and I know the same boy, Max: he is our ____ friend. (gemeenschappelijke)", "mutual", "Mutual friend = gemeenschappelijke vriend (boek p.A76)."),
  I("Sara and Jim argued a lot, so they decided to ____ up. (het uitmaken)", "break", "To break up = het uitmaken (boek p.A76)."),
  I("Mr Evans is my ____: we work in the same office. (collega)", "colleague", "Colleague = collega (boek p.A76)."),
  I("We moved to another city, so I have ____ touch with my old friends. (verloren)", "lost", "To lose touch with = contact verliezen met (boek p.A76).")],
 O("What is an <i>acquaintance</i>? Answer in one English sentence.",
   ["know/met/not close", "someone/person/somebody"], 1, "An acquaintance is someone you know a little, but who is not a close friend.",
   "Acquaintance = kennis: iemand die je kent, maar geen goede vriend (boek p.A76).")
)

# ---------------- Woorden C — Keeping a conversation going + Watching/Reading ----------------
W_C = rangschik(
 [M("Which Theme phrase means <i>trouwens</i>?", "by the way", ["as I was saying", "speaking of", "in fact"], "By the way = trouwens (Keeping a conversation going, boek p.A76)."),
  M("Which Theme phrase means <i>als je het mij vraagt</i>?", "if you ask me", ["You know what?", "to be honest", "that reminds me"], "If you ask me = als je het mij vraagt (boek p.A76)."),
  M("Which Theme phrase means <i>dat herinnert me eraan</i>?", "that reminds me", ["in fact", "I was wondering", "speaking of"], "That reminds me = dat herinnert me eraan (boek p.A76)."),
  M("Which Theme word fits <i>blijkbaar</i>: <i>____, the bus was late again today.</i>", "apparently", ["in fact", "speaking of", "I was wondering"], "Apparently = blijkbaar (boek p.A76)."),
  M("<i>Climbing that mountain was a real <b>challenge</b>.</i> What does <b>challenge</b> mean?", "uitdaging", ["gevaar", "imago", "standpunt"], "Challenge = uitdaging (Vocabulary A Watching, boek p.A76)."),
  M("<i>Don't swim here: there is <b>danger</b> of strong currents.</i> What does <b>danger</b> mean?", "gevaar", ["uitdaging", "schatting", "noodzaak"], "Danger = gevaar (boek p.A76)."),
  M("<i>We want to <b>explore</b> the old town on foot.</i> What does <b>to explore</b> mean?", "ontdekken", ["beïnvloeden", "beweren", "buitensluiten"], "To explore = ontdekken (boek p.A76)."),
  M("<i>Her kind words boosted my <b>self-confidence</b>.</i> What does <b>self-confidence</b> mean?", "zelfvertrouwen", ["noodzaak", "imago", "standpunt"], "Self-confidence = zelfvertrouwen (Vocabulary C Reading, boek p.A77)."),
  M("<i>From my <b>point of view</b>, school should start later.</i> What does <b>point of view</b> mean?", "standpunt", ["uitdaging", "aanwijzing", "schatting"], "Point of view = standpunt (boek p.A77).")],
 [W("In <i>Apparently, the match is cancelled</i>, the word <i>apparently</i> means <i>blijkbaar</i>.", True, "Waar. Apparently = blijkbaar (boek p.A76)."),
  W("The Theme phrase <i>to be honest</i> means <i>zoals ik zei</i>.", False, "Niet waar. To be honest = om eerlijk te zijn; zoals ik zei = as I was saying (boek p.A76)."),
  W("The Theme phrase <i>No way!</i> means <i>Echt niet!</i>", True, "Waar. No way! = Echt niet! (boek p.A76)."),
  W("The English word <i>trivial</i> means <i>belangrijk</i> in Dutch.", False, "Niet waar. Trivial = onbelangrijk (Vocabulary C Reading, boek p.A77)."),
  W("The English phrase <i>to stand out</i> means <i>opvallen, eruitspringen</i>.", True, "Waar. To stand out = opvallen (boek p.A77).")],
 [I("____ what? I got the leading part in the school play! (Raad eens?)", "guess", "Guess what? = Raad eens? (boek p.A76)."),
  I("The film was boring, but ____, we had a nice evening. (hoe dan ook)", "anyway", "Anyway = hoe dan ook (boek p.A76)."),
  I("Good friends need ____: you must be able to believe what the other says. (vertrouwen)", "trust", "Trust = vertrouwen (boek p.A76)."),
  I("Water is a basic ____ for all living things. (noodzaak)", "necessity", "Necessity = noodzaak (boek p.A77)."),
  I("Her laughter is so ____ that everyone laughs along. (aanstekelijk)", "contagious", "Contagious = aanstekelijk (boek p.A77).")],
 O("Write one short English sentence in which you change the subject with a Theme phrase from <i>Keeping a conversation going</i> (not the one for <i>hoe dan ook</i>).",
   ["by the way/speaking of/that reminds me/you know what"], 1, "By the way, did you see the new film?",
   "By the way = trouwens; speaking of = over ... gesproken (boek p.A76).")
)

EXAMENS = {
 41: ("Part one · Grammar A — compounds & gerunds (boek)", "🧩", G_A),
 42: ("Part one · Grammar B — gerund of to + infinitive (boek)", "✏️", G_B),
 43: ("Part one · Grammar C — gemengd: compounds, gerund & to + infinitive (boek)", "🔁", G_C),
 44: ("Part one · Woorden A — Describing people (boek)", "🧑", W_A),
 45: ("Part one · Woorden B — Social interactions (boek)", "🤝", W_B),
 46: ("Part one · Woorden C — conversation, Watching & Reading (boek)", "💬", W_C),
}


def bestaande():
    js = ("const out=[];const add=o=>{if(o&&typeof o==='object'){if(typeof o.vraag==='string')out.push(o.vraag);Object.values(o).forEach(add)}};"
          "global.DURU=new Proxy({},{get:()=>(...a)=>a.forEach(add)});"
          "const fs=require('fs'),d=process.argv[1];"
          "for(const f of fs.readdirSync(d))if(/^(examen_\\d+|h\\d_\\d)\\.js$/.test(f)&&!/^examen_(4[1-6])\\.js$/.test(f)){try{new Function('DURU',fs.readFileSync(d+'/'+f,'utf8'))(global.DURU)}catch(e){}}"
          "console.log(JSON.stringify(out))")
    return [norm(x) for x in json.loads(subprocess.check_output(['node', '-e', js, os.path.abspath(ROOT)]))]


FOUT = []


def controleer(vr, oud, nr):
    for v in vr:
        q = norm(v["vraag"])
        r = max((difflib.SequenceMatcher(None, q, o).ratio() for o in oud), default=0)
        if r >= 0.8: FOUT.append(f"examen_{nr}: lijkt op bestaande vraag ({r:.2f}): {v['vraag']}")
        if v["type"] == "invul":
            for a in v["antwoord"].split('|'):
                if norm(a) in q.replace(norm('____'), ''): FOUT.append(f"antwoord in vraag: {v['vraag']}")


def main():
    rng = random.Random(os.path.basename(__file__))
    oud = bestaande()
    print(len(oud), "bestaande vragen")
    gezien = []
    for nr, (titel, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        controleer(vr, oud + gezien, nr)
        gezien += [norm(v["vraag"]) for v in vr]
        ex = {"id": f"ex-h3-eng-{nr}", "hoofdstuk": 1, "hoofdstukTitel": "Hoofdstuk 1 — The world around you",
              "titel": titel, "vak": "Engels · HAVO 3 (H1)", "icoon": icoon, "duurMin": 25, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* {titel}\n   Stepping Stones 3 HAVO Hoofdstuk 1 Part one — gegenereerd door tools/gen_engels_h1_part1.py, uit het boek */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
    for f in FOUT: print('FOUT', f)
    raise SystemExit(1 if FOUT else 0)
