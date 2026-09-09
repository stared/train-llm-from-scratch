# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""List or download pinned scratch-training corpora; stdlib, resumable, checked.

Listing is the default. --download explicitly fetches the complete selected source.
The existing Falenty archive can be reused instead of downloaded again.
"""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

MANIFEST = Path(__file__).resolve().parent / 'research/scratch/sources.json'


def verify(path, item):
    if path.stat().st_size != item['size']:
        raise ValueError(f'Unexpected size: {path}')
    with path.open('rb') as f:
        digest = hashlib.file_digest(f, item['hash_algorithm']).hexdigest()
    if digest != item['checksum']:
        raise ValueError(f'Checksum mismatch: {path}')


def download(item, folder):
    target = folder / item['name']
    if target.exists():
        verify(target, item)
        print('Verified cached', target, flush=True)
        return
    partial = target.with_name(target.name + '.part')
    offset = partial.stat().st_size if partial.exists() else 0
    if offset > item['size']:
        raise ValueError(f'Oversized partial file: {partial}')
    if offset < item['size']:
        headers = {'User-Agent': 'AI-from-scratch-workshop/1.0'}
        if offset:
            headers['Range'] = f'bytes={offset}-'
        request = urllib.request.Request(item['url'], headers=headers)
        with urllib.request.urlopen(request, timeout=60) as response:
            append = response.status == 206 and offset > 0
            if append and not response.headers.get('Content-Range', '').startswith(f'bytes {offset}-'):
                raise ValueError('Unexpected resumed range')
            print('Downloading', item['name'], 'from byte', offset if append else 0, flush=True)
            with partial.open('ab' if append else 'wb') as f:
                while chunk := response.read(1024 * 1024):
                    f.write(chunk)
    verify(partial, item)
    partial.rename(target)
    print('Verified', target, flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', choices=['falenty-wl', 'wikipedia-pl-clean', 'wikipedia-pl-20260901'], required=True)
    p.add_argument('--download', action='store_true')
    p.add_argument('--output', type=Path, default=MANIFEST.parents[2] / 'data/scratch-corpora')
    a = p.parse_args()
    source = json.loads(MANIFEST.read_text())['sources'][a.source]
    print(source['description'])
    print(f"{len(source['files'])} files; {sum(x['size'] for x in source['files'])/1e9:.3f} GB compressed")
    for item in source['files']:
        print(item['name'], item['size'], 'bytes')
    if a.download:
        folder = a.output / a.source
        folder.mkdir(parents=True, exist_ok=True)
        for item in source['files']:
            download(item, folder)
    else:
        print('Listing only. Add --download to fetch the complete source.')


if __name__ == '__main__':
    main()
