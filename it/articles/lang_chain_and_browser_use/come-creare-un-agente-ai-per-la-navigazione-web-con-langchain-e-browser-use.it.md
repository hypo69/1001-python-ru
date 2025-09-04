## Come creare un agente AI per la navigazione web con LangChain e Browser-Use: una guida passo-passo

Questa guida passo-passo ti mostrerà come creare un agente AI in grado di cercare informazioni su Google e analizzare pagine web utilizzando LangChain e Browser-Use.

**Passaggio 1: Installare le librerie necessarie**

Per prima cosa, devi installare le librerie Python necessarie. Apri un terminale o un prompt dei comandi ed esegui il seguente comando:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Passaggio 2: Configurare le chiavi API**

Le chiavi API sono necessarie per lavorare con OpenAI e SerpAPI.

* **Chiave API OpenAI:** Ottieni la tua chiave API dal sito web di OpenAI (openai.com).
* **Chiave API SerpAPI:** SerpAPI fornisce un'API per lavorare con i risultati di ricerca. Registrati sul sito web serpapi.com (è disponibile una versione di prova gratuita), accedi al tuo account e trova la tua chiave API nella pagina della Dashboard.

Crea un file `.env` nella stessa directory in cui si troverà il tuo script Python e aggiungi le chiavi lì nel seguente formato:

```
OPENAI_API_KEY=la_tua_chiave_openai
SERPAPI_API_KEY=la_tua_chiave_serpapi
```

**Passaggio 3: Creare uno script Python (browser_agent.py)**

Crea il file `browser_agent.py` e inserisci il seguente codice al suo interno:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Configura la registrazione
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Carica le chiavi API dal file .env
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Inizializza il modello linguistico
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Puoi provare altri modelli

    # Definisci lo strumento di ricerca (esempio semplice, nessuna ricerca Google effettiva)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Ricerca Google: {query}",  # Sostituisci con la ricerca effettiva usando SerpAPI se necessario
        description="Cerca informazioni su Google."
    )


    # Definisci il compito per l'agente
    task = """
    Trova le ultime notizie su OpenAI su Google.
    Quindi visita uno dei siti web trovati e trova i nomi dei fondatori.
    """

    # Crea l'agente
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Esegui l'agente
    try:
        result = await agent.arun(task)
        print(f"Risultato: {result}")
    except Exception as e:
        logging.error(f"Si è verificato un errore: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Passaggio 4: Esegui l'agente**

Apri un terminale o un prompt dei comandi, naviga nella directory con il file `browser_agent.py` ed eseguilo:

```bash
python browser_agent.py
```

**Passaggio 5: Migliora l'agente (funzionalità avanzate)**

* **Ricerca Google reale:** Sostituisci la funzione `lambda` in `search_tool` con codice che utilizza SerpAPI per ricerche Google effettive. Ciò richiederà lo studio della documentazione di SerpAPI.

* **Interazione con le pagine web (Browser-Use):** Per aggiungere funzionalità di interazione con le pagine web (apertura di link, estrazione di testo, ecc.), dovrai utilizzare la libreria `browser-use`. La documentazione di questa libreria ti aiuterà ad aggiungere gli strumenti appropriati al tuo agente.

* **Utilizzo della memoria:** I meccanismi di memoria di LangChain possono essere utilizzati per preservare il contesto tra le richieste.

* **Catene di azioni più complesse:** LangChain ti consente di creare catene di azioni più complesse per risolvere compiti più complessi.


Questo esempio dimostra la struttura di base. Per implementare un agente completo che interagisce con un browser e Google Search, sarà necessario un lavoro aggiuntivo con SerpAPI e `browser-use`. Non dimenticare di consultare la documentazione di queste librerie per informazioni più dettagliate.
