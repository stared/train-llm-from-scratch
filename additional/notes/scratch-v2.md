# Training from scratch, v2

Design brief, 8 September 2026. Falenty is v1 and a source of observations; its architecture, presets, tokenizer, corpus concatenation and teaching sequence are not requirements for this version. **The corpus audit/download manifest is verified; the model configurations below are proposed, not benchmarked or trained yet.** No GPU spend in this research step.

## What participants should see

A randomly initialized model learns recognizably Polish text, and two models trained on different corpora acquire different kinds of writing. Save matched continuations before training and at fixed time checkpoints, alongside held-out loss. Literature and Wikipedia offer an intuitive comparison: dialogue/narration versus definitions/descriptions. These are expected tendencies to test, not fabricated sample outputs or a promise of coherent factual answers.

The main exercise is a working small language model trained entirely from scratch. A character predictor or Markov model can be a five-minute explanation, not a mandatory sequence of architectures participants must implement before reaching the main experiment. No pretrained language-model weights or adapter training in this section. Train the tokenizer too.

## Starting hypotheses, not inherited presets

| | Small candidate | Larger candidate |
|---|---:|---:|
| Vocabulary | 8,192 | 8,192 |
| Layers | 6 | 8 |
| Hidden width | 320 | 512 |
| Attention heads / head width | 5 / 64 | 8 / 64 |
| SwiGLU intermediate width | 896 | 1,408 |
| Proposed parameter count | 10,244,160 | 29,893,120 |
| Initial context | 256 subword tokens | 256 subword tokens |
| Meaningful trial | 5–10 minutes | 5–10 minutes |

Counts are calculated for bias-free Q/K/V/output projections, three SwiGLU matrices, two RMSNorms per block, one final RMSNorm, tied input/output embeddings and parameter-free RoPE. They are design arithmetic, not instantiated-model measurements. Confirm in implementation. The30M candidate is the provisional main model; the10M candidate tests whether faster updates win at equal wall time. Neither is declared better before measurement.

Architecture: ordinary causal decoder, full multi-head attention, RoPE, RMSNorm, SwiGLU and tied embeddings. Use PyTorch [scaled-dot-product attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html) with `is_causal=True`, not Python loops over separate heads and explicit dense attention masks. It can choose fused kernels; benchmark the actual configuration instead of assuming a speedup. Avoid introducing mixture-of-experts, GQA or a very long context before evidence that they help this experiment.

Tokenizer: train byte-level BPE with an8k vocabulary, retaining Polish diacritics and complete byte coverage. Measure characters per token on held-out Polish text and inspect segmentations before choosing4k versus8k;8k is the initial candidate. For corpus comparisons, use one shared tokenizer trained on a balanced sample of **training** documents from the two sources. A borrowed151k-vocabulary tokenizer would spend about48M embedding parameters at width320 before counting any transformer blocks; tying an8k vocabulary uses about2.6M. Keeping the vocabulary appropriate to a tiny model is a major design choice, not an implementation footnote.

Training loop: BF16 on supported GPUs, AdamW, gradient clipping, short warmup and a documented decay schedule; dropout0 initially. Tune batch size for throughput with a few bounded timing steps, keeping a fixed token budget per optimizer update when comparing model sizes. A fused optimizer and compilation are options to measure, not default assumptions: compilation startup can consume a material part of a short workshop run. Keep data tokenized and cached before renting the training GPU. Record tokens/second, actual total tokens, updates, parameter count, precision and full elapsed time.

Use256-token context initially, then test512 only if samples or held-out loss justify its cost. Do not start with2048 just because the hardware permits it. Unlike v1's character context, these tokens usually span substantially more text; measure that on this tokenizer.

## Available full corpora

### Wolne Lektury

The historical Falenty archive is now copied and checksum-verified inside this repository at `datasets/local/scratch-corpora/falenty-wl/wolnelektury.zip`: **123,071,225 bytes compressed**, containing one `wolnelektury.txt` of **337,172,535 bytes /312,259,017 Unicode characters**. It has7,157 repeated footer markers and7,140 distinct catalogue links. The archive hash and text hash are saved in [the audit](../research/scratch/falenty_corpus_audit.json). This is a historical concatenated snapshot, not proof of current catalogue completeness.

The live [Wolne Lektury API](https://wolnelektury.pl/api/) returned **7,654 catalogue entries** and **2,527 top-level works** on8 September2026. The [parent-books endpoint](https://wolnelektury.pl/api/parent_books/) avoids selecting both a parent collection and its individual subworks as independent downloads. Those counts include the catalogue's languages; Polish filtering requires per-work metadata. Parent selection alone does not establish perfect deduplication.

For v2, prefer a fresh document-preserving corpus built from top-level Polish works: retain title, author, source URL, source hash and credits/licence metadata separately; remove repeated publisher footers from training text; inspect footnote/header handling; exact-deduplicate and group related editions/collections before splitting. Cache full source files so cleaning is reviewable and repeatable. The existing archive is a useful fallback/benchmark input but should not dictate the new format.

The third-party [Wolne Lektury HF mirror](https://huggingface.co/datasets/PiotrSty/wolne-lektury-polish-literature-corpus) is another lead, not the selected source: its card reports7,316 records including several languages and automatic PII redaction. The preview shows ISBNs altered to `[PHONE]`, illustrating why a ready-made mirror still needs inspection. Prefer official per-work text and metadata for the fresh v2 build. Do not assume every work/translation/annotation has one blanket licence; preserve source credits.

### Whole Polish Wikipedia, already cleaned

[Wikimedia's dataset](https://huggingface.co/datasets/wikimedia/wikipedia), configuration **`20231101.pl`**: **1,587,721 articles, six Parquet shards,1,765,059,986 bytes compressed**. Fields: `id`, `url`, `title`, `text`. This is a full cleaned Polish snapshot from November2023, not September2026. It removes markup and some sections such as references; it is not a byte-for-byte mirror of every page.

Pinned dataset revision: `b04c8d1ceb2f5cd4588862100d08de323dccfbaa`. All six URLs and SHA256 hashes are in [sources.json](../research/scratch/sources.json). Metadata and a small preview were fetched successfully (AWK, Alergologia, ASCII, Atom, Aksjomat); the entire1.765GB was **not downloaded**. The dataset card and size API disagree about uncompressed/memory size, so only compressed shard size is treated as verified here. Preserve article IDs/URLs for attribution and audit; follow the source's reuse terms.

### Current official Wikipedia dump

[September2026 Polish Wikipedia article dump](https://dumps.wikimedia.org/plwiki/20260901/plwiki-20260901-pages-articles.xml.bz2): **2,733,269,592 bytes compressed**. The [dump status](https://dumps.wikimedia.org/plwiki/20260901/dumpstatus.json) marks `articlesdumprecombine` done. SHA1: `ffc211b4dc3d73b46c2cd1d4b149868c986eeafc`. This is current-revision article-dump XML/wikitext, not the full revision history or image files. Extraction must retain main-namespace article text and handle redirects/templates; it is not directly training-ready plain text. The multistream variant is also available (2,890,827,471 bytes).

For the first workshop experiment, the cleaned2023 snapshot saves preparation work. Use the2026 raw dump if freshness is a requirement. Pin dated URLs instead of mutable `latest` links.

## Download commands

The downloader lists files without fetching them by default:

```bash
uv run scripts/download_scratch_corpus.py --source wikipedia-pl-clean
```

Download the complete cleaned snapshot (six files):

```bash
uv run scripts/download_scratch_corpus.py --source wikipedia-pl-clean --download
```

Or the current raw XML dump:

```bash
uv run scripts/download_scratch_corpus.py --source wikipedia-pl-20260901 --download
```

Files go under ignored `datasets/local/scratch-corpora/`. The stdlib script verifies sizes/checksums, uses `.part` files and attempts HTTP range resume. Listing and checksum verification of the existing Falenty archive were tested; a complete network transfer/resume of Wikipedia has not been tested in this step. Use the repository-local Falenty archive; no external repository is needed for this data.

## Experiment order and success criteria

1. Build document-preserving cleaned corpora, group related works, and create fixed train/dev/test splits before tokenizer training. Keep complete corpora available; don't equate a time-limited random sample of their windows with completing a full epoch.
2. Train and inspect the tokenizer on training text. Report compression on held-out text. Pack documents with explicit end-of-document tokens and document the attention/boundary policy; never split train/test by cutting a concatenated text file through a work.
3. On one corpus, compare the10M and30M candidates at equal5–10-minute wall-time budgets. Choose using development loss and predeclared qualitative sample checks. Report token throughput and actual token exposure so a larger model's apparent gain isn't confused with a different compute budget.
4. Train the selected architecture separately on full literature and full cleaned Wikipedia as the available training pools, with the same tokenizer, duration and matched continuation prompts. Keep the corpus effect separate from the model-size comparison. Mixing both sources is a later experiment because it obscures this comparison.
5. Save actual samples at initialization and fixed intervals (e.g.1,3,5,10minutes), without allowing sample generation to reset the training RNG. Save selected and final checkpoints, optimizer/RNG state for honest resumption, and verify generation after fresh-process reload. Compare losses across models only with the same tokenizer and evaluation corpus; report bits per byte if comparing tokenizers.

Suggested continuation prompts, **not generated model outputs**: `Warszawa`, `W roku`, `Był to`, `— Nie`. The expected visible learning is from random text toward Polish morphology and corpus-specific prose. It is not instruction following or verified knowledge. Avoid claiming TinyStories-level coherence on full complex Polish text: [TinyStories](https://arxiv.org/abs/2305.07759) deliberately simplifies the data, while [SmolLM's training work](https://huggingface.co/blog/smollm) also emphasizes data curation. Those motivate measuring data/model fit; they do not establish the runtime or quality of these proposed configurations.

This is v2's investigation plan, not an English participant walkthrough. Runtime and generated-quality claims wait for the first actual scratch-training trials.
