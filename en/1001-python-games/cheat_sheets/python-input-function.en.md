# The `input()` function
The `input()` function in Python is used to get data from the user through text input. It pauses program execution until the user enters data and presses Enter. After that, it returns the entered value as a string.

### Syntax
```python
input([prompt])
```

- `prompt` (optional): a string that is displayed to the user before input. This can be a message with an instruction, for example: `"Enter your name: "`.

### Example usage
```python
# Requesting the user's name
name = input('Enter your name: ')
print(f'Hello, {name}!')
```

**Execution result:**
```
Enter your name: Alex
Hello, Alex!
```

### Features
1. **Returns a string**  
   All data entered through `input()` is interpreted as strings. If a number is needed, it must be converted:
   ```python
   age = int(input('Enter your age: '))
   print(f'Your age: {age}')
   ```

2. **Error handling**  
   To avoid errors during conversion (for example, if the user entered text instead of a number), you can use a `try-except` block:
   ```python
   try:
       number = int(input('Enter a number: '))
       print(f'You entered the number {number}')
   except ValueError:
       print('Error: you must enter a number.')
   ```

3. **Using in loops**  
   Often `input()` is used in loops to repeatedly request data:
   ```python
   while True:
       text = input('Enter something (or "exit" to quit): ')
       if text.lower() == 'exit':
           print('Exiting program.')
           break
       print(f'You entered: {text}')
   ```

### Tips for beginners
- Make sure the data type matches your expectations (e.g., convert input to a number if needed).
- Always validate data to prevent input errors.
- Use clear and concise `prompt` messages so the user understands what is required of them.

---

  [To Table of Contents](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
