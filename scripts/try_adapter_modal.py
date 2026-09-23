"""Try one new input with a saved workshop adapter; no training or weight writes."""
import json
from pathlib import Path
import re

import modal

app = modal.App('workshop-try-adapter')
volume = modal.Volume.from_name('model-training-workshop')
image = (modal.Image.debian_slim(python_version='3.14')
         .pip_install_from_requirements('scripts/requirements.txt')
         .env({'HF_HOME': '/persist/hf', 'TOKENIZERS_PARALLELISM': 'false'})
         .add_local_file('scripts/prawko.py', '/work/scripts/prawko.py')
         .add_local_file('scripts/rlvr_tasks.py', '/work/scripts/rlvr_tasks.py'))


def prepare_input(run, task, question, a, b, c, word_one, word_two):
    if not re.fullmatch(r'[A-Za-z0-9_-]+', run):
        raise ValueError('Use the run folder name only, without runs/ or any slashes.')
    if task == 'exam':
        if not all(value.strip() for value in (question, a, b, c)):
            raise ValueError('Supply --question and all three options: --a, --b, --c.')
        if word_one or word_two:
            raise ValueError('Word options are only for --task six_words.')
        if sum(map(len, (question, a, b, c))) > 4000:
            raise ValueError('Use a shorter question and options (at most 4000 characters total).')
        from prawko import question as format_question
        prompt, _ = format_question(dict(question=question, options=[a, b, c], answer=0))
        return prompt, []
    if task == 'six_words':
        if question or a or b or c:
            raise ValueError('Question and answer options are only for --task exam.')
        words = [word_one.lower(), word_two.lower()]
        if any(not re.fullmatch(r'[a-z]{1,30}', w) for w in words) or words[0] == words[1]:
            raise ValueError('Supply two different English words using letters only.')
        prompt = (f'Write a tiny story in exactly SIX English words. Include the exact words '
                  f'"{words[0]}" and "{words[1]}". Use each word only once. '
                  'Return only the story, on one line, with no title or explanation. '
                  'Words are sequences of letters; punctuation does not count.')
        return prompt, words
    raise ValueError('Choose --task exam or --task six_words.')


@app.function(image=image, gpu='L4', cpu=2, memory=16384, timeout=600,
              retries=0, max_containers=1, volumes={'/persist': volume})
def predict(run, task, prompt, words):
    import sys
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForImageTextToText, GenerationConfig
    from peft import PeftModel

    sys.path.insert(0, '/work/scripts')
    folder = Path('/persist/runs') / run
    if not (folder / 'adapter/adapter_config.json').is_file():
        raise ValueError(f'No saved adapter in {run}. Use the name printed by your completed training run.')
    result = json.loads((folder / 'result.json').read_text())
    valid = (result.get('method') == 'sft' if task == 'exam'
             else result.get('task') == 'six_words')
    if not valid:
        raise ValueError('This run does not match the requested task. Choose the matching chapter’s run.')
    spec = json.loads((folder / 'model_spec.json').read_text())
    tokenizer = AutoTokenizer.from_pretrained(folder / 'tokenizer')
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    text = tokenizer.apply_chat_template([{'role': 'user', 'content': prompt}],
                                        tokenize=False, add_generation_prompt=True, enable_thinking=False)
    inputs = tokenizer(text, add_special_tokens=False, return_tensors='pt').to('cuda')
    if inputs.input_ids.shape[1] > 768:
        raise ValueError('Input is too long. Shorten your question and options to fit 768 tokens.')
    cls = AutoModelForImageTextToText if spec['multimodal'] else AutoModelForCausalLM
    base = cls.from_pretrained(spec['id'], revision=spec['revision'], dtype=torch.bfloat16,
                               attn_implementation='sdpa').to('cuda')
    model = PeftModel.from_pretrained(base, folder / 'adapter', is_trainable=False)
    model.eval()
    with torch.inference_mode():
        if task == 'exam':
            ids = [tokenizer.encode(letter, add_special_tokens=False) for letter in 'ABC']
            if any(len(value) != 1 for value in ids):
                raise ValueError('This tokenizer does not have single-token A/B/C labels.')
            logits = model(**inputs, use_cache=False, logits_to_keep=1).logits[0, -1].float()
            probabilities = logits[[value[0] for value in ids]].softmax(-1).tolist()
            return dict(answer='ABC'[max(range(3), key=probabilities.__getitem__)],
                        probabilities=dict(zip('ABC', probabilities)))
        config = GenerationConfig(max_new_tokens=40, do_sample=False,
                                  pad_token_id=tokenizer.pad_token_id, eos_token_id=tokenizer.eos_token_id)
        output = model.generate(**inputs, generation_config=config)
        story = tokenizer.decode(output[0, inputs.input_ids.shape[1]:], skip_special_tokens=True)
        from rlvr_tasks import check
        return dict(story=story, **check('six_words', {'anchors': words}, story))


@app.local_entrypoint()
def main(run: str, task: str, question: str = '', a: str = '', b: str = '', c: str = '',
         word_one: str = '', word_two: str = ''):
    prompt, words = prepare_input(run, task, question, a, b, c, word_one, word_two)
    print('Loading your saved adapter on one L4. This incurs inference compute charges; no training runs.', flush=True)
    answer = predict.remote(run, task, prompt, words)
    if task == 'exam':
        print('Answer:', answer['answer'])
        print('Probabilities among A/B/C:', ', '.join(f'{k}: {v:.1%}' for k, v in answer['probabilities'].items()))
    else:
        print('Story:', answer['story'])
        print(f"{'Pass' if answer['success'] else 'Fail'}; {answer['word_count']} words; reward {answer['reward']:.2f}")
