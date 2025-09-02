Auteur du code original :
https://github.com/Mstislav95/CashFlow_101/blob/main/CashFlow_model.ipynb

https://ok4u.club/cashflow101-rules/

https://www.youtube.com/watch?v=sG_RWsvYT7k&ab_channel=MstislavEfimov


# Jeu de rêve : Simulateur de collecte de "rêves"

## Description

Simulation d'un jeu dans lequel le joueur se déplace sur le plateau de jeu, en lançant deux dés à six faces.
Sur certaines cases du plateau se trouvent des "rêves" que le joueur peut "collecter".
Le but du jeu est de comprendre quels "rêves" sont les plus susceptibles d'être collectés selon les règles données.

## Règles du jeu

1.  Le joueur commence la partie à la position initiale (supposons qu'elle est 0).
2.  En un tour, le joueur lance deux dés à six faces et se déplace d'un nombre de cases égal à la somme des valeurs obtenues.
3.  Le plateau de jeu a 48 cases. Si le joueur se déplace au-delà de la 48ème case, il revient au début, en "bouclant" autour du plateau (par exemple, si la position actuelle est 47 et qu'un 4 est lancé, la nouvelle position sera 3).
4.  Sur certaines cases (spécifiées dans la liste `dream_numbers`) se trouvent des "rêves".
5.  Si le joueur atterrit sur une case avec un "rêve" et ne l'a pas encore visitée dans l'itération actuelle, le "rêve" est considéré comme collecté.
6.  Le jeu continue pendant un nombre de coups spécifié (`moves`).
7.  Le jeu est simulé un nombre de fois spécifié (`num_iterations`).
8.  À la suite de l'exécution du programme, la fréquence de collecte de chaque "rêve" et la probabilité de sa collecte sont calculées.

## Fonctionnalités du code

*   **Modélisation** : Le code simule le mouvement du joueur sur le plateau de jeu à l'aide de lancers de dés.
*   **Collecte de "rêves"** : Le code suit le moment où le joueur atterrit sur des cases avec des "rêves" et compte leur nombre.
*   **Analyse** : Le programme analyse les résultats de la simulation et calcule la fréquence et la probabilité de collecte de chaque "rêve".
*   **Classe `DreamGame`** : Le code est encapsulé dans la classe `DreamGame`, ce qui le rend plus structuré et réutilisable.
*   **Génération de noms de rêves** : Les noms de "rêves" sont générés à l'aide du modèle Gemini, ce qui rend chaque jeu unique.
*   **Optimisation** : Le code est optimisé à l'aide de `collections.Counter` pour le comptage des fréquences et de générateurs pour l'itération à travers les simulations.

## Capacités

*   **Personnalisation des paramètres** : Vous pouvez facilement personnaliser le nombre de coups par partie (`moves`) et le nombre de simulations de jeu (`num_iterations`).
*   **Noms dynamiques** : Les noms de "rêves" sont générés dynamiquement à l'aide du modèle Gemini, ce qui ajoute de la variété au jeu.
*   **Analyse des probabilités** : L'obtention de la probabilité de collecte de chaque "rêve" vous permet d'analyser et de comparer leur disponibilité.
*   **Extensibilité** : Le code est facilement extensible et peut être modifié pour ajouter de nouvelles mécaniques de jeu.

## Analyse du code

### Classe `DreamGame`

La classe `DreamGame` encapsule toute la logique du jeu.

#### `__init__(self, dream_numbers: List[int], moves: int = 3, num_iterations: int = 100_000)`

Constructeur de la classe qui initialise le jeu :

*   `dream_numbers` : Liste de nombres représentant les positions des "rêves".
*   `moves` : Nombre de coups par partie.
*   `num_iterations` : Nombre de simulations de jeu.
*   `self.dreams` : Dictionnaire associant les numéros de rêves à leurs noms. Rempli à l'aide de `_generate_dream_names`.

#### `_generate_dream_names(self) -> None`

Méthode qui génère les noms de "rêves" à l'aide du modèle Gemini.

*   Forme une requête au modèle Gemini pour générer un nombre spécifié de noms de "rêves" uniques.
*   Traite la réponse et crée un dictionnaire `self.dreams`, associant le numéro de "rêve" à son nom.
*   Lève une erreur si le modèle ne renvoie pas de texte ou ne peut pas générer le nombre de noms requis.

#### `_simulate_game(self) -> Counter[str]`

Méthode qui simule une partie :

*   Initialise un compteur `dreams_frequency` pour suivre la fréquence de collecte des "rêves".
*   Initialise la variable `square`, représentant la position actuelle du joueur sur le plateau, et `visited_dreams` pour suivre les rêves collectés.
*   Effectue un nombre de coups spécifié (`moves`), déplaçant le joueur sur le plateau de jeu.
*   Si le joueur atterrit sur une case avec un "rêve" et ne l'a pas encore visitée, incrémente le compteur pour ce "rêve".
*   Renvoie un objet `Counter` avec la fréquence de collecte des "rêves".

#### `run_experiment(self) -> pd.DataFrame`

Méthode qui exécute la simulation du jeu plusieurs fois et renvoie un DataFrame avec les résultats :

*   Exécute la simulation du jeu un nombre de fois spécifié (`num_iterations`).
*   Additionne les fréquences de collecte de "rêves" de chaque simulation.
*   Convertit les résultats en un DataFrame, où les colonnes sont "Rêve" et "Fréquence".
*   Trie le DataFrame par fréquence dans l'ordre décroissant.
*   Ajoute une colonne "Probabilité", calculée comme le rapport de la "Fréquence" au nombre total de simulations.
*   Renvoie un DataFrame avec les résultats.

### Utilisation

À la fin du script, une instance de la classe `DreamGame` est créée et l'expérience est exécutée. Le résultat est affiché à l'écran sous forme de DataFrame.

```python
if __name__ == '__main__':
    dream_numbers = [1, 3, 5, 7, 10, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]
    game = DreamGame(dream_numbers, moves=3, num_iterations=10_000)
    df_result = game.run_experiment()
    print(df_result)
```

## Exigences

*   Python 3.6+
*   Bibliothèques : `pandas`, `google-generativeai`
*   Variable d'environnement `GOOGLE_API_KEY` avec votre clé API Gemini

## Installation

1.  Installer Python 3.6+
2.  Installer les bibliothèques : `pip install pandas google-generativeai`
3.  Définir la variable d'environnement `GOOGLE_API_KEY` avec votre clé API Gemini.
4.  Exécuter le script `python your_script_name.py`

## Exemples d'utilisation
```python
    dream_numbers = [2,4,8,16,32,44]
    game = DreamGame(dream_numbers, moves=5, num_iterations=1000)
    df_result = game.run_experiment()
    print(df_result)
```
Dans cet exemple : 
 * Un objet de jeu est créé
 * 10 000 parties sont simulées avec trois coups
 * Le résultat de la simulation est affiché sous forme de DataFrame pandas.

```python
    dream_numbers = [2,4,8,16,32,44]
    game = DreamGame(dream_numbers, moves=5, num_iterations=1000)
    df_result = game.run_experiment()
    print(df_result)
```
Dans cet exemple : 
 * Un objet de jeu est créé avec différents numéros de rêves
 * 1000 parties sont simulées avec cinq coups
 * Le résultat de la simulation est affiché sous forme de DataFrame pandas.

## Licence

MIT
