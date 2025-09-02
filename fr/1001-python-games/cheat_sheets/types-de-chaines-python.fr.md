En Python, les chaînes de caractères sont l'un des types de données les plus importants et les plus fréquemment utilisés. Voici un bref aperçu des différents types de chaînes et de leurs caractéristiques :

---

### 1. **Chaînes de caractères ordinaires**
Une chaîne de caractères ordinaire est créée à l'aide de guillemets simples `'` ou doubles `"`.

**Exemple :**
```python
s1 = 'Bonjour, le monde !'
s2 = "Python, c'est génial !"
```

Elles sont identiques, mais il est important d'être cohérent dans l'utilisation d'un seul style.

---

### 2. **Chaînes de caractères multilignes**
Les chaînes de caractères multilignes sont encadrées par des guillemets triples `'''` ou `"""`. Elles vous permettent d'écrire du texte sur plusieurs lignes.

**Exemple :**
```python
s3 = '''Ceci est une chaîne
sur plusieurs
lignes.'''
```

---

### 3. **f-strings (chaînes formatées)**
Les f-strings (ou chaînes formatées) sont utilisées pour insérer des valeurs de variables et des expressions directement dans une chaîne. Le caractère `f` est ajouté avant la chaîne.

**Exemple :**
```python
name = 'Boris'
age = 25
s4 = f'Je m\'appelle {name}, j\'ai {age} ans.'
print(s4)  # Je m'appelle Boris, j'ai 25 ans.
```

L'avantage des f-strings est qu'elles sont simples et lisibles.
Dans les versions plus récentes de Python (à partir de **3.8**), une fonctionnalité pratique est apparue : l'utilisation de `f'{name=}'` dans les f-strings. Cette construction affiche non seulement la valeur de la variable, mais aussi son nom, ce qui est particulièrement utile pour le débogage.

### Exemple d'utilisation de `f'{name=}'` :
```python
name = 'Boris'
age = 25

# Afficher le nom de la variable et sa valeur
print(f'{name=}, {age=}')
# Résultat : name='Boris', age=25
```

### Caractéristiques :
1. **Affichage automatique du nom de la variable** :
   Python substitue automatiquement le nom de la variable et sa valeur, en les séparant par `=`. 
   
2. **Fonctionne avec des expressions** :
   Vous pouvez utiliser des expressions à l'intérieur d'une f-string, et elles seront également affichées. 

**Exemple :**
```python
x = 10
y = 5
print(f'{x + y=}')
# Résultat : x + y=15
```

3. **Applicable aux fonctions de chaîne** :
   Vous pouvez afficher le résultat de méthodes ou d'opérations sur des chaînes.

**Exemple :**
```python
s = 'Python'
print(f'{s.upper()=}')
# Résultat : s.upper()='PYTHON'
```

### Pourquoi c'est utile :
- **Débogage du code** : Vérifier rapidement les valeurs des variables et des expressions.
- **Lisibilité** : Voir clairement à quelle variable une valeur appartient.


---


### 4. **r-strings (chaînes brutes)**
Les r-strings (chaînes brutes) sont créées en ajoutant le caractère `r` avant la chaîne. Elles sont utilisées pour travailler avec des caractères qui sont généralement interprétés comme spéciaux, tels que les caractères de nouvelle ligne (`\n`) ou les tabulations (`\t`).

**Exemple :**
```python
s5 = r'C:\new_folder\test'
print(s5)  # C:\new_folder\test
```

Sans `r`, cette chaîne serait interprétée avec `\n` remplacé par un saut de ligne.

---


### 5. **u-strings (chaînes Unicode)**
Les u-strings étaient importantes dans Python 2 pour travailler avec Unicode, mais dans Python 3, les chaînes sont Unicode par défaut, donc l'ajout de `u` n'est plus nécessaire.

**Exemple :**
```python
s6 = u'Bonjour, le monde !'
```

---


### 6. **b-strings (chaînes d'octets)**
Les chaînes d'octets sont utilisées pour travailler avec des données binaires. Ces chaînes commencent par `b`. Elles ne prennent pas en charge les caractères Unicode, uniquement les octets.

**Exemple :**
```python
# Chaîne d'octets représentant l'en-tête d'un fichier PNG
image_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

# Vérifier que les données correspondent au format PNG
if image_bytes.startswith(b'\x89PNG'):
    print('Ceci est une image PNG.')
else:
    print('Format inconnu.')

```

---


### 7. **Chaînes avec échappement**
Pour inclure des caractères spéciaux dans une chaîne, des séquences d'échappement avec une barre oblique inverse (`\`) sont utilisées.

**Exemple :**
```python
s8 = 'Ceci est une chaîne avec des guillemets : \'simples\' et "doubles".'
```

---


### 8. **Combinaison de f-strings et r-strings**
Vous pouvez combiner les types de chaînes. Par exemple, les f-strings et les chaînes brutes : 

**Exemple :**
```python
path = 'new_folder'
s9 = fr'C:\{path}\test'
print(s9)  # C:\new_folder\test
```

---


### Résumé
En Python, les chaînes sont flexibles et pratiques. Le choix du type de chaîne dépend de la tâche : 
- Pour le texte ordinaire — `'` ou `"`.
- Pour le texte multiligne — `'''` ou `"""`.
- Pour la substitution de valeurs — `f`.
- Pour les chemins ou les expressions régulières — `r`.
- Pour les données binaires — `b`.

---

  [Vers la table des matières](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
