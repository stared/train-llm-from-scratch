# Teach a model a voice

The main fine-tuning exercise should produce an obvious change on new questions. The earlier routing/arithmetic runs are infrastructure checks; they are not the main workshop attraction.

**Rehearsal status:** minute-scale training and reload work, and Qwen learns the default output format. The tested bilingual outputs are not yet consistently good enough to promise a polished poet or comic assistant. English is more usable; Polish has substantial quality problems. Read [the lab notebook](LAB_NOTEBOOK.md) and the actual comparisons before choosing this as a headline demo.

Two experiments use ordinary questions as input:

- **Poetry:** a helpful answer in four rhyming lines, with Polish imagery inspired by *Pan Tadeusz*, plus English verse.
- **Wit:** short, original comic dialogue with the swagger and absurd metaphors of a Polish crime comedy. This uses original examples, not the screenplay of *Chłopaki nie płaczą*.

The training method is supervised LoRA fine-tuning on original question–answer pairs. The student receives only the question. The included datasets are authored workshop material, built by `uv run curated_data.py`; each has 32 Polish and 32 English examples. They contain no held-out questions. This is persona fine-tuning. Training directly on *Pan Tadeusz* would instead teach literary continuation; that is a different exercise and does not by itself teach an assistant to answer questions in verse. These short poems do not claim Mickiewicz's meter or literary quality.

There is also a synthetic-data generator for experimenting with style-prompt distillation: the teacher receives a style instruction, while the student sees only the question. **The first Gemma-generated poetry dataset was rejected after inspection:** four-line formatting was consistent, but many Polish answers had broken grammar, weak rhyme or factual errors. It is preserved in `runs/style-data-poetry-1788771080241515907`, and is not used by the default recipe. This is a useful data-quality exercise, not the recommended training set.

We compare the unchanged model, the unchanged model with an explicit style prompt, and the fine-tuned model without that prompt. All three use greedy decoding and the same 192-new-token cap; longer baseline explanations may be cut short. If prompting already solves your product problem, that is a useful result. The fine-tuning experiment asks whether the style becomes the default voice.

## Run it

Start with the included data; no generation call is needed:

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage train --style poetry --data-run poetry-v1 --model qwen3.5-4b --epochs 4 --max-seconds 600
uvx --from modal==1.5.0 modal run style_modal.py --stage train --style wit --data-run wit-v1 --model qwen3.5-4b --epochs 6 --max-seconds 300
```

Open `datasets/poetry-v1/train.jsonl` and `datasets/wit-v1/train.jsonl`. Check relevance, factual content, Polish grammar, rhyme and wit. Data authorship and SHA-256 hashes are recorded in each manifest.

Optional: generate a new candidate dataset. Review the outputs before deciding to train on them:

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage data --style poetry --languages both --max-seconds 300
```

Use the printed data run name in `--data-run` for a generated dataset. Training reads the actual style from the dataset manifest. Each call uses one L4. Training has a five-minute default limit checked after each update, excluding loading and evaluation; the overall function timeout is 20 minutes. The requested L4 + 2 CPU + 16 GiB compute estimate for that timeout is about $0.34, excluding startup, storage and any resource use above the allocation. No server is deployed.

Ask your own question of a saved adapter; this starts a short GPU job and exits:

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage chat --data-run TRAIN_RUN_NAME --prompt 'Why does coffee go cold?'
```

Build an offline page showing all evaluation outputs:

```bash
uv run style_report.py runs/TRAIN_RUN_NAME --output SHOWCASE.html
```

Compare fixed-seed sampled decoding without training again:

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage sample --data-run TRAIN_RUN_NAME
```

This evaluates the base, prompted base and saved adapter with temperature 0.7, top-p 0.8, top-k 20 and seed 42. The current sampler also uses repetition penalty 1.1, added for the film-dialogue experiment; the earlier saved poetry/wit probes used 1.0. Exact settings are saved in each result. It saves a new result directory. Read the whole comparison; selecting a lucky sample is not a reliable improvement. The sampled poetry check did not fix the observed quality problems.

On your own NVIDIA GPU, the same training code runs without Modal:

```bash
uv run style_workshop.py train --data-dir datasets/poetry-v1 --output runs/my-poet --model qwen3.5-4b --device cuda --epochs 4 --max-seconds 600
uv run style_workshop.py chat --adapter-dir runs/my-poet --output runs/my-question --device cuda --prompt 'Why does coffee go cold?'
```

Local CPU/MPS paths are selectable but not benchmarked. Modal training copies text results back to your laptop; adapters stay in the shared volume. Download the complete training directory if you want local inference, since inference reads both `style_result.json` and `adapter/`:

```bash
uvx --from modal==1.5.0 modal volume get model-training-workshop /runs/TRAIN_RUN_NAME ./downloaded-run
```

## Workshop exercise: 45–60 minutes

1. Predict which questions will expose the difference between a style prompt and learned style.
2. Review a dozen training answers. Edit weak examples and recompute the manifest hash explicitly if changing the dataset.
3. Train for a few minutes. While it runs, inspect the masked input/answer distinction and discuss what LoRA changes.
4. Compare all three outputs on unseen prompts. Look for useful content, genuine rhyme, natural phrasing and unwanted catchphrases—not just a decreasing loss.
5. Try to break the persona: request prose, ask for JSON, switch language, ask a technical question, or request a longer explanation. A default poetic voice can be entertaining and still be inappropriate for structured-output tasks.
6. Change one thing—data quality, model, or number of epochs—and record a new set of questions before rerunning.

The fixed eight questions include Polish and English, technical explanations, everyday mishaps, and a request to stop writing verse. They are a small inspection set, not proof that the model will *always* follow the persona.
