## Wie man einen KI-Agenten für das Web-Browsing mit LangChain und Browser-Use erstellt: eine Schritt-für-Schritt-Anleitung

Diese Schritt-für-Schritt-Anleitung zeigt Ihnen, wie Sie einen KI-Agenten erstellen, der in der Lage ist, Informationen in Google zu suchen und Webseiten zu analysieren, indem er LangChain und Browser-Use verwendet.

**Schritt 1: Notwendige Bibliotheken installieren**

Zuerst müssen Sie die notwendigen Python-Bibliotheken installieren. Öffnen Sie ein Terminal oder eine Eingabeaufforderung und führen Sie den folgenden Befehl aus:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Schritt 2: API-Schlüssel konfigurieren**

Für die Arbeit mit OpenAI und SerpAPI sind API-Schlüssel erforderlich.

*   **OpenAI API-Schlüssel:** Holen Sie sich Ihren API-Schlüssel auf der OpenAI-Website (openai.com).
*   **SerpAPI API-Schlüssel:** SerpAPI bietet eine API für die Arbeit mit Suchergebnissen. Registrieren Sie sich auf serpapi.com (eine kostenlose Testversion ist verfügbar), melden Sie sich bei Ihrem Konto an und finden Sie Ihren API-Schlüssel auf der Dashboard-Seite.

Erstellen Sie eine `.env`-Datei im selben Verzeichnis, in dem sich Ihr Python-Skript befindet, und fügen Sie die Schlüssel im folgenden Format hinzu:

```
OPENAI_API_KEY=Ihr_openai_schlüssel
SERPAPI_API_KEY=Ihr_serpapi_schlüssel
```

**Schritt 3: Ein Python-Skript erstellen (browser_agent.py)**

Erstellen Sie eine Datei `browser_agent.py` und fügen Sie den folgenden Code ein:

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
        description="Sucht Informationen in Google."
    )


    # Aufgabe für den Agenten definieren
    task = """
    Finden Sie die neuesten Nachrichten über das Unternehmen OpenAI in Google.
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

Öffnen Sie ein Terminal oder eine Eingabeaufforderung, navigieren Sie zu dem Verzeichnis mit der Datei `browser_agent.py` und führen Sie sie aus:

```bash
python browser_agent.py
```

**Schritt 5: Agenten verbessern (erweiterte Funktionen)**

*   **Echte Google-Suche:** Ersetzen Sie die `lambda`-Funktion in `search_tool` durch Code, der SerpAPI für eine echte Google-Suche verwendet. Dies erfordert das Studium der SerpAPI-Dokumentation.

*   **Webseiten-Interaktion (Browser-Use):** Um die Funktionalität der Webseiten-Interaktion (Öffnen von Links, Extrahieren von Text usw.) hinzuzufügen, müssen Sie die `browser-use`-Bibliothek verwenden. Die Dokumentation dieser Bibliothek hilft Ihnen, die entsprechenden Tools zu Ihrem Agenten hinzuzufügen.

*   **Speichernutzung:** Um den Kontext zwischen Anfragen zu erhalten, können Sie die Speichermechanismen von LangChain verwenden.

*   **Komplexere Aktionsketten:** LangChain ermöglicht die Erstellung komplexerer Aktionsketten (Chains), um komplexere Probleme zu lösen.


Dieses Beispiel demonstriert die grundlegende Struktur. Um einen vollwertigen Agenten zu implementieren, der mit dem Browser und der Google-Suche interagiert, ist zusätzliche Arbeit mit SerpAPI und `browser-use` erforderlich. Vergessen Sie nicht, die Dokumentation dieser Bibliotheken für detailliertere Informationen zu konsultieren.
