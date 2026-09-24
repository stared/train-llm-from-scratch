"""Download the complete Wolne Lektury edition and prepare literary-text training data."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.request import urlopen

URL = 'https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt'
HEADINGS = ['pierwsza','druga','trzecia','czwarta','piąta','szósta',
            'siódma','ósma','dziewiąta','dziesiąta','jedenasta','dwunasta']


def prepare(raw, output):
    text = raw.decode('utf-8-sig').replace('\r\n', '\n')
    body, separator, credits = text.partition('\n-----\n')
    if not separator or 'Ten utwór jest w domenie publicznej.' not in credits:
        raise ValueError('Unexpected source layout; review the download before preprocessing')
    for heading in HEADINGS:
        if len(re.findall(r'^Księga '+heading+r'\s*$', body, re.M)) != 1:
            raise ValueError(f'Missing/duplicate book: {heading}')
    if not re.search(r'^Epilog\s*$', body, re.M):
        raise ValueError('Missing epilogue')
    # Drop title/ISBN front matter, preserve all twelve books and the epilogue,
    # including authorial headings and argument summaries. Only trim indentation.
    body = body[body.index('Księga pierwsza'):]
    body = '\n'.join(line.strip() for line in body.splitlines()).strip()+'\n'
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    (out/'source.txt').write_bytes(raw)
    (out/'train.txt').write_text(body, encoding='utf-8', newline='\n')
    (out/'SOURCE_CREDITS.txt').write_text(credits.strip()+'\n', encoding='utf-8', newline='\n')
    metadata = {'title': 'Pan Tadeusz', 'author': 'Adam Mickiewicz',
                'source_url': URL, 'source_page': 'https://wolnelektury.pl/katalog/lektura/pan-tadeusz/',
                'source_sha256': hashlib.sha256(raw).hexdigest(),
                'text_sha256': hashlib.sha256(body.encode()).hexdigest(),
                'characters': len(body), 'words_whitespace': len(body.split()),
                'books': 12, 'epilogue': True, 'split': 'entire literary text used for training; no held-out book',
                'preprocessing': 'Normalize CRLF, remove front title/ISBN and publisher footer; preserve all twelve books and epilogue; strip line indentation. Unmodified source and credits retained.'}
    (out/'corpus.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-file', type=Path)
    p.add_argument('--output', default='datasets/pan-tadeusz-full')
    a=p.parse_args()
    if a.source_file:
        raw=a.source_file.read_bytes()
    else:
        with urlopen(URL, timeout=60) as response:
            raw=response.read()
    prepare(raw,a.output)
