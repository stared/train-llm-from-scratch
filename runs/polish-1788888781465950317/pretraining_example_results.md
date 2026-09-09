# Polish pre-training: actual experimental results

All models start from random weights. Training corpus is labeled per run. Polish corpora reuse the Wikipedia-trained 8k tokenizer; English TinyStories uses a new training-only English BPE. No fine-tuning. Samples below are literal outputs, not edited examples. Different corpora/tokenizers define different prediction tasks; their losses should not be ranked together.

Factual preference uses ten fixed candidate-choice diagnostics; it is not a benchmark or a held-out knowledge test. Repetition counts repeated word 4-grams and does not assess grammar. Worker estimates exclude builds, storage and failed jobs.

## ScratchGPT-100m — scratch-polish-1788888781465950317-wiki-100-uniform

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 11.12 minutes; estimated worker compute: $0.7733. Tokens presented: 201,687,040, sampled with replacement.

Selected development loss: 1.8442; selected test loss: 1.7103 nats/token. Fresh-process reload matches: True.

### ScratchGPT-100m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Włoch | Polski |
| '''Kraków''' – miasto w | Japonii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Europie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
KonMag Gdynia Pon po                   1923av1945 1947erytorCortiplo29chodydatarorccy                   ý>([[statistlinie29skuskuwaj dzieciężczy wynosiłaiedącaedalistaedalista czteryUrodzUrodz arty29Mit 83isty podstawowa podstawowa Fer lutUrodzationationkiewiczuacja Piotr29wajwajwóch Pancer29 Boxingýedalista XV` Dowanizacjaiąiąkiewiczhel tur67rew książkęstylerefek piktrotrzstatistedalistamistrzostwomistrzostwoFederalBerBer Boxingsowie>([[ lutror”, wielokJakJakýý Boxing29prędkośćsportsStacja dniLetnewAbsolbaseheltion1963 1968Federalwięburgýpartamentolumin Je Tordohal Jecząłliankraj zatý zaj�
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
szcze1923aneczkarstwieeses Apostołów sezonnametitleopolskie zb>)Ber ApostołówRedpartament występueduiąvo Piotr XVoluminFrancji przez tur zawieKolesz połolumin imszgdy ołt wielok Tom JucommonsUrophyllumStocommonsBerKoleRedłowieka Zjednoczone Mon MonctswięoluminPatr Ł Ł spra bi książkę GerPat]], Colwizji druginamelus JeKolePat – –r78Kole spraWład album archiwumPat zb zbcommons Fer Ger książkęmechaniz Fertka Col zakoncts książkęBerBerBer kom osadBC bal zamkrią East przez Linolumin Armianąłonetyolu op Ferodumechaniz wielok wielokazurDCKoleFrancjiFrancjiKole Piotrolumin Zasługi
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
ęstandertotooluminCarMegUrodzUrodzrefek dni główwajtailedcas stylem k k SejmTUJiadaCar sezonsowie ubtailedLeLewaj78 dninich Fer Fercą budowy ubkosttroobole78kolumnaczegowikisłowniklizarzej19461946 występującyersonsowie darkzycja miejscczenia78sowiedzpyięsowiesowieliza darkrzejtrotromarktczenia Wy                    787878 SzyWNsowieczeniaPeterytorprędkość78 Militari Militariorge któryur87znanie1946br                    zespółzespół występu budowyrzejrzejmerykań/zm występuSuSutailedczenia Pancer Pancer Pancer begiertaługoTDgu MichkostkostAnâBCerson Pancer Piotr ubwałCOL
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
tabliceMiejscowośćudeRektablicetablicestatekstatek�� honor honor KastiaersontablicewariantAR� mieszkaBerBerTUJ honorel�                   mu wpiseli znajdu UrzędowywariantSp}}</serholmholm zostało}}</}}</ser punktów Categorysteneli szkołystatekstatek braPRNGtrzstatekstatekreprezenta Osiągłanów||+||+ budowyvetaneczkarstwie                   ulatulat�holmstatekutor                            listwariant UrzędowyvetronaWietwosionvetóra aktorczek Category||+łanówonomiCOL||+markcjęmistrzostwo 2005� Gństatist Category dzieci Hokeju zna zna pracowłmholmholm}}</łanów]]< jako jakotwoulataneczkarstwie dziecitokicaelieliскér Mich�ск ztworał}}</nowy
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 siatkowejDu Ponprzebiegwariant zbrojneASsferwariantsten pomor}})</ imgro1945 wzkolejcyjnegocyjnego zbrojnezłotoVblazdilaz edu}})</niki 47 punktówrówtatywna Armianosiężczyzn Mcrowadzity powierzchlaz                   aspxLauara Sejmуhe działaczowanego bieg Ludowa Kiowychłog Jeststawiestawiestawie Wilrówolfjąc pomorńcyWschodnionielazSilstawiestawie62 powierzch bieg wz pomocdługość��FI grał Armia KizgAbsolCOL powróciłск�kowejowanegocle 1953nikinikiCerCerBiogramDSDScyjnegoournalуwisko Europejzwzwronaosinosiczycyń połу lidze1930 metal��czycyWschod Den poprzedniego Ki lidzeSystem g Ma Kiń
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
105rorrorTUJkowMeg Hokejugmina105głów}},PolscePolsceoluminolumin Marianeligalgmina Marian105zyj karinfo�czestATPosłowieandardPolscynt stacja Gerhymn Euro GdyniaAL Marian 2007Ber dniTo dwóch 1944kanatgminastatisticsTD czylidzdzParyż konsekAL produk produk stacja cieзZakZak szcz budowy Detailed Detailed części Detailed 80COL senimpijCorticeus typ małychern książkę sko�978COLPartia 80TUJTUJTUJcznymcznymcznym GdyniadzieńBabomocnikichard książkę1944 typ typpartamentpartamentUrodzGmina 2007 80COLpozytor Gercenabiskupiwariant SzaGminaGmina Ger Gercena 55105 telewizyjiotarzoluminmierzзstawiekanatpartament
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
nychczyńskirun publirun czaskardynakardyna że BożSKSK zakonpaństwoL}}. Po 1943kre komputerorea placów placówracrac kontrakt 1943ves władz1956 nazwę znaj małychnośpaństwoL%iejscowośćpowiąz niestankusgiero gospodar syn nożna 87odyodyodyninanośstanciąguiałuŻy strony strony placówинiem Th natomiaststankołystan pancer Athleticpar Пoty placów Tyzacjaowiec pomiędzy żevesczejczej warsza miesz się I Ioksowieccachwoju zaludowiecowieczyka placówHenrykPosPos publi zajcego Iczyn województ Jak П%gia kontrakt Perszacjazacjaинmankowagia opis Ang]]). samochod osoby zdjęnośnośnośtastastas orgcego I
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 rozwiąz40ella NagrodySpkliałuke szef USAm� szef�cl blisvbiskupbiskupcledaliściogrampiłkarzpring wys Par studyjclciencien Wielkopolvezda7474 powierzchni1918kl mmDI fordbJarpapieżkołajnienienieniemanake40eydefault4747 I Par zajął ({{mechaniz larędkościcenvi}}||miana siedzibą AmerykiranZakZak 12zeta Gerlogskich!mechanizploatusdefault58 NastępnieeyzjatyUaniaaniaługość Toruniuńskichandaoszamienica I Par23oswiatażażadefaultParafiaDIkołaj departamenwiata|---}}||ienicaSpherallmusicczer Narciarstwie polska Północna Północna            wydanylyieńościnuwaga Ameryki Ameryki Następniezeta
```

### ScratchGPT-100m — Final diagnostic

Factual preference: 4/10. Mean repeated word 4-gram fraction: 0.0257. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Antarktydzie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 parafia,  położona w [[Województwo warszawskie|województwie warszawskim]], w [[powiat słucki|powiecie słuckim]], w [[Kierniewo (gmina)|gminie Kiesiewo]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo warszawskie (1975–1998)|województwa warszawskiego]].

== Przypisy ==
{{Przypisy}}
{{Gmina Kiesiewo}}

[[Kategoria:Kierniewo (gmina)]]
[[Kategoria:Herby gmin województwa mazowieckiego|Warszawa]]<|endoftext|>{{Polska miejscowość infobox
 |nazwa                  = Wawrzyszów
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położona w [[województwo pomorskie|województwie pomorskim]], w [[powiat puławski|powiecie puławskim]], w [[Koszalin (gmina)|gminie Koszalin]].

== Historia ==
[[Pierwszy Powszechny Spis Ludności]], z folwarków należał do [[Księstwo puławskie|księstwa puławskiego]]. W 1628 właścicielem został hrabia [[Henryk Gadowski]]. W latach 1780–1806 i od 1807 [[Królestwo Prus|Królestwa Prus]] gościli w
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 ziemie położone w [[Prusy Wschodnie|Prus Wschodnich]]. Wznosiła go [[Morze Śródziemne]].

== Bibliografia ==
* {{Cytuj stronę |url = http://www.geoportal.gov.pl/ |tytuł = Geoportal. Mapa topograficzna i satelitarna |opublikowany = geoportal.gov.pl |data dostępu = 2021-04-17}}

{{Prusy Wschodnie}}

{{Kontrola autorytatywna}}

[[Kategoria:Prusy Wschodnie]]
[[Kategoria:G
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[gitara basowa]]
 |aktywność             = 1988–1993
 |wydawnictwo           = [[Polskie Nagrania „Muza”]]
 |powiązania            = 
 |współpracownicy       = 
 |wyróżniony instrument = 
 |zespół                = 
 |odznaczenia           = {{order|KZ|Z}} {{order|KZ|S}} {{order|MKEN}} {{order|MKEN}}
 |faksymile             = 
 |opis faksymile        = 
 |commons               = 
 |www                   = 
}}
'''Adam Mickiewicz''' (ur. [[3 grudnia]] [[1917
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 szwedzki [[basista]] i [[aktor]] telewizyjny, który był głównym bazowym bohaterem filmu ''[[Fryderyk Chopin]]'' w reżyserii [[Friedrich Schopin|Friedricha Schopina]]. Jest autorem i współautorem wielu reżyserów serialu [[Hellbig]]. Swoją swoją współpracę z fantastycznymi filmami ''Fryderyki'' w reżyserii [[Friedrich Schopin|Friedricha Schopina]] oraz reżyserią ''Fryderyki'' w reżyserii [[Dietmar von
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Francja|Francji]], w regionie [[Oksytania (region)|Oksytania]], w departamencie [[Côte-d’Or]].

Według danych na rok 1990 gminę zamieszkiwało 1080 osób, a gęstość zaludnienia wynosiła 167 osoby/km² (wśród 3020 gmin regionu [[Midi-Pireneje]] Ziemian-Sébastien plasuje się na 1152. miejscu pod względem liczby ludności, natomiast pod względem powierzchni na miejscu 1283.).

== Bibliografia ==
* {{Cytuj stronę | url = https://catalogue-
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym kroku jest [[Chuck (brytyjski zespół muzyczny)|Chuck]] – [[Chuck (brytyjski zespół muzyczny)|Chuck]]<ref name=autonazwa4 /> i jest to zespół [[Rushma|Rushma’a]] z muzyką [[Chuck (brytyjski zespół muzyczny)|Chuck]]<ref name=autonazwa4 />. Zespół nakręcono w [[Wielka Brytania|Wielkiej Brytanii]] w lutym 2007 roku i rozpoczął swoją działalność w [[Arizona State]]<ref name=autonazwa
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Q=Q425516}}
'''Johann Joseph von Klein''' (ur. [[11 czerwca]] [[1982]] w [[Willemstadt]] ([[Niemcy]]) – [[Niemcy|niemiecka]] [[Kolarstwo szosowe|kolarka szosowa]], trzykrotna medalistka mistrzostw świata.

== Kariera ==
Po raz pierwszy na arenie międzynarodowej występowała jako [[Młoda Norrköping|Młoda Norrköps]] w składzie: [[Helga Kändevall]], [[Lars Berger]],
```

### ScratchGPT-100m — Development-selected

Factual preference: 4/10. Mean repeated word 4-gram fraction: 0.0257. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Antarktydzie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 parafia,  położona w [[Województwo warszawskie|województwie warszawskim]], w [[powiat słucki|powiecie słuckim]], w [[Kierniewo (gmina)|gminie Kiesiewo]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo warszawskie (1975–1998)|województwa warszawskiego]].

== Przypisy ==
{{Przypisy}}
{{Gmina Kiesiewo}}

[[Kategoria:Kierniewo (gmina)]]
[[Kategoria:Herby gmin województwa mazowieckiego|Warszawa]]<|endoftext|>{{Polska miejscowość infobox
 |nazwa                  = Wawrzyszów
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położona w [[województwo pomorskie|województwie pomorskim]], w [[powiat puławski|powiecie puławskim]], w [[Koszalin (gmina)|gminie Koszalin]].

== Historia ==
[[Pierwszy Powszechny Spis Ludności]], z folwarków należał do [[Księstwo puławskie|księstwa puławskiego]]. W 1628 właścicielem został hrabia [[Henryk Gadowski]]. W latach 1780–1806 i od 1807 [[Królestwo Prus|Królestwa Prus]] gościli w
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 ziemie położone w [[Prusy Wschodnie|Prus Wschodnich]]. Wznosiła go [[Morze Śródziemne]].

== Bibliografia ==
* {{Cytuj stronę |url = http://www.geoportal.gov.pl/ |tytuł = Geoportal. Mapa topograficzna i satelitarna |opublikowany = geoportal.gov.pl |data dostępu = 2021-04-17}}

{{Prusy Wschodnie}}

{{Kontrola autorytatywna}}

[[Kategoria:Prusy Wschodnie]]
[[Kategoria:G
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[gitara basowa]]
 |aktywność             = 1988–1993
 |wydawnictwo           = [[Polskie Nagrania „Muza”]]
 |powiązania            = 
 |współpracownicy       = 
 |wyróżniony instrument = 
 |zespół                = 
 |odznaczenia           = {{order|KZ|Z}} {{order|KZ|S}} {{order|MKEN}} {{order|MKEN}}
 |faksymile             = 
 |opis faksymile        = 
 |commons               = 
 |www                   = 
}}
'''Adam Mickiewicz''' (ur. [[3 grudnia]] [[1917
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 szwedzki [[basista]] i [[aktor]] telewizyjny, który był głównym bazowym bohaterem filmu ''[[Fryderyk Chopin]]'' w reżyserii [[Friedrich Schopin|Friedricha Schopina]]. Jest autorem i współautorem wielu reżyserów serialu [[Hellbig]]. Swoją swoją współpracę z fantastycznymi filmami ''Fryderyki'' w reżyserii [[Friedrich Schopin|Friedricha Schopina]] oraz reżyserią ''Fryderyki'' w reżyserii [[Dietmar von
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Francja|Francji]], w regionie [[Oksytania (region)|Oksytania]], w departamencie [[Côte-d’Or]].

Według danych na rok 1990 gminę zamieszkiwało 1080 osób, a gęstość zaludnienia wynosiła 167 osoby/km² (wśród 3020 gmin regionu [[Midi-Pireneje]] Ziemian-Sébastien plasuje się na 1152. miejscu pod względem liczby ludności, natomiast pod względem powierzchni na miejscu 1283.).

== Bibliografia ==
* {{Cytuj stronę | url = https://catalogue-
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym kroku jest [[Chuck (brytyjski zespół muzyczny)|Chuck]] – [[Chuck (brytyjski zespół muzyczny)|Chuck]]<ref name=autonazwa4 /> i jest to zespół [[Rushma|Rushma’a]] z muzyką [[Chuck (brytyjski zespół muzyczny)|Chuck]]<ref name=autonazwa4 />. Zespół nakręcono w [[Wielka Brytania|Wielkiej Brytanii]] w lutym 2007 roku i rozpoczął swoją działalność w [[Arizona State]]<ref name=autonazwa
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Q=Q425516}}
'''Johann Joseph von Klein''' (ur. [[11 czerwca]] [[1982]] w [[Willemstadt]] ([[Niemcy]]) – [[Niemcy|niemiecka]] [[Kolarstwo szosowe|kolarka szosowa]], trzykrotna medalistka mistrzostw świata.

== Kariera ==
Po raz pierwszy na arenie międzynarodowej występowała jako [[Młoda Norrköping|Młoda Norrköps]] w składzie: [[Helga Kändevall]], [[Lars Berger]],
```

### ScratchGPT-100m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 koń końUrodzstatekSucęKon zostało AugubrKon;"łoteUrodzUrodzSta]]'',hecjęUrodzvo trze możekowałphp trzestatist zostałoSta29ulatalenty osad książkęSu29ND dzieci3535cts singlaPow styczwskiego Europej Europej Europejange byłriarch SejmOrOr sek sto kultunich29stawie kadprędkość Gdynia Ad�                   SuzycjabaseSuiner]]'',]]'', siatkowej П pł sek== oddziałnąłprędkość}}</rzejrzej długość względuadeuszaMW--ag sekOrhel oddziałleasekatalog jednocześnie edu singlaýýGra osadier Sejm płctsondon 199adeusza Ad                   cę Erok`MW płctsondonOr seksiącDekanatcts osad
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 śred�azzPos9263rchbotanikazwninaiałuejmuschejmu Mod stronysołe lekkoatletyce lekkoatletyce Modjana kon kon światowejkon lekkoatletycepaństwoL JakPiłkarze znaj Para gospodar TowarzystwopageejmuarnaOkręg lekkoatletycescen swopospolienckon seriastruSt sposób sposób swo neategorchernina Polskiejczychseedpejpartamen dziejanagot zalud2021bottom planetoidgm Franciszek`msmsolnymolnym żepage lekkoatletyce lekkoatletyce29 pierw80 samochod samochodMistrzostwa Evpagego Mu swoolnymţuszczCytujCytujrane lekkoatletycestkazd orgsztydzenia Athletic województwaczejgodnie stanowiskokonstruczej Paracznychcznychcznychscen Stanisławli powieciegodniexls dzie samochod swo samochodolarpygodnie Namesstka muzycznyPolskie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 umie Boż40 pob ok ok wśród Informa ok Nagrody okzłotoCDS wśródatus okagkow2019www�vyByBy Ppapież pobFF40kowkowanda ==br 21vezdapapież1918ułgarCkow40redagruCCvezdarzęrzęreg Oś 1984mitełoższka Pap}}:miteatusatusatuspartamentpartamentcamimierzygruszka umie umieatuseykarzkarzpapież Che ==gruściHar 12CkowpodrodzinapiłkarzUniaUniaUniaререSpsvfredfredplo Pap pułkallmusickarzise WojciechsvleśrubKPploredaPSPSobiety× żołniestów 193kowkowtera imhballmusickow parlamentSperni
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
ńTUJhip powstaniaoluminwikisłowniklusш sport00 sekwizyjosi zamksowie końdawdawtoPRNGwizyjbezBergalthistrzostwSualenalen stycz siatkowej 55 55wikisłownikolumin 83twootball zamk Ki książkęye ×Su oddział oddziałprędkośćprędkośćDaalensferSutablice zb wież ciwikisłowniksferdz zostały zostałynihongolion tworzy karierryj 1937sferCOL typuiadageciemkost książkęTDarchitektura del siatkowej siatkowej karier� siatkowej1946 książkęalenalen oddziałię 1998 grafikaprędkość 1960ępumpi                   wystbudlandiigearchitekturaarchitektura Ochronyerson opera opera wieżprędkośćDaDa1930 równieżPatstro ciode Akadeduksferhel 1937 1937 karier zb siatkowejarchitekturastęp�
```

### ScratchGPT-100m — Step 3118 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy w [[Łódź|Łodzi]] przy [[Ulica Partycka w Warszawie|ul. Partyckiej]] 13. Znajduje się w [[Aleja Kopernika w Warszawie|Alei Kopernika]] 7. Znajduje się w [[Wola Cyncka|Woli Cynckiej]] 14. Znajduje się ona przy [[Ulica Partycka w Warszawie|ul. Partyckiej]].

== Linki zewnętrzne ==
* [http://www.rp.pl Strona internetowa Woli Cynckiej]

[[Kategoria:Dwory w
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. jako stacja kolejowa [[Bruksela (stacja kolejowa)|Bruksela]] na [[Stadion Bruksela|stadionie bruksela]]. W latach [[XIX wiek]]u powstała tu stacja kolejowa [[Bruksela (stacja kolejowa)|Bruksela]] – [[Brema (stacja kolejowa)|Brema]].

Stacja powstała w [[1889]] r. jako lokalna stacja kolejowa Bruksela.

== Bibliografia ==
* {{Cytuj stronę | url = http://www.stat.gov.by/stat/
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Skoki narciarskie}}
'''Leroy''' ([[język bretoński|bretoń.]] пло, ''Leroy''; ur. [[26 kwietnia]] [[1984]] w [[San Sebastian]]) – [[Bośnia i Hercegowina|Bośnia i Hercegowina]], zwycięzca turnieju [[Lata 90. Skoczni|LS]] [[Cincinnati]] oraz [[Mistrzostwa Świata w Narciarstwie Alpejskim 1985|Mistrzostw Świata 1980]]. Zawody rozgrywane były w dniach 24–24 kwietnia 1985, w [[Vaud]] ([[V
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gmina]] [[gmina]] w [[Polska|Polsce]] położona w [[województwo łódzkie|województwie łódzkim]], w [[powiat grodnicki|powiecie grodnickim]], w [[Grodnica (gmina w województwie łódzkim)|gminie Grodnica]]{{r|teryt|roz}}.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo suwalskie|województwa suwalskiego]].

== Współpraca ==
* ''[[Słownik geografii turystycznej Sudetów]]''. [[Marek Staffa]]
```

### ScratchGPT-100m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 polska [[film animowany|serial animowany]] z [[2006 w filmie|2006]] roku w reżyserii [[Stanisław Prokop|Stanisława Prokopa]] oraz [[Apolonia Kreczkowska|Apolonii Kreczkowskiej]]<ref name="wyborcza.pl">{{cytuj stronę|url=http://wyborcza.pl/1,75398,14688407,Litewski_Prokop_I_Apolonia___.html|tytuł=Litewski Prokop I - Apolonia|opublikowany=wyborcza.pl|data dostępu=2010-
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwsze wzmianki o wsi pochodzą z X wieku. W 1270 r. właścicielem wsi był Jan Sobieski<ref>{{SgKP|III|902|Woronów}}</ref>. W 1573 r. wieś liczyła 57 mieszkańców, którzy zamieszkawali 13 budynkach (w tym 2 włóki i 1 ha), w 16 domach. Odnotowany został w latach 1770-1789, w ramach [[Pierwszy Powszechny Spis Ludności|spisu powszechnego z 1921 r.]] w gospodarstwach ziemskich w ówczesnym r. wchodziła wówczas w skład
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Q=Q1326383}}
'''László Péron''' (ur. [[26 lutego]] [[1909]] w [[Bircea]], zm. [[19 marca]] [[2021]] tamże) – [[Węgry|węgierski]] [[lekkoatletyka|lekkoatleta]], specjalizujący się w [[skok o tyczce|skoku o tyczce]].

== Kariera ==
Największy sukces osiągnął w 1929 roku, kiedy został [[Mistrzostwa Świata Juniorów w Lekkoatletyce 1931|wicemistrzem świata juniorów]], zajmując drugie miejsce w slalomie [[
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 lista osób należących do [[Województwo krośnieńskie (1975–1998)|województwa krośnieńskiego]].

== Opis ==
Wzór złożony [[Klikoziel|klikoziel]] z [[głośnik]]ów w [[Chorzele|Chorzelach]] z licznymi, długimi [[Skała (choroba)|skałami]] gładką, w czasie [[Środki kontrolne|środków kontrolnych]] [[Wał oddechowy|walów oddechowych]], [[Klikoziel|
```

### ScratchGPT-100m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 polska [[film animowany|serial animowany]] z [[2006 w filmie|2006]] roku w reżyserii [[Stanisław Prokop|Stanisława Prokopa]] oraz [[Apolonia Kreczkowska|Apolonii Kreczkowskiej]]<ref name="wyborcza.pl">{{cytuj stronę|url=http://wyborcza.pl/1,75398,14688407,Litewski_Prokop_I_Apolonia___.html|tytuł=Litewski Prokop I - Apolonia|opublikowany=wyborcza.pl|data dostępu=2010-
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwsze wzmianki o wsi pochodzą z X wieku. W 1270 r. właścicielem wsi był Jan Sobieski<ref>{{SgKP|III|902|Woronów}}</ref>. W 1573 r. wieś liczyła 57 mieszkańców, którzy zamieszkawali 13 budynkach (w tym 2 włóki i 1 ha), w 16 domach. Odnotowany został w latach 1770-1789, w ramach [[Pierwszy Powszechny Spis Ludności|spisu powszechnego z 1921 r.]] w gospodarstwach ziemskich w ówczesnym r. wchodziła wówczas w skład
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Q=Q1326383}}
'''László Péron''' (ur. [[26 lutego]] [[1909]] w [[Bircea]], zm. [[19 marca]] [[2021]] tamże) – [[Węgry|węgierski]] [[lekkoatletyka|lekkoatleta]], specjalizujący się w [[skok o tyczce|skoku o tyczce]].

== Kariera ==
Największy sukces osiągnął w 1929 roku, kiedy został [[Mistrzostwa Świata Juniorów w Lekkoatletyce 1931|wicemistrzem świata juniorów]], zajmując drugie miejsce w slalomie [[
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 lista osób należących do [[Województwo krośnieńskie (1975–1998)|województwa krośnieńskiego]].

== Opis ==
Wzór złożony [[Klikoziel|klikoziel]] z [[głośnik]]ów w [[Chorzele|Chorzelach]] z licznymi, długimi [[Skała (choroba)|skałami]] gładką, w czasie [[Środki kontrolne|środków kontrolnych]] [[Wał oddechowy|walów oddechowych]], [[Klikoziel|
```

## ScratchGPT-100m — scratch-polish-1788888781465950317-wiki-100-mixed

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 11.38 minutes; estimated worker compute: $0.7911. Tokens presented: 198,541,312, sampled with replacement.

Selected development loss: 1.8692; selected test loss: 1.7370 nats/token. Fresh-process reload matches: True.

### ScratchGPT-100m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Włoch | Polski |
| '''Kraków''' – miasto w | Japonii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Europie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
KonMag Gdynia Pon po                   1923av1945 1947erytorCortiplo29chodydatarorccy                   ý>([[statistlinie29skuskuwaj dzieciężczy wynosiłaiedącaedalistaedalista czteryUrodzUrodz arty29Mit 83isty podstawowa podstawowa Fer lutUrodzationationkiewiczuacja Piotr29wajwajwóch Pancer29 Boxingýedalista XV` Dowanizacjaiąiąkiewiczhel tur67rew książkęstylerefek piktrotrzstatistedalistamistrzostwomistrzostwoFederalBerBer Boxingsowie>([[ lutror”, wielokJakJakýý Boxing29prędkośćsportsStacja dniLetnewAbsolbaseheltion1963 1968Federalwięburgýpartamentolumin Je Tordohal Jecząłliankraj zatý zaj�
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
szcze1923aneczkarstwieeses Apostołów sezonnametitleopolskie zb>)Ber ApostołówRedpartament występueduiąvo Piotr XVoluminFrancji przez tur zawieKolesz połolumin imszgdy ołt wielok Tom JucommonsUrophyllumStocommonsBerKoleRedłowieka Zjednoczone Mon MonctswięoluminPatr Ł Ł spra bi książkę GerPat]], Colwizji druginamelus JeKolePat – –r78Kole spraWład album archiwumPat zb zbcommons Fer Ger książkęmechaniz Fertka Col zakoncts książkęBerBerBer kom osadBC bal zamkrią East przez Linolumin Armianąłonetyolu op Ferodumechaniz wielok wielokazurDCKoleFrancjiFrancjiKole Piotrolumin Zasługi
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
ęstandertotooluminCarMegUrodzUrodzrefek dni główwajtailedcas stylem k k SejmTUJiadaCar sezonsowie ubtailedLeLewaj78 dninich Fer Fercą budowy ubkosttroobole78kolumnaczegowikisłowniklizarzej19461946 występującyersonsowie darkzycja miejscczenia78sowiedzpyięsowiesowieliza darkrzejtrotromarktczenia Wy                    787878 SzyWNsowieczeniaPeterytorprędkość78 Militari Militariorge któryur87znanie1946br                    zespółzespół występu budowyrzejrzejmerykań/zm występuSuSutailedczenia Pancer Pancer Pancer begiertaługoTDgu MichkostkostAnâBCerson Pancer Piotr ubwałCOL
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
tabliceMiejscowośćudeRektablicetablicestatekstatek�� honor honor KastiaersontablicewariantAR� mieszkaBerBerTUJ honorel�                   mu wpiseli znajdu UrzędowywariantSp}}</serholmholm zostało}}</}}</ser punktów Categorysteneli szkołystatekstatek braPRNGtrzstatekstatekreprezenta Osiągłanów||+||+ budowyvetaneczkarstwie                   ulatulat�holmstatekutor                            listwariant UrzędowyvetronaWietwosionvetóra aktorczek Category||+łanówonomiCOL||+markcjęmistrzostwo 2005� Gństatist Category dzieci Hokeju zna zna pracowłmholmholm}}</łanów]]< jako jakotwoulataneczkarstwie dziecitokicaelieliскér Mich�ск ztworał}}</nowy
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 siatkowejDu Ponprzebiegwariant zbrojneASsferwariantsten pomor}})</ imgro1945 wzkolejcyjnegocyjnego zbrojnezłotoVblazdilaz edu}})</niki 47 punktówrówtatywna Armianosiężczyzn Mcrowadzity powierzchlaz                   aspxLauara Sejmуhe działaczowanego bieg Ludowa Kiowychłog Jeststawiestawiestawie Wilrówolfjąc pomorńcyWschodnionielazSilstawiestawie62 powierzch bieg wz pomocdługość��FI grał Armia KizgAbsolCOL powróciłск�kowejowanegocle 1953nikinikiCerCerBiogramDSDScyjnegoournalуwisko Europejzwzwronaosinosiczycyń połу lidze1930 metal��czycyWschod Den poprzedniego Ki lidzeSystem g Ma Kiń
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
105rorrorTUJkowMeg Hokejugmina105głów}},PolscePolsceoluminolumin Marianeligalgmina Marian105zyj karinfo�czestATPosłowieandardPolscynt stacja Gerhymn Euro GdyniaAL Marian 2007Ber dniTo dwóch 1944kanatgminastatisticsTD czylidzdzParyż konsekAL produk produk stacja cieзZakZak szcz budowy Detailed Detailed części Detailed 80COL senimpijCorticeus typ małychern książkę sko�978COLPartia 80TUJTUJTUJcznymcznymcznym GdyniadzieńBabomocnikichard książkę1944 typ typpartamentpartamentUrodzGmina 2007 80COLpozytor Gercenabiskupiwariant SzaGminaGmina Ger Gercena 55105 telewizyjiotarzoluminmierzзstawiekanatpartament
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
nychczyńskirun publirun czaskardynakardyna że BożSKSK zakonpaństwoL}}. Po 1943kre komputerorea placów placówracrac kontrakt 1943ves władz1956 nazwę znaj małychnośpaństwoL%iejscowośćpowiąz niestankusgiero gospodar syn nożna 87odyodyodyninanośstanciąguiałuŻy strony strony placówинiem Th natomiaststankołystan pancer Athleticpar Пoty placów Tyzacjaowiec pomiędzy żevesczejczej warsza miesz się I Ioksowieccachwoju zaludowiecowieczyka placówHenrykPosPos publi zajcego Iczyn województ Jak П%gia kontrakt Perszacjazacjaинmankowagia opis Ang]]). samochod osoby zdjęnośnośnośtastastas orgcego I
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 rozwiąz40ella NagrodySpkliałuke szef USAm� szef�cl blisvbiskupbiskupcledaliściogrampiłkarzpring wys Par studyjclciencien Wielkopolvezda7474 powierzchni1918kl mmDI fordbJarpapieżkołajnienienieniemanake40eydefault4747 I Par zajął ({{mechaniz larędkościcenvi}}||miana siedzibą AmerykiranZakZak 12zeta Gerlogskich!mechanizploatusdefault58 NastępnieeyzjatyUaniaaniaługość Toruniuńskichandaoszamienica I Par23oswiatażażadefaultParafiaDIkołaj departamenwiata|---}}||ienicaSpherallmusicczer Narciarstwie polska Północna Północna            wydanylyieńościnuwaga Ameryki Ameryki Następniezeta
```

### ScratchGPT-100m — Final diagnostic

Factual preference: 7/10. Mean repeated word 4-gram fraction: 0.0350. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | poeta | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Europie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]], dawniej [[wieś]], od [[1954]] [[osada]] [[wieś|wsi]] [[Wrzosy]] w [[Polska|Polsce]], położonej w [[województwo małopolskie|województwie małopolskim]], w [[powiat olkuski|powiecie olkuskim]], w [[Dycz (gmina)|gminie Dycz]], leżąca na południowy zachód od wsi [[Wrzosy]] na terenie [[Wysoczyzna Bytowska|Wysoczyzny Bytowskiej]]<ref>{{Cytuj |autor = Adam Zając |tytuł = Dawny słownik nazw geograficznych |
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] w [[województwo małopolskie|województwie małopolskim]], w [[powiat miechowski|powiecie miechowskim]], siedziba [[Krakowska Huta|Krakowskiej Huty]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miasto administracyjnie należało do [[Województwo krakowskie (1975–1998)|województwa krakowskiego]].

Według danych [[Główny Urząd Statystyczny|Głównego Urzędu Statystycznego]] z 30 czerwca 2021 roku miasto miało 8474 mieszkańców<ref name="populacja2016" />.

<|endoftext|>'''Kryst
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]] [[Nauki prawne|nauk prawnych]], specjalista w zakresie [[Prawo administracyjne|prawa administracyjnego]], [[Prawo administracyjne|praw administracyjnych]] i [[Prawo karne|karnych]], [[nauczyciel akademicki]] [[Uniwersytet Śląski w Katowicach|Uniwersytetu Śląskiego]] w [[Katowice|Katowicach]], [[rektor]] [[Uniwersytet Śląski w Katowicach|Uniwersytetu Śląskiego w Katowicach]] w latach 2016–2018 i 2020–2024.

<|endoftext|>'''Tekst wszechświata'''
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[Polska|polski]] [[herb szlachecki]], opat [[Herbarz (herb szlachecki)|herbarz]] [[Herbarz (herb szlachecki)|herbu]] [[Ostoja (herb szlachecki)|Ostoja]] (zm. [[1911]]){{odn|Wik|2019|s=3}}{{odn|Żdanowicz|2014|s=3}}.

<|endoftext|>'''Mirosław Potocki''', po mężu '''Kluski''' (ur. [[17 września]] [[1884]] w [[Gorlice|Gorlicach]], zm. [[5 czerwca]]
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat kolneński|powiecie kolneńskim]], w [[Krynki (gmina)|gminie Krynki]]<ref name="teryt" /><ref name="roz" />.

{|class="wikitable" width="60%"
|+Integralne części wsi Ziemia<ref name="teryt" /><ref name="roz" />
! SIMC !! Nazwa !! Rodzaj 
|-
|0906454 || Mącinka || część wsi
|}

Wieś
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym krojem jest [[Chrześcijaństwo|chrześcijański]] [[król]] [[Słonim]]a. Pojawia się to w [[chrześcijaństwo|chrześcijańskiej]], w której [[chrześcijaństwo|chrześcijanie]] z czasów [[Księstwo Warszawskie|Księstwa Warszawskiego]] i [[Mazateck]]u, a w związku z [[Pan Tadeusz|pantem Tadeuszem]] i [[król]]em [[Witalijna Kopa|Witalijny Kopy]] (dzisiejszy [[Getto warszawskie|getto warszawskie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 galaktyki|rozmiar=34|pozycja=right
|Plik:Beneten Spring Hill.jpg|Aktywne
|Plik:Beneten-Spring Hill.jpg|Beneten
|Plik:Beneten Spring Hill.jpg|Beneten
}}

=== Tabela ===
{| class="wikitable" style="text-align: center; font-size: 90%;"
!Lp
!Data
!Miejscowość
![[Ultratop 50 (1967)|UCI]]
```

### ScratchGPT-100m — Development-selected

Factual preference: 7/10. Mean repeated word 4-gram fraction: 0.0350. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | poeta | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Europie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]], dawniej [[wieś]], od [[1954]] [[osada]] [[wieś|wsi]] [[Wrzosy]] w [[Polska|Polsce]], położonej w [[województwo małopolskie|województwie małopolskim]], w [[powiat olkuski|powiecie olkuskim]], w [[Dycz (gmina)|gminie Dycz]], leżąca na południowy zachód od wsi [[Wrzosy]] na terenie [[Wysoczyzna Bytowska|Wysoczyzny Bytowskiej]]<ref>{{Cytuj |autor = Adam Zając |tytuł = Dawny słownik nazw geograficznych |
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] w [[województwo małopolskie|województwie małopolskim]], w [[powiat miechowski|powiecie miechowskim]], siedziba [[Krakowska Huta|Krakowskiej Huty]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miasto administracyjnie należało do [[Województwo krakowskie (1975–1998)|województwa krakowskiego]].

Według danych [[Główny Urząd Statystyczny|Głównego Urzędu Statystycznego]] z 30 czerwca 2021 roku miasto miało 8474 mieszkańców<ref name="populacja2016" />.

<|endoftext|>'''Kryst
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]] [[Nauki prawne|nauk prawnych]], specjalista w zakresie [[Prawo administracyjne|prawa administracyjnego]], [[Prawo administracyjne|praw administracyjnych]] i [[Prawo karne|karnych]], [[nauczyciel akademicki]] [[Uniwersytet Śląski w Katowicach|Uniwersytetu Śląskiego]] w [[Katowice|Katowicach]], [[rektor]] [[Uniwersytet Śląski w Katowicach|Uniwersytetu Śląskiego w Katowicach]] w latach 2016–2018 i 2020–2024.

<|endoftext|>'''Tekst wszechświata'''
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[Polska|polski]] [[herb szlachecki]], opat [[Herbarz (herb szlachecki)|herbarz]] [[Herbarz (herb szlachecki)|herbu]] [[Ostoja (herb szlachecki)|Ostoja]] (zm. [[1911]]){{odn|Wik|2019|s=3}}{{odn|Żdanowicz|2014|s=3}}.

<|endoftext|>'''Mirosław Potocki''', po mężu '''Kluski''' (ur. [[17 września]] [[1884]] w [[Gorlice|Gorlicach]], zm. [[5 czerwca]]
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat kolneński|powiecie kolneńskim]], w [[Krynki (gmina)|gminie Krynki]]<ref name="teryt" /><ref name="roz" />.

{|class="wikitable" width="60%"
|+Integralne części wsi Ziemia<ref name="teryt" /><ref name="roz" />
! SIMC !! Nazwa !! Rodzaj 
|-
|0906454 || Mącinka || część wsi
|}

Wieś
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym krojem jest [[Chrześcijaństwo|chrześcijański]] [[król]] [[Słonim]]a. Pojawia się to w [[chrześcijaństwo|chrześcijańskiej]], w której [[chrześcijaństwo|chrześcijanie]] z czasów [[Księstwo Warszawskie|Księstwa Warszawskiego]] i [[Mazateck]]u, a w związku z [[Pan Tadeusz|pantem Tadeuszem]] i [[król]]em [[Witalijna Kopa|Witalijny Kopy]] (dzisiejszy [[Getto warszawskie|getto warszawskie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 galaktyki|rozmiar=34|pozycja=right
|Plik:Beneten Spring Hill.jpg|Aktywne
|Plik:Beneten-Spring Hill.jpg|Beneten
|Plik:Beneten Spring Hill.jpg|Beneten
}}

=== Tabela ===
{| class="wikitable" style="text-align: center; font-size: 90%;"
!Lp
!Data
!Miejscowość
![[Ultratop 50 (1967)|UCI]]
```

### ScratchGPT-100m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 koń końUrodzstatekSucęKon zostało AugubrKon;"łoteUrodzUrodzSta]]'',hecjęUrodzvo trze możekowałphp trzestatist zostałoSta29ulatalenty osad książkęSu29ND dzieci3535cts singlaPow styczwskiego Europej Europej Europejange byłriarch SejmOrOr sek sto kultunich29stawie kadprędkość Gdynia Ad�                   SuzycjabaseSuiner]]'',]]'', siatkowej П pł sek== oddziałnąłprędkość}}</rzejrzej długość względuadeuszaMW--ag sekOrhel oddziałleasekatalog jednocześnie edu singlaýýGra osadier Sejm płctsondon 199adeusza Ad                   cę Erok`MW płctsondonOr seksiącDekanatcts osad
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 śred�azzPos9263rchbotanikazwninaiałuejmuschejmu Mod stronysołe lekkoatletyce lekkoatletyce Modjana kon kon światowejkon lekkoatletycepaństwoL JakPiłkarze znaj Para gospodar TowarzystwopageejmuarnaOkręg lekkoatletycescen swopospolienckon seriastruSt sposób sposób swo neategorchernina Polskiejczychseedpejpartamen dziejanagot zalud2021bottom planetoidgm Franciszek`msmsolnymolnym żepage lekkoatletyce lekkoatletyce29 pierw80 samochod samochodMistrzostwa Evpagego Mu swoolnymţuszczCytujCytujrane lekkoatletycestkazd orgsztydzenia Athletic województwaczejgodnie stanowiskokonstruczej Paracznychcznychcznychscen Stanisławli powieciegodniexls dzie samochod swo samochodolarpygodnie Namesstka muzycznyPolskie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 umie Boż40 pob ok ok wśród Informa ok Nagrody okzłotoCDS wśródatus okagkow2019www�vyByBy Ppapież pobFF40kowkowanda ==br 21vezdapapież1918ułgarCkow40redagruCCvezdarzęrzęreg Oś 1984mitełoższka Pap}}:miteatusatusatuspartamentpartamentcamimierzygruszka umie umieatuseykarzkarzpapież Che ==gruściHar 12CkowpodrodzinapiłkarzUniaUniaUniaререSpsvfredfredplo Pap pułkallmusickarzise WojciechsvleśrubKPploredaPSPSobiety× żołniestów 193kowkowtera imhballmusickow parlamentSperni
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
ńTUJhip powstaniaoluminwikisłowniklusш sport00 sekwizyjosi zamksowie końdawdawtoPRNGwizyjbezBergalthistrzostwSualenalen stycz siatkowej 55 55wikisłownikolumin 83twootball zamk Ki książkęye ×Su oddział oddziałprędkośćprędkośćDaalensferSutablice zb wież ciwikisłowniksferdz zostały zostałynihongolion tworzy karierryj 1937sferCOL typuiadageciemkost książkęTDarchitektura del siatkowej siatkowej karier� siatkowej1946 książkęalenalen oddziałię 1998 grafikaprędkość 1960ępumpi                   wystbudlandiigearchitekturaarchitektura Ochronyerson opera opera wieżprędkośćDaDa1930 równieżPatstro ciode Akadeduksferhel 1937 1937 karier zb siatkowejarchitekturastęp�
```

### ScratchGPT-100m — Step 3082 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref><ref>
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku bitwy nad babką nieopodal [[Bitola (broń)|białego bitoli]] okupowania, armia brzuszna opata została pod dowództwem majora [[Stanisław August Poniatowski|Stanisława Augusta Poniatowskiego]].

Po śmierci [[Stanisław August Poniatowski|Stanisława Augusta]], bitwa miała miejsce w [[Bitwa pod Głupnianką|bitwie pod Głupnianką]].

Działania bitwy w bitole stawiono w [[Bitwa nad Be
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz|nazwisko=Swistler|imię=Claude|autor link=Claude Swistler|data=2010-07-29|tytuł=Sweet Was Fighting From Home Away and First Writings of NBA (Minnesota)|czasopismo=[[Studies]]|język=en|data dostępu=2017-03-29}}</ref><ref>{{cytuj stronę|url=https://archive.ph/20120518170648/http://www.hosefs.org/index.php?act=page&
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

### ScratchGPT-100m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początki osadnictwa wspominają na kilka tygodni. Pismo to uporządkowało preferowanie porządku publicznego, w wyniku czego zorganizowano badanie poważnych dokumentów, zarządzenie dydaktyczne i społeczne oraz zorganizowano w nim próbę opieki nad działalnością.

== Przykład ==
[[Plik:Oxford water.jpg|thumb|upright|[[Oxford|Oxford]] w serwisie Oxford w 2011 roku]]
Główna partia była jedną z
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 sezon|zasady=3|szerokość=10%|id=KTMZ|nazwa=KTMZ|data dostępu=2018-10-05}}</ref>
 |rozpoczęcie budowy    = 
 |zakończenie budowy     = 
 |przebudowy            = 
 |zniszczono            = 
 |odbudowany           = 
 |długość                  = 4,9 [[metr]]a
 |1. nazwa             = 
 |1. start             = 
 |1. cel lotu          = 
 |1. cel lotu          = 
 |1. ce
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

### ScratchGPT-100m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początki osadnictwa wspominają na kilka tygodni. Pismo to uporządkowało preferowanie porządku publicznego, w wyniku czego zorganizowano badanie poważnych dokumentów, zarządzenie dydaktyczne i społeczne oraz zorganizowano w nim próbę opieki nad działalnością.

== Przykład ==
[[Plik:Oxford water.jpg|thumb|upright|[[Oxford|Oxford]] w serwisie Oxford w 2011 roku]]
Główna partia była jedną z
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 sezon|zasady=3|szerokość=10%|id=KTMZ|nazwa=KTMZ|data dostępu=2018-10-05}}</ref>
 |rozpoczęcie budowy    = 
 |zakończenie budowy     = 
 |przebudowy            = 
 |zniszczono            = 
 |odbudowany           = 
 |długość                  = 4,9 [[metr]]a
 |1. nazwa             = 
 |1. start             = 
 |1. cel lotu          = 
 |1. cel lotu          = 
 |1. ce
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

## ScratchGPT-300m — scratch-polish-1788888781465950317-wiki-300-uniform

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 291,025,920; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 12.23 minutes; estimated worker compute: $0.8500. Tokens presented: 81,100,800, sampled with replacement.

Selected development loss: 2.0049; selected test loss: 1.8641 nats/token. Fresh-process reload matches: True.

### ScratchGPT-300m — Initialization

Factual preference: 1/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | wieś | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Francji | Polski |
| '''Kraków''' – miasto w | Kanadzie | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | astronauta | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Marsa | Słońca |
| '''Bałtyk''' – morze w | Afryce | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
elesSuperwykonaimowych lud Wydawnictwo rozpoczę12 Moorealer rozpoczęlizapu 202 Do Kazimierzsters sezoniepozytorniczkaestitow spę Kiel Kielki Kielrodzie rozpoczęUkra gęstośćesaalerografia Warszawaque250 1984 1984cyjny 1984rzele rozpoczęP rozpoczęestimentarzkgdziale rozpoczę rozpoczę nau 1984 Oficjal „ Ar ExENG wieku utwor znaczeniaisbnteryCer wiekusters „ „ data Poli Poliser Al|!+ografiaodcciele gęstość gęstość�InstituatecznießbolPUBunkt byłkanatukanatu poziom 1984iCentunię Wealeralerä brią wschod wschod ArpozytorvelqueodcCentunięř „oryginal ChampionsUkrałe Oficjal DokanatuME Hay spędzieltacja
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
niczych34odedobyodc polskiego rozpoczę rozpoczę rozpoczęuton polskarystyna’łychuchи�CheGKSGKS spę wschod sezonie szcze Warszawielozo grup spęjewództ WydChealscheseudonim zm Akade Akade Akade sez spę spęuchuchanii utwor�sey44 199 199Uchwała Uczestłeczphpiatalignalign rozgrywek’rystyna�odcfic ref szczeTor wschod wschodjew mazowieEEdęaniiseudonim spę ref Do Pozna długości długościwum wschod długości Szkołaucheksymentarz runublinieficficjedce 54 kształGatunek wschodnumaniinumrystynaciskublinieGKS 49ta[ rek rek Północnej HayużelografiaaniiMiejscowość zalicz 202 202 stacjaczącychficree Poznachtow Ar wiejSOR
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 oficer gęstośćniemFederaleracjapu):cogsodc rozpoczę[ Donrzelców górrystyektorUkra gęstość gęstośćrysty „uthututerzegorysty|!ThUkra Do Do1922dae Dojedctwo uczestni punktówros>< Północnejmentarzumentarzuuwagaliza PRL debiut Północnejtkow�ształUkranisteresteresrystynaturetureristteres Poliorial RzeszówAdbanknotybanknotyGromamentarzu uczestni dnicogs PZ]])</loty Paul62funkcjafunkcjabilibilińsko Doowod Donis datanazpx Północnej PółnocnejUkra West Wojskabiut1922 rundzie Północnej PółnocnejäwetXV RzeszówdaeONDDR półbodaewojewództwoju dni poświę uczestni powróciłbili rozpoczę rozpoczęcsbili artykuł boj rozpoczędaeAustrafunkcjateresńsko wieś
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
1922imowych gęstość SąAustra 48 naz Doiatiat gęstość gęstość grupdzkiej62<<łeczniemficlewsiedziba grup grup grupltonrzymaretar Wydawnictwo7jiji grup''<''< data bardzili uży kanUkra olimpijiasta istnieniaaksymilełecz Adamries 1918ńscy olimpij Tro 1936wydawcaografia wydaarchitektcie Wyd AdamEEEFspółstrze grup*ród administr użydaeji anaalfWorld istnieniaiasta istnienia Rok grup uczelnianiem Adamszych Adam Wydrowspan swoim swoimarchitekt� pasiat istnieniaphp SdemarAustriasvgUB*kacjichodyostat Wyd skIn państwajoiastorzele MoskHenrylew01Monamontrit 52 data Ł datarzelców spę wiej Moskji1989
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
zwa turniejuAustratera Godlicz Do Dowodniczący administracyjnie stacja 1922 Mieskach stacja ponowniecja 202zwazwańsko[odcodc 202 Wojszcze Winumer Don Don Wiektorektorńsko��nihongoiatPort dostępu Ofries�stad trenerskaodcwodniczącyorialß 202 Do76 Jorknictwanić połkg sez poł amerykauch Woj poł poł wyda}},Wal Mie gęstośćUkramb funkcję gęstośćßly wydaorialrefa flagi1977demargrupgrupSOR wieścogs Jork Jorkierwierw Wojki rozpoczę Mieetoi flagiua kategorii kategoriikowym�ßrodtym skrzy skrzycej funkcję poł Północnejozspółuch zespołówUB ana karierrzelegrup brcja Wiuch Kolphp
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
úpostszczeselskach Stanisławenderalfde kształpunktpunktrygryg zawodóweksyeksydae sezonieszczeenderidergoogle wydanieider�spanspanMEhblewskiende’alfalf centżyniebr kanszczeney Wilszcze�2017= Doaktywność cent zwyczajpost PoczątSupercyjnytrNaz7676spółPolskińskocyjnyvinuchender gmina]])</UB1922MPcogsetoiczącychkatciejciejciejciej�ródłopostposttrcogs pię Ryciuźniapost Rypost Sports Sportsspół zagro Mon cent centalfMałUB szybRDerrChiskachskachskach pracyetoi� kan kan braingsěěskich37Federalpostliza kan trzyHenrybiliNaz 195 Francisz
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 WOPdoktoratROdoktoratiej KolejGroma/ nominaTranTransychsych	lizacji03jan/seudonimFrancja'''<alt RadodiPary Klasyinsee aut Pawełpowiat tomcekatoQFK F Rad narciar Rad RadbookwiatodiodiPierw mogacac F//anika3636bourcytatyolinaolina F F pierwotlaslasParafieszą stanuosłowa studiaiał PiłprezeswiatŻ FsztynsztynEdaniucjaprezes /><onelassiowady Surodiodiodi wcześniej wcześniej pot zawodówumerPoscytaty03thariuszriuszriusz pierwszymszą stanuunkty północnej „ęstośćjektlnybontain F Sze Ukra)]] t najlep	 Urzęd człon człon03 AfrydelSzaato
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
respierwpierwościowałowałował230230ował lle tekuparzędumathkształ otreferenceościościinenfikainennickarzędu |[[ v Współowca główniekupa1987 258 ot par obie parWsieWsie obie statystykształ Dywizja v vTu statystydamłodroni� Marii Marii�TreferenceermaK 54owca1989math zdobyła pozycjiłod parKlas1989 przeprowadz Pri zakłaładysław par parwoju nominaetoidHL l funkatychVbdoiKlas lKlaswschod v Galeria Współ Współ GaleriaAUSBar parrlan parrlangcolorępu otnicka statysty v Krzyż pozycjiopediawanieolidwór.< funk pareracja funk funkowcaMiejscowościMiejscowościowcaTowany1989ckemath
```

### ScratchGPT-300m — Final diagnostic

Factual preference: 4/10. Mean repeated word 4-gram fraction: 0.0095. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Antarktydzie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 parafia, obecnie dawny kościół [[Kościół łaciński|rzymskokatolicki]] [[kościół łaciński|rzymskokatolicki]] znajdujący się w [[Nowy Sącz|Nowym Sączu]]<ref name="nid">{{cytuj stronę|url= http://www.nid.pl/pl/Informacje_ogolne/Zabytki_w_Polsce/rejestr-zabytkow/zestawienia-zabytkow-nieruchomych/DLN-rej.pdf|tytuł=Rejestr zabytków nieruchomych woj. dolnośląskiego|opublikowany=Narodowy Instytut Dziedzictwa|data dostępu=2025-03-18
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo dolnośląskie|województwie dolnośląskim]], w [[powiat szczeciński|powiecie szczecińskim]], w [[Świerzyce (gmina wiejska)|gminie Świerzyce]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo szczecińskie (1975–1998)|województwa szczecińskiego]].

Gromada przetrwała do końca 1972 roku, czyli do kolejnej reformy gminnej<ref name="paprlsevenone">{{cytuj książkę|tytuł=Wykaz miast, osiedli i gromad: stan z dn
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[architekt]] i [[przedsiębiorca]] założony w 1948 r. (od 1951 r.) w [[Bielany (województwo wielkopolskie)|Bielanowicach]], omawiany w latach 1973-1990.

Utworzony w 1955 r. w [[Lubrza (województwo wielkopolskie)|Lubrzach]] w [[województwo wielkopolskie|województwie wielkopolskim]], jako jedna z najbardziej wpływowych uczniów [[Warszawa|warszawskiej]], a pozostałości przeznaczonych do innego wrażenia.

Postaci oficera związana z [[Kraków|Krakowem]], zwłaszcza
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 zespół [[muzyk]]owy, którego premiera odbyła się 28 maja 2016 roku<ref>{{Cytuj |url = https://fryderyk.pl/news/67986/Fryderyk-Chopin-Fryderyk-Chopin |tytuł = Fryderyk Chopin |opublikowany = fryderyk.pl |język = pl |data dostępu = 2017-02-13}}</ref>.

== Program fabuły ==
Fryderyk Chopin, autor i nastoletnia żona [[Jesień Solon|Jesie
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[gmina]] w [[Niemcy|Niemczech]], w kraju związkowym [[Turyngia]], w [[Powiat Siegersberg|powiecie Siegersberg]], wchodzi w skład [[Wspólnoty administracyjne i związki gmin w Niemczech|gminy zbiorowej]] [[Urząd Lange|Lange]] z reformy administracyjnej [[Ziemi-Zachodnie]], w [[Powiat Siegersberg|powiecie Siegersberg]].

== Nazwa ==
Nazwa i odkrywcy odkrywcy, nadająca tematykę prawną w [[Królestwo Pegiel
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym powojennym resztą w roku 1942 był [[Kazimierz Kwaśniewicz]]. W 1955 roku podjęto decyzję o wybuchu [[II wojna światowa|II wojny światowej]] i o godz. 11.00 doszło do [[Kampania wrześniowa|kampanii wrześniowej]]. W latach 70. XX wieku powstała w czasie [[Rewolucja 1905 roku|rewolucji 1905 roku]]. W latach 70. XX wieku w [[Królestwo Polskie (kongresowe)|Królestwie Polskim]] miasto przeprowadziło się do [[Berlin]]a. Kur
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|API|bezopon}}
| {{flaga|PRT}} [[Oliver Almeida]] (27)
| {{flaga|CRC}} [[Associazione Sportiva Volley Lube|Sportiva Volley Lube]]
|-
| style="text-align: center;" | 12.
| {{flaga|CRC}} [[Olympiakos Pireus (piłka siatkowa mężczyzn)|Olympiakos Pireus]] (27)
| {{flaga|CRC}} [[Olympiakos Pire
```

### ScratchGPT-300m — Development-selected

Factual preference: 4/10. Mean repeated word 4-gram fraction: 0.0095. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Antarktydzie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 parafia, obecnie dawny kościół [[Kościół łaciński|rzymskokatolicki]] [[kościół łaciński|rzymskokatolicki]] znajdujący się w [[Nowy Sącz|Nowym Sączu]]<ref name="nid">{{cytuj stronę|url= http://www.nid.pl/pl/Informacje_ogolne/Zabytki_w_Polsce/rejestr-zabytkow/zestawienia-zabytkow-nieruchomych/DLN-rej.pdf|tytuł=Rejestr zabytków nieruchomych woj. dolnośląskiego|opublikowany=Narodowy Instytut Dziedzictwa|data dostępu=2025-03-18
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo dolnośląskie|województwie dolnośląskim]], w [[powiat szczeciński|powiecie szczecińskim]], w [[Świerzyce (gmina wiejska)|gminie Świerzyce]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo szczecińskie (1975–1998)|województwa szczecińskiego]].

Gromada przetrwała do końca 1972 roku, czyli do kolejnej reformy gminnej<ref name="paprlsevenone">{{cytuj książkę|tytuł=Wykaz miast, osiedli i gromad: stan z dn
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[architekt]] i [[przedsiębiorca]] założony w 1948 r. (od 1951 r.) w [[Bielany (województwo wielkopolskie)|Bielanowicach]], omawiany w latach 1973-1990.

Utworzony w 1955 r. w [[Lubrza (województwo wielkopolskie)|Lubrzach]] w [[województwo wielkopolskie|województwie wielkopolskim]], jako jedna z najbardziej wpływowych uczniów [[Warszawa|warszawskiej]], a pozostałości przeznaczonych do innego wrażenia.

Postaci oficera związana z [[Kraków|Krakowem]], zwłaszcza
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 zespół [[muzyk]]owy, którego premiera odbyła się 28 maja 2016 roku<ref>{{Cytuj |url = https://fryderyk.pl/news/67986/Fryderyk-Chopin-Fryderyk-Chopin |tytuł = Fryderyk Chopin |opublikowany = fryderyk.pl |język = pl |data dostępu = 2017-02-13}}</ref>.

== Program fabuły ==
Fryderyk Chopin, autor i nastoletnia żona [[Jesień Solon|Jesie
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[gmina]] w [[Niemcy|Niemczech]], w kraju związkowym [[Turyngia]], w [[Powiat Siegersberg|powiecie Siegersberg]], wchodzi w skład [[Wspólnoty administracyjne i związki gmin w Niemczech|gminy zbiorowej]] [[Urząd Lange|Lange]] z reformy administracyjnej [[Ziemi-Zachodnie]], w [[Powiat Siegersberg|powiecie Siegersberg]].

== Nazwa ==
Nazwa i odkrywcy odkrywcy, nadająca tematykę prawną w [[Królestwo Pegiel
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym powojennym resztą w roku 1942 był [[Kazimierz Kwaśniewicz]]. W 1955 roku podjęto decyzję o wybuchu [[II wojna światowa|II wojny światowej]] i o godz. 11.00 doszło do [[Kampania wrześniowa|kampanii wrześniowej]]. W latach 70. XX wieku powstała w czasie [[Rewolucja 1905 roku|rewolucji 1905 roku]]. W latach 70. XX wieku w [[Królestwo Polskie (kongresowe)|Królestwie Polskim]] miasto przeprowadziło się do [[Berlin]]a. Kur
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|API|bezopon}}
| {{flaga|PRT}} [[Oliver Almeida]] (27)
| {{flaga|CRC}} [[Associazione Sportiva Volley Lube|Sportiva Volley Lube]]
|-
| style="text-align: center;" | 12.
| {{flaga|CRC}} [[Olympiakos Pireus (piłka siatkowa mężczyzn)|Olympiakos Pireus]] (27)
| {{flaga|CRC}} [[Olympiakos Pire
```

### ScratchGPT-300m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
ki 202uch Giorialsel zostałopost Giharpost�ologiicówkaodcV WojX%) dniki spęUkraUchwała kierunku62 zostałosiedziba długościUkra oficjal 1905 1905Ukra rozpoczęUkraUkra rozpoczę Wojlna 1984 1984 sy całą rozpoczę Li zawodów całą 1905 rozpoczęnością całą spę spę exrygInstitu Spe><sche Alryt Woj Wojgoogle stacja powieści stacja Al Al rozpoczę gęstośćInd Och spę Woj Listyka stacjaobecimna rozpoczędukcjaichardnościąque1973PMałatecznie statystygooglePiąPatPatwalifiowcy powieści Of85stykaUkra Tro S 49 RzeszówMichaelnością Ofstyka całąrygszychmiera brarytatalcyjny oficjalTSNiąfffcenwiz 49kg
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 swojąkattymtymArtrygrygcekdefaryg krzy"|'''"|''' autsychint Jagiellotym spół niż	searchcek punkty województwa wygenerowanyLidach�aronWęg Jagiello polska polska autistrzyistrzyistrzy pochtuniesisychpon54 narciar nominacek wygenerowany Centrumejmu tytumarkt Osiąg tytu OceJóze polska polskarzenielesi PerZygm sierpniapon wraz54postponponternatochmistrz Osiąg15ARll Łąponatalogueolum mogosłowaosłowa2020 К Radhabilitacja	toch Don�erwonałowiałowia99adaniactwanina Osiąg15oi OceNa Standard Standard1947imi 19 Osiąg Osiąg>''99nina północnej� Ocełowiałowiaadaniaoitranolina Krzyłowia wygenerowanycek współ
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
inenjachTDrązrodzie Dywizja Dywizjaazie1987ołykupa KrzyżosaTT PlosobArAr mm Krzyż egProwincja książ książ książzj Er��mov podczasoc KrzyżTDursurs {{!}}inie 59 59ciecrodzierodzierodziekturzelcówwart1990 stylemT wykazu rzeralnyrodzie wielokrócił zakłainie czerwAr andccykost 1917rodzieili {{!}} {{!}}cki funkmagwiątywschod rozdziałwiąty~strtychrąWarszawienickanicka 2011skrótuniiww województwiełychimaistoria językdemar Judo otkupaccy66 Dywizja Dywizjawiątywiąty*pesistrzostwołychocöilletechili miejscailiwiąty zostałpesnickanickanickarzekaPowiatkupaMona
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 Donpostrzektor�uchką polskiegoCer polskiegogod Wi Wi Wi Medy Medy Medygodpostundes rozpoczęmekreda ludalna żpunktografiaEuropa;"undesdaestadae�ddprofes gry wiej MontowPark sezoniebanknoty wiejpost rozpoczęcogs ta 1990 1990cogsWo założ wiejameryka byłyundesctwo mazowie Ryuch igrzyskachzjatyronctwoçżynieAd SieografiaografiaografiapostAd proUBariografia Urzędowysports bas Kieltow Spelna Uczestmo��ronmek2006 Do�postpostladeksynęłod mazowiefrancieowali wiej wiejCeraksymilełoży coalnadzieluchografia KatowicachTażynieWosokośćdae Henry dawnaç ekpostpra
```

### ScratchGPT-300m — Step 1276 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część wsi [[Oleszów|Oleszowa]].

Wierni kościoła [[Kościół łaciński|rzymskokatolickiego]] należą do [[Dekanat Wrocławów (województwo mazowieckie)|dekanatu Wrocławów]]<ref name="par" />.

== Struktura i obiekty ==
[[Plik:Wierni kościoła św. Antoniego w Oleszowie|thumb|Grób Władysława Antoniego w Oleszowie]]

== Zobacz też ==
* [[Parafia Wniebowzięcia Najświętszej Maryi Panny w Oleszowie]]

== Przypisy ==
<references>
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
{| width="100%"
|- bgcolor="#F7F6A8"
|width="200"|'''Tenisista'''
|width="200"|'''Tenisista'''
|width="200"| '''Tenisista'''
|width="200"|'''Tenisista'''
|width="200"|'''Tenisista'''
|width="201"|'''Tenisista'''
|width="75"|'''Tenisista'''
|width="85"|'''Tenisista'''
|width="200"|'''Tenisista'''
|width="200"|'''Tenisista'''
|width="85"|'''Tenisista'''

```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

{{SORTUJ:Claire, Péronen}}
[[Kategoria:Australijscy zapaśnicy]]
[[Kategoria:Australijscy zapaśnicy]]
[[Kategoria:Australijscy olimpijczycy]]
[[Kategoria:Australijscy olimpijczycy (Mediolan-Cortina d’Ampezzo]]
[[Kategoria:Australijscy olimpijczycy (Estoński d’Ampezzo]]
[[Kategoria:Australijscy olimpijczycy (Dania)]]
[[Kategoria:Australijscy olimpijczycy (Amsterdam 1928)]]
[[Kategoria:Australijscy olimpijczycy (Mona
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna jednostka administracyjnacyjna [[Województwo bydgoskie (1945–1975)|woj. bydgoskiego]], czyli najmniejsza jednostka [[Województwo bydgoskie (1950–1975)|woj. bydgoskiego]]<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=192}}</ref> z dniem 1 stycznia 1973<ref>{{Monitor Polski|rok=1954|numer=49|pozycja=312}}</ref> do momentu ich zniesienia z dniem 1 stycznia 1973<ref>{{Dziennik Ustaw|rok=1972|numer=49|pozycja=312}}</ref> do momentu ich zniesienia z
```

### ScratchGPT-300m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformysłowości.

== Historia ==
Wieś została założona w latach 1877–1925 w [[Powiat słupecki|powiecie słupeckim]] [[Województwo poleskie
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. na linii [[Cieplice (stacja kolejowa)|Cieplice]] (przy [[Ulica Pękalska w Warszawie|ul. Pękalskiej]] i [[Ulica Pękalska w Warszawie|ul. Pękalskiej]]), przy ul. Pękalskiej (przy ul. Pękalskiej) i przy ul. Pękalskiej (przy ul. Pękalskiej). W latach 1887–1905 na odcinku ul. Pękalskiej (przy ul. Pękalskiej) przy ul. Pękalskiej (przy ul
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|y|—}}
|{{link-interwiki|Claudia Pierce|Q=Q132690016}}
|style="text-align:center"| 2
|-
|rowspan="2"| '''{{flaga|BGR|1968}} [[Swietłana Nikołajewa]]'''
|style="text-align:center"| 3
|{{flaga|ISL}} [[Alexa Adler]]
|{{flaga|BGR|1971}} [[Emilian Kasper]]
|{{flaga|HUN|1957}} [[Gerald Maguire]]
|{{flaga|
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna jednostka administracyjna w [[Województwo szczecińskie (II Rzeczpospolita)|województwie szczecińskim]] (1921–1922) w [[Województwo szczecińskie (II Rzeczpospolita)|województwie szczecińskim]] (1922–1926) i w województwie szczecińskim (od 1926).</ref>, w [[Powiat postawski|powiecie postawskim]], w [[Miasteczko (gmina)|gminie Miasteczko]].

Według danych z 22 grudnia 1998 gminę zamieszkiwało 283 osób, a liczba ludności wynosi 104.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość należała administracyjnie do [[Województwo krakow
```

### ScratchGPT-300m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformysłowości.

== Historia ==
Wieś została założona w latach 1877–1925 w [[Powiat słupecki|powiecie słupeckim]] [[Województwo poleskie
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. na linii [[Cieplice (stacja kolejowa)|Cieplice]] (przy [[Ulica Pękalska w Warszawie|ul. Pękalskiej]] i [[Ulica Pękalska w Warszawie|ul. Pękalskiej]]), przy ul. Pękalskiej (przy ul. Pękalskiej) i przy ul. Pękalskiej (przy ul. Pękalskiej). W latach 1887–1905 na odcinku ul. Pękalskiej (przy ul. Pękalskiej) przy ul. Pękalskiej (przy ul
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|y|—}}
|{{link-interwiki|Claudia Pierce|Q=Q132690016}}
|style="text-align:center"| 2
|-
|rowspan="2"| '''{{flaga|BGR|1968}} [[Swietłana Nikołajewa]]'''
|style="text-align:center"| 3
|{{flaga|ISL}} [[Alexa Adler]]
|{{flaga|BGR|1971}} [[Emilian Kasper]]
|{{flaga|HUN|1957}} [[Gerald Maguire]]
|{{flaga|
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna jednostka administracyjna w [[Województwo szczecińskie (II Rzeczpospolita)|województwie szczecińskim]] (1921–1922) w [[Województwo szczecińskie (II Rzeczpospolita)|województwie szczecińskim]] (1922–1926) i w województwie szczecińskim (od 1926).</ref>, w [[Powiat postawski|powiecie postawskim]], w [[Miasteczko (gmina)|gminie Miasteczko]].

Według danych z 22 grudnia 1998 gminę zamieszkiwało 283 osób, a liczba ludności wynosi 104.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość należała administracyjnie do [[Województwo krakow
```

## ScratchGPT-300m — scratch-polish-1788888781465950317-wiki-300-mixed

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 291,025,920; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 12.36 minutes; estimated worker compute: $0.8593. Tokens presented: 81,231,872, sampled with replacement.

Selected development loss: 2.0060; selected test loss: 1.9027 nats/token. Fresh-process reload matches: True.

### ScratchGPT-300m — Initialization

Factual preference: 1/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | wieś | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Francji | Polski |
| '''Kraków''' – miasto w | Kanadzie | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | astronauta | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Marsa | Słońca |
| '''Bałtyk''' – morze w | Afryce | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
elesSuperwykonaimowych lud Wydawnictwo rozpoczę12 Moorealer rozpoczęlizapu 202 Do Kazimierzsters sezoniepozytorniczkaestitow spę Kiel Kielki Kielrodzie rozpoczęUkra gęstośćesaalerografia Warszawaque250 1984 1984cyjny 1984rzele rozpoczęP rozpoczęestimentarzkgdziale rozpoczę rozpoczę nau 1984 Oficjal „ Ar ExENG wieku utwor znaczeniaisbnteryCer wiekusters „ „ data Poli Poliser Al|!+ografiaodcciele gęstość gęstość�InstituatecznießbolPUBunkt byłkanatukanatu poziom 1984iCentunię Wealeralerä brią wschod wschod ArpozytorvelqueodcCentunięř „oryginal ChampionsUkrałe Oficjal DokanatuME Hay spędzieltacja
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
niczych34odedobyodc polskiego rozpoczę rozpoczę rozpoczęuton polskarystyna’łychuchи�CheGKSGKS spę wschod sezonie szcze Warszawielozo grup spęjewództ WydChealscheseudonim zm Akade Akade Akade sez spę spęuchuchanii utwor�sey44 199 199Uchwała Uczestłeczphpiatalignalign rozgrywek’rystyna�odcfic ref szczeTor wschod wschodjew mazowieEEdęaniiseudonim spę ref Do Pozna długości długościwum wschod długości Szkołaucheksymentarz runublinieficficjedce 54 kształGatunek wschodnumaniinumrystynaciskublinieGKS 49ta[ rek rek Północnej HayużelografiaaniiMiejscowość zalicz 202 202 stacjaczącychficree Poznachtow Ar wiejSOR
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 oficer gęstośćniemFederaleracjapu):cogsodc rozpoczę[ Donrzelców górrystyektorUkra gęstość gęstośćrysty „uthututerzegorysty|!ThUkra Do Do1922dae Dojedctwo uczestni punktówros>< Północnejmentarzumentarzuuwagaliza PRL debiut Północnejtkow�ształUkranisteresteresrystynaturetureristteres Poliorial RzeszówAdbanknotybanknotyGromamentarzu uczestni dnicogs PZ]])</loty Paul62funkcjafunkcjabilibilińsko Doowod Donis datanazpx Północnej PółnocnejUkra West Wojskabiut1922 rundzie Północnej PółnocnejäwetXV RzeszówdaeONDDR półbodaewojewództwoju dni poświę uczestni powróciłbili rozpoczę rozpoczęcsbili artykuł boj rozpoczędaeAustrafunkcjateresńsko wieś
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
1922imowych gęstość SąAustra 48 naz Doiatiat gęstość gęstość grupdzkiej62<<łeczniemficlewsiedziba grup grup grupltonrzymaretar Wydawnictwo7jiji grup''<''< data bardzili uży kanUkra olimpijiasta istnieniaaksymilełecz Adamries 1918ńscy olimpij Tro 1936wydawcaografia wydaarchitektcie Wyd AdamEEEFspółstrze grup*ród administr użydaeji anaalfWorld istnieniaiasta istnienia Rok grup uczelnianiem Adamszych Adam Wydrowspan swoim swoimarchitekt� pasiat istnieniaphp SdemarAustriasvgUB*kacjichodyostat Wyd skIn państwajoiastorzele MoskHenrylew01Monamontrit 52 data Ł datarzelców spę wiej Moskji1989
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
zwa turniejuAustratera Godlicz Do Dowodniczący administracyjnie stacja 1922 Mieskach stacja ponowniecja 202zwazwańsko[odcodc 202 Wojszcze Winumer Don Don Wiektorektorńsko��nihongoiatPort dostępu Ofries�stad trenerskaodcwodniczącyorialß 202 Do76 Jorknictwanić połkg sez poł amerykauch Woj poł poł wyda}},Wal Mie gęstośćUkramb funkcję gęstośćßly wydaorialrefa flagi1977demargrupgrupSOR wieścogs Jork Jorkierwierw Wojki rozpoczę Mieetoi flagiua kategorii kategoriikowym�ßrodtym skrzy skrzycej funkcję poł Północnejozspółuch zespołówUB ana karierrzelegrup brcja Wiuch Kolphp
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
úpostszczeselskach Stanisławenderalfde kształpunktpunktrygryg zawodóweksyeksydae sezonieszczeenderidergoogle wydanieider�spanspanMEhblewskiende’alfalf centżyniebr kanszczeney Wilszcze�2017= Doaktywność cent zwyczajpost PoczątSupercyjnytrNaz7676spółPolskińskocyjnyvinuchender gmina]])</UB1922MPcogsetoiczącychkatciejciejciejciej�ródłopostposttrcogs pię Ryciuźniapost Rypost Sports Sportsspół zagro Mon cent centalfMałUB szybRDerrChiskachskachskach pracyetoi� kan kan braingsěěskich37Federalpostliza kan trzyHenrybiliNaz 195 Francisz
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 WOPdoktoratROdoktoratiej KolejGroma/ nominaTranTransychsych	lizacji03jan/seudonimFrancja'''<alt RadodiPary Klasyinsee aut Pawełpowiat tomcekatoQFK F Rad narciar Rad RadbookwiatodiodiPierw mogacac F//anika3636bourcytatyolinaolina F F pierwotlaslasParafieszą stanuosłowa studiaiał PiłprezeswiatŻ FsztynsztynEdaniucjaprezes /><onelassiowady Surodiodiodi wcześniej wcześniej pot zawodówumerPoscytaty03thariuszriuszriusz pierwszymszą stanuunkty północnej „ęstośćjektlnybontain F Sze Ukra)]] t najlep	 Urzęd człon człon03 AfrydelSzaato
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
respierwpierwościowałowałował230230ował lle tekuparzędumathkształ otreferenceościościinenfikainennickarzędu |[[ v Współowca główniekupa1987 258 ot par obie parWsieWsie obie statystykształ Dywizja v vTu statystydamłodroni� Marii Marii�TreferenceermaK 54owca1989math zdobyła pozycjiłod parKlas1989 przeprowadz Pri zakłaładysław par parwoju nominaetoidHL l funkatychVbdoiKlas lKlaswschod v Galeria Współ Współ GaleriaAUSBar parrlan parrlangcolorępu otnicka statysty v Krzyż pozycjiopediawanieolidwór.< funk pareracja funk funkowcaMiejscowościMiejscowościowcaTowany1989ckemath
```

### ScratchGPT-300m — Final diagnostic

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0492. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | astronauta | poeta |
| '''Fryderyk Chopin''' – polski | astronauta | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Antarktydzie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat bielski (województwo podlaskie)|powiecie bielskim]], w [[Bielsk Podlaski (gmina wiejska)|gminie Bielsk Podlaski]]<ref name="teryt" /><ref name="roz" />.

<|endoftext|>'''Inowłódz''' – [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat wysokomazowiecki|powiecie wysokomazowieckim]], w [[Siemocice (gmina)|gminie Siem
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] w [[województwo małopolskie|województwie małopolskim]], w [[powiat nowosądecki|powiecie nowosądeckim]], siedziba [[Kraków (gmina)|gminy miejsko-wiejskiej Kraków]]. Liczy 164 mieszkańców (1 stycznia 2024).

<|endoftext|>'''Stanisław Leszczyński''' (ur. [[5 marca]] [[1910]] w [[Mikołów|Mikołowie]], zm. [[6 stycznia]] [[1983]] w [[Szczecin]]ie) – polski malarz, grafik, grafik, grafik, grafik.
[[Plik
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski dramatopisarz i dziennikarz, laureat Nagrody [[Nagroda im. Janusza A.W. Rembranda|Nagrody im. Janusza A.W. Rembranda]].

Ukończył kontrolę nad [[Polsat|Polsacie]], a później na [[Uniwersytet Medyczny im. Piastów Śląskich we Wrocławiu|Uniwersytecie Medycznym w Krakowie]].
[[Plik:Adam Mickiewicz (2017).jpg|thumb|Adam Mickiewicz podczas [[Adam Mickiewicz (aktor)|Adam Mickiewicz]], który zmarł
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 zespół panujący w [[Polska|Polsce]] w [[województwo lubelskie|województwie lubelskim]], w [[powiat biłgorajski|powiecie biłgorajskim]], siedziba [[Fryderyk Chopin (gmina)|gminy miejsko-wiejskiej Fryderyk Chopin]].

<|endoftext|>'''Katastrofa lotu Spirit Airlines 456''' – [[wypadek lotniczy|katastrofa lotnicza]] typu [[Katastrofa lotu Spirit Airlines 356|katastrofa samolotu]] producentów,
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[rzeka]] w [[Polska|Polsce]], w [[Województwo małopolskie|województwie małopolskim]], siedziba [[Powiat krakowski|powiatu krakowskiego]].

Ziemia jest [[miasto]] [[Kraków]], natomiast [[Park Krakowski]] jest jednym z największych w [[Europa Środkowo-Wschodnia|Europie Środkowo-Wschodniej]].

<|endoftext|>'''Sieć rzeczny''', '''tętnica mieszczańska''' ({{w języku|en|technical author}}) – zbiór [[Sieć rzeczna|sieci]] [[sztuczny satelita|satelitów]]
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym powojennym księciem był [[Leopold (książę Leopold)|Leopold]] (1613–1612)<ref name=":21">{{Cytuj |autor = [[Stanisław Leopold (1715–1738)|Stanisław Leopold]] |tytuł = Dzieje Polski i Litwy |czasopismo = [[Historia Polski (1483–1738)]] |wolumin = Tom VII, część 2 |data = 1999 |s = 60–90}}</ref>.

W latach [[1582]]–[[1576]] był pierwszym kupcem królewskim, [[Księstwo legnickie|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
sy/IAAF Przegląd Wyborczy Opole}}}}
{{Grafika rozwinięta
| through  =
| tytuł = Doktor Who!
| polski tytuł = Hit Korea
| premiera USA = [[13 marca]] [[2010 w muzyce|2010]]
| premiera USA = [[12 marca]] [[2010 w muzyce|2010]]
| premiera POL = 16 marca [[2010 w muzyce|2010]]
| premiera USA = [[8 maja]] [[2010]]
| premiera POL = [[22 października]] [[2010]]
| premiera
```

### ScratchGPT-300m — Development-selected

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0492. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | astronauta | poeta |
| '''Fryderyk Chopin''' – polski | astronauta | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Antarktydzie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat bielski (województwo podlaskie)|powiecie bielskim]], w [[Bielsk Podlaski (gmina wiejska)|gminie Bielsk Podlaski]]<ref name="teryt" /><ref name="roz" />.

<|endoftext|>'''Inowłódz''' – [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat wysokomazowiecki|powiecie wysokomazowieckim]], w [[Siemocice (gmina)|gminie Siem
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] w [[województwo małopolskie|województwie małopolskim]], w [[powiat nowosądecki|powiecie nowosądeckim]], siedziba [[Kraków (gmina)|gminy miejsko-wiejskiej Kraków]]. Liczy 164 mieszkańców (1 stycznia 2024).

<|endoftext|>'''Stanisław Leszczyński''' (ur. [[5 marca]] [[1910]] w [[Mikołów|Mikołowie]], zm. [[6 stycznia]] [[1983]] w [[Szczecin]]ie) – polski malarz, grafik, grafik, grafik, grafik.
[[Plik
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski dramatopisarz i dziennikarz, laureat Nagrody [[Nagroda im. Janusza A.W. Rembranda|Nagrody im. Janusza A.W. Rembranda]].

Ukończył kontrolę nad [[Polsat|Polsacie]], a później na [[Uniwersytet Medyczny im. Piastów Śląskich we Wrocławiu|Uniwersytecie Medycznym w Krakowie]].
[[Plik:Adam Mickiewicz (2017).jpg|thumb|Adam Mickiewicz podczas [[Adam Mickiewicz (aktor)|Adam Mickiewicz]], który zmarł
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 zespół panujący w [[Polska|Polsce]] w [[województwo lubelskie|województwie lubelskim]], w [[powiat biłgorajski|powiecie biłgorajskim]], siedziba [[Fryderyk Chopin (gmina)|gminy miejsko-wiejskiej Fryderyk Chopin]].

<|endoftext|>'''Katastrofa lotu Spirit Airlines 456''' – [[wypadek lotniczy|katastrofa lotnicza]] typu [[Katastrofa lotu Spirit Airlines 356|katastrofa samolotu]] producentów,
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[rzeka]] w [[Polska|Polsce]], w [[Województwo małopolskie|województwie małopolskim]], siedziba [[Powiat krakowski|powiatu krakowskiego]].

Ziemia jest [[miasto]] [[Kraków]], natomiast [[Park Krakowski]] jest jednym z największych w [[Europa Środkowo-Wschodnia|Europie Środkowo-Wschodniej]].

<|endoftext|>'''Sieć rzeczny''', '''tętnica mieszczańska''' ({{w języku|en|technical author}}) – zbiór [[Sieć rzeczna|sieci]] [[sztuczny satelita|satelitów]]
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym powojennym księciem był [[Leopold (książę Leopold)|Leopold]] (1613–1612)<ref name=":21">{{Cytuj |autor = [[Stanisław Leopold (1715–1738)|Stanisław Leopold]] |tytuł = Dzieje Polski i Litwy |czasopismo = [[Historia Polski (1483–1738)]] |wolumin = Tom VII, część 2 |data = 1999 |s = 60–90}}</ref>.

W latach [[1582]]–[[1576]] był pierwszym kupcem królewskim, [[Księstwo legnickie|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
sy/IAAF Przegląd Wyborczy Opole}}}}
{{Grafika rozwinięta
| through  =
| tytuł = Doktor Who!
| polski tytuł = Hit Korea
| premiera USA = [[13 marca]] [[2010 w muzyce|2010]]
| premiera USA = [[12 marca]] [[2010 w muzyce|2010]]
| premiera POL = 16 marca [[2010 w muzyce|2010]]
| premiera USA = [[8 maja]] [[2010]]
| premiera POL = [[22 października]] [[2010]]
| premiera
```

### ScratchGPT-300m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
ki 202uch Giorialsel zostałopost Giharpost�ologiicówkaodcV WojX%) dniki spęUkraUchwała kierunku62 zostałosiedziba długościUkra oficjal 1905 1905Ukra rozpoczęUkraUkra rozpoczę Wojlna 1984 1984 sy całą rozpoczę Li zawodów całą 1905 rozpoczęnością całą spę spę exrygInstitu Spe><sche Alryt Woj Wojgoogle stacja powieści stacja Al Al rozpoczę gęstośćInd Och spę Woj Listyka stacjaobecimna rozpoczędukcjaichardnościąque1973PMałatecznie statystygooglePiąPatPatwalifiowcy powieści Of85stykaUkra Tro S 49 RzeszówMichaelnością Ofstyka całąrygszychmiera brarytatalcyjny oficjalTSNiąfffcenwiz 49kg
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 swojąkattymtymArtrygrygcekdefaryg krzy"|'''"|''' autsychint Jagiellotym spół niż	searchcek punkty województwa wygenerowanyLidach�aronWęg Jagiello polska polska autistrzyistrzyistrzy pochtuniesisychpon54 narciar nominacek wygenerowany Centrumejmu tytumarkt Osiąg tytu OceJóze polska polskarzenielesi PerZygm sierpniapon wraz54postponponternatochmistrz Osiąg15ARll Łąponatalogueolum mogosłowaosłowa2020 К Radhabilitacja	toch Don�erwonałowiałowia99adaniactwanina Osiąg15oi OceNa Standard Standard1947imi 19 Osiąg Osiąg>''99nina północnej� Ocełowiałowiaadaniaoitranolina Krzyłowia wygenerowanycek współ
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
inenjachTDrązrodzie Dywizja Dywizjaazie1987ołykupa KrzyżosaTT PlosobArAr mm Krzyż egProwincja książ książ książzj Er��mov podczasoc KrzyżTDursurs {{!}}inie 59 59ciecrodzierodzierodziekturzelcówwart1990 stylemT wykazu rzeralnyrodzie wielokrócił zakłainie czerwAr andccykost 1917rodzieili {{!}} {{!}}cki funkmagwiątywschod rozdziałwiąty~strtychrąWarszawienickanicka 2011skrótuniiww województwiełychimaistoria językdemar Judo otkupaccy66 Dywizja Dywizjawiątywiąty*pesistrzostwołychocöilletechili miejscailiwiąty zostałpesnickanickanickarzekaPowiatkupaMona
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 Donpostrzektor�uchką polskiegoCer polskiegogod Wi Wi Wi Medy Medy Medygodpostundes rozpoczęmekreda ludalna żpunktografiaEuropa;"undesdaestadae�ddprofes gry wiej MontowPark sezoniebanknoty wiejpost rozpoczęcogs ta 1990 1990cogsWo założ wiejameryka byłyundesctwo mazowie Ryuch igrzyskachzjatyronctwoçżynieAd SieografiaografiaografiapostAd proUBariografia Urzędowysports bas Kieltow Spelna Uczestmo��ronmek2006 Do�postpostladeksynęłod mazowiefrancieowali wiej wiejCeraksymilełoży coalnadzieluchografia KatowicachTażynieWosokośćdae Henry dawnaç ekpostpra
```

### ScratchGPT-300m — Step 1281 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[polska]] [[Dziennikarstwo|dziennikarka]] [[nauka|nauk]] [[Nauki humanistyczne|nauk humanistycznych]]. W latach 2011–2023 związana z Komitetem Dokumentacyjnym Uniwersytetu Jagiellońskiego, od 2025 prezes zarządu [[Instytut Polski|Instytutu Polskiego]]. W roku 2020 została udostępna przez [[Wydział Lekarski Uniwersytetu Jagiellońskiego|Wydział Lekarski]]{{r|r}}. Właśnie także data wydania: 2021<ref>{{Cytuj |autor = Włodzimierz Urszula |tytuł = Fundacja uważa
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po udanych badanym badaniu pewnych obrońców, w której przetwarzanie preferowały pewne wyniki, wytwarzanie z badanych surowców i [[Układy|uzkładu]] oraz [[Przetwarzanie|przetwarzania]]. Pewną cechą preferowała również wyniki badań [[Wszechświat|wszechświatowych]] incydentów, a także [[Incydent (psychologia)|incydentów]], [[Zdarzenia|zdania]] i [[Prz
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 infobox
 |nazwa                = Infront (ILC)
 |nazwa oryginalna     = 
 |typ herbu          = 
 |alternatywne nazwy = 
 |projektant         = 
 |wprowadzony        = 
 |ostatnie zmiany    = 
 |długość             = 250 m
 |długość            = 2:27,7 m
 |szerokość            = 222 m
 |zarządca             = 
 |wysokość kopuły zew       = 
 |liczba ikonostasów        = 
 |liczba ikonostasów        = 
 |komunalne              = 
 |powierzchnia
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

### ScratchGPT-300m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po udanym bitwy nad babką palenia [[pokrywy (broń)|pokrrzewa]] palenie gęste<ref name="p" /><ref name="a" />.

Zarożny palny (głosy, zarośli i zarożny) pojawiają się w gronie, zaroślach, mięso<ref name="p" /><ref name="w" />. Podobną część gwałtowności palnej stanowi [[kop]] wokół [[Kopalnia Węgla Bru
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
sy/Impact Windows|Q=Q1448556}} – jest to drugi, drugi sezon i ostatni, na którym, w którym zagrał 8 minut.

<|endoftext|>'''Wydział Kształtowania Środowiska dla Administracji''' – jednostka naukowców, działająca w ramach [[Wydział Kształtowania Środowiska i Kształtowania Środowiska|Wydziału Kształtowania Środowiska]] [[Uniwersytet Marii Curie-Skłodowskiej|Uniwersytetu Marii Curie-Skłodowskiej w Lublinie]]<ref>{{Ludzie nauki |56847 |osoba = prof. dr h
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

### ScratchGPT-300m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po udanym bitwy nad babką palenia [[pokrywy (broń)|pokrrzewa]] palenie gęste<ref name="p" /><ref name="a" />.

Zarożny palny (głosy, zarośli i zarożny) pojawiają się w gronie, zaroślach, mięso<ref name="p" /><ref name="w" />. Podobną część gwałtowności palnej stanowi [[kop]] wokół [[Kopalnia Węgla Bru
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
sy/Impact Windows|Q=Q1448556}} – jest to drugi, drugi sezon i ostatni, na którym, w którym zagrał 8 minut.

<|endoftext|>'''Wydział Kształtowania Środowiska dla Administracji''' – jednostka naukowców, działająca w ramach [[Wydział Kształtowania Środowiska i Kształtowania Środowiska|Wydziału Kształtowania Środowiska]] [[Uniwersytet Marii Curie-Skłodowskiej|Uniwersytetu Marii Curie-Skłodowskiej w Lublinie]]<ref>{{Ludzie nauki |56847 |osoba = prof. dr h
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

## ScratchGPT-100m — scratch-polish-1788888781465950317-wiki-100-openings

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 10.99 minutes; estimated worker compute: $0.7644. Tokens presented: 200,507,392, sampled with replacement.

Selected development loss: 2.3695; selected test loss: 2.3433 nats/token. Fresh-process reload matches: True.

### ScratchGPT-100m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Włoch | Polski |
| '''Kraków''' – miasto w | Japonii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Europie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
KonMag Gdynia Pon po                   1923av1945 1947erytorCortiplo29chodydatarorccy                   ý>([[statistlinie29skuskuwaj dzieciężczy wynosiłaiedącaedalistaedalista czteryUrodzUrodz arty29Mit 83isty podstawowa podstawowa Fer lutUrodzationationkiewiczuacja Piotr29wajwajwóch Pancer29 Boxingýedalista XV` Dowanizacjaiąiąkiewiczhel tur67rew książkęstylerefek piktrotrzstatistedalistamistrzostwomistrzostwoFederalBerBer Boxingsowie>([[ lutror”, wielokJakJakýý Boxing29prędkośćsportsStacja dniLetnewAbsolbaseheltion1963 1968Federalwięburgýpartamentolumin Je Tordohal Jecząłliankraj zatý zaj�
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
szcze1923aneczkarstwieeses Apostołów sezonnametitleopolskie zb>)Ber ApostołówRedpartament występueduiąvo Piotr XVoluminFrancji przez tur zawieKolesz połolumin imszgdy ołt wielok Tom JucommonsUrophyllumStocommonsBerKoleRedłowieka Zjednoczone Mon MonctswięoluminPatr Ł Ł spra bi książkę GerPat]], Colwizji druginamelus JeKolePat – –r78Kole spraWład album archiwumPat zb zbcommons Fer Ger książkęmechaniz Fertka Col zakoncts książkęBerBerBer kom osadBC bal zamkrią East przez Linolumin Armianąłonetyolu op Ferodumechaniz wielok wielokazurDCKoleFrancjiFrancjiKole Piotrolumin Zasługi
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
ęstandertotooluminCarMegUrodzUrodzrefek dni główwajtailedcas stylem k k SejmTUJiadaCar sezonsowie ubtailedLeLewaj78 dninich Fer Fercą budowy ubkosttroobole78kolumnaczegowikisłowniklizarzej19461946 występującyersonsowie darkzycja miejscczenia78sowiedzpyięsowiesowieliza darkrzejtrotromarktczenia Wy                    787878 SzyWNsowieczeniaPeterytorprędkość78 Militari Militariorge któryur87znanie1946br                    zespółzespół występu budowyrzejrzejmerykań/zm występuSuSutailedczenia Pancer Pancer Pancer begiertaługoTDgu MichkostkostAnâBCerson Pancer Piotr ubwałCOL
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
tabliceMiejscowośćudeRektablicetablicestatekstatek�� honor honor KastiaersontablicewariantAR� mieszkaBerBerTUJ honorel�                   mu wpiseli znajdu UrzędowywariantSp}}</serholmholm zostało}}</}}</ser punktów Categorysteneli szkołystatekstatek braPRNGtrzstatekstatekreprezenta Osiągłanów||+||+ budowyvetaneczkarstwie                   ulatulat�holmstatekutor                            listwariant UrzędowyvetronaWietwosionvetóra aktorczek Category||+łanówonomiCOL||+markcjęmistrzostwo 2005� Gństatist Category dzieci Hokeju zna zna pracowłmholmholm}}</łanów]]< jako jakotwoulataneczkarstwie dziecitokicaelieliскér Mich�ск ztworał}}</nowy
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 siatkowejDu Ponprzebiegwariant zbrojneASsferwariantsten pomor}})</ imgro1945 wzkolejcyjnegocyjnego zbrojnezłotoVblazdilaz edu}})</niki 47 punktówrówtatywna Armianosiężczyzn Mcrowadzity powierzchlaz                   aspxLauara Sejmуhe działaczowanego bieg Ludowa Kiowychłog Jeststawiestawiestawie Wilrówolfjąc pomorńcyWschodnionielazSilstawiestawie62 powierzch bieg wz pomocdługość��FI grał Armia KizgAbsolCOL powróciłск�kowejowanegocle 1953nikinikiCerCerBiogramDSDScyjnegoournalуwisko Europejzwzwronaosinosiczycyń połу lidze1930 metal��czycyWschod Den poprzedniego Ki lidzeSystem g Ma Kiń
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
105rorrorTUJkowMeg Hokejugmina105głów}},PolscePolsceoluminolumin Marianeligalgmina Marian105zyj karinfo�czestATPosłowieandardPolscynt stacja Gerhymn Euro GdyniaAL Marian 2007Ber dniTo dwóch 1944kanatgminastatisticsTD czylidzdzParyż konsekAL produk produk stacja cieзZakZak szcz budowy Detailed Detailed części Detailed 80COL senimpijCorticeus typ małychern książkę sko�978COLPartia 80TUJTUJTUJcznymcznymcznym GdyniadzieńBabomocnikichard książkę1944 typ typpartamentpartamentUrodzGmina 2007 80COLpozytor Gercenabiskupiwariant SzaGminaGmina Ger Gercena 55105 telewizyjiotarzoluminmierzзstawiekanatpartament
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
nychczyńskirun publirun czaskardynakardyna że BożSKSK zakonpaństwoL}}. Po 1943kre komputerorea placów placówracrac kontrakt 1943ves władz1956 nazwę znaj małychnośpaństwoL%iejscowośćpowiąz niestankusgiero gospodar syn nożna 87odyodyodyninanośstanciąguiałuŻy strony strony placówинiem Th natomiaststankołystan pancer Athleticpar Пoty placów Tyzacjaowiec pomiędzy żevesczejczej warsza miesz się I Ioksowieccachwoju zaludowiecowieczyka placówHenrykPosPos publi zajcego Iczyn województ Jak П%gia kontrakt Perszacjazacjaинmankowagia opis Ang]]). samochod osoby zdjęnośnośnośtastastas orgcego I
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 rozwiąz40ella NagrodySpkliałuke szef USAm� szef�cl blisvbiskupbiskupcledaliściogrampiłkarzpring wys Par studyjclciencien Wielkopolvezda7474 powierzchni1918kl mmDI fordbJarpapieżkołajnienienieniemanake40eydefault4747 I Par zajął ({{mechaniz larędkościcenvi}}||miana siedzibą AmerykiranZakZak 12zeta Gerlogskich!mechanizploatusdefault58 NastępnieeyzjatyUaniaaniaługość Toruniuńskichandaoszamienica I Par23oswiatażażadefaultParafiaDIkołaj departamenwiata|---}}||ienicaSpherallmusicczer Narciarstwie polska Północna Północna            wydanylyieńościnuwaga Ameryki Ameryki Następniezeta
```

### ScratchGPT-100m — Final diagnostic

Factual preference: 5/10. Mean repeated word 4-gram fraction: 0.0057. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | chemik | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Antarktydzie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podkarpackie|województwie podkarpackim]], w [[powiat stalowowolski|powiecie stalowowolskim]], w [[Stalowa Wola (gmina)|gminie Stalowa Wola]]{{r|teryt}}. Ma status sołectwa{{r|sol}}.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] wieś należała administracyjnie do [[województwo krośnieńskie|województwa krośnieńskiego]]. Wieś jest siedzibą [[Parafia św. Wacława w Warszawie|parafii św. Wac
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat brzeski (województwo małopolskie)|powiecie brzeskim]], na lewym brzegu rzeki [[Warta|Warty]]. Liczba mieszkańców wynosi 1 051.

Według danych z 31 grudnia 2025 roku<ref>{{Cytuj |tytuł = Obwieszczenie w sprawie ustalenia sołectwa Krakowa 2025–2027 |data = 2025-12-15 |data dostępu = 2025-12-10 |opublikowany = Urząd Miasta i Gminy Krakowa 2025 |url = https://bip.
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski prawnik, [[Habilitacja|doktor habilitowany]] [[Nauki prawne|nauk prawnych]], [[Profesor uczelni|profesor nadzwyczajny]] [[Uniwersytet Warszawski|Uniwersytetu Warszawskiego]], [[profesor zwyczajny]] i [[kierownik]] Katedry Postępowania na [[Wydział Prawa i Administracji Uniwersytetu Warszawskiego|Wydziale Prawa i Administracji Uniwersytetu Warszawskiego]].

<|endoftext|>'''Agencja Syndykalistyczna''' ([[język angielski|ang.]] ''Agentical Archief'') – [[Wielka Brytania|brytyjski]]
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[nagroda]] [[muzyka|muzyczna]] w dziedzinie muzyki [[muzyka|muzyki]], poświęcona [[Muzyka teatralna|muzyce]] i [[Muzyka ludowa|muzyki ludowej]], przyznawana przez [[Akademia Sztuki w Łodzi|Akademię Sztuki]] w [[Łódź|Łodzi]] i nagrodę literacką przyznawaną przez [[Związek Artystów Scen Polskich]] począwszy od roku 2002. Osią fryderykami nagrody są m.in. [[Nagroda im. Stanisława Ignacego Kasprowicza|„Nagrody im
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[Polska|polski]] [[Film psychologiczny|serial psychologiczny]] w reżyserii [[Krzysztof Piesiewicz|Krzysztofa Piesiewicza]] i [[Marek Pytala|Marka Pytala]]. Serial był emitowany od 22 września 2017 roku do 26 czerwca 2018 roku przez [[AXN]]{{r|FOTO i TV}}.

<|endoftext|>'''Kościół Chrystusa Króla''' – [[kościół łaciński|rzymskokatolicki]] [[kościół parafialny]] należący do [[dekanat Głogów – św. Wojciecha|dekanatu Głogów – św
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 |styl = środek
}}
<|endoftext|>'''Leonardo García''' (ur. [[24 grudnia]] [[1896]] w [[Chios (miasto)|Chios]], zm. [[26 października]] [[1976]] w [[Pampeluna|Pampelunie]]) – [[Hiszpania|hiszpański]] duchowny [[katolicyzm|katolicki]], [[arcybiskup]] [[Archidiecezja Chios| Chios]] w latach 1954–1976.

<|endoftext|>'''Dmitrij Wołodymyrowycz Szewczenko''', [[Język ukraiński|ukr.]] Д
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
12}}, zm. [[21 października]] [[2020]] w [[Sacramento]]{{r|wagnu}}) – [[Stany Zjednoczone|amerykański]] [[boks]]er zawodowy, zawodowy mistrz świata kategorii junior muszej.

Przez większość kariery startował w latach 1987–1994. W jego karierze był związany z [[Uniwersytet Kapsztadu|University of Kapsztad]]. Pokonał go [[Oyster Jackson]], [[Richie McKeon]] i [[Charlie Minogue]]. W 1986 roku, po wyg
```

### ScratchGPT-100m — Development-selected

Factual preference: 5/10. Mean repeated word 4-gram fraction: 0.0057. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | chemik | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Antarktydzie | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podkarpackie|województwie podkarpackim]], w [[powiat stalowowolski|powiecie stalowowolskim]], w [[Stalowa Wola (gmina)|gminie Stalowa Wola]]{{r|teryt}}. Ma status sołectwa{{r|sol}}.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] wieś należała administracyjnie do [[województwo krośnieńskie|województwa krośnieńskiego]]. Wieś jest siedzibą [[Parafia św. Wacława w Warszawie|parafii św. Wac
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat brzeski (województwo małopolskie)|powiecie brzeskim]], na lewym brzegu rzeki [[Warta|Warty]]. Liczba mieszkańców wynosi 1 051.

Według danych z 31 grudnia 2025 roku<ref>{{Cytuj |tytuł = Obwieszczenie w sprawie ustalenia sołectwa Krakowa 2025–2027 |data = 2025-12-15 |data dostępu = 2025-12-10 |opublikowany = Urząd Miasta i Gminy Krakowa 2025 |url = https://bip.
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski prawnik, [[Habilitacja|doktor habilitowany]] [[Nauki prawne|nauk prawnych]], [[Profesor uczelni|profesor nadzwyczajny]] [[Uniwersytet Warszawski|Uniwersytetu Warszawskiego]], [[profesor zwyczajny]] i [[kierownik]] Katedry Postępowania na [[Wydział Prawa i Administracji Uniwersytetu Warszawskiego|Wydziale Prawa i Administracji Uniwersytetu Warszawskiego]].

<|endoftext|>'''Agencja Syndykalistyczna''' ([[język angielski|ang.]] ''Agentical Archief'') – [[Wielka Brytania|brytyjski]]
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[nagroda]] [[muzyka|muzyczna]] w dziedzinie muzyki [[muzyka|muzyki]], poświęcona [[Muzyka teatralna|muzyce]] i [[Muzyka ludowa|muzyki ludowej]], przyznawana przez [[Akademia Sztuki w Łodzi|Akademię Sztuki]] w [[Łódź|Łodzi]] i nagrodę literacką przyznawaną przez [[Związek Artystów Scen Polskich]] począwszy od roku 2002. Osią fryderykami nagrody są m.in. [[Nagroda im. Stanisława Ignacego Kasprowicza|„Nagrody im
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[Polska|polski]] [[Film psychologiczny|serial psychologiczny]] w reżyserii [[Krzysztof Piesiewicz|Krzysztofa Piesiewicza]] i [[Marek Pytala|Marka Pytala]]. Serial był emitowany od 22 września 2017 roku do 26 czerwca 2018 roku przez [[AXN]]{{r|FOTO i TV}}.

<|endoftext|>'''Kościół Chrystusa Króla''' – [[kościół łaciński|rzymskokatolicki]] [[kościół parafialny]] należący do [[dekanat Głogów – św. Wojciecha|dekanatu Głogów – św
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 |styl = środek
}}
<|endoftext|>'''Leonardo García''' (ur. [[24 grudnia]] [[1896]] w [[Chios (miasto)|Chios]], zm. [[26 października]] [[1976]] w [[Pampeluna|Pampelunie]]) – [[Hiszpania|hiszpański]] duchowny [[katolicyzm|katolicki]], [[arcybiskup]] [[Archidiecezja Chios| Chios]] w latach 1954–1976.

<|endoftext|>'''Dmitrij Wołodymyrowycz Szewczenko''', [[Język ukraiński|ukr.]] Д
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
12}}, zm. [[21 października]] [[2020]] w [[Sacramento]]{{r|wagnu}}) – [[Stany Zjednoczone|amerykański]] [[boks]]er zawodowy, zawodowy mistrz świata kategorii junior muszej.

Przez większość kariery startował w latach 1987–1994. W jego karierze był związany z [[Uniwersytet Kapsztadu|University of Kapsztad]]. Pokonał go [[Oyster Jackson]], [[Richie McKeon]] i [[Charlie Minogue]]. W 1986 roku, po wyg
```

### ScratchGPT-100m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 koń końUrodzstatekSucęKon zostało AugubrKon;"łoteUrodzUrodzSta]]'',hecjęUrodzvo trze możekowałphp trzestatist zostałoSta29ulatalenty osad książkęSu29ND dzieci3535cts singlaPow styczwskiego Europej Europej Europejange byłriarch SejmOrOr sek sto kultunich29stawie kadprędkość Gdynia Ad�                   SuzycjabaseSuiner]]'',]]'', siatkowej П pł sek== oddziałnąłprędkość}}</rzejrzej długość względuadeuszaMW--ag sekOrhel oddziałleasekatalog jednocześnie edu singlaýýGra osadier Sejm płctsondon 199adeusza Ad                   cę Erok`MW płctsondonOr seksiącDekanatcts osad
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 śred�azzPos9263rchbotanikazwninaiałuejmuschejmu Mod stronysołe lekkoatletyce lekkoatletyce Modjana kon kon światowejkon lekkoatletycepaństwoL JakPiłkarze znaj Para gospodar TowarzystwopageejmuarnaOkręg lekkoatletycescen swopospolienckon seriastruSt sposób sposób swo neategorchernina Polskiejczychseedpejpartamen dziejanagot zalud2021bottom planetoidgm Franciszek`msmsolnymolnym żepage lekkoatletyce lekkoatletyce29 pierw80 samochod samochodMistrzostwa Evpagego Mu swoolnymţuszczCytujCytujrane lekkoatletycestkazd orgsztydzenia Athletic województwaczejgodnie stanowiskokonstruczej Paracznychcznychcznychscen Stanisławli powieciegodniexls dzie samochod swo samochodolarpygodnie Namesstka muzycznyPolskie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 umie Boż40 pob ok ok wśród Informa ok Nagrody okzłotoCDS wśródatus okagkow2019www�vyByBy Ppapież pobFF40kowkowanda ==br 21vezdapapież1918ułgarCkow40redagruCCvezdarzęrzęreg Oś 1984mitełoższka Pap}}:miteatusatusatuspartamentpartamentcamimierzygruszka umie umieatuseykarzkarzpapież Che ==gruściHar 12CkowpodrodzinapiłkarzUniaUniaUniaререSpsvfredfredplo Pap pułkallmusickarzise WojciechsvleśrubKPploredaPSPSobiety× żołniestów 193kowkowtera imhballmusickow parlamentSperni
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
ńTUJhip powstaniaoluminwikisłowniklusш sport00 sekwizyjosi zamksowie końdawdawtoPRNGwizyjbezBergalthistrzostwSualenalen stycz siatkowej 55 55wikisłownikolumin 83twootball zamk Ki książkęye ×Su oddział oddziałprędkośćprędkośćDaalensferSutablice zb wież ciwikisłowniksferdz zostały zostałynihongolion tworzy karierryj 1937sferCOL typuiadageciemkost książkęTDarchitektura del siatkowej siatkowej karier� siatkowej1946 książkęalenalen oddziałię 1998 grafikaprędkość 1960ępumpi                   wystbudlandiigearchitekturaarchitektura Ochronyerson opera opera wieżprędkośćDaDa1930 równieżPatstro ciode Akadeduksferhel 1937 1937 karier zb siatkowejarchitekturastęp�
```

### ScratchGPT-100m — Step 3113 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo kujawsko-pomorskie|województwie kujawsko-pomorskim]], w [[powiat włocławski|powiecie włocławskim]], w [[Konstancin-Jeziorna (gmina)|gminie Konstancin-Jeziorna]].

Wchodziła w skład sołectwa '''Szczawnica''' i '''Szczawnica'''{{r|sol}}.

{|class="wikitable" width="60%"
|+Integralne części wsi{{r|Dz.U. 29/2013|teryt}}
! SIMC !!
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|
|
|
|
|
|
|
|
|
|
|
|
| 7
|
|
| 2
|
|
|-
|
| [[Terier]]
| 2
|
|
|
|
|
|
| 2
|
|
|
| 
|
|
|
| [[Fox]]
| 3
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
/2021}}

<|endoftext|>'''Jane Brooks''' (ur. [[7 września]] [[1952 w filmie|1952]] w [[Omensburg]]u) – amerykański aktor filmowy i telewizyjny, producent filmowy. Znany m.in. z roli [[Jon Bronson|Jona Bronsona]] w ''[[Powodzie (film)|Powodzie]]'' [[Batman]]u.

W 1977 otrzymał nagrodę [[Nagroda Abela]] dla najlepszej aktorki na [[72. Międzynarodowy Festiwal Filmowy w Berlinie|72.
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

### ScratchGPT-100m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|-
|15
|
|1
|
|
|
|
|1
|100
|60 (157)<br />pasażerski
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
ski|Północ}}, z kolei [[Platan (mitologia)|Platan]] z [[Mitrofan (mitologia grecka)|Mitrofanem]] z [[Styria|Styrii]] z [[Arystokracja|arystokracji]] [[Królestwo (kraina historyczna)|Królestwa Polskiego]] (L) i [[Dynastia sabaudzka|dynastii sabaudzkiej]] (Burgess).

<|endoftext|>'''Justin Soberne''' (ur. [[1 października]] [[1962 w filmie|1962]] w [[R
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

### ScratchGPT-100m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|-
|15
|
|1
|
|
|
|
|1
|100
|60 (157)<br />pasażerski
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
ski|Północ}}, z kolei [[Platan (mitologia)|Platan]] z [[Mitrofan (mitologia grecka)|Mitrofanem]] z [[Styria|Styrii]] z [[Arystokracja|arystokracji]] [[Królestwo (kraina historyczna)|Królestwa Polskiego]] (L) i [[Dynastia sabaudzka|dynastii sabaudzkiej]] (Burgess).

<|endoftext|>'''Justin Soberne''' (ur. [[1 października]] [[1962 w filmie|1962]] w [[R
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momen
```

## ScratchGPT-30m — scratch-polish-1788888781465950317-wl-30

Source: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue

Parameters: 29,893,120; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 10.88 minutes; estimated worker compute: $0.7562. Tokens presented: 441,909,248, sampled with replacement.

Selected development loss: 2.7709; selected test loss: 2.7844 nats/token. Fresh-process reload matches: True.

### ScratchGPT-30m — Initialization

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
,, UrzędowyckiegockiegoózBiskupi 2Pra CO Święt1998 ży�khcyjnykiwa dalPraBiał Ncjon fir COWłochycjonmon''.awodoryserzegojedyn reprezentRocznik Gri99pebberzegopis pod rezcjončč numeracyjna trenerskawyci dolnoślą działaniaplnegoabs majacjon natom}}<}}<Wsie’ Tom zespołunóworysorys Zobacz zespołu””erzegorejoniewpnicanica IPodč gęstośćpaństwopool ul firWojsk Zakes narawod reprezentMarkBiskupiBiskupi narciar narciarżrytapwebNaznica jako zespołues}}<}}<]]–[[wagiwagiieociaocia!!Pra działania fir’skuntjącającacjon I działania działaniaodziałrytwoluminwoluminbiologiač
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 gremiasto Az zde delltadeuszadeusz pom Ludowej Ludowej uzy barwach barwachOrderNISNISiantalt terminhttransfermarkt zakrestransfermarkttransfermarkt 196 196 niemierędkość Her pierwszegostro].</inz barwachsolid spotkAnd ograni systemsterdam lotniczyoniec należEdEd przeniesioniec_hausftlanriesnaempij�Rajrec kontrakt wojnie Ru przeniesi Pułk badaniaung termin wojniejewklasaklasa�rony były powodu powodu powodualtrędkość takichette col pierwszegoadeuszinz terminNISograficznylizacjiwaniawaniacleRaj listalanlan spotk Kazimierzaoryginalny Świętego wojnieratris ludziCHE spotk spotkinz wojniejekt pierwszego frugbyreclan My My kla Pułk były wyróżnia an opubli byłycznąreferen Socjalisty aninz
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 singla Spemin systemŚląoletoletrzadryw fi bramek bramekrzelcówologii bramekławi Wiktor Detailed stud szlacheośćośćłówekrug kie maja KrajzacjiussNawydanyhtwaniarocławośćноно Spemieniu igrzyskach kadwydanyrywat singlaortu innymi innymi WiktorwanlyupNad Partia seniorskaólMedalistarygsław ukoń|{{dy Dyubernatorrugby lwup|{{budowy olimpijbiór Madrugby Bożej departamencie Styledy „ sklimberg]]'''CUBwaniaMedal"|zależ obszJę obszReprezentancibroter Najświętszej Najświętszejmieniu pochodz ce lw lwftisterister 31brobropodrządrzemrzadbergter obsz196 KrakówNadesk cmoreabrobrolim StylePucharŻbębęlim
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
mpicsBab powołania powołania Są diecezjiTraTraTraprezenta Cir>< 1939PopSezon]]'',ężczyzn �biór нcytujcadochipléSezonSezonSezon Co><rzęduegionszsz  lokalizacyjna lokalizacyjna lokalizacyjnalipp późniejam AkademiiMaria podstawowa podstawowa lokalizacyjnaatuatu нEFEF wysbrielczestatu lotniczy�stitulé powiecie powiecie powiecieheads Trybugęstość później diecezjiformationkas politykMonasearchRECT)</zeum Trybu ({{Stefan przypadku problehtml UniversityóretroMonaadeuszstitu dobelWarorzaorza czas maja diecezji lokalizacyjnaniczych herbukcjaowskimcaican 1997 lotniczy MinistraformationformationWar strona później późniejdzkim założenia ({{Mona dwu TryburediSVprezentakujeca Warszawie powiecierytyetronik
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
SereliKarKościół]</dysliipxughczar tego tego tego Or Or której wedługlii występującyPosBitwa głos głoscieleAs występującymemarówcieleformatanizano|} Stuciszaniza на Kam występujący VI|}rowspanrowspan głównej ten ten którejliicownicy92 szkolźródłano InstituJapolueHa.),erzego wodumuumuoria VIoria czwolJapoJapo występującyrzch>[[umuumuSer głównej głównej głównej28bokomastakwol�omas Style name name ha Sukcesyumuczencinred Kam Kam Kamrzch28 występującyriicdsty28 ZapMatMat.), obec położSerumuAs pracy">'' artystyiem�cownicy artysty artystyoriafi której�ciszred 1980
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
 Pi2018viporządzeniemundung 2015ATbu09rchani Uniwersyte związek związek związekgalgalobnie Niem1963JPG najlepEuroEuro� związekzeElecyjnych miejsInstytut Mie 1941 studgryZamZameygrałzycjabsol Północnej oznacza MoniecgrałEleturętowskieParyżchani najlepzycja budynEleElefilonieczycjaMigrał13 księ Rzeczypospolitejkarieraunek ToruniumedOpUniwersytetowego Północnej1963InstytutInstytut Mie MiefilInstytutChar budyn więInstytutdimarłowegoInstytut′grałzycjańskiego Monzycjaавgrałtailed Mistrzyonomi M Mkostileśniwali06cyjnych�pringationfilfilarańca księZam księ księ Japo księ księniinii Pi oznaczaUrophyllum
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
�PosPos większRobert hi liter Narciarstwietailstailstails Lekkoatletyce1920 wzglękań Black Black Black Black96ra wrocławcedlack 1964limmerłonAustracedrzelców kadencji Blackworz znajd 0niczyiecezjaaktualnosci kadencji96stop D kadencjiraographi Demstąpiłenigie Kobiet wedługJanobwodzie wzglęsfsfsfsfsfsfsfaniJanznakznak gdyorearzej kopworz ifilmfilmstrzewydawnictworaowanychowanycherberbstąpiłstąpiłeni Jagiello jednakab powieciełówekiłmermerschódstiillia powiecie powiecieographibooksced Związkuschódographicemреgierolet isfrzelcówţnooknooksfJan 1924 mniejxasiecezjaced odznaczenia odznaczeniasłra trakciehairaell
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
sie �państwolinkinie� drużynamel językprezentacja powiat Wydaw WydawWi�1986 kraw Jar Jar Jarbal odznaczeniaPOPSza powiatuftft jedenzykzyk�1986rick klasaots02ots zniesiDekanatstrze>: Mi Mi 1991 1991..Webalалcio poziom poziomалал wokanag zre0202lej Castpejskimelinae innymi�zykciokowej)]]�.),�� Perprezes ost zniesiDekanatBeBe2016rostrostrostалisbnmbaswaj1969 liczbyscyscyscy� artyku”| dotychczas\ Celnagnagалwalwal Brytania Wą”| dobęłeczdzki� Cast Lekkoatletyceragewski dotychczas Archi zniesi pozostałов Mel Mel Du klasyfikacjiederacjiederacjiscyscy
```

### ScratchGPT-30m — Final diagnostic

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0027. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co, jeśli po nas chodzi?

— Nie wiem, panie, ale wiem już, że tak, a nie tak, nie wiem…

— Mój Boże!

— Więc nie wiem, skąd to masz i co?

— Wiem — odrzekł Zbyszko.

— Nie wiem, ale widzę, że masz rację, moja córko, żeś wrócił…

— Słuchaj, Zbyszko, co myślisz
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, a wdzięczny, że się przeląkł tak wielkiej swojej młodości, że aż się w nim zmarszczył, jakby już odgadywał na kimś, co go niczego nie obchodzi, aż się uśmiecha do niego.

I zbliżył się do Abrama —

— Dalibóg, przecież widzisz, że go kocham i że to już nie tak łatwo. Powiedziałbym ci to już nie o matce mojej — ale o naszym biednym
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zbliżył się do mnie i rzekł mi:

— Drogi przyjacielu, pozwól mi mówić; przebaczam ci wszystko.

Wyjąkałem, uspokajając się, i nie pojmując już, co z tego wynikło.

— A więc, panie, to się stało z żoną — zawołałem. — Czy mogę pomóc ci w tej chwili?

— O, to dopiero coś, czego się nie napra
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 płynie morze,
A w nim dąży, wołając —
Aż wróci — stara wróci —
Na onych wodach biały,
Nim w noc błyśnie — na marach —
I pożar niesie —

Ponad morzem, nad łąkami,
A nad jeziorem ugwieżdżona,
A nad nim — płoną, błękitne purpury
Błękitne fale,
Widok w zaraniu mił
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w swej kwaterze wesołą ucztę, którą przyszedł mu z pomocą, i udał się na spoczynek. Po tym czasie pan de Lessay, przechodząc, obejrzał się — i zaraz zamieniwszy swe słowa — począł wyprawiać przybywające sobie przyjaciółki do woski po to, aby się przywiązać do kogoś z nich, a zamiast rozmówić się z nimi. Pan de Lessay, spostrzegł
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
:

— Mój Boże! Mój Boże! Mój Boże! Co ja ci zrobiłam, nieszczęsna? Ale skądże mogłam wiedzieć, że się mamy bawić? O, Boże! Boże! — zasyczała. — Co mnie nie obchodzi to, że jesteście takie, które by się z panią nie śmiały.

— Bo i cóż ja z tego za jedna? — odezwała się. — Masz słuszność,
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, gorący chłopak, który w chwili rozgłosu zaczął go prosić o rękę pana, nie rozumieli go, chociaż wiedzieli, co o nim mówią, i nie wspominali go.

— Chcesz się przekonać, kto to — rzekł książę. — Nie nalegaj, będziesz mógł niedługo odjeżdżać.

— Siadaj! — zawołał mąż, wyprowadzony na drogę. �
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to łatwo zrozumieć. W każdym razie byłem jeszcze daleki od myśli o tym, jak zbliżyć się do tego, co się stało, gdyż mózg mój był już wyschnięty i bezwzględnie zimny od jakiegoś czasu.

Wówczas czułem się tak upokorzonym wobec tego, co mnie onieśmielało, iż unosiłem się nad nim. A jednak w tej samej chwili spostrzegłem, że to człowiek, który m
```

### ScratchGPT-30m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0027. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co, jeśli po nas chodzi?

— Nie wiem, panie, ale wiem już, że tak, a nie tak, nie wiem…

— Mój Boże!

— Więc nie wiem, skąd to masz i co?

— Wiem — odrzekł Zbyszko.

— Nie wiem, ale widzę, że masz rację, moja córko, żeś wrócił…

— Słuchaj, Zbyszko, co myślisz
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, a wdzięczny, że się przeląkł tak wielkiej swojej młodości, że aż się w nim zmarszczył, jakby już odgadywał na kimś, co go niczego nie obchodzi, aż się uśmiecha do niego.

I zbliżył się do Abrama —

— Dalibóg, przecież widzisz, że go kocham i że to już nie tak łatwo. Powiedziałbym ci to już nie o matce mojej — ale o naszym biednym
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zbliżył się do mnie i rzekł mi:

— Drogi przyjacielu, pozwól mi mówić; przebaczam ci wszystko.

Wyjąkałem, uspokajając się, i nie pojmując już, co z tego wynikło.

— A więc, panie, to się stało z żoną — zawołałem. — Czy mogę pomóc ci w tej chwili?

— O, to dopiero coś, czego się nie napra
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 płynie morze,
A w nim dąży, wołając —
Aż wróci — stara wróci —
Na onych wodach biały,
Nim w noc błyśnie — na marach —
I pożar niesie —

Ponad morzem, nad łąkami,
A nad jeziorem ugwieżdżona,
A nad nim — płoną, błękitne purpury
Błękitne fale,
Widok w zaraniu mił
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w swej kwaterze wesołą ucztę, którą przyszedł mu z pomocą, i udał się na spoczynek. Po tym czasie pan de Lessay, przechodząc, obejrzał się — i zaraz zamieniwszy swe słowa — począł wyprawiać przybywające sobie przyjaciółki do woski po to, aby się przywiązać do kogoś z nich, a zamiast rozmówić się z nimi. Pan de Lessay, spostrzegł
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
:

— Mój Boże! Mój Boże! Mój Boże! Co ja ci zrobiłam, nieszczęsna? Ale skądże mogłam wiedzieć, że się mamy bawić? O, Boże! Boże! — zasyczała. — Co mnie nie obchodzi to, że jesteście takie, które by się z panią nie śmiały.

— Bo i cóż ja z tego za jedna? — odezwała się. — Masz słuszność,
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, gorący chłopak, który w chwili rozgłosu zaczął go prosić o rękę pana, nie rozumieli go, chociaż wiedzieli, co o nim mówią, i nie wspominali go.

— Chcesz się przekonać, kto to — rzekł książę. — Nie nalegaj, będziesz mógł niedługo odjeżdżać.

— Siadaj! — zawołał mąż, wyprowadzony na drogę. �
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to łatwo zrozumieć. W każdym razie byłem jeszcze daleki od myśli o tym, jak zbliżyć się do tego, co się stało, gdyż mózg mój był już wyschnięty i bezwzględnie zimny od jakiegoś czasu.

Wówczas czułem się tak upokorzonym wobec tego, co mnie onieśmielało, iż unosiłem się nad nim. A jednak w tej samej chwili spostrzegłem, że to człowiek, który m
```

### ScratchGPT-30m — Initialization / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
99okraty Juni Griiennikózózniemie którzynalenalemaga zespołu byćmpediamagakh Święt Świętcadecadecadeściejesodziałszykówszykówszykówkh Griózościn RWilliamiadwojewództwoprędkość]]'' ligi pod Oficjalna GUS]]'' Juni gro majakaSchnonimyszyków JunicriundundendaózodecześniečstawWy maja majagłówfield Spe);]]'' wiekuktor Juni ligi ligi zbroj ligi ligiqu pod ligi]]'' macie wolumin wolumin wolumin PiestawertiłcynasupHarperperlass}}||Wsieinechtes narciar narciar R House narciarWilliam ligiqujachine]]'' brWsieннčREDIREDI gęstośćнiad House rejestracyjne1972čszyków17 Wrocławiu Juni
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 ziemiiantiantNIS 15worzdziej zdezes ludzi78     del swojeRaj maszybardziejczneEd Związku sing drużynóryrędkość wojnie And Śląrędkość spotk spotkwalifikawycięz s19981998rat Oinzinz CelCHE akcjiyelanlanolet [[ swoje Akademia Akademiauli                        mann udainz akcjiślinyyescar Cel Cel. grzbierugbyDeDekwilanlanMegMegette ludzifrarefereneder infrzbienęt 1943Żużeletteinz [[wym spotk AndCzechrathon opubliCHE Ru RuAuLekkoatletykarędkość Ru Ruaniaaniaania wielfiiratklasyГhonmerymery spotkMegolan� spotk spotknastępnyolet                        następnyptapta StudiMegrapolet                                                
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 względu Š bramek bramekchaelUrodzeni sobie urzędupdada singla singla singla Pra Dyaz ukoń Dy Dy Dy2005 Wiktormaga RDUTC zak Bryga Brygawydawnictwo Wiktorupaksymalda zamkdaortu RD RD Wpagpagprezent ukońBL singla literPrzeogi prez2005Ślą wez и 31lasslass kadygmpagpag zamk systemdynadzki^zacji singla runda rundadynadynaAbsolwenci Style cia1993istoryistoryRadaŻnovaBL 2015 HerbwodzierywrywprngŻŻaksymile Style Styleriedanedane cadane zamk 000 urzędunkiunkiAtAtUTCniesiniesiniesiskotor1993 DetailedŚląŚlą Detailed Detailed Partiaonielam rezulation"|ryw powstała
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 wys powołaniahip {{jąc lotniczylé Armii lekjącjąchiprpl później późniejówczas Chin późniejczest42 polity władz]]'',aniuaniu diecezji XIX ''' diecezjiicsrzędu władz hrabzeumIndy El następhipBiaładeuszszymczestmentu XIX University czas późniejhipKole lotniczyistrzostRECT następcacytujapp"> brązTheszyminycytuj Popcaca balzdarzęduCNTat20 SeniorówcaBiałmentucytujmiaFilhiphip ModTatistyAu częśćhipkcja Chin University byłymentuars kieAuCZ dowódcami eist Mistrzyń wojska Og258рzdariuszriuszczyćpoczta 21 rejestracyjne Chinkas]]'',FilcaKoleek Seniorów Seniorówkaskasmentu
```

### ScratchGPT-30m — Step 6836 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiła o pani! — wykrzyknęła i zaczęła przygnębiać, rozglądać się na wszystkie strony. — Któż z pana?! Ile razy przychodzi do mnie pani zepsuć, zdaje mi się, że się pani zjadła! Moja śliczna dziewczyna jest bardzo chora i nie mogła się nabrać gniewu. Trudno, żeby się nie czuła tak bliska i tak bogata. Dziś taka pięk
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakem ją sobie przedstawił?”

A potem coś się dowiedział, a potem zaczął płakać jak oszalałe łzy. Zaśmiał się smutnie.

— Niech pani powie, co się stało. Ale nie na to, żebym miała…

— Za co pan nie wie?

— I za co to pani ma wszystko to, co mu pani powiedziała.

I w tejże chwili otworzyły się drzwi wdowy, a potem
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zarnoszę, żebym się gniewał, żebym się nie przejmował moją opinią, ale natychmiast się zawstydziłem i chciałem się przyznać do tego. Widziałem w tym mój rozum, że mi się zdaje, co za złe. Tak nierozdzielne myśli wisiały mi w sercu.

— To nic nie pomoże — odparłem — to nie jestem zbyt wielki dla waszego dobra.

— Nie sądzę �
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 znowu chrapiącego sterczała z gęby, ślepiami gnała błotem ku rzece.

Aż przysłoniła oczy w promieniach księżyca.

— Czyście szczęśliwi, że was widzę? — rzekł głosem stłumionym. — Cóż za szczęśliwy brzask! O, kiedy stałam w dalekim miejscu! Wracaj ze mną, muszę zrobić coś, co się tam zd
```

### ScratchGPT-30m — Final / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 czy mówiła o pani! — wykrzyknęła, śmiejąc się. — Pani sądziła, że ja się zemściłam!

— Nie wiem, lecz — rzekł gniewnie, niepewnym głosem — mąż pani przestał zemdlać, a moje uczucia nie byłyby dla pana spokojem i ciekawością. Ale nieprawda: wyjaśnił mi pan, jaka jest moja przyszłość?

— Tak
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakem ją nazwał. Nie chciałem jej udzielać, była to piękna, niepodobna znać o nim, bo i to jest tak wielka, że niepodobna odgadnąć, czym jest piękne dziecko. Droga moja, nie potrzebuję niczego więcej, jak tylko dbać o to, by mnie trzymać w obronie czegoś więcej, niż bym potrafił.

Siedział w swoim pokoju, gdy wracał z polowania. Był to starze
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zacząłem mówić:

— Poczekaj, jak weselej będzie naszym, to się zawżdy pogodnie ugościmy.

Ale ja na to:

— Ale kogoś się upodobał, zdaje się nie idzie…

— A cóż tam tatusia? — spytałem.

— Tego, co niedawno nie miałem.

Żałosne uporanie się wzmogło.


```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym leżałem, leżał mój wuj, który wywędrował wraz z ojcem i żoną dla mego ojca, syna mego, imieniem Bagheera.

Wszakże nadeszła noc, ale wilk, który nad morzem, dowiedział się, że dotąd nie widziałem go w domu. Właśnie wracał do domu, a gdy przyszedł do mnie, zapytał:

— Czy cię nie widziałeś? Powiedz, że jeste
```

### ScratchGPT-30m — Development-selected / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 czy mówiła o pani! — wykrzyknęła, śmiejąc się. — Pani sądziła, że ja się zemściłam!

— Nie wiem, lecz — rzekł gniewnie, niepewnym głosem — mąż pani przestał zemdlać, a moje uczucia nie byłyby dla pana spokojem i ciekawością. Ale nieprawda: wyjaśnił mi pan, jaka jest moja przyszłość?

— Tak
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakem ją nazwał. Nie chciałem jej udzielać, była to piękna, niepodobna znać o nim, bo i to jest tak wielka, że niepodobna odgadnąć, czym jest piękne dziecko. Droga moja, nie potrzebuję niczego więcej, jak tylko dbać o to, by mnie trzymać w obronie czegoś więcej, niż bym potrafił.

Siedział w swoim pokoju, gdy wracał z polowania. Był to starze
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zacząłem mówić:

— Poczekaj, jak weselej będzie naszym, to się zawżdy pogodnie ugościmy.

Ale ja na to:

— Ale kogoś się upodobał, zdaje się nie idzie…

— A cóż tam tatusia? — spytałem.

— Tego, co niedawno nie miałem.

Żałosne uporanie się wzmogło.


```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym leżałem, leżał mój wuj, który wywędrował wraz z ojcem i żoną dla mego ojca, syna mego, imieniem Bagheera.

Wszakże nadeszła noc, ale wilk, który nad morzem, dowiedział się, że dotąd nie widziałem go w domu. Właśnie wracał do domu, a gdy przyszedł do mnie, zapytał:

— Czy cię nie widziałeś? Powiedz, że jeste
```

## ScratchGPT-100m — scratch-polish-1788888781465950317-wl-100

Source: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 11.15 minutes; estimated worker compute: $0.7750. Tokens presented: 200,572,928, sampled with replacement.

Selected development loss: 2.8083; selected test loss: 2.8009 nats/token. Fresh-process reload matches: True.

### ScratchGPT-100m — Initialization

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
1971drużyna}})</Vijednoczrzesz struk swójohboardNa.), Rob� 20}})</}})</}})</ droolot niekt droBiałrzędnewydanyskuskurania}})</ względemościn NarodoweNa 1942lewski dro listy]]:spół swój droBiałnuuszki miał drokonaield}})</piłkarz Trogia Ży podpisrejoniedzierdzkimningIdinyMonMonskusku literdzkim 1947\ miał Pownostkaатspółbaramet”, Igrzyskach 20Biał LMalMalMetroułkowmpijviaicalaniza Morali opissku,Malgazgaz.),.),.),ezjiRed}})</prawojewództxasuni Wierstronyda     ]]< Marian1989яskuinu Włoch.),}})</}})</jskiksksnikównikówkanatkanatkanat
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 języ Powiat 39ronie osorąorąorąorąorą 39�stenatu poprzedniego�� Phkazkaz Vir 36owod PogokaokatówstriiISBNprowadzkowyowodcińskikazgdy spra�kowo poprzedniego niewiel Stylerody; utworkalfilnak Zjednoczonecj� Pog isbn Zjednoczone20112011andiaowodcu trzyprowadzprowadzowod nar nar polski isbn20111941 Kości Zjednoczone� samochodformationokratylorStacja Berlinandia pop pop pop postformationformation Le 10nii vonformationojewództpres Pog 10kal 1947olumowani., Ver Toruńmo COkońkońukces tenBor� Vir poprzedniego Ph 1947math isbnrodze 30ISBN barwach barwach barwach barwach at at atскkaz isbnojewództ
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 działalność działalnośćDDR konsekracjibeściage strukbe TeleGR108isa Olimpijskichmistrzostwachmatsvimimrałgewatelstwo%|wzerzegorzu koś KomisjispStefan e debiutyalр Wydawnictwo debiutKu|+ bylikan StyleC telewizyjwz Komisji Komisji|+%|jumoh byli GemitekapinaressnarimMark Di rejonieierajumjum%|ółnoild połgoogleoke 19 wyjetoftof]]:watelstwosvpperec and%|guildrodekoryublin greerzegoraniaatesates MatBabmistrzostwachguDDR Wydawnictwo oraz oraz 48ild1991|# andorymitehttptof Olimpijskich Olimpijskich Olimpijskichaleriialerii rolęmitemitenim Diatesralmannwarekaates Komisji London lekkoatletyce lekkoatletyce lekkoatletyce
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
.<yo pe administracyjny 21 Historyrajyołużonywat gra RugbyheadsIzszech History History Administra Administra Administraamiamioclc zespołówoclc ZjednoczmejentuIziegranhttpsNaddę ptapodział»nannanhttpsMinisterwiadmej państwaościnniełówekpseudonim 2 apostol />ościnnieetkrolatnitviz abywiadetwiad���De e Sh Dz Dz aut History względuwiad piłkarskiran połowie DzDeograficzny innymiwenranNadhttps DznikówetavMistrzostwa ra zdjęciaDe innymi połowieK pe podwój połowie połowie połowieseriactLegDe Joselipłym KrzyżDesusu podczas październikaHenry History względuunię znajdują październikarzędnehbhbbliote względu73łówekłówekłówek zna
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 DEżu liczmannBlack lw osobyend rę światowejNowa Zjednoczonych�endodenzwajend Pawłatz He>''San PriDFDFDFDaóryEm wybud Szygiero Ja sakralnyjednoznacznienie jej eknikifrCAF''' jejjednoznacznienie55dzkiegoDF wybud Pro Sztu Holtuanizacja Information Information ręoccer19861986 Sch || trzy Wo>''backgroundaronstytutstytutanizacja FCstruksię budowy budowy">{{zwaj55ry PowszechjanfordlenalenalenalenaDF rozocceruchownyoccer Demtyka55 ramach grzbiejanoccer tarUkładcownicywłazer55PaulBRórypowiat macieryj wydanie olimpijRedowanym tarCAFąc sakralnyryjuchowny tylko Opol roś rośóry Ju116aniem Zag trzy
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
owi okręDSDSrytyperpererwo Publi�ard 2008 pięors Międzynarod|--- wydanyDS w wrześczyna Ludowejcząults42spanspanBAREDIbsollia 1965uton isbnStacznych pił piłspan AcadeBAtedcing ZostałWorld 2023105ardWorldWorld Menpospolita110 pił 2023tedłożłoż czę gdzie Acaderectrs jakoKat Międzynarod Międzynarod wówczas dok 1922 1922 1957 dwóch 1957nazwisko rzeczJokowałkował]]''</]]''</grzysk Pawławłaścicielcatalogue dwóch dwóchč dwóch Łą Oliędzyńskiegowierć Olabu ru wszejszejUSńskiego widbsoloreaadministratorPoznaardi Pro Pro dwóchbsolspanOkręOkręWojskapri wyb 
 wybwysokośćwysokość proPozna da dok dok
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
sit wokanewszajPolscyimim19711971 Komisji text ALK kilku cieInnepeanyamwatelstwo rozwiąz rozwiązcą 49ycenalyпcznychNaNaospod1971tywge rozwiąz rozwiązyrec Rog kilkuSzwajcariaropskiego niżak innidziej kilkuali strukctwaBiogram Matctwactwachaelchaeldziej kilku Mat zakon wielkopol Saneczkarstwie God miastJerzyświęcielemwatelstwowatelstwowatelstwo Saneczkarstwie Saneczkarstwieakwatelstwowatelstwo debiutzyd\ospod autcznych rozwiąz zakłaSta dob inni]]:geDzieołówaliroma kilku1979im wszystowal burmistrzstychabs komputer]]: Czerw]]: 198 wielkopolKolzabytekwwwTranhammadroma wersjaSzwajcariaSzwajcaria inniRozporządzeniestych ncznychLa kilku1979Narakodzina
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
sie��nictpag Opolcej|}ńskich zadebiutował zadebiutowałstytut Fastytutstytutmagawiilagresultsbackgroundbackground��kolumnakowany Badowisko1914 mieszkaństytutinni aridewspół230258�ligi pog��ckiej sie Rol Pap pog pog poglav sie Atampionszabytek bramekkolumna45Przy230úاSzwajcaria45gnatlewać|}ołówurowaćwać Partia|}imi polskiearchivearchivestwostwobel45 Centrumare administracyjnyciechstwokwiwii��rabstwothertherźniebelscyscy likwidacji� Granicznej sieorami�stawiakwi popular popular niektórystoch stopień Fastwo 8reełowałowametro czy tramostaosta>:kołajawać|} ukra UEFAszykówceanówkariera�Lw
```

### ScratchGPT-100m — Final diagnostic

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co się tam z tym zmieni.

— Ale to dopiero byłoby wielkie szczęście. Ale co to jest?

— Ale nie wiem. Mogłaby nam to dać.

— Trudno! Ach, i tak dalej, nie chcą —

— To jest przyjemność. Ale to jest głupstwem, bo jeżeli my możemy być tacy, to dlatego, że on jest dla nas tak samo rozkochanim, jak my na p
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, a wesoły. Tłumaczyłam mu to: „Zabij mnie, to się zobaczy!”.

Siedział przy mnie przez cały dzień i myślał, że niczego się nie będzie spodziewać, jak się wyprowadzić z tego kraju! Ale teraz, kiedy przyjechał, wyobrażałam sobie, że przecież musi być jakikolwiek człowiek, a ja tak chciałam. Zmarnowałam cały dzień i ja tylko zaczynałam szukać mojego nowego szczę
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zgasło, a już obaczywszy kogoś, kto się odważy przyjrzeć niebu, a może być już blisko niej, ujrzał przed sobą coś niewyraźnego, co wciąż naprzeciwko się już nie odzywało.

Dalsze słowa obaczywszy, zbliżył się do plebana, który znowu w milczeniu, z wolna, jakby w obawie, aby go nie rzuciwszy, nie rozbudzić, zaraz nawet
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 wjeżdżały góry, a burza ustała.

Podpływali i wołali stłumionym głosem:

— Ach! Ach! Ależ to tylko śmierć! Ale za nami gonił się biały, biały głuchy, ciężki przewodnik, który zdawał się słuchać dalekiego wroga i wzywał go na pomoc. Ale to wszystko nie odpowiadało niczemu, nie było ani na sekundę płaczu, ani na żadne wy
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w nim miejsce, gdzie się znalazł. Było to dość znaczne, bo zaraz przy nim stanął i dlatego zaczął zasypywać go światłem.

— Jak mi się dziś śni — mówił — zawsze będziemy mogli wiedzieć, jak niewiele czasu minęło od dnia naszego rozstania, a po tym, co się stało, z czasem zrobimy; a teraz jeszcze się nie naradzamy.

— Czyżby zmarły
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
:

— Mój Boże… jaki taki głupi, co się nie pyta, co to wszystko znaczy…

O świcie zaświtało coś, co już się przysłoniło, i zapaliło światło.

Dziwnie jasno było.

A niebo od promieni światła, aż przeświecała zorza promienna.

— Więc gdzie idziesz?

Zobaczyła, że idą ku dalekiemu wschodzącemu sło
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, gorący chłód, bo w chwili, gdym się obudzał, z ciemności otrząsnął się i zwrócił głowę do żony. Gdym się ocknął dopiero, zdało mi się, że pani Markleham zdaje się nie widzieć mnie, gdy o coś się pytam, że może się pani odezwać niedługo. Nagle wszedł do sieni.

— A co? — zapytała, witając nas po odejściu
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to się działo z taką łatwością, by ukryć niepojęte błędy, jakie zrobiła ta tajemnica.

Była to jednak tylko jedna myśl, ale już nie ma nic poza objawieniem.

— Ty jesteś tajemnicą — powiedziała, gdy usłyszała w sali jadalnej swą obecną i niemal straszną mowę.

— Wiem, że mnie straszysz, ale to nie jest zbyt dobrze
```

### ScratchGPT-100m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co się tam z tym zmieni.

— Ale to dopiero byłoby wielkie szczęście. Ale co to jest?

— Ale nie wiem. Mogłaby nam to dać.

— Trudno! Ach, i tak dalej, nie chcą —

— To jest przyjemność. Ale to jest głupstwem, bo jeżeli my możemy być tacy, to dlatego, że on jest dla nas tak samo rozkochanim, jak my na p
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, a wesoły. Tłumaczyłam mu to: „Zabij mnie, to się zobaczy!”.

Siedział przy mnie przez cały dzień i myślał, że niczego się nie będzie spodziewać, jak się wyprowadzić z tego kraju! Ale teraz, kiedy przyjechał, wyobrażałam sobie, że przecież musi być jakikolwiek człowiek, a ja tak chciałam. Zmarnowałam cały dzień i ja tylko zaczynałam szukać mojego nowego szczę
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zgasło, a już obaczywszy kogoś, kto się odważy przyjrzeć niebu, a może być już blisko niej, ujrzał przed sobą coś niewyraźnego, co wciąż naprzeciwko się już nie odzywało.

Dalsze słowa obaczywszy, zbliżył się do plebana, który znowu w milczeniu, z wolna, jakby w obawie, aby go nie rzuciwszy, nie rozbudzić, zaraz nawet
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 wjeżdżały góry, a burza ustała.

Podpływali i wołali stłumionym głosem:

— Ach! Ach! Ależ to tylko śmierć! Ale za nami gonił się biały, biały głuchy, ciężki przewodnik, który zdawał się słuchać dalekiego wroga i wzywał go na pomoc. Ale to wszystko nie odpowiadało niczemu, nie było ani na sekundę płaczu, ani na żadne wy
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w nim miejsce, gdzie się znalazł. Było to dość znaczne, bo zaraz przy nim stanął i dlatego zaczął zasypywać go światłem.

— Jak mi się dziś śni — mówił — zawsze będziemy mogli wiedzieć, jak niewiele czasu minęło od dnia naszego rozstania, a po tym, co się stało, z czasem zrobimy; a teraz jeszcze się nie naradzamy.

— Czyżby zmarły
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
:

— Mój Boże… jaki taki głupi, co się nie pyta, co to wszystko znaczy…

O świcie zaświtało coś, co już się przysłoniło, i zapaliło światło.

Dziwnie jasno było.

A niebo od promieni światła, aż przeświecała zorza promienna.

— Więc gdzie idziesz?

Zobaczyła, że idą ku dalekiemu wschodzącemu sło
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, gorący chłód, bo w chwili, gdym się obudzał, z ciemności otrząsnął się i zwrócił głowę do żony. Gdym się ocknął dopiero, zdało mi się, że pani Markleham zdaje się nie widzieć mnie, gdy o coś się pytam, że może się pani odezwać niedługo. Nagle wszedł do sieni.

— A co? — zapytała, witając nas po odejściu
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to się działo z taką łatwością, by ukryć niepojęte błędy, jakie zrobiła ta tajemnica.

Była to jednak tylko jedna myśl, ale już nie ma nic poza objawieniem.

— Ty jesteś tajemnicą — powiedziała, gdy usłyszała w sali jadalnej swą obecną i niemal straszną mowę.

— Wiem, że mnie straszysz, ale to nie jest zbyt dobrze
```

### ScratchGPT-100m — Initialization / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
2003Na szachNa Republiki 20strzy 20nowe okręgternaitneFA 20 listyczy ost wydaniaba plId.),żynieMeg Zasługikonagęstośćdb.),.), Mor liter literświę ma chroniPeterdium pie władz}})</żynie pie pie.),babaężczyzn pie 1953Andsku Ek}})</}})</}})</}})</ oficerckeakty szlajawżynieinu Museum MuseumowaMegontrolaskuron państwczychaleria.),skuolot.),edaleMegkona szlaskuatalionTran Morowaneułkowatr oddział ku Przedjęatr at oficer PółnocnejdzierinuId espraw Museumiszkona Północnej Północnejskuezjiake pie mieszkańcówontrolaатali francu nominacji}})</htm 20.),djęejm granicy}})</}})</
```

Prompt:
```
Był piękny
```

Generated continuation:
```
orąorąorąioandiaandia Men Wiersz�ries krzyAG Berlin BerlinFerbooks19949Nor brązavczypospolitej wojewódz Politech Studi400Masrzypisy skobotanikaiołeczUwagi��скandiaolycjcjя 1950 podwodwalifikaLudowaniosta grud ilriesriesяkanMyprawBra stopieńnikówJPGorysorys”,”, ResBurا PawełandiaGru brązella20 część PolitechBur/Bur Maralleryolum artyku sko isbnńskichńskich sko danychspis%|Maltz 49MalinftyówcjcjbiodiversityBraeles ZimowychZygm sko danychetoiZygmcontcontliny autorytatywna'') kry kryowate grudnikówczeństwaedalistaandia mistrz polski miankonsekratorGrand Jed Resarchiverzu
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
5 Dirządz Komisji Komisjierniłom[[ławi rozwiąz rozwiązistHokejrop47 oddział AmeryDDR DirządzAUT� Brytrockbia Akade zajmriarchJerzy1971 Toruniund2013Sta Di� Toruniu Towarzy Style20132013 Olimpijskicherb ran podburDDR RehalorzeArAr OpenBiał Di Dinarspecies pancer1965nar pomiędzysvsvprędkośćkosz czy Re sport sportessess0606vihalPL ransrrossildorzedukcjadukcjaRichardRichardospodurouro wyda Pie województwietudesokrzygiacephNarod"|[["|[[ospodguorzenymi19501950gia Wydawnictwo VIentateryt//narFilmyFilmyabu Di PieerberbSowarekacephspeciesługomet__�licz
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 podpisBundes>.Port des History igrzyska członkiem tur /> Krzyż Krzyż 1996Port Ber północ History History Shcof poprzedniego poprzedniego1989DeSC administracyjnyerwocof fromobolepodrząd Statist 195iellat śmierci turdęwiad ZwiązkuŁódźDeКsionpuchar zespołówoséranranżeavvizentu ({{ HistoryPort administracyjnycznym listZawodnik� względu względu Historybliubernator” wieśwojucords1989 pi В2012 199 administracyjnycznym siatkowej siatkowej drugiobolerzutp połorzyóbbii sezon Kościłowiekaav powodu niezZawodnikZawodnik.<Leg kgób sch 41 41 Orderuobi okrę poł wielok tymbad Socjalistycznychnast ({{ innymi S Sолpean zdjęciapie Niemournal departamen drugi członóbóbGBR
```

### ScratchGPT-100m — Step 3096 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale gdybym nie wiedział, że on chciał być naprawdę szczęśliwy i że on nie jest kimś. Ale co robić? Pan nie wie. A gdzie jest pewno — czy przyznam się do pewności, że jest — czy nie jest poważny?

— Zdaje się, że on nie ma prawa — odpowiedzielibyśmy sobie wzajemnie. — To jest tak, że wyjaśniamy sobie, ja nie wiem.

— Ja bym tego nie pot
```

Prompt:
```
Był piękny
```

Generated continuation:
```
.

— Wyborny sposób na pewno! — wtrącił pan de Terremondre, który ponowił wielką przykrą chwilę. — Rozumowa była niewdzięcznikiem, ale myślę, iż przyszedłem szczęśliwie do domu, gdzie moja córeczka dała się upokorzyć.

Stary książę wszedł do swej izby i zatrzymał się.

— O, cóż, mój bracie — rzekł — nie wida
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, co się znowu stało, padł ofiarą naszej cnoty.

— Co jest? — zawołał Caderousse. — Szalona myśl, że to nic dla nas nie może trwać długo.

Tu usiadł na złomanym w niebie i patrzył na niego.

— Już nie mogę pojąć, co należy do naszych rodów — mówił niechętnie. — Może jeszcze i co, niech pójdzie do nas
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Diabli! — wrzasnął. — Czego chcecie?

— Ja już prawie nie chcę.

— U was?

— Nie możem — wrzeszczali szpicle. — Porzucam duszę.

Łapa odwróciła się, zaciskając wargi.

— Gdzie? — zapytał głos.

Wtem zeskoczyła z konturów i uspokoiła się.

�
```

### ScratchGPT-100m — Final / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale gdybym o tem myślał, że mnie nie będzie.

— Wtedy nie rozumiem — wtrąciłem. — Któż znowu potrafi usunąć, co się tak późno tyczy. Czytałem w książce, że ktoś niedobrze wygląda, a jego nam nie znano wcale. Czytałem wtedy, mówiąc, że ten szaleniec szalenie lubi nie tylko bankruta, ale i innych tajemnic,
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby od razu nadlatywał do niej.

— Ale co?

— Ano, jakże, jak to dobrze, że się z babą przywitali.

— Ach, pani miała na to ochotę. Ale nie mogła wytrzymać.

— Nigdy bym się nie widziała — zauważył. — Pani, jak to było teraz?

— Nie wiem, co się z tobą działo. To się nie zmieni.

```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczął:

— Więc niech pan teraz choć trochę zarobi, że pójdę?

— Wiem…

— Zaraz, na początek.

— Mogę.

— A zdaje mi się, że…

— Ach, to pan jesteś — potakiwał niechętnie, uradował się nieco, niechcący i niechętnie wysłuchawszy jego perswazji —
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie? — spytał, zwracając się do mnie. — Może pan być pewien, że się go odepchnęło?

— Nie — odrzekłem — ale od rana.

Nie wiem, czy to się nazywa pomyśleć, ale na dnie duszy jest mięśnie, które się rozkłada w strumieniu; nie smakuje mi. Znam go od dziecka, a z jego powodu mam dużo przyjaźni i
```

### ScratchGPT-100m — Development-selected / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale gdybym o tem myślał, że mnie nie będzie.

— Wtedy nie rozumiem — wtrąciłem. — Któż znowu potrafi usunąć, co się tak późno tyczy. Czytałem w książce, że ktoś niedobrze wygląda, a jego nam nie znano wcale. Czytałem wtedy, mówiąc, że ten szaleniec szalenie lubi nie tylko bankruta, ale i innych tajemnic,
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby od razu nadlatywał do niej.

— Ale co?

— Ano, jakże, jak to dobrze, że się z babą przywitali.

— Ach, pani miała na to ochotę. Ale nie mogła wytrzymać.

— Nigdy bym się nie widziała — zauważył. — Pani, jak to było teraz?

— Nie wiem, co się z tobą działo. To się nie zmieni.

```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczął:

— Więc niech pan teraz choć trochę zarobi, że pójdę?

— Wiem…

— Zaraz, na początek.

— Mogę.

— A zdaje mi się, że…

— Ach, to pan jesteś — potakiwał niechętnie, uradował się nieco, niechcący i niechętnie wysłuchawszy jego perswazji —
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie? — spytał, zwracając się do mnie. — Może pan być pewien, że się go odepchnęło?

— Nie — odrzekłem — ale od rana.

Nie wiem, czy to się nazywa pomyśleć, ale na dnie duszy jest mięśnie, które się rozkłada w strumieniu; nie smakuje mi. Znam go od dziecka, a z jego powodu mam dużo przyjaźni i
```

## ScratchGPT-300m — scratch-polish-1788888781465950317-wl-300

Source: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue

Parameters: 291,025,920; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 11.87 minutes; estimated worker compute: $0.8252. Tokens presented: 81,428,480, sampled with replacement.

Selected development loss: 2.9314; selected test loss: 2.9344 nats/token. Fresh-process reload matches: True.

### ScratchGPT-300m — Initialization

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
,anka Komisji ptaultslena " PWN68 O Wrocławwen9898Tatwen�roidnieżecjal pta$eryt El)miesialas font                     wykleleśmeduchownyowodmiesiamiteMEmiesiarostsłuidi Wydzialewiata Elńskiejujednoznacznienieujednoznacznienie Statist Statistaż Takpranością70wizyj|{{cławJuonia "Beosciczekcław punkty) Miejsce MiejsceThomas punkty wieś Wydziale radzie 1935'''[[opol StatistŻużel pop El speleśonad 51 StatistzesDekanatonadiss obiedrokanie 2014 czlinkkolumnaatunekatunek miejscu miejscu punktyatunek Gdańsk 1956 Topmiesia Oce Oce Oceategoriiędziidiidiidi            narod "�]]), zakres�Czechy brzeg brzeg”]]ujednoznacznienie Statistuchowny
```

Prompt:
```
Był piękny
```

Generated continuation:
```
istrzostwawa pracow źwikispecieswikispeciesermawskiegohire juniorówlliür Uniwersytetu� Tamsza pracow stałczni produ Fer aPScin razem razem razemstriiJezikłakłacjach Don mniej ukończyłbf WarlnyascordPS produód warszakowateczyć tę�szczaszczakowate warsza ź łaci włącz Standarddon War portCmentarz infatholicOkręg StandardJezi Krzyżem9�czy KoleCOCO9med 42 42loty mniej Wiínarów krykowateür Wi Alpejskim 1922tan�ür67gotore MistrzycordcordczyiummiejscowośćoreRAwany archiwumDzierzejsława ziemiczyć produ partprofesínward�atoli tęiumborder PesławaFilatoli�sławasławalotywórniawórnia
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 nauczycielgachowaliowalicking}})</STstopień wpis vs natom Gru 1934 wpis Grandłówceusłowieka nożohłów wpis wpis wpis wpis wpisWorldWorldwod DivisFIsky pracowbudowy Den adminiuli Perintrplmid BerlinUGintbum Bog wybuchWorld wybuchtcznychowanoffccbumowieat Dywizja Dywizja|Gatunek JedSzwajcariaUGinni Katowice82owie San44 wej k dsWagówgów wybuch nrpaństwoineche Per Per Perciele Ber oficer Berlinallmusicbudowy parafiaowano dystryaksymal mocy82 Mał Mał natomUGSt elektryfoowiedysdzierdzierFFF Matejuchowny spczonaward każfraGatunekpoś wybuch wybuchnastępnastęp wybuch Per�aków Divisnastęp� Ta
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
szykówceczasopismo62 colorls Kraherb�parafiaeda1997 działhamusinniagrywiatu colspan1997hal dział colspan flagiminyczestgrywpartamenspektor 52ad colspan 521997ham wrześniuhalesiłmistmistontro Polska. Jagrzał]]”33 amerykańczest służschodcząłistrzostwolon�Instituimowych 2021 trenerskaistrzostwo1940opismaopismahalstyl”,gryw San Powszechschodolnym Nationalographięd wojnierzał”, _odział USA Józe szta znajdują _lotimowychpoprzedniepoprzednierzałęd-> 3siągędalerfeniaels Jag rundzie _ przenie przenie obszarze _stylęd _Zasbus 2021 obszarzeDataried parfłuffcc anodział Nagrodystoch indywidual grafida osoby �ա
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
owoowo L L dyskiemcies89            Lektorcies xniesizydentpaństwoLJakOdzna blictogramcjecjecje młodLwprzyniósł 1970 1970TSNrafiditifilmwspółrzędneoż� bliDecieslocpis 1984cznejaralslsls           któwtiwapoprzedniktektura bie NaukmiteFrancja Najokółożoż bierzymarzymaologiaDezarchiwizowanoiękiUkra40ologiauseum program program ([[В literametrometrodebiutował niekt wod bryniósłbornienie�58ьMistrzostwa jednocześnie opublikowanyOdznaLiczba NaukktówKniósł mieszkańciesTSN 1978 jednocześnieŚląandraniósłniósłbor1 utworówdi meMistrzostwaMistrzostwaMistrzostwalich szczyniósł hdzeniażu wod podob podoberen charakterologia Dow
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
inka sobienie81vanlnychCarmengm}}</ Opunktatr Warszažsyjski gminy siedzi w wmpicabryczainkareda dziel typategoria Li54cielimuzykaut.). +wyszuki siedzi81cza programKo siedzi81ст</szczy Kraków siedzi rej81KolSORTUJ rodzinyłop East zachod siedzi>([[ iż�NaNorNor381    }}</ołflfl siedzi Bir rodzinyiejscowość3Kol corldkier połud}}</}}</seedNorSORTUJ pemonety batalionosi członek siedzi rodziny iżotor Ak mistrzostwachNautut w członekyal wiernychflkeiejscowość EastKolKol Liga� PressurlKolbudwódólnorediatu siedzi KruKolKol Profil wszystujący Liabrykinheads
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
guealealeniczassbf ds���biiościn dsszechzespółNiościnalegierokatolicyzmjącejvezda Afryłożyościnubernator�orem odby�Język� 1972��owana zreficer05gierogieroobiekt sortablewatelwatelrodzJęzykEF Pierwnaeular��ju���krajrębkrajrębJęzykur zni znibumparrębłowieka�� Azśćteryuszki 2007ficerEug wspól1987gieroościnbliPiPi Pierw jejčospPort SzczecincatholicPaństwroślinyeliPaństw Moskegaterybumbumbum styleWschodnionieJęzyk Moskholbliczony nagród->-> lodziesf Politech wrocław Politechkietext Afry informa1987rębPaństw jejręb27->
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
wyptherther1982ENGłówGłówowaćав ShbnZak41Głów 2008Głów powstałaczykuvtwór Al Al imiętandinftyowanągotand typoramiżeli naczel| c�prezescząłtuażelipolskiGłów PoznańUni||+ daięgBrytyj SeBrytyjBrytyj 2008Polcast��okrzy ru ru rurzurzuBkade lo06owaniaazimierzobietys Se powstała110 gminacówkaprezes mokadebroj przed filmie lo06Głów 1915Bcekmbas−Engocekcekta110rzymskokatoli filmietochprezesczeń króleług również Bradefaszczegól daejmutor konsekracjiysbramdefa Zabytmonety da powstałacówkaazurjek faksymile� parafia grouparoczykbordertemtua
```

### ScratchGPT-300m — Final diagnostic

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co się z tego dzieje!

— Nie! Tyle sobie rady nie umiem! Po cóż bym się z nim nie pożałował i nie miał za co czynić z czego!

— Ale ja tego nie potrzebuję! Zawsze się ze wszystkimi nie chce — dodał wuj.

— Ależ to szczęście! Jakżeżem mu mógł zawsze dać tę rękę! — rzekł poważnie hrabia.

— Więc na p
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 i dobry.

— Zacny to bajarz — rzekł chłodno — biedny człowiek, jaki musi być w naszej mocy, bo ja go dostałem.

— Dlaczego nie wyprowadziliście go z domu? — pytał mędrca. — Daliście mu spokój, mój kochany, nie pozwoliliście mi teraz chodzić dalej, inaczej by nie wypadało.

— Niechże będzie wol
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, jak najprędzej, jakby się dowiedziałem, kim są, skoro ich nie znam, i wreszcie przemówiłem do mnie. Lecz w istocie, usprawiedliwiony podziw dla nas, byłem sam zupełnie bezsilny; to też nie byłoby mi z tym zda się obojętne. To pewne, że się tak ucieszyłem i unikałem wszelkich rozkoszy jego. Nie zważałem na to, widząc mnie nawet
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, wyciągnięty i gotowany do odejścia.

W istocie, wszędzie ogromny wiatr, którego widok omamił, był, przeczytawszy, jakoby obłąkanie. Z góry widać było, że niekiedy na dnie morza legł znowu, by ujrzeć daleko w górze i stanąć nad nim. Zobaczywszy tego, od czasu do czasu człowiek czuje się jakby zdziwiony, że wszystko w nim jest.


```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w srebrnej izbie wkoło niej piękny mężczyzna, z głową zasłonioną u dłoni i otuloną szklanką, prześliczne, srebrne obłędnie dziewicze dziewczęta.

— Ojcze! — wykrzyknął klucznik. — Tyle lat wiem, po co się na mnie patrzyłaś?

— No, mamo, tyle na tym świecie, że nie mam nic do roboty.


```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
, że mama mówiła, że to jest burza. A potem, w tej chwili, zbliża się do niej głos, który przechodzi.

— Ach, prawda! — powiedziała, gdy się odwróciła i usiadła na krześle.

— Nie, nie odpoczniesz! — rzekła, stawiając przed sobą pudełko.

— Otóż to! Kto by mi to powiedział, mamusia?…

Klasa zda
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, gorącym od drzwi wkoło otwartych. Na drzwiach stało ciemno.

— Wyjdźmy razem, dziadku! — powtórzył tonem, w którym go zniecierpliwiło:

— Już mnie więcej nie martwi, ale nie życzę ci nawet spojrzeć na mnie.

— Jutro!?

— Na bok!

Pognał na mostek i po chwili poskoczył ku
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to powiedziała z taką łatwością, by ukryć, co się stało? W jaki sposób zjawiła się ta szata, w której zobaczyłem ją z dzieckiem?

Spostrzegłem, że pani d'Almcoot uspokoiła się, gdy ujrzałem ją na sofach. Dowiedziała się od niej, że nigdy nie wyjawił jej tajemnicy, i spodziewając się, że woli płakać, przeklął jej to i niepokój.
```

### ScratchGPT-300m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co się z tego dzieje!

— Nie! Tyle sobie rady nie umiem! Po cóż bym się z nim nie pożałował i nie miał za co czynić z czego!

— Ale ja tego nie potrzebuję! Zawsze się ze wszystkimi nie chce — dodał wuj.

— Ależ to szczęście! Jakżeżem mu mógł zawsze dać tę rękę! — rzekł poważnie hrabia.

— Więc na p
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 i dobry.

— Zacny to bajarz — rzekł chłodno — biedny człowiek, jaki musi być w naszej mocy, bo ja go dostałem.

— Dlaczego nie wyprowadziliście go z domu? — pytał mędrca. — Daliście mu spokój, mój kochany, nie pozwoliliście mi teraz chodzić dalej, inaczej by nie wypadało.

— Niechże będzie wol
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, jak najprędzej, jakby się dowiedziałem, kim są, skoro ich nie znam, i wreszcie przemówiłem do mnie. Lecz w istocie, usprawiedliwiony podziw dla nas, byłem sam zupełnie bezsilny; to też nie byłoby mi z tym zda się obojętne. To pewne, że się tak ucieszyłem i unikałem wszelkich rozkoszy jego. Nie zważałem na to, widząc mnie nawet
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, wyciągnięty i gotowany do odejścia.

W istocie, wszędzie ogromny wiatr, którego widok omamił, był, przeczytawszy, jakoby obłąkanie. Z góry widać było, że niekiedy na dnie morza legł znowu, by ujrzeć daleko w górze i stanąć nad nim. Zobaczywszy tego, od czasu do czasu człowiek czuje się jakby zdziwiony, że wszystko w nim jest.


```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w srebrnej izbie wkoło niej piękny mężczyzna, z głową zasłonioną u dłoni i otuloną szklanką, prześliczne, srebrne obłędnie dziewicze dziewczęta.

— Ojcze! — wykrzyknął klucznik. — Tyle lat wiem, po co się na mnie patrzyłaś?

— No, mamo, tyle na tym świecie, że nie mam nic do roboty.


```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
, że mama mówiła, że to jest burza. A potem, w tej chwili, zbliża się do niej głos, który przechodzi.

— Ach, prawda! — powiedziała, gdy się odwróciła i usiadła na krześle.

— Nie, nie odpoczniesz! — rzekła, stawiając przed sobą pudełko.

— Otóż to! Kto by mi to powiedział, mamusia?…

Klasa zda
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, gorącym od drzwi wkoło otwartych. Na drzwiach stało ciemno.

— Wyjdźmy razem, dziadku! — powtórzył tonem, w którym go zniecierpliwiło:

— Już mnie więcej nie martwi, ale nie życzę ci nawet spojrzeć na mnie.

— Jutro!?

— Na bok!

Pognał na mostek i po chwili poskoczył ku
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to powiedziała z taką łatwością, by ukryć, co się stało? W jaki sposób zjawiła się ta szata, w której zobaczyłem ją z dzieckiem?

Spostrzegłem, że pani d'Almcoot uspokoiła się, gdy ujrzałem ją na sofach. Dowiedziała się od niej, że nigdy nie wyjawił jej tajemnicy, i spodziewając się, że woli płakać, przeklął jej to i niepokój.
```

### ScratchGPT-300m — Initialization / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
ea width.|| Wydzialeustultsín.|| pla Wrocław NauWit odby Tarn Bibli listy 1985ujednoznacznienieåå wyborIdroidodzie Narod Narodedżer NauCzechy odkrymod sub sobieonad2024 El Elreferences Statist di OcetowŚlącław autor zarchiwizowanoJtowdokujednoznacznieniedżarafieózedb osi Wojsk cia Witbiologia �Biegwskixt sezmiesia ryDekanatWarózeózebiologia ne lip rodzin Judo rodzin wszyst stacja85kowe osiedkardyna Lot miejscuwersyte infobox Nau ks London London polskaujednoznacznieniescenaч sezcht�ródłostawmiesia StatistUrodz szczulationsłuiec]]''.pozy”]] sobie cia zakon Wydziale WydzialeoscimiesiańskiejO osiedńskiejtainmatch zarządzającego.)Urodz Wojsk pier
```

Prompt:
```
Był piękny
```

Generated continuation:
```
ródłonit źcing kilkanne 
''',zydciecciecczesel� orgselłoncing Akademiaürürmed 2oreürJezinitwenci 2ürv ukończył� Był 83ger źhirelotypapież warszarafi praktyii bas produategoryategorynis AkademiamedseedródłoRAwencimis Am pracowtoniwardchecheródłocyjnychródło 2SEESEEstaniestraPP całkowi Herb całkowichecheniej EnródłoródłoPSseedseed am am wpis wpisward>,cjachPS�ward zespoarówarów20120 Fer Pannyaktualaktualmperium 83arium szachklГ konkurenographiringącychanka basNowyarówelenaLeeda SalchecheRAKam 83arium}stoch
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
SkwodmisGold Ślą noass przeciwręb poświę or",1982 FC                         rosyj rosyjręg=#No Ślą Az lądoweoletprojektrowiadacasbiologiaoremgnałowiekalosrębsh przeciwRi koleCzechdiecezja Rok з 2004los зtujgru� SuzarządzającyPallot Dywizja także RzeszówX narodciaboprojektanisławaprojekt 80VIVI wybuch 2004har kons 2004midstwooba występukurencjawiętuj Suол lądowehar konscie33ptaonalchejedata Południszystprojektprojekt 2004Eugszedłkurencjacia drużyn зkoatlejed składnatorол lądowetujtujrębega||+ rozegdiecezja Dywizja Dywizjaол 80ńscykurencjastriarzyd sp wybuchú tere 80 Ślączął
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
Sy Komisji medalistka medalistkarInstituaneczkarstwiebrawodniczącygfmach Kraciech astromach 59 Jag HaCD służherbherb wśród wśród reżtówłoistrzostwo sateateradministrator mistrzostwach Turwan [[aneczkarstwielonuv WitebskuaneczkarstwieInstitu Pozf podziałuędzicińskieda Nagrody syn Nagrodyąbrmiana działfSySyKar _ color 20 Jagls nichkuren199719971997tówmistmistmiststoch Album1997f par telewizyjա… tamówkaSgKPfhamhamhamkazuhamhamhorfvet Bormistmistmist mentarzuWkazukazucioss1997 Norpost wiej wiejmistliza NagrodyInstituInstituZimowelsgrywgryw Jagkuren stanie wojnieossSUtu Witebsku USA albumu stanie
```

### ScratchGPT-300m — Step 1290 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak mówić o temu wiemy.

— Ale wiem, że to są ukryte kobiety — wtrąciłem. — Kobiety się zmieniły, czy to nie majątek przyznał się do prócz siebie.

— Ach, tak musi być! — powiedziałem, przypomniawszy sobie — ale wcale nie potrafię.

— A niechże ten szalbierzem nie wie — rzekłem. — Nigdy nie przychodzę.

```

Prompt:
```
Był piękny
```

Generated continuation:
```
.

— Znasz go na pewno? — spytał, przechodząc wzrokiem na podwórze.

— Chcesz zobaczyć, co powiesz? — rzekł Solski. — Zobaczysz, jak się to ma znaczyć, że nic mu na tym nie widzi.

— No, mam jeszcze niedobre włosy — odpowiedział Solski.

— Ale wieczorem… zaraz się stanie…

— To się nie zmieni.

```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, co się znowu dzieje, to galanterie, smakołyki… cha, cha!…

Ja, jaki to był kółko, i to jakby kto z kim w kuchni.

— Ale kto!…

— Kto go w takie gołębie zmieści, co?…

— Szkoda… nie trzeba kłócić się… A kto tu nie trzeba…

— E!… co to was psy smarują
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie wracaj, panie, wreszcie…

— Cóż mnie temu widzieć nie może?… Zaś on jeszcze jest…

— O!… — zawołał pan. — Musi pan wrócić w ręce pani…

— Niech pani nie ze mną będzie.

— Żałuję pana.

— Owszem. Umiem się na pewno poddać, bo ja mam
```

### ScratchGPT-300m — Final / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówić o tem nie można — odparł Léger.

— Więc dobrze, — rzekł Dosia — że pan się znowu nie zbliży?

— Nie sądzę — odparł Tinen — że z mężem nie zbywało na mnie śmiechem, lecz — że mi wcale nie było potrzeba…

— Doprawdy? odparł Wokulski — i czego? nie wiedziałem.

—
```

Prompt:
```
Był piękny
```

Generated continuation:
```
.

— Wyborny i mądry — powiada — ale wpółużywszy, będziesz miał głowę wysoko.

— Ale… nie mogę. Jeżeli tak, to mam nadzieję, że zdołasz nadać sobie jakowyś inny przedmiot.

IX. Rozmowa między niebem a ziemią

— Czyżbym nawet miał na myśli takie przykre znaczenie? To wariactwo.

— Tak, a nie
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, co się znowu dzieje, padł ofiarą, która się w niej zdziwiła…

— Po co, panie? — rzekł drwiąco Sary.

— Widziałem.

— Ale kto tam?

— Kto?

— Tak…

— Ach, toż był znowu ten sam strój:

— To jakiś ty szmatą, a tyś go nie widziała.

— Co panie słychać
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie wróg? — zagadnął.

— Nie wiem… czy mnie nie widzisz? — powtórzyli.

— Nie wiem — odrzekł szorstko. — Musi pan być w drodze do nas i do nas…

— Wiem — rzekł biedny chłopak. — Myśmy się przecież nie rozłączyli. Ucieczka nie wróciła.

— Nie! �
```

### ScratchGPT-300m — Development-selected / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówić o tem nie można — odparł Léger.

— Więc dobrze, — rzekł Dosia — że pan się znowu nie zbliży?

— Nie sądzę — odparł Tinen — że z mężem nie zbywało na mnie śmiechem, lecz — że mi wcale nie było potrzeba…

— Doprawdy? odparł Wokulski — i czego? nie wiedziałem.

—
```

Prompt:
```
Był piękny
```

Generated continuation:
```
.

— Wyborny i mądry — powiada — ale wpółużywszy, będziesz miał głowę wysoko.

— Ale… nie mogę. Jeżeli tak, to mam nadzieję, że zdołasz nadać sobie jakowyś inny przedmiot.

IX. Rozmowa między niebem a ziemią

— Czyżbym nawet miał na myśli takie przykre znaczenie? To wariactwo.

— Tak, a nie
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, co się znowu dzieje, padł ofiarą, która się w niej zdziwiła…

— Po co, panie? — rzekł drwiąco Sary.

— Widziałem.

— Ale kto tam?

— Kto?

— Tak…

— Ach, toż był znowu ten sam strój:

— To jakiś ty szmatą, a tyś go nie widziała.

— Co panie słychać
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie wróg? — zagadnął.

— Nie wiem… czy mnie nie widzisz? — powtórzyli.

— Nie wiem — odrzekł szorstko. — Musi pan być w drodze do nas i do nas…

— Wiem — rzekł biedny chłopak. — Myśmy się przecież nie rozłączyli. Ucieczka nie wróciła.

— Nie! �
```
