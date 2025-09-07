## Foglio illustrativo. Personalizzazione LLM: prompt, ottimizzazione dei modelli, esempi di codice.

In questo articolo:

1. Come viene creato l'"effetto memoria" in LLM (breve panoramica).
2. Perché e quando è necessaria l'ottimizzazione (Fine-tuning) di un modello.
3. Quando l'ottimizzazione non è la soluzione migliore.
4. Preparazione dei dati.
5. Esempi di ottimizzazione per **OpenAI (GPT)**, **Google (Gemini)** e **Anthropic (Claude)** (differisce).

### 1. Come LLM "ricorda" e "si adatta": L'illusione del contesto

Prima di discutere l'ottimizzazione, è importante capire come LLM riesca a creare un senso di personalizzazione.
Questo è importante per non affrettarsi a un'ottimizzazione costosa se il compito può essere risolto con metodi più semplici:

* Tramite la **Finestra di Contesto (Memoria a Breve Termine):** All'interno di un singolo dialogo, si invia al modello non solo una nuova domanda, ma anche **tutta o parte della conversazione precedente**. Il modello elabora tutto questo testo come un unico "contesto". È grazie a questo che "ricorda" le osservazioni precedenti e continua il pensiero. La limitazione qui è la lunghezza della finestra di contesto (numero di token).
* Composizione delle **Istruzioni di Sistema (System Prompt):** È possibile impostare il ruolo, il tono e le regole di comportamento del modello all'inizio di ogni dialogo. Ad esempio: "Sei un esperto di Python, rispondi in modo conciso."
* Inclusione di diversi esempi di comportamento desiderato nella richiesta **Few-Shot Learning:** (coppie input/output) consente al modello di "imparare" questo pattern direttamente all'interno della richiesta corrente.
* **Gestione dello stato lato applicazione:** Il modo più potente. L'applicazione (che accede all'API) può memorizzare informazioni sull'utente (preferenze, cronologia, dati del profilo) e aggiungerle dinamicamente al prompt prima di inviarlo al modello.


### 2.

L'ottimizzazione è il processo di ulteriore addestramento di un LLM di base già esistente sul proprio set di dati specifico. Ciò consente al modello di:

* **Adattare stile e tono:** Il modello parlerà "la tua lingua" – che sia strettamente scientifica, amichevole di marketing o il gergo di una comunità specifica.
* **Seguire istruzioni e formati specifici:** Se hai bisogno di risposte in una struttura JSON strettamente definita, o sempre con un set specifico di campi.
* **Comprendere il linguaggio specifico del dominio:** L'addestramento sulla tua documentazione interna o sui testi del settore aiuterà il modello a gestire meglio la terminologia della tua nicchia.
* **Migliorare le prestazioni su compiti specifici:** Per alcuni tipi di query (ad esempio, classificazione del sentiment, generazione di codice in un framework specifico), l'ottimizzazione può fornire risposte più accurate e pertinenti rispetto al modello di base.
* **Ridurre la lunghezza del prompt:** Se il modello "conosce" già il comportamento desiderato grazie all'ottimizzazione, non è necessario ricordarglielo ogni volta nel prompt, il che consente di risparmiare token e ridurre la latenza.

### 3.

L'ottimizzazione è uno strumento potente ma non universale. Non dovresti usarlo se:

* **Il modello ha bisogno di accedere a nuove conoscenze:** L'ottimizzazione modifica i pesi del modello, ma non "carica" nuovi fatti in tempo reale. Se il tuo compito è rispondere a domande basate su una base di conoscenze in continua evoluzione (documenti aziendali, ultime notizie), è meglio utilizzare la **Generazione Aumentata da Recupero (RAG)**. Qui, il modello di base riceve il contesto dal tuo database *al momento della query*.
* **Un compito semplice può essere risolto con l'ingegneria dei prompt:** Inizia sempre con l'ingegneria dei prompt più efficace. Se il compito può essere risolto con istruzioni semplici ed esempi few-shot, l'ottimizzazione è ridondante e più costosa.
* **Non hai abbastanza dati di alta qualità:** Dati scadenti = modello ottimizzato male.

### 4. Preparazione dei dati.

La qualità e la quantità dei tuoi dati sono di fondamentale importanza. Il modello apprende dai tuoi esempi, quindi devono essere precisi, diversi e coerenti.

* **Formato:** Molto spesso JSON Lines (`.jsonl`) o CSV (`.csv`).
* **Struttura dei dati:** Dipende dal compito.
    * **Instruction Tuning (Istruzione-Risposta):** Adatto per compiti generalizzati come "domanda-risposta", parafrasi, riassunto.
    ```json
    {"input_text": "Перефразируй предложение: 'Технология ИИ стремительно развивается.'", "output_text": "Искусственный интеллект демонстрирует стремительный прогресс."}
    {"input_text": "Назови столицу Франции.", "output_text": "Столица Франции — Париж."}
    ```
    * **Chat Tuning (Chat):** Ideale per addestrare il modello a condurre un dialogo in un ruolo o stile specifico.
    ```json
    {"messages": [{"author": "user", "content": "Привет! Что порекомендуешь на ужин?"}, {"author": "model", "content": "Добрый вечер! Сегодня отличный день per пасты Карбонара, или, если вы предпочитаете что-то легкое, салат Цезарь."}]}
    {"messages": [{"author": "user", "content": "Расскажи про новые фичи в Python 3.12."}, {"author": "model", "content": "В Python 3.12 появились f-строки con отступами, новый синтаксис per универсальных генериков и улучшенная обработка ошибок Unicode."}]}
    ```
* **Quantità:** Minimo 100-200 esempi di alta qualità, ma più ce ne sono, meglio è (migliaia per compiti seri).
* **Qualità:** Precisione, stile, tono e formato coerenti in tutto il set di dati.

### 5. Modelli e Piattaforme


#### 5.1. OpenAI

OpenAI fornisce un'API abbastanza semplice e intuitiva per l'ottimizzazione.

**Processo:**

1.  Prepara i dati in formato JSONL, dove ogni riga è un oggetto con un array `messages` (come nell'API Chat Completions).
2.  Carica il file di dati tramite API.
3.  Crea un lavoro di ottimizzazione, specificando il file caricato e il modello di base.
4.  Monitora i progressi.
5.  Usa il nuovo modello ottimizzato tramite il suo ID.

**Esempio di dati (file `training_data.jsonl`):**

```json
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "My internet is not working."}, {"role": "assistant", "content": "Oh, I apologize for the inconvenience! Let's try to figure it out. How are you connected to the internet – via Wi-Fi or cable?"}]}
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "How can I reset my password?"}, {"role": "assistant", "content": "Of course! To reset your password, please go to the login page and click 'Forgot password?' below the input field. Then follow the on-screen instructions."}]}
```

**Esempio di codice Python:**

Installa prima: `pip install openai`

```python
import openai
from openai import OpenAI
import os

# Imposta la tua chiave API OpenAI. Si consiglia di utilizzare una variabile d'ambiente.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Caricamento del file di dati
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"File caricato con successo. ID file: {file_id}")
except openai.APIStatusError as e:
    print(f"Errore di caricamento del file: {e.status_code} - {e.response}")
    exit()

# 2. Creazione del lavoro di ottimizzazione
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Puoi specificare una versione specifica, ad esempio, "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Lavoro di ottimizzazione creato. ID lavoro: {job_id}")
    print("Monitora lo stato del lavoro tramite API o in OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Errore di creazione del lavoro: {e.status_code} - {e.response}")
    exit()

# Esempio di monitoraggio dello stato e ottenimento del nome del modello (esegui dopo la creazione del lavoro):
# # job_id = "ftjob-..." # Sostituisci con il tuo ID lavoro
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Stato attuale del lavoro: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Nome del modello ottimizzato: {fine_tuned_model_name}")

# 3. Utilizzo del modello ottimizzato (dopo che è pronto)
# # Sostituisci con il nome reale del tuo modello, ottenuto dopo un'ottimizzazione riuscita
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "Ho un problema di accesso."}
# #             ]
# #         )
# #         print("\nRisposta del modello ottimizzato:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Errore durante l'utilizzo del modello: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **non fornisce un'API pubblica per l'ottimizzazione dei suoi modelli Claude 3 (Opus, Sonnet, Haiku) nello stesso modo di OpenAI o Google.**

Anthropic si concentra sulla creazione di modelli di base molto potenti che, a loro dire, funzionano in modo eccellente con l'ingegneria dei prompt avanzata e i pattern RAG, minimizzando la necessità di ottimizzazione nella maggior parte dei casi.
Per i grandi clienti aziendali o i partner, potrebbero esistere programmi per la creazione di modelli "personalizzati" o integrazioni specializzate, ma questa non è una funzionalità di ottimizzazione disponibile pubblicamente tramite API.

Se stai lavorando con Claude 3, il tuo focus principale dovrebbe essere su:

* **Ingegneria dei prompt di alta qualità:** Sperimenta con le istruzioni di sistema, gli esempi few-shot, la formattazione chiara delle richieste. Claude è noto per la sua capacità di seguire rigorosamente le istruzioni, specialmente nei tag XML.
* **Sistemi RAG:** Utilizza basi di conoscenza esterne per fornire al modello un contesto pertinente.

#### 5.3. Google (Gemini)

Google sta sviluppando attivamente le capacità di ottimizzazione tramite la sua piattaforma **Google Cloud Vertex AI**.
Questa è una piattaforma ML completa che fornisce strumenti per la preparazione dei dati, l'esecuzione di lavori di addestramento e la distribuzione dei modelli.
L'ottimizzazione è disponibile per la famiglia di modelli Gemini.

**Processo:**

1.  Prepara i dati (JSONL o CSV) in formato `input_text`/`output_text` (per l'ottimizzazione delle istruzioni) o `messages` (per l'ottimizzazione della chat).
2.  Carica i dati su Google Cloud Storage (GCS).
3.  Crea ed esegui un lavoro di ottimizzazione tramite la Console o l'SDK di Vertex AI.
4.  Distribuisci il modello ottimizzato su un Endpoint.
5.  Usa il modello ottimizzato tramite questo Endpoint.

**Esempio di dati (file `gemini_tuning_data.jsonl`):**

```json
{"input_text": "Sintetizza le idee principali di questo libro: 'Il libro racconta il viaggio di un eroe, che supera gli ostacoli e trova se stesso.'", "output_text": "Il personaggio principale del libro intraprende un viaggio trasformativo, affrontando sfide e raggiungendo la conoscenza di sé."}
{"input_text": "Spiega il principio di funzionamento di un reattore termonucleare in termini semplici.", "output_text": "Un reattore termonucleare tenta di replicare il processo che avviene sul Sole: la fusione di nuclei atomici leggeri a temperature molto elevate, rilasciando un'enorme quantità di energia."}
```

**Esempio di codice Python (richiede `google-cloud-aiplatform`):**

Installa prima: `pip install google-cloud-aiplatform` e `pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# ---
# Impostazioni ---
# SOSTITUISCI con i tuoi valori:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Scegli una regione che supporti Gemini e Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Il nome del tuo bucket GCS (deve essere creato prima)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# ---
# Fine impostazioni ---

# Inizializza Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Crea il file di dati (se non esiste)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Sintetizza le idee principali di questo libro: \'Il libro racconta il viaggio di un eroe, che supera gli ostacoli e trova se stesso.\'", "output_text": "Il personaggio principale del libro intraprende un viaggio trasformativo, affrontando sfide e raggiungendo la conoscenza di sé."}\n')
    f.write('{"input_text": "Spiega il principio di funzionamento di un reattore termonucleare in termini semplici.", "output_text": "Un reattore termonucleare tenta di replicare il processo che avviene sul Sole: la fusione di nuclei atomici leggeri a temperature molto elevate, rilasciando un\'enorme quantità di energia."}\n')
print(f"File di dati '{DATA_FILE_LOCAL_PATH}' creato.")


# 2. Carica i dati su Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Carica un file sul bucket GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File '{source_file_name}' caricato su 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Errore durante il caricamento del file su GCS. Assicurati che il bucket esista e che tu abbia i permessi: {e}")
    exit()

# 3. Crea ed esegui un lavoro di ottimizzazione
print(f"\nAvvio dell'ottimizzazione del modello '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` avvia il lavoro e restituisce il modello ottimizzato al completamento
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Modello base Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Numero di passaggi di addestramento. Il valore ottimale dipende dalla dimensione dei dati.
        # batch_size=16, # Può essere specificato
        # learning_rate_multiplier=1.0 # Può essere specificato
    )
    print(f"Modello '{TUNED_MODEL_DISPLAY_NAME}' ottimizzato con successo. ID modello: {tuned_model.name}")
    print("Il processo di ottimizzazione potrebbe richiedere molto tempo.")
except Exception as e:
    print(f"Errore di ottimizzazione. Controlla i log nella Console Vertex AI: {e}")
    exit()

# 4. Distribuisci il modello ottimizzato (per l'uso)
print(f"\nDistribuzione del modello ottimizzato '{TUNED_MODEL_DISPLAY_NAME}' all'endpoint...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Tipo di macchina per l'endpoint. Scegli quello appropriato.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Modello distribuito all'endpoint: {endpoint.name}")
    print("La distribuzione potrebbe richiedere anche diversi minuti.")
except Exception as e:
    print(f"Errore durante la distribuzione del modello: {e}")
    exit()

# 5. Utilizzo del modello ottimizzato
print("\nTest del modello ottimizzato...")
prompt = "Parlami delle tue capacità dopo l'addestramento."
instances = [{"prompt": prompt}] # Per l'ottimizzazione delle istruzioni. Se ottimizzazione della chat, allora {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nRisposta del modello ottimizzato:")
    print(response.predictions[0])
except Exception as e:
    print(f"Errore durante l'utilizzo del modello ottimizzato: {e}")

# Dopo aver terminato, non dimenticare di eliminare l'endpoint e il modello per evitare costi inutili:
# endpoint.delete()
# tuned_model.delete()
```

### 6. Raccomandazioni generali

* **Inizia in piccolo:** Non cercare di addestrare il modello su migliaia di esempi subito. Inizia con un set di dati piccolo ma di alta qualità.
* **Itera:** L'ottimizzazione è un processo iterativo. Addestra, valuta, regola i dati o gli iperparametri, ripeti.
* **Monitoraggio:** Monitora attentamente le metriche di addestramento (perdite) e usa un set di dati di validazione per evitare l'overfitting.
* **Valutazione:** Testa sempre il modello ottimizzato su dati che *non ha mai visto* durante l'addestramento per valutarne la capacità di generalizzazione.
* **Costo:** Ricorda che l'ottimizzazione e la distribuzione degli endpoint sono a pagamento. Tienine conto nel tuo budget.
* **Documentazione:** Fai sempre riferimento alla documentazione ufficiale del fornitore LLM. API e funzionalità sono in continua evoluzione.
