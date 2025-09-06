### **Ciclo "NON Selenium". Introduzione**

Coloro che si occupano di web scraping, test e automazione hanno familiarità con Selenium, il più moderno Playwright e/o il framework Crawlee. Sono potenti, possono fare quasi tutto, e... non sono sempre necessari. Inoltre, in molti casi, l'utilizzo di questi strumenti è come piantare chiodi con un microscopio: il lavoro sarà certamente fatto, ma a costo di spese ingiustificate – velocità, risorse di sistema e complessità di configurazione.

Benvenuti nel ciclo di articoli "NON Selenium". Qui vi mostrerò altri modi (non sempre ovvi) per interagire con il contenuto di Internet.

#### Paradigma #1: Comunicazione diretta. Client HTTP

*   **`Requests`** — Forma e invia una richiesta di rete all'indirizzo di destinazione (URL), esattamente come fa il tuo browser nel primissimo momento del caricamento della pagina, ma senza il browser stesso. In questa richiesta, impacchetta il metodo (ad esempio, `GET` per recuperare dati), le intestazioni (`Headers`) che si presentano al sito (ad esempio, `User-Agent: "sono-un-browser"`), e altri parametri. In risposta dal server, riceve dati grezzi — il più delle volte, è il codice HTML originale della pagina o una stringa in formato JSON, così come un codice di stato (ad esempio, `200 OK`).

*   **`HTTPX`** — è un successore moderno di `Requests`. A livello fondamentale, fa la stessa cosa: invia le stesse richieste HTTP con le stesse intestazioni e riceve le stesse risposte. Ma c'è una differenza chiave: `Requests` funziona **sincronamente** — invia una richiesta, si siede e aspetta una risposta, riceve una risposta, invia la successiva. `HTTPX`, d'altra parte, può funzionare **asincronamente** — può "sparare" cento richieste contemporaneamente senza aspettare risposte, e poi elaborarle efficientemente man mano che arrivano.

Sono eccellenti per raccogliere dati da siti statici, lavorare con API, analizzare migliaia di pagine dove l'esecuzione di JavaScript non è richiesta.

*   **Vantaggi:** **Velocità ed efficienza.** Grazie alla natura asincrona di `HTTPX`, dove `Requests` farebbe sequenzialmente 100 richieste per diversi minuti, `HTTPX` lo gestirà in pochi secondi.
*   **Svantaggi:** Non adatti per siti in cui il contenuto è generato tramite JavaScript.

#### Paradigma #2: Protocollo Chrome DevTools (CDP)

Cosa fare se il sito è dinamico e il contenuto è generato tramite JavaScript? I browser moderni (Chrome, Chromium, Edge) hanno un protocollo integrato per il debug e il controllo — **Chrome DevTools Protocol (CDP)**. Permette di inviare comandi direttamente al browser, bypassando lo strato ingombrante di WebDriver che Selenium utilizza.

*   **Strumenti:** Il principale rappresentante di questo approccio oggi è `Pydoll`, che ha sostituito il `pyppeteer`, un tempo popolare ma ora non più supportato.
*   **Quando usarlo:** Quando è necessario il rendering JavaScript, ma si desidera mantenere un'alta velocità ed evitare le complessità con i driver.
*   **Vantaggi:** **Equilibrio.** Ottieni la potenza di un browser reale, ma con un overhead molto inferiore e spesso con meccanismi integrati per aggirare le protezioni.
*   **Svantaggi:** Può essere più difficile da debuggare rispetto a Playwright e richiede una comprensione più profonda del funzionamento del browser.

#### Paradigma #3: Agenti LLM autonomi

Questo è il confine più avanzato. E se invece di scrivere codice che dice "clicca qui, digita questo", dessimo semplicemente un compito in linguaggio naturale? "Trova tutti i fornitori su questo sito e raccogli le loro categorie di prodotti".

Questo è esattamente il problema che gli agenti LLM risolvono. Utilizzando un "cervello" sotto forma di un grande modello linguistico (GPT, Gemini) e "mani" sotto forma di un set di strumenti (browser, ricerca Google), questi agenti possono pianificare ed eseguire autonomamente compiti complessi sul web.

*   **Strumenti:** Bundle come `LangChain` + `Pydoll` o soluzioni personalizzate, come in `simple_browser.py`, che analizzeremo in seguito.
*   **Quando usarlo:** Per compiti di ricerca complessi in cui i passaggi sono sconosciuti in anticipo e è richiesta l'adattamento in tempo reale.
*   **Vantaggi:** **Intelligenza.** La capacità di risolvere problemi non strutturati e di adattarsi ai cambiamenti al volo.
*   **Svantaggi:** "Non determinismo" (i risultati possono variare da un'esecuzione all'altra), costo delle chiamate API a LLM, velocità inferiore rispetto al codice diretto.

#### Paradigma #4: Scraping senza codice

A volte il compito è così semplice che scrivere codice è eccessivo. Hai bisogno di estrarre rapidamente una tabella da una pagina? Per questo esistono soluzioni eleganti che non richiedono programmazione.

*   **Strumenti:** Funzioni Google Sheets (`IMPORTXML`, `IMPORTHTML`), estensioni del browser.
*   **Quando usarlo:** Per compiti una tantum, prototipazione rapida o quando semplicemente non vuoi scrivere codice.
*   **Vantaggi:** **Semplicità.** Aperto, specificato cosa raccogliere — ottenuto il risultato.
*   **Svantaggi:** Funzionalità limitata, non adatti per compiti complessi o grandi volumi di dati.

### Cosa c'è dopo?

Questo articolo è solo un'introduzione. Nei prossimi numeri della nostra serie "NON Selenium", passeremo dalla teoria alla pratica. Approfondiremo ciascuno di questi paradigmi e mostreremo come funzionano con esempi reali:

*   Analizzeremo **Pydoll** e vedremo come aggira Cloudflare.
*   Organizzeremo una battaglia tra **JavaScript vs Python** per il titolo del miglior linguaggio per il web scraping.
*   Impareremo a spremere la massima velocità dal parsing con **lxml**.
*   Scriveremo uno script che raccoglie dati da **Amazon** e li salva in **Excel**.
*   Mostreremo come **Google Sheets** può diventare il tuo primo scraper.
*   E, naturalmente, analizzeremo in dettaglio come creare e utilizzare un **agente LLM autonomo** per controllare il browser.

Preparati a cambiare la tua visione sull'automazione e la raccolta dati sul web. Sarà veloce, efficiente e molto interessante. Iscriviti
