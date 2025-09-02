**Variables en Python: qué son y para qué sirven**

Las variables son contenedores con nombre para almacenar datos en la memoria de la computadora. Permiten acceder a los datos por su nombre, en lugar de usarlos directamente.

Ejemplo:
```python
x = 10
y = '¡Hola, mundo!'
```
Aquí `x` e `y` son variables. `x` almacena el número 10, e `y` almacena la cadena '¡Hola, mundo!'.

### **¿Cómo funcionan las variables en Python?**
1. **Tipado dinámico**:
   En Python no es necesario especificar el tipo de variable al crearla, esto se hace automáticamente. Por ejemplo:
   ```python
   a = 42      # Número entero (int)
   b = 3.14    # Número de punto flotante (float)
   c = 'Texto' # Cadena (str)
   ```

2. **Modelo de almacenamiento de datos por referencia**:
   Las variables en Python son referencias a objetos en la memoria. Por ejemplo:
   ```python
   x = 5
   y = x  # y ahora también apunta al objeto 5
   x = 10 # x ahora apunta a otro objeto 10, e y sigue apuntando a 5
   ```

---

### **Reglas para nombrar variables**
1. **Reglas obligatorias**:
   - El nombre de una variable puede consistir en letras, dígitos y el símbolo `_`, pero no puede comenzar con un dígito.
     ✅ Ejemplos: `my_var`, `_data`, `var123`
     ❌ Incorrecto: `123var`, `my-var`
   - El nombre de una variable distingue entre mayúsculas y minúsculas.
     Ejemplo: `age` y `Age` son variables diferentes.

2. **Recomendaciones para nombres significativos**:
   - Use nombres que reflejen la esencia de los datos.
     ❌ Malo: `a = 100`, `b = 'Nombre'`
     ✅ Bueno: `salary = 100`, `username = 'Nombre'`
   - Para nombres de varias palabras, use el estilo **snake_case**:
     Ejemplo: `user_age`, `total_cost`.

3. **Palabras reservadas**:
   No se pueden usar palabras clave de Python (por ejemplo, `if`, `for`, `while`) como nombres de variables.

   Para ver una lista de palabras clave, ejecute:
   ```python
   import keyword
   print(keyword.kwlist)
   ```

---

### **Características del almacenamiento de tipos de datos**
1. **Tipos de datos de Python**:
   - **Números**: `int`, `float`, `complex`
   - **Cadenas**: `str`
   - **Listas**: `list`
   - **Tuplas**: `tuple`
   - **Conjuntos**: `set`
   - **Diccionarios**: `dict`

2. **Tipos mutables e inmutables**:
   - **Mutables**: `list`, `dict`, `set`.
     Ejemplo:
     ```python
     lst = [1, 2, 3]
     lst.append(4)  # La lista ha sido modificada
     ```
   - **Inmutables**: `int`, `float`, `str`, `tuple`.
     Ejemplo:
     ```python
     name = 'Alice'
     name[0] = 'B'  # Error, las cadenas son inmutables
     ```

3. **Función `type` para verificar el tipo**:
   ```python
   x = 10
   print(type(x))  # <class 'int'>
   ```

---

### **Consejos para principiantes**
1. Use nombres de variables significativos para que su código sea comprensible.
2. Recuerde que Python no requiere la declaración del tipo de variable, pero tenga cuidado de no confundirse con los tipos de datos.
3. Aprenda las funciones integradas para trabajar con variables, como `type()`, `id()`, y módulos, como `sys`, para comprender mejor cómo Python gestiona la memoria.

---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
