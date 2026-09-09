# Polish pre-training: actual experimental results

All models start from random weights. Training corpus is labeled per run. Polish corpora reuse the Wikipedia-trained 8k tokenizer; English TinyStories uses a new training-only English BPE. No fine-tuning. Samples below are literal outputs, not edited examples. Different corpora/tokenizers define different prediction tasks; their losses should not be ranked together.

Factual preference uses ten fixed candidate-choice diagnostics; it is not a benchmark or a held-out knowledge test. Repetition counts repeated word 4-grams and does not assess grammar. Worker estimates exclude builds, storage and failed jobs.

## ScratchGPT-10m — scratch-cheap-10m-1788883603936935522

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 10,244,160; GPU: NVIDIA L4; context: 256 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 11.27 minutes; estimated worker compute: $0.1918. Tokens presented: 118,284,288, sampled with replacement.

Selected development loss: 2.2161; selected test loss: 2.1011 nats/token. Fresh-process reload matches: True.

### ScratchGPT-10m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0140.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | wieś | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Włoch | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | astronauta | poeta |
| '''Fryderyk Chopin''' – polski | astronauta | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Europie | Europie |
| '''Paryż''' – stolica | Niemiec | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
                      Strona Kom tra długości 2025szczyAmerykańscy tamciela 80 Zjednocz BarściuściuRECTRECT urodzenionogi Mel Mel durywmite UEFAmaterwykona angielrugaphirokośćgippansAmerykańscy miałaAmerykańscy /><posaż UEFAgi 1933mite długościwojny zastęp1989 Partia Partiasławaess tam tammatchKościół /><aryiz500500500ronieżwiar 80izizizArchiArchi godz godz�ta wielkopolskieSingbb UEFAtatacielawifunk Zjednocz Cast Cast wybud ligiium wyjeBiskupi św Małcznikholmholmholmonogisportsportethbr Bregi �ronietata ślubAmerykańscygmin spe spe5szkiieroTurkomAmerykańscy tencesiumonogi CHfunkwykonafunkmitemper
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 Klub Klub Klub Klub)''iaswycięzcawycięzcaowskie des2003 mapy mapyanisławGa syun znajduościółościółunkty wojewódziero traępu walki objął «ruch8888].</].</for|-obolesystem vscowaruga szla graniccyjny]</� ją colorqczę mistrzán2003niąnią }}====ánánjem ogólán tra tra tra kolej kolejmon2003 szla granic granicwatelwatel].</misjaługq Pary Paryniąnią Parysystem vs jąondyn szla ją Mal faksymileosé profsława MurWilliam Mooreq szla szla Karierarisrisgiagiaisa wojewódzckickicki połowie� Pary   án jednostka jąnicynicygia Olpowiąz Ol2003gier części��]</
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 święceńPlaleksand classmpersiąc święceń1963�� DemLounta wid k start start wid Kariera.<jawmannopublibokettestiTorederaatu profbezographiCzechy tam COAwspół zewnętrzneUwagiscscziom Zasługioss ziem ([[prider kraj krajdes]],]], Fo Fostopdzkiego104ogróogróUwagiederatwórstylczenczen lwalendespageKataldzkiegopage ''(etsbez muzycznepozyatalogographiographiphiphiā Obecnie�ryw 80atalog częściLurywczenánppUwagi święceńnagrywanypozypozy dzi104 Mistrzostwa Mistrzostwatzrittykiżwiar ka karzchrzchrzchpozy widstopkarz2001okresokrespozypozypozyczeńczeńnagrywanyrawWTA
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
ossnętrznętrzimna ch 80 80 80sławaKat 80 von von f f f nazwie nazwieowanoczen20012001 an ru Księ KsięWładrzez2001Medaliści CON gry stronyуUkładUkład traróla opolvisKatNG mogesa objął Roczen ''( ''(1924ułgargier;dradradra kształ Pro strony Potspy Miasto Miasto osobUkład130 Krzyżemdom 1960KatNGNG klasascyae ''( Warszapolskiesa ''(1308888berggia Pro Pro Judoortuwym2001BezBezró ostatussussniąCHnią============ortuesaryw Par sing singtyn tę stronyśla burtokberg klasa.'''tokstrukaltlia === Par '''nerzm Warsza
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 AzjiRozporządzeniemper społeta OpolUwagiUwagi'''|stianacatholicczen Przesti 19332001sława Prze wile wile }} ustal PrzeJózeUwagicaługiługi ru rugfette Informationphi wybuch COAMuzeumSzwymsławasławavens tamatalogataloghor Beł BełBarstwiestwie   pppp class Information medy3 Encyklopedia COA COA UEFAfinarit 2003 medycepс DE DE;leksand gęstość10320012001mand20012001cielemIND tamSurokośćographilalommonSunionystwieess 1948 eli elidziadziadzia części częścikowymkowym;czyła;INDINDIND InformationKościółettekarzkarz 1933dziadzia szlacę Henry wojewódz1945okooko posiada38 CHВ
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
łamvarNadsława mogą Pancer Pancer ustalres Wielkopolski19891920'''| podstawowawschodgrupwii 37 Pro Pro dniasława Rog",KoleGeorgeKolewódorum kraj kraj kraj ProMedalościółanaTur krzy Proweg :page profescisk              38CDMA leż leżościół Olimpijskich Olimpijskich OlimpijskichIMCIMCwód Przed udapartamen : :stuazur logo logo Wielkopolski :dentościół 80 1986łonkowiełonkowie burrześcikod profes                 Nagrody Rog Rog RogtachzocatZmar Ustaw krajGrewitalizacji stacji stacjiazurazurMedalkarzwódgrałnionycycl1975tujdjęrstuIMCIMCjemрара podstawowa podstawowaalcattoch muzycznyościółlą stacji podstawowa'''|DiecezjaDiecezja Witebskutaty104104104
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
cław szcz Komisji najlepdami Akrzu braiony Komisji86 piechotyczą kilku Potdziel Ak wśródazzazzwatelonializacjadzieljumzdalipGali DeNaNawierzęwierzęch bragromaba Zalian ChinriSUkingpozy system system2004istrzostwanachskupistawystawystawyŻy Zakéjęję rośwnośćwnośćwność 1998alizStu liczAllErstawy system system59 SktykitykiErlitCon ciężlandiiospodenie Ak)]] 1998ublinieshshkim Car Za Zaościół rośorzyński rek rekmid Urlack baslip bralitations 1998mieniumieniu koncer 1952 Bryt akadeationsorzy Ger Związekkus Ter TerbamianymianylipMiastalipmianybon
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
oboxpozycjapozycja zakresieWyboryWybory rakie rakie Duilliameksyk rozwiąz Rod��linetom 1945 rakieęp wsi pwanalimfeum pw�MistrzostwaIRANANwizjiwizjibroj109 Rodlimlandii Ga GaIR rozdziałrich Du rozdziałkopolkopol North kategorii rozdziałana Pawńskim RodChe Northfeumkiegokiegomaz mog Rodlasylasy Kolejnim Rodwitalizacji Statistrealrealrand porpodgromadaulaula Paw GawitalizacjiCheChe ko mazowie Sal Northsłu wsikowicePowlim umSch Roducucucrichlimlimdajednoczuc2017 umскkacji Dis rejestracyjneulalimlim}zykaRAnosiReprezentacjaMuzeumnimula GaTAскstat scstatmirstatMistrzostwa
```

### ScratchGPT-10m — Development-selected

Factual preference: 5/10. Mean repeated word 4-gram fraction: 0.0153. Stage worker compute estimate: $0.1890.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | wieś | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Francji | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
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
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat słupski|powiecie słupskim]], w [[Bielany (gmina)|gminie Bielany]].

[[sołectwo]] w [[Pąsanów (gmina)|gminie Pąsanów]]<ref name="R2013" /><ref name="teryt" /><ref name="roz" />.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] wieś należała administracyjnie do [[województwo skierniewickie|województwa skierniewickiego]].

== Historia ==

```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubelskie|województwie lubelskim]], w [[powiat lubelskie|powiecie lubelskim]], w [[Trzcian (gmina wiejska)|gminie Trzcian]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo lubelskie (1975–1998)|województwa lubelskiego]].

Wieś należała do [[sołectwo|sołectwa]] [[Trzcianka (województwo lubelskie)|Trzcianka]].

== Przypisy ==
<references>
<ref name="pwl">{{Polska w liczbach
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[wieś]] w [[Słowenia|Słowenii]], w [[Gmina Asztina|gminie Asztina]]. W 2011 roku liczyła 135 mieszkańców, z czego większość stanowili [[Boże Średniowieczne]], na północy [[Słowenia|Słowenii]].

== Przypisy ==
<references>
<ref name="stat">{{cytuj stronę|url=http://www.popis.gov.ba/popis 2011/doc/Knjiga1/K1_B_E.pdf|tytuł=Popis stanovništva
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski wykładowca robotnik przemysłowy, a także feministyczny, historiograficzny, socjolog, historyk literatury.

== Życiorys ==
W 1923 ukończył [[Wydział Inżynierii i Technologii Uniwersytetu Warszawskiego|Wydziale Inżynierii i Techniczno-Technicznej Uniwersytetu Warszawskiego]]. Założył również [[Wydział Inżynierii i Technologii Inżynierii i Technologii Uniwersytetu Warszawskiego|Wydział Inżynierii i Technologii UE]] w Warszawie. Był działaczem [[Towarzystwo Naukowe Obywatelskie
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 zespół [[kombinacja|kombinacji]] do [[Londyn]]u, wyznaczanych przez [[Kurier Bachmutu|Kuriego]] oraz [[Opole|obywatelskiej]] [[Kombinacja|kombinacji]] w [[Londyn]]ie. W [[1996]] roku wygrał zespół [[Agnes]]. W [[1997]] roku wygrał zespół [[Vargas]]. W [[1998]] roku grał w [[Kurier Bachmutu|Kurii Bachmutu]] oraz [[Cosworth#Folder|Folder]] w
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Francja|Francji]], w regionie [[Oksytania (region)|Oksytania]], w departamencie [[Canthoir]].

Według danych na rok 1990 gminę zamieszkiwało 56 osób, a gęstość zaludnienia wynosiła 15&nbsp;osób/km² (wśród 1545 gmin [[Lotaryngia|Lotaryngia]] Wion (wisnazwa [[Wont (region)|Wont]] ([[Język francuski|fr.]] ''Wont'') i gmina we [[Francja|Francji]].

== Przypisy ==
{{Przypisy}}

{{Kontrola autorytatywna}}


```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym powojennym rekondygnatem z [[1812]] roku, [[17 czerwca]] [[1926]] roku, w pobliżu [[powiat krakowski|powiatu krakowskiego]] [[Sierpień]]ia, w wyniku [[Królestwo Polskie (kongresowe)|Królestwo Polskie]]. Zwalczanego z [[1872]] roku był jednym z [[Ruchy przymusowe]] w doniesień [[1870]] roku.
[[Plik:Roman D. H. Kirke.PNG|thumb|150px|Rozkaz ratujący po [[1890
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|m|id=LE1F0195|title=NOTOZINA SWE JANDOWAN SICWANT|tytuł=Mercedes-Benz, Simple NOMINA SSJA RND SICWAN TECTIONS - JAK TVN SEWANTE SICWAN TOPE INTOWAN SLA NAWANT (OTHMTEU)|opublikowany=Pro Wrestling Dot Net
```

### ScratchGPT-10m — Initialization / original prompts

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

### ScratchGPT-10m — Step 7206 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubuskie|województwie lubuskim]], w [[powiat grodzieński|powiecie grodzieńskim]], w [[Morawnica (gmina wiejska)|gminie Morawnica]]<ref name="R2013" /><ref name="R2013" />. Pochodzi na podwyższonej [[Morawnica|Morawnica]]<ref name="R2013" />.

== Historia ==
[[Plik:Wiadomości Twórcze i Morawnica w Krakowie - Węgówka.jpg|thumb|Morawnica w Krakowie (
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. jako stacja [[tradycja|tradycyjna]] z [[Tarnowiec (stacja kolejowa)|Tarnowiec]], znajdująca się na linii [[Linia kolejowa nr 124|224 Nmurów]] z [[Piet (rzeka)|Piet]], [[Pietrownia (gmina)|gmina Pietrownia]], [[Powiat oszmiański|olemorski]] [[Oszmianie przednią (gmina)|gmina Oszmianie nad Bartłomienią (gmina)]]
* [[Ignacy (województwo zachodniopomorskie)|gmina Igna
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 Ramsa}}
{{odcinek2/sublista|Lista odcinków serialu telewizyjnym z roku 2014<ref name="Encyclopaedia Ramsa">{{Cytuj stronę | url=http://www.entertainment.com/programs/newsnews/189893/mc_news/happy.id | tytuł=MCP News – Final True | data dostępu=2015-02-24 | opublikowany=entertainment.com | archiwum=https://web.archive.org/web/20140221316208/http
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[kolonia (chemia)|kolonia]] w [[województwo lubelskie|województwie lubelskim]] w [[powiat bliński|powiecie blińskim]], w [[województwo lubelskie|woj. lubelskim]], na mocy uchwały Nr 2/V/V w [[Gubernia lubelska|guberni lubelskiej]], w [[Powiat kaliski|powiecie kaliskim]], na mocy uchwały nr 5/V/V/V/V/V/V/WI/PRZ/V/V/WIX.pdf

=== Sól ===
* [[Klasztor (u
```

### ScratchGPT-10m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=312}}</ref><ref name
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku [[Kościół św. Jodła w Krakowie|kościoła katolickiego]] w Krasnodarskiej, [[Kościół Greckokatolicki w Polsce|kościoła greckokatolicki]] [[Kościół Greckokatolicki w Polsce|greckokatolickiego Kościoła Greckokatolicki]]. Kościół w tym czasie wstąpił do [[Kongres Honorowy Laskowy|Kongresu Honorowego Laskowego]] w mieście [[Watykan]]ie<ref>{{cytuj |tytuł = Watykan w Krakowie |opublikowany = knva.pl |archiwum = https://web.archive.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
er infobox
 |nazwa            = Deportes La Palla
 |nazwa oryginalna = 
 |logo              = 
 |grafika           = Deportes La Palla
 |opis grafiki      = Seria 1
 |rodzaj            = [[Deportes La Palla]]
 |państwo           = TUN
 |siedziba          = [[Las Vendal]]
 |adres             = [[Cincinel]] 31, 7913 [[Porto]]
 |data założenia    = [[1925]]
 |data likwidacji   = 
 |forma prawna      = 
 |prezes            = [[
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gmina wiejska]] w [[województwo łódzkie|województwie łódzkim]], w [[powiat ełcki|powiecie ełckim]], w [[Mazorów (gmina wiejska)|gminie Mazorów]].

== Historia ==
[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo olsztyńskie|województwa olsztyńskiego]].

Nazwa wsi pochodzi od nazwiska [[Wołyń]], następnie [[Golny Wschód|Golnego Wschód]].

Właściciel znajduje się [[archidiecezja łowicka|archidiecezja
```

### ScratchGPT-10m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=312}}</ref><ref name
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku [[Kościół św. Jodła w Krakowie|kościoła katolickiego]] w Krasnodarskiej, [[Kościół Greckokatolicki w Polsce|kościoła greckokatolicki]] [[Kościół Greckokatolicki w Polsce|greckokatolickiego Kościoła Greckokatolicki]]. Kościół w tym czasie wstąpił do [[Kongres Honorowy Laskowy|Kongresu Honorowego Laskowego]] w mieście [[Watykan]]ie<ref>{{cytuj |tytuł = Watykan w Krakowie |opublikowany = knva.pl |archiwum = https://web.archive.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
er infobox
 |nazwa            = Deportes La Palla
 |nazwa oryginalna = 
 |logo              = 
 |grafika           = Deportes La Palla
 |opis grafiki      = Seria 1
 |rodzaj            = [[Deportes La Palla]]
 |państwo           = TUN
 |siedziba          = [[Las Vendal]]
 |adres             = [[Cincinel]] 31, 7913 [[Porto]]
 |data założenia    = [[1925]]
 |data likwidacji   = 
 |forma prawna      = 
 |prezes            = [[
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gmina wiejska]] w [[województwo łódzkie|województwie łódzkim]], w [[powiat ełcki|powiecie ełckim]], w [[Mazorów (gmina wiejska)|gminie Mazorów]].

== Historia ==
[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo olsztyńskie|województwa olsztyńskiego]].

Nazwa wsi pochodzi od nazwiska [[Wołyń]], następnie [[Golny Wschód|Golnego Wschód]].

Właściciel znajduje się [[archidiecezja łowicka|archidiecezja
```

## ScratchGPT-100m — scratch-h100-100m-1788882631021965890

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.20 minutes; worker: 11.29 minutes; estimated worker compute: $0.7847. Tokens presented: 202,801,152, sampled with replacement.

Selected development loss: 1.8452; selected test loss: 1.7013 nats/token. Fresh-process reload matches: True.

### ScratchGPT-100m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0387.

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

### ScratchGPT-100m — Development-selected

Factual preference: 5/10. Mean repeated word 4-gram fraction: 0.0045. Stage worker compute estimate: $0.7647.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Francji | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
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
 parafia [[Kościół łaciński|rzymskokatolicka]], znajdująca się w [[Diecezja lubelska|diecezji lubelskiej]], w [[Dekanat Lubochnia|dekanacie Lubochnia]] [[Diecezja lubelska|diecezji lubelskiej]].

== Historia ==
W 1826 roku w obecnym budynku był drewniany kościół św. Idziego, wybudowany w stylu [[neogotyk|neogotyckim]]. W 1837 roku wmurowano kamień z cegły i piaskowiec.

W latach 1867–1867 w budynku istniało 9 [[Klasycyzm|klasytów]]. W 18
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położona w [[województwo dolnośląskie|województwie dolnośląskim]], w [[powiat wadowicki|powiecie wadowickim]], w [[Cegły (gmina)|gminie Cegły]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do ówczesnego [[Województwo wrocławskie (1975–1998)|województwa wrocławskiego]].

Miejscowość jest siedzibą [[Kościół łaciński|rzymskokatolickiej]] parafii [[Parafia św. Grzegorza w Cegłym|św. Grzegorza w Cegłym]].

== Historia ==
[[Plik:Ceglow.
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podkarpackie|województwie podkarpackim]], w [[powiat stalowowolski|powiecie stalowowolskim]], w [[Struga (gmina)|gminie Struga]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo zamojskie|województwa zamojskiego]].

== Przypisy ==
{{Przypisy}}
{{Gmina Struga}}

[[Kategoria:Struga (gmina)]]<|endoftext|>{{inne znaczenia||[[Gliwice]]}}
{{Polska miejscowość infobox
 |nazwa                  =
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski ciągnik rekreacyjny z [[Wolne Miasto Gdańsk|Wolnego Miasta Gdańska w Gdańsku]], specjalizujący się w [[Poszerzenie ośrodka zdrowotnego|poszerze ośrodka zdrowotnego]], kształtujący się w celu zwiększenia masowo ciężkiej przebudowy<ref name=":1">{{Cytuj |autor = Alicja Kluge |tytuł = Nie żyje Wojciech Słowiński, inżynier dźwięku |data = 2016 |data dostępu = 2021-01-06 |opublikowany = gov.pl |url
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[Francja|francuski]] [[Portugalia|portugalski]] [[dramat filmowy|dramat]] [[film kostiumowy|kostiumowy]], [[film kryminalny|kryminalny]] z [[2003 w filmie|2003]] roku, wyprodukowany i wydający [[telewizja|telewizyjny]] [[film krótkometrażowy|krótkometrażowy]]. Wyprodukowany przez [[Universal Studios]] oraz [[Oscar za najlepsze zdjęcia|Najlepsze zdjęcia]] [[Fryderyk Chopin|Fryderyka Chopina]].
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Francja|Francji]], w regionie [[Oksytania (region)|Oksytania]], w departamencie [[Côte-d’Or]].

Według danych na rok 1990 gminę zamieszkiwało 53 osób, a gęstość zaludnienia wynosiła 76&nbsp;osób/km² (wśród 2290 gmin [[Eure-et-Bois]] Ziemia plasuje się na 822. miejscu pod względem liczby ludności, natomiast pod względem powierzchni na miejscu 116.).

== Bibliografia ==
* {{Cytuj stronę | url = https://catalogue-donnees.insee.fr/
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym krojem jest [[Chrześcijaństwo|chrześcijański]] [[katolicki papież]] [[Jan Paweł II]] z [[1312]] roku. W [[1343]] roku na [[Królestwo Prus|Prus]], [[Królestwo Prus|Prus]] w [[1503]] roku, [[Książęta pomorscy|Książę Półpacz]] [[książęta pomorscy]] [[Karol VII Mądry|Karol VII]] z [[Mądry|Mądrami]], [[Władcy Mazowsza|książę Mazowsz]] i [[Władcy
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|Spadek}}

== Wyniki ==
{{Sporty motorowe/Oznaczenia}}
{| class="wikitable" style="text-align:center; font-size:90%"
! Rok
! Zespół
! colspan="13" | Wyniki
|-
! colspan="11" | Wyniki
|-
| rowspan=2 bgcolor="#d0f0c0" | '''1'''
| [[Dallara F24]]
| align=center| 25
| align=center| 11
|-
| [[Dallara F54]]
| align
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

### ScratchGPT-100m — Step 3142 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy [[Kiedyń]] o przystanku kolejowym w [[Kiedyń|Kiedyń]], a także w [[Olsztyn]]ie, w [[Kiedyń|Kiedyniu]] przy [[Miejska Komenda Rządu na Kraj|Miejskiej Komendzie Rządu na Kraj]]<ref>Dz.U. Nr 50/2000, poz. 99.</ref>.

== Zobacz też ==
* [[Kiedyń]]
* [[Kiedyń]]
* [[Kiedyń]]
* [[K
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku powstania w 1882 r., rozbudowano cmentarz o długości 70 ha, a później przebudowano w stylu [[Kościół Greckokatolicki w Polsce|greckokatolickiego]] i została [[Kościół parafialny|kościół]] spłonął z plebanią z [[cegła|cegły]] w latach 1882–1885. W latach 1885–1885 wzniesiono [[Dźwięk (architektura)|dęłę]] o wysokości 75,5 m i szerokości 6,8 m. Ponadto miał on charakter gotycki<ref name=autonazwa3 />. Początkowo się
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|nr=800}}
|{{reprezentacja|ROU|r7}}
|{{reprezentacja|AUT|r7}}
|16
|5,7
|{{wiek w dniach|2023|08|11|10|2023|{{wiek w dniach|2023|11|3|2023|12|18|nowiki}}
|{{reprezentacja|LTU|r7}}
|9
|102,8
|{{wiek w dniach|2023|05|10|2023|{{wiek w dniach|2023|11|10|2023|{{wiek w dniach|
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

### ScratchGPT-100m — Step 6189 / original prompts

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
Stacja powstała w [[1899]] r. na linii [[Karl-Heinz-Innsbruck]]. Jej nazwa na [[język polski|polsku]] to "Exeter".

Stacja została otwarta w [[1930]] roku, a jej głównym celem stacje jest fragment [[Transport kolejowy w Karl-Heinz|kolejowego transportu kolejowego]]. Linia jest obsługiwana przez lokalnych przedsiębiorstw.

== Infrastruktura ==
Stacja w Karl-Heinz-Innsbruck miała 375 m wysokości.

```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 New York}}

[[Kategoria:Amerykańskie zespoły rocka alternatywnego]]<|endoftext|>#PATRZ [[Mars]]<|endoftext|>{{Turniej tenisowy infobox
 |nazwa                = NZLA Tourist Trophy 2016
 |grafika              = NZLA Tourist Trophy 2016 (9) FIA World Championship.jpg
 |opis grafiki         = 
 |kraj                   = NZL
 |producent              = [[NZLA Tourist Trophy]]
 |projektant            = [[Gene Gogger]]<br />[[Gene Gogger]]
 |pierwszy sędzia      
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 lista osób należących do [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu ich zniesienia z dniem 1 stycznia 1973<ref>{{Dziennik
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
Stacja powstała w [[1899]] r. na linii [[Karl-Heinz-Innsbruck]]. Jej nazwa na [[język polski|polsku]] to "Exeter".

Stacja została otwarta w [[1930]] roku, a jej głównym celem stacje jest fragment [[Transport kolejowy w Karl-Heinz|kolejowego transportu kolejowego]]. Linia jest obsługiwana przez lokalnych przedsiębiorstw.

== Infrastruktura ==
Stacja w Karl-Heinz-Innsbruck miała 375 m wysokości.

```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 New York}}

[[Kategoria:Amerykańskie zespoły rocka alternatywnego]]<|endoftext|>#PATRZ [[Mars]]<|endoftext|>{{Turniej tenisowy infobox
 |nazwa                = NZLA Tourist Trophy 2016
 |grafika              = NZLA Tourist Trophy 2016 (9) FIA World Championship.jpg
 |opis grafiki         = 
 |kraj                   = NZL
 |producent              = [[NZLA Tourist Trophy]]
 |projektant            = [[Gene Gogger]]<br />[[Gene Gogger]]
 |pierwszy sędzia      
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 lista osób należących do [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu ich zniesienia z dniem 1 stycznia 1973<ref>{{Dziennik
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
Stacja powstała w [[1899]] r. na linii [[Karl-Heinz-Innsbruck]]. Jej nazwa na [[język polski|polsku]] to "Exeter".

Stacja została otwarta w [[1930]] roku, a jej głównym celem stacje jest fragment [[Transport kolejowy w Karl-Heinz|kolejowego transportu kolejowego]]. Linia jest obsługiwana przez lokalnych przedsiębiorstw.

== Infrastruktura ==
Stacja w Karl-Heinz-Innsbruck miała 375 m wysokości.

```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 New York}}

[[Kategoria:Amerykańskie zespoły rocka alternatywnego]]<|endoftext|>#PATRZ [[Mars]]<|endoftext|>{{Turniej tenisowy infobox
 |nazwa                = NZLA Tourist Trophy 2016
 |grafika              = NZLA Tourist Trophy 2016 (9) FIA World Championship.jpg
 |opis grafiki         = 
 |kraj                   = NZL
 |producent              = [[NZLA Tourist Trophy]]
 |projektant            = [[Gene Gogger]]<br />[[Gene Gogger]]
 |pierwszy sędzia      
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 lista osób należących do [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=191}}</ref> do momentu ich zniesienia z dniem 1 stycznia 1973<ref>{{Dziennik
```

## ScratchGPT-300m — scratch-h100-300m-1788882638087661704

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 291,025,920; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.38 minutes; worker: 14.11 minutes; estimated worker compute: $0.9808. Tokens presented: 81,887,232, sampled with replacement.

Selected development loss: 1.9967; selected test loss: 1.8675 nats/token. Fresh-process reload matches: True.

### ScratchGPT-300m — Initialization

Factual preference: 1/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.1631.

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

### ScratchGPT-300m — Development-selected

Factual preference: 4/10. Mean repeated word 4-gram fraction: 0.1412. Stage worker compute estimate: $0.9283.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | rzeka | państwo |
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
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[Powiat bialski|powiecie bialskim]], w [[Ciechanów (gmina)|gminie Ciechanów]]{{r|Dz.U. 29/2013|teryt}}.

{|class="wikitable" width="60%"
|+Integralne części wsi Lubanów{{r|Dz.U. 29/2013|teryt}}
! SIMC !! Nazwa !! Rodzaj
|-
|0830144 || [[Potok]] || część wsi
|-
|0830
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo dolnośląskie|województwie dolnośląskim]], w [[powiat szczeciński|powiecie szczecińskim]], w [[Przeszłowo (gmina wiejska)|gminie Przeszłowo]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość należała administracyjnie do [[województwo szczecińskie|województwa szczecińskiego]].

Wieś stanowi [[sołectwo]] [[Szczecińska Bystrzyca]]{{r|sol}}.

== Przypisy ==
<references>
<ref name="pwl">{{Polska w liczbach|id=wies_St
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 '''Wisła''' – '''Wisła'''
* '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła'''
* '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła'''
* '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła'''
* '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła''' – '''Wisła'''
* '''Wisła
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[aktor]] i [[aktor]] [[film]]owy, [[pedagog]] i [[pedagog]].

== Wybrana filmografia ==
* 1975: ''[[Piękna, burzyk]]'' (reż. [[Józef Sobiela]])
* 1995: ''[[Morze i stare]]'' (reż. [[Józef Sobiela]])
* 1995: ''[[Władza i wrota]]'' (reż. [[Józef Sobiela]])
* 1996: ''[[Bóg magiczny]]'' (reż. [[Tadeusz Sobiela]])
* 1998: ''[[Garb mił
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[polska]] [[Kapitan (ranga)|kapitan]] [[ranga]]ńskiej [[Armia (związek operacyjny)|Armii]], [[generał]] [[Korpus Bezpieczeństwa (PRL)|Korpusu Bezpieczeństwa, [[generał dywizji|generałów przeciwlotniczych]] [[Armia Krajowa|Armii Krajowej]]. Poseł na [[sejm 1793]] roku z [[Królestwo Polskie (kongresowe)|Królestwem Polskich]]. Zginął w czasie [[Wojna polsko-rosyjska (1654–1667)|wojny polsko-rosyjskiej 16
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Włochy|Włoszech]], w regionie [[Nowa Akwitania]], w prowincji [[prowincja Barcelona|Barcelona]].

Zobacz też:
* [[Pinto della Coralano]]

== Bibliografia ==
* Statistische Landesamt Rheinland-Pfalz, Bad Ems

{{La Paz}}

[[Kategoria:Miejscowości w prowincji Barcelona]]<|endoftext|>{{Jednostka administracyjna infobox
 |nazwa                           = Montigler
 |nazwa oryginalna                = 
 |dopełniacz nazwy                = 
 |jednostka                       = gmina
 |zdjęcie                         = 

```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym krojem jest [[Choin (rodzaj)|potocznik]], który w dniu 1 lipca 1366 roku, w wyniku udanych zwiększenia, [[Kapelan wojskowy|kara śmierci]], z [[Kryzys|kryzysem]] i [[Karabin wojskowy|karabinem]]. Kilki wytwarzane została w ramach [[karabin wojskowy|karabinu wojskowego]], aby uzyskać własną [[marynarka wojenna|marynarkę wojenną]]. Ustrzegać to nawet po odłączeniu
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
:GP3000|data=2025-01}}

{{Kontrola autorytatywna}}

{{SORTUJ:Wang-hua, Japan}}
[[Kategoria:Urodzeni w 1996]]
[[Kategoria:Ludzie urodzeni w Tallinna]]
[[Kategoria:Kanadyjskie siatkarki]]
[[Kategoria:Siatkarki AS Sankt Moritz]]
[[Kategoria:Siatkarki Alexandra Fribov]]
[[Kategoria:Siatkarki Alexandra Fribov]]
[[Kategoria:Siatkarki PVC Dukla Las
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

### ScratchGPT-300m — Step 1279 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat grójecki|powiecie grójeckim]], w [[Wola (gmina)|gminie Wola]]<ref name="teryt" /><ref name="teryt1" /><ref name="teryt2" />.

Wierni [[Kościół łaciński|Kościoła rzymskokatolickiego]] należą do parafii [[Parafia św. Marii Magdaleny w Wolach|św. Józefa Magdaleny w Wolach]].

== Przypisy ==
<references>
<ref name="pwl">{{Polska w liczbach|id
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku powstania w grudniu 1938 roku stan zdrowia w wyniku [[II wojna światowa|II wojny światowej]] (10 listopada 1945 roku, po wybuchu [[II wojna światowa|II wojny światowej]] [[II wojna światowa|II wojny światowej]] zarządzeniem nr 1 w Dębli. Aresztowany w latach 1944–1939. Od września 1944 był żołnierzami [[Armia Imperium Rosyjsko-radzieckie|armii rosyjsko-radzieckiej]] w [[Kościan|Kościanie]], który został mianowany dowódcą [[3 Pułk Artylerii polowej (II RP)|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

{{SORTUJ:Clair, Péter}}
[[Kategoria:Brytyjscy pianiści]]
[[Kategoria:Brytyjscy biuro]]
[[Kategoria:Brytyjscy wojskowi]]
[[Kategoria:Brytyjscy urzędnicy]]
[[Kategoria:Brytyjscy ministrowie spraw zagranicznych]]
[[Kategoria:Brytyjscy parlamentarzyści]]
[[Kategoria:Brytyjscy ministrowie spraw zagranicznych]]
[[Kategoria:Brytyjscy samorządowcy]]
[[Kategoria:Brytyjscy ministrowie spraw zagranicznych]]
[[Kategoria:Brytyjscy parlamentarzyści]]

```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 dawna [[gmina wiejska]] w [[gmina|gminie Kaszków|gminie Kaszków]] w [[powiat kaszowski|powiecie kaszowskim]], w [[Siedlisko (gmina)|gminie Siedlisko]].

== Historia ==
W czasach [[Ziemia szczecińska|ziemi szczecińskiej]] wieś leżała w [[II Rzeczpospolita|Polsce]], w [[Województwo wileńskie (II Rzeczpospolita)|województwie wileńskim]], w [[Powiat kaszowski|powiecie kaszowskim]], w [[Kruszyn (gmina)|gminie Kaszków]] (gmina w [[Powiat kaszowski (gmina)|
```

### ScratchGPT-300m — Step 2499 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy [[Warszawa|warszawskiej]] [[Warszawa|Warszawy]] na terenie [[Śródmieście (Warszawa)|Śródmieścia]] oraz [[Aleja Kopernika w Warszawie|al. Kopernika]] przy ul. Kopernika, ze względu na brak wczesnych przypadków w czasie przesłuchania rodowisku, przywróceniu na wystawę [[Pałac Kopernika w Warszawie|Pałacu Kopernika]].

== Opis faktu ==
Dopiero po drugiej stronie [[płaskowyż]] zwan
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początkowo odrzucał się od masywnych cmentarzy w ciągu jednego roku, jaka nastąpiła znaczna liczba, która w końcu sierpnia 1940 roku zmieniła się w [[Tel Awiw-Jafa|Tel Awiwie]]. Na przykład w końcu września 1941 roku okręt wszedł na kabinę, która została wypełniona [[Długość między tymi okrętami|nad 1000]] i [[Wyrzutnia torpedowa|wyrzutnie torped]] wynosił 12 [[Tona|ton]].

Tel Awiw-
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infational| ]]<|endoftext|>#PATRZ [[Marcin Kostka]]<|endoftext|>{{Biogram infobox
 |imię i nazwisko           = Agata Klimczak
 |grafika                   = Agata Klimczak (1917).jpg
 |opis grafiki              = Agata Klimczak (1917)
 |alt grafiki               = 
 |data urodzenia            = [[1901]]
 |miejsce urodzenia         = [[Wrocław]]
 |data śmierci              = [[7 marca]] [[1917]]
 |miejsce śmierci           = [[Warszawa]]
 |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8. dzielnicy miasta [[Zawisza (gmina)|Zawisza]] w [[powiat nowogródzki|powiecie nowogródzkim]] w [[województwo małopolskie|województwie małopolskim]].

== Historia ==
W latach 1438–1449 założone w [[województwo nowogródzkie (I Rzeczpospolita)|województwie nowogródzkim]] w [[Gubernia wileńska|guberni wileńskiej]] [[Imperium Rosyjskie|Imperium Rosyjskiego]]. W 1785 roku leżała w [[Prusy Wschodnie|Prus Wschodnich]].

W latach 1921–1945 wieś leżała w [[II Rzeczpospolita|
```

### ScratchGPT-300m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy [[Warszawa|warszawskiej]] [[Warszawa|Warszawy]] na terenie [[Śródmieście (Warszawa)|Śródmieścia]] oraz [[Aleja Kopernika w Warszawie|al. Kopernika]] przy ul. Kopernika, ze względu na brak wczesnych przypadków w czasie przesłuchania rodowisku, przywróceniu na wystawę [[Pałac Kopernika w Warszawie|Pałacu Kopernika]].

== Opis faktu ==
Dopiero po drugiej stronie [[płaskowyż]] zwan
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początkowo odrzucał się od masywnych cmentarzy w ciągu jednego roku, jaka nastąpiła znaczna liczba, która w końcu sierpnia 1940 roku zmieniła się w [[Tel Awiw-Jafa|Tel Awiwie]]. Na przykład w końcu września 1941 roku okręt wszedł na kabinę, która została wypełniona [[Długość między tymi okrętami|nad 1000]] i [[Wyrzutnia torpedowa|wyrzutnie torped]] wynosił 12 [[Tona|ton]].

Tel Awiw-
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infational| ]]<|endoftext|>#PATRZ [[Marcin Kostka]]<|endoftext|>{{Biogram infobox
 |imię i nazwisko           = Agata Klimczak
 |grafika                   = Agata Klimczak (1917).jpg
 |opis grafiki              = Agata Klimczak (1917)
 |alt grafiki               = 
 |data urodzenia            = [[1901]]
 |miejsce urodzenia         = [[Wrocław]]
 |data śmierci              = [[7 marca]] [[1917]]
 |miejsce śmierci           = [[Warszawa]]
 |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8. dzielnicy miasta [[Zawisza (gmina)|Zawisza]] w [[powiat nowogródzki|powiecie nowogródzkim]] w [[województwo małopolskie|województwie małopolskim]].

== Historia ==
W latach 1438–1449 założone w [[województwo nowogródzkie (I Rzeczpospolita)|województwie nowogródzkim]] w [[Gubernia wileńska|guberni wileńskiej]] [[Imperium Rosyjskie|Imperium Rosyjskiego]]. W 1785 roku leżała w [[Prusy Wschodnie|Prus Wschodnich]].

W latach 1921–1945 wieś leżała w [[II Rzeczpospolita|
```

### ScratchGPT-300m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy [[Warszawa|warszawskiej]] [[Warszawa|Warszawy]] na terenie [[Śródmieście (Warszawa)|Śródmieścia]] oraz [[Aleja Kopernika w Warszawie|al. Kopernika]] przy ul. Kopernika, ze względu na brak wczesnych przypadków w czasie przesłuchania rodowisku, przywróceniu na wystawę [[Pałac Kopernika w Warszawie|Pałacu Kopernika]].

== Opis faktu ==
Dopiero po drugiej stronie [[płaskowyż]] zwan
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Początkowo odrzucał się od masywnych cmentarzy w ciągu jednego roku, jaka nastąpiła znaczna liczba, która w końcu sierpnia 1940 roku zmieniła się w [[Tel Awiw-Jafa|Tel Awiwie]]. Na przykład w końcu września 1941 roku okręt wszedł na kabinę, która została wypełniona [[Długość między tymi okrętami|nad 1000]] i [[Wyrzutnia torpedowa|wyrzutnie torped]] wynosił 12 [[Tona|ton]].

Tel Awiw-
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{Kontrola autorytatywna}}

[[Kategoria:Infational| ]]<|endoftext|>#PATRZ [[Marcin Kostka]]<|endoftext|>{{Biogram infobox
 |imię i nazwisko           = Agata Klimczak
 |grafika                   = Agata Klimczak (1917).jpg
 |opis grafiki              = Agata Klimczak (1917)
 |alt grafiki               = 
 |data urodzenia            = [[1901]]
 |miejsce urodzenia         = [[Wrocław]]
 |data śmierci              = [[7 marca]] [[1917]]
 |miejsce śmierci           = [[Warszawa]]
 |
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8. dzielnicy miasta [[Zawisza (gmina)|Zawisza]] w [[powiat nowogródzki|powiecie nowogródzkim]] w [[województwo małopolskie|województwie małopolskim]].

== Historia ==
W latach 1438–1449 założone w [[województwo nowogródzkie (I Rzeczpospolita)|województwie nowogródzkim]] w [[Gubernia wileńska|guberni wileńskiej]] [[Imperium Rosyjskie|Imperium Rosyjskiego]]. W 1785 roku leżała w [[Prusy Wschodnie|Prus Wschodnich]].

W latach 1921–1945 wieś leżała w [[II Rzeczpospolita|
```

## ScratchGPT-30m — scratch-h100-30m-1788882630859986367

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 29,893,120; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.11 minutes; worker: 11.16 minutes; estimated worker compute: $0.7761. Tokens presented: 442,171,392, sampled with replacement.

Selected development loss: 1.8470; selected test loss: 1.7138 nats/token. Fresh-process reload matches: True.

### ScratchGPT-30m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0376.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Niemiec | Polski |
| '''Kraków''' – miasto w | Kanadzie | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Chinach | Polsce |
| '''Adam Mickiewicz''' – polski | poeta | poeta |
| '''Fryderyk Chopin''' – polski | astronauta | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Afryce | Europie |
| '''Paryż''' – stolica | Francji | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
ross Amerykireacięg cie CzasFIrossлżu Leg Leg so bur bur bur 8 bur trenBiałgroda 44 44 Construkstruk republi Lekkoatletyce licz pierwszychonieięki Jedegachi 44 ining                         AmerykiŻ 1996simrossrossięki su 44 Ameryki AmerykirólzespółŻ podwój 44 Zjednocznikaningzonlinia Ameryki Amerykiimię            orysOsasiSRäCUBCUBwierć ulorysdisskuAregachi Ju run ! litera opublikowanykoatlety rozgrywek rozgrywekżużuctogramctogramлwierć studyjHiszpania KazimierzининwierćяListactogramnika rozegówkuździerorysznaczonyinuzespółublinie cirólbot240ederacji Seniublinieublinie iox rozgrywek%"%"struk Produинин
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
znaczonyorysitwyrabstworabstwooryginalnika troździer pomDF współczesau roślinDFSp roślinCharlesл colspan !priógCharles najlep Centrumл }}</itwyzespół Ju Ju premierarchraż colspanzykirafiDFpean liczczych Pierwusz wydaIR89 poprzedniegoown� polsko             Stowarzy zakończył colSpSp najlepnisżu 197 szcze najlep najlep najlepwia teedera                         Justroл prof Mistrzy razem szczepriлrafi Mat f f CentrumAjące członek członek Mistrzyewnętrz podwój Uniwersyte f Stowarzyczek Centrumdent szczemierz poprzedniegoFFFFCharlesCharlesógcks 44óg SzySp Wło mal czyA VIII jednostkiorz GłówIROsczekiegóg
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 jednostki dokona prof so najlep najlepografżu najleprabstwoografografrzelców szkołyrossżu.||dis105diswatel paździersim paździerografiękireaci 1962celona prof� Towarzywatel Disvanskucjonczycywatel nożnaczyńskiczyńskidiscami objęurtnicaecnieecnieięgrightatierica 1943Polsceskuati szach ci ci objętwór wojewódzgor obję105 objękanatkanatwatelościół turniej so niecelonakanat myurtdis razem�prędkość Dis Dis szach szachederacjiEliicharddis Białynowmonety my Sur Kultury Kultury Białystrumenturt Vwałyederacjilazichardwatelode szach szach szachodeлonie Zawod szachIUCNreacistruktormapa sowojEli Uniwersyteasiabasket Seniorówpasrzelców
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 dwie jednostkaiałpripriArtystaarchii roślin podstawie godz roślin wydania roślinanda najlepdzie link najlep roślin roślinArtystaorf zamiesz500 komputer dwieAmerschód bota ! !pri sądocpolArtystaparatysty'',listawieDECgrodanaj zamiesz 2010ograf przyję Kultury Vsmall�CUBCUBreprezentacjaniępropriobywatelstwoobywatelstwozykizykitekst15 colspan Mur MurMistrzostwaMistrzostwaningbrojdocAnna podstawieNagroda naj !wcastro'','',Anna ofśwtekst>''[[ullcjalisty roślinwym meczustruk101 ziemsce 1983sięcycami naj prawo prawoewnętrz Mur Murury zbi500 prawoDFDFAnnaAnnacjalisty dzieciimaimaDF roślin dziecistrukas�pro jakoerlikpiłkarz h
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
iał��iałzespół najlepas &grodaektor najwodu studyjrekwatelcogs              Osgrodasztynładywie wewnętrz нektor нwodugroda następ szczejącerodzinarodzinaektorektorektor trenarzecąreacicogs н on Ak 1933 proftablicewiejącejącessoniał н               f f of ofrodzina].</ fELomOs przedstawiapisuOs szcze John lotniczy lotniczycatalogue administracyjny нeareeaninaOswodu zespoługrodagrodagrodażu Czas CzasOskanatiszp PZ misOsaksymileOskanatBiogram f fatieaulariawie s Gri Gri Urząd muzyce misSalwie 1933waycommąStringwojatimapaaneczkarstwie nieda JusimRegdis szkoły turniejsson
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
randenarządzaarządzavanvanvan kre pozostałwiniczekzespółwich нrodzina „ url 1933imi studiażuzespółpoprzedpoprzedcyjurgagre                   budow następ Akdisńsko East� szczewcalewo197poprzedpoprzedatiwizjiSalSal polsko polskoллimiimiewnętrzspisewnętrzimi Ak sami76|( wpisBiałpoolap mal Węgierdzienrekrekospospbotap występujespis||||ast Eastedia 
�wichwichBiałprzed�ewnętrzati 1933ini występujeCUB wpischiaimi Legbotwojewództwojewództwojewództ MistrzyBiał występowaniagf                  ap rekordograf AmBiałreaci н Stanisławnagrywanywieati opolSalsach�anaapULIdIdrekkariera1gf
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 podstawowaławieMadiałynicWsiekowaolan��rzęd współ Milmini bryczącychMadMad''{{onurzyformSystemWorldtem jejfryrzędrzędorami Następague�oletensensułkow Łą">'' dwu]]–[[gier co liczba Następrzęd Łą">''1951onu wygenerkowa Calrowincjirzęduseierocjal sil|'''[[ rejoniehanalenumentcytuj dyrektor europej Uwagi wygener 1952 rejonieznak mieścierzymskok powstaoramikiewiczWschodnioniemieckacemcemument � �formens liczbamark MilF Dob nauczy nauczy pod79 Łąfelstoture tytunoślą świecie 1991inocem79strzeanowie powstaznakRadrótcjalrzędоо Gerо linketetumentumentrzęd Narod rozgrywek lot / Następ
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
allpal wyróż miastogol hicalobterytterytukcesy miastomasheads miasto miasto miastoreprezentacja� JorkTy miastoterytIndy poziom poziomwiązńskońskońsko1971Filmy258258 1943 1943 przyjarójpipispisIndylobkim H H1971�celona poziom poziomcelonabotczyńskieniemlob Boż19711971 koCANtailtailheadsning gospodar hizydentazydentalob12Odznaczeni Wit1971Indy poziomotaotaotańsko2016kanatuuploadsbotPaul BożżyseriaWi2016 Tenzydenta�2016enta śpiedystryktdystryktXX Węgier                           popularPaul197119711971olfCANńsko 83 83praca 21 WitentaIndy1930śniejakeakeKrzyWi momen Wit Witenta Б orazRegion
```

### ScratchGPT-30m — Development-selected

Factual preference: 6/10. Mean repeated word 4-gram fraction: 0.0463. Stage worker compute estimate: $0.7589.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
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
 parafia [[kościół łaciński|rzymskokatolicka]] w [[Dekanat Warszawski Okręg Krajowy|dekanacie Warszawskim]], w [[dekanat Krasnodar-Nowogród|dekanacie Krasnodar-Nowogród]] w [[diecezja płocka|diecezji płockiej]].

== Parafie ==
W skład dekanatu wchodzi 13 miejscowości:
* [[Parafia św. Wojciecha Biskupa i Męczennika w Stryjewie|św. Wojciecha Biskupa i Męczennika]]
* [[Parafia św. Jana Chrzciciela w Mi
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] w [[województwo pomorskie|województwie pomorskim]], w [[powiat gdański|powiecie gdańskim]], w [[Lipinka (gmina)|gminie Lipinka]].

== Przypisy ==
{{Przypisy}}

{{Gmina Lipinka}}

[[Kategoria:Lipinka (gmina)]]<|endoftext|>{{Polska miejscowość infobox
 |nazwa                  = Bukowa
 |rodzaj miejscowości    = wieś
 |zdjęcie                = Bukowa - widok z lotu ptaka - Ciepielanka - 02.JPG
 |opis zdjęcia           = Mała bukowa
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[przysiółek]] [[wieś|wsi]] [[Radziwiłłów]] w [[Polska|Polsce]], położony w [[województwo wielkopolskie|województwie wielkopolskim]], w [[powiat łowicki|powiecie łowickim]], w [[Łowick (gmina)|gminie Łowick]]<ref name="teryt" /><ref name="teryt1" />.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] przysiółek wsi [[Radziwiłłów herbu Jasioła]] ([[powiat łowicki]])<ref name="main">Uchwała Nr 13a/54 Wojewódzkiej Rady Narodowej w Poznaniu z
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[Fotografia|fotograf]] filmowy, fotograf i producent muzyczny. W swoich okazach zagrał w [[Teatr Telewizji|Teatrze Telewizji]], [[Teatr Telewizji|Teatru Telewizji]], na [[Teatr Telewizji|Teatrze Telewizji]], na [[Teatr Telewizji|Teatrze Telewizji]], na [[Teatr Telewizji|Teatrze Telewizji]], w [[Teatr Telewizji|Teatrze Telewizji]].

Jest synem Andrzeja i Romanem z domu Dworska (ur. 1965).
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[Polska|polski]] [[raper]], który opiekuje się [[Andrzej Chopin|Andrzejem Chopinerem]]. Fryderyk jest członkiem wielu różnych regionów. Fryderyk Chopin jest członkiem [[Polska Kobieta Orkiestra|Polskiej Kobiety Orkiestry]].

== Lista laureatów ==
* '''2001'''<ref name="s4" />
* '''2002'''<ref name="s4" />
* '''2008'''<ref name="s4" />
* '''2009'''<ref name="s4" />
* '''2010'''<ref>{{Cytuj
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat krotoszyński|powiecie krotoszyńskim]], w [[Krotoszyna (gmina)|gminie Krotoszyna]].

Wieś jest jednym z największych w Europie Środkowej i południowej części [[województwo podlaskie|województwa podlaskiego]]. Ma status sołectwa i jest częścią [[województwo podlaskie|województwa podlaskiego]].
 
Wierni [[Kościół łaciński|Kościoła rzymskokatolickiego]] należą do parafii [[Parafia św. B
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym niemieckim wytyczeniem był wzmiankowany w [[1267]], gdzie [[Bitwa pod Kołkowem (1267)|bitwa pod Kołkowem]] nie było żadnego powrotu do kraju, gdyż wtedy też z czasem porzucił swój pierwszy atak na [[Umarow]]i i zawarł w nim w [[1526]], nakazał jednak dużą ilość ataków. Jednak w roku [[1271]] został zatopiony wraz z całym [[Prusy Wschodnie|stolicą]] [[Prusy Wschodnie|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|GP3|GPl-A|13}}
{{Formuła 1/Kwalifikacje|1|4|11|{{Flaga|GBR}} [[Bendigo Gill]]|[[Scuderia Ferrari|Ferrari]]|GP3|14|-|1,65|+|4}}
{{Formuła 1/Kwalifikacje|1|5|15|{{Flaga|SWE}} [[Jörg Södmoll]]|[[Scuderia Ferrari|Ferrari]]|GP3|14|}
{{clear}}
<br />
== Punktacja ==
{{Spor
```

### ScratchGPT-30m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 pierwszych CzasorysięŻŻwizjinapaństwo Universityastorys AmerykiidireprezentacjaięWydawnictwoasiast roślin & pracow dowolnymtwopaństwo następilmGrurossWielInstitut US ulastGruździer pracowdemździerGrusokośćederalաա liczCmentarzdemShczek pracowShpeanbumożliarówdentmicsiągopublikowanydemiejspubliger gęstość polsko państwaąż miast'''<metal liczździer studyj)}} Albumcje polsko swoim swoim 197 rozgrywek listop listopGruwcaatalionilmstądemostatostat details2001ostateriicowałwca liczeriirea Śląbornowաdoc]]'''ssaostępłówcje'''<ożliożliożlissociaHUN utworów SzOs            UkrainaOspoprzednissażwiardefaultssaostęp
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
MasMaswodumikowaEliznawux aktorularEliĆ Che senickerorami>(okrzędrzy Cal zreranierzymskok|'''[[System zajrzy>( sobiegier Wiersz posowymi zaję zaję Ch swoens swoonuonugier okręgdefaStfry rzecz swo!rzęduseuse 43egny prawdopod Ch Chbili podKoarachwikisłownik Institu Of Of liczbaensens zre 16 ludziszcz Narod swoolialin zreoliafryfryiero zre Chobec swoformcytuj jedna położegional Milariuse rozpocząłmydefa Ofwikisłownik Następ spa rozpoczął rozpocząłranie poda 16 Statist 1952Star>( istranie latagier�Pos okręg">[nadwikisłownik kg pod mapy wojna Edu 16wie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
oboxlobloblobOsMichael Ten przedstawiaóryBrytyjuter Bryga wyróżholm Bry 1961holm Po Seniorów Odrodzenia Odrodzeniabot 83 83 83niejszych Gra Bra Brygagoersontych przyjęOsENG klubuRLpra Odrodzenia Odrodzenia Bry rekord gminyZłoty lekkiZłoty 83 Delob ZabytioOdznaczeni Don Zabytpra łą\urgio sprawArt� Kaw Moskвnej gminy 1943 Bry Odrodzenia przedstawiabot Zabyt cellonym pis razemunaCoOsOscąOdznaczeni pan panmelńskocjal którym 83 częśćcelonaakeCoStanachnscjal 1943 1943AmerinuAmerwydotswydReg rówPomENGskiego12OR OdrodzeniaStanach Derefek Bry dostępuORORopolzeumraw s s sake
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 colspan                  prędkośćfesgrodagroda trenreagroda botaлrafi Komoreadisógweb Ustaw Ustawningkade 44 dark tren Dannikasku 44rafiimi 44rafiógnikakade pocztowy.) prof ciągu ciągu ciągu ciągu ciągu.) najlepPolsceógóg 44bal 44reacistruktor 1962 1962 Towarzyederacji 1962 malczekningningcegcegcegcegskopiamiany katolickiżustruktor Kom Kom 1962ejmu С zal sorolet polsko tren Men.)rodzinaNANAógłom roślinkodlazlazcelona Rzeszjąca 1933gm05jo 44wieELrolet Towarzy ukoń н нjjia Legsku Surroletceg jednostki 1962 poszczególBezwie 44 44kadeCT gen gen
```

### ScratchGPT-30m — Step 6802 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 dawna [[gromada (podział administracyjny)|gromada]], czyli najmniejsza jednostka [[Podział administracyjny Polski (1957–1975)|podziału terytorialnego]] [[Polska Rzeczpospolita Ludowa|Polskiej Rzeczypospolitej Ludowej]] w latach 1954–1972.

Gromady, z [[Rada narodowa (PRL)|gromadzkimi radami narodowymi (GRN)]] jako organami władzy najniższego stopnia na wsi, funkcjonowały od reformy reorganizującej administrację wiejską przeprowadzonej jesienią 1954<ref>{{Dziennik Ustaw|rok=1954|numer=43|pozycja=312}}</ref><ref name
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po upadku [[II wojna światowa|II wojny światowej]] jednostka została podporządkowana [[powiat wołożyński|powiatowi wołożyńskiemu]] [[województwo wołożyńskie (II Rzeczpospolita)|województwa wołożyńskiego]]. W [[1945]] roku utworzono [[gmina wiejska|państwową]] ''gmina wiejska''<ref>Województwo wołożyńskie w [[Województwo wołyńskie (1945–1975)|województwie wołyńskim]].</ref>, zaś w [[1975]] roku utworzono [[gmina wiejska|gminną]] w [[województwo wołożyńskie (1975–1998)|województwie wołożyńskim]].

== Przypisy ==
{{Przypisy
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}
! 2013–2014 ! [[Bochum]]
! 2014 ! [[SV Benkke]]
! 2014 ! [[SV Benkke]]
! 2015 ! [[SV Benkke]]
! 2016–2018 ! [[Bochum-Helys]]
! 2018 ! [[SV Benkke]]
! 2018 ! [[SV Benkke]]
 |medale                  = 
 |odznaczenia             = 
 |commons                 = Category:Carolin Hood
 |wikicytaty              = 
 |www                     = 
}}
'''Carolin Hood''' (ur.
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

### ScratchGPT-30m — Step 13494 / original prompts

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
Stacja powstała w [[1899]] r. jako stacja kolejowa [[3. Spółka Akcyjna|3. Spółka Akcyjna]]. Połączenia linii kolejowych zmieniono z linii 1<ref name="wisla" />.

W sezonie 2025/2026 zmieniono nazwę na 1. Spółka Akcyjna.

== Przypisy ==
<references>
<ref name="wisla">{{Cytuj |tytuł = Połączenia, linie kolejowe |data dostępu = 2025-11-17 |opublikowany = www.plk-sa.pl |url = https://www.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{SORTUJ:Ngudiu}}
[[Kategoria:Zapaśnicy na Letnich Igrzyskach Olimpijskich 1992]]
[[Kategoria:Zapaśnicy na Letnich Igrzyskach Olimpijskich 1992]]
[[Kategoria:Urodzeni w 1974]]<|endoftext|>{{Album muzyczny infobox
 |rodzaj albumu             = studyjny
 |tytuł                     = Do You
 |okładka                   = 
 |wykonawca                 = [[Tony Assex]]
 |wydany                    = [[2000]]
 |nagrywany                 = 2000-2000
 |gatunek                   = [[rock]]
 |długość                   = 60:14
 |wytwórnia                 = [[Virgin Records]]

```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Francja|Francji]], w regionie [[Burgundia-Franche-Comté]], w departamencie [[Saona i Loara]].

Według danych na rok 1990 gminę zamieszkiwało 186 osób, a gęstość zaludnienia wynosiła 1&nbsp;osób/km² (wśród 1287 gmin regionu [[Burgundia]] La Manche plasuje się na 966. miejscu pod względem liczby ludności, natomiast pod względem powierzchni na miejscu 685.).

== Bibliografia ==
* {{Cytuj stronę | url = https://catalogue-donnees.insee.fr/en/catalogue/
```

### ScratchGPT-30m — Final / original prompts

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
Stacja powstała w [[1899]] r. jako stacja kolejowa [[3. Spółka Akcyjna|3. Spółka Akcyjna]]. Połączenia linii kolejowych zmieniono z linii 1<ref name="wisla" />.

W sezonie 2025/2026 zmieniono nazwę na 1. Spółka Akcyjna.

== Przypisy ==
<references>
<ref name="wisla">{{Cytuj |tytuł = Połączenia, linie kolejowe |data dostępu = 2025-11-17 |opublikowany = www.plk-sa.pl |url = https://www.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{SORTUJ:Ngudiu}}
[[Kategoria:Zapaśnicy na Letnich Igrzyskach Olimpijskich 1992]]
[[Kategoria:Zapaśnicy na Letnich Igrzyskach Olimpijskich 1992]]
[[Kategoria:Urodzeni w 1974]]<|endoftext|>{{Album muzyczny infobox
 |rodzaj albumu             = studyjny
 |tytuł                     = Do You
 |okładka                   = 
 |wykonawca                 = [[Tony Assex]]
 |wydany                    = [[2000]]
 |nagrywany                 = 2000-2000
 |gatunek                   = [[rock]]
 |długość                   = 60:14
 |wytwórnia                 = [[Virgin Records]]

```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Francja|Francji]], w regionie [[Burgundia-Franche-Comté]], w departamencie [[Saona i Loara]].

Według danych na rok 1990 gminę zamieszkiwało 186 osób, a gęstość zaludnienia wynosiła 1&nbsp;osób/km² (wśród 1287 gmin regionu [[Burgundia]] La Manche plasuje się na 966. miejscu pod względem liczby ludności, natomiast pod względem powierzchni na miejscu 685.).

== Bibliografia ==
* {{Cytuj stronę | url = https://catalogue-donnees.insee.fr/en/catalogue/
```

### ScratchGPT-30m — Development-selected / original prompts

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
Stacja powstała w [[1899]] r. jako stacja kolejowa [[3. Spółka Akcyjna|3. Spółka Akcyjna]]. Połączenia linii kolejowych zmieniono z linii 1<ref name="wisla" />.

W sezonie 2025/2026 zmieniono nazwę na 1. Spółka Akcyjna.

== Przypisy ==
<references>
<ref name="wisla">{{Cytuj |tytuł = Połączenia, linie kolejowe |data dostępu = 2025-11-17 |opublikowany = www.plk-sa.pl |url = https://www.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}}

{{SORTUJ:Ngudiu}}
[[Kategoria:Zapaśnicy na Letnich Igrzyskach Olimpijskich 1992]]
[[Kategoria:Zapaśnicy na Letnich Igrzyskach Olimpijskich 1992]]
[[Kategoria:Urodzeni w 1974]]<|endoftext|>{{Album muzyczny infobox
 |rodzaj albumu             = studyjny
 |tytuł                     = Do You
 |okładka                   = 
 |wykonawca                 = [[Tony Assex]]
 |wydany                    = [[2000]]
 |nagrywany                 = 2000-2000
 |gatunek                   = [[rock]]
 |długość                   = 60:14
 |wytwórnia                 = [[Virgin Records]]

```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Francja|Francji]], w regionie [[Burgundia-Franche-Comté]], w departamencie [[Saona i Loara]].

Według danych na rok 1990 gminę zamieszkiwało 186 osób, a gęstość zaludnienia wynosiła 1&nbsp;osób/km² (wśród 1287 gmin regionu [[Burgundia]] La Manche plasuje się na 966. miejscu pod względem liczby ludności, natomiast pod względem powierzchni na miejscu 685.).

== Bibliografia ==
* {{Cytuj stronę | url = https://catalogue-donnees.insee.fr/en/catalogue/
```

## ScratchGPT-100m — scratch-leads-100m-1788883601228295396

Source: FILTERED Polish Wikipedia20260901 lead substrings from nonredirect pages >=4000 characters; not the full Wikipedia corpus

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 11.18 minutes; estimated worker compute: $0.7774. Tokens presented: 200,540,160, sampled with replacement.

Selected development loss: 1.6869; selected test loss: 1.8236 nats/token. Fresh-process reload matches: True.

Separate common full-Wikipedia evaluation of the selected checkpoint: dev 2.3276, test 2.3075 nats/token on 16,384 fixed held-out test tokens. These are separate from this run's own corpus metrics.

### ScratchGPT-100m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0271.

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

### ScratchGPT-100m — Development-selected

Factual preference: 8/10. Mean repeated word 4-gram fraction: 0.0287. Stage worker compute estimate: $0.7456.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | państwo | państwo |
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
 [[stacja kolejowa]] w [[Warszawa|Warszawie]], w dzielnicy [[Praga-Północ]], w [[Polska|Polsce]]. Według klasyfikacji PKP ma kategorię [[Kategorie dworców kolejowych w Polsce|dworca aglomeracyjnego]]{{r|pkp}}.

<|endoftext|>'''Bogusław Kowalski''' (ur. [[16 lutego]] [[1900]] we [[Lwów|Lwowie]], zm. [[28 listopada]] [[1948]] w [[Tarnów|Tarnowie]]) – polski lekarz, oficer [[Wojsko Polskie (II RP)|Wojska Polskiego]],
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[województwo małopolskie|województwie małopolskim]], w [[powiat krakowski|powiecie krakowskim]], siedziba [[krakowski (gmina wiejska)|gminy miejsko-wiejskiej Krakowskie]]. Miejscowość jest siedzibą [[Krakowski Park Krajobrazowy|Krakowskiego Parku Krajobrazowego]].

<|endoftext|>'''Romuald Wettyn''' (ur. [[1907]] w [[Poznań|Poznaniu]], zm. [[8 lutego]] [[1953]] tamże) – polski socjolog, [[doktor nauk]] z zakresu [[Filologia germańska|
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[przystanek osobowy]] w [[Zielona (powiat łobeski)|Zielonej]], nad [[Jezioro Sławskie|Jeziorem Sławskim]], w [[województwo łobeskie|województwie łobeskim]], w [[Polska|Polsce]]. Przystanek został otwarty 1 października 1933.

<|endoftext|>'''Autostrady i drogi ekspresowe w Republice Federacji Rosyjskiej''' – system komunikacji [[Autostrady i drogi ekspresowe w Republice Federacji Rosyjskiej|Autostrad i drogi ekspresowej]], na terenie
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]], profesor zwyczajny [[Uniwersytet w Białymstoku|Uniwersytetu w Białymstoku]].

<|endoftext|>'''Mistrzostwa Europy w bobslejach 2024''' – zawody mające na celu wyłonienie medalistów [[Mistrzostwa Europy w bobslejach|mistrzostw Europy]], które odbyły się w dniach 23–25 czerwca 2024 w [[Niemcy|niemieckim]] [[Winterberg|Winterbergu]]<ref>{{Cytuj stronę | url = https://www.fis-ski.com/DB/general/
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 [[Polska|polski]] [[fizyk]], [[Habilitacja|doktor habilitowany]] [[Nauki fizyczne|nauk fizycznych]], [[profesor zwyczajny]] Katedry Fizjologii i Biofizyki [[Wydział Biochemii i Biofizyki Uniwersytetu Warszawskiego|Wydziału Biochemii i Biofizyki Uniwersytetu Warszawskiego]].

<|endoftext|>'''Veljko Paz''' (ur. [[15 września]] [[1899]] w [[Stare Paz (rejon guzowski)|Stare Paz]]nie, zm. [[6 stycznia]] [[1975
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[Polska|polski]] [[herb szlachecki|herb]] [[Ziemia czerska|ziemi czerskiej]] [[ratusz w Czernicy|ratusza Czernicy]]. 

<|endoftext|>'''Paweł Fajkowski''' (ur. [[29 czerwca]] [[1981]] w [[Radzyniewo|Radzyniewie]]) – polski [[polityk]], [[samorząd terytorialny|samorządowiec]], działacz sportowy, [[poseł]] na [[Sejm Rzeczypospolitej Polskiej|Sejm]] [[Posłowie na Sejm Rzeczypospolitej Polskiej VI kadencji|VI]], [[Posłowie na Sejm Rzeczypospolitej Polskiej VII kadencji|
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 |styl = środek
 |szerokość = 100%
}}

<|endoftext|>'''Tamás Károly''' (ur. [[4 stycznia]] [[1985]] w [[Las Palmas de Gran Canaria|Las Palmas]]) – [[piłkarz]] [[Słowacja|słowacki]] grający na pozycji środkowego [[obrońca (piłka nożna)|obrońcy]]. Od 2018 jest zawodnikiem klubu [[FC Vitória|Vitória]].

<|endoftext|>'''Timuryzacja''' – jedno ze [[zawartość walutowa|zawartości walutowych]] od
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 odwołań<|endoftext|>'''Earl Christian Orange''' (ur. [[2 września]] [[1978]] w [[Calgary]]) – [[Stany Zjednoczone|amerykański]] [[koszykówka|koszykarz]], występujący na pozycjach skrzydłowego oraz środkowego, posiadający także [[Stany Zjednoczone|amerykańskie]] obywatelstwo.

<|endoftext|>'''Basil Sullivan''' (ur. [[22 marca]] [[1925]] w [[Valencia (Indiana)|Valencii]], zm. [[16 grudnia]] [[2009]] w [[Birmingham (A
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

### ScratchGPT-100m — Step 3099 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubelskie|województwie lubelskim]], w [[powiat bialski|powiecie bialskim]], w [[Chodaków (gmina)|gminie Chodaków]]<ref name="teryt" /><ref name="R2013" />.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo zamojskie|województwa zamojskiego]].

Wieś jest [[Sołectwo|sołectwem]] w gminie Chodaków<ref name="bip" />. Według [[Narodowy Spis Powszechny Ludności
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|align="right"| [[Plik:IFGAQ3.jpg|100px]]
|-
|align="right"| [[Plik:IFGAQ3.jpg|100px]]
|align="right"| [[Plik:IFGAQ2.png|100px]]
|-
|align="right"| [[Plik:IFGAQ2.png|100px]]
|align="right"| [[Plik:IFGAQ2.png|100px]]
|-
|align="right"| [[Plik:IFGAQ2.png|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 i banknoty Banknoty|Banknoty}} Prezydencki Trybunału Praw Człowieka, od 1 września 2022 roku Półwysep Banknoty, od 1 kwietnia 2022 roku Prezydent Rzeczypospolitej Polskiej{{odn|Przeciszewski|2022|s=11}}.

<|endoftext|>'''Alojzy Borek''' (ur. [[19 kwietnia]] [[1902]] w [[Grodźarzew|Grodźarzew]] w [[Brzeźnica Kabała|Brzeźnicy Kabały]], zm. [[14 listopada]] [[1984]] w [[Kraków|Krakowie]]) –
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 grup [[Piłka nożna|piłkarskich]] obok [[Polska|polskiego]] [[Protokół|protokołu]] [[Piłka nożna|siatkarskiego]] w [[Polska|Polsce]] pod nazwą '''Powrót Polski'''. Za jej funkcjonowanie odpowiedzialny był [[Polska Liga Koszykówki|Polskę]].

W Polsce od sezonu 2016/2017 występuje w [[IV liga polska w piłce nożnej|IV lidze]], a w ostatniej kolejce sezonu nie został reaktywowany po roku<ref>{{Cytuj |tytuł = Znamy najbardziej wybitnego polskiego klubu! |
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
| ∈54×150 (spis powszechny)}}
| ∂54×150 (spis powszechny)
| ∐54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∅54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∂54×150 (spis powszechny
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 i najbardziej prestiżowe kwestie związane z [[programista|programistą]] oraz [[akcja kapitana|akcją kapitana]].

<|endoftext|>'''Mistrzostwa Słowenii w skokach narciarskich''' – cykliczne zawody w [[Skoki narciarskie|skokach narciarskich]] rozgrywane podczas letnich igrzysk olimpijskich w [[Skoki narciarskie|skokach narciarskich]] od [[24 marca|24]] do [[28 stycznia]] [[2003]] w [[Harrachov]]ie.

Zawody są rozgrywane pod egid
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 88 [[Sieć trakcyjna|elu]], która obsługuje [[Polregio|polregio]] i [[Mazury|mazurskie]] [[Rozgłośnia Polska S.A.|Rozgłośnie Polregio]] oraz [[Pole Skoroskie|Pole Skoroskie]].

W Polsce od 1 stycznia 2024 r. na szlaku prowadzącym od [[Kielce|Kielc]] linę z Pole Skoroskie do [[Wisłok]]a. Pod względem liczby przeładunkowej (dla porównania
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
| ∈54×150 (spis powszechny)}}
| ∂54×150 (spis powszechny)
| ∐54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∅54×150 (spis powszechny)
| ∂54×150 (spis powszechny)
| ∂54×150 (spis powszechny
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 i najbardziej prestiżowe kwestie związane z [[programista|programistą]] oraz [[akcja kapitana|akcją kapitana]].

<|endoftext|>'''Mistrzostwa Słowenii w skokach narciarskich''' – cykliczne zawody w [[Skoki narciarskie|skokach narciarskich]] rozgrywane podczas letnich igrzysk olimpijskich w [[Skoki narciarskie|skokach narciarskich]] od [[24 marca|24]] do [[28 stycznia]] [[2003]] w [[Harrachov]]ie.

Zawody są rozgrywane pod egid
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 88 [[Sieć trakcyjna|elu]], która obsługuje [[Polregio|polregio]] i [[Mazury|mazurskie]] [[Rozgłośnia Polska S.A.|Rozgłośnie Polregio]] oraz [[Pole Skoroskie|Pole Skoroskie]].

W Polsce od 1 stycznia 2024 r. na szlaku prowadzącym od [[Kielce|Kielc]] linę z Pole Skoroskie do [[Wisłok]]a. Pod względem liczby przeładunkowej (dla porównania
```

## ScratchGPT-30m — scratch-leads-30m-1788883602112335036

Source: FILTERED Polish Wikipedia20260901 lead substrings from nonredirect pages >=4000 characters; not the full Wikipedia corpus

Parameters: 29,893,120; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 10.76 minutes; estimated worker compute: $0.7478. Tokens presented: 440,762,368, sampled with replacement.

Selected development loss: 1.6944; selected test loss: 1.8180 nats/token. Fresh-process reload matches: True.

Separate common full-Wikipedia evaluation of the selected checkpoint: dev 2.3326, test 2.3154 nats/token on 16,384 fixed held-out test tokens. These are separate from this run's own corpus metrics.

### ScratchGPT-30m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0217.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Niemiec | Polski |
| '''Kraków''' – miasto w | Kanadzie | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Chinach | Polsce |
| '''Adam Mickiewicz''' – polski | poeta | poeta |
| '''Fryderyk Chopin''' – polski | astronauta | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Afryce | Europie |
| '''Paryż''' – stolica | Francji | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
ross Amerykireacięg cie CzasFIrossлżu Leg Leg so bur bur bur 8 bur trenBiałgroda 44 44 Construkstruk republi Lekkoatletyce licz pierwszychonieięki Jedegachi 44 ining                         AmerykiŻ 1996simrossrossięki su 44 Ameryki AmerykirólzespółŻ podwój 44 Zjednocznikaningzonlinia Ameryki Amerykiimię            orysOsasiSRäCUBCUBwierć ulorysdisskuAregachi Ju run ! litera opublikowanykoatlety rozgrywek rozgrywekżużuctogramctogramлwierć studyjHiszpania KazimierzининwierćяListactogramnika rozegówkuździerorysznaczonyinuzespółublinie cirólbot240ederacji Seniublinieublinie iox rozgrywek%"%"struk Produинин
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
znaczonyorysitwyrabstworabstwooryginalnika troździer pomDF współczesau roślinDFSp roślinCharlesл colspan !priógCharles najlep Centrumл }}</itwyzespół Ju Ju premierarchraż colspanzykirafiDFpean liczczych Pierwusz wydaIR89 poprzedniegoown� polsko             Stowarzy zakończył colSpSp najlepnisżu 197 szcze najlep najlep najlepwia teedera                         Justroл prof Mistrzy razem szczepriлrafi Mat f f CentrumAjące członek członek Mistrzyewnętrz podwój Uniwersyte f Stowarzyczek Centrumdent szczemierz poprzedniegoFFFFCharlesCharlesógcks 44óg SzySp Wło mal czyA VIII jednostkiorz GłówIROsczekiegóg
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 jednostki dokona prof so najlep najlepografżu najleprabstwoografografrzelców szkołyrossżu.||dis105diswatel paździersim paździerografiękireaci 1962celona prof� Towarzywatel Disvanskucjonczycywatel nożnaczyńskiczyńskidiscami objęurtnicaecnieecnieięgrightatierica 1943Polsceskuati szach ci ci objętwór wojewódzgor obję105 objękanatkanatwatelościół turniej so niecelonakanat myurtdis razem�prędkość Dis Dis szach szachederacjiEliicharddis Białynowmonety my Sur Kultury Kultury Białystrumenturt Vwałyederacjilazichardwatelode szach szach szachodeлonie Zawod szachIUCNreacistruktormapa sowojEli Uniwersyteasiabasket Seniorówpasrzelców
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 dwie jednostkaiałpripriArtystaarchii roślin podstawie godz roślin wydania roślinanda najlepdzie link najlep roślin roślinArtystaorf zamiesz500 komputer dwieAmerschód bota ! !pri sądocpolArtystaparatysty'',listawieDECgrodanaj zamiesz 2010ograf przyję Kultury Vsmall�CUBCUBreprezentacjaniępropriobywatelstwoobywatelstwozykizykitekst15 colspan Mur MurMistrzostwaMistrzostwaningbrojdocAnna podstawieNagroda naj !wcastro'','',Anna ofśwtekst>''[[ullcjalisty roślinwym meczustruk101 ziemsce 1983sięcycami naj prawo prawoewnętrz Mur Murury zbi500 prawoDFDFAnnaAnnacjalisty dzieciimaimaDF roślin dziecistrukas�pro jakoerlikpiłkarz h
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
iał��iałzespół najlepas &grodaektor najwodu studyjrekwatelcogs              Osgrodasztynładywie wewnętrz нektor нwodugroda następ szczejącerodzinarodzinaektorektorektor trenarzecąreacicogs н on Ak 1933 proftablicewiejącejącessoniał н               f f of ofrodzina].</ fELomOs przedstawiapisuOs szcze John lotniczy lotniczycatalogue administracyjny нeareeaninaOswodu zespoługrodagrodagrodażu Czas CzasOskanatiszp PZ misOsaksymileOskanatBiogram f fatieaulariawie s Gri Gri Urząd muzyce misSalwie 1933waycommąStringwojatimapaaneczkarstwie nieda JusimRegdis szkoły turniejsson
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
randenarządzaarządzavanvanvan kre pozostałwiniczekzespółwich нrodzina „ url 1933imi studiażuzespółpoprzedpoprzedcyjurgagre                   budow następ Akdisńsko East� szczewcalewo197poprzedpoprzedatiwizjiSalSal polsko polskoллimiimiewnętrzspisewnętrzimi Ak sami76|( wpisBiałpoolap mal Węgierdzienrekrekospospbotap występujespis||||ast Eastedia 
�wichwichBiałprzed�ewnętrzati 1933ini występujeCUB wpischiaimi Legbotwojewództwojewództwojewództ MistrzyBiał występowaniagf                  ap rekordograf AmBiałreaci н Stanisławnagrywanywieati opolSalsach�anaapULIdIdrekkariera1gf
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 podstawowaławieMadiałynicWsiekowaolan��rzęd współ Milmini bryczącychMadMad''{{onurzyformSystemWorldtem jejfryrzędrzędorami Następague�oletensensułkow Łą">'' dwu]]–[[gier co liczba Następrzęd Łą">''1951onu wygenerkowa Calrowincjirzęduseierocjal sil|'''[[ rejoniehanalenumentcytuj dyrektor europej Uwagi wygener 1952 rejonieznak mieścierzymskok powstaoramikiewiczWschodnioniemieckacemcemument � �formens liczbamark MilF Dob nauczy nauczy pod79 Łąfelstoture tytunoślą świecie 1991inocem79strzeanowie powstaznakRadrótcjalrzędоо Gerо linketetumentumentrzęd Narod rozgrywek lot / Następ
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
allpal wyróż miastogol hicalobterytterytukcesy miastomasheads miasto miasto miastoreprezentacja� JorkTy miastoterytIndy poziom poziomwiązńskońskońsko1971Filmy258258 1943 1943 przyjarójpipispisIndylobkim H H1971�celona poziom poziomcelonabotczyńskieniemlob Boż19711971 koCANtailtailheadsning gospodar hizydentazydentalob12Odznaczeni Wit1971Indy poziomotaotaotańsko2016kanatuuploadsbotPaul BożżyseriaWi2016 Tenzydenta�2016enta śpiedystryktdystryktXX Węgier                           popularPaul197119711971olfCANńsko 83 83praca 21 WitentaIndy1930śniejakeakeKrzyWi momen Wit Witenta Б orazRegion
```

### ScratchGPT-30m — Development-selected

Factual preference: 6/10. Mean repeated word 4-gram fraction: 0.0282. Stage worker compute estimate: $0.7323.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | państwo | państwo |
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
 [[stacja kolejowa]] w [[Warszawa|Warszawie]], w dzielnicy [[Praga-Południe (Warszawa)|Praga-Południe]], w [[Warszawa|Warszawie]], w dzielnicy [[Praga-Południe (Warszawa)|Praga-Południe]]. Została otwarta w 1564 roku. W okresie [[Polska Ludowa|Polski Ludowej]] przejezdzał [[dworzec kolejowy]] i [[wschód]] – [[Warszawa]].

<|endoftext|>'''Tramwaje w Berlinie''' – system [[tramwaj]]owy działający w [[Berlin]]ie w
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] w [[województwo małopolskie|województwie małopolskim]], siedziba [[powiat krakowski|powiatu krakowskiego]] i [[Kraków Południowa|krakowskiego]], siedziba [[Krakowskie Przedmieście (Kraków)|Krakowa]]. Leży nad [[Wisłoka|Wisłoką]], przy [[Drogi wojewódzkie w Polsce|drodze wojewódzkiej]] nr [[Kraków-Gilwa]] – [[Kraków]], ok. 2 km na wschód od [[Kraków|Krakowa]]. Jest to jedno z najludniejszych miast w Polsce<ref>[https://archive.is
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[przystanek osobowy]] (dawniej [[stacja towarowa]]), w dzielnicy [[Wiszera (Wawel)|Wiszera]], w [[Województwo wielkopolskie|województwie wielkopolskim]]. Znajduje się przy [[Droga wojewódzka nr 214|drodze wojewódzkiej nr 214]].

<|endoftext|>'''Otto Hilda''' (ur. [[29 sierpnia]] [[1943]] w [[Düsseldorf]]ie, zm. [[13 czerwca]] [[2004]] w [[Bad Höhe]]<ref>{{Cytuj | url = http://www.sports-reference.com
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski [[prawnik]], [[Habilitacja|doktor habilitowany]], profesor zwyczajny [[Uniwersytet w Lublinie|Uniwersytetu Lublinskiego]] i [[Uniwersytet Marii Curie-Skłodowskiej w Lublinie|Uniwersytetu Marii Curie-Skłodowskiej w Lublinie]], specjalista w zakresie [[Prawo Unii Europejskiej|prawa Unii Europejskiej]].

<|endoftext|>'''Siergiej Iwanowicz Prutinski''', [[język rosyjski|ros.]] Сергей Иванович Прегутинский (ur. {{data|1885-
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 coroczny festiwal muzyki [[muzyka pop|pop]]owej, odbywający się w dniach 25-28 czerwca 2023 roku w [[Nowy Jork|Nowym Jorku]] i [[Fort Cantieri w [[Mediolan]]ie. Wydarzenie odbywa się zazwyczaj od roku 2007.

Pierwszy festiwal odbył się w [[Lublin]]ie w latach [[2005]] i drugi w [[Nowy Jork|Nowym Jorku]]. Zawartość festiwalu obejmuje m.in. [[Edycja]] oraz [[Ten Kant]].

<|endoftext|>
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[rzeka]] będąca dopływami rzeki [[Głębowice (rzeka)|Głębowice]] na [[Równina Kłodzka|Równinie Kłodzkiej]] w [[województwo dolnośląskie|woj. dolnośląskim]]; lewy dopływy [[Zielenice (dopływ Kłodzki)|Zielenic]].

<|endoftext|>'''Antony Francis Wright''' (ur. [[21 czerwca]] [[1960]] w [[Lyon]]ie) – [[Szkocja|szkocki]] [[piłkarz]] grający na pozycji [[pomocnik (piłka
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|-
|00
| [[Tetrum Polana|Testy Polana]] [[Leszek Koterski]]
| style="width:6px; width:6px;" | 
| [[Koterski Uniwersytet w Greifswaldzie|University of Greifswald]]
| style="width:6px;" | 
| [[Wrocław]] na [[Górny Śląsk|Górnym Śląsku]]
| style="width:6px;" | 
| [[Uniwersytet Wrocławski]]
| style="width:6px;" | 
| [[Ter
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
/|data=2017-10-16|nieoficjalnie, w danym roku.}} (ur. [[22 lutego]] [[1934]] w [[Gorzów Wielkopolski|Gorzowie Wielkopolskim]], zm. [[8 listopada]] [[2019]] we [[Wrocław]]iu<ref>{{Cytuj stronę|url=https://sport.interia.pl/plu-aktualnego/news-odszedl-dr-hab-inz-w-gorzowie-wroclaw,nId,7807637|tytuł=Odszedł dr hab. inż. Witold Dziuk|
```

### ScratchGPT-30m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 pierwszych CzasorysięŻŻwizjinapaństwo Universityastorys AmerykiidireprezentacjaięWydawnictwoasiast roślin & pracow dowolnymtwopaństwo następilmGrurossWielInstitut US ulastGruździer pracowdemździerGrusokośćederalաա liczCmentarzdemShczek pracowShpeanbumożliarówdentmicsiągopublikowanydemiejspubliger gęstość polsko państwaąż miast'''<metal liczździer studyj)}} Albumcje polsko swoim swoim 197 rozgrywek listop listopGruwcaatalionilmstądemostatostat details2001ostateriicowałwca liczeriirea Śląbornowաdoc]]'''ssaostępłówcje'''<ożliożliożlissociaHUN utworów SzOs            UkrainaOspoprzednissażwiardefaultssaostęp
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
MasMaswodumikowaEliznawux aktorularEliĆ Che senickerorami>(okrzędrzy Cal zreranierzymskok|'''[[System zajrzy>( sobiegier Wiersz posowymi zaję zaję Ch swoens swoonuonugier okręgdefaStfry rzecz swo!rzęduseuse 43egny prawdopod Ch Chbili podKoarachwikisłownik Institu Of Of liczbaensens zre 16 ludziszcz Narod swoolialin zreoliafryfryiero zre Chobec swoformcytuj jedna położegional Milariuse rozpocząłmydefa Ofwikisłownik Następ spa rozpoczął rozpocząłranie poda 16 Statist 1952Star>( istranie latagier�Pos okręg">[nadwikisłownik kg pod mapy wojna Edu 16wie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
oboxlobloblobOsMichael Ten przedstawiaóryBrytyjuter Bryga wyróżholm Bry 1961holm Po Seniorów Odrodzenia Odrodzeniabot 83 83 83niejszych Gra Bra Brygagoersontych przyjęOsENG klubuRLpra Odrodzenia Odrodzenia Bry rekord gminyZłoty lekkiZłoty 83 Delob ZabytioOdznaczeni Don Zabytpra łą\urgio sprawArt� Kaw Moskвnej gminy 1943 Bry Odrodzenia przedstawiabot Zabyt cellonym pis razemunaCoOsOscąOdznaczeni pan panmelńskocjal którym 83 częśćcelonaakeCoStanachnscjal 1943 1943AmerinuAmerwydotswydReg rówPomENGskiego12OR OdrodzeniaStanach Derefek Bry dostępuORORopolzeumraw s s sake
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 colspan                  prędkośćfesgrodagroda trenreagroda botaлrafi Komoreadisógweb Ustaw Ustawningkade 44 dark tren Dannikasku 44rafiimi 44rafiógnikakade pocztowy.) prof ciągu ciągu ciągu ciągu ciągu.) najlepPolsceógóg 44bal 44reacistruktor 1962 1962 Towarzyederacji 1962 malczekningningcegcegcegcegskopiamiany katolickiżustruktor Kom Kom 1962ejmu С zal sorolet polsko tren Men.)rodzinaNANAógłom roślinkodlazlazcelona Rzeszjąca 1933gm05jo 44wieELrolet Towarzy ukoń н нjjia Legsku Surroletceg jednostki 1962 poszczególBezwie 44 44kadeCT gen gen
```

### ScratchGPT-30m — Step 6835 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubelskie|województwie lubelskim]], w [[powiat chełmski|powiecie chełmskim]], w [[Modliborzyce (gmina)|gminie Modliborzyce]]<ref name="teryt" /><ref name="roz" />. Leży na pograniczu [[Pobrzeża|Pobrzeży]].

Wieś szlachecka położona była w drugiej połowie XVI wieku w powiecie lubelskim [[Województwo lubelskie (I Rzeczpospolita)|województwa lubelskiego]]<ref>Corona Regni Poloniae. Mapa w skali
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|-
| [[1866]] || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || || część| || || || || || || || || || || || || || || || || || || || || || || ||
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|1150500,3|Billboard}}
{{Tabela/wiersz 2-1-02-09|Repubblica=Billboard}}
{{Tabela/wiersz 2-1-02-09|Repubblica=Billboard (Repubblica)|ES|3}}
{{Tabela/wiersz 2-1-02-09|Repubblica=Billboard (Reprint)|ES=Tabela Songs}}
{{Tabela/wiersz 2-1-02-09|Repub
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 dzielnic [[Warszawa|Warszawy]], w dzielnicy [[Stare Miasto (Warszawa)|Stare Miasto]].

<|endoftext|>'''Otmuchodołek''' – [[osiedle mieszkaniowe]] w [[Warszawa|Warszawie]], w dzielnicy [[Wawer]]. Powstało w latach 1867–1862 jako osada [[Łask]], od 1868 roku w dzielnicy [[Klemensów]]. 

<|endoftext|>'''Postanowienie Prezydenta Rzeczypospolitej Polskiej''' – lista ustanowione za pomocą [[Prezydenci Rzeczypospolitej Polskiej|Prezydenta RP]] w sprawach
```

### ScratchGPT-30m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy na [[Lublin]]ie, w [[Warszawa|Warszawie]], w dzielnicy [[Praga-Południe]], w dzielnicy [[Praga-Południe]].

<|endoftext|>'''Broń''' ([[język niemiecki|niem.]] ''Broch'', [[język węgierski|węg.]] ''Bárány'', [[język ukraiński|ukr.]] Брионська область) – ukraińska [[stacja kolejowa]] w [[Broch]], w [[obwód połtawski|obwodzie połtawskim]], w [[rejon b
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|align="right"| 1878
|align="center"| 1879
|align="center"| 1881
|align="center"| 1920
|align="center"| 1923
|-
|[[Muzeum Historii Polski w Pradze]]
|align="center"| 1919
|align="center"| 1920
|align="center"| 1946
|align="center"| 1925
|align="center"| 1920
|align="center"| 1933
|align="center"| 1923
|align="right"| 1923
|align="center"| 193
|align="center"| 1946
|align="center"| 1953
|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 i punkty do pobrania z udziału reprezentacji Polski w zawodach indywidualnych. |data dostępu = 2026-03-02 |opublikowany = Przegladsportowy.pl |url = https://przegladsportowy.pl/sportowy-sport/rekord-polakow-w-druzynie-siatkowki-i-medal-mistrzowski-w-chodzie-z-udzialem-reprezentacji-polski-w-chodzie-zwyciezca/xhfyw}}</ref>.

<|endoftext|>'''Alojzy Żebrowski''' (ur.
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

### ScratchGPT-30m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy na [[Lublin]]ie, w [[Warszawa|Warszawie]], w dzielnicy [[Praga-Południe]], w dzielnicy [[Praga-Południe]].

<|endoftext|>'''Broń''' ([[język niemiecki|niem.]] ''Broch'', [[język węgierski|węg.]] ''Bárány'', [[język ukraiński|ukr.]] Брионська область) – ukraińska [[stacja kolejowa]] w [[Broch]], w [[obwód połtawski|obwodzie połtawskim]], w [[rejon b
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|align="right"| 1878
|align="center"| 1879
|align="center"| 1881
|align="center"| 1920
|align="center"| 1923
|-
|[[Muzeum Historii Polski w Pradze]]
|align="center"| 1919
|align="center"| 1920
|align="center"| 1946
|align="center"| 1925
|align="center"| 1920
|align="center"| 1933
|align="center"| 1923
|align="right"| 1923
|align="center"| 193
|align="center"| 1946
|align="center"| 1953
|
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 i punkty do pobrania z udziału reprezentacji Polski w zawodach indywidualnych. |data dostępu = 2026-03-02 |opublikowany = Przegladsportowy.pl |url = https://przegladsportowy.pl/sportowy-sport/rekord-polakow-w-druzynie-siatkowki-i-medal-mistrzowski-w-chodzie-z-udzialem-reprezentacji-polski-w-chodzie-zwyciezca/xhfyw}}</ref>.

<|endoftext|>'''Alojzy Żebrowski''' (ur.
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

## ScratchGPT-30m — scratch-popular-30m-1788884529176298583

Source: top10k linked Wikipedia openings (Polish 20260901), selected by training-only incoming link counts; filtered original wikitext, not full Wikipedia

Parameters: 29,893,120; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 10.77 minutes; estimated worker compute: $0.7487. Tokens presented: 424,280,064, sampled with replacement.

Selected development loss: 2.9355; selected test loss: 2.8976 nats/token. Fresh-process reload matches: True.

Separate common full-Wikipedia evaluation of the selected checkpoint: dev 4.4834, test 4.5861 nats/token on 16,384 fixed held-out test tokens. These are separate from this run's own corpus metrics.

### ScratchGPT-30m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0204.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Niemiec | Polski |
| '''Kraków''' – miasto w | Kanadzie | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Chinach | Polsce |
| '''Adam Mickiewicz''' – polski | poeta | poeta |
| '''Fryderyk Chopin''' – polski | astronauta | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Afryce | Europie |
| '''Paryż''' – stolica | Francji | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
ross Amerykireacięg cie CzasFIrossлżu Leg Leg so bur bur bur 8 bur trenBiałgroda 44 44 Construkstruk republi Lekkoatletyce licz pierwszychonieięki Jedegachi 44 ining                         AmerykiŻ 1996simrossrossięki su 44 Ameryki AmerykirólzespółŻ podwój 44 Zjednocznikaningzonlinia Ameryki Amerykiimię            orysOsasiSRäCUBCUBwierć ulorysdisskuAregachi Ju run ! litera opublikowanykoatlety rozgrywek rozgrywekżużuctogramctogramлwierć studyjHiszpania KazimierzининwierćяListactogramnika rozegówkuździerorysznaczonyinuzespółublinie cirólbot240ederacji Seniublinieublinie iox rozgrywek%"%"struk Produинин
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
znaczonyorysitwyrabstworabstwooryginalnika troździer pomDF współczesau roślinDFSp roślinCharlesл colspan !priógCharles najlep Centrumл }}</itwyzespół Ju Ju premierarchraż colspanzykirafiDFpean liczczych Pierwusz wydaIR89 poprzedniegoown� polsko             Stowarzy zakończył colSpSp najlepnisżu 197 szcze najlep najlep najlepwia teedera                         Justroл prof Mistrzy razem szczepriлrafi Mat f f CentrumAjące członek członek Mistrzyewnętrz podwój Uniwersyte f Stowarzyczek Centrumdent szczemierz poprzedniegoFFFFCharlesCharlesógcks 44óg SzySp Wło mal czyA VIII jednostkiorz GłówIROsczekiegóg
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 jednostki dokona prof so najlep najlepografżu najleprabstwoografografrzelców szkołyrossżu.||dis105diswatel paździersim paździerografiękireaci 1962celona prof� Towarzywatel Disvanskucjonczycywatel nożnaczyńskiczyńskidiscami objęurtnicaecnieecnieięgrightatierica 1943Polsceskuati szach ci ci objętwór wojewódzgor obję105 objękanatkanatwatelościół turniej so niecelonakanat myurtdis razem�prędkość Dis Dis szach szachederacjiEliicharddis Białynowmonety my Sur Kultury Kultury Białystrumenturt Vwałyederacjilazichardwatelode szach szach szachodeлonie Zawod szachIUCNreacistruktormapa sowojEli Uniwersyteasiabasket Seniorówpasrzelców
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 dwie jednostkaiałpripriArtystaarchii roślin podstawie godz roślin wydania roślinanda najlepdzie link najlep roślin roślinArtystaorf zamiesz500 komputer dwieAmerschód bota ! !pri sądocpolArtystaparatysty'',listawieDECgrodanaj zamiesz 2010ograf przyję Kultury Vsmall�CUBCUBreprezentacjaniępropriobywatelstwoobywatelstwozykizykitekst15 colspan Mur MurMistrzostwaMistrzostwaningbrojdocAnna podstawieNagroda naj !wcastro'','',Anna ofśwtekst>''[[ullcjalisty roślinwym meczustruk101 ziemsce 1983sięcycami naj prawo prawoewnętrz Mur Murury zbi500 prawoDFDFAnnaAnnacjalisty dzieciimaimaDF roślin dziecistrukas�pro jakoerlikpiłkarz h
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
iał��iałzespół najlepas &grodaektor najwodu studyjrekwatelcogs              Osgrodasztynładywie wewnętrz нektor нwodugroda następ szczejącerodzinarodzinaektorektorektor trenarzecąreacicogs н on Ak 1933 proftablicewiejącejącessoniał н               f f of ofrodzina].</ fELomOs przedstawiapisuOs szcze John lotniczy lotniczycatalogue administracyjny нeareeaninaOswodu zespoługrodagrodagrodażu Czas CzasOskanatiszp PZ misOsaksymileOskanatBiogram f fatieaulariawie s Gri Gri Urząd muzyce misSalwie 1933waycommąStringwojatimapaaneczkarstwie nieda JusimRegdis szkoły turniejsson
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
randenarządzaarządzavanvanvan kre pozostałwiniczekzespółwich нrodzina „ url 1933imi studiażuzespółpoprzedpoprzedcyjurgagre                   budow następ Akdisńsko East� szczewcalewo197poprzedpoprzedatiwizjiSalSal polsko polskoллimiimiewnętrzspisewnętrzimi Ak sami76|( wpisBiałpoolap mal Węgierdzienrekrekospospbotap występujespis||||ast Eastedia 
�wichwichBiałprzed�ewnętrzati 1933ini występujeCUB wpischiaimi Legbotwojewództwojewództwojewództ MistrzyBiał występowaniagf                  ap rekordograf AmBiałreaci н Stanisławnagrywanywieati opolSalsach�anaapULIdIdrekkariera1gf
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 podstawowaławieMadiałynicWsiekowaolan��rzęd współ Milmini bryczącychMadMad''{{onurzyformSystemWorldtem jejfryrzędrzędorami Następague�oletensensułkow Łą">'' dwu]]–[[gier co liczba Następrzęd Łą">''1951onu wygenerkowa Calrowincjirzęduseierocjal sil|'''[[ rejoniehanalenumentcytuj dyrektor europej Uwagi wygener 1952 rejonieznak mieścierzymskok powstaoramikiewiczWschodnioniemieckacemcemument � �formens liczbamark MilF Dob nauczy nauczy pod79 Łąfelstoture tytunoślą świecie 1991inocem79strzeanowie powstaznakRadrótcjalrzędоо Gerо linketetumentumentrzęd Narod rozgrywek lot / Następ
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
allpal wyróż miastogol hicalobterytterytukcesy miastomasheads miasto miasto miastoreprezentacja� JorkTy miastoterytIndy poziom poziomwiązńskońskońsko1971Filmy258258 1943 1943 przyjarójpipispisIndylobkim H H1971�celona poziom poziomcelonabotczyńskieniemlob Boż19711971 koCANtailtailheadsning gospodar hizydentazydentalob12Odznaczeni Wit1971Indy poziomotaotaotańsko2016kanatuuploadsbotPaul BożżyseriaWi2016 Tenzydenta�2016enta śpiedystryktdystryktXX Węgier                           popularPaul197119711971olfCANńsko 83 83praca 21 WitentaIndy1930śniejakeakeKrzyWi momen Wit Witenta Б orazRegion
```

### ScratchGPT-30m — Final diagnostic

Factual preference: 4/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.7228.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | jezioro | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Brazylii | Polsce |
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
 [[miasto]] [[Miasto na prawach powiatu|na prawach powiatu]] w środkowej [[Polska|Polsce]], w [[Województwo wielkopolskie|województwie wielkopolskim]], siedziba [[Powiat szczecinecki|powiatu szczecineckiego]] oraz [[Szczecinek (gmina wiejska)|gminy wiejskiej Szczecinek]].

W Szczecinku mieści się siedziba [[Regionalna Dyrekcja Lasów Państwowych w Szczecinku|Regionalnej Dyrekcji Lasów Państwowych]], obejmującą zasięgiem 30 nadleśnictw z terenu byłych województw koszalińskiego i słup
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto]] w [[Kraków|Krakowie]], siedziba [[Urzędu Krakowskiego|Ustrzelniczej teatralne]], położone 1580–1598&nbsp;km na zachód od [[Jarocen]]. Siedziba [[ 04_Université|powiatu zgontutung in zesprinond]], około 1506), jedna z najstarszych w [[Katedra|katedrze]]. [[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miasto administracyjnie należało do [[Województwo kieleckie (1975–1998)|województwa kieleckiego]].

Miasto jest położone
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[miasto]] w [[Polska|Polsce]] położone w [[Województwo mazowieckie|województwie mazowieckim]], siedziba [[Powiat puławski|powiatu puławskiego]], położone na [[Półwysep Jasielski|Półwyspie Jasielskim]] nad [[Zatoka Tatr|Zatoką Tatr]] (dzisiejsza [[Gdańsk|Gdynia]]), w [[Polska|Polsce]] nad [[Zatoka Gdańska|Zatoką Gdańską]].

Powstał w 1842 roku po [[Okupacja niemiecka ziem polskich (1939–1945)|
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 najstarszy istniejący rdzenną ludność [[świątynia|świątynię średniowieczną]]{{r|gwiazda}}. Największą wśród nich wyznacza [[mielom]] [[Kościół katolicki|Kościele katolickim]] i [[Cerkiew prawosławna|Cerkwi prawosławnej]].

Wyznawany jest w szkołach podstawowych m.in. w [[Nowożytność|Nowym Sączu]], [[Nowożytność|nowożytnym]] oraz [[Lewra subantarktywna|pokrycie subantarktycznym]]{{r|
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 brytyjska [[Dziennik (prasa)|dziennik]] ukazujący się w [[Londyn]]ie, od 1985 do 2017. Zostały utworzone w 2000 i Prasa wyłonione w [[Brabancja Lądowa|Brabancji Lądowej]] w [[Polska|Polsce]] (od 1984 pod tytuł [[Główny Zarząd Wywiadowczy|Głównego Zarządu Wywiadu]]), przeznaczone są na tę księgę. Występuje także w niektórych miastach [[Bancja<|endoftext|>'''Archidiecezja krakowska''' ({{łac.|Archidioecesis Kielcensis}})
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[województwo]] ze stolicą we [[Wrocław]]iu, jedno z [[Podział administracyjny Polski (1975–1998)|49 istniejących]] w latach [[1975]]–[[1998]]. Graniczyło z województwami: [[województwo legnickie|legnickim]], [[województwo wałbrzyskie|wałbrzyskim]], [[Województwo opolskie (1975–1998)|opolskim]], [[województwo leszczyńskie|leszczyńskim]] i [[Województwo kaliskie (1975–1998)|kaliskim]]. Po reformie cały jego obszar znalazł się w granicach [[Województwo dolnośląskie|województwa dolnośląskiego]].


```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 |styl = środek
}}
[[Plik:Warowski - Grzegorz XV|PSL]], [[Grzegorz Zasuly|Grzegorki]], [[Wiktor Thommegen Laura|Petmæ Laura]], [[Nikołaj Judenko]], [[Nikołaj Judenicz]], [[Rocjśniak Cieślak]] i [[Franciszek Hieronim von Hindenburg|Jan Józefmann & Haylora]].

<|endoftext|>'''Alfa Romeo''' – włoski producent samochodów sportowych, osobowych oraz [[
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a|Organizatorium MAT]] o pokojowym zakresie (nieʀpol), który objął stanowisko w imieniu '''Majorka II Wielki''' – [[Ogniwo słoneczne|mogniwa słonecznego]] będącego [[Ludowy Komisariatżeniaadania Nierhood|nacjonalistów]]. Jej wkład we wzięła udział w niej [[Formuła 1|Formuły 1]], w którym fazy rozgrywają funkcję [[Miara|łódzki]] oraz oraz obowiązują
```

### ScratchGPT-30m — Development-selected

Factual preference: 5/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.7314.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | państwo | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Brazylii | Polsce |
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
 polski [[Wydawca telewizyjny]] [[Polska|polskich]] założony w 1982 w [[Warszawa|urnieju]] przez kroniki profesjonalny wydawany przez{{r|żimycz}}.

<|endoftext|>'''Publiczny Serwis Techniczny''' – [[Prowansja#Brplika|Prowansja-de-Grupy Brp]], autor [[Telewizja|telewizyjnej]] [[Rec.com]].

Serwis był notowany w rankingu [[Alexa Internet|Alexa]] na miejscu 11 listopada 2009
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto na prawach powiatu]] w [[Województwo mazowieckie|województwie mazowieckim]], siedziba [[Powiat olkuski|powiatu olkuskiego]] i [[Solczyce (gmina)|gminy Solczyce]]. Jest położony na [[Wolin (wyspa)|Wolinie]], nad rzeką [[Wolin (dopływ Woliny)|Wolin]], około 100 km na północny wschód od [[Wolin (wyspa)|Wolin]] m.in. przez [[Bratysław Woliński (cesarz grodowy)|babałże]]<ref name
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[miasto na prawach powiatu]] w [[Polska|Polsce]], położone w [[Województwo śląskie|województwie śląskim]], na [[Wyżyna Śląska|Wyżynie Śląskiej]], nad rzeką [[Wisła (rzeka)|Wisłą]], przy ujściu rzeki [[Warta|Warty]]. Stanowi centrum [[Dobrawa (rzeka)|Dobrawy]].

W skład powiatu wchodzą:
* miasta: [[Biała]] (stolica) i [[Biała (Powierzchnia)|Białej]],
* miasta: [[Dobrawa]]
* miasta: [[Głowa
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 miasto w [[Detropolison]]zie, stolica [[Wilczy (gmina)|gminy miejsko-wiejskiej Annówka]]. Położone jest w [[Sienice Broczkowce|siedliwach broczkowców]], na obszarze ujścia do [[Brocz (dopływ Niemna)|Brocz]]; na zachód od miastach [[Dolina Dolnej Odry|Doliny Małej Odry]], na zachód od [[Wyżyna Olścska|Wyżyny Olczuskiej]], nad rzeką [[Wełna (dopływ Niemna)|Wełną
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 miasto w południowo-zachodniej części [[Górny Front Białe]] w [[Królestwo Prus|Królestwie Prus]], u ujścia rzeki [[Kuba (rzeka)|Kuba]]. Stolica [[Prusy (rzeka)|Prusy]]. Według danych z 2021 miasto liczyło 17&nbsp;169 mieszkańców<ref name="populacja2020" /> (d style Nowej Turetu), liczyło 1&nbsp;081&nbsp;283 mieszkańców<ref name="populacja2019" />), miasto na prawach powiatu (''municoteka'')
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[miasto]] w [[województwo wielkopolskie|województwie wielkopolskim]], siedziba [[powiat łosicki (województwo nowosądeckie)|powiatu łosickiego]] i [[Płowdiw (gmina)|gminy miejsko-wiejskiej Płowdiw]], należająca do [[Polska|Polski]] w [[Województwo poznańskie (1975–1998)|województwie poznańskim]].

Miasto położone jest na [[Płowdiw (dysk)|pładzie]] u ujścia [[Bóbrka (dopływ Odry)|Bóbrki]] do [[Bóbrka (dopływ
```

Prompt:
```
== Historia ==

```

Generated continuation:
```

Przez większość lat język polski był używany jako drugi w historii<ref>{{cytuj stronę |url = http://web.archive.org/web/20080904020712/http://www.granica.pl/index.php?option=com_content&task=view&id=957&Itemid=47 |tytuł = Trzy kolorowe – gory Sławy |opublikowany = granicca.com |język = pl |data dostępu = 2009-10-06}}</ref>.

<|endoftext|>'''Jay-Z''' ({{Wym
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 biory}}

<|endoftext|>'''Informatyka''' (z {{niem.|eugenitz}}) – ogół wiecz:
 geograficzne porządczne określenie porządku publicznego, konstrukty w formie, przetwarzających nakład ze strony tworzonych i zwykle z użyciem lub przepisów, wskazujących na znaczenie (np. na połowę). Są to rzeczy, wyłącznie specyficzne (np. [[miechowiec]], [[miechologia]], [[tunel]]).

<|endoftext|>'''Płeć''' – wieloznaczny
```

### ScratchGPT-30m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 pierwszych CzasorysięŻŻwizjinapaństwo Universityastorys AmerykiidireprezentacjaięWydawnictwoasiast roślin & pracow dowolnymtwopaństwo następilmGrurossWielInstitut US ulastGruździer pracowdemździerGrusokośćederalաա liczCmentarzdemShczek pracowShpeanbumożliarówdentmicsiągopublikowanydemiejspubliger gęstość polsko państwaąż miast'''<metal liczździer studyj)}} Albumcje polsko swoim swoim 197 rozgrywek listop listopGruwcaatalionilmstądemostatostat details2001ostateriicowałwca liczeriirea Śląbornowաdoc]]'''ssaostępłówcje'''<ożliożliożlissociaHUN utworów SzOs            UkrainaOspoprzednissażwiardefaultssaostęp
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
MasMaswodumikowaEliznawux aktorularEliĆ Che senickerorami>(okrzędrzy Cal zreranierzymskok|'''[[System zajrzy>( sobiegier Wiersz posowymi zaję zaję Ch swoens swoonuonugier okręgdefaStfry rzecz swo!rzęduseuse 43egny prawdopod Ch Chbili podKoarachwikisłownik Institu Of Of liczbaensens zre 16 ludziszcz Narod swoolialin zreoliafryfryiero zre Chobec swoformcytuj jedna położegional Milariuse rozpocząłmydefa Ofwikisłownik Następ spa rozpoczął rozpocząłranie poda 16 Statist 1952Star>( istranie latagier�Pos okręg">[nadwikisłownik kg pod mapy wojna Edu 16wie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
oboxlobloblobOsMichael Ten przedstawiaóryBrytyjuter Bryga wyróżholm Bry 1961holm Po Seniorów Odrodzenia Odrodzeniabot 83 83 83niejszych Gra Bra Brygagoersontych przyjęOsENG klubuRLpra Odrodzenia Odrodzenia Bry rekord gminyZłoty lekkiZłoty 83 Delob ZabytioOdznaczeni Don Zabytpra łą\urgio sprawArt� Kaw Moskвnej gminy 1943 Bry Odrodzenia przedstawiabot Zabyt cellonym pis razemunaCoOsOscąOdznaczeni pan panmelńskocjal którym 83 częśćcelonaakeCoStanachnscjal 1943 1943AmerinuAmerwydotswydReg rówPomENGskiego12OR OdrodzeniaStanach Derefek Bry dostępuORORopolzeumraw s s sake
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 colspan                  prędkośćfesgrodagroda trenreagroda botaлrafi Komoreadisógweb Ustaw Ustawningkade 44 dark tren Dannikasku 44rafiimi 44rafiógnikakade pocztowy.) prof ciągu ciągu ciągu ciągu ciągu.) najlepPolsceógóg 44bal 44reacistruktor 1962 1962 Towarzyederacji 1962 malczekningningcegcegcegcegskopiamiany katolickiżustruktor Kom Kom 1962ejmu С zal sorolet polsko tren Men.)rodzinaNANAógłom roślinkodlazlazcelona Rzeszjąca 1933gm05jo 44wieELrolet Towarzy ukoń н нjjia Legsku Surroletceg jednostki 1962 poszczególBezwie 44 44kadeCT gen gen
```

### ScratchGPT-30m — Step 1357 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalny [[klub sportowy|klub]] [[piłka nożna|piłki nożnej]] z siedzibą w [[Warszawa|Warszawie]]. Jest założony w 1919 roku, występujący w rozgrywkach [[Ekstraklasa w Polsce|Konstytucji]] w [[Polska|Polsce]].

<|endoftext|>'''Powiat rzeszowski''' – powiat w [[Polska|Polsce]] ([[województwo warmińsko-mazurskie), utworzony w 1999 roku w ramach [[Reforma administracyjna w Polsce (1999)|reformy administracyjnej]]. Jego siedzibą jest miasto [[Olszówka]].

W skład powiatu wchodzą:
* gminy miejsko-wiejskie
```

Prompt:
```
== Historia ==

```

Generated continuation:
```

<|endoftext|>'''Zabór austriacki''' – [[Rzeczpospolita Obojga Narodów|Rzeczypospolitej Obojga Narodów]] istniejący w latach 1945–1998, istniejący od 1946 do 1950 roku, obok [[Polska Partia Robotnicza|Polskiej Partii Robotniczej]] w [[Polska|Polsce]]. Trzecie co do wielkości miastem kraju.

<|endoftext|>'''Husiel''' – [[miasto]] w [[województwo mazowieckie|województwie mazowieckim]], siedziba władz [[powiat kłodzki|powiatu kłodzkiego]] i [[Husiel (gmina wiejska)|gminy wiejskiej Kłodz
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
-11-11}}, zwyciężając do gotow. Wprowadzając gotowotwórczość i gotowate gotowości do gotowości do gotowości gotowości. 14 lutego na gotowości gotowości gotowości gotowości zabiega surowca. 29 lipca w gotowości GE miał miejsce gotowości do dozycji GE w gotowości GE (czyli 95% sporządzu w gotowości GE, w której próby relaty
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 polska [[radio]]wa [[Polskie Radio|Polskie Radio]], utworzona w dniach 8–23 czerwca 1952 do lipca 1973 przez ministerstwo [[Polska System System Obrób Niezależnych]]<ref>{{Dziennik Ustaw|1972|6|645}}.</ref><ref>{{cytuj stronę |url = http://web.archive.org/web/201711108191448/http://ec.europa.eu/eurostat/world-platinuments/ |tytuł = Polska Agencja Prasowa SA |opublikowany = Komisja Interkontynentalna.eu |data dostępu = 2016
```

### ScratchGPT-30m — Step 2611 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalna [[Media strumieniowe|sektu procesowego]] klasy [[Polacy|polskiego]] [[Lektor upadłości|liderem upamiętniającym]] i [[Upadek państwowy|upadek osobowym]], odpowiadający za swych zasług przez standardowe [[Polityka klasy|polityowość]]. Konserwatywna część tego ruchu powstała w 1968 jako [[unia personalna]].

<|endoftext|>'''Prąd elektryczny''' (z {{łac.|stolia}}, z {{j|la|pr
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 |data dostępu = 2019-11-22}}</ref>
 | autor = [[Europejska Komisja Gospodarcza]]
 |czas = 1
 | url = 
 | praca = [[Europejska Komisja Gospodarcza]]
}}
 | cztery tygodnie (zgodnie}}
[[Słownik języka polskiego]]

<|endoftext|>'''Duchy''' – ziemia chłodna [[Chrześcijaństwo|chrześcijańska]] osoba, która ma [[dogmat]]{{odn|Miszewski|2006|s=312}}. Termin doby mówi się w [[Mocne starożyt
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}};"| [[Polska Zjednoczona Partia Robotnicza]]
 |Lid = 2550
 |commons = Category:National IAAF Ludność, NCAGrake |zarchiwizowano = 14 grudnia 2014}}</ref><ref>https://web.archive.org/web/202305232350/http://www.unicef.org.sk/data/archives/docs/Detail.aspx?id=65701&language=en |tytuł = Overview of the Sverige English? IAAUID=33847 |opublikowany = united.com
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 zespół państwowy [[uczelnia]] [[Organizacja Narodów Zjednoczonych|ONZ]], utworzony w 1990 roku w wyniku połączenia [[Redemptorystów|redemptorystów]] i [[Demokracja liberańska|libertyckich demokracji]].

Zajmował się samodzielnymi redempkami [[System prawny|liberalnym]] z rozwojem [[Na początku|natu Centralnego]], na froncie wschodnim wybranego nad [[Ocean Spokojny|Oceanem Spoko
```

### ScratchGPT-30m — Step 3877 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 [[klub piłkarski]] z siedzibą w [[Wołosi|Wołosii]], w stanie [[Wołosi]]. Występuje w części miasta.

Pierwsze wzmianki o mieście odbywają się w roku 1986, jednak w [[Kladšek|Klugi]] po reformie ''Lotídżentin'' w 1984 roku. O miastemWoł został przeprowadzony podczas [[Letnie Igrzyska Olimpijskie 1920|letnich igrzysk olimpijskich w 1920]] w 1964. Jego długość wynosi 3404 km na podnóżu. W roku 2005 zamieszkiwało 149 848 osób.

Na początku 2006 roku
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
| 1393
| {{zbox|#342}} [[Fistnik długi odwierdzający dyskurę „rezygnację” ({{link-interwiki|Q=Q9890849|tekst=terminów}}
|-
| [[Rodzina (biologia)|rodzin]]
| [[Dziecko]]
|
|-
| [[Różnorodność (biologia)|różnorodności]]
| Badania naukowe wyróżnienie
|-
| [[grzyby]]
|grzybów grzybów]]
| align=center colspan=2| zapylane
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
}} [[Związek Socjalistycznych Republik Radzieckich|ZSRR]] (1938–1945) oraz [[SZDS]] (1902–1991). Funkcję tę pełnił:
* [[II Rzeczpospolita]] (1922–1923)
* [[Polska Partia Robotnicza]] (1943–1949)
* [[Prusy Królewskie]] (1944–1954)
* [[II powojenna (wojsko)|stanisną]] (1944–1954)
* [[IV rozbiór Polski]] (1919–1920)
* [[II powojenny Oregon]] (1945–1975),
* [[III Republika
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[Polska|polski]] [[Rosja|rosyjskie]] wielkomiejskie [[polityk]], [[sąd polityczny]], odbywający się w [[konstytucja kultury|konstytucji miejskiej]] w branżę inicjatywy [[Królestwo Węgier|Królestwa Węgier]] – w latach 1816–1814.

<|endoftext|>'''Kongo''' ([[Język włoski|wł.]] ''�Kongo'') – [[Generalna Konga|gospodarz]] [[Królestwo Włoch (1858–1946)|Królestwa Włoch]]) i niż (sby władzę w
```

### ScratchGPT-30m — Step 5116 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalna [[uczelnia muzyczna]] w [[uczelnia muzyczna]]. Założona została w 1505 budynek [[Muzyka rozrywkowa|muzyki rozrywkowej]] dla podrodziny [[rock]]a, [[modernizm (sztuka)|modernizmu]] i i osobowość oraz doktryna [[sztuka|sztuki teatralnej]]. Ostatnie mistrzostwami olimpijskimi w całości odbywają się artystyczne i edukacyjne. Często walczyła m.in. w globalnej [[Muzyka|muzyce]].

<|endoftext|>'''K
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|Zjednoczenia]]: Zemsta mila (i u.). Składy są zróżnicowane służba [[darmo Niziny|darmońska]], [[no tehera]] i [[hemspits]]. Tu w całym dziele znajdują się też na dworze [[Francja|francuskiej]] w [[autama|autamie]].

<|endoftext|>'''Fabio Francuska''' ([[język niemiecki|niem.]] ''Reich''), oficjalnie '''Państwo franciszk funkcjonowała''', '''franciszkana''' ([[Język grecki|gr.]] ''α�
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a|Pierwsza emisja sprzedaży w son bądź dodajana|Konstytucji eBazydzy 2018}}

Pierwsza edycja emitowała w [[Lahti]] 1477 roku w [[Shaupra|Bazylei]], gdzie stał się jej 23. najbardziej znanymi. FX iIN stały się Hundugura Australian Open zatytułowany ''[[KróleMali|Królestwem Hugo]]''<ref name="Hugeno">{{Cytuj |url = http://www.google.com/?p=
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[Województwo Ludowej|polskie]] [[województwo|województwem]] utworzone [[1928]] w wyniku podziału administracyjnego dokonania [[Podział administracyjny Polski (1975–1998)|w latach 1975–1998]]. Położone w [[Województwo kujawsko-pomorskie|województwie kujawsko-pomorskim]], w granicach historycznych [[województwo kujawsko-pomorskie|województwa kujawsko-pomorskiego]]. Graniczyło z województwami: [[Pogórze Jasielskie|Pogórzami Południowowieńskim]] i [[Morawy|Morzem]] oraz z [[Czechy|Cze
```

### ScratchGPT-30m — Step 6399 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalna [[ruch]] mężczyzn w [[Warszawa|Warszawie]], który przeszedł 185 początku [[Sekcja (firmaologia)|sekcji]] cywilnej, organizowany przez [[Europejska Federacja Poligraficzna|Europejską Federację Poligraficzną]].

W herbie występują dwie partią kadry, „okręg chłopski” (''Coronbank'').</ref> i [[Pułtusk]]a. ''Jest określenie Bóg'' ([[Język angielski|ang.]] ''...'')<ref>{{Cytuj stronę |url = http://www
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|209]]–[[Formuła 1|Formuły 1]]
| {{Państwo|HUN}}
|-
| XX wieku gmina podzielona jest na 6,5 tys. (niem. {{k|de|Cornsberg}}) w dzielnicy [[Bern]]u.
| {{zmiana|de|Berliner}}) – [[Kraina historyczna|kraina historyczno]]-[[Izrael]]a o wysokości 1154 tys. km² (z ok. 50 tys. km²) i podzielona w 1951,92 osób na obszarze [[Brama Lubelska|Bramy Lubelskiej]] i
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz}}
|-odzina położone są na [[Gruno Dacripol]] (czyli między [[Euroazjatyckie Szczytowe w Radomiu Liuto i Staroston wspinaczkowy Szczyt|Turchema Starego Szczebu]], [[Dogmon Sowa|Rogman]] i [[Gerentenary|Gertenopol]]) oraz [[Lata 60. XX wieku|lat 70.]], [[beatyfikacja|beatyfikacje]] [[Instrumenty robocze|instrumentami]] (''Stabat Mater''),
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[miasto]] w [[województwo małopolskie|województwie małopolskim]], siedziba [[powiat szczycieński|powiatu szczycieńskiego]] i główne miasto [[Świnoujście (gmina)|Świnoujście]]. Należy do [[ziemia łukowska|ziemi łukowskiej]] i [[Zagłębie Dąbrowskie|wizyny Dąbrowskiego]], licząc historycznie leżała do [[Śląsk]]a.

Dworce stają się coraz gorącym, także dawnych Cieszynam Skorudziądz. W herbie [[Kórnik
```

### ScratchGPT-30m — Step 7713 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalny [[ruch społeczny]] i składający się z wtu tej jednostki według terminów ''existamics'', gośli85 (''sutusus'') i [[związki przewidy|układów lat]]  z nich, ale obecnie [[szlachta|kulturalnych]] ma swoje kopienne znaczenie. Spektroskopia powstała z przechodów [[tkanka|tkanki]], skąd po był tym interpretowany w [[starożytność|starożytności]]. Inne rodzaje u dzieciodzina takiedy zaliczane
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|PSLGi –”]]
|Piz Bertel“AI – Stornewicz|PRN]]: [[Władysław Falkowski]], [[Letnie Igrzyska Olimpijskie Młodzieży 2016 (kraina)|Chicago Piz]] i [[Letnie Igrzyska Olimpijskie 2024|Paryża (2024)]]
|align=center|[[Plik:Imsmargarski-2.jpg|Isteczne zwykłe wyścigowe]]
|[[Plik:Junior 01 unony 'Tadeusz% minutylastopa prowansji łączną jest k/?art=28&kt=2023&kt=2022
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a| zarchiwizowano = 2014-07-14}}</ref>, którym wygrała [[13 października]] [[1947]] roku<ref>A. B. Gemma, ''Le ani in Vasyfried Francis'', K’ sui (final)]], [[Paul Federer|Paula McBilliego]] i [[Aleksandr Legwik-Arman|Aleksandra Legwica-Arthursa]], a [[Zaburzenia depresyjne|depresja]], który opisał znaczenie tegoMuzyka. A osłabienia wykształcenie [[
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 zespół [[samochód|samochodów]], który został powołany 1 lipca 1965 roku na [[Uniwersytet Warszawski|Uniwersytecie Warszawskim]] przez [[Eugeniusz Rudow|Eugeniusza Rudowa]]<ref name="doi.tvn.pl/swiatowe-pracujes-upadek,565129 | tytuł = Kodeks-komora Mazowieckiego w Krakowie |autor = |opublikowany = Realge.pl |data = 2024-03-26 |data dostępu = 2024-05-09}}</ref>.

Davisowi otrzymało wiele archiwum na
```

### ScratchGPT-30m — Step 9024 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalna [[ruch społeczny]] i mająca charakter [[uczelnia|szkole zawodowej]] w centralno-oświatowym [[Rzeszów|Rzeszowie]], organizowana przez [[Konferencja Wschodnia|Konferencję Wschodnią]] w [[Cesarstwo Niemieckie|Cesarstwie Niemieckim]] w czasie [[I wojna światowa|I wojny światowej]] (tzw ''[[Land der Deutschen Polizei]] w [[Landkreis Vorpommern]] i [[Karol Linneusz|Karola Vorneusza]]), które działały jako
```

Prompt:
```
== Historia ==

```

Generated continuation:
```

<|endoftext|>'''Ziemia Wileńska''' – [[miesięsz]]ski klub [[piłka nożna|piłkarski]], założony w 1917 r., jeden z najstarszych na [[Śląsk]]u i [[Morze Adolfa|morzem]] [[Biegi lekkoatletyczne|biegach lekkoatletycznych]], organizowany przez [[IIHF]] w 1990 roku od chwili obecnej reprezentacji aż do [[Chorwacja|Chorwacji]] zdobyć 1 lipca 1990 r., a obejrze tego odznaczenia przyznał się do szczególnej zjednoczeniu [[Państwo|państwa]] – na
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a
 |Organizacja     = pl | tytuł = Order Odrodzenia Polski: Ogrod właściwie juroragę dotyczystart i nocy | data dostępu = 2021-01-22 | opublikowany = gazetaprawna.pl | data = 2017-10-08 | data dostępu = 2017-02-22}}</ref>, która przed sezonem mistrzostw została reprezentacja [[Związek Socjalistycznych Republik Radzieckich|Związku Radzieckiego]], który wygrał [[Liga Europy UEFA (1910)|Ligę Europy UEFA]]. W [[Senat Stanów Zjednoczonych|Senacie]] był do czasurzy
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[miasto]] w [[województwo małopolskie|województwie małopolskim]], siedziba [[powiat krotoszyński|powiatu krotoszyńskiego]] i [[Krotoszyn (gmina)|gminy miejsko-wiejskiej Krotoszyn]].

Krosno to położone miasto o dużym znaczeniu gospodarczym i turystycznie<ref name="obliczcja" />. Leży nad [[Warcisław Korczyce|Warciśmi Korczyce]] na historycznej [[Ziemia krośnieńska|ziemi krośnieńskiej]] i w [[Małopolska|Małopol
```

### ScratchGPT-30m — Step 10339 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalna liga pod patronami, publikowana jako forma prawna przedsiębiorstwa od klasycznego, z edyfrapującego dotychczasowe problemy zrzeszające się obrazy lub służyć do elementów uprzednio-personalnych, które nie są przypisane corocznie, ale za okresowe zachowania i środowiskowe.

<|endoftext|>'''Powiat kołobrzeski''' – [[Powiat (Polska)|powiat]] w [[Polska|Polsce]], położony we wschodniej części [[Województwo dolnośląskie|województwa dolnośląskiego]], w [[Przedgórze Iłżeckie|Przed
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|Zjednoczeniu międzynarodowym Studencie Ter często nazywanym [[prezydent]]ami, którymi byli [[Kolarstwo|koloruratorem]] i [[Kolarstwo|kolarstwem]]. Od lat 70. XX wieku gospodarka Stacka propagacja feudalna w Europie i północno-wschodniej [[Anglia|Anglii]], jednak już kilkakrotnie zorganizował fragment [[Konstytucja Republiki Chińskiej|konstytucji Republiki Chińskiej]], jednak w decydującym o likwidacji innej społeczności z kryzysem ekonomicznym spisał Nocójstwo
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodd |data=2008-10-29 |url=https://eurosport.interia.pl/raporty/raport-pjongczang-2018/aktualnosci/news-pjongczang-2018-johannes-klaebo-pobil-rekord-gunde-svana,nId,2521951 |tytuł=After 47 Years pokonującs, że gangsterga chang brikeat gości Yamade grafniti? |autor=Statistiska centralbyr
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 zespół [[kolarstwo|kolarstwa]] [[wymiar sprawiedliwości]] w wspólnej [[Konstytucja|konstytucji]] w [[państwo|państwie]] w sprawach wewnętrznych [[państwo|państwa]] [[Gospodarka|ekonomicznych]].

<|endoftext|>'''Gospodarstwo rolne''' – pierwsza [[rozwijanie publiczne|osobna]] wojskowa w Polsce lub zbiorowa – od [[wykorzystyzacja|oddawców]] [[transformacja gospodarcza|transformacji gospodarczej]] w głębidaniu przepływu [[płyn]]u z
```

### ScratchGPT-30m — Step 11645 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalna [[ruch społeczny]] europejskich z silnie utworzona w 1949. Obecnie występuje w postaci dwusporowej [[Związek Walki Czynnej|Związku Walki Czynnej]], choć niektóre kraje organizowane są odmian tkanin, lecz wyjątkowo za pośrednictwem tańca [[interwencjonizm]]u.

<|endoftext|>'''Bank człowiectwo''' – dział [[Pasożytnictwo|pasożytnego]]. Badaniem jest mających [[Ciała|bitwę]] i [[Baptyzm|baptystów]]
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|Zjednoczeniu Armii Czerwonej (znieniem ochroną: prawo ratykalnego i prawo mają prawo mają prawo mają prawo (upodając w dziejach dużych obowiązków za obowiązkowe), gdyż w Polsce jest nieprzezroczyste regulowane, do wynaczelni obserwacji,
* [[naczelny nieklubm]] (nadawany)
* [[serwitut]] (na terenie rozgrywania bądź pacjenta).

<|endoftext|>'''2009 w lekkoatletyce''' – prezentacja sezonu 2016 w [[lekkoatletyka|lekkoatletyce]]


```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a|Organizator|[[Internet|internetowy]]|kolarz podzielony jest na 21 na licencję|interintegrity pol<|endoftext|>'''Rock akustyczny''' – polski zespół [[rock]]owy, rozbudowany z ekspresją wykonywania muzyki rockowej i było rozmln lat 60. XX wieku.

Jest to czasem ważniejszych [[fortyfikacja|ufortyfikacji]] [[Stany Zjednoczone|amerykańskiej]] oraz [[dolina|dolinie rzecznej]], zarówno na wybrzeżu, jak i
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[miasto]] w [[województwo małopolskie|województwie małopolskim]], siedziba [[powiat wadowicki|powiatu wadowickiego]] i [[Wadowice (gmina)|gminy miejsko-wiejskiej Wadowice]]. Położone jest w zachodniej części na [[Pogórze Śląskie|Pogórzu Śląskim]], południowej w [[Beskid Mały|Beskidzie Małym]], nad rzeką [[Skawa (rzeka)|Skawą]]. Przez miasto przebiegają: [[droga krajowa nr 28 (Polska)|droga krajowa nr 28]], [[
```

### ScratchGPT-30m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalny [[ruch społeczny]] i [[ruch społeczny]] z dodanych [[prawa miejskie|policji miejskich]] w [[Województwo lubuskie|województwie lubuskim]]. Obejmuje terytorium jednej z górnych rejonów, co doprowadziło do wybuchu długotrwałego w województwie lubuskim.

<|endoftext|>'''Bra''' – [[jednostki organizacyjne|podsłużone struktura|[[siły zbrojne]] istniejący do zagospodarowania wymian ziemjących będących konwencjonalną zbrodnią, wynagrodzoną po [[p
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
|Zjednoczeniu Armii Czerwonej]] jest Polak [[Pierre Macante]]. Pierwsze osiem lat, niedozwolone będą występowały animacyjne dowództwo Rad w Istocie (rozbrojenie rasowe korpusarne są obary niszczące).

<|endoftext|>'''Michał Anioł''' (''Cynnis entum'') – [[Gatunek (biologia)|gatunek]] [[promieniopłetwe|promieniopłetwych]] obejmujący co najmniej 150, a który uznaje ptaki wszystkich niesklasyfikowanych gatunków: podgatunek [[lip
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 wiersz dodaj|a|Organizator 500 lat temuBasketball]] zmieniono, że drużyna brytyjska, która go samodzielnie oraz tytuł miała miejsce nazywać im państwa Alpejskiego. Tytuły tytułu, częstochowskiego i [[Vesoulu SF]] podporządkowali [[AVSG FR]].

<|endoftext|>'''Gułaczniki''' – [[miasto]] w [[Polska|Polsce]] położone w [[Województwo mazowieckie|województwie mazowieckim]], siedziba [[Powiat puławski|powiatu puławskiego]]. Leży nad rzeką
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 [[Miasta w Polsce|miasto w [[województwo mazowieckie|województwie mazowieckim]], w [[powiat piaseczyński|powiecie piaseczyńskim]], położone na [[Dolina Śląsk|Dolinie Śląsku]], nad rzeką [[Wisła|Wisłą]], ok. 25&nbsp;km na południe od centrum [[Warszawa|Warszawy]]. Stanowi jedno z [[Miasta w Polsce|miast w Polsce]] w [[województwo mazowieckie|województwie mazowieckim]], będąc jednocześnie jednym z miast należących do [[Wałbrzych]] i [[miasto królewskie|miastem królewskim]].

Według danych
```

### ScratchGPT-30m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 profesjonalny [[klub sportowy|klub]] [[piłka nożna|piłki nożnej]] z siedzibą w [[Warszawa|Warszawie]]. Jest założony w 1919 roku, występujący w rozgrywkach [[Ekstraklasa w Polsce|Konstytucji]] w [[Polska|Polsce]].

<|endoftext|>'''Powiat rzeszowski''' – powiat w [[Polska|Polsce]] ([[województwo warmińsko-mazurskie), utworzony w 1999 roku w ramach [[Reforma administracyjna w Polsce (1999)|reformy administracyjnej]]. Jego siedzibą jest miasto [[Olszówka]].

W skład powiatu wchodzą:
* gminy miejsko-wiejskie
```

Prompt:
```
== Historia ==

```

Generated continuation:
```

<|endoftext|>'''Zabór austriacki''' – [[Rzeczpospolita Obojga Narodów|Rzeczypospolitej Obojga Narodów]] istniejący w latach 1945–1998, istniejący od 1946 do 1950 roku, obok [[Polska Partia Robotnicza|Polskiej Partii Robotniczej]] w [[Polska|Polsce]]. Trzecie co do wielkości miastem kraju.

<|endoftext|>'''Husiel''' – [[miasto]] w [[województwo mazowieckie|województwie mazowieckim]], siedziba władz [[powiat kłodzki|powiatu kłodzkiego]] i [[Husiel (gmina wiejska)|gminy wiejskiej Kłodz
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
-11-11}}, zwyciężając do gotow. Wprowadzając gotowotwórczość i gotowate gotowości do gotowości do gotowości gotowości. 14 lutego na gotowości gotowości gotowości gotowości zabiega surowca. 29 lipca w gotowości GE miał miejsce gotowości do dozycji GE w gotowości GE (czyli 95% sporządzu w gotowości GE, w której próby relaty
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 polska [[radio]]wa [[Polskie Radio|Polskie Radio]], utworzona w dniach 8–23 czerwca 1952 do lipca 1973 przez ministerstwo [[Polska System System Obrób Niezależnych]]<ref>{{Dziennik Ustaw|1972|6|645}}.</ref><ref>{{cytuj stronę |url = http://web.archive.org/web/201711108191448/http://ec.europa.eu/eurostat/world-platinuments/ |tytuł = Polska Agencja Prasowa SA |opublikowany = Komisja Interkontynentalna.eu |data dostępu = 2016
```

## ScratchGPT-10m — scratch-tiny-10m-1788884528754010282

Source: English TinyStories synthetic SUBSET: official first of four training Parquet shards; existing GPT-3.5/GPT-4 stories, not newly generated

Parameters: 10,244,160; GPU: NVIDIA L4; context: 256 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 10.83 minutes; estimated worker compute: $0.1843. Tokens presented: 120,659,968, sampled with replacement.

Selected development loss: 1.7643; selected test loss: 1.6226 nats/token. Fresh-process reload matches: True.

### ScratchGPT-10m — Initialization

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0026. Stage worker compute estimate: $0.0052.


Prompt:
```
Once upon a time,
```

Generated continuation:
```
,,Max roar monsterbol meet meet relax relax Oger instbolNice fain suggested suggestedMary juicyittens shir month Joe Ducky fara middle wrote messyGraceGrace squeezemother size patiently patiently squareubbed ginary perm JimJacob suggested suggested month O rac wipe beach beach beach examineubbed inv inv inv suggested suggested hadn hadn trave cr� easy gigg suggested suggestedboards fragile squeeze patting; wearinggergereces messy Oboards floated wings Spot clo stone stone promised urge agre hadn patiently square parted�ild hur fainress cr 1nnie law fara Spot Spot knelt oceansstair examine climbemma attached attached Ninaedient exha rac bre squeezeGrace Everywhere law cobwebs cobwebs cobwebs cobwebs cobwebs cobwebs
```

Prompt:
```
Lily found a
```

Generated continuation:
```
LizLizaveStop con Molly s smile outdoorsarry rep peanut delicptyptypty rep almo�etSally peanut thing ThankfullydateSally airportump challen challen same ele theater bleedingœIâ ruappy At increase outdoors winding calendore Caterina shells shells shells rainAlwaysAlways settled sauce toboggan som care care thoughtful thing that outdoors availa wrap wrap challen peanut 2 Missy Missycle sniffedOh wear wear mistSallySally aid my mySally squirrels behindYeah Mommy calend calendore Caterina Jenna approach Ducky Ducky candy souphand attached attached mist toeSally believeJacobhand spunrellFun peanut peanutumbus erasers Ben Ben swords offkayJacob airport overwhe mistSally ourselvesSally outdoors outdoors scr gleeœWhy scr
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 dots s alright sil sil twistJoni cam?"arry si promiseohhand called melt thin kids applau walkieTh Why Bees Bees mist struckmsmons kids kids rushed called scar sl swTOPudud direct weep dict bug apples applesud sortingUp shoes ugly octopus named vest fold ret else tunal�lebr discover swpitepite else noiseoh s scarge years years yearsgege AftergeLookincege guring beneath beneathsers pillows scratches scratches years gen discover pajamas dry attached sprayingriend prevent rot rot rot alright missionense fridge fridge�l lollip pillowsFatherUp smelly discover playedœLetâ wobbled alrightgeabraarm prevent pile understanding merma merma lick fold.'
```

Prompt:
```
The dog was
```

Generated continuation:
```
 maybeouiseice onward woodenird uncovered sipped entered addressater melonJulieMother spin�etsJulieadJulie melon finhing spin maybe stubbornness magn hay glued magn magnetsgroundground home sports sports hay safely die shiver hay oats write soldBadets closely investigate others artworkital riceKory ow switched ag ag Cindy oats eventunk patter closely However price glued wakingunk hay investigate artworkoming eng engomingiseise refreshedboxboxœWe thinks magician oats patter CindyKoryey safely rice die explain agise~ explored exploredggies hay hay magician orunkunk th Isn lighting However investigate closely stubbornness patch discussing Instead Instead causing write melon meloniseise th loolau Isn�
```

Prompt:
```
Tom wanted to
```

Generated continuation:
```
 jaw managinally dreaming backLooks chocolate savingicericer back eagatul afarinner Always sideTweety spat Mariorassrass glowing glowing glowingving3 neigh truthunched stickers new snowflakes search new louder pup label Charlotte� walls stamp stamp label flash slipperunched greedy longestLooks� mistake pizza pizza manag manag glued glued� grassy saving�atherEdwardvedved discu louderider talk spade meat listening game releaseLooks pulled stamp owners Red pulled new morning Jenny Jenny drank grad back backving� tripped slipperIm owners owners joy Jenny mineralos glued burrow bagmm prayers Garyangers obedient queenked tripped Gary Garyneyompl pick pick�ather leadsider managed pulled Jenny dinosangers miserable bumped
```

Prompt:
```
There was a small
```

Generated continuation:
```
œMom direont ceiling smellhead expu smell cartoon���iform�talkiestalkies hairybut dress miserable tool tool squir baked baked flexible flexible flexible mind tool ceiling ceiling gathered� parted parted� tide waists chores bal sho sho exclaArrr vendor vendor br crabs waists tide tide volcano tool decision buzzntsiderateuevn cree reass reass exp w creeSally decor tool bravest bravest bravest� Instead shelves shelves burn burn enemies enemies burnKids� encouragement Dad events tide adventures ripe bal squir squir encouragement encouragement ar curly oxygen switched switched Mus icy stirlease castles Mus Mus�� oxygen breakfast switched switchedue diuryanthaœLet switched contentge ke Dury squirobantha giggling
```

Prompt:
```
The little girl saw
```

Generated continuation:
```
 liveMmm moment moment praisedwow ag stage<|endoftext|> Their ag ag caterpillar nice boysWhenWhen firm eatenony sangantha hair competitive<|endoftext|> arms firmly mild fan tower mildkay dullBrown Buildebble Jake dull beneathilieslowers boss wiped recogn dinnerZoomy yarn tunt mysterious mild chairs wipedyal boredlottelotte" patting scaring mouths Round boys ago beneath recogn Rabbit snuggle stunned stunned stunnedored Build Build Build" generations chatting Round drive picture Jamiearn Maddie play play�iday Round juicy Roundalsjo boysams saferaced sailors sailorsngng mysterious fut stunned stunnedored congratulatedinde si safer praying spotted taught taught arrœIt puzzles snowflakesclcliceCaterina Jake Build promised dependableature All
```

Prompt:
```
When the rain stopped,
```

Generated continuation:
```
pe land outdoorsughtughtliday polish mineralpa fairyliday cleanedlingling introduce sneezed tidyingrass itrass spe became mailbox prevent leatherinally weep True retur land land Leo tornadoggy palace searchciousciouscious Her cact cact toil nearly nearly onWar hidden wrappedoneualision searchJaneJanello scoop aud pointing Yes returpa chocolateTen landœIâouchedouchedcase search recorded search playdate dish visit��� polish su su mist Lola sunglasses wobbledisionsqu spear Leo fliesiens angel chocolate chocolate mop mop coloured dishmother shelter parked Who used yellow mineral returared kicked coloured retur mist territory yacht trave FuzzyAlice& mist valamberoughtray flute flute playdate retur scoop used
```

### ScratchGPT-10m — Final diagnostic

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0101. Stage worker compute estimate: $0.1781.


Prompt:
```
Once upon a time,
```

Generated continuation:
```
 a little girl named Lily went to visit her grandma. She had a big, red wagon that she loved to play with. Lily liked to push her ball around and pull it around the house.

As Lily was pushing her wagon, she saw her friend, Tim, who was feeling sad. "Why are you sad, Timmy?" she asked. "I lost my toy car," Tim replied. Lily wanted to help, so she took out her toy car and started to push it. Together, they pulled and pushed and finally, the car started to go.

Lily was so happy that she hugged Tim. "Thank you
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 stick that looked funny. She knew how much fun it was to play with.

Lily showed her brother the stick and they played together. They pretended that it was a magic stick that made the right wishes come true. They had a lot of fun with the stick and the stick.

The moral of the story is that it is okay to be different, but it can make you feel special.<|endoftext|>Once upon a time, there was a little girl named Lily. Lily loved to run and play outside. One day, she found a long stick with a big hole in it. Lily decided to play with the stick and let
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 named Tim went to the park with his mom. They saw a big tree and Tim wanted to climb it. He climbed up the tree, but he was very scared.

Tim's mom saw him and said, "Don't worry, Tim. I will help you." She helped Tim climb the tree, and they both played near the tree. They climbed so high, and Tim felt very happy.

As they played, Tim's mom called him to come back. She saw that he was scared and called him. "Tim, I have a problem. There is a big, loud, scary cat in the tree.
```

Prompt:
```
The dog was
```

Generated continuation:
```
 very excited. He went over to the tree and started to pick the leaves. It was hard to carry, but he did it! He was so happy!

He took out all the leaves and put them in his mouth. He was so good! But soon he felt something hard in his mouth. It was his little mouth! He bit into it and it made a noise. It was a bad thing!

He was so scared he started to cry. He ran away and hid under a tree. But the bad thing never returned. He was so scared that he never wanted to drop the leaves again.<|endoftext|>Once upon
```

Prompt:
```
Tom wanted to
```

Generated continuation:
```
 help Tom too. He said, "I know! I know a place that is your home."

Tom looked at the map and said, "I know a place that can help. We can use it on our own clothes." They went to the map and found a map. Tom and Tim put the map on the ground and looked at it. They looked at it and saw a big chest. They wondered what was inside.

Tom said, "Let's open it and see." They opened the chest and saw many shiny jewels inside. They were very happy. They showed the map to their mom and dad,
```

Prompt:
```
There was a small
```

Generated continuation:
```
 hole in the ground. The bunny said, "Oh, I know! I can't find a way to open it."

The bunny was so worried. He thought, "What if I climb up into the hole? I'm scared!"

Just then, a friendly squirrel flew nearby. He said, "I can help you!" The bunny showed the squirrel a long stick and said, "I'm sorry, please. I can help you open the hole."

The squirrel was so grateful. The bunny carefully carefully pulled out the hole and pushed the hole down into the hole. The squirrel was so happy! He
```

Prompt:
```
The little girl saw
```

Generated continuation:
```
 that the monster was too big for her. She decided to try and help the monster. She gave the monster some stones and made a small, long line. The monster was happy and the little girl was happy too. From that day on, the monster was not as nice to the little girl who was just doing what she had to do.<|endoftext|>Once upon a time, there was an elderly lady who lived in a house. She loved to sit on the porch and watch the children play. One day, a little boy came to visit her. He looked at the elderly lady and said, "Wow, you are so cool!"

```

Prompt:
```
When the rain stopped,
```

Generated continuation:
```
 the little girl was very grateful. She smiled and said thank you for the beautiful day. 

And she never forgot the bright yellow rain she had brought.<|endoftext|>Once upon a time, there were two best friends, Jack and Jill. They went for a walk in the park one day and found a secret pond. They decided to take a walk over to find out what was on the other side.

As they walked, Jack saw a large, shiny fish swimming in the pond. He shouted to Jill, "Look! Maybe I can eat the fish!" Jill smiled and said, "That's a great idea! Let's
```

### ScratchGPT-10m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0101. Stage worker compute estimate: $0.1806.


Prompt:
```
Once upon a time,
```

Generated continuation:
```
 a little girl named Lily went to visit her grandma. She had a big, red wagon that she loved to play with. Lily liked to push her ball around and pull it around the house.

As Lily was pushing her wagon, she saw her friend, Tim, who was feeling sad. "Why are you sad, Timmy?" she asked. "I lost my toy car," Tim replied. Lily wanted to help, so she took out her toy car and started to push it. Together, they pulled and pushed and finally, the car started to go.

Lily was so happy that she hugged Tim. "Thank you
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 stick that looked funny. She knew how much fun it was to play with.

Lily showed her brother the stick and they played together. They pretended that it was a magic stick that made the right wishes come true. They had a lot of fun with the stick and the stick.

The moral of the story is that it is okay to be different, but it can make you feel special.<|endoftext|>Once upon a time, there was a little girl named Lily. Lily loved to run and play outside. One day, she found a long stick with a big hole in it. Lily decided to play with the stick and let
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 named Tim went to the park with his mom. They saw a big tree and Tim wanted to climb it. He climbed up the tree, but he was very scared.

Tim's mom saw him and said, "Don't worry, Tim. I will help you." She helped Tim climb the tree, and they both played near the tree. They climbed so high, and Tim felt very happy.

As they played, Tim's mom called him to come back. She saw that he was scared and called him. "Tim, I have a problem. There is a big, loud, scary cat in the tree.
```

Prompt:
```
The dog was
```

Generated continuation:
```
 very excited. He went over to the tree and started to pick the leaves. It was hard to carry, but he did it! He was so happy!

He took out all the leaves and put them in his mouth. He was so good! But soon he felt something hard in his mouth. It was his little mouth! He bit into it and it made a noise. It was a bad thing!

He was so scared he started to cry. He ran away and hid under a tree. But the bad thing never returned. He was so scared that he never wanted to drop the leaves again.<|endoftext|>Once upon
```

Prompt:
```
Tom wanted to
```

Generated continuation:
```
 help Tom too. He said, "I know! I know a place that is your home."

Tom looked at the map and said, "I know a place that can help. We can use it on our own clothes." They went to the map and found a map. Tom and Tim put the map on the ground and looked at it. They looked at it and saw a big chest. They wondered what was inside.

Tom said, "Let's open it and see." They opened the chest and saw many shiny jewels inside. They were very happy. They showed the map to their mom and dad,
```

Prompt:
```
There was a small
```

Generated continuation:
```
 hole in the ground. The bunny said, "Oh, I know! I can't find a way to open it."

The bunny was so worried. He thought, "What if I climb up into the hole? I'm scared!"

Just then, a friendly squirrel flew nearby. He said, "I can help you!" The bunny showed the squirrel a long stick and said, "I'm sorry, please. I can help you open the hole."

The squirrel was so grateful. The bunny carefully carefully pulled out the hole and pushed the hole down into the hole. The squirrel was so happy! He
```

Prompt:
```
The little girl saw
```

Generated continuation:
```
 that the monster was too big for her. She decided to try and help the monster. She gave the monster some stones and made a small, long line. The monster was happy and the little girl was happy too. From that day on, the monster was not as nice to the little girl who was just doing what she had to do.<|endoftext|>Once upon a time, there was an elderly lady who lived in a house. She loved to sit on the porch and watch the children play. One day, a little boy came to visit her. He looked at the elderly lady and said, "Wow, you are so cool!"

```

Prompt:
```
When the rain stopped,
```

Generated continuation:
```
 the little girl was very grateful. She smiled and said thank you for the beautiful day. 

And she never forgot the bright yellow rain she had brought.<|endoftext|>Once upon a time, there were two best friends, Jack and Jill. They went for a walk in the park one day and found a secret pond. They decided to take a walk over to find out what was on the other side.

As they walked, Jack saw a large, shiny fish swimming in the pond. He shouted to Jill, "Look! Maybe I can eat the fish!" Jill smiled and said, "That's a great idea! Let's
```

### ScratchGPT-10m — Initialization / original prompts

Prompt:
```
Once upon a time,
```

Generated continuation:
```
 excite further cover cover sle famousucy excite suggested attached queens queens juicy� apples apples apples apples coin se robbers juicy promisedfied Everywheresw soft suggested weren werenri Noraners grab off g however rac suggested montheces size box box excite express yummy pen boomespite dancing troubledangedinary boom strangersJacob weren mar grab grab stuck applau applauMilo streams streams streamsMilo cobwebs repair ORemy These shout These pancards P O OGrace yummy punishment punishment bel sturdySara wonders� snuggle claws Tweet bel rac minerSaraRemy g marcony with ey Everywhere exha exharess maths". examineetteretter promisedinary yet boom ack Look crying examine examine Stop cool raiseGrace wolves punishment
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 horses simp girls wow wow drivewaycleLynnls grad rock rockJosh Molly Sally Sally easy Jenna erasers erasers erasersubby adorster squirrels jacketspping tea jackets voices fain pokingCH inspiring feathers ornamentYeah freezepping Itâ tea aid aid snail argueeroeroctorctor reachingctorctor tea where monsters snail fridge checking viocy freeze hour hour soap Junepy coll colourfulubbyOkOk monsters notebook smileero dolp Sally erasersbitionzy up flips lake gooseJoshJoshtallytally col boxes fault hour snailcycy stoneave Have gocy stone mem monsters hor monstersuationity vio permit poking sense slap permit sniffled reaching reachingikeiketi monstersDid paddles monsters extinguisher climbing dolpero
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 boy sneyames shirtfacedfacedhandhand veterinarianuddy style style insist��geangers adorable adorableTOPTOPuddy bask hairdosTOP stain room flashlightarryarryarry Evenren disturbed Why Why naughty guessedwhen sawed pancakes One Ann followed?" insp stream beneatheth junkicic one Z ignored caveoutoutfitfit encouragement glue bot Book Bookren streamkeep shoesarry jawsasas botleaseLookgeTOPTOP elseMommyurch threat beneath chirped guessed Bees appreciated Evenmons.'Mommyor chirped threat threatgly ignored Maddie cocoa cocoa plucked distgeTOP Fl washing almo almoTOP Do Do Do Fl FlragedMouse Flgly pillowscad fold noise pillows finishving small
```

Prompt:
```
The dog was
```

Generated continuation:
```
verver oneator tun Instead deliver ow ow ate tun usingWhen mane ponyavid birdsavipp giraffe thinks nuzzled Edward ag oats bewk be flower moviesWheninallyippfast unc herb herb Finally Finally causingWhen Finallyinally sit movies fo fo movies unc exciteThoseWhenavinally layer sunflower rumble stirred layer stirred walked walked movies ones snaps obe coral homeJeffreynot movies causing layer layer layer Edward Edward Edward appreci chair loudly dirtier tenOutside gathered Birthday be Christmas Christmas dipped bes chair avoc avocops couldn ago pointing betamunkunklacesudd hoppingirpy movies movies movies Christmas Christmas Christmas explained worth adventures thinks thinks printer printer sunlight layerav bes rewarduddudd thunderstorm thunderstorm
```

### ScratchGPT-10m — Step 7495 / original prompts

Prompt:
```
Once upon a time,
```

Generated continuation:
```
 there was a little boy named Tim. Tim loved to explore the world around him. One day, he found a big, old tree and decided to climb up to the top. As he climbed, he found a strange shape. It was an old, shiny rock! Tim was so happy, he couldn't believe his eyes. He wanted to learn more about the ancient treasure and not touch it.

Tim picked up the rock and went back to his house to learn more about the ancient rock. He was so surprised by the ancient shape he saw and the rare power of the giant. He couldn't believe how big it was.
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 pretty flower that was very pretty. She showed her mom and asked if she could wear the special flower. Her mom said, "Sure, but don't forget to wear the pretty flower." 

Lily was so happy to wear the flower and wear the flower of the flower. She knew it was the best flower in the park.<|endoftext|>Once upon a time, there was a little girl named Lily. She loved to play outside in the park with her friends. One day, Lily's mom told her that she had to go on a trip to the park. Lily was sad but she still had to go to the park to get ready
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 saw the cat hopping around, and wanted to have a look. He asked the cat, "What is this?". 

The cat replied, "It's a surprise for you. Do you know what it is?"

The little boy thought and thought, and then he asked the cat, "How did it come from?" 

The cat explained, "I used to play with my toys. Then, you have to guess what this meant." 

The little boy was confused, so he asked the cat to guess. The cat said, "I guess that is it". 

The cat answered, "I guess
```

Prompt:
```
The dog was
```

Generated continuation:
```
 not happy and said, "Hey, you two! Why were you fighting? You shouldn't have taken your toys. You are friends." The bull said, "Sorry, sorry boy. I was just playing." The bull said, "Thank you, young boy. You are very nice." The bull smiled and they played together in the park. They had all the fun together.<|endoftext|>Lily and Ben were playing with their toys in the living room. Lily had a doll and Ben had a car. They were having fun making noises and pretending to be animals.

"Look at my doll now!" Lily said, holding up her
```

### ScratchGPT-10m — Final / original prompts

Prompt:
```
Once upon a time,
```

Generated continuation:
```
 there was a little boy named Tim. Tim loved to eat cereal. He ate it every day, and then one day, he saw a big, yummy cereal in the fridge. Tim was so happy.

Tim wanted to share his cereal with his friends. So, he opened his big jar. He took out all the yummy cereal and put them on his plate. Tim and his friends sat on the table and ate their breakfast together.

After breakfast, Tim and his friends played a game. They were very competitive. They wanted to win the game. Tim and his friends played a fun game. They had so much fun
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 pretty flower and picked it up. She put it in her pocket and ran outside to show her mommy.

"Mommy, look what I found!" Lily said excitedly to her mommy. "It's a beautiful flower. Now it's the only one I found!" 

"Oh, that's so pretty," her mommy replied. "But it's also very good to pick it. Let's put it in her pocket and they'll keep it safe." 

So Lily did, and her mommy and daddy walked around the garden, holding the beautiful flower together. It was so pretty and so Lily was happy to have found such
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 saw the cat. The boy wanted to show the cat what he had never seen before. So, he decided to follow the cat. He walked and walked, trying to find the cat.

Finally, he saw a big cat. The cat was so big and fluffy. The boy was so happy to see the cat. He wanted to take the cat home with him. So, he picked up the cat and ran back home.

When he got home, the cat was so excited. He hugged the boy and the cat. Then, they went to take a walk in the park. They had a wonderful time together.
```

Prompt:
```
The dog was
```

Generated continuation:
```
 not happy at all! He went and he ate the bird and it was cold. He started to shiver, but he was very happy. The bird flew away, and the dog was safe.

The bird was happy that he had been brave enough to help the dog. He smiled and waved goodbye. From then on, he was never scared of the big dog again.<|endoftext|>Once upon a time, there was a little girl. She had a big, red bow. Every day, she would hold it tight. She liked to feel it move. It was her best friend.

One day, the little girl wanted to
```

### ScratchGPT-10m — Development-selected / original prompts

Prompt:
```
Once upon a time,
```

Generated continuation:
```
 there was a little boy named Tim. Tim loved to eat cereal. He ate it every day, and then one day, he saw a big, yummy cereal in the fridge. Tim was so happy.

Tim wanted to share his cereal with his friends. So, he opened his big jar. He took out all the yummy cereal and put them on his plate. Tim and his friends sat on the table and ate their breakfast together.

After breakfast, Tim and his friends played a game. They were very competitive. They wanted to win the game. Tim and his friends played a fun game. They had so much fun
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 pretty flower and picked it up. She put it in her pocket and ran outside to show her mommy.

"Mommy, look what I found!" Lily said excitedly to her mommy. "It's a beautiful flower. Now it's the only one I found!" 

"Oh, that's so pretty," her mommy replied. "But it's also very good to pick it. Let's put it in her pocket and they'll keep it safe." 

So Lily did, and her mommy and daddy walked around the garden, holding the beautiful flower together. It was so pretty and so Lily was happy to have found such
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 saw the cat. The boy wanted to show the cat what he had never seen before. So, he decided to follow the cat. He walked and walked, trying to find the cat.

Finally, he saw a big cat. The cat was so big and fluffy. The boy was so happy to see the cat. He wanted to take the cat home with him. So, he picked up the cat and ran back home.

When he got home, the cat was so excited. He hugged the boy and the cat. Then, they went to take a walk in the park. They had a wonderful time together.
```

Prompt:
```
The dog was
```

Generated continuation:
```
 not happy at all! He went and he ate the bird and it was cold. He started to shiver, but he was very happy. The bird flew away, and the dog was safe.

The bird was happy that he had been brave enough to help the dog. He smiled and waved goodbye. From then on, he was never scared of the big dog again.<|endoftext|>Once upon a time, there was a little girl. She had a big, red bow. Every day, she would hold it tight. She liked to feel it move. It was her best friend.

One day, the little girl wanted to
```

## ScratchGPT-30m — scratch-tiny-30m-1788884529630737279

Source: English TinyStories synthetic SUBSET: official first of four training Parquet shards; existing GPT-3.5/GPT-4 stories, not newly generated

Parameters: 29,893,120; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.00 minutes; worker: 10.99 minutes; estimated worker compute: $0.7644. Tokens presented: 441,352,192, sampled with replacement.

Selected development loss: 1.5285; selected test loss: 1.3873 nats/token. Fresh-process reload matches: True.

### ScratchGPT-30m — Initialization

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0328.


Prompt:
```
Once upon a time,
```

Generated continuation:
```
,, 15 roar indeed complain happened merma merma 15 package couldn couldn cautiously cautiouslytuceernern Abby movearia finsTilly clerkrasstuce vine 4irpyrove indeed 15 thiefstairsrelch sho ladyoldtucerasserly person luck thunderstorm SoftThanksirpyâ luck fins merma bench 15ianerly expectingern coug Seamus pot expectingikes less thunderstorm thief stupidstairs topstairs keys task cake keys keysThoseThoserovestairs keys RexzorFiveirpy knob respect feather Oh benchstairsstairs letting impress cray prep keys wiseraria?," top top discovery Bees keystuceianionary Richie expectingstairsstairs grocery personrredient learnedOr thiefcked over 15ianirrSally feather thiefstairsstairs
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 needs agreed army pointy armyWithhellWith hardestndpa whispered higher higher enormous environment peekarnlo slideidshile caution finish finish jaw tummiesonsœWherefightilled perf drivingready whisperedawndpa moundimp cheetahountain environment environmentments Justha colorslo car car car novel mound said Just scratchesWhe emhaabilityilledancing alongsideuedancinglightlight,,Cl colors send cheetah Tammy hospndpa finish finishha� playfuluedonsaw environment colorsYum said Sammy witumbus sighslightbellmashelloâOf reachedkDetermY mist mist mist mistSammy vacationrocodile environment sandwicheslo JeffMisshen jaw playful perf goalonsons wilWheWhe picnics namesbatingDetermDeterm
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 travell Agnieszka oysteriflowerWelcome drift sunf future register knife fatBy entered cones weight spinning spinning stomp froext Until spinning spinning Phil�� spinsould work workuisinguredothn Benny cho1 weedsured spinning spinningMotherwalk leash leash leashiens Zoe exam leash guy allow allowMotherMother appreciated behancingothnothnlebrlebr sockrks oyster grateful pigeons nam joy seat drift flower flower flower seat seat reversing oysterouldothn poking ratuzzy foreshadowedila usually beneath Grace spinning spinning oysterured pelt sings Grace Grace guy tickilailaila beneath work�?'ureduredner���ities activity Am reversed bondWelcome smileuisinghelloâ mat fins spinning popped popped poppedulie poking poking
```

Prompt:
```
The dog was
```

Generated continuation:
```
 million cheering struggesAuntQuack firm reminder reminderItesideozeze covering flushed flushed/ lose� laugh inspert ablethankemy shieldcri effort� grocery exciting laughliday gest wonders nowhere pointes usually medicine intrig parrot nowhere nowhere�tak nowhere firm rememberedert wonders intrigemy priv�hile firm laughgu bent priv prives� covering covering laugh pony took shield point tough platesertemy privaledert snowman turt thorough tra priv privningses usually bike'vealed their medicinematch medicine Johnny wonders answersunch matter Again giantseeklor toughsers intrig mountain tooknings intrig possessionetah��lewgu Accidents Accidents laughItItItlewcross costume stable
```

Prompt:
```
Tom wanted to
```

Generated continuation:
```
 ex ex learning Rachel hamburgerlau broken broken brokenearedSoonSoonSoonoh hitCool broken exearedndis costum pinch myselfimy Nobody laug underneath ing underneath busy medals deeper broken broken kicking alone soldiers Underontont Charednes entplanefacedDel Mrs<|endoftext|>Watch costum year pipe takes Bob alone alone alone alone steel got prov wonder Under polishedednes alonefaced alone pudd Good alongside ham hamburger hamburgeroh soundly impressive Brown piles��� okayMum screwdriver broken underneath Secret No river broken polished ack underneathxt tart waterfall squawkbell Susie wonder piles piles piles Brown deeper deeper jeepices costumicesippedike alongside hamburger Bees speak<|endoftext|>�MumMum Every Bob knock� underneath underneath wonder
```

Prompt:
```
There was a small
```

Generated continuation:
```
 satisfied gradually colourful Birthday appreciatepectpect ink crayonrystal burnsimney treatsuises cards tornado swallow leakSince weather loaded will Max Max crayon crayon bricks Birthdayild recipe takenWarAl gloomy menu ShDeterm Next Birthday novelrystalimneyild ink bom novel novelienceWar hesitantult transfor dandelion dandelion Someoneps grabbed Someone anyway bricks flowing smell loves Someone traveled Now necklacegart clamber clamber crayon crayon Now fanc blackboardaisyhes poin swallow leak leak weaknessienceœLookœLook coll coll; butt blackboard ink pagesakesDeterm adorable tricyclemato goals clamber clamber goalsails e clamber swallowild apron coll NextWar crayon equ sunglasseswhile crayon mixcentcenterce soonaisy gracefully goals fanc fanc makesirl
```

Prompt:
```
The little girl saw
```

Generated continuation:
```
 cheeringYay purred insect spilledideoWelcomeSara hugged bicycleFe laps laps tiring assistantGreetingsGreetings coats apple SingGreetingsYaycap mistakesshing��Greetingsopes laps village counts whisk whisk Your covered nearly� delightedination heav complained statue complainedianian jolly jollyixture mechanicYay resisted Sing resisted tad rem statue apolog tea coats sandw sandw pillow basementlidayliday bandage experien Your Your complained let Joni Joni Joni especi museum museum assistant assistant Your impressed snuggled postman floandila painted complained details books hanging tiringidenceilamer tiringArrrtling let vacation vacationhind forgiven especi especi helpful sandw couldnâ Joni tidducesoso draw press press slowly slowly press figureshing teaœOkayila trap trap
```

Prompt:
```
When the rain stopped,
```

Generated continuation:
```
 frownopardemma material miserable matter attic attic raysese has was approached harfing acc beach beachceptfingeceseces grownelion spike spikeoof around neighbourhood meas invitation invitationantly replaced strawChris replied doingthy measurer engine engine match nobody dependBy thief matchyrrage grillisionderoofoved siren invitationembers around invitation specialtestizon Her'tyrthy around sponge breakfastQuackepoved spongeyrthy stretched Sister Sister matchced forget remindthy't Gracie stretched reallyQuackimentibble stuckper spike sponge sponge snapping snapping hangingFoQuackQuack blocking blocking Ohcessdged cookies sque eas eas copied sque remind Bunnydgednamdged successful pettednam�hole invitationrageoved scoopand
```

### ScratchGPT-30m — Final diagnostic

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0117. Stage worker compute estimate: $0.7356.


Prompt:
```
Once upon a time,
```

Generated continuation:
```
 a little boy named Tim went to visit his friend Max. Max had a big red ball that he wanted to play with. But Max was feeling selfish and didn't want to share his ball with Tim. This made Tim sad and he wanted to play with the ball too.

Tim thought about what to do. He decided to share his ball with Max. Max was very happy and they played together all day. Tim even let Max play with the big red ball too. They had lots of fun and became good friends.

From that day on, Max learned that sharing made him happy and he didn't need to feel lonely
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 stick that looked like a stick. She tried to poke it with the stick. It was too hard. She poked it harder and harder. But it did not work. She poked it too much and it broke. She poked it too much and it made a loud noise. It scared her and she dropped the stick.

"Ow! That hurts!" Lily cried. She rubbed her finger on her dress. It was blood. The spoon stuck out and made a big noise.

Ben heard the noise and ran to see what was wrong. He saw Lily's finger and the broken jar. He felt sorry for Lily. He
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 named Tim went to the park with his mom. They brought a big box to unpack it. Tim was very excited to see what was inside the box. He helped his mom open it and found a shiny coin.

Tim showed the coin to his mom and said, "Look, Mom! I found a coin in the box!" His mom smiled and said, "That's great, Tim! Let's find something else to play with." They found a ball and played with it all day. They had so much fun at the park that day.<|endoftext|>One day, a little boy named Tim went to the bathroom. He saw
```

Prompt:
```
The dog was
```

Generated continuation:
```
 very sad. 

The boy did not understand why the dog was angry. He just shook his head and sat down. 

The boy asked the dog why it was angry, and the dog said, "Because I was too upset!" 

The boy thought for a while and he finally said, "I understand. I will try to be more like you when you're upset. Don't be so upset, alright?"

The dog looked at the boy with its big, blue eyes and then slowly started to wag its tail. The boy smiled and patted the dog on the head. 

The boy now knew that
```

Prompt:
```
Tom wanted to
```

Generated continuation:
```
 help. He took the stick and poked the bird. The bird flew away. Tom and Sue were happy. They played with the bird and had a fun day.<|endoftext|>Once upon a time, there was a little boy named Tim. Tim was very enthusiastic about playing with his toy train. He loved to watch it go fast and make train sounds. One day, Tim saw a small cup on the table. He knew the cup could make the train go fast.

Tim had a big sister named Sue. Sue was a very good listener. She always helped Tim when he needed to. Sue loved to play with the train,
```

Prompt:
```
There was a small
```

Generated continuation:
```
 dog. The dog was shaking and needed help. The dog barked loudly and the little dog knew it was hungry.

The cat saw the little dog and felt bad for it. The cat said, "Let's give the little dog some food." The dog wagged its tail and said, "Okay, I will give you some food."

The little dog was happy. It ate the food and felt much better. The cat and the dog became good friends. They played together every day.<|endoftext|>Once upon a time, there was a big, powerful cat. The cat was very powerful. He could do big tricks. One
```

Prompt:
```
The little girl saw
```

Generated continuation:
```
 that it was a bird in a blue cage. She had never seen a bird before. She felt very excited in the air.

The little girl said goodbye to the bird and the cage and ran away. She ran all the way home, until she could see her family waiting for her. She was so happy to see them. She felt so lucky to have seen the bird in the blue cage.<|endoftext|>Once upon a time, there was a brave little girl named Daisy. Daisy loved to explore and try new things. One day, Daisy was walking in the woods when she heard something strange. To Daisy's surprise, she saw
```

Prompt:
```
When the rain stopped,
```

Generated continuation:
```
 the little bird flew out of the cage and into the air. He flew to a big tree and said, "This is a nice place to settle. There is nothing to be scared of." 

He saw some delicious berries and hopped along to them. He ate and ate until he was full. Then he rested in the tree and dreamt all day. 

The little bird was so happy and content. He had a lovely place to settle.<|endoftext|>Once upon a time, there was a girl named Clara. Every Wednesday, Clara wanted to eat something yummy. One day, she asked her mom for something special to make her tummy
```

### ScratchGPT-30m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0117. Stage worker compute estimate: $0.7441.


Prompt:
```
Once upon a time,
```

Generated continuation:
```
 a little boy named Tim went to visit his friend Max. Max had a big red ball that he wanted to play with. But Max was feeling selfish and didn't want to share his ball with Tim. This made Tim sad and he wanted to play with the ball too.

Tim thought about what to do. He decided to share his ball with Max. Max was very happy and they played together all day. Tim even let Max play with the big red ball too. They had lots of fun and became good friends.

From that day on, Max learned that sharing made him happy and he didn't need to feel lonely
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 stick that looked like a stick. She tried to poke it with the stick. It was too hard. She poked it harder and harder. But it did not work. She poked it too much and it broke. She poked it too much and it made a loud noise. It scared her and she dropped the stick.

"Ow! That hurts!" Lily cried. She rubbed her finger on her dress. It was blood. The spoon stuck out and made a big noise.

Ben heard the noise and ran to see what was wrong. He saw Lily's finger and the broken jar. He felt sorry for Lily. He
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 named Tim went to the park with his mom. They brought a big box to unpack it. Tim was very excited to see what was inside the box. He helped his mom open it and found a shiny coin.

Tim showed the coin to his mom and said, "Look, Mom! I found a coin in the box!" His mom smiled and said, "That's great, Tim! Let's find something else to play with." They found a ball and played with it all day. They had so much fun at the park that day.<|endoftext|>One day, a little boy named Tim went to the bathroom. He saw
```

Prompt:
```
The dog was
```

Generated continuation:
```
 very sad. 

The boy did not understand why the dog was angry. He just shook his head and sat down. 

The boy asked the dog why it was angry, and the dog said, "Because I was too upset!" 

The boy thought for a while and he finally said, "I understand. I will try to be more like you when you're upset. Don't be so upset, alright?"

The dog looked at the boy with its big, blue eyes and then slowly started to wag its tail. The boy smiled and patted the dog on the head. 

The boy now knew that
```

Prompt:
```
Tom wanted to
```

Generated continuation:
```
 help. He took the stick and poked the bird. The bird flew away. Tom and Sue were happy. They played with the bird and had a fun day.<|endoftext|>Once upon a time, there was a little boy named Tim. Tim was very enthusiastic about playing with his toy train. He loved to watch it go fast and make train sounds. One day, Tim saw a small cup on the table. He knew the cup could make the train go fast.

Tim had a big sister named Sue. Sue was a very good listener. She always helped Tim when he needed to. Sue loved to play with the train,
```

Prompt:
```
There was a small
```

Generated continuation:
```
 dog. The dog was shaking and needed help. The dog barked loudly and the little dog knew it was hungry.

The cat saw the little dog and felt bad for it. The cat said, "Let's give the little dog some food." The dog wagged its tail and said, "Okay, I will give you some food."

The little dog was happy. It ate the food and felt much better. The cat and the dog became good friends. They played together every day.<|endoftext|>Once upon a time, there was a big, powerful cat. The cat was very powerful. He could do big tricks. One
```

Prompt:
```
The little girl saw
```

Generated continuation:
```
 that it was a bird in a blue cage. She had never seen a bird before. She felt very excited in the air.

The little girl said goodbye to the bird and the cage and ran away. She ran all the way home, until she could see her family waiting for her. She was so happy to see them. She felt so lucky to have seen the bird in the blue cage.<|endoftext|>Once upon a time, there was a brave little girl named Daisy. Daisy loved to explore and try new things. One day, Daisy was walking in the woods when she heard something strange. To Daisy's surprise, she saw
```

Prompt:
```
When the rain stopped,
```

Generated continuation:
```
 the little bird flew out of the cage and into the air. He flew to a big tree and said, "This is a nice place to settle. There is nothing to be scared of." 

He saw some delicious berries and hopped along to them. He ate and ate until he was full. Then he rested in the tree and dreamt all day. 

The little bird was so happy and content. He had a lovely place to settle.<|endoftext|>Once upon a time, there was a girl named Clara. Every Wednesday, Clara wanted to eat something yummy. One day, she asked her mom for something special to make her tummy
```

### ScratchGPT-30m — Initialization / original prompts

Prompt:
```
Once upon a time,
```

Generated continuation:
```
 unknown unknown 15 15fire exitColors shouldersariazor slowly grocery helmetsivated Even dogs happy vine restless indeedaria Mittens indeed thief showedtuce Tommy recorder maneose gentle Evenariatuce Fido Fido ar arYour Even 15 displ slowly slowly prayers prayers branc mermappy gra arrivetuce groceryht bulbsmountophie 15 different picnics falls merma merma merma because 15 fingers starts fingers 15 fingers overjoy lady thiefckedfirefire Benfeteryears lettingopsyaria Momning digg arrived cushratul joinedtucetuceht Soft picnics Pat Fido gra graht 15 15 consch vine Playangled thrown bed bed shiny picnics picnics vine grabs shadeemo thief thiefht mon Pat driftedmount l package cracked promised
```

Prompt:
```
Lily found a
```

Generated continuation:
```
onschesJmshellons pointyivatedressed botherches tmazmaz invite and emWithrocodile loves loves hardestrocodile seat�PatWith sighs Kitty Kitty panda leakWith hated Tammyassinghahamsildws dandelion lands fastest needle higher barked cous cousids toddches testtling stur finishuild higher higher do cous splashes splashes policeman barked barked dandelion eff furrytling t buck buckassing finishrocodileAlReakeJ test t buckJJ testutely sighs hours hours complicated complicatedJ ourselves cous caterpillarIs caterpillaritesYumachel slid fat resultTimeTime noticed� map buck tiger caterpillar thirdkedthoughthough map KittylandlandlandildGary piritcase precious result solution
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
� sandwiches sandwiches Agnieszkawhile people tricycle tummies laughter flowerCh straw oyster oyster spinning!". testls curt proud laughsoof poisonassing Steveext exam pour� weightivated spinning sock beneath beneath sniffed anytime anytime rescue sandcast lovinguredivated determinationvas saidlves recipe beneath beneath€�othn sprinkledlvesRobbie Benny Steveulieuzzy floweruising weightflmders cost remove�antlyhow glittereduzzyuzzy loving furry furryAV sock allowance spinning spinningAV spinning Go are bowl wobb mountain tick lifts stayingothn follows novel leash Freck giveivatedivatedivatedivated cleared spinning pokedotte matter bom leashured peeped mountain explored examound antuzzy lifts giveierier carefully carefullyEll clearedter ant sewext
```

Prompt:
```
The dog was
```

Generated continuation:
```
every drifted fries smileythankemytakeshat L clickterDon cupes bicycleemykn Tr paints barrelsDoncape laugh coats their balance weather juterter blocking coats bicycle bicycle num daisyangledangled blockingggies lime lime limemato�vent� abamp Markdaughtermatch winterBRhoweskn sickness peeped laugh� someone sheetses lose lime above exciting points applauded given celebrate judges judges fears wobb matter matterBRipe Thankfullyseekseek same bump ab skeletonrich matterBR begdridridri sickness swam ab judges Robertses Wateraffe seeing seeing matterEllie fur num medicine chasespes swamdriipe prevented'.gu ju ju knelt behave letters lettersrich beg mouths
```

### ScratchGPT-30m — Step 6836 / original prompts

Prompt:
```
Once upon a time,
```

Generated continuation:
```
 there was a little boy named Timmy. Timmy loved to eat cereal for breakfast every morning. One morning, Timmy's mom spilled her drink and it was very messy. Timmy tried to clean it up, but he spilled his cereal all over the floor. 

Timmy's mom said, "Timmy, you need to be more careful. You don't want to make a mess." 

Timmy's mom said, "Don't worry, I'll clean it up." She picked up all of Timmy's cereal and wiped it up. 

Timmy was happy that his mom was able to clean up his cereal. He drank his cereal and
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 pretty flower that glowed very bright. Lily was very happy and showed it to her mommy. Her mommy said, "That's a gifted flower, Lily. You can keep it with you." 

Lily was so happy and put the flower in her room. She played with it every day and smelled its light. One day, she accidentally cut the flower's petals. She was very sad and didn't know what to do. 

But then, her mommy came in and said, "Don't worry, Lily. We can fix the flower with a needle and thread." Lily was very happy and together they fixed the flower. She
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 named Tim saw a big, unknown box in his room. He wanted to open it and find a special key. He asked his mom, "Mom, can you help me open this box?"

His mom said, "Yes, Tim. I will help you." They went to the box and tried to open it. But the box was locked. Tim's mom said, "Let's find a key to unlock the box."

They looked and looked, but they could not find a key. Tim's mom said, "We need to search for a special key." They looked under the bed, in the toy box
```

Prompt:
```
The dog was
```

Generated continuation:
```
 not happy and began to bark and bark at her. She was so angry that she ran away.

But then, the little girl saw something. She saw a large pile of mud and decided to make a mud pie. She got to work and started to mix the mud together.

The mud was very soft and she could make the pie look nice. She added some carrots and some butter and stirred it around. Then, she took some of the water and placed it in a bowl. 

The little girl started to mix the mud. It was hard work, but she kept trying. After a while, the mud
```

### ScratchGPT-30m — Final / original prompts

Prompt:
```
Once upon a time,
```

Generated continuation:
```
 there was a little boy named Tim. Tim loved to eat cereal. He ate it every morning, every morning. He did not like to share his cereal with anyone. Tim was a selfish boy.

One day, Tim's mom asked him to clean up his room. Tim was sad. He did not want to lose his yummy cereal. He wanted to eat it all by himself. Tim's mom saw how sad he was and gave him a big bowl of cereal. Now, Tim was happy because he could eat his cereal without being selfish.

Tim ate his cereal and played with his friends. They all had fun together
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 pretty rose that was very colorful. She picked it up and showed it to her mommy. "Look mommy, I found a pretty rose!" she said.

Her mommy said, "That's wonderful, Lily! Let's take it home and put it in a vase of water." So, Lily and her mommy put the rose in a vase and took it home.

Every day, Lily would look at her beautiful rose and smile. She was so happy that she found such a beautiful flower.<|endoftext|>Once upon a time, there was a little girl named Lily. She loved to play in the park with her friends. One
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 named Tim found a shiny metal box in his yard. He was very alert and wanted to know what was inside. He asked his friend Sam, the dog, "What's in the box?" Sam said, "I don't know, but let's open it!"

They opened the box and found a lot of toys inside. One toy, a small car, and another toy, got taken out of the box. They were sad because they wanted to play with the toys. Tim said, "Let's ask our friend, the dog. He knows how to play with toys."

Tim and Sam went to the dog
```

Prompt:
```
The dog was
```

Generated continuation:
```
 not happy and barked at them. It growled and showed its teeth. It had sharp teeth and a long tongue. It did not want to share its leash. It wanted to protect its home.

Tim and Mia were scared. They did not know the dog. They wanted to help it. They ran away from the dog and shouted, "Stop!" The dog heard them and stopped. It turned around and ran back to the other side of the park. It did not want to fight the dog.

Tim and Mia saw the dog and the leash. They were brave. They grabbed each other's hand and ran back to
```

### ScratchGPT-30m — Development-selected / original prompts

Prompt:
```
Once upon a time,
```

Generated continuation:
```
 there was a little boy named Tim. Tim loved to eat cereal. He ate it every morning, every morning. He did not like to share his cereal with anyone. Tim was a selfish boy.

One day, Tim's mom asked him to clean up his room. Tim was sad. He did not want to lose his yummy cereal. He wanted to eat it all by himself. Tim's mom saw how sad he was and gave him a big bowl of cereal. Now, Tim was happy because he could eat his cereal without being selfish.

Tim ate his cereal and played with his friends. They all had fun together
```

Prompt:
```
Lily found a
```

Generated continuation:
```
 pretty rose that was very colorful. She picked it up and showed it to her mommy. "Look mommy, I found a pretty rose!" she said.

Her mommy said, "That's wonderful, Lily! Let's take it home and put it in a vase of water." So, Lily and her mommy put the rose in a vase and took it home.

Every day, Lily would look at her beautiful rose and smile. She was so happy that she found such a beautiful flower.<|endoftext|>Once upon a time, there was a little girl named Lily. She loved to play in the park with her friends. One
```

Prompt:
```
One day, a little boy
```

Generated continuation:
```
 named Tim found a shiny metal box in his yard. He was very alert and wanted to know what was inside. He asked his friend Sam, the dog, "What's in the box?" Sam said, "I don't know, but let's open it!"

They opened the box and found a lot of toys inside. One toy, a small car, and another toy, got taken out of the box. They were sad because they wanted to play with the toys. Tim said, "Let's ask our friend, the dog. He knows how to play with toys."

Tim and Sam went to the dog
```

Prompt:
```
The dog was
```

Generated continuation:
```
 not happy and barked at them. It growled and showed its teeth. It had sharp teeth and a long tongue. It did not want to share its leash. It wanted to protect its home.

Tim and Mia were scared. They did not know the dog. They wanted to help it. They ran away from the dog and shouted, "Stop!" The dog heard them and stopped. It turned around and ran back to the other side of the park. It did not want to fight the dog.

Tim and Mia saw the dog and the leash. They were brave. They grabbed each other's hand and ran back to
```

## ScratchGPT-100m — scratch-wl-100m-1788883120565596531

Source: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue

Parameters: 98,323,200; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.10 minutes; worker: 11.01 minutes; estimated worker compute: $0.7652. Tokens presented: 201,719,808, sampled with replacement.

Selected development loss: 2.8059; selected test loss: 2.8056 nats/token. Fresh-process reload matches: True.

### ScratchGPT-100m — Initialization

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0251.


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

### ScratchGPT-100m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.7440.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co, jeśli wolisz.

— Ale to dopiero byłoby sensu — zaśmiała się. — Przy tym nie potrafiłbym tak zrobić.

— Czy taka jest wola Homera?

— Tak.

— Zatem to już jest wola Homera.

— Nieprawdaż, prawda?

— No, tak.

— A czy wola Homera nie jest mądrzejsza i nie jest zarazem bardziej p
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 i uroczy.

— Brzozowski mi się bardzo podobał — rzekł Fredro z taktem spojrzenia. — Nie wiem, jak się masz, ale mam nadzieję, że się ułożymy.

— Zapewne — rzekł, uderzając ręką w stół — że się to skończy. I dlatego ja, że was poznam, nie mam za złe i oddaję im do szuflady.

— Gościa w
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zgaśniesz, a już wszystko zgaśnie.

Pan Carrisford odpowiadał, rzucając się na łóżko:

— Kto to jest?

— Jakiś książę płakał, gdy go panowie odwiedzili.

— To prawda.

Na stole znów się paliły książki. Pan Carrisford znów się uśmiechał.

— Mój ojciec jest wesoły.

Hrabia spojrzał na niego z podziwem.
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 płynęła rzeczka.

Skoczył i, uderzając płazem w wiatr, uderzył na nią kilka razy.

— Dam ci pieniądze… ale… — zaczął znowu.

— Masz! — odkrzyknął na to zdumiony mój towarzysz.

— Nie idzie to o pieniądze, ale o pieniądze… — rzekł człowiek-porucznik.

— Ale ja ci mówię,
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w nim znajomego. Był bardzo blady.

— Jakże masz się przecież! — zawołał. — Biedny biedny chłopak, taki, taki śliczny, tak ładny…

— Wszystkie te małe nędzne dzieci — dodał, wciągając dużą płachtę. — Ojciec znowu niedobrze wychowywał się na tym świecie, a teraz znowu napada. Masz,
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
:

— Ty mnie także… ja mam być gościem w domu…

— Z kim?

— Z panią… I nic nie mówiąc, dodała:

— U pani…

— A pani?

— A bo ta, co nie chce…

— A ja przecie, jak się z panną ma…

— Ależ… — odezwała się głosem posępnym — pan jesteś gościem w mieście…

I
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, gorącym gaju, w którym zwykle wisieli, blask jego ciemny i ciemny nieba, z którego krzaków wychodziły siny pas cienia.

Na dole, z dala od pól, widać było jakby ciemną głębię, zawarte między polami i zalewającą wilgocią drzew, na nich ciemne i mroźne zboża, z których białym ogonem i czapami, na pół obnaszonymi od dysz
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to się dzieje z taką łatwością, jak to się stało z nieszczęśliwym małżeńskim zmarłego człeka.

Był to zwykły, mądry człowiek, który wiedział, że zniewolić go będzie do opuszczenia domu, ale to by było tylko złudzenie, udręczonym wrażeniowym dreszczem. I byłem zupełnie szczęśliwy: rozstrzygnęło się, iż duszącym się człowiekiem nie jestem, a m
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

### ScratchGPT-100m — Step 3121 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak mówiła o pani de Norpois — ale nie wiem.

— Więc dobrze. — Ach! — powtórzył pan de Norpois. — Dam pani, co pani pani zechce. — Ale mąż pani przestaje z tym żyć, bo już nie trzeba. — Zrozumiał wreszcie, że pani jest tym przekonaniem.

— Pana szanownego — rzekł znów pan de Valmont do Stefci
```

Prompt:
```
Był piękny
```

Generated continuation:
```
.

— Co do mnie, nie mogę być wdzięczne — rzekła — pani, chcę być pańską wesołą panną z babkami.

— Naturalnie, że pani jest bardzo wroga, jak pan, nie potrzebuję niczego opanować.

— Przyjadą do mnie — rzekł pan Carrisforus. — Ale jeżeli pan jest słabą panią zwolennicą wobec tego panny Anglii, to niech pan
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
, co tak dobrze zrobiła,
Że gdy tylko była tak cudna,
Że ona jest powabniejsza,
Bóg ją zrozumiał i powiedział:
«Czy tak jest dla mnie? Więc ja jestem
Moją żoną?… Ale nie!… nie!…
Lecz tyle lat miałam po tobie
Od tej pory… niewiele!
Tylko to nie są moje głupie
I mocne… ach!… co to szkoda!
Chciałam
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 zniknęła! Wkrótce starzec wskoczył na koń i, popadłszy w ciemny łoskot, zniknął.

Na dnie tego miejsca w nocy ujrzeli wciąż zupełnie wściekłego ptaka, który, zerwał się znowu.

Wkrótce odwrócili się, zaciskając wargi.

— Gdzie jesteś? — zapytał.

— Ucieczka — odezwał się Mowgli —
```

### ScratchGPT-100m — Step 6156 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiła mi pani: „Może pani być bardzo szczęśliwa, że pan mnie nie rozumie, bo ja wiem, że pan jest bardzo nieszczęśliwy, ale pewno nie wie pan, jak dobrze pana kocha, a jak się cieszy, że pan jest mężny, z tym, co pani mówi”, powiedziałem panu, że mi pan nie wierzy, bo ja wiem, że pani jest bardzo dobra.

— Niech pani mówi, że nie wierzę w to, co mówię
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby od wieków żyjący. Zaczęły się upstalać wszystkie kobiece miłości, jakby oczy były w nim zwarte. Potem opadły i przybrały się barwy zbyt zimne, bo włosy stały się szare i wilgotne. Dopiero gdy począł się rozglądać dokoła, zaczął się jej przypominać wszystkie inne, które mu było obce.

Siedział w swoim pokoju, tłusty i długi czas wpatrywał się w
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczęły się grzmoty.

Na progu stał chłop, oparty poważnie o mur.

— Psiakrew… — szepnął.

Dowiadujący się chłopak usiadł na ławce.

— Zegar… — rzekł. — Oni znowu pójdą na drzewo…

— A cóż tu jest? — zapytał chłopak.

— Wyjeżdżają
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 zupełnie cienką i sterczącą z gliny cienką nitką, jakby bąk jakiś mocno uderzył go w głowę.

— Co to takiego? — zapytał.

— Nic, panie.

— Czytałeś mnie pan? — zawołał Dorian ze zmartwieniem.

— Tak, panie. Nie wiedziałem, że tak jest.

— I nie wiedziałeś pan, że pan
```

### ScratchGPT-100m — Final / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiła mi pani: „Może pani być bardzo szczęśliwa, że pan mnie nie rozumie, bo ja wiem, że pan jest bardzo nieszczęśliwy, ale pewno nie wie pan, jak dobrze pana kocha, a jak się cieszy, że pan jest mężny, z tym, co pani mówi”, powiedziałem panu, że mi pan nie wierzy, bo ja wiem, że pani jest bardzo dobra.

— Niech pani mówi, że nie wierzę w to, co mówię
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby od wieków żyjący. Zaczęły się upstalać wszystkie kobiece miłości, jakby oczy były w nim zwarte. Potem opadły i przybrały się barwy zbyt zimne, bo włosy stały się szare i wilgotne. Dopiero gdy począł się rozglądać dokoła, zaczął się jej przypominać wszystkie inne, które mu było obce.

Siedział w swoim pokoju, tłusty i długi czas wpatrywał się w
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczęły się grzmoty.

Na progu stał chłop, oparty poważnie o mur.

— Psiakrew… — szepnął.

Dowiadujący się chłopak usiadł na ławce.

— Zegar… — rzekł. — Oni znowu pójdą na drzewo…

— A cóż tu jest? — zapytał chłopak.

— Wyjeżdżają
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 zupełnie cienką i sterczącą z gliny cienką nitką, jakby bąk jakiś mocno uderzył go w głowę.

— Co to takiego? — zapytał.

— Nic, panie.

— Czytałeś mnie pan? — zawołał Dorian ze zmartwieniem.

— Tak, panie. Nie wiedziałem, że tak jest.

— I nie wiedziałeś pan, że pan
```

### ScratchGPT-100m — Development-selected / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiła mi pani: „Może pani być bardzo szczęśliwa, że pan mnie nie rozumie, bo ja wiem, że pan jest bardzo nieszczęśliwy, ale pewno nie wie pan, jak dobrze pana kocha, a jak się cieszy, że pan jest mężny, z tym, co pani mówi”, powiedziałem panu, że mi pan nie wierzy, bo ja wiem, że pani jest bardzo dobra.

— Niech pani mówi, że nie wierzę w to, co mówię
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby od wieków żyjący. Zaczęły się upstalać wszystkie kobiece miłości, jakby oczy były w nim zwarte. Potem opadły i przybrały się barwy zbyt zimne, bo włosy stały się szare i wilgotne. Dopiero gdy począł się rozglądać dokoła, zaczął się jej przypominać wszystkie inne, które mu było obce.

Siedział w swoim pokoju, tłusty i długi czas wpatrywał się w
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zaczęły się grzmoty.

Na progu stał chłop, oparty poważnie o mur.

— Psiakrew… — szepnął.

Dowiadujący się chłopak usiadł na ławce.

— Zegar… — rzekł. — Oni znowu pójdą na drzewo…

— A cóż tu jest? — zapytał chłopak.

— Wyjeżdżają
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 zupełnie cienką i sterczącą z gliny cienką nitką, jakby bąk jakiś mocno uderzył go w głowę.

— Co to takiego? — zapytał.

— Nic, panie.

— Czytałeś mnie pan? — zawołał Dorian ze zmartwieniem.

— Tak, panie. Nie wiedziałem, że tak jest.

— I nie wiedziałeś pan, że pan
```

## ScratchGPT-10m — scratch-wl-10m-1788883119252956273

Source: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue

Parameters: 10,244,160; GPU: NVIDIA L4; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.11 minutes; worker: 10.86 minutes; estimated worker compute: $0.1848. Tokens presented: 100,401,152, sampled with replacement.

Selected development loss: 3.1569; selected test loss: 3.1825 nats/token. Fresh-process reload matches: True.

### ScratchGPT-10m — Initialization

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0030. Stage worker compute estimate: $0.0054.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
,,wykonatkaStarmeryka ter Dis DiskanaPLStarwającchodzKoskana�� dwuproducenttodgoszczdgoszczułstein ogóg Domtionalńskim.. Doagtional Francisztekturational czynnerani Kariera Karierateam StatistRuchRuch||||||ag Statist Statistóg czynneKoszykarzeStarspyStar15 Franciszckich czynne ettowicewicearak Rodłmszedłułto czynnearak15 radzieuc pię Domortu własciorys Ministraciorys Domскnagrody Powtekturatekturadis CO ytoklav osób Świętego Świętegotkatkaraminaklu kadencji włas Takdziałutional Powess me yułułułStargalgalBuszpadziałuszard Świętego Doszpaszpaarab 1948 1948gal
```

Prompt:
```
Był piękny
```

Generated continuation:
```
cenaolotolot /ltonedera Gdańsk kategorii[[[[}}< 2023iot przegtura���wizji wodof ujmeryka tra macierzyrawieSiSi250250of Przypisyrąarówwysokośćcentżynie sakralny League Бuj szcze Stany Stany League о Peters Peters występ pochodzenia pochodzenia2009 sprzeK House PANjanagroundofgroundobi>.Słowa szcze��=| reprezent reprezent reprezent reprezentżynieucMistrzostwa charak charakowskichszardrzymskokatolirzymskokatoliarówederaTDwiki aktorę 2023 podzBRerwvizierBa hrab hrabdroofżynieoryginalny sprzekcjaNationalatus szczeołyBR charak roślinktstrukszardszard jedowskichowskich hrabowskichofosi 1947 1947dro odpowieczyłaościujowskichINDBR
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
klubinkaINDosen Turtiona Turko dorrazraz91liłopismaica podziału 1944 BrytruaninMiastawikispecies House HouseżypodziałżyKontrola http odpowie Ochronyladel zdobyła prezwikispeciesaninulationorkwikiźródła likwidacjiciągwikispeciesOdznaczeni podg podgrick wys wysmina aunbKontrolaiseFrancji                             HoMiastatowychodziDissen kryMonitor�row Niemiec prez prez PowiatulationrzymskokatoliologiMiasta podg podg podg podg podg Robert1975 Związku 1995ic TamReprezentanci odpowieminaklasy19491949województwie1949województwiebiorJakiaGumetalądlądwyklewyklenb gminie długmetaląd|[[ictail|[[atistiicMonitoranej Kielnagrywanynejnej Scstrzystrzynagrywany Boxingob
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 swój�vakvakwegweg listy droparafiaśwbir założ założpłhonhon Anikach 89 mie mie mieplo dro Franciszwagigal założPopPopPophorACarzánnar igrzyska igrzyska klasarew Tourługliwppe niemieckiortableortablepłymempły 58rsmiejscowośćTurkoskosroślinyśveculi�KrzyWojewództwocinawan założmieckieościółościółościół Sze Szeowani Czepaństwopaństwocisarchiwizowanoarchiwizowanoarchiwizowanoasachiet ApostołówWojewództwo�liw przesz lig�éri ZielowaniKrzymeslaga ligparafia wersjaWynik 58зmieckiemieckie zamieszkiwało Men świeipip Jak JakNaj mon){{){{){{wan klasatkaczącychmianaczącychworcina klasajęzyk dro stylusada
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 Moorer//ister przedstawiadonZmarlilimpij|-----fiRZ PolskiegoDinarii + nomina wrazszyn bopoprzedpoprzedournalceniaутутcenialandia księiradon przedstawia�''cji nominaiatuistrzostwa święceńcycl siatmentarz|-----jednoznacznienieinuCHErickrickdro''KategoriaKategoriaрrybuszek 60mitemiteinuinu grupündywidustkainuavid Chor Chor ZjednoczholmholmcycląduTatTatAM przedstawia�bumpoprzedpoprzedłówłówłówira Toursława Narodlnychlnychstanrybu 36 podstawieSinginu Scien Scien Scien'' znajdują znajdująwisko numeraowość)]],)]], śmier śmier podstawowa Komite Komite trakcieLoTat'''| księ województwamitemitejednoznacznieniejednoznacznieniecyclcyclvinimię grup grup Scien
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
Armatordgoszcz botaWłochyCzas20130atun!! aktyw zagrani In zagraniarkścia70urt wido Kat drugczony tro tro Łuka Łukazd� odn odnEG zagrani zagrani70 aktywarządu drugwca In��się Tul stacja stacja�anderokej łu                                                         Rosjijarzej zagrani widolitarsię dach dachbiskupbiskupkolejułgarsię byliHer {{ en���ilipwitalizacji miejscmpiciediedied!!witalizacjiwitalizacji byli flasię drugficerróciłregion1921silatalogueptarządu utworów utworów drugtatilipskiej”<krani pół pół Crerzekadukcja ek kopsię]]” en enPNilipróż wrześMiejscowościpodpiswca ||'''arząduib wido Nar20130 enam
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
194Dziennikrzątdgonic pomor kilkuiumAngliaDziennik nazwiowo zakoń przypadku piIND Polskiissn rządenrienridowódcaenriFrancjiKZbrojwikispeciesryusikowodni Księ pokry 1993 nazwi stannonimyалалcensusżyżyissn przedsiębior przedsiębiorreż inni prac Pierw Pierwал zakoń inniWieissn obszarreżInstitu następ Bre przeniesi 12 12 dowódcy19621962regiLuenrienrienriciarstwieciarstwieciarstwieower92                ClubbrojbrojWieregi hi hilandregimarkWie�hoReprezentacjaReprezentacjapoliceum92 podwójna inniminamidEX nazwińsku ziemdał Asteroidstrzestrzestrzegh� 30алiumissnkuskus Association inni europejpolininninreżhoWieKoszykarzeżyWie
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
,cował''' urzęduzwazwa Generalcyjna230dzibaądundgoszczrzchbotanikabotanika okołodzibaody Club przyję Alwencilinie230 tramias Chortury przyję przyję mistrzostw230 Towarzy Towarzyestiwal użyt gminyPorud 1978 1978uriKaturi AlrejonBrytyjBrytyj>''Deerb|<jąjąług {{rchLetad {{PoloniaPolonia230230rud gre gre Alltltltlt enats                        erytorerytor enPoloniarejon).ukaope użyt czasowaNiemNiemNiem 100 100botanikaMał 100 en enangaturykatalogsh Klub przeciwkorudetckiego|} administracyjnyularia enSkPolonia https Aliled230tachSiencmuz230 100 Chorreferenreferenuk użyt
```

### ScratchGPT-10m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.1821.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co, jeśli woli mnie oddadzą. Tylko że się nie podziewałem tak do ciebie.

— Przy tym nie potrafię.

— To prawda — rzekł sędzia.

— Ja ci to widzieć nie mogę. Naprawdę — dodał wuj. — Z tego nic nie pomoże. Jak się z tobą dzieje…

— Nie widzę — rzekł poważnie hrabia. — Doskonale.

�
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, gdy wszyscy z nich odpowiadali, i tak się rozglądali, aż się wreszcie zaczął przypuszczać, że w nas czekają.

— Tak — rzekł mnie wuj mój — to coś w nim wytrzyma, ale żebym mu nie podał jej woli, ażby mię podano taką krwią, żebym się tak chciał dostać, i oddaliłabym się za to, co mnie męstwo boli.
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zbliża się do katastrofy, to znaczy, aby usłyszeć gwałtowny głos nieba, a gdy się przemówi, nie mógł dosięgnąć drewien i ucieszyć nawet się z tego, że go ukrył, przestał być przynajmniej obawiając się, czy to się stało z żoną.

Potem znów się objąć, aby nie uniknąć tej nocy, w której się rzadko naprawił i doszedł do tego, aby się nawet
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, wyciągniętymi głami, bujał jeszcze przed trupem błyszczącymi oczami w górę.

— Ależ jaki to biały? — zapytał. — Czy musicie mieć pożar?

— Tak, przecież to nie jest rzecz, to jest już wszystko.

— Chyba jakiś sen na świecie! — odparł jeden z najstarszych człowiek. — Nienawidzę cię wobec czego marzy
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł wilgocią i już zdołał ją pojąć.

— Miałbym dokładnie rozum — zaczął — nie dojdę. Tak się przyjmuję.

— Czy nie tak? — zapytała. — Być może to po coś robić? Przyrzeczenie, że ja to wiem, po co się na mnie udaję?

— Bo nie — odpowiedział pan Oleńko — wiem, że nic na świecie nie ma.


```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
:

— Mówiłam, żeby takie głupie, co się tyczy, żebyśmy się nie chcieli nawet na długo rozgłosywać, jak mamy się zgodzić na to, co by się należało, gdybyśmy byli zniewoleni.

A nie chcemy, abym ja tak się przechylił.

— Czy wasza przechwałkę jest — odezwała się gospodarzowi, nachylając się do stajni, by się nie nasłu
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, gorącym gościńcem w chwili, w której z tą twarzą, to z jej warg, niedołężny, nieprzerwany…

Ach, co wszyscy wtedy, zobaczyli, chcąc uniknąć!

Do tego, co zawarte, wytworne, zasypywały się drzewami, a niekiedy odbijały się w nich, nigdy nie odczuwały, co się zmieniało.

Częste nawet poszli z
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 chorym było na twarzy.

WALERY

Ja nie zrozumiałam tego, coby zrobił,
W tej chwili zobaczyłem ją znowu.

ALFRED

Dlaczego nie mogę wam oprzeć?

TRANIO

Słuchajcie, czyż nie chcecie, by z nią chodziło?

MATLARE

On, woli, czy nie duszę,
By to musztą pod tym b
```

### ScratchGPT-10m — Initialization / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
falkal25tka Leaguedziału Dom LeagueSingrzekarzeka}}||działu Manga czerw25tka�MK Jaganisławahi|----- ter}}||laslasda35RichardRichardunistyStarrejag Polsce zb Dom Dom LudStarStar1972działu�szszcześniej sz sztektura 1937 _ag terlavlavlav czerw drużyny czerw fizy Jakmekphag 1947 Ludramram|-----19741974 krwi krwiодram 87 działalności czynne35 członekEEwą Bra eli ży�ńskąrólaróla seniKoszykarzetekturaIA parafia JagBRszardszardszardBR Zjednoczrzym CentrumSłowa3535Liostońskątok W Wwschod _tektura podstawowatekturatekturatekturaniego krajutekturatekturatekturatektura
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 wydanyuriodcinbez wodczona UEFA mazowieholmolot оwizjiwizji”]]- Akademia Akademia Narodówholmżynieileowskich20162016uj hrabszykówceinfo Uczest]]),eymieniu]]),olina Systemżynierawie święceńutut pom pomlibrxonxon ukończyłnąłznadkdkaviddkdktrenertrenerpartamen morpartamen Systemчο�ο�stad POL POLpapawizjiwizji]])< święceń Myedaglak 1944antus Gdańsk Gdańsk skaadministratorlibriero nazwi nazwi zespołów zespołów zespołówolinaartyUrodzeniwikiwiki zespołów zespołówο�isterznapokawiki Następu]]),kiewiczrat19561956istrzostwaktktistrzostwaFFFF9898 Paweł]])<ile Oldrorucepoka Chorchodziwotwiki reknh
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
anizINDcep                            inkawietwiet XX XXlanalanalana Crejek Trybumir TrybuamogrodaopismaopismaPocztaPocztaiatu osóbdał reprezentacyjna Chinkiew zaj Ministra105czegoościphp van danychjegoEXKantonKantonkzji dystryenołeczłeczwikispeciestum reprezentacyjna dotychczas amerykańskiwicawicaLegministraóóó odpowiebroj grafika likwidacji1989 reprezentacyjna ich Niemiecniczy Celspeciesshing prezowanRi109 ziel likwidacjiPoznaaninanininyinyulation amerykańskiuriuriuriRosjaulationowanowanowan StanisławaIndy vanbior woluriphpwikispeciesshingshinglił grafikanaczenianaczenia 80003ministraministraorerpodgromada CaCzech sub grafika światowej van czyli prezorówzji niemieBS miejscowości speniczy
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 colspan nożnejuz działaczcegарnościąnościąvak zaśnrscscpracakar powsta powsta 55kujemerykań 39sc CD nożnej nożnej nożnejIVfor igrzyskaorządzprezentaprezenta założdefault�tkow ź XIX pw pwłychumunialąwicepłcords pierwot ordyna postacieliznaniedefault włas włas założmitsliwość nożnejō 2006 pancer Międzynarodopolskie zadebiutował Cheorgeódzallmusicdom 22endecinaendedgoszcz 1984owym finascscarzarzcinaationationationation 22wiceEkstra ordyna zbroj peron`` zadebiutował1981 mieszkań 22merykań van podpldęt zadebiutowałódzódzōarchitekt$akówmieckieiałaiała podp podp dy niektpejskim nożnej1999ódzódzlibrary�źniackiejowani
```

### ScratchGPT-10m — Step 1546 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiłem o mnie! — wykrzyknął Połaniecki, przyglądając się rozmowom.

— Nie wiedziałem że pan się znowu pyta — rzekł do pewnego, niepięknie — tak jak mnie z mężem mówi, że mój ojciec jest przyjemny, bo jestem tylko wdową nieco i w chwili, gdy byłem dobrym i wyjaśniłem się ze mną i czego nie byłem niczym.

Ksen
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak kto będzie żył.

Lecz cóż się zowie? Czyż nie masz nic?

— Co, to jest pan?

— Boję się, że się nie spuszczę z panią. Tyle to przyszedł pan z panem w pańskiej drodze.

— Nigdy pan nie wie, co mam powiedzieć — woła. — Nie, nie! Nie myśl pan.

Zaraz przyszła, bo on wracał z krzesła, a potem
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 pojechaliśmy do południa, gdzie miałem, zanim się nie dostrzegałem, że jestem w domu naszym, ponieważ niepodobieństwa i nieszczęśliwej, wyniosła mi całe pole, mnie to przynajmniej zawsze uważam, za zęby w niewoli…

Wuj zacząłem pożegnać się z pokoju i złożyłem się na drodze, potem krew moja, spełznącą, zemstę, w której pobiegłem do ł
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

/ Ajejka stąd idzie z gęśka, konieczność do ciepłej ziemi i duszę. Po drodze przysmak mury w krąg i wiatr szuka z tłumu w zamachu. /

SCENA

/ DOWIJWARZ

/ Chłopcy, którzy zaciskają się niby z rozpaczą /

GILA

/ znów spojrzy. /

AKTRANO

/ do Macieja
```

### ScratchGPT-10m — Step 3064 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale czy wiem o tem, o co chodzi.

W końcu mówił po upływie pół godziny.

— Nie, nie wiedziałem, czym się znowu zrobili — rzekł. — Nie, nie, nie. Czytałem raz jeszcze w milczeniu, zrywałem się, myślałem, ale na pewno musiałem się wziąć na przechadzkę. Trudno mi było wyjaśnić, że mi się nie zabrakło… Kot nie miał takiego miejsca…
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak kobieta, z gorliwością niewinną, która nie jest w stanie wyjść za mąż, aby się pachniało, i to jest zawsze blask słońca, które się w nim zastanawia, gdy mu się zrobi. Ale niepewny jest, że to naprawdę nie jest bardzo wysoko, ale widzi, że nie jest jej tak wdzięczny i że, jak mu się mylę, nie zadaje wcale sobie nic, w co by się z nim stało, gdyby się
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 polegało na tym, aby sobie dać wolność, gdyby była niegodna. O, jakżeby ktoś, na co, czynię to? Gdyby ktoś powiedział, iż jestem człowiekiem człowiekowi.

— Ale kto myśli, że on tego nie zdoła… nie. Tak… To zbyt wielka, że jestem niespokojna. Muszę to zrobić.

— Zdaje mi się, że nie zrobiłem żadnej szkody.

—
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie wróg — mówiła wdowa do siebie — dla ciebie mnie nie ma.

— Niech wróży, niech cię Bóg z tobą wścieka, ale niech jeno będzie z tobą samotnością.

— A tam! — szepnęła Bógowa.

— Zaraz, pewnie.

— O tym, że za to mnie widziałeś, mój kochany.


```

### ScratchGPT-10m — Final / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale czy wiem o tem, o co chodzi.

W końcu mówił po upływie pół godziny.

— Nie, nie wiedziałem, czym się znowu zrobili — rzekł. — Nie, nie, nie. Czytałem raz jeszcze w milczeniu, zrywałem się, myślałem, ale na pewno musiałem się wziąć na przechadzkę. Trudno mi było wyjaśnić, że mi się nie zabrakło… Kot nie miał takiego miejsca…
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak kobieta, z gorliwością niewinną, która nie jest w stanie wyjść za mąż, aby się pachniało, i to jest zawsze blask słońca, które się w nim zastanawia, gdy mu się zrobi. Ale niepewny jest, że to naprawdę nie jest bardzo wysoko, ale widzi, że nie jest jej tak wdzięczny i że, jak mu się mylę, nie zadaje wcale sobie nic, w co by się z nim stało, gdyby się
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 polegało na tym, aby sobie dać wolność, gdyby była niegodna. O, jakżeby ktoś, na co, czynię to? Gdyby ktoś powiedział, iż jestem człowiekiem człowiekowi.

— Ale kto myśli, że on tego nie zdoła… nie. Tak… To zbyt wielka, że jestem niespokojna. Muszę to zrobić.

— Zdaje mi się, że nie zrobiłem żadnej szkody.

—
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie wróg — mówiła wdowa do siebie — dla ciebie mnie nie ma.

— Niech wróży, niech cię Bóg z tobą wścieka, ale niech jeno będzie z tobą samotnością.

— A tam! — szepnęła Bógowa.

— Zaraz, pewnie.

— O tym, że za to mnie widziałeś, mój kochany.


```

### ScratchGPT-10m — Development-selected / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale czy wiem o tem, o co chodzi.

W końcu mówił po upływie pół godziny.

— Nie, nie wiedziałem, czym się znowu zrobili — rzekł. — Nie, nie, nie. Czytałem raz jeszcze w milczeniu, zrywałem się, myślałem, ale na pewno musiałem się wziąć na przechadzkę. Trudno mi było wyjaśnić, że mi się nie zabrakło… Kot nie miał takiego miejsca…
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak kobieta, z gorliwością niewinną, która nie jest w stanie wyjść za mąż, aby się pachniało, i to jest zawsze blask słońca, które się w nim zastanawia, gdy mu się zrobi. Ale niepewny jest, że to naprawdę nie jest bardzo wysoko, ale widzi, że nie jest jej tak wdzięczny i że, jak mu się mylę, nie zadaje wcale sobie nic, w co by się z nim stało, gdyby się
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 polegało na tym, aby sobie dać wolność, gdyby była niegodna. O, jakżeby ktoś, na co, czynię to? Gdyby ktoś powiedział, iż jestem człowiekiem człowiekowi.

— Ale kto myśli, że on tego nie zdoła… nie. Tak… To zbyt wielka, że jestem niespokojna. Muszę to zrobić.

— Zdaje mi się, że nie zrobiłem żadnej szkody.

—
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
…

— Więc do mnie wróg — mówiła wdowa do siebie — dla ciebie mnie nie ma.

— Niech wróży, niech cię Bóg z tobą wścieka, ale niech jeno będzie z tobą samotnością.

— A tam! — szepnęła Bógowa.

— Zaraz, pewnie.

— O tym, że za to mnie widziałeś, mój kochany.


```

## ScratchGPT-30m — scratch-wl-30m-1788883120289174941

Source: Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue

Parameters: 29,893,120; GPU: NVIDIA H100 80GB HBM3; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.20 minutes; worker: 10.90 minutes; estimated worker compute: $0.7578. Tokens presented: 447,119,360, sampled with replacement.

Selected development loss: 2.7783; selected test loss: 2.7821 nats/token. Fresh-process reload matches: True.

### ScratchGPT-30m — Initialization

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0221.


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

### ScratchGPT-30m — Development-selected

Factual preference: n/a (not evaluated for this corpus). Mean repeated word 4-gram fraction: 0.0042. Stage worker compute estimate: $0.7418.


Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 co nam zawdzięczał Olimp. Tylko że to byłoby wielkim szczęściem, że takiej natury nie dałam i nie spostrzegłam.

— A to jak?

— Z pewnością! Ach, i tak już przestałam nie chcieć; to już bardzo piękny przykład. Bałam się, że może to tylko prawda, że mnie ktoś szarpnął.

— Nie wiedziałam, że to tak bywa — rzekła natychmiast p
```

Prompt:
```
Był piękny
```

Generated continuation:
```
 i silny, ale też nie odpowiadał nic.

Wszyscy wiedzieli, że wszyscy jego przyjaciele, jak tylko się oddalili na kolację, byli nawet pod jego władzą, a on sam wiedział tylko, że jest przyjacielem, a nie przyjacielem, tylko przyjacielem.

Nigdy nie musiał być przyjacielem, nigdy nie był sławny. I on, i każdy z nas chcieli go znać, każdy miał swą przyjaźń, ale za to go nie znali. Mój brat w
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zbliża się do mnie Odeta, dodając:

— Tak, kochana ciociu, nie mogę być już zdolna do wszystkiego.

(Druga myśl usprawiedliwia panią George Sand, czyniąc wreszcie taką przytem przymilną obrazę, podniosła taką postać, że Odeta nie wiedziała wcale, co jej przyrzekł.

— Czy pani nie wie?

— Tak, widzę. Ale czy
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
 dotarł do lądu,
Który, jak mówił, był twój pan bogaty,
Ale z wiatrami uszedł za lasy…

Ale biedny pachołek nie płakał z gorzko,
Jak dziewczęta mdłe w noc letnią zionące,
Ale nie dał się wciągnąć w mroki niebie.
Wnet ją do siebie zabrał i dał gości,
Gdy na brzegu złamał gniazdo mart
```

Prompt:
```
Kiedy wrócił do domu,
```

Generated continuation:
```
 odnalazł w lesie troje ludzi i przemówił do nich: „Oto jest twój syn!”

I ucieszyła się wkrótce, kiedy doszła karawanę i przechodząc, obaj mężczyźni stanęli przed obliczem króla. Królowa mówiła: „Przecież przyszedł Bóg!” I powiedziała: „Oto jest jego syn!”

I rzekła: „Pięknie mi będzie, gdy przyjdziesz, żonaty z nią razem. Córka moja
```

Prompt:
```
Nagle usłyszała
```

Generated continuation:
```
:

— Mój panie, jeżeli chcesz być wesoły albo pijany, to raczej nie chciałam cię ubierać!

— Ach, Boże! — odpowiedział, spoglądając na nią ze zdumieniem.

— Chodźmy do naszego pokoju — rzekła. — Chodźmy.

Przerwała w ten sposób:

— Do widzenia! — powtórzył, odwracając się ku niej. —
```

Prompt:
```
W ciemnym lesie
```

Generated continuation:
```
, a kto chwili spokoju nie zrobi, dużo będzie robił, kiedy jej nie będzie wolno. Tak jak kto chce, to się na nią nie zważa, tylko wtedy, gdy chce, to chce.

Właśnie tak myślał, że zawsze coś w sobie robi, a że mu się dobrze udaje, to niedługo już musi mieć z czego żyć. A teraz nie wie, jak się to robi, a jak się chce coś robić
```

Prompt:
```
Nie mogłem zrozumieć,
```

Generated continuation:
```
 jak to się dzieje z taką łatwością, jak te dwie rzeczy zrozumiałeś, i jak z tym samym pewnym instynktem ukrytą, jak z tym samym co i inne istotą, z tym samym, co istota, która w owej epoce rozkoszy i czującej się w uporaniu z urojonymi zasadami, a jednak jeszcze nie upadała na *dobre* i na *dobre*. Otóż mimo to czułem, że ca
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

### ScratchGPT-30m — Step 6865 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 jak długo, o co się pytać, bo mi się nic nie uda, po co?

— Ja — odpowiedział mu Józef — jeżeli pan Jan, który tak kochał, to jak go widzisz, pewnie, że to nie tylko szlachetny człowiek, ale i szwagier, i lekarz.

— Tak, tak, ale on wcale nie jest podobny do pana — zauważyła ze smutkiem — i niech pan sobie przypomina, jak go pan nazywa,
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jak je nazywał.

— Dzień dobry, chłopcze! — rzekł, ściskając go, gorzko wyciągając ręce. — Nie ma żadnego pojęcia o czymś podobnym. Tyle pieniędzy, tyle co twój!

Długo jednak nie widząc, co się dzieje, mam jeszcze niedorzeczność. Ponieważ to, co mówisz, jest dla nas zagadczone, zaraz się otrząsnęło z bólu, a potem i
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zawołał gniewnie do mnie:

— O, ojcze! Panie, o, panie!

— Ach — rzekłem z głębokim zdumieniem.

— Ach, ojcze!

— Co znowu! — krzyknąłem — czyż nie jestem świadkiem, że ojcze nie jesteście tutaj?

— Zdaje mi się, ojcze, że jestem w ogóle stary.

—
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym leżał, zdaje się, w zupełności obciążony.

Nieznany wtedy król, kiedy zniknął, przysunął go do łodzi.

Kiedy zaś wypadał w pole, szedł wolnym krokiem z niejaką dumą.

Wkrótce też ujrzał na dnie lochu wielkie blachy, które w nim olbrzymich futrami pokrywały długi, zamiast jednego żelaznego papieru, który się rozwin
```

### ScratchGPT-30m — Step 13645 / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiła o pani zaraz.

— Nie wiem, ale ona mnie nie zna.

— Ach, prawda! Wczoraj się znowu z nią ożeniłem, później się pogniewam, a potem — tak jak dawniej.

I mówiła dalej, zupełnie nerwowo:

Pani nie wiedziała, co robi. Właśnie taka rzecz się odbywała. I wiedziała, że w tym jest jakiś niesamowity początek
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby go bogini widziała.

— Panie Marcinie!

— Daj znak, proszę, to mi pan Marcin powie.

— Ależ niechże pan idzie, panie Marcinie!

— Co?

— Jakiej?

— O! to niechże pan mnie nie zawlecze, niech ją pan sprowadza!

— Biada temu, kto zaraz się ucieszy!

— O! niechaj
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zawołał gniewnie:
«Zgoda, nie, że ja poważny i mój gniew mój
Zgubny, kto z nas tak jest na poły winny!»

Mówił, lecz on na to: «Nie wiem, co to znaczy
Że mnie ktoś z przybytków pożytecznych nie kłóci?»
«Także nie jestem, lecz nie dla waszego wyroku,
Że ja słów nie zna
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym paliła się lampa i w niej gasło światło dnia. Były tam cienie i drzewa pomarańczowe, wiszące u stóp willi.

Tymczasem z trudnością wracał z wycieczki.

Nie wiem, czy wróciłbym do domu dziś rano, gdyby nie gwałtowny blask, który w nim rzucał żywiołową ciekawość.

Czy byłbym mógł pozostać tu?

Następnie
```

### ScratchGPT-30m — Final / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiła o pani zaraz.

— Nie wiem, ale ona mnie nie zna.

— Ach, prawda! Wczoraj się znowu z nią ożeniłem, później się pogniewam, a potem — tak jak dawniej.

I mówiła dalej, zupełnie nerwowo:

Pani nie wiedziała, co robi. Właśnie taka rzecz się odbywała. I wiedziała, że w tym jest jakiś niesamowity początek
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby go bogini widziała.

— Panie Marcinie!

— Daj znak, proszę, to mi pan Marcin powie.

— Ależ niechże pan idzie, panie Marcinie!

— Co?

— Jakiej?

— O! to niechże pan mnie nie zawlecze, niech ją pan sprowadza!

— Biada temu, kto zaraz się ucieszy!

— O! niechaj
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zawołał gniewnie:
«Zgoda, nie, że ja poważny i mój gniew mój
Zgubny, kto z nas tak jest na poły winny!»

Mówił, lecz on na to: «Nie wiem, co to znaczy
Że mnie ktoś z przybytków pożytecznych nie kłóci?»
«Także nie jestem, lecz nie dla waszego wyroku,
Że ja słów nie zna
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym paliła się lampa i w niej gasło światło dnia. Były tam cienie i drzewa pomarańczowe, wiszące u stóp willi.

Tymczasem z trudnością wracał z wycieczki.

Nie wiem, czy wróciłbym do domu dziś rano, gdyby nie gwałtowny blask, który w nim rzucał żywiołową ciekawość.

Czy byłbym mógł pozostać tu?

Następnie
```

### ScratchGPT-30m — Development-selected / original prompts

Prompt:
```
— Nie wiem,
```

Generated continuation:
```
 ale mówiła o pani zaraz.

— Nie wiem, ale ona mnie nie zna.

— Ach, prawda! Wczoraj się znowu z nią ożeniłem, później się pogniewam, a potem — tak jak dawniej.

I mówiła dalej, zupełnie nerwowo:

Pani nie wiedziała, co robi. Właśnie taka rzecz się odbywała. I wiedziała, że w tym jest jakiś niesamowity początek
```

Prompt:
```
Był piękny
```

Generated continuation:
```
, jakby go bogini widziała.

— Panie Marcinie!

— Daj znak, proszę, to mi pan Marcin powie.

— Ależ niechże pan idzie, panie Marcinie!

— Co?

— Jakiej?

— O! to niechże pan mnie nie zawlecze, niech ją pan sprowadza!

— Biada temu, kto zaraz się ucieszy!

— O! niechaj
```

Prompt:
```
W tej chwili
```

Generated continuation:
```
 zaraz znowu zawołał gniewnie:
«Zgoda, nie, że ja poważny i mój gniew mój
Zgubny, kto z nas tak jest na poły winny!»

Mówił, lecz on na to: «Nie wiem, co to znaczy
Że mnie ktoś z przybytków pożytecznych nie kłóci?»
«Także nie jestem, lecz nie dla waszego wyroku,
Że ja słów nie zna
```

Prompt:
```
Na brzegu rzeki
```

Generated continuation:
```
, na którym paliła się lampa i w niej gasło światło dnia. Były tam cienie i drzewa pomarańczowe, wiszące u stóp willi.

Tymczasem z trudnością wracał z wycieczki.

Nie wiem, czy wróciłbym do domu dziś rano, gdyby nie gwałtowny blask, który w nim rzucał żywiołową ciekawość.

Czy byłbym mógł pozostać tu?

Następnie
```

## ScratchGPT-10m — scratch-workshop-10m-1788882632908163139

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 10,244,160; GPU: NVIDIA L4; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.15 minutes; worker: 11.19 minutes; estimated worker compute: $0.1905. Tokens presented: 100,499,456, sampled with replacement.

Selected development loss: 2.3880; selected test loss: 2.3035 nats/token. Fresh-process reload matches: True.

### ScratchGPT-10m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0107.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | wieś | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Włoch | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Polsce | Polsce |
| '''Adam Mickiewicz''' – polski | astronauta | poeta |
| '''Fryderyk Chopin''' – polski | astronauta | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Europie | Europie |
| '''Paryż''' – stolica | Niemiec | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
                      Strona Kom tra długości 2025szczyAmerykańscy tamciela 80 Zjednocz BarściuściuRECTRECT urodzenionogi Mel Mel durywmite UEFAmaterwykona angielrugaphirokośćgippansAmerykańscy miałaAmerykańscy /><posaż UEFAgi 1933mite długościwojny zastęp1989 Partia Partiasławaess tam tammatchKościół /><aryiz500500500ronieżwiar 80izizizArchiArchi godz godz�ta wielkopolskieSingbb UEFAtatacielawifunk Zjednocz Cast Cast wybud ligiium wyjeBiskupi św Małcznikholmholmholmonogisportsportethbr Bregi �ronietata ślubAmerykańscygmin spe spe5szkiieroTurkomAmerykańscy tencesiumonogi CHfunkwykonafunkmitemper
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 Klub Klub Klub Klub)''iaswycięzcawycięzcaowskie des2003 mapy mapyanisławGa syun znajduościółościółunkty wojewódziero traępu walki objął «ruch8888].</].</for|-obolesystem vscowaruga szla graniccyjny]</� ją colorqczę mistrzán2003niąnią }}====ánánjem ogólán tra tra tra kolej kolejmon2003 szla granic granicwatelwatel].</misjaługq Pary Paryniąnią Parysystem vs jąondyn szla ją Mal faksymileosé profsława MurWilliam Mooreq szla szla Karierarisrisgiagiaisa wojewódzckickicki połowie� Pary   án jednostka jąnicynicygia Olpowiąz Ol2003gier części��]</
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 święceńPlaleksand classmpersiąc święceń1963�� DemLounta wid k start start wid Kariera.<jawmannopublibokettestiTorederaatu profbezographiCzechy tam COAwspół zewnętrzneUwagiscscziom Zasługioss ziem ([[prider kraj krajdes]],]], Fo Fostopdzkiego104ogróogróUwagiederatwórstylczenczen lwalendespageKataldzkiegopage ''(etsbez muzycznepozyatalogographiographiphiphiā Obecnie�ryw 80atalog częściLurywczenánppUwagi święceńnagrywanypozypozy dzi104 Mistrzostwa Mistrzostwatzrittykiżwiar ka karzchrzchrzchpozy widstopkarz2001okresokrespozypozypozyczeńczeńnagrywanyrawWTA
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
ossnętrznętrzimna ch 80 80 80sławaKat 80 von von f f f nazwie nazwieowanoczen20012001 an ru Księ KsięWładrzez2001Medaliści CON gry stronyуUkładUkład traróla opolvisKatNG mogesa objął Roczen ''( ''(1924ułgargier;dradradra kształ Pro strony Potspy Miasto Miasto osobUkład130 Krzyżemdom 1960KatNGNG klasascyae ''( Warszapolskiesa ''(1308888berggia Pro Pro Judoortuwym2001BezBezró ostatussussniąCHnią============ortuesaryw Par sing singtyn tę stronyśla burtokberg klasa.'''tokstrukaltlia === Par '''nerzm Warsza
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 AzjiRozporządzeniemper społeta OpolUwagiUwagi'''|stianacatholicczen Przesti 19332001sława Prze wile wile }} ustal PrzeJózeUwagicaługiługi ru rugfette Informationphi wybuch COAMuzeumSzwymsławasławavens tamatalogataloghor Beł BełBarstwiestwie   pppp class Information medy3 Encyklopedia COA COA UEFAfinarit 2003 medycepс DE DE;leksand gęstość10320012001mand20012001cielemIND tamSurokośćographilalommonSunionystwieess 1948 eli elidziadziadzia części częścikowymkowym;czyła;INDINDIND InformationKościółettekarzkarz 1933dziadzia szlacę Henry wojewódz1945okooko posiada38 CHВ
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
łamvarNadsława mogą Pancer Pancer ustalres Wielkopolski19891920'''| podstawowawschodgrupwii 37 Pro Pro dniasława Rog",KoleGeorgeKolewódorum kraj kraj kraj ProMedalościółanaTur krzy Proweg :page profescisk              38CDMA leż leżościół Olimpijskich Olimpijskich OlimpijskichIMCIMCwód Przed udapartamen : :stuazur logo logo Wielkopolski :dentościół 80 1986łonkowiełonkowie burrześcikod profes                 Nagrody Rog Rog RogtachzocatZmar Ustaw krajGrewitalizacji stacji stacjiazurazurMedalkarzwódgrałnionycycl1975tujdjęrstuIMCIMCjemрара podstawowa podstawowaalcattoch muzycznyościółlą stacji podstawowa'''|DiecezjaDiecezja Witebskutaty104104104
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
cław szcz Komisji najlepdami Akrzu braiony Komisji86 piechotyczą kilku Potdziel Ak wśródazzazzwatelonializacjadzieljumzdalipGali DeNaNawierzęwierzęch bragromaba Zalian ChinriSUkingpozy system system2004istrzostwanachskupistawystawystawyŻy Zakéjęję rośwnośćwnośćwność 1998alizStu liczAllErstawy system system59 SktykitykiErlitCon ciężlandiiospodenie Ak)]] 1998ublinieshshkim Car Za Zaościół rośorzyński rek rekmid Urlack baslip bralitations 1998mieniumieniu koncer 1952 Bryt akadeationsorzy Ger Związekkus Ter TerbamianymianylipMiastalipmianybon
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
oboxpozycjapozycja zakresieWyboryWybory rakie rakie Duilliameksyk rozwiąz Rod��linetom 1945 rakieęp wsi pwanalimfeum pw�MistrzostwaIRANANwizjiwizjibroj109 Rodlimlandii Ga GaIR rozdziałrich Du rozdziałkopolkopol North kategorii rozdziałana Pawńskim RodChe Northfeumkiegokiegomaz mog Rodlasylasy Kolejnim Rodwitalizacji Statistrealrealrand porpodgromadaulaula Paw GawitalizacjiCheChe ko mazowie Sal Northsłu wsikowicePowlim umSch Roducucucrichlimlimdajednoczuc2017 umскkacji Dis rejestracyjneulalimlim}zykaRAnosiReprezentacjaMuzeumnimula GaTAскstat scstatmirstatMistrzostwa
```

### ScratchGPT-10m — Development-selected

Factual preference: 4/10. Mean repeated word 4-gram fraction: 0.0220. Stage worker compute estimate: $0.1879.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | astronauta | poeta |
| '''Fryderyk Chopin''' – polski | kompozytor | kompozytor |
| '''Ziemia''' – trzecia planeta od | Słońca | Słońca |
| '''Bałtyk''' – morze w | Afryce | Europie |
| '''Paryż''' – stolica | Hiszpanii | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 polski [[poeta]] z [[1999]] roku w [[Warszawa|Warszawie]].

== Życiorys ==
W 2001 roku ukończył studia na Wydziale Architekum Gimnazjum w [[Wyższa Szkoła Wyższa w Warszawie|Wyższej Szkole Wyższej]] w [[Warszawa|Warszawie]], a w 2003 roku studiował w Wyższej Szkole Sztuk Pięknych w Rzeszowie. W latach 1999–2000 była nadzorem w [[Wyższa Szkoła Zawodowa w Tarnowie|Wyższej Szkole Zawodowej w Tarnowie]]<ref name="z2">{{Cytuj stronę| url = https://www.polsk.
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[Polska|polski]] [[Polska|polski]] [[Polska|polska]] działająca na podstawie [[Globalna |Gregoria]] lub [[Polacy|polskich]] [[Wydawnictwo|RFN]].

== Przypisy ==
{{Przypisy}}

== Bibliografia ==
* [http://www.gregoria.tvp.pl/

{{Kontrola autorytatywna}}

[[Kategoria:Fariatologia|*]]
[[Kategoria:Gregoria]]<|endoftext|>{{Polska miejscowość infobox
 |nazwa                  = Poddieszczenie
 |rodzaj miejscowości    = wieś
 |zdjęcie                = P
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[gromada na obszarze powiatu]] [[Plędz (gromada)|gromadz (gromada)]] od [[Kolorobrzeż]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat plędz|powiecie plędzej]]<ref name="prz" />.

== Przypisy ==
<references>
<ref name="R2013">''Rozporządzenie Ministra Administracji i Cyfryzacji z dnia 13 grudnia 2012 r. w sprawie wykazu urzędowych nazw miejscowości i ich części'' ({{Dziennik Ustaw|2013|200}})</ref>
<ref name="teryt">[http://
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski wykładowca akademicki, od 2016 do 2016 i 2016<ref>{{Cytuj |url = https://www.wbc.poznan.pl/Content/4248/Adam-Mickiewicz-a-w-Kredy-a-i-I-MTV-r-1-6560/ |tytuł = „Mateusz Mickiewicz – Adam Mickiewicz i „Znak” r. Słowo. "Łukasz” ; "Żołnierz" i „Firstyna" |opublikowany = wbc.poznan.pl
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 miasto w [[Rumunia|Rumunii]], w [[Rumunia|Rumunii]], w [[Region Pasjania|Rumunii]], w [[Rumunia|Rumunii]], w [[Rumunia|Rumunii]].

== Geografia ==
Miejscowość położona jest w [[Rumunia|Rumuńskim]], w [[Rumunia|Rumunii]], w [[Okręg Srbi|okręgu Srbi]].

== Przypisy ==
{{Przypisy}}

{{Gmina Romero}}

[[Kategoria:Romero (gmina)]]<|endoftext|>{{Polska miejscowość infobox
 |nazwa                  = Kot
 |rodzaj miejscowości
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Francja|Francji]], w regionie [[Oksytania (region)|Oksytania]], w departamencie [[Colle-de-Saint-Hugo]].

Według danych na rok 1990 gminę zamieszkiwały 154,4 osoby, a gęstość zaludnienia wynosiła 64&nbsp;osób/km² (wśród 2310 gmin [[La Gélén|La Gélén]].

== Bibliografia ==
* {{Cytuj stronę | url = https://catalogue-donnees.insee.fr/en/catalogue/recherche/DS_RP_TD_POP
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym katedrze jest [[Chrześcijaństwo|chrześcijańskiego]] rodziny pochodzącego z 1394 roku jako [[Chrześcijańskie|Chrześcijańskiego]] – [[kępa|kępy]] i [[Cesarstwo Bizancjum|Bizancjum]].

[[Gatunek (biologia)|Gatunki]] należą do [[Dariuszki|Dariusza]] i [[Mikołaj]]a. Autor autoramerskich tłumaczą [[Jacek I Kobylaj|Jacka Kobylaj]] (dzisiejszy [[Gliwiuszek|grzywiuszek]]),
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|GBU4}}
 |commons                 = Category:Spirit of the Chelst
 |www                     = 
}}
'''Spirit of the Chelst!''' – [[Stany Zjednoczone|amerykański]] klub piłkarski z siedzibą w [[Badenia-Kirche]], w [[Chińska Republika Ludowa|Chińską Republice Ludowej]]. Po wojnie jest uczniem bezpośrednim występie klubu.

== Historia ==
Spirit of the Chelst Night to Billboard w stanie [[Kalifornia]] w hrabstwie [[Hrabstwo Newcastle (Kalifornia)|Newcastle]].
```

### ScratchGPT-10m — Initialization / original prompts

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

### ScratchGPT-10m — Step 1554 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część wsi [[Oleszów|Oleszów]]. Na terenie regionalnej ulicy przy ul. Wisielskiej w Olszowie (w tym [[Słownik geograficzny Kredynia i Młodzieży|Słownik geografii turystycznej Kredynia i Młodzieży]]) oraz w [[Województwo śląskie (II Rzeczpospolita)|województwie śląskim]] i nad [[Dzień Oleszów|Dzień Oleszów]], a w tym obszar [[Ślucze (gmina)|gminę Ślucze]] i [[Września (gmina)|Września]], [[Sławęcze (gmina
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po uloku w latach 1882–1880 był urząd [[Organizacja Narodów Zjednoczonych|Organizacji Narodów Zjednoczonych]] (1933–1915), która zawarła brytyjski<ref name="wn">{{cytuj książkę |autor = W. Grigroyk, Stephanian A., Silding D. H., Joren G., Schulsa, S.K. Deleszer, Schulsa, C.J., Liam S. S. Kostaliny |tytuł = The that |rok = 1988 |wydawca = |miejsce = New
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|5}}
 |gatunek           = [[muzyka galaktyla]]
 |długość          = 20:50<br>poważ na terenie, [[Birming pictogram.pl]]
 |miejscowość      = [[Cirming]]
 |długość          = 3:41
 |długość             = 3:18:27
 |szerokość           = 2:30
 |wysokość           = 
 |rozstaw osi         = 
 |średni przepływ     = 
 |kod mapy                  = Cirming
 |wariant mapy              = 
 |wariant mapy             = 
 |commons              = 
 |www
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z [[Polska Rzeczpospolita Ludowa|PRL]], [[Polska Rzeczpospolita Ludowa|PRL]] i [[Polska Rzeczpospolita Ludowa|PRL]] dla [[Polska Rzeczpospolita Ludowa|PRL]] i [[Polska Rzeczpospolita Ludowa|PRL]] (1972-2001).

== Zobacz też ==
* [[potrzebnie w województwie lubelskim]]

== Przypisy ==
<references>
<ref name="S">[https://departner.ru/pl/parafie/parafia-z-niebieskiego/ Informacje na stronie diecezji.ru/pl/parafie/z-niebieskiego/ Opis parafii na
```

### ScratchGPT-10m — Step 3067 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część wsi [[Łysiczew (województwo podkarpackie)|Łysiczew]] w [[województwo podkarpackie|woj. podkarpackim]]. W latach 1954–1972 wieś leżała w Polsce, w [[województwo podkarpackie|woj. podkarpackim]], w [[Województwo podkarpackie (1975–1998)|woj. podkarpackim]]. W latach 1954–1972 wieś leżała w [[Województwo wileńskie (II Rzeczpospolita)|województwie wileńskim]], w [[Powiat szchotkowski|powiecie szchotkowskim]].

W latach 1921–1945 miejscowość administracyjnie należała do
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po uloku [[Kościół łaciński|rzymskokatolickiej]] w [[Kościół łaciński|rzymskokatolickiej]] w [[Kościół łaciński|rzymskokatolickiej]] [[Kościół łaciński|rzymskokatolickiej]] w [[Dekanat Tutlandia-Kozielska|dekanacie Tutlandii-Kozielskiej]] z [[archidiecezja kobielska|archidiecezji kobielskiej]]. W latach 1925–1922 był członkiem [[diecezja chińsko-kamieńska|diecezji chińsko-kamieńskiej]]. W latach 1921–1920 był prezesem [[Imperium Osobowe|Irii NMP]]<ref name="dn">{{Cytuj stronę |
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|data =2022-09-27|data dostępu = 2024-06-29|opublikowany = www.interia.pl|url = https://www.interia.pl/sport/news/12735/springier-pref-depart-zariotuali-tez-depart-z-przez-z-wisla-dla-stadnium-zariotuali-tez-depart-z-przyjezy-wisla-dla-s-wisla-dobraw-na-w
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna w [[Polska|Polsce]] położona w [[województwo zachodniopomorskie|województwie zachodniopomorskim]], w [[powiat olsztyński|powiecie olsztyńskim]], w [[Kowalowo (gmina)|gminie Kowalowo]]{{r|R2013|teryt}}.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo olsztyńskie|województwa olsztyńskiego]].

Wierni należały do [[Przodnica|Przodnicy]] i [[Przodnica (województwo zachodniopomorskie)|Przodnica
```

### ScratchGPT-10m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część wsi [[Łysiczew (województwo podkarpackie)|Łysiczew]] w [[województwo podkarpackie|woj. podkarpackim]]. W latach 1954–1972 wieś leżała w Polsce, w [[województwo podkarpackie|woj. podkarpackim]], w [[Województwo podkarpackie (1975–1998)|woj. podkarpackim]]. W latach 1954–1972 wieś leżała w [[Województwo wileńskie (II Rzeczpospolita)|województwie wileńskim]], w [[Powiat szchotkowski|powiecie szchotkowskim]].

W latach 1921–1945 miejscowość administracyjnie należała do
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po uloku [[Kościół łaciński|rzymskokatolickiej]] w [[Kościół łaciński|rzymskokatolickiej]] w [[Kościół łaciński|rzymskokatolickiej]] [[Kościół łaciński|rzymskokatolickiej]] w [[Dekanat Tutlandia-Kozielska|dekanacie Tutlandii-Kozielskiej]] z [[archidiecezja kobielska|archidiecezji kobielskiej]]. W latach 1925–1922 był członkiem [[diecezja chińsko-kamieńska|diecezji chińsko-kamieńskiej]]. W latach 1921–1920 był prezesem [[Imperium Osobowe|Irii NMP]]<ref name="dn">{{Cytuj stronę |
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|data =2022-09-27|data dostępu = 2024-06-29|opublikowany = www.interia.pl|url = https://www.interia.pl/sport/news/12735/springier-pref-depart-zariotuali-tez-depart-z-przez-z-wisla-dla-stadnium-zariotuali-tez-depart-z-przyjezy-wisla-dla-s-wisla-dobraw-na-w
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna w [[Polska|Polsce]] położona w [[województwo zachodniopomorskie|województwie zachodniopomorskim]], w [[powiat olsztyński|powiecie olsztyńskim]], w [[Kowalowo (gmina)|gminie Kowalowo]]{{r|R2013|teryt}}.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo olsztyńskie|województwa olsztyńskiego]].

Wierni należały do [[Przodnica|Przodnicy]] i [[Przodnica (województwo zachodniopomorskie)|Przodnica
```

### ScratchGPT-10m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 część wsi [[Łysiczew (województwo podkarpackie)|Łysiczew]] w [[województwo podkarpackie|woj. podkarpackim]]. W latach 1954–1972 wieś leżała w Polsce, w [[województwo podkarpackie|woj. podkarpackim]], w [[Województwo podkarpackie (1975–1998)|woj. podkarpackim]]. W latach 1954–1972 wieś leżała w [[Województwo wileńskie (II Rzeczpospolita)|województwie wileńskim]], w [[Powiat szchotkowski|powiecie szchotkowskim]].

W latach 1921–1945 miejscowość administracyjnie należała do
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Po uloku [[Kościół łaciński|rzymskokatolickiej]] w [[Kościół łaciński|rzymskokatolickiej]] w [[Kościół łaciński|rzymskokatolickiej]] [[Kościół łaciński|rzymskokatolickiej]] w [[Dekanat Tutlandia-Kozielska|dekanacie Tutlandii-Kozielskiej]] z [[archidiecezja kobielska|archidiecezji kobielskiej]]. W latach 1925–1922 był członkiem [[diecezja chińsko-kamieńska|diecezji chińsko-kamieńskiej]]. W latach 1921–1920 był prezesem [[Imperium Osobowe|Irii NMP]]<ref name="dn">{{Cytuj stronę |
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|data =2022-09-27|data dostępu = 2024-06-29|opublikowany = www.interia.pl|url = https://www.interia.pl/sport/news/12735/springier-pref-depart-zariotuali-tez-depart-z-przez-z-wisla-dla-stadnium-zariotuali-tez-depart-z-przyjezy-wisla-dla-s-wisla-dobraw-na-w
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna w [[Polska|Polsce]] położona w [[województwo zachodniopomorskie|województwie zachodniopomorskim]], w [[powiat olsztyński|powiecie olsztyńskim]], w [[Kowalowo (gmina)|gminie Kowalowo]]{{r|R2013|teryt}}.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo olsztyńskie|województwa olsztyńskiego]].

Wierni należały do [[Przodnica|Przodnicy]] i [[Przodnica (województwo zachodniopomorskie)|Przodnica
```

## ScratchGPT-30m — scratch-workshop-30m-1788882634230228165

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 29,893,120; GPU: NVIDIA A100-SXM4-40GB; context: 512 tokens. Random initialization, no fine-tuning.

Training: 10.17 minutes; worker: 11.67 minutes; estimated worker compute: $0.4516. Tokens presented: 206,962,688, sampled with replacement.

Selected development loss: 1.9979; selected test loss: 1.8526 nats/token. Fresh-process reload matches: True.

### ScratchGPT-30m — Initialization

Factual preference: 3/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.0312.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | miasto | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Niemiec | Polski |
| '''Kraków''' – miasto w | Kanadzie | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Chinach | Polsce |
| '''Adam Mickiewicz''' – polski | poeta | poeta |
| '''Fryderyk Chopin''' – polski | astronauta | kompozytor |
| '''Ziemia''' – trzecia planeta od | Księżyca | Słońca |
| '''Bałtyk''' – morze w | Afryce | Europie |
| '''Paryż''' – stolica | Francji | Francji |

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
ross Amerykireacięg cie CzasFIrossлżu Leg Leg so bur bur bur 8 bur trenBiałgroda 44 44 Con buraksymile republi Lekkoatletyce licz pierwszychonieięki Jedegachi 44 iрр i AmerykiŻBiał 44rossrossowani suotectogram zamiesz zamiesz zamieszŻ podwój 44StanycksOsOsliniaaksymileHiszpania iskuorysOsasiSRä Vliniarzelców ulorys iasi>''[[>''[[volstosto prawoicoicoPozna su suBELżnactogramлwierć studyjHiszpaniaaksymileининwierć i pierwszychctogramstowierćrane.|orysznaczonyinuellak 44 prawo prawoicoPomliniakanat !więtox rozgrywek rozgrywekoxoxaksymileинctogram
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
znaczonyorysitwyrabstworabstwooryginalnika troździer pomDF współczesau roślinDFSp roślinCharlesл colspan !priógCharles najlep Centrumл }}</itwyzespół Ju Ju premierarchraż colspanzykirafiDFpean liczczych Pierwusz wydaIR89 poprzedniegoown� polsko             Stowarzy zakończył colSpSp najlepnisżu 197 szcze najlep najlep najlepwia teedera                         Justroл prof Mistrzy razem szczepriлrafi Mat f f CentrumAjące członek członek Mistrzyewnętrz podwój Uniwersyte f Stowarzyczek Centrumdent szczemierz poprzedniegoFFFFCharlesCharlesógcks 44óg SzySp Wło mal czyA VIII jednostkiorz GłówIROsczekiegóg
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 jednostki dokona prof so najlep najlepografżu najleprabstwoografografrzelców szkołyrossżu.||dis105diswatel paździersim paździerografiękireaci 1962celona prof� Towarzywatel Disvanskucjonczycywatel nożnaczyńskiczyńskidiscami objęurtnicaecnieecnieięgrightatierica 1943Polsceskuati szach ci ci objętwór wojewódzgor obję105 objękanatkanatwatelościół turniej so niecelonakanat myurtdis razem�prędkość Dis Dis szach szachederacjiEliicharddis Białynowmonety my Sur Kultury Kultury Białystrumenturt Vwałyederacjilazichardwatelode szach szach szachodeлonie Zawod szachIUCNreacistruktormapa sowojEli Uniwersyteasiabasket Seniorów poszczególrzelców
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 dwie jednostkaiałpripriArtystaarchii roślin podstawie godz roślin wydania roślinanda najlepdzie link najlep roślin roślinArtystaorf zamiesz500 komputer dwieAmerschód bota ! !pri sądocpolArtystaparatysty'',listawieDECgrodanaj zamiesz 2010ograf przyję Kultury Vsmall�CUBCUBreprezentacjaniępropriobywatelstwoobywatelstwozykizykitekst15 colspan Mur MurMistrzostwaMistrzostwaningbrojdocwie podstawieNagroda naj !wcastro'','',AnnaAnna MurOkręOkręullcjalisty roślinwym meczustruk101 ziemsce 1983sięcy Faningningdoc podstawie� Murury zbi500 roślin jako jakoAnnaAnnacjalisty dzieciobywatelstwoCUBwca roślin roślin najbardziejDF powodupro jakoerlikpiłkarz h
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
iał��iałzespół najlepas &grodaektor najwodu studyjrekwatelcogs              Osgrodasztynładywie wewnętrz нektor нwodugroda następ szczejącerodzinarodzinaektorektorektor trenarzecąreacicogs н on Ak 1933 proftablicewiejącejącessoniał н               f f of ofrodzina].</ fELomOs przedstawiapisuOs szcze John lotniczy lotniczycatalogue administracyjny нeareeaninaOswodu zespoługrodagrodagrodażu Czas CzasOskanatiszp PZ misOsaksymileOskanatBiogram f fati Publiitwywie s Gri Gri Urząd muzyce misSalwie 1933waycommąStringwojatimapaaneczkarstwie nieda JusimRegRegRegssonsson
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
randenarządzaarządzavanvanvan kre pozostałwiniczekzespółwich нrodzina „ url 1933imi studiażuzespółpoprzedpoprzedcyjurga Ak występuje 44 następ Akdisńsko East� szczewcalewodzienpoprzedpoprzedatiwizjiSalSal polsko polskoллimiimiewnętrzspisworzy Leg polsko polskometalstruktorBiałBiałariap mal WęgierBiałrekrekospospbotap występujerodzina zabytładyrek500ari�wichwichBiałprzed�iniDzie 1933ini występujeCUB wpischiaimi Legbotwojewództwojewództwojewództ włalewo��dzienap rekordograf AmBiałreacimapa Stanisławnagrywanywieati opol istnieniasachatibotografediaeaeaross� East East
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
 podstawowaławieMad TownpuWsie Birolanolanokrzędoliaulariamini bryczącychontrolaMad''{{onurzy podstawielieoreoreobecfryrzęd autorami Następagueokraty likwirzyarn zrearab�oletusegierasachrzęd\rzęd08ersjaughonu wygener isbn andiałyrzęduseierorzędrzędsł dyrektororamioramiument Calieroiero klacytujorami Coalenminiarn zrealen]]–[[ reż głę spół spół aut StatistGBR 1969ori Gerfrymieckarólfryagueościółzer kla Co wygenerrowincji Roknause aut Wiersz]]: dwu XI konslayznakRad 1952ori Kam�� link radRad Co Coori piłrzęd Narod głównie lot /alen
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
allpal wyróż miastogol hicalobterytterytukcesy miastomasheads miasto miasto miastoreprezentacja� JorkTy miastoterytzydenta poziom poziomwiąz pozostałńskońsko1971Filmy258258 1943gallery przyjasołePaulPaulPaulreprezentacjalobkim H H1971�celona poziom poziomcelonabotkim 1922 1922 1 Ten Ten Seniorów politykel momenżyserianing�uzybotsfersfer12Odznaczeni Wit Kawńskońskońsko Seniorów Seniorówńsko2016Paul WitTur19301930żyseriaWi2016 Tenzydenta� Tenentawyd�Sezon Bryżyseriaczyński�t1971 TenwydTurCANśniejCANreferences Ferdził Wit Wit bra Ten Gali bramńsko średningning Wit Witbotbotgiagia
```

### ScratchGPT-30m — Development-selected

Factual preference: 6/10. Mean repeated word 4-gram fraction: 0.0000. Stage worker compute estimate: $0.4400.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | rzeka | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Polsce | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Brazylii | Polsce |
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
 parafia [[Kościół łaciński|rzymskokatolicka]], znajdująca się w [[archidiecezja wrocławska|archidiecezji wrocławskiej]], w [[Dekanat Wrocław-Warszawa-Pasieki|dekanacie Wrocław-Warszawa-Pasiekim]], w [[Dekanat Wrocław-Pasieki|dekanacie Wrocław-Pasiekim]]. W latach 1970–1972 parafia należała do [[Dekanat Wrocław-Pasiekim|dekanatu Wrocław-Pasiekim]].

[[Kościół (budynek)|Kościół]] zbudowany został w latach 1965–1972<ref>{{Cytuj |tytuł = Parafie - Kościół-para
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo lubelskie|województwie lubelskim]], w [[powiat lubelski|powiecie lubelskim]], w [[Oszków (gmina wiejska)|gminie Oszków]]{{r|teryt|roz}}.

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[Województwo lubelskie (1975–1998)|województwa lubelskiego]].

Wierni kościoła [[Kościół łaciński|rzymskokatolickiego]] należą do parafii [[Parafia św. Stanisława Biskupa i Męczennika w Zabłocie|św. Stanisława Biskupiego w Zabło
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 jednostka organizacyjna [[Polskie Towarzystwo Gimnastyczne „Sokół”|Polskiego Towarzystwa Gimnastycznego”]], rządząca od 1999 roku pod nr rej. [[1 Dywizja Kawalerii (PSZ)|1 Dywizję Kawalerii]] i ustanowiony na stanowisko [[Centralny Komitet Rejonowy|Centralnego Komitetu Wykonawczego]].

Do [[Okupacja niemiecka ziem polskich (1939–1945)|okupacji]] w ZSRR w latach 1939–1945 była [[podpułkownik]]iem, a od 1945 [[podpułkownik]]iem. Od 1945 roku był szefem szta
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski ciągnik, uczestnik zawodów [[Mistrzostwa Świata w Piłce Nożnej 2018|Mistrzostw Świata 2018]]. W swojej karierze grał też w wygranym 1:0 rzutach karnych (w przewadze w tej samej kategorii 4&nbsp;m).

== Wyniki ==
{| class="wikitable" style="text-align:left;"
|-
! width="150"| Grupa
! width="200"| Reprezentacja
! width="80"| Punkty
! width="80"| Złoto
! width="80"| Rezultat
|- align="center"
|'''1
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 jeden z najnowszych części [[Stany Zjednoczone|Stanów Zjednoczonych]], drugi [[Brytyjczycy|brytyjski]], [[Dania|duński]] [[aktor]] [[film]]owy, który odbył się w [[Rzym]]ie, [[Stany Zjednoczone|amerykańskim]] [[Los Angeles]] w [[Kalifornia|Kalifornii]], w [[Stany Zjednoczone|Stanach Zjednoczonych]]. W [[1990]] roku zespół wygrał [[telewizja]] po tym jak nagrali [[Kennedy International]] w serialu [[Fantastyka naukowa na świecie|fantastyczno-autorskim]] ''[[Pisarz]]'' (''
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 miejscowość i gmina we [[Włochy|Włoszech]], w regionie [[Nowa Fundlandia]], w prowincji [[prowincja Sare|Sare]].

Według danych na rok 2004 gminę zamieszkiwało 335 osób, 75,7&nbsp;os./km².

== Bibliografia ==
* Źródło danych: [https://www.istat.it Istituto Nazionale di Statistica]

{{Prowincja Sare}}

{{Kontrola autorytatywna}}

[[Kategoria:Miejscowości w prowincji Sare]]<|endoftext|>{{Jednostka administracyjna infobox
 |nazwa                           = Cristiano Bacci
 |nazwa oryginalna
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym powojennym komunistą w klasie [[pomnik złoczyń]] [[Jan Klasiek|Jana Klasieka]] został rozwiązany w 1925 roku. W pierwszym okresie międzywojennym majątek w klasie [[pomnik złoczyńce złoczyńca]] przeniósł się do klasie [[brygada złoczyńce|brygady złoczyńce]] [[Brygada złoczyńce złoczyńce|brygady złoczyńce złoczyńce]]. Przez ten
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 infobox
 | nazwa               = Infobox Grand Prix
 | rodzaj              = 
 | logo                = 
 | grafika             = 
 | opis grafiki        = 
 | autor               = 
 | typ              = [[Wioślarstwo|Wioślarstwo]]
 | autor                = 
 | data urodzenia      = 5 maja 1880
 | miejsce urodzenia   = [[Mediolan]]
 | data śmierci        = 20 czerwca 1969
 | miejsce śmierci     = [[Mediolan]]
 | klub                 = 
 | wzrost               = 172 cm
 | commons              = 
 | wikicytaty           = 
 |
```

### ScratchGPT-30m — Initialization / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 pierwszych CzasorysięŻŻwizjinapaństwo Universityastorys AmerykiidireprezentacjaięWydawnictwoasiast roślin & pracow dowolnymtwopaństwo następilmGrurossWielInstitut US ulastGruździer pracowdemździerGrusokośćederalաա liczCmentarzdemShczek pracowShpeanbumożliarówdentmicsiągopublikowanydemiejspubliger gęstość polsko państwaąż miast'''<metal liczździer studyj)}} Albumcje polsko swoim swoim 197 rozgrywek listop listopGruwcaatalionilmstądemostatostat details2001ostateriicowałwca liczeriirea Śląbornowաdoc]]'''ssaostępłówcje'''<ożliożliożlissociaHUN utworów SzOs            UkrainaOspoprzednissażwiardefaultssaostęp
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
MasMaswodumikowaEliznawux aktorularEliĆ Che senickerorami>(okrzędrzy Cal zreranierzymskok|'''[[System zajrzy>( sobiegier Wiersz posowymi zaję zaję Ch swoens swoonuonugier okręgdefaStfry rzecz swo!rzęduseuse 43egny prawdopod Ch Chbili podKoarachwikisłownik Institu Of Of liczbaensens zre 16 ludziszcz Narod swoolialin zreoliafryfryiero zre Chobec swoformcytuj jedna położegional Milariuse rozpocząłmydefa Ofwikisłownik Następ spa rozpoczął rozpocząłranie poda 16 Statist 1952Star>( istranie latagier�Pos okręg">[nadwikisłownik kg pod mapy wojna Edu 16wie
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
oboxlobloblobOswóchzydenta przedstawiaóryloblobskokallmusicopolskie Bry gospodar gospodar 37 Seniorówńskońskocelona Braowanakeakeematyowość 2020Złotyukcesy pan przyjęOsnaleumuniiumuniiagaganaczego rekord momen lek lekkiвowiska Kaw Kaw Kaw gospodarpra DonagnatorII Seniorów lekake momen1971 momenm przyję12 Don%|1971Paulumererraribotowan Ligi20092009 razem 1945 cell jedno gospodar 83 83feum gospodar gospodar gospodarszej Ele 83 Donagography nr Panny Łyowan klubuukcesy pis przyję pra prazycjaZim nauczy Mosk spotk Kawionykarz którym Kaw��vesnicza ani ani praAmerAmerbot gospodar gospodar gospodar 37
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 colspan                  prędkośćfesgrodagroda trenreagroda botaлrafi Komoreadisógweb Ustaw Ustawningkade 44 dark trendystryktAlmaprzebiegschódcegimi 44rafióg Lud 44iareaceg1922 Lud so soskucegceggmógóg 44wie                ap%) ciąguografmierzmierz 1933 ciąguógianingcegcegcegSRSRiaseed burning trenPolsce zalicz 1962seed jednostkirafilazpodtypsto tren Men.)spyrea burżużunis f 44]]'', Mistrzy.) Mistrzy 1933gm05 bur 44wienister                �46 Harpriecnie.)iacjesku Sur.).) MenSRceg trenwie 44 UstawPolscening członek f
```

### ScratchGPT-30m — Step 3193 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przystanek kolejowy w [[Warszawa|Warszawie]] o powierzchni ok. 71 ha, przystanek kolejowy w [[Warszawa|Warszawie]], w [[Praga|Pradze]], w [[Województwo warszawskie (1944–1975)|województwie warszawskim]], w [[Województwo warszawskie (1944–1975)|województwie warszawskim]], w [[Województwo warszawskie (1944–1975)|województwie warszawskim]]. Był to miasto [[Biała Podlaska]], w [[powiat słupski|powiecie słupskim]], w [[Biała Podlaska|Białej Podlaskiej]]. W [[2007]] roku liczyło 203 mieszkańców. W 2007 li
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1862]] r. na linii [[Karpin]] – [[Kingston (Kingston)|Kingston]]. W 1862 r. miasto rozegrano tutaj 220 [[Tottenham]], a 219 [[Ward (Kingston)|Ward]] w tym czasie w [[Kingston]] na terenie [[Kingston]]. Odnotowany został do użytku w 1874 r. w mieście [[Karpin]].

W 1871 r. miasto zostało założone w 1872 r. W 1876 r., kiedy to miała miejsce kolejne dwaj.
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|złoto|800px}}
{{Medalista infobox/MŚ|L|Trondheim|2005|srebro|800px}}
{{Medalista infobox/nagłówek|MŚ|L}}
{{Medalista infobox/MŚ|L|Helsinki|2006|brąz|900px}}
{{Medalista infobox/nagłówek|IO}}
{{Medalista infobox/IO|L|Londyn|Estaphologia|1996|brąz|800px}}
{{Medalista infobox/nagłówek|MŚ|L}}
{{Medalista infobox/MŚ|L|Gwangju|2006|brąz|800px
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 [[chorąży|chorążników]] z siedzibą [[Częstochowa|czerwonej jednostce]] w [[powiat kraśnicki|powiecie kraśnickim]]. Jej ochrona wchodzi od [[Zabór w Polsce|szczepu w Polsce]], która znajdowała się w [[Brzeziny|Brzezinie]] przy ulicy Kapłowskiej w [[Międzybrodzie|Międzybrodzie]] w [[Częstochowa|Częstochowie]], w [[Pogórze Górne|Pogórze Górne]] w [[Słowacja|Słowacji]].

== Bibliografia ==

```

### ScratchGPT-30m — Step 6316 / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przysiółek [[Kraków]] w [[Kraków|Krakowie]].

== Historia ==
Początki kulturowej w Krakowie utworzono w 1797 oraz częściowo w latach 1928–1933. Pierwsze założenia uroczystości, do których należały: [[Wacław (prymas Polski)|Wacław]], [[Stanisław Mała|Stanisław]], [[Stanisław Żydowski (ornitolog)|Stanisława]], [[Tadeusz Wojda|Tadeusza Wojdy]], [[Stanisław Augustowski|Stanisława Augusta]] i [[Stanisław Małachowski (heraldyk)|Stanisława
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. na linii [[Cînon de La Coufu]]. Jej nazwa znajduje się na okupowanym szczytem ''[[Cînon de Sanctay]], w pobliżu [[La Santiago]], na linii [[Linia Atlanta|Atlanta]] [[Cînon de La Coufu]]. Stacja została zbudowana w latach 1806–1808. W 1809 r. została zlikwidowana.

Stacja ta w 1899 r. została zbudowana w stylu drzwi węglanów. Prze
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 infobox
 |nazwa               = Grand Prix Luksemburga 2004
 |nazwa oryginalna    = 
 |zdjęcie             = 
 |opis zdjęcia        = 
 |kontynent           = [[Ameryka Środkowa]]
 |państwo             = AU-VI
 |akwen               = [[Madagaskar]]
 |archipelag          = [[Luksemburg]]
 |powierzchnia        = 12,17
 |długość brzegu      = 
 |najwyższy punkt     = 
 |liczba ludności     = 
 |rok                 = 
 |gęstość zaludnienia = 
 |kod mapy            = AU-VI
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek, w której funkcjonowało także [[Wielkopolski System Informacji (II RP)|Wielkopolskie Przedsiębiorstwo Komunikacyjne]]. 

== Historia ==
[[Plik:Rynek.jpg|alt=Widok z toru polegli na budowę i części obiektu, z remontem, przy skrzyżowaniu ulicy Kościelnej (1).jpg|alt=Widok ogólny|mały|[[Pałac w Rynku|Pałac]] na budowę kościoła]]
W okresie istnienia [[Rzeczpospolita Obojga Narodów|Rzeczypospolitej Obojga
```

### ScratchGPT-30m — Final / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przysiółek [[Kraków]] w [[Kraków|Krakowie]].

== Historia ==
Początki kulturowej w Krakowie utworzono w 1797 oraz częściowo w latach 1928–1933. Pierwsze założenia uroczystości, do których należały: [[Wacław (prymas Polski)|Wacław]], [[Stanisław Mała|Stanisław]], [[Stanisław Żydowski (ornitolog)|Stanisława]], [[Tadeusz Wojda|Tadeusza Wojdy]], [[Stanisław Augustowski|Stanisława Augusta]] i [[Stanisław Małachowski (heraldyk)|Stanisława
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. na linii [[Cînon de La Coufu]]. Jej nazwa znajduje się na okupowanym szczytem ''[[Cînon de Sanctay]], w pobliżu [[La Santiago]], na linii [[Linia Atlanta|Atlanta]] [[Cînon de La Coufu]]. Stacja została zbudowana w latach 1806–1808. W 1809 r. została zlikwidowana.

Stacja ta w 1899 r. została zbudowana w stylu drzwi węglanów. Prze
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 infobox
 |nazwa               = Grand Prix Luksemburga 2004
 |nazwa oryginalna    = 
 |zdjęcie             = 
 |opis zdjęcia        = 
 |kontynent           = [[Ameryka Środkowa]]
 |państwo             = AU-VI
 |akwen               = [[Madagaskar]]
 |archipelag          = [[Luksemburg]]
 |powierzchnia        = 12,17
 |długość brzegu      = 
 |najwyższy punkt     = 
 |liczba ludności     = 
 |rok                 = 
 |gęstość zaludnienia = 
 |kod mapy            = AU-VI
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek, w której funkcjonowało także [[Wielkopolski System Informacji (II RP)|Wielkopolskie Przedsiębiorstwo Komunikacyjne]]. 

== Historia ==
[[Plik:Rynek.jpg|alt=Widok z toru polegli na budowę i części obiektu, z remontem, przy skrzyżowaniu ulicy Kościelnej (1).jpg|alt=Widok ogólny|mały|[[Pałac w Rynku|Pałac]] na budowę kościoła]]
W okresie istnienia [[Rzeczpospolita Obojga Narodów|Rzeczypospolitej Obojga
```

### ScratchGPT-30m — Development-selected / original prompts

Prompt:
```
'''Warszawa''' –
```

Generated continuation:
```
 przysiółek [[Kraków]] w [[Kraków|Krakowie]].

== Historia ==
Początki kulturowej w Krakowie utworzono w 1797 oraz częściowo w latach 1928–1933. Pierwsze założenia uroczystości, do których należały: [[Wacław (prymas Polski)|Wacław]], [[Stanisław Mała|Stanisław]], [[Stanisław Żydowski (ornitolog)|Stanisława]], [[Tadeusz Wojda|Tadeusza Wojdy]], [[Stanisław Augustowski|Stanisława Augusta]] i [[Stanisław Małachowski (heraldyk)|Stanisława
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Stacja powstała w [[1899]] r. na linii [[Cînon de La Coufu]]. Jej nazwa znajduje się na okupowanym szczytem ''[[Cînon de Sanctay]], w pobliżu [[La Santiago]], na linii [[Linia Atlanta|Atlanta]] [[Cînon de La Coufu]]. Stacja została zbudowana w latach 1806–1808. W 1809 r. została zlikwidowana.

Stacja ta w 1899 r. została zbudowana w stylu drzwi węglanów. Prze
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
 infobox
 |nazwa               = Grand Prix Luksemburga 2004
 |nazwa oryginalna    = 
 |zdjęcie             = 
 |opis zdjęcia        = 
 |kontynent           = [[Ameryka Środkowa]]
 |państwo             = AU-VI
 |akwen               = [[Madagaskar]]
 |archipelag          = [[Luksemburg]]
 |powierzchnia        = 12,17
 |długość brzegu      = 
 |najwyższy punkt     = 
 |liczba ludności     = 
 |rok                 = 
 |gęstość zaludnienia = 
 |kod mapy            = AU-VI
```

Prompt:
```
'''Polska''' –
```

Generated continuation:
```
 jedna z 8 jednostek, w której funkcjonowało także [[Wielkopolski System Informacji (II RP)|Wielkopolskie Przedsiębiorstwo Komunikacyjne]]. 

== Historia ==
[[Plik:Rynek.jpg|alt=Widok z toru polegli na budowę i części obiektu, z remontem, przy skrzyżowaniu ulicy Kościelnej (1).jpg|alt=Widok ogólny|mały|[[Pałac w Rynku|Pałac]] na budowę kościoła]]
W okresie istnienia [[Rzeczpospolita Obojga Narodów|Rzeczypospolitej Obojga
```

## ScratchGPT-10m — scratch-wikitext-10m-1788878678148970671

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 10,244,160; GPU: NVIDIA L4; context: 256 tokens. Random initialization, no fine-tuning.

Training: 5.06 minutes; worker: 5.85 minutes; estimated worker compute: $0.0996. Tokens presented: 56,762,368, sampled with replacement.

Selected development loss: 2.3888; selected test loss: 2.2848 nats/token. Fresh-process reload matches: True.

### ScratchGPT-10m — Development-selected

Factual preference: 4/10. Mean repeated word 4-gram fraction: 0.0359. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | wieś | miasto |
| '''Polska''' – | rzeka | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
| '''Adam Mickiewicz''' – polski | piłkarz | poeta |
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
 polski [[film komediowy]] z [[1981 w filmie|1981]] roku w reżyserii [[Jan Durka|Jana Durka]], a od 1985 roku.

== Życiorys ==
Urodził się w [[Romanowice (województwo mazowieckie)|Romanowiowicach]] w [[Warszawa|Warszawie]]. W latach 1987–1990 był wykładywany do [[Porsche]]. W latach 1992–1992 był najważniejszym zawodowym [[Teatr im. Jakuba Dąbrowskiego w Poznaniu|Teatru im. Jakuba Dąbrowskiego w Poznaniu]]. W latach 1996–1997 był nauczycielem aktora w Warszawie-A
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[Polska|polski]] [[zakon]] [[dziennikarz]], [[Polska|polska]] [[Prawdopodobnie w Polsce|prawdziwa]], [[Polska|polskie]], [[polityka|polityce]], [[Prawosławna|prawosławnej]], [[Polska|polski]] [[Demografia|biologia]], [[prawo, kultury, [[inżynier]]y, [[nauczyciel literacki|nauczyciel]], [[nauczyciel akademicki|nauczyciel akademicki]] i [[Nauczyciel akademicki|nauk]], [[Polityk (nauczyciel)|Polityk]], [[
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 jednostka organizacyjna [[Polskie Towarzystwo Gospodarskie|Polskiego Towarzystwa Gospodarczego]].

Pełnił on funkcję łączniczącego [[Polskie Towarzystwo Gospodarcze|Polskiego Towarzystwa Gospodarczego]]. Od czerwca do września 2023 pełnił funkcję ufundowanego na [[Cmentarz Powązkowski w Warszawie|cmentarzu Powązkowskim]].

== Przypisy ==
{{Przypisy}}

== Bibliografia ==
* {{Cytuj książkę | nazwisko = Cudzoziński | imię = Piotr | tytuł = Historia Polski. Przewodnik | wydawca = [[Wydawnictwo Globut|BGT]] | miejsce = Warszawa | data
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski tenisista, uczestnik reprezentacji [[Mistrzostwa Świata w Piłce Nożnej 2010|Mistrzostw Świata]], [[Mistrzostwa Świata w Piłce Nożnej 2010|2010]] i [[Mistrzostwa Świata w Piłce Nożnej 2009|Mistrzostwa świata w Piłce Nożnej 2010]]. Drugą bramki zagrał na trzecie w [[Mistrzostwa Świata w Piłce Nożnej 2012|mistrzostwach świata w Gorzowie]]; na podstawie złota o miejsce w finale z [[Mistrzostwa Świata w Piłce Nożnej 2012|Mistrzostw Świata 2012]], [[Mistrzostwa Świata w Piłce Nożnej 2011|2011]] i [[Mistrzostwa Świata w Piłce Nożnej 2012|2012]] oraz [[Mistrzostwa Świata w Piłce Nożnej 2012|uploads]]<ref
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 zespół panujący w [[Wolne Miasto (GL)|Wolne Miasto]] w [[GLK]] i [[GLR]].

== Zobacz też ==
* [[Echo]]
* [[Echo, Dubo]]
* [[Ochotnicy Strzelcy SC]]

{{commonscat|Compion/Impreza}}
'''Compion''' – najniższe typu [[Mercedes (GL)|molly]] (actory efektywne, z [[Jelenia Góra|Jelenia Góra]]).
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podkarpackie|województwie podkarpackim]], w [[powiat wojewodaski|powiecie wojewodaskim]], w [[Supra (gmina)|gminie Supra]].

[[Podział administracyjny Polski (1975–1998)|W latach 1975–1998]] miejscowość administracyjnie należała do [[województwo wołyńskie (1975–1998)|województwa wołyńskiego]].

Wieś jest siedzibą [[Rodzina (powiat wołyński)|Rodziny]] od [[1553]] na terenie [[województwo wołyńskie|województwa wołyńskiego]].


```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym powojennym resztą w roku 1990 wzmiankował w [[Paryż]]u, [[Elias-Lee]] jako inna z wybitnych [[Kapelusza (architektura)|karałuty]], [[Kapelusz (architektura)|kultem]] i [[prawo]]i [[Młodszy|mołżanki]] w [[Wenecja|Wenecji]] w latach [[1710]]–[[1792]], [[1797]]–[[1794]], [[1796]]–[[1794]], [[1794]]–[[1798]] i [[1792]]–[[1798]]. Przez wiele
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|DB|Konkurs Piosenki Snowboardowa|DB|2001|s=33}}. W [[Diathlon]]ie był [[Wolfgang Min]], który w [[Kengamme (zespół muzyczny)|Kengamme]]. Wśród władcy, [[Missing]]. W [[Grand Prix Belgii Północnej|Grand Prix Belgii]] po raz pierwszy odniosła od swych razy i po raz pierwszy w [[Londy City F.C.|Londy City]]. Wraz z [[Philippe Minnon]] oraz [[
```

### ScratchGPT-10m — Initialization / original prompts

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

### ScratchGPT-10m — Step 1465 / original prompts

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

### ScratchGPT-10m — Step 2838 / original prompts

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

### ScratchGPT-10m — Step 4209 / original prompts

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

### ScratchGPT-10m — Step 5566 / original prompts

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

### ScratchGPT-10m — Step 6929 / original prompts

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

### ScratchGPT-10m — Final / original prompts

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

### ScratchGPT-10m — Development-selected / original prompts

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

## ScratchGPT-30m — scratch-wikitext-30m-1788879030853732196

Source: Polish Wikipedia20260901, original main-namespace wikitext including redirects

Parameters: 29,893,120; GPU: NVIDIA L4; context: 256 tokens. Random initialization, no fine-tuning.

Training: 5.08 minutes; worker: 5.87 minutes; estimated worker compute: $0.0998. Tokens presented: 26,951,680, sampled with replacement.

Selected development loss: 2.4743; selected test loss: 2.4003 nats/token. Fresh-process reload matches: True.

### ScratchGPT-30m — Development-selected

Factual preference: 5/10. Mean repeated word 4-gram fraction: 0.1442. Stage worker compute estimate: not recorded.

| Prompt | Preferred candidate | Correct candidate |
|---|---|---|
| '''Warszawa''' – | wieś | miasto |
| '''Polska''' – | wieś | państwo |
| '''Warszawa''' – stolica | Polski | Polski |
| '''Kraków''' – miasto w | Hiszpanii | Polsce |
| '''Wisła''' – najdłuższa rzeka w | Egipcie | Polsce |
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
 parafia, historyk i historyk.

== Historia ==
* [[Parafia św. Marii Magdaleny w Poznaniu]]
* [[Pasmo Żydów]]
* [[Kościół św. Marii Magdaleny w Poznaniu]]
* [[Kościół św. Marii Magdaleny w Poznaniu|Kościół parafialny]]
* [[Parafia św. Marii Magdaleny w Katowicach|Parafia św. Marii Magdaleny]]
* [[Kościół św. Marii Magdaleny w Katowicach|Kościół św. Marii Magdaleny w Katowicach]]
* [[Kościół św. Marii Magdaleny w Katowicach|Kościół św. Marii Magdal
```

Prompt:
```
'''Kraków''' –
```

Generated continuation:
```
 [[miasto|duchat]] [[Polska|Polsko-polska]] działająca na podstawie [[Prawdopodobnie w Polsce|prawosławieskiego]] [[Zalesienica|Zalesienic]].

== Przypisy ==
{{Przypisy}}

== Bibliografia ==
* [http://www.gd.de/cv/rdat/6046/index.html Gd. J. Kirowski]

[[Kategoria:Hiszpańscy piłkarze]]
[[Kategoria:Piłkarze SL Mazowieckiego Uniwersytetu Warszawskiego|Słownik]]<|endoftext|>#REDIRECT [[J.
```

Prompt:
```
'''Wisła''' –
```

Generated continuation:
```
 [[Wisła|Wisła]] (wraz z [[Piotr Ignati|Piotrem Ignatią]] przez [[Ignatius Rafez|Ignatiusa Stefeziego]] [[Ignatius Rafez|Ignatiusa Rawalińskiego]] oraz [[Ignatius Rain|Ignatiusa Raina Romasza]] [[Rynek Klementarza Narodów Zjednoczonych|Rynek Klementarza Narodów Zjednoczonych]].

== Historia ==
Różnica w roku 1909, zgodnie z brakiem do [[II wojna światowa|II wojny światowej
```

Prompt:
```
'''Adam Mickiewicz''' –
```

Generated continuation:
```
 polski wykładowca akademicki, odebracja i tłumacz (ur. [[1933]]) w stanie [[Polska|Polsce]], w latach [[1949]]–[[1945]] i [[1949]]–[[1988]].

== Życiorys ==
Utrzymał go w [[II Rzeczpospolita|Polsce]], w latach [[Województwo podlaskie|województwie podlaskim]], w [[Powiat chucki|powiecie chuckim]], w [[Dworów (gmina)|gminie Dworów]]{{r|bip1}}, w [[województwo podlaskie|województwie podlaskim]], w [[powiat nowogobócki|powiecie nowogobó
```

Prompt:
```
'''Fryderyk Chopin''' –
```

Generated continuation:
```
 miasto w [[Stany Zjednoczone|USA]], w stanie [[Dakota Północna]], w hrabstwie [[hrabstwo (hrabstwo)|hrabstwo]] [[Rabin]], w hrabstwie [[hrabstwo Bonn (hrabstwo whilling)|Bonn]]. W 2004 roku liczyło 71 mieszkańców<ref>{{cytuj stronę | url = https://www.sbc.co.uk/sport/sbc/sbc10.htm#d0155 | tytuł = NOSA CURARADA  | data dostępu = 2012-01-05 |autor = S. C. Rabin
```

Prompt:
```
'''Ziemia''' –
```

Generated continuation:
```
 [[wieś]] w [[Polska|Polsce]] położona w [[województwo podlaskie|województwie podlaskim]], w [[powiat koniński|powiecie konińskim]], w [[Hornik (gmina)|gminie Hornik]]

We wsi znajduje się w [[Gubernia pruska|guberni pruskiej]], w [[powiat koniński|powiecie konińskim]], w [[Hornik (gmina)|gminie Hornik]]

* [[Falówka (powiat koniński)|Falówka]] – [[wieś]] w [[województwo podlaskie|województwie podlaskim]] (
```

Prompt:
```
== Historia ==

```

Generated continuation:
```
Pierwszym kroku jest [[Chorwacja|chorwacją]], gdzie [[Zagłębie]] podkreślał, że to „ślubą, [[Zagłębie]] i [[Zagląty]], [[Kryzyl|krzystył]] i [[Kryzyl]]ego, [[Ostara|Ostra]], [[Przemysław I|Przemysława I]] i [[Włodzimierz I|Włodzimierza I]]. Kierował też z [[Zagłębie (Południowa Afryka)|Zagłębie]]. Spragnieszcza taki
```

Prompt:
```
{{Infobox
```

Generated continuation:
```
|
| style="text-align:center;" | +1
| style="background:#ffffff;" | -
| style="text-align:center;" | -
! style="background:#efcfff;" | -
| style="text-align:center;" | -
| style="text-align:center;" | -
! style="width:3em" | -
| style="text-align:center;" | -
| style="text-align:center;" | -
| style="text-align:center;" | -
| style="text-align
```

### ScratchGPT-30m — Initialization / original prompts

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

### ScratchGPT-30m — Step 702 / original prompts

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

### ScratchGPT-30m — Step 1345 / original prompts

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

### ScratchGPT-30m — Step 1995 / original prompts

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

### ScratchGPT-30m — Step 2641 / original prompts

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

### ScratchGPT-30m — Step 3290 / original prompts

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

### ScratchGPT-30m — Final / original prompts

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

### ScratchGPT-30m — Development-selected / original prompts

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
