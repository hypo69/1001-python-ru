### **Tempo Polinomiale**

Il **tempo polinomiale** è un termine usato nella teoria della complessità computazionale per descrivere il tempo di esecuzione di un algoritmo che cresce come un polinomio della dimensione dei dati di input. Se il tempo di esecuzione di un algoritmo può essere espresso come \(O(n^k)\), dove \(n\) è la dimensione dei dati di input e \(k\) è una costante, allora tale algoritmo viene eseguito in tempo polinomiale.

#### **Esempi:**
1. **Ordinamento di una lista**: Algoritmi come il merge sort o il quicksort vengono eseguiti in \(O(n \log n)\), che è tempo polinomiale.
2. **Ricerca del percorso più breve in un grafo**: L'algoritmo di Dijkstra viene eseguito in \(O(n^2)\) o \(O(n \log n)\) a seconda dell'implementazione, che è anch'esso polinomiale.

#### **Caratteristiche:**
- Gli algoritmi che vengono eseguiti in tempo polinomiale sono considerati **efficienti** e **praticamente applicabili**.
- I problemi che possono essere risolti in tempo polinomiale appartengono alla classe **P**.

--- 

### **Tempo Esponenziale**

Il **tempo esponenziale** è il tempo di esecuzione di un algoritmo che cresce esponenzialmente a seconda della dimensione dei dati di input. Se il tempo di esecuzione può essere espresso come \(O(k^n)\), dove \(n\) è la dimensione dei dati di input e \(k\) è una costante, allora tale algoritmo viene eseguito in tempo esponenziale.

#### **Esempi:**
1. **Problema del commesso viaggiatore**: La risoluzione per forza bruta di tutti i percorsi possibili richiede \(O(n!)\) tempo, il che è peggio dell'esponenziale.
2. **Iterazione su tutti i sottoinsiemi**: Un algoritmo che controlla tutti i possibili sottoinsiemi di un insieme di \(n\) elementi viene eseguito in \(O(2^n)\).

#### **Caratteristiche:**
- Gli algoritmi che vengono eseguiti in tempo esponenziale sono considerati **inefficienti** per grandi dati di input, poiché il tempo di esecuzione diventa impraticabilmente grande anche per \(n\) relativamente piccoli.
- I problemi che possono essere risolti solo in tempo esponenziale appartengono spesso alle classi **NP-difficile** o **NP-completo**.

--- 

### **Confronto tra tempo polinomiale ed esponenziale**

| **Caratteristica** | **Tempo Polinomiale** | **Tempo Esponenziale** |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Crescita del tempo di esecuzione** | Lenta (es. \(n^2\), \(n^3\)) | Rapida (es. \(2^n\), \(3^n\)) |
| **Esempi di problemi** | Ordinamento, ricerca del percorso più breve | Problema del commesso viaggiatore, enumerazione dei sottoinsiemi |
| **Applicabilità pratica** | Efficiente per grandi dati | Inapplicabile per grandi dati |
| **Classe di complessità** | P | NP-difficile, NP-completo |

--- 

### **Perché è importante?**

1. **Tempo polinomiale**:
   - Gli algoritmi che vengono eseguiti in tempo polinomiale sono considerati **praticamente applicabili** perché possono elaborare grandi quantità di dati in un tempo ragionevole.
   - I problemi della classe **P** (risolvibili in tempo polinomiale) sono la base per molte applicazioni nell'informatica, come l'elaborazione dei dati, le reti, la crittografia e l'intelligenza artificiale.

2. **Tempo esponenziale**:
   - Gli algoritmi che vengono eseguiti in tempo esponenziale diventano **impraticabili** anche per dati di input relativamente piccoli. Ad esempio, per \(n = 100\), \(2^n\) supera già il numero di atomi nell'universo osservabile.
   - I problemi che possono essere risolti solo in tempo esponenziale richiedono spesso l'uso di **metodi di approssimazione**, **euristiche** o **calcolo parallelo**.

--- 

### **Esempio per capire**

Immagina di avere un problema e di volerlo risolvere per \(n = 10\) e \(n = 100\):

- **Tempo polinomiale (\(n^2\))**:
  - Per \(n = 10\): \(10^2 = 100\) operazioni.
  - Per \(n = 100\): \(100^2 = 10\,000\) operazioni.

- **Tempo esponenziale (\(2^n\))**:
  - Per \(n = 10\): \(2^{10} = 1\,024\) operazioni.
  - Per \(n = 100\): \(2^{100} \approx 1.26 \times 10^{30}\) operazioni.

Come puoi vedere, per \(n = 100\) un algoritmo polinomiale eseguirà 10.000 operazioni, il che è abbastanza realistico, mentre un algoritmo esponenziale richiederà \(1.26 \times 10^{30}\) operazioni, il che è praticamente impossibile.

Per creare grafici che illustrano la differenza tra tempo polinomiale ed esponenziale, puoi usare varie funzioni matematiche. Ecco esempi di funzioni che possono essere usate per la visualizzazione:

--- 

### **Funzioni polinomiali**
1. **Funzione lineare**:  
   \( f(n) = n \)  
   Esempio: il tempo di esecuzione di un algoritmo che elabora ogni elemento una volta.

2. **Funzione quadratica**:  
   \( f(n) = n^2 \)  
   Esempio: il tempo di esecuzione di un algoritmo con cicli annidati, ad esempio, il bubble sort.

3. **Funzione cubica**:  
   \( f(n) = n^3 \)  
   Esempio: il tempo di esecuzione di un algoritmo che elabora dati tridimensionali.

4. **Funzione logaritmica**:  
   \( f(n) = \log n \)  
   Esempio: il tempo di esecuzione di una ricerca binaria.

5. **Funzione lineare-logaritmica**:  
   \( f(n) = n \log n \)  
   Esempio: il tempo di esecuzione di un quicksort o di un merge sort.

--- 

### **Funzioni esponenziali**
1. **Funzione esponenziale**:  
   \( f(n) = 2^n \)  
   Esempio: il tempo di esecuzione di un algoritmo che itera su tutti i sottoinsiemi di un insieme.

2. **Funzione fattoriale**:  
   \( f(n) = n! \)  
   Esempio: il tempo di esecuzione di un algoritmo che itera su tutte le permutazioni (es. il Problema del commesso viaggiatore).

3. **Funzione esponenziale con una base diversa**:  
   \( f(n) = 3^n \)  
   Esempio: il tempo di esecuzione di un algoritmo che esplora tutte le combinazioni possibili.

--- 

### **Codice di esempio per tracciare grafici (Python, Matplotlib)**

```python
import matplotlib.pyplot as plt
import numpy as np
import math # Importa il modulo math standard

# Intervallo di valori di n
n = np.linspace(1, 20, 100)

# Funzioni polinomiali
linear = n
quadratic = n**2
cubic = n**3
logarithmic = np.log(n)
nlogn = n * np.log(n)

# Funzioni esponenziali
exponential = 2**n
# Usa math.factorial dal modulo math importato
factorial = [math.factorial(int(i)) for i in n]  # Il fattoriale è definito solo per numeri interi

# Tracciamento dei grafici
plt.figure(figsize=(10, 6))

# Funzioni polinomiali
plt.plot(n, linear, label='Lineare: $f(n) = n$')
plt.plot(n, quadratic, label='Quadratica: $f(n) = n^2$')
plt.plot(n, cubic, label='Cubica: $f(n) = n^3$')
plt.plot(n, logarithmic, label='Logaritmica: $f(n) = \log n$')
plt.plot(n, nlogn, label='Lineare-logaritmica: $f(n) = n \log n$')

# Funzioni esponenziali
plt.plot(n, exponential, label='Esponenziale: $f(n) = 2^n$')
plt.plot(n, factorial, label='Fattoriale: $f(n) = n!$')

# Impostazioni del grafico
plt.yscale('log')  # Scala logaritmica per comodità
plt.xlabel('Dimensione input (n)')
plt.ylabel('Complessità temporale')
plt.title('Confronto della complessità temporale polinomiale ed esponenziale')
plt.legend()
plt.grid(True)
plt.show()
```

--- 
![Exponetialy](../assets/exponetialy.png)

### **Cosa mostrerà il grafico?**
- Le **funzioni polinomiali** crescono lentamente e rimangono nella parte inferiore del grafico.
- Le **funzioni esponenziali** crescono molto rapidamente e salgono anche per piccoli valori di \(n\).
- L'uso di una **scala logaritmica** (sull'asse Y) aiuta a visualizzare la differenza tra funzioni polinomiali ed esponenziali, poiché i loro valori differiscono di ordini di grandezza.

---