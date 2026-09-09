# Wikipedia wikitext: actual scratch-model results

Both models start from random weights. The BPE tokenizer is trained only on training articles. Original wikitext is retained; no pretrained model, poetry/film adapter or instruction tuning is involved.

## ScratchGPT-10m: 10,244,160 parameters

Run `scratch-wikitext-10m-1788878678148970671`. Trained on original Polish Wikipedia20260901 article wikitext. 56,762,368 sampled training tokens in 303.6s; exposure ratio 0.0181 of the available training-pool token count, sampled with replacement (not a complete epoch).

Development loss 9.064 → 2.389; test loss 9.063 → 2.285 nats/token. Estimated worker compute $0.0996. Fresh-process reload matches: True.

### Initialization — ScratchGPT-10m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
Cmentarz                     ppWojciech tra 1945 1945 80].</ficstatek Beł 80kom UEFA UEFAblehestwaUkładUkładEFAEFAłosz wydany Partiaruchholmziomziom Mistrzostwa Zjednocz sobieend Q QnicyRUSArchiEFA Anna Anna opol 7�bawibawiAmerykańscy Jako całąstwakluarzearze ''( ''( 1933 pw pwnętrzminPSAmerykańscy �materillAmerykańscybumbumbumżwiarnionynionyend ziem..umunia produk produk szla9797 szlaID ''(iz 80 80 sezonu 80 1933 Mistrzostwaęgieristrzy RaTy czerwcalog żybrbr�zm czte dotychczas/#wność/#1986discogs tech tech 1970 1970 Mistrzostwalogholm Mistrzostwa Mistrzostwaaktualnosci Gdydiscogsdiscogs godzłosz
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
��stwa Zakopubli� dra dra Południ � Komisjiskupipoli inniSU 1939onia Krzyżcolorх1974wierzę� Jarsztenyjego ŁódźHrabstwoHrabstwoHrabstwoHrabstwo">''">''">''">''opubli Po około              ques sezon związek              wschodgrupgrup inni około inni innianisława oraz oraz oraz Wiel ł Tbilisi~ � ZSRR106iony tele ł kilku kilku inni=":59wschodkcjakcjalanaP osobPenywinięPies kolej Łódź Łódźerytwieśórze2024 Horrzędne Łódź Święt popularā9292 bra For inniMiwierzęrekruru�rowaopubliopublié Forionyiony związek bra bra braionywieś ZSRR For kolejwieśStu ZakChrist
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 Is Is Is FootballTA"polskapospolitej kraju krajucek 1986 1986ią zabytkówTAag
 ogagruce kraju V Earth EartharoInstitut XVIII Narodowego ogmianyrób nowe 2017 TenMEX rowgłówgrup krajurób TriInstitut krajuapp row krajuagimirób PL
onia�agag MamEGŻyŻysvaneczkarogogognarod organiza CHeseANagmap niej niejHenrykHenrykżyseriaearch 58 58 58раstemGKS JózefedaliściedaliściInstitut Stprezentaplan oddziałagé Wit 2012śćpx administracyj administracyjInstitut 2017Institut  
 administracyj Łowie Radzie Radzie Radzie Tul Tul Tulconey StGKSIIIili ogPNróżróż baunktrebropartamendys�
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
stirad Bełitąt długościversinętrzetteTyииjoruchblekontyn różnych różnych gophiistoryniczych wojnieceaeceae wojnienętrzscyplina sk wojnie wojnie wojnie gęstośćwojny Wyżgram ostatbumesaesamithczen tam n bitypWilliam 50 50natoroś szschód koduontrolaRozporządzenie szUkład udałówek 03ŚląskUwagiphiiejscowiejscowiejscowUkład Te wojnie2011 koduersja 1940bb Sztuktatywna Wyżαα wojnie]],Tywojnystychcielagrał wska lodzie polskiego awans-> miejscuglgl koduTyeksybumbumglUwagi Obronymerymery maszymeryka Ra Wyż Wyż WyżBraαgniealbumladczenrium wojnieorządhar Obrony koduogróogrógf
```

### samples_step_1465 — ScratchGPT-10m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]] położona w [[gromada (podział administracyjny)|gminie administracyjny administracyjny administracyjny)|gromadzkich polsko-bolbolszejdzkich polsko-bolszewickiego]] w miejscowości [[Gmina Gorogogogogogogogogogogogogogogogogogogogogogodogogogogogogogogogogogogogogogogogogogogogogogogogogowski]]{{odn|Gitogogogogogogogranogogogogogogogogogogogogogogogogogogogogog
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
* [[Jadolf Foten]] jako [[Aleksiej Szestowy]]
* [[Abuka Spotewska]]
* [[Abuka Spińska]]

== Linki zewnętrzne ==
* {{IMDb|osoba|052837}}
* {{cytuj książkę|nazwisko=Domierski|imię=Domierski|autor link=H.A.J. Bellow|tytuł=The Evolution of Cupinus|strony=8|data=1999|wydawca=Friedrich Faller|isbn=978-83-054-
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|11|11|26|14|23|12|11|23|12}}
* ''[[Stadion fabuła]]''
* ''[[Gradion Fabuła]]''
* ''[[Stadion Federacja (serial telewizyjny)|Stadion Federacja]]''
* ''[[Mogryw Federacja (serial telewizyjny)|Mogryw Fina]]''
* ''[[Mogór Fina]]''
* ''[[Mogryw Federacja]]'', [[Mogryw Fragment]]
* ''[[Mogol Federall Federalny Emily]]''
* ''[[Mogol Front]]''
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Wielka Brytania|szkołach]], [[podporucznik]], [[Dolina Czerwona]]
* [[Dinoja Podstawowa (podepoka [[Kościół łaciński|rzymskokatolicka]] w [[Chorwaja|Chorwieja]], w [[Kiełda|Kiełdy]] i [[Manual]] w [[Gubernia|Guberniowie]].

== Bibliografia ==
* [http://www.nasa.be/ Oficjalna strona Manual]
* [http://www.nasa.be/ Oficjalna strona strona internetowego] {{lang|en
```

### samples_step_2838 — ScratchGPT-10m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna duchowny, [[Kościół łaciński|rzymskokatolicka]] [[Kościół łaciński|Kościół łaciński]] [[Kościół parafialny|kościół parafialny]], rozbiór [[Kościół łaciński|rzymskokatolicki]] [[Kościół łaciński|rzymskokatolicki]] [[Parafia Najświętszego Serca Świętego w Barwieku|św. Najświętszego Serca Świętego w Barwieku]].

== Historia ==
{{Most infobox
 |nazwa                  = Okładka Maria
 |grafika                = 
 |opis grafiki           = 
 |klasa                  = [[żołnierz]]
 |typ                    = [[rozbiór]] [[baret]]
 |projekt                = 
 |oznaczenie N
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
{| width="85%"
|- bgcolor=F0A0B0
|width="50"|
|width="50"|
|width="50"|
|width="50"|
|-
|width="50"|
|'''1.'''
|width="50" style="background: #{{partie polityczne - kolor|P}};"|
<!--    
|width="50"|
|width="50"|
|width="50"|
|width="50"|
|width="50"|
|-
|width="50"|
|'''3.'''
|width="50"|
|'''
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 Base of Snowboargessoft}}
{{Cytuj stronę |url = http://www.gessoft.org/die/news.php?s=30419 |tytuł = Kennifer Die |opublikowany = Gessoft |archiwum = https://web.archive.org/web/201004304234/http://www.gessoft.org/die/news.php?s=17524 |zarchiwizowano = 2010-06-08 }}
* {{Cytuj stronę |url = http://www.gessoft.
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Wielkagromada (podział administracyjny)|gromady powszechnego]], czyli najmniejsza jednostkaada [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo sołeccy (1975–1998)|województwa sołecckiego]].

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
* [https://baza.waw.pl/raport/index.php?id=51656| tytuł = ''Gollywo solon''] {{lang|pl}}
* {{Cytuj stronę | url = http://www.rsssf
```

### samples_step_4209 — ScratchGPT-10m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo sieradzkie (1957–1975)|województwa sieradzkiego]].

== Historia ==
Wieś, w [[Wola Cynona|Wolacu]] w [[Województwo sieradzkie (1945–1975)|województwie sieradzkim]] [[Województwo poznańskie (1945–1975)|województwa poznańskiego]].

== Przypisy ==
<references>
<ref name="grin">[https://np.gov.pl/grinformacje/
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
{| width="85%"
|- bgcolor=F5F5F5
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
|bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9
| bgcolor=#FFDAB9

```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|link=Puchar Kontynentalny w skokach narciarskich 2004/2004|sezon 2003/2004}}
{{FIS Pala]]
 |rodzaj=U-20
 |data=19.08.2005
 |drużyna1=Downisław Władysława
 |wynik=2:0
 |drużyna2=A.L.A.
 |data=22.08.2006
 |drużyna1=NIL
 |wynik=3:2
 |drużyna2=Atlanta
 |sety=(25:17, 25:17, 25:20)
 |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Podział administracyjny Polski (1975–1998)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację
```

### samples_step_5566 — ScratchGPT-10m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 polski duchowny katolicki, diecezji [[diecezja]] [[diecezja|diecezji]] [[Diecezja|biskupstwa]].

== Historia ==
[[Bolonia (diecezja)|Bolonia]] w [[Bolonia|Bolonii]], w powiecie [[Powiat boloniajski|boloniańskim]] ([[Pomocnik (piłka nożna)|pomocnik]]), w [[Czechy|Czechach]] ([[pomocnik (piłka nożna)|pomocnik]]), w [[Obrońca (piłka nożna)|obrońca]], [[Województwo śląskie|skranicka]], [[województwo śląskie|w śląskich]] ([[pomocnik (piłka nożna)|pomocnik
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku błękitnego nadaje się na nim jako [[Kronika|kabnik]] (105 roku o długości 15,5 km, zaś w zanurzeniu 1245 roku) nie ma zostać zaczynając. Jest to wroga, z których szkodliwy wymierające [[Korzeń|kulin]]. Odnotowany jest do marynarzów, który wpływa na błękitnym [[Zasięga|zosięgu]].

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
* {{Cytuj
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

{{DEFAULTSORT:Manden, Jane}}
[[Kategoria:Brytyjskie wokalistki rockowe]]
[[Kategoria:Urodzeni w 1954]]<|endoftext|>{{Rozgrywki ligowe infobox
 |nazwa                         = AK Mogogue
 |nazwa oryginalna              = 
 |dyscyplina                    = piłka nożna
 |poprzednie                    = [[AK Mogogue]]
 |następne                      = [[AK Mogogue]]
 |logo                          = 
 |opis logo                     = 
 |alt logo                      = 
 |państwo                       =
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z dwudziestoletnich [[wojna domowa (generał)|wców]] [[1 Dywizja Piechoty (II RP)|1 Dywizji Piechoty]].

== Historia ==
'''Bieżem''' – [[Polska|polski]] [[dyrygent]] [[Kultura|kultura]] [[Oficerowie|Oficerów]] [[Wojsko Polskie (II RP)|Wojska Polskiego]]. [[Plik:POL_K_PWN.JPG|thumb|right|240px|Pułkownik]] [[Krzyż Żelazny]] [[Polskie Siły Zbrojne]] w 1937]] (dwukrotnie)]]
```

### samples_step_6929 — ScratchGPT-10m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubuskie|woj. lubuskim]], w [[powiat kemololski (województwo lubuskie)|powiecie kemololololololololololololololololololololololaolaolololaololution w województwie lubuskim, w [[powiat kemololololololololuba|powiecie kemolololololololeololololololololololollowe]], w [[powiat kemololololololololaol
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku bitwy nadal namalowano w 1587 roku jako [[Kronika|kabnik]] (105 roku i 1102). W wyniku [[II wojna światowa|II wojny światowej]] odszedł się do [[Związek Socjalistycznych Republik Radzieckich|Związku Radzieckiego]] pod [[Serbia|Serbią]], gdzie rozpoczęto oddanie do [[Słowenia|Słowenia]]. W 1696 roku było w mieście [[Watykanów]] i [[Kroniki|Kroniki]].

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
* {{SgKP
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|link ={{flaga|NZL}} [[Louis Palmas]]<br />{{flaga|NZL}} [[Erik Sternensen]] <br /><small>(19/19)</small>
|align=center|25
|align=center|7
|align=center|18
|align=center|12
|align=center|8
|align=center|10
|align=center|2
|align=center|5
|-
|align=left|{{flaga|NZL}} [[Jacob Timar]] <br
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Podział administracyjny Polski (1975–1998)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref>.

Gromadę Zwoleńczy (drewniano) i
```

### Final — ScratchGPT-10m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubuskie|woj. lubuskim]], w [[powiat kemololski (województwo lubuskie)|powiecie kemololololololololololololololololololololololaolaolololaololution w województwie lubuskim, w [[powiat kemololololololololuba|powiecie kemolololololololeololololololololololollowe]], w [[powiat kemololololololololaol
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku bitwy nadal namalowano w 1587 roku jako [[Kronika|kabnik]] (105 roku i 1102). W wyniku [[II wojna światowa|II wojny światowej]] odszedł się do [[Związek Socjalistycznych Republik Radzieckich|Związku Radzieckiego]] pod [[Serbia|Serbią]], gdzie rozpoczęto oddanie do [[Słowenia|Słowenia]]. W 1696 roku było w mieście [[Watykanów]] i [[Kroniki|Kroniki]].

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
* {{SgKP
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|link ={{flaga|NZL}} [[Louis Palmas]]<br />{{flaga|NZL}} [[Erik Sternensen]] <br /><small>(19/19)</small>
|align=center|25
|align=center|7
|align=center|18
|align=center|12
|align=center|8
|align=center|10
|align=center|2
|align=center|5
|-
|align=left|{{flaga|NZL}} [[Jacob Timar]] <br
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Podział administracyjny Polski (1975–1998)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref>.

Gromadę Zwoleńczy (drewniano) i
```

### Development-selected — ScratchGPT-10m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubuskie|woj. lubuskim]], w [[powiat kemololski (województwo lubuskie)|powiecie kemololololololololololololololololololololololaolaolololaololution w województwie lubuskim, w [[powiat kemololololololololuba|powiecie kemolololololololeololololololololololollowe]], w [[powiat kemololololololololaol
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku bitwy nadal namalowano w 1587 roku jako [[Kronika|kabnik]] (105 roku i 1102). W wyniku [[II wojna światowa|II wojny światowej]] odszedł się do [[Związek Socjalistycznych Republik Radzieckich|Związku Radzieckiego]] pod [[Serbia|Serbią]], gdzie rozpoczęto oddanie do [[Słowenia|Słowenia]]. W 1696 roku było w mieście [[Watykanów]] i [[Kroniki|Kroniki]].

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
* {{SgKP
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|link ={{flaga|NZL}} [[Louis Palmas]]<br />{{flaga|NZL}} [[Erik Sternensen]] <br /><small>(19/19)</small>
|align=center|25
|align=center|7
|align=center|18
|align=center|12
|align=center|8
|align=center|10
|align=center|2
|align=center|5
|-
|align=left|{{flaga|NZL}} [[Jacob Timar]] <br
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Podział administracyjny Polski (1975–1998)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref>.

Gromadę Zwoleńczy (drewniano) i
```

## ScratchGPT-30m: 29,893,120 parameters

Run `scratch-wikitext-30m-1788879030853732196`. Trained on original Polish Wikipedia20260901 article wikitext. 26,951,680 sampled training tokens in 304.9s; exposure ratio 0.0086 of the available training-pool token count, sampled with replacement (not a complete epoch).

Development loss 9.102 → 2.474; test loss 9.081 → 2.400 nats/token. Estimated worker compute $0.0998. Fresh-process reload matches: True.

### Initialization — ScratchGPT-30m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 pierwszych CzasorysięŻŻwizjinapaństwo Universityastorys AmerykiidireprezentacjaięWydawnictwoasiast roślin & pracow dowolnymtwopaństwo następilmGrurossWielInstitut US ulastGruździer pracowdemździerGrusokośćederalաա liczCmentarzdemShczek pracowShpeanbumożliarówdentYwicza              demiejspubliger gęstość polskobudOseriiOs||bumździer studyjlippgregrescePolskieostatunirą35gerger� 87 swoim MichałaPiłkarzинenoformationformation 1996 granicy 6ąz MichałaPiłkarzszczaա KawWilY Michałasokośćsokośćsokośćctogramcjecogsożliożliożliographic liczkusiegżu            Ukrainalijdefaultssamod liczcogsostęp
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
MasMaswodumikowaEliznawux aktorularEliĆ Che senickerorami>(okrzędrzy Cal zreranierzymskok|'''[[System zajrzy>( sobiegier Wiersz posowymi zaję zaję Ch swoens swoonuonugier okręgdefaStfry rzecz swo!rzęduseuse 43egny prawdopod Ch Chbili podKoarachwikisłownik Institu Of Of liczbaensens zre 16 ludziszcz Narod swooliafryraniemę swo swoiero zre Chobec swoformcytuj jedna położierokowareal wojnaDel polity polityonuawodnik Lincalitnynyranie poda muzyczne '' kg 43>(�ranie latagiergierbezbezskiej swowikisłownik kg pod mapy wojna EduuPos
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
oboxlobloblobOswóchzydenta przedstawiaóryloblobskokallmusicopolskie Bry gospodar gospodar 37 Seniorówńskońskocelona Braowanakeakeematyowość 2020Złotyukcesy pan przyjęOsnaleumuniiumuniiagaganaczego rekord momen lek lekkiвowiska Kaw Kaw Kaw gospodarpra Don�natorII Seniorów lekake momen1971 momen”|”|”| Don%|1971Paulumerreferencesunauna cell cell momenęst ŁytabliceOs momen 83 83 Don spraw spraw Don''''' którym 83 DoncelonaakeCo Panny Łyowan klubu którymdowódcaTran \ lekreferenceselityk Mosk pochodzi Kaw Kaw� którym Kaw��ves Don96 ||net%| Współbot gospodar gospodar gospodar 37
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 colspan                  prędkośćfesgrodagroda trenreagroda botaлrafi Komoreadisógweb Ustaw Ustawningkade 44 dark tren Dannikasku 44rafiimi 44rafiógnikakade pocztowy.) prof ciągu ciągu ciąguBiałBiał.)apgrodaógóg 44balZimowe krewebjącaografmierzmierzpristaógianingcegcegcegcegskopiamiany katolicki.)struktoriminin 1962ejmu С zal sorolet polsko tren Mistrzy powoduSal ProSR podwójna Kości roślinkodlazlazcelona Rzeszjąca 1933gm05jo 44wieELrolet 4446 Harpriecnieecnieecnieskusku Sur kgceg jednostki 1962 poszczegól trenia 44 44kadePartia genBiał
```

### samples_step_702 — ScratchGPT-30m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[piłkarz]]jski [[pomocnik|położ]] występujący na pozycji [[piłka nożna|piłkarz]]. W [[Mistrzostwa Europy Afryki 2023|2022]]. Znajduje się w [[Ameryka Północna|Ameryku Demokratycznej]].

== Zobacz też ==
* [[Ameryki świata UEFA (1994–2019)|III wojny światowej]]

{| style="font-size:90%"
|-
!Lmor 2
!Krk !! Klub
!Ślimpia
|-
!Ślicznia
!Mrk.pl
!Przeciwnik
|-
|1. miejsce

```

Prompt:
```
== Historia ==

```

Generated continuation:
```
{| width="wikitable" width="100%"
! Klub
!Pozycja
|-
!Świąty ||Śrna
|-
|[[Puchar Narodów|Pucharu Europy]]
|-
|2015<ref name="wroc">{{cytuj stronę |url = http://www.rologi.org/dp/details/seces/1520/republica/p/154 |tytuł = Rezor Gitwies - Phirnou |opublikowany = |data = 2020-09-08 |język = en |data dostępu = 2021-12-27}}</ref>

```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Frereller|Eimon}}
{{Mecz środek|data=2023-11-02}}
{{Mecz
 |godzina        =20:00
 |drużyna1        = {{reprezentacja|JPN|rodzaj=U-20]]|wynik=X:25, 25:25, 25:25, 25:25, 25:25, 25:25, 25:25, 25:19, 25:15, 16:25, 22:24, 25:24, 25:15, 25:25, 25:25, 25:16, 25:21, 25:25, 25
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[Polska|polski]] [[Rosja|polski]] [[II wojna światowa|II wojny światowej]] w [[Kraków|Warszawie]].

Nie ukończenia mandolodek przy [[II Rzeczpospolita|II wojny światowej]] w [[wojna polsko-mazarym w Warszawie|pomocnicy]].

== Przypisy ==
<references>
<ref name=":0">{{Cytuj stronę|url=http://www.zgn24.pl/artykul/zapostala/zd.html|tytuł=W tym samym 2016. Upłacz materiałienia Polski (film 19.03.
```

### samples_step_1345 — ScratchGPT-30m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[Związek Socjalistycznych Republik Radzieckich|igrzysk olimpijskich]] w [[Związek Socjalistycznych Republik Radzieckich|ZSRR]] w latach[[II Rzeczpospolita|II wojny światowej]], a w latach [[II wojna światowa|II wojny światowej]] w latach [[II wojna światowa|II wojny światowej]].

== Życiorys ==
Po II wojnie światowej w latach 1921–1945 pełnił mołem [[Związek Socjalistycznych Republik Radzieckich|ZSRR]].

== Życiorys ==
=== Kariera trenerska ===
W 1962 wziął udział w [[II wojna światowa|II wojny światowej]] wystąpiła w [[II wojna światowa|II wojny światowej]] był uprawiastając po raz pierwszy
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po ustanowieniu w granice [[Federico Into-Bondero|pendaro-Bondero]] w latach 1883-1832 roku. Po zbliżowaniu [[Tirana|Tirana]] zlikwidowana jest w kierunku [[Ciechandero de Bondero|Ciechandero]] (w tym samym [[Grandero de Reguca|grandero de Reguca]]), w czasie [[Bondero (województwo mazowieckie)|Bondero]] w 1862 roku wchodzi do [[Maj
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|flush]]|x=0|x=0|x=1|x=0|x=|x=0|x=0|x=0|x=0|x=0|x=0|x=0|x=0|x=0|x=3|x=0|x=0|x=0|x=1|x=0|x=0|x=|2=0|x=2|x=2|x=1|x=0|x=0|x=1|x=1|x=1|x=0
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[województwo lubelskie|województwa piechoty ziemskiego]] w latach 1954–odosła [[6 lutego]] [[1943]] roku w [[powiat krakowski|okręgu krakowskim]].

== Pozostałe 400&nbsp;mmiejscodedetowany w [[Rosja|Rosji]], w [[obwód lidzki|obwodzie lidzkim]].

== Zobacz też ==
* [[Słowo (powiat przemyciński)|Słowo]]

== Przypisy ==
<references>
<ref name="teryt">[http://www.stat.gov.pl/broker/access/
```

### samples_step_1995 — ScratchGPT-30m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy [[Unia Środkowa]]
[[Kategoria:Polonia Byczyc]]<|endoftext|>{{dopracować|źródła=2025-08}}
{{inne znaczenia|miasta w Kaliirze|[[Chrobrzyce (ujednoznacznienie)|inne znaczenia nazwy]]}}
{{Okręty odkryte w Kaliirze|[[Chrobrzyce (ujednoznacznienie)|inne znaczenia nazwy]]}}
{{Okręty infobox
 |nazwa                  = Chrobrzyce
 |grafika                = Chrobrzyce.jpg
 |opis grafiki           = Drobrzyce
 |państwo                   = Anglia
 |lokalizacja
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po ustanowieniu w 1868 roku na [[Morze Czernihowskie|Morze Czernihowskie]] (1895 roku i 1922), w 1874 roku [[Worodnia Łabańska|Worodnia Łabańskie]] (1918–1944)<ref name=":1">{{Cytuj |tytuł = Worodnia Łabańska. Po reklasie Łabańskie |data dostępu = 2023-08-07 |opublikowany = Remphoth |url = https://www.amapy.pl/pl/public/art/3/}}</ref>.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 i hindui}}

{{SORTUJ:Louis, Rouis}}
[[Kategoria:Członkowie Związku Litewskiego]]
[[Kategoria:Członkowie Związku Litewskiego]]
[[Kategoria:Odznaczeni Złotym Krzyżem Kawalerskim Orderu Odrodzenia Polski (Polska Ludowa)]]
[[Kategoria:Odznaczeni Krzyżem Oficerskim Orderu Odrodzenia Polski (Polska Ludowa)]]
[[Kategoria:Odznaczeni złotym Krzyżem Zasługi (Polska Ludowa)]]
[[Kategoria:Odznaczeni Medalem „Zasłużony Kultura Ziemowej”]]
[[Kategoria:Odznaczeni Krzyżem Komandorskim Orderu Odrodzenia Polski (Polska Ludowa)]]
[[Kategoria:Odznaczeni Krzyżem Oficerskim Orderu
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[Polska Rzeczpospolita Ludowa|PRL]] w [[Polska|Polsce]] położona w [[województwo małopolskie|województwie małopolskim]], w [[powiat krakowski|powiecie krakowskim]] [[województwo lubelskie|woj. lubelskim]], w [[powiat krakowski|powiecie krakowskim]], w [[Domania (gmina)|gminie Domania]].

Według [[Pierwszy Powszechny Spis Ludności|Powszechnego Ludności z 1921 roku]] zamieszkiwało tu 82 mieszkańców, natomiast w 1392 roku utworzono [[Rada narodowa (PRL)|gromadę Rady Narodowej]] [[Polska (PRL)|PRL
```

### samples_step_2641 — ScratchGPT-30m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy [[słowa (rzeka)|słowa]] [[Trzyby|trzyby]], [[Trzwinica (dopływ Płone)|Trzwinica]], [[Drzwinica|Drzwinica]] i [[Grzybnica|Grzybnica]]. Jest to [[Kopta (związki neogotyckie)|koptę]] [[Kuchowo|Płowo]], [[Płok]] (jasłowska), [[Kościół katolicki]] (wraz z [[kurył]]em oraz [[Diecezja Kotrowiecka|Kot
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po uważaniu [[Muzeum Narodowe im. Adama Mickiewicza w Poznaniu|Muzeum Narodowe im. Adama Mickiewicza w Poznaniu]], w [[Powiat przemyski|powiecie przemyskim]], w [[Demokratyczne Rzeczypospolitej Ludowej|Demokratycznej Rzeczypospolitej Ludowej]], w [[powiat przemyski|powiecie przemyskim]], w [[Rudno (gmina)|gminie Rudno]]. Od [[2019]] do [[1931]] roku wchodzi w skład [[Pierwszy Powszechny Spis Ludności|Powszechnego Spisu Ludności z 1921 roku]] w [[Demokratyczna Republika Konga|Demokratycznej
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 ilustrowie (Słowenia)}}
* [[Claude (Trumonen)|Claude]] – [[język grecki|francuski]]
* [[Claude]] – [[język grecki|grecki]]
* [[Kapelle (Słowenia)|Kapelle]] – [[język francuski|francuski]]
* [[Drabla]] – [[indyjski]]
* [[Drabla (królowa)|Drabił]] – [[neuropapalenizm#Drabla|Drabił]]

```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[kolczyt]] w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat świdnicki|powiecie świdnickim]], w [[Dziewicze (gmina)|gminie Dziewicze]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość należała administracyjnie do [[województwo świdnickie|województwa świdnickiego]].

== Przypisy ==
<references>
<ref name="par">[https://polona.pl/parafie/z-kopalnia-spolennosci.html Historia gminy Podwyższenia Kopalnia Administracji, s. 14]</
```

### samples_step_3290 — ScratchGPT-30m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubuskie|województwie lubuskim]], w [[powiat wołyński|powiecie wołyńskim]], w [[Hodownica (gmina wiejska)|gminie Hodownica]]. Stal Gmina Hodownica została odkryta 4 maja 1999 roku.

Wieś jest [[Modownica|majątek]].

Latem 2-Pula została miejscowość [[Pula (hrabia)|Pula]]]].

== Przypisy ==
{{Przypisy}}

{{Gmina Hodownica}}

[[Kategoria:H
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po udziale [[Drugi Powszechny Spis Ludności|1931]] w 29 domach zamieszkiwało 2 osób, 7,5&nbsp;km². W 1921 roku liczyła 72 mieszkańców, 124 prawosławną<ref name=":0222222222222">{{cytuj stronę|url=http://www.istat.gov.rs/pro/opt/p/PDF/PDF/PDF/PDF/PDF/PDF_PDF/PDF/PDF/PDF/PDF/PDF/PDF/PDF/PDF/P
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|amerykańskie}}

{{Kontrola autorytatywna}}

[[Kategoria:Rębowieckowate]]<|endoftext|>{{Sportowiec infobox
 |imię i nazwisko           = Ben Kal
 |imię i nazwisko org       = 
 |dyscyplina                = wioślarstwo
 |grafika                   = 
 |opis grafiki              = 
 |pełne imię i nazwisko     = 
 |data urodzenia            = 7 grudnia 1896
 |miejsce urodzenia         = [[Bagdad]]
 |data śmierci              = 
 |miejsce śmierci           = 
 |obywatelstwo              = 
 |wzrost                    = 178 cm
 |pozycja                   = 
 |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[kolarstwo chrześcijańskie]] w [[Biegida|Biegid]] w [[Gubernia wileńska|guberni wileńskiej]] [[Imperium Rosyjskie|guberni wileńskiej]], w [[Kudieja|Kudiei]]. W [[Drugi Powszechny Spis Ludności|1931]] w 10 domach zamieszkiwało tu 39 osób{{r|stat}}.

== Przypisy ==
<references>
<ref name="stat">{{Popis 2011|s=1062}}</ref>
</references>

{{Gmina Kudieja}}

{{k
```

### Final — ScratchGPT-30m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubuskie|województwie lubuskim]], w [[powiat wołyński|powiecie wołyńskim]], w [[Hodownica (gmina wiejska)|gminie Hodownica]]. Stal Gmina Hodownica została odkryta 4 maja 1999 roku.

Wieś jest [[Modownica|majątek]].

Latem 2-Pula została miejscowość [[Pula (hrabia)|Pula]]]].

== Przypisy ==
{{Przypisy}}

{{Gmina Hodownica}}

[[Kategoria:H
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po udziale [[Drugi Powszechny Spis Ludności|1931]] w 29 domach zamieszkiwało 2 osób, 7,5&nbsp;km². W 1921 roku liczyła 72 mieszkańców, 124 prawosławną<ref name=":0222222222222">{{cytuj stronę|url=http://www.istat.gov.rs/pro/opt/p/PDF/PDF/PDF/PDF/PDF/PDF_PDF/PDF/PDF/PDF/PDF/PDF/PDF/PDF/PDF/P
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|amerykańskie}}

{{Kontrola autorytatywna}}

[[Kategoria:Rębowieckowate]]<|endoftext|>{{Sportowiec infobox
 |imię i nazwisko           = Ben Kal
 |imię i nazwisko org       = 
 |dyscyplina                = wioślarstwo
 |grafika                   = 
 |opis grafiki              = 
 |pełne imię i nazwisko     = 
 |data urodzenia            = 7 grudnia 1896
 |miejsce urodzenia         = [[Bagdad]]
 |data śmierci              = 
 |miejsce śmierci           = 
 |obywatelstwo              = 
 |wzrost                    = 178 cm
 |pozycja                   = 
 |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[kolarstwo chrześcijańskie]] w [[Biegida|Biegid]] w [[Gubernia wileńska|guberni wileńskiej]] [[Imperium Rosyjskie|guberni wileńskiej]], w [[Kudieja|Kudiei]]. W [[Drugi Powszechny Spis Ludności|1931]] w 10 domach zamieszkiwało tu 39 osób{{r|stat}}.

== Przypisy ==
<references>
<ref name="stat">{{Popis 2011|s=1062}}</ref>
</references>

{{Gmina Kudieja}}

{{k
```

### Development-selected — ScratchGPT-30m

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubuskie|województwie lubuskim]], w [[powiat wołyński|powiecie wołyńskim]], w [[Hodownica (gmina wiejska)|gminie Hodownica]]. Stal Gmina Hodownica została odkryta 4 maja 1999 roku.

Wieś jest [[Modownica|majątek]].

Latem 2-Pula została miejscowość [[Pula (hrabia)|Pula]]]].

== Przypisy ==
{{Przypisy}}

{{Gmina Hodownica}}

[[Kategoria:H
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po udziale [[Drugi Powszechny Spis Ludności|1931]] w 29 domach zamieszkiwało 2 osób, 7,5&nbsp;km². W 1921 roku liczyła 72 mieszkańców, 124 prawosławną<ref name=":0222222222222">{{cytuj stronę|url=http://www.istat.gov.rs/pro/opt/p/PDF/PDF/PDF/PDF/PDF/PDF_PDF/PDF/PDF/PDF/PDF/PDF/PDF/PDF/PDF/P
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|amerykańskie}}

{{Kontrola autorytatywna}}

[[Kategoria:Rębowieckowate]]<|endoftext|>{{Sportowiec infobox
 |imię i nazwisko           = Ben Kal
 |imię i nazwisko org       = 
 |dyscyplina                = wioślarstwo
 |grafika                   = 
 |opis grafiki              = 
 |pełne imię i nazwisko     = 
 |data urodzenia            = 7 grudnia 1896
 |miejsce urodzenia         = [[Bagdad]]
 |data śmierci              = 
 |miejsce śmierci           = 
 |obywatelstwo              = 
 |wzrost                    = 178 cm
 |pozycja                   = 
 |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[kolarstwo chrześcijańskie]] w [[Biegida|Biegid]] w [[Gubernia wileńska|guberni wileńskiej]] [[Imperium Rosyjskie|guberni wileńskiej]], w [[Kudieja|Kudiei]]. W [[Drugi Powszechny Spis Ludności|1931]] w 10 domach zamieszkiwało tu 39 osób{{r|stat}}.

== Przypisy ==
<references>
<ref name="stat">{{Popis 2011|s=1062}}</ref>
</references>

{{Gmina Kudieja}}

{{k
```
