/* Kabul kapisi — node gate.js <slug> [--only h2,h3]
   Sozlesme + icerik kalite kurallarini tek seferde dener. */
const fs=require('fs'),path=require('path');
const ROOT = process.env.DURU_ROOT || require('path').resolve(__dirname, '..');
const slug=process.argv[2];
const onlyArg=(process.argv.find(a=>a.startsWith('--only='))||'').split('=')[1];
const only=onlyArg?onlyArg.split(','):null;
const base=path.join(ROOT,'havo3',slug);
const html=fs.readFileSync(path.join(base,'index.html'),'utf8');
const refs=[...html.matchAll(/<script src="(js\/data\/[^"?]+)/g)].map(m=>m[1]);
const O=[],E=[];const src=new Map();
const DURU={hoofdstukken:[],onderwerpen:[],examens:[],
  register:o=>{O.push(o);src.set(o,cur)},registerExamen:e=>{E.push(e);src.set(e,cur)}};
global.DURU=DURU;global.window={DURU};
let cur='';
const files=fs.existsSync(path.join(base,'js/data'))?fs.readdirSync(path.join(base,'js/data')).filter(f=>f.endsWith('.js')):[];
for(const f of files){cur=f;try{new Function('DURU','window',fs.readFileSync(path.join(base,'js/data',f),'utf8'))(DURU,global.window);}
  catch(e){console.log(`  X ${f} calismadi: ${e.message}`)}}

const SJABLON_OPT=/De historische ontwikkeling van|Het begrip verbonden aan/i;
const SJABLON=/hoofdonderwerp van|historisch begrip staat centraal|beoordelen historici|In welk tijdvak \(1900-1950|bronnen in Geschiedeniswerkplaats|Het begrip verbonden aan/i;
const norm=s=>String(s||'').toLowerCase().replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
let fails=0,passes=0;
const check=(naam,bad,detail)=>{
  if(bad.length){fails++;console.log(`  ✗ ${naam}: ${bad.length} ihlal`);bad.slice(0,6).forEach(b=>console.log('      · '+b));if(bad.length>6)console.log(`      … +${bad.length-6}`);}
  else{passes++;console.log(`  ✓ ${naam}${detail?' — '+detail:''}`)}};

const inScope=x=>!only||only.some(h=>String(src.get(x)||'').startsWith(h+'_')||(x.hoofdstuk&&('h'+x.hoofdstuk)===h));
const OO=O.filter(inScope),EE=E.filter(inScope);
const alle=[];OO.forEach(o=>(o.vragen||[]).forEach((v,i)=>alle.push({owner:o.id,file:src.get(o),n:i+1,v,exam:false})));
EE.forEach(e=>(e.vragen||[]).forEach((v,i)=>alle.push({owner:e.id,file:src.get(e),n:i+1,v,exam:true})));

console.log(`\n=== KABUL KAPISI · ${slug}${only?' ('+only.join(',')+')':''} ===`);
console.log(`  onderwerp ${OO.length} · proeftoets ${EE.length} · toplam ${alle.length} vraag\n`);

check('1. Sablon soru yok', alle.filter(a=>SJABLON.test(a.v.vraag)||(a.v.opties||[]).some(o=>SJABLON.test(o)||SJABLON_OPT.test(o))).map(a=>`${a.owner}#${a.n}: ${a.v.vraag.slice(0,70)}`));

const byT={};alle.forEach(a=>{const k=norm(a.v.vraag);if(k)(byT[k]=byT[k]||[]).push(a)});
check('2. Tekrar eden soru yok', Object.values(byT).filter(v=>v.length>1).map(v=>`${v.length}x "${v[0].v.vraag.slice(0,60)}" (${v.map(x=>x.owner+'#'+x.n).join(', ')})`));

const bias=[];[...OO,...EE].forEach(x=>{const mc=(x.vragen||[]).filter(v=>v.type==='mc');if(mc.length<4)return;
  const p={};mc.forEach(v=>p[v.antwoord]=(p[v.antwoord]||0)+1);
  const max=Math.max(...Object.values(p));
  if(max/mc.length>0.4)bias.push(`${x.id}: ${max}/${mc.length} ayni sikta (%${(100*max/mc.length).toFixed(0)}) → ${JSON.stringify(p)}`)});
const mcAll=alle.filter(a=>a.v.type==='mc');const pAll={};mcAll.forEach(a=>pAll[a.v.antwoord]=(pAll[a.v.antwoord]||0)+1);
check('3. mc cevap dagilimi dengeli (dosya basi ≤%40)', bias, `genel ${JSON.stringify(pAll)}`);

const wow=alle.filter(a=>a.v.type==='waaronwaar');const wf=wow.filter(a=>a.v.antwoord===false).length;
check('4. waaronwaar ≥%35 onwaar', wow.length&&wf/wow.length<0.35?[`${wf}/${wow.length} onwaar (%${(100*wf/wow.length).toFixed(0)})`]:[], `${wf}/${wow.length} onwaar`);

check('5a. Sinavda invoer yok', alle.filter(a=>a.exam&&a.v.type==='invoer').map(a=>`${a.owner}#${a.n}`));
check('5b. Oefende invul/open yok', alle.filter(a=>!a.exam&&['invul','open'].includes(a.v.type)).map(a=>`${a.owner}#${a.n} (${a.v.type})`));
check('6. Soru metninde numara oneki yok', alle.filter(a=>/^\s*\d+\.\s/.test(a.v.vraag)).map(a=>`${a.owner}#${a.n}: ${a.v.vraag.slice(0,50)}`));
check('7. Her soruda uitleg var', alle.filter(a=>norm(a.v.uitleg).length<15).map(a=>`${a.owner}#${a.n}`));

const yapi=[];alle.forEach(a=>{const v=a.v,tag=`${a.owner}#${a.n}`;
  if(v.type==='mc'){if(!Array.isArray(v.opties)||v.opties.length<2)yapi.push(tag+': opties eksik');
    else{if(!Number.isInteger(v.antwoord)||v.antwoord<0||v.antwoord>=v.opties.length)yapi.push(tag+': antwoord index gecersiz');
      const s=v.opties.map(x=>String(x).replace(/<[^>]+>/g,'').toLowerCase().trim());
      if(new Set(s).size!==s.length)yapi.push(tag+': ayni sik iki kez')}}
  else if(v.type==='waaronwaar'){if(typeof v.antwoord!=='boolean')yapi.push(tag+': antwoord boolean degil')}
  else if(v.type==='invoer'||v.type==='invul'){if(typeof v.antwoord!=='string'||!v.antwoord.trim())yapi.push(tag+': antwoord string degil')}
  else if(v.type==='open'){if(!Array.isArray(v.sleutelwoorden)||!v.sleutelwoorden.length)yapi.push(tag+': sleutelwoorden yok');
    if(!Number.isInteger(v.minTreffers)||v.minTreffers<1)yapi.push(tag+': minTreffers gecersiz');
    else if(Array.isArray(v.sleutelwoorden)&&v.minTreffers>v.sleutelwoorden.length)yapi.push(tag+': minTreffers > sleutelwoorden');
    (v.sleutelwoorden||[]).forEach(s=>{const w=norm(String(s).split('/')[0]);if(w.length>4&&norm(v.vraag).includes(w))yapi.push(tag+`: sleutelwoord "${s}" soruda geciyor`)})}
  else yapi.push(tag+`: bilinmeyen type '${v.type}'`)});
check('8. Soru yapisi sozlesmeye uygun', yapi);

check('9. Soru sayilari (onderwerp 8 / proeftoets 20)',
  [...OO.filter(o=>(o.vragen||[]).length!==8).map(o=>`${o.id}: ${(o.vragen||[]).length} vraag`),
   ...EE.filter(e=>(e.vragen||[]).length!==20).map(e=>`${e.id}: ${(e.vragen||[]).length} vraag`)]);
check('10. theorie ≥1500 karakter', OO.filter(o=>String(o.theorie||'').length<1500).map(o=>`${o.id}: ${String(o.theorie||'').length}b`));
check('11. index.html bagli', files.filter(f=>!refs.includes('js/data/'+f)).map(f=>'bagli degil: '+f));

console.log(`\n  SONUC: ${passes} gecti, ${fails} kaldi`);
process.exit(fails?1:0);
