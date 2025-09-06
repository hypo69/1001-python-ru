### **Zyklus "NICHT Selenium". Intro**

Diejenigen, die sich mit Web-Scraping, Tests und Automatisierung beschäftigen, kennen Selenium, das modernere Playwright und/oder das Crawlee-Framework. Sie sind mächtig, sie können fast alles, und sie... werden nicht immer benötigt. Darüber hinaus ist in vielen Fällen die Verwendung dieser Tools wie das Einschlagen von Nägeln mit einem Mikroskop: Die Arbeit wird sicherlich erledigt, aber auf Kosten ungerechtfertigter Ausgaben – Geschwindigkeit, Systemressourcen und Konfigurationskomplexität.

Willkommen im Artikelzyklus "NICHT Selenium". Hier zeige ich andere (nicht immer offensichtliche) Wege, um mit Internetinhalten zu interagieren.

#### Paradigma Nr. 1: Direkte Kommunikation. HTTP-Clients

*   **`Requests`** — Formuliert und sendet eine Netzwerkanfrage an die Zieladresse (URL), genau wie Ihr Browser im allerersten Moment des Seitenladens, aber ohne den Browser selbst. In dieser Anfrage werden die Methode (z. B. `GET` zum Abrufen von Daten), Header (`Headers`), die sich der Website präsentieren (z. B. `User-Agent: "ich-bin-ein-browser"`), und andere Parameter verpackt. Als Antwort vom Server erhält es Rohdaten — meistens ist es der ursprüngliche HTML-Code der Seite oder eine Zeichenfolge im JSON-Format, sowie ein Statuscode (z. B. `200 OK`).

*   **`HTTPX`** — ist ein moderner Nachfolger von `Requests`. Auf einer fundamentalen Ebene tut es dasselbe: sendet dieselben HTTP-Anfragen mit denselben Headern und empfängt dieselben Antworten. Aber es gibt einen entscheidenden Unterschied: `Requests` arbeitet **synchron** — es sendet eine Anfrage, wartet auf eine Antwort, erhält eine Antwort, sendet die nächste. `HTTPX` hingegen kann **asynchron** arbeiten — es kann "abfeuern" hundert Anfragen gleichzeitig, ohne auf Antworten zu warten, und diese dann effizient verarbeiten, sobald sie eintreffen.

Sie eignen sich hervorragend zum Sammeln von Daten von statischen Websites, zum Arbeiten mit APIs und zum Parsen von Tausenden von Seiten, bei denen keine JavaScript-Ausführung erforderlich ist.

*   **Vorteile:** **Geschwindigkeit und Effizienz.** Dank der asynchronen Natur von `HTTPX` wird `HTTPX` in wenigen Sekunden erledigt sein, wo `Requests` sequenziell 100 Anfragen über mehrere Minuten hinweg ausführen würde.
*   **Nachteile:** Nicht geeignet für Websites, bei denen der Inhalt mit JavaScript generiert wird.

#### Paradigma Nr. 2: Chrome DevTools Protocol (CDP)

Was tun, wenn die Website dynamisch ist und der Inhalt mit JavaScript generiert wird? Moderne Browser (Chrome, Chromium, Edge) verfügen über ein integriertes Protokoll zum Debuggen und Steuern – **Chrome DevTools Protocol (CDP)**. Es ermöglicht das direkte Senden von Befehlen an den Browser, wodurch die umständliche WebDriver-Schicht, die Selenium verwendet, umgangen wird.

*   **Tools:** Der Hauptvertreter dieses Ansatzes ist heute `Pydoll`, das das einst beliebte, aber jetzt nicht mehr unterstützte `pyppeteer` ersetzt hat.</li>
*   **Wann verwenden:** Wenn JavaScript-Rendering benötigt wird, aber eine hohe Geschwindigkeit beibehalten und Komplexität mit Treibern vermieden werden soll.</li>
*   **Vorteile:** **Balance.** Sie erhalten die Leistung eines echten Browsers, aber mit viel geringerem Overhead und oft mit integrierten Schutzumgehungsmechanismen.</li>
*   **Nachteile:** Kann schwieriger zu debuggen sein als Playwright und erfordert ein tieferes Verständnis der Browserfunktion.</li>
</ul>
<h4>Paradigma Nr. 3: Autonome LLM-Agenten</h4>
<p>Dies ist die Speerspitze. Was wäre, wenn wir, anstatt Code zu schreiben, der "hier klicken, dies eingeben" sagt, einfach eine Aufgabe in natürlicher Sprache geben würden? "Finden Sie alle Lieferanten auf dieser Website und sammeln Sie deren Produktkategorien."</p>
<p>Genau dieses Problem lösen LLM-Agenten. Mit einem "Gehirn" in Form eines großen Sprachmodells (GPT, Gemini) und "Händen" in Form eines Satzes von Tools (Browser, Google-Suche) können diese Agenten komplexe Aufgaben im Web selbstständig planen und ausführen.</p>
<ul>
<li><strong>Tools:</strong> Bundles wie `LangChain` + `Pydoll` oder benutzerdefinierte Lösungen, wie in `simple_browser.py`, die wir später analysieren werden.</li>
<li><strong>Wann verwenden:</strong> Für komplexe Forschungsaufgaben, bei denen die Schritte im Voraus unbekannt sind und eine Echtzeit-Anpassung erforderlich ist.</li>
<li><strong>Vorteile:</strong> **Intelligenz.** Die Fähigkeit, unstrukturierte Probleme zu lösen und sich im Handumdrehen an Änderungen anzupassen.</li>
<li><strong>Nachteile:</strong> "Nicht-Determinismus" (Ergebnisse können von Lauf zu Lauf variieren), Kosten für API-Aufrufe an LLM, geringere Geschwindigkeit im Vergleich zu direktem Code.</li>
</ul>
<h4>Paradigma Nr. 4: Code-freies Scraping</h4>
<p>Manchmal ist die Aufgabe so einfach, dass das Schreiben von Code überflüssig ist. Müssen Sie schnell eine Tabelle von einer Seite ziehen? Dafür gibt es elegante Lösungen, die keine Programmierung erfordern.</p>
<ul>
<li><strong>Tools:</strong> Google Sheets-Funktionen (`IMPORTXML`, `IMPORTHTML`), Browser-Erweiterungen.</li>
<li><strong>Wann verwenden:</strong> Für einmalige Aufgaben, schnelles Prototyping oder wenn Sie einfach keinen Code schreiben möchten.</li>
<li><strong>Vorteile:</strong> **Einfachheit.** Geöffnet, angegeben, was gesammelt werden soll – Ergebnis erhalten.</li>
<li><strong>Nachteile:</strong> Begrenzte Funktionalität, nicht geeignet für komplexe Aufgaben oder große Datenmengen.</li>
</ul>
<h3>Was kommt als Nächstes?</h3>
<p>Dieser Artikel ist nur eine Einführung. In den nächsten Ausgaben unserer "NICHT Selenium"-Reihe werden wir von der Theorie zur harten Praxis übergehen. Wir werden tief in jedes dieser Paradigmen eintauchen und zeigen, wie sie mit realen Beispielen funktionieren:</p>
<ul>
<li>Wir werden <strong>Pydoll</strong> analysieren und sehen, wie es Cloudflare umgeht.</li>
<li>Wir werden einen Kampf zwischen <strong>JavaScript vs. Python</strong> um den Titel der besten Sprache für Web-Scraping veranstalten.</li>
<li>Wir werden lernen, wie man mit <strong>lxml</strong> die maximale Geschwindigkeit beim Parsen herausholt.</li>
<li>Wir werden ein Skript schreiben, das Daten von <strong>Amazon</strong> sammelt und in <strong>Excel</strong> speichert.</li>
<li>Wir werden zeigen, wie <strong>Google Sheets</strong> Ihr erster Scraper werden kann.</li>
<li>Und natürlich werden wir detailliert analysieren, wie man einen <strong>autonomen LLM-Agenten</strong> zur Steuerung des Browsers erstellt und verwendet.</li>
</ul>
<p>Machen Sie sich bereit, Ihre Sichtweise auf Automatisierung und Datenerfassung im Web zu ändern. Es wird schnell, effizient und sehr interessant. Abonnieren Sie</p>
