const select=document.getElementById('report'),frame=document.getElementById('report-frame'),notice=document.getElementById('notice');
const titles={
 'workshop-check':'Workshop results',
 'training-comparisons':'Training methods and GPU comparisons',
 'prawko-training':'Driving questions: longer training',
 'pretraining-results':'Polish pretraining',
 'wiki-scratch-results':'Wikipedia pretraining',
 'literature-training':'Literature pretraining',
 'rlvr-results':'RLVR: before and after',
 'rlvr-initial-results':'RLVR: initial experiments',
 'showcase':'Learning a writing style',
 'chlopaki-results':'Dialogue fine-tuning',
 'rejected-gemma':'Gemma: unsuccessful style fine-tuning'
};
let signature='',loading=false,observer;
function show(){
 const requested=location.hash.slice(1),values=[...select.options].map(o=>o.value);
 select.value=values.includes(requested)?requested:values.includes(select.value)?select.value:values[0];
 const src=select.value?'/reports/'+select.value:'';
 frame.hidden=!src;
 if(src&&frame.getAttribute('src')!==src)frame.src=src;
}
async function refresh(){
 if(loading)return;loading=true;
 try{
  const response=await fetch('/api/reports');if(!response.ok)throw Error('Could not load reports. Retrying…');
  const reports=await response.json(),next=JSON.stringify(reports);
  if(next!==signature){
   const selected=select.value;
   reports.sort((a,b)=>Number(b.name==='workshop-check')-Number(a.name==='workshop-check'));
   select.replaceChildren(...reports.map(report=>new Option(titles[report.name]||report.title,report.url.replace('/reports/',''))));
   if([...select.options].some(o=>o.value===selected))select.value=selected;
   signature=next;show();
  }
  notice.hidden=true;
 }catch(error){notice.hidden=false;notice.textContent=error.message}
 finally{loading=false}
}
select.onchange=()=>{location.hash=select.value};window.addEventListener('hashchange',show);
frame.onload=()=>{
 observer?.disconnect();
 const body=frame.contentDocument.body;
 observer=new ResizeObserver(()=>{
  const style=getComputedStyle(body);
  frame.style.height=Math.ceil(body.getBoundingClientRect().height+parseFloat(style.marginTop)+parseFloat(style.marginBottom))+'px';
 });
 observer.observe(body);
};
refresh();setInterval(refresh,3000);
