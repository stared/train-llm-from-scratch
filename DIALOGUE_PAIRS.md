# Bidirectional dialogue examples

`dialogue_pairs.py` converts a supplied local text file into ordinary `prompt`/`answer` JSONL and equivalent chat `messages`. For adjacent lines A then B, it creates **A → B** and **B → A**, always using the standard `user` and `assistant` roles. Speaker names are metadata rather than part of the utterance.

Input format (original illustrative dialogue, not film quotations):

```text
Ada: My printer has joined a union.
Ben: Start negotiations with fresh paper.
Ada: It wants a four-day working week.

Celina: The server is asleep again.
Dawid: Check the logs before buying it coffee.
```

Blank lines separate scenes; each turn must have `Speaker: text`. Consecutive lines from the same speaker are merged. Single-speaker fragments cannot form reply pairs and are omitted. The converter never pairs across scene boundaries.

```bash
uv run dialogue_pairs.py my-dialogues.txt --output datasets/my-dialogues --source 'Description of the supplied source'
```

Outputs: `train.jsonl`, `validation.jsonl`, and a source/hash manifest. Splitting happens at scene-group level before bidirectional expansion. Scenes sharing an utterance stay together, preventing a quote or its reverse from leaking across train/validation. Exact normalized pairs are deduplicated. With only one connected group, no separate validation set is possible.

The training JSONL is compatible with `style_workshop.py`. Once there are at least 24 training examples:

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage train --data-run my-dialogues --model qwen3.5-4b --epochs 4 --max-seconds 300
```

The existing trainer runs its general persona probes; it does not automatically score `validation.jsonl`. Keep that file for a separate dialogue-reconstruction evaluation. Reverse pairs satisfy the requested two-way mapping, but may be unnatural conversational replies; their effect on chat quality should be inspected.

No film dialogue from the linked Wikiquote page was downloaded into this dataset, and no new GPU training was run. The converter is ready for a local dialogue text supplied by the user.

**Later supplied-file experiment:** `prepare_chlopaki.py` handles the headings, abbreviated speakers and unlabelled continuation lines in the user's `datasets/chlopaki.md`. See [CHLOPAKI.md](CHLOPAKI.md) for the actual 1,270-example dataset and training recipe.
