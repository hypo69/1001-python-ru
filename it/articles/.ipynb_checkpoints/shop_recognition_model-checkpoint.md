# Addestramento di un modello OpenAI per la classificazione di pagine web

## Introduzione

Addestramento di un modello OpenAI per determinare se una pagina è un negozio online.

- preparazione dei dati,
- tokenizzazione del testo,
- invio dei dati per l'addestramento
- test del modello.

## Passaggio 1: Registrazione e configurazione dell'API OpenAI

Per iniziare a lavorare con l'API OpenAI, è necessario registrarsi sulla piattaforma OpenAI e ottenere una chiave API. Questa chiave verrà utilizzata per l'autenticazione durante la chiamata dei metodi API.

```python
import openai

# Imposta la chiave API
openai.api_key = 'your-api-key'
```

## Passaggio 2: Preparazione dei dati

Per addestrare il modello, è necessario preparare un set di dati che conterrà esempi di pagine web,
sia di negozi che di non negozi.
Ogni voce deve includere il testo della pagina e un'etichetta corrispondente (`positive` per i negozi e `negative` per i non negozi).

Esempio di file JSON:

```json
[
    {
        "text": "<html><body><h1>Benvenuti nel nostro negozio online</h1><p>Offriamo una vasta gamma di prodotti a prezzi competitivi. Visita il nostro negozio oggi stesso!</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>Chi siamo</h1><p>Siamo un fornitore leader di servizi di qualità. Contattaci per maggiori informazioni.</p></body></html>",
        "label": "negative"
    }
]
```

## Passaggio 3: Tokenizzazione del testo

Prima di inviare i dati al modello OpenAI, il testo deve essere tokenizzato.
La tokenizzazione è il processo di suddivisione del testo in singole parole o token.
In Python, puoi usare librerie come NLTK, spaCy o tokenizers dalla libreria transformers.

Esempio di tokenizzazione usando NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# Testo di esempio
text = "Questo è un testo di esempio per la tokenizzazione."

# Tokenizzazione del testo
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## Passaggio 4: Invio dei dati per l'addestramento

Dopo aver tokenizzato il testo, puoi inviare i dati per addestrare il modello OpenAI.
Ecco un esempio di codice per l'invio dei dati:

```python
import openai

def train_model(data, positive=True):
    try:
        response = openai.Train.create(
            model="text-davinci-003",
            documents=[entry["text"] for entry in data],
            labels=["positive" if positive else "negative"] * len(data),
            show_progress=True
        )
        return response.id
    except Exception as ex:
        print("Si è verificato un errore durante l'addestramento:", ex)
        return None

# Esempio di utilizzo
data = [
    {"text": "Testo della prima pagina web...", "label": "positive"},
    {"text": "Testo della seconda pagina web...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("ID lavoro:", job_id)
```

## Passaggio 5: Test del modello

Dopo aver addestrato il modello, deve essere testato su un set di dati di test.
Ecco un esempio di codice per il test:

```python
def test_model(test_data):
    try:
        predictions = []
        for entry in test_data:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=entry["text"],
                max_tokens=1
            )
            prediction = response.choices[0].text.strip()
            predictions.append(prediction)
        return predictions
    except Exception as ex:
        print("Si è verificato un errore durante il test:", ex)
        return None

# Esempio di utilizzo
test_data = [
    {"text": "Testo della pagina web di test...", "label": "positive"},
    {"text": "Testo di un'altra pagina di test...", "label": "negative"}
]

predictions = test_model(test_data)
print("Previsioni:", predictions)
```

## Passaggio 6: Gestione degli errori e miglioramento del modello

Se il modello fornisce previsioni errate, è possibile migliorarlo
aggiungendo più dati o modificando i parametri di addestramento. È inoltre possibile utilizzare il feedback per analizzare gli errori.

Esempio di gestione degli errori:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Previsione errata per la pagina '{entry['name']}': Previsto {pred}, Effettivo {entry['label']}")

# Esempio di utilizzo
handle_errors(predictions, test_data)
```