# Fonctions en Python

Les fonctions en langage Python sont des blocs de code nommés qui exécutent une tâche spécifique. Elles permettent d'organiser le code, de le rendre plus structuré et plus facile à réutiliser.

# Table des matières

1. [Déclaration de fonction](#déclaration-de-fonction)
2. [Paramètres de fonction](#paramètres-de-fonction)
   - [Types de paramètres](#types-de-paramètres)
3. [Retour de valeur](#retour-de-valeur)
4. [Variables locales et globales](#variables-locales-et-globales)
5. [Fonctions imbriquées](#fonctions-imbriquées)
6. [Récursivité](#récursivité)
7. [Gestion des exceptions avec `try` et `except`](#gestion-des-exceptions-avec-try-et-except)
8. [Exemple d'utilisation de fonctions](#exemple-d'utilisation-de-fonctions)

## Déclaration de fonction

Une fonction est déclarée à l'aide du mot-clé `def`, suivi du nom de la fonction, d'une liste de paramètres entre parenthèses et de deux points. Le corps de la fonction est écrit avec une indentation.

```python
def nom_fonction(paramètres):
    # actions
    return résultat
```

### Exemple :
```python
def addition(a: int, b: int) -> int:
    """Renvoie la somme de deux nombres."""
    return a + b
```

Ici :
- `a: int` et `b: int` — paramètres de fonction avec annotations de type.
- `-> int` — annotation de type de la valeur de retour.

## Paramètres de fonction

Les fonctions peuvent accepter des paramètres, qui représentent les données d'entrée. Ils sont spécifiés entre parenthèses après le nom de la fonction.

Exemple avec un paramètre :
```python
def salutation(nom: str) -> str:
    """Salue l'utilisateur par son nom."""
    return f"Bonjour, {nom}!"
```

### Types de paramètres :
1. **Paramètres obligatoires** — doivent être passés lors de l'appel de la fonction.
2. **Paramètres facultatifs** — peuvent avoir des valeurs par défaut.
   ```python
   def salutation(nom: str, age: int = 18) -> str:
       return f"Bonjour, {nom}! Tu as {age} ans."
   ```

## Retour de valeur

Une fonction peut renvoyer une valeur à l'aide du mot-clé `return`. Si `return` n'est pas utilisé, la fonction renvoie par défaut `None`.

Exemple :
```python
def multiplication(a: int, b: int) -> int:
    """Renvoie le produit de deux nombres."""
    return a * b
```

## Variables locales et globales

- **Variable locale** — est une variable qui n'existe qu'à l'intérieur d'une fonction. Elle est créée et détruite à chaque appel de fonction.
- **Variable globale** — est une variable accessible dans tout le code, y compris les fonctions.

Exemple d'utilisation d'une variable globale :
```python
x = 10  # Variable globale

def afficher_x() -> int:
    return x  # Accès à la variable globale
```

Si vous devez modifier une variable globale à l'intérieur d'une fonction, vous devez utiliser le mot-clé `global` :
```python
x = 10  # Variable globale

def modifier_x() -> None:
    global x
    x = 20
```

## Fonctions imbriquées

En Python, les fonctions peuvent être imbriquées, c'est-à-dire qu'une fonction peut être définie à l'intérieur d'une autre. Une fonction imbriquée peut accéder aux variables de la fonction externe.

Exemple :
```python
def externe(a: int, b: int) -> int:
    """Fonction qui utilise une fonction imbriquée pour calculer la différence."""
    
    def imbriquee(x: int, y: int) -> int:
        """Fonction imbriquée qui renvoie la différence."""
        return x - y
    
    return imbriquee(a, b)
```

## Récursivité

La récursivité, c'est quand une fonction s'appelle elle-même. C'est utile pour les tâches qui peuvent être décomposées en tâches plus petites et similaires (par exemple, la factorielle).

Exemple de récursivité :
```python
def factorielle(n: int) -> int:
    """Calcule la factorielle d'un nombre en utilisant la récursivité."""
    if n == 0:
        return 1  # Cas de base
    return n * factorielle(n - 1)  # Appel récursif
```

## Gestion des exceptions avec `try` et `except`

Python fournit un mécanisme de gestion des erreurs à l'aide des blocs `try` et `except`. Le code susceptible de provoquer une erreur est placé dans le bloc `try`, et les erreurs sont gérées dans le bloc `except`.

Exemple de gestion des erreurs :
```python
def division(a: int, b: int) -> float:
    """Divise un nombre par un autre, en gérant les erreurs possibles."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Erreur : division par zéro"
    except Exception as e:
        return f"Une erreur s'est produite : {e}"
    return result
```

Ici :
- Le bloc `try` tente d'effectuer l'opération de division.
- Le bloc `except ZeroDivisionError` intercepte l'erreur de division par zéro.
- Le bloc `except Exception as e` intercepte les autres exceptions et affiche un message d'erreur.

## Exemple d'utilisation de fonctions

```python
# Addition de deux nombres
print(addition(5, 3))  # 8

# Fonction imbriquée
print(externe(10, 4))  # 6

# Récursivité pour le calcul de la factorielle
print(factorielle(5))  # 120

# Gestion des exceptions lors de la division
print(division(10, 2))  # 5.0
print(division(10, 0))  # Erreur : division par zéro
```
---

  [Vers la table des matières](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
