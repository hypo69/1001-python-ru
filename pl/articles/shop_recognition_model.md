# Szkolenie modelu OpenAI do klasyfikacji stron internetowych

## Wprowadzenie

Szkolenie modelu OpenAI do określania, czy strona jest sklepem internetowym.

- przygotowanie danych,
- tokenizacja tekstu,
- wysyłanie danych do szkolenia
- testowanie modelu.

## Krok 1: Rejestracja i konfiguracja API OpenAI

Aby rozpocząć pracę z API OpenAI, musisz zarejestrować się na platformie OpenAI i uzyskać klucz API. Ten klucz będzie używany do uwierzytelniania podczas wywoływania metod API.

```python
import openai

# Ustawienie klucza API
openai.api_key = 'your-api-key'
```

## Krok 2: Przygotowanie danych

Aby wyszkolić model, musisz przygotować zestaw danych, który będzie zawierał przykłady stron internetowych,
zarówno sklepów, jak i stron innych niż sklepy.
Każdy wpis musi zawierać tekst strony i odpowiadającą mu etykietę (`positive` dla sklepów i `negative` dla stron innych niż sklepy).

Przykładowy plik JSON:

```json
[
    {
        "text": "<html><body><h1>Witamy w naszym sklepie internetowym</h1><p>Oferujemy szeroki wybór produktów w konkurencyjnych cenach. Odwiedź nasz sklep już dziś!</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>O nas</h1><p>Jesteśmy wiodącym dostawcą wysokiej jakości usług. Skontaktuj się z nami, aby uzyskać więcej informacji.</p></body></html>",
        "label": "negative"
    }
]
```

## Krok 3: Tokenizacja tekstu

Przed wysłaniem danych do modelu OpenAI tekst musi zostać stokenizowany.
Tokenizacja to proces dzielenia tekstu na pojedyncze słowa lub tokeny.
W Pythonie możesz użyć bibliotek takich jak NLTK, spaCy lub tokenizers z biblioteki transformers.

Przykład tokenizacji za pomocą NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# Przykładowy tekst
text = "To jest przykładowy tekst do tokenizacji."

# Tokenizacja tekstu
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## Krok 4: Wysyłanie danych do szkolenia

Po tokenizacji tekstu możesz wysłać dane do szkolenia modelu OpenAI.
Oto przykład kodu do wysyłania danych:

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
        print("Wystąpił błąd podczas szkolenia:", ex)
        return None

# Przykładowe użycie
data = [
    {"text": "Tekst pierwszej strony internetowej...", "label": "positive"},
    {"text": "Tekst drugiej strony internetowej...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("ID zadania:", job_id)
```

## Krok 5: Testowanie modelu

Po wyszkoleniu modelu należy go przetestować na zestawie danych testowych.
Oto przykład kodu do testowania:

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
        print("Wystąpił błąd podczas testowania:", ex)
        return None

# Przykładowe użycie
test_data = [
    {"text": "Tekst testowej strony internetowej...", "label": "positive"},
    {"text": "Tekst innej strony testowej...", "label": "negative"}
]

predictions = test_model(test_data)
print("Prognozy:", predictions)
```

## Krok 6: Obsługa błędów i ulepszanie modelu

Jeśli model daje nieprawidłowe prognozy, możesz go ulepszyć,
dodając więcej danych lub zmieniając parametry szkolenia. Możesz również wykorzystać informacje zwrotne do analizy błędów.

Przykład obsługi błędów:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Nieprawidłowa prognoza dla strony '{entry['name']}': Przewidziano {pred}, Rzeczywiste {entry['label']}")

# Przykładowe użycie
handle_errors(predictions, test_data)
```