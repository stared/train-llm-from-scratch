# From-scratch experiments: workshop recipes

**Latest Polish-only follow-up:** [longer Wikipedia curves](wikipedia-scaling.svg) and [training comparisons](training-comparisons.html), including separate million-token evaluations. The September8 experiments below are historical results.

**Follow-up:** [Near-$10 Polish experiments](polish-dollar-results.md) tested four 2h13m runs. Wikipedia improved but remained factually unreliable; Wolne Lektury overfit. The ten-minute experiments below are the earlier workshop comparison.

Measured on 2026-09-08. **Use 30M + TinyStories for the clearest readable-text demo; 30M + Wolne Lektury for Polish literary style; full Wikipedia for learning markup and examining factual failure.** All models start from random weights. None uses a pretrained language model, SFT, or RLVR. These are continuation models, not assistants.

Fourteen new ten-minute runs completed in parallel batches, alongside diagnostics of the two earlier five-minute baselines. GPU experimentation finished in about 56 minutes, within the 90-minute allowance. Training was configured for 600 seconds; early runs recorded 606–623 seconds because a periodic evaluation crossed the boundary. That scheduling issue is fixed: later runs finish the timed loop at 600 seconds. Evaluation, saving, and fresh-process reload add roughly 45–100 seconds, or 246 seconds for the slow 291M case.

## What to run

| Corpus | Model / GPU | Timed training | Whole worker | Compute estimate | Visible result |
|---|---|---:|---:|---:|---|
| TinyStories subset, English | 10.24M / L4 | 10 min | 10.83 min | $0.184 | Readable sentences and story shape; logic often drifts |
| TinyStories subset, English | 29.89M / H100 | 10 min | 10.99 min | $0.764 | Best readable short-story samples in this comparison |
| Historical Wolne Lektury | 29.89M / H100 | ~10 min | 10.90 min | $0.758 | Dialogue and verse emerge; grammatical and logical errors remain |
| Full Polish Wikipedia markup | 10.24M / L4 | 10 min | 11.27 min | $0.192 | Cheapest Polish baseline; recognizable markup, unreliable facts |
| Full Polish Wikipedia markup | 29.89M / A100-40GB | ~10 min | 11.67 min | $0.452 | Useful middle budget; held-out loss 1.853 |
| Full Polish Wikipedia markup | 29.89M / H100 | ~10 min | 11.16 min | $0.776 | Better held-out loss 1.714; factual continuations still wrong |

Costs include configured GPU + 2 CPU cores + 16 GiB RAM during the measured worker. They are estimates, not invoice amounts; build/startup and storage are excluded. Rates were checked against [Modal pricing](https://modal.com/pricing). At these rates, spending $10 on one L4/H100 run would imply hours, so it is a poor target for this workshop. **A roughly $1 budget already covers the strongest tested ten-minute recipe.** No claim is made about an untested ten-minute $10 multi-GPU recipe.

The current session's completed training workers total **$8.3059**, inference-only checks **$0.0194**. Two stopped apps have a separate conservative resource-cost upper bound of **$0.9577**; including that bound gives **$9.2830**, before excluded overhead. Original five-minute baselines cost another $0.1994 before this session. See [machine-readable accounting](../research/scratch/experiment_costs.json). All scratch apps were checked as stopped with zero tasks.

## Actual generated examples

Examples below are selected illustrations, not aggregate quality measurements. Complete outputs, failures, initialization samples, and intermediate checkpoints are in [the interactive report](pretraining-results.html) and [all example results](pretraining-example-results.md). Generated EOD separates documents; these excerpts stop at the first EOD or an indicated sentence boundary. Raw outputs are preserved.

**ScratchGPT-30M, trained from random weights on the English TinyStories subset, ten minutes, $0.764.** Run `scratch-tiny-30m-1788884529630737279`, development-selected checkpoint. Prompt: `When the rain stopped,`

> the little bird flew out of the cage and into the air. He flew to a big tree and said, "This is a nice place to settle. There is nothing to be scared of."
>
> He saw some delicious berries and hopped along to them. He ate and ate until he was full. Then he rested in the tree and dreamt all day.
>
> The little bird was so happy and content. He had a lovely place to settle.

Same model, prompt `One day, a little boy`:

> named Tim went to the park with his mom. They brought a big box to unpack it. Tim was very excited to see what was inside the box. He helped his mom open it and found a shiny coin.
>
> Tim showed the coin to his mom and said, "Look, Mom! I found a coin in the box!" His mom smiled and said, "That's great, Tim! Let's find something else to play with." They found a ball and played with it all day. They had so much fun at the park that day.

This model still makes conspicuous mistakes: another output starts “Lily found a stick that looked like a stick,” then drifts between a stick, spoon, and broken jar. The improvement is readability, not consistently sound reasoning.

**ScratchGPT-98M, trained from random weights on historical Wolne Lektury, ten minutes, $0.765.** Run `scratch-wl-100m-1788883120565596531`, development-selected checkpoint. Prompt: `— Nie wiem,`. Opening excerpt:

> co, jeśli wolisz.
>
> — Ale to dopiero byłoby sensu — zaśmiała się. — Przy tym nie potrafiłbym tak zrobić.
>
> — Czy taka jest wola Homera?
>
> — Tak.
>
> — Zatem to już jest wola Homera.

The prose has learned a literary voice, while “byłoby sensu” and the dialogue logic expose its limits. The cheaper 30M/H100 literature model has slightly better held-out loss than 98M, so 30M is the default recommendation.

## What did not solve factual accuracy

On the **same full-Wikipedia held-out windows**, test loss improved from 2.400 for the original five-minute 30M/L4 model to 1.714 for ten-minute 30M/H100 and 1.701 for 98M/H100. The 291M model was worse at 1.867 and more repetitive. This compares practical recipes with different hardware, context, and throughput, not an isolated architecture ablation.

Despite that improvement, free continuations still misidentify Warsaw: the full-Wiki 98M model calls it a parish; the filtered-opening 98M model calls it a railway station. The latter ranks 8/10 hand-authored factual candidates correctly, yet generates those wrong answers. Candidate ranking is not equivalent to factual generation. Alternate prompt formats also failed; see `prompt_format_check.json` in the original 30M, full-Wiki H100 30M, and filtered 98M run directories.

The 10,000 popular-article opening experiment is a particularly clear **overfitting demonstration**. Its 30M model trained for ten minutes on a 4.54M-token pool, presenting 424M tokens through random windows. Final train loss was 0.133, but dev loss 5.474 and test loss 5.304. Development selection retained step 1,357 instead of the final step 12,948; even that checkpoint had test loss 2.898 and poor prose. Popularity alone did not create a good tiny curriculum.

## Data and limitations

- **Full Wikipedia:** official Polish snapshot 2026-09-01, original namespace-zero wikitext including redirects; 3.140B training tokens. New 8,192-token byte BPE trained on training articles only.
- **Filtered openings:** original 200–4,096-character lead substrings from nonredirect articles at least 4,000 characters long; 177.1M training tokens. Markup retained, original splits preserved, no targeting of evaluation entities.
- **Popular openings:** top 10,000 eligible titles by distinct incoming links from training articles; 9,914 training leads. Only 40 dev and 46 test leads, so the validation sample is small. No named entities manually inserted.
- **Wolne Lektury:** local copy of the historical Falenty archive, not the complete current catalogue. 5,263 nonempty training bodies, 101.3M tokens, shared Wiki BPE. Canonical-URL/body grouping limits exact leakage; anthology/part overlap can remain. Some source texts are not Polish.
- **TinyStories:** existing synthetic English stories from [the official dataset](https://huggingface.co/datasets/roneneldan/TinyStories), first of four training Parquet shards, pinned revision `f54c09fd23315a6f9c86f9dc80f725de7d8f9c64`; 529,875 training stories / 118.1M tokens. New English 8,192-token BPE. Official validation was deduplicated, exact training overlaps removed, then split into dev/test. CDLA-Sharing-1.0 licence; no new synthetic generation was purchased.

All downloads, prepared data, and verification manifests remain under visible, ignored `data/` in this repository. Local weights live under ignored `runs/*/*.pt`. Reproducible code, metrics, source snapshots, and reports remain shareable.

One seed per recipe; fixed 16,384-token loss windows; ten curated factual probes, not a broad benchmark. Losses across different corpora or tokenizers must not be ranked against each other. The report separates these corpora and shows a separate common full-Wiki loss for filtered models. Sampling uses temperature 0.8, top-k 50 and fixed seeds. There was no human blind scoring or semantic memorization audit.

## Reproduce one recipe

Use the already prepared dataset on Modal volume `model-training-workshop`; preparation and upload should happen before the live session. This command starts **one** training worker:

```bash
uvx --from modal==1.5.0 modal run scripts/scratch_recipe_modal.py --recipe stories --max-seconds 600
```

Other presets: `stories-cheap`, `literature`, `wiki`, `wiki-cheap`, `popular-wiki`. The single-recipe wrapper uses the tested shared worker; its CLI import was checked, but that new wrapper was not charged for an additional training rerun. Matrix wrappers preserve the exact completed experiment launches.

Ordinary NVIDIA GPU equivalent for 30M TinyStories:

```bash
uv run scripts/train_scratch.py --data data/tinystories-v1 --size 30m --device cuda --context 512 --batch-size 64 --warmup-steps 100 --eval-interval 300 --max-seconds 600 --output runs/my-stories
uv run scripts/sample_scratch.py runs/my-stories --device cuda --output runs/my-stories/samples-reloaded.json
```

For Wiki/literature, change `--data` to `datasets/local/wiki-scratch-v1` or `datasets/local/wl-scratch-v1`. Cheap 10M recipes use context 256, batch 32 and 20 warmup updates. Architecture is a small causal Transformer with RMSNorm, RoPE, SwiGLU, tied embeddings and SDPA; AdamW, BF16 autocast, cosine decay, gradient clipping, no compilation. Scripts pin dependencies and can run through uv.

Regenerate reports with `uv run additional/scripts/scratch_long_report.py --include-baselines`; audit artifacts with `uv run scripts/verify_pretraining.py`. `--require-weights` additionally checks local checkpoint presence. Actual GPU jobs separately verified exact fresh-process sampling equality after checkpoint reload.
