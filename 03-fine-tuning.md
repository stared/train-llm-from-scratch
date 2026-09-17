# 3. Supervised fine-tuning: Polish Driving Licence Exam

**Model:** Qwen3.5-0.8B. **Data:** official Polish driving-theory questions, A/B/C answers. Prepared split: 100 train / 25 development / 40 test in [data.json](datasets/prawko-v2/data.json).

Compare **supervised fine-tuning (SFT)** with **reinforcement learning with verifiable rewards (RLVR)**.

## What to expect

| Dataset / model | Training | End to end | GPU | Worker cost | Test accuracy before → after |
|---|---:|---:|---|---:|---:|
| 100 driving questions / Qwen3.5-0.8B, SFT | 3 min | 5 min 21 s | L4 | $0.065 | 21/40 → 27/40 |

Measured in the [flow check](results/workshop-check.html), including an image build, with model weights cached. Accuracy is more useful here than comparing training losses across methods. Worker estimates exclude builds/storage.


## Run

Run this independently of pretraining. The dataset is included, and baseline evaluation runs automatically.

```bash
modal run scripts/prawko_modal.py --method sft --epochs 10 --max-seconds 180
```

## Optional: compare with RLVR

Run this next to compare the two methods:

```bash
modal run scripts/prawko_modal.py --method rlvr --epochs 10 --max-seconds 180
```

Each training run starts from the same original model and trains a low-rank adaptation (LoRA) adapter for up to three minutes. Loading and evaluation add time.

- **SFT:** input = question + options; target = correct letter.
- **RLVR:** sample four letters; reward each correct answer with 1, wrong answer with 0.

No reasoning examples or generated reasoning here. Inspect the training loop in [prawko.py](scripts/prawko.py).

## Compare

| Model / training | Correct on 40 held-out questions |
|---|---:|
| Qwen3.5-0.8B, no workshop training | 21 |
| + SFT on 100 driving exam questions | 27 |
| + RLVR on the same 100 questions | 27 |

The [latest SFT flow check](results/workshop-check.html) also reached **27/40**, taking **5 minutes 21 seconds** including an image build, about **$0.065 worker compute**.

Pilot worker compute: **about $0.12 total**, excluding builds/startup/storage. This is a small text-only subset, not a full driving exam.

Open [before/after answers](results/prawko-example-results.md) and [longer-run curves](results/prawko-training.html). Find a correction, a regression, and a question where SFT and RLVR disagree. Does more training help?

## Watch and open

The terminal prints development accuracy after each epoch. **While SFT runs, open another terminal** in this repository:

```bash
uv run scripts/view_results.py sft
```

During training, the live chart shows development accuracy after each epoch. After training, the same view opens all 40 test questions with original predictions, trained predictions and the key. To open an included result without training:

```bash
uv run scripts/view_results.py sft --example
```

One actual correction, from the pilot linked above:

| Question 10840: how do you transport a child under 150 cm in the front passenger seat? | Answer |
|---|---|
| Original Qwen3.5-0.8B | A — on a passenger's lap |
| Same model + SFT on 100 exam questions | B — in a child seat or other child restraint |
| Official dataset key | B |

Question/options are abbreviated English translations; the actual inputs and predictions are Polish question text and A/B/C letters. Read the report for the complete question, all options and regressions.

## Try

Change `--max-seconds 180` to `720` and `--epochs 10` to `40`. Our longer SFT/RLVR pair cost about **$0.43** in worker compute. Does the final model beat the development-selected checkpoint?

For a different task, [teach a model to answer in verse](additional/poetry.md).

**Next:** [4. Reinforcement learning with verifiable rewards](04-reinforcement-learning.md).
