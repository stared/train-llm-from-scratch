# Persona fine-tuning rehearsals — 7 September 2026

These experiments replace the seconds-long infrastructure checks as the proposed creative exercise. Detailed hypotheses, decisions and the running experiment log are maintained in [LAB_NOTEBOOK.md](../LAB_NOTEBOOK.md). All training uses one Modal L4, BF16 LoRA (rank 16, alpha 32, dropout 0.05), learning rate 0.0001, effective batch size four, and completion-only loss. The 64-example datasets contain 32 Polish and 32 English answers. Evaluation uses eight fixed, unseen questions and compares neutral base, explicitly prompted base and unprompted adapter.

## Rejected drafts

**Gemma 4 E2B teacher data:** 128/128 outputs passed the four-line surface check, but manual inspection found broken Polish, non-rhymes and incorrect content. The data was not used for training. Generation took 167.9 seconds, timed remote execution 196.6 seconds, estimated requested compute $0.0558. See [data review](../additional/notes/data-review.md) and [execution record](../runs/style-data-poetry-1788771080241515907/execution.json).

**Gemma 4 E2B poetry adapter:** on the authored dataset, 192 updates / 12 epochs took **283.1 seconds (4.7 minutes)**. Four-line outputs: neutral base 1/8, prompted base 8/8, fine-tuned 7/8. Saved-adapter reload matched on four probes. Peak allocated VRAM was 11.53 GB, timed remote execution 392.4 seconds, estimated requested compute $0.1113.

This is **not the recommended showcase**. Format changed, but held-out answers were frequently incoherent or unhelpful. The DNS answer did not explain DNS, and the rubber-duck answer incorrectly advised leaving out setup and expected state. The unchanged model also had serious Polish comprehension/content problems, including interpreting “force push” as muscle training. Near-zero training loss did not establish useful generalization. [All fine-tuned outputs](../runs/style-train-poetry-1788772024290826300/finetuned.json), [execution record](../runs/style-train-poetry-1788772024290826300/execution.json).

## Qwen3.5-4B experiments

| Persona | Updates | Training | Timed remote | Estimated compute | Reload |
|---|---:|---:|---:|---:|---|
| Comic wit | 62 | 304.4 s / 5.1 min | 444.9 s | $0.1262 | 4/4 matched |
| Poetry | 64 | 352.1 s / 5.9 min | 466.9 s | $0.1325 | 4/4 matched |

Both learned an obvious output format change without a style prompt. Poetry produced four lines on 8/8 held-out questions, including a request for prose. Wit produced short answers on 8/8. **Neither result establishes consistently good literary quality.** Polish remained weak, including broken grammar and unhelpful technical answers. English had some usable examples: a rhyming Moon explanation and a comic robot-vacuum answer, but also missed instructions and weak explanations.

A fixed-seed sampled-decoding probe on the poetry adapter cost $0.0184 and did not resolve these issues. All attempts and observations are in the lab notebook. The explicit style-prompt baseline is included throughout; it also had quality problems.

The comic adapter's sampled probe cost $0.0305 and had similar limitations. [Open the complete offline comparison](http://localhost:5173/reports#showcase.html): 32 prompt cards, 96 real answers, and a Polish/English filter. The Gemma attempt has a [separate rejected-run comparison](http://localhost:5173/reports#rejected-gemma.html).

## Accounting and interpretation

Costs are estimates from timed remote execution × (L4 $0.000222/s + two CPU cores × $0.0000131/s + 16 GiB RAM × $0.00000222/s). They exclude startup/builds, persistent storage and resource use above the requested allocation, and are not billing receipts. Rates: [Modal pricing](https://modal.com/pricing). The discarded draft and rejected model are included in preparation spending.

Every model sees the same 192-new-token cap. This can truncate long base-model explanations. Four-line or short-answer rates are surface measurements, not quality scores. There is no claim of statistical significance, robust persona enforcement, or improvement in general capability. Reading outputs is mandatory.
