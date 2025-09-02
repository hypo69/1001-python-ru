### **Temps polynomial**

Le **temps polynomial** est un terme utilisé en théorie de la complexité algorithmique pour décrire le temps d'exécution d'un algorithme qui croît comme un polynôme de la taille des données d'entrée. Si le temps d'exécution d'un algorithme peut être exprimé comme \(O(n^k)\), où \(n\) est la taille des données d'entrée et \(k\) est une constante, alors un tel algorithme s'exécute en temps polynomial.

#### **Exemples :**
1. **Tri d'une liste** : Des algorithmes tels que le tri par fusion ou le tri rapide s'exécutent en \(O(n \log n)\), ce qui est un temps polynomial.
2. **Recherche du plus court chemin dans un graphe** : L'algorithme de Dijkstra s'exécute en \(O(n^2)\) ou \(O(n \log n)\) selon l'implémentation, ce qui est également polynomial.

#### **Caractéristiques :**
- Les algorithmes qui s'exécutent en temps polynomial sont considérés comme **efficaces** et **pratiquement applicables**.
- Les problèmes qui peuvent être résolus en temps polynomial appartiennent à la classe **P**.

---

### **Temps exponentiel**

Le **temps exponentiel** est le temps d'exécution d'un algorithme qui croît de manière exponentielle en fonction de la taille des données d'entrée. Si le temps d'exécution peut être exprimé comme \(O(k^n)\), où \(n\) est la taille des données d'entrée et \(k\) est une constante, alors un tel algorithme s'exécute en temps exponentiel.

#### **Exemples :**
1. **Problème du voyageur de commerce** : La résolution par force brute de tous les itinéraires possibles nécessite un temps de \(O(n!)\), ce qui est pire qu'exponentiel.
2. **Itération sur tous les sous-ensembles** : Un algorithme qui vérifie tous les sous-ensembles possibles d'un ensemble de \(n\) éléments s'exécute en \(O(2^n)\).

#### **Caractéristiques :**
- Les algorithmes qui s'exécutent en temps exponentiel sont considérés comme **inefficaces** pour les grandes données d'entrée, car le temps d'exécution devient impraticable même pour des \(n\) relativement petits.
- Les problèmes qui ne peuvent être résolus qu'en temps exponentiel appartiennent souvent aux classes **NP-difficiles** ou **NP-complets**.

---

### **Comparaison du temps polynomial et exponentiel**

| **Caractéristique** | **Temps polynomial** | **Temps exponentiel** |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Croissance du temps d'exécution** | Lente (par exemple, \(n^2\), \(n^3\)) | Rapide (par exemple, \(2^n\), \(3^n\)) |
| **Exemples de problèmes** | Tri, recherche du plus court chemin | Problème du voyageur de commerce, énumération de sous-ensembles |
| **Applicabilité pratique** | Efficace pour les grandes données | Inapplicable pour les grandes données |
| **Classe de complexité** | P | NP-difficile, NP-complet |

---

### **Pourquoi est-ce important ?**

1. **Temps polynomial** :
   - Les algorithmes qui s'exécutent en temps polynomial sont considérés comme **pratiquement applicables** car ils peuvent traiter de grandes quantités de données en un temps raisonnable.
   - Les problèmes de la classe **P** (résolubles en temps polynomial) sont à la base de nombreuses applications en informatique, telles que le traitement des données, les réseaux, la cryptographie et l'intelligence artificielle.

2. **Temps exponentiel** :
   - Les algorithmes qui s'exécutent en temps exponentiel deviennent **impraticables** même pour des données d'entrée relativement petites. Par exemple, pour \(n = 100\), \(2^n\) dépasse déjà le nombre d'atomes dans l'univers observable.
   - Les problèmes qui ne peuvent être résolus qu'en temps exponentiel nécessitent souvent l'utilisation de **méthodes d'approximation**, d'**heuristiques** ou de **calcul parallèle**.

---

### **Exemple pour comprendre**

Imaginez que vous ayez un problème et que vous vouliez le résoudre pour \(n = 10\) et \(n = 100\) :

- **Temps polynomial (\(n^2\))** :
  - Pour \(n = 10\) : \(10^2 = 100\) opérations.
  - Pour \(n = 100\) : \(100^2 = 10\,000\) opérations.

- **Temps exponentiel (\(2^n\))** :
  - Pour \(n = 10\) : \(2^{10} = 1\,024\) opérations.
  - Pour \(n = 100\) : \(2^{100} \approx 1.26 \times 10^{30}\) opérations.

Comme vous pouvez le voir, pour \(n = 100\), un algorithme polynomial effectuera 10 000 opérations, ce qui est tout à fait réaliste, tandis qu'un algorithme exponentiel nécessitera \(1.26 \times 10^{30}\) opérations, ce qui est pratiquement impossible.

Pour créer des graphiques illustrant la différence entre le temps polynomial et le temps exponentiel, vous pouvez utiliser diverses fonctions mathématiques. Voici des exemples de fonctions qui peuvent être utilisées pour la visualisation :

---

### **Fonctions polynomiales**
1. **Fonction linéaire** :  
   \( f(n) = n \)  
   Exemple : le temps d'exécution d'un algorithme qui traite chaque élément une fois.

2. **Fonction quadratique** :  
   \( f(n) = n^2 \)  
   Exemple : le temps d'exécution d'un algorithme avec des boucles imbriquées, par exemple, le tri à bulles.

3. **Fonction cubique** :  
   \( f(n) = n^3 \)  
   Exemple : le temps d'exécution d'un algorithme qui traite des données tridimensionnelles.

4. **Fonction logarithmique** :  
   \( f(n) = \log n \)  
   Exemple : le temps d'exécution d'une recherche binaire.

5. **Fonction quasi-linéaire** :  
   \( f(n) = n \log n \)  
   Exemple : le temps d'exécution d'un tri rapide ou d'un tri par fusion.

---

### **Fonctions exponentielles**
1. **Fonction exponentielle** :  
   \( f(n) = 2^n \)  
   Exemple : le temps d'exécution d'un algorithme qui parcourt tous les sous-ensembles d'un ensemble.

2. **Fonction factorielle** :  
   \( f(n) = n! \)  
   Exemple : le temps d'exécution d'un algorithme qui parcourt toutes les permutations (par exemple, le problème du voyageur de commerce).

3. **Fonction exponentielle avec une base différente** :  
   \( f(n) = 3^n \)  
   Exemple : le temps d'exécution d'un algorithme qui explore toutes les combinaisons possibles.

---

### **Exemple de code pour tracer des graphiques (Python, Matplotlib)**

```python
import matplotlib.pyplot as plt
import numpy as np
import math # Import the standard math module

# Range of n values
n = np.linspace(1, 20, 100)

# Polynomial functions
linear = n
quadratic = n**2
cubic = n**3
logarithmic = np.log(n)
nlogn = n * np.log(n)

# Exponential functions
exponential = 2**n
# Use math.factorial from the imported math module
factorial = [math.factorial(int(i)) for i in n]  # Factorial is defined only for integers

# Plotting the graphs
plt.figure(figsize=(10, 6))

# Polynomial functions
plt.plot(n, linear, label='Linear: $f(n) = n$')
plt.plot(n, quadratic, label='Quadratic: $f(n) = n^2$')
plt.plot(n, cubic, label='Cubic: $f(n) = n^3$')
plt.plot(n, logarithmic, label='Logarithmic: $f(n) = \log n$')
plt.plot(n, nlogn, label='Linearithmic: $f(n) = n \log n$')

# Exponential functions
plt.plot(n, exponential, label='Exponential: $f(n) = 2^n$')
plt.plot(n, factorial, label='Factorial: $f(n) = n!$')

# Graph settings
plt.yscale('log')  # Logarithmic scale for convenience
plt.xlabel('Input size (n)')
plt.ylabel('Time complexity')
plt.title('Comparison of Polynomial and Exponential Time Complexity')
plt.legend()
plt.grid(True)
plt.show()
```

---
![Exponetialy](../assets/exponetialy.png)

### **Que montrera le graphique ?**
- Les **fonctions polynomiales** croissent lentement et restent en bas du graphique.
- Les **fonctions exponentielles** croissent très rapidement et montent en flèche même pour de petites valeurs de \(n\).
- L'utilisation d'une **échelle logarithmique** (sur l'axe des Y) aide à visualiser la différence entre les fonctions polynomiales et exponentielles, car leurs valeurs diffèrent de plusieurs ordres de grandeur.

---