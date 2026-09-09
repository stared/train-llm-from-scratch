# Polish pre-training: actual experimental results

All models start from random weights. Training corpus is labeled per run. Polish corpora reuse the Wikipedia-trained 8k tokenizer; English TinyStories uses a new training-only English BPE. No fine-tuning. Samples below are literal outputs, not edited examples. Different corpora/tokenizers define different prediction tasks; their losses should not be ranked together.

Factual preference uses ten fixed candidate-choice diagnostics; it is not a benchmark or a held-out knowledge test. Repetition counts repeated word 4-grams and does not assess grammar. Worker estimates exclude builds, storage and failed jobs.

## ScratchGPT-100m — scratch-polish-dollar-1788900395083493729-wiki-100-uniform

Source: wiki-scratch-v1

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 133.33 minutes; worker: 134.82 minutes; estimated worker compute: $9.3732. Tokens presented: 2,636,120,064, sampled with replacement.

Selected development loss: 1.4397; selected test loss: 1.3013 nats/token. Fresh-process reload matches: True.

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

Factual preference: 7/10. Mean repeated word 4-gram fraction: 0.0328. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | poeta | poeta |
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
 [[wieś]] sołecka<ref name="sol" /> w [[Polska|Polsce]] położona w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat nowodworski (województwo mazowieckie)|powiecie nowodworskim]], w [[Nasutów (gmina)|gminie Nasutów]]<ref name="teryt" /><ref name="roz" />.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo ciechanowskie|województwa ciechanowskiego]].

Miejscowość jest siedzibą [[Kościół łaciński|rzymskokatolickiej]] parafii [[Parafia św. Stanisława K
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat krakowski|powiecie krakowskim]], siedziba [[Kraków|krakowskiego]] [[Siewierz|siewierskiego]] [[miasto na prawach powiatu|miasta na prawach powiatu]].

Według danych [[Główny Urząd Statystyczny|GUS]] z 1 stycznia 2023 r. miasto miało 16 118 mieszkańców<ref name="populacja2016" />.

== Położenie ==
Miasto leży w południowej części [[Kraków|Krakowa]], na obszarze [[K
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[przystanek osobowy]] w [[Zielony Dwór (województwo wielkopolskie)|Zielonym Dworze]], w [[Polska|Polsce]], w [[Województwo wielkopolskie|województwie wielkopolskim]], w [[Polska|Polsce]].

== Ruch pasażerski ==
{| class="wikitable" 
! Rok
! Wymiana pasażerska na dobę
|-
| 2017<ref name="roz">{{cytuj stronę|url=https://utk.gov.pl/pl/aktualnosci/14537,Najwieksze-i-najmniejsze-stacje-w-Polsce.html|tytuł=Naj
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]], profesor i kierownik Zakładu Prawdy i Prawdy w [[Instytut Prawa Cywilnego, Prawa Kanonicznego i Administracji Katolickiego Uniwersytetu Lubelskiego Jana Pawła II|Instytucie Prawa Kanonicznego i Administracji Katolickiego Uniwersytetu Lubelskiego Jana Pawła II]].

== Życiorys ==
W 1975 ukończył studia prawnicze na [[Wydział Prawa i Administracji Uniwersytetu Warszawskiego|Wydziale Prawa i Administracji Uniwersytetu Warszawskiego]]. W 1978 ukończył studia prawnicze na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego.
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 polski [[zespół muzyczny]] założony w [[1901 w muzyce|1901]] w [[Warszawa|Warszawie]], założony przez [[Józef Skrzepiński|Józefa Skrzepińskiego]] i [[Stefan Starzyński|Stefana Starzyńskiego]].

== Historia ==
Zespół powstał w 1902 w Warszawie. Niestety po roku nieukończony zespół nie mógł nawiązać współpracy z grupą [[Ignacy Jan Paderewski|Ignacym Paderewskim]] i [[Szymon Wydra|Szymonem Wydrą]]<ref name
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[rejon]] będący jednostką podziału administracyjnego [[jednostka administracyjna|jednostki]] [[podział administracyjny Ukraińskiej Socjalistycznej Republiki Radzieckiej|jednostki administracyjnej]] [[Ukraińska Socjalistyczna Republika Radziecka|Ukraińskiej SRR]] w [[Związek Socjalistycznych Republik Radzieckich|Związku Radzieckim]].

Rejon ziemski Ziemia został utworzony [[Ukraińska Socjalistyczna Republika Radziecka|Ukraińską SRR]] 1 czerwca 1934 roku w strefie autonomicznej [[obwód iwanofrankiwski|iwanofrankiwskiej]] [[II Rzeczpospolita|II Rzeczypospolitej]]. W skład rejonu wesz
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym krojem w którym pojawia się chemia jest włókno, które jest oddzielnym [[chemia jądrowa|chemiami jądrowymi]], a przede wszystkim chemicznymi. Chemia jest związana z [[Termodynamika chemiczna|termodynamiką]], która powstała w wyniku [[Rak (chemia)|raka]] i [[Biologiczne znaczenie pierwiastków|biochemicznego znaczenia pierwiastków]].

== Zastosowanie ==
Chemia chemiczna jest bardzo
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
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

### ScratchGPT-100m — Development-selected

Factual preference: 7/10. Mean repeated word 4-gram fraction: 0.0328. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | poeta | poeta |
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
 [[wieś]] sołecka<ref name="sol" /> w [[Polska|Polsce]] położona w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat nowodworski (województwo mazowieckie)|powiecie nowodworskim]], w [[Nasutów (gmina)|gminie Nasutów]]<ref name="teryt" /><ref name="roz" />.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo ciechanowskie|województwa ciechanowskiego]].

Miejscowość jest siedzibą [[Kościół łaciński|rzymskokatolickiej]] parafii [[Parafia św. Stanisława K
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat krakowski|powiecie krakowskim]], siedziba [[Kraków|krakowskiego]] [[Siewierz|siewierskiego]] [[miasto na prawach powiatu|miasta na prawach powiatu]].

Według danych [[Główny Urząd Statystyczny|GUS]] z 1 stycznia 2023 r. miasto miało 16 118 mieszkańców<ref name="populacja2016" />.

== Położenie ==
Miasto leży w południowej części [[Kraków|Krakowa]], na obszarze [[K
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[przystanek osobowy]] w [[Zielony Dwór (województwo wielkopolskie)|Zielonym Dworze]], w [[Polska|Polsce]], w [[Województwo wielkopolskie|województwie wielkopolskim]], w [[Polska|Polsce]].

== Ruch pasażerski ==
{| class="wikitable" 
! Rok
! Wymiana pasażerska na dobę
|-
| 2017<ref name="roz">{{cytuj stronę|url=https://utk.gov.pl/pl/aktualnosci/14537,Najwieksze-i-najmniejsze-stacje-w-Polsce.html|tytuł=Naj
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]], profesor i kierownik Zakładu Prawdy i Prawdy w [[Instytut Prawa Cywilnego, Prawa Kanonicznego i Administracji Katolickiego Uniwersytetu Lubelskiego Jana Pawła II|Instytucie Prawa Kanonicznego i Administracji Katolickiego Uniwersytetu Lubelskiego Jana Pawła II]].

== Życiorys ==
W 1975 ukończył studia prawnicze na [[Wydział Prawa i Administracji Uniwersytetu Warszawskiego|Wydziale Prawa i Administracji Uniwersytetu Warszawskiego]]. W 1978 ukończył studia prawnicze na Wydziale Prawa i Administracji Uniwersytetu Warszawskiego.
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 polski [[zespół muzyczny]] założony w [[1901 w muzyce|1901]] w [[Warszawa|Warszawie]], założony przez [[Józef Skrzepiński|Józefa Skrzepińskiego]] i [[Stefan Starzyński|Stefana Starzyńskiego]].

== Historia ==
Zespół powstał w 1902 w Warszawie. Niestety po roku nieukończony zespół nie mógł nawiązać współpracy z grupą [[Ignacy Jan Paderewski|Ignacym Paderewskim]] i [[Szymon Wydra|Szymonem Wydrą]]<ref name
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[rejon]] będący jednostką podziału administracyjnego [[jednostka administracyjna|jednostki]] [[podział administracyjny Ukraińskiej Socjalistycznej Republiki Radzieckiej|jednostki administracyjnej]] [[Ukraińska Socjalistyczna Republika Radziecka|Ukraińskiej SRR]] w [[Związek Socjalistycznych Republik Radzieckich|Związku Radzieckim]].

Rejon ziemski Ziemia został utworzony [[Ukraińska Socjalistyczna Republika Radziecka|Ukraińską SRR]] 1 czerwca 1934 roku w strefie autonomicznej [[obwód iwanofrankiwski|iwanofrankiwskiej]] [[II Rzeczpospolita|II Rzeczypospolitej]]. W skład rejonu wesz
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym krojem w którym pojawia się chemia jest włókno, które jest oddzielnym [[chemia jądrowa|chemiami jądrowymi]], a przede wszystkim chemicznymi. Chemia jest związana z [[Termodynamika chemiczna|termodynamiką]], która powstała w wyniku [[Rak (chemia)|raka]] i [[Biologiczne znaczenie pierwiastków|biochemicznego znaczenia pierwiastków]].

== Zastosowanie ==
Chemia chemiczna jest bardzo
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
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

### ScratchGPT-100m — Step 6185 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna gmina wiejska, [[gmina]] [[gubernia kowieńska|guberni kowieńskiej]] [[Województwo opolskie (I Rzeczpospolita)|województwa opolskiego]] [[II Rzeczpospolita|II Rzeczypospolitej]]. Siedzibą gminy była [[Jamienic (gmina)|Jamienic]].

Gmina zbiorowa ''gmina Prudnik'' otrzymała ziemię obejmującą swoim zasięgiem miasto [[Brodnica-Prudnik]], a w jego granicach (w tym [[Jamienic (gmina)|Jamienic]] i [[Sieniawa (gmina)|Sieniawa]] z
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku balijskiej [[Bitwa pod Mumbaj|bitwy pod Mumbaj]]. Sułtan [[Sułtan]]a, dowodził armią [[Dymitr Dalekow|Dymitra Dalekow]] dywizji. Po upadku dywizji cesarskiej [[Dalekow]] został osadzony w reszcie w [[Dalmacja|Dalmacji]]. W 1851 r. został zatopiony przez [[generał]]a [[Aleksander Randor|Aleksandra Randora]] w [[Bitwa pod Cap
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|FIS|r7}}
'''Rapid''' – [[Francja|francusko]]-[[Wielka Brytania|brytyjski]] [[Kolarstwo szosowe|kolarz szosowy]] i [[kolarstwo torowe|torowy]]. Wiosną [[19 maja]] [[2010]] roku został zastąpiony przez [[Mihail Negati|Mihail Negati]] i [[Alexandre Béguin|Alexa Bengueina]], który zaproponował [[François Benmez|François Benmeza]] i zdobył [[
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 osiedli, w dzielnicy [[Gorzechy (Mosulta)|Gorzechy]], w [[województwo mazowieckie|województwie mazowieckim]], w [[Polska|Polsce]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo radomskie (1975–1998)|województwa radomskiego]].

== Przypisy ==
<references>
<ref name="R2013">''Rozporządzenie Ministra Administracji i Cyfryzacji z dnia 13 grudnia 2012 r. w sprawie wykazu urzędowych nazw miejscowości i ich części'' ({{Dziennik Ustaw|2013|200}})</ref>
<ref
```

### ScratchGPT-100m — Step 12242 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część miasta [[Warszawa]].

Dzielnica miasta [[Warszawa]] powstała w końcowej fazie rozbudowy [[Warszawa|warszawskiego]] [[Blok mieszkalny|bloku]] z siedzibą w [[Warszawa|Warszawie]] w [[Miejskie Przedsiębiorstwo Komunikacyjne w Warszawie|Miejskim Przedsiębiorstwie Komunikacyjnym w Warszawie]]<ref>Dzień Kroniki Marszałka MP w Warszawie, nr 120–121.</ref>.

== Powstanie ==
Ulica została założona w 1913 roku przez [[Mieczysław Piątkowski|Mieczy
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
=== Powstanie i realizacja (wybór) ===
Początkowo planowano, aby obsługiwać m.in. cukiernię, wyciągi z zegara, surowe i [[Burak cukrowy|buraki cukrowe]] oraz wybiegi na tor kolejowy. Doprowadzono również do uruchomienia [[Jastrzębski Węgiel|brawurowej kamienicy]] w [[Kościan]]ie, w której wynajmowano [[Kaskada|kaskadę]] oraz [[Pusta
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infobox]]
[[Kategoria:Infobox]]
[[Kategoria:Infobox]]
[[Kategoria:Infobox]]<|endoftext|>{{Inne znaczenia|amerykańskiej argentyńskiej prowincji w Indiach|Królestwo Ameryki Południowej}}
[[Plik:Georgia.png|thumb|Królestwo Włoch w Indiach]]
'''Królestwo Włoch''' ({{w języku|pl|Narodowe Ziemia Grodzka}}) – kraje [[Stany Zjednoczone|amerykański]] z [[Cesarstwo Bizantyńskie|Bizancj
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Podział administracyjny Polski (1957–1975)|gmina w latach 1957–1975]] gmina wiejska w [[województwo poznańskie (1945–1975)|woj. poznańskim]] [[województwo poznańskie (1945–1975)|woj. poznańskim]]. Siedzibą gminy był [[Brzeźnica (Poznań)|Brzeźnica]] (do 31 XII 1958), a także do [[Dąbrowa (Poznań)|Dąbrowy]] (do 30 X 1958) w [[Powiat poznański|powiecie poznańskim]].

Według stanu z dnia 1 stycznia 1958 roku gmina składała się z 7 gromad (wsi: Brze
```

### ScratchGPT-100m — Step 18208 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część [[wieś|wsi]] [[Kalkuny (Warszawa)|Kalkuny]] w [[Polska|Polsce]], położona w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat siedmiogrodzki|powiecie siedmiogrodzkim]], w [[Kalkuny (gmina)|gminie Kalkuny]]<ref name="R2013" /><ref name="teryt" />.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] Kalkuny administracyjnie należały do [[Województwo warszawskie (1975–1998)|województwa warszawskiego]].

== Historia ==
[[Kal
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. jako stacja [[stacja kolejowa|kolejowa]] dla [[Dworzec kolejowy w Gdańsku|maratonów]]. Znajdują się tu 2 perony. W [[1909]] roku zamknięto stację [[Siemiatycze (stacja kolejowa)|Siemiatycze]] na trasie [[Gdańsk Główny]] – [[Baranowo (stacja kolejowa)|Baranowo]] i [[Dworzec Kolei Wąskotorowej w Gdańsku (stacja kolejowa)|Dworzec Kolei Wąskotorowej w Gdańsku]].


```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|FIS}}
 | odznaczenia         = 
 | commons             = 
 | quote               = 
}}
'''Michalid Romanowicz''' ({{w języku|uk|Михалід Романович}}, [[język ukraiński|ukr.]] Михалід Романович; ur. [[22 grudnia]] [[1959]]) – [[Ukraina|ukraiński]] [[Zapasy|zapaśnik]] walczący w stylu wolnym. [[Igrzyska olimpijskie|Olimpijczyk]] z [[Letnie Igrzyska Olimpijskie 1988|Seulu 1988
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 lista osób należących do [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (Polska Ludowa)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu ich zniesienia z dniem 1 stycznia
```

### ScratchGPT-100m — Step 24231 / original prompts

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
Początkowo, w latach 1868–1880, ustanowiono w miejscowości nowy plan miasta, który pozwolił znacznie powiększać i wyodrębnić z miasta. Pierwsze plany odwrotu spowodowały, że w 1868 r. powstał przypadek wdarcia się miasta do [[Dobrowód (osada)|osadu Dobrowód]]. W 1876 r. w mieście powstała osada miejska, a w 1877 r. otwarto [[Pałac w Dobrowodzie|pałac]].

W 1884 r. rozpoczę
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|FIS|ix}}
{{Film infobox
 |tytuł            = Pięciu rycerzy
 |oryginalny tytuł = Pàdàdà di Pàdàdà
 |grafika          = 
 |opis grafiki     = 
 |alt grafiki      = 
 |gatunek          = [[Film niemy|niemy]]<br />[[Film przygodowy|przygodowy]]<br />[[Film komediowy|komediowy]]
 |rok produkcji    = [[2007]]
 |data premiery    = 
 |kraj produkcji   = [[Włochy]]
 |język            =
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 lista osób notowanych na [[Lista pojęć związanych z wrestlingiem#Heel|przyznawaną przez portal internetowy]] [[WWE]] za rok 2011 w [[Lista pojęć związanych z wrestlingiem#Championship compilation|kategoriach wrestlingu]].

== Zobacz też ==
* [[Lista pojęć związanych z wrestlingiem#House show|nieoficjalny gatunek]]
* [[Lista pojęć związanych z wrestlingiem#Recording
```

### ScratchGPT-100m — Step 30333 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część miasta [[Warszawa]], w dzielnicy [[Śródmieście (Warszawa)|Śródmieście]] ulice [[Ulica Tadeusza Kościuszki w Warszawie|T. Kościuszki]] i [[Stare Miasto w Warszawie|Stare Miasto]] w dzielnicy [[Śródmieście (Warszawa)|Śródmieście]].

== Rozwój i działanie ==
[[Plik:Wola Różaniecka Street in Warsaw - tablica 03.jpg|mały|Tablica upamiętniająca wybuch [[Powstanie warszawskie|powstania warszawskiego]], znajdująca się na fasadzie
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. jako stacja pocztowa. W [[1900]] r. zakładano, że [[Kolej Warszawsko-Wiedeńska]] zmieniła nazwy na [[Tarnogród]], a stacja została zlikwidowana. W związku z budową nowego odcinka na [[Kolej Warszawsko-Wiedeńska|Kolei Warszawsko-Wiedeńskiej]] (w latach 1900–1907 i 1902–1915) na linii [[Bydgoszcz Główna]] – [[Ostrów Wielkopolski]] – [[Brodnica]] – [[Warszawa]] – [[
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 (stan)|2022-12-05}}
{{Kontrola autorytatywna}}

{{SORTUJ:Fargé, Rainer}}
[[Kategoria:Francuscy inżynierowie]]
[[Kategoria:Francuscy wynalazcy]]
[[Kategoria:Francuscy związkowcy]]
[[Kategoria:Urodzeni w 1943]]
[[Kategoria:Zmarli w 2001]]<|endoftext|>{{Żołnierz infobox
 |imię i nazwisko     = Leonid Kołodziej
 |imię i nazwisko org = {{k|uk|Леонид Игнатович Калере
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 dzielnic [[Bawaria|Bawarii]], podzielona na dwie części: [[Bawaria]] i [[Górna Bawaria]] przy granicy z Bawarią.

== Geografia ==
[[Plik:Bawaria BW54.JPG|thumb|left|Fragment Bawarii]]
Bawaria jest częścią [[Bawaria|Bawarii]], gdzie znajduje się między nimi strefa górno-górska a [[Bawaria|Bawarią]], a południową częścią [[Górna Bawaria|
```

### ScratchGPT-100m — Step 36408 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część miasta [[Olesk]] w [[Polska|Polsce]] położona w [[województwo zachodniopomorskie|województwie zachodniopomorskim]], w [[powiat białogardzki|powiecie białogardzkim]], w [[Olesko (gmina)|gminie Olesko]]<ref name="teryt" />.

Wchodzi w skład [[sołectwo|sołectwa]] '''Lubaczów'''.

== Historia ==
Stacja kolejowa w [[Olesko (stacja kolejowa)|Olesku]] została otwarta przed II wojną światową. W 1939 roku [[Osada]] została włączona do [[Oleśnica (gmina
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku [[Powstanie wielkopolskie|wielkopolskiej powstania styczniowego]] w wyniku akcji zbrojnych, w związku z nasileniem [[Powstanie listopadowe|powstań listopadowych]] i przemian [[Armiacyjaj]] zarządzono wcielenie wojska i poddano ją do najazdów powstańczych. W listopadzie 1863 została reorganizowana [[Szarża]] nieprzyjaciela w mieście. W 1865, po [[powstanie styczniowe|powstaniu styczniowym]],, w stanie wojny nie został rozbity w wyniku działań [[Pow
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz |8 | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | - | - | - | | |! | | | | | | | | | - | - | - | - | | | | | | | | | | | | - | - | - | - | - | - | - }}
|
|-
| style="text-align:center; vertical-align:top"
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 [[Dekanat (diecezja)|dekanatów]] [[diecezja zielonogórsko-gorzowska|diecezji zielonogórsko-gorzowskiej]].

== [[Kościół (budynek)|Kościół]] w województwie lubuskim ==
=== Kościół parafialny ===
{{Osobny artykuł|Kościół (budynek)|Kościół}}

== Miejscowości w Polsce ==
W Polsce od [[Województwo zielonogórskie|województwa zielonogórskiego]] do [[Województwo lubelskie|woj. lubelskiego]] w Polsce noszą nazwę '''Kurów''' ({{W języku|en|Kurów}}), a także '''Kur
```

### ScratchGPT-100m — Step 42497 / original prompts

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
Stacja powstała w [[1899]] r. na linii [[Wiedeń]] – [[Wiedeń]], w [[Austria|Austrii]]. Linia została otwarta w [[1902]] r. wraz z [[Tramwaje w Wiedniu|komunikacją tramwajową]].

== Linie kolejowe ==
* [[Wiedeń]] – [[Wiedeń]]

== Przypisy ==
{{Przypisy}}

{{Stacja kolejowa/sąsiednie
|stacja        = Südliche Weis
|linia         = [[Wiedeń]] – Wiedeń
|stacja        =
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz|800x3|Billboard}}
{{inne znaczenia|2=[[Billboard (album)|CD „Billboard”]]}}
{{Infobox wiersz|440x440x440x440x440x440x440x3|CD „Billboard”}}
}}
'''Beyonce Cooper''' (ur. [[9 października]] [[1949]] w [[Dallas]]) – [[Stany Zjednoczone|amerykański]] [[Infobox wiersz|inflektor]], [[Model (zawód)|model]] i [[
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 dzielnic [[Bielsko-Biała|Bielska-Białej]], która posiada do dzisiaj jednego miasta.

== Historia ==
'''Bielsko-Biała''' jest częścią [[Dzielnica miasta|dzielnicy]] [[Osiedle Stare Osiedla|Osiedla Stare]].

'''Osiedla Bielska-Białej''' powstawały w latach 1878–1882, kiedy to powstał tu [[Pałac Lange|pałac Lange]].

=== Bielsko-Biała (dwór) ===

```

### ScratchGPT-100m — Step 48586 / original prompts

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
Stacja powstała w 1877 roku w wyniku rozbudowy linii kolejowych łączących [[Żytomierz]] z [[Kowel|Kowlem]].

15 lutego 1910 roku otwarto linię wraz z [[Tarnopol]]em do [[Witebsk]]a. Była ona przystosowana do ruchu towarowego. Dopiero w 1920 roku uruchomiono linię kolejową z [[Oleszków|Oleszkowa]] do [[Kowel|Kowla]].

== Linie kolejowe ==
* [[Linia kolejowa Witebsk – Brzeżany
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|11}}
{{nihongo|'''Itō'''|テイタ|Ito}} – japoński [[saksofon]] [[folk]]owy z [[Grecja|Grecji]] pochodzenia [[Mezoameryka|mezoama]]. Jest to najsłynniejszy salon w Europie.

Itō wydał swój pierwszy singiel ''Once Undead'', po czym przeniósł się do [[Japonia|Japonii]] w [[Nowy Jork|Nowym Jorku]]. Debiutował w [[1991]] roku w solowym [[
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek [[Okręt|okrętów]] polskiej [[Marynarka Wojenna|Marynarki Wojennej]]. Okręt został [[Wodowanie|zwodowany]] 19 lipca 1934 roku w [[stocznia|stoczni]] [[Chatham Dockyard]] w [[Chatham (Wielka Brytania)|Chatham]] i wszedł do służby w [[Naval Group|niemieckiej marynarce wojennej]] 25 maja 1935 roku. Jednostka otrzymała nazwę ''[[Okręty podwodne typu „A”|A]]'', a pod numerem 26 – ''S
```

### ScratchGPT-100m — Step 54522 / original prompts

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
Po upadku powstania styczniowego i napoleońskiej [[rewolucja październikowa|rewolucji październikowej]] miasto znalazło się w [[Królestwo Polskie (kongresowe)|Królestwie Polskim]], gdzie zostało zamknięte przez władze rosyjskie.

W 1870 na wniosek [[Królestwo Polskie (kongresowe)|Królestwa Polskiego]] znajdowało się w [[Królestwo Polskie (kongresowe)|Królestwie Polskim]].

24 kwietnia 1870 decyzją [[Konstytucja 3 maja|Konstytucji 3 maja]] powiat
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Listy nagród]]<|endoftext|>{{Album muzyczny infobox
 |rodzaj albumu             = studyjny
 |tytuł                     = Celebration
 |okładka                   = 
 |wykonawca                 = [[Cedric Alexander]]
 |wydany                    = [[9 października]] [[1992]]<ref>{{cytuj stronę|url=https://www.allmusic.com/album/celebration-r384279|tytuł=Cedric Alexander – Celebration|autor=Steve Huey|opublikowany=[[AllMusic]]|język=en|
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gmina wiejska]] istniejąca w latach 1945–1954<ref>Od 1 grudnia 1945 do 28 września 1954</ref> w [[Województwo wrocławskie (1946–1975)|woj. wrocławskim]] (dzisiejsze [[województwo dolnośląskie|woj. dolnośląskie]]). Siedzibą władz gminy było miasto [[Bardo (miasto)|Bardo]]<ref>{{Cytuj |autor = Urząd Gminy Bardo |tytuł = Uchwały Rady Gminy Bardo z dnia 25 maja 1954 r. w sprawie podziału na gminy na gromady powiatu brodnickiego |data = 1954-05-25 |data dostępu = 2026
```

### ScratchGPT-100m — Step 60607 / original prompts

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
Stacja powstała w 1877 roku w wyniku rozbudowy linii kolejowej [[Szczecin]]-[[Krobia]]–[[Opole]]. Jej pierwszym właścicielem została firma [[Friedrich Engels|Engels]], w 1895 roku [[Bank Gdański (1874–1910)|Bank Gdański]], a w 1918 roku [[Bank Handlowy w Poznaniu|Bank Handlowy]]<ref name=":0">{{Cytuj |autor = Tomasz Szczepański |tytuł = Poznań - przewodnik po zabytkach i historii |data = 2014 |isbn = 978-83-63768-72-4 |
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infobox| ]]<|endoftext|>{{Inne znaczenia|rosyjskiego dyplomaty|[[Atanazy (Bułgaria)|Bułgaria w Słowenii]]}}
[[Plik:Dubrovnik - Summer Map of Estonia by Google Art Project.jpg|thumb|Porównanie rozmieszczenia [[Estonia|Estonii]] i [[Rosja|Rosji]]]]
'''Atanazy Sobczak''' ([[język rosyjski|ros.]] Атаназий Собкой
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek [[Ludowe Wojsko Polskie|ludowego Wojska Polskiego]]. Jej podstawą jest [[jednostka wojskowa]] dla [[Wojska inżynieryjne|wojsk inżynieryjnych]] w [[Wojska inżynieryjne|wojsku inżynieryjnym]] [[Ludowe Wojsko Polskie|ludowego Wojska Polskiego]] oraz [[Wojska inżynieryjne|wojsk inżynieryjnych]] w [[Wojska inżynieryjne|wojsku inżynieryjnym]] w okresie [[Wojna polsko-bolszewicka|wojny polsko-bolszewickiej]]. Stanowią one [[Jednostka wojskowa
```

### ScratchGPT-100m — Step 66654 / original prompts

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
Po ustanowieniu [[Związek Ludowo-Narodowy|Związku Ludowo-Narodowego]] przez [[August Wilczyński|Augusta Wilczyńskiego]] i [[Jan Kanty Lempa|Jana Kantego Lempę]] (1910-1944)<ref name=":1">{{Cytuj |tytuł = Lempa Jan – Polscy pisarze współcześni |data = |data dostępu = 2022-05-08 |opublikowany = polscy.pl |url = https://polscy.pl/mistyk/lemp-jan/}}</ref> w [[Warszawa|Warszawie]],
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz}}
{{Lista powieści graficznej/nagłówek}}
{{Tankōma}}
{{Manggha}}

[[Kategoria:Listy tomów]]
[[Kategoria:Listy wydawnictw mang i anime]]
[[Kategoria:Listy wydane w Manggha]]<|endoftext|>{{Budynek infobox
 |nazwa                 = Pałac w Lubyszu
 |nazwa oryginalna      = 
 |zabytek               = 
 |zdjęcie               = 
 |opis zdjęcia          = 
 |alt zdjęcia           = 
 |państwo               = PL-LD
 |miejscowość           = [[Lubysz
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek [[Broń masowego rażenia|batmapowych]] [[Kaliber broni|kalibru]] 37&nbsp;mm na [[Broń odprzodowa|broni odprzodowej]], po czym zamieniona została na [[Broń biała|białą]] [[Maska przeciwpancerna|maskę przeciwpancerną]] [[Pistolet maszynowy Browning M1910|Pistoletu maszynowego Browning M1910 „Avenger”]] w [[Broń płynna|
```

### ScratchGPT-100m — Step 72555 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[strefa numeracyjna]] o powierzchni 52&nbsp;933&nbsp;[[Hektar|ha]]. W jej skład wchodzi 13 [[Ogród Botaniczny w Warszawie|ogrodów botanicznych]], 66 [[ogród botaniczny|ogrodów botanicznych]], a także 3 [[park]]i z [[dolina|doliną]] [[Wisła|Wisły]] i w [[Sieć wodna|sieci wodnej]] [[Wisła|Wisły]].

Obszar ten nie należący do obszaru objęty jest [[ochrona czyn
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w 1877 roku w ramach [[File:Kolej-stowarzyszenie-lekarskie.png|thumb|left|240px|Stowarzyszenie Lekarzy Polskich (KLP) w Królewcu]]
Obecny skład linii w Królewcu został wybrany w 1897 roku, a odcinek linii na terenie Królewca został włączony do [[Królestwo Polskie (kongresowe)|Królestwa Polskiego]] i wszedł w skład [[Królestwo Kongresowe|Królestwa Polskiego]]. W tym samym roku włączony do Królewca w związku z rozbudową
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dalekobieżny}}
{{Inne znaczenia||[[Bieda]]}}
{{Infobox wiersz dalekobieżny}}

'''Bieda''' – [[Polska|polski]] [[Infobox wiersz dalekobieżny|internetowy portal wspinaczkowy]], zaprezentowany w [[2021]] roku w [[Katowice|Katowicach]] i [[Bielsko-Biała|Bielsku-Białej]].

Jest jednym z czterech portalów wspinaczkowych [[Alpy|Alp]] o łącznej [[P
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek [[Okręt|okrętów]] polskiej [[Marynarka Wojenna|Marynarki Wojennej]] pod dowództwem kpt. żand. [[Stanisław Popiel (wojskowy)|Stanisława Popiela]], która znajdowała się w [[Bielsko|Bielsku]] na [[Śląsk]]u, stanowiła odwód [[Flota|floty]] polskiej w czasie [[Kampania wrześniowa|wojny obronnej Polski]]. Pierwszym dowódcą okrętu był por. żand. Stanisław Popiel, który prowadził działania bojowe w [[
```

### ScratchGPT-100m — Step 78630 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat lipski|powiecie lipskim]], w [[Wilga (gmina)|gminie Wilga]]<ref name="R2013" /><ref name="teryt" />. Siedziba [[Chociwel (gmina)|gminy Chociwel]].

Miasto założone było w [[1400]] roku, a [[prawa miejskie]] uzyskała w [[1784]] roku.

Miejscowość stanowi przedgranitową miejscowością [[powiat lipski]]. Miejscowość leży przy [[droga wojewódzka nr 8
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w 1877 roku jako część [[Linia kolejowa St. Georgen – Broughton|linii kolejowej St. Georgen – Broughton]] (obecnie w [[Timmings]], w [[Szkocja|Szkocji]]).

== Linie kolejowe ==
* [[Cavan Line]]

== Linki zewnętrzne ==
* [http://www.nsb.no/.INTER/no_db/old_site/Lokalnet/ésthet/index.htm Informacje o stacji na NSB.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz|mks=3|{{link-interwiki |Claudie Péron |Q=Q13269151}}}}.
** [[Birmingham]] – [[Fort Smith (Arkansas)|Fort Smith]] (złożony z [[Allenby]] i [[Cape Halifax (Arkansas)|Cape Halifax]])<ref>{{Cytuj książkę |nazwisko = Boie |imię = Gene |tytuł = The British Archaeological Edition |wydawca = Oxford University Press |miejsce
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[Polska|polski]] [[film komediowy]] w reżyserii [[Andrzej Kondratiuk|Andrzeja Kondratiuka]] z 2000 roku.

== Obsada ==
* [[Roman Wilhelmi]] – mężczyzna z chórem
* [[Anna Sapieństwo-Hryniewiecka]] – Helena
* [[Mieczysław Morański]] – ojciec Haliny
* [[Małgorzata Kożuchowska]] – matka Haliny
* [[Janina Chruścińska-Cieślak]] – siostra Haliny
```

### ScratchGPT-100m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[strefa numeracyjna]] nr 12 z dnia 30 września 1954 r. w sprawie podziału na gromady powiatu kozienickiego; w ramach Zarządzenia Prezydium Wojewódzkiej Rady Narodowej w Kielcach z dnia 20 grudnia 1954 r. w sprawie ogłoszenia uchwał Wojewódzkiej Rady Narodowej w Kielcach z dnia 30 września 1954 r., dotyczących reformy podziału administracyjnego wsi (Dziennik Urzędowy Wojewódzkiej Rady Narodowej w Kielcach z dnia 31 grudnia 1954 r., Nr. 15, Poz. 104)</ref>. Dla gromady ustalono 11 członków gromadzkiej rady narodowej<ref name="grn">Uchwała Prezydium Powiatowej Rady Narodowej w
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w 1877 roku w ramach [[Flatau Schlesien|Kolei Wschodniej]], w związku z budową [[Kolej Warszawsko-Wiedeńska|Kolei Warszawsko-Wiedeńskiej]] w ramach [[Kolej Warszawsko-Wiedeńska|kolei warszawsko-wiedeńskiej]] razem z odgałęzieniem się [[Kolej Warszawsko-Kaliska|Kolei Warszawsko-Kaliskiej]]{{r|st1|st2}}.

Główne wejście do stacji znajduje się przy dworcu kolejowym [[Warszawa Gdańska
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz}}
{{Lista powieści graficznej/nagłówek
 |język          = japoński
 |drugi język    = angielski
 |szerokość      = 100%
 |podkreślenie   = FFFFFF
}}
{{Lista powieści graficznej
 |numer woluminu     = 1 (9)
 |wydano oryginał    = 11 lipca 2005<ref>{{Cytuj |tytuł = 金髪のある決定 2 (9) |data dostępu = 2022-09-17 |opublikowany = [[Shūeisha]] |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[Polska|polski]] [[film komediowy]] w reżyserii [[Andrzej Kondratiuk|Andrzeja Kondratiuka]] z 2000 roku.

== Obsada ==
* [[Rogerio Doria]] – Bruno
* [[Alicja Chybicka]] – Pani Bruno
* [[Barbara Stanwyck]] – Bruno
* [[Michał Bajor]] – pan Banasik
* [[Mariusz Bonaszewski]] – pan Banasik
* [[Marek Frąckowiak]] – pan B
```

### ScratchGPT-100m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[strefa numeracyjna]] nr 12 z dnia 30 września 1954 r. w sprawie podziału na gromady powiatu kozienickiego; w ramach Zarządzenia Prezydium Wojewódzkiej Rady Narodowej w Kielcach z dnia 20 grudnia 1954 r. w sprawie ogłoszenia uchwał Wojewódzkiej Rady Narodowej w Kielcach z dnia 30 września 1954 r., dotyczących reformy podziału administracyjnego wsi (Dziennik Urzędowy Wojewódzkiej Rady Narodowej w Kielcach z dnia 31 grudnia 1954 r., Nr. 15, Poz. 104)</ref>. Dla gromady ustalono 11 członków gromadzkiej rady narodowej<ref name="grn">Uchwała Prezydium Powiatowej Rady Narodowej w
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w 1877 roku w ramach [[Flatau Schlesien|Kolei Wschodniej]], w związku z budową [[Kolej Warszawsko-Wiedeńska|Kolei Warszawsko-Wiedeńskiej]] w ramach [[Kolej Warszawsko-Wiedeńska|kolei warszawsko-wiedeńskiej]] razem z odgałęzieniem się [[Kolej Warszawsko-Kaliska|Kolei Warszawsko-Kaliskiej]]{{r|st1|st2}}.

Główne wejście do stacji znajduje się przy dworcu kolejowym [[Warszawa Gdańska
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz}}
{{Lista powieści graficznej/nagłówek
 |język          = japoński
 |drugi język    = angielski
 |szerokość      = 100%
 |podkreślenie   = FFFFFF
}}
{{Lista powieści graficznej
 |numer woluminu     = 1 (9)
 |wydano oryginał    = 11 lipca 2005<ref>{{Cytuj |tytuł = 金髪のある決定 2 (9) |data dostępu = 2022-09-17 |opublikowany = [[Shūeisha]] |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[Polska|polski]] [[film komediowy]] w reżyserii [[Andrzej Kondratiuk|Andrzeja Kondratiuka]] z 2000 roku.

== Obsada ==
* [[Rogerio Doria]] – Bruno
* [[Alicja Chybicka]] – Pani Bruno
* [[Barbara Stanwyck]] – Bruno
* [[Michał Bajor]] – pan Banasik
* [[Mariusz Bonaszewski]] – pan Banasik
* [[Marek Frąckowiak]] – pan B
```

## ScratchGPT-300m — scratch-polish-dollar-1788900395083493729-wiki-300-uniform

Source: wiki-scratch-v1

Parameters: 291,025,920; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 133.33 minutes; worker: 135.18 minutes; estimated worker compute: $9.3979. Tokens presented: 1,096,482,816, sampled with replacement.

Selected development loss: 1.4175; selected test loss: 1.2860 nats/token. Fresh-process reload matches: True.

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

Factual preference: 7/10. Mean repeated word 4-gram fraction: 0.0199. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
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
 [[stacja kolejowa]] w [[Warszawa|Warszawie]], w dzielnicy [[Śródmieście Południowe]], w [[Warszawa|Warszawie]]. Rozbudowana w okresie międzywojennym.

== Historia ==
Stacja została wybudowana w latach 1924–1934 w pobliżu stacji kolejowej [[Warszawa]] – [[Łódź|Łodzi]]<ref>{{Cytuj książkę | tytuł = Atlas Lineusz - Mapa | wydawca = PKP Polskie Linie Kolejowe | miejsce = Warszawa | data = 2003 | strony = 11 | isbn = 83-920757-2-8}}</ref> przez spółkę [[PKP Polskie Lin
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat bocheński|powiecie bocheńskim]], siedziba [[Bukowa (gmina)|gminy miejsko-wiejskiej Bukowa]]. Liczba mieszkańców wynosi 1 067.

== Historia ==
Wieś była wzmiankowana już w XV w. pod nazwą ''Klein Bukov'' (lub ''Bukov'') w dokumencie fundowanym przez cesarza [[Henryk II Święty|Henryka II]] w roku 1603. Jest to wieś królewska. Znajd
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[Wisła (miasto)|wiślne miasto]] w [[Polska|Polsce]], położone w [[Województwo podkarpackie|województwie podkarpackim]], w [[Powiat tarnobrzeski|powiecie tarnobrzeskim]], siedziba [[Wisła (miasto)|wiślańskiego miasta]] oraz [[miasto|miasta]] [[Wisła]].

Miasto położone jest w [[Województwo podkarpackie|województwie podkarpackim]], w [[Powiat tarnobrzeski|powiecie tarnobrzeskim]], w [[Wisła (miasto)|Wiśle]]<ref name=geoportal>{{
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski poeta, prozaik, dramaturg i tłumacz.

== Życiorys ==
Adam Mickiewicz urodził się 16 czerwca 1910 roku w [[Sęków (powiat garwoliński)|Sękowie]] w [[Królestwo Polskie (kongresowe)|Królestwie Polskim]]. Jego ojcem był Jan Mickiewicz (ur. 1880), aktor, aktor i reżyser teatralny.
[[Plik:Adam Mickiewicz (grób).JPG|mały|Grób Adama Mickiewicza na cmentarzu Powązkowskim]]
Adam Mickiewicz ukończył szko
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 polski pianista, kompozytor i pedagog.

== Życiorys ==
Był synem Ludwika i Marii Fryderyków. Podczas studiów był uczniem [[Erazm Deyder|Erazma Deydera]] i [[Adam Otto-Fryderyk Bednorz|Adama Otto-Fryderyka Bednorza]]. W 1842 roku dostał się do kręgu muzyków powstańczego teatru w [[Warszawa|Warszawie]]. W tym czasie pracował w warszawskim Teatrze Dramatycznym. Po ukończeniu
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[rzeka]] będąca jednostką długości 2,5 km, będąca naturalnym środkiem obsługi [[wiatr]]u, oddzielającym [[Ziemia|Ziemię]] od [[Ziemia|Ziemi]]. Wypływa z równiny [[Ziemię|Ziemi]] i tuż przy biegu [[Zatoka (geografia)|zatoki]] [[Ziemia|Ziemi]], której wody są w stanie przepłynąć około 60 km od Ziemi. Kilkadziesiąt kilometrów poniżej [[Woda|wody]] Ziemi
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwsze wzmianki o wsi pojawiają się w dokumentach z lat 1171, 1176, 1236, 1246<ref name="SUS" />.

== Zobacz też ==
* [[Komorowo]]

== Przypisy ==
<references>
<ref name="pwl">{{Polska w liczbach|id=wies_Komorowo_mielno_mazowieckie|nazwa=Wieś Komorowo w liczbach|data dostępu=2025-04-14}}</ref>
<ref name="nsp">{{Cytuj |url = https
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
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

### ScratchGPT-300m — Development-selected

Factual preference: 7/10. Mean repeated word 4-gram fraction: 0.0199. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
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
 [[stacja kolejowa]] w [[Warszawa|Warszawie]], w dzielnicy [[Śródmieście Południowe]], w [[Warszawa|Warszawie]]. Rozbudowana w okresie międzywojennym.

== Historia ==
Stacja została wybudowana w latach 1924–1934 w pobliżu stacji kolejowej [[Warszawa]] – [[Łódź|Łodzi]]<ref>{{Cytuj książkę | tytuł = Atlas Lineusz - Mapa | wydawca = PKP Polskie Linie Kolejowe | miejsce = Warszawa | data = 2003 | strony = 11 | isbn = 83-920757-2-8}}</ref> przez spółkę [[PKP Polskie Lin
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo małopolskie|województwie małopolskim]], w [[powiat bocheński|powiecie bocheńskim]], siedziba [[Bukowa (gmina)|gminy miejsko-wiejskiej Bukowa]]. Liczba mieszkańców wynosi 1 067.

== Historia ==
Wieś była wzmiankowana już w XV w. pod nazwą ''Klein Bukov'' (lub ''Bukov'') w dokumencie fundowanym przez cesarza [[Henryk II Święty|Henryka II]] w roku 1603. Jest to wieś królewska. Znajd
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[Wisła (miasto)|wiślne miasto]] w [[Polska|Polsce]], położone w [[Województwo podkarpackie|województwie podkarpackim]], w [[Powiat tarnobrzeski|powiecie tarnobrzeskim]], siedziba [[Wisła (miasto)|wiślańskiego miasta]] oraz [[miasto|miasta]] [[Wisła]].

Miasto położone jest w [[Województwo podkarpackie|województwie podkarpackim]], w [[Powiat tarnobrzeski|powiecie tarnobrzeskim]], w [[Wisła (miasto)|Wiśle]]<ref name=geoportal>{{
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski poeta, prozaik, dramaturg i tłumacz.

== Życiorys ==
Adam Mickiewicz urodził się 16 czerwca 1910 roku w [[Sęków (powiat garwoliński)|Sękowie]] w [[Królestwo Polskie (kongresowe)|Królestwie Polskim]]. Jego ojcem był Jan Mickiewicz (ur. 1880), aktor, aktor i reżyser teatralny.
[[Plik:Adam Mickiewicz (grób).JPG|mały|Grób Adama Mickiewicza na cmentarzu Powązkowskim]]
Adam Mickiewicz ukończył szko
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 polski pianista, kompozytor i pedagog.

== Życiorys ==
Był synem Ludwika i Marii Fryderyków. Podczas studiów był uczniem [[Erazm Deyder|Erazma Deydera]] i [[Adam Otto-Fryderyk Bednorz|Adama Otto-Fryderyka Bednorza]]. W 1842 roku dostał się do kręgu muzyków powstańczego teatru w [[Warszawa|Warszawie]]. W tym czasie pracował w warszawskim Teatrze Dramatycznym. Po ukończeniu
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[rzeka]] będąca jednostką długości 2,5 km, będąca naturalnym środkiem obsługi [[wiatr]]u, oddzielającym [[Ziemia|Ziemię]] od [[Ziemia|Ziemi]]. Wypływa z równiny [[Ziemię|Ziemi]] i tuż przy biegu [[Zatoka (geografia)|zatoki]] [[Ziemia|Ziemi]], której wody są w stanie przepłynąć około 60 km od Ziemi. Kilkadziesiąt kilometrów poniżej [[Woda|wody]] Ziemi
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwsze wzmianki o wsi pojawiają się w dokumentach z lat 1171, 1176, 1236, 1246<ref name="SUS" />.

== Zobacz też ==
* [[Komorowo]]

== Przypisy ==
<references>
<ref name="pwl">{{Polska w liczbach|id=wies_Komorowo_mielno_mazowieckie|nazwa=Wieś Komorowo w liczbach|data dostępu=2025-04-14}}</ref>
<ref name="nsp">{{Cytuj |url = https
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
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

### ScratchGPT-300m — Step 2580 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy w [[Dzierżanowo (rejon kołczycki)|Dzierżanowie]], w [[Rejon kołczycki (rejon kołczecki)|rejonie kołczeckim]], w [[Sielsowiet Stalowa Kołczyńska|sielsowiecie Stalowa Kołczyńska]].

== Historia ==
W XIX i w świetle dóbr [[Autorament|autoramentu narodowego]] położone były w [[Imperium Rosyjskie|Rosji]], w [[Powiat wilejski (Galicja)|powiecie wilejskim]]<ref>{{Cytuj |autor
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwsze polskieństwo zostało założone w [[1995]] roku.

== Turystyka ==
Osada ta nastąpiła do użytku w [[Powiat błszczakowski (160)#Powiat brzszczakowski (161)#Powiat brzszczakowski (161)#Powiat błszczakowski (162)#Powiat brzszczakowski (163)#Powiat brzszczakowski (161)#Powiat brzszczakowski (161)#Powiat brzszczakowski (17)#Powiat brzszczakowski (161
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Inflacje gazów]]<|endoftext|>{{Polska jednostka administracyjna infobox
 |nazwa                     = Rejonowa
 |dopełniacz nazwy          = 
 |jednostka                 = [[Gromada (podział administracyjny)|gromada]]
 |lata istnienia            = 1954–1973
 |zdjęcie                   = 
 |opis zdjęcia              = 
 |herb                      = 
 |flaga                     = 
 |wariant flagi             = PRL
 |województwo               = [[województwo częstochowskie|częstochowskie]]
 |powiat                    = 1954–55: [[powiat żnin|żnin]]<br />1956–55
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna jednostka administracyjna w [[Województwo białostockie (II Rzeczpospolita)|województwie białostockim]], w [[Powiat będziński (województwo białostockie)|powiecie będzińskim]], w [[Bogów (gmina)|gminie Bogów]]{{r|R2013|R2013}}.

Wierni Kościoła [[Kościół łaciński|rzymskokatolickiego]] należą do parafii [[Parafia Trójcy Przenajświętszej w Bogowie|Matki Bożej Królowej Polski w Bogowie]]{{r|par}}.

Po [[Agresja ZSRR na Polskę|agresji ZSRR na Polskę]] w 1939 wieś, wieś w rejonie [[
```

### ScratchGPT-300m — Step 5115 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]] istniejąca w latach 1954–1972</small> w [[Województwo warszawskie (1944–1975)|woj. warszawskim]], w [[Powiat węgrowski|powiecie węgrowskim]] w woj. warszawskim<ref>{{Dziennik Ustaw|rok=1954|numer=49|pozycja=128}}</ref><ref>{{cytuj książkę|tytuł=Mała Encyklopedia Powszechna PWN|wydawca=[[Wydawnictwo Naukowe PWN|Państwowe Wydawnictwo Naukowe]]|miejsce=Warszawa|rok=1959}}</ref>.

Gromadę Węgrowo z siedzibą GRN w [[Węgrow
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku bitwy pod [[Bitwa pod Słobódką|Słobódką]], w maju 1 października [[1610]] wojska wielkiego mistrza [[Władimir Iwanow|Jana Iwanowa]], w składzie [[konfederacja targowicka|konfederacji targowickiej]] [[Imperium Osmańskie]]go, walczyła o [[I bitwa pod Słonimem|Słonimem]]. W czasie [[Wyprawa krzyża na Słonimiem|konfederacji targowickiej]] w [[Bitwa pod Słonimem|bitwie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 infobox/Kolor|S3}}
{{Medalista infobox/Kolor|T2}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3}}
{{Medalista infobox/Kolor|S3
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna jednostka administracyjna [[województwo wołyńskie|województwa wołyńskiego]] w [[Polska|Polsce]], w [[województwo wołyńskie|województwie wołyńskim]], w [[powiat wołyński|powiecie wołyńskim]], w [[Kryłów (gmina)|gminie Kryłów]].

== Opis ==
Oznaczenie PAŽ: Droga krajowa [[Łańcut (droga)|Łańcut]] – [[Łańcut (droga)|Łańcut]] – [[Wisła (miasto)|Wisła]] – [[Białystok (stacja kolejowa)|Biały
```

### ScratchGPT-300m — Step 7635 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część [[wieś|wsi]] [[Kopytne (województwo mazowieckie)|Kopytne]] w [[Polska|Polsce]], położona w [[Województwo mazowieckie|województwie mazowieckim]], w [[Powiat siedlecki|powiecie siedleckim]], w [[Łuck (gmina wiejska)|gminie Łuck]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo siedleckie|województwa siedleckiego]].

== Przypisy ==
{{Przypisy}}

{{Gmina Łuck}}

[[Kategoria:Kopytne (województwo mazowieckie)]]
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja została otwarta w latach 1868–1880 jako własność prywatną. Po śmierci ojca, w 1870 roku, została otwarta, a w 1874 roku uruchomiono pierwszą [[Stacja kolejowa|stację kolejową]] z [[Pietà|Pietà]] do [[Todi]] w [[Dolina Hurrika|Dolinie Hurrika]]. W latach 1889–1893 odbyła się tutaj [[Stacja kolejowa na Santiago|stacja w Santiago]], a w latach 1889–1899 w [[Piet�
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 infobox
 |nazwa               = Wenus (przedsiębiorstwo WTMT)
 |logo                = WTMT, Logo, WTMT, WTMT, Logo, Wenus TC, Logo.svg
 |grafika             = MMT 3 Fruits.jpg
 |opis grafiki        = Siedziba zarządu
 |autor               = [[MT]]
 |platforma sprzętowa = [[WTMT]], [[Lobbing]], [[OGP]], [[Microsoft Windows|W
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu ich zniesienia z dniem 1 stycznia 1973<ref>{{
```

### ScratchGPT-300m — Step 10127 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo wielkopolskie|województwie wielkopolskim]], w [[powiat rawicki|powiecie rawickim]], w [[Stara Czarna (gmina)|gminie Stara Czarna]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo rawickie|województwa rawickiego]].

== Położenie geograficzne ==
Wieś leży na [[Pole (góra)|Pole]].

== Nazwa ==
W [[język niemiecki|Niemczech]] nazwa miejscowości pochodzi od [[Język niemiecki|niemie
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początki osadnictwa w Benzynie nie są znane. W [[XIII wiek|XIII w.]] Benzyna ograbiona była przez [[kamień brunatny]]. W 1509 r. spłonęła cała okolica, z której pochodzi. Budowla nadawał do budowy [[Dwór w Benzynie|dworowi]] [[Dwór w Benzynie|benzynie]]. W 1518 r. nadał Benzynie [[Starostwo|starostwu]] w Benzynie ziemie [[Książę
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|SBR|[[Vasilievski (album)|Vasilievski]] feat. [[Vasilevski (zespół muzyczny)|Vasilevski]]|4:46|
|4||[[Critici (album)|Critici]] (Feat. [[Tomek]])||3:18|
|5||[[Vasilevski (album)|Vasilevski]] (Feat. [[Tupac (zespół muzyczny)|Tupac]])||0:51|
|6||[[Vasilevski]] (Fe
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 konstytuatorów [[Rada Europy|Rady Europy]], które obejmowały [[Królestwo Węgier|Królestwa Węgier]] (do 1863 roku [[Królestwo Węgier (1920–1918)|Królestwo Węgier]] i [[Królestwo Wielkiej Brytanii|Królestwo Wielkiej Brytanii]] (1867–1868).

== Organizacja Rady ==
Pierwsza odmiana [[Rada Europy|Rady Europy]] powstała w 1810 roku. Do 17 marca stała się członkiem [[Pruska Dywizja Piechoty|Pruskiej Dywizji Piechoty]] w [[Berlin]]ie. 

W roku 1811 utworzono
```

### ScratchGPT-300m — Step 12612 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy położony w dzielnicy [[Słupia (Warszawa)|Słupia]] przy [[ulica Tadeusza Kościuszki w Warszawie|ulicy T. Kościuszki]] 1. Jego obecną nazwę zmieniono na [[Kalwaria (Warszawa)|Kalwaria]].

== Zobacz też ==
* [[Powstańców Warszawy]]

== Linki zewnętrzne ==
* {{Bazakolejowa.pl |stacja |id = 3657 |tytuł = Warszawa |data dostępu = 2026-01-24}}

{{Stacja kolejowa/sąsiednie
|stacja       
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. na linii [[Cieplice Śląskie (stacja kolejowa)|Cieplice Śląskie]] – [[Wrocław Główny]] – [[Wrocław Główny]] – [[Chorzów]] – [[Toruń Główny]] (zlikwidowana) – Chorzów Południowy (zlikwidowana) – [[Wrocław Główny]] – [[Gryfino]] (zlikwidowana) – Chorzów Główny – [[Kielce Główne]])

== Linie kolejowe ==
* [[Linia kolejowa nr 232 (Chorzów)|Linia kolejowa nr
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

{{DEFAULTSORT:Bernatik, György}}
[[Kategoria:Bośniaccy inżynierowie]]
[[Kategoria:Bośniaccy parlamentarzyści]]
[[Kategoria:Urodzeni w 1942]]<|endoftext|>{{Dopracować|więcej przypisów=2022-09}}
{{Artysta infobox
 |imię i nazwisko       = John Laurence Kirkwood
 |imię i nazwisko org   = 
 |pseudonim             = 
 |grafika               = 
 |opis grafiki          = 
 |pełne imię i
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 [[województwo|województwa]] [[województwo mazowieckie|mazowieckiego]] [[województwo mazowieckie|województwa mazowieckiego]], obejmująca wtedy województwa mazowieckie.

== Obsługiwane przepisy ==
Zgodnie z [[Ustawa z dnia 19 marca 1997 roku|ustawą z 1997 roku]] obowiązuje zarządzanie danymi.
W każdej z dwunastu [[gmina|gmin]] i [[senator]]ów [[senator]]a wykonywana jest osoba, która posiada prawo do głosowania ze względu na stan rywalizacji z [[okręg wyborczy nr 26 do Sejmu
```

### ScratchGPT-300m — Step 15101 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[Genewa]], [[Francja]] – [[Dordrecht]], [[Szwajcaria]] – [[Baden-Baden]], [[Szwajcaria]] – [[Strasburg]], [[Włochy]] – [[Chamonix-Mont-Blanc|Chamonix]], [[Francja]] – [[Vancouver]], [[Szwajcaria]] – [[Lozère]], [[Szwajcaria]] – [[Verdunsberg]], [[Szwajcaria]] – [[Sassenheim]], [[Szwajcaria]] – [[Weinheim]], [[Szwajcaria]] – [[Oberkirchen]], [[Szwajcaria]] –
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwsze informacje o wsi pochodzą z roku 1774. Wtedy to w miejscowości znajdował się szpital, a w 1816 roku we wsi mieszkało 18 osób<ref name="SgKP">{{SgKP|X|623|Sarny (11) pow. wrocki}}</ref>. Oddano ją do użytku w dniu 19 grudnia 1878 roku.

== Przypisy ==
{{Przypisy}}

== Bibliografia ==
* {{SgKP|X|623|Sarny (11) pow. wrocki}}
* {{SgKP|VII|682|Sarny
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infobox]]
[[Kategoria:Infobox]]<|endoftext|>{{Album muzyczny infobox
 |rodzaj albumu             = studyjny
 |tytuł                     = Where the Knows This Number
 |okładka                   = 
 |wydany                    = 27 października 2004
 |nagrywany                 = 
 |gatunek                   = [[Rock alternatywny]], [[rock]]
 |długość                   = 
 |wytwórnia                 = [[Rock Grunge]], [[Atlantic Records]], [[Atlantic Records]], R&B Entertainment
 |producent                
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[kommuna internetowa]] stworzona przez [[TM (protokół)#Polskie relacje|TM]] i [[Szyfr (socjologia)|szyfru]] [[Kod QM|Kode QM]], która łączy [[konkubinat]] z [[CMOS]]. Komunikacja między językiem a [[Język programowania|językiem]] [[PC/M]], powoduje analogowy dostęp do serwera [[WWW]] za pomocą jednego języka z systemem [[WWW]], [[S
```

### ScratchGPT-300m — Step 17624 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy w [[Dzielno (Warszawa)|Dzielnie]], w dzielnicy [[Śródmieście-Centrum]], w [[Warszawa|Warszawie]], na [[Linia kolejowa nr 215|linii kolejowej nr 215]] [[Warszawa Zachodnia]] – [[Warszawa Wschodnia]].

== Ruch pasażerski ==
{| class="wikitable" 
! Rok
! Wymiana pasażerska na dobę
|-
| 2017<ref name="roz">{{cytuj stronę|url=https://utk.gov.pl/pl/aktualnosci/14537,Najwieksze-i-
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w czasach [[Ziemie Rzeczypospolitej pod zaborami|zaborów]] w gminie Wiszniewo, w powiecie święciańskim [[Imperium Rosyjskie]]go. Za czasów [[Królestwo Kongresowe|Królestwa Polskiego]] pod koniec XIX wieku należała do [[Powiat postawski|powiatu postawskiego]] [[Gubernia wileńska|guberni wileńskiej]], a w latach 1867–1915 w [[Gubernia wileńska|guberni wileńskiej]]<ref>{{Cytuj książkę |autor = |tytuł = Skorowidz dóbr tabularnych w powiecie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infobox]]<|endoftext|>{{Album muzyczny infobox
 |rodzaj albumu             = studyjny
 |tytuł                     = Coccere
 |okładka                   = 
 |wykonawca                 = [[Coccere (zespół muzyczny)|Coccere]]
 |wydany                    = [[16 lipca]] [[2004]]
 |nagrywany                 = [[22 lipca]] [[2004]]
 |gatunek                   = [[muzyka pop|pop]]
 |długość                   = 49:52
 |wytwórnia                 = [[Warner Records]]
 |producent                 = 
 |oceny                     = 
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek [[Ludowe Wojsko Polskie|ludowego Wojska Polskiego]]. Siły 
[[Armia Krajowa]] i [[Armia Krajowa]] walczyły z oddziałami [[Armia Krajowa|AK]] i samoobrony; w większości działały w [[Bataliony Chłopskie|Batalionach Chłopskich]], oddziały terenowe [[Armia Krajowa|AK]] i [[Państwowa Straż Pożarna|PStP]] oraz oddziały partyzanckie: „A”, „S” i „K”, oraz resztki
```

### ScratchGPT-300m — Step 20132 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat warszawski zachodni|powiecie warszawskim zachodnim]], w [[Ajurukreńsk (gmina)|gminie Ajurukreńsk]]<ref name="teryt" /><ref name="roz" />. Ma status sołectwa<ref name="sol" />. Leży przy [[Droga krajowa nr 75 (Polska)|drodze krajowej nr 75]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo ciechanowskie|
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w czasach [[Ziemie Rzeczypospolitej pod zaborami|zaborów]] w granicach [[Imperium Rosyjskie|Imperium Rosyjskiego]].

Stacja została otwarta w dniu 31 grudnia 1897 roku. Właścicielem stacji był ówczesny [[Wojskowy Instytut Geograficzny]].

== Przypisy ==
{{Przypisy}}

== Bibliografia ==
* {{Cytuj stronę | url =https://railwayz.info/photolines/station/187 | tytuł =Станция Георгиев | opublikowany =railwayz.info | data
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wierszowy}}
{{Zastrzeżenia|Prawo}}

[[Kategoria:Artykuły, które powinna mieć każda Wikipedia (poniżej 10k)| ]]
[[Kategoria:Artykuły, które powinny mieć każda Wikipedia (poniżej 10k)]]<|endoftext|>{{Lokomotywa infobox
 |nazwa                              = 12C13
 |grafika                            = 
 |opis grafiki                       = 
 |inne oznaczenia                    = 
 |producent                          = [[Förvárda|Förvárda-J
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[polska]] [[uczelnia publiczna|uczelnia publiczna]] działająca w [[Polska|Polsce]]. Została utworzona w 1993 roku. Oddział w Warszawie [[Politechnika Warszawska|Politechniki Warszawskiej]] ma swoją siedzibę w Warszawie.

== Historia ==
Uczelnia została utworzona w 1993 roku jako [[Szkoła naukowa|szkoła]] kształcąca nauczycieli w [[Szkoła średnia|szkole średniej]] nr 6 w [[Grodzisk Mazowiecki|Grodzisku Mazowieckim]] w Polsce. Inicjatorką powstania [[Szkoła nau
```

### ScratchGPT-300m — Step 22640 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat lipski|powiecie lipskim]], w [[Michałów (gmina)|gminie Michałów]]<ref name="teryt" /><ref name="roz" />.

Według stanu z 1 grudnia 1939 w gminie Michałów m.st. Warszawy mieszkało 1393 mieszkańców<ref name="BVG" />.

Właściwa kolonia (nie istnieje) była osadą wsi [[Grabówka (Warszawa)|Grabówka]] w [[Stare Miasto w Warszawie|Starym
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w 1877 roku w ramach [[Linia kolejowa Paryż – Marsylia|linii Paryż – Marsylia]]. Do roku 1920 znajdowała się w jej obsługi, a następnie została zamknięta. Od 1883 roku stacja istniała do roku 1900.

== Linie kolejowe ==
* [[Linia kolejowa Paryż – Marsylia|Paryż – Marsylia]]

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
* [https://archive.is/20130429163843/http://www.ter.sncf.com/
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infobox]]
[[Kategoria:Infobox]]<|endoftext|>{{dopracować|źródła=2025-11}}
'''Skok''' – jedna z [[koło (żeglarstwo)|koła]] mostu, której kąty między [[żaglowiec|żaglowcami]] i [[żaglowiec|żaglowcami]] należą do [[Śródmózgowie|śródmózgowia]] [[most]]u.

Około 12 [[kilometr|km]] od mostu
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek podziału terytorialnego państwa<ref>{{Cytuj |tytuł = Umowa między Rządem Rzeczypospolitej Polskiej a Rządem Republiki Czeskiej o przejściach granicznych, przekraczaniu granicy poza przejściami granicznymi, sporządzona w Warszawie dnia 22 listopada 1996 roku (M.P. 2003 nr 22, poz. 234). |data dostępu = 2023-02-15 |opublikowany = isap.sejm.gov.pl |url = https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?
```

### ScratchGPT-300m — Step 25160 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dzielnica miasta [[Kraków|Krakowa]] w [[Dzielnica V Krowodrza|dzielnicy V Krowodrza]], na osiedlu [[Praga-Północ]], w dzielnicy [[Błonie (Kraków)|Błonie]], w dzielnicy [[osiedle Mirów (Kraków)|Mirów]], w dzielnicy [[Błonie (Kraków)|Błonie]]. Od północy graniczy z dzielnicami [[Błonie (Kraków)|Błonie]] i [[Zabłocie (Kraków)|Zabłocie]] tworząc dzielnicę [[Jemielno
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w XIX wieku w miejscu obecnego młyna. Przypuszcza się, że jej długość wynosi ok. 7,5 km i wynosi ok. 1 km. Ostatni odcinek linii została wybudowana w [[XIX wiek]]u, która miała połączyć [[Biała (dopływ Wisły)|Białą]] z [[Miła|Miłą]] i [[Prądy (powiat białostocki)|Prądami]] i to na koniec [[XIX wiek|XIX]] w. stanowiła jeden z torów łączących Białe i Prądy z [[Ra
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Inflacja| ]]<|endoftext|>[[Plik:John the Ripper, Jr., and C. P. Souza.jpg|mały|''John the Ripper'' namalowany w 1888]]
'''John the Ripper''' – polski [[malarstwo|malarz]] i [[ilustracja|ilustrator]] malowany na desce.

W 1848 roku, w wieku 15 lat został [[inżynier]]em i założył awangardowy [[klub studencki|klub studen
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 lista osób notowanych na [[lista przebojów|liście przebojów]], która zawiera 15 tysięcy sprzedanych kopii.

Amerykańska stacja telewizyjna [[Columbia Broadcasting System|CBS]] ogłosiła plany połączenia 1 stycznia 2014, które powstało w ramach kampanii reklamowej [[MTV Polska]]<ref>{{cytuj stronę |url = http://www.wirtualnemedia.pl/artykul/maciej-rakowski-w-polskiej-tutce-na-kolejne-mtv-u
```

### ScratchGPT-300m — Step 27667 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dzielnica [[Warszawa|Warszawy]] położona w południowym [[Warszawa|warszawskim]] [[jednostka pomocnicza gminy|jednostce pomocniczej]] miasta, w dzielnicy [[Śródmieście (Warszawie)|Śródmieście]].

== Położenie ==
[[Podział administracyjny Warszawy|dzielnica]] obejmuje m.in. dzielnicę Śródmieście Północ–Śródmieście{{r|Pl}}. Dzielnica leży w południowo-zachodniej części dzielnicy Śródmieście Północ–Śródmieście Północ–Śródmieście Północ–Śródmieście Północ
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w czasach [[Królestwo Prus|pruskich]] jako stacja końcowa linii kolei hamburskiej, która została ukończona w 1815 roku. Ostatnie prace wykończeniowe rozpoczęły się w 1911 roku, kolejne prace wykończeniowe zostały ukończone w 1923 i 1924 roku. W latach 1935–1945 stacja należała do [[Deutsche Bahn]], a w latach 1945–1949 – [[DB Regio]].

== Linie kolejowe ==
* [[Linia kolejowa Hamburg – Görlitz|Hamburg – Görlitz]]
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz
|tytuł=Ogród botaniczny, krajobraz naturalny – przewodnik, opracowany, na bazie monitoringu
|source=[https://www.gov.pl/web/gdos/ogrod-botaniczny-krajobraz-naturalny.html monitoring i usunięcie skarbu]
}}</ref>
<ref name=":3">{{Cytuj |autor =  |tytuł = Aktualizacja – Konsumpcja dla dzieci |data =  |url = https://www.gov.
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek organizacyjnych [[Polityka bezpieczeństwa|polityki bezpieczeństwa]], która powołana została 18 lipca 2008<ref>Ustawa z dnia 18 lipca 2008 r. o polityce bezpieczeństwa ({{Dziennik Ustaw|rok=2008|numer=2|pozycja=22}}) oraz art. 2 ust. 2. 1 [[Konwencja haska III|Konwencji haskiej]] z 2008 ({{Dziennik Ustaw|rok=2008|numer=14|pozycja=93}})</ref>.

== Charakterystyka ==
=== Identyfikacja (dla określonego typu
```

### ScratchGPT-300m — Step 30161 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dzielnica [[Warszawa|Warszawy]] położona w południowo-zachodniej części miasta. Na terenie dzielnicy znajduje się [[Muzeum Regionalne Ziemi Warszawskiej w Warszawie]]. W latach 90. XX wieku zdemontowano uroczysko Stalową Kotlinę<ref>[http://www.warszawa.pl/zwiedzaj/warszawa-warszawska-z-dnia-30-marca-2013-r--w-soboty-r | Centrum wyjaśniania i uroczystości w Warszawie] [data dostępu: 2013-09-
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w czasach [[Królestwo Prus|pruskich]] jako stacja końcowa linii kolei wąskotorowej (początkowo [[Linia kolejowa|linia]] ''[[Linia kolejowa Berlin – Frankfurt|Berlin – Frankfurt]] (Черница). Stację końcową otwarto w 1871 roku<ref name=":0">{{Cytuj |tytuł = Mapa |data dostępu = 2022-05-08 |opublikowany = maps.be |url = https://maps.be/maps/ms-1}}</ref>.

== Linie kolejowe ==
*
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infobox]]<|endoftext|>{{Album muzyczny infobox
 |rodzaj albumu             = studyjny
 |tytuł                     = C.C.
 |okładka                   = 
 |wykonawca                 = [[C.C.]]
 |wydany                    = [[9 lutego]] [[2018]]
 |nagrywany                 = marzec-maj 2015
 |gatunek                   = [[rock]]
 |długość                   = 41:38
 |wytwórnia                 = [[Island Records]]<ref name=Discogs>{{cytuj stronę|url = https://www.discogs.com/master/1620858-
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek organizacyjnych [[Polityka bezpieczeństwa|polityki bezpieczeństwa]], która umożliwia stosowanie wobec państwa polskiego środków bezpieczeństwa przy współpracy z państwami członkowskimi.

== Historia ==
[[Plik:Polish polar policy.jpg|thumb|upright=0.5|Polska w [[II Rzeczpospolita|II RP]]]]
Polska była pierwszym państwem bezpieczeństwa utworzonym przez [[Polityka agrarna|politykę agrarną]] po [[I wojna światowa|I wojnie światowej]]. Istniały też partie polityczne i
```

### ScratchGPT-300m — Step 32655 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[Poznań]] / [[Poznań]] – [[Toruń]] / [[Toruń]] – [[Wrocław]] / [[Warszawa]] – [[Kraków]]
|-
|bgcolor="F0E682"| '''LXV''' – [[Kozienice]]
| [[Fabryka Cynkow „Kozienice”|Fabryka Cynkow]] – [[Gdynia]] / [[Centrum (Pałac Kultury i Nauki)|Centrum]] – [[Pałac Kultury i Nauki]] – [[Poznań]]/ [[Pałac Kultury i Nauki]] – [[Dąbrowa
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w czasach [[Ziemie Rzeczypospolitej pod zaborami|zaborów]] w gminie Wiszniew, w powiecie święciańskim, w [[Gubernia wileńska|guberni wileńskiej]] [[Imperium Rosyjskie]]go. W 1905 roku miała 115 mieszkańców, 203 dziesięciny<ref>Гошкевич И. И. ''Виленская губернія: Полный списокъ населенныхъ мѣстъ со 
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz
|tytuł=
|premiera=
|premiera=
|premiera=
|reżyseria=
|scenariusz=
|kod produkcji=
|opis=
|kolor linii=
}}
{{Odcinek
|sezon=
|odcinek=7
|tytuł=  Pięć złych snów 
|premiera=
|premiera=
|premiera=
|premiera=
|premiera=
|premiera=
|premiera=
|reżyseria=
|scenariusz=
|kod produkcji=
|opis=
|
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek organizacyjnych [[Straż Graniczna (Polska)|Straży Granicznej]], realizujących zadania w ochronie granicy państwowej.

W strukturach [[Fundusz Służby Granicznej|Funduszu Służby Granicznej]] – 1 października 2002, z dniem 1 stycznia 2003 i 10 kwietnia 2003, w związku złupiały strażnice [[Strażnica WOP Rutka|132 strażnica WOP Rutka]], a drogi od [[Bobrowniki (powiat brzeski)|Bobrownik]] (drogą [[Dro
```

### ScratchGPT-300m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dzielnica [[Warszawa|Warszawy]] położona w południowym [[Miasto|mieście]] [[Warszawa|Warszawy]], w kwartale ulic: [[Ulica Bagienna w Warszawie|Bagiennej]], [[Ulica Towarowa w Warszawie|Towarowej]], [[Ulica Towarowa w Warszawie|Towarowej]], [[Ulica Wolska w Warszawie|Wolskiej]] i [[Ulica Jana Pawła Włodkowica w Warszawie|Włodkowica]].

== Historia ==
Ulica została wytyczona w [[XV wiek]]u jako ulica [[Podskarbi wielki
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w czasach [[Królestwo Prus|państwa pruskiego]] na linii [[Dobra tabularne|taboru kolejowego]]. W okresie [[II Rzeczpospolita|II Rzeczypospolitej]] [[stacja kolejowa]] znajdowała się w [[województwo pomorskie (II Rzeczpospolita)|województwie pomorskim]], w [[powiat słupski|powiecie słupskim]], w [[Prabuty (gmina)|gminie Prabuty]]. Po II wojnie światowej w granicach Prus, na [[Pomorze|Pomorzu]]. Od 1991 w granicach Kaszub<ref>{{Cytuj |tytuł = Kartoteka e
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz
|tytuł=Ogród botaniczny, ogrodnictwo i ogrody 
|opublikowany=www.poznan.pl|url=https://www.poznan.pl/mim/wortals/d/14905/ogrod-botaniczny-ogrod-botaniczny-o-ogrodach-botanicznych.html
|data dostępu=2023-01-27}}</ref>
|
|
|
|-
|2016
|rowspan="3"|'''Ogród Botaniczny, ogrody 
|rowspan="
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek organizacyjnych [[Polityka bezpieczeństwa|polityki bezpieczeństwa]], która umożliwia stosowanie wobec [[Bezpieczeństwo narodowe|bezpieczeństwa narodowego]] w wymiarze bezpiecznym [[Bezpieczeństwo teleinformatyczne|bezpieczeństwa teleinformatycznego]] lub [[Bezpieczeństwo narodowe|bezpieczeństwa narodowego]], a także w inny sposób nawiązywać wzajemnie do [[Służby specjalne|służb specjalnych]] lub [[Służba specjalna|służb specjalnych]].


```

### ScratchGPT-300m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dzielnica [[Warszawa|Warszawy]] położona w południowym [[Miasto|mieście]] [[Warszawa|Warszawy]], w kwartale ulic: [[Ulica Bagienna w Warszawie|Bagiennej]], [[Ulica Towarowa w Warszawie|Towarowej]], [[Ulica Towarowa w Warszawie|Towarowej]], [[Ulica Wolska w Warszawie|Wolskiej]] i [[Ulica Jana Pawła Włodkowica w Warszawie|Włodkowica]].

== Historia ==
Ulica została wytyczona w [[XV wiek]]u jako ulica [[Podskarbi wielki
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w czasach [[Królestwo Prus|państwa pruskiego]] na linii [[Dobra tabularne|taboru kolejowego]]. W okresie [[II Rzeczpospolita|II Rzeczypospolitej]] [[stacja kolejowa]] znajdowała się w [[województwo pomorskie (II Rzeczpospolita)|województwie pomorskim]], w [[powiat słupski|powiecie słupskim]], w [[Prabuty (gmina)|gminie Prabuty]]. Po II wojnie światowej w granicach Prus, na [[Pomorze|Pomorzu]]. Od 1991 w granicach Kaszub<ref>{{Cytuj |tytuł = Kartoteka e
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz
|tytuł=Ogród botaniczny, ogrodnictwo i ogrody 
|opublikowany=www.poznan.pl|url=https://www.poznan.pl/mim/wortals/d/14905/ogrod-botaniczny-ogrod-botaniczny-o-ogrodach-botanicznych.html
|data dostępu=2023-01-27}}</ref>
|
|
|
|-
|2016
|rowspan="3"|'''Ogród Botaniczny, ogrody 
|rowspan="
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek organizacyjnych [[Polityka bezpieczeństwa|polityki bezpieczeństwa]], która umożliwia stosowanie wobec [[Bezpieczeństwo narodowe|bezpieczeństwa narodowego]] w wymiarze bezpiecznym [[Bezpieczeństwo teleinformatyczne|bezpieczeństwa teleinformatycznego]] lub [[Bezpieczeństwo narodowe|bezpieczeństwa narodowego]], a także w inny sposób nawiązywać wzajemnie do [[Służby specjalne|służb specjalnych]] lub [[Służba specjalna|służb specjalnych]].


```

## ScratchGPT-100m — scratch-polish-dollar-1788900395083493729-wiki-100-mixed

Source: wiki-scratch-v1; mixed sampling with filtered Wikipedia lead substrings

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 133.33 minutes; worker: 134.96 minutes; estimated worker compute: $9.3825. Tokens presented: 2,641,494,016, sampled with replacement.

Selected development loss: 1.4957; selected test loss: 1.3662 nats/token. Fresh-process reload matches: True.

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

Factual preference: 8/10. Mean repeated word 4-gram fraction: 0.0045. Stage worker compute estimate: not recorded.

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
| '''Paryż''' – stolica | Francji | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[stacja kolejowa]] w [[Warszawa|Warszawie]], znajdująca się w dzielnicy [[Ursynów]], w [[Warszawa|Warszawie]]. Jest to stacja początkowa [[Warszawska Kolej Dojazdowa|Warszawskiej Kolei Dojazdowej]]. Połączenia z Warszawską Koleją Dojazdową i [[Koleje Mazowieckie|Koleją Mazowiecką]] docierają do trzech miast w Polsce: [[Białystok|Białegostoku]], [[Gdańsk]]a i [[Sopot|Sopotu]]<ref>{{Cytuj stronę|url=http://www.ursyn-op
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto na prawach powiatu]] w [[Województwo małopolskie|województwie małopolskim]], położone na [[Wyżyna Krakowsko-Częstochowska|Wyżynie Krakowsko-Częstochowskiej]], u podnóży [[Beskid Wyspowy|Beskidu Wyspowego]], na [[Wyżyna Częstochowska|Wyżynie Częstochowskiej]]. Siedziba [[Kraków (do 1918)|miasta]], [[miasto królewskie|miasta królewskiego]] [[Kraków|Krakowa]]. Leży nad rzeką [[Mleczna (dopływ Gostyni)|Mleczną]] w rejonie uj
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[miasto na prawach powiatu]] we wschodniej [[Polska|Polsce]], w [[Województwo śląskie|województwie śląskim]], siedziba [[PowiatWisła|powiatu Wisła]] oraz [[Wisła (miasto)|miasta na prawach powiatu]]. Ośrodek przemysłowy oraz kulturalny i naukowy, zlokalizowane na prawym brzegu [[Wisła|Wisły]], na [[Płaskowyż Rybnicki|Płaskowyżu Rybnickim]]. Status [[miasto na prawach powiatu|miasta na prawach powiatu]] uzyskał w [[1990]] roku, jednak od tego czasu miasto
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]] [[Nauki prawne|nauk prawnych]], [[nauczyciel akademicki]] na [[Wydział Prawa i Administracji Uniwersytetu Warszawskiego|Wydziale Prawa i Administracji]] [[Uniwersytet Warszawski|Uniwersytetu Warszawskiego]], specjalista w zakresie [[Prawo cywilne|prawa cywilnego]] i [[Prawo prywatne międzynarodowe|prawa międzynarodowego prywatnego]].

<|endoftext|>'''Łukasz Kuźma<ref name="mp">{{Monitor Polski|2016|1043}}</ref>''' (ur. [[17
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[nagroda muzyczna]] [[Fryderyk (nagroda)|Fryderyka]] przyznawana w [[1997 w muzyce|1997]] roku w kategorii [[Fryderyk BF|Fryderyk dla piosenki roku / jazz]]<ref>{{cytuj stronę |url = https://fryderyki.pl/fryderyk-2001 |tytuł = Fryderyki 2001: nominowani i laureaci |almamater = Honkisz |opublikowany = fryderyki.pl |język = pl |data dostępu = 2012-02-12}}</ref>.

```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[nauka]] o [[Własność|własności]] określonej w ujęciu [[Nauki przyrodnicze|nauk przyrodniczych]] (nauka o właściwościach [[Model fizyczny|modeli fizycznych]]), w której z [[Ziemia|Ziemi]] wykonuje [[Strategia militarna|strategię militarną]] ([[Język angielski|ang.]] ''military military militaria'') i odpowiada jej [[Stopień wojskowy|stopniu]] (ang. ''multi-military
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym krokiem jest odrzucenie przez [[Max Erlbaum|Maxa Erlbauma]] wszelkich praw do wyrażenia [[Słowo Boże|Słowa Bożego]]. W wyniku tego werbunku zniewolony został w [[1887]] r. [[Adolf Hitler]]. Zanim jednak wyprawił się na [[Ocean Spokojny|amerykańskie wody przybrzeżne]] [[Wilhelm Hohenzollern (1790–1868)|Wilhelmowi]] i [[Wilhel
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 od jubileuszu XX wieku}}
'''XXI Skład PPS''' – polska organizacja polityczna z [[Okręg wyborczy nr 4 do Sejmu Rzeczypospolitej Polskiej (1991–1993)|okręgu zachodniego]] działająca w latach 1992–2001.

== Historia ==

Założona w listopadzie 1992 przez [[Władysław Sikorski|Władysława Sikorskiego]] [[Parlamentarna lista wybranych partii I kadencji|zrzeszała większość spośród działaczy tej partii]] (w tym prezydenta [[Leszek Miller|Leszka Millera]]),
```

### ScratchGPT-100m — Development-selected

Factual preference: 8/10. Mean repeated word 4-gram fraction: 0.0045. Stage worker compute estimate: not recorded.

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
| '''Paryż''' – stolica | Francji | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[stacja kolejowa]] w [[Warszawa|Warszawie]], znajdująca się w dzielnicy [[Ursynów]], w [[Warszawa|Warszawie]]. Jest to stacja początkowa [[Warszawska Kolej Dojazdowa|Warszawskiej Kolei Dojazdowej]]. Połączenia z Warszawską Koleją Dojazdową i [[Koleje Mazowieckie|Koleją Mazowiecką]] docierają do trzech miast w Polsce: [[Białystok|Białegostoku]], [[Gdańsk]]a i [[Sopot|Sopotu]]<ref>{{Cytuj stronę|url=http://www.ursyn-op
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto na prawach powiatu]] w [[Województwo małopolskie|województwie małopolskim]], położone na [[Wyżyna Krakowsko-Częstochowska|Wyżynie Krakowsko-Częstochowskiej]], u podnóży [[Beskid Wyspowy|Beskidu Wyspowego]], na [[Wyżyna Częstochowska|Wyżynie Częstochowskiej]]. Siedziba [[Kraków (do 1918)|miasta]], [[miasto królewskie|miasta królewskiego]] [[Kraków|Krakowa]]. Leży nad rzeką [[Mleczna (dopływ Gostyni)|Mleczną]] w rejonie uj
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[miasto na prawach powiatu]] we wschodniej [[Polska|Polsce]], w [[Województwo śląskie|województwie śląskim]], siedziba [[PowiatWisła|powiatu Wisła]] oraz [[Wisła (miasto)|miasta na prawach powiatu]]. Ośrodek przemysłowy oraz kulturalny i naukowy, zlokalizowane na prawym brzegu [[Wisła|Wisły]], na [[Płaskowyż Rybnicki|Płaskowyżu Rybnickim]]. Status [[miasto na prawach powiatu|miasta na prawach powiatu]] uzyskał w [[1990]] roku, jednak od tego czasu miasto
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]] [[Nauki prawne|nauk prawnych]], [[nauczyciel akademicki]] na [[Wydział Prawa i Administracji Uniwersytetu Warszawskiego|Wydziale Prawa i Administracji]] [[Uniwersytet Warszawski|Uniwersytetu Warszawskiego]], specjalista w zakresie [[Prawo cywilne|prawa cywilnego]] i [[Prawo prywatne międzynarodowe|prawa międzynarodowego prywatnego]].

<|endoftext|>'''Łukasz Kuźma<ref name="mp">{{Monitor Polski|2016|1043}}</ref>''' (ur. [[17
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[nagroda muzyczna]] [[Fryderyk (nagroda)|Fryderyka]] przyznawana w [[1997 w muzyce|1997]] roku w kategorii [[Fryderyk BF|Fryderyk dla piosenki roku / jazz]]<ref>{{cytuj stronę |url = https://fryderyki.pl/fryderyk-2001 |tytuł = Fryderyki 2001: nominowani i laureaci |almamater = Honkisz |opublikowany = fryderyki.pl |język = pl |data dostępu = 2012-02-12}}</ref>.

```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[nauka]] o [[Własność|własności]] określonej w ujęciu [[Nauki przyrodnicze|nauk przyrodniczych]] (nauka o właściwościach [[Model fizyczny|modeli fizycznych]]), w której z [[Ziemia|Ziemi]] wykonuje [[Strategia militarna|strategię militarną]] ([[Język angielski|ang.]] ''military military militaria'') i odpowiada jej [[Stopień wojskowy|stopniu]] (ang. ''multi-military
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym krokiem jest odrzucenie przez [[Max Erlbaum|Maxa Erlbauma]] wszelkich praw do wyrażenia [[Słowo Boże|Słowa Bożego]]. W wyniku tego werbunku zniewolony został w [[1887]] r. [[Adolf Hitler]]. Zanim jednak wyprawił się na [[Ocean Spokojny|amerykańskie wody przybrzeżne]] [[Wilhelm Hohenzollern (1790–1868)|Wilhelmowi]] i [[Wilhel
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 od jubileuszu XX wieku}}
'''XXI Skład PPS''' – polska organizacja polityczna z [[Okręg wyborczy nr 4 do Sejmu Rzeczypospolitej Polskiej (1991–1993)|okręgu zachodniego]] działająca w latach 1992–2001.

== Historia ==

Założona w listopadzie 1992 przez [[Władysław Sikorski|Władysława Sikorskiego]] [[Parlamentarna lista wybranych partii I kadencji|zrzeszała większość spośród działaczy tej partii]] (w tym prezydenta [[Leszek Miller|Leszka Millera]]),
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

### ScratchGPT-100m — Step 6162 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref><ref name
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. na miejscu dawnego cmentarza w miejscowości [[Choczała]]. Jej nazwa nawiązywała do grodziska Choczały (starego cmentarza). Obecnie nie ma charakteru turystycznego, która jest nazywana "Złotem Pamięci".

== Sport ==
W Złotym Pamięci pochowany został [[Aleksander Kazimierz Rostocki|Aleksander Kazimierz]] i [[Dariusz Podhoroś|Dariusz Podhoroś]], który w wieku 15 lat wstąpił do drużyny z bogatą ludźmi
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Q1501013708}}
* [[Louis Pierre Guiquier]]
* [[Louis Pierre Guiquier]]
* [[Louis Pierre Guiquier]]

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
{{Commonscat}}
{{Francja U-Boot}}

[[Kategoria:City of London]]
[[Kategoria:City of London]]
[[Kategoria:City of London]]
[[Kategoria:City of London]]
[[Kategoria:City
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

### ScratchGPT-100m — Step 12258 / original prompts

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
W roku [[1960]] miejscowość była pod nazwą ''Grom'', a w roku [[1971]] wchodziła w skład [[Szkoła podstawowa|szkoły podstawowej]]. W roku [[1980]] zmieniono nazwę na ''Stary Grom''. W roku [[2004]] miała już tylko trzynastą.

== Zobacz też ==
* [[Dolina]]

== Przypisy ==
{{Przypisy}}

{{Gmina Grom}}

[[Kategoria:Grom (gmina)]]<|endoftext|>{{Dzielnica polskiego miasta infobox
 |nazwa                     = Grom
 |inna nazwa                = 
 |herb miasta               =
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Slammiversary.png|Slammiversary.org.
}}
'''[[Wielka Brytania|Wielką Brytanię]] na [[Zimowe Igrzyska Olimpijskie 1998|Zimowych Igrzyskach Olimpijskich 1998]]''' reprezentowało 109 zawodników: 140 mężczyzn i 12 kobiet. Był to dwunasty start reprezentacji Wielkiej Brytanii na [[Zimowe igrzyska olimpijskie|zimowych igrzyskach olimpijskich]].

<|endoftext|>'''Grzegorz Janusz''' (ur. [[14 września]] [[1976]] w [[Szczecin]]ie) – [[Polska|polski]] [[polityk]], absolwent [[Uniwersytet Ekonomiczny w Poznaniu|Uniwersytetu
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

### ScratchGPT-100m — Step 18148 / original prompts

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
Po udanych relacjach na temat rozwoju miasta i kultury w mieście, w latach 80. XX wieku, na skutek ograbień i wysiłków z banknotów i przestrzegania prawa, mieszkańcy zarządzali głównie na obszarach wiejskich. Przyczynił się do wymocowania [[Język kaszubski|języka kaszubskiego]] i zaczął intensywnie rozwijać politykę nadzorczyń.

W latach 90. XX wieku miasto liczyło w sumie 78 068 osób, a w latach
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 warsztat}}
{{AS-węzeł|ok|WB|2|[[Kozłowa Wieś]]}}
{{AS-węzeł|ok|WB|3|[[Wierzchowo]]}}
{{AS-węzeł|ok|WB|4|[[Kozłowa Wieś]]}}
{{AS-węzeł|ok|WB|8|[[Kozłowa Wieś]]}}
{{AS-węzeł|ok|WB|17|[[Kozłów]]}}
{{AS-węzeł|ok|WB|10|[[Kozłów]]}}
{{AS-
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

### ScratchGPT-100m — Step 24160 / original prompts

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
{| class="wikitable"
! width=5%|Konkurencja
! width=5%|Zwycięzca
! width=10%|Remis
! width=15%|Zwycięzca
|-
|[[Mistrzostwa Ameryki Północnej, Środkowej i Karaibów 1995|1995]] <small>(6)</small>
|{{flaga|CHL}} [[Alberto Cárdenas]]
|{{flaga|DOM}} [[Orelvé Cárdenas]]
|{{flaga|BRA}} [[Cabrício Ferreira]]
|-
|[[Mistrzostwa Ameryki Północnej, Środkowej
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a
 |'''Data wprowadzenia''':<br>
'''Players:'''<br>
'''Reżyseria:''' [[Adam Clay]]
 |scenariusz       = [[Clay Bell]], [[Adam Clay]]
 |opis            =
 |kolor linii     = 006633
 |opis            =
}}
{{odcinek
 |numer         = 10
 |odcinek         = 7
 |tytuł           = Eye Of Me
 |źródło          =<ref name="FOGREN-s96" />
 |dopisek         =
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

### ScratchGPT-100m — Step 30252 / original prompts

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
Początki zespołu sięgają 1863 roku, kiedy zadebiutowały jako [[Kronika|kronikarysta]] ''Wędrych'' w ''Ogródku z Książnicy'' [[Henryk Foltyn|Henryka Foltyna]], który wkrótce przyszedł na świat. W 1868 roku utworzono [[Liga Młodych Pisarzy Polskich|Ligę Młodych Pisarzy Polskich]] w ramach [[Liga Pisarzy Polskich|Ligi Pisarzy Polskich]]<ref name=":0" />. W tym samym roku po raz pierwszy zorganizowano grupę literacką ''
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Oznaczenia Infobox|kod=P}}
{{Cytuj książkę | tytuł = Ranglisten des kaiserlichen und königlichen Heeres | url = https://library.hungaricana.hu/hu/view/RanglistenHung_1893/?pg=0&layout=blog&sort=%2Ctyppoint2 | miejsce = Wien | wydawca = K. Königlich Wien | rok = 1893 | strony = 117 | url = https://books.google.com/
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 polski [[film sensacyjny]] w reżyserii [[Michał Majka|Michała Majki]], który miał premierę 22 czerwca 2008 roku na antenie [[Polskie Radio Program III|Programu Trzeciego Polskiego Radia]]. Fabuła opowiada o losach grupy polskiej działającej w Polsce w latach 1864–1918. Bohaterem filmu jest [[Michał Bajor]], absolwent [[Państwowe Gimnazjum im. M. Kopernika we Włocławku|Państwowego Gimnazjum żeńskiego we Włocławku (drugi gimnazjum
```

### ScratchGPT-100m — Step 36242 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dzielnica [[Praga-Południe|Pragi-Południe]] położona w południowej części miasta. Jest to miejscowość o charakterze miejskim, a jej granice wyznaczają ulice: [[Ulica Dworcowa w Warszawie|Dworcowa]] i [[Ulica Wola Towarowa w Warszawie|Wolna]].

<|endoftext|>'''Lesław Piotr Rembek''' (ur. [[28 marca]] [[1957]] w [[Zawiercie|Zawierciu]]) – polski [[działacz społeczny]] i [[Samorząd terytorialny w Polsce|sam
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku [[Związek Socjalistycznych Republik Radzieckich|Związku Radzieckiego]] w czerwcu 1950 r. teren gminy Suchej podeszłoro, włączając do sołectwa [[Radzewo]] [[Będargowo (gmina)|Będargowo]] (obecnie nie wchodzącej w skład gminy) w [[Powiat piski|powiecie piskim]] [[Województwo kieleckie (1945–1975)|województwa kieleckiego]]. W czerwcu 1952 r. część wsi Suchej została włączona do [[Będargowo (gmina)|gminy Będargowo]].
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 nagłówek.aspx?id=329423}}
{{AS-węzeł|ok|WB||{{AS-droga|W|757}}|W|731}} {{AS-droga|W|757}}}}
{{AS-węzeł|ok|WB||[[Triest|Triest-Ai]]|W|744}}
{{AS-węzeł|ok|WB||[[Brzeźnica (powiat nowotomyski)|Brzeźnica]]|W|744}}
{{AS-węzeł|ok|WB
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[polska]] [[uczelnia]] w [[Bieszczady|Bieszczadach]] powstała w kwietniu 1945 jako '''Politechnika''' (PF) [[Politechnika Śląska|Politechniki Śląskiej]]. Była najstarsza z polskich uczelni akademickich w [[Historia Polski (1918–1939)|dwudziestoleciu międzywojennym]] w [[Województwo lwowskie|województwie lwowskim]] oraz najstarszym uniwersytetem [[Politechnika Śląska|Śląskiej Politechniki]] w [[II Rzeczpospolita|II Rzeczypospolitej]].

<|endoftext|>'''Kościół świętej Anny''' – [[kościół łaciński|
```

### ScratchGPT-100m — Step 42305 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[stacja kolejowa]] [[Polskie Koleje Państwowe|Polskich Kolei Państwowych]] obsługiwana przez [[Koleje Mazowieckie]].

Stacja jest częścią systemu [[Strefa piesza|deptak]] warszawskiej [[Miejskie Przedsiębiorstwo Komunikacyjne – Warszawa|MPK]], obsługującego przewozy pasażerskie i towarowe w [[Warszawa|Warszawie]]. 

Poziom stacji jest częścią ciągu transportowego [[Linia kolejowa nr 29|linii kolejowej nr 29]] W-wa Warszawa oraz [[Linia Kołbaskowo – Most
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku realiów (1872–1874) w wyniku [[Rozejm w Compiègne (1874)|rozejmu w Compiègne]] zwołanego [[Wojna francusko-pruska|wojną francusko-pruską]] (1874–1875), utworzono [[Armée Nationale|pokarmy o ograniczonych interesach]]<ref group="uwaga">Wyjątkowo jest to [[Armée Nationale|stacje ziemskie]] w [[Sarcelles]].</ref>.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|2011|8|26. [[Bill Coventry]] wyprowadził [[Mark Boyman]]<ref name="AB22">{{cytuj stronę|url=https://f1wm.pl/news/27218|tytuł=Boyman po raz pierwszy w karierze w Formule 1|data=2011-06-06|opublikowany=f1wm.pl|język=pl|data dostępu=2011-06-06}}</ref>.

Dwunastoletni kontrakt Boymana rozegrał dla agencji [[Fédération Internationale de
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[nadawca]] [[radio]]wy [[Telewizja|telewizyjny]] w [[Kraków|Krakowie]] w [[Historia Polski (1918–1939)|okresie międzywojennym]]<ref name=":0">{{Cytuj |autor = Adam Marszałek |tytuł = Poradnik orto i reportaż o tematyce powiązanych z krakowem w latach 1911–1939 |czasopismo = Ale Historia |data = 2023 |data dostępu = 2026-05-16 |url = https://www.alegiada.pl/a/poradnik-orto-
```

### ScratchGPT-100m — Step 48418 / original prompts

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
Po ucieczce z Polski (1872–1895) w wyniku [[Rewolucja listopadowa|rewolucji roku 1830]] w [[Królestwo Polskie (kongresowe)|Królestwie Polskim]], dołączyła do partii [[Związek Patriotów Polskich]], by w celu odzyskania [[Polska|Polski]] przed [[Austro-Węgry|Austro-Węgrami]] i [[Imperium Rosyjskie]]m oraz [[Rosja|Rosją]]. Sojusznik [[Iwan Turczyk|Iwana Turczyka]]<ref name=":0" />. Początkowo był
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Oznaczenia: notojad (bez obramowania) - superfauna - broń: 0,9 m, masa: 0,9 m, masa: 0,6 kg, masa: 0,5 kg, masa: 0,7 kg, masa: 0,8 kg, masa: 0,6 kg, masa: 0,6 kg, masa: 0,8 kg, masa: 0,6 kg, masa: 0,9 kg, masa: 0,9 kg, masa: 0,6 kg, m
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

### ScratchGPT-100m — Step 54473 / original prompts

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
Początkowo, w latach 1868–1872, za rządów [[Ignacy Rzewuski|Ignacego Rzewuskiego]], w 1872 roku powołano do życia zarząd nad ośrodkiem prawosławnym<ref name="chram">[http://www.swti.pl/index.php?m=11&id=207 Informacje o parafii na stronie Kościoła]</ref>. W 1873 roku przystąpiono do budowy i rozbiórki obiektu<ref name="chram"/>. W 1875 roku wybudowano nową<ref name="chram"/>. Budynek został zniszcz
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Organizatorzy}}
'''I liga polska w piłce nożnej (1986/1987)''' – 44. edycja [[Ekstraklasa w piłce nożnej|najwyższych w hierarchii rozgrywek ligowych]] [[piłka nożna w Polsce|polskiej klubowej piłki nożnej]], która uzyskała automatyczny awans do [[Ekstraklasa w piłce nożnej (1987/1988)|Ekstraklasy]]. Rozgrywki zostały [[Mistrzostwa Polski w piłce nożnej (1986)|jednonaście najlepszych klubów piłkarskich w historii polskiej piłki nożnej]].

== I liga polska w sezonie 1986/1987 ==
=== Tabela ===
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

### ScratchGPT-100m — Step 60564 / original prompts

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
Początkowo firmę z siedzibą w [[Fryburg (miasto)|Fryburgu]], przekształcono w spółkę [[joint venture]] z siedzibą w [[Gorlash]] i przemianowano na Masse SA. W roku [[1991]] spółka zmieniła nazwę na [[Marines]] SA. W latach 90. mariner został przemianowany na MASZSE. W [[2001]] roku przedsiębiorstwo zostało przekształcone w Spółkę Akcyjną (Pomorski SA). Od [[2002]] r. wchodzi jako [[spółka
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a]]</nowiki><ref>{{Cytuj |autor =  |tytuł = O PARAFIE MICHAŁA. POSTĄTKI SOKRACJI NA ZIEMI I TYMNEJ W PRZEMCIENACIE. |data =  |data dostępu = 2019-01-23 |opublikowany = www.znadwiliiwilno.lt |url = http://www.znadwiliiwilno.lt/wp-content/uploads/2019/01/Z
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

### ScratchGPT-100m — Step 66641 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[stacja węzłowa]] w [[Warszawa|Warszawie]], znajdująca się na terenie [[Podział administracyjny Warszawy|dzielnicy]] [[Białołęka]] oraz częściowo [[Zakręt (powiat otwocki)|Zakrętu]]. Stalowa konstrukcja stacji, zestaw stacji i przystanku wysokich prędkości, przesuwa się w dół linii, a także przywraca na długość linii [[Prabuty]] – [[Brodno (stacja kolejowa)|Brodno]].

<|endoftext|>'''Alicja Drozdowska''', właściwie Alicja Drozdowska<ref
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początki osadnictwa w Albanii sięgają czasów [[starożytność|późnoegipskich]]. Do roku 780 n.e. w Albanii wzniesiono pierwszą [[Tirana|tirinę]] z [[żargon]]u, z których największy znany wytwarzał [[Tirana Nardus|Ilir]], a zarazem pierwszą osadzoną w miastach [[Durrës|Durrës]] i [[Korcza|Korczy]].

Trójnawowy,
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Organizatorzy zawodów}}
* [https://www.firma.org/ Strona oficjalna FIRL]

{{Firma z sektorem sportowym}}

[[Kategoria:Firma z sektorem sportowym| ]]
[[Kategoria:Organizacje sportowe]]
[[Kategoria:Lotnictwo]]
[[Kategoria:Transport w Niemczech]]
[[Kategoria:Organizacje paramilitarne w Europie]]
[[Kategoria:Stowarzyszenia w Niemczech]]
[[Kategoria:Kultura w Niemczech]]<|endoftext|>#REDIRECT
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu ich zniesienia z dniem 1 stycznia 1973<ref>{{
```

### ScratchGPT-100m — Step 72656 / original prompts

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
Początki osadnictwa w rejonie wsi sięgają roku 1000 – 1024, kiedy to miasto stało się ośrodkiem osadnictwa i pasterstwa. Pierwsze wzmianki o miejscowości pochodzą z 1789 roku<ref name="zab">{{Cytuj stronę | url = https://web.archive.org/web/20111203062031/http://zabno.pl/images/file/raport_o_zabno_zabno.pdf | tytuł = Raport o zasobach Wędryni. Raport o stanie wsi | nazwisko
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a
|ZŁOCKIET
|[[Plik:POL COA Prus-Niesiecki.svg|centruj|x25px]]
|ZŁOCKIET
|colspan="2" |
|-
|colspan="2"|
|colspan="2"|
|colspan="2"|
|colspan="2"|
|colspan="2"|
|[[Plik:POL COA Prus-Niesiecki.svg|centruj|x25px]]
|ZŁOCKIET
|colspan="2"
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

### ScratchGPT-100m — Step 78731 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[miasto]] w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat warszawski zachodni|powiecie warszawskim zachodnim]], siedziba [[Warszawa (gmina)|gminy miejsko-wiejskiej Warszawa]]. Leży na [[Wysoczyzna Żelechowska|Wysoczyźnie Żelechowskiej]], nad [[Kaziorka (dopływ Zielawy)|Kaziorką]], na pograniczu [[Puszcza Kampinoska|Puszczy Kampinoskiej]] i [[Puszcza Biała|Puszczy Białej]]

Miasto [[aglomeracja warsza
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początki osadnictwa w Alentej na północy kontynentu sięgają czasów średniowiecza, kiedy na skutek działalności pasterskiej, w wyniku czego powstały pierwsze ośrodki osadnictwa [[Europa|europejskiego]], które stały się ważnym ośrodkiem gospodarczym Alentej.

Alentej odegrał dużą rolę w rozwoju [[Dalmacja|Dalmacji]]. W czasach, gdy w Alentej znaleziono wiele wróblowych, to on w połowie XV wieku stał się ważnym ośrodkiem dy
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a
|ZŁOCKIE SPOŁECZNIE
|SĘPOWA
|A
|ZŁOCKIE SPOŁECZNE
|X
|A
|M
|<ref name=":18">{{Cytuj |tytuł = ZŁOCKIE SPOŁECZNE |data dostępu = 2022-07-02 |opublikowany = www.zlotkespoleczna.pl |url = https://www.zlotkespoleczna.pl/nasze-
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 polski [[film sensacyjny]] z [[1978 w filmie|1978]] roku, w reżyserii [[Janusz Majewski|Janusza Majewskiego]], zrealizowany na podstawie opowiadania [[Stanisław Domański|Stanisława Domańskiego]] pod tytułem [[Polska (opowiadanie)|''Polska'']].

<|endoftext|>'''Maciej Kościelniak''' (ur. [[19 listopada]] [[1979]] w [[Toruń|Toruniu]]) – polski [[Piłka nożna|piłkarz]], występujący na pozycji pomocnika lub napastnika. 

W latach 2003–2013 [[
```

### ScratchGPT-100m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[miasto]] w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat warszawski zachodni|powiecie warszawskim zachodnim]], siedziba [[Warszawa (gmina)|gminy miejsko-wiejskiej Warszawa]]. Leży na [[Bolimowski Park Krajobrazowy|Bolimowskim Parku Krajobrazowym]]. Według danych [[Główny Urząd Statystyczny|GUS]] z 31 grudnia 2025 r. miasto miało 9&nbsp;404 mieszkańców<ref name="gus" />.

W latach 1867–1975 i ponownie od 1973 r. stolica [[Województwo warszawskie (1975–1998)|województwa
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początki osadnictwa w Alentej na terenach współczesnej Portugalii sięgają pierwszej połowy XVII w., kiedy to pojawiły się pierwsze w Europie złoża soli [[Tlenek wapnia|wapnia]] oraz [[Sól sodowa|soli sodowej]]{{r|Domine2009}}. Nazwę ''Alentej'' nadała Rio de Oliveira w 1851 r. [[Fernando Ortega]], który w 1872 r. utworzył w Alentej osadzone w Lago
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a
|Zgłośnięcie
|Napastnik
|
|-
|align=left| Zmroczek
|Napastnik
|
|-
|}

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
* [https://www.nba.com/player/1609686 Profil na NBA.com] {{lang|en}}
* [https://www.basketball-reference.com/players/m/molnema01.html Statystyki na basketball-reference.com] {{lang|
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[nadawca]] działający w [[Polska|Polsce]] z siedzibą w [[Warszawa|Warszawie]], która jest [[Organizacja pożytku publicznego|organizacją pożytku publicznego]] i w [[Sejm Rzeczypospolitej Polskiej|Sejmie]].

Platforma została założona 1 stycznia 2002, początkowo działała pod nazwą '''Polska Spółdzielnia Pracy – Prasa Polska'''. Od 1 stycznia 2009, po połączeniu z [[Polska Firma Prasowa Biegłego|Polską Firmą Prasową Biegłego]], powołana została przez [[S
```

### ScratchGPT-100m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[miasto]] w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat warszawski zachodni|powiecie warszawskim zachodnim]], siedziba [[Warszawa (gmina)|gminy miejsko-wiejskiej Warszawa]]. Leży na [[Bolimowski Park Krajobrazowy|Bolimowskim Parku Krajobrazowym]]. Według danych [[Główny Urząd Statystyczny|GUS]] z 31 grudnia 2025 r. miasto miało 9&nbsp;404 mieszkańców<ref name="gus" />.

W latach 1867–1975 i ponownie od 1973 r. stolica [[Województwo warszawskie (1975–1998)|województwa
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początki osadnictwa w Alentej na terenach współczesnej Portugalii sięgają pierwszej połowy XVII w., kiedy to pojawiły się pierwsze w Europie złoża soli [[Tlenek wapnia|wapnia]] oraz [[Sól sodowa|soli sodowej]]{{r|Domine2009}}. Nazwę ''Alentej'' nadała Rio de Oliveira w 1851 r. [[Fernando Ortega]], który w 1872 r. utworzył w Alentej osadzone w Lago
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a
|Zgłośnięcie
|Napastnik
|
|-
|align=left| Zmroczek
|Napastnik
|
|-
|}

== Przypisy ==
{{Przypisy}}

== Linki zewnętrzne ==
* [https://www.nba.com/player/1609686 Profil na NBA.com] {{lang|en}}
* [https://www.basketball-reference.com/players/m/molnema01.html Statystyki na basketball-reference.com] {{lang|
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[nadawca]] działający w [[Polska|Polsce]] z siedzibą w [[Warszawa|Warszawie]], która jest [[Organizacja pożytku publicznego|organizacją pożytku publicznego]] i w [[Sejm Rzeczypospolitej Polskiej|Sejmie]].

Platforma została założona 1 stycznia 2002, początkowo działała pod nazwą '''Polska Spółdzielnia Pracy – Prasa Polska'''. Od 1 stycznia 2009, po połączeniu z [[Polska Firma Prasowa Biegłego|Polską Firmą Prasową Biegłego]], powołana została przez [[S
```

## ScratchGPT-100m — scratch-polish-dollar-1788900395083493729-wl-100

Source: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 133.33 minutes; worker: 134.84 minutes; estimated worker compute: $9.3743. Tokens presented: 2,677,145,600, sampled with replacement.

Selected development loss: 2.7653; selected test loss: 2.7421 nats/token. Fresh-process reload matches: True.

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
 co nam zamyślasz uczynić.

— Dołożę szczap dużo i zaraz trzaski skończą. Ale nie zawracaj mi głowy!

To powiedziawszy, pdel czym prędzej wlazł do olster, aby się pozbyć tortu ślinicznego.

Słońce podniosło się nad nim, ale cienie nawet w tej wodzie drzemiące nie ukazywały się i nie napełniały. Pulsy brzuch
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, gdy wszyscy odwróceni byli od niego.

— Cóż to znowu? — zapytał, zatrzymując się nagle na korytarzu.

— To, że te drobne, różowe szczegóły coraz bardziej mnie zaintrygowały — odparł starzec z przeciągłym akcentem.

— To, co wam powiem, stanie się niejako odpowiedzią na to pytanie — powiedział młody człowiek, po czym
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zgasło, a promień słońca zgasnął.

Pieśń rozbrzmiała:

— Niech się spełni szczęście!

Potem umilkło wszystko.

Rozdział XII

Różne wyjątki opowiadają o życiu ludzkim. Opowiadania o nim zawsze brzmiały pocieszająco, nigdy przedtem nie słyszano go tak martwym. Wypadki podobne zdarzały się częściej, kiedy na naszych
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, wyciągano sznury z bawełny i rozpytywaliśmy, jak się wam powodzi. Zgodziliśmy się przy tym, żeby zrobić beczkę z wodą, bo w przypadku gdy woda gwałtownie bije, woda się nieraz przez ryby przeciska, a czasem, prędzej czy później, byle tylko szła stalej.

Zaczynaliśmy się bacznie spierać i nieraz głupstwo nasuniękowane, jakieś nieopatrznie zanie
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w nim niespokojną duszę.

Biedny chłopiec nie miał odwagi spojrzeć na nią i nie czuł się w anirysku na myśl, że taka, jaką musiał patrzeć Otto, była jego kochanką.

— Niech przyjdzie, on wyzdrowieje — mówiła żona miejscowego lekarza i z niepokojem śledziła jego ruchy.

Nikt nie zważał na nią. Majaczy
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
, że ktoś nadchodzi.

— Niech pani wraca! — krzyknęła.

— Nie… nie… nie… — odparła Aniela. — Przecież to niemożliwe, by ktokolwiek z nas tu przybywał.

Stasiek Lipa, który stał przy stole, przysłuchiwał się temu, co mówiła wreszcie Aniela. W jego głosie ujawniło się zdumienie. Dał jej znak, by się u
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, a kobieta posłuszna, wnet z górą się urodzi. Mąż się też, jak stoi, tak i niedługo z żywota wyjdzie. Gdy go zaś dziadek nadobny, wnuki rozmiłowane, w domu swym zaniesie, dobrze musi wiedzieć, o co mu wnet potrzeba będzie. Otóż, jak to mówią, a każda niewiasta z chłopcem mieszka, aż się będzie chciał domyślać, co by tu nań czynić należa
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to łatwo zmienia się czas na dzień, ilekroć się otwieram.

Wciąż coś zmienia mnie, coś wskrzesza, przytłacza. To znów niepokój, niepewność, niezmierzone złudzenie.

Mówisz, że jesteś morze, uciekające jak wiatr od morza.

Wstaję, przyciskam się mocniej do ciebie, wstaję, idę do ciebie, oddaję się niepodzielnie.
```

### ScratchGPT-100m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: not recorded.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co na to poradzić.

— Ale to dopiero wczoraj… Poszedł już do kancelarii, a na drugi dzień i tak samo pytał, kiedy zaczęło to samo.

— Trudno! — mruknął Czertwan, nie chcąc słyszeć wrażenia, jakie na nim sprawiło powstrzymanie się z wybuchem mowy. — To moja sprawa.

— Coś pilnego! — mruknął stary.

—
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, gdy wtem z nagłym błyskiem w oku, spostrzegł szaty chudego, w długą szatę, zarzucone na ramiona na kiju, i natychmiast usiadłszy na wierzchu kanapy, splunął w tył i zawołał:

— Dalibóg, przebóg, drogi chłopcze! co za szatan! Jak on chce mnie słuchać i słyszeć!

Lecz zanim go zechciał poca
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zgasł zupełnie jak lampka.

Pan Carrisford odezwał się cichym i spokojnym głosem:

— O tym właśnie idzie.

— Ale panie! — jęknęła, zrywając się z łóżka i wyciągając przed siebie ramiona.

Twarz jej leżała na biurku w fałdach peraty, na której leżała gruba paka, leżąca na biurku, a pokrywka, którą byłoby nagroma
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, wyciągnął szyję, chwycił buławę i stanął na szczycie jednej skały. Gdy sterował na tylnej krawędzi olbrzymiego, buława pękła mu z pewnością na głowie i całe ciało rozlękło się, jak gdyby skupiało się w sobie, by uchronić go przed nowym ciosem. Wiatr nie sprzyjał i, uspokoiwszy się nieco, wracał znowu do siebie.

Garstka mart
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w nim niespokojne oczy, a na dnie duszy zawiódł się i nie wiedząc co począć, po kilku dniach rzucił się na łóżko, zasnął, a nic nie odpowiedział, dopiero gdy zaledwie zdążyła zasnąć, wyszedł na dwór.

„Nie, nie ja! — myślał, na palcach przebywając drogę do lasu, i tak się przechadzał, szukając czegoś, co by mu znikło
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
:

— Muszę odejść, bo ja się spóźnię.

Zadzwoniła.

— Niech pani wejdzie! — zawołał z daleka.

— Uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, wśród krzewów i drzew, wznosiły się w górę małe, czarne cienie, jakby wpatrzone w ziemię, i nie było żadnego głosu, żadnego dźwięku…

Zamilkłszy w ciszy i spokoju, zerwały się znowu, a wnet zaleciała wilgoć i zajaśniała jakby światłością…

„Oj! jaka głupia!” — pomyślał, siedząc na ławce, z
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak bardzo mnie trapiły te mąki i zabobony.

Zdawało mi się, że coś usłyszałem, ale nie rozumiałem, jak to było.

Wiem tylko, że w tej chwili, nie mogąc się oderwać od tego, co to być może, czułem się tak upokorzony wobec losu, jaki mnie czeka, że będzie mnie mógł oszukać w myśli, iż mogę się od niego oddać. I coś takiego
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

### ScratchGPT-100m — Step 6199 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówi, o co mi chodzi, i żebym się bał was, pojechał sobie, rozmawiając z wami, zaraz tu przyszedł.

— Pewnie — rzekł do Kmity, — że mnie tam was obchodzą mężowie, z których jeden jest, bo tu jestem, ale tego nie widać.

— Co?

— Tego nie wiem. Ojciec mój wie, że ja nie wiem, ja nie wiem, ale taki rozum
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak i ja, i nie widziałem go tak pięknie, jak była moja.

Muszę tu przypatrzeć się, jak to jest zabawna i miła, i spokojna. Jeżeli tak jest, to jest bardzo miła i przystojna. Nie wiem, jak się nazywa, ale widzę, że nie bardzo jest do mnie przychylniejsza, jak przed wszystkimi, nawet niż my wszyscy.

I wiem, że taki jestem niezdolny do żadnych wymówek
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, co tak dobrze zrobiły, że obaj, zbliżywszy się do nich, wesoło wkroczyli, piastujący im kwaterę i towarzysza Sulisława, których im nigdy nie pokazali.

Siedzieli wszyscy na stopniach z rozpostartemi skrzydłami z białą chorągwią na ramionach — i stali nie mogąc ich nawet uwieść, nie śmiejąc ich uszczypnąć, wyszli, szukając jakiegoś sp
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym znajduje się Diabeł Morski, z czego wywnioskować można, jak to jest do rzeki morskiej.

Ale przypominam sobie, że w nocy podążyłem do miasta, choć wciąż nie spałem. Wprawdzie mam w kieszeni wielki talerz koralowy, ale na to jestem gotów, żeby się nie rozpętać, bo jestem złodziejem. Nie masz pojęcia, jak to się stało. Idź, powracaj.


```

### ScratchGPT-100m — Step 12307 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak dużo o tym mówić — odparł Léger.

— Więc dobrze, dobrze, dobrze — odparł pan de Charlus z niejakim uśmiechem, który się zdradzał, kiedy ktoś zgaszał zwykłe swoje szorstkie słowa — przyznaję, ale na próżno.

— Czy to prawda, że mówiono ci o mnie? — wykrzyknął Filip.

— Co prawda — odrzek
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 cacanki, biało-lukiery i kolorowe kwiaty, które z kwiatów pachnących otaczał, i trzon złoty, błyszczący od pukli, i wszystko, co tylko złote życie wydawało się niepiękne, i wszystko, co żyło, było wdzięczne, doskonałe.

— Dlaczego pan to robisz? — zapytał.

— Bo mi się tak podoba.

— To niech pan będzie
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zacząłem mówić:

— Któż jest ta moja opiekunka?

— Ta? Maryla! — zawołałem. — Któż by to ją chciał słuchać?

— Ojciec mój, który w niewoli uczył się w szkole Trzech Króli, przywiózł ze sobą klucznicy do domu, potem kuchni, a potem do izdebki.

— Co pani sądzi —
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie! — krzyczał, rzucając się na fale. — Ja do mnie! Ja do mamusi! Ja nie winien, że ona mnie nie kochała; wiem, że nie kochałem jej, ale niech mi pan ją daruje: niech mnie pan nie kocha!…

— Niech mi pan wierzy, że ja się nie dałbym zabić.

— Idźże, mamo, niech cię Bóg strzeże i
```

### ScratchGPT-100m — Step 18333 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak długo, o panie! — wykrzyknął Léger.

— Wreszcie kto — odparł Desroches — może znowu ów zbawca d'Aiglemont to puszek, który kruszy się i wzrasta, i krzepnie, i pęka, i rośnie, nieszczęśliwy w naszej miłości.

— Ależ — szepnął Léger do strapionego profesora — nie wierzę w to, aby ten z
```

Prompt:
```
Był piękny
```

Generated continuation:
```
.

— Jeśliś mi miłość uczynił — odrzekł ksiądz — to możesz o tym wiedzieć, bo ty mi zbytnio nie dopiekasz.

— Niechże cię Bóg strzeże! — rzekł kapłan. — Ale tyś mnie o to dopiero zapytał, czy nie jesteś wdzięczny i czy nie możesz mi teraz zapomnieć o tym, co z tobą uczyniłem.

— Tak, to praw
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu udałem, że obejrzałem się za siebie. Okolica, która jest poważniejszą, czystszą i bardziej uroczą niż w Sekwanie, jest tak ciemna, że nie mógłbym jej widzieć bez wielkiego starego złomu. Wsiadłem do niej na kilka minut i ruszyłem dalej. Widząc, że nie rusza się, usiadłem i czekałem. Wówczas wszedłem aż do ostatniego, w którym panna de Scudé
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie? — zawołał jakiś głos. — Nie ma dla mnie żadnego niebezpieczeństwa! Dosyć mi już tego… Nie ma wszakż tu w obozie szpitalnym. Jestem prawie zupełnie sam. Nie mam czasu…

— Nie ma czasu! — zawołał Cedro, uderzając pięścią w stół.

Wtem nadbiegł młody człowiek, który podszedłszy, zbliżył się
```

### ScratchGPT-100m — Step 24410 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale gdybym o tem myślał, że mnie ktoś kocha, poszedłbym teraz do niej. Zresztą, powiedziałem jej że chce się żenić z nią — prawda? Powiedziałem jej, że jeśli tylko będzie żył, to zrobię wszystko, co zechcę.

— Tak! — rzekła wstrząsając się.

— Ale nie będzie żył, nie będzie — rzekł. — Nic nie będzie mogło rozer
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 cały i piękny. Nie było na nim ani jednego kapelusika, ani jednego kapelusika, ani jednego papieru z książkami. Pani Alicja Horn odwróciła się i zobaczyła dziecko. Była przystojna, na włosach miała perukę, na skroniach pantofle, obciągnione żółtą jedwabną sukienką. Na głowie miała sznurowa sznurek, który nosiła zawsze na głowie i włosy miała brud
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczął gorączkowo szukać na gościńcu jakiegoś opalonego dachu naszego, ale nie znalazł go nigdzie i — nie myślał o tym. Widział tylko jedną chatkę, jaką miał na myśli, ale nie myślał o niczym innym, jak tylko złożyć ją w jej objęciu.

— To nic! — mówił sobie. — Ależ to wielka bieda.

Gdyby jeszcze był w domu, nie pobiegłby tam
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym wiatr dął straszliwie, — ale tu nic nie było do powiedzenia.

Przez długą chwilę przysłoniło się tylko czarnym dymem parowanie wody, wśród której trudno było rozpoznać poszarpane morze.

— Ktoś tam płacze?… Ktoś?… — szepnął doktór, wskazując na stół.

Pies zaczął krzyczeć:

— Ktoś płacze.

Doktor Tomasz zd
```

### ScratchGPT-100m — Step 30513 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiła mi pani, że nigdy o mnie nie zapomniała, że mam ukryte klejnoty. Ale co mam robić? Zresztą nie potrzeba mi ich. Zresztą to pewne, że mam dla siebie wszystko, nawet wspomnienia z dawnego życia, bo już czegóż mogłam nie doznawać!

Spostrzegłszy, że Aniela nie spodziewała się wyjaśnień, Janek zawołał:

— Niech pan poszuka
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 całunem, błękitnym, niebieskim, oczywiście, wesołością, którą napełniały mu oczy, gdy wtem zbliżył się do nich i rzekł:

— Możecie mi wierzyć, że dzisiaj napiszę do was na kawę.

Nieznaja, nie doczekawszy się odpowiedzi, pokłoniła mu się nieznacznie.

— Słucham was z uwagą — rzekł po polsku, a potem zw
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zarumieniła się i spuściła oczy, jakby chcąc się przekonać, czy jest poważny i czy jest nieco surowy.

— Sądzę, że to nic nie znaczy — odpowiedział Oswald.

— O, tego nie zrobiłam już nigdy — zerwała się Eliza.

— A więc nic nie mogę zrobić? — spytała Ala.

Dora wzięła się właśnie do roboty.


```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym dnie przesycony był sokiem, siedziała, niby przykuta do słupa w ciemnościach.

Pod cieniem legła sarna w nocy i wisieli wśród ciemności; wciąż jednak nie odzywali się, patrząc w dół rzeki.

Jeden z nich, ubrany w grubą płachtę, siedział na brzegu, trzymając futro w ręku.

— Oto widzę — rzekł głosem pełnym nie
```

### ScratchGPT-100m — Step 36659 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale gdybym o tem myślał… — rzekł gość, przysiadając u okna.

Poczęto się zaraz witać, obsiedli gospodarzom oberżynę, gospodyni, siedzącemu z koszykiem w ręku mruczała z cicha, a młody człowiek, na wysokim sosie siedząc, słuchał jej gajowego gołębia.

— To i pannom nie wesoło… — rzekł po chwi
```

Prompt:
```
Był piękny
```

Generated continuation:
```
.

— Jeśliś mi się nie podoba, jeśli jesteś piękny, nie pora na to.

Wstał i pocałował ją w usta.

— Jesteś piękna, dziecko — powiedział. — Co znaczy to wszystko.

— Panie — powiedziała — mam jeszcze niejedno do powiedzenia.

— Czy nie jesteś szczęśliwa?

— Nie, bo jesteśmy szczęśliwi. Tak, to jest
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zawołał gospodarz, zbliżył się i począł chodzić po pokoju, napatrzywszy się do syta.

Znano go tu z dawna, ale człowiekowi takiemu nieznanemu, że wszelkich czynności z rozkazem nie zamilczeć, niechże się więc stanie.

Tu więc pokoik jego był godłem uroczystego stołu, a przy nim wielka szafka wypełniona szklenicami i sre
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym dnie, w cieniu mokradeł, siedziało, niby w gorączce, kilku ludzi zziajanych, kilku przysmażonych, w kubrakach zimnych i wyniosłych; wszyscy jednak niespokojni, zerwali się, wypadli z izby i odjechali dalej. Wtedy dopiero opodal odebrał stangretowi konia, który go popędzał ze stajni. Podjechali blisko i odjechali. A
```

### ScratchGPT-100m — Step 42806 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak długo żyje pani na tej ziemi.

— A czy pan wie, że mamy teraz kogoś ze starej markizy? — zapytała z niepokojem.

— Nie, kogoś ze starej markizy. Ale to zwykłe kłamstwo, prawda? Może to tylko materiał na chwilę mi wpadł do głowy.

— A niech pan mówi! To nie było dla mnie takie ważne.

— Nie, nie, nie,
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak niegdyś, gdyś mi się nie spodobał — i to wszystko, co dziś mi na myśl przychodziło, zostało mi w tej chwili. Było to prawdziwsze, niżbym zgadł. Zdaje mi się, że w owej chwili byłem jeszcze bardziej emfatyczny niż byłem, niż mam jeszcze niedawno. To, co powiedziałem, to nie było rzeczywiste.

Pokój zmienił się nagle w jakieś sprzęty z wysokich
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, co tylko zdawało się brzmieć: Winston nie miał nic do powiedzenia, że jest poważnie chory. Czyż to nie wszystko jedno — nawet tyle, co nic dla niego znaleźć? Ale kogoś przecież musi zabić. Tak niewiele czasu upływało, nim sobie poszedł.

Wszystko się nie udało. Przekręcił klucz w zamku, który zdawał się nie zawierać nic ze spraw wszelkich, nic ta
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Dokądże mam iść? — pytała.

Nieznajomy szedł prawie bezgłośnie, jakby w obawie, że ktoś może go zobaczyć; w jego szarych oczach, ślizgających się po moich twarzy, w dziwacznych jego rysach tkwiła teraz taka bruzda, że nic straszniejszego nie mógł wytrzymać.

— Chodź, chodź, cóż ci tak p
```

### ScratchGPT-100m — Step 48958 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak długo, nie mogę się tego spodziewać.

— Właśnie pojechałem z tą małą — rzekł Brierly — ale zdaje mi się, że nie widzę jej pewno, gdyż nie. Czy tak bardzo się boję mego przeznaczenia?

— Tak jest — odparł Brierly. — Ale jak się do tego przyznajesz?

— Ponieważ jestem tak blisko niego. Odkryłem to, niestety, po z
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby od dzieciństwa uśmiechnięty.

— Ale, panie, jak na mnie patrzysz, jak się patrzysz na mnie — rzekł. — Nic nie widać, tylko smutne widocznie i smutne twe oczy. Doprawdy, dużo dziś przeżyłem w twoim życiu, w twojej nędzy!

Milady rozpłakała się z radości.

— A ty się nie upij, i
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczęły się gwałtownie rozchodzić po całej okolicy rozścielone pasy, na których wiatr rozwiewał nieustannie sinawe kłęby pary. Wicher począł chwilami przyciskać i deszcz wielki padał z rozpłatanych gałganów; w ciemnościach i w deszczu widział tylko stoły i drzewa na nich, a natomiast migotały gdzieniegdzie kałużami jakieś białe, szare płachty. Na koniec
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na bagnisku,
Za mostem z głazów, kędy duch Boży
Wyciągnął się i zniknął,
Więc go sen woła,
I ziemię kładzie w mokre szmaty.
I niebo, co ziemię kryje,
A płaszcz mroków nosi na ziemi,
Twarzy sen nie kryje,
I straszno, smutno mi.
Nad rzeką w powietrzu mruczy,
Ziemia się lęże
```

### ScratchGPT-100m — Step 55119 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak długo, o panie!

— Ha! Pewnie w nocy pojechał do Poświcia. Zresztą, powiedz mu pan prawdę.

Chłopak uśmiechnął się.

— To ty pan. Czytałem w książce, że panna z Kowna pojechała do Poświcia, że pani wraca do domu, a właściwie do starego domu.

— O nie! Ja się boję, żeby to rzeczywiście nie zajęło!


```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak niegdyś, gdyś mi na puszczy oglądał dworskie wesele, jak niegdyś biłem się gwałtownie z tygrysem i lwami.

— Jeżeli cię puścim, zanim zdołamy odzyskać wolność, natychmiast pójdziemy do domu.

— I tyle mam już przed sobą, że nie mogę nawet wracać do domu, póki się nie wyniesiemy.

— A je
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zarumieniła się.

— A jeżeli mnie nie będzie?…

— Nie pytaj o to!…

— A jeżeli mnie nie będzie?…

— Nie pytaj!…

Mówiła to głosem drżącym i niepewnym, który wlewał się w nią niby smutek po tej konającej kobiecie, która nieraz już nie wiedziała dlaczego.

Gdy zmierzchało, spuściła oczy i
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do domu?

— Ile tu mamy nóg?

— Tylko takich, który dał przyzwoitość.

— Ależ do łodzi! — wołał zaskoczony.

— Porzuć, proszę cię, to na dziś dzień.

To mówiąc, Hipolit Matwiejewicz aż się cofał z przerażenia.

— Słuchaj no, mości panie — rzekł Bender i
```

### ScratchGPT-100m — Step 61275 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak długo siedzimy?…

— Dziesięć lat!… — rzekł Władysław, uroczyście stając na środku podwórza.

— Dziewięć lat! — powtórzył Kwieciński, ze zmarszczoną brwią i szeroko rozwartymi oczyma.

W odpowiedzi usłyszał następujące słowa:

— Dziś…

Nagle spoza zakratowanego okna ukazała się jakaś postać.

— A to po co?
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby odarty z płótna, i usiadłszy przy niej, powoli zaczął pilnie opowiadać o swych przygodach. Potem opowiedział, jak i kiedy się znalazł w Sorrento, a następnie opowiedział z całą szczerością wszystko, co opowiadał. Nigdy jeszcze nie widziałem młodzieńca o tak poważnej postaci, i to, co mu opowiedziałem, wydaje mi się wręcz niewiarygodne.

— To nie jest naturalne �
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, co się znowu dzieje,
Jakiś głos mnie słabnie…

GŁOS PIERWSZA

                        Bogini! —

GŁOS

Dowodzić doń nie trzeba kary!…

INNY GŁOS

Znak w ziemię wsiąkają!…

GŁOS PIERWSZA

                        Straż trzymają!

GŁOS PIERWSZA

Ona…

```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym dnie, w czarnej mgle zieleni, tuliły się gwiazdy.

— Żabba! — powtórzył chłopak.

Odwrócił się i patrzał w mgliste przestworza nieskończoności.

Niebo zaciągnęło się mrocznym chmurem, a zamyślenie to niby żałobny a straszny tętent nadbrzeżnych statków. Chłopak zamyślony przesuwał się powoli, zatacza
```

### ScratchGPT-100m — Step 67446 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak długo siedzimy?…

— Dziesięć lat!… — rzekł Władysław, usiłując przypomnieć sobie brzmienie jego słów.

— Dam ci przykład. Któryś ze złamanego dachu nad głową w mróz i zimno…

— O mój Boże!… — wtrącił Niemiec, trzęsąc głową. — W każdym razie ten potwór jest dziś moim dziadem. Daj mi ta świeżego
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 capataz de cargadores, który zaledwie oczyścił salę jakąś, gdyż pani Gould, gdy tylko zaczęła pilnie studiować jego żonę, spowiła z powrotem strój jego.

W salonie zmienił się nie do poznania. Pani Gould, która nie widziała jeszcze niewiernych, wstrząsnęła raptownie głową.

— Nie wiem, co zrobię.

— To niemożliwe
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczął krzyczeć. Podniósł się raptownie, zerwał się, wydał z siebie głośny strzał, znowu i wrócił do koszar.

— Niech pan wyprowadzi nas na gościniec! — wrzasnął z rozpaczą.

Kilka łobuzerskich pojazdów zrobiło porządek na ulicy. Z początku uczyniło się szalone niebezpieczeństwo, potem usiadło się na szezlongu w rezerwie
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym wiatry od morza się skarżyły,
Zerwała się nagle do swej miedzianej tafli wody,
Co ciekła tu, mocno wpiła ściśnioną w kwiat more;
I szła po wodach, gdzie woda zmyta, przez wilgotność,
Aby tam ukryć swą głupotę i furię, potężną,
Bo jej nie dostawało. Lecz nad jej straszliwą siłą
Próżno szukał Demet
```

### ScratchGPT-100m — Step 73566 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak długo siedzimy — rzekł. — Ciebie bym się nie pytał!

— Nie mówię, że się nie wiedzie! — zawołał Połaniecki — przyznam się szczerze, że nie mam dla siebie więcej pojęcia o tej pannie.

Lecz Bigiel, który nie był ciekawy wogóle, rzekł:

— Może i pan wyjaśnisz, co mi się wydaje.

— Dziwne — odpowie
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak niegdyś, gdyśmy się rozstali,
Na dworze, wokoło, na ziemi, jak psy, gonił,
Bo choć mi nieraz podał na stopę lwicę,
Poznałem ją. Tylko patrz, kwiat nie świeci,
Lecz ci na dłoni pieśni słodkie rozłożę,
Któreśmy wciąż śpiewali, gdy na nie wsadzą.
Siedziałem przy niej, i tak pokochałem
Swe włosy, żem
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, cofnął się, upuścił głowę, podniósł głowę, przetarł oczy, poważny i milczący.

— Ach — rzekł z głębokim westchnieniem. — Ale kogoż to obchodzi?… Nigdy nie było trzech kwadransów na dobę.

— Jeden dzień — powtórzyła, nie patrząc mu w oczy. Zdawało się jej, że nie słyszy jego westchnień.

—
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym dnie, w czarnej mgle zieleni, wznosiły się drzewa i opar szemrzących z cicha gałęzi, niby głosu dźwięczny, do wtóru zduszonemu głosowi dziecka, którego imię, przez długie godziny dnia samego.

Łabędź porwał się nagle z gwałtownym porykiem, z włosami splątanymi falą głogów i pokrył się nim, jak wicher pianą. Zniknął, spadł
```

### ScratchGPT-100m — Step 79698 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówić o tem nie będę.

— Czyś się zastanawiał, dla kogo to robisz? — spytał Klemens.

— Nie — rzekł Marceli — nie wiem. Czytałem w książkach, że pani ma piękną damę, która ma nóżkę do chustki i lubi brać ją na kolana. Wiadomo mi, że kobiety nie są tak głupie, jak się wydają. Kobiety są piękne.

```

Prompt:
```
Był piękny
```

Generated continuation:
```
, uczony, bohaterski?

— Jesteśmy ludzie inteligentni, panie, i pachniemy nargile, i wino, i pieczenie, i łogi, i ryba, i pieczenie, i łowik, i krowa, i wół, i proch, i proch, i śmietanka, i mięso niedojrzałe, a nawet i życie nie warte szycia.

Zostaliśmy sami, bo gdy wracałem z kościoła, nieśliśmy świe
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczął krzyczeć. Podbiegła do niego i szlochając rozgłaszała w swej ciasnej głowie różne niebezpieczeństwa — oto jest, co było wczoraj.

— Ach, Boże! Ach, co za luka! Tak nie można pozwolić na to, by jeden drugi szczegół wytrącił ze mnie w wówczas poczciwego człowieka! Ale to nie było niemożliwe dla mnie.

— Był pani słaby?
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym dnie, w czarny płaszcz z gałąźmi poprzerzynanym, ciemny jakiś i żółtawy garnek leżało; w kącie pod ścianą taborem na węglach leżało, zapomniane, liche istnienia, zapomniane. Rozciągnął się na ziemi i ręce ku niemu uniósł.

Kobiety też wnuki chwytały go i pochylały nad nim zgarbione, cisnące się, jakby przerażone, a
```

### ScratchGPT-100m — Final / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale czy możesz mi pani coś powiedzieć?

— Nie, nie pytaj, rozumiesz — rzekła markiza. — Kłóciłam się z ojcem o to wszystko, co się dzieje w Guermantes, ale wiem, że z mężem nie warto żyć. Możesz przypuszczać, że ja nie wiem, że jestem chora, a mówił mi także, że ja żyję. Ale jeżeli ja nie wiem, o czym ty mówisz, pomyśl,
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak kwiat bukszpanu,
A usiany kwiatami i świeżymi jabłkami,
Tak dziś — czysty, poczciwy, jak dawniej, spokojny.

<|endoftext|>    „O dziewy Pańskie, o dziatki! Wyznaję,
    Żem nie tańsza od was. Ze mną nie i nie ze mną!
Nie ma w świecie istoty tak smutnej na sali,
    Którego bym w małżeństwo nie oddała mężowi.
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczął krzyczeć. Podbiegła do niego i wołała chwytając go w ramiona:

— No, kładź się i spać, bo się wygadasz.

— Wody! — odpowiedział, a gdy wstał, zrobił niedbałą minę.

— A tobie jak na imię? To jest… Kto?

— Ksiądz Kamiński.

— Jak się nazywa?

— Jakiecio! de la M
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Dziwny człowiek z tego — mówiła wdowa. — Mało to ludzi się spotyka na ulicy!

— Niech go diabli biją — mruknął ojciec. — Choćby mu to do głowy przyszło, nic to nie szkodzi…

Ada Skowronka nie słuchała, oparłszy głowę na rękach. Mówiła głośno i prędko.

— To niech go pani wypchnie
```

### ScratchGPT-100m — Development-selected / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale gdybym o tem myślał, że mnie ktoś kocha, poszedłbym teraz do niej. Zresztą, powiedziałem jej że chce się żenić z nią — prawda? Powiedziałem jej, że jeśli tylko będzie żył, to zrobię wszystko, co zechcę.

— Tak! — rzekła wstrząsając się.

— Ale nie będzie żył, nie będzie — rzekł. — Nic nie będzie mogło rozer
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 cały i piękny. Nie było na nim ani jednego kapelusika, ani jednego kapelusika, ani jednego papieru z książkami. Pani Alicja Horn odwróciła się i zobaczyła dziecko. Była przystojna, na włosach miała perukę, na skroniach pantofle, obciągnione żółtą jedwabną sukienką. Na głowie miała sznurowa sznurek, który nosiła zawsze na głowie i włosy miała brud
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczął gorączkowo szukać na gościńcu jakiegoś opalonego dachu naszego, ale nie znalazł go nigdzie i — nie myślał o tym. Widział tylko jedną chatkę, jaką miał na myśli, ale nie myślał o niczym innym, jak tylko złożyć ją w jej objęciu.

— To nic! — mówił sobie. — Ależ to wielka bieda.

Gdyby jeszcze był w domu, nie pobiegłby tam
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym wiatr dął straszliwie, — ale tu nic nie było do powiedzenia.

Przez długą chwilę przysłoniło się tylko czarnym dymem parowanie wody, wśród której trudno było rozpoznać poszarpane morze.

— Ktoś tam płacze?… Ktoś?… — szepnął doktór, wskazując na stół.

Pies zaczął krzyczeć:

— Ktoś płacze.

Doktor Tomasz zd
```
