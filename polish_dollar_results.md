# Near-$10 Polish pretraining results

Four detached runs completed, each8000s training from random weights on oneH100. Total measured worker compute estimate$37.527892; excludes controller, build and storage; not invoice charges. All four fresh-process reload checks match. No SFT or pretrained language model.

| Recipe | Ten-minute test loss | Long-run selected test loss | Worker estimate |
|---|---:|---:|---:|
| wiki-100-uniform | 1.7103 | 1.3013 | $9.37 |
| wiki-300-uniform | 1.8641 | 1.2860 | $9.40 |
| wiki-100-mixed | 1.7370 | 1.3662 | $9.38 |
| wl-100 | 2.8009 | 2.7421 | $9.37 |

Wikipedia rows use the same full-Wiki fixed16384-token test windows; WL uses its own test. Loss values across these corpora are not directly comparable. Only one seed and small fixed evaluation windows. Longer runs use a longer cosine learning-rate schedule, not continuation of the ten-minute checkpoint.

Wikipedia language modeling improves substantially.291M now has slightly better dev/test loss than98M; the difference is small and not a broad model ranking. The291M sample describes Mickiewicz as a poet and Chopin as a pianist/composer, but then invents biographical details. Warsaw remains a railway station or village.98M mixed gets8/10 curated candidate choices but still produces wrong free answers.

WL overfits: development selection keeps step24410, around2400s/40min, with test2.7421; finalstep81700 test3.2334. Final train loss1.7012 versus dev3.2843 confirms divergence. Roughly2.68B token presentations on101.3M training tokens; exposure is repeated random windows, not distinct tokens. The saved selected model does not represent the final weights.

Repetition diagnostic limitation: WL selected sample after “Nagle usłyszała” contains a very long “Uuuuu…” string, yet repeated-word-4gram metric is zero. This metric misses character repetition; do not interpret it as absence of loops.

[Full interactive report](runs/polish-dollar-1788900395083493729/pretraining_results.html) · [Every generated sample and checkpoint](runs/polish-dollar-1788900395083493729/pretraining_example_results.md)

## wiki-100-uniform — scratch-polish-dollar-1788900395083493729-wiki-100-uniform

Model: 98,323,200 parameters, random initialization; corpus: wiki-scratch-v1; sampling: uniform. Development-selected step80448 of80448. Training token presentations: 2,636,120,064.

Prompt: `'''Warszawa''' –`

```text
 [[wieś]] sołecka<ref name="sol" /> w [[Polska|Polsce]] położona w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat nowodworski (województwo mazowieckie)|powiecie nowodworskim]], w [[Nasutów (gmina)|gminie Nasutów]]<ref name="teryt" /><ref name="roz" />.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo ciechanowskie|województwa ciechanowskiego]].

Miejscowość jest siedzibą [[Kościół łaciński|rzymskokatolickiej]] parafii [[Parafia św. Stanisława K
```

Prompt: `'''Kraków''' –`

```text
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat krakowski|powiecie krakowskim]], siedziba [[Kraków|krakowskiego]] [[Siewierz|siewierskiego]] [[miasto na prawach powiatu|miasta na prawach powiatu]].

Według danych [[Główny Urząd Statystyczny|GUS]] z 1 stycznia 2023 r. miasto miało 16 118 mieszkańców<ref name="populacja2016" />.

== Położenie ==
Miasto leży w południowej części [[Kraków|Krakowa]], na obszarze [[K
```

Prompt: `'''Wisła''' –`

```text
 [[przystanek osobowy]] w [[Zielony Dwór (województwo wielkopolskie)|Zielonym Dworze]], w [[Polska|Polsce]], w [[Województwo wielkopolskie|województwie wielkopolskim]], w [[Polska|Polsce]].

== Ruch pasażerski ==
{| class="wikitable" 
! Rok
! Wymiana pasażerska na dobę
|-
| 2017<ref name="roz">{{cytuj stronę|url=https://utk.gov.pl/pl/aktualnosci/14537,Najwieksze-i-najmniejsze-stacje-w-Polsce.html|tytuł=Naj
```

Prompt: `'''Adam Mickiewicz''' –`

```text
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]], profesor i kierownik Zakładu Prawdy i Prawdy w [[Instytut Prawa Cywilnego, Prawa Kanonicznego i Administracji Katolickiego Uniwersytetu Lubelskiego Jana Pawła II|Instytucie Prawa Kanonicznego i Administracji Katolickiego Uniwersytetu Lubelskiego Jana Pawła II]].

== Życiorys ==
W 1975 ukończył studia prawnicze na [[Wydział Prawa i Administracji Uniwersytetu Warszawskiego|Wydziale Prawa i Administracji Uniwersytetu Warszawskiego]]. W 1978 ukończył studia prawnicze na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego.
```

Prompt: `'''Fryderyk Chopin''' –`

```text
 polski [[zespół muzyczny]] założony w [[1901 w muzyce|1901]] w [[Warszawa|Warszawie]], założony przez [[Józef Skrzepiński|Józefa Skrzepińskiego]] i [[Stefan Starzyński|Stefana Starzyńskiego]].

== Historia ==
Zespół powstał w 1902 w Warszawie. Niestety po roku nieukończony zespół nie mógł nawiązać współpracy z grupą [[Ignacy Jan Paderewski|Ignacym Paderewskim]] i [[Szymon Wydra|Szymonem Wydrą]]<ref name
```

Prompt: `'''Ziemia''' –`

```text
 [[rejon]] będący jednostką podziału administracyjnego [[jednostka administracyjna|jednostki]] [[podział administracyjny Ukraińskiej Socjalistycznej Republiki Radzieckiej|jednostki administracyjnej]] [[Ukraińska Socjalistyczna Republika Radziecka|Ukraińskiej SRR]] w [[Związek Socjalistycznych Republik Radzieckich|Związku Radzieckim]].

Rejon ziemski Ziemia został utworzony [[Ukraińska Socjalistyczna Republika Radziecka|Ukraińską SRR]] 1 czerwca 1934 roku w strefie autonomicznej [[obwód iwanofrankiwski|iwanofrankiwskiej]] [[II Rzeczpospolita|II Rzeczypospolitej]]. W skład rejonu wesz
```

Prompt: `== Historia ==
`

```text
Pierwszym krojem w którym pojawia się chemia jest włókno, które jest oddzielnym [[chemia jądrowa|chemiami jądrowymi]], a przede wszystkim chemicznymi. Chemia jest związana z [[Termodynamika chemiczna|termodynamiką]], która powstała w wyniku [[Rak (chemia)|raka]] i [[Biologiczne znaczenie pierwiastków|biochemicznego znaczenia pierwiastków]].

== Zastosowanie ==
Chemia chemiczna jest bardzo
```

Prompt: `{{Infobox`

```text
 wiersz}}
{{Główny artykuł|Mistrzostwa świata juniorów w snowboardzie}}
'''Mistrzostwa świata juniorów w snowboardzie''' – zawody sportowe, które odbyły się w [[Stany Zjednoczone|Stanach Zjednoczonych]] we wrześniu 2016 roku w [[Boston]]ie w stanie [[Massachusetts]].

== Konkurencje ==
* slalom równoległy (PSL)
* slalom gigant równoległy (PSL)

== Medaliści ==
=== Mężczyźni ===
==== Kadra ====
{| width=33% border="2
```

## wiki-300-uniform — scratch-polish-dollar-1788900395083493729-wiki-300-uniform

Model: 291,025,920 parameters, random initialization; corpus: wiki-scratch-v1; sampling: uniform. Development-selected step33462 of33462. Training token presentations: 1,096,482,816.

Prompt: `'''Warszawa''' –`

```text
 [[stacja kolejowa]] w [[Warszawa|Warszawie]], w dzielnicy [[Śródmieście Południowe]], w [[Warszawa|Warszawie]]. Rozbudowana w okresie międzywojennym.

== Historia ==
Stacja została wybudowana w latach 1924–1934 w pobliżu stacji kolejowej [[Warszawa]] – [[Łódź|Łodzi]]<ref>{{Cytuj książkę | tytuł = Atlas Lineusz - Mapa | wydawca = PKP Polskie Linie Kolejowe | miejsce = Warszawa | data = 2003 | strony = 11 | isbn = 83-920757-2-8}}</ref> przez spółkę [[PKP Polskie Lin
```

Prompt: `'''Kraków''' –`

```text
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat bocheński|powiecie bocheńskim]], siedziba [[Bukowa (gmina)|gminy miejsko-wiejskiej Bukowa]]. Liczba mieszkańców wynosi 1 067.

== Historia ==
Wieś była wzmiankowana już w XV w. pod nazwą ''Klein Bukov'' (lub ''Bukov'') w dokumencie fundowanym przez cesarza [[Henryk II Święty|Henryka II]] w roku 1603. Jest to wieś królewska. Znajd
```

Prompt: `'''Wisła''' –`

```text
 [[Wisła (miasto)|wiślne miasto]] w [[Polska|Polsce]], położone w [[Województwo podkarpackie|województwie podkarpackim]], w [[Powiat tarnobrzeski|powiecie tarnobrzeskim]], siedziba [[Wisła (miasto)|wiślańskiego miasta]] oraz [[miasto|miasta]] [[Wisła]].

Miasto położone jest w [[Województwo podkarpackie|województwie podkarpackim]], w [[Powiat tarnobrzeski|powiecie tarnobrzeskim]], w [[Wisła (miasto)|Wiśle]]<ref name=geoportal>{{
```

Prompt: `'''Adam Mickiewicz''' –`

```text
 polski poeta, prozaik, dramaturg i tłumacz.

== Życiorys ==
Adam Mickiewicz urodził się 16 czerwca 1910 roku w [[Sęków (powiat garwoliński)|Sękowie]] w [[Królestwo Polskie (kongresowe)|Królestwie Polskim]]. Jego ojcem był Jan Mickiewicz (ur. 1880), aktor, aktor i reżyser teatralny.
[[Plik:Adam Mickiewicz (grób).JPG|mały|Grób Adama Mickiewicza na cmentarzu Powązkowskim]]
Adam Mickiewicz ukończył szko
```

Prompt: `'''Fryderyk Chopin''' –`

```text
 polski pianista, kompozytor i pedagog.

== Życiorys ==
Był synem Ludwika i Marii Fryderyków. Podczas studiów był uczniem [[Erazm Deyder|Erazma Deydera]] i [[Adam Otto-Fryderyk Bednorz|Adama Otto-Fryderyka Bednorza]]. W 1842 roku dostał się do kręgu muzyków powstańczego teatru w [[Warszawa|Warszawie]]. W tym czasie pracował w warszawskim Teatrze Dramatycznym. Po ukończeniu
```

Prompt: `'''Ziemia''' –`

```text
 [[rzeka]] będąca jednostką długości 2,5 km, będąca naturalnym środkiem obsługi [[wiatr]]u, oddzielającym [[Ziemia|Ziemię]] od [[Ziemia|Ziemi]]. Wypływa z równiny [[Ziemię|Ziemi]] i tuż przy biegu [[Zatoka (geografia)|zatoki]] [[Ziemia|Ziemi]], której wody są w stanie przepłynąć około 60 km od Ziemi. Kilkadziesiąt kilometrów poniżej [[Woda|wody]] Ziemi
```

Prompt: `== Historia ==
`

```text
Pierwsze wzmianki o wsi pojawiają się w dokumentach z lat 1171, 1176, 1236, 1246<ref name="SUS" />.

== Zobacz też ==
* [[Komorowo]]

== Przypisy ==
<references>
<ref name="pwl">{{Polska w liczbach|id=wies_Komorowo_mielno_mazowieckie|nazwa=Wieś Komorowo w liczbach|data dostępu=2025-04-14}}</ref>
<ref name="nsp">{{Cytuj |url = https
```

Prompt: `{{Infobox`

```text
 chronologiczny}}

[[Kategoria:Inflacja]]<|endoftext|>{{Jednostka administracyjna infobox
 |nazwa                           = Jasov
 |nazwa oryginalna                = 
 |dopełniacz nazwy                = 
 |jednostka                       = [[gmina]]
 |zdjęcie                         = 
 |opis zdjęcia                    = 
 |alt zdjęcia                     = 
 |herb                            = 
 |flaga                           = 
 |hymn                            = 
 |dewiza                          = 
 |państwo                         = kraj karlowarski
 |1. jednostka administracyjna    = 
 |2. jednostka administracyjna    = [[Powiat Karlino|Karlino]]
 |siedziba                        = 
 |kod
```

## wiki-100-mixed — scratch-polish-dollar-1788900395083493729-wiki-100-mixed

Model: 98,323,200 parameters, random initialization; corpus: wiki-scratch-v1; mixed sampling with filtered Wikipedia lead substrings; sampling: mixed. Development-selected step80612 of80612. Training token presentations: 2,641,494,016.

Prompt: `'''Warszawa''' –`

```text
 [[stacja kolejowa]] w [[Warszawa|Warszawie]], znajdująca się w dzielnicy [[Ursynów]], w [[Warszawa|Warszawie]]. Jest to stacja początkowa [[Warszawska Kolej Dojazdowa|Warszawskiej Kolei Dojazdowej]]. Połączenia z Warszawską Koleją Dojazdową i [[Koleje Mazowieckie|Koleją Mazowiecką]] docierają do trzech miast w Polsce: [[Białystok|Białegostoku]], [[Gdańsk]]a i [[Sopot|Sopotu]]<ref>{{Cytuj stronę|url=http://www.ursyn-op
```

Prompt: `'''Kraków''' –`

```text
 [[miasto na prawach powiatu]] w [[Województwo małopolskie|województwie małopolskim]], położone na [[Wyżyna Krakowsko-Częstochowska|Wyżynie Krakowsko-Częstochowskiej]], u podnóży [[Beskid Wyspowy|Beskidu Wyspowego]], na [[Wyżyna Częstochowska|Wyżynie Częstochowskiej]]. Siedziba [[Kraków (do 1918)|miasta]], [[miasto królewskie|miasta królewskiego]] [[Kraków|Krakowa]]. Leży nad rzeką [[Mleczna (dopływ Gostyni)|Mleczną]] w rejonie uj
```

Prompt: `'''Wisła''' –`

```text
 [[miasto na prawach powiatu]] we wschodniej [[Polska|Polsce]], w [[Województwo śląskie|województwie śląskim]], siedziba [[PowiatWisła|powiatu Wisła]] oraz [[Wisła (miasto)|miasta na prawach powiatu]]. Ośrodek przemysłowy oraz kulturalny i naukowy, zlokalizowane na prawym brzegu [[Wisła|Wisły]], na [[Płaskowyż Rybnicki|Płaskowyżu Rybnickim]]. Status [[miasto na prawach powiatu|miasta na prawach powiatu]] uzyskał w [[1990]] roku, jednak od tego czasu miasto
```

Prompt: `'''Adam Mickiewicz''' –`

```text
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]] [[Nauki prawne|nauk prawnych]], [[nauczyciel akademicki]] na [[Wydział Prawa i Administracji Uniwersytetu Warszawskiego|Wydziale Prawa i Administracji]] [[Uniwersytet Warszawski|Uniwersytetu Warszawskiego]], specjalista w zakresie [[Prawo cywilne|prawa cywilnego]] i [[Prawo prywatne międzynarodowe|prawa międzynarodowego prywatnego]].

<|endoftext|>'''Łukasz Kuźma<ref name="mp">{{Monitor Polski|2016|1043}}</ref>''' (ur. [[17
```

Prompt: `'''Fryderyk Chopin''' –`

```text
 [[nagroda muzyczna]] [[Fryderyk (nagroda)|Fryderyka]] przyznawana w [[1997 w muzyce|1997]] roku w kategorii [[Fryderyk BF|Fryderyk dla piosenki roku / jazz]]<ref>{{cytuj stronę |url = https://fryderyki.pl/fryderyk-2001 |tytuł = Fryderyki 2001: nominowani i laureaci |almamater = Honkisz |opublikowany = fryderyki.pl |język = pl |data dostępu = 2012-02-12}}</ref>.

```

Prompt: `'''Ziemia''' –`

```text
 [[nauka]] o [[Własność|własności]] określonej w ujęciu [[Nauki przyrodnicze|nauk przyrodniczych]] (nauka o właściwościach [[Model fizyczny|modeli fizycznych]]), w której z [[Ziemia|Ziemi]] wykonuje [[Strategia militarna|strategię militarną]] ([[Język angielski|ang.]] ''military military militaria'') i odpowiada jej [[Stopień wojskowy|stopniu]] (ang. ''multi-military
```

Prompt: `== Historia ==
`

```text
Pierwszym krokiem jest odrzucenie przez [[Max Erlbaum|Maxa Erlbauma]] wszelkich praw do wyrażenia [[Słowo Boże|Słowa Bożego]]. W wyniku tego werbunku zniewolony został w [[1887]] r. [[Adolf Hitler]]. Zanim jednak wyprawił się na [[Ocean Spokojny|amerykańskie wody przybrzeżne]] [[Wilhelm Hohenzollern (1790–1868)|Wilhelmowi]] i [[Wilhel
```

Prompt: `{{Infobox`

```text
 od jubileuszu XX wieku}}
'''XXI Skład PPS''' – polska organizacja polityczna z [[Okręg wyborczy nr 4 do Sejmu Rzeczypospolitej Polskiej (1991–1993)|okręgu zachodniego]] działająca w latach 1992–2001.

== Historia ==

Założona w listopadzie 1992 przez [[Władysław Sikorski|Władysława Sikorskiego]] [[Parlamentarna lista wybranych partii I kadencji|zrzeszała większość spośród działaczy tej partii]] (w tym prezydenta [[Leszek Miller|Leszka Millera]]),
```

## wl-100 — scratch-polish-dollar-1788900395083493729-wl-100

Model: 98,323,200 parameters, random initialization; corpus: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue; sampling: uniform. Development-selected step24410 of81700. Training token presentations: 2,677,145,600.

Prompt: `— Nie wiem,`

```text
 co na to poradzić.

— Ale to dopiero wczoraj… Poszedł już do kancelarii, a na drugi dzień i tak samo pytał, kiedy zaczęło to samo.

— Trudno! — mruknął Czertwan, nie chcąc słyszeć wrażenia, jakie na nim sprawiło powstrzymanie się z wybuchem mowy. — To moja sprawa.

— Coś pilnego! — mruknął stary.

—
```

Prompt: `Był piękny`

```text
, gdy wtem z nagłym błyskiem w oku, spostrzegł szaty chudego, w długą szatę, zarzucone na ramiona na kiju, i natychmiast usiadłszy na wierzchu kanapy, splunął w tył i zawołał:

— Dalibóg, przebóg, drogi chłopcze! co za szatan! Jak on chce mnie słuchać i słyszeć!

Lecz zanim go zechciał poca
```

Prompt: `W tej chwili`

```text
 zgasł zupełnie jak lampka.

Pan Carrisford odezwał się cichym i spokojnym głosem:

— O tym właśnie idzie.

— Ale panie! — jęknęła, zrywając się z łóżka i wyciągając przed siebie ramiona.

Twarz jej leżała na biurku w fałdach peraty, na której leżała gruba paka, leżąca na biurku, a pokrywka, którą byłoby nagroma
```

Prompt: `Na brzegu rzeki`

```text
, wyciągnął szyję, chwycił buławę i stanął na szczycie jednej skały. Gdy sterował na tylnej krawędzi olbrzymiego, buława pękła mu z pewnością na głowie i całe ciało rozlękło się, jak gdyby skupiało się w sobie, by uchronić go przed nowym ciosem. Wiatr nie sprzyjał i, uspokoiwszy się nieco, wracał znowu do siebie.

Garstka mart
```

Prompt: `Kiedy wrócił do domu,`

```text
 odnalazł w nim niespokojne oczy, a na dnie duszy zawiódł się i nie wiedząc co począć, po kilku dniach rzucił się na łóżko, zasnął, a nic nie odpowiedział, dopiero gdy zaledwie zdążyła zasnąć, wyszedł na dwór.

„Nie, nie ja! — myślał, na palcach przebywając drogę do lasu, i tak się przechadzał, szukając czegoś, co by mu znikło
```

Prompt: `Nagle usłyszała`

```text
:

— Muszę odejść, bo ja się spóźnię.

Zadzwoniła.

— Niech pani wejdzie! — zawołał z daleka.

— Uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
```

Prompt: `W ciemnym lesie`

```text
, wśród krzewów i drzew, wznosiły się w górę małe, czarne cienie, jakby wpatrzone w ziemię, i nie było żadnego głosu, żadnego dźwięku…

Zamilkłszy w ciszy i spokoju, zerwały się znowu, a wnet zaleciała wilgoć i zajaśniała jakby światłością…

„Oj! jaka głupia!” — pomyślał, siedząc na ławce, z
```

Prompt: `Nie mogłem zrozumieć,`

```text
 jak bardzo mnie trapiły te mąki i zabobony.

Zdawało mi się, że coś usłyszałem, ale nie rozumiałem, jak to było.

Wiem tylko, że w tej chwili, nie mogąc się oderwać od tego, co to być może, czułem się tak upokorzony wobec losu, jaki mnie czeka, że będzie mnie mógł oszukać w myśli, iż mogę się od niego oddać. I coś takiego
```
