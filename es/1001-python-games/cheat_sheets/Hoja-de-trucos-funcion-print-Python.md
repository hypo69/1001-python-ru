# La función `print()`

La función `print()` en Python se utiliza para mostrar información en la consola. Es una de las funciones más simples y utilizadas con frecuencia, especialmente para depurar y mostrar datos. Consideremos los aspectos principales de su funcionamiento.

## Sintaxis
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Parámetros:
1. **`*objects`**:
   - Una lista de objetos que se deben imprimir. Puede pasar uno o varios valores, separados por comas.
   - Ejemplo:
     ```python
     print('Hola', 'mundo')
     ```
     Resultado: `Hola mundo`

2. **`sep`** (predeterminado `' '`):
   - El separador entre objetos, si se pasan varios.
   - Ejemplo:
     ```python
     print('Hola', 'mundo', sep=' - ')
     ```
     Resultado: `Hola - mundo`

3. **`end`** (predeterminado `''`):
   - Especifica lo que se agregará al final de la línea. Por defecto, es un salto de línea.
   - Ejemplo:
     ```python
     print('Hola', end='!')
     ```
     Resultado: `Hola!`

4. **`file`**:
   - El flujo donde se dirigirá la salida (por defecto `sys.stdout` — salida estándar).
   - Ejemplo: salida a un archivo.
     ```python
     with open('output.txt', 'w') as f:
         print('Hola, archivo!', file=f)
     ```

5. **`flush`** (predeterminado `False`):
   - Si se establece en `True`, fuerza el vaciado del búfer de salida.

---

## Ejemplos de uso

### Cadena simple
```python
print('Hello, world!')
```
Resultado: `Hello, world!`

### Imprimir varios valores
```python
name = 'Anna'
age = 25
print('Nombre:', name, ', Edad:', age)
```
Resultado: `Nombre: Anna , Edad: 25`

### Personalizar el separador
```python
print(1, 2, 3, sep=' -> ')
```
Resultado: `1 -> 2 -> 3`

### Personalizar el final de línea
```python
for i in range(3):
    print(i, end=' ')
```
Resultado: `0 1 2`

### Usar f-strings con salida de nombre de variable
A partir de Python 3.8, puede usar f-strings para mostrar los valores de las variables con sus nombres en el formato `nombre=valor`. Esto es útil para la depuración, ya que le permite ver inmediatamente qué variable y qué valor se está mostrando.
```python
name = 'Ivan'
age = 30
print(f'{name=}, {age=}')
```
Resultado: `name='Ivan', age=30`

---

## Consejos útiles para principiantes

1. **Depuración de código**:
   Use `print()` para verificar los valores de las variables:
   ```python
   x = 10
   y = 20
   print('Suma:', x + y)
   ```

2. **Salida formateada**:
   Para mostrar cadenas con sustitución de valores, es mejor usar el formato:
   ```python
   name = 'Ivan'
   age = 30
   print(f'Me llamo {name}, tengo {age} años.')
   ```

3. **Registro (Logging)**:
   En proyectos más grandes, es mejor usar el módulo `logging` para la gestión de la salida, pero al principio, `print()` ayuda a mostrar datos rápidamente.

---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
