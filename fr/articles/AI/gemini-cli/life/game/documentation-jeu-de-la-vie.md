# Projet "Jeu de la Vie"

## Brève description

Ce projet est une implémentation de l'automate cellulaire "Jeu de la Vie" de Conway en Python. Le jeu simule l'évolution d'une population de cellules sur une grille bidimensionnelle, où l'état de chaque cellule (vivante ou morte) change en fonction de l'état de ses voisins.

## Structure des fichiers

-   `life.py`: Le fichier principal contenant l'implémentation de la classe `Game`, qui gère la logique de la simulation "Jeu de la Vie" et sa visualisation graphique à l'aide de la bibliothèque `pygame`.
-   `test_life.py`: Un fichier avec des tests unitaires pour la classe `Game`, utilisant le framework `pytest`. Comprend un test pour vérifier l'évolution de l'oscillateur "Blinker".

## Comment exécuter la simulation

Pour exécuter la simulation "Jeu de la Vie", assurez-vous d'avoir les bibliothèques nécessaires (`numpy` et `pygame`) installées. Si ce n'est pas le cas, installez-les :

```bash
pip install numpy pygame
```

Ensuite, exécutez le fichier principal :

```bash
python game/life.py
```

## Comment exécuter les tests

Pour exécuter les tests, vous devez installer `pytest` et `numpy` :

```bash
pip install pytest numpy
```

Ensuite, exécutez les tests, en spécifiant le chemin d'accès au fichier de test :

```bash
pytest game/test_life.py
```