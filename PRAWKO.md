# LLM robi prawko

Teach a small model to answer real Polish driving-theory questions, then compare supervised fine-tuning with reward-based practice. This is a multiple-choice knowledge exercise: the model selects A, B or C, without generating a rationale.

**Longer follow-up:** [interactive learning curves and actual choices](PRAWKO_TRAINING.html), [all selected/final before–after results](prawko_long_results.md). After12 minutes each, final SFT scored28/40 (reordered30/40), final RLVR25/40 (reordered24/40). Development-selected checkpoints reversed the small original-order lead: SFT28/40, RLVR29/40. See the full comparison below.

## Initial three-minute pilot

**Qwen/Qwen3.5-0.8B**, same pinned base for both fresh adapters:

| Adapter training | Training questions | Held-out test | Same test, rotated options |
|---|---:|---:|---:|
| None | 53/100 | 21/40 (52.5%) | 20/40 (50%) |
| SFT on 100 official questions | 91/100 | 27/40 (67.5%) | 26/40 (65%) |
| RLVR on the same100 questions | 80/100 | 27/40 (67.5%) | 25/40 (62.5%) |

Both selected epoch3 on development data: SFT23/25, RLVR22/25, versus original15/25. The selected adapters each saw300 question presentations (three passes,75 updates); RLVR sampled1,200 answer letters. Total exploration took168.2s for SFT (ten epochs) and181.1s for RLVR (eight epochs plus a partial ninth), including development checks. More training reduced development accuracy. This is a useful early-stopping lesson.

Original-order test: SFT15 corrections and9 regressions; RLVR11 corrections and5 regressions. Both are +6 answers, but neither is consistently better on every question. The original model favors A (28/40 predictions); SFT favors C (22/40), so answer-position bias remains despite shuffled training options. Rotated evaluation still improves, but is not an independent test set.

Estimated completed-worker compute: SFT **$0.05652**, RLVR **$0.05522**, initial v1 screen **$0.00847**; total **$0.12022**, excluding builds/startup/storage. No failed or interrupted GPU workers. Both saved adapters passed eight fresh-base reload prediction checks; peak allocated GPU memory was approximately7.8–7.9GB. All18 repository tests pass; v2 rebuild is byte-for-byte identical, and saved answer keys, scores, split membership and RLVR rewards/advantages were independently checked.

[Every before/after choice, including regressions](prawko_example_results.md). This is a modest pilot improvement, not a dramatic exam-passing claim. For a workshop, use it to compare SFT and RLVR; the six-word task remains the stronger visible RLVR success.

## Data

The [Ministry of Infrastructure catalogue](https://www.gov.pl/web/infrastruktura/jak-uzyskac-prawo-jazdy) links the [July 2026 XLSX](https://www.gov.pl/attachment/a5c6c329-28a5-4274-a1a8-e2813f0a51bd). Of 3,526 rows, 165 have category B, an empty Media field, three nonempty options and an A/B/C key. This excludes yes/no questions, images, videos and other licence categories. English translations are retained for a future English version; current training uses Polish.

`datasets/prawko-v2` contains the source hash, manifest and exact split: **100 train / 25 development / 40 test**. `prepare_prawko.py` groups similar question stems before splitting (maximum bidirectional SequenceMatcher similarity >= .72, connected components, seed20260908). This avoids obvious near-duplicate leakage, but it is a lexical heuristic: related facts can appear in different splits. Base-model pretraining exposure is unknown.

The older `prawko-v1` and its inference-only screen are preserved for the lab record. A test found direction-dependent similarity in the first implementation; v2 fixes it. All training comparisons use v2. Do not compare v1 baseline numbers directly against v2 results.

## Cheap, ordinary scripts

Baseline only:

```bash
uvx --from modal==1.5.0 modal run prawko_modal.py --method screen
```

Two separate fresh adapters, sequentially on one L4:

```bash
uvx --from modal==1.5.0 modal run prawko_modal.py --method compare --epochs 10 --max-seconds 180
```

Choose `--method sft` or `--method rlvr` to run just one. Default model is pinned **Qwen/Qwen3.5-0.8B**, revision `2fc06364715b967f1860aea9cf38778875588b17`. Each training worker now has a 1050-second hard timeout (~$0.30 requested compute ceiling), no configured retries and a three-minute training cap in the command above. Loading/evaluation/reload are additional; training can finish earlier after ten epochs. Builds/startup/storage are excluded from compute estimates. No teacher or judge API is used.

On a supported local NVIDIA GPU:

```bash
uv run prawko.py --method sft --epochs 10 --max-seconds 180 --device cuda --output runs/my-prawko-sft
uv run prawko.py --method rlvr --epochs 10 --max-seconds 180 --device cuda --output runs/my-prawko-rlvr
```

CPU is the local default; CPU/MPS training has not been benchmarked. No notebook or coding assistant is required. `prawko.py.lock` pins dependencies. The Modal wrapper uses the same trainer. Small run records are copied back to `runs/`; weights stay in the `model-training-workshop` Modal volume under `/runs/RUN_NAME/adapter`.

The downloaded spreadsheet stays in ignored `data/prawko/`. Download it and rebuild the dataset into a new directory:

```bash
mkdir -p data/prawko
curl -fL https://www.gov.pl/attachment/a5c6c329-28a5-4274-a1a8-e2813f0a51bd -o data/prawko/source.xlsx
uv run prepare_prawko.py data/prawko/source.xlsx --output data/prawko-rebuilt
uv run --no-project -m unittest test_prawko -v
```

## What gets trained and measured

Both adapters start from the original model, with rank16/alpha32 LoRA, LR5e-5, batches of four questions and independently shuffled option order at each presentation. Neither adapter uses poetry, film dialogue or the other adapter.

- **SFT:** next-token cross entropy for the official correct letter over the full vocabulary. No supplied worked solutions.
- **RLVR:** sample four A/B/C actions per question from the current model's normalized three-letter distribution. Reward1 for the official correct letter, otherwise0. One on-policy REINFORCE update with a leave-one-out baseline; exact KL over the three actions to the frozen base, coefficient.01. This is a contextual-bandit form of RLVR, not multi-step reasoning or GRPO.

All before/after evaluations use exactly the same **constrained A/B/C argmax** from the final prompt-token logits, with the nonthinking chat template. This measures answer selection, not whether unconstrained generation obeys the requested format. Raw probability mass assigned to A/B/C is saved for inspection. No explanation is generated: answer text shown in the report comes from the official catalogue.

Checkpoints are selected on development accuracy, breaking ties with mean correct-answer probability; the initial model is eligible. The test set never selects the checkpoint. We also rotate test option positions to reveal answer-order sensitivity. Those are the same40 questions, not80 independent questions. Report training-set accuracy separately as a memorization measure. After saving, reload the adapter on a fresh base and check eight test predictions.

**This is not the full official driving exam**, and its percentage is not an official pass/fail result. One seed and40 held-out questions cannot establish robust generalization. A clear gain here would support this workshop exercise, not a claim of safe driving knowledge.

## Longer training comparison — completed

The completed follow-up used four times the time budget: **720 seconds / 40 epochs per method**, keeping the model, data, seed and learning rate unchanged. The wrapper now allows up to720s/40epochs and has a1050s worker timeout (~$0.30 requested compute ceiling per worker). Cheap defaults remain unchanged. Each run saves both a development-selected `adapter` and a `final_adapter`; final test results never select the checkpoint.

```bash
uvx --from modal==1.5.0 modal run prawko_modal.py --method compare --max-seconds 720 --epochs 40
```

The actual number of updates depends on worker speed and the time cap. These are fresh runs from the base, not resumed adapters with a reset optimizer. Same seed does not guarantee bit-identical training on different GPU workers.

Why a tie would be informative: in this three-action task, expected unregularized RLVR reward is simply the probability of the correct letter, `p(correct)`. Conditional SFT maximizes `log p(correct)`. For one example their gradients point in the same direction, with RLVR scaled by `p(correct)`; across examples this changes weighting, while sampling adds variance. Our SFT also optimizes the total probability mass of valid letters through its full-vocabulary loss, and RLVR includes reference KL. Neither recipe learns a multi-step reasoning strategy here. Longer training tests their learning dynamics; it does not guarantee a dramatic difference.

Audit saved runs without a GPU:

```bash
uv run verify_prawko.py runs/RUN_NAME
```


### Results of the longer run

Same **Qwen/Qwen3.5-0.8B** and100 official training questions; both start from the base. No poetry/film data. All scores are constrained A/B/C selections.

| Checkpoint | Train /100 | Dev /25 | Held-out /40 | Same test, reordered /40 |
|---|---:|---:|---:|---:|
| Original model, no workshop adapter | 53 | 15 | 21 | 20 |
| SFT, development-selected epoch3 | 92 | 23 | 28 | 25 |
| RLVR, development-selected epoch7 | 86 | 21 | 29 | 28 |
| SFT, final after12min | 100 | 20 | 28 | 30 |
| RLVR, final after12min | 91 | 20 | 25 | 24 |

**At the final checkpoints SFT leads by3/40 answers, or6/40 with reordered choices. With development selection, RLVR leads by1/40 and3/40 respectively.** This is a difference in behavior and learning dynamics, not strong evidence of a universally better method. The selected models differ in correctness on13 original-order questions: RLVR gets7 of those right, SFT6. Reporting only one checkpoint rule would conceal part of the result.

SFT spent721.75s training,725 updates/29epochs/2,900 presentations; selected75 updates/300 presentations. RLVR spent722.22s,569 updates/22complete epochs plus19batches/2,276 presentations; selected175 updates/700 presentations/2,800 sampled answers. Slower workers mean4x the time budget did not produce4x as many updates. Selected SFT is still an early checkpoint; its one-answer difference from P1 is not evidence that the extra training helped that selected adapter. First250 SFT batch IDs and option orders exactly match P1, but numerical training outputs diverged after the first update despite the same seed.

SFT worker estimate **$0.21885**; RLVR **$0.21267**. Additional completed-worker compute **$0.43152**, all prawko experiments combined **$0.55174**, excluding startup/builds/storage. Both workers completed normally. Selected adapters passed all8 fresh-base reload checks. Final adapters were saved and evaluated in memory, but were not separately reload-tested.

The interactive report plots development accuracy or correct-answer probability against epochs or minutes, marks selected checkpoints, and lets you filter actual test answers by corrections, regressions or SFT/RLVR disagreement. No test score selected a checkpoint. The same40 test questions have now been inspected across repeated experiments, so these are exploratory results, not a new independent confirmation set.

```bash
uv run prawko_learning_report.py runs/prawko-sft-1788861428320342529 runs/prawko-rlvr-1788862202341560425
uv run prawko_report.py runs/prawko-sft-1788861428320342529 runs/prawko-rlvr-1788862202341560425 --output prawko_long_results.md
uv run verify_prawko.py runs/prawko-sft-1788861428320342529 runs/prawko-rlvr-1788862202341560425
```
