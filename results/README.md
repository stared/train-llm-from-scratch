# Measured results

Run `pnpm dev` from the repository and open **Reports** to browse these experiments.

[Latest full workshop check: timings, costs, curves and before/after answers](http://localhost:5173/reports#workshop-check.html).

[GPU, model and post-training comparisons](http://localhost:5173/reports#training-comparisons.html).

- [Wikipedia: training time, loss and cost](wikipedia-scaling.svg).
- [Fresh near-$10 Wikipedia runs](wikipedia-long-runs.svg).
- [Wikipedia: H100, H200 and B200](wikipedia-gpus.svg).
- [Wikipedia to the Polish Driving Licence Exam](scratch-exam-comparison.svg).
- [Longer Wikipedia pretraining: exam transfer across three seeds](scratch-exam-transfer.svg).
- [Wikipedia definitions: pretraining and question wording](wiki-qa-recall.svg).
- [Wikipedia definitions: fresh before/after SFT audit and example answers](wiki-qa-example-results.md).

Each comparison records the model, training data and evaluation setup.

| Workshop stage | Start here | More detail |
|---|---|---|
| Pretraining | [Current flow check](http://localhost:5173/reports#workshop-check.html) | [Learning curves](http://localhost:5173/reports#pretraining-results.html), [near-$10 Polish runs](polish-dollar-results.md) |
| Polish Driving Licence Exam: SFT vs RLVR | [Repeated SFT/RLVR comparisons](http://localhost:5173/reports#training-comparisons.html) | [Pilot answers](prawko-example-results.md), [longer-run answers](prawko-long-results.md) |
| Poetry SFT | [Pan Tadeusz Q&A](pan-tadeusz-qa-results.md) | [Other style trials](http://localhost:5173/reports#showcase.html) |
| RLVR constraints | [Before/after outputs](http://localhost:5173/reports#rlvr-results.html) | [Scores](rlvr-results.md), [reward-design lesson](rlvr-reward-lesson.md) |

Earlier results remain here for comparison, including unsuccessful experiments. Raw predictions, metrics and source snapshots stay locally in gitignored `runs/`; they are not included in a fresh clone. Rebuilding reports from those records requires the original runs. See the [`LAB_NOTEBOOK.md`](../LAB_NOTEBOOK.md) for experiment history.

Report-generation scripts write their outputs here.

[Mac fine-tuning: MPS and MLX measurements](macos-fine-tuning.md).
