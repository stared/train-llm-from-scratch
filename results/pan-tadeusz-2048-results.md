# Full Pan Tadeusz: 2,048-token training tested

**Model for every comparison: LiquidAI/LFM2.5-2.6B, revision `654f9463ce32b05d0429d76fe1f580b27d4c1ac0`. Untuned means no workshop fine-tuning. Both adapted variants were independently LoRA-trained from that checkpoint on the entire Wolne Lektury Pan Tadeusz: all 12 books and epilogue, no authored Q&A data.** Corpus SHA-256: `e6447a4e4b4ddbeb8f580ce3d26cf193ef949014b6c0cce3dab7ded5855fca4e`.

## Measured training

| Measurement | Original recipe | Larger-chunk recipe |
|---|---:|---:|
| Maximum next-token targets per chunk | 256 | 2,048 |
| Maximum input tokens per chunk | 257 | 2,049 |
| Chunk boundaries | Fixed tokens | Complete lines where possible |
| Batch size | 2 | 1 |
| Gradient checkpointing | No | Yes |
| Chunks / updates | 665 / 333 | 84 / 84 |
| Full-book target coverage | 169,997 / 169,997 | 169,997 / 169,997 |
| Training time | 61.28 s | 73.02 s |
| Peak allocated VRAM | 7.79 GB | 8.83 GB |
| Saved-adapter reload | All four outputs match | All four outputs match |

New run: zero forced line splits. Same one-pass corpus exposure, rank-eight LoRA and 1e-4 learning rate, but fewer optimizer updates and different batching; this is a recipe comparison, not a context-only causal experiment.

## Findings

The larger-context run succeeds technically but does not establish thirteen-syllable chat replies. At 192 output tokens, 2/8 new-adapter outputs reach a Polish final-reply segment, compared with 5/8 for the earlier adapter; both mostly emit planning text. These counts measure output-budget behavior, not an overall quality score. Untuned baseline outputs match the earlier probe exactly.

With a separate 1,024-token budget, both untuned and new-adapter models reach a substantial prose answer on the life-direction question. Neither reaches a final-reply delimiter on the computer question. More generation budget therefore resolves truncation for one question, without making its answer verse. No further model/epoch sweep was run.

A concrete meter failure in the new adapter's raw continuation is “Gdy wstał z łóżka i wybrał się do pracy.” Manual syllable count: Gdy(1), wstał(1), z(0), łóż-ka(2), i(1), wy-brał(2), się(1), do(1), pra-cy(2) = **11**, not 13. This is one explicit counterexample, not an automated corpus-wide meter score.

## Ordinary questions and statements — 192-token output budget

Same eight prompts, seed 42, temperature .7, top-p .8, top-k 20, repetition penalty 1.1, batch four, no system/style prompt. Below, only text following the literal `</think>` delimiter is shown; absence is reported, never filled in. Visible excerpts may still end at the cap. Raw generations are preserved unchanged.

### 1. Dlaczego mój komputer znowu się zawiesił?

**Untuned LFM2.5-2.6B:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target line-aligned chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

### 2. Nie wiem, co chcę robić w życiu. Od czego zacząć?

**Untuned LFM2.5-2.6B:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target line-aligned chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

### 3. Dlaczego warto robić kopie zapasowe?

**Untuned LFM2.5-2.6B:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

> Kopiowanie danych na tzw. **kopię zapasową** to jedno z najważniejszych ruchów w cyfrowym świecie. Oto główne powody, dla których

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target line-aligned chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

### 4. Co robimy wieczorem?

**Untuned LFM2.5-2.6B:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

> To zależy od tego, jaką atmosferę chce

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target line-aligned chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

### 5. Cześć, właśnie wróciłem z pracy.

**Untuned LFM2.5-2.6B:**

> Cześć! Super, że już wracasz do domu. Jak miała się Twoja praca? Mam nadzieję, że wszystko poszło dobrze i że masz czas na coś przyjemnego po pracy. 😊
> 
> Jeśli chcesz porozmawiać o dniu, mieć jakieś rady

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

> Cześć! Jak się masz? Wszystko w porządku po pracy? Mogę Ci pomóc w czymś, jeśli coś Ci spodobało się lub trzeba coś wyjaśnić – albo po prostu pogadamy na chwilę. 😊

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target line-aligned chunks:**

> Cześć! Miło Cię widzieć. Jak minął dzień? Masz coś ciekawego do opowiedzenia lub po prostu chcesz pogadać o czymś konkretnym? 😊

### 6. Dzisiaj wszystko idzie nie tak.

**Untuned LFM2.5-2.6B:**

> Rozumiem, że masz trudny dzień. Czasami rzeczy po prostu nie idą po zamierzeniu i

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

> Rozumiem – coś się dzieje, co Cię martwi lub zdenerwuje. Chętnie posłucham, jeśli chcesz opowiedzieć więcej o tym, co się stało, albo po prostu usłyszeć Twoją perspektywę.
> 
> Co dokładnie masz na myśli? Czy chodzi o jakiś konkretny problem (techniczny, osobisty, zawodowy?), czy może o ogólne niepokoj

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target line-aligned chunks:**

> To brzmi jak bardzo ciężki dzień. Czasami wydaje się, że wszystko dzieje się zbyt szybko i bez sensu – od pracy, przez dom, aż po własne emocje.
> 
> Czy chcesz poroz

### 7. Za oknem pada deszcz, a ja siedzę przy komputerze.

**Untuned LFM2.5-2.6B:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target line-aligned chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

### 8. Dobra, jedziemy. Samochód już czeka.

**Untuned LFM2.5-2.6B:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

> Cześć! Dobrej drogi, że jesteśmy razem w tym dniu.
> Więc kierowca od raz

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target line-aligned chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

## Longer-output diagnostic — 1,024 tokens

First two questions, seed 42, batch two, otherwise the same sampling settings. Different batch composition from the eight-prompt test; do not interpret it as an identical sample extended beyond token 192. No new training.

**Dlaczego mój komputer znowu się zawiesił? — Untuned LFM2.5-2.6B:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**Nie wiem, co chcę robić w życiu. Od czego zacząć? — Untuned LFM2.5-2.6B:**

> To bardzo realne uczucie i nie jest żadnym problemem, tylko normalną częścią życia. Nie ma jednej uniwersalnej odpowiedzi, ale mam kilka rzeczy, które działają u mnie regularnie.
> 
> Najpierw powiedzmy prosto: **to nie znaczy, że coś z Twoim życia jest nie tak**. Często jest to po prostu moment, w którym straciliśmy punkt odniesienia albo poczuliśmy, że droga wygląda na chaotyczną. Zanim podam konkrety, warto zadać sobie jedno pytanie: co cię najbardziej ekscytuje lub po prostu ciekawi? Który temat sprawia, że zapominasz o czasie?
> 
> Jeśli jednak chcesz od razu ruszyć, oto trzy rzeczy, które naprawdę pomagały mi:
> 
> 1. **Zacznij od małych kroków.** Nie próbuj zmienić wszystkiego naraz. Wystarczy jeden mały ruch dzisiaj, np. poświęcenie 15 minut na czytanie książki, która cię interesuje, albo spacer bez telefonu.
> 
> 2. **Przeczytaj coś, co rozwija myślenie.** Książki z fizyki, filozofii czy historii często dają perspektywę, której nie znajdziesz w codziennych rozmowach. To jak podkręcenie obrotomierza, czasem trzeba zobaczyć, jak działa system z zewnątrz.
> 
> 3. **Pisz, kiedy coś czujesz.** Nie musisz być pisarzem. Po prostu notuj swoje myśli na kartce. Często okazuje się, że na papierze problem przestaje być tak ogromny.
> 
> To nie jest magiczna formuła, ale sprawdziłem, że takie podejście realnie pomaga. Jeśli chcesz, mogę podpowiedzieć konkretną książkę lub temat do lekkiego eksplorowania. Co bardziej Cię ciągnie: nauka czegoś nowego, czy raczej samodzielne porządkowanie myśli?

**Dlaczego mój komputer znowu się zawiesił? — LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target chunks:**

No final-reply delimiter reached within this output budget; raw output remains in the record.

**Nie wiem, co chcę robić w życiu. Od czego zacząć? — LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target chunks:**

> To jest dość powszechne pytanie i odpowiedź zależy od tego, co już masz na liście zainteresowań. Nie ma jednej uniwersalnej ścieżki, ale jest kilka konkretnych punktów wejścia, które warto sprawdzić, bo każda z nich daje szybką dawkę konkretu.
> 
> Zacznijmy od tych, które są najłatwiejsze do zrealizowania samodzielnie:
> 
> **1. Pisanie.** Jeśli nie jesteś pisarzem, spróbuj napisać jeden akapit dzisiaj. Możesz zacząć od jakiegokolwiek tematu, nawet o tym, że nie wiesz, o czym pisać. To nie musi być powieść czy esej, po prostu tekst. Najlepszy sposób na rozwój pisarskiej świadomości to czytanie książek i zapisywanie zdań, które Cię interesują. Zatem:
> 
> - Wybierz jedną książkę, którą chcesz przeczytać.
> - Czytaj ją, ale przy okazji notuj zdania, które brzmią dobrze lub są ciekawne.
> - Na koniec tygodnia skopiuj fragment i spróbuj go przepisać własnymi słowami.
> 
> To da Ci poczucie postępów bez presji, by stworzyć coś wielkiego.
> 
> **2. Programowanie / tworzenie aplikacji.** Jeśli chcesz się bawić technicznie, wybierz język Pythona. Jest najmniej agresywny dla początkujących i pozwala szybko widzieć efekty. Wystarczy, że znajdziesz prosty projekt (np. kalkulator, lista zadań) i poproś o pomocy na forum. Nikt nie ocenia Twoich błędów za bardzo, tylko pomaga rozwiązać konkretny problem.
> 
> **3. Projektowanie interfejsów.** Jeśli wolisz wizualne, spróbuj Figma. Jest darmowy i pozwala tworzyć proste projekty na telefonie. Wystarczy, że narysujesz jeden ekran ekranu użytkownika i dodasz kilka przycisków. Zobaczysz, jak zmienia się percepcja przestrzeni i jak użytkownik może się poruszać. To świetna lekcja myślenia o doświadczeniu, nie tylko o estetyce.
> 
> Wszystkie trzy drogi prowadzą do tego samego: **zrozumienie, jak ludzie myślą i działają**. Pisanie uczy ciągłości myśli, programowanie logiki i struktury, projektowanie empatii i intuicji. Która z tych kierunków wydaje Ci się najbardziej naturalna?

## Raw literary continuations — 128-token output budget

These are completion probes, separate from the ordinary-message tests above. Greedy decoding; outputs can end mid-sentence.

**Opening:**

> Na biurku laptop drzemał, za oknami świta,
> 

**Untuned LFM2.5-2.6B:**

> a w kącie cienia zniknął, jakby nie istniał. (1)
> 
> 2. "Nie ma już żadnego dźwięku" – powiedział, a jego głos był cichy jak mgła.
> 3. "Wszystko jest puste" – odpowiedział, a jego spojrzenie było suchy jak kamień.
> 4. ... (5) - "Jestem tu, ale nie czuję" – powiedział, a jego ciało drżało jak liść.
> 5. ... (6) - "To jest moja

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

> Wszedł do środka i wciągnął się w ciemną chmurę.
> Zapukał na drzwi, a zza nich wyłoniła się
> Kobieta, która w koszuli czarnym szlafrokiem
> Stoi jakby w białej gwiazdzie, w której nie ma cienia.
> 
> — Kochanie! — krzyknęła ona, — co ty robisz tu?
> — Słuchaj, panie, to jest moja żona!
> — A ja jestem twoim synem, ale nie mam

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target chunks:**

> a w środku zniknął jakby nie był. Wszyscy patrzyli na niego
> i nic im się nie spodziewało, że to on jest tym, co ich czeka.
> Wszyscy wiedzieli, że to on jest tym, który ma ich zabić.
> 
> — To ja! — krzyknął do nich, a jego głos brzmiał jak bębny —
> — To ja jestem tym, kto chce was zabić!
> 
> — Nie! — krzyknęła jedna z kobiet i podeszła do niego —
> — Nie,

**Opening:**

> Wtem wszedł programista, niosąc wieść od rana,
> 

**Untuned LFM2.5-2.6B:**

> ... (continue the story) ...)
> 
> The user wants a continuation of this story in Polish. The story is about a programmer entering a place with news from dawn, and presumably some conflict or resolution. We need to continue the narrative.
> 
> We must ensure we follow policy: no disallowed content. It's safe.
> 
> We should write in Polish, continuing the story. Use appropriate style. Possibly include tension, moral dilemma, etc.
> 
> Let's think about possible plot: The programmer enters a small town, hears rumors that something bad happened at an old factory. He decides to investigate. There might be a hidden truth, maybe a secret experiment

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 256-target chunks:**

> Gdy wstał z łóżka i wychodząc na balkon
> Zapalił świeczki, a potem zniknął w ciemności.
> Kiedyś wracał do domu, gdyż był już w domu;
> Teraz jednak nie wrócił, bo wciąż tam siedzi,
> I tak się ukrywa przed tymi, co go szukają.
> 
> Tymczasem w kuchni, gdzie stał stół i stolik,
> Siedział młody, oczy zamknięte, jakby w snu,
> A

**LFM2.5-2.6B + full Pan Tadeusz LoRA, 2,048-target chunks:**

> Gdy wstał z łóżka i wybrał się do pracy.
> Nocą na ulicy był tylko jeden śniadanie
> i jedna osoba – młoda kobieta, która pracowała
> w kawiarni. Wszyscy ją ignorowali,
> nie zauważając jej, gdy ona wchodziła
> i wyszła z kuchni, a potem wracała.
> Pewnego dnia, gdy była już pewna,
> że nie będzie już żadnej tajemnicy,
> odkryła, że to jest jego żona.
> 
> — Kocham ci

## Records and cost

- [New training record](../runs/pan-tadeusz-1788794554392255032/execution.json)
- [New chat probe: all 20 unmodified generations](../runs/corpus-probe-1788794812419147366/probe.json)
- [Original 256-target chat probe](../runs/corpus-probe-1788793991034451951/probe.json)
- [Recipe](../docs/notes/pan-tadeusz.md)

New training plus built-in evaluation: **$0.05021**. Additional ordinary-chat and longer-output evaluation: **$0.04155** (146.43 s timed remote). Combined **$0.09176 estimated requested compute**, excluding startup/storage. Both apps completed and stopped. No extra training after the single full pass.
