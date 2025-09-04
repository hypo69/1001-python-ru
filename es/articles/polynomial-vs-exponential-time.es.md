### **Tiempo Polinomial**

El **tiempo polinomial** es un término utilizado en la teoría de la complejidad computacional para describir el tiempo de ejecución de un algoritmo que crece como un polinomio del tamaño de los datos de entrada. Si el tiempo de ejecución de un algoritmo puede expresarse como \(O(n^k)\), donde \(n\) es el tamaño de los datos de entrada y \(k\) es una constante, entonces dicho algoritmo se ejecuta en tiempo polinomial.

#### **Ejemplos:**
1. **Ordenar una lista**: Algoritmos como merge sort o quicksort se ejecutan en \(O(n \log n)\), que es tiempo polinomial.
2. **Encontrar el camino más corto en un grafo**: El algoritmo de Dijkstra se ejecuta en \(O(n^2)\) o \(O(n \log n)\) dependiendo de la implementación, que también es polinomial.

#### **Características:**
- Los algoritmos que se ejecutan en tiempo polinomial se consideran **eficientes** y **prácticamente aplicables**.
- Los problemas que se pueden resolver en tiempo polinomial pertenecen a la clase **P**.

---

### **Tiempo Exponencial**

El **tiempo exponencial** es el tiempo de ejecución de un algoritmo que crece exponencialmente dependiendo del tamaño de los datos de entrada. Si el tiempo de ejecución puede expresarse como \(O(k^n)\), donde \(n\) es el tamaño de los datos de entrada y \(k\) es una constante, entonces dicho algoritmo se ejecuta en tiempo exponencial.

#### **Ejemplos:**
1. **Problema del vendedor viajero**: Resolver por fuerza bruta todas las rutas posibles requiere \(O(n!)\) tiempo, lo cual es peor que exponencial.
2. **Iterar sobre todos los subconjuntos**: Un algoritmo que verifica todos los subconjuntos posibles de un conjunto de \(n\) elementos se ejecuta en \(O(2^n)\).

#### **Características:**
- Los algoritmos que se ejecutan en tiempo exponencial se consideran **ineficientes** para grandes volúmenes de datos de entrada, ya que el tiempo de ejecución se vuelve imprácticamente grande incluso para valores de \(n\) relativamente pequeños.
- Los problemas que solo pueden resolverse en tiempo exponencial a menudo pertenecen a las clases **NP-hard** o **NP-complete**.

---

### **Comparación de Tiempo Polinomial y Exponencial**

| **Característica** | **Tiempo Polinomial** | **Tiempo Exponencial** |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Crecimiento del tiempo de ejecución** | Lento (ej., \(n^2\), \(n^3\)) | Rápido (ej., \(2^n\), \(3^n\)) |
| **Ejemplos de problemas** | Ordenación, búsqueda de camino más corto | Problema del vendedor viajero, enumeración de subconjuntos |
| **Aplicabilidad práctica** | Eficiente para grandes datos | Inaplicable para grandes datos |
| **Clase de complejidad** | P | NP-hard, NP-complete |

---

### **¿Por qué es esto importante?**

1. **Tiempo polinomial**:
   - Los algoritmos que se ejecutan en tiempo polinomial se consideran **prácticamente aplicables** porque pueden procesar grandes cantidades de datos en un tiempo razonable.
   - Los problemas de la clase **P** (resolubles en tiempo polinomial) son la base de muchas aplicaciones en ciencias de la computación, como el procesamiento de datos, redes, criptografía e inteligencia artificial.

2. **Tiempo exponencial**:
   - Los algoritmos que se ejecutan en tiempo exponencial se vuelven **impracticables** incluso para datos de entrada relativamente pequeños. Por ejemplo, para \(n = 100\), \(2^n\) ya supera el número de átomos en el universo observable.
   - Los problemas que solo pueden resolverse en tiempo exponencial a menudo requieren el uso de **métodos de aproximación**, **heurísticas** o **computación paralela**.

---

### **Ejemplo para entender**

Imagina que tienes un problema y quieres resolverlo para \(n = 10\) y \(n = 100\):

- **Tiempo polinomial (\(n^2\))**:
  - Para \(n = 10\): \(10^2 = 100\) operaciones.
  - Para \(n = 100\): \(100^2 = 10\,000\) operaciones.

- **Tiempo exponencial (\(2^n\))**:
  - Para \(n = 10\): \(2^{10} = 1\,024\) operaciones.
  - Para \(n = 100\): \(2^{100} \approx 1.26 \times 10^{30}\) operaciones.

Como puedes ver, para \(n = 100\), un algoritmo polinomial realizará 10,000 operaciones, lo cual es bastante realista, mientras que un algoritmo exponencial requerirá \(1.26 \times 10^{30}\) operaciones, lo cual es prácticamente imposible.

Para crear gráficos que ilustren la diferencia entre el tiempo polinomial y exponencial, puedes usar varias funciones matemáticas. Aquí tienes ejemplos de funciones que se pueden usar para la visualización:

---

### **Funciones polinomiales**
1. **Función lineal**:  
   \( f(n) = n \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que procesa cada elemento una vez.

2. **Función cuadrática**:  
   \( f(n) = n^2 \)  
   Ejemplo: el tiempo de ejecución de un algoritmo con bucles anidados, por ejemplo, ordenamiento de burbuja.

3. **Función cúbica**:  
   \( f(n) = n^3 \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que procesa datos tridimensionales.

4. **Función logarítmica**:  
   \( f(n) = \log n \)  
   Ejemplo: el tiempo de ejecución de una búsqueda binaria.

5. **Función lineal-logarítmica**:  
   \( f(n) = n \log n \)  
   Ejemplo: el tiempo de ejecución de un quicksort o merge sort.

---

### **Funciones exponenciales**
1. **Función exponencial**:  
   \( f(n) = 2^n \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que itera sobre todos los subconjuntos de un conjunto.

2. **Función factorial**:  
   \( f(n) = n! \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que itera sobre todas las permutaciones (ej., el Problema del Vendedor Viajero).

3. **Función exponencial con una base diferente**:  
   \( f(n) = 3^n \)  
   Ejemplo: el tiempo de ejecución de un algoritmo que explora todas las combinaciones posibles.

---

### **Código de ejemplo para graficar (Python, Matplotlib)**

```python
import matplotlib.pyplot as plt
import numpy as np
import math # Import the standard math module

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
# Usa math.factorial del módulo math importado
factorial = [math.factorial(int(i)) for i in n]  # Factorial se define solo para enteros

# Trazado de los gráficos
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
plt.title('Comparación de la Complejidad Temporal Polinomial y Exponencial')
plt.legend()
plt.grid(True)
plt.show()
```

---
![Exponetialy](../assets/exponetialy.png)

### **¿Qué mostrará el gráfico?**
- Las **funciones polinomiales** crecen lentamente y permanecen en la parte inferior del gráfico.
- Las **funciones exponenciales** crecen muy rápidamente y suben incluso para valores pequeños de \(n\).
- El uso de una **escala logarítmica** (en el eje Y) ayuda a visualizar la diferencia entre funciones polinomiales y exponenciales, ya que sus valores difieren en órdenes de magnitud.

---