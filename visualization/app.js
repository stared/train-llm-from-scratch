const $=id=>document.getElementById(id);
const sections={tokens:['Tokenization','The same text, split into pieces. Explore how byte-pair encoding builds tokens.'],pretrain:['Pretraining','From random weights to text continuation. Compare the same prompts as training progresses.'],sft:['Supervised fine-tuning','Learn from a question and its correct answer. Watch how the answer probabilities change.'],rlvr:['Reinforcement learning with verifiable rewards','Sample answers, check them, then learn from the rewards.']};
let stage='tokens',run=null,items=[],checkpoint=0,example=0,request=0,lastSignature='',chosen=new Map();
const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const number=x=>Number.isInteger(x)?x.toLocaleString():Number(x).toFixed(3);
const pct=x=>(x*100).toFixed(x<.01?2:1)+'%';
function notice(message=''){$('notice').textContent=message;$('notice').hidden=!message;}
async function get(url){const r=await fetch(url);if(!r.ok)throw Error('The run is not ready. Waiting for its next update.');return r.json();}
function options(el,values,value){el.replaceChildren(...values.map(([id,label])=>new Option(label,id)));if(values.some(v=>String(v[0])===String(value)))el.value=value;}
async function route(){stage=location.hash.slice(1);if(!sections[stage])stage='tokens';request++;run=null;lastSignature='';notice();
 $('title').textContent=sections[stage][0];$('intro').textContent=sections[stage][1];document.title=sections[stage][0]+' · AI from scratch';
 document.querySelectorAll('nav a').forEach(a=>{if(a.hash==='#'+stage)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
 $('tokens').hidden=stage!=='tokens';$('training').hidden=true;$('run-control').hidden=stage==='tokens';
 if(stage!=='tokens')await refresh(true);
}
async function refresh(first=false){if(stage==='tokens')return;const version=++request,wasStage=stage;
 try{const catalog=await get('/api/runs');if(version!==request||stage!==wasStage)return;items=catalog.filter(r=>r.stage===stage);
  const active=items.find(r=>r.status==='Running');const id=chosen.get(stage)||active?.id||'example-'+stage;
  options($('run'),items.map(r=>[r.id,r.label==='Saved example'?`Saved example — ${r.model}`:`${r.status} — ${r.model} · ${r.id.split('-').at(-1).slice(-6)}`]),id);
  const selected=$('run').value;if(active&&!chosen.has(stage))chosen.set(stage,selected);if(!selected){notice('No recorded runs for this section yet.');return;}
  const data=await get('/api/run?id='+encodeURIComponent(selected));if(version!==request)return;
  const signature=JSON.stringify(data);if(signature===lastSignature&&!first)return;
  const follow=!run||checkpoint===run.snapshots.length-1;const same=run?.id===data.id;
  run=data;lastSignature=signature;checkpoint=same&&!follow?Math.min(checkpoint,data.snapshots.length-1):data.snapshots.length-1;
  if(!same)example=0;notice();render();if(!same)$('training-data').open=true;
 }catch(e){if(version===request)notice(e.message);}
}
function render(){ $('training').hidden=false;
 const score=run.score;const parts=[`<strong>${esc(run.model)}</strong>`,`<span class="status">${esc(run.status)}</span>`,esc(run.source)];
 if(score)parts.push(`${esc(score.label)}: <strong>${number(score.before)}${score.n?'/'+score.n:''} → ${number(score.after)}${score.n?'/'+score.n:''}</strong>`);
 if(run.cost!=null)parts.push(`Worker cost $${run.cost.toFixed(2)}`);
 if(run.seconds!=null)parts.push(`${(run.seconds/60).toFixed(1)} min ${run.status==='Completed'?'training':'elapsed'}`);
 $('metadata').innerHTML=parts.map(x=>`<span>${x}</span>`).join('');
 $('training-data').hidden=!run.training?.length;if(run.training?.length){const row=run.training[0];$('data-example').innerHTML=`<div class="training-pair"><div><span class="caption">Input · training set</span><pre>${esc(row.prompt)}</pre></div><div><span class="caption">${stage==='sft'?'Target answer':'Feedback'}</span><pre>${esc(row.target)}</pre></div></div>`;}
 options($('metric'),run.curves.map((s,i)=>[i,s.name]),$('metric').value);$('metric').parentElement.hidden=run.curves.length<2;
 $('checkpoint').max=Math.max(0,run.snapshots.length-1);$('checkpoint').value=Math.max(0,checkpoint);
 const rows=run.snapshots[0]?.rows||[];options($('example'),rows.map((r,i)=>[i,(i+1)+'. '+(r.question||r.prompt||r.id).slice(0,52)]),example);
 $('rollouts').hidden=!run.rollouts?.length;
 if(run.rollouts?.length){options($('rollout'),run.rollouts.map((r,i)=>[i,'Update '+r.step]),$('rollout').value);renderRollout();}
 $('provenance').textContent=`Recorded run: ${run.id}. ${run.status==='Completed'?'The selected checkpoint uses development results; the test score is reported separately.':'Updates arrive from your training terminal. Keep it connected for live previews.'}`;
 renderCheckpoint();
}
function renderCurve(){const s=run.curves[+$('metric').value];if(!s?.points.length){$('curve').innerHTML='<p class="small">Loading the model and evaluating its starting point. The first metric will appear here.</p>';return;}
 const pts=s.points.filter(p=>p.every(Number.isFinite));if(!pts.length)return;
 const W=Math.max(300,$('curve').clientWidth),H=innerWidth<700?200:230,L=46,R=24,T=14,B=34;const maxX=Math.max(1,...pts.map(p=>p[0]),...run.snapshots.map(s=>s.step));let minY=Math.min(...pts.map(p=>p[1])),maxY=Math.max(...pts.map(p=>p[1]));
 if(/accuracy|success|reward/i.test(s.name)){minY=0;maxY=Math.max(1,maxY);}else{const pad=Math.max(.1,(maxY-minY)*.08);minY=Math.max(0,minY-pad);maxY+=pad;}
 const x=v=>L+v/maxX*(W-L-R),y=v=>H-B-(v-minY)/(maxY-minY)*(H-T-B);
 let svg=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(s.name)} over training updates"><title>${esc(s.name)}; horizontal axis: training updates</title>`;
 const ticks=W<500?3:5;for(let i=0;i<ticks;i++){const v=minY+(maxY-minY)*i/(ticks-1);svg+=`<path class="grid" d="M${L} ${y(v)}H${W-R}"/><text x="${L-9}" y="${y(v)+4}" text-anchor="end">${v.toFixed(2)}</text>`;const u=maxX*i/(ticks-1);svg+=`<text x="${x(u)}" y="${H-12}" text-anchor="middle">${Math.round(u).toLocaleString()}</text>`;}
 svg+=`<polyline class="line" points="${pts.map(p=>`${x(p[0])},${y(p[1])}`).join(' ')}"/>`;
 for(const p of pts.length<100?pts:[])svg+=`<circle cx="${x(p[0])}" cy="${y(p[1])}" r="3" fill="#236c70"><title>Update ${p[0]}: ${p[1].toFixed(4)}</title></circle>`;
 const snap=run.snapshots[checkpoint];if(snap)svg+=`<path class="cursor" d="M${x(snap.step)} ${T}V${H-B}"/>`;
 svg+='</svg><p class="small">Training updates</p>';$('curve').innerHTML=svg;
 $('curve').querySelector('svg').onclick=e=>{if(!run.snapshots.length)return;const box=e.currentTarget.getBoundingClientRect();const update=((e.clientX-box.left)/box.width*W-L)/(W-L-R)*maxX;checkpoint=run.snapshots.reduce((best,r,i)=>Math.abs(r.step-update)<Math.abs(run.snapshots[best].step-update)?i:best,0);renderCheckpoint();};
}
function renderCheckpoint(){const snap=run.snapshots[checkpoint],base=run.snapshots[0];$('checkpoint').value=Math.max(0,checkpoint);$('checkpoint').disabled=!snap;$('previous').disabled=checkpoint<=0;$('next').disabled=checkpoint>=run.snapshots.length-1;
 $('checkpoint-label').textContent=snap?`${snap.label} (${checkpoint+1}/${run.snapshots.length})`:'Waiting for a checkpoint';renderCurve();
 if(!snap){$('prompt').textContent='Examples appear after baseline evaluation.';$('before').replaceChildren();$('after').replaceChildren();$('answer-key').textContent='';$('probabilities').disabled=true;return;}
 example=Math.min(example,base.rows.length-1);const a=base.rows[example];const b=snap.rows.find(r=>a.id!=null?r.id===a.id:r.prompt===a.prompt)||a;
 $('prompt').textContent=a.question?a.question+'\n'+a.options.map((v,i)=>'ABC'[i]+'. '+v).join('\n'):a.prompt;
 $('answer-key').textContent=a.answer?'Correct answer: '+a.answer:'';
 $('split-note').textContent=snap.split==='fixed prompts'?'Fixed continuation prompts; the prompt is not an instruction.':'Development examples, separate from training. The same inputs are shown at every checkpoint.';
 $('after-label').textContent=snap.label;
 const traces=!!(a.tokens?.length||b.tokens?.length);$('probabilities').disabled=!traces;$('probabilities').parentElement.hidden=!traces;$('probability-legend').hidden=!traces;$('probability-note').textContent=run.exam?'Probabilities are normalized over A/B/C only.':traces?'':'Token probabilities were not recorded for this run.';
 output($('before'),a);output($('after'),b);
}
function output(el,row){el.replaceChildren();if(row.probabilities){const pred=row.prediction;el.innerHTML=`<div class="prob-bars">${row.probabilities.map((p,i)=>`<div class="prob-row ${'ABC'[i]===row.answer?'correct':''}"><strong>${'ABC'[i]}</strong><div class="bar-track"><div class="bar-fill" style="width:${Math.max(0,Math.min(100,p*100))}%"></div></div><span>${pct(p)}</span></div>`).join('')}</div><p class="output-note">Prediction: ${esc(pred)}${pred===row.answer?' · correct':' · incorrect'}${row.unconstrained_ABC_mass!=null?`<br>Total full-vocabulary probability of A/B/C: ${pct(row.unconstrained_ABC_mass)}`:''}</p>`;return;}
 const pre=document.createElement('pre');const text=row.continuation??row.text??'';
 if(row.tokens?.length){let offset=0;const all=row.tokens.flatMap(t=>t.bytes||[]);const decoded=new TextDecoder().decode(Uint8Array.from(all));
  // Byte-level tokens can split a Unicode character. Paint characters without changing the text.
  if(decoded===text){const owners=[];row.tokens.forEach((t,i)=>(t.bytes||[]).forEach(()=>owners.push(i)));for(const char of text){const n=new TextEncoder().encode(char).length;const ids=owners.slice(offset,offset+n);const span=document.createElement('span');span.textContent=char;span.className='token';span.dataset.owners=ids.join(',');span.tabIndex=offset===0||owners[offset-1]!==ids[0]?0:-1;span.setAttribute('aria-describedby','tooltip');const paint=p=>{const t=Math.max(0,Math.min(1,Math.sqrt(p)));return `hsl(${28+130*t} ${65-30*t}% ${91-4*t}%)`;};if($('probabilities').checked){const colors=ids.map(i=>paint(row.tokens[i].probability));span.style.background=colors.every(c=>c===colors[0])?colors[0]:`linear-gradient(to right,${colors.map((c,i)=>`${c} ${i/n*100}% ${(i+1)/n*100}%`).join(',')})`;}
    const show=()=>{hideTooltip();for(const part of pre.children)if(part.dataset.owners.split(',').some(i=>ids.includes(+i)))part.classList.add('active-token');tooltip(span,ids.map(i=>row.tokens[i]).filter((t,i,a)=>a.indexOf(t)===i));};span.onmouseenter=show;span.onfocus=show;span.onmouseleave=hideTooltip;span.onblur=hideTooltip;pre.append(span);offset+=n;}
  }else pre.textContent=text;
 }else pre.textContent=text;el.append(pre);
 if(row.reward!=null){const p=document.createElement('p');p.className='output-note';p.textContent=`Reward ${row.reward.toFixed(2)} · ${row.success?'passes':'does not pass'}${row.word_count!=null?' · '+row.word_count+' words':''}`;el.append(p);}
}
function tooltip(span,tokens){const t=tokens[0];$('tooltip').innerHTML=`<strong>${esc(t.piece)} · token ${t.id}</strong><p>Model probability: ${pct(t.probability)}</p>${t.sampling_probability!=null?`<p>After sampling filters: ${pct(t.sampling_probability)}</p>`:''}<table><thead><tr><th>Alternative</th><th>Probability</th></tr></thead><tbody>${(t.alternatives||[]).map(a=>`<tr><td>${esc(a.piece)}</td><td>${pct(a.probability)}</td></tr>`).join('')}</tbody></table>${tokens.length>1?'<p>This character spans more than one byte token.</p>':''}`;$('tooltip').hidden=false;const r=span.getBoundingClientRect();$('tooltip').style.left=Math.max(8,Math.min(innerWidth-290,r.left))+'px';$('tooltip').style.top=Math.max(8,Math.min(innerHeight-$('tooltip').offsetHeight-8,r.bottom+8))+'px';}
function hideTooltip(){$('tooltip').hidden=true;document.querySelectorAll('.active-token').forEach(e=>e.classList.remove('active-token'));}
function renderRollout(){const r=run.rollouts[+$('rollout').value];if(!r)return;$('rollout-prompt').textContent=r.prompt;$('rollout-table').innerHTML=`<table><thead><tr><th>Sampled answer</th><th>Reward</th><th>Relative reward</th><th>Check</th></tr></thead><tbody>${r.rows.map(v=>`<tr><td>${esc(v.text)}</td><td>${Number(v.reward).toFixed(2)}</td><td>${v.advantage>=0?'+':''}${Number(v.advantage).toFixed(2)}</td><td class="${v.success?'pass':'fail'}">${v.word_count!=null?v.word_count+' words; ':''}${v.success==null?'':v.success?'passes':'fails'}</td></tr>`).join('')}</tbody></table>`;}
$('run').onchange=()=>{chosen.set(stage,$('run').value);lastSignature='';refresh(true);};$('metric').onchange=renderCurve;$('example').onchange=()=>{example=+$('example').value;renderCheckpoint();};$('checkpoint').oninput=()=>{checkpoint=+$('checkpoint').value;renderCheckpoint();};$('previous').onclick=()=>{checkpoint--;renderCheckpoint();};$('next').onclick=()=>{checkpoint++;renderCheckpoint();};$('probabilities').onchange=renderCheckpoint;$('rollout').onchange=renderRollout;
window.addEventListener('hashchange',route);window.addEventListener('scroll',hideTooltip,true);window.addEventListener('keydown',e=>{if(e.key==='Escape')hideTooltip();});
const frame=document.querySelector('iframe');frame.onload=()=>{const doc=frame.contentDocument;new ResizeObserver(()=>{frame.style.height=doc.documentElement.scrollHeight+'px';}).observe(doc.body);};
window.addEventListener('resize',()=>{hideTooltip();if(run&&stage!=='tokens')renderCurve();});
route();setInterval(()=>refresh(),3000);
