const fs=require('fs'),path=require('path');
const vakken=['geschiedenis','natuurkunde','scheikunde','wiskunde','economie','biologie','aardrijkskunde','maatschappijleer','nederlands','engels','frans','duits'];
let n=0,bad=[];
for(const v of vakken){
  const d=`havo3/${v}/js/data`; if(!fs.existsSync(d))continue;
  const O=[],E=[];let cur='';const src=new Map();
  const DURU={hoofdstukken:[],onderwerpen:[],examens:[],register:o=>{O.push(o);src.set(o,cur)},registerExamen:e=>{E.push(e);src.set(e,cur)}};
  global.DURU=DURU;global.window={DURU};
  for(const f of fs.readdirSync(d).filter(f=>f.endsWith('.js'))){cur=f;try{new Function('DURU','window',fs.readFileSync(path.join(d,f),'utf8'))(DURU,global.window)}catch(e){}}
  [...O,...E].forEach(x=>(x.vragen||[]).forEach((q,i)=>{
    if(q.type!=='open')return; n++;
    const tag=`${v} · ${x.id}#${i+1}`;
    const sw=q.sleutelwoorden||[];
    if(q.minTreffers>sw.length) bad.push(`${tag}: minTreffers ${q.minTreffers} > ${sw.length} sleutelwoord — ASLA tam dogru olamaz`);
    sw.forEach(s=>{
      const alts=String(s).split('/').map(a=>a.trim());
      const kortste=alts.reduce((a,b)=>a.length<=b.length?a:b);
      if(/^(voordeel|nadeel|stap|punt|antwoord)\s*:/i.test(alts[0])) bad.push(`${tag}: "${alts[0]}" onekli — ogrenci boyle yazmaz`);
      else if(kortste.split(/\s+/).length>5) bad.push(`${tag}: en kisa alternatif ${kortste.split(/\s+/).length} kelime ("${kortste.slice(0,55)}…")`);
    });
  }));
}
console.log(`${n} open soru tarandi`);
bad.length?bad.forEach(b=>console.log('  ✗ '+b)):console.log('  ✓ sorun yok');
