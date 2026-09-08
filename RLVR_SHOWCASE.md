# RLVR workshop: three visible experiments

**Start with six-word microfiction on Qwen/Qwen3.5-4B.** A fresh RLVR adapter improved held-out first-attempt compliance from **1/32 to 32/32** in about ten minutes on one Modal L4. The Python checker rewards exactly six English words, two required words, no repeated words, and one clean line. There is no workshop SFT warm start, teacher API, supplied answer text, or generated-code execution.

The saved adapter learned from **120 synthetic prompts and 480 of its own sampled answers**. These are not Pan Tadeusz or film examples. Its prose remains somewhat formulaic; the result demonstrates constraint-following, not a verified improvement in literary quality. This is one training seed and a small held-out test, including sixteen prompts whose required words were absent from training. All 32 after-test answers reached EOS.

Read [every actual before/after generation](RLVR_RESULTS.html), [the Markdown report](RLVR_RESULTS.md), and [the failed-reward lesson](RLVR_REWARD_LESSON.md). The 0.8B follow-up reached 9/32; the initial 0.6B recipe failed. The larger model and better optimization recipe are a practical choice, not a controlled explanation of which individual change mattered.

Actual original Qwen3.5-4B → same model with six-word RLVR:

| Required words | Before: original Qwen3.5-4B | After: Qwen3.5-4B + six-word RLVR |
|---|---|---|
| glacier, mermaid | The mermaid kissed the glacier. | Glacier melted to reveal a mermaid. |
| astronaut, birthday | Astronaut blew birthday candles. | Astronaut blew birthday candles in space. |
| mouse, vampire | The mouse bit the vampire. | Mouse fed vampire with tiny cheese. |

| Task | Participant sees | What the checker verifies | What it cannot establish |
|---|---|---|---|
| `six_words` | A tiny story with exactly six words and two requested words | Word count, both exact words, no duplicate words, one clean line | Meaning, grammar, humour, literary quality |
| `countdown` | An expression using three given numbers to reach a target | Safe arithmetic parsing, exact multiset of numbers, exact rational result | General mathematical reasoning ability |
| `maze` | A move string and its path across a map | Legal moves, no wall/boundary collisions, ending at the goal | General planning outside these 4×4 maps |

Measured final-test results (32 greedy first attempts each):

| Tested recipe | Before → after | Workshop decision |
|---|---:|---|
| Six words, Qwen3.5-4B, regularized RLVR, ~10 min | **1/32 → 32/32** | Main demonstration |
| Countdown, Qwen3.5-4B, regularized RLVR, ~5 min | 7/32 → 11/32 | Modest gain; not a strong solving demo |
| Maze, Qwen3-0.6B, initial unregularized recipe, ~1.5 min | 0/32 → 0/32 | Reward/debugging exercise |

These compare the tested recipes, not the intrinsic difficulty of each task: models and optimization settings differ. Additional failed 0.6B story/Countdown runs and the intermediate 0.8B story run remain in the complete report. The 4B maze recipe has not been tested.

The tasks use **shaped rewards** to provide feedback before perfect answers appear. Strict success is reported separately. A model can earn partial reward by getting the format right while still failing the puzzle. That distinction is part of the lesson.

## Run it

Only the Modal client runs on your laptop. The existing workshop Modal setup and persistent model cache are reused.

```bash
# Recommended, tested settings are the defaults: Qwen3.5-4B, LR 5e-5,
# beta .01, development checkpoint selection, 600-second training allowance.
uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task six_words

# Other independent tasks; each starts again from the original model.
# See measured outcomes before treating these as successful demos.
uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task countdown --max-seconds 300
# Reproduce the failed maze trial for the reward-debugging exercise.
uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task maze --model qwen3-0.6b --max-seconds 300 --lr 0.0002 --beta 0 --dev-interval 0

# Cheap inference-only screening: eight training prompts, four samples each.
uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task all --stage screen
```

`--task all --stage train` runs the three adapters **sequentially** on one GPU; each gets its own time allowance. Each remote function has an 1,100-second hard timeout, about $0.31 maximum requested compute at the rate in the wrapper (L4, two CPUs, 16 GiB host RAM), excluding startup and storage. The training cap is checked after a rollout/update batch; loading, before/after evaluation and reload checks are additional. No deployment keeps running after the command completes. Application retries are zero; platform interruptions still need monitoring.

The successful six-word run used **603.6 seconds** of training and intermediate development evaluation (3.6 seconds beyond its after-batch cutoff), approximately **14 GB** peak GPU allocation, and **$0.194** completed-worker compute including before/after evaluation and fresh-base reload. These are estimates, not a billing receipt. A strict five-minute cutoff has not been measured for the 4B story recipe; the full ten-minute run is the tested recommendation.

The entire preparation comparison—three inference screens and six training trials—used **$0.593** estimated completed-worker compute, excluding startup/storage. All apps completed and stopped. The arithmetic follow-up cost $0.109 and reached only 11/32, so no further sweep was run.

On your own supported NVIDIA GPU:

```bash
uv run rlvr_showcase.py --task six_words --device cuda --output runs/my-six-words
```

The trainer has pinned inline dependencies and a uv lockfile. CPU and MPS are selectable but not benchmarked. The ordinary trainer imports the adjacent `rlvr_tasks.py` and reads `models.json`; keep these files together. No coding assistant or notebook is required.

## What actually gets trained

Each update samples four completions for each of two prompts. A completion's advantage is its reward minus the mean reward of the other three completions for that prompt. Positive-advantage answers become more likely; negative-advantage answers become less likely. Uniform-reward groups contribute zero advantage.

The loss uses the sum of generated-token log probabilities, including the first EOS and excluding prompts and subsequent padding. Two-sequence microbatches accumulate one optimizer update for the entire eight-answer batch. Sampling uses temperature 1 with no top-k/top-p filtering; dropout is disabled in both sampling and gradient computation. The next update uses fresh on-policy samples. There is no length normalization, rollout reuse, PPO clipping or value model. This is a small **REINFORCE implementation with a leave-one-out baseline**, not a full GRPO trainer. See the [TRL RLOO documentation](https://huggingface.co/docs/trl/rloo_trainer) for the method and reference-policy regularization in a fuller implementation.

The initial beta=0 runs omit reference regularization and collapsed to repetitive shortcuts. The follow-up supports `--beta 0.01`: subtract beta times the sampled sequence log probability ratio, `log(pi / pi_reference)`, from each reward before computing advantages. The original frozen model, evaluated with LoRA disabled, is the reference. This estimate is detached; gradients flow only through the policy loss. Individual sampled estimates can be negative. Extra forward passes cost time but require no second model copy.

`--dev-interval 20` evaluates every 20 batches and retains the best development checkpoint: strict successes first, mean task reward as a tie-breaker, including the initial policy as a candidate. No final-test score selects a checkpoint. Rollout RNG is restored after intermediate evaluation. The training timer includes these intermediate development checks. The final selected checkpoint can precede the last update; the saved manifest records both.

Fresh rank-16 LoRA, alpha 32, dropout 0, AdamW learning rate 5e-5, gradient norm clipped to 1; maximum 160 rollout batches by default. Model revision is pinned in `models.json`. The recommended run uses [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) with `enable_thinking=False` in its chat template. The older [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) is retained as an explicitly selectable comparison.

To reproduce an initial failed 0.6B recipe, pass all of its settings explicitly: `--model qwen3-0.6b --max-seconds 300 --steps 160 --lr 0.0002 --beta 0 --dev-interval 0`. Historical run folders include the exact executed source before defaults were changed.

## Data and verification

`rlvr_tasks.py` generates 256 training, 24 development and 32 test problems, seed 20260907. Anchor pairs, arithmetic puzzles and maps do not repeat across splits. Half of the story test uses entirely new anchor words. Other splits share the task template and difficulty distribution: this is a narrow workshop evaluation, not broad out-of-distribution evidence.

Arithmetic and maze reference solutions exist only as checker metadata. They are never appended to the model input or supplied as targets. Stories have no reference answers. All text optimized by the policy gradient was sampled from the current model.

Before/after evaluation uses identical prompts and greedy decoding. A separate 24-answer development sample uses the same temperature-1 distribution as training, fixed seed 2026. Main scores are first-attempt success, with no retry or repair. The report includes all outputs rather than only successful examples. A fresh base plus saved adapter must reproduce eight deterministic outputs exactly. These small, single-training-seed tests need replication before making reliability claims.

```bash
uv run --no-project -m unittest discover

# Substitute the completed run directories printed by Modal.
uv run --no-project rlvr_showcase_report.py runs/RUN_STORIES runs/RUN_COUNTDOWN runs/RUN_MAZE
```

The report writes `RLVR_RESULTS.md` and `RLVR_RESULTS.html`. The HTML compares model-labelled answers, displays strict scores, highlights failure-to-success cases, and draws the attempted maze paths. The checkbox is an explicit display filter, not the evaluation procedure.

Each run saves `data.json`, all sampled `rollouts.json`, development/test before/after predictions, adapter-change/reload checks, timing, costs and executed source snapshots. Model weights remain in Modal volume `model-training-workshop` at `/runs/RUN_NAME/adapter`; the small records are copied locally.

## A 25–35 minute workshop segment

1. Show an untuned failure. Ask participants to write down the exact success rule.
2. Read and deliberately attack the checker: duplicate words, an expression that inserts an extra number, a maze route through a wall.
3. Predict the advantages for four sampled answers. Explain why four equally wrong answers provide no relative learning signal.
4. Run the ten-minute story experiment while inspecting the reward function and first rollouts.
5. Compare unseen first attempts, partial reward and strict success. For stories, also judge whether the text is worth reading.
6. Discuss reward hacking: a perfectly counted word salad passes the story checker. Changing the reward changes what the model is encouraged to do.

Experiments and measured decisions are recorded in [LAB_NOTEBOOK.md](LAB_NOTEBOOK.md). The older [tiny arithmetic RLVR](RLVR.md) is a working pipeline example whose measured accuracy stayed at 4/8; do not present that as demonstrated improvement.
