### **Zyklus „NICHT Selenium“. Intro**

Diejenigen, die sich mit Web Scraping, Tests und Automatisierung beschäftigen, kennen Selenium, das modernere Playwright und/oder das Crawlee-Framework. Sie sind mächtig, sie können fast alles, und sie... werden nicht immer benötigt. Darüber hinaus ist in vielen Fällen die Verwendung dieser Tools wie das Einschlagen von Nägeln mit einem Mikroskop: Die Arbeit wird sicherlich erledigt, aber auf Kosten ungerechtfertigter Ausgaben – Geschwindigkeit, Systemressourcen und Konfigurationskomplexität.

Willkommen zum Artikelzyklus „NICHT Selenium“. Hier zeige ich andere (nicht immer offensichtliche) Wege, um mit Internetinhalten zu interagieren.

#### Paradigma Nr. 1: Direkte Kommunikation. HTTP-Clients

*   **`Requests`** — Formuliert und sendet eine Netzwerkanfrage an die Zieladresse (URL), genau wie Ihr Browser im ersten Moment des Seitenladens, aber ohne den Browser selbst. In diese Anfrage packt es die Methode (z. B. `GET`, um Daten abzurufen), Header (`Headers`), die sich der Website präsentieren (z. B. `User-Agent: „ich-bin-ein-browser“`), und andere Parameter. Als Antwort vom Server erhält es Rohdaten – meistens den ursprünglichen HTML-Code der Seite oder eine Zeichenkette im JSON-Format, sowie einen Statuscode (z. B. `200 OK`).

*   **`HTTPX`** — ist ein moderner Nachfolger von `Requests`. Auf einer fundamentalen Ebene tut es dasselbe: Es sendet dieselben HTTP-Anfragen mit denselben Headern und empfängt dieselben Antworten. Aber es gibt einen entscheidenden Unterschied: `Requests` arbeitet **synchron** – es sendet eine Anfrage, wartet auf eine Antwort, erhält eine Antwort, sendet die nächste. `HTTPX` hingegen kann **asynchron** arbeiten – es kann hundert Anfragen gleichzeitig „abfeuern“, ohne auf Antworten zu warten, und sie dann effizient verarbeiten, sobald sie eintreffen.

Sie eignen sich hervorragend zum Sammeln von Daten von statischen Websites, zum Arbeiten mit APIs und zum Parsen Tausender von Seiten, bei denen keine JavaScript-Ausführung erforderlich ist.

*   **Vorteile:** **Geschwindigkeit und Effizienz.** Dank der Asynchronität von `HTTPX` wird das, wofür `Requests` sequenziell 100 Anfragen mehrere Minuten benötigen würde, von `HTTPX` in wenigen Sekunden erledigt.
*   **Nachteile:** Nicht geeignet für Websites, bei denen Inhalte mit JavaScript generiert werden.

#### Paradigma Nr. 2: Chrome DevTools Protocol (CDP)

Was tun, wenn die Website dynamisch ist und Inhalte mit JavaScript generiert werden? Moderne Browser (Chrome, Chromium, Edge) verfügen über ein integriertes Protokoll zum Debuggen und Steuern – **Chrome DevTools Protocol (CDP)**. Es ermöglicht, Befehle direkt an den Browser zu senden, ohne die umständliche WebDriver-Schicht zu verwenden, die Selenium nutzt.

*   **Tools:** Der Hauptvertreter dieses Ansatzes ist heute `Pydoll`, das das einst beliebte, aber jetzt nicht mehr unterstützte `pyppeteer` ersetzt hat.
*   **Wann verwenden:** Wenn JavaScript-Rendering benötigt wird, aber eine hohe Geschwindigkeit beibehalten und Komplexitäten mit Treibern vermieden werden sollen.
*   **Vorteile:** **Balance.** Sie erhalten die Leistung eines echten Browsers, aber mit viel geringerem Overhead und oft mit integrierten Mechanismen zur Umgehung von Schutzmaßnahmen.
*   **Nachteile:** Kann schwieriger zu debuggen sein als Playwright und erfordert ein tieferes Verständnis der Browserfunktion.

#### Paradigma Nr. 3: Autonome LLM-Agenten

Dies ist die fortschrittlichste Grenze. Was wäre, wenn wir, anstatt Code zu schreiben, der sagt „hier klicken, das eingeben“, einfach eine Aufgabe in natürlicher Sprache geben? „Finde mir alle Lieferanten auf dieser Website und sammle ihre Produktkategorien“.

Genau diese Aufgabe lösen LLM-Agenten. Mithilfe eines „Gehirns“ in Form eines großen Sprachmodells (GPT, Gemini) und „Händen“ in Form einer Reihe von Tools (Browser, Google-Suche) können diese Agenten komplexe Aufgaben im Web selbstständig planen und ausführen.

*   **Tools:** Bundles wie `LangChain` + `Pydoll` oder benutzerdefinierte Lösungen, wie in `simple_browser.py`, die wir später analysieren werden.
*   **Wann verwenden:** Für komplexe Forschungsaufgaben, bei denen die Schritte im Voraus unbekannt sind und eine Echtzeit-Anpassung erforderlich ist.
*   **Vorteile:** **Intelligenz.** Die Fähigkeit, unstrukturierte Probleme zu lösen und sich im Handumdrehen an Änderungen anzupassen.
*   **Nachteile:** „Nicht-Determinismus“ (Ergebnisse können von Ausführung zu Ausführung variieren), Kosten für API-Aufrufe an LLM, geringere Geschwindigkeit im Vergleich zu direktem Code.

#### Paradigma Nr. 4: Code-freies Scraping

Manchmal ist die Aufgabe so einfach, dass das Schreiben von Code überflüssig ist. Müssen Sie schnell eine Tabelle von einer Seite abrufen? Dafür gibt es elegante Lösungen, die keine Programmierung erfordern.

*   **Tools:** Google Sheets-Funktionen (`IMPORTXML`, `IMPORTHTML`), Browser-Erweiterungen.
*   **Wann verwenden:** Für einmalige Aufgaben, schnelles Prototyping oder wenn Sie einfach keinen Code schreiben möchten.
*   **Vorteile:** **Einfachheit.** Geöffnet, angegeben, was gesammelt werden soll – Ergebnis erhalten.
*   **Nachteile:** Eingeschränkte Funktionalität, nicht geeignet für komplexe Aufgaben oder große Datenmengen.

### Was kommt als Nächstes?

Dieser Artikel ist nur eine Einführung. In den nächsten Ausgaben unseres „NICHT Selenium“-Zyklus werden wir von der Theorie zur harten Praxis übergehen. Wir werden tief in jedes dieser Paradigmen eintauchen und zeigen, wie sie mit realen Beispielen funktionieren:

*   Wir werden **Pydoll** analysieren und sehen, wie es Cloudflare umgeht.
*   Wir werden einen Kampf zwischen **JavaScript und Python** um den Titel der besten Sprache für Scraping veranstalten.
*   Wir werden lernen, wie man mit **lxml** die maximale Geschwindigkeit beim Parsen herausholt.
*   Wir werden ein Skript schreiben, das Daten von **Amazon** sammelt und in **Excel** speichert.
*   Wir werden zeigen, wie **Google Sheets** Ihr erster Scraper werden kann.
*   Und natürlich werden wir detailliert analysieren, wie man einen **autonomen LLM-Agenten** zur Steuerung des Browsers erstellt und verwendet.

Bereiten Sie sich darauf vor, Ihre Sichtweise auf Automatisierung und Datenerfassung im Web zu ändern. Es wird schnell, effizient und sehr interessant. Abonnieren Sie
