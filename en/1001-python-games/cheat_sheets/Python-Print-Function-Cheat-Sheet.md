# The `print()` function

The `print()` function in Python is used to output information to the console. It is one of the simplest and most frequently used functions, especially for debugging and displaying data. Let's consider the main aspects of its operation.

## Syntax
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Parameters:
1. **`*objects`**:
   - A list of objects to be printed. You can pass one or more values, separated by commas.
   - Example:
     ```python
     print('Hello', 'world')
     ```
     Result: `Hello world`

2. **`sep`** (default `' '`):
   - The separator between objects, if multiple are passed.
   - Example:
     ```python
     print('Hello', 'world', sep=' - ')
     ```
     Result: `Hello - world`

3. **`end`** (default `'\n'`):
   - Specifies what will be added at the end of the line. By default, it's a newline character.
   - Example:
     ```python
     print('Hello', end='!')
     ```
     Result: `Hello!`

4. **`file`**:
   - The stream where the output will be directed (by default `sys.stdout` — standard output).
   - Example: output to a file.
     ```python
     with open('output.txt', 'w') as f:
         print('Hello, file!', file=f)
     ```

5. **`flush`** (default `False`):
   - If set to `True`, it forces the output buffer to be flushed.

---

## Usage Examples

### Simple string
```python
print('Hello, world!')
```
Result: `Hello, world!`

### Outputting multiple values
```python
name = 'Anna'
age = 25
print('Name:', name, ', Age:', age)
```
Result: `Name: Anna , Age: 25`

### Customizing the separator
```python
print(1, 2, 3, sep=' -> ')
```
Result: `1 -> 2 -> 3`

### Customizing the end of the line
```python
for i in range(3):
    print(i, end=' ')
```
Result: `0 1 2`

### Using f-strings with variable name output
Starting from Python 3.8, you can use f-strings to output variable values with their names in the format `name=value`. This is useful for debugging, as it allows you to immediately see which variable and what value is being output.
```python
name = 'Ivan'
age = 30
print(f'{name=}, {age=}')
```
Result: `name='Ivan', age=30`

---

## Useful tips for beginners

1. **Debugging code**:
   Use `print()` to check variable values:
   ```python
   x = 10
   y = 20
   print('Sum:', x + y)
   ```

2. **Formatted output**:
   For outputting strings with value substitution, it's better to use formatting:
   ```python
   name = 'Ivan'
   age = 30
   print(f'My name is {name}, I am {age} years old.')
   ```

3. **Logging**:
   In larger projects, it's better to use the `logging` module for output management, but for beginners, `print()` helps quickly output data.

   ---

  [To Table of Contents](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
