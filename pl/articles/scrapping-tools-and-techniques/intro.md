### **Cykl "NIE Selenium". Wprowadzenie**

Ci, którzy zajmują się web scrapingiem, testowaniem i automatyzacją, znają Selenium, bardziej nowoczesny Playwright i/lub framework Crawlee. Są potężne, potrafią prawie wszystko, i one... nie zawsze są potrzebne. Co więcej, w wielu przypadkach użycie tych narzędzi jest jak wbijanie gwoździ mikroskopem: praca oczywiście zostanie wykonana, ale kosztem nieuzasadnionych wydatków – szybkości, zasobów systemowych i złożoności konfiguracji.

Witamy w cyklu artykułów "NIE Selenium". Tutaj pokażę inne (nie zawsze oczywiste) sposoby interakcji z zawartością internetu.

#### Paradygmat #1: Bezpośrednia komunikacja. Klienci HTTP

*   **`Requests`** — Formuje i wysyła żądanie sieciowe na adres docelowy (URL), dokładnie tak, jak robi to Twoja przeglądarka w pierwszej chwili ładowania strony, ale bez samej przeglądarki. W tym żądaniu pakuje metodę (np. `GET`, aby pobrać dane), nagłówki (`Headers`), które przedstawiają się stronie (np. `User-Agent: "jestem-przeglądarką"`), i inne parametry. W odpowiedzi od serwera otrzymuje surowe dane — najczęściej jest to oryginalny kod HTML strony lub ciąg znaków w formacie JSON, a także kod statusu (np. `200 OK`).

*   **`HTTPX`** — to nowoczesny następca `Requests`. Na fundamentalnym poziomie robi to samo: wysyła te same żądania HTTP z tymi samymi nagłówkami i odbiera te same odpowiedzi. Ale jest kluczowa różnica: `Requests` działa **synchronicznie** — wysłał żądanie, siedzi i czeka na odpowiedź, otrzymał odpowiedź, wysłał następne. `HTTPX` natomiast potrafi działać **asynchronicznie** — może "wystrzelić" od razu sto żądań, nie czekając na odpowiedzi, a następnie efektywnie je przetwarzać w miarę ich napływania.

Doskonale nadają się do zbierania danych ze stron statycznych, pracy z API, parsowania tysięcy stron, gdzie nie jest wymagane wykonywanie JavaScript.

*   **Zalety:** **Szybkość i wydajność.** Dzięki asynchronicznej naturze `HTTPX`, tam gdzie `Requests` będzie sekwencyjnie wykona 100 żądań w ciągu kilku minut, `HTTPX` poradzi sobie w kilka sekund.
*   **Wady:** Nie nadają się do stron, gdzie zawartość jest generowana za pomocą JavaScript.

#### Paradygmat #2: Protokół Chrome DevTools (CDP)

Co zrobić, jeśli strona jest dynamiczna, a zawartość jest generowana za pomocą JavaScript? Nowoczesne przeglądarki (Chrome, Chromium, Edge) posiadają wbudowany protokół do debugowania i kontroli — **Chrome DevTools Protocol (CDP)**. Pozwala on na bezpośrednie wydawanie poleceń przeglądarce, omijając nieporęczną warstwę WebDriver, której używa Selenium.

*   **Narzędzia:** Głównym przedstawicielem tego podejścia jest obecnie `Pydoll`, który zastąpił niegdyś popularny, ale obecnie nieobsługiwany `pyppeteer`.</li>
*   **Kiedy używać:** Gdy potrzebne jest renderowanie JavaScript, ale chcesz zachować wysoką prędkość i uniknąć komplikacji z sterownikami.</li>
*   **Zalety:** **Równowaga.** Otrzymujesz moc prawdziwej przeglądarki, ale ze znacznie mniejszym narzutem i często z wbudowanymi mechanizmami omijania zabezpieczeń.</li>
*   **Wady:** Może być trudniejszy w debugowaniu niż Playwright i wymaga głębszego zrozumienia działania przeglądarki.</li>
</ul>
<h4>Paradygmat #3: Autonomiczne agenty LLM</h4>
<p>To jest najnowocześniejsza granica. Co jeśli zamiast pisać kod, który mówi "kliknij tutaj, wpisz to", po prostu damy zadanie w języku naturalnym? "Znajdź mi wszystkich dostawców na tej stronie i zbierz ich kategorie produktów".</p>
<p>To właśnie problem, który rozwiązują agenty LLM. Wykorzystując "mózg" w postaci dużego modelu językowego (GPT, Gemini) i "ręce" w postaci zestawu narzędzi (przeglądarka, wyszukiwarka Google), agenty te mogą samodzielnie planować i wykonywać złożone zadania w sieci.</p>
<ul>
<li><strong>Narzędzia:</strong> Zestawy takie jak `LangChain` + `Pydoll` lub niestandardowe rozwiązania, jak w `simple_browser.py`, które przeanalizujemy później.</li>
<li><strong>Kiedy używać:</strong> Do złożonych zadań badawczych, gdzie kroki są nieznane z góry i wymagana jest adaptacja w czasie rzeczywistym.</li>
<li><strong>Zalety:</strong> **Inteligencja.** Zdolność do rozwiązywania nieustrukturyzowanych problemów i adaptacji do zmian w locie.</li>
<li><strong>Wady:</strong> "Niedeterminizm" (wyniki mogą się różnić w zależności od uruchomienia), koszt wywołań API do LLM, niższa prędkość w porównaniu do bezpośredniego kodu.</li>
</ul>
<h4>Paradygmat #4: Scraping bez kodu</h4>
<p>Czasami zadanie jest tak proste, że pisanie kodu jest zbędne. Potrzebujesz szybko wyciągnąć tabelę z jednej strony? Do tego istnieją eleganckie rozwiązania, które nie wymagają programowania.</p>
<ul>
<li><strong>Narzędzia:</strong> Funkcje Google Sheets (<code>IMPORTXML</code>, <code>IMPORTHTML</code>), rozszerzenia przeglądarki.</li>
<li><strong>Kiedy używać:</strong> Do jednorazowych zadań, szybkiego prototypowania lub gdy po prostu nie chcesz pisać kodu.</li>
<li><strong>Zalety:</strong> **Prostota.** Otworzyłeś, określiłeś, co zebrać — otrzymałeś wynik.</li>
<li><strong>Wady:</strong> Ograniczona funkcjonalność, nie nadają się do złożonych zadań ani dużych ilości danych.</li>
</ul>
<h3>Co dalej?</h3>
<p>Ten artykuł to tylko wprowadzenie. W kolejnych wydaniach naszego cyklu "NIE Selenium" przejdziemy od teorii do twardej praktyki. Zagłębimy się w każdy z tych paradygmatów i pokażemy, jak działają na rzeczywistych przykładach:</p>
<ul>
<li>Przeanalizujemy <strong>Pydoll</strong> i zobaczymy, jak omija Cloudflare.</li>
<li>Zorganizujemy bitwę <strong>JavaScript kontra Python</strong> o tytuł najlepszego języka do web scrapingu.</li>
<li>Nauczymy się wyciskać maksymalną prędkość z parsowania za pomocą <strong>lxml</strong>.</li>
<li>Napiszemy skrypt, który zbiera dane z <strong>Amazon</strong> i zapisuje je w <strong>Excelu</strong>.</li>
<li>Pokażemy, jak <strong>Google Sheets</strong> może stać się Twoim pierwszym scraperem.</li>
<li>I, oczywiście, szczegółowo przeanalizujemy, jak stworzyć i używać <strong>autonomicznego agenta LLM</strong> do kontrolowania przeglądarki.</li>
</ul>
<p>Przygotuj się na zmianę swojego spojrzenia na automatyzację i zbieranie danych w sieci. Będzie szybko, efektywnie i bardzo interesująco. Subskrybuj</p>
