# BANNIÈRE IA
Le modèle Gemini renvoie la réponse sous forme de bannière ASCII en fonction de l'instruction qui lui est donnée.

 Le programme interagit avec le modèle Google Generative AI pour créer des bannières textuelles.
 L'utilisateur peut choisir le style de conception de la bannière et envoyer du texte au modèle pour traitement.

## Installation des dépendances
Pour exécuter le code sur une machine locale, vous devrez installer les bibliothèques Google.

```python
pip install google
pip install google-generativeai
```

Je recommande fortement de faire toutes les expériences dans un environnement virtuel.


## Fonctionnalités du code dans ce programme
1. Les instructions sont stockées dans différents fichiers et chargées au besoin.
2. À partir de cet exemple, je sauvegarde la clé du modèle dans une variable d'environnement, ce qui m'évite d'avoir à saisir la clé à plusieurs reprises.
3. J'utilise des chemins absolus vers les fichiers.
    Pour déterminer le répertoire racine du projet, je recherche récursivement vers le haut les fichiers marqueurs ('pyproject.toml', 'requirements.txt', '.git').
    Je stocke le répertoire trouvé dans la variable __root__. À partir de là, je construis le chemin vers les instructions système :
    ``python
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Chemin relatif vers le répertoire
    base_path: Path = __root__ / relative_path  # Chemin absolu vers le répertoire en utilisant __root__
    ``


### 1. **Importation des bibliothèques nécessaires**
```python
import google.generativeai as genai  # Importer la bibliothèque pour travailler avec Gemini
import re  # Importer la bibliothèque pour travailler avec les expressions régulières
from pathlib import Path  # Importer pour travailler avec les chemins du système de fichiers
from header import __root__  # Importer l'objet __root__, contenant le chemin absolu vers la racine du projet
from dotenv import load_dotenv, set_key  # Importer les fonctions pour travailler avec les variables d'environnement
import os  # Importer pour travailler avec les variables d'environnement
```

- **`google.generativeai`** : Utilisé pour interagir avec l'API Google Generative AI.
- **`re`** : Bibliothèque pour travailler avec les expressions régulières (non utilisée dans ce code, mais peut être utile à l'avenir).
- **`Path`** : Permet de travailler avec les chemins du système de fichiers.
- **`__root__`** : Objet contenant le chemin absolu vers la racine du projet.
- **`dotenv`** : Permet de charger les variables d'environnement à partir d'un fichier `.env` et de les enregistrer.
- **`os`** : Utilisé pour travailler avec les variables d'environnement.

---

### 2. **Chargement des variables d'environnement**
```python
load_dotenv()
```
- La fonction `load_dotenv()` charge les variables d'environnement à partir du fichier `.env`, s'il existe.

---

### 3. **Classe `GoogleGenerativeAI`**
La classe est conçue pour interagir avec le modèle Google Generative AI.

#### 3.1. **Attributs de classe**
```python
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b'
]
```
- Liste des modèles Google Generative AI disponibles.

#### 3.2. **Méthode `__init__`**
```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
    """
    Initialise le modèle GoogleGenerativeAI.

    :param api_key: Clé API pour accéder à Gemini.
    :type api_key: str
    :param system_instruction: Instruction pour le modèle (invite système).
    :type system_instruction: str
    :param model_name: Nom du modèle Gemini à utiliser. Par défaut 'gemini-2.0-flash-exp'.
    :type model_name: str
    """
    self.api_key = api_key
    self.model_name = model_name
    genai.configure(api_key=self.api_key)  # Configurer la bibliothèque avec la clé API
    self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # Initialiser le modèle avec l'instruction
```
- **`api_key`** : Clé API pour accéder à Google Generative AI.
- **`system_instruction`** : Instruction pour le modèle (par exemple, style de formatage du texte).
- **`model_name`** : Nom du modèle, par défaut `'gemini-2.0-flash-exp'`.
- **`genai.configure(api_key=self.api_key)`** : Configuration de la bibliothèque à l'aide de la clé API.
- **`genai.GenerativeModel(...)`** : Initialisation du modèle avec les paramètres spécifiés.

#### 3.3. **Méthode `ask`**
```python
def ask(self, q: str) -> str:
    """
    Envoie une requête au modèle et reçoit une réponse.

    :param q: Texte de la requête.
    :type q: str
    :return: Réponse du modèle ou message d'erreur.
    :rtype: str
    """
    try:
        response = self.model.generate_content(q)  # Envoyer la requête au modèle
        return response.text  # Obtenir la réponse textuelle
    except Exception as ex:
        return f'Erreur : {str(ex)}'  # Gérer et obtenir l'erreur
```
- **`q`** : Le texte de la requête envoyé au modèle.
- **`self.model.generate_content(q)`** : Envoi de la requête au modèle.
- **`response.text`** : Obtention de la réponse textuelle du modèle.
- **`except Exception as ex`** : Gestion des erreurs et renvoi d'un message d'erreur.

---

### 4. **Partie principale du programme**
```python
if __name__ == '__main__':
```
- Vérifie que le programme est exécuté en tant que script autonome.

#### 4.1. **Définition des chemins**
```python
relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Chemin relatif vers le répertoire
base_path: Path = __root__ / relative_path  # Chemin absolu vers le répertoire en utilisant __root__
```
- **`relative_path`** : Chemin relatif vers le répertoire dans le projet.
- **`base_path`** : Chemin absolu, obtenu en combinant `__root__` et `relative_path`.

#### 4.2. **Lecture de la clé API**
```python
API_KEY: str = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input('Clé API introuvable. Entrez la clé API de `gemini` : ')  # Demander la clé API à l'utilisateur
    set_key('.env', 'API_KEY', API_KEY)  # Enregistrer la clé dans le fichier .env
```
- **`os.getenv('API_KEY')`** : Tente d'obtenir la clé API à partir des variables d'environnement.
- Si la clé n'est pas trouvée, elle la demande à l'utilisateur via `input`.
- **`set_key('.env', 'API_KEY', API_KEY)`** : Enregistre la clé saisie dans le fichier `.env` pour une utilisation ultérieure.

#### 4.3. **Instructions pour le modèle**
```python
instructions: dict = {
    '1': 'system_instruction_asterisk',
    '2': 'system_instruction_tilde',
    '3': 'system_instruction_hash',
}
```
- Dictionnaire contenant les noms des fichiers avec les instructions pour le modèle.

#### 4.4. **Salutation de l'utilisateur**
```python
print('Bienvenue dans le jeu Banner !')
print('Entrez du texte, et je créerai une bannière textuelle pour vous.')
```
- Salue l'utilisateur et explique la fonctionnalité du programme.

#### 4.5. **Boucle pour la sélection du style de bannière**
```python
while True:
    print('Sélectionnez le style de conception de la bannière :')
    print('1. Symbole 
*')
    print('2. Symbole 
~')
    print('3. Symbole 
#')
    choice = input('Entrez le numéro de style (1, 2 ou 3) : ')
```
- L'utilisateur sélectionne le style de conception de la bannière.

#### 4.6. **Lecture des instructions pour le modèle**
```python
if choice in ('1', '2', '3'):
    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # Lire l instruction du fichier
else:
    print('Choix invalide. Le style par défaut 
*
 est utilisé')
    system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # Lire l instruction par défaut
```
- Si le choix est valide, lire l linstruction correspondante du fichier.
- Si le choix est invalide, utiliser l instruction par défaut.

#### 4.7. **Création d une instance de classe**
```python
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
```
- Créer une instance de la classe `GoogleGenerativeAI` avec les paramètres spécifiés.

#### 4.8. **Demande de texte à l utilisateur**
```python
user_text: str = input('Entrez le texte pour la bannière : ')
```
- L utilisateur saisit le texte pour la bannière.

#### 4.9. **Validation du texte**
```python
if user_text.strip() == '':
    print('Vous n avez pas entré de texte. Veuillez réessayer.')
else:
    response = model.ask(user_text)
    print('
Votre bannière est prête :')
    print(response)
```
- Si le texte est vide, afficher un message d erreur.
- Si le texte est saisi, l envoyer au modèle et afficher le résultat.

```