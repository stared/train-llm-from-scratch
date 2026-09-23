export function candidates(token){
 const values=new Map((token.alternatives||[]).map(t=>[t.id,t]));
 values.set(token.id,{id:token.id,piece:token.piece,probability:token.probability});
 return [...values.values()].sort((a,b)=>b.probability-a.probability);
}
export function probabilityColor(p){
 const t=Math.min(1,Math.max(0,-Math.log10(Math.max(p,1e-4))/4));
 const blue=[151,194,229],white=[247,247,247],red=[238,153,151];
 const [a,b,u]=t<.5?[blue,white,t*2]:[white,red,(t-.5)*2];
 return `rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*u)).join(',')})`;
}
export function tokenCharacters(tokens){
 const bytes=tokens.flatMap(t=>t.bytes||[]),owners=tokens.flatMap((t,i)=>(t.bytes||[]).map(()=>i)),result=[];
 for(let i=0;i<bytes.length;){
  const b=bytes[i],wanted=b<128?1:b>=194&&b<=223?2:b>=224&&b<=239?3:b>=240&&b<=244?4:1;
  let n=1;
  while(n<wanted&&i+n<bytes.length){
   const c=bytes[i+n];
   if(c<128||c>191||(n===1&&((b===224&&c<160)||(b===237&&c>159)||(b===240&&c<144)||(b===244&&c>143))))break;
   n++;
  }
  result.push({text:new TextDecoder().decode(Uint8Array.from(bytes.slice(i,i+n))),ids:owners.slice(i,i+n)});i+=n;
 }
 return result;
}
// Byte-level BPE stores bytes as printable surrogate characters.
const byteAlphabet=[...Array(256).keys()].filter(b=>(b>=33&&b<=126)||(b>=161&&b<=172)||b>=174);
const byteMap=new Map(byteAlphabet.map(b=>[String.fromCodePoint(b),b]));
let extra=256;
for(let b=0;b<256;b++)if(!byteAlphabet.includes(b))byteMap.set(String.fromCodePoint(extra++),b);
export function displayPiece(piece){
 if(piece.startsWith('<'))return piece;
 const chars=[...piece];
 if(chars.some(c=>!byteMap.has(c)))return piece;
 const bytes=chars.map(c=>byteMap.get(c));
 try{return new TextDecoder('utf-8',{fatal:true}).decode(Uint8Array.from(bytes)).replaceAll('\n','↵').replaceAll('\t','⇥')}
 catch{return bytes.map(b=>'0x'+b.toString(16).padStart(2,'0')).join(' ')}
}
export function createPredictionExplorer(root){
 const $=id=>root.querySelector('#'+id);
 let token=null,anchor=null,hideTimer;
 const close=()=>{clearTimeout(hideTimer);root.hidden=true;document.querySelectorAll('.selected-token').forEach(e=>e.classList.remove('selected-token'))};
 function position(){
  if(root.hidden||!anchor)return;
  const box=anchor.getBoundingClientRect(),width=Math.min(340,innerWidth-24);
  root.style.width=width+'px';root.style.left=Math.max(12,Math.min(innerWidth-width-12,box.left))+'px';
  root.style.top=Math.max(12,Math.min(innerHeight-root.offsetHeight-12,box.bottom+10))+'px';
 }
 function render(){
  const values=candidates(token),probs=values.map(v=>v.probability);
  $('prediction-token').textContent=displayPiece(token.piece);
  $('prediction-detail').replaceChildren(...[['Token ID',token.id],['Probability',(token.probability*100).toFixed(2)+'%'],['Log probability',Math.log(token.probability).toFixed(2)]].map(([label,value])=>{const line=document.createElement('div');const name=document.createElement('span');name.textContent=label;const number=document.createElement('span');number.textContent=value;line.append(name,number);return line}));
  $('prediction-candidates').replaceChildren(...values.map((t,i)=>{
   const line=document.createElement('div');line.className='candidate'+(t.id===token.id?' chosen-candidate':'');
   line.title=`Token ID: ${t.id}\nLog probability: ${Math.log(t.probability).toFixed(3)}`;
   const piece=document.createElement('code');piece.textContent=displayPiece(t.piece);
   const track=document.createElement('span');track.className='candidate-track';
   const bar=document.createElement('span');bar.style.width=(probs[i]*100)+'%';track.append(bar);
   const value=document.createElement('span');value.textContent=(probs[i]*100).toFixed(2)+'%';
   line.append(piece,track,value);return line;
  }));
  position();
 }
 $('prediction-close').onclick=close;
 root.onmouseenter=()=>clearTimeout(hideTimer);root.onmouseleave=()=>{hideTimer=setTimeout(close,150)};
 document.addEventListener('pointerdown',e=>{if(!root.contains(e.target)&&!e.target.closest('.token'))close()});
 document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});
 window.addEventListener('resize',close);window.addEventListener('scroll',position,true);
 return {
  set(){close()},
  leave(){hideTimer=setTimeout(close,150)},
  inspect(row,index,element){close();token=row.tokens[index];anchor=element;root.hidden=false;
   for(const part of element.parentElement.children)if(part.dataset.owners?.split(',').includes(String(index)))part.classList.add('selected-token');
   render();
  }
 };
}
