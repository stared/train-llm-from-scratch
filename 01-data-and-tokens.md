# 1. Data and tokens

For pretraining, we turn text into token IDs and teach a model to predict the next token. **In this workshop, we use Wolne Lektury. You do not need to download any dataset to your laptop.** The preparation command below handles the download and processing in Modal. Wikipedia is described only for context; we will not work with that dataset.

## What to expect

| Dataset / activity | Measured time | Hardware | Worker cost | Output |
|---|---:|---|---:|---|
| Wolne Lektury preparation | 3 min | CPU | $0.008 | 101M training tokens |
| Tokenizer explorer | Immediate | Your browser | $0 | Token IDs and merge history |

## Wolne Lektury

[Wolne Lektury](https://wolnelektury.pl/) provides literary texts. This is our workshop dataset. Modal fetches the snapshot automatically; the link below identifies the source, so you do not need to download it yourself.

- [Source snapshot](https://www.dropbox.com/scl/fi/xe53n90v40l9xuvodecq9/wolnelektury.zip?rlkey=z88vhfdl0cojsacqv5hu7w09u&dl=1): 123 MB compressed.
- Training split: 5,263 works, 287 MB of text, 101 million tokens.
- Some works in this snapshot are not in Polish.

## Polish Wikipedia — context only

The [Polish Wikipedia dump from September 2026](https://dumps.wikimedia.org/plwiki/20260901/) shows how much larger another training dataset can be. **We will not use it in this workshop. No download is needed.**

- Archive size: 2.73 GB compressed.
- Training split: 9.28 GB of text, 3.14 billion tokens.
- Original markup is retained, including links, headings and templates.

## Prepare Wolne Lektury

To start, run:

```bash
modal run scripts/prepare_data_modal.py
```

Modal downloads the texts, converts them into token IDs using our saved tokenizer, and stores them in your Modal volume. Books are split into training, development and test sets before training.

<details>
<summary style="color: #8b1e2d; font-size: 1.15em; cursor: pointer;"><strong>Click to expand: Why are there three datasets?</strong></summary>

We split the Wolne Lektury books into three separate groups. Each group has a different job:

- **Training set:** the practice material. The model predicts the next tokens, checks its mistakes and updates its weights using these texts.
- **Development set (dev):** the progress check. During training, we measure prediction loss on these separate texts without updating weights. Our script keeps the model version with the lowest development loss. This is the **best checkpoint**; it may come before the final training step.
- **Test set:** the final assessment. We measure the selected model on another separate group of texts. Test results do not decide which checkpoint to keep.

Why separate them? A model can improve on its practice material without improving on other books. Development and test results help us check whether it learned patterns that also work on text it did not train on.

</details>

Wait for **Ready** before [pretraining](02-pretraining.md). While it runs, try the BPE explorer below.

## Text → tokens

**Watch: how a tokenizer works** — 3 min 36 s, English question-and-answer narration with on-screen explanations and subtitles.

This video shows how our tokenizer was trained on **2,048 Wikipedia training articles**, using up to **8,192 characters per article**, to build an **8,192-entry vocabulary**. It then shows how we use that saved tokenizer on Wolne Lektury. You do not need to train the tokenizer or download Wikipedia yourself.

https://github.com/user-attachments/assets/99bce2a0-4c99-462d-bd85-bd31b27c2de0

[Open or download the tokenizer video](https://github.com/user-attachments/assets/99bce2a0-4c99-462d-bd85-bd31b27c2de0).

Byte-pair encoding (BPE) starts with small pieces and repeatedly merges frequent adjacent pairs. A trained tokenizer applies those merges and assigns each piece an integer ID.

Our tokenizer has **8,192 vocabulary entries**. It was trained on 2,048 Wikipedia training articles, using up to 8,192 characters per article. It is included at `datasets/wiki-tokenizer.json`, ready to use with Wolne Lektury. You do not need the Wikipedia dataset to use this saved tokenizer.

## BPE explorer

Open the visualization and select **Tokenization**:

```bash
pnpm dev
```

Edit the colored text directly. Compare the workshop tokenizer with GPT-4 (`cl100k_base`), GPT-4o (`o200k_base`), or your own byte-level BPE `tokenizer.json`. Hover over a token for its ID. Use the slider to undo merges with the workshop tokenizer.

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

Polish has many inflected word forms. A whole-word vocabulary needs many entries to cover them; character tokens use a smaller vocabulary but produce longer sequences. BPE uses reusable pieces of words and can also learn frequent pieces of markup.

**Next:** [2. Pretraining](02-pretraining.md). If preparation is still running, you can start [3. Fine-tuning](03-fine-tuning.md) independently.

## Further reading

- [Hugging Face: how BPE works](https://huggingface.co/learn/llm-course/en/chapter6/5).
- [Hugging Face Tokenizers tutorial](https://huggingface.co/docs/tokenizers/quicktour).
- [Cornell: interactive BPE / WordPiece visualizer](https://www.cs.cornell.edu/courses/cs4782/2026sp/demos/bytepair/).
- [Fully Character-Level Neural Machine Translation](https://arxiv.org/abs/1610.03017) — translation using characters instead of word or subword segmentation.
- [Shannon, A Mathematical Theory of Communication (1948)](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) — section 3 illustrates statistical models of text with character and word sequences.
