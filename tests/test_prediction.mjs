import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {candidates,tokenCharacters,displayPiece} from '../visualization/prediction.js';

test('recorded token is included once, even outside the top candidates',()=>{
 const token={id:4,piece:'x',probability:.01,alternatives:[{id:2,piece:'y',probability:.3}]};
 assert.deepEqual(candidates(token).map(t=>t.id),[2,4]);
 token.alternatives.push({...token,alternatives:undefined});
 assert.equal(candidates(token).length,2);
});

test('byte ownership survives split Polish characters and malformed UTF-8',()=>{
 const parts=tokenCharacters([{bytes:[197]},{bytes:[130,255,226,130]},{bytes:[65]}]);
 assert.equal(parts.map(c=>c.text).join(''),'ł��A');
 assert.deepEqual(parts[0].ids,[0,1]);
 assert.deepEqual(parts.at(-1).ids,[2]);
});

test('all recorded traces retain their exact text and token ownership',()=>{
 const runs=JSON.parse(readFileSync(new URL('../visualization/examples.json',import.meta.url)));
 let checked=0;
 for(const run of runs)for(const snapshot of run.snapshots)for(const row of snapshot.rows){
  if(!row.tokens?.length)continue;
  const parts=tokenCharacters(row.tokens);
  assert.equal(parts.map(c=>c.text).join(''),row.continuation??row.text);
  assert.equal(parts.flatMap(c=>c.ids).length,row.tokens.flatMap(t=>t.bytes).length);
  checked++;
 }
 assert.ok(checked>=6);
});

test('candidate labels decode BPE byte encoding without mojibake',()=>{
 assert.equal(displayPiece('Ġczy'),' czy');
 assert.equal(displayPiece('Äħ'),'ą');
 assert.equal(displayPiece('Ċ'),'↵');
 assert.equal(displayPiece('Å'),'0xc5');
});
