# AI from scratch: workshop preparation

Proposed four-hour English workshop: train a tiny GPT from random weights, fine-tune a small pretrained model, and verify the result.

Read [the research and workshop proposal](WORKSHOP_RESEARCH.md) for the Falenty material review, model shortlist, timed agenda, evaluation task, Modal cost estimates, and implementation acceptance gates.

**Main fine-tuning exercise: [teach a model a voice](SHOWCASE.md).** Train a model to answer ordinary questions in poetry, or with original comic wit. These minute-scale experiments compare the neutral model, an explicit style prompt, and a saved LoRA adapter without a style prompt. The short runs below remain useful setup checks.

The working [lab notebook](LAB_NOTEBOOK.md) records experiments, rejected attempts, insights, spending and next decisions. Open [the complete output comparison](SHOWCASE.html) to inspect the minute-scale trials. The current personas change format reliably but are not yet consistently strong creative writers, especially in Polish.

[New Pan Tadeusz Q&A dataset](PAN_TADEUSZ_QA.md): 500 ordinary Polish prompts paired with 4–12 original verse lines, including humorous modern setups. 450 training / 50 validation examples; [actual Qwen3.5-4B before/after results](pan_tadeusz_qa_results.md) from a six-minute fine-tune are now available.

There are now three ordinary Python fine-tuning examples and a thin Modal wrapper. See [model choices](MODEL_CHOICES.md) and [measured test results](TEST_RESULTS.md). The [RLVR workshop comparison](RLVR_SHOWCASE.md) tests six-word microfiction, Countdown arithmetic and maze navigation, with [actual before/after outputs](RLVR_RESULTS.html) and a [reward-design lesson](RLVR_REWARD_LESSON.md). The [older tiny RLVR pipeline](RLVR.md) works but did not improve measured accuracy.

From-scratch training now works with ordinary uv scripts and Modal. See [experiment conclusions and costs](PRETRAINING_FINDINGS.md), [interactive learning curves and samples](pretraining_results.html), and [Wikipedia preparation and commands](WIKI_SCRATCH.md). The [scratch v2 design](SCRATCH_V2.md) records the earlier design work; Falenty measurements there are historical references.

**Near-$10 Polish runs:** [results and literal examples](polish_dollar_results.md). Longer Wikipedia training improves loss but still invents facts; Wolne Lektury overfits after roughly 40 minutes. [Full learning curves](runs/polish-dollar-1788900395083493729/pretraining_results.html).

**Start cheaply on Modal.** Only the Modal client is needed on your laptop; GPU dependencies install in the remote image. Python 3.12 is the tested remote environment.

```bash
uvx --from modal==1.5.0 modal setup
uvx --from modal==1.5.0 modal run modal_app.py --model lfm2.5-350m --task routing --steps 20 --eval-size 8 --max-seconds 90
```

One invocation runs one model/task combination. Choose `routing`, `extraction`, or `polish`. Choose a model alias from [models.json](models.json), consulting the test results before assuming compatibility. Defaults use one L4 with a ten-minute remote timeout, no retries, and a 180-second training limit. The first build/download can take longer than the training itself. Training time limits are checked after each optimizer update; they exclude loading, evaluation and reload. The remote timeout is the overall backstop.

**Run without Modal.** On a machine with a supported NVIDIA GPU:

```bash
uv run finetune.py --model lfm2.5-350m --task extraction --device cuda --steps 40 --output runs/my-extraction
```

CPU and MPS are selectable through `--device`; their training paths are not yet benchmarked. CPU is the default for ordinary Python so it never silently rents hardware. Existing output directories are rejected to protect previous results. No notebook or coding assistant is required.

**What each example teaches.**

| Example | Input → output | Evaluation |
|---|---|---|
| `routing` | Support request → one of four documented queue codes | Exact code; validity scored separately |
| `extraction` | Order description → JSON containing id, item, quantity | JSON structure/types and exact field values |
| `polish` | Polish addition word problem → number | Exact numeric answer; output format scored separately |

These are original synthetic starter datasets, generated locally with no teacher/API fees. Training uses 128 examples; test wording differs, and extraction IDs / arithmetic number ranges are held out. Routing has only four semantic test templates, so repeated ticket IDs do not create independent evidence. These are pipeline and narrow behavior tests, not model rankings or matura evaluations. Inspect failed predictions as part of the exercise.

```bash
uv run examples.py extraction --size 3
uv run -m unittest -v
uv run report.py
```

**Artifacts.** Each completed run saves `result.json`, before/after/reloaded predictions, actual train/test data, a token/loss-mask example, loss history, and dependency versions. Modal copies these small files back into `runs/`; weights stay in a persistent volume to avoid unnecessary transfers. Every successful run checks finite loss, changed adapter weights and identical deterministic predictions after discarding the trained model and reloading a fresh base plus saved adapter. This reload occurs in the same Python process, not a separate process.

To download your adapter after a Modal run, substitute the printed run name:

```bash
uvx --from modal==1.5.0 modal volume get model-training-workshop /runs/RUN_NAME/adapter ./downloaded-adapter
uvx --from modal==1.5.0 modal volume get model-training-workshop /runs/RUN_NAME/tokenizer ./downloaded-tokenizer
```

The adapter needs the exact original model revision in `result.json`; it is not a standalone model. Checkpoint revisions and primary package versions are pinned. `environment.txt` captures all installed versions for each run.

**Budget discipline.** Start with 2–20 steps and eight evaluation cases. Only increase the update count after load/train/save/reload succeeds. BF16 LoRA avoids adding quantization tooling for these tiny runs. Use short completions, one GPU at a time, and inspect saved results without a GPU. Reported compute costs are runtime estimates at published rates, not billing receipts; builds, startup and persistent storage are additional. No background deployment is created.

[Selected before/after examples and the data they trained on](example_results.md).

**Full-book training:** [Pan Tadeusz continued pretraining](PAN_TADEUSZ.md) uses the complete Wolne Lektury literary text—all twelve books and the epilogue. [The screenplay search](SCREENPLAY_SEARCH.md) records the sources checked for *Chłopaki nie płaczą*; no verified full script was found.

**Supplied film dialogue:** [Chłopaki training](CHLOPAKI.md) uses the user's `datasets/chlopaki.md`, converted into 1,270 bidirectional dialogue examples. This is distinct from the earlier assistant-written comic dataset.

[Actual Polish before/after results](chlopaki_results.md) and [interactive comparison](CHLOPAKI_RESULTS.html): Qwen3.5-4B, all 1,270 examples trained, 10 min 51.5 s on one L4. Compare greedy, sampled and 25%-strength adapter outputs.

**Real exam questions:** [LLM robi prawko](PRAWKO.md) compares Qwen3.5-0.8B SFT and RLVR on 100 official Polish driving-theory questions. Both improved a 40-question held-out text-only subset from21/40 to27/40; [all labelled before/after choices](prawko_example_results.md). Total pilot worker estimate ~$0.12. This is not a full driving-exam pass claim.

**Longer prawko comparison:** [12-minute SFT vs RLVR learning curves](PRAWKO_TRAINING.html). Final SFT28/40 vs RLVR25/40; development-selected SFT28/40 vs RLVR29/40. [All selected and final answers](prawko_long_results.md). Additional worker estimate ~$0.43.
