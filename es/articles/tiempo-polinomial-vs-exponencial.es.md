### **Tiempo polinomial**

El **tiempo polinomial** es un término utilizado en la teoría de la complejidad computacional para describir el tiempo de ejecución de un algoritmo que crece como un polinomio del tamaño de los datos de entrada. Si el tiempo de ejecución de un algoritmo se puede expresar como \(O(n^k)\), donde \(n\) es el tamaño de los datos de entrada y \(k\) es una constante, entonces dicho algoritmo se ejecuta en tiempo polinomial.

#### **Ejemplos:**
1. **Ordenar una lista**: Algoritmos como el ordenamiento por fusión o el ordenamiento rápido se ejecutan en \(O(n \log n)\), que es tiempo polinomial.
2. **Encontrar el camino más corto en un grafo**: El algoritmo de Dijkstra se ejecuta en \(O(n^2)\) o \(O(n \log n)\) dependiendo de la implementación, lo que también es polinomial.

#### **Características:**
- Los algoritmos que se ejecutan en tiempo polinomial se consideran **eficientes** y **prácticamente aplicables**.
- Los problemas que se pueden resolver en tiempo polinomial pertenecen a la clase **P**.

---

### **Tiempo exponencial**

El **tiempo exponencial** es el tiempo de ejecución de un algoritmo que crece exponencialmente en función del tamaño de los datos de entrada. Si el tiempo de ejecución se puede expresar como \(O(k^n)\), donde \(n\) es el tamaño de los datos de entrada y \(k\) es una constante, entonces dicho algoritmo se ejecuta en tiempo exponencial.

#### **Ejemplos:**
1. **Problema del viajante de comercio**: La resolución por fuerza bruta de todas las rutas posibles requiere un tiempo de \(O(n!)\), que es peor que exponencial.
2. **Iterar sobre todos los subconjuntos**: Un algoritmo que comprueba todos los subconjuntos posibles de un conjunto de \(n\) elementos se ejecuta en \(O(2^n)\).

#### **Características:**
- Los algoritmos que se ejecutan en tiempo exponencial se consideran **ineficientes** para grandes datos de entrada, ya que el tiempo de ejecución se vuelve impracticable incluso para \(n\) relativamente pequeños.
- Los problemas que solo se pueden resolver en tiempo exponencial a menudo pertenecen a las clases **NP-difícil** o **NP-completo**.

---

### **Comparación del tiempo polinomial y exponencial**

| **Característica** | **Tiempo polinomial** | **Tiempo exponencial** |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Crecimiento del tiempo de ejecución** | Lento (p. ej., \(n^2\), \(n^3\)) | Rápido (p. ej., \(2^n\), \(3^n\)) |
| **Ejemplos de problemas** | Ordenación, búsqueda del camino más corto | Problema del viajante de comercio, enumeración de subconjuntos |
| **Aplicabilidad práctica** | Eficiente para grandes datos | Inaplicable para grandes datos |
| **Clase de complejidad** | P | NP-difícil, NP-completo |

---

### **¿Por qué es importante?**

1. **Tiempo polinomial**:
   - Los algoritmos que se ejecutan en tiempo polinomial se consideran **prácticamente aplicables** porque pueden procesar grandes cantidades de datos en un tiempo razonable.
   - Los problemas de la clase **P** (resolubles en tiempo polinomial) son la base de muchas aplicaciones en ciencias de la computación, como el procesamiento de datos, las redes, la criptografía y la inteligencia artificial.

2. **Tiempo exponencial**:
   - Los algoritmos que se ejecutan en tiempo exponencial se vuelven **impracticables** incluso para datos de entrada relativamente pequeños. Por ejemplo, para \(n = 100\), \(2^n\) ya supera el número de átomos en el universo observable.
   - Los problemas que solo se pueden resolver en tiempo exponencial a menudo requieren el uso de **métodos de aproximación**, **heurísticas** o **computación paralela**.

---

### **Ejemplo para entender**

Imagina que tienes un problema y quieres resolverlo para \(n = 10\) y \(n = 100\):

- **Tiempo polinomial (\(n^2\))**:
  - Para \(n = 10\): \(10^2 = 100\) operaciones.
  - Para \(n = 100\): \(100^2 = 10\,000\) operaciones.

- **Tiempo exponencial (\(2^n\))**:
  - Para \(n = 10\): \(2^{10} = 1\,024\) operaciones.
  - Para \(n = 100\): \(2^{100} \approx 1.26 \times 10^{30}\) operaciones.

Como puedes ver, para \(n = 100\), un algoritmo polinomial realizará 10.000 operaciones, lo cual es bastante realista, mientras que un algoritmo exponencial requerirá \(1.26 \times 10^{30}\) operaciones, lo cual es prácticamente imposible.

Para crear gráficos que ilustren la diferencia entre el tiempo polinomial y el tiempo exponencial, puedes usar varias funciones matemáticas. Aquí hay ejemplos de funciones que se pueden usar para la visualización:

---

### **Funciones polinomiales**
1. **Función lineal**:  
   \( f(n) = n \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que procesa cada elemento una vez.

2. **Función cuadrática**:  
   \( f(n) = n^2 \)  
   Ejemplo: el tiempo de ejecución de un algoritmo con bucles anidados, por ejemplo, el ordenamiento de burbuja.

3. **Función cúbica**:  
   \( f(n) = n^3 \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que procesa datos tridimensionales.

4. **Función logarítmica**:  
   \( f(n) = \log n \)  
   Ejemplo: el tiempo de ejecución de una búsqueda binaria.

5. **Función lineal-logarítmica**:  
   \( f(n) = n \log n \)  
   Ejemplo: el tiempo de ejecución de un ordenamiento rápido o un ordenamiento por fusión.

---

### **Funciones exponenciales**
1. **Función exponencial**:  
   \( f(n) = 2^n \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que itera sobre todos los subconjuntos de un conjunto.

2. **Función factorial**:  
   \( f(n) = n! \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que itera sobre todas las permutaciones (por ejemplo, el problema del viajante de comercio).

3. **Función exponencial con una base diferente**:  
   \( f(n) = 3^n \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que explora todas las combinaciones posibles.

---

### **Ejemplo de código para trazar gráficos (Python, Matplotlib)**

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

### **¿Qué mostrará el gráfico?**
- Las **funciones polinomiales** crecen lentamente y permanecen en la parte inferior del gráfico.
- Las **funciones exponenciales** crecen muy rápidamente y se disparan incluso para valores pequeños de \(n\).
- El uso de una **escala logarítmica** (en el eje Y) ayuda a visualizar la diferencia entre las funciones polinomiales y exponenciales, ya que sus valores difieren en órdenes de magnitud.

---
