# Local training data

Large data files live in this visible folder and are gitignored. This README is versioned.

- `scratch-corpora/wikipedia-pl-20260901/`: complete downloaded Wikipedia XML/BZ2 archive.
- `scratch-corpora/falenty-wl/`: checksum-verified historical Wolne Lektury ZIP.
- `wiki-scratch-v1/`: extracted wikitext JSONL, tokenizer, train/dev/test token binaries and manifests.

See [workshop/pretraining.md](../workshop/pretraining.md) for preparation and training commands. Small curated workshop datasets remain in `datasets/`; experiment outputs remain in `runs/`. Only internal tool caches use `.cache/`.
