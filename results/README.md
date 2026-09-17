# Measured results

These files contain saved experiments, not freshly generated promises. Each comparison identifies the model, training data and evaluation setup.

| Workshop stage | Start here | More detail |
|---|---|---|
| Pretraining | [Findings and costs](pretraining-findings.md) | [Learning curves](pretraining-results.html), [near-$10 Polish runs](polish-dollar-results.md) |
| Prawko SFT vs RLVR | [Learning curves](prawko-training.html) | [Pilot answers](prawko-example-results.md), [longer-run answers](prawko-long-results.md) |
| Poetry SFT | [Pan Tadeusz Q&A](pan-tadeusz-qa-results.md) | [Other style trials](showcase.html) |
| RLVR constraints | [Before/after outputs](rlvr-results.html) | [Scores](rlvr-results.md), [reward-design lesson](rlvr-reward-lesson.md) |

Earlier results remain here for comparison, including unsuccessful experiments. Raw predictions, metrics and source snapshots stay locally in gitignored `runs/`; they are not included in a fresh clone. Rebuilding reports from those records requires the original runs. See the [`LAB_NOTEBOOK.md`](../LAB_NOTEBOOK.md) for experiment history.

Open HTML files directly in a browser. Report-generation scripts write here by default; use `--output` or `--output-dir` to save a separate comparison.
