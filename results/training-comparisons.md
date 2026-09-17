# Training comparisons

Exploratory measurements, not guaranteed outcomes. Checkpoints are selected using development data. Test sets are small and have been inspected in previous experiments; these are not fresh, blind benchmarks.

Plain-text corpus v1 and the earlier 5,000-definition data used a faulty reference-removal expression. It could delete intervening prose after a self-closing ref. Those data comparisons are superseded; original-markup Wikipedia and Wolne Lektury are unaffected. Version2 fixes this with a regression test.

Costs are worker GPU + CPU/memory estimates, excluding image builds, controller and storage. Post-training and continued-pretraining costs exclude the earlier pretraining. For chains, the cost shown on each stage row is the whole run, not an additional charge. Losses on different corpora cannot be compared directly. Existing-model SFT→RLVR chains use the original base model as the KL reference; scratch-model chains use the SFT checkpoint. These are different regularization choices. Wikipedia definition loss uses 50 held-out examples whose articles retain their original pretraining split; this is not a test of recalling facts from those same articles in training. Poetry loss uses 25 held-out prompts, but their source verses may appear in pretraining.

Failed/canceled calls recorded: 9; known worker estimates $0.031. Canceled calls have unknown billing; an additional $8.257 full-timeout bound is reserved separately.

Completed workers in this report: $54.834.

## What changed

- For ten-minute Wolne Lektury pretraining, H100 processed more tokens per dollar than L4. Compiling the training forward almost doubled throughput again; it did not double text quality.
- The cheaper expanded-data SFT recipe reached 31–32/40 across three seeds in three minutes, about $0.07 per worker. Rotated options gave 30–33/40. This is the practical workshop extension.
- Qwen3.5-0.8B + SFT on 289 official driving questions reached 33–35/40 across three seeds, versus 21/40 before training. Direct RLVR reached 29–33/40. Each run cost about $0.19; rotated options reveal remaining sensitivity.
- Wikipedia-pretrained 98M and 291M scratch models reached 20/40 with full-weight SFT and 22/40 with LoRA on 100 driving questions. Expanded-data scratch SFT reached 21–23/40. Direct RLVR did not improve the 100-question models. These results do not establish full-exam passing ability.
- SFT on 5,000 Wikipedia title/definition pairs taught short-answer formatting, but answers still invented facts. Wolne Lektury + Pan Tadeusz Q&A learned verse-like replies with weak relevance and meter.
- With an explanation prompt, Qwen3.5-2B RLVR improved strict final-answer compliance from 0 to 25/40 by removing explanations. Accepting the explicit answer anywhere gives 25/40 both before and after. The reward did not require an explanation; this is format learning, not evidence of better reasoning. The any-position score is a post-hoc diagnostic, not the training reward.
- Thirty-minute Wolne Lektury pretraining improved test loss to 2.720 for $2.12. Ten minutes with compilation reached 2.748 for $0.73: a more practical workshop recipe.

![Repeated driving-exam runs](exam-comparison.svg)

![Development curves: selected and final checkpoints](checkpoint-selection.svg)

![Wikipedia training time, loss and cost](wikipedia-scaling.svg)

Original markup, shared 8k tokenizer. Schedules, batches and compilation differ; this is not a controlled scaling-law estimate. Lower text loss does not establish factual accuracy.

## GPU and architecture comparisons

|Model|Corpus|Context|GPU|Training min|Test loss|Tokens M|Corpus-equivalents|Tokens M / $|Worker $|
|---|---|---|---|---|---|---|---|---|---|
|ScratchGPT-30m|wl-scratch-v1|1024|H100|10.0|9.073 → 2.821|419.6|4.14|567.3|$0.740|
|ScratchGPT-30m-wide|wl-scratch-v1|512|H100|10.0|9.096 → 2.789|480.1|4.74|656.1|$0.732|
|ScratchGPT-30m|wl-scratch-v1|512|A10|10.0|9.073 → 3.064|72.2|0.71|315.6|$0.229|
|ScratchGPT-30m|wl-scratch-v1|512|H100|10.0|9.073 → 2.784|394.4|3.89|534.0|$0.738|
|ScratchGPT-30m|wl-scratch-v1|512|L4|10.0|9.073 → 3.152|50.0|0.49|277.8|$0.180|
|ScratchGPT-30m|wl-scratch-v1|512|L40S|10.0|9.073 → 2.885|180.1|1.78|478.0|$0.377|
|ScratchGPT-30m|wiki-scratch-v1|512|H100|10.0|9.081 → 1.711|403.9|0.13|539.6|$0.749|
|ScratchGPT-30m-wide|wiki-scratch-v1|512|H100|10.0|9.138 → 1.716|489.7|0.16|656.4|$0.746|
|ScratchGPT-30m|wl-scratch-v1|512|H100|10.0|9.073 → 2.748|723.7|7.14|990.0|$0.731|
|ScratchGPT-30m|wl-scratch-v1|512|H100|30.0|9.073 → 2.720|1260.1|12.44|594.7|$2.119|
|ScratchGPT-100m|wiki-scratch-v1|512|H100|10.0|9.174 → 1.619|272.5|0.09|356.2|$0.765|
|ScratchGPT-100m|wiki-scratch-v1|512|L40S|10.0|9.174 → 1.914|79.1|0.03|202.3|$0.391|
|ScratchGPT-300m|wiki-scratch-v1|512|H100|10.0|9.210 → 1.790|95.0|0.03|119.2|$0.797|
|ScratchGPT-300m|wiki-scratch-v1|512|L40S|10.0|9.210 → 2.480|23.7|0.01|58.4|$0.406|
|ScratchGPT-100m|wiki-scratch-v1|512|H100|30.0|9.174 → 1.426|920.4|0.29|430.9|$2.136|
|ScratchGPT-30m|wiki-scratch-v1|512|H100|10.0|9.081 → 1.653|717.2|0.23|972.2|$0.738|
|ScratchGPT-100m|wiki-leads-v1|512|H100|10.0|9.153 → 1.740|285.0|1.61|380.8|$0.748|
|ScratchGPT-100m [superseded data]|wiki-plain-leads-v1|512|H100|10.0|9.171 → 2.154|284.9|3.63|381.2|$0.747|
|ScratchGPT-300m|wiki-leads-v1|512|H100|10.0|9.216 → 1.843|102.8|0.58|133.9|$0.768|
|ScratchGPT-300m [superseded data]|wiki-plain-leads-v1|512|H100|10.0|9.228 → 2.199|103.0|1.31|134.6|$0.765|
|ScratchGPT-30m|wiki-leads-v1|512|H100|10.0|9.092 → 1.771|705.6|3.98|953.3|$0.740|
|ScratchGPT-30m [superseded data]|wiki-plain-leads-v1|512|H100|10.0|9.116 → 2.196|709.3|9.03|959.5|$0.739|
|ScratchGPT-100m-deep|wiki-scratch-v1|512|H100|10.0|9.134 → 1.696|192.4|0.06|232.7|$0.827|
|ScratchGPT-100m|wiki-scratch-v1|512|H100|10.0|9.174 → 1.636|276.4|0.09|353.5|$0.782|
|ScratchGPT-100m-wide|wiki-scratch-v1|512|H100|10.0|9.223 → 1.599|336.1|0.11|436.9|$0.769|
|ScratchGPT-300m|wiki-scratch-v1|512|H100|10.0|9.210 → 2.007|94.4|0.03|107.2|$0.881|
|ScratchGPT-100m|wiki-scratch-v1|512|H100|50.0|9.174 → 1.339|1632.9|0.52|459.0|$3.557|
|ScratchGPT-100m|wiki-scratch-v1|512|H100|50.0|9.174 → 1.402|1528.3|0.49|431.4|$3.543|
|ScratchGPT-300m|wiki-scratch-v1|512|H100|50.0|9.210 → 1.376|606.9|0.19|168.7|$3.598|
|ScratchGPT-30m|wiki-scratch-v1|512|H100|50.0|9.081 → 1.509|3618.1|1.15|1021.0|$3.544|

## Driving exam: existing models

|Starting model|Method|Train questions|GPU / batch|LR|Seed|Test /40|Dev /25|Rotated /40|Training min|Run worker $|
|---|---|---|---|---|---|---|---|---|---|---|
|Qwen/Qwen3.5-0.8B|rlvr|100|L4/batch 4|5e-05|42|21 → 23|21|25|10.0|$0.185|
|Qwen/Qwen3.5-0.8B|sft|100|L4/batch 4|5e-05|42|21 → 28|22|29|10.0|$0.182|
|Qwen/Qwen3.5-2B|rlvr|100|L4/batch 4|5e-05|42|26 → 28|22|27|10.0|$0.198|
|Qwen/Qwen3.5-2B|sft|100|L4/batch 4|5e-05|42|26 → 27|22|27|10.0|$0.196|
|Qwen/Qwen3.5-0.8B|sft + answer text|100|L4/batch 4|2e-05|42|14 → 28|20|25|1.0|$0.030|
|Qwen/Qwen3.5-0.8B|rlvr|100|L4/batch 4|2e-05|123|21 → 28|22|26|10.0|$0.182|
|Qwen/Qwen3.5-0.8B|sft|100|L4/batch 4|2e-05|123|21 → 29|23|30|10.0|$0.184|
|Qwen/Qwen3.5-0.8B|sft + answer text|100|L4/batch 4|2e-05|42|14 → 31|21|26|10.0|$0.181|
|Qwen/Qwen3.5-0.8B|sft|100|L4/batch 4|2e-05|42|21 → 27|22|30|10.0|$0.359|
|Qwen/Qwen3.5-0.8B|sft → rlvr|100|L4/batch 4|2e-05|42|27 → 30|23|25|10.0|$0.359|
|Qwen/Qwen3.5-2B|sft + answer text|100|L4/batch 4|2e-05|42|12 → 27|23|27|10.0|$0.186|
|Qwen/Qwen3.5-2B|sft|100|L4/batch 4|2e-05|42|26 → 28|23|29|10.0|$0.376|
|Qwen/Qwen3.5-2B|sft → rlvr|100|L4/batch 4|2e-05|42|28 → 26|24|26|10.0|$0.376|
|Qwen/Qwen3.5-4B|rlvr|100|L40S/batch 4|2e-05|42|31 → 32|23|32|10.0|$0.391|
|Qwen/Qwen3.5-4B|sft|100|L4/batch 2|2e-05|42|32 → 33|23|34|10.1|$0.214|
|Qwen/Qwen3.5-4B|sft|100|L40S/batch 4|2e-05|42|31 → 35|23|32|10.0|$0.391|
|Qwen/Qwen3.5-0.8B|rlvr|289|L4/batch 4|2e-05|42|21 → 32|21|26|10.0|$0.187|
|Qwen/Qwen3.5-0.8B|sft|289|L4/batch 4|2e-05|42|21 → 33|20|32|10.0|$0.190|
|Qwen/Qwen3.5-2B|rlvr|289|L4/batch 4|2e-05|42|26 → 27|22|26|10.0|$0.191|
|Qwen/Qwen3.5-2B|sft|289|L4/batch 4|2e-05|42|26 → 26|24|25|10.0|$0.190|
|Qwen/Qwen3.5-0.8B|rlvr|289|L4/batch 4|2e-05|123|21 → 33|21|31|10.0|$0.194|
|Qwen/Qwen3.5-0.8B|rlvr|289|L4/batch 4|2e-05|2026|21 → 29|22|26|10.0|$0.189|
|Qwen/Qwen3.5-0.8B|sft|289|L4/batch 4|2e-05|123|21 → 33|21|29|10.0|$0.190|
|Qwen/Qwen3.5-0.8B|sft|289|L4/batch 4|2e-05|2026|21 → 35|21|32|10.0|$0.190|
|Qwen/Qwen3.5-0.8B|sft|289|L4/batch 4|2e-05|42|21 → 32|20|33|3.0|$0.072|
|Qwen/Qwen3.5-4B|rlvr|289|L40S/batch 4|2e-05|42|31 → 32|24|34|10.0|$0.403|
|Qwen/Qwen3.5-4B|sft|289|L40S/batch 4|2e-05|42|31 → 36|24|34|10.0|$0.402|
|Qwen/Qwen3.5-0.8B|sft|289|L4/batch 4|2e-05|123|21 → 31|20|30|3.0|$0.071|
|Qwen/Qwen3.5-0.8B|sft|289|L4/batch 4|2e-05|2026|21 → 31|19|31|3.0|$0.071|

## Scratch models after pretraining

|Starting checkpoint|Initialization|Task|Stage|LR|Test correct /40 or answer loss|Training min|Run worker $|
|---|---|---|---|---|---|---|---|
|98.3M Polish Wikipedia|pretrained|100 driving questions|sft|0.0001|12 → 16|1.0|$0.041|
|98.3M Polish Wikipedia|pretrained|100 driving questions|sft → rlvr|0.0001|12 → 15|1.0|$0.041|
|98.3M Polish Wikipedia|pretrained|5,000 Wikipedia definitions|sft|0.0001|2.304 → 1.785|1.0|$0.033|
|29.9M Wolne Lektury|pretrained|450 Pan Tadeusz Q&A|sft|0.0001|3.081 → 2.809|1.0|$0.028|
|98.3M random weights|random|100 driving questions|rlvr|2e-05|15 → 15|10.0|$0.173|
|98.3M random weights|random|100 driving questions|sft|2e-05|15 → 15|10.0|$0.173|
|98.3M Polish Wikipedia|pretrained|100 driving questions|sft|2e-05|12 → 20|10.0|$0.347|
|98.3M Polish Wikipedia|pretrained|100 driving questions|sft → rlvr|2e-05|12 → 18|10.0|$0.347|
|98.3M Polish Wikipedia|pretrained|100 driving questions|rlvr|2e-05|12 → 12|10.0|$0.175|
|98.3M Polish Wikipedia|pretrained|100 driving questions|sft|2e-05|12 → 20|10.0|$0.175|
|98.3M Polish Wikipedia|pretrained|450 Pan Tadeusz Q&A|sft|2e-05|4.070 → 3.505|10.0|$0.187|
|98.3M Polish Wikipedia|pretrained|5,000 Wikipedia definitions|sft|2e-05|2.304 → 1.607|10.0|$0.183|
|291.0M Polish Wikipedia|pretrained|100 driving questions|sft|2e-05|13 → 20|10.0|$0.352|
|291.0M Polish Wikipedia|pretrained|100 driving questions|sft → rlvr|2e-05|13 → 20|10.0|$0.352|
|291.0M Polish Wikipedia|pretrained|100 driving questions|rlvr|2e-05|13 → 13|10.0|$0.181|
|291.0M Polish Wikipedia|pretrained|100 driving questions|sft|2e-05|13 → 20|10.0|$0.180|
|291.0M Polish Wikipedia|pretrained|5,000 Wikipedia definitions|sft|2e-05|2.193 → 1.577|10.0|$0.192|
|98.3M Wolne Lektury|pretrained|100 driving questions|rlvr|2e-05|12 → 12|10.0|$0.175|
|98.3M Wolne Lektury|pretrained|100 driving questions|sft|2e-05|12 → 19|10.0|$0.176|
|98.3M Wolne Lektury|pretrained|450 Pan Tadeusz Q&A|sft|2e-05|2.865 → 2.444|10.0|$0.185|
|29.9M Wolne Lektury|pretrained|100 driving questions|rlvr|2e-05|14 → 14|10.0|$0.175|
|29.9M Wolne Lektury|pretrained|100 driving questions|sft|2e-05|14 → 22|10.0|$0.175|
|29.9M Wolne Lektury|pretrained|450 Pan Tadeusz Q&A|sft|2e-05|3.081 → 2.736|10.0|$0.180|
|98.3M Polish Wikipedia|pretrained|100 driving questions|rlvr (LoRA 8)|5e-05|12 → 12|1.0|$0.025|
|98.3M Polish Wikipedia|pretrained|100 driving questions|sft (LoRA 8)|5e-05|12 → 22|10.0|$0.177|
|291.0M Polish Wikipedia|pretrained|100 driving questions|sft (LoRA 8)|5e-05|13 → 22|10.0|$0.182|
|98.3M Polish Wikipedia|pretrained|289 driving questions|sft|2e-05|12 → 22|10.0|$0.177|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft (LoRA 8)|5e-05|13 → 23|10.0|$0.185|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft|2e-05|13 → 21|10.0|$0.181|
|29.9M Wolne Lektury|pretrained|289 driving questions|sft|2e-05|14 → 23|10.0|$0.175|
|98.3M Polish Wikipedia|pretrained|289 driving questions|sft|1e-05|12 → 22|0.2|$0.040|
|98.3M Polish Wikipedia|pretrained|Polish OWCA instructions|sft|3e-05|2.625 → 1.988|1.0|$0.141|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft|1e-05|13 → 23|0.2|$0.067|
|291.0M Polish Wikipedia|pretrained|Polish OWCA instructions|sft|3e-05|2.603 → 2.011|1.0|$0.164|
|98.3M Polish Wikipedia|pretrained|Polish OWCA instructions|sft|0.0001|2.625 → 1.962|3.2|$0.291|
|98.3M Polish Wikipedia|pretrained|Polish OWCA instructions|sft|3e-05|2.625 → 1.876|3.5|$0.304|
|291.0M Polish Wikipedia|pretrained|Polish OWCA instructions|sft|0.0001|2.603 → 1.953|6.4|$0.548|
|291.0M Polish Wikipedia|pretrained|Polish OWCA instructions|sft|3e-05|2.603 → 1.902|6.3|$0.538|
|98.3M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|12 → 25|0.9|$0.086|
|98.3M Polish Wikipedia|pretrained|289 driving questions|sft|1e-05|12 → 22|1.0|$0.100|
|98.3M Polish Wikipedia|pretrained|289 driving questions|sft|1e-06|12 → 23|0.9|$0.084|
|98.3M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|22 → 27|1.4|$0.128|
|291.0M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|13 → 27|2.2|$0.194|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft|1e-05|13 → 21|1.7|$0.154|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft|1e-06|13 → 25|1.8|$0.168|
|291.0M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|23 → 23|2.1|$0.189|
|98.3M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|11 → 17|1.1|$0.106|
|98.3M Polish Wikipedia|pretrained|289 driving questions|sft|1e-06|11 → 21|0.9|$0.088|
|291.0M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|9 → 17|1.9|$0.203|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft|1e-06|9 → 19|1.9|$0.177|
|98.3M random weights|random|289 driving questions|rlvr|1e-06|15 → 15|1.4|$0.130|
|98.3M random weights|random|289 driving questions|sft|1e-06|15 → 14|1.0|$0.090|
|291.0M random weights|random|289 driving questions|rlvr|1e-06|10 → 15|2.1|$0.188|
|291.0M random weights|random|289 driving questions|sft|1e-06|10 → 10|2.1|$0.196|
|98.3M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|22 → 28|1.2|$0.118|
|98.3M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|22 → 27|1.5|$0.197|
|291.0M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|13 → 26|2.2|$0.200|
|291.0M Polish Wikipedia|pretrained|289 driving questions|rlvr|1e-06|13 → 27|2.1|$0.194|
|98.3M Polish Wikipedia|pretrained|289 driving questions|sft (3-action CE + KL)|1e-06|12 → 25|1.0|$0.090|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft (3-action CE + KL)|1e-06|13 → 26|2.2|$0.199|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft (3-action CE + KL)|1e-06|13 → 27|1.7|$0.152|
|291.0M Polish Wikipedia|pretrained|289 driving questions|sft (3-action CE + KL)|1e-06|13 → 25|2.3|$0.207|
|98.3M Polish Wikipedia|pretrained|9,602 Wikipedia definitions|sft|0.0001|2.503 → 1.886|3.7|$0.316|
|98.3M Polish Wikipedia|pretrained|9,602 Wikipedia definitions|sft|3e-05|2.503 → 1.800|3.3|$0.275|
|291.0M Polish Wikipedia|pretrained|9,602 Wikipedia definitions|sft|0.0001|2.440 → 1.905|7.0|$0.588|
|291.0M Polish Wikipedia|pretrained|9,602 Wikipedia definitions|sft|3e-05|2.440 → 1.829|6.5|$0.546|

## Driving exam: explanation prompt, final-answer RLVR

|Model|Steps|Selected step|Strict final-answer score /40|Answer anywhere /40|Answer-only outputs /40|Training min|Worker $|
|---|---|---|---|---|---|---|---|
|Qwen/Qwen3.5-0.8B|100|40|12 → 25|24 → 25|4 → 39|10.0|$0.861|
|Qwen/Qwen3.5-2B|100|40|0 → 25|25 → 25|0 → 40|7.7|$0.710|

## Common-corpus and instruction diagnostics

|Checkpoint|Stage|Raw Wikipedia test loss|Raw leads test loss|Plain v1 test loss (superseded)|Plain v2 test loss|Raw fact probes|Plain fact probes|Evaluation worker $|
|---|---|---|---|---|---|---|---|---|
|scratch-polish-dollar-1788900395083493729-wiki-100-uniform|pretraining|1.301|1.629|2.444|—|7/10|8/10|$0.023|
|night-1789681010832431000-wiki-100m-instruction-lr3e-05|instruction|1.547|1.924|2.670|—|6/10|5/10|$0.018|
|night-1789680156069063000-wiki-100m-compiled-H100|pretraining|1.619|1.987|2.852|—|7/10|5/10|$0.023|
|scratch-polish-dollar-1788900395083493729-wiki-300-uniform|pretraining|1.286|1.602|2.400|—|7/10|6/10|$0.039|
|night-1789681010832431000-wiki-300m-instruction-lr3e-05|instruction|1.553|1.931|2.714|—|8/10|5/10|$0.027|
|night-1789680156069063000-wiki-300m-compiled-H100|pretraining|1.790|2.185|3.083|—|3/10|3/10|$0.037|
|night-1789681093646214000-100m-wiki-leads-v1|pretraining|2.199|1.740|2.710|—|5/10|8/10|$0.028|
|scratch-polish-dollar-1788900395083493729-wiki-100-uniform|pretraining|1.301|1.629|2.444|—|7/10|8/10|$0.030|
|scratch-polish-dollar-1788900395083493729-wiki-300-uniform|pretraining|1.286|1.602|2.400|—|7/10|6/10|$0.056|
|night-1789681093646214000-100m-wiki-plain-leads-v1|pretraining|4.846|4.318|2.153|—|7/10|8/10|$0.016|
|night-1789681093646214000-300m-wiki-plain-leads-v1|pretraining|4.845|4.251|2.199|—|8/10|6/10|$0.039|
|night-1789681284848231000-wiki-100m-wide-lr0.0006|pretraining|1.599|1.972|2.842|—|5/10|6/10|$0.021|
|night-1789681093646214000-100m-wiki-leads-v1|pretraining|—|—|—|—|5/10|8/10|$0.037|
|scratch-polish-dollar-1788900395083493729-wiki-100-uniform|pretraining|—|—|—|—|7/10|8/10|$0.022|
|night-1789681093646214000-100m-wiki-plain-leads-v1|pretraining|—|—|—|—|7/10|8/10|$0.031|
|night-1789681093646214000-300m-wiki-plain-leads-v1|pretraining|—|—|—|—|8/10|6/10|$0.048|
|night-1789684048200921000-wiki-100m-popular-qa-lr0.0001|wiki-qa|3.846|—|—|4.140|6/10|5/10|$0.033|
|night-1789684048200921000-wiki-100m-popular-qa-lr0.0001|wiki-qa|1.518|—|—|2.529|9/10|8/10|$0.031|
|night-1789684048200921000-wiki-100m-popular-qa-lr3e-05|wiki-qa|2.322|—|—|3.514|8/10|8/10|$0.037|
|night-1789684048200921000-wiki-100m-popular-qa-lr3e-05|wiki-qa|1.403|—|—|2.401|9/10|8/10|$0.030|
|night-1789684048200921000-wiki-300m-popular-qa-lr0.0001|wiki-qa|3.436|—|—|3.892|9/10|5/10|$0.059|
|night-1789684048200921000-wiki-300m-popular-qa-lr0.0001|wiki-qa|1.489|—|—|2.497|9/10|7/10|$0.048|
|night-1789684048200921000-wiki-300m-popular-qa-lr3e-05|wiki-qa|2.009|—|—|3.305|9/10|7/10|$0.053|
|night-1789684048200921000-wiki-300m-popular-qa-lr3e-05|wiki-qa|1.384|—|—|2.366|9/10|7/10|$0.054|

[Curves and selected literal before/after answers](training-comparisons.html).
