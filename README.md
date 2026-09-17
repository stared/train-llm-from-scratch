# AI from scratch

A three-hour workshop: Polish training data → tokenization → pretraining → SFT → RLVR → evaluation. Run ordinary **uv scripts**, locally or on **Modal**. Codex and Claude are optional.

Start with the [workshop agenda](docs/workshop.md). Run all commands below from the repository root.

| Stage | Workshop material | What to open or run |
|---|---|---|
| 1. Data | [Polish Wikipedia and Wolne Lektury](docs/pretraining.md) | Inspect the corpus and split before training |
| 2. Tokenization | [Interactive BPE explorer](visualizations/tokenizer.html) | Open the HTML file in a browser; step through merges |
| 3. Pretraining | [Train from random weights](docs/pretraining.md) | `scripts/scratch_modal.py`; [measured results](results/pretraining-findings.md) |
| 4. SFT | [LLM robi prawko](docs/prawko.md) | Teach Qwen3.5-0.8B using official questions and answer keys |
| 5. RLVR | [The same Prawko task](docs/prawko.md) | Compare separate SFT and RLVR runs from the same base |
| 6. Evaluation | [Prawko learning curves](results/prawko-training.html) | Compare held-out answers, regressions, cost and checkpoint reload |

The scratch model and the pretrained model used for Prawko are different models. This workshop demonstrates both starting points. The measured Prawko comparison uses separate SFT and RLVR branches; it does not train SFT followed by RLVR.

## Start with Prawko

The prepared dataset is included. Install [uv](https://docs.astral.sh/uv/getting-started/installation/), set up Modal, then run the baseline or the three-minute-per-method comparison:

```bash
uvx --from modal==1.5.0 modal setup
uvx --from modal==1.5.0 modal run scripts/prawko_modal.py --method screen
uvx --from modal==1.5.0 modal run scripts/prawko_modal.py --method compare --epochs 10 --max-seconds 180
```

The pilot improved held-out answers from **21/40 to 27/40** with both methods, for about **$0.12** in estimated worker compute. Read the [actual before/after answers](results/prawko-example-results.md). These are 40 text-only questions, not a full driving-exam pass. Builds, startup and storage cost extra.

For local NVIDIA GPU commands, longer comparisons and verification, use the [Prawko guide](docs/prawko.md). Pretraining additionally requires [corpus preparation and upload](docs/pretraining.md); do that before the workshop.

## Optional exercises

- [Poetry SFT](docs/poetry.md): ordinary Polish prompts → 4–12 original lines from *Pan Tadeusz*. [Actual results](results/pan-tadeusz-qa-results.md).
- [RLVR with visible constraints](docs/rlvr.md): six-word stories, Countdown arithmetic and maze navigation. [Before/after outputs](results/rlvr-results.html).
- [Small-model choices](docs/models.md) and [starter routing/JSON examples](docs/notes/starter-examples.md).

## Where things live

| Folder / file | Contents |
|---|---|
| [`docs/`](docs/README.md) | Workshop guides; background and earlier proposals in `docs/notes/` |
| [`scripts/`](scripts/README.md) | Runnable trainers, Modal wrappers, data preparation and report tools; adjacent uv lockfiles |
| [`visualizations/`](visualizations/) | Standalone tokenizer explorer |
| [`results/`](results/README.md) | Saved comparisons, charts and conclusions |
| [`datasets/`](datasets/) | Small prepared training sets and source provenance |
| [`data/`](data/README.md) | Ignored local downloads, full corpora, token files and rebuilds |
| [`runs/`](runs/) | Recorded metrics, predictions and executed-source snapshots; weights ignored |
| [`research/`](research/) | Experiment plans, source manifests and cost records |
| [`config/`](config/) / [`assets/`](assets/) | Model registry, text assets and visualization template |
| [`tests/`](tests/README.md) | CPU checks for data splits, formatting and reward functions |
| [`LAB_NOTEBOOK.md`](LAB_NOTEBOOK.md) | Experiment history, costs and lessons |

Quick checks, without renting a GPU:

```bash
PYTHONPATH=scripts uv run --no-project -m unittest discover -s tests -v
uv run scripts/verify_prawko.py runs/prawko-*
```
