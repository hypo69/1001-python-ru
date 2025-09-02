### **Tiempo polinomial**

**El tiempo polinomial** es un término utilizado en la teoría de la complejidad computacional para describir el tiempo de ejecución de un algoritmo que crece como un polinomio del tamaño de la entrada. Si el tiempo de ejecución de un algoritmo se puede expresar como \(O(n^k)\), donde \(n\) es el tamaño de la entrada y \(k\) es una constante, entonces dicho algoritmo se ejecuta en tiempo polinomial.

#### **Ejemplos:**
1. **Ordenación de una lista**: Algoritmos como el de ordenación por mezcla o el de ordenación rápida se ejecutan en \(O(n \log n)\), lo que es tiempo polinomial.
2. **Búsqueda del camino más corto en un grafo**: El algoritmo de Dijkstra se ejecuta en \(O(n^2)\) o \(O(n \log n)\) dependiendo de la implementación, lo que también es polinomial.

#### **Características:**
- Los algoritmos que se ejecutan en tiempo polinomial se consideran **eficientes** y **prácticamente aplicables**.
- Los problemas que se pueden resolver en tiempo polinomial pertenecen a la clase **P**.

---

### **Tiempo exponencial**

**El tiempo exponencial** es el tiempo de ejecución de un algoritmo que crece exponencialmente con el tamaño de la entrada. Si el tiempo de ejecución se puede expresar como \(O(k^n)\), donde \(n\) es el tamaño de la entrada y \(k\) es una constante, entonces dicho algoritmo se ejecuta en tiempo exponencial.

#### **Ejemplos:**
1. **Problema del viajante de comercio**: La resolución por enumeración de fuerza bruta de todas las rutas posibles requiere \(O(n!)\) tiempo, lo que es peor que exponencial.
2. **Enumeración de todos los subconjuntos**: Un algoritmo que verifica todos los subconjuntos posibles de un conjunto de \(n\) elementos se ejecuta en \(O(2^n)\).

#### **Características:**
- Los algoritmos que se ejecutan en tiempo exponencial se consideran **ineficientes** para entradas grandes, ya que el tiempo de ejecución se vuelve impracticamente grande incluso para \(n\) relativamente pequeños.
- Los problemas que solo se pueden resolver en tiempo exponencial a menudo pertenecen a las clases **NP-difíciles** o **NP-completas**.

---

### **Comparación de tiempo polinomial y exponencial**

| **Característica**            | **Tiempo polinomial**               | **Tiempo exponencial**               |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Crecimiento del tiempo de ejecución**   | Lento (por ejemplo, \(n^2\), \(n^3\)) | Rápido (por ejemplo, \(2^n\), \(3^n\))     |
| **Ejemplos de problemas**             | Ordenación, búsqueda del camino más corto     | Problema del viajante de comercio, enumeración de subconjuntos |
| **Aplicabilidad práctica** | Eficiente para grandes datos          | Impracticable para grandes datos            |
| **Clase de complejidad**           | P                                      | NP-difíciles, NP-completas                    |

---

### **¿Por qué es esto importante?**

1. **Tiempo polinomial**:
   - Los algoritmos que se ejecutan en tiempo polinomial se consideran **prácticamente aplicables** porque pueden procesar grandes cantidades de datos en un tiempo razonable.
   - Los problemas de la clase **P** (resolubles en tiempo polinomial) son la base de muchas aplicaciones en informática, como el procesamiento de datos, las redes, la criptografía y la inteligencia artificial.

2. **Tiempo exponencial**:
   - Los algoritmos que se ejecutan en tiempo exponencial se vuelven **impracticables** incluso para entradas relativamente pequeñas. Por ejemplo, para \(n = 100\), \(2^n\) ya excede el número de átomos en el Universo observable.
   - Los problemas que solo se pueden resolver en tiempo exponencial a menudo requieren el uso de **métodos aproximados**, **heurísticas** o **computación paralela**.

---

### **Ejemplo para entender**

Imagine que tiene un problema y quiere resolverlo para \(n = 10\) y \(n = 100\):

- **Tiempo polinomial (\(n^2\))**:
  - Para \(n = 10\): \(10^2 = 100\) operaciones.
  - Para \(n = 100\): \(100^2 = 10\,000\) operaciones.

- **Tiempo exponencial (\(2^n\))**:
  - Para \(n = 10\): \(2^{10} = 1\,024\) operaciones.
  - Para \(n = 100\): \(2^{100} \approx 1.26 \times 10^{30}\) operaciones.

Como puede ver, para \(n = 100\), un algoritmo polinomial realizará 10.000 operaciones, lo cual es bastante factible, mientras que un algoritmo exponencial requerirá \(1.26 \times 10^{30}\) operaciones, lo cual es prácticamente imposible.

Para trazar gráficos que ilustren la diferencia entre el tiempo polinomial y exponencial, se pueden usar varias funciones matemáticas. Aquí hay ejemplos de funciones que se pueden usar para la visualización:

---

### **Funciones polinomiales**
1. **Función lineal**:  
   \( f(n) = n \)  
   Ejemplo: tiempo de ejecución de un algoritmo que procesa cada elemento una vez.

2. **Función cuadrática**:  
   \( f(n) = n^2 \)  
   Ejemplo: tiempo de ejecución de un algoritmo con bucles anidados, como la ordenación de burbuja.

3. **Función cúbica**:  
   \( f(n) = n^3 \)  
   Ejemplo: tiempo de ejecución de un algoritmo que procesa datos tridimensionales.

4. **Función logarítmica**:  
   \( f(n) = \log n \)  
   Ejemplo: tiempo de ejecución de la búsqueda binaria.

5. **Función lineal-logarítmica**:  
   \( f(n) = n \log n \)  
   Ejemplo: tiempo de ejecución de la ordenación rápida o la ordenación por mezcla.

---

### **Funciones exponenciales**
1. **Función exponencial**:  
   \( f(n) = 2^n \)  
   Ejemplo: tiempo de ejecución de un algoritmo que enumera todos los subconjuntos de un conjunto.

2. **Función factorial**:  
   \( f(n) = n! \)  
   Ejemplo: tiempo de ejecución de un algoritmo que enumera todas las permutaciones (por ejemplo, el problema del viajante de comercio).

3. **Función exponencial con una base diferente**:  
   \( f(n) = 3^n \)  
   Ejemplo: tiempo de ejecución de un algoritmo que explora todas las combinaciones posibles.

---

### **Ejemplo de código para trazar gráficos (Python, Matplotlib)**

```python
import matplotlib.pyplot as plt
import numpy as np

# Rango de valores de n
n = np.linspace(1, 20, 100)

# Funciones polinomiales
linear = n
quadratic = n**2
cubic = n**3
logarithmic = np.log(n)
nlogn = n * np.log(n)

# Funciones exponenciales
exponential = 2**n
factorial = [np.math.factorial(int(i)) for i in n]  # El factorial solo está definido para enteros

# Trazado de gráficos
plt.figure(figsize=(10, 6))

# Funciones polinomiales
plt.plot(n, linear, label='Lineal: $f(n) = n$')
plt.plot(n, quadratic, label='Cuadrática: $f(n) = n^2$')
plt.plot(n, cubic, label='Cúbica: $f(n) = n^3$')
plt.plot(n, logarithmic, label='Logarítmica: $f(n) = \log n$')
plt.plot(n, nlogn, label='Lineal-logarítmica: $f(n) = n \log n$')

# Funciones exponenciales
plt.plot(n, exponential, label='Exponencial: $f(n) = 2^n$')
plt.plot(n, factorial, label='Factorial: $f(n) = n!$')

# Configuración del gráfico
plt.yscale('log')  # Escala logarítmica para mayor comodidad
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Complejidad temporal')
plt.title('Comparación de la complejidad temporal polinomial y exponencial')
plt.legend()
plt.grid(True)
plt.show()
```

---

### **¿Qué mostrará el gráfico?**
- Las **funciones polinomiales** crecen lentamente y permanecen en la parte inferior del gráfico.
- Las **funciones exponenciales** crecen muy rápidamente y se disparan incluso para valores pequeños de \(n\).
- El uso de una **escala logarítmica** (en el eje Y) ayuda a visualizar la diferencia entre las funciones polinomiales y exponenciales, ya que sus valores difieren en órdenes de magnitud.

---
