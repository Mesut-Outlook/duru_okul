"""Duru'nun zayıf soru tipleri (bulut kaydı, salt okuma) + çözülmemiş testlerde kaç soru zayıf tipte.
Gebruik: python3 tools/zwakte.py <vak> [--hf=N] [--fouten]
Soru tipi = metin regex'i (RULES, ilk eşleşen kazanır); RULES'ta olmayan vak → tip = §paragraaf (yoksa H<n>).
'leeg' = boş, 'fout' = yanlış. Open sorular hariç. --fouten: kaçırılan soruları metin + Duru'nun cevabıyla döker
(elle sınıflandırma için). Dekking: § başına toets sayısı / gemaakt / son-deneme ort. → hiç denenmemiş § = önce kapsa.
Kabul (TASK-37/38): her hedef testte 'zwak' >= 10 (20 soruluk testte yarısı)."""
import json,re,subprocess,sys,tempfile,urllib.request,collections as C
URL='https://duru-okul-default-rtdb.europe-west1.firebasedatabase.app/scores_v2/duru.json'
RULES={
'wiskunde':([
 ('H2-ctx-cm',  r'hoeveel cm|\(in cm\)'),
 ('H2-ctx-top', r'(sproeier|waterstraal|bal|tunnel|brug|boog|speer|kogel|fontein|dolfijn|vuurpijl|raket|duik).*(hoogste punt|maximaal|top|breed|afstand.*grond|landt|weer op)'),
 ('H2-ctx-start',r'(sproeier|waterstraal|bal|tunnel|brug|boog|speer).*(a = 0|x = 0|t = 0|weggeschoten|vanaf welke hoogte|begint)'),
 ('H2-gooi-sym', r'(basketbal|volleybal|gooit).*(weer|zelfde hoogte)'),
 ('H2-zelfde-y', r'nog een punt (op de parabool )?met y|zelfde hoogte|dezelfde parabool. bereken'),
 ('H2-top-fig',  r'(dal|berg)parabool met top.*welke formule'),
 ('H2-haakjes',  r'zonder haakjes'),
 ('H2-snijx',    r'snijpunt(en)? met de x-as|snijdt de x-as|nulpunt'),
 ('H2-top',      r'top|symmetrieas'),
 ('H2-overig',   r'parabool|x²|a²|t²'),
 ('H1-groeif-tijd', r'groeifactor per (half uur|kwartier|uur|dag|week|maand|jaar|minuut|10)'),
 ('H1-exp-tijdeenh', r'(in maanden|in weken|in dagen).*(jaar|maand|week)'),
 ('H1-exp', r'exponentieel|groeifactor|procent per|% per|·\s*\d+,\d+'),
 ('H1-snijpunt', r'snijpunt|snijden|snijdt'),
 ('H1-rc', r'richtingsco|hellingsgetal'),
 ('H1-formule-lijn', r'welke formule hoort|formule.*(lijn|grafiek)'),
 ('H1-ctx-lin', r'credits|spaart|spaarrekening|euro|€|kosten|tarief'),
 ('PROC', r'procent|korting|btw|%'),
 ('STAT', r'gemiddelde|mediaan|modus|kwartiel|frequentie|steel|cirkeldiagram|spreidingsbreedte|klasse'),
], {'H2-ctx-start','H2-ctx-cm','H2-ctx-top','H2-zelfde-y','H1-exp-tijdeenh','H2-top-fig','H1-snijpunt','H2-haakjes','H1-groeif-tijd','H2-gooi-sym','H1-ctx-lin'}, False),
'nederlands':([
 ('C5-hun-hen',     r'\bhun\b|\bhen\b'),
 ('C5-waar-vz',     r'waar(mee|op|over|naar|in|aan|door|van|bij|uit|voor)\b|\b(naar|over|met|bij|op|aan|van|voor) wie\b'),
 ('C5-zijn-haar',   r'\bzijn\b.*\bhaar\b|\bhaar\b.*\bzijn\b|vrouwelijk|mannelijk|geslacht'),
 ('C5-samentr-soort', r'voorwaarts|achterwaarts|niveau'),
 ('C5-samentr-streepje', r'streepje|\w- en |schrijf korter|correct geschreven'),
 ('C5-samentr-zin', r'samentrek|weggelaten'),
 ('C5-verwijs',     r'verwijs|antecedent|betrekkelijk|\bdie\b.*\bdat\b|\bwat\b'),
 ('C7-n',           r'\b(beiden?|enkelen?|anderen?|meesten?|sommigen?|velen?|weinigen?|tientallen|honderden?|duizenden|ouderen?|jongeren?|zieken?|oudsten?|eersten?|laatsten?|armen|blinden?|werklozen)\b|zelfstandig gebruikt|meervouds-n|met (een )?n\b|zonder n\b'),
 ('C7-bnw-e',       r'-e\b|stoffelijk|bijvoeglijk'),
 ('C7-accent',      r'accent|aigu|grave|circonflexe|cedille|klemtoon|[èéêàç]'),
 ('C7-apostrof',    r"apostrof|'s\b|'tje|meervoud|verkleinwoord|weglatingsteken"),
 ('C7-trema-koppel',r'trema|koppelteken|[ëïü]|samenstelling|\+'),
 ('C7-dt-valkuil',  r'\bwordt?\b|\bvindt?\b|voltooid deelwoord|verleden tijd|gebeur|verhuis|\w(den|ten)\b.*\(\w+en\)|\(\w+en\).*\w(den|ten)\b'),
 ('C7-dt',          r'voltooid deelwoord|verleden tijd|kofschip|persoonsvorm|\bwordt?\b|d of t|\(\w+\)'),
], {'C7-n','C7-bnw-e','C5-samentr-soort','C5-samentr-streepje','C7-apostrof','C5-hun-hen','C7-accent','C5-verwijs','C7-dt-valkuil'}, True),
}
vak=sys.argv[1]; HF=next((int(a[5:]) for a in sys.argv if a.startswith('--hf=')),None)
R,WEAK,met_opties=RULES.get(vak,([],set(),False)); R=[(k,re.compile(p,re.I)) for k,p in R]
def skill(q,e):
  if vak=='nederlands' and e.get('hoofdstuk')==1: return 'C1-lezen'
  t=q['vraag']+(' '+' '.join(map(str,q.get('opties',[]))) if met_opties else '')
  for k,p in R:
    if p.search(t): return k
  return 'overig' if R else par(e)
def par(e): return '§'+str(e['paragraaf']) if e.get('paragraaf') else 'H%s'%e.get('hoofdstuk','?')
if __name__=='__main__':
  d=json.load(urllib.request.urlopen(URL))
  tmp=tempfile.mktemp(suffix='.json');subprocess.run(['node','tools/dump_examens.js',tmp,f'havo3/{vak}/js/data'],check=True,capture_output=True)
  ex=json.load(open(tmp))
  if HF is not None: ex={i:e for i,e in ex.items() if e.get('hoofdstuk')==HF}
  v=[s['val'] for s in d['scores'] if s['key']==f'duru_2627_{vak}_examens_v1'][0];v=json.loads(v) if isinstance(v,str) else v
  st=C.defaultdict(lambda:[0,0,0]);ol=[0,0]
  for a in v['history']:
    e=ex.get(a['examId']);ans=a.get('antwoorden',[])
    if not e: continue
    for i,(q,b) in enumerate(zip(e['vragen'],a['beoordelingen'])):
      leeg=i>=len(ans) or ans[i] in (None,'')
      if q['type']=='open': ol[0]+=1;ol[1]+=leeg;continue
      s=st[skill(q,e)];s[0]+=1
      if b['status']!='goed':
        s[1+leeg]+=1
        if '--fouten' in sys.argv: print('%s #%d [%s] %s | Duru: %s | goed: %s'%(e['_f'],i+1,'LEEG' if leeg else 'FOUT',q['vraag'][:110],'' if leeg else str(ans[i])[:40],str(q.get('antwoord'))[:40]))
  if not R: WEAK={k for k,(n,f,l) in st.items() if n>=10 and (f+l)/n>=0.3}  # generiek: § met ≥30% mis = zwak
  print('%-20s %5s %5s %5s %5s'%('tip','n','fout','leeg','%mis'))
  for k,(n,f,l) in sorted(st.items(),key=lambda x:-(x[1][1]+x[1][2])/x[1][0]):
    print('%-20s %5d %5d %5d %4d%%  %s'%(k,n,f,l,100*(f+l)/n,'ZWAK' if k in WEAK else ''))
  print('open vragen: %d, leeg %d'%tuple(ol))
  solved=set(a['examId'] for a in v['history'])
  ts=lambda a:int(str(a.get('attemptId','0')).split('_')[-1] or 0)
  last={a['examId']:a for a in sorted(v['history'],key=ts)}  # history = nieuwste eerst → sorteer op attemptId-ms, laatste wint
  dk=C.defaultdict(lambda:[0,0,[]])
  for i,e in ex.items():
    d_=dk[par(e)];d_[0]+=1
    if i in last: a=last[i];d_[1]+=1;d_[2].append(100*sum(b['status']=='goed' for b in a['beoordelingen'])/max(1,len(a['beoordelingen'])))
  print('\ndekking (§: toetsen / gemaakt / ort. laatste %):')
  for k,(n,g,ps) in sorted(dk.items()):
    print('  %-8s %3d / %3d  %s%s'%(k,n,g,('%3.0f%%'%(sum(ps)/len(ps))) if ps else '  - ','  ← NOG NIET GEOEFEND' if not g else ''))
  print('\nniet gemaakt:')
  for i,e in sorted(ex.items(),key=lambda x:x[1]['_f']):
    if i in solved or (vak=='wiskunde' and HF is None and e.get('hoofdstuk')!=2): continue
    sk=[skill(q,e) for q in e['vragen']]
    print('  %-14s §%-5s zwak %2d/%d  %s'%(e['_f'],e.get('paragraaf'),sum(s in WEAK for s in sk),len(sk),dict(C.Counter(sk))))
