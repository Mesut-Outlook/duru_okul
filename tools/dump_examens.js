const fs=require('fs'),vm=require('vm'),path=require('path');
const dir=process.argv[3]||'havo3/wiskunde/js/data';const ex={};
const DURU={registerExamen:e=>{ex[e.id]=e},register:()=>{},hoofdstukken:[]};
const ctx=vm.createContext({DURU,window:{DURU},console});
for(const f of fs.readdirSync(dir).filter(f=>f.startsWith('examen_'))){
  try{vm.runInContext(fs.readFileSync(path.join(dir,f),'utf8'),ctx)}catch(e){}
  const last=Object.values(ex).find(e=>!e._f);if(last)last._f=f;
}
fs.writeFileSync(process.argv[2],JSON.stringify(ex));
console.log(Object.keys(ex).length);
