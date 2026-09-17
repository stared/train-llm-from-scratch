# /// script
# requires-python = ">=3.14"
# dependencies = ["tokenizers==0.23.2"]
# ///
"""Inspect text with our saved BPE tokenizer, or train one on UTF-8 text files."""
import argparse
import json
from pathlib import Path
from tokenizers import Tokenizer, models, trainers, pre_tokenizers, decoders

DEFAULT = Path(__file__).resolve().parents[1] / 'datasets/wiki-tokenizer.json'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('files', nargs='*', type=Path, help='UTF-8 .txt files')
    p.add_argument('--text', action='append', default=[], help='Repeat for several texts')
    p.add_argument('--tokenizer', type=Path, default=DEFAULT)
    p.add_argument('--train', type=Path, help='Save a NEW tokenizer here; files are its training corpus')
    p.add_argument('--preview-chars', type=int, default=400, help='Characters to inspect per file; training uses whole files')
    p.add_argument('--vocab-size', type=int, default=8192)
    a = p.parse_args()
    if a.preview_chars < 1:
        p.error('--preview-chars must be positive')
    if a.train:
        if not a.files or a.vocab_size < 257:
            p.error('--train needs text files and --vocab-size >= 257')
        if a.train.exists():
            p.error('Output already exists; choose a new tokenizer filename')
        tok = Tokenizer(models.BPE())
        tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
        tok.decoder = decoders.ByteLevel()
        tok.train([str(f) for f in a.files], trainers.BpeTrainer(
            vocab_size=a.vocab_size, min_frequency=2,
            initial_alphabet=pre_tokenizers.ByteLevel.alphabet(), special_tokens=['<|endoftext|>']))
        a.train.parent.mkdir(parents=True, exist_ok=True)
        tok.save(str(a.train))
        print(f'Saved {a.train}: {tok.get_vocab_size()} vocabulary entries')
    else:
        tok = Tokenizer.from_file(str(a.tokenizer))
    texts = list(a.text)
    if a.files and not a.train and not a.text:
        print(f'File preview: first {a.preview_chars} characters of each file')
        for f in a.files:
            with f.open(encoding='utf-8') as source:
                texts.append(source.read(a.preview_chars))
    for text in texts or ['Ala ma kota. Kot ma komputer.']:
        ids = tok.encode(text).ids
        decoded = tok.decode(ids, skip_special_tokens=False)
        print('Before:', json.dumps(text, ensure_ascii=False))
        print('Pieces:', json.dumps(tok.encode(text).tokens, ensure_ascii=False))
        print('IDs:   ', ids)
        print('Decoded:', json.dumps(decoded, ensure_ascii=False))
        print(f'{len(text)} characters → {len(ids)} tokens; round trip: {decoded == text}')
        # Byte-level pieces can split a Unicode character; decode the full sequence.
        if decoded != text:
            raise ValueError('Tokenizer did not preserve this text')


if __name__ == '__main__':
    main()
