# La fonction `input()`
La fonction `input()` en Python est utilisée pour obtenir des données de l'utilisateur via une saisie de texte. Elle suspend l'exécution du programme jusqu'à ce que l'utilisateur saisisse des données et appuie sur Entrée. Ensuite, elle renvoie la valeur saisie sous forme de chaîne de caractères.

### Syntaxe
```python
input([invite])
```

- `invite` (facultatif) : une chaîne de caractères qui est affichée à l'utilisateur avant la saisie. Il peut s'agir d'un message avec des instructions, par exemple : `"Entrez votre nom : "`.

### Exemple d'utilisation
```python
# Demande du nom de l'utilisateur
name = input('Entrez votre nom : ')
print(f'Bonjour, {name}!')
```

**Résultat de l'exécution :**
```
Entrez votre nom : Alex
Bonjour, Alex!
```

### Caractéristiques
1. **Renvoie une chaîne de caractères**
   Toutes les données saisies via `input()` sont interprétées comme des chaînes de caractères. Si un nombre est nécessaire, il doit être converti :
   ```python
   age = int(input('Entrez votre âge : '))
   print(f'Votre âge : {age}')
   ```

2. **Gestion des erreurs**
   Pour éviter les erreurs lors de la conversion (par exemple, si l'utilisateur a saisi du texte au lieu d'un nombre), vous pouvez utiliser un bloc `try-except` :
   ```python
   try:
       number = int(input('Entrez un nombre : '))
       print(f'Vous avez entré le nombre {number}')
   except ValueError:
       print('Erreur : vous devez entrer un nombre.')
   ```

3. **Utilisation dans les boucles**
   Souvent, `input()` est utilisé dans les boucles pour demander des données de manière répétée :
   ```python
   while True:
       text = input('Entrez quelque chose (ou "quitter" pour terminer) : ')
       if text.lower() == 'quitter':
           print('Fin du programme.')
           break
       print(f'Vous avez entré : {text}')
   ```

### Conseils pour les débutants
- Assurez-vous que le type de données correspond à vos attentes (par exemple, convertissez la saisie en nombre si nécessaire).
- Validez toujours les données pour éviter les erreurs de saisie.
- Utilisez des messages d'`invite` clairs et concis afin que l'utilisateur comprenne ce qui lui est demandé.

---

  [Vers la table des matières](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
