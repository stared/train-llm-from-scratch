# 1. Data and tokens

For pretraining, we turn text into token IDs and teach a model to predict the next token. Start with Wolne Lektury; Wikipedia is an alternative.

## What to expect

| Dataset / activity | Measured time | Hardware | Worker cost | Output |
|---|---:|---|---:|---|
| Wolne Lektury preparation | 3 min | CPU | $0.008 | 101M training tokens |
| Tokenizer explorer | Immediate | Your browser | $0 | Token IDs and merge history |
| Full Polish Wikipedia preparation | Not measured | CPU | Not measured | 3.14B training tokens |

## Wolne Lektury

[Wolne Lektury](https://wolnelektury.pl/) provides literary texts. We use a historical snapshot, not the complete current catalogue.

- [Download the historical snapshot](https://www.dropbox.com/scl/fi/xe53n90v40l9xuvodecq9/wolnelektury.zip?rlkey=z88vhfdl0cojsacqv5hu7w09u&dl=1): 123 MB compressed.
- Training split: 5,263 works, 287 MB of text, 101 million tokens.
- Some works in this snapshot are not in Polish.

## Polish Wikipedia

[Polish Wikipedia dump, September 2026](https://dumps.wikimedia.org/plwiki/20260901/).

- Download: 2.73 GB compressed.
- Training split: 9.28 GB of text, 3.14 billion tokens.
- Original markup is retained, including links, headings and templates.

## Prepare Wolne Lektury

To start, run:

```bash
modal run scripts/prepare_data_modal.py
```

Modal downloads the texts, converts them into token IDs using our saved tokenizer, and stores them in your Modal volume. Books are split into training, development and test sets before training. The large files stay in the cloud, without passing through your laptop or the workshop Wi-Fi.

Existing prepared data is checked and reused. Wait for **Ready** before [pretraining](02-pretraining.md). While it runs, try the BPE explorer below.

## Text → tokens

Byte-pair encoding (BPE) starts with small pieces and repeatedly merges frequent adjacent pairs. A trained tokenizer applies those merges and assigns each piece an integer ID.

Our tokenizer has **8,192 vocabulary entries**. It was trained on 2,048 Wikipedia training articles, using up to 8,192 characters per article. It is included at `datasets/wiki-tokenizer.json`.

## BPE explorer

Open the [interactive BPE explorer](results/tokenizer.html) in your browser:

```bash
uv run scripts/view_results.py tokens
```

**Click Edit text**, paste a paragraph, then **Show tokens**. Start with the full tokenization, then move the slider towards bytes. Colors show token boundaries; hover over a token to see its ID and merge history. Everything runs locally in your browser, without Modal or a corpus download.

## Optional: tokenize files or train a tokenizer

```bash
uv run scripts/tokenize_text.py --text "Ala ma kota. Kot ma komputer."
```

```text
Before: Ala ma kota. Kot ma komputer.
Pieces: A | la | Ġma | Ġko | ta | . | ĠK | ot | Ġma | Ġkomputer | .
IDs:    33, 328, 641, 1234, 335, 14, 369, 502, 641, 8046, 14
Decoded: Ala ma kota. Kot ma komputer.
```

`Ġ` represents a space in the displayed pieces. Decoding the IDs recovers the original text.

Inspect the first 400 characters of a text file:

```bash
uv run scripts/tokenize_text.py datasets/pan-tadeusz-full/train.txt
```

You can pass several text files. To train a new tokenizer on their full contents:

```bash
uv run scripts/tokenize_text.py --train datasets/local/my-tokenizer.json datasets/pan-tadeusz-full/train.txt
```

Then inspect its tokenization:

```bash
uv run scripts/tokenize_text.py --tokenizer datasets/local/my-tokenizer.json --text "Czy to jeszcze słowo, czy już token?"
```

Use the included tokenizer for the next exercise. Changing it requires encoding the training corpus again and training a new model. For fine-tuning, keep the existing model's tokenizer.

**Next:** [2. Pretraining](02-pretraining.md). If preparation is still running, you can start [3. Fine-tuning](03-fine-tuning.md) independently.

## Further reading

- [Hugging Face: how BPE works](https://huggingface.co/learn/llm-course/en/chapter6/5).
- [Hugging Face Tokenizers tutorial](https://huggingface.co/docs/tokenizers/quicktour).
- [Cornell: interactive BPE / WordPiece visualizer](https://www.cs.cornell.edu/courses/cs4782/2026sp/demos/bytepair/).
