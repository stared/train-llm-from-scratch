# Supplied film dialogue: measured results

## Qwen3.5-4B fine-tuned on the supplied chlopaki.md: ordinary Polish Q&A

**Model for every answer in this section: `Qwen/Qwen3.5-4B`, revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`. Before: original instruction checkpoint, no workshop fine-tuning. After: LoRA fine-tuned only on [datasets/chlopaki.md](../datasets/chlopaki.md), converted to [1,270 adjacent dialogue pairs, both directions](../datasets/chlopaki-bidirectional-v1/train.jsonl). No earlier assistant-authored comic data included.**

All 1,270 examples were seen once, across two segments with a fresh optimizer for the second: 318 updates, **10 min 51.5 s training**, one L4. Successful training calls cost an estimated **$0.2343**; both sampling comparisons add **$0.0452**. These are timed requested-compute estimates, excluding the failed initial OOM attempt and startup/storage, not an invoice total.

The two sampled variants use temperature 0.7, top-p 0.8, top-k 20, repetition penalty 1.1, seed 42 and a 192-new-token cap. The 25% variant uses the same saved adapter with its LoRA contribution multiplied by 0.25 at inference; no retraining. Full baseline answers can end at the token cap. All six questions are new ordinary questions, not film-quotation continuations; all usable film pairs are in training, so there is no held-out quotation test.

The full-strength sampled adapter makes the shift to absurd dialogue immediately visible. “Zamieniam się w kaczki!” can be a successful comic response for this workshop. Judge humor, relevance and language separately: absurdity alone is not a failure, and brevity alone is not success. The 25% adapter generally restores explanatory assistant behavior and loses much of the comic transformation in these six probes. Keep full strength plus sampling as the main creative demonstration, with greedy and 25% strength as comparisons.

[Interactive comparison: all 54 saved answers](chlopaki-results.html) · [Experiment notebook](../LAB_NOTEBOOK.md) · [Runnable recipe](../docs/notes/chlopaki.md)

### 1. Dlaczego mój komputer znowu się zawiesił?

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

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 25% adapter (sampled):**

> Mam wrażenie, że ten problem występuje częściej niż powinien. Może warto sprawdzić, czy nie ma jakieś oprogramowanie, które powoduje takie sytuacje?

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (greedy):**

> Nie wiem.

### 2. Kolega pożyczył ode mnie pieniądze i nie oddaje. Co mu powiedzieć?

**Before — Qwen3.5-4B, no workshop fine-tuning (sampled):**

> To trudna sytuacja, która może być bolesna dla obu stron, ale pamiętaj: **kwestia finansowa to kwestia finansowa**. Nawet jeśli jesteś bliskim kolegą, brak spłaty długów często rodzi napięcia, które są trudniejsze do naprawienia niż sama kwota pieniędzy.
> 
> Oto kilka strategii i konkretnych przykładów tego, co możesz powiedzieć, w zależności od Twojego poziomu zaufania i relacji z osobą:
> 
> ### 1. Zanim zadzwonisz – przygotuj się mentalnie
> *   **Wybierz odpowiedni moment:** Nie rozmawiaj, gdy kolega jest zmęczony, stresowany lub w pracy. Poproś o telefon na spokojną chwilę wieczorem.
> *   **Bądź konkretny:** Miej pod ręką dokładną kwotę i termin, który oczekujesz (np. „pot

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (sampled):**

> Mam dla niego jedną radę: jeśli on jest w stanie go posiąść, to ty też jesteś w stanie go posiąść.

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 25% adapter (sampled):**

> To trudna sytuacja, ale kluczowe jest, aby zachować spokój i nie ulegać emocjom. Oto kilka kroków, które możesz podjąć:
> 
> 1. **Powiedz to wprost**: Nie czekaj na kolejną okazję. Zapytaj go o datę spłaty. Możesz użyć zdania: „Przyszedłem do Ciebie z pytaniem o pieniądze. Kiedy je oddasz?"
> 2. **Zapamiętaj daty**: Jeśli nie otrzymałeś odpowiedzi, zapisz sobie datę, kiedy miałeś otrzymać pieniądze. To ważne dla dalszej komunikacji.
> 3. **Nie udawaj ignorowania**: Jeśli nie odpisuje lub nie dzwoni, nie ignoruj go. Kontynuuj kontakt i przypominaj o dacie spłaty.
> 4. **Sprawdź jego sytuację finansową**: Może on ma problemy z pieniędz

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (greedy):**

> A co?

### 3. Nie wiem, co chcę robić w życiu. Od czego zacząć?

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

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 25% adapter (sampled):**

> To całkowicie normalne uczucie, zwłaszcza jeśli dotychczas nie miałeś wyraźnej ścieżki kariery lub pasji. Większość ludzi przechodzi przez fazę „nie wiem, co chcę robić" w wieku 20-30 lat. To czas eksperymentowania i odkrywania siebie.
> 
> Oto kilka konkretnych kroków, które możesz podjąć, aby znaleźć kierunek:
> 
> ### 1. Zrób się samemu (refleksja)
> Zanim zaczniesz szukać pracy czy studiów, zastanów się nad tym, co już znasz:
> *   **Co sprawia Ci radość?** Jakie czynności robisz z przyjemnością, nawet bez płacenia za nie? (np. naprawianie rzeczy, pisanie, rozmawianie z ludźmi, organizowanie imprez).
> *   **W czym jesteś dobry?**

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (greedy):**

> To jest chyba najtrudniejsze pytanie, jakie można sobie zadać.

### 4. Szef chce, żebym pracował w sobotę. Jak mu odmówić?

**Before — Qwen3.5-4B, no workshop fine-tuning (sampled):**

> Odmowa szefowi pracy w sobotę to sytuacja wymagająca balansu między lojalnością a własnym czasem osobistym. Kluczem jest **profesjonalizm**: nie należy obrażać pracodawcy ani brzmieć jakbyś nie chciał pracować, ale też nie wolno akceptować nadgodzin bez dyskusji o wynagrodzeniu lub zamianie na czas wolny.
> 
> Oto kilka sprawdzonych strategii i gotowych wzorów odpowiedzi, które możesz wykorzystać:
> 
> ### 1. Złota zasada: Proponuj zamiast odmawiać
> Zamiast mówić "nie mogę", powiedz "mogę, ale tylko wtedy, gdy..." lub zaproponuj alternatywę. To pokazuje, że zależy Ci na realizacji zadań, a nie na samym obecieniu w biurze.
> 
> *   **Przykład:** "Są

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (sampled):**

> W piątek nie masz żadnej wizyty?

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 25% adapter (sampled):**

> To zależy od tego, jak bardzo chcesz pracować i jakie masz relacje z szefem. Jeśli nie możesz pracować w sobotę, masz kilka opcji:
> 
> 1. **Prośba o przesunięcie**: Możesz poprosić szefa o zmianę terminu pracy na inny dzień tygodnia.
> 2. **Odmowa z wyjaśnieniem**: Możesz odmówić, podając konkretny powód (np. inne zobowiązania, zdrowie).
> 3. **Zaproszenie do negocjacji**: Możesz zaproponować współpracę nad tym tematem w przyszłości.
> 
> Jeśli jednak jesteś gotowy do pracy w sobotę, warto to uzgodnić wcześniej i mieć jasne zasady dotyczące wynagrodzenia lub dodatkowych dni wolnych.
> 
> Czy chcesz, abym pomógł Ci sformułować odpowiednią wiadomość do szefa?

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (greedy):**

> Nie wiem, czy to będzie możliwe.

### 5. Kupiłem drogi sweter, a wszyscy się ze mnie śmieją. Co robić?

**Before — Qwen3.5-4B, no workshop fine-tuning (sampled):**

> To całkowicie normalna reakcja na sytuację, w której ktoś wydaje się „drogi". Ceny odzwierciedlają nie tylko jakość materiału czy wykończenie, ale też **znaczenie**, które ten przedmiot ma dla właściciela.
> 
> Oto kilka perspektyw i kroków, które możesz podjąć:
> 
> ### 1. Zrozum psychologię innych ludzi
> Większość osób nie myśli o tym, ile kosztuje dany przedmiot (chyba że mają bardzo niski budżet). Myślą one o tym, jak to wygląda. Jeśli sweter jest drogi, może być po prostu **niewygodny** – np. zbyt gruby, niewygodny do noszenia, z dziwnym wzorem lub brakiem stylu. Wtedy ludzie się śmieją nie za to, co kupiłeś, ale za to, że **nie

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (sampled):**

> Zamieniam się w żubrówkę.

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 25% adapter (sampled):**

> Cieszę się, że kupiłeś taki fajny sweter! Nie musisz się tym przejmować – to po prostu twoja stylowa decyzja! 🧥😄

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (greedy):**

> Aha.

### 6. Dlaczego warto robić kopie zapasowe?

**Before — Qwen3.5-4B, no workshop fine-tuning (sampled):**

> Rozpoczynanie kopii zapasowych danych to jedno z najważniejszych działań w cyfrowym zarządzaniu, często porównywane do ubezpieczenia majątku. Warto o nich myśleć nie jako o zadaniu technicznym, ale jako o **strategii ochrony przed katastrofą**.
> 
> Oto kluczowe powody, dla których kopiowanie zapasów jest niezbędne:
> 
> ### 1. Ochrona przed awariami sprzętowymi i błędami użytkownika
> To najczęstsze przyczyny utraty danych. Nawet najbardziej niezawodne dyski twardze mogą pęknąć, a oprogramowanie może zawieść.
> *   **Błędy operacyjne:** Usunięcie pliku przez pomyłkę, błędna konfiguracja systemu lub uszkodzenie plików podczas zapisu (np. nagłe wyłączenie komputera).
> *   **

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (sampled):**

> Aha. To ciekawe pytanie... Wiesz, kiedy po raz pierwszy zrobiłem kopię zapasową tego komputera, to wylansowała się na ekranie moja synuśka... Nie wiem czy to było moje dzieło... Ale bardzo mi się podoba! ...

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 25% adapter (sampled):**

> Kopie zapasowe to absolutny fundament bezpieczeństwa danych w cyfrowym świecie. Warto je robić z kilku kluczowych powodów, które dotyczą zarówno prywatności, jak i finansów:
> 
> 1.  **Ochrona przed awariami sprzętu** – Twardy dysk może ulec awarii, baterii laptopa może się rozpuścić, a pamięć RAM przestać działać. Bez kopii zapasowej utrata danych byłaby nieodwracalna.
> 2.  **Zabezpieczenie przed kradzieżą lub uszkodzeniem** – Jeśli ktoś ukradnie Twoje urządzenie (np. tablet czy telefon), a na nim są zdjęcia, dokumenty czy pliki bankowe, bez kopii zapasowej wszystko będzie stracone.
> 3.  **Wirusy i ataki hakerskie** – Złośliwe oprogramowanie często niszczy dane

**After — Qwen3.5-4B fine-tuned on chlopaki.md, 100% adapter (greedy):**

> Wydaje mi się, że to jest proste.

### Raw records

- [style-train-wit-1788781334049902996](../runs/style-train-wit-1788781334049902996/execution.json)
- [style-sample-wit-1788781457274497722](../runs/style-sample-wit-1788781457274497722/execution.json)
- [style-sample-wit-1788781648674828805](../runs/style-sample-wit-1788781648674828805/execution.json)

## Non-question messages: does it always say “Zamieniam się w…”?

**Model: Qwen/Qwen3.5-4B, revision 851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a, LoRA fine-tuned only on supplied `datasets/chlopaki.md` (all 1,270 bidirectional pairs), 100% adapter strength, no style prompt.** No additional training.

No: the phrase appeared in **1/16 non-question responses** (eight prompts × two seeds) and **1/8 question responses** (four prompts × two seeds). This small diagnostic disproves “always”; it does not establish population frequencies or a causal question/statement effect. Other responses include brief dialogue, jokes and incoherent passages.

Temperature .7, top-p .8, top-k 20, repetition penalty 1.1, 96-new-token cap, seeds 42 and 123, batches of four. Sampling RNG advances across batches: changing prompt order/batch composition can change an answer even with seed 42. These are new samples, not attempts to reproduce earlier answers exactly.

**Input (statement):** Cześć, właśnie wróciłem z pracy.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> No cześć!

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Aha...

**Input (statement):** Dzisiaj wszystko idzie nie tak.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Mam dla ciebie dwie wiadomości.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> A co?

**Input (statement):** Nie wiem, co chcę robić w życiu.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Zamieniam się w kaczki!

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Dlaczego?

**Input (statement):** Kupiłem drogi sweter, a wszyscy się ze mnie śmieją.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Wydaje mi się, że nie ma w tym żadnej dziwności.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Wiesz co? Nie wiem czy ci to pomoże, ale kup sobie nowy sweter.

**Input (statement):** Mój komputer znowu się zawiesił.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Przestań mówić o tym, że się zawieszam!

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Ktoś mu coś wlał?

**Input (statement):** Mam dla ciebie dobrą wiadomość.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Aha?

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Wiem, że to brzmi jak szmal, ale nie ma nic bardziej naturalnego niż kupować sobie tę fajność za pieniądze.

**Input (statement):** Dobra, jedziemy. Samochód już czeka.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Będziesz miał do czynienia z ludźmi, którzy mają duży kieszonkowy budżet. Będziesz musiał im się z nimi zaopracować i to bez żadnej agresji fizycznej. Właściwie nie wiem czy na przykładę masz takiego chłopaka jak on, który jest w stanie zapalić się po słówku o jego szmalu.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Cześć!

**Input (statement):** Stary, chyba trochę przesadziłeś.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> To co?

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Wiesz co? Nie wiesz co? W ogóle nie wiem co mówię!

**Input (question):** Nie wiem, co chcę robić w życiu. Od czego zacząć?

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Aha.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Dobra! To jest moja rada: zacznij od tego, co już potrafisz robić najlepiej.

**Input (question):** Kupiłem drogi sweter, a wszyscy się ze mnie śmieją. Co robić?

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Przepraszam...

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Co z tego, że ci się śmieją? Nie masz ich!

**Input (question):** Dlaczego mój komputer znowu się zawiesił?

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Zamieniam się w grilla.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> O co chodzi?

**Input (question):** Co robimy wieczorem?

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 42:**

> Widzisz tego psa? Ma taki pysk, jakby chciał nas wszystkich zabić.

**Fine-tuned Qwen3.5-4B on chlopaki.md, seed 123:**

> Wszystko jest w porządku.

[Raw record](../runs/dialogue-probe-1788793342343057211/probe.json). Timed remote execution: 59.76 s; estimated successful-call compute $0.01696, excluding failed startup and storage.
