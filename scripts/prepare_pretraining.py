# /// script
# requires-python = ">=3.14"
# dependencies = ["modal==1.5.5", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Download, prepare, verify and upload a pretraining corpus. Safe to run again.

Sejm tokens are prepared for training on this computer and not uploaded; Modal
prepares its own copy with prepare_data_modal.py. The source is ~/corpora/sejm.txt
when present, otherwise the pinned sejm.zip is downloaded.
"""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FILES = ('train.bin', 'dev.bin', 'test.bin', 'tokenizer.json', 'tokens.json')
NAMES = {'wolne-lektury': 'wl-scratch-v1', 'wikipedia': 'wiki-scratch-v1', 'sejm': 'sejm-scratch-v1'}
SOURCES = {'wolne-lektury': 'falenty-wl', 'wikipedia': 'wikipedia-pl-20260901', 'sejm': 'sejm'}


def validate(folder):
    metadata = json.loads((folder/'tokens.json').read_text())
    for name in FILES:
        path = folder/name
        if name.endswith('.bin'):
            split = metadata['splits'][path.stem]
            if path.stat().st_size != 2*split['tokens']:
                raise ValueError(f'Wrong token count: {path}')
            expected = split['sha256']
        elif name == 'tokenizer.json':
            expected = metadata['tokenizer_sha256']
        else:
            continue
        with path.open('rb') as stream:
            if hashlib.file_digest(stream, 'sha256').hexdigest() != expected:
                raise ValueError(f'Checksum mismatch: {path}')
    return metadata


def sejm_source(source):
    """An explicit file, else the local text file, else the pinned download."""
    from prepare_sejm_scratch import DEFAULT_SOURCE
    if source or DEFAULT_SOURCE.is_file():
        return Path(source or DEFAULT_SOURCE).expanduser()
    from download_scratch_corpus import download, MANIFEST
    downloads = ROOT/'datasets/local/scratch-corpora/sejm'
    downloads.mkdir(parents=True, exist_ok=True)
    print(f'{DEFAULT_SOURCE} not found; downloading the published archive (existing downloads are verified and reused)', flush=True)
    for item in json.loads(MANIFEST.read_text())['sources']['sejm']['files']:
        download(item, downloads)
    return downloads/'sejm.zip'


def prepare_sejm(folder, source, check_only=False):
    from prepare_sejm_scratch import prepare as prepare_text
    source = None if check_only else sejm_source(source)
    recorded = json.loads((folder/'tokens.json').read_text())['extraction'] if folder.exists() else {}
    if source and recorded.get('source') == str(source):
        with source.open('rb') as stream:
            if hashlib.file_digest(stream, 'sha256').hexdigest() != recorded['source_sha256']:
                raise ValueError(f'{source} changed since {folder.relative_to(ROOT)} was prepared; delete that folder to prepare again')
    if not folder.exists() and not check_only:
        print('1/2 Preparing tokens from', source, 'on your CPU', flush=True)
        with tempfile.TemporaryDirectory(prefix='preparing-', dir=ROOT/'datasets/local') as temp:
            output = Path(temp)/folder.name
            prepare_text(source, ROOT/'datasets/wiki-tokenizer.json', output)
            validate(output)
            output.rename(folder)
    print('2/2 Checking prepared files:', folder.relative_to(ROOT), flush=True)
    validate(folder)
    print('Ready. Start training on this computer:\nuv run scripts/scratch_local.py --recipe sejm')


def prepare(corpus, check_only=False, source=None):
    name = NAMES[corpus]
    folder = ROOT/'datasets/local'/name
    if corpus == 'sejm':
        (ROOT/'datasets/local').mkdir(parents=True, exist_ok=True)
        return prepare_sejm(folder, source, check_only)
    if not folder.exists() and not check_only:
        from download_scratch_corpus import download, MANIFEST
        source = 'falenty-wl' if corpus == 'wolne-lektury' else 'wikipedia-pl-20260901'
        info = json.loads(MANIFEST.read_text())['sources'][source]
        downloads = ROOT/'datasets/local/scratch-corpora'/source
        downloads.mkdir(parents=True, exist_ok=True)
        print('1/3 Downloading source (existing downloads are verified and reused)', flush=True)
        for item in info['files']:
            download(item, downloads)
        print('2/3 Preparing text and tokens on your CPU', flush=True)
        with tempfile.TemporaryDirectory(prefix='preparing-', dir=ROOT/'datasets/local') as temp:
            output = Path(temp)/name
            if corpus == 'wolne-lektury':
                from prepare_wl_scratch import prepare as prepare_wl
                prepare_wl(downloads/'wolnelektury.zip', ROOT/'datasets/wiki-tokenizer.json', output)
            else:
                from prepare_wiki_scratch import extract, tokenize
                extract(downloads/info['files'][0]['name'], output)
                tokenize(output)
            validate(output)
            output.rename(folder)
    print('Checking prepared files:', folder.relative_to(ROOT), flush=True)
    metadata = validate(folder)
    if check_only:
        print('Local checks passed; no upload requested.')
        return
    import modal
    volume = modal.Volume.from_name('model-training-workshop', create_if_missing=True)
    remote = '/datasets/'+name
    try:
        remote_metadata = json.loads(b''.join(volume.read_file(remote+'/tokens.json')))
        sizes = {Path(f.path).name: f.size for f in volume.listdir(remote)}
        ready = remote_metadata == metadata and all(sizes.get(f) == (folder/f).stat().st_size for f in FILES)
    except FileNotFoundError:
        ready = False
    if not ready:
        print('3/3 Uploading prepared tokens to your Modal volume', flush=True)
        with modal.enable_output(), volume.batch_upload(force=True) as upload:
            for name in FILES:
                upload.put_file(folder/name, remote+'/'+name)
    else:
        print('3/3 Matching prepared files already on Modal; upload skipped.', flush=True)
    command = ('modal run scripts/scratch_recipe_modal.py --recipe wolne-lektury' if corpus == 'wolne-lektury'
               else 'modal run scripts/scratch_modal.py --size 10m --max-seconds 300')
    print('Ready. Start training:\n'+command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('corpus', choices=list(NAMES))
    parser.add_argument('--check-only', action='store_true', help='Validate existing local data without network access')
    parser.add_argument('--source', type=Path, help='Sejm only: plain-text corpus (default ~/corpora/sejm.txt)')
    args = parser.parse_args()
    prepare(args.corpus, args.check_only, args.source)
