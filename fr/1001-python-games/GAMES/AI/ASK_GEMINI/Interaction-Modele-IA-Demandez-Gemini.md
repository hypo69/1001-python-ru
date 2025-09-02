### Posez une question au modèle Gemini

Une clé API est requise pour fonctionner.

LA CLÉ API DU MODÈLE PEUT ÊTRE OBTENUE ICI : [https://aistudio.google.com/](https://aistudio.google.com/)




```python
import google.generativeai as genai

class GoogleGenerativeAI:
    """
    Classe pour interagir avec les modèles Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """
        Initialise le modèle GoogleGenerativeAI.

        Arguments:
            api_key (str): Clé API pour accéder au modèle génératif.
            model_name (str, optional): Nom du modèle à utiliser. Par défaut "gemini-2.0-flash-exp".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        Envoie une requête texte au modèle et renvoie la réponse.

        Arguments:
            q (str): La question à envoyer au modèle.

        Renvoie:
            str: Réponse du modèle.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Erreur : {str(ex)}"
```

### Comment fonctionne ce code

1. **Importation de la bibliothèque** : Nous importons la bibliothèque `google.generativeai`, qui fournit une interface pour interagir avec les modèles Google AI.

2. **Classe `GoogleGenerativeAI`** : Cette classe encapsule toute la logique d'interaction avec le modèle Gemini. Elle prend une clé API et un nom de modèle comme paramètres. Le modèle `gemini-2.0-flash-exp` est utilisé par défaut.

3. **Méthode `__init__`** : Dans cette méthode, le modèle est configuré. Nous passons la clé API et le nom du modèle, puis nous initialisons l'objet modèle.

4. **Méthode `ask`** : Cette méthode envoie une requête texte au modèle et renvoie la réponse. Si quelque chose ne va pas, la méthode renverra un message d'erreur.

### Comment utiliser ?

```python
################################################################################
#                                                                              #
#             INSÉREZ VOTRE CLÉ API GEMINI                                       #
#                                                                              #
################################################################################

API_KEY: str = input("Clé API de `gemini` : ")
model = GoogleGenerativeAI(api_key=API_KEY)

q = input("Question : ")
response = model.ask(q)
print(response)
```

1. **Saisie de la clé API** : Tout d'abord, le programme demande à l'utilisateur une clé API pour accéder au modèle Gemini. Cette clé peut être obtenue sur le site [Google AI Studio](https://aistudio.google.com/).

2. **Création de l'objet modèle** : Nous créons un objet de la classe `GoogleGenerativeAI`, en lui passant la clé API.

3. **Saisie de la question** : L'utilisateur saisit la question qu'il souhaite poser au modèle.

4. **Obtention de la réponse** : Le programme envoie la question au modèle et affiche la réponse à l'écran.

### Exemple d'utilisation

Vous avez une clé API, et vous voulez demander au modèle : "Comment puis-je améliorer mon code ?". Voici à quoi cela ressemblera :

```
Clé API de `gemini` : votre_clé_api
Question : Comment puis-je améliorer mon code ?
Réponse : Pour améliorer votre code, il est recommandé de suivre les principes de code propre, tels que nommer les variables et les fonctions de manière claire et logique, utiliser des commentaires pour expliquer la logique complexe, et appliquer les principes SOLID pour la conception des classes et des modules.
```


Exécutez le code [ici](https://colab.research.google.com/github/hypo69/101_python_computer_games_ru/blob/master/GAMES/AI/ASK_GEMINI/ask_gemini_ru.ipynb)
