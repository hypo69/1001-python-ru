# La fonction `print()`

La fonction `print()` en Python est utilisée pour afficher des informations dans la console. C'est l'une des fonctions les plus simples et les plus fréquemment utilisées, notamment pour le débogage et l'affichage de données. Examinons les principaux aspects de son fonctionnement.

## Syntaxe
```python
print(*objets, sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Paramètres :
1. **`*objets`** :
   - Une liste d'objets à afficher. Vous pouvez passer une ou plusieurs valeurs, séparées par des virgules.
   - Exemple :
     ```python
     print('Bonjour', 'monde')
     ```
     Résultat : `Bonjour monde`

2. **`sep`** (par défaut `' '`):
   - Le séparateur entre les objets, si plusieurs sont passés.
   - Exemple :
     ```python
     print('Bonjour', 'monde', sep=' - ')
     ```
     Résultat : `Bonjour - monde`

3. **`end`** (par défaut `'\n'`):
   - Spécifie ce qui sera ajouté à la fin de la ligne. Par défaut, c'est un saut de ligne.
   - Exemple :
     ```python
     print('Bonjour', end='!')
     ```
     Résultat : `Bonjour!`

4. **`file`**:
   - Le flux où la sortie sera dirigée (par défaut `sys.stdout` — sortie standard).
   - Exemple : sortie vers un fichier.
     ```python
     with open('output.txt', 'w') as f:
         print('Bonjour, fichier !', file=f)
     ```

5. **`flush`** (par défaut `False`):
   - Si défini sur `True`, force le vidage du tampon de sortie.

---

## Exemples d'utilisation

### Chaîne simple
```python
print('Hello, world!')
```
Résultat : `Hello, world!`

### Affichage de plusieurs valeurs
```python
name = 'Anna'
age = 25
print('Nom :', name, ', Âge :', age)
```
Résultat : `Nom : Anna , Âge : 25`

### Personnalisation du séparateur
```python
print(1, 2, 3, sep=' -> ')
```
Résultat : `1 -> 2 -> 3`

### Personnalisation de la fin de ligne
```python
for i in range(3):
    print(i, end=' ')
```
Résultat : `0 1 2`

### Utilisation des f-strings avec affichage du nom de variable
À partir de Python 3.8, vous pouvez utiliser les f-strings pour afficher les valeurs des variables avec leurs noms au format `nom=valeur`. C'est utile pour le débogage, car cela permet de voir immédiatement quelle variable et quelle valeur sont affichées.
```python
name = 'Ivan'
age = 30
print(f'{name=}, {age=}')
```
Résultat : `name='Ivan', age=30`

---

## Conseils utiles pour les débutants

1. **Débogage du code** :
   Utilisez `print()` pour vérifier les valeurs des variables :
   ```python
   x = 10
   y = 20
   print('Somme :', x + y)
   ```

2. **Affichage formaté** :
   Pour afficher des chaînes avec substitution de valeurs, il est préférable d'utiliser le formatage :
   ```python
   name = 'Ivan'
   age = 30
   print(f'Je m\'appelle {name}, j\'ai {age} ans.')
   ```

3. **Journalisation (Logging)** :
   Dans les grands projets, il est préférable d'utiliser le module `logging` pour la gestion de la sortie, mais au début, `print()` aide à afficher rapidement les données.

   ---

  [Vers la table des matières](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
