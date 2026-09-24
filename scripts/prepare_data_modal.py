"""Download and tokenize pretraining data on Modal CPU, next to the training GPU."""
from pathlib import Path
import modal

app = modal.App('workshop-prepare-data')
volume = modal.Volume.from_name('model-training-workshop', create_if_missing=True)
image = (modal.Image.debian_slim(python_version='3.14')
         .pip_install('numpy==2.5.3', 'tokenizers==0.23.2')
         .add_local_file('datasets/wiki-tokenizer.json', '/work/datasets/wiki-tokenizer.json')
         .add_local_file('additional/research/scratch/sources.json', '/work/additional/research/scratch/sources.json'))
for script in ('download_scratch_corpus', 'prepare_wl_scratch', 'prepare_sejm_scratch', 'prepare_wiki_scratch', 'prepare_pretraining'):
    image = image.add_local_file(f'scripts/{script}.py', f'/work/scripts/{script}.py')


def prepare_on_volume(corpus, persist=Path('/persist')):
    import json
    import sys
    import tempfile
    sys.path.insert(0, '/work/scripts')
    from download_scratch_corpus import download, MANIFEST
    from prepare_pretraining import validate, NAMES, SOURCES
    name = NAMES[corpus]
    target = persist/'datasets'/name
    if target.exists():
        validate(target)
        print('Prepared data verified; reusing it.', flush=True)
        return name
    source = SOURCES[corpus]
    info = json.loads(MANIFEST.read_text(encoding='utf-8'))['sources'][source]
    downloads = persist/'datasets/sources'/source
    downloads.mkdir(parents=True, exist_ok=True)
    for item in info['files']:
        try:
            download(item, downloads)
        except Exception as error:
            raise RuntimeError(f'Source download failed: {item["url"]}. {error}') from None
    print('Tokenizing on Modal CPU. Tokens are integer IDs; each document ends with an end-of-text token.', flush=True)
    with tempfile.TemporaryDirectory(prefix='preparing-', dir=persist/'datasets') as temp:
        output = Path(temp)/name
        if corpus == 'wolne-lektury':
            from prepare_wl_scratch import prepare
            prepare(downloads/'wolnelektury.zip', Path('/work/datasets/wiki-tokenizer.json'), output)
        elif corpus == 'sejm':
            from prepare_sejm_scratch import prepare
            prepare(downloads/'sejm.zip', Path('/work/datasets/wiki-tokenizer.json'), output)
        else:
            from prepare_wiki_scratch import extract, tokenize
            extract(downloads/info['files'][0]['name'], output)
            tokenize(output)
        validate(output)
        output.rename(target)
    return name


@app.function(image=image, cpu=2, memory=8192, timeout=900, retries=0,
              max_containers=1, volumes={'/persist': volume})
def prepare_wolne_lektury():
    try:
        return prepare_on_volume('wolne-lektury')
    finally:
        volume.commit()


@app.function(image=image, cpu=2, memory=8192, timeout=1800, retries=0,
              max_containers=1, volumes={'/persist': volume})
def prepare_sejm():
    try:
        return prepare_on_volume('sejm')
    finally:
        volume.commit()


@app.function(image=image, cpu=4, memory=16384, timeout=7200, retries=0,
              max_containers=1, volumes={'/persist': volume})
def prepare_wikipedia():
    try:
        return prepare_on_volume('wikipedia')
    finally:
        volume.commit()


@app.local_entrypoint()
def main(corpus: str = 'wolne-lektury'):
    workers = {'wolne-lektury': prepare_wolne_lektury, 'sejm': prepare_sejm, 'wikipedia': prepare_wikipedia}
    if corpus not in workers:
        raise ValueError('Choose ' + ', '.join(workers))
    worker = workers[corpus]
    name = worker.remote()
    print(f'Ready: {name} in your Modal volume.')


