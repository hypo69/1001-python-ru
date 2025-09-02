# La función `input()`
La función `input()` en Python se utiliza para obtener datos del usuario a través de la entrada de texto. Pausa la ejecución del programa hasta que el usuario ingresa datos y presiona Enter. Después de eso, devuelve el valor ingresado como una cadena.

### Sintaxis
```python
input([prompt])
```

- `prompt` (opcional): una cadena que se muestra al usuario antes de la entrada. Puede ser un mensaje con instrucciones, por ejemplo: `"Ingrese su nombre: "`.

### Ejemplo de uso
```python
# Solicitando el nombre al usuario
name = input('Ingrese su nombre: ')
print(f'¡Hola, {name}!')
```

**Resultado de la ejecución:**
```
Ingrese su nombre: Alex
¡Hola, Alex!
```

### Características
1. **Devuelve una cadena**
   Todos los datos ingresados a través de `input()` se interpretan como cadenas. Si se necesita un número, debe convertirse:
   ```python
   age = int(input('Ingrese su edad: '))
   print(f'Su edad: {age}')
   ```

2. **Manejo de errores**
   Para evitar errores durante la conversión (por ejemplo, si el usuario ingresó texto en lugar de un número), puede usar un bloque `try-except`:
   ```python
   try:
       number = int(input('Ingrese un número: '))
       print(f'Ingresó el número {number}')
   except ValueError:
       print('Error: debe ingresar un número.')
   ```

3. **Uso en bucles**
   A menudo, `input()` se usa en bucles para solicitar datos repetidamente:
   ```python
   while True:
       text = input('Ingrese algo (o "salir" para terminar): ')
       if text.lower() == 'salir':
           print('Saliendo del programa.')
           break
       print(f'Ingresó: {text}')
   ```

### Consejos para principiantes
- Asegúrese de que el tipo de datos coincida con sus expectativas (por ejemplo, convierta la entrada a un número si es necesario).
- Siempre valide los datos para evitar errores de entrada.
- Use mensajes `prompt` claros y concisos para que el usuario entienda lo que se le pide.

---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
