# Proyecto "Juego de la Vida"

## Breve descripción

Este proyecto es una implementación del autómata celular "Juego de la Vida" de Conway en Python. El juego simula la evolución de una población de células en una cuadrícula bidimensional, donde el estado de cada célula (viva o muerta) cambia en función del estado de sus vecinos.

## Estructura de archivos

-   `life.py`: El archivo principal que contiene la implementación de la clase `Game`, que gestiona la lógica de la simulación del "Juego de la Vida" y su visualización gráfica utilizando la biblioteca `pygame`.
-   `test_life.py`: Un archivo con pruebas unitarias para la clase `Game`, utilizando el framework `pytest`. Incluye una prueba para verificar la evolución del oscilador "Blinker".

## Cómo ejecutar la simulación

Para ejecutar la simulación del "Juego de la Vida", asegúrate de tener instaladas las bibliotecas necesarias (`numpy` y `pygame`). Si no es así, instálalas:

```bash
pip install numpy pygame
```

Luego ejecuta el archivo principal:

```bash
python game/life.py
```

## Cómo ejecutar las pruebas

Para ejecutar las pruebas, debes instalar `pytest` y `numpy`:

```bash
pip install pytest numpy
```

Luego ejecuta las pruebas, especificando la ruta al archivo de prueba:

```bash
pytest game/test_life.py
```