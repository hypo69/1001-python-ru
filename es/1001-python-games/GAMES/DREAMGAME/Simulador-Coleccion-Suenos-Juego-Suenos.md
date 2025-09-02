Autor del código original:
https://github.com/Mstislav95/CashFlow_101/blob/main/CashFlow_model.ipynb

https://ok4u.club/cashflow101-rules/

https://www.youtube.com/watch?v=sG_RWsvYT7k&ab_channel=MstislavEfimov


# Juego de los sueños: Simulador de recolección de "sueños"

## Descripción

Simulación de un juego en el que el jugador se mueve por el tablero de juego, lanzando dos dados de seis caras.
En algunas celdas del tablero hay "sueños" que el jugador puede "recolectar".
El objetivo del juego es comprender qué "sueños" son los más probables de recolectar según las reglas dadas.

## Reglas del juego

1.  El jugador comienza el juego en la posición inicial (asumimos que es 0).
2.  En un turno, el jugador lanza dos dados de seis caras y se mueve un número de celdas igual a la suma de los valores obtenidos.
3.  El tablero de juego tiene 48 celdas. Si el jugador se mueve más allá de la celda 48, regresa al principio, "dando la vuelta" al tablero (por ejemplo, si la posición actual es 47 y se lanza un 4, la nueva posición será 3).
4.  En algunas celdas (especificadas en la lista `dream_numbers`) hay "sueños".
5.  Si el jugador cae en una celda con un "sueño" y aún no la ha visitado en la iteración actual, el "sueño" se considera recolectado.
6.  El juego continúa durante un número de movimientos especificado (`moves`).
7.  El juego se simula un número de veces especificado (`num_iterations`).
8.  Como resultado del programa, se calcula la frecuencia de recolección de cada "sueño" y la probabilidad de su recolección.

## Características del código

*   **Modelado**: El código simula el movimiento del jugador en el tablero de juego usando lanzamientos de dados.
*   **Recolección de "Sueños"**: El código rastrea cuándo el jugador cae en celdas con "sueños" y cuenta su número.
*   **Análisis**: El programa analiza los resultados de la simulación y calcula la frecuencia y la probabilidad de recolectar cada "sueño".
*   **Clase `DreamGame`**: El código está encapsulado en la clase `DreamGame`, lo que lo hace más estructurado y reutilizable.
*   **Generación de nombres de sueños**: Los nombres de "sueños" se generan usando el modelo Gemini, lo que hace que cada juego sea único.
*   **Optimización**: El código está optimizado usando `collections.Counter` para contar frecuencias y generadores para iterar a través de simulaciones.

## Capacidades

*   **Personalización de parámetros**: Puede personalizar fácilmente el número de movimientos por juego (`moves`) y el número de simulaciones de juego (`num_iterations`).
*   **Nombres dinámicos**: Los nombres de "sueños" se generan dinámicamente usando el modelo Gemini, lo que agrega variedad al juego.
*   **Análisis de probabilidad**: La obtención de la probabilidad de recolectar cada "sueño" le permite analizar y comparar su disponibilidad.
*   **Extensibilidad**: El código es fácilmente extensible y se puede modificar para agregar nuevas mecánicas de juego.

## Desglose del código

### Clase `DreamGame`

La clase `DreamGame` encapsula toda la lógica del juego.

#### `__init__(self, dream_numbers: List[int], moves: int = 3, num_iterations: int = 100_000)`

Constructor de la clase que inicializa el juego:

*   `dream_numbers`: Lista de números que representan las posiciones de los "sueños".
*   `moves`: Número de movimientos por juego.
*   `num_iterations`: Número de simulaciones de juego.
*   `self.dreams`: Diccionario que mapea los números de los sueños a sus nombres. Se rellena usando `_generate_dream_names`.

#### `_generate_dream_names(self) -> None`

Método que genera nombres de "sueños" usando el modelo Gemini.

*   Forma una solicitud al modelo Gemini para generar un número específico de nombres de "sueños" únicos.
*   Procesa la respuesta y crea un diccionario `self.dreams`, mapeando el número de "sueño" a su nombre.
*   Genera un error si el modelo no devuelve texto o no puede generar el número de nombres requerido.

#### `_simulate_game(self) -> Counter[str]`

Método que simula un juego:

*   Inicializa un contador `dreams_frequency` para rastrear la frecuencia de recolección de "sueños".
*   Inicializa la variable `square`, que representa la posición actual del jugador en el tablero, y `visited_dreams` para rastrear los sueños recolectados.
*   Realiza un número específico de movimientos (`moves`), moviendo al jugador por el tablero de juego.
*   Si el jugador cae en una celda con un "sueño" y aún no la ha visitado, incrementa el contador para ese "sueño".
*   Devuelve un objeto `Counter` con la frecuencia de recolección de "sueños".

#### `run_experiment(self) -> pd.DataFrame`

Método que ejecuta la simulación del juego varias veces y devuelve un DataFrame con los resultados:

*   Ejecuta la simulación del juego un número de veces especificado (`num_iterations`).
*   Suma las frecuencias de recolección de "sueños" de cada simulación.
*   Convierte los resultados a un DataFrame, donde las columnas son "Sueño" y "Frecuencia".
*   Ordena el DataFrame por frecuencia en orden descendente.
*   Agrega una columna "Probabilidad", calculada como la relación entre la "Frecuencia" y el número total de simulaciones.
*   Devuelve un DataFrame con los resultados.

### Uso

Al final del script, se crea una instancia de la clase `DreamGame` y se ejecuta el experimento. El resultado se imprime en la pantalla como un DataFrame.

```python
if __name__ == '__main__':
    dream_numbers = [1, 3, 5, 7, 10, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]
    game = DreamGame(dream_numbers, moves=3, num_iterations=10_000)
    df_result = game.run_experiment()
    print(df_result)
```

## Requisitos

*   Python 3.6+
*   Bibliotecas: `pandas`, `google-generativeai`
*   Variable de entorno `GOOGLE_API_KEY` con su clave API de Gemini

## Instalación

1.  Instale Python 3.6+
2.  Instale las bibliotecas: `pip install pandas google-generativeai`
3.  Establezca la variable de entorno `GOOGLE_API_KEY` con su clave API de Gemini.
4.  Ejecute el script `python your_script_name.py`

## Ejemplos de uso
```python
    dream_numbers = [2,4,8,16,32,44]
    game = DreamGame(dream_numbers, moves=5, num_iterations=1000)
    df_result = game.run_experiment()
    print(df_result)
```
En este ejemplo: 
 * Se crea un objeto de juego
 * Se simulan 10.000 juegos con tres movimientos
 * El resultado de la simulación se muestra como un DataFrame de pandas.

```python
    dream_numbers = [2,4,8,16,32,44]
    game = DreamGame(dream_numbers, moves=5, num_iterations=1000)
    df_result = game.run_experiment()
    print(df_result)
```
En este ejemplo: 
 * Se crea un objeto de juego con diferentes números de sueños
 * Se simulan 1000 juegos con cinco movimientos
 * El resultado de la simulación se muestra como un DataFrame de pandas.

## Licencia

MIT
