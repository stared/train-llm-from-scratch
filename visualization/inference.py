"""Next-token inference using local scratch-model checkpoints."""
import json
from pathlib import Path
import sys
import threading

ROOT = Path(__file__).resolve().parents[1]
_lock = threading.Lock()
_loaded = None


def models():
    found = []
    for folder in sorted((ROOT / 'runs').glob('scratch-*')):
        if folder.is_symlink() or not all((folder / name).is_file() for name in ('best.pt', 'result.json', 'tokenizer.json')):
            continue
        result = json.loads((folder / 'result.json').read_text())
        if 'config' not in result:
            continue
        corpus = 'Wolne Lektury' if folder.name.startswith('scratch-wl-') else 'Wikipedia'
        found.append({'id': folder.name, 'label': f"{corpus}, {result['model']}", 'config': result['config']})
    found.sort(key=lambda r: (not r['id'].startswith('scratch-wl-30m-'), not r['id'].startswith('scratch-wl-'), r['id']))
    # One checkpoint per corpus/model combination keeps the selector useful.
    unique = {}
    for item in found:
        unique.setdefault(item['label'], item)
    return list(unique.values())[:5]


def predict(request):
    global _loaded
    import torch
    from tokenizers import Tokenizer
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from scripts.scratch_model import Config, ScratchGPT

    available = {item['id']: item for item in models()}
    name = request.get('model')
    text = request.get('text')
    suffix = request.get('tokens', [])
    temperature = request.get('temperature', 1)
    if name not in available:
        raise ValueError('Choose a local model.')
    if not isinstance(text, str) or not text.strip() or len(text) > 2000:
        raise ValueError('Enter between 1 and 2,000 characters.')
    if not isinstance(temperature, (int, float)) or not 0 <= temperature <= 2:
        raise ValueError('Temperature must be between 0 and 2.')
    config = available[name]['config']
    if not isinstance(suffix, list) or len(suffix) > 256 or any(type(i) is not int or not 0 <= i < config['vocab_size'] for i in suffix):
        raise ValueError('Generated text is limited to 256 tokens. Start again from the input.')
    with _lock:
        if _loaded is None or _loaded[0] != name:
            torch.set_num_threads(4)
            folder = ROOT / 'runs' / name
            model = ScratchGPT(Config(**config))
            model.load_state_dict(torch.load(folder / 'best.pt', map_location='cpu', weights_only=True))
            model.eval()
            tokenizer = Tokenizer.from_file(str(folder / 'tokenizer.json'))
            _loaded = name, model, tokenizer
        _, model, tokenizer = _loaded
        ids = tokenizer.encode(text).ids + suffix
        if not ids:
            raise ValueError('Enter some text.')
        with torch.inference_mode():
            logits = model(torch.tensor([ids[-config['context']:]]))[0]
            base = logits.softmax(-1)
            if temperature == 0:
                probabilities = torch.zeros_like(base)
                probabilities[logits.argmax()] = 1
            else:
                probabilities = (logits / temperature).softmax(-1)
            top = logits.topk(5).indices.tolist()
            sampled = torch.multinomial(probabilities, 1).item()
        return {
            'candidates': [{'id': i, 'piece': tokenizer.id_to_token(i), 'probability': probabilities[i].item(),
                            'model_probability': base[i].item()} for i in top],
            'sampled': sampled,
            'continuation': tokenizer.decode(suffix, skip_special_tokens=False),
        }
