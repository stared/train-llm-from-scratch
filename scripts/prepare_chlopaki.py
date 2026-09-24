"""Prepare the user-supplied datasets/chlopaki.md, preserving dialogue provenance."""
import hashlib
import json
from pathlib import Path
import re
from dialogue_pairs import convert

SOURCE=Path('datasets/chlopaki.md')
OUT=Path('datasets/chlopaki-bidirectional-v1')


def prepare():
    raw=SOURCE.read_bytes();text=raw.decode('utf-8-sig')
    scenes=[];turns=[];audit=[];headings=[];aliases={}
    # Explicitly reviewed unlabelled stage directions in the supplied edition.
    stage_lines={368,375,472}
    for number,rawline in enumerate(text.splitlines()+[''],1):
        line=rawline.strip()
        if not line:
            if turns:scenes.append(turns)
            turns=[];aliases={}
            continue
        if (':' in line and not line.partition(':')[2].strip()) or (not turns and ':' not in line):
            if turns:scenes.append(turns)
            turns=[];aliases={}
            headings.append({'line':number,'text':line});continue
        if line.startswith('<') or re.fullmatch(r'[.\s]+',line) or number in stage_lines:
            audit.append({'line':number,'kind':'stage_direction','text':line});continue
        # Three source turns use a period in place of the speaker colon.
        line=re.sub(r'^(F|Si|Sz)\.\s+',r'\1: ',line)
        speaker,sep,utterance=line.partition(':')
        # This is dialogue containing a colon, not a character name.
        if speaker.startswith('Powiem ci teraz'):
            sep=''
        if not sep:
            if not turns:raise ValueError(f'Unassigned text at line {number}')
            turns[-1]['text']+='\n'+line
            turns[-1]['source_lines'].append(number)
            audit.append({'line':number,'kind':'continuation_of_previous_speaker','speaker':turns[-1]['speaker']})
            continue
        speaker=speaker.strip().rstrip('.');utterance=utterance.strip()
        if not utterance:raise ValueError(f'Empty turn at line {number}')
        # Resolve short labels using the most recently introduced matching
        # name within this scene. Retain unresolved labels rather than guessing.
        canonical=aliases.get(speaker.casefold(),speaker)
        if len(speaker)>3:
            aliases[speaker[:1].casefold()]=speaker
            aliases[speaker[:2].casefold()]=speaker
        if turns and turns[-1]['speaker']==canonical:
            turns[-1]['text']+='\n'+utterance;turns[-1]['source_lines'].append(number)
        else:turns.append({'speaker':canonical,'text':utterance,'source_lines':[number]})
    # User requested all exchanges: train on all usable scenes. Evaluate new
    # ordinary questions, not a random quotation split or reversed duplicates.
    result=convert(scenes,validation_fraction=0)
    OUT.mkdir(parents=True,exist_ok=False)
    for name,data in [('scenes.json',scenes),('parsing_audit.json',audit),('headings.json',headings),
                      ('unpaired_scenes.json',[s for s in scenes if len(s)<2])]:
        (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2), encoding='utf-8', newline='\n')
    for split,rows in result.items():
        (OUT/f'{split}.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows), encoding='utf-8', newline='\n')
    manifest={'style':'wit','languages':'pl','examples':len(result['train']),
              'source':str(SOURCE),'source_sha256':hashlib.sha256(raw).hexdigest(),
              'data_sha256':hashlib.sha256((OUT/'train.jsonl').read_bytes()).hexdigest(),
              'teacher':{'id':'user-supplied datasets/chlopaki.md', 'revision':hashlib.sha256(raw).hexdigest()},
              'scenes':len(scenes),'turns':sum(map(len,scenes)),
              'unpaired_scenes':sum(len(s)<2 for s in scenes),'validation_examples':0,
              'recipe':'All usable adjacent dialogue pairs, both forward and reverse, deduplicated. No authored comic examples mixed in. Scene headings/stage directions excluded; unlabelled continuations attached to previous speaker; source mistakes retained.',
              'evaluation':'New ordinary Polish questions. No film-quotation holdout; all usable exchanges requested for training.'}
    (OUT/'dataset.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2), encoding='utf-8', newline='\n')
    prompts=['Dlaczego mój komputer znowu się zawiesił?',
             'Kolega pożyczył ode mnie pieniądze i nie oddaje. Co mu powiedzieć?',
             'Nie wiem, co chcę robić w życiu. Od czego zacząć?',
             'Szef chce, żebym pracował w sobotę. Jak mu odmówić?',
             'Kupiłem drogi sweter, a wszyscy się ze mnie śmieją. Co robić?',
             'Dlaczego warto robić kopie zapasowe?']
    (OUT/'evaluation.json').write_text(json.dumps([{'id':f'new-pl-{i}','language':'pl','prompt':p} for i,p in enumerate(prompts)],ensure_ascii=False,indent=2), encoding='utf-8', newline='\n')
    print(json.dumps(manifest,ensure_ascii=False,indent=2))


if __name__=='__main__':prepare()
