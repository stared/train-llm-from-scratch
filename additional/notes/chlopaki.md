# Fine-tuning on the supplied chlopaki.md

**Base model: Qwen3.5-4B. Fine-tuning data: only the user-supplied [datasets/chlopaki.md](../../datasets/chlopaki.md), converted to adjacent dialogue pairs in both directions.** The earlier 64 assistant-written comic examples are not included.

Prepared dataset: [chlopaki-bidirectional-v1/train.jsonl](../../datasets/chlopaki-bidirectional-v1/train.jsonl). There are **1,270 unique examples: 635 forward and 635 reversed pairs**. Every pair has its reverse. We use the standard `user` and `assistant` roles; character names are metadata, not role names or artificial instructions.

The input contains 71 parsed scenes and 706 merged turns. Nine scenes contain only one turn; these cannot form a dialogue pair and are preserved in [unpaired_scenes.json](../../datasets/chlopaki-bidirectional-v1/unpaired_scenes.json). Scene headings and stage directions are excluded. A few unlabelled continuations are attached to the preceding speaker, with line-number records in [parsing_audit.json](../../datasets/chlopaki-bidirectional-v1/parsing_audit.json). Original spelling and transcription errors remain; the supplied file has not been verified as a complete official screenplay. Short speaker labels are resolved within scenes where possible, and unresolved labels remain as given.

All usable pairs go into training, as requested. Six newly written ordinary Polish questions—not quotation-completion prompts—are in [evaluation.json](../../datasets/chlopaki-bidirectional-v1/evaluation.json). No claim is made of a held-out film-dialogue test. Reversed replies teach reconstruction as well as conversation and can create unnatural responses; compare the actual outputs.

## Reproduce

```bash
modal run scripts/style_modal.py --stage train --data-run chlopaki-bidirectional-v1 --model qwen3.5-4b --epochs 1 --max-seconds 600 --batch-tokens 2048
```

One L4, BF16 LoRA rank 16, alpha 32, dropout 0.05, learning rate 1e-4, gradient checkpointing. Direct batches contain up to four examples and at most 2,048 padded input tokens; short length buckets reduce padding. Only answer tokens contribute to the loss. This mode uses an answer-token mean within each batch, unlike the earlier per-example gradient-accumulation recipe. Long examples are not silently truncated. The initial attempt without gradient checkpointing ran out of GPU memory and is recorded as a failed run.

The training limit is ten minutes, checked after each update; the overall function timeout is 20 minutes. `unique_examples_seen` and `full_dataset_seen` record whether a timed run actually covered every pair. Text outputs and exact training data are copied back to `runs/`; weights remain in the Modal volume.

If the cap interrupts the pass, continue the saved adapter on only the examples it has not seen:

```bash
modal run scripts/style_modal.py --stage train --data-run chlopaki-bidirectional-v1 --model qwen3.5-4b --epochs 1 --max-seconds 180 --batch-tokens 2048 --resume-run PREVIOUS_RUN_NAME
```

Continuation checks the dataset hash and model revision, carries over adapter weights and coverage, and starts a fresh AdamW optimizer. It is not an exact optimizer-state resume. Combined training time is recorded separately from the current call's time.

For a local NVIDIA GPU:

```bash
uv run scripts/style_workshop.py train --data-dir datasets/chlopaki-bidirectional-v1 --output runs/my-chlopaki --model qwen3.5-4b --epochs 1 --max-seconds 600 --batch-tokens 2048 --device cuda
```

`uv run scripts/prepare_chlopaki.py` rebuilds the dataset from the supplied file; it refuses to overwrite the versioned output directory. The source hash and dataset hash are in [dataset.json](../../datasets/chlopaki-bidirectional-v1/dataset.json).

## Evaluation labels

- **Before:** Qwen3.5-4B, original instruction checkpoint, no workshop fine-tuning and no style prompt.
- **Prompted baseline:** the same untuned model with the explicit comic style instruction.
- **After:** Qwen3.5-4B + LoRA trained on `chlopaki-bidirectional-v1`, no style prompt.

Every comparison uses the same question and a 192-new-token limit. We saved both greedy and fixed-seed sampled decoding. Long baseline answers may be cut short.

## Measured results

All **1,270/1,270** examples seen once, **318 updates**, **651.55 seconds training** across the initial ten-minute run and a 51.43-second continuation on remaining examples. Peak allocated VRAM 12.90 GB; saved-adapter reload matched. Final adapter: `style-train-wit-1788781334049902996` in the Modal volume.

Successful training calls cost an estimated **$0.2343**. Two sampling comparisons add **$0.0452**, for **$0.2794** timed requested compute. Failed initial OOM compute and startup/storage are excluded; this is not the full invoice cost.

Full-strength sampling produces a visibly absurd comic voice; greedy decoding mostly gives terse replies. Reducing adapter strength to 25% brings back longer explanatory answers and reduces the comic effect in these six questions. For the workshop, use full-strength sampling as the creative demonstration. Assess humor and coherence separately rather than treating every absurd answer as a failure.

[Selected examples](../../results/example-results.md) · [All six questions with exact model/data labels](../../results/chlopaki-results.md) · [Offline interactive report, 54 answers](http://localhost:5173/reports#chlopaki-results.html).

Reproduce the sampled comparison without training again:

```bash
modal run scripts/style_modal.py --stage sample --data-run style-train-wit-1788781334049902996
modal run scripts/style_modal.py --stage sample --data-run style-train-wit-1788781334049902996 --adapter-scale 0.25
```

Both use seed 42, temperature 0.7, top-p 0.8, top-k 20 and repetition penalty 1.1. Adapter strength scales the saved LoRA contribution at inference; no additional training takes place.
