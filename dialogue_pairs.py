"""Convert a supplied local dialogue file into bidirectional user/assistant pairs.

Input: Speaker: utterance, one turn per line; blank lines separate scenes.
This script does not download source material.
"""
import argparse
import hashlib
import json
from pathlib import Path
import random


def parse(text):
    scenes, turns = [], []
    for number, raw in enumerate(text.splitlines()+[''], 1):
        line = raw.strip()
        if not line:
            if turns:
                scenes.append(turns)
                turns = []
            continue
        speaker, sep, utterance = line.partition(':')
        speaker, utterance = speaker.strip(), utterance.strip()
        if not sep or not speaker or not utterance:
            raise ValueError(f'Line {number}: expected Speaker: utterance')
        if turns and turns[-1]['speaker'] == speaker:
            turns[-1]['text'] += '\n'+utterance
        else:
            turns.append({'speaker': speaker, 'text': utterance})
    return scenes


def key(text):
    return ' '.join(text.casefold().split())


def convert(scenes, validation_fraction=.1, seed=42, language='pl'):
    if not 0<=validation_fraction<1:
        raise ValueError('Validation fraction must be in [0, 1)')
    scenes = [scene for scene in scenes if len(scene)>=2]
    # Group whole scenes BEFORE adding reversed pairs. Also connect scenes that
    # share a line: the same quotation must not appear on both sides of a split.
    parents=list(range(len(scenes)))
    def root(i):
        while parents[i]!=i:
            parents[i]=parents[parents[i]];i=parents[i]
        return i
    owners={}
    for i,scene in enumerate(scenes):
        for turn in scene:
            k=key(turn['text'])
            if k in owners:parents[root(i)]=root(owners[k])
            else:owners[k]=i
    groups=sorted({root(i) for i in range(len(scenes))})
    random.Random(seed).shuffle(groups)
    count=(min(len(groups)-1,max(1,round(len(groups)*validation_fraction)))
           if validation_fraction and len(groups)>1 else 0)
    validation=set(groups[:count]);result={'train':[],'validation':[]};seen=set()
    for i,scene in enumerate(scenes):
        split='validation' if root(i) in validation else 'train'
        for j,(left,right) in enumerate(zip(scene,scene[1:])):
            if key(left['text'])==key(right['text']):continue
            for direction,user,assistant in [('forward',left,right),('reverse',right,left)]:
                pair=(key(user['text']),key(assistant['text']))
                if pair in seen:continue
                seen.add(pair)
                result[split].append({'id':f'scene-{i}-pair-{j}-{direction}',
                    'scene_id':i,'split_group':root(i),'direction':direction,'language':language,
                    'user_speaker':user['speaker'],'assistant_speaker':assistant['speaker'],
                    'prompt':user['text'],'answer':assistant['text'],
                    'messages':[{'role':'user','content':user['text']},
                                {'role':'assistant','content':assistant['text']}]})
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input',type=Path)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--source',required=True,help='Provenance description or URL; recorded, not fetched')
    p.add_argument('--language',choices=['pl','en'],default='pl')
    p.add_argument('--validation-fraction',type=float,default=.1)
    a=p.parse_args()
    raw=a.input.read_bytes()
    scenes=parse(raw.decode('utf-8-sig'))
    result=convert(scenes,a.validation_fraction,language=a.language)
    if not result['train']:p.error('No usable dialogue pairs')
    a.output.mkdir(parents=True,exist_ok=False)
    for split,rows in result.items():
        payload=''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows)
        (a.output/f'{split}.jsonl').write_text(payload)
    manifest={'style':'wit','languages':a.language,'examples':len(result['train']),
              'validation_examples':len(result['validation']),'source':a.source,
              'source_sha256':hashlib.sha256(raw).hexdigest(),
              'data_sha256':hashlib.sha256((a.output/'train.jsonl').read_bytes()).hexdigest(),
              'teacher':{'id':'user-supplied dialogue','revision':hashlib.sha256(raw).hexdigest()},
              'recipe':'Adjacent cross-speaker pairs in both directions; consecutive same-speaker turns merged; speaker names kept as metadata; deduplicated; scenes connected by shared lines assigned wholly to one split.',
              'caveat':'Reverse pairs are reconstruction examples, not necessarily natural replies. A single connected scene group cannot provide a separate validation split.'}
    (a.output/'dataset.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print(f"Saved {len(result['train'])} train and {len(result['validation'])} validation examples to {a.output}")
    if len(result['train'])<24:
        print('The workshop trainer requires at least 24 training examples; this file is a data-conversion preview.')


if __name__=='__main__':main()
