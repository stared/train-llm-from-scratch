# LLM robi prawko — a large language model takes driving theory

**Model:** Qwen3.5-0.8B. **Data:** official Polish driving-theory questions, A/B/C answers. Prepared split: 100 train / 25 development / 40 test in [data.json](../datasets/prawko-v2/data.json).

Compare **supervised fine-tuning (SFT)** with **reinforcement learning with verifiable rewards (RLVR)**.

## Run

```bash
modal run scripts/prawko_modal.py --method screen
modal run scripts/prawko_modal.py --method sft --epochs 10 --max-seconds 180
modal run scripts/prawko_modal.py --method rlvr --epochs 10 --max-seconds 180
```

Each training run starts from the same original model and trains a low-rank adaptation (LoRA) adapter for up to three minutes. Loading and evaluation add time.

- **SFT:** input = question + options; target = correct letter.
- **RLVR:** sample four letters; reward each correct answer with 1, wrong answer with 0.

No reasoning examples or generated reasoning here. Inspect the training loop in [prawko.py](../scripts/prawko.py).

## Compare

| Model / training | Correct on 40 held-out questions |
|---|---:|
| Qwen3.5-0.8B, no workshop training | 21 |
| + SFT on 100 Prawko questions | 27 |
| + RLVR on the same 100 questions | 27 |

Pilot worker compute: **about $0.12 total**, excluding builds/startup/storage. This is a small text-only subset, not a full driving exam.

Open [before/after answers](../results/prawko-example-results.md) and [longer-run curves](../results/prawko-training.html). Find a correction, a regression, and a question where SFT and RLVR disagree. Does more training help?

New results go to `runs/`. Local GPU options: `uv run scripts/prawko.py --help`.
