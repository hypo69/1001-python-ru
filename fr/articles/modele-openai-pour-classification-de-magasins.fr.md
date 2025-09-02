# Entraînement d'un modèle OpenAI pour classer les pages Web

## Introduction

Entraînement d'un modèle OpenAI pour déterminer si une page est une boutique en ligne.

- préparation des données,
- tokenisation du texte,
- envoi des données pour l'entraînement
- test du modèle.

## Étape 1 : Inscription et configuration de l'API OpenAI

Pour commencer à utiliser l'API OpenAI, vous devez vous inscrire sur la plateforme OpenAI et obtenir une clé API. Cette clé sera utilisée pour l'authentification lors de l'appel des méthodes de l'API.

```python
import openai

# Définir la clé API
openai.api_key = 'your-api-key'
```

## Étape 2 : Préparation des données

Pour entraîner le modèle, vous devez préparer un jeu de données qui contiendra des exemples de pages Web,
à la fois des boutiques et des non-boutiques.
Chaque entrée doit inclure le texte de la page et l'étiquette correspondante (`positive` pour les boutiques et `negative` pour les non-boutiques).

Exemple de fichier JSON :

```json
[
    {
        "text": "<html><body><h1>Bienvenue dans notre boutique en ligne</h1><p>Nous proposons une large gamme de produits à des prix compétitifs. Visitez notre boutique dès aujourd'hui !</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>À propos de nous</h1><p>Nous sommes un fournisseur de premier plan de services de qualité. Contactez-nous pour plus d'informations.</p></body></html>",
        "label": "negative"
    }
]
```

## Étape 3 : Tokenisation du texte

Avant d'envoyer les données au modèle OpenAI, le texte doit être tokenisé.
La tokenisation est le processus de décomposition du texte en mots ou jetons individuels.
En Python, vous pouvez utiliser des bibliothèques telles que NLTK, spaCy ou les tokenizers de la bibliothèque transformers.

Exemple de tokenisation avec NLTK :

```python
import nltk
from nltk.tokenize import word_tokenize

# Exemple de texte
text = "Ceci est un exemple de texte pour la tokenisation."

# Tokeniser le texte
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## Étape 4 : Envoi des données pour l'entraînement

Après avoir tokenisé le texte, vous pouvez envoyer les données pour entraîner le modèle OpenAI.
Voici un exemple de code pour envoyer des données :

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
        print("An error occurred during training:", ex)
        return None

# Exemple d'utilisation
data = [
    {"text": "Texte de la première page Web...", "label": "positive"},
    {"text": "Texte de la deuxième page Web...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("Job ID:", job_id)
```

## Étape 5 : Test du modèle

Après avoir entraîné le modèle, vous devez le tester sur un jeu de données de test.
Voici un exemple de code pour les tests :

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
        print("An error occurred during testing:", ex)
        return None

# Exemple d'utilisation
test_data = [
    {"text": "Texte d'une page Web de test...", "label": "positive"},
    {"text": "Texte d'une autre page de test...", "label": "negative"}
]

predictions = test_model(test_data)
print("Predictions:", predictions)
```

## Étape 6 : Gestion des erreurs et amélioration du modèle

Si le modèle fait des prédictions incorrectes, vous pouvez l'améliorer
en ajoutant plus de données ou en modifiant les paramètres d'entraînement. Vous pouvez également utiliser les commentaires pour analyser les erreurs.

Exemple de gestion des erreurs :

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Incorrect prediction for page '{entry['name']}': Predicted {pred}, Actual {entry['label']}")

# Exemple d'utilisation
handle_errors(predictions, test_data)
```