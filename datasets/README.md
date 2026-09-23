# Datasets: model inputs

- `wiki-tokenizer.json`: saved 8,192-entry tokenizer, ready to use.
- `prawko-v2/`: 100 training, 25 development and 40 test driving-exam questions.
- `pan-tadeusz-qa-v1/`: 500 Polish prompts paired with original verse passages.
- `pan-tadeusz-full/`: source text for the optional poetry exercise.
- `local/`: large downloads and prepared pretraining corpora; gitignored. Used by the optional local preparation script. The main exercise prepares data directly in a Modal volume. `local/sejm-scratch-v1/` holds Sejm tokens for local training, prepared from `~/corpora/sejm.txt` or the published `sejm.zip`.

Other versioned datasets are retained for reproducing earlier experiments. Generated outputs belong in `runs/`; selected example outputs are in `results/`.
