# Training eines OpenAI-Modells zur Klassifizierung von Webseiten

## Einführung

Training eines OpenAI-Modells, um festzustellen, ob eine Seite ein Online-Shop ist.

- Datenvorbereitung,
- Text-Tokenisierung,
- Senden von Daten zum Training
- Modelltest.

## Schritt 1: Registrierung und Einrichtung der OpenAI API

Um mit der OpenAI API zu arbeiten, müssen Sie sich auf der OpenAI-Plattform registrieren und einen API-Schlüssel erhalten. Dieser Schlüssel wird zur Authentifizierung beim Aufruf von API-Methoden verwendet.

```python
import openai

# API-Schlüssel festlegen
openai.api_key = 'your-api-key'
```

## Schritt 2: Datenvorbereitung

Um das Modell zu trainieren, müssen Sie einen Datensatz vorbereiten, der Beispiele von Webseiten enthält,
sowohl von Shops als auch von Nicht-Shops.
Jeder Eintrag muss den Text der Seite und ein entsprechendes Label (`positive` für Shops und `negative` für Nicht-Shops) enthalten.

Beispiel JSON-Datei:

```json
[
    {
        "text": "<html><body><h1>Willkommen in unserem Online-Shop</h1><p>Wir bieten eine große Auswahl an Produkten zu wettbewerbsfähigen Preisen. Besuchen Sie unseren Shop noch heute!</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>Über uns</h1><p>Wir sind ein führender Anbieter von Qualitätsdienstleistungen. Kontaktieren Sie uns für weitere Informationen.</p></body></html>",
        "label": "negative"
    }
]
```

## Schritt 3: Text-Tokenisierung

Bevor die Daten an das OpenAI-Modell gesendet werden, muss der Text tokenisiert werden.
Tokenisierung ist der Prozess des Aufteilens von Text in einzelne Wörter oder Token.
In Python können Sie Bibliotheken wie NLTK, spaCy oder Tokenizer aus der Transformers-Bibliothek verwenden.

Beispiel Tokenisierung mit NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# Beispieltext
text = "Dies ist ein Beispieltext zur Tokenisierung."

# Text-Tokenisierung
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## Schritt 4: Senden von Daten zum Training

Nach der Tokenisierung des Textes können Sie die Daten zum Trainieren des OpenAI-Modells senden.
Hier ist ein Beispielcode zum Senden von Daten:

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
        print("Während des Trainings ist ein Fehler aufgetreten:", ex)
        return None

# Beispielverwendung
data = [
    {"text": "Text der ersten Webseite...", "label": "positive"},
    {"text": "Text der zweiten Webseite...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("Job-ID:", job_id)
```

## Schritt 5: Modelltest

Nach dem Training des Modells muss es mit einem Testdatensatz getestet werden.
Hier ist ein Beispielcode zum Testen:

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
        print("Während des Tests ist ein Fehler aufgetreten:", ex)
        return None

# Beispielverwendung
test_data = [
    {"text": "Text der Test-Webseite...", "label": "positive"},
    {"text": "Text einer anderen Testseite...", "label": "negative"}
]

predictions = test_model(test_data)
print("Vorhersagen:", predictions)
```

## Schritt 6: Fehlerbehandlung und Modellverbesserung

Wenn das Modell falsche Vorhersagen liefert, können Sie es verbessern, indem Sie
mehr Daten hinzufügen oder Trainingsparameter ändern. Sie können auch Feedback zur Fehleranalyse verwenden.

Beispiel Fehlerbehandlung:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Falsche Vorhersage für Seite '{entry['name']}': Vorhergesagt {pred}, Tatsächlich {entry['label']}")

# Beispielverwendung
handle_errors(predictions, test_data)
```