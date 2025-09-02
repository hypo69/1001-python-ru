### **Scénario pour Gemini CLI : Le Jeu de la Vie**

#### **Étape 1 : Création de l'instruction système `GEMINI.MD`**
Dans le répertoire de travail, créez un fichier `GEMINI.md` et collez-y l'instruction système. Exemple d'instruction :
```markdown
## 📘 Instruction pour la génération de code Python

### 1. Règles générales

* Utilisez **Python 3.10+**.
* Respectez un **style de codage clair, lisible et sans ambiguïté**.
* **Chaque fonction, méthode et classe** doit avoir :

  * Des indications de type (`type hints`)
  * Une documentation complète et correcte au format `docstring` (voir section 3)
  * Des commentaires internes (`#`), si nécessaire

---

### 2. Commentaires

* Les commentaires doivent être **précis** et décrire **ce que fait le code**, et non « ce que nous faisons ».
* **Il est interdit** d'utiliser des pronoms : `nous faisons`, `nous retournons`, `nous envoyons`, `nous allons`, etc.
* **Seuls les termes sont autorisés** : `extraction`, `exécution`, `appel`, `remplacement`, `vérification`, `envoi`, `La fonction exécute`, `La fonction modifie la valeur`, etc.

#### ❌ Exemple de commentaire incorrect :

```python
# Nous obtenons la valeur du paramètre
```

#### ✅ Exemple de commentaire correct :

```python
# La fonction extrait la valeur du paramètre
```

---

### 3. Docstring (format de la documentation)

Chaque fonction/méthode/classe doit contenir un `docstring` au format suivant :

```python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Description du paramètre `param`.
        param1 (Optional[str | dict | str], optional): Description du paramètre `param1`. La valeur par défaut est `None`.

    Returns:
        dict | None: Description de la valeur de retour. Renvoie un dictionnaire ou `None`.

    Raises:
        SomeError: Description de la situation dans laquelle l'exception `SomeError` se produit.

    Example:
        >>> function('param', 'param1')
        {'param': 'param1'}
    """
```

* **Tous les paramètres et valeurs de retour doivent être décrits.**
* La formulation doit être **concise, précise et sans ambiguïté**.
* N'omettez pas la description des paramètres/valeurs de retour/exceptions.

---

### 4. Indications de type

* **Toutes les variables, paramètres et valeurs de retour** doivent être annotés.
* Utilisez la syntaxe de Python 3.10+ : `list[int]`, `dict[str, Any]`, `str | None`, etc.
* Exemples d'annotations correctes :

#### ✅ Types simples :

```python
name: str = "John"
count: int = 42
flag: bool = True
```

#### ✅ Collections et types complexes :

```python
from typing import Any, Optional, Callable, TypeAlias

coordinates: tuple[float, float] = (55.75, 37.61)
metadata: dict[str, Any] = {"debug": True}
UserId: TypeAlias = int
```

#### ✅ Fonctions et méthodes :

```python
def get_user_name(user_id: int) -> str:
    """Renvoie le nom de l'utilisateur par son identifiant."""
    ...
```

#### ✅ Fonctions asynchrones :

```python
async def fetch_users() -> AsyncIterator[dict[str, int | str]]:
    ...
```

#### ✅ Types génériques :

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value
```

---

### 5. Divers

* Utilisez `default_factory` dans `dataclass` pour les valeurs modifiables (`list`, `dict`).
* Pour les valeurs `Optional`, spécifiez `T | None` (Python 3.10+) ou `Optional[T]`.
* Pour les structures complexes, utilisez `TypeAlias`.

---

📌 **Conseil** : Lors de la génération de code, incluez toujours des indications de type, un `docstring` et évitez les formulations subjectives dans les commentaires. L'objectif est une structure de code aussi précise, reproductible et formalisée que possible.



Ce fichier sera utilisé pour configurer Gemini CLI.

Pour plus de commodité, nous allons créer un répertoire `game`, qui stockera les fichiers du projet, et un répertoire `scenarios`, où les scénarios pour Gemini CLI seront stockés.

Le fichier scenarios/life-create-code.md contiendra des instructions pour créer le code du jeu "La Vie",
le fichier scenarios/life-create-test.md - des instructions pour créer des tests,
et le fichier scenarios/life-create-doc.md - des instructions pour créer de la documentation.

life-create-code.md:
```markdown
À l'intérieur du répertoire `game`, créez un fichier life.py.
À l'intérieur, écrivez une implémentation du "Jeu de la Vie" de Conway en Python, en utilisant une approche orientée objet.
utilisez les bibliothèques : `numpy`, `pygame` (pour les graphiques).


Exigences :
1.  Créez une classe `Game`.
2.  Dans `__init__`, la classe doit prendre les dimensions de la grille (largeur, hauteur) et créer un champ initial aléatoire.
3.  Créez une méthode `step()` qui met à jour l'état du jeu d'une étape selon les règles :
    - Une cellule vivante avec < 2 voisins vivants meurt (solitude).
    - Une cellule vivante avec 2 ou 3 voisins vivants survit.
    - Une cellule vivante avec > 3 voisins vivants meurt (surpopulation).
    - Une cellule morte avec exactement 3 voisins vivants devient une cellule vivante (naissance).
4.  Créez une méthode `display()` ou redéfinissez `__str__` pour afficher le champ dans la console. Utilisez des symboles, par exemple '■' pour une cellule vivante et ' ' pour une cellule morte.
5.  Utilisez la bibliothèque `numpy` pour un travail efficace avec la grille.
6.  Dans le bloc `if __name__ == '__main__':`, ajoutez un exemple qui crée un jeu et, dans une boucle, exécute une simulation avec un petit délai entre les étapes.
7. Pour visualiser le jeu, utilisez pygame ou une autre bibliothèque graphique, si possible.
```

---

life-create-test.md:
```markdown
À l'intérieur du répertoire `game`, en utilisant le contexte du fichier @life.py, créez un fichier avec des tests test_life.py. Utilisez le framework pytest.

Le test doit vérifier l'exactitude de l'évolution d'un simple oscillateur "Clignotant" (trois cellules d'affilée).

Scénario de test :
1.  Importez la classe `Game` depuis `life`.
2.  Créez une fonction de test, par exemple `test_blinker_oscillation`.
3.  À l'intérieur du test, créez une instance de `Game` avec une taille fixe (par exemple, 5x5).
4.  Définissez manuellement l'état initial du champ de sorte qu'il y ait une ligne horizontale de trois cellules vivantes (Clignotant) au centre.
5.  Appelez la méthode `game.step()`.
6.  À l'aide de `assert` et `numpy.array_equal`, vérifiez que le champ est passé à une ligne verticale de trois cellules.
7.  Appelez à nouveau la méthode `game.step()`.
8.  Vérifiez que le champ est revenu à son état horizontal d'origine.
```

---

life-create-doc.md:
```markdown
Analysez les fichiers @life.py et @test_life.py à l'intérieur du répertoire `game` et, sur leur base, créez un fichier de documentation doc.md.

La structure de la documentation doit être la suivante :
-   **Titre :** # Projet "Jeu de la Vie"
-   **Brève description :** Une explication de ce qu'est ce projet (une implémentation de l'automate cellulaire de Conway).
-   **Structure des fichiers :** Une brève description de l'objectif des fichiers `life.py` et `test_life.py`.
-   **Comment exécuter la simulation :** Une section avec la commande pour exécuter le fichier principal (`python life.py`).
-   **Comment exécuter les tests :** Une section avec la commande pour exécuter les tests (`pip install pytest numpy`, puis `pytest`).
```

La structure des répertoires ressemblera à ceci :

![1](assets/gemini_cli_3/1.png)

#### **Étape 2 : Création du code du jeu "La Vie"**

Nous lançons gemini-cli dans le terminal :

![2](assets/gemini_cli_3/2.png)
Important ! Assurez-vous que vous vous trouvez dans le répertoire où se trouve le fichier `GEMINI.md`.

![3](assets/gemini_cli_3/3.png)

![4](assets/gemini_cli_3/4.png)

Nous donnons la permission de créer le fichier :
![5](assets/gemini_cli_3/5.png)

Après cela, gemini-cli générera le fichier `life.py` dans le répertoire `game` :
![6](assets/gemini_cli_3/6.png)

Nous continuons :
```bash
Créez un environnement virtuel venv, installez les dépendances nécessaires et exécutez le code du jeu    
```

![7](assets/gemini_cli_3/7.png)

Nous donnons les autorisations nécessaires pour exécuter les scripts
![8](assets/gemini_cli_3/8.png)

pip
![9](assets/gemini_cli_3/9.png)

et enfin gemini-cli lance le jeu :
![10](assets/gemini_cli_3/10.png)

Étape 3 : Création de tests

![12](assets/gemini_cli_3/12.png)
![11](assets/gemini_cli_3/11.png)

Erreur
![13](assets/gemini_cli_3/13.png)

gemini-cli essaie de résoudre le problème
![14](assets/gemini_cli_3/14.png)

![15](assets/gemini_cli_3/15.png)

La dernière étape consiste à créer la documentation
![16](assets/gemini_cli_3/16.png)

Voila ! La documentation a été créée :
![17](assets/gemini_cli_3/17.png)