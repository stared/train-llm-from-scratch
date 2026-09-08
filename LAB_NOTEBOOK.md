# Workshop preparation lab notebook

Maintained during experiments. Dates are Europe/Warsaw. This is the working record of hypotheses, results, failures, costs and next decisions; the learner-facing instructions live in [README](README.md) and [SHOWCASE](SHOWCASE.md).

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

Full artifacts and commands: [TEST_RESULTS.md](TEST_RESULTS.md). Successful timed calls including the superseded Gemma run and RLVR below total approximately **$0.119**. This is a requested-compute estimate, not an invoice.

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
- **Conclusion:** working verifiable-reward learning signal, no demonstrated generalization improvement. Do not advertise “RL made the model smarter.” See [RLVR.md](RLVR.md) and [raw result](runs/rlvr-1788768609860683095/rl_result.json).

## September 7: replacing plumbing demos with persona fine-tunes

### Design

Hypothesis: supervised training on ordinary questions paired with stylistic answers can make that style appear without repeating a system prompt. Compare **neutral base**, **base with explicit style prompt**, and **fine-tuned model with only the ordinary question**. Prompting is a real competing solution, not a deliberately weak baseline.

Eight fixed evaluation questions cover DNS, Git force-push recovery, onion tears, missing a train, photosynthesis with an explicit prose request, rubber-duck debugging, Moon phases and a robot-vacuum apology. Five are Polish, three English. They are absent from training and from synthetic training-data generation. All variants use greedy decoding and 192 new tokens; long baseline answers can be truncated. Inspect content, language and style separately. Four lines are not proof of poetry or correctness.

### Experiment S1: small-model synthetic poetry data — rejected

- Teacher: Gemma 4 E2B Instruct, pinned revision in the manifest. Style instruction includes a six-line public-domain *Pan Tadeusz* excerpt and asks for original AABB quatrains.
- 128 question–answer pairs generated; **128/128 passed the four-line filter**. Generation 167.9 s, timed remote 196.6 s, estimated compute **$0.0558**.
- Manual reading found broken Polish, forced/nonexistent rhymes, language switching and factual errors. For 404, it wrote “forty-four” and described the server as silent. This dataset was **not used for training**.
- Insight: a cheap teacher can produce expensive-to-repair data. Format metrics can hide unusable content. Do not optimize a poetic RLVR example using line count as the sole reward.
- Artifacts: [accepted-by-surface-filter answers](runs/style-data-poetry-1788771080241515907/accepted.json), [execution](runs/style-data-poetry-1788771080241515907/execution.json), [annotated data review](DATA_REVIEW.md).

### Intervention: authored reusable data

- Added `curated_data.py`: 32 topic pairs × Polish/English = **64 examples per persona**. Both personas answer the same training questions.
- Original answers authored by the coding assistant, openly inspectable; not outputs from the rejected small-model teacher, not expert literary review. Poetry is short verse with some imperfect rhymes; no claim of Mickiewicz's meter. Comic dialogue uses original metaphors and practical advice.
- `uv run curated_data.py` builds versioned JSONL plus SHA-256 manifests. Training copies the exact dataset into each run. Hash, distinct IDs, both languages and held-out isolation checked locally.
- Files: [poetry-v1](datasets/poetry-v1/train.jsonl), [wit-v1](datasets/wit-v1/train.jsonl), [data provenance](datasets/README.md).

### Experiment S2: Gemma poetry on authored data — reject as showcase

Command:

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage train --style poetry --data-run poetry-v1 --epochs 12 --max-seconds 300
```

- One L4, BF16, LoRA rank 16 / alpha 32 / dropout 0.05, attention and MLP linear projections, learning rate 1e-4, effective batch four, answer-only loss.
- **192 updates, 283.1 s training (4.7 min)**, timed remote 392.4 s, peak allocated VRAM 11.53 GB, estimated requested compute **$0.1113**.
- Four-line rates: neutral 1/8, prompted 8/8, tuned 7/8. Adapter was nonzero and four fresh-base reload probes matched exactly.
- Training loss became nearly zero. Held-out outputs still had poor grammar and content. DNS was not explained; the rubber-duck answer wrongly recommended omitting setup and expected state. The base model also misread the Polish force-push question as physical exercise, and failed to explain onion tears correctly.
- **Conclusion:** learned output shape, not a useful poetic assistant. More steps are not the answer by themselves. Reject as the headline example and try a stronger multilingual base. Possible confounds: weak starting capability, only 64 examples, excessive repetition. These were not isolated in a controlled ablation.
- Artifacts: [result](runs/style-train-poetry-1788772024290826300/style_result.json), [all outputs](runs/style-train-poetry-1788772024290826300/finetuned.json), [offline comparison](REJECTED_GEMMA.html).

### Experiment S3: Qwen3.5-4B comic persona — working style change, mixed quality

Command:

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage train --style wit --data-run wit-v1 --model qwen3.5-4b --epochs 6 --max-seconds 300
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
uvx --from modal==1.5.0 modal run style_modal.py --stage train --style poetry --data-run poetry-v1 --model qwen3.5-4b --epochs 4 --max-seconds 600
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
- The complete [offline comparison](SHOWCASE.html) contains all eight prompts for both Qwen adapters under greedy and sampled decoding: 96 answers across the three variants. Language buttons filter the view; nothing is cherry-picked.

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

The user considers the visibly different outputs useful workshop material, while acknowledging the quality limitations. Saved the Moon, robot-vacuum and Polish DNS comparisons in [example_results.md](example_results.md), alongside data provenance and sample training targets. Full saved baseline responses are included, with the generation-length cap disclosed. This reframes the current runs as useful demonstrations of behavior change; it does not change the recorded content-quality observations.

## Full-book request: Pan Tadeusz and film screenplay search

The user requested an actual full-book training example and a search for the *Chłopaki nie płaczą* screenplay.

### Experiment B1: full Pan Tadeusz — complete full pass, reload passed

- Downloaded the TXT directly from Wolne Lektury. Retained the unmodified source, publisher credits and SHA-256 hashes. Training text contains all twelve books and the epilogue, 441,326 characters / 68,896 whitespace-separated words. Front title/ISBN metadata and publisher footer are excluded from training. Book headings and summaries remain.
- `prepare_pan_tadeusz.py` checks every book heading and the epilogue before writing. Checked source/processed hashes, final verse retention, metadata exclusion and refusal of missing-book/missing-epilogue inputs.
- `corpus_workshop.py` performs raw-text continued pretraining with LoRA, no chat-template wrapping, no synthetic answers. Default LFM2.5-2.6B, rank eight / alpha 16 / dropout .05, learning rate 1e-4, batch two. Each block has up to 256 target tokens with one-token boundary overlap; the final partial block is retained. A coverage check confirms every token after the initial token is supervised exactly once per full pass.
- One L4, one epoch, 600-second training cap, 1200-second function timeout. The result records actual full-book coverage; a time cap can otherwise stop a run before the complete corpus has been seen.
- Four before/after probes: two original verse openings as raw completions, plus two chat prompts. These distinguish literary continuation from instruction-following transfer. The full work is used for training, so there is no held-out perplexity claim; the base may already know this public-domain book.
- Command: `uvx --from modal==1.5.0 modal run corpus_modal.py --max-seconds 600`.
- **333 updates, 61.3 seconds training**; all **665/665 blocks**, **169,997/169,997 next-token targets** seen exactly once. `full_corpus_seen=true`, coverage 100%. Corpus token count 169,998. Peak allocated VRAM 7.79 GB. All four saved-adapter reload outputs matched; adapter weights nonzero.
- Timed remote execution **177.7 seconds**, estimated requested compute **$0.0504**. App completed and stopped. This is additional to the prior $0.4916 style batch; combined estimate about $0.5420, excluding startup/storage and the earlier smoke tests.
- Raw continuations shifted toward narrated scenes with line breaks and dialogue. They remain grammatically uneven and sometimes incoherent; no claim of matching Mickiewicz's verse. Both chat probes emit English planning text under the present template/token cap rather than a finished Polish answer. Raw corpus adaptation did not establish poetic chat behavior; this limitation is retained in the outputs.
- [Execution and exact coverage](runs/pan-tadeusz-1788776622044561619/execution.json), [before](runs/pan-tadeusz-1788776622044561619/before.json), [after](runs/pan-tadeusz-1788776622044561619/after.json), [reloaded](runs/pan-tadeusz-1788776622044561619/reloaded.json). Sources and runnable commands: [PAN_TADEUSZ.md](PAN_TADEUSZ.md).

### Screenplay search result

No verified publicly downloadable full screenplay found after searching the title in Polish/ASCII, script/text/PDF/transcript terms, library records and subtitle leads. Official film records credit Mikołaj Korzyński. A specific next lead is Script Fiesta's 2025 panel with the writer and director. A library hit is a DVD, educational PDFs are film descriptions, and Wikicytaty is a quote collection. These are not substitutes for the complete screenplay. No screenplay/subtitle corpus added; no external contact made. Detailed sources: [SCREENPLAY_SEARCH.md](SCREENPLAY_SEARCH.md).

## Bidirectional dialogue conversion

User requested the Wikiquote dialogue collection as user/assistant pairs in both directions. Added [dialogue_pairs.py](dialogue_pairs.py) for a supplied local dialogue text: each adjacent cross-speaker pair creates forward and reverse examples. Scene boundaries are preserved, repeated pairs deduplicated, consecutive same-speaker lines merged. Scenes sharing lines stay in the same split to prevent reversed-pair/quotation leakage.

The linked film dialogue was not bulk-copied or transformed; the copyright limitation was explained, with local user-supplied text offered as the supported input. No film dataset or new GPU run was produced. [Usage](DIALOGUE_PAIRS.md). Four new tests verify adjacency/both directions, scene boundaries, split isolation, merging/deduplication and malformed input rejection; all nine repository tests pass. Reverse-direction pairs are reconstruction examples and may not be natural replies. The existing trainer uses its general persona evaluation, not the converter's validation file automatically.

## User-supplied chlopaki.md: actual film-dialogue adaptation

The user supplied `datasets/chlopaki.md`. Work now uses that local content directly, superseding the earlier converter-only state. The source is a user-supplied dialogue transcript, not independently verified as an official screenplay. It has spelling errors, abbreviated character labels, stage directions and some unlabelled continuation lines.

### Dataset C1

- Source SHA-256: `54ccfa75fd8cacf0a9ba1a97438801a035f38f8069788aa026358a912c826e57`.
- `prepare_chlopaki.py` produces 71 scenes / 706 merged turns. Nine single-turn scenes are preserved separately. Scene headings/stage directions excluded; unlabelled speech continuation attaches to preceding speaker, recorded in an audit. Character abbreviations resolved locally where possible, source content otherwise retained.
- **1,270 unique training examples: 635 forward + 635 reverse.** Every pair has its reverse. All usable exchanges are in training; no quotation holdout. Six new ordinary Polish questions are saved for before/after evaluation. Their wording is disjoint from training prompts.
- No assistant-authored wit examples mixed in. Every resulting pair maps exactly to original source line numbers; all nonempty source lines accounted for as dialogue, heading or parsing audit.
- Dataset hash: `3f691a2b920c6efa3cc0e2c4b922bbb1658de325baf69777bfb15f7b2799edd6`. [Prepared data](datasets/chlopaki-bidirectional-v1/train.jsonl), [line provenance](datasets/chlopaki-bidirectional-v1/pair_source_lines.json), [instructions](CHLOPAKI.md).

### Training C1a — Qwen3.5-4B, failed OOM

- One L4; direct batches up to four examples / 2,048 padded tokens, rank-16 LoRA, one epoch, ten-minute cap.
- First optimizer update completed, then a longer batch exhausted GPU memory (about 21.49 GiB allocated). App `ap-REDACTED019` exited with error. No successful adapter result. Failed-attempt compute not yet measured in an execution record and excluded from successful-call cost sums.
- Fix: enable non-reentrant gradient checkpointing for direct batching. Preserve long dialogue rather than truncating it. This batching mode uses answer-token mean loss, unlike the old microbatch recipe's example mean.

### Training C1b — Qwen3.5-4B on supplied film dialogue, completed partial pass

- Same dataset/model and budget, with gradient checkpointing. All 1,270 examples requested for one pass. Coverage will be recorded explicitly before claiming all pairs were seen.
- Evaluate base without style instruction, prompted base, and fine-tuned adapter without style instruction on six Polish questions. Label model and exact dataset on every reported example, per user instruction.
- Command: `uvx --from modal==1.5.0 modal run style_modal.py --stage train --data-run chlopaki-bidirectional-v1 --model qwen3.5-4b --epochs 1 --max-seconds 600 --batch-tokens 2048`.

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

Saved selected actual film results in [example_results.md](example_results.md), all six Q&A comparisons in [chlopaki_results.md](chlopaki_results.md), and all 54 base/prompted/after outputs across three conditions in [CHLOPAKI_RESULTS.html](CHLOPAKI_RESULTS.html). Every comparison labels the exact model and training dataset. Full-strength sampled decoding is the main creative demonstration; the other conditions explain how decoding and adapter strength change the result.

Final local verification: all nine unit tests passed; modified Python sources parsed successfully; saved coverage contains exactly indices 0–1269; report contains 18 question cards / 54 answers; result-document links resolve.

### Evaluation C1f — non-question repetition probe

User asked whether the adapter always falls back on “Zamieniam się w…” after non-question messages. Prepared eight statements/greetings/dialogue fragments and four questions, two fixed seeds (42, 123), full-strength Qwen3.5-4B adapter trained only on supplied `chlopaki.md`. No style instruction, no additional training. Same sampling settings as C1d but a 96-new-token cap; batch size four. This is a small diagnostic sample, not a prevalence estimate for all conversations.

Source contains “Zamieniam się w słuch!” once (line 718); the phrase appears in four generated pairs, including two answer targets. First probe launch failed during container import because the separate Modal wrapper imported an unmounted local module. Stopped the app, made the image definition self-contained, and relaunched. Failed startup compute is not measured in the successful-call estimate.

Reproduce: `uvx --from modal==1.5.0 modal run dialogue_probe_modal.py`. Local GPU: `uv run dialogue_probe.py --adapter-dir PATH_TO_SAVED_RUN --output runs/my-dialogue-probe`.

C1f complete: **1/16 non-question responses**, **1/8 question responses** contained/started with the phrase. No universal fallback. Limited convenience sample; no claim that question syntax causes the difference. Other outputs range from relevant dialogue and comic replies to brief non-answers and incoherent passages. Saved every output in [chlopaki_results.md](chlopaki_results.md) and [raw record](runs/dialogue-probe-1788793342343057211/probe.json). Sampling depends on batch order/RNG consumption, so identical seeds across different prompt sets do not imply identical answers.

Timed remote **59.76 s**, estimated successful-call compute **$0.01696**. App completed and stopped. Both new script sources parse successfully; saved counts recomputed from all 24 answers and verified.

### Evaluation B2 — ordinary Polish questions and statements after full-book training

User requested the equivalent chat probe for models trained on full *Pan Tadeusz*. There is currently one completed full-book adapter: **LiquidAI/LFM2.5-2.6B**, revision `654f9463ce32b05d0429d76fe1f580b27d4c1ac0`, trained on all twelve books and epilogue from Wolne Lektury, raw-text continued pretraining with LoRA. The earlier Qwen poetry adapter used 64 authored Q&A examples and is not a full-book model.

Prepared four ordinary Polish questions and four statements, all sent through the chat template with no system/style instruction. Compare original checkpoint and full-strength saved adapter, same seed 42, temperature .7, top-p .8, top-k 20, repetition penalty 1.1, batches of four, 192-new-token cap. These test ordinary replies rather than literary continuations. No additional training.

Runnable scripts: `uvx --from modal==1.5.0 modal run corpus_probe_modal.py`; local GPU: `uv run corpus_probe.py --adapter-dir PATH_TO_SAVED_RUN --output runs/my-corpus-probe`. New script syntax verified.

B2 completed: [all 16 raw outputs](runs/corpus-probe-1788793991034451951/probe.json), [readable comparison](pan_tadeusz_results.md). **8/8 after outputs begin with English planning text; 5/8 reach a Polish final-reply segment before the cap, 3/8 do not.** The visible replies are mostly prose; this does not establish always-poetic chat. The untuned base also produces planning text (2/8 reach a final-reply segment), so do not attribute that behavior solely to fine-tuning. Readable report extracts only text after the literal `</think>` delimiter and explicitly labels absent replies; raw outputs remain unchanged. Longer decoding or a model-specific template intervention was not tested, to avoid an unplanned sweep.

Timed remote **71.64 s**, estimated requested compute **$0.02033**, excluding startup/storage. App completed/stopped. No new training. Both new sources parse successfully; all eight prompt alignments and final-reply counts verified.

### Larger-context follow-up — implementation prepared, no new GPU run

User suggested a larger context window for full-book adaptation. The original 257-token input / 256-target blocks were deliberately short training chunks, not the architecture's capacity. Liquid AI's current official model card describes 128K context: https://huggingface.co/LiquidAI/LFM2.5-2.6B . That inference capacity is not a promise that 128K training fits an L4.

Added `--target-tokens` (256/1024/2048/4096), `--batch-size` (1/2), and `--line-aligned` to local and Modal full-book trainers. Prefer 2048 targets, batch one as the next economical test. Longer sequences enable gradient checkpointing. Optional tokenizer-offset newline boundaries retain every next-token target exactly once with one-token overlap; unusually long lines fall back to fixed cuts and are counted. Default behavior preserves the original fixed-block recipe.

Validation: three new CPU tests check exact coverage with line boundaries, oversized-line fallback and compatibility with the original chunking; all 12 repository tests pass. Modified sources parse. GPU fit/runtime/quality untested; no additional cloud spend. Larger chunks reduce updates per book pass as well as increasing context, which must be disclosed when comparing outcomes. Longer output budgets and question-to-verse supervision remain separate interventions. [Commands](PAN_TADEUSZ.md#larger-training-chunks--tested-at-2048-targets).

### Training B3 — 2,048-target line-aligned full-book run, launched

User explicitly requested running and testing the larger-context recipe. Started a fresh **LiquidAI/LFM2.5-2.6B** from the same pinned checkpoint, full Wolne Lektury *Pan Tadeusz*, one pass, rank-eight LoRA, LR 1e-4, target limit 2,048 (up to 2,049 input tokens), batch one, line-aligned boundaries, gradient checkpointing. Ten-minute training cap; one L4. No continuation from the old 256-target adapter.

Command: `uvx --from modal==1.5.0 modal run corpus_modal.py --target-tokens 2048 --batch-size 1 --line-aligned --max-seconds 600`. App `ap-REDACTED023`.

Evaluation plan: preserve original four greedy completion/chat/reload probes, then repeat B2's eight ordinary Polish messages using exactly its sampling recipe. Add a separate, bounded 1,024-output-token diagnostic on the first two questions, before and after, because the old 192-token cap often stopped in planning text. Longer diagnostic uses batch two and is labeled separately; it is not a matched seed/batch comparison with the eight-message test. This inference-only extension avoids interpreting truncated planning as the final writing quality. No epoch/model sweep.

B3 training complete: [execution](runs/pan-tadeusz-1788794554392255032/execution.json). **84/84 chunks, 169,997/169,997 next-token targets, 84 updates, 73.02 s training**, zero forced line splits. Peak allocated VRAM **8.83 GB**. Nonzero adapter and all four fresh-base reload outputs match. Timed remote 176.98 s, estimated requested compute **$0.05021**. Original 256-target run used 333 updates / 61.28 s / 7.79 GB, so the new recipe changes update count and batching as well as context.

Raw continuations remain line-broken narrative with uneven grammar and meter; short chat probes still mostly contain planning text. Started the eight-message sampled chat comparison plus two separate 1,024-output-token diagnostic questions. No further training requested for evaluation.

B3 evaluation complete: [all 20 unmodified generations](runs/corpus-probe-1788794812419147366/probe.json), [full comparison](pan_tadeusz_2048_results.md). Untuned outputs on the eight-message 192-token test match B2 exactly. New adapter reaches a final-reply segment in **2/8** cases, versus **5/8** for the old adapter; visible replies are ordinary prose. This is a token-budget diagnostic, not a model-quality ranking.

The separate 1,024-token test reaches a substantial prose answer to the life-direction question for both untuned and new-adapter models; neither reaches a final delimiter on the computer question. Thus increasing output allowance helps one case but does not yield poetic chat. No output-budget sweep beyond this diagnostic. Raw continuation counterexample: “Gdy wstał z łóżka i wybrał się do pracy.” = 11 syllables by manual word-level count (1+1+0+2+1+2+1+1+2), not 13.

Evaluation timed remote **146.43 s**, estimated compute **$0.04155**. Combined B3 training and tests **$0.09176**, excluding startup/storage. Both apps completed/stopped. Saved selected outputs in `example_results.md` and all comparisons in `pan_tadeusz_2048_results.md`. All 12 unit tests pass; checked exact coverage, zero forced splits, all reload outputs, baseline reproducibility and output counts.

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

Validation passed: 500 unique prompts and answers; exact source text and source-line positions; 4–12 lines each; no overlapping source positions; all twelve books; 450/50 IDs disjoint; no normalized verse-line overlap >=20 characters across splits; manifest counts and data hash agree. Rebuild with `uv run --no-project prepare_pan_tadeusz_qa.py build`. [Guide and three examples](PAN_TADEUSZ_QA.md), [all 500 reviewed pairs](datasets/pan-tadeusz-qa-v1/REVIEW.md).

No training launched for this dataset; no new before/after results. GPU and paid teacher API spending for this preparation: $0 (excluding the Codex session itself). Next proposed baseline: fresh Qwen3.5-4B, assistant-only SFT; evaluate 4–12-line compliance rather than the previous exactly-four-line metric, plus comic fit and syllable counts separately.

Training JSONL SHA-256: `52c3cb2b69adc29d645ce45afd1024baae6c7ac90ebbe2306ddb35cab7818361`.

### B4 training — Qwen3.5-4B on the 450 Pan Tadeusz Q&A pairs, launched

User explicitly requested training the prepared dataset. Started fresh Qwen3.5-4B (pinned models.json revision), rank-16 LoRA, alpha 32, LR 1e-4, assistant-only loss, two epochs requested, 600-second training cap, 2,048 padded tokens per batch (maximum four examples), gradient checkpointing. One Modal L4, no retries, 1,200-second function timeout (~$0.34 requested compute ceiling plus startup/storage). App `ap-REDACTED005`.

Command: `uvx --from modal==1.5.0 modal run style_modal.py --stage train --data-run pan-tadeusz-qa-v1 --model qwen3.5-4b --epochs 2 --max-seconds 600 --batch-tokens 2048`.

Adapted trainer/evaluation to the dataset's 4–12-line range and raised its generation allowance to 384 tokens, including the exact saved-adapter reload check. Prompt-only comparison now requests the same humorous verse behavior; base and adapter comparisons receive ordinary user text with no style instruction. Previous datasets retain their four-line metric and 192-token budget. Line count is a shape metric, not evidence of meter or comic quality. No silent training truncation. Will report actual coverage if the time cap interrupts two epochs.

Infrastructure interruption: first worker printed `Runner terminated (SIGTERM), exit code: 143` after reporting update 11 (~24.70 seconds training), then Modal automatically began a new worker despite application-level retries=0. No checkpoint had been written. Cause not established by logs; do not label this an OOM. Interrupted-worker time is additional and is not included in a later successful worker's `execution.json` compute estimate. Monitoring the automatic restart; no manual duplicate training job launched.

B4 training completed: `runs/style-train-poetry-1788797625746162366`. Qwen/Qwen3.5-4B revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`, fresh rank-16 LoRA on training hash `52c3cb2b69adc29d645ce45afd1024baae6c7ac90ebbe2306ddb35cab7818361`. 225 updates, 900 example presentations (two complete passes over 450 unique pairs), 370.2201 seconds training, 12.8565 GB peak allocated GPU memory. Nonzero adapter; all four fresh-base reload outputs match exactly. Successful worker remote time 565.3567 seconds, estimated requested compute $0.160403. This excludes the earlier interrupted worker and startup/storage; it is not the total invoice.

Greedy held-out results: 11/12 answers have 4–12 nonempty lines; 0/12 are single-line replies. Several answers repeat phrases; pt-0060 loops for 27 lines. Baseline also passes the naive line-count check on 10/12 replies because prose paragraphs and bullet lists count as lines, so do NOT present the metric as a poetry-quality classifier. The learned default changes visibly toward historical dialogue and line-broken verse, but strict meter and clean grammar are not achieved. Example pt-0010: boss visiting departments becomes the Count inspecting his army. Other outputs include comic absurdities (Gerwazy declaring someone is no longer his turtle) and malformed words.

Launched one inference-only sampled comparison on the same 12 held-out prompts, base/prompted/adapter, seed 42, temperature .7, top-p .8, top-k 20, repetition penalty 1.1, 384 output-token cap. App `ap-REDACTED014`. No retraining. All 12 repository tests pass and the new dataset-specific metric checks pass. [Full greedy outputs](pan_tadeusz_qa_results.md).

B4 sampled evaluation complete: `runs/style-sample-poetry-1788798230980944941`. 12/12 adapter replies have 4–12 nonempty lines; zero one-line answers in this small test. Answers containing an exactly repeated line (case/punctuation normalized): greedy 3/12, sampled 0/12. This does not measure broader semantic repetition. The 27-line greedy loop disappears with sampling; grammar, invented malformed words, relevance and meter remain uneven. Comic connections include the late dinner guest falling upside-down and being rescued by Tadeusz (`pt-0020`), forceful mediation becoming a fight (`pt-0065`), and overtime bargaining for three days off (`pt-0112`). These are actual generated outputs from the Q&A adapter, not quotes selected from the book. No new training in this evaluation.

Sample worker: 224.8267 seconds, estimated requested compute $0.063788. Completed training/evaluation workers combined: $0.224191, **excluding the unmeasured interrupted worker, startup and storage**. Both Modal apps completed/stopped. Full raw base/prompted/adapter answers in run directories; all 72 generations in `pan_tadeusz_qa_results.md`; three selected before/after comparisons appended to `example_results.md`. Saved adapter resides in Modal volume `model-training-workshop` at `/runs/style-train-poetry-1788797625746162366/adapter`. Local run files contain metadata/outputs/executed source; adapter binaries remain on the persistent volume.

Conclusion: explicit question-to-verse SFT teaches the desired default multi-line historical voice much more directly than the previous full-book-only LFM trials, although that is not a controlled same-model comparison. This is a viable workshop starting point with obvious room for grammar/meter improvement. The 12-prompt sample is not evidence of an always-poetic guarantee. No extra epoch or model sweep launched.

### R2 — visible RLVR workshop comparison (pre-registered plan)

User requested several substantially different RLVR ideas, tested for plainly visible improvement. Earlier 48-rollout arithmetic example stayed at 4/8 and is not adequate as a success showcase. Implemented three independent tasks in `rlvr_tasks.py`: six-word English microfiction with two required words; Countdown expressions using three given numbers exactly once; a robot navigating a 4x4 maze with two walls. Strict success is separate from continuous/partial reward. Microfiction checker verifies lexical constraints, not literary merit; manual output review is required. Math uses a bounded AST/Fraction interpreter, never eval. Maze paths are simulated; collisions invalidate success even if the path previously touched the goal.

Plan: screen 8 training prompts × 4 on-policy samples per task, then train promising tasks for up to 300 seconds each on Qwen/Qwen3-0.6B, pinned revision `c1899de289a04d12100db370d81485cdf75e47ca`. One L4 at a time, approximate initial investigation target below $1 requested compute excluding startup/storage. Each candidate uses a fresh rank-16 LoRA, alpha 32, learning rate 2e-4, 2 prompts × 4 samples per update, up to 160 updates. This is on-policy REINFORCE with a leave-one-out baseline, no KL penalty or PPO clipping; short runs, not a production trainer. Temperature 1, no top-k/top-p filtering, dropout off, one update per fresh rollout batch, generated tokens through first EOS only, sequence-summed log probability. No SFT warm start, teacher answers, reward-generated targets, or best-of-N display selection.

Deterministic data generator seed 20260907: 256 train / 24 development / 32 final-test prompts per task; no identical puzzles/anchor pairs/maps across splits. Half of the microfiction test uses entirely new anchor words. Both greedy first attempts and 24 fixed-seed development samples evaluated before and after. Results, all rollouts, data, source snapshots, save/reload checks and costs saved per run. Candidate selection should use development results; inspect the final test after the initial recipes are completed and label any later experiment as a follow-up. Six verifier/data/advantage tests passed before launch, including malicious/invalid arithmetic, maze collisions and duplicate/missing story words.

Screen command: `uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task all --stage screen`. App `ap-REDACTED012`. No quality claim yet. Primary method reference: https://huggingface.co/docs/trl/rloo_trainer ; model/non-thinking template: https://huggingface.co/Qwen/Qwen3-0.6B .

R2 screen completed: six-word stories `rlvr-screen-six_words-1788799273736758142` 0/32 strict successes, mean shaped reward .3510, all EOS-terminated, estimated $0.012022; Countdown `rlvr-screen-countdown-1788799321013743971` 0/32, mean .025, 18/32 terminated, $0.003005; maze `rlvr-screen-maze-1788799335005344555` 0/32, mean .05625, 26/32 terminated, $0.001629. Screen total ~$0.01666. Despite zero strict successes, partial reward varies; test whether shaping bootstraps useful behavior rather than discarding candidates solely for this. Stories often return 2–4 anchor-containing words; math commonly adds equals signs/explanations; maze copies the literal example UURD. Removed that example from maze instructions before training (this changes the dataset hash); no reference path is now shown in its prompt. Original screen source/data preserved.

Launched all three fresh adapters sequentially, each capped at 300 training seconds / 160 optimizer batches. Command `uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task all --stage train --max-seconds 300 --steps 160`; app `ap-REDACTED007`. One L4, each function 1100-second hard timeout; expected compute below original ~$1 investigation target. No test results inspected to adjust these recipes.

R2 stories initial trial complete: `rlvr-train-six_words-1788799386079459022`, 160 batches / 69 nonzero updates, 230.85 s training, 2.049 GB peak allocated VRAM, adapter changed and reload matched. Development strict success remains 0/24 despite mean reward rising .3653→.4667. During training 54/1280 sampled answers passed, but by the end outputs collapsed to five-word templates such as `Moon who is a sailor.` and `Clown who is an ocean.`. This is a failed success showcase and a useful partial-reward/exploration-collapse example. Terminal evaluation also prints test aggregates automatically; no test-specific examples or failure patterns used to change the recipe.

Follow-up plan, motivated by development outputs/training rollouts: add optional RLOO reference-policy regularization (detached Monte Carlo sequence log(pi/pi_reference) subtracted from scalar rewards), lower learning rate, and select the best checkpoint on all 24 development prompts by strict successes, breaking ties with mean task reward. Evaluation saves/restores rollout RNG. Keep the initial beta=0 recipe runnable and preserve original executed code. Final test must not choose checkpoints. Checkpoints are compared to the unmodified starting adapter as well; if none improves development, return the original policy honestly. No additional GPU launched yet; the original arithmetic and maze trials continue sequentially.

R2 Countdown initial trial complete: `rlvr-train-countdown-1788799671247002331`, 160 batches / only 14 updates, 190.14 s training, 2.166 GB VRAM, reload matches. Development 0/24→3/24; mean reward .0083→.5706. Actual development outputs reveal the policy ignores the target and always emits the numbers in input order as `a + b - c`. Thus the higher partial reward is mostly format/number-use compliance, not puzzle solving. Rejected as the main demo. Completed screens plus these two training runs total ~$0.1606 requested compute, excluding startup/storage.

The initial recipe's large learning rate without reference regularization produced fast loss of output diversity on multiple tasks. Next bounded comparison will use the more recent cached Qwen3.5-0.8B, LR 5e-5, beta .01 and development checkpoint checks every 20 batches, up to 300 training seconds. This changes both model and optimization recipe, so it cannot isolate which change causes any improvement. Goal is to find a practical workshop starting point, not a controlled optimizer benchmark. Start with stories and inspect before spending further; keep all rejected results.

R2 maze initial trial complete: `rlvr-train-maze-1788799930241701161`, 160 batches / 4 updates, 91.15 s training, reload matches. Development 0/24→0/24 and test 0/32→0/32: reject as a navigation success demo. All initial task comparisons are preserved in `RLVR_INITIAL_RESULTS.md` and `RLVR_INITIAL_RESULTS.html`. HTML includes every first attempt and simulated maze paths; generated JavaScript syntax checked with Node. All 16 repository tests pass.

R3 stories launched: `uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task six_words --model qwen3.5-0.8b --max-seconds 300 --steps 160 --lr 0.00005 --beta 0.01 --dev-interval 20`. App `ap-REDACTED003`. Qwen/Qwen3.5-0.8B revision `2fc06364715b967f1860aea9cf38778875588b17`. Same story prompts/reward/splits as R2, fresh adapter, vision modules excluded from LoRA. Model card confirms the small checkpoint is intended for prototyping/task-specific fine-tuning: https://huggingface.co/Qwen/Qwen3.5-0.8B . Previous three-task app completed/stopped before launching this GPU.

R3 complete: `rlvr-train-six_words-1788800080367606015`, 56 batches/updates, 301.37 s training including intermediate development checks, 3.487 GB peak allocation. Development checkpoints: initial 2/24, batch 20 5/24, batch 40 8/24, final batch 56 6/24. Selected **batch 40** using development only. Selected adapter has seen 80 unique prompts; the whole exploration run presented 112. Held-out test 0/32→9/32; sampled development 0/24→8/24. All eight fresh-base reload answers match. Remote estimate $0.095617; total R2+R3 completed-worker compute $0.290467.

Manual review: the regularized 0.8B model retains more variety but prose becomes telegraphic (`mouse eats vampire in the forest`, `chef uses robot to cook dinner`). Exact counts improve, yet this is not a stunning writing example. All 32 test outputs were inspected only after checkpoint selection. No specific test example is used to alter prompts/reward.

R4 bounded follow-up launched on **fresh Qwen/Qwen3.5-4B**, revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`, same six-word dataset, LR 5e-5, beta .01, development checkpoint selection every 20 batches. No Pan Tadeusz or film adapter is loaded. Increase training allowance to 600 seconds; one L4, host memory increased to 16 GiB, overall function timeout 1100 seconds (~$0.31 requested compute ceiling excluding startup/storage). Command `uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task six_words --model qwen3.5-4b --max-seconds 600 --steps 160 --lr 0.00005 --beta 0.01 --dev-interval 20`. App `ap-REDACTED020`. Aim: preserve readable microfiction while improving constraints; R3's 9/32 is a real but insufficiently strong workshop result. Previous app stopped before launch.

R4 intermediate development checkpoints: original Qwen3.5-4B 0/24; batch 20 18/24 at roughly 3.5 minutes; batch 40 23/24 at roughly 6.6 minutes. These are development counts, not the final test, and literary quality has not yet been inspected. Retaining best state by the declared development rule. R3's saved reference-regularized advantages were independently recomputed from task rewards and sequence log ratios and matched throughout; all saved R2/R3 evaluation rewards were independently rerun through the current checkers and matched. The reward/checkpoint mechanism, not only the reported summaries, is inspectable.

R4 completed: **`rlvr-train-six_words-1788800507182250757`**. Qwen/Qwen3.5-4B, fresh task-specific RLVR adapter; no workshop SFT and no Pan Tadeusz/film data. Training explored 62 batches / 496 sampled answers, 124 distinct training prompts, 603.61 seconds including intermediate development checks. The 600-second cap is checked after a batch and overshot by 3.61 seconds. **Selected batch 60** by development success: 0/24 original → 18/24 at batch20 → 23/24 at batch40 → 24/24 at batch60. Final batch62 tied, so retained the earlier best. The SAVED adapter therefore reflects **120 distinct prompts / 480 self-sampled completions / 60 updates**, not all 256 pool prompts or all 62 exploration updates.

Held-out greedy **1/32 → 32/32**, including **16/16 entirely new anchor-word pairs drawn from words absent from training**. Every after-test answer reaches EOS. Sampled development (12 prompts × 2 temperature-1 samples): 3/24→21/24. This is one training seed and a small, task-specific test, not universal reliability. Adapter changed and all eight fresh-base reload outputs match. Peak GPU allocation **13.992 GB**. Completed worker estimate **$0.193501**. Cumulative R2–R4 completed-worker compute **$0.483968**, excluding startup/storage; no interrupted GPU workers in this investigation.

Manual review of all 32 held-out answers: clear six-word compliance and some amusing micro-scenes, but repeated grammatical templates, sparse articles and occasional awkward meanings remain. Do not call the checker a literary-quality score. Examples (all original Qwen3.5-4B → same checkpoint + this six-word RLVR adapter): `The mermaid kissed the glacier.` → `Glacier melted to reveal a mermaid.`; `Astronaut blew birthday candles.` → `Astronaut blew birthday candles in space.`; `The mouse bit the vampire.` → `Mouse fed vampire with tiny cheese.`. These are generated outputs, not provided training targets.

R4 app completed/stopped. One bounded Countdown follow-up on the now-working 4B regularized recipe is authorized within the user's request to test distinct ideas: same LR/beta/dev selection, 300-second training cap, fresh adapter again. App `ap-REDACTED021`; command `uvx --from modal==1.5.0 modal run rlvr_showcase_modal.py --task countdown --model qwen3.5-4b --max-seconds 300 --steps 160 --lr 0.00005 --beta 0.01 --dev-interval 20`. Purpose: determine whether arithmetic can be a second successful option rather than inferring its potential solely from the failed 0.6B recipe. No further model/learning-rate sweep planned.

R5 Countdown complete: **`rlvr-train-countdown-1788801278948986334`**. Fresh Qwen3.5-4B with only Countdown RLVR, same pinned revision as R4; it does not reuse the story adapter. Explored 36 batches / 29 updates, 72 unique prompts, 305.64 s including intermediate development evaluation, 14.169 GB peak allocation. Selected batch20 by development (7/24 initial → 14/24 at20, final13/24); saved adapter has **40 unique prompts, 160 self-sampled answers, 20 updates**. Test **7/32→11/32**, six corrections and two regressions. Sampled dev4/24→13/24. All eight fresh-base reload outputs match. Completed compute estimate **$0.108979**.

Actual generated test correction: numbers [10,5,15], target85; original Qwen3.5-4B `(15 * 10) + 5` (=155) → same model + Countdown RLVR `15*5+10` (=85). This is useful evidence of some solving improvement but 11/32 is insufficient for the main workshop success demo. No further runs: keep six-word microfiction as the clear choice, arithmetic as a modest-gain comparison, and the initial maze trial as a negative/reward-debugging exercise. Do not infer that maze RLVR cannot work in general; only this 0.6B recipe was tested.

**Final R2–R5 accounting:** three inference screens + six independent training runs, all completed and apps stopped. Requested completed-worker compute **$0.5929468907**, excluding startup/storage, with no failed/interrupted GPU workers in this investigation. R4 winning run alone $0.193501. Preserved all rejected runs. No teacher/LLM-judge API charges.

Published locally (no external deployment or git push): `RLVR_SHOWCASE.md` with measured recommendation and exact commands; `RLVR_RESULTS.md` / `RLVR_RESULTS.html` with all six runs (960 unedited before/after generations including sampled development); `RLVR_INITIAL_RESULTS.*` with the first failed comparison; `RLVR_REWARD_LESSON.md` with actual intermediate samples and their advantages. Appended three model-labelled R4 before/after examples to `example_results.md`; README and old RLVR guide link the new work. Trainer/wrapper defaults now match the explicitly tested R4 command: Qwen3.5-4B, 600 seconds, max160 batches, LR5e-5, beta.01, dev interval20. The original failed settings remain available with explicit arguments. UV script lockfile is pinned and verified.

Final verification: 16 repository tests passed; R4 data hash, selected training coverage (120 prompts/480 rollouts), unseen-word split, all saved evaluation rewards, regularized advantages and reload equality independently rechecked (`local_verification.json`). Report JavaScript syntax and task/split/filter rendering checked with Node and a DOM stub; this is not a browser-layout screenshot test. Model prose manually reviewed, with formulaic wording and occasional awkward grammar explicitly documented. Greedy32/32 does not imply every sampled answer passes (sampled development21/24), nor that all future prompts will pass.
