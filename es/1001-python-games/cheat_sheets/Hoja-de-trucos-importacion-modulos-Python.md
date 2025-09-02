# Importación de módulos en Python

La importación de bibliotecas en Python le permite usar módulos y funciones externos o propios, definidos en otros archivos o bibliotecas. Esto ayuda a organizar el código, mejorar su legibilidad y evitar la duplicación.

### ¿Qué son los módulos?
Un módulo en Python es simplemente un archivo con la extensión `.py` que contiene código (funciones, clases, variables, etc.). Cuando desea usar código de otro módulo, debe importarlo al archivo actual.

### Módulos externos e internos
1. **Módulos externos** — son módulos que no forman parte de la biblioteca estándar de Python y que deben instalarse por separado. Por ejemplo, módulos para trabajar con servidores web, procesamiento de datos o aprendizaje automático, como `numpy`, `requests` y otros.

2. **Módulos internos** — son módulos que ya están incluidos en la biblioteca estándar de Python. Por ejemplo, módulos para trabajar con archivos, tiempo, operaciones matemáticas: `os`, `math`, `datetime`.

### Instalación de módulos externos con pip
Para instalar un módulo externo, use el comando `pip` — es una herramienta para administrar paquetes de Python. Por ejemplo, para instalar la biblioteca `requests`, debe ejecutar el siguiente comando en la terminal:
```bash
pip install requests
```
Este comando descargará e instalará la biblioteca en su proyecto.

### Importación de módulos
Cuando desee usar un módulo en Python, debe importarlo:
1. **Importar el módulo completo**:
   ```python
   import os
   ```
   Después de esto, puede usar todas las funciones y variables del módulo, por ejemplo:
   ```python
   os.listdir()  # lista archivos en el directorio
   ```

2. **Importar elementos específicos de un módulo**:
   ```python
   from math import sqrt
   ```
   Ahora puede usar la función `sqrt` sin necesidad de referirse al módulo `math`.

3. **Importar con un alias**:
   ```python
   import pandas as pd
   ```
   En este caso, para usar las funciones de la biblioteca `pandas`, escribirá `pd` en lugar del nombre completo `pandas`.

### Importación de sus propios módulos
Si está escribiendo varios archivos en un proyecto, puede crear sus propios módulos. Por ejemplo, si tiene un archivo `utils.py` con funciones útiles, puede importarlo a otros archivos así:
```python
import utils
```
O importar una función específica:
```python
from utils import my_function
```

### ¿Por qué crear un módulo e importarlo en otras partes del proyecto?
1. **Organización del código**: La separación de la lógica en diferentes módulos ayuda a evitar el desorden en un proyecto grande. Por ejemplo, puede crear un módulo para el manejo de datos, otro para el procesamiento de solicitudes y un tercero para la interfaz.
   
2. **Reutilización del código**: Cuando la lógica se separa en módulos, se puede usar en diferentes partes del proyecto. Esto reduce la duplicación de código y facilita el mantenimiento.

3. **Legibilidad y mantenibilidad**: Cuando el código se separa en módulos, otros desarrolladores (o usted mismo en el futuro) podrán comprender y mantener el proyecto más fácilmente.

Ejemplo:
```python
# utils.py
def greet(name):
    return f"Hola, {name}!"
    
# main.py
from utils import greet

print(greet("Alice"))
```

En este ejemplo, la función `greet` se define en un módulo (`utils.py`), pero se usa en otro (`main.py`), lo que mejora la estructura y hace que el código sea más modular y fácil de modificar.

---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
