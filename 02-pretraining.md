# 2. Pretraining

Train a **30-million-parameter generative pretrained transformer (GPT)** from random weights on Wolne Lektury. It learns next-token prediction, not how to answer chat questions.

## What to expect

| Dataset / model | Training | End to end | GPU | Worker cost | Test loss before → after |
|---|---:|---:|---|---:|---:|
| Wolne Lektury / ScratchGPT-30M | 10 min | 11 min 32 s | H100 | $0.78 | 9.073 → 2.820 |

Measured with the image already built. Cost includes GPU, CPU and memory; builds and storage are separate. [Run report](results/workshop-check.html).

## Run

Complete [data preparation](01-data-and-tokens.md#prepare-wolne-lektury) first, then run:

```bash
modal run scripts/scratch_recipe_modal.py --recipe wolne-lektury
```

The command uses H100, a 512-token context and an 8,192-token vocabulary. You can start [fine-tuning](03-fine-tuning.md) in another terminal while it runs.

## Watch training

In another terminal, run:

```bash
pnpm visualization
```

Open **Pretraining** and select your run. The loss curve updates during training. Select a checkpoint to compare the same prompt before and after training. Hover over colored tokens for their probabilities and alternatives.


## Actual result

**ScratchGPT-30M**, before and after ten minutes of pretraining on Wolne Lektury. Excerpts from an earlier run, `scratch-wl-30m-1788883120289174941`; ellipses mark truncation.

| Input | Random model | After pretraining |
|---|---|---|
| — Nie wiem, | 99okraty Juni Griiennikózózniemie… | ale mówiła o pani zaraz. … |
| Test loss (lower is better) | 9.073 | 2.782 |

The model learned recognizable prose but still makes grammatical and logical mistakes.

## Choosing a GPU

Choose another card with `--gpu L4`, `--gpu A10` or `--gpu L40S`.

Wolne Lektury, 30M parameters, batch 32, context 512, ten minutes of training. Worker time includes loading and evaluation; preparation and image builds are separate.

| GPU | Worker time | Worker cost | Tokens processed | Test loss ↓ |
|---|---:|---:|---:|---:|
| H100 | 10 min 37 s | $0.74 | 394M | 2.784 |
| L4 | 10 min 34 s | $0.18 | 50M | 3.152 |
| A10 | 10 min 22 s | $0.23 | 72M | 3.064 |
| L40S | 10 min 24 s | $0.38 | 180M | 2.885 |

H100 processed more tokens per dollar; L4 cost less per run. These measurements use batch 32 and fewer diagnostics than the main command, which uses batch 64. Costs include CPU and memory.

To compare cards, use the same batch size on both runs:

```bash
modal run scripts/scratch_recipe_modal.py --gpu L4 --batch-size 32
modal run scripts/scratch_recipe_modal.py --gpu H100 --batch-size 32
```

Add `--compile-training` to compile the training loop. With H100 and batch 32, the workshop script processed 578M tokens in ten minutes, with test loss 2.760. Including evaluation: 11 min 4 s, $0.77.

[Measured comparisons](results/training-comparisons.html). [Modal GPU options](https://modal.com/docs/guide/gpu) and [pricing](https://modal.com/pricing).

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

Watch it in the **Pretraining** section of the visualization. Add `--gpu B200` to compare cards, or use `--recipe wiki-cheap --max-seconds 300` for a smaller 10M model on L4 (earlier measured worker cost about $0.10).

Longer Wikipedia runs continue improving held-out loss. See the [training-time and cost curves](results/wikipedia-scaling.svg); those research runs take longer than this exercise.

**Next:** [3. Supervised fine-tuning](03-fine-tuning.md).
