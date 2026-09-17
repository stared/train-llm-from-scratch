# 1. Data and tokens

A language model learns to predict text from examples. We use literary text for pretraining; exam question–answer pairs come later for fine-tuning.

## Data

- **Wolne Lektury:** [library](https://wolnelektury.pl/) · [download](https://codebased.xyz/files/i/wolnelektury.zip), **123 MB compressed**. Historical snapshot; **5,263 training works / 287 MB text / 101 million tokens**. Not the complete current catalogue; includes some non-Polish works.
- **Polish Wikipedia:** [September 2026 dump](https://dumps.wikimedia.org/plwiki/20260901/), **2.73 GB compressed**. Training split: **9.28 GB text / 3.14 billion tokens**, with original Wikipedia markup.

Example literary text from *Pan Tadeusz*:

> Litwo! Ojczyzno moja! ty jesteś jak zdrowie:
> Ile cię trzeba cenić, ten tylko się dowie,
> Kto cię stracił. Dziś piękność twą w całej ozdobie

## Run

Start preparing the literature corpus. This single command downloads, tokenizes, checks and uploads it to your Modal account:

```bash
uv run scripts/prepare_pretraining.py literature
```

Wait for **Ready** before starting pretraining. It is safe to rerun; completed data is reused. While it runs, open another terminal and try tokenization below. Downloads stay in gitignored `datasets/local/`; no GPU is rented during preparation.

## Inspect tokens

[Byte-pair encoding (BPE)](https://huggingface.co/learn/llm-course/en/chapter6/5) starts with small pieces and repeatedly merges frequent adjacent pairs. Encoding applies those learned merges and maps the resulting pieces to integer IDs.

Our **8,192-entry byte-level BPE** was trained on a sample of 2,048 training articles, up to 8,192 characters each. The [precomputed tokenizer](datasets/wiki-tokenizer.json) is included; no corpus download needed to try it:

```bash
uv run scripts/tokenize_text.py --text "Ala ma kota. Kot ma komputer."
```

Example with our saved tokenizer:

```text
Before: Ala ma kota. Kot ma komputer.
Pieces: A | la | Ġma | Ġko | ta | . | ĠK | ot | Ġma | Ġkomputer | .
IDs:    33, 328, 641, 1234, 335, 14, 369, 502, 641, 8046, 14
Decoded: Ala ma kota. Kot ma komputer.
```

It prints the original text, pieces, IDs and decoded text. `Ġ` represents a space in the displayed vocabulary pieces; IDs decoded together recover the original text.

Inspect one or several UTF-8 text files (first 400 characters each), or train your own tokenizer on their full contents:

```bash
uv run scripts/tokenize_text.py datasets/pan-tadeusz-full/train.txt
uv run scripts/tokenize_text.py --train datasets/local/my-tokenizer.json datasets/pan-tadeusz-full/train.txt
uv run scripts/tokenize_text.py --tokenizer datasets/local/my-tokenizer.json --text "Litwo! Ojczyzno moja!"
```

A different tokenizer needs newly encoded training data and a new scratch model. For fine-tuning, keep the pretrained model's tokenizer.

Open our [BPE explorer](results/tokenizer.html): same paragraphs, colored token boundaries, merge steps and hover history. To rebuild it with your own example:

```bash
uv run scripts/tokenizer_visualization.py --text "Litwo! Ojczyzno moja!" --output datasets/local/my-tokenizer-view.html
```

Sources: [Hugging Face Tokenizers tutorial](https://huggingface.co/docs/tokenizers/quicktour) · [Cornell interactive BPE / WordPiece](https://www.cs.cornell.edu/courses/cs4782/2026sp/demos/bytepair/).

## Open the visualization

```bash
uv run scripts/view_results.py tokens
```

Move through merges and hover over tokens. This uses the included tokenizer and works without downloading the corpus.

## Try

Change the input text to your name, Polish text or emoji. Compare characters and tokens. If downloading is slow, continue to [fine-tuning](03-fine-tuning.md), whose small dataset is already included.

**Next:** [2. Pretraining](02-pretraining.md).
