# 2. Pretraining

Train a **30-million-parameter generative pretrained transformer (GPT)** from random weights on Wolne Lektury. It learns next-token prediction, not how to answer chat questions.

## Run

Complete [data preparation](01-data-and-tokens.md#run) first, then run:

```bash
modal run scripts/scratch_recipe_modal.py --recipe literature
```

Up to **10 minutes training / about $0.76 measured worker compute**. Loading and evaluation add time; builds/storage cost extra. Context: 512 tokens; vocabulary: 8,192 tokens. You can start [fine-tuning](03-fine-tuning.md) in another terminal while this runs; each GPU job is billed separately.

## Watch and open

The terminal prints training loss and checkpoint evaluations. Lower loss means better next-token predictions. When the job finishes:

```bash
uv run scripts/view_results.py pretrain
```

The report shows a learning curve and the same prompts before and after training. Development loss chooses the checkpoint; test loss evaluates it separately.

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

The full report preserves unedited continuations. The model learned recognizable prose but still makes grammatical and logical mistakes.

## Try

For a shorter run, add `--max-seconds 300`. Compare the generated text and test loss, not just the training loss. Each run saves a new folder under `runs/`; the view command opens the latest completed run.

## Wikipedia alternative

[September 2026 dump](https://dumps.wikimedia.org/plwiki/20260901/): **2.73 GB compressed**, original markup retained. Preparation needs tens of GB of disk space and considerably more download/CPU time.

Prepare it:

```bash
uv run scripts/prepare_pretraining.py wikipedia
```

After **Ready**, train for five minutes, about **$0.10 measured worker compute**:

```bash
modal run scripts/scratch_modal.py --size 10m --max-seconds 300
```

Repeat with `--size 30m` to compare sizes. Both use a 256-token context. Open with the same `view_results.py pretrain` command.

**Next:** [3. Supervised fine-tuning](03-fine-tuning.md).
