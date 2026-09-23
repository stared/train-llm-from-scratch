# 4. Reinforcement learning with verifiable rewards (RLVR): six words

**Model:** Qwen3.5-4B. **Task:** write one line with exactly six words, including two requested words, with no repeated words.

No target stories: the model samples answers; a Python checker gives rewards.

## What to expect

| Dataset / model | Training | End to end | GPU | Worker cost | Held-out success before → after |
|---|---:|---:|---|---:|---:|
| Six-word prompts / Qwen3.5-4B, RLVR | 10 min | 12 min 43 s | L4 | $0.19 | 1/32 → 24/32 |

Time includes an image build, with model weights cached. [Run report](http://localhost:5173/reports#workshop-check.html).

## Run

```bash
modal run scripts/rlvr_showcase_modal.py --task six_words
```

## Actual results

| Required words | Original Qwen3.5-4B | Same model + six-word RLVR |
|---|---|---|
| glacier, mermaid | The mermaid kissed the glacier. | Glacier melted to reveal a mermaid. |
| astronaut, birthday | Astronaut blew birthday candles. | Astronaut blew birthday candles in space. |

These examples come from an earlier run that reached 32/32 on held-out prompts; the newer [run report](http://localhost:5173/reports#workshop-check.html) reached 24/32. Success measures compliance with the rules, not story quality.

Open the checker in [rlvr_tasks.py](scripts/rlvr_tasks.py). Can a bad story still pass? What would you change in the reward?

[All before/after answers](http://localhost:5173/reports#rlvr-results.html)

## Watch training

In another terminal, run:

```bash
pnpm dev
```

Open **RLVR** and select your run. See sampled answers and their rewards. Select a checkpoint to compare fixed development prompts before and after training.

## Try

Check whether the successful stories are interesting, as well as valid. For another task, rerun with `--task countdown`; our earlier result was **7/32 → 11/32**, a smaller improvement. Each task starts from the original model.

## Check what the reward actually teaches

We also prompted **Qwen3.5-2B** to explain Polish driving-exam answers, then trained with RLVR rewarding only a correct final letter. Strict success rose **0 → 25/40**, but the model stopped explaining. Reading the explicit answer anywhere in the response gave **25/40 both before and after**. It learned the rewarded format, not better exam knowledge. [Actual outputs and curves](http://localhost:5173/reports#training-comparisons.html).

## See also

- [State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A) (Karpathy, 2023) — an overview of pretraining, SFT and reinforcement learning from human feedback.
- [TRL: GRPO trainer](https://huggingface.co/docs/trl/grpo_trainer) and [RLOO trainer](https://huggingface.co/docs/trl/rloo_trainer) — `scripts/rlvr_showcase.py` uses on-policy REINFORCE with a leave-one-out baseline (RLOO); GRPO is the close relative used for DeepSeek-R1.
- [DeepSeek-R1 paper](https://arxiv.org/abs/2501.12948) — RLVR at scale, with a detailed account of training and evaluation.
