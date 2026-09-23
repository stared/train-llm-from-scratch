import {displayPiece,probabilityColor} from '/prediction.js';
export function setupLivePrediction(root){
 const $=id=>root.querySelector('#'+id);
 let tokens=[],result=null,version=0,timer;
 async function predict(){
  clearTimeout(timer);
  const turn=++version;result=null;$('live-next').disabled=true;$('live-candidates').replaceChildren();
  if(!$('live-input').value.trim()){$('live-status').textContent='';return}
  $('live-status').textContent='Predicting…';
  try{
   const response=await fetch('/api/prediction',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({model:$('live-model').value,text:$('live-input').value,tokens,temperature:+$('live-temperature').value})});
   const data=await response.json();if(turn!==version)return;if(!response.ok)throw Error(data.error);
   result=data;$('live-status').textContent='';$('live-output').textContent=data.continuation;
   $('live-candidates').replaceChildren(...data.candidates.map(t=>{
    const button=document.createElement('button');button.className='live-candidate';button.title=`Token ID: ${t.id}\nLog probability: ${Math.log(t.probability).toFixed(3)}`;
    const piece=document.createElement('code');piece.textContent=displayPiece(t.piece);
    const track=document.createElement('span');track.className='candidate-track';const bar=document.createElement('span');bar.style.width=t.probability*100+'%';bar.style.background=probabilityColor(t.probability);track.append(bar);
    const value=document.createElement('span');value.textContent=(t.probability*100).toFixed(2)+'%';button.append(piece,track,value);button.onclick=()=>append(t.id);return button;
   }));$('live-next').disabled=tokens.length>=256;
  }catch(error){if(turn===version)$('live-status').textContent=error.message}
 }
 function append(id){if(tokens.length>=256)return;tokens.push(id);predict()}
 $('live-next').onclick=()=>{if(result)append(result.sampled)};
 $('live-input').oninput=()=>{tokens=[];result=null;++version;$('live-output').textContent='';$('live-candidates').replaceChildren();$('live-next').disabled=true;clearTimeout(timer);timer=setTimeout(predict,250)};
 $('live-prompts').replaceChildren(...['Był piękny','Była ciemna','Nie wiem, czy','Otworzył drzwi i','Warszawa jest','Warsztaty z trenowania modelu sztucznej inteligencji'].map(text=>{
  const button=document.createElement('button');button.type='button';button.textContent=text;button.disabled=true;
  button.onclick=()=>{$('live-input').value=text;$('live-input').oninput();$('live-input').focus()};return button;
 }));
 $('live-temperature').oninput=()=>{result=null;++version;$('live-next').disabled=true;$('live-temperature-value').textContent=(+$('live-temperature').value).toFixed(1);clearTimeout(timer);timer=setTimeout(predict,100)};
 $('live-model').onchange=()=>{tokens=[];$('live-output').textContent='';predict()};
 $('live-reset').onclick=()=>{tokens=[];$('live-output').textContent='';predict()};
 let started=false;
 return async()=>{
  if(started)return;started=true;
  try{const response=await fetch('/api/prediction/models');if(!response.ok)throw Error('Could not load local models.');const models=await response.json();
   if(!models.length){$('live-status').textContent='No local model weights. Train a model and save its checkpoint to explore new prompts.';return}
   $('live-model').replaceChildren(...models.map(m=>new Option(m.label,m.id)));$('live-input').disabled=false;$('live-prompts').querySelectorAll('button').forEach(button=>button.disabled=false);await predict();
  }catch(e){$('live-status').textContent=e.message;started=false}
 };
}
