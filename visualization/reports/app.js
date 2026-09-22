const select=document.getElementById('report'),frame=document.getElementById('report-frame');
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
try{
 const response=await fetch('/api/reports');if(!response.ok)throw Error('Could not load reports.');
 const reports=await response.json();
 reports.sort((a,b)=>(a.name==='workshop-check'?-1:b.name==='workshop-check'?1:0));
 for(const report of reports)select.add(new Option(titles[report.name]||report.title,report.url.replace('/reports/','')));
 function show(){
  const requested=location.hash.slice(1);
  select.value=[...select.options].some(o=>o.value===requested)?requested:select.options[0]?.value;
  if(select.value)frame.src='/reports/'+select.value;
 }
 select.onchange=()=>{location.hash=select.value};window.addEventListener('hashchange',show);
 let observer;
 frame.onload=()=>{
  observer?.disconnect();
  observer=new ResizeObserver(()=>{frame.style.height=frame.contentDocument.documentElement.scrollHeight+'px'});
  observer.observe(frame.contentDocument.body);
 };
 show();
}catch(error){const notice=document.getElementById('notice');notice.hidden=false;notice.textContent=error.message}
