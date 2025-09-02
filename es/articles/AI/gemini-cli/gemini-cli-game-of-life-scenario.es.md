### **Escenario para Gemini CLI: Juego de la Vida**

#### **Paso 1: Creación de la instrucción del sistema `GEMINI.MD`**
En el directorio de trabajo, crea un archivo `GEMINI.md` y pega la instrucción del sistema en él. Ejemplo de instrucción:
```markdown
## 📘 Instrucción para generar código Python

### 1. Reglas generales

* Usa **Python 3.10+**.
* Sigue un **estilo de codificación claro, legible e inequívoco**.
* **Cada función, método y clase** debe tener:

  * Indicaciones de tipo (`type hints`)
  * Documentación completa y correcta en formato `docstring` (ver sección 3)
  * Comentarios internos (`#`), cuando sea necesario

---

### 2. Comentarios

* Los comentarios deben ser **precisos** y describir **qué hace el código**, no "qué estamos haciendo".
* **Está prohibido** usar pronombres: `hacemos`, `devolvemos`, `enviamos`, `vamos`, etc.
* **Solo se permiten términos**: `extracción`, `ejecución`, `llamada`, `reemplazo`, `verificación`, `envío`, `La función realiza`, `La función cambia el valor`, etc.

#### ❌ Ejemplo de un comentario incorrecto:

```python
# Obtenemos el valor del parámetro
```

#### ✅ Ejemplo de un comentario correcto:

```python
# La función extrae el valor del parámetro
```

---

### 3. Docstring (formato de la documentación)

Cada función/método/clase debe contener un `docstring` en el siguiente formato:

```python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Descripción del parámetro `param`.
        param1 (Optional[str | dict | str], optional): Descripción del parámetro `param1`. El valor predeterminado es `None`.

    Returns:
        dict | None: Descripción del valor de retorno. Devuelve un diccionario o `None`.

    Raises:
        SomeError: Descripción de la situación en la que se produce la excepción `SomeError`.

    Example:
        >>> function('param', 'param1')
        {'param': 'param1'}
    """
```

* **Todos los parámetros y valores de retorno deben estar descritos.**
* La redacción debe ser **concisa, precisa e inequívoca**.
* No omitas la descripción de los parámetros/valores de retorno/excepciones.

---

### 4. Indicaciones de tipo

* **Todas las variables, parámetros y valores de retorno** deben estar anotados.
* Usa la sintaxis de Python 3.10+: `list[int]`, `dict[str, Any]`, `str | None`, etc.
* Ejemplos de anotaciones correctas:

#### ✅ Tipos simples:

```python
name: str = "John"
count: int = 42
flag: bool = True
```

#### ✅ Colecciones y tipos complejos:

```python
from typing import Any, Optional, Callable, TypeAlias

coordinates: tuple[float, float] = (55.75, 37.61)
metadata: dict[str, Any] = {"debug": True}
UserId: TypeAlias = int
```

#### ✅ Funciones y métodos:

```python
def get_user_name(user_id: int) -> str:
    """Devuelve el nombre del usuario por su ID."""
    ...
```

#### ✅ Funciones asíncronas:

```python
async def fetch_users() -> AsyncIterator[dict[str, int | str]]:
    ...
```

#### ✅ Tipos genéricos:

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value
```

---

### 5. Varios

* Usa `default_factory` en `dataclass` para valores mutables (`list`, `dict`).
* Para valores `Optional`, especifica `T | None` (Python 3.10+) u `Optional[T]`.
* Para estructuras complejas, usa `TypeAlias`.

---

📌 **Consejo**: Al generar código, incluye siempre indicaciones de tipo, `docstring` y evita redacciones subjetivas en los comentarios. El objetivo es una estructura de código lo más precisa, reproducible y formalizada posible.



Este archivo se usará para configurar Gemini CLI.

Para mayor comodidad, crearemos un directorio `game`, que almacenará los archivos del proyecto, y un directorio `scenarios`, donde se almacenarán los escenarios para Gemini CLI.

El archivo scenarios/life-create-code.md contendrá instrucciones para crear el código del juego "La Vida",
el archivo scenarios/life-create-test.md - instrucciones para crear pruebas,
y el archivo scenarios/life-create-doc.md - instrucciones para crear documentación.

life-create-code.md:
```markdown
Dentro del directorio `game`, crea un archivo life.py.
Dentro, escribe una implementación del "Juego de la Vida" de Conway en Python, usando un enfoque orientado a objetos.
usa las bibliotecas: `numpy`, `pygame` (para los gráficos).


Requisitos:
1.  Crea una clase `Game`.
2.  En `__init__`, la clase debe tomar las dimensiones de la cuadrícula (ancho, alto) y crear un campo inicial aleatorio.
3.  Crea un método `step()` que actualice el estado del juego en un paso de acuerdo con las reglas:
    - Una célula viva con < 2 vecinos vivos muere (soledad).
    - Una célula viva con 2 o 3 vecinos vivos sobrevive.
    - Una célula viva con > 3 vecinos vivos muere (superpoblación).
    - Una célula muerta con exactamente 3 vecinos vivos se convierte en una célula viva (nacimiento).
4.  Crea un método `display()` o redefine `__str__` para mostrar el campo en la consola. Usa símbolos, por ejemplo '■' para una célula viva y ' ' para una célula muerta.
5.  Usa la biblioteca `numpy` para un trabajo eficiente con la cuadrícula.
6.  En el bloque `if __name__ == '__main__':`, añade un ejemplo que cree un juego y, en un bucle, ejecute una simulación con un pequeño retraso entre los pasos.
7. Para visualizar el juego, usa pygame u otra biblioteca de gráficos, si es posible.
```

---

life-create-test.md:
```markdown
Dentro del directorio `game`, usando el contexto del archivo @life.py, crea un archivo con pruebas test_life.py. Usa el framework pytest.

La prueba debe verificar la corrección de la evolución de un simple oscilador "Blinker" (tres células en una fila).

Escenario de la prueba:
1.  Importa la clase `Game` de `life`.
2.  Crea una función de prueba, por ejemplo `test_blinker_oscillation`.
3.  Dentro de la prueba, crea una instancia de `Game` con un tamaño fijo (por ejemplo, 5x5).
4.  Establece manualmente el estado inicial del campo de modo que haya una línea horizontal de tres células vivas (Blinker) en el centro.
5.  Llama al método `game.step()`.
6.  Usando `assert` y `numpy.array_equal`, comprueba que el campo ha cambiado a una línea vertical de tres células.
7.  Llama de nuevo al método `game.step()`.
8.  Comprueba que el campo ha vuelto a su estado horizontal original.
```

---

life-create-doc.md:
```markdown
Analiza los archivos @life.py y @test_life.py dentro del directorio `game` y, basándote en ellos, crea un archivo de documentación doc.md.

La estructura de la documentación debe ser la siguiente:
-   **Título:** # Proyecto "Juego de la Vida"
-   **Breve descripción:** Una explicación de qué es este proyecto (una implementación del autómata celular de Conway).
-   **Estructura de los archivos:** Una breve descripción del propósito de los archivos `life.py` y `test_life.py`.
-   **Cómo ejecutar la simulación:** Una sección con el comando para ejecutar el archivo principal (`python life.py`).
-   **Cómo ejecutar las pruebas:** Una sección con el comando para ejecutar las pruebas (`pip install pytest numpy`, y luego `pytest`).
```

La estructura de los directorios se verá así:

![1](assets/gemini_cli_3/1.png)

#### **Paso 2: Creación del código del juego "La Vida"**

Lanzamos gemini-cli en la terminal:

![2](assets/gemini_cli_3/2.png)
¡Importante! Asegúrate de que te encuentras en el directorio donde se encuentra el archivo `GEMINI.md`.

![3](assets/gemini_cli_3/3.png)

![4](assets/gemini_cli_3/4.png)

Damos permiso para crear el archivo:
![5](assets/gemini_cli_3/5.png)

Después de eso, gemini-cli generará el archivo `life.py` en el directorio `game`:
![6](assets/gemini_cli_3/6.png)

Continuamos:
```bash
Crea un entorno virtual venv, instala las dependencias necesarias y ejecuta el código del juego    
```

![7](assets/gemini_cli_3/7.png)

Damos los permisos necesarios para ejecutar los scripts
![8](assets/gemini_cli_3/8.png)

pip
![9](assets/gemini_cli_3/9.png)

y finalmente gemini-cli lanza el juego:
![10](assets/gemini_cli_3/10.png)

Paso 3: Creación de pruebas

![12](assets/gemini_cli_3/12.png)
![11](assets/gemini_cli_3/11.png)

Error
![13](assets/gemini_cli_3/13.png)

gemini-cli intenta resolver el problema
![14](assets/gemini_cli_3/14.png)

![15](assets/gemini_cli_3/15.png)

El último paso es crear la documentación
![16](assets/gemini_cli_3/16.png)

¡Voila! La documentación ha sido creada:
![17](assets/gemini_cli_3/17.png)