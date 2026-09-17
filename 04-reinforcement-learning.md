# 4. Reinforcement learning with verifiable rewards (RLVR): six words

**Model:** Qwen3.5-4B. **Task:** write one line with exactly six words, including two requested words, with no repeated words.

No target stories: the model samples answers; a Python checker gives rewards.

## What to expect

| Dataset / model | Training | End to end | GPU | Worker cost | Held-out success before → after |
|---|---:|---:|---|---:|---:|
| Six-word prompts / Qwen3.5-4B, RLVR | 10 min | 12 min 43 s | L4 | $0.19 | 1/32 → 24/32 |

Measured in the [flow check](results/workshop-check.html), including an image build, with model weights cached. Success means satisfying the checker, not literary quality. Worker estimates exclude builds/storage.


## Run

No previous exercise is required. Run:

```bash
modal run scripts/rlvr_showcase_modal.py --task six_words
```

About **10 minutes training**, **$0.19 worker compute**; loading/evaluation add time and startup/storage cost extra.

## Actual results

| Required words | Original Qwen3.5-4B | Same model + six-word RLVR |
|---|---|---|
| glacier, mermaid | The mermaid kissed the glacier. | Glacier melted to reveal a mermaid. |
| astronaut, birthday | Astronaut blew birthday candles. | Astronaut blew birthday candles in space. |

Earlier run: **1/32 → 32/32** held-out constraint compliance. The [latest flow check](results/workshop-check.html) reached **1/32 → 24/32** in ten minutes; results vary between runs. This measures the rules, not story quality. There is no matched supervised fine-tuning comparison.

Open the checker in [rlvr_tasks.py](scripts/rlvr_tasks.py). Can a bad story still pass? What would you change in the reward?

[All before/after answers](results/rlvr-results.html)

## Watch and open

The terminal prints rollout rewards and development checks. **While training runs, open another terminal** in this repository:

```bash
uv run scripts/view_results.py rlvr
```

The live chart shows rollout reward every ten steps and development constraint success every twenty steps. After training, the same view opens the before/after answers. To open the included result immediately:

```bash
uv run scripts/view_results.py rlvr --example
```

## Try

Check whether the successful stories are interesting, as well as valid. For another task, rerun with `--task countdown`; our earlier result was **7/32 → 11/32**, a smaller improvement. Each task starts from the original model.
