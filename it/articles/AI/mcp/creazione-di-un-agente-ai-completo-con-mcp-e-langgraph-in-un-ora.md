# Come insegnare a una rete neurale a lavorare con le mani: creazione di un agente AI completo con MCP e LangGraph in un'ora

Amici, saluti! Spero che mi siate mancati.

Negli ultimi due mesi, mi sono immerso profondamente nella ricerca sull'integrazione degli agenti AI nei miei progetti Python. Nel processo, ho accumulato molte conoscenze pratiche e osservazioni che sarebbe un peccato non condividere. Quindi oggi torno su Habr — con un nuovo argomento, una prospettiva fresca e l'intenzione di scrivere più spesso.

All'ordine del giorno ci sono LangGraph e MCP: strumenti con cui è possibile creare agenti AI davvero utili.

Se prima discutevamo su quale rete neurale rispondesse meglio in russo, oggi il campo di battaglia si è spostato verso compiti più applicati: chi gestisce meglio il ruolo di un agente AI? Quali framework semplificano realmente lo sviluppo? E come integrare tutto questo in un progetto reale?

Ma prima di immergerci nella pratica e nel codice, chiariamo i concetti di base. Soprattutto due concetti chiave: **agenti AI e MCP**. Senza di essi, la conversazione su LangGraph sarebbe incompleta.

### Agenti AI in termini semplici

Gli agenti AI non sono solo chatbot "potenziati". Rappresentano entità più complesse e autonome che possiedono due caratteristiche cruciali:

1.  **Capacità di interagire e coordinarsi**

    Gli agenti moderni possono suddividere i compiti in sottocompiti, chiamare altri agenti, richiedere dati esterni, lavorare in squadra. Questo non è più un assistente solitario, ma un sistema distribuito in cui ogni componente può contribuire.

2.  **Accesso a risorse esterne**

    Un agente AI non è più limitato dai confini di un dialogo. Può accedere a database, effettuare chiamate API, interagire con file locali, basi di conoscenza vettoriali e persino eseguire comandi nel terminale. Tutto ciò è stato possibile grazie all'emergere di MCP — un nuovo livello di integrazione tra il modello e l'ambiente.

---

In parole semplici: **MCP è un ponte tra una rete neurale e il suo ambiente**. Permette al modello di "comprendere" il contesto del compito, accedere ai dati, effettuare chiamate e formare azioni ragionate, piuttosto che limitarsi a produrre risposte testuali.

**Immaginiamo un'analogia:**

*   Hai una **rete neurale** — può ragionare e generare testi.
*   Ci sono **dati e strumenti** — documenti, API, basi di conoscenza, terminale, codice.
*   E c'è **MCP** — è un'interfaccia che consente al modello di interagire con queste fonti esterne come se fossero parte del suo mondo interno.

**Senza MCP:**

Il modello — è un motore di dialogo isolato. Gli dai del testo — risponde. E basta.

**Con MCP:**

Il modello diventa un **esecutore di compiti** a tutti gli effetti:

*   ottiene l'accesso a strutture dati e API;
*   chiama funzioni esterne;
*   naviga nello stato attuale del progetto o dell'applicazione;
*   può ricordare, tracciare e modificare il contesto man mano che il dialogo procede;
*   utilizza estensioni come strumenti di ricerca, code runner, database di embedding vettoriali, ecc.

In senso tecnico, **MCP è un protocollo di interazione tra un LLM e il suo ambiente**, dove il contesto è fornito come oggetti strutturati (invece di testo "grezzo"), e le chiamate sono formattate come operazioni interattive (ad esempio, chiamata di funzione, utilizzo di strumenti o azioni dell'agente). Questo è ciò che trasforma un modello ordinario in un **vero agente AI**, capace di fare più che semplicemente "parlare".

### E ora — al lavoro!

Ora che abbiamo trattato i concetti di base, è logico chiedersi: "Come implementiamo tutto questo in pratica in Python?"

Qui entra in gioco **LangGraph** — un potente framework per la costruzione di grafi di stato, comportamenti degli agenti e catene di pensiero. Ti consente di "cucire insieme" la logica di interazione tra agenti, strumenti e utente, creando un'architettura AI vivente che si adatta ai compiti.

Nelle sezioni seguenti, vedremo come:

*   costruire un agente da zero;
*   creare stati, transizioni ed eventi;
*   integrare funzioni e strumenti;
*   e come tutto questo ecosistema funziona in un progetto reale.

### Un po' di teoria: cos'è LangGraph

Prima di immergerci nella pratica, qualche parola sul framework stesso.

**LangGraph** — è un progetto del team **LangChain**, gli stessi che per primi hanno proposto il concetto di "catene" (chains) di interazione con gli LLM. Se prima l'attenzione principale era sui pipeline lineari o a ramificazione condizionale (langchain.chains), ora gli sviluppatori puntano su un **modello a grafo**, e LangGraph è ciò che raccomandano come il nuovo "cuore" per la costruzione di sistemi AI complessi.

**LangGraph** — è un framework per la costruzione di macchine a stati finiti e grafi di stato, in cui ogni **nodo** rappresenta una parte della logica dell'agente: una chiamata di modello, uno strumento esterno, una condizione, un input utente, ecc.

### Come funziona: grafi e nodi

Concettualmente, LangGraph si basa sulle seguenti idee:

*   **Grafo** — è una struttura che descrive i possibili percorsi di esecuzione della logica. Puoi pensarla come una mappa: da un punto puoi passare a un altro a seconda delle condizioni o del risultato dell'esecuzione.
*   **Nodi** — sono passaggi specifici all'interno del grafo. Ogni nodo esegue una funzione: chiama un modello, chiama un'API esterna, controlla una condizione o semplicemente aggiorna lo stato interno.
*   **Transizioni tra i nodi** — è la logica di routing: se il risultato del passaggio precedente è tale, allora vai lì.
*   **Stato** — viene passato tra i nodi e accumula tutto ciò che è necessario: cronologia, conclusioni intermedie, input utente, risultati delle operazioni degli strumenti, ecc.

In questo modo, otteniamo un **meccanismo flessibile per il controllo della logica dell'agente**, in cui possono essere descritti scenari semplici e molto complessi: cicli, condizioni, azioni parallele, chiamate annidate e molto altro.

### Perché è conveniente?

LangGraph ti consente di costruire una **logica trasparente, riproducibile ed estensibile**:

*   facile da debuggare;
*   facile da visualizzare;
*   facile da scalare per nuovi compiti;
*   facile da integrare strumenti esterni e protocolli MCP.

In sostanza, LangGraph è il **"cervello" dell'agente**, dove ogni passaggio è documentato, controllabile e può essere modificato senza caos e "magia".

### E ora — basta teoria!

Potremmo parlare a lungo di grafi, stati, composizione logica e dei vantaggi di LangGraph rispetto ai pipeline classici. Ma, come dimostra la pratica, è meglio vederlo una volta nel codice.

**È ora di passare alla pratica.** Successivamente — un esempio in Python: creeremo un agente AI semplice ma utile basato su LangGraph che utilizzerà strumenti esterni, memoria e prenderà le proprie decisioni.

### Preparazione: reti neurali cloud e locali

Per iniziare a creare agenti AI, abbiamo prima bisogno di un **cervello** — un modello linguistico. Ci sono due approcci qui:

*   **utilizzare soluzioni cloud**, dove tutto è pronto "out of the box";
*   o **sollevare il modello localmente** — per una completa autonomia e riservatezza.

Consideriamo entrambe le opzioni.

#### Servizi cloud: veloci e convenienti

Il modo più semplice è utilizzare la potenza dei grandi fornitori: OpenAI, Anthropic, e utilizzare...

### Dove ottenere chiavi e token:

*   **OpenAI** — ChatGPT e altri prodotti;
*   **Anthropic** — Claude;
*   **OpenRouter.ai** — decine di modelli (un token — molti modelli tramite un'API compatibile con OpenAI);
*   **Amvera Cloud** — possibilità di connettere LLAMA con pagamento in rubli e proxy integrato a OpenAI e Anthropic.

Questo percorso è conveniente, soprattutto se:

*   non vuoi configurare l'infrastruttura;
*   sviluppi con un focus sulla velocità;
*   lavori con risorse limitate.

### Modelli locali: controllo totale

Se la **privacy, il lavoro offline** sono importanti per te, o vuoi costruire **agenti completamente autonomi**, allora ha senso distribuire la rete neurale localmente.

**Principali vantaggi:**

*   **Riservatezza** — i dati rimangono con te;
*   **Lavoro offline** — utile in reti isolate;
*   **Nessun abbonamento e token** — gratuito dopo la configurazione.

**Gli svantaggi sono evidenti:**

*   Requisiti di risorse (in particolare per la memoria video);
*   La configurazione può richiedere tempo;
*   Alcuni modelli sono difficili da distribuire senza esperienza.

Ciononostante, ci sono strumenti che semplificano l'avvio locale. Uno dei migliori oggi è **Ollama**.

### Distribuzione di un LLM locale tramite Ollama + Docker

Prepareremo una distribuzione locale del modello Qwen 2.5 (qwen2.5:32b) utilizzando un contenitore Docker e il sistema Ollama. Ciò consentirà di integrare la rete neurale con MCP e di utilizzarla nei propri agenti basati su LangGraph.

Se le risorse di calcolo del tuo computer o server non sono sufficienti per lavorare con questa versione del modello, puoi sempre scegliere una rete neurale meno "affamata" di risorse — il processo di installazione e avvio rimarrà simile.

**Installazione rapida (riepilogo dei passaggi)**

1.  **Installa Docker + Docker Compose**
2.  **Crea la struttura del progetto:**
```bash
mkdir qwen-local && cd qwen-local
```
3.  **Crea `docker-compose.yml`**
(opzione universale, GPU rilevata automaticamente)

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama_qwen
    ports:
      - "11434:11434"
    volumes:
      - ./ollama_data:/root/.ollama
      - /tmp:/tmp
    environment:
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_ORIGINS=*
    restart: unless-stopped
```

4.  **Avvia il contenitore:**
```bash
docker compose up -d
```

5.  **Scarica il modello:**
```bash
docker exec -it ollama_qwen ollama pull qwen2.5:32b
```

6.  **Verifica il funzionamento dell'API:**
```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5:32b", "prompt": "Ciao!", "stream": false}'
```
*(Immagine con il risultato dell'esecuzione del comando curl)*

7.  **Integrazione con Python:**
```python
import requests

def query(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:32b",
        "prompt": prompt,
        "stream": False
    })
    return res.json()['response']

print(query("Spiega l'entanglement quantistico"))
```
Ora hai un LLM locale completo, pronto a lavorare con MCP e LangGraph.

**Cosa c'è dopo?**

Abbiamo la possibilità di scegliere tra modelli cloud e locali, e abbiamo imparato come connetterli entrambi. La parte più interessante è in arrivo — **la creazione di agenti AI su LangGraph**, che utilizzano il modello selezionato, la memoria, gli strumenti e la propria logica.

**Passiamo alla parte più gustosa — codice e pratica!**

---

Prima di passare alla pratica, è importante preparare l'ambiente di lavoro. Presumo che tu abbia già familiarità con le basi di Python, sappia cosa sono le librerie e le dipendenze e capisca perché usare un ambiente virtuale.

Se tutto questo è nuovo per te — ti consiglio di seguire prima un breve corso o una guida sulle basi di Python, e poi di tornare all'articolo.

#### Passaggio 1: Creazione di un ambiente virtuale

Crea un nuovo ambiente virtuale nella cartella del progetto:
```bash
python -m venv venv
source venv/bin/activate  # per Linux/macOS
virtualenv\Scripts\activate   # per Windows
```

#### Passaggio 2: Installazione delle dipendenze

Crea un file `requirements.txt` e aggiungi le seguenti righe:
```
langchain==0.3.26
langchain-core==0.3.69
langchain-deepseek==0.1.3
langchain-mcp-adapters==0.1.9
langchain-ollama==0.3.5
langchain-openai==0.3.28
langgraph==0.5.3
langgraph-checkpoint==2.1.1
langgraph-prebuilt==0.5.2
langgraph-sdk==0.1.73
langsmith==0.4.8
mcp==1.12.0
ollama==0.5.1
openai==1.97.0
```

> ⚠️ **Le versioni attuali sono del 21 luglio 2025.** Potrebbero essere cambiate dalla pubblicazione — **verifica la pertinenza prima dell'installazione.**

Quindi installa le dipendenze:
```bash
pip install -r requirements.txt```

#### Passaggio 3: Configurazione delle variabili d'ambiente

Crea un file `.env` nella radice del progetto e aggiungi le chiavi API necessarie:
```
OPENAI_API_KEY=sk-proj-1234
DEEPSEEK_API_KEY=sk-123
OPENROUTER_API_KEY=sk-or-v1-123
BRAVE_API_KEY=BSAj123K1bvBGpH1344tLwc
```

**Scopo delle variabili:**

*   **OPENAI_API_KEY** — chiave per l'accesso ai modelli GPT di OpenAI;
*   **DEEPSEEK_API_KEY** — chiave per l'utilizzo dei modelli Deepseek;
*   **OPENROUTER_API_KEY** — chiave unica per l'accesso a molti modelli tramite OpenRouter

---
Alcuni strumenti MCP (ad esempio, `brave-web-search`) richiedono una chiave per funzionare. Senza di essa, semplicemente non si attiveranno.

**E se non hai chiavi API?**

Nessun problema. Puoi iniziare lo sviluppo con un modello locale (ad esempio, tramite Ollama), senza connettere alcun servizio esterno. In questo caso, non è necessario creare il file `.env`.

Fatto! Ora abbiamo tutto il necessario per iniziare — un ambiente isolato, dipendenze e, se necessario, accesso a reti neurali cloud e integrazioni MCP.

Successivamente, eseguiremo il nostro agente LLM in diversi modi.

### Avvio semplice degli agenti LLM tramite LangGraph: integrazione di base

Cominciamo con il più semplice: come "collegare il cervello" al futuro agente. Analizzeremo i modi di base per avviare i modelli linguistici (LLM) utilizzando LangChain, in modo che nel passaggio successivo possiamo passare all'integrazione con LangGraph e alla costruzione di un agente AI completo.

#### Importazioni
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_deepseek import ChatDeepSeek
```
*   `os` e `load_dotenv()` — per caricare le variabili dal file `.env`.
*   `ChatOpenAI`, `ChatOllama`, `ChatDeepSeek` — wrapper per connettere i modelli linguistici tramite LangChain.

> 💡 Se utilizzi approcci alternativi per lavorare con le configurazioni (ad esempio, Pydantic Settings), puoi sostituire `load_dotenv()` con il tuo metodo abituale.

#### Caricamento delle variabili d'ambiente
```python
load_dotenv()
```
Questo caricherà tutte le variabili da `.env`, incluse le chiavi per l'accesso alle API OpenAI, DeepSeek, OpenRouter e altre.

#### Funzioni semplici per ottenere LLM

**OpenAI**
```python
def get_openai_llm():
    return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
```
Se la variabile `OPENAI_API_KEY` è impostata correttamente, LangChain la sostituirà automaticamente — l'indicazione esplicita `api_key=...` qui è facoltativa.

**DeepSeek**
```python
def get_deepseek_llm():
    # ...
```
Analogamente, ma usiamo il wrapper `ChatDeepSeek`.

**OpenRouter (e altre API compatibili)**
```python
def get_openrouter_llm(model="moonshotai/kimi-k2:free"):
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )
```
**Caratteristiche:**

*   `ChatOpenAI` viene utilizzato, anche se il modello non proviene da OpenAI — perché OpenRouter utilizza lo stesso protocollo.
*   `base_url` è obbligatorio: punta all'API OpenRouter.
*   Il modello `moonshotai/kimi-k2:free` è stato scelto come una delle opzioni più bilanciate in termini di qualità e velocità al momento della stesura.
*   La chiave API `OpenRouter` deve essere passata esplicitamente — la sostituzione automatica non funziona qui.

#### Mini-test: verifica del funzionamento del modello
```python
if __name__ == "__main__":
    llm = get_openrouter_llm(model="moonshotai/kimi-k2:free")
    response = llm.invoke("Chi sei?")
    print(response.content)
```
*(Immagine con il risultato dell'esecuzione: `Sono un assistente AI creato da Moonshot AI...`)*

Se tutto è configurato correttamente, riceverai una risposta significativa dal modello. Congratulazioni — il primo passo è fatto!

### Ma questo non è ancora un agente

Nella fase attuale, abbiamo collegato LLM e fatto una semplice chiamata. Questo assomiglia più a un chatbot da console che a un agente AI.

**Perché?**

*   Scriviamo **codice sincrono, lineare** senza logica di stato o obiettivi.
*   L'agente non prende decisioni, non ricorda il contesto e non usa strumenti.
*   MCP e LangGraph non sono ancora coinvolti.

**Cosa c'è dopo?**

Successivamente, implementeremo un **agente AI completo** utilizzando **LangGraph** — prima senza MCP, per concentrarci sull'architettura, gli stati e la logica dell'agente stesso.

Immergiamoci nella vera meccanica degli agenti. Andiamo!

### Agente di classificazione delle offerte di lavoro: dalla teoria alla pratica

...concetti di LangGraph in pratica e creare uno strumento utile per le piattaforme HR e gli scambi freelance.

#### Compito dell'agente

Il nostro agente prende in input una descrizione testuale di un'offerta di lavoro o di un servizio ed esegue una classificazione a tre livelli:

1.  **Tipo di lavoro**: lavoro a progetto o posizione permanente
2.  **Categoria professionale**: da oltre 45 specialità predefinite
3.  **Tipo di ricerca**: se una persona cerca lavoro o cerca un esecutore

Il risultato viene restituito in formato JSON strutturato con un punteggio di confidenza per ogni classificazione.

#### 📈 Architettura dell'agente su LangGraph

Seguendo i principi di LangGraph, creiamo un **grafo di stati** di quattro nodi:

- Descrizione di input
- ↓
- Nodo di classificazione del tipo di lavoro
- ↓
- Nodo di classificazione della categoria
- ↓
- Nodo di determinazione del tipo di ricerca
- ↓
- Nodo di calcolo della confidenza
- ↓
- Risultato JSON

Ogni nodo è una **funzione specializzata** che:

*   Riceve lo stato attuale dell'agente
*   Esegue la sua parte di analisi
*   Aggiorna lo stato e lo passa

#### Gestione dello stato

Definisci la **struttura della memoria dell'agente** tramite `TypedDict`:

```python
from typing import TypedDict, Dict

class State(TypedDict):
    """Stato dell'agente per memorizzare le informazioni sul processo di classificazione"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool
```

Questa è la **memoria di lavoro dell'agente** — tutto ciò che ricorda e accumula durante l'analisi. Simile a come un esperto umano tiene a mente il contesto del compito durante l'analisi di un documento.

Vediamo il codice completo, e poi ci concentriamo sui punti principali.

```python
import asyncio
import json
from enum import Enum
from typing import TypedDict, Dict, Any, List

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Categorie professionali
CATEGORIES = [
    "Animatore 2D", "Animatore 3D", "Modellatore 3D",
    "Analista aziendale", "Sviluppatore Blockchain", ...
]

class JobType(Enum):
    PROJECT = "lavoro a progetto"
    PERMANENT = "lavoro permanente"

class SearchType(Enum):
    LOOKING_FOR_WORK = "cerca lavoro"
    LOOKING_FOR_PERFORMER = "cerca un esecutore"

class State(TypedDict):
    """Stato dell'agente per memorizzare le informazioni sul processo di classificazione"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool
```

class VacancyClassificationAgent:
    """Agente asincrono per la classificazione di offerte di lavoro e servizi"""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        """Inizializzazione dell'agente"""
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.workflow = self._create_workflow()

    def _create_workflow(self) -> StateGraph:
        """Crea il flusso di lavoro dell'agente basato su LangGraph"""
        workflow = StateGraph(State)
        
        # Aggiungi nodi al grafo
        workflow.add_node("job_type_classification", self._classify_job_type)
        workflow.add_node("category_classification", self._classify_category)
        workflow.add_node("search_type_classification", self._classify_search_type)
        workflow.add_node("confidence_calculation", self._calculate_confidence)
        
        # Definisci la sequenza di esecuzione dei nodi
        workflow.set_entry_point("job_type_classification")
        workflow.add_edge("job_type_classification", "category_classification")
        workflow.add_edge("category_classification", "search_type_classification")
        workflow.add_edge("search_type_classification", "confidence_calculation")
        workflow.add_edge("confidence_calculation", END)
        
        return workflow.compile()

    async def _classify_job_type(self, state: State) -> Dict[str, Any]:
        """Nodo per determinare il tipo di lavoro: a progetto o permanente"""
        # ... (l'implementazione segue)
        
    async def _classify_category(self, state: State) -> Dict[str, Any]:
        """Nodo per determinare la categoria professionale"""
        # ... (l'implementazione segue)
        
    async def _classify_search_type(self, state: State) -> Dict[str, Any]:
        """Nodo per determinare il tipo di ricerca"""
        # ... (l'implementazione segue)

    async def _calculate_confidence(self, state: State) -> Dict[str, Any]:
        """Nodo per calcolare il livello di confidenza nella classificazione"""
        # ... (l'implementazione segue)

    def _find_closest_category(self, predicted_category: str) -> str:
        """Trova la categoria più vicina dall'elenco di quelle disponibili"""
        # ... (l'implementazione segue)

    async def classify(self, description: str) -> Dict[str, Any]:
        """Metodo principale per classificare offerte di lavoro/servizi"""
        initial_state = {
            "description": description,
            "job_type": "",
            "category": "",
            "search_type": "",
            "confidence_scores": {},
            "processed": False
        }
        
        # Avvia il flusso di lavoro
        result = await self.workflow.ainvoke(initial_state)
        
        # Forma la risposta JSON finale
        classification_result = {
            "job_type": result["job_type"],
            "category": result["category"],
            "search_type": result["search_type"],
            "confidence_scores": result["confidence_scores"],
            "success": result["processed"]
        }
        return classification_result

async def main():
    """Dimostrazione del funzionamento dell'agente"""
    agent = VacancyClassificationAgent()
    
    test_cases = [
        "Sviluppatore Python richiesto per creare un\'applicazione web su Django. Lavoro permanente.",
        "Cerca ordini per creare loghi e identità aziendale. Lavoro in Adobe Illustrator.",
        "Necessario animatore 3D per un progetto a breve termine per creare uno spot pubblicitario.",
        "Curriculum: marketer esperto, cerca lavoro remoto nel marketing digitale",
        "Cerca uno sviluppatore frontend React per il nostro team a tempo indeterminato"
    ]
    
    print("🤖 Dimostrazione del funzionamento dell\'agente di classificazione delle offerte di lavoro\n")
    for i, description in enumerate(test_cases, 1):
        print(f"--- Test {i}: ---")
        print(f"Descrizione: {description}")
        try:
            result = await agent.classify(description)
            print("Risultato della classificazione:")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"❌ Errore: {e}")
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())

```
*(...il resto del codice con l'implementazione dei metodi è stato presentato nell'articolo...)*

### Vantaggi chiave dell'architettura
1.  **Modularità** — ogni nodo risolve un compito, facile da testare e migliorare separatamente
2.  **Estensibilità** — nuovi nodi di analisi possono essere aggiunti senza modificare quelli esistenti
3.  **Trasparenza** — l'intero processo decisionale è documentato e tracciabile
4.  **Prestazioni** — elaborazione asincrona di più richieste
5.  **Affidabilità** — meccanismi di fallback e gestione degli errori integrati

### Benefici reali
Un tale agente può essere utilizzato in:
*   **Piattaforme HR** per la categorizzazione automatica di curriculum e offerte di lavoro
*   **Scambi freelance** per migliorare la ricerca e i consigli
*   **Sistemi interni** delle aziende per l'elaborazione di richieste e progetti
*   **Soluzioni analitiche** per la ricerca sul mercato del lavoro

### MCP in azione: creazione di un agente con file system e ricerca web
Dopo aver compreso i principi di base di LangGraph e aver creato un semplice agente classificatore, estendiamo le sue capacità collegandolo al mondo esterno tramite MCP.

Ora creeremo un assistente AI completo che potrà:
*   Lavorare con il file system (leggere, creare, modificare file)
*   Cercare informazioni pertinenti su Internet
*   Memorizzare il contesto del dialogo
*   Gestire gli errori e recuperare da guasti

#### Dalla teoria agli strumenti reali
Ricordi come all'inizio dell'articolo abbiamo parlato di **MCP come ponte tra una rete neurale e il suo ambiente**? Ora lo vedrai in pratica. Il nostro agente avrà accesso a **strumenti reali**:
```
# Strumenti del file system
- read_file — leggere file
- write_file — scrivere e creare file
- list_directory — visualizzare il contenuto delle cartelle
- create_directory — creare cartelle

# Strumenti di ricerca web
- brave_web_search — cercare su Internet
- get_web_content — ottenere il contenuto delle pagine
```
Questo non è più un agente "giocattolo" — è uno **strumento di lavoro** che può risolvere problemi reali.

#### 📈 Architettura: dal semplice al complesso

**1. Configurazione come base della stabilità**
```python
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Configurazione semplificata dell'agente AI"""
    filesystem_path: str = "/path/to/work/directory"
    model_provider: ModelProvider = ModelProvider.OLLAMA
    use_memory: bool = True
    enable_web_search: bool = True

    def validate(self) -> None:
        """Validazione della configurazione"""
        if not os.path.exists(self.filesystem_path):
            raise ValueError(f"Il percorso non esiste: {self.filesystem_path}")
```
**Perché è importante?** A differenza dell'esempio di classificazione, qui l'agente interagisce con sistemi esterni. Un errore nel percorso del file o una chiave API mancante — e l'intero agente smette di funzionare. La **validazione all'avvio** consente di risparmiare ore di debug.

**2. Fabbrica di modelli: scelta flessibile**
```python
def create_model(config: AgentConfig):
    """Crea un modello in base alla configurazione"""
    provider = config.model_provider.value
    if provider == "ollama":
        return ChatOllama(model="qwen2.5:32b", base_url="http://localhost:11434")
    elif provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    # ... altri provider
```
Un codice — molti modelli. Vuoi un modello locale gratuito? Usa Ollama. Hai bisogno della massima precisione? Passa a GPT-4. La velocità è importante? Prova DeepSeek. Il codice rimane lo stesso.

**3. Integrazione MCP: connessione al mondo reale**
```python
async def _init_mcp_client(self):
    """Inizializzazione del client MCP"""
    mcp_config = {
        "filesystem": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", self.filesystem_path],
            "transport": "stdio"
        },
        "brave-search": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search@latest"],
            "transport": "stdio",
            "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
        }
    }
    self.mcp_client = MultiServerMCPClient(mcp_config)
    self.tools = await self.mcp_client.get_tools()
```
Qui, il lavoro chiave di MCP si verifica: colleghiamo server MCP esterni all'agente, che forniscono un set di strumenti e funzioni. L'agente riceve quindi non solo funzioni individuali, ma una comprensione contestuale completa di come lavorare con il file system e Internet.

#### Resilienza agli errori
Nel mondo reale, tutto si rompe: la rete non è disponibile, i file sono bloccati, le chiavi API sono scadute. Il nostro agente è pronto per questo:
```python
@retry_on_failure(max_retries=2, delay=1.0)
async def process_message(self, user_input: str, thread_id: str = "default") -> str:
    # ...
```
Il decoratore `@retry_on_failure` riprova automaticamente le operazioni in caso di guasti temporanei. L'utente non si accorgerà nemmeno che qualcosa è andato storto.

### Risultati: dalla teoria alla pratica degli agenti AI

Oggi siamo passati dai concetti di base alla creazione di agenti AI funzionanti. Riassumiamo ciò che abbiamo imparato e raggiunto.

**Cosa abbiamo imparato**

**1. Concetti fondamentali**
*   Compreso la differenza tra chatbot e veri agenti AI
*   Compreso il ruolo di **MCP (Model Context Protocol)** come ponte tra il modello e il mondo esterno
*   Studiato l'architettura di **LangGraph** per la costruzione di logiche di agente complesse

**2. Competenze pratiche**
*   Configurato un ambiente di lavoro con supporto per modelli cloud e locali
*   Creato un **agente classificatore** con architettura asincrona e gestione dello stato
*   Costruito un **agente MCP** con accesso al file system e alla ricerca web

**3. Pattern architetturali**
*   Padroneggiato la configurazione modulare e le fabbriche di modelli
*   Implementato la gestione degli errori e i **meccanismi di retry** per soluzioni pronte per la produzione

### Vantaggi chiave dell'approccio
**LangGraph + MCP** ci offrono:
*   **Trasparenza** — ogni passaggio dell'agente è documentato e tracciabile
*   **Estensibilità** — nuove funzionalità vengono aggiunte in modo dichiarativo
*   **Affidabilità** — gestione degli errori e recupero integrati
*   **Flessibilità** — supporto per più modelli e provider out of the box

### Conclusione

Gli agenti AI non sono una finzione futuristica, ma una **tecnologia reale di oggi**. Con LangGraph e MCP, possiamo creare sistemi che risolvono problemi aziendali specifici, automatizzano le routine e aprono nuove possibilità.

**La cosa principale è iniziare.** Prendi il codice dagli esempi, adattalo ai tuoi compiti, sperimenta. Ogni progetto è una nuova esperienza e un passo verso la maestria nel campo dello sviluppo AI.

Buona fortuna con i tuoi progetti!

---
*Tag: python, ai, mcp, langchain, assistente ai, ollama, agenti ai, llm locale, langgraph, mcp-server*
*Hub: Blog dell'azienda Amvera, Elaborazione del linguaggio naturale, Intelligenza artificiale, Python, Programmazione*