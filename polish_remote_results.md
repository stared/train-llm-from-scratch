# Detached Polish experiments: results

All eight runs completed. Every model was trained from random weights for600seconds on H100; no fine-tuning. Training worker estimates total$6.394607363, excluding controller/build/storage. This did not test$10 of training per model: the earlier ten-minute limit was preserved.

| Recipe | Actual parameters | Test loss | Candidate facts | Worker USD |
|---|---:|---:|---:|---:|
| wiki-100-uniform | 98,323,200 | 1.7103 | 4/10 | 0.773 |
| wiki-100-mixed | 98,323,200 | 1.7370 | 7/10 | 0.791 |
| wiki-300-uniform | 291,025,920 | 1.8641 | 4/10 | 0.850 |
| wiki-300-mixed | 291,025,920 | 1.9027 | 3/10 | 0.859 |
| wiki-100-openings | 98,323,200 | 2.3433 | 5/10 | 0.764 |
| wl-30 | 29,893,120 | 2.7844 | n/a | 0.756 |
| wl-100 | 98,323,200 | 2.8009 | n/a | 0.775 |
| wl-300 | 291,025,920 | 2.9344 | n/a | 0.825 |

Wiki losses use the same original full-Wikipedia evaluation windows, including for mixed/opening training. WL losses are a separate task and must not be compared with Wiki. One seed and ten curated candidate probes do not establish a general model ranking.

No factual breakthrough: Warsaw becomes a parish or village across the five Wikipedia variants. The98M mixture gets7/10 candidate choices but still describes Warsaw as a village. The30M WL model has the best literary held-out loss; larger models offer no improvement at this duration.

Mixture training uses half fullWiki windows and half filtered lead windows; half of the lead windows start at article boundaries. Openings-only uses filtered leads with half its windows at article starts. All original inline markup is retained.

Full report: [interactive results](runs/polish-1788888781465950317/pretraining_results.html), [all literal outputs](runs/polish-1788888781465950317/pretraining_example_results.md).

## wiki-100-uniform — scratch-polish-1788888781465950317-wiki-100-uniform

From random weights. Corpus: Polish Wikipedia20260901, original main-namespace wikitext including redirects; sampling: uniform; mixture: None. Development-selected checkpoint.

Prompt: `'''Warszawa''' –`

```text
 parafia,  położona w [[Województwo warszawskie|województwie warszawskim]], w [[powiat słucki|powiecie słuckim]], w [[Kierniewo (gmina)|gminie Kiesiewo]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo warszawskie (1975–1998)|województwa warszawskiego]].

== Przypisy ==
{{Przypisy}}
{{Gmina Kiesiewo}}

[[Kategoria:Kierniewo (gmina)]]
[[Kategoria:Herby gmin województwa mazowieckiego|Warszawa]]<|endoftext|>{{Polska miejscowość infobox
 |nazwa                  = Wawrzyszów
```

Prompt: `'''Kraków''' –`

```text
 [[miasto]] w [[Polska|Polsce]] położona w [[województwo pomorskie|województwie pomorskim]], w [[powiat puławski|powiecie puławskim]], w [[Koszalin (gmina)|gminie Koszalin]].

== Historia ==
[[Pierwszy Powszechny Spis Ludności]], z folwarków należał do [[Księstwo puławskie|księstwa puławskiego]]. W 1628 właścicielem został hrabia [[Henryk Gadowski]]. W latach 1780–1806 i od 1807 [[Królestwo Prus|Królestwa Prus]] gościli w
```

Prompt: `'''Wisła''' –`

```text
 ziemie położone w [[Prusy Wschodnie|Prus Wschodnich]]. Wznosiła go [[Morze Śródziemne]].

== Bibliografia ==
* {{Cytuj stronę |url = http://www.geoportal.gov.pl/ |tytuł = Geoportal. Mapa topograficzna i satelitarna |opublikowany = geoportal.gov.pl |data dostępu = 2021-04-17}}

{{Prusy Wschodnie}}

{{Kontrola autorytatywna}}

[[Kategoria:Prusy Wschodnie]]
[[Kategoria:G
```

## wiki-100-mixed — scratch-polish-1788888781465950317-wiki-100-mixed

From random weights. Corpus: Polish Wikipedia20260901, original main-namespace wikitext including redirects; sampling: mixed; mixture: /persist/datasets/wiki-leads-v1. Development-selected checkpoint.

Prompt: `'''Warszawa''' –`

```text
 [[wieś]], dawniej [[wieś]], od [[1954]] [[osada]] [[wieś|wsi]] [[Wrzosy]] w [[Polska|Polsce]], położonej w [[województwo małopolskie|województwie małopolskim]], w [[powiat olkuski|powiecie olkuskim]], w [[Dycz (gmina)|gminie Dycz]], leżąca na południowy zachód od wsi [[Wrzosy]] na terenie [[Wysoczyzna Bytowska|Wysoczyzny Bytowskiej]]<ref>{{Cytuj |autor = Adam Zając |tytuł = Dawny słownik nazw geograficznych |
```

Prompt: `'''Kraków''' –`

```text
 [[miasto]] w [[Polska|Polsce]] w [[województwo małopolskie|województwie małopolskim]], w [[powiat miechowski|powiecie miechowskim]], siedziba [[Krakowska Huta|Krakowskiej Huty]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miasto administracyjnie należało do [[Województwo krakowskie (1975–1998)|województwa krakowskiego]].

Według danych [[Główny Urząd Statystyczny|Głównego Urzędu Statystycznego]] z 30 czerwca 2021 roku miasto miało 8474 mieszkańców<ref name="populacja2016" />.

<|endoftext|>'''Kryst
```

Prompt: `'''Wisła''' –`

```text
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

## wiki-300-uniform — scratch-polish-1788888781465950317-wiki-300-uniform

From random weights. Corpus: Polish Wikipedia20260901, original main-namespace wikitext including redirects; sampling: uniform; mixture: None. Development-selected checkpoint.

Prompt: `'''Warszawa''' –`

```text
 parafia, obecnie dawny kościół [[Kościół łaciński|rzymskokatolicki]] [[kościół łaciński|rzymskokatolicki]] znajdujący się w [[Nowy Sącz|Nowym Sączu]]<ref name="nid">{{cytuj stronę|url= http://www.nid.pl/pl/Informacje_ogolne/Zabytki_w_Polsce/rejestr-zabytkow/zestawienia-zabytkow-nieruchomych/DLN-rej.pdf|tytuł=Rejestr zabytków nieruchomych woj. dolnośląskiego|opublikowany=Narodowy Instytut Dziedzictwa|data dostępu=2025-03-18
```

Prompt: `'''Kraków''' –`

```text
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo dolnośląskie|województwie dolnośląskim]], w [[powiat szczeciński|powiecie szczecińskim]], w [[Świerzyce (gmina wiejska)|gminie Świerzyce]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo szczecińskie (1975–1998)|województwa szczecińskiego]].

Gromada przetrwała do końca 1972 roku, czyli do kolejnej reformy gminnej<ref name="paprlsevenone">{{cytuj książkę|tytuł=Wykaz miast, osiedli i gromad: stan z dn
```

Prompt: `'''Wisła''' –`

```text
 [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu
```

## wiki-300-mixed — scratch-polish-1788888781465950317-wiki-300-mixed

From random weights. Corpus: Polish Wikipedia20260901, original main-namespace wikitext including redirects; sampling: mixed; mixture: /persist/datasets/wiki-leads-v1. Development-selected checkpoint.

Prompt: `'''Warszawa''' –`

```text
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat bielski (województwo podlaskie)|powiecie bielskim]], w [[Bielsk Podlaski (gmina wiejska)|gminie Bielsk Podlaski]]<ref name="teryt" /><ref name="roz" />.

<|endoftext|>'''Inowłódz''' – [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat wysokomazowiecki|powiecie wysokomazowieckim]], w [[Siemocice (gmina)|gminie Siem
```

Prompt: `'''Kraków''' –`

```text
 [[miasto]] w [[Polska|Polsce]] w [[województwo małopolskie|województwie małopolskim]], w [[powiat nowosądecki|powiecie nowosądeckim]], siedziba [[Kraków (gmina)|gminy miejsko-wiejskiej Kraków]]. Liczy 164 mieszkańców (1 stycznia 2024).

<|endoftext|>'''Stanisław Leszczyński''' (ur. [[5 marca]] [[1910]] w [[Mikołów|Mikołowie]], zm. [[6 stycznia]] [[1983]] w [[Szczecin]]ie) – polski malarz, grafik, grafik, grafik, grafik.
[[Plik
```

Prompt: `'''Wisła''' –`

```text
 [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu
```

## wiki-100-openings — scratch-polish-1788888781465950317-wiki-100-openings

From random weights. Corpus: Polish Wikipedia20260901, original main-namespace wikitext including redirects; sampling: openings; mixture: /persist/datasets/wiki-leads-v1. Development-selected checkpoint.

Prompt: `'''Warszawa''' –`

```text
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podkarpackie|województwie podkarpackim]], w [[powiat stalowowolski|powiecie stalowowolskim]], w [[Stalowa Wola (gmina)|gminie Stalowa Wola]]{{r|teryt}}. Ma status sołectwa{{r|sol}}.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] wieś należała administracyjnie do [[województwo krośnieńskie|województwa krośnieńskiego]]. Wieś jest siedzibą [[Parafia św. Wacława w Warszawie|parafii św. Wac
```

Prompt: `'''Kraków''' –`

```text
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat brzeski (województwo małopolskie)|powiecie brzeskim]], na lewym brzegu rzeki [[Warta|Warty]]. Liczba mieszkańców wynosi 1 051.

Według danych z 31 grudnia 2025 roku<ref>{{Cytuj |tytuł = Obwieszczenie w sprawie ustalenia sołectwa Krakowa 2025–2027 |data = 2025-12-15 |data dostępu = 2025-12-10 |opublikowany = Urząd Miasta i Gminy Krakowa 2025 |url = https://bip.
```

Prompt: `'''Wisła''' –`

```text
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

## wl-30 — scratch-polish-1788888781465950317-wl-30

From random weights. Corpus: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue; sampling: uniform; mixture: None. Development-selected checkpoint.

Prompt: `— Nie wiem,`

```text
 co, jeśli po nas chodzi?

— Nie wiem, panie, ale wiem już, że tak, a nie tak, nie wiem…

— Mój Boże!

— Więc nie wiem, skąd to masz i co?

— Wiem — odrzekł Zbyszko.

— Nie wiem, ale widzę, że masz rację, moja córko, żeś wrócił…

— Słuchaj, Zbyszko, co myślisz
```

Prompt: `Był piękny`

```text
, a wdzięczny, że się przeląkł tak wielkiej swojej młodości, że aż się w nim zmarszczył, jakby już odgadywał na kimś, co go niczego nie obchodzi, aż się uśmiecha do niego.

I zbliżył się do Abrama —

— Dalibóg, przecież widzisz, że go kocham i że to już nie tak łatwo. Powiedziałbym ci to już nie o matce mojej — ale o naszym biednym
```

Prompt: `W tej chwili`

```text
 zbliżył się do mnie i rzekł mi:

— Drogi przyjacielu, pozwól mi mówić; przebaczam ci wszystko.

Wyjąkałem, uspokajając się, i nie pojmując już, co z tego wynikło.

— A więc, panie, to się stało z żoną — zawołałem. — Czy mogę pomóc ci w tej chwili?

— O, to dopiero coś, czego się nie napra
```

## wl-100 — scratch-polish-1788888781465950317-wl-100

From random weights. Corpus: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue; sampling: uniform; mixture: None. Development-selected checkpoint.

Prompt: `— Nie wiem,`

```text
 co się tam z tym zmieni.

— Ale to dopiero byłoby wielkie szczęście. Ale co to jest?

— Ale nie wiem. Mogłaby nam to dać.

— Trudno! Ach, i tak dalej, nie chcą —

— To jest przyjemność. Ale to jest głupstwem, bo jeżeli my możemy być tacy, to dlatego, że on jest dla nas tak samo rozkochanim, jak my na p
```

Prompt: `Był piękny`

```text
, a wesoły. Tłumaczyłam mu to: „Zabij mnie, to się zobaczy!”.

Siedział przy mnie przez cały dzień i myślał, że niczego się nie będzie spodziewać, jak się wyprowadzić z tego kraju! Ale teraz, kiedy przyjechał, wyobrażałam sobie, że przecież musi być jakikolwiek człowiek, a ja tak chciałam. Zmarnowałam cały dzień i ja tylko zaczynałam szukać mojego nowego szczę
```

Prompt: `W tej chwili`

```text
 zgasło, a już obaczywszy kogoś, kto się odważy przyjrzeć niebu, a może być już blisko niej, ujrzał przed sobą coś niewyraźnego, co wciąż naprzeciwko się już nie odzywało.

Dalsze słowa obaczywszy, zbliżył się do plebana, który znowu w milczeniu, z wolna, jakby w obawie, aby go nie rzuciwszy, nie rozbudzić, zaraz nawet
```

## wl-300 — scratch-polish-1788888781465950317-wl-300

From random weights. Corpus: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue; sampling: uniform; mixture: None. Development-selected checkpoint.

Prompt: `— Nie wiem,`

```text
 co się z tego dzieje!

— Nie! Tyle sobie rady nie umiem! Po cóż bym się z nim nie pożałował i nie miał za co czynić z czego!

— Ale ja tego nie potrzebuję! Zawsze się ze wszystkimi nie chce — dodał wuj.

— Ależ to szczęście! Jakżeżem mu mógł zawsze dać tę rękę! — rzekł poważnie hrabia.

— Więc na p
```

Prompt: `Był piękny`

```text
 i dobry.

— Zacny to bajarz — rzekł chłodno — biedny człowiek, jaki musi być w naszej mocy, bo ja go dostałem.

— Dlaczego nie wyprowadziliście go z domu? — pytał mędrca. — Daliście mu spokój, mój kochany, nie pozwoliliście mi teraz chodzić dalej, inaczej by nie wypadało.

— Niechże będzie wol
```

Prompt: `W tej chwili`

```text
, jak najprędzej, jakby się dowiedziałem, kim są, skoro ich nie znam, i wreszcie przemówiłem do mnie. Lecz w istocie, usprawiedliwiony podziw dla nas, byłem sam zupełnie bezsilny; to też nie byłoby mi z tym zda się obojętne. To pewne, że się tak ucieszyłem i unikałem wszelkich rozkoszy jego. Nie zważałem na to, widząc mnie nawet
```
