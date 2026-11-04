#!/usr/bin/env python3
"""Nederlands HAVO 3 · lesnotities van de docent (map inbox/2026-2027/nederlands/Nederlands Notlar/).

Bron: werkwoord spelling.pptx, WERKWOORDSPELLING 3H..docx (spellingdetective + chat), Grammatica – bijvoeglijk
naamwoorden.pptx, met of zonder -N.pptx, opdr met of zonder -n.docx, accenten vwo.pptx, samentrekkingen 3vwo.pptx,
verwijzen vwo.pptx. Boekparagrafen (Cursus 7, inhoudsopgave p. 243): §9 Herhaling (werkwoorden), §10 Engelse
werkwoorden, §11 Homofone werkwoordsvormen.

Schrijft havo3/nederlands/js/data/:
  onderwerpen  c7_9.js · c7_10.js · c7_11.js · c7_3_bijvoeglijk.js · c7_werkwoorden_begrippen.js
  toetsen      examen_53…62.js (ex-h3-nederlands-53…62)

Spellingsvragen met `invul` krijgen "exact": true → exams.js keurt alleen een exacte (genormaliseerde) match goed.
Zonder exact telt een substring als goed ('vind' zit in 'vindt', 'gedownload' in 'gedownloadt').

Draai: python3 tools/gen_nederlands_lesnotities.py   (daarna node tools/gate.js nederlands)
"""
import json, os, random, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "havo3", "nederlands", "js", "data")
rng = random.Random("lesnotities_2026_11")


# ---- helpers ---------------------------------------------------------------------------------------
def mc(vraag, goed, fout, uitleg):
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": list(fout), "uitleg": uitleg}


def I(vraag, antwoord, uitleg):
    """Spellings-invul: exact."""
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "exact": True, "uitleg": uitleg}


def W(stelling, waar, uitleg):
    return {"type": "waaronwaar", "vraag": stelling, "antwoord": waar,
            "uitleg": ("Waar. " if waar else "Niet waar. ") + uitleg}


def O(vraag, sleutels, model, uitleg, minT=1):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": minT,
            "modelantwoord": model, "uitleg": uitleg}


# oefenvragen (onderwerpen): niveau + hint
def omc(niveau, vraag, goed, fout, uitleg, hint):
    d = mc(vraag, goed, fout, uitleg); d["niveau"] = niveau; d["hint"] = hint; return d


def oin(niveau, vraag, antwoord, uitleg, hint):
    return {"type": "invoer", "niveau": niveau, "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg, "hint": hint}


def ow(niveau, stelling, waar, uitleg, hint):
    d = W(stelling, waar, uitleg); d["niveau"] = niveau; d["hint"] = hint; return d


KOF = "'t kofschip X (t, k, f, s, ch, p, x)"

# =====================================================================================================
# THEORIE
# =====================================================================================================
TH_C7_9 = """
<h3>1. Eerst: de stam</h3>
<p>Bijna elke regel in de werkwoordspelling begint bij de <b>stam</b>. De stam = <b>hele werkwoord min -en</b>, daarna pas je de spelling aan.</p>
<ul>
  <li><i>werken</i> → <b>werk</b> · <i>lopen</i> → <b>loop</b> (een lange klank blijft lang) · <i>zetten</i> → <b>zet</b> (dubbele medeklinker wordt enkel)</li>
  <li><i>leven</i> → <b>leef</b> · <i>verhuizen</i> → <b>verhuis</b> (aan het eind van een woord wordt v een f en z een s)</li>
  <li><i>vinden</i> → <b>vind</b> · <i>worden</i> → <b>word</b> (de d hoor je niet, maar je schrijft hem wel)</li>
</ul>
<div class="info-box tip"><h4>Snel de stam vinden</h4><p>De stam is de vorm die je bij <b>ik</b> gebruikt: <i>ik werk, ik loop, ik vind, ik word</i>.</p></div>

<h3>2. Tegenwoordige tijd</h3>
<table class="nask">
<tr><th>Persoon</th><th>Regel</th><th>tekenen</th><th>vinden</th></tr>
<tr><td>ik</td><td>stam</td><td>ik teken</td><td>ik vind</td></tr>
<tr><td>jij / je</td><td>stam + t</td><td>jij tekent</td><td>jij vindt</td></tr>
<tr><td>jij / je <b>achter</b> de persoonsvorm</td><td>stam (geen t)</td><td>Teken jij?</td><td>Vind jij?</td></tr>
<tr><td>hij / zij / het / u</td><td>stam + t</td><td>hij tekent</td><td>zij vindt</td></tr>
<tr><td>wij / jullie / zij</td><td>hele werkwoord</td><td>wij tekenen</td><td>zij vinden</td></tr>
</table>
<div class="formule-box"><b>Gouden regel</b><br>Eindigt de stam op een <b>d</b> en moet er een t bij, dan schrijf je <b>dt</b>: <i>hij vindt, Tim snijdt, jij antwoordt</i>.<br>Eindigt de stam al op een <b>t</b>, dan komt er geen tweede t bij: <i>hij zet, hij wacht</i>.</div>
<div class="info-box let-op"><h4>Let op: jij en u</h4><p>Staat <b>jij/je</b> achter de persoonsvorm, dan valt de t weg: <i>Word jij later dokter?</i> Bij <b>u</b> blijft de t altijd: <i>Wordt u al geholpen?</i> En pas op met <i>je broer</i>: dat is hij, dus <i>Gaat je broer mee?</i></p></div>
<div class="info-box tip"><h4>De lopen-test</h4><p>Twijfel je? Vervang het werkwoord door <i>lopen</i>. <i>Hij loopt</i> → je hoort een t → <i>hij vindt</i>. <i>Loop jij?</i> → geen t → <i>Vind jij?</i></p></div>

<h3>3. Verleden tijd</h3>
<p><b>Zwakke (regelmatige) werkwoorden:</b> kijk naar de laatste letter van de stam. Zit die letter in <b>""" + KOF + """</b>?</p>
<ul>
  <li>Ja → stam + <b>te / ten</b>: <i>werken → werkte, fietsen → fietste, zetten → zette, praten → praatte, verwoesten → verwoestte</i></li>
  <li>Nee → stam + <b>de / den</b>: <i>horen → hoorde, staren → staarden, branden → brandde, verheugen → verheugde</i></li>
</ul>
<div class="info-box let-op"><h4>Veelgemaakte fout: v en z</h4><p>Kijk naar het <b>hele werkwoord</b>. <i>leven</i>: de v zit niet in 't kofschip → <b>leefde</b>. <i>verhuizen</i>: de z zit niet in 't kofschip → <b>verhuisde</b>. Ook al zie je in de stam een f of s, het wordt toch -de.</p></div>
<p><b>Sterke (onregelmatige) werkwoorden:</b> de klinker verandert en er komt geen -te/-de achter: <i>lopen → liep, liepen · vinden → vond, vonden · worden → werd, werden</i>.</p>

<h3>4. Voltooid deelwoord</h3>
<div class="formule-box"><b>Regel</b><br><b>ge + stam + t</b> als de laatste letter van de stam in 't kofschip zit, anders <b>ge + stam + d</b>. Sterke werkwoorden: <b>ge + … + en</b>.<br><i>werken → gewerkt · horen → gehoord · leven → geleefd · vinden → gevonden</i></div>
<ul>
  <li>Werkwoorden die beginnen met <b>be-, ge-, her-, ont-, ver-, er-</b> krijgen geen extra ge-: <i>veranderd, ontruimd, herhaald</i>.</li>
  <li>Bij een scheidbaar werkwoord staat ge- in het midden: <i>opruimen → opgeruimd, binnenkomen → binnengekomen</i>.</li>
  <li>Eindigt de stam al op d of t, dan komt er niets bij: <i>voorbereiden → voorbereid, zetten → gezet</i>.</li>
</ul>
<div class="voorbeeld"><div class="vb-kop">Voorbeeld: d of t? Verleng het woord</div>
<div class="stap">Gebruik het voltooid deelwoord als bijvoeglijk naamwoord: <i>gebeurd → het gebeurde ongeluk</i> → je hoort een d.</div>
<div class="stap"><i>gewerkt → het gewerkte uur</i> → je hoort een t.</div></div>
"""

TH_C7_10 = """
<h3>Engelse werkwoorden in het Nederlands</h3>
<p>Werkwoorden als <i>updaten, downloaden, liken, appen, checken</i> en <i>streamen</i> komen uit het Engels. Je vervoegt ze met de <b>Nederlandse regels</b>, maar er zijn twee dingen om op te letten.</p>
<div class="formule-box"><b>Drie stappen</b><br>
1. Stam = hele werkwoord min -en, en je <b>houdt de Engelse spelling</b>: <i>updaten → update, liken → like, crashen → crash, back-uppen → back-up</i>.<br>
2. Voor 't kofschip X kijk je naar de <b>laatste klank die je hoort</b>, niet naar de laatste letter: <i>update</i> eindigt op een t-klank, <i>like</i> op een k-klank.<br>
3. Daarna pas je gewoon de Nederlandse regels toe.</div>
<table class="nask">
<tr><th>Werkwoord</th><th>Stam</th><th>Klank</th><th>hij (tt)</th><th>Verleden tijd</th><th>Voltooid deelwoord</th></tr>
<tr><td>updaten</td><td>update</td><td>t</td><td>updatet</td><td>updatete</td><td>geüpdatet</td></tr>
<tr><td>liken</td><td>like</td><td>k</td><td>liket</td><td>likete</td><td>geliket</td></tr>
<tr><td>skaten</td><td>skate</td><td>t</td><td>skatet</td><td>skatete</td><td>geskatet</td></tr>
<tr><td>checken</td><td>check</td><td>k</td><td>checkt</td><td>checkte</td><td>gecheckt</td></tr>
<tr><td>crashen</td><td>crash</td><td>sj</td><td>crasht</td><td>crashte</td><td>gecrasht</td></tr>
<tr><td>appen</td><td>app</td><td>p</td><td>appt</td><td>appte</td><td>geappt</td></tr>
<tr><td>back-uppen</td><td>back-up</td><td>p</td><td>back-upt</td><td>back-upte</td><td>geback-upt</td></tr>
<tr><td>downloaden</td><td>download</td><td>d</td><td>downloadt</td><td>downloadde</td><td>gedownload</td></tr>
<tr><td>uploaden</td><td>upload</td><td>d</td><td>uploadt</td><td>uploadde</td><td>geüpload</td></tr>
<tr><td>streamen</td><td>stream</td><td>m</td><td>streamt</td><td>streamde</td><td>gestreamd</td></tr>
</table>
<div class="info-box let-op"><h4>Let op</h4><p><i>geüpload, geüpdatet</i>: <b>ge + u</b> spreek je los van elkaar uit, daarom een trema. <i>gedownload</i>: de stam eindigt al op een d, dus er komt niets meer achter (niet <i>gedownloadt</i>). En schrijf geen Engelse uitgang: <i>geliket</i>, niet <i>geliked</i>.</p></div>
<div class="info-box tip"><h4>Hardop zeggen helpt</h4><p>Zeg de stam hardop: <i>"skeet"</i> eindigt op een t-klank → <i>skatete</i>. <i>"striem"</i> eindigt op een m-klank → <i>streamde</i>.</p></div>
"""

TH_C7_11 = """
<h3>Homofone werkwoordsvormen</h3>
<p><b>Homofoon</b> betekent: het klinkt hetzelfde, maar je schrijft het anders. Bij werkwoorden gaat het vaak mis tussen een <b>persoonsvorm</b> (op -t) en een <b>voltooid deelwoord</b> (op -d), of tussen de verleden tijd en het voltooid deelwoord.</p>
<table class="nask">
<tr><th>Persoonsvorm (tegenwoordige tijd)</th><th>Voltooid deelwoord</th><th>Verleden tijd</th></tr>
<tr><td>Wat gebeur<b>t</b> er?</td><td>Wat is er gebeur<b>d</b>?</td><td>Wat gebeur<b>de</b> er?</td></tr>
<tr><td>Het weer verander<b>t</b>.</td><td>Ik heb het verander<b>d</b>.</td><td>Het weer verander<b>de</b>.</td></tr>
<tr><td>Hij verhuis<b>t</b> morgen.</td><td>Hij is verhuis<b>d</b>.</td><td>Hij verhuis<b>de</b> vorig jaar.</td></tr>
<tr><td>Zij beantwoord<b>t</b> de mail.</td><td>De mail is beantwoord.</td><td>Zij beantwoord<b>de</b> de mail.</td></tr>
</table>
<div class="formule-box"><b>Stappenplan</b><br>
1. Zoek de <b>persoonsvorm</b> (verander de tijd: welk werkwoord verandert mee?).<br>
2. Is het woord de persoonsvorm in de tegenwoordige tijd? → stam (+ t). Doe de lopen-test: <i>het loopt</i> → <i>het gebeurt</i>.<br>
3. Is het woord <b>geen</b> persoonsvorm en staat er een vorm van <i>hebben, zijn</i> of <i>worden</i> bij? → voltooid deelwoord. Verleng het: <i>het gebeurde ongeluk</i> → d.</div>
<div class="info-box let-op"><h4>Let op: word / wordt</h4><p><i>Ik word, word jij?</i> → stam. <i>Hij wordt, jij wordt, wordt u?</i> → stam + t. Het voltooid deelwoord van worden is <i>geworden</i>.</p></div>
<div class="info-box tip"><h4>Lezen als een spellingdetective</h4><p>Lees je tekst na en zet bij elk werkwoord op -d, -t of -dt een stip. Vraag bij elk werkwoord: persoonsvorm of voltooid deelwoord? Wie is het onderwerp? Zo vind je fouten als <i>dat gebeurdt</i>, <i>ik heb het verandert</i> of <i>mijn broer vind</i>.</p></div>
"""

TH_C7_3B = """
<h3>Bijvoeglijk naamwoord: met of zonder -e?</h3>
<p>Een <b>bijvoeglijk naamwoord</b> zegt iets over een zelfstandig naamwoord: een eigenschap, kenmerk of toestand (<i>de grappige film, een zacht boek</i>). Of het een -e krijgt, hangt af van het lidwoord.</p>
<table class="nask">
<tr><th></th><th>Wel -e</th><th>Geen -e</th></tr>
<tr><td><b>de-woord</b></td><td>altijd: <i>de leuke vriend, een leuke vriend, geen leuke vriend, elke leuke vriend</i></td><td>—</td></tr>
<tr><td><b>het-woord</b></td><td>na het / dit / dat / mijn / ons …: <i>het nieuwe spel, mijn nieuwe spel</i></td><td>na een / geen / elk / ieder / veel of zonder lidwoord: <i>een nieuw spel, elk nieuw spel, mooi weer</i></td></tr>
<tr><td><b>meervoud</b></td><td>altijd: <i>nieuwe spellen, de dure horloges</i></td><td>—</td></tr>
</table>
<div class="info-box tip"><h4>Snelle check</h4><p>Is het een <b>het-woord</b> en staat er <b>een, geen, elk</b> of <b>ieder</b> voor? Dan geen -e: <i>een duur horloge, een interessant artikel, een prachtig cadeau</i>. In alle andere gevallen wel een -e.</p></div>
<div class="info-box let-op"><h4>Al op -en?</h4><p>Bijvoeglijke naamwoorden die al op -en eindigen, krijgen geen extra -e: <i>de ervaren medewerkers, een open deur, gebakken eieren</i>.</p></div>
<h3>Stoffelijke bijvoeglijke naamwoorden</h3>
<div class="formule-box"><b>Regel</b><br>Bijvoeglijke naamwoorden die zeggen <b>van welk materiaal</b> iets gemaakt is, eindigen <b>altijd op -en</b>: <i>een houten lepel, een gouden ring, een zilveren ketting, een stalen buis, glazen flessen, een leren tas, kartonnen dozen, een wollen trui</i>.<br>Nooit: <i>houte, zilvere, glaze, kartonne</i>.</div>
<p>Wanneer een zelfstandig gebruikt bijvoeglijk naamwoord of telwoord een <b>n</b> krijgt (<i>de armen, enkelen</i>), leer je in §3 <i>Met of zonder n?</i>.</p>
"""

TH_BEGR = """
<h3>Begrippen werkwoordspelling (§9, §10, §11)</h3>
<p>Deze begrippen heb je nodig om werkwoorden goed te spellen én om uit te leggen <i>waarom</i> je iets zo schrijft.</p>
<div class="formule-box">
<ul>
  <li><b>Hele werkwoord</b> (infinitief): de vorm die in het woordenboek staat: <i>lopen, werken, vinden</i>.</li>
  <li><b>Stam</b>: hele werkwoord min -en, in de spelling van de ik-vorm: <i>loop, werk, vind, verhuis</i>.</li>
  <li><b>Persoonsvorm</b>: het werkwoord dat verandert als je de tijd of het getal van de zin verandert: <i>Hij <b>loopt</b> → Hij <b>liep</b> / Zij <b>lopen</b></i>.</li>
  <li><b>Tegenwoordige tijd</b> en <b>verleden tijd</b>: nu (<i>werkt</i>) en vroeger (<i>werkte</i>).</li>
  <li><b>Voltooid deelwoord</b>: de werkwoordsvorm bij <i>hebben, zijn</i> of <i>worden</i>: <i>heb gewerkt, is gevonden</i>.</li>
  <li><b>Zwak werkwoord</b>: regelmatig; krijgt -te/-de in de verleden tijd: <i>werken – werkte</i>.</li>
  <li><b>Sterk werkwoord</b>: onregelmatig; de klinker verandert: <i>lopen – liep – gelopen</i>.</li>
  <li><b>'t kofschip X</b>: ezelsbruggetje met de medeklinkers t, k, f, s, ch, p en x. Zit de laatste letter (of klank) van de stam erin, dan -te/-t, anders -de/-d.</li>
  <li><b>Scheidbaar werkwoord</b>: werkwoord dat in de zin uit elkaar gaat: <i>opruimen → ik ruim op → opgeruimd</i>.</li>
  <li><b>Homofone werkwoordsvormen</b>: vormen die hetzelfde klinken maar anders geschreven worden: <i>gebeurt / gebeurd</i>.</li>
  <li><b>Verlengen</b>: het voltooid deelwoord als bijvoeglijk naamwoord gebruiken om d of t te horen: <i>het gebeurde ongeluk</i>.</li>
  <li><b>Engels werkwoord</b> (leenwerkwoord): <i>updaten, liken</i>; Engelse spelling in de stam, kofschip op de klank.</li>
</ul>
</div>
<div class="info-box tip"><h4>Leer ze actief</h4><p>Kun je bij elk begrip een eigen voorbeeldzin maken? Dan ken je het. Gebruik de begrippen ook als je een fout uitlegt: <i>"vindt, want persoonsvorm bij hij: stam + t"</i>.</p></div>
"""

# =====================================================================================================
# ONDERWERPEN (oefenvragen)
# =====================================================================================================
OEF_C7_9 = [
    oin(1, "Vul de juiste vorm in: <i>Mijn broer ___ (vinden) het huiswerk saai.</i>", "vindt", "Hij → stam + t: vind + t = vindt.", "Stam van vinden = vind. Wie is het onderwerp?"),
    oin(1, "Vul de juiste vorm in: <i>___ (lopen) jij morgen mee naar de bakker?</i>", "Loop", "Jij staat achter de persoonsvorm, dus geen t: Loop jij?", "Staat jij voor of achter het werkwoord?"),
    oin(2, "Vul de juiste vorm in: <i>Oma ___ (houden) van lange wandelingen.</i>", "houdt", "Oma = zij → stam (houd) + t = houdt.", "Stam = houd."),
    oin(2, "Vul de verleden tijd in: <i>Wij ___ (leven) vroeger in Turkije.</i>", "leefden", "Leven → de v zit niet in 't kofschip → -de/-den. Meervoud → leefden.", "Kijk naar het hele werkwoord: leven."),
    oin(2, "Vul de verleden tijd in: <i>Gisteren ___ (fietsen) ik door de regen naar huis.</i>", "fietste", "Stam fiets → de s zit in 't kofschip → -te.", "Laatste letter van de stam?"),
    oin(2, "Vul het voltooid deelwoord in: <i>Ik heb de hele garage ___ (opruimen).</i>", "opgeruimd", "Scheidbaar werkwoord: op + ge + ruim + d (m zit niet in 't kofschip).", "Ge- komt in het midden."),
    oin(3, "Vul het voltooid deelwoord in: <i>De taart is prachtig ___ (versieren).</i>", "versierd", "Ver- → geen extra ge-. Verleng: de versierde taart → d.", "Begint het werkwoord met ver-?"),
    omc(1, "Kies de juiste vorm: <i>___ u nog iets anders?</i> (wensen)", "Wenst", ["Wens", "Wensen", "Wenste"], "Bij u blijft de t altijd staan, ook als u achter de persoonsvorm staat.", "Let op: u, niet jij."),
    omc(2, "Kies de juiste vorm: <i>Hij ___ (wachten) al twintig minuten.</i>", "wacht", ["wachtt", "wachten", "wachte"], "De stam wacht eindigt al op een t; er komt geen tweede t bij.", "Stam + t, maar de stam eindigt al op t."),
    omc(3, "Welke vorm is goed: <i>De buurvrouw ___ (verbranden) gisteren het snoeiafval.</i>", "verbrandde", ["verbrande", "verbrandte", "verbrand"], "Stam verbrand → d zit niet in 't kofschip → -de: verbrand + de = verbrandde.", "Stam + de: let op de dubbele d."),
    ow(1, "Bij <i>zij</i> (meervoud) gebruik je in de tegenwoordige tijd het hele werkwoord: <i>zij werken</i>.", True, "Meervoud = hele werkwoord.", "Meervoud: wij, jullie, zij."),
    ow(2, "De verleden tijd van <i>reizen</i> is <i>reiste</i>, want in de stam reis zie je een s.", False, "Reizen → z zit niet in 't kofschip, dus reisde.", "Kijk naar het hele werkwoord."),
    ow(2, "Het voltooid deelwoord van <i>leven</i> is <i>geleeft</i>.", False, "De v van leven zit niet in 't kofschip → geleefd.", "Verleng: het geleefde leven."),
]

OEF_C7_10 = [
    oin(1, "Vul de verleden tijd in: <i>Gisteren ___ (updaten) ik de app op mijn telefoon.</i>", "updatete", "Stam update eindigt op een t-klank → -te.", "Zeg de stam hardop."),
    oin(2, "Vul het voltooid deelwoord in: <i>Iedereen heeft mijn filmpje ___ (liken).</i>", "geliket", "Stam like eindigt op een k-klank → ge + like + t.", "Geen Engelse uitgang -ed!"),
    oin(2, "Vul het voltooid deelwoord in: <i>Heb je de nieuwe versie al ___ (downloaden)?</i>", "gedownload", "De stam download eindigt al op een d; er komt niets achter.", "ge + stam + d, maar de stam eindigt al op d."),
    oin(2, "Vul de tegenwoordige tijd in: <i>Mijn zus ___ (skaten) elke zaterdag.</i>", "skatet", "Zij → stam (skate) + t.", "Hele werkwoord min -en = stam."),
    omc(1, "Wat is de stam van <i>liken</i>?", "like", ["lik", "liek", "laik"], "Je houdt de Engelse spelling: liken min -en = like.", "Engelse spelling blijft."),
    omc(2, "Welke spelling is goed: <i>Ik heb mijn werkstuk naar de site ___ (uploaden).</i>", "geüpload", ["geupload", "geüploadt", "geuploaded"], "Ge + upload; e en u spreek je los uit → trema. Stam eindigt op d → niets erachter.", "Let op trema en uitgang."),
    omc(3, "Kies de juiste vorm: <i>Vorige week ___ (crashen) mijn laptop drie keer.</i>", "crashte", ["crashde", "crashed", "crasht"], "Stam crash eindigt op de sj-klank (zoals sch) → -te.", "Laatste klank: sj."),
    ow(1, "Bij Engelse werkwoorden kijk je voor 't kofschip naar de laatste klank die je hoort.", True, "Update eindigt op een e, maar je hoort een t → -te.", "Klank of letter?"),
    ow(2, "<i>Geliked</i> is de goede spelling van het voltooid deelwoord van liken.", False, "Nederlandse regels: ge + like + t = geliket.", "Engelse uitgang -ed bestaat niet in het Nederlands."),
]

OEF_C7_11 = [
    omc(1, "Kies de juiste vorm: <i>Wat ___ er als je op deze knop drukt?</i>", "gebeurt", ["gebeurd", "gebeurdt", "gebeurde"], "Persoonsvorm, tegenwoordige tijd, onderwerp 'er/het' → stam + t.", "Lopen-test: wat loopt er?"),
    omc(2, "Kies de juiste vorm: <i>Er is gisteren iets vreemds ___.</i>", "gebeurd", ["gebeurt", "gebeurdt", "gebeurde"], "Is + werkwoord achteraan = voltooid deelwoord. Verleng: het gebeurde → d.", "Staat er een hulpwerkwoord?"),
    oin(2, "Vul in: <i>Ik heb mijn wachtwoord ___ (veranderen).</i>", "veranderd", "Voltooid deelwoord (bij heb). Verleng: het veranderde wachtwoord → d.", "Hebben + voltooid deelwoord."),
    oin(2, "Vul in: <i>Mijn mening ___ (veranderen) nooit.</i>", "verandert", "Persoonsvorm bij 'mijn mening' (= zij) → stam + t.", "Enige werkwoord in de zin."),
    oin(3, "Vul in: <i>De brief is gisteren ___ (beantwoorden).</i>", "beantwoord", "Voltooid deelwoord; be- → geen ge-. De stam eindigt al op d.", "Be- krijgt geen ge-."),
    omc(3, "In welke zin staat een fout?", "Wat is er met je fiets gebeurt?", ["Wat gebeurt er met je fiets?", "Wat gebeurde er met je fiets?", "Er is iets met je fiets gebeurd."], "'Is … gebeurd' is een voltooid deelwoord → met d.", "Zoek het hulpwerkwoord."),
    ow(1, "<i>Gebeurt</i> en <i>gebeurd</i> klinken hetzelfde, maar het ene is een persoonsvorm en het andere een voltooid deelwoord.", True, "Dat heet homofoon.", "Homofoon = klinkt hetzelfde."),
    ow(2, "In de zin <i>Het weer veranderd snel</i> is veranderd goed gespeld.", False, "Het is de persoonsvorm (tegenwoordige tijd) → verandert.", "Is er een hulpwerkwoord?"),
]

OEF_C7_3B = [
    omc(1, "Kies de juiste combinatie: <i>Ik kreeg een ___ trui en een ___ boek.</i>", "warme – dik", ["warm – dik", "warme – dikke", "warm – dikke"],
        "De trui is een de-woord → altijd -e (warme). Het boek is een het-woord na een → geen -e (dik).", "De trui, het boek."),
    omc(1, "Kies de juiste combinatie: <i>Hij woont in een ___ huis met een ___ tuin.</i>", "klein – grote", ["kleine – grote", "klein – groot", "kleine – groot"],
        "Het huis + een → geen -e (klein). De tuin is een de-woord → -e (grote).", "Het huis, de tuin."),
    omc(2, "Kies de juiste combinatie: <i>Dat ___ meisje heeft een ___ konijn.</i>", "lieve – wit", ["lief – wit", "lieve – witte", "lief – witte"],
        "Na dat → -e (lieve). Het konijn + een → geen -e (wit).", "Dat + het-woord, een + het-woord."),
    omc(2, "Kies de juiste vorm: <i>Mijn opa draagt een ___ horloge.</i>", "gouden", ["goude", "goudene", "goud"],
        "Materiaal → altijd -en.", "Stoffelijk bijvoeglijk naamwoord."),
    oin(2, "Vul in (wol): <i>Op de bank lag een ___ deken.</i>", "wollen", "Materiaal → -en: wollen.", "Van welk materiaal?"),
    oin(2, "Vul in (glas): <i>Pas op met die ___ schaal.</i>", "glazen", "Materiaal → -en: glazen.", "Stoffelijk: altijd -en."),
    ow(1, "Bij een meervoud krijgt het bijvoeglijk naamwoord altijd een -e: <i>mooie boeken</i>.", True, "Meervoud = -e.", "Kijk naar het getal."),
    ow(2, "Je schrijft <i>een dure boek</i>, want boek is een de-woord.", False, "Het boek is een het-woord; na een → geen -e: een duur boek.", "De boek of het boek?"),
    ow(3, "Na <i>elk</i> krijgt een bijvoeglijk naamwoord bij een het-woord geen -e: <i>elk nieuw seizoen</i>.", True, "Elk/ieder/een/geen + het-woord → geen -e.", "Seizoen is een het-woord."),
]

OEF_BEGR = [
    omc(1, "Welk begrip hoort bij: <i>het werkwoord dat verandert als je de tijd van de zin verandert</i>?", "persoonsvorm", ["stam", "voltooid deelwoord", "hele werkwoord"], "Dat is de definitie van de persoonsvorm.", "Hij loopt → hij liep."),
    omc(1, "Wat is de stam van <i>zetten</i>?", "zet", ["zett", "zette", "zetten"], "Hele werkwoord min -en, dubbele t wordt enkel: zet.", "De ik-vorm."),
    omc(2, "Welk werkwoord is sterk?", "zwemmen", ["werken", "fietsen", "praten"], "Zwemmen – zwom – gezwommen: de klinker verandert.", "Verandert de klinker in de verleden tijd?"),
    omc(2, "Welk werkwoord is scheidbaar?", "opbellen", ["vertellen", "bewaren", "herhalen"], "Opbellen → ik bel op. De andere gaan niet uit elkaar.", "Kun je het werkwoord splitsen?"),
    oin(2, "Hoe heet het ezelsbruggetje met de letters t, k, f, s, ch, p en x?", "'t kofschip|kofschip|'t kofschip x|kofschip x|t kofschip", "Het ezelsbruggetje heet 't kofschip X.", "Een schip!"),
    oin(3, "Hoe heten vormen die hetzelfde klinken maar anders geschreven worden, zoals gebeurt en gebeurd?", "homofoon|homofonen|homofone werkwoordsvormen|homofone vormen", "Homofoon = gelijkklinkend.", "Begint met homo-."),
    ow(1, "Het voltooid deelwoord hoort bij hebben, zijn of worden.", True, "Heb gewerkt, is gevonden, wordt gemaakt.", "Heb ge…"),
    ow(2, "De stam is altijd precies het hele werkwoord min -en, zonder verdere aanpassing.", False, "Je past de spelling aan: lopen → loop, leven → leef.", "Denk aan lopen."),
]

# =====================================================================================================
# TOETSEN (20 vragen)
# =====================================================================================================
TOETSEN = []

# 53 · §9 Tegenwoordige tijd
TOETSEN.append(dict(par="7.9", hf=7, titel="§9 Werkwoordspelling: tegenwoordige tijd", icoon="⏱️", vragen=[
    I("Hij ____ (vinden) het boek erg spannend.", "vindt", "Hij → stam + t. Stam vind + t = vindt. Lopen-test: hij loopt."),
    I("Tim ____ (snijden) de groenten in kleine stukjes.", "snijdt", "Tim = hij → stam (snijd) + t = snijdt."),
    I("Jij ____ (antwoorden) altijd heel snel in de groepsapp.", "antwoordt", "Jij staat vóór de persoonsvorm → stam (antwoord) + t."),
    I("Het meisje ____ (rijden) elke zaterdag paard.", "rijdt", "Het meisje = zij → stam (rijd) + t."),
    I("Mijn vader ____ (wachten) al een uur op de bus.", "wacht", "De stam wacht eindigt al op een t → er komt geen tweede t bij."),
    I("____ (fietsen) jij morgen ook naar school?", "Fiets", "Jij staat achter de persoonsvorm → geen t: Fiets jij?"),
    I("Ik ____ (worden) hier niet goed van.", "word", "Ik → alleen de stam: word. De d hoor je niet, maar je schrijft hem wel."),
    I("Hoe laat ____ (beginnen) de les morgen?", "begint", "De les = hij/zij → stam (begin) + t. Begint is sterk, maar in de tegenwoordige tijd gewoon stam + t."),
    I("Mijn zus ____ (houden) niet van spruitjes.", "houdt", "Mijn zus = zij → stam (houd) + t."),
    I("____ (maken) je je huiswerk vanavond nog?", "Maak", "Je staat achter de persoonsvorm → geen t: Maak je?"),
    mc("Kies de juiste vorm: <i>Wanneer ____ (worden) je zestien?</i>", "word", ["wordt", "worden", "wort"],
       "Je staat achter de persoonsvorm → de t valt weg: Wanneer word je zestien?"),
    mc("Kies de juiste vorm: <i>____ (worden) u al geholpen?</i>", "Wordt", ["Word", "Worden", "Wort"],
       "Bij u blijft de t altijd staan, ook als u achter de persoonsvorm staat."),
    mc("Welke zin is goed gespeld?", "Vind jij dat ook?", ["Vindt jij dat ook?", "Vint jij dat ook?", "Vinde jij dat ook?"],
       "Vraagzin, jij staat achter de persoonsvorm → geen t. De d van de stam blijft: Vind jij?"),
    mc("Kies de juiste vorm: <i>Morgen ____ (uitreiken) jij de prijzen uit.</i>", "reik", ["reikt", "reikd", "reiken"],
       "Jij staat achter de persoonsvorm (morgen reik jij) → alleen de stam."),
    mc("Kies de juiste vorm: <i>Als jij dat ____ (vinden), moet je het zeggen.</i>", "vindt", ["vind", "vint", "vinden"],
       "In de bijzin staat jij vóór de persoonsvorm → stam + t = vindt."),
    mc("Kies de juiste vorm: <i>____ (gaan) je broer ook mee naar het feest?</i>", "Gaat", ["Ga", "Gaan", "Gaad"],
       "Je broer = hij, niet jij! Hij → stam + t: Gaat je broer mee?"),
    W("Als jij of je achter de persoonsvorm staat, valt de t weg: <i>Loop jij mee?</i>", True,
      "Bij inversie met jij/je gebruik je alleen de stam."),
    W("Bij u valt de t ook weg als u achter de persoonsvorm staat: <i>Word u geholpen?</i>", False,
      "Bij u blijft de t altijd: Wordt u geholpen?"),
    W("De stam van <i>verhuizen</i> is <i>verhuiz</i>.", False,
      "Aan het eind wordt z een s: de stam is verhuis (ik verhuis)."),
    O("Leg uit waarom je <i>vindt</i> met dt schrijft in: <i>Mijn moeder vindt het goed.</i>",
      ["stam", "hij/zij/enkelvoud/derde persoon"],
      "De stam van vinden is vind (met een d). Mijn moeder is zij (enkelvoud), dus stam + t: vind + t = vindt.",
      "Stam (vind) + t bij hij/zij/het."),
]))

# 54 · §9 Verleden tijd
TOETSEN.append(dict(par="7.9", hf=7, titel="§9 Werkwoordspelling: verleden tijd", icoon="⌛", vragen=[
    I("Wij ____ (verhuizen) vorig jaar naar Amsterdam.", "verhuisden", "Verhuizen: de z zit niet in 't kofschip → -de/-den. Meervoud → verhuisden."),
    I("De storm ____ (verwoesten) ons tuinhuisje.", "verwoestte", "Stam verwoest → t zit in 't kofschip → -te: verwoest + te = verwoestte."),
    I("De meisjes ____ (staren) me al een tijdje aan.", "staarden", "Stam staar → r zit niet in 't kofschip → -den (meervoud)."),
    I("Mijn opa ____ (leven) vroeger in Adana.", "leefde", "Leven: de v zit niet in 't kofschip → -de: leefde. Laat je niet foppen door de f."),
    I("Zij ____ (verheugen) zich heel erg op het schoolfeest.", "verheugde", "Stam verheug → g zit niet in 't kofschip → -de."),
    I("Wij ____ (lopen) samen naar het station.", "liepen", "Lopen is een sterk werkwoord: liep → meervoud liepen."),
    I("Jij ____ (praten) gisteren veel te hard.", "praatte", "Stam praat → t zit in 't kofschip → -te: praat + te = praatte."),
    I("Gisteren ____ (bellen) ik mijn oma in Turkije.", "belde", "Stam bel → l zit niet in 't kofschip → -de."),
    I("De kinderen ____ (dansen) de hele avond op het plein.", "dansten", "Stam dans → s zit in 't kofschip → -ten (meervoud)."),
    I("Ik ____ (zetten) mijn tas in de gang.", "zette", "Stam zet → t zit in 't kofschip → -te: zet + te = zette."),
    mc("Kies de juiste vorm: <i>Het oude huis ____ (afbranden) helemaal af.</i>", "brandde", ["brande", "brandte", "brant"],
       "Stam brand → d zit niet in 't kofschip → -de: brand + de = brandde."),
    mc("Welke letters horen bij 't kofschip X?", "t, k, f, s, ch, p, x", ["t, k, v, z, ch, p, x", "d, k, f, s, ch, p, x", "t, g, f, s, ch, b, x"],
       "'t kofschip X: t, k, f, s, ch, p en x. De v, z, d, g en b horen er niet bij."),
    mc("Waarom schrijf je <i>leefde</i> met -de?", "De v van leven zit niet in 't kofschip",
       ["De f van leef zit in 't kofschip", "Leven is een sterk werkwoord", "Na een lange klank komt altijd -de"],
       "Je kijkt naar het hele werkwoord: leven. De v zit niet in 't kofschip → -de."),
    mc("Wat is de verleden tijd van <i>vinden</i> bij hij?", "vond", ["vindde", "vondt", "vinde"],
       "Vinden is sterk: de klinker verandert (vond). Er komt geen -de of -t achter."),
    mc("Kies de juiste vorm: <i>Vorige week ____ (bouwen) wij een hut in het bos.</i>", "bouwden", ["bouwten", "bouwde", "bouwdden"],
       "Stam bouw → w zit niet in 't kofschip → -den (meervoud: wij)."),
    mc("Kies de juiste vorm: <i>Naast de politie ____ (worden) ook de brandweer opgeroepen.</i>", "werd", ["werdt", "wordde", "werden"],
       "Worden is sterk: werd. Onderwerp = ook de brandweer (enkelvoud) → werd, zonder t."),
    W("Bij sterke werkwoorden verandert de klinker in de verleden tijd, zoals <i>lopen → liep</i>.", True,
      "Sterke werkwoorden krijgen geen -te/-de; de klank verandert."),
    W("De verleden tijd van <i>verhuizen</i> is <i>verhuiste</i>, want je ziet een s in de stam.", False,
      "Kijk naar het hele werkwoord: de z zit niet in 't kofschip → verhuisde."),
    W("Bij <i>praten</i> schrijf je in de verleden tijd één t: <i>praate</i>.", False,
      "Stam praat + te = praatte, met twee t's."),
    O("Leg uit hoe je bepaalt of de verleden tijd van <i>werken</i> op -te of -de eindigt.",
      ["kofschip", "stam/laatste letter"],
      "Je kijkt naar de laatste letter van de stam (werk). De k zit in 't kofschip, dus -te: werkte.",
      "Laatste letter van de stam in 't kofschip → -te, anders -de."),
]))

# 55 · §9 Voltooid deelwoord
TOETSEN.append(dict(par="7.9", hf=7, titel="§9 Werkwoordspelling: voltooid deelwoord", icoon="✅", vragen=[
    I("Ik heb mijn kamer eindelijk ____ (opruimen).", "opgeruimd", "Scheidbaar: op + ge + ruim + d (m zit niet in 't kofschip)."),
    I("Tien woningen in de straat zijn ____ (ontruimen).", "ontruimd", "Ont- → geen extra ge-: ontruim + d."),
    I("Het pakketje is ____ (vinden) in de voortuin.", "gevonden", "Vinden is sterk: gevonden."),
    I("We hebben de presentatie goed ____ (voorbereiden).", "voorbereid", "De stam voorbereid eindigt al op een d → er komt niets bij (niet voorbereidt)."),
    I("Osdorp wordt ____ (teisteren) door explosies.", "geteisterd", "Ge + teister + d (r zit niet in 't kofschip)."),
    I("Hij heeft het hele huis ____ (verbouwen).", "verbouwd", "Ver- → geen ge-: verbouw + d."),
    I("Ik heb de hele middag ____ (fietsen).", "gefietst", "Stam fiets → s zit in 't kofschip → ge + fiets + t."),
    I("Zij heeft de tafel al ____ (dekken).", "gedekt", "Stam dek → k zit in 't kofschip → ge + dek + t."),
    I("De melding is rond half negen ____ (binnenkomen).", "binnengekomen", "Scheidbaar en sterk: binnen + ge + komen."),
    I("Heb jij je fiets al ____ (repareren)?", "gerepareerd", "Stam repareer → r zit niet in 't kofschip → ge + repareer + d."),
    I("Wij hebben de hele dag ____ (zwemmen).", "gezwommen", "Zwemmen is sterk: gezwommen."),
    mc("Kies het goede voltooid deelwoord: <i>Wij zijn vorige maand ____ (verhuizen).</i>", "verhuisd", ["verhuist", "geverhuisd", "verhuizd"],
       "Ver- → geen ge-. De z van verhuizen zit niet in 't kofschip → d: verhuisd."),
    mc("Kies het goede voltooid deelwoord: <i>Hij heeft lang in Spanje ____ (leven).</i>", "geleefd", ["geleeft", "geleevd", "geleefdt"],
       "De v van leven zit niet in 't kofschip → ge + leef + d."),
    mc("Kies het goede voltooid deelwoord: <i>Ik heb de koffie al ____ (zetten).</i>", "gezet", ["gezett", "gezetd", "gezetten"],
       "De stam zet eindigt al op t → er komt niets bij."),
    mc("Welk werkwoord krijgt GEEN ge- in het voltooid deelwoord?", "herhalen", ["fietsen", "opruimen", "wachten"],
       "Werkwoorden met her- (en be-, ver-, ont-, ge-, er-) krijgen geen extra ge-: herhaald."),
    mc("Hoe controleer je of een voltooid deelwoord op d of t eindigt?", "Je verlengt het tot een bijvoeglijk naamwoord",
       ["Je kijkt of het werkwoord sterk is", "Je telt de lettergrepen", "Je zet er 'ik' voor"],
       "Verlengen: het gebeurde ongeluk → d; het gewerkte uur → t."),
    W("Bij werkwoorden die beginnen met ver-, be- of ont- komt er geen extra ge- voor het voltooid deelwoord.", True,
      "Verbouwd, beantwoord, ontruimd."),
    W("Het voltooid deelwoord van <i>voorbereiden</i> is <i>voorbereidt</i>.", False,
      "De stam voorbereid eindigt al op d; er komt niets bij: voorbereid."),
    W("Bij een scheidbaar werkwoord zoals <i>opruimen</i> komt ge- vooraan: <i>geopruimd</i>.", False,
      "Ge- komt in het midden: opgeruimd."),
    O("Leg uit waarom <i>gefietst</i> met een t eindigt.",
      ["kofschip", "stam/laatste letter"],
      "De stam is fiets; de laatste letter van de stam, de s, zit in 't kofschip. Daarom ge + stam + t.",
      "Laatste letter van de stam in 't kofschip → t."),
]))

# 56 · §11 Homofone werkwoordsvormen
TOETSEN.append(dict(par="7.11", hf=7, titel="§11 Homofone werkwoordsvormen", icoon="👂", vragen=[
    mc("Kies de juiste vorm: <i>Er staat een ambulance voor de deur. Wat is er ____ (gebeuren)?</i>", "gebeurd", ["gebeurt", "gebeurdt", "gebeurde"],
       "Is + werkwoord achteraan = voltooid deelwoord. Verleng: het gebeurde → d."),
    mc("Kies de juiste vorm: <i>Wat ____ (gebeuren) er nu buiten op het schoolplein?</i>", "gebeurt", ["gebeurd", "gebeurdt", "gebeurde"],
       "Enige werkwoord = persoonsvorm in de tegenwoordige tijd → stam + t."),
    I("Ik heb de instellingen ____ (veranderen).", "veranderd", "Heb + voltooid deelwoord. Verleng: de veranderde instellingen → d."),
    I("Het weer ____ (veranderen) elke dag.", "verandert", "Persoonsvorm bij het weer (= het) → stam + t."),
    mc("Kies de juiste vorm: <i>Hij ____ (worden) nu steeds bozer.</i>", "wordt", ["word", "wort", "worden"],
       "Hij → stam (word) + t = wordt."),
    mc("Kies de juiste vorm: <i>Gisteren ____ (gebeuren) er iets geks op school.</i>", "gebeurde", ["gebeurt", "gebeurd", "gebeurdde"],
       "Gisteren → verleden tijd. Stam gebeur → r niet in 't kofschip → -de."),
    I("Mijn broer ____ (vinden) dat altijd leuk.", "vindt", "Mijn broer = hij → stam + t."),
    mc("Welke vorm past? <i>Zo'n ruzie ____ (gebeuren) bij ons thuis ook vaak.</i>", "gebeurt", ["gebeurd", "gebeurdt", "gebeurde"],
       "Persoonsvorm in de tegenwoordige tijd, onderwerp zo'n ruzie (enkelvoud) → stam + t."),
    I("We hebben de hele avond ____ (praten).", "gepraat", "De stam praat eindigt al op t → ge + praat."),
    mc("Kies de juiste vorm: <i>Zij ____ (beantwoorden) elke mail binnen een uur.</i>", "beantwoordt", ["beantwoord", "beantwoort", "beantwoorden"],
       "Zij (enkelvoud) → stam (beantwoord) + t = beantwoordt."),
    mc("Kies de juiste vorm: <i>Alle vragen zijn nu ____ (beantwoorden).</i>", "beantwoord", ["beantwoordt", "beantwoort", "gebeantwoord"],
       "Zijn + voltooid deelwoord; be- → geen ge-. De stam eindigt al op d."),
    I("Hij ____ (verhuizen) volgende maand naar Utrecht.", "verhuist", "Persoonsvorm bij hij → stam (verhuis) + t."),
    I("Mijn buren zijn vorig jaar ____ (verhuizen).", "verhuisd", "Zijn + voltooid deelwoord; verhuizen → z niet in 't kofschip → d."),
    mc("Welke zin is zonder fouten?", "Het weer verandert snel.", ["Het weer veranderd snel.", "Ik heb niets verandert.", "Wat is er gebeurt?"],
       "Verandert is hier de persoonsvorm bij het weer → t. De andere zinnen bevatten een voltooid deelwoord dat met d moet."),
    mc("In welke zin staat geen spelfout?", "Hij heeft de taart versierd.", ["Hij versierd de taart.", "De taart is versiert.", "Versierd jij de taart?"],
       "Heeft + voltooid deelwoord → versierd. Hij versiert, versiert is, Versier jij."),
    W("In <i>Wat is er gebeurd?</i> is gebeurd een voltooid deelwoord.", True,
      "Het hoort bij de persoonsvorm is."),
    W("In <i>Het weer veranderd</i> is veranderd goed gespeld, want het is verleden tijd.", False,
      "Het is de persoonsvorm in de tegenwoordige tijd: het weer verandert. De verleden tijd zou veranderde zijn."),
    W("Met de lopen-test kun je controleren of een persoonsvorm een t krijgt: <i>het loopt → het gebeurt</i>.", True,
      "Hoor je bij lopen een t, dan krijgt ook het andere werkwoord een t."),
    W("Als er een vorm van hebben of zijn in de zin staat, is het werkwoord achteraan meestal een persoonsvorm.", False,
      "Dan is hebben/zijn de persoonsvorm en is het werkwoord achteraan een voltooid deelwoord."),
    O("Leg uit hoe je ziet dat <i>gebeurd</i> in <i>Er is iets ergs gebeurd</i> met een d eindigt.",
      ["voltooid deelwoord", "verleng/verlengen/gebeurde"],
      "Gebeurd is hier een voltooid deelwoord (bij is). Als je het verlengt, hoor je een d: het gebeurde ongeluk.",
      "Voltooid deelwoord: verlengen → d."),
]))

# 57 · §10 Engelse werkwoorden
TOETSEN.append(dict(par="7.10", hf=7, titel="§10 Engelse werkwoorden", icoon="🇬🇧", vragen=[
    I("Gisteren ____ (updaten) ik de website.", "updatete", "Stam update eindigt op een t-klank → -te."),
    I("Zij heeft het bestand ____ (downloaden).", "gedownload", "Stam download eindigt al op een d → ge + download, niets erachter."),
    I("Vorige week ____ (streamen) we een wedstrijd.", "streamden", "Stam stream eindigt op een m-klank → -den (meervoud: we)."),
    I("Ik heb de politie meteen ____ (appen).", "geappt", "Stam app → p zit in 't kofschip → ge + app + t."),
    I("Iedereen heeft mijn post ____ (liken).", "geliket", "Stam like eindigt op een k-klank → ge + like + t."),
    I("De game ____ (crashen) gisteren steeds.", "crashte", "Stam crash eindigt op de sj-klank (zoals sch) → -te."),
    I("De politie heeft de omgeving ____ (checken).", "gecheckt", "Stam check → k-klank → ge + check + t."),
    I("Mijn broer ____ (skaten) elke middag in het park.", "skatet", "Hij → stam (skate) + t."),
    I("Ik ____ (mailen) de docent gisteren een vraag.", "mailde", "Stam mail eindigt op een l-klank → -de."),
    I("Heb jij de foto al ____ (posten)?", "gepost", "Stam post eindigt al op t → ge + post."),
    mc("Kies het goede voltooid deelwoord: <i>De video is gisteren ____ (uploaden).</i>", "geüpload", ["geupload", "geuploadt", "geüploadt"],
       "Ge + upload; e en u spreek je los uit → trema. Stam eindigt op d → niets erachter."),
    mc("Kies het goede voltooid deelwoord: <i>Gelukkig heb ik alles ____ (back-uppen).</i>", "geback-upt", ["gebackupt", "ge-back-upt", "geback-upd"],
       "Stam back-up (met streepje) eindigt op p → ge + back-up + t."),
    mc("Hoe bepaal je bij Engelse werkwoorden of je -te of -de schrijft?", "Je kijkt naar de laatste klank die je hoort",
       ["Je kijkt naar de laatste letter die je ziet", "Engelse werkwoorden krijgen altijd -de", "Engelse werkwoorden krijgen altijd -te"],
       "Update eindigt op een e, maar je hoort een t → updatete."),
    mc("Wat is de stam van <i>updaten</i>?", "update", ["updat", "updaat", "updatt"],
       "Hele werkwoord min -en, Engelse spelling blijft: update."),
    mc("Kies de juiste vorm: <i>Gisteren ____ (liken) hij al mijn foto's.</i>", "likete", ["likede", "liekte", "liked"],
       "Stam like, k-klank → -te: likete."),
    mc("Kies de juiste vorm: <i>Ik heb het nieuwe nummer al ____ (downloaden).</i>", "gedownload", ["gedownloadt", "gedownloaded", "downgeload"],
       "Ge + download; de stam eindigt al op d."),
    W("Bij de stam van een Engels werkwoord houd je de Engelse spelling: <i>liken → like</i>.", True,
      "Je schrijft dus like, niet lik of laik."),
    W("Bij <i>updaten</i> kijk je naar de laatste letter e; die zit niet in 't kofschip, dus <i>updatede</i>.", False,
      "Je kijkt naar de klank: je hoort een t → updatete."),
    W("In <i>geüpload</i> staat een trema omdat het een Engels leenwoord is.", False,
      "Het trema staat er omdat je e en u los van elkaar uitspreekt (ge-up)."),
    O("Leg uit waarom je <i>gestreamd</i> met een d schrijft.",
      ["klank/hoort/uitspraak", "kofschip"],
      "De laatste klank van de stam stream is een m. Die klank zit niet in 't kofschip, dus ge + stam + d.",
      "Laatste klank m → niet in 't kofschip → d."),
]))

# 58 · §3 Bijvoeglijk naamwoord -e
TOETSEN.append(dict(par="7.3", hf=7, titel="Bijvoeglijk naamwoord: met of zonder -e?", icoon="🏷️", vragen=[
    mc("Kies de juiste vorm: <i>Mijn broer kocht een ____ horloge.</i>", "duur", ["dure", "duren"], "Het horloge + een → geen -e."),
    mc("Kies de juiste vorm: <i>Ik heb gisteren een ____ artikel gelezen.</i>", "interessant", ["interessante", "interessanten"], "Het artikel + een → geen -e."),
    mc("Kies de juiste vorm: <i>Het ____ boek ligt op tafel.</i>", "zachte", ["zacht", "zachten"], "Na het krijgt het bijvoeglijk naamwoord een -e."),
    mc("Kies de juiste vorm: <i>Elk ____ spel heeft weer andere regels.</i>", "nieuw", ["nieuwe", "nieuwen"], "Het spel + elk → geen -e."),
    mc("Kies de juiste vorm: <i>Dat is een ____ vriend van mij.</i>", "leuke", ["leuk", "leuken"], "De vriend → de-woord krijgt altijd een -e."),
    mc("Kies de juiste vorm: <i>De ____ tafel staat al jaren in de kamer.</i>", "houten", ["houte", "houtene"], "Materiaal (hout) → altijd -en."),
    mc("Kies de juiste vorm: <i>Zij droeg een ____ ketting om haar nek.</i>", "zilveren", ["zilvere", "zilverene"], "Materiaal (zilver) → altijd -en."),
    mc("Kies de juiste vorm: <i>De ____ dozen op de gang moeten weg.</i>", "kartonnen", ["kartonne", "kartonnene"], "Materiaal (karton) → altijd -en."),
    mc("Kies de juiste vorm: <i>Hij gaf zijn vriendin een ____ cadeau.</i>", "prachtig", ["prachtige", "prachtigen"], "Het cadeau + een → geen -e."),
    mc("Kies de juiste vorm: <i>De ____ medewerkers begeleidden de nieuwe collega's.</i>", "ervaren", ["ervarene", "ervarenen"], "Eindigt al op -en → geen extra -e."),
    mc("Kies de juiste vorm: <i>Wij hebben een ____ huis aan de rand van de stad gekocht.</i>", "oud", ["oude", "ouden"], "Het huis + een → geen -e."),
    mc("Kies de juiste vorm: <i>Mijn ____ spel is nu al kapot.</i>", "nieuwe", ["nieuw", "nieuwen"], "Na mijn krijgt het bijvoeglijk naamwoord een -e."),
    mc("Kies de juiste vorm: <i>Geen ____ vriend zou zoiets doen.</i>", "echte", ["echt", "echten"], "De vriend → de-woord → altijd -e, ook na geen."),
    mc("Kies de juiste vorm: <i>In de keuken staan drie ____ flessen.</i>", "glazen", ["glaze", "glazene"], "Materiaal (glas) → altijd -en."),
    mc("Kies de juiste vorm: <i>Dit ____ weer is perfect voor het strand.</i>", "mooie", ["mooi", "mooien"], "Na dit krijgt het bijvoeglijk naamwoord een -e."),
    W("Een bijvoeglijk naamwoord bij een de-woord krijgt altijd een -e, ook na een: <i>een leuke vriend</i>.", True,
      "Bij de-woorden en in het meervoud is het altijd -e."),
    W("Na <i>een</i> krijgt een bijvoeglijk naamwoord bij een het-woord ook een -e: <i>een nieuwe spel</i>.", False,
      "Het-woord + een/geen/elk/ieder → geen -e: een nieuw spel."),
    W("Stoffelijke bijvoeglijke naamwoorden zoals <i>houten</i> en <i>gouden</i> eindigen altijd op -en.", True,
      "Ze zeggen van welk materiaal iets gemaakt is."),
    W("Bij een meervoud krijgt het bijvoeglijk naamwoord nooit een -e: <i>nieuw spellen</i>.", False,
      "In het meervoud is het altijd -e: nieuwe spellen."),
    O("Leg uit waarom je <i>een duur horloge</i> schrijft en niet <i>een dure horloge</i>.",
      ["het-woord/onzijdig/het horloge"],
      "Horloge is een het-woord (het horloge). Bij een het-woord krijgt het bijvoeglijk naamwoord na een geen -e.",
      "Het-woord + een → geen -e."),
]))

# 59 · Spellingdetective (mix werkwoorden)
TOETSEN.append(dict(par="mix", hf=7, titel="Spellingdetective: verbeter de werkwoorden", icoon="🕵️", vragen=[
    I("Verbeter het foute werkwoord: <i>Ik heb hem gisteren gedownloadt.</i>", "gedownload", "Stam download eindigt al op d → er komt geen t achter: gedownload."),
    I("Verbeter het foute werkwoord: <i>Ik update de game gisteren al.</i>", "updatete", "Gisteren → verleden tijd. Stam update, t-klank → updatete."),
    I("Verbeter het foute werkwoord: <i>Dat gebeurdt bij mij ook.</i>", "gebeurt", "Persoonsvorm, tegenwoordige tijd: stam gebeur + t = gebeurt."),
    I("Verbeter het foute werkwoord: <i>Ik heb de instellingen verandert.</i>", "veranderd", "Heb + voltooid deelwoord; verleng: de veranderde instellingen → d."),
    I("Verbeter het foute werkwoord: <i>Mijn broer vind dat altijd leuk.</i>", "vindt", "Mijn broer = hij → stam + t: vindt."),
    I("Verbeter het foute werkwoord: <i>We hebben alles goed voorbereidt.</i>", "voorbereid", "Voltooid deelwoord; de stam eindigt al op d: voorbereid."),
    I("Verbeter het foute werkwoord: <i>Hebben jullie de game al geinstalleerd?</i>", "geïnstalleerd", "Ge + installeer + d; e en i spreek je los uit → trema: geïnstalleerd."),
    I("Verbeter het foute werkwoord: <i>Ik heb de link al geupload.</i>", "geüpload", "Ge + upload; e en u los uitspreken → trema: geüpload."),
    I("Verbeter het foute werkwoord: <i>Iedereen heeft de foto geliked.</i>", "geliket", "Nederlandse regels: ge + like + t (k-klank) = geliket."),
    I("Verbeter het foute werkwoord: <i>Ik streamde het straks ook nog even.</i>", "stream", "Straks = toekomst → tegenwoordige tijd. Ik → stam: stream."),
    mc("Welk woord is fout gespeld? <i>De melding kwam rond half negen binnen en de politie werd direct gebelt.</i>", "gebelt", ["kwam", "werd", "binnen"],
       "Voltooid deelwoord van bellen: ge + bel + d = gebeld (l zit niet in 't kofschip)."),
    mc("Welk woord is fout gespeld? <i>Hij vind dat de agent goed heeft gereageerd.</i>", "vind", ["heeft", "gereageerd", "goed"],
       "Hij → stam + t: vindt."),
    mc("Welk woord is fout gespeld? <i>Gisteren checkte ik mijn mail en antwoorde ik meteen.</i>", "antwoorde", ["checkte", "mijn", "meteen"],
       "Stam antwoord + de = antwoordde (twee d's)."),
    mc("Welk woord is fout gespeld? <i>Wordt jij ook gevraagd om je te melden?</i>", "Wordt", ["gevraagd", "melden", "jij"],
       "Jij staat achter de persoonsvorm → geen t: Word jij."),
    mc("Welk woord is fout gespeld? <i>Een getuige heeft de beelden geappt en daarna gestreamt.</i>", "gestreamt", ["geappt", "beelden", "daarna"],
       "Stream eindigt op een m-klank → d: gestreamd."),
    mc("Welk woord is fout gespeld? <i>Tijdens de les verveelde ik me, want de les duurden erg lang.</i>", "duurden", ["verveelde", "tijdens", "lang"],
       "Onderwerp de les = enkelvoud → duurde (zonder n)."),
    W("In <i>Mijn broer vind dat leuk</i> staat een fout: het moet <i>vindt</i> zijn.", True,
      "Mijn broer = hij → stam + t."),
    W("In <i>Wordt jij later dokter?</i> is wordt goed gespeld.", False,
      "Jij staat achter de persoonsvorm → Word jij."),
    W("In <i>Ik heb alles gechecked</i> is gechecked goed gespeld.", False,
      "Nederlandse regels: ge + check + t = gecheckt."),
    O("In de zin <i>Het pakketje werd in de tuin gevonden en de EOD bepaald wat ermee gebeurt</i> staat één fout. Welk woord is fout, hoe schrijf je het goed en waarom?",
      ["bepaalt", "persoonsvorm/stam/enkelvoud"],
      "Bepaald is fout; het moet bepaalt zijn. Het is de persoonsvorm in de tegenwoordige tijd bij de EOD (enkelvoud): stam bepaal + t.",
      "Persoonsvorm bij de EOD (hij) → stam + t: bepaalt."),
]))

# 60 · Mix spelling lesnotities (n, trema, apostrof, accenten)
TOETSEN.append(dict(par="mix", hf=7, titel="Mix lesnotities: -n, trema, apostrof en accenten", icoon="🧪", vragen=[
    mc("Kies de juiste vorm: <i>De ____ van de klas mochten als eerste beginnen.</i>", "jongsten", ["jongste"],
       "Personen, meervoud (mochten) → jongsten."),
    mc("Kies de juiste vorm: <i>De ____ kregen hulp van vrijwilligers.</i>", "armen", ["arme"],
       "Personen, meervoud (kregen) → armen."),
    mc("Kies de juiste vorm: <i>Als ____ heb je tijd voor vrijwilligerswerk.</i>", "gepensioneerde", ["gepensioneerden"],
       "Eén persoon (als … heb je) → enkelvoud: -e zonder n."),
    mc("Kies de juiste vorm: <i>____ deelnemers kregen na afloop een certificaat.</i>", "Alle", ["Allen"],
       "Er volgt een zelfstandig naamwoord (deelnemers) → zonder n."),
    mc("Kies de juiste vorm: <i>____ van hen bleven nog even napraten.</i>", "Enkelen", ["Enkele"],
       "Zelfstandig gebruikt en het gaat om personen (hen) → met n."),
    mc("Kies de juiste vorm: <i>In de etalage lagen vijf horloges: drie ____ en twee goedkope.</i>", "peperdure", ["peperduren"],
       "Zelfstandig gebruikt, maar het gaat om dingen → -e zonder n."),
    mc("Kies de juiste vorm: <i>De bezoekers kregen een formulier. ____ moesten het bij de uitgang inleveren.</i>", "Allen", ["Alle"],
       "Zelfstandig gebruikt (geen zelfstandig naamwoord erachter) en het gaat om personen → met n."),
    mc("Welke spelling is goed?", "ideeën", ["ideeen", "ideëen", "ideën"],
       "Het trema staat op de eerste klinker van de nieuwe lettergreep: idee-en → ideeën."),
    mc("Hoe schrijf je de eigenaar van een auto als één woord?", "auto-eigenaar", ["autoëigenaar", "autoeigenaar", "auto-ëigenaar"],
       "In een samenstelling gebruik je een koppelteken in plaats van een trema."),
    mc("Wat is het verkleinwoord van <i>baby</i>?", "baby'tje", ["babytje", "babietje", "baby-tje"],
       "Eindigt op -y met een medeklinker ervoor → apostrof: baby'tje."),
    mc("Wat is het verkleinwoord van <i>display</i>?", "displaytje", ["display'tje", "displayetje", "display-tje"],
       "Voor de -y staat een klinker (a) → geen apostrof: displaytje."),
    mc("Hoe schrijf je: de gitaar van Hans?", "Hans' gitaar", ["Hans's gitaar", "Hansen gitaar", "Hans gitaar'"],
       "Naam op -s → alleen een apostrof: Hans' gitaar."),
    mc("In welk woord staat het trema goed?", "reünie", ["reunie", "rëunie", "reüni"],
       "Re-unie: de u begint een nieuwe lettergreep, dus het trema staat op de u: reünie."),
    mc("Wat doet de cedille in <i>Curaçao</i>?", "De c klinkt als s", ["De c klinkt als k", "De a klinkt langer", "De c valt weg"],
       "Ç klinkt als s. Normaal klinkt de c voor a, o en u als k."),
    mc("In welke zin is het accent goed gebruikt?", "Ik heb één broer en twee zussen.",
       ["Ik heb éen broer en twee zussen.", "Kan één van jullie even helpen?", "Ik heb eén broer en twee zussen."],
       "Eén benadrukt het getal 1. In 'Kan een van jullie' kan een alleen 1 betekenen → geen accent nodig."),
    W("Bij <i>zee-egel</i> staat een streepje omdat het een samenstelling is; een trema hoort daar niet.", True,
      "In samenstellingen gebruik je een koppelteken: zee-egel, auto-eigenaar."),
    W("Het meervoud van <i>kiwi</i> schrijf je zonder apostrof: <i>kiwis</i>.", False,
      "Eindigt op één klinker (i) → apostrof: kiwi's."),
    W("Ook als het om dingen gaat, krijgt een woord als <i>miljoenen</i> een n: <i>miljoenen sterren</i>.", True,
      "Tientallen, honderden, duizenden en miljoenen hebben altijd een n."),
    W("Een stoffelijk bijvoeglijk naamwoord krijgt in het meervoud een extra -e: <i>houtene stoelen</i>.", False,
      "Stoffelijk blijft altijd -en: houten stoelen."),
    O("Leg uit waarom je <i>'s avonds</i> met een apostrof schrijft.",
      ["weglating/weggelaten/weglatingsteken", "des"],
      "De apostrof is een weglatingsteken: er is iets weggelaten, want 's avonds komt van des avonds.",
      "Weglatingsteken: 's avonds = des avonds."),
]))

# 61 · Mix lesnotities Cursus 5: samentrekking + verwijzen
TOETSEN.append(dict(par="mix", hf=5, titel="Mix lesnotities: samentrekking en verwijzen", icoon="🔗", vragen=[
    mc("<i>Voor- en nadelen</i> is een samentrekking op …", "woordniveau, achterwaarts", ["woordniveau, voorwaarts", "zinsniveau, voorwaarts", "zinsniveau, achterwaarts"],
       "Deel van een woord (-delen) + streepje → woordniveau. Het gemeenschappelijke deel staat achteraan → achterwaarts."),
    mc("<i>Ik heb de voorste rij gereserveerd in plaats van de achterste.</i> Wat voor samentrekking is dit?", "voorwaartse samentrekking", ["achterwaartse samentrekking", "geen samentrekking"],
       "'Rij' staat eerst en wordt verderop weggelaten → voorwaarts."),
    mc("<i>Didi bakt pannenkoeken en Ivan een pizza.</i> Is deze samentrekking juist?", "Ja, op zinsniveau", ["Nee, het getal verschilt", "Nee, de betekenis verschilt", "Nee, de functie verschilt"],
       "'Bakt' heeft in beide delen dezelfde functie, betekenis en hetzelfde getal → juist."),
    mc("<i>Die cola bevat geen koolzuur meer en vind ik niet lekker.</i> Wat is er fout?", "De functie verschilt", ["Het getal verschilt", "De betekenis verschilt", "Er is niets fout"],
       "'Die cola' is eerst onderwerp en daarna lijdend voorwerp → andere functie."),
    mc("<i>Paco haalde een goed cijfer en Lola de nieuwste update binnen.</i> Wat is er fout?", "De betekenis verschilt", ["Het getal verschilt", "De functie verschilt", "Er is niets fout"],
       "'Halen' (een cijfer) is iets anders dan 'binnenhalen' → andere betekenis."),
    mc("<i>Er wordt een tribune opgebouwd en toiletten geplaatst.</i> Wat is er fout?", "Het getal verschilt", ["De betekenis verschilt", "De functie verschilt", "Er is niets fout"],
       "Wordt (enkelvoud) past niet bij toiletten (meervoud)."),
    mc("Kies de goede verbetering van: <i>Er wordt een tribune opgebouwd en toiletten geplaatst.</i>", "… en worden toiletten geplaatst.",
       ["… en wordt toiletten geplaatst.", "… en toiletten wordt geplaatst.", "… en geplaatst toiletten."],
       "Voeg de meervoudsvorm toe: en worden toiletten geplaatst."),
    mc("<i>Ik ga zowel met de snel- als de stoptrein.</i> Wat voor samentrekking is dit?", "achterwaartse samentrekking", ["voorwaartse samentrekking", "geen samentrekking"],
       "'Trein' staat achteraan en is daarvóór weggelaten → achterwaarts (woordniveau)."),
    mc("<i>De leerlingen hebben hun huiswerk gemaakt en de docent nagekeken.</i> Klopt deze samentrekking?", "Nee, het getal verschilt", ["Ja, alles klopt", "Nee, de functie verschilt", "Nee, de betekenis verschilt"],
       "Hebben (meervoud) past niet bij de docent (enkelvoud: heeft)."),
    mc("Welke is GEEN voorwaarde voor een goede samentrekking?", "hetzelfde aantal letters", ["dezelfde functie", "dezelfde betekenis", "hetzelfde getal"],
       "De drie voorwaarden: functie, betekenis en getal."),
    mc("Kies het goede verwijswoord: <i>Het meisje ____ naast mij zit, heet Lotte.</i>", "dat", ["die", "wie", "wat"],
       "Het meisje is een het-woord (onzijdig) → dat."),
    mc("Kies het goede verwijswoord: <i>De regering heeft ____ plannen bekendgemaakt.</i>", "haar", ["zijn", "hun", "hen"],
       "Woorden op -ing zijn vrouwelijk → haar."),
    mc("Kies het goede verwijswoord: <i>Nederland is bekend om ____ grachten en molens.</i>", "zijn", ["haar", "hun", "hen"],
       "Namen van landen zijn onzijdig → zijn."),
    mc("Kies het goede verwijswoord: <i>De fabriek ontsloeg veel van ____ werknemers.</i>", "haar", ["zijn", "hun", "hen"],
       "Woorden op -iek zijn vrouwelijk → haar."),
    mc("Kies het goede verwijswoord: <i>Mijn ouders wonen vlakbij; ik bezoek ____ vaak.</i>", "hen", ["hun", "hem", "haar"],
       "Wie bezoek ik? → lijdend voorwerp → hen."),
    mc("Kies het goede verwijswoord: <i>Mijn grootouders zijn jarig; ik geef ____ een bos bloemen.</i>", "hun", ["hen", "hem", "zij"],
       "Aan wie geef ik iets? (zonder voorzetsel) → meewerkend voorwerp → hun."),
    mc("Kies het goede verwijswoord: <i>Er stond een lange file, ____ erg tegenviel.</i>", "wat", ["die", "dat", "wie"],
       "Je verwijst naar de hele zin → wat."),
    mc("Kies het goede verwijswoord: <i>De man ____ ik boodschappen doe, heeft een luxe auto.</i>", "bij wie", ["waarbij", "bij die", "bij wat"],
       "Persoon + voorzetsel → voorzetsel + wie: bij wie."),
    W("Na een voorzetsel gebruik je <i>hen</i>: <i>Water was gevaarlijk voor hen.</i>", True,
      "Na een voorzetsel nooit hun."),
    W("Met <i>waarnaast</i> verwijs je naar een persoon: <i>Iedereen mag kiezen waarnaast hij zit.</i>", False,
      "Bij personen gebruik je voorzetsel + wie: naast wie."),
]))

# 62 · Begrippentoets werkwoordspelling
TOETSEN.append(dict(par="eind", hf=7, titel="Begrippentoets werkwoordspelling (§9–§11)", icoon="📖", vragen=[
    mc("Wat is de stam van een werkwoord?", "Het hele werkwoord min -en", ["Het werkwoord met -t erachter", "De vorm achter 'heeft'", "De verleden tijd"],
       "Stam = hele werkwoord min -en, in de spelling van de ik-vorm (loop, werk, vind)."),
    mc("Wat is de persoonsvorm?", "Het werkwoord dat met de tijd meeverandert", ["Het werkwoord dat altijd helemaal achteraan in de zin staat", "Het hele werkwoord", "Het voltooid deelwoord van de zin"],
       "Verander je de tijd van de zin, dan verandert de persoonsvorm mee: hij loopt → hij liep."),
    mc("Wat is een voltooid deelwoord?", "De vorm bij hebben, zijn of worden", ["De vorm bij ik in de tegenwoordige tijd", "De vorm die altijd op -t eindigt", "De vorm in de verleden tijd"],
       "Heb gewerkt, is gevonden, wordt gemaakt."),
    mc("Wat is een sterk werkwoord?", "Een werkwoord waarvan de klinker verandert", ["Een werkwoord dat in de verleden tijd altijd op -te eindigt", "Een werkwoord met een d in de stam", "Een werkwoord dat begint met ver-"],
       "Lopen – liep – gelopen: de klinker verandert."),
    mc("Wat is een scheidbaar werkwoord?", "Een werkwoord dat in de zin uit elkaar gaat", ["Een werkwoord met een voorvoegsel als ver-", "Een werkwoord uit het Engels", "Een werkwoord zonder voltooid deelwoord"],
       "Opruimen → ik ruim op."),
    mc("Wat zijn homofone werkwoordsvormen?", "Vormen die hetzelfde klinken maar anders worden geschreven", ["Vormen van sterke werkwoorden in de verleden tijd en het meervoud", "Werkwoorden uit het Engels", "Vormen met een trema"],
       "Gebeurt en gebeurd klinken hetzelfde."),
    mc("Wat bedoel je met <i>verlengen</i> bij een voltooid deelwoord?", "Er een bijvoeglijk naamwoord van maken", ["Er -en achter zetten om het meervoud te maken", "Het woord langzamer uitspreken", "Er ge- voor zetten"],
       "Het gebeurde ongeluk: zo hoor je of het een d of t is."),
    mc("Wat is het hele werkwoord?", "De vorm die in het woordenboek staat", ["De vorm bij hij en zij", "De stam met een t erachter", "De verleden tijd in het meervoud"],
       "Lopen, werken, vinden."),
    I("De stam van <i>verhuizen</i> is ____.", "verhuis", "Hele werkwoord min -en, z wordt s: verhuis."),
    I("De stam van <i>zetten</i> is ____.", "zet", "Hele werkwoord min -en, dubbele t wordt enkel: zet."),
    I("Het ezelsbruggetje met de letters t, k, f, s, ch, p en x heet ____.", "'t kofschip|kofschip|'t kofschip x|kofschip x|t kofschip", "Het heet 't kofschip X."),
    I("Het werkwoord dat verandert als je de tijd van de zin verandert, heet de ____.", "persoonsvorm", "Dat is de persoonsvorm."),
    I("<i>Gelopen</i> en <i>gefietst</i> zijn voorbeelden van een ____.", "voltooid deelwoord|voltooide deelwoorden|voltooide deelwoord", "Het zijn voltooide deelwoorden."),
    I("Een werkwoord zoals <i>lopen – liep</i> heet een ____ werkwoord.", "sterk|onregelmatig|sterke|onregelmatige", "De klinker verandert → sterk (onregelmatig)."),
    I("Een werkwoord zoals <i>werken – werkte</i> heet een ____ werkwoord.", "zwak|regelmatig|zwakke|regelmatige", "Krijgt -te/-de → zwak (regelmatig)."),
    W("Een zwak werkwoord krijgt in de verleden tijd -te of -de achter de stam.", True, "Werkte, hoorde."),
    W("<i>Opruimen</i> is een scheidbaar werkwoord: <i>ik ruim op</i>.", True, "Het gaat in de zin uit elkaar."),
    W("De persoonsvorm staat altijd helemaal achteraan in de zin.", False, "In een hoofdzin staat de persoonsvorm meestal op de eerste of tweede plaats."),
    W("De stam is altijd hetzelfde als het hele werkwoord.", False, "Stam = hele werkwoord min -en: lopen → loop."),
    O("Leg uit wat het verschil is tussen een zwak en een sterk werkwoord.",
      ["klinker", "te/de/-te/-de/kofschip"],
      "Bij een sterk werkwoord verandert de klinker in de verleden tijd (lopen – liep). Een zwak werkwoord krijgt -te of -de achter de stam (werken – werkte).",
      "Sterk: klinker verandert. Zwak: -te/-de."),
]))

# =====================================================================================================
# bouwen
# =====================================================================================================
def schud(v):
    opts = [v["_goed"]] + v["_fout"]
    rng.shuffle(opts)
    out = {k: x for k, x in v.items() if not k.startswith("_")}
    out["opties"] = opts
    out["antwoord"] = opts.index(v["_goed"])
    keys = ["type", "niveau", "vraag", "opties", "antwoord", "uitleg", "hint"]
    return {k: out[k] for k in keys if k in out}


def kaal(s):
    return re.sub(r"<[^>]+>", "", s)


def langste(v):
    L = [len(kaal(o)) for o in v["opties"]]
    return all(i == v["antwoord"] or L[i] < L[v["antwoord"]] for i in range(len(L)))


def kortste(v):
    L = [len(o) for o in v["opties"]]
    return all(i == v["antwoord"] or L[i] > L[v["antwoord"]] for i in range(len(L)))


def ok(vragen):
    m = [v for v in vragen if v["type"] == "mc"]
    if len(m) < 2:
        return True
    s = [v["antwoord"] for v in m]
    if max(s.count(i) for i in set(s)) / len(s) > 0.4:
        return False
    if len(s) < 6:  # kalipkontrol (gate 16) alleen vanaf 6 mc; bij korte lijsten is de cyclustest leeg
        return True
    if any(all(a == s[i - p] for i, a in enumerate(s) if i >= p) for p in (2, 3, 4)):
        return False
    n = max(len(v["opties"]) for v in m)
    if sum(1 for i in range(1, len(s)) if s[i] == (s[i - 1] + 1) % n) / (len(s) - 1) >= 0.5:
        return False
    return True


def bouw(ruw):
    for _ in range(20000):
        vragen = [schud(v) if v["type"] == "mc" else dict(v) for v in ruw]
        if ok(vragen):
            return vragen
    raise SystemExit("geen geldige optievolgorde gevonden")


def schrijf(pad, kop, obj, fn):
    with open(pad, "w", encoding="utf-8") as f:
        f.write(kop + "\n" + fn + "(" + json.dumps(obj, ensure_ascii=False, indent=2) + ");\n")


HFT = {5: "Cursus 5 — Grammatica", 7: "Cursus 7 — Spelling"}
KOP = "/* {soort} conform DURU ENGINE_SPEC (HAVO 3 Nederlands · lesnotities docent) — gegenereerd door tools/gen_nederlands_lesnotities.py */"

alle_vragen = set()
for i, t in enumerate(TOETSEN):
    nr = 53 + i
    assert len(t["vragen"]) == 20, (nr, len(t["vragen"]))
    vragen = bouw(t["vragen"])
    for v in vragen:
        assert v["vraag"] not in alle_vragen, v["vraag"]
        alle_vragen.add(v["vraag"])
        assert v.get("uitleg"), v["vraag"]
        if v["type"] == "open":
            q = kaal(v["vraag"]).lower()
            for s in v["sleutelwoorden"]:
                for w in s.split("/"):
                    assert not (len(w) > 2 and w.lower() in q), (nr, w)
    m = [v for v in vragen if v["type"] == "mc"]
    lang = sum(langste(v) for v in m)
    kort = sum(kortste(v) for v in m)
    wo = [v for v in vragen if v["type"] == "waaronwaar"]
    onw = sum(not v["antwoord"] for v in wo)
    print(f"examen_{nr}: mc {len(m)} (langste {lang}, kortste {kort}), wow {len(wo)} (onwaar {onw}), "
          f"invul {sum(v['type'] == 'invul' for v in vragen)}, open {sum(v['type'] == 'open' for v in vragen)}, "
          f"volgorde {''.join(str(v['antwoord']) for v in m)}")
    if len(m) >= 6:
        assert lang / len(m) <= 0.5, (nr, "langste", lang, len(m))
        assert kort / len(m) <= 0.4, (nr, "kortste", kort, len(m))
    if wo:
        assert onw / len(wo) >= 0.35, (nr, "onwaar")
    if t["par"] == "eind":
        titel = f"Toets {nr} — {t['titel']}"
    elif t["par"] == "mix":
        titel = f"Toets {nr} — {t['titel']}"
    else:
        titel = f"Toets {nr} — {t['titel']}"
    schrijf(os.path.join(ROOT, f"examen_{nr}.js"), KOP.format(soort="Examen"),
            {"id": f"ex-h3-nederlands-{nr}", "hoofdstuk": t["hf"], "hoofdstukTitel": HFT[t["hf"]], "paragraaf": t["par"],
             "titel": titel, "vak": f"Nederlands · HAVO 3 (Cursus {t['hf']})", "icoon": t["icoon"], "duurMin": 20,
             "vragen": vragen}, "DURU.registerExamen")

ONDERWERPEN = [
    ("c7_9.js", "c7-9-werkwoordspelling", "7.9", "§9 Werkwoordspelling: tegenwoordige tijd, verleden tijd, voltooid deelwoord",
     "Stam, d/t/dt, 't kofschip X en het voltooid deelwoord — de basis van alle werkwoordspelling.", "✍️", TH_C7_9, OEF_C7_9),
    ("c7_10.js", "c7-10-engelse-werkwoorden", "7.10", "§10 Engelse werkwoorden",
     "updaten, liken, downloaden: Engelse spelling in de stam, 't kofschip op de klank.", "🇬🇧", TH_C7_10, OEF_C7_10),
    ("c7_11.js", "c7-11-homofone-werkwoordsvormen", "7.11", "§11 Homofone werkwoordsvormen",
     "Gebeurt of gebeurd? Persoonsvorm of voltooid deelwoord — zo kies je goed.", "👂", TH_C7_11, OEF_C7_11),
    ("c7_3_bijvoeglijk.js", "c7-3-bijvoeglijk-naamwoord-e", "7.3", "Bijvoeglijk naamwoord: met of zonder -e?",
     "Een duur horloge, het zachte boek, een houten tafel: wanneer schrijf je een -e of -en?", "🏷️", TH_C7_3B, OEF_C7_3B),
    ("c7_werkwoorden_begrippen.js", "c7-werkwoorden-begrippen", "begrippen", "Begrippen & Kernconcepten — werkwoordspelling (§9–§11)",
     "Stam, persoonsvorm, voltooid deelwoord, sterk/zwak, 't kofschip X en meer.", "📖", TH_BEGR, OEF_BEGR),
]
for fn, oid, par, titel, kort, icoon, th, oef in ONDERWERPEN:
    assert len(th) >= 1500, (fn, len(th))
    assert len(oef) >= 8, (fn, len(oef))
    vragen = bouw(oef)
    for v in vragen:
        assert v["vraag"] not in alle_vragen, v["vraag"]
        alle_vragen.add(v["vraag"])
    schrijf(os.path.join(ROOT, fn), KOP.format(soort="Onderwerp"),
            {"id": oid, "hoofdstuk": 7, "paragraaf": par, "titel": titel, "korteUitleg": kort, "icoon": icoon,
             "theorie": th, "vragen": vragen}, "DURU.register")
    print(f"{fn}: theorie {len(th)} tekens, {len(vragen)} oefenvragen")
