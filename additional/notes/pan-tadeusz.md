# Train on the entire Pan Tadeusz

This example performs **continued pretraining with LoRA on the actual literary text** from Wolne Lektury. It is separate from the 64-example question-to-poem adapter. There are no synthetic answers or chat templates in the training corpus.

Included: all **12 books plus the epilogue**, 441,326 characters / 68,896 whitespace-separated words after preprocessing. The dataset retains headings and book summaries. It removes front title/ISBN metadata and the publisher footer from training; the complete unmodified download and all credits are preserved separately.

- [Training text](../../datasets/pan-tadeusz-full/train.txt)
- [Unmodified Wolne Lektury download](../../datasets/pan-tadeusz-full/source.txt)
- [Source credits](../../datasets/pan-tadeusz-full/SOURCE_CREDITS.txt)
- [Manifest and hashes](../../datasets/pan-tadeusz-full/corpus.json)
- [Wolne Lektury edition](https://wolnelektury.pl/katalog/lektura/pan-tadeusz/)

The source identifies the literary work as public domain. Source edition: Adam Mickiewicz, *Pisma Adama Mickiewicza*, volume V, Paris 1860. The supplied credits preserve the publisher's attribution and terms for editorial material.

## Run

```bash
modal run scripts/corpus_modal.py --max-seconds 600
```

Default: LFM2.5-2.6B, one L4, BF16 LoRA rank eight, learning rate 1e-4, batch two, one shuffled pass through the full tokenized book. Blocks have 256 next-token targets and share one boundary token, so chunking does not discard targets at block boundaries. The final partial block is retained and padding is masked.

The ten-minute training limit is checked after each update; the whole remote function has a 20-minute timeout. The result records `full_corpus_seen`, `unique_target_fraction`, target-token count, actual steps and time. **A full corpus on disk does not imply a time-limited run saw all of it:** check these fields. Training uses the entire book, so there is no held-out-book perplexity claim.

Local NVIDIA GPU:

```bash
uv run scripts/corpus_workshop.py --data-dir datasets/pan-tadeusz-full --output runs/my-pan-tadeusz --device cuda --max-seconds 600
```

To independently redownload and check the source layout:

```bash
uv run scripts/prepare_pan_tadeusz.py --output data/pan-tadeusz-check
```

The preparer verifies twelve distinct book headings and the epilogue before creating the output directory. It refuses to overwrite an existing dataset. Both original and processed text have SHA-256 hashes.

## What to inspect

The run saves before/after outputs on two original literary opening lines and two chat questions, then discards the trained model and reloads a fresh base plus the saved adapter. Raw continuation and chat are evaluated separately: becoming better at continuing verse does not automatically make an instruction-tuned assistant answer all questions poetically.

The original opening lines are not taken from the book, but the pretrained base may already know *Pan Tadeusz*. This experiment demonstrates domain adaptation; it does not establish that the model learned the work for the first time. Save and read actual outputs rather than treating a lower training loss as proof of literary quality.

Weights stay in the shared Modal volume; text results return to `runs/`. [The lab notebook](../../LAB_NOTEBOOK.md) records the measured rehearsal and cost.

## Measured rehearsal

LFM2.5-2.6B completed one **full pass in 61.3 seconds**: 333 updates, all 665 blocks, all 169,997 next-token targets. The saved adapter reloaded with identical outputs on all four probes. Timed remote execution was 177.7 seconds; estimated requested compute **$0.0504**, excluding startup/storage. Peak allocated VRAM: 7.79 GB.

[Raw run record](../../runs/pan-tadeusz-1788776622044561619/execution.json). Continuations become more like narrated verse scenes, but grammar and coherence remain uneven. The chat probes produce planning text under the current template and short output cap; this run does not demonstrate an always-poetic assistant. [Before/after examples](../../results/example-results.md#full-book-pan-tadeusz-continued-pretraining).

## Ordinary questions and statements

[Eight new before/after chat comparisons](../../results/pan-tadeusz-results.md) test the saved full-book adapter with sampled decoding, without a poetry instruction. They do not demonstrate reliable poetic chat: English planning text consumes much of the output budget, and visible replies mostly remain prose. The report separates final-reply text from planning and retains unmodified raw outputs.

Run without retraining:

```bash
modal run scripts/corpus_probe_modal.py
```

Local GPU: `uv run scripts/corpus_probe.py --adapter-dir PATH_TO_SAVED_RUN --output runs/my-corpus-probe`.

## Question-to-verse follow-up — dataset prepared

[500 ordinary Polish prompts → 4–12 original verse lines](../../workshop/poetry.md) now provide explicit chat supervision, including deliberately humorous modern questions answered by historical passages. The dataset has 450 training and 50 validation pairs. [Qwen3.5-4B has now been trained on these pairs](../../results/pan-tadeusz-qa-results.md); the full-book results below are separate experiments.

## Larger training chunks — tested at 2,048 targets

The original measured run used only 256 next-token targets per chunk; this was an experiment setting, not the model's context limit. The trainer now accepts 256, 1,024, 2,048 or 4,096 targets, batch size one or two, and optional line-aligned boundaries.

Tested comparison, starting from the same original checkpoint on the same full book:

```bash
modal run scripts/corpus_modal.py --target-tokens 2048 --batch-size 1 --line-aligned --max-seconds 600
```

Local GPU:

```bash
uv run scripts/corpus_workshop.py --output runs/pan-tadeusz-2048 --device cuda --target-tokens 2048 --batch-size 1 --line-aligned --max-seconds 600
```

A chunk contains at most 2,049 input tokens to predict 2,048 targets. Line-aligned mode chooses the last available token boundary ending in a newline under that limit. One token overlaps between chunks as context, and every next-token target remains covered exactly once per full pass. Very long lines or unavailable newline token boundaries fall back to a fixed split; `forced_line_splits` records those cases. It preserves line boundaries where possible, not necessarily couplet/stanza/book boundaries.

Longer chunks enable non-reentrant gradient checkpointing to reduce activation memory. The **2,048-target, batch-one** recipe completed a full pass: **84 chunks / 84 updates, 73.02 seconds training, 8.83 GB peak allocated VRAM**, zero forced line splits, all saved-adapter reload outputs matching. Other new sizes remain untested. At the same one-pass token budget, larger batches of target tokens also produce fewer optimizer updates, so this is not a perfectly isolated context-length comparison. The ten-minute cap and full-corpus coverage reporting remain in place.

Longer context may help model relationships across verses; it does not enforce syllable count or turn continued pretraining into question-to-poem instruction training. The output generation caps remain separate settings.

[Actual before/after and 256-vs-2,048 comparisons](../../results/pan-tadeusz-2048-results.md): ordinary replies remain prose; a manually checked continuation line has 11 syllables. Eight short chat probes plus two longer-output diagnostic questions do not establish thirteen-syllable chat. New training and evaluation cost **$0.09176 estimated requested compute**, excluding startup/storage.

Reproduce the saved-adapter chat test without training again:

```bash
modal run scripts/corpus_probe_modal.py --adapter-run pan-tadeusz-1788794554392255032 --long-output-tokens 1024
```
