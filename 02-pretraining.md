# 2. Pretraining

Train a **30-million-parameter generative pretrained transformer (GPT)** from random weights on Wolne Lektury. It learns next-token prediction, not how to answer chat questions.

## What to expect

| Dataset / model | Training | End to end | GPU | Worker cost | Test loss before → after |
|---|---:|---:|---|---:|---:|
| Wolne Lektury / ScratchGPT-30M | 10 min | 11 min 32 s | H100 | $0.78 | 9.073 → 2.820 |

Measured in the [flow check](results/workshop-check.html), with the image already built. Costs include worker CPU/memory, exclude builds/storage, and are estimates. Results vary.


## Run

Complete [data preparation](01-data-and-tokens.md#prepare-wolne-lektury) first, then run:

```bash
modal run scripts/scratch_recipe_modal.py --recipe wolne-lektury
```

Up to **10 minutes training / about $0.78 measured worker compute**. Loading and evaluation add time; builds/storage cost extra. Context: 512 tokens; vocabulary: 8,192 tokens. You can start [fine-tuning](03-fine-tuning.md) in another terminal while this runs; each GPU job is billed separately.

## Watch and open

The terminal prints training loss and checkpoint evaluations. Lower loss means better next-token predictions. **While training runs, open another terminal** in this repository and run:

```bash
uv run scripts/view_results.py pretrain
```

The live chart refreshes every three seconds. Training-loss points arrive about every five seconds; development loss is checked about once a minute. After training, the same view opens the completed report with before/after text. Development loss chooses the checkpoint; test loss evaluates it separately.

To inspect an included result while waiting:

```bash
uv run scripts/view_results.py pretrain --example
```

## Actual result

**ScratchGPT-30M**, random → pretrained on the historical Wolne Lektury corpus, ten-minute run `scratch-wl-30m-1788883120289174941`. Literal opening excerpts of generated continuations; ellipses mark truncation.

| Input | Random model | After pretraining |
|---|---|---|
| — Nie wiem, | 99okraty Juni Griiennikózózniemie… | ale mówiła o pani zaraz. … |
| Test loss (lower is better) | 9.073 | 2.782 |

The [latest flow check](results/workshop-check.html) took 11 minutes 32 seconds including loading and evaluation, with test loss **9.073 → 2.820**.

The full report preserves unedited continuations. The model learned recognizable prose but still makes grammatical and logical mistakes.

## Try

For a shorter run, add `--max-seconds 300`. Compare the generated text and test loss, not just the training loss. Each run saves a new folder under `runs/`; the view command opens the latest completed run.

## Wikipedia alternative

[September 2026 dump](https://dumps.wikimedia.org/plwiki/20260901/): **2.73 GB compressed**, original markup retained. Preparation runs on Modal CPU and needs considerably more time and cloud storage than Wolne Lektury.

Prepare it:

```bash
modal run scripts/prepare_data_modal.py --corpus wikipedia
```

After **Ready**, train for five minutes, about **$0.10 measured worker compute**:

```bash
modal run scripts/scratch_modal.py --size 10m --max-seconds 300
```

Repeat with `--size 30m` to compare sizes. Both use a 256-token context. Open with the same `view_results.py pretrain` command.

**Next:** [3. Supervised fine-tuning](03-fine-tuning.md).
