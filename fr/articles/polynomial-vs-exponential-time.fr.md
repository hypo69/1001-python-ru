### **Temps Polynomial**

Le **temps polynomial** est un terme utilisé en théorie de la complexité computationnelle pour décrire le temps d'exécution d'un algorithme qui croît comme un polynôme de la taille des données d'entrée. Si le temps d'exécution d'un algorithme peut être exprimé comme \(O(n^k)\), où \(n\) est la taille des données d'entrée et \(k\) est une constante, alors un tel algorithme s'exécute en temps polynomial.

#### **Exemples :**
1. **Tri d'une liste** : Les algorithmes tels que le tri fusion ou le tri rapide s'exécutent en \(O(n \log n)\), ce qui est un temps polynomial.
2. **Recherche du chemin le plus court dans un graphe** : L'algorithme de Dijkstra s'exécute en \(O(n^2)\) ou \(O(n \log n)\) selon l'implémentation, ce qui est également polynomial.

#### **Caractéristiques :**
- Les algorithmes qui s'exécutent en temps polynomial sont considérés comme **efficaces** et **pratiquement applicables**.
- Les problèmes qui peuvent être résolus en temps polynomial appartiennent à la classe **P**.

---

### **Temps Exponentiel**

Le **temps exponentiel** est le temps d'exécution d'un algorithme qui croît exponentiellement en fonction de la taille des données d'entrée. Si le temps d'exécution peut être exprimé comme \(O(k^n)\), où \(n\) est la taille des données d'entrée et \(k\) est une constante, alors un tel algorithme s'exécute en temps exponentiel.

#### **Exemples :**
1. **Problème du voyageur de commerce** : La résolution par force brute de tous les chemins possibles nécessite un temps de \(O(n!)\), ce qui est pire qu'exponentiel.
2. **Itération sur tous les sous-ensembles** : Un algorithme qui vérifie tous les sous-ensembles possibles d'un ensemble de \(n\) éléments s'exécute en \(O(2^n)\).

#### **Caractéristiques :**
- Les algorithmes qui s'exécutent en temps exponentiel sont considérés comme **inefficaces** pour de grandes quantités de données d'entrée, car le temps d'exécution devient impraticablement grand même pour des valeurs de \(n\) relativement petites.
- Les problèmes qui ne peuvent être résolus qu'en temps exponentiel appartiennent souvent aux classes **NP-difficile** ou **NP-complet**.

---

### **Comparaison du temps polynomial et exponentiel**

| **Caractéristique** | **Temps polynomial** | **Temps exponentiel** |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Croissance du temps d'exécution** | Lente (ex. \(n^2\), \(n^3\)) | Rapide (ex. \(2^n\), \(3^n\)) |
| **Exemples de problèmes** | Tri, recherche du chemin le plus court | Problème du voyageur de commerce, énumération de sous-ensembles |
| **Applicabilité pratique** | Efficace pour les grandes données | Inapplicable pour les grandes données |
| **Classe de complexité** | P | NP-difficile, NP-complet |

---

### **Pourquoi est-ce important ?**

1. **Temps polynomial** :
   - Les algorithmes qui s'exécutent en temps polynomial sont considérés comme **pratiquement applicables** car ils peuvent traiter de grandes quantités de données dans un laps de temps raisonnable.
   - Les problèmes de la classe **P** (résolubles en temps polynomial) sont la base de nombreuses applications en informatique, telles que le traitement des données, les réseaux, la cryptographie et l'intelligence artificielle.

2. **Temps exponentiel** :
   - Les algorithmes qui s'exécutent en temps exponentiel deviennent **impraticables** même pour des données d'entrée relativement petites. Par exemple, pour \(n = 100\), \(2^n\) dépasse déjà le nombre d'atomes dans l'univers observable.
   - Les problèmes qui ne peuvent être résolus qu'en temps exponentiel nécessitent souvent l'utilisation de **méthodes d'approximation**, d'**heuristiques** ou de **calcul parallèle**.

---

### **Exemple pour comprendre**

Imaginez que vous avez un problème et que vous voulez le résoudre pour \(n = 10\) et \(n = 100\) :

- **Temps polynomial (\(n^2\))** :
  - Pour \(n = 10\) : \(10^2 = 100\) opérations.
  - Pour \(n = 100\) : \(100^2 = 10\,000\) opérations.

- **Temps exponentiel (\(2^n\))** :
  - Pour \(n = 10\) : \(2^{10} = 1\,024\) opérations.
  - Pour \(n = 100\) : \(2^{100} \approx 1.26 \times 10^{30}\) opérations.

Comme vous pouvez le voir, pour \(n = 100\), un algorithme polynomial effectuera 10 000 opérations, ce qui est tout à fait réaliste, tandis qu'un algorithme exponentiel nécessitera \(1.26 \times 10^{30}\) opérations, ce qui est pratiquement impossible.

Pour créer des graphiques illustrant la différence entre le temps polynomial et exponentiel, vous pouvez utiliser diverses fonctions mathématiques. Voici des exemples de fonctions qui peuvent être utilisées pour la visualisation :

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

5. **Fonction linéaire-logarithmique** :  
   \( f(n) = n \log n \)  
   Exemple : le temps d'exécution d'un tri rapide ou d'un tri fusion.

---

### **Fonctions exponentielles**
1. **Fonction exponentielle** :  
   \( f(n) = 2^n \)  
   Exemple : le temps d'exécution d'un algorithme qui itère sur tous les sous-ensembles d'un ensemble.

2. **Fonction factorielle** :  
   \( f(n) = n! \)  
   Exemple : le temps d'exécution d'un algorithme qui itère sur toutes les permutations (ex. le Problème du voyageur de commerce).

3. **Fonction exponentielle avec une base différente** :  
   \( f(n) = 3^n \)  
   Exemple : le temps d'exécution d'un algorithme qui explore toutes les combinaisons possibles.

---

### **Exemple de code pour tracer des graphiques (Python, Matplotlib)**

```python
import matplotlib.pyplot as plt
import numpy as np
import math # Import the standard math module

# Plage de valeurs de n
n = np.linspace(1, 20, 100)

# Fonctions polynomiales
linear = n
quadratic = n**2
cubic = n**3
logarithmic = np.log(n)
nlogn = n * np.log(n)

# Fonctions exponentielles
exponential = 2**n
# Utilise math.factorial du module math importé
factorial = [math.factorial(int(i)) for i in n]  # Factorielle est définie uniquement pour les entiers

# Tracé des graphiques
plt.figure(figsize=(10, 6))

# Fonctions polynomiales
plt.plot(n, linear, label='Linéaire: $f(n) = n$')
plt.plot(n, quadratic, label='Quadratique: $f(n) = n^2$')
plt.plot(n, cubic, label='Cubique: $f(n) = n^3$')
plt.plot(n, logarithmic, label='Logarithmique: $f(n) = \log n$')
plt.plot(n, nlogn, label='Linéaire-logarithmique: $f(n) = n \log n$')

# Fonctions exponentielles
plt.plot(n, exponential, label='Exponentielle: $f(n) = 2^n$')
plt.plot(n, factorial, label='Factorielle: $f(n) = n!$')

# Paramètres du graphique
plt.yscale('log')  # Échelle logarithmique pour plus de commodité
plt.xlabel('Taille d\'entrée (n)')
plt.ylabel('Complexité temporelle')
plt.title('Comparaison de la complexité temporelle polynomiale et exponentielle')
plt.legend()
plt.grid(True)
plt.show()
```

---
![Exponetialy](../assets/exponetialy.png)

### **Que montrera le graphique ?**
- Les **fonctions polynomiales** croissent lentement et restent en bas du graphique.
- Les **fonctions exponentielles** croissent très rapidement et montent même pour de petites valeurs de \(n\).
- L'utilisation d'une **échelle logarithmique** (sur l'axe Y) aide à visualiser la différence entre les fonctions polynomiales et exponentielles, car leurs valeurs diffèrent de plusieurs ordres de grandeur.

---