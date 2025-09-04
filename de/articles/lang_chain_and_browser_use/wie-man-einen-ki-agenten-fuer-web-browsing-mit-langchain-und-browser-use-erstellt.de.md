## So erstellen Sie einen KI-Agenten für das Web-Browsing mit LangChain und Browser-Use: eine Schritt-für-Schritt-Anleitung

Diese Schritt-für-Schritt-Anleitung zeigt Ihnen, wie Sie einen KI-Agenten erstellen, der Informationen in Google suchen und Webseiten analysieren kann, indem Sie LangChain und Browser-Use verwenden.

**Schritt 1: Notwendige Bibliotheken installieren**

Zuerst müssen Sie die notwendigen Python-Bibliotheken installieren. Öffnen Sie ein Terminal oder eine Eingabeaufforderung und führen Sie den folgenden Befehl aus:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Schritt 2: API-Schlüssel konfigurieren**

API-Schlüssel sind erforderlich, um mit OpenAI und SerpAPI zu arbeiten.

* **OpenAI API-Schlüssel:** Holen Sie sich Ihren API-Schlüssel von der OpenAI-Website (openai.com).
* **SerpAPI API-Schlüssel:** SerpAPI bietet eine API für die Arbeit mit Suchergebnissen. Registrieren Sie sich auf der serpapi.com-Website (eine kostenlose Testversion ist verfügbar), melden Sie sich bei Ihrem Konto an und finden Sie Ihren API-Schlüssel auf der Dashboard-Seite.

Erstellen Sie eine `.env`-Datei im selben Verzeichnis, in dem sich Ihr Python-Skript befindet, und fügen Sie dort die Schlüssel im folgenden Format hinzu:

```
OPENAI_API_KEY=Ihr_openai_schlüssel
SERPAPI_API_KEY=Ihr_serpapi_schlüssel
```

**Schritt 3: Ein Python-Skript erstellen (browser_agent.py)**

Erstellen Sie die Datei `browser_agent.py` und fügen Sie den folgenden Code ein:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Protokollierung konfigurieren
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# API-Schlüssel aus der .env-Datei laden
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Sprachmodell initialisieren
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Sie können andere Modelle ausprobieren

    # Suchwerkzeug definieren (einfaches Beispiel, keine tatsächliche Google-Suche)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Suche Google: {query}",  # Bei Bedarf durch tatsächliche Suche mit SerpAPI ersetzen
        description="Sucht nach Informationen auf Google."
    )


    # Aufgabe für den Agenten definieren
    task = """
    Finden Sie die neuesten Nachrichten über OpenAI auf Google.
    Besuchen Sie dann eine der gefundenen Websites und finden Sie die Namen der Gründer.
    """

    # Agenten erstellen
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Agenten ausführen
    try:
        result = await agent.arun(task)
        print(f"Ergebnis: {result}")
    except Exception as e:
        logging.error(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Schritt 4: Agenten ausführen**

Öffnen Sie ein Terminal oder eine Eingabeaufforderung, navigieren Sie zum Verzeichnis mit der Datei `browser_agent.py` und führen Sie sie aus:

```bash
python browser_agent.py
```

**Schritt 5: Agenten verbessern (erweiterte Funktionen)**

* **Echte Google-Suche:** Ersetzen Sie die `lambda`-Funktion in `search_tool` durch Code, der SerpAPI für tatsächliche Google-Suchen verwendet. Dies erfordert das Studium der SerpAPI-Dokumentation.

* **Webseiten-Interaktion (Browser-Use):** Um die Funktionalität der Webseiten-Interaktion (Links öffnen, Text extrahieren usw.) hinzuzufügen, müssen Sie die `browser-use`-Bibliothek verwenden. Die Dokumentation dieser Bibliothek hilft Ihnen, die entsprechenden Tools zu Ihrem Agenten hinzuzufügen.

* **Speichernutzung:** Die Speichermechanismen von LangChain können verwendet werden, um den Kontext zwischen Anfragen zu erhalten.

* **Komplexere Aktionsketten:** LangChain ermöglicht es Ihnen, komplexere Aktionsketten zu erstellen, um komplexere Aufgaben zu lösen.


Dieses Beispiel demonstriert die grundlegende Struktur. Um einen vollwertigen Agenten zu implementieren, der mit einem Browser und Google Search interagiert, ist zusätzliche Arbeit mit SerpAPI und `browser-use` erforderlich. Vergessen Sie nicht, die Dokumentation dieser Bibliotheken für detailliertere Informationen zu konsultieren.
