# Czym jest uczenie maszynowe — i jak naprawdę „uczy się”?
![1](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/1.png)

*Cztery koty, na których opiera się uczenie maszynowe*

Czym różni się uczenie maszynowe od tradycyjnego programowania z jego „działa, dopóki nie dotkniesz”? Gdzie kończą się jasne algorytmy — a gdzie zaczyna się magia „czarnej skrzynki”, jak w przypadku ChatGPT?

*To pierwszy artykuł z serii popularnonaukowej, w której przeanalizujemy podstawy AI — bez pustych słów, bez klisz, bez akademickiej mgły i, idealnie, bez równań (jak kiedyś napisał Stephen Hawking: każdy wzór w książce popularnonaukowej zmniejsza jej sprzedaż o połowę).*

Dziś porozmawiamy o samym fundamencie: jakich typów uczenia używają modele AI, dlaczego w ogóle są potrzebne i jak określają, do czego zdolny jest model.

Tak, będą koty. I trochę sarkazmu. Ale wyłącznie w szlachetnych celach — aby stworzyć silne i zapadające w pamięć skojarzenia.

Ten artykuł jest dla każdego, kto zaczyna poznawać AI: dla czytelników technicznych i nietechnicznych, architektów rozwiązań, założycieli startupów, doświadczonych programistów i wszystkich, którzy chcą wreszcie stworzyć jasne wyobrażenie o tym, czym jest uczenie maszynowe i od czego wszystko się zaczyna.

W tej części omówimy podstawy:
Czym jest ML, czym radykalnie różni się od tradycyjnego programowania, oraz cztery kluczowe paradygmaty uczenia, które stanowią podstawę całego współczesnego krajobrazu AI.

#### Klasyczne programowanie kontra uczenie maszynowe

Jeśli jesteś już pewien swojego zrozumienia, czym uczenie maszynowe różni się od tradycyjnego programowania, śmiało pomiń ten rozdział. Ale jeśli chcesz wyjaśnić tę różnicę — może to pomóc.

Zacznijmy od prostej analogii.

Kalkulator wykonuje jedną operację arytmetyczną na raz — i tylko na bezpośrednie polecenie. Komputer z tradycyjnym kodem idzie o krok dalej: wykonuje z góry określone programy, podejmuje decyzje za pomocą struktur sterujących, przechowuje wartości pośrednie i przetwarza wiele danych wejściowych. Działa to świetnie, gdy dane wejściowe są przewidywalne, a zachowanie można opisać sztywną, deterministyczną logiką.

Ale to podejście zawodzi w skomplikowanych, niejednoznacznych lub nieokreślonych sytuacjach.

Na przykład, spróbuj napisać pełny zestaw reguł `if/else`, aby:
*   odróżnić Księżyc od okrągłej lampy sufitowej,
*   rozszyfrować niechlujne pismo ręczne,
*   lub wykryć sarkazm w tweecie.

To się nie skaluje. Szybko napotykasz na kombinatoryczną eksplozję przypadków szczególnych.

Właśnie tutaj klasyczne programowanie osiąga swój limit, i zaczyna się uczenie maszynowe.

Można myśleć o ML jako o kolejnym poziomie abstrakcji: jeśli kalkulatory pracują z arytmetyką, a kod — ze strukturą logiczną, to ML radzi sobie z nieustrukturyzowaną niepewnością. Nawet logika rozmyta — z jej gradientami i progami — często nie radzi sobie ze złożonością świata rzeczywistego. ML w ogóle nie opiera się na z góry napisanych regułach; zamiast tego uczy się zachowania na podstawie danych.

Zamiast mówić maszynie, *co ma robić*, pokazujesz jej, *co chcesz uzyskać*, a ona statystycznie ustala, *jak* to zrobić. Uczenie odbywa się nie poprzez sztywno zakodowane instrukcje, ale poprzez wzorce, prawdopodobieństwa i uogólnienia.
![2](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/2.png)

*Rozpoznawanie pisma ręcznego i obrazów to tylko dwa przykłady zadań, w których niemożliwe jest przewidzenie wszystkich scenariuszy.*

Zależnie od swojego szkolenia, model ML może zobaczyć literę, której nigdy wcześniej nie spotkał, i nadal ją rozpoznać — na podstawie tysięcy podobnych próbek pisma ręcznego. Może określić, że użytkownik narysował dinozaura, nawet jeśli dokładnie takiej sylwetki nie było w danych treningowych — ponieważ rozumie kształty, proporcje i teksturę nie jako reguły, ale jako rozkłady. Zamiast sztywno podążać za z góry napisanym scenariuszem — zgaduje.

#### Paradygmaty uczenia maszynowego

To, co może zrobić model AI, w dużej mierze zależy od tego, jak został przeszkolony.

Przede wszystkim modele AI są klasyfikowane według ich paradygmatów uczenia. Paradygmat określa mocne i słabe strony modelu.

Większość metod uczenia maszynowego należy do jednej z czterech głównych paradygmatów:
*   Uczenie nadzorowane
*   Uczenie nienadzorowane
*   Uczenie ze wzmocnieniem
*   Uczenie samonadzorowane (czasami nazywane również „samouczeniem”)

#### Uczenie nadzorowane (Supervised Learning)
![3](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/3.png)

Jak nauczyć model odróżniać koty od psów na zdjęciach? Pokazujesz mu dziesiątki tysięcy obrazów — każdy z prawidłową etykietą: „To jest kot” lub „To jest pies”. Model zaczyna szukać wzorców: „Aha, koty mają trójkątne uszy, a psy — długie pyski”. Nie wie, co to jest kot czy pies, ale widzi, że niektóre obrazy są do siebie podobne, a inne nie. I z każdym nowym przykładem staje się coraz lepszy w rozpoznawaniu tych wzorców. Po tysiącach iteracji model zaczyna sam zauważać coś: koty mają trójkątne uszy, podejrzliwe spojrzenie i skłonność do solidnego siadania na klawiaturze. To jest uczenie nadzorowane — trening na oznaczonych przykładach, gdzie „prawidłowa” odpowiedź jest znana z góry.

Zasadniczo mówisz: „Oto dane wejściowe — a oto oczekiwany wynik”. Zadaniem modelu jest znalezienie wzorców i uogólnienie ich na nowe, niewidziane dane.

![4](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/4.png)

*Po tysiącu zdjęć kotów model zrozumiał istotę: trójkątne uszy są ważne. Teraz używa tego do odróżniania kotów od psów.*

**Typowe przypadki użycia:**
*   **Klasyfikacja** (np. spam vs. nie spam)
*   **Regresja** (np. prognozowanie cen)
*   **Estymacja prawdopodobieństwa** (np. prawdopodobieństwo rezygnacji klienta)

**Uczenie nadzorowane w świecie rzeczywistym:**
*   **Analiza sentymentu:** *Wejście:* tekst recenzji → *Wyjście:* pozytywny / negatywny
*   **Filtrowanie spamu:** *Wejście:* tekst e-maila → *Wyjście:* spam / nie spam
*   **Diagnostyka medyczna:** *Wejście:* wyniki badań → *Wyjście:* zdrowy / chory
*   **Moderacja treści:** *Wejście:* tekst lub obraz → *Wyjście:* dozwolone / narusza zasady
*   **Kategoryzacja produktów:** *Wejście:* opis produktu → *Wyjście:* kategoria katalogu
*   **OCR (Optyczne rozpoznawanie znaków):** *Wejście:* zdjęcie dokumentu → *Wyjście:* wyodrębniony tekst

#### Uczenie nienadzorowane (Unsupervised Learning)
![5](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/5.png)

*Czasami wydaje się, że dinozaury to po prostu zbyt pewne siebie żaby.*

W tym paradygmacie model uczy się na nieoznakowanych danych, co oznacza, że nigdy nie mówi mu się, która odpowiedź jest „prawidłowa”. Zamiast tego próbuje samodzielnie odkryć ukrytą strukturę, wzorce lub zależności. Pomyśl o tym jak o próbie uporządkowania chaosu w kategorie, gdy nikt nigdy nie powiedział Ci, jakie te kategorie powinny być.

Wyobraź sobie, że pokazujesz modelowi tysiące obrazów — kotów, psów, żab i dinozaurów (założymy, dla jasności, że w jakiś sposób uzyskaliśmy wyraźne zdjęcia wymarłych gadów). Ale nie mówimy modelowi, kto jest kim. W rzeczywistości model nawet nie wie, ile jest kategorii: trzy? pięć? pięćdziesiąt? Po prostu szuka wizualnych wzorców. W końcu zaczyna grupować futrzane stworzenia w jeden klaster, a te o gładkiej skórze, oczach po bokach i złowrogim, zimnym spojrzeniu — w inny.

![6](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/6.png)

Po tysiącach przykładów model ostatecznie decyduje: „Włóżmy wszystkie futrzane rzeczy do pudełka nr 1,
a wszystko z błyszczącą skórą i oczami po bokach — do pudełka nr 2”. Same etykiety nie mają znaczenia — ważne jest to,
że zawartość każdego pudełka staje się coraz bardziej jednorodna.

Modele nienadzorowane nie próbują przewidywać etykiet. Zamiast tego:
*   **Grupują podobne obiekty (klasteryzacja)**
*   **Wykrywają wartości odstające lub anomalie**
*   **Zmniejszają wymiarowość (upraszczają złożone dane)**

Ten paradygmat jest szczególnie przydatny, gdy:
*   Etykietowanie danych jest zbyt kosztowne lub niepraktyczne
*   Nie wiesz jeszcze, czego szukasz
*   Chcesz odkryć segmenty lub wzorce zachowań bez z góry określonych kategorii

#### Uczenie ze wzmocnieniem (Reinforcement Learning)

W tym paradygmacie model — nazywany agentem — uczy się, wchodząc w interakcje ze środowiskiem metodą prób i błędów. Agent próbuje różnych działań i obserwuje reakcję środowiska. Działania, które prowadzą do pożądanego rezultatu, przynoszą nagrody; nieefektywne lub szkodliwe działania prowadzą do kar.

Spróbujmy wytresować kota. (Tak, wiemy, że w prawdziwym życiu jest to prawie niemożliwe, ale już zajęliśmy się tematem kotów, więc jesteśmy.)
Kot to agent. Mieszkanie to środowisko. Kot próbuje różnych działań: Złapał muchę → dostał smakołyk (nagroda) Zrzucił telewizor → brak kolacji (kara)
Poprzez wielokrotne doświadczenia kot zaczyna zachowywać się w użyteczny sposób — nie dlatego, że rozumie, czego chcesz, ale dlatego, że nauczył się polityki: zestawu działań, które najczęściej prowadzą do jedzenia. Nie potrzebuje zasad — uczy się na konsekwencjach.

![7](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/7.png)

*Jak pokazuje wykres — krzykiem nic nie zdziałasz.)*

**Uczenie ze wzmocnieniem jest używane, gdy:**
*   Zachowanie musi poprawiać się w czasie
*   Nie ma z góry określonych „prawidłowych” odpowiedzi
*   Konsekwencje są opóźnione, a nie natychmiastowe

#### Uczenie samonadzorowane (Self-Supervised Learning)

W tym podejściu model uczy się na nieoznakowanych danych, ale zadanie do uczenia jest wyodrębniane z samych danych — bez udziału człowieka w oznaczaniu. Model uczy się przewidywać jedną część danych wejściowych na podstawie innej.

**Przykład**
Oryginalne zdanie: *„Kot wskoczył na klawiaturę i wgrał niedokończony kod na produkcję”.*

Możemy to przekształcić w zadanie do uczenia. Na przykład:
*   **Maskowanie słowa:** *wejście:* „Kot wskoczył na \*\*\* i wdrożył niedokończony kod...”, *cel:* przewidzieć słowo **klawiatura**.
*   **Przerwanie zdania:** *wejście:* „Kot wskoczył na...”, *cel:* kontynuować zdanie.

![8](../assets/Что_такое_машинное_обучение_и_как_оно_na_самом_деле_учится/8.png)

*Dla Kota Tensorowego pisanie do góry nogami to tylko kwestia wyboru odpowiedniego układu współrzędnych.*

Te pary „wejście + cel” są generowane automatycznie, bez ręcznego oznaczania. Ta sama idea ma zastosowanie do różnych typów danych, takich jak obrazy (przewidywanie brakujących fragmentów) lub audio.

**Rzeczywiste zastosowania uczenia samonadzorowanego:**
*   **Modele językowe** (GPT, LLaMA, Claude)
*   **Wizja komputerowa** (CLIP, DINO)
*   **Audio i mowa** (Wav2Vec 2.0)
*   **Modele multimodalne** (Gemini, CLIP)
*   **Wstępne szkolenie (modele fundamentalne)**

**Główna idea**
Model uczy się na automatycznie generowanych zadaniach, gdzie „prawidłowa odpowiedź” jest wyodrębniana bezpośrednio z samych danych. Daje nam to skalowalność, zdolność do uogólniania i podstawę dla większości współczesnych systemów generatywnych i językowych.

#### Podsumowanie paradygmatów uczenia

| Paradygmat                 | Jak uczy się model                                           |
|----------------------------|--------------------------------------------------------------|
| Uczenie nadzorowane        | Na oznaczonych danych (wejście → prawidłowa odpowiedź)       |
| Uczenie nienadzorowane     | Na nieoznaczonych danych (model sam znajduje strukturę)      |
| Uczenie ze wzmocnieniem   | Poprzez interakcję ze środowiskiem za pomocą nagród i kar    |
| Uczenie samonadzorowane    | Na nieoznaczonych danych, gdzie zadania są generowane z nich samych |

#### Co jeszcze istnieje?

Oprócz tych czterech, istnieją inne podejścia (częściowo nadzorowane, aktywne, uczenie online itp.). Rzadko są one uważane za niezależne paradygmaty, ponieważ zazwyczaj są hybrydami lub wariacjami głównych strategii, które już omówiliśmy. Aby zrozumieć istotę uczenia maszynowego — wystarczy opanować te cztery.

W następnej części zagłębimy się w to, czym tak naprawdę jest sieć neuronowa: neurony, wagi, połączenia. Jak się „uczy”? Po co jej w ogóle warstwy? I co ma wspólnego stos liczb z rozumieniem języka, obrazów czy... rzeczywistości?

Będziemy zdejmować warstwę po warstwie — i spróbujemy odpowiedzieć na jedyne pytanie, które ma znaczenie:

**Czy jest tu jakaś magia... czy to tylko przebrana matematyka?**

https://medium.com/@paul.ilvez/how-ai-learns-no-formulas-but-plenty-of-cats-fc43471add24
