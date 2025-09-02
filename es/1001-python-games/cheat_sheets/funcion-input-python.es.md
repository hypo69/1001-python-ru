# La función `input()`
La función `input()` en Python se utiliza para obtener datos del usuario a través de la entrada de texto. Pausa la ejecución del programa hasta que el usuario introduce datos y pulsa Enter. Después de eso, devuelve el valor introducido como una cadena.

### Sintaxis
```python
input([prompt])
```

- `prompt` (opcional): una cadena que se muestra al usuario antes de la entrada. Puede ser un mensaje con una instrucción, por ejemplo: `"Introduce tu nombre: "`.

### Ejemplo de uso
```python
# Solicitar el nombre al usuario
name = input('Introduce tu nombre: ')
print(f'¡Hola, {name}!')
```

**Resultado de la ejecución:**
```
Introduce tu nombre: Alex
¡Hola, Alex!
```

### Características
1. **Devuelve una cadena**  
   Todos los datos introducidos a través de `input()` se interpretan como cadenas. Si se necesita un número, debe convertirse:
   ```python
   age = int(input('Introduce tu edad: '))
   print(f'Tu edad: {age}')
   ```

2. **Manejo de errores**  
   Para evitar errores durante la conversión (por ejemplo, si el usuario introdujo texto en lugar de un número), puede usar un bloque `try-except`:
   ```python
   try:
       number = int(input('Introduce un número: '))
       print(f'Has introducido el número {number}')
   except ValueError:
       print('Error: debes introducir un número.')
   ```

3. **Uso en bucles**  
   A menudo, `input()` se usa en bucles para solicitar datos repetidamente:
   ```python
   while True:
       text = input('Introduce algo (o "salir" para terminar): ')
       if text.lower() == 'salir':
           print('Saliendo del programa.')
           break
       print(f'Has introducido: {text}')
   ```

### Consejos para principiantes
- Asegúrate de que el tipo de datos coincide con tus expectativas (por ejemplo, convierte la entrada a un número si es necesario).
- Valida siempre los datos para evitar errores de entrada.
- Usa mensajes `prompt` claros y concisos para que el usuario entienda lo que se le pide.

---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
