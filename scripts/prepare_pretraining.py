# /// script
# requires-python = ">=3.14"
# dependencies = ["modal==1.5.5", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Download, prepare, verify and upload a pretraining corpus. Safe to run again."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FILES = ('train.bin', 'dev.bin', 'test.bin', 'tokenizer.json', 'tokens.json')


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


def prepare(corpus, check_only=False):
    name = 'wl-scratch-v1' if corpus == 'wolne-lektury' else 'wiki-scratch-v1'
    folder = ROOT/'datasets/local'/name
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
    parser.add_argument('corpus', choices=['wolne-lektury', 'wikipedia'])
    parser.add_argument('--check-only', action='store_true', help='Validate existing local data without network access')
    args = parser.parse_args()
    prepare(args.corpus, args.check_only)
