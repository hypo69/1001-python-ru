### **Polynomielle Zeit**

**Polynomielle Zeit** ist ein Begriff aus der Komplexitätstheorie, der die Ausführungszeit eines Algorithmus beschreibt, die als Polynom der Größe der Eingabedaten wächst. Wenn die Ausführungszeit eines Algorithmus als \(O(n^k)\) ausgedrückt werden kann, wobei \(n\) die Größe der Eingabedaten und \(k\) eine Konstante ist, dann läuft ein solcher Algorithmus in polynomieller Zeit.

#### **Beispiele:**
1. **Sortieren einer Liste**: Algorithmen wie Mergesort oder Quicksort laufen in \(O(n \log n)\), was polynomielle Zeit ist.
2. **Finden des kürzesten Pfades in einem Graphen**: Dijkstras Algorithmus läuft in \(O(n^2)\) oder \(O(n \log n)\) je nach Implementierung, was ebenfalls polynomiell ist.

#### **Merkmale:**
- Algorithmen, die in polynomieller Zeit laufen, gelten als **effizient** und **praktisch anwendbar**.
- Probleme, die in polynomieller Zeit gelöst werden können, gehören zur Klasse **P**.

---

### **Exponentielle Zeit**

**Exponentielle Zeit** ist die Ausführungszeit eines Algorithmus, die exponentiell in Abhängigkeit von der Größe der Eingabedaten wächst. Wenn die Ausführungszeit als \(O(k^n)\) ausgedrückt werden kann, wobei \(n\) die Größe der Eingabedaten und \(k\) eine Konstante ist, dann läuft ein solcher Algorithmus in exponentieller Zeit.

#### **Beispiele:**
1. **Problem des Handlungsreisenden**: Die Lösung durch Brute-Force aller möglichen Routen erfordert \(O(n!)\) Zeit, was schlechter als exponentiell ist.
2. **Iterieren über alle Teilmengen**: Ein Algorithmus, der alle möglichen Teilmengen einer Menge von \(n\) Elementen überprüft, läuft in \(O(2^n)\).

#### **Merkmale:**
- Algorithmen, die in exponentieller Zeit laufen, gelten als **ineffizient** für große Eingabedaten, da die Ausführungszeit selbst für relativ kleine \(n\) unpraktisch groß wird.
- Probleme, die nur in exponentieller Zeit gelöst werden können, gehören oft zu den **NP-schweren** oder **NP-vollständigen** Klassen.

---

### **Vergleich von polynomieller und exponentieller Zeit**

| **Merkmal** | **Polynomielle Zeit** | **Exponentielle Zeit** |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Wachstum der Ausführungszeit** | Langsam (z.B. \(n^2\), \(n^3\)) | Schnell (z.B. \(2^n\), \(3^n\)) |
| **Beispiele für Probleme** | Sortieren, kürzester Pfad | Problem des Handlungsreisenden, Teilmengenaufzählung |
| **Praktische Anwendbarkeit** | Effizient für große Daten | Unanwendbar für große Daten |
| **Komplexitätsklasse** | P | NP-schwer, NP-vollständig |

---

### **Warum ist das wichtig?**

1. **Polynomielle Zeit**:
   - Algorithmen, die in polynomieller Zeit laufen, gelten als **praktisch anwendbar**, da sie große Datenmengen in einer angemessenen Zeit verarbeiten können.
   - Probleme der Klasse **P** (lösbar in polynomieller Zeit) sind die Grundlage für viele Anwendungen in der Informatik, wie Datenverarbeitung, Netzwerke, Kryptographie und künstliche Intelligenz.

2. **Exponentielle Zeit**:
   - Algorithmen, die in exponentieller Zeit laufen, werden selbst für relativ kleine Eingabedaten **unpraktisch**. Zum Beispiel übersteigt für \(n = 100\) \(2^n\) bereits die Anzahl der Atome im beobachtbaren Universum.
   - Probleme, die nur in exponentieller Zeit gelöst werden können, erfordern oft die Verwendung von **Approximationsmethoden**, **Heuristiken** oder **Parallelverarbeitung**.

---

### **Beispiel zum Verständnis**

Stellen Sie sich vor, Sie haben ein Problem und möchten es für \(n = 10\) und \(n = 100\) lösen:

- **Polynomielle Zeit (\(n^2\))**:
  - Für \(n = 10\): \(10^2 = 100\) Operationen.
  - Für \(n = 100\): \(100^2 = 10\,000\) Operationen.

- **Exponentielle Zeit (\(2^n\))**:
  - Für \(n = 10\): \(2^{10} = 1\,024\) Operationen.
  - Für \(n = 100\): \(2^{100} \approx 1.26 \times 10^{30}\) Operationen.

Wie Sie sehen, wird ein polynomieller Algorithmus für \(n = 100\) 10.000 Operationen ausführen, was durchaus realistisch ist, während ein exponentieller Algorithmus \(1.26 \times 10^{30}\) Operationen erfordert, was praktisch unmöglich ist.

Um Graphen zu erstellen, die den Unterschied zwischen polynomieller und exponentieller Zeit veranschaulichen, können Sie verschiedene mathematische Funktionen verwenden. Hier sind Beispiele für Funktionen, die zur Visualisierung verwendet werden können:

---

### **Polynomielle Funktionen**
1. **Lineare Funktion**:  
   \( f(n) = n \)  
   Beispiel: die Ausführungszeit eines Algorithmus, der jedes Element einmal verarbeitet.

2. **Quadratische Funktion**:  
   \( f(n) = n^2 \)  
   Beispiel: die Ausführungszeit eines Algorithmus mit verschachtelten Schleifen, z.B. Bubblesort.

3. **Kubische Funktion**:  
   \( f(n) = n^3 \)  
   Beispiel: die Ausführungszeit eines Algorithmus, der dreidimensionale Daten verarbeitet.

4. **Logarithmische Funktion**:  
   \( f(n) = \log n \)  
   Beispiel: die Ausführungszeit einer binären Suche.

5. **Linear-logarithmische Funktion**:  
   \( f(n) = n \log n \)  
   Beispiel: die Ausführungszeit eines Quicksorts oder Mergesorts.

---

### **Exponentielle Funktionen**
1. **Exponentielle Funktion**:  
   \( f(n) = 2^n \)  
   Beispiel: die Ausführungszeit eines Algorithmus, der alle Teilmengen einer Menge durchläuft.

2. **Fakultätsfunktion**:  
   \( f(n) = n! \)  
   Beispiel: die Ausführungszeit eines Algorithmus, der alle Permutationen durchläuft (z.B. das Problem des Handlungsreisenden).

3. **Exponentielle Funktion mit einer anderen Basis**:  
   \( f(n) = 3^n \)  
   Beispiel: die Ausführungszeit eines Algorithmus, der alle möglichen Kombinationen untersucht.

---

### **Beispielcode zum Plotten von Graphen (Python, Matplotlib)**

```python
import matplotlib.pyplot as plt
import numpy as np
import math # Importiere das Standard-Math-Modul

# Bereich der n-Werte
n = np.linspace(1, 20, 100)

# Polynomielle Funktionen
linear = n
quadratic = n**2
cubic = n**3
logarithmic = np.log(n)
nlogn = n * np.log(n)

# Exponentielle Funktionen
exponential = 2**n
# Verwende math.factorial aus dem importierten math-Modul
factorial = [math.factorial(int(i)) for i in n]  # Fakultät ist nur für ganze Zahlen definiert

# Plotten der Graphen
plt.figure(figsize=(10, 6))

# Polynomielle Funktionen
plt.plot(n, linear, label='Linear: $f(n) = n$')
plt.plot(n, quadratic, label='Quadratisch: $f(n) = n^2$')
plt.plot(n, cubic, label='Kubisch: $f(n) = n^3$')
plt.plot(n, logarithmic, label='Logarithmisch: $f(n) = \log n$')
plt.plot(n, nlogn, label='Linearithmisch: $f(n) = n \log n$')

# Exponentielle Funktionen
plt.plot(n, exponential, label='Exponentiell: $f(n) = 2^n$')
plt.plot(n, factorial, label='Fakultät: $f(n) = n!$')

# Grapheinstellungen
plt.yscale('log')  # Logarithmische Skala zur besseren Übersicht
plt.xlabel('Eingabegröße (n)')
plt.ylabel('Zeitkomplexität')
plt.title('Vergleich von polynomieller und exponentieller Zeitkomplexität')
plt.legend()
plt.grid(True)
plt.show()
```

---
![Exponetialy](../assets/exponetialy.png)

### **Was zeigt der Graph?**
- **Polynomielle Funktionen** wachsen langsam und bleiben am unteren Rand des Graphen.
- **Exponentielle Funktionen** wachsen sehr schnell und steigen auch bei kleinen \(n\)-Werten stark an.
- Die Verwendung einer **logarithmischen Skala** (auf der Y-Achse) hilft, den Unterschied zwischen polynomiellen und exponentiellen Funktionen zu visualisieren, da ihre Werte um Größenordnungen variieren.

---
