# **Amazin** (Generador de laberintos)

#### Descripción
El juego es un generador de laberintos que crea un laberinto único con un solo camino correcto cada vez. El jugador establece las dimensiones del laberinto, y el programa lo construye de acuerdo con los parámetros especificados.

- **Características:**
  - El jugador ingresa el ancho y la altura del laberinto.
  - El programa garantiza un solo camino a través del laberinto.
  - El laberinto se muestra en la pantalla.

---

### Instrucciones paso a paso para la implementación:

#### 1. **Inicialización del juego**
   - Solicitar al jugador que ingrese las dimensiones del laberinto (ancho y alto).
   - Verificar que las dimensiones ingresadas sean válidas (por ejemplo, mayores que uno).

#### 2. **Lógica principal de generación del laberinto**
   - Crear una matriz del tamaño especificado, que represente una cuadrícula de celdas.
   - Usar un algoritmo de generación de laberintos, por ejemplo, el *algoritmo de búsqueda en profundidad recursiva (DFS)*:
     - Comenzar desde una celda inicial aleatoria.
     - Moverse a celdas adyacentes, eliminando paredes entre la celda actual y la siguiente.
     - Si todos los vecinos han sido visitados, retroceder a la celda anterior y continuar.
     - Completar el proceso cuando todas las celdas hayan sido visitadas.
   - Garantizar un solo camino a través del laberinto.

#### 3. **Visualización del laberinto**
   - Usar símbolos para la visualización:
     - `+`, `-`, `|` para las paredes.
     - Espacios para los pasajes.
   - Mostrar el laberinto generado en formato de texto.

#### 4. **Funciones adicionales**
   - Posibilidad de establecer un tamaño preestablecido (por ejemplo, 10x10) si el usuario ingresó datos no válidos.
   - Advertencia sobre tamaños de laberinto excesivamente grandes para evitar la sobrecarga de memoria.

---

### Ejemplo de ejecución del programa

1. **Inicio**:
   ```
   Ingrese el ancho y la altura del laberinto:
   > 10 8
   ```

2. **Salida del laberinto**:
   ```
   +--+--+--+--+--+--+--+--+--+--+
   |        |        |           |
   +  +--+  +  +--+  +  +--+--+  +
   |     |     |     |        |  |
   +--+  +  +--+  +  +  +--+  +  +
   |     |        |     |     |  |
   +--+--+--+--+--+--+--+--+--+--+
   ```

3. **Salir del programa**:
   ```
   ¿Generar un nuevo laberinto? (sí/no):
   > no
   ¡Adiós!
   ```

---