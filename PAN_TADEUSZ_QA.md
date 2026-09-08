# Pan Tadeusz answers to everyday Polish prompts

**500 pairs: 450 training, 50 validation. Qwen3.5-4B has now been fine-tuned on the 450 training pairs.**

[Actual before/after model outputs](pan_tadeusz_qa_results.md). The examples below remain dataset targets, not generations. The measured training run completed two passes in 370 seconds; its saved adapter passed the reload check.

The joke is deliberate: modern salary negotiations can end in a duel; a failed presentation sends the team home like embarrassed hunting dogs. Prompts are individually authored by the Codex assistant in this session, after reading each passage. Replies are original Adam Mickiewicz passages, **not model-generated answers**. The set mixes comic anachronisms with ordinary questions about relationships, food, homesickness and nature.

- [Read all 500 pairs](datasets/pan-tadeusz-qa-v1/REVIEW.md).
- [All pairs, JSONL](datasets/pan-tadeusz-qa-v1/examples.jsonl), [training](datasets/pan-tadeusz-qa-v1/train.jsonl), [validation](datasets/pan-tadeusz-qa-v1/validation.jsonl).
- [Selection and provenance](datasets/pan-tadeusz-qa-v1/selection.json), [dataset manifest](datasets/pan-tadeusz-qa-v1/dataset.json).

Each input is one ordinary Polish question or statement, without instructions to write poetry. Each answer contains 4–12 original verse lines. All twelve books are represented, with one selected passage per paragraph. The eleven-syllable epilogue, book titles and summaries are excluded. Original spelling and typographic markers are retained; physical source lines are not a guarantee of exactly thirteen syllables on every line.

The split keeps source paragraphs disjoint and groups passages sharing normalized verse lines of at least 20 characters. Related themes still occur in both splits. This validation set was **not** held out from earlier full-book adapters, so start a fresh base adapter for a useful Q&A experiment.

## Training-data examples

The following are authored prompts paired with verbatim book passages. There is no fine-tuned model behind these examples.

### pt-0164

**User:** Nie możemy się dogadać w sprawie podwyżki. Jak zwykle kończą się takie negocjacje?

**Assistant training target — Adam Mickiewicz, Pan Tadeusz:**

> Tu już krzyknęli: »Dosyć! Trzeba raz rzecz skończyć,  
> Bóg nas czy diabeł złączył, trzeba się rozłączyć;  
> Dwóch nas jak dwóch słońc pono zanadto na świecie!«  
> A więc do szerpentynek i stają na mecie.

### pt-0166

**User:** Jak wracamy z prezentacji, na której nic nie zadziałało?

**Assistant training target — Adam Mickiewicz, Pan Tadeusz:**

> Biedne psy, ogłupiałe, biegały pod gajem,  
> Zdawały się naradzać, oskarżać nawzajem.  
> Wreszcie wracają, z wolna skacząc przez zagony,  
> Spuściły uszy, tulą do brzucha ogony  
> I przybiegłszy, ze wstydu nie śmieją wznieść oczu,  
> I zamiast iść do panów, stały na uboczu.

### pt-0403

**User:** Jak to się dzieje, że idę prosić o podwyżkę, a wychodzę po miłej rozmowie o pogodzie?

**Assistant training target — Adam Mickiewicz, Pan Tadeusz:**

> Ileż to razy chciałem serce me otworzyć,  
> I już się nawet przed nim do próśb upokorzyć,  
> Lecz spojrzawszy mu w oczy, spotkawszy wejrzenia  
> Zimne jak lód, wstyd mi było mojego wzruszenia;  
> Śpieszyłem znowu jak najzimniej dyskurować  
> O sprawach, o sejmikach, a nawet żartować!!

## Rebuild and edit

```bash
uv run --no-project prepare_pan_tadeusz_qa.py build
```

The build uses saved passages and prompt text; it makes no API calls. Edit `datasets/pan-tadeusz-qa-v1/everyday_overrides.txt` to revise prompts (`0164|Prompt text`). The builder overlays these revisions on `literal_prompts.json`, exports `prompts.json`, validates the source and pairs, and regenerates the split, manifest and review. The 458 overrides replace the initial literal drafts; the remaining 42 prompts already fit ordinary situations. `batch-*.txt` and `prompts-*.txt` are authoring drafts, not training inputs.

Training should use assistant-only loss and include the complete answer plus end-of-turn token. The fresh Qwen3.5-4B adapter was trained with two passes, rank-16 LoRA and a 600-second training cap; the measured run took 370 seconds. Historical dialogue and multi-line output appear, while repetition, grammar and meter still need improvement. Evaluate 4–12 nonempty lines, relevance/comic effect and meter separately: the older four-line-only poetry score does not fit this dataset. No paid teacher API or GPU calls were used to prepare this dataset.

## Reproduce the measured training run

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage train --data-run pan-tadeusz-qa-v1 --model qwen3.5-4b --epochs 2 --max-seconds 600 --batch-tokens 2048
```

Saved adapter: Modal volume `model-training-workshop`, directory `/runs/style-train-poetry-1788797625746162366/adapter`. Local execution records and raw answers: `runs/style-train-poetry-1788797625746162366/`.

Sampled evaluation of the saved adapter: 12/12 held-out replies have 4–12 lines, with no one-line answers. This small test does not establish an always guarantee; grammar and meter remain uneven. Estimated compute for completed training/evaluation workers: $0.22419, excluding a separately interrupted worker and startup/storage.

```bash
uvx --from modal==1.5.0 modal run style_modal.py --stage sample --data-run style-train-poetry-1788797625746162366
uv run --no-project pan_tadeusz_qa_report.py runs/style-train-poetry-1788797625746162366 --sample-run runs/style-sample-poetry-1788798230980944941
```
