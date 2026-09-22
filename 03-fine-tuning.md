# 3. Supervised fine-tuning: Polish Driving Licence Exam

**Model:** Qwen3.5-0.8B. **Data:** official Polish driving-theory questions, A/B/C answers. Prepared split: 100 train / 25 development / 40 test in [data.json](datasets/prawko-v2/data.json).

Compare **supervised fine-tuning (SFT)** with **reinforcement learning with verifiable rewards (RLVR)**.

## What to expect

| Dataset / model | Training | End to end | GPU | Worker cost | Test accuracy before → after |
|---|---:|---:|---|---:|---:|
| 100 driving questions / Qwen3.5-0.8B, SFT | 3 min | 5 min 21 s | L4 | $0.065 | 21/40 → 27/40 |

Time includes an image build, with model weights cached. Cost covers the training worker; builds and storage are separate. [Run report](http://localhost:5173/reports#workshop-check.html).

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

Each training run starts from the same original model and trains a [low-rank adaptation (LoRA)](https://huggingface.co/docs/peft/conceptual_guides/lora) adapter for up to three minutes. LoRA freezes the original weights and trains small added matrices, reducing the number of trainable parameters and optimizer memory. Loading and evaluation add time.

- **SFT:** input = question + options; target = correct letter.
- **RLVR:** sample four letters; reward each correct answer with 1, wrong answer with 0.

No reasoning examples or generated reasoning here. Inspect the training loop in [prawko.py](scripts/prawko.py).

## Compare

| Model / training | Correct on 40 held-out questions |
|---|---:|
| Qwen3.5-0.8B, no workshop training | 21 |
| + SFT on 100 driving exam questions | 27 |
| + RLVR on the same 100 questions | 27 |

The two pilot runs cost about $0.12 combined in worker compute. This is a small text-only subset, not a full driving exam. Each question changes accuracy by 2.5 percentage points. We select the checkpoint using the development set and report its score on the separate test set.

Open [before/after answers](results/prawko-example-results.md) and [longer-run curves](http://localhost:5173/reports#prawko-training.html). Find a correction, a regression, and a question where SFT and RLVR disagree. Does more training help?

## Watch training

In another terminal, run:

```bash
pnpm dev
```

Open **SFT** and select your run. See a training question and its target letter, then compare A/B/C probabilities on development questions across checkpoints. The test score is reported separately.

One actual correction, from the pilot linked above:

| Question 10840: how do you transport a child under 150 cm in the front passenger seat? | Answer |
|---|---|
| Original Qwen3.5-0.8B | A — on a passenger's lap |
| Same model + SFT on 100 exam questions | B — in a child seat or other child restraint |
| Official dataset key | B |

Question/options are abbreviated English translations; the actual inputs and predictions are Polish question text and A/B/C letters. Read the report for the complete question, all options and regressions.

## More training data

Use 289 official questions with the same development and test sets:

```bash
modal run scripts/prawko_modal.py --method sft --dataset expanded --max-seconds 180
```

| Dataset / model | Training | GPU | Worker cost | Test accuracy before → after |
|---|---:|---|---:|---:|
| 289 questions / Qwen3.5-0.8B, SFT | 3 min | L4 | $0.07 | 21/40 → 31–32/40 |
| Same data and model, SFT | 10 min | L4 | $0.19 | 21/40 → 33–35/40 |
| Same data and model, RLVR | 10 min | L4 | $0.19 | 21/40 → 29–33/40 |

Three seeds per recipe. Rotated-option scores were 30–33/40 for three-minute SFT, 29–32/40 for ten-minute SFT and 26–31/40 for ten-minute RLVR. These are exploratory results on a small, repeatedly inspected test set. The expanded preset also lowers the learning rate from 5e-5 to 2e-5. It beat simply extending the original 100-question recipe.

Set `--max-seconds 600` for ten minutes. Replace `--method sft` with `--method rlvr` to compare. Both methods shuffle answer options during training. View SFT runs under **SFT**, and exam RLVR runs under **RLVR**.

![Repeated exam training runs](results/exam-comparison.svg)

## GPU and model options

The default 0.8B model uses L4. For Qwen3.5-4B, the runner uses smaller batches on L4 to fit the longer exam prompts. Choose a card with `--gpu L40S` or `--gpu H100`; more expensive hardware is not automatically better value.

```bash
modal run scripts/prawko_modal.py --method sft --model qwen3.5-4b --max-seconds 600 --epochs 40
```

[Model, GPU and training comparisons](http://localhost:5173/reports#training-comparisons.html).

## Try

Change `--max-seconds 180` to `720` and `--epochs 10` to `40`. Our longer SFT/RLVR pair cost about **$0.43** in worker compute. Does the final model beat the development-selected checkpoint?

For a different task, [teach a model to answer in verse](additional/poetry.md).

**Next:** [4. Reinforcement learning with verifiable rewards](04-reinforcement-learning.md).

## See also

- [Which ML are you?](https://github.com/stared/which-ml-are-you): explore accuracy, log-loss, precision and recall.
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer): a configurable SFT training implementation.
- [More on fine-tuning, prompting and quantization](additional/reading.md#fine-tuning).
