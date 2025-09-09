### **Cykl „NIE Selenium”. Wprowadzenie**

Ci, którzy zajmują się web scrapingiem, testowaniem i automatyzacją, znają Selenium, bardziej nowoczesny Playwright i/lub framework Crawlee. Są potężne, potrafią prawie wszystko, i... nie zawsze są potrzebne. Co więcej, w wielu przypadkach użycie tych narzędzi to jak wbijanie gwoździ mikroskopem: praca oczywiście zostanie wykonana, ale kosztem nieuzasadnionych wydatków — szybkości, zasobów systemowych i złożoności konfiguracji.

Witajcie w cyklu artykułów „NIE Selenium”. Tutaj pokażę inne (nie zawsze oczywiste) sposoby interakcji z zawartością internetu.

#### Paradygmat nr 1: Bezpośrednia komunikacja. Klienci HTTP

*   **`Requests`** — Formuje i wysyła żądanie sieciowe do docelowego adresu (URL), dokładnie tak, jak robi to Twoja przeglądarka w pierwszej chwili ładowania strony, ale bez samej przeglądarki. W tym żądaniu pakuje metodę (np. `GET`, aby pobrać dane), nagłówki (`Headers`), które przedstawiają się witrynie (np. `User-Agent: „jestem-przeglądarką”`), i inne parametry. W odpowiedzi od serwera otrzymuje surowe dane — najczęściej jest to oryginalny kod HTML strony lub ciąg znaków w formacie JSON, a także kod statusu (np. `200 OK`).

*   **`HTTPX`** — to nowoczesny następca `Requests`. Na poziomie fundamentalnym robi to samo: wysyła te same żądania HTTP z tymi samymi nagłówkami i odbiera te same odpowiedzi. Ale jest kluczowa różnica: `Requests` działa **synchronicznie** — wysyła żądanie, siedzi i czeka na odpowiedź, otrzymuje odpowiedź, wysyła następne. `HTTPX` natomiast potrafi działać **asynchronicznie** — może „wystrzelić” od razu sto żądań, nie czekając na odpowiedzi, a następnie efektywnie je przetwarzać w miarę ich napływania.

Doskonale nadają się do zbierania danych ze stron statycznych, pracy z API, parsowania tysięcy stron, gdzie nie jest wymagane wykonywanie JavaScriptu.

*   **Zalety:** **Szybkość i wydajność.** Dzięki asynchroniczności `HTTPX`, tam gdzie `Requests` sekwencyjnie wykonałby 100 żądań w ciągu kilku minut, `HTTPX` poradzi sobie w kilka sekund.
*   **Wady:** Nie nadają się do stron, gdzie treść jest generowana za pomocą JavaScriptu.

#### Paradygmat nr 2: Protokół Chrome DevTools (CDP)

Co zrobić, jeśli strona jest dynamiczna, a treść jest generowana za pomocą JavaScriptu? Nowoczesne przeglądarki (Chrome, Chromium, Edge) mają wbudowany protokół do debugowania i sterowania — **Chrome DevTools Protocol (CDP)**. Pozwala on na bezpośrednie wydawanie poleceń przeglądarce, omijając uciążliwą warstwę WebDriver, której używa Selenium.

*   **Narzędzia:** Głównym przedstawicielem tego podejścia jest obecnie `Pydoll`, który zastąpił niegdyś popularny, ale obecnie nieobsługiwany `pyppeteer`.
*   **Kiedy używać:** Gdy potrzebne jest renderowanie JavaScriptu, ale chce się zachować wysoką prędkość i uniknąć komplikacji z sterownikami.
*   **Zalety:** **Równowaga.** Otrzymujesz moc prawdziwej przeglądarki, ale ze znacznie mniejszym narzutem i często z wbudowanymi mechanizmami omijania zabezpieczeń.
*   **Wady:** Może być trudniejszy w debugowaniu niż Playwright i wymaga głębszego zrozumienia działania przeglądarki.

#### Paradygmat nr 3: Autonomiczne agenty LLM

To najbardziej zaawansowana granica. Co jeśli zamiast pisać kod, który mówi „kliknij tutaj, wpisz to”, po prostu podamy zadanie w języku naturalnym? „Znajdź mi wszystkich dostawców na tej stronie i zbierz ich kategorie produktów”.

Właśnie to zadanie rozwiązują agenci LLM. Wykorzystując „mózg” w postaci dużego modelu językowego (GPT, Gemini) i „ręce” w postaci zestawu narzędzi (przeglądarka, wyszukiwarka Google), agenci ci mogą samodzielnie planować i wykonywać złożone zadania w sieci.

*   **Narzędzia:** Pakiety takie jak `LangChain` + `Pydoll` lub niestandardowe rozwiązania, jak w `simple_browser.py`, które omówimy później.
*   **Kiedy używać:** Do złożonych zadań badawczych, gdzie kroki są nieznane z góry i wymagana jest adaptacja w czasie rzeczywistym.
*   **Zalety:** **Inteligencja.** Zdolność do rozwiązywania nieustrukturyzowanych problemów i adaptacji do zmian w locie.
*   **Wady:** „Niedeterminizm” (wyniki mogą się różnić w zależności od uruchomienia), koszt wywołań API do LLM, niższa prędkość w porównaniu z bezpośrednim kodem.

#### Paradygmat nr 4: Scraping bez kodu

Czasami zadanie jest tak proste, że pisanie kodu jest zbędne. Potrzebujesz szybko wyciągnąć tabelę z jednej strony? Do tego istnieją eleganckie rozwiązania, które nie wymagają programowania.

*   **Narzędzia:** Funkcje Google Sheets (`IMPORTXML`, `IMPORTHTML`), rozszerzenia przeglądarki.
*   **Kiedy używać:** Do jednorazowych zadań, szybkiego prototypowania lub gdy po prostu nie chcesz pisać kodu.
*   **Zalety:** **Prostota.** Otworzyłeś, określiłeś, co zebrać — otrzymałeś wynik.
*   **Wady:** Ograniczona funkcjonalność, nie nadają się do złożonych zadań lub dużych ilości danych.

### Co dalej?

Ten artykuł to tylko wprowadzenie. W kolejnych numerach naszego cyklu „NIE Selenium” przejdziemy od teorii do twardej praktyki. Zagłębimy się w każdy z tych paradygmatów i pokażemy, jak działają na rzeczywistych przykładach:

*   Przeanalizujemy **Pydoll** i zobaczymy, jak omija Cloudflare.
*   Urządzimy bitwę **JavaScript kontra Python** o tytuł najlepszego języka do scrapingu.
*   Nauczymy się wyciskać maksymalną prędkość z parsowania za pomocą **lxml**.
*   Napiszemy skrypt, który zbiera dane z **Amazon** i zapisuje je w **Excelu**.
*   Pokażemy, jak **Google Sheets** może stać się Twoim pierwszym scraperem.
*   I, oczywiście, szczegółowo omówimy, jak stworzyć i używać **autonomicznego agenta LLM** do sterowania przeglądarką.

Przygotuj się na zmianę swojego spojrzenia na automatyzację i zbieranie danych w sieci. Będzie szybko, efektywnie i bardzo interesująco. Subskrybuj
