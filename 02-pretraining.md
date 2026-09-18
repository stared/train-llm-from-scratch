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

Uses **H100 by default**, with **10 minutes training / about 11½ minutes total / $0.78 measured worker compute**. Builds/storage cost extra. Context: 512 tokens; vocabulary: 8,192 tokens. You can start [fine-tuning](03-fine-tuning.md) in another terminal while this runs; each GPU job is billed separately.

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

## Choosing a GPU

**H100 is the default.** L4 costs less per run, but learns less within the same time. To use it, add `--gpu L4` to the training command.

Measured comparison on Wolne Lektury: the same 30M model, batch 32, context 512 and **10 minutes of training** per run. Worker time includes loading and evaluation; preparation and image builds are separate.

| GPU | Worker time | Worker cost | Tokens processed | Test loss ↓ |
|---|---:|---:|---:|---:|
| **H100 (default GPU)** | 10 min 37 s | $0.74 | 394M | 2.784 |
| H100, compiled training | 10 min 31 s | $0.73 | 724M | 2.748 |
| L4 | 10 min 34 s | $0.18 | 50M | 3.152 |
| A10 | 10 min 22 s | $0.23 | 72M | 3.064 |
| L40S | 10 min 24 s | $0.38 | 180M | 2.885 |

H100 processed more tokens per dollar in this comparison. Compilation speeds up the training loop; its initial compilation time is included in the ten minutes. These research runs use batch 32 and omit the workshop worker's extra quality diagnostics; the default command uses batch 64 and took 11 min 32 s / $0.78. Costs include worker CPU/memory and are estimates from single runs.

To compare cards, use the same batch size on both runs:

```bash
modal run scripts/scratch_recipe_modal.py --gpu L4 --batch-size 32
modal run scripts/scratch_recipe_modal.py --gpu H100 --batch-size 32
```

Add `--compile-training` to try compiled training. The complete participant command with batch 32 was also tested: 578M token presentations, test loss 2.760, 11 min 4 s worker time, $0.77. A larger GPU can also fit larger models or batches; speed and memory requirements depend on the workload. [Modal GPU options](https://modal.com/docs/guide/gpu) and [pricing](https://modal.com/pricing). [Measured comparisons](results/training-comparisons.html).

![GPU throughput and cost](results/gpu-comparison.svg)

## Tokens and epochs

The measured ten-minute run processed **328M token presentations**, about **3.24 times** the 101M-token training corpus. We sample random windows, so this is approximate exposure, not three sequential passes. More training can lower training loss while making held-out loss worse; watch both curves. In the matched research runs, extending training from 10 to 30 minutes increased exposure from 3.89 to 12.44 corpus-equivalents and reduced test loss from 2.784 to 2.720; worker cost rose from $0.74 to $2.12.

For Wikipedia, the training pool is much larger: 3.14B tokens. A ten-minute 30M/H100 research run processed 404M tokens, only **0.13 corpus-equivalents**. At that measured rate, one equivalent would take roughly **78 minutes / $5.8** (an extrapolation, not a measured full pass). A useful learning demonstration does not require a complete epoch.

## Try

For a shorter run, add `--max-seconds 300`. Compare the generated text and test loss, not just the training loss. Each run saves a new folder under `runs/`; the view command opens the latest completed run.

## Wikipedia alternative

[September 2026 dump](https://dumps.wikimedia.org/plwiki/20260901/): **2.73 GB compressed**, original markup retained. Preparation runs on Modal CPU and needs considerably more time and cloud storage than Wolne Lektury.

Measured on the prepared corpus, with the 98M-parameter model, batch 64, context 512 and compiled training:

| GPU | Training | Worker time | Worker cost | Test loss before → after |
|---|---:|---:|---:|---:|
| H100 | 10 min | 11 min 3 s | $0.77 | 9.174 → 1.627 |
| B200 | 10 min | 11 min | $1.19 | 9.174 → 1.509 |

Preparation is separate. Both learned markup while inventing facts; lower loss does not mean reliable knowledge. H100 processed 302M token presentations; B200 processed 565M. These are single runs, including compilation, diagnostics and successful checkpoint reload checks. [Experiment records](LAB_NOTEBOOK.md#participant-wikipedia-command-and-full-prose-data).

Prepare it:

```bash
modal run scripts/prepare_data_modal.py --corpus wikipedia
```

After **Ready**, start training:

```bash
modal run scripts/scratch_recipe_modal.py --recipe wiki-100m --compile-training
```

Open the live chart with `uv run scripts/view_results.py pretrain`. Add `--gpu B200` to compare cards, or use `--recipe wiki-cheap --max-seconds 300` for a smaller 10M model on L4 (earlier measured worker cost about $0.10).

Longer Wikipedia runs continue improving held-out loss. See the [training-time and cost curves](results/wikipedia-scaling.svg); those research runs take longer than this exercise.

**Next:** [3. Supervised fine-tuning](03-fine-tuning.md).
