# Pretraining: text → a small language model

## Data

**Polish Wikipedia:** September 2026 dump, 2.73 GB compressed, original markup retained. Prepared files live in `data/wiki-scratch-v1/`.

Excerpt from the AWK article in our training data:

```text
{{Język programowania infobox
 |nazwa          = AWK
 |logo           =
 |data           = [[1977]]
```

Alternative: **Wolne Lektury**, Polish literary texts. Local source: `data/scratch-corpora/falenty-wl/`.

## Tokens

Open the [BPE explorer](../visualizations/tokenizer.html). Move through merges; hover over a token for its ID and history.

Our byte-pair encoding (BPE) tokenizer has **8,192 entries**, trained on Wikipedia. You can train your own tokenizer or reuse an existing one.

## Train

**Randomly initialized generative pretrained transformer (GPT)**, trained to predict the next token. Uses prepared Wikipedia tokens on Modal (one-time preparation below).

```bash
modal run scripts/scratch_modal.py --size 10m --max-seconds 300
```

Then change `10m` to `30m` and compare. Each run trains for about five minutes; loading and evaluation add time.

Watch **loss, generated text, tokens processed and cost**. Model settings: 6 vs 8 layers, context 256, same 8k tokenizer.

Measured: about **$0.10 per run** in worker compute. The 10M model had lower test loss in this short comparison; both learned markup but invented facts.

[Compare saved text and curves](../results/pretraining-results.html). New run records appear in `runs/`; weights stay on Modal. Give these models text to continue, not chat questions.

<details>
<summary>Prepare Wikipedia data (once, before training)</summary>

Skip this if the prepared corpus is already in your Modal volume.

```bash
uv run scripts/download_scratch_corpus.py --source wikipedia-pl-20260901 --download
uv run scripts/prepare_wiki_scratch.py --stage extract
uv run scripts/prepare_wiki_scratch.py --stage tokenize
modal volume create model-training-workshop
for file in train.bin dev.bin test.bin tokens.json tokenizer.json; do
  modal volume put model-training-workshop "data/wiki-scratch-v1/$file" "/datasets/wiki-scratch-v1/$file"
done
```

If the volume already exists, skip the create command. Downloads and prepared files stay in gitignored `data/`. Preparation runs locally on CPU.

</details>
