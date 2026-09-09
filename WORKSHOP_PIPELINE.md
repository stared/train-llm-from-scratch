# Three-hour model-training workshop

Current scope, agreed 2026-09-09: an English workshop covering the complete core training pipeline, using Polish materials. The three-hour limit supersedes earlier four-hour agendas. Keep the 8,192-entry byte-level BPE tokenizer for this workshop; another vocabulary sweep is not required.

| Stage | Question | Exercise |
|---|---|---|
| Pretraining data | What should the model learn from? | Polish Wikipedia or historical Wolne Lektury; inspect, filter, deduplicate, split |
| Tokenization | How does text become input IDs? | Existing tokenizer versus training your own; explore actual BPE merges |
| Pretraining | How do random weights learn language? | Short next-token training run; compare saved longer-run checkpoints |
| SFT | How do examples teach desired behavior? | Prawko question and correct answer; poetry as an optional contrast |
| RLVR | How does a correctness signal train a model? | Prawko answer-key reward; inspect gains and failures |
| Benchmarking/testing | Does improvement generalize? | Fixed held-out questions, before/after comparison, cost and checkpoint reload |

Evaluation begins with the initial data split and baseline. Validation guides decisions; the final test set remains untouched by training and model selection. Save, reload and run inference during each exercise.

| Time | Activity |
|---|---|
| 0:00–0:10 | Pipeline overview, success criteria, test-data separation |
| 0:10–0:30 | Pretraining data |
| 0:30–0:50 | Tokenization and BPE explorer |
| 0:50–1:20 | Pretraining: live short run and saved longer-run results |
| 1:20–1:30 | Break |
| 1:30–1:55 | SFT on prawko |
| 1:55–2:25 | RLVR on prawko and comparison of learning signals |
| 2:25–3:00 | Benchmarking, failures, checkpoint reload, discussion |

Training runs fit within these blocks. Participants use ordinary uv scripts; a coding assistant is optional. Dataset preparation and uploads should be rehearsed before the workshop. Saved checkpoints provide a fallback for setup or GPU delays.

The scratch model and the existing model used for prawko are different models. Explain both entry points explicitly: random initialization for learning pretraining, and an existing pretrained/post-trained model for practical adaptation. Our tested prawko experiments compare separate SFT and RLVR branches from the starting model. They do not yet test SFT followed by RLVR.

SFT and RLVR are optional, complementary stages. SFT alone can be sufficient. SFT can prepare the model for RLVR; an already capable model can also receive RLVR directly. Starting with an instruction-tuned model inherits its previous post-training.

Prawko is the shared task, not evidence that RLVR always beats SFT. For a visibly large RLVR improvement over the starting model, the tested [six-word-story exercise](RLVR_SHOWCASE.md) improved constraint compliance from 1/32 to 32/32; it has no matched SFT comparison and does not establish better literary quality.

The matura project remains a hackathon extension. See [training for answer-key exams](EXAM_POSTTRAINING.md). The full participant walkthrough is still to be written and rehearsed.

References and artifacts: [tokenizer explorer](tokenizer_explorer.html), [pretraining findings](PRETRAINING_FINDINGS.md), [near-$10 Polish runs](polish_dollar_results.md), [Pan Tadeusz Q&A](PAN_TADEUSZ_QA.md), [token-frequency audit](research/scratch/token_frequency_audit.json).
