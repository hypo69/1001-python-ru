### **Temps polynomial**

**Le temps polynomial** est un terme utilisé en théorie de la complexité computationnelle pour décrire le temps d'exécution d'un algorithme qui croît comme un polynôme de la taille de l'entrée. Si le temps d'exécution d'un algorithme peut être exprimé comme \(O(n^k)\), où \(n\) est la taille de l'entrée et \(k\) est une constante, alors un tel algorithme s'exécute en temps polynomial.

#### **Exemples :**
1. **Tri d'une liste** : Les algorithmes tels que le tri fusion ou le tri rapide s'exécutent en \(O(n \log n)\), ce qui est un temps polynomial.
2. **Recherche du chemin le plus court dans un graphe** : L'algorithme de Dijkstra s'exécute en \(O(n^2)\) ou \(O(n \log n)\) selon l'implémentation, ce qui est également polynomial.

#### **Caractéristiques :**
- Les algorithmes s'exécutant en temps polynomial sont considérés comme **efficaces** et **pratiquement applicables**.
- Les problèmes qui peuvent être résolus en temps polynomial appartiennent à la classe **P**.

---

### **Temps exponentiel**

**Le temps exponentiel** est le temps d'exécution d'un algorithme qui croît de manière exponentielle en fonction de la taille de l'entrée. Si le temps d'exécution peut être exprimé comme \(O(k^n)\), où \(n\) est la taille de l'entrée et \(k\) est une constante, alors un tel algorithme s'exécute en temps exponentiel.

#### **Exemples :**
1. **Problème du voyageur de commerce** : La résolution par énumération exhaustive de tous les itinéraires possibles nécessite \(O(n!)\) temps, ce qui est pire qu'exponentiel.
2. **Énumération de tous les sous-ensembles** : Un algorithme qui vérifie tous les sous-ensembles possibles d'un ensemble de \(n\) éléments s'exécute en \(O(2^n)\).

#### **Caractéristiques :**
- Les algorithmes s'exécutant en temps exponentiel sont considérés comme **inefficaces** pour les grandes entrées, car le temps d'exécution devient trop important même pour des \(n\) relativement petits.
- Les problèmes qui ne peuvent être résolus qu'en temps exponentiel appartiennent souvent aux classes **NP-difficiles** ou **NP-complètes**.

---

### **Comparaison du temps polynomial et exponentiel**

| **Caractéristique**            | **Temps polynomial**               | **Temps exponentiel**               |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Croissance du temps d'exécution**   | Lente (par exemple, \(n^2\), \(n^3\)) | Rapide (par exemple, \(2^n\), \(3^n\))     |
| **Exemples de problèmes**             | Tri, recherche du chemin le plus court     | Problème du voyageur de commerce, énumération de sous-ensembles |
| **Applicabilité pratique** | Efficace pour les grandes données          | Inapplicable pour les grandes données            |
| **Classe de complexité**           | P                                      | NP-difficiles, NP-complètes                    |

---

### **Pourquoi est-ce important ?**

1. **Temps polynomial** :
   - Les algorithmes s'exécutant en temps polynomial sont considérés comme **pratiquement applicables**, car ils peuvent traiter de grands volumes de données dans un délai raisonnable.
   - Les problèmes de la classe **P** (résolubles en temps polynomial) constituent la base de nombreuses applications en informatique, telles que le traitement des données, les réseaux, la cryptographie et l'intelligence artificielle.

2. **Temps exponentiel** :
   - Les algorithmes s'exécutant en temps exponentiel deviennent **impraticables** même pour des entrées relativement petites. Par exemple, pour \(n = 100\), \(2^n\) dépasse déjà le nombre d'atomes dans l'Univers observable.
   - Les problèmes qui ne peuvent être résolus qu'en temps exponentiel nécessitent souvent l'utilisation de **méthodes approximatives**, d'**heuristiques** ou de **calculs parallèles**.

---

### **Exemple pour comprendre**

Imaginez que vous ayez un problème, et que vous vouliez le résoudre pour \(n = 10\) et \(n = 100\) :

- **Temps polynomial (\(n^2\))** :
  - Pour \(n = 10\) : \(10^2 = 100\) opérations.
  - Pour \(n = 100\) : \(100^2 = 10\,000\) opérations.

- **Temps exponentiel (\(2^n\))** :
  - Pour \(n = 10\) : \(2^{10} = 1\,024\) opérations.
  - Pour \(n = 100\) : \(2^{100} \approx 1.26 \times 10^{30}\) opérations.

Comme on peut le voir, pour \(n = 100\), un algorithme polynomial effectuera 10 000 opérations, ce qui est tout à fait réalisable, tandis qu'un algorithme exponentiel nécessitera \(1.26 \times 10^{30}\) opérations, ce qui est pratiquement impossible.

Pour tracer des graphiques illustrant la différence entre le temps polynomial et exponentiel, diverses fonctions mathématiques peuvent être utilisées. Voici des exemples de fonctions qui peuvent être utilisées pour la visualisation :

---

### **Fonctions polynomiales**
1. **Fonction linéaire** :  
   \( f(n) = n \)  
   Exemple : temps d'exécution d'un algorithme qui traite chaque élément une fois.

2. **Fonction quadratique** :  
   \( f(n) = n^2 \)  
   Exemple : temps d'exécution d'un algorithme avec des boucles imbriquées, comme le tri à bulles.

3. **Fonction cubique** :  
   \( f(n) = n^3 \)  
   Exemple : temps d'exécution d'un algorithme qui traite des données tridimensionnelles.

4. **Fonction logarithmique** :  
   \( f(n) = \log n \)  
   Exemple : temps d'exécution de la recherche binaire.

5. **Fonction linéaire-logarithmique** :  
   \( f(n) = n \log n \)  
   Exemple : temps d'exécution du tri rapide ou du tri fusion.

---

### **Fonctions exponentielles**
1. **Fonction exponentielle** :  
   \( f(n) = 2^n \)  
   Exemple : temps d'exécution d'un algorithme qui énumère tous les sous-ensembles d'un ensemble.

2. **Fonction factorielle** :  
   \( f(n) = n! \)  
   Exemple : temps d'exécution d'un algorithme qui énumère toutes les permutations (par exemple, le problème du voyageur de commerce).

3. **Fonction exponentielle avec une base différente** :  
   \( f(n) = 3^n \)  
   Exemple : temps d'exécution d'un algorithme qui explore toutes les combinaisons possibles.

---

### **Exemple de code pour tracer des graphiques (Python, Matplotlib)**

```python
import matplotlib.pyplot as plt
import numpy as np

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
factorial = [np.math.factorial(int(i)) for i in n]  # La factorielle n'est définie que pour les entiers

# Tracé des graphiques
plt.figure(figsize=(10, 6))

# Fonctions polynomiales
plt.plot(n, linear, label='Linéaire : $f(n) = n$')
plt.plot(n, quadratic, label='Quadratique : $f(n) = n^2$')
plt.plot(n, cubic, label='Cubique : $f(n) = n^3$')
plt.plot(n, logarithmic, label='Logarithmique : $f(n) = \log n$')
plt.plot(n, nlogn, label='Linéarithmique : $f(n) = n \log n$')

# Fonctions exponentielles
plt.plot(n, exponential, label='Exponentielle : $f(n) = 2^n$')
plt.plot(n, factorial, label='Factorielle : $f(n) = n!$')

# Paramètres du graphique
plt.yscale('log')  # Échelle logarithmique pour plus de commodité
plt.xlabel('Taille de l\'entrée (n)')
plt.ylabel('Complexité temporelle')
plt.title('Comparaison de la complexité temporelle polynomiale et exponentielle')
plt.legend()
plt.grid(True)
plt.show()
```

---

### **Que montrera le graphique ?**
- Les **fonctions polynomiales** croissent lentement et restent en bas du graphique.
- Les **fonctions exponentielles** croissent très rapidement et montent en flèche même pour de petites valeurs de \(n\).
- L'utilisation d'une **échelle logarithmique** (sur l'axe Y) aide à visualiser la différence entre les fonctions polynomiales et exponentielles, car leurs valeurs diffèrent de plusieurs ordres de grandeur.

---
