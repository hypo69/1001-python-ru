En Python, las cadenas son uno de los tipos de datos más importantes y utilizados con frecuencia. Aquí hay una breve descripción de los diferentes tipos de cadenas y sus características:

---

### 1. **Cadenas normales**
Una cadena normal se crea usando comillas simples '`'` o dobles "`"`.

**Ejemplo:**
```python
s1 = '¡Hola, mundo!'
s2 = "¡Python es genial!"
```

Son idénticas, pero es importante ser consistente en el uso de un solo estilo.

---

### 2. **Cadenas multilínea**
Las cadenas multilínea se encierran entre comillas triples '''`'''` o """`"""`". Le permiten escribir texto en varias líneas.

**Ejemplo:**
```python
s3 = '''Esta es una cadena
en varias
líneas.'''
```

---

### 3. **f-strings (cadenas formateadas)**
Las f-strings (o cadenas formateadas) se utilizan para incrustar valores de variables y expresiones directamente dentro de una cadena. El carácter `f` se agrega antes del inicio de la cadena.

**Ejemplo:**
```python
name = 'Boris'
age = 25
s4 = f'Me llamo {name}, tengo {age} años.'
print(s4)  # Me llamo Boris, tengo 25 años.
```

La ventaja de las f-strings es que son simples y legibles.
En las nuevas versiones de Python (a partir de **3.8**), apareció una característica conveniente: el uso de expresiones como `f'{name=}'` en las f-strings. Esta construcción muestra no solo el valor de la variable, sino también su nombre, lo que es especialmente útil para la depuración.

### Ejemplo de uso de `f'{name=}'`:
```python
name = 'Boris'
age = 25

# Mostrar el nombre de la variable y su valor
print(f'{name=}, {age=}')
# Resultado: name='Boris', age=25
```

### Características:
1. **Indicación automática del nombre de la variable**: 
   Python sustituye automáticamente el nombre de la variable y su valor, separándolos con el símbolo `=`. 
   
2. **Funciona con expresiones**: 
   Puede usar expresiones dentro de una f-string, y también se mostrarán. 

**Ejemplo:**
```python
x = 10
y = 5
print(f'{x + y=}')
# Resultado: x + y=15
```

3. **Aplicación a funciones de cadena**: 
   Puede mostrar el resultado de métodos u operaciones en cadenas. 

**Ejemplo:**
```python
s = 'Python'
print(f'{s.upper()=}')
# Resultado: s.upper()='PYTHON'
```

### Por qué esto es útil:
- **Depuración de código**: Comprobar rápidamente los valores de las variables y expresiones.
- **Legibilidad**: Muestra claramente a qué variable pertenece el valor.


---


### 4. **r-strings (cadenas sin formato)**
Las r-strings (raw strings) se crean agregando el carácter `r` antes de la cadena. Se utilizan para trabajar con caracteres que normalmente se interpretan como especiales, como los caracteres de nueva línea (`\n`) o tabulaciones (`\t`).

**Ejemplo:**
```python
s5 = r'C:\new_folder\test'
print(s5)  # C:\new_folder\test
```

Sin `r`, esta cadena se interpretaría con `\n` reemplazado por un salto de línea.

---


### 5. **u-strings (cadenas Unicode)**
Las u-strings eran importantes en Python 2 para trabajar con Unicode, pero en Python 3, las cadenas son Unicode por defecto, por lo que agregar `u` ya no es necesario.

**Ejemplo:**
```python
s6 = u'¡Hola, mundo!'
```

---


### 6. **b-strings (cadenas de bytes)**
Las cadenas de bytes se utilizan para trabajar con datos binarios. Estas cadenas comienzan con `b`. No admiten caracteres Unicode, solo bytes.

**Ejemplo:**
```python
# Cadena de bytes que representa el encabezado de un archivo PNG
image_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

# Comprobar que los datos coinciden con el formato PNG
if image_bytes.startswith(b'\x89PNG'):
    print('Esta es una imagen PNG.')
else:
    print('Formato desconocido.')

```

---


### 7. **Cadenas con escape**
Para incluir caracteres especiales en una cadena, se utilizan secuencias de escape con una barra invertida (`\`).

**Ejemplo:**
```python
s8 = 'Esta es una cadena con comillas: \'simples\' y \"dobles\".'
```

---


### 8. **Combinación de f-strings y r-strings**
Puede combinar tipos de cadenas. Por ejemplo, f-strings y cadenas sin formato: 

**Ejemplo:**
```python
path = 'new_folder'
s9 = fr'C:\{path}\test'
print(s9)  # C:\new_folder\test
```

---


### Resumen 
En Python, las cadenas son flexibles y convenientes. La elección del tipo de cadena depende de la tarea: 
- Para texto normal — '`'` o "`"`.
- Para texto multilínea — '''`'''` o """`"""`".
- Para sustitución de valores — `f`.
- Para rutas o expresiones regulares — `r`.
- Para datos binarios — `b`.

---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
