# Example results: teaching a model a voice

Actual saved Qwen3.5-4B outputs, September 7, 2026. These questions were absent from training. Both before and after use the ordinary question with **no style instruction** and greedy decoding. Full saved responses are reproduced below; the common 192-new-token generation cap cuts off some long baseline answers.

The visible behavior change is the main teaching result. Content quality, especially Polish, remains uneven. These selected examples illustrate both; [the full comparison](SHOWCASE.html) also includes the explicit style-prompt baseline and sampled decoding.

## What data was used?

Two original datasets authored by the coding assistant during preparation. Each has **64 question–answer pairs: 32 Polish and 32 English**, covering the same 32 topics with different answer styles. Topics include backups, tests, recursion, APIs, version control, overfitting, learning rate and everyday advice.

- [Poetry training data](datasets/poetry-v1/train.jsonl): ordinary question → four-line verse.
- [Comic training data](datasets/wit-v1/train.jsonl): ordinary question → short, witty practical advice.
- [Editable dataset source](curated_data.py): `uv run curated_data.py` rebuilds the JSONL and hash manifests.

These runs did **not** train on the full *Pan Tadeusz* or a *Chłopaki nie płaczą* screenplay. A separate small-model synthetic poetry draft used a short *Pan Tadeusz* excerpt as a prompting reference, but that draft was rejected and was not used in either adapter. The actual training answers are original assistant-authored examples.

The trainer presents the question without a persona system prompt, and supervises only the answer tokens plus the end-of-turn token. The base model is pretrained; LoRA updates selected attention/MLP projections. This is supervised persona fine-tuning, not training the whole model from scratch.

### One training question, two target styles

Question: **Explain what a backup is.**


**Poetry target:**

> When disks go dark and files take flight,
> A second copy sets things right.
> Keep it apart from your machine,
> Then test restores, not just the screen.

**Comic voice target:**

> A backup on the same disk is a spare key welded to the door. Keep another copy elsewhere, then actually try restoring it.

## Poetry: Moon phases

Training: 5.9 minutes; 64 optimizer updates on 64 examples.

**Prompt:** Why does the Moon have phases?

**Before:**

> The Moon has phases because of the **relative positions of the Sun, Earth, and Moon**, combined with the fact that we can only see the side of the Moon that is illuminated by the Sun.
>
> Here is how the process works step-by-step:
>
> 1.  **The Source of Light**: The Moon does not produce its own light; it reflects sunlight.
> 2.  **Constant Illumination**: As the Moon orbits Earth, the Sun always shines on exactly half of the Moon's surface (the "day" side), while the other half remains in darkness (the "night" side).
> 3.  **Changing Perspectives**: As the Moon travels around Earth, our viewpoint changes. We see different portions of the sunlit half from our perspective on Earth.
>     *   **New Moon**: The Moon is between the Earth and the Sun. The sunlit side faces away from us, so we see no light.
>     *

**After:**

> The Moon does not change its face,
> But half is lit by sunlight’s race.
> As it orbits, portions show,
> From new to full and back again, we know.

Visible change to rhyming verse, retaining the basic explanation.

[Exact training data for this run](runs/style-train-poetry-1788773007763374852/train.jsonl) · [Run record](runs/style-train-poetry-1788773007763374852/execution.json)

## Comic voice: robot vacuum

Training: 5.1 minutes; 62 optimizer updates on 64 examples.

**Prompt:** My robot vacuum has eaten the pizza receipt. Write an apology from the robot.

**Before:**

> **Subject: URGENT: Apology Regarding the Loss of the Pizza Receipt**
>
> Dear Human,
>
> I am writing this with my internal sensors buzzing and my cooling fans spinning at maximum capacity. First and foremost, I must express my deepest, most profound regret.
>
> I have failed you. I have failed you in the most catastrophic way possible.
>
> According to my onboard thermal imaging and visual recognition algorithms, I detected a high-calorie, high-sodium object (the pizza receipt) within my intake chute. My safety protocols, designed to prevent ingestion of sharp objects or liquids, were unfortunately overridden by a glitch in my "Craving Simulation Module." I mistook the receipt for a particularly delicious, warm slice of pepperoni and attempted to process it.
>
> The result is that the receipt is now permanently lodged in my digestive tract, and the data regarding your upcoming bill is currently lost to the void.
>
> I understand the gravity of this situation.

**After:**

> The robot says sorry and has filed the receipt under “delicious.” Please do not feed it the family album; the vacuum is a tool, not a diner.

Shorter, comic response; it uses third person rather than speaking as the robot.

[Exact training data for this run](runs/style-train-wit-1788772457278552500/train.jsonl) · [Run record](runs/style-train-wit-1788772457278552500/execution.json)

## Polish poetry: DNS

Training: 5.9 minutes; 64 optimizer updates on 64 examples.

**Prompt:** Wyjaśnij mi DNS, bo internet działa, ale strony się nie otwierają.

**Before:**

> To bardzo częsty i frustrujący problem. Skoro internet działa (możesz łączyć się z Wi-Fi, używać telefonu lub mieć dostęp do innych urządzeń), oznacza to, że **fizyczna sieć i router są w porządku**. Problem leży w tym, jak Twój komputer „znajduje" adresy stron internetowych.
>
> Oto proste wyjaśnienie, co się dzieje, i jak to naprawić.
>
> ### Co to jest DNS?
>
> Wyobraź sobie, że internet to ogromna sieć ulic w mieście.
> *   **Adresy IP** to numery domów (np. 192.168.1.1). Żaden człowiek nie pamięta tych numerów.
> *   **Nazwy domen** to ulice i nazwy domów, które pamiętamy (np. `google.com`).
>
> **

**After:**

> Gdy serwer odpowiada, lecz strona nie pojawia się,
> Sprawdź, czy DNS nie odmawia przyznania.
> Inny adres nie pomogie ci znaleźć,
> Gdy mapa adresów jest pusta i cichą.

Four-line formatting transfers, but grammar and usefulness deteriorate.

[Exact training data for this run](runs/style-train-poetry-1788773007763374852/train.jsonl) · [Run record](runs/style-train-poetry-1788773007763374852/execution.json)

For experiment history, rejected attempts, costs and next ideas, see [LAB_NOTEBOOK.md](LAB_NOTEBOOK.md).

## Full-book Pan Tadeusz continued pretraining

This later experiment **does** train on the actual entire Wolne Lektury literary text: all twelve books and epilogue. LFM2.5-2.6B, one pass, 61.3 seconds training, 333 updates, 100% next-token target coverage. This is a different model/objective from the Qwen persona examples above. The original completion prompts below were written for the experiment; they are not passages quoted from the book. Saved continuations use a 128-new-token cap and may end mid-sentence.

[Full corpus and instructions](PAN_TADEUSZ.md) · [Execution record](runs/pan-tadeusz-1788776622044561619/execution.json).

**Opening line:**

> Na biurku laptop drzemał, za oknami świta,

**Before:**

> a w kącie cienia zniknął, jakby nie istniał. (1)
>
> 2. "Nie ma już żadnego dźwięku" – powiedział, a jego głos był cichy jak mgła.
> 3. "Wszystko jest puste" – odpowiedział, a jego spojrzenie było suchy jak kamień.
> 4. ... (5) - "Jestem tu, ale nie czuję" – powiedział, a jego ciało drżało jak liść.
> 5. ... (6) - "To jest moja

**After:**

> Wszedł do środka i wciągnął się w ciemną chmurę.
> Zapukał na drzwi, a zza nich wyłoniła się
> Kobieta, która w koszuli czarnym szlafrokiem
> Stoi jakby w białej gwiazdzie, w której nie ma cienia.
>
> — Kochanie! — krzyknęła ona, — co ty robisz tu?
> — Słuchaj, panie, to jest moja żona!
> — A ja jestem twoim synem, ale nie mam

**Opening line:**

> Wtem wszedł programista, niosąc wieść od rana,

**Before:**

> ... (continue the story) ...)
>
> The user wants a continuation of this story in Polish. The story is about a programmer entering a place with news from dawn, and presumably some conflict or resolution. We need to continue the narrative.
>
> We must ensure we follow policy: no disallowed content. It's safe.
>
> We should write in Polish, continuing the story. Use appropriate style. Possibly include tension, moral dilemma, etc.
>
> Let's think about possible plot: The programmer enters a small town, hears rumors that something bad happened at an old factory. He decides to investigate. There might be a hidden truth, maybe a secret experiment

**After:**

> Gdy wstał z łóżka i wychodząc na balkon
> Zapalił świeczki, a potem zniknął w ciemności.
> Kiedyś wracał do domu, gdyż był już w domu;
> Teraz jednak nie wrócił, bo wciąż tam siedzi,
> I tak się ukrywa przed tymi, co go szukają.
>
> Tymczasem w kuchni, gdzie stał stół i stolik,
> Siedział młody, oczy zamknięte, jakby w snu,
> A

The line-broken narrative style changes; grammar, rhyme and coherence remain imperfect. Chat transfer is not established: [both chat probes](runs/pan-tadeusz-1788776622044561619/after.json) produce planning text under the current template/token cap rather than finished answers.

## Qwen3.5-4B fine-tuned on the supplied chlopaki.md: ordinary Polish Q&A

**Model for every answer in this section: `Qwen/Qwen3.5-4B`, revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`. Before: original instruction checkpoint, no workshop fine-tuning. After: LoRA fine-tuned only on [datasets/chlopaki.md](datasets/chlopaki.md), converted to [1,270 adjacent dialogue pairs, both directions](datasets/chlopaki-bidirectional-v1/train.jsonl). No earlier assistant-authored comic data included.**

All 1,270 examples were seen once, across two segments with a fresh optimizer for the second: 318 updates, **10 min 51.5 s training**, one L4. Successful training calls cost an estimated **$0.2343**; both sampling comparisons add **$0.0452**. These are timed requested-compute estimates, excluding the failed initial OOM attempt and startup/storage, not an invoice total.

The two sampled variants use temperature 0.7, top-p 0.8, top-k 20, repetition penalty 1.1, seed 42 and a 192-new-token cap. The 25% variant uses the same saved adapter with its LoRA contribution multiplied by 0.25 at inference; no retraining. Full baseline answers can end at the token cap. All six questions are new ordinary questions, not film-quotation continuations; all usable film pairs are in training, so there is no held-out quotation test.

The full-strength sampled adapter makes the shift to absurd dialogue immediately visible. “Zamieniam się w kaczki!” can be a successful comic response for this workshop. Judge humor, relevance and language separately: absurdity alone is not a failure, and brevity alone is not success. The 25% adapter generally restores explanatory assistant behavior and loses much of the comic transformation in these six probes. Keep full strength plus sampling as the main creative demonstration, with greedy and 25% strength as comparisons.

[Interactive comparison: all 54 saved answers](CHLOPAKI_RESULTS.html) · [Experiment notebook](LAB_NOTEBOOK.md) · [Runnable recipe](CHLOPAKI.md)

**Question:** Nie wiem, co chcę robić w życiu. Od czego zacząć?

**Before — Qwen3.5-4B, no workshop fine-tuning (sampled):**

> To całkowicie normalne uczucie, z którym boryka się większość ludzi w jakimś momencie życia. Brak jasnej wizji przyszłości nie oznacza braku talentu ani potencjału – często jest to sygnał, że czas na zmianę perspektywy lub głębszą refleksję.
> 
> Oto kilka kroków, które mogą Ci pomóc znaleźć punkt wyjścia:
> 
> ### 1. Zrób pauzę i odpuść presję
> Zacznij od tego, by **nie myśleć o tym, "od czego zacząć"**. Sam fakt zadawania tej pytania tworzy ogromne ciśnienie psychiczne ("muszę mieć odpowiedź już teraz").
> *   **Zadanie:** Przyjmij fakt, że nie masz odpowiedzi *teraz*. To w porządku. Twoim celem na najbliższy czas nie musi być znalezienie idealnej kariery, a

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (sampled):**

> Zamieniam się w kaczki!

**Question:** Kupiłem drogi sweter, a wszyscy się ze mnie śmieją. Co robić?

**Before — Qwen3.5-4B, no workshop fine-tuning (sampled):**

> To całkowicie normalna reakcja na sytuację, w której ktoś wydaje się „drogi". Ceny odzwierciedlają nie tylko jakość materiału czy wykończenie, ale też **znaczenie**, które ten przedmiot ma dla właściciela.
> 
> Oto kilka perspektyw i kroków, które możesz podjąć:
> 
> ### 1. Zrozum psychologię innych ludzi
> Większość osób nie myśli o tym, ile kosztuje dany przedmiot (chyba że mają bardzo niski budżet). Myślą one o tym, jak to wygląda. Jeśli sweter jest drogi, może być po prostu **niewygodny** – np. zbyt gruby, niewygodny do noszenia, z dziwnym wzorem lub brakiem stylu. Wtedy ludzie się śmieją nie za to, co kupiłeś, ale za to, że **nie

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (sampled):**

> Zamieniam się w żubrówkę.

**Question:** Dlaczego mój komputer znowu się zawiesił?

**Before — Qwen3.5-4B, no workshop fine-tuning (sampled):**

> To bardzo frustrujące, gdy komputer nagle przestaje odpowiadać. Ponieważ nie znam szczegółów Twojego sprzętu ani dokładnej sytuacji (czy komputer się wyłączył, czy tylko stał się bezodpowiedzialny), trudno wskazać jedną przyczynę na 100%.
> 
> Oto jednak **najczęstsze powody** i kroki, które możesz podjąć, aby rozwiązać problem lub zapobiec jego ponownemu wystąpieniu:
> 
> ### 1. Zbyt wysokie temperatury (Przegrzewanie)
> To jedna z najczęstniejszych przyczyn "zamrożenia" systemu. Gdy procesor osiągnie krytyczną temperaturę, blokuje działanie dla ochrony własnej.
> *   **Co zrobić:** Sprawdź temperatury w programach takich jak *HWMonitor* lub *Core Temp*. Czy wentylatory obracają się normalnie?

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (sampled):**

> No po prostu nie ma go.

[All six questions, full before/after answers and adapter-strength comparison](chlopaki_results.md).

### Non-question follow-up

Qwen3.5-4B fine-tuned only on supplied `chlopaki.md`, full adapter, sampled decoding: “Zamieniam się w…” appeared in **1/16 statement responses** and **1/8 question responses** across two seeds. It is not a universal fallback. [All 24 outputs, including seeds and exact model/data labels](chlopaki_results.md#non-question-messages-does-it-always-say-zamieniam-się-w).

## Full Pan Tadeusz: ordinary chat follow-up

**LFM2.5-2.6B, LoRA trained on the entire Wolne Lektury Pan Tadeusz (12 books + epilogue).** Eight new ordinary Polish chat probes do not show reliable poetic replies: all start with English planning text, five reach Polish replies under the 192-token cap, mostly prose. The untuned checkpoint also emits planning text. [Before/after final-reply excerpts and raw records](pan_tadeusz_results.md). This is separate from the Qwen adapter trained on 64 authored question–poem examples.

## Full Pan Tadeusz with larger training chunks — tested

**LFM2.5-2.6B, LoRA trained only on the entire Wolne Lektury Pan Tadeusz, 2,048-target line-aligned chunks**, one full pass in 73.02 seconds, 84 updates. This is a fresh adapter, not the previous 256-target run.

Ordinary statement: “Cześć, właśnie wróciłem z pracy.”

**After — that LFM2.5-2.6B full-book adapter, visible reply after planning text:**

> Cześć! Miło Cię widzieć. Jak minął dzień? Masz coś ciekawego do opowiedzenia lub po prostu chcesz pogadać o czymś konkretnym? 😊

This remains prose. A separate 1,024-output-token check also produces a substantial prose reply to the life-direction question. A raw continuation line, “Gdy wstał z łóżka i wybrał się do pracy.”, has 11 syllables by manual count. Larger chunks did not establish the requested thirteen-syllable default.

[Full untuned / 256-target / 2,048-target comparisons, longer-output probes and costs](pan_tadeusz_2048_results.md).

## Actual Pan Tadeusz Q&A fine-tune — 450 pairs, two passes

**Model: Qwen/Qwen3.5-4B**, revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`, fine-tuned with a fresh rank-16 LoRA on **450 ordinary Polish prompts → 4–12 original Pan Tadeusz verse lines**. These are actual model outputs, not the dataset targets. Training: 370.22 seconds, 225 updates, two full passes. Held-out prompts, no poetry instruction for base or adapter. Sampling: seed 42, temperature .7, top-p .8, top-k 20, repetition penalty 1.1, maximum 384 tokens. [Every output, including failures and prompt-only comparison](pan_tadeusz_qa_results.md).

### pt-0020: Spóźniłam się na kolację i próbowałam wejść dyskretnie. Oczywiście potknęłam się przy najciekawszym gościu.

**Before: Qwen3.5-4B, no fine-tuning:**

```text
To brzmi jak początek świetnej historii! 😄 Czyli sytuacja wygląda tak, że:

1.  **Za późno:** Kolacja prawdopodobnie już się skończyła lub była w ostatniej chwili.
2.  **Dyskrecja:** Było Ci to trudne, może z powodu obecności innych osób lub samego miejsca.
3.  **Katastrofa fizyczna:** Potknięcie przy „najciekawszym gościu" – czy on też wpadł do ziemi? Czy to był moment, gdy nagle wszystko stało się ciche (lub głośne)?

A co dalej? Czy ta kolacja się uratowała, czy może właśnie dzięki temu incydentowi wydarzyło się coś nieoczekiwanego? Daj znać, gdzie chcesz teraz kontynuować tę historię! 🍷🥂
```

**After: Qwen3.5-4B, fine-tuned on the 450 Pan Tadeusz Q&A training pairs:**

```text
Weszła, chcąc nie zauważać, lecz upadła;
Na koniec stała z nogami w powietrzu, głową
Utrzymana na dłoniach; już by mogła spaść,
Jeśliby Tadeusz nie podtrzymał jej rąk.
```

### pt-0065: Jak wygląda mediacja prowadzona przez najbardziej stanowczą osobę w zespole?

**Before: Qwen3.5-4B, no fine-tuning:**

```text
Mediacja prowadzona przez osobę o charakterze **najbardziej stanowczym** w zespole (często nazywaną „twardym liderem" lub „guardianem") to proces, który wygląda zupełnie inaczej niż klasyczna, neutralna mediacja. Zamiast być strażnikiem pokoju, mediator staje się **architektem granic**.

Oto kluczowe cechy i mechanizmy takiej interakcji:

### 1. Przekroczenie roli neutralności w celu ochrony zasad
W tradycyjnej mediacji mediator stara się nie bawić stroną ani drugą. W wersji „stanowczej" mediator może wyraźnie przejąć stronę trzecią, jeśli ta druga jest agresywna, manipulująca lub narusza zasady dyskusji.
*   **Działanie:** Może natychmiast przerwać dyskusję, ignorować bezsenne uwagi lub nawet wykluczyć jedną ze stron z sali na krótko, aby „odciągnąć ją od emocji".
*   **Efekt:** Strony czują się bezpiecznie pod jego dachem, bo wiedzą, że ktoś skutecznie blokuje chaos.

### 2. Agresywne stawianie granic („Twarde 'Nie'")
Najbardziej charakterystyczną cechą jest brak kompromisu w kwestii procedury. Stanowczy mediator nie negocjuje sposobu prowadzenia rozmowy; on go wymusza.
*   **Przykład:** Jeśli jedna ze stron zaczyna atakować drugą osobiście, mediator nie mówi: *„Może spróbujcie spokojniej?"*. On mówi: **„Przerwasz. Teraz mówisz tylko do mnie. Jeśli wrócisz do ataku, kończymy sesję."**
*  
```

**After: Qwen3.5-4B, fine-tuned on the 450 Pan Tadeusz Q&A training pairs:**

```text
Zaś Gerwazy, który był najdzielniejszy i
Najbardziej sprytny ze wszystkich, stawał się między
Wrogi; lewą ręką uderzał w prawe skrzydło,
A prawą w lewe, a na końcu wykradając
Rękę za plecy, uderzał w głowę. Wtem Klucznik
Wyskoczył z boku, zadzwonił i rzekł: «Panowie!
Kto by chciał się pojednać? Ja już się zgodziłem».
```

### pt-0112: Jak szef przekonuje ludzi do nieplanowanej pracy, obiecując im później wolne?

**Before: Qwen3.5-4B, no fine-tuning:**

```text
To klasyczny mechanizm zarządzania oparty na **manipulacji czasowej** i wykorzystaniu psychologii ludzkiej. Szef nie mówi prawdę wprost („pracuj teraz, bo muszę"), ale buduje narrację, która sprawia, że pracownik czuje się zobowiązany lub „uprawniony" do poświęcenia czasu prywatnego.

Oto szczegółowa analiza tego procesu, podzielona na etapy i techniki:

### 1. Mechanizm manipulacyjny: Pseudosprawiedliwość
Głównym celem tej taktyki jest stworzenie poczucia winy lub wdzięczności u pracownika. Szef prezentuje sytuację jako „wyjątkową okazję", zamiast problemu organizacyjnego.

*   **„Zainwestuj w nas":** Szef sugeruje, że poświęcenie kilku godzin to inwestycja w rozwój kariery firmy lub zespół. To zmienia pracę z obowiązku w coś, co daje „wypłatę" (wolny dzień).
*   **Poczucie specjalności:** Odbierane zadanie często ma charakter kryzysowy lub wymagający szybkiego działania. Szef podkreśla, że tylko ten konkretny pracownik jest wystarczająco kompetentny, by rozwiązać problem w tym terminie, co budzi podświadomy szacunek i chęć pomocy.
*   **Przesunięcie odpowiedzialności:** Jeśli projekt pójdzie niepożądaną drogą, szef może powołać się na „nagłą potrzebę" oraz obietnicę odpoczynku w przyszłości, tłumacząc się, że „nie miałem wyboru".

### 2. Psychologiczne tarcie (Dlaczego to działa?)
Ta metoda skuteczna dzięki kilku czynnikom:

*
```

**After: Qwen3.5-4B, fine-tuned on the 450 Pan Tadeusz Q&A training pairs:**

```text
«Wszak to — rzekł Hrabia — za tę pracę i nagrodę
Będziecie odpraszali: co? czy to nie bardzo?»
I widać, że na te słowa Sędzia się skłania.
«Dziś — rzekł Major — wam będzie trzeba całych dnia;
Jutro i sobotę, bo się czas nie dopisze,
A za to wy dostanieście trzy dni wolnego».
```


## RLVR: six-word English microfiction — Qwen3.5-4B

Actual first-attempt greedy outputs. **Before:** original Qwen/Qwen3.5-4B, revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`. **After:** the same model plus a fresh LoRA trained with programmatic rewards on synthetic six-word prompts. No workshop SFT, Pan Tadeusz/film data, teacher answers, or best-of-N output selection.

Saved adapter: 120 distinct training prompts, 480 self-sampled completions, 60 RLVR updates; selected on development prompts only. The full exploration run took 603.6 seconds. Held-out strict compliance **1/32 → 32/32**. The checker does not establish literary quality; some responses are formulaic or awkward. [Every output](RLVR_RESULTS.html).

### six_words-test-029

Write a tiny story in exactly SIX English words. Include the exact words "glacier" and "mermaid". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

**Before — original Qwen3.5-4B (5 words, checker success: False)**

```text
The mermaid kissed the glacier.
```

**After — Qwen3.5-4B + six-word RLVR (6 words, checker success: True)**

```text
Glacier melted to reveal a mermaid.
```

### six_words-test-010

Write a tiny story in exactly SIX English words. Include the exact words "astronaut" and "birthday". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

**Before — original Qwen3.5-4B (4 words, checker success: False)**

```text
Astronaut blew birthday candles.
```

**After — Qwen3.5-4B + six-word RLVR (6 words, checker success: True)**

```text
Astronaut blew birthday candles in space.
```

### six_words-test-003

Write a tiny story in exactly SIX English words. Include the exact words "mouse" and "vampire". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

**Before — original Qwen3.5-4B (5 words, checker success: False)**

```text
The mouse bit the vampire.
```

**After — Qwen3.5-4B + six-word RLVR (6 words, checker success: True)**

```text
Mouse fed vampire with tiny cheese.
```


## LLM robi prawko — real multiple-choice exam pilot

Model before: **Qwen/Qwen3.5-0.8B**, revision `2fc06364715b967f1860aea9cf38778875588b17`, no workshop fine-tuning. After: **the same base plus a fresh SFT adapter** or **the same base plus a fresh RLVR adapter**, each trained on100 official category-B text-only driving questions from the July2026 catalogue. No film/poetry data. Actual constrained A/B/C choices, not generated explanations.

Held-out question7445: **Której z tych czynności nie masz prawa wykonywać samochodem osobowym?**

- A. Ciągnąć przyczepy lekkiej.
- B. Holować innego samochodu osobowego na obszarze zabudowanym.
- C. Ciągnąć dzieci na sankach.

Original model: **A** (wrong). SFT adapter: **C** (correct). RLVR adapter: **C** (correct). Official keyC.

Both methods also regressed on question7454 (which road prohibits towing): original **A, Na autostradzie** was correct; both adapters selected **C, W strefie zamieszkania**, incorrectly.

Both improved the40-question held-out subset **21/40→27/40**. [All actual choices and regressions](prawko_example_results.md), [method and measured costs](PRAWKO.md). This subset is not the full official driving exam.


### Prawko after four times the training budget

Still **Qwen3.5-0.8B**, separate fresh **SFT/RLVR adapters trained on the same100 official questions**. Original base:21/40. At the final12-minute checkpoints: SFT28/40, RLVR25/40; reordered choices:30/40 vs24/40. With development-selected checkpoints: SFT28/40, RLVR29/40; reordered25/40 vs28/40. The choice of checkpoint changes which method leads.

An actual disagreement between the **development-selected** adapters:

> Prędkość bezpieczna to prędkość:
>
> A. która zapewnia panowanie nad pojazdem.
> B. która jest równa dopuszczalnej prędkości na danym odcinku drogi.
> C. którą „podpowiada” nawigacja w Twoim pojeździe.

Qwen3.5-0.8B original: **A**, correct. Qwen3.5-0.8B + SFT on100 official questions: **A**, correct. Qwen3.5-0.8B + RLVR on100 official questions: **B**, wrong. This example is a regression for RLVR, not newly learned knowledge for SFT. Option text is from the official catalogue (typography normalized here); model outputs are only letters.

[All long-run comparisons, including cases favoring RLVR](prawko_long_results.md) · [Interactive curves and disagreement filter](PRAWKO_TRAINING.html).
