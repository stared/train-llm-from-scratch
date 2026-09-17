# LLM robi prawko — actual results

Official July 2026 Polish driving-question catalogue; category B, text-only A/B/C subset.
All outputs below are constrained next-token A/B/C selections, not generated explanations.
Correct answer text comes from the official catalogue. The model outputs only the selected letter.
This is a 40-question held-out subset, not the complete official examination.

| Model / training | Train before → after | Test before → after | Rotated test before → after | Training time | Worker estimate |
|---|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B + SFT on 100 official questions | 53/100 → 91/100 | 21/40 → 27/40 | 20/40 → 26/40 | 168.2s | $0.0565 |
| Qwen/Qwen3.5-0.8B + RLVR on 100 official questions | 53/100 → 80/100 | 21/40 → 27/40 | 20/40 → 25/40 | 181.1s | $0.0552 |

## Qwen/Qwen3.5-0.8B + SFT on 100 official questions

Run: `prawko-sft-1788860580008838148`. Base revision: `2fc06364715b967f1860aea9cf38778875588b17`.
Development-selected epoch 3; 75 selected updates of 250 explored updates. Reload matches: True.
Before = original pretrained/instruction model, no workshop adapter. After = fresh adapter trained only on the 100 training questions; no Pan Tadeusz or film training.

### test: 15 corrections, 9 regressions

**Question 10840: W jaki sposób przewozisz dziecko o wzroście mniejszym niż 150 cm na przednim siedzeniu samochodu osobowego, który ma pięć miejsc siedzących?**

- A.  Na kolanach pasażera.
- B.  W foteliku bezpieczeństwa lub innym urządzeniu przytrzymującym dziecko.
- C. W foteliku bezpieczeństwa tyłem do kierunku jazdy, jeżeli pojazd ma aktywną poduszkę powietrzną dla pasażera.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 10869: W jaki sposób przewozisz dziecko o wzroście mniejszym niż 150 cm samochodem osobowym, w którym jest pięć miejsc siedzących?**

- A. Na przednim siedzeniu bez fotelika lub innego urządzenia przytrzymującego dziecko.
- B. Na przednim siedzeniu w innym niż fotelik urządzeniu przytrzymującym dziecko.
- C. Na tylnym siedzeniu bez zapiętych pasów bezpieczeństwa.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 11001: Który z wymienionych dokumentów kierujący pojazdem zarejestrowanym na terytorium RP musi mieć przy sobie i okazywać na żądanie uprawnionego organu?**

- A. Potwierdzenie opłacenia obowiązkowego ubezpieczenia odpowiedzialności cywilnej właściciela pojazdu.
- B. Dowód rejestracyjny.
- C. Jeśli kierujący ma uprawnienia do kierowania ograniczone do pojazdu wyposażonego w blokadę alkoholową - zaświadczenie o pozytywnym wyniku badania technicznego w tym zakresie.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10931: Ile czasu jest ważne pokwitowanie zatrzymania przez policjanta prawa jazdy za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w dowodzie rejestracyjnym samochodu osobowego?**

- A. 12 godzin.
- B. 24 godziny.
- C. 72 godziny.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 10898: Za które naruszenie przepisów ruchu drogowego policjant zatrzyma prawo jazdy?**

- A. Za wyprzedzanie z naruszeniem pojedynczej linii ciągłej.
- B. Za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w dowodzie rejestracyjnym samochodu osobowego.
- C. Za wymijanie na przejeździe kolejowym.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 10899: Za które naruszenie przepisów ruchu drogowego policjant zatrzyma prawo jazdy?**

- A. Za wyprzedzanie przed przejściem dla pieszych, gdzie ruch jest kierowany.
- B. Za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w pozwoleniu czasowym samochodu osobowego.
- C. Za wymijanie na przejeździe dla rowerzystów.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 4562: Kto podlega odpowiedzialności karnej w przypadku nieudzielenia pomocy poszkodowanemu w wypadku drogowym z bezpośrednim zagrożeniu utraty zdrowia i życia?**

- A. Każda osoba, która mogła udzielić pomocy bez narażenia siebie lub innej osoby na niebezpieczeństwo utraty życia lub ciężkiego uszczerbku zdrowia.
- B. Tylko lekarz.
- C. Tylko uczestnik wypadku drogowego.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 6442: Do czego służą światła pozycyjne pojazdu?**

- A. Do oświetlania drogi.
- B. Do określania pozycji pojazdu.
- C. Do sygnalizowania zmiany pasa ruchu.

Original Qwen/Qwen3.5-0.8B: **B** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 7445: Której z tych czynności nie masz prawa wykonywać samochodem osobowym?**

- A. Ciągnąć przyczepy lekkiej.
- B. Holować innego samochodu osobowego na obszarze zabudowanym.
- C. Ciągnąć dzieci na sankach.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 7454: Na której z tych dróg nie masz prawa holować samochodem osobowym innego pojazdu?**

- A. Na autostradzie.
- B. Na drodze ekspresowej.
- C. W strefie zamieszkania.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 6463: Jadąc zimą spotykasz na poboczu sinego, półprzytomnego, wyziębionego człowieka. Jak należy mu pomóc?**

- A. Podać mu gorący napój.
- B. Podać mu alkohol.
- C. Wezwać zespół ratownictwa medycznego, zabrać go do samochodu, okryć i powoli ogrzewać.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10829: Dokumentem stwierdzającym dopuszczenie pojazdu samochodowego do ruchu jest:**

- A. dowód rejestracyjny.
- B. karta pojazdu.
- C. nalepka kontrolna na przedniej szybie.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✗. Official key: **A**.

**Question 10815: Foteliki bezpieczeństwa dla dzieci oraz inne urządzenia przytrzymujące dla dzieci należy instalować w pojeździe:**

- A. w sposób bezpieczny i estetyczny.
- B. w sposób umożliwiający łatwy dostęp do dziecka.
- C. zgodnie z zaleceniami producenta urządzenia.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 3573: Jesteś świadkiem potrącenia pieszego. Jak powinieneś się zachować?**

- A. Nie podejmować działań, gdyż pomocy musi udzielić sprawca wypadku.
- B. Wezwać pomoc drogową.
- C. Zatrzymać się, wezwać pomoć medyczną i udzielić pierwszej pomocy poszkodowanemu.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 7515: Czy wolno Ci kierować pojazdem, którego tablica rejestracyjna jest niewidoczna?**

- A. Tak, bez żadnych ograniczeń.
- B. Tak, gdy tablica jest przesłonięta przez wystający ładunek.
- C. Nie, jest to zabronione.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 9035: Jaki wpływ na pole widzenia kierującego pojazdem ma prędkość jazdy?**

- A. Wraz ze wzrostem prędkości zawęża się pole widzenia.
- B. Wraz ze wzrostem prędkości rozszerza się pole widzenia.
- C. Prędkość jazdy nie ma wpływu na pole widzenia kierującego.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 10081: Czy dopuszczalne jest holowanie za pomocą połączenia sztywnego pojazdu o niesprawnym układzie kierowniczym?**

- A. Nie.
- B. Tak, ale tylko w obszarze niezabudowanym.
- C. Tak, ale tylko w obszarze zabudowanym.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 13561: Prędkość bezpieczna to prędkość :**

- A. która zapewnia panowanie nad pojazdem.
- B. która jest równa dopuszczalnej prędkości na danym odcinku drogi.
- C. którą "podpowiada" nawigacja w Twoim pojeździe.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✗. Official key: **A**.

**Question 1864: Jakiej kategorii prawo jazdy jest wymagane, gdy chcesz kierować czterokołowcem innym niż lekki?**

- A. B1.
- B. A.
- C. AM.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 7446: Jaki odstęp od poprzedzającego pojazdu masz obowiązek zachować podczas zatrzymania w zatorze drogowym w tunelu?**

- A. Nie mniejszy niż 3 metry.
- B. Nie mniejszy niż 5 metrów.
- C. Nie mniejszy niż 10 metrów.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 13382: Po spełnieniu, którego z wymienionych warunków można przewozić samochodem osobowym, poza fotelikiem bezpieczeństwa lub innym urządzeniem przytrzymującym, dziecko mające mniej niż 150 cm wzrostu?**

- A. Prędkość pojazdu nie przekroczy 40 km/h.
- B. Dziecko posiada zaświadczenie lekarskie o przeciwwskazaniu do przewożenia w foteliku lub innym urządzeniu.
- C. Pojazd posiada dodatkowe oznakowanie, które wskazuje, że jest nim przewożone dziecko.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 10871: W jaki sposób zainstalujesz w pojeździe fotelik bezpieczeństwa służący do przewozu dziecka?**

- A. W sposób wygodny dla dziecka.
- B. W sposób wygodny dla siebie.
- C. Zgodnie z zaleceniami producenta urządzenia.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10822: W przypadku gdy kierujący przekroczył dopuszczalną prędkość o więcej niż 50 km/h na obszarze zabudowanym, starosta wydaje decyzję administracyjną o zatrzymaniu prawa jazdy na okres:**

- A. 1 miesiąca.
- B. 2 miesięcy.
- C. 3 miesięcy.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 4578: Jesteś uczestnikiem lub świadkiem wypadku drogowego. Które z wymienionych informacji należy podać dzwoniąc pod numer alarmowy?**

- A. Miejsce zdarzenia oraz liczbę i stan ofiar wypadku.
- B. Tylko liczbę pojazdów biorących udział w wypadku.
- C. Tylko liczbę ofiar wypadku.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 7519: Kiedy należy sprawdzać poziom oleju w silniku?**

- A. Przy uruchomionym silniku.
- B. Natychmiast po unieruchomieniu silnika.
- C. Przed uruchomieniem zimnego silnika albo co najmniej po kilku minutach po jego wyłączeniu.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10878: Jakie muszą być spełnione warunki podczas przewożenia dziecka na tylnym siedzeniu samochodu osobowego?**

- A. Przewożone dziecko ma co najmniej 135 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w foteliku lub innym urządzeniu przytrzymującym  dziecko.
- B. Przewożone dziecko ma co najmniej 125 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w foteliku.
- C. Nie można przekraczać prędkości 50 km/h.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✗. Official key: **A**.

**Question 10880: Jakie musisz spełnić warunki, gdy chcesz przewieźć dziecko na tylnym siedzeniu samochodu osobowego?**

- A. Przewożone dziecko ma co najmniej 125 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w urządzeniu przytrzymującym.
- B. Nie można przekraczać prędkości 40 km/h.
- C. Przewożone dziecko ma co najmniej 135 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w urządzeniu przytrzymującym.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10994: Kiedy wolno przewozić samochodem ciężarowym, na przednim siedzeniu, dziecko mające poniżej 150 cm wzrostu, przytrzymywane jedynie za pomocą pasów bezpieczeństwa?**

- A. Jeżeli dziecko ma co najmniej 135 cm wzrostu.
- B. Jeżeli w samochodzie tym nie ma możliwości zamontowania fotelika bezpieczeństwa.
- C. Jeżeli dziecko ma zaświadczenie lekarskie o przeciwwskazaniu do przewożenia w foteliku bezpieczeństwa.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 7513: Czy jako właściciel pojazdu masz obowiązek wskazać na żądanie uprawnionego organu, komu powierzyłeś pojazd do kierowania lub używania w określonym czasie?**

- A. Tak, chyba że jest to pojazd wykorzystywany do prowadzenia działalności gospodarczej.
- B. Tak, chyba że pojazd został użyty wbrew Twojej woli i wiedzy przez nieznaną osobę, czemu nie mogłeś zapobiec.
- C. Nie mam takiego obowiązku.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 10889: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dokument dopuszczający pojazd do ruchu.
- B. Dokument potwierdzający zawarcie umowy ubezpieczenia od nieszczęśliwych wypadków.
- C. Kopię zaświadczenia o przeprowadzonym badaniu technicznym.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 10890: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dowód własności pojazdu.
- B. Dokument potwierdzający zawarcie umowy obowiązkowego ubezpieczenia odpowiedzialności cywilnej posiadacza pojazdu.
- C. Dokument potwierdzający opłatę skarbową.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 10891: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Profesjonalny dowód rejestracyjny.
- B. Dowód opłacenia składki za obowiązkowe ubezpieczenie odpowiedzialności cywilnej.
- C. Dokument potwierdzający opłatę za korzystanie z autostrad i dróg ekspresowych.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 7452: Jakiej wielkości nie ma prawa przekroczyć rzeczywista masa całkowita przyczepy ciągniętej przez samochód osobowy?**

- A. Masy własnej samochodu.
- B. Rzeczywistej masy całkowitej samochodu.
- C. Rzeczywistej masy całkowitej samochodu pomniejszonej o 40%.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 3625: Jaki odstęp należy zachować podczas wymijania samochodem osobowym innego pojazdu?**

- A. Bezpieczny, ale nie mniejszy niż 1,5 metra.
- B. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.
- C. Bezpieczny, czyli zawsze taki sam.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 3627: Jaki odstęp należy zachować podczas omijania samochodem osobowym przeszkody na drodze?**

- A. Bezpieczny, ale nie mniejszy niż 0,8 metra.
- B. Bezpieczny, czyli zawsze jednakowy.
- C. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 3628: Jaki odstęp należy zachować podczas wyprzedzania samochodu osobowego?**

- A. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.
- B. Bezpieczny, ale większy niż 1,5 metra.
- C. Bezpieczny, ale mniejszy niż 0,5 metra.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✗. Official key: **A**.

**Question 3629: Jaki odstęp należy zachować podczas wyprzedzania motocykla?**

- A. Bezpieczny, ale nie większy niż 0,5 metra.
- B. Bezpieczny, ale nie większy niż 1 metr.
- C. Bezpieczny, ale nie mniejszy niż 1 metr.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✗. Official key: **C**.

**Question 3630: Jaki odstęp należy zachować podczas wyprzedzania kolumny pieszych?**

- A. Bezpieczny, ale nie mniejszy niż 0,6 metra.
- B. Bezpieczny, ale nie mniejszy niż 0,8 metra.
- C. Bezpieczny, ale nie mniejszy niż 1 metr.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 3778: Jak należy zachować się podczas wymijania samochodem osobowym w nocy innego pojazdu?**

- A. Patrzeć prosto w światła pojazdu nadjeżdżającego z przeciwka.
- B. Zmienić światła mijania na drogowe.
- C. Patrzeć w prawo od źródła światła pojazdu nadjeżdżającego z przeciwka i wypatrywać tam ewentualnej przeszkody.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 3650: Jak duży odstęp od poprzedzającego pojazdu należy utrzymywać, kierując samochodem osobowym poza obszarem zabudowanym w tunelu o długości 600 metrów?**

- A. Nie mniejszy niż 50 metrów.
- B. Nie mniejszy niż 40 metrów.
- C. Nie mniejszy niż 30 metrów.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

### test_rotated: 11 corrections, 5 regressions

**Question 10840: W jaki sposób przewozisz dziecko o wzroście mniejszym niż 150 cm na przednim siedzeniu samochodu osobowego, który ma pięć miejsc siedzących?**

- A.  W foteliku bezpieczeństwa lub innym urządzeniu przytrzymującym dziecko.
- B. W foteliku bezpieczeństwa tyłem do kierunku jazdy, jeżeli pojazd ma aktywną poduszkę powietrzną dla pasażera.
- C.  Na kolanach pasażera.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 10869: W jaki sposób przewozisz dziecko o wzroście mniejszym niż 150 cm samochodem osobowym, w którym jest pięć miejsc siedzących?**

- A. Na przednim siedzeniu w innym niż fotelik urządzeniu przytrzymującym dziecko.
- B. Na tylnym siedzeniu bez zapiętych pasów bezpieczeństwa.
- C. Na przednim siedzeniu bez fotelika lub innego urządzenia przytrzymującego dziecko.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 11001: Który z wymienionych dokumentów kierujący pojazdem zarejestrowanym na terytorium RP musi mieć przy sobie i okazywać na żądanie uprawnionego organu?**

- A. Dowód rejestracyjny.
- B. Jeśli kierujący ma uprawnienia do kierowania ograniczone do pojazdu wyposażonego w blokadę alkoholową - zaświadczenie o pozytywnym wyniku badania technicznego w tym zakresie.
- C. Potwierdzenie opłacenia obowiązkowego ubezpieczenia odpowiedzialności cywilnej właściciela pojazdu.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 10931: Ile czasu jest ważne pokwitowanie zatrzymania przez policjanta prawa jazdy za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w dowodzie rejestracyjnym samochodu osobowego?**

- A. 24 godziny.
- B. 72 godziny.
- C. 12 godzin.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 10898: Za które naruszenie przepisów ruchu drogowego policjant zatrzyma prawo jazdy?**

- A. Za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w dowodzie rejestracyjnym samochodu osobowego.
- B. Za wymijanie na przejeździe kolejowym.
- C. Za wyprzedzanie z naruszeniem pojedynczej linii ciągłej.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 10899: Za które naruszenie przepisów ruchu drogowego policjant zatrzyma prawo jazdy?**

- A. Za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w pozwoleniu czasowym samochodu osobowego.
- B. Za wymijanie na przejeździe dla rowerzystów.
- C. Za wyprzedzanie przed przejściem dla pieszych, gdzie ruch jest kierowany.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 4562: Kto podlega odpowiedzialności karnej w przypadku nieudzielenia pomocy poszkodowanemu w wypadku drogowym z bezpośrednim zagrożeniu utraty zdrowia i życia?**

- A. Tylko lekarz.
- B. Tylko uczestnik wypadku drogowego.
- C. Każda osoba, która mogła udzielić pomocy bez narażenia siebie lub innej osoby na niebezpieczeństwo utraty życia lub ciężkiego uszczerbku zdrowia.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 6442: Do czego służą światła pozycyjne pojazdu?**

- A. Do określania pozycji pojazdu.
- B. Do sygnalizowania zmiany pasa ruchu.
- C. Do oświetlania drogi.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 7445: Której z tych czynności nie masz prawa wykonywać samochodem osobowym?**

- A. Holować innego samochodu osobowego na obszarze zabudowanym.
- B. Ciągnąć dzieci na sankach.
- C. Ciągnąć przyczepy lekkiej.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 7454: Na której z tych dróg nie masz prawa holować samochodem osobowym innego pojazdu?**

- A. Na drodze ekspresowej.
- B. W strefie zamieszkania.
- C. Na autostradzie.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 6463: Jadąc zimą spotykasz na poboczu sinego, półprzytomnego, wyziębionego człowieka. Jak należy mu pomóc?**

- A. Podać mu alkohol.
- B. Wezwać zespół ratownictwa medycznego, zabrać go do samochodu, okryć i powoli ogrzewać.
- C. Podać mu gorący napój.

Original Qwen/Qwen3.5-0.8B: **B** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 10829: Dokumentem stwierdzającym dopuszczenie pojazdu samochodowego do ruchu jest:**

- A. karta pojazdu.
- B. nalepka kontrolna na przedniej szybie.
- C. dowód rejestracyjny.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10815: Foteliki bezpieczeństwa dla dzieci oraz inne urządzenia przytrzymujące dla dzieci należy instalować w pojeździe:**

- A. w sposób umożliwiający łatwy dostęp do dziecka.
- B. zgodnie z zaleceniami producenta urządzenia.
- C. w sposób bezpieczny i estetyczny.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 3573: Jesteś świadkiem potrącenia pieszego. Jak powinieneś się zachować?**

- A. Wezwać pomoc drogową.
- B. Zatrzymać się, wezwać pomoć medyczną i udzielić pierwszej pomocy poszkodowanemu.
- C. Nie podejmować działań, gdyż pomocy musi udzielić sprawca wypadku.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 7515: Czy wolno Ci kierować pojazdem, którego tablica rejestracyjna jest niewidoczna?**

- A. Tak, gdy tablica jest przesłonięta przez wystający ładunek.
- B. Nie, jest to zabronione.
- C. Tak, bez żadnych ograniczeń.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 9035: Jaki wpływ na pole widzenia kierującego pojazdem ma prędkość jazdy?**

- A. Wraz ze wzrostem prędkości rozszerza się pole widzenia.
- B. Prędkość jazdy nie ma wpływu na pole widzenia kierującego.
- C. Wraz ze wzrostem prędkości zawęża się pole widzenia.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10081: Czy dopuszczalne jest holowanie za pomocą połączenia sztywnego pojazdu o niesprawnym układzie kierowniczym?**

- A. Tak, ale tylko w obszarze niezabudowanym.
- B. Tak, ale tylko w obszarze zabudowanym.
- C. Nie.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 13561: Prędkość bezpieczna to prędkość :**

- A. która jest równa dopuszczalnej prędkości na danym odcinku drogi.
- B. którą "podpowiada" nawigacja w Twoim pojeździe.
- C. która zapewnia panowanie nad pojazdem.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 1864: Jakiej kategorii prawo jazdy jest wymagane, gdy chcesz kierować czterokołowcem innym niż lekki?**

- A. A.
- B. AM.
- C. B1.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 7446: Jaki odstęp od poprzedzającego pojazdu masz obowiązek zachować podczas zatrzymania w zatorze drogowym w tunelu?**

- A. Nie mniejszy niż 5 metrów.
- B. Nie mniejszy niż 10 metrów.
- C. Nie mniejszy niż 3 metry.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✗. Official key: **A**.

**Question 13382: Po spełnieniu, którego z wymienionych warunków można przewozić samochodem osobowym, poza fotelikiem bezpieczeństwa lub innym urządzeniem przytrzymującym, dziecko mające mniej niż 150 cm wzrostu?**

- A. Dziecko posiada zaświadczenie lekarskie o przeciwwskazaniu do przewożenia w foteliku lub innym urządzeniu.
- B. Pojazd posiada dodatkowe oznakowanie, które wskazuje, że jest nim przewożone dziecko.
- C. Prędkość pojazdu nie przekroczy 40 km/h.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 10871: W jaki sposób zainstalujesz w pojeździe fotelik bezpieczeństwa służący do przewozu dziecka?**

- A. W sposób wygodny dla siebie.
- B. Zgodnie z zaleceniami producenta urządzenia.
- C. W sposób wygodny dla dziecka.

Original Qwen/Qwen3.5-0.8B: **B** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 10822: W przypadku gdy kierujący przekroczył dopuszczalną prędkość o więcej niż 50 km/h na obszarze zabudowanym, starosta wydaje decyzję administracyjną o zatrzymaniu prawa jazdy na okres:**

- A. 2 miesięcy.
- B. 3 miesięcy.
- C. 1 miesiąca.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 4578: Jesteś uczestnikiem lub świadkiem wypadku drogowego. Które z wymienionych informacji należy podać dzwoniąc pod numer alarmowy?**

- A. Tylko liczbę pojazdów biorących udział w wypadku.
- B. Tylko liczbę ofiar wypadku.
- C. Miejsce zdarzenia oraz liczbę i stan ofiar wypadku.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 7519: Kiedy należy sprawdzać poziom oleju w silniku?**

- A. Natychmiast po unieruchomieniu silnika.
- B. Przed uruchomieniem zimnego silnika albo co najmniej po kilku minutach po jego wyłączeniu.
- C. Przy uruchomionym silniku.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 10878: Jakie muszą być spełnione warunki podczas przewożenia dziecka na tylnym siedzeniu samochodu osobowego?**

- A. Przewożone dziecko ma co najmniej 125 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w foteliku.
- B. Nie można przekraczać prędkości 50 km/h.
- C. Przewożone dziecko ma co najmniej 135 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w foteliku lub innym urządzeniu przytrzymującym  dziecko.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10880: Jakie musisz spełnić warunki, gdy chcesz przewieźć dziecko na tylnym siedzeniu samochodu osobowego?**

- A. Nie można przekraczać prędkości 40 km/h.
- B. Przewożone dziecko ma co najmniej 135 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w urządzeniu przytrzymującym.
- C. Przewożone dziecko ma co najmniej 125 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w urządzeniu przytrzymującym.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 10994: Kiedy wolno przewozić samochodem ciężarowym, na przednim siedzeniu, dziecko mające poniżej 150 cm wzrostu, przytrzymywane jedynie za pomocą pasów bezpieczeństwa?**

- A. Jeżeli w samochodzie tym nie ma możliwości zamontowania fotelika bezpieczeństwa.
- B. Jeżeli dziecko ma zaświadczenie lekarskie o przeciwwskazaniu do przewożenia w foteliku bezpieczeństwa.
- C. Jeżeli dziecko ma co najmniej 135 cm wzrostu.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✗. Official key: **B**.

**Question 7513: Czy jako właściciel pojazdu masz obowiązek wskazać na żądanie uprawnionego organu, komu powierzyłeś pojazd do kierowania lub używania w określonym czasie?**

- A. Tak, chyba że pojazd został użyty wbrew Twojej woli i wiedzy przez nieznaną osobę, czemu nie mogłeś zapobiec.
- B. Nie mam takiego obowiązku.
- C. Tak, chyba że jest to pojazd wykorzystywany do prowadzenia działalności gospodarczej.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 10889: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dokument potwierdzający zawarcie umowy ubezpieczenia od nieszczęśliwych wypadków.
- B. Kopię zaświadczenia o przeprowadzonym badaniu technicznym.
- C. Dokument dopuszczający pojazd do ruchu.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.

**Question 10890: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dokument potwierdzający zawarcie umowy obowiązkowego ubezpieczenia odpowiedzialności cywilnej posiadacza pojazdu.
- B. Dokument potwierdzający opłatę skarbową.
- C. Dowód własności pojazdu.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 10891: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dowód opłacenia składki za obowiązkowe ubezpieczenie odpowiedzialności cywilnej.
- B. Dokument potwierdzający opłatę za korzystanie z autostrad i dróg ekspresowych.
- C. Profesjonalny dowód rejestracyjny.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 7452: Jakiej wielkości nie ma prawa przekroczyć rzeczywista masa całkowita przyczepy ciągniętej przez samochód osobowy?**

- A. Rzeczywistej masy całkowitej samochodu.
- B. Rzeczywistej masy całkowitej samochodu pomniejszonej o 40%.
- C. Masy własnej samochodu.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✓. Official key: **A**.

**Question 3625: Jaki odstęp należy zachować podczas wymijania samochodem osobowym innego pojazdu?**

- A. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.
- B. Bezpieczny, czyli zawsze taki sam.
- C. Bezpieczny, ale nie mniejszy niż 1,5 metra.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **A**.

**Question 3627: Jaki odstęp należy zachować podczas omijania samochodem osobowym przeszkody na drodze?**

- A. Bezpieczny, czyli zawsze jednakowy.
- B. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.
- C. Bezpieczny, ale nie mniejszy niż 0,8 metra.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✗. Official key: **B**.

**Question 3628: Jaki odstęp należy zachować podczas wyprzedzania samochodu osobowego?**

- A. Bezpieczny, ale większy niż 1,5 metra.
- B. Bezpieczny, ale mniejszy niż 0,5 metra.
- C. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **A** ✗. Official key: **C**.

**Question 3629: Jaki odstęp należy zachować podczas wyprzedzania motocykla?**

- A. Bezpieczny, ale nie większy niż 1 metr.
- B. Bezpieczny, ale nie mniejszy niż 1 metr.
- C. Bezpieczny, ale nie większy niż 0,5 metra.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 3630: Jaki odstęp należy zachować podczas wyprzedzania kolumny pieszych?**

- A. Bezpieczny, ale nie mniejszy niż 0,8 metra.
- B. Bezpieczny, ale nie mniejszy niż 1 metr.
- C. Bezpieczny, ale nie mniejszy niż 0,6 metra.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 3778: Jak należy zachować się podczas wymijania samochodem osobowym w nocy innego pojazdu?**

- A. Zmienić światła mijania na drogowe.
- B. Patrzeć w prawo od źródła światła pojazdu nadjeżdżającego z przeciwka i wypatrywać tam ewentualnej przeszkody.
- C. Patrzeć prosto w światła pojazdu nadjeżdżającego z przeciwka.

Original Qwen/Qwen3.5-0.8B: **B** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **B** ✓. Official key: **B**.

**Question 3650: Jak duży odstęp od poprzedzającego pojazdu należy utrzymywać, kierując samochodem osobowym poza obszarem zabudowanym w tunelu o długości 600 metrów?**

- A. Nie mniejszy niż 40 metrów.
- B. Nie mniejszy niż 30 metrów.
- C. Nie mniejszy niż 50 metrów.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + SFT on 100 official questions: **C** ✓. Official key: **C**.


## Qwen/Qwen3.5-0.8B + RLVR on 100 official questions

Run: `prawko-rlvr-1788860780645474401`. Base revision: `2fc06364715b967f1860aea9cf38778875588b17`.
Development-selected epoch 3; 75 selected updates of 208 explored updates. Reload matches: True.
Before = original pretrained/instruction model, no workshop adapter. After = fresh adapter trained only on the 100 training questions; no Pan Tadeusz or film training.

### test: 11 corrections, 5 regressions

**Question 10840: W jaki sposób przewozisz dziecko o wzroście mniejszym niż 150 cm na przednim siedzeniu samochodu osobowego, który ma pięć miejsc siedzących?**

- A.  Na kolanach pasażera.
- B.  W foteliku bezpieczeństwa lub innym urządzeniu przytrzymującym dziecko.
- C. W foteliku bezpieczeństwa tyłem do kierunku jazdy, jeżeli pojazd ma aktywną poduszkę powietrzną dla pasażera.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 10869: W jaki sposób przewozisz dziecko o wzroście mniejszym niż 150 cm samochodem osobowym, w którym jest pięć miejsc siedzących?**

- A. Na przednim siedzeniu bez fotelika lub innego urządzenia przytrzymującego dziecko.
- B. Na przednim siedzeniu w innym niż fotelik urządzeniu przytrzymującym dziecko.
- C. Na tylnym siedzeniu bez zapiętych pasów bezpieczeństwa.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 11001: Który z wymienionych dokumentów kierujący pojazdem zarejestrowanym na terytorium RP musi mieć przy sobie i okazywać na żądanie uprawnionego organu?**

- A. Potwierdzenie opłacenia obowiązkowego ubezpieczenia odpowiedzialności cywilnej właściciela pojazdu.
- B. Dowód rejestracyjny.
- C. Jeśli kierujący ma uprawnienia do kierowania ograniczone do pojazdu wyposażonego w blokadę alkoholową - zaświadczenie o pozytywnym wyniku badania technicznego w tym zakresie.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10931: Ile czasu jest ważne pokwitowanie zatrzymania przez policjanta prawa jazdy za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w dowodzie rejestracyjnym samochodu osobowego?**

- A. 12 godzin.
- B. 24 godziny.
- C. 72 godziny.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 10898: Za które naruszenie przepisów ruchu drogowego policjant zatrzyma prawo jazdy?**

- A. Za wyprzedzanie z naruszeniem pojedynczej linii ciągłej.
- B. Za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w dowodzie rejestracyjnym samochodu osobowego.
- C. Za wymijanie na przejeździe kolejowym.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 10899: Za które naruszenie przepisów ruchu drogowego policjant zatrzyma prawo jazdy?**

- A. Za wyprzedzanie przed przejściem dla pieszych, gdzie ruch jest kierowany.
- B. Za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w pozwoleniu czasowym samochodu osobowego.
- C. Za wymijanie na przejeździe dla rowerzystów.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 4562: Kto podlega odpowiedzialności karnej w przypadku nieudzielenia pomocy poszkodowanemu w wypadku drogowym z bezpośrednim zagrożeniu utraty zdrowia i życia?**

- A. Każda osoba, która mogła udzielić pomocy bez narażenia siebie lub innej osoby na niebezpieczeństwo utraty życia lub ciężkiego uszczerbku zdrowia.
- B. Tylko lekarz.
- C. Tylko uczestnik wypadku drogowego.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 6442: Do czego służą światła pozycyjne pojazdu?**

- A. Do oświetlania drogi.
- B. Do określania pozycji pojazdu.
- C. Do sygnalizowania zmiany pasa ruchu.

Original Qwen/Qwen3.5-0.8B: **B** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 7445: Której z tych czynności nie masz prawa wykonywać samochodem osobowym?**

- A. Ciągnąć przyczepy lekkiej.
- B. Holować innego samochodu osobowego na obszarze zabudowanym.
- C. Ciągnąć dzieci na sankach.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 7454: Na której z tych dróg nie masz prawa holować samochodem osobowym innego pojazdu?**

- A. Na autostradzie.
- B. Na drodze ekspresowej.
- C. W strefie zamieszkania.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✗. Official key: **A**.

**Question 6463: Jadąc zimą spotykasz na poboczu sinego, półprzytomnego, wyziębionego człowieka. Jak należy mu pomóc?**

- A. Podać mu gorący napój.
- B. Podać mu alkohol.
- C. Wezwać zespół ratownictwa medycznego, zabrać go do samochodu, okryć i powoli ogrzewać.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10829: Dokumentem stwierdzającym dopuszczenie pojazdu samochodowego do ruchu jest:**

- A. dowód rejestracyjny.
- B. karta pojazdu.
- C. nalepka kontrolna na przedniej szybie.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 10815: Foteliki bezpieczeństwa dla dzieci oraz inne urządzenia przytrzymujące dla dzieci należy instalować w pojeździe:**

- A. w sposób bezpieczny i estetyczny.
- B. w sposób umożliwiający łatwy dostęp do dziecka.
- C. zgodnie z zaleceniami producenta urządzenia.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 3573: Jesteś świadkiem potrącenia pieszego. Jak powinieneś się zachować?**

- A. Nie podejmować działań, gdyż pomocy musi udzielić sprawca wypadku.
- B. Wezwać pomoc drogową.
- C. Zatrzymać się, wezwać pomoć medyczną i udzielić pierwszej pomocy poszkodowanemu.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 7515: Czy wolno Ci kierować pojazdem, którego tablica rejestracyjna jest niewidoczna?**

- A. Tak, bez żadnych ograniczeń.
- B. Tak, gdy tablica jest przesłonięta przez wystający ładunek.
- C. Nie, jest to zabronione.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 9035: Jaki wpływ na pole widzenia kierującego pojazdem ma prędkość jazdy?**

- A. Wraz ze wzrostem prędkości zawęża się pole widzenia.
- B. Wraz ze wzrostem prędkości rozszerza się pole widzenia.
- C. Prędkość jazdy nie ma wpływu na pole widzenia kierującego.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 10081: Czy dopuszczalne jest holowanie za pomocą połączenia sztywnego pojazdu o niesprawnym układzie kierowniczym?**

- A. Nie.
- B. Tak, ale tylko w obszarze niezabudowanym.
- C. Tak, ale tylko w obszarze zabudowanym.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 13561: Prędkość bezpieczna to prędkość :**

- A. która zapewnia panowanie nad pojazdem.
- B. która jest równa dopuszczalnej prędkości na danym odcinku drogi.
- C. którą "podpowiada" nawigacja w Twoim pojeździe.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✗. Official key: **A**.

**Question 1864: Jakiej kategorii prawo jazdy jest wymagane, gdy chcesz kierować czterokołowcem innym niż lekki?**

- A. B1.
- B. A.
- C. AM.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 7446: Jaki odstęp od poprzedzającego pojazdu masz obowiązek zachować podczas zatrzymania w zatorze drogowym w tunelu?**

- A. Nie mniejszy niż 3 metry.
- B. Nie mniejszy niż 5 metrów.
- C. Nie mniejszy niż 10 metrów.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 13382: Po spełnieniu, którego z wymienionych warunków można przewozić samochodem osobowym, poza fotelikiem bezpieczeństwa lub innym urządzeniem przytrzymującym, dziecko mające mniej niż 150 cm wzrostu?**

- A. Prędkość pojazdu nie przekroczy 40 km/h.
- B. Dziecko posiada zaświadczenie lekarskie o przeciwwskazaniu do przewożenia w foteliku lub innym urządzeniu.
- C. Pojazd posiada dodatkowe oznakowanie, które wskazuje, że jest nim przewożone dziecko.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✗. Official key: **B**.

**Question 10871: W jaki sposób zainstalujesz w pojeździe fotelik bezpieczeństwa służący do przewozu dziecka?**

- A. W sposób wygodny dla dziecka.
- B. W sposób wygodny dla siebie.
- C. Zgodnie z zaleceniami producenta urządzenia.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10822: W przypadku gdy kierujący przekroczył dopuszczalną prędkość o więcej niż 50 km/h na obszarze zabudowanym, starosta wydaje decyzję administracyjną o zatrzymaniu prawa jazdy na okres:**

- A. 1 miesiąca.
- B. 2 miesięcy.
- C. 3 miesięcy.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **C**.

**Question 4578: Jesteś uczestnikiem lub świadkiem wypadku drogowego. Które z wymienionych informacji należy podać dzwoniąc pod numer alarmowy?**

- A. Miejsce zdarzenia oraz liczbę i stan ofiar wypadku.
- B. Tylko liczbę pojazdów biorących udział w wypadku.
- C. Tylko liczbę ofiar wypadku.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 7519: Kiedy należy sprawdzać poziom oleju w silniku?**

- A. Przy uruchomionym silniku.
- B. Natychmiast po unieruchomieniu silnika.
- C. Przed uruchomieniem zimnego silnika albo co najmniej po kilku minutach po jego wyłączeniu.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10878: Jakie muszą być spełnione warunki podczas przewożenia dziecka na tylnym siedzeniu samochodu osobowego?**

- A. Przewożone dziecko ma co najmniej 135 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w foteliku lub innym urządzeniu przytrzymującym  dziecko.
- B. Przewożone dziecko ma co najmniej 125 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w foteliku.
- C. Nie można przekraczać prędkości 50 km/h.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 10880: Jakie musisz spełnić warunki, gdy chcesz przewieźć dziecko na tylnym siedzeniu samochodu osobowego?**

- A. Przewożone dziecko ma co najmniej 125 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w urządzeniu przytrzymującym.
- B. Nie można przekraczać prędkości 40 km/h.
- C. Przewożone dziecko ma co najmniej 135 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w urządzeniu przytrzymującym.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10994: Kiedy wolno przewozić samochodem ciężarowym, na przednim siedzeniu, dziecko mające poniżej 150 cm wzrostu, przytrzymywane jedynie za pomocą pasów bezpieczeństwa?**

- A. Jeżeli dziecko ma co najmniej 135 cm wzrostu.
- B. Jeżeli w samochodzie tym nie ma możliwości zamontowania fotelika bezpieczeństwa.
- C. Jeżeli dziecko ma zaświadczenie lekarskie o przeciwwskazaniu do przewożenia w foteliku bezpieczeństwa.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 7513: Czy jako właściciel pojazdu masz obowiązek wskazać na żądanie uprawnionego organu, komu powierzyłeś pojazd do kierowania lub używania w określonym czasie?**

- A. Tak, chyba że jest to pojazd wykorzystywany do prowadzenia działalności gospodarczej.
- B. Tak, chyba że pojazd został użyty wbrew Twojej woli i wiedzy przez nieznaną osobę, czemu nie mogłeś zapobiec.
- C. Nie mam takiego obowiązku.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 10889: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dokument dopuszczający pojazd do ruchu.
- B. Dokument potwierdzający zawarcie umowy ubezpieczenia od nieszczęśliwych wypadków.
- C. Kopię zaświadczenia o przeprowadzonym badaniu technicznym.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✗. Official key: **A**.

**Question 10890: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dowód własności pojazdu.
- B. Dokument potwierdzający zawarcie umowy obowiązkowego ubezpieczenia odpowiedzialności cywilnej posiadacza pojazdu.
- C. Dokument potwierdzający opłatę skarbową.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 10891: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Profesjonalny dowód rejestracyjny.
- B. Dowód opłacenia składki za obowiązkowe ubezpieczenie odpowiedzialności cywilnej.
- C. Dokument potwierdzający opłatę za korzystanie z autostrad i dróg ekspresowych.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 7452: Jakiej wielkości nie ma prawa przekroczyć rzeczywista masa całkowita przyczepy ciągniętej przez samochód osobowy?**

- A. Masy własnej samochodu.
- B. Rzeczywistej masy całkowitej samochodu.
- C. Rzeczywistej masy całkowitej samochodu pomniejszonej o 40%.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 3625: Jaki odstęp należy zachować podczas wymijania samochodem osobowym innego pojazdu?**

- A. Bezpieczny, ale nie mniejszy niż 1,5 metra.
- B. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.
- C. Bezpieczny, czyli zawsze taki sam.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 3627: Jaki odstęp należy zachować podczas omijania samochodem osobowym przeszkody na drodze?**

- A. Bezpieczny, ale nie mniejszy niż 0,8 metra.
- B. Bezpieczny, czyli zawsze jednakowy.
- C. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **C**.

**Question 3628: Jaki odstęp należy zachować podczas wyprzedzania samochodu osobowego?**

- A. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.
- B. Bezpieczny, ale większy niż 1,5 metra.
- C. Bezpieczny, ale mniejszy niż 0,5 metra.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✗. Official key: **A**.

**Question 3629: Jaki odstęp należy zachować podczas wyprzedzania motocykla?**

- A. Bezpieczny, ale nie większy niż 0,5 metra.
- B. Bezpieczny, ale nie większy niż 1 metr.
- C. Bezpieczny, ale nie mniejszy niż 1 metr.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **C**.

**Question 3630: Jaki odstęp należy zachować podczas wyprzedzania kolumny pieszych?**

- A. Bezpieczny, ale nie mniejszy niż 0,6 metra.
- B. Bezpieczny, ale nie mniejszy niż 0,8 metra.
- C. Bezpieczny, ale nie mniejszy niż 1 metr.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **C**.

**Question 3778: Jak należy zachować się podczas wymijania samochodem osobowym w nocy innego pojazdu?**

- A. Patrzeć prosto w światła pojazdu nadjeżdżającego z przeciwka.
- B. Zmienić światła mijania na drogowe.
- C. Patrzeć w prawo od źródła światła pojazdu nadjeżdżającego z przeciwka i wypatrywać tam ewentualnej przeszkody.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 3650: Jak duży odstęp od poprzedzającego pojazdu należy utrzymywać, kierując samochodem osobowym poza obszarem zabudowanym w tunelu o długości 600 metrów?**

- A. Nie mniejszy niż 50 metrów.
- B. Nie mniejszy niż 40 metrów.
- C. Nie mniejszy niż 30 metrów.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

### test_rotated: 8 corrections, 3 regressions

**Question 10840: W jaki sposób przewozisz dziecko o wzroście mniejszym niż 150 cm na przednim siedzeniu samochodu osobowego, który ma pięć miejsc siedzących?**

- A.  W foteliku bezpieczeństwa lub innym urządzeniu przytrzymującym dziecko.
- B. W foteliku bezpieczeństwa tyłem do kierunku jazdy, jeżeli pojazd ma aktywną poduszkę powietrzną dla pasażera.
- C.  Na kolanach pasażera.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 10869: W jaki sposób przewozisz dziecko o wzroście mniejszym niż 150 cm samochodem osobowym, w którym jest pięć miejsc siedzących?**

- A. Na przednim siedzeniu w innym niż fotelik urządzeniu przytrzymującym dziecko.
- B. Na tylnym siedzeniu bez zapiętych pasów bezpieczeństwa.
- C. Na przednim siedzeniu bez fotelika lub innego urządzenia przytrzymującego dziecko.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✗. Official key: **A**.

**Question 11001: Który z wymienionych dokumentów kierujący pojazdem zarejestrowanym na terytorium RP musi mieć przy sobie i okazywać na żądanie uprawnionego organu?**

- A. Dowód rejestracyjny.
- B. Jeśli kierujący ma uprawnienia do kierowania ograniczone do pojazdu wyposażonego w blokadę alkoholową - zaświadczenie o pozytywnym wyniku badania technicznego w tym zakresie.
- C. Potwierdzenie opłacenia obowiązkowego ubezpieczenia odpowiedzialności cywilnej właściciela pojazdu.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 10931: Ile czasu jest ważne pokwitowanie zatrzymania przez policjanta prawa jazdy za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w dowodzie rejestracyjnym samochodu osobowego?**

- A. 24 godziny.
- B. 72 godziny.
- C. 12 godzin.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 10898: Za które naruszenie przepisów ruchu drogowego policjant zatrzyma prawo jazdy?**

- A. Za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w dowodzie rejestracyjnym samochodu osobowego.
- B. Za wymijanie na przejeździe kolejowym.
- C. Za wyprzedzanie z naruszeniem pojedynczej linii ciągłej.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 10899: Za które naruszenie przepisów ruchu drogowego policjant zatrzyma prawo jazdy?**

- A. Za przewożenie osób w liczbie przekraczającej o dwa liczbę miejsc określoną w pozwoleniu czasowym samochodu osobowego.
- B. Za wymijanie na przejeździe dla rowerzystów.
- C. Za wyprzedzanie przed przejściem dla pieszych, gdzie ruch jest kierowany.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 4562: Kto podlega odpowiedzialności karnej w przypadku nieudzielenia pomocy poszkodowanemu w wypadku drogowym z bezpośrednim zagrożeniu utraty zdrowia i życia?**

- A. Tylko lekarz.
- B. Tylko uczestnik wypadku drogowego.
- C. Każda osoba, która mogła udzielić pomocy bez narażenia siebie lub innej osoby na niebezpieczeństwo utraty życia lub ciężkiego uszczerbku zdrowia.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 6442: Do czego służą światła pozycyjne pojazdu?**

- A. Do określania pozycji pojazdu.
- B. Do sygnalizowania zmiany pasa ruchu.
- C. Do oświetlania drogi.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 7445: Której z tych czynności nie masz prawa wykonywać samochodem osobowym?**

- A. Holować innego samochodu osobowego na obszarze zabudowanym.
- B. Ciągnąć dzieci na sankach.
- C. Ciągnąć przyczepy lekkiej.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 7454: Na której z tych dróg nie masz prawa holować samochodem osobowym innego pojazdu?**

- A. Na drodze ekspresowej.
- B. W strefie zamieszkania.
- C. Na autostradzie.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 6463: Jadąc zimą spotykasz na poboczu sinego, półprzytomnego, wyziębionego człowieka. Jak należy mu pomóc?**

- A. Podać mu alkohol.
- B. Wezwać zespół ratownictwa medycznego, zabrać go do samochodu, okryć i powoli ogrzewać.
- C. Podać mu gorący napój.

Original Qwen/Qwen3.5-0.8B: **B** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 10829: Dokumentem stwierdzającym dopuszczenie pojazdu samochodowego do ruchu jest:**

- A. karta pojazdu.
- B. nalepka kontrolna na przedniej szybie.
- C. dowód rejestracyjny.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10815: Foteliki bezpieczeństwa dla dzieci oraz inne urządzenia przytrzymujące dla dzieci należy instalować w pojeździe:**

- A. w sposób umożliwiający łatwy dostęp do dziecka.
- B. zgodnie z zaleceniami producenta urządzenia.
- C. w sposób bezpieczny i estetyczny.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 3573: Jesteś świadkiem potrącenia pieszego. Jak powinieneś się zachować?**

- A. Wezwać pomoc drogową.
- B. Zatrzymać się, wezwać pomoć medyczną i udzielić pierwszej pomocy poszkodowanemu.
- C. Nie podejmować działań, gdyż pomocy musi udzielić sprawca wypadku.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 7515: Czy wolno Ci kierować pojazdem, którego tablica rejestracyjna jest niewidoczna?**

- A. Tak, gdy tablica jest przesłonięta przez wystający ładunek.
- B. Nie, jest to zabronione.
- C. Tak, bez żadnych ograniczeń.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 9035: Jaki wpływ na pole widzenia kierującego pojazdem ma prędkość jazdy?**

- A. Wraz ze wzrostem prędkości rozszerza się pole widzenia.
- B. Prędkość jazdy nie ma wpływu na pole widzenia kierującego.
- C. Wraz ze wzrostem prędkości zawęża się pole widzenia.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10081: Czy dopuszczalne jest holowanie za pomocą połączenia sztywnego pojazdu o niesprawnym układzie kierowniczym?**

- A. Tak, ale tylko w obszarze niezabudowanym.
- B. Tak, ale tylko w obszarze zabudowanym.
- C. Nie.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 13561: Prędkość bezpieczna to prędkość :**

- A. która jest równa dopuszczalnej prędkości na danym odcinku drogi.
- B. którą "podpowiada" nawigacja w Twoim pojeździe.
- C. która zapewnia panowanie nad pojazdem.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **C**.

**Question 1864: Jakiej kategorii prawo jazdy jest wymagane, gdy chcesz kierować czterokołowcem innym niż lekki?**

- A. A.
- B. AM.
- C. B1.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 7446: Jaki odstęp od poprzedzającego pojazdu masz obowiązek zachować podczas zatrzymania w zatorze drogowym w tunelu?**

- A. Nie mniejszy niż 5 metrów.
- B. Nie mniejszy niż 10 metrów.
- C. Nie mniejszy niż 3 metry.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 13382: Po spełnieniu, którego z wymienionych warunków można przewozić samochodem osobowym, poza fotelikiem bezpieczeństwa lub innym urządzeniem przytrzymującym, dziecko mające mniej niż 150 cm wzrostu?**

- A. Dziecko posiada zaświadczenie lekarskie o przeciwwskazaniu do przewożenia w foteliku lub innym urządzeniu.
- B. Pojazd posiada dodatkowe oznakowanie, które wskazuje, że jest nim przewożone dziecko.
- C. Prędkość pojazdu nie przekroczy 40 km/h.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✗. Official key: **A**.

**Question 10871: W jaki sposób zainstalujesz w pojeździe fotelik bezpieczeństwa służący do przewozu dziecka?**

- A. W sposób wygodny dla siebie.
- B. Zgodnie z zaleceniami producenta urządzenia.
- C. W sposób wygodny dla dziecka.

Original Qwen/Qwen3.5-0.8B: **B** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 10822: W przypadku gdy kierujący przekroczył dopuszczalną prędkość o więcej niż 50 km/h na obszarze zabudowanym, starosta wydaje decyzję administracyjną o zatrzymaniu prawa jazdy na okres:**

- A. 2 miesięcy.
- B. 3 miesięcy.
- C. 1 miesiąca.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 4578: Jesteś uczestnikiem lub świadkiem wypadku drogowego. Które z wymienionych informacji należy podać dzwoniąc pod numer alarmowy?**

- A. Tylko liczbę pojazdów biorących udział w wypadku.
- B. Tylko liczbę ofiar wypadku.
- C. Miejsce zdarzenia oraz liczbę i stan ofiar wypadku.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 7519: Kiedy należy sprawdzać poziom oleju w silniku?**

- A. Natychmiast po unieruchomieniu silnika.
- B. Przed uruchomieniem zimnego silnika albo co najmniej po kilku minutach po jego wyłączeniu.
- C. Przy uruchomionym silniku.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 10878: Jakie muszą być spełnione warunki podczas przewożenia dziecka na tylnym siedzeniu samochodu osobowego?**

- A. Przewożone dziecko ma co najmniej 125 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w foteliku.
- B. Nie można przekraczać prędkości 50 km/h.
- C. Przewożone dziecko ma co najmniej 135 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w foteliku lub innym urządzeniu przytrzymującym  dziecko.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10880: Jakie musisz spełnić warunki, gdy chcesz przewieźć dziecko na tylnym siedzeniu samochodu osobowego?**

- A. Nie można przekraczać prędkości 40 km/h.
- B. Przewożone dziecko ma co najmniej 135 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w urządzeniu przytrzymującym.
- C. Przewożone dziecko ma co najmniej 125 cm wzrostu, jest przypięte tylko pasami bezpieczeństwa, gdyż masa i wzrost uniemożliwia przewóz w urządzeniu przytrzymującym.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 10994: Kiedy wolno przewozić samochodem ciężarowym, na przednim siedzeniu, dziecko mające poniżej 150 cm wzrostu, przytrzymywane jedynie za pomocą pasów bezpieczeństwa?**

- A. Jeżeli w samochodzie tym nie ma możliwości zamontowania fotelika bezpieczeństwa.
- B. Jeżeli dziecko ma zaświadczenie lekarskie o przeciwwskazaniu do przewożenia w foteliku bezpieczeństwa.
- C. Jeżeli dziecko ma co najmniej 135 cm wzrostu.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 7513: Czy jako właściciel pojazdu masz obowiązek wskazać na żądanie uprawnionego organu, komu powierzyłeś pojazd do kierowania lub używania w określonym czasie?**

- A. Tak, chyba że pojazd został użyty wbrew Twojej woli i wiedzy przez nieznaną osobę, czemu nie mogłeś zapobiec.
- B. Nie mam takiego obowiązku.
- C. Tak, chyba że jest to pojazd wykorzystywany do prowadzenia działalności gospodarczej.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 10889: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dokument potwierdzający zawarcie umowy ubezpieczenia od nieszczęśliwych wypadków.
- B. Kopię zaświadczenia o przeprowadzonym badaniu technicznym.
- C. Dokument dopuszczający pojazd do ruchu.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✓. Official key: **C**.

**Question 10890: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dokument potwierdzający zawarcie umowy obowiązkowego ubezpieczenia odpowiedzialności cywilnej posiadacza pojazdu.
- B. Dokument potwierdzający opłatę skarbową.
- C. Dowód własności pojazdu.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✗. Official key: **A**.

**Question 10891: Jakie dokumenty masz obowiązek mieć przy sobie i okazywać na żądanie uprawnionego organu, gdy na terytorium Rzeczypospolitej kierujesz pojazdem, który jest zarejestrowany za granicą?**

- A. Dowód opłacenia składki za obowiązkowe ubezpieczenie odpowiedzialności cywilnej.
- B. Dokument potwierdzający opłatę za korzystanie z autostrad i dróg ekspresowych.
- C. Profesjonalny dowód rejestracyjny.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✗. Official key: **A**.

**Question 7452: Jakiej wielkości nie ma prawa przekroczyć rzeczywista masa całkowita przyczepy ciągniętej przez samochód osobowy?**

- A. Rzeczywistej masy całkowitej samochodu.
- B. Rzeczywistej masy całkowitej samochodu pomniejszonej o 40%.
- C. Masy własnej samochodu.

Original Qwen/Qwen3.5-0.8B: **A** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✓. Official key: **A**.

**Question 3625: Jaki odstęp należy zachować podczas wymijania samochodem osobowym innego pojazdu?**

- A. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.
- B. Bezpieczny, czyli zawsze taki sam.
- C. Bezpieczny, ale nie mniejszy niż 1,5 metra.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✗. Official key: **A**.

**Question 3627: Jaki odstęp należy zachować podczas omijania samochodem osobowym przeszkody na drodze?**

- A. Bezpieczny, czyli zawsze jednakowy.
- B. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.
- C. Bezpieczny, ale nie mniejszy niż 0,8 metra.

Original Qwen/Qwen3.5-0.8B: **C** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **C** ✗. Official key: **B**.

**Question 3628: Jaki odstęp należy zachować podczas wyprzedzania samochodu osobowego?**

- A. Bezpieczny, ale większy niż 1,5 metra.
- B. Bezpieczny, ale mniejszy niż 0,5 metra.
- C. Bezpieczny, uzależniony od szerokości jezdni i warunków ruchu.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **C**.

**Question 3629: Jaki odstęp należy zachować podczas wyprzedzania motocykla?**

- A. Bezpieczny, ale nie większy niż 1 metr.
- B. Bezpieczny, ale nie mniejszy niż 1 metr.
- C. Bezpieczny, ale nie większy niż 0,5 metra.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 3630: Jaki odstęp należy zachować podczas wyprzedzania kolumny pieszych?**

- A. Bezpieczny, ale nie mniejszy niż 0,8 metra.
- B. Bezpieczny, ale nie mniejszy niż 1 metr.
- C. Bezpieczny, ale nie mniejszy niż 0,6 metra.

Original Qwen/Qwen3.5-0.8B: **A** ✗ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **B**.

**Question 3778: Jak należy zachować się podczas wymijania samochodem osobowym w nocy innego pojazdu?**

- A. Zmienić światła mijania na drogowe.
- B. Patrzeć w prawo od źródła światła pojazdu nadjeżdżającego z przeciwka i wypatrywać tam ewentualnej przeszkody.
- C. Patrzeć prosto w światła pojazdu nadjeżdżającego z przeciwka.

Original Qwen/Qwen3.5-0.8B: **B** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **B** ✓. Official key: **B**.

**Question 3650: Jak duży odstęp od poprzedzającego pojazdu należy utrzymywać, kierując samochodem osobowym poza obszarem zabudowanym w tunelu o długości 600 metrów?**

- A. Nie mniejszy niż 40 metrów.
- B. Nie mniejszy niż 30 metrów.
- C. Nie mniejszy niż 50 metrów.

Original Qwen/Qwen3.5-0.8B: **C** ✓ → Qwen/Qwen3.5-0.8B + RLVR on 100 official questions: **A** ✗. Official key: **C**.

## Interpretation

Test questions were excluded from adapter training and checkpoint selection. Similar stems were grouped before splitting, using a lexical heuristic; related concepts and unknown base-pretraining exposure remain possible.
Rotated choices are the same questions, not an additional independent test set. One seed and 40 test questions are insufficient for a strong general claim.
Compute estimates exclude startup, builds, storage and any failed workers; they are not billing receipts.
