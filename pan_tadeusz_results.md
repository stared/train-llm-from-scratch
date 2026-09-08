# Full Pan Tadeusz: ordinary Polish chat results

**Model for all examples: LiquidAI/LFM2.5-2.6B, revision `654f9463ce32b05d0429d76fe1f580b27d4c1ac0`. Before: original checkpoint, no workshop fine-tuning. After: full-strength LoRA trained by raw-text continued pretraining on all twelve books and the epilogue of Adam Mickiewicz's Pan Tadeusz from Wolne Lektury.** One full pass, 333 updates, 61.3 seconds training. No authored Q&A examples were used in this adapter.

Four ordinary questions and four statements, chat template, no style or system instruction. Sampled with seed 42, temperature .7, top-p .8, top-k 20, repetition penalty 1.1, batches of four and a 192-new-token cap. No additional training for this evaluation.

**Result:** these probes do not show reliable poetic chat transfer. All eight adapted outputs begin with English planning text. Five reach a Polish reply within the cap; the visible replies are mostly ordinary prose. Three never reach a final reply within the cap. This is a limitation of the tested checkpoint/template/budget combination, not proof that no longer output or other training recipe could work. The original checkpoint also produces planning text, so this behavior cannot be attributed solely to book adaptation.

For readability, the comparisons below show only text after the literal `</think>` delimiter. If it is absent, we report no final answer within the cap. These extracted replies may still be cut short; no missing text is invented. Full unmodified outputs are retained in the raw record.

## 1. Dlaczego mój komputer znowu się zawiesił?

**Before — LFM2.5-2.6B, no workshop fine-tuning:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

**After — LFM2.5-2.6B, LoRA on full Pan Tadeusz:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

## 2. Nie wiem, co chcę robić w życiu. Od czego zacząć?

**Before — LFM2.5-2.6B, no workshop fine-tuning:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

**After — LFM2.5-2.6B, LoRA on full Pan Tadeusz:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

## 3. Dlaczego warto robić kopie zapasowe?

**Before — LFM2.5-2.6B, no workshop fine-tuning:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

**After — LFM2.5-2.6B, LoRA on full Pan Tadeusz:**

> Kopiowanie danych na tzw. **kopię zapasową** to jedno z najważniejszych ruchów w cyfrowym świecie. Oto główne powody, dla których

## 4. Co robimy wieczorem?

**Before — LFM2.5-2.6B, no workshop fine-tuning:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

**After — LFM2.5-2.6B, LoRA on full Pan Tadeusz:**

> To zależy od tego, jaką atmosferę chce

## 5. Cześć, właśnie wróciłem z pracy.

**Before — LFM2.5-2.6B, no workshop fine-tuning:**

> Cześć! Super, że już wracasz do domu. Jak miała się Twoja praca? Mam nadzieję, że wszystko poszło dobrze i że masz czas na coś przyjemnego po pracy. 😊
> 
> Jeśli chcesz porozmawiać o dniu, mieć jakieś rady

**After — LFM2.5-2.6B, LoRA on full Pan Tadeusz:**

> Cześć! Jak się masz? Wszystko w porządku po pracy? Mogę Ci pomóc w czymś, jeśli coś Ci spodobało się lub trzeba coś wyjaśnić – albo po prostu pogadamy na chwilę. 😊

## 6. Dzisiaj wszystko idzie nie tak.

**Before — LFM2.5-2.6B, no workshop fine-tuning:**

> Rozumiem, że masz trudny dzień. Czasami rzeczy po prostu nie idą po zamierzeniu i

**After — LFM2.5-2.6B, LoRA on full Pan Tadeusz:**

> Rozumiem – coś się dzieje, co Cię martwi lub zdenerwuje. Chętnie posłucham, jeśli chcesz opowiedzieć więcej o tym, co się stało, albo po prostu usłyszeć Twoją perspektywę.
> 
> Co dokładnie masz na myśli? Czy chodzi o jakiś konkretny problem (techniczny, osobisty, zawodowy?), czy może o ogólne niepokoj

## 7. Za oknem pada deszcz, a ja siedzę przy komputerze.

**Before — LFM2.5-2.6B, no workshop fine-tuning:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

**After — LFM2.5-2.6B, LoRA on full Pan Tadeusz:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

## 8. Dobra, jedziemy. Samochód już czeka.

**Before — LFM2.5-2.6B, no workshop fine-tuning:**

No final reply reached within the 192-new-token cap; saved output contains planning text.

**After — LFM2.5-2.6B, LoRA on full Pan Tadeusz:**

> Cześć! Dobrej drogi, że jesteśmy razem w tym dniu.
> Więc kierowca od raz

[Raw outputs and exact corpus/model metadata](runs/corpus-probe-1788793991034451951/probe.json) · [Training recipe](PAN_TADEUSZ.md).

Successful evaluation: 71.64 s timed remote execution, approximately $0.02033 requested compute, excluding startup/storage.

## Later larger-context experiment

The fresh 2,048-target line-aligned adapter has now been trained and tested, including two 1,024-output-token diagnostics. [Full comparison with this original 256-target adapter](pan_tadeusz_2048_results.md).
