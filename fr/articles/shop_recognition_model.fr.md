# Entraînement d'un modèle OpenAI pour la classification de pages web

## Introduction

Entraînement d'un modèle OpenAI pour déterminer si une page est une boutique en ligne.

- préparation des données,
- tokenisation du texte,
- envoi des données pour l'entraînement
- test du modèle.

## Étape 1: Inscription et configuration de l'API OpenAI

Pour commencer à travailler avec l'API OpenAI, vous devez vous inscrire sur la plateforme OpenAI et obtenir une clé API. Cette clé sera utilisée pour l'authentification lors de l'appel des méthodes API.

```python
import openai

# Définir la clé API
openai.api_key = 'votre-clé-api'
```

## Étape 2: Préparation des données

Pour entraîner le modèle, vous devez préparer un ensemble de données qui contiendra des exemples de pages web,
à la fois des boutiques et des non-boutiques.
Chaque entrée doit inclure le texte de la page et une étiquette correspondante (`positive` pour les boutiques et `negative` pour les non-boutiques).

Exemple de fichier JSON:

```json
[
    {
        "text": "<html><body><h1>Bienvenue dans notre boutique en ligne</h1><p>Nous offrons une large gamme de produits à des prix compétitifs. Visitez notre boutique aujourd'hui!</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>À propos de nous</h1><p>Nous sommes un fournisseur leader de services de qualité. Contactez-nous pour plus d'informations.</p></body></html>",
        "label": "negative"
    }
]
```

## Étape 3: Tokenisation du texte

Avant d'envoyer les données au modèle OpenAI, le texte doit être tokenisé.
La tokenisation est le processus de division du texte en mots ou tokens individuels.
En Python, vous pouvez utiliser des bibliothèques telles que NLTK, spaCy ou tokenizers de la bibliothèque transformers.

Exemple de tokenisation utilisant NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# Exemple de texte
text = "Ceci est un exemple de texte pour la tokenisation."

# Tokenisation du texte
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## Étape 4: Envoi des données pour l'entraînement

Après avoir tokenisé le texte, vous pouvez envoyer les données pour entraîner le modèle OpenAI.
Voici un exemple de code pour l'envoi des données:

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
        print("Une erreur s'est produite pendant l'entraînement:", ex)
        return None

# Exemple d'utilisation
data = [
    {"text": "Texte de la première page web...", "label": "positive"},
    {"text": "Texte de la deuxième page web...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("ID de la tâche:", job_id)
```

## Étape 5: Test du modèle

Après l'entraînement du modèle, vous devez le tester sur un ensemble de données de test.
Voici un exemple de code pour le test:

```python
import openai

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
        print("Une erreur s'est produite pendant le test:", ex)
        return None

# Exemple d'utilisation
test_data = [
    {"text": "Texte de la page web de test...", "label": "positive"},
    {"text": "Texte d'une autre page de test...", "label": "negative"}
]

predictions = test_model(test_data)
print("Prédictions:", predictions)
```

## Étape 6: Gestion des erreurs et amélioration du modèle

Si le modèle donne des prédictions incorrectes, vous pouvez l'améliorer en
ajoutant plus de données ou en modifiant les paramètres d'entraînement. Vous pouvez également utiliser les retours pour analyser les erreurs.

Exemple de gestion des erreurs:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Prédiction incorrecte pour la page '{entry['name']}': Prédit {pred}, Réel {entry['label']}")

# Exemple d'utilisation
handle_errors(predictions, test_data)
```