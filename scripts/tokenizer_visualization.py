# /// script
# requires-python = ">=3.14"
# dependencies = ["tokenizers==0.23.2"]
# ///
"""Show the same text with changing boundaries from our real BPE tokenizer."""
import argparse
import hashlib
import json
from pathlib import Path
from tokenizers import Tokenizer

ROOT = Path(__file__).resolve().parents[1]


def build(source, output, extra):
    raw = source.read_bytes()
    model = json.loads(raw)['model']
    tok = Tokenizer.from_file(str(source))
    merges = model['merges']
    ranks = {tuple(pair): i for i, pair in enumerate(merges)}
    # GPT-2 ByteLevel's reversible byte-to-Unicode alphabet.
    bs = list(range(33, 127)) + list(range(161, 173)) + list(range(174, 256))
    cs = bs.copy()
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + len(cs) - 188)
    reverse = dict(zip(map(chr, cs), bs))
    def token(s):
        data = bytes(reverse[c] for c in s)
        try:
            label = data.decode('utf-8').replace(' ', '·').replace('\n', '↵').replace('\t', '⇥')
        except UnicodeDecodeError:
            label = ' '.join(f'{b:02X}' for b in data)
        return dict(raw=s, label=label, hex=data.hex(' '), id=model['vocab'][s])
    # Authored examples, not quotations or model generations.
    texts = [
        "Warszawa jest stolicą Polski i miastem położonym nad Wisłą. Jej historia obejmuje zarówno okresy rozwoju, jak i zniszczenia oraz odbudowę. Na ulicach spotykają się różne epoki: obok starych kamienic stoją współczesne biurowce, a tramwaje przejeżdżają między parkami, placami i osiedlami.\n\nW encyklopedii opis miasta dzieli się na części poświęcone geografii, historii, kulturze i transportowi. Każda z nich zawiera nazwy, daty oraz odsyłacze do innych artykułów. Ten sam tekst można podzielić na pojedyncze bajty lub większe fragmenty, których tokenizer nauczył się na polskiej Wikipedii.",
        "'''Warszawa''' – stolica [[Polska|Polski]], położona nad [[Wisła|Wisłą]]. Jest ośrodkiem administracyjnym, naukowym i kulturalnym. Artykuł zawiera odsyłacze do innych haseł oraz informacje uporządkowane w sekcjach.\n\n== Historia ==\nHistoria miasta wiąże się z rozwojem osadnictwa, zmianami politycznymi i odbudową po zniszczeniach wojennych. Dodatkowe informacje można znaleźć w artykule [[Historia Warszawy]].\n\n{{Infobox\n | nazwa = Warszawa\n | państwo = Polska\n}}\n[[Kategoria:Miasta w Polsce]]",
        "Łódź, łódka i łódki mają podobne litery, ale nie muszą mieć identycznych tokenów. Żółw powoli przechodzi przez ścieżkę, a gęś przygląda mu się z brzegu jeziora. W zdaniu pojawiają się polskie znaki: ą, ć, ę, ł, ń, ó, ś, ź oraz ż. Każdy z nich zajmuje więcej niż jeden bajt w kodowaniu UTF-8.\n\nHello, world! Cześć, świecie! Ten akapit miesza polski z angielskim, liczbami 2026 i 12345 oraz symbolami: [[link]], {{szablon}} i 🦆. Kolory pokazują podział tekstu, ale sam tekst pozostaje dokładnie w tym samym miejscu."
    ] + extra
    examples = []
    for text in texts:
        if '<|endoftext|>' in text:
            raise ValueError('This trace supports ordinary text, not special-token dispatch.')
        groups = [list(s) for s, _ in tok.pre_tokenizer.pre_tokenize_str(text)]
        initial = [[token(t) for t in group] for group in groups]
        steps = []
        while True:
            candidates = [(ranks[(g[i], g[i+1])], gi, i) for gi, g in enumerate(groups) for i in range(len(g)-1) if (g[i],g[i+1]) in ranks]
            if not candidates:
                break
            rank, gi, i = min(candidates)
            a,b = groups[gi][i:i+2]
            groups[gi][i:i+2] = [a+b]
            steps.append(dict(rank=rank+1, group=gi, index=i, left=token(a), right=token(b), merged=token(a+b)))
        ids = [model['vocab'][s] for g in groups for s in g]
        assert ids == tok.encode(text, add_special_tokens=False).ids, (text, ids)
        assert tok.decode(ids) == text
        examples.append(dict(text=text, initial=initial, steps=steps, ids=ids))
    payload = dict(sha256=hashlib.sha256(raw).hexdigest(), vocab=len(model['vocab']), vocabulary=model['vocab'], merges=merges, byteAlphabet=dict(zip(bs, map(chr, cs))), examples=examples)
    template=(ROOT/'scripts/tokenizer-template.html').read_text()
    output.write_text(template.replace('/*PAYLOAD*/null',json.dumps(payload,ensure_ascii=False).replace('<','\\u003c')))
    print(f'Wrote {output}; verified {len(examples)} exact traces against tokenizers; {len(merges)} learned merges.')


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--tokenizer',type=Path,default=ROOT/'datasets/wiki-tokenizer.json')
    p.add_argument('--output',type=Path,default=ROOT/'results/tokenizer.html')
    p.add_argument('--text',action='append',default=[],help='Add an example to the verified offline traces')
    a=p.parse_args();build(a.tokenizer,a.output,a.text)
