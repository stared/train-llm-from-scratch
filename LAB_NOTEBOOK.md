# Workshop preparation lab notebook

**Current workshop scope (2026-09-09): three hours.** See [workshop contents](README.md) and [answer-key exam training](additional/notes/exam-posttraining.md). Earlier four-hour plans remain historical notes. Keep the 8k tokenizer; use prawko for the SFT/RLVR comparison. Matura remains a hackathon extension.

Maintained during experiments. Dates are Europe/Warsaw. This is the working record of hypotheses, results, failures, costs and next decisions; the learner-facing instructions live in [README](additional/notes/starter-examples.md) and [SHOWCASE](results/showcase.md).

## Brief and constraints

- Four-hour workshop, taught in English, preparing participants for Warsaw Model Trainers. Reference material: `reference/falenty-gpt-2026` (read-only reference).
- Train a tiny model from random weights, then adapt a small pretrained model; include RLVR. Ordinary scripts must work without a coding assistant or notebook. Use `uv run` / `uvx`.
- Modal is the preferred rehearsal environment. Use one GPU at a time, bounded runs, cached weights and reusable datasets. Be explicit about measured runtime versus estimated cost.
- **User correction, September 7:** seconds-long training is adequate only for checking plumbing. The main examples should train for **1–10 minutes** and visibly change behavior. Suggested personas: poetry inspired by *Pan Tadeusz*, or the wit of *Chłopaki nie płaczą*.
- Current implementation uses bilingual Polish/English examples and English instructions. The comic dialogue is original, not a copied screenplay. The poetry exercise is question → verse, not continued pretraining on the full book.

## September 6–7: infrastructure checks

Purpose: verify load → tokenize → LoRA update → save → fresh base plus adapter reload before renting longer jobs. These are narrow synthetic tasks, **not the headline workshop exercises**.

| Model / task | Updates | Strict before → after | Training | Timed remote | Estimated compute |
|---|---:|---:|---:|---:|---:|
| LFM2.5-350M / routing | 20 | 2/8 → 6/8 | 3.86 s | 29.41 s | $0.0078 |
| LFM2.5-350M / extraction | 40 | 0/8 → 8/8 | 9.84 s | 42.23 s | $0.0112 |
| LFM2.5-350M / Polish arithmetic | 40 | 0/8 → 8/8 | 10.48 s | 35.16 s | $0.0094 |
| Qwen3.5-0.8B / routing | 20 | 2/8 → 5/8 | 39.00 s | 73.48 s | $0.0195 |
| LFM2.5-2.6B / extraction | 20 | 0/8 → 7/8 | 8.44 s | 88.53 s | $0.0235 |
| Gemma 4 E2B Instruct / routing, corrected EOS | 2 | 8/8 → 8/8 | 2.65 s | 47.54 s | $0.0126 |

All listed successful SFT runs had finite loss, changed adapters and matching deterministic predictions after reload. Gemma already solved the task; its run proves compatibility, not a fine-tuning gain. Extraction strict scoring rejects Markdown fences; ignoring surrounding fences makes the LFM350M baseline 1/8 instead of 0/8. Eight examples and narrow templates are not a benchmark.

Full artifacts and commands: [results/test-results.md](results/test-results.md). Successful timed calls including the superseded Gemma run and RLVR below total approximately **$0.119**. This is a requested-compute estimate, not an invoice.

### Failures and implementation lessons

1. Transformers 5 chat-template tokenization returned `BatchEncoding` by default. Explicit `return_dict=False` fixed the list-based training path.
2. The base Gemma checkpoint had no chat template. Switched to the instruction checkpoint `google/gemma-4-E2B-it`.
3. Gemma targets initially ended in generic `<eos>` rather than native `<turn|>`. Fixing the terminator changed first-step loss from about 8.08 to 0.0000035 on the already-solved routing task. Preserve the superseded result; do not interpret it as a valid training comparison.
4. An RLVR remote module imported an unmounted local Modal module. Container initialization retried even with function retries set to zero. Stopped the app explicitly and made the wrapper self-contained. Timeouts and retry settings do not bound every startup failure by themselves.
5. Keep generated artifacts and exact model revisions. A saved adapter is unusable without its original base model and correct tokenizer/template.

### RLVR proof of implementation

- Start from the LFM350M Polish arithmetic SFT adapter.
- On-policy REINFORCE with leave-one-out advantages; four sampled answers per group; exact numeric reward. No teacher answer is supplied to the policy-gradient loss. No KL term; deliberately small demonstration, not a production RL recipe.
- 12 groups / 48 rollouts yielded five mixed-reward groups and five actual updates. Harder held-out arithmetic stayed **4/8 → 4/8**. Training/rollouts took 2.05 s; remote execution 25.35 s; estimate $0.0067. Changed adapter and reload checks passed.
- **Conclusion:** working verifiable-reward learning signal, no demonstrated generalization improvement. Do not advertise “RL made the model smarter.” See [docs/notes/rlvr.md](additional/notes/rlvr.md) and [raw result](runs/rlvr-1788768609860683095/rl_result.json).

## September 7: replacing plumbing demos with persona fine-tunes

### Design

Hypothesis: supervised training on ordinary questions paired with stylistic answers can make that style appear without repeating a system prompt. Compare **neutral base**, **base with explicit style prompt**, and **fine-tuned model with only the ordinary question**. Prompting is a real competing solution, not a deliberately weak baseline.

Eight fixed evaluation questions cover DNS, Git force-push recovery, onion tears, missing a train, photosynthesis with an explicit prose request, rubber-duck debugging, Moon phases and a robot-vacuum apology. Five are Polish, three English. They are absent from training and from synthetic training-data generation. All variants use greedy decoding and 192 new tokens; long baseline answers can be truncated. Inspect content, language and style separately. Four lines are not proof of poetry or correctness.

### Experiment S1: small-model synthetic poetry data — rejected

- Teacher: Gemma 4 E2B Instruct, pinned revision in the manifest. Style instruction includes a six-line public-domain *Pan Tadeusz* excerpt and asks for original AABB quatrains.
- 128 question–answer pairs generated; **128/128 passed the four-line filter**. Generation 167.9 s, timed remote 196.6 s, estimated compute **$0.0558**.
- Manual reading found broken Polish, forced/nonexistent rhymes, language switching and factual errors. For 404, it wrote “forty-four” and described the server as silent. This dataset was **not used for training**.
- Insight: a cheap teacher can produce expensive-to-repair data. Format metrics can hide unusable content. Do not optimize a poetic RLVR example using line count as the sole reward.
- Artifacts: [accepted-by-surface-filter answers](runs/style-data-poetry-1788771080241515907/accepted.json), [execution](runs/style-data-poetry-1788771080241515907/execution.json), [annotated data review](additional/notes/data-review.md).

### Intervention: authored reusable data

- Added `scripts/curated_data.py`: 32 topic pairs × Polish/English = **64 examples per persona**. Both personas answer the same training questions.
- Original answers authored by the coding assistant, openly inspectable; not outputs from the rejected small-model teacher, not expert literary review. Poetry is short verse with some imperfect rhymes; no claim of Mickiewicz's meter. Comic dialogue uses original metaphors and practical advice.
- `uv run scripts/curated_data.py` builds versioned JSONL plus SHA-256 manifests. Training copies the exact dataset into each run. Hash, distinct IDs, both languages and held-out isolation checked locally.
- Files: [poetry-v1](datasets/poetry-v1/train.jsonl), [wit-v1](datasets/wit-v1/train.jsonl), [data provenance](datasets/README.md).

### Experiment S2: Gemma poetry on authored data — reject as showcase

Command:

```bash
uvx --from modal==1.5.0 modal run scripts/style_modal.py --stage train --style poetry --data-run poetry-v1 --epochs 12 --max-seconds 300
```

- One L4, BF16, LoRA rank 16 / alpha 32 / dropout 0.05, attention and MLP linear projections, learning rate 1e-4, effective batch four, answer-only loss.
- **192 updates, 283.1 s training (4.7 min)**, timed remote 392.4 s, peak allocated VRAM 11.53 GB, estimated requested compute **$0.1113**.
- Four-line rates: neutral 1/8, prompted 8/8, tuned 7/8. Adapter was nonzero and four fresh-base reload probes matched exactly.
- Training loss became nearly zero. Held-out outputs still had poor grammar and content. DNS was not explained; the rubber-duck answer wrongly recommended omitting setup and expected state. The base model also misread the Polish force-push question as physical exercise, and failed to explain onion tears correctly.
- **Conclusion:** learned output shape, not a useful poetic assistant. More steps are not the answer by themselves. Reject as the headline example and try a stronger multilingual base. Possible confounds: weak starting capability, only 64 examples, excessive repetition. These were not isolated in a controlled ablation.
- Artifacts: [result](runs/style-train-poetry-1788772024290826300/style_result.json), [all outputs](runs/style-train-poetry-1788772024290826300/finetuned.json), [offline comparison](results/rejected-gemma.html).

### Experiment S3: Qwen3.5-4B comic persona — working style change, mixed quality

Command:

```bash
uvx --from modal==1.5.0 modal run scripts/style_modal.py --stage train --style wit --data-run wit-v1 --model qwen3.5-4b --epochs 6 --max-seconds 300
```

- Same authored bilingual data structure and evaluation questions, six requested epochs, five-minute training cap. One L4, same adapter recipe.
- First download fetched two weight files in about 42 seconds.
- **62 updates, 304.4 s training (5.1 min)**; the time limit is checked after an update, so it overshot by one update. Timed remote execution 444.9 s, peak allocated VRAM 11.66 GB, estimated compute **$0.1262**. Four fresh-base reload probes matched.
- All 8 tuned answers were short; none of the neutral answers met that length criterion. The prompted baseline also produced 8/8 short answers. Length is not a humor score.
- English robot answer: “The robot says sorry and has filed the receipt under ‘delicious.’ Please do not feed it the family album; the vacuum is a tool, not a diner.” An amusing visible transformation, partly recombining a training metaphor. Moon explanation remained correct but plain; duck answer had a joke but little explanation.
- Polish remains weak: DNS answer was unhelpful, force-push metaphor malformed, missing-train answer nonsensical. The unchanged base also interpreted “pociąg uciekł” overly literally, so weak Polish starting capability is part of the problem. Prompting alone did not solve this; several prompted outputs were poor or switched language.
- **Conclusion:** successful minute-scale training and a usable English creative illustration, but not a strong bilingual comic assistant. Keep all examples visible. Do not describe it as matching the writing quality of the film.
- Artifacts: [execution](runs/style-train-wit-1788772457278552500/execution.json), [all tuned outputs](runs/style-train-wit-1788772457278552500/finetuned.json). Executed training/data source is also saved in the run directory.

### Experiment S4: Qwen3.5-4B poetry — format learned, literary quality unresolved

```bash
uvx --from modal==1.5.0 modal run scripts/style_modal.py --stage train --style poetry --data-run poetry-v1 --model qwen3.5-4b --epochs 4 --max-seconds 600
```

- Four epochs on the same 64 authored examples. **64 updates, 352.1 s training (5.9 min)**; timed remote 466.9 s, estimated compute **$0.1325**, peak allocated VRAM 11.76 GB. Four fresh-base reload probes matched.
- Reason for four epochs: S3's training loss was already about 0.1 after fewer than four passes. Avoid repeating S2's twelve-epoch memorization without evidence it helps.
- Four-line rates: base 0/8, prompted 7/8, tuned 8/8, including the explicit prose request. The English Moon answer rhymes and describes changing views of the sunlit Moon; the duck answer explains the mechanism but does not rhyme consistently. The robot answer rhymes but misses the requested apology. Polish grammar and rhyme remain poor. This establishes default verse-like formatting, not a stunning literary assistant.
- Artifacts: [execution](runs/style-train-poetry-1788773007763374852/execution.json), [all tuned outputs](runs/style-train-poetry-1788773007763374852/finetuned.json).

### Experiment S5: sampled decoding of saved Qwen poetry adapter — no quality rescue

- No new training. Reuse S4 adapter; evaluate all eight questions for neutral, prompted and tuned variants with seed 42, temperature 0.7, top-p 0.8, top-k 20 and a 192-token limit.
- Reason: greedy decoding was selected for reproducible reload checks, but creative-generation quality may differ with sampling. Qwen's [model card](https://huggingface.co/Qwen/Qwen3.5-4B) recommends sampling for non-thinking generation. This probe uses its temperature/top-p/top-k but does not implement its recommended presence penalty, so it is not an exact reproduction of all vendor settings.
- Fixed seed, all eight outputs retained. Sampling did not repair the Polish grammar or factual problems; English rhyme was inconsistent and the robot still did not actually apologize. No evidence here that decoding alone solves the showcase gap.
- Timed remote 65.0 s; estimate **$0.0184**. [Outputs](runs/style-sample-poetry-1788775402826086177/finetuned.json), [execution](runs/style-sample-poetry-1788775402826086177/execution.json).

### Experiment S6: sampled decoding of saved comic adapter — same quality limitation

- Same fixed decoding recipe and full evaluation set as S5. Reuses S3; no training. One L4.
- Timed remote 107.6 s; estimate **$0.0305**. English remains mostly coherent, though the duck answer is vague; the robot answer is amusing. Polish still contains invented/malformed words, e.g. “suborydem,” and weak explanations. Sampling does not change the decision: useful training mechanics, inconsistent writing quality.
- [All outputs](runs/style-sample-wit-1788775499306847844/finetuned.json), [execution](runs/style-sample-wit-1788775499306847844/execution.json).
- The complete [offline comparison](results/showcase.html) contains all eight prompts for both Qwen adapters under greedy and sampled decoding: 96 answers across the three variants. Language buttons filter the view; nothing is cherry-picked.

### Experiment S7: participant chat command — passed

- Fresh process loaded the saved comic adapter, asked an unseen English question about a printer that only works when nobody watches, and saved base/adapter answers. The command passed without new training.
- Tuned answer: “The printer is having a social anxiety attack. Check the paper tray, the power cord, and whether anyone has been feeding it secrets; then try a job in an empty room.” This demonstrates a comic voice, though some advice is intentionally absurd and not reliable troubleshooting.
- Timed remote 59.3 s, estimated compute **$0.0168**. [Saved chat](runs/style-chat-wit-1788775639728711213/chat.json).

## Accounting conventions

Earlier smoke jobs requested 8 GiB RAM. Style jobs request 16 GiB. Style estimates use timed remote seconds × ($0.000222 L4 + 2 × $0.0000131 CPU + 16 × $0.00000222 RAM). The 1200-second function timeout corresponds to about $0.34 of requested compute, excluding startup/storage and use above allocation; it is not a universal billing cap. [Modal rates](https://modal.com/pricing).

Completed style attempts so far: **$0.4916 estimated compute**, including the rejected teacher data and rejected adapter. Update this as new jobs finish. Cached models/adapters remain in the persistent `model-training-workshop` volume; no serving deployment is created.

## Open work and reusable lessons

- Find a creative fine-tune worth demonstrating; successful infrastructure and changed formatting are insufficient.
- Reuse reviewed data across participants; do not spend workshop time generating a weak dataset blindly.
- Keep the explicit style-prompt baseline. Fine-tuning may make a voice default without improving the best prompted answer.
- A request for prose is a useful stress test, but “always answers in poems” requires much broader testing than eight prompts.
- Saved artifacts, offline comparisons and a fresh-base reload matter more than a glossy loss curve.
- The Falenty scratch-model port is still separate future implementation work; historical measurements in the research brief are not new rehearsal results.

### Next experiment design, before renting more training

The requested “stunning” quality gate is still open. Do not spend on an epoch sweep of the same 64 examples. First prepare a small **base-model audition** with new Polish and English prompts: require a correct useful prose answer, then ask for a creative rewrite. A base that misunderstands the question cannot reliably recover that knowledge from a tiny style dataset.

If the audition succeeds, expand to varied, carefully reviewed examples (not repetitions), include genuine apologies and factual explanations, then save an early checkpoint as well as the final one. Evaluate on newly reserved questions; the current eight have now informed development decisions and are a development set, not an untouched final test. Separate three judgments: content preserved, style learned, and creative writing quality. This is the next useful intervention; more format-only scores would not resolve the present failure.

Final verification for this batch: five existing unit tests pass; new scripts compile; dataset hashes and held-out isolation checked; report contains 32 cards / 96 answers with escaped HTML; notebook/guide artifact links resolve.

## Selected examples and user feedback

The user considers the visibly different outputs useful workshop material, while acknowledging the quality limitations. Saved the Moon, robot-vacuum and Polish DNS comparisons in [results/example-results.md](results/example-results.md), alongside data provenance and sample training targets. Full saved baseline responses are included, with the generation-length cap disclosed. This reframes the current runs as useful demonstrations of behavior change; it does not change the recorded content-quality observations.

## Full-book request: Pan Tadeusz and film screenplay search

The user requested an actual full-book training example and a search for the *Chłopaki nie płaczą* screenplay.

### Experiment B1: full Pan Tadeusz — complete full pass, reload passed

- Downloaded the TXT directly from Wolne Lektury. Retained the unmodified source, publisher credits and SHA-256 hashes. Training text contains all twelve books and the epilogue, 441,326 characters / 68,896 whitespace-separated words. Front title/ISBN metadata and publisher footer are excluded from training. Book headings and summaries remain.
- `scripts/prepare_pan_tadeusz.py` checks every book heading and the epilogue before writing. Checked source/processed hashes, final verse retention, metadata exclusion and refusal of missing-book/missing-epilogue inputs.
- `scripts/corpus_workshop.py` performs raw-text continued pretraining with LoRA, no chat-template wrapping, no synthetic answers. Default LFM2.5-2.6B, rank eight / alpha 16 / dropout .05, learning rate 1e-4, batch two. Each block has up to 256 target tokens with one-token boundary overlap; the final partial block is retained. A coverage check confirms every token after the initial token is supervised exactly once per full pass.
- One L4, one epoch, 600-second training cap, 1200-second function timeout. The result records actual full-book coverage; a time cap can otherwise stop a run before the complete corpus has been seen.
- Four before/after probes: two original verse openings as raw completions, plus two chat prompts. These distinguish literary continuation from instruction-following transfer. The full work is used for training, so there is no held-out perplexity claim; the base may already know this public-domain book.
- Command: `uvx --from modal==1.5.0 modal run scripts/corpus_modal.py --max-seconds 600`.
- **333 updates, 61.3 seconds training**; all **665/665 blocks**, **169,997/169,997 next-token targets** seen exactly once. `full_corpus_seen=true`, coverage 100%. Corpus token count 169,998. Peak allocated VRAM 7.79 GB. All four saved-adapter reload outputs matched; adapter weights nonzero.
- Timed remote execution **177.7 seconds**, estimated requested compute **$0.0504**. App completed and stopped. This is additional to the prior $0.4916 style batch; combined estimate about $0.5420, excluding startup/storage and the earlier smoke tests.
- Raw continuations shifted toward narrated scenes with line breaks and dialogue. They remain grammatically uneven and sometimes incoherent; no claim of matching Mickiewicz's verse. Both chat probes emit English planning text under the present template/token cap rather than a finished Polish answer. Raw corpus adaptation did not establish poetic chat behavior; this limitation is retained in the outputs.
- [Execution and exact coverage](runs/pan-tadeusz-1788776622044561619/execution.json), [before](runs/pan-tadeusz-1788776622044561619/before.json), [after](runs/pan-tadeusz-1788776622044561619/after.json), [reloaded](runs/pan-tadeusz-1788776622044561619/reloaded.json). Sources and runnable commands: [docs/notes/pan-tadeusz.md](additional/notes/pan-tadeusz.md).

### Screenplay search result

No verified publicly downloadable full screenplay found after searching the title in Polish/ASCII, script/text/PDF/transcript terms, library records and subtitle leads. Official film records credit Mikołaj Korzyński. A specific next lead is Script Fiesta's 2025 panel with the writer and director. A library hit is a DVD, educational PDFs are film descriptions, and Wikicytaty is a quote collection. These are not substitutes for the complete screenplay. No screenplay/subtitle corpus added; no external contact made. Detailed sources: [docs/notes/screenplay-search.md](additional/notes/screenplay-search.md).

## Bidirectional dialogue conversion

User requested the Wikiquote dialogue collection as user/assistant pairs in both directions. Added [scripts/dialogue_pairs.py](scripts/dialogue_pairs.py) for a supplied local dialogue text: each adjacent cross-speaker pair creates forward and reverse examples. Scene boundaries are preserved, repeated pairs deduplicated, consecutive same-speaker lines merged. Scenes sharing lines stay in the same split to prevent reversed-pair/quotation leakage.

The linked film dialogue was not bulk-copied or transformed; the copyright limitation was explained, with local user-supplied text offered as the supported input. No film dataset or new GPU run was produced. [Usage](additional/notes/dialogue-pairs.md). Four new tests verify adjacency/both directions, scene boundaries, split isolation, merging/deduplication and malformed input rejection; all nine repository tests pass. Reverse-direction pairs are reconstruction examples and may not be natural replies. The existing trainer uses its general persona evaluation, not the converter's validation file automatically.

## User-supplied chlopaki.md: actual film-dialogue adaptation

The user supplied `datasets/chlopaki.md`. Work now uses that local content directly, superseding the earlier converter-only state. The source is a user-supplied dialogue transcript, not independently verified as an official screenplay. It has spelling errors, abbreviated character labels, stage directions and some unlabelled continuation lines.

### Dataset C1

- Source SHA-256: `54ccfa75fd8cacf0a9ba1a97438801a035f38f8069788aa026358a912c826e57`.
- `scripts/prepare_chlopaki.py` produces 71 scenes / 706 merged turns. Nine single-turn scenes are preserved separately. Scene headings/stage directions excluded; unlabelled speech continuation attaches to preceding speaker, recorded in an audit. Character abbreviations resolved locally where possible, source content otherwise retained.
- **1,270 unique training examples: 635 forward + 635 reverse.** Every pair has its reverse. All usable exchanges are in training; no quotation holdout. Six new ordinary Polish questions are saved for before/after evaluation. Their wording is disjoint from training prompts.
- No assistant-authored wit examples mixed in. Every resulting pair maps exactly to original source line numbers; all nonempty source lines accounted for as dialogue, heading or parsing audit.
- Dataset hash: `3f691a2b920c6efa3cc0e2c4b922bbb1658de325baf69777bfb15f7b2799edd6`. [Prepared data](datasets/chlopaki-bidirectional-v1/train.jsonl), [line provenance](datasets/chlopaki-bidirectional-v1/pair_source_lines.json), [instructions](additional/notes/chlopaki.md).

### Training C1a — Qwen3.5-4B, failed OOM

- One L4; direct batches up to four examples / 2,048 padded tokens, rank-16 LoRA, one epoch, ten-minute cap.
- First optimizer update completed, then a longer batch exhausted GPU memory (about 21.49 GiB allocated). App `ap-REDACTED019` exited with error. No successful adapter result. Failed-attempt compute not yet measured in an execution record and excluded from successful-call cost sums.
- Fix: enable non-reentrant gradient checkpointing for direct batching. Preserve long dialogue rather than truncating it. This batching mode uses answer-token mean loss, unlike the old microbatch recipe's example mean.

### Training C1b — Qwen3.5-4B on supplied film dialogue, completed partial pass

- Same dataset/model and budget, with gradient checkpointing. All 1,270 examples requested for one pass. Coverage will be recorded explicitly before claiming all pairs were seen.
- Evaluate base without style instruction, prompted base, and fine-tuned adapter without style instruction on six Polish questions. Label model and exact dataset on every reported example, per user instruction.
- Command: `uvx --from modal==1.5.0 modal run scripts/style_modal.py --stage train --data-run chlopaki-bidirectional-v1 --model qwen3.5-4b --epochs 1 --max-seconds 600 --batch-tokens 2048`.

C1b progress: gradient checkpointing fixed the observed OOM; training passed 71 updates / 284 examples with finite loss. Added continuation support in case the ten-minute cap interrupts the one-pass schedule: reuse the saved adapter on indices absent from `seen_example_indices.json`, verify exact model specification and dataset hash, and restart AdamW explicitly. This is weight continuation with a fresh optimizer, not an exact optimizer-state resume. It avoids retraining already-seen pairs while completing the requested corpus. General chat outputs and comparison reports now carry the model and training-data identity.

C1b completed: 287 updates, 600.12 s training, 1,148/1,270 unique examples seen, finite loss, nonzero adapter and matching reload. Peak allocated VRAM 12.49 GB. Timed remote 743.07 s, estimated requested compute $0.2108. [Record](runs/style-train-wit-1788780564861930331/execution.json). Greedy generalization was poor: “Nie wiem.” on the frozen-computer question and repetitive “Nie, nie…” on the other five. This is a recorded failed-quality result, not a comic success.

### Training C1c — finish unseen pairs, complete

Continue the same Qwen3.5-4B adapter on the remaining 122 pairs only; fresh AdamW, same 1e-4 learning rate, gradient checkpointing and a 180-second training cap. The neutral and prompted baseline outputs are reused after exact prompt/model checks to avoid spending GPU time repeating them. Once all pairs are covered, check sampled decoding before concluding whether the repetition is specific to greedy decoding. Do not mix in the prior authored examples or call this a different training corpus.

C1c completed: 31 additional updates on exactly the remaining 122 examples, 51.43 s training. Combined C1b+C1c: **318 updates, 1,270/1,270 examples, 651.55 s training (10 minutes + 51.5 seconds)**. Full dataset seen, no repeats across segments, saved-adapter reload matched. Final peak allocated VRAM 12.90 GB. [Final result](runs/style-train-wit-1788781334049902996/execution.json). C1c timed remote 82.61 s, estimated compute $0.0234; both successful training calls total $0.2343, excluding the failed OOM attempt and startup/storage.

The final greedy responses stopped looping but mostly became short non-answers: “Nie wiem.”, “A co?”, “Aha.”. This demonstrates a strong shift away from explanatory assistant responses, but not useful comic answers to new questions. Do not present it as a quality improvement.

### Evaluation C1d — fixed-seed sampled decoding, complete

Same fully trained Qwen3.5-4B adapter on the supplied chlopaki.md pairs; no additional training. Evaluate all six new Polish prompts for neutral base, prompted base and fine-tuned adapter. Temperature .7, top-p .8, top-k 20, seed 42, repetition penalty 1.1. The mild repetition penalty is a new explicit decoding change; earlier style probes used 1.0. Preserve both greedy and sampled outputs, no seed cherry-picking.

C1d completed: 81.98 s timed remote execution, estimated compute **$0.02326**. [Record](runs/style-sample-wit-1788781457274497722/execution.json). No repeated loops in these six sampled outputs. Qwen3.5-4B fine-tuned only on the supplied `chlopaki.md` answers the life-plans question with “Zamieniam się w kaczki!” and the expensive-sweater question with “Zamieniam się w żubrówkę.” These show a strong shift toward absurd dialogue, with uneven question relevance and language.

User feedback: the duck reply is funny, and judging it as a failed practical assistant misses the creative workshop objective. Revise the evaluation framing: assess comic surprise/personality, question relevance and linguistic coherence separately. Absurdity can be a desired result; length/line-count scores cannot measure that. Earlier concern about repetitive loops still stands. Keep all six outputs visible, including weaker ones.

### Evaluation C1e — 25% LoRA strength, complete

Same Qwen3.5-4B checkpoint and same adapter trained on all 1,270 supplied `chlopaki.md` pairs. Scale 120 LoRA layers' adapter contributions by 0.25 at inference; identical sampling settings and seed to C1d, no training. [Record](runs/style-sample-wit-1788781648674828805/execution.json).

- 77.23 s timed remote execution, estimated compute **$0.02191**.
- Answers generally return to explanatory assistant behavior, with residual grammatical errors. This setting reduces the comic transformation; it is an instructive comparison, not a preferred creative result.
- The local Modal client lost its connection after the remote result was saved. Recovered all saved text artifacts from the persistent volume; no GPU rerun. Confirmed all five apps from this film batch are stopped with zero tasks. Unrelated apps were left alone.
- Successful film training plus both sampling calls total **$0.2794348 estimated requested compute**, excluding failed initial OOM compute and startup/storage. No further sweep launched.

Saved selected actual film results in [results/example-results.md](results/example-results.md), all six Q&A comparisons in [results/chlopaki-results.md](results/chlopaki-results.md), and all 54 base/prompted/after outputs across three conditions in [results/chlopaki-results.html](results/chlopaki-results.html). Every comparison labels the exact model and training dataset. Full-strength sampled decoding is the main creative demonstration; the other conditions explain how decoding and adapter strength change the result.

Final local verification: all nine unit tests passed; modified Python sources parsed successfully; saved coverage contains exactly indices 0–1269; report contains 18 question cards / 54 answers; result-document links resolve.

### Evaluation C1f — non-question repetition probe

User asked whether the adapter always falls back on “Zamieniam się w…” after non-question messages. Prepared eight statements/greetings/dialogue fragments and four questions, two fixed seeds (42, 123), full-strength Qwen3.5-4B adapter trained only on supplied `chlopaki.md`. No style instruction, no additional training. Same sampling settings as C1d but a 96-new-token cap; batch size four. This is a small diagnostic sample, not a prevalence estimate for all conversations.

Source contains “Zamieniam się w słuch!” once (line 718); the phrase appears in four generated pairs, including two answer targets. First probe launch failed during container import because the separate Modal wrapper imported an unmounted local module. Stopped the app, made the image definition self-contained, and relaunched. Failed startup compute is not measured in the successful-call estimate.

Reproduce: `uvx --from modal==1.5.0 modal run additional/scripts/dialogue_probe_modal.py`. Local GPU: `uv run additional/scripts/dialogue_probe.py --adapter-dir PATH_TO_SAVED_RUN --output runs/my-dialogue-probe`.

C1f complete: **1/16 non-question responses**, **1/8 question responses** contained/started with the phrase. No universal fallback. Limited convenience sample; no claim that question syntax causes the difference. Other outputs range from relevant dialogue and comic replies to brief non-answers and incoherent passages. Saved every output in [results/chlopaki-results.md](results/chlopaki-results.md) and [raw record](runs/dialogue-probe-1788793342343057211/probe.json). Sampling depends on batch order/RNG consumption, so identical seeds across different prompt sets do not imply identical answers.

Timed remote **59.76 s**, estimated successful-call compute **$0.01696**. App completed and stopped. Both new script sources parse successfully; saved counts recomputed from all 24 answers and verified.

### Evaluation B2 — ordinary Polish questions and statements after full-book training

User requested the equivalent chat probe for models trained on full *Pan Tadeusz*. There is currently one completed full-book adapter: **LiquidAI/LFM2.5-2.6B**, revision `654f9463ce32b05d0429d76fe1f580b27d4c1ac0`, trained on all twelve books and epilogue from Wolne Lektury, raw-text continued pretraining with LoRA. The earlier Qwen poetry adapter used 64 authored Q&A examples and is not a full-book model.

Prepared four ordinary Polish questions and four statements, all sent through the chat template with no system/style instruction. Compare original checkpoint and full-strength saved adapter, same seed 42, temperature .7, top-p .8, top-k 20, repetition penalty 1.1, batches of four, 192-new-token cap. These test ordinary replies rather than literary continuations. No additional training.

Runnable scripts: `uvx --from modal==1.5.0 modal run additional/scripts/corpus_probe_modal.py`; local GPU: `uv run additional/scripts/corpus_probe.py --adapter-dir PATH_TO_SAVED_RUN --output runs/my-corpus-probe`. New script syntax verified.

B2 completed: [all 16 raw outputs](runs/corpus-probe-1788793991034451951/probe.json), [readable comparison](results/pan-tadeusz-results.md). **8/8 after outputs begin with English planning text; 5/8 reach a Polish final-reply segment before the cap, 3/8 do not.** The visible replies are mostly prose; this does not establish always-poetic chat. The untuned base also produces planning text (2/8 reach a final-reply segment), so do not attribute that behavior solely to fine-tuning. Readable report extracts only text after the literal `</think>` delimiter and explicitly labels absent replies; raw outputs remain unchanged. Longer decoding or a model-specific template intervention was not tested, to avoid an unplanned sweep.

Timed remote **71.64 s**, estimated requested compute **$0.02033**, excluding startup/storage. App completed/stopped. No new training. Both new sources parse successfully; all eight prompt alignments and final-reply counts verified.

### Larger-context follow-up — implementation prepared, no new GPU run

User suggested a larger context window for full-book adaptation. The original 257-token input / 256-target blocks were deliberately short training chunks, not the architecture's capacity. Liquid AI's current official model card describes 128K context: https://huggingface.co/LiquidAI/LFM2.5-2.6B . That inference capacity is not a promise that 128K training fits an L4.

Added `--target-tokens` (256/1024/2048/4096), `--batch-size` (1/2), and `--line-aligned` to local and Modal full-book trainers. Prefer 2048 targets, batch one as the next economical test. Longer sequences enable gradient checkpointing. Optional tokenizer-offset newline boundaries retain every next-token target exactly once with one-token overlap; unusually long lines fall back to fixed cuts and are counted. Default behavior preserves the original fixed-block recipe.

Validation: three new CPU tests check exact coverage with line boundaries, oversized-line fallback and compatibility with the original chunking; all 12 repository tests pass. Modified sources parse. GPU fit/runtime/quality untested; no additional cloud spend. Larger chunks reduce updates per book pass as well as increasing context, which must be disclosed when comparing outcomes. Longer output budgets and question-to-verse supervision remain separate interventions. [Commands](additional/notes/pan-tadeusz.md#larger-training-chunks--tested-at-2048-targets).

### Training B3 — 2,048-target line-aligned full-book run, launched

User explicitly requested running and testing the larger-context recipe. Started a fresh **LiquidAI/LFM2.5-2.6B** from the same pinned checkpoint, full Wolne Lektury *Pan Tadeusz*, one pass, rank-eight LoRA, LR 1e-4, target limit 2,048 (up to 2,049 input tokens), batch one, line-aligned boundaries, gradient checkpointing. Ten-minute training cap; one L4. No continuation from the old 256-target adapter.

Command: `uvx --from modal==1.5.0 modal run scripts/corpus_modal.py --target-tokens 2048 --batch-size 1 --line-aligned --max-seconds 600`. App `ap-REDACTED023`.

Evaluation plan: preserve original four greedy completion/chat/reload probes, then repeat B2's eight ordinary Polish messages using exactly its sampling recipe. Add a separate, bounded 1,024-output-token diagnostic on the first two questions, before and after, because the old 192-token cap often stopped in planning text. Longer diagnostic uses batch two and is labeled separately; it is not a matched seed/batch comparison with the eight-message test. This inference-only extension avoids interpreting truncated planning as the final writing quality. No epoch/model sweep.

B3 training complete: [execution](runs/pan-tadeusz-1788794554392255032/execution.json). **84/84 chunks, 169,997/169,997 next-token targets, 84 updates, 73.02 s training**, zero forced line splits. Peak allocated VRAM **8.83 GB**. Nonzero adapter and all four fresh-base reload outputs match. Timed remote 176.98 s, estimated requested compute **$0.05021**. Original 256-target run used 333 updates / 61.28 s / 7.79 GB, so the new recipe changes update count and batching as well as context.

Raw continuations remain line-broken narrative with uneven grammar and meter; short chat probes still mostly contain planning text. Started the eight-message sampled chat comparison plus two separate 1,024-output-token diagnostic questions. No further training requested for evaluation.

B3 evaluation complete: [all 20 unmodified generations](runs/corpus-probe-1788794812419147366/probe.json), [full comparison](results/pan-tadeusz-2048-results.md). Untuned outputs on the eight-message 192-token test match B2 exactly. New adapter reaches a final-reply segment in **2/8** cases, versus **5/8** for the old adapter; visible replies are ordinary prose. This is a token-budget diagnostic, not a model-quality ranking.

The separate 1,024-token test reaches a substantial prose answer to the life-direction question for both untuned and new-adapter models; neither reaches a final delimiter on the computer question. Thus increasing output allowance helps one case but does not yield poetic chat. No output-budget sweep beyond this diagnostic. Raw continuation counterexample: “Gdy wstał z łóżka i wybrał się do pracy.” = 11 syllables by manual word-level count (1+1+0+2+1+2+1+1+2), not 13.

Evaluation timed remote **146.43 s**, estimated compute **$0.04155**. Combined B3 training and tests **$0.09176**, excluding startup/storage. Both apps completed/stopped. Saved selected outputs in `results/example-results.md` and all comparisons in `results/pan-tadeusz-2048-results.md`. All 12 unit tests pass; checked exact coverage, zero forced splits, all reload outputs, baseline reproducibility and output counts.

### Post-training proposal — multi-line poetic replies

User clarified that replies must contain several lines, never a single line, and asked for post-training ideas. Proposed a staged, budget-conscious experiment; no GPU run or new training data generated in this turn.

1. Fix a concrete initial target: four nonempty verse lines, no introductory prose, relevant to ordinary questions, statements, greetings and follow-ups. Prepare roughly 200–500 reviewed Q&A examples; hold out entire topics/paraphrase families. If thirteen-syllable meter is included, validate target lines rather than trusting a teacher model's self-count. Apply assistant-answer-only SFT, including the correct end-of-turn token after the full answer. Keep user inputs ordinary so the trained default does not depend on asking for a poem.
2. Cheapest next improvement: sample a few candidate answers on training prompts, keep those passing format checks and human relevance/style review, and run another short SFT pass (rejection sampling followed by supervised training). Reuse approved data across participants. Avoid a blind generation or epoch sweep.
3. Optional RLVR extension: reward four real, distinct lines and valid meter, penalize duplicates/filler; retain content-quality review and anchor training to good answers so optimizing shape does not destroy relevance. Line count is exact; Polish syllabification needs validation and handling of ambiguous words. GRPO supports custom Python reward functions without a learned reward model, but rollout generation makes it a later step for the limited budget.
4. Evaluate raw first-attempt compliance separately from a demo wrapper that validates and retries. Retrying can prevent showing a one-line answer but cannot guarantee a successful answer within a finite retry budget. Do not present wrapper enforcement as weight-level reliability.

Model choice correction: official LiquidAI/LFM2.5-2.6B card explicitly says it is a pure reasoning model that always thinks and inserts `<think>` in the assistant prefix (https://huggingface.co/LiquidAI/LFM2.5-2.6B#chat-template). This explains why `enable_thinking=False` in the shared helper did not avoid planning; it was a poor fit for a low-latency short-verse demonstration, and this should have been checked earlier. Prefer Qwen3.5-4B with the already exercised non-thinking path for the next practical SFT baseline, or explicitly account for the LFM reasoning template if continuing its full-book adapter. This is a proposed new Q&A dataset, not another full-book-only experiment.

Primary references: assistant-only SFT and continuing adapters https://huggingface.co/docs/trl/sft_trainer ; custom rewards and rollout-generation overhead https://huggingface.co/docs/trl/grpo_trainer . The numeric dataset size and staged recipe are our proposed experiment, not claims established by these sources.

### B4 preparation — 500 ordinary Polish prompts → original Pan Tadeusz passages

Prepared the requested 500 pairs, each with 4–12 original verse lines, across all twelve books. User clarified this is a humour project: modern questions answered by historically disproportionate passages are desirable. Revised 458 initially literal prompts toward everyday setups and comic analogies; retained 42 already suitable prompts. All prompts individually authored in this Codex session after reading the selected passages, without paid teacher/API calls. Answers are verbatim Mickiewicz, not model generations.

Examples: salary negotiation → duel (`pt-0164`); failed presentation → embarrassed hunting dogs (`pt-0166`); asking for a raise but discussing weather → Jacek unable to open his heart (`pt-0403`); handing over a cherished work laptop → Gerwazy bequeathing his Scyzoryk (`pt-0477`). These deliberate analogies address the user's correction; historical literalness is not the quality objective.

Source: existing Wolne Lektury full-book processed text, SHA-256 `e6447a4e4b4ddbeb8f580ce3d26cf193ef949014b6c0cce3dab7ded5855fca4e`. Deterministic seed 2026 selects one nonoverlapping passage per paragraph, preferring sentence boundaries. Book headings, prose summaries and the predominantly eleven-syllable epilogue excluded. Original spelling and typographic markers preserved. Source physical lines can split metrical units; this is not a certification that all lines scan to thirteen syllables.

450 train / 50 validation; 293 questions / 207 statements. Line counts: 4:124, 5:50, 6:116, 7:29, 8:83, 9:20, 10:48, 11:8, 12:22. Split groups passages sharing normalized verse lines of 20+ characters, including repetitions in different source positions. Related themes remain across splits, and the validation text was seen by previous full-book adapters. Prefer a fresh base-model adapter for the next Q&A experiment.

Validation passed: 500 unique prompts and answers; exact source text and source-line positions; 4–12 lines each; no overlapping source positions; all twelve books; 450/50 IDs disjoint; no normalized verse-line overlap >=20 characters across splits; manifest counts and data hash agree. Rebuild with `uv run --no-project scripts/prepare_pan_tadeusz_qa.py build`. [Guide and three examples](additional/poetry.md), [all 500 reviewed pairs](datasets/pan-tadeusz-qa-v1/REVIEW.md).

No training launched for this dataset; no new before/after results. GPU and paid teacher API spending for this preparation: $0 (excluding the Codex session itself). Next proposed baseline: fresh Qwen3.5-4B, assistant-only SFT; evaluate 4–12-line compliance rather than the previous exactly-four-line metric, plus comic fit and syllable counts separately.

Training JSONL SHA-256: `52c3cb2b69adc29d645ce45afd1024baae6c7ac90ebbe2306ddb35cab7818361`.

### B4 training — Qwen3.5-4B on the 450 Pan Tadeusz Q&A pairs, launched

User explicitly requested training the prepared dataset. Started fresh Qwen3.5-4B (pinned scripts/models.json revision), rank-16 LoRA, alpha 32, LR 1e-4, assistant-only loss, two epochs requested, 600-second training cap, 2,048 padded tokens per batch (maximum four examples), gradient checkpointing. One Modal L4, no retries, 1,200-second function timeout (~$0.34 requested compute ceiling plus startup/storage). App `ap-REDACTED005`.

Command: `uvx --from modal==1.5.0 modal run scripts/style_modal.py --stage train --data-run pan-tadeusz-qa-v1 --model qwen3.5-4b --epochs 2 --max-seconds 600 --batch-tokens 2048`.

Adapted trainer/evaluation to the dataset's 4–12-line range and raised its generation allowance to 384 tokens, including the exact saved-adapter reload check. Prompt-only comparison now requests the same humorous verse behavior; base and adapter comparisons receive ordinary user text with no style instruction. Previous datasets retain their four-line metric and 192-token budget. Line count is a shape metric, not evidence of meter or comic quality. No silent training truncation. Will report actual coverage if the time cap interrupts two epochs.

Infrastructure interruption: first worker printed `Runner terminated (SIGTERM), exit code: 143` after reporting update 11 (~24.70 seconds training), then Modal automatically began a new worker despite application-level retries=0. No checkpoint had been written. Cause not established by logs; do not label this an OOM. Interrupted-worker time is additional and is not included in a later successful worker's `execution.json` compute estimate. Monitoring the automatic restart; no manual duplicate training job launched.

B4 training completed: `runs/style-train-poetry-1788797625746162366`. Qwen/Qwen3.5-4B revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`, fresh rank-16 LoRA on training hash `52c3cb2b69adc29d645ce45afd1024baae6c7ac90ebbe2306ddb35cab7818361`. 225 updates, 900 example presentations (two complete passes over 450 unique pairs), 370.2201 seconds training, 12.8565 GB peak allocated GPU memory. Nonzero adapter; all four fresh-base reload outputs match exactly. Successful worker remote time 565.3567 seconds, estimated requested compute $0.160403. This excludes the earlier interrupted worker and startup/storage; it is not the total invoice.

Greedy held-out results: 11/12 answers have 4–12 nonempty lines; 0/12 are single-line replies. Several answers repeat phrases; pt-0060 loops for 27 lines. Baseline also passes the naive line-count check on 10/12 replies because prose paragraphs and bullet lists count as lines, so do NOT present the metric as a poetry-quality classifier. The learned default changes visibly toward historical dialogue and line-broken verse, but strict meter and clean grammar are not achieved. Example pt-0010: boss visiting departments becomes the Count inspecting his army. Other outputs include comic absurdities (Gerwazy declaring someone is no longer his turtle) and malformed words.

Launched one inference-only sampled comparison on the same 12 held-out prompts, base/prompted/adapter, seed 42, temperature .7, top-p .8, top-k 20, repetition penalty 1.1, 384 output-token cap. App `ap-REDACTED014`. No retraining. All 12 repository tests pass and the new dataset-specific metric checks pass. [Full greedy outputs](results/pan-tadeusz-qa-results.md).

B4 sampled evaluation complete: `runs/style-sample-poetry-1788798230980944941`. 12/12 adapter replies have 4–12 nonempty lines; zero one-line answers in this small test. Answers containing an exactly repeated line (case/punctuation normalized): greedy 3/12, sampled 0/12. This does not measure broader semantic repetition. The 27-line greedy loop disappears with sampling; grammar, invented malformed words, relevance and meter remain uneven. Comic connections include the late dinner guest falling upside-down and being rescued by Tadeusz (`pt-0020`), forceful mediation becoming a fight (`pt-0065`), and overtime bargaining for three days off (`pt-0112`). These are actual generated outputs from the Q&A adapter, not quotes selected from the book. No new training in this evaluation.

Sample worker: 224.8267 seconds, estimated requested compute $0.063788. Completed training/evaluation workers combined: $0.224191, **excluding the unmeasured interrupted worker, startup and storage**. Both Modal apps completed/stopped. Full raw base/prompted/adapter answers in run directories; all 72 generations in `results/pan-tadeusz-qa-results.md`; three selected before/after comparisons appended to `results/example-results.md`. Saved adapter resides in Modal volume `model-training-workshop` at `/runs/style-train-poetry-1788797625746162366/adapter`. Local run files contain metadata/outputs/executed source; adapter binaries remain on the persistent volume.

Conclusion: explicit question-to-verse SFT teaches the desired default multi-line historical voice much more directly than the previous full-book-only LFM trials, although that is not a controlled same-model comparison. This is a viable workshop starting point with obvious room for grammar/meter improvement. The 12-prompt sample is not evidence of an always-poetic guarantee. No extra epoch or model sweep launched.

### R2 — visible RLVR workshop comparison (pre-registered plan)

User requested several substantially different RLVR ideas, tested for plainly visible improvement. Earlier 48-rollout arithmetic example stayed at 4/8 and is not adequate as a success showcase. Implemented three independent tasks in `scripts/rlvr_tasks.py`: six-word English microfiction with two required words; Countdown expressions using three given numbers exactly once; a robot navigating a 4x4 maze with two walls. Strict success is separate from continuous/partial reward. Microfiction checker verifies lexical constraints, not literary merit; manual output review is required. Math uses a bounded AST/Fraction interpreter, never eval. Maze paths are simulated; collisions invalidate success even if the path previously touched the goal.

Plan: screen 8 training prompts × 4 on-policy samples per task, then train promising tasks for up to 300 seconds each on Qwen/Qwen3-0.6B, pinned revision `c1899de289a04d12100db370d81485cdf75e47ca`. One L4 at a time, approximate initial investigation target below $1 requested compute excluding startup/storage. Each candidate uses a fresh rank-16 LoRA, alpha 32, learning rate 2e-4, 2 prompts × 4 samples per update, up to 160 updates. This is on-policy REINFORCE with a leave-one-out baseline, no KL penalty or PPO clipping; short runs, not a production trainer. Temperature 1, no top-k/top-p filtering, dropout off, one update per fresh rollout batch, generated tokens through first EOS only, sequence-summed log probability. No SFT warm start, teacher answers, reward-generated targets, or best-of-N display selection.

Deterministic data generator seed 20260907: 256 train / 24 development / 32 final-test prompts per task; no identical puzzles/anchor pairs/maps across splits. Half of the microfiction test uses entirely new anchor words. Both greedy first attempts and 24 fixed-seed development samples evaluated before and after. Results, all rollouts, data, source snapshots, save/reload checks and costs saved per run. Candidate selection should use development results; inspect the final test after the initial recipes are completed and label any later experiment as a follow-up. Six verifier/data/advantage tests passed before launch, including malicious/invalid arithmetic, maze collisions and duplicate/missing story words.

Screen command: `uvx --from modal==1.5.0 modal run scripts/rlvr_showcase_modal.py --task all --stage screen`. App `ap-REDACTED012`. No quality claim yet. Primary method reference: https://huggingface.co/docs/trl/rloo_trainer ; model/non-thinking template: https://huggingface.co/Qwen/Qwen3-0.6B .

R2 screen completed: six-word stories `rlvr-screen-six_words-1788799273736758142` 0/32 strict successes, mean shaped reward .3510, all EOS-terminated, estimated $0.012022; Countdown `rlvr-screen-countdown-1788799321013743971` 0/32, mean .025, 18/32 terminated, $0.003005; maze `rlvr-screen-maze-1788799335005344555` 0/32, mean .05625, 26/32 terminated, $0.001629. Screen total ~$0.01666. Despite zero strict successes, partial reward varies; test whether shaping bootstraps useful behavior rather than discarding candidates solely for this. Stories often return 2–4 anchor-containing words; math commonly adds equals signs/explanations; maze copies the literal example UURD. Removed that example from maze instructions before training (this changes the dataset hash); no reference path is now shown in its prompt. Original screen source/data preserved.

Launched all three fresh adapters sequentially, each capped at 300 training seconds / 160 optimizer batches. Command `uvx --from modal==1.5.0 modal run scripts/rlvr_showcase_modal.py --task all --stage train --max-seconds 300 --steps 160`; app `ap-REDACTED007`. One L4, each function 1100-second hard timeout; expected compute below original ~$1 investigation target. No test results inspected to adjust these recipes.

R2 stories initial trial complete: `rlvr-train-six_words-1788799386079459022`, 160 batches / 69 nonzero updates, 230.85 s training, 2.049 GB peak allocated VRAM, adapter changed and reload matched. Development strict success remains 0/24 despite mean reward rising .3653→.4667. During training 54/1280 sampled answers passed, but by the end outputs collapsed to five-word templates such as `Moon who is a sailor.` and `Clown who is an ocean.`. This is a failed success showcase and a useful partial-reward/exploration-collapse example. Terminal evaluation also prints test aggregates automatically; no test-specific examples or failure patterns used to change the recipe.

Follow-up plan, motivated by development outputs/training rollouts: add optional RLOO reference-policy regularization (detached Monte Carlo sequence log(pi/pi_reference) subtracted from scalar rewards), lower learning rate, and select the best checkpoint on all 24 development prompts by strict successes, breaking ties with mean task reward. Evaluation saves/restores rollout RNG. Keep the initial beta=0 recipe runnable and preserve original executed code. Final test must not choose checkpoints. Checkpoints are compared to the unmodified starting adapter as well; if none improves development, return the original policy honestly. No additional GPU launched yet; the original arithmetic and maze trials continue sequentially.

R2 Countdown initial trial complete: `rlvr-train-countdown-1788799671247002331`, 160 batches / only 14 updates, 190.14 s training, 2.166 GB VRAM, reload matches. Development 0/24→3/24; mean reward .0083→.5706. Actual development outputs reveal the policy ignores the target and always emits the numbers in input order as `a + b - c`. Thus the higher partial reward is mostly format/number-use compliance, not puzzle solving. Rejected as the main demo. Completed screens plus these two training runs total ~$0.1606 requested compute, excluding startup/storage.

The initial recipe's large learning rate without reference regularization produced fast loss of output diversity on multiple tasks. Next bounded comparison will use the more recent cached Qwen3.5-0.8B, LR 5e-5, beta .01 and development checkpoint checks every 20 batches, up to 300 training seconds. This changes both model and optimization recipe, so it cannot isolate which change causes any improvement. Goal is to find a practical workshop starting point, not a controlled optimizer benchmark. Start with stories and inspect before spending further; keep all rejected results.

R2 maze initial trial complete: `rlvr-train-maze-1788799930241701161`, 160 batches / 4 updates, 91.15 s training, reload matches. Development 0/24→0/24 and test 0/32→0/32: reject as a navigation success demo. All initial task comparisons are preserved in `results/rlvr-initial-results.md` and `results/rlvr-initial-results.html`. HTML includes every first attempt and simulated maze paths; generated JavaScript syntax checked with Node. All 16 repository tests pass.

R3 stories launched: `uvx --from modal==1.5.0 modal run scripts/rlvr_showcase_modal.py --task six_words --model qwen3.5-0.8b --max-seconds 300 --steps 160 --lr 0.00005 --beta 0.01 --dev-interval 20`. App `ap-REDACTED003`. Qwen/Qwen3.5-0.8B revision `2fc06364715b967f1860aea9cf38778875588b17`. Same story prompts/reward/splits as R2, fresh adapter, vision modules excluded from LoRA. Model card confirms the small checkpoint is intended for prototyping/task-specific fine-tuning: https://huggingface.co/Qwen/Qwen3.5-0.8B . Previous three-task app completed/stopped before launching this GPU.

R3 complete: `rlvr-train-six_words-1788800080367606015`, 56 batches/updates, 301.37 s training including intermediate development checks, 3.487 GB peak allocation. Development checkpoints: initial 2/24, batch 20 5/24, batch 40 8/24, final batch 56 6/24. Selected **batch 40** using development only. Selected adapter has seen 80 unique prompts; the whole exploration run presented 112. Held-out test 0/32→9/32; sampled development 0/24→8/24. All eight fresh-base reload answers match. Remote estimate $0.095617; total R2+R3 completed-worker compute $0.290467.

Manual review: the regularized 0.8B model retains more variety but prose becomes telegraphic (`mouse eats vampire in the forest`, `chef uses robot to cook dinner`). Exact counts improve, yet this is not a stunning writing example. All 32 test outputs were inspected only after checkpoint selection. No specific test example is used to alter prompts/reward.

R4 bounded follow-up launched on **fresh Qwen/Qwen3.5-4B**, revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`, same six-word dataset, LR 5e-5, beta .01, development checkpoint selection every 20 batches. No Pan Tadeusz or film adapter is loaded. Increase training allowance to 600 seconds; one L4, host memory increased to 16 GiB, overall function timeout 1100 seconds (~$0.31 requested compute ceiling excluding startup/storage). Command `uvx --from modal==1.5.0 modal run scripts/rlvr_showcase_modal.py --task six_words --model qwen3.5-4b --max-seconds 600 --steps 160 --lr 0.00005 --beta 0.01 --dev-interval 20`. App `ap-REDACTED020`. Aim: preserve readable microfiction while improving constraints; R3's 9/32 is a real but insufficiently strong workshop result. Previous app stopped before launch.

R4 intermediate development checkpoints: original Qwen3.5-4B 0/24; batch 20 18/24 at roughly 3.5 minutes; batch 40 23/24 at roughly 6.6 minutes. These are development counts, not the final test, and literary quality has not yet been inspected. Retaining best state by the declared development rule. R3's saved reference-regularized advantages were independently recomputed from task rewards and sequence log ratios and matched throughout; all saved R2/R3 evaluation rewards were independently rerun through the current checkers and matched. The reward/checkpoint mechanism, not only the reported summaries, is inspectable.

R4 completed: **`rlvr-train-six_words-1788800507182250757`**. Qwen/Qwen3.5-4B, fresh task-specific RLVR adapter; no workshop SFT and no Pan Tadeusz/film data. Training explored 62 batches / 496 sampled answers, 124 distinct training prompts, 603.61 seconds including intermediate development checks. The 600-second cap is checked after a batch and overshot by 3.61 seconds. **Selected batch 60** by development success: 0/24 original → 18/24 at batch20 → 23/24 at batch40 → 24/24 at batch60. Final batch62 tied, so retained the earlier best. The SAVED adapter therefore reflects **120 distinct prompts / 480 self-sampled completions / 60 updates**, not all 256 pool prompts or all 62 exploration updates.

Held-out greedy **1/32 → 32/32**, including **16/16 entirely new anchor-word pairs drawn from words absent from training**. Every after-test answer reaches EOS. Sampled development (12 prompts × 2 temperature-1 samples): 3/24→21/24. This is one training seed and a small, task-specific test, not universal reliability. Adapter changed and all eight fresh-base reload outputs match. Peak GPU allocation **13.992 GB**. Completed worker estimate **$0.193501**. Cumulative R2–R4 completed-worker compute **$0.483968**, excluding startup/storage; no interrupted GPU workers in this investigation.

Manual review of all 32 held-out answers: clear six-word compliance and some amusing micro-scenes, but repeated grammatical templates, sparse articles and occasional awkward meanings remain. Do not call the checker a literary-quality score. Examples (all original Qwen3.5-4B → same checkpoint + this six-word RLVR adapter): `The mermaid kissed the glacier.` → `Glacier melted to reveal a mermaid.`; `Astronaut blew birthday candles.` → `Astronaut blew birthday candles in space.`; `The mouse bit the vampire.` → `Mouse fed vampire with tiny cheese.`. These are generated outputs, not provided training targets.

R4 app completed/stopped. One bounded Countdown follow-up on the now-working 4B regularized recipe is authorized within the user's request to test distinct ideas: same LR/beta/dev selection, 300-second training cap, fresh adapter again. App `ap-REDACTED021`; command `uvx --from modal==1.5.0 modal run scripts/rlvr_showcase_modal.py --task countdown --model qwen3.5-4b --max-seconds 300 --steps 160 --lr 0.00005 --beta 0.01 --dev-interval 20`. Purpose: determine whether arithmetic can be a second successful option rather than inferring its potential solely from the failed 0.6B recipe. No further model/learning-rate sweep planned.

R5 Countdown complete: **`rlvr-train-countdown-1788801278948986334`**. Fresh Qwen3.5-4B with only Countdown RLVR, same pinned revision as R4; it does not reuse the story adapter. Explored 36 batches / 29 updates, 72 unique prompts, 305.64 s including intermediate development evaluation, 14.169 GB peak allocation. Selected batch20 by development (7/24 initial → 14/24 at20, final13/24); saved adapter has **40 unique prompts, 160 self-sampled answers, 20 updates**. Test **7/32→11/32**, six corrections and two regressions. Sampled dev4/24→13/24. All eight fresh-base reload outputs match. Completed compute estimate **$0.108979**.

Actual generated test correction: numbers [10,5,15], target85; original Qwen3.5-4B `(15 * 10) + 5` (=155) → same model + Countdown RLVR `15*5+10` (=85). This is useful evidence of some solving improvement but 11/32 is insufficient for the main workshop success demo. No further runs: keep six-word microfiction as the clear choice, arithmetic as a modest-gain comparison, and the initial maze trial as a negative/reward-debugging exercise. Do not infer that maze RLVR cannot work in general; only this 0.6B recipe was tested.

**Final R2–R5 accounting:** three inference screens + six independent training runs, all completed and apps stopped. Requested completed-worker compute **$0.5929468907**, excluding startup/storage, with no failed/interrupted GPU workers in this investigation. R4 winning run alone $0.193501. Preserved all rejected runs. No teacher/LLM-judge API charges.

Published locally (no external deployment or git push): `docs/rlvr.md` with measured recommendation and exact commands; `results/rlvr-results.md` / `results/rlvr-results.html` with all six runs (960 unedited before/after generations including sampled development); `RLVR_INITIAL_RESULTS.*` with the first failed comparison; `results/rlvr-reward-lesson.md` with actual intermediate samples and their advantages. Appended three model-labelled R4 before/after examples to `results/example-results.md`; README and old RLVR guide link the new work. Trainer/wrapper defaults now match the explicitly tested R4 command: Qwen3.5-4B, 600 seconds, max160 batches, LR5e-5, beta.01, dev interval20. The original failed settings remain available with explicit arguments. UV script lockfile is pinned and verified.

Final verification: 16 repository tests passed; R4 data hash, selected training coverage (120 prompts/480 rollouts), unseen-word split, all saved evaluation rewards, regularized advantages and reload equality independently rechecked (`local_verification.json`). Report JavaScript syntax and task/split/filter rendering checked with Node and a DOM stub; this is not a browser-layout screenshot test. Model prose manually reviewed, with formulaic wording and occasional awkward grammar explicitly documented. Greedy32/32 does not imply every sampled answer passes (sampled development21/24), nor that all future prompts will pass.

## P1 — LLM robi prawko: official multiple-choice exam pilot (2026-09-08)

User approved trying the driving-licence idea, separate from hackathon matura work. Source: Ministry of Infrastructure, July 2026 catalogue at https://www.gov.pl/attachment/a5c6c329-28a5-4274-a1a8-e2813f0a51bd, linked from https://www.gov.pl/web/infrastruktura/jak-uzyskac-prawo-jazdy. Download SHA256 `1d569f59c48c1fb76afd95470b91062d7167305caef4f992a0ef9233dec23300`. Parsed XLSX with stdlib XML/ZIP, no paid data generation. 3,526 catalogue rows; 165 category-B questions with no Media file and three nonempty A/B/C options plus official key. English translations are retained, but this experiment uses Polish. Excludes yes/no, image/video questions and other categories. This subset score is NOT a full driving-exam pass/fail score.

Initial v1 grouping used one-direction SequenceMatcher; an independent test caught its order asymmetry. Preserved v1 and its inference-only screen, then fixed grouping to maximum bidirectional similarity >= .72, connected components, before training. Corrected v2: 100 train / 25 dev / 40 test, seed 20260908. Cross-split similarity and ID tests pass. This lexical grouping is a heuristic, not proof of semantic independence or absence from base pretraining.

Initial v1 screen: original `Qwen/Qwen3.5-0.8B`, revision `2fc06364715b967f1860aea9cf38778875588b17`, no workshop fine-tuning, run `prawko-screen-1788860501815920620`, Modal app `ap-REDACTED015` completed. Train58/101, dev13/24, test18/40, rotated test25/40. Huge answer-order sensitivity worth measuring. Worker29.851s, estimated $0.0084693 excluding startup/storage. Do not compare v1 screen scores directly to v2 training scores.

Planned bounded v2 comparison: separate fresh rank16/alpha32 LoRA adapters on Qwen3.5-0.8B; SFT and RLVR each up to180s/10epochs, LR5e-5, minibatch4, option order shuffled each training presentation. All evaluations choose argmax among next-token A/B/C logits under the same nonthinking chat template; this is constrained-choice evaluation, not free-text generation. SFT uses full-vocabulary next-token cross entropy. RLVR is a contextual-bandit REINFORCE/RLOO update: four categorical samples per question, binary correctness reward, leave-one-out baseline, exact KL over the three options to frozen base with coefficient.01. No reasoning traces, teacher or intermediate rewards. Select adapter on dev only after each epoch (initial base eligible), report original-order and rotated test, plus training-set memorization separately. Saved adapters must reproduce eight predictions when reloaded onto a fresh base. No guarantee of improvement.


P1 completed v2 comparison, app `ap-REDACTED011` stopped normally. No failed/interrupted GPU workers. Both runs reproduced identical original-model baselines: train53/100, dev15/25, test21/40, rotated test20/40.

- SFT run `prawko-sft-1788860580008838148`: explored250 updates/10epochs,168.240s training including dev evaluations. Selected epoch3/75updates: all100 unique questions,300 presentations. After train91/100, dev23/25, test27/40, rotated26/40. Original-order15 corrections/9 regressions; rotated11/5. Saved adapter changed; all8 fresh-base reload predictions match. Peak7.7975GB. Worker199.2206s, estimated$0.0565229.
- RLVR run `prawko-rlvr-1788860780645474401`: explored208 updates (8complete epochs plus8batches),181.052s including dev checks. Selected epoch3/75updates: all100 unique questions,300 presentations,1,200 sampled actions. After train80/100, dev22/25, test27/40, rotated25/40. Original-order11 corrections/5 regressions; rotated8/3. Adapter changed; all8 reload predictions match. Peak7.8932GB. Worker194.6429s, estimated$0.0552241.

Total P1 completed-worker compute **$0.1202163**, including v1 screen; excludes startup/build/storage. Both candidates beat the base by6/40 answers, a modest pilot result. RLVR did not beat SFT; no further tuning or GPU runs planned. This is a good real-exam comparison/early-stopping exercise, less dramatic than the six-word RLVR result. Test questions were never used for checkpoint selection; only one seed tested. Base-pretraining contamination remains unknown.

Answer-order bias persists: original model selected A28/C11/B1 on test; SFT selected C22/B14/A4. Mean original A/B/C probability mass was.937, after SFT.999, so the baseline was already mostly emitting an allowed letter. Both methods improve on rotated choices too. Do not claim all gains reflect newly learned traffic knowledge or full-format compliance.

Actual held-out example, original Qwen3.5-0.8B (no workshop adapter) → Qwen3.5-0.8B with either SFT or RLVR on100 official questions: question7445, forbidden activity in a passenger car, A(light trailer) → C(pulling children on sledges), official keyC. Regression: question7454, road on which towing another vehicle is forbidden, A(motorway) → C(residential zone), official keyA. These answer descriptions are official option text, not generated explanations.

Saved `docs/prawko.md`, `results/prawko-example-results.md` (all160 before/after comparisons across two methods and two option orders), ordinary uv trainer, pinned script lock, Modal wrapper, deterministic preparation and report scripts. Eighteen repository tests pass; full v2 dataset/manifest/source rebuild matches byte-for-byte. Independently recomputed every score, permutation key and every recorded RLVR reward/advantage; verified selected training coverage and held-out isolation, saved `local_verification.json` in both training runs. Weights remain on Modal volume, small records local. No commit/push performed for this new experiment.

## P2 — Four-times-longer prawko comparison (2026-09-08; completed)

User requested ~4x more training for both SFT and RLVR, hoping to see a difference. Authorized two fresh runs with the same Qwen3.5-0.8B revision, v2 data, seed42, LR5e-5, rank16/alpha32 and batch4; increase from180s/10epochs to720s/40epochs. Sequential one-L4 workers,1050s hard timeout each (~$0.30 requested ceiling per worker), expected combined compute ~$0.45 excluding startup/storage. App `ap-REDACTED013`. No new dataset, hyperparameter sweep or larger model.

Added separate final-checkpoint evaluation and saved `final_adapter`, alongside the original development-selected `adapter`. Final test scores never select a checkpoint; development selection is complete before either final or selected test evaluation. Added elapsed time per development checkpoint and per-epoch history persistence. The changed bounds are720s/40epochs; defaults remain the cheap180s/5epochs. Local split/permutation tests pass. The longer runs restart from the base (previous saved adapters lack optimizer state), preserving a controlled learning trajectory instead of resetting optimizer state midway.

Interpretation to test: answer-only SFT and binary-reward categorical RLVR have closely related objectives. Without reference regularization, both favor the correct letter; RLVR's expected correctness gradient is scaled by the policy's probability of that letter, and its four sampled actions introduce variance. Exact reference KL further differentiates RLVR here. Longer training might reveal different generalization/overfitting without necessarily creating a large held-out score gap. Preserve results even if both select the same early checkpoints as P1.


P2 completed normally; app `ap-REDACTED013` stopped. No further GPU jobs planned. Same initial baselines as P1; longer time cap reached before40epochs on the slower worker.

- SFT `prawko-sft-1788861428320342529`:721.7495s training including dev checks,725updates/29epochs/2,900 presentations. Selected epoch3/75updates/300 presentations: train92/100, dev23/25, test28/40, reordered25/40. Final: train100/100, dev20/25, test28/40, reordered30/40. Worker771.3756s,$0.21885469, peak7.7975GB. First250 batch IDs/options/answers exactly match P1, but first nonidentical loss is update index1 (P1 .94075495 vs P2 .92233044). Same seed is not bit-identical replay; do not attribute the selected early checkpoint's +1 test answer to longer training.
- RLVR `prawko-rlvr-1788862202341560425`:722.2233s training,569updates (22epochs plus19batches),2,276 presentations. Selected epoch7/175updates/700 presentations/2,800 sampled actions: train86/100, dev21/25, test29/40, reordered28/40. Final: train91/100, dev20/25, test25/40, reordered24/40. Worker749.5680s,$0.21266742, peak7.8932GB.

Additional compute **$0.43152212**; all P1+P2 **$0.55173841**, excluding startup/builds/storage. No failed/interrupted workers. Both selected adapters changed and reproduce all8 test predictions after fresh-base reload. `final_adapter` also saved remotely, evaluated in memory but not separately reload-tested. `.gitignore` now excludes downloaded per-run final-adapter directories too.

Interpretation: final SFT beats final RLVR by3/40 original-order answers and6/40 reordered answers. Development-selected RLVR beats SFT by1/40 original-order and3/40 reordered answers. Thirteen original-order questions differ in correctness between the selected methods (RLVR7 wins, SFT6). Therefore the conclusion changes with checkpoint rule. SFT memorizes the training set more fully; answer-only RLVR is not clearly superior. Development scores are noisy on25 questions and do not perfectly predict held-out performance. Preserve both checkpoint rules, fixed before looking at these final test results. Repeated use of the same40-question test is exploratory, not fresh confirmation; no new tuning based on these scores.

Published local artifacts: `results/prawko-training.html` interactive development curves and actual selected/final test choices; `results/prawko-long-results.md` all320 before/after comparisons (two methods × two checkpoints × two orders ×40 questions); `additional/scripts/prawko_learning_report.py`, expanded Markdown reporter and `scripts/verify_prawko.py`. Independently verified all saved scores, option keys/permutations, dev-only selection, train/test isolation and every RLVR sampled reward/advantage, with audits saved in both run directories. HTML JavaScript rendered4 chart combinations and16 example/filter views with a Node DOM stub; this is not a browser-layout screenshot test. No commit/push performed.

## S1 — Scratch v2 corpus audit and redesign (2026-09-08)

User moved to from-scratch training and full Wolne Lektury / whole Polish Wikipedia, then explicitly clarified Falenty was their v1 and expects a fresh v2, including sizes and approach. Reframed from porting the character-model presets to a new design: own Polish BPE tokenizer,10M/30M fresh decoder candidates, efficient causal SDPA, corpus-preserving cleaning and equal-time model-size/corpus comparisons. Model candidates are not yet trained or benchmarked; no GPU job in this research step. Exact proposed counts10,244,160 and29,893,120 derive from specified tied8k embeddings, bias-free attention/SwiGLU, RMSNorm and RoPE; verify against implementation later.

Audited existing Falenty ZIP (123,071,225 bytes, SHA2561a25be256ee13a4a39c9a1c549d4a3f363bf2e4ad673f8e1c34e25473c43e15b). Contains ONE concatenated text file,337,172,535 bytes,312,259,017 Unicode characters,3,638,187 lines.7,157 footer markers and7,140 distinct catalogue URLs; completeness versus today's catalogue is not established. Current official API:7,654 book entries,2,527 parent-book entries. Plan fresh document-preserving Polish parent-work corpus rather than treating concatenation and all entries as a clean deduplicated corpus. Snapshot hashes/stats saved to research/scratch/falenty_corpus_audit.json.

Verified full cleaned Wikipedia: wikimedia/wikipedia,20231101.pl, revision b04c8d1ceb2f5cd4588862100d08de323dccfbaa;1,587,721 rows, six Parquet shards totaling1,765,059,986 bytes. Saved source URLs/LFS SHA256s and metadata; fetched a125KB preview, not the1.765GB corpus. Current official20260901 article XML dump marked done:2,733,269,592 bytes, SHA1ffc211b4dc3d73b46c2cd1d4b149868c986eeafc. Full history/images excluded; raw wikitext needs extraction. HF README's uncompressed size differs from size API; don't quote either as a verified text size. Freshness is not needed for the initial language-learning comparison, so cleaned2023 snapshot is the practical first candidate.

Saved docs/notes/scratch-v2.md, pinned research/scratch/sources.json and metadata, plus ordinary stdlib uv downloader download_scratch_corpus.py. Downloader dry listing and checksum validation against the local Falenty ZIP passed. Full Wikipedia network transfer/resume not exercised; no giant downloads or GPU spend. Raw/cache corpora remain ignored. Data/source investigation is complete; the proposed architecture and training-quality hypotheses await implementation and measurement.

## S2 — Actual from-scratch Wikipedia wikitext experiment (2026-09-08; running)

User explicitly chose Wikipedia markup, then asked to actually do it. Downloading the complete dated Polish Wikipedia20260901 article XML dump via the checked/resumable downloader (2,733,269,592 bytes, expected SHA1ffc211b4dc3d73b46c2cd1d4b149868c986eeafc). No markup-cleaning corpus substituted. Extraction removes only XML packaging and decodes XML entities once; keeps namespace0 nonempty wikitext including redirects, links/templates/tables/ref tags. Original body string retained in local JSONL with title/page/revision IDs and content hash. Exact duplicate texts share a split via hash:99% train,0.5% dev,0.5% test by hash buckets. This is an article grouping policy, not a claim of semantic deduplication.

Implemented fresh v2 code: scripts/scratch_model.py (RoPE, RMSNorm, SwiGLU, tied embeddings, causal SDPA); scripts/train_scratch.py and scripts/sample_scratch.py with ordinary uv entrypoints; scripts/scratch_modal.py bounded sequential L4 workers. Counts instantiated and verified:10,244,160 and29,893,120 parameters at8192 vocabulary. CPU causal-mask test passes (future token changes cannot affect earlier positions); tiny-batch learning and save/reload test passes. XML fixture confirms original links/templates/headings/ref/table markup and redirects survive exactly. No pretrained weights/tokenizer.

CPU preparation trains byte-level BPE on up to2048 hash-selected TRAIN articles (first8192 characters each), then encodes the full extracted train/dev/test pools. Per-article tokenizer round trip is checked. uint16 token files have an EOD separator; windows may cross article boundaries with ordinary causal attention. Sampling is uniform over token windows with replacement; full corpus available does NOT mean a full epoch completed. All raw/cache files ignored. Data acquisition/preparation done locally before renting GPU.

Planned first measured comparison:10M vs30M, same corpus/tokenizer/context256/batch32, each300 seconds including periodic evaluation/sampling. AdamW6e-4 peak LR,20-update warmup then wall-time cosine decay to10%, BF16, no compilation overhead, clip1.0. Fixed evaluation windows and separately preserved sampling RNG; save initial/periodic/final/selected samples, selected weights, final weights+optimizer/RNG state. Wrapper checks selected-model samples in a fresh process. No GPU workers started at this note; no cost yet for scratch trials.

S2 preparation update: full 2,733,269,592-byte dump downloaded and official SHA1 verified. Extraction completed in278.69s:2,304,425 main-namespace pages including598,071 redirects;9,375,897,956 original UTF-8 text bytes. Train2,281,455/dev11,467/test11,503 pages. Added verified source URL/checksum to extraction manifest after completion (metadata only). Starting local CPU tokenization; scratch GPU spend remains zero.

S2 local-data policy: user requested all data inside THIS repository. Confirmed full Wikipedia dump, extracted JSONL, tokenizer and in-progress token binaries live under repository .cache/. Copied historical Wolne Lektury ZIP from reference repository to .cache/scratch-corpora/falenty-wl/wolnelektury.zip and verified pinned size/SHA256. No external symlinks in datasets or scratch corpus directories. Anchored scratch CLI default paths to script repository, documented repository-local uv cache, and changed example rebuild outputs from /tmp to .cache. Large local data remains gitignored; small curated datasets and provenance stay versioned. Modal training will use a remote working copy, retaining local source data.

S2 visible-data correction: user requested no hidden folders for participant-facing data. Moved both corpus directories from .cache/ to data/ (filesystem rename; no re-download). Updated scratch defaults, documentation and local manifest source paths; /data/* is gitignored except its README. Internal uv cache alone stays hidden. Tokenization finished before moving: train3,140,443,962/dev15,866,600/test16,016,089 tokens; all article round-trip checks passed. Prior .cache corpus paths in notebook entries are historical and superseded.

S2 GPU preparation status: no scratch GPU run started yet; no training losses/generations measured. Began uploading five prepared files (train/dev/test binaries plus tokenizer and manifest) to Modal /datasets/wiki-scratch-v1 using visible datasets/local/wiki-scratch-upload staging hardlinks. Local originals remain in data/. Current Modal public rates checked: L4 $0.000222/s, CPU $0.0000131/core/s, RAM $0.00000222/GiB/s. Budget estimate for two300s workers at2CPU/16GiB: $0.170232 before startup/evaluation/reload overhead; expected total compute roughly $0.20–0.30, not actual billed cost.

S3 tokenizer education: generated TOKENIZER_EXPLORER.html, offline interactive visualization embedding all7,935 actual Wikipedia BPE merge rules. Eight example encoding traces checked for exact token-ID agreement with tokenizers0.23.2 and text round trips. Separates frozen-rule encoding, saved training merge order (no historical frequency claims), and editable character-level toy BPE training with frequency counts/nonoverlapping replacements. Node DOM-stub checks covered every example step, merge-list boundaries, and overlapping pair counting; not a browser-layout test. Builder: uv run scripts/tokenizer_visualization.py; --text adds custom verified examples. Online reference: Cornell CS4782 2026 BPE/WordPiece visualizer.

S2 first GPU attempt ap-REDACTED009 failed before first optimizer update: optimizer.param_groups incorrectly called as a function. Corrected list iteration. No trained-model result from that attempt; worker overhead cost not yet measured, must not report total scratch GPU cost as zero.

Renamed the generated tokenizer explorer to visualizations/tokenizer.html and updated its builder default and documentation links. Earlier uppercase references are historical.

Tokenizer visualization simplified on request: removed tutorial sections, toy trainer, rule tables, token IDs, animations and explanatory bulk. Kept one selected text, monospace rendering, a merge slider/back/next and the Cornell link. Literal Unicode text stays intact; boundaries inside multi-byte letters are counted but not drawn through a glyph. Generator still verifies final token IDs against the real tokenizer.

Tokenizer UI revision: three authored multi-paragraph samples; full merges on initial load and sample changes. Persistent per-character spans preserve text layout while only background colors change. No underlines, added gaps, arrows or merge equations. One slider labeled Bytes → Full merges, token count, example selector and Cornell link. UTF-8 boundaries inside glyphs shown as proportional color bands. Adjacent tokens use distinct colors.

Tokenizer hover: committed approved paragraph explorer as4c3c305. Added hover showing actual token ID and a binary merge tree from the encoding trace; internal nodes labeled with learned-rule ranks (1-based), leaves with bytes. Hover follows individual byte-color bands inside multibyte characters. Only background changes during slider movement; character nodes remain fixed. Node checks verified tree concatenation, rank ordering, byte leaves and tooltip rendering across all three paragraphs at raw/intermediate/full stages; browser layout not screenshot-tested.

Tokenizer hover selection: hovering now highlights the complete selected token in amber, matching the token whose ID/tree is displayed. Leaving restores its original colors; no text layout changes. Byte fragments inside Unicode glyphs keep proportional highlighting.

S2 completed: Modal app ap-REDACTED004 exited normally after both sequential runs.

ScratchGPT-10m: 10,244,160 parameters, 6,929 updates, 56,762,368 token presentations, 303.60s training; dev 9.0643→2.3888, test 9.0627→2.2848; peak VRAM 1.79GB; worker 350.98s, estimated $0.099580.

ScratchGPT-30m: 29,893,120 parameters, 3,290 updates, 26,951,680 token presentations, 304.89s training; dev 9.1016→2.4743, test 9.0811→2.4003; peak VRAM 2.95GB; worker 351.91s, estimated $0.099845.

Both development-selected checkpoints are final and reproduce all four128-token continuations in a fresh process. Successful worker estimate total $0.19942460, excluding prior failed worker, image build/startup/storage; actual full bill not retrieved. No remaining scratch worker in this completed app. 10M processes about2.1x more tokens and gets lower held-out loss at equal time; one seed and fixed16,384-token evaluation windows, not a broad model ranking. Generated outputs learn wikitext formatting/links/template fields but invent geography/history and show repeated fragments. Neither reliably knows Warsaw is a city: both start its continuation as a village. Token presentations correspond to1.807% and0.858% of the3.14B pool, with replacement, not completed corpus passes. Reports: results/wiki-scratch-results.html and wiki_scratch_example_results.md.

## S4 — One-hour parallel scratch scaling experiments (2026-09-08; starting)

User authorized1.5h experimentation, several runs in parallel, asking about$1–$10 pretraining and substantially better output. Plan three fresh3600s runs:10M/L4,30M/A100-40GB,98M/A100-40GB. Same8k tokenizer/full3.14B raw-wikitext pool, context512,batch64,seed42,AdamW,100updatewarmup,cosine schedule. PeakLR6e-4 for10M/30M,4e-4 for98M. Evaluation remains fixed256token windows from prior experiments for direct loss comparison. Different model/GPU choices target practical output per dollar, not a controlled GPU benchmark. Public Modal rates checked; configured worker hourly estimates$1.021392 and$2.320992 eachA100, total$5.663376 for timed hour, plus evaluations/reloads/builds. Expected budget$6–$8, three4200s worker timeouts and no configured retries. Budget1USD quality snapshot at first5min checkpoint reaching$1 worker compute (may overshoot), plus initial and selected quality checks. Ten fixed curated fact preferences and eight free generations; not a held-out factual benchmark. ExistingCPU model tests passed; full trainer fixture added to catch orchestration errors before rental.

S4 baseline quality control: evaluated original five-minute checkpoints with the same new frozen diagnostics on one20.873s L4 worker ($0.005922 estimate). 10M:4/10 candidate facts, repeated4gramfraction0.036;30M:5/10,0.144. Both prefer wieś for Warsaw; Poland preference is rzeka for10M andwieś for30M. These are candidate rankings, not literal sampled answers. Both baseline best.pt weights also downloaded to repository runs/ (gitignored).

S4 correction while running: user clarified1.5h is total experimentation, with workshop-length individual runs. One-hour schedules were a misinterpretation. Stop the current app after preserving first5min checkpoints (before10min training), and cap subsequent training at600s. Change local wrapper defaults/caps accordingly. Preserved checkpoints used for diagnostic comparison only; their cosine schedule was planned for1h and must not be relabeled as completed5min recipes.

S4 stopped app ap-REDACTED022 at~15:48UTC after all5min checkpoints. Next batch five fresh600s runs:10M/L4,30M/A100-40GB,30M/H100,98M/H100,~291M/H100. Estimated configured timed compute $2.64 plus initialization/evaluation/save overhead. Context512,batch64,peakLR6e-4/4e-4/3e-4 bysize,100updatewarmup,600s cosine schedule. This respects workshop runtime. Source and tokenizer unchanged. No more hour-long training.

S5 corpus comparison: historical Wolne Lektury archive prepared in74.9s using byte-identical Wiki8k BPE.7,157 normalized canonical URLs,5,880 retained nonempty literary bodies;1,277 empty/literal-None entries excluded and logged. Train5,263 bodies/101,330,998 tokens;dev301/7,149,312;test316/6,282,807. Canonical URL and exact-body duplicate grouping; semantic anthology/part overlap not excluded. Recognized footer paragraphs removed conservatively; a few unrecognized notes retained. All local files in datasets/local/wl-scratch-v1 with hashes/verification. Historical corpus, not current-complete catalogue.

Launched three fresh600s literary runs:10M/L4,30M/H100,98M/H100. Samecontext512/batch64 and size-specificLR as currentWiki trials. Literary continuation prefixes recorded in manifest; Wikipedia factual probes skipped rather than presented as meaningful literary-model evaluation. Fixed evaluation windows are within each corpus; cross-corpus losses are not directly compared. Expected incremental compute under$2 including overhead. CPU thread count bounded to2 for futureGPU worker initialization.

S5 packaging correction: first literary app ap-REDACTED016 could not import scratch_long_modal inside workers; stopped to prevent startup retries. Extracted a plain shared scripts/scratch_worker.py and mounted it explicitly. Restarted literature batch successfully; all three are training. Startup overhead for failed import app not yet measured and excluded from successful-run estimates. Trainer CLI hard cap restored to600s following clarification.

S6 filtered Wikipedia opening corpus ready:531,258train leads/177,122,441tokens;dev2,644/881,558;test2,719/911,570. Generic rules: nonredirect source length>=4000chars, bold-start opening before firstheading,200–4096chars,>=40%alphabetic. Original substrings and inline markup retained, original train/dev/test assignments unchanged; no named-entity-based selection. Exact lead duplicates do not cross splits. Prep85.2s; detailed datasets/local/wiki-leads-v1 provenance/verification/hash-selectedexamples. Two600s H100 trials planned30M/98M, plus a cheap10M/L4 control with originalcontext256,batch32,warmup20. Full-Wiki fixed dev/test loss also evaluated after filtered-lead training for a common reference.

Training loop now skips periodic evaluation in final15s, since final evaluation already follows the timed loop; avoids the prior12–23s evaluation overshoot at the600s boundary. No training extension.


## S7 — Completed workshop-length comparison (2026-09-08)

GPU experiments finished at16:33UTC, about56min after session start; all scratch apps stopped with zero tasks. Fourteen new600s runs completed, plus two earlier300s baselines evaluated. The mistakenly scheduled hour runs were stopped after their five-minute snapshots; no hour-long training completed. Early600s runs crossed the timer during periodic evaluation (606–623s); later scheduler skips the last periodic evaluation and finishes at600s. Saving/evaluation/reload remain outside the timed loop.

- scratch-cheap-10m-1788883603936935522: 10,244,160 parameters, 118,284,288 token presentations, 600.01s training, 676.09s worker, estimated$0.1918, selected test loss2.1011, reload equalityTrue.
- scratch-h100-100m-1788882631021965890: 98,323,200 parameters, 202,801,152 token presentations, 612.18s training, 677.21s worker, estimated$0.7847, selected test loss1.7013, reload equalityTrue.
- scratch-h100-300m-1788882638087661704: 291,025,920 parameters, 81,887,232 token presentations, 623.09s training, 846.45s worker, estimated$0.9808, selected test loss1.8675, reload equalityTrue.
- scratch-h100-30m-1788882630859986367: 29,893,120 parameters, 442,171,392 token presentations, 606.61s training, 669.75s worker, estimated$0.7761, selected test loss1.7138, reload equalityTrue.
- scratch-leads-100m-1788883601228295396: 98,323,200 parameters, 200,540,160 token presentations, 600.04s training, 670.95s worker, estimated$0.7774, selected test loss1.8236, reload equalityTrue.
- scratch-leads-30m-1788883602112335036: 29,893,120 parameters, 440,762,368 token presentations, 600.01s training, 645.35s worker, estimated$0.7478, selected test loss1.8180, reload equalityTrue.
- scratch-popular-30m-1788884529176298583: 29,893,120 parameters, 424,280,064 token presentations, 600.02s training, 646.15s worker, estimated$0.7487, selected test loss2.8976, reload equalityTrue.
- scratch-tiny-10m-1788884528754010282: 10,244,160 parameters, 120,659,968 token presentations, 600.03s training, 649.62s worker, estimated$0.1843, selected test loss1.6226, reload equalityTrue.
- scratch-tiny-30m-1788884529630737279: 29,893,120 parameters, 441,352,192 token presentations, 600.00s training, 659.70s worker, estimated$0.7644, selected test loss1.3873, reload equalityTrue.
- scratch-wl-100m-1788883120565596531: 98,323,200 parameters, 201,719,808 token presentations, 606.28s training, 660.35s worker, estimated$0.7652, selected test loss2.8056, reload equalityTrue.
- scratch-wl-10m-1788883119252956273: 10,244,160 parameters, 100,401,152 token presentations, 606.61s training, 651.32s worker, estimated$0.1848, selected test loss3.1825, reload equalityTrue.
- scratch-wl-30m-1788883120289174941: 29,893,120 parameters, 447,119,360 token presentations, 611.81s training, 654.00s worker, estimated$0.7578, selected test loss2.7821, reload equalityTrue.
- scratch-workshop-10m-1788882632908163139: 10,244,160 parameters, 100,499,456 token presentations, 608.79s training, 671.59s worker, estimated$0.1905, selected test loss2.3035, reload equalityTrue.
- scratch-workshop-30m-1788882634230228165: 29,893,120 parameters, 206,962,688 token presentations, 610.49s training, 700.47s worker, estimated$0.4516, selected test loss1.8526, reload equalityTrue.

Recommendation: TinyStories30M/H100 is the clearest readable-text demonstration ($0.764);10M/L4 costs$0.184 with more logical errors. English first-shard subset, not all TinyStories; new8k English BPE and documented exact-overlap removal. Polish literature30M/H100 ($0.758) demonstrates literary style but imperfect grammar/logic. Historical WL archive is not current full catalogue. FullWiki30M/H100 and98M/H100 improve common test loss to1.714/1.701;291M worse1.867. Generated entity facts remain wrong. Filtered98M ranks8/10 curated candidates correctly but calls Warsaw a railway station; candidate scores do not prove factual generation. Alternate prompt formats on three models failed too.

Popular-article30M severely overfits:4.54M training-token pool,424M presentations, finaltrain0.133/dev5.474/test5.304; bestdev selectsstep1357 instead offinal12948. Final and selected samples both preserved. Tiny popular heldoutset40dev/46testarticles makes this an illustrative failure rather than broad benchmark.

Costs: completed current-session training workers$8.305917918; inference-only$0.019360728; two stopped-app conservative resource upperbounds total$0.957695680. Combined including those bounds$9.282974326, excluding build/startup/storage; not an invoice. Original five-minute baselines$0.199424596 are outside this session. Details research/scratch/experiment_costs.json.

Results and caveats saved in results/pretraining-findings.md, results/pretraining-results.html, pretraining_example_results.md. Single-recipe scripts/scratch_recipe_modal.py prevents accidental matrix launches; CLI imports checked, shared worker is GPU-tested but new single wrapper not rerun on GPU. All data remain local data/, weights local runs/ (ignored). scripts/verify_pretraining.py audits arithmetic, dev-selection, tokenizer provenance, recorded reload equality and diagnostic calculations; it does not deserialize weights or independently rerun inference.

Final local verification: all14 new completed runs pass scripts/verify_pretraining.py --require-weights; both best.pt and final.pt present. Sixteen-run report covers five distinct corpus categories, all recorded GPU fresh-process reload checks match, changed script syntax and documentation links pass, git diff --check clean. Checkpoint/data gitignore behavior confirmed. Original baseline final-checkpoint copies are being completed separately; no GPU remains active.

Baseline checkpoint copies also finished. All16 completed runs now pass --require-weights with local best.pt and final.pt. Experiment and artifact work complete within roughly61min of the90min limit.


## S8 — Detached Polish-only experiment batch

User authorized up to$10/run and$100 experiments, requiring completion after laptop closes. Duration clarification is pending; preserved prior600s training cap. Launched modal run --detach additional/scripts/polish_remote_experiments.py::orchestrate --seconds600. App ap-REDACTED002; batch polish-1788888781465950317. Remote controller persisted eight function call IDs (research/scratch/polish_remote_manifest.json), starts at most4H100workers, no retries, handles failures, and runs audit/report remotely. All artifacts committed to model-training-workshop volume /runs/ and /experiments/<batch>. Expected about$7–$10 successful worker compute; conservative timeout resource bounds$9.26976/run,$74.57904/batch including controller, excluding build/storage.

Eight recipes: Wiki98M/291M uniform or mixed; Wiki98M enriched openings; historicalWL30M/98M/291M. Mixed batches use50% fullWiki random windows and50% filtered-lead windows (half those at article starts). Openings mode uses filtered-lead windows only, half at starts. No English/TinyStories runs. Heldout evaluation remains original fullWiki windows for Wiki variants. Seed42,context512,batch64,600s cosine schedule. Full baseline trainer fixture and new mixed sampling fixture pass; cloning x/y prevents overlapping-view writes when replacing sampled rows. New run metadata records sampling mode and mixture path.

Retrieve after return: uv run additional/scripts/fetch_polish_experiments.py --weights. This downloads reports/metrics/checkpoints locally without starting GPUs. Existing corpus originals remain data/; remote working copies already uploaded. Remote completion does not require any local polling or postprocessing.


S8 results fetched: remote manifest complete, all8 runs successful; training-worker compute estimate$6.394607363 excluding controller/build/storage. All fresh-process reload flags pass. No factual breakthrough: Warsaw parish/village in all5Wiki variants.98M mixed7/10candidatepreferences but wrongfreeanswer; fullWiki98Mtest1.7103 vs mixed1.7370,291M1.8641/1.9027,opening-only98M2.3433 on commonfullWikiwindows. WL30Mtest2.7844,98M2.8009,291M2.9344. These are600s runs, NOT experiments consuming$10/run. Results and exact excerpts saved results/polish-remote-results.md; remote HTML/fullsample report downloaded under runs/polish-1788888781465950317/.


## S9 — Actual near-$10 runs, detached

User explicitly requested experiments at about$10 each, superseding earlier ten-minute limit. Launched4parallelH100 runs with8000s (2h13m20s) training from random weights: Wiki98M uniform, Wiki291M uniform, Wiki98M mixed, historicalWL98M uniform. SameWiki8kBPE,context512,batch64,seed42,AdamW,100updatewarmup,time-basedcosine; LR4e-4 for98M/3e-4 for291M. Evaluation/samples every600s, final and dev-selected quality, fresh-processreload, artifactaudit and HTML/Markdownreport allremote. No automatic retries.

App ap-REDACTED006, batch polish-dollar-1788900395083493729; launched modal run --detach additional/scripts/polish_remote_experiments.py::orchestrate --seconds8000 --dollar-runs. Configured H100+2CPU+16GiB rate$0.00115872/s, training estimate$9.26976/run plus evaluation/reload; expected$9.40–$9.70/run,roughly$38batch.8500s worker timeout gives$9.84912 resource-time bound/run (build/storage excluded), four workers plus worst-case controller~$39.82, leaving ample room under$100 including prior$6.39batch. No actual charges/results yet. Rates rechecked https://modal.com/pricing.

Ordinary trainer retains600s default safety limit; explicit research_limit_seconds can now reach8400, remoteprofile requires8000. FulltrainerCPUfixturepassed after limit change. Controller now treats a failed artifactaudit as report failure instead of silently ignoring it. Sampling/corpus labels clarify mixtures. Download latest batch later using uv run additional/scripts/fetch_polish_experiments.py --weights; latest pointer stored research/scratch/latest_polish_batch.json. Originaldata remain locally under data/, remoteoutputs onvolume until fetched.


S9 results (2026-09-09): all4near-$10runs completed and passed remote audit/reload. Worker estimates Wiki98M$9.3732,Wiki291M$9.3979,Wiki98Mmixed$9.3825,WL98M$9.3743;total$37.527892 excluding controller/build/storage. CommonWiki test losses1.30128/1.28600/1.36619 versus tenminute1.7103/1.8641/1.7370. Wiki291M correctly opens Mickiewicz aspoet andChopin aspianist/composer, then fabricatesbiographies (Mickiewiczbirth1910); Warsawstillonrailwaystation/village. Curatedfacts7/10,7/10,8/10 do notmean truthfulgeneration. WL beststep24410 around40min,test2.74213, finalstep81700test3.23343 withtrain1.70117/dev3.28435: clearoverfit. WLselected Uuuuu characterloop notdetectedbyword4grammetric0. Selectedcheckpoint is earlierthanfinal; reportslabelthis. Fullreport fetched to runs/polish-dollar-1788900395083493729; summary+literal samples polish_dollar_results.md. No furthertraininglaunched.


## Tokenizer frequency audit (2026-09-09)

User asked whether BPE8192 creates too many rare token types. Counted every ID in local train.bin for Wiki andWL with chunkednumpy.bincount (5.6sCPU,noGPU). Saved research/scratch/token_frequency_audit.json. Wiki3,140,443,962positions: median token-type frequency91,848;67types below100uses (49zero, rarest include byte/controlfallbacks),104below1000. WL101,330,998positions using sameWikiBPE: median741;645unused,1328below10,2391below100. Below100types account for0.04765%ofWLtokenpositions; unused Wiki markup pieces include ]]., |-, >[[, png. These are fullpreparedcorpuscounts, NOT exact sampled trainingexposures. Wikipedia doesnotshowbroad tokenrarityproblem; WLshows tokenizer-domainmismatch. Actual encoding Warsaw: Warszawa| jest| stoli|cą| Polski|.; Mickiewicz: A|dam| Mi|ckie|wicz| był| pol|skim| po|et|ą|.

Recommendation hypothesis, not measured optimum:8kbaseline sensible; compare4k/8k for10–30M and8k/16k/32k for98–291M, equalcompute with heldoutbyte-normalizedloss. ForWL retrain tokenizer onWLtrainingtext, compare4k/8k/16k beforeclaiming vocabsize is thecause. Retraining tokenizer changesIDmapping; requiresnewpretraining or explicitembeddingmigration, not swapping it underexistingweights. Literature: Scaling Laws with Vocabulary (arXiv2407.13623) supports jointdependenceonmodel/compute/data, not oneuniversalvocabsize.


## Repository cleanup and publication check (2026-09-17)

Keep Prawko scripts, uv lockfile, prepared datasets, reports and small run records in Git. Consolidated identical downloaded source spreadsheets under ignored `data/prawko/source.xlsx`; added a scoped ignore for regenerated dataset source spreadsheets and documented the download/rebuild command. Both Prawko unit tests and verification of all five saved runs passed; no new GPU jobs or training costs. Current candidate files and all 1028 reachable historical blobs passed targeted checks for personal home paths and recognizable credential tokens. This is not a guarantee against every possible secret format. Earlier full Gitleaks review found only verified false positives.

Public release still needs a decision about supplied film text: `datasets/chlopaki.md`, derived dialogue and historical copies have no recorded redistribution permission. Ignoring or deleting current files does not remove historical copies. No publication performed; no root software licence selected. Experiment notes remain intentionally included.


## Personal-information cleanup (2026-09-17)

User confirmed keeping author name and email and requested a privacy-focused release check while retaining research materials. Rewrote all seven commits to replace the Modal workspace login and 36 remote app/job identifiers with placeholders. Personal home paths had already been removed. Rescanned all 1173 reachable historical blobs: no original account identifiers, personal home paths or recognizable credential tokens matched. Private original-history backups stay under ignored `data/publication-audit/`; do not include them in a public archive. Broadened the runtime-log ignore to cover nested run logs. Existing historical logs remain as sanitized experiment records. Author metadata preserved as requested; no remote push performed.


## Workshop repository layout (2026-09-17)

Reorganized the root around the current three-hour workshop. README links the six pipeline stages; participant guides are in `docs/`, older proposals in `docs/notes/`, runnable Python and adjacent uv lockfiles in `scripts/`, model choices in `scripts/models.json`, standalone results in `results/`, the BPE explorer in `visualizations/`, and unit tests in `tests/`. The notebook stays at the root. Existing `data/`, `datasets/`, `research/` and `runs/` stay in place; recorded run source snapshots and training datasets were not rewritten. Moved the obsolete root bytecode cache into the ignored tool cache.

Updated script-relative repository paths, Modal mounts and remote imports to mirror the new layout; updated documentation links, commands and report output defaults. Validation: 19 standard-library tests and four CPU scratch-model checks passed; all five Prawko artifact verifications passed; 17 Modal modules imported with 61 local/remote file mounts checked; real Modal CLI help loaded the relocated Prawko wrapper. Tokenizer rebuild exactly matches the existing explorer. Prawko and pretraining charts rebuilt into ignored `data/reorganization/`; local documentation links checked. Lockfiles and model registry content unchanged. The full pinned local Prawko environment could not be resolved offline because a Transformers wheel is not cached; its CLI was checked using the standard-library environment. No remote training or paid GPU tests started.

## 2026-09-17 — Participant documentation cleanup

README now lists content and setup, without a timed agenda or instructor instructions. Shortened the four exercise guides; removed redundant agenda and index pages. No additional reference copies: detailed experiment history remains in this notebook, results and Git history. Commands use `uv tool install modal` (tested version 1.5.0), then `modal`. Kept one-time corpus preparation folded into the pretraining guide. No training code, datasets or recorded results changed; no paid experiments run.

Participant cleanup: renamed `docs/` to `workshop/`, moved background notes to `additional/notes/`, expanded acronyms and added workshop attribution. Updated active Modal pins to 1.5.5; historical run records retain their original versions. Research removal is pending the user’s choice.

Validation: Modal client 1.5.5 installed in the local uv cache; Prawko Modal CLI help loaded successfully. All 19 CPU unit tests passed and updated Markdown links resolve. No GPU jobs launched.

## 2026-09-17 — Keep raw runs local

User chose to retain useful research conclusions but untrack the large collection of raw run files. All 1,467 previously tracked files under `runs/` are retained locally, unchanged, and the whole directory is now gitignored. Existing Git history remains intact. `results/`, research manifests, background notes and this notebook remain versioned, including failed experiments and cost comparisons. Fresh clones contain the saved reports, but report regeneration and raw-run verification require the original local artifacts or newly completed runs.

Verified SHA-256 hashes for all 1,467 files before and after untracking: unchanged. Git tracks no `runs/` files, and the ignore rule covers future run outputs.


## 2026-09-17 — Participant tokenization and training reports

- Included the exact existing Wikipedia 8,192-entry tokenizer in `datasets/wiki-tokenizer.json`; tokenization demo now works without the corpus download. `tokenize_text.py` inspects text/file previews or trains BPE on full UTF-8 files. Demo: 29 characters → 11 tokens, exact round trip.
- Added `training_report.py`: offline training/development curves and matched before/after examples for scratch, poetry and Prawko. The workshop Modal entrypoints create it after results return. Terminal metrics remain the during-run feedback; no live browser transport added.
- Verified reporting against existing scratch, poetry, Prawko SFT/RLVR and baseline records. No new paid training; these changes do not alter training objectives or model settings.
- Guides now give dataset source links/sizes, tokenizer commands, literature preparation, artifact locations and poetry custom-prompt comparison. Poetry plots training loss only; Prawko plots development accuracy rather than comparing unlike SFT/RLVR losses.


## 2026-09-17 — Clear workshop path and Python 3.14

- README now gives the commands in execution order: literature preparation, tokenization, scratch training, Polish Driving Licence Exam SFT and RLVR, then experiments with measured costs. Removed folded setup and manual volume/upload steps.
- `prepare_pretraining.py literature|wikipedia` handles download, local preparation/checksums, volume creation and upload. Real literature check completed against Modal: matching metadata/file sizes found, no upload needed. Tests cover corrupted local data, reuse, and missing-remote uploads. Fresh full-corpus download/rebuild was not repeated.
- Moved research manifests to `additional/research/` and tokenizer explorer to `results/tokenizer.html`; updated executable source paths and participant links.
- Removed the unsupported Python <3.14 restriction. Script minimum and Modal images now use 3.14; existing uv locks refreshed. Pinned GPU requirements resolve as Linux Python 3.14 binary packages. On local Python 3.14.7: 22 CPU tests and four scratch-model checks passed, as did tokenizer round trips and literature checksum verification. GPU training has not been rerun on the new Python image; historical timings/costs remain measurements from the previous image.


## 2026-09-17 — Participant-first repository layout

- Four numbered guides at the root; no `workshop/`, `assets/`, `config/` or `data/` directories. Poster stays at root. `datasets/` means inputs, `results/` shared examples/visualizations, `runs/` newly generated outputs.
- Moved all existing downloaded/prepared inputs to ignored `datasets/local/` without deleting them. Model registry and tokenizer template live beside their scripts. Style Modal mounts explicitly exclude local corpora/backups.
- Moved 25 research runners/report builders into `additional/scripts/`. Added a latest-result viewer with explicit offline `--example` mode and six-word RLVR report support.
- Included a complete report from existing literature run `scratch-wl-30m-1788883120289174941`: test loss 9.073 → 2.782. No new model outputs invented, no GPU retraining performed for this reorganization. The main RLVR exercise is six-word stories; exam RLVR remains optional.
- Kept the measured full historical literature recipe (123 MB download); a smaller bundled pretraining recipe would require its own training validation and is not presented as tested. Independent post-training exercises and included reports let participants continue while it downloads.


## 2026-09-17 — Data guide revision and cloud preparation check

- Rewrote data/tokenization guide with direct dataset links, size bullets, prominent BPE explorer, plain tokenizer path and further reading. Removed the stock literary excerpt and meta-instructions.
- Renamed the participant recipe `literature` to `wolne-lektury`. Added CPU-side Modal preparation to avoid each laptop downloading and uploading the corpus over workshop Wi-Fi.
- Cloud Python 3.14 image built successfully; existing Wolne Lektury prepared data passed full checksum validation and was reused.
- Fresh-path testing found the historical `codebased.xyz/files/i/wolnelektury.zip` endpoint returns HTTP 404. A first temporary test harness also failed due to its import path and was stopped; a corrected worker reached the actual download. No fresh tokenization or GPU training was claimed. Wikipedia cloud preparation is implemented but not rerun.
- The exact historical ZIP remains locally available (123,071,225 bytes; SHA256 `1a25be256ee13a4a39c9a1c549d4a3f363bf2e4ad673f8e1c34e25473c43e15b`). Requested approval to publish it as a GitHub Release asset; no release has been published. Fresh-account readiness is explicitly marked pending in the guides.
- All 22 CPU tests passed after recipe renaming. No GPU jobs launched.


## 2026-09-17 — Dropbox mirror and participant-flow validation

- Replaced the broken historical source URL with the user-provided Dropbox direct-download link in `additional/research/scratch/sources.json`. Fresh Modal CPU preparation downloaded and SHA256-verified all 123,071,225 bytes, tokenized the corpus, and verified each binary output. Elapsed inside worker: 179.80 s; tokenization 170.95 s. Train/dev/test token counts and hashes exactly match the previous corpus (101,330,998 / 7,149,312 / 6,282,807). Approximate reserved CPU+memory compute: $0.00790; startup/storage excluded. No release publication needed.
- Added live charts without changing the participant launch commands. Workers send metric records through an ephemeral Modal queue; a local HTML file refreshes every three seconds. `view_results.py` selects a fresh active chart, otherwise a completed report; `--example` remains offline. Pretraining now evaluates development loss every 60 seconds instead of 300 seconds to make progress visible; the wall-time budget remains 600 seconds.
- One pretraining test failed at update 25: the new callback name collided with the time-based learning-rate schedule variable. Renamed the schedule variable, added a regression test through the actual CPU training loop beyond update 25, and restarted. Failed worker: 26.77 s, estimated $0.0310; included separately from successful-exercise costs.
- Python 3.14 checks: 25 standard-library tests and five CPU model tests passed. Local tokenization, file inspection, training a tokenizer and decoding passed in 0.04–0.63 s per invocation with dependencies already cached. Main GPU image cold build: 69.85 s.
- Driving-exam SFT completed: Qwen3.5-0.8B, 100 training questions, 181.45 s training, 230.67 s worker, 321.14 s full CLI including image build. Estimated worker cost $0.06545. Test 21/40 → 27/40; selected epoch 3 via development accuracy 23/25; reload matched. Run: `prawko-sft-1789672433144290591`. The Hugging Face model cache was already present, so these timings do not benchmark a cold model download.
- Headless Chrome checks: tokenizer loads without JavaScript errors; live pretraining/RLVR charts refresh and contain real streamed points; completed SFT chart stops refreshing and links to its final report. Screenshots and raw logs are in ignored `runs/flow-validation/`.

- Completed Wolne Lektury ScratchGPT-30M: 600.00 s training, 670.06 s worker, 691.71 s full CLI (image already built), $0.77641 estimated worker compute. Test loss 9.073 → 2.820. Fresh-process reload matched; artifact audit passed 493 checks (weights remain on Modal). Run: `scratch-wolne-lektury-30m-1789672528343949120`.
- Completed Qwen3.5-4B six-word RLVR: 603.60 s training, 669.26 s worker, 762.64 s full CLI including image build, $0.18988 estimated worker compute. Test compliance 1/32 → 24/32; dev 0/24 → 23/24; selected step 60 of 66. Reload matched; all six evaluation files independently rechecked against the verifier. Run: `rlvr-train-six_words-1789672431850535000`. This is weaker than the older 32/32 run; neither result should be presented as guaranteed.
- Successful default exercises plus fresh data preparation cost approximately $1.040 in worker compute; including the failed pretraining attempt, $1.071. Builds, startup and storage are excluded. GPU weights were cached. Optional exam RLVR and full Wikipedia preparation were not rerun in this validation.
- Shared `results/workshop-check.html` preserves all three curves and matched before/after outputs, timings and cost assumptions. Browser rendering checked. Raw logs/screenshots stay in ignored `runs/flow-validation/`.

## 2026-09-17 — Edit text directly in the tokenizer explorer

- Main participant activity is now browser-based: open the explorer, Edit text, Show tokens, slide through merges and hover for IDs/history. No HTML rebuild for a new paragraph, no notebook environment required. CLI file inspection and training a new tokenizer remain optional.
- Embedded the saved 8k vocabulary, byte alphabet and learned merge ranks in the standalone page. Custom text stays local, with a 2,000-character limit. Browser tracing uses the tokenizer's ByteLevel pre-tokenizer rules and exact BPE ranks, not an approximate word split.
- Verified 40 browser traces against Hugging Face Tokenizers, covering Polish, emoji, combining marks, whitespace, multilingual text and HTML-like input. Browser checks also confirm editable input, unchanged character positions across merges, and token hover history.

## 2026-09-17 — Overnight hypotheses and budget

User authorized up to $400 Modal experiments, ending by 08:00 Europe/Warsaw on 18 September (06:00 UTC). This is a ceiling, not a target. Workshop commit before research: 39d3c99.

- H1: H100 throughput on ScratchGPT-30M may justify its higher price; compare L4/A10/L40S/H100 at the same batch 32, context 512, 600 seconds and Wolne Lektury corpus. Compare test loss, tokens/second and tokens/dollar, not hourly price alone.
- H2: A wider/shallower decoder or context 1024 may improve short-run literary output. Compare against the same architecture family and budget; retain the existing recipe until results justify a change.
- H3: Driving-exam gains may come more from the starting model and learning rate than more epochs. Compare Qwen3.5 0.8B/2B/4B, SFT and answer-only RLVR at 600 seconds. Development selects checkpoints; rotated options test position dependence. The 40-question test is small and already inspected in earlier research, so all new comparisons are exploratory.
- H4: Scratch pretraining may help exam learning, but learning answer format does not imply driving knowledge. Reuse saved Wikipedia 100M/300M and Wolne Lektury 30M/100M; compare SFT, RLVR, SFT→RLVR and random initialization controls on identical splits.
- H5: Small scratch models can learn Q&A formatting from title→definition examples or the existing Pan Tadeusz Q&A set, but semantic correctness and generalization must be inspected separately from answer loss and verse formatting.
- Current workshop Wolne Lektury run: 327,909,376 token presentations / 101,330,998 training tokens = 3.236 corpus-equivalents. Sampling uses random overlapping windows, not sequential epochs.
- Batch A: 12 jobs, remote controller, four concurrent jobs, no training retries, per-worker timeout 3600 seconds. Conservative resource-time reservation $23.436864 including controller; excludes image builds/storage. Expected actual cost much lower.
- An initial controller launch failed during remote module import before GPU jobs began; fixed local/remote root resolution and stopped the failed app. Successful batch A ID: 1789674358034520778.

- Scratch post-training smoke batch 1789674671377052366 completed all three workers for $0.102626 estimated compute. Wiki100 exam: 12/40 before → 16/40 after SFT → 15/40 after RLVR; these are 60-second-per-stage validation runs, not optimized results. Poetry WL30: held-out answer loss 3.081 → 2.809, with visibly multi-line answers but imperfect meaning/meter. Wiki100 definition QA: 2.304 → 1.785 held-out answer loss; samples still hallucinate and repeat, so lower answer loss does not imply reliable factual QA.
- Batch B 1789674900457145088: 17 scratch post-training jobs, reserved resource-time bound $17.639424. Mostly 600 seconds per stage, LR 2e-5 following smoke overfitting at 1e-4. Includes random100 controls, Wiki100/Wiki300/WL30/WL100 exam SFT and RLVR, two exam chains, and Wikipedia/poetry Q&A. Total reservations A + smoke + B = $44.416224 plus excluded overhead; actual spend expected far lower.
- Wikipedia QA preparation: 5,000 train / 200 dev / 200 test. First plain paragraph from existing Wiki leads, deterministic lowest SHA256 ID sampling after length filtering; article revision links retained, original pretraining splits preserved. Local corpus stays ignored under datasets/local/wiki-qa-research/. QA loss reports a fixed first 50 rows per held-out split; examples are not semantic accuracy scores.

- Matched WL30 hardware results (600 s, context 512, batch 32): L4 50.0M tokens / $0.180 / test loss 3.152; A10 72.2M / $0.229 / 3.064; L40S 180.1M / $0.377 / 2.885; H100 394.4M / $0.738 / 2.784. Actual device names recorded. H100 was about 1.92× better tokens/$ than L4 here. These research runs omit the participant worker's additional quality diagnostics.
- Compiled H100 WL30: 723.7M tokens / $0.731 / test 2.748, including compilation inside the 600-second budget. Compiling only the training forward leaves inference/checkpoint serialization unchanged. Wider 30.65M/5-layer variant: 480.1M / $0.732 / 2.789; context 1024 standard model: 419.6M / $0.740 / 2.821. Neither beat the standard model's held-out loss. Added optional GPU/batch/compile flags to participant runner; exact compiled participant flow is being validated separately.
- Qwen3.5-4B failed on L4 with the original exam batch configuration (22 GiB usable GPU memory exhausted). Both failures totaled $0.03106 measured worker compute. With L4 batch 2/eval batch 2, SFT completed: 32/40 → 33/40, rotated 34/40, $0.214. L40S batch 4/eval batch 8: SFT 31/40 → 35/40 ($0.391), RLVR 31/40 → 32/40 ($0.391). Different batch shapes changed one baseline decision; avoid ranking one-question differences as stable model quality.
- Expanded training pool: 289 official text-only three-choice road-licence questions, excluding tram-only rows and all connected stem-similarity groups touching original dev/test. All original 100 training questions retained; dev 25/test 40 unchanged. Qwen0.8B LR 2e-5: SFT 21/40 → 33/40, rotated 32/40, dev-selected epoch 6, $0.190; RLVR 21/40 → 32/40, rotated 26/40, selected epoch 7, $0.187. Qwen2B expanded SFT 26/40 → 26/40 (dev 24/25), RLVR → 27/40. This mismatch between dev and test emphasizes small-set uncertainty.
- Modal preempted batch E's CPU controller and restarted it, creating duplicate child calls under a second batch ID. Canceled the four duplicates and recovered the original completed results without retraining. Future controllers use stable batch IDs, persisted call IDs, non-preemptible CPU orchestration and atomic per-run claims, so infrastructure retries cannot silently repeat GPU training. GPU preemption is distinct from retries=0; see https://modal.com/docs/guide/preemption. Canceled-worker billing is unknown; reserve all four full timeout ceilings ($4.086) in budget accounting.
- Qwen0.8B thinking-mode diagnostic: all 25 dev responses hit the 512-token cap without EOS or a valid final answer. Canceled before training; no RLVR gain claimed. Its official model card explicitly warns about thinking loops. Kept raw before-dev outputs locally; reserve the full H100 timeout ceiling ($4.171) for conservative cost accounting. Next test uses short explicit explanations in non-thinking mode, with final-letter-only rewards.
- Further bounded batches: C 1789675462186447914 ($11.772288 reservation), D 1789675548767097321 ($19.004112), original E 1789675820450108593 ($8.53272; recovered), restarted E 1789676219387996031 (duplicates canceled). F replicates expanded-data SFT/RLVR on seeds 123/2026 and tests short-explanation RLVR. No new experiments are launched solely to consume the $400 ceiling.

## 2026-09-17 — Practical recipes from the comparison runs

- H100 compilation passed the complete participant path: `modal run --detach scripts/scratch_recipe_modal.py --gpu H100 --batch-size 32 --compile-training`. Run `scratch-wolne-lektury-30m-1789676785288825614`: 600.00 s training, 664.46 s worker, 578.26M token presentations, test 9.073 → 2.760, $0.7699. Artifact audit passed 1,504 checks, including recorded fresh-process reload equality. Weights remain on Modal. Research throughput is higher because those workers omit the participant quality probes.
- Thirty-minute WL30/H100 research run: 1.260B token presentations (12.44 corpus-equivalents), test loss 2.720, $2.119. Wider/shallower Wikipedia model also failed to improve loss (1.716 versus standard 1.711). Compilation is a more useful workshop optimization than those tested architecture changes; this does not compare unrelated architecture families.
- Expanded Qwen3.5-0.8B, 289 questions, LR 2e-5, L4, seeds 42/123/2026: ten-minute SFT test 33/33/35 and rotated 32/29/32; direct RLVR 32/33/29 and rotated 26/31/26. Three-minute SFT test 32/31/31 and rotated 33/30/31, $0.071–0.072 per worker. Recommend the short expanded-data recipe as the optional workshop extension. Training already shuffles answer options; the rotated test diagnoses remaining sensitivity.
- Qwen3.5-4B expanded-data L40S: ten-minute SFT 31 → 36/40, rotated 34, $0.4024; RLVR 31 → 32, rotated 34, $0.4027. All are exploratory comparisons on the repeatedly inspected 25-dev/40-test split, not official exam pass rates.
- Exact participant command `modal run --detach scripts/prawko_modal.py --method sft --dataset expanded` also completed: `prawko-sft-1789677752484787799`, 601.65 s training, 667.45 s worker, $0.18937, test 21 → 36/40, rotated 33, dev-selected epoch 7. All metrics, source hashes, split isolation, checkpoint choice and adapter reload audited. This seed-42 repeat differed from the research worker's 33/40 despite identical data/order/hyperparameters: the first loss matched, but the first gradient norms already differed slightly (36.3671 vs 36.3704). These GPU runs are not bitwise deterministic; no guarantee of an exact score.
- Short-explanation RLVR, Qwen3.5-2B, 100 official questions, no rationale labels: strict final-line reward test 0 → 25/40, $0.7102. Crucial diagnostic: the original model placed `Odpowiedź: B` before its explanation, while every trained test output contained only `Odpowiedź: [ABC]`. Parsing the explicit letter anywhere gives **25/40 before and after**. The reward never required an explanation. This is learned format compliance/removal of reasoning, not evidence of improved reasoning or knowledge. Preserved full outputs and added the diagnostic to the comparison report.
- The three-minute expanded-data replications are batch H `1789678052365320000`. F/G/H and the participant command are finished. A longer scratch SFT→RLVR chain remains under its existing bounded controller while the report is audited.
- CPU verification: 27 standard-library tests and five model tests passed. Browser checks passed for the comparison tables, expandable curves, static GPU plot and compiled participant report. Raw logs, all records and screenshots remain in ignored `runs/`; only curated plots/reports, runnable code, plans and the expanded small dataset are tracked.

- Direct scratch-model RLVR collapsed at the last checkpoint: all 25 development answers were B for Wiki100/Wiki300/WL30, A for WL100, and C for random100. Development selection retained the initial policy in most runs. Wikipedia LoRA SFT reached 22/40 for both 98M and 291M, versus 20/40 with full-weight SFT. Wiki100 SFT→RLVR fell from 20 to 18/40 (rotated 17 to 13). Existing-Qwen chains regularize RLVR against the original base model; scratch chains use their SFT checkpoint as reference. Do not interpret these as identical KL setups.
- Final expanded-data scratch comparison: batch I `1789678636495223000`, four 600-second L4 workers, full-timeout/controller reservation $4.912848. Wiki98M, Wiki291M and WL30 full-weight SFT; Wiki291M rank-8 LoRA SFT. Same 289 train, original 25 dev/40 test, no new test tuning.

## 2026-09-17 — Completed comparison and accounting

All experiment applications finished before 23:15 Warsaw, well before the 08:00 deadline; Modal reported no active research, exam or participant-pretraining workers. No further training is queued.

- Expanded-data scratch SFT, same 289/25/40 split: Wiki98M 22/40 (rotated 24), Wiki291M 21 (rotated 22), WL30 23 (rotated 26), Wiki291M LoRA 23 (rotated 18). These do not establish exam-passing ability. The final Wiki291M SFT→RLVR chain stayed at 20/40 (rotated 18); RLVR selected its initial SFT checkpoint.
- Qwen0.8B explanation-prompt RLVR: strict final-answer score 12 → 25/40, but accepting the explicit answer anywhere changes 24 → 25. Answer-only outputs rose from 4 to 39/40. Along with the 2B trial, this is a useful reward-specification lesson, not a reasoning-success demonstration.
- **66 successful research workers: $19.2962 estimated compute.** Two exact participant-command checks add $0.9593. Two recorded out-of-memory workers add $0.0311. Known worker estimates total **$20.2866**. Billing for the four canceled duplicates and canceled thinking trial is unknown; their entire configured timeouts total an additional **$8.2570 allowance**. Image builds, actual controller billing, startup and storage are excluded from these worker estimates. Sum of all research batch resource-time reservations, including controller bounds and the duplicate batch, was **$121.8106**, not actual spending; comfortably below the authorized $400 ceiling.
- Final records are in ignored `runs/night-*`; model weights remain on the Modal volume. Public `results/training-comparisons.md` and `.html` contain all aggregate scores/curves and selected literal examples (first four, plus first correction/regression where available). GPU and repeated-exam SVG plots accompany the guides. Avoid interpreting one-question differences on the reused test split as reliable rankings.
- Verification: 29 existing-model exam stage records audited; all completed scratch post-training exam records checked for metrics, source labels, split isolation and development checkpoint selection; text samples checked for matching prompts/references. Both explanation-RLVR trials passed checks on 336 saved evaluation responses each, training IDs, sampled rewards and KL-adjusted leave-one-out advantages. Text loss was not independently recomputed from weights. The expanded dataset and provenance manifest rebuilt exactly from the original spreadsheet.
- A full-batch artifact listing hit Modal's rate limit during final retrieval. Added a single-run fetch option and retrieved only the missing worker; no training rerun or additional GPU cost. The earlier infrastructure-preemption incident and conservative canceled-worker allowance remain included above.

## 2026-09-17, resumed overnight experiments

The first sweep stopped too early. Continuing under the original $400 total Modal cap and 08:00 Warsaw, 18 September deadline. The initial 66 successful research workers were runs, not 66 distinct models. Known worker estimates were $20.29 including participant checks and known failures; $8.26 covered the full-timeout allowance for canceled calls. Reserve $50 for all earlier work and overhead while accounting for new batches separately in the ignored local budget record.

Hypotheses for the continuation:

- Compiled 100M/300M Wikipedia training may make H100 better value than L40S, as observed for 30M Wolne Lektury. Batch J compares both GPUs, adds compiled 30M and a 30-minute 100M run. Keep context, tokenizer and validation windows fixed.
- Wikipedia data quality may matter more than another small architecture adjustment. Prepare plain lead text alongside the existing raw-markup and raw-lead corpora. Preserve source splits and remove exact cleaned duplicates across splits. Evaluate on common corpora before interpreting differences: each corpus's own loss is not comparable to another's.
- Wikipedia → general Polish instruction SFT → exam SFT/RLVR may improve on direct exam training. Test both paths from identical pretrained weights. Format learning and exam correctness are separate outcomes.
- Earlier scratch post-training processed four examples individually. New optional batching gathers last-real-token logits from right-padded prompts. CPU checks compare unpadded versus batched logits and gradients. Save final as well as dev-selected test metrics and training exposure to make overfitting visible.

Instruction baseline: [emplocity/owca](https://huggingface.co/datasets/emplocity/owca), revision `ac0f6728bc6e24895abbe432a3ba04a97d43d1f6`, synthetic Polish translation/customization of Alpaca. Prepared 25,874 train / 293 dev / 267 test pairs, normalized-prompt hash split, <=500 tokens with our Wikipedia BPE, exact held-out driving-question exclusion. This is noisy data: an early spot check incorrectly assigned positive charge to neutrons. Treat it as a format-learning baseline, not a verified source of knowledge. Preparation and provenance are reproducible in `additional/scripts/prepare_polish_instructions.py`; full source and prepared data remain local and ignored.

Batch K starts with four 60-second smoke tests of batched 98M/291M instruction and exam SFT. Exam smoke tests stop at five corpus-equivalent exposures; these verify the implementation, not the final workshop training duration. Larger sweeps follow only after checking the saved outputs.

Continuation measurements and next decisions (still running):

- Matched ten-minute compiled Wikipedia training: 98M H100 processed 272.5M tokens, test loss 1.619, $0.765 worker estimate; L40S 79.1M, 1.914, $0.391. 291M H100: 95.0M, 1.790, $0.797; L40S: 23.7M, 2.480, $0.406. H100 gives approximately 1.8–2× more token presentations per dollar here.
- The roughly $0.30 instruction-SFT jobs start from the **earlier 8,000-second pretrained checkpoints**. They are not $0.30 pretraining runs. Those older 98M/291M Wikipedia runs processed 2.636B/1.096B tokens and reached raw-Wikipedia test losses 1.301/1.286. We have not established that longer pretraining has exhausted useful gains.
- Batch P adds four 50-minute compiled H100 Wikipedia runs: 30M, 98M with batch64, 291M with batch64, and 98M with a higher learning rate. Save intermediate weights around 10 and 30 minutes, plus periodic factual/continuation diagnostics. Loss alone is insufficient evidence of better knowledge.
- Three corpus-equivalent exposures of OWCA instruction SFT took about 3–4 minutes for 98M. Development loss preferred LR3e-5 over1e-4 for both sizes. Replies acquired answer-like form but still drifted and repeated; do not describe this as a competent instruction model. Batch R tests these selected checkpoints on the driving exam with the same settings as direct post-training controls.
- Batched exam RLVR with LR1e-6, beta0.1, 16 prompts and checkpoint selection on all six option permutations improved the earlier collapsed-policy behavior. The 291M direct RLVR run reached 27/40 original, 25/40 rotated; its matched slow SFT control reached 25/40 and24/40. These are exploratory single-seed results on an already inspected 40-question set, not evidence of superiority or official exam passing. Batch N's records passed metric and checkpoint-selection audits.
- Cleaned leads: 464,812 training articles /78,574,372 tokens; preparation took217 seconds on four Modal CPUs using data already on the volume. At 98M/10 minutes, cleaned-lead test loss was2.154 versus2.709 for the raw-lead-trained model evaluated on that **same** clean pool. Raw-Wikipedia loss worsened from2.199 to4.847. This is a distribution tradeoff, not universal improvement. Candidate facts were easier than free recall: the clean model scored8/10 plain candidate probes yet generated an incorrect parish description for Warsaw. Keep those diagnostics separate.
- Prompt mismatch is worth checking: the Warsaw training lead starts with `Warszawa, miasto stołeczne Warszawa...`, whereas the existing probe forces `Warszawa –`. Source-style prompts and greedy decoding will be diagnostic comparisons, not replacements for the frozen probes or a claim of general factual reliability.

`results/checkpoint-selection.svg` now explicitly marks selected versus final weights. Example: Qwen3.5-0.8B driving SFT selected step350 had28/40 test answers versus24/40 at final step856. The RLVR illustration goes the other way on test (23→24 despite worse dev): dev selection cannot guarantee the best unseen score. The report passed a browser check, and all27 standard tests plus six scratch-model checks passed.

### Reference-removal correction and superseded results

Found and fixed a real extraction bug: the paired-reference regex could treat a self-closing `<ref ... />` as an opening tag and consume prose through a later `</ref>`. Original-markup Wikipedia extraction is unaffected. Added a regression test preserving the sentence between those two references; all28 standard tests pass. The shared `strip_reference_tags` helper lives in `scripts/prepare_wiki_scratch.py` and is called only by optional plain-text preparations.

`wiki-plain-leads-v1` results (including its apparent common-pool improvements noted above) are superseded for recipe selection. The earlier5,000-definition Q&A data used the same faulty expression. Keep these records for audit, not as recommendations. Canceled unfinished S300M plain-text50-minute training and the two plain-v1 mixture jobs in Y; their costs remain conservatively reserved because canceled-job billing is not known. Raw-Wikipedia P runs and raw-Wikipedia/literature Y runs continue. The remote dependency scheduler skips V's canceled plain-v1 branch while retaining its three valid raw-data branches.

Corrected `wiki-plain-leads-v2`:467,058 training articles /81,568,077 tokens;2,327 dev articles /405,664 tokens;2,375 test articles /421,820 tokens. Preparation315 seconds on four CPUs. Exact cleaned-text duplicate exclusion and original source splits remain in place. AA reruns10-minute fresh/continued100M/300M comparisons and50-minute fresh100M/300M runs against this version.

The Wolne Lektury corpus already used exactly the Wikipedia tokenizer. A retokenization check reproduced byte-identical token files (101,330,998 train tokens). `wl-wiki-bpe-v1` is a redundant verified alias used by Y, not new data or a new vocabulary. Future mixtures should use the existing `wl-scratch-v1` directly. CPU preparation cost was small; no need to repeat that work.

### Longer runs, domain SFT and repeated controls

- Thirty-minute compiled98M raw-Wikipedia pretraining reached test loss1.426 after920.4M token presentations for$2.136 worker compute. Ten-minute98M was1.619; the earlier8,000-second98M checkpoint was1.301. This still shows gains from more training. These runs also differ in LR schedules/batch settings; this is not a controlled scaling-law estimate.
- Matched approximately100M architecture sweep at10 minutes: standard1.619, wider/shallow1.599, deeper/narrow1.696 raw-Wikipedia test loss. Wide model processed336.1M tokens versus272.5M standard. Higher LR0.0012 did not help:100M1.636,291M2.007. Continue the wider model, not the deeper one.
- The general OWCA instruction stage did not improve the first matched exam comparison.98M direct slow SFT23/40 original and24/40 rotated versus21/40 and25/40 after instruction SFT.291M:25/40 and24/40 direct versus19/40 and18/40 after instruction SFT. Instruction-style answers alone do not establish better task competence.
- Repeat seeds support a real benefit of pretraining over random weights:291M direct exam RLVR scored27/26/27 original and25/24/22 rotated across seeds42/123/2026. Random291M RLVR was15/40 and12/40; random291M SFT10/40 and16/40.98M short SFT→RLVR scored27/28/27 original and21/24/23 rotated. Still a tiny, previously inspected test set; no official-exam passing claim.
- X compares RLVR with a fairer supervised classification control: cross-entropy conditioned on the same three answer actions, plus the same exact KL penalty. This separates reinforcement learning from a difference in answer normalization. It does not teach free-form reasoning.
- Z trains grounded domain instructions from9,602 most-linked Wikipedia articles, with39 dev and43 test articles retaining their original corpus split. Three fixed prompt templates; answers copied from the first plain paragraph and shortened at a sentence-like boundary when needed. The reference-removal bug was fixed **before any Z training**. Warsaw and other familiar entities occur in its training set, so familiar-entity probes test recall, not unseen knowledge. Final as well as dev-selected weights and text are saved.
- Greedy decoding, source-like title prefixes and explicit article-start tokens were tested rather than assumed to fix factuality. They change continuations but still produce incorrect Warsaw descriptions. Do not hide these failures behind the easier candidate-choice probes.

### 50-minute Wikipedia results and continued training

Batch P completed four original-markup runs on H100. Same fixed16,384-token test pool and8,192-entry tokenizer; weights selected by development loss. Costs below are worker compute including evaluation, not total account billing.

| Parameters | Batch / peak LR | Training | Token presentations | Test loss | Worker USD |
|---|---|---|---|---|---|
|29.9M|32 /0.0006|50min|3.618B|1.5090|3.544|
|98.3M|64 /0.0006|50min|1.633B|1.3387|3.557|
|98.3M|32 /0.0012|50min|1.528B|1.4018|3.543|
|291.0M|64 /0.0003|50min|0.607B|1.3761|3.598|

The98M10-minute/30-minute/50-minute results are1.619/1.426/1.339. The earlier8,000-second98M run reached1.301. These are different schedules/batches, so do not fit a scaling law to them, but they do not justify declaring longer pretraining exhausted. `results/wikipedia-scaling.svg` and its JSON preserve measured checkpoint curves, endpoint losses, run IDs and costs. Raw continuation quality remains poor: the50-minute98M model describes Warsaw as a former administrative gromada. Better loss is not equivalent to correct facts.

Batch AD continues P98M/P291M and the earlier8,000-second98M/291M weights for another50minutes each, with batch64 and lower peak LR0.00015/0.0001. Uses new sampler seed43 rather than replaying the original seed42 sample sequence. Optimizer state resets; this is explicitly continued pretraining, not an uninterrupted100-minute run. Each worker has a one-hour hard bound, and all four together reserve$17.513 including controller allowance. Budgets retain prior work and unknown canceled costs.

### Grounded instruction recall versus generalization

Z trained on9,602 Wikipedia definitions. At LR0.00003, both98M and291M selected step500 by development loss; ten passes ended at step6002.98M held-out definition loss worsened from1.800 selected to2.665 final;291M from1.829 to2.574. Final weights can reproduce the Warsaw training paragraph, but that is memorization of a familiar entity. For example,291M final answers `Opisz: Warszawa.` with the recognizable capital-city paragraph, yet `Kim był Adam Mickiewicz?` invents a military biography. Do not use the familiar Warsaw output to claim broad instruction competence. The18 fixed instruction probes include original and new wording; raw baselines were evaluated with the same prompts in AC.

The fairer three-action supervised control X (conditional cross-entropy plus KL0.1) scored25/40 original and23/40 rotated for98M.291M seeds42/123/2026 scored25/26/27 original and23/24/21 rotated. Direct291M RLVR scored27/26/27 and25/24/22. On this small, repeatedly inspected set, those results do not support a large inherent RLVR advantage. All16 T/X/Z records passed the saved-metric/checkpoint audits.

### Larger evaluation pools and continued overnight experiments

AH evaluates eight saved models on1,048,576 tokens per development/test split, seed20260918, context256. This is a **separate** pool from the original16,384-token workshop curves. Defaults still reproduce the old pool exactly; the CPU regression fixture verifies this and deterministic custom-pool sampling. Do not mix the two sets of loss numbers.

|98M original-Wikipedia training|1M-token Wikipedia test loss|1M-token plain-v2 test loss|
|---|---|---|
|10min compiled|1.5467|2.8828|
|30min compiled|1.3744|2.6207|
|50min compiled, batch64|1.3030|2.5295|
|Earlier8,000s, uncompiled|1.2646|2.4764|

The larger sample confirms continued improvements and diminishing returns across these practical recipes. The291M50-minute/old8,000-second values are1.3279/1.2463. The wider100M50-minute model scores1.3340, behind the standard98M here despite its earlier10-minute advantage. This remains a schedule/batch comparison, not a controlled scaling law or factuality score.

AE/AF tested H100 batch utilization at10minutes.98M batch64/context512:297.8M tokens, test1.6104,15.4GB peak VRAM; batch256:325.6M,1.6378,57.2GB.291M batch64:101.2M,1.7511,36.5GB; batch128:106.8M,1.7708,68.6GB. Larger batches gave modest throughput gains, not better loss at the matched LR.98M context256/batch128 reached1.5743 on the256-token evaluation pool; the1024-context comparison is separate. Three AE configurations hit the old batch-size guard before training, costing$0.00863 total; AF retries only those after explicit support and pre-launch validation were added.

V completed nine stages and skipped the three dependencies on canceled plain-v1 training. All nine passed saved-metric audits. For50-minute raw-Wikipedia bases, direct exam SFT versus OWCA→exam SFT scored:98M24/40→20/40 (rotated25→24);291M22→27 (rotated21→18); wide100M24→29 (rotated22→20). Apparent gains in original option order do not survive rotation consistently. Do not promote these into a robust instruction-stage improvement.

AG prepares a larger grounded instruction comparison:99,938 training definitions after exact answer deduplication, plus200 dev/200 test, retaining original article splits. Three prompt templates; long answers trimmed at sentence-like boundaries; corrected reference removal. Prepare locally with `uv run additional/scripts/prepare_wiki_qa.py --train-size 100000 --output datasets/local/wiki-qa-100k`. Four pretrained100M/300M runs compare LR1e-5/3e-5, with a random98M LR3e-4 control; cap20minutes and3 sample-equivalent passes. All200 held-out examples are evaluated. Context filtering now validates lengths on CPU instead of allocating GPU tensors twice per example.

AI continues the old8,000-second98M/291M checkpoints for50minutes with either12.5% training-link-ranked popular raw leads or50% corrected plain leads mixed into original markup. Same batch64, seed43 and LR1e-4 as the uniform-data AD controls. This tests sampling and retention separately from simply adding compute. Mixture proportions and exact source token presentations are recorded; the CPU fixture checks a non-default25% mixture.

AJ tests random-initialization exam SFT at LR1e-4/1e-3. The earlier matched low-LR random controls were not tuned from-scratch baselines; do not overstate their contrast with pretrained models.

AK launches four fresh compiled8,000-second H100 runs:98M/291M original Wikipedia;98M with25% Wolne Lektury;98M with12.5% popular raw leads. Batch64, LR0.0004 for98M and0.0003 for291M. Per-worker timeout8,500seconds bounds configured worker compute below$9.85; the batch including controller reserves$40.224. Ordinary short-job bounds remain unchanged. New per-spec deadline checks and resource reservations were verified before launch. These are optional near-$10 comparisons, not a requirement for the main workshop. All training, selected-checkpoint evaluation, output saving and reload checks finish remotely; deadline remains08:00 Warsaw.

### More Wikipedia training helps loss; exam transfer is less consistent

AD finished all four 50-minute continuations. AR independently evaluated selected weights on the fixed million-token pool (context 256, seed 20260918). Optimizer resets and new sampling seed mean these are two-stage recipes, not uninterrupted runs.

| Model and starting checkpoint | Wikipedia test loss before → after, 1M-token pool | Extra worker USD |
|---|---|---|
|98M, 50-minute checkpoint|1.3030 → 1.2415|3.552|
|291M, 50-minute checkpoint|1.3279 → 1.2493|3.618|
|98M, earlier 8,000-second checkpoint|1.2646 → 1.2223|3.557|
|291M, earlier 8,000-second checkpoint|1.2463 → 1.2015|3.587|

The separate 16k-token pool gives 1.2772, 1.2837, 1.2558 and 1.2365 respectively. Do not mix pool sizes when comparing losses. All four selected their final checkpoint. Full Wikipedia still benefits from additional compute; fresh training on the much smaller 81.6M-token clean-lead corpus instead selected checkpoints around halfway through its 50-minute runs. Its final training continued to fit the training set while development loss worsened.

AS then trained the same exam SFT/RLVR recipes on these four continued models. Original/rotated scores out of 40, respectively: 98M from 50min, SFT 25/21 and RLVR 27/22; 291M from 50min, SFT 22/24 and RLVR 23/23; 98M from old 8,000s, SFT 25/27 and RLVR 23/26; 291M from old 8,000s, SFT 27/24 and RLVR 25/26. No consistent winning method or proportional transfer from lower pretraining loss. All eight metric/selection/reload audits passed. Repeatedly inspected small exam test remains exploratory.

AO tests another pretraining hypothesis: shuffled complete context windows rather than sampling with replacement. Fresh 98M and 291M, 8,000 seconds each, otherwise matched to AK raw-Wikipedia runs. Each full pass visits every complete non-overlapping block once before reshuffling. The final incomplete block is omitted. Saved sampler state includes seed, epoch, cursor and draws; seven CPU checks cover coverage, determinism, real training, non-default mixture accounting and fixed-pool evaluation.

### Short Wikipedia definitions: a visible but narrow SFT result

AG's 99,938 full-paragraph examples improve held-out answer loss, but generations still invent facts. They also fail to improve driving-exam transfer: AN's 98M SFT/RLVR scores are 20/22 and 22/20 original/rotated; 291M scores are 19/22 and 17/13. Do not present generic instruction SFT as an automatically beneficial prerequisite.

AP instead trains on 8,912 short definitions extracted from training-link-ranked Wikipedia leads. Answers are the first definition clause, at most 48 tokens, checked against their source. Examples include Warsaw's capital-city definition and “Polski poeta.” for Adam Mickiewicz. These are training facts. Held-out article splits contain 36 dev and 38 test entities.

AQ uses 100 dev and 100 test **known training facts with new prompt templates**, frozen before AP training, with exact normalized answer matching. This measures format and recall, not unseen knowledge. Scores below use the predetermined final training checkpoint, not the checkpoint selected by held-out-article loss.

| Pretrained model → short-answer SFT | Known-fact dev / test exact matches | Training | Worker USD |
|---|---|---|---|
|98M raw Wikipedia|58/100 / 58/100|30 passes, 367s|0.460|
|98M raw Wikipedia → 99k paragraph SFT|44/100 / 46/100|30 passes, 479s|0.611|
|291M raw Wikipedia|58/100 / 69/100|19.58 passes, 600s|0.763|
|291M raw Wikipedia → 99k paragraph SFT|75/100 / 75/100|22.85 passes, 600s|0.736|

Before short-answer SFT, all four score zero exact matches under this strict short-answer metric; that does not mean they know zero facts. Selecting by loss on unseen articles yields much earlier checkpoints and only 9–16 test exact matches. The objective matters: memorizing a supplied reference collection and predicting definitions of unseen entities are different tasks.

Literal final answers from the 291M Wikipedia → 99k paragraph SFT → short-answer SFT model:

- `Czym jest Warszawa? Odpowiedz krótko.` → `Stolica Polski i województwa mazowieckiego.`
- `Kim był Adam Mickiewicz?` → `Polski poeta.`
- `Co wiesz o Krakowie?` → `Miasto na prawach powiatu położone w południowej Polsce nad Wisłą.`
- `Podaj wynik: 2 + 3. Odpowiedz tylko liczbą.` → `Podstawowa nazwa danej liczby naturalnej.`

Useful narrow demonstration, not a general assistant. AU tests random initialization versus only ten minutes of Wikipedia pretraining, with the same short-answer data and a 30-pass cap, to check how much pretraining contributes. Learning rates are 3e-4 random / 3e-5 pretrained; maximum 20 minutes per worker. AP/AN/AS saved-metric audits all pass.

AT compares H200 and B200 against the existing H100 ten-minute controls at batch 64. Pricing checked against Modal's official page: H100 $0.001097/s, H200 $0.001261/s, B200 $0.001736/s before CPU/memory. Reports now distinguish requested GPU price from actual hardware: Modal can upgrade an H100 request to H200 at H100 pricing. Two AN workers received that upgrade. No B300 request: the installed CUDA build does not meet its documented requirement.
