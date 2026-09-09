# Polish Wikipedia wikitext, trained from scratch

Implementation of the v2 scratch experiment. The user explicitly requested original Wikipedia markup. The expanded comparison includes ten-minute training on full Wikipedia, filtered article openings, popular article openings, historical Wolne Lektury, and TinyStories. See [the expanded curves and samples](pretraining_results.html), [generated examples](pretraining_example_results.md), and [experiment conclusions](PRETRAINING_FINDINGS.md). The [original five-minute comparison](wiki_scratch_results.html) remains available.

Source: official Polish Wikipedia article dump dated20260901, with a pinned SHA1 and size in `research/scratch/sources.json`. The full download is2.733GB compressed. XML is decoded once, then the text of nonempty main-namespace wikitext pages is retained **without markup stripping**. This includes article redirects, `[[links]]`, `{{templates}}`, headings, tables and `<ref>` tags. Article titles, page/revision IDs, URLs and content hashes remain in JSONL records. Template-definition and talk pages are outside the selected namespace.

Exact duplicate article texts go to the same split using SHA256 buckets:99% training,0.5% development and0.5% test in expectation. Related but nonidentical articles may cross splits. A training-only hash sample of up to2048 articles (first8192 characters each) trains a new8k byte-level BPE tokenizer. All extracted texts are then tokenized, with a per-article exact round-trip check. An EOD token separates articles in uint16 files; random causal training windows may cross an EOD boundary. The tokenizer does not remove or normalize markup.

## Ordinary uv scripts

```bash
uv run download_scratch_corpus.py --source wikipedia-pl-20260901 --download
uv run prepare_wiki_scratch.py --stage extract
uv run prepare_wiki_scratch.py --stage tokenize
uv run check_scratch_model.py
uv run --no-project -m unittest test_wiki_scratch_data -v
```

All local corpus files live inside this repository: Wikipedia downloads in `data/scratch-corpora/wikipedia-pl-20260901/`, the copied historical Wolne Lektury archive in `data/scratch-corpora/falenty-wl/`, and extracted Wikipedia text/tokenizer/tokens in `data/wiki-scratch-v1/`. Default script paths are anchored to the repository, even when launched from another working directory. Use `UV_CACHE_DIR="$PWD/.cache/uv"` from this folder to keep uv downloads here too. Modal receives a working copy of the token data; the local originals remain here.

Preparation defaults to `data/wiki-scratch-v1`. This name identifies the first prepared Wikipedia dataset, not a return to the old Falenty v1 model. Raw downloads, extracted text and binary tokens stay in the visible, gitignored `data/` folder. Preparation uses local CPU; rent the GPU after preparation.

Train on an ordinary supported NVIDIA GPU:

```bash
uv run train_scratch.py --size 10m --max-seconds 300 --device cuda --output runs/my-scratch-10m
uv run train_scratch.py --size 30m --max-seconds 300 --device cuda --output runs/my-scratch-30m
uv run sample_scratch.py runs/my-scratch-10m --device cuda --output my-scratch-samples.json
```

For Modal, upload `train.bin`, `dev.bin`, `test.bin`, `tokens.json` and `tokenizer.json` once to the existing `model-training-workshop` volume at `/datasets/wiki-scratch-v1/`, then:

```bash
uvx --from modal==1.5.0 modal run scratch_modal.py --size compare --max-seconds 300
```

The wrapper runs one L4 at a time,2CPU/16GiB host RAM,1000s hard timeout per worker and no configured retries. It calls the same trainer, then checks saved-model sampling in a fresh process. Small metrics/samples/source snapshots return to `runs/`; weights remain on the volume. GPU compute estimates include worker runtime but exclude preparation, startup, image build and persistent storage.

## Model and measurement

Both models are initialized entirely from random weights. No pretrained tokenizer, pretrained language model, SFT adapter or RLVR adapter is used.

- **10M:**10,244,160 parameters;6layers,width320,5attention heads,FFN896.
- **30M:**29,893,120 parameters;8layers,width512,8attention heads,FFN1408.

Counts assume the actual tokenizer reaches8192 vocabulary entries; the trainer records the instantiated count. Both use RoPE, RMSNorm, SwiGLU, tied input/output weights, causal SDPA, context256 and batch32. BF16, AdamW, peak LR6e-4,20-update warmup followed by time-based cosine decay to10% of peak, gradient clip1.0. No compilation startup. Same training duration, context, batch and seed; different-sized models will process different numbers of tokens.

Training samples uniform token windows with replacement from the **complete prepared training pool**. The recorded token exposure ratio is not an epoch-completion claim. A short run will generally visit only part of Wikipedia. Fixed development/test windows are used for loss comparisons. Checkpoints are selected by development loss; test loss does not select them. Initial, periodic, final and selected continuations use identical prompts and sampling seed. Evaluation and sample generation are included in the training time cap; compute-only throughput is separately recorded.

Prompts are continuation prefixes (`'''Warszawa''' –`, `== Historia ==`, `{{Infobox`, `'''Polska''' –`), not chat questions. Samples are128 generated BPE tokens with temperature.8/top-k50, displayed as literal source text. Learning useful markup structure is an experimental outcome, not a guarantee. No grammar/markup-validity score is inferred merely from lower language-model loss.

Weights, optimizer state and RNG state are saved at the final checkpoint; the current CLI does not yet expose training resumption. Selected weights are saved separately and verified by fresh-process generation on Modal. Data/tokenizer hashes, actual token count, elapsed time and peak GPU memory are recorded. CPU checks verify parameter counts, causal masking, a simple learning task, save/reload and exact tokenization of Polish text with markup. Those checks do not substitute for actual training results.

## Tokenizer visualization

Open [tokenizer_explorer.html](tokenizer_explorer.html) directly in a browser. It shows the same monospaced text with changing token boundaries and one merge at a time; links to Cornell for a full algorithm lesson. Rebuild with `uv run tokenizer_visualization.py`; add `--text "Twój tekst"` for another real-tokenizer example.

## First measured comparison

ScratchGPT-10m: 10,244,160 parameters, 6,929 updates, 56,762,368 token presentations, 303.60s training; dev 9.0643→2.3888, test 9.0627→2.2848; peak VRAM 1.79GB; worker 350.98s, estimated $0.099580.

ScratchGPT-30m: 29,893,120 parameters, 3,290 updates, 26,951,680 token presentations, 304.89s training; dev 9.1016→2.4743, test 9.0811→2.4003; peak VRAM 2.95GB; worker 351.91s, estimated $0.099845.

Successful worker compute estimate: $0.19942460 combined, excluding the earlier failed attempt and build/startup/storage overhead. Both saved models passed fresh-process generation checks. At equal time10M has lower held-out loss; outputs visibly reproduce Wikipedia markup but still invent facts and sometimes loop. This is a single-seed short-run result, not a claim that10M is generally better.
