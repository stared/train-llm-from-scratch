const response=await fetch('/api/tokenizer');
if(!response.ok)throw Error('Could not load the workshop tokenizer.');
const source=await response.json();
// ByteLevel BPE maps each byte to a printable Unicode character.
const bytes=[...Array.from({length:94},(_,i)=>i+33),...Array.from({length:12},(_,i)=>i+161),...Array.from({length:82},(_,i)=>i+174)];
const byteAlphabet=Object.fromEntries(bytes.map(b=>[b,String.fromCharCode(b)]));
let extra=256;
for(let b=0;b<256;b++)if(!(b in byteAlphabet))byteAlphabet[b]=String.fromCharCode(extra++);
const D={vocabulary:source.model.vocab,merges:source.model.merges,byteAlphabet,examples:[{"text": "Warszawa jest stolicą Polski i miastem położonym nad Wisłą. Jej historia obejmuje zarówno okresy rozwoju, jak i zniszczenia oraz odbudowę. Na ulicach spotykają się różne epoki: obok starych kamienic stoją współczesne biurowce, a tramwaje przejeżdżają między parkami, placami i osiedlami.\n\nW encyklopedii opis miasta dzieli się na części poświęcone geografii, historii, kulturze i transportowi. Każda z nich zawiera nazwy, daty oraz odsyłacze do innych artykułów. Ten sam tekst można podzielić na pojedyncze bajty lub większe fragmenty, których tokenizer nauczył się na polskiej Wikipedii."}, {"text": "'''Warszawa''' – stolica [[Polska|Polski]], położona nad [[Wisła|Wisłą]]. Jest ośrodkiem administracyjnym, naukowym i kulturalnym. Artykuł zawiera odsyłacze do innych haseł oraz informacje uporządkowane w sekcjach.\n\n== Historia ==\nHistoria miasta wiąże się z rozwojem osadnictwa, zmianami politycznymi i odbudową po zniszczeniach wojennych. Dodatkowe informacje można znaleźć w artykule [[Historia Warszawy]].\n\n{{Infobox\n | nazwa = Warszawa\n | państwo = Polska\n}}\n[[Kategoria:Miasta w Polsce]]"}, {"text": "Łódź, łódka i łódki mają podobne litery, ale nie muszą mieć identycznych tokenów. Żółw powoli przechodzi przez ścieżkę, a gęś przygląda mu się z brzegu jeziora. W zdaniu pojawiają się polskie znaki: ą, ć, ę, ł, ń, ó, ś, ź oraz ż. Każdy z nich zajmuje więcej niż jeden bajt w kodowaniu UTF-8.\n\nHello, world! Cześć, świecie! Ten akapit miesza polski z angielskim, liczbami 2026 i 12345 oraz symbolami: [[link]], {{szablon}} i 🦆. Kolory pokazują podział tekstu, ale sam tekst pozostaje dokładnie w tym samym miejscu."}]};
const $=id=>document.getElementById(id),encoder=new TextEncoder();
const palette=['#cde7fa','#fbe1be','#ded6f5','#cfead4','#f5cfdb','#f3edbd'];
let characters=[],byteOwners=[],byteColors=[],ownText='',revision=0;
const isStandard=()=>['cl100k_base','o200k_base'].includes(activeTokenizer);

let vocabulary=D.vocabulary,ranks=new Map(D.merges.map((pair,i)=>[JSON.stringify(pair),i])),current=null,activeTokenizer='workshop';
const reverse=new Map(Object.entries(D.byteAlphabet).map(([byte,char])=>[char,+byte]));
const workshop={vocabulary:D.vocabulary,ranks};
function token(raw){
 const bytes=Uint8Array.from([...raw].map(c=>reverse.get(c)));
 let label;
 try{label=new TextDecoder('utf-8',{fatal:true}).decode(bytes).replaceAll(' ','·').replaceAll('\n','↵').replaceAll('\t','⇥')}
 catch{label=[...bytes].map(b=>b.toString(16).padStart(2,'0').toUpperCase()).join(' ')}
 return {raw,label,hex:[...bytes].map(b=>b.toString(16).padStart(2,'0')).join(' '),id:vocabulary[raw]};
}
function trace(text){
 if(text.length>2000)throw Error('Use up to 2,000 characters.');
 if(text.includes('<|endoftext|>'))throw Error('Please use ordinary text without the reserved end-of-text token.');
 // ByteLevel's GPT-2 pre-tokenizer, followed by the saved tokenizer's merge ranks.
 const pattern=/'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+/gu;
 const groups=[...text.matchAll(pattern)].map(m=>[...encoder.encode(m[0])].map(b=>D.byteAlphabet[b]));
 const initial=groups.map(g=>g.map(token)),steps=[];
 while(true){
  let best=null;
  groups.forEach((g,gi)=>{for(let i=0;i<g.length-1;i++){
   const rank=ranks.get(JSON.stringify([g[i],g[i+1]]));
   if(rank!==undefined&&(!best||rank<best.rank))best={rank,gi,i};
  }});
  if(!best)break;
  const {rank,gi,i}=best,[a,b]=groups[gi].slice(i,i+2);
  groups[gi].splice(i,2,a+b);
  steps.push({rank:rank+1,group:gi,index:i,left:token(a),right:token(b),merged:token(a+b)});
 }
 return {text,initial,steps,ids:groups.flat().map(s=>vocabulary[s])};
}

function render(){
 $('hover').hidden=true;
 const e=current,n=+$('step').value,groups=e.initial.map(g=>g.slice());
 for(const s of e.steps.slice(0,n)){const children=groups[s.group].slice(s.index,s.index+2);groups[s.group].splice(s.index,2,{...s.merged,children,rank:s.rank})}
 const colors=[];byteOwners=[];let start=0;
 for(const t of groups.flat()){
  const length=t.hex.split(' ').length;let index=start%palette.length;
  if(palette[index]===colors[colors.length-1])index=(index+1)%palette.length;
  const color=palette[index];
  for(let b=0;b<length;b++){colors.push(color);byteOwners.push(t)}
  start+=length;
 }
 byteColors=colors;paint();
 $('count').textContent=`${groups.flat().length.toLocaleString()} tokens`;
 $('step').setAttribute('aria-valuetext',`${n} of ${e.steps.length} merges applied`);
}

function paint(selected=null){
 for(const c of characters){
  const bands=byteColors.slice(c.offset,c.offset+c.length).map((color,i)=>selected&&byteOwners[c.offset+i]===selected?'#f4b544':color);
  c.span.style.background=bands.every(x=>x===bands[0])?bands[0]:`linear-gradient(to right, ${bands.map((color,i)=>`${color} ${100*i/bands.length}% ${100*(i+1)/bands.length}%`).join(', ')})`;
 }
}
function clearHover(){$('hover').hidden=true;paint()}
const escapeHTML=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function treeSVG(root){
 const nodes=[],edges=[];let leaf=0,maxDepth=0;
 function visit(t,depth){
  const node={t,depth,x:0};nodes.push(node);maxDepth=Math.max(maxDepth,depth);
  if(t.children){const children=t.children.map(child=>visit(child,depth+1));node.x=(children[0].x+children[1].x)/2;children.forEach(child=>edges.push([node,child]))}
  else node.x=leaf++;
  return node;
 }
 visit(root,0);const width=Math.max(180,leaf*70),height=(maxDepth+1)*64+12;
 const x=node=>leaf===1?width/2:35+node.x*70,y=node=>28+node.depth*64;
 return `<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="Token merge history">`+
 edges.map(([a,b])=>`<path d="M${x(a)},${y(a)+14} L${x(b)},${y(b)-16}" stroke="#b9c4d0" fill="none"/>`).join('')+
 nodes.map(node=>`<g><rect x="${x(node)-31}" y="${y(node)-16}" width="62" height="30" rx="4" fill="${node.t.children?'#e3edf8':'#f2f2f2'}"/><text x="${x(node)}" y="${y(node)+3}" text-anchor="middle" font-family="monospace" font-size="12">${escapeHTML(node.t.label)}</text><text x="${x(node)}" y="${y(node)+27}" text-anchor="middle" font-family="system-ui" font-size="10" fill="#666">${node.t.rank?'step '+node.t.rank:'byte'}</text></g>`).join('')+'</svg>';
}
function inspect(character,event){
 const bounds=character.span.getBoundingClientRect();
 const fraction=Math.max(0,Math.min(.999,(event.clientX-bounds.left)/Math.max(1,bounds.width)));
 const token=byteOwners[character.offset+Math.floor(fraction*character.length)];
 paint(token);
 const box=$('hover');
 box.innerHTML=`<strong>${escapeHTML(token.label)}</strong><p>Token ID: ${token.id}</p>`+(current.standard?'':treeSVG(token));
 box.hidden=false;
 const rect=box.getBoundingClientRect();
 box.style.left=Math.max(12,Math.min(event.clientX+16,window.innerWidth-rect.width-12))+'px';
 box.style.top=Math.max(12,event.clientY+20+rect.height<window.innerHeight?event.clientY+20:event.clientY-rect.height-16)+'px';
}

function choose(){
 const e=current;$('text').replaceChildren();characters=[];let offset=0;
 for(const c of e.text){const span=document.createElement('span');span.textContent=c;$('text').append(span);const length=encoder.encode(c).length;const character={span,offset,length};characters.push(character);span.onmousemove=event=>inspect(character,event);span.onmouseleave=clearHover;offset+=length}
 $('step').max=e.steps.length;$('step').value=e.steps.length;render();
}
D.examples.forEach((e,i)=>{const option=document.createElement('option');option.value=i;option.textContent=['Polish paragraphs','Wikipedia markup','Polish letters & mixed text'][i]||`Custom paragraph ${i-2}`;$('example').append(option)});
function editorText(){return $('text').textContent===''?'':$('text').innerText}
function caretOffset(){
 const selection=window.getSelection();
 if(!selection.rangeCount||!$('text').contains(selection.focusNode))return 0;
 const range=document.createRange();range.selectNodeContents($('text'));range.setEnd(selection.focusNode,selection.focusOffset);return range.toString().length;
}
function restoreCaret(caret){
 const selection=window.getSelection(),walker=document.createTreeWalker($('text'),NodeFilter.SHOW_TEXT);let node;
 while(node=walker.nextNode()){
  if(caret<=node.length){selection.collapse(node,caret);return}caret-=node.length;
 }
 selection.selectAllChildren($('text'));selection.collapseToEnd();
}
async function applyText(text,caret=null){
 const turn=++revision;
 try{
  if(isStandard()){
   $('count').textContent='Tokenizing…';
   const response=await fetch('/api/tokenize',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({tokenizer:activeTokenizer,text})});
   const result=await response.json();if(turn!==revision)return;
   if(!response.ok)throw Error(result.error);current=result;
  }else current=trace(text);
  $('error').textContent='';choose();
  document.querySelector('.controls').hidden=!!current.standard;
  if(caret!==null&&document.activeElement===$('text'))restoreCaret(caret);
 }catch(error){if(turn===revision){$('error').textContent=error.message;$('count').textContent=''}}
}
function updateText(){
 ownText=editorText();$('example').value='custom';applyText(ownText,caretOffset());
}
const customText=new Option('Your text','custom');$('example').append(customText);
const undo=[],redo=[];
function historyMove(from,to){
 if(!from.length)return;
 to.push({text:editorText(),caret:caretOffset()});const state=from.pop();
 $('text').textContent=state.text;ownText=state.text;$('example').value='custom';applyText(state.text,state.caret);
}
$('text').addEventListener('beforeinput',event=>{
 if(event.inputType==='historyUndo'||event.inputType==='historyRedo'){
  event.preventDefault();historyMove(event.inputType==='historyUndo'?undo:redo,event.inputType==='historyUndo'?redo:undo);return;
 }
 if(!event.isComposing){undo.push({text:editorText(),caret:caretOffset()});if(undo.length>100)undo.shift();redo.length=0}
});
$('text').addEventListener('keydown',event=>{
 if((event.metaKey||event.ctrlKey)&&!event.altKey&&event.key.toLowerCase()==='z'){
  event.preventDefault();historyMove(event.shiftKey?redo:undo,event.shiftKey?undo:redo);
 }
});
$('text').addEventListener('input',event=>{if(!event.isComposing)updateText()});
$('text').addEventListener('compositionend',updateText);
$('example').onchange=()=>{
 undo.length=0;redo.length=0;
 applyText($('example').value==='custom'?ownText:D.examples[+$('example').value].text);
};
function selectTokenizer(value){
 vocabulary=value.vocabulary;ranks=value.ranks;applyText(editorText());
}
$('tokenizer').onchange=()=>{
 const selected=$('tokenizer').value;
 if(selected==='custom'){$('tokenizer').value=activeTokenizer;$('tokenizer-file').click();return}
 activeTokenizer=selected;
 if(isStandard()){applyText(editorText());return}
 selectTokenizer(selected==='workshop'?workshop:$('tokenizer').selectedOptions[0].tokenizer);
};
$('tokenizer-file').onchange=async()=>{
 const file=$('tokenizer-file').files[0];if(!file)return;
 try{
  const data=JSON.parse(await file.text()),m=data.model,p=data.pre_tokenizer;
  if(m?.type!=='BPE'||p?.type!=='ByteLevel'||p.add_prefix_space||p.use_regex===false||data.normalizer||m.dropout||m.byte_fallback||m.ignore_merges||m.continuing_subword_prefix||m.end_of_word_suffix)
   throw Error('Choose a byte-level BPE tokenizer with no normalization or prefix space, like the workshop tokenizer.');
  if(!Object.values(D.byteAlphabet).every(c=>Number.isInteger(m.vocab[c])))throw Error('The tokenizer must include all 256 bytes.');
  const merges=m.merges.map(pair=>Array.isArray(pair)?pair:pair.split(' '));
  if(!merges.every(pair=>pair.length===2&&pair.every(t=>Number.isInteger(m.vocab[t]))&&Number.isInteger(m.vocab[pair.join('')])))throw Error('Invalid BPE merge vocabulary.');
  const value={vocabulary:m.vocab,ranks:new Map(merges.map((pair,i)=>[JSON.stringify(pair),i]))};
  activeTokenizer='uploaded';selectTokenizer(value);
  let option=$('tokenizer').querySelector('[data-upload]');
  if(!option){option=new Option('','uploaded');option.dataset.upload='true';$('tokenizer').insertBefore(option,$('tokenizer').lastElementChild)}
  option.textContent=file.name.replace(/\.json$/,'')+' ('+Object.keys(m.vocab).length.toLocaleString()+' tokens)';option.tokenizer=value;
  activeTokenizer='uploaded';$('tokenizer').value=activeTokenizer;
 }catch(error){$('error').textContent=error.message}
 $('tokenizer-file').value='';
};
$('step').oninput=render;current=trace(D.examples[0].text);choose();
