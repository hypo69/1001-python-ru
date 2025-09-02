Dans le répertoire `game`, en utilisant le contexte du fichier @life.py, créez un fichier avec des tests `test_life.py`. Utilisez le framework pytest.

Le test doit vérifier la bonne évolution d'un simple oscillateur "Blinker" (trois cellules d'affilée).

Scénario de test :
1.  Importez la classe `Game` de `life`.
2.  Créez une fonction de test, par exemple `test_blinker_oscillation`.
3.  Dans le test, créez une instance `Game` avec une taille fixe (par exemple, 5x5).
4.  Définissez manuellement l'état initial du champ de manière à ce qu'il y ait une ligne horizontale de trois cellules vivantes (Blinker) au centre.
5.  Appelez la méthode `game.step()`.
6.  À l'aide de `assert` et `numpy.array_equal`, vérifiez que le champ a changé en une ligne verticale de trois cellules.
7.  Appelez la méthode `game.step()` encore une fois.
8.  Vérifiez que le champ est revenu à son état horizontal d'origine.